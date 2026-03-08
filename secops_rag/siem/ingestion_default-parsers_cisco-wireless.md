# Collect Cisco Wireless LAN Controller (WLC) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/  
**Scraped:** 2026-03-05T09:22:00.006633Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Wireless LAN Controller (WLC) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Wireless LAN Controller (WLC)
logs to Google Security Operations using Bindplane. The parser extracts fields from
the syslog messages, handling both JSON and plain text formats. It uses grok
patterns to identify key fields, including timestamps, severity, and message
content, and then populates the UDM model with extracted data, including
principal and intermediary information when available within the logs.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the Cisco Wireless LAN Controllers
Cisco Wireless LAN Controllers running AireOS 8.8.111.0 or later software
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
Save the file securely on the system where Bindplane will be installed.
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
Configure the BindPlane agent to ingest Syslog and send to Google SecOps
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
udplog
:
# Replace the port and IP address as required
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
log_type
:
'CISCO_WIRELESS'
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
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on Cisco WLC (GUI)
Sign in to the
WLC
web UI.
Go to
Management
>
Logs
>
Config
.
Enter the Bindplane agent IP address in the
Syslog Server IP Address
field.
Click
Add
.
Provide the following configuration details:
Syslog Severity
: Select
Informational
.
Syslog Facility
: Select
Local Use 0
.
Click
Apply
.
Click
Save Configuration
.
UDM mapping table
Log Field
UDM Mapping
Logic
action_data
read_only_udm.security_result.action_details
Directly mapped from the
action_data
field.
data
read_only_udm.metadata.description
Directly mapped from the
data
field after some processing (e.g., removing timestamps, extra characters). Extracted from the timestamp at the beginning of the log message. Various formats are handled by the parser. Determined based on the
mnemonic
and
messageToProcess
fields using complex logic within the
cisco_wireless.include
file. Set to "CISCO_WIRELESS". Concatenation of
facility
,
cisco_severity
, and
mnemonic
fields. Extracted from the log message when available. Set to "CISCO_WIRELESS". Extracted from the
version
field when available. Set to "CISCO". Set to "DHCP" when the event relates to DHCP. Set to "BROADCAST" for broadcast network events. Set to "UDP" for UDP network events. Extracted from the description when available. Extracted from the description when available. Mapped from
wlc_controller
or
hostname
fields, depending on the log format. Extracted from the description or
MessageSourceAddress
when available. Mapped from
wlc_controller
or
hostname
fields, depending on the log format. Extracted from the description or
MessageSourceAddress
when available. Extracted from the description when available. Extracted from the description when available. Created from
SourceModuleName
and
SourceModuleType
fields when available. Mapped from
read_only_udm.principal.user.userid
when the userid looks like an email address. Extracted from the description when available. Extracted from the description when available. Determined based on the event type and description. Determined based on the event type and description. Created from specific fields within the description when available. Extracted from the description when available.  Sometimes combines information from multiple fields. Determined based on the
cisco_severity
field and event type. Derived from the
read_only_udm.security_result.severity
field. A concise summary of the security result, derived from the description and event type. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Set to "SETTING" for setting modification events. Extracted from the description when available.
event_data
read_only_udm.metadata.product_event_type
Directly mapped from the
event_data
field.
event_id
read_only_udm.metadata.product_log_id
Directly mapped from the
event_id
field.
event_ts
read_only_udm.metadata.event_timestamp
Directly mapped from the
event_ts
field.
facility
read_only_udm.metadata.product_event_type
Directly mapped from the
facility
field.
hostname
read_only_udm.principal.hostname
Directly mapped from the
hostname
field.
hostname
read_only_udm.target.hostname
Directly mapped from the
hostname
field.
inter_mac
read_only_udm.intermediary.mac
Directly mapped from the
inter_mac
field.
intermediary_hostname
read_only_udm.intermediary.hostname
Directly mapped from the
intermediary_hostname
field.
kv_data
read_only_udm.principal.resource.attribute.labels
Parsed as key-value pairs and used to populate labels.
log_message
read_only_udm.security_result.description
Directly mapped from the
log_message
field.
MessageSourceAddress
read_only_udm.principal.asset.ip
Directly mapped from the
MessageSourceAddress
field.
MessageSourceAddress
read_only_udm.principal.ip
Directly mapped from the
MessageSourceAddress
field.
messageToProcess
read_only_udm.metadata.description
Directly mapped from the
messageToProcess
field after some processing.
mnemonic
read_only_udm.metadata.event_type
Used in conjunction with other fields to determine the event type.
mnemonic
read_only_udm.metadata.product_event_type
Directly mapped from the
mnemonic
field.
severity_data
read_only_udm.security_result.severity
Mapped from the
severity_data
field after converting it to an enum value.
SourceModuleName
read_only_udm.principal.resource.attribute.labels
Directly mapped from the
SourceModuleName
field.
SourceModuleType
read_only_udm.principal.resource.attribute.labels
Directly mapped from the
SourceModuleType
field.
timestamp
read_only_udm.metadata.event_timestamp
Directly mapped from the
timestamp
field.
version
read_only_udm.metadata.product_version
Directly mapped from the
version
field.
wlc_controller
read_only_udm.principal.hostname
Directly mapped from the
wlc_controller
field.
wlc_controller
read_only_udm.target.hostname
Directly mapped from the
wlc_controller
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
