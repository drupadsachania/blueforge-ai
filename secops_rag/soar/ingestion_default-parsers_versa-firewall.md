# Collect Versa Networks Secure Access Service Edge (SASE) 
logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/versa-firewall/  
**Scraped:** 2026-03-05T10:02:08.250523Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Versa Networks Secure Access Service Edge (SASE) 
logs
Supported in:
Google secops
SIEM
This document describes how you can collect the Versa Networks Secure Access Service Edge (SASE) logs. The parser extracts key-value pairs after an initial grok filter. It then maps these values to the Unified Data Model (UDM), handling various log formats like firewall events, application logs, and alarm logs, and performs conversions and enrichments for specific fields like IP protocol and risk score.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Versa SASE.
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
system where Bindplane Agent will be installed.
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
Install Bindplane Agent
Windows Installation
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
Linux Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:54525"
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
`
/path/to/ingestion-authentication-file.json`
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
SYSLOG
namespace
:
versa_networks_sase
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
tcplog
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
Restart Bindplane Agent to apply the changes
In Linux, to restart the Bindplane Agent, run the following command:
sudo
systemctl
restart
bindplane-agent
In Windows, to restart the Bindplane Agent, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Versa Networks SASE
Administrators must configure remote collectors on each Versa Analytics node to forward logs to third-party systems.
To configure the Versa analytics nodes, do the following:
Enable log forwarding
Enable session ID logging
Enable log forwarding
Sign in to the
Versa analytics server
.
Go to
CLI
by running the
cli
command.
Switch to
Configuration mode
by running the
configure
command, and then enter
load merge terminal
.
Copy and paste the following commands to set up log forwarding:
Replace
<collector_ip>
and
<collector_port>
with the IP address and port of your syslog collector (Bindplane).
set
system
analytics
log-collector-exporter
destination-address
<collector_ip>
set
system
analytics
log-collector-exporter
destination-port
<collector_port>
set
system
analytics
log-collector-exporter
transport
tcp
set
system
analytics
log-collector-exporter
log-types
firewall-log
set
system
analytics
log-collector-exporter
log-types
threat-log
commit
Save the configuration:
save
Enable session ID logging
To log IP-related information, enable session ID logging.
Sign in to
Versa Director
.
Switch to
Director View
.
Go to
Configuration
>
Devices
>
Tenant
>
Device
to access
Appliance View
.
Select
Configuration
>
Others
>
System
>
Configuration
>
Configuration
.
In the
Parameters
pane, click
Edit
.
In the
Edit parameters
window, select
LEF
.
In the
Firewall
section, select the
Include session ID logging
checkbox.
Click
OK
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
accCkt
additional.fields[].key
: "accCkt"
additional.fields[].value.string_value
:
accCkt
Value taken directly from the
accCkt
field.
accCktId
additional.fields[].key
: "accCktId"
additional.fields[].value.string_value
:
accCktId
Value taken directly from the
accCktId
field.
accCktName
additional.fields[].key
: "accCktName"
additional.fields[].value.string_value
:
accCktName
Value taken directly from the
accCktName
field.
accessType
additional.fields[].key
: "accessType"
additional.fields[].value.string_value
:
accessType
Value taken directly from the
accessType
field.
action
security_result.action
:
action
If
action
,
type
,
idpAction
,
avAction
, or
urlAction
are "allow" then
ALLOW
. If
action
,
type
,
idpAction
,
avAction
, or
urlAction
are "reject", "drop", "block", "deny" then
BLOCK
. If
idpAction
is anything else then
UNKNOWN_ACTION
.
alarmCause
security_result.detection_fields[].key
: "alarmCause"
security_result.detection_fields[].value
:
alarmCause
Value taken directly from the
alarmCause
field.
alarmClass
security_result.detection_fields[].key
: "alarmClass"
security_result.detection_fields[].value
:
alarmClass
Value taken directly from the
alarmClass
field.
alarmClearable
security_result.detection_fields[].key
: "alarmClearable"
security_result.detection_fields[].value
:
alarmClearable
Value taken directly from the
alarmClearable
field.
alarmEventType
metadata.product_event_type
:
alarmEventType
Value taken directly from the
alarmEventType
field.
alarmKey
security_result.detection_fields[].key
: "alarmKey"
security_result.detection_fields[].value
:
alarmKey
Value taken directly from the
alarmKey
field.
alarmKind
security_result.detection_fields[].key
: "alarmKind"
security_result.detection_fields[].value
:
alarmKind
Value taken directly from the
alarmKind
field.
alarmOwner
security_result.detection_fields[].key
: "alarmOwner"
security_result.detection_fields[].value
:
alarmOwner
Value taken directly from the
alarmOwner
field.
alarmSeqNo
security_result.detection_fields[].key
: "alarmSeqNo"
security_result.detection_fields[].value
:
alarmSeqNo
Value taken directly from the
alarmSeqNo
field.
alarmSeverity
security_result.severity_details
:
alarmSeverity
Value taken directly from the
alarmSeverity
field.
alarmText
security_result.summary
:
alarmText
Value taken directly from the
alarmText
field, with double quotes removed.
alarmType
security_result.description
:
alarmType
Value taken directly from the
alarmType
field.
appFamily
metadata.product_event_type
:
appFamily
security_result.detection_fields[].key
: "appFamily"
security_result.detection_fields[].value
:
appFamily
Value taken directly from the
appFamily
field.
appId
security_result.detection_fields[].key
: "Application ID"
security_result.detection_fields[].value
:
appId
Value taken directly from the
appId
field.
appIdStr
security_result.detection_fields[].key
: "appIdStr"
security_result.detection_fields[].value
:
appIdStr
Value taken directly from the
appIdStr
field.
applianceName
principal.hostname
:
applianceName
Value taken directly from the
applianceName
,
siteName
, or
site
field.
appProductivity
security_result.detection_fields[].key
: "appProductivity"
security_result.detection_fields[].value
:
appProductivity
Value taken directly from the
appProductivity
field.
appRisk
security_result.severity_details
:
appRisk
Value taken directly from the
appRisk
field.
appSubFamily
security_result.detection_fields[].key
: "appSubFamily"
security_result.detection_fields[].value
:
appSubFamily
Value taken directly from the
appSubFamily
field.
avAccuracy
additional.fields[].key
: "avAccuracy"
additional.fields[].value.string_value
:
avAccuracy
Value taken directly from the
avAccuracy
field.
avAction
security_result.action
:
avAction
See
action
for logic.
avMalwareName
security_result.threat_name
:
avMalwareName
Value taken directly from the
avMalwareName
field.
avMalwareType
security_result.category_details
:
avMalwareType
Value taken directly from the
avMalwareType
field.
classMsg
security_result.description
:
classMsg
Value taken directly from the
classMsg
field, with double quotes removed.
clientIPv4Address
target.ip
:
clientIPv4Address
Value taken directly from the
clientIPv4Address
field.
destIp
target.ip
:
destIp
destinationIPv4Address
:
destIp
Value taken directly from the
destIp
field.
destinationIPv4Address
target.ip
:
destinationIPv4Address
Value taken directly from the
destinationIPv4Address
or derived from
networkPrefix
field.
destinationIPv6Address
target.ip
:
destinationIPv6Address
Value taken directly from the
destinationIPv6Address
field.
destinationPort
target.port
:
destinationPort
Value taken directly from the
destinationPort
field and converted to integer.
destinationTransportPort
target.port
:
destinationTransportPort
Value taken directly from the
destinationTransportPort
field and converted to integer.
deviceKey
about.resource.attribute.labels[].key
: "deviceKey"
about.resource.attribute.labels[].value
:
deviceKey
Value taken directly from the
deviceKey
field if not "Unknown".
deviceName
about.resource.attribute.labels[].key
: "deviceName"
about.resource.attribute.labels[].value
:
deviceName
Value taken directly from the
deviceName
field if not "Unknown".
duration
network.session_duration.seconds
:
duration
Value taken directly from the
duration
field and converted to integer.
egressInterfaceName
additional.fields[].key
: "egressInterfaceName"
additional.fields[].value.string_value
:
egressInterfaceName
Value taken directly from the
egressInterfaceName
field.
event.type
metadata.event_type
:
event.type
If both
applianceName
(or
sourceIPv4Address
or
user
or
sourceIPv6Address
) and
destinationIPv4Address
(or
remoteSite
or
destinationIPv6Address
or
clientIPv4Address
or
hostname
) are present, then
NETWORK_CONNECTION
. Otherwise,
STATUS_UPDATE
. If
applianceName
is empty, then
GENERIC_EVENT
.
eventType
principal.resource.attribute.labels[].key
: "eventType"
principal.resource.attribute.labels[].value
:
eventType
Value taken directly from the
eventType
field.
family
security_result.detection_fields[].key
: "family"
security_result.detection_fields[].value
:
family
Value taken directly from the
family
field.
fc
security_result.detection_fields[].key
: "ForwardingClass"
security_result.detection_fields[].value
:
fc
Value taken directly from the
fc
field.
fileTransDir
additional.fields[].key
: "fileTransDir"
additional.fields[].value.string_value
:
fileTransDir
Value taken directly from the
fileTransDir
field.
filename
target.file.names
:
filename
Value taken directly from the
filename
field.
flowCookie
metadata.collected_timestamp
:
flowCookie
Value taken directly from the
flowCookie
field and converted to timestamp using UNIX format.
flowId
principal.resource.product_object_id
:
flowId
Value taken directly from the
flowId
field.
forwardForwardingClass
security_result.detection_fields[].key
: "forwardForwardingClass"
security_result.detection_fields[].value
:
forwardForwardingClass
Value taken directly from the
forwardForwardingClass
field.
fromCountry
principal.location.country_or_region
:
fromCountry
target.location.country_or_region
:
fromCountry
Value taken directly from the
fromCountry
field.
fromUser
principal.user.userid
:
fromUser
Value taken directly from the
fromUser
field if not empty, "unknown", or "Unknown".
fromZone
additional.fields[].key
: "fromZone"
additional.fields[].value.string_value
:
fromZone
Value taken directly from the
fromZone
field.
generateTime
metadata.collected_timestamp
:
generateTime
Value taken directly from the
generateTime
field and converted to timestamp using UNIX format.
hostname
target.hostname
:
hostname
Value taken directly from the
hostname
field.
httpUrl
target.url
:
httpUrl
Value taken directly from the
httpUrl
field.
icmpTypeIPv4
additional.fields[].key
: "icmpTypeIPv4"
additional.fields[].value.string_value
:
icmpTypeIPv4
Value taken directly from the
icmpTypeIPv4
field.
idpAction
security_result.action
:
idpAction
See
action
for logic.
ingressInterfaceName
additional.fields[].key
: "ingressInterfaceName"
additional.fields[].value.string_value
:
ingressInterfaceName
Value taken directly from the
ingressInterfaceName
field.
ipsApplication
additional.fields[].key
: "ipsApplication"
additional.fields[].value.string_value
:
ipsApplication
Value taken directly from the
ipsApplication
field.
ipsDirection
security_result.detection_fields[].key
: "ipsDirection"
security_result.detection_fields[].value
:
ipsDirection
Value taken directly from the
ipsDirection
field.
ipsProfile
security_result.detection_fields[].key
: "ipsProfile"
security_result.detection_fields[].value
:
ipsProfile
Value taken directly from the
ipsProfile
field.
ipsProfileRule
security_result.rule_name
:
ipsProfileRule
Value taken directly from the
ipsProfileRule
field.
ipsProtocol
network.ip_protocol
:
ipsProtocol
Value taken directly from the
ipsProtocol
field.
log_type
metadata.description
:
log_type
metadata.log_type
:
log_type
Value taken directly from the
log_type
field.
mstatsTimeBlock
metadata.collected_timestamp
:
mstatsTimeBlock
Value taken directly from the
mstatsTimeBlock
field and converted to timestamp using UNIX format.
mstatsTotRecvdOctets
network.received_bytes
:
mstatsTotRecvdOctets
Value taken directly from the
mstatsTotRecvdOctets
field and converted to unsigned integer.
mstatsTotSentOctets
network.sent_bytes
:
mstatsTotSentOctets
Value taken directly from the
mstatsTotSentOctets
field and converted to unsigned integer.
mstatsTotSessCount
additional.fields[].key
: "mstatsTotSessCount"
additional.fields[].value.string_value
:
mstatsTotSessCount
Value taken directly from the
mstatsTotSessCount
field.
mstatsTotSessDuration
network.session_duration.seconds
:
mstatsTotSessDuration
Value taken directly from the
mstatsTotSessDuration
field and converted to integer.
mstatsType
security_result.category_details
:
mstatsType
Value taken directly from the
mstatsType
field.
networkPrefix
target.ip
:
networkPrefix
target.port
:
networkPrefix
IP address extracted from the
networkPrefix
field. Port extracted from the
networkPrefix
field and converted to integer.
protocolIdentifier
network.ip_protocol
:
protocolIdentifier
Value taken directly from the
protocolIdentifier
field, converted to integer, and mapped to IP protocol name using a lookup.
recvdOctets
network.received_bytes
:
recvdOctets
Value taken directly from the
recvdOctets
field and converted to unsigned integer.
recvdPackets
network.received_packets
:
recvdPackets
Value taken directly from the
recvdPackets
field and converted to integer.
remoteSite
target.hostname
:
remoteSite
Value taken directly from the
remoteSite
field.
reverseForwardingClass
security_result.detection_fields[].key
: "reverseForwardingClass"
security_result.detection_fields[].value
:
reverseForwardingClass
Value taken directly from the
reverseForwardingClass
field.
risk
security_result.risk_score
:
risk
Value taken directly from the
risk
field and converted to float.
rule
security_result.rule_name
:
rule
Value taken directly from the
rule
field.
sentOctets
network.sent_bytes
:
sentOctets
Value taken directly from the
sentOctets
field and converted to unsigned integer.
sentPackets
network.sent_packets
:
sentPackets
Value taken directly from the
sentPackets
field and converted to integer.
serialNum
security_result.detection_fields[].key
: "serialNum"
security_result.detection_fields[].value
:
serialNum
Value taken directly from the
serialNum
field.
signatureId
security_result.detection_fields[].key
: "signatureID"
security_result.detection_fields[].value
:
signatureId
Value taken directly from the
signatureId
field.
signatureMsg
security_result.detection_fields[].key
: "signatureMsg"
security_result.detection_fields[].value
:
signatureMsg
Value taken directly from the
signatureMsg
field.
signaturePriority
security_result.severity
:
signaturePriority
If
signaturePriority
is "low" (case-insensitive), then
LOW
. If
signaturePriority
is "medium" (case-insensitive), then
MEDIUM
. If
signaturePriority
is "high" (case-insensitive), then
HIGH
.
site
principal.hostname
:
site
applianceName
:
site
Value taken directly from the
site
field.
siteId
additional.fields[].key
: "siteId"
additional.fields[].value.string_value
:
siteId
Value taken directly from the
siteId
field.
siteName
principal.hostname
:
siteName
applianceName
:
siteName
Value taken directly from the
siteName
field.
sourceIPv4Address
principal.ip
:
sourceIPv4Address
Value taken directly from the
sourceIPv4Address
field.
sourceIPv6Address
principal.ip
:
sourceIPv6Address
Value taken directly from the
sourceIPv6Address
field.
sourcePort
principal.port
:
sourcePort
Value taken directly from the
sourcePort
field and converted to integer.
sourceTransportPort
principal.port
:
sourceTransportPort
Value taken directly from the
sourceTransportPort
field and converted to integer.
subFamily
security_result.detection_fields[].key
: "subFamily"
security_result.detection_fields[].value
:
subFamily
Value taken directly from the
subFamily
field.
tcpConnAborted
additional.fields[].key
: "tcpConnAborted"
additional.fields[].value.string_value
:
tcpConnAborted
Value taken directly from the
tcpConnAborted
field if not empty or "0".
tcpConnRefused
additional.fields[].key
: "tcpConnRefused"
additional.fields[].value.string_value
:
tcpConnRefused
Value taken directly from the
tcpConnRefused
field if not empty or "0".
tcpPktsFwd
network.sent_packets
:
tcpPktsFwd
Value taken directly from the
tcpPktsFwd
field and converted to integer.
tcpPktsRev
network.received_packets
:
tcpPktsRev
Value taken directly from the
tcpPktsRev
field and converted to integer.
tcpReXmitFwd
additional.fields[].key
: "tcpReXmitFwd"
additional.fields[].value.string_value
:
tcpReXmitFwd
Value taken directly from the
tcpReXmitFwd
field if not empty or "0".
tcpReXmitRev
additional.fields[].key
: "tcpReXmitRev"
additional.fields[].value.string_value
:
tcpReXmitRev
Value taken directly from the
tcpReXmitRev
field if not empty or "0".
tcpSAA
additional.fields[].key
: "tcpSAA"
additional.fields[].value.string_value
:
tcpSAA
Value taken directly from the
tcpSAA
field if not empty or "0".
tcpSSA
additional.fields[].key
: "tcpSSA"
additional.fields[].value.string_value
:
tcpSSA
Value taken directly from the
tcpSSA
field if not empty or "0".
tcpSessCnt
additional.fields[].key
: "tcpSessCnt"
additional.fields[].value.string_value
:
tcpSessCnt
Value taken directly from the
tcpSessCnt
field.
tcpSessDur
network.session_duration.seconds
:
tcpSessDur
Value taken directly from the
tcpSessDur
field and converted to integer.
tcpSynAckReXmit
additional.fields[].key
: "tcpSynAckReXmit"
additional.fields[].value.string_value
:
tcpSynAckReXmit
Value taken directly from the
tcpSynAckReXmit
field if not empty or "0".
tcpSynReXmit
additional.fields[].key
: "tcpSynReXmit"
additional.fields[].value.string_value
:
tcpSynReXmit
Value taken directly from the
tcpSynReXmit
field if not empty or "0".
tcpTWHS
additional.fields[].key
: "tcpTWHS"
additional.fields[].value.string_value
:
tcpTWHS
Value taken directly from the
tcpTWHS
field if not empty or "0".
tenantId
principal.resource.attribute.labels[].key
: "tenantId"
principal.resource.attribute.labels[].value
:
tenantId
Value taken directly from the
tenantId
field.
tenantName
observer.hostname
:
tenantName
Value taken directly from the
tenantName
field.
threatType
security_result.detection_fields[].key
: "threatType"
security_result.detection_fields[].value
:
threatType
Value taken directly from the
threatType
field.
toCountry
target.location.country_or_region
:
toCountry
Value taken directly from the
toCountry
field.
toZone
additional.fields[].key
: "toZone"
additional.fields[].value.string_value
:
toZone
Value taken directly from the
toZone
field.
traffType
additional.fields[].key
: "traffType"
additional.fields[].value.string_value
:
traffType
Value taken directly from the
traffType
field.
ts
metadata.event_timestamp
:
ts
Value taken directly from the
ts
field and converted to timestamp.
type
security_result.action
:
type
See
action
for logic.
urlAction
security_result.action
:
urlAction
See
action
for logic.
urlActionMessage
security_result.summary
:
urlActionMessage
Value taken directly from the
urlActionMessage
field.
urlCategory
principal.resource.attribute.labels[].key
: "urlCategory"
principal.resource.attribute.labels[].value
:
urlCategory
Value taken directly from the
urlCategory
field.
urlProfile
additional.fields[].key
: "urlProfile"
additional.fields[].value.string_value
:
urlProfile
Value taken directly from the
urlProfile
field.
urlReputation
security_result.severity_details
:
urlReputation
Value taken directly from the
urlReputation
field.
user
principal.ip
:
user
Value taken directly from the
user
field.
vsnId
principal.resource.attribute.labels[].key
: "vsnId"
principal.resource.attribute.labels[].value
:
vsnId
Value taken directly from the
vsnId
field. Hardcoded value. Hardcoded value.
Need more help?
Get answers from Community members and Google SecOps professionals.
