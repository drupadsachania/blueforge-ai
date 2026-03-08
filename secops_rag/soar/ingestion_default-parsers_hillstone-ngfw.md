# Collect Hillstone Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hillstone-ngfw/  
**Scraped:** 2026-03-05T09:56:54.129629Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Hillstone Firewall logs
Supported in:
Google secops
SIEM
This document explains how to ingest Hillstone Firewall logs to Google Security Operations using Bindplane.
Hillstone Firewall is a next-generation firewall that provides advanced threat detection and prevention capabilities, application control, intrusion prevention, and policy automation. The firewall offers comprehensive security features including real-time threat protection, unified threat management, and intelligent policy operation to protect network infrastructure from known and unknown threats.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and Hillstone Firewall
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Hillstone Firewall management console or appliance
Administrative credentials for the Hillstone Firewall web interface
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
chronicle/hillstone_firewall
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
HILLSTONE_NGFW
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
hillstone_firewall
service
:
pipelines
:
logs/hillstone_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/hillstone_firewall
Configuration parameters
Replace the following placeholders:
Receiver configuration:
The receiver is configured to listen on UDP port 514 on all interfaces (0.0.0.0).
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
: Replace
YOUR_CUSTOMER_ID
with the Customer ID from the previous step.
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
for a complete list.
log_type
: Set to
HILLSTONE_NGFW
exactly as shown.
ingestion_labels
: Optional labels in YAML format (customize as needed).
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
Configure Hillstone Firewall syslog forwarding
Create a syslog server
Sign in to the Hillstone Firewall web interface.
Go to
Log
>
Configuration
>
Syslog Server
to visit the Syslog Server List page.
Click
New
to create a new syslog server.
In the
Syslog Server Configuration
dialog, configure the following settings:
Host name
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
Binding
: Select
Virtual Router
and then select a virtual router from the drop-down list, or select
Source Interface
and then select a source interface from the drop-down list.
Protocol
: Select
UDP
from the drop-down list.
Port
: Enter
514
.
Log Type
: Select the log types you want the syslog server to receive. Available log types include:
Event
: System and administrative activity audits, routing and networking events.
Alarm
: Urgent, alert, and critical severity logs.
Security
: Security events such as attack defense and application security.
IPS
: Network intrusion protection events.
Configuration
: Configuration changes on command line interface.
Network
: Network services operations such as PPPoE and DDNS.
Session
: Session logs including protocols, source and destination IP addresses and ports.
NAT
: NAT logs including NAT type, source and destination IP addresses and ports.
Click
OK
to save the syslog server configuration.
Enable log forwarding for each log type
Go to
Log
>
Configuration
>
Log
to visit the
Log Configuration
page.
Click the tab of the log type you want to configure (for example,
Event
,
Alarm
,
Security
,
IPS
,
Configuration
,
Network
,
Session
, or
NAT
).
For each log type you want to forward:
Select the
Enable
to enable the log function.
Select the
Syslog server
to export logs to the syslog server.
In the
Lowest severity
drop-down list, select the lowest severity level. Logs below the severity level selected here won't be exported.
Click the
All syslog servers
link to verify that your configured syslog server is listed.
Click
OK
to save the settings.
Repeat steps 2 through 4 for each log type you want to forward to Google SecOps.
Verify log forwarding
On the Bindplane agent host, verify that syslog messages are being received:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Look for log entries indicating successful receipt and forwarding of Hillstone Firewall logs.
After 5 to 10 minutes, verify that logs appear in the Google SecOps console.
UDM mapping table
Log Field
UDM Mapping
Logic
start_time_label, close_time_label, state_label, vr_label
additional.fields
Additional metadata fields
desc
metadata.description
Description of the event
metadata.event_type
Type of event
metadata.product_name
Product name
metadata.vendor_name
Vendor name
protocol_number_src
network.ip_protocol
IP protocol used
receive_bytes
network.received_bytes
Number of bytes received
receive_packets
network.received_packets
Number of packets received
send_bytes
network.sent_bytes
Number of bytes sent
send_packets
network.sent_packets
Number of packets sent
session_id
network.session_id
Session identifier
host
principal.asset.hostname
Hostname of the principal asset
src_ip
principal.asset.ip
IP address of the principal asset
zone_val
principal.cloud.availability_zone
Cloud availability zone
host
principal.hostname
Hostname of the principal
src_ip
principal.ip
IP address of the principal
mac_address
principal.mac
MAC address of the principal
src_port
principal.port
Port number of the principal
ethernet_src_label
principal.resource.attribute.labels
Labels for principal resource attributes
id
principal.user.userid
User ID of the principal
dst_ip
target.asset.ip
IP address of the target asset
dst_ip
target.ip
IP address of the target
dst_port
target.port
Port number of the target
ethernet_dst_label
target.resource.attribute.labels
Labels for target resource attributes
policy
target.resource.name
Name of the target resource
policy
target.resource.type
Type of the target resource
user
target.user.userid
User ID of the target
Need more help?
Get answers from Community members and Google SecOps professionals.
