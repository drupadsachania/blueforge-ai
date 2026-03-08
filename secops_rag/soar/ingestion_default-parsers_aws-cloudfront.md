# Collect Amazon CloudFront logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudfront/  
**Scraped:** 2026-03-05T09:49:41.492604Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Amazon CloudFront logs
Supported in:
Google secops
SIEM
This document describes how you can collect Amazon CloudFront logs by
setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google Security Operations overview
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
AWS_CLOUDFRONT
ingestion label.
Before you begin
Make sure that the Amazon S3 bucket is created. For more information,
see
Create your first S3 bucket
.
Configure Amazon CloudFront
Sign in to the
AWS Management
console.
Access the Amazon S3 console, and create the Amazon S3 bucket.
Click
On
to enable logging.
In the
Bucket for logs
field, specify the Amazon S3 bucket name.
In the
Log prefix
field, specify an optional prefix.
After the logs files are stored in the Amazon S3 bucket, create an SQS queue,
and attach it with the Amazon S3 bucket.
Identify the endpoints for connectivity
Check the required Identity and Access Management user and KMS key policies for S3, SQS, and KMS.
Based on the service and region, identify the endpoints for connectivity by
referring to the following AWS documentation:
For information about any logging sources, see
AWS Identity and Access Management endpoints and quotas
.
For information about S3 logging sources, see
Amazon Simple Storage Service endpoints and quotas
.
For information about SQS logging sources, see
Amazon Simple Queue Service endpoints and quotas
.
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
How to set up the AWS CloudFront feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS CloudFront
log type.
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
Field mapping reference
This parser extracts fields from AWS CloudFront logs in either SYSLOG or JSON format, normalizing them into the UDM. It uses grok patterns to parse message strings, handles various data transformations (e.g., type conversions, renaming), and enriches the data with additional context like user agent parsing and application protocol identification.
UDM mapping table
Log Field
UDM Mapping
Logic
c-ip
principal.ip
Directly mapped. Also mapped to
principal.asset.ip
.
c-port
principal.port
Directly mapped.
cs(Cookie)
additional.fields[].key
: "cookie"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if
cs(Cookie)
is present and
agent
does not contain "://".
cs(Host)
principal.hostname
Directly mapped. Also mapped to
principal.asset.hostname
.  Used in constructing the
target.url
if other URL fields are not available.
cs(Referer)
network.http.referral_url
Directly mapped.
cs(User-Agent)
network.http.user_agent
Directly mapped. Also mapped to
network.http.parsed_user_agent
and parsed into its components if it does not contain "://".
cs-bytes
network.sent_bytes
Directly mapped. Converted to unsigned integer.
cs-method
network.http.method
Directly mapped.
cs-protocol
network.application_protocol
Mapped after converting to uppercase. If the value is not recognized as a standard application protocol and
cs-protocol-version
contains "HTTP", then
network.application_protocol
is set to "HTTP".
dport
target.port
Directly mapped. Converted to integer.
edge_location
principal.location.name
Directly mapped.
fle-encrypted-fields
additional.fields[].key
: "fle-encrypted-fields"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
fle-status
additional.fields[].key
: "fle-status"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
host
principal.hostname
,
principal.asset.hostname
Directly mapped.
id
principal.asset_id
Directly mapped with the prefix "id: ".
ip
target.ip
,
target.asset.ip
Directly mapped.
log_id
metadata.product_log_id
Directly mapped.
resource
additional.fields[].key
: "resource"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
result_type
additional.fields[].key
: "result_type"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
sc-bytes
network.received_bytes
Directly mapped. Converted to unsigned integer.
sc-content-len
additional.fields[].key
: "sc-content-len"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
sc-content-type
additional.fields[].key
: "sc-content-type"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
sc-status
network.http.response_code
Directly mapped. Converted to integer.
ssl-cipher
network.tls.cipher
Directly mapped.
ssl-protocol
network.tls.version
Directly mapped.
timestamp
metadata.event_timestamp
Parsed and mapped if available.  Different formats are supported.
ts
metadata.event_timestamp
Parsed and mapped if available. ISO8601 format is expected.
url
target.url
Directly mapped.
url_back_to_product
metadata.url_back_to_product
Directly mapped.
x-edge-detailed-result-type
additional.fields[].key
: "x-edge-detailed-result-type"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
x-edge-location
additional.fields[].key
: "x-edge-location"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
x-edge-request-id
additional.fields[].key
: "x-edge-request-id"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
x-edge-response-result-type
additional.fields[].key
: "x-edge-response-result-type"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
x-edge-result-type
additional.fields[].key
: "x-edge-result-type"
additional.fields[].value.string_value
: Directly mapped.
Conditionally mapped if present.
x-forwarded-for
target.ip
,
target.asset.ip
Directly mapped. If multiple IPs are present (comma-separated), they are split and merged into the respective UDM fields.
x-host-header
target.hostname
,
target.asset.hostname
Directly mapped. Set to "NETWORK_HTTP" if either
ip
or
x-forwarded-for
and
http_verb
are present. Otherwise, set to "GENERIC_EVENT". Hardcoded to "AWS_CLOUDFRONT". Hardcoded to "AWS CloudFront". Hardcoded to "AMAZON". The ingestion time of the log entry into Google Security Operations.
Need more help?
Get answers from Community members and Google SecOps professionals.
