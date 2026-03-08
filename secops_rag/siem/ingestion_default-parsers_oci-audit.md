# Collect Oracle Cloud Infrastructure Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-audit/  
**Scraped:** 2026-03-05T09:27:11.517136Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Oracle Cloud Infrastructure Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Oracle Cloud Infrastructure Audit logs to Google Security Operations using Google Cloud Storage.
Oracle Cloud Infrastructure Audit service automatically records calls to all supported Oracle Cloud Infrastructure public application programming interface (API) endpoints as log events. Currently, all services support logging by Oracle Cloud Infrastructure Audit. Log events recorded by Oracle Cloud Infrastructure Audit include API calls made by the Oracle Cloud Infrastructure console, Command Line Interface (CLI), Software Development Kits (SDK), your own custom clients, or other Oracle Cloud Infrastructure services.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Oracle Cloud Infrastructure account with permissions to create and manage:
Service Connector Hub
Functions
Object Storage buckets
IAM policies
Privileged access to Oracle Cloud Infrastructure console
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
oci-audit-logs-gcs
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
Configure Oracle Cloud Infrastructure to export Audit logs to GCS
Oracle Cloud Infrastructure does not support native export to Google Cloud Storage. You will use Oracle Cloud Infrastructure Service Connector Hub with a Function to forward Audit logs to GCS.
Create Oracle Cloud Infrastructure Function to forward logs to GCS
Sign in to the
Oracle Cloud Console
.
Go to
Developer Services
>
Functions
>
Applications
.
Select the compartment where you want to create the function application.
Click
Create Application
.
Provide the following configuration details:
Name
: Enter
audit-logs-to-gcs-app
.
VCN
: Select a Virtual Cloud Network.
Subnets
: Select a subnet with internet access.
Click
Create
.
After the application is created, click
Getting Started
and follow the instructions to set up your local development environment with the Fn CLI.
Create a new function directory on your local machine:
mkdir
oci-audit-to-gcs
cd
oci-audit-to-gcs
Initialize a Python function:
fn
init
--runtime
python
oci-audit-to-gcs
cd
oci-audit-to-gcs
Replace the contents of
func.py
with the following code:
import
io
import
json
import
logging
import
os
from
fdk
import
response
from
google.cloud
import
storage
from
google.oauth2
import
service_account
from
datetime
import
datetime
# Configure logging
logging
.
basicConfig
(
level
=
logging
.
INFO
)
logger
=
logging
.
getLogger
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
'oci-audit-logs'
)
GCS_CREDENTIALS_JSON
=
os
.
environ
.
get
(
'GCS_CREDENTIALS_JSON'
)
def
handler
(
ctx
,
data
:
io
.
BytesIO
=
None
):
"""
Oracle Cloud Infrastructure Function to forward Audit logs to GCS.
Args:
ctx: Function context
data: Input data containing Audit log events
"""
if
not
all
([
GCS_BUCKET
,
GCS_CREDENTIALS_JSON
]):
logger
.
error
(
'Missing required environment variables: GCS_BUCKET or GCS_CREDENTIALS_JSON'
)
return
response
.
Response
(
ctx
,
response_data
=
json
.
dumps
({
"error"
:
"Missing configuration"
}),
headers
=
{
"Content-Type"
:
"application/json"
}
)
try
:
# Parse input data
body
=
json
.
loads
(
data
.
getvalue
())
logger
.
info
(
f
"Received event:
{
json
.
dumps
(
body
)
}
"
)
# Extract log entries
log_entries
=
[]
if
isinstance
(
body
,
list
):
log_entries
=
body
elif
isinstance
(
body
,
dict
):
# Service Connector Hub sends data in specific format
if
'data'
in
body
:
log_entries
=
[
body
[
'data'
]]
if
isinstance
(
body
[
'data'
],
dict
)
else
body
[
'data'
]
else
:
log_entries
=
[
body
]
if
not
log_entries
:
logger
.
info
(
"No log entries to process"
)
return
response
.
Response
(
ctx
,
response_data
=
json
.
dumps
({
"status"
:
"no_logs"
}),
headers
=
{
"Content-Type"
:
"application/json"
}
)
# Initialize GCS client with service account credentials
credentials_dict
=
json
.
loads
(
GCS_CREDENTIALS_JSON
)
credentials
=
service_account
.
Credentials
.
from_service_account_info
(
credentials_dict
)
storage_client
=
storage
.
Client
(
credentials
=
credentials
,
project
=
credentials_dict
.
get
(
'project_id'
))
bucket
=
storage_client
.
bucket
(
GCS_BUCKET
)
# Write logs to GCS as NDJSON
timestamp
=
datetime
.
utcnow
()
.
strftime
(
'%Y%m
%d
_%H%M%S_
%f
'
)
object_key
=
f
"
{
GCS_PREFIX
}
/logs_
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
entry
,
ensure_ascii
=
False
)
for
entry
in
log_entries
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
logger
.
info
(
f
"Wrote
{
len
(
log_entries
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
return
response
.
Response
(
ctx
,
response_data
=
json
.
dumps
({
"status"
:
"success"
,
"records"
:
len
(
log_entries
)}),
headers
=
{
"Content-Type"
:
"application/json"
}
)
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
'Error processing logs:
{
str
(
e
)
}
'
)
return
response
.
Response
(
ctx
,
response_data
=
json
.
dumps
({
"error"
:
str
(
e
)}),
headers
=
{
"Content-Type"
:
"application/json"
},
status_code
=
500
)
Update
requirements.txt
with the following dependencies:
fdk>=0.1.0
google-cloud-storage>=2.0.0
google-auth>=2.0.0
Deploy the function to Oracle Cloud Infrastructure:
fn
-v
deploy
--app
audit-logs-to-gcs-app
After deployment completes, note the function OCID. You will use it in the next step.
Configure function environment variables
In the Oracle Cloud Console, go to
Developer Services
>
Functions
>
Applications
.
Click the application (
audit-logs-to-gcs-app
).
Click the function name (
oci-audit-to-gcs
).
Click
Configuration
.
Add the following configuration variables:
Key
Value
GCS_BUCKET
Your GCS bucket name (for example,
oci-audit-logs-gcs
)
GCS_PREFIX
Prefix for log files (for example,
oci-audit-logs
)
GCS_CREDENTIALS_JSON
JSON string of GCP service account key (see below)
Click
Save changes
.
Create GCP service account for Oracle Cloud Infrastructure Function
The Oracle Cloud Infrastructure Function needs a GCP service account to write to the GCS bucket.
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
oci-function-gcs-writer
.
Service account description
: Enter
Service account for OCI Function to write Audit logs to GCS
.
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following role:
Click
Select a role
.
Search for and select
Storage Object Admin
.
Click
Continue
.
Click
Done
.
Click the newly created service account email.
Go to the
Keys
tab.
Click
Add Key
>
Create new key
.
Select
JSON
as the key type.
Click
Create
.
The JSON key file will be downloaded to your computer.
Open the JSON key file and copy its entire contents.
Return to the Oracle Cloud Console function configuration.
Paste the JSON contents into the
GCS_CREDENTIALS_JSON
configuration variable.
Grant IAM permissions on GCS bucket
Grant the service account write permissions on the GCS bucket:
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
oci-audit-logs-gcs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (
oci-function-gcs-writer@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create Oracle Cloud Infrastructure Service Connector Hub
Sign in to the Oracle Cloud Console.
Go to
Observability & Management
>
Logging
>
Service Connector Hub
.
Select the compartment where you want to create the service connector.
Click
Create Service Connector
.
Provide the following configuration details:
Service Connector Information:
Setting
Value
Connector Name
Enter
audit-logs-to-gcs-connector
Description
Enter
Forward OCI Audit logs to Google Cloud Storage
Resource Compartment
Select the compartment
Configure Source:
Setting
Value
Source
Select
Logging
Compartment
Select the compartment containing audit logs
Log Group
Select
_Audit
(default log group for audit logs)
Click
+ Another Log
.
Select the audit log for your compartment (for example,
_Audit_Include_Subcompartment
).
Configure Target:
Setting
Value
Target
Select
Functions
Function Compartment
Select the compartment containing the function
Function Application
Select
audit-logs-to-gcs-app
Function
Select
oci-audit-to-gcs
Scroll to
Configure task (optional)
and leave the default settings.
Click
Create
.
Create IAM policy for Service Connector Hub
The Service Connector Hub requires permissions to invoke the function.
In the Oracle Cloud Console, go to
Identity & Security
>
Policies
.
Select the compartment where you created the Service Connector Hub.
Click
Create Policy
.
Provide the following configuration details:
Name
: Enter
service-connector-functions-policy
.
Description
: Enter
Allow Service Connector Hub to invoke Functions
.
Compartment
: Select the compartment.
In the
Policy Builder
section, toggle
Show manual editor
.
Enter the following policy statements:
Allow
any
-
user
to
use
fn
-
function
in
compartment
<
compartment
-
name
>
where
all
{
request
.
principal
.
type
=
'
serviceconnector
'
}
Allow
any
-
user
to
use
fn
-
invocation
in
compartment
<
compartment
-
name
>
where
all
{
request
.
principal
.
type
=
'
serviceconnector
'
}
Replace
<compartment-name>
with your compartment name.
Click
Create
.
Test the integration
Sign in to the Oracle Cloud Console.
Perform some actions that generate audit logs (for example, create or modify a resource).
Wait 2-5 minutes for logs to be processed.
Go to
Cloud Storage
>
Buckets
in the GCP Console.
Click your bucket name (
oci-audit-logs-gcs
).
Navigate to the prefix folder (
oci-audit-logs/
).
Verify that new
.ndjson
files are appearing in the bucket.
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
Oracle Cloud Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Oracle Cloud Infrastructure
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
Click your bucket name (
oci-audit-logs-gcs
).
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
Configure a feed in Google SecOps to ingest Oracle Cloud Infrastructure Audit logs
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
Oracle Cloud Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Oracle Cloud Infrastructure
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://oci-audit-logs-gcs/oci-audit-logs/
Replace:
oci-audit-logs-gcs
: Your GCS bucket name.
oci-audit-logs
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/oci-audit-logs/
With subfolder:
gs://company-logs/oracle/audit/
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
