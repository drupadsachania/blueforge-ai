# Collect Workday audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-audit/  
**Scraped:** 2026-03-05T10:02:37.299998Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Workday audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Workday audit logs to Google Security Operations using Google Cloud Storage. The parser first identifies the specific event type from the logs based on pattern analysis of the JSON data. Then, it extracts and structures relevant fields according to the identified type, mapping them to a unified data model (UDM) for consistent security analysis.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Workday
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
workday-audit-logs
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
Create Workday Integration System User (ISU)
In Workday, search for
Create Integration System User
>
OK
.
Fill in the
User Name
(for example,
audit_gcs_user
).
Click
OK
.
Reset the password by going to
Related Actions
>
Security
>
Reset Password
.
Select
Maintain Password Rules
to prevent the password from expiring.
Search for
Create Security Group
>
Integration System Security Group (Unconstrained)
.
Provide a name (for example,
ISU_Audit_GCS
) and add the ISU to
Integration System Users
.
Search for
Domain Security Policies for Functional Area
>
System
.
For
Audit Trail
, select
Actions
>
Edit Permissions
.
Under
Get Only
, add the
ISU_Audit_GCS
group.
Click
OK
>
Activate Pending Security Policy Changes
.
Configure Workday Custom Report
In Workday, search
Create Custom Report
.
Provide the following configuration details:
Name
: Enter a unique name (for example,
Audit_Trail_BP_JSON
).
Type
: Select
Advanced
.
Data Source
: Select
Audit Trail – Business Process
.
Click
OK
.
Optional: Add filters on
Business Process Type
or
Effective Date
.
Go to
Output
tab.
Select
Enable as Web Service
,
Optimized for Performance
and select
JSON Format
.
Click
OK
>
Done
.
Open the report and click
Share
>
add ISU_Audit_GCS with View permission
>
OK
.
Go to
Related Actions
>
Web Service
>
View URLs
.
Copy the JSON URL.
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
workday-audit-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Workday audit logs
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
workday-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
workday-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Workday API and writes them to GCS.
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
workday-audit-collector
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
workday-audit-trigger
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
workday-audit-collector-sa
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
workday-audit-logs
WD_USER
audit_gcs_user
WD_PASS
your-workday-password
WD_URL
https://wd-servicesN.workday.com/ccx/service/customreport2/<tenant>/<user>/Audit_Trail_BP_JSON?format=json
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
base64
import
gzip
import
io
import
uuid
# Initialize HTTP client
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
5.0
,
read
=
30.0
),
retries
=
False
,
)
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
Cloud Run function triggered by Pub/Sub to fetch logs from Workday API and write to GCS.
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
wd_user
=
os
.
environ
.
get
(
'WD_USER'
)
wd_pass
=
os
.
environ
.
get
(
'WD_PASS'
)
wd_url
=
os
.
environ
.
get
(
'WD_URL'
)
if
not
all
([
bucket_name
,
wd_user
,
wd_pass
,
wd_url
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
print
(
f
'Fetching Workday audit report from
{
wd_url
}
'
)
# Fetch report from Workday
data
=
fetch_report
(
wd_url
,
wd_user
,
wd_pass
)
# Upload to GCS
timestamp
=
datetime
.
now
(
timezone
.
utc
)
upload
(
bucket
,
data
,
timestamp
)
print
(
f
'Successfully uploaded Workday audit report (
{
len
(
data
)
}
bytes raw)'
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
fetch_report
(
url
,
username
,
password
):
"""Fetch report from Workday using Basic Auth."""
credentials
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
credentials_bytes
=
credentials
.
encode
(
'utf-8'
)
auth_header
=
b
"Basic "
+
base64
.
b64encode
(
credentials_bytes
)
req_headers
=
{
"Authorization"
:
auth_header
.
decode
(
'utf-8'
)
}
response
=
http
.
request
(
'GET'
,
url
,
headers
=
req_headers
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
"Failed to fetch report: HTTP
{
response
.
status
}
"
)
return
response
.
data
def
upload
(
bucket
,
payload
,
ts
):
"""Upload gzipped JSON to GCS."""
key
=
f
"
{
ts
:
%Y/%m/%d
}
/workday-audit-
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
'w'
)
as
gz
:
gz
.
write
(
payload
)
buf
.
seek
(
0
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
'application/gzip'
)
print
(
f
'Uploaded to gs://
{
bucket
.
name
}
/
{
key
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
Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
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
workday-audit-collector-daily
Region
Select same region as Cloud Run function
Frequency
20 2 * * *
(runs daily at 02:20 UTC)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select the topic
workday-audit-trigger
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
Standard
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
20 2 * * *
Historical data collection (recommended)
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
workday-audit-collector
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
Workday Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Workday Audit
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
Configure a feed in Google SecOps to ingest Workday Audit logs
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
Workday Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Workday Audit
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://workday-audit-logs/
Replace
workday-audit-logs
with your actual GCS bucket name.
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
Account
metadata.event_type
If the "Account" field is not empty, the "metadata.event_type" field is set to "USER_RESOURCE_UPDATE_CONTENT".
Account
principal.user.primaryId
The userid is extracted from the "Account" field using a grok pattern and mapped to principal.user.primaryId.
Account
principal.user.primaryName
The user display name is extracted from the "Account" field using a grok pattern and mapped to "principal.user.primaryName".
ActivityCategory
metadata.event_type
If the "ActivityCategory" field is "READ", the "metadata.event_type" field is set to "RESOURCE_READ". If "WRITE", it's set to "RESOURCE_WRITTEN".
ActivityCategory
metadata.product_event_type
Directly mapped from the "ActivityCategory" field.
AffectedGroups
target.user.group_identifiers
Directly mapped from the "AffectedGroups" field.
Area
target.resource.attribute.labels.area.value
Directly mapped from the "Area" field.
AuthType
extensions.auth.auth_details
Directly mapped from the "AuthType" field.
AuthType
extensions.auth.type
Mapped from the "AuthType" field to different authentication types defined in the UDM based on specific values.
CFIPdeConexion
src.domain.name
If the "CFIPdeConexion" field is not a valid IP address, it's mapped to "src.domain.name".
CFIPdeConexion
target.ip
If the "CFIPdeConexion" field is a valid IP address, it's mapped to "target.ip".
ChangedRelationship
metadata.description
Directly mapped from the "ChangedRelationship" field.
ClassOfInstance
target.resource.attribute.labels.class_instance.value
Directly mapped from the "ClassOfInstance" field.
column18
about.labels.utub.value
Directly mapped from the "column18" field.
CreatedBy
principal.user.userid
The userid is extracted from the "CreatedBy" field using a grok pattern and mapped to "principal.user.userid".
CreatedBy
principal.user.user_display_name
The user display name is extracted from the "CreatedBy" field using a grok pattern and mapped to "principal.user.user_display_name".
Domain
about.domain.name
Directly mapped from the "Domain" field.
EffectiveDate
@timestamp
Parsed to "@timestamp" after converting to "yyyy-MM-dd HH:mm:ss.SSSZ" format.
EntryMoment
@timestamp
Parsed to "@timestamp" after converting to "ISO8601" format.
EventType
security_result.description
Directly mapped from the "EventType" field.
Form
target.resource.name
Directly mapped from the "Form" field.
InstancesAdded
about.resource.attribute.labels.instances_added.value
Directly mapped from the "InstancesAdded" field.
InstancesAdded
target.user.attribute.roles.instances_added.name
Directly mapped from the "InstancesAdded" field.
InstancesRemoved
about.resource.attribute.labels.instances_removed.value
Directly mapped from the "InstancesRemoved" field.
InstancesRemoved
target.user.attribute.roles.instances_removed.name
Directly mapped from the "InstancesRemoved" field.
IntegrationEvent
target.resource.attribute.labels.integration_event.value
Directly mapped from the "IntegrationEvent" field.
IntegrationStatus
security_result.action_details
Directly mapped from the "IntegrationStatus" field.
IntegrationSystem
target.resource.name
Directly mapped from the "IntegrationSystem" field.
IP
src.domain.name
If the "IP" field is not a valid IP address, it's mapped to "src.domain.name".
IP
src.ip
If the "IP" field is a valid IP address, it's mapped to "src.ip".
IsDeviceManaged
additional.fields.additional1.value.string_value
If the "IsDeviceManaged" field is "N", the value is set to "Successful". Otherwise, it's set to "Failed login occurred".
IsDeviceManaged
additional.fields.additional2.value.string_value
If the "IsDeviceManaged" field is "N", the value is set to "Successful". Otherwise, it's set to "Invalid Credentials".
IsDeviceManaged
additional.fields.additional3.value.string_value
If the "IsDeviceManaged" field is "N", the value is set to "Successful". Otherwise, it's set to "Account Locked".
IsDeviceManaged
security_result.action_details
Directly mapped from the "IsDeviceManaged" field.
OutputFiles
about.file.full_path
Directly mapped from the "OutputFiles" field.
Person
principal.user.primaryId
If the "Person" field starts with "INT", the userid is extracted using a grok pattern and mapped to "principal.user.primaryId".
Person
principal.user.primaryName
If the "Person" field starts with "INT", the user display name is extracted using a grok pattern and mapped to "principal.user.primaryName".
Person
principal.user.user_display_name
If the "Person" field doesn't start with "INT", it's directly mapped to "principal.user.user_display_name".
Person
metadata.event_type
If the "Person" field is not empty, the "metadata.event_type" field is set to "USER_RESOURCE_UPDATE_CONTENT".
ProcessedTransaction
target.resource.attribute.creation_time
Parsed to "target.resource.attribute.creation_time" after converting to "dd/MM/yyyy HH:mm:ss,SSS (ZZZ)", "dd/MM/yyyy, HH:mm:ss,SSS (ZZZ)", or "MM/dd/yyyy, HH:mm:ss.SSS A ZZZ" format.
ProgramBy
principal.user.userid
Directly mapped from the "ProgramBy" field.
RecurrenceEndDate
principal.resource.attribute.last_update_time
Parsed to "principal.resource.attribute.last_update_time" after converting to "yyyy-MM-dd" format.
RecurrenceStartDate
principal.resource.attribute.creation_time
Parsed to "principal.resource.attribute.creation_time" after converting to "yyyy-MM-dd" format.
RequestName
metadata.description
Directly mapped from the "RequestName" field.
ResponseMessage
security_result.summary
Directly mapped from the "ResponseMessage" field.
RestrictedToEnvironment
security_result.about.hostname
Directly mapped from the "RestrictedToEnvironment" field.
RevokedSecurity
security_result.outcomes.outcomes.value
Directly mapped from the "RevokedSecurity" field.
RunFrequency
principal.resource.attribute.labels.run_frequency.value
Directly mapped from the "RunFrequency" field.
ScheduledProcess
principal.resource.name
Directly mapped from the "ScheduledProcess" field.
SecuredTaskExecuted
target.resource.name
Directly mapped from the "SecuredTaskExecuted" field.
SecureTaskExecuted
metadata.event_type
If the "SecureTaskExecuted" field contains "Create", the "metadata.event_type" field is set to "USER_RESOURCE_CREATION".
SecureTaskExecuted
target.resource.name
Directly mapped from the "SecureTaskExecuted" field.
SentTime
@timestamp
Parsed to "@timestamp" after converting to "ISO8601" format.
SessionId
network.session_id
Directly mapped from the "SessionId" field.
ShareBy
target.user.userid
Directly mapped from the "ShareBy" field.
SignOffTime
additional.fields.additional4.value.string_value
The "AuthFailMessage" field value is placed within the "additional.fields" array with the key "Enterprise Interface Builder".
SignOffTime
metadata.description
Directly mapped from the "AuthFailMessage" field.
SignOffTime
metadata.event_type
If the "SignOffTime" field is empty, the "metadata.event_type" field is set to "USER_LOGIN". Otherwise, it's set to "USER_LOGOUT".
SignOffTime
principal.user.attribute.last_update_time
Parsed to "principal.user.attribute.last_update_time" after converting to "ISO8601" format.
SignOnIp
src.domain.name
If the "SignOnIp" field is not a valid IP address, it's mapped to "src.domain.name".
SignOnIp
src.ip
If the "SignOnIp" field is a valid IP address, it's mapped to "src.ip".
Status
metadata.product_event_type
Directly mapped from the "Status" field.
SystemAccount
principal.user.email_addresses
The email address is extracted from the "SystemAccount" field using a grok pattern and mapped to "principal.user.email_addresses".
SystemAccount
principal.user.primaryId
The userid is extracted from the "SystemAccount" field using a grok pattern and mapped to "principal.user.primaryId".
SystemAccount
principal.user.primaryName
The user display name is extracted from the "SystemAccount" field using a grok pattern and mapped to "principal.user.primaryName".
SystemAccount
src.user.userid
The secondary userid is extracted from the "SystemAccount" field using a grok pattern and mapped to "src.user.userid".
SystemAccount
src.user.user_display_name
The secondary user display name is extracted from the "SystemAccount" field using a grok pattern and mapped to "src.user.user_display_name".
SystemAccount
target.user.userid
The target userid is extracted from the "SystemAccount" field using a grok pattern and mapped to "target.user.userid".
Target
target.user.user_display_name
Directly mapped from the "Target" field.
Template
about.resource.name
Directly mapped from the "Template" field.
Tenant
target.asset.hostname
Directly mapped from the "Tenant" field.
TlsVersion
network.tls.version
Directly mapped from the "TlsVersion" field.
Transaction
security_result.action_details
Directly mapped from the "Transaction" field.
TransactionType
security_result.summary
Directly mapped from the "TransactionType" field.
TypeForm
target.resource.resource_subtype
Directly mapped from the "TypeForm" field.
UserAgent
network.http.parsed_user_agent
Parsed from the "UserAgent" field using the "useragent" filter.
UserAgent
network.http.user_agent
Directly mapped from the "UserAgent" field.
WorkdayAccount
target.user.user_display_name
The user display name is extracted from the "WorkdayAccount" field using a grok pattern and mapped to "target.user.user_display_name".
WorkdayAccount
target.user.userid
The userid is extracted from the "WorkdayAccount" field using a grok pattern and mapped to "target.user.userid".
additional.fields.additional1.key
Set to "FailedSignOn".
additional.fields.additional2.key
Set to "InvalidCredentials".
additional.fields.additional3.key
Set to "AccountLocked".
additional.fields.additional4.key
Set to "Enterprise Interface Builder".
metadata.event_type
Set to "GENERIC_EVENT" initially and then updated based on the logic involving other fields.
metadata.event_type
Set to "USER_CHANGE_PERMISSIONS" for specific event types.
metadata.event_type
Set to "RESOURCE_WRITTEN" for specific event types.
metadata.log_type
Hardcoded to "WORKDAY_AUDIT".
metadata.product_name
Hardcoded to "Enterprise Interface Builder".
metadata.vendor_name
Hardcoded to "Workday".
principal.asset.category
Set to "Phone" if the "DeviceType" field is "Phone".
principal.resource.resource_type
Hardcoded to "TASK" if the "ScheduledProcess" field is not empty.
security_result.action
Set to "ALLOW" or "FAIL" based on the values of "FailedSignOn", "IsDeviceManaged", "InvalidCredentials", and "AccountLocked" fields.
security_result.summary
Set to "Successful" or specific error messages based on the values of "FailedSignOn", "IsDeviceManaged", "InvalidCredentials", and "AccountLocked" fields.
target.resource.resource_type
Hardcoded to "TASK" for specific event types.
target.resource.resource_type
Hardcoded to "DATASET" if the "TypeForm" field is not empty.
message
principal.user.email_addresses
Extracts the email address from the "message" field using a grok pattern and merges it into "principal.user.email_addresses" if a specific pattern is matched.
message
src.user.userid
Clears the field if the "event.idm.read_only_udm.principal.user.userid" field matches the extracted "user_target" from the "message" field.
message
src.user.user_display_name
Clears the field if the "event.idm.read_only_udm.principal.user.userid" field matches the extracted "user_target" from the "message" field.
message
target.user.userid
Extracts the userid from the "message" field using a grok pattern and maps it to "target.user.userid" if a specific pattern is matched.
Need more help?
Get answers from Community members and Google SecOps professionals.
