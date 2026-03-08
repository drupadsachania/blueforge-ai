# Collect Delinea Single Sign-On (SSO) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centrify-sso/  
**Scraped:** 2026-03-05T09:54:21.707438Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Delinea Single Sign-On (SSO) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Delinea (formerly Centrify) Single Sign-On (SSO) logs to Google Security Operations using Google Cloud Storage. The parser extracts the logs, handling both JSON and syslog formats. It parses key-value pairs, timestamps, and other relevant fields, mapping them to the UDM model, with specific logic for handling login failures, user agents, severity levels, authentication mechanisms, and various event types. It prioritizes FailUserName over NormalizedUser for target email addresses in failure events.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Delinea (Centrify) SSO tenant
Collect Delinea (Centrify) SSO credentials
Create OAuth2 client application
Sign in to the
Delinea Admin Portal
.
Go to
Apps
>
Add Web Apps
.
Click the
Custom
tab.
Search for
OAuth2 Client
and click
Add
.
Click
Yes
in the
Add Web App
dialog.
Click
Close
in the
Add Web Apps
dialog.
On the
Application Configuration
page, configure the following:
Settings
tab:
Application ID
: Enter a unique identifier (for example,
secops-oauth-client
).
Application Name
: Enter a descriptive name (for example,
SecOps Data Export
).
Application Description
: Enter description (for example,
OAuth client for exporting audit events to SecOps
).
General Usage
section:
Client ID Type
: Select
Confidential
.
Issued Client ID
: Copy and save this value.
Issued Client Secret
: Copy and save this value.
Tokens
tab:
Auth Methods
: Select
Client Creds
.
Token Type
: Select
JwtRS256
.
Scope
tab:
Add scope
redrock/query
with the description
Query API Access
.
Click
Save
to create the OAuth client.
Copy and save in a secure location the following details:
Tenant URL
: Your Centrify tenant URL (for example,
https://yourtenant.my.centrify.com
).
Client ID
: From step 7.
Client Secret
: From step 7.
OAuth Application ID
: From the Application Configuration.
Verify permissions
To verify the OAuth client has the required permissions:
Sign in to the
Delinea Admin Portal
.
Go to
Settings
(⚙️)
>
Resources
>
Roles
.
Verify that the role assigned to the OAuth client includes
Report: Audit Events: View
permission.
If the permission is missing, contact your Delinea administrator to grant the required permission.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
TENANT_URL
=
"https://yourtenant.my.centrify.com"
CLIENT_ID
=
"your-client-id"
CLIENT_SECRET
=
"your-client-secret"
OAUTH_APP_ID
=
"your-oauth-application-id"
# Get OAuth token
TOKEN
=
$(
curl
-s
-X
POST
"
${
TENANT_URL
}
/oauth2/token/
${
OAUTH_APP_ID
}
"
\
-H
"Authorization: Basic
$(
echo
-n
"
${
CLIENT_ID
}
:
${
CLIENT_SECRET
}
"
|
base64
)
"
\
-H
"X-CENTRIFY-NATIVE-CLIENT: True"
\
-H
"Content-Type: application/x-www-form-urlencoded"
\
-d
"grant_type=client_credentials&scope=redrock/query"
|
jq
-r
'.access_token'
)
# Test query API access
curl
-v
-X
POST
"
${
TENANT_URL
}
/Redrock/query"
\
-H
"Authorization: Bearer
${
TOKEN
}
"
\
-H
"X-CENTRIFY-NATIVE-CLIENT: True"
\
-H
"Content-Type: application/json"
\
-d
'{"Script":"Select * from Event where WhenOccurred > datefunc('
"'"
'now'
"'"
', '
"'"
'-1'
"'"
') ORDER BY WhenOccurred ASC","args":{"PageNumber":1,"PageSize":10,"Limit":10,"Caching":-1}}'
If successful, you should see a JSON response with audit events. If you receive a 401 or 403 error, verify your credentials and permissions.
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
delinea-centrify-logs-bucket
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
delinea-sso-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Delinea SSO logs
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
delinea-centrify-logs-bucket
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
delinea-sso-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
delinea-sso-logs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Delinea SSO API and writes them to GCS.
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
delinea-sso-log-export
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
, choose the Pub/Sub topic
delinea-sso-logs-trigger
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
delinea-sso-collector-sa
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
Description
GCS_BUCKET
delinea-centrify-logs-bucket
GCS bucket name
GCS_PREFIX
centrify-sso-logs
Prefix for log files
STATE_KEY
centrify-sso-logs/state.json
State file path
TENANT_URL
https://yourtenant.my.centrify.com
Delinea tenant URL
CLIENT_ID
your-client-id
OAuth client ID
CLIENT_SECRET
your-client-secret
OAuth client secret
OAUTH_APP_ID
your-oauth-application-id
OAuth application ID
PAGE_SIZE
1000
Records per page
MAX_PAGES
10
Maximum pages to fetch
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
Cloud Run function triggered by Pub/Sub to fetch Delinea Centrify SSO audit events and write to GCS.
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
'centrify-sso-logs'
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
'centrify-sso-logs/state.json'
)
# Centrify API credentials
tenant_url
=
os
.
environ
.
get
(
'TENANT_URL'
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
oauth_app_id
=
os
.
environ
.
get
(
'OAUTH_APP_ID'
)
# Optional parameters
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
tenant_url
,
client_id
,
client_secret
,
oauth_app_id
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
)
print
(
f
'Processing logs since
{
last_timestamp
if
last_timestamp
else
"24 hours ago"
}
'
)
# Get OAuth access token
access_token
=
get_oauth_token
(
tenant_url
,
client_id
,
client_secret
,
oauth_app_id
)
# Fetch audit events
events
=
fetch_audit_events
(
tenant_url
,
access_token
,
last_timestamp
,
page_size
,
max_pages
)
if
events
:
# Write events to GCS
current_timestamp
=
datetime
.
now
(
timezone
.
utc
)
blob_name
=
f
"
{
prefix
}
/centrify-sso-events-
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
blob
=
bucket
.
blob
(
blob_name
)
# Convert to JSONL format (one JSON object per line)
jsonl_content
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
])
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
blob_name
}
'
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
current_timestamp
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
events'
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
'Error processing Centrify SSO logs:
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
tenant_url
,
client_id
,
client_secret
,
oauth_app_id
):
"""Get OAuth access token using client credentials flow."""
credentials
=
f
"
{
client_id
}
:
{
client_secret
}
"
basic_auth
=
base64
.
b64encode
(
credentials
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
token_url
=
f
"
{
tenant_url
}
/oauth2/token/
{
oauth_app_id
}
"
headers
=
{
'Authorization'
:
f
'Basic
{
basic_auth
}
'
,
'X-CENTRIFY-NATIVE-CLIENT'
:
'True'
,
'Content-Type'
:
'application/x-www-form-urlencoded'
}
data
=
{
'grant_type'
:
'client_credentials'
,
'scope'
:
'redrock/query'
}
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
fields
=
data
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
"OAuth token request failed:
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
'utf-8'
)
}
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
tenant_url
,
access_token
,
last_timestamp
,
page_size
,
max_pages
):
"""Fetch audit events from Centrify using the Redrock/query API with proper pagination."""
query_url
=
f
"
{
tenant_url
}
/Redrock/query"
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
'X-CENTRIFY-NATIVE-CLIENT'
:
'True'
,
'Content-Type'
:
'application/json'
}
# Build SQL query with timestamp filter
if
last_timestamp
:
sql_query
=
f
"Select * from Event where WhenOccurred > '
{
last_timestamp
}
' ORDER BY WhenOccurred ASC"
else
:
# First run - get events from last 24 hours
sql_query
=
"Select * from Event where WhenOccurred > datefunc('now', '-1') ORDER BY WhenOccurred ASC"
all_events
=
[]
page_num
=
1
backoff
=
1.0
while
page_num
<
=
max_pages
:
payload
=
{
"Script"
:
sql_query
,
"args"
:
{
"PageNumber"
:
page_num
,
"PageSize"
:
page_size
,
"Limit"
:
page_size
*
max_pages
,
"Caching"
:
-
1
}
}
try
:
response
=
http
.
request
(
'POST'
,
query_url
,
headers
=
headers
,
body
=
json
.
dumps
(
payload
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
raise
Exception
(
f
"API query failed:
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
'utf-8'
)
}
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
if
not
response_data
.
get
(
'success'
,
False
):
raise
Exception
(
f
"API query failed:
{
response_data
.
get
(
'Message'
,
'Unknown error'
)
}
"
)
# Parse the response
result
=
response_data
.
get
(
'Result'
,
{})
columns
=
{
col
[
'Name'
]:
i
for
i
,
col
in
enumerate
(
result
.
get
(
'Columns'
,
[]))}
raw_results
=
result
.
get
(
'Results'
,
[])
if
not
raw_results
:
print
(
f
"No more results on page
{
page_num
}
"
)
break
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
raw_results
)
}
events"
)
for
raw_event
in
raw_results
:
event
=
{}
row_data
=
raw_event
.
get
(
'Row'
,
{})
# Map column names to values
for
col_name
,
col_index
in
columns
.
items
():
if
col_name
in
row_data
and
row_data
[
col_name
]
is
not
None
:
event
[
col_name
]
=
row_data
[
col_name
]
# Add metadata
event
[
'_source'
]
=
'centrify_sso'
event
[
'_collected_at'
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
+
'Z'
all_events
.
append
(
event
)
# Check if we've reached the end
if
len
(
raw_results
)
<
page_size
:
print
(
f
"Reached last page (page
{
page_num
}
returned
{
len
(
raw_results
)
}
<
{
page_size
}
)"
)
break
page_num
+=
1
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
page_num
}
:
{
e
}
"
)
raise
print
(
f
"Retrieved
{
len
(
all_events
)
}
total events from
{
page_num
}
pages"
)
return
all_events
def
get_latest_event_timestamp
(
events
):
"""Get the latest timestamp from the events for state tracking."""
if
not
events
:
return
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
latest
=
None
for
event
in
events
:
when_occurred
=
event
.
get
(
'WhenOccurred'
)
if
when_occurred
:
if
latest
is
None
or
when_occurred
>
latest
:
latest
=
when_occurred
return
latest
or
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
delinea-sso-log-export-hourly
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
Select the Pub/Sub topic
delinea-sso-logs-trigger
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
console, find your job (for example,
delinea-sso-log-export-hourly
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
Click on the function name
delinea-sso-log-export
.
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Proc
essing
logs
since
YYYY
-
MM
-
DDTHH
:
MM
:
SS
+
00
:
00
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
centrify
-
sso
-
logs
/
centrify
-
sso
-
events_YYYYMMDD_HHMMSS.json
Successfully
processed
X
events
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (for example,
delinea-centrify-logs-bucket
).
Navigate to the prefix folder
centrify-sso-logs/
.
Verify that a new
.json
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables (CLIENT_ID, CLIENT_SECRET, OAUTH_APP_ID)
HTTP 403
: Verify the OAuth client has
Report: Audit Events: View
permission
HTTP 429
: Rate limiting - function will automatically retry with backoff
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
Delinea Centrify SSO logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Centrify
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
Click your bucket name (for example,
delinea-centrify-logs-bucket
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
Configure a feed in Google SecOps to ingest Delinea (Centrify) SSO logs
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
Delinea Centrify SSO logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Centrify
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://delinea-centrify-logs-bucket/centrify-sso-logs/
Replace:
delinea-centrify-logs-bucket
: Your GCS bucket name.
centrify-sso-logs
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/centrify-sso-logs/
With subfolder:
gs://company-logs/delinea/sso/
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
AccountID
security_result.detection_fields.value
The value of AccountID from the raw log is assigned to a security_result.detection_fields object with key: Account ID.
ApplicationName
target.application
The value of ApplicationName from the raw log is assigned to the target.application field.
AuthorityFQDN
target.asset.network_domain
The value of AuthorityFQDN from the raw log is assigned to the target.asset.network_domain field.
AuthorityID
target.asset.asset_id
The value of AuthorityID from the raw log is assigned to the target.asset.asset_id field, prefixed with "AuthorityID:".
AzDeploymentId
security_result.detection_fields.value
The value of AzDeploymentId from the raw log is assigned to a security_result.detection_fields object with key: AzDeploymentId.
AzRoleId
additional.fields.value.string_value
The value of AzRoleId from the raw log is assigned to an additional.fields object with key: AzRoleId.
AzRoleName
target.user.attribute.roles.name
The value of AzRoleName from the raw log is assigned to the target.user.attribute.roles.name field.
ComputerFQDN
principal.asset.network_domain
The value of ComputerFQDN from the raw log is assigned to the principal.asset.network_domain field.
ComputerID
principal.asset.asset_id
The value of ComputerID from the raw log is assigned to the principal.asset.asset_id field, prefixed with "ComputerId:".
ComputerName
about.hostname
The value of ComputerName from the raw log is assigned to the about.hostname field.
CredentialId
security_result.detection_fields.value
The value of CredentialId from the raw log is assigned to a security_result.detection_fields object with key: Credential Id.
DirectoryServiceName
security_result.detection_fields.value
The value of DirectoryServiceName from the raw log is assigned to a security_result.detection_fields object with key: Directory Service Name.
DirectoryServiceNameLocalized
security_result.detection_fields.value
The value of DirectoryServiceNameLocalized from the raw log is assigned to a security_result.detection_fields object with key: Directory Service Name Localized.
DirectoryServiceUuid
security_result.detection_fields.value
The value of DirectoryServiceUuid from the raw log is assigned to a security_result.detection_fields object with key: Directory Service Uuid.
EventMessage
security_result.summary
The value of EventMessage from the raw log is assigned to the security_result.summary field.
EventType
metadata.product_event_type
The value of EventType from the raw log is assigned to the metadata.product_event_type field. It is also used to determine the metadata.event_type.
FailReason
security_result.summary
The value of FailReason from the raw log is assigned to the security_result.summary field when present.
FailUserName
target.user.email_addresses
The value of FailUserName from the raw log is assigned to the target.user.email_addresses field when present.
FromIPAddress
principal.ip
The value of FromIPAddress from the raw log is assigned to the principal.ip field.
ID
security_result.detection_fields.value
The value of ID from the raw log is assigned to a security_result.detection_fields object with key: ID.
InternalTrackingID
metadata.product_log_id
The value of InternalTrackingID from the raw log is assigned to the metadata.product_log_id field.
JumpType
additional.fields.value.string_value
The value of JumpType from the raw log is assigned to an additional.fields object with key: Jump Type.
NormalizedUser
target.user.email_addresses
The value of NormalizedUser from the raw log is assigned to the target.user.email_addresses field.
OperationMode
additional.fields.value.string_value
The value of OperationMode from the raw log is assigned to an additional.fields object with key: Operation Mode.
ProxyId
security_result.detection_fields.value
The value of ProxyId from the raw log is assigned to a security_result.detection_fields object with key: Proxy Id.
RequestUserAgent
network.http.user_agent
The value of RequestUserAgent from the raw log is assigned to the network.http.user_agent field.
SessionGuid
network.session_id
The value of SessionGuid from the raw log is assigned to the network.session_id field.
Tenant
additional.fields.value.string_value
The value of Tenant from the raw log is assigned to an additional.fields object with key: Tenant.
ThreadType
additional.fields.value.string_value
The value of ThreadType from the raw log is assigned to an additional.fields object with key: Thread Type.
UserType
principal.user.attribute.roles.name
The value of UserType from the raw log is assigned to the principal.user.attribute.roles.name field.
WhenOccurred
metadata.event_timestamp
The value of WhenOccurred from the raw log is parsed and assigned to the metadata.event_timestamp field. This field also populates the top-level timestamp field.
Hardcoded value
metadata.product_name
"SSO".
Hardcoded value
metadata.event_type
Determined by the EventType field. Defaults to STATUS_UPDATE if EventType is not present or doesn't match any specific criteria. Can be USER_LOGIN, USER_CREATION, USER_RESOURCE_ACCESS, USER_LOGOUT, or USER_CHANGE_PASSWORD.
Hardcoded value
metadata.vendor_name
"CENTRIFY_SSO".
Hardcoded value
metadata.product_version
"SSO".
Hardcoded value
metadata.log_type
"Centrify".
Extracted from message field
network.session_id
If message field contains a session ID, it is extracted and used. Otherwise defaults to "1".
Extracted from host field
principal.hostname
Extracted from the host field if available, which comes from the syslog header.
Extracted from pid field
principal.process.pid
Extracted from the pid field if available, which comes from the syslog header.
UserGuid or extracted from message
target.user.userid
If UserGuid is present, its value is used. Otherwise, if message field contains a user ID, it is extracted and used.
Determined by Level and FailReason
security_result.action
Set to "ALLOW" if Level is "Info", and "BLOCK" if FailReason is present.
Determined by FailReason
security_result.category
Set to "AUTH_VIOLATION" if FailReason is present.
Determined by Level field
security_result.severity
Determined by the Level field. Set to "INFORMATIONAL" if Level is "Info", "MEDIUM" if Level is "Warning", and "ERROR" if Level is "Error".
Need more help?
Get answers from Community members and Google SecOps professionals.
