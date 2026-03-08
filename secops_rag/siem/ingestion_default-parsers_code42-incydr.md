# Collect Code42 Incydr core datasets

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/code42-incydr/  
**Scraped:** 2026-03-05T09:22:23.842889Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Code42 Incydr core datasets
Supported in:
Google secops
SIEM
This document explains how to ingest Code42 Incydr core datasets (Users, Audit, Cases, and optionally File Events) to Google Security Operations using Google Cloud Storage.
Code42 Incydr is an insider risk management solution that detects, investigates, and responds to data exfiltration across devices by monitoring file activity in real time across endpoints, cloud services, and email.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Code42 Incydr API or admin console with Insider Risk Admin role
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
code42-incydr-logs
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
Collect Code42 Incydr API credentials
Create API client
Sign in to the Code42 Incydr web console.
Go to
Administration
>
Integrations
>
API Clients
.
Click
Create new API client
.
In the
Create new API client
dialog, enter a name for the client (for example,
Google Security Operations Integration
).
Copy and save the following details in a secure location:
Client ID
: The API client identifier.
Secret
: The API client secret key.
Click
Create
.
Determine API base URL
The API base URL depends on your Code42 Incydr console URL. Verify your API gateway URL in the Incydr Developer Portal or your tenant's environment documentation.
Common defaults:
Console URL
API Base URL
https://console.us.code42.com
https://api.us.code42.com
https://console.us2.code42.com
https://api.us2.code42.com
https://console.ie.code42.com
https://api.ie.code42.com
https://console.gov.code42.com
https://api.gov.code42.com
Verify API client permissions
The API client must have appropriate permissions to access the required endpoints:
In the Code42 Incydr console, go to
Administration
>
Integrations
>
API Clients
.
Click on the API client name you created.
Verify the API client has access to the following scopes:
Users
: Read access to user data
Audit Log
: Read access to audit logs
Cases
: Read access to case data
File Events
(optional): Read access to file event data
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
CLIENT_ID
=
"your-client-id"
CLIENT_SECRET
=
"your-client-secret"
API_BASE
=
"https://api.us.code42.com"
# Get OAuth token
TOKEN
=
$(
curl
-s
-X
POST
"
${
API_BASE
}
/v1/oauth/token"
\
-u
"
${
CLIENT_ID
}
:
${
CLIENT_SECRET
}
"
\
-H
"Content-Type: application/x-www-form-urlencoded"
\
-d
"grant_type=client_credentials"
|
jq
-r
'.access_token'
)
# Test API access
curl
-v
-H
"Authorization: Bearer
${
TOKEN
}
"
"
${
API_BASE
}
/v1/users?pageSize=1"
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
code42-incydr-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Code42 Incydr logs
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
Click your bucket name (for example,
code42-incydr-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
code42-incydr-collector-sa@your-project.iam.gserviceaccount.com
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
code42-incydr-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Code42 Incydr API and writes them to GCS.
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
code42-incydr-collector
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
code42-incydr-trigger
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
code42-incydr-collector-sa
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
Description
INCYDR_BASE_URL
https://api.us.code42.com
API base URL from your tenant
INCYDR_CLIENT_ID
your-client-id
API client ID
INCYDR_CLIENT_SECRET
your-client-secret
API client secret
GCS_BUCKET
code42-incydr-logs
GCS bucket name
GCS_PREFIX
code42/
Prefix for log files
PAGE_SIZE
500
Records per page
LOOKBACK_MINUTES
60
Initial lookback period
STREAMS
users,audit,cases
Comma-separated data streams
FE_QUERY_JSON
``
Optional: File events query JSON
FE_PAGE_SIZE
1000
Optional: File events page size
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
1024 MiB
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
time
# Initialize HTTP client
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
BASE
=
os
.
environ
.
get
(
"INCYDR_BASE_URL"
,
""
)
.
rstrip
(
"/"
)
CID
=
os
.
environ
.
get
(
"INCYDR_CLIENT_ID"
,
""
)
CSECRET
=
os
.
environ
.
get
(
"INCYDR_CLIENT_SECRET"
,
""
)
BUCKET
=
os
.
environ
.
get
(
"GCS_BUCKET"
,
""
)
PREFIX_BASE
=
os
.
environ
.
get
(
"GCS_PREFIX"
,
"code42/"
)
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
"PAGE_SIZE"
,
"500"
))
LOOKBACK_MINUTES
=
int
(
os
.
environ
.
get
(
"LOOKBACK_MINUTES"
,
"60"
))
STREAMS
=
[
s
.
strip
()
for
s
in
os
.
environ
.
get
(
"STREAMS"
,
"users"
)
.
split
(
","
)
if
s
.
strip
()]
FE_QUERY_JSON
=
os
.
environ
.
get
(
"FE_QUERY_JSON"
,
""
)
.
strip
()
FE_PAGE_SIZE
=
int
(
os
.
environ
.
get
(
"FE_PAGE_SIZE"
,
"1000"
))
def
now_utc
():
return
datetime
.
now
(
timezone
.
utc
)
def
iso_minus
(
minutes
:
int
):
return
(
now_utc
()
-
timedelta
(
minutes
=
minutes
))
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
)
def
put_json
(
bucket
,
prefix
:
str
,
page_label
:
str
,
data
):
ts
=
now_utc
()
.
strftime
(
"%Y/%m/
%d
/%H%M%S"
)
key
=
f
"
{
PREFIX_BASE
}{
prefix
}{
ts
}
-
{
page_label
}
.json"
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
data
),
content_type
=
'application/json'
)
return
key
def
get_token
():
"""Get OAuth 2.0 access token using client credentials flow."""
token_url
=
f
"
{
BASE
}
/v1/oauth/token"
# Encode credentials
import
base64
credentials
=
f
"
{
CID
}
:
{
CSECRET
}
"
encoded_credentials
=
base64
.
b64encode
(
credentials
.
encode
(
'utf-8'
))
.
decode
(
'utf-8'
)
headers
=
{
'Authorization'
:
f
'Basic
{
encoded_credentials
}
'
,
'Content-Type'
:
'application/x-www-form-urlencoded'
,
'Accept'
:
'application/json'
}
body
=
'grant_type=client_credentials'
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
response
=
http
.
request
(
'POST'
,
token_url
,
body
=
body
,
headers
=
headers
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
"Rate limited (429) on token request. Retrying after
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
if
response
.
status
!=
200
:
raise
RuntimeError
(
f
"Failed to get access token:
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
(
'utf-8'
)
}
"
)
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
return
data
[
'access_token'
]
raise
RuntimeError
(
f
"Failed to get token after
{
max_retries
}
retries due to rate limiting"
)
def
auth_header
():
token
=
get_token
()
return
{
"Authorization"
:
f
"Bearer
{
token
}
"
,
"Accept"
:
"application/json"
}
def
http_get
(
path
:
str
,
params
:
dict
=
None
,
headers
:
dict
=
None
):
url
=
f
"
{
BASE
}{
path
}
"
if
params
:
from
urllib.parse
import
urlencode
url
+=
"?"
+
urlencode
(
params
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
return
response
.
data
raise
RuntimeError
(
f
"Failed after
{
max_retries
}
retries due to rate limiting"
)
def
http_post_json
(
path
:
str
,
body
:
dict
,
headers
:
dict
=
None
):
url
=
f
"
{
BASE
}{
path
}
"
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
response
=
http
.
request
(
'POST'
,
url
,
body
=
json
.
dumps
(
body
),
headers
=
{
**
headers
,
'Content-Type'
:
'application/json'
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
return
response
.
data
raise
RuntimeError
(
f
"Failed after
{
max_retries
}
retries due to rate limiting"
)
# USERS (/v1/users)
def
pull_users
(
bucket
,
hdrs
):
next_token
=
None
pages
=
0
while
True
:
params
=
{
"active"
:
"true"
,
"blocked"
:
"false"
,
"pageSize"
:
PAGE_SIZE
}
if
next_token
:
params
[
"pageToken"
]
=
next_token
raw
=
http_get
(
"/v1/users"
,
params
,
hdrs
)
data
=
json
.
loads
(
raw
.
decode
(
'utf-8'
))
put_json
(
bucket
,
"users/"
,
f
"users-page-
{
pages
}
"
,
data
)
pages
+=
1
next_token
=
data
.
get
(
"nextPageToken"
)
or
data
.
get
(
"next_page_token"
)
if
not
next_token
:
break
return
pages
# AUDIT LOG (/v1/audit/log)
def
pull_audit
(
bucket
,
hdrs
):
start_iso
=
iso_minus
(
LOOKBACK_MINUTES
)
next_token
=
None
pages
=
0
while
True
:
params
=
{
"startTime"
:
start_iso
,
"pageSize"
:
PAGE_SIZE
}
if
next_token
:
params
[
"pageToken"
]
=
next_token
raw
=
http_get
(
"/v1/audit/log"
,
params
,
hdrs
)
try
:
data
=
json
.
loads
(
raw
.
decode
(
'utf-8'
))
put_json
(
bucket
,
"audit/"
,
f
"audit-page-
{
pages
}
"
,
data
)
next_token
=
data
.
get
(
"nextPageToken"
)
or
data
.
get
(
"next_page_token"
)
pages
+=
1
if
not
next_token
:
break
except
Exception
as
e
:
print
(
f
"Error parsing audit log response:
{
e
}
"
)
# Save raw response
ts
=
now_utc
()
.
strftime
(
"%Y/%m/
%d
/%H%M%S"
)
key
=
f
"
{
PREFIX_BASE
}
audit/
{
ts
}
-audit-export.bin"
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
raw
,
content_type
=
'application/octet-stream'
)
pages
+=
1
break
return
pages
# CASES (/v1/cases)
def
pull_cases
(
bucket
,
hdrs
):
next_token
=
None
pages
=
0
while
True
:
params
=
{
"pageSize"
:
PAGE_SIZE
}
if
next_token
:
params
[
"pageToken"
]
=
next_token
raw
=
http_get
(
"/v1/cases"
,
params
,
hdrs
)
data
=
json
.
loads
(
raw
.
decode
(
'utf-8'
))
put_json
(
bucket
,
"cases/"
,
f
"cases-page-
{
pages
}
"
,
data
)
pages
+=
1
next_token
=
data
.
get
(
"nextPageToken"
)
or
data
.
get
(
"next_page_token"
)
if
not
next_token
:
break
return
pages
# FILE EVENTS (/v2/file-events/search)
def
pull_file_events
(
bucket
,
hdrs
):
if
not
FE_QUERY_JSON
:
return
0
try
:
base_query
=
json
.
loads
(
FE_QUERY_JSON
)
except
Exception
as
e
:
print
(
f
"Error: FE_QUERY_JSON is not valid JSON:
{
e
}
"
)
return
0
pages
=
0
next_token
=
None
while
True
:
body
=
dict
(
base_query
)
body
[
"pageSize"
]
=
FE_PAGE_SIZE
if
next_token
:
body
[
"pageToken"
]
=
next_token
raw
=
http_post_json
(
"/v2/file-events/search"
,
body
,
hdrs
)
data
=
json
.
loads
(
raw
.
decode
(
'utf-8'
))
put_json
(
bucket
,
"file_events/"
,
f
"fileevents-page-
{
pages
}
"
,
data
)
pages
+=
1
next_token
=
(
data
.
get
(
"nextPageToken"
)
or
data
.
get
(
"next_page_token"
)
or
(
data
.
get
(
"file_events"
)
or
{})
.
get
(
"nextPageToken"
)
)
if
not
next_token
:
break
return
pages
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch logs from Code42 Incydr API and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
BASE
,
CID
,
CSECRET
,
BUCKET
]):
print
(
'Error: Missing required environment variables'
)
return
try
:
bucket
=
storage_client
.
bucket
(
BUCKET
)
hdrs
=
auth_header
()
report
=
{}
if
"users"
in
STREAMS
:
print
(
"Fetching users..."
)
report
[
"users_pages"
]
=
pull_users
(
bucket
,
hdrs
)
if
"audit"
in
STREAMS
:
print
(
"Fetching audit logs..."
)
report
[
"audit_pages"
]
=
pull_audit
(
bucket
,
hdrs
)
if
"cases"
in
STREAMS
:
print
(
"Fetching cases..."
)
report
[
"cases_pages"
]
=
pull_cases
(
bucket
,
hdrs
)
if
"file_events"
in
STREAMS
:
print
(
"Fetching file events..."
)
report
[
"file_events_pages"
]
=
pull_file_events
(
bucket
,
hdrs
)
print
(
f
'Successfully processed logs:
{
json
.
dumps
(
report
)
}
'
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
code42-incydr-hourly
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
code42-incydr-trigger
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
console, find your job (
code42-incydr-hourly
).
Click
Force run
to trigger manually.
Wait a few seconds and go to
Cloud Run
>
Services
>
code42-incydr-collector
>
Logs
.
Verify the function executed successfully. Look for:
Fetching users...
Fetching audit logs...
Fetching cases...
Successfully processed logs: {"users_pages": X, "audit_pages": Y, "cases_pages": Z}
Check the GCS bucket (
code42-incydr-logs
) to confirm logs were written.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables
HTTP 403
: Verify API client has required permissions in Code42 Incydr console
HTTP 429
: Rate limiting - function will automatically retry with backoff
Failed to get access token
: Verify
INCYDR_BASE_URL
,
INCYDR_CLIENT_ID
, and
INCYDR_CLIENT_SECRET
are correct
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
Code42 Incydr Datasets
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Code42 Incydr
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
Click your bucket name (
code42-incydr-logs
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
Configure a feed in Google SecOps to ingest Code42 Incydr logs
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
Code42 Incydr Datasets
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Code42 Incydr
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://code42-incydr-logs/code42/
Replace:
code42-incydr-logs
: Your GCS bucket name.
code42/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://code42-incydr-logs/
With prefix:
gs://code42-incydr-logs/code42/
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
