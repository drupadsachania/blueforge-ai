# Collect VMware vRealize logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vrealize/  
**Scraped:** 2026-03-05T10:02:21.164464Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware vRealize logs
Supported in:
Google secops
SIEM
This document explains how to ingest VMware Aria Suite (previously known as VMware vRealize) logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages using grok patterns based on the
msg_type
field. It then maps these extracted fields to the UDM, handling various log formats and enriching the data with additional context like network information, user details, and resource attributes.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the VMware Aria Suite software
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the
system where Bindplane will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
Windows installation
Open the
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'VMWARE_VREALIZE'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog for VMware Aria Suite
Sign in to the
VMware Aria Suite
web UI.
Go to
Management
>
Event Forwarding
.
Click
New Destination
.
Provide the following configuration details:
Name
: Enter a unique name to identify the server.
Host
: Enter the Bindplane agent IP address.
Protocol
: Select
Syslog
.
Transport
: Select
UDP
or
TCP
, depending on your actual Bindplane agent configuration.
Port
: Enter the Bindplane agent port number.
Click
Test
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
actorDomain
principal.hostname
The value of
actorDomain
from the raw log is mapped to the UDM field.
actorId
principal.resource.attribute.labels.key
The string "actorId" is assigned to the key.
actorId
principal.resource.attribute.labels.value
The value of
actorId
from the raw log is assigned to the value.
actorId
additional.fields.key
The string "actorId" is assigned to the key.
actorId
additional.fields.value.string_value
The value of
actorId
from the raw log is assigned to the value.
actorUserName
principal.user.userid
The value of
actorUserName
from the raw log is mapped to the UDM field.
actorUuid
principal.resource.attribute.labels.key
The string "actorUuid" is assigned to the key.
actorUuid
principal.resource.attribute.labels.value
The value of
actorUuid
from the raw log is assigned to the value.
actorUuid
additional.fields.key
The string "actorUuid" is assigned to the key.
actorUuid
additional.fields.value.string_value
The value of
actorUuid
from the raw log is assigned to the value.
all_request_headers.sec-ch-ua-platform
principal.platform
The value is derived from
all_request_headers.sec-ch-ua-platform
. If it contains "win" or "windows" (case-insensitive), the value is "WINDOWS". If it contains "Mac" (case-insensitive), the value is "MAC". If it contains "lin" or "linux" (case-insensitive), the value is "LINUX".
all_request_headers.X-Requested-With
network.application_protocol
If the value contains "http" (case-insensitive), the value is set to "HTTP".
automation_tag
metadata.product_event_type
The value of
automation_tag
from the raw log is mapped to the UDM field.
client_ip
principal.ip
The value of
client_ip
from the raw log is mapped to the UDM field.
client_src_port
principal.port
The value of
client_src_port
from the raw log is mapped to the UDM field.
comp
about.resource.attribute.labels.key
The string "Component" is assigned to the key.
comp
about.resource.attribute.labels.value
The value of
comp
from the raw log is assigned to the value.
compression
additional.fields.key
The string "compression" is assigned to the key.
compression
additional.fields.value.string_value
The value of
compression
from the raw log is assigned to the value.
data
about.resource.attribute.labels.key
Logic depends on
msg_type
. If
msg_type
is "Vpxa", "Hostd", or "VSANMGMTSVC", the
data
field is parsed using key-value pairs, and specific keys (like
opID
,
sub
) are mapped to
about.resource.attribute.labels
. If
msg_type
is "SWITCHING", "FABRIC", "MONITORING", "SYSTEM", "ROUTING", "LOAD", "nsx", "nestdb", "cfgAgent", "NSX", or "NSXV", the
data
field is parsed for keys like
comp
,
subcomp
,
s2comp
, which are then mapped to
about.resource.attribute.labels
.
data
about.resource.attribute.labels.value
See logic for
about.resource.attribute.labels.key
.
data
security_result.description
If
msg_type
is "Vpxa", "Hostd", or "VSANMGMTSVC", and after parsing
data
for key-value pairs, if a
msg
field exists, its value is assigned to
security_result.description
.
description
security_result.description
If the
description
field exists in the raw log, its value is mapped to the UDM field.
deviceId
principal.resource.attribute.labels.key
The string "deviceType" is assigned to the key.
deviceId
principal.resource.attribute.labels.value
The value of
values.deviceType
from the raw log is assigned to the value.
deviceId
additional.fields.key
The string "deviceType" is assigned to the key.
deviceId
additional.fields.value.string_value
The value of
values.deviceType
from the raw log is assigned to the value.
direction
network.direction
If the value is "OUT", it's mapped to "OUTBOUND". If it's "IN", it's mapped to "INBOUND".
dst_ip
target.ip
The value of
dst_ip
from the raw log is mapped to the UDM field.
dst_port
target.port
The value of
dst_port
from the raw log is mapped to the UDM field.
event_source
principal.url
The value of
event_source
from the raw log is mapped to the UDM field.
headers_received_from_server.Access-Control-Allow-Origin
target.resource.attribute.labels.key
The string "headers_received_from_server.Access-Control-Allow-Origin" is assigned to the key.
headers_received_from_server.Access-Control-Allow-Origin
target.resource.attribute.labels.value
The value of
headers_received_from_server.Access-Control-Allow-Origin
from the raw log is assigned to the value.
headers_received_from_server.Content-Security-Policy
principal.resource.attribute.labels.key
The string "headers_received_from_server.Content-Security-Policy" is assigned to the key.
headers_received_from_server.Content-Security-Policy
principal.resource.attribute.labels.value
The value of
headers_received_from_server.Content-Security-Policy
from the raw log is assigned to the value.
headers_received_from_server.Cookie
target.resource.attribute.labels.key
The string "headers_received_from_server.Cookie" is assigned to the key.
headers_received_from_server.Cookie
target.resource.attribute.labels.value
The value of
headers_sent_to_server.Cookie
from the raw log is assigned to the value.
headers_received_from_server.set-cookie
target.resource.attribute.labels.key
The string "headers_received_from_server.set-cookie" is assigned to the key.
headers_received_from_server.set-cookie
target.resource.attribute.labels.value
The value of
headers_received_from_server.set-cookie
from the raw log is assigned to the value.
headers_sent_to_server.sec-ch-ua
principal.resource.attribute.labels.key
The string "headers_sent_to_server.sec-ch-ua" is assigned to the key.
headers_sent_to_server.sec-ch-ua
principal.resource.attribute.labels.value
The value of
headers_sent_to_server.sec-ch-ua
from the raw log is assigned to the value.
headers_sent_to_server.X-CSRF-TOKEN
principal.resource.attribute.labels.key
The string "headers_sent_to_server.X-CSRF-TOKEN" is assigned to the key.
headers_sent_to_server.X-CSRF-TOKEN
principal.resource.attribute.labels.value
The value of
headers_sent_to_server.X-CSRF-TOKEN
from the raw log is assigned to the value.
hostname
principal.hostname
The value of
hostname
from the raw log is mapped to the UDM field.
hostname
intermediary.hostname
The value of
hostname
from the raw log is mapped to the UDM field.
host
principal.hostname
The value of
host
from the raw log is mapped to the UDM field.
isLocal
additional.fields.key
The string "isLocal" is assigned to the key.
isLocal
additional.fields.value.string_value
The value of
isLocal
from the raw log is assigned to the value.
json_data
Various fields within
principal
,
target
,
additional
, and
security_result
The
json_data
field from the raw log is parsed as JSON, and the extracted fields are mapped to various UDM fields based on their names and the parser's logic.  This includes fields like
uuid
,
tenantId
,
actorId
,
actorUserName
,
actorDomain
,
sourceIp
,
objectName
,
objectType
,
objectId
,
values.resourceType
,
values.success
, and others.
kv_data
Various fields
The
kv_data
field is parsed as key-value pairs, and the extracted fields are mapped to various UDM fields based on their names and the parser's logic.
level
security_result.severity
If the value is "info" (case-insensitive), it's mapped to "INFORMATIONAL".
log_id
metadata.product_log_id
The value of
log_id
from the raw log is mapped to the UDM field.
message
Various fields
The
message
field is the main source of data and is parsed extensively using
grok
patterns to extract various fields like
ts
,
hostname
,
msg_type
,
sub_msg
, and others. These extracted fields are then used to populate different UDM fields based on the parser's logic.
method
network.http.method
The value of
method
from the raw log is mapped to the UDM field.
msg
security_result.description
If
msg_type
is "Vpxa", "Hostd", "VSANMGMTSVC", "SWITCHING", "FABRIC", "ROUTING", "LOAD-BALANCER", "nsx", "nestdb", "cfgAgent", "NSX", "NSXV", or "Rhttpproxy", and after any relevant
grok
parsing, if the
msg
field exists, its value is assigned to
security_result.description
.  There are special cases within this logic for specific message content like "keepalive connection".
msg_type
metadata.product_event_type
If
msg_type
is "FIREWALL_PKTLOG" or "FIREWALL-PKTLOG", its value is mapped to the UDM field.
msg_type
event_type
The value of
event_type
is determined based on the
msg_type
. If
msg_type
is "FIREWALL_PKTLOG" or "FIREWALL-PKTLOG", the
event_type
is "NETWORK_CONNECTION". If
msg_type
is "Vpxa", "Hostd", "VSANMGMTSVC", "nsx", "LOAD", "ROUTING", "SWITCHING", "FABRIC", "MONITORING", "SYSTEM", "nestdb", "cfgAgent", "NSX", "NSXV", "Rhttpproxy", "audispd", or "vsantraceUrgent", the
event_type
is "GENERIC_EVENT". If
msg_type
is "queries" or "responses", the
event_type
is "NETWORK_DNS". If
msg_type
is "sudo", the
event_type
is "STATUS_UPDATE". If the
description
field contains "cmmdsTimeMachineDump", the
event_type
is "GENERIC_EVENT". If the
description
field contains "prodjbossapp", the
event_type
is "GENERIC_EVENT". If the
description
field contains "liagent@6876", the
event_type
is "GENERIC_EVENT". If none of the above conditions are met and the
description
field is not empty, the
event_type
is "GENERIC_EVENT". If
src_ip
and
dst_ip
are both present, the
event_type
is "NETWORK_CONNECTION". If
src_ip
or
dst_ip
or
hostname
is present, the
event_type
is "STATUS_UPDATE". If
has_principal_ip
is true and
has_target_ip
is true, the
event_type
is "SCAN_UNCATEGORIZED". If
has_principal_ip
is true or
has_principal_host
is true, the
event_type
is "STATUS_UPDATE". If none of the above conditions are met, the
event_type
is "GENERIC_EVENT".
objectName
target.resource.attribute.labels.key
The string "objectName" is assigned to the key.
objectName
target.resource.attribute.labels.value
The value of
objectName
from the raw log is assigned to the value.
objectName
additional.fields.key
The string "objectName" is assigned to the key.
objectName
additional.fields.value.string_value
The value of
objectName
from the raw log is assigned to the value.
objectId
target.resource.attribute.labels.key
The string "objectId" is assigned to the key.
objectId
target.resource.attribute.labels.value
The value of
objectId
from the raw log is assigned to the value.
objectId
additional.fields.key
The string "objectId" is assigned to the key.
objectId
additional.fields.value.string_value
The value of
objectId
from the raw log is assigned to the value.
objectType
target.resource.attribute.labels.key
The string "objectType" is assigned to the key.
objectType
target.resource.attribute.labels.value
The value of
objectType
from the raw log is assigned to the value.
objectType
additional.fields.key
The string "objectType" is assigned to the key.
objectType
additional.fields.value.string_value
The value of
objectType
from the raw log is assigned to the value.
objectType
security_result.description
If
objectType
is "LAUNCH" and
success
is not "true", the description is "application launch attempt was successful". If
objectType
is "LAUNCH_ERROR" and
success
is not "true", the description is "User launched an application with an invalid request".
opID
about.resource.attribute.labels.key
The string "opId" is assigned to the key.
opID
about.resource.attribute.labels.value
The value of
opID
from the raw log is assigned to the value.
pool
additional.fields.key
The string "pool" is assigned to the key.
pool
additional.fields.value.string_value
The value of
pool
from the raw log is assigned to the value.
pool_name
additional.fields.key
The string "pool_name" is assigned to the key.
pool_name
additional.fields.value.string_value
The value of
pool_name
from the raw log is assigned to the value.
protocol
network.ip_protocol
The value of
protocol
from the raw log is converted to uppercase and mapped to the UDM field. If the value is "PROTO", it is not mapped.
protocol
additional.fields.key
If the value of
protocol
is "PROTO", the string "ip_protocol" is assigned to the key.
protocol
additional.fields.value.string_value
If the value of
protocol
is "PROTO", the value of
protocol
from the raw log is assigned to the value.
query_data
network.dns.questions.name
The
query_data
field is parsed to extract the
question_name
, which is then mapped to the UDM field.
query_data
network.dns.questions.type
The
query_data
field is parsed to extract the
query_type
, which is then mapped to the UDM field using a lookup included from "dns_record_type.include".
query_data
network.dns.questions.class
The
query_data
field is parsed to extract the
dns_class
, which is then mapped to the UDM field using a lookup included from "dns_query_class_mapping.include".
referer
principal.url
The value of
referer
from the raw log is mapped to the UDM field.
request_content_type
additional.fields.key
The string "request_content_type" is assigned to the key.
request_content_type
additional.fields.value.string_value
The value of
request_content_type
from the raw log is assigned to the value.
request_state
additional.fields.key
The string "request_state" is assigned to the key.
request_state
additional.fields.value.string_value
The value of
request_state
from the raw log is assigned to the value.
response_code
network.http.response_code
The value of
response_code
or
server_response_code
from the raw log is mapped to the UDM field.
response_content_type
additional.fields.key
The string "response_content_type" is assigned to the key.
response_content_type
additional.fields.value.string_value
The value of
response_content_type
from the raw log is assigned to the value.
rule_id
security_result.rule_id
The value of
rule_id
from the raw log is mapped to the UDM field.
s2comp
about.resource.attribute.labels.key
The string "S2-Component" is assigned to the key.
s2comp
about.resource.attribute.labels.value
The value of
s2comp
from the raw log is assigned to the value.
server_ip
target.ip
The value of
server_ip
from the raw log is mapped to the UDM field.
server_name
target.hostname
The value of
server_name
from the raw log is mapped to the UDM field.
server_response_code
network.http.response_code
See logic for
response_code
.
server_src_port
target.port
The value of
server_src_port
from the raw log is mapped to the UDM field.
service_engine
additional.fields.key
The string "service_engine" is assigned to the key.
service_engine
additional.fields.value.string_value
The value of
service_engine
from the raw log is assigned to the value.
sourceIp
principal.ip
The value of
sourceIp
from the raw log is mapped to the UDM field.
ssl_cipher
network.tls.cipher
The value of
ssl_cipher
from the raw log is mapped to the UDM field.
ssl_session_id
network.session_id
The value of
ssl_session_id
from the raw log is mapped to the UDM field.
ssl_version
network.tls.version_protocol
The value of
ssl_version
from the raw log is mapped to the UDM field.
sub
about.resource.attribute.labels.key
The string "Sub Component" is assigned to the key.
sub
about.resource.attribute.labels.value
The value of
sub
from the raw log is assigned to the value.
subClusterUuid
additional.fields.key
The string "subClusterUuid" is assigned to the key.
subClusterUuid
additional.fields.value.string_value
The value of
subClusterUuid
from the raw log is assigned to the value.
sub_msg
Various fields within
principal
,
target
,
network
,
security_result
, and
about
The
sub_msg
field is parsed differently based on the
msg_type
.  It can be parsed as JSON, using
grok
patterns, or using key-value pairs.  The extracted fields are then mapped to various UDM fields based on their names and the parser's logic.  This includes fields like
ip_type
,
action
,
rule_id
,
direction
,
protocol
,
tcp_flag
,
src_ip
,
src_port
,
dst_ip
,
dst_port
,
data
,
msg
, and others.
subcomp
about.resource.attribute.labels.key
The string "Sub Component" is assigned to the key.
subcomp
about.resource.attribute.labels.value
The value of
subcomp
from the raw log is assigned to the value.
tenantId
principal.resource.attribute.labels.key
The string "tenantId" is assigned to the key.
tenantId
principal.resource.attribute.labels.value
The value of
tenantId
from the raw log is assigned to the value.
tenantId
additional.fields.key
The string "tenantId" is assigned to the key.
tenantId
additional.fields.value.string_value
The value of
tenantId
from the raw log is assigned to the value.
ts
metadata.event_timestamp
The value of
ts
from the raw log is parsed as a timestamp and mapped to the UDM field.
ts
timestamp
The value of
ts
from the raw log is parsed as a timestamp and mapped to the UDM field.
updateType
additional.fields.key
The string "updateType" is assigned to the key.
updateType
additional.fields.value.string_value
The value of
updateType
from the raw log is assigned to the value.
uri_path
network.http.referral_url
The value of
uri_path
from the raw log is mapped to the UDM field.
user_agent
network.http.user_agent
The value of
user_agent
from the raw log is mapped to the UDM field.
user_agent
network.http.parsed_user_agent
The value of
user_agent
from the raw log is parsed as a user agent string and mapped to the UDM field.
USER
principal.user.user_display_name
The value of
USER
from the raw log is mapped to the UDM field.
values.actorExternalId
principal.resource.attribute.labels.key
The string "actorExternalId" is assigned to the key.
values.actorExternalId
principal.resource.attribute.labels.value
The value of
values.actorExternalId
from the raw log is assigned to the value.
values.actorExternalId
additional.fields.key
The string "actorExternalId" is assigned to the key.
values.actorExternalId
additional.fields.value.string_value
The value of
values.actorExternalId
from the raw log is assigned to the value.
values.deviceType
principal.resource.attribute.labels.key
The string "deviceType" is assigned to the key.
values.deviceType
principal.resource.attribute.labels.value
The value of
values.deviceType
from the raw log is assigned to the value.
values.deviceType
additional.fields.key
The string "deviceType" is assigned to the key.
values.deviceType
additional.fields.value.string_value
The value of
values.deviceType
from the raw log is assigned to the value.
values.resourceType
principal.resource.resource_subtype
The value of
values.resourceType
from the raw log is mapped to the UDM field.  The
principal.resource.type
is set to "VIRTUAL_MACHINE".
values.success
security_result.action
If the value is "true" (case-insensitive), it's mapped to "ALLOW". If it's "false" (case-insensitive), it's mapped to "BLOCK".
virtualservice
additional.fields.key
The string "virtualservice" is assigned to the key.
virtualservice
additional.fields.value.string_value
The value of
virtualservice
from the raw log is assigned to the value.
vmw_vr_ops_appname
about.resource.attribute.labels.key
The string "Ops AppName" is assigned to the key.
vmw_vr_ops_appname
about.resource.attribute.labels.value
The value of
vmw_vr_ops_appname
from the raw log is assigned to the value.
vmw_vr_ops_clustername
about.resource.attribute.labels.key
The string "Ops ClusterName" is assigned to the key.
vmw_vr_ops_clustername
about.resource.attribute.labels.value
The value of
vmw_vr_ops_clustername
from the raw log is assigned to the value.
vmw_vr_ops_logtype
about.resource.attribute.labels.key
The string "Ops Logtype" is assigned to the key.
vmw_vr_ops_logtype
about.resource.attribute.labels.value
The value of
vmw_vr_ops_logtype
from the raw log is assigned to the value.
vmw_vr_ops_nodename
about.resource.attribute.labels.key
The string "Ops NodeName" is assigned to the key.
vmw_vr_ops_nodename
about.resource.attribute.labels.value
The value of
vmw_vr_ops_nodename
from the raw log is assigned to the value.
vs_name
additional.fields.key
The string "vs_name" is assigned to the key.
vs_name
additional.fields.value.string_value
The value of
vs_name
from the raw log is assigned to the value. The string "VMWARE" is assigned. The string "VMWARE_VREALIZE" is assigned. The string "VMWARE_VREALIZE" is assigned.
Need more help?
Get answers from Community members and Google SecOps professionals.
