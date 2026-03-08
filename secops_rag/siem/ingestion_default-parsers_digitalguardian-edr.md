# Collect Digital Guardian EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr/  
**Scraped:** 2026-03-05T09:23:23.299270Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Digital Guardian EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest Digital Guardian EDR logs into Google Security Operations using Google Cloud Storage V2 via a Cloud Run function.
Fortra's Digital Guardian (formerly Digital Guardian) is a comprehensive data loss prevention and endpoint detection and response platform that provides visibility into system, user, and data events across endpoints, networks, and cloud applications. The Analytics & Reporting Cloud (ARC) service delivers advanced analytics, workflow, and reporting capabilities for holistic data protection. The Cloud Run function authenticates to the ARC Export API using OAuth 2.0, retrieves export data, acknowledges the bookmark to advance to the next chunk, writes the results as NDJSON to a GCS bucket, and Google SecOps ingests them through a GCS V2 feed.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Google Cloud project with the following APIs enabled:
Cloud Storage
Cloud Run functions
Cloud Scheduler
Pub/Sub
Cloud Build
Permissions to create and manage Cloud Storage buckets, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to the Digital Guardian Management Console (DGMC)
Access to Digital Guardian Analytics & Reporting Cloud (ARC) Tenant Settings
Administrator permissions to configure Cloud Services in DGMC
An Export Profile created in DGMC with a valid GUID
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
digitalguardian-edr-logs
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location closest to your Google SecOps instance (for example,
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
Collect Digital Guardian API credentials
To enable the Cloud Run function to retrieve export data from the Digital Guardian ARC, you need to obtain API credentials and configure an export profile.
Obtain API credentials from DGMC
Sign in to the
Digital Guardian Management Console (DGMC)
.
Go to
System
>
Configuration
>
Cloud Services
.
In the
API Access
section, locate and record the following values:
API Access ID
: This is your Client ID for OAuth 2.0 authentication.
API Access Secret
: This is your Client Secret for OAuth 2.0 authentication.
Access Gateway Base URL
: The API gateway endpoint (for example,
https://accessgw-usw.msp.digitalguardian.com
).
Authorization Server URL
: The OAuth 2.0 token endpoint (for example,
https://authsrv.msp.digitalguardian.com/as/token.oauth2
).
Create and configure an export profile
In the
Digital Guardian Management Console (DGMC)
, go to
Admin
>
Reports
>
Export Profiles
.
Click
Create Export Profile
or select an existing export profile.
Configure the export profile with the following settings:
Profile Name
: Enter a descriptive name (for example,
Google SecOps SIEM Integration
).
Data Source
: Select
Events
or
Alerts
depending on the data you want to export.
Export Format
: Select
JSON Flattened Table
(recommended for SIEM integrations).
Fields
: Select the fields you want to include in the export.
Filters
: Configure any filters to limit the data exported (optional).
Click
Save
to create the export profile.
After saving, locate the export profile in the list and copy the
GUID
from the export profile URL or details page.
Record credentials summary
Save the following information for configuring the Cloud Run function environment variables:
Client ID (API Access ID)
: From DGMC Cloud Services
Client Secret (API Access Secret)
: From DGMC Cloud Services
Authorization Server URL
: For example,
https://authsrv.msp.digitalguardian.com/as/token.oauth2
Access Gateway Base URL
: For example,
https://accessgw-usw.msp.digitalguardian.com
Export Profile GUID
: From the export profile created in DGMC
Test API access
Verify that your credentials are valid by running the following commands:
# Step 1: Obtain OAuth 2.0 access token
curl
-s
-X
POST
\
-d
"grant_type=client_credentials&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&scope=client"
\
"https://authsrv.msp.digitalguardian.com/as/token.oauth2"
# Step 2: Test export endpoint with the access token
curl
-s
-H
"Authorization: Bearer YOUR_ACCESS_TOKEN"
\
"https://accessgw-usw.msp.digitalguardian.com/rest/1.0/export/YOUR_EXPORT_PROFILE_GUID"
A successful response returns a JSON document containing export data. If you receive an authentication error, verify the API Access ID and Secret in DGMC Cloud Services.
Create a service account for the Cloud Run function
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
digitalguardian-ingestion
(or a descriptive name).
Service account description
: Enter
Service account for Digital Guardian EDR Cloud Run function to write logs to GCS
.
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
Storage Object Admin
(to read/write objects in the Cloud Storage bucket)
Cloud Run Invoker
(to allow Cloud Scheduler to invoke the function)
Click
Continue
.
Click
Done
.
Create a Pub/Sub topic
Cloud Scheduler triggers the Cloud Run function through a Pub/Sub topic.
In the
Google Cloud console
, go to
Pub/Sub
>
Topics
.
Click
Create topic
.
In the
Topic ID
field, enter
digitalguardian-edr-trigger
.
Leave the default settings.
Click
Create
.
Create the Cloud Run function
Create a Cloud Run function that authenticates to the Digital Guardian ARC using OAuth 2.0 client credentials, retrieves export data, acknowledges the bookmark to advance to the next chunk, and writes results as NDJSON to GCS.
Prepare function source files
Create the following two files for the Cloud Run function deployment.
requirements.txt
functions-framework==3.*
google-cloud-storage==2.*
urllib3==2.*
main.py
"""Cloud Run function to ingest Digital Guardian EDR logs into GCS."""
import
json
import
os
import
time
import
urllib.parse
from
datetime
import
datetime
,
timezone
import
functions_framework
import
urllib3
from
google.cloud
import
storage
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
"digitalguardian_edr"
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
"digitalguardian_edr_state.json"
)
AUTH_SERVER_URL
=
os
.
environ
[
"AUTH_SERVER_URL"
]
ARC_SERVER_URL
=
os
.
environ
[
"ARC_SERVER_URL"
]
CLIENT_ID
=
os
.
environ
[
"CLIENT_ID"
]
CLIENT_SECRET
=
os
.
environ
[
"CLIENT_SECRET"
]
EXPORT_PROFILE_GUID
=
os
.
environ
[
"EXPORT_PROFILE_GUID"
]
MAX_RECORDS
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
http
=
urllib3
.
PoolManager
()
gcs
=
storage
.
Client
()
def
_get_access_token
()
-
>
str
:
"""Obtain an OAuth 2.0 access token using client credentials grant."""
body
=
urllib
.
parse
.
urlencode
({
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
,
"scope"
:
"client"
,
})
resp
=
http
.
request
(
"POST"
,
AUTH_SERVER_URL
,
body
=
body
,
headers
=
{
"Content-Type"
:
"application/x-www-form-urlencoded"
},
)
if
resp
.
status
!=
200
:
raise
RuntimeError
(
f
"OAuth token request failed:
{
resp
.
status
}
— "
f
"
{
resp
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
token_data
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
return
token_data
[
"access_token"
]
def
_arc_get
(
token
:
str
,
path
:
str
,
retries
:
int
=
5
)
-
>
dict
:
"""Execute a GET request against the ARC API with retry on 429."""
url
=
f
"
{
ARC_SERVER_URL
}{
path
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
,
}
backoff
=
2
for
attempt
in
range
(
retries
):
resp
=
http
.
request
(
"GET"
,
url
,
headers
=
headers
)
if
resp
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
resp
.
data
.
decode
(
"utf-8"
))
if
resp
.
status
==
429
:
wait
=
backoff
*
(
2
**
attempt
)
print
(
f
"Rate limited (429). Retrying in
{
wait
}
s "
f
"(attempt
{
attempt
+
1
}
/
{
retries
}
)."
)
time
.
sleep
(
wait
)
continue
raise
RuntimeError
(
f
"ARC API error:
{
resp
.
status
}
—
{
resp
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
raise
RuntimeError
(
"ARC API rate limit exceeded after maximum retries."
)
def
_arc_acknowledge
(
token
:
str
)
-
>
None
:
"""POST to the acknowledge endpoint to advance the export bookmark."""
url
=
(
f
"
{
ARC_SERVER_URL
}
/rest/1.0/export/"
f
"
{
EXPORT_PROFILE_GUID
}
/acknowledge"
)
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
,
}
resp
=
http
.
request
(
"POST"
,
url
,
headers
=
headers
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
204
):
raise
RuntimeError
(
f
"ARC acknowledge failed:
{
resp
.
status
}
— "
f
"
{
resp
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
print
(
"Export bookmark acknowledged successfully."
)
def
_load_state
()
-
>
dict
:
"""Load the last run state from GCS."""
bucket
=
gcs
.
bugcs
.
bucket
UCKET
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
}
/
{
STATE_KEY
}
"
)
if
blob
.
exists
():
return
json
.
loads
(
blob
.
downlo
download_as_text
return
{}
def
_save_state
(
state
:
dict
)
-
>
None
:
"""Persist run state to GCS."""
bucket
=
gcs
.
bugcs
.
bucket
UCKET
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
}
/
{
STATE_KEY
}
"
)
blob
.
upload
upload_from_string
json
.
dumps
(
state
),
content_type
=
"application/json"
)
def
_fetch_export
(
token
:
str
)
-
>
list
:
"""Fetch export data from the ARC Export API."""
path
=
f
"/rest/1.0/export/
{
EXPORT_PROFILE_GUID
}
"
data
=
_arc_get
(
token
,
path
)
records
=
data
if
isinstance
(
data
,
list
)
else
data
.
get
(
"data"
,
[])
return
records
[:
MAX_RECORDS
]
def
_write_ndjson
(
records
:
list
,
run_ts
:
str
)
-
>
str
:
"""Write records as NDJSON to GCS and return the blob path."""
bucket
=
gcs
.
bugcs
.
bucket
UCKET
)
blob_path
=
(
f
"
{
GCS_PREFIX
}
/year=
{
run_ts
[:
4
]
}
/month=
{
run_ts
[
5
:
7
]
}
/"
f
"day=
{
run_ts
[
8
:
10
]
}
/
{
run_ts
}
_export.ndjson"
)
blob
=
bucket
.
blob
(
blob_path
)
ndjson
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
r
,
separators
=
(
","
,
":"
))
for
r
in
records
)
blob
.
upload
upload_from_string
n
,
content_type
=
"application/x-ndjson"
)
return
blob_path
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""Entry point triggered by Pub/Sub via Cloud Scheduler."""
state
=
_load_state
()
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
print
(
"Authenticating to Digital Guardian ARC."
)
token
=
_get_access_token
()
print
(
f
"Fetching export data for profile
{
EXPORT_PROFILE_GUID
}
."
)
records
=
_fetch_export
(
token
)
if
not
records
:
print
(
"No new export data found."
)
return
"OK"
run_ts
=
now
.
strftime
(
"%Y-%m-
%d
T%H%M%SZ"
)
blob_path
=
_write_ndjson
(
records
,
run_ts
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
records to "
f
"gs://
{
GCS_BUCKET
}
/
{
blob_path
}
."
)
_arc_acknowledge
(
token
)
state
[
"last_run"
]
=
now
.
isoformat
()
state
[
"records_written"
]
=
len
(
records
)
_save_state
(
state
)
print
(
f
"State updated. last_run=
{
now
.
isoformat
()
}
."
)
return
"OK"
Deploy the Cloud Run function
Save both files (
main.py
and
requirements.txt
) into a local directory (for example,
digitalguardian-function/
).
Open
Cloud Shell
or a terminal with the
gcloud
CLI installed.
Run the following command to deploy the function:
gcloud
functions
deploy
digitalguardian-edr-to-gcs
\
--gen2
\
--region
=
us-central1
\
--runtime
=
python312
\
--trigger-topic
=
digitalguardian-edr-trigger
\
--entry-point
=
main
\
--memory
=
512MB
\
--timeout
=
540s
\
--service-account
=
digitalguardian-ingestion@PROJECT_ID.iam.gserviceaccount.com
\
--set-env-vars
=
\
"GCS_BUCKET=digitalguardian-edr-logs"
,
\
"GCS_PREFIX=digitalguardian_edr"
,
\
"STATE_KEY=digitalguardian_edr_state.json"
,
\
"AUTH_SERVER_URL=https://authsrv.msp.digitalguardian.com/as/token.oauth2"
,
\
"ARC_SERVER_URL=https://accessgw-usw.msp.digitalguardian.com"
,
\
"CLIENT_ID=YOUR_CLIENT_ID"
,
\
"CLIENT_SECRET=YOUR_CLIENT_SECRET"
,
\
"EXPORT_PROFILE_GUID=YOUR_EXPORT_PROFILE_GUID"
,
\
"MAX_RECORDS=10000"
Replace the following placeholder values:
PROJECT_ID
: Your Google Cloud project ID.
digitalguardian-edr-logs
: Your GCS bucket name.
YOUR_CLIENT_ID
: Your Digital Guardian API Access ID.
YOUR_CLIENT_SECRET
: Your Digital Guardian API Access Secret.
YOUR_EXPORT_PROFILE_GUID
: Your Export Profile GUID from DGMC.
Verify the deployment by checking the function status:
gcloud
functions
describe
digitalguardian-edr-to-gcs
--region
=
us-central1
--gen2
Environment variables reference
Variable
Required
Default
Description
GCS_BUCKET
Yes
GCS bucket name for storing NDJSON output
GCS_PREFIX
No
digitalguardian_edr
Object prefix (folder path) within the bucket
STATE_KEY
No
digitalguardian_edr_state.json
Blob name for the state file within the prefix
AUTH_SERVER_URL
Yes
OAuth 2.0 authorization server URL
ARC_SERVER_URL
Yes
ARC Access Gateway base URL
CLIENT_ID
Yes
API Access ID from DGMC
CLIENT_SECRET
Yes
API Access Secret from DGMC
EXPORT_PROFILE_GUID
Yes
Export Profile GUID from DGMC
MAX_RECORDS
No
10000
Maximum number of records to write per execution
Create a Cloud Scheduler job
Cloud Scheduler triggers the Cloud Run function at regular intervals through the Pub/Sub topic.
In the
Google Cloud console
, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Name
: Enter
digitalguardian-edr-ingestion-schedule
.
Region
: Select the same region as your Cloud Run function (for example,
us-central1
).
Frequency
: Enter
*/5 * * * *
(every 5 minutes).
Timezone
: Select your preferred timezone (for example,
UTC
).
Click
Continue
.
In the
Configure the execution
section:
Target type
: Select
Pub/Sub
.
Topic
: Select
digitalguardian-edr-trigger
.
Message body
: Enter
{"run": true}
.
Click
Continue
.
In the
Configure optional settings
section:
Max retry attempts
: Enter
3
.
Min backoff duration
: Enter
5s
.
Max backoff duration
: Enter
60s
.
Click
Create
.
To run an immediate test, click the three dots (
...
) next to the job name and select
Force run
.
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
Digital Guardian EDR Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Digital Guardian EDR
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
: Enter the GCS bucket URI:
gs://digitalguardian-edr-logs/digitalguardian_edr/
Replace
digitalguardian-edr-logs
with your GCS bucket name.
Replace
digitalguardian_edr
with your configured
GCS_PREFIX
value.
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days).
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
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your Cloud Storage bucket.
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name (for example,
digitalguardian-edr-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email (for example,
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Viewer
.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
Application
target.application
Value copied directly
Application
target.process.command_line
Set to %{Application} if Rule matches .
Printer.
Bytes_Written
network.sent_bytes
Value copied directly and converted to uinteger
Category, Computer_Name, Detail
metadata.description
Set to %{Detail} if Category == "Policies" and Computer_Name is empty; else set to %{message} on grok_parse_failure
Command_Line, Command_Line1
principal.process.command_line
Value from Command_Line after removing trailing quotes if not empty, else from Command_Line1 after removing trailing quotes
Computer_Name, source
principal.hostname
Value from computerName if not empty, else set to %{source}
Destination_Device_Serial_Number, Destination_Device_Serial_Number1
Extracted using grok pattern for handling quotes
Destination_Directory, Destination_File
target.file.full_path
Concatenated from Destination_Directory and Destination_File if both not empty
Destination_Drive_Type
security_result.detection_fields
Merged with destination_drive_type_label (key: Destination_Drive_Type, value: %{Destination_Drive_Type})
Destination_File
target.file.names
Merged from Destination_File
Destination_File_Extension
target.file.mime_type
Value copied directly
Dll_SHA1_Hash
target.process.file.sha1
Value copied directly after converting to lowercase
Email_Address
principal.user.email_addresses
Merged from Email_Address
Email_Sender, Email_Subject
network.email.from
Set to %{Email_Sender} if not empty
Email_Sender, Email_Subject
network.email.subject
Merged from subject (%{Email_Subject}) if Email_Sender not empty
File_Extension
principal.process.file.mime_type
Value copied directly
IP_Address, source_ip
principal.ip
Merged from source_ip if not empty, else from IP_Address
Local_Port, source_port
principal.port
Value from source_port if not empty and converted to integer, else from Local_Port and converted to integer
MD5_Checksum
target.process.file.md5
Value copied directly after converting to lowercase
Network_Direction
network.direction
Set to INBOUND if True, else OUTBOUND if False
Process_PID
principal.process.pid
Value copied directly
Process_SHA256_Hash
target.process.file.sha256
Value copied directly after converting to lowercase
Product_Version
metadata.product_version
Value copied directly
Protocol
network.ip_protocol
Set to ICMP if == "1"
Remote_Port
target.port
Value copied directly and converted to integer
Rule
security_result.rule_name
Value copied directly
Rule
metadata.event_type
Set to PROCESS_UNCATEGORIZED if matches .
Printer.
, else FILE_MOVE if matches DLP.*
Severity
security_result.severity
Set to LOW if <=3, MEDIUM if <=6, HIGH if <=8, CRITICAL if <=10 after converting to integer
Severity
security_result.severity_details
Value copied directly
Source_Directory, Source_File
src.file.full_path
Concatenated from Source_Directory and Source_File if both not empty
Source_Drive_Type
security_result.detection_fields
Merged with source_drive_type_label (key: Source_Drive_Type, value: %{Source_Drive_Type})
Source_File
src.file.names
Merged from Source_File
Source_File_Extension
src.file.mime_type
Value copied directly
URL_Path, http_url
target.url
Value from http_url if not empty, else from URL_Path
User_Name
principal.user.userid
Value from userName after grok extraction
User_Name
principal.administrative_domain
Value from domainName after grok extraction
Was_Removable
security_result.detection_fields
Merged with was_removable_label (key: Was_Removable, value: %{Was_Removable})
Was_Source_Removable
security_result.detection_fields
Merged with was_source_removable_label (key: Was_Source_Removable, value: %{Was_Source_Removable})
computerName, destination_ip, protocol, source_ip, IP_Address, destination, userName, Process_PID, Category, Computer_Name
metadata.event_type
Set to GENERIC_EVENT initially; NETWORK_HTTP if protocol == HTTPS and (destination_ip or computerName); NETWORK_CONNECTION if (source_ip or IP_Address) and destination_ip; USER_UNCATEGORIZED if userName not empty; SCAN_PROCESS if Process_PID not empty
destination_ip
target.ip
Merged from destination_ip
incidents_url, matched_policies_by_severity
security_result
Merged with _sr (rule_name: %{matched_policies_by_severity}, url_back_to_product: %{incidents_url})
protocol
network.application_protocol
Set to HTTPS if protocol == HTTP or HTTPS
security_action
security_result.action
Merged from security_action
metadata.product_name
Set to "Enterprise DLP Platform"
metadata.vendor_name
Set to "DigitalGuardian"
Need more help?
Get answers from Community members and Google SecOps professionals.
