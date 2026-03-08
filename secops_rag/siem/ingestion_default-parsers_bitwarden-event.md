# Collect Bitwarden Enterprise Event Logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitwarden-event/  
**Scraped:** 2026-03-05T09:20:30.815370Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Bitwarden Enterprise Event Logs
Supported in:
Google secops
SIEM
This document explains how to ingest Bitwarden Enterprise Event Logs to Google Security Operations using Google Cloud Storage. The parser transforms raw JSON formatted event logs into a structured format conforming to the SecOps UDM. It extracts relevant fields like user details, IP addresses, and event types, mapping them to corresponding UDM fields for consistent security analysis.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to Bitwarden tenant
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Get Bitwarden API key and URL
In the
Bitwarden Admin Console
, go to
Settings
>
Organization info
>
View API key
.
Copy and save the following details to a secure location:
Client ID
Client Secret
Determine your Bitwarden endpoints (based on region):
IDENTITY_URL
=
https://identity.bitwarden.com/connect/token
(EU:
https://identity.bitwarden.eu/connect/token
)
API_BASE
=
https://api.bitwarden.com
(EU:
https://api.bitwarden.eu
)
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
bitwarden-events
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
Collect Bitwarden API prerequisites
You have already collected the Bitwarden API credentials in the previous step:
Client ID
: Organization client ID from Bitwarden Admin Console
Client Secret
: Organization client secret from Bitwarden Admin Console
IDENTITY_URL
:
https://identity.bitwarden.com/connect/token
(or EU endpoint)
API_BASE
:
https://api.bitwarden.com
(or EU endpoint)
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
bitwarden-events-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Bitwarden Enterprise Event logs
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
bitwarden-events-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
bitwarden-events-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Bitwarden Events API and writes them to GCS.
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
bitwarden-events-collector
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
bitwarden-events-trigger
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
bitwarden-events-collector-sa
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
bitwarden-events
GCS_PREFIX
bitwarden/events
STATE_KEY
bitwarden/events/state.json
BW_CLIENT_ID
organization.your-client-id
BW_CLIENT_SECRET
your-client-secret
IDENTITY_URL
https://identity.bitwarden.com/connect/token
API_BASE
https://api.bitwarden.com
MAX_PAGES
10
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
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch events from Bitwarden API and write to GCS.
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
'bitwarden/events'
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
,
'bitwarden/events/state.json'
)
# Bitwarden API credentials
identity_url
=
os
.
environ
.
get
(
'IDENTITY_URL'
,
'https://identity.bitwarden.com/connect/token'
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
'https://api.bitwarden.com'
)
.
rstrip
(
'/'
)
client_id
=
os
.
environ
.
get
(
'BW_CLIENT_ID'
)
client_secret
=
os
.
environ
.
get
(
'BW_CLIENT_SECRET'
)
max_pages
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
'10'
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
# Load state (continuation token)
state
=
load_state
(
bucket
,
state_key
)
continuation_token
=
state
.
get
(
'continuationToken'
)
print
(
f
'Processing events with continuation token:
{
continuation_token
}
'
)
# Get OAuth token
access_token
=
get_oauth_token
(
identity_url
,
client_id
,
client_secret
)
# Fetch events from Bitwarden API
run_timestamp
=
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
pages
=
0
total_events
=
0
written_files
=
[]
while
pages
<
max_pages
:
events_data
=
fetch_events
(
api_base
,
access_token
,
continuation_token
)
# Extract events array from API response
events
=
events_data
.
get
(
'data'
,
[])
# Only write file if there are events
if
events
:
gcs_key
=
write_events_jsonl
(
bucket
,
events
,
prefix
,
run_timestamp
,
pages
)
if
gcs_key
:
written_files
.
append
(
gcs_key
)
total_events
+=
len
(
events
)
pages
+=
1
# Check for next page token
next_token
=
events_data
.
get
(
'continuationToken'
)
if
next_token
:
continuation_token
=
next_token
continue
else
:
# No more pages
break
# Save state only if there are more pages to continue in next run
# If we hit MAX_PAGES and there's still a continuation token, save it
# Otherwise, clear the state (set to None)
save_state
(
bucket
,
state_key
,
{
'continuationToken'
:
continuation_token
if
pages
>
=
max_pages
and
continuation_token
else
None
})
print
(
f
'Successfully processed
{
total_events
}
events across
{
pages
}
pages'
)
print
(
f
'Files written:
{
len
(
written_files
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
'Error processing events:
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
get_oauth_token
(
identity_url
,
client_id
,
client_secret
):
"""Get OAuth 2.0 access token from Bitwarden."""
body_data
=
{
'grant_type'
:
'client_credentials'
,
'scope'
:
'api.organization'
,
'client_id'
:
client_id
,
'client_secret'
:
client_secret
}
encoded_data
=
'&'
.
join
([
f
'
{
k
}
=
{
v
}
'
for
k
,
v
in
body_data
.
items
()])
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
identity_url
,
body
=
encoded_data
,
headers
=
{
'Content-Type'
:
'application/x-www-form-urlencoded'
}
)
if
response
.
status
!=
200
:
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
api_base
,
access_token
,
continuation_token
=
None
):
"""Fetch events from Bitwarden API with pagination."""
url
=
f
'
{
api_base
}
/public/events'
if
continuation_token
:
url
+=
f
'?continuationToken=
{
continuation_token
}
'
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
access_token
}
'
,
'Accept'
:
'application/json'
}
)
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
'60'
))
print
(
f
'Rate limited (429). Retrying after
{
retry_after
}
s...'
)
import
time
time
.
sleep
(
retry_after
)
return
fetch_events
(
api_base
,
access_token
,
continuation_token
)
if
response
.
status
!=
200
:
raise
Exception
(
f
'Failed to fetch events:
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
write_events_jsonl
(
bucket
,
events
,
prefix
,
run_timestamp
,
page_index
):
"""
Write events in JSONL format (one JSON object per line).
Only writes if there are events to write.
Returns the GCS key of the written file.
"""
if
not
events
:
return
None
# Build JSONL content: one event per line
lines
=
[
json
.
dumps
(
event
,
separators
=
(
','
,
':'
))
for
event
in
events
]
jsonl_content
=
'
\n
'
.
join
(
lines
)
+
'
\n
'
# JSONL format with trailing newline
# Generate unique filename with page number to avoid conflicts
timestamp_str
=
datetime
.
fromtimestamp
(
run_timestamp
,
tz
=
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
key
=
f
'
{
prefix
}
/
{
timestamp_str
}
-page
{
page_index
:
05d
}
-bitwarden-events.jsonl'
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
print
(
f
'Wrote
{
len
(
events
)
}
events to
{
key
}
'
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
bitwarden-events-hourly
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
bitwarden-events-trigger
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
bitwarden-events-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for:
Proc
essing
events
with
continuation
token
:
None
Page
1
:
Retrieved
X
events
Wrote
X
events
to
bitwarden
/
events
/
YYYY
/
MM
/
DD
/
HHMMSS
-
page00000
-
bitwarden
-
events.jsonl
Successfully
processed
X
events
across
1
pages
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
bitwarden/events/
).
Verify that a new
.jsonl
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables
HTTP 403
: Verify account has required permissions and Events feature is enabled in Organization Settings
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
Bitwarden Events
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Bitwarden events
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
Configure a feed in Google SecOps to ingest Bitwarden Enterprise Event Logs
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
Bitwarden Events
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Bitwarden events
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://bitwarden-events/bitwarden/events/
Replace:
bitwarden-events
: Your GCS bucket name.
bitwarden/events/
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
Log Field
UDM Mapping
Logic
actingUserId
target.user.userid
If enriched.actingUser.userId is empty or null, this field is used to populate the target.user.userid field.
collectionID
security_result.detection_fields.key
Populates the key field within detection_fields in security_result.
collectionID
security_result.detection_fields.value
Populates the value field within detection_fields in security_result.
date
metadata.event_timestamp
Parsed and converted to a timestamp format and mapped to event_timestamp.
enriched.actingUser.accessAll
security_result.rule_labels.key
Sets the value to "Access_All" within rule_labels in security_result.
enriched.actingUser.accessAll
security_result.rule_labels.value
Populates the value field within rule_labels in security_result with the value from enriched.actingUser.accessAll converted to string.
enriched.actingUser.email
target.user.email_addresses
Populates the email_addresses field within target.user.
enriched.actingUser.id
metadata.product_log_id
Populates the product_log_id field within metadata.
enriched.actingUser.id
target.labels.key
Sets the value to "ID" within target.labels.
enriched.actingUser.id
target.labels.value
Populates the value field within target.labels with the value from enriched.actingUser.id.
enriched.actingUser.name
target.user.user_display_name
Populates the user_display_name field within target.user.
enriched.actingUser.object
target.labels.key
Sets the value to "Object" within target.labels.
enriched.actingUser.object
target.labels.value
Populates the value field within target.labels with the value from enriched.actingUser.object.
enriched.actingUser.resetPasswordEnrolled
target.labels.key
Sets the value to "ResetPasswordEnrolled" within target.labels.
enriched.actingUser.resetPasswordEnrolled
target.labels.value
Populates the value field within target.labels with the value from enriched.actingUser.resetPasswordEnrolled converted to string.
enriched.actingUser.twoFactorEnabled
security_result.rule_labels.key
Sets the value to "Two Factor Enabled" within rule_labels in security_result.
enriched.actingUser.twoFactorEnabled
security_result.rule_labels.value
Populates the value field within rule_labels in security_result with the value from enriched.actingUser.twoFactorEnabled converted to string.
enriched.actingUser.userId
target.user.userid
Populates the userid field within target.user.
enriched.collection.id
additional.fields.key
Sets the value to "Collection ID" within additional.fields.
enriched.collection.id
additional.fields.value.string_value
Populates the string_value field within additional.fields with the value from enriched.collection.id.
enriched.collection.object
additional.fields.key
Sets the value to "Collection Object" within additional.fields.
enriched.collection.object
additional.fields.value.string_value
Populates the string_value field within additional.fields with the value from enriched.collection.object.
enriched.type
metadata.product_event_type
Populates the product_event_type field within metadata.
groupId
target.user.group_identifiers
Adds the value to the group_identifiers array within target.user.
ipAddress
principal.ip
Extracted IP address from the field and mapped to principal.ip.
N/A
extensions.auth
An empty object is created by the parser.
N/A
metadata.event_type
Determined based on the enriched.type and presence of principal and target information. Possible values: USER_LOGIN, STATUS_UPDATE, GENERIC_EVENT.
N/A
security_result.action
Determined based on the enriched.type. Possible values: ALLOW, BLOCK.
object
additional.fields.key
Sets the value to "Object" within additional.fields.
object
additional.fields.value
Populates the value field within additional.fields with the value from object.
Need more help?
Get answers from Community members and Google SecOps professionals.
