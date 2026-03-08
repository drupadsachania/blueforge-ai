# Collect Extreme Networks switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-switch/  
**Scraped:** 2026-03-05T09:55:18.831623Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Extreme Networks switch logs
Supported in:
Google secops
SIEM
This document explains how to ingest Extreme Networks switch logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages using grok patterns and conditional logic. It maps the extracted fields to the UDM, handling login events, status updates, and generic events, enriching the data with additional context like protocol, VLAN, and user roles.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to Extreme Networks switch appliance
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
'EXTREME_SWITCH'
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
to the path where the authentication file was saved in the
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
Configure Syslog for Extreme networks switch
Sign in to the switch using CLI or Console.
Enter the configure command to access the global configuration level:
device#
configure
terminal
Enter the syslog-server IP address command to add a syslog server:
Replace
<bindplane-ip>
with the actual Bindplane agent IP address.
logging
syslog-server
<bindplane_ip>
Enter the format command to configure the RFC-5424 format for messages:
format
RFC-5424
UDM Mapping Table
Log Field
UDM Mapping
Logic
account_type
target.user.user_role
If
account_type
is "Administrative" or "admin", set to "ADMINISTRATOR". Otherwise, map to
target.user.attribute.roles.name
.
application
target.application
Directly mapped.
attr
additional.fields
Parsed to extract the WWN and create a key-value pair with key "wwn" and the extracted WWN as the string value.
class
additional.fields
Creates a key-value pair with key "class" and the value of the
class
field as the string value.
Cause
additional.fields
Creates a key-value pair with key "Cause" and the value of the
Cause
field as the string value.  Empty object created if no specific auth fields are present.
Info
security_result.summary
Directly mapped.
interface
additional.fields
Creates a key-value pair with key "interface" and the value of the
interface
field as the string value.
ip
principal.ip
Directly mapped.
intermediary_ip
intermediary.ip
Directly mapped.
kv_data
Various
Used to extract key-value pairs and map them to different UDM fields based on the key.  For example,
VrIpAddr
is mapped to
intermediary.ip
,
IP
and
Addr
are mapped to
principal.ip
,
SlppRxPort
is mapped to
principal.port
, and various
rc*
fields are mapped to
security_result.detection_fields
.
log_data
Various
Parsed to extract information about user logins, logouts, and other events. Used to populate fields like
principal.ip
,
principal.resource.name
,
target.user.userid
,
target.application
,
security_result.summary
,
security_result.description
, and
metadata.description
.
log_type
additional.fields
Creates a key-value pair with key "log" and the value of the
log_type
field as the string value.
message
Various
The original log message.  Parsed to extract various fields. The timestamp is extracted from either the
timestamp
field (if present and in "yyyy-mm-ddTHH:mm:ss" format) or from the
message
field using grok patterns. If extracted from the message field, it's the timestamp within the log message itself. Determined based on the presence of
has_principal
,
has_target
,
user_login
, and
user_logout
flags. Can be "USER_LOGIN", "USER_LOGOUT", "STATUS_UPDATE", or "GENERIC_EVENT". Mapped from the
msgid
field. Static value: "EXTREME_SWITCH". Mapped from the
ver
field. Static value: "EXTREME_SWITCH".
msgid
metadata.product_log_id
Directly mapped.
port
principal.port
Directly mapped and converted to an integer.
protocol
additional.fields
Creates a key-value pair with key "Protocol" and the value of the
protocol
field as the string value.
rcPortVLacpAdminEnable
security_result.detection_fields
Creates a key-value pair with key "rcPortVLacpAdminEnable" and its value.
rcSyslogHostAddress
principal.hostname
Directly mapped.
rcSyslogHostAddressType
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostAddressType" and its value.
rcSyslogHostEnable
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostEnable" and its value.
rcSyslogHostFacility
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostFacility" and its value.
rcSyslogHostMapErrorSeverity
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostMapErrorSeverity" and its value.
rcSyslogHostMapFatalSeverity
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostMapFatalSeverity" and its value.
rcSyslogHostMapInfoSeverity
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostMapInfoSeverity" and its value.
rcSyslogHostMapWarningSeverity
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostMapWarningSeverity" and its value.
rcSyslogHostRowStatus
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostRowStatus" and its value.
rcSyslogHostSeverity
security_result.detection_fields
Creates a key-value pair with key "rcSyslogHostSeverity" and its value.
resource
principal.resource.name
Directly mapped.
sec_description
security_result.description
Directly mapped.
seqnum
additional.fields
Creates a key-value pair with key "seqnum" and the value of the
seqnum
field as the string value.
session_id
network.session_id
Directly mapped.
severity
security_result.severity
Mapped with conversion: "CRITICAL", "ERROR", "HIGH" are mapped directly; "INFO" is mapped to "INFORMATIONAL"; "WARNING" is mapped to "MEDIUM"; "LOW", "MEDIUM", and "INFORMATIONAL" are mapped directly.
SlppIncomingVlanId
additional.fields
Creates a key-value pair with key "SlppIncomingVlanId" and the value of the
SlppIncomingVlanId
field as the string value.
SlppRxVlan
additional.fields
Creates a key-value pair with key "SlppRxVlan" and the value of the
SlppRxVlan
field as the string value.
SlppSrcMacAddress
principal.mac
Directly mapped.
Status
additional.fields
Creates a key-value pair with key "Status" and the value of the
Status
field as the string value.
swname
additional.fields
Creates a key-value pair with key "swname" and the value of the
swname
field as the string value.
timestamp
metadata.event_timestamp
Parsed and converted to a timestamp object.
tz
additional.fields
Creates a key-value pair with key "tz" and the value of the
tz
field as the string value.
Type
additional.fields
Creates a key-value pair with key "Type" and the value of the
Type
field as the string value.
username
target.user.userid
Directly mapped.
ver
metadata.product_version
Directly mapped.
VrId
additional.fields
Creates a key-value pair with key "VrId" and the value of the
VrId
field as the string value.
Need more help?
Get answers from Community members and Google SecOps professionals.
