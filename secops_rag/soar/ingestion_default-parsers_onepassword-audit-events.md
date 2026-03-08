# Collect 1Password Audit Events logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events/  
**Scraped:** 2026-03-05T09:58:53.434938Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect 1Password Audit Events logs
Supported in:
Google secops
SIEM
This document explains how to ingest 1Password Audit Events logs to Google Security Operations using Google Cloud Storage V2.
1Password is a password management platform that helps teams securely store, share, and manage credentials, secrets, and sensitive information. The 1Password Events API provides access to audit event data that captures administrative and policy actions performed in your 1Password Business account.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
A
1Password Business
account
An owner or administrator role in your 1Password account
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
onepassword-audit-secops-logs
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
Collect 1Password credentials
Set up Events Reporting integration
Sign in to your account on
1Password.com
.
Select
Integrations
in the sidebar.
If you have previously set up other integrations, select
Directory
on the
Integrations
page.
In the
Events Reporting
section, select
Other
.
In the
Name
field, enter a name for the integration (for example,
Google SecOps Audit Events
).
Click
Add Integration
.
Create a bearer token
On the integration details page, click
Add a Bearer Token
.
Provide the following configuration details:
Token Name
: Enter a descriptive name (for example,
SecOps GCS Collector - Audit Events
)
Expires After
: Select the expiration period according to your preference. Select
Never
for a non-expiring token, or choose
30 days
,
90 days
, or
180 days
.
Events to Report
: Select the following checkbox:
Audit events
Click
Issue Token
.
On the
Save your token
page, click
Save in 1Password
or copy the token and save it in a secure location.
Click
View Integration Details
to confirm the integration is active.
Determine your Events API base URL
The base URL depends on the server that hosts your 1Password account:
If your account is hosted on
Your Events API base URL is
1password.com
https://events.1password.com
ent.1password.com
https://events.ent.1password.com
1password.ca
https://events.1password.ca
1password.eu
https://events.1password.eu
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual bearer token and base URL
BEARER_TOKEN
=
"<your-bearer-token>"
API_BASE
=
"https://events.1password.com"
# Test API access using the introspect endpoint
curl
-v
\
-H
"Authorization: Bearer
$BEARER_TOKEN
"
\
"
$API_BASE
/api/v2/auth/introspect"
A successful response returns a JSON object with the
features
field listing the event types your token can access (for example,
["auditevents"]
).
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
onepassword-audit-collector-sa
Service account description
: Enter
Service account for Cloud Run function to collect 1Password Audit Events logs
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
Click your bucket (
onepassword-audit-secops-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter
onepassword-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com
Assign roles
: Select
Storage Object Admin
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
onepassword-audit-trigger
Leave other settings as default
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit event logs from the 1Password Events API and write them to GCS.
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
onepassword-audit-collector
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
, choose
onepassword-audit-trigger
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
Scroll to and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select
onepassword-audit-collector-sa
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
onepassword-audit-secops-logs
GCS bucket name
GCS_PREFIX
onepassword-audit
Prefix for log files
STATE_KEY
onepassword-audit/state.json
State file path
OP_API_BASE
https://events.1password.com
1Password Events API base URL
OP_BEARER_TOKEN
<your-bearer-token>
1Password Events API bearer token
MAX_RECORDS
10000
Max records per run
PAGE_SIZE
1000
Records per page (max 1000)
LOOKBACK_HOURS
24
Initial lookback period in hours
In the
Variables & Secrets
section, scroll to
Requests
:
Request timeout
: Enter
600
seconds (10 minutes)
Go to the
Settings
tab:
In the
Resources
section:
Memory
: Select
512 MiB
or higher
CPU
: Select
1
In the
Revision scaling
section:
Minimum number of instances
: Enter
0
Maximum number of instances
: Enter
100
(or adjust based on expected load)
Click
Create
.
Wait for the service to be created (1-2 minutes).
After the service is created, the
inline code editor
will open automatically.
Add function code
Enter
main
in the
Entry point
field.
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
'onepassword-audit'
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
'onepassword-audit/state.json'
)
API_BASE
=
os
.
environ
.
get
(
'OP_API_BASE'
)
BEARER_TOKEN
=
os
.
environ
.
get
(
'OP_BEARER_TOKEN'
)
MAX_RECORDS
=
int
(
os
.
environ
.
get
(
'MAX_RECORDS'
,
'10000'
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
'1000'
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
# 1Password Events API v2 audit events endpoint
AUDIT_EVENTS_PATH
=
'/api/v2/auditevents'
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
"""Parse RFC 3339 datetime string to datetime object."""
if
value
.
endswith
(
'Z'
):
value
=
value
[:
-
1
]
+
'+00:00'
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
Cloud Run function triggered by Pub/Sub to fetch 1Password
audit event logs and write them to GCS as NDJSON.
"""
if
not
all
([
GCS_BUCKET
,
API_BASE
,
BEARER_TOKEN
]):
print
(
'Error: Missing required environment variables '
'(GCS_BUCKET, OP_API_BASE, OP_BEARER_TOKEN)'
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
GCS_BUCKET
)
# Load state (stores cursor)
state
=
load_state
(
bucket
,
STATE_KEY
)
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
print
(
'--- Processing endpoint: auditevents ---'
)
saved_cursor
=
state
.
get
(
'cursor_auditevents'
)
records
,
last_cursor
=
fetch_endpoint
(
api_base
=
API_BASE
,
path
=
AUDIT_EVENTS_PATH
,
bearer_token
=
BEARER_TOKEN
,
saved_cursor
=
saved_cursor
,
lookback_hours
=
LOOKBACK_HOURS
,
page_size
=
PAGE_SIZE
,
max_records
=
MAX_RECORDS
,
)
if
records
:
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
(
f
'
{
GCS_PREFIX
}
/'
f
'auditevents_
{
timestamp
}
.ndjson'
)
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
(
json
.
dumps
(
r
,
ensure_ascii
=
False
)
for
r
in
records
)
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
'Wrote
{
len
(
records
)
}
auditevents records '
f
'to gs://
{
GCS_BUCKET
}
/
{
object_key
}
'
)
# Save cursor even if no records (for next poll)
if
last_cursor
:
state
[
'cursor_auditevents'
]
=
last_cursor
# Save state
state
[
'last_run'
]
=
now
.
isoformat
()
save_state
(
bucket
,
STATE_KEY
,
state
)
print
(
f
'Successfully processed
{
len
(
records
)
}
records'
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
e
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
:
dict
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
,
indent
=
2
),
content_type
=
'application/json'
,
)
print
(
f
'Saved state:
{
json
.
dumps
(
state
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
'Warning: Could not save state:
{
e
}
'
)
def
fetch_endpoint
(
api_base
,
path
,
bearer_token
,
saved_cursor
,
lookback_hours
,
page_size
,
max_records
):
"""
Fetch events from the 1Password Events API v2 audit events
endpoint.
The 1Password Events API uses cursor-based pagination with POST
requests. The first request sends a ResetCursor object with
optional start_time and limit. Subsequent requests send the
cursor returned from the previous response.
Args:
api_base: Events API base URL
path: Endpoint path
bearer_token: JWT bearer token
saved_cursor: Cursor from previous run (or None)
lookback_hours: Hours to look back on first run
page_size: Max events per page (1-1000)
max_records: Max total events per run
Returns:
Tuple of (records list, last_cursor string)
"""
url
=
f
'
{
api_base
.
rstrip
(
"/"
)
}{
path
}
'
headers
=
{
'Authorization'
:
f
'Bearer
{
bearer_token
}
'
,
'Content-Type'
:
'application/json'
,
'Accept'
:
'application/json'
,
}
records
=
[]
cursor
=
saved_cursor
page_num
=
0
backoff
=
1.0
while
True
:
page_num
+=
1
if
len
(
records
)
>
=
max_records
:
print
(
f
'Reached max_records limit (
{
max_records
}
)'
)
break
# Build request body
if
cursor
:
# Continuing cursor: resume from last position
body
=
json
.
dumps
({
'cursor'
:
cursor
})
else
:
# ResetCursor: first request or no saved state
start_time
=
(
datetime
.
now
(
timezone
.
utc
)
-
timedelta
(
hours
=
lookback_hours
)
)
body
=
json
.
dumps
({
'limit'
:
page_size
,
'start_time'
:
start_time
.
strftime
(
'%Y-%m-
%d
T%H:%M:%SZ'
),
})
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
url
,
body
=
body
,
headers
=
headers
,
)
# Handle rate limiting (600 req/min, 30000 req/hour)
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
))
)
)
print
(
f
'Rate limited (429). Retrying after '
f
'
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
60.0
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
'HTTP Error
{
response
.
status
}
: '
f
'
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
page_items
=
data
.
get
(
'items'
,
[])
cursor
=
data
.
get
(
'cursor'
)
has_more
=
data
.
get
(
'has_more'
,
False
)
if
page_items
:
print
(
f
'Page
{
page_num
}
: Retrieved '
f
'
{
len
(
page_items
)
}
events'
)
records
.
extend
(
page_items
)
if
not
has_more
:
print
(
f
'No more pages (has_more=false)'
)
break
if
not
cursor
:
print
(
f
'No cursor returned, stopping'
)
break
except
urllib3
.
exceptions
.
HTTPError
as
e
:
print
(
f
'HTTP error:
{
str
(
e
)
}
'
)
break
except
Exception
as
e
:
print
(
f
'Error fetching events:
{
str
(
e
)
}
'
)
break
print
(
f
'Retrieved
{
len
(
records
)
}
total records '
f
'from
{
page_num
}
pages'
)
return
records
,
cursor
Second file:
requirements.txt:
functions-framework==3.*
google-cloud-storage==2.*
urllib3>=2.0.0
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
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
onepassword-audit-collector-hourly
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
Select
onepassword-audit-trigger
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
console, find
onepassword-audit-collector-hourly
.
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click
onepassword-audit-collector
.
Click the
Logs
tab.
Verify the function executed successfully. Look for:
--- Processing endpoint: auditevents ---
Page 1: Retrieved X events
Wrote X auditevents records to gs://onepassword-audit-secops-logs/onepassword-audit/auditevents_YYYYMMDD_HHMMSS.ndjson
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click
onepassword-audit-secops-logs
.
Navigate to the
onepassword-audit/
folder.
Verify that a new
.ndjson
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check the bearer token in the
OP_BEARER_TOKEN
environment variable. The token may have expired.
HTTP 429
: Rate limiting. The function automatically retries with backoff. The 1Password Events API allows 600 requests per minute and 30,000 requests per hour.
Missing environment variables
: Check all required variables are set in the Cloud Run function configuration.
No records returned
: Verify your bearer token has access to audit events using the introspect endpoint.
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
1Password Audit Events Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
1Password Audit Events
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://onepassword-audit-secops-logs/onepassword-audit/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days)
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click
onepassword-audit-secops-logs
.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email
Assign roles
: Select
Storage Object Viewer
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
