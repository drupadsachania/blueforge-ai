# Collect Swimlane Platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swimlane/  
**Scraped:** 2026-03-05T09:28:38.082744Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Swimlane Platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest Swimlane Platform logs to Google Security Operations using Google Cloud Storage. Swimlane Platform is a security orchestration, automation, and response (SOAR) platform that provides audit logging capabilities for tracking user activities, configuration changes, and system events across accounts and tenants.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Swimlane Platform with Account Admin permissions to access audit logs
Swimlane Platform instance URL and account credentials
Collect Swimlane Platform credentials
Get Swimlane Platform instance URL
Sign in to your
Swimlane Platform
instance.
Note your instance URL from the browser address bar.
Format:
https://<region>.swimlane.app
(for example,
https://us.swimlane.app
or
https://eu.swimlane.app
)
Example: If you access Swimlane at
https://us.swimlane.app/workspace
, your base URL is
https://us.swimlane.app
Create Personal Access Token
Sign in to the
Swimlane Platform
as an Account Admin.
Go to
Profile Options
.
Click
Profile
to open the profile editor.
Navigate to the
Personal Access Token
section.
Click
Generate token
to create a new Personal Access Token.
Copy the token immediately and store it securely (it won't be shown again).
Get Account ID
Contact your Swimlane administrator if you don't know your Account ID. The Account ID is required for the Audit Log API path.
Record the following details for the integration:
Personal Access Token (PAT)
: Used in the
Private-Token
header for API calls.
Account ID
: Required for the Audit Log API path
/api/public/audit/account/{ACCOUNT_ID}/auditlogs
.
Base URL
: Your Swimlane domain (for example,
https://eu.swimlane.app
,
https://us.swimlane.app
).
Verify permissions
To verify your account has the required permissions to access audit logs:
Sign in to
Swimlane Platform
.
Confirm you have Account Admin access.
Contact your Swimlane administrator if you cannot access audit log features.
Test API access
Before proceeding with the integration, verify your API credentials work correctly:
# Replace with your actual credentials
SWIMLANE_BASE_URL
=
"https://<region>.swimlane.app"
SWIMLANE_ACCOUNT_ID
=
"<your-account-id>"
SWIMLANE_PAT_TOKEN
=
"<your-personal-access-token>"
# Test API access
curl
-v
-X
GET
"
${
SWIMLANE_BASE_URL
}
/api/public/audit/account/
${
SWIMLANE_ACCOUNT_ID
}
/auditlogs?pageNumber=1&pageSize=10"
\
-H
"Private-Token:
${
SWIMLANE_PAT_TOKEN
}
"
\
-H
"Accept: application/json"
Expected response: HTTP 200 with JSON containing audit logs.
If you receive errors:
HTTP 401
: Verify your Personal Access Token is correct
HTTP 403
: Verify your account has Account Admin permissions
HTTP 404
: Verify the Account ID and base URL are correct
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
swimlane-audit
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
swimlane-audit-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Swimlane Platform logs
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
swimlane-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
swimlane-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Swimlane Platform API and writes them to GCS.
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
swimlane-audit-collector
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
swimlane-audit-trigger
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
swimlane-audit-collector-sa
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
swimlane-audit
GCS bucket name
GCS_PREFIX
swimlane/audit/
Prefix for log files
STATE_KEY
swimlane/audit/state.json
State file path
SWIMLANE_BASE_URL
https://us.swimlane.app
Swimlane Platform base URL
SWIMLANE_PAT_TOKEN
your-personal-access-token
Swimlane Personal Access Token
SWIMLANE_ACCOUNT_ID
your-account-id
Swimlane account identifier
SWIMLANE_TENANT_LIST
``
Comma-separated tenant IDs (optional, leave empty for all tenants)
INCLUDE_ACCOUNT
true
Include account-level logs (true/false)
PAGE_SIZE
100
Records per page (max 100)
LOOKBACK_HOURS
24
Initial lookback period
TIMEOUT
30
API request timeout in seconds
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
import
uuid
import
gzip
import
io
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
'swimlane/audit/'
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
'swimlane/audit/state.json'
)
SWIMLANE_BASE_URL
=
os
.
environ
.
get
(
'SWIMLANE_BASE_URL'
,
''
)
.
rstrip
(
'/'
)
SWIMLANE_PAT_TOKEN
=
os
.
environ
.
get
(
'SWIMLANE_PAT_TOKEN'
)
SWIMLANE_ACCOUNT_ID
=
os
.
environ
.
get
(
'SWIMLANE_ACCOUNT_ID'
)
SWIMLANE_TENANT_LIST
=
os
.
environ
.
get
(
'SWIMLANE_TENANT_LIST'
,
''
)
INCLUDE_ACCOUNT
=
os
.
environ
.
get
(
'INCLUDE_ACCOUNT'
,
'true'
)
.
lower
()
==
'true'
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
'100'
))
LOOKBACK_HOURS
=
int
(
os
.
environ
.
get
(
'LOOKBACK_HOURS'
,
'24'
))
TIMEOUT
=
int
(
os
.
environ
.
get
(
'TIMEOUT'
,
'30'
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
Cloud Run function triggered by Pub/Sub to fetch Swimlane Platform logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
SWIMLANE_BASE_URL
,
SWIMLANE_PAT_TOKEN
,
SWIMLANE_ACCOUNT_ID
]):
print
(
'Error: Missing required environment variables (GCS_BUCKET, SWIMLANE_BASE_URL, SWIMLANE_PAT_TOKEN, SWIMLANE_ACCOUNT_ID)'
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
hours
=
LOOKBACK_HOURS
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
base_url
=
SWIMLANE_BASE_URL
,
pat_token
=
SWIMLANE_PAT_TOKEN
,
account_id
=
SWIMLANE_ACCOUNT_ID
,
tenant_list
=
SWIMLANE_TENANT_LIST
,
include_account
=
INCLUDE_ACCOUNT
,
start_time
=
last_time
,
end_time
=
now
,
page_size
=
PAGE_SIZE
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
# Write to GCS as gzipped NDJSON
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
}{
now
:
%Y/%m/%d
}
/swimlane-audit-
{
uuid
.
uuid4
()
}
.json.gz"
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
record
in
records
:
gz
.
write
((
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
+
'
\n
'
)
.
encode
())
buf
.
seek
(
0
)
blob
=
bucket
.
blob
(
object_key
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
,
'updated_at'
:
datetime
.
now
(
timezone
.
utc
)
.
isoformat
()
+
'Z'
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
base_url
:
str
,
pat_token
:
str
,
account_id
:
str
,
tenant_list
:
str
,
include_account
:
bool
,
start_time
:
datetime
,
end_time
:
datetime
,
page_size
:
int
):
"""
Fetch logs from Swimlane Platform API with pagination and rate limiting.
Args:
base_url: Swimlane Platform base URL
pat_token: Personal Access Token
account_id: Swimlane account identifier
tenant_list: Comma-separated tenant IDs (optional)
include_account: Include account-level logs
start_time: Start time for log query
end_time: End time for log query
page_size: Number of records per page (max 100)
Returns:
Tuple of (records list, newest_event_time ISO string)
"""
endpoint
=
f
"
{
base_url
}
/api/public/audit/account/
{
account_id
}
/auditlogs"
headers
=
{
'Private-Token'
:
pat_token
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
'GoogleSecOps-SwimlaneCollector/1.0'
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
True
:
params
=
[]
params
.
append
(
f
"pageNumber=
{
page_num
}
"
)
params
.
append
(
f
"pageSize=
{
min
(
page_size
,
100
)
}
"
)
params
.
append
(
f
"fromdate=
{
start_time
.
isoformat
()
}
"
)
params
.
append
(
f
"todate=
{
end_time
.
isoformat
()
}
"
)
if
tenant_list
:
params
.
append
(
f
"tenantList=
{
tenant_list
}
"
)
params
.
append
(
f
"includeAccount=
{
'true'
if
include_account
else
'false'
}
"
)
url
=
f
"
{
endpoint
}
?
{
'&'
.
join
(
params
)
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
TIMEOUT
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
==
401
:
print
(
f
"Authentication failed (401). Verify SWIMLANE_PAT_TOKEN is correct."
)
return
[],
None
if
response
.
status
==
403
:
print
(
f
"Access forbidden (403). Verify account has Account Admin permissions to access audit logs."
)
return
[],
None
if
response
.
status
==
400
:
print
(
f
"Bad request (400). Verify account_id and query parameters are correct."
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
page_results
=
data
.
get
(
'auditlogs'
,
[])
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
events"
)
records
.
extend
(
page_results
)
# Track newest event time
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
'eventTime'
)
or
event
.
get
(
'EventTime'
)
if
event_time
:
if
newest_time
is
None
or
parse_datetime
(
event_time
)
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
# Check for more results
has_next
=
data
.
get
(
'next'
)
total_count
=
data
.
get
(
'totalCount'
,
0
)
if
not
has_next
:
print
(
f
"Reached last page (no next link)"
)
break
# Check if we've hit the 10,000 log limit
if
total_count
>
10000
and
len
(
records
)
>
=
10000
:
print
(
f
"Warning: Reached Swimlane API limit of 10,000 logs. Consider narrowing the time range."
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
swimlane-audit-schedule-15min
Region
Select same region as Cloud Run function
Frequency
*/15 * * * *
(every 15 minutes)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select the Pub/Sub topic (
swimlane-audit-trigger
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
Standard (recommended)
Every hour
0 * * * *
Medium volume
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
0 0 * * *
Historical data collection
Test the integration
In the
Cloud Scheduler
console, find your job.
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
swimlane-audit-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
Page 1: Retrieved X events
Wrote X records to gs://bucket-name/swimlane/audit/YYYY/MM/DD/swimlane-audit-UUID.json.gz
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
swimlane/audit/
).
Verify that a new
.json.gz
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check SWIMLANE_PAT_TOKEN in environment variables and verify the Personal Access Token is correct
HTTP 403
: Verify account has Account Admin permissions to access audit logs
HTTP 400
: Verify SWIMLANE_ACCOUNT_ID is correct and query parameters are valid
HTTP 404
: Verify SWIMLANE_BASE_URL and API endpoint path are correct
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set (GCS_BUCKET, SWIMLANE_BASE_URL, SWIMLANE_PAT_TOKEN, SWIMLANE_ACCOUNT_ID)
Connection errors
: Verify network connectivity to Swimlane Platform and firewall rules
10,000 log limit warning
: Reduce LOOKBACK_HOURS or increase Cloud Scheduler frequency to stay within Swimlane's API limit
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
Swimlane Platform logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Swimlane Platform
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
Configure a feed in Google SecOps to ingest Swimlane Platform logs
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
Swimlane Platform logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Swimlane Platform
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://swimlane-audit/swimlane/audit/
Replace:
swimlane-audit
: Your GCS bucket name.
swimlane/audit/
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
