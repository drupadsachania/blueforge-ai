# Collect VMware vCenter logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter/  
**Scraped:** 2026-03-05T10:02:18.482398Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware vCenter logs
Supported in:
Google secops
SIEM
This document explains how to ingest VMware vCenter logs to Google Security Operations using Bindplane. The parser transforms raw logs into a unified data model (UDM). It first attempts to parse the log data as JSON, and if unsuccessful, it treats the data as a syslog message, extracting fields using grok patterns and mapping them to the UDM schema.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to VMware vCenter
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
'VMWARE_VCENTER'
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
Configure Syslog for VMware vCenter
Sign in to the
vCenter Server Management
web UI.
Go to
Syslog
>
Forwarding Configuration
>
Configure
.
Select
Create Forwarding Configuration
and enter the Bindplane agent IP address.
From the
Protocol
drop-down, select
UDP
or
TCP
, depending on your actual Bindplane agent configuration.
In the
Port
section, enter the Bindplane agent port number.
Click
Save
.
Click
Send Test Message
and verify it was received.
UDM Mapping Table
Log Field
UDM Mapping
Logic
Access Mask
principal.process.access_mask
Converted to decimal from hexadecimal.
Account Domain
principal.administrative_domain
Account Name
principal.user.userid
ApplicationProtocol
additional.fields
Authentication Package
security_result.about.resource.name
Client Address
principal.ip, principal.asset.ip
Parsed as IP.
Client Port
principal.port
Converted to integer.
cmd
target.process.command_line
date
timestamp
Parsed as yyyy-MM-dd and merged with time as yyyy-MM-dd HH:mm:ss to when, parsed as date.
date_time
timestamp
Parsed as date with RFC 3339, TIMESTAMP_ISO8601, SYSLOGTIMESTAMP formats.
desc
metadata.description
eventid
metadata.product_event_type
Merged with task as eventid - task.
host_name
principal.hostname, principal.asset.hostname
http_method
network.http.method
ip
target.ip, target.asset.ip
kv_data1
Parsed as key-value pairs.
kv_data2
Parsed as key-value pairs.
kv_msg1.cipher
network.tls.cipher
kv_msg1.ctladdr
intermediary.labels
kv_msg1.daemon
security_result.about.labels
kv_msg1.from
network.email.from
If mail_from does not contain @ then appended with @local.
kv_msg1.msgid
network.email.mail_id
kv_msg1.proto
security_result.about.labels
kv_msg1.relay
intermediary.hostname, intermediary.ip
Parsed as (HOSTNAME)? [IP] or HOSTNAME, if relay_domain is present then set to intermediary.hostname, if relay_ip is present then merged to intermediary.ip.
kv_msg1.size
network.sent_bytes
Converted to unsigned integer.
kv_msg1.stat
security_result.summary
kv_msg1.verify
security_result.description, security_result.action
If kv_msg1.verify is FAIL then security_result.action set to BLOCK.
kv_msg1.version
network.tls.version
labels.log_type
metadata.product_event_type
labels.net.host.ip
principal.ip, principal.asset.ip
labels.net.host.port
principal.port
labels.net.peer.ip
target.ip, target.asset.ip
labels.net.peer.port
target.port
labels.net.transport
network.ip_protocol
If labels.net.transport is TCP then TCP.
level
security_result.severity
If level is INFO/Informational/DEBUG/info/Information then INFORMATIONAL, if level is ERROR/error then ERROR, if level is WARNING then LOW.
log.file.path
target.process.file.full_path
logName
security_result.category_details
Logon Account
principal.user.userid
Logon Type
extensions.auth.mechanism
If logon_type is 2/Interactive then INTERACTIVE, if logon_type is 3/8 then NETWORK, if logon_type is 4 then BATCH, if logon_type is 5 then SERVICE, if logon_type is 7 then UNLOCK, if logon_type is 9 then NEW_CREDENTIALS, if logon_type is 10 then REMOTE_INTERACTIVE, if logon_type is 11 then CACHED_INTERACTIVE, else MECHANISM_UNSPECIFIED.
mail_from
network.email.from
If mail_from does not contain @ then appended with @local.
mail_to
network.email.to
If mail_to does not contain @ then appended with @local.
message
Parsed with grok patterns.
namespace
principal.namespace
port
target.port
Converted to integer.
process_id
target.process.pid
providername
principal.application
Relative Target Name
target.file.full_path
resource.labels.project_id
src.cloud.project.id
resource.type
src.labels
response_status
network.http.response_code
Converted to integer.
sec_desc
security_result.description
Security ID
target.user.windows_sid
security_result_action_detail
security_result.action_details
server_name
target.hostname, target.asset.hostname
Share Name
target.resource.name
Source Network Address
principal.ip, principal.asset.ip
Parsed as IP.
Source Port
principal.port
Converted to integer.
summary
security_result.summary
target_host
target.hostname, target.asset.hostname
target_url
target.url
target_userid
target.user.userid
time
timestamp
Parsed as HH:mm:ss and merged with date as yyyy-MM-dd HH:mm:ss to when, parsed as date.
upn_name
intermediary.url
URL
target.url
User ID
target.user.windows_sid
user_id
principal.user.userid
UserAgent
network.http.user_agent
metadata.event_type
Set to STATUS_UPDATE if msg contains API_HEALTH. or JobDispatcher, set to USER_LOGIN if msg contains logged in as and target_userid is not empty, set to SCAN_HOST if msg contains Leave Validate., set to NETWORK_UNCATEGORIZED if msg contains Getting IP Address from host, set to RESOURCE_WRITTEN if msg contains Wrote vpxd health, set to NETWORK_HTTP if has_principal and has_target are true and application_protocol is not empty, set to PROCESS_LAUNCH if process_id and cmd are not empty, set to USER_UNCATEGORIZED if user_id is not empty or eventid is 4776, set to USER_LOGIN if eventid is 4624/4768/4769, set to USER_LOGOUT if eventid is 4634/4647, set to USER_RESOURCE_ACCESS if eventid is 5145, set to STATUS_UPDATE if host_name is not empty, set to GENERIC_EVENT otherwise.
extensions.auth.type
Set to MACHINE if eventid is 4624/4768/4769.
metadata.log_type
Set to VMWARE_VCENTER.
metadata.vendor_name
Set to VMWARE.
metadata.product_name
Set to VCENTER.
security_result.action
Set to ALLOW if response_status is 200 or action is Allow.
Need more help?
Get answers from Community members and Google SecOps professionals.
