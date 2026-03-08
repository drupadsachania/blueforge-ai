# Collect Security Command Center Error logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-error/  
**Scraped:** 2026-03-05T09:59:47.142864Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Security Command Center Error logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Security Command Center Error logs into Google Security Operations using Cloud Storage. The parser transforms raw JSON formatted logs into a unified data model (UDM). It extracts relevant fields from the raw log, performs data cleaning and normalization, and structures the output according to the UDM schema for consistent security analysis.
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
gcp-scc-error-logs
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
Configure Security Command Center Error logs export
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
scc-error-logs-sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-scc-error-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudsecurityscanner.googleapis.com%2Ferror_logs"
resource.type
=
"security_command_center_error"
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
Security Command Center Error Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Security Command Center Error
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
gs://gcp-scc-error-logs
/. This URL must end with a trailing forward slash (/).
Source deletion options
: select the deletion option according to your preference.
Note: If you select the
Delete transferred files
or
Delete transferred files and empty directories
option, make sure that you granted appropriate permissions to the service account.
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
access.principalEmail
about.user.email_addresses
Value taken from the
access.principalEmail
field.
category
metadata.product_event_type
Value taken from the
category
or
findings.category
field depending on the log format.
contacts.security.contacts.email
security_result.about.user.email_addresses
Value taken from the
contacts.security.contacts.email
field. The role is set to
Security
.
contacts.technical.contacts.email
security_result.about.user.email_addresses
Value taken from the
contacts.technical.contacts.email
field. The role is set to
Technical
.
createTime
security_result.detection_fields.value
Value taken from the
createTime
or
findings.createTime
field depending on the log format. The key is set to
createTime
.
description
security_result.description
Value taken from the
description
or
findings.description
field depending on the log format.
eventTime
metadata.event_timestamp
Value taken from the
eventTime
or
findings.eventTime
field depending on the log format and converted to a timestamp.
externalUri
about.url
Value taken from the
externalUri
or
findings.externalUri
field depending on the log format.
findingClass
security_result.category_details
Value taken from the
findingClass
or
findings.findingClass
field depending on the log format.
findingProviderId
target.resource.attribute.labels.value
Value taken from the
findingProviderId
or
findings.findingProviderId
field depending on the log format. The key is set to
finding_provider_id
.
mute
security_result.detection_fields.value
Value taken from the
mute
or
findings.mute
field depending on the log format. The key is set to
mute
.
nextSteps
security_result.outcomes.value
Value taken from the
nextSteps
or
findings.nextSteps
field depending on the log format. The key is set to
nextSteps
.
resourceName
target.resource.name
Value taken from the
resourceName
,
findings.resourceName
,
resource_name
or
findings.resource_name
field depending on the log format.
securityMarks.name
security_result.detection_fields.value
Value taken from the
securityMarks.name
or
findings.securityMarks.name
field depending on the log format. The key is set to
securityMarks_name
.
severity
security_result.severity
Value taken from the
severity
or
findings.severity
field depending on the log format and mapped to the corresponding UDM severity level.
sourceDisplayName
target.resource.attribute.labels.value
Value taken from the
sourceDisplayName
or
findings.sourceDisplayName
field depending on the log format. The key is set to
source_display_name
.
sourceProperties.ReactivationCount
target.resource.attribute.labels.value
Value taken from the
sourceProperties.ReactivationCount
or
findings.sourceProperties.ReactivationCount
field depending on the log format. The key is set to
sourceProperties_ReactivationCount
.
state
security_result.detection_fields.value
Value taken from the
state
or
findings.state
field depending on the log format. The key is set to
state
.
metadata.event_type
Set to
GENERIC_EVENT
as a default value.
metadata.log_type
Hardcoded value
GCP_SECURITYCENTER_ERROR
.
metadata.description
Hardcoded value
Security Command Center
.
metadata.product_name
Hardcoded value
Security Command Center
.
metadata.vendor_name
Hardcoded value
Google
.
target.resource.attribute.labels.key
Hardcoded value
finding_id
.
target.resource.attribute.labels.value
Extracted from the
name
or
findings.name
field, capturing the last part after the last
/
character.
target.resource.product_object_id
Extracted from the
parent
or
findings.parent
field, capturing the value after the last
/
character.
target.resource.ancestors.name
Value taken from the
parent
or
findings.parent
field depending on the log format.
target.resource_ancestors.name
Extracted from the
resourceName
or
findings.resourceName
field, capturing the value after the
//cloudresourcemanager.googleapis.com/projects/
prefix.
target.resource_ancestors.resource_type
Hardcoded value
CLOUD_PROJECT
.
target.resource.attribute.labels.key
Hardcoded value
source_id
.
target.resource.attribute.labels.value
Extracted from the
parent
or
findings.parent
field, capturing the value after the second
/
character.
security_result.alert_state
Mapped based on the
state
or
findings.state
field. If the state is
ACTIVE
, the alert_state is set to
ALERTING
, otherwise
NOT_ALERTING
.
about.user.email_addresses
Value taken from the
iamBindings.member
field.
about.user.attribute.roles.name
Hardcoded value
Security
.
Need more help?
Get answers from Community members and Google SecOps professionals.
