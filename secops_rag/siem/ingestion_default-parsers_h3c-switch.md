# Collect H3C Comware Platform Switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/h3c-switch/  
**Scraped:** 2026-03-05T09:25:10.624421Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect H3C Comware Platform Switch logs
Supported in:
Google secops
SIEM
This document explains how to ingest H3C Comware Platform Switch logs to Google Security Operations using Bindplane.
H3C Comware Platform Switches are enterprise-class network switches that provide Layer 2 and Layer 3 switching capabilities, advanced security features, and comprehensive network management through the Comware operating system. The switches support extensive logging capabilities through the information center feature for monitoring network operations, security events, and system diagnostics.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and H3C Comware Platform Switch
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the H3C Comware Platform Switch management console via console, Telnet, or SSH
H3C Comware Platform Switch with information center feature enabled (enabled by default)
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
chronicle/h3c_switch
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
H3C_SWITCH
raw_log_field
:
body
ingestion_labels
:
env
:
production
service
:
pipelines
:
logs/h3c_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/h3c_switch
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on UDP port 51. You may use a different port such as
1514
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
customer_id
: Replace
YOUR_CUSTOMER_ID
with your customer ID from the previous step.
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
: Set to
H3C_SWITCH
exactly as shown.
ingestion_labels
: Optional labels in YAML format (for example,
env: production
).
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
Configure H3C Comware Platform Switch syslog forwarding
Configure your H3C Comware Platform Switch to send syslog messages to the Bindplane agent.
Access the switch CLI
Sign in to the H3C Comware Platform Switch using one of the following methods:
Console port connection
Telnet
SSH
Enter system view by typing the following command:
<H3C> system-view
The prompt changes to
[H3C]
indicating you are in system view.
Verify information center is enabled
The information center is enabled by default on H3C Comware Platform Switches. To verify or enable the information center, enter the following command:
[H3C] info-center enable
If the information center is already enabled, the system displays:
Info: Information center is enabled.
Configure timestamp format (optional)
The default timestamp format for system information sent to the log host is date. To configure the timestamp format, use the following command:
[H3C] info-center timestamp loghost date
Available timestamp formats:
date
: Format is "Mmm dd hh:mm:ss:ms yyyy" (for example, Dec 8 10:12:21:708 2012)
iso
: ISO 8601 format (for example, 2012-09-21T15:32:55)
no-year-date
: Current system date and time without year
none
: No timestamp information
Configure log host
Specify the Bindplane agent host as the log host. The facility parameter can be set from local0 to local7, with the default value being local7.
[H3C] info-center loghost BINDPLANE_AGENT_IP port 514 facility local7
Replace
BINDPLANE_AGENT_IP
with the IP address of the host running the Bindplane agent.
For example, if the Bindplane agent is running on host 192.168.1.100:
[H3C] info-center loghost 192.168.1.100 port 514 facility local7
Parameters:
BINDPLANE_AGENT_IP
: IP address of the Bindplane agent host
port 514
: UDP port number (must match the port configured in Bindplane agent)
facility local7
: Syslog facility (local0 through local7 are valid; default is local7)
Configure source interface (optional)
The info-center loghost source command takes effect only after the information center is enabled with the info-center enable command. To specify a source interface for log messages:
[H3C] info-center loghost source INTERFACE_TYPE INTERFACE_NUMBER
For example, to use VLAN-interface 1 as the source:
[H3C] info-center loghost source vlan-interface 1
Disable default log output to log host
By default, the system outputs information of all modules to the log host. To control which modules send logs, first disable the default output:
[H3C] undo info-center source default loghost
Configure log output rules
Configure which modules and severity levels should send logs to the log host. The system information is classified into eight severity levels from 0 through 7 in descending order. The switch outputs the system information with a severity level higher than or equal to the specified level. For example, if you configure an output rule with a severity value of 6 (informational), the information with a severity value from 0 to 6 will be output.
Severity levels (0-7):
0: emergencies
1: alerts
2: critical
3: errors
4: warnings
5: notifications
6: informational
7: debugging
To configure log output for all modules at informational level or higher:
[
H3C
]
info
-
center
source
default
loghost
level
informational
To configure log output for specific modules (for example, ARP and IP):
[H3C] info-center source arp loghost level informational
[H3C] info-center source ip loghost level informational
To view available source modules, use:
[H3C] info-center source ?
Save the configuration
Save the configuration to ensure it persists after a reboot:
[H3C] save
When prompted, confirm by entering
Y
.
Verify the configuration
To verify the information center configuration, use the following command:
[H3C] display info-center
This command displays the current information center configuration, including log host settings, output rules, and channel configurations.
Example complete configuration
The following example shows a complete configuration for sending logs from all modules at informational level or higher to a log host at 192.168.1.100:
<H3C> system-view
[H3C] info-center enable
[H3C] info-center timestamp loghost date
[H3C] info-center loghost 192.168.1.100 port 514 facility local7
[H3C] undo info-center source default loghost
[H3C] info-center source default loghost level informational
[H3C] save
Example configuration for specific modules
The following example shows configuration for sending ARP and IP module logs at informational level to a log host:
<H3C> system-view
[H3C] info-center enable
[H3C] info-center loghost 192.168.1.100 port 514 facility local7
[H3C] undo info-center source default loghost
[H3C] info-center source arp loghost level informational
[H3C] info-center source ip loghost level informational
[H3C] save
UDM mapping table
Log Field
UDM Mapping
Logic
extensions.auth.type
Authentication type used in the event
hostname
intermediary.asset.hostname
Hostname of the asset associated with the intermediary
hostname
intermediary.hostname
Hostname of the intermediary entity
inter_ip
intermediary.asset.ip
IP address of the asset associated with the intermediary
inter_ip
intermediary.ip
IP address of the intermediary entity
IPAddr, prin_ip
principal.asset.ip
IP address of the asset associated with the principal
IPAddr, prin_ip
principal.ip
IP address of the principal entity
prin_port
principal.port
Port number associated with the principal
User, user
principal.user.userid
User ID of the principal
tar_host
target.asset.hostname
Hostname of the asset associated with the target
tar_host
target.hostname
Hostname of the target entity
tar_ip
target.asset.ip
IP address of the asset associated with the target
tar_ip
target.ip
IP address of the target entity
tar_port
target.port
Port number associated with the target
tar_user
target.user.userid
User ID of the target
Line, OperateType, OperateTime, OperateState, OperateEndTime, EventIndex, CommandSource, ConfigSource, ConfigDestination
additional.fields
Additional metadata fields not covered by standard UDM fields
desc
metadata.description
Description of the event
timestamp
metadata.event_timestamp
Timestamp when the event occurred
metadata.event_type
Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)
event_type
metadata.product_event_type
Product-specific event type identifier
metadata.product_name
Name of the product generating the event
metadata.vendor_name
Name of the vendor of the product
Need more help?
Get answers from Community members and Google SecOps professionals.
