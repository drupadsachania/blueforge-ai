# Collect Cisco AMP for Endpoints logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp/  
**Scraped:** 2026-03-05T09:52:05.324172Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco AMP for Endpoints logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco AMP for Endpoints logs to Google Security Operations using Google Cloud Storage. The parser transforms raw JSON formatted logs into a structured format conforming to the Chronicle UDM. It extracts fields from nested JSON objects, maps them to the UDM schema, identifies event categories, assigns severity levels, and ultimately generates a unified event output, flagging security alerts when specific conditions are met.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Cisco AMP for Endpoints console
Collect Cisco AMP for Endpoints API credentials
Sign in to the Cisco AMP for Endpoints console.
Go to
Accounts
>
API Credentials
.
Click
New API Credential
to create a new API key and client ID.
Provide the following configuration details:
Application Name
: Enter a name (for example,
Chronicle SecOps Integration
).
Scope
: Select
Read-only
for basic event polling.
Click
Create
.
Copy and save in a secure location the following details:
3API Client ID
API Key
API Base URL
: Depending on your region:
US:
https://api.amp.cisco.com
EU:
https://api.eu.amp.cisco.com
APJC:
https://api.apjc.amp.cisco.com
Verify permissions
To verify the account has the required permissions:
Sign in to Cisco AMP for Endpoints console.
Go to
Accounts
>
API Credentials
.
If you can see the
API Credentials
page and your newly created credential is listed, you have the required permissions.
If you cannot see this option, contact your administrator to grant API access permissions.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
AMP_CLIENT_ID
=
"your-client-id"
AMP_API_KEY
=
"your-api-key"
API_BASE
=
"https://api.amp.cisco.com"
# Test API access
curl
-v
-u
"
${
AMP_CLIENT_ID
}
:
${
AMP_API_KEY
}
"
"
${
API_BASE
}
/v1/events?limit=1"
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
cisco-amp-logs
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
cisco-amp-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Cisco AMP for Endpoints logs
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
Grant the service account (
cisco-amp-collector-sa
) write permissions on the GCS bucket:
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
cisco-amp-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
cisco-amp-events-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco AMP for Endpoints API and write them to GCS.
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
cisco-amp-events-collector
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
cisco-amp-events-trigger
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
Select
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
cisco-amp-collector-sa
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
cisco-amp-logs
GCS bucket name
GCS_PREFIX
cisco-amp-events/
Prefix for log files
STATE_KEY
cisco-amp-events/state.json
State file path
API_BASE
https://api.amp.cisco.com
API base URL
AMP_CLIENT_ID
your-client-id
API client ID
AMP_API_KEY
your-api-key
API key
PAGE_SIZE
500
Records per page
MAX_PAGES
10
Maximum pages to fetch
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
'cisco-amp-events/'
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
'cisco-amp-events/state.json'
)
API_BASE
=
os
.
environ
.
get
(
'API_BASE'
)
AMP_CLIENT_ID
=
os
.
environ
.
get
(
'AMP_CLIENT_ID'
)
AMP_API_KEY
=
os
.
environ
.
get
(
'AMP_API_KEY'
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
'500'
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
'10'
))
def
parse_datetime
(
value
:
str
)
-
>
datetime
:
"""Parse ISO datetime string to datetime object."""
if
value
.
endswith
(
"Z"
):
value
=
value
[:
-
1
]
+
"+00:00"
return
datetime
.
fromisoformat
(
value
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
Cloud Run function triggered by Pub/Sub to fetch Cisco AMP events and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
API_BASE
,
AMP_CLIENT_ID
,
AMP_API_KEY
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
# Determine time window
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
last_time
=
None
if
isinstance
(
state
,
dict
)
and
state
.
get
(
"last_event_time"
):
try
:
last_time
=
parse_datetime
(
state
[
"last_event_time"
])
# Overlap by 2 minutes to catch any delayed events
last_time
=
last_time
-
timedelta
(
minutes
=
2
)
except
Exception
as
e
:
print
(
f
"Warning: Could not parse last_event_time:
{
e
}
"
)
if
last_time
is
None
:
last_time
=
now
-
timedelta
(
days
=
1
)
print
(
f
"Fetching logs from
{
last_time
.
isoformat
()
}
to
{
now
.
isoformat
()
}
"
)
# Fetch logs
records
,
newest_event_time
=
fetch_logs
(
api_base
=
API_BASE
,
client_id
=
AMP_CLIENT_ID
,
api_key
=
AMP_API_KEY
,
start_time
=
last_time
,
page_size
=
PAGE_SIZE
,
max_pages
=
MAX_PAGES
,
)
if
not
records
:
print
(
"No new log records found."
)
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
return
# Write to GCS as NDJSON
timestamp
=
now
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
object_key
=
f
"
{
GCS_PREFIX
}
cisco_amp_events_
{
timestamp
}
.ndjson"
blob
=
bucket
.
blob
(
object_key
)
ndjson
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
record
,
ensure_ascii
=
False
)
for
record
in
records
])
+
'
\n
'
blob
.
upload_from_string
(
ndjson
,
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
records
)
}
records to gs://
{
GCS_BUCKET
}
/
{
object_key
}
"
)
# Update state with newest event time
if
newest_event_time
:
save_state
(
bucket
,
STATE_KEY
,
newest_event_time
)
else
:
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
print
(
f
"Successfully processed
{
len
(
records
)
}
records"
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
last_event_time_iso
:
str
):
"""Save the last event timestamp to GCS state file."""
try
:
state
=
{
'last_event_time'
:
last_event_time_iso
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
"Saved state: last_event_time=
{
last_event_time_iso
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
fetch_logs
(
api_base
:
str
,
client_id
:
str
,
api_key
:
str
,
start_time
:
datetime
,
page_size
:
int
,
max_pages
:
int
):
"""
Fetch logs from Cisco AMP for Endpoints API with pagination and rate limiting.
Args:
api_base: API base URL
client_id: API client ID
api_key: API key
start_time: Start time for log query
page_size: Number of records per page
max_pages: Maximum total pages to fetch
Returns:
Tuple of (records list, newest_event_time ISO string)
"""
# Clean up base URL
base_url
=
api_base
.
rstrip
(
'/'
)
endpoint
=
f
"
{
base_url
}
/v1/events"
# Create Basic Auth header
auth_string
=
f
"
{
client_id
}
:
{
api_key
}
"
auth_bytes
=
auth_string
.
encode
(
'utf-8'
)
auth_b64
=
base64
.
b64encode
(
auth_bytes
)
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
auth_b64
}
'
,
'Accept'
:
'application/json'
,
'User-Agent'
:
'GoogleSecOps-CiscoAMPCollector/1.0'
}
records
=
[]
newest_time
=
None
page_num
=
0
backoff
=
1.0
# Build initial URL with start_date parameter
start_date_str
=
start_time
.
isoformat
()
+
'Z'
if
not
start_time
.
isoformat
()
.
endswith
(
'Z'
)
else
start_time
.
isoformat
()
next_url
=
f
"
{
endpoint
}
?limit=
{
page_size
}
&
start_date=
{
start_date_str
}
"
while
next_url
and
page_num
<
max_pages
:
page_num
+=
1
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
next_url
,
headers
=
headers
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
print
(
f
"HTTP Error:
{
response
.
status
}
"
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
"Response body:
{
response_text
[:
256
]
}
"
)
return
[],
None
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
# Extract events from response
page_results
=
data
.
get
(
'data'
,
[])
if
not
page_results
:
print
(
f
"No more results (empty page)"
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
page_results
)
}
events"
)
records
.
extend
(
page_results
)
# Track newest event time
for
event
in
page_results
:
try
:
event_time
=
event
.
get
(
'date'
)
if
event_time
:
if
newest_time
is
None
or
parse_datetime
(
event_time
)
>
parse_datetime
(
newest_time
):
newest_time
=
event_time
except
Exception
as
e
:
print
(
f
"Warning: Could not parse event time:
{
e
}
"
)
# Check for next page URL in metadata
next_url
=
data
.
get
(
'metadata'
,
{})
.
get
(
'links'
,
{})
.
get
(
'next'
)
if
not
next_url
:
print
(
"No more pages (no next URL)"
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
"Error fetching logs:
{
e
}
"
)
return
[],
None
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
total records from
{
page_num
}
pages"
)
return
records
,
newest_time
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
cisco-amp-events-collector-hourly
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
cisco-amp-events-trigger
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
Click your function name (
cisco-amp-events-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
Page 1: Retrieved X events
Wrote X records to gs://cisco-amp-logs/cisco-amp-events/cisco_amp_events_YYYYMMDD_HHMMSS.ndjson
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
cisco-amp-events/
).
Verify that a new
.ndjson
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables
HTTP 403
: Verify account has required permissions
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
Cisco AMP for Endpoints logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cisco AMP
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
Configure a feed in Google SecOps to ingest Cisco AMP for Endpoints logs
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
Cisco AMP for Endpoints logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cisco AMP
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://cisco-amp-logs/cisco-amp-events/
Replace:
cisco-amp-logs
: Your GCS bucket name.
cisco-amp-events/
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
active
read_only_udm.principal.asset.active
Directly mapped from computer.active
connector_guid
read_only_udm.principal.asset.uuid
Directly mapped from computer.connector_guid
date
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from date after converting to timestamp
detection
read_only_udm.security_result.threat_name
Directly mapped from detection
detection_id
read_only_udm.security_result.detection_fields.value
Directly mapped from detection_id
disposition
read_only_udm.security_result.description
Directly mapped from file.disposition
error.error_code
read_only_udm.security_result.detection_fields.value
Directly mapped from error.error_code
error.description
read_only_udm.security_result.detection_fields.value
Directly mapped from error.description
event_type
read_only_udm.metadata.product_event_type
Directly mapped from event_type
event_type_id
read_only_udm.metadata.product_log_id
Directly mapped from event_type_id
external_ip
read_only_udm.principal.asset.external_ip
Directly mapped from computer.external_ip
file.file_name
read_only_udm.target.file.names
Directly mapped from file.file_name
file.file_path
read_only_udm.target.file.full_path
Directly mapped from file.file_path
file.identity.md5
read_only_udm.security_result.about.file.md5
Directly mapped from file.identity.md5
file.identity.md5
read_only_udm.target.file.md5
Directly mapped from file.identity.md5
file.identity.sha1
read_only_udm.security_result.about.file.sha1
Directly mapped from file.identity.sha1
file.identity.sha1
read_only_udm.target.file.sha1
Directly mapped from file.identity.sha1
file.identity.sha256
read_only_udm.security_result.about.file.sha256
Directly mapped from file.identity.sha256
file.identity.sha256
read_only_udm.target.file.sha256
Directly mapped from file.identity.sha256
file.parent.disposition
read_only_udm.target.resource.attribute.labels.value
Directly mapped from file.parent.disposition
file.parent.file_name
read_only_udm.target.resource.attribute.labels.value
Directly mapped from file.parent.file_name
file.parent.identity.md5
read_only_udm.target.resource.attribute.labels.value
Directly mapped from file.parent.identity.md5
file.parent.identity.sha1
read_only_udm.target.resource.attribute.labels.value
Directly mapped from file.parent.identity.sha1
file.parent.identity.sha256
read_only_udm.target.resource.attribute.labels.value
Directly mapped from file.parent.identity.sha256
file.parent.process_id
read_only_udm.security_result.about.process.parent_process.pid
Directly mapped from file.parent.process_id
file.parent.process_id
read_only_udm.target.process.parent_process.pid
Directly mapped from file.parent.process_id
hostname
read_only_udm.principal.asset.hostname
Directly mapped from computer.hostname
hostname
read_only_udm.target.hostname
Directly mapped from computer.hostname
hostname
read_only_udm.target.asset.hostname
Directly mapped from computer.hostname
ip
read_only_udm.principal.asset.ip
Directly mapped from computer.network_addresses.ip
ip
read_only_udm.principal.ip
Directly mapped from computer.network_addresses.ip
ip
read_only_udm.security_result.about.ip
Directly mapped from computer.network_addresses.ip
mac
read_only_udm.principal.mac
Directly mapped from computer.network_addresses.mac
mac
read_only_udm.security_result.about.mac
Directly mapped from computer.network_addresses.mac
severity
read_only_udm.security_result.severity
Mapped from severity based on the following logic: - "Medium" -> "MEDIUM" - "High" or "Critical" -> "HIGH" - "Low" -> "LOW" - Otherwise -> "UNKNOWN_SEVERITY"
timestamp
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from timestamp
user
read_only_udm.security_result.about.user.user_display_name
Directly mapped from computer.user
user
read_only_udm.target.user.user_display_name
Directly mapped from computer.user
vulnerabilities.cve
read_only_udm.extensions.vulns.vulnerabilities.cve_id
Directly mapped from vulnerabilities.cve
vulnerabilities.name
read_only_udm.extensions.vulns.vulnerabilities.name
Directly mapped from vulnerabilities.name
vulnerabilities.score
read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score
Directly mapped from vulnerabilities.score after converting to float
vulnerabilities.url
read_only_udm.extensions.vulns.vulnerabilities.vendor_knowledge_base_article_id
Directly mapped from vulnerabilities.url
vulnerabilities.version
read_only_udm.extensions.vulns.vulnerabilities.cvss_version
Directly mapped from vulnerabilities.version
is_alert
Set to true if event_type is one of the following: "Threat Detected", "Exploit Prevention", "Executed malware", "Potential Dropper Infection", "Multiple Infected Files", "Vulnerable Application Detected" or if security_result.severity is "HIGH"
is_significant
Set to true if event_type is one of the following: "Threat Detected", "Exploit Prevention", "Executed malware", "Potential Dropper Infection", "Multiple Infected Files", "Vulnerable Application Detected" or if security_result.severity is "HIGH"
read_only_udm.metadata.event_type
Determined based on event_type and security_result.severity values. - If event_type is one of the following: "Executed malware", "Threat Detected", "Potential Dropper Infection", "Cloud Recall Detection", "Malicious Activity Detection", "Exploit Prevention", "Multiple Infected Files", "Cloud IOC", "System Process Protection", "Vulnerable Application Detected", "Threat Quarantined", "Execution Blocked", "Cloud Recall Quarantine Successful", "Cloud Recall Restore from Quarantine Failed", "Cloud Recall Quarantine Attempt Failed", "Quarantine Failure", then the event type is set to "SCAN_FILE". - If security_result.severity is "HIGH", then the event type is set to "SCAN_FILE". - If both has_principal and has_target are true, then the event type is set to "SCAN_UNCATEGORIZED". - Otherwise, the event type is set to "GENERIC_EVENT".
read_only_udm.metadata.log_type
Set to "CISCO_AMP"
read_only_udm.metadata.vendor_name
Set to "CISCO_AMP"
read_only_udm.security_result.about.file.full_path
Directly mapped from file.file_path
read_only_udm.security_result.about.hostname
Directly mapped from computer.hostname
read_only_udm.security_result.about.user.user_display_name
Directly mapped from computer.user
read_only_udm.security_result.detection_fields.key
Set to "Detection ID" for detection_id, "Error Code" for error.error_code, "Error Description" for error.description, "Parent Disposition" for file.parent.disposition, "Parent File Name" for file.parent.file_name, "Parent MD5" for file.parent.identity.md5, "Parent SHA1" for file.parent.identity.sha1, and "Parent SHA256" for file.parent.identity.sha256
read_only_udm.security_result.summary
Set to event_type if event_type is one of the following: "Threat Detected", "Exploit Prevention", "Executed malware", "Potential Dropper Infection", "Multiple Infected Files", "Vulnerable Application Detected" or if security_result.severity is "HIGH"
read_only_udm.target.asset.ip
Directly mapped from computer.network_addresses.ip
read_only_udm.target.resource.attribute.labels.key
Set to "Parent Disposition" for file.parent.disposition, "Parent File Name" for file.parent.file_name, "Parent MD5" for file.parent.identity.md5, "Parent SHA1" for file.parent.identity.sha1, and "Parent SHA256" for file.parent.identity.sha256
timestamp.seconds
Directly mapped from date after converting to timestamp
Need more help?
Get answers from Community members and Google SecOps professionals.
