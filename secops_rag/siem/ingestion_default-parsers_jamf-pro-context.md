# Collect Jamf Pro context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context/  
**Scraped:** 2026-03-05T09:25:51.396774Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Jamf Pro context logs
Supported in:
Google secops
SIEM
This document explains how to ingest Jamf Pro context logs (device & user context) to Google Security Operations using Google Cloud Storage with Cloud Run functions, Pub/Sub, and Cloud Scheduler. Jamf Pro is a comprehensive management solution for Apple devices, providing device inventory, user context, and configuration management capabilities.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Jamf Pro tenant
Configure Jamf API Role
Sign in to Jamf web UI.
Go to
Settings
>
System section
>
API Roles and Clients
.
Select the
API Roles
tab.
Click
New
.
Enter a display name for the API role (for example,
context_role
).
In the
Jamf Pro API role privileges
, type the name of a privilege, and then select it from the menu:
Computer Inventory
Mobile Device Inventory
Click
Save
.
Configure Jamf API Client
In Jamf Pro, go to
Settings
>
System section
>
API roles and clients
.
Select the
API Clients
tab.
Click
New
.
Enter a display name for the API client (for example,
context_client
).
In the
API Roles
field, add the
context_role
role you previously created.
Under
Access Token Lifetime
, enter the time in seconds for the access tokens to be valid.
Click
Save
.
Click
Edit
.
Click
Enable API Client
.
Click
Save
.
Configure Jamf Client Secret
In Jamf Pro, go to the newly created API client.
Click
Generate Client Secret
.
In a confirmation screen, click
Create Secret
.
Save the following parameters in a secure location:
Base URL
:
https://<your>.jamfcloud.com
Client ID
: UUID.
Client Secret
: Value is shown once.
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
jamfpro
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
jamf-pro-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Jamf Pro context logs
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
jamf-pro-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
jamf-pro-context-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Jamf Pro API and writes them to GCS.
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
jamf-pro-context-collector
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
jamf-pro-context-trigger
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
jamf-pro-collector-sa
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
jamfpro
GCS_PREFIX
jamf-pro/context/
JAMF_CLIENT_ID
Enter Jamf Client ID
JAMF_CLIENT_SECRET
Enter Jamf Client Secret
JAMF_BASE_URL
Enter Jamf URL, replace
<your>
in
https://<your>.jamfcloud.com
PAGE_SIZE
200
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
gzip
import
io
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
# Configuration
BASE_URL
=
os
.
environ
.
get
(
"JAMF_BASE_URL"
,
""
)
.
rstrip
(
"/"
)
CLIENT_ID
=
os
.
environ
.
get
(
"JAMF_CLIENT_ID"
)
CLIENT_SECRET
=
os
.
environ
.
get
(
"JAMF_CLIENT_SECRET"
)
GCS_BUCKET
=
os
.
environ
.
get
(
"GCS_BUCKET"
)
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
"jamf-pro/context/"
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
"PAGE_SIZE"
,
"200"
))
SECTIONS
=
[
"GENERAL"
,
"HARDWARE"
,
"OPERATING_SYSTEM"
,
"USER_AND_LOCATION"
,
"DISK_ENCRYPTION"
,
"SECURITY"
,
"EXTENSION_ATTRIBUTES"
,
"APPLICATIONS"
,
"CONFIGURATION_PROFILES"
,
"LOCAL_USER_ACCOUNTS"
,
"CERTIFICATES"
,
"SERVICES"
,
"PRINTERS"
,
"SOFTWARE_UPDATES"
,
"GROUP_MEMBERSHIPS"
,
"CONTENT_CACHING"
,
"STORAGE"
,
"FONTS"
,
"PACKAGE_RECEIPTS"
,
"PLUGINS"
,
"ATTACHMENTS"
,
"LICENSED_SOFTWARE"
,
"IBEACONS"
,
"PURCHASING"
]
def
_now_iso
():
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
def
get_token
():
"""OAuth2 client credentials > access_token"""
url
=
f
"
{
BASE_URL
}
/api/oauth/token"
# Encode credentials for form data
fields
=
{
"grant_type"
:
"client_credentials"
,
"client_id"
:
CLIENT_ID
,
"client_secret"
:
CLIENT_SECRET
}
headers
=
{
"Content-Type"
:
"application/x-www-form-urlencoded"
}
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
fields
=
fields
,
headers
=
headers
,
timeout
=
30.0
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
"Failed to get token:
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
return
data
[
"access_token"
],
int
(
data
.
get
(
"expires_in"
,
1200
))
def
fetch_page
(
token
,
page
):
"""GET /api/v1/computers-inventory with sections & pagination"""
url
=
f
"
{
BASE_URL
}
/api/v1/computers-inventory"
# Build query parameters
params
=
[(
"page"
,
str
(
page
)),
(
"page-size"
,
str
(
PAGE_SIZE
))]
params
.
extend
([(
"section"
,
s
)
for
s
in
SECTIONS
])
# Encode parameters
query_string
=
"&"
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
])
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
"Authorization"
:
f
"Bearer
{
token
}
"
,
"Accept"
:
"application/json"
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
,
timeout
=
60.0
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
"Failed to fetch page
{
page
}
:
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
to_context_event
(
item
):
inv
=
item
.
get
(
"inventory"
,
{})
or
{}
general
=
inv
.
get
(
"general"
,
{})
or
{}
hardware
=
inv
.
get
(
"hardware"
,
{})
or
{}
osinfo
=
inv
.
get
(
"operatingSystem"
,
{})
or
{}
loc
=
inv
.
get
(
"location"
,
{})
or
inv
.
get
(
"userAndLocation"
,
{})
or
{}
computer
=
{
"udid"
:
general
.
get
(
"udid"
)
or
hardware
.
get
(
"udid"
),
"deviceName"
:
general
.
get
(
"name"
)
or
general
.
get
(
"deviceName"
),
"serialNumber"
:
hardware
.
get
(
"serialNumber"
)
or
general
.
get
(
"serialNumber"
),
"model"
:
hardware
.
get
(
"model"
)
or
general
.
get
(
"model"
),
"osVersion"
:
osinfo
.
get
(
"version"
)
or
general
.
get
(
"osVersion"
),
"osBuild"
:
osinfo
.
get
(
"build"
)
or
general
.
get
(
"osBuild"
),
"macAddress"
:
hardware
.
get
(
"macAddress"
),
"alternateMacAddress"
:
hardware
.
get
(
"wifiMacAddress"
),
"ipAddress"
:
general
.
get
(
"ipAddress"
),
"reportedIpV4Address"
:
general
.
get
(
"reportedIpV4Address"
),
"reportedIpV6Address"
:
general
.
get
(
"reportedIpV6Address"
),
"modelIdentifier"
:
hardware
.
get
(
"modelIdentifier"
),
"assetTag"
:
general
.
get
(
"assetTag"
),
}
user_block
=
{
"userDirectoryID"
:
loc
.
get
(
"username"
)
or
loc
.
get
(
"userDirectoryId"
),
"emailAddress"
:
loc
.
get
(
"emailAddress"
),
"realName"
:
loc
.
get
(
"realName"
),
"phone"
:
loc
.
get
(
"phone"
)
or
loc
.
get
(
"phoneNumber"
),
"position"
:
loc
.
get
(
"position"
),
"department"
:
loc
.
get
(
"department"
),
"building"
:
loc
.
get
(
"building"
),
"room"
:
loc
.
get
(
"room"
),
}
return
{
"webhook"
:
{
"name"
:
"api.inventory"
},
"event_type"
:
"ComputerInventory"
,
"event_action"
:
"snapshot"
,
"event_timestamp"
:
_now_iso
(),
"event_data"
:
{
"computer"
:
{
k
:
v
for
k
,
v
in
computer
.
items
()
if
v
not
in
(
None
,
""
)},
**
{
k
:
v
for
k
,
v
in
user_block
.
items
()
if
v
not
in
(
None
,
""
)}
},
"_jamf"
:
{
"id"
:
item
.
get
(
"id"
),
"inventory"
:
inv
}
}
def
write_ndjson_gz
(
objs
,
when
):
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
filename
=
"-"
,
mode
=
"wb"
,
fileobj
=
buf
,
mtime
=
int
(
time
.
time
()))
as
gz
:
for
obj
in
objs
:
line
=
json
.
dumps
(
obj
,
separators
=
(
","
,
":"
))
+
"
\n
"
gz
.
write
(
line
.
encode
(
"utf-8"
))
buf
.
seek
(
0
)
prefix
=
GCS_PREFIX
.
strip
(
"/"
)
+
"/"
if
GCS_PREFIX
else
""
key
=
f
"
{
prefix
}{
when
:
%Y/%m/%d
}
/jamf_pro_context_
{
int
(
when
.
timestamp
())
}
.ndjson.gz"
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
key
)
blob
.
upload_from_file
(
buf
,
content_type
=
"application/gzip"
)
return
key
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Jamf Pro context logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
BASE_URL
,
CLIENT_ID
,
CLIENT_SECRET
,
GCS_BUCKET
]):
print
(
"Error: Missing required environment variables"
)
return
try
:
token
,
_ttl
=
get_token
()
page
=
0
total
=
0
batch
=
[]
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
while
True
:
payload
=
fetch_page
(
token
,
page
)
results
=
payload
.
get
(
"results"
)
or
[]
if
not
results
:
break
for
item
in
results
:
batch
.
append
(
to_context_event
(
item
))
total
+=
1
if
len
(
batch
)
>
=
5000
:
key
=
write_ndjson_gz
(
batch
,
now
)
print
(
f
"Wrote
{
len
(
batch
)
}
records to gs://
{
GCS_BUCKET
}
/
{
key
}
"
)
batch
=
[]
if
len
(
results
)
<
PAGE_SIZE
:
break
page
+=
1
if
batch
:
key
=
write_ndjson_gz
(
batch
,
now
)
print
(
f
"Wrote
{
len
(
batch
)
}
records to gs://
{
GCS_BUCKET
}
/
{
key
}
"
)
print
(
f
"Successfully processed
{
total
}
total records"
)
except
Exception
as
e
:
print
(
f
"Error processing Jamf Pro context logs:
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
jamfpro-context-schedule-1h
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
jamf-pro-context-trigger
)
Message body
{}
(empty JSON object)
Click
Create
.
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
jamf-pro-context-collector
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
Jamf Pro Context logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Jamf pro context
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
Configure a feed in Google SecOps to ingest Jamf Pro context logs
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
Jamf Pro Context logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Jamf pro context
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://jamfpro/jamf-pro/context/
Replace
jamfpro
with the actual name of the bucket.
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
