# Collect Symantec EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-edr/  
**Scraped:** 2026-03-05T10:00:43.109680Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec Endpoint Detection and Response (EDR) logs to Google Security Operations using Bindplane. The parser handles the logs in either JSON or CEF format. It extracts fields, maps them to the UDM, and performs event type classification based on log content, handling network connections, process events, file system activity, registry operations, and user login/logout events.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Symantec EDR.
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
For additional installation options, consult this
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
'SYMANTEC_EDR'
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
Configure Syslog in Symantec EDR
Sign in to your
Symantec EDR
web UI.
In the EDR cloud console, go to
Environment
>
Settings
.
Select an
appliance
and then click
Appliances
.
In the EDR appliance console, click
Settings
>
Appliances
.
Click
Edit Default Appliance
.
Double-click the
device
in the
Appliances
list.
In the Syslog section, clear
Use default
(if it is marked).
Click
+Add Syslog Server
.
Provide the following configuration details:
Host
: enter the Bindplane agent IP address.
Protocol
: select the configured protocol in the Bindplane agent server; for example,
UDP
.
Port
: enter the Bindplane agent port number; for example,
514
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
actor.cmd_line
principal.process.command_line
The command line executed by the actor process.
actor.file.md5
principal.process.file.md5
The MD5 hash of the actor's executable file.
actor.file.path
principal.process.file.full_path
The full path to the actor's executable file.
actor.file.sha2
principal.process.file.sha256
The SHA256 hash of the actor's executable file.
actor.pid
principal.process.pid
The process ID of the actor.
actor.uid
principal.resource.id
Unique identifier for the actor.
actor.user.name
principal.user.userid
The username of the actor.
actor.user.sid
principal.user.windows_sid
The Windows SID of the actor user.
attack.technique_name
security_result.threat_name
The name of the MITRE ATT&CK technique.
attack.technique_uid
security_result.description
Used with
attack.technique_name
to populate
security_result.description
in the format
<technique_uid>: <technique_name>
.
collector_device_ip
intermediary.ip
The IP address of the collector device.
collector_device_name
intermediary.hostname
The hostname of the collector device.
collector_name
intermediary.resource.name
The name of the collector.
collector_uid
intermediary.resource.id
The unique identifier of the collector.
connection.bytes_download
network.received_bytes
The number of bytes downloaded in the connection.
connection.bytes_upload
network.sent_bytes
The number of bytes uploaded in the connection.
connection.direction_id
network.direction
The direction of the network connection (1 for INBOUND, 2 for OUTBOUND).
connection.dst_ip
target.ip
The destination IP address of the connection.
connection.dst_port
target.port
The destination port of the connection.
connection.src_ip
principal.ip
The source IP address of the connection.
connection.src_name
principal.hostname
The source hostname of the connection.
connection.src_port
principal.port
The source port of the connection.
connection.url.host
target.hostname
The hostname in the connection URL.
connection.url.scheme
network.application_protocol
The scheme of the connection URL (e.g., HTTP, HTTPS).
connection.url.text
target.url
The full connection URL.
data_source_url_domain
target.url
The domain of the data source URL.
device_domain
principal.administrative_domain
/
target.administrative_domain
The domain of the device. Mapped to principal or target based on logic related to
connection.direction_id
.
device_ip
principal.ip
/
target.ip
The IP address of the device. Mapped to principal or target based on logic related to
connection.direction_id
.
device_name
principal.hostname
/
target.hostname
The name of the device. Mapped to principal or target based on logic related to
connection.direction_id
.
device_os_name
principal.platform_version
/
target.platform_version
The operating system of the device. Mapped to principal or target based on logic related to
connection.direction_id
.
device_uid
target.asset_id
The unique identifier of the device, prefixed with
Device ID:
.
directory.path
target.file.full_path
The path of the directory.
domain_name
target.administrative_domain
The name of the domain.
event_actor.file.path
target.process.file.full_path
The path to the event actor's executable file.
event_actor.pid
target.process.pid
The process ID of the event actor.
event_desc
metadata.description
Description of the event.
externalIP
target.ip
The external IP address.
file.md5
target.file.md5
The MD5 hash of the file.
file.path
target.file.full_path
The path to the file.
file.rep_prevalence_band
additional.fields.value.number_value
The reputation prevalence band of the file, mapped with key
prevalence_score
.
file.rep_score_band
additional.fields.value.number_value
The reputation score band of the file, mapped with key
reputation_score
.
file.sha2
target.file.sha256
The SHA256 hash of the file.
file.size
target.file.size
The size of the file.
internalHost
principal.hostname
The internal hostname.
internalIP
principal.ip
The internal IP address.
internal_port
principal.port
The internal port.
kernel.name
target.resource.name
The name of the kernel object.  The
target.resource.type
is set to
MUTEX
.
message
metadata.description
The log message.
module.md5
target.process.file.md5
The MD5 hash of the module.
module.path
target.process.file.full_path
The path to the module.
module.sha2
target.process.file.sha256
The SHA256 hash of the module.
module.size
target.process.file.size
The size of the module.
process.cmd_line
target.process.command_line
The command line of the process.
process.file.md5
target.process.file.md5
The MD5 hash of the process's executable file.
process.file.path
target.process.file.full_path
The path to the process's executable file.
process.file.sha2
target.process.file.sha256
The SHA256 hash of the process's executable file.
process.pid
target.process.pid
The process ID.
process.uid
target.resource.id
The unique identifier of the process.
process.user.name
target.user.userid
The username associated with the process.
process.user.sid
target.user.windows_sid
The Windows SID of the process user.
product_name
metadata.product_name
The name of the product generating the log.
product_ver
metadata.product_version
The version of the product generating the log.
reg_key.path
target.registry.registry_key
The registry key path.
reg_value.data
target.registry.registry_value_data
The registry value data.
reg_value.name
target.registry.registry_value_name
The registry value name.
reg_value.path
target.registry.registry_key
The registry key path for the value.
security_result.severity
security_result.severity
The severity of the security result. Translated from numeric value to UDM enum (e.g., 1 to LOW, 5 to MEDIUM, 10 to LOW, 15 to LOW).
session.id
network.session_id
The session ID.
session.user.name
target.user.userid
The username associated with the session.
sid
principal.user.userid
The security identifier (SID).
status_detail
security_result.summary
Additional details about the status.
type_id
metadata.product_event_type
The event type ID.
user_agent_ip
target.ip
The IP address of the user agent.
user_name
principal.user.userid
/
target.user.user_display_name
The username. Mapped to principal or target based on logic related to CEF or JSON parsing.
user_uid
target.user.userid
The unique identifier of the user.
uuid
metadata.product_log_id
The UUID of the event.
event.idm.read_only_udm.metadata.event_timestamp
event.idm.read_only_udm.metadata.event_timestamp
The timestamp of the event. Derived from
log_time
or CEF
device_time
.
event.idm.read_only_udm.metadata.log_type
event.idm.read_only_udm.metadata.log_type
The type of log. Hardcoded to
SYMANTEC_EDR
.
event.idm.read_only_udm.metadata.vendor_name
event.idm.read_only_udm.metadata.vendor_name
The name of the vendor. Hardcoded to
Symantec
.
event.idm.read_only_udm.extensions.auth.type
event.idm.read_only_udm.extensions.auth.type
The authentication type. Set to
MACHINE
for login and logout events.
security_result.action
security_result.action
The action taken as a result of the security event. Set to
ALLOW
for successful logins and logouts.
Need more help?
Get answers from Community members and Google SecOps professionals.
