# Collect Cisco vManage SD-WAN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan/  
**Scraped:** 2026-03-05T09:52:50.577448Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco vManage SD-WAN logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco vManage SD-WAN logs to Google Security Operations using Google Cloud Storage. Cisco vManage SD-WAN is a centralized network management system that provides visibility and control over SD-WAN fabric, enabling administrators to monitor network performance, configure policies, and manage security across distributed enterprise networks.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to the Cisco vManage SD-WAN management console
Cisco vManage user account with API access permissions
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
cisco-sdwan-logs-bucket
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
Collect Cisco vManage SD-WAN API credentials
Create API user account
Sign in to the
Cisco vManage Management Console
.
Go to
Administration
>
Settings
>
Users
.
Click
Add User
.
Provide the following configuration details:
Username
: Enter a username for API access (for example,
chronicle-api
).
Password
: Enter a strong password.
Confirm Password
: Re-enter the password.
User Group
: Select a user group with appropriate permissions (see next section).
Click
Add
.
Copy and save in a secure location the following details:
Username
: Your vManage username.
Password
: Your vManage password.
vManage Base URL
: The base URL of your vManage server (for example,
https://your-vmanage-server:8443
).
Configure user permissions
The API user account requires specific permissions to access audit logs, alarms, and events.
In the
Cisco vManage Management Console
, go to
Administration
>
Settings
>
User Groups
.
Select the user group assigned to the API user (or create a new group).
Click
Edit
.
In the
Feature
section, ensure the following permissions are enabled:
Audit Log
: Select
Read
permission.
Alarms
: Select
Read
permission.
Events
: Select
Read
permission.
Click
Update
.
Verify API access
Test your credentials before proceeding with the integration:
Open a terminal or command prompt.
Run the following command to test authentication:
# Replace with your actual credentials
VMANAGE_HOST
=
"https://your-vmanage-server:8443"
VMANAGE_USERNAME
=
"chronicle-api"
VMANAGE_PASSWORD
=
"your-password"
# Test authentication (returns JSESSIONID cookie)
curl
-c
cookies.txt
-X
POST
\
"
${
VMANAGE_HOST
}
/j_security_check"
\
-H
"Content-Type: application/x-www-form-urlencoded"
\
-d
"j_username=
${
VMANAGE_USERNAME
}
&
j_password=
${
VMANAGE_PASSWORD
}
"
# Get CSRF token
curl
-b
cookies.txt
\
"
${
VMANAGE_HOST
}
/dataservice/client/token"
If authentication is successful, the second command will return a CSRF token string.
Note
:
In
production
environments
,
configure
valid
TLS
certificates
on
vManage
and
verify
certificates
in
the
HTTP
client
.
The
code
examples
use
certificate
verification
disabled
for
testing
purposes
only
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
cisco-sdwan-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Cisco vManage SD-WAN logs
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
cisco-sdwan-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
cisco-sdwan-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco vManage SD-WAN API and writes them to GCS.
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
cisco-sdwan-log-collector
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
cisco-sdwan-trigger
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
cisco-sdwan-collector-sa
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
cisco-sdwan-logs-bucket
GCS_PREFIX
cisco-sdwan/
STATE_KEY
cisco-sdwan/state.json
VMANAGE_HOST
https://your-vmanage-server:8443
VMANAGE_USERNAME
chronicle-api
VMANAGE_PASSWORD
your-vmanage-password
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
Scroll down to
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
import
time
# Disable SSL warnings for self-signed certificates (testing only)
urllib3
.
disable_warnings
(
urllib3
.
exceptions
.
InsecureRequestWarning
)
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
10.0
,
read
=
60.0
),
cert_reqs
=
'ssl.CERT_NONE'
,
retries
=
urllib3
.
Retry
(
total
=
3
,
backoff_factor
=
1
)
)
# Environment variables
VMANAGE_HOST
=
os
.
environ
[
'VMANAGE_HOST'
]
VMANAGE_USERNAME
=
os
.
environ
[
'VMANAGE_USERNAME'
]
VMANAGE_PASSWORD
=
os
.
environ
[
'VMANAGE_PASSWORD'
]
GCS_BUCKET
=
os
.
environ
[
'GCS_BUCKET'
]
GCS_PREFIX
=
os
.
environ
[
'GCS_PREFIX'
]
STATE_KEY
=
os
.
environ
[
'STATE_KEY'
]
# Initialize clients
storage_client
=
storage
.
Client
()
class
VManageAPI
:
def
__init__
(
self
,
host
,
username
,
password
):
self
.
host
=
host
.
rstrip
(
'/'
)
self
.
username
=
username
self
.
password
=
password
self
.
cookies
=
None
self
.
token
=
None
def
authenticate
(
self
):
"""Authenticate with vManage and get session tokens"""
try
:
# Login to get JSESSIONID
login_url
=
f
"
{
self
.
host
}
/j_security_check"
# Encode credentials properly
import
urllib.parse
login_data
=
urllib
.
parse
.
urlencode
({
'j_username'
:
self
.
username
,
'j_password'
:
self
.
password
})
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
login_url
,
body
=
login_data
,
headers
=
{
'Content-Type'
:
'application/x-www-form-urlencoded'
},
)
# Check if login was successful
if
b
'<html>'
in
response
.
data
or
response
.
status
!=
200
:
print
(
f
"Authentication failed: HTTP
{
response
.
status
}
"
)
return
False
# Extract cookies
self
.
cookies
=
{}
if
'Set-Cookie'
in
response
.
headers
:
cookie_header
=
response
.
headers
[
'Set-Cookie'
]
for
cookie
in
cookie_header
.
split
(
';'
):
if
'JSESSIONID='
in
cookie
:
self
.
cookies
[
'JSESSIONID'
]
=
cookie
.
split
(
'JSESSIONID='
)[
1
]
.
split
(
';'
)[
0
]
break
if
not
self
.
cookies
.
get
(
'JSESSIONID'
):
print
(
"Failed to get JSESSIONID"
)
return
False
# Get XSRF token
token_url
=
f
"
{
self
.
host
}
/dataservice/client/token"
headers
=
{
'Content-Type'
:
'application/json'
,
'Cookie'
:
f
"JSESSIONID=
{
self
.
cookies
[
'JSESSIONID'
]
}
"
}
response
=
http
.
request
(
'GET'
,
token_url
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
self
.
token
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
"Successfully authenticated with vManage"
)
return
True
else
:
print
(
f
"Failed to get XSRF token: HTTP
{
response
.
status
}
"
)
return
False
except
Exception
as
e
:
print
(
f
"Authentication error:
{
e
}
"
)
return
False
def
get_headers
(
self
):
"""Get headers for API requests"""
return
{
'Content-Type'
:
'application/json'
,
'Cookie'
:
f
"JSESSIONID=
{
self
.
cookies
[
'JSESSIONID'
]
}
"
,
'X-XSRF-TOKEN'
:
self
.
token
}
def
get_audit_logs
(
self
,
last_timestamp
=
None
):
"""Get audit logs from vManage"""
try
:
url
=
f
"
{
self
.
host
}
/dataservice/auditlog"
headers
=
self
.
get_headers
()
query
=
{
"query"
:
{
"condition"
:
"AND"
,
"rules"
:
[]
},
"size"
:
10000
}
if
last_timestamp
:
if
isinstance
(
last_timestamp
,
str
):
try
:
dt
=
datetime
.
fromisoformat
(
last_timestamp
.
replace
(
'Z'
,
'+00:00'
))
epoch_ms
=
int
(
dt
.
timestamp
()
*
1000
)
except
:
epoch_ms
=
int
(
last_timestamp
)
else
:
epoch_ms
=
int
(
last_timestamp
)
query
[
"query"
][
"rules"
]
.
append
({
"value"
:
[
str
(
epoch_ms
)],
"field"
:
"entry_time"
,
"type"
:
"date"
,
"operator"
:
"greater"
})
else
:
query
[
"query"
][
"rules"
]
.
append
({
"value"
:
[
"1"
],
"field"
:
"entry_time"
,
"type"
:
"date"
,
"operator"
:
"last_n_hours"
})
response
=
http
.
request
(
'POST'
,
url
,
body
=
json
.
dumps
(
query
),
headers
=
headers
,
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
else
:
print
(
f
"Failed to get audit logs: HTTP
{
response
.
status
}
"
)
return
None
except
Exception
as
e
:
print
(
f
"Error getting audit logs:
{
e
}
"
)
return
None
def
get_alarms
(
self
,
last_timestamp
=
None
):
"""Get alarms from vManage"""
try
:
url
=
f
"
{
self
.
host
}
/dataservice/alarms"
headers
=
self
.
get_headers
()
query
=
{
"query"
:
{
"condition"
:
"AND"
,
"rules"
:
[]
},
"size"
:
10000
}
if
last_timestamp
:
if
isinstance
(
last_timestamp
,
str
):
try
:
dt
=
datetime
.
fromisoformat
(
last_timestamp
.
replace
(
'Z'
,
'+00:00'
))
epoch_ms
=
int
(
dt
.
timestamp
()
*
1000
)
except
:
epoch_ms
=
int
(
last_timestamp
)
else
:
epoch_ms
=
int
(
last_timestamp
)
query
[
"query"
][
"rules"
]
.
append
({
"value"
:
[
str
(
epoch_ms
)],
"field"
:
"entry_time"
,
"type"
:
"date"
,
"operator"
:
"greater"
})
else
:
query
[
"query"
][
"rules"
]
.
append
({
"value"
:
[
"1"
],
"field"
:
"entry_time"
,
"type"
:
"date"
,
"operator"
:
"last_n_hours"
})
response
=
http
.
request
(
'POST'
,
url
,
body
=
json
.
dumps
(
query
),
headers
=
headers
,
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
else
:
print
(
f
"Failed to get alarms: HTTP
{
response
.
status
}
"
)
return
None
except
Exception
as
e
:
print
(
f
"Error getting alarms:
{
e
}
"
)
return
None
def
get_events
(
self
,
last_timestamp
=
None
):
"""Get events from vManage"""
try
:
url
=
f
"
{
self
.
host
}
/dataservice/events"
headers
=
self
.
get_headers
()
query
=
{
"query"
:
{
"condition"
:
"AND"
,
"rules"
:
[]
},
"size"
:
10000
}
if
last_timestamp
:
if
isinstance
(
last_timestamp
,
str
):
try
:
dt
=
datetime
.
fromisoformat
(
last_timestamp
.
replace
(
'Z'
,
'+00:00'
))
epoch_ms
=
int
(
dt
.
timestamp
()
*
1000
)
except
:
epoch_ms
=
int
(
last_timestamp
)
else
:
epoch_ms
=
int
(
last_timestamp
)
query
[
"query"
][
"rules"
]
.
append
({
"value"
:
[
str
(
epoch_ms
)],
"field"
:
"entry_time"
,
"type"
:
"date"
,
"operator"
:
"greater"
})
else
:
query
[
"query"
][
"rules"
]
.
append
({
"value"
:
[
"1"
],
"field"
:
"entry_time"
,
"type"
:
"date"
,
"operator"
:
"last_n_hours"
})
response
=
http
.
request
(
'POST'
,
url
,
body
=
json
.
dumps
(
query
),
headers
=
headers
,
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
else
:
print
(
f
"Failed to get events: HTTP
{
response
.
status
}
"
)
return
None
except
Exception
as
e
:
print
(
f
"Error getting events:
{
e
}
"
)
return
None
def
get_last_run_time
(
bucket
):
"""Get the last successful run timestamp from GCS"""
try
:
blob
=
bucket
.
blob
(
STATE_KEY
)
if
blob
.
exists
():
state_data
=
json
.
loads
(
blob
.
download_as_text
())
return
state_data
.
get
(
'last_run_time'
)
except
Exception
as
e
:
print
(
f
"Error reading state:
{
e
}
"
)
print
(
"No previous state found, collecting last hour of logs"
)
return
None
def
update_last_run_time
(
bucket
,
timestamp
):
"""Update the last successful run timestamp in GCS"""
try
:
state_data
=
{
'last_run_time'
:
timestamp
,
'updated_at'
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
()
}
blob
=
bucket
.
blob
(
STATE_KEY
)
blob
.
upload_from_string
(
json
.
dumps
(
state_data
),
content_type
=
'application/json'
)
print
(
f
"Updated state with timestamp:
{
timestamp
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
"Error updating state:
{
e
}
"
)
def
upload_logs_to_gcs
(
bucket
,
logs_data
,
log_type
,
timestamp
):
"""Upload logs to GCS bucket"""
try
:
if
not
logs_data
or
'data'
not
in
logs_data
or
not
logs_data
[
'data'
]:
print
(
f
"No
{
log_type
}
data to upload"
)
return
dt
=
datetime
.
now
(
timezone
.
utc
)
filename
=
f
"
{
GCS_PREFIX
}{
log_type
}
/
{
dt
.
strftime
(
'%Y/%m/
%d
'
)
}
/
{
log_type
}
_
{
dt
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
filename
)
blob
.
upload_from_string
(
json
.
dumps
(
logs_data
),
content_type
=
'application/json'
)
print
(
f
"Uploaded
{
len
(
logs_data
[
'data'
])
}
{
log_type
}
records to gs://
{
GCS_BUCKET
}
/
{
filename
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
"Error uploading
{
log_type
}
to GCS:
{
e
}
"
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
Cloud Run function triggered by Pub/Sub to fetch logs from Cisco vManage API and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
print
(
f
"Starting Cisco vManage log collection at
{
datetime
.
now
(
timezone
.
utc
)
}
"
)
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
# Get last run time
last_run_time
=
get_last_run_time
(
bucket
)
# Initialize vManage API client
vmanage
=
VManageAPI
(
VMANAGE_HOST
,
VMANAGE_USERNAME
,
VMANAGE_PASSWORD
)
# Authenticate
if
not
vmanage
.
authenticate
():
print
(
'Failed to authenticate with vManage'
)
return
# Current timestamp for state tracking (store as epoch milliseconds)
current_time
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
()
*
1000
)
# Collect different types of logs
log_types
=
[
(
'audit_logs'
,
vmanage
.
get_audit_logs
),
(
'alarms'
,
vmanage
.
get_alarms
),
(
'events'
,
vmanage
.
get_events
)
]
total_records
=
0
for
log_type
,
get_function
in
log_types
:
try
:
print
(
f
"Collecting
{
log_type
}
..."
)
logs_data
=
get_function
(
last_run_time
)
if
logs_data
:
upload_logs_to_gcs
(
bucket
,
logs_data
,
log_type
,
current_time
)
if
'data'
in
logs_data
:
total_records
+=
len
(
logs_data
[
'data'
])
except
Exception
as
e
:
print
(
f
"Error processing
{
log_type
}
:
{
e
}
"
)
continue
# Update state with current timestamp
update_last_run_time
(
bucket
,
current_time
)
print
(
f
"Collection completed. Total records processed:
{
total_records
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
"Function execution error:
{
e
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
cisco-sdwan-log-collector-hourly
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
cisco-sdwan-trigger
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
cisco-sdwan-log-collector
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
Cisco SD-WAN logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cisco vManage SD-WAN
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
Configure a feed in Google SecOps to ingest Cisco vManage SD-WAN logs
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
Cisco SD-WAN logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cisco vManage SD-WAN
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://cisco-sdwan-logs-bucket/cisco-sdwan/
Replace:
cisco-sdwan-logs-bucket
: Your GCS bucket name.
cisco-sdwan/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/cisco-sdwan/
With subfolder:
gs://company-logs/cisco-sdwan/audit_logs/
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
Need more help?
Get answers from Community members and Google SecOps professionals.
