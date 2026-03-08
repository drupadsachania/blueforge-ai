# Collect ESET Threat Intelligence logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-ioc/  
**Scraped:** 2026-03-05T09:23:52.116856Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ESET Threat Intelligence logs
Supported in:
Google secops
SIEM
This document explains how to ingest ESET Threat Intelligence logs into Google Security Operations using Google Cloud Storage V2, a Cloud Run function, and Cloud Scheduler.
ESET Threat Intelligence (ETI) provides evidence-based information and actionable advice about existing or emerging threats. ETI services warn you about malicious software or activity that might threaten your organization or its customers. The service delivers threat intelligence data through TAXII 2.1 feeds in STIX 2.1 format, including APT IoC, botnet C&C and targets, malicious domains, IPs, URLs, files, phishing URLs, ransomware, and Android threats.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Google Cloud project with the following APIs enabled:
Cloud Storage API
Cloud Run functions API
Cloud Scheduler API
Cloud Pub/Sub API
Permissions to create and manage Google Cloud Storage buckets, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Permissions to manage IAM policies on Google Cloud Storage buckets
An active ESET Threat Intelligence subscription
Access to the ESET Threat Intelligence portal at https://eti.eset.com
Create a Google Cloud Storage bucket
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
eset-ti-logs
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
Collect ESET Threat Intelligence TAXII credentials
To enable the Cloud Run function to retrieve threat intelligence data, you need to activate TAXII feeds and generate TAXII credentials from the ETI portal.
Activate TAXII feeds
Sign in to the
ESET Threat Intelligence portal
at https://eti.eset.com.
Go to
Data Feeds
in the main menu.
Click the
three dots
icon next to the data feed you want to activate.
Select
Enable feed
.
Repeat steps 3-4 for each feed you want to ingest into Google SecOps.
Generate TAXII credentials
In the ESET Threat Intelligence portal, go to
Admin Settings
>
Access Credentials
.
Click
Generate TAXII Credentials
.
In the dialog that appears, copy and save the following values:
Username
: Your TAXII username
Password
: Your TAXII password
Record TAXII feed details
After activating feeds and generating credentials, record the following information for each feed you want to ingest:
In the ESET Threat Intelligence portal, go to
Data Feeds
.
Click the
three dots
icon next to an activated feed.
Select
Show Data Feed detail
.
In the side panel, note the following values:
TAXII feed name
: The feed identifier (for example,
botnet stix 2.1
)
TAXII 2 ID
: The collection ID (for example,
0abb06690b0b47e49cd7794396b76b20
)
TAXII 2 feed URL
: The full collection URL
Available TAXII feeds
ESET Threat Intelligence provides the following TAXII 2.1 feeds:
Feed Name
TAXII Feed Name
Collection ID
Android infostealer feed
androidinfostealer stix 2.1
9ee501cde0c44d6db4ae995fead1a7c8
Android threats feed
androidthreats stix 2.1
daf3de8fab144552a1cb5af054ed07ee
APT IoC
apt stix 2.1
97e3eb74ae5f46dd9e22f677a6938ee7
Botnet feed
botnet stix 2.1
0abb06690b0b47e49cd7794396b76b20
Botnet - C&C
botnet.cc stix 2.1
d1923a526e8f400dbb301259240ee3d5
Botnet - Target
botnet.target stix 2.1
61b6e4f9153e411ca7a9982a2c6ae788
Cryptoscam feed
cryptoscam stix 2.1
2c183ce9551a43338c6cc2ed7c2a704d
Domain feed
domain stix 2.1
a34aa0a4f9de419582a883863503f9c4
eCrime IoC feed
ecrime stix 2.1
08059376eac84ec4a076cfd682493f91
IP feed
ip stix 2.1
baaed2a92335418aa753fe944e13c23a
Malicious email attachments
emailattachments stix 2.1
c0d56cf7f81d482eb97fd46beaa4bae0
Malicious files feed
file stix 2.1
ee6a153ed77e4ec3ab21e76cc2074b9f
Phishing URL feed
phishingurl stix 2.1
d0a6c0f962dd4dd2b3eeb96b18612584
PUA adware files feed
puaadware stix 2.1
d1bfc81202fc4c6599326771ec2da41d
PUA dual-use app files feed
puadualapps stix 2.1
970a7d0039ac4668addf058cd9feb953
Ransomware feed
ransomware stix 2.1
8d3490d688ce4a989aee9af5c680d8bf
Scam URL feed
scamurl stix 2.1
2130adc3c67c43f9a3664b187931375e
Smishing feed
smishing stix 2.1
330ad7d0c736476babe5e49077b96c95
SMS scam feed
smsscam stix 2.1
6e20217a2e1246b8ab11be29f759f716
URL feed
url stix 2.1
1d3208c143be49da8130f5a66fd3a0fa
Create service account for the Cloud Run function
In the
Google Cloud console
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
eset-ti-collector
Service account description
: Enter
Service account for ESET Threat Intelligence Cloud Run function to write STIX objects to GCS
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
Click
Select a role
and search for and select
Storage Object Admin
.
Click
Add Another Role
and search for and select
Cloud Run Invoker
.
Click
Continue
.
Click
Done
.
Grant IAM permissions on the Google Cloud Storage bucket
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name (for example,
eset-ti-logs
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
eset-ti-collector@PROJECT_ID.iam.gserviceaccount.com
)
Assign roles
: Select
Storage Object Admin
Click
Save
.
Create Pub/Sub topic
The Pub/Sub topic triggers the Cloud Run function when a message is published by Cloud Scheduler.
In the
Google Cloud console
, go to
Pub/Sub
>
Topics
.
Click
Create Topic
.
Provide the following configuration details:
Topic ID
: Enter
eset-ti-trigger
Add a default subscription
: Leave selected
Click
Create
.
Create the Cloud Run function
In the
Google Cloud console
, go to
Cloud Run functions
.
Click
Create function
.
Provide the following configuration details:
Setting
Value
Environment
2nd gen
Function name
eset-ti-collector
Region
Select the same region as your GCS bucket
Trigger type
Cloud Pub/Sub
Pub/Sub topic
eset-ti-trigger
Memory allocated
512 MiB
Timeout
540 seconds
Runtime service account
eset-ti-collector
Click
Next
.
Set
Runtime
to
Python 3.12
.
Set
Entry point
to
main
.
In the
requirements.txt
file, add the following dependencies:
functions-framework==3.*
google-cloud-storage==2.*
urllib3==2.*
In the
main.py
file, paste the following code:
import
functions_framework
import
json
import
os
import
logging
import
time
import
urllib3
from
datetime
import
datetime
,
timedelta
,
timezone
from
google.cloud
import
storage
logger
=
logging
.
getLogger
(
__name__
)
logger
.
setLevel
(
logging
.
INFO
)
HTTP
=
urllib3
.
PoolManager
(
retries
=
False
)
storage_client
=
storage
.
Client
()
API_ROOT
=
"https://taxii.eset.com/taxii2/643f4eb5-f8b7-46a3-a606-6d61d5ce223a"
TAXII_CONTENT_TYPE
=
"application/taxii+json;version=2.1"
def
_load_state
(
bucket_name
:
str
,
state_key
:
str
,
lookback_hours
:
int
)
-
>
str
:
"""Return ISO8601 checkpoint (UTC)."""
try
:
bucket
=
storage_client
.
bucket
(
bucket_name
)
blob
=
bucket
.
blob
(
state_key
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
state
=
json
.
loads
(
state_data
)
ts
=
state
.
get
(
"last_poll_time"
)
if
ts
:
logger
.
info
(
f
"Loaded state:
{
ts
}
"
)
return
ts
except
Exception
as
e
:
logger
.
warning
(
f
"State read error:
{
e
}
"
)
default_ts
=
(
datetime
.
now
(
timezone
.
utc
)
-
timedelta
(
hours
=
lookback_hours
)
)
.
strftime
(
"%Y-%m-
%d
T%H:%M:%S.000Z"
)
logger
.
info
(
f
"No previous state found, using lookback:
{
default_ts
}
"
)
return
default_ts
def
_save_state
(
bucket_name
:
str
,
state_key
:
str
,
ts
:
str
)
-
>
None
:
"""Persist the checkpoint to GCS."""
bucket
=
storage_client
.
bucket
(
bucket_name
)
blob
=
bucket
.
blob
(
state_key
)
blob
.
upload_from_string
(
json
.
dumps
({
"last_poll_time"
:
ts
}),
content_type
=
"application/json"
,
)
logger
.
info
(
f
"Saved state:
{
ts
}
"
)
def
_fetch_objects
(
username
:
str
,
password
:
str
,
collection_id
:
str
,
added_after
:
str
,
max_records
:
int
,
)
-
>
list
:
"""Query TAXII 2.1 collection objects with pagination."""
url
=
f
"
{
API_ROOT
}
/collections/
{
collection_id
}
/objects/"
headers
=
urllib3
.
make_headers
(
basic_auth
=
f
"
{
username
}
:
{
password
}
"
)
headers
[
"Accept"
]
=
TAXII_CONTENT_TYPE
headers
[
"User-Agent"
]
=
"Chronicle-ESET-TI-GCS/1.0"
all_objects
=
[]
params
=
{
"added_after"
:
added_after
}
while
True
:
qs
=
"&"
.
join
(
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
.
items
())
request_url
=
f
"
{
url
}
?
{
qs
}
"
if
qs
else
url
for
attempt
in
range
(
3
):
try
:
resp
=
HTTP
.
request
(
"GET"
,
request_url
,
headers
=
headers
)
break
except
Exception
as
e
:
wait
=
2
**
(
attempt
+
1
)
logger
.
warning
(
f
"Request error:
{
e
}
, retrying in
{
wait
}
s"
)
time
.
sleep
(
wait
)
else
:
raise
RuntimeError
(
"Exceeded retry budget for TAXII API"
)
if
resp
.
status
==
401
:
raise
RuntimeError
(
"Authentication failed: check TAXII credentials"
)
if
resp
.
status
==
404
:
raise
RuntimeError
(
f
"Collection not found:
{
collection_id
}
"
)
if
resp
.
status
not
in
(
200
,
206
):
raise
RuntimeError
(
f
"TAXII API error
{
resp
.
status
}
:
{
resp
.
data
[:
500
]
}
"
)
body
=
json
.
loads
(
resp
.
data
.
decode
(
"utf-8"
))
objects
=
body
.
get
(
"objects"
,
[])
all_objects
.
extend
(
objects
)
logger
.
info
(
f
"Fetched
{
len
(
objects
)
}
objects (total:
{
len
(
all_objects
)
}
)"
)
if
len
(
all_objects
)
>
=
max_records
:
logger
.
info
(
f
"Reached max_records limit:
{
max_records
}
"
)
all_objects
=
all_objects
[:
max_records
]
break
more
=
body
.
get
(
"more"
,
False
)
next_param
=
body
.
get
(
"next"
)
if
more
and
next_param
:
params
=
{
"added_after"
:
added_after
,
"next"
:
next_param
}
else
:
break
return
all_objects
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""Cloud Run function entry point triggered by Pub/Sub."""
bucket_name
=
os
.
environ
[
"GCS_BUCKET"
]
prefix
=
os
.
environ
.
get
(
"GCS_PREFIX"
,
"eset-ti"
)
state_key
=
os
.
environ
.
get
(
"STATE_KEY"
,
"eset-ti/state.json"
)
username
=
os
.
environ
[
"TAXII_USERNAME"
]
password
=
os
.
environ
[
"TAXII_PASSWORD"
]
collection_id
=
os
.
environ
[
"COLLECTION_ID"
]
max_records
=
int
(
os
.
environ
.
get
(
"MAX_RECORDS"
,
"10000"
))
lookback_hours
=
int
(
os
.
environ
.
get
(
"LOOKBACK_HOURS"
,
"48"
))
try
:
last_poll
=
_load_state
(
bucket_name
,
state_key
,
lookback_hours
)
objects
=
_fetch_objects
(
username
,
password
,
collection_id
,
last_poll
,
max_records
)
if
not
objects
:
logger
.
info
(
"No new STIX objects found"
)
return
"No new objects"
,
200
now_str
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
"%Y%m
%d
_%H%M%S"
)
blob_path
=
(
f
"
{
prefix
}
/eset_ti_
{
collection_id
}
_
{
now_str
}
.json"
)
ndjson_body
=
"
\n
"
.
join
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
))
for
obj
in
objects
)
bucket
=
storage_client
.
bucket
(
bucket_name
)
blob
=
bucket
.
blob
(
blob_path
)
blob
.
upload_from_string
(
ndjson_body
,
content_type
=
"application/x-ndjson"
)
new_poll_time
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
"%Y-%m-
%d
T%H:%M:%S.000Z"
)
_save_state
(
bucket_name
,
state_key
,
new_poll_time
)
msg
=
(
f
"Wrote
{
len
(
objects
)
}
STIX objects to "
f
"gs://
{
bucket_name
}
/
{
blob_path
}
"
)
logger
.
info
(
msg
)
return
msg
,
200
except
Exception
as
e
:
logger
.
error
(
f
"Error collecting ESET TI:
{
e
}
"
)
raise
Click
Deploy
.
Wait for the function to be deployed. The status changes to a green checkmark when the deployment is complete.
Configure environment variables
After the function is deployed, go to
Cloud Run functions
>
eset-ti-collector
.
Click
Edit and deploy new revision
.
Click the
Variables and Secrets
tab (or expand
Runtime, build, connections and security settings
for 1st gen).
Add the following environment variables:
Key
Example value
GCS_BUCKET
eset-ti-logs
GCS_PREFIX
eset-ti
STATE_KEY
eset-ti/state.json
TAXII_USERNAME
Your TAXII username from the ETI portal
TAXII_PASSWORD
Your TAXII password from the ETI portal
COLLECTION_ID
0abb06690b0b47e49cd7794396b76b20
MAX_RECORDS
10000
LOOKBACK_HOURS
48
Click
Deploy
.
Create Cloud Scheduler job
Cloud Scheduler publishes a message to the Pub/Sub topic on a schedule, triggering the Cloud Run function to poll ESET Threat Intelligence for new STIX objects.
In the
Google Cloud console
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
eset-ti-poll
Region
Select the same region as your function
Frequency
0 */1 * * *
(every hour)
Timezone
Select your timezone (for example,
UTC
)
Click
Continue
.
In the
Configure the execution
section:
Target type
: Select
Pub/Sub
Topic
: Select
eset-ti-trigger
Message body
: Enter
{"poll": true}
Click
Create
.
Verify the Cloud Run function
In
Cloud Scheduler
, locate the
eset-ti-poll
job.
Click
Force Run
to trigger an immediate execution.
Go to
Cloud Run functions
>
eset-ti-collector
>
Logs
.
Verify the function executed successfully by checking for log entries such as:
Fetched 250 objects (total: 250)
Wrote 250 STIX objects to gs://eset-ti-logs/eset-ti/eset_ti_0abb06690b0b47e49cd7794396b76b20_20250115_103000.json
Go to
Cloud Storage
>
Buckets
>
eset-ti-logs
.
Navigate to the
eset-ti/
prefix.
Verify that NDJSON files are being created with STIX objects.
Retrieve the Google SecOps service account and configure the feed
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
ESET Threat Intelligence - Botnet
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
ESET Threat Intelligence
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://eset-ti-logs/eset-ti/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days)
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed (for example,
ESET_IOC
)
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
role on your Google Cloud Storage bucket.
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name (for example,
eset-ti-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email
Assign roles
: Select
Storage Object Viewer
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
when
metadata.event_timestamp
Timestamp when the event occurred
metadata.event_type
Type of event (for example, USER_LOGIN, NETWORK_CONNECTION)
messageid
metadata.id
Unique identifier for the event
protocol
network.ip_protocol
IP protocol (for example, TCP, UDP)
deviceName
principal.hostname
Source hostname
srcAddr
principal.ip
Source IP address of the connection
srcPort
principal.port
Source port number
action
security_result.action
Action taken by the security product (for example, ALLOW, BLOCK)
dstAddr
target.ip
Destination IP address
dstPort
target.port
Destination port number
metadata.product_name
Product name
metadata.vendor_name
Vendor/company name
Need more help?
Get answers from Community members and Google SecOps professionals.
