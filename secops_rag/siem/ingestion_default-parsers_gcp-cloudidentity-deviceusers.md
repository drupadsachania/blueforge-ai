# Collect Cloud Identity Device Users logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudidentity-deviceusers/  
**Scraped:** 2026-03-05T09:22:10.007172Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloud Identity Device Users logs
Supported in:
Google secops
SIEM
This document explains how to collect Cloud Identity Device Users logs 
into Google Security Operations using the
Third Party API
method, which is the 
recommended approach. The parser first extracts data from JSON formatted
Cloud Identity Device Users
logs and transforms the timestamp to the 
standardized format. Then, it maps specific fields from the raw log data to the 
corresponding fields in the unified data model (UDM) for user entities, their 
relationships to assets, and additional user attributes like management and 
password states.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Domain-Wide Delegation setup
for a Service Account. The Service Account must be authorized for the following scope:
https://www.googleapis.com/auth/cloud-identity.devices.readonly
The following APIs are enabled in your Google Cloud project:
Cloud Identity API
Google Workspace Admin SDK
Alert Center API
Recommended: Set up Third Party API Feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the Google Cloud Identity Device Users feed
Click the
Google Cloud Compute platform
pack.
Locate the
Google Cloud Identity Device Users
log type and click
Add new feed
.
Specify values for the following fields:
Source Type
: Select
Third party API
.
OAuth JWT endpoint
: Enter the OAuth token endpoint:
https://oauth2.googleapis.com/token
JWT claims issuer
: Enter the Enter the
email address
of the Service Account (found in the Service Account's JSON key file).
JWT claims subject
: Enter the email address of the user who is granted the role of
services admin
or
super admin
in the Workspace console (the user being impersonated through Domain-Wide Delegation).
JWT claims audience
: Enter the endpoint again:
https://oauth2.googleapis.com/token
RSA private key
: Paste the full contents of the
private key
from the Service Account's JSON key file (including the
-----BEGIN PRIVATE KEY-----
and
-----END PRIVATE KEY-----
lines).
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Alternate Method: Ingestion via Cloud Storage
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
gcp-cloudidentity-users-logs
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
section, clear
Enforce public access prevention
, and select an
Access control
model for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the expander arrow labeled
Data encryption
, and select a data encryption method.
Click
Create
.
Configure Cloud Identity Device Users logs export
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
Cloudidentity-Users-Sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-cloudidentity-users-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudaudit.googleapis.com%2Factivity"
resource.type
=
"cloud_identity_user"
Set Export Options
: include all log entries.
Click
Create
.
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
collection_time.nanos
timestamp.nanos
Directly mapped from the log field. Represents the event timestamp in nanoseconds.
collection_time.seconds
timestamp.seconds
Directly mapped from the log field. Represents the event timestamp in seconds.
createTime
entity.metadata.creation_timestamp
Directly mapped from the log field after being parsed by the
date
filter. Represents the creation timestamp of the user.
managementState
entity.additional.fields.value.string_value
Directly mapped from the log field. Represents the management state of the user.
name
entity.entity.resource.name
Directly mapped from the log field. Represents the full resource name of the device user.
passwordState
entity.additional.fields.value.string_value
Directly mapped from the log field. Represents the password state of the user. This field is only mapped if the
passwordState
field exists in the raw log.
userEmail
entity.entity.user.email_addresses
Directly mapped from the log field. Represents the email address of the user.
entity.additional.fields.key
Set to a constant value
Management State
within the parser. This field is used to provide context to the
managementState
value.
entity.additional.fields.key
Set to a constant value
Password State
within the parser. This field is used to provide context to the
passwordState
value and is only present if
passwordState
exists in the raw log.
entity.entity.user.product_object_id
Extracted from the
name
field using the
grok
filter, capturing the
deviceuser_id
portion. Represents the unique identifier of the device user.
entity.metadata.collected_timestamp.nanos
Copied from
collection_time.nanos
. Represents the timestamp when the log was collected.
entity.metadata.collected_timestamp.seconds
Copied from
collection_time.seconds
. Represents the timestamp when the log was collected.
entity.metadata.entity_type
Set to a constant value
USER
within the parser.
entity.metadata.product_name
Set to a constant value
GCP Cloud Identity Device Users
within the parser.
entity.metadata.vendor_name
Set to a constant value
Google Cloud Platform
within the parser.
relations.entity.asset.product_object_id
Extracted from the
name
field using the
grok
filter, capturing the
device_id
portion. Represents the unique identifier of the device.
relations.entity_type
Set to a constant value
ASSET
within the parser.
relations.relationship
Set to a constant value
MEMBER
within the parser.
Need more help?
Get answers from Community members and Google SecOps professionals.
