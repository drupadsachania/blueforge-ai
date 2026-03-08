# Collect Forcepoint DLP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-dlp/  
**Scraped:** 2026-03-05T09:24:33.140820Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forcepoint DLP logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forcepoint DLP logs to Google Security Operations using Bindplane.
Forcepoint DLP (Data Loss Prevention) is a data protection solution that identifies, monitors, and protects sensitive data across enterprise environments. It detects and prevents unauthorized data transfers through email, web, endpoints, and cloud applications using content-aware policies and machine learning. The parser extracts fields from Forcepoint DLP CEF formatted logs. It then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Forcepoint Security Manager web console
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
tcplog
:
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'FORCEPOINT_DLP'
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
tcplog
exporters
:
-
chronicle/chronicle_w_labels
Configuration parameters
Replace the following placeholders:
Receiver configuration:
tcplog
: Use
udplog
for UDP syslog or
tcplog
for TCP syslog
0.0.0.0
: IP address to listen on (
0.0.0.0
to listen on all interfaces)
514
: Port number to listen on (standard syslog port)
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
: Customer ID from the Get customer ID section
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
for complete list
log_type
: Log type exactly as it appears in Chronicle (
FORCEPOINT_DLP
)
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
Configure Forcepoint DLP syslog forwarding
Sign in to the
Forcepoint Security Manager
web console.
Go to
Settings
>
General
>
SIEM Integration
.
Select
Enable SIEM integration
.
Provide the following configuration details:
Syslog Server IP Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Protocol
: Select
TCP
.
Format
: Select
CEF
(Common Event Format).
TLS Enabled
: Uncheck (unless using TLS).
In the
Incident Data
section, select the data to include in syslog messages:
Action taken
Severity
Policy name
Source information
Destination information
Content details
Click
OK
to save.
Go to
Main
>
Policy Management
>
DLP Policies
.
For each policy that should forward events, verify syslog notification is enabled:
Select the policy.
Go to the
Action Plan
tab.
Verify the action plan includes
Send to SIEM
.
Click
Deploy
to apply the policy changes.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
act
security_result.description
If actionPerformed is empty, the value of act is assigned to security_result.description.
actionID
metadata.product_log_id
The value of actionID is assigned to metadata.product_log_id.
actionPerformed
security_result.description
The value of actionPerformed is assigned to security_result.description.
administrator
principal.user.userid
The value of administrator is assigned to principal.user.userid.
analyzedBy
additional.fields.key
The string "analyzedBy" is assigned to additional.fields.key.
analyzedBy
additional.fields.value.string_value
The value of analyzedBy is assigned to additional.fields.value.string_value.
cat
security_result.category_details
The values of cat are merged into the security_result.category_details field as a list.
destinationHosts
target.hostname
The value of destinationHosts is assigned to target.hostname.
destinationHosts
target.asset.hostname
The value of destinationHosts is assigned to target.asset.hostname.
details
security_result.description
If both actionPerformed and act are empty, the value of details is assigned to security_result.description.
duser
target.user.userid
The value of duser is used to populate target.user.userid. Multiple values separated by "; " are split and assigned as individual email addresses if they match the email regex, otherwise they are treated as user IDs.
eventId
metadata.product_log_id
If actionID is empty, the value of eventId is assigned to metadata.product_log_id.
fname
target.file.full_path
The value of fname is assigned to target.file.full_path.
logTime
metadata.event_timestamp
The value of logTime is parsed and used to populate metadata.event_timestamp.
loginName
principal.user.user_display_name
The value of loginName is assigned to principal.user.user_display_name.
msg
metadata.description
The value of msg is assigned to metadata.description.
productVersion
additional.fields.key
The string "productVersion" is assigned to additional.fields.key.
productVersion
additional.fields.value.string_value
The value of productVersion is assigned to additional.fields.value.string_value.
role
principal.user.attribute.roles.name
The value of role is assigned to principal.user.attribute.roles.name.
severityType
security_result.severity
The value of severityType is mapped to security_result.severity. "high" maps to "HIGH", "med" maps to "MEDIUM", and "low" maps to "LOW" (case-insensitive).
sourceHost
principal.hostname
The value of sourceHost is assigned to principal.hostname.
sourceHost
principal.asset.hostname
The value of sourceHost is assigned to principal.asset.hostname.
sourceIp
principal.ip
The value of sourceIp is added to the principal.ip field.
sourceIp
principal.asset.ip
The value of sourceIp is added to the principal.asset.ip field.
sourceServiceName
principal.application
The value of sourceServiceName is assigned to principal.application.
suser
principal.user.userid
If administrator is empty, the value of suser is assigned to principal.user.userid.
timestamp
metadata.event_timestamp
The value of timestamp is used to populate metadata.event_timestamp.
topic
security_result.rule_name
The value of topic is assigned to security_result.rule_name after commas are removed. Hardcoded to "FORCEPOINT_DLP". Hardcoded to "Forcepoint". Extracted from the CEF message. Can be "Forcepoint DLP" or "Forcepoint DLP Audit". Extracted from the CEF message. Concatenation of device_event_class_id and event_name, formatted as "[device_event_class_id] - event_name". Initialized to "GENERIC_EVENT". Changed to "USER_UNCATEGORIZED" if is_principal_user_present is "true".
Need more help?
Get answers from Community members and Google SecOps professionals.
