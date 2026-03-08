# Collect Check Point Harmony logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-harmony/  
**Scraped:** 2026-03-05T09:21:02.687379Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Check Point Harmony logs
Supported in:
Google secops
SIEM
This document explains how to ingest Check Point Harmony Email and
Collaboration (HEC) logs to Google Security Operations using Bindplane. This parser code
extracts key-value pairs from Check Point Harmony syslog messages and maps them
to a Unified Data Model (UDM). It first normalizes the message format, then
iteratively parses and maps fields to UDM categories like
principal
,
target
,
network
, and
security_result
, enriching the data for security analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Check Point Harmony HEC (Infinity Portal)
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
'CHECKPOINT_HARMONY'
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
Configure Syslog for Check Point Harmony HEC
Sign in to the
Infinity Portal
>
Harmony Email & Collaboration
web UI.
Go to
Settings
>
Monitoring
>
SIEM
.
Click
Add SIEM Server
.
Provide the following configuration details:
Host: Enter the Bindplane agent IP address.
Port: Enter the Bindplane agent port number.
Protocol: Select
UDP
.
(Optional) Token: Enter an optional tag to the logs.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.action_details
Directly mapped.
security_result.action
Mapped to ALLOW, BLOCK, ALLOW_WITH_MODIFICATION, or QUARANTINE based on the value of the action field.
additional_info
additional.fields.value.string_value
Directly mapped with key =
additional_info
.
analyzed_on
security_result.detection_fields.value
Directly mapped with key =
analyzed_on
.
client_name
additional.fields.value.string_value
Directly mapped with key =
client_name
.
client_version
intermediary.platform_version
Directly mapped.
confidence_level
security_result.detection_fields.value
Directly mapped with key =
confidence_level
.
security_result.confidence
Mapped to UNKNOWN_CONFIDENCE, LOW_CONFIDENCE, MEDIUM_CONFIDENCE, or HIGH_CONFIDENCE based on the value of the confidence_level field.
description
security_result.description
Directly mapped.
dst
target.ip
Directly mapped.
dst_dns_name
security_result.detection_fields.value
Directly mapped with key =
dst_dns_name
.
dst_machine_name
security_result.detection_fields.value
Directly mapped with key =
dst_machine_name
.
target.asset.hostname
Directly mapped.
target.hostname
Directly mapped.
dst_user_dn
security_result.detection_fields.value
Directly mapped with key =
dst_user_dn
.
dst_user_name
target.user.userid
Directly mapped.
ep_rule_id
security_result.rule_id
Directly mapped if rule_uid is empty.
errors
security_result.summary
Directly mapped.
event_type
metadata.product_event_type
Directly mapped.
file_md5
target.process.file.md5
Directly mapped if the value is a valid MD5 hash and not all zeros.
target.file.md5
Directly mapped if the value is a valid MD5 hash and not all zeros.
file_name
target.process.file.full_path
Directly mapped.
file_sha1
target.process.file.sha1
Directly mapped if the value is a valid SHA-1 hash and not all zeros.
target.file.sha1
Directly mapped if the value is a valid SHA-1 hash and not all zeros.
file_sha256
target.process.file.sha256
Directly mapped if the value is a valid SHA256 hash and not all zeros.
target.file.sha256
Directly mapped if the value is a valid SHA256 hash and not all zeros.
file_size
target.file.size
Directly mapped.
file_type
target.file.file_type
Mapped to FILE_TYPE_ZIP, FILE_TYPE_DOS_EXE, FILE_TYPE_PDF, or FILE_TYPE_XLSX based on the value of the file_type field.
flags
additional.fields.value.string_value
Directly mapped with key =
flags
.
fw_subproduct
additional.fields.value.string_value
Directly mapped with key =
fw_subproduct
if product is empty.
metadata.product_name
Directly mapped if product is empty.
host_type
security_result.detection_fields.value
Directly mapped with key =
host_type
.
ifdir
network.direction
Directly mapped after converting to uppercase.
ifname
security_result.detection_fields.value
Directly mapped with key =
ifname
.
installed_products
security_result.detection_fields.value
Directly mapped with key =
installed_products
.
is_scanned
security_result.detection_fields.value
Directly mapped with key =
is_scanned
.
layer_name
security_result.detection_fields.value
Directly mapped with key =
layer_name
.
security_result.rule_set_display_name
Directly mapped.
layer_uuid
security_result.detection_fields.value
Directly mapped with key =
layer_uuid
.
security_result.rule_set
Directly mapped.
loguid
metadata.product_log_id
Directly mapped.
machine_guid
principal.asset.attribute.labels.value
Directly mapped with key =
machine_guid
.
malware_action
security_result.detection_fields.value
Directly mapped with key =
malware_action
.
malware_family
security_result.detection_fields.value
Directly mapped with key =
malware_family
.
media_authorized
security_result.detection_fields.value
Directly mapped with key =
media_authorized
.
media_class_id
security_result.detection_fields.value
Directly mapped with key =
media_class_id
.
media_description
security_result.detection_fields.value
Directly mapped with key =
media_description
.
media_encrypted
security_result.detection_fields.value
Directly mapped with key =
media_encrypted
.
media_manufacturer
security_result.detection_fields.value
Directly mapped with key =
media_manufacturer
.
media_type
security_result.detection_fields.value
Directly mapped with key =
media_type
.
methods
security_result.detection_fields.value
Directly mapped with key =
methods
.
originsicname
security_result.detection_fields.value
Directly mapped with key =
originsicname
.
origin
intermediary.ip
Directly mapped.
os_version
principal.asset.platform_software.platform_patch_level
Directly mapped.
outzone
security_result.detection_fields.value
Directly mapped with key =
outzone
.
parent_rule
security_result.detection_fields.value
Directly mapped with key =
parent_rule
.
peer_gateway
intermediary.ip
Directly mapped.
policy_guid
security_result.detection_fields.value
Directly mapped with key =
policy_guid
.
policy_name
security_result.detection_fields.value
Directly mapped with key =
policy_name
.
policy_number
security_result.detection_fields.value
Directly mapped with key =
policy_number
.
policy_type
security_result.detection_fields.value
Directly mapped with key =
policy_type
.
product
additional.fields.value.string_value
Directly mapped with key =
product
.
metadata.product_name
Directly mapped.
product_family
additional.fields.value.string_value
Directly mapped with key =
product_family
.
program_name
additional.fields.value.string_value
Directly mapped with key =
program_name
.
protection_name
security_result.detection_fields.value
Directly mapped with key =
protection_name
.
protection_type
security_result.detection_fields.value
Directly mapped with key =
protection_type
.
reading_data_access
security_result.detection_fields.value
Directly mapped with key =
reading_data_access
.
rule_action
security_result.detection_fields.value
Directly mapped with key =
rule_action
.
rule_name
security_result.rule_name
Directly mapped.
rule_uid
security_result.rule_id
Directly mapped if ep_rule_id is empty.
s_port
principal.port
Directly mapped.
scheme
security_result.detection_fields.value
Directly mapped with key =
scheme
.
sequencenum
additional.fields.value.string_value
Directly mapped with key =
sequencenum
.
service
target.port
Directly mapped.
service_id
security_result.detection_fields.value
Directly mapped with key =
service_id
.
session_uid
network.session_id
Directly mapped.
src
principal.ip
Directly mapped.
src_dns_name
security_result.detection_fields.value
Directly mapped with key =
src_dns_name
.
src_machine_name
security_result.detection_fields.value
Directly mapped with key =
src_machine_name
.
principal.asset.hostname
Directly mapped.
principal.hostname
Directly mapped.
src_user_dn
security_result.detection_fields.value
Directly mapped with key =
src_user_dn
.
src_user_name
principal.user.userid
Directly mapped.
principal.user.email_addresses
The email address is extracted from the src_user_name field if it exists and is in the format
userid (email)
.
te_verdict_determined_by
security_result.detection_fields.value
Directly mapped with key =
te_verdict_determined_by
.
timestamp
metadata.event_timestamp
Directly mapped.
trusted_domain
security_result.detection_fields.value
Directly mapped with key =
trusted_domain
.
user
principal.user.userid
Directly mapped if src_user_name is empty.
principal.user.email_addresses
The email address is extracted from the user field if it exists and is in the format
userid (email)
.
user_name
principal.user.email_addresses
Directly mapped if the value is a valid email address.
user_sid
principal.user.windows_sid
Directly mapped.
verdict
security_result.detection_fields.value
Directly mapped with key =
verdict
.
version
additional.fields.value.string_value
Directly mapped with key =
version
.
vpn_feature_name
security_result.detection_fields.value
Directly mapped with key =
vpn_feature_name
.
web_client_type
security_result.detection_fields.value
Directly mapped with key =
web_client_type
.
metadata.log_type
This field is hardcoded to
CHECKPOINT_HARMONY
.
metadata.vendor_name
This field is hardcoded to
CHECKPOINT_HARMONY
.
principal.asset.platform_software.platform
Mapped to WINDOWS, MAC, or LINUX based on the value of the os_name field.
network.ip_protocol
Mapped to TCP, UDP, ICMP, IP6IN4, or GRE based on the value of the proto field and other fields like service and service_id.
security_result.severity
Mapped to LOW, MEDIUM, HIGH, or CRITICAL based on the value of the severity field.
metadata.event_type
This field is set to
NETWORK_CONNECTION
if both principal and target are present,
STATUS_UNCATEGORIZED
if only principal is present, and
GENERIC_EVENT
otherwise.
Need more help?
Get answers from Community members and Google SecOps professionals.
