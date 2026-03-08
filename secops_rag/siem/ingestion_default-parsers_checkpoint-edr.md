# Collect Check Point EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-edr/  
**Scraped:** 2026-03-05T09:20:59.422104Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Check Point EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest Check Point Antivirus logs to
Google Security Operations using Bindplane. The parser handles logs from Check Point
SandBlast, converting both SYSLOG + KV and SYSLOG + CEF formatted logs into the
Unified Data Model (UDM). The parser extracts fields from CEF messages using
included modules and maps them to UDM fields, handling various event types and
enriching the data with additional context from the raw logs. For non-CEF
messages, the parser uses key-value extraction, grok patterns, and conditional
logic to map relevant fields to the EDR UDM schema.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Check Point Appliance with SandBlast
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
'CHECKPOINT_EDR'
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
Restart the BindPlane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog in Checkpoint 1500 Appliance Series
Sign in to the
Checkpoint Appliance
.
Go to
Logs & Monitoring
>
Log Servers
>
Syslog Servers
.
Click
Configure
.
Provide the following configuration details:
Protocol
: Select
UDP
.
Name
: Enter a descriptive name.
IP Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Select
Enable
log server.
Select logs to forward: Both system and security logs.
Click
Apply
.
UDM mapping table
Log Field
UDM Mapping
Logic
action
event.idm.read_only_udm.security_result.action
Directly mapped from the
action
CEF field.
action_comment
event.idm.read_only_udm.additional.fields[<N>].key
:
action_comment
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
action_comment
Directly mapped from the
action_comment
field.
action_details
event.idm.read_only_udm.security_result.action_details
Directly mapped from the
action_details
CEF field.
additional_info
event.idm.read_only_udm.additional.fields[<N>].key
:
additional_info
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
additional_info
Directly mapped from the
additional_info
field.
am_update_proxy
event.idm.read_only_udm.intermediary.domain.name
Directly mapped from the
am_update_proxy
field.
am_update_source
event.idm.read_only_udm.target.url
Directly mapped from the
am_update_source
field.
client_version
event.idm.read_only_udm.metadata.product_version
Directly mapped from the
client_version
field.
cn1
event.idm.read_only_udm.security_result.severity
Mapped from the
cn1
CEF field and converted to UDM severity values (CRITICAL, HIGH, MEDIUM, LOW, INFO).
cs1
event.idm.read_only_udm.additional.fields[<N>].key
:
Connectivity State
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
cs1
Directly mapped from the
cs1
field.
description
event.idm.read_only_udm.metadata.description
Directly mapped from the
description
CEF field.
deviceDirection
event.idm.read_only_udm.network.direction
Mapped from the
deviceDirection
field. A value of
0
is mapped to
INBOUND
, other values are not mapped.
deviceFacility
event.idm.read_only_udm.additional.fields[<N>].key
:
deviceFacility
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
deviceFacility
Directly mapped from the
deviceFacility
field.
dst
event.idm.read_only_udm.network.target.ip
Directly mapped from the
dst
field when
event_type
is
Firewall
.
engine_ver
event.idm.read_only_udm.additional.fields[<N>].key
:
engine_ver
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
engine_ver
Directly mapped from the
engine_ver
field.
ep_rule_id
event.idm.read_only_udm.firewall.firewall_rule_id
Directly mapped from the
ep_rule_id
field when
event_type
is
Firewall
.
event_type
event.idm.read_only_udm.metadata.product_event_type
Directly mapped from the
event_type
CEF field.
failed_updates
event.idm.read_only_udm.additional.fields[<N>].key
:
failed_updates
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
failed_updates
Directly mapped from the
failed_updates
field.
file_md5
event.idm.read_only_udm.source_file.hash_md5
Directly mapped from the
file_md5
field when
event_type
is
TE Event
.
file_name
event.idm.read_only_udm.source_file.file_name
Directly mapped from the
file_name
field when
event_type
is
TE Event
.
file_sha1
event.idm.read_only_udm.source_file.hash_sha1
Directly mapped from the
file_sha1
field when
event_type
is
TE Event
.
file_sha256
event.idm.read_only_udm.source_file.hash_sha256
Directly mapped from the
file_sha256
field when
event_type
is
TE Event
.
host_type
event.idm.read_only_udm.principal.asset.type
Mapped from the
host_type
field.
Desktop
is converted to
WORKSTATION
, then the value is uppercased.
ifdir
event.idm.read_only_udm.network.direction
Directly mapped from the
ifdir
field and uppercased when
event_type
is
Firewall
.
installed_products
event.idm.read_only_udm.principal.asset.software.name
Directly mapped from the
installed_products
field.
is_scanned
sec_res.detection_fields[<N>].key
:
is_scanned
sec_res.detection_fields[<N>].value
: Value of
is_scanned
Directly mapped from the
is_scanned
field.
local_time
event.idm.read_only_udm.additional.fields[<N>].key
:
local_time
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
local_time
Directly mapped from the
local_time
field.
log_type
event.idm.read_only_udm.metadata.log_type
Directly mapped from the
log_type
field.
loguid
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
loguid
field.
machine_guid
event.idm.read_only_udm.principal.asset.product_object_id
Directly mapped from the
machine_guid
field.
media_authorized
event.idm.read_only_udm.additional.fields[<N>].key
:
media_authorized
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
media_authorized
Directly mapped from the
media_authorized
field.
media_class_id
event.idm.read_only_udm.additional.fields[<N>].key
:
media_class_id
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
media_class_id
Directly mapped from the
media_class_id
field.
media_description
event.idm.read_only_udm.additional.fields[<N>].key
:
media_description
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
media_description
Directly mapped from the
media_description
field.
media_encrypted
event.idm.read_only_udm.additional.fields[<N>].key
:
media_encrypted
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
media_encrypted
Directly mapped from the
media_encrypted
field.
media_manufacturer
event.idm.read_only_udm.additional.fields[<N>].key
:
media_manufacturer
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
media_manufacturer
Directly mapped from the
media_manufacturer
field.
media_type
event.idm.read_only_udm.additional.fields[<N>].key
:
media_type
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
media_type
Directly mapped from the
media_type
field.
msg
event.idm.read_only_udm.metadata.description
Directly mapped from the
msg
CEF field.
origin
event.idm.read_only_udm.about.ip
Directly mapped from the
origin
CEF field.
os_name
event.idm.read_only_udm.additional.fields[<N>].key
:
os_name
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
os_name
Directly mapped from the
os_name
field.
os_version
event.idm.read_only_udm.principal.asset.platform_software.platform_version
Directly mapped from the
os_version
field.
policy_date
event.idm.read_only_udm.additional.fields[<N>].key
:
policy_date
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
policy_date
Directly mapped from the
policy_date
field.
policy_guid
event.idm.read_only_udm.principal.resource.product_object_id
Directly mapped from the
policy_guid
field.
policy_name
event.idm.read_only_udm.principal.resource.name
Directly mapped from the
policy_name
field.
policy_number
event.idm.read_only_udm.principal.resource.product_object_id
Directly mapped from the
policy_number
field.
policy_type
event.idm.read_only_udm.additional.fields[<N>].key
:
policy_type
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
policy_type
Directly mapped from the
policy_type
field.
policy_version
event.idm.read_only_udm.additional.fields[<N>].key
:
policy_version
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
policy_version
Directly mapped from the
policy_version
field.
product
event.idm.read_only_udm.metadata.product_name
Directly mapped from the
product
CEF field.
proto
event.idm.read_only_udm.network.protocol
Directly mapped from the
proto
field when
event_type
is
Firewall
.
reading_data_access
event.idm.read_only_udm.additional.fields[<N>].key
:
reading_data_access
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
reading_data_access
Directly mapped from the
reading_data_access
field.
requestClientApplication
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the
requestClientApplication
field.
result
event.idm.read_only_udm.security_result.summary
Directly mapped from the
result
field.
rt
event.idm.read_only_udm.metadata.event_timestamp.seconds
Mapped from the
rt
field, divided by 1000, and the integer part is taken as seconds.
rule_name
event.idm.read_only_udm.firewall.firewall_rule
Directly mapped from the
rule_name
field when
event_type
is
Firewall
.
s_port
event.idm.read_only_udm.network.client.port
Directly mapped from the
s_port
field when
event_type
is
Firewall
.
sequencenum
event.idm.read_only_udm.additional.fields[<N>].key
:
sequencenum
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
sequencenum
Directly mapped from the
sequencenum
field.
service
event.idm.read_only_udm.network.target.port
Directly mapped from the
service
field when
event_type
is
Firewall
.
severity
event.idm.read_only_udm.security_result.severity
Mapped from the
severity
field and converted to UDM severity values (CRITICAL, HIGH, MEDIUM, LOW, INFO).
shost
event.idm.read_only_udm.principal.hostname
Directly mapped from the
shost
CEF field.
sig_ver
event.idm.read_only_udm.additional.fields[<N>].key
:
sig_ver
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
sig_ver
Directly mapped from the
sig_ver
field.
src
event.idm.read_only_udm.principal.ip
Directly mapped from the
src
CEF field.
src_machine_name
event.idm.read_only_udm.principal.hostname
Directly mapped from the
src_machine_name
field when
event_type
is empty.
subject
event.idm.read_only_udm.task.task_name
Directly mapped from the
subject
field when
event_type
is empty.
suser
event.idm.read_only_udm.principal.user.user_display_name
Directly mapped from the
suser
CEF field.
time
event.idm.read_only_udm.metadata.event_timestamp.seconds
Directly mapped from the
time
field and converted to Unix epoch seconds.
user_name
event.idm.read_only_udm.principal.user.email_addresses
Directly mapped from the
user_name
CEF field.
user_sid
event.idm.read_only_udm.principal.user.windows_sid
Directly mapped from the
user_sid
field.
version
event.idm.read_only_udm.additional.fields[<N>].key
:
version
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
version
Directly mapped from the
version
field.
writing_data_access
event.idm.read_only_udm.additional.fields[<N>].key
:
writing_data_access
event.idm.read_only_udm.additional.fields[<N>].value.string_value
: Value of
writing_data_access
Directly mapped from the
writing_data_access
field.
N/A
event.idm.read_only_udm.metadata.event_type
Set to
GENERIC_EVENT
if none of
principal.ip
,
principal.hostname
, or
principal.mac
are present in the raw log, otherwise set to
STATUS_UPDATE
.
N/A
event.idm.read_only_udm.metadata.vendor_name
Constant value:
Check Point
.
N/A
event.idm.read_only_udm.metadata.log_type
Constant value:
CHECKPOINT_EDR
.
N/A
event.idm.read_only_udm.principal.asset.platform_software.platform
Set to
WINDOWS
if
os_name
contains
WINDOWS
or
Windows
.
N/A
event.idm.read_only_udm.network.http.user_agent
Set to
Check Point Endpoint Security Client
if
requestClientApplication
is present.
N/A
event.edr.data_source
Constant value:
CHECKPOINT_SANDBLAST
when
message
doesn't contain
CEF
.
Need more help?
Get answers from Community members and Google SecOps professionals.
