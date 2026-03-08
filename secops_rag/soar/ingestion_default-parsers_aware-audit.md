# Collect Aware audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-audit/  
**Scraped:** 2026-03-05T09:50:24.495813Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Aware audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Aware audit logs to Google Security Operations using Google Cloud Storage. Aware is a collaboration intelligence platform that provides insights and governance for enterprise collaboration tools.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Aware tenant
Collect Aware API prerequisites
Sign in to the
Aware Admin Console
.
Go to
System Settings
>
Integrations
>
API Tokens
.
Click
+ API Token
and grant
Audit Logs Read-only
permission.
Copy and save in a secure location the following details:
API Token
API Base URL
: The endpoint is
https://api.aware.work/external/system/auditlogs/v1
Create Google Cloud Storage bucket
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
aware-audit-logs
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location (for example,
us-central1
)
Storage class
Standard (recommended for frequently accessed logs)
Access control
Uniform (recommended)
Protection tools
Optional: Enable object versioning or retention policy
Click
Create
.
Create service account for Cloud Run function
The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.
Create service account
In the
GCP Console
, go to
IAM & Admin
>
Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter
aware-audit-poller-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Aware audit logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
Click
Select a role
.
Search for and select
Storage Object Admin
.
Click
+ Add another role
.
Search for and select
Cloud Run Invoker
.
Click
+ Add another role
.
Search for and select
Cloud Functions Invoker
.
Click
Continue
.
Click
Done
.
These roles are required for:
Storage Object Admin
: Write logs to GCS bucket and manage state files
Cloud Run Invoker
: Allow Pub/Sub to invoke the function
Cloud Functions Invoker
: Allow function invocation
Grant IAM permissions on GCS bucket
Grant the service account write permissions on the GCS bucket:
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
aware-audit-poller-sa@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create Pub/Sub topic
Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.
In the
GCP Console
, go to
Pub/Sub
>
Topics
.
Click
Create topic
.
Provide the following configuration details:
Topic ID
: Enter
aware-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Aware API and writes them to GCS.
In the
GCP Console
, go to
Cloud Run
.
Click
Create service
.
Select
Function
(use an inline editor to create a function).
In the
Configure
section, provide the following configuration details:
Setting
Value
Service name
aware-audit-poller
Region
Select region matching your GCS bucket (for example,
us-central1
)
Runtime
Select
Python 3.12
or later
In the
Trigger (optional)
section:
Click
+ Add trigger
.
Select
Cloud Pub/Sub
.
In
Select a Cloud Pub/Sub topic
, choose the topic
aware-audit-trigger
.
Click
Save
.
In the
Authentication
section:
Select
Require authentication
.
Check
Identity and Access Management (IAM)
.
Scroll down and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select the service account
aware-audit-poller-sa
.
Go to the
Containers
tab:
Click
Variables & Secrets
.
Click
+ Add variable
for each environment variable:
Variable Name
Example Value
GCS_BUCKET
aware-audit-logs
GCS_PREFIX
aware/audit/
STATE_KEY
aware/state.json
AWARE_API_TOKEN
your-aware-api-token
MAX_PER_PAGE
500
Scroll down in the
Variables & Secrets
tab to
Requests
:
Request timeout
: Enter
600
seconds (10 minutes).
Go to the
Settings
tab in
Containers
:
In the
Resources
section:
Memory
: Select
512 MiB
or higher.
CPU
: Select
1
.
Click
Done
.
Scroll to
Execution environment
:
Select
Default
(recommended).
In the
Revision scaling
section:
Minimum number of instances
: Enter
0
.
Maximum number of instances
: Enter
100
(or adjust based on expected load).
Click
Create
.
Wait for the service to be created (1-2 minutes).
After the service is created, the
inline code editor
opens automatically.
Add function code
Enter
main
in
Function entry point
In the inline code editor, create two files:
First file:
main.py:
import
functions_framework
from
google.cloud
import
storage
import
json
import
os
import
urllib3
from
datetime
import
datetime
,
timedelta
,
timezone
import
gzip
import
io
import
time
# Initialize HTTP client with timeouts
http
=
urllib3
.
PoolManager
(
timeout
=
urllib3
.
Timeout
(
connect
=
5.0
,
read
=
30.0
),
retries
=
False
,
)
# Initialize Storage client
storage_client
=
storage
.
Client
()
AWARE_ENDPOINT
=
"https://api.aware.work/external/system/auditlogs/v1"
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Aware audit logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
# Get environment variables
bucket_name
=
os
.
environ
.
get
(
'GCS_BUCKET'
)
prefix
=
os
.
environ
.
get
(
'GCS_PREFIX'
,
'aware/audit/'
)
state_key
=
os
.
environ
.
get
(
'STATE_KEY'
,
'aware/state.json'
)
api_token
=
os
.
environ
.
get
(
'AWARE_API_TOKEN'
)
max_per_page
=
int
(
os
.
environ
.
get
(
'MAX_PER_PAGE'
,
'500'
))
if
not
all
([
bucket_name
,
api_token
]):
print
(
'Error: Missing required environment variables'
)
return
try
:
# Get GCS bucket
bucket
=
storage_client
.
bucket
(
bucket_name
)
# Load state
state
=
load_state
(
bucket
,
state_key
)
tz_utc
=
timezone
.
utc
now
=
datetime
.
now
(
tz
=
tz_utc
)
start_date
=
(
datetime
.
fromisoformat
(
state
[
'last_date'
])
.
date
()
if
'last_date'
in
state
else
(
now
-
timedelta
(
days
=
1
))
.
date
()
)
end_date
=
now
.
date
()
total
=
0
day
=
start_date
backoff
=
1.0
while
day
<
=
end_date
:
day_str
=
day
.
strftime
(
'%Y-%m-
%d
'
)
params
=
{
'filter'
:
f
'startDate:
{
day_str
}
,endDate:
{
day_str
}
'
,
'limit'
:
str
(
max_per_page
)
}
offset
=
1
out
=
io
.
BytesIO
()
with
gzip
.
GzipFile
(
filename
=
'aware_audit.jsonl'
,
mode
=
'wb'
,
fileobj
=
out
)
as
gz
:
wrote_any
=
False
while
True
:
# Build query URL
query_params
=
{
**
params
,
'offset'
:
str
(
offset
)}
query_string
=
'&'
.
join
([
f
'
{
k
}
=
{
v
}
'
for
k
,
v
in
query_params
.
items
()])
url
=
f
'
{
AWARE_ENDPOINT
}
?
{
query_string
}
'
# Make API request
headers
=
{
'X-Aware-Api-Key'
:
api_token
}
try
:
response
=
http
.
request
(
'GET'
,
url
,
headers
=
headers
,
timeout
=
30.0
)
# Handle rate limiting with exponential backoff
if
response
.
status
==
429
:
retry_after
=
int
(
response
.
headers
.
get
(
'Retry-After'
,
str
(
int
(
backoff
))))
print
(
f
'Rate limited (429). Retrying after
{
retry_after
}
s...'
)
time
.
sleep
(
retry_after
)
backoff
=
min
(
backoff
*
2
,
30.0
)
continue
backoff
=
1.0
if
response
.
status
!=
200
:
print
(
f
'Error: API returned status
{
response
.
status
}
'
)
break
payload
=
json
.
loads
(
response
.
data
.
decode
(
'utf-8'
))
items
=
(
payload
.
get
(
'value'
)
or
{})
.
get
(
'auditLogData'
)
or
[]
if
not
items
:
break
for
item
in
items
:
gz
.
write
((
json
.
dumps
(
item
,
separators
=
(
','
,
':'
))
+
'
\n
'
)
.
encode
(
'utf-8'
))
total
+=
1
wrote_any
=
True
offset
+=
1
except
Exception
as
e
:
print
(
f
'Error fetching page:
{
str
(
e
)
}
'
)
break
if
wrote_any
:
blob_name
=
f
"
{
prefix
}{
day
.
strftime
(
'%Y/%m/
%d
'
)
}
/aware_audit_
{
now
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
}
.jsonl.gz"
blob
=
bucket
.
blob
(
blob_name
)
blob
.
upload_from_string
(
out
.
getvalue
(),
content_type
=
'application/json'
,
content_encoding
=
'gzip'
)
print
(
f
'Wrote
{
total
}
logs to
{
blob_name
}
'
)
save_state
(
bucket
,
state_key
,
{
'last_date'
:
day
.
isoformat
()})
day
+=
timedelta
(
days
=
1
)
print
(
f
'Successfully processed
{
total
}
logs'
)
except
Exception
as
e
:
print
(
f
'Error processing logs:
{
str
(
e
)
}
'
)
raise
def
load_state
(
bucket
,
key
):
"""Load state from GCS."""
try
:
blob
=
bucket
.
blob
(
key
)
if
blob
.
exists
():
state_data
=
blob
.
download_as_text
()
return
json
.
loads
(
state_data
)
except
Exception
as
e
:
print
(
f
'Warning: Could not load state:
{
str
(
e
)
}
'
)
return
{}
def
save_state
(
bucket
,
key
,
state
):
"""Save state to GCS."""
try
:
blob
=
bucket
.
blob
(
key
)
blob
.
upload_from_string
(
json
.
dumps
(
state
),
content_type
=
'application/json'
)
except
Exception
as
e
:
print
(
f
'Warning: Could not save state:
{
str
(
e
)
}
'
)
Second file:
requirements.txt:
functions
-
framework
==
3
.*
google
-
cloud
-
storage
==
2
.*
urllib3
>
=
2.0
.
0
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
In the
GCP Console
, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Setting
Value
Name
aware-audit-poller-hourly
Region
Select same region as Cloud Run function
Frequency
0 * * * *
(every hour, on the hour)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select the topic
aware-audit-trigger
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose frequency based on log volume and latency requirements:
Frequency
Cron Expression
Use Case
Every 5 minutes
*/5 * * * *
High-volume, low-latency
Every 15 minutes
*/15 * * * *
Medium volume
Every hour
0 * * * *
Standard (recommended)
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
0 0 * * *
Historical data collection
Test the scheduler job
In the
Cloud Scheduler
console, find your job.
Click
Force run
to trigger manually.
Wait a few seconds and go to
Cloud Run
>
Services
>
aware-audit-poller
>
Logs
.
Verify the function executed successfully.
Check the GCS bucket to confirm logs were written.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Get the service account email
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Aware Audit logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Aware Audit
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle
-
12345678
@chronicle
-
gcp
-
prod
.
iam
.
gserviceaccount
.
com
Copy this email address for use in the next step.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email.
Assign roles
: Select
Storage Object Viewer
.
Click
Save
.
Configure a feed in Google SecOps to ingest Aware Audit logs
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Aware Audit logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Aware Audit
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://aware-audit-logs/aware/audit/
Replace:
aware-audit-logs
: Your GCS bucket name.
aware/audit/
: Prefix/folder path where logs are stored.
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Need more help?
Get answers from Community members and Google SecOps professionals.
