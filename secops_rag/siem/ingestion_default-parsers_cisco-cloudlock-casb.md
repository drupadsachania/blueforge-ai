# Collect Cisco CloudLock CASB logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb/  
**Scraped:** 2026-03-05T09:21:18.432789Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco CloudLock CASB logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco CloudLock CASB logs to Google Security Operations using Google Cloud Storage .The parser extracts fields from the JSON logs, transforms and maps them to the Unified Data Model (UDM). It handles date parsing, converts specific fields to strings, maps fields to UDM entities (metadata, target, security result, about), and iterates through matches to extract detection fields, ultimately merging all extracted data into the @output field.
Cisco CloudLock is a cloud-native Cloud Access Security Broker (CASB) that provides visibility and control over cloud applications. It helps organizations discover shadow IT, enforce data loss prevention policies, detect threats, and maintain compliance across SaaS applications.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Cisco CloudLock admin console
Get Cisco CloudLock API prerequisites
To get started, contact Cloudlock Support to obtain your Cloudlock API URL. Generate an access token in the Cloudlock application by selecting the Authentication & API tab in the Settings page and clicking Generate.
Sign in to the
Cisco CloudLock
admin console.
Go to
Settings
>
Authentication & API
.
Under
API
, click
Generate
to create your access token.
Copy and save the following details in a secure location:
API Access Token
API Base URL
(provided by Cisco CloudLock Support at [email protected])
Create Google Cloud Storage bucket
Go to the
Google Cloud console
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
cisco-cloudlock-logs
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
cloudlock-data-export-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Cisco CloudLock logs
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
Grant IAM permissions on GCS bucket
Grant the service account write permissions on the GCS bucket:
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
cloudlock-data-export-sa@PROJECT_ID.iam.gserviceaccount.com
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
cloudlock-data-export-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco CloudLock API and write them to GCS.
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
cloudlock-data-export
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
cloudlock-data-export-trigger
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
Scroll to and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select the service account (
cloudlock-data-export-sa
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
cisco-cloudlock-logs
GCS_PREFIX
cloudlock/
STATE_KEY
cloudlock/state.json
CLOUDLOCK_API_TOKEN
your-api-token
CLOUDLOCK_API_BASE
https://api.cloudlock.com
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
will open automatically.
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
Cloud Run function triggered by Pub/Sub to fetch logs from Cisco CloudLock API and write to GCS.
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
'cloudlock/'
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
'cloudlock/state.json'
)
api_token
=
os
.
environ
.
get
(
'CLOUDLOCK_API_TOKEN'
)
api_base
=
os
.
environ
.
get
(
'CLOUDLOCK_API_BASE'
)
if
not
all
([
bucket_name
,
api_token
,
api_base
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
# Load state (last processed offset for each endpoint)
state
=
load_state
(
bucket
,
state_key
)
print
(
f
'Processing logs with state:
{
state
}
'
)
# Create Authorization header
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
'Content-Type'
:
'application/json'
}
# Fetch incidents data (using offset-based pagination)
incidents_offset
=
state
.
get
(
'incidents_offset'
,
0
)
incidents
,
new_incidents_offset
=
fetch_cloudlock_incidents
(
http
,
api_base
,
headers
,
incidents_offset
)
if
incidents
:
upload_to_gcs_ndjson
(
bucket
,
prefix
,
'incidents'
,
incidents
)
print
(
f
'Uploaded
{
len
(
incidents
)
}
incidents to GCS'
)
state
[
'incidents_offset'
]
=
new_incidents_offset
# Fetch activities data (using time-based filtering with offset pagination)
activities_last_time
=
state
.
get
(
'activities_last_time'
)
if
not
activities_last_time
:
activities_last_time
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
24
))
.
isoformat
()
activities_offset
=
state
.
get
(
'activities_offset'
,
0
)
activities
,
new_activities_offset
,
newest_activity_time
=
fetch_cloudlock_activities
(
http
,
api_base
,
headers
,
activities_last_time
,
activities_offset
)
if
activities
:
upload_to_gcs_ndjson
(
bucket
,
prefix
,
'activities'
,
activities
)
print
(
f
'Uploaded
{
len
(
activities
)
}
activities to GCS'
)
state
[
'activities_offset'
]
=
new_activities_offset
if
newest_activity_time
:
state
[
'activities_last_time'
]
=
newest_activity_time
# Fetch entities data (using offset-based pagination)
entities_offset
=
state
.
get
(
'entities_offset'
,
0
)
entities
,
new_entities_offset
=
fetch_cloudlock_entities
(
http
,
api_base
,
headers
,
entities_offset
)
if
entities
:
upload_to_gcs_ndjson
(
bucket
,
prefix
,
'entities'
,
entities
)
print
(
f
'Uploaded
{
len
(
entities
)
}
entities to GCS'
)
state
[
'entities_offset'
]
=
new_entities_offset
# Update consolidated state
state
[
'updated_at'
]
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
isoformat
()
save_state
(
bucket
,
state_key
,
state
)
print
(
'CloudLock data export completed successfully'
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
make_api_request
(
http
,
url
,
headers
,
retries
=
3
):
"""Make API request with exponential backoff retry logic."""
for
attempt
in
range
(
retries
):
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
if
response
.
status
==
200
:
return
response
elif
response
.
status
==
429
:
# Rate limit
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
60
))
print
(
f
'Rate limited, waiting
{
retry_after
}
seconds'
)
time
.
sleep
(
retry_after
)
else
:
print
(
f
'API request failed with status
{
response
.
status
}
:
{
response
.
data
.
decode
(
"utf-8"
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
'Request attempt
{
attempt
+
1
}
failed:
{
str
(
e
)
}
'
)
if
attempt
<
retries
-
1
:
wait_time
=
2
**
attempt
time
.
sleep
(
wait_time
)
else
:
raise
return
None
def
fetch_cloudlock_incidents
(
http
,
api_base
,
headers
,
start_offset
=
0
):
"""
Fetch incidents data from Cisco CloudLock API using offset-based pagination.
Note: The CloudLock API does not support updated_after parameter. This function
uses offset-based pagination. For production use, consider implementing time-based
filtering using created_at or updated_at fields in the response data.
"""
url
=
f
"
{
api_base
}
/api/v2/incidents"
limit
=
1000
offset
=
start_offset
all_data
=
[]
try
:
while
True
:
# Build URL with parameters
full_url
=
f
"
{
url
}
?limit=
{
limit
}
&
offset=
{
offset
}
"
print
(
f
"Fetching incidents with offset:
{
offset
}
"
)
response
=
make_api_request
(
http
,
full_url
,
headers
)
if
not
response
:
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
# CloudLock API returns items in 'items' array
batch_data
=
data
.
get
(
'items'
,
[])
if
not
batch_data
:
print
(
"No more incidents to fetch"
)
break
all_data
.
extend
(
batch_data
)
# Check if we've reached the end
total
=
data
.
get
(
'total'
,
0
)
results
=
data
.
get
(
'results'
,
len
(
batch_data
))
print
(
f
"Fetched
{
results
}
incidents (total available:
{
total
}
)"
)
if
results
<
limit
or
offset
+
results
>
=
total
:
print
(
"Reached end of incidents"
)
break
offset
+=
limit
print
(
f
"Fetched
{
len
(
all_data
)
}
total incidents"
)
return
all_data
,
offset
except
Exception
as
e
:
print
(
f
"Error fetching incidents:
{
str
(
e
)
}
"
)
return
[],
start_offset
def
fetch_cloudlock_activities
(
http
,
api_base
,
headers
,
from_time
,
start_offset
=
0
):
"""
Fetch activities data from Cisco CloudLock API using time-based filtering and offset pagination.
"""
url
=
f
"
{
api_base
}
/api/v2/activities"
limit
=
1000
offset
=
start_offset
all_data
=
[]
newest_time
=
None
try
:
while
True
:
# Build URL with time filter and pagination
full_url
=
f
"
{
url
}
?limit=
{
limit
}
&
offset=
{
offset
}
"
print
(
f
"Fetching activities with offset:
{
offset
}
"
)
response
=
make_api_request
(
http
,
full_url
,
headers
)
if
not
response
:
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
batch_data
=
data
.
get
(
'items'
,
[])
if
not
batch_data
:
print
(
"No more activities to fetch"
)
break
# Filter activities by time (client-side filtering since API may not support time parameters)
filtered_batch
=
[]
for
item
in
batch_data
:
item_time
=
item
.
get
(
'timestamp'
)
or
item
.
get
(
'created_at'
)
if
item_time
and
item_time
>
=
from_time
:
filtered_batch
.
append
(
item
)
if
not
newest_time
or
item_time
>
newest_time
:
newest_time
=
item_time
all_data
.
extend
(
filtered_batch
)
results
=
data
.
get
(
'results'
,
len
(
batch_data
))
total
=
data
.
get
(
'total'
,
0
)
print
(
f
"Fetched
{
results
}
activities,
{
len
(
filtered_batch
)
}
after time filter (total available:
{
total
}
)"
)
if
results
<
limit
or
offset
+
results
>
=
total
:
print
(
"Reached end of activities"
)
break
offset
+=
limit
print
(
f
"Fetched
{
len
(
all_data
)
}
total activities"
)
return
all_data
,
offset
,
newest_time
except
Exception
as
e
:
print
(
f
"Error fetching activities:
{
str
(
e
)
}
"
)
return
[],
start_offset
,
None
def
fetch_cloudlock_entities
(
http
,
api_base
,
headers
,
start_offset
=
0
):
"""
Fetch entities data from Cisco CloudLock API using offset-based pagination.
Note: This endpoint requires the Entity Cache feature. If not enabled,
use the incident entities endpoint as an alternative.
"""
url
=
f
"
{
api_base
}
/api/v2/entities"
limit
=
1000
offset
=
start_offset
all_data
=
[]
try
:
while
True
:
full_url
=
f
"
{
url
}
?limit=
{
limit
}
&
offset=
{
offset
}
"
print
(
f
"Fetching entities with offset:
{
offset
}
"
)
response
=
make_api_request
(
http
,
full_url
,
headers
)
if
not
response
:
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
batch_data
=
data
.
get
(
'items'
,
[])
if
not
batch_data
:
print
(
"No more entities to fetch"
)
break
all_data
.
extend
(
batch_data
)
results
=
data
.
get
(
'results'
,
len
(
batch_data
))
total
=
data
.
get
(
'total'
,
0
)
print
(
f
"Fetched
{
results
}
entities (total available:
{
total
}
)"
)
if
results
<
limit
or
offset
+
results
>
=
total
:
print
(
"Reached end of entities"
)
break
offset
+=
limit
print
(
f
"Fetched
{
len
(
all_data
)
}
total entities"
)
return
all_data
,
offset
except
Exception
as
e
:
print
(
f
"Error fetching entities:
{
str
(
e
)
}
"
)
return
[],
start_offset
def
upload_to_gcs_ndjson
(
bucket
,
prefix
,
data_type
,
data
):
"""Upload data to GCS bucket in NDJSON format (one JSON object per line)."""
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
'%Y/%m/
%d
/%H'
)
filename
=
f
"
{
prefix
}{
data_type
}
/
{
timestamp
}
/cloudlock_
{
data_type
}
_
{
int
(
datetime
.
now
(
timezone
.
utc
)
.
timestamp
())
}
.jsonl"
try
:
# Convert to NDJSON format
ndjson_content
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
item
,
separators
=
(
','
,
':'
))
for
item
in
data
])
blob
=
bucket
.
blob
(
filename
)
blob
.
upload_from_string
(
ndjson_content
,
content_type
=
'application/x-ndjson'
)
print
(
f
"Successfully uploaded
{
filename
}
to GCS"
)
except
Exception
as
e
:
print
(
f
"Error uploading to GCS:
{
str
(
e
)
}
"
)
raise
def
load_state
(
bucket
,
key
):
"""Load state from GCS with separate tracking for each endpoint."""
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
print
(
"No previous state found, starting fresh"
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
"""Save consolidated state to GCS."""
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
)
print
(
"Updated state successfully"
)
except
Exception
as
e
:
print
(
f
"Error updating state:
{
str
(
e
)
}
"
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
cloudlock-data-export-hourly
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
cloudlock-data-export-trigger
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
console, find your job.
Click
Force run
to trigger manually.
Wait a few seconds and go to
Cloud Run
>
Services
>
cloudlock-data-export
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
Cisco CloudLock logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cisco CloudLock
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
Click on your bucket name.
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
Configure a feed in Google SecOps to ingest Cisco CloudLock logs
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
Cisco CloudLock logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cisco CloudLock
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://cisco-cloudlock-logs/cloudlock/
Replace:
cisco-cloudlock-logs
: Your GCS bucket name.
cloudlock/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://cisco-cloudlock-logs/
With prefix:
gs://cisco-cloudlock-logs/cloudlock/
With subfolder:
gs://cisco-cloudlock-logs/cloudlock/incidents/
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
created_at
about.resource.attribute.labels.key
The created_at field's value is assigned to the labels key.
created_at
about.resource.attribute.labels.value
The created_at field's value is assigned to the labels value.
created_at
about.resource.attribute.creation_time
The created_at field is parsed as a timestamp and mapped.
entity.id
target.asset.product_object_id
The entity.id field is renamed.
entity.ip
target.ip
The entity.ip field is merged into the target IP field.
entity.mime_type
target.file.mime_type
The entity.mime_type field is renamed when entity.origin_type is "document".
entity.name
target.application
The entity.name field is renamed when entity.origin_type is "app".
entity.name
target.file.full_path
The entity.name field is renamed when entity.origin_type is "document".
entity.origin_id
target.resource.product_object_id
The entity.origin_id field is renamed.
entity.origin_type
target.resource.resource_subtype
The entity.origin_type field is renamed.
entity.owner_email
target.user.email_addresses
The entity.owner_email field is merged into the target user email field if it matches an email regex.
entity.owner_email
target.user.user_display_name
The entity.owner_email field is renamed if it does not match an email regex.
entity.owner_name
target.user.user_display_name
The entity.owner_name field is renamed when entity.owner_email matches an email regex.
entity.vendor.name
target.platform_version
The entity.vendor.name field is renamed.
id
metadata.product_log_id
The id field is renamed.
incident_status
metadata.product_event_type
The incident_status field is renamed.
metadata.event_timestamp
Value is hardcoded to "updated_at". Value is derived from the updated_at field. The updated_at field is parsed as a timestamp and mapped.
security_result.detection_fields.key
Set to "true" if severity is "ALERT" and incident_status is "NEW". Converted to boolean.
security_result.detection_fields.value
Set to "true" if severity is "ALERT" and incident_status is "NEW". Converted to boolean.
metadata.event_type
Value is hardcoded to "GENERIC_EVENT".
metadata.product_name
Value is hardcoded to "CISCO_CLOUDLOCK_CASB".
metadata.vendor_name
Value is hardcoded to "CloudLock".
metadata.product_version
Value is hardcoded to "Cisco".
security_result.alert_state
Set to "ALERTING" if severity is "ALERT" and incident_status is not "RESOLVED" or "DISMISSED". Set to "NOT_ALERTING" if severity is "ALERT" and incident_status is "RESOLVED" or "DISMISSED".
security_result.detection_fields.key
Derived from the matches array, specifically the key of each match object.
security_result.detection_fields.value
Derived from the matches array, specifically the value of each match object.
security_result.rule_id
Derived from policy.id.
security_result.rule_name
Derived from policy.name.
security_result.severity
Set to "INFORMATIONAL" if severity is "INFO". Set to "CRITICAL" if severity is "CRITICAL". Derived from severity.
security_result.summary
The value is set to "match count: " concatenated with the value of match_count.
target.resource.resource_type
Set to "STORAGE_OBJECT" when entity.origin_type is "document".
target.url
Derived from entity.direct_url when entity.origin_type is "document".
policy.id
security_result.rule_id
The policy.id field is renamed.
policy.name
security_result.rule_name
The policy.name field is renamed.
severity
security_result.severity_details
The severity field is renamed.
updated_at
about.resource.attribute.labels.key
The updated_at field's value is assigned to the labels key.
updated_at
about.resource.attribute.labels.value
The updated_at field's value is assigned to the labels value.
updated_at
about.resource.attribute.last_update_time
The updated_at field is parsed as a timestamp and mapped.
Need more help?
Get answers from Community members and Google SecOps professionals.
