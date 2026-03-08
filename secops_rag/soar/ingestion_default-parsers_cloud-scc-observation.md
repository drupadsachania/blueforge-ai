# Collect Security Command Center Observation logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-observation/  
**Scraped:** 2026-03-05T09:59:49.644880Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Security Command Center Observation logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Security Command Center Observation logs into Google Security Operations using Cloud Storage. The parser transforms raw JSON data into a unified data model (UDM). It normalizes the data structure, handling potential variations in the input, then extracts and maps relevant fields to the UDM schema, enriching the data with additional context and flags for downstream analysis.
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
gcp-scc-observation-logs
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
Configure Security Command Center Observation logs export
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
scc-observation-logs-sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-scc-observation-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudsecurityscanner.googleapis.com%2Fobservations"
resource.type
=
"security_command_center_observation"
logName
=
"projects/<your-project-id>/logs/cloudsecurityscanner.googleapis.com%2Ffindings"
resource.type
=
"security_center_findings"
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
Security Command Center Observation logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Security Command Center Observation
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
gs://gcp-scc-observation-logs/
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
access.callerIp
read_only_udm.principal.ip
Direct mapping.
access.callerIpGeo.regionCode
read_only_udm.principal.location.country_or_region
Direct mapping.
access.methodName
read_only_udm.additional.fields.value.string_value
Direct mapping. Also mapped to read_only_udm.target.labels.value.
access.principalEmail
read_only_udm.principal.user.email_addresses
Direct mapping.
access.principalSubject
read_only_udm.principal.user.attribute.labels.value
Direct mapping.
assetDisplayName
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
assetId
read_only_udm.target.asset.asset_id
The value after
assets/
is extracted from assetId field and mapped as
AssetID:<extracted_value>
.
category
read_only_udm.metadata.product_event_type
Direct mapping.
contacts.security.contacts.email
read_only_udm.security_result.about.user.email_addresses
Direct mapping. The
about
object can repeat multiple times based on the number of contacts. The
roles.name
field is set to
Security
for this field.
contacts.technical.contacts.email
read_only_udm.security_result.about.user.email_addresses
Direct mapping. The
about
object can repeat multiple times based on the number of contacts. The
roles.name
field is set to
Technical
for this field.
createTime
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields. The
key
field is set to
createTime
for this field.
eventTime
read_only_udm.metadata.event_timestamp
Converted to timestamp format.
externalUri
read_only_udm.about.url
Direct mapping.
findingClass
read_only_udm.security_result.category_details
Direct mapping.
findingProviderId
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
mitreAttack.primaryTactic
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields. The
key
field is set to
primary_tactic
for this field.
mitreAttack.primaryTechniques
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the number of techniques. The
key
field is set to
primary_technique
for this field.
mute
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields. The
key
field is set to
mute
for this field.
name
read_only_udm.metadata.product_log_id
Direct mapping.
parentDisplayName
read_only_udm.metadata.description
Direct mapping.
resource.display_name
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
resource.name
read_only_udm.target.resource.name, read_only_udm.principal.resource.name
Direct mapping. When this field is used to populate the
principal.resource.name
field, the parser will check if
resource.project_name
is empty. If it's not empty, it will use
resource.project_name
instead.
resource.parent_display_name
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
resource.parent_name
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
resource.project_display_name
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
resource.project_name
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
resource.type
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
resourceName
read_only_udm.target.resource.name
Direct mapping.
securityMarks.name
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields. The
key
field is set to
securityMarks_name
for this field.
severity
read_only_udm.security_result.severity, read_only_udm.security_result.priority_details
Direct mapping.
sourceDisplayName
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
sourceProperties.contextUris.mitreUri.displayName
read_only_udm.security_result.detection_fields.key
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields.
sourceProperties.contextUris.mitreUri.url
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields.
sourceProperties.detectionCategory.ruleName
read_only_udm.security_result.rule_name
Direct mapping.
sourceProperties.detectionCategory.subRuleName
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields. The
key
field is set to
sourceProperties_detectionCategory_subRuleName
for this field.
sourceProperties.detectionPriority
read_only_udm.security_result.priority_details
Direct mapping.
sourceProperties.findingId
read_only_udm.target.resource.attribute.labels.value
Direct mapping.
state
read_only_udm.security_result.detection_fields.value
Direct mapping. The
detection_fields
object can repeat multiple times based on the available fields. The
key
field is set to
state
for this field.
N/A
read_only_udm.metadata.log_type
Hardcoded to
GCP_SECURITYCENTER_OBSERVATION
.
N/A
read_only_udm.metadata.product_name
Hardcoded to
Security Command Center
.
N/A
read_only_udm.metadata.vendor_name
Hardcoded to
Google
.
N/A
read_only_udm.principal.user.account_type
Set to CLOUD_ACCOUNT_TYPE if principal email is present.
N/A
read_only_udm.security_result.alert_state
Hardcoded to
ALERTING
.
N/A
read_only_udm.security_result.priority
Set to LOW_PRIORITY if severity is
LOW
.
N/A
read_only_udm.target.application
Extracted from resourceName field.
N/A
read_only_udm.target.resource.product_object_id
Extracted from parent field.
N/A
read_only_udm.target.resource.resource_type
Set to
CLUSTER
by default. Set to
VIRTUAL_MACHINE
if category is
Impact: GPU Instance Created
or
Impact: Many Instances Created
. Set to
SETTING
if category is
Persistence: Add Sensitive Role
.
N/A
read_only_udm.target.resource_ancestors.name
Extracted from parent and resourceName fields.
N/A
read_only_udm.target.resource_ancestors.product_object_id
Extracted from parent, resource.project_name, and resourceName fields.
N/A
read_only_udm.target.resource_ancestors.resource_type
Set to CLOUD_PROJECT if resource.type is
google.compute.Project
.
N/A
read_only_udm.target.labels.key
The value is set to
access_methodName
if
access.methodName
is present.
N/A
read_only_udm.target.labels.value
The value is set from
access.methodName
.
N/A
read_only_udm.target.resource.attribute.labels.key
The key is set to one of the following values based on the available field:
resource_parentDisplayName
,
resource_type
,
resource_parentName
,
resource_projectDisplayName
,
resource_displayName
,
finding_id
,
source_id
,
FindingProviderId
,
sourceDisplayName
,
asset_display_name
.
N/A
read_only_udm.target.resource.attribute.labels.value
The value is set from one of the following fields based on the available field: parentDisplayName, resource.type, resource.parent_name, resource.project_display_name, resource.display_name, sourceProperties.findingId, sourceProperties.sourceId, findingProviderId, sourceDisplayName, assetDisplayName.
Need more help?
Get answers from Community members and Google SecOps professionals.
