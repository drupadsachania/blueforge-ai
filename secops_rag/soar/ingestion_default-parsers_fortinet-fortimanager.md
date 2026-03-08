# Collect Fortinet FortiManager logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimanager/  
**Scraped:** 2026-03-05T09:56:22.096138Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiManager logs
Supported in:
Google secops
SIEM
This guide explains how you can ingest Fortinet FortiManager logs to Google Security Operations using Bindplane agent.
Fortinet FortiManager is a centralized network management platform that provides unified management, best practices compliance, and workflow automation for Fortinet security and networking devices. FortiManager enables administrators to centrally manage configurations, policies, firmware updates, and security services across thousands of FortiGate firewalls and other Fortinet devices in the Security Fabric.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Windows Server 2016 or later, or Linux host with systemd.
Network connectivity between Bindplane agent and Fortinet FortiManager.
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
Privileged access to the Fortinet FortiManager management console with permissions to modify System Settings.
FortiManager version 5.0.7 or later.
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
chronicle/fortimanager
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'your-customer-id-here'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
FORTINET_FORTIMANAGER
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
fortimanager
service
:
pipelines
:
logs/fortimanager_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/fortimanager
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on. Use
0.0.0.0:514
to listen on all interfaces on port 51. If port 514 requires root privileges on Linux, use
0.0.0.0:1514
and configure FortiManager to send to port 1514.
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
: Customer ID from the previous step (for example,
a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
)
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
: Must be exactly
FORTINET_FORTIMANAGER
ingestion_labels
: Optional labels for filtering and organization
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
Configure Fortinet FortiManager syslog forwarding
FortiManager syslog configuration is a two-step process: first, define the syslog server in the GUI, then enable local log forwarding via CLI.
Step 1: Add syslog server in FortiManager GUI
Sign in to the
Fortinet FortiManager
web interface.
Go to
System Settings
>
Advanced
>
Syslog Server
.
Click
Create New
in the toolbar.
The
Create New Syslog Server Settings
pane opens.
Configure the following settings:
Name
: Enter a descriptive name (for example,
Chronicle-Bindplane
).
IP address (or FQDN)
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
Syslog Server Port
: Enter
514
(or
1514
if you configured Bindplane to listen on a non-privileged port).
Reliable Connection
: Leave disabled for UDP (default), or enable for TCP.
Secure Connection
: Leave disabled unless you have configured TLS certificates.
Click
OK
to save the syslog server configuration.
Step 2: Enable local log forwarding via CLI
After adding the syslog server in the GUI, you must enable FortiManager to send local logs to the syslog server using the CLI.
Connect to the FortiManager CLI via SSH or console.
Run the following commands:
For FortiManager 5.0.7 and later:
config system locallog syslogd setting
    set syslog-name Chronicle-Bindplane
    set severity information
    set status enable
end
Configuration parameters:
syslog-name
: Must match the
Name
you configured in the GUI (for example,
Chronicle-Bindplane
).
severity
: Set to
information
to capture all local logs. The default is
notification
, which captures fewer events. Options are:
emergency
,
alert
,
critical
,
error
,
warning
,
notification
,
information
,
debug
.
status
: Set to
enable
to start forwarding logs.
Verify the configuration:
config system locallog syslogd setting
    show
end
Verify logs are being sent by checking the Bindplane agent logs or using packet capture on the Bindplane agent host:
Linux:
sudo
tcpdump
-i
any
port
514
-A
Windows:
Use Wireshark or Microsoft Message Analyzer to capture traffic on port 514.
Notes on FortiManager syslog behavior
FortiManager sends its own local event logs (system, configuration changes, administrative actions) to the configured syslog server, not logs from managed FortiGate devices.
By default,
Reliable Connection
is disabled, which means logs are sent via UDP on port 51. If you enable
Reliable Connection
, logs are sent via TCP on port 514.
FortiManager syslog messages use a Fortinet-specific format that is not strictly RFC 3164 or RFC 5424 compliant. The Google SecOps FORTINET_FORTIMANAGER parser is designed to handle this format.
Ensure the FortiManager system time is synchronized with NTP and configured to UTC for accurate log timestamps. To configure system time, go to
Dashboard
, then in the
System Information
widget, click the edit system time button next to the
System Time
field.
UDM mapping table
Log field
UDM mapping
Logic
type, subtype, pri, operation, performed_on, lograte, msgrate, logratelimit, logratepeak, action, cpuusage, memusage, diskusage, disk2usage, userfrom
about.resource.attribute.labels
Labels associated with the resource.
clearpass-spt, allow-routing, color, comment, fabric-object, name, node-ip-only, obj-type, sdn-addr-type, sub-type, adom, pkgname, _signal-lte-rsrq, _signal-lte-rssi, performed_on_dev, changetype
event.idm.read_only_udm.additional.fields
Additional fields not covered by the standard UDM schema.
event.idm.read_only_udm.about
Information about the event.
event.idm.read_only_udm.extensions
Extensions to the event.
event.idm.read_only_udm.metadata
Metadata about the event.
cache_ttl_label
event.idm.read_only_udm.network
Network-related information.
event.idm.read_only_udm.principal
Information about the principal entity.
event.idm.read_only_udm.security_result
Results of security analysis.
event.idm.read_only_udm.target
Information about the target entity.
extensions.auth.type
The type of authentication.
changes
metadata.description
A description of the event.
event_type
metadata.event_type
The type of event.
log_id
metadata.product_log_id
The product-specific identifier for the log entry.
cache_ttl_label
network.dns.answers
DNS answers.
session_id
network.session_id
The session ID of the network connection.
adminprof
principal.administrative_domain
The administrative domain of the principal.
devname
principal.asset.hostname
The hostname of the asset associated with the principal.
src_ip
principal.asset.ip
The IP address of the asset associated with the principal.
devname
principal.hostname
The hostname of the principal.
src_ip
principal.ip
The IP address of the principal.
device_id
principal.resource.product_object_id
The product-specific identifier for the resource.
principal.resource.resource_type
The type of resource.
uuid
principal.user.userid
The user ID of the principal user.
action_details
security_result.action
The action taken as a result of the security event.
wildcard, subnet, end-ip, start-ip
security_result.detection_fields
Fields used for detection in security results.
msg
security_result.summary
A summary of the security result.
target_ip, tar_ip, remote_ip
target.asset.ip
The IP address of the asset associated with the target.
target_ip, tar_ip, remote_ip
target.ip
The IP address of the target.
tar_port, remote_port
target.port
The port number of the target.
user
target.user.userid
The user ID of the target user.
metadata.vendor_name
The vendor name.
metadata.product_name
The product name.
Need more help?
Get answers from Community members and Google SecOps professionals.
