# Collect Google Cloud Compute context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-compute-context/  
**Scraped:** 2026-03-05T09:25:04.452744Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud Compute context logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Google Cloud Compute context logs into Google Security Operations using Cloud Storage. The parser extracts information from the logs in JSON format. It then normalizes and structures the extracted data into the Google SecOps UDM format, focusing on details about virtual machines like hardware specs, network configuration, security settings, and relationships to other entities.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Compute is set up and active in your Google Cloud environment.
Privileged access to Google Cloud and appropriate permissions.
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
compute-context-logs
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
Configure Google Cloud Compute logs export
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
Compute-Context-Sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://compute-context-logs/
.
Log Filter
:
logName
=
"*compute*"
resource.type
=
"gce_instance"
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
Set up feeds
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
How to set up the Google Cloud Compute Context feed
Click the
Google Cloud Compute platform
pack.
Locate the
GCP Compute Context
log type.
Specify the following values:
Source Type
: Google Cloud Storage V2.
Storage Bucket URI
: Cloud Storage bucket URL; for example,
gs://compute-context-logs/
. This URL must end with a trailing forward slash (/).
Source deletion options
: select the deletion option according to your preference.
Maximum File Age
: Files modified in the last number of days. Default is 180 days.
Chronicle Service Account
: Copy the Service Account. You'll need it to add permissions in the bucket for this Service Account to let Google SecOps read or delete data in the bucket.
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
ancestors
event.idm.entity.entity.asset.attribute.labels.value
Each ancestor value in the ancestors array is mapped to a separate label with the key
ancestors
.
assetType
event.idm.entity.entity.asset.category
Directly mapped from the assetType field.
asset_type
event.idm.entity.entity.asset.category
Directly mapped from the asset_type field.
name
event.idm.entity.entity.resource.name
Directly mapped from the name field.
resource.data.cpuPlatform
event.idm.entity.entity.asset.hardware.cpu_platform
Directly mapped from the resource.data.cpuPlatform field.
resource.data.creationTimestamp
event.idm.entity.entity.asset.attribute.creation_time
Parsed to a timestamp format from the resource.data.creationTimestamp field.
resource.data.id
event.idm.entity.entity.asset.product_object_id
Directly mapped from the resource.data.id field.
resource.data.labels.business_function
event.idm.entity.entity.asset.attribute.labels.value
Directly mapped from the resource.data.labels.business_function field, with the key set to
business_function
.
resource.data.labels.environment
event.idm.entity.entity.asset.attribute.labels.value
Directly mapped from the resource.data.labels.environment field, with the key set to
environment
.
resource.data.labels.infra_location
event.idm.entity.entity.asset.attribute.labels.value
Directly mapped from the resource.data.labels.infra_location field, with the key set to
infra_location
.
resource.data.labels.instance_group
event.idm.entity.user.group_identifiers
Directly mapped from the resource.data.labels.instance_group field.
resource.data.labels.os
event.idm.entity.entity.asset.platform_software.platform_version
Directly mapped from the resource.data.labels.os field.
resource.data.labels.primary_application
event.idm.entity.entity.asset.attribute.labels.value
Directly mapped from the resource.data.labels.primary_application field, with the key set to
primary_application
.
resource.data.labels.project_code
event.idm.entity.entity.asset.attribute.labels.value
Directly mapped from the resource.data.labels.project_code field, with the key set to
project_code
.
resource.data.lastStartTimestamp
event.idm.entity.entity.asset.last_boot_time
Parsed to a timestamp format from the resource.data.lastStartTimestamp field.
resource.data.machineType
event.idm.entity.entity.asset.hardware.model
The machine type is extracted from the resource.data.machineType field using a regular expression.
resource.data.name
event.idm.entity.entity.asset.hostname
Directly mapped from the resource.data.name field.
resource.data.networkInterfaces.0.accessConfigs.0.natIP
event.idm.entity.entity.asset.nat_ip
The first NAT IP address from the first network interface is mapped.
resource.data.networkInterfaces.0.network
event.idm.entity.entity.asset.attribute.cloud.vpc.name
The network ID is extracted from the resource.data.networkInterfaces.0.network field using a regular expression.
resource.data.networkInterfaces.0.networkIP
event.idm.entity.entity.asset.ip
The IP address of the first network interface is mapped.
resource.data.networkInterfaces.1.networkIP
event.idm.entity.entity.asset.ip
The IP address of the second network interface is mapped.
resource.data.selfLink
event.idm.entity.entity.url
Directly mapped from the resource.data.selfLink field.
resource.data.serviceAccounts.0.email
event.idm.entity.relations.entity.user.email_addresses
The email address of the first service account is mapped.
resource.data.status
event.idm.entity.entity.asset.deployment_status
Mapped to
ACTIVE
if the status is one of
RUNNING
,
PROVISIONING
,
STAGING
,
STOPPING
,
SUSPENDING
,
SUSPENDED
,
REPAIRING
,
TERMINATED
. Otherwise, mapped to
DEPLOYMENT_STATUS_UNSPECIFIED
.
event.idm.entity.entity.asset.attribute.cloud.availability_zone
The availability zone is constructed by combining the region and zone_suffix fields.
event.idm.entity.entity.asset.attribute.cloud.environment
Set to
GOOGLE_CLOUD_PLATFORM
.
event.idm.entity.entity.asset.attribute.cloud.project.name
The project ID is extracted from the name field using a regular expression.
event.idm.entity.entity.asset.attribute.cloud.project.resource_type
Set to
CLOUD_PROJECT
.
event.idm.entity.entity.asset.attribute.cloud.vpc.resource_type
Set to
VPC_NETWORK
.
event.idm.entity.entity.resource.resource_type
Set to
VIRTUAL_MACHINE
if asset_type or assetType contains
Instance
.
event.idm.entity.entity.resource.type
Set to
VIRTUAL_MACHINE
if asset_type or assetType contains
Instance
.
event.idm.entity.metadata.collected_timestamp
Set to the Logstash event timestamp.
event.idm.entity.metadata.entity_type
Set to
ASSET
.
event.idm.entity.metadata.product_name
Set to
GCP Compute Context
.
event.idm.entity.metadata.vendor_name
Set to
Google Cloud Platform
.
event.idm.entity.relations.entity.user.attribute.cloud.environment
Set to
GOOGLE_CLOUD_PLATFORM
.
event.idm.entity.relations.entity_type
Set to
USER
.
event.idm.entity.relations.relationship
Set to
ADMINISTERS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
