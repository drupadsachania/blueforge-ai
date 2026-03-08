# Collect Cisco FireSIGHT Management Center logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firesight/  
**Scraped:** 2026-03-05T09:21:27.447456Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco FireSIGHT Management Center logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco FireSIGHT Management Center logs to Google Security Operations using Bindplane agent.
Cisco FireSIGHT Management Center (FMC), formerly known as FireSIGHT Management Center or Firepower Management Center, is a centralized management console that provides comprehensive policy management, event analysis, and reporting for Cisco Secure Firewall Threat Defense devices. FMC can send connection events, security intelligence events, intrusion events, file events, and malware events via syslog to external SIEM systems.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and Cisco FireSIGHT Management Center
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco FireSIGHT Management Center web interface
Admin or Security Analyst user role in FMC
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
chronicle/cisco_fmc
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
CISCO_FIRESIGHT
raw_log_field
:
body
ingestion_labels
:
env
:
production
source
:
fmc
service
:
pipelines
:
logs/fmc_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/cisco_fmc
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on UDP port
51
. If port
514
requires root privileges on Linux, use port
1514
instead and configure FMC to send to that port.
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
: Replace with your
customer ID
. For details, see
Get Google SecOps customer ID
.
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
log_type
: Set to
CISCO_FIRESIGHT
(exact match required)
ingestion_labels
: Optional labels for filtering and organization
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
To restart the Bindplane agent in Linux:
Run the following command:
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
To restart the Bindplane agent in Windows:
Choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press Enter.
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
Configure Cisco FireSIGHT Management Center syslog forwarding
This section describes how to configure FMC to send security event syslog messages (connection, security intelligence, intrusion, file, and malware events) from Firepower Threat Defense devices to the Bindplane agent.
Configure syslog settings for Firepower Threat Defense devices
Sign in to the
Cisco FireSIGHT Management Center
web interface.
Go to
Devices
>
Platform Settings
.
Edit the platform settings policy associated with your Firepower Threat Defense device, or create a new policy.
In the left navigation pane, click
Syslog
.
Click
Syslog Servers
and click
Add
to configure a new syslog server.
Provide the following configuration details:
IP Address
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
Protocol
: Select
UDP
.
Port
: Enter
514
(or
1514
if you configured Bindplane to listen on a non-privileged port).
Interface
: Select the management interface or the interface that can reach the Bindplane agent.
Click
OK
to save the syslog server configuration.
Click
Syslog Settings
and configure the following settings:
Check
Enable Timestamp on Syslog Messages
.
Timestamp Format
: Select
ISO 8601
(recommended for Chronicle).
Check
Enable Syslog Device ID
and optionally enter a custom device identifier.
Click
Logging Setup
.
Select whether or not to
Send syslogs in EMBLEM format
. For Chronicle ingestion, either format is supported.
Click
Save
to save the platform settings policy.
Configure access control policy logging settings
In the Cisco FireSIGHT Management Center web interface, go to
Policies
>
Access Control
.
Edit the applicable access control policy.
Click the
Logging
tab.
Select
FTD 6.3 and later: Use the syslog settings configured in the FTD Platform Settings policy deployed on the device
.
Optionally select a
Syslog Severity
level (for example,
Info
or
Alert
).
If you will send file and malware events, check
Send Syslog messages for File and Malware events
.
Click
Save
.
Enable logging for Security Intelligence events
In the same access control policy, click the
Security Intelligence
tab.
In each of the following locations, click
Logging
and enable logging:
Beside
DNS Policy
: Click
Logging
, enable
Log at Beginning of Connection
and
Log at End of Connection
, and enable
Syslog Server
.
In the
Block List
box for
Networks
: Click
Logging
, enable
Log at Beginning of Connection
and
Log at End of Connection
, and enable
Syslog Server
.
In the
Block List
box for
URLs
: Click
Logging
, enable
Log at Beginning of Connection
and
Log at End of Connection
, and enable
Syslog Server
.
Click
Save
.
Enable syslog logging for access control rules
In the same access control policy, click the
Rules
tab.
Click a rule to edit.
Click the
Logging
tab in the rule.
Choose whether to log the beginning or end of connections, or both:
Check
Log at Beginning of Connection
(generates high volume).
Check
Log at End of Connection
(recommended for most use cases).
If you will log file events, check
Log Files
.
Check
Syslog Server
.
Verify that the rule is
Using default syslog configuration in Access Control Logging
. Do not configure overrides.
Click
Add
to save the rule.
Repeat steps 2-8 for each rule in the policy that you want to log.
Configure intrusion policy syslog settings
Navigate to
Policies
>
Intrusion
.
Edit the intrusion policy associated with your access control policy.
Click
Advanced Settings
>
Syslog Alerting
.
Set
Syslog Alerting
to
Enabled
.
Click
Edit
next to
Syslog Alerting
.
Configure the following settings:
Logging Host
: Leave this blank to use the syslog settings configured in the FTD Platform Settings. If you specify a logging host here, you must also configure
Facility
and
Severity
.
Facility
: Only applicable if you specify a
Logging Host
. Select a facility (for example,
AUTH
or
LOCAL0
).
Severity
: Only applicable if you specify a
Logging Host
. Select a severity level (for example,
Info
or
Alert
).
Click
Back
.
Click
Policy Information
in the left navigation pane.
Click
Commit Changes
.
Deploy configuration changes
After configuring all syslog settings, deploy the changes to your managed devices.
In the Cisco FireSIGHT Management Center web interface, click
Deploy
in the top right corner.
Select the devices to which you want to deploy the configuration.
Click
Deploy
to apply the changes.
Verify syslog forwarding
Generate test traffic or security events on your Firepower Threat Defense devices.
Check the Bindplane agent logs to verify that syslog messages are being received:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Sign in to the Google SecOps console and verify that events are appearing in the
Events
viewer.
Supported event types
Cisco FireSIGHT Management Center can send the following event types via syslog to Google SecOps:
Event Type
Description
Connection Events
Network connection data between monitored hosts and all other hosts
Security Intelligence Events
Events related to Security Intelligence block lists (IP, URL, DNS)
Intrusion Events
Intrusion detection and prevention events generated by managed devices
File Events
File analysis events
Malware Events
Malware detection events
Syslog message format
Cisco FireSIGHT Management Center sends syslog messages in the following format:
Example connection event:
<134>1 2024-01-15T10:15:45.123Z fmc-hostname %FTD-6-430003:
EventPriority: Low,
DeviceUUID: abc123,
InstanceID: 1,
FirstPacketSecond: 1705318545,
ConnectionID: 12345,
AccessControlRuleAction: Allow,
SrcIP: 10.0.0.5,
DstIP: 8.8.8.8,
SrcPort: 54321,
DstPort: 53,
Protocol: udp,
IngressInterface: inside,
EgressInterface: outside,
IngressZone: inside-zone,
EgressZone: outside-zone,
ACPolicy: Default-Policy,
AccessControlRuleName: Allow-DNS,
User: user@example.com,
ApplicationProtocol: DNS,
InitiatorBytes: 64,
ResponderBytes: 128
Example intrusion event:
<134>1 2024-01-15T10:16:30.456Z fmc-hostname %FTD-4-430001:
EventPriority: High,
DeviceUUID: abc123,
InstanceID: 1,
SrcIP: 192.168.1.100,
DstIP: 10.0.0.50,
SrcPort: 12345,
DstPort: 80,
Protocol: tcp,
IngressInterface: outside,
EgressInterface: inside,
IngressZone: outside-zone,
EgressZone: inside-zone,
IntrusionPolicy: Security-Over-Connectivity,
SignatureID: 1:2024123:1,
SignatureGeneratorID: 1,
Classification: web-application-attack,
Priority: 1,
Message: SQL injection attempt detected
The syslog messages include key-value pairs separated by commas, making them suitable for parsing by Google SecOps.
Limitations
It may take up to 15 minutes for events to appear in Google SecOps after being sent from FMC.
Retrospective malware events are not available via syslog.
Events generated by AMP for Endpoints are not available via syslog.
Some metadata available via eStreamer API is not included in syslog messages (for example, detailed user information from LDAP, extended application metadata, geolocation data).
If you configure object names (policy names, rule names) with special characters such as commas, they may interfere with syslog parsing. Avoid using special characters in object names.
UDM mapping table
Log Field
UDM Mapping
Logic
WebApplication, URLReputation, EgressInterface, IngressInterface, ACPolicy, NAPPolicy, ConnectionID, ssl_ticket_id, qoa_applied_interface, sinkhole_uuid, security_context, sec_zone_egress, sec_zone_ingress
additional.fields
Merged from various label fields if not empty
eventType
extensions.auth.type
Set to "VPN" if eventType is "USER_LOGIN_INFORMATION"
vulnerabilities
extensions.vulns.vulnerabilities
Merged from vulnerabilities if not empty
flowStatistics.httpReferrer
http.referral_url
Value copied directly
flowStatistics.httpResponse
http.response_code
Converted to integer
flowStatistics.userAgent
http.user_agent
Value copied directly
_intermediary
intermediary
Merged from _intermediary if not empty
recordTypeDescription, entry.message
metadata.description
Value from recordTypeDescription if not empty, else from entry.message
event_second, connection_timestamp, _serverTimestamp
metadata.event_timestamp
Date parsed from event_second if not empty, else connection_timestamp, else _serverTimestamp
event_type
metadata.event_type
Value copied directly
prod_event_type, eventId, recordTypeCategory, app, _recordTypeName, eventType
metadata.product_event_type
Value from prod_event_type if not empty, else eventId, else recordTypeCategory, else app, else _recordTypeName, else eventType
DeviceUUID
metadata.product_log_id
Value copied directly
flowStatistics.clientAppVersion, client_version
metadata.product_version
Value from flowStatistics.clientAppVersion if not empty, else client_version
flowStatistics.clientAppURL
metadata.url_back_to_product
Value copied directly
ApplicationProtocol
network.application_protocol
Set to "LDAP" if matches (?i)ldap, "HTTPS" if (?i)https, "HTTP" if (?i)http
answer
network.dns.answers
Merged from answer
flowStatistics.dnsQuery
network.dns.answers.name
Value copied directly
flowStatistics.dnsTTL
network.dns.answers.ttl
Converted to uinteger
flowStatistics.dnsRecordType
network.dns.answers.type
Converted to uinteger
flowStatistics.dnsResponseType
network.dns.response_code
Converted to uinteger
user_agent
network.http.parsed_user_agent
Converted to parseduseragent
user_agent
network.http.user_agent
Value copied directly
proto, Protocol, inputType, proto_type, protocol, ip_v4_protocol, protocol_number_src
network.ip_protocol
Set based on various fields with protocol mappings and cases
ResponderBytes, flowStatistics.bytesReceived
network.received_bytes
Value from ResponderBytes if not empty, else flowStatistics.bytesReceived, converted to uinteger
ResponderPackets
network.received_packets
Converted to integer
InitiatorBytes, flowStatistics.bytesSent
network.sent_bytes
Value from InitiatorBytes if not empty, else flowStatistics.bytesSent, converted to uinteger
InitiatorPackets, packet_data
network.sent_packets
Value from InitiatorPackets if not empty, else packet_data, converted to integer
ssl_session_id
network.session_id
Value copied directly
ssl_cipher_suite
network.tls.cipher
Value copied directly
agent_type, agent_version
observer.application
Concatenated as agent_type agent_version if both not empty
entry.host.hostname
observer.hostname
Value copied directly
entry.host.ip
observer.ip
Merged from entry.host.ip
entry.host.mac
observer.mac
Merged from entry.host.mac
clientApplication, hold.app_string
principal.application
Value from clientApplication if not empty, else hold.app_string
prin_host, DeviceAddress, principal_hostname
principal.asset.hostname
Value from prin_host if not empty, else DeviceAddress if sourceAddress empty, else principal_hostname
SrcIP, principal_ip, source_address_IPv4v6
principal.asset.ip
Merged from SrcIP (grok validated), principal_ip, source_address_IPv4v6 (grok validated)
file_sha_hash, sha_hash
principal.file.sha256
Value from file_sha_hash if not empty, else sha_hash
prin_host, DeviceAddress, principal_hostname
principal.hostname
Value from prin_host if not empty, else DeviceAddress if sourceAddress empty, else principal_hostname
SrcIP, principal_ip, source_address_IPv4v6
principal.ip
Merged from SrcIP (grok validated), principal_ip, source_address_IPv4v6 (grok validated)
flowStatistics.initiatorCountry.geolocation.countryName, src_ip_country
principal.location.country_or_region
Value from flowStatistics.initiatorCountry.geolocation.countryName if not empty, else src_ip_country
entry.macAddress
principal.mac
Merged from entry.macAddress
host_os_platform
principal.platform
Set to LINUX if centos, else uppercased entry.host.os.platform
entry.host.os.kernel
principal.platform_patch_level
Value copied directly
identityData.fingerprintUUID.osName, osFingerprint.fingerprintUUID.osName
principal.platform_version
Concatenated osName osVersion from identityData if not empty, else osFingerprint
SrcPort, entry.sourcePort, entry.sourcePortOrIcmpType, source_port, flowStatistics.initiatorPort, source_port_or_icmp_code
principal.port
Value from SrcPort if not empty, else entry.sourcePort, else entry.sourcePortOrIcmpType, else source_port, else flowStatistics.initiatorPort, else source_port_or_icmp_code, converted to integer
isecurityZoneName
principal.resource.attribute.labels
Merged from isecurityZoneName
DeviceType
principal.resource.name
Value copied directly
principal.resource.resource_type
Set to "DEVICE"
entry.computed.user
principal.user.user_display_name
Converted to string
entry.userId, user_id, flowStatistics.user.userId, entry.computed.user, userLoginInformation.userName
principal.user.userid
Value from entry.userId if not empty, else user_id, else flowStatistics.user.userId, else entry.computed.user, else userLoginInformation.userName
connectionID_label, FirstPacketSecond_label
sec_result.about.resource.attribute.labels
Merged from connectionID_label and FirstPacketSecond_label if not empty
sec_result_action
sec_result.action
Merged from sec_result_action
flowStatistics.securityIntelligenceList1.securityIntelligenceListName
sec_result.category
Set to NETWORK_MALICIOUS if rule_name is Malware, NETWORK_SUSPICIOUS if Anomali_IP
classification.description, userLoginInformation.description, sec_desc
sec_result.description
Value from classification.description if not empty, else userLoginInformation.description, else sec_desc
entry.computed.priority
sec_result.priority
Uppercased entry.computed.priority _PRIORITY
entry.ruleId, rule_ruleId
sec_result.rule_id
Value from entry.ruleId if not empty, else rule_ruleId
AccessControlRuleName, rule_message, fw_rule, flowStatistics.securityIntelligenceList1.securityIntelligenceListName
sec_result.rule_name
Value from AccessControlRuleName if not empty, else rule_message, else fw_rule, else flowStatistics.securityIntelligenceList1.securityIntelligenceListName
EventPriority, sec_severity, severity_code, priority_name
sec_result.severity
Set to LOW if EventPriority Low, HIGH if High, MEDIUM if Medium; else from sec_severity mappings; else from severity_code mappings; else priority_name uppercased
User
sec_result.summary
Value copied directly
threat_name
sec_result.threat_name
Value copied directly
security_result
security_result
Merged from security_result
firewallRuleAction, hold.action, AccessControlRuleAction, sec_result_action, vendor_blocked
security_result.action
Value from firewallRuleAction uppercased if not no_action, else hold.action, else from AccessControlRuleAction with cases, else sec_result_action, else from vendor_blocked (0 ALLOW, else BLOCK)
disposition
security_result.action_details
Set to "Infected" if disposition 3, else "Unknown"
eventDescription
security_result.description
Value copied directly
firewallRule
security_result.rule_name
Value copied directly
threat_name
security_result.threat_name
Value copied directly
hostService.webApplication.webApplication0.applicationId.webApplicationName
target.application
Value copied directly
DstIP, entry.destinationIpAddress, dest_ip, flowStatistics.responderIPAddress, destination_address_IPv4v6
target.asset.ip
Merged from DstIP (grok), entry.destinationIpAddress, dest_ip, flowStatistics.responderIPAddress, destination_address_IPv4v6 (grok)
InstanceID, flowStatistics.clientAppId
target.asset_id
Value from InstanceID if not empty, else " Client_app_id: " + flowStatistics.clientAppId
file
target.file
Renamed from file
DstIP, entry.destinationIpAddress, dest_ip, flowStatistics.responderIPAddress, destination_address_IPv4v6
target.ip
Merged from DstIP (grok), entry.destinationIpAddress, dest_ip, flowStatistics.responderIPAddress, destination_address_IPv4v6 (grok)
flowStatistics.responderCountry.geolocation.countryName, dest_ip_country, entry.country.data
target.location.country_or_region
Value from flowStatistics.responderCountry.geolocation.countryName if not empty, else dest_ip_country, else entry.country.data
MACAddress
target.mac
Lowercased MACAddress if not 00:00:00:00:00:00
DstPort, entry.destinationPort, entry.destinationPortOrIcmpType, dest_port, flowStatistics.responderPort, destination_port_or_icmp_code
target.port
Value from DstPort if not empty, else entry.destinationPort, else entry.destinationPortOrIcmpType, else dest_port, else flowStatistics.responderPort, else destination_port_or_icmp_code, converted to integer
securityZoneName, det_engine, file_num, file_pos, rec_length
target.resource.attribute.labels
Merged from securityZoneName, det_engine, file_num, file_pos, rec_length if not empty
URL
target.url
Value copied directly
entry.user.username.data
target.user.userid
Value copied directly
descript
vulnerabilities.description
Value copied directly
severity_detail
vulnerabilities.severity_details
Value copied directly
product
vulnerabilities.vendor
Value copied directly
metadata.product_name
Set to "CISCO_FIRESIGHT"
metadata.vendor_name
Set to "CISCO MANAGEMENT CENTER"
Need more help?
Get answers from Community members and Google SecOps professionals.
