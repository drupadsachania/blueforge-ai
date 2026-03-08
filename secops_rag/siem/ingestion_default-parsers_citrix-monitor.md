# Collect Citrix Monitor Service logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-monitor/  
**Scraped:** 2026-03-05T09:22:03.796852Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Citrix Monitor Service logs
Supported in:
Google secops
SIEM
This document explains how to ingest Citrix Monitor Service logs to Google Security Operations using Google Cloud Storage. The parser transforms raw JSON formatted logs into a structured format conforming to the Google SecOps UDM. It extracts relevant fields from the raw log, maps them to corresponding UDM fields, and enriches the data with additional context like user information, machine details, and network activity.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Permissions to create service accounts and manage IAM roles
Privileged access to Citrix Cloud tenant
Citrix Cloud API credentials (Client ID, Client Secret, Customer ID)
Collect Citrix Monitor Service prerequisites
Sign in to the
Citrix Cloud Console
.
Go to
Identity and Access Management
>
API Access
.
Click
Create Client
.
Copy and save in a secure location the following details:
Client ID
Client Secret
Customer ID
(visible in Citrix Cloud console)
API Base URL
:
US/EU/AP-S
:
https://api.cloud.com
Japan
:
https://api.citrixcloud.jp
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
citrix-monitor-logs
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
citrix-monitor-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Citrix Monitor Service logs
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
: Enter the service account email (
citrix-monitor-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
citrix-monitor-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Citrix Monitor Service API and writes them to GCS.
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
citrix-monitor-collector
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
, choose the topic (
citrix-monitor-trigger
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
citrix-monitor-collector-sa
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
citrix-monitor-logs
GCS_PREFIX
citrix_monitor
STATE_KEY
citrix_monitor/state.json
CITRIX_CLIENT_ID
your-client-id
CITRIX_CLIENT_SECRET
your-client-secret
CITRIX_CUSTOMER_ID
your-customer-id
API_BASE
https://api.cloud.com
ENTITIES
Machines,Sessions,Connections,Applications,Users
PAGE_SIZE
1000
LOOKBACK_MINUTES
75
USE_TIME_FILTER
true
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
# Citrix Cloud OAuth2 endpoint template
TOKEN_URL_TMPL
=
"
{api_base}
/cctrustoauth2/
{customerid}
/tokens/clients"
DEFAULT_API_BASE
=
"https://api.cloud.com"
MONITOR_BASE_PATH
=
"/monitorodata"
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
def
http_post_form
(
url
,
data_dict
):
"""POST form data to get authentication token."""
encoded_data
=
urllib3
.
request
.
urlencode
(
data_dict
)
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
encoded_data
,
headers
=
{
'Accept'
:
'application/json'
,
'Content-Type'
:
'application/x-www-form-urlencoded'
}
)
return
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
def
http_get_json
(
url
,
headers
):
"""GET JSON data from API endpoint."""
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
return
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
def
get_citrix_token
(
api_base
,
customer_id
,
client_id
,
client_secret
):
"""Get Citrix Cloud authentication token."""
url
=
TOKEN_URL_TMPL
.
format
(
api_base
=
api_base
.
rstrip
(
'/'
),
customerid
=
customer_id
)
payload
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
response
=
http_post_form
(
url
,
payload
)
return
response
[
'access_token'
]
def
build_entity_url
(
api_base
,
entity
,
filter_query
=
None
,
top
=
None
):
"""Build OData URL with optional filter and pagination."""
base
=
api_base
.
rstrip
(
'/'
)
+
MONITOR_BASE_PATH
+
'/'
+
entity
params
=
[]
if
filter_query
:
# Encode filter query with safe characters for OData
encoded_filter
=
urllib3
.
request
.
urlencode
({
'$filter'
:
filter_query
})[
9
:]
# Remove '$filter='
params
.
append
(
'$filter='
+
encoded_filter
)
if
top
:
params
.
append
(
'$top='
+
str
(
top
))
return
base
+
(
'?'
+
'&'
.
join
(
params
)
if
params
else
''
)
def
fetch_entity_rows
(
entity
,
start_iso
=
None
,
end_iso
=
None
,
page_size
=
1000
,
headers
=
None
,
api_base
=
DEFAULT_API_BASE
):
"""Fetch entity data with optional time filtering and pagination."""
first_url
=
None
if
start_iso
and
end_iso
:
filter_query
=
f
"(ModifiedDate ge
{
start_iso
}
and ModifiedDate lt
{
end_iso
}
)"
first_url
=
build_entity_url
(
api_base
,
entity
,
filter_query
,
page_size
)
else
:
first_url
=
build_entity_url
(
api_base
,
entity
,
None
,
page_size
)
url
=
first_url
while
url
:
try
:
data
=
http_get_json
(
url
,
headers
)
items
=
data
.
get
(
'value'
,
[])
for
item
in
items
:
yield
item
url
=
data
.
get
(
'@odata.nextLink'
)
except
Exception
as
e
:
# If ModifiedDate filtering fails, fall back to unfiltered query
if
'Bad Request'
in
str
(
e
)
and
start_iso
and
end_iso
:
print
(
f
"ModifiedDate filter not supported for
{
entity
}
, falling back to unfiltered query"
)
url
=
build_entity_url
(
api_base
,
entity
,
None
,
page_size
)
continue
else
:
raise
def
load_state
(
bucket
,
key
):
"""Read the last processed timestamp from GCS state file."""
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
content
=
blob
.
download_as_text
()
state
=
json
.
loads
(
content
)
timestamp_str
=
state
.
get
(
'last_hour_utc'
)
if
timestamp_str
:
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
.
replace
(
tzinfo
=
None
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
str
(
e
)
}
"
)
return
None
def
save_state
(
bucket
,
key
,
dt_utc
):
"""Write the current processed timestamp to GCS state file."""
state
=
{
'last_hour_utc'
:
dt_utc
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
separators
=
(
','
,
':'
)),
content_type
=
'application/json'
)
def
write_ndjson_to_gcs
(
bucket
,
key
,
rows
):
"""Write rows as NDJSON to GCS."""
body_lines
=
[]
for
row
in
rows
:
json_line
=
json
.
dumps
(
row
,
separators
=
(
','
,
':'
),
ensure_ascii
=
False
)
body_lines
.
append
(
json_line
)
body
=
'
\n
'
.
join
(
body_lines
)
+
'
\n
'
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
body
,
content_type
=
'application/x-ndjson'
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
Cloud Run function triggered by Pub/Sub to fetch Citrix Monitor Service logs and write to GCS.
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
'citrix_monitor'
)
.
strip
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
)
or
f
"
{
prefix
}
/state.json"
customer_id
=
os
.
environ
.
get
(
'CITRIX_CUSTOMER_ID'
)
client_id
=
os
.
environ
.
get
(
'CITRIX_CLIENT_ID'
)
client_secret
=
os
.
environ
.
get
(
'CITRIX_CLIENT_SECRET'
)
api_base
=
os
.
environ
.
get
(
'API_BASE'
,
DEFAULT_API_BASE
)
entities
=
[
e
.
strip
()
for
e
in
os
.
environ
.
get
(
'ENTITIES'
,
'Machines,Sessions,Connections,Applications,Users'
)
.
split
(
','
)
if
e
.
strip
()]
page_size
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
lookback_minutes
=
int
(
os
.
environ
.
get
(
'LOOKBACK_MINUTES'
,
'75'
))
use_time_filter
=
os
.
environ
.
get
(
'USE_TIME_FILTER'
,
'true'
)
.
lower
()
==
'true'
if
not
all
([
bucket_name
,
customer_id
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
# Time window calculation
now
=
datetime
.
utcnow
()
fallback_hour
=
(
now
-
timedelta
(
minutes
=
lookback_minutes
))
.
replace
(
minute
=
0
,
second
=
0
,
microsecond
=
0
)
last_processed
=
load_state
(
bucket
,
state_key
)
target_hour
=
(
last_processed
+
timedelta
(
hours
=
1
))
if
last_processed
else
fallback_hour
start_iso
=
target_hour
.
isoformat
()
+
'Z'
end_iso
=
(
target_hour
+
timedelta
(
hours
=
1
))
.
isoformat
()
+
'Z'
# Authentication
token
=
get_citrix_token
(
api_base
,
customer_id
,
client_id
,
client_secret
)
headers
=
{
'Authorization'
:
f
'CWSAuth bearer=
{
token
}
'
,
'Citrix-CustomerId'
:
customer_id
,
'Accept'
:
'application/json'
,
'Accept-Encoding'
:
'gzip, deflate, br'
,
'User-Agent'
:
'citrix-monitor-gcs-collector/1.0'
}
total_records
=
0
# Process each entity type
for
entity
in
entities
:
rows_batch
=
[]
try
:
entity_generator
=
fetch_entity_rows
(
entity
=
entity
,
start_iso
=
start_iso
if
use_time_filter
else
None
,
end_iso
=
end_iso
if
use_time_filter
else
None
,
page_size
=
page_size
,
headers
=
headers
,
api_base
=
api_base
)
for
row
in
entity_generator
:
# Store raw Citrix data directly for proper parser recognition
rows_batch
.
append
(
row
)
# Write in batches to avoid memory issues
if
len
(
rows_batch
)
>
=
1000
:
gcs_key
=
f
"
{
prefix
}
/
{
entity
}
/year=
{
target_hour
.
year
:
04d
}
/month=
{
target_hour
.
month
:
02d
}
/day=
{
target_hour
.
day
:
02d
}
/hour=
{
target_hour
.
hour
:
02d
}
/part-
{
uuid
.
uuid4
()
.
hex
}
.ndjson"
write_ndjson_to_gcs
(
bucket
,
gcs_key
,
rows_batch
)
total_records
+=
len
(
rows_batch
)
rows_batch
=
[]
except
Exception
as
ex
:
print
(
f
"Error processing entity
{
entity
}
:
{
str
(
ex
)
}
"
)
continue
# Write remaining records
if
rows_batch
:
gcs_key
=
f
"
{
prefix
}
/
{
entity
}
/year=
{
target_hour
.
year
:
04d
}
/month=
{
target_hour
.
month
:
02d
}
/day=
{
target_hour
.
day
:
02d
}
/hour=
{
target_hour
.
hour
:
02d
}
/part-
{
uuid
.
uuid4
()
.
hex
}
.ndjson"
write_ndjson_to_gcs
(
bucket
,
gcs_key
,
rows_batch
)
total_records
+=
len
(
rows_batch
)
# Update state file
save_state
(
bucket
,
state_key
,
target_hour
)
print
(
f
"Successfully processed
{
total_records
}
records for hour
{
start_iso
}
"
)
print
(
f
"Entities processed:
{
', '
.
join
(
entities
)
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
'Error processing Citrix Monitor logs:
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
citrix-monitor-collector-hourly
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
Select the topic (
citrix-monitor-trigger
)
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
citrix-monitor-collector
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
Citrix Monitor Service logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Citrix Monitor
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
Configure a feed in Google SecOps to ingest Citrix Monitor Service logs
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
Citrix Monitor Service logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Citrix Monitor
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://citrix-monitor-logs/citrix_monitor/
Replace:
citrix-monitor-logs
: Your GCS bucket name.
citrix_monitor
: Optional prefix/folder path where logs are stored (leave empty for root).
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
