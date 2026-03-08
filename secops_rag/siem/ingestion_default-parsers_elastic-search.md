# Collect Elasticsearch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-search/  
**Scraped:** 2026-03-05T09:23:43.605222Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Elasticsearch logs
Supported in:
Google secops
SIEM
This document explains how to ingest Elasticsearch logs to Google Security Operations using Amazon S3. The parser transforms raw JSON formatted logs into a unified data model (UDM). It extracts fields from nested JSON structures, maps them to UDM fields, and enriches the data with security-relevant context like severity levels and user roles.
Before you begin
A Google SecOps instance
Privileged access to
Elasticsearch
cluster administration
Privileged access to
AWS
(S3, IAM, EC2)
EC2 instance or persistent host to run Logstash
Get Elasticsearch prerequisites
Sign in to your
Elasticsearch cluster
as an administrator.
Verify that your Elasticsearch subscription includes
Security features
(required for audit logging).
Note your Elasticsearch cluster name and version for reference.
Identify the path where audit logs will be written (default:
$ES_HOME/logs/<clustername>_audit.json
).
Enable Elasticsearch audit logging
On each Elasticsearch node, edit the
elasticsearch.yml
configuration file.
Add the following setting:
xpack.security.audit.enabled
:
true
Perform a
rolling restart
of the cluster to apply changes:
Disable shard allocation:
PUT _cluster/settings {"persistent": {"cluster.routing.allocation.enable": "primaries"}}
Stop and restart each node one at a time.
Re-enable shard allocation:
PUT _cluster/settings {"persistent": {"cluster.routing.allocation.enable": null}}
Verify audit logs are being generated at
<clustername>_audit.json
in the logs directory.
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save bucket
Name
and
Region
for future reference (for example,
elastic-search-logs
).
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
Configure Logstash to ship audit logs to S3
Install
Logstash
on an EC2 instance or persistent host that can access the Elasticsearch audit log files.
Install the S3 output plugin if not already present:
bin/logstash-plugin
install
logstash-output-s3
Create a Logstash configuration file (
elastic-to-s3.conf
):
input
{
file
{
path
=
>
"/path/to/elasticsearch/logs/*_audit.json"
start_position
=
>
"beginning"
codec
=
>
"json"
# audit file: 1 JSON object per line
sincedb_path
=
>
"/var/lib/logstash/sincedb_elastic_search"
exclude
=
>
[
"*.gz"
]
}
}
filter
{
# Intentionally minimal: do NOT reshape audit JSON the ELASTIC_SEARCH parser expects.
# If you must add metadata for ops, put it under [@metadata] so it won't be written.
# ruby { code => "event.set('[@metadata][ingested_at]', Time.now.utc.iso8601)" }
}
output
{
s3
{
access_key_id
=
>
"YOUR_AWS_ACCESS_KEY"
secret_access_key
=
>
"YOUR_AWS_SECRET_KEY"
region
=
>
"us-east-1"
bucket
=
>
"elastic-search-logs"
prefix
=
>
"logs/%{+YYYY}/%{+MM}/%{+dd}/"
codec
=
>
"json_lines"
# NDJSON output (1 JSON object per line)
encoding
=
>
"gzip"
# compress objects
server_side_encryption
=
>
true
# Optionally for KMS:
# server_side_encryption_kms_key_id => "arn:aws:kms:REGION:ACCT:key/KEY_ID"
size_file
=
>
104857600
# 100MB rotation
time_file
=
>
300
# 5 min rotation
}
}
Start Logstash with the configuration:
bin/logstash
-f
elastic-to-s3.conf
Optional: Create read-only IAM user for Google SecOps
Go to
AWS Console
>
IAM
>
Users
>
Add users
.
Click
Add users
.
Provide the following configuration details:
User
: Enter
secops-reader
.
Access type
: Select
Access key – Programmatic access
.
Click
Create user
.
Attach minimal read policy (custom):
Users
>
secops-reader
>
Permissions
>
Add permissions
>
Attach policies directly
>
Create policy
.
In the JSON editor, enter the following policy:
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:GetObject"
],
"Resource"
:
"arn:aws:s3:::elastic-search-logs/*"
},
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:ListBucket"
],
"Resource"
:
"arn:aws:s3:::elastic-search-logs"
}
]
}
Set the name to
secops-reader-policy
.
Go to
Create policy
>
search/select
>
Next
>
Add permissions
.
Go to
Security credentials
>
Access keys
>
Create access key
.
Download the
CSV
(these values are entered into the feed).
Configure a feed in Google SecOps to ingest Elasticsearch logs
Go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Elasticsearch Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Elastic Search
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://elastic-search-logs/logs/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log field
UDM mapping
Logic
Level
security_result.severity
The logic checks the value of the "Level" field and maps it to the corresponding UDM severity level:
- "INFO", "ALL", "OFF", "TRACE", "DEBUG" are mapped to "INFORMATIONAL".
- "WARN" is mapped to "LOW".
- "ERROR" is mapped to "ERROR".
- "FATAL" is mapped to "CRITICAL".
message.@timestamp
timestamp
The timestamp is parsed from the "@timestamp" field within the "message" field of the raw log, using the format "yyyy-MM-ddTHH:mm:ss.SSS".
message.action
security_result.action_details
Value is taken from the "action" field within the "message" field of the raw log.
message.event.action
security_result.summary
Value is taken from the "event.action" field within the "message" field of the raw log.
message.event.type
metadata.product_event_type
Value is taken from the "event.type" field within the "message" field of the raw log.
message.host.ip
target.ip
Value is taken from the "host.ip" field within the "message" field of the raw log.
message.host.name
target.hostname
Value is taken from the "host.name" field within the "message" field of the raw log.
message.indices
target.labels.value
Value is taken from the "indices" field within the "message" field of the raw log.
message.mrId
target.hostname
Value is taken from the "mrId" field within the "message" field of the raw log.
message.node.id
principal.asset.product_object_id
Value is taken from the "node.id" field within the "message" field of the raw log.
message.node.name
target.asset.hostname
Value is taken from the "node.name" field within the "message" field of the raw log.
message.origin.address
principal.ip
The IP address is extracted from the "origin.address" field within the "message" field of the raw log, by removing the port number.
message.origin.type
principal.resource.resource_subtype
Value is taken from the "origin.type" field within the "message" field of the raw log.
message.properties.host_group
principal.hostname
Value is taken from the "properties.host_group" field within the "message" field of the raw log.
message.properties.host_group
target.group.group_display_name
Value is taken from the "properties.host_group" field within the "message" field of the raw log.
message.request.id
target.resource.product_object_id
Value is taken from the "request.id" field within the "message" field of the raw log.
message.request.name
target.resource.name
Value is taken from the "request.name" field within the "message" field of the raw log.
message.user.name
principal.user.userid
Value is taken from the "user.name" field within the "message" field of the raw log.
message.user.realm
principal.user.attribute.permissions.name
Value is taken from the "user.realm" field within the "message" field of the raw log.
message.user.roles
about.user.attribute.roles.name
Value is taken from the "user.roles" field within the "message" field of the raw log.
metadata.event_type
Hardcoded value: "USER_RESOURCE_ACCESS"
metadata.log_type
Hardcoded value: "ELASTIC_SEARCH"
metadata.product_name
Hardcoded value: "ELASTICSEARCH"
metadata.vendor_name
Hardcoded value: "ELASTIC"
principal.port
The port number is extracted from the "origin.address" field within the "message" field of the raw log.
target.labels.key
Hardcoded value: "Indice"
Need more help?
Get answers from Community members and Google SecOps professionals.
