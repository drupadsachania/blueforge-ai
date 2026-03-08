# Collect Elastic Auditbeat logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-auditbeat/  
**Scraped:** 2026-03-05T09:23:40.194943Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Elastic Auditbeat logs
Supported in:
Google secops
SIEM
This document explains how to ingest Elastic Auditbeat logs to
Google Security Operations using Amazon S3. The parser extracts fields from the
JSON logs, normalizes them into the Unified Data Model (UDM), and enriches the
data with additional context like host information, network details, and security
result classifications. It handles various event types by mapping
event1.action
and other fields to specific UDM metadata event types, defaulting to
GENERIC_EVENT
or more specific categories when possible.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
Privileged access to
Elastic Auditbeat
server.
Privileged access to
Logstash
server.
Privileged access to
AWS
(S3, Identity and Access Management (IAM)).
Get Elastic Auditbeat prerequisites
Make sure
Elastic Auditbeat
is installed and configured on your servers.
Install
Logstash
on a dedicated server or alongside Auditbeat.
Note the Auditbeat configuration file location (typically
/etc/auditbeat/auditbeat.yml
).
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
elastic-auditbeat-logs
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
Optional: Add description tag.
Click
Create access key
.
Click
Download .CSV file
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
Configure Auditbeat to send to Logstash
Edit the Auditbeat configuration file
/etc/auditbeat/auditbeat.yml
.
Comment out any existing output configuration (Elasticsearch, etc.).
Add the Logstash output configuration:
# ==================== Outputs ====================
output.logstash
:
hosts
:
[
"localhost:5044"
]
# If Logstash is on a different server, use its IP/hostname
# hosts: ["logstash-server:5044"]
# Optional: Enable load balancing if using multiple Logstash instances
loadbalance
:
true
# Optional: Configure bulk settings (default is 2048)
bulk_max_size
:
2048
# Optional: Configure SSL if needed
# ssl.enabled: true
# ssl.certificate_authorities: ["/path/to/ca.crt"]
Restart Auditbeat to apply changes:
sudo
systemctl
restart
auditbeat
Configure Logstash pipeline
Create a new Logstash pipeline configuration file
/etc/logstash/conf.d/auditbeat-to-s3.conf
:
input
{
beats
{
port
=
>
5044
# Optional: Configure SSL
# ssl => true
# ssl_certificate => "/path/to/server.crt"
# ssl_key => "/path/to/server.key"
}
}
filter
{
# Add any necessary transformations here
# The data should remain in raw JSON format for Chronicle parsing
# Optional: Add metadata for debugging
mutate
{
add_field
=
>
{
"[@metadata][pipeline]"
=
>
"auditbeat-to-s3"
}
}
}
output
{
s3
{
# AWS credentials
access_key_id
=
>
"YOUR_AWS_ACCESS_KEY_ID"
secret_access_key
=
>
"YOUR_AWS_SECRET_ACCESS_KEY"
# S3 bucket configuration
region
=
>
"us-east-1"
# Replace with your bucket region
bucket
=
>
"elastic-auditbeat-logs"
# Replace with your bucket name
# Organize logs by date using Logstash timestamp interpolation
prefix
=
>
"auditbeat/%{+YYYY}/%{+MM}/%{+dd}/"
# File rotation settings
size_file
=
>
10485760
# 10MB files
time_file
=
>
5
# Rotate every 5 minutes
# Compression for cost optimization
encoding
=
>
"gzip"
# Output format - keep as JSON for Chronicle
codec
=
>
"json_lines"
# Optional: Server-side encryption
# server_side_encryption => true
# server_side_encryption_algorithm => "AES256"
}
# Optional: Keep a local copy for debugging
# stdout {
#   codec => rubydebug
# }
}
Replace
YOUR_AWS_ACCESS_KEY_ID
and
YOUR_AWS_SECRET_ACCESS_KEY
with your actual AWS credentials.
Update the
region
and
bucket
values to match your S3 configuration.
Start or restart Logstash:
sudo
systemctl
restart
logstash
(Optional) Create read-only IAM user & keys for Google SecOps
Go to
AWS Console
>
IAM
>
Users
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
JSON:
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
"arn:aws:s3:::elastic-auditbeat-logs/*"
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
"arn:aws:s3:::elastic-auditbeat-logs"
}
]
}
Name =
secops-reader-policy
.
Click
Create policy
>
search/select
>
Next
>
Add permissions
.
Create access key for
secops-reader
:
Security credentials
>
Access keys
.
Click
Create access key
.
Download the
.CSV
. (You'll paste these values into the feed).
Configure a feed in Google SecOps to ingest Elastic Auditbeat logs
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
Elastic Auditbeat Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Elastic Audit Beats
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://elastic-auditbeat-logs/auditbeat/
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
UDM mapping table
Log field
UDM mapping
Logic
@timestamp
metadata.event_timestamp
The event timestamp is parsed from the
@timestamp
field.
agent.id
observer.asset_id
Prefixed with "agent_id: ".
agent.type
observer.application
The observer application is set to the agent type.
agent.version
observer.platform_version
The observer platform version is set to the agent version.
client.bytes
principal.labels
Added as a label with key "Bytes". Converted to string.
client.ip
principal.ip
The principal IP is set to the client IP.
client.packets
principal.labels
Added as a label with key "Packets". Converted to string.
client.port
principal.port
The principal port is set to the client port. Converted to integer.
cloud.availability_zone
principal.cloud.availability_zone
The principal cloud availability zone is set to the cloud availability zone.
cloud.instance.id
principal.resource.id
The principal resource ID is set to the cloud instance ID.
cloud.machine.type
principal.resource.resource_subtype
The principal resource subtype is set to the cloud machine type.
cloud.region
principal.cloud.availability_zone
If cloud region is present, it overrides the availability zone.
destination.bytes
target.labels
Added as a label with key "Bytes". Converted to string.
destination.ip
target.ip
The target IP is set to the destination IP.
destination.packets
target.labels
Added as a label with key "Packets". Converted to string.
destination.port
target.port
The target port is set to the destination port. Converted to integer.
ecs.version
metadata.product_version
If present, overrides the value from
jsonPayload.@metadata.version
.
event1.category
security_result.category_details
All values are added to category_details.
event1.duration
network.session_duration.seconds
Converted to integer.
event1.id
metadata.product_log_id
The metadata product log ID is set to the event ID.
event1.outcome
extensions.auth.auth_details
The auth details are set to the event outcome.
file.extension
target.file.mime_type
The target file MIME type is set to the file extension.
file.hash.sha1
target.file.sha1
The target file SHA-1 is set to the file SHA-1 hash.
file.path
target.file.full_path
The target file full path is set to the path.
file.size
target.file.size
Converted to uinteger.
group.id
principal.group.product_object_id
The principal group product object ID is set to the group ID.
group.name
principal.group.group_display_name
The principal group display name is set to the group name.
host.architecture
principal.asset.hardware.cpu_platform
Stored in temporary variable
hardware.cpu_platform
and then merged into
principal.asset.hardware
.
host.hostname
principal.hostname
The principal hostname is set to the host hostname.
host.id
principal.asset.asset_id
Prefixed with "Host Id: ".
host.ip
principal.asset.ip
All values are added to the principal asset IPs.
host.mac
principal.mac
Dashes are replaced with colons.
host.name
principal.hostname
,
observer.hostname
If present, overrides the value from
host.hostname
.
host.os.kernel
principal.platform_patch_level
The principal platform patch level is set to the host OS kernel.
host.os.version
principal.platform_version
The principal platform version is set to the host OS version. Stored in temporary variable
host_os_version
.
httpRequest.remoteIp
target.ip
If present, and no other target IP is set, this value is used.
httpRequest.requestMethod
network.http.method
The network HTTP method is set to the HTTP request method.
httpRequest.requestSize
network.sent_bytes
Converted to uinteger.
httpRequest.requestUrl
network.http.referral_url
The network HTTP referral URL is set to the HTTP request URL.
httpRequest.responseSize
network.received_bytes
Converted to uinteger.
httpRequest.serverIp
principal.ip
If present, and no other principal IP is set, this value is used.
httpRequest.status
network.http.response_code
Converted to integer.
httpRequest.userAgent
network.http.user_agent
The network HTTP user agent is set to the HTTP request user agent.
insertId
network.session_id
The network session ID is set to the insert ID.
jsonPayload.@metadata.beat
metadata.product_event_type
The metadata product event type is set to the metadata beat.
jsonPayload.@metadata.version
metadata.product_version
The metadata product version is set to the metadata version.
jsonPayload.destination.ip
target.ip
If present, and no other target IP is set, this value is used.
jsonPayload.destination.port
target.port
If present, and no other target port is set, this value is used. Converted to integer.
jsonPayload.event1.category
security_result.category_details
All values are added to category_details.
jsonPayload.file.path
target.file.full_path
If present, and no other target path is set, this value is used.
jsonPayload.process.executable
principal.process.file.full_path
,
target.process.file.full_path
Used to set both principal and target process full path if no other value is present.
jsonPayload.process.name
principal.application
If present, and no other principal application is set, this value is used.
jsonPayload.process.parent.pid
principal.process.pid
If present, and no other principal process PID is set, this value is used. Converted to string.
jsonPayload.process.parent.ppid
principal.process.parent_process.pid
If present, and no other principal parent process PID is set, this value is used. Converted to string.
jsonPayload.process.parent.process.executable
principal.process.file.full_path
If present, and no other principal process full path is set, this value is used.
jsonPayload.process.parent.process.exe
principal.process.file.full_path
If present, and no other principal process full path is set, this value is used.
jsonPayload.process.parent.process.title
principal.process.command_line
If present, and no other principal process command line is set, this value is used.
jsonPayload.process.pid
target.process.pid
The target process PID is set to the JSON payload process PID.
jsonPayload.process.title
target.process.command_line
The target process command line is set to the JSON payload process title.
jsonPayload.user.id
target.user.userid
If present, and no other target user ID is set, this value is used. Converted to string.
jsonPayload.user.name
target.user.user_display_name
If present, and no other target user display name is set, this value is used.
msg
metadata.description
The metadata description is set to the message.
network.bytes
network.sent_bytes
Converted to uinteger.
network.community_id
network.community_id
The network community ID is set to the network community ID.
network.transport
network.ip_protocol
Converted to uppercase.
package.description
security_result.description
The security result description is set to the package description.
package.name
security_result.rule_name
The security result rule name is set to the package name.
package.reference
security_result.about.url
The security result URL is set to the package reference.
package.size
security_result.about.file.size
Converted to uinteger.
package.type
security_result.about.file.mime_type
,
security_result.rule_type
The security result MIME type and rule type are set to the package type.
process.created
principal.asset.creation_time
If present, this value is used. Parsed as ISO8601.
process.entity_id
principal.process.product_specific_process_id
Prefixed with "Process:".
process.executable
principal.process.file.full_path
,
target.process.file.full_path
Used to set both principal and target process full path if no other value is present.
process.hash.sha1
principal.process.file.sha1
The principal process SHA-1 is set to the process SHA-1 hash.
process.name
principal.application
If present, and no other principal application is set, this value is used.
process.pid
principal.process.pid
If present, and no other principal process PID is set, this value is used. Converted to string.
process.ppid
principal.process.parent_process.pid
If present, and no other principal parent process PID is set, this value is used. Converted to string.
process.start
principal.asset.creation_time
If
process.created
is not present, and this field is present, this value is used. Parsed as ISO8601.
resource.labels.backend_service_name
target.resource.name
The target resource name is set to the resource backend service name.
resource.labels.forwarding_rule_name
target.resource.attribute.labels
Added as a label with key "Forwarding rule name".
resource.labels.project_id
target.resource.product_object_id
The target resource product object ID is set to the resource project ID.
resource.labels.target_proxy_name
target.resource.attribute.labels
Added as a label with key "Target proxy name".
resource.labels.url_map_name
target.resource.attribute.labels
Added as a label with key "URL map name".
server.bytes
intermediary.labels
Added as a label with key "Bytes". Converted to string.
server.ip
intermediary.ip
The intermediary IP is set to the server IP.
server.packets
intermediary.labels
Added as a label with key "Packets". Converted to string.
server.port
intermediary.port
The intermediary port is set to the server port. Converted to integer.
service.type
target.application
The target application is set to the service type.
source.bytes
src.labels
Added as a label with key "Bytes". Converted to string.
source.ip
src.ip
The source IP is set to the source IP.
source.packets
src.labels
Added as a label with key "Packets". Converted to string.
source.port
src.port
The source port is set to the source port. Converted to integer.
system.audit.host.boottime
about.asset.last_boot_time
Parsed as ISO8601.
system.audit.host.hostname
about.hostname
The about hostname is set to the system audit host hostname.
system.audit.host.id
principal.user.userid
The principal user ID is set to the system audit host ID.
system.audit.host.mac.0
about.mac
The about MAC address is set to the first system audit host MAC address.
trace
target.process.file.full_path
If present, and no other target process full path is set, this value is used.
user.effective.id
target.user.userid
If present, and no other target user ID is set, this value is used.
user.effective.name
target.user.user_display_name
If present, and no other target user display name is set, this value is used.
user.id
target.user.userid
If present, and no other target user ID is set, this value is used. Converted to string.
user.name
target.user.user_display_name
If present, and no other target user display name is set, this value is used.
N/A
metadata.event_type
Set to "GENERIC_EVENT" initially. Changed based on the logic described in the parser code comments.
N/A
metadata.log_type
Set to "ELASTIC_AUDITBEAT".
N/A
metadata.product_name
Set to "Auditbeat".
N/A
metadata.vendor_name
Set to "Elastic".
N/A
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" for USER_LOGIN and USER_LOGOUT events.
auditd.data.syscall
metadata.product_event_type
The metadata product event type is set to the auditd syscall.
Need more help?
Get answers from Community members and Google SecOps professionals.
