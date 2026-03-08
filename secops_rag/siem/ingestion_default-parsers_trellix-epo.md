# Collect Trellix ePO logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-epo/  
**Scraped:** 2026-03-05T09:29:20.826539Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trellix ePO logs
Supported in:
Google secops
SIEM
This document explains how to ingest Trellix (formerly McAfee) ePolicy (ePO) Orchestrator
logs to Google Security Operations using Bindplane. The parser uses grok patterns
and XML filtering to extract fields from both XML and CSV formatted logs,
normalizes IP and MAC addresses, and maps the extracted data to the Unified Data
Model (UDM). The parser also handles specific event types and security actions,
setting appropriate UDM fields based on the log content.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to McAfee EPO
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
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
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
For additional installation options, consult the
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:6514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
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
'MCAFEE_EPO'
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
Restart BindPlane Agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure (Trellix) McAfee ePO Syslog Server
Sign in to the
(Trellix) McAfee EPO
.
Go to
Menu
>
Configuration
>
Registered Servers
.
Click
New Server
.
Select
Syslog Server
, specify a unique name, then click
Next
.
Provide the following configuration details:
Server name
: Enter the Bindplane agent IP address.
TCP port number
: Enter the Bindplane agent TCP port (default is
6514
).
Enable event forwarding
: Select to enable event forwarding from
Agent Handler
to this syslog server.
Click
Test Connection
to verify the connection to Bindplane.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
AgentGUID
principal.asset.id
The Agent GUID is directly mapped to the asset ID in the UDM.
Analyzer
idm.read_only_udm.security_result.detection_fields.value
Analyzer value is mapped as a detection field with key "DetectingProductID".
AnalyzerContentCreationDate
idm.read_only_udm.additional.fields.value.string_value
Analyzer content creation date is mapped to additional fields with key "Analyzer Content Creation Date".
AnalyzerContentVersion
idm.read_only_udm.additional.fields.value.string_value
Analyzer content version is mapped to additional fields with key "Analyzer Content Version".
AnalyzerDATVersion
idm.read_only_udm.security_result.detection_fields.value
Analyzer DAT version is mapped as a detection field with key "datversion".
AnalyzerDetectionMethod
idm.read_only_udm.security_result.detection_fields.value
Analyzer detection method is mapped as a detection field with key "scantype".
AnalyzerEngineVersion
idm.read_only_udm.security_result.detection_fields.value
Analyzer engine version is mapped as a detection field with key "DetectingAgentVersion".
AnalyzerHostName
idm.read_only_udm.intermediary.hostname
Analyzer hostname is mapped to intermediary hostname.
AnalyzerName
idm.read_only_udm.security_result.detection_fields.value
Analyzer name is mapped as a detection field with key "productname".
AnalyzerRuleID
idm.read_only_udm.additional.fields.value.string_value
Analyzer rule ID is mapped to additional fields with key "Analyzer Rule Id".
AnalyzerRuleName
idm.read_only_udm.security_result.rule_name
Analyzer rule name is directly mapped to the security result rule name.
AnalyzerVersion
idm.read_only_udm.security_result.detection_fields.value
Analyzer version is mapped as a detection field with key "productversion".
BladeName
idm.read_only_udm.additional.fields.value.string_value
Blade name is mapped to additional fields with key "BladeName".
DetectedUTC
metadata.event_timestamp
Detected UTC time is parsed and mapped to the event timestamp in metadata.
DurationBeforeDetection
idm.read_only_udm.additional.fields.value.string_value
Duration before detection is mapped to additional fields with key "DurationBeforeDetection".
EventID
idm.read_only_udm.security_result.rule_id
Event ID is mapped to the security result rule ID.
GMTTime
metadata.event_timestamp
GMT time is parsed and mapped to the event timestamp in metadata.
IPAddress
principal.ip
IP address is directly mapped to principal IP.
MachineName
principal.hostname
Machine name is directly mapped to principal hostname.
NaturalLangDescription
idm.read_only_udm.additional.fields.value.string_value
Natural language description is mapped to additional fields with key "NaturalLangDescription".
OSName
principal.platform
OS name is normalized and mapped to principal platform (WINDOWS, MAC, LINUX, or UNKNOWN_PLATFORM).
ProductName
metadata.product_name
Product name is directly mapped to the product name in metadata.
ProductVersion
metadata.product_version
Product version is directly mapped to the product version in metadata.
RawMACAddress
principal.mac
Raw MAC address is parsed and mapped to principal MAC.
Severity
idm.read_only_udm.security_result.severity
Severity is mapped to security result severity (HIGH, MEDIUM, or LOW).
SourceIPV4
idm.read_only_udm.src.ip
Source IPv4 address is mapped to source IP.
SourceProcessName
principal.application
Source process name is directly mapped to principal application.
SourceUserName
principal.user.user_display_name
Source username is directly mapped to principal user display name.
TargetFileName
target.process.file.full_path
Target filename is mapped to target file full path.
TargetHostName
target.hostname
Target host name is mapped to target hostname.
TargetPort
target.port
Target port is mapped to target port.
TargetProtocol
network.ip_protocol
Target protocol is mapped to network IP protocol.
TargetUserName
target.user.user_display_name
Target username is mapped to target user display name.
ThreatActionTaken
security_result.action_details
Threat action taken is mapped to security result action details.
ThreatCategory
security_result.category_details
Threat category is mapped to security result category details.
ThreatEventID
security_result.rule_id
Threat event ID is mapped to security result rule ID.
ThreatHandled
security_result.detection_fields.value
Threat handled status is mapped as a detection field with key "ThreatHandled".
ThreatName
security_result.threat_name
Threat name is directly mapped to security result threat name.
ThreatSeverity
security_result.severity
Threat severity is mapped to security result severity (HIGH, MEDIUM, or LOW).
ThreatType
security_result.threat_id
Threat type is mapped to security result threat ID.
UserName
principal.user.user_display_name
User name is mapped to principal user display name.
collection_time
metadata.collected_timestamp
Collection time is mapped to collected timestamp in metadata.
log_type
metadata.log_type
Log type is directly mapped to metadata log type.
Need more help?
Get answers from Community members and Google SecOps professionals.
