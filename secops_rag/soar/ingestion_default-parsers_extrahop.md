# Collect ExtraHop RevealX logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop/  
**Scraped:** 2026-03-05T09:55:17.641286Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ExtraHop RevealX logs
Supported in:
Google secops
SIEM
This document explains how to ingest ExtraHop RevealX logs to Google Security Operations using Bindplane. The parser extracts fields from JSON and Syslog formatted logs. It uses grok patterns and conditional logic to handle different log formats, mapping extracted fields to the UDM and enriching the data with security-related information like severity and categories. The parser also handles specific ExtraHop event types like DNS Rebinding, Kerberos authentication errors, and RDP connections, applying specialized parsing logic for each.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to ExtraHop Reveal X
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
'EXTRAHOP'
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
Configure ExtraHop Syslog
Sign in to the
ExtraHop Administration
using
https://<extrahop-hostname-or-IP-address>/admin
.
Go to
Status and Diagnostics
>
Audit Log
.
Click
Configure Syslog Settings
.
Provide the following configuration details:
Destination
: Enter the Bindplane agent IP address.
Protocol
: Select
UDP
, or
TCP
, depending on your Bindplane configuration.
Port
: Enter the Bindplane agent port number.
Click
Test Settings
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
alert_name
security_result.summary
The value of
alert_name
from the raw log is mapped to
security_result.summary
.
answers[].data
network.dns.answers[].data
The value of
data
for each element in the
answers
array from the raw log is mapped to the
data
field of the corresponding element in the
network.dns.answers
array.
answers[].name
network.dns.answers[].name
The value of
name
for each element in the
answers
array from the raw log is mapped to the
name
field of the corresponding element in the
network.dns.answers
array.
answers[].ttl
network.dns.answers[].ttl
The value of
ttl
for each element in the
answers
array from the raw log is mapped to the
ttl
field of the corresponding element in the
network.dns.answers
array.
answers[].typeNum
network.dns.answers[].type
The value of
typeNum
for each element in the
answers
array from the raw log is mapped to the
type
field of the corresponding element in the
network.dns.answers
array.
client_ip
principal.ip
The value of
client_ip
from the raw log is mapped to
principal.ip
.
cn1
security_result.rule_labels[].value
The value of
cn1
from the raw log is used as the value for a
security_result.rule_labels
element with key "Detection ID".
cn2
security_result.detection_fields[].value
The value of
cn2
from the raw log is used as the value for a
security_result.detection_fields
element with key "riskscore".
cs1
security_result.rule_name
The value of
cs1
from the raw log is mapped to
security_result.rule_name
.
cs2
security_result.category_details[]
The value of
cs2
from the raw log is added as an element to the
security_result.category_details
array.
description
metadata.description
The value of
description
from the raw log, after some processing (removing newline characters and backslashes), is mapped to
metadata.description
.  In some cases, other fields from the raw log may contribute to or overwrite this field.
details
principal.resource.resource_subtype
,
security_result.summary
,
principal.ip
The
details
field is parsed. The value associated with the "facility" key is mapped to
principal.resource.resource_subtype
. The value associated with the "details" key is mapped to
security_result.summary
. The value associated with the "src_ip" key is mapped to
principal.ip
.
dst
target.ip
or
target.mac
The value of
dst
from the raw log is mapped to
target.ip
if it's an IP address, or
target.mac
if it's a MAC address.
dst_ip
target.ip
The value of
dst_ip
from the raw log is mapped to
target.ip
.
eh_event
metadata.event_type
,
network.application_protocol
If
eh_event
is "dns",
metadata.event_type
is set to
NETWORK_DNS
and
network.application_protocol
is set to
DNS
. If
eh_event
is "RDP",
metadata.event_type
is set to
NETWORK_CONNECTION
and
network.application_protocol
is set to
RDP
.
event_id
metadata.product_event_type
The value of
event_id
from the raw log is mapped to
metadata.product_event_type
.
facility
principal.resource.resource_subtype
The value of
facility
from the raw log is mapped to
principal.resource.resource_subtype
.
ipaddr
principal.ip
The value of
ipaddr
from the raw log is mapped to
principal.ip
.
jsonPayload.description
metadata.product_event_type
,
principal.hostname
,
principal.asset.hostname
,
security_result.summary
The
jsonPayload.description
field is parsed as JSON. The "operation" field is mapped to
metadata.product_event_type
. The "event" field (after removing " Audit Log") is mapped to
principal.hostname
and
principal.asset.hostname
. The "details" field is mapped to
security_result.summary
.
jsonPayload.event
metadata.product_event_type
,
principal.hostname
,
principal.asset.hostname
The value of
jsonPayload.event
from the raw log (after removing " Audit Log") is mapped to
metadata.product_event_type
,
principal.hostname
, and
principal.asset.hostname
.
jsonPayload.id
metadata.product_log_id
The value of
jsonPayload.id
from the raw log is mapped to
metadata.product_log_id
.
macaddr
principal.mac
The value of
macaddr
from the raw log is mapped to
principal.mac
.
name
metadata.description
The value of
name
from the raw log is mapped to
metadata.description
.
object_id
target.resource.product_object_id
The value of
object_id
from the raw log is mapped to
target.resource.product_object_id
.
object_name
target.resource.name
The value of
object_name
from the raw log is mapped to
target.resource.name
.
object_type
target.resource.resource_type
The value of
object_type
from the raw log (converted to uppercase) is mapped to
target.resource.resource_type
.
operation
metadata.product_event_type
The value of
operation
from the raw log is mapped to
metadata.product_event_type
.
priority
security_result.severity
,
security_result.severity_details
If
priority
is "notice",
security_result.severity
is set to
MEDIUM
and
security_result.severity_details
is set to the value of
priority
.
product_event_type
metadata.product_event_type
The value of
product_event_type
from the raw log is mapped to
metadata.product_event_type
. It is also used to determine the
metadata.event_type
and other fields based on its value.
qname
network.dns.questions[].name
The value of
qname
from the raw log is mapped to the
name
field of a
network.dns.questions
element.
qname_or_host
intermediary.hostname
The value of
qname_or_host
from the raw log is mapped to
intermediary.hostname
.
qtype
network.dns.questions[].type
The value of
qtype
from the raw log is mapped to the
type
field of a
network.dns.questions
element, converting the string representation to its numeric equivalent according to DNS record types.
resource.labels.project_id
target.resource.attribute.labels[].value
The value of
resource.labels.project_id
from the raw log is used as the value for a
target.resource.attribute.labels
element with key "Project id".
resource.type
target.resource.resource_subtype
The value of
resource.type
from the raw log is mapped to
target.resource.resource_subtype
.
rdp_record.clientBuild
metadata.product_version
The value of
rdp_record.clientBuild
from the raw log is mapped to
metadata.product_version
.
rdp_record.clientBytes
network.sent_bytes
The value of
rdp_record.clientBytes
from the raw log is mapped to
network.sent_bytes
.
rdp_record.clientName
principal.hostname
The value of
rdp_record.clientName
from the raw log is mapped to
principal.hostname
.
rdp_record.clientPort
principal.port
The value of
rdp_record.clientPort
from the raw log is mapped to
principal.port
.
rdp_record.cookie
principal.user.userid
The value of
rdp_record.cookie
(after removing "mstshash=") from the raw log is mapped to
principal.user.userid
.
rdp_record.proto
network.ip_protocol
The value of
rdp_record.proto
from the raw log is mapped to
network.ip_protocol
, converting "TCP" to "TCP" and "UDP" to "UDP".
rdp_record.selectedProtocol
security_result.description
The value of
rdp_record.selectedProtocol
from the raw log is mapped to
security_result.description
.
rdp_record.serverBytes
network.received_bytes
The value of
rdp_record.serverBytes
from the raw log is mapped to
network.received_bytes
.
rdp_record.serverPort
target.port
The value of
rdp_record.serverPort
from the raw log is mapped to
target.port
.
rt
metadata.event_timestamp
The value of
rt
from the raw log is parsed as a timestamp and mapped to
metadata.event_timestamp
.
severity
security_result.severity
,
security_result.severity_details
,
event.idm.is_alert
,
event.idm.is_significant
The value of
severity
is mapped to
security_result.severity_details
. It is also used to determine the value of
security_result.severity
,
event.idm.is_alert
, and
event.idm.is_significant
.
src
principal.ip
or
principal.mac
The value of
src
from the raw log is mapped to
principal.ip
if it's an IP address, or
principal.mac
if it's a MAC address.
src_ip
principal.ip
or
principal.mac
The value of
src_ip
from the raw log is mapped to
principal.ip
if it's an IP address, or
principal.mac
if it's a MAC address.
summary
security_result.summary
The value of
summary
from the raw log is mapped to
security_result.summary
.
ts
metadata.event_timestamp
The value of
ts
from the raw log is parsed as a timestamp and mapped to
metadata.event_timestamp
.
user
principal.user.userid
The value of
user
from the raw log is mapped to
principal.user.userid
.
(N/A)
metadata.log_type
Always set to "EXTRAHOP".
(N/A)
metadata.vendor_name
Always set to "EXTRAHOP".
(N/A)
metadata.product_name
Always set to "EXTRAHOP".
(N/A)
security_result.severity
Set to
CRITICAL
by default, or based on the value of
severity
or
priority
.
(N/A)
event.idm.is_alert
Set to
true
if
security_result.severity
is "HIGH" or "CRITICAL".
(N/A)
event.idm.is_significant
Set to
true
if
security_result.severity
is "HIGH" or "CRITICAL".
(N/A)
metadata.event_type
Determined based on the values of other fields, such as
eh_event
,
product_event_type
,
has_principal
, and
dst
. Defaults to
GENERIC_EVENT
.
(N/A)
network.application_protocol
Set to
DNS
if
eh_event
is "dns" or
message
contains "DNS Rebinding". Set to
RDP
if
eh_event
is "RDP".
(N/A)
security_result.rule_labels[].key
Set to "Detection ID" for the rule label derived from
cn1
.
(N/A)
security_result.detection_fields[].key
Set to "riskscore" for the detection field derived from
cn2
.
(N/A)
principal.user.attribute.roles[].type
Set to
SERVICE_ACCOUNT
if
user_name
is present.
(N/A)
extensions.auth.type
Set to
SSO
if
product_event_type
is "Kerberos Client Auth Errors".
(N/A)
extensions.auth.mechanism
Set to
USERNAME_PASSWORD
if
product_event_type
is "Unsafe LDAP Authentication" or "Kerberos Client Auth Errors".
(N/A)
security_result.category
Set to
NETWORK_SUSPICIOUS
if
product_event_type
is "DNS Internal Reverse Lookup Scan" or contains "Inbound Suspicious Connections". Set to
NETWORK_MALICIOUS
if
product_event_type
is "Request to External Database Server".
(N/A)
network.http.response_code
Set based on the
status_code
extracted from
product_event_type
if it matches the pattern "HTTP Server %{INT:status_code} %{GREEDYDATA}".
jsonPayload.cs1
security_result.detection_fields[].value
The value of
jsonPayload.cs1
from the raw log is used as the value for a
security_result.detection_fields
element.
jsonPayload.cn1
security_result.detection_fields[].value
The value of
jsonPayload.cn1
from the raw log is used as the value for a
security_result.detection_fields
element.
jsonPayload.cn2
security_result.detection_fields[].value
The value of
jsonPayload.cn2
from the raw log is used as the value for a
security_result.detection_fields
element.
jsonPayload.cs1Label
,
jsonPayload.cn1Label
,
jsonPayload.cn2Label
security_result.detection_fields[].key
These fields from the raw log are used as keys for corresponding elements in
security_result.detection_fields
.
jsonPayload.src
principal.ip
The value of
jsonPayload.src
from the raw log is mapped to
principal.ip
.
jsonPayload.dst
target.ip
The value of
jsonPayload.dst
from the raw log is mapped to
target.ip
.
Need more help?
Get answers from Community members and Google SecOps professionals.
