# Collect Azion firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azion/  
**Scraped:** 2026-03-05T09:50:55.653266Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azion firewall logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Azion firewall JSON logs, performs data type conversions and enrichment (for example, user-agent parsing), and maps the extracted fields to the UDM. It generates
NETWORK_HTTP
,
SCAN_UNCATEGORIZED
, or
GENERIC_EVENT
events based on the presence of principal and target machines. It also handles WAF-related fields and actions, mapping them to UDM security result fields.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to AWS IAM and S3.
Privileged access to an active Azion account.
Configure Amazon S3 bucket
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
.
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
Optional: Add description tag.
Click
Create access key
.
Click
Download .csv file
. (Save
Access Key
and
Secret Access Key
for future reference).
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
Configure Azion for continuous log delivery to Amazon S3
In the Azion console, go to to the
DataStream
section.
Click
+ Stream
.
Specify values for the following parameters:
Name
: Provide a unique and descriptive name to identify the data stream.
Source
: Select the source to collect the data from.
Template
: A preset of variables for specific sources or an open template to choose variables. You have the option to filter domains.
In
Destination
section, click
Connector
>
Simple Storage Service (S3)
.
URL
: the bucket URI.
s3:/BUCKET_NAME
.
Replace the following:
BUCKET_NAME
: the name of the bucket.
Bucket Name
: Name of the bucket to which the object will be sent.
Region
: Region where your bucket is located.
Access Key
: User access key with access to the s3 bucket.
Secret Key
: User secret key with access to the s3 bucket.
Content Type
: Select plain/text.
Click
Save
.
For more information, see
How to use Amazon S3 to receive data from Data Stream
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
Azion Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select Azion as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: the bucket URI.
s3:/BUCKET_NAME
.
Replace the following:
BUCKET_NAME
: the name of the bucket.
Source deletion options
: select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Note: If you select the
Delete transferred files
or
Delete transferred files and empty directories
option, make sure that you granted appropriate permissions to the service account.
Access Key ID
: the User access key with access to the s3 bucket.
Secret Access Key
: the User secret key with access to the s3 bucket.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label to be applied to the events from this feed.
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
asn
read_only_udm.network.asn
Directly mapped from the
asn
field.
bytes_sent
read_only_udm.network.sent_bytes
Directly mapped from the
bytes_sent
field, converted to unsigned integer.
country
read_only_udm.principal.location.country_or_region
Directly mapped from the
country
field.
host
read_only_udm.principal.hostname
Directly mapped from the
host
field.
http_referer
read_only_udm.network.http.referral_url
Directly mapped from the
http_referer
field.
http_user_agent
read_only_udm.network.http.user_agent
Directly mapped from the
http_user_agent
field.
http_user_agent
read_only_udm.network.http.parsed_user_agent
Parsed from the
http_user_agent
field using the
parseduseragent
filter.
read_only_udm.event_type
Determined by the parser based on the presence of
principal
and
target
information. Can be
NETWORK_HTTP
,
SCAN_UNCATEGORIZED
, or
GENERIC_EVENT
.
read_only_udm.metadata.product_name
Hardcoded to
"AZION"
.
read_only_udm.metadata.vendor_name
Hardcoded to
"AZION"
.
read_only_udm.metadata.product_version
Hardcoded to
"AZION"
.
remote_addr
read_only_udm.principal.ip
Directly mapped from the
remote_addr
field.
remote_port
read_only_udm.principal.port
Directly mapped from the
remote_port
field, converted to integer.
requestPath
read_only_udm.target.url
Directly mapped from the
requestPath
field if
request_uri
is not present.
request_method
read_only_udm.network.http.method
Directly mapped from the
request_method
field, converted to uppercase.
request_time
read_only_udm.additional.fields
Added as a key-value pair to the
additional.fields
array, with key
"request_time"
and value from the
request_time
field.
request_uri
read_only_udm.target.url
Directly mapped from the
request_uri
field if present.
server_addr
read_only_udm.target.ip
Directly mapped from the
server_addr
field.
server_port
read_only_udm.target.port
Directly mapped from the
server_port
field, converted to integer.
ssl_cipher
read_only_udm.network.tls.cipher
Directly mapped from the
ssl_cipher
field.
ssl_protocol
read_only_udm.network.tls.version_protocol
Directly mapped from the
ssl_protocol
field.
ssl_server_name
read_only_udm.network.tls.client.server_name
Directly mapped from the
ssl_server_name
field.
state
read_only_udm.principal.location.state
Directly mapped from the
state
field.
status
read_only_udm.network.http.response_code
Directly mapped from the
status
field, converted to integer.
time
read_only_udm.metadata.event_timestamp
Parsed from the
time
field using date filter and multiple date formats.
upstream_addr
read_only_udm.intermediary.ip
,
read_only_udm.intermediary.port
Extracted from the
upstream_addr
field using grok, splitting into IP and port.
upstream_status
read_only_udm.additional.fields
Added as a key-value pair to the
additional.fields
array, with key
"upstream_status"
and value from the
upstream_status
field.
waf_args
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_attack_action
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_attack_family
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_headers
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_learning
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_match
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_score
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_server
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_total_blocked
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_total_processed
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
waf_uri
read_only_udm.security_result.detection_fields
Added as a key-value pair to the
security_result.detection_fields
array.
read_only_udm.security_result.action
Determined by the parser based on the
waf_block
or
blocked
fields. Set to
ALLOW
or
BLOCK
.
Need more help?
Get answers from Community members and Google SecOps professionals.
