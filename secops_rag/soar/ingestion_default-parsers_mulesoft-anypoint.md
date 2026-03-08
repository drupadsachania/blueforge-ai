# Collect MuleSoft Anypoint platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mulesoft-anypoint/  
**Scraped:** 2026-03-05T09:58:23.938358Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect MuleSoft Anypoint platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest audit-trail events from MuleSoft Anypoint platform logs to Google Security Operations using Google Cloud Storage.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Permissions to create service accounts
Privileged access to MuleSoft Anypoint Platform
Get the MuleSoft Organization ID
Sign in to the
Anypoint Platform
.
Go to
Access Management
>
Organizations
.
In the
Business Groups
table, click your organization's name.
Copy the
Organization ID
(for example,
0a12b3c4-d5e6-789f-1021-1a2b34cd5e6f
).
Alternatively, go to
MuleSoft Business Groups
and copy the ID from the URL.
Create the MuleSoft Connected App
Sign in to the
Anypoint Platform
.
Go to
Access Management
>
Connected Apps
>
Create App
.
Provide the following configuration details:
App name
: Enter a unique name (for example,
Google SecOps export
).
Select
App acts on its own behalf (client credentials)
.
Click
Add scopes
>
Audit Log Viewer
>
Next
.
Select every Business Group whose logs you need.
Click
Next
>
Add scopes
.
Click
Save
and copy the
Client ID
and
Client Secret
.
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
mulesoft-audit-logs
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
The Cloud Run function needs a service account with permissions to write to GCS bucket.
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
mulesoft-logs-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect MuleSoft Anypoint logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section:
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
mulesoft-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
mulesoft-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from MuleSoft Anypoint API and writes them to GCS.
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
mulesoft-audit-collector
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
mulesoft-audit-trigger
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
mulesoft-logs-collector-sa
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
MULE_ORG_ID
your_org_id
CLIENT_ID
your_client_id
CLIENT_SECRET
your_client_secret
GCS_BUCKET
mulesoft-audit-logs
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
uuid
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
# MuleSoft API endpoints
TOKEN_URL
=
"https://anypoint.mulesoft.com/accounts/api/v2/oauth2/token"
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch MuleSoft audit logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
# Get environment variables
org_id
=
os
.
environ
.
get
(
'MULE_ORG_ID'
)
client_id
=
os
.
environ
.
get
(
'CLIENT_ID'
)
client_secret
=
os
.
environ
.
get
(
'CLIENT_SECRET'
)
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
if
not
all
([
org_id
,
client_id
,
client_secret
,
bucket_name
]):
print
(
'Error: Missing required environment variables'
)
return
query_url
=
f
"https://anypoint.mulesoft.com/audit/v2/organizations/
{
org_id
}
/query"
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
# Get OAuth token
token
=
get_token
(
client_id
,
client_secret
)
# Calculate time range (last 24 hours)
now
=
datetime
.
now
(
timezone
.
utc
)
.
replace
(
microsecond
=
0
)
start
=
now
-
timedelta
(
days
=
1
)
print
(
f
'Fetching audit logs from
{
start
.
isoformat
()
}
to
{
now
.
isoformat
()
}
'
)
# Fetch audit logs
events
=
list
(
fetch_audit
(
query_url
,
token
,
start
,
now
))
# Upload to GCS
if
events
:
upload_to_gcs
(
bucket
,
events
,
start
)
print
(
f
'Uploaded
{
len
(
events
)
}
events'
)
else
:
print
(
'No events in the last 24 hours'
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
get_token
(
client_id
,
client_secret
):
"""Get OAuth 2.0 access token from MuleSoft."""
data
=
{
'grant_type'
:
'client_credentials'
,
'client_id'
:
client_id
,
'client_secret'
:
client_secret
}
encoded_data
=
urllib3
.
request
.
urlencode
(
data
)
.
encode
(
'utf-8'
)
backoff
=
1.0
max_retries
=
3
for
attempt
in
range
(
max_retries
):
try
:
response
=
http
.
request
(
'POST'
,
TOKEN_URL
,
body
=
encoded_data
,
headers
=
{
'Content-Type'
:
'application/x-www-form-urlencoded'
}
)
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
'Rate limited (429) on token request. Retrying after
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
if
response
.
status
!=
200
:
raise
Exception
(
f
'Failed to get token:
{
response
.
status
}
-
{
response
.
data
.
decode
()
}
'
)
token_data
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
return
token_data
[
'access_token'
]
except
Exception
as
e
:
if
attempt
==
max_retries
-
1
:
raise
print
(
f
'Token request failed (attempt
{
attempt
+
1
}
/
{
max_retries
}
):
{
e
}
'
)
time
.
sleep
(
backoff
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
raise
Exception
(
'Failed to get token after maximum retries'
)
def
fetch_audit
(
query_url
,
token
,
start
,
end
):
"""Fetch audit logs from MuleSoft API with pagination."""
headers
=
{
'Authorization'
:
f
'Bearer
{
token
}
'
,
'Content-Type'
:
'application/json'
}
body
=
{
'startDate'
:
f
"
{
start
.
isoformat
(
timespec
=
'milliseconds'
)
}
Z"
,
'endDate'
:
f
"
{
end
.
isoformat
(
timespec
=
'milliseconds'
)
}
Z"
,
'limit'
:
200
,
'offset'
:
0
,
'ascending'
:
False
}
backoff
=
1.0
while
True
:
try
:
response
=
http
.
request
(
'POST'
,
query_url
,
body
=
json
.
dumps
(
body
)
.
encode
(
'utf-8'
),
headers
=
headers
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
'HTTP Error:
{
response
.
status
}
'
)
response_text
=
response
.
data
.
decode
(
'utf-8'
)
print
(
f
'Response body:
{
response_text
}
'
)
break
data
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
if
not
data
.
get
(
'data'
):
break
yield from
data
[
'data'
]
body
[
'offset'
]
+=
body
[
'limit'
]
except
Exception
as
e
:
print
(
f
'Error fetching audit logs:
{
e
}
'
)
break
def
upload_to_gcs
(
bucket
,
events
,
timestamp
):
"""Upload events to GCS as compressed JSON."""
import
gzip
import
io
# Create blob name with timestamp and UUID
blob_name
=
f
"
{
timestamp
.
strftime
(
'%Y/%m/
%d
'
)
}
/mulesoft-audit-
{
uuid
.
uuid4
()
}
.json.gz"
# Compress events
buf
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
fileobj
=
buf
,
mode
=
'w'
)
as
gz
:
for
event
in
events
:
gz
.
write
((
json
.
dumps
(
event
)
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
buf
.
seek
(
0
)
# Upload to GCS
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
upload_from_file
(
buf
,
content_type
=
'application/gzip'
)
print
(
f
'Uploaded to gs://
{
bucket
.
name
}
/
{
blob_name
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
Important considerations
Rate limiting:
The Audit Log Query endpoint applies rate limits per IP in the three control planes. The US control plane allows 700 requests per minute per IP, while EU and Gov control planes allow 40 requests per minute per IP. The function implements exponential backoff to handle rate limiting automatically.
Token expiration:
Access tokens usually expire about 30 to 60 minutes after being issued. The function requests a new token for each execution. For production deployments with frequent executions, consider implementing token caching with refresh logic.
Audit log retention:
Audit logs have a default retention period of one year. If your organization was created before July 10, 2023 and you didn't manually change the retention period, the retention period is six years. Download logs periodically if you need to retain them beyond the configured retention period.
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
daily-mulesoft-audit-export
Region
Select same region as Cloud Run function
Frequency
0 2 * * *
(runs daily at 02:00 UTC)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select the topic
mulesoft-audit-trigger
Message body
{}
(empty JSON object)
Click
Create
.
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
mulesoft-audit-collector
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
MuleSoft Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Mulesoft
as the
Log type
.
Click
Get Service Account
. A unique service account email is displayed, for example:
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
Configure a feed in Google SecOps to ingest the MuleSoft logs
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
MuleSoft Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Mulesoft
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI:
gs://mulesoft-audit-logs/
Replace
mulesoft-audit-logs
with the actual name of the bucket.
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
