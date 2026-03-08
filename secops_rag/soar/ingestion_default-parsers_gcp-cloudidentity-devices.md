# Collect Cloud Identity Devices logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudidentity-devices/  
**Scraped:** 2026-03-05T09:53:07.300367Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloud Identity Devices logs
Supported in:
Google secops
SIEM
This document explains how to collect Cloud Identity Devices logs into 
Google SecOps using the
Third Party API
method, which is the 
recommended approach. The parser extracts fields from JSON logs, transforms 
specific fields like
deviceType
and dates, and maps them to the UDM, creating 
an
asset_entity
representing the device and enriching it with hardware and 
metadata information.
Before you begin
Ensure that you have the following prerequisites:
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
How to set up the Google Cloud Identity Devices feed
Click the
Google Cloud Compute platform
pack.
Locate the
Google Cloud Identity Devices
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
gcp-cloudidentity-devices-logs
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
section, either select a default storage class for the bucket, or select
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
Configure Cloud Identity Devices Logs Export
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
cloud-identity-devices-logs-sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-cloudidentity-devices-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudaudit.googleapis.com%2Factivity"
resource.type
=
"cloud_identity_device"
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
createTime
entity.metadata.creation_timestamp
The value of
createTime
is parsed as a timestamp and mapped.
deviceId
entity.entity.asset.asset_id
Directly mapped.
deviceType
entity.entity.asset.platform_software.platform
Mapped to
MAC
if the original value is
MAC_OS
or
IOS
. Mapped to
WINDOWS
,
MAC
, or
LINUX
if the original value matches. Otherwise, set to
UNKNOWN_PLATFORM
.
encryptionState
entity.entity.asset.attribute.labels.key
Value is set to
encryptionState
. Used as part of a label.
encryptionState
entity.entity.asset.attribute.labels.value
Directly mapped. Used as part of a label.
lastSyncTime
entity.entity.asset.system_last_update_time
The value of
lastSyncTime
is parsed as a timestamp and mapped.
managementState
entity.entity.asset.attribute.labels.key
Value is set to
managementState
. Used as part of a label.
managementState
entity.entity.asset.attribute.labels.value
Directly mapped. Used as part of a label.
model
entity.entity.asset.hardware.model
Directly mapped.
name
entity.entity.asset.product_object_id
The portion after
devices/
is extracted and mapped.
name
entity.entity.resource.name
Directly mapped.
osVersion
entity.entity.asset.platform_software.platform_version
Directly mapped.
securityPatchTime
entity.entity.asset.attribute.labels.key
Value is set to
securityPatchTime
. Used as part of a label.
securityPatchTime
entity.entity.asset.attribute.labels.value
Directly mapped. Used as part of a label.
serialNumber
entity.entity.asset.hardware.serial_number
Directly mapped. Copied from the top-level
create_time
field in the raw log.  Value is set to
ASSET
. Value is set to
GCP Cloud Identity Devices
. Value is set to
Google Cloud Platform
. Copied from the top-level
create_time
field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
