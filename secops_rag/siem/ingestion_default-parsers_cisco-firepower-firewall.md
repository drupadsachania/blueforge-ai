# Collect Cisco Firepower NGFW logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall/  
**Scraped:** 2026-03-05T09:21:26.023612Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Firepower NGFW logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Firepower Next Generation Firewall
(NGFW) logs to Google Security Operations using Bindplane. The parser extracts the
logs from various formats (syslog, JSON, and combinations thereof), normalizes
the timestamp, and maps relevant fields to the Unified Data Model (UDM). It
handles both conventional syslog messages and JSON-formatted payloads within the
logs, leveraging grok patterns and conditional logic to extract fields like
event ID, severity, and client IP, then enriches the data with labels based on
HTTP Hostname and URI.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to a Cisco Firepower device
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
ingestion authentication file
.
Save the file securely on the system where BindPlane will be installed.
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
Configure the Bindplane Agent to ingest Syslog and send to Google SecOps
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
'CISCO_FIREPOWER_FIREWALL'
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
Configure Syslog on Cisco FirePower Device
Sign in to the Firepower Device Manager web UI.
Go to
System Settings
>
Logging Settings
.
Switch to
Enable
the
Data Logging
toggle.
Click the
+
icon under
Syslog Servers
.
Click
Create new Syslog Server
. (Alternatively, you can create the
Syslog Server
in
Objects
>
Syslog Servers
).
Provide the following configuration details:
IP Address
: Enter the Bindplane agent IP address.
Protocol Type
: Select
UDP
.
Port Number
: Enter the Bindplane agent port number.
Select
Data Interface
or
Management Interface
.
Click
OK
.
Select the newly created
Syslog server
from the list and click
OK
.
Click
Severity level for filtering all events
and select
Informational
logging level from the list.
Click
Save
.
Click the
Deploy New Settings icon
>
Deploy Now
.
Click
Policies
at the top of the screen.
Hold the pointer over the side of the
ACP rule
and click
edit
Edit
.
Go to the
Logging
tab.
Select
At End of Connection
.
Open the
Select a Syslog Alert Configuration
list.
select the Bindplane
Syslog Server
.
Click
OK
.
Click the
Deploy New Settings icon
>
Deploy Now
.
UDM mapping table
Log field
UDM mapping
Remark
act
security_result.action_details
For event IDs
313001
,
746014
.
Addr
principal.ip principal.asset.ip
For event ID
734001
.
address
principal.ip principal.asset.ip
For event ID
746014
.
action
metadata.ingestion_labels
For event IDs
313001
,
746014
.
ap
metadata.ingestion_labels
api
metadata.ingestion_labels
Assigned Ip
principal.ip principal.asset.ip
For event IDs
109201
,
109210
,
109207
.
assigned_ip
principal.ip principal.asset.ip
For event IDs
109201
,
109210
,
109207
.
bytes
network.received_bytes
centry_addr
metadata.ingestion_labels
Client
network.http.parsed_user_agent
client_ip
principal.ip principal.asset.ip
COMMAND
principal.process.command_line
For the
useradd
log type, which is event ID
199017
.
command_line
principal.process.command_line
connection_type
metadata.ingestion_labels
For event ID
734001
.
ConnectionID
network.session_id
ConnectType
metadata.ingestion_labels
cribl_pipe
additional.fields
DE
metadata.ingestion_labels
desc
metadata.description
For event IDs
109201
,
109210
,
109207
.
desc1
metadata.description
desc_data
metadata.description
description
metadata.description
dest_addr
target.ip target.asset.ip
For event ID
602101
.
device_uuid
metadata.product_log_id
Retrieved from JSON logs, where it indicates product ID details.
DeviceUUID
principal.resource.product_object_id
Retrieved from syslog, which has the resource ID.
direction
network.direction
For event ID
302020
.
DNSResponseType
network.dns.response_code
DNSSICategory
security_result.category_details
dpt
target.port
dst management IP
target.ip target.asset.ip
For event ID
418001
.
dst management Port
target.port
For event ID
418001
.
DstIP
target.ip
For event ID
713906
.
dst_ip_range
target.network.ip_subnet_range
For event IDs
418001
.
750001
,
750003
,
751002
,
750014
.
DstPort
target.port
For event ID
713906
.
duration
network.session_duration.seconds
Can be accessed in seconds.
euid
metadata.ingestion_labels
event_name
metadata.product_event_type
eventId
metadata.ingestion_labels
metadata.product_event_type
exe
principal.process.command_line
exitcode
metadata.ingestion_labels
faddr
target.ip
(outbound)
principal.ip
(inbound)
For event ID
302020
.
fdqn
principal.hostname
For event ID
746014
.
firewall
principal.ip
principal.asset.ip
flag
metadata.ingestion_labels
For event ID
500003
.
fport
target.port
(outbound)
principal.port
(inbound)
For event ID
302020
.
from
network.email.from
For the
useradd
log type, which is event ID
199017
.
fromIP
principal.ip
principal.asset.ip
For event ID
500003
.
fromPort
principal.port
For event ID
500003
.
gaddr
target.nat_port
(outbound)
principal.nat_port
(inbound)
For event ID
302020
.
GID
target.group.product_object_id
For the
useradd
log type, which is event ID
199017
.
group_id
target.group.group_display_name
hdrlen
metadata.ingestion_labels
For event ID
500003
.
home
metadata.ingestion_labels
For the
useradd
log type, which is event ID
199017
.
host
principal.ip/hostname
principal.hostname
principal.asset.hostname
host_name
principal.hostname
HTTP_Hostname
target.resource.attribute.labels
HTTP_URI
target.resource.attribute.labels
icmp_code
metadata.ingestion_labels
For event ID
313001
.
icmp_type
metadata.ingestion_labels
For event ID
313001
.
interface
metadata.ingestion_labels
For event ID
313004
.
interface_name
metadata.ingestion_labels
For event IDs
313001
,
500003
.
intermediary_host
intermed.hostname
intermed.asset.hostname
intermediary_ip
intermediary.ip
For event ID
713906
.
ipp
principal.ip
IPReputationSICategory
security_result.category_details
kernel_value
additional.fields
laddr
principal.ip
(outbound)
target.ip
(inbound)
For event ID
302020
, and mapped based on the direction (inbound or outbound).
laddr
principal.ip
principal.asset.ip
For event ID
313004
.
Local
principal.ip
principal.asset.ip
For event IDs
750001
,
750003
,
751002
,
750014
.
Local_port
principal.port
For event IDs
750001
,
750003
,
751002
,
750014
.
mailsize
network.sent_bytes
msgid
metadata.ingestion_labels
mtu_size
metadata.ingestion_labels
For event ID
602101
.
name
target.user.user_display_name
For the
useradd
log type, which is event ID
199017
.
NETWORK_SUSPICIOUS
SecCategory
(
security_result.category
)
For event ID
430001
.
os
principal.platform_version
osuser
principal.user.user_display_name
packet_size
metadata.ingestion_labels
For event ID
602101
.
path
principal.process.file.full_path
pid
principal.process.pid
pktlen
metadata.ingestion_labels
For event ID
500003
.
Policy
security_result.rule_labels
prin_ip
principal.ip
principal.asset.ip
Retrieved from
desc_data
(using the logic:
"desc_data" => "(?P<desc>.* %{IP:prin_ip}.*)"
).
prin_user
principal.user.userid
product
security_result.summary
For event IDs
430002
,
430003
.
prot
network.ip_protocol
For event ID
602101
.
Protocol
network.ip_protocol
For event IDs
302020
,
313001
,
313004
,
418001
,
protocol
network.app_protocol
For event ID
713906
.
protocol
network.ip_protocol
network.application_protocol
For when the log-field value is an application or IP protocol.
PWD
principal.process.file.full_path
For the
useradd
log type, which is event ID
199017
.
reason
security_result.detection_fields
recipients
network.email.to
Remote
target.ip
target.asset.ip
For event IDs
750001
,
750003
,
751002
,
750014
.
Remote_port
target.port
For event IDs
750001
,
750003
,
751002
,
750014
.
Revision
security_result.detection_fields
sec_desc
security_result.description
SecIntMatchingIP
metadata.ingestion_labels
SecRuleName
security_result.rule_name
For event ID
734001
.
seq_num
security_result.detection_fields
Session
network.session_id
For event IDs
109201
,
109210
,
109207
.
session_id
network.session_id
severity
security_result.summary
For event IDs
430002
,
430003
.
shell
metadata.ingestion_labels
For the
useradd
log type, which is event ID
199017
.
Sinkhole
metadata.ingestion_labels
smtpmsg
network.smtp.server_response
smtpstatus
network.http.response_code
sourceIpAddress
principal.ip
For event ID
713906
.
source_ip
principal.ip
principal.asset.ip
spt
principal.port
src management IP
principal.ip
principal.asset.ip
For event ID
418001
.
src management Port
principal.port
For event ID
418001
.
src_addr
principal.ip
principal.asset.ip
For event ID
602101
.
src_app
principal.application
src_fwuser
principal.hostname
For when
src_fwuser
is in the
host
format.
src_fwuser
principal.administrative_domain
principal.hostname
For when
src_fwuser
is in the
domain
or
host
format.
src_host
principal.hostname
principal.asset.hostname
src_interface_name
metadata.ingestion_labels
SrcIP
principal.ip
For event ID
713906
.
src_ip
principal.ip
principal.asset.ip
src_ip_range
principal.network.ip_subnet_range
For event IDs
750001
,
750003
,
751002
,
750014
.
src_port
principal.port
SrcPort
principal.port
For event ID
713906
.
srcuser
principal.user.userid
principal.user.user_display_name metadata.event_type
The value for
metadata.event_type
is
USER_UNCATEGORIZED
.
sshd
principal.application
syslog_msg_id
For event ID
716001
.
syslog_msg_text
security_result.description
tag
security_result.detection_fields
tar_ip
target.ip target.asset.ip
tar_port
target.port
TCPFlags
metadata.ingestion_labels
thread
metadata.ingestion_labels
timezoneadjustment
metadata.ingestion_labels
tls
network.smtp.is_tls
to
target.ip target.asset.ip
For event ID
313004
.
toIP
target.ip target.asset.ip
For event ID
500003
.
TRUE
is_significant
For event ID
430001
.
toPort
target.port
For event ID
500003
.
ts
metadate.event_timestamp
ts_year
metadate.event_timestamp
For event ID
430001
.
tty
metadata.ingestion_labels
TTY
metadata.ingestion_labels
For the
useradd
log type, which is event ID
199017
.
uid
metadata.ingestion_labels
UID
target.user.userid
For the
useradd
log type, which is event ID
199017
.
URLSICategory
security_result.category_details
USER
target.user.userid
For the
useradd
log type, which is event ID
199017
.
USER
principal.user.userid
For all log types other than the
useradd
log type.
User
target.user.userid
For event IDs
109201
,
109210
,
109207
,
734001
.
user
principal.user.userid
user_name
principal.user.email_addresses
UserAgent
network.http.user_agent
network.http.parsed_user_agent
Username
principal.user.userid
For event IDs
750001
,
750003
,
751002
,
750014
.
username
target.user.userid
username_Id
target.user.userid
version
metadata.ingestion_labels
UDM mapping delta reference
On November 6, 2025, Google SecOps released a new version of the Cisco Firepower NGFW parser, which includes significant changes to the mapping of Cisco Firepower NGFW log fields to UDM fields and changes to the mapping of event types.
Log-field mapping delta
The following table lists the mapping delta for Cisco Firepower NGFW log-to-UDM fields exposed prior to November 6, 2025 and subsequently (listed in the
Old mapping
and
Current mapping
columns respectively).
Log field
Old mapping
Current mapping
act
security_result.description
security_result.action_details
action
product_event_type
metadata.ingestion_labels
DeviceUUID
principal.resource.id
principal.resource.product_object_id
dpt
security_result.detection_fields
target.port
flag
about.labels
metadata.ingestion_labels
pid
principal.port
principal.process.pid
Revision
security_result.about.labels
security_result.detection_fields
spt
security_result.detection_fields
principal.port
username
principal.user.userid
target.user.userid
Event-type mapping delta
Multiple events that were classified before as generic event are now properly classified with meaningful event types.
The following table lists the delta for the handling of Cisco Firepower NGFW event types prior to November 6, 2025 and subsequently (listed in the
Old event_type
and
Current event-type
columns respectively).
Event ID from log
Old event_type
Current event_type
113003
GENERIC_EVENT
USER_UNCATEGORIZED
113009
GENERIC_EVENT
STATUS_UPDATE
113010
GENERIC_EVENT
USER_LOGIN
113039
GENERIC_EVENT
USER_LOGIN
302020
STATUS_UPDATE
NETWORK_CONNECTION
313001
GENERIC_EVENT
STATUS_UPDATE
313004
GENERIC_EVENT
NETWORK_CONNECTION
430002
NETWORK_CONNECTION
NETWORK_DNS
430003
NETWORK_CONNECTION
NETWORK_DNS
500003
GENERIC_EVENT
NETWORK_CONNECTION
602101
STATUS_UPDATE
NETWORK_CONNECTION
713906
STATUS_UPDATE
NETWORK_CONNECTION
722051
GENERIC_EVENT
STATUS_UPDATE
750003
STATUS_UPDATE
NETWORK_CONNECTION
msmtp
STATUS_UPDATE
EMAIL_TRANSACTION
Need more help?
Get answers from Community members and Google SecOps professionals.
