# Collect Fortinet Switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-switch/  
**Scraped:** 2026-03-05T09:24:53.794617Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet Switch logs
Supported in:
Google secops
SIEM
This guide explains how you can ingest Fortinet Switch logs to Google Security Operations using Bindplane agent.
Fortinet Switch is a line of secure, high-performance Ethernet switches designed for enterprise networks. FortiSwitch provides Layer 2 and Layer 3 switching capabilities, VLAN support, link aggregation, Power over Ethernet (PoE), and integrated security features. FortiSwitch units can operate in standalone mode or be managed by FortiGate firewalls via FortiLink.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Windows Server 2016 or later, or Linux host with systemd.
Network connectivity between Bindplane agent and Fortinet Switch.
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
Privileged access to the Fortinet Switch management console or FortiGate console (for managed switches).
Fortinet Switch running FortiSwitchOS 7.0 or later.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Click
Download
to download the
ingestion authentication file
.
Save the file securely on the system where Bindplane agent will be installed.
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
Install Bindplane agent
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
chronicle/fortiswitch
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
FORTINET_SWITCH
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
logs/fortiswitch_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/fortiswitch
Configuration parameters
Replace the following placeholders:
Receiver configuration:
The receiver is configured to listen on UDP port 514 for syslog messages from Fortinet Switch.
To listen on all interfaces, use
0.0.0.0:514
.
To use a non-privileged port on Linux, change to
0.0.0.0:1514
and configure Fortinet Switch to send to port 1514.
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
: Customer ID from the previous step.
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
for complete list.
log_type
: Must be exactly
FORTINET_SWITCH
.
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
.
Windows
: Click
File
>
Save
.
Restart Bindplane agent to apply the changes
Linux
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
Windows
Choose one of the following options:
Using Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Using Services console:
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
Configure Fortinet Switch syslog forwarding
Configure Fortinet Switch to send logs to the Bindplane agent. The configuration steps differ depending on whether the switch is standalone or managed by FortiGate.
For standalone FortiSwitch (GUI configuration)
Sign in to the FortiSwitch web interface.
Go to
Log
>
Config
.
Under
Syslog
, select
Enable
.
Select the severity of events to log (for example,
Information
or higher).
In the
Server
field, enter the IP address or fully qualified domain name of the Bindplane agent host.
In the
Port
field, enter
514
(or the port configured in the Bindplane agent).
In the
Facility
dropdown, select
local7
.
Click
Apply
.
For standalone FortiSwitch (CLI configuration)
Sign in to the FortiSwitch CLI via SSH or console.
Enter the following commands:
config log syslogd setting
    set status enable
    set server <BINDPLANE_AGENT_IP>
    set port 514
    set facility local7
end

config log syslogd filter
    set severity information
end
Replace
<BINDPLANE_AGENT_IP>
with the IP address of the Bindplane agent host.
Verify the configuration:
show log syslogd setting
For FortiSwitch managed by FortiGate
When FortiSwitch is managed by FortiGate, configure syslog forwarding from the FortiGate CLI.
Sign in to the FortiGate CLI via SSH or console.
Enter the following commands to configure remote syslog for managed FortiSwitch:
config switch-controller remote-log
    edit "chronicle-syslog"
        set status enable
        set server <BINDPLANE_AGENT_IP>
        set port 514
        set severity information
        set facility local7
    next
end
Replace
<BINDPLANE_AGENT_IP>
with the IP address of the Bindplane agent host.
Verify the configuration:
show switch-controller remote-log
Ensure that the FortiGate firewall policy allows syslog traffic from the FortiLink interface to the interface where the Bindplane agent is located. If needed, create a policy:
config
firewall
policy
edit
0
set
srcintf
<
fortilink_interface
>
set
dstintf
<
bindplane_interface
>
set
srcaddr
"all"
set
dstaddr
"all"
set
action
accept
set
schedule
"always"
set
service
"SYSLOG"
next
end
Replace
<fortilink_interface>
with the FortiLink interface name and
<bindplane_interface>
with the interface where the Bindplane agent is reachable.
UDM mapping table
Log field
UDM mapping
Logic
metadata.event_type
The type of event represented by this record.
event
metadata.product_event_type
The event type as reported by the product.
log_id
metadata.product_log_id
Unique identifier for the log entry as assigned by the product.
device_id
principal.asset.asset_id
Unique identifier for the asset.
devname
principal.asset.hostname
Hostname of the asset associated with the principal.
devname
principal.hostname
Hostname associated with the principal.
vd
principal.user.attribute.labels
List of labels associated with the user.
oldrole
principal.user.attribute.roles
List of roles associated with the user.
unit
principal.user.role_description
Description of the user's role.
user
principal.user.userid
Unique identifier for the user.
action
security_result.action_details
Details about the action taken.
msg
security_result.description
Description of the security result.
type, subtype, switch.physical-port, instanceid
security_result.detection_fields
List of fields that were used for detection.
pri
security_result.priority_details
Details about the priority of the event.
status
security_result.summary
Summary of the security result.
newrole
target.user.attribute.roles
List of roles associated with the target user.
metadata.product_name
Name of the product that generated the event.
metadata.vendor_name
Name of the vendor that produced the product.
Need more help?
Get answers from Community members and Google SecOps professionals.
