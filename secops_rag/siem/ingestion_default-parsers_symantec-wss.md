# Collect Symantec Web Security Service (WSS) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-wss/  
**Scraped:** 2026-03-05T09:28:50.923329Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec Web Security Service (WSS) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec Web Security Service (WSS) logs to Google Security Operations using Google Cloud Storage. The parser first attempts to parse the log message as JSON. If that fails, it uses a series of increasingly specific grok patterns to extract fields from the raw text, ultimately mapping the extracted data to the Unified Data Model (UDM). Symantec Web Security Service (WSS) is a cloud-based web security solution that provides real-time protection against web-based threats, including malware, phishing, and data loss.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Symantec Web Security Service Portal
Collect Symantec WSS API credentials
Get Symantec WSS site URL
Sign in to your Symantec Web Security Service portal.
Note your portal URL from the browser address bar.
Format:
https://portal.threatpulse.com
or your organization-specific URL
Example: If you access WSS at
https://portal.threatpulse.com/reportpod
, your site URL is
https://portal.threatpulse.com
Create API credentials
Sign in to the
Symantec Web Security Service Portal
as an administrator.
Go to
Account
>
API Credentials
.
Click
Add API Credentials
.
The portal displays the
Add API Credential
dialog with auto-generated
Username
and
Password
.
Copy and save the
Username
and
Password
securely.
Select the
API Expiry
option:
Time-based
: Define the date and time when this token expires.
Never expires
: Token remains valid indefinitely (recommended for production).
For the
Access
option, select
Reporting Access Logs
.
Click
Save
.
Verify permissions
To verify the account has the required permissions:
Sign in to the
Symantec Web Security Service Portal
.
Go to
Account
>
API Credentials
.
If you can see the API credentials you created with
Access
set to
Reporting Access Logs
, you have the required permissions.
If you cannot see this option, contact your administrator to grant
Reporting Access Logs
permission.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
WSS_USERNAME
=
"your-api-username"
WSS_PASSWORD
=
"your-api-password"
WSS_SYNC_URL
=
"https://portal.threatpulse.com/reportpod/logs/sync"
# Test API access (note: sync endpoint requires time parameters)
curl
-v
-H
"X-APIUsername:
${
WSS_USERNAME
}
"
\
-H
"X-APIPassword:
${
WSS_PASSWORD
}
"
\
"
${
WSS_SYNC_URL
}
?startDate=0&endDate=1000&token=none"
Expected response: HTTP 200 with log data or empty response if no logs in time range.
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
symantec-wss-logs
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
symantec-wss-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Symantec WSS logs
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
symantec-wss-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
symantec-wss-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Symantec WSS Sync API and writes them to GCS.
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
symantec-wss-collector
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
symantec-wss-trigger
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
symantec-wss-collector-sa
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
Description
GCS_BUCKET
symantec-wss-logs
GCS bucket name
GCS_PREFIX
symantec/wss/
Prefix for log files
STATE_KEY
symantec/wss/state.json
State file path
WINDOW_SECONDS
3600
Time window in seconds (1 hour)
HTTP_TIMEOUT
60
HTTP request timeout in seconds
MAX_RETRIES
3
Maximum retry attempts
USER_AGENT
symantec-wss-to-gcs/1.0
User agent string
WSS_SYNC_URL
https://portal.threatpulse.com/reportpod/logs/sync
WSS Sync API endpoint
WSS_API_USERNAME
your-api-username
(from API credentials)
WSS API username
WSS_API_PASSWORD
your-api-password
(from API credentials)
WSS API password
WSS_TOKEN_PARAM
none
Token parameter for sync API
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
timezone
import
uuid
import
time
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
60.0
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
Cloud Run function triggered by Pub/Sub to fetch logs from Symantec WSS Sync API and write to GCS.
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
'symantec/wss/'
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
'symantec/wss/state.json'
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
'symantec-wss-to-gcs/1.0'
)
wss_sync_url
=
os
.
environ
.
get
(
'WSS_SYNC_URL'
,
'https://portal.threatpulse.com/reportpod/logs/sync'
)
api_username
=
os
.
environ
.
get
(
'WSS_API_USERNAME'
)
api_password
=
os
.
environ
.
get
(
'WSS_API_PASSWORD'
)
token_param
=
os
.
environ
.
get
(
'WSS_TOKEN_PARAM'
,
'none'
)
if
not
all
([
bucket_name
,
api_username
,
api_password
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
,
now
-
window_sec
))
to_ts
=
now
# Convert to milliseconds for WSS API
start_ms
=
int
(
from_ts
*
1000
)
end_ms
=
int
(
to_ts
*
1000
)
print
(
f
'Fetching Symantec WSS logs from
{
start_ms
}
to
{
end_ms
}
'
)
# Fetch logs from WSS Sync API
blob_data
,
content_type
,
content_encoding
=
fetch_wss_logs
(
wss_sync_url
,
api_username
,
api_password
,
token_param
,
start_ms
,
end_ms
,
user_agent
,
http_timeout
,
max_retries
)
print
(
f
'Retrieved
{
len
(
blob_data
)
}
bytes with content-type:
{
content_type
}
'
)
if
content_encoding
:
print
(
f
'Content encoding:
{
content_encoding
}
'
)
# Write to GCS
if
blob_data
:
blob_name
=
write_wss_data
(
bucket
,
prefix
,
blob_data
,
content_type
,
content_encoding
,
from_ts
,
to_ts
)
print
(
f
'Wrote logs to
{
blob_name
}
'
)
# Update state
save_state
(
bucket
,
state_key
,
{
'last_to_ts'
:
to_ts
,
'last_successful_run'
:
now
})
print
(
f
'Successfully processed logs up to
{
to_ts
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
fetch_wss_logs
(
sync_url
,
username
,
password
,
token
,
start_ms
,
end_ms
,
user_agent
,
timeout
,
max_retries
):
"""Fetch logs from WSS Sync API with retry logic using custom HTTP headers."""
params
=
f
"startDate=
{
start_ms
}
&
endDate=
{
end_ms
}
&
token=
{
token
}
"
url
=
f
"
{
sync_url
}
?
{
params
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
headers
=
{
'User-Agent'
:
user_agent
,
'X-APIUsername'
:
username
,
'X-APIPassword'
:
password
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
timeout
)
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
'Rate limited (429). Retrying after
{
retry_after
}
s...'
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
==
200
:
content_type
=
response
.
headers
.
get
(
'Content-Type'
,
'application/octet-stream'
)
content_encoding
=
response
.
headers
.
get
(
'Content-Encoding'
,
''
)
return
response
.
data
,
content_type
,
content_encoding
else
:
raise
Exception
(
f
'HTTP
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
,
errors
=
"ignore"
)
}
'
)
except
Exception
as
e
:
attempt
+=
1
print
(
f
'HTTP error on attempt
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
# Exponential backoff with jitter
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
determine_extension
(
content_type
,
content_encoding
):
"""Determine file extension based on content type and encoding."""
if
'zip'
in
content_type
.
lower
():
return
'.zip'
if
'gzip'
in
content_type
.
lower
()
or
content_encoding
.
lower
()
==
'gzip'
:
return
'.gz'
if
'json'
in
content_type
.
lower
():
return
'.json'
if
'csv'
in
content_type
.
lower
():
return
'.csv'
return
'.bin'
def
write_wss_data
(
bucket
,
prefix
,
blob_data
,
content_type
,
content_encoding
,
from_ts
,
to_ts
):
"""Write WSS data to GCS with unique key."""
ts_path
=
datetime
.
fromtimestamp
(
to_ts
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
'
)
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
ext
=
determine_extension
(
content_type
,
content_encoding
)
blob_name
=
f
"
{
prefix
}{
ts_path
}
/symantec_wss_
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
}{
ext
}
"
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
blob_data
,
content_type
=
content_type
)
# Set metadata
blob
.
metadata
=
{
'source'
:
'symantec-wss'
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
)),
'content_encoding'
:
content_encoding
}
blob
.
patch
()
return
blob_name
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
symantec-wss-collector-hourly
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
symantec-wss-trigger
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
symantec-wss-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching
Symantec
WSS
logs
from
[
start_ms
]
to
[
end_ms
]
Retrieved
X
bytes
with
content
-
type
:
[
type
]
Wrote
logs
to
symantec
/
wss
/
YYYY
/
MM
/
DD
/
symantec_wss_
[
timestamps
]
.
[
ext
]
Successfully
processed
logs
up
to
[
timestamp
]
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
symantec/wss/
).
Verify that a new file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables. Verify username and password are correct.
HTTP 403
: Verify API credentials have "Reporting Access Logs" permission enabled in WSS portal.
HTTP 429
: Rate limiting - function will automatically retry with backoff.
Missing environment variables
: Check all required variables are set in Cloud Run function configuration.
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
Symantec WSS logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Symantec WSS
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
Configure a feed in Google SecOps to ingest Symantec WSS logs
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
Symantec WSS logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Symantec WSS
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://symantec-wss-logs/symantec/wss/
Replace:
symantec-wss-logs
: Your GCS bucket name.
symantec/wss/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/symantec-wss/
With subfolder:
gs://company-logs/symantec/wss/
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
category_id
read_only_udm.metadata.product_event_type
If category_id is 1, then read_only_udm.metadata.product_event_type is set to Security. If category_id is 5, then read_only_udm.metadata.product_event_type is set to Policy
collector_device_ip
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Value of collector_device_ip field
connection.bytes_download
read_only_udm.network.received_bytes
Value of connection.bytes_download field converted to integer
connection.bytes_upload
read_only_udm.network.sent_bytes
Value of connection.bytes_upload field converted to integer
connection.dst_ip
read_only_udm.target.ip
Value of connection.dst_ip field
connection.dst_location.country
read_only_udm.target.location.country_or_region
Value of connection.dst_location.country field
connection.dst_name
read_only_udm.target.hostname
Value of connection.dst_name field
connection.dst_port
read_only_udm.target.port
Value of connection.dst_port field converted to integer
connection.http_status
read_only_udm.network.http.response_code
Value of connection.http_status field converted to integer
connection.http_user_agent
read_only_udm.network.http.user_agent
Value of connection.http_user_agent field
connection.src_ip
read_only_udm.principal.ip, read_only_udm.src.ip
Value of connection.src_ip field. If src_ip or collector_device_ip is not empty, then it is mapped to read_only_udm.src.ip
connection.tls.version
read_only_udm.network.tls.version_protocol
Value of connection.tls.version field
connection.url.host
read_only_udm.target.hostname
Value of connection.url.host field
connection.url.method
read_only_udm.network.http.method
Value of connection.url.method field
connection.url.path
read_only_udm.target.url
Value of connection.url.path field
connection.url.text
read_only_udm.target.url
Value of connection.url.text field
cs_connection_negotiated_cipher
read_only_udm.network.tls.cipher
Value of cs_connection_negotiated_cipher field
cs_icap_status
read_only_udm.security_result.description
Value of cs_icap_status field
device_id
read_only_udm.target.resource.id, read_only_udm.target.resource.product_object_id
Value of device_id field
device_ip
read_only_udm.intermediary.ip, read_only_udm.intermediary.asset.ip
Value of device_ip field
device_time
read_only_udm.metadata.collected_timestamp, read_only_udm.metadata.event_timestamp
Value of device_time field converted to string. If when is empty, then it is mapped to read_only_udm.metadata.event_timestamp
hostname
read_only_udm.principal.hostname, read_only_udm.principal.asset.hostname
Value of hostname field
log_time
read_only_udm.metadata.event_timestamp
Value of log_time field converted to timestamp. If when and device_time are empty, then it is mapped to read_only_udm.metadata.event_timestamp
msg_desc
read_only_udm.metadata.description
Value of msg_desc field
os_details
read_only_udm.target.asset.platform_software.platform, read_only_udm.target.asset.platform_software.platform_version
Value of os_details field. If os_details is not empty, then it is parsed to extract os_name and os_ver. If os_name contains Windows, then read_only_udm.target.asset.platform_software.platform is set to WINDOWS. os_ver is mapped to read_only_udm.target.asset.platform_software.platform_version
product_data.cs(Referer)
read_only_udm.network.http.referral_url
Value of product_data.cs(Referer) field
product_data.r-supplier-country
read_only_udm.principal.location.country_or_region
Value of product_data.r-supplier-country field
product_data.s-supplier-ip
read_only_udm.intermediary.ip, read_only_udm.intermediary.asset.ip
Value of product_data.s-supplier-ip field
product_data.x-bluecoat-application-name
read_only_udm.target.application
Value of product_data.x-bluecoat-application-name field
product_data.x-bluecoat-transaction-uuid
read_only_udm.metadata.product_log_id
Value of product_data.x-bluecoat-transaction-uuid field
product_data.x-client-agent-sw
read_only_udm.observer.platform_version
Value of product_data.x-client-agent-sw field
product_data.x-client-agent-type
read_only_udm.observer.application
Value of product_data.x-client-agent-type field
product_data.x-client-device-id
read_only_udm.target.resource.type, read_only_udm.target.resource.id, read_only_udm.target.resource.product_object_id
If not empty, read_only_udm.target.resource.type is set to DEVICE. Value of product_data.x-client-device-id field is mapped to read_only_udm.target.resource.id and read_only_udm.target.resource.product_object_id
product_data.x-client-device-name
read_only_udm.src.hostname, read_only_udm.src.asset.hostname
Value of product_data.x-client-device-name field
product_data.x-cs-client-ip-country
read_only_udm.target.location.country_or_region
Value of product_data.x-cs-client-ip-country field
product_data.x-cs-connection-negotiated-cipher
read_only_udm.network.tls.cipher
Value of product_data.x-cs-connection-negotiated-cipher field
product_data.x-cs-connection-negotiated-ssl-version
read_only_udm.network.tls.version_protocol
Value of product_data.x-cs-connection-negotiated-ssl-version field
product_data.x-exception-id
read_only_udm.security_result.summary
Value of product_data.x-exception-id field
product_data.x-rs-certificate-hostname
read_only_udm.network.tls.client.server_name
Value of product_data.x-rs-certificate-hostname field
product_data.x-rs-certificate-hostname-categories
read_only_udm.security_result.category_details
Value of product_data.x-rs-certificate-hostname-categories field
product_data.x-rs-certificate-observed-errors
read_only_udm.network.tls.server.certificate.issuer
Value of product_data.x-rs-certificate-observed-errors field
product_data.x-rs-certificate-validate-status
read_only_udm.network.tls.server.certificate.subject
Value of product_data.x-rs-certificate-validate-status field
product_name
read_only_udm.metadata.product_name
Value of product_name field
product_ver
read_only_udm.metadata.product_version
Value of product_ver field
proxy_connection.src_ip
read_only_udm.intermediary.ip, read_only_udm.intermediary.asset.ip
Value of proxy_connection.src_ip field
received_bytes
read_only_udm.network.received_bytes
Value of received_bytes field converted to integer
ref_uid
read_only_udm.metadata.product_log_id
Value of ref_uid field
s_action
read_only_udm.metadata.description
Value of s_action field
sent_bytes
read_only_udm.network.sent_bytes
Value of sent_bytes field converted to integer
severity_id
read_only_udm.security_result.severity
If severity_id is 1 or 2, then read_only_udm.security_result.severity is set to LOW. If severity_id is 3 or 4, then read_only_udm.security_result.severity is set to MEDIUM. If severity_id is 5 or 6, then read_only_udm.security_result.severity is set to HIGH
supplier_country
read_only_udm.principal.location.country_or_region
Value of supplier_country field
target_ip
read_only_udm.target.ip, read_only_udm.target.asset.ip
Value of target_ip field
user.full_name
read_only_udm.principal.user.user_display_name
Value of user.full_name field
user.name
read_only_udm.principal.user.user_display_name
Value of user.name field
user_name
read_only_udm.principal.user.user_display_name
Value of user_name field
uuid
read_only_udm.metadata.product_log_id
Value of uuid field
when
read_only_udm.metadata.event_timestamp
Value of when field converted to timestamp
read_only_udm.metadata.event_type
Set to NETWORK_UNCATEGORIZED if hostname is empty and connection.dst_ip is not empty. Set to SCAN_NETWORK if hostname is not empty. Set to NETWORK_CONNECTION if has_principal and has_target are true. Set to STATUS_UPDATE if has_principal is true and has_target is false. Set to GENERIC_EVENT if has_principal and has_target are false
read_only_udm.metadata.log_type
Always set to SYMANTEC_WSS
read_only_udm.metadata.vendor_name
Always set to SYMANTEC
read_only_udm.security_result.action
Set to ALLOW if product_data.sc-filter_result is OBSERVED or PROXIED. Set to BLOCK if product_data.sc-filter_result is DENIED
read_only_udm.security_result.action_details
Value of product_data.sc-filter_result field
read_only_udm.target.resource.type
Set to DEVICE if product_data.x-client-device-id is not empty
Need more help?
Get answers from Community members and Google SecOps professionals.
