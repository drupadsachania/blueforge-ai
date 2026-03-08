# Collect Fortinet FortiDDoS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiddos/  
**Scraped:** 2026-03-05T09:24:47.638380Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiDDoS logs
Supported in:
Google secops
SIEM
This guide explains how you can ingest Fortinet FortiDDoS logs to Google Security Operations using Bindplane agent.
Fortinet FortiDDoS is a DDoS attack mitigation appliance that protects networks and applications from distributed denial of service attacks. FortiDDoS provides real-time attack detection, automated mitigation, and detailed reporting for both network and application layer attacks.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Windows Server 2016 or later, or Linux host with systemd.
Network connectivity between Bindplane agent and Fortinet FortiDDoS appliance.
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
Privileged access to the FortiDDoS web interface with Read-Write permission for Log & Report settings.
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
chronicle/fortiddos
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
FORTINET_FORTIDDOS
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
logs/fortiddos_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/fortiddos
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on. Use
0.0.0.0:514
to listen on all interfaces on port 514.
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
: Must be
FORTINET_FORTIDDOS
.
ingestion_labels
: Optional labels in YAML format.
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
Configure FortiDDoS Event Log remote logging
FortiDDoS supports two types of remote syslog logging: Event Logs for system events and Attack Logs for DDoS attack events. Configure both to send comprehensive logs to Google SecOps.
Sign in to the
FortiDDoS
web interface.
Go to
Log & Report
>
Log Configuration
>
Event Log Remote
.
Click
Add
to create a new remote log server configuration.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Chronicle-Event-Logs
).
Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Minimum Log Level
: Select the minimum severity level to forward (for example,
Information
or
Notification
).
Facility
: Select a syslog facility (for example,
local0
).
Click
Save
to save the configuration.
Configure FortiDDoS Attack Log remote logging
Attack log remote logging is configured per Service Protection Profile (SPP). You must configure attack log forwarding for each SPP that you want to monitor.
Sign in to the
FortiDDoS
web interface.
Go to
Log & Report
>
Log Configuration
>
Attack Log Remote
.
Click
Add
to create a new remote log server configuration.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Chronicle-Attack-Logs
).
SPP
: Select the Service Protection Profile to configure.
Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Interval
: Select the reporting interval (for example,
1 minute
or
5 minutes
).
Click
Save
to save the configuration.
Repeat steps 3 through 5 for each SPP that you want to monitor.
Verify syslog forwarding
After configuring remote logging, verify that logs are being sent to the Bindplane agent:
On the Bindplane agent host, monitor incoming syslog traffic:
Linux:
sudo
tcpdump
-i
any
-n
port
514
Windows:
Use a network monitoring tool or check the Bindplane agent logs.
On the FortiDDoS appliance, generate test log messages:
Event log test:
Make a configuration change in the FortiDDoS web interface to generate an event log.
Attack log test:
Wait for the configured reporting interval (1 or 5 minutes). FortiDDoS reports at regular intervals and takes an additional 2 minutes to aggregate reporting. For example, logs reported for the 5-minute mark will show on the syslog server at the 7-minute mark.
Verify logs appear in Google SecOps console within 5 to 10 minutes.
UDM mapping table
Log field
UDM mapping
Logic
additional
additional
Value copied directly
additional.fields.additional_label.key
Set to "type"
type
additional.fields.additional_label.value.string_value
Value copied directly
additional.fields.src_label.key
Set to "device_id"
devid
additional.fields.src_label.value.string_value
Value copied directly
log_id
security_result.detection_fields.log_id_label.value
Value copied directly
security_result.detection_fields.log_id_label.key
Set to "log_id"
metadata
metadata
Value copied directly
desc_Data
metadata.description
Value copied directly
sip,dip,user
metadata.event_type
Set to "NETWORK_CONNECTION" if sip and dip not empty, else "USER_UNCATEGORIZED" if user not empty, else "STATUS_UPDATE" if sip not empty, else "GENERIC_EVENT"
network
network
Value copied directly
principal
principal
Value copied directly
sip
principal.asset.ip
Value copied directly
sip
principal.ip
Value copied directly
date,time,tz
principal.labels.date_label.value
Concatenated from date, time, tz with spaces
principal.labels.date_label.key
Set to "date"
dir
principal.labels.direction_label.value
Value copied directly
principal.labels.direction_label.key
Set to "direction"
dport
principal.port
Converted to integer
user
principal.user.userid
Value copied directly
security_result
security_result
Value copied directly
direction
security_result.detection_fields.direction_label.value
Value copied directly
security_result.detection_fields.direction_label.key
Set to "direction"
dropcount
security_result.detection_fields.dropcount_label.value
Value copied directly
security_result.detection_fields.dropcount_label.key
Set to "dropcount"
evecode
security_result.detection_fields.evecode_label.value
Value copied directly
security_result.detection_fields.evecode_label.key
Set to "evecode"
evesubcode
security_result.detection_fields.evesubcode_label.value
Value copied directly
security_result.detection_fields.evesubcode_label.key
Set to "evesubcode"
facility
security_result.detection_fields.facility_label.value
Value copied directly
security_result.detection_fields.facility_label.key
Set to "facility"
level
security_result.detection_fields.level_label.value
Value copied directly
security_result.detection_fields.level_label.key
Set to "level"
msg_id
security_result.detection_fields.msg_id_label.value
Value copied directly
security_result.detection_fields.msg_id_label.key
Set to "msg_id"
spp_name
security_result.detection_fields.spp_name_label.value
Value copied directly
security_result.detection_fields.spp_name_label.key
Set to "spp_name"
spp
security_result.detection_fields.spp_label.value
Value copied directly
security_result.detection_fields.spp_label.key
Set to "spp"
sppoperatingmode
security_result.detection_fields.sppoperatingmode_label.value
Value copied directly
security_result.detection_fields.sppoperatingmode_label.key
Set to "sppoperatingmode"
subnet_name
security_result.detection_fields.subnet_name_label.value
Value copied directly
security_result.detection_fields.subnet_name_label.key
Set to "subnet_name"
subnetid
security_result.detection_fields.subnetid_label.value
Value copied directly
security_result.detection_fields.subnetid_label.key
Set to "subnetid"
subtype
security_result.detection_fields.subtype_label.value
Value copied directly
security_result.detection_fields.subtype_label.key
Set to "subtype"
target
target
Value copied directly
dip
target.asset.ip
Value copied directly
dip
target.ip
Value copied directly
Need more help?
Get answers from Community members and Google SecOps professionals.
