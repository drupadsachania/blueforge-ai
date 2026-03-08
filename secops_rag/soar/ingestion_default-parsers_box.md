# Collect Box JSON logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/box/  
**Scraped:** 2026-03-05T09:51:33.599229Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Box JSON logs
Supported in:
Google secops
SIEM
This document explains how to ingest Box JSON logs to Google Security Operations using Google Cloud Storage. The parser processes Box event logs in JSON format, mapping them to a unified data model (UDM). It extracts relevant fields from the raw logs, performs data transformations like renaming and merging, and enriches the data with intermediary information before outputting the structured event data.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Box (Admin + Developer Console)
Configure Box Developer Console (Client Credentials)
Sign in to
Box Developer Console
.
Create a
Custom App
with
Server Authentication (Client Credentials Grant)
.
Set
Application Access
=
App + Enterprise Access
.
In
Application Scopes
, enable
Manage enterprise properties
.
In
Admin Console
>
Apps
>
Custom Apps Manager
, authorize the app by
Client ID
.
Copy and save the
Client ID
and
Client Secret
in a secure location.
Go to
Admin Console
>
Account & Billing
>
Account Information
.
Copy and save the
Enterprise ID
in a secure location.
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
box-collaboration-logs
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
box-collaboration-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Box Collaboration logs
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
: Enter the service account email (
box-collaboration-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
box-collaboration-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Box API and writes them to GCS.
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
box-collaboration-collector
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
box-collaboration-trigger
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
box-collaboration-collector-sa
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
box-collaboration-logs
GCS_PREFIX
box/collaboration/
STATE_KEY
box/collaboration/state.json
BOX_CLIENT_ID
Enter Box Client ID
BOX_CLIENT_SECRET
Enter Box Client Secret
BOX_ENTERPRISE_ID
Enter Box Enterprise ID
STREAM_TYPE
admin_logs_streaming
LIMIT
500
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
import
base64
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
TOKEN_URL
=
"https://api.box.com/oauth2/token"
EVENTS_URL
=
"https://api.box.com/2.0/events"
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Box enterprise events and write to GCS.
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
'box/collaboration/'
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
'box/collaboration/state.json'
)
client_id
=
os
.
environ
.
get
(
'BOX_CLIENT_ID'
)
client_secret
=
os
.
environ
.
get
(
'BOX_CLIENT_SECRET'
)
enterprise_id
=
os
.
environ
.
get
(
'BOX_ENTERPRISE_ID'
)
stream_type
=
os
.
environ
.
get
(
'STREAM_TYPE'
,
'admin_logs_streaming'
)
limit
=
int
(
os
.
environ
.
get
(
'LIMIT'
,
'500'
))
if
not
all
([
bucket_name
,
client_id
,
client_secret
,
enterprise_id
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
# Get OAuth token
token
=
get_token
(
client_id
,
client_secret
,
enterprise_id
)
# Load state (stream position)
state
=
load_state
(
bucket
,
state_key
)
stream_position
=
state
.
get
(
'stream_position'
)
print
(
f
'Processing events from stream position:
{
stream_position
}
'
)
total_events
=
0
idx
=
0
while
True
:
# Fetch events page
page
=
fetch_events
(
token
,
stream_type
,
limit
,
stream_position
)
entries
=
page
.
get
(
'entries'
)
or
[]
if
not
entries
:
next_pos
=
page
.
get
(
'next_stream_position'
)
or
stream_position
if
next_pos
and
next_pos
!=
stream_position
:
save_state
(
bucket
,
state_key
,
{
'stream_position'
:
next_pos
})
break
# Write page to GCS
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
/%H%M%S'
)
blob_name
=
f
"
{
prefix
}{
timestamp
}
-box-events-
{
idx
:
03d
}
.json"
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
json
.
dumps
(
page
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
idx
+=
1
total_events
+=
len
(
entries
)
stream_position
=
page
.
get
(
'next_stream_position'
)
or
stream_position
# Save state after each page
if
stream_position
:
save_state
(
bucket
,
state_key
,
{
'stream_position'
:
stream_position
})
# Break if fewer entries than limit (last page)
if
len
(
entries
)
<
limit
:
break
print
(
f
'Successfully processed
{
total_events
}
events, final position:
{
stream_position
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
'Error processing Box events:
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
(
client_id
,
client_secret
,
enterprise_id
):
"""Get OAuth 2.0 access token using client credentials grant."""
fields
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
'box_subject_type'
:
'enterprise'
,
'box_subject_id'
:
enterprise_id
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
fields
=
fields
,
headers
=
{
'Content-Type'
:
'application/x-www-form-urlencoded'
}
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
fetch_events
(
token
,
stream_type
,
limit
,
stream_position
=
None
,
timeout
=
60
,
max_retries
=
5
):
"""Fetch events from Box API with retry logic."""
params
=
{
'stream_type'
:
stream_type
,
'limit'
:
str
(
limit
),
'stream_position'
:
stream_position
or
'now'
}
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
EVENTS_URL
}
?
{
query_string
}
"
attempt
=
0
backoff
=
1.0
while
True
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
{
'Authorization'
:
f
'Bearer
{
token
}
'
},
timeout
=
timeout
)
if
response
.
status
==
200
:
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
elif
response
.
status
==
429
and
attempt
<
max_retries
:
# Rate limited - retry with backoff
retry_after
=
response
.
headers
.
get
(
'Retry-After'
)
delay
=
int
(
retry_after
)
if
retry_after
and
retry_after
.
isdigit
()
else
int
(
backoff
)
print
(
f
'Rate limited, retrying after
{
delay
}
seconds'
)
import
time
time
.
sleep
(
max
(
1
,
delay
))
attempt
+=
1
backoff
*=
2
continue
elif
500
<
=
response
.
status
<
=
599
and
attempt
<
max_retries
:
# Server error - retry with backoff
print
(
f
'Server error
{
response
.
status
}
, retrying after
{
backoff
}
seconds'
)
import
time
time
.
sleep
(
backoff
)
attempt
+=
1
backoff
*=
2
continue
else
:
raise
Exception
(
f
'Box API error:
{
response
.
status
}
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
if
attempt
<
max_retries
:
print
(
f
'Request error:
{
str
(
e
)
}
, retrying after
{
backoff
}
seconds'
)
import
time
time
.
sleep
(
backoff
)
attempt
+=
1
backoff
*=
2
continue
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
box-collaboration-schedule-15min
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
Select the Pub/Sub topic (
box-collaboration-trigger
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
Medium volume (recommended)
Every hour
0 * * * *
Standard
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
0 0 * * *
Historical data collection
Test the integration
In the
Cloud Scheduler
console, find your job.
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click on your function name (
box-collaboration-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Proc
essing
events
from
stream
position
:
...
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
gs
:
//
box
-
collaboration
-
logs
/
box
/
collaboration
/
...
Successfully
processed
X
events
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
box/collaboration/
).
Verify that a new
.json
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check Box API credentials in environment variables
HTTP 403
: Verify Box app has required permissions and is authorized in Admin Console
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set
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
Box Collaboration
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Box
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
Configure a feed in Google SecOps to ingest Box logs
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
Box Collaboration
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Box
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://box-collaboration-logs/box/collaboration/
Replace:
box-collaboration-logs
: Your GCS bucket name.
box/collaboration/
: Prefix/folder path where logs are stored.
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/box-logs/
With subfolder:
gs://company-logs/box/collaboration/
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
additional_details.ekm_id
additional.fields
Value taken from additional_details.ekm_id
additional_details.service_id
additional.fields
Value taken from additional_details.service_id
additional_details.service_name
additional.fields
Value taken from additional_details.service_name
additional_details.shared_link_id
additional.fields
Value taken from additional_details.shared_link_id
additional_details.size
target.file.size
Value taken from additional_details.size
additional_details.version_id
additional.fields
Value taken from additional_details.version_id
created_at
metadata.event_timestamp
Value taken from created_at
created_by.id
principal.user.userid
Value taken from created_by.id
created_by.login
principal.user.email_addresses
Value taken from created_by.login
created_by.name
principal.user.user_display_name
Value taken from created_by.name
event_id
metadata.product_log_id
Value taken from event_id
event_type
metadata.product_event_type
Value taken from event_type
ip_address
principal.ip
Value taken from ip_address
source.item_id
target.file.product_object_id
Value taken from source.item_id
source.item_name
target.file.full_path
Value taken from source.item_name
source.item_type
Not mapped
source.login
target.user.email_addresses
Value taken from source.login
source.name
target.user.user_display_name
Value taken from source.name
source.owned_by.id
target.user.userid
Value taken from source.owned_by.id
source.owned_by.login
target.user.email_addresses
Value taken from source.owned_by.login
source.owned_by.name
target.user.user_display_name
Value taken from source.owned_by.name
source.parent.id
Not mapped
source.parent.name
Not mapped
source.parent.type
Not mapped
source.type
Not mapped
type
metadata.log_type
Value taken from type
metadata.vendor_name
Hardcoded value
metadata.product_name
Hardcoded value
security_result.action
Derived from event_type. If event_type is FAILED_LOGIN then BLOCK, if event_type is USER_LOGIN then ALLOW, otherwise UNSPECIFIED.
extensions.auth.type
Derived from event_type. If event_type is USER_LOGIN or ADMIN_LOGIN then MACHINE, otherwise UNSPECIFIED.
extensions.auth.mechanism
Derived from event_type. If event_type is USER_LOGIN or ADMIN_LOGIN then USERNAME_PASSWORD, otherwise UNSPECIFIED.
Need more help?
Get answers from Community members and Google SecOps professionals.
