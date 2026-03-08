# Collect Juniper Junos logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-junos/  
**Scraped:** 2026-03-05T09:25:55.351898Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Juniper Junos logs
Supported in:
Google secops
SIEM
This document explains how to ingest Juniper Junos logs to Google Security Operations using Bindplane.
Juniper Junos OS is the operating system that powers Juniper Networks routers, switches, and security devices. It provides a unified platform for network infrastructure management, routing, switching, and security functions with comprehensive logging of system events, security events, and network traffic. The parser extracts fields from Juniper Junos syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Juniper device running Junos OS
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
'JUNIPER_JUNOS'
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
JUNIPER_JUNOS
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
Configure Syslog forwarding on Juniper Junos
Connect to the
Juniper
device via SSH or console.
Enter configuration mode:
configure
Configure the syslog host with the following commands:
set system syslog host BINDPLANE_IP any info
set system syslog host BINDPLANE_IP port 514
set system syslog host BINDPLANE_IP facility-override local7
set system syslog host BINDPLANE_IP log-prefix JUNOS
Replace
BINDPLANE_IP
with the IP address of the Bindplane agent host.
Configure additional log sources (optional but recommended):
set system syslog host BINDPLANE_IP authorization info
set system syslog host BINDPLANE_IP daemon info
set system syslog host BINDPLANE_IP kernel info
set system syslog host BINDPLANE_IP firewall any
set system syslog host BINDPLANE_IP interactive-commands info
Configure structured syslog data (optional for enhanced parsing):
set system syslog host BINDPLANE_IP structured-data
Commit the configuration:
commit and-quit
Verify the syslog configuration:
show system syslog host BINDPLANE_IP
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
DPT
target.port
The destination port of the network connection, converted to an integer.
DST
target.ip
The destination IP address of the network connection.
FLAG
additional.fields{}.key: "FLAG", additional.fields{}.value.string_value: Value of FLAG
The TCP flag associated with the network connection.
ID
additional.fields{}.key: "ID", additional.fields{}.value.string_value: Value of ID
The IP identification field.
IN
additional.fields{}.key: "IN", additional.fields{}.value.string_value: Value of IN
The incoming network interface.
LEN
additional.fields{}.key: "LEN", additional.fields{}.value.string_value: Value of LEN
The length of the IP packet.
MAC
principal.mac
The MAC address extracted from the MAC field.
OUT
additional.fields{}.key: "OUT", additional.fields{}.value.string_value: Value of OUT
The outgoing network interface.
PREC
additional.fields{}.key: "PREC", additional.fields{}.value.string_value: Value of PREC
The Precedence field in the IP header.
PROTO
network.ip_protocol
The IP protocol used in the network connection.
RES
additional.fields{}.key: "RES", additional.fields{}.value.string_value: Value of RES
Reserved field in the TCP header.
SPT
principal.port
The source port of the network connection, converted to an integer.
SRC
principal.ip
The source IP address of the network connection.
TOS
additional.fields{}.key: "TOS", additional.fields{}.value.string_value: Value of TOS
The Type of Service field in the IP header.
TTL
network.dns.additional.ttl
Time To Live value, converted to an unsigned integer.
URGP
additional.fields{}.key: "URGP", additional.fields{}.value.string_value: Value of URGP
Urgent pointer field in the TCP header.
WINDOW
additional.fields{}.key: "WINDOW_SIZE", additional.fields{}.value.string_value: Value of WINDOW
The TCP window size.
action
security_result.action
The action taken by the firewall, extracted from the CEF message.
agt
observer.ip
The IP address of the agent.
amac
target.mac
The MAC address of the target, converted to lowercase and with hyphens replaced by colons.
app
target.application
The application involved in the event.
artz
observer.zone
The observer time zone.
atz
target.location.country_or_region
The target time zone.
categoryBehavior
additional.fields{}.key: "Category Behavior", additional.fields{}.value.string_value: Value of categoryBehavior with slashes removed
The category behavior.
categoryDeviceGroup
additional.fields{}.key: "Category Device Group", additional.fields{}.value.string_value: Value of categoryDeviceGroup with slashes removed
The category device group.
categoryObject
additional.fields{}.key: "Category Object", additional.fields{}.value.string_value: Value of categoryObject with slashes removed
The category object.
categoryOutcome
additional.fields{}.key: "Category Outcome", additional.fields{}.value.string_value: Value of categoryOutcome with slashes removed
The category outcome.
categorySignificance
additional.fields{}.key: "category Significance", additional.fields{}.value.string_value: Value of categorySignificance
The category significance.
command
target.process.command_line
The command executed.
cs1Label
additional.fields{}.key: cs1Label, additional.fields{}.value.string_value: Value of corresponding CEF field
Custom string field 1 label and value from the CEF message.
cs2Label
additional.fields{}.key: cs2Label, additional.fields{}.value.string_value: Value of corresponding CEF field
Custom string field 2 label and value from the CEF message.
cs3Label
additional.fields{}.key: cs3Label, additional.fields{}.value.string_value: Value of corresponding CEF field
Custom string field 3 label and value from the CEF message.
cs4Label
additional.fields{}.key: cs4Label, additional.fields{}.value.string_value: Value of corresponding CEF field
Custom string field 4 label and value from the CEF message.
cs5Label
additional.fields{}.key: cs5Label, additional.fields{}.value.string_value: Value of corresponding CEF field
Custom string field 5 label and value from the CEF message.
cs6Label
additional.fields{}.key: cs6Label, additional.fields{}.value.string_value: Value of corresponding CEF field
Custom string field 6 label and value from the CEF message.
dhost
target.hostname
Destination hostname.
deviceCustomString1
additional.fields{}.key: cs1Label, additional.fields{}.value.string_value: Value of deviceCustomString1
Device custom string 1.
deviceCustomString2
additional.fields{}.key: cs2Label, additional.fields{}.value.string_value: Value of deviceCustomString2
Device custom string 2.
deviceCustomString3
additional.fields{}.key: cs3Label, additional.fields{}.value.string_value: Value of deviceCustomString3
Device custom string 3.
deviceCustomString4
additional.fields{}.key: cs4Label, additional.fields{}.value.string_value: Value of deviceCustomString4
Device custom string 4.
deviceCustomString5
additional.fields{}.key: cs5Label, additional.fields{}.value.string_value: Value of deviceCustomString5
Device custom string 5.
deviceCustomString6
additional.fields{}.key: cs6Label, additional.fields{}.value.string_value: Value of deviceCustomString6
Device custom string 6.
deviceDirection
network.direction
The direction of the network traffic.
deviceEventClassId
additional.fields{}.key: "eventId", additional.fields{}.value.string_value: Value of deviceEventClassId
The device event class ID.
deviceFacility
observer.product.subproduct
The device facility.
deviceProcessName
about.process.command_line
The device process name.
deviceSeverity
security_result.severity
The device severity.
deviceTimeZone
observer.zone
The device time zone.
deviceVendor
metadata.vendor_name
The device vendor.
deviceVersion
metadata.product_version
The device version.
dpt
target.port
The destination port.
dst
target.ip
The destination IP address.
duser
target.user.user_display_name
The destination user.
eventId
additional.fields{}.key: "eventId", additional.fields{}.value.string_value: Value of eventId
Event ID.
event_time
metadata.event_timestamp
The time the event occurred, parsed from the message.
firewall_action
security_result.action_details
The firewall action taken.
host
principal.hostname, intermediary.hostname
The hostname of the device generating the log. Used for both principal and intermediary in different cases.
msg
security_result.summary
The message associated with the event, used as a summary for the security result.
name
metadata.product_event_type
The name of the event.
process_name
additional.fields{}.key: "process_name", additional.fields{}.value.string_value: Value of process_name
The name of the process.
p_id
target.process.pid
The process ID, converted to a string.
sha256
principal.process.file.sha256
The SHA256 hash of a file, extracted from the SSH2 key information.
shost
principal.hostname
Source hostname.
source_address
principal.ip
The source IP address.
source_port
principal.port
The source port, converted to an integer.
src
principal.ip
The source IP address.
src_ip
principal.ip
The source IP address.
src_port
principal.port
The source port, converted to an integer.
ssh2
security_result.detection_fields{}.key: "ssh2", security_result.detection_fields{}.value: Value of ssh2
SSH2 key information.
subtype
metadata.product_event_type
The subtype of the event.
task_summary
security_result.description
The task summary, used as the description for the security result.
timestamp
metadata.event_timestamp
The timestamp of the event.
user
target.user.userid
The user associated with the event.
username
principal.user.userid
The username associated with the event.
user_name
principal.user.userid
The username.
metadata.vendor_name
Hardcoded to "Juniper Firewall". Hardcoded to "Juniper Firewall". Hardcoded to "JUNIPER_JUNOS". Determined by parser logic based on log content. Defaults to "STATUS_UPDATE" if not a CEF message and no other specific event type is identified. Set to "NETWORK_HTTP" for CEF messages. If no desc field is present, this field is populated with the message_description extracted from the raw log message.
Need more help?
Get answers from Community members and Google SecOps professionals.
