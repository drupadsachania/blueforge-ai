# Collect Cloud Next Generation Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-ngfw-enterprise/  
**Scraped:** 2026-03-05T09:53:13.393211Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloud Next Generation Firewall logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Cloud NGFW logs into Google Security Operations using Google Cloud. The parser extracts fields from Google Cloud Firewall logs, transforms and maps them to the UDM. It handles various log fields, including connection details, threat information, rule details, and network information, performing data type conversions, renaming, and conditional logic based on the
action
and
direction
fields to populate the UDM model correctly.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Cloud NGFW is active and configured in your Google Cloud environment.
Privileged access to Google Cloud and appropriate permissions to access Cloud NGFW logs.
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
gcp-ngfw-logs
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
Configure Cloud NGFW logs export
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
NGFW-Export-Sink
.
Sink Destination
: select
Google Cloud Storage
and enter the URI for your bucket; for example,
gs://gcp-ngfw-logs/
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/gcp-firewall"
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
How to set up the Google Cloud NGFW Enterprise feed
Click the
Google Cloud Compute platform
pack.
Locate the
GCP NGFW Enterprise
log type.
Click
Next
.
Specify values for the following fields:
Source Type
: Google Cloud Storage V2
Storage Bucket URI
: Google Cloud storage bucket URL; for example,
gs://gcp-ngfw-logs/
. This URL must end with a trailing forward slash (/).
Source deletion options
: select the deletion option according to your preference.
Maximum file age
: Include files modified within the last number of days. Default is 180 days.
Click
Get a Service Account
next to the
Chronicle Service Account
field.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
:
Namespace associated with the feed
.
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
insertId
metadata.product_log_id
Directly mapped from the
insertId
field.
jsonPayload.action
security_result.action_details
Directly mapped from the
jsonPayload.action
field.
jsonPayload.connection.clientIp
principal.asset.ip
Directly mapped from the
jsonPayload.connection.clientIp
field.
jsonPayload.connection.clientIp
principal.ip
Directly mapped from the
jsonPayload.connection.clientIp
field.
jsonPayload.connection.clientPort
principal.port
Directly mapped from the
jsonPayload.connection.clientPort
field and converted to integer.
jsonPayload.connection.protocol
network.ip_protocol
Mapped from
jsonPayload.connection.protocol
. If the value is
tcp
, the UDM field is set to
TCP
. Similar logic applies for
udp
,
icmp
, and
igmp
.
jsonPayload.connection.serverIp
target.asset.ip
Directly mapped from the
jsonPayload.connection.serverIp
field.
jsonPayload.connection.serverIp
target.ip
Directly mapped from the
jsonPayload.connection.serverIp
field.
jsonPayload.connection.serverPort
target.port
Directly mapped from the
jsonPayload.connection.serverPort
field and converted to integer.
jsonPayload.interceptVpc.projectId
security_result.rule_labels
Mapped from
jsonPayload.interceptVpc.projectId
with key
rule_details_projectId
.
jsonPayload.interceptVpc.vpc
security_result.rule_labels
Mapped from
jsonPayload.interceptVpc.vpc
with key
rule_details_vpc_network
.
jsonPayload.securityProfileGroupDetails.securityProfileGroupId
security_result.rule_labels
Mapped from
jsonPayload.securityProfileGroupDetails.securityProfileGroupId
with key
rule_details_security_profile_group
.
jsonPayload.securityProfileGroupDetails.securityProfileGroupId
security_result.rule_labels
Mapped from
jsonPayload.securityProfileGroupDetails.securityProfileGroupId
with key
rule_details_securityProfileGroupDetails_id
.
jsonPayload.threatDetails.category
security_result.rule_labels
Mapped from
jsonPayload.threatDetails.category
with key
rule_details_category
.
jsonPayload.threatDetails.direction
security_result.rule_labels
Mapped from
jsonPayload.threatDetails.direction
with key
rule_details_direction
.
jsonPayload.threatDetails.id
security_result.threat_id
Directly mapped from the
jsonPayload.threatDetails.id
field.
jsonPayload.threatDetails.severity
security_result.severity
Mapped from
jsonPayload.threatDetails.severity
.  If the value is
CRITICAL
, the UDM field is set to
CRITICAL
. Similar logic applies for
HIGH
,
MEDIUM
,
LOW
, and
INFO
.
jsonPayload.threatDetails.threat
security_result.threat_name
Directly mapped from the
jsonPayload.threatDetails.threat
field.
jsonPayload.threatDetails.type
security_result.rule_labels
Mapped from
jsonPayload.threatDetails.type
with key
rule_details_threat_type
.
jsonPayload.threatDetails.uriOrFilename
security_result.rule_labels
Mapped from
jsonPayload.threatDetails.uriOrFilename
with key
rule_details_uriOrFilename
.
logName
metadata.product_event_type
Directly mapped from the
logName
field.
metadata.collected_timestamp
metadata.collected_timestamp
Directly mapped from the
receiveTimestamp
field and parsed using the specified date format.
metadata.event_type
metadata.event_type
Set to
NETWORK_CONNECTION
if both
principal_ip
and
target_ip
are present. Set to
STATUS_UNCATEGORIZED
if only
principal_ip
is present. Otherwise, set to
GENERIC_EVENT
.
metadata.product_name
metadata.product_name
Hardcoded to
GCP Firewall
.
metadata.vendor_name
metadata.vendor_name
Hardcoded to
Google Cloud Platform
.
receiveTimestamp
metadata.collected_timestamp
Directly mapped from the
receiveTimestamp
field.
security_result.action
security_result.action
Derived from the
jsonPayload.action
field. Mapped to
ALLOW
,
BLOCK
, or
UNKNOWN_ACTION
based on the value of
jsonPayload.action
.
timestamp
metadata.event_timestamp
Directly mapped from the
timestamp
field.
timestamp
timestamp
Directly mapped from the
timestamp
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
