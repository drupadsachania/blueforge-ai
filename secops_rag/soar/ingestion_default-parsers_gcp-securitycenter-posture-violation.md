# Collect Security Command Center Posture Violation logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-securitycenter-posture-violation/  
**Scraped:** 2026-03-05T09:59:51.266728Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Security Command Center Posture Violation logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Security Command Center Posture Violation logs into Google Security Operations using Cloud Storage. The parser transforms raw JSON data from findings into a unified data model (UDM). It extracts relevant fields, restructures the data, maps it to UDM fields, and performs various validations and enrichments to ensure data quality and consistency.
Before you begin
Ensure that you have the following prerequisites:
Security Command Center is enabled in your Google Cloud environment.
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
gcp-scc-posture-violation-logs
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
Configure Security Command Center Posture Violation logs export
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
scc-posture-violation-logs-sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-scc-posture-violation-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudsecurityscanner.googleapis.com%2Fposture_violations"
resource.type
=
"cloud_security_center_posture_violation"
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
Security Command Center Posture Violation Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Security Command Center Posture Violation
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
gs://gcp-scc-posture-violation-logs/
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
category
read_only_udm.metadata.product_event_type
Direct mapping.
changed_policy
read_only_udm.security_result.rule_name
Direct mapping.
cloudProvider
read_only_udm.target.resource.attribute.cloud.environment
Direct mapping.
createTime
read_only_udm.security_result.detection_fields[
createTime
]
Direct mapping.
finding.risks.riskCategory
read_only_udm.security_result.detection_fields[
risk_category
]
Direct mapping.
mute
read_only_udm.security_result.detection_fields[
mute
]
Direct mapping.
name
read_only_udm.metadata.product_log_id
Direct mapping.
originalProviderId
read_only_udm.target.resource.attribute.labels[
original_provider_id
]
Direct mapping.
parent
read_only_udm.target.resource_ancestors[0].name
Direct mapping.
parentDisplayName
read_only_udm.metadata.description
Direct mapping.
propertyDataTypes.changed_policy.primitiveDataType
read_only_udm.security_result.rule_labels[
changed_policy_primitive_data_type
]
Direct mapping.
propertyDataTypes.policy_drift_details.listValues.propertyDataTypes[0].structValue.fields.drift_details.structValue.fields.detected_configuration.primitiveDataType
read_only_udm.security_result.rule_labels[
detected_configuration_primitive_data_type
]
Direct mapping.
propertyDataTypes.policy_drift_details.listValues.propertyDataTypes[0].structValue.fields.drift_details.structValue.fields.expected_configuration.primitiveDataType
read_only_udm.security_result.rule_labels[
expected_configuration_primitive_data_type
]
Direct mapping.
propertyDataTypes.policy_drift_details.listValues.propertyDataTypes[0].structValue.fields.field_name.primitiveDataType
read_only_udm.security_result.rule_labels[
field_name_primitive_data_type
]
Direct mapping.
propertyDataTypes.posture_deployment_name.primitiveDataType
read_only_udm.security_result.detection_fields[
posture_deployment_name_primitiveDataType
]
Direct mapping.
propertyDataTypes.posture_deployment_resource.primitiveDataType
read_only_udm.security_result.detection_fields[
posture_deployment_resource_primitiveDataType
]
Direct mapping.
propertyDataTypes.posture_name.primitiveDataType
read_only_udm.security_result.detection_fields[
posture_name_primitiveDataType
]
Direct mapping.
propertyDataTypes.posture_revision_id.primitiveDataType
read_only_udm.security_result.detection_fields[
posture_revision_id_primitiveDataType
]
Direct mapping.
resource.cloudProvider
read_only_udm.target.resource.attribute.cloud.environment
Direct mapping.
resource.displayName
read_only_udm.target.resource.attribute.labels[
resource_displayName
]
Direct mapping.
resource.gcpMetadata.organization
read_only_udm.target.resource.attribute.labels[
resource_organization
]
Direct mapping.
resource.gcpMetadata.parent
read_only_udm.target.resource.attribute.labels[
resource_parent
]
Direct mapping.
resource.gcpMetadata.parentDisplayName
read_only_udm.target.resource.attribute.labels[
resource_parentDisplayName
]
Direct mapping.
resource.gcpMetadata.project
read_only_udm.target.resource.attribute.labels[
resource_project
]
Direct mapping.
resource.gcpMetadata.projectDisplayName
read_only_udm.target.resource.attribute.labels[
resource_projectDisplayName
]
Direct mapping.
resource.organization
read_only_udm.target.resource.attribute.labels[
resource_organization
]
Direct mapping.
resource.resourcePath.nodes.displayName
read_only_udm.target.resource_ancestors.name
Direct mapping.
resource.resourcePath.nodes.id
read_only_udm.target.resource_ancestors.product_object_id
Direct mapping.
resource.resourcePath.nodes.nodeType
read_only_udm.target.resource_ancestors.resource_subtype
Direct mapping.
resource.resourcePathString
read_only_udm.target.resource.attribute.labels[
resource_path_string
]
Direct mapping.
resource.service
read_only_udm.target.resource_ancestors[10].name
Direct mapping.
resource.type
read_only_udm.target.resource.attribute.labels[
resource_type
]
Direct mapping.
resourceName
read_only_udm.target.resource.name
Direct mapping.
securityPosture.changedPolicy
read_only_udm.security_result.rule_labels[
changed_policy
]
Direct mapping.
securityPosture.name
read_only_udm.security_result.detection_fields[
security_posture_name
]
Direct mapping.
securityPosture.policyDriftDetails[0].detectedValue
read_only_udm.security_result.rule_labels[
policy_drift_details_detected_value
]
Direct mapping.
securityPosture.policyDriftDetails[0].expectedValue
read_only_udm.security_result.rule_labels[
policy_drift_details_expected_value
]
Direct mapping.
securityPosture.policyDriftDetails[0].field
read_only_udm.security_result.rule_labels[
policy_drift_details_field
]
Direct mapping.
securityPosture.policySet
read_only_udm.security_result.rule_set
Direct mapping.
securityPosture.postureDeployment
read_only_udm.security_result.detection_fields[
posture_deployment
]
Direct mapping.
securityPosture.postureDeploymentResource
read_only_udm.security_result.detection_fields[
posture_deployment_resource
]
Direct mapping.
securityPosture.revisionId
read_only_udm.security_result.detection_fields[
security_posture_revision_id
]
Direct mapping.
severity
read_only_udm.security_result.severity
Direct mapping.
sourceProperties.categories[0]
read_only_udm.security_result.detection_fields[
source_properties_categories
]
Direct mapping.
sourceProperties.changed_policy
read_only_udm.security_result.rule_name
Direct mapping.
sourceProperties.name
read_only_udm.target.application
Direct mapping.
sourceProperties.policy_drift_details[0].drift_details.detected_configuration
read_only_udm.security_result.rule_labels[
policy_drift_details_detected_configuration
]
Direct mapping.
sourceProperties.policy_drift_details[0].drift_details.expected_configuration
read_only_udm.security_result.rule_labels[
policy_drift_details_expected_configuration
]
Direct mapping.
sourceProperties.policy_drift_details[0].field_name
read_only_udm.security_result.rule_labels[
policy_drift_details_field_name
]
Direct mapping.
sourceProperties.posture_deployment
read_only_udm.security_result.detection_fields[
source_properties_posture_deployment_name
]
Direct mapping.
sourceProperties.posture_deployment_name
read_only_udm.security_result.detection_fields[
source_properties_posture_deployment_name
]
Direct mapping.
sourceProperties.posture_deployment_resource
read_only_udm.security_result.detection_fields[
source_properties_posture_deployment_resource
]
Direct mapping.
sourceProperties.posture_name
read_only_udm.target.application
Direct mapping.
sourceProperties.posture_revision_id
read_only_udm.security_result.detection_fields[
source_properties_posture_revision_id
]
Direct mapping.
sourceProperties.revision_id
read_only_udm.security_result.detection_fields[
source_properties_posture_revision_id
]
Direct mapping.
state
read_only_udm.security_result.detection_fields[
state
]
Direct mapping.
read_only_udm.metadata.vendor_name
The parser maps the static value
Google
.
read_only_udm.metadata.product_name
The parser maps the static value
Security Command Center
.
read_only_udm.target.resource.resource_type
The parser maps the static value
CLUSTER
.
read_only_udm.security_result.about.investigation.status
The parser maps the static value
NEW
.
read_only_udm.security_result.alert_state
The parser maps the static value
ALERTING
.
read_only_udm.metadata.event_type
The parser maps to
GENERIC_EVENT
as default value. If the field 'category' equals to 'SECURITY_POSTURE_DRIFT' and 'client_device_present' and 'token_target.application' are not empty, it maps to 'SERVICE_MODIFICATION'. If the field 'category' equals to 'SECURITY_POSTURE_POLICY_DRIFT', 'SECURITY_POSTURE_POLICY_DELETE', 'SECURITY_POSTURE_DETECTOR_DRIFT' or 'SECURITY_POSTURE_DETECTOR_DELETE' and 'network_edr_not_present' is false and 'client_device_present' is true, it maps to 'SCAN_UNCATEGORIZED'. If the field 'token_metadata.event_type' equals to 'GENERIC_EVENT' and 'network_edr_not_present' is false and 'client_device_present' is true, it maps to 'STATUS_UPDATE'.
read_only_udm.target.resource_ancestors[1].resource_type
The parser maps the static value
CLOUD_PROJECT
.
read_only_udm.target.resource.product_object_id
The parser extracts the value from the 'parent' field, between the second and third '/' characters.
read_only_udm.target.resource_ancestors[1].name
The parser extracts the value from the 'resourceName' field, between the fourth and fifth '/' characters.
read_only_udm.security_result.url_back_to_product
The parser dynamically builds the URL using the organization, source, and finding IDs extracted from the log.
securityMarks.name
read_only_udm.security_result.detection_fields[
securityMarks_name
]
Direct mapping.
Need more help?
Get answers from Community members and Google SecOps professionals.
