# Collect FireEye eMPS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-emps/  
**Scraped:** 2026-03-05T09:24:22.281232Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FireEye eMPS logs
Supported in:
Google secops
SIEM
This document explains how to ingest FireEye eMPS logs to Google Security Operations using Bindplane agent.
FireEye Email Malware Protection System (eMPS), also known as FireEye EX Series (formerly FireEye Email Security, now part of Trellix Email Security), is an email security appliance that protects organizations from advanced email threats including spear phishing, malware, and targeted attacks by analyzing email content and attachments in real time.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between Bindplane agent and FireEye eMPS appliance
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the FireEye eMPS appliance CLI (Admin or Operator role)
FireEye eMPS appliance with syslog notification capability
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Click
Download
to download the
ingestion authentication file
.
Save the file securely on the system where Bindplane agent will be installed.
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
Install Bindplane agent
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
chronicle/fireeye_emps
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
FIREEYE_EMPS
raw_log_field
:
body
ingestion_labels
:
env
:
production
service
:
pipelines
:
logs/fireeye_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/fireeye_emps
Configuration parameters
Replace the following placeholders:
Receiver configuration:
The receiver is configured for UDP syslog on port 514 (standard syslog port).
To use a non-privileged port on Linux, change
514
to
1514
or higher.
To use TCP instead of UDP, replace
udplog
with
tcplog
.
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Replace
YOUR_CUSTOMER_ID
with the customer ID from the previous step.
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
for complete list.
log_type
: Must be exactly
FIREEYE_EMPS
to match the Chronicle parser.
ingestion_labels
: Optional labels in YAML format (customize as needed).
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
Restart Bindplane agent to apply the changes
Linux
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
Windows
Choose one of the following options:
Using Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Using Services console:
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
Configure FireEye eMPS syslog forwarding
Configure the FireEye eMPS appliance to forward syslog notifications to the Bindplane agent using the CLI.
Access the FireEye eMPS CLI
Connect to the FireEye eMPS appliance via SSH or console.
Log in with an account that has Admin or Operator privileges.
Enter enable mode:
hostname> enable
Enter configuration mode:
hostname# configure terminal
Configure syslog server
Add the Bindplane agent as a syslog trap sink:
hostname
(
config
)
#
fenotify
rsyslog
trap
-
sink
chronicle
address
<
BINDPLANE_IP_ADDRESS
>
Replace
<BINDPLANE_IP_ADDRESS>
with the IP address of the host running Bindplane agent (for example,
192.168.1.100
).
Set the syslog format to CEF (Common Event Format):
hostname(config)# fenotify rsyslog trap-sink chronicle prefer message format cef
Set the syslog facility to local4 (recommended):
hostname(config)# fenotify syslog default facility local4
Set the delivery mode to send notifications per event:
hostname(config)# fenotify rsyslog trap-sink chronicle message delivery per-event
Set the alert severity to alert level (recommended):
hostname(config)# fenotify rsyslog trap-sink chronicle prefer message send-as alert
Set the protocol to UDP (or TCP if configured in Bindplane):
hostname(config)# fenotify rsyslog trap-sink chronicle protocol udp
Set the port to 514 (or the port configured in Bindplane):
hostname(config)# fenotify rsyslog trap-sink chronicle port 514
Enable syslog notifications
Enable rsyslog notifications globally:
hostname(config)# fenotify rsyslog enable
Enable global notifications:
hostname(config)# fenotify enable
Enable specific alert types for rsyslog. For example, to enable all email-related alerts:
hostname(config)# fenotify rsyslog alert malware-object enable
hostname(config)# fenotify rsyslog alert malware-callback enable
hostname(config)# fenotify rsyslog alert infection-match enable
hostname(config)# fenotify rsyslog alert domain-match enable
Verify the configuration:
hostname(config)# show fenotify alerts
This command displays the enabled notification methods and alert types.
Save the configuration:
hostname(config)# write memory
Exit configuration mode:
hostname(config)# exit
hostname# exit
Test syslog connectivity
Send a test syslog message to verify connectivity:
hostname# fenotify rsyslog send-test
Check the Bindplane agent logs to confirm receipt of the test message:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-n
50
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Verify logs are appearing in Google SecOps console (allow 5 to 10 minutes for initial ingestion).
Additional configuration notes
FireEye eMPS sends syslog messages in CEF (Common Event Format) when configured as shown above.
The syslog messages include email threat details such as sender, recipient, subject, malware names, URLs, file hashes, and threat severity.
Ensure firewall rules allow UDP (or TCP) traffic from the FireEye eMPS appliance to the Bindplane agent on the configured port.
For detailed CLI command reference, consult the FireEye documentation portal at
https://docs.fireeye.com/
(login required).
UDM mapping table
Log Field
UDM Mapping
Logic
_hash
about.file.sha256
Value taken from _hash
_message
security_result_token.description
Value taken from _message if has_invalid_msg is false
IPv6_Address
event.idm.read_only_udm.target.ip
Value taken from IPv6_Address if not "-"
Action_Taken
security_result.action_details
Value taken from Action_Taken
CustomerName
event.idm.read_only_udm.target.user.user_display_name
Value taken from CustomerName after removing quotes
Device_name
event.idm.read_only_udm.principal.hostname
Value taken from Device_name if present
Domene
sntdom
Value taken from Domene if Domain not present
Domain
sntdom
Value taken from Domain
Emne
about.process.command_line
Value taken from Emne if Subject not present
Enhetsnavn
event.idm.read_only_udm.principal.hostname
Value taken from Enhetsnavn if Device_name not present
File_name
event.idm.read_only_udm.target.process.file.full_path
Value taken from File_name
Generated
event.idm.read_only_udm.metadata.event_timestamp
Converted from Generated to timestamp format
Group_name
event.idm.read_only_udm.principal.group.group_display_name
Value taken from Group_name
Gruppenavn
event.idm.read_only_udm.principal.group.group_display_name
Value taken from Gruppenavn if Group_name not present
Infected_Resource
event.idm.read_only_udm.target.process.file.full_path
Value taken from Infected_Resource if others not present
Infection_Channel
security_result.detection_fields
Key set to "Infection Channel", value from Infection_Channel
IPv6_Address
target_machine_id_present
Set to true if IPv6_Address not "-"
Object
event.idm.read_only_udm.target.process.file.full_path
Value taken from Object if File_name not present
Objekt
event.idm.read_only_udm.target.process.file.full_path
Value taken from Objekt if others not present
Operasjon
operasjon_label
Value taken from Operasjon
Operation
operation_label
Value taken from Operation
Path
about.process.command_line
Value taken from Path if others not present
Permission
permission_label
Value taken from Permission
Received
event.idm.read_only_udm.metadata.collected_timestamp
Converted from Received to timestamp format
Resource_Type
event.idm.read_only_udm.target.resource.attribute.labels
Key set to "Resource_Type", value from Resource_Type
Result
security_result.summary
Value taken from Result
Scan_Type
security_result.description
Value taken from Scan_Type if Type not present
Spyware
security_result.threat_name
Value taken from Spyware
Spyware_Grayware_Type
security_result.detection_fields
Key set to "Spyware/Grayware_Type", value from Spyware_Grayware_Type
Subject
about.process.command_line
Value taken from Subject
Threat_Probability
security_result.detection_fields
Key set to "Threat_Probability", value from Threat_Probability
Tillatelse
tillatelse_label
Value taken from Tillatelse
Type
security_result.description
Value taken from Type
Unknown_Threat
security_result.threat_name
Value taken from Unknown_Threat if others not present
User
event.idm.read_only_udm.target.user.userid
Value taken from User
Virus_Malware_Name
security_result.threat_name
Value taken from Virus_Malware_Name if Spyware not present
_metadata.customer
security_result_token.detection_fields
Key set to "Customer", value from _metadata.customer
_metadata.proxy.address
event.idm.read_only_udm.principal.hostname
Value taken from _metadata.proxy.address
_metadata.proxy.address
event.idm.read_only_udm.principal.asset.hostname
Value taken from _metadata.proxy.address
_metadata.source.address
principal.hostname
Value taken from _metadata.source.address
_metadata.source.address
principal.asset.hostname
Value taken from _metadata.source.address
_metadata.source.port
principal.port
Converted from _metadata.source.port to integer
_metadata.source.type
security_result_token.detection_fields
Key set to "Type", value from _metadata.source.type
_metadata.timestamp.producer_process
event.idm.read_only_udm.metadata.event_timestamp
Converted from _metadata.timestamp.producer_process to timestamp format
_metadata.timestamp.producer_process
metadata.event_timestamp
Converted from _metadata.timestamp.producer_process to timestamp format
about
event.idm.read_only_udm.about
Merged from about
about_token
event.idm.read_only_udm.about
Merged from about_token
act
security_result.action
Derived from act: accept/notified → ALLOW; deny/blocked → BLOCK; Failure → FAIL
act
security_result.action_details
Value taken from act
additional_cs1
event.idm.read_only_udm.additional.fields
Key set to cs1Label, value from cs1
additional_cs2
event.idm.read_only_udm.additional.fields
Key set to cs2Label, value from cs2
additional_cs3
event.idm.read_only_udm.additional.fields
Key set to cs3Label, value from cs3 if not empty
additional_cs4
event.idm.read_only_udm.additional.fields
Key set to cs4Label, value from cs4
additional_cs5
event.idm.read_only_udm.additional.fields
Key set to cs5Label, value from cs5 if not NA
additional_cs6
event.idm.read_only_udm.additional.fields
Key set to cs6Label, value from cs6 if not empty
additional_cs7
event.idm.read_only_udm.additional.fields
Key set to cs7Label, value from cs7 if not empty
additional_cn1
event.idm.read_only_udm.additional.fields
Key set to cn1Label, value from cn1 if not empty
additional_cn2
event.idm.read_only_udm.additional.fields
Key set to cn2Label, value from cn2 if not empty
additional_cn3
event.idm.read_only_udm.additional.fields
Key set to cn3Label, value from cn3 if not empty
additional_cfp1
event.idm.read_only_udm.additional.fields
Key set to cfp1Label, value from cfp1 if not empty
additional_cfp2
event.idm.read_only_udm.additional.fields
Key set to cfp2Label, value from cfp2 if not empty
additional_cfp3
event.idm.read_only_udm.additional.fields
Key set to cfp3Label, value from cfp3 if not empty
additional_cfp4
event.idm.read_only_udm.additional.fields
Key set to cfp4Label, value from cfp4 if not empty
additional_devicePayloadId
event.idm.read_only_udm.additional.fields
Key set to "devicePayloadId", value from devicePayloadId
additional_eventId
event.idm.read_only_udm.additional.fields
Key set to "eventId", value from eventId
additional_fname
event.idm.read_only_udm.additional.fields
Key set to "fname", value from fname if not N/A
additional_flexString1
event.idm.read_only_udm.additional.fields
Key set to flexString1Label, value from flexString1
additional_flexString2
event.idm.read_only_udm.additional.fields
Key set to flexString2Label, value from flexString2 if not empty
app
app_protocol_src
Value taken from app
appcategory
security_result.summary
Value taken from appcategory
base64_sha256
event.idm.read_only_udm.network.tls.client.certificate.sha256
Converted from Sha256 to base64 hex
base64_sha256
event.idm.read_only_udm.target.resource.name
Value taken from base64_sha256
cat
security_result.category_details
Value taken from cat
cs5
cs5_label
Value taken from cs5 if label not set
cs5_label
event.idm.read_only_udm.additional.fields
Key set to "cs5 Label", value from cs5 if invalid
destinationServiceName
event.idm.read_only_udm.target.application
Value taken from destinationServiceName
destinationTranslatedAddress
event.idm.read_only_udm.target.nat_ip
Value taken from destinationTranslatedAddress
destinationTranslatedPort
event.idm.read_only_udm.target.nat_port
Converted from destinationTranslatedPort to integer
deviceDirection
event.idm.read_only_udm.network.direction
Set to INBOUND if 0, OUTBOUND if 1
deviceExternalId
about.asset.asset_id
Value taken from deviceExternalId as "device_vendor.device_product:deviceExternalId"
deviceNtDomain
about.administrative_domain
Value taken from deviceNtDomain
devicePayloadId
additional_devicePayloadId
Value taken from devicePayloadId
deviceProcessName
about.process.command_line
Value taken from deviceProcessName
deviceTranslatedAddress
about.nat_ip
Value taken from deviceTranslatedAddress
device_vendor
event.idm.read_only_udm.metadata.vendor_name
Value taken from device_vendor
device_version
event.idm.read_only_udm.metadata.product_version
Value taken from device_version
dhost
temp_dhost
Value taken from dhost
dmac
event.idm.read_only_udm.target.mac
Value taken from dmac after formatting
dmac
mac_address
Value taken from dmac after formatting
dntdom
event.idm.read_only_udm.target.administrative_domain
Value taken from dntdom
dpid
event.idm.read_only_udm.target.process.pid
Value taken from dpid
dpriv
target_role
Value taken from dpriv
dproc
event.idm.read_only_udm.target.process.command_line
Value taken from dproc
dpt
event.idm.read_only_udm.target.port
Converted from dpt to integer
dst
event.idm.read_only_udm.target.asset.ip
Value taken from dst
dst
event.idm.read_only_udm.target.ip
Value taken from dst
dst_ip
target_ip
Value taken from dst_ip
duid
temp_duid
Value taken from duid
duser
event.idm.read_only_udm.metadata.event_type
Set to USER_UNCATEGORIZED if duser not empty
duser
temp_duser
Value taken from duser
dvchost
about.hostname
Value taken from dvchost
dvcmac
about.mac
Value taken from dvcmac after formatting if valid MAC
dvcmac
dvc_mac
Value taken from dvcmac after formatting
dvcpid
about.process.pid
Value taken from dvcpid
dvc
about.ip
Split from dvc array
eventId
additional_eventId
Value taken from eventId
event_name
event.idm.read_only_udm.metadata.product_event_type
Combined with device_event_class_id as "[device_event_class_id] - event_name" or just event_name
event_name
event.idm.read_only_udm.metadata.event_type
Set to SCAN_UNCATEGORIZED if LogSpyware or LogPredictiveMachineLearning
eventid
eventId
Value taken from eventid
externalId
event.idm.read_only_udm.metadata.product_log_id
Value taken from externalId
fileHash
about.file.sha256
Value taken from fileHash if valid hash
fileHash
about.file.full_path
Value taken from fileHash if not valid hash
filePath
about.file.full_path
Value taken from filePath
filePermission
permissions
Value taken from filePermission
fileType
about.file.mime_type
Value taken from fileType
flexString2
additional_flexString2
Value taken from flexString2
flexString2Label
additional_flexString2
Value taken from flexString2Label
fname
additional_fname
Value taken from fname
fsize
about.file.size
Converted from fsize to uinteger
has_principal
metadata.event_type
Set to STATUS_UPDATE if has_principal true and has_target false
has_principal
principal_present
Set to true
has_target
metadata.event_type
Set to GENERIC_EVENT if has_principal false
in
event.idm.read_only_udm.network.received_bytes
Converted from in to uinteger if >0
infection_channel_label
security_result.detection_fields
Key set to "Infection Channel", value from Infection_Channel
ipv6
target_machine_id_present
Set to true if IPv6_Address not "-"
mac
event.idm.read_only_udm.principal.mac
Value taken from mac
mac_address
event.idm.read_only_udm.target.mac
Value taken from mac_address
mac_address
about.mac
Value taken from mac_address
metadata
event.idm.read_only_udm.metadata
Renamed from metadata
msg
event.idm.read_only_udm.metadata.description
Value taken from msg after removing quotes
msg_data_2
security_result.description
Value taken from msg_data_2 if not empty
mwProfile
security_result.rule_name
Value taken from mwProfile
oldFilePath
event.idm.read_only_udm.src.file.full_path
Value taken from oldFilePath
oldFilePermission
old_permissions
Value taken from oldFilePermission
oldFileSize
event.idm.read_only_udm.src.file.size
Converted from oldFileSize to uinteger
operasjon_label
security_result.detection_fields
Merged from operasjon_label if value not empty
operation_label
security_result.detection_fields
Merged from operation_label if value not empty
out
event.idm.read_only_udm.network.sent_bytes
Converted from out to uinteger if >0
permission_label
security_result.detection_fields
Merged from permission_label if value not empty
port
event.idm.read_only_udm.principal.port
Converted from port to integer
principal
event.idm.read_only_udm.principal
Renamed from principal
proto
protocol_number_src
Value taken from proto
request
event.idm.read_only_udm.target.url
Value taken from request
requestClientApplication
event.idm.read_only_udm.network.http.user_agent
Value taken from requestClientApplication
requestMethod
event.idm.read_only_udm.network.http.method
Value taken from requestMethod
resource_Type_label
event.idm.read_only_udm.target.resource.attribute.labels
Merged from resource_Type_label if not invalid
rt
event.idm.read_only_udm.metadata.event_timestamp
Converted from rt to timestamp format
security_result
event.idm.read_only_udm.security_result
Merged from security_result
security_result_token
event.idm.read_only_udm.security_result
Merged from security_result_token
severity
security_result.severity
Derived from severity: 0-1 → LOW; 2-3 → MEDIUM; 4-5 → HIGH; 6-9 → CRITICAL
shost
event.idm.read_only_udm.principal.hostname
Value taken from shost if IP, else hostname
shost
event.idm.read_only_udm.principal.ip
Value taken from shost if IP
shost_present
shost_present
Set to true
smac
event.idm.read_only_udm.principal.mac
Value taken from smac after formatting
smac
mac
Value taken from smac after formatting
sntdom
event.idm.read_only_udm.principal.administrative_domain
Value taken from sntdom
sourceDnsDomain
event.idm.read_only_udm.target.asset.hostname
Value taken from sourceDnsDomain hostname
sourceDnsDomain
event.idm.read_only_udm.target.hostname
Value taken from sourceDnsDomain hostname
sourceServiceName
event.idm.read_only_udm.principal.application
Value taken from sourceServiceName
sourceTranslatedAddress
event.idm.read_only_udm.principal.nat_ip
Value taken from sourceTranslatedAddress
sourceTranslatedPort
event.idm.read_only_udm.principal.nat_port
Converted from sourceTranslatedPort to integer
spid
event.idm.read_only_udm.principal.process.pid
Value taken from spid
spriv
principal_role
Value taken from spriv
sproc
event.idm.read_only_udm.principal.process.command_line
Value taken from sproc
spt
event.idm.read_only_udm.principal.port
Converted from spt to integer if valid
src
event.idm.read_only_udm.principal.asset.ip
Value taken from src
src
event.idm.read_only_udm.principal.ip
Value taken from src
src
event.idm.read_only_udm.metadata.event_type
Set to STATUS_UPDATE if src not empty
srcip
principal_ip
Value taken from srcip
spyware_Grayware_Type_label
security_result.detection_fields
Merged from spyware_Grayware_Type_label
suid
event.idm.read_only_udm.principal.user.userid
Value taken from suid
suser
event.idm.read_only_udm.principal.user.user_display_name
Value taken from suser if not starts with {
target
event.idm.read_only_udm.target
Renamed from target
target_hostname_present
target_hostname_present
Set to true
target_machine_id_present
target_machine_id_present
Set to true
target_present
target_present
Set to true
temp_dhost
event.idm.read_only_udm.target.hostname
Value taken from temp_dhost
temp_dhost
target_hostname_present
Set to true
temp_dhost
target_machine_id_present
Set to true
temp_duid
event.idm.read_only_udm.target.user.userid
Value taken from temp_duid after grok
temp_duser
event.idm.read_only_udm.target.user.user_display_name
Value taken from temp_duser
temp_duser
has_target_user
Set to true
threat_probability_label
security_result.detection_fields
Merged from threat_probability_label
tillatelse_label
security_result.detection_fields
Merged from tillatelse_label
type_label
security_result_token.detection_fields
Key set to "Type", value from _metadata.source.type
customer_label
security_result_token.detection_fields
Key set to "Customer", value from _metadata.customer
event.idm.read_only_udm.metadata.vendor_name
Set to "FIREEYE_EMPS"
event.idm.read_only_udm.metadata.product_name
Set to "FIREEYE_EMPS"
Need more help?
Get answers from Community members and Google SecOps professionals.
