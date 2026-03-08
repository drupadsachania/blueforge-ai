# Collect Twingate VPN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/twingate/  
**Scraped:** 2026-03-05T09:29:40.631622Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Twingate VPN logs
Supported in:
Google secops
SIEM
Overview
This Twingate parser extracts fields from Twingate VPN JSON logs, normalizes them, and maps them to the Unified Data Model (UDM). It handles various event types, including connection details, user information, resource access, and intermediary relays, enriching the data with metadata like vendor and product information.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to AWS IAM and S3.
Configure Amazon S3 bucket
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save bucket
Name
and
Region
for future reference.
Create a
User
following this user guide:
Creating an IAM user
.
Select the created
User
.
Select
Security credentials
tab.
Click
Create Access Key
in section
Access Keys
.
Select
Third-party service
as
Use case
.
Click
Next
.
Optional: add description tag.
Click
Create access key
.
Click
Download .csv file
for save the
Access Key
and
Secret Access Key
for future reference.
Click
Done
.
Select
Permissions
tab.
Click
Add permissions
in section
Permissions policies
.
Select
Add permissions
.
Select
Attach policies directly
.
Search for
AmazonS3FullAccess
policy.
Select the policy.
Click
Next
.
Click
Add permissions
.
Configure Twingate sync with Amazon S3
Go to the Twingate Admin Console.
Go to
Settings
>
Reports
.
Click
Sync to S3 Bucket
.
Configure the S3 Sync:
Bucket Name
: Provide the name of your S3 bucket.
Access Key ID
: Enter the Access Key.
Secret Access Key
: Enter the Secret Key.
Click
Start Syncing
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
Twingate Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select
Twingate
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: the bucket URI.
s3:/BUCKET_NAME
Replace the following:
BUCKET_NAME
: the name of the bucket.
Source deletion options
: select deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize screen
, and then click
Submit
.
Field mapping reference
This parser transforms raw Twingate logs in JSON format into UDM. It normalizes the data and extracts relevant information, mapping it to corresponding UDM fields.
UDM Mapping Table
Log Field
UDM Mapping
Logic
connector.id
read_only_udm.additional.fields[].key
Set to "connector_id".
connector.id
read_only_udm.additional.fields[].value.string_value
Value from
connector.id
.
connector.name
read_only_udm.additional.fields[].key
Set to "connector_name".
connector.name
read_only_udm.additional.fields[].value.string_value
Value from
connector.name
.
connection.bytes_received
read_only_udm.network.received_bytes
Value from
connection.bytes_received
(converted to an unsigned integer).
connection.bytes_transferred
read_only_udm.network.sent_bytes
Value from
connection.bytes_transferred
(converted to an unsigned integer).
connection.client_ip
read_only_udm.principal.asset.ip
Value from
connection.client_ip
.
connection.client_ip
read_only_udm.principal.ip
Value from
connection.client_ip
.
connection.protocol
read_only_udm.network.ip_protocol
Value from
connection.protocol
(converted to uppercase).
device.id
read_only_udm.principal.user.product_object_id
Value from
device.id
.
event.id
read_only_udm.metadata.event_id
Value from
event.id
event.time
read_only_udm.metadata.event_timestamp.seconds
Seconds part of the timestamp from
event.time
.
event.type
read_only_udm.event.type
Value from
event.type
.
event.version
read_only_udm.metadata.product_version
Value from
event.version
.
relays[].ip
read_only_udm.intermediary.ip
Value from
relays[].ip
.
relays[].name
read_only_udm.intermediary.hostname
Value from
relays[].name
.
relays[].port
read_only_udm.intermediary.port
Value from
relays[].port
(converted to an integer).
remote_network.id
read_only_udm.network.session_id
Value from
remote_network.id
.
remote_network.name
read_only_udm.network.dhcp.sname
Value from
remote_network.name
.
resource.address
read_only_udm.principal.asset.hostname
Value from
resource.address
.
resource.address
read_only_udm.principal.hostname
Value from
resource.address
.
resource.id
read_only_udm.resource.product_object_id
Value from
resource.id
.
resource.port
read_only_udm.principal.port
Value from
resource.port
(converted to an integer).
status
read_only_udm.security_result.summary
Value from
status
.
time
read_only_udm.event.timestamp.seconds
Seconds part of the timestamp from
time
.
user.email
read_only_udm.principal.user.email_addresses
Value from
user.email
.
user.id
read_only_udm.principal.user.userid
Value from
user.id
.
Need more help?
Get answers from Community members and Google SecOps professionals.
