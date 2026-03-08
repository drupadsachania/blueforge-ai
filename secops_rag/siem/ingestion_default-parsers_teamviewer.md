# Collect TeamViewer logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teamviewer/  
**Scraped:** 2026-03-05T09:29:17.606377Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect TeamViewer logs
Supported in:
Google secops
SIEM
This document explains how to ingest TeamViewer logs to Google Security Operations using Google Cloud Storage. The parser extracts the audit events from JSON formatted logs. It iterates through event details, mapping specific properties to Unified Data Model (UDM) fields, handling participant and presenter information, and categorizing events based on user activity. The parser also performs data transformations, such as merging labels and converting timestamps to a standardized format.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to TeamViewer Management Console
TeamViewer Business, Premium, Corporate, or Tensor license (required for API access)
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
teamviewer-logs
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
Get TeamViewer prerequisites
Sign in to the
TeamViewer Management Console
at
https://login.teamviewer.com/
.
Click on your user icon in the upper right corner and select
Edit profile
.
Select
Apps
.
Click
Create script token
.
Provide the following configuration details:
Token name
: Enter a descriptive name (for example,
Google SecOps Integration
).
Permissions
: Select the following permissions:
Account management
>
View account data
Session management
>
View session data
Connection reporting
>
View connection reports
Click
Create
.
Copy and save the generated script token in a secure location.
Record your TeamViewer API Base URL:
https://webapi.teamviewer.com/api/v1
Verify permissions
To verify the account has the required permissions:
Sign in to the
TeamViewer Management Console
.
Go to
Edit profile
>
Apps
.
Locate your script token in the list.
Verify that
Connection reporting
>
View connection reports
is enabled.
If this permission is not enabled, edit the token and add the required permission.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual script token
SCRIPT_TOKEN
=
"your-script-token"
API_BASE
=
"https://webapi.teamviewer.com/api/v1"
# Test API access
curl
-v
-H
"Authorization: Bearer
${
SCRIPT_TOKEN
}
"
\
-H
"Accept: application/json"
\
"
${
API_BASE
}
/reports/connections?from_date=2024-01-01T00:00:00Z&to_date=2024-01-01T01:00:00Z"
If you receive a 200 response with JSON data, your credentials are configured correctly.
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
teamviewer-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect TeamViewer logs
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
-
Storage Object Admin
: Write logs to GCS bucket and manage state files
-
Cloud Run Invoker
: Allow Pub/Sub to invoke the function
-
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
teamviewer-logs
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
teamviewer-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
teamviewer-logs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from TeamViewer API and writes them to GCS.
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
teamviewer-logs-collector
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
teamviewer-logs-trigger
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
teamviewer-collector-sa
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
teamviewer-logs
GCS_PREFIX
teamviewer/audit/
STATE_KEY
teamviewer/audit/state.json
WINDOW_SECONDS
3600
HTTP_TIMEOUT
60
MAX_RETRIES
3
USER_AGENT
teamviewer-to-gcs/1.0
SCRIPT_TOKEN
your-script-token
(from TeamViewer prerequisites)
API_BASE_URL
https://webapi.teamviewer.com/api/v1
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
urllib.request
import
urllib.parse
import
urllib.error
from
datetime
import
datetime
,
timezone
import
time
import
uuid
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
Cloud Run function triggered by Pub/Sub to fetch TeamViewer audit logs and write to GCS.
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
'teamviewer/audit/'
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
'teamviewer/audit/state.json'
)
window_sec
=
int
(
os
.
environ
.
get
(
'WINDOW_SECONDS'
,
'3600'
))
http_timeout
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
max_retries
=
int
(
os
.
environ
.
get
(
'MAX_RETRIES'
,
'3'
))
user_agent
=
os
.
environ
.
get
(
'USER_AGENT'
,
'teamviewer-to-gcs/1.0'
)
# TeamViewer API credentials
api_base_url
=
os
.
environ
.
get
(
'API_BASE_URL'
)
script_token
=
os
.
environ
.
get
(
'SCRIPT_TOKEN'
)
if
not
all
([
bucket_name
,
api_base_url
,
script_token
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
now
=
time
.
time
()
from_ts
=
float
(
state
.
get
(
'last_to_ts'
)
or
(
now
-
window_sec
))
to_ts
=
now
print
(
f
'Fetching TeamViewer audit data from
{
iso_format
(
from_ts
)
}
to
{
iso_format
(
to_ts
)
}
'
)
# Build audit API URL
url
=
build_audit_url
(
api_base_url
,
from_ts
,
to_ts
)
print
(
f
'Fetching TeamViewer audit data from:
{
url
}
'
)
# Fetch audit data with retries and pagination
all_records
=
[]
offset_id
=
None
while
True
:
blob_data
,
content_type
,
next_offset
=
fetch_audit_data
(
url
,
script_token
,
user_agent
,
http_timeout
,
max_retries
,
offset_id
)
# Validate JSON data
try
:
audit_data
=
json
.
loads
(
blob_data
)
records
=
audit_data
.
get
(
'records'
,
[])
all_records
.
extend
(
records
)
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
audit records (total:
{
len
(
all_records
)
}
)"
)
# Check for pagination
if
next_offset
and
len
(
records
)
==
1000
:
offset_id
=
next_offset
print
(
f
"Fetching next page with offset_id:
{
offset_id
}
"
)
else
:
break
except
json
.
JSONDecodeError
as
e
:
print
(
f
"Warning: Invalid JSON received:
{
e
}
"
)
break
if
all_records
:
# Write to GCS
key
=
put_audit_data
(
bucket
,
prefix
,
json
.
dumps
({
'records'
:
all_records
}),
'application/json'
,
from_ts
,
to_ts
)
print
(
f
'Successfully wrote
{
len
(
all_records
)
}
audit records to
{
key
}
'
)
else
:
print
(
'No audit records found'
)
# Update state
state
[
'last_to_ts'
]
=
to_ts
state
[
'last_successful_run'
]
=
now
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
'Error processing TeamViewer logs:
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
iso_format
(
ts
):
"""Convert Unix timestamp to ISO 8601 format."""
return
time
.
strftime
(
'%Y-%m-
%d
T%H:%M:%SZ'
,
time
.
gmtime
(
ts
))
def
build_audit_url
(
api_base_url
,
from_ts
,
to_ts
):
"""Build URL for TeamViewer audit API endpoint."""
base_endpoint
=
f
"
{
api_base_url
.
rstrip
(
'/'
)
}
/reports/connections"
params
=
{
'from_date'
:
iso_format
(
from_ts
),
'to_date'
:
iso_format
(
to_ts
)
}
query_string
=
urllib
.
parse
.
urlencode
(
params
)
return
f
"
{
base_endpoint
}
?
{
query_string
}
"
def
fetch_audit_data
(
url
,
script_token
,
user_agent
,
http_timeout
,
max_retries
,
offset_id
=
None
):
"""Fetch audit data from TeamViewer API with retries and pagination support."""
# Add offset_id parameter if provided
if
offset_id
:
separator
=
'&'
if
'?'
in
url
else
'?'
url
=
f
"
{
url
}{
separator
}
offset_id=
{
offset_id
}
"
attempt
=
0
while
True
:
req
=
urllib
.
request
.
Request
(
url
,
method
=
'GET'
)
req
.
add_header
(
'User-Agent'
,
user_agent
)
req
.
add_header
(
'Authorization'
,
f
'Bearer
{
script_token
}
'
)
req
.
add_header
(
'Accept'
,
'application/json'
)
try
:
with
urllib
.
request
.
urlopen
(
req
,
timeout
=
http_timeout
)
as
r
:
response_data
=
r
.
read
()
content_type
=
r
.
headers
.
get
(
'Content-Type'
)
or
'application/json'
# Extract next_offset from response if present
try
:
data
=
json
.
loads
(
response_data
)
next_offset
=
data
.
get
(
'next_offset'
)
except
:
next_offset
=
None
return
response_data
,
content_type
,
next_offset
except
urllib
.
error
.
HTTPError
as
e
:
if
e
.
code
==
429
:
attempt
+=
1
print
(
f
'Rate limited (429) on attempt
{
attempt
}
'
)
if
attempt
>
max_retries
:
raise
time
.
sleep
(
min
(
60
,
2
**
attempt
)
+
(
time
.
time
()
%
1
))
else
:
print
(
f
'HTTP error
{
e
.
code
}
:
{
e
.
reason
}
'
)
raise
except
urllib
.
error
.
URLError
as
e
:
attempt
+=
1
print
(
f
'URL error on attempt
{
attempt
}
:
{
e
}
'
)
if
attempt
>
max_retries
:
raise
time
.
sleep
(
min
(
60
,
2
**
attempt
)
+
(
time
.
time
()
%
1
))
def
put_audit_data
(
bucket
,
prefix
,
blob_data
,
content_type
,
from_ts
,
to_ts
):
"""Write audit data to GCS."""
ts_path
=
time
.
strftime
(
'%Y/%m/
%d
'
,
time
.
gmtime
(
to_ts
))
uniq
=
f
"
{
int
(
time
.
time
()
*
1e6
)
}
_
{
uuid
.
uuid4
()
.
hex
[:
8
]
}
"
key
=
f
"
{
prefix
}{
ts_path
}
/teamviewer_audit_
{
int
(
from_ts
)
}
_
{
int
(
to_ts
)
}
_
{
uniq
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
metadata
=
{
'source'
:
'teamviewer-audit'
,
'from_timestamp'
:
str
(
int
(
from_ts
)),
'to_timestamp'
:
str
(
int
(
to_ts
))
}
blob
.
upload_from_string
(
blob_data
,
content_type
=
content_type
)
return
key
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
teamviewer-logs-collector-hourly
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
teamviewer-logs-trigger
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
teamviewer-logs-collector-hourly
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
Click on the function name (
teamviewer-logs-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching TeamViewer audit data from YYYY-MM-DDTHH:MM:SSZ to YYYY-MM-DDTHH:MM:SSZ
Retrieved X audit records (total: X)
Successfully wrote X audit records to teamviewer/audit/YYYY/MM/DD/teamviewer_audit_...json
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
teamviewer-logs
).
Navigate to the prefix folder (
teamviewer/audit/
).
Verify that a new
.json
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check the
SCRIPT_TOKEN
environment variable matches your TeamViewer script token
HTTP 403
: Verify the script token has
Connection reporting
>
View connection reports
permission
HTTP 429
: Rate limiting - function will automatically retry with exponential backoff
Missing environment variables
: Check all required variables (
GCS_BUCKET
,
API_BASE_URL
,
SCRIPT_TOKEN
) are set
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
TeamViewer logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
TeamViewer
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
teamviewer-logs
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
Configure a feed in Google SecOps to ingest TeamViewer logs
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
TeamViewer logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
TeamViewer
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://teamviewer-logs/teamviewer/audit/
Replace:
teamviewer-logs
: Your GCS bucket name.
teamviewer/audit/
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
UDM mapping table
Log field
UDM mapping
Logic
AffectedItem
metadata.product_log_id
The value of AffectedItem from the raw log is directly mapped to this UDM field.
EventDetails.NewValue
principal.resource.attribute.labels.value
If PropertyName contains (server), the NewValue is used as the value of a label in principal.resource.attribute.labels.
EventDetails.NewValue
principal.user.user_display_name
If PropertyName is Name of participant, the NewValue is used as the user display name for the principal.
EventDetails.NewValue
principal.user.userid
If PropertyName is ID of participant, the NewValue is used as the user ID for the principal.
EventDetails.NewValue
security_result.about.labels.value
For all other PropertyName values (except those handled by specific conditions), the NewValue is used as the value of a label within the security_result.about.labels array.
EventDetails.NewValue
target.file.full_path
If PropertyName is Source file, the NewValue is used as the full path for the target file.
EventDetails.NewValue
target.resource.attribute.labels.value
If PropertyName contains (client), the NewValue is used as the value of a label in target.resource.attribute.labels.
EventDetails.NewValue
target.user.user_display_name
If PropertyName is Name of presenter, the NewValue is parsed. If it's an integer, it's discarded. Otherwise, it's used as the user display name for the target.
EventDetails.NewValue
target.user.userid
If PropertyName is ID of presenter, the NewValue is used as the user ID for the target.
EventDetails.PropertyName
principal.resource.attribute.labels.key
If PropertyName contains (server), the PropertyName is used as the key of a label in principal.resource.attribute.labels.
EventDetails.PropertyName
security_result.about.labels.key
For all other PropertyName values (except those handled by specific conditions), the PropertyName is used as the key of a label within the security_result.about.labels array.
EventDetails.PropertyName
target.resource.attribute.labels.key
If PropertyName contains (client), the PropertyName is used as the key of a label in target.resource.attribute.labels.
EventName
metadata.product_event_type
The value of EventName from the raw log is directly mapped to this UDM field.
Timestamp
metadata.event_timestamp
The value of Timestamp from the raw log is parsed and used as the event timestamp in the metadata.
metadata.event_type
Set to USER_UNCATEGORIZED if src_user (derived from ID of participant) is not empty, otherwise set to USER_RESOURCE_ACCESS.
metadata.vendor_name
Hardcoded to TEAMVIEWER.
metadata.product_name
Hardcoded to TEAMVIEWER.
network.application_protocol
Hardcoded to TEAMVIEWER.
Need more help?
Get answers from Community members and Google SecOps professionals.
