# Collect Dell switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-switch/  
**Scraped:** 2026-03-05T09:54:32.469534Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Dell switch logs
Supported in:
Google secops
SIEM
This parser extracts Dell switch logs, normalizes timestamps, and uses grok patterns to structure the log message into key-value pairs. It then maps these extracted fields to the Unified Data Model (UDM), handling various log formats and enriching the data with contextual information such as asset details and security severity.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have an active connection and administrative credentials for a Dell switch.
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
system where Bindplane Agent will be installed.
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
Install Bindplane Agent
Windows Installation
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
Linux Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
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
tcplog
:
# Replace the below port <54525> and IP <0.0.0.0> with your specific values
listen_address
:
"0.0.0.0:54525"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the creds location below according the placement of the credentials file you downloaded
creds
:
'{
json
file
for
creds
}'
# Replace <customer_id> below with your actual ID that you copied
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# You can apply ingestion labels below as preferred
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
sell_switch
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
tcplog
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
Restart Bindplane Agent to apply the changes
In Linux, to restart the Bindplane Agent, run the following command:
sudo
systemctl
restart
bindplane-agent
In Windows, to restart the Bindplane Agent, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog export from a Dell switch
Connect to the Dell switch using SSH or the console port.
Sign in with administrative credentials.
Use the following command to specify the IP address or hostname of the syslog server (replace
<syslog_server_ip>
,
<udp|tcp>
and
<syslog-port-number>
with the actual details):
logging
host
<syslog-server-ip>
transport
<udp
|
tcp>
port
<syslog-port-number>
Optional: Define the minimum severity level for messages to be sent to the syslog server. For example, to log informational messages and above:
logging
level
informational
Save the
running configuration
to the
startup configuration
to ensure changes persist across reboots:
copy
running-config
startup-config
Save the configuration:
write
memory
Supported Dell Switch sample logs
SYSLOG
{
"priority"
:
165
,
"version"
:
1
,
"timestamp"
:
"2023-10-12T12:37:17.249566+00:00"
,
"hostname"
:
"switch-lon-01"
,
"app_name"
:
"dn_alm"
,
"proc_id"
:
"940"
,
"message"
:
"Node.1-Unit.1:PRI [event], Dell EMC (OS10) %ALM_AUTH_EVENT: Authentication event was raised MESSAGE=pam_unix(sshd:session): session opened for user service_account by (uid=0)"
}
JSON
{
"appname"
:
"SNOOP"
,
"facility"
:
23
,
"hostname"
:
"access-switch-a1"
,
"message"
:
"snooping.c(2177) 70820228 %% DBG Report from intf Gi6/0/11 ignored -- no router ports on vlan 193"
,
"priority"
:
191
,
"proc_id"
:
"snoopTask"
}
KV / events format
Events: 
  Eventid        = {38812} 
  Occurrencetime = {3 Sept 2024 00:06:06} 
  Eventseverity  = {Minor} 
  Jobid          = {30506} 
  Computer       = {backup-server-01} 
  Program        = {DatabaseAgent} 
  Description    = {Block Change Tracking is found DISABLED on Oracle DB [PROD_DB]. Incremental backups may run slow.}
Audit SYSLOG
{
"priority"
:
110
,
"version"
:
1
,
"timestamp"
:
"2023-12-12T00:58:26.893679+00:00"
,
"hostname"
:
"core-switch-palf"
,
"app_name"
:
".clish"
,
"proc_id"
:
"29156"
,
"message"
:
"Node.1-Unit.1:PRI [audit], User sec_admin on /dev/pts/0 from 10.0.0.50 used cmd: 'terminal length 0' - completed"
}
SNMP trap / TRAPMGR format
{
"priority"
:
189
,
"version"
:
1
,
"timestamp"
:
"2023-12-28T23:37:27.394Z"
,
"hostname"
:
"dist-switch-01"
,
"app_name"
:
"TRAPMGR"
,
"proc_id"
:
"trapTask"
,
"extensions"
:
{
"origin_ip"
:
"192.168.1.1"
,
"software"
:
"N3000_Series"
,
"swVersion"
:
"6.3.2.3"
},
"message"
:
"traputil.c(721) 1056839 %% Gi1/0/5 is transitioned from the Learning state to the Forwarding state"
}
UDM mapping table
Log field
UDM mapping
Logic
acct
principal.user.userid
Used as the
userid
if the
user
field is not present.
addr
principal.asset.ip
,
principal.ip
Parsed as an IP address and used for the principal's IP and asset IP if it is a valid IP and different from the hostname.
application
principal.application
Directly mapped.
asset
principal.asset.attribute.labels.value
Directly mapped to the asset label value, with the key hardcoded as "Asset Name". If the asset field is empty and the message contains "Dell", the asset is set to "Dell".
auid
principal.resource.attribute.labels.value
Directly mapped to a label with key
auid
within
principal.resource.attribute.labels
.
datetime
metadata.event_timestamp
Parsed from various formats in the message field and converted to a timestamp.
dest_ip
target.asset.ip
,
target.ip
Mapped to target IP and target asset IP.
enterpriseId
principal.resource.attribute.labels.value
Mapped to a label with key
enterpriseId
within
principal.resource.attribute.labels
.
exe
sec_result.detection_fields.value
Mapped to a detection field with key
exe
.
File
target.file.full_path
Directly mapped.
grantors
principal.resource.attribute.labels.value
Mapped to a label with key
grantors
within
principal.resource.attribute.labels
.
host
principal.hostname
,
principal.asset.hostname
,
metadata.event_type
Used as principal hostname and asset hostname. If
host
is present,
metadata.event_type
is set to
STATUS_UPDATE
. If hostname is present but host is not, hostname is used as host.
hostname
principal.asset.ip
,
principal.ip
,
host
If it is a valid IP, used for principal IP and asset IP. If
host
is empty, it is used as
host
.
ID
principal.resource.attribute.labels.value
Mapped to a label with key
ID
within
principal.resource.attribute.labels
.
ip
principal.asset.ip
,
principal.ip
Mapped to principal IP and asset IP.
is_synced
sec_result.detection_fields.value
Mapped to a detection field with key
is_synced
.
local
target.asset.ip
,
target.ip
,
target.port
Parsed to extract local IP and port, mapped to target IP, target asset IP, and target port.
local_ip
target.asset.ip
,
target.ip
Extracted from the
local
field and mapped to target IP and target asset IP.
local_port
target.port
Extracted from the
local
field and mapped to target port.
mac
principal.mac
If it is a valid MAC address, mapped to principal MAC address.
msg
metadata.description
Used as the event description if present. Also parsed for additional fields.
msg1
metadata.description
Used as event description if
msg2
is not present.
msg2
sec_result.description
,
metadata.event_type
,
extensions.auth.type
Used as security result description. If it contains "opened for user", event type is set to
USER_LOGIN
and auth type to
MACHINE
. If it contains "closed for user", event type is set to
USER_LOGOUT
and auth type to
MACHINE
.
op
metadata.product_event_type
Used as product event type if present.
pid
principal.process.pid
Directly mapped.
port
principal.port
Directly mapped.
prod_event_type
metadata.product_event_type
Used as product event type if present.
res
sec_result.summary
Directly mapped.
sec_description
sec_result.description
,
target.url
,
target.ip
,
target.asset.ip
,
sec_result.action_details
Parsed for target URL, IP, action details, and used as security result description.
Server_ID
target.resource.product_object_id
Directly mapped.
server
principal.asset.ip
,
principal.ip
,
principal.port
Parsed to extract server IP and port, mapped to principal IP, principal asset IP, and principal port.
server_ip
principal.asset.ip
,
principal.ip
Extracted from the
server
field and mapped to principal IP and principal asset IP.
server_port
principal.port
Extracted from the
server
field and mapped to principal port.
ses
network.session_id
Directly mapped.
severity
sec_result.severity
,
metadata.product_event_type
Used to determine security result severity and product event type based on specific values.
software
principal.asset.software
Directly mapped.
softwareName
software.name
Directly mapped.
Status
sec_result.summary
Used as the security result summary if
res
is not present.
subj
principal.resource.attribute.labels.value
Mapped to a label with key
subj
within
principal.resource.attribute.labels
.
swVersion
software.version
Directly mapped.
target_host
target.hostname
,
target.asset.hostname
Directly mapped to target hostname and target asset hostname.
target_ip
target.asset.ip
,
target.ip
Directly mapped to target IP and target asset IP.
target_url
target.url
Directly mapped.
target_user_id
target.user.userid
Directly mapped.
terminal
principal.resource.attribute.labels.value
Mapped to a label with key
terminal
within
principal.resource.attribute.labels
.
tzknown
sec_result.detection_fields.value
Mapped to a detection field with key
tzknown
.
uid
principal.resource.attribute.labels.value
Mapped to a label with key
uid
within
principal.resource.attribute.labels
.
user
principal.user.userid
,
metadata.event_type
Used as principal user ID. If
user
is present,
metadata.event_type
is set to
USER_UNCATEGORIZED
.
username
target.user.userid
Directly mapped to target user ID.
N/A
metadata.vendor_name
Hardcoded to "Dell".
N/A
metadata.product_name
Hardcoded to "Dell Switch".
N/A
extensions.auth.type
Set to
MACHINE
for specific login/logout events.
N/A
metadata.event_type
Determined by a complex logic based on various fields and conditions, defaults to
GENERIC_EVENT
if not set otherwise. Can be
USER_LOGIN
,
USER_LOGOUT
,
USER_UNCATEGORIZED
,
NETWORK_CONNECTION
,
NETWORK_UNCATEGORIZED
,
STATUS_UPDATE
, or
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
