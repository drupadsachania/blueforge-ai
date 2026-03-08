# Collect ForgeRock OpenIDM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openidm/  
**Scraped:** 2026-03-05T09:56:09.577842Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ForgeRock OpenIDM logs
Supported in:
Google secops
SIEM
This document explains how to ingest ForgeRock OpenIDM logs to Google Security Operations using Google Cloud Storage V2.
ForgeRock OpenIDM (now branded as PingIDM) is an identity management platform that provides user provisioning, synchronization, password management, and access governance. It logs identity lifecycle events, authentication attempts, reconciliation operations, and configuration changes to audit logs accessible over REST.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to ForgeRock OpenIDM or PingIDM instance with administrative credentials
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
forgerock-openidm-audit-logs
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
Collect ForgeRock OpenIDM credentials
Get ForgeRock OpenIDM base URL
Sign in to your ForgeRock OpenIDM or PingIDM instance.
Note your base URL from the browser address bar.
Format:
https://openidm.example.com
Do not include trailing slashes or paths like
/admin
Get administrative credentials
Obtain administrative credentials for your ForgeRock OpenIDM instance.
You will need:
Username
: Administrative username (for example,
openidm-admin
)
Password
: Administrative password
Verify permissions
To verify the account has the required permissions:
Sign in to ForgeRock OpenIDM.
Go to
Configure
>
System Preferences
>
Audit
.
If you can see audit configuration and topics, you have the required permissions.
If you cannot see this option, contact your administrator to grant audit read permissions.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
OPENIDM_BASE_URL
=
"https://openidm.example.com"
OPENIDM_USERNAME
=
"openidm-admin"
OPENIDM_PASSWORD
=
"your-admin-password"
# Test API access to authentication audit topic
curl
-v
\
-H
"X-OpenIDM-Username:
${
OPENIDM_USERNAME
}
"
\
-H
"X-OpenIDM-Password:
${
OPENIDM_PASSWORD
}
"
\
-H
"Accept-API-Version: resource=1.0"
\
-H
"Accept: application/json"
\
"
${
OPENIDM_BASE_URL
}
/openidm/audit/authentication?_queryFilter=true&_pageSize=1"
Expected response: HTTP 200 with JSON containing audit events.
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
forgerock-openidm-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect ForgeRock OpenIDM logs
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
forgerock-openidm-audit-logs
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
forgerock-openidm-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
forgerock-openidm-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from ForgeRock OpenIDM API and write them to GCS.
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
forgerock-openidm-collector
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
forgerock-openidm-trigger
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
Scroll to and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select the service account
forgerock-openidm-collector-sa
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
forgerock-openidm-audit-logs
GCS bucket name
GCS_PREFIX
openidm
Prefix for log files
STATE_KEY
openidm/state.json
State file path
OPENIDM_BASE_URL
https://openidm.example.com
OpenIDM base URL
OPENIDM_USERNAME
openidm-admin
OpenIDM admin username
OPENIDM_PASSWORD
your-admin-password
OpenIDM admin password
AUDIT_TOPICS
access,activity,authentication,config,sync
Comma-separated audit topics
PAGE_SIZE
100
Records per page
MAX_PAGES
50
Maximum pages per topic
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
will open automatically.
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
urllib3
from
datetime
import
datetime
,
timezone
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
'openidm'
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
'openidm/state.json'
)
OPENIDM_BASE_URL
=
os
.
environ
.
get
(
'OPENIDM_BASE_URL'
)
OPENIDM_USERNAME
=
os
.
environ
.
get
(
'OPENIDM_USERNAME'
)
OPENIDM_PASSWORD
=
os
.
environ
.
get
(
'OPENIDM_PASSWORD'
)
AUDIT_TOPICS
=
os
.
environ
.
get
(
'AUDIT_TOPICS'
,
'access,activity,authentication,config,sync'
)
.
split
(
','
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
'100'
))
MAX_PAGES
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
'50'
))
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch ForgeRock OpenIDM logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
OPENIDM_BASE_URL
,
OPENIDM_USERNAME
,
OPENIDM_PASSWORD
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
GCS_BUCKET
)
# Load state
state
=
load_state
(
bucket
,
STATE_KEY
)
all_events
=
[]
for
topic
in
AUDIT_TOPICS
:
topic
=
topic
.
strip
()
print
(
f
"Fetching audit logs for topic:
{
topic
}
"
)
events
=
fetch_audit_logs
(
topic
,
state
.
get
(
topic
,
{}))
all_events
.
extend
(
events
)
if
events
:
latest_timestamp
=
max
(
e
.
get
(
'timestamp'
,
''
)
for
e
in
events
)
state
[
topic
]
=
{
'last_timestamp'
:
latest_timestamp
,
'last_run'
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
(),
'events_count'
:
len
(
events
)
}
if
all_events
:
write_to_gcs
(
bucket
,
all_events
)
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
"Successfully processed
{
len
(
all_events
)
}
audit events"
)
else
:
print
(
"No new audit events to process"
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
"Warning: Could not load state:
{
e
}
"
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
f
"Saved state:
{
json
.
dumps
(
state
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
"Warning: Could not save state:
{
e
}
"
)
def
fetch_audit_logs
(
topic
,
topic_state
):
"""
Fetch audit logs from ForgeRock OpenIDM API with pagination.
Args:
topic: Audit topic name
topic_state: State dictionary for this topic
Returns:
List of audit events
"""
base_url
=
OPENIDM_BASE_URL
.
rstrip
(
'/'
)
all_events
=
[]
last_timestamp
=
topic_state
.
get
(
'last_timestamp'
)
query_filter
=
'true'
if
last_timestamp
:
query_filter
=
f
'timestamp gt "
{
last_timestamp
}
"'
page_offset
=
0
page_count
=
0
while
page_count
<
MAX_PAGES
:
try
:
url
=
f
"
{
base_url
}
/openidm/audit/
{
topic
}
"
params
=
{
'_queryFilter'
:
query_filter
,
'_pageSize'
:
str
(
PAGE_SIZE
),
'_pagedResultsOffset'
:
str
(
page_offset
),
'_sortKeys'
:
'timestamp'
}
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
urllib3
.
request
.
urlencode
({
k
:
v
})[
len
(
k
)
+
1
:]
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
url
}
?
{
query_string
}
"
headers
=
{
'X-OpenIDM-Username'
:
OPENIDM_USERNAME
,
'X-OpenIDM-Password'
:
OPENIDM_PASSWORD
,
'Accept-API-Version'
:
'resource=1.0'
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
full_url
,
headers
=
headers
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
"API error for topic
{
topic
}
:
{
response
.
status
}
-
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
events
=
data
.
get
(
'result'
,
[])
if
not
events
:
print
(
f
"No more events for topic
{
topic
}
"
)
break
all_events
.
extend
(
events
)
page_offset
+=
PAGE_SIZE
page_count
+=
1
print
(
f
"Fetched page
{
page_count
}
for topic
{
topic
}
, total events:
{
len
(
all_events
)
}
"
)
if
len
(
events
)
<
PAGE_SIZE
:
break
except
urllib3
.
exceptions
.
HTTPError
as
e
:
print
(
f
"HTTP error for topic
{
topic
}
:
{
str
(
e
)
}
"
)
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
"JSON decode error for topic
{
topic
}
:
{
str
(
e
)
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
"Unexpected error for topic
{
topic
}
:
{
str
(
e
)
}
"
)
break
return
all_events
def
write_to_gcs
(
bucket
,
events
):
"""Write events to GCS as NDJSON."""
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
filename
=
f
"
{
GCS_PREFIX
}
/openidm_audit_
{
timestamp
}
.json"
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
event
)
for
event
in
events
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
.
encode
(
'utf-8'
),
content_type
=
'application/x-ndjson'
)
print
(
f
"Wrote
{
len
(
events
)
}
events to gs://
{
GCS_BUCKET
}
/
{
filename
}
"
)
Second file:
requirements.txt:
functions-framework==3.*
google-cloud-storage==2.*
urllib3>=2.0.0
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
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
forgerock-openidm-collector-hourly
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
forgerock-openidm-trigger
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose the frequency based on log volume and latency requirements:
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
console, find your job
forgerock-openidm-collector-hourly
.
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click your function name
forgerock-openidm-collector
.
Click the
Logs
tab.
Verify the function executed successfully. Look for:
Fetching audit logs for topic: access
Fetched page 1 for topic access, total events: X
Wrote X events to gs://forgerock-openidm-audit-logs/openidm/openidm_audit_YYYYMMDD_HHMMSS.json
Successfully processed X audit events
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name
forgerock-openidm-audit-logs
.
Navigate to the prefix folder
openidm/
.
Verify that a new
.json
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check OpenIDM credentials in environment variables
HTTP 403
: Verify account has audit read permissions
HTTP 404
: Verify OPENIDM_BASE_URL is correct and does not include trailing paths
Missing environment variables
: Check all required variables are set
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest ForgeRock OpenIDM logs
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
ForgeRock OpenIDM Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
FORGEROCK_OPENIDM
as the
Log type
.
Click
Get Service Account
.
A unique service account email will be displayed, for example:
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
Copy this email address. You will use it in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://forgerock-openidm-audit-logs/openidm/
Replace:
forgerock-openidm-audit-logs
: Your GCS bucket name.
openidm
: The prefix path where logs are stored.
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
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name
forgerock-openidm-audit-logs
.
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
UDM mapping table
Log field
UDM mapping
Logic
additional_label, additional_elapsed_time, additional_ContentLength, additional_accept_encoding, additional_Accept, additional_accept_language, additional_origin_hop, additional_cache_control, additional_Connection, additional_Cookie, additional_Pragma, additional_exchange_id, additional_contentType, additional_X-content_type-Options, fluenttag_label, source_label, topic_label, request_protocol_label, taskName_label, linkQualifier_label, situation_label, mapping_label, eventid_label, context_roles_label, field_names_label
additional.fields
Additional key-value pairs
Via
intermediary.hostname
Hostname of the intermediary
x_forwarded_ip, ip, caller.callerIps
intermediary.ip
IP address of the intermediary
timestamp
metadata.event_timestamp
Timestamp of the event
metadata.event_type
Type of the event
transactionId
metadata.product_deployment_id
Deployment identifier of the product
eventName
metadata.product_event_type
Event type from the product
_id, trackingIds
metadata.product_log_id
Log identifier from the product
http.request.secure
network.application_protocol
Application protocol
http_version
network.application_protocol_version
Version of the application protocol
request_method, http.request.method
network.http.method
HTTP method
user_agent, http.request.headers.user_agent.0
network.http.parsed_user_agent
Parsed user agent
refferal_url
network.http.referral_url
Referral URL
response.statusCode, status_code
network.http.response_code
HTTP response code
user_agent, http.request.headers.user_agent
network.http.user_agent
User agent string
transaction_id, transactionId
network.session_id
Session identifier
Host
principal.asset.hostname
Hostname of the principal's asset
true_client_ip, client.ip, context.ipAddress, entry.info.ipAddress, src_ip
principal.asset.ip
IP address of the principal's asset
Host
principal.hostname
Hostname of the principal
true_client_ip, client.ip, context.ipAddress, entry.info.ipAddress, src_ip
principal.ip
IP address of the principal
client.port, src_port
principal.port
Port of the principal
component_label, moduleId_label, query_id_label
principal.resource.attribute.labels
Attribute labels for the principal's resource
entry.info.treeName
principal.resource.name
Name of the principal's resource
sourceObjectId, objectId, entry.info.nodeId
principal.resource.product_object_id
Product object ID for the principal's resource
entry.info.authLevel
principal.resource.resource_subtype
Subtype of the principal's resource
user_roles_property_label, authentication_id_label, authentication_id_property_label
principal.user.attribute.labels
Attribute labels for the principal's user
userId, principalData.0
principal.user.userid
User ID of the principal
security_action
security_result.action
Action taken in the security result
result, action
security_result.action_details
Details of the action
result_label, moduleId_label, nodeType_label, displayName_label, nodeOutcome_label, elapsedTimeUnits_label, elapsedTime_label, operation_label, taskName_label, linkQualifier_label, situation_label, mapping_label
security_result.detection_fields
Detection fields
level
security_result.severity
Severity of the security result
level
security_result.severity_details
Details of the severity
response_detail_reason
security_result.summary
Summary of the security result
http.request.headers.host.0
target.asset.hostname
Hostname of the target's asset
server.ip, x_forwarded_ip
target.asset.ip
IP address of the target's asset
http.request.headers.host.0
target.hostname
Hostname of the target
server.ip, x_forwarded_ip
target.ip
IP address of the target
server.port
target.port
Port of the target
targetObjectId
target.resource.product_object_id
Product object ID for the target's resource
http.request.path
target.url
URL of the target
metadata.product_name
Name of the product
metadata.vendor_name
Name of the vendor
Need more help?
Get answers from Community members and Google SecOps professionals.
