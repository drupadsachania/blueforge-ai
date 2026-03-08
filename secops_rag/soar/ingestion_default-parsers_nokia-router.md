# Collect Nokia Router logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nokia-router/  
**Scraped:** 2026-03-05T09:58:41.157437Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Nokia Router logs
Supported in:
Google secops
SIEM
This document explains how to collect Nokia Router logs to Google Security Operations using a Bindplane agent. The parser first extracts fields like timestamps, IP addresses, hostnames, and event details using Grok patterns. It then maps these extracted fields to the corresponding fields in the Google SecOps UDM schema, performing data transformations and enriching the data with additional context based on specific event types and conditions.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the Nokia Router.
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
For additional installation options, consult this
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
creds
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
ingestion_labels
:
log_type
:
NOKIA_ROUTER
raw_log_field
:
body
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
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on Nokia Service Router
Enter Configuration Mode:
config#
log
Define a Syslog Destination:
config>log#
syslog
1
Configure Syslog Parameters:
config>log>syslog#
address
<syslog-server-ip>
config>log>syslog#
port
<port-number>
config>log>syslog#
facility
local0
config>log>syslog#
level
info
config>log>syslog#
log-prefix
"Nokia-SR"
config>log>syslog#
description
"Google SecOps syslog server"
Replace
<syslog-server-ip>
with the IP address of the Bindplane Agent and
<port-number>
with the appropriate port (for example,
514
for UDP).
Apply the Syslog Destination to a Log File:
config>log#
log-id
1
config>log>log-id#
to
syslog
1
Enable the Log File:
config>log>log-id#
no
shutdown
Save the configuration:
config>log>log-id#
exit
config>log#
save
Example full configuration:
```
bash
config
#
log
config>log
#
syslog
1
config>log>syslog
#
address
192.168.1.100
config>log>syslog
#
port
514
config>log>syslog
#
facility
local0
config>log>syslog
#
level
info
config>log>syslog
#
log
-
prefix
"Nokia-SR"
config>log>syslog
#
description
"Google SecOps syslog server"
config>log>syslog
#
exit
config>log
#
log
-
id
1
config>log>log
-
id
#
to
syslog
1
config>log>log
-
id
#
no
shutdown
config>log>log
-
id
#
exit
config>log
#
save
```
UDM Mapping Table
Log Field
UDM Mapping
Logic
%{SYSLOGTIMESTAMP:date_time}
metadata.event_timestamp
Extracted from the raw log and converted to a timestamp.
%{IP:src_ip}
principal.ip
Extracted from the raw log.
%{HOSTNAME:host_name}
principal.hostname
Extracted from the raw log.
%{INT:sequence_id}
metadata.product_log_id
Extracted from the raw log.
%{DATA:router_name}
metadata.product_name
Extracted from the raw log.
%{DATA:application}
target.application
Extracted from the raw log.
%{WORD:severity}
security_result.severity
Mapped from the raw log severity based on the following logic:
- CLEARED, INFO -> INFORMATIONAL
- MINOR -> ERROR
- WARNING -> LOW
- MAJOR -> HIGH
- CRITICAL -> CRITICAL
%{DATA:event_name}
metadata.product_event_type
Extracted from the raw log.
%{INT:event_id}
additional.fields.value.string_value
Extracted from the raw log and placed within the
additional fields
with the key
Event Id
.
%{GREEDYDATA:message1}
Used for extracting various fields based on the
event_name
. See logic for specific fields below.
Group %{NOTSPACE:group_id}
target.group.product_object_id
Extracted from
message1
when
event_name
is related to BGP events.
%{WORD} %{IP:dest_ip}
target.ip
Extracted from
message1
when
event_name
is related to BGP events.
%{GREEDYDATA:desc}
security_result.description
Extracted from
message1
for various
event_name
scenarios.
SAP %{DATA:sap_id}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
sapStatusChanged
and placed within the
additional fields
with the key
SAP Id
.
in service %{INT:service_id}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
sapStatusChanged
and placed within the
additional fields
with the key
Service Id
.
\\(customer %{INT:customer_id}\\)
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
sapStatusChanged
and placed within the
additional fields
with the key
Customer Id
.
admin=%{WORD:admin_status}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
sapStatusChanged
and placed within the
additional fields
with the key
Admin Status
.
oper=%{WORD:operation_status}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
sapStatusChanged
and placed within the
additional fields
with the key
Operation Status
.
flags=%{WORD:flag}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
sapStatusChanged
and placed within the
additional fields
with the key
Flag
.
with MI:SCI %{DATA:mi_sci}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
tmnxMkaSessionEstablished
and placed within the
additional fields
with the key
MI:SCI
.
on port %{DATA:port_id}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
tmnxMkaSessionEstablished
and placed within the
additional fields
with the key
Port Id
.
sub-port %{INT:sub_port_id}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
tmnxMkaSessionEstablished
and placed within the
additional fields
with the key
Sub-port Id
.
CA %{INT:ca}
additional.fields.value.string_value
Extracted from
message1
when
event_name
is
tmnxMkaSessionEstablished
and placed within the
additional fields
with the key
CA
.
EAPOL-destination %{MAC:dest_mac}
target.mac
Extracted from
message1
when
event_name
is
tmnxMkaSessionEstablished
.
local port-id %{DATA:local_port_id}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
local_port_id
.
dest-mac-type %{NOTSPACE:mac_type}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
mac_type
.
remote system name %{HOSTNAME:dest_host}
target.hostname
Extracted from
message1
for specific
event_name
values.
remote chassis-id %{DATA:dest_mac}
target.mac
Extracted from
message1
for specific
event_name
values.
remote port-id %{DATA:port_id}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
port_id
.
remote-index %{INT:remote_index}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
remote_index
.
remote management address %{IP:dest_ip}
target.ip
Extracted from
message1
for specific
event_name
values.
advRtr:%{HOSTNAME:dest_host}%{GREEDYDATA}, ip@:%{IP:dest_ip}/%{INT:dest_port}
target.hostname
,
target.ip
,
target.port
Extracted from
message1
for specific
event_name
values.
SID:%{INT:sid}
network.session_id
Extracted from
message1
for specific
event_name
values.
level:%{DATA:level}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
level
.
mtid:%{INT:mtid}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
mtid
.
type:%{WORD:type}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
type
.
flags:%{WORD:flag}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
flag
.
, algo:%{INT:algo}
target.resource.attribute.labels.value
Extracted from
message1
for specific
event_name
values and placed within the
target.resource.attribute.labels
with the key
algo
.
Description:%{GREEDYDATA:desc}.
security_result.description
Extracted from
message1
when
event_name
is
mafEntryMatch
.
SrcIP
principal.ip
Extracted from the
kv_data
field when
event_name
is
mafEntryMatch
.
SrcIP: %{INT:src_port}
principal.port
Extracted from the
kv_data
field when
event_name
is
mafEntryMatch
.
DstIP
target.ip
Extracted from the
kv_data
field when
event_name
is
mafEntryMatch
.
DstIP: %{INT:dest_port}
target.port
Extracted from the
kv_data
field when
event_name
is
mafEntryMatch
.
Protocol
network.ip_protocol
Extracted from the
kv_data
field when
event_name
is
mafEntryMatch
.
N/A
metadata.vendor_name
Set to
NOKIA_ROUTER
.
N/A
metadata.event_type
Determined based on the presence and combination of extracted fields:
-
src_ip
,
dest_ip
, and
network
present -> NETWORK_CONNECTION
-
principal
present -> STATUS_UPDATE
- Otherwise -> GENERIC_EVENT
%{GREEDYDATA:description}
metadata.description
Extracted from
message1
when
event_name
is
tmnxMkaSessionEstablished
.
Need more help?
Get answers from Community members and Google SecOps professionals.
