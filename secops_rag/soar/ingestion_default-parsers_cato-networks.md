# Collect Cato Networks logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cato-networks/  
**Scraped:** 2026-03-05T09:51:49.585707Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cato Networks logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cato Networks logs to Google Security Operations
using AWS S3. The parser first initializes a set of fields to empty strings and
then parses JSON-formatted Cato Networks logs. It then maps the extracted fields
to the corresponding fields in the Google SecOps Unified Data Model
(UDM) model, handling different event types and enriching the data with
additional context.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS S3, AWS IAM
Privileged access to Cato Networks
Configure AWS IAM and S3 Bucket
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save the bucket
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
Select the
Security credentials
tab.
Click
Create Access Key
in the
Access Keys
section.
Select
Third-party service
as
Use case
.
Click
Next
.
Optional: Add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
Access Key
and
Secret Access Key
for future reference.
Click
Done
.
Select the
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
Search for the
AmazonS3FullAccess
policy and then select the policy.
Click
Next
.
Click
Add permissions
.
Configure a New IAM Policy For S3 Bucket to enable data uploads
In
Policy
, click the
JSON
tab.
Edit the following
JSON
, replace
<bucket name>
with your S3 bucket, and
then paste it in the tab.
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Sid"
:
""
,
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:ListBucket"
,
"s3:GetBucketLocation"
],
"Resource"
:
[
"arn:aws:s3:::<bucket name>"
]
},
{
"Sid"
:
""
,
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:PutObject"
],
"Resource"
:
[
"arn:aws:s3:::<bucket name>/*"
]
}
]
}
Click
Create policy
.
Configure a New IAM Role With Cato's ARN
In the
Select trusted entity
screen, select
Custom Trust Policy
and
add Cato's ARN to the role: arn:aws:iam::428465470022:role/cato-events-integration
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Sid"
:
"Statement1"
,
"Effect"
:
"Allow"
,
"Principal"
:
{
"AWS"
:
"arn:aws:iam::428465470022:role/cato-events-integration"
},
"Action"
:
"sts:AssumeRole"
}
]
}
Click
Next
.
In the
Add permissions
screen, attach the policy that you created earlier
to the role.
Click
Next
.
Enter the
Role name
and click
Create role
.
Configure Cato Networks Events and S3 Integration
Sign in to the
Cato Networks
web UI.
Go to
Resources
>
Event Integrations
.
Click
Enable integration with Cato events
.
Click
New
.
Provide the following configuration details:
Enter the
Name
for the integration.
Bucket Name
: Identical name of the S3 bucket.
Folder
: Identical name for the folder path within the S3 bucket (if necessary).
Region
: Identical region for the S3 bucket.
Role ARN
: Copy and paste the ARN for the role for the S3 bucket.
(Optional) Define the filter settings for events that are uploaded to the S3 bucket (When you define multiple filters, there is an AND relationship, and the events that match all filters are uploaded).
Click
Apply
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
field, enter a name for the feed (for example,
Cato Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Cato Networks
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: The bucket URI (the format should be:
s3://<your-log-bucket-name>
).
Replace the following:
your-log-bucket-name
: the name of the bucket.
Source deletion options
: Select deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM mapping table
Log field
UDM mapping
Logic
account_id
target.user.userid
The value of this field is taken from the
account_id
field.
action
additional.fields.value.string_value
The value of this field is taken from the
action
field.
app_stack
additional.fields.value.list_value.values.string_value
The value of this field is taken from the
app_stack
field.
application
principal.application
The value of this field is taken from the
application
field.
categories
additional.fields.value.list_value.values.string_value
The value of this field is taken from the
categories
field.
clientIP
principal.ip, principal.asset.ip
The value of this field is taken from the
clientIP
field.
creationTime
This field is used to calculate the event timestamp.
custom_categories
additional.fields.value.list_value.values.string_value
The value of this field is taken from the
custom_categories
field.
dest_country
target.location.country_or_region
The value of this field is taken from the
dest_country
field.
dest_country_code
target.resource.attribute.labels.value
The value of this field is taken from the
dest_country_code
field.
dest_ip
target.ip, target.asset.ip
The value of this field is taken from the
dest_ip
field.
dest_port
target.port
The value of this field is taken from the
dest_port
field.
destinationCountry
target.location.country_or_region
The value of this field is taken from the
destinationCountry
field.
destinationIp
target.ip, target.asset.ip
The value of this field is taken from the
destinationIp
field.
destinationName
target.hostname, target.asset.hostname
The value of this field is taken from the
destinationName
field.
device_name
network.dhcp.client_hostname
The value of this field is taken from the
device_name
field.
dns_name
additional.fields.value.string_value
The value of this field is taken from the
dns_name
field.
event_count
additional.fields.value.string_value
The value of this field is taken from the
event_count
field.
event_sub_type
metadata.description
The value of this field is taken from the
event_sub_type
field.
fieldsMap.ISP_name
additional.fields.value.string_value
The value of this field is taken from the
fieldsMap.ISP_name
field.
fieldsMap.action
security_result.action_details
The value of this field is taken from the
fieldsMap.action
field.
fieldsMap.categories
security_result.category_details
The value of this field is taken from the
fieldsMap.categories
field.
fieldsMap.dest_country
target.location.country_or_region
The value of this field is taken from the
fieldsMap.dest_country
field.
fieldsMap.dest_ip
target.ip, target.asset.ip
The value of this field is taken from the
fieldsMap.dest_ip
field.
fieldsMap.dest_port
principal.port
The value of this field is taken from the
fieldsMap.dest_port
field.
fieldsMap.domain_name
principal.administrative_domain
The value of this field is taken from the
fieldsMap.domain_name
field.
fieldsMap.event_sub_type
metadata.description
The value of this field is taken from the
fieldsMap.event_sub_type
field.
fieldsMap.event_type
metadata.product_event_type
The value of this field is taken from the
fieldsMap.event_type
field.
fieldsMap.ip_protocol
network.ip_protocol
The value of this field is taken from the
fieldsMap.ip_protocol
field.
fieldsMap.os_type
This field is used to determine the operating system of the principal.
fieldsMap.pop_name
additional.fields.value.string_value
The value of this field is taken from the
fieldsMap.pop_name
field.
fieldsMap.rule_id
security_result.rule_id
The value of this field is taken from the
fieldsMap.rule_id
field.
fieldsMap.rule_name
security_result.rule_name
The value of this field is taken from the
fieldsMap.rule_name
field.
fieldsMap.src_ip
principal.ip, principal.asset.ip
The value of this field is taken from the
fieldsMap.src_ip
field.
fieldsMap.src_isp_ip
src.ip, src.asset.ip
The value of this field is taken from the
fieldsMap.src_isp_ip
field.
fieldsMap.time
This field is used to calculate the event timestamp.
file_hash
target.file.sha256
The value of this field is taken from the
file_hash
field.
file_name
target.file.full_path
The value of this field is taken from the
file_name
field.
file_size
target.file.size
The value of this field is taken from the
file_size
field.
http_host_name
principal.hostname, principal.asset.hostname
The value of this field is taken from the
http_host_name
field.
insertionDate
additional.fields.value.string_value
The value of this field is taken from the
insertionDate
field.
internalId
additional.fields.value.string_value
The value of this field is taken from the
internalId
field.
ip_protocol
network.ip_protocol
The value of this field is taken from the
ip_protocol
field.
is_sanctioned_app
security_result.detection_fields.value
The value of this field is taken from the
is_sanctioned_app
field.
os_type
principal.platform
The value of this field is taken from the
os_type
field.
pop_name
This field is used to populate the
fieldsMap.pop_name
field.
prettyType
metadata.product_event_type
The value of this field is taken from the
prettyType
field.
rule
additional.fields.value.string_value
The value of this field is taken from the
rule
field.
rule_id
security_result.rule_id
The value of this field is taken from the
rule_id
field.
rule_name
security_result.rule_name
The value of this field is taken from the
rule_name
field.
server_port
target.port
The value of this field is taken from the
server_port
field.
severity
security_result.severity_details
The value of this field is taken from the
severity
field.
sourceCountry
principal.location.country_or_region
The value of this field is taken from the
sourceCountry
field.
sourceInternalIp
principal.ip
The value of this field is taken from the
sourceInternalIp
field.
sourceIp
src.ip, src.asset.ip
The value of this field is taken from the
sourceIp
field.
sourceName
principal.user.user_display_name
The value of this field is taken from the
sourceName
field.
sport
principal.port
The value of this field is taken from the
sport
field.
src_country
This field is used to populate the
sourceCountry
field.
src_country_code
principal.resource.attribute.labels.value
The value of this field is taken from the
src_country_code
field.
src_ip
principal.ip, principal.asset.ip
The value of this field is taken from the
src_ip
field.
src_is_site_or_vpn
security_result.detection_fields.value
The value of this field is taken from the
src_is_site_or_vpn
field.
src_isp_ip
src.ip, src.asset.ip
The value of this field is taken from the
src_isp_ip
field.
src_site
additional.fields.value.string_value
The value of this field is taken from the
src_site
field.
src_site_name
additional.fields.value.string_value
The value of this field is taken from the
src_site_name
field.
start
This field is used to calculate the event timestamp.
subnet_name
additional.fields.value.string_value
The value of this field is taken from the
subnet_name
field.
time
This field is used to calculate the event timestamp.
time_str
This field is used to calculate the event timestamp.
tunnel_host_logon_names
principal.user.userid
The value of this field is taken from the
tunnel_host_logon_names
field.
URL
target.url
The value of this field is taken from the
url
field.
user_id
principal.user.userid
The value of this field is taken from the
user_id
field.
metadata.event_type
The value of this field is set to
GENERIC_EVENT
and can be overridden to
NETWORK_CONNECTION
,
NETWORK_DHCP
or
NETWORK_HTTP
based on the event.
metadata.log_type
The value of this field is set to
CATO_NETWORKS
.
metadata.product_name
The value of this field is set to
SASE
.
metadata.vendor_name
The value of this field is set to
Cato Networks
.
network.application_protocol
The value of this field is set to
DHCP
for
Connected
events.
network.dhcp.chaddr
The value of this field is set to
01:23:45:ab:cd:ef
for
Connected
events.
network.dhcp.lease_time_seconds
The value of this field is set to
86400
for
Connected
events.
network.dhcp.opcode
The value of this field is set to
BOOTREPLY
for
Connected
events.
network.dhcp.type
The value of this field is set to
ACK
for
Connected
events.
network.direction
The value of this field is set to
OUTBOUND
for
Anti Malware
and
URL Filtering
events.
security_result.action
The value of this field is set to
ALLOW
if the
action
field is not
BLOCK
, otherwise it is set to
BLOCK
.
event_type
metadata.description
The value of this field is taken from the
event_type
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
