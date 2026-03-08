# Collect Forseti Open Source logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forseti/  
**Scraped:** 2026-03-05T09:24:43.106265Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forseti Open Source logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forseti Open Source logs to Google Security Operations using Google Cloud Storage V2.
Forseti Security is a community-driven collection of open source tools to improve the security of Google Cloud Platform environments. Forseti takes inventory snapshots of GCP resources on a recurring cadence, scans resources to ensure that access controls are set as intended, and provides visibility into Cloud IAM policies.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
GCP project with Cloud Storage API enabled.
Permissions to create and manage GCS buckets.
Permissions to manage IAM policies on GCS buckets.
An existing Forseti Security deployment (for example, deployed using the Forseti Terraform module on Google Compute Engine).
Access to the Forseti server configuration file (
forseti_conf_server.yaml
).
Create Google Cloud Storage bucket
Using Google Cloud Console
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
forseti-violations-export
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location (for example,
us-central1
)
Storage class
Standard (recommended for frequently accessed logs)
Access control
Uniform (recommended)
Protection tools
Optional: Enable object versioning or retention policy
Click
Create
.
Using gcloud command-line tool
Alternatively, create a bucket using the
gcloud
command:
gcloud
storage
buckets
create
gs://forseti-violations-export
\
--location
=
us-central1
\
--default-storage-class
=
STANDARD
Replace:
forseti-violations-export
: Your desired bucket name (globally unique).
us-central1
: Your preferred region (for example,
us-central1
,
europe-west1
).
Configure Forseti Security to export violations to GCS
Forseti Security uses a notifier configuration in the
forseti_conf_server.yaml
file to export scanner violations to Google Cloud Storage.
Connect to your Forseti server VM using SSH:
gcloud
compute
ssh
forseti-server-vm
--project
=
YOUR_PROJECT_ID
--zone
=
YOUR_ZONE
Replace
YOUR_PROJECT_ID
and
YOUR_ZONE
with your Forseti deployment values.
Open the Forseti server configuration file for editing:
sudo
nano
/home/ubuntu/forseti-security/configs/forseti_conf_server.yaml
If your Forseti deployment uses a GCS-based configuration, download the file from your Forseti server bucket:
gsutil
cp
gs://YOUR_FORSETI_SERVER_BUCKET/configs/forseti_conf_server.yaml
~/forseti_conf_server.yaml
Navigate to the
notifier
section and locate the
resources
subsection.
For each violation resource type you want to export, configure the
gcs_violations
notifier. Add or update the configuration as follows:
notifier
:
resources
:
-
resource
:
iam_policy_violations
should_notify
:
true
notifiers
:
-
name
:
gcs_violations
configuration
:
data_format
:
csv
gcs_path
:
gs://forseti-violations-export/violations/
-
resource
:
firewall_rule_violations
should_notify
:
true
notifiers
:
-
name
:
gcs_violations
configuration
:
data_format
:
csv
gcs_path
:
gs://forseti-violations-export/violations/
-
resource
:
cloudsql_acl_violations
should_notify
:
true
notifiers
:
-
name
:
gcs_violations
configuration
:
data_format
:
csv
gcs_path
:
gs://forseti-violations-export/violations/
-
resource
:
bucket_acl_violations
should_notify
:
true
notifiers
:
-
name
:
gcs_violations
configuration
:
data_format
:
csv
gcs_path
:
gs://forseti-violations-export/violations/
-
resource
:
config_validator_violations
should_notify
:
true
notifiers
:
-
name
:
gcs_violations
configuration
:
data_format
:
csv
gcs_path
:
gs://forseti-violations-export/violations/
Replace:
forseti-violations-export
: Your GCS bucket name created in the previous step.
violations/
: Optional prefix path for organizing violation files.
Configuration parameters:
resource
: The violation resource type. Available resource types depend on which Forseti scanners are enabled in your deployment. Common types include
iam_policy_violations
,
firewall_rule_violations
,
cloudsql_acl_violations
,
bucket_acl_violations
,
config_validator_violations
,
groups_settings_violations
, and others.
should_notify
: Set to
true
to enable notifications for this resource type.
data_format
: The format of the exported data. Valid values are
csv
or
json
. The default is
csv
.
gcs_path
: The Cloud Storage path where violations will be exported. The path must begin with
gs://
and should include a trailing slash.
Save the configuration file.
If you downloaded the configuration from GCS, upload the updated file back to your Forseti server bucket:
gsutil
cp
~/forseti_conf_server.yaml
gs://YOUR_FORSETI_SERVER_BUCKET/configs/forseti_conf_server.yaml
Reload the Forseti server configuration:
forseti
server
configuration
reload
Verify the configuration was loaded successfully:
forseti
server
configuration
get
|
grep
gcs_violations
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest Forseti Open Source logs
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Forseti Violations
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Forseti Open Source
as the
Log type
.
Click
Get Service Account
.
A unique service account email will be displayed, for example:
chronicle
-
12345678
@chronicle
-
gcp
-
prod
.
iam
.
gserviceaccount
.
com
Copy this email address. You will use it in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs
:
//
forseti
-
violations
-
export
/
violations
/
Replace:
forseti-violations-export
: Your GCS bucket name.
violations/
: Optional prefix/folder path where logs are stored (leave empty for root).
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Using Google Cloud Console
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email.
Assign roles
: Select
Storage Object Viewer
.
Click
Save
.
Using gcloud command-line tool
Alternatively, grant permissions using the
gcloud
command:
gcloud
storage
buckets
add-iam-policy-binding
gs://forseti-violations-export
\
--member
=
"serviceAccount:chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com"
\
--role
=
"roles/storage.objectViewer"
Replace:
forseti-violations-export
: Your bucket name.
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
: The Google SecOps service account email.
Using gsutil command-line tool (legacy)
gsutil
iam
ch
serviceAccount:chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com:objectViewer
\
gs://forseti-violations-export
Verify permissions
To verify the permissions were granted correctly:
gcloud
storage
buckets
get-iam-policy
gs://forseti-violations-export
\
--flatten
=
"bindings[].members"
\
--filter
=
"bindings.role:roles/storage.objectViewer"
You should see the Google SecOps service account email in the output.
UDM mapping table
Log field
UDM mapping
Logic
data.resource_data.instanceGroupUrls
about
Merged from array of instanceGroupUrls
data.resource_data.nodePools.*.statusMessage
metadata.description
Value from nodePool.statusMessage
data.resource_type
metadata.event_type
Set to RESOURCE_PERMISSIONS_CHANGE for kms_cryptokey/serviceaccount_key, RESOURCE_DELETION for firewall, STATUS_HEARTBEAT for kubernetes_cluster, else GENERIC_EVENT
data.scanner_index_id
metadata.product_log_id
Value copied directly, converted to string
metadata.product_name
Set to "FORSETI SECURITY"
metadata.vendor_name
Set to "FORSETI"
data.resource_data.direction
network.direction
Set to INBOUND if direction is INGRESS
data.resource_data.endpoint
principal.ip
Value copied directly
data.resource_data.nodeConfig.oauthScopes.0
principal.url
Value copied directly
data.full_name, serviceAccount
principal.user.userid
Extracted from data.full_name using grok, or set to serviceAccount if not empty
data.violation_data.protection_level, data.violation_data.purpose, data.violation_data.project_id, data.violation_data.node_pool_name, data.violation_data.violation_reason
security_result.detection_fields
Merged from multiple key-value pairs
data.violation_type
security_result.category
Set to POLICY_VIOLATION if FIREWALL_BLACKLIST_VIOLATION, UNKNOWN_CATEGORY if KE_VERSION_VIOLATION, else ACL_VIOLATION
data.rule_name
security_result.rule_name
Value copied directly
data.violation_type
security_result.summary
Value copied directly
data.resource_data.zone
target.asset.attribute.cloud.availability_zone
Value copied directly
target.asset.attribute.cloud.environment
Set to "GOOGLE_CLOUD_PLATFORM"
data.full_name
target.asset.attribute.cloud.project.id
Extracted from data.full_name using grok
data.resource_data.subnetwork
target.asset.attribute.cloud.vpc.name
Value copied directly
data.resource_data.nodeConfig.machineType
target.asset.hardware
Merged from machineType and constant CPU platform
data.resource_data.privateClusterConfig.privateEndpoint
target.ip
Value copied directly
data.resource_data.versionTemplate.algorithm, data.resource_data.key_algorithm
target.labels
Merged key-value pair for algorithm if present
data.resource_data.location
target.location.name
Value copied directly
data.resource_name
target.resource.name
Value copied directly
data.resource_id
target.resource.product_object_id
Value copied directly if different from resource_name
data.resource_type
target.resource.resource_subtype
Set to "gke" if resource_type is kubernetes_cluster
data.resource_type
target.resource.resource_type
Mapped to specific type based on original resource_type
Need more help?
Get answers from Community members and Google SecOps professionals.
