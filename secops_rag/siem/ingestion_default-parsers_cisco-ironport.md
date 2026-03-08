# Collect Cisco IronPort logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ironport/  
**Scraped:** 2026-03-05T09:21:32.872176Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco IronPort logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco IronPort logs to
Google Security Operations using Bindplane. The parser extracts fields from the
syslog messages, specifically those related to
AccessLogs_chron
events. It
uses grok patterns to parse the message, converts data types, and maps the
extracted fields to the Unified Data Model (UDM), handling various Cisco
Ironport-specific fields like policy groups and access decisions. It also
performs basic error handling and sets metadata fields like vendor and product
name.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to
Cisco IronPort
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
Save the file securely on the system where Bindplane will be installed.
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
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
Configure the Bindpolane agent to ingest Syslog and send to Google SecOps
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
'CISCO_IRONPORT'
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
Configure Syslog on Cisco IronPort
Sign in to the Cisco IronPort web UI.
Click
System Administration
>
Log Subscriptions
.
Click
Add Log Subscription
.
Provide the following configuration details:
Log Type
: Select
Access Logs
or other logs you would like export.
Log Style
: Select
Squid
.
File Name
: Provide a filename if not provided by default.
Retrieval Method
: Select
Syslog Push
(uses default port
514
).
Hostname
: Enter the Bindplane agent IP address.
Protocol
: Select UDP.
Facility
: Select
local0
or
syslog
.
Click
Submit
.
UDM mapping table
Log Field
UDM Mapping
Logic
AccessLogs_chron
metadata.product_event_type
Directly mapped from the
product_event
field extracted by the first grok parser.
acl_decision_tag
security_result.detection_fields.key
Value is "ACL Decision Tag". Parser logic sets this value when
acl_decision_tag
is present in the logs.
acl_decision_tag
security_result.detection_fields.value
Directly mapped from the
acl_decision_tag
field extracted by the second grok parser.
access_or_decryption_policy_group
security_result.detection_fields.key
Value is "AccessOrDecryptionPolicyGroup". Parser logic sets this value when
access_or_decryption_policy_group
is present in the logs.
access_or_decryption_policy_group
security_result.detection_fields.value
Directly mapped from the
access_or_decryption_policy_group
field extracted by the second grok parser.
authenticated_user
principal.user.userid
Extracted from the
authenticated_user
field using grok and gsub to remove backslashes and quotes.
cache_hierarchy_retrieval
security_result.detection_fields.key
Value is "Cache Hierarchy Retrieval". Parser logic sets this value when
cache_hierarchy_retrieval
is present in the logs.
cache_hierarchy_retrieval
security_result.detection_fields.value
Directly mapped from the
cache_hierarchy_retrieval
field extracted by the second grok parser.
data_security_policy_group
security_result.detection_fields.key
Value is "DataSecurityPolicyGroup". Parser logic sets this value when
data_security_policy_group
is present in the logs.
data_security_policy_group
security_result.detection_fields.value
Directly mapped from the
data_security_policy_group
field extracted by the second grok parser.
external_dlp_policy_group
security_result.detection_fields.key
Value is "ExternalDlpPolicyGroup". Parser logic sets this value when
external_dlp_policy_group
is present in the logs.
external_dlp_policy_group
security_result.detection_fields.value
Directly mapped from the
external_dlp_policy_group
field extracted by the second grok parser.
hostname
principal.asset.hostname
Directly mapped from the
hostname
field extracted by the first grok parser.
hostname
principal.hostname
Directly mapped from the
hostname
field extracted by the first grok parser.
http_method
network.http.method
Directly mapped from the
http_method
field extracted by the second grok parser.
http_response_code
network.http.response_code
Directly mapped from the
http_response_code
field extracted by the second grok parser and converted to integer.
identity_policy_group
security_result.detection_fields.key
Value is "IdentityPolicyGroup". Parser logic sets this value when
identity_policy_group
is present in the logs.
identity_policy_group
security_result.detection_fields.value
Directly mapped from the
identity_policy_group
field extracted by the second grok parser. Copied from the
timestamp
field after the date filter processes it. Set to "STATUS_UPDATE" if
has_principal
is true, otherwise set to "GENERIC_EVENT". Constant value: "Cisco Ironport". Constant value: "Cisco".
outbound_malware_scanning_policy_group
security_result.detection_fields.key
Value is "OutboundMalwareScanningPolicyGroupS". Parser logic sets this value when
outbound_malware_scanning_policy_group
is present in the logs.
outbound_malware_scanning_policy_group
security_result.detection_fields.value
Directly mapped from the
outbound_malware_scanning_policy_group
field extracted by the second grok parser.
request_method_uri
target.url
Directly mapped from the
request_method_uri
field extracted by the second grok parser.
result_code
security_result.detection_fields.key
Value is "Result Code". Parser logic sets this value when
result_code
is present in the logs.
result_code
security_result.detection_fields.value
Directly mapped from the
result_code
field extracted by the second grok parser.
routing_policy_group
security_result.detection_fields.key
Value is "RoutingPolicyGroup". Parser logic sets this value when
routing_policy_group
is present in the logs.
routing_policy_group
security_result.detection_fields.value
Directly mapped from the
routing_policy_group
field extracted by the second grok parser.
severity
security_result.severity
Mapped from the
severity
field. If the value is "Info", it's set to "INFORMATIONAL".
source_ip
principal.asset.ip
Directly mapped from the
source_ip
field extracted by the second grok parser.
source_ip
principal.ip
Directly mapped from the
source_ip
field extracted by the second grok parser.
timestamp
timestamp
Extracted from the
message
field using grok and then parsed using the date filter.
total_bytes
network.sent_bytes
Directly mapped from the
total_bytes
field extracted by the second grok parser and converted to unsigned integer. Only mapped if not empty or "0".
Need more help?
Get answers from Community members and Google SecOps professionals.
