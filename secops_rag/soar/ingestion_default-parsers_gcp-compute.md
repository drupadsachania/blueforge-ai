# Collect Google Cloud Compute logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-compute/  
**Scraped:** 2026-03-05T09:56:41.872392Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud Compute logs
Supported in:
Google secops
SIEM
This document explains how to configure Google Cloud Compute logs export to Google Security Operations using Cloud Storage. The parser extracts fields, normalizes the message field, and maps the extracted data to the Unified Data Model (UDM) schema for consistent security event representation. It handles various log formats, including syslog-like messages and key-value pairs, and categorizes events based on extracted fields like
type
and
action
.
Before You Begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Compute is set up and active in your Google Cloud environment.
Privileged access to Google Cloud.
Create a Google Cloud Storage Bucket
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
compute-logs
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
Configure Google Cloud Compute Logs Export
In the
Google Cloud console
, go to
Logging
>
Log Router
.
Click
Create Sink
.
Provide the following configuration details:
Sink Name
: Enter a meaningful name (for example,
Compute-Logs-Sink
).
Sink Destination
: Select
Cloud Storage
.
Cloud Storage Bucket
: Enter the bucket URI (for example,
gs://compute-logs/compute-logs/
).
In the
Build inclusion filter
section, configure the log filter to capture Google Cloud Compute logs using one or more of the following patterns:
Resource type filter (required - choose one):
For
VM Instance logs only
:
resource.type="gce_instance"
For
all GCE-related resources
(VM instances, subnetworks, firewalls):
resource.type=("gce_instance" OR "gce_subnetwork" OR "gce_network" OR "gce_firewall_rule")
Specific log types (optional - add as needed):
For
Audit logs
(instance operations, configuration changes):
resource.type="gce_instance"
logName:"cloudaudit.googleapis.com/activity"
For
VPC Flow logs
(network traffic):
resource.type="gce_subnetwork"
logName:"vpc_flows"
For
Firewall logs
(allowed/denied connections):
resource.type="gce_subnetwork"
logName:"compute.googleapis.com/firewall"
For
Serial Console logs
:
resource.type="gce_instance"
logName:"serialconsole.googleapis.com"
Network-related filters (optional - add as needed):
Filter by
connection details
(source/destination IPs, ports):
jsonPayload.connection.dest_ip:*
OR jsonPayload.connection.src_ip:*
Filter by
instance details
:
jsonPayload.dest_instance.project_id:*
OR jsonPayload.src_instance.project_id:*
Filter by
security actions
:
jsonPayload.rule_details.action=("ALLOW" OR "BLOCK")
Example: Complete filter for comprehensive Compute logging:
(resource.type="gce_instance" OR resource.type="gce_subnetwork")
AND (
 logName:"cloudaudit.googleapis.com/activity"
 OR logName:"vpc_flows"
 OR logName:"compute.googleapis.com/firewall"
 OR jsonPayload.connection.dest_ip:*
 OR jsonPayload.connection.src_ip:*
)
Click
Create Sink
.
Configure Permissions for Cloud Storage
Go to
IAM
>
IAM & Admin
>
Service Accounts
.
Find the Cloud Logging service account; for example, service-account@logging.iam.gserviceaccount.com.
Provide it with
roles/storage.admin
role on the bucket.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New
Content Hub
>
Content Packs
>
Get Started
How to set up the Google Cloud compute feed
Click the
Google Cloud Compute platform
pack.
Locate the
GCP Compute Feed
logtype and click
Add new feed
.
Specify values for the following fields:
Source Type
:
Google Cloud Storage V2
.
Storage Bucket URI
: Cloud Storage bucket URL; for example,
gs://compute-context-logs/
. This URL must end with a trailing forward slash (/).
Source deletion option
: select the deletion option according to your preference.
Maximum File Age
: Include files modified within the last number of days. Default is 180 days.
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
Log field
UDM mapping
Logic
addr
read_only_udm.principal.ip
Merged into the principal IP address list if the field is not empty or "?".
jsonPayload.connection.dest_ip
read_only_udm.target.ip
Merged into the target IP address list if the field exists.
jsonPayload.connection.dest_port
read_only_udm.target.port
Converted to string, then to integer and mapped if no errors occur during conversion.
jsonPayload.connection.protocol
read_only_udm.network.ip_protocol
Converted to string, then to integer. Used to determine the IP protocol (TCP, UDP, etc.) using a lookup table and mapped if no errors occur during conversion.
jsonPayload.connection.src_ip
read_only_udm.principal.ip
Merged into the principal IP address list if the field exists.
jsonPayload.connection.src_port
read_only_udm.principal.port
Converted to string, then to integer and mapped if no errors occur during conversion.
jsonPayload.dest_instance.project_id
read_only_udm.target.resource.product_object_id
Conditionally mapped if jsonPayload.dest_vpc.project_id exists.
jsonPayload.dest_instance.region
read_only_udm.target.location.name
Conditionally mapped if jsonPayload.dest_vpc.project_id exists.
jsonPayload.dest_instance.vm_name
read_only_udm.target.resource.attribute.cloud.project.name
Conditionally mapped if jsonPayload.dest_vpc.project_id exists.
jsonPayload.dest_instance.zone
read_only_udm.target.resource.attribute.cloud.availability_zone
Conditionally mapped if jsonPayload.dest_vpc.project_id exists.
jsonPayload.dest_vpc.project_id
read_only_udm.target.cloud.vpc.product_object_id
Used as a condition to map related fields.
jsonPayload.dest_vpc.subnetwork_name
read_only_udm.target.cloud.vpc.name
Conditionally mapped if jsonPayload.dest_vpc.project_id exists.
jsonPayload.instance.project_id
read_only_udm.target.resource.product_object_id
Conditionally mapped if jsonPayload.instance.project_id exists.
jsonPayload.instance.region
read_only_udm.target.location.name
Conditionally mapped if jsonPayload.instance.project_id exists.
jsonPayload.instance.vm_name
read_only_udm.target.resource.attribute.cloud.project.name
Conditionally mapped if jsonPayload.instance.project_id exists.
jsonPayload.instance.zone
read_only_udm.target.resource.attribute.cloud.availability_zone
Conditionally mapped if jsonPayload.instance.project_id exists.
jsonPayload.message
read_only_udm.metadata.product_event_type, read_only_udm.principal.application, read_only_udm.target.process.pid, read_only_udm.target.user.userid, read_only_udm.principal.hostname, read_only_udm.target.process.command_line, read_only_udm.security_result.description, read_only_udm.principal.process.file.full_path
Parsed and mapped to different fields based on grok patterns and conditional logic.
jsonPayload.rule_details.action
read_only_udm.security_result.action
Used to determine the security result action (ALLOW/BLOCK) and mapped.
jsonPayload.rule_details.direction
read_only_udm.network.direction
Used to determine the network direction (INBOUND/OUTBOUND/UNKNOWN_DIRECTION) and mapped.
jsonPayload.rule_details.priority
read_only_udm.security_result.priority_details
Converted to string and mapped if no errors occur during conversion.
jsonPayload.rule_details.reference
read_only_udm.security_result.rule_labels.value
Mapped to the rule label value.
jsonPayload.src_instance.project_id
read_only_udm.principal.resource.product_object_id
Conditionally mapped if jsonPayload.src_vpc.project_id exists.
jsonPayload.src_instance.region
read_only_udm.principal.location.name
Conditionally mapped if jsonPayload.src_vpc.project_id exists.
jsonPayload.src_instance.vm_name
read_only_udm.principal.resource.attribute.cloud.project.name
Conditionally mapped if jsonPayload.src_vpc.project_id exists.
jsonPayload.src_instance.zone
read_only_udm.principal.resource.attribute.cloud.availability_zone
Conditionally mapped if jsonPayload.src_vpc.project_id exists.
jsonPayload.src_vpc.project_id
read_only_udm.principal.cloud.vpc.product_object_id
Used as a condition to map related fields.
jsonPayload.src_vpc.subnetwork_name
read_only_udm.principal.cloud.vpc.name
Conditionally mapped if jsonPayload.src_vpc.project_id exists.
jsonPayload.vpc.project_id
read_only_udm.target.cloud.vpc.product_object_id
Conditionally mapped if jsonPayload.vpc.project_id exists.
jsonPayload.vpc.subnetwork_name
read_only_udm.target.cloud.vpc.name
Conditionally mapped if jsonPayload.vpc.project_id exists.
logName
read_only_udm.security_result.category_details
Mapped directly.
resource.labels.instance_id
read_only_udm.principal.resource.product_object_id, read_only_udm.principal.asset_id
Conditionally mapped. If type is "PROCTITLE", it's used to construct the asset ID.
resource.labels.location
read_only_udm.principal.location.name
Conditionally mapped if the field exists.
resource.labels.project_id
read_only_udm.metadata.product_deployment_id
Conditionally mapped if the field exists.
resource.labels.zone
read_only_udm.principal.resource.attribute.cloud.availability_zone
Conditionally mapped if the field exists.
resource.type
read_only_udm.metadata.event_type
Used to determine the event type and mapped.
timestamp
read_only_udm.metadata.event_timestamp
Mapped directly.
type
read_only_udm.metadata.product_event_type, read_only_udm.metadata.event_type, read_only_udm.extensions.auth.type
Used to determine the event type, product event type, and authentication type and mapped accordingly.
read_only_udm.metadata.event_type
The logic sets the event type based on the "type" field and other conditions. If no specific match is found, it defaults to "GENERIC_EVENT".
read_only_udm.metadata.log_type
Constant value "GCP_COMPUTE".
read_only_udm.metadata.vendor_name
Constant value "Google Cloud Platform".
read_only_udm.metadata.product_name
Constant value "Google Cloud Platform".
read_only_udm.security_result.rule_labels.key
Constant value "Reference".
read_only_udm.target.cloud.vpc.resource_type
Conditionally set to "VPC_NETWORK" if jsonPayload.instance.project_id or jsonPayload.dest_vpc.project_id exists.
read_only_udm.target.resource.attribute.cloud.environment
Conditionally set to "GOOGLE_CLOUD_PLATFORM" if jsonPayload.instance.project_id, jsonPayload.dest_vpc.project_id, or jsonPayload.src_vpc.project_id exists.
read_only_udm.principal.administrative_domain
Mapped from the "Account Domain" field extracted from the "kv_data" field.
read_only_udm.principal.user.user_display_name
Mapped from the "Account Name" field extracted from the "kv_data" field.
read_only_udm.target.resource.name
Mapped from the "Object Name" field extracted from the "kv_data" field.
read_only_udm.target.resource.type
Mapped from the "Object Type" field extracted from the "kv_data" field.
read_only_udm.principal.process.pid
Mapped from the "Process ID" field extracted from the "kv_data" field.
read_only_udm.target.user.windows_sid
Mapped from the "Security ID" field extracted from the "kv_data" field.
read_only_udm.network.session_id
Mapped from the "auid" field.
Need more help?
Get answers from Community members and Google SecOps professionals.
