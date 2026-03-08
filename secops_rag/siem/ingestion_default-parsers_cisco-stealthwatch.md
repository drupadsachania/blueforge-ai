# Collect Cisco Stealthwatch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stealthwatch/  
**Scraped:** 2026-03-05T09:21:44.791684Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Stealthwatch logs
Supported in:
Google secops
SIEM
This document explains how to collect Cisco Secure Network Analytics (formerly Stealthwatch) logs to Google Security Operations using Bindplane. The parser handles two formats of Cisco Stealthwatch logs: one with client/server IP and packet information, and another with device ID and byte counts. It extracts fields, converts them to the appropriate data types, maps them to the UDM, and sets metadata fields like vendor, product, and event type based on log content and format.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Cisco Stealthwatch.
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
CISCO_STEALTHWATCH
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
Configure Cisco Secure Network Analytics (formerly Stealthwatch) Syslog
Sign in to the
Management Console
Web UI.
Go to
Configuration
>
Response Management
.
Edit Syslog Format:
Name
: enter a name for the syslog format.
Description
: provide a description for the format.
Facility
: set to
Local 0
Severity
: set to
Informational
.
In the
Message
field, paste the following format:
Lancope|StealthWatch|time|{time}|target_hostname|{target_hostname}|alarm_severity_id|{alarm_severity_id}|alarm_type_id|{alarm_type_id}|alarm_type_description|{alarm_type_description}|port|{port}|target_ip|{target_ip}|target_mac_address|{target_mac_address}|target_label|{target_label}|alarm_type_name|{alarm_type_name}|source_hostname|{source_hostname}|source_ip|{source_ip}|source_mac_address|{source_mac_address}|source_username|{source_username}|device_ip|{device_ip}|device_name|{device_name}|details|{details}|protocol|{protocol}|alarm_id|{alarm_id}|alarm_category_name|{alarm_category_name}|start_active_time|{start_active_time}| end_active_time|{end_active_time}
Click
OK
.
Go to
Response Management
>
Actions
>
Add Syslog Message
.
Configure Syslog Forwarder:
Name
: enter the name for the Google SecOps Bindplane forwarder.
Description
: enter the description for the Google SecOps Bindplane forwarder.
IP Address
: enter the Bindplane agent IP address.
Port
: enter the Bindplane agent port number; for example,
514
.
Format
: select the format created in Step 3.
Click
OK
.
Configure Rule Names for Cisco Secure Network Analytics (formerly Stealthwatch)
Go to
Configuration
>
Response Management
.
Select
Rules
>
Add
>
SMC system alarms
.
Click
OK
.
In the
Rule types
dialog, select a rule.
Click
OK
.
In the
Rule
dialog, do the following:
Name
: enter a name for the rule.
This rule is triggered if
: select
Any
,
Severity
, and
Informational
in the respective lists.
Click
OK
.
Select
Actions
>
Add
.
Select the action you have created previously.
Click
Ok
, and then
Ok
.
Repeat the previous steps to rename the following three options under the
Rule
section:
Supported log collection mechanism - Syslog
Preferred log collection mechanism - Syslog
Event flow logical diagram - SMC Remote Syslog Server
UDM Mapping Table
Log Field
UDM Mapping
Logic
Alarm_ID
additional.fields[?key=='Alarm_ID'].value.string_value
The value of
Alarm_ID
from the raw log is placed within a nested
additional.fields
structure under the key
Alarm_ID
.
ClientBytes
network.sent_bytes
ClientBytes
from the raw log is converted to an unsigned integer and mapped.
ClientIP
principal.ip
ClientIP
from the raw log is mapped.
ClientPort
principal.port
ClientPort
from the raw log is converted to an integer and mapped.
CPayload
Not Mapped
This field is not used in the final UDM.
DestIPv4Address
target.ip
DestIPv4Address
from the raw log is mapped.
DestPort
target.port
DestPort
from the raw log is converted to an integer and mapped.
details
security_result.summary
The value of
details
from the raw log, with double quotes removed, is mapped.
FC
intermediary.ip
FC
from the raw log is mapped.
host.country
principal.location.country_or_region
host.country
from the raw log is mapped.
host.hostGroupNames
about.group.group_display_name
Each element in the
host.hostGroupNames
array from the raw log is prepended with
host:
and mapped as a separate
about
object.
host.ipAddress
principal.ip
host.ipAddress
from the raw log is mapped.
hostBytes
network.sent_bytes
hostBytes
from the raw log is converted to an unsigned integer and mapped.
InPackets
additional.fields[?key=='InPackets'].value.string_value
The value of
InPackets
from the raw log is placed within a nested
additional.fields
structure under the key
InPackets
.
inputSNMPIface
additional.fields[?key=='inputSNMPIface'].value.string_value
The value of
inputSNMPIface
from the raw log is placed within a nested
additional.fields
structure under the key
inputSNMPIface
.
LastTime
Not Mapped
This field is parsed for the event timestamp in some cases, but not directly mapped to the UDM.
MessageSourceAddress
principal.ip
MessageSourceAddress
from the raw log is mapped.
method
network.http.method
method
from the raw log is mapped.
outputSNMPIface
additional.fields[?key=='outputSNMPIface'].value.string_value
The value of
outputSNMPIface
from the raw log is placed within a nested
additional.fields
structure under the key
outputSNMPIface
.
PAAppID
Not Mapped
This field is not used in the final UDM.
peer.country
target.location.country_or_region
peer.country
from the raw log is mapped.
peer.hostGroupNames
about.group.group_display_name
Each element in the
peer.hostGroupNames
array from the raw log is prepended with
peer:
and mapped as a separate
about
object.
peer.ipAddress
target.ip
peer.ipAddress
from the raw log is mapped.
peerBytes
network.received_bytes
peerBytes
from the raw log is converted to an unsigned integer and mapped.
peerPackets
Not Mapped
This field is not used in the final UDM.
Protocol
Not Mapped
This field is parsed to determine the
network.ip_protocol
, but not directly mapped.
ProtocolIdentifier
Not Mapped
This field is used to derive
network.ip_protocol
, but not directly mapped.
reportName
metadata.product_event_type
reportName
from the raw log is mapped.
ServerBytes
network.received_bytes
ServerBytes
from the raw log is converted to an unsigned integer and mapped.
ServerIP
target.ip
ServerIP
from the raw log is mapped.
ServerPort
target.port
ServerPort
from the raw log is converted to an integer and mapped.
Service
Not Mapped
This field is not used in the final UDM.
sid
target.user.windows_sid
sid
from the raw log is mapped.
SourceModuleName
target.resource.name
SourceModuleName
from the raw log is mapped.
SourceModuleType
observer.application
SourceModuleType
from the raw log is mapped.
SourcePort
principal.port
SourcePort
from the raw log is converted to an integer and mapped.
sourceIPv4Address
principal.ip
sourceIPv4Address
from the raw log is mapped.
SPayload
Not Mapped
This field is not used in the final UDM.
src_ip
principal.ip
src_ip
from the raw log is mapped.
StartTime
Not Mapped
This field is parsed for the event timestamp in some cases, but not directly mapped to the UDM.
time
Not Mapped
This field is parsed for the event timestamp in some cases, but not directly mapped to the UDM.
timestamp
Not Mapped
This field is parsed for the event timestamp, but not directly mapped to the UDM.
UserName
principal.user.user_display_name
UserName
from the raw log is mapped.
Version
metadata.product_version
Version
from the raw log is converted to a string and mapped.
N/A
metadata.event_timestamp
The event timestamp is derived from various fields (
LastTime
,
time
,
timestamp
,
StartTime
) depending on the log format, or from the
create_time
field if no other timestamp is available.
N/A
metadata.log_type
Always set to
CISCO_STEALTHWATCH
.
N/A
metadata.vendor_name
Always set to
Cisco
.
N/A
metadata.event_type
Determined by parser logic based on log content. Can be
NETWORK_CONNECTION
,
USER_STATS
,
USER_UNCATEGORIZED
,
FILE_OPEN
,
FILE_DELETION
, or
FILE_UNCATEGORIZED
.
N/A
network.ip_protocol
Determined by parser logic based on the
Protocol
or
ProtocolIdentifier
fields. Can be
TCP
,
UDP
, or
ICMP
.
action
security_result.action_details
The value of
action
from the raw log is mapped.
action
security_result.action
Derived from the
action
field. If
action
is
SUCCESS
, this field is set to
ALLOW
; otherwise, it's set to
BLOCK
.
category
security_result.category_details
The value of
category
from the raw log is mapped.
description
security_result.description
If both
description
and
file_type
are present in the raw log, they are concatenated and mapped.
desc
metadata.description
The value of
desc
from the raw log, with double quotes removed, is mapped.
failuer_reason
security_result.summary
If both
failuer_reason
and
file_type
are present in the raw log, they are concatenated and mapped.
file_path
target.file.full_path
file_path
from the raw log is mapped.
file_type
target.file.mime_type
file_type
from the raw log is mapped.
hostname
principal.hostname
hostname
from the raw log is mapped.
ip
principal.ip
ip
from the raw log is mapped.
ipf
intermediary.ip
ipf
from the raw log is mapped.
ipt
target.ip
ipt
from the raw log is mapped.
process_id
target.process.pid
process_id
from the raw log is mapped.
protocol
network.application_protocol
protocol
from the raw log is mapped.
security_res.severity
security_result.severity
If
severity
is
Minor
, this field is set to
INFORMATIONAL
; if
severity
is
Major
, it's set to
ERROR
.
session_id
network.session_id
session_id
from the raw log is mapped.
severity
Not Mapped
This field is used to derive
security_result.severity
, but not directly mapped.
Source_HG
principal.location.country_or_region
Source_HG
from the raw log is mapped.
Source_HostSnapshot
principal.url
Source_HostSnapshot
from the raw log is mapped.
Target_HostSnapshot
target.url
Target_HostSnapshot
from the raw log is mapped.
user_name
principal.user.userid
user_name
from the raw log is mapped.
Need more help?
Get answers from Community members and Google SecOps professionals.
