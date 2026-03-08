# Collect AWS Elastic Load Balancer logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-elb/  
**Scraped:** 2026-03-05T09:50:32.195946Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Elastic Load Balancer logs
Supported in:
Google secops
SIEM
This document explains how to collect AWS Elastic Load Balancer logs by setting up a Google Security Operations feed. The parser converts the logs into UDM format. It uses grok patterns to extract fields from both CEF and non-CEF formatted messages, mapping them to UDM fields and handling various data transformations, including specific logic for HTTP, TLS, and security-related fields. It also performs conditional processing based on the presence or format of certain fields to ensure accurate UDM representation.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure AWS Elastic Load Balancer
Enable access logging to send Access Logs to an S3 storage bucket
Create an Amazon Simple Queue Service (SQS) and attach it to an S3 storage bucket.
Configure Amazon S3 bucket
Sign in to the AWS console.
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
Save the bucket
Name
(for example,
elb-logs
) and
Region
for later use.
Create a user following this user guide:
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
as the
Use case
.
Click
Next
.
Optional: add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
Access Key
and
Secret Access Key
for later use.
Click
Done
.
Select the
Permissions
tab.
Click
Add permissions
in the
Permissions policies
section.
Select
Add permissions
.
Select
Attach policies directly
.
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
How to configure AWS Elastic Load Balancer to Enable Access Logs
Sign in to the AWS Management Console.
Search for and select
EC2
.
Select
Load balancers
in the navigation menu.
Select the
load balancer
for which you want to enable logging.
In the
Description
tab, scroll to
Attributes
.
Click
Edit attributes
.
Enable Access logs by selecting
Enable
.
Select the
S3 bucket
created earlier (for example,
elb-logs
).
Optional: set the Log Prefix for easier log identification (for example,
elb/access-logs/
).
Click
Save
.
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
How to set up the AWS Elastic Load Balancer feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Elastic Load Balancer
log type.
Specify the values in the following fields.
Specify the values in the following fields.
Source Type
: Amazon SQS V2
Queue Name
: The SQS queue name to read from
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
SQS Queue Access Key ID
: An account access key that is a 20-character alphanumeric string.
SQS Queue Secret Access Key
: An account access key that is a 40-character alphanumeric string.
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
Log Field
UDM Mapping
Logic
actions_executed
security_result.action
If
actions_executed
is "waf,forward" or "waf,redirect", set to "ALLOW". If
actions_executed
is "waf", set to "BLOCK".
chosen_cert_arn
principal.user.attribute.labels
If
chosen_cert_arn
contains "session", map its value to
security_result.description
. Otherwise, create a label with key "ARN" and value as
chosen_cert_arn
and add it to the
principal.user.attribute.labels
array.
chosen_cert_arn
security_result.description
If
chosen_cert_arn
contains "session", map its value to this field.
client_ip
principal.asset.ip
Directly mapped.
client_ip
principal.ip
Directly mapped.
client_port
principal.port
Directly mapped.
classification
security_result.rule_name
Directly mapped if not empty or "-".
classification_reason
security_result.summary
Directly mapped if not empty or "-".
Customer
(CEF)
principal.user.user_display_name
Directly mapped from the CEF field.
data
Various
Parsed using grok patterns to extract multiple fields. See other rows for specific mappings.
data.act
(CEF)
security_result.action_details
Directly mapped from the CEF field.
data.app
(CEF)
principal.application
Directly mapped from the CEF field.
data.ccode
(CEF)
principal.location.country
Directly mapped from the CEF field.
data.cicode
(CEF)
principal.location.city
Directly mapped from the CEF field.
data.cn1
(CEF)
network.http.response_code
Directly mapped from the CEF field.
data.cpt
(CEF)
principal.port
Directly mapped from the CEF field.
data.cs1Label
(CEF)
additional.fields
Creates a key-value pair with key "Cap Support" and value from
cs1Label
.
data.cs2Label
(CEF)
additional.fields
Creates a key-value pair with key "Javascript Support" and value from
cs2Label
.
data.cs3Label
(CEF)
additional.fields
Creates a key-value pair with key "CO Support" and value from
cs3Label
.
data.cs4Label
(CEF)
additional.fields
Creates a key-value pair with key "VID" and value from
cs4Label
.
data.cs5Label
(CEF)
additional.fields
Creates a key-value pair with key "clappsig" and value from
cs5Label
.
data.cs6Label
(CEF)
additional.fields
Creates a key-value pair with key "clapp" and value from
cs6Label
.
data.cs7Label
(CEF)
additional.fields
Creates a key-value pair with key "latitude" and value from
cs7Label
.
data.deviceExternalId
(CEF)
about.asset.asset_id
Used as part of the asset ID:
Incapsula.SIEMintegration:deviceExternalId
.
data.deviceFacility
(CEF)
principal.location.region
Directly mapped from the CEF field.
data.dproc
(CEF)
target.process.command_line
Directly mapped from the CEF field.
data.dst_ip
target.asset.ip
Directly mapped.
data.dst_ip
target.ip
Directly mapped.
data.dst_port
target.port
Directly mapped.
data.elb
target.resource.id
Directly mapped.
data.fileId
(CEF)
security_result.detection_fields
Creates a key-value pair with key "fileId" and value from
fileId
.
data.in
(CEF)
network.received_bytes
Directly mapped from the CEF field.
data.request
(CEF)
target.url
Directly mapped from the CEF field.
data.requestClientApplication
(CEF)
network.http.user_agent
Directly mapped from the CEF field.
data.requestMethod
(CEF)
network.http.method
Directly mapped from the CEF field.
data.severity
(CEF)
security_result.severity
Mapped to LOW if severity is 0.
data.sip
(CEF)
principal.asset.ip
Directly mapped from the CEF field.
data.sip
(CEF)
principal.ip
Directly mapped from the CEF field.
data.siteid
(CEF)
security_result.detection_fields
Creates a key-value pair with key "siteid" and value from
siteid
.
data.sourceServiceName
(CEF)
principal.application
Directly mapped from the CEF field.
data.spt
(CEF)
principal.port
Directly mapped from the CEF field.
data.src
(CEF)
principal.ip
Directly mapped from the CEF field.
data.suid
(CEF)
principal.user.userid
Directly mapped from the CEF field.
data.ver
(CEF)
network.tls.version
The version part is extracted using grok and mapped.
data.ver
(CEF)
network.tls.cipher
The cipher part is extracted using grok and mapped.
data.xff
(CEF)
principal.ip
Directly mapped from the CEF field.
domain_name
principal.administrative_domain
Directly mapped.
http_method
network.http.method
Directly mapped.
log_type
metadata.log_type
Directly mapped.
message
Various
Parsed using grok patterns to extract multiple fields. See other rows for specific mappings.
received_bytes
network.received_bytes
Directly mapped.
redirect_url
network.application_protocol
If
redirect_url
starts with "http", the protocol is extracted and mapped.
redirect_url
target.asset.hostname
If
redirect_url
starts with "http", the hostname is extracted and mapped.
redirect_url
target.hostname
If
redirect_url
starts with "http", the hostname is extracted and mapped.
redirect_url
target.port
If
redirect_url
starts with "http", the port is extracted and mapped.
request_creation_time
metadata.collected_timestamp
Directly mapped after date parsing.
request_processing_time
security_result.detection_fields
Creates a key-value pair with key "request_processing_time" and value from this field.
response_processing_time
security_result.detection_fields
Creates a key-value pair with key "response_processing_time" and value from this field.
sent_bytes
network.sent_bytes
Directly mapped.
ssl_cipher
network.tls.cipher
Directly mapped.
ssl_protocol
network.tls.version
Directly mapped.
target_group_arn
target.group.group_display_name
Directly mapped.
target_processing_time
security_result.detection_fields
Creates a key-value pair with key "target_processing_time" and value from this field.
target_status_code
target.labels
Creates a label with key "target_status_code" and value from this field, and adds it to the
target.labels
array.
time
metadata.event_timestamp
Directly mapped after date parsing.
trace_id
metadata.product_log_id
Directly mapped after removing "Root=".
url
network.http.referral_url
Directly mapped.
user_agent
network.http.user_agent
Directly mapped.
(Parser)
metadata.event_type
Set to "NETWORK_HTTP" if principal and target machine IDs are present, "STATUS_UPDATE" if only principal machine ID is present, "GENERIC_EVENT" if no target IP, hostname, or destination IP is present, and "NETWORK_HTTP" otherwise.
(Parser)
metadata.product_name
Set to "AWS Elastic Load Balancer".
(Parser)
metadata.vendor_name
Set to "AMAZON".
Need more help?
Get answers from Community members and Google SecOps professionals.
