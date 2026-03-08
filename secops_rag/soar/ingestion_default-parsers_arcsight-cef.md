# Collect ArcSight CEF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arcsight-cef/  
**Scraped:** 2026-03-05T09:49:57.695775Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ArcSight CEF logs
Supported in:
Google secops
SIEM
This document explains how to ingest ArcSight CEF (Common Event Format) logs to
Google Security Operations using Bindplane. The parser transforms raw data
into a structured Unified Data Model (UDM) format. It extracts fields from the
CEF header and extensions, maps them to UDM fields, and performs specific logic
to categorize events like user logins, network connections, and resource accesses
based on extracted information.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
ArcSight SmartConnector 8.4
(or later) installed on a host with network access to the Bindplane agent
Privileged access to OpenText portal
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
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
Windows installation
Open the
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
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory
on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
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
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'ARCSIGHT_CEF'
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
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the
authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Download ArcSight SmartConnector
Sign in to the
OpenText support portal
.
Find and download the latest ArcSight SmartConnector for Linux.
Example filename:
ArcSight-Connector-Linux64-8.4.0.8499.0.bin
.
Install the ArcSight SmartConnector
Upload the
.bin
file to the SmartConnector server:
scp
ArcSight-Connector-Linux64-8.4.0.8499.0.bin
user@your-smartconnector-host:/tmp
Sign in to the
SmartConnector
server using SSH and run:
cd
/tmp
chmod
+x
ArcSight-Connector-Linux64-8.4.0.8499.0.bin
./ArcSight-Connector-Linux64-8.4.0.8499.0.bin
Follow the interactive installer:
Select installation directory (for example,
/opt/arcsight/connectors/current
).
Accept the license.
Select
Install connector
when prompted.
Configure ArcSight SmartConnector to send CEF to Syslog
In the
SmartConnector host
, launch the destination wizard:
cd
/opt/arcsight/connectors/current/bin
./arcsight
connectors
In the wizard, do the following:
Select
Add Destination
.
Select
CEF Syslog
.
Provide the following configuration details:
Host/IP
: Enter the Bindplane agent IP address.
Port
: Enter your Bindplane agent port number.
Protocol
: Select
UDP
.
Finish the setup and restart the connector:
./arcsight
agents
Run a check for connectivity: (for example, look for:
Successfully connected to syslog: X.X.X.X:514
).
tail
-f
/opt/arcsight/connectors/current/logs/agent.log
UDM mapping table
Log field
UDM mapping
Logic
act
security_result.action_details
Directly mapped from the
act
field.
agt
principal.ip
Directly mapped from the
agt
field.
agt
principal.asset.ip
Directly mapped from the
agt
field.
app
network.application_protocol
Directly mapped from the
app
field.
art
metadata.event_timestamp.seconds
Directly mapped from the
art
field.
cs2
additional.fields.value.string_value
Directly mapped from the
cs2
field when
cs2Label
is
EventlogCategory
.
cs2Label
additional.fields.key
Directly mapped from the
cs2Label
field when its value is
EventlogCategory
.
cs3
additional.fields.value.string_value
Directly mapped from the
cs3
field when
cs3Label
is
Process ID
.
cs3Label
additional.fields.key
Directly mapped from the
cs3Label
field when its value is
Process ID
.
cs5
additional.fields.value.string_value
Directly mapped from the
cs5
field when
cs5Label
is
Authentication Package Name
.
cs5Label
additional.fields.key
Directly mapped from the
cs5Label
field when its value is
Authentication Package Name
.
cs6
additional.fields.value.string_value
Directly mapped from the
cs6
field when
cs6Label
is
Logon GUID
.
cs6Label
additional.fields.key
Directly mapped from the
cs6Label
field when its value is
Logon GUID
.
dhost
about.hostname
Directly mapped from the
dhost
field.
dhost
target.hostname
Directly mapped from the
dhost
field.
dntdom
about.administrative_domain
Directly mapped from the
dntdom
field.
dntdom
target.administrative_domain
Directly mapped from the
dntdom
field.
dproc
about.process.command_line
Directly mapped from the
dproc
field.
dproc
target.process.command_line
Directly mapped from the
dproc
field.
dst
principal.ip
Directly mapped from the
dst
field.
dst
principal.asset.ip
Directly mapped from the
dst
field.
dst
target.ip
Directly mapped from the
dst
field.
duid
target.user.userid
Directly mapped from the
duid
field.
duser
target.user.user_display_name
Directly mapped from the
duser
field.
dvc
about.ip
Directly mapped from the
dvc
field.
dvchost
about.hostname
Directly mapped from the
dvchost
field.
eventId
additional.fields.value.string_value
Directly mapped from the
eventId
field.
externalId
metadata.product_log_id
Directly mapped from the
externalId
field.
fname
additional.fields.value.string_value
Directly mapped from the
fname
field.
msg
metadata.description
Directly mapped from the
msg
field.
proto
network.ip_protocol
Directly mapped from the
proto
field. Translates protocol names to their respective constants (e.g.,
tcp
to
TCP
).
rt
metadata.event_timestamp.seconds
Directly mapped from the
rt
field.
shost
about.hostname
Directly mapped from the
shost
field.
shost
principal.hostname
Directly mapped from the
shost
field.
src
principal.ip
Directly mapped from the
src
field.
src
principal.asset.ip
Directly mapped from the
src
field.
src
target.ip
Directly mapped from the
src
field.
sproc
principal.process.command_line
Directly mapped from the
sproc
field.
spt
principal.port
Directly mapped from the
spt
field.
spt
target.port
Directly mapped from the
spt
field.
additional.EventRecordID
additional.fields.value.string_value
Directly mapped from the
ad.EventRecordID
field.
additional.ThreadID
additional.fields.value.string_value
Directly mapped from the
ad.ThreadID
field.
additional.Opcode
additional.fields.value.string_value
Directly mapped from the
ad.Opcode
field.
additional.ProcessID
additional.fields.value.string_value
Directly mapped from the
ad.ProcessID
field.
additional.TargetDomainName
additional.fields.value.string_value
Directly mapped from the
ad.TargetDomainName
field.
additional.Version
additional.fields.value.string_value
Directly mapped from the
ad.Version
field.
deviceExternalId
about.asset.hardware.serial_number
Directly mapped from the
deviceExternalId
field.
deviceInboundInterface
additional.fields.value.string_value
Directly mapped from the
deviceInboundInterface
field.
deviceOutboundInterface
additional.fields.value.string_value
Directly mapped from the
deviceOutboundInterface
field.
PanOSConfigVersion
security_result.detection_fields.value
Directly mapped from the
PanOSConfigVersion
field.
PanOSContentVersion
security_result.detection_fields.value
Directly mapped from the
PanOSContentVersion
field.
PanOSDGHierarchyLevel1
security_result.detection_fields.value
Directly mapped from the
PanOSDGHierarchyLevel1
field.
PanOSDestinationLocation
target.location.country_or_region
Directly mapped from the
PanOSDestinationLocation
field.
PanOSRuleUUID
metadata.product_log_id
Directly mapped from the
PanOSRuleUUID
field.
PanOSThreatCategory
security_result.category_details
Directly mapped from the
PanOSThreatCategory
field.
PanOSThreatID
security_result.threat_id
Directly mapped from the
PanOSThreatID
field.
about.asset.asset_id
Generated by concatenating
Palo Alto Networks.
, the vendor name (
LF
), and the
deviceExternalId
field.
extensions.auth.type
Set to
AUTHTYPE_UNSPECIFIED
if the
event_name
field contains
logged on
.
metadata.description
If the
description
field contains
by
followed by an IP address, the IP address is extracted and mapped to
principal.ip
and
principal.asset.ip
.
metadata.event_type
Determined based on a series of conditional checks on various fields, including
event_name
,
principal_*
,
target_*
, and
device_event_class_id
.  The logic determines the most appropriate event type based on the available information.
metadata.log_type
Set to
ARCSIGHT_CEF
.
metadata.product_event_type
Generated by concatenating
\[
, the
device_event_class_id
field,
\] -
, and the
name
field.
metadata.product_name
Set to
NGFW
if the
product_name
field is
LF
.
principal.asset.ip
If the
description
field contains
by
followed by an IP address, the IP address is extracted and mapped to
principal.ip
and
principal.asset.ip
.
principal.ip
If the
description
field contains
by
followed by an IP address, the IP address is extracted and mapped to
principal.ip
and
principal.asset.ip
.
security_result.action
Set to
ALLOW
if the
act
field is
alert
, otherwise set to
BLOCK
.
security_result.severity
Set to
HIGH
if the
sev
field is greater than or equal to 7, otherwise set to
LOW
.
Need more help?
Get answers from Community members and Google SecOps professionals.
