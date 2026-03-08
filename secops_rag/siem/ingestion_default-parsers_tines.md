# Collect Tines audit Logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tines/  
**Scraped:** 2026-03-05T09:29:18.632140Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tines audit Logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tines audit Logs to Google Security Operations using Google Cloud Storage.
Tines is a no-code automation platform that enables security teams to build workflows and automate security operations. Tines Audit Logs provide visibility into user actions, configuration changes, and system events within the Tines platform.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Tines
Get the Tines URL
In your browser, open the Tines UI for your tenant.
Copy the domain from the address bar — you'll use it as
TINES_BASE_URL
.
Format:
https://<tenant-domain>
(for example,
https://<tenant-domain>.tines.com
).
Create a Tines Service API key (recommended) or Personal API key
Values to save for later steps:
TINES_BASE_URL
— For example,
https://<domain>.tines.com
TINES_API_KEY
— The token you create in the following steps
Option 1 - Service API key (recommended)
Go to the
Navigation menu
>
API keys
.
Click
+ New key
.
Select
Service API key
.
Enter a descriptive name (for example,
SecOps Audit Logs
).
Click
Create
.
Copy the generated token immediately and save it securely — you'll use it as
TINES_API_KEY
.
Option 2 - Personal API key (if Service keys are not available)
Go to the
Navigation menu
>
API keys
.
Click
+ New key
.
Select
Personal API key
.
Enter a descriptive name.
Click
Create
.
Copy the generated token and save it securely.
Grant the Audit Log Read permission
Sign in as a Tenant Owner (or request one to do this).
Go to
Settings
>
Admin
>
User administration
(or click your team name in the upper left menu and select
Users
).
Find the service account user associated with your Service API key (it will have the same name as your API key). If using a Personal API key, find your own user account instead.
Click the user to open their profile.
In the
Tenant permissions
section, enable
AUDIT_LOG_READ
.
Click
Save
.
Verify permissions
To verify the account has the required permissions:
Sign in to Tines.
Go to
Settings
>
Monitoring
>
Audit logs
.
If you can see audit log entries, you have the required permissions.
If you cannot see this option, contact your Tenant Owner to grant
AUDIT_LOG_READ
permission.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
TINES_BASE_URL
=
"https://<tenant-domain>.tines.com"
TINES_API_KEY
=
"<your-api-key>"
# Test API access
curl
-X
GET
"
${
TINES_BASE_URL
}
/api/v1/audit_logs?per_page=1"
\
-H
"Authorization: Bearer
${
TINES_API_KEY
}
"
\
-H
"Content-Type: application/json"
You should receive a JSON response with audit log entries.
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
tines-audit-logs
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
tines-audit-to-gcs-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Tines Audit Logs
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
tines-audit-to-gcs-sa@PROJECT_ID.iam.gserviceaccount.com
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
tines-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Tines API and writes them to GCS.
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
tines-audit-to-gcs
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
, choose the Pub/Sub topic (
tines-audit-trigger
).
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
: Select the service account (
tines-audit-to-gcs-sa
).
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
Description
GCS_BUCKET
tines-audit-logs
GCS bucket name
GCS_PREFIX
tines/audit/
Prefix for log files
STATE_KEY
tines/audit/state.json
State file path
TINES_BASE_URL
https://your-tenant.tines.com
API base URL
TINES_API_KEY
your-tines-api-key
API key
LOOKBACK_SECONDS
3600
Initial lookback period
PAGE_SIZE
500
Records per page
MAX_PAGES
20
Maximum pages per run
HTTP_TIMEOUT
60
HTTP request timeout
HTTP_RETRIES
3
HTTP retry attempts
In the
Variables & Secrets
section, scroll down to
Requests
:
Request timeout
: Enter
600
seconds (10 minutes).
Go to the
Settings
tab:
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
timezone
,
timedelta
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
# Environment variables
GCS_BUCKET
=
os
.
environ
.
get
(
'GCS_BUCKET'
)
GCS_PREFIX
=
os
.
environ
.
get
(
'GCS_PREFIX'
,
'tines/audit/'
)
STATE_KEY
=
os
.
environ
.
get
(
'STATE_KEY'
,
'tines/audit/state.json'
)
TINES_BASE_URL
=
os
.
environ
.
get
(
'TINES_BASE_URL'
)
TINES_API_KEY
=
os
.
environ
.
get
(
'TINES_API_KEY'
)
LOOKBACK_SECONDS
=
int
(
os
.
environ
.
get
(
'LOOKBACK_SECONDS'
,
'3600'
))
PAGE_SIZE
=
int
(
os
.
environ
.
get
(
'PAGE_SIZE'
,
'500'
))
MAX_PAGES
=
int
(
os
.
environ
.
get
(
'MAX_PAGES'
,
'20'
))
HTTP_TIMEOUT
=
int
(
os
.
environ
.
get
(
'HTTP_TIMEOUT'
,
'60'
))
HTTP_RETRIES
=
int
(
os
.
environ
.
get
(
'HTTP_RETRIES'
,
'3'
))
def
parse_datetime
(
value
:
str
)
-
>
datetime
:
"""Parse ISO datetime string to datetime object."""
if
value
.
endswith
(
"Z"
):
value
=
value
[:
-
1
]
+
"+00:00"
return
datetime
.
fromisoformat
(
value
)
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Tines Audit Logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
TINES_BASE_URL
,
TINES_API_KEY
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
GCS_BUCKET
)
# Load state
state
=
load_state
(
bucket
,
STATE_KEY
)
# Determine time window
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
last_time
=
None
if
isinstance
(
state
,
dict
)
and
state
.
get
(
"last_event_time"
):
try
:
last_time
=
parse_datetime
(
state
[
"last_event_time"
])
# Overlap by 2 minutes to catch any delayed events
last_time
=
last_time
-
timedelta
(
minutes
=
2
)
except
Exception
as
e
:
print
(
f
"Warning: Could not parse last_event_time:
{
e
}
"
)
if
last_time
is
None
:
last_time
=
now
-
timedelta
(
seconds
=
LOOKBACK_SECONDS
)
print
(
f
"Fetching logs from
{
last_time
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
"
)
# Fetch logs
records
,
newest_event_time
=
fetch_logs
(
api_base
=
TINES_BASE_URL
,
api_key
=
TINES_API_KEY
,
start_time
=
last_time
,
page_size
=
PAGE_SIZE
,
max_pages
=
MAX_PAGES
,
)
if
not
records
:
print
(
"No new log records found."
)
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
return
# Write to GCS as NDJSON
timestamp
=
now
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
object_key
=
f
"
{
GCS_PREFIX
}
/logs_
{
timestamp
}
.ndjson"
blob
=
bucket
.
blob
(
object_key
)
ndjson
=
'
\n
'
.
join
([
json
.
dumps
(
record
,
ensure_ascii
=
False
)
for
record
in
records
])
+
'
\n
'
blob
.
upload_from_string
(
ndjson
,
content_type
=
'application/x-ndjson'
)
print
(
f
"Wrote
{
len
(
records
)
}
records to gs://
{
GCS_BUCKET
}
/
{
object_key
}
"
)
# Update state with newest event time
if
newest_event_time
:
save_state
(
bucket
,
STATE_KEY
,
newest_event_time
)
else
:
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
print
(
f
"Successfully processed
{
len
(
records
)
}
records"
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
"Warning: Could not load state:
{
e
}
"
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
last_event_time_iso
:
str
):
"""Save the last event timestamp to GCS state file."""
try
:
state
=
{
'last_event_time'
:
last_event_time_iso
}
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
,
indent
=
2
),
content_type
=
'application/json'
)
print
(
f
"Saved state: last_event_time=
{
last_event_time_iso
}
"
)
except
Exception
as
e
:
print
(
f
"Warning: Could not save state:
{
e
}
"
)
def
fetch_logs
(
api_base
:
str
,
api_key
:
str
,
start_time
:
datetime
,
page_size
:
int
,
max_pages
:
int
):
"""
Fetch logs from Tines API with pagination and rate limiting.
Args:
api_base: API base URL
api_key: Tines API key
start_time: Start time for log query
page_size: Number of records per page
max_pages: Maximum pages to fetch
Returns:
Tuple of (records list, newest_event_time ISO string)
"""
base_url
=
api_base
.
rstrip
(
'/'
)
endpoint
=
f
"
{
base_url
}
/api/v1/audit_logs"
headers
=
{
'Authorization'
:
f
'Bearer
{
api_key
}
'
,
'Accept'
:
'application/json'
,
'Content-Type'
:
'application/json'
,
'User-Agent'
:
'GoogleSecOps-TinesCollector/1.0'
}
records
=
[]
newest_time
=
None
page_num
=
1
backoff
=
1.0
while
page_num
<
=
max_pages
:
# Build URL with query parameters
params
=
{
'page'
:
page_num
,
'per_page'
:
page_size
}
param_str
=
'&'
.
join
([
f
"
{
k
}
=
{
v
}
"
for
k
,
v
in
params
.
items
()])
url
=
f
"
{
endpoint
}
?
{
param_str
}
"
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
HTTP_TIMEOUT
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
"Rate limited (429). Retrying after
{
retry_after
}
s..."
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
"HTTP Error:
{
response
.
status
}
"
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
"Response body:
{
response_text
}
"
)
return
[],
None
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
# Extract results
page_results
=
[]
if
isinstance
(
data
,
dict
):
page_results
=
data
.
get
(
'audit_logs'
,
[])
elif
isinstance
(
data
,
list
):
page_results
=
data
if
not
page_results
:
print
(
f
"No more results (empty page)"
)
break
# Filter by start_time
filtered_results
=
[]
for
event
in
page_results
:
try
:
event_time
=
event
.
get
(
'created_at'
)
if
event_time
:
event_dt
=
parse_datetime
(
event_time
)
if
event_dt
>
=
start_time
:
filtered_results
.
append
(
event
)
# Track newest event time
if
newest_time
is
None
or
event_dt
>
parse_datetime
(
newest_time
):
newest_time
=
event_time
except
Exception
as
e
:
print
(
f
"Warning: Could not parse event time:
{
e
}
"
)
filtered_results
.
append
(
event
)
print
(
f
"Page
{
page_num
}
: Retrieved
{
len
(
page_results
)
}
events,
{
len
(
filtered_results
)
}
after filtering"
)
records
.
extend
(
filtered_results
)
# Check for more results
if
isinstance
(
data
,
dict
):
meta
=
data
.
get
(
'meta'
,
{})
next_page
=
meta
.
get
(
'next_page_number'
)
if
not
next_page
:
print
(
"No more pages (no next_page_number)"
)
break
page_num
=
next_page
else
:
# If response is a list, check if we got fewer results than requested
if
len
(
page_results
)
<
page_size
:
print
(
f
"Reached last page (size=
{
len
(
page_results
)
}
< limit=
{
page_size
}
)"
)
break
page_num
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
"Error fetching logs:
{
e
}
"
)
if
page_num
<
=
HTTP_RETRIES
:
print
(
f
"Retrying... (attempt
{
page_num
}
/
{
HTTP_RETRIES
}
)"
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
continue
return
[],
None
print
(
f
"Retrieved
{
len
(
records
)
}
total records from
{
page_num
}
pages"
)
return
records
,
newest_time
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
Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
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
tines-audit-hourly
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
Select the Pub/Sub topic (
tines-audit-trigger
)
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
Test the integration
In the
Cloud Scheduler
console, find your job (
tines-audit-hourly
).
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click on your function name (
tines-audit-to-gcs
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
Page 1: Retrieved X events
Wrote X records to gs://bucket-name/tines/audit/logs_YYYYMMDD_HHMMSS.ndjson
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
tines-audit-logs
).
Navigate to the
tines/audit/
folder.
Verify that a new
.ndjson
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables
HTTP 403
: Verify account has AUDIT_LOG_READ permission
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set
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
Tines Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Tines
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
Click your bucket name (
tines-audit-logs
).
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
Configure a feed in Google SecOps to ingest Tines Audit Logs
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
Tines Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Tines
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://tines-audit-logs/tines/audit/
Replace:
tines-audit-logs
: Your GCS bucket name.
tines/audit/
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
