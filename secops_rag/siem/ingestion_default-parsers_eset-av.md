# Collect ESET AV logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-av/  
**Scraped:** 2026-03-05T09:23:49.880105Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ESET AV logs
Supported in:
Google secops
SIEM
This document explains how to ingest ESET AV logs to Google Security Operations
using Bindplane. The Logstash parser code extracts security event data from
ESET_AV logs formatted in SYSLOG or JSON. It first normalizes the raw message,
then parses it based on the identified format, mapping extracted fields to the
corresponding Unified Data Model (UDM) schema for consistent representation and
analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to ESET Protect
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
ingestion_labels
:
log_type
:
'ESET_AV'
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
Configure Syslog for ESET PROTECT on-premises
Sign in to the
ESET Protect
Web Console.
Go to
More
>
Settings
>
Advanced Settings
>
Syslog Server
.
Select the toggle next to
Enable Syslog
.
Provide the following configuration details:
Host
: Enter the Bindplane agent IP address
Port
: Enter the Bindplane agent port number (
514
for UDP)
Format
: Select
Syslog
Transport
: Select
UDP
Trace log verbosity
: Select
Informational
Export logs to Syslog toggle
: Select
Enable
Exported logs format
: Select
JSON
Click
Save
.
Configure Syslog for ESET PROTECT Cloud
Sign in to the
ESET Protect
Web Console.
Go to
More
>
Settings
>
Syslog Server
.
Select the toggle next to
Enable Syslog
.
Provide the following configuration details:
Format of payload
: Select
JSON
Format of the envelope
: Select
Syslog
Minimum log Level
: Select
Informational
Event types to log
: Select
All
event types
Destination IP
: Enter the Bindplane agent IP address
Port
: Enter the Bindplane agent port number (
514
for UDP)
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
account
principal.administrative_domain
Extracted from the
account
field using grok pattern
%{DATA:admin_domain}\\\\%{WORD:user_id}
.
account
principal.user.userid
Extracted from the
account
field using grok pattern
%{DATA:admin_domain}\\\\%{WORD:user_id}
.
action
security_result.action
If
action
is
Block
(case-insensitive), set to
BLOCK
. If
action
is
Start
(case-insensitive), set to
ALLOW
.
action_taken
security_result.action_details
Directly mapped from the
action_taken
field.
computer_severity_score
security_result.detection_fields
A key-value pair is created with the key
computer_severity_score
and the value from the
computer_severity_score
field. This pair is appended to the
security_result.detection_fields
array.
detail
security_result.description
Directly mapped from the
detail
field.
domain
principal.domain.name
Directly mapped from the
domain
field.
eialarmid
security_result.detection_fields
A key-value pair is created with the key
eialarmid
and the value from the
eialarmid
field. This pair is appended to the
security_result.detection_fields
array.
eiconsolelink
principal.url
Directly mapped from the
eiconsolelink
field.
event
metadata.description
Renamed from
event
to
event_desc
and mapped to
metadata.description
.
event_type
metadata.product_event_type
Directly mapped from the
event_type
field.
group_name
principal.group.group_display_name
Directly mapped from the
group_name
field.
hash
principal.file.sha1
Converted to lowercase. If the lowercase value matches the SHA-1 regex, mapped to
principal.file.sha1
.
hash
principal.resource.attribute.labels
A key-value pair is created with the key
hash
and the value from the
hash
field. This pair is appended to the
principal.resource.attribute.labels
array.
hostname
principal.asset.hostname
Directly mapped from the
hostname
field.
hostname
principal.hostname
Directly mapped from the
hostname
field.
inbound
network.direction
If true, set to
INBOUND
. If false, set to
OUTBOUND
.
ipv4
target.asset.ip
Directly mapped from the
ipv4
field if
target_address
is empty.
ipv4
target.ip
Directly mapped from the
ipv4
field if
target_address
is empty.
json_data
Parsed as JSON to extract various fields.
message
Parsed using grok to extract timestamp, host, and json_data.
need_restart
additional.fields
A key-value pair is created with the key
need_restart
and the value from the
need_restart
field (converted to string). This pair is appended to the
additional.fields
array.
os_name
principal.platform
If contains
Window
or
window
(case-insensitive), set to
WINDOWS
. If contains
Linux
or
linux
(case-insensitive), set to
LINUX
. If contains
Mac
or
mac
(case-insensitive), set to
MAC
.
os_name
principal.platform_version
Directly mapped from the
os_name
field.
process_name
principal.process.file.full_path
Directly mapped from the
process_name
field. If empty, takes the value of
processname
.
processname
principal.process.file.full_path
If
process_name
is empty, mapped to
process_name
.
protocol
network.ip_protocol
Converted to uppercase. If the uppercase value matches known protocols (TCP, UDP, ICMP, etc.), mapped to
network.ip_protocol
.
result
security_result.summary
Directly mapped from the
result
field.
rulename
security_result.rule_name
Directly mapped from the
rulename
field.
scan_id
security_result.detection_fields
A key-value pair is created with the key
scan_id
and the value from the
scan_id
field. This pair is appended to the
security_result.detection_fields
array.
scanner_id
security_result.detection_fields
A key-value pair is created with the key
scanner_id
and the value from the
scanner_id
field. This pair is appended to the
security_result.detection_fields
array.
severity
security_result.severity
If contains
Warn
or
warn
(case-insensitive), set to
HIGH
. If contains
Info
or
info
(case-insensitive), set to
LOW
.
severity_score
security_result.detection_fields
A key-value pair is created with the key
severity_score
and the value from the
severity_score
field. This pair is appended to the
security_result.detection_fields
array.
source_address
principal.asset.ip
Directly mapped from the
source_address
field.
source_address
principal.ip
Directly mapped from the
source_address
field.
source_port
principal.port
Converted to string and then to integer. Mapped to
principal.port
.
source_uuid
metadata.product_log_id
Directly mapped from the
source_uuid
field.
target
Renamed to
target1
.
target_address
target.asset.ip
Directly mapped from the
target_address
field.
target_address
target.ip
Directly mapped from the
target_address
field.
target_port
target.port
Converted to string and then to integer. Mapped to
target.port
.
threat_handled
security_result.detection_fields
A key-value pair is created with the key
threat_handled
and the value from the
threat_handled
field (converted to string). This pair is appended to the
security_result.detection_fields
array.
threat_name
security_result.threat_name
Directly mapped from the
threat_name
field.
threat_type
security_result.threat_id
Directly mapped from the
threat_type
field.
time
metadata.event_timestamp
Used to populate
metadata.event_timestamp
.
username
principal.user.userid
Directly mapped from the
username
field if
user_id
and
user
are empty.
user
principal.user.userid
Directly mapped from the
user
field if
user_id
is empty.
metadata.event_type
If
source_address
and
target_address
are not empty, set to
NETWORK_CONNECTION
. Else if
has_user
is true, set to
USER_UNCATEGORIZED
. Else if
has_principal
is true, set to
STATUS_UPDATE
. Otherwise, set to
GENERIC_EVENT
.
metadata.log_type
Set to
ESET_AV
.
metadata.product_name
Set to
ESET_AV
.
metadata.vendor_name
Set to
ESET_AV
.
intermediary.hostname
The value of this field is taken from the
host
field extracted from the log message.
principal.user.userid
If the field
account
is not empty, the parser extracts the user ID from the
account
field using a grok pattern. Otherwise it checks if the field
user
is not empty, if so it takes its value. If both
account
and
user
are empty, it checks if the field
username
is not empty, if so it takes its value.
Need more help?
Get answers from Community members and Google SecOps professionals.
