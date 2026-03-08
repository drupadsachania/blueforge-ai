# Collect FireEye HX Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit/  
**Scraped:** 2026-03-05T09:24:26.276381Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FireEye HX Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest FireEye HX Audit logs to Google Security Operations using Bindplane agent.
FireEye HX Audit provides endpoint detection and response capabilities with advanced threat hunting, forensics data collection, and behavioral analysis to detect and respond to advanced threats on endpoints using machine learning built from thousands of incident response engagements.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and FireEye HX Audit appliance
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the FireEye HX Audit management console
Administrative access to the FireEye HX Audit appliance CLI
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
chronicle/trellix_hx
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
FIREEYE_HX_AUDIT
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
trellix_hx
service
:
pipelines
:
logs/trellix_hx_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/trellix_hx
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on. Use
0.0.0.0:514
to listen on all interfaces on port 514, or specify a different port such as
0.0.0.0:1514
if running as non-root on Linux.
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
: Replace with your actual customer ID from the previous step.
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
: Must be exactly
FIREEYE_HX_AUDIT
for proper parsing.
ingestion_labels
: Optional labels for organizing logs (customize as needed).
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
.
Windows
: Click
File
>
Save
.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, do the following:
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
To restart the Bindplane agent in Windows, do the following:
Choose one of the following options:
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
Configure FireEye HX Audit syslog forwarding
FireEye HX Audit supports two methods for forwarding logs to Google SecOps: Event Streamer module for Windows Event Logs and CLI configuration for appliance logs in CEF format.
Method 1: Configure Event Streamer for Windows Event Logs (UI)
Sign in to the
FireEye HX Audit
management console.
Go to
Event Streamer
.
Select
Enable Event Streamer on the host
.
Click
Save
to apply the policy changes.
Go to
Destinations
>
Server settings
>
Add syslog destination
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
SecOps-Collector
).
IP address
: Enter the IP address of the Bindplane agent host.
Port
: Enter the port number configured in the Bindplane agent (for example,
514
).
Click
Save
to apply the changes.
Method 2: Configure appliance syslog forwarding (CLI)
Sign in to the
FireEye HX Audit
appliance using SSH or console access.
Run the following command to enter privileged mode:
enable
Run the following command to enter configuration mode:
configure
terminal
Run the following command to verify current logging configuration:
show
logging
Run the following commands to configure syslog forwarding to the Bindplane agent:
logging
BINDPLANE_IP_ADDRESS
trap
none
logging
BINDPLANE_IP_ADDRESS
trap
override
class
cef
priority
info
logging
BINDPLANE_IP_ADDRESS
protocol
tcp
Replace
BINDPLANE_IP_ADDRESS
with the IP address of the Bindplane agent host.
Run the following command to save the configuration:
write
memory
Run the following command to exit configuration mode:
exit
Enable Data Acquisition for event log collection
To enable Windows Event Log collection through Event Streamer, configure the Data Acquisition Script settings:
Sign in to the
FireEye HX Audit
Web UI with admin access.
Go to
Admin
>
Data Acquisition Scripts
.
Click
Standard Investigative Details
.
On the
Script Description
page, click
ACTIONS
and select
Edit
.
Click
Event Logs
.
Enable
Security logs
in the
Windows event logs
section.
Click
Save
.
Enable Auto Triage
To make triage files available for collection:
Sign in to the
FireEye HX Audit
Web UI with admin access.
Go to
Admin
>
Triage Settings
.
On the
Automatic Triages
settings page, toggle the
Triage Settings switch to ON
.
Click
Save
.
Enable File and Data Audits
To enable triage file retrieval:
Sign in to the
FireEye HX Audit
Web UI with admin access.
Go to
Admin
>
Policies
.
In the
Edit Policy
page under
Configurations
, click
Audits - version number
.
Turn on
Enable the File and Data Audits on the host
.
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
alert.agent._id
principal.asset.asset_id
The agent ID from the raw log, prefixed with AGENT ID:
alert.agent.url
principal.labels.value
The agent URL from the raw log.
alert.condition._id
additional.fields.value.string_value
The condition ID from the raw log, with = characters removed.
alert.condition.url
additional.fields.value.string_value
The condition URL from the raw log, with = characters removed.
alert.decorators[].data.fireeye_report.indicator_verdict.malware_families.0
security_result.threat_name
The malware family from the FireEye report in the decorators field of the raw log.
alert.decorators[].data.fireeye_report.risk_summary
security_result.description
The risk summary from the FireEye report in the decorators field of the raw log.
alert.decorators[].data.fireeye_verdict
security_result.severity_details
The FireEye verdict from the decorators field of the raw log.
alert.event_at
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_id
read_only_udm.metadata.product_log_id
The event ID from the raw log.
alert.event_type
read_only_udm.metadata.product_event_type
The event type from the raw log.
alert.event_values.fileWriteEvent/fullPath
target.file.full_path
The full path of the file written from the raw log.
alert.event_values.fileWriteEvent/md5
target.file.md5
The MD5 hash of the file written from the raw log.
alert.event_values.fileWriteEvent/pid
principal.process.pid
The process ID that wrote the file from the raw log.
alert.event_values.fileWriteEvent/processPath
principal.process.file.full_path
The path of the process that wrote the file from the raw log.
alert.event_values.fileWriteEvent/size
target.file.size
The size of the file written from the raw log.
alert.event_values.fileWriteEvent/username
principal.user.userid
The user that wrote the file from the raw log.
alert.event_values.ipv4NetworkEvent/localIP
principal.ip
The local IP address from the raw log.
alert.event_values.ipv4NetworkEvent/localPort
principal.port
The local port from the raw log.
alert.event_values.ipv4NetworkEvent/pid
principal.process.pid
The process ID from the raw log.
alert.event_values.ipv4NetworkEvent/process
principal.process.file.full_path
The process name from the raw log.
alert.event_values.ipv4NetworkEvent/processPath
principal.process.file.full_path
The process path from the raw log.
alert.event_values.ipv4NetworkEvent/protocol
network.ip_protocol
The network protocol from the raw log.
alert.event_values.ipv4NetworkEvent/remoteIP
target.ip
The remote IP address from the raw log.
alert.event_values.ipv4NetworkEvent/remotePort
target.port
The remote port from the raw log.
alert.event_values.ipv4NetworkEvent/timestamp
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_values.ipv4NetworkEvent/username
principal.user.userid
The user from the raw log.
alert.event_values.processEvent/md5
target.process.file.md5
The MD5 hash of the process from the raw log.
alert.event_values.processEvent/parentPid
principal.process.pid
The parent process ID from the raw log.
alert.event_values.processEvent/parentProcess
principal.process.file.full_path
The parent process name from the raw log.
alert.event_values.processEvent/parentProcessPath
principal.process.file.full_path
The parent process path from the raw log.
alert.event_values.processEvent/pid
target.process.pid
The process ID from the raw log.
alert.event_values.processEvent/process
target.process.file.full_path
The process name from the raw log.
alert.event_values.processEvent/processCmdLine
target.process.command_line
The process command line from the raw log.
alert.event_values.processEvent/processPath
target.process.file.full_path
The process path from the raw log.
alert.event_values.processEvent/timestamp
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_values.processEvent/username
principal.user.userid
The user from the raw log.
alert.event_values.urlMonitorEvent/hostname
target.hostname
The hostname from the raw log.
alert.event_values.urlMonitorEvent/localPort
principal.port
The local port from the raw log.
alert.event_values.urlMonitorEvent/pid
principal.process.pid
The process ID from the raw log.
alert.event_values.urlMonitorEvent/process
principal.process.file.full_path
The process name from the raw log.
alert.event_values.urlMonitorEvent/processPath
principal.process.file.full_path
The process path from the raw log.
alert.event_values.urlMonitorEvent/remoteIpAddress
target.ip
The remote IP address from the raw log.
alert.event_values.urlMonitorEvent/remotePort
target.port
The remote port from the raw log.
alert.event_values.urlMonitorEvent/requestUrl
target.url
The requested URL from the raw log.
alert.event_values.urlMonitorEvent/timestamp
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_values.urlMonitorEvent/urlMethod
network.http.method
The HTTP method from the raw log.
alert.event_values.urlMonitorEvent/userAgent
network.http.user_agent
The user agent from the raw log.
alert.event_values.urlMonitorEvent/username
principal.user.userid
The user from the raw log.
alert.indicator._id
security_result.about.labels.value
The indicator ID from the raw log.
alert.indicator.name
read_only_udm.security_result.summary
The indicator name from the raw log.
alert.indicator.url
security_result.about.labels.value
The indicator URL from the raw log.
alert.multiple_match
read_only_udm.metadata.description
The multiple match message from the raw log.
alert.source
additional.fields.value.string_value
The source of the alert from the raw log.
host.agent_version
read_only_udm.metadata.product_version
The agent version from the raw log.
host.containment_state
read_only_udm.principal.containment_state
The containment state from the raw log.
host.domain
read_only_udm.principal.administrative_domain
The domain from the raw log.
host.hostname
read_only_udm.principal.hostname
The hostname from the raw log.
host.os.platform
read_only_udm.principal.platform
The operating system platform from the raw log.
host.os.product_name
read_only_udm.principal.platform_version
The operating system product name from the raw log.
host.primary_ip_address
read_only_udm.principal.ip
The primary IP address from the raw log.
host.primary_mac
read_only_udm.principal.mac
The primary MAC address from the raw log.
severity
security_result.severity
Set to LOW, MEDIUM, or HIGH based on the severity from the raw log.
timestamp
timestamp
The timestamp from the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
