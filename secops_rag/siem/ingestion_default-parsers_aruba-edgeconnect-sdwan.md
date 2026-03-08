# Collect Aruba EdgeConnect SD-WAN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-edgeconnect-sdwan/  
**Scraped:** 2026-03-05T09:19:12.657319Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Aruba EdgeConnect SD-WAN logs
Supported in:
Google secops
SIEM
This document explains how to ingest Aruba EdgeConnect SD-WAN logs to
Google Security Operations using Bindplane. The parser extracts fields from syslog
messages, handling both key-value and unstructured formats. It then maps these
extracted fields to the Unified Data Model (UDM), enriching the data with
network connection details and security results while categorizing events based
on available information.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Aruba Central or SD-WAN Orchestrator or both
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
'ARUBA_EDGECONNECT_SDWAN'
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
Configure Syslog in Aruba Central
Sign in to the
Aruba Central
web UI.
Go to
Manage
>
Devices
>
Gateways
.
Select a
Gateway
under
Device Name
. The dashboard context for the gateway device is displayed.
In
Manage
, click
Device
. The gateway configuration page is displayed.
Click
System
>
Logging
.
Click
+
in the
Syslog Servers
section.
Provide the following configuration details:
IP address
: Enter the Bindplane agent IP address.
Category
: Select
security
(you can repeat the process later to add other categories).
Logging facility
: Select
Local0
.
Logging level
: Select
Informational
.
Format
: Select
cef
.
Click
Save Settings
.
UDM mapping table
Log Field
UDM Mapping
Logic
Action
security_result.action_details
Directly mapped from the
Action
field.
Application
network.application_protocol
If the
Application
field contains "dhcp" (case-insensitive), the value is set to "DHCP".
Application
intermediary.application
Directly mapped from the
Application
field.
Direction
network.direction
Directly mapped from the
Direction
field, converted to uppercase. If the value is not "INBOUND", "OUTBOUND", or "BROADCAST", it's set to "UNKNOWN_DIRECTION".
DstAddr
target.ip
Directly mapped from the
DstAddr
field.
DstPort
target.port
Directly mapped from the
DstPort
field, converted to an integer.
Flow-ID
metadata.id
Directly mapped from the
Flow-ID
field.
FromZone
target.resource.attribute.labels
Creates a label with key "FromZone" and value from the
FromZone
field.
Host
intermediary.hostname
Directly mapped from the
Host
field.
Protocol
network.ip_protocol
Directly mapped from the
Protocol
field, converted to uppercase, and then parsed using an include file (
parse_ip_protocol.include
) to get the protocol name.
Reason
security_result.category_details
Directly mapped from the
Reason
field.
Reason
security_result.category
If the
Reason
field contains "policy deny", the value is set to "POLICY_VIOLATION".
SrcAddr
principal.ip
Directly mapped from the
SrcAddr
field.
SrcPort
principal.port
Directly mapped from the
SrcPort
field, converted to an integer.
Tag
security_result.rule_name
Directly mapped from the
Tag
field.
ToZone
target.resource.attribute.labels
Creates a label with key "ToZone" and value from the
ToZone
field.
description
metadata.description
Directly mapped from the
description
field, which is extracted from the log message when the
kv_data
field is empty.
intermediary_pid
intermediary.process.pid
Directly mapped from the
intermediary_pid
field.
timestamp
metadata.event_timestamp
Directly mapped from the
timestamp
field extracted from the log message. Set to "NETWORK_CONNECTION" if both
SrcAddr
and
DstAddr
are present, otherwise set to "GENERIC_EVENT".  Hardcoded to "ARUBA_EDGECONNECT_SDWAN". Hardcoded to "ARUBA_EDGECONNECT_SDWAN".
Need more help?
Get answers from Community members and Google SecOps professionals.
