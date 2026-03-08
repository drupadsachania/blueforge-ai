# Collect Security Command Center Unspecified logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-unspecified/  
**Scraped:** 2026-03-05T10:00:00.288702Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Security Command Center Unspecified logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Security Command Center Unspecified logs into Google Security Operations using Cloud Storage. The parser transforms raw JSON formatted security findings into a unified data model (UDM). It specifically handles inconsistencies in the input data structure, extracts relevant fields like vulnerability details and user information, and enriches the output with labels and metadata for improved analysis and correlation.
Before you begin
Ensure that you have the following prerequisites:
Security Command Center is enabled and configured in your Google Cloud environment.
Google SecOps instance.
Privileged access to Security Command Center and Cloud Logging.
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
gcp-scc-unspecified-logs
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
Configure Security Command Center logging
Sign in to the
Google Cloud console
.
Go to the
Security Command Center
page.
Go to Security Command Center
Select your organization.
Click
Settings
.
Click the
Continuous Exports
tab.
Under
Export name
, click
Logging Export
.
Under
Sinks
, turn on
Log Findings to Logging
.
Under
Logging project
, enter or search for the project where you want to log findings.
Click
Save
.
Configure Security Command Center Unspecified Logs Export
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
scc-unspecified-logs-sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-scc-unspecified-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudsecurityscanner.googleapis.com%2Funspecified"
resource.type
=
"security_command_center_unspecified"
Set Export Options
: Include all log entries.
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
Security Command Center Unspecified logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Security Command Center Unspecified
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
gs://gcp-scc-unspecified-logs/
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
canonicalName
read_only_udm.target.resource_ancestors.name
Directly mapped from the raw log field
canonicalName
. This represents the ancestor of the target resource.
category
read_only_udm.metadata.product_event_type
Directly mapped from the raw log field
category
.
category
read_only_udm.metadata.event_type
Derived from the
category
field. If the category is
OPEN_FIREWALL
and certain conditions are met, it's mapped to
SCAN_VULN_HOST
. Otherwise, it defaults to
GENERIC_EVENT
.
category
read_only_udm.security_result.category
Mapped from the raw log field
category
. If the category is
OPEN_FIREWALL
, it's mapped to
POLICY_VIOLATION
.
complies.ids
read_only_udm.additional.fields.value.string_value
Directly mapped from the raw log field
complies.ids
. Represents the compliance ID.
complies.standard
read_only_udm.additional.fields.value.string_value
Directly mapped from the raw log field
complies.standard
. Represents the compliance standard.
complies.standard
read_only_udm.about.labels.value
Directly mapped from the raw log field
complies.standard
. Represents the compliance standard.
contacts.security.contacts.email
read_only_udm.security_result.about.user.email_addresses
Directly mapped from the raw log field
contacts.security.contacts.email
. Represents the email address of the security contact.
contacts.technical.contacts.email
read_only_udm.security_result.about.user.email_addresses
Directly mapped from the raw log field
contacts.technical.contacts.email
. Represents the email address of the technical contact.
createTime
read_only_udm.security_result.detection_fields.value
Directly mapped from the raw log field
createTime
.
eventTime
read_only_udm.metadata.event_timestamp
Directly mapped from the raw log field
eventTime
after converting to a timestamp.
externalUri
read_only_udm.about.url
Directly mapped from the raw log field
externalUri
.
mute
read_only_udm.security_result.detection_fields.value
Directly mapped from the raw log field
mute
.
muteInitiator
read_only_udm.security_result.detection_fields.value
Directly mapped from the raw log field
muteInitiator
.
muteUpdateTime
read_only_udm.security_result.detection_fields.value
Directly mapped from the raw log field
muteUpdateTime
.
name
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
name
. This will be used as the finding ID.
parent
read_only_udm.target.resource_ancestors.name
Directly mapped from the raw log field
parent
.
parentDisplayName
read_only_udm.metadata.description
Directly mapped from the raw log field
parentDisplayName
.
resourceName
read_only_udm.target.resource.name
Directly mapped from the raw log field
resourceName
.
severity
read_only_udm.security_result.severity
Directly mapped from the raw log field
severity
.
sourceDisplayName
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
sourceDisplayName
.
sourceProperties.AllowedIpRange
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
sourceProperties.AllowedIpRange
.
sourceProperties.ExternallyAccessibleProtocolsAndPorts.IPProtocol
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
sourceProperties.ExternallyAccessibleProtocolsAndPorts.IPProtocol
.
sourceProperties.ExternallyAccessibleProtocolsAndPorts.ports
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
sourceProperties.ExternallyAccessibleProtocolsAndPorts.ports
.
sourceProperties.ReactivationCount
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
sourceProperties.ReactivationCount
.
sourceProperties.ResourcePath
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the raw log field
sourceProperties.ResourcePath
. The values are concatenated into a single string.
sourceProperties.ScannerName
read_only_udm.additional.fields.value.string_value
Directly mapped from the raw log field
sourceProperties.ScannerName
.
sourceProperties.ScannerName
read_only_udm.principal.labels.value
Directly mapped from the raw log field
sourceProperties.ScannerName
.
state
read_only_udm.security_result.detection_fields.value
Directly mapped from the raw log field
state
.
read_only_udm.metadata.log_type
Hardcoded to
GCP_SECURITYCENTER_UNSPECIFIED
in the parser code.
read_only_udm.metadata.product_log_id
Extracted from the
name
field, representing the finding ID.
read_only_udm.metadata.product_name
Hardcoded to
Security Command Center
in the parser code.
read_only_udm.metadata.vendor_name
Hardcoded to
Google
in the parser code.
read_only_udm.security_result.about.investigation.status
Hardcoded to
NEW
in the parser code.
read_only_udm.security_result.alert_state
Hardcoded to
NOT_ALERTING
in the parser code.
read_only_udm.security_result.url_back_to_product
Constructed in the parser code using the format:
https://console.cloud.google.com/security/command-center/findingsv2;name=organizations%2F{organization_id}%2Fsources%2F{source_id}%2Ffindings%2F{finding_id}
.
read_only_udm.target.resource.product_object_id
Extracted from the
parent
field in the raw log, representing the source ID.
read_only_udm.target.resource.resource_type
Set to
CLUSTER
in the parser code.
read_only_udm.target.resource_ancestors.resource_type
Hardcoded to
CLOUD_PROJECT
in the parser code.
read_only_udm.target.resource_ancestors.name
Extracted from the
resourceName
field in the raw log, representing the project ID.
read_only_udm.additional.fields.key
Several instances are created with hardcoded keys:
compliances_id_0_0
,
compliances_standard_0
,
sourceProperties_ScannerName
.
read_only_udm.about.labels.key
Hardcoded to
compliances_standard
and
compliances_id
in the parser code.
read_only_udm.principal.labels.key
Hardcoded to
sourceProperties_ScannerName
in the parser code.
read_only_udm.target.resource.attribute.labels.key
Several instances are created with hardcoded keys:
finding_id
,
source_id
,
sourceProperties_ResourcePath
,
sourceDisplayName
,
sourceProperties_ReactivationCount
,
sourceProperties_AllowedIpRange
,
sourceProperties_ExternallyAccessibleProtocolsAndPorts_IPProtocol
,
sourceProperties_ExternallyAccessibleProtocolsAndPorts_ports
.
read_only_udm.security_result.about.user.attribute.roles.name
Two instances are created, one with the value
Security
and the other with
Technical
, based on the
contacts
field in the raw log.
read_only_udm.security_result.detection_fields.key
Several instances are created with hardcoded keys:
mute
,
mute_update_time
,
mute_initiator
,
createTime
,
state
.
Need more help?
Get answers from Community members and Google SecOps professionals.
