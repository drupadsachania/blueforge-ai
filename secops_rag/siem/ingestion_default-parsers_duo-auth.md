# Collect Duo authentication logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-auth/  
**Scraped:** 2026-03-05T09:23:33.042711Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Duo authentication logs
Supported in:
Google secops
SIEM
This document explains how to ingest Duo authentication logs to Google Security Operations. The parser extracts the logs from JSON formatted messages. It transforms the raw log data into the Unified Data Model (UDM), mapping fields like user, device, application, location, and authentication details, while also handling various authentication factors and results to categorize security events. The parser also performs data cleaning, type conversion, and error handling to ensure data quality and consistency.
Choose between two collection methods:
Option 1
: Direct ingestion using Third party API
Option 2
: Collect logs using Cloud Run function and Google Cloud Storage
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to the Duo Admin Panel (Owner role required to create Admin API applications)
Privileged access to GCP if using Option 2
Option 1: Ingest Duo authentication logs using Third party API
Collect Duo prerequisites (API credentials)
Sign in to the Duo Admin Panel as an administrator with the
Owner
,
Administrator
or
Application Manager
role.
Go to
Applications
>
Application Catalog
.
Locate the entry for
Admin API
in the catalog.
Click
+ Add
to create the application.
Copy and save in a secure location the following details:
Integration Key
Secret Key
API Hostname
(for example,
api-XXXXXXXX.duosecurity.com
)
Go to the
Permissions
section.
Deselect all permission options except
Grant read log
.
Click
Save Changes
.
Configure a feed in Google SecOps to ingest Duo authentication logs
Go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Duo Authentication Logs
).
Select
Third party API
as the
Source type
.
Select
Duo Auth
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Username
: Enter the Integration key from Duo.
Secret
: Enter the Secret key from Duo.
API Hostname
: Enter your API hostname (for example,
api-XXXXXXXX.duosecurity.com
).
Asset namespace
: Optional. The
asset namespace
.
Ingestion labels
: Optional. The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Option 2: Ingest Duo authentication logs using Google Cloud Storage
Collect Duo Admin API credentials
Sign in to the Duo Admin Panel.
Go to
Applications
>
Application Catalog
.
Locate
Admin API
in the application catalog.
Click
+ Add
to add the Admin API application.
Copy and save the following values:
Integration key
(ikey)
Secret key
(skey)
API hostname
(for example,
api-XXXXXXXX.duosecurity.com
)
In
Permissions
, enable
Grant read log
.
Click
Save Changes
.
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
duo-auth-logs
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
The Cloud Run function needs a service account with permissions to write to GCS bucket.
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
duo-auth-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Duo authentication logs
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
duo-auth-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
duo-auth-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Duo Admin API and writes them to GCS.
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
duo-auth-collector
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
, choose the topic
duo-auth-trigger
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
duo-auth-collector-sa
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
duo-auth-logs
GCS_PREFIX
duo/auth/
STATE_KEY
duo/auth/state.json
DUO_IKEY
DIXYZ...
DUO_SKEY
****************
DUO_API_HOSTNAME
api-XXXXXXXX.duosecurity.com
LIMIT
500
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
#!/usr/bin/env python3
# Cloud Run Function: Pull Duo Admin API v2 Authentication Logs to GCS (raw JSON pages)
# Notes:
# - Duo v2 requires mintime/maxtime in *milliseconds* (13-digit epoch).
# - Pagination via metadata.next_offset ("<millis>,<txid>").
# - We save state (mintime_ms) in ms to resume next run without gaps.
import
functions_framework
from
google.cloud
import
storage
import
os
import
json
import
time
import
hmac
import
hashlib
import
base64
import
email.utils
import
urllib.parse
from
urllib.request
import
Request
,
urlopen
from
urllib.error
import
HTTPError
,
URLError
DUO_IKEY
=
os
.
environ
[
"DUO_IKEY"
]
DUO_SKEY
=
os
.
environ
[
"DUO_SKEY"
]
DUO_API_HOSTNAME
=
os
.
environ
[
"DUO_API_HOSTNAME"
]
.
strip
()
GCS_BUCKET
=
os
.
environ
[
"GCS_BUCKET"
]
GCS_PREFIX
=
os
.
environ
.
get
(
"GCS_PREFIX"
,
"duo/auth/"
)
.
strip
(
"/"
)
STATE_KEY
=
os
.
environ
.
get
(
"STATE_KEY"
,
"duo/auth/state.json"
)
LIMIT
=
min
(
int
(
os
.
environ
.
get
(
"LIMIT"
,
"500"
)),
1000
)
# default 500, max 1000
storage_client
=
storage
.
Client
()
def
_canon_params
(
params
:
dict
)
-
>
str
:
parts
=
[]
for
k
in
sorted
(
params
.
keys
()):
v
=
params
[
k
]
if
v
is
None
:
continue
parts
.
append
(
f
"
{
urllib
.
parse
.
quote
(
str
(
k
),
'~'
)
}
=
{
urllib
.
parse
.
quote
(
str
(
v
),
'~'
)
}
"
)
return
"&"
.
join
(
parts
)
def
_sign
(
method
:
str
,
host
:
str
,
path
:
str
,
params
:
dict
)
-
>
dict
:
now
=
email
.
utils
.
formatdate
()
canon
=
"
\n
"
.
join
([
now
,
method
.
upper
(),
host
.
lower
(),
path
,
_canon_params
(
params
)
])
sig
=
hmac
.
new
(
DUO_SKEY
.
encode
(
"utf-8"
),
canon
.
encode
(
"utf-8"
),
hashlib
.
sha1
)
.
hexdigest
()
auth
=
base64
.
b64encode
(
f
"
{
DUO_IKEY
}
:
{
sig
}
"
.
encode
())
.
decode
()
return
{
"Date"
:
now
,
"Authorization"
:
f
"Basic
{
auth
}
"
}
def
_http
(
method
:
str
,
path
:
str
,
params
:
dict
,
timeout
:
int
=
60
,
max_retries
:
int
=
5
)
-
>
dict
:
host
=
DUO_API_HOSTNAME
assert
host
.
startswith
(
"api-"
)
and
host
.
endswith
(
".duosecurity.com"
),
\
"DUO_API_HOSTNAME must be like api-XXXXXXXX.duosecurity.com"
qs
=
_canon_params
(
params
)
url
=
f
"https://
{
host
}{
path
}
"
+
(
f
"?
{
qs
}
"
if
qs
else
""
)
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
req
=
Request
(
url
,
method
=
method
.
upper
())
req
.
add_header
(
"Accept"
,
"application/json"
)
for
k
,
v
in
_sign
(
method
,
host
,
path
,
params
)
.
items
():
req
.
add_header
(
k
,
v
)
try
:
with
urlopen
(
req
,
timeout
=
timeout
)
as
r
:
return
json
.
loads
(
r
.
read
()
.
decode
(
"utf-8"
))
except
HTTPError
as
e
:
if
(
e
.
code
==
429
or
500
<
=
e
.
code
<
=
599
)
and
attempt
<
max_retries
:
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
except
URLError
:
if
attempt
<
max_retries
:
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
_read_state_ms
()
-
>
int
|
None
:
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
blob
.
download_as_text
()
val
=
json
.
loads
(
state_data
)
.
get
(
"mintime"
)
if
val
is
None
:
return
None
# Backward safety: if seconds were stored, convert to ms
return
int
(
val
)
*
1000
if
len
(
str
(
int
(
val
)))
<
=
10
else
int
(
val
)
except
Exception
:
return
None
def
_write_state_ms
(
mintime_ms
:
int
):
bucket
=
storage_client
.
bucket
(
GCS_BUCKET
)
blob
=
bucket
.
blob
(
STATE_KEY
)
body
=
json
.
dumps
({
"mintime"
:
int
(
mintime_ms
)})
.
encode
(
"utf-8"
)
blob
.
upload_from_string
(
body
,
content_type
=
"application/json"
)
def
_write_page
(
payload
:
dict
,
when_epoch_s
:
int
,
page
:
int
)
-
>
str
:
bucket
=
storage_client
.
bucket
(
GCS_BUCKET
)
key
=
f
"
{
GCS_PREFIX
}
/
{
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
when_epoch_s
))
}
/duo-auth-
{
page
:
05d
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
upload_from_string
(
json
.
dumps
(
payload
,
separators
=
(
","
,
":"
))
.
encode
(
"utf-8"
),
content_type
=
"application/json"
)
return
key
def
fetch_and_store
():
now_s
=
int
(
time
.
time
())
# Duo recommends a ~2-minute delay buffer; use maxtime = now - 120 seconds (in ms)
maxtime_ms
=
(
now_s
-
120
)
*
1000
mintime_ms
=
_read_state_ms
()
or
(
maxtime_ms
-
3600
*
1000
)
# 1 hour on first run
page
=
0
total
=
0
next_offset
=
None
while
True
:
params
=
{
"mintime"
:
mintime_ms
,
"maxtime"
:
maxtime_ms
,
"limit"
:
LIMIT
}
if
next_offset
:
params
[
"next_offset"
]
=
next_offset
data
=
_http
(
"GET"
,
"/admin/v2/logs/authentication"
,
params
)
_write_page
(
data
,
maxtime_ms
//
1000
,
page
)
page
+=
1
resp
=
data
.
get
(
"response"
)
items
=
resp
if
isinstance
(
resp
,
list
)
else
[]
total
+=
len
(
items
)
meta
=
data
.
get
(
"metadata"
)
or
{}
next_offset
=
meta
.
get
(
"next_offset"
)
if
not
next_offset
:
break
# Advance window to maxtime_ms for next run
_write_state_ms
(
maxtime_ms
)
return
{
"ok"
:
True
,
"pages"
:
page
,
"events"
:
total
,
"next_mintime_ms"
:
maxtime_ms
}
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Duo authentication logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
try
:
result
=
fetch_and_store
()
print
(
f
"Successfully processed
{
result
[
'events'
]
}
events in
{
result
[
'pages'
]
}
pages"
)
print
(
f
"Next mintime_ms:
{
result
[
'next_mintime_ms'
]
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
"Error processing logs:
{
str
(
e
)
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
duo-auth-collector-hourly
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
Select the topic
duo-auth-trigger
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
duo-auth-collector
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
Duo Authentication Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Auth
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
Configure a feed in Google SecOps to ingest Duo authentication logs
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
Duo Authentication Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Auth
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://duo-auth-logs/duo/auth/
Replace:
duo-auth-logs
: Your GCS bucket name.
duo/auth/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/duo-logs/
With subfolder:
gs://company-logs/duo/auth/
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
access_device.browser
target.resource.attribute.labels.value
If access_device.browser is present, its value is mapped to the UDM.
access_device.hostname
principal.hostname
If access_device.hostname is present and not empty, its value is mapped to the UDM. If it's empty and the event_type is USER_CREATION, the event_type is changed to USER_UNCATEGORIZED. If access_device.hostname is empty and hostname field exists, the value of hostname is used.
access_device.ip
principal.ip
If access_device.ip exists and is a valid IPv4 address, its value is mapped to the UDM. If it's not a valid IPv4 address, it's added as a string value to additional.fields with key access_device.ip.
access_device.location.city
principal.location.city
If present, the value is mapped to the UDM.
access_device.location.country
principal.location.country_or_region
If present, the value is mapped to the UDM.
access_device.location.state
principal.location.state
If present, the value is mapped to the UDM.
access_device.os
principal.platform
If present, the value is translated to the corresponding UDM value (MAC, WINDOWS, LINUX).
access_device.os_version
principal.platform_version
If present, the value is mapped to the UDM.
application.key
target.resource.id
If present, the value is mapped to the UDM.
application.name
target.application
If present, the value is mapped to the UDM.
auth_device.ip
target.ip
If present and not "None", the value is mapped to the UDM.
auth_device.location.city
target.location.city
If present, the value is mapped to the UDM.
auth_device.location.country
target.location.country_or_region
If present, the value is mapped to the UDM.
auth_device.location.state
target.location.state
If present, the value is mapped to the UDM.
auth_device.name
target.hostname OR target.user.phone_numbers
If auth_device.name is present and is a phone number (after normalization), it's added to target.user.phone_numbers. Otherwise, it's mapped to target.hostname.
client_ip
target.ip
If present and not "None", the value is mapped to the UDM.
client_section
target.resource.attribute.labels.value
If client_section is present, its value is mapped to the UDM with the key client_section.
dn
target.user.userid
If dn is present and user.name and username are not, the userid is extracted from the dn field using grok and mapped to the UDM. The event_type is set to USER_LOGIN.
event_type
metadata.product_event_type AND metadata.event_type
The value is mapped to metadata.product_event_type. It's also used to determine the metadata.event_type: "authentication" becomes USER_LOGIN, "enrollment" becomes USER_CREATION, and if it's empty or neither of those, it becomes GENERIC_EVENT.
factor
extensions.auth.mechanism AND extensions.auth.auth_details
The value is translated to the corresponding UDM auth.mechanism value (HARDWARE_KEY, REMOTE_INTERACTIVE, LOCAL, OTP). The original value is also mapped to extensions.auth.auth_details.
hostname
principal.hostname
If present and access_device.hostname is empty, the value is mapped to the UDM.
log_format
target.resource.attribute.labels.value
If log_format is present, its value is mapped to the UDM with the key log_format.
log
level.
_class
uuid
_
target.resource.attribute.labels.value
If log
level.
_class
uuid
_ is present, its value is mapped to the UDM with the key
class_uuid
.
log_level.name
target.resource.attribute.labels.value AND security_result.severity
If log_level.name is present, its value is mapped to the UDM with the key name. If the value is "info", security_result.severity is set to INFORMATIONAL.
log_logger.unpersistable
target.resource.attribute.labels.value
If log_logger.unpersistable is present, its value is mapped to the UDM with the key unpersistable.
log_namespace
target.resource.attribute.labels.value
If log_namespace is present, its value is mapped to the UDM with the key log_namespace.
log_source
target.resource.attribute.labels.value
If log_source is present, its value is mapped to the UDM with the key log_source.
msg
security_result.summary
If present and reason is empty, the value is mapped to the UDM.
reason
security_result.summary
If present, the value is mapped to the UDM.
result
security_result.action_details AND security_result.action
If present, the value is mapped to security_result.action_details. "success" or "SUCCESS" translates to security_result.action ALLOW, otherwise BLOCK.
server_section
target.resource.attribute.labels.value
If server_section is present, its value is mapped to the UDM with the key server_section.
server_section_ikey
target.resource.attribute.labels.value
If server_section_ikey is present, its value is mapped to the UDM with the key server_section_ikey.
status
security_result.action_details AND security_result.action
If present, the value is mapped to security_result.action_details. "Allow" translates to security_result.action ALLOW, "Reject" translates to BLOCK.
timestamp
metadata.event_timestamp AND event.timestamp
The value is converted to a timestamp and mapped to both metadata.event_timestamp and event.timestamp.
txid
metadata.product_log_id AND network.session_id
The value is mapped to both metadata.product_log_id and network.session_id.
user.groups
target.user.group_identifiers
All values in the array are added to target.user.group_identifiers.
user.key
target.user.product_object_id
If present, the value is mapped to the UDM.
user.name
target.user.userid
If present, the value is mapped to the UDM.
username
target.user.userid
If present and user.name is not, the value is mapped to the UDM. The event_type is set to USER_LOGIN.
(Parser Logic)
metadata.vendor_name
Always set to "DUO_SECURITY".
(Parser Logic)
metadata.product_name
Always set to "MULTI-FACTOR_AUTHENTICATION".
(Parser Logic)
metadata.log_type
Taken from the raw log's top-level log_type field.
(Parser Logic)
extensions.auth.type
Always set to "SSO".
Need more help?
Get answers from Community members and Google SecOps professionals.
