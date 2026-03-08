# Collect Qualys asset context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-asset-context/  
**Scraped:** 2026-03-05T09:27:36.065045Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Qualys asset context logs
Supported in:
Google secops
SIEM
This parser extracts asset context information from Qualys JSON logs and transforms it into the UDM format. It parses various fields such as ID, IP, hostname, cloud resource details, OS, and tags, mapping them to corresponding UDM fields and creating relationships between assets and resources. The parser also handles specific logic for cloud providers and operating systems, ensuring accurate representation in the UDM.
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
role on the Cloud Storage bucket you created in the previous step.
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
fetch-qualys-assets
).
Region
: select a region close to your Bucket.
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
# Cloud Storage configuration
BUCKET_NAME
=
"<bucket-name>"
FILE_NAME
=
"qualys_assets.json"
# Qualys API credentials
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
fetch_qualys_assets
():
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
<Criteria field="asset.name" operator="LIKE">%</Criteria>
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
/qps/rest/2.0/search/am/asset"
,
headers
=
headers
,
data
=
payload
)
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
assets
=
fetch_qualys_assets
()
upload_to_gcs
(
assets
)
return
"Data uploaded to Cloud Storage successfully!"
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
trigger-fetch-qualys-assets
).
Frequency
: use
cron
syntax to specify the schedule (for example, 0 0 * * * for daily at midnight).
Time Zone
: set your preferred time zone.
Trigger Type
: Choose
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
Qualys Asset Context Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Qualys Asset Context
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
GCS URI
: the Cloud Storage URI.
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
ASSET_ID
entity.entity.asset.asset_id
Directly mapped from the
ASSET_ID
field.
CLOUD_PROVIDER
entity.relations.entity.resource.resource_subtype
Directly mapped from the
CLOUD_PROVIDER
field.
CLOUD_PROVIDER_TAGS.CLOUD_TAG[].NAME
entity.relations.entity.resource.attribute.labels.key
Directly mapped from the
CLOUD_PROVIDER_TAGS.CLOUD_TAG[].NAME
field.
CLOUD_PROVIDER_TAGS.CLOUD_TAG[].VALUE
entity.relations.entity.resource.attribute.labels.value
Directly mapped from the
CLOUD_PROVIDER_TAGS.CLOUD_TAG[].VALUE
field.
CLOUD_RESOURCE_ID
entity.relations.entity.resource.id
Directly mapped from the
CLOUD_RESOURCE_ID
field.
CLOUD_SERVICE
entity.relations.entity.resource.resource_type
If
CLOUD_SERVICE
is "VM", the value is set to "VIRTUAL_MACHINE".
DNS_DATA.HOSTNAME
entity.entity.asset.hostname
Directly mapped from the
DNS_DATA.HOSTNAME
field.
EC2_INSTANCE_ID
entity.relations.entity.resource.product_object_id
Directly mapped from the
EC2_INSTANCE_ID
field.
ID
entity.entity.asset.product_object_id
Directly mapped from the
ID
field.
IP
entity.entity.asset.ip
Directly mapped from the
IP
field.
METADATA.AZURE.ATTRIBUTE[].NAME
entity.relations.entity.resource.attribute.labels.key
Directly mapped from the
METADATA.AZURE.ATTRIBUTE[].NAME
field.
METADATA.AZURE.ATTRIBUTE[].VALUE
entity.relations.entity.resource.attribute.labels.value
Directly mapped from the
METADATA.AZURE.ATTRIBUTE[].VALUE
field.
OS
entity.entity.asset.platform_software.platform
If
OS
contains "windows" (case-insensitive), the value is set to "WINDOWS".
TAGS.TAG[].NAME
entity.relations.entity.resource.attribute.labels.key
Directly mapped from the
TAGS.TAG[].NAME
field.
TAGS.TAG[].TAG_ID
entity.relations.entity.resource.attribute.labels.value
Concatenated string "TAG_ID: " with the value of
TAGS.TAG[].TAG_ID
. Copied from the
create_time
field of the raw log.  Hardcoded to "ASSET". Hardcoded to "QUALYS ASSET CONTEXT". Hardcoded to "QUALYS ASSET CONTEXT". Hardcoded to "RESOURCE". Hardcoded to "MEMBER". Copied from the
create_time
field of the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
