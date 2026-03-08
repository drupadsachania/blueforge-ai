# Collect Cyber 2.0 IDS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyber-2-ids/  
**Scraped:** 2026-03-05T09:22:49.846386Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cyber 2.0 IDS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cyber 2.0 IDS logs into Google Security Operations using the Bindplane agent.
Cyber 2.0 IDSs provide enterprise-grade network security with integrated intrusion detection and prevention capabilities. The MX appliances use the Snort intrusion detection engine to monitor network traffic for malicious activity and generate IDS alerts based on threat intelligence from Cisco Talos. IDS alerts are generated in two formats: legacy
ids-alerts
and current
security_event
types, with priority levels ranging from 1 (high) to 4 (very low) based on Snort signature classifications.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and Cyber 2.0 IDS
If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
Administrative access to the Cisco Meraki Dashboard
Cyber 2.0 IDS with Advanced Security Edition licensing (required for IDS/IPS features)
Network connectivity from the Meraki MX appliance to the Bindplane agent host (UDP port 514 or custom port)
Get the Google SecOps ingestion authentication file
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
Get the Google SecOps customer ID
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
Configure Bindplane agent to ingest syslog and send logs to Google SecOps
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
chronicle/meraki_ids
:
compression
:
gzip
creds_file_path
:
'<CREDS_FILE_PATH>'
customer_id
:
'<CUSTOMER_ID>'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
CYBER_2_IDS
raw_log_field
:
body
ingestion_labels
:
vendor
:
cisco_meraki
product
:
mx_security_appliance
service
:
pipelines
:
logs/meraki_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/meraki_ids
Replace the following placeholders:
Receiver configuration:
The receiver is configured to listen on all interfaces (
0.0.0.0
) on UDP port
514
(standard syslog port)
If port 514 is already in use or you need to run as non-root on Linux, change the port to
1514
or another available port
Exporter configuration:
<CREDS_FILE_PATH>
: Full path to the ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
<CUSTOMER_ID>
: Customer ID copied from the previous step
endpoint
: Regional endpoint URL (the default shown is the US region):
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
: Set to
CYBER_2_IDS
for Cisco Meraki IDS alerts.
ingestion_labels
: Optional labels to categorize logs in Google SecOps.
Example configuration
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/meraki_ids
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
CYBER_2_IDS
raw_log_field
:
body
ingestion_labels
:
vendor
:
cisco_meraki
product
:
mx_security_appliance
environment
:
production
service
:
pipelines
:
logs/meraki_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/meraki_ids
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
Verify the service is running:
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
Verify the service is running:
sc query observiq-otel-collector
Check the logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Cyber 2.0 IDS syslog forwarding
Sign in to the
Cisco Meraki Dashboard
at
https://dashboard.meraki.com
.
Select your organization from the organization dropdown menu at the top left.
Select the network containing your MX Security Appliance from the network dropdown menu.
Go to
Network-wide
>
Configure
>
General
.
Scroll down to the
Reporting
section.
Under
Syslog servers
, click
Add a syslog server
.
Configure the syslog server with the following settings:
Server IP
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
Port
: Enter
514
(or the custom port configured in the Bindplane agent if different).
Roles
: Select the following roles to forward IDS alerts:
Check
IDS alerts
(for legacy
ids-alerts
format events)
Check
Security events
(for current
security_event
format events including IDS alerts and AMP malware detections)
Click
Save changes
at the bottom of the page.
Verify that IDS/IPS is enabled on your MX Security Appliance:
Go to
Security & SD-WAN
>
Configure
>
Threat protection
.
Ensure
Mode
is set to
Detection
(IDS) or
Prevention
(IPS).
Select a ruleset:
Connectivity
,
Balanced
, or
Security
, based on your security requirements.
Click
Save changes
.
Generate test traffic to verify log forwarding:
Go to
Security & SD-WAN
>
Monitor
>
Security center
.
Verify that IDS alerts are being generated.
Check the Bindplane agent logs to confirm that events are being received and forwarded to Google SecOps.
UDM mapping table
Log Field
UDM Mapping
Logic
time1, monthnum+day+time2, time
metadata.event_timestamp
Timestamp when the event occurred
app_version
about.resource.attribute.labels
List of key-value pairs for resource attributes
prod_event_type
metadata.product_event_type
Product-specific event type
Groups
principal.group.group_display_name
Display name of the group
app_name, app_version, hostname, principal_ip, md5_value
about
Information about the event
inter_host
intermediary.hostname
Hostname of the intermediary
description
metadata.description
Description of the event
Protocol
network.ip_protocol
IP protocol used in the network connection
Direction
network.direction
Direction of the network traffic
Source
principal.port
Port number of the principal
Destination
target.port
Port number of the target
SourceIP, principal_ip
principal.ip
IP address of the principal
SourceIP, principal_ip
principal.asset.ip
IP address of the principal's asset
DestinationIP
target.ip
IP address of the target
DestinationIP
target.asset.ip
IP address of the target's asset
HostName, hostname
principal.hostname
Hostname of the principal
HostName, hostname
principal.asset.hostname
Hostname of the principal's asset
ApplicationName
target.application
Application name of the target
UserName
principal.user.userid
User ID of the principal
FullPath
target.file.full_path
Full path of the file
Status
security_result.action
Action taken by the security system
pid
principal.process.pid
Process ID
src_application
principal.application
Application name of the principal
SubSeqNumber, FlowHandle, ClientZValue, MACAddress, State, IsXCast, FlowState, DLLMode
security_result.detection_fields
Detection fields from the security result
severity
security_result.severity
Severity of the security result
DB, NewApps, UniqueApps, Computers, Duration
additional.fields
Additional fields
metadata.event_type
Type of event
metadata.product_name
Product name
metadata.vendor_name
Vendor name
Need more help?
Get answers from Community members and Google SecOps professionals.
