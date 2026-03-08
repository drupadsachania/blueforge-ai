# Collect Symantec CloudSOC CASB logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-casb/  
**Scraped:** 2026-03-05T10:00:40.122911Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec CloudSOC CASB logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec CloudSOC logs to
Google Security Operations using Bindplane. The parser extracts logs from syslog or
JSON formatted messages. It performs several key operations: parsing the message
field, converting the message to JSON if necessary, extracting fields, mapping
them to the Unified Data Model (UDM), and enriching the event with additional
context like timestamps and security result details. The parser also handles
various log formats and performs specific actions based on the
activity_type
field to categorize the event correctly.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Symantec CloudSOC
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
'SYMANTEC_CASB'
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
Configure Syslog in Symantec CASB
Sign in to your
Symantec CloudSOC
host.
Run the following command to identify which logger the system uses:
ls
–d
/etc/*syslog*
Go to the corresponding section, according to the response for the previous command:
syslog.conf
: Legacy Syslog.
syslog-ng.conf
: Syslog-ng.
Legacy Syslog configuration
Open the
syslogd
file, typically located in
/etc/default
directory using the
vi
editor.
vi
/etc/default/syslogd
Make sure
SYSLOGD
value contains the
-r
flag.
SYSLOGD="-r"
Save the file and exit the editor:
Switch to
command mode
by pressing the
Esc
key.
Press
:
(colon) to open the prompt bar.
Type
wq
after the colon and press
Enter
.
Open
services
file, typically located in the
/etc
directory using the
vi
editor.
vi
/etc/services
Edit the port value for syslog service:
syslog 514/udp
Save the file and exit the editor:
Switch to
command mode
by pressing the
Esc
key.
Press
:
(colon) to open the prompt bar.
Type
wq
after the colon and press
Enter
.
Open the
syslog.conf
file, typically located in the
/etc
directory using the
vi
editor.
vi
/etc/syslog.conf
Update the configuration to forward all logs to Google SecOps.
*.* @bindplane_agent_host
Save the file and exit the editor:
Switch to
command mode
by pressing the
Esc
key.
Press
:
(colon) to open the prompt bar.
Type
wq
after the colon and press
Enter
.
Open the
hosts
file, typically located in the
/etc
directory using the
vi
editor.
vi
/etc/hosts
Create a local DNS entry for
bindplane_agent_host
.
0.0.0.0 bindplane_agent_host
Save the file and exit the editor:
Switch to
command mode
by pressing the
Esc
key.
Press
:
(colon) to open the prompt bar.
Type
wq
after the colon and press
Enter
.
Restart the syslog daemon service.
Syslog-ng configuration
Open the
syslog-ng.conf
file, typically located in the
/etc
directory using the
vi
editor.
vi
/etc/syslog-ng.conf
Add the following code to the end of the file:
destination d____ { udp("bindplane_agent_host" port(514));}; log {source(s_src);
destination(d____);};
Open the
hosts
file, typically located in the
/etc
directory using the
vi
editor.
vi
/etc/hosts
Create a local DNS entry for
bindplane_agent_host
.
0.0.0.0 bindplane_agent_host
Save the file and exit the editor:
Switch to
command mode
by pressing the
Esc
key.
Press
:
(colon) to open the prompt bar.
Type
wq
after the colon and press
Enter
.
Restart the syslog-ng daemon service.
UDM mapping table
Log Field
UDM Mapping
Logic
_domain
target.hostname
The value of the
_domain
field
_domain
target.asset.hostname
The value of the
_domain
field
_id
metadata.product_log_id
The value of the
_id
field
actions_taken
security_result.detection_fields[].value
The value of the
actions_taken
field. Key is dynamically generated as
Action_
+ index.
activity_type
metadata.product_event_type
The value of the
activity_type
field if
product_data.activity_type
is empty, or the value of
product_data.activity_type
if it's not empty.
collector_device_ip
principal.ip
The value of the
collector_device_ip
field, if not
Unknown IP
.
collector_device_ip
principal.asset.ip
The value of the
collector_device_ip
field, if not
Unknown IP
.
collector_device_name
principal.hostname
The value of the
collector_device_name
field.
collector_device_name
principal.asset.hostname
The value of the
collector_device_name
field.
content_checks.dlp.raw_response.contentdetails[].contentBlockId
security_result.detection_fields[].value
The value of
content_checks.dlp.raw_response.contentdetails[].contentBlockId
. Key is dynamically generated as
contentBlockId_
+ index.
content_checks.dlp.raw_response.contentdetails[].topLevelFileType
security_result.detection_fields[].value
The value of
content_checks.dlp.raw_response.contentdetails[].topLevelFileType
. Key is dynamically generated as
topLevelFileType_
+ index.
content_checks.dlp.raw_response.requestid
security_result.detection_fields[].value
The value of
content_checks.dlp.raw_response.requestid
. Key is
Request ID
.
content_checks.dlp.raw_response.responseaction
security_result.detection_fields[].value
The value of
content_checks.dlp.raw_response.responseaction
. Key is
Response Action
.
content_checks.dlp.raw_response.violation[].name
security_result.detection_fields[].value
The value of
content_checks.dlp.raw_response.violation[].name
. Key is dynamically generated as
Violation_Policy_Name_
+ index.
content_checks.dlp.raw_response.violation[].policyId
security_result.detection_fields[].value
The value of
content_checks.dlp.raw_response.violation[].policyId
. Key is dynamically generated as
Violation_Policy_ID_
+ index.
content_checks.dlp.updated_timestamp
additional.fields[].value.string_value
The value of
content_checks.dlp.updated_timestamp
. Key is
Updated TimeStamp
.
content_checks.filename
target.file.full_path
The value of
content_checks.filename
.
content_checks.mimetype
target.file.mime_type
The value of
content_checks.mimetype
.
content_checks.risktype_list[]
security_result.detection_fields[].value
The value of
content_checks.risktype_list[]
. Key is dynamically generated as
RiskType_
+ index.
content_checks.vba_macros.expressions[].values[].key
security_result.detection_fields[].key
The value of
content_checks.vba_macros.expressions[].values[].key
concatenated with indexes.
content_checks.vba_macros.expressions[].values[].value
security_result.detection_fields[].value
The value of
content_checks.vba_macros.expressions[].values[].value
.
content_checks.vk_content_iq_violations[]
security_result.detection_fields[].value
The value of
content_checks.vk_content_iq_violations[]
. Key is dynamically generated as
content_violation_
+ index.
content_checks.vk_dlp_policy_violations[]
security_result.detection_fields[].value
The value of
content_checks.vk_dlp_policy_violations[]
. Key is dynamically generated as
dlp_policy_violation_
+ index.
content_checks.vk_encryption
security_result.detection_fields[].value
The value of
content_checks.vk_encryption
. Key is
vk_encryption
.
content_checks.vk_glba
security_result.detection_fields[].value
The value of
content_checks.vk_glba
. Key is
vk_glba
.
content_checks.vk_hipaa
security_result.detection_fields[].value
The value of
content_checks.vk_hipaa
. Key is
vk_hipaa
.
content_checks.vk_pci
security_result.detection_fields[].value
The value of
content_checks.vk_pci
. Key is
vk_pci
.
content_checks.vk_pii
security_result.detection_fields[].value
The value of
content_checks.vk_pii
. Key is
vk_pii
.
content_checks.vk_source_code
security_result.detection_fields[].value
The value of
content_checks.vk_source_code
. Key is
vk_source_code
.
content_checks.vk_vba_macros
security_result.detection_fields[].value
The value of
content_checks.vk_vba_macros
. Key is
vk_vba_macros
.
content_checks.vk_virus
security_result.detection_fields[].value
The value of
content_checks.vk_virus
. Key is
vk_virus
.
content_checks.violations
security_result.detection_fields[].value
The value of
content_checks.violations
. Key is
violations
.
created_timestamp
additional.fields[].value.string_value
The value of
created_timestamp
. Key is
Created TimeStamp
.
date
metadata.event_timestamp.seconds
Epoch seconds extracted from the
date
field.
device_ip
target.ip
The value of the
device_ip
field, if not
Unknown IP
.
device_ip
target.asset.ip
The value of the
device_ip
field, if not
Unknown IP
.
file_size
target.file.size
The value of
file_size
or
product_data.file_size
if the former is empty. Converted to unsigned integer.
file_url
target.file.full_path
The value of
product_data.file_url
.
group_name
target.group.group_display_name
The display name extracted from the
group_name
field.
hosts[]
principal.ip
The values of the
hosts
field, split by comma.
inserted_timestamp
additional.fields[].value.string_value
The value of
inserted_timestamp
. Key is
Inserted TimeStamp
.
instance
principal.hostname
The first value of the
instance
field if it's an array, or the value of the
instance
field if it's a string.
instance
principal.asset.hostname
The first value of the
instance
field if it's an array, or the value of the
instance
field if it's a string.
ioi_code
security_result.summary
The value of the
ioi_code
field.
_latency
security_result.detection_fields[].value
The value of the
_latency
field. Key is
Latency
.
locations
security_result.detection_fields[].value
The value of the
locations
field. Key is
Locations
.
log_name
intermediary.asset.asset_id
The log ID extracted from the
log_name
field, prefixed with
logid:
.
mailbox_owner
target.user.userid
The value of
product_data.mailbox owner
.
metadata.log_type
metadata.log_type
Hardcoded to
SYMANTEC_CASB
.
metadata.product_name
metadata.product_name
Hardcoded to
SYMANTEC_CASB
.
metadata.vendor_name
metadata.vendor_name
Hardcoded to
SYMANTEC
.
msg
metadata.description
The value of the
msg
field or the
message
field if
msg
is not present.
name
security_result.detection_fields[].value
The value of the
name
field. Key is
Name
.
object_name
security_result.detection_fields[].value
The value of the
object_name
field. Key is
Object Name
.
object_type
target.resource.name
The value of the
object_type
field.
org_unit
security_result.detection_fields[].value
The value of the
org_unit
field. Key is
org_unit ID
.
policy_action
security_result.action_details
The value of the
policy_action
field.
policy_type
security_result.detection_fields[].value
The value of the
policy_type
field. Key is
policy_type
.
policy_violated
security_result.detection_fields[].value
The value of the
policy_violated
field. Key is
policy_violated
.
product_data._domain
target.hostname
The value of
product_data._domain
.
product_data._domain
target.asset.hostname
The value of
product_data._domain
.
product_data.activity_type
metadata.product_event_type
The value of
product_data.activity_type
.
product_data.file url
target.file.full_path
The value of
product_data.file url
.
product_data.file_size
target.file.size
The value of
product_data.file_size
.
product_data.group
target.group.group_display_name
The value of
product_data.group
.
product_data.location
principal.location.country_or_region
The value of
product_data.location
.
product_data.logon error
security_result.summary
The value of
product_data.logon error
.
product_data.mailbox owner
target.user.userid
The value of
product_data.mailbox owner
.
product_data.name
target.file.full_path
The value of
product_data.name
.
product_data.object_name
target.file.full_path
The value of
product_data.object_name
.
product_data.originatingserver
product_data.service
target.application
The value of
product_data.service
.
product_data.site url
target.url
The value of
product_data.site url
.
product_data.target
target.user.userid
The value of
product_data.target
.
product_data.useragent
network.http.user_agent
The value of
product_data.useragent
.
product_name
intermediary.application
The value of the
product_name
field.
product_uid
metadata.product_name
The value of the
product_uid
field.
responsible_logs
additional.fields[].value.string_value
The value of the
responsible_logs
field. Key is
responsible_logs
.
resource_id
target.resource.product_object_id
The value of the
resource_id
field.
risks
security_result.detection_fields[].value
The value of the
risks
field. Key is
Risks
.
security_result.action
security_result.action
Derived from
product_data.logon error
. Set to
BLOCK
if
product_data.logon error
is
BlockedByConditionalAccess
.
security_result.severity
security_result.severity
The uppercase value of the
severity
field, if it's one of the supported severity levels.
security_result.severity_details
security_result.severity_details
The value of the
severity
field, if it's not one of the supported severity levels.
security_result.summary
security_result.summary
The value of the
ioi_code
field or
product_data.logon error
if
ioi_code
is not present.
service
target.application
The value of the
service
field if
product_data.service
is empty.
site_url
target.url
The value of
product_data.site url
.
source
principal.resource.attribute.labels[].value
The value of the
source
field. Key is
Source
.
sub_feature
additional.fields[].value.string_value
The value of the
sub_feature
field. Key is
Sub Feature
.
target.application
target.application
Derived based on
product_data.activity_type
and presence of principal and target.
target.resource.name
target.resource.name
Derived based on
product_data.activity_type
and presence of principal and target.
threat_score
security_result.detection_fields[].value
The value of the
threat_score
field. Key is
Threat Score
.
transaction_id
security_result.detection_fields[].value
The value of the
transaction_id
field. Key is
Transaction ID
.
updated_timestamp
additional.fields[].value.string_value
The value of
updated_timestamp
or
content_checks.dlp.updated_timestamp
if the former is empty. Key is
Updated TimeStamp
.
user
principal.user.userid
The value of the
user
field.
user_email
target.user.userid
The value of the
user_email
field.
user_mail
target.user.userid
The value of the
user_mail
field extracted from the
msg
field.
user_name
principal.user.user_display_name
The value of the
user_name
field.
user_uid
principal.user.userid
or
target.user.userid
The value of the
user_uid
field. Mapped to
principal.user.userid
if
product_data.activity_type
is not
InvalidLogin
or
Login
, otherwise mapped to
target.user.userid
.
uuid
intermediary.asset.product_object_id
The value of the
uuid
field.
version
metadata.product_version
The value of the
version
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
