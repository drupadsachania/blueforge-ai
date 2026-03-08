# Collect DigiCert audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digicert/  
**Scraped:** 2026-03-05T09:23:21.065246Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect DigiCert audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest DigiCert audit logs to Google Security Operations using Google Cloud Storage. DigiCert CertCentral is a certificate lifecycle management platform that provides audit logs for certificate operations, user activities, and administrative actions.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to DigiCert CertCentral (API key with Administrator role)
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
digicert-logs
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
Collect DigiCert API credentials
Get DigiCert API key
Sign in to
DigiCert CertCentral
.
Go to
Account
>
API Keys
.
Click
Create API Key
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Chronicle Integration
).
Role
: Select
Administrator
.
Click
Create
.
Copy and save the API key (
X-DC-DEVKEY
). This value will not be shown again.
Get DigiCert Report ID
In
DigiCert CertCentral
, go to
Reports
>
Report Library
.
Click
Create Report
.
Provide the following configuration details:
Report Type
: Select
Audit log
.
Format
: Select
JSON
.
Name
: Enter a descriptive name (for example,
Chronicle Audit Logs
).
Click
Create
.
Copy and save the
Report ID
(UUID format).
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
digicert-logs-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect DigiCert audit logs
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
digicert-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
digicert-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from DigiCert API and writes them to GCS.
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
digicert-audit-logs-collector
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
digicert-audit-trigger
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
digicert-logs-collector-sa
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
digicert-logs
GCS_PREFIX
digicert/logs
STATE_KEY
digicert/logs/state.json
DIGICERT_API_KEY
xxxxxxxxxxxxxxxxxxxxxxxx
DIGICERT_REPORT_ID
88de5e19-ec57-4d70-865d-df953b062574
REQUEST_TIMEOUT
30
POLL_INTERVAL
10
MAX_WAIT_SECONDS
300
Scroll down in the
Variables & Secrets
tab to
Requests
:
Request timeout
: Enter
900
seconds (15 minutes).
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
io
import
gzip
import
zipfile
import
uuid
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
API_BASE
=
"https://api.digicert.com/reports/v1"
USER_AGENT
=
"secops-digicert-reports/1.0"
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch DigiCert audit logs and write to GCS.
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
'digicert/logs'
)
.
rstrip
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
f
'
{
prefix
}
/state.json'
)
api_key
=
os
.
environ
.
get
(
'DIGICERT_API_KEY'
)
report_id
=
os
.
environ
.
get
(
'DIGICERT_REPORT_ID'
)
max_wait
=
int
(
os
.
environ
.
get
(
'MAX_WAIT_SECONDS'
,
'300'
))
poll_int
=
int
(
os
.
environ
.
get
(
'POLL_INTERVAL'
,
'10'
))
timeout
=
int
(
os
.
environ
.
get
(
'REQUEST_TIMEOUT'
,
'30'
))
if
not
all
([
bucket_name
,
api_key
,
report_id
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
# Load state
state
=
load_state
(
bucket
,
state_key
)
last_run
=
state
.
get
(
'last_run_id'
)
# Start report run
started
=
datetime
.
now
(
timezone
.
utc
)
start_report_run
(
api_key
,
report_id
,
timeout
)
# Wait for report to be ready
run_id
=
find_ready_run
(
api_key
,
report_id
,
started
,
timeout
,
max_wait
,
poll_int
)
# Skip if same run as last time
if
last_run
and
last_run
==
run_id
:
print
(
f
'Skipping duplicate run:
{
run_id
}
'
)
return
# Get report data
rows
=
get_json_rows
(
api_key
,
report_id
,
run_id
,
timeout
)
# Write to GCS
key
=
write_ndjson_gz
(
bucket
,
prefix
,
rows
,
run_id
)
# Update state
save_state
(
bucket
,
state_key
,
{
'last_run_id'
:
run_id
,
'last_success_at'
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
'last_s3_key'
:
key
,
'rows_count'
:
len
(
rows
)
})
print
(
f
'Successfully processed
{
len
(
rows
)
}
logs to
{
key
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
http_request
(
method
,
url
,
api_key
,
body
=
None
,
timeout
=
30
,
max_retries
=
5
):
"""Make HTTP request with retry logic."""
headers
=
{
'X-DC-DEVKEY'
:
api_key
,
'Content-Type'
:
'application/json'
,
'User-Agent'
:
USER_AGENT
}
attempt
,
backoff
=
0
,
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
method
,
url
,
headers
=
headers
,
body
=
body
,
timeout
=
timeout
)
status
=
response
.
status
# Retry on server errors
if
500
<
=
status
<
=
599
and
attempt
<
max_retries
:
attempt
+=
1
time
.
sleep
(
backoff
)
backoff
*=
2
continue
# Retry on rate limit
if
status
==
429
and
attempt
<
max_retries
:
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
float
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
backoff
attempt
+=
1
time
.
sleep
(
delay
)
backoff
*=
2
continue
if
status
not
in
(
200
,
201
):
raise
RuntimeError
(
f
'HTTP
{
status
}
:
{
response
.
data
[:
200
]
}
'
)
return
status
,
response
.
headers
,
response
.
data
except
urllib3
.
exceptions
.
HTTPError
as
e
:
if
attempt
<
max_retries
:
attempt
+=
1
time
.
sleep
(
backoff
)
backoff
*=
2
continue
raise
def
start_report_run
(
api_key
,
report_id
,
timeout
):
"""Start a new report run."""
status
,
_
,
body
=
http_request
(
'POST'
,
f
'
{
API_BASE
}
/report/
{
report_id
}
/run'
,
api_key
,
b
'
{}
'
,
timeout
)
if
status
not
in
(
200
,
201
):
raise
RuntimeError
(
f
'Start run failed:
{
status
}
{
body
[:
200
]
}
'
)
def
list_report_history
(
api_key
,
status_filter
=
None
,
report_type
=
None
,
limit
=
100
,
timeout
=
30
):
"""List report history."""
params
=
{
'limit'
:
str
(
limit
),
'offset'
:
'0'
,
'sort_by'
:
'report_start_date'
,
'sort_direction'
:
'DESC'
}
if
status_filter
:
params
[
'status'
]
=
status_filter
if
report_type
:
params
[
'report_type'
]
=
report_type
query_string
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
params
.
items
()])
url
=
f
'
{
API_BASE
}
/report/history?
{
query_string
}
'
status
,
_
,
body
=
http_request
(
'GET'
,
url
,
api_key
,
timeout
=
timeout
)
if
status
!=
200
:
raise
RuntimeError
(
f
'History failed:
{
status
}
{
body
[:
200
]
}
'
)
return
json
.
loads
(
body
.
decode
(
'utf-8'
))
def
find_ready_run
(
api_key
,
report_id
,
started_not_before
,
timeout
,
max_wait_seconds
,
poll_interval
):
"""Find a ready report run."""
deadline
=
time
.
time
()
+
max_wait_seconds
while
time
.
time
()
<
deadline
:
hist
=
list_report_history
(
api_key
,
status_filter
=
'READY'
,
limit
=
200
,
timeout
=
timeout
)
.
get
(
'report_history'
,
[])
for
item
in
hist
:
if
item
.
get
(
'report_identifier'
)
!=
report_id
:
continue
if
not
item
.
get
(
'report_run_identifier'
):
continue
try
:
rsd
=
datetime
.
strptime
(
item
.
get
(
'report_start_date'
,
''
),
'%Y-%m-
%d
%H:%M:%S'
)
.
replace
(
tzinfo
=
timezone
.
utc
)
except
Exception
:
rsd
=
started_not_before
if
rsd
+
timedelta
(
seconds
=
60
)
>
=
started_not_before
:
return
item
[
'report_run_identifier'
]
time
.
sleep
(
poll_interval
)
raise
TimeoutError
(
'READY run not found in time'
)
def
get_json_rows
(
api_key
,
report_id
,
run_id
,
timeout
):
"""Get JSON rows from report."""
status
,
headers
,
body
=
http_request
(
'GET'
,
f
'
{
API_BASE
}
/report/
{
report_id
}
/
{
run_id
}
/json'
,
api_key
,
timeout
=
timeout
)
if
status
!=
200
:
raise
RuntimeError
(
f
'Get JSON failed:
{
status
}
{
body
[:
200
]
}
'
)
# Check if response is ZIP
content_type
=
headers
.
get
(
'content-type'
,
''
)
.
lower
()
if
'application/zip'
in
content_type
or
body
[:
2
]
==
b
'PK'
:
with
zipfile
.
ZipFile
(
io
.
BytesIO
(
body
))
as
zf
:
json_files
=
[
n
for
n
in
zf
.
namelist
()
if
n
.
lower
()
.
endswith
(
'.json'
)]
if
not
json_files
:
raise
RuntimeError
(
'ZIP has no JSON'
)
rows
=
json
.
loads
(
zf
.
read
(
json_files
[
0
])
.
decode
(
'utf-8'
))
else
:
rows
=
json
.
loads
(
body
.
decode
(
'utf-8'
))
if
not
isinstance
(
rows
,
list
):
raise
RuntimeError
(
'Unexpected JSON format'
)
return
rows
def
write_ndjson_gz
(
bucket
,
prefix
,
rows
,
run_id
):
"""Write NDJSON gzipped file to GCS."""
ts
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
key
=
f
'
{
prefix
}
/
{
ts
}
-digicert-audit-
{
run_id
[:
8
]
}
-
{
uuid
.
uuid4
()
.
hex
}
.json.gz'
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
'wb'
)
as
gz
:
for
r
in
rows
:
gz
.
write
((
json
.
dumps
(
r
,
separators
=
(
','
,
':'
))
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
buf
.
getvalue
(),
content_type
=
'application/x-ndjson'
,
content_encoding
=
'gzip'
)
return
key
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
digicert-audit-hourly
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
digicert-audit-trigger
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
digicert-audit-logs-collector
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
DigiCert Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Digicert
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
Configure a feed in Google SecOps to ingest DigiCert logs
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
DigiCert Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Digicert
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://digicert-logs/digicert/logs/
Replace:
digicert-logs
: Your GCS bucket name.
digicert/logs
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
Supported DigiCert sample logs
Audit/activity schema
{
"Account ID"
:
"0000000"
,
"Action"
:
"User SSO login"
,
"Action taken via"
:
"CertCentral"
,
"Activity"
:
"User SSO login #9999999\nLogged through SAML SSO"
,
"Adjustment/Ledger ID"
:
""
,
"Date and time (UTC)"
:
"06-Feb-2025 10:28:04"
,
"Division/Container ID"
:
"111222"
,
"Division/Container name"
:
"Global_Internal_Division"
,
"Domain ID"
:
""
,
"Domain name"
:
""
,
"IP address"
:
"192.168.1.100"
,
"IP country"
:
"US"
,
"Message"
:
"Logged through SAML SSO"
,
"Order ID"
:
""
,
"Order request ID"
:
""
,
"Organization ID"
:
""
,
"Organization name"
:
""
,
"Primary organization name"
:
"Example Corp, Inc."
,
"Result"
:
"Successful"
,
"Revocation comments"
:
""
,
"User ID"
:
"9999999"
,
"User name"
:
"John Doe"
,
"Voucher code ID"
:
""
,
"Voucher order ID"
:
""
}
Domain metadata schema
{
"Domain ID"
:
"8888888"
,
"Domain name"
:
"secure.example.com"
,
"Organization ID"
:
"7777777"
,
"Organization name"
:
"Example Corp, Inc."
,
"DCV email recipients"
:
""
,
"DCV method"
:
"email"
,
"Domain approver email"
:
""
,
"Domain expiration date (UTC)"
:
"18-May-2025 08:36:42"
}
Lifecycle event schema
{
"event"
:
"certificate_issued"
,
"data"
:
{
"order_id"
:
123456789
,
"certificate_id"
:
987654321
}
}
Need more help?
Get answers from Community members and Google SecOps professionals.
