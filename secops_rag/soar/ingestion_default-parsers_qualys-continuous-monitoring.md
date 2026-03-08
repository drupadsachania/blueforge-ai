# Collect Qualys Continuous Monitoring logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-continuous-monitoring/  
**Scraped:** 2026-03-05T09:59:24.206942Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Qualys Continuous Monitoring logs
Supported in:
Google secops
SIEM
This Logstash parser code first extracts fields such as source IP, user, method, and application protocol from raw log messages using grok patterns. It thenmaps specific fields from the raw log data to their corresponding fields in the Unified Data Model (UDM), performs data type conversions, and enriches the data with additional labels and metadata before finally structuring the output in the desired UDM format.
Before you begin
Ensure that you have the following prerequisites:
Google Security Operations instance.
Privileged access to Google Cloud.
Privileged access to Qualys.
Enable Required APIs:
Sign in to the Google Cloud console.
Go to
APIs & Services
>
Library
.
Search for the following APIs and enable them:
Cloud Functions API
Cloud Scheduler API
Cloud Pub/Sub (required for Cloud Scheduler to invoke functions)
Create a Google Cloud Storage Bucket
Sign in to the Google Cloud console.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
Configure the bucket:
Name
: enter a unique name that meets the bucket name requirements (for example,
qualys-asset-bucket
).
Choose where to store your data
: select a location.
Choose a storage class for your data
: either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management.
Choose how to control access to objects
: select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
Storage class
: choose based on your needs (for example,
Standard
).
Click
Create
.
Create a Google Cloud Service Account
Sign in to the Google Cloud console.
Go to to
IAM & Admin
>
Service Accounts
.
Create a new service account.
Give it a descriptive name (for example,
qualys-user
).
Grant the service account with
Storage Object Admin
role on the GCS bucket you created in the previous step.
Grant the service account with
Cloud Functions Invoker
role.
Create an
SSH key
for the service account.
Download a JSON key file for the service account. Keep this file secure.
Optional: Create a dedicated API User in Qualys
Sign in to the Qualys console.
Go to
Users
.
Click
New
>
User
.
Enter the
General Information
required for the user.
Select the
User Role
tab.
Make sure the role has the
API Access
checkbox selected.
Click
Save
.
Identify your specific Qualys API URL
Option 1
Identify your URLs as mentioned in the
platform identification
.
Option 2
Sign in to the Qualys console.
Go to
Help
>
About
.
Scroll to see this information under Security Operations Center (SOC).
Copy the Qualys API URL.
Configure the Cloud Function
Go to
Cloud Functions
in the Google Cloud console.
Click
Create Function
.
Configure the Function:
Name
: enter a name for your function (for example,
fetch-qualys-cm-alerts
).
Region
: select a region close to your Bucket.
Runtime
: Python 3.10 (or your preferred runtime).
Trigger
: choose HTTP trigger if needed or Cloud Pub/Sub for scheduled execution.
Authentication
: secure with authentication.
Write the Code
with an inline editor:
```
python
from
google.cloud
import
storage
import
requests
import
base64
import
json
# Google Cloud Storage Configuration
BUCKET_NAME
=
"<bucket-name>"
FILE_NAME
=
"qualys_cm_alerts.json"
# Qualys API Credentials
QUALYS_USERNAME
=
"<qualys-username>"
QUALYS_PASSWORD
=
"<qualys-password>"
QUALYS_BASE_URL
=
"https://<qualys_base_url>"
def
fetch_cm_alerts
():
"""Fetch alerts from Qualys Continuous Monitoring."""
auth
=
base64
.
b64encode
(
f
"
{
QUALYS_USERNAME
}
:
{
QUALYS_PASSWORD
}
"
.
encode
())
.
decode
()
headers
=
{
"Authorization"
:
f
"Basic
{
auth
}
"
,
"Content-Type"
:
"application/xml"
}
payload
=
"""
<ServiceRequest>
<filters>
<Criteria field="alert.date" operator="GREATER">2024-01-01</Criteria>
</filters>
</ServiceRequest>
"""
response
=
requests
.
post
(
f
"
{
QUALYS_BASE_URL
}
/qps/rest/2.0/search/cm/alert"
,
headers
=
headers
,
data
=
payload
)
response
.
raise_for_status
()
return
response
.
json
()
def
upload_to_gcs
(
data
):
"""Upload data to Google Cloud Storage."""
client
=
storage
.
Client
()
bucket
=
client
.
get_bucket
(
BUCKET_NAME
)
blob
=
bucket
.
blob
(
FILE_NAME
)
blob
.
upload_from_string
(
json
.
dumps
(
data
,
indent
=
2
),
content_type
=
"application/json"
)
def
main
(
request
):
"""Cloud Function entry point."""
try
:
alerts
=
fetch_cm_alerts
()
upload_to_gcs
(
alerts
)
return
"Qualys CM alerts uploaded to Cloud Storage successfully!"
except
Exception
as
e
:
return
f
"An error occurred:
{
e
}
"
,
500
```
Click
Deploy
after completing the configuration.
Configure Cloud Scheduler
Go to
Cloud Scheduler
in the Google Cloud console.
Click
Create Job
.
Configure the Job:
Name
: enter a name for your job (for example,
trigger-fetch-qualys-cm-alerts
).
Frequency
: use
cron
syntax to specify the schedule (for example,
0 * * * *
to run every hour).
Time Zone
: set your preferred time zone.
Trigger Type
: choose
HTTP
.
Trigger URL
: Enter the Cloud Function's URL (found in the function details after deployment).
Method
: Choose
POST
.
Create the job.
Set up feeds
To configure a feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed; for example,
Qualys Continuous Monitoring Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Qualys Continuous Monitoring
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: the Google Cloud storage bucket source URI.
Source deletion options
: select the deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
Alert.alertInfo.appVersion
metadata.product_version
Directly mapped from
Alert.alertInfo.appVersion
Alert.alertInfo.operatingSystem
principal.platform_version
Directly mapped from
Alert.alertInfo.operatingSystem
Alert.alertInfo.port
additional.fields.value.string_value
Directly mapped from
Alert.alertInfo.port
and added as a key-value pair in
additional.fields
with the key "Alert port"
Alert.alertInfo.protocol
network.ip_protocol
Directly mapped from
Alert.alertInfo.protocol
Alert.alertInfo.sslIssuer
network.tls.client.certificate.issuer
Directly mapped from
Alert.alertInfo.sslIssuer
Alert.alertInfo.sslName
additional.fields.value.string_value
Directly mapped from
Alert.alertInfo.sslName
and added as a key-value pair in
additional.fields
with the key "SSL Name"
Alert.alertInfo.sslOrg
additional.fields.value.string_value
Directly mapped from
Alert.alertInfo.sslOrg
and added as a key-value pair in
additional.fields
with the key "SSL Org"
Alert.alertInfo.ticketId
additional.fields.value.string_value
Directly mapped from
Alert.alertInfo.ticketId
and added as a key-value pair in
additional.fields
with the key "Ticket Id"
Alert.alertInfo.vpeConfidence
additional.fields.value.string_value
Directly mapped from
Alert.alertInfo.vpeConfidence
and added as a key-value pair in
additional.fields
with the key "VPE Confidence"
Alert.alertInfo.vpeStatus
additional.fields.value.string_value
Directly mapped from
Alert.alertInfo.vpeStatus
and added as a key-value pair in
additional.fields
with the key "VPE Confidence"
Alert.eventType
additional.fields.value.string_value
Directly mapped from
Alert.eventType
and added as a key-value pair in
additional.fields
with the key "Event Type"
Alert.hostname
principal.hostname
Directly mapped from
Alert.hostname
Alert.id
security_result.threat_id
Directly mapped from
Alert.id
Alert.ipAddress
principal.ip
Directly mapped from
Alert.ipAddress
Alert.profile.id
additional.fields.value.string_value
Directly mapped from
Alert.profile.id
and added as a key-value pair in
additional.fields
with the key "Profile Id"
Alert.profile.title
additional.fields.value.string_value
Directly mapped from
Alert.profile.title
and added as a key-value pair in
additional.fields
with the key "Profile Title"
Alert.qid
vulnerability.name
Mapped as "QID:
" from
Alert.qid
Alert.source
additional.fields.value.string_value
Directly mapped from
Alert.source
and added as a key-value pair in
additional.fields
with the key "Alert Source"
Alert.triggerUuid
metadata.product_log_id
Directly mapped from
Alert.triggerUuid
Alert.vulnCategory
additional.fields.value.string_value
Directly mapped from
Alert.vulnCategory
and added as a key-value pair in
additional.fields
with the key "Vulnerability Category"
Alert.vulnSeverity
vulnerability.severity
Mapped based on the value of
Alert.vulnSeverity
: 1-3: LOW, 4-6: MEDIUM, 7-8: HIGH
Alert.vulnTitle
vulnerability.description
Directly mapped from
Alert.vulnTitle
Alert.vulnType
additional.fields.value.string_value
Directly mapped from
Alert.vulnType
and added as a key-value pair in
additional.fields
with the key "Vulnerability Type"
Host
principal.ip
Parsed from log line "Host:
"
edr.client.ip_addresses
Copied from
principal.ip
edr.client.hostname
Copied from
principal.hostname
edr.raw_event_name
Set to "STATUS_UPDATE" if
Alert.ipAddress
,
Alert.hostname
or
src_ip
are present, otherwise set to "GENERIC_EVENT"
metadata.event_timestamp
Extracted from
Alert.eventDate
or
timestamp
fields.
Alert.eventDate
is prioritized if it exists, otherwise
timestamp
is used. The timestamp is converted to UTC.
metadata.event_type
Same logic as
edr.raw_event_name
metadata.log_type
Set to "QUALYS_CONTINUOUS_MONITORING"
metadata.product_name
Set to "QUALYS_CONTINUOUS_MONITORING"
metadata.vendor_name
Set to "QUALYS_CONTINUOUS_MONITORING"
network.application_protocol
Parsed from log line "
/user
HTTP"
network.http.method
Parsed from log line "
/user HTTP"
timestamp
event.timestamp
Extracted from
Alert.eventDate
or
timestamp
fields.
Alert.eventDate
is prioritized if it exists, otherwise
timestamp
is used. The timestamp is converted to UTC.
Need more help?
Get answers from Community members and Google SecOps professionals.
