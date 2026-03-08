# Collect F5 BIG-IP APM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-apm/  
**Scraped:** 2026-03-05T09:24:00.313084Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 BIG-IP APM logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 BIG-IP APM logs to Google Security Operations using Bindplane.
F5 BIG-IP Access Policy Manager (APM) provides secure, unified access to applications, APIs, and data. It delivers identity-aware, context-based access control with SSO, multi-factor authentication, and SSL VPN capabilities for enterprise networks. The parser extracts fields from F5 BIG-IP APM syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the F5 BIG-IP management interface
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
udplog
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
'F5_BIGIP_APM'
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
Configuration parameters
Replace the following placeholders:
Receiver configuration:
udplog
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
F5_BIGIP_APM
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
Configure F5 BIG-IP APM syslog forwarding
Sign in to the
F5 BIG-IP
web interface (TMUI/Configuration Utility).
Go to
System
>
Logs
>
Configuration
>
Remote Logging
.
In the
Remote Logging
section, provide the following configuration details:
Remote IP
: Enter the IP address of the Bindplane agent host.
Remote Port
: Enter
514
.
Click
Add
.
Click
Update
to save the configuration.
To configure high-speed logging (HSL) for detailed APM logs via CLI:
SSH to the
F5 BIG-IP
system.
Run the following commands:
tmsh create ltm pool syslog_pool members add { BINDPLANE_IP:514 }
tmsh create sys log-config destination remote-high-speed-log secops_hsl pool-name syslog_pool protocol udp
tmsh create sys log-config destination remote-syslog secops_syslog remote-high-speed-log secops_hsl
tmsh create sys log-config publisher secops_publisher destinations add { secops_syslog }
tmsh save sys config
Replace
BINDPLANE_IP
with the IP address of the Bindplane agent host.
Assign the publisher to the APM access profile:
Go to
Access
>
Profiles / Policies
>
Access Profiles
.
Select the target access profile.
In the
Log Settings
tab, select the created publisher.
Click
Update
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
application
principal.application
The value is taken from the application field extracted by the grok filter.
bytes_in
network.received_bytes
The value is taken from the bytes_in field extracted by the grok filter and converted to unsigned integer.
bytes_out
network.sent_bytes
The value is taken from the bytes_out field extracted by the grok filter and converted to unsigned integer.
cmd_data
principal.process.command_line
The value is taken from the cmd_data field extracted by the kv filter.
destination_ip
target.ip
The value is taken from the destination_ip field extracted by the grok filter.
destination_port
target.port
The value is taken from the destination_port field extracted by the grok filter and converted to integer.
folder
principal.process.file.full_path
The value is taken from the folder field extracted by the kv filter.
geoCountry
principal.location.country_or_region
The value is taken from the geoCountry field extracted by the grok filter.
geoState
principal.location.state
The value is taken from the geoState field extracted by the grok filter.
inner_msg
security_result.description
The value is taken from the inner_msg field extracted by the grok filter when no other specific description is available.
ip_protocol
network.ip_protocol
The value is taken from the ip_protocol field extracted by the grok filter.
principal_hostname
principal.hostname
The value is taken from the principal_hostname field extracted by the grok filter.
principal_ip
principal.ip
The value is taken from the principal_ip field extracted by the grok filter.
process_id
principal.process.pid
The value is taken from the process_id field extracted by the grok filter.
role
user_role.name
The value is taken from the role field extracted by the grok filter. If the role field contains "admin" (case-insensitive), the value is set to "ADMINISTRATOR".
severity
security_result.severity_details
The original value from the syslog message is stored here. The value is derived from the severity field using conditional logic: , CRITICAL -> CRITICAL , ERR -> ERROR , ALERT, EMERGENCY -> HIGH , INFO, NOTICE -> INFORMATIONAL , DEBUG -> LOW , WARN -> MEDIUM
source_ip
principal.ip
The value is taken from the source_ip field extracted by the grok filter.
source_port
principal.port
The value is taken from the source_port field extracted by the grok filter and converted to integer.
status
security_result.summary
The value is taken from the status field extracted by the kv filter.
timestamp
metadata.event_timestamp, timestamp
The value is taken from the timestamp field extracted by the grok filter and parsed into a timestamp object. The timestamp field in the top level event object also gets this value.
user
principal.user.userid
The value is taken from the user field extracted by the grok filter, after removing "id" or "ID" prefixes. The value is derived based on the presence of other fields: , If user exists: USER_UNCATEGORIZED , If source_ip and destination_ip exist: NETWORK_CONNECTION , If principal_ip or principal_hostname exist: STATUS_UPDATE , Otherwise: GENERIC_EVENT Hardcoded to "BIGIP_APM". Hardcoded to "F5". If the result field is "failed", the value is set to "BLOCK".
Need more help?
Get answers from Community members and Google SecOps professionals.
