# Collect Cloud Intrusion Detection System (Cloud IDS) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-ids/  
**Scraped:** 2026-03-05T09:22:11.080533Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloud Intrusion Detection System (Cloud IDS) logs
Supported in:
Google secops
SIEM
This document explains how to export and ingest Cloud IDS logs into Google Security Operations using Cloud Storage. The parser transforms raw JSON formatted Cloud IDS logs from Google Cloud into a structured UDM format. It extracts relevant fields, maps them to UDM schema, categorizes events, and enriches the data with additional context like network direction and resource types.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Cloud IDS is set up and active in your Google Cloud environment.
Privileged access to Google Cloud and appropriate permissions to access Cloud IDS.
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
gcp-ids-logs
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
Configure Cloud IDS logs export
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
google-cloud-ids-logs-sink
.
Sink Destination
: select
Cloud Storage
and provide the Google Cloud storage bucket URI; for example,
gs://gcp-ids-logs
.
Log Filter
:
logName
=
"projects/<your-project-id>/logs/cloud-ids"
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
GCP IDS Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
GCP IDS
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
gs://gcp-ids-logs
.
Source deletion options
: select the deletion option according to your preference..
Note: If you select the
Delete transferred files
or
Delete transferred files and empty directories
option, make sure that you granted appropriate permissions to the service account.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days
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
insertId
metadata.product_log_id
Direct mapping.
jsonPayload.alert_severity
security_result.severity
Direct mapping.
jsonPayload.alert_time
metadata.event_timestamp
Direct mapping.
jsonPayload.application
principal.application
Direct mapping, only if direction is server-to-client.
jsonPayload.application
target.application
Direct mapping, only if direction is client-to-server or logName contains
traffic
.
jsonPayload.category
security_result.category
Mapped based on the value of 'jsonPayload.category':
- 'dos': NETWORK_DENIAL_OF_SERVICE
- 'info-leak': NETWORK_SUSPICIOUS
- 'protocol-anomaly': NETWORK_MALICIOUS
- 'backdoor', 'spyware', 'trojan': SOFTWARE_MALICIOUS
jsonPayload.category
security_result.category_details
Direct mapping.
jsonPayload.cves
extensions.vulns.vulnerabilities.cve_id
Direct mapping, iterating over the array.
jsonPayload.destination_ip_address
target.ip
Direct mapping.
jsonPayload.destination_port
target.port
Direct mapping.
jsonPayload.details
extensions.vulns.vulnerabilities.description
Direct mapping.
jsonPayload.details
security_result.detection_fields.value
Mapped if 'jsonPayload.repeat_count' exists. The key is set to 'repeat_count'.
jsonPayload.direction
network.direction
Mapped based on the value of 'jsonPayload.direction':
- 'client-to-server': OUTBOUND
- 'server-to-client': INBOUND
jsonPayload.elapsed_time
network.session_duration.seconds
Direct mapping.
jsonPayload.ip_protocol
network.ip_protocol
Direct mapping, converting to uppercase and then mapping to protocol number.
jsonPayload.name
security_result.threat_name
Direct mapping.
jsonPayload.network
principal.resource.name
Direct mapping, only if direction is server-to-client.
jsonPayload.network
target.resource.name
Direct mapping, only if direction is client-to-server or logName contains
traffic
.
jsonPayload.repeat_count
security_result.detection_fields.value
Mapped if it exists. The key is set to 'repeat_count'.
jsonPayload.session_id
network.session_id
Direct mapping.
jsonPayload.source_ip_address
principal.ip
Direct mapping.
jsonPayload.source_port
principal.port
Direct mapping.
jsonPayload.start_time
about.labels.value
Mapped if it exists. The key is set to 'start_time'.
jsonPayload.start_time
additional.fields.value.string_value
Mapped if it exists. The key is set to 'start_time'.
jsonPayload.threat_id
security_result.threat_id
Direct mapping.
jsonPayload.total_bytes
about.labels.value
Mapped if it exists. The key is set to 'total_bytes'.
jsonPayload.total_bytes
additional.fields.value.string_value
Mapped if it exists. The key is set to 'total_bytes'.
jsonPayload.total_packets
about.labels.value
Mapped if it exists. The key is set to 'total_packets'.
jsonPayload.total_packets
additional.fields.value.string_value
Mapped if it exists. The key is set to 'total_packets'.
jsonPayload.type
security_result.detection_fields.value
Mapped if it exists. The key is set to 'type'.
jsonPayload.uri_or_filename
target.file.full_path
Direct mapping.
logName
security_result.category_details
Direct mapping.
receiveTimestamp
metadata.collected_timestamp
Direct mapping.
resource.labels.id
observer.resource.product_object_id
Direct mapping.
resource.labels.location
observer.location.name
Direct mapping.
resource.labels.resource_container
observer.resource.name
Direct mapping.
resource.type
observer.resource.resource_subtype
Direct mapping.
metadata.event_type
Determined by a set of conditional rules based on the presence and values of other fields, defaulting to 'GENERIC_EVENT'.
metadata.vendor_name
Static value:
Google Cloud Platform
.
metadata.product_name
Static value:
GCP_IDS
.
metadata.log_type
Static value:
GCP_IDS
.
extensions.vulns.vulnerabilities.vendor
Static value:
GCP_IDS
, added for each CVE in 'jsonPayload.cves'.
principal.resource.resource_type
Static value:
VPC_NETWORK
, added if 'jsonPayload.network' exists and direction is server-to-client.
target.resource.resource_type
Static value:
VPC_NETWORK
, added if 'jsonPayload.network' exists and direction is client-to-server or logName contains
traffic
.
observer.resource.resource_type
Static value:
CLOUD_PROJECT
, added if 'resource.labels.resource_container' or 'resource.type' exists.
observer.resource.attribute.cloud.environment
Static value:
GOOGLE_CLOUD_PLATFORM
, added if 'resource.labels.resource_container' or 'resource.type' exists.
Need more help?
Get answers from Community members and Google SecOps professionals.
