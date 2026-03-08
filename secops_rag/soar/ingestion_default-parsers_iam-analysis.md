# Collect Identity and Access Management (IAM) Analysis context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iam-analysis/  
**Scraped:** 2026-03-05T09:57:06.486397Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Identity and Access Management (IAM) Analysis context logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest IAM Analysis logs into Google Security Operations using Cloud Storage. The parser extracts user and resource information from IAM JSON data. It then maps the extracted fields to the UDM, creating user entities with associated roles and resource relationships, ultimately enriching security context within the Google SecOps platform.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
IAM is set up and active in your Google Cloud environment.
Privileged access to Google Cloud and appropriate permissions to access IAM logs.
Create a Cloud Storage bucket
Sign in to the
Google Cloud console
.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
On the
Create a bucket
page, enter your bucket information. After each of the following steps, click
Continue
to proceed to the next step:
In the
Get started
section, do the following:
Enter a unique name that meets the bucket name requirements; for example,
google-cloud-iam-logs
.
To enable hierarchical namespace, click the expander arrow to expand the
Optimize for file oriented and data-intensive workloads
section, and then select
Enable Hierarchical namespace on this bucket
.
To add a bucket label, click the expander arrow to expand the
Labels
section.
Click
Add label
, and specify a key and a value for your label.
In the
Choose where to store your data
section, do the following:
Select a
Location type
.
Use the location type menu to select a
Location
where object data within your bucket will be permanently stored.
To set up cross-bucket replication, expand the
Set up cross-bucket replication
section.
In the
Choose a storage class for your data
section, either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management of your bucket's data.
In the
Choose how to control access to objects
section, select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the expander arrow labeled
Data encryption
, and select a
Data encryption method
.
Click
Create
.
Configure IAM Analysis logs export
Sign in to the
Google Cloud console
.
Go to
Logging
>
Log Router
.
Click
Create Sink
.
Provide the following configuration parameters:
Sink Name
: enter a meaningful name; for example,
IAM-Analysis-Sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-iam-analysis-logs/
.
Log Filter
:
logName
=
"*iam*"
resource.type
=
"gce_instance"
Configure permissions for Cloud Storage
Go to
IAM & Admin
>
IAM
.
Locate the
Cloud Logging
service account.
Grant the
roles/storage.admin
on the bucket.
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
IAM Analysis Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
GCP IAM Analysis
as the
Log type
.
Click
Get Service Account
next to the
Chronicle Service Account
field.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Cloud Storage bucket URL; for example,
gs://gcp-iam-analysis-logs/
. This URL must end with a trailing forward slash (/).
Source deletion options
: select the deletion option according to your preference.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
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
accessControlLists.accesses.permission
relations.entity.resource.attribute.permissions.name
Directly from the
accessControlLists.accesses.permission
field in the raw log.
attachedResourceFullName
relations.entity.resource.name
Directly from the
attachedResourceFullName
field in the raw log, but with any trailing resource names removed.
relations.entity.resource.attribute.cloud.environment
Set to
GOOGLE_CLOUD_PLATFORM
.
relations.entity.resource.product_object_id
For STORAGE_BUCKET, directly from the
attachedResourceFullName
field in the raw log, but with any trailing resource names removed. For BigQuery datasets, it's the
projectName
(extracted from
attachedResourceFullName
) followed by a colon and the
datasetName
(extracted from
attachedResourceFullName
) field.
relations.entity.resource.resource_type
Determined by the pattern of the
attachedResourceFullName
field in the raw log.
relations.entity_type
Set to
RESOURCE
, except for SERVICE_ACCOUNT, where it's set to
USER
.
relations.relationship
Set to
MEMBER
.
metadata.collected_timestamp
Directly from the
timestamp
field in the raw log.
metadata.entity_type
Set to
USER
.
metadata.product_name
Set to
GCP IAM ANALYSIS
.
metadata.vendor_name
Set to
Google Cloud Platform
.
iamBinding.role
entity.user.attribute.roles.name
Directly from the
iamBinding.role
field in the raw log.
identityList.identities.name
entity.user.attribute.roles.type
Set to
SERVICE_ACCOUNT
if the
identityList.identities.name
field contains the string
serviceAccount
.
entity.user.email_addresses
If the
identityList.identities.name
field contains an
@
symbol, it's treated as an email address.
entity.user.userid
If the
identityList.identities.name
field doesn't contain an
@
symbol, it's treated as a userid.
identityList.identities.product_object_id
entity.user.product_object_id
Directly from the
identityList.identities.product_object_id
field in the raw log.
timestamp
timestamp
Directly from the
timestamp
field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
