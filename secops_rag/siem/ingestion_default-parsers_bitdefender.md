# Collect Bitdefender logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitdefender/  
**Scraped:** 2026-03-05T09:20:29.658324Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Bitdefender logs
Supported in:
Google secops
SIEM
This parser extracts Bitdefender logs in CEF or CSV format, normalizes fields to the UDM, and performs specific actions based on the
event_name
and
module
fields. It handles various event types, such as file operations, network connections, process creation, and registry modifications, mapping relevant information to appropriate UDM fields and enriching the data with additional context from the raw logs.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have a Windows 2016 or later or Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Bitdefender.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
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
For
Windows installation
, run the following script:
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane is installed.
Edit the
config.yaml
file as follows:
receivers:
    tcplog:
        # Replace the below port <54525> and IP <0.0.0.0> with your specific values
        listen_address: "0.0.0.0:54525" 

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        # Adjust the creds location below according the placement of the credentials file you downloaded
        creds: '{ json file for creds }'
        # Replace <customer_id> below with your actual ID that you copied
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        # You can apply ingestion labels below as preferred
        ingestion_labels:
        log_type: SYSLOG
        namespace: bitdefender
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes:
sudo
systemctl
restart
bindplane
Configure Syslog Streaming in Bitdefender GravityZone
Sign in to the GravityZone Control Center.
Go to
Configuration
>
Integrations
>
Syslog
.
Click
Add Syslog Server
.
Provide the required details:
Name
: provide a unique name for the syslog server (for example,
CentralSyslog
).
IP Address/Hostname
: enter the IP address or hostname of the Bindplane server.
Protocol
: select the protocol to use:
TCP
/
UDP
.
Port
: specify the port number of the Bindplane server.
Select the
log types
to stream (for example,
Antimalware Events
,
Network Attack Defense (NAD) Events
,
Web Control Events
,
Firewall Events
, or
Policy Changes
).
Optional: configure
filters
to include or exclude specific event types.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
BitdefenderGZAttackEntry
security_result.detection_fields.value
The value of
BitdefenderGZAttackEntry
from the raw log is assigned as a value to a
security_result.detection_fields
object where the key is "attack_entry".
BitdefenderGZAttackTypes
security_result.category_details
The value of
BitdefenderGZAttackTypes
from the raw log is assigned to
security_result.category_details
. The value is then split into individual strings and each string is added as a value to the
security_result.category_details
array.
BitdefenderGZAttCkId
security_result.detection_fields.value
The value of
BitdefenderGZAttCkId
from the raw log is assigned as a value to a
security_result.detection_fields
object where the key is "BitdefenderGZAttCkId".
BitdefenderGZCompanyId
target.user.company_name
The value of
BitdefenderGZCompanyId
from the raw log is assigned to
target.user.company_name
.
BitdefenderGZComputerFQDN
principal.asset.network_domain
The value of
BitdefenderGZComputerFQDN
from the raw log is assigned to
principal.asset.network_domain
.
BitdefenderGZDetectionName
security_result.threat_name
The value of
BitdefenderGZDetectionName
from the raw log is assigned to
security_result.threat_name
.
BitdefenderGZEndpointId
security_result.detection_fields.value
The value of
BitdefenderGZEndpointId
from the raw log is assigned as a value to a
security_result.detection_fields
object where the key is "BitdefenderGZEndpointId".
BitdefenderGZIncidentId
metadata.product_log_id
The value of
BitdefenderGZIncidentId
from the raw log is assigned to
metadata.product_log_id
.
BitdefenderGZMainAction
security_result.action_details
The value of
BitdefenderGZMainAction
from the raw log is assigned to
security_result.action_details
. Based on this value, the
security_result.action
field is set (e.g., "blocked" maps to "BLOCK"). The
security_result.description
field is also populated with "main_action: " followed by the value of
BitdefenderGZMainAction
.
BitdefenderGZMalwareHash
principal.process.file.sha256
The value of
BitdefenderGZMalwareHash
from the raw log is assigned to
principal.process.file.sha256
.
BitdefenderGZMalwareName
security_result.threat_name
The value of
BitdefenderGZMalwareName
from the raw log is assigned to
security_result.threat_name
.
BitdefenderGZMalwareType
security_result.detection_fields.value
The value of
BitdefenderGZMalwareType
from the raw log is assigned as a value to a
security_result.detection_fields
object where the key is "malware_type".
BitdefenderGZModule
metadata.product_event_type
The value of
BitdefenderGZModule
from the raw log is assigned to
metadata.product_event_type
.
BitdefenderGZSeverityScore
security_result.severity_details
The value of
BitdefenderGZSeverityScore
from the raw log is assigned to
security_result.severity_details
.
BitdefenderGZHwId
target.resource.id
The value of
BitdefenderGZHwId
from the raw log is assigned to
target.resource.id
.
act
security_result.action_details
The value of
act
from the raw log is assigned to
security_result.action_details
.
actionTaken
security_result.action_details
The value of
actionTaken
from the raw log is assigned to
security_result.action_details
. Based on this value, the
security_result.action
field is set (e.g., "block" maps to "BLOCK"). The
security_result.description
field is also populated with "actionTaken: " followed by the value of
actionTaken
.
additional.fields
additional.fields
Parser logic creates a key/value pair for "product_installed" and adds it to the
additional.fields
object.
categories
principal.asset.category
The value of
categories
from the raw log is assigned to
principal.asset.category
.
cmd_line
target.process.command_line
The value of
cmd_line
from the raw log is assigned to
target.process.command_line
.
companyId
target.user.company_name
The value of
companyId
from the raw log is assigned to
target.user.company_name
.
computer_fqdn
principal.asset.network_domain
The value of
computer_fqdn
from the raw log is assigned to
principal.asset.network_domain
.
computer_id
principal.asset.asset_id
The value of
computer_id
from the raw log is assigned to
principal.asset.asset_id
after prepending "ComputerId:".
computer_ip
principal.asset.ip
The value of
computer_ip
from the raw log is parsed, split by commas, and each resulting IP address is added to the
principal.asset.ip
array.
computer_name
principal.resource.attribute.labels.value
The value of
computer_name
from the raw log is assigned as a value to a
principal.resource.attribute.labels
object where the key is "computer_name". It is also added as a value to a
security_result.detection_fields
object where the key is "computer_name".
column1
metadata.product_log_id
The value of
column1
from the raw log is assigned to
metadata.product_log_id
.
column3
observer.ip
The value of
column3
from the raw log is assigned to
observer.ip
.
command_line
target.process.command_line
The value of
command_line
from the raw log is assigned to
target.process.command_line
.
data
target.registry.registry_value_data
The value of
data
from the raw log is assigned to
target.registry.registry_value_data
.
detection_attackTechnique
security_result.detection_fields.value
The value of
detection_attackTechnique
from the raw log is assigned as a value to a
security_result.detection_fields
object where the key is "detection attackTechnique".
detection_name
security_result.threat_name
The value of
detection_name
from the raw log is assigned to
security_result.threat_name
.
destination_ip
target.ip
The value of
destination_ip
from the raw log is assigned to
target.ip
.
destination_port
target.port
The value of
destination_port
from the raw log is assigned to
target.port
.
direction
network.direction
The value of
direction
from the raw log is uppercased and assigned to
network.direction
.
dvc
principal.ip
The value of
dvc
from the raw log is parsed, split by commas, and each resulting IP address is added to the
principal.ip
array.
dvchost
about.hostname
The value of
dvchost
from the raw log is assigned to
about.hostname
.
event_description
metadata.description
The value of
event_description
from the raw log is assigned to
metadata.description
.
event_name
metadata.product_event_type
The value of
event_name
from the raw log is assigned to
metadata.product_event_type
.  If the value is "Antiphishing",
security_result.category
is set to "PHISHING". If the value is "AntiMalware",
security_result.category
is set to "SOFTWARE_MALICIOUS".  The
metadata.event_type
field is derived from
event_name
using a series of conditional statements within the parser.
ev
metadata.product_event_type
The value of
ev
from the raw log is assigned to
metadata.product_event_type
.
extra_info.command_line
target.process.command_line
The value of
extra_info.command_line
from the raw log is assigned to
target.process.command_line
.
extra_info.parent_pid
principal.process.pid
The value of
extra_info.parent_pid
from the raw log is assigned to
principal.process.pid
.
extra_info.parent_process_cmdline
principal.process.command_line
The value of
extra_info.parent_process_cmdline
from the raw log is assigned to
principal.process.command_line
.
extra_info.parent_process_path
principal.process.file.full_path
The value of
extra_info.parent_process_path
from the raw log is assigned to
principal.process.file.full_path
.
extra_info.pid
target.process.pid
The value of
extra_info.pid
from the raw log is assigned to
target.process.pid
.
extra_info.process_path
target.process.file.full_path
The value of
extra_info.process_path
from the raw log is assigned to
target.process.file.full_path
.
extra_info.user
target.user.userid
The value of
extra_info.user
from the raw log is assigned to
target.user.userid
.
filePath
principal.process.file.full_path
The value of
filePath
from the raw log is assigned to
principal.process.file.full_path
.
file_path
principal.process.file.full_path
The value of
file_path
from the raw log is assigned to
principal.process.file.full_path
.
final_status
security_result.action_details
The value of
final_status
from the raw log is assigned to
security_result.action_details
. Based on this value, the
security_result.action
field is set (e.g., "deleted" maps to "BLOCK", "ignored" to "ALLOW"). The
security_result.description
field is also populated with "final_status: " followed by the value of
final_status
. If the value is "deleted" or "blocked",
metadata.event_type
is set to "SCAN_NETWORK".
hash
principal.process.file.sha256
The value of
hash
from the raw log is assigned to
principal.process.file.sha256
.
host
principal.hostname
The value of
host
from the raw log is assigned to
principal.hostname
.
hostname
principal.hostname
The value of
hostname
from the raw log is assigned to
principal.hostname
if
event_name
is not "log_on" or "log_out". Otherwise, it is assigned to
target.hostname
.
host_name
principal.hostname
The value of
host_name
from the raw log is assigned to
principal.hostname
.
hwid
principal.resource.id
The value of
hwid
from the raw log is assigned to
principal.resource.id
if it's not empty. If it's empty and the event is not "log_on" or "log_out", the value of
source_hwid
is assigned to
principal.resource.id
. If the event is "log_on" or "log_out", it is assigned to
target.resource.id
.
incident_id
metadata.product_log_id
The value of
incident_id
from the raw log is assigned to
metadata.product_log_id
.
ip_dest
target.ip
The value of
ip_dest
from the raw log is assigned to
target.ip
.
ip_source
principal.ip
The value of
ip_source
from the raw log is assigned to
principal.ip
.
key_path
target.registry.registry_key
The value of
key_path
from the raw log is assigned to
target.registry.registry_key
.
local_port
principal.port
The value of
local_port
from the raw log is converted to an integer and assigned to
principal.port
.
logon_type
extensions.auth.mechanism
The value of
logon_type
from the raw log is used to determine the value of
extensions.auth.mechanism
. Different numeric values of
logon_type
map to different authentication mechanisms (e.g., 2 maps to "LOCAL", 3 to "NETWORK"). If no matching
logon_type
is found, the mechanism is set to "MECHANISM_UNSPECIFIED".
lurker_id
intermediary.resource.id
The value of
lurker_id
from the raw log is assigned to
intermediary.resource.id
.
main_action
security_result.action_details
The value of
main_action
from the raw log is assigned to
security_result.action_details
. Based on this value, the
security_result.action
field is set (e.g., "blocked" maps to "BLOCK", "no action" to "ALLOW"). The
security_result.description
field is also populated with "main_action: " followed by the value of
main_action
.
malware_name
security_result.threat_name
The value of
malware_name
from the raw log is assigned to
security_result.threat_name
.
malware_type
security_result.detection_fields.value
The value of
malware_type
from the raw log is assigned as a value to a
security_result.detection_fields
object where the key is "malware_type".
metadata.description
metadata.description
The parser sets the
metadata.description
field based on the
event_name
field.
metadata.event_type
metadata.event_type
The parser sets the
metadata.event_type
field based on the
event_name
field.
metadata.product_event_type
metadata.product_event_type
The parser sets the
metadata.product_event_type
field based on the
event_name
or
module
fields.
metadata.product_log_id
metadata.product_log_id
The parser sets the
metadata.product_log_id
field based on the
msg_id
or
incident_id
fields.
metadata.product_name
metadata.product_name
The parser sets the
metadata.product_name
to "BitDefender EDR".
metadata.product_version
metadata.product_version
The parser renames the
product_version
field to
metadata.product_version
.
metadata.vendor_name
metadata.vendor_name
The parser sets the
metadata.vendor_name
to "BitDefender".
module
metadata.product_event_type
The value of
module
from the raw log is assigned to
metadata.product_event_type
. If the value is "new-incident" and
target_process_file_full_path
is not empty,
metadata.event_type
is set to "PROCESS_UNCATEGORIZED". If the value is "task-status",
metadata.event_type
is set to "STATUS_UPDATE". If the value is "network-monitor" or "fw",
metadata.event_type
is set to "SCAN_NETWORK".
msg_id
metadata.product_log_id
The value of
msg_id
from the raw log is assigned to
metadata.product_log_id
.
network.application_protocol
network.application_protocol
The value of
uc_type
from the raw log is uppercased and assigned to
network.application_protocol
.
network.direction
network.direction
The parser sets the
network.direction
field based on the
direction
field.
network.ip_protocol
network.ip_protocol
If
protocol_id
is "6", the parser sets the
network.ip_protocol
to "TCP".
new_path
target.file.full_path
The value of
new_path
from the raw log is assigned to
target.file.full_path
.
old_path
src.file.full_path
The value of
old_path
from the raw log is assigned to
src.file.full_path
.
origin_ip
intermediary.ip
The value of
origin_ip
from the raw log is assigned to
intermediary.ip
.
os
principal.platform_version
The value of
os
from the raw log is assigned to
principal.platform_version
. The
principal.platform
field is derived from
os
(e.g., "Win" maps to "WINDOWS"). If the event is "log_on" or "log_out", the
principal.platform
and
principal.platform_version
fields are renamed to
target.platform
and
target.platform_version
, respectively.
os_type
principal.platform
The value of
os_type
from the raw log is used to determine the value of
principal.platform
(e.g., "Win" maps to "WINDOWS").
parent_pid
principal.process.pid
The value of
parent_pid
from the raw log is assigned to
principal.process.pid
.
parent_process_path
principal.process.file.full_path
The value of
parent_process_path
from the raw log is assigned to
principal.process.file.full_path
.
parent_process_pid
principal.process.pid
The value of
parent_process_pid
from the raw log is assigned to
principal.process.pid
.
path
target.file.full_path
The value of
path
from the raw log is assigned to
target.file.full_path
.
pid
principal.process.pid
or
target.process.pid
The value of
pid
from the raw log is assigned to
principal.process.pid
if
event_name
starts with "file
" or "reg
", or if it's one of "process_signal", "network_connection", or "connection_connect". Otherwise, it is assigned to
target.process.pid
.
pid_path
principal.process.file.full_path
The value of
pid_path
from the raw log is assigned to
principal.process.file.full_path
.
port_dest
target.port
The value of
port_dest
from the raw log is converted to an integer and assigned to
target.port
.
port_source
principal.port
The value of
port_source
from the raw log is converted to an integer and assigned to
principal.port
.
ppid
principal.process.pid
The value of
ppid
from the raw log is assigned to
principal.process.pid
.
principal.ip
principal.ip
The parser sets the
principal.ip
field based on the
ip_source
or
dvc
fields.
principal.platform
principal.platform
The parser sets the
principal.platform
field based on the
os
or
os_type
fields.
principal.platform_version
principal.platform_version
The parser sets the
principal.platform_version
field based on the
os
or
osi_version
fields.
principal.process.command_line
principal.process.command_line
The parser sets the
principal.process.command_line
field based on the
parent_process_cmdline
field.
principal.process.file.full_path
principal.process.file.full_path
The parser sets the
principal.process.file.full_path
field based on the
pid_path
,
file_path
,
parent_process_path
, or
process_path
fields.
principal.process.file.md5
principal.process.file.md5
The parser renames the
file_hash_md5
field to
principal.process.file.md5
.
principal.process.file.sha256
principal.process.file.sha256
The parser sets the
principal.process.file.sha256
field based on the
hash
,
BitdefenderGZMalwareHash
, or
file_hash_sha256
fields.
principal.process.parent_process.pid
principal.process.parent_process.pid
The parser renames the
ppid
field to
principal.process.parent_process.pid
.
principal.process.pid
principal.process.pid
The parser sets the
principal.process.pid
field based on the
pid
,
parent_pid
,
ppid
, or
parent_process_pid
fields.
principal.resource.id
principal.resource.id
The parser sets the
principal.resource.id
field based on the
hwid
or
source_hwid
fields.
principal.url
principal.url
The parser sets the
principal.url
field based on the
url
field.
process_command_line
target.process.command_line
The value of
process_command_line
from the raw log is assigned to
target.process.command_line
.
process_path
principal.process.file.full_path
or
target.process.file.full_path
The value of
process_path
from the raw log is assigned to
principal.process.file.full_path
if
event_name
is "network_connection" or "connection_connect". Otherwise, it is assigned to
target.process.file.full_path
.
product_installed
additional.fields.value.string_value
The value of
product_installed
from the raw log is assigned as a value to an
additional.fields
object where the key is "product_installed".
product_version
metadata.product_version
The value of
product_version
from the raw log is assigned to
metadata.product_version
.
protocol_id
network.ip_protocol
If
protocol_id
is "6", the parser sets the
network.ip_protocol
to "TCP".
request
target.url
The value of
request
from the raw log is assigned to
target.url
.
security_result.action
security_result.action
The parser sets the
security_result.action
field based on the
main_action
,
actionTaken
,
status
, or
final_status
fields. If none of these fields provide a valid action, it defaults to "UNKNOWN_ACTION".
security_result.action_details
security_result.action_details
The parser sets the
security_result.action_details
field based on the
main_action
,
actionTaken
,
status
, or
final_status
fields.
security_result.category
security_result.category
The parser sets the
security_result.category
field to "PHISHING" if
event_name
is "Antiphishing", to "SOFTWARE_MALICIOUS" if
event_name
is "AntiMalware", or merges the value from the
sec_category
field.
security_result.category_details
security_result.category_details
The parser sets the
security_result.category_details
field based on the
block_type
or
attack_types
fields.
security_result.detection_fields
security_result.detection_fields
The parser creates
security_result.detection_fields
objects for various fields, including "malware_type", "attack_entry", "BitdefenderGZAttCkId", "BitdefenderGZEndpointId", "final_status", "detection attackTechnique", and "computer_name".
security_result.description
security_result.description
The parser sets the
security_result.description
field based on the
main_action
,
actionTaken
, or
final_status
fields.
security_result.severity
security_result.severity
The parser sets the
security_result.severity
field based on the uppercased value of the
severity
field if it's not empty and the
module
is "new-incident".
security_result.severity_details
security_result.severity_details
The parser sets the
security_result.severity_details
field based on the
severity_score
field.
security_result.threat_name
security_result.threat_name
The parser sets the
security_result.threat_name
field based on the
malware_name
or
detection_name
fields.
severity
security_result.severity
The value of
severity
from the raw log is uppercased and assigned to
security_result.severity
if it's not empty and the
module
is "new-incident".
severity_score
security_result.severity_details
The value of
severity_score
from the raw log is converted to a string and assigned to
security_result.severity_details
.
source_host
observer.ip
The value of
source_host
from the raw log is assigned to
observer.ip
.
source_hwid
principal.resource.id
The value of
source_hwid
from the raw log is assigned to
principal.resource.id
.
source_ip
src.ip
The value of
source_ip
from the raw log is assigned to
src.ip
.
source_port
principal.port
The value of
source_port
from the raw log is converted to an integer and assigned to
principal.port
.
spt
principal.port
The value of
spt
from the raw log is assigned to
principal.port
.
sproc
principal.process.command_line
The value of
sproc
from the raw log is assigned to
principal.process.command_line
.
src
principal.ip
The value of
src
from the raw log is assigned to
principal.ip
.
src.ip
src.ip
The parser sets the
src.ip
field based on the
source_ip
field.
src.file.full_path
src.file.full_path
The parser sets the
src.file.full_path
field based on the
old_path
field.
status
security_result.action_details
The value of
status
from the raw log is assigned to
security_result.action_details
. Based on this value, the
security_result.action
field is set (e.g., "portscan_blocked" and "uc_site_blocked" map to "BLOCK"). The
security_result.description
field is also populated with "status: " followed by the value of
status
.
suid
principal.user.userid
The value of
suid
from the raw log is assigned to
principal.user.userid
.
suser
principal.user.user_display_name
The value of
suser
from the raw log is assigned to
principal.user.user_display_name
.
target.file.full_path
target.file.full_path
The parser sets the
target.file.full_path
field based on the
path
or
new_path
fields.
target.hostname
target.hostname
The parser sets the
target.hostname
field based on the
hostname
field.
target.ip
target.ip
The parser sets the
target.ip
field based on the
ip_dest
or
destination_ip
fields.
target.platform
target.platform
The parser sets the
target.platform
field based on the
principal.platform
field.
target.platform_version
target.platform_version
The parser sets the
target.platform_version
field based on the
principal.platform_version
field.
target.port
target.port
The parser sets the
target.port
field based on the
port_dest
or
destination_port
fields.
target.process.command_line
target.process.command_line
The parser sets the
target.process.command_line
field based on the
command_line
,
process_command_line
, or
cmd_line
fields.
target.process.file.full_path
target.process.file.full_path
The parser sets the
target.process.file.full_path
field based on the
process_path
field.
target.process.pid
target.process.pid
The parser sets the
target.process.pid
field based on the
pid
field.
target.registry.registry_key
target.registry.registry_key
The parser sets the
target.registry.registry_key
field based on the
key_path
field.
target.registry.registry_value_data
target.registry.registry_value_data
The parser sets the
target.registry.registry_value_data
field based on the
data
field.
target.registry.registry_value_name
target.registry.registry_value_name
The parser sets the
target.registry.registry_value_name
field based on the
value
field.
target.resource.id
target.resource.id
The parser sets the
target.resource.id
field based on the
hwid
or
BitdefenderGZHwId
fields.
target.url
target.url
The parser sets the
target.url
field based on the
request
field.
target.user.company_name
target.user.company_name
The parser sets the
target.user.company_name
field based on the
companyId
field.
target.user.user_display_name
target.user.user_display_name
The parser sets the
target.user.user_display_name
field based on the
user.name
or
user.userName
fields.
target.user.userid
target.user.userid
The parser sets the
target.user.userid
field based on the
user_name
,
user
,
user.id
, or
extra_info.user
fields.
target_pid
target.process.pid
The value of
target_pid
from the raw log is assigned to
target.process.pid
.
timestamp
metadata.event_timestamp
The value of
timestamp
from the raw log is parsed and assigned to
metadata.event_timestamp
.
uc_type
network.application_protocol
The value of
uc_type
from the raw log is uppercased and assigned to
network.application_protocol
. If
target_user_userid
is not empty,
metadata.event_type
is set to "USER_UNCATEGORIZED". Otherwise, it's set to "STATUS_UPDATE".
url
principal.url
The value of
url
from the raw log is assigned to
principal.url
if it's not empty or "0.0.0.0".
user
target.user.userid
The value of
user
from the raw log is assigned to
target.user.userid
.
user.id
target.user.userid
The value of
user.id
from the raw log is assigned to
target.user.userid
.
user.name
target.user.user_display_name
The value of
user.name
from the raw log is assigned to
target.user.user_display_name
.
user.userName
target.user.user_display_name
The value of
user.userName
from the raw log is assigned to
target.user.user_display_name
.
user.userSid
principal.user.windows_sid
The value of
user.userSid
from the raw log is assigned to
principal.user.windows_sid
.
user_name
target.user.userid
The value of
user_name
from the raw log is assigned to
target.user.userid
.
value
target.registry.registry_value_data
or
target.registry.registry_value_name
The value of
value
from the raw log is assigned to
target.registry.registry_value_data
if
event_name
is "reg_delete_value". Otherwise, it is assigned to
target.registry.registry_value_name
.
Need more help?
Get answers from Community members and Google SecOps professionals.
