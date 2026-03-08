# Collect BeyondTrust Endpoint Privilege Management (EPM) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint/  
**Scraped:** 2026-03-05T09:20:23.828898Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BeyondTrust Endpoint Privilege Management (EPM) logs
Supported in:
Google secops
SIEM
This document explains how to ingest BeyondTrust Endpoint Privilege Management (EPM) logs to Google Security Operations using Google Cloud Storage. The parser focuses on transforming raw JSON log data from BeyondTrust Endpoint into a structured format conforming to the Chronicle UDM. It first initializes default values for various fields and then parses the JSON payload, subsequently mapping specific fields from the raw log into corresponding UDM fields within the
event.idm.read_only_udm
object.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to BeyondTrust Endpoint Privilege Management tenant or API
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
beyondtrust-epm-logs
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
Collect BeyondTrust EPM API credentials
Sign in to the BeyondTrust Privilege Management web console as an administrator.
Go to
Configuration
>
Settings
>
API Settings
.
Click
Create an API Account
.
Provide the following configuration details:
Name
: Enter
Google SecOps Collector
.
API Access
: Enable
Audit (Read)
and other scopes as required.
Copy and save the
Client ID
and
Client Secret
.
Copy your API base URL; it's typically
https://<your-tenant>-services.pm.beyondtrustcloud.com
(you'll use this as BPT_API_URL).
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
beyondtrust-epm-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect BeyondTrust EPM logs
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
beyondtrust-epm-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
beyondtrust-epm-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from BeyondTrust EPM API and writes them to GCS.
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
beyondtrust-epm-collector
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
beyondtrust-epm-trigger
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
beyondtrust-epm-collector-sa
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
beyondtrust-epm-logs
GCS_PREFIX
beyondtrust-epm/
STATE_KEY
beyondtrust-epm/state.json
BPT_API_URL
https://yourtenant-services.pm.beyondtrustcloud.com
CLIENT_ID
your-client-id
CLIENT_SECRET
your-client-secret
OAUTH_SCOPE
management-api
RECORD_SIZE
1000
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
# Initialize HTTP client
http
=
urllib3
.
PoolManager
()
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
Cloud Run function triggered by Pub/Sub to fetch logs from BeyondTrust EPM API and write to GCS.
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
'beyondtrust-epm/'
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
'beyondtrust-epm/state.json'
)
# BeyondTrust EPM API credentials
api_url
=
os
.
environ
.
get
(
'BPT_API_URL'
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
oauth_scope
=
os
.
environ
.
get
(
'OAUTH_SCOPE'
,
'management-api'
)
record_size
=
int
(
os
.
environ
.
get
(
'RECORD_SIZE'
,
'1000'
))
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
if
not
all
([
bucket_name
,
api_url
,
client_id
,
client_secret
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
# Load state (last processed timestamp)
state
=
load_state
(
bucket
,
state_key
)
last_timestamp
=
state
.
get
(
'last_timestamp'
,
(
datetime
.
utcnow
()
-
timedelta
(
hours
=
24
))
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
))
print
(
f
'Processing logs since
{
last_timestamp
}
'
)
# Get OAuth access token
token
=
get_oauth_token
(
api_url
,
client_id
,
client_secret
,
oauth_scope
)
# Fetch audit events
events
=
fetch_audit_events
(
api_url
,
token
,
last_timestamp
,
record_size
,
max_iterations
)
if
events
:
# Store events in GCS
current_timestamp
=
datetime
.
utcnow
()
filename
=
f
"
{
prefix
}
beyondtrust-epm-events-
{
current_timestamp
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
}
.json"
store_events_to_gcs
(
bucket
,
filename
,
events
)
# Update state with latest timestamp
latest_timestamp
=
get_latest_event_timestamp
(
events
)
save_state
(
bucket
,
state_key
,
{
'last_timestamp'
:
latest_timestamp
,
'updated_at'
:
datetime
.
utcnow
()
.
isoformat
()
+
'Z'
})
print
(
f
'Successfully processed
{
len
(
events
)
}
events and stored to
{
filename
}
'
)
else
:
print
(
'No new events found'
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
get_oauth_token
(
api_url
,
client_id
,
client_secret
,
scope
):
"""
Get OAuth access token using client credentials flow for BeyondTrust EPM.
Uses the correct endpoint: /oauth/token
"""
token_url
=
f
"
{
api_url
}
/oauth/token"
headers
=
{
'Content-Type'
:
'application/x-www-form-urlencoded'
}
body
=
f
"grant_type=client_credentials&client_id=
{
client_id
}
&
client_secret=
{
client_secret
}
&
scope=
{
scope
}
"
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
headers
=
headers
,
body
=
body
,
timeout
=
urllib3
.
Timeout
(
60.0
))
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
"Token request failed:
{
response
.
status
}
{
response
.
data
[:
256
]
!r}
"
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
def
fetch_audit_events
(
api_url
,
access_token
,
last_timestamp
,
record_size
,
max_iterations
):
"""
Fetch audit events using the BeyondTrust EPM API endpoint: /management-api/v2/AuditEvents
with query parameters for filtering and pagination
"""
headers
=
{
'Authorization'
:
f
'Bearer
{
access_token
}
'
,
'Content-Type'
:
'application/json'
}
all_events
=
[]
current_start_date
=
last_timestamp
iterations
=
0
# Enforce maximum RecordSize limit of 1000 based on BeyondTrust documentation
record_size_limited
=
min
(
record_size
,
1000
)
while
iterations
<
max_iterations
:
iterations
+=
1
if
len
(
all_events
)
>
=
10000
:
print
(
f
"Reached maximum events limit (10000)"
)
break
# Use the BeyondTrust EPM API endpoint for audit events
query_url
=
f
"
{
api_url
}
/management-api/v2/AuditEvents"
params
=
{
'StartDate'
:
current_start_date
,
'RecordSize'
:
record_size_limited
}
# Construct URL with query parameters
query_string
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
full_url
=
f
"
{
query_url
}
?
{
query_string
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
full_url
,
headers
=
headers
,
timeout
=
urllib3
.
Timeout
(
300.0
))
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
'30'
))
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
"API request failed:
{
response
.
status
}
{
response
.
data
[:
256
]
!r}
"
)
response_data
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
events
=
response_data
.
get
(
'events'
,
[])
if
not
events
:
break
print
(
f
"Page
{
iterations
}
: Retrieved
{
len
(
events
)
}
events"
)
all_events
.
extend
(
events
)
# If we got fewer events than RecordSize, we've reached the end
if
len
(
events
)
<
record_size_limited
:
break
# For pagination, update StartDate to the timestamp of the last event
last_event
=
events
[
-
1
]
last_timestamp
=
extract_event_timestamp
(
last_event
)
if
not
last_timestamp
:
print
(
"Warning: Could not find timestamp in last event for pagination"
)
break
# Convert to datetime and add 1 second to avoid retrieving the same event again
try
:
dt
=
parse_timestamp
(
last_timestamp
)
dt
=
dt
+
timedelta
(
seconds
=
1
)
current_start_date
=
dt
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
)
except
Exception
as
e
:
print
(
f
"Error parsing timestamp
{
last_timestamp
}
:
{
e
}
"
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
"Error fetching page
{
iterations
}
:
{
e
}
"
)
break
return
all_events
def
extract_event_timestamp
(
event
):
"""Extract timestamp from event, checking multiple possible fields"""
# Check common timestamp fields
timestamp_fields
=
[
'event.dateTime'
,
'event.timestamp'
,
'timestamp'
,
'eventTime'
,
'dateTime'
,
'whenOccurred'
,
'date'
,
'time'
,
'event.ingested'
]
# Try nested event.dateTime first (common in BeyondTrust)
if
isinstance
(
event
,
dict
)
and
isinstance
(
event
.
get
(
"event"
),
dict
):
ts
=
event
[
"event"
]
.
get
(
"dateTime"
)
if
ts
:
return
ts
ts
=
event
[
"event"
]
.
get
(
"timestamp"
)
if
ts
:
return
ts
# Fallback to other timestamp fields
for
field
in
timestamp_fields
:
if
field
in
event
and
event
[
field
]:
return
event
[
field
]
return
None
def
parse_timestamp
(
timestamp_str
):
"""Parse timestamp string to datetime object, handling various formats"""
if
isinstance
(
timestamp_str
,
(
int
,
float
)):
# Unix timestamp (in milliseconds or seconds)
if
timestamp_str
>
1e12
:
# Milliseconds
return
datetime
.
fromtimestamp
(
timestamp_str
/
1000
,
tz
=
timezone
.
utc
)
else
:
# Seconds
return
datetime
.
fromtimestamp
(
timestamp_str
,
tz
=
timezone
.
utc
)
if
isinstance
(
timestamp_str
,
str
):
# Try different string formats
try
:
# ISO format with Z
if
timestamp_str
.
endswith
(
'Z'
):
return
datetime
.
fromisoformat
(
timestamp_str
.
replace
(
'Z'
,
'+00:00'
))
# ISO format with timezone
elif
'+'
in
timestamp_str
or
timestamp_str
.
endswith
(
'00:00'
):
return
datetime
.
fromisoformat
(
timestamp_str
)
# ISO format without timezone (assume UTC)
else
:
dt
=
datetime
.
fromisoformat
(
timestamp_str
)
if
dt
.
tzinfo
is
None
:
dt
=
dt
.
replace
(
tzinfo
=
timezone
.
utc
)
return
dt
except
ValueError
:
pass
raise
ValueError
(
f
"Could not parse timestamp:
{
timestamp_str
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
def
store_events_to_gcs
(
bucket
,
key
,
events
):
"""Store events as JSONL (one JSON object per line) in GCS"""
# Convert to JSONL format (one JSON object per line)
jsonl_content
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
event
,
default
=
str
)
for
event
in
events
)
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
jsonl_content
,
content_type
=
'application/x-ndjson'
)
def
get_latest_event_timestamp
(
events
):
"""Get the latest timestamp from the events for state tracking"""
if
not
events
:
return
datetime
.
utcnow
()
.
isoformat
()
+
'Z'
latest
=
None
for
event
in
events
:
timestamp
=
extract_event_timestamp
(
event
)
if
timestamp
:
try
:
event_dt
=
parse_timestamp
(
timestamp
)
event_iso
=
event_dt
.
isoformat
()
+
'Z'
if
latest
is
None
or
event_iso
>
latest
:
latest
=
event_iso
except
Exception
as
e
:
print
(
f
"Error parsing event timestamp
{
timestamp
}
:
{
e
}
"
)
continue
return
latest
or
datetime
.
utcnow
()
.
isoformat
()
+
'Z'
Second file:
requirements.txt:
functions
-
framework
==
3.
*
google
-
cloud
-
storage
==
2.
*
urllib3
>
=
2.0.0
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
beyondtrust-epm-collector-hourly
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
beyondtrust-epm-trigger
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
beyondtrust-epm-collector
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
BeyondTrust EPM logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
BeyondTrust Endpoint Privilege Management
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle
-
12345678
@
chronicle
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
Configure a feed in Google SecOps to ingest BeyondTrust EPM logs
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
BeyondTrust EPM logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
BeyondTrust Endpoint Privilege Management
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs
:
//beyondtrust-epm-logs/beyondtrust-epm/
Replace:
beyondtrust-epm-logs
: Your GCS bucket name.
beyondtrust-epm/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://beyondtrust-epm-logs/
With prefix:
gs://beyondtrust-epm-logs/beyondtrust-epm/
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
Log Field
UDM Mapping
Logic
agent.id
principal.asset.attribute.labels.value
Mapped to label with key agent_id
agent.version
principal.asset.attribute.labels.value
Mapped to label with key agent_version
ecs.version
principal.asset.attribute.labels.value
Mapped to label with key ecs_version
event_data.reason
metadata.description
Event description from raw log
event_datas.ActionId
metadata.product_log_id
Product-specific log identifier
file.path
principal.file.full_path
Full file path from the event
headers.content_length
additional.fields.value.string_value
Mapped to label with key content_length
headers.content_type
additional.fields.value.string_value
Mapped to label with key content_type
headers.http_host
additional.fields.value.string_value
Mapped to label with key http_host
headers.http_version
network.application_protocol_version
HTTP protocol version
headers.request_method
network.http.method
HTTP request method
host.hostname
principal.hostname
Principal hostname
host.hostname
principal.asset.hostname
Principal asset hostname
host.ip
principal.asset.ip
Principal asset IP address
host.ip
principal.ip
Principal IP address
host.mac
principal.mac
Principal MAC address
host.os.platform
principal.platform
Set to MAC if equals macOS
host.os.version
principal.platform_version
Operating system version
labels.related_item_id
metadata.product_log_id
Related item identifier
process.command_line
principal.process.command_line
Process command line
process.name
additional.fields.value.string_value
Mapped to label with key process_name
process.parent.name
additional.fields.value.string_value
Mapped to label with key process_parent_name
process.parent.pid
principal.process.parent_process.pid
Parent process PID converted to string
process.pid
principal.process.pid
Process PID converted to string
user.id
principal.user.userid
User identifier
user.name
principal.user.user_display_name
User display name
N/A
metadata.event_timestamp
Event timestamp set to log entry timestamp
N/A
metadata.event_type
GENERIC_EVENT if no principal, otherwise STATUS_UPDATE
N/A
network.application_protocol
Set to HTTP if http_version field contains HTTP
Need more help?
Get answers from Community members and Google SecOps professionals.
