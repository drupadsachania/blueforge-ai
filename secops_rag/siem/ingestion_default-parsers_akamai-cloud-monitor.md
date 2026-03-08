# Collect Akamai Cloud Monitor logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-cloud-monitor/  
**Scraped:** 2026-03-05T09:18:36.176257Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akamai Cloud Monitor logs
Supported in:
Google secops
SIEM
This document explains how to ingest Akamai Cloud Monitor (Load Balancer, Traffic Shaper, ADC) logs to Google Security Operations using Cloud Storage. Akamai pushes JSON events to your HTTPS endpoint; an API Gateway + Cloud Function receiver writes the events to GCS (JSONL, gz). The parser transforms the JSON logs into UDM. It extracts fields from the JSON payload, performs data type conversions, renames fields to match the UDM schema, and handles specific logic for custom fields and URL construction. It also incorporates error handling and conditional logic based on field presence.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Google Cloud project with Google Cloud enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and API Gateway
Privileged access to Akamai Control Center and Property Manager
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
akamai-cloud-monitor
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
Collect Akamai Cloud Monitor configuration details
You will need the following information from Akamai Control Center:
Property name in Property Manager
Required Cloud Monitor datasets to collect
Optional shared secret token for webhook authentication
Create service account for Cloud Function
The Cloud Function needs a service account with permissions to write to GCS bucket.
Create service account
In the
Google Cloud Console
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
akamai-cloud-monitor-sa
.
Service account description
: Enter
Service account for Cloud Function to collect Akamai Cloud Monitor logs
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
: Enter the service account email (for example,
akamai-cloud-monitor-sa@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create Cloud Function to receive Akamai logs
The Cloud Function receives HTTP POST requests from Akamai Cloud Monitor and writes logs to GCS.
In the
GCP Console
, go to
Cloud Functions
.
Click
Create function
.
Provide the following configuration details:
Setting
Value
Environment
Select
2nd gen
Function name
akamai-cloud-monitor-receiver
Region
Select region matching your GCS bucket (for example,
us-central1
)
In the
Trigger
section:
Trigger type
: Select
HTTPS
.
Authentication
: Select
Allow unauthenticated invocations
(Akamai will send unauthenticated requests).
Click
Save
to save the trigger configuration.
Expand
Runtime, build, connections and security settings
.
In the
Runtime
section:
Memory allocated
: Select
512 MiB
.
Timeout
: Enter
600
seconds (10 minutes).
Runtime service account
: Select the service account (
akamai-cloud-monitor-sa
).
In the
Runtime environment variables
section, click
+ Add variable
for each:
Variable Name
Example Value
GCS_BUCKET
akamai-cloud-monitor
GCS_PREFIX
akamai/cloud-monitor/json
INGEST_TOKEN
random-shared-secret
(optional)
Click
Next
to proceed to the code editor.
In the
Runtime
dropdown, select
Python 3.12
.
Add function code
Enter
main
in
Function entry point
In the inline code editor, create two files:
First file:
main.py:
import
os
import
json
import
gzip
import
io
import
uuid
import
datetime
as
dt
from
google.cloud
import
storage
import
functions_framework
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
"akamai/cloud-monitor/json"
)
.
strip
(
"/"
)
+
"/"
INGEST_TOKEN
=
os
.
environ
.
get
(
"INGEST_TOKEN"
)
# optional shared secret
storage_client
=
storage
.
Client
()
def
_write_jsonl_gz
(
objs
:
list
)
-
>
str
:
"""Write JSON objects to GCS as gzipped JSONL."""
timestamp
=
dt
.
datetime
.
utcnow
()
key
=
f
"
{
timestamp
:
%Y/%m/%d
}
/akamai-cloud-monitor-
{
uuid
.
uuid4
()
}
.json.gz"
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
"w"
)
as
gz
:
for
o
in
objs
:
gz
.
write
((
json
.
dumps
(
o
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
)
.
encode
())
buf
.
seek
(
0
)
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
f
"
{
GCS_PREFIX
}{
key
}
"
)
blob
.
upload_from_file
(
buf
,
content_type
=
"application/json"
,
content_encoding
=
"gzip"
)
return
f
"gs://
{
GCS_BUCKET
}
/
{
GCS_PREFIX
}{
key
}
"
def
_parse_records_from_request
(
request
)
-
>
list
:
"""Parse JSON records from HTTP request body."""
body
=
request
.
get_data
(
as_text
=
True
)
if
not
body
:
return
[]
try
:
data
=
json
.
loads
(
body
)
except
Exception
:
# Accept line-delimited JSON as pass-through
try
:
return
[
json
.
loads
(
line
)
for
line
in
body
.
splitlines
()
if
line
.
strip
()]
except
Exception
:
return
[]
if
isinstance
(
data
,
list
):
return
data
if
isinstance
(
data
,
dict
):
return
[
data
]
return
[]
@functions_framework
.
http
def
main
(
request
):
"""
Cloud Function HTTP handler for Akamai Cloud Monitor logs.
Args:
request: Flask request object
Returns:
Tuple of (response_body, status_code, headers)
"""
# Optional shared-secret verification via query parameter (?token=...)
if
INGEST_TOKEN
:
token
=
request
.
args
.
get
(
"token"
)
if
token
!=
INGEST_TOKEN
:
return
(
"Forbidden"
,
403
)
records
=
_parse_records_from_request
(
request
)
if
not
records
:
return
(
"No content"
,
204
)
try
:
gcs_key
=
_write_jsonl_gz
(
records
)
response
=
{
"ok"
:
True
,
"gcs_key"
:
gcs_key
,
"count"
:
len
(
records
)
}
return
(
json
.
dumps
(
response
),
200
,
{
"Content-Type"
:
"application/json"
})
except
Exception
as
e
:
print
(
f
"Error writing to GCS:
{
str
(
e
)
}
"
)
return
(
f
"Internal server error:
{
str
(
e
)
}
"
,
500
)
Second file:
requirements.txt:
functions-framework==3.*
google-cloud-storage==2.*
Click
Deploy
to deploy the function.
Wait for deployment to complete (2-3 minutes).
After deployment, go to the
Trigger
tab and copy the
Trigger URL
. You will use this URL in the Akamai configuration.
Configure Akamai Cloud Monitor to push logs
Sign in to
Akamai Control Center
.
Open your Property in
Property Manager
.
Click
Add Rule
>
choose Cloud Management
.
Add
Cloud Monitor Instrumentation
and select required
Datasets
.
Add
Cloud Monitor Data Delivery
.
Provide the following configuration details:
Delivery Hostname
: Enter the hostname from your Cloud Function trigger URL (for example,
us-central1-your-project.cloudfunctions.net
).
Delivery URL Path
: Enter the path from your Cloud Function trigger URL plus optional query token:
Without token:
/akamai-cloud-monitor-receiver
With token:
/akamai-cloud-monitor-receiver?token=<INGEST_TOKEN>
Replace
<INGEST_TOKEN>
with the value you set in the Cloud Function environment variables.
Click
Save
.
Click
Activate
to activate the property version.
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
Akamai Cloud Monitor - GCS
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Akamai Cloud Monitor
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
Configure a feed in Google SecOps to ingest Akamai Cloud Monitor logs
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
Akamai Cloud Monitor - GCS
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Akamai Cloud Monitor
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://akamai-cloud-monitor/akamai/cloud-monitor/json/
Replace:
akamai-cloud-monitor
: Your GCS bucket name.
akamai/cloud-monitor/json
: Prefix path where logs are stored (must match
GCS_PREFIX
in Cloud Function).
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
:
akamai.cloud_monitor
Ingestion labels
: Labels are added to all the events from this feed (for example,
source=akamai_cloud_monitor
,
format=json
).
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Supported Akamai Cloud Monitor Sample Logs
JSON:
{
"UA"
:
"-"
,
"accLang"
:
"-"
,
"bytes"
:
"3929"
,
"cacheStatus"
:
"1"
,
"cliIP"
:
"0.0.0.0"
,
"cookie"
:
"-"
,
"cp"
:
"848064"
,
"customField"
:
"-"
,
"dnsLookupTimeMSec"
:
"-"
,
"errorCode"
:
"-"
,
"maxAgeSec"
:
"31536000"
,
"objSize"
:
"3929"
,
"overheadBytes"
:
"240"
,
"proto"
:
"HTTPS"
,
"queryStr"
:
"-"
,
"range"
:
"-"
,
"referer"
:
"-"
,
"reqEndTimeMSec"
:
"4"
,
"reqHost"
:
"www.example.com"
,
"reqId"
:
"1ce83c03"
,
"reqMethod"
:
"GET"
,
"reqPath"
:
"assets/images/placeholder-tagline.png"
,
"reqPort"
:
"443"
,
"reqTimeSec"
:
"1622470405.760"
,
"rspContentLen"
:
"3929"
,
"rspContentType"
:
"image/png"
,
"statusCode"
:
"200"
,
"tlsOverheadTimeMSec"
:
"0"
,
"tlsVersion"
:
"TLSv1.2"
,
"totalBytes"
:
"4599"
,
"transferTimeMSec"
:
"0"
,
"turnAroundTimeMSec"
:
"0"
,
"uncompressedSize"
:
"-"
,
"version"
:
"1"
,
"xForwardedFor"
:
"-"
}
UDM Mapping Table
Log Field
UDM Mapping
Logic
accLang
network.http.user_agent
Directly mapped if not "-" or empty string.
city
principal.location.city
Directly mapped if not "-" or empty string.
cliIP
principal.ip
Directly mapped if not empty string.
country
principal.location.country_or_region
Directly mapped if not "-" or empty string.
cp
additional.fields
Mapped as a key-value pair with key "cp".
customField
about.ip, about.labels, src.ip
Parsed as key-value pairs. Special handling for "eIp" and "pIp" to map to src.ip and about.ip respectively. Other keys are mapped as labels within about.
errorCode
security_result.summary, security_result.severity
If present, sets security_result.severity to "ERROR" and maps the value to security_result.summary.
geo.city
principal.location.city
Directly mapped if city is "-" or empty string.
geo.country
principal.location.country_or_region
Directly mapped if country is "-" or empty string.
geo.lat
principal.location.region_latitude
Directly mapped, converted to float.
geo.long
principal.location.region_longitude
Directly mapped, converted to float.
geo.region
principal.location.state
Directly mapped.
id
metadata.product_log_id
Directly mapped if not empty string.
message.cliIP
principal.ip
Directly mapped if cliIP is empty string.
message.fwdHost
principal.hostname
Directly mapped.
message.reqHost
target.hostname, target.url
Used to construct target.url and extract target.hostname.
message.reqLen
network.sent_bytes
Directly mapped, converted to unsigned integer if totalBytes is empty or "-".
message.reqMethod
network.http.method
Directly mapped if reqMethod is empty string.
message.reqPath
target.url
Appended to target.url.
message.reqPort
target.port
Directly mapped, converted to integer if reqPort is empty string.
message.respLen
network.received_bytes
Directly mapped, converted to unsigned integer.
message.sslVer
network.tls.version
Directly mapped.
message.status
network.http.response_code
Directly mapped, converted to integer if statusCode is empty or "-".
message.UA
network.http.user_agent
Directly mapped if UA is "-" or empty string.
network.asnum
additional.fields
Mapped as a key-value pair with key "asnum".
network.edgeIP
intermediary.ip
Directly mapped.
network.network
additional.fields
Mapped as a key-value pair with key "network".
network.networkType
additional.fields
Mapped as a key-value pair with key "networkType".
proto
network.application_protocol
Used to determine network.application_protocol.
queryStr
target.url
Appended to target.url if not "-" or empty string.
referer
network.http.referral_url, about.hostname
Directly mapped if not "-". Extracted hostname is mapped to about.hostname.
reqHost
target.hostname, target.url
Used to construct target.url and extract target.hostname.
reqId
metadata.product_log_id, network.session_id
Directly mapped if id is empty string. Also mapped to network.session_id.
reqMethod
network.http.method
Directly mapped if not empty string.
reqPath
target.url
Appended to target.url if not "-".
reqPort
target.port
Directly mapped, converted to integer.
reqTimeSec
metadata.event_timestamp, timestamp
Used to set event timestamp.
start
metadata.event_timestamp, timestamp
Used to set event timestamp if reqTimeSec is empty string.
statusCode
network.http.response_code
Directly mapped, converted to integer if not "-" or empty string.
tlsVersion
network.tls.version
Directly mapped.
totalBytes
network.sent_bytes
Directly mapped, converted to unsigned integer if not empty or "-".
type
metadata.product_event_type
Directly mapped.
UA
network.http.user_agent
Directly mapped if not "-" or empty string.
version
metadata.product_version
Directly mapped.
xForwardedFor
principal.ip
Directly mapped if not "-" or empty string.
(Parser Logic)
metadata.vendor_name
Set to "Akamai".
(Parser Logic)
metadata.product_name
Set to "Cloud Monitor".
(Parser Logic)
metadata.event_type
Set to "NETWORK_HTTP".
(Parser Logic)
metadata.product_version
Set to "2" if version is empty string.
(Parser Logic)
metadata.log_type
Set to "AKAMAI_CLOUD_MONITOR".
(Parser Logic)
network.application_protocol
Determined from proto or message.proto. Set to "HTTPS" if either contains "HTTPS" (case-insensitive), "HTTP" otherwise.
(Parser Logic)
security_result.severity
Set to "INFORMATIONAL" if errorCode is "-" or empty string.
(Parser Logic)
target.url
Constructed from protocol, reqHost (or message.reqHost), reqPath (or message.reqPath), and queryStr.
Need more help?
Get answers from Community members and Google SecOps professionals.
