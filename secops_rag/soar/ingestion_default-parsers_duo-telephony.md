# Collect Duo Telephony logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-telephony/  
**Scraped:** 2026-03-05T09:54:53.879020Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Duo Telephony logs
Supported in:
Google secops
SIEM
This document explains how to ingest Duo Telephony logs to Google Security Operations using Google Cloud Storage. The parser extracts fields from the logs, transforms and maps them to the Unified Data Model (UDM). It handles various Duo log formats, converting timestamps, extracting user information, network details, and security results, and finally structuring the output into the standardized UDM format.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Duo Admin Panel with Owner role
Collect Duo prerequisites (API credentials)
Sign in to the Duo Admin Panel as an administrator with the Owner role.
Go to
Applications
>
Application Catalog
.
Locate the entry for
Admin API
in the catalog.
Click
+ Add
to create the application.
Copy and save in a secure location the following details:
Integration Key
Secret Key
API Hostname
(for example,
api-yyyyyyyy.duosecurity.com
)
In the
Permissions
section, check only the
Read Telephony
permission checkbox and deselect all other permissions.
Click
Save Changes
.
Verify permissions
To verify the Admin API application has the required permissions:
Sign in to the Duo Admin Panel.
Go to
Applications
>
Protect an Application
.
Locate your
Admin API
application.
Click the application name to view details.
In the
Permissions
section, verify that only
Read Telephony
is checked.
If other permissions are checked or Read Telephony is not checked, update the permissions and click
Save Changes
.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
DUO_IKEY
=
"your-integration-key"
DUO_SKEY
=
"your-secret-key"
DUO_HOST
=
"api-yyyyyyyy.duosecurity.com"
# Test API access (requires signing - use Duo's API test tool or Python script)
# Visit https://duo.com/docs/adminapi#testing to test your credentials
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
duo-telephony-logs
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
duo-telephony-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Duo Telephony logs
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
duo-telephony-logs
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
duo-telephony-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
duo-telephony-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Duo Telephony API and writes them to GCS.
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
duo-telephony-logs-collector
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
duo-telephony-trigger
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
duo-telephony-collector-sa
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
GCS_BUCKET
duo-telephony-logs
GCS_PREFIX
duo-telephony
STATE_KEY
duo-telephony/state.json
DUO_IKEY
<your-integration-key>
DUO_SKEY
<your-secret-key>
DUO_API_HOST
api-yyyyyyyy.duosecurity.com
MAX_ITERATIONS
10
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
hmac
import
hashlib
import
base64
import
urllib.parse
import
urllib3
import
email.utils
from
datetime
import
datetime
,
timedelta
,
timezone
from
typing
import
Dict
,
Any
,
List
,
Optional
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
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Duo telephony logs and write to GCS.
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
'duo-telephony'
)
.
rstrip
(
'/'
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
'duo-telephony/state.json'
)
integration_key
=
os
.
environ
.
get
(
'DUO_IKEY'
)
secret_key
=
os
.
environ
.
get
(
'DUO_SKEY'
)
api_hostname
=
os
.
environ
.
get
(
'DUO_API_HOST'
)
if
not
all
([
bucket_name
,
integration_key
,
secret_key
,
api_hostname
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
# Calculate time range
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
if
state
.
get
(
'last_offset'
):
# Continue from last offset
next_offset
=
state
[
'last_offset'
]
logs
=
[]
has_more
=
True
else
:
# Start from last timestamp or 24 hours ago
mintime
=
state
.
get
(
'last_timestamp_ms'
,
int
((
now
-
timedelta
(
hours
=
24
))
.
timestamp
()
*
1000
))
# Apply 2-minute delay as recommended by Duo
maxtime
=
int
((
now
-
timedelta
(
minutes
=
2
))
.
timestamp
()
*
1000
)
next_offset
=
None
logs
=
[]
has_more
=
True
# Fetch logs with pagination
total_fetched
=
0
max_iterations
=
int
(
os
.
environ
.
get
(
'MAX_ITERATIONS'
,
'10'
))
while
has_more
and
total_fetched
<
max_iterations
:
page_num
=
total_fetched
+
1
if
next_offset
:
# Use offset for pagination
params
=
{
'limit'
:
'100'
,
'next_offset'
:
next_offset
}
else
:
# Initial request with time range
params
=
{
'mintime'
:
str
(
mintime
),
'maxtime'
:
str
(
maxtime
),
'limit'
:
'100'
,
'sort'
:
'ts:asc'
}
# Make API request with retry logic
response
=
duo_api_call_with_retry
(
'GET'
,
api_hostname
,
'/admin/v2/logs/telephony'
,
params
,
integration_key
,
secret_key
)
if
'items'
in
response
:
logs
.
extend
(
response
[
'items'
])
total_fetched
+=
1
# Check for more data
if
'metadata'
in
response
and
'next_offset'
in
response
[
'metadata'
]:
next_offset
=
response
[
'metadata'
][
'next_offset'
]
state
[
'last_offset'
]
=
next_offset
else
:
has_more
=
False
state
[
'last_offset'
]
=
None
# Update timestamp for next run
if
logs
:
# Get the latest timestamp from logs (ISO 8601 format)
latest_ts
=
max
([
log
.
get
(
'ts'
,
''
)
for
log
in
logs
])
if
latest_ts
:
# Convert ISO timestamp to milliseconds
dt
=
datetime
.
fromisoformat
(
latest_ts
.
replace
(
'Z'
,
'+00:00'
))
state
[
'last_timestamp_ms'
]
=
int
(
dt
.
timestamp
()
*
1000
)
+
1
# Save logs to GCS if any were fetched
if
logs
:
timestamp
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
strftime
(
'%Y%m
%d
_%H%M%S'
)
blob_name
=
f
"
{
prefix
}
/telephony_
{
timestamp
}
.json"
# Format logs as newline-delimited JSON
log_data
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
log
)
for
log
in
logs
)
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
log_data
,
content_type
=
'application/x-ndjson'
)
print
(
f
"Saved
{
len
(
logs
)
}
telephony logs to gs://
{
bucket_name
}
/
{
blob_name
}
"
)
else
:
print
(
"No new telephony logs found"
)
# Save state
save_state
(
bucket
,
state_key
,
state
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
duo_api_call_with_retry
(
method
:
str
,
host
:
str
,
path
:
str
,
params
:
Dict
[
str
,
str
],
ikey
:
str
,
skey
:
str
,
max_retries
:
int
=
3
)
-
>
Dict
[
str
,
Any
]:
"""Make an authenticated API call to Duo Admin API with retry logic."""
for
attempt
in
range
(
max_retries
):
try
:
return
duo_api_call
(
method
,
host
,
path
,
params
,
ikey
,
skey
)
except
Exception
as
e
:
if
'429'
in
str
(
e
)
or
'5'
in
str
(
e
)[:
1
]:
if
attempt
<
max_retries
-
1
:
wait_time
=
(
2
**
attempt
)
*
2
print
(
f
"Retrying after
{
wait_time
}
seconds..."
)
import
time
time
.
sleep
(
wait_time
)
continue
raise
def
duo_api_call
(
method
:
str
,
host
:
str
,
path
:
str
,
params
:
Dict
[
str
,
str
],
ikey
:
str
,
skey
:
str
)
-
>
Dict
[
str
,
Any
]:
"""Make an authenticated API call to Duo Admin API."""
# Create canonical string for signing using RFC 2822 date format
now
=
email
.
utils
.
formatdate
()
canon
=
[
now
,
method
.
upper
(),
host
.
lower
(),
path
]
# Add parameters
args
=
[]
for
key
in
sorted
(
params
.
keys
()):
val
=
params
[
key
]
args
.
append
(
f
"
{
urllib
.
parse
.
quote
(
key
,
'~'
)
}
=
{
urllib
.
parse
.
quote
(
val
,
'~'
)
}
"
)
canon
.
append
(
'&'
.
join
(
args
))
canon_str
=
'
\n
'
.
join
(
canon
)
# Sign the request
sig
=
hmac
.
new
(
skey
.
encode
(
'utf-8'
),
canon_str
.
encode
(
'utf-8'
),
hashlib
.
sha1
)
.
hexdigest
()
# Create authorization header
auth
=
base64
.
b64encode
(
f
"
{
ikey
}
:
{
sig
}
"
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
# Build URL
url
=
f
"https://
{
host
}{
path
}
"
if
params
:
url
+=
'?'
+
'&'
.
join
(
args
)
# Make request
headers
=
{
'Authorization'
:
f
'Basic
{
auth
}
'
,
'Date'
:
now
,
'Host'
:
host
,
'User-Agent'
:
'duo-telephony-gcs-ingestor/1.0'
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
if
data
.
get
(
'stat'
)
==
'OK'
:
return
data
.
get
(
'response'
,
{})
else
:
raise
Exception
(
f
"API error:
{
data
.
get
(
'message'
,
'Unknown error'
)
}
"
)
except
urllib3
.
exceptions
.
HTTPError
as
e
:
raise
Exception
(
f
"HTTP error:
{
str
(
e
)
}
"
)
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
duo-telephony-logs-1h
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
duo-telephony-trigger
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
Test the scheduler job
In the
Cloud Scheduler
console, find your job (
duo-telephony-logs-1h
).
Click
Force run
to trigger manually.
Wait a few seconds and go to
Cloud Run
>
Services
.
Click on the function name (
duo-telephony-logs-collector
).
Click the
Logs
tab.
Verify the function executed successfully.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
duo-telephony-logs
).
Navigate to the prefix folder (
duo-telephony/
).
Verify that a new
.json
file was created with logs.
If you see errors in the logs:
HTTP 401
: Check API credentials (DUO_IKEY, DUO_SKEY, DUO_API_HOST) in environment variables
HTTP 403
: Verify the Admin API application has
Read Telephony
permission enabled
HTTP 429
: Rate limiting - function will automatically retry with exponential backoff
Missing environment variables
: Check all required variables are set in the Cloud Run function configuration
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
Duo Telephony logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Telephony Logs
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
Click your bucket name (for example,
duo-telephony-logs
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
Configure a feed in Google SecOps to ingest Duo Telephony logs
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
Duo Telephony logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Telephony Logs
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://duo-telephony-logs/duo-telephony/
Replace:
duo-telephony-logs
: Your GCS bucket name.
duo-telephony
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://duo-telephony-logs/
With prefix:
gs://duo-telephony-logs/duo-telephony/
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
UDM mapping table
Log field
UDM mapping
Logic
context
metadata.product_event_type
Directly mapped from the context field in the raw log.
credits
security_result.detection_fields.value
Directly mapped from the credits field in the raw log, nested under a detection_fields object with the corresponding key credits.
eventtype
security_result.detection_fields.value
Directly mapped from the eventtype field in the raw log, nested under a detection_fields object with the corresponding key eventtype.
host
principal.hostname
Directly mapped from the host field in the raw log if it's not an IP address.
security_result.action
Set to a static value of "ALLOW" in the parser.
security_result.detection_fields.value
Set to a static value of "MECHANISM_UNSPECIFIED" in the parser.
metadata.event_timestamp
Parsed from the ts field in the raw log, which is an ISO 8601 timestamp string.
metadata.event_type
Set to "USER_UNCATEGORIZED" if both context and host fields are present in the raw log. Set to "STATUS_UPDATE" if only host is present. Otherwise, set to "GENERIC_EVENT".
metadata.log_type
Directly taken from the raw log's log_type field.
metadata.product_name
Set to a static value of "Telephony" in the parser.
metadata.vendor_name
Set to a static value of "Duo" in the parser.
phone
principal.user.phone_numbers
Directly mapped from the phone field in the raw log.
phone
principal.user.userid
Directly mapped from the phone field in the raw log.
security_result.severity
Set to a static value of "INFORMATIONAL" in the parser.
security_result.summary
Set to a static value of "Duo Telephony" in the parser.
ts
metadata.event_timestamp
Parsed from the ts field in the raw log, which is an ISO 8601 timestamp string.
type
security_result.summary
Directly mapped from the type field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
