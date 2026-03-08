# Collect CyberArk logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark/  
**Scraped:** 2026-03-05T09:53:56.450662Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CyberArk logs
Supported in:
Google secops
SIEM
This document explains how to ingest CyberArk logs into Google Security Operations using the Bindplane agent.
CyberArk Privileged Access Manager (PAM) is an enterprise-grade privileged access security solution that secures, manages, and monitors privileged accounts and credentials across on-premises and cloud environments. It provides credential vaulting, session isolation and monitoring, threat detection through Privileged Threat Analytics (PTA), and comprehensive audit logging of all privileged activities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and the CyberArk Vault Server
If running behind a proxy, ensure firewall ports are open as per the Bindplane agent requirements
Administrative access to the CyberArk Vault Server (access to the
Server\Conf
installation folder)
CyberArk Vault version 10.0 or later
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
Configure the Bindplane agent to ingest syslog and send it to Google SecOps
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
chronicle/cyberark
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
CYBERARK
raw_log_field
:
body
service
:
pipelines
:
logs/cyberark_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/cyberark
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on:
0.0.0.0:514
to listen on all interfaces on port 514 (requires root on Linux)
0.0.0.0:1514
to listen on an unprivileged port (recommended for Linux non-root)
Receiver type options:
udplog
for UDP syslog (default for CyberArk Vault)
tcplog
for TCP syslog
Use
tcplog
if CyberArk Vault is configured with
SyslogServerProtocol=TCP
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
Configure CyberArk syslog forwarding
CyberArk Vault sends audit events in CEF (Common Event Format) via syslog. The Vault Server converts XML audit records to CEF messages using an XSL translator file, then forwards them to the Bindplane agent.
Configure the Vault Server to send syslog
Sign in to the CyberArk Vault Server host machine with administrator privileges.
Navigate to the CyberArk Vault Server installation folder 
(for example, `C:\Program Files (x86)\PrivateArk\Server\Conf`).
Open the
DBParm.ini
file in a text editor.
Copy the
[SYSLOG]
section from the
DBParm.sample.ini
file (located in the same folder) and paste it at the bottom of
DBParm.ini
.
Configure the following syslog parameters in the
[SYSLOG]
section:
[SYSLOG]
SyslogServerIP=<BINDPLANE_AGENT_IP>
SyslogServerPort=514
SyslogServerProtocol=UDP
UseLegacySyslogFormat=No
SyslogTranslatorFile=Syslog\Arcsight.sample.xsl
SyslogMessageCodeFilter=0-999
Replace the following values:
SyslogServerIP
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
SyslogServerPort
: Enter the port matching the Bindplane agent
listen_address
(for example,
514
).
SyslogServerProtocol
: Select the protocol:
UDP
for UDP syslog (default)
TCP
for TCP syslog
SyslogTranslatorFile
: Enter the XSL translator file for CEF format:
Syslog\Arcsight.sample.xsl
for standard CEF output (recommended)
SyslogMessageCodeFilter
: Enter the message codes to forward:
0-999
to forward all events
Specify individual codes or ranges (for example,
1,2,3,5-10,30
) to filter specific events
UseLegacySyslogFormat
: Set to
No
for RFC 5424 format.
Save the
DBParm.ini
file.
Restart the
PrivateArk Server
service:
Open
Windows Services
(
services.msc
).
Locate the
CyberArk Vault Disaster Recovery
service and stop it (if running).
Locate the
PrivateArk Server
service.
Right-click and select
Restart
.
Start the
CyberArk Vault Disaster Recovery
service again (if applicable).
Forward syslog to multiple destinations
To forward Vault syslog events to both the Bindplane agent and other destinations (for example, PTA), specify multiple IP addresses and translator files separated by commas:
SyslogServerIP=<BINDPLANE_AGENT_IP>,<PTA_SERVER_IP>
SyslogTranslatorFile=Syslog\Arcsight.sample.xsl,Syslog\PTA.xsl
Configure Privileged Threat Analytics (PTA) syslog forwarding (optional)
If you also want to forward PTA security alerts to Google SecOps, configure PTA SIEM integration:
Sign in to the
PVWA
(Password Vault Web Access) console.
Go to
Administration
>
Configuration Options
>
Privileged Threat Analytics
.
In the
SIEM
section, configure the following:
Syslog Server IP
: Enter the IP address of the Bindplane agent host.
Syslog Server Port
: Enter the port matching the Bindplane agent configuration (for example,
514
).
Protocol
: Select
UDP
or
TCP
to match the Bindplane agent receiver.
Format
: Select
CEF
.
Click
Save
.
Available XSL translator files
The
Syslog
subfolder in the CyberArk Server installation folder contains sample XSL translator files:
Translator File
Format
Description
Arcsight.sample.xsl
CEF
Standard CEF format (recommended for Google SecOps)
SplunkCIM.xsl
CIM
Splunk Common Information Model format
PTA.xsl
Custom
Format for forwarding to CyberArk PTA
XSIAM.xsl
CEF
Palo Alto Cortex XSIAM format
Verify syslog forwarding
After restarting the PrivateArk Server service, perform a test action in the Vault (for example, retrieve a password or sign in to PVWA).
Check the Bindplane agent logs for incoming syslog messages:
Linux
:
sudo journalctl -u observiq-otel-collector -f
Windows
:
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Verify that CEF-formatted messages appear in the logs, for example:
CEF:0|Cyber-Ark|Vault|10.0|22|CPM password retrieved|5|suser=Administrator src=10.0.0.1 fname=Root\operating system-server1-admin
UDM mapping table
Log Field
UDM Mapping
Logic
RequestId_label
additional.fields
Mapped as key-value pair
Category_label
additional.fields
Mapped as key-value pair
ExtraDetails_label
additional.fields
Mapped as key-value pair
CAPolicy_label
additional.fields
Mapped as key-value pair
line_number_label
additional.fields
Mapped as key-value pair
pasvc_action_label
additional.fields
Mapped as key-value pair
control_socket_label
additional.fields
Mapped as key-value pair
data_socket_label
additional.fields
Mapped as key-value pair
timeout_label
additional.fields
Mapped as key-value pair
vault_name_label
additional.fields
Mapped as key-value pair
class_name_label
additional.fields
Mapped as key-value pair
status_label
additional.fields
Mapped as key-value pair
Publisher_Event
additional.fields
Mapped as key-value pair
Last_Event
additional.fields
Mapped as key-value pair
Total_Events
additional.fields
Mapped as key-value pair
cs1_var
additional.fields
Mapped as key-value pair
cs3_var
additional.fields
Mapped as key-value pair
app_var
additional.fields
Mapped as key-value pair
reason_var
additional.fields
Mapped as key-value pair
cs5_var
additional.fields
Mapped as key-value pair
cs4_var
additional.fields
Mapped as key-value pair
_auth_mechanism
extensions.auth.mechanism
Directly merged
dvc
intermediary.ip
If value matches IP address pattern
EventName
metadata.description
If process does not match exe pattern
act
metadata.description
If fname is empty
EventMessage
metadata.description
If act is empty
LastEventDate
metadata.event_timestamp
Converted using ISO8601 or yyyy-MM-ddTHH:mm:ss format
_temp_datetime
metadata.event_timestamp
Converted using dd/MM/yyyy HH:mm:ss format
datetime
metadata.event_timestamp
Converted using ISO8601 or MMM d HH:mm:ss format
_event_type
metadata.event_type
Directly renamed
name
metadata.event_type
Set based on conditions: FILE_CREATION for "Store File", USER_LOGIN for "Logon", NETWORK_CONNECTION if has_principal and has_target, FILE_UNCATEGORIZED if has_target_file_details, PROCESS_UNCATEGORIZED if has_target_process_details, STATUS_UPDATE if has_principal only, NETWORK_UNCATEGORIZED if app_error and has_principal and has_target, otherwise GENERIC_EVENT
EventType
metadata.product_event_type
Directly mapped
signature_id, name
metadata.product_event_type
Concatenated from signature_id and name
LastEventID
metadata.product_log_id
Converted to string
tid
metadata.product_log_id
Directly mapped
product
metadata.product_name
Directly renamed
version
metadata.product_version
Directly renamed
vendor
metadata.vendor_name
Directly renamed
host
observer.hostname
Directly mapped
LastEventUserName
principal.administrative_domain
Extracted using grok pattern domain\user
ApplicationType
principal.application
Directly mapped
shost
principal.asset.hostname
If value does not match IP address pattern
shost
principal.asset.hostname
Fallback if dhost is empty
shost
principal.asset.ip
If value matches IP address pattern
src
principal.asset.ip
Directly mapped
ip_address
principal.asset.ip
Directly mapped
shost
principal.asset.ip
Fallback if dhost is empty
shost
principal.ip
If value matches IP address pattern, merged
src
principal.ip
Directly merged
ip_address
principal.ip
Directly merged
Location
principal.location.name
Directly mapped
LastEventSourceName
principal.platform
Set to WINDOWS if value matches Windows pattern
EventName
principal.process.command_line
If process matches exe pattern
LastEventPackageName
principal.resource.name
If value is not EventName
ApplicationType
principal.user.attribute.roles
Set to ADMINISTRATOR if value equals AdminTask
LastEventUserName
principal.user.user_display_name
User portion extracted using grok pattern domain\user
user_name
principal.user.user_display_name
Directly mapped
SourceUser
principal.user.userid
Directly mapped
suser
principal.user.userid
If event is not USER_ type
usrName
principal.user.userid
Directly mapped
_action
security_result.action
Directly merged
name
security_result.action
Set to BLOCK if value starts with "Failure" or "Failed", otherwise ALLOW
msg
security_result.description
Directly mapped
msg, reason
security_result.description
Concatenated from msg and reason if failure condition
_sec_result_description
security_result.description
Directly mapped
PolicyName
security_result.rule_name
Directly mapped
cs2
security_result.rule_name
Directly mapped
severity
security_result.severity
Set to LOW if value <= 5, MEDIUM if value <= 8, HIGH otherwise
sev
security_result.severity
Directly mapped
sev
security_result.severity_details
Directly mapped
Reason
security_result.summary
Directly mapped
name
security_result.summary
Directly mapped
dhost
target.asset.hostname
If value does not match IP address pattern
shost
target.asset.hostname
Fallback if dhost is empty
dhost
target.asset.ip
If value matches IP address pattern
GatewayStation
target.asset.ip
Directly mapped
shost
target.asset.ip
Fallback if dhost is empty
FileQualifier
target.asset_id
Prefixed with "ASSET ID:" and converted to string
File
target.file.full_path
Directly mapped
file_path
target.file.full_path
Directly mapped
LastEventSourceName
target.file.full_path
If value starts with "C:"
fname
target.file.full_path
Directly mapped
Hash
target.file.sha1
"SHA1##" prefix removed and value lowercased, if SHA1 type
GatewayStation
target.ip
Directly merged
pid
target.process.pid
Converted to string
Safe
target.resource.name
Directly mapped
user_name
target.user.user_display_name
Directly mapped
TargetUser
target.user.userid
Directly mapped
duser
target.user.userid
Directly mapped
suser
target.user.userid
If event is USER_ type
Need more help?
Get answers from Community members and Google SecOps professionals.
