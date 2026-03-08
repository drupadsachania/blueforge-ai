# Collect Duo administrator logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-admin/  
**Scraped:** 2026-03-05T09:54:48.868181Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Duo administrator logs
Supported in:
Google secops
SIEM
This document explains how to ingest Duo administrator logs to Google Security Operations using Google Cloud Storage. The parser extracts fields from the logs (JSON format) and maps them to the Unified Data Model (UDM). It handles various Duo action types (login, user management, group management) differently, populating relevant UDM fields based on the action and available data, including user details, authentication factors, and security results. It also performs data transformations, such as merging IP addresses, converting timestamps, and handling errors.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Duo tenant (Admin API application)
Configure Duo Admin API application
Sign in to
Duo Admin Panel
.
Go to
Applications
>
Application Catalog
.
Add
Admin API
application.
Record the following values:
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
(to read administrator logs).
Save the application.
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
duo-admin-logs
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
duo-admin-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Duo administrator logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section:
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
: Enter the service account email.
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
duo-admin-trigger
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
duo-admin-collector
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
duo-admin-trigger
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
duo-admin-collector-sa
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
duo-admin-logs
GCS_PREFIX
duo/admin
STATE_KEY
duo/admin/state.json
DUO_IKEY
DIXYZ...
DUO_SKEY
****************
DUO_API_HOSTNAME
api-XXXXXXXX.duosecurity.com
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
hmac
import
hashlib
import
base64
import
email.utils
import
urllib.parse
import
time
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
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Duo Admin logs and write to GCS.
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
'duo/admin'
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
'duo/admin/state.json'
)
# Duo API credentials
duo_ikey
=
os
.
environ
.
get
(
'DUO_IKEY'
)
duo_skey
=
os
.
environ
.
get
(
'DUO_SKEY'
)
duo_api_hostname
=
os
.
environ
.
get
(
'DUO_API_HOSTNAME'
,
''
)
.
strip
()
if
not
all
([
bucket_name
,
duo_ikey
,
duo_skey
,
duo_api_hostname
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
int
(
time
.
time
())
mintime
=
state
.
get
(
'mintime'
,
now
-
3600
)
print
(
f
'Processing logs since
{
mintime
}
'
)
# Fetch logs from Duo Admin API
page
=
0
total
=
0
next_mintime
=
mintime
max_seen_ts
=
mintime
while
True
:
page_num
=
0
data
=
duo_api_request
(
duo_ikey
,
duo_skey
,
duo_api_hostname
,
'GET'
,
'/admin/v1/logs/administrator'
,
{
'mintime'
:
mintime
}
)
# Write page to GCS
write_page
(
bucket
,
prefix
,
data
,
now
,
page
)
page
+=
1
# Extract items
resp
=
data
.
get
(
'response'
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
(
resp
.
get
(
'items'
)
if
isinstance
(
resp
,
dict
)
else
[])
items
=
items
or
[]
if
not
items
:
break
total
+=
len
(
items
)
# Track the newest timestamp in this batch
for
it
in
items
:
ts
=
epoch_from_item
(
it
)
if
ts
and
ts
>
max_seen_ts
:
max_seen_ts
=
ts
# Duo returns only the 1000 earliest events; page by advancing mintime
if
len
(
items
)
>
=
1000
and
max_seen_ts
>
=
mintime
:
mintime
=
max_seen_ts
next_mintime
=
max_seen_ts
continue
else
:
break
# Save checkpoint: newest seen ts, or "now" if nothing new
if
max_seen_ts
>
next_mintime
:
save_state
(
bucket
,
state_key
,
{
'mintime'
:
max_seen_ts
})
next_state
=
max_seen_ts
else
:
save_state
(
bucket
,
state_key
,
{
'mintime'
:
now
})
next_state
=
now
print
(
f
'Successfully processed
{
total
}
events across
{
page
}
pages, next_mintime:
{
next_state
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
write_page
(
bucket
,
prefix
,
payload
,
when
,
page
):
"""Write a page of logs to GCS."""
try
:
timestamp_str
=
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
when
))
key
=
f
"
{
prefix
}
/
{
timestamp_str
}
/duo-admin-
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
','
,
':'
)),
content_type
=
'application/json'
)
print
(
f
'Wrote page
{
page
}
to
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
'Error writing page
{
page
}
:
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
canon_params
(
params
):
"""Canonicalize parameters for Duo API signature."""
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
sign_request
(
method
,
host
,
path
,
params
,
ikey
,
skey
):
"""Sign Duo API request."""
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
canon_params
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
skey
.
encode
(
'utf-8'
),
canon
.
encode
(
'utf-8'
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
ikey
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
'Date'
:
now
,
'Authorization'
:
f
'Basic
{
auth
}
'
}
def
duo_api_request
(
ikey
,
skey
,
host
,
method
,
path
,
params
,
timeout
=
60
,
max_retries
=
5
):
"""Make a signed request to Duo Admin API with retry logic."""
assert
host
.
startswith
(
'api-'
)
and
host
.
endswith
(
'.duosecurity.com'
),
\
"DUO_API_HOSTNAME must be like api-XXXXXXXX.duosecurity.com"
qs
=
canon_params
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
=
0
backoff
=
1.0
while
True
:
headers
=
sign_request
(
method
,
host
,
path
,
params
,
ikey
,
skey
)
headers
[
'Accept'
]
=
'application/json'
try
:
response
=
http
.
request
(
method
.
upper
(),
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
except
urllib3
.
exceptions
.
HTTPError
as
e
:
# Retry on 429 or 5xx
if
hasattr
(
e
,
'status'
)
and
(
e
.
status
==
429
or
500
<
=
e
.
status
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
Exception
as
e
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
epoch_from_item
(
item
):
"""Extract epoch timestamp from log item."""
# Prefer numeric 'timestamp' (seconds); fallback to ISO8601 'ts'
ts_num
=
item
.
get
(
'timestamp'
)
if
isinstance
(
ts_num
,
(
int
,
float
)):
return
int
(
ts_num
)
ts_iso
=
item
.
get
(
'ts'
)
if
isinstance
(
ts_iso
,
str
):
try
:
# Accept "...Z" or with offset
return
int
(
datetime
.
fromisoformat
(
ts_iso
.
replace
(
'Z'
,
'+00:00'
))
.
timestamp
())
except
Exception
:
return
None
return
None
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
duo-admin-collector-hourly
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
duo-admin-trigger
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
duo-admin-collector
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
Duo Administrator Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Administrator Logs
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
Configure a feed in Google SecOps to ingest Duo Administrator Logs
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
Duo Administrator Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Administrator Logs
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://duo-admin-logs/duo/admin/
Replace:
duo-admin-logs
: Your GCS bucket name.
duo/admin
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/duo-logs/
With subfolder:
gs://company-logs/duo/admin/
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
The value of the action field from the raw log.
desc
metadata.description
The value of the desc field from the raw log's description object.
description._status
target.group.attribute.labels.value
The value of the _status field within the description object from the raw log, specifically when processing group-related actions. This value is placed within a "labels" array with a corresponding "key" of "status".
description.desc
metadata.description
The value of the desc field from the raw log's description object.
description.email
target.user.email_addresses
The value of the email field from the raw log's description object.
description.error
security_result.summary
The value of the error field from the raw log's description object.
description.factor
extensions.auth.auth_details
The value of the factor field from the raw log's description object.
description.groups.0._status
target.group.attribute.labels.value
The value of the _status field from the first element in the groups array within the raw log's description object. This value is placed within a "labels" array with a corresponding "key" of "status".
description.groups.0.name
target.group.group_display_name
The value of the name field from the first element in the groups array within the raw log's description object.
description.ip_address
principal.ip
The value of the ip_address field from the raw log's description object.
description.name
target.group.group_display_name
The value of the name field from the raw log's description object.
description.realname
target.user.user_display_name
The value of the realname field from the raw log's description object.
description.status
target.user.attribute.labels.value
The value of the status field from the raw log's description object. This value is placed within a "labels" array with a corresponding "key" of "status".
description.uname
target.user.email_addresses or target.user.userid
The value of the uname field from the raw log's description object. If it matches an email address format, it's mapped to email_addresses; otherwise, it's mapped to userid.
host
principal.hostname
The value of the host field from the raw log.
isotimestamp
metadata.event_timestamp.seconds
The value of the isotimestamp field from the raw log, converted to epoch seconds.
object
target.group.group_display_name
The value of the object field from the raw log.
timestamp
metadata.event_timestamp.seconds
The value of the timestamp field from the raw log.
username
target.user.userid or principal.user.userid
If the action field contains "login", the value is mapped to target.user.userid. Otherwise, it's mapped to principal.user.userid.
-
extensions.auth.mechanism
Set to "USERNAME_PASSWORD" if the action field contains "login".
-
metadata.event_type
Determined by the parser based on the action field. Possible values: USER_LOGIN, GROUP_CREATION, USER_UNCATEGORIZED, GROUP_DELETION, USER_CREATION, GROUP_MODIFICATION, GENERIC_EVENT.
-
metadata.product_name
Always set to "DUO_ADMIN".
-
metadata.product_version
Always set to "MULTI-FACTOR_AUTHENTICATION".
-
metadata.vendor_name
Always set to "DUO_SECURITY".
-
principal.user.user_role
Set to "ADMINISTRATOR" if the eventtype field contains "admin".
-
security_result.action
Determined by the parser based on the action field. Set to "BLOCK" if the action field contains "error"; otherwise, set to "ALLOW".
-
target.group.attribute.labels.key
Always set to "status" when populating target.group.attribute.labels.
-
target.user.attribute.labels.key
Always set to "status" when populating target.user.attribute.labels.
Need more help?
Get answers from Community members and Google SecOps professionals.
