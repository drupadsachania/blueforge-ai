# Collect ZeroFox platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform/  
**Scraped:** 2026-03-05T09:30:27.339373Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ZeroFox platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest ZeroFox Platform logs to Google Security Operations using Google Cloud Storage. ZeroFox Platform provides digital risk protection by monitoring and analyzing threats across social media, mobile apps, cloud, email, and other digital channels.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to ZeroFox Platform tenant
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
zerofox-platform-logs
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
Collect ZeroFox Platform credentials
Get ZeroFox personal access token
Sign in to the ZeroFox Platform at
https://cloud.zerofox.com
.
Go to
Settings
>
Data Connections
>
API Data Feeds
.
Direct URL (after login):
https://cloud.zerofox.com/data_connectors/api
Note: If you don't see this menu item, contact your ZeroFox administrator for access. The menu may also be labeled
Data Connectors
>
API Data Feeds
depending on your tenant UI version.
Click
Generate Token
or
Create Personal Access Token
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps GCS Ingestion
).
Expiration
: Select a rotation period according to your organization's security policy.
Permissions/Feeds
: Select read permissions for:
Alerts
CTI feeds
Other data types you want to export
Click
Generate
.
Copy and save the generated Personal Access Token in a secure location (you won't be able to view it again).
Save the
ZEROFOX_BASE_URL
:
https://api.zerofox.com
(default for most tenants).
Verify permissions
To verify the account has the required permissions:
Sign in to ZeroFox Platform.
Go to
Settings
(⚙️)
>
Data Connections
>
API Data Feeds
.
If you can see the
API Data Feeds
section and generate tokens, you have the required permissions.
If you cannot see this option, contact your administrator to grant API access permissions.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
ZEROFOX_API_TOKEN
=
"your-personal-access-token"
ZEROFOX_BASE_URL
=
"https://api.zerofox.com"
# Test API access (example endpoint - adjust based on your data type)
curl
-v
-H
"Authorization: Bearer
$ZEROFOX_API_TOKEN
"
\
-H
"Accept: application/json"
\
"
$ZEROFOX_BASE_URL
/v1/alerts?limit=1"
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
zerofox-logs-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect ZeroFox Platform logs
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
Grant the service account (
zerofox-logs-collector-sa
) write permissions on the GCS bucket:
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (for example,
zerofox-platform-logs
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
zerofox-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
zerofox-logs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from ZeroFox Platform API and writes them to GCS.
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
zerofox-logs-collector
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
zerofox-logs-trigger
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
zerofox-logs-collector-sa
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
zerofox-platform-logs
GCS bucket name
GCS_PREFIX
zerofox/platform
Prefix for log files
STATE_KEY
zerofox/platform/state.json
State file path
ZEROFOX_BASE_URL
https://api.zerofox.com
API base URL
ZEROFOX_API_TOKEN
your-zerofox-personal-access-token
Personal access token
LOOKBACK_HOURS
24
Initial lookback period
PAGE_SIZE
200
Records per page
MAX_PAGES
20
Maximum pages per run
HTTP_TIMEOUT
60
HTTP request timeout in seconds
HTTP_RETRIES
3
Number of HTTP retries
URL_TEMPLATE
(optional)
Custom URL template with
{SINCE}
,
{PAGE_TOKEN}
,
{PAGE_SIZE}
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
urllib.parse
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
'zerofox/platform'
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
'zerofox/platform/state.json'
)
ZEROFOX_BASE_URL
=
os
.
environ
.
get
(
'ZEROFOX_BASE_URL'
,
'https://api.zerofox.com'
)
ZEROFOX_API_TOKEN
=
os
.
environ
.
get
(
'ZEROFOX_API_TOKEN'
)
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
'200'
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
URL_TEMPLATE
=
os
.
environ
.
get
(
'URL_TEMPLATE'
,
''
)
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
Cloud Run function triggered by Pub/Sub to fetch ZeroFox Platform logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
ZEROFOX_BASE_URL
,
ZEROFOX_API_TOKEN
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
"last_since"
):
try
:
last_time
=
parse_datetime
(
state
[
"last_since"
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
"Warning: Could not parse last_since:
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
since_iso
=
last_time
.
strftime
(
'%Y-%m-
%d
T%H:%M:%SZ'
)
print
(
f
"Fetching logs since
{
since_iso
}
"
)
# Fetch logs
records
,
newest_since
=
fetch_logs
(
api_base
=
ZEROFOX_BASE_URL
,
api_token
=
ZEROFOX_API_TOKEN
,
since
=
since_iso
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
since_iso
)
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
# Update state with newest timestamp
if
newest_since
:
save_state
(
bucket
,
STATE_KEY
,
newest_since
)
else
:
save_state
(
bucket
,
STATE_KEY
,
since_iso
)
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
last_since
:
str
):
"""Save the last since timestamp to GCS state file."""
try
:
state
=
{
'last_since'
:
last_since
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
"Saved state: last_since=
{
last_since
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
api_token
:
str
,
since
:
str
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
Fetch logs from ZeroFox Platform API with pagination and rate limiting.
Args:
api_base: API base URL
api_token: Personal access token
since: ISO timestamp for filtering logs
page_size: Number of records per page
max_pages: Maximum pages to fetch
Returns:
Tuple of (records list, newest_since ISO string)
"""
# Use URL_TEMPLATE if provided, otherwise construct default alerts endpoint
if
URL_TEMPLATE
:
base_url
=
URL_TEMPLATE
.
replace
(
"
{SINCE}
"
,
urllib
.
parse
.
quote
(
since
))
else
:
base_url
=
f
"
{
api_base
}
/v1/alerts?since=
{
urllib
.
parse
.
quote
(
since
)
}
"
headers
=
{
'Authorization'
:
f
'Bearer
{
api_token
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
'GoogleSecOps-ZeroFoxCollector/1.0'
}
records
=
[]
newest_since
=
since
page_num
=
0
page_token
=
""
backoff
=
1.0
while
page_num
<
max_pages
:
page_num
+=
1
# Construct URL with pagination
if
URL_TEMPLATE
:
url
=
(
base_url
.
replace
(
"
{PAGE_TOKEN}
"
,
urllib
.
parse
.
quote
(
page_token
))
.
replace
(
"
{PAGE_SIZE}
"
,
str
(
page_size
)))
else
:
url
=
f
"
{
base_url
}
&
limit=
{
page_size
}
"
if
page_token
:
url
+=
f
"&page_token=
{
urllib
.
parse
.
quote
(
page_token
)
}
"
attempt
=
0
while
attempt
<
=
HTTP_RETRIES
:
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
attempt
+=
1
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
records
,
newest_since
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
# Extract results (try multiple possible keys)
page_results
=
[]
for
key
in
(
'results'
,
'data'
,
'alerts'
,
'items'
,
'logs'
,
'events'
):
if
isinstance
(
data
.
get
(
key
),
list
):
page_results
=
data
[
key
]
break
if
not
page_results
:
print
(
f
"No more results (empty page)"
)
return
records
,
newest_since
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
# Track newest timestamp
for
event
in
page_results
:
try
:
# Try multiple possible timestamp fields
event_time
=
(
event
.
get
(
'timestamp'
)
or
event
.
get
(
'created_at'
)
or
event
.
get
(
'last_modified'
)
or
event
.
get
(
'event_time'
)
or
event
.
get
(
'log_time'
)
or
event
.
get
(
'updated_at'
))
if
event_time
and
isinstance
(
event_time
,
str
):
if
event_time
>
newest_since
:
newest_since
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
# Check for next page token
next_token
=
(
data
.
get
(
'next'
)
or
data
.
get
(
'next_token'
)
or
data
.
get
(
'nextPageToken'
)
or
data
.
get
(
'next_page_token'
))
if
isinstance
(
next_token
,
dict
):
next_token
=
(
next_token
.
get
(
'token'
)
or
next_token
.
get
(
'cursor'
)
or
next_token
.
get
(
'value'
))
if
not
next_token
:
print
(
"No more pages (no next token)"
)
return
records
,
newest_since
page_token
=
str
(
next_token
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
if
attempt
<
HTTP_RETRIES
:
print
(
f
"HTTP error (attempt
{
attempt
+
1
}
/
{
HTTP_RETRIES
}
):
{
e
}
"
)
time
.
sleep
(
1
+
attempt
)
attempt
+=
1
continue
else
:
print
(
f
"Error fetching logs after
{
HTTP_RETRIES
}
retries:
{
e
}
"
)
return
records
,
newest_since
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
records
,
newest_since
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
newest_since
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
Cloud scheduler publishes messages to the Pub/Sub topic (
zerofox-logs-trigger
) at regular intervals, triggering the Cloud Run function.
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
zerofox-logs-collector-hourly
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
zerofox-logs-trigger
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
zerofox-logs-collector-hourly
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
Click your function name (
zerofox-logs-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching logs since YYYY-MM-DDTHH:MM:SSZ
Page 1: Retrieved X events
Wrote X records to gs://zerofox-platform-logs/zerofox/platform/logs_YYYYMMDD_HHMMSS.ndjson
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
zerofox-platform-logs
).
Navigate to the prefix folder (
zerofox/platform/
).
Verify that a new
.ndjson
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables. Verify the
ZEROFOX_API_TOKEN
is correct and has not expired.
HTTP 403
: Verify the ZeroFox account has required permissions for Alerts and CTI feeds. Go to
Settings
>
Data Connections
>
API Data Feeds
and check token permissions.
HTTP 404
: The default
/v1/alerts
endpoint may not be correct for your tenant. Set the
URL_TEMPLATE
environment variable to match your ZeroFox API documentation or contact ZeroFox support.
HTTP 429
: Rate limiting - function will automatically retry with exponential backoff.
Missing environment variables
: Check all required variables are set in the Cloud Run function configuration.
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
ZeroFox Platform Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
ZeroFox Platform
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
zerofox-platform-logs
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
Configure a feed in Google SecOps to ingest ZeroFox Platform logs
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
ZeroFox Platform Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
ZeroFox Platform
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://zerofox-platform-logs/zerofox/platform/
Replace:
zerofox-platform-logs
: Your GCS bucket name.
zerofox/platform
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
