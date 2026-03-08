# Collect Cisco Meraki logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-meraki/  
**Scraped:** 2026-03-05T09:52:29.410202Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Meraki logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Meraki logs to Google Security Operations using Bindplane.
The parser extracts fields from Cisco Meraki syslog and JSON formatted logs. It uses grok and/or JSON parsing to process the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco Meraki Dashboard
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
'CISCO_MERAKI'
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
CISCO_MERAKI
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
Configure Syslog forwarding on Cisco Meraki
Sign in to the
Cisco Meraki Dashboard
at
https://dashboard.meraki.com
.
Select the target
Network
from the network dropdown.
Go to
Network-wide
>
General
.
Go to the
Reporting
section.
Locate
Syslog servers
and click
Add a syslog server
.
Provide the following configuration details:
Server IP
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Roles
: Select the log types to forward:
Flows
: Network flow data
URLs
: URL access logs
Security events
: IDS/IPS alerts
Appliance event log
: MX appliance events
Air Marshal events
: Wireless threat detection
IDS alerts
: Intrusion detection system alerts
Click
Save
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.action
Value is converted to uppercase. If the value is "deny", it's replaced with "BLOCK". If sc_action contains "allow", the value is replaced with "ALLOW". Otherwise, if decision contains "block", the value is replaced with "BLOCK". Otherwise, if authorization is "success", it's set to "ALLOW", and if "failure", it's set to "BLOCK". Otherwise, if pattern is "1 all", "deny all", or "Group Policy Deny", it's set to "BLOCK". If pattern is "allow all", "Group Policy Allow", or "0 all", it's set to "ALLOW". Otherwise, it's set to "UNKNOWN_ACTION". If decision contains "block", it's set to "BLOCK".
adId
principal.user.user_display_name
Directly mapped from the adId field in JSON logs.
agent
network.http.user_agent
Apostrophes are removed. Directly mapped from the agent field. Also converted to network.http.parsed_user_agent using the parseduseragent filter.
aid
network.session_id
Directly mapped from the aid field.
appProtocol
network.application_protocol
Converted to uppercase. Directly mapped from the appProtocol field.
attr
additional.fields
Added as a key-value pair to the additional.fields array with the key "attr".
authorization
security_result.action_details
Directly mapped from the authorization field in JSON logs.
band
additional.fields
Added as a key-value pair to the additional.fields array with the key "band".
bssids.bssid
principal.mac
Converted to lowercase. Merged into the principal.mac array.
bssids.detectedBy.device
intermediary.asset.asset_id
Formatted as "Device id: ".
bssids.detectedBy.rssi
intermediary.asset.product_object_id
Converted to a string.
Channel
about.resource.attribute.labels
Added as a key-value pair to the about.resource.attribute.labels array with the key "Channel".
clientDescription
additional.fields
Added as a key-value pair to the additional.fields array with the key "clientDescription".
clientId
additional.fields
Added as a key-value pair to the additional.fields array with the key "clientId".
clientIp
principal.ip, principal.asset.ip
Directly mapped from the clientIp field.
clientMac
principal.mac
Converted to lowercase. Directly mapped from the clientMac field in JSON logs.
client_ip
principal.ip, principal.asset.ip
Directly mapped from the client_ip field.
client_mac
principal.mac
Converted to lowercase. Directly mapped from the client_mac field.
code
additional.fields
Added as a key-value pair to the additional.fields array with the key "code".
collection_time
metadata.event_timestamp
The seconds and nanos fields are combined to create a timestamp.
Conditions
security_result.about.resource.attribute.labels
Carriage returns, newlines, and tabs are replaced with spaces and specific values are substituted. The modified value is added as a key-value pair to the security_result.about.resource.attribute.labels array with the key "Conditions".
decision
security_result.action
If the value is "blocked", it's set to "BLOCK".
desc
metadata.description
Directly mapped from the desc field.
description
security_result.description
Directly mapped from the description field in JSON logs.
DestAddress
target.ip, target.asset.ip
Directly mapped from the DestAddress field.
DestPort
target.port
Converted to an integer. Directly mapped from the DestPort field.
deviceIp
target.ip
Directly mapped from the deviceIp field.
deviceMac
target.mac
Converted to lowercase. Directly mapped from the deviceMac field.
deviceName
target.hostname, target.asset.hostname
Directly mapped from the deviceName field in JSON logs.
deviceSerial
target.asset.hardware.serial_number
Directly mapped from the deviceSerial field in JSON logs.
Direction
network.direction
Special characters are removed, and the value is mapped to network.direction.
DisabledPrivilegeList
target.user.attribute
Carriage returns, newlines, and tabs are replaced, and the modified value is parsed as JSON and merged into the target.user.attribute object.
dport
target.port
Converted to an integer. Directly mapped from the dport field.
dst
target.ip, target.asset.ip
Directly mapped from the dst field.
dstIp
target.ip, target.asset.ip
Directly mapped from the dstIp field.
dstPort
target.port
Converted to an integer. Directly mapped from the dstPort field.
dvc
intermediary.hostname
Directly mapped from the dvc field.
EnabledPrivilegeList
target.user.attribute
Carriage returns, newlines, and tabs are replaced, and the modified value is parsed as JSON and merged into the target.user.attribute object.
eventData.aid
principal.asset_id
Formatted as "ASSET_ID:".
eventData.client_ip
principal.ip, principal.asset.ip
Directly mapped from the eventData.client_ip field in JSON logs.
eventData.client_mac
principal.mac
Converted to lowercase. Directly mapped from the eventData.client_mac field in JSON logs.
eventData.group
principal.group.group_display_name
Directly mapped from the eventData.group field in JSON logs.
eventData.identity
principal.hostname
Directly mapped from the eventData.identity field in JSON logs.
eventData.ip
principal.ip, principal.asset.ip
Directly mapped from the eventData.ip field in JSON logs.
EventID
metadata.product_event_type, security_result.rule_name
Converted to a string. Mapped to metadata.product_event_type. Also used to create security_result.rule_name in the format "EventID: ". Used to determine event_type and sec_action.
eventSummary
security_result.summary, metadata.description
Directly mapped from the eventSummary field. Also used in security_result.description for some events.
eventType
metadata.product_event_type
Directly mapped from the eventType field. Used to determine which parsing logic to apply.
filename
principal.process.file.full_path
Directly mapped from the filename field.
FilterId
target.resource.product_object_id
Directly mapped from the FilterId field for EventID 5447.
FilterName
target.resource.name
Directly mapped from the FilterName field for EventID 5447.
FilterRTID
security_result.detection_fields
Added as a key-value pair to the security_result.detection_fields array with the key "FilterRTID".
firstSeen
security_result.detection_fields
Converted to a string. Added as a key-value pair to the security_result.detection_fields array with the key "firstSeen".
gatewayDeviceMac
target.mac
Converted to lowercase. Merged into the target.mac array.
group
additional.fields
Added as a key-value pair to the additional.fields array with the key "group".
GroupMembership
target.user
Carriage returns, newlines, tabs, and special characters are removed. The modified value is parsed as JSON and merged into the target.user object.
Hostname
principal.hostname, principal.asset.hostname
Directly mapped from the Hostname field.
identity
target.user.userid
Directly mapped from the identity field.
instigator
additional.fields
Added as a key-value pair to the additional.fields array with the key "instigator".
int_ip
intermediary.ip
Directly mapped from the int_ip field.
ip_msg
principal.resource.attribute.labels
Added as a key-value pair to the principal.resource.attribute.labels array with the key "IPs".
is_8021x
additional.fields
Added as a key-value pair to the additional.fields array with the key "is_8021x".
KeyName
target.resource.name
Directly mapped from the KeyName field.
KeyFilePath
target.file.full_path
Directly mapped from the KeyFilePath field.
lastSeen
security_result.detection_fields
Converted to a string. Added as a key-value pair to the security_result.detection_fields array with the key "lastSeen".
last_known_client_ip
principal.ip, principal.asset.ip
Directly mapped from the last_known_client_ip field.
LayerName
security_result.detection_fields
Added as a key-value pair to the security_result.detection_fields array with the key "Layer Name".
LayerRTID
security_result.detection_fields
Added as a key-value pair to the security_result.detection_fields array with the key "LayerRTID".
localIp
principal.ip, principal.asset.ip
Directly mapped from the localIp field.
login
principal.user.email_addresses
Directly mapped from the login field in JSON logs if it matches an email address format.
LogonGuid
additional.fields
Added as a key-value pair to the additional.fields array with the key "LogonGuid".
LogonType
extensions.auth.mechanism
Mapped to a specific authentication mechanism based on its value. If PreAuthType is present, it overrides LogonType. Values are mapped as follows: 2 -> USERNAME_PASSWORD, 3 -> NETWORK, 4 -> BATCH, 5 -> SERVICE, 7 -> UNLOCK, 8 -> NETWORK_CLEAR_TEXT, 9 -> NEW_CREDENTIALS, 10 -> REMOTE_INTERACTIVE, 11 -> CACHED_INTERACTIVE, 12 -> CACHED_REMOTE_INTERACTIVE, 13 -> CACHED_UNLOCK, other -> MECHANISM_UNSPECIFIED.
mac
principal.mac
Converted to lowercase. Merged into the principal.mac array.
MandatoryLabel
additional.fields
Added as a key-value pair to the additional.fields array with the key "MandatoryLabel".
Message
security_result.description, security_result.summary
If AccessReason is present, Message is mapped to security_result.summary and AccessReason is mapped to security_result.description. Otherwise, Message is mapped to security_result.description.
method
network.http.method
Directly mapped from the method field.
msg
security_result.description
Directly mapped from the msg field.
name
principal.user.user_display_name
Directly mapped from the name field in JSON logs.
natsrcIp
principal.nat_ip
Directly mapped from the natsrcIp field.
natsrcport
principal.nat_port
Converted to an integer. Directly mapped from the natsrcport field.
network_id
additional.fields
Added as a key-value pair to the additional.fields array with the key "Network ID".
NewProcessId
target.process.pid
Directly mapped from the NewProcessId field.
NewProcessName
target.process.file.full_path
Directly mapped from the NewProcessName field.
NewSd
target.resource.attribute.labels
Added as a key-value pair to the target.resource.attribute.labels array with the key "New Security Descriptor".
occurredAt
metadata.event_timestamp
Parsed as a timestamp using the ISO8601 format.
ObjectName
target.file.full_path, target.registry.registry_key, target.process.file.full_path, additional.fields
If EventID is 4663 and ObjectType is "Process", it's mapped to target.process.file.full_path. If ObjectType is "Key", it's mapped to target.registry.registry_key. Otherwise, it's mapped to target.file.full_path. For other events, it's added as a key-value pair to the additional.fields array with the key "ObjectName".
ObjectType
additional.fields
Added as a key-value pair to the additional.fields array with the key "ObjectType". Used to determine event_type.
OldSd
target.resource.attribute.labels
Added as a key-value pair to the target.resource.attribute.labels array with the key "Original Security Descriptor".
organizationId
principal.resource.id
Directly mapped from the organizationId field in JSON logs.
ParentProcessName
target.process.parent_process.file.full_path
Directly mapped from the ParentProcessName field.
pattern
security_result.description
Directly mapped to security_result.description. Used to determine security_result.action.
peer_ident
target.user.userid
Directly mapped from the peer_ident field.
PreAuthType
extensions.auth.mechanism
Used to determine the authentication mechanism if present. Overrides LogonType.
principalIp
principal.ip, principal.asset.ip
Directly mapped from the principalIp field.
principalMac
principal.mac
Converted to lowercase. Merged into the principal.mac array.
principalPort
principal.port
Converted to an integer. Directly mapped from the principalPort field.
prin_ip2
principal.ip, principal.asset.ip
Directly mapped from the prin_ip2 field.
prin_url
principal.url
Directly mapped from the prin_url field.
priority
security_result.priority
Mapped to a priority level based on its value: 1 -> HIGH_PRIORITY, 2 -> MEDIUM_PRIORITY, 3 -> LOW_PRIORITY, other -> UNKNOWN_PRIORITY.
ProcessID
principal.process.pid
Converted to a string. Directly mapped from the ProcessID field.
ProcessName
principal.process.file.full_path, target.process.file.full_path
If EventID is 4689, it's mapped to target.process.file.full_path. Otherwise, it's mapped to principal.process.file.full_path.
prod_log_id
metadata.product_log_id
Directly mapped from the prod_log_id field.
protocol
network.ip_protocol
Converted to uppercase. If it's a number, it's converted to its corresponding IP protocol name. If it's "ICMP6", it's replaced with "ICMP". Directly mapped from the protocol field.
ProviderGuid
metadata.product_deployment_id
Directly mapped from the ProviderGuid field.
query
network.dns.questions.name
Directly mapped from the query field.
query_type
network.dns.questions.type
Renamed to question.type and merged into the network.dns.questions array. Mapped to a numerical value based on the DHCP query type.
radio
additional.fields
Added as a key-value pair to the additional.fields array with the key "radio".
reason
additional.fields
Added as a key-value pair to the additional.fields array with the key "reason".
rec_bytes
network.received_bytes
Converted to an unsigned integer. Directly mapped from the rec_bytes field.
RecordNumber
metadata.product_log_id
Converted to a string. Directly mapped from the RecordNumber field.
RelativeTargetName
target.process.file.full_path
Directly mapped from the RelativeTargetName field.
response_ip
principal.ip, principal.asset.ip
Directly mapped from the response_ip field.
rssi
intermediary.asset.product_object_id
Directly mapped from the rssi field.
sc_action
security_result.action_details
Directly mapped from the sc_action field.
sec_action
security_result.action
Merged into the security_result.action array.
server_ip
client_ip
Directly mapped to the client_ip field.
Severity
security_result.severity
Mapped to a severity level based on its value: "Info" -> INFORMATIONAL, "Error" -> ERROR, "Warning" -> MEDIUM, other -> UNKNOWN_SEVERITY.
sha256
target.file.sha256
Directly mapped from the sha256 field.
signature
additional.fields
Added as a key-value pair to the additional.fields array with the key "signature".
SourceAddress
principal.ip, principal.asset.ip
Directly mapped from the SourceAddress field.
SourceHandleId
src.resource.id
Directly mapped from the SourceHandleId field.
SourceModuleName
observer.labels
Added as a key-value pair to the observer.labels array with the key "SourceModuleName".
SourceModuleType
observer.application
Directly mapped from the SourceModuleType field.
SourcePort
principal.port
Converted to an integer. Directly mapped from the SourcePort field.
SourceProcessId
src.process.pid
Directly mapped from the SourceProcessId field.
source_client_ip
client_ip
Directly mapped to the client_ip field.
sport
principal.port
Converted to an integer. Directly mapped from the sport field.
src
principal.ip, principal.asset.ip
Directly mapped from the src field.
ssid
network.session_id
Directly mapped from the ssid field in JSON logs.
ssidName
additional.fields
Added as a key-value pair to the additional.fields array with the key "ssidName".
state
additional.fields
Added as a key-value pair to the additional.fields array with the key "state".
Status
additional.fields
Added as a key-value pair to the additional.fields array with the key "Status".
status_code
network.http.response_code
Converted to an integer. Directly mapped from the status_code field.
SubjectDomainName
principal.administrative_domain
Directly mapped from the SubjectDomainName field.
SubjectLogonId
principal.resource.attribute.labels
Added as a key-value pair to the principal.resource.attribute.labels array with the key "SubjectLogonId".
SubjectUserName
principal.user.userid
Directly mapped from the SubjectUserName field.
SubjectUserSid
principal.user.windows_sid
Directly mapped from the SubjectUserSid field.
targetHost
target.hostname, target.asset.hostname
Converted to an IP address if possible. Otherwise, parsed to extract the hostname and mapped to target.hostname and target.asset.hostname.
TargetHandleId
target.resource.id
Directly mapped from the TargetHandleId field.
TargetLogonId
principal.resource.attribute.labels
Added as a key-value pair to the principal.resource.attribute.labels array with the key "TargetLogonId" if it's different from SubjectLogonId.
TargetProcessId
target.process.pid
Directly mapped from the TargetProcessId field.
TargetUserName
target.user.userid
Directly mapped from the TargetUserName field.
TargetUserSid
target.user.windows_sid
Directly mapped from the TargetUserSid field.
Task
additional.fields
Converted to a string. Added as a key-value pair to the additional.fields array with the key "Task".
timestamp
metadata.event_timestamp
The seconds field is used to create a timestamp.
ts
metadata.event_timestamp
If ts is empty, it's created by combining tsDate, tsTime, and tsTZ. If it contains "", it's parsed to extract the integer value. Then, it's parsed as a timestamp using various formats.
type
security_result.summary, metadata.product_event_type
Directly mapped from the type field in JSON logs. Also used as eventSummary and metadata.product_event_type in some cases.
url
target.url, principal.url
Directly mapped from the url field.
url1
target.url
Directly mapped from the url1 field.
user
target.user.group_identifiers
Merged into the target.user.group_identifiers array.
user_id
target.user.userid
Directly mapped from the user_id field.
UserID
principal.user.windows_sid
Directly mapped from the UserID field.
UserName
principal.user.userid
Directly mapped from the UserName field.
user_agent
network.http.user_agent
Directly mapped from the user_agent field.
userId
target.user.userid
Directly mapped from the userId field.
vap
additional.fields
Added as a key-value pair to the additional.fields array with the key "vap".
VirtualAccount
security_result.about.labels
Added as a key-value pair to the security_result.about.labels array with the key "VirtualAccount".
wiredLastSeen
security_result.detection_fields
Converted to a string. Added as a key-value pair to the security_result.detection_fields array with the key "wiredLastSeen".
wiredMacs
intermediary.mac
Converted to lowercase. Merged into the intermediary.mac array.
WorkstationName
principal.hostname, principal.asset.hostname
Directly mapped from the WorkstationName field.
Need more help?
Get answers from Community members and Google SecOps professionals.
