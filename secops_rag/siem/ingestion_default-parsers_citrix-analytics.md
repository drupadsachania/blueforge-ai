# Collect Citrix Analytics logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-analytics/  
**Scraped:** 2026-03-05T09:22:02.771047Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Citrix Analytics logs
Supported in:
Google secops
SIEM
This document explains how to ingest Citrix Analytics logs to Google Security Operations using Google Cloud Storage. Citrix Analytics for Performance provides aggregated data from performance data sources, enabling you to fetch session, machine, and user data.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Citrix Analytics for Performance tenant
Citrix Cloud API credentials (Client ID, Client Secret, Customer ID)
Collect Citrix Analytics API credentials
Sign in to the Citrix Cloud Console. In the Citrix Cloud console, click the menu in the upper left corner of the screen. Select the Identity and Access Management option from the menu. Select the API Access tab.
Click
Create Client
.
Copy and save in a secure location the following details:
Client ID
Client Secret
Customer ID
(located in the Citrix Cloud URL or IAM page)
API Base URL
:
https://api.cloud.com/casodata
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
citrix-analytics-logs
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
citrix-analytics-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Citrix Analytics logs
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
: Enter the service account email.
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
citrix-analytics-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Citrix Analytics OData API and writes them to GCS.
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
citrix-analytics-collector
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
citrix-analytics-trigger
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
citrix-analytics-collector-sa
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
citrix-analytics-logs
GCS_PREFIX
citrix_analytics
STATE_KEY
citrix_analytics/state.json
CITRIX_CLIENT_ID
your-client-id
CITRIX_CLIENT_SECRET
your-client-secret
CITRIX_CUSTOMER_ID
your-customer-id
API_BASE
https://api.cloud.com/casodata
ENTITIES
sessions,machines,users
TOP_N
1000
LOOKBACK_MINUTES
75
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
Scroll down to
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
urllib.parse
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
CITRIX_TOKEN_URL_TMPL
=
"https://api.cloud.com/cctrustoauth2/
{customerid}
/tokens/clients"
DEFAULT_API_BASE
=
"https://api.cloud.com/casodata"
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch logs from Citrix Analytics API and write to GCS.
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
'citrix_analytics'
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
'sessions,machines,users'
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
top_n
=
int
(
os
.
environ
.
get
(
'TOP_N'
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
# Determine target hour to collect
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
fallback_target
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
# Load state (last processed timestamp)
state
=
load_state
(
bucket
,
state_key
)
last_processed_str
=
state
.
get
(
'last_hour_utc'
)
if
last_processed_str
:
last_processed
=
datetime
.
fromisoformat
(
last_processed_str
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
target_hour
=
last_processed
+
timedelta
(
hours
=
1
)
else
:
target_hour
=
fallback_target
print
(
f
'Processing logs for hour:
{
target_hour
.
isoformat
()
}
Z'
)
# Get authentication token
token
=
get_citrix_token
(
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
'CwsAuth bearer=
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
'Content-Type'
:
'application/json'
,
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
records
=
[]
for
row
in
fetch_odata_entity
(
entity
,
target_hour
,
top_n
,
headers
,
api_base
):
enriched_record
=
{
'citrix_entity'
:
entity
,
'citrix_hour_utc'
:
target_hour
.
isoformat
()
+
'Z'
,
'collection_timestamp'
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
,
'raw'
:
row
}
records
.
append
(
enriched_record
)
# Write in batches to avoid memory issues
if
len
(
records
)
>
=
1000
:
blob_name
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
%H%M%S
%f
'
)
}
.ndjson"
write_ndjson_to_gcs
(
bucket
,
blob_name
,
records
)
total_records
+=
len
(
records
)
records
=
[]
# Write remaining records
if
records
:
blob_name
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
%H%M%S
%f
'
)
}
.ndjson"
write_ndjson_to_gcs
(
bucket
,
blob_name
,
records
)
total_records
+=
len
(
records
)
# Update state file
save_state
(
bucket
,
state_key
,
{
'last_hour_utc'
:
target_hour
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
total_records
}
records for hour
{
target_hour
.
isoformat
()
}
Z'
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
get_citrix_token
(
customer_id
,
client_id
,
client_secret
):
"""Get Citrix Cloud authentication token."""
url
=
CITRIX_TOKEN_URL_TMPL
.
format
(
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
,
}
data
=
urllib
.
parse
.
urlencode
(
payload
)
.
encode
(
'utf-8'
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
data
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
,
}
)
token_response
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
token_response
[
'access_token'
]
def
fetch_odata_entity
(
entity
,
when_utc
,
top
,
headers
,
api_base
):
"""Fetch data from Citrix Analytics OData API with pagination."""
year
=
when_utc
.
year
month
=
when_utc
.
month
day
=
when_utc
.
day
hour
=
when_utc
.
hour
base_url
=
f
"
{
api_base
.
rstrip
(
'/'
)
}
/
{
entity
}
?year=
{
year
:
04d
}
&
month=
{
month
:
02d
}
&
day=
{
day
:
02d
}
&
hour=
{
hour
:
02d
}
"
skip
=
0
while
True
:
url
=
f
"
{
base_url
}
&
$top=
{
top
}
&
$skip=
{
skip
}
"
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
items
=
data
.
get
(
'value'
,
[])
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
yield
item
if
len
(
items
)
<
top
:
break
skip
+=
top
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
write_ndjson_to_gcs
(
bucket
,
key
,
records
):
"""Write records as NDJSON to GCS."""
body_lines
=
[]
for
record
in
records
:
json_line
=
json
.
dumps
(
record
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
(
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
)
.
encode
(
'utf-8'
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
body
,
content_type
=
'application/x-ndjson'
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
citrix-analytics-collector-hourly
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
citrix-analytics-trigger
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
Every hour
0 * * * *
Standard (recommended)
Every 2 hours
0 */2 * * *
Lower volume
Every 6 hours
0 */6 * * *
Low volume, batch processing
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
citrix-analytics-collector
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
Citrix Analytics Performance logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Citrix Analytics
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
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
Configure a feed in Google SecOps to ingest Citrix Analytics logs
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
Citrix Analytics logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Citrix Analytics
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://citrix-analytics-logs/citrix_analytics/
Replace:
citrix-analytics-logs
: Your GCS bucket name.
citrix_analytics
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://citrix-analytics-logs/
With prefix:
gs://citrix-analytics-logs/citrix_analytics/
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
