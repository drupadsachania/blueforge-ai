# Collect IBM Guardium logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardium/  
**Scraped:** 2026-03-05T09:57:03.923608Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect IBM Guardium logs
Supported in:
Google secops
SIEM
This document explains how to ingest IBM Guardium logs to Google Security Operations using Bindplane.
IBM Guardium is a database activity monitoring and data protection platform that provides real-time monitoring, auditing, and protection for databases and file systems. Guardium offers vulnerability assessment, data discovery and classification, database activity monitoring, and compliance reporting capabilities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and IBM Guardium Collector
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the IBM Guardium CLI
IBM Guardium version 9.1 or later for encrypted syslog support (optional)
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
Configure the Bindplane agent to ingest syslog and send to Google SecOps
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
chronicle/guardium
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
GUARDIUM
raw_log_field
:
body
ingestion_labels
:
log_source
:
guardium
service
:
pipelines
:
logs/guardium_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/guardium
Configuration parameters
Replace the following placeholders:
Receiver configuration:
Use
udplog
for UDP syslog (most common for Guardium).
Use
tcplog
for TCP syslog if required.
Listen address
0.0.0.0:514
listens on all interfaces on port 514.
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
: Customer ID from the previous step.
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
: Must be
GUARDIUM
.
ingestion_labels
: Optional labels in YAML format.
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
Configure IBM Guardium syslog forwarding
Configure syslog destination via CLI
To create a syslog destination for events on IBM Guardium, you must log in to the command-line interface and define the IP address for the Bindplane agent host.
Using SSH, log in to IBM Guardium Collector as the CLI user.
Type the following commands to configure the syslog destination:
For UDP syslog (recommended):
store
remotelog
add
non_encrypted
daemon.all
BINDPLANE_AGENT_IP
udp
For TCP syslog:
store
remotelog
add
non_encrypted
daemon.all
BINDPLANE_AGENT_IP:514
tcp
For specific severity levels:
store
remotelog
add
non_encrypted
daemon.alert
BINDPLANE_AGENT_IP
udp
store
remotelog
add
non_encrypted
daemon.err
BINDPLANE_AGENT_IP
udp
store
remotelog
add
non_encrypted
daemon.warning
BINDPLANE_AGENT_IP
udp
Replace
BINDPLANE_AGENT_IP
with the IP address of the host where Bindplane agent is installed.
Verify the configuration by running:
show
remotelog
The output should display your configured remote syslog destination.
Configure encrypted syslog (optional)
If you require encrypted syslog forwarding, IBM Guardium version 9.1 and above supports TLS encryption over TCP.
Obtain the public certificate in PEM format from the certificate authority used by your remote syslog receiver.
Log in to the CLI on the Guardium Collector.
Type the following command:
store
remotelog
add
encrypted
daemon.all
BINDPLANE_AGENT_IP:6514
tcp
When prompted, paste the CA certificate in PEM format, including the BEGIN and END lines, then press
Ctrl+D
.
Guardium stores the certificate as
/etc/pki/rsyslog/ca.pem
.
Configure message template (optional)
Guardium supports multiple message formats including CEF (Common Event Format) and LEEF (Log Event Extended Format). The default format is suitable for most deployments.
To customize the message template:
Sign in to the Guardium appliance GUI as a user with admin privileges.
Go to
Administration Console
>
Configuration
>
Global Profile
.
In the
Message Template
section, edit the template with your desired format.
Click
Save
.
Configure policy to send alerts to syslog
Policies in IBM Guardium are responsible for reacting to events and forwarding the event information to the remote syslog receiver.
Configure policy alert action
Sign in to the Guardium appliance GUI.
Click the
Tools
tab.
From the left navigation, select
Policy Builder
.
From the
Policy Finder
pane, select an existing policy and click
Edit Rules
.
Click
Edit this Rule individually
.
The
Access Rule Definition
is displayed.
Click
Add Action
.
From the
Action
list, select one of the following alert types:
Alert Per Match
: A notification is provided for every policy violation.
Alert Daily
: A notification is provided the first time a policy violation occurs that day.
Alert Once Per Session
: A notification is provided per policy violation for unique session.
Alert Per Time Granularity
: A notification is provided per your selected timeframe.
From the
Message Template
list, select the required template or keep
Default
.
From
Notification Type
, select
SYSLOG
.
Click
Add
, then click
Apply
.
Click
Save
.
Repeat this process for all rules within the policy that you want to forward to Google SecOps.
Install the policy
Any new or edited policy in IBM Guardium must be installed before the updated alert actions or rule changes can occur.
Click the
Administration Console
tab.
From the left navigation, select
Configuration
>
Policy Installation
.
From the
Policy Installer
pane, select the policy that you modified in the previous step.
From the drop-down list, select
Install and Override
.
A confirmation is displayed to install the policy to all Inspection Engines.
Click
OK
.
UDM mapping table
Log Field
UDM Mapping
Logic
deviceNtDomain
about.administrative_domain
Administrative domain of the about entity
deviceExternalId
about.asset.asset_id
Asset identifier
filePath, fileHash
about.file.full_path
Full path of the file
_hash, fileHash
about.file.sha256
SHA256 hash of the file
fsize
about.file.size
Size of the file
dvchost
about.hostname
Hostname of the about entity
dvc
about.ip
IP address of the about entity
smac, dmac, dvcmac
about.mac
MAC address of the about entity
deviceProcessName, Subject, Emne, Path
about.process.command_line
Command line of the process
dvcpid
about.process.pid
Process ID
filePermission
about.resource.attribute.permissions
Permissions associated with the resource
extensions.auth.type
Authentication type
sender_ip
intermediary.ip
IP address of the intermediary
intermediary
Intermediary entity details
Received, Generated, timestamp
metadata.collected_timestamp
Timestamp when the event was collected
msg, signature_name
metadata.description
Description of the event
metadata.event_type
Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)
device_event_class_id, event_name, eventType
metadata.product_event_type
Product-specific event type
externalId
metadata.product_log_id
Product log identifier
metadata.product_version
Version of the product
network.application_protocol
Application protocol used in the network connection
deviceDirection
network.direction
Direction of the network traffic
requestMethod
network.http.method
HTTP method used in the request
requestClientApplication
network.http.user_agent
User agent string from the HTTP request
proto
network.ip_protocol
IP protocol used
in
network.received_bytes
Number of bytes received
out
network.sent_bytes
Number of bytes sent
session_id
network.session_id
Session identifier for the network connection
sntdom, Domain, Domene
principal.administrative_domain
Administrative domain of the principal
sourceServiceName, source_program
principal.application
Application associated with the principal
prin_host, Device_name, Enhetsnavn, shost, principal_hostname, client_hostname
principal.asset.hostname
Hostname of the principal asset
sender_ip, src_ip, src, principal_ip, client_ip
principal.asset.ip
IP address of the principal asset
Group_name, Gruppenavn
principal.group.group_display_name
Display name of the principal group
prin_host, Device_name, Enhetsnavn, shost, principal_hostname, client_hostname
principal.hostname
Hostname of the principal
sender_ip, src_ip, src, principal_ip, client_ip
principal.ip
IP address of the principal
smac
principal.mac
MAC address of the principal
sourceTranslatedAddress
principal.nat_ip
NAT IP address of the principal
sourceTranslatedPort
principal.nat_port
NAT port of the principal
spt, client_port
principal.port
Port used by the principal
sproc
principal.process.command_line
Command line of the principal process
spid
principal.process.pid
Process ID of the principal
spriv
principal.user.attribute.roles
Roles associated with the principal user
suser, usrName, CustomerName
principal.user.user_display_name
Display name of the principal user
dbUser, usrName, db_user, os_user, suid, db_username
principal.user.userid
User ID of the principal
security_result
Security result details
security_result.action
Action taken in the security result
act, Action_Taken
security_result.action_details
Details of the action taken
cat
security_result.category_details
Category details of the security result
msg_data_2, alert_description, Type, Scan_Type
security_result.description
Description of the security result
operation_label, operasjon_label, permission_label, tillatelse_label, infection_channel_label, spyware_Grayware_Type_label, threat_probability_label
security_result.detection_fields
Fields used for detection in the security result
mwProfile, alert_name
security_result.rule_name
Name of the rule that triggered the security result
severity, event_severity
security_result.severity
Severity level of the security result
reason, ruleDesc, appcategory, Result
security_result.summary
Summary of the security result
Spyware, Virus_Malware_Name, Unknown_Threat
security_result.threat_name
Name of the threat detected
oldFilePath
src.file.full_path
Full path of the source file
oldFileSize
src.file.size
Size of the source file
oldFilePermission
src.resource.attribute.permissions
Permissions of the source resource
os_user
src.user.userid
User ID of the source user
dntdom
target.administrative_domain
Administrative domain of the target
destinationServiceName, service_name
target.application
Application associated with the target
prin_host, dest_host, server_hostname
target.asset.hostname
Hostname of the target asset
dst_ip, dest_ip, server_ip, IPv6_Address
target.asset.ip
IP address of the target asset
temp_dhost, dest_host, server_hostname
target.hostname
Hostname of the target
dst_ip, dst, dest_ip, server_ip, IPv6_Address
target.ip
IP address of the target
dmac
target.mac
MAC address of the target
destinationTranslatedAddress
target.nat_ip
NAT IP address of the target
destinationTranslatedPort
target.nat_port
NAT port of the target
dpt, dstPort, dest_port, server_port
target.port
Port used by the target
dproc, full_sql
target.process.command_line
Command line of the target process
File_name, Object, Objekt, Infected_Resource
target.process.file.full_path
Full path of the target process file
dpid, full_sql_id
target.process.pid
Process ID of the target
session_start
target.resource.attribute.creation_time
Creation time of the target resource
additional_environment_name, additional_db_protocol_version, additional_dbProtocolVersion, additional_operation_name, additional_signature_id, resource_Type_label
target.resource.attribute.labels
Labels associated with the target resource
session_end
target.resource.attribute.last_update_time
Last update time of the target resource
db_name, database_name
target.resource.name
Name of the target resource
db_type, server_type
target.resource.resource_subtype
Subtype of the target resource
target.resource.resource_type
Type of the target resource
request
target.url
URL associated with the target
dpriv, roles
target.user.attribute.roles
Roles associated with the target user
temp_duser, CustomerName
target.user.user_display_name
Display name of the target user
temp_duid, User, Bruker, db_username
target.user.userid
User ID of the target
metadata.product_name
Name of the product
metadata.vendor_name
Name of the vendor
Need more help?
Get answers from Community members and Google SecOps professionals.
