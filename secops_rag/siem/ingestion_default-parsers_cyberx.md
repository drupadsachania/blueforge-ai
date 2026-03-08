# Collect Microsoft Defender for IoT (CyberX) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberx/  
**Scraped:** 2026-03-05T09:22:57.564497Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Defender for IoT (CyberX) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Microsoft Defender for IoT (CyberX) logs to Google Security Operations using Bindplane.
Microsoft Defender for IoT (formerly CyberX) is an agentless IoT/OT security platform that provides asset discovery, vulnerability management, and continuous threat monitoring for industrial control systems (ICS) and operational technology (OT) environments. It detects anomalous behavior and known threats across IoT/OT networks without impacting operational processes. The parser extracts fields from CyberX syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Microsoft Defender for IoT sensor console
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
udplog
:
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'CYBERX'
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
Configuration parameters
Replace the following placeholders:
Receiver configuration:
udplog
: Use
udplog
for UDP syslog or
tcplog
for TCP syslog
0.0.0.0
: IP address to listen on (
0.0.0.0
to listen on all interfaces)
514
: Port number to listen on (standard syslog port)
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
YOUR_CUSTOMER_ID
: Customer ID from the Get customer ID section
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
: Log type exactly as it appears in Chronicle (
CYBERX
)
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
To restart the Bindplane agent in Windows, choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Syslog forwarding on Microsoft Defender for IoT (CyberX)
Sign in to the
Microsoft Defender for IoT
sensor console (formerly CyberX).
Go to
System Settings
>
Forwarding
.
Click
Add
(or
+
) to create a new forwarding rule.
Provide the following configuration details:
Rule Name
: Enter a descriptive name (for example,
Google-SecOps-Bindplane
).
Severity
: Select
All
(or select specific severity levels: Minor, Major, Critical).
Protocol
: Select
All
(or select specific protocols to monitor).
Engine
: Select
All
(or select specific detection engines).
Action
: Select
Send Syslog
.
In the
Syslog Server
configuration:
Host
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Protocol
: Select
UDP
.
Format
: Select
CEF
(Common Event Format).
Timezone
: Select
UTC
(recommended).
Click
Save
.
Enable the forwarding rule by toggling the rule to
Active
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
Access Mask
security_result.detection_fields.value
Value of access_mask from parsed access_request_kvdata
Account Domain
principal.administrative_domain
Value of principal_domain from parsed principal_kvdata
Account Domain
target.administrative_domain
Value of target_domain from parsed target_kvdata
Account Name
principal.user.userid
Value of principal_account_name from parsed principal_kvdata
Account Name
target.user.userid
Value of target_account_name from parsed target_kvdata
action
security_result.action_details
Value of action
action
security_result.action
Derived. If action is "accept", "passthrough", "pass", "permit", "detected", or "close", map to "ALLOW". If action is "deny", "dropped", or "blocked", map to "BLOCK". If action is "timeout", map to "FAIL". Otherwise, map to "UNKNOWN_ACTION".
Algorithm Name
security_result.detection_fields.value
Value of algorithm_name from parsed cryptographic_kvdata
app
target.application
Value of service if app_protocol_output is empty
appcat
security_result.detection_fields.value
Value of appcat
Application Name
principal.application
Value of application_name
Authentication Package
security_result.about.resource.name
Value of authentication_package
Azure Defender for IoT Alert
security_result.detection_fields.value
Value of azure_defender_for_iot_alert
channel
security_result.detection_fields.value
Value of channel
Client Address
principal.ip, principal.asset.ip
Value of source_ip
Client Port
principal.port
Value of source_port
craction
security_result.detection_fields.value
Value of craction
Credential Manager credentials were backupped
security_result.description
Value of description
Credential Manager credentials were read.
security_result.description
Value of description
crscore
security_result.severity_details
Value of crscore
crlevel
security_result.severity, security_result.severity_details
Value of crlevel. If crlevel is "HIGH", "MEDIUM", "LOW", or "CRITICAL", map to the corresponding UDM severity.
Cryptographic Operation
metadata.description
Value of product_desc
CyberX platform name
security_result.detection_fields.value
Value of cyberx_platform_name
Description
security_result.description
Value of description if Message is empty
Destination
target.ip, target.asset.ip or target.hostname
If Destination is an IP address, map to target.ip and target.asset.ip. Otherwise, map to target.hostname.
Destination Address
target.ip, target.asset.ip
Value of destination_ip from parsed network_information
Destination DRA
target.resource.name
Value of destination_dra
Destination ip
target.ip, target.asset.ip
Value of destination_ip
Destination Port
target.port
Value of destination_port from parsed network_information
devid
principal.resource.product_object_id
Value of devid
devname
principal.resource.name
Value of devname
Direction
network.direction
If Direction is "incoming", "inbound", or "response", map to "INBOUND". If Direction is "outgoing", "outbound", or "request", map to "OUTBOUND".
dstip
target.ip, target.asset.ip
Value of dstip if destination_ip is empty
dstcountry
target.location.country_or_region
Value of dstcountry
dstintf
security_result.detection_fields.value
Value of dstintf
dstintfrole
security_result.detection_fields.value
Value of dstintfrole
dstosname
target.platform
Value of dstosname if it is "WINDOWS", "LINUX", or "MAC".
dstport
target.port
Value of dstport if destination_port is empty
dstswversion
target.platform_version
Value of dstswversion
duration
network.session_duration.seconds
Value of duration
event_id
security_result.rule_name
Used to construct rule name as "EventID: %{event_id}"
event_in_sequence
security_result.detection_fields.value
Value of event_in_sequence
Filter Run-Time ID
security_result.detection_fields.value
Value of filter_run_time_id from parsed filter_information
Group Membership
security_result.detection_fields.value
Value of group_membership if event_id is not 4627
Group Membership
target.user.group_identifiers
Values from parsed group_membership if event_id is 4627
handle_id
security_result.detection_fields.value
Value of handle_id from parsed object_kvdata
Handle ID
security_result.detection_fields.value
Value of handle_id from parsed object_kvdata
impersonation_level
security_result.detection_fields.value
Value of impersonation_level from parsed logon_information_kvdata
Key Length
security_result.detection_fields.value
Value of key_length from parsed auth_kvdata
Key Name
security_result.detection_fields.value
Value of key_name from parsed cryptographic_kvdata
Key Type
security_result.detection_fields.value
Value of key_type from parsed cryptographic_kvdata
keywords
security_result.detection_fields.value
Value of keywords
Layer Name
security_result.detection_fields.value
Value of layer_name from parsed filter_information
Layer Run-Time ID
security_result.detection_fields.value
Value of layer_run_time_id from parsed filter_information
logid
metadata.product_log_id
Value of logid
Logon GUID
principal.resource.product_object_id
Value of logon_guid
Logon ID
security_result.detection_fields.value
Value of logon_id
logon_type
event.idm.read_only_udm.extensions.auth.mechanism
Derived. If logon_type is '3', map to "NETWORK". If '4', map to "BATCH". If '5', map to "SERVICE". If '8', map to "NETWORK_CLEAR_TEXT". If '9', map to "NEW_CREDENTIALS". If '10', map to "REMOTE_INTERACTIVE". If '11', map to "CACHED_INTERACTIVE". Otherwise, if not empty, map to "MECHANISM_OTHER".
Logon Account
security_result.detection_fields.value
Value of logon_id from grok parse
Logon Process
security_result.detection_fields.value
Value of logon_process from parsed auth_kvdata
Mandatory Label
security_result.detection_fields.value
Value of mandatory_label
mastersrcmac
principal.mac
Value of mastersrcmac
Message
security_result.description
Value of Message
new_process_id
target.process.pid
Value of new_process_id from parsed process_kvdata
new_process_name
target.process.file.full_path
Value of new_process_name from parsed process_kvdata
Object Name
security_result.detection_fields.value
Value of object_name from parsed object_kvdata
Object Server
security_result.detection_fields.value
Value of object_server from parsed object_kvdata
Object Type
security_result.detection_fields.value
Value of object_type from parsed object_kvdata
osname
principal.platform
Value of osname if it is "WINDOWS", "LINUX", or "MAC".
Package Name (NTLM only)
security_result.detection_fields.value
Value of package_name from parsed auth_kvdata
policyid
security_result.rule_id
Value of policyid
policyname
security_result.rule_name
Value of policyname
policytype
security_result.rule_type
Value of policytype
Process ID
principal.process.pid
Value of process_id
Process Name
principal.process.file.full_path
Value of creator_process_name from parsed process_kvdata
profile_changed
security_result.detection_fields.value
Value of profile_changed
Profile Changed
security_result.detection_fields.value
Value of profile_changed from grok parse
proto
network.ip_protocol
If proto is "17", map to "UDP". If "6" or subtype is "wad", map to "TCP". If "41", map to "IP6IN4". If service is "PING" or proto is "1" or service contains "ICMP", map to "ICMP".
Protocol
network.application_protocol
Value of app_protocol_output derived from Protocol
Provider Name
security_result.detection_fields.value
Value of provider_name from parsed provider_kvdata or cryptographic_kvdata
rcvdbyte
network.received_bytes
Value of rcvdbyte
rcvdpkt
security_result.detection_fields.value
Value of rcvdpkt
restricted_admin_mode
security_result.detection_fields.value
Value of restricted_admin_mode from parsed logon_information_kvdata
Return Code
security_result.detection_fields.value
Value of return_code from parsed cryptographic_kvdata
response
security_result.detection_fields.value
Value of response
rule_id
security_result.rule_id
Value of rule_id
Security ID
principal.user.windows_sid
Value of principal_security_id from parsed principal_kvdata
Security ID
target.user.windows_sid
Value of target_security_id from parsed target_kvdata
sentbyte
network.sent_bytes
Value of sentbyte
sentpkt
security_result.detection_fields.value
Value of sentpkt
service
network.application_protocol or target.application
Value of app_protocol_output derived from service. If app_protocol_output is empty, map to target.application.
Service ID
security_result.detection_fields.value
Value of service_id from parsed service_kvdata
Service Name
security_result.detection_fields.value
Value of service_name from parsed service_kvdata
sessionid
network.session_id
Value of sessionid
Severity
security_result.severity, security_result.severity_details
If Severity is "ERROR" or "CRITICAL", map to the corresponding UDM severity. If "INFO", map to "INFORMATIONAL". If "MINOR", map to "LOW". If "WARNING", map to "MEDIUM". If "MAJOR", map to "HIGH". Also map the raw value to severity_details.
severity
security_result.severity, security_result.severity_details
If severity is "1", "2", or "3", map to "LOW". If "4", "5", or "6", map to "MEDIUM". If "7", "8", or "9", map to "HIGH". Also map the raw value to severity_details.
Share Name
security_result.detection_fields.value
Value of share_name from parsed share_information_kvdata
Share Path
security_result.detection_fields.value
Value of share_path from parsed share_information_kvdata
Source
principal.ip, principal.asset.ip or principal.hostname, principal.asset.hostname
If Source is an IP address, map to principal.ip and principal.asset.ip. Otherwise, map to principal.hostname and principal.asset.hostname.
Source Address
principal.ip, principal.asset.ip
Value of source_ip from parsed network_information
Source DRA
principal.resource.name
Value of source_dra
Source ip
principal.ip
Value of source_ip
Source Network Address
principal.ip, principal.asset.ip
Value of source_ip
Source Port
principal.port
Value of source_port from parsed network_information
Source Workstation
workstation_name
Value of source_workstation_name
srcip
source_ip
Value of srcip if source_ip is empty
srccountry
principal.location.country_or_region
Value of srccountry
srcmac
principal.mac
Value of srcmac
srcname
principal.hostname, principal.asset.hostname
Value of srcname
srcport
source_port
Value of srcport if source_port is empty
srcswversion
principal.platform_version
Value of srcswversion
Status Code
network.http.response_code
Value of status_code
Token Elevation Type
security_result.detection_fields.value
Value of token_elevation_type
transited_services
security_result.detection_fields.value
Value of transited_services from parsed auth_kvdata
transip
principal.nat_ip
Value of transip
transport
principal.nat_port
Value of transport
type
metadata.product_event_type
Used with subtype to create metadata.product_event_type
Type
security_result.detection_fields.value
Value of Type
UUID
metadata.product_log_id
Value of UUID
vd
principal.administrative_domain
Value of vd
virtual_account
security_result.detection_fields.value
Value of virtual_account from parsed logon_information_kvdata
Workstation Name
principal.hostname, principal.asset.hostname
Value of workstation_name if no other principal identifier is present
metadata.event_type
metadata.event_type
Derived. If both principal_present and target_present are true, map to "NETWORK_CONNECTION". If user_present is true, map to "USER_RESOURCE_ACCESS". If principal_present is true, map to "STATUS_UPDATE". Otherwise, map to "GENERIC_EVENT".
metadata.log_type
metadata.log_type
Hardcoded to "CYBERX"
metadata.product_name
metadata.product_name
Hardcoded to "CYBERX"
metadata.vendor_name
metadata.vendor_name
Hardcoded to "CYBERX"
metadata.event_timestamp
metadata.event_timestamp
Copied from the top-level timestamp field, or derived from eventtime or date and time fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
