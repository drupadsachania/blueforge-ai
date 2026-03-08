# Collect Fortra Powertech SIEM Agent logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortra-powertech-siem-agent/  
**Scraped:** 2026-03-05T09:24:56.988818Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortra Powertech SIEM Agent logs
Supported in:
Google secops
SIEM
This guide explains how you can ingest Fortra Powertech SIEM Agent for IBM i logs to Google Security Operations using Bindplane agent.
Powertech SIEM Agent for IBM i (formerly Powertech Interact) monitors IBM i journals and message queues for critical system messages and audit entries, transmits the messages using UDP, TCP, TLS, message queue, or stream file (IFS), and formats the MSG portion of the syslog packet in compliance with Micro Focus ArcSight Common Event Format (CEF) v25.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Windows Server 2016 or later, or Linux host with systemd.
Network connectivity between Bindplane agent and the IBM i system running Powertech SIEM Agent.
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
Privileged access to the IBM i system with authority to configure Powertech SIEM Agent (user profile with *ALLOBJ special authority or member of PTADMIN authorization list).
Powertech SIEM Agent for IBM i installed and licensed on the IBM i system.
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
chronicle/powertech_siem
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
FORTRA_POWERTECH_SIEM_AGENT
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
logs/powertech_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/powertech_siem
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on. Use
0.0.0.0:514
to listen on all interfaces on port 514, or change the port to
1514
or another value if port 514 requires root privileges or is already in use.
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
: Replace with your Google SecOps customer ID.
endpoint
: Regional endpoint URL. Use the appropriate endpoint for your Google SecOps instance:
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
ingestion_labels
: Optional labels in YAML format (for example,
env: production
,
source: ibm_i
).
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
Configure Powertech SIEM Agent syslog forwarding
On the IBM i command line, enter POWERTECH to open the Powertech Main Menu, then choose Option 6 to open the SIEM Agent Main Menu.
Configure the syslog format
From the SIEM Agent Main Menu, choose option 2 to open the Work with Formats panel. CEF, JSON, LEEF, MODERN, and SYSLOG Formats are included by default.
Type 2 next to SYSLOG and press Enter.
In the Message Style field, type *SYSLOG.
In the Header specification field type RFC3164.
Ensure that Use Header Format Compatibility is set to 'Y' and save the configuration.
Press F3 twice to return to the Main Menu.
Create a network output
From the Main Menu, choose option 3 Work with Outputs, then press F6 to create a new output.
Enter the following options:
Name
: CHRONICLE (or a descriptive name)
Description
: Chronicle Bindplane Output
Active
: 1
Format
: SYSLOG
Type
: *NETWORK
Press Enter.
On the subsequent screen, enter these options:
Location
: Enter the IP address of the machine on which the Bindplane agent is installed
Port
: 514 (or the port configured in the Bindplane agent)
Protocol
: UDP
Press Enter to save changes, then press F12 to close the window.
Attach the output to event sources
Choose option 1 Work with Event Sources, then type 2 next to AUDIT and press Enter.
Press F8 Maintain Outputs, then press F6 Attach to attach the recently created output. Type 1 next to CHRONICLE (or your output name) and press Enter.
Press F3 to return to the Main Menu.
Activate event descriptions
From the SIEM Agent Main Menu, choose option 1, then enter 9 for an Event Source. The Work with Event Descriptions panel appears. Use option 6 to activate the events you would like to process.
Commit configuration changes
From the Main Menu, choose option 82,
Work with Utilities
, then select option 1,
Commit configuration changes
.
Start SIEM Agent monitoring
If SIEM Agent is not already running, start the monitor jobs:
From the IBM i command line, enter:
CALL PTSTARTUP
These commands start the required Central Administration and SIEM Agent monitor jobs in the PTWRKMGT subsystem.
Verify logs are being sent
Check that logs are arriving at the Bindplane agent by reviewing the Bindplane agent logs (see the restart section above for log locations).
Verify logs are appearing in Google SecOps console (allow 5 to 10 minutes for initial ingestion).
Optionally, assign a message queue to log all messages sent by SIEM Agent to confirm which messages have been sent.
UDM mapping table
Log field
UDM mapping
Logic
principal_ip
principal.ip
The IP address of the principal.
dst_ip
target.ip
The IP address of the target.
sourceTranslatedAddress
principal.nat_ip
The NAT IP address of the principal.
destinationTranslatedAddress
target.nat_ip
The NAT IP address of the target.
dvc
about.ip
The IP address of the asset.
deviceTranslatedAddress
about.nat_ip
The NAT IP address of the asset.
smac
principal.mac
The MAC address of the principal.
dmac
target.mac
The MAC address of the target.
dvcmac
about.mac
The MAC address of the asset.
spriv
principal.user.attribute.roles
The roles associated with the principal user.
dpriv
target.user.attribute.roles
The roles associated with the target user.
oldFilePermission
src.resource.attribute.permissions
The permissions of the source resource.
filePermission
about.resource.attribute.permissions
The permissions of the resource.
cat
security_result.category_details
Additional details about the security result category.
device_vendor, device_product, deviceExternalId
about.asset.asset_id
The unique identifier for the asset.
out
network.sent_bytes
The number of bytes sent in the network connection.
in
network.received_bytes
The number of bytes received in the network connection.
fsize
about.file.size
The size of the file.
oldFileSize
src.file.size
The size of the source file.
destinationTranslatedPort
target.nat_port
The NAT port of the target.
dpt
target.port
The port number of the target.
sourceTranslatedPort
principal.nat_port
The NAT port of the principal.
spt
principal.port
The port number of the principal.
rt
metadata.event_timestamp
The timestamp when the event occurred.
severity
security_result.severity
The severity level of the security result.
app_protocol_src
network.application_protocol
The application protocol used in the network connection.
proto
network.ip_protocol
The IP protocol used in the network connection.
deviceDirection
network.direction
The direction of the network traffic.
act
security_result.action
The action taken by the security system.
outcome, categoryOutcome, cs2
security_result.action
The action taken by the security system.
msg_data_2
security_result.description
A description of the security result.
msg
metadata.description
A description of the event.
destinationServiceName
target.application
The application associated with the target.
dntdom
target.administrative_domain
The administrative domain of the target.
oldFilePath
src.file.full_path
The full path of the source file.
requestClientApplication
network.http.user_agent
The user agent string from the HTTP request.
requestMethod
network.http.method
The HTTP method used in the request.
filePath
about.file.full_path
The full path of the file.
dvchost
about.hostname
The hostname of the asset.
deviceNtDomain
about.administrative_domain
The administrative domain of the asset.
dvcpid
about.process.pid
The process ID of the asset.
deviceProcessName
about.process.command_line
The command line of the process on the asset.
_hash
about.file.sha256
The SHA256 hash of the file.
externalId
metadata.product_log_id
The product-specific log identifier.
security_result.action_details
security_result.action_details
Additional details about the security action.
device_version
metadata.product_version
The version of the product that generated the event.
temp_dhost
target.hostname
The hostname of the target.
request
target.url
The URL associated with the target.
temp_duser
target.user.user_display_name
The display name of the target user.
temp_duid
target.user.userid
The user ID of the target user.
Device_name
principal.hostname
The hostname of the principal.
Enhetsnavn
principal.hostname
The hostname of the principal.
Domain
principal.administrative_domain
The administrative domain of the principal.
Domene
principal.administrative_domain
The administrative domain of the principal.
Group_name
principal.group.group_display_name
The display name of the principal group.
Gruppenavn
principal.group.group_display_name
The display name of the principal group.
Received, Mottatt
metadata.collected_timestamp
The timestamp when the event was collected.
Generated, Generert
metadata.event_timestamp
The timestamp when the event occurred.
Subject
about.process.command_line
The command line of the process.
Emne
about.process.command_line
The command line of the process.
Path
about.process.command_line
The command line of the process.
Type
security_result.description
A description of the security result.
Scan_Type
security_result.description
A description of the security result.
User
target.user.userid
The user ID of the target user.
Bruker
target.user.userid
The user ID of the target user.
CustomerName
target.user.user_display_name
The display name of the target user.
File_name, Object, Objekt, Infected_Resource
target.process.file.full_path
The full path of the file associated with the target process.
Action_Taken
security_result.action_details
Additional details about the security action.
Spyware, Virus_Malware_Name, Unknown_Threat
security_result.threat_name
The name of the threat detected.
shost
principal.hostname
The hostname of the principal.
shost
principal.ip
The IP address of the principal.
sntdom
principal.administrative_domain
The administrative domain of the principal.
sourceServiceName
principal.application
The application associated with the principal.
spid
principal.process.pid
The process ID of the principal.
sproc
principal.process.command_line
The command line of the principal process.
suid
principal.user.userid
The user ID of the principal user.
suser
principal.user.user_display_name
The display name of the principal user.
dpid
target.process.pid
The process ID of the target process.
dproc
target.process.command_line
The command line of the target process.
reason
security_result.summary
A summary of the security result.
event_name, device_event_class_id
metadata.product_event_type
The product-specific event type.
fileHash
about.file.sha256
The SHA256 hash of the file.
about
about
Additional information about the event.
mwProfile
security_result.rule_name
The name of the rule that triggered the security result.
appcategory
security_result.summary
A summary of the security result.
Result
security_result.summary
A summary of the security result.
eventid
additional.fields
Additional fields for the event.
eventId
additional.fields
Additional fields for the event.
devicePayloadId
additional.fields
Additional fields for the event.
fname
additional.fields
Additional fields for the event.
cs1, cs1Label
additional.fields
Additional fields for the event.
cs2, cs2Label
additional.fields
Additional fields for the event.
cs3, cs3Label
additional.fields
Additional fields for the event.
cs4, cs4Label
additional.fields
Additional fields for the event.
cs5, cs5Label
additional.fields
Additional fields for the event.
cs6, cs6Label
additional.fields
Additional fields for the event.
cs7, cs7Label
additional.fields
Additional fields for the event.
flexString1, flexString1Label
additional.fields
Additional fields for the event.
cn1, cn1Label
additional.fields
Additional fields for the event.
cn2, cn2Label
additional.fields
Additional fields for the event.
cn3, cn3Label
additional.fields
Additional fields for the event.
cfp1, cfp1Label
additional.fields
Additional fields for the event.
cfp2, cfp2Label
additional.fields
Additional fields for the event.
cfp3, cfp3Label
additional.fields
Additional fields for the event.
cfp4, cfp4Label
additional.fields
Additional fields for the event.
Operation
security_result.detection_fields
Fields used for threat detection.
Operasjon
security_result.detection_fields
Fields used for threat detection.
Permission
security_result.detection_fields
Fields used for threat detection.
Tillatelse
security_result.detection_fields
Fields used for threat detection.
Infection_Channel
security_result.detection_fields
Fields used for threat detection.
IPv6_Address
target.ip
The IP address of the target.
Resource_Type
target.resource.attribute.labels
Labels for the target resource attributes.
Spyware_Grayware_Type
security_result.detection_fields
Fields used for threat detection.
Threat_Probability
security_result.detection_fields
Fields used for threat detection.
security_result
security_result
The security result of the event.
host
principal.hostname
The hostname of the principal.
failure
metadata.description
A description of the event.
changed
metadata.description
A description of the event.
log_version
additional.fields
Additional fields for the event.
cnt
additional.fields
Additional fields for the event.
fileType
target.file.mime_type
The MIME type of the target file.
fname
target.file.names
The names of the target files.
ip
principal.ip
The IP address of the principal.
metadata.event_type
metadata.event_type
The type of event.
principal_hostname
principal.asset.hostname
The hostname of the principal asset.
principal_asset_hostname
principal.asset.hostname
The hostname of the principal asset.
target_hostname
target.asset.hostname
The hostname of the target asset.
target_asset_hostname
target.asset.hostname
The hostname of the target asset.
device_vendor
metadata.vendor_name
The vendor name of the product.
device_product
metadata.product_name
The product name.
Need more help?
Get answers from Community members and Google SecOps professionals.
