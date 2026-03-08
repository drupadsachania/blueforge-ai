# Collect Duo entity context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-context/  
**Scraped:** 2026-03-05T09:54:52.024858Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Duo entity context logs
Supported in:
Google secops
SIEM
This document explains how to ingest Duo entity context data to Google Security Operations using Google Cloud Storage. The parser transforms the JSON logs into a unified data model (UDM) by first extracting fields from the raw JSON, then mapping those fields to UDM attributes. It handles various data scenarios, including user and asset information, software details, and security labels, ensuring comprehensive representation within the UDM schema.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to Duo tenant (Admin API application with sufficient administrative privileges to manage applications)
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Configure Duo Admin API application
Sign in to
Duo Admin Panel
.
Go to
Applications
>
Protect an Application
.
Search for
Admin API
and click
Protect
.
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
Grant resource - Read
(to read users, groups, phones, endpoints, tokens, and WebAuthn credentials).
Click
Save
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
duo-context
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
Save the bucket name and region for future reference.
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
duo-entity-context-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Duo entity context data
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
: Write logs to GCS bucket
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
duo-entity-context-sa@PROJECT_ID.iam.gserviceaccount.com
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
duo-entity-context-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect entity context data
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch entity context data from Duo Admin API and writes them to GCS.
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
duo-entity-context-collector
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
duo-entity-context-trigger
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
duo-entity-context-sa
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
duo-context
GCS_PREFIX
duo/context/
DUO_IKEY
DIXYZ...
DUO_SKEY
****************
DUO_API_HOSTNAME
api-XXXXXXXX.duosecurity.com
LIMIT
100
RESOURCES
users,groups,phones,endpoints,tokens,webauthncredentials
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
# Environment variables
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
"duo/context/"
)
# Default resources can be adjusted via ENV
RESOURCES
=
[
r
.
strip
()
for
r
in
os
.
environ
.
get
(
"RESOURCES"
,
"users,groups,phones,endpoints,tokens,webauthncredentials,desktop_authenticators"
)
.
split
(
","
)
if
r
.
strip
()]
# Duo paging: default 100; max varies by endpoint
LIMIT
=
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
"100"
))
# Initialize Storage client
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
"""RFC3986 encoding with '~' unescaped, keys sorted lexicographically."""
if
not
params
:
return
""
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
ks
=
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
safe
=
"~"
)
vs
=
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
safe
=
"~"
)
parts
.
append
(
f
"
{
ks
}
=
{
vs
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
"""Construct Duo Admin API Authorization + Date headers (HMAC-SHA1)."""
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
(
"utf-8"
))
.
decode
(
"utf-8"
)
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
_call
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
"DUO_API_HOSTNAME must be e.g. api-XXXXXXXX.duosecurity.com"
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
method
.
upper
()
==
"GET"
and
qs
else
""
)
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
with
urlopen
(
req
,
timeout
=
60
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
def
_write_json
(
obj
:
dict
,
when
:
float
,
resource
:
str
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
}
/duo-
{
resource
}
-
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
obj
,
separators
=
(
","
,
":"
)),
content_type
=
"application/json"
)
return
key
def
_fetch_resource
(
resource
:
str
)
-
>
dict
:
"""Fetch all pages for a list endpoint using limit/offset + metadata.next_offset."""
path
=
f
"/admin/v1/
{
resource
}
"
offset
=
0
page
=
0
now
=
time
.
time
()
total_items
=
0
while
True
:
params
=
{
"limit"
:
LIMIT
,
"offset"
:
offset
}
data
=
_call
(
"GET"
,
path
,
params
)
_write_json
(
data
,
now
,
resource
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
# most endpoints return a list; if not a list, count as 1 object page
if
isinstance
(
resp
,
list
):
total_items
+=
len
(
resp
)
elif
resp
is
not
None
:
total_items
+=
1
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
next_offset
is
None
:
break
# Duo returns next_offset as int
try
:
offset
=
int
(
next_offset
)
except
Exception
:
break
return
{
"resource"
:
resource
,
"pages"
:
page
,
"objects"
:
total_items
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
Cloud Run function triggered by Pub/Sub to fetch Duo entity context data and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
results
=
[]
for
res
in
RESOURCES
:
print
(
f
"Fetching resource:
{
res
}
"
)
result
=
_fetch_resource
(
res
)
results
.
append
(
result
)
print
(
f
"Completed
{
res
}
:
{
result
[
'pages'
]
}
pages,
{
result
[
'objects'
]
}
objects"
)
print
(
f
"All resources fetched successfully:
{
results
}
"
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
duo-entity-context-hourly
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
duo-entity-context-trigger
)
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose frequency based on data freshness requirements:
Frequency
Cron Expression
Use Case
Every hour
0 * * * *
Standard (recommended)
Every 2 hours
0 */2 * * *
Moderate freshness
Every 6 hours
0 */6 * * *
Low frequency updates
Daily
0 0 * * *
Minimal updates
Test the scheduler job
In the
Cloud Scheduler
console, find your job (
duo-entity-context-hourly
).
Click
Force run
to trigger manually.
Wait a few seconds and go to
Cloud Run
>
Services
>
duo-entity-context-collector
>
Logs
.
Verify the function executed successfully.
Check the GCS bucket to confirm entity context data was written.
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
Duo Entity Context
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Entity context data
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
Configure a feed in Google SecOps to ingest Duo Entity Context data
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
Duo Entity Context
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Duo Entity context data
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://duo-context/duo/context/
Replace:
duo-context
: Your GCS bucket name.
duo/context/
: Prefix/folder path where logs are stored (must match
GCS_PREFIX
environment variable).
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
activated
entity.asset.deployment_status
If 'activated' is false, set to "DECOMISSIONED", otherwise "ACTIVE".
browsers.browser_family
entity.asset.software.name
Extracted from the 'browsers' array in the raw log.
browsers.browser_version
entity.asset.software.version
Extracted from the 'browsers' array in the raw log.
device_name
entity.asset.hostname
Directly mapped from the raw log.
disk_encryption_status
entity.asset.attribute.labels.key: "disk_encryption_status", entity.asset.attribute.labels.value
Directly mapped from the raw log, converted to lowercase.
email
entity.user.email_addresses
Directly mapped from the raw log if it contains "@", otherwise uses 'username' or 'username1' if they contain "@".
encrypted
entity.asset.attribute.labels.key: "Encrypted", entity.asset.attribute.labels.value
Directly mapped from the raw log, converted to lowercase.
epkey
entity.asset.product_object_id
Used as 'product_object_id' if present, otherwise uses 'phone_id' or 'token_id'.
fingerprint
entity.asset.attribute.labels.key: "Finger Print", entity.asset.attribute.labels.value
Directly mapped from the raw log, converted to lowercase.
firewall_status
entity.asset.attribute.labels.key: "firewall_status", entity.asset.attribute.labels.value
Directly mapped from the raw log, converted to lowercase.
hardware_uuid
entity.asset.asset_id
Used as 'asset_id' if present, otherwise uses 'user_id'.
last_seen
entity.asset.last_discover_time
Parsed as an ISO8601 timestamp and mapped.
model
entity.asset.hardware.model
Directly mapped from the raw log.
number
entity.user.phone_numbers
Directly mapped from the raw log.
os_family
entity.asset.platform_software.platform
Mapped to "WINDOWS", "LINUX", or "MAC" based on the value, case-insensitive.
os_version
entity.asset.platform_software.platform_version
Directly mapped from the raw log.
password_status
entity.asset.attribute.labels.key: "password_status", entity.asset.attribute.labels.value
Directly mapped from the raw log, converted to lowercase.
phone_id
entity.asset.product_object_id
Used as 'product_object_id' if 'epkey' is not present, otherwise uses 'token_id'.
security_agents.security_agent
entity.asset.software.name
Extracted from the 'security_agents' array in the raw log.
security_agents.version
entity.asset.software.version
Extracted from the 'security_agents' array in the raw log.
timestamp
entity.metadata.collected_timestamp
Populates the 'collected_timestamp' field within the 'metadata' object.
token_id
entity.asset.product_object_id
Used as 'product_object_id' if 'epkey' and 'phone_id' are not present.
trusted_endpoint
entity.asset.attribute.labels.key: "trusted_endpoint", entity.asset.attribute.labels.value
Directly mapped from the raw log, converted to lowercase.
type
entity.asset.type
If the raw log 'type' contains "mobile" (case-insensitive), set to "MOBILE", otherwise "LAPTOP".
user_id
entity.asset.asset_id
Used as 'asset_id' if 'hardware_uuid' is not present.
users.email
entity.user.email_addresses
Used as 'email_addresses' if it's the first user in the 'users' array and contains "@".
users.username
entity.user.userid
Extracted username before "@" and used as 'userid' if it's the first user in the 'users' array.
entity.metadata.vendor_name
"Duo"
entity.metadata.product_name
"Duo Entity Context Data"
entity.metadata.entity_type
ASSET
entity.relations.entity_type
USER
entity.relations.relationship
OWNS
Need more help?
Get answers from Community members and Google SecOps professionals.
