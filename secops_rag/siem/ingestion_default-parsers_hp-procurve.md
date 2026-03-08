# Collect HP ProCurve logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-procurve/  
**Scraped:** 2026-03-05T09:25:19.445365Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect HP ProCurve logs
Supported in:
Google secops
SIEM
This document explains how to ingest the HP ProCurve switch logs to Google Security Operations using Bindplane. The parser code first attempts to parse the raw log message as JSON. If that fails, it uses regular expressions (
grok
patterns) to extract fields from the message based on common HP ProCurve log formats.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to an HP ProCurve switch
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
directory on Linux or in the installation directory on Windows.
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
creds
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
ingestion_labels
:
log_type
:
HP_PROCURVE
raw_log_field
:
body
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
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on HP ProCurve Switch
Sign in to the
HP Procurve switch
with SSH.
Verify the switch interface by using the following command:
show
ip
int
br
Enable config mode on the switch using the following command:
console#
conf
t
Configure the switch to send logs using the following commands:
logging
host
<bindplae-server-ip>
transport
<udp/tcp>
port
<port-number>
logging
facility
syslog
logging
trap
informational
logging
buffer
65536
logging
origin-id
hostname
logging
source-interface
<interface>
Replace
<bindplae-server-ip>
and
<port-number>
with
Bindplane IP address
and
port
number.
Replace
<udp/tcp>
by selecting only
UDP
or
TCP
as communication protocol (depending on your Bindplane agent configuration).
Replace
<interface>
with the interface ID you received earlier from the switch (for example,
Ethernet1/1
).
Exit the configuration mode and save using the following commands:
console#
exit
console#
wr
UDM mapping table
Log field
UDM mapping
Logic
AAAScheme
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
AAAScheme
AAAType
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
AAAType
Chassis ID
read_only_udm.security_result.detection_fields.value
Value extracted from
description
field if the key is
Chassis ID
Command is
read_only_udm.security_result.detection_fields.value
Text after
Command is
in the
commandInfo
field
CommandSource
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
CommandSource
Config-Method
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
config_method
ConfigDestination
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
ConfigDestination
ConfigSource
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
ConfigSource
Device-Name
read_only_udm.principal.hostname
If the field exists in the log, it's mapped to principal hostname and asset hostname
Event-ID
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
event_id
EventIndex
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
EventIndex
IfIndex
read_only_udm.security_result.detection_fields.value
Value extracted from
description
field if the key is
IfIndex
IP: %{IP:IPAddr}
read_only_udm.target.ip, read_only_udm.target.asset.ip
IP address extracted from the
desc
field and mapped to target IP and target asset IP
IPAddr
read_only_udm.target.ip, read_only_udm.target.asset.ip
If the field exists in the log, it's mapped to target IP and target asset IP
Notice-Type
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
notice_type
Port ID
read_only_udm.security_result.detection_fields.value
Value extracted from
description
field if the key is
Port ID
Remote-IP-Address
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
remote_ip_address
Service
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
Service
Task
read_only_udm.security_result.detection_fields.value
Value extracted from
descrip
field if the key is
Task
User
read_only_udm.principal.user.userid
If the field exists in the log, it's mapped to principal user ID
User-Name
read_only_udm.principal.user.userid
If the field exists in the log, it's mapped to principal user ID
UserName
read_only_udm.principal.user.userid
If the field exists in the log, it's mapped to principal user ID
UserService
read_only_udm.security_result.detection_fields.value
Value extracted from
desc
field if the key is
UserService
collection_time.seconds
read_only_udm.metadata.event_timestamp.seconds
Seconds part of the event timestamp
data
This field contains the raw log message and is parsed to extract other fields. It's not mapped to the UDM.
desc
read_only_udm.security_result.description
Description extracted from the log message
descrip
Description extracted from the
desc
field, further parsed for key-value pairs. It's not mapped to the UDM.
description
read_only_udm.security_result.description
If the field exists in the log, it's mapped to the security result description
descript
read_only_udm.metadata.description
If the field exists in the log, it's mapped to the metadata description
event_id
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
event_id
eventId
read_only_udm.metadata.product_event_type
Event ID extracted from the log message
hostname
read_only_udm.principal.hostname, read_only_udm.principal.asset.hostname
Hostname extracted from the log message and mapped to principal hostname and asset hostname
inter_ip
read_only_udm.additional.fields.value.string_value, read_only_udm.intermediary.ip
If the field exists in the log and is a valid IP, it's mapped to intermediary IP. Otherwise, it's placed in the additional fields as
inter_ip
notice_type
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
notice_type
pid
read_only_udm.principal.process.pid
If the field exists in the log, it's mapped to principal process PID
program
Program information extracted from the log message, further parsed to extract module, severity, and action. It's not mapped to the UDM.
proto
read_only_udm.network.application_protocol, read_only_udm.additional.fields.value.string_value
Protocol extracted from the log message. If it matches known protocols, it's mapped to application protocol. Otherwise, it's placed in the additional fields as
Application Protocol
remote_ip_address
read_only_udm.principal.ip, read_only_udm.principal.asset.ip, read_only_udm.additional.fields.value.string_value
If the field exists in the log and is a valid IP, it's mapped to principal IP and principal asset IP. Otherwise, it's placed in the additional fields as
remote_ip_address
severity
read_only_udm.security_result.severity, read_only_udm.security_result.severity_details
Severity extracted from the
program
field after splitting by
/
. It's mapped to UDM severity levels and also stored as raw severity details
src_ip
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Source IP extracted from the log message and mapped to principal IP and principal asset IP
status
read_only_udm.additional.fields.value.string_value
If the field exists in the log, it's placed in the additional fields as
status
targetHostname
read_only_udm.target.hostname, read_only_udm.target.asset.ip
If the field exists in the log, it's mapped to target hostname and target asset IP
target_ip
read_only_udm.target.ip, read_only_udm.target.asset.ip
Target IP extracted from the log message and mapped to target IP and target asset IP
timestamp
read_only_udm.metadata.event_timestamp.seconds
Timestamp extracted from the log message and converted to event timestamp
timestamp.seconds
read_only_udm.metadata.event_timestamp.seconds
Seconds part of the event timestamp
username
read_only_udm.principal.user.userid
If the field exists in the log, it's mapped to principal user ID
read_only_udm.metadata.event_type
Determined based on a combination of fields and logic:
-
NETWORK_CONNECTION
: if
has_principal
and
has_target
are true.
-
USER_LOGOUT
: if
action
is
WEBOPT_LOGOUT
,
LOGOUT
, or
SHELL_LOGOUT
.
-
USER_LOGIN
: if
action
is
LOGIN
or
WEBOPT_LOGIN_SUC
.
-
STATUS_UPDATE
: if
action
is not empty or
src_ip
/
hostname
are not empty.
-
USER_UNCATEGORIZED
: if
has_user
is true.
-
GENERIC_EVENT
: if none of the these conditions are met.
read_only_udm.metadata.product_name
Hardcoded to
Procurve
read_only_udm.metadata.vendor_name
Hardcoded to
HP
read_only_udm.extensions.auth.type
Set to
MACHINE
if
event_type
is
USER_LOGOUT
or
USER_LOGIN
Need more help?
Get answers from Community members and Google SecOps professionals.
