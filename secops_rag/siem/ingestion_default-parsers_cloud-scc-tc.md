# Collect Security Command Center Toxic Combination logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-tc/  
**Scraped:** 2026-03-05T09:28:03.660723Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Security Command Center Toxic Combination logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Security Command Center Toxic Combination logs into Google Security Operations using Cloud Storage. The parser extracts and structures security finding data from JSON logs. It normalizes the data into a unified data model (UDM), handling different data formats and enriching it with additional context like network information and user agent details.
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
gcp-scc-toxic-combination-logs
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
Configure Security Command Center Toxic Combination logs export
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
scc-toxic-combination-logs-sink
.
Sink Destination
: select
Cloud Storage Storage
and enter the URI for your bucket; for example,
gs://gcp-scc-toxic-combination-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloudsecurityscanner.googleapis.com%2Ftoxic_combinations"
resource.type
=
"security_command_center_toxic_combination"
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
Security Command Center Toxic Combination logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Security Command Center Toxic Combination
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
gs://gcp-scc-toxic-combination-logs/
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
Directly mapped from the
category
field in the raw log.
createTime
read_only_udm.security_result.detection_fields.value
Directly mapped from the
createTime
field in the raw log, where key is 'createTime'.
mute
read_only_udm.security_result.detection_fields.value
Directly mapped from the
mute
field in the raw log, where key is 'mute'.
name
read_only_udm.metadata.product_log_id
Directly mapped from the
name
field in the raw log.
parent
read_only_udm.target.resource_ancestors.name
Directly mapped from the
parent
field in the raw log.
parentDisplayName
read_only_udm.metadata.description
Directly mapped from the
parentDisplayName
field in the raw log.
resource.displayName
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
resource.displayName
field in the raw log, where key is 'resource_displayName'.
resource.folders
read_only_udm.target.resource_ancestors
The parser extracts resource folder information from the
folders
array in the
resource
object. It iterates through each folder and maps the
resourceFolder
to
name
and
resourceFolderDisplayName
to
attribute.labels.value
where key is 'folder_resourceFolderDisplayName'.
resource.name
read_only_udm.target.resource.name
Directly mapped from the
resource.name
field in the raw log.
resource.parent
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
resource.parent
field in the raw log, where key is 'resource_parent'.
resource.parentDisplayName
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
resource.parentDisplayName
field in the raw log, where key is 'resource_parentDisplayName'.
resource.project
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
resource.project
field in the raw log, where key is 'resource_project'.
resource.projectDisplayName
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
resource.projectDisplayName
field in the raw log, where key is 'resource_projectDisplayName'.
resource.service
read_only_udm.target.application
Directly mapped from the
resource.service
field in the raw log.
resource.type
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
resource.type
field in the raw log, where key is 'resource_type'.
resourceName
read_only_udm.target.resource.name
Directly mapped from the
resourceName
field in the raw log.
securityMarks.name
read_only_udm.security_result.detection_fields.value
Directly mapped from the
securityMarks.name
field in the raw log, where key is 'securityMarks_name'.
severity
read_only_udm.security_result.severity
Directly mapped from the
severity
field in the raw log.
state
read_only_udm.security_result.detection_fields.value
Directly mapped from the
state
field in the raw log, where key is 'state'.
eventTime
read_only_udm.metadata.event_timestamp.seconds
The parser extracts the timestamp from the
eventTime
field and converts it to Unix epoch seconds.
read_only_udm.metadata.product_name
The parser sets the
product_name
to
Security Command Center
based on the log source.
read_only_udm.metadata.vendor_name
The parser sets the
vendor_name
to
Google
based on the log source.
read_only_udm.security_result.alert_state
The parser sets the
alert_state
to
ALERTING
as this log represents an active alert.
read_only_udm.security_result.category_details
The parser sets the
category_details
to
POSTURE_VIOLATION
based on the log source.
read_only_udm.security_result.url_back_to_product
The parser dynamically constructs the
url_back_to_product
using the organization, source, and finding IDs extracted from the log.
parent
read_only_udm.target.resource.product_object_id
The parser extracts the source ID from the
parent
field and sets it as the
product_object_id
.
resourceName
read_only_udm.target.resource_ancestors.name
The parser extracts the project ID from the
resourceName
field and sets it as a
resource_ancestors
entry with
resource_type
as
CLOUD_PROJECT
.
read_only_udm.target.resource_ancestors.resource_subtype
The parser sets the
resource_subtype
to
google.cloud.resourcemanager.Project
for folder ancestors based on the log source.
read_only_udm.target.resource.attribute.labels.key
The parser sets multiple keys for the
labels
field in the
attribute
object of the target resource. These keys include 'resource_parentDisplayName', 'resource_type', 'resource_projectDisplayName', 'resource_displayName', 'finding_id', 'source_id', 'resource_parent', and 'resource_project'.
Need more help?
Get answers from Community members and Google SecOps professionals.
