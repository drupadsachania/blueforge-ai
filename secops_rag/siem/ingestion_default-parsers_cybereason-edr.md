# Collect Cybereason EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybereason-edr/  
**Scraped:** 2026-03-05T09:22:56.049713Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cybereason EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cybereason EDR logs to Google Security Operations using the Bindplane agent.
Cybereason EDR (Endpoint Detection and Response) is a cybersecurity platform that detects and responds to advanced threats across endpoints. It identifies Malops (Malicious Operations) — correlated attack chains that tie together suspicious activities into complete attack narratives — and provides security analysts with visibility into threat progression, affected machines, compromised users, and network connections.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and the Cybereason Detection Server
If running behind a proxy, ensure firewall ports are open as per the Bindplane agent requirements
Access to Cybereason management console with the System Admin role
Cybereason platform version 20.1 or later
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where the Bindplane agent will be installed.
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
The service status should be
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
The service status should be
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send it to Google SecOps
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
tcplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/cybereason
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'your-customer-id'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
CYBEREASON_EDR
raw_log_field
:
body
service
:
pipelines
:
logs/cybereason_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/cybereason
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on:
0.0.0.0:514
to listen on all interfaces on port 514 (requires root on Linux)
0.0.0.0:1514
to listen on an unprivileged port (recommended for Linux non-root)
Receiver type options:
tcplog
for TCP syslog (required for Cybereason syslog forwarding)
Exporter configuration:
creds_file_path
: Full path to the Google SecOps ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Google SecOps customer ID
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
for the complete list
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
Verify that the service is running:
sudo
systemctl
status
observiq-otel-collector
Check the logs for errors:
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
Verify that the service is running:
sc query observiq-otel-collector
Check the logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Cybereason EDR syslog forwarding
Cybereason sends MalOp and User Audit events in CEF (Common Event Format) via syslog. Syslog forwarding configuration requires a request to Cybereason Technical Support.
Request syslog forwarding from Cybereason Technical Support
Sign in to the
Cybereason management console
.
Contact
Cybereason Technical Support
through the Cybereason support portal.
Submit a syslog forwarding configuration request with the following information:
Syslog server IP address
: The IP address of the Bindplane agent host (for example,
192.168.1.100
).
Syslog server port
: The port matching the Bindplane agent
listen_address
(for example,
514
).
Protocol
: TCP (unencrypted TCP syslog).
Log types
: Request forwarding of the following log types:
MalOp syslog
: Security alerts and Malicious Operations events
User Audit syslog
: User activity and administrative actions
Wait for Cybereason Technical Support to confirm the syslog forwarding configuration.
Configure firewall rules
Ensure the following firewall rules are in place:
Direction
Protocol
Port
Source
Destination
Outbound
TCP
514
Cybereason Detection Server
Bindplane agent host
Alternative: Cybereason CEF Forwarder
If Cybereason Technical Support is unable to configure direct syslog forwarding, you can use the Cybereason CEF Forwarder tool:
Download the Cybereason CEF Forwarder Docker image from Cybereason Technical Support.
Create or edit the configuration file at
cybereason-forwarders/config/config.json
.
Configure the following settings:
{
"host"
:
"<BINDPLANE_AGENT_IP>"
,
"port"
:
514
}
Replace
<BINDPLANE_AGENT_IP>
with the IP address of the Bindplane agent host.
Build and run the Docker container:
docker
build
-t
cybereason-cef-forwarder
.
docker
run
-d
--name
cybereason-forwarder
cybereason-cef-forwarder
Syslog event types
Cybereason generates CEF syslog messages for the following event categories:
Event Category
Description
MalOp created
New Malicious Operation detected
MalOp updated
Existing MalOp status or details changed
MalOp closed
MalOp resolved or closed by analyst
Malware detected
Malware identified on an endpoint
Suspicious process
Suspicious process activity detected
Network connection
Suspicious network connection identified
User login
User authentication events
Machine isolation
Endpoint isolated from or reconnected to the network
Policy changes
Security policy modifications
Verify syslog forwarding
After Cybereason Technical Support confirms the syslog configuration, perform a test action in the Cybereason console (for example, view a MalOp or isolate a test machine).
Check the Bindplane agent logs for incoming syslog messages:
Linux
:
sudo journalctl -u observiq-otel-collector -f
Windows
:
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Verify that CEF-formatted messages appear in the logs, for example:
CEF:0|Cybereason|Cybereason|2.0|MalOp|MalOp Created|8|cs1=MALOP_ID_HERE dvchost=server01.company.com suser=admin@company.com
UDM mapping table
Log Field
UDM Mapping
Logic
detectionName_label
additional.fields
Mapped as key-value pair
sensorId_label
additional.fields
Mapped as key-value pair
status
metadata.description
If value is not empty
log_description
metadata.description
Fallback if status is empty
(CEF format)
metadata.event_type
Set to GENERIC_EVENT for CEF logs
event_type
metadata.event_type
Set to PROCESS_OPEN if value is "PROCESS_OPEN", NETWORK_CONNECTION if value is "NETWORK_CONNECTION", SCAN_HOST if value is "MALWARE"
has_principal, has_target
metadata.event_type
Set to SCAN_FILE if both has_principal and has_target are true
has_principal
metadata.event_type
Set to STATUS_UPDATE if only has_principal is true
has_user
metadata.event_type
Set to USER_UNCATEGORIZED if has_user is true in Malop context
(default)
metadata.event_type
Set to GENERIC_EVENT otherwise
LogType
metadata.product_event_type
If value is not empty
malop_data.simpleValues.elementDisplayName.values.0
metadata.product_event_type
Fallback if LogType is empty
type
metadata.product_event_type
Fallback
prod_event, prod_event2
metadata.product_event_type
Concatenated as prod_event - prod_event2
malop_process.guidString
metadata.product_log_id
For PROCESS_OPEN event type
malop_connection.guidString
metadata.product_log_id
For NETWORK_CONNECTION event type
guid
metadata.product_log_id
For MALWARE or Malop event types
(static)
metadata.product_version
Set to "2.0" initially
Sensor.version
metadata.product_version
Overwrites "2.0" if present
malop_url
metadata.url_back_to_product
Directly mapped
(static)
metadata.vendor_name
Set to "Cybereason"
direction
network.direction
Directly mapped
malop_connection.simpleValues.transportProtocol.values.0
network.ip_protocol
Directly mapped
malop_connection.simpleValues.receivedBytesCount.values.0
network.received_bytes
Converted to unsigned integer
malop_connection.simpleValues.transmittedBytesCount.values.0
network.sent_bytes
Converted to unsigned integer
Sensor.fqdn
principal.administrative_domain
Directly mapped
malop_process.elementValues.ownerMachine.elementValues.0.guid
principal.asset.asset_id
Prefixed with "Cybereason:"
malop_data.elementValues.affectedMachines.elementValues.0.guid
principal.asset.asset_id
Prefixed with "Cybereason:", fallback
malop_process.elementValues.ownerMachine.elementValues.0.name
principal.asset.hostname
Directly mapped
malop_data.elementValues.affectedMachines.elementValues.0.name
principal.asset.hostname
Fallback
machineName
principal.asset.hostname
Fallback
host
principal.asset.hostname
Fallback
dvchost
principal.asset.hostname
Fallback
Sensor.fqdn
principal.asset.hostname
Fallback
client.ip
principal.asset.ip
Directly mapped
Sensor.externalIpAddress
principal.asset.ip
Fallback
malop_process.elementValues.ownerMachine.elementValues.0.name
principal.hostname
Directly mapped
malop_data.elementValues.affectedMachines.elementValues.0.name
principal.hostname
Fallback
machineName
principal.hostname
Fallback
host
principal.hostname
Fallback
dvchost
principal.hostname
Fallback
Sensor.fqdn
principal.hostname
Fallback
client.ip
principal.ip
Directly mapped
Sensor.externalIpAddress
principal.ip
Fallback
Sensor.internalIpAddress
principal.nat_ip
Directly mapped
Sensor.privateServerIp
principal.nat_ip
Fallback
Sensor.osType
principal.platform
Set to WINDOWS if value is "WINDOWS", LINUX if "LINUX", MAC if "MAC"
Sensor.osVersionType
principal.platform_version
Directly mapped
malop_connection.simpleValues.localPort.values.0
principal.port
Converted to integer
malop_process.simpleValues.commandLine.values.0
principal.process.command_line
Directly mapped
malwareDataModel.filePath
principal.process.command_line
Fallback
malop_process.simpleValues.calculatedName.values.0
principal.process.file.full_path
Directly mapped
name
principal.process.file.full_path
Fallback
malop_process.elementValues.parentProcess.elementValues.0.guid
principal.process.parent_process.product_specific_process_id
Prefixed with "Cybereason:"
malop_process.elementValues.self.elementValues.0.guid
principal.process.pid
Directly mapped
malop_process.elementValues.self.elementValues.0.guid
principal.process.product_specific_process_id
Prefixed with "Cybereason:"
malop_connection.elementValues.ownerProcess.elementValues.0.guid
principal.process.product_specific_process_id
Prefixed with "Cybereason:", fallback
companyName
principal.user.company_name
Directly mapped
malop_process.elementValues.calculatedUser.elementValues.0.name
principal.user.user_display_name
Directly mapped
malop_data.elementValues.affectedUsers.elementValues.0.name
principal.user.user_display_name
Fallback
malop_connection.elementValues.ownerProcess.user.elementValues.0.name
principal.user.user_display_name
Fallback
malop_process.elementValues.calculatedUser.elementValues.0.guid
principal.user.userid
Directly mapped
malop_data.elementValues.affectedUsers.elementValues.0.guid
principal.user.userid
Fallback
malop_connection.elementValues.ownerProcess.user.elementValues.0.guid
principal.user.userid
Fallback
security_result_action
security_result.action
Set to ALLOW, BLOCK, or QUARANTINE based on status
is_alert
security_result.alert_state
Set to ALERTING if value is True
sr_category
security_result.category
Set to SOFTWARE_MALICIOUS or NETWORK_MALICIOUS
query_details
security_result.detection_fields
Mapped as key-value pair
affected_machine_count
security_result.detection_fields
Mapped as key-value pair
link_to_malop
security_result.detection_fields
Mapped as key-value pair
context_label
security_result.detection_fields
Mapped as key-value pair
old_state_label
security_result.detection_fields
Mapped as key-value pair
new_state_label
security_result.detection_fields
Mapped as key-value pair
investigation_label
security_result.detection_fields
Mapped as key-value pair
event_id_label
security_result.detection_fields
Mapped as key-value pair
malop_activity_type_label
security_result.detection_fields
Mapped as key-value pair
malop_suspect_label
security_result.detection_fields
Mapped as key-value pair
malop_key_suspicion_label
security_result.detection_fields
Mapped as key-value pair
device_custom_date_label
security_result.detection_fields
Mapped as key-value pair
device_custom_date2_label
security_result.detection_fields
Mapped as key-value pair
device_custom_date3_label
security_result.detection_fields
Mapped as key-value pair
guid_label
security_result.detection_fields
Mapped as key-value pair
displayName_label
security_result.detection_fields
Mapped as key-value pair
pylumId_label
security_result.detection_fields
Mapped as key-value pair
connected_label
security_result.detection_fields
Mapped as key-value pair
isolated_label
security_result.detection_fields
Mapped as key-value pair
osType_label
security_result.detection_fields
Mapped as key-value pair
admin_label
security_result.detection_fields
Mapped as key-value pair
domainUser_label
security_result.detection_fields
Mapped as key-value pair
localSystem_label
security_result.detection_fields
Mapped as key-value pair
description
security_result.description
Concatenated with decision_feature, malop_status, privileges, passwordAgeDays, elementType, status, score, detectionValue, detectionValueType, detectionEngine
decision_feature
security_result.description
Concatenated into description
malop_status
security_result.description
Concatenated into description
privileges
security_result.description
Concatenated into description
passwordAgeDays
security_result.description
Concatenated into description
elementType
security_result.description
Concatenated into description
status
security_result.description
Concatenated into description
score
security_result.description
Concatenated into description
detectionValue
security_result.description
Concatenated into description
detectionValueType
security_result.description
Concatenated into description
detectionEngine
security_result.description
Concatenated into description
malop_data.malopPriority
security_result.priority
Directly mapped
malop_severity
security_result.severity
Directly mapped
security_severity
security_result.severity
Set to CRITICAL if value > 8, HIGH if > 6, MEDIUM if > 4, LOW if > 1
severity
security_result.severity
Set to INFORMATIONAL if "Info", ERROR if "Error" or "High", MEDIUM if "Warning" or "Medium", CRITICAL if "Critical", LOW if "Low", UNKNOWN otherwise
description
security_result.summary
Directly mapped
type
security_result.summary
Fallback
malopId
security_result.threat_id
Directly mapped
malop_data.simpleValues.detectionType.values.0
security_result.threat_name
Directly mapped
virusName
security_result.threat_name
Fallback
status
security_result.threat_status
Set to ACTIVE if value is "Active", otherwise FALSE_POSITIVE
malop_url
security_result.url_back_to_product
Directly mapped
machineName
target.asset.hostname
Directly mapped
affectedMachine
target.asset.hostname
Fallback
dvchost
target.asset.hostname
Fallback
Sensor.serverName
target.asset.hostname
Fallback
server.ip
target.asset.ip
Directly mapped
Sensor.serverIp
target.asset.ip
Fallback
malop_process.simpleValues.calculatedName.values.0
target.file.full_path
Directly mapped
malop_connection.elementValues.ownerProcess.elementValues.0.name
target.file.full_path
Fallback
name
target.file.full_path
Fallback
malwareDataModel_filePath
target.file.full_path
Fallback
malop_process.simpleValues.imageFile.md5String.values.0
target.file.md5
Directly mapped
name
target.file.names
Directly mapped
machineName
target.hostname
Directly mapped
affectedMachine
target.hostname
Fallback
dvchost
target.hostname
Fallback
Sensor.serverName
target.hostname
Fallback
server.ip
target.ip
Directly mapped
Sensor.serverIp
target.ip
Fallback
malop_connection.simpleValues.remoteAddressCountryName.values.0
target.location.country_or_region
Directly mapped
Sensor.privateServerIp
target.nat_ip
Directly mapped
malop_connection.simpleValues.remotePort.values.0
target.port
Converted to integer
malop_process.simpleValues.calculatedName.values.0
target.process.file.full_path
Directly mapped
malop_process.elementValues.self.elementValues.0.guid
target.process.pid
Directly mapped
malop_url
target.url
Directly mapped
(static)
metadata.product_name
Set to "Cybereason"
Need more help?
Get answers from Community members and Google SecOps professionals.
