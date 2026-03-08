# Collect Zoom operation logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zoom-operation-logs/  
**Scraped:** 2026-03-05T09:30:29.027796Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zoom operation logs
Supported in:
Google secops
SIEM
This document explains how to ingest Zoom operation logs to Google Security Operations using Google Cloud Storage. The parser transforms the raw logs into a unified data model (UDM). It extracts fields from the raw log message, performs data cleaning and normalization, and maps the extracted information to corresponding UDM fields, ultimately enriching the data for analysis and correlation within a SIEM system.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Zoom
Collect Zoom operation logs prerequisites
Sign in to
Zoom App Marketplace
.
Go to
Develop
>
Build App
>
Server-to-Server OAuth
.
Create the app and add the following scope:
report:read:operation_logs:admin
(or
report:read:admin
).
In
App Credentials
, copy and save the following details in a secure location:
Account ID
Client ID
Client Secret
Verify permissions
To verify the account has the required permissions:
Sign in to your Zoom account.
Go to
Admin
>
Account Management
>
Account Profile
.
If you can access the account settings and view operation logs, you have the required permissions.
If you cannot access these options, contact your Zoom administrator to grant the necessary permissions.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
ZOOM_ACCOUNT_ID
=
"<your-account-id>"
ZOOM_CLIENT_ID
=
"<your-client-id>"
ZOOM_CLIENT_SECRET
=
"<your-client-secret>"
# Get OAuth token
TOKEN
=
$(
curl
-s
-X
POST
"https://zoom.us/oauth/token?grant_type=account_credentials&account_id=
${
ZOOM_ACCOUNT_ID
}
"
\
-u
"
${
ZOOM_CLIENT_ID
}
:
${
ZOOM_CLIENT_SECRET
}
"
\
|
grep
-o
'"access_token":"[^"]*"'
|
cut
-d
'"'
-f4
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
\
"https://api.zoom.us/v2/report/operationlogs?from=
$(
date
-u
-d
'1 day ago'
+%Y-%m-%d
)
&
to=
$(
date
-u
+%Y-%m-%d
)
&
page_size=10"
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
zoom-operation-logs
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
zoom-operationlogs-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Zoom operation logs
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
zoom-operation-logs
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
zoom-operationlogs-sa@PROJECT_ID.iam.gserviceaccount.com
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
zoom-operationlogs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Zoom API and writes them to GCS.
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
zoom-operationlogs-to-gcs
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
zoom-operationlogs-trigger
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
: Select
zoom-operationlogs-sa
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
zoom-operation-logs
GCS_PREFIX
zoom/operationlogs/
STATE_KEY
zoom/operationlogs/state.json
ZOOM_ACCOUNT_ID
<your-zoom-account-id>
ZOOM_CLIENT_ID
<your-zoom-client-id>
ZOOM_CLIENT_SECRET
<your-zoom-client-secret>
PAGE_SIZE
300
TIMEOUT
30
In the
Variables & Secrets
section, scroll to
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
date
,
timedelta
,
timezone
import
base64
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
'zoom/operationlogs/'
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
'zoom/operationlogs/state.json'
)
ZOOM_ACCOUNT_ID
=
os
.
environ
.
get
(
'ZOOM_ACCOUNT_ID'
)
ZOOM_CLIENT_ID
=
os
.
environ
.
get
(
'ZOOM_CLIENT_ID'
)
ZOOM_CLIENT_SECRET
=
os
.
environ
.
get
(
'ZOOM_CLIENT_SECRET'
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
'PAGE_SIZE'
,
'300'
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
TOKEN_URL
=
"https://zoom.us/oauth/token"
REPORT_URL
=
"https://api.zoom.us/v2/report/operationlogs"
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Zoom operation logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
ZOOM_ACCOUNT_ID
,
ZOOM_CLIENT_ID
,
ZOOM_CLIENT_SECRET
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
GCS_BUCKET
)
# Get OAuth token
token
=
get_token
()
# Load state
state
=
load_state
(
bucket
,
STATE_KEY
)
cursor_date
=
state
.
get
(
'cursor_date'
,
date
.
today
()
.
isoformat
())
print
(
f
'Processing logs for date:
{
cursor_date
}
'
)
# Fetch logs
from_date
=
cursor_date
to_date
=
cursor_date
total_written
=
0
next_token
=
state
.
get
(
'next_page_token'
)
while
True
:
page
=
fetch_page
(
token
,
from_date
,
to_date
,
next_token
)
items
=
page
.
get
(
'operation_logs'
,
[])
or
[]
if
items
:
write_chunk
(
bucket
,
items
,
datetime
.
now
(
timezone
.
utc
))
total_written
+=
len
(
items
)
next_token
=
page
.
get
(
'next_page_token'
)
if
not
next_token
:
break
# Advance to next day if we've finished this date
today
=
date
.
today
()
.
isoformat
()
if
cursor_date
<
today
:
nxt
=
(
datetime
.
fromisoformat
(
cursor_date
)
+
timedelta
(
days
=
1
))
.
date
()
.
isoformat
()
state
[
'cursor_date'
]
=
nxt
state
[
'next_page_token'
]
=
None
else
:
# stay on today; continue later with next_page_token=None
state
[
'next_page_token'
]
=
None
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
total_written
}
logs for
{
from_date
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
def
get_token
():
"""Get OAuth 2.0 access token from Zoom."""
params
=
f
"grant_type=account_credentials&account_id=
{
ZOOM_ACCOUNT_ID
}
"
basic
=
base64
.
b64encode
(
f
"
{
ZOOM_CLIENT_ID
}
:
{
ZOOM_CLIENT_SECRET
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
headers
=
{
'Authorization'
:
f
'Basic
{
basic
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
,
'Host'
:
'zoom.us'
}
response
=
http
.
request
(
'POST'
,
TOKEN_URL
,
body
=
params
,
headers
=
headers
,
timeout
=
TIMEOUT
)
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
'Token request failed:
{
response
.
status
}
'
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
'Response body:
{
response_text
}
'
)
raise
Exception
(
f
'Failed to get OAuth token:
{
response
.
status
}
'
)
body
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
body
[
'access_token'
]
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
# Initial state: start today
today
=
date
.
today
()
.
isoformat
()
return
{
'cursor_date'
:
today
,
'next_page_token'
:
None
}
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
write_chunk
(
bucket
,
items
,
ts
):
"""Write log chunk to GCS."""
key
=
f
"
{
GCS_PREFIX
}{
ts
:
%Y/%m/%d
}
/zoom-operationlogs-
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
rec
in
items
:
gz
.
write
((
json
.
dumps
(
rec
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
))
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
key
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
'Wrote
{
len
(
items
)
}
logs to
{
key
}
'
)
return
key
def
fetch_page
(
token
,
from_date
,
to_date
,
next_page_token
):
"""Fetch a page of logs from Zoom API."""
params
=
{
'from'
:
from_date
,
'to'
:
to_date
,
'page_size'
:
str
(
PAGE_SIZE
)
}
if
next_page_token
:
params
[
'next_page_token'
]
=
next_page_token
# Build query string
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
url
=
f
"
{
REPORT_URL
}
?
{
query_string
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
token
}
'
,
'Accept'
:
'application/json'
}
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
'API request failed:
{
response
.
status
}
'
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
'Response body:
{
response_text
}
'
)
raise
Exception
(
f
'Failed to fetch logs:
{
response
.
status
}
'
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
zoom-operationlogs-schedule-15min
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
Select
zoom-operationlogs-trigger
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
Low volume
Every 6 hours
0 */6 * * *
Batch processing
Test the integration
In the
Cloud Scheduler
console, find your job (for example,
zoom-operationlogs-schedule-15min
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
Click the function name (
zoom-operationlogs-to-gcs
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Proc
essing
logs
for
date
:
YYYY
-
MM
-
DD
Page
1
:
Retrieved
X
events
Wrote
X
records
to
zoom
/
operationlogs
/
YYYY
/
MM
/
DD
/
zoom
-
operationlogs
-
UUID.json.gz
Successfully
processed
X
logs
for
YYYY
-
MM
-
DD
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
zoom-operation-logs
).
Navigate to the prefix folder (
zoom/operationlogs/
).
Verify that a new
.json.gz
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check Zoom API credentials in environment variables
HTTP 403
: Verify Zoom app has
report:read:operation_logs:admin
scope
Missing environment variables
: Check all required variables are set in Cloud Run function configuration
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
Zoom Operation Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Zoom Operation Logs
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
zoom-operation-logs
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
Configure a feed in Google SecOps to ingest Zoom operation logs
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
Zoom Operation Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Zoom Operation Logs
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://zoom-operation-logs/zoom/operationlogs/
Replace:
zoom-operation-logs
: Your GCS bucket name.
zoom/operationlogs/
: Prefix path where logs are stored.
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
action
metadata.product_event_type
The raw log field "action" is mapped to this UDM field.
category_type
additional.fields.key
The raw log field "category_type" is mapped to this UDM field.
category_type
additional.fields.value.string_value
The raw log field "category_type" is mapped to this UDM field.
Department
target.user.department
The raw log field "Department" (extracted from "operation_detail" field) is mapped to this UDM field.
Description
target.user.role_description
The raw log field "Description" (extracted from "operation_detail" field) is mapped to this UDM field.
Display Name
target.user.user_display_name
The raw log field "Display Name" (extracted from "operation_detail" field) is mapped to this UDM field.
Email Address
target.user.email_addresses
The raw log field "Email Address" (extracted from "operation_detail" field) is mapped to this UDM field.
First Name
target.user.first_name
The raw log field "First Name" (extracted from "operation_detail" field) is mapped to this UDM field.
Job Title
target.user.title
The raw log field "Job Title" (extracted from "operation_detail" field) is mapped to this UDM field.
Last Name
target.user.last_name
The raw log field "Last Name" (extracted from "operation_detail" field) is mapped to this UDM field.
Location
target.location.name
The raw log field "Location" (extracted from "operation_detail" field) is mapped to this UDM field.
operation_detail
metadata.description
The raw log field "operation_detail" is mapped to this UDM field.
operator
principal.user.email_addresses
The raw log field "operator" is mapped to this UDM field if it matches an email regex.
operator
principal.user.userid
The raw log field "operator" is mapped to this UDM field if it doesn't match an email regex.
Room Name
target.user.attribute.labels.value
The raw log field "Room Name" (extracted from "operation_detail" field) is mapped to this UDM field.
Role Name
target.user.attribute.roles.name
The raw log field "Role Name" (extracted from "operation_detail" field) is mapped to this UDM field.
time
metadata.event_timestamp.seconds
The raw log field "time" is parsed and mapped to this UDM field.
Type
target.user.attribute.labels.value
The raw log field "Type" (extracted from "operation_detail" field) is mapped to this UDM field.
User Role
target.user.attribute.roles.name
The raw log field "User Role" (extracted from "operation_detail" field) is mapped to this UDM field.
User Type
target.user.attribute.labels.value
The raw log field "User Type" (extracted from "operation_detail" field) is mapped to this UDM field.
metadata.log_type
The value "ZOOM_OPERATION_LOGS" is assigned to this UDM field.
metadata.vendor_name
The value "ZOOM" is assigned to this UDM field.
metadata.product_name
The value "ZOOM_OPERATION_LOGS" is assigned to this UDM field.
metadata.event_type
The value is determined based on the following logic: 1. If "event_type" field is not empty, its value is used. 1. If "operator", "email", or "email2" fields are not empty, the value is set to "USER_UNCATEGORIZED". 1. Otherwise, the value is set to "GENERIC_EVENT".
json_data
about.user.attribute.labels.value
The raw log field "json_data" (extracted from "operation_detail" field) is parsed as JSON. The "assistant" and "options" fields from each element of the parsed JSON array are mapped to the "value" field of the "labels" array in the UDM.
json_data
about.user.userid
The raw log field "json_data" (extracted from "operation_detail" field) is parsed as JSON. The "userId" field from each element of the parsed JSON array (except the first one) is mapped to the "userid" field of the "about.user" object in the UDM.
json_data
target.user.attribute.labels.value
The raw log field "json_data" (extracted from "operation_detail" field) is parsed as JSON. The "assistant" and "options" fields from the first element of the parsed JSON array are mapped to the "value" field of the "labels" array in the UDM.
json_data
target.user.userid
The raw log field "json_data" (extracted from "operation_detail" field) is parsed as JSON. The "userId" field from the first element of the parsed JSON array is mapped to the "userid" field of the "target.user" object in the UDM.
email
target.user.email_addresses
The raw log field "email" (extracted from "operation_detail" field) is mapped to this UDM field.
email2
target.user.email_addresses
The raw log field "email2" (extracted from "operation_detail" field) is mapped to this UDM field.
role
target.user.attribute.roles.name
The raw log field "role" (extracted from "operation_detail" field) is mapped to this UDM field.
Need more help?
Get answers from Community members and Google SecOps professionals.
