# Collect Google Cloud IoT logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-iot/  
**Scraped:** 2026-03-05T09:25:03.457098Z

---

Home
Documentation
Security
Google Security Operations
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud IoT logs
Supported in:
Google secops
SIEM
This guide explains how to export Google Cloud IoT logs to Google Security Operations using Cloud Storage. The parser extracts fields from JSON-formatted logs and then maps those fields to the corresponding fields in the Google SecOps UDM schema, ultimately transforming raw log data into a structured format suitable for security analysis.
Before You Begin
Ensure that you have the following prerequisites:
Google SecOps instance.
IoT is set up and active in your Google Cloud environment.
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
cloudiot-logs
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
Configure Log Export in Google Cloud IoT
Sign in to
Google Cloud
account using your privileged account.
Search and select
Logging
in the search bar.
In
Log Explorer
, filter the logs by choosing
Cloud IoT Core
and click
Apply
.
Click
More Actions
.
Click
Create Sink
.
Provide the following configurations:
Sink Details
: enter a name and description.
Click
Next
.
Sink Destination
: select
Cloud Storage Bucket
.
Cloud Storage Bucket
: select the bucket created earlier or create a new bucket.
Click
Next
.
Choose Logs to include in Sink
: a default log is populated when you select an option in Cloud Storage Bucket.
Click
Next
.
Optional:
Choose Logs to filter out of Sink
: select the logs that you would like not to sink.
Click
Create Sink
.
In the
GCP console
, go to
Logging
>
Log Router
.
Click
Create Sink
.
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
GCP Cloud IoT Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
GCP Cloud IoT
as the
Log type
.
Click
Get Service Account
as the
Chronicle Service Account
.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Google Cloud storage bucket URL in
gs://my-bucket/<value>/
format.
Source deletion options
: select deletion option according to your preference.
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
Directly mapped from
insertId
field.
jsonPayload.eventType
metadata.product_event_type
Directly mapped from
jsonPayload.eventType
field.
jsonPayload.protocol
network.application_protocol
Directly mapped from
jsonPayload.protocol
field.
jsonPayload.serviceName
target.application
Directly mapped from
jsonPayload.serviceName
field.
jsonPayload.status.description
metadata.description
Directly mapped from
jsonPayload.status.description
field.
jsonPayload.status.message
security_result.description
Directly mapped from
jsonPayload.status.message
field.
labels.device_id
principal.asset_id
Value is set to
Device ID:
concatenated with the value of
labels.device_id
field.
receiveTimestamp
metadata.event_timestamp
Parsed from the
receiveTimestamp
field and used to populate both
events.timestamp
and
metadata.event_timestamp
.
resource.labels.device_num_id
target.resource.product_object_id
Directly mapped from
resource.labels.device_num_id
field.
resource.labels.location
target.location.name
Directly mapped from
resource.labels.location
field.
resource.labels.project_id
target.resource.name
Directly mapped from
resource.labels.project_id
field.
resource.type
target.resource.resource_subtype
Directly mapped from
resource.type
field.
severity
security_result.severity
Mapped from the
severity
field based on the following logic:
- If
severity
is
DEFAULT
,
DEBUG
,
INFO
, or
NOTICE
, then
security_result.severity
is set to
INFORMATIONAL
.
- If
severity
is
WARNING
or
ERROR
, then
security_result.severity
is set to
MEDIUM
.
- If
severity
is
CRITICAL
,
ALERT
, or
EMERGENCY
, then
security_result.severity
is set to
HIGH
.
N/A
metadata.log_type
Hardcoded to
GCP_CLOUDIOT
.
N/A
metadata.vendor_name
Hardcoded to
Google Cloud Platform
.
N/A
metadata.event_type
Hardcoded to
GENERIC_EVENT
.
N/A
metadata.product_name
Hardcoded to
GCP_CLOUDIOT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
