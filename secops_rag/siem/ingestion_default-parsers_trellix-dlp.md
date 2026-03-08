# Collect Trellix DLP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-dlp/  
**Scraped:** 2026-03-05T09:29:19.769513Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trellix DLP logs
Supported in:
Google secops
SIEM
This document explains how to ingest Trellix (formerly McAfee) DLP (Data Loss
Prevention) logs to Google Security Operations using Bindplane. This parser processes
McAfee DLP logs in CSV format, transforming them into the Unified Data
Model (UDM). It cleans the input, parses the CSV data, maps fields to UDM,
handles specific DLP event types and severities, and enriches the UDM with
additional metadata and security result details.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to McAfee EPO
McAfee DLP Endpoint Extension is installed and active
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
ingestion_labels
:
log_type
:
'MCAFEE_DLP'
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
Configure Syslog Server in McAfee ePO
Sign in to the
McAfee ePO
console.
Go to
Menu
>
Configuration
>
Registered Servers
.
Click
New Server
>
Syslog Server
.
Provide the following configuration details:
Name
: Unique name for the Syslog server (for example,
Google SecOps
).
Server Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (default is
514
).
Protocol
: Select UDP or TCP (depending on your Bindplane Agent installation).
Format
: Use
CSV
or
CEF
.
Click
Save
.
Configure DLP Event Forwarding
Go to
Menu
>
Data Protection
>
DLP Policy Manager
.
Click the
DLP Policy Assignment Rules
tab.
Edit the rule that applies to your target systems or create a new one.
Go to the
Actions
tab of the rule.
Check the box for
Log to Syslog Server
and select the Syslog Server you previously created.
Save
the rule.
Enable DLP Incident Forwarding
Go to
Menu
>
Data Protection
>
DLP Incident Manager
.
Click
Incident Actions
.
Create or edit an action to forward to syslog server.
Assign this action to a rule in your DLP policy.
Deploy the Policy
Go to
System Tree
>
select the desired group or system
.
Click
Actions
>
Agent
>
Wake Up Agents
.
Select the
Send Policies
.
Click
OK
.
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.action_details
Directly mapped from the
action
field.
action
security_result.action
Derived from the
action
field.  If
action
is 1, it's BLOCK. If
action
is 0, it's ALLOW. If
action
is 6, it's UNKNOWN_ACTION.
agent_ver
metadata.product_version
Directly mapped from the
agent_ver
field (which comes from
column8
).
class_count
additional.fields[4].key
Value is
ClassCount
.
class_count
additional.fields[4].value.string_value
Directly mapped from the
class_count
field.
class_display
additional.fields[5].key
Value is
ClassDisplay
.
class_display
additional.fields[5].value.string_value
Directly mapped from the
class_display
field.
count
additional.fields[6].key
Value is
Count
.
count
additional.fields[6].value.string_value
Directly mapped from the
count
field.
device_name
principal.hostname
Directly mapped from the
device_name
field.
dst
target.hostname
Directly mapped from the
dst
field if
inc_type
is
10000
.
dst
target.user.userid
Directly mapped from the
dst
field if
inc_type
is not
10000
.
dst_app
target.application
Directly mapped from the
dst_app
field.
dst_url
target.url
Directly mapped from the
dst_url
field.
encrypt
security_result.detection_fields[1].key
Value is
EncryptionProvider
.
encrypt
security_result.detection_fields[1].value
Directly mapped from the
encrypt
field.
evidence_count
additional.fields[2].key
Value is
EvidenceCount
.
evidence_count
additional.fields[2].value.string_value
Directly mapped from the
evidence_count
field.
fail_reason
additional.fields[3].key
Value is
FailReason
.
fail_reason
additional.fields[3].value.string_value
Directly mapped from the
fail_reason
field.
fail_reason
security_result.description
If
fail_reason
is
0
, the value is
No Failure
. Otherwise, the value is
Failure Occurred
.
file
target.file.full_path
Directly mapped from the
file
field.
file_size
target.file.size
Directly mapped from the
file_size
field, converted to an unsigned integer.
group
principal.user.attribute.labels.key
Value is
group
.
group
principal.user.attribute.labels.value
Directly mapped from the
group
field.
inc_id
metadata.product_log_id
Directly mapped from the
inc_id
field (which comes from
column1
).
inc_type
metadata.event_type
Used in conditional logic to determine the
metadata.event_type
. See logic for details.
inc_type
metadata.product_event_type
Directly mapped from the
inc_type
field (which comes from
column2
).
ip
principal.ip
Extracted IP address from the
ip
field using grok.
local_date
metadata.event_timestamp
The timestamp from the
local_date
field, parsed and converted to seconds since epoch.
name
principal.user.user_display_name
Directly mapped from the
name
field. If
inc_type
is in [
10000
,
10001
,
10002
,
40101
,
40400
,
40500
,
40700
] and
ip
is a valid IP, the value is
SCAN_NETWORK
. If
inc_type
is
40102
and
file
is not empty, the value is
SCAN_FILE
. If
inc_type
is in [
40301
,
40602
], the value is
PROCESS_UNCATEGORIZED
. Otherwise, the value is
GENERIC_EVENT
. Hardcoded value:
GCP_CLOUDAUDIT
. Hardcoded value:
Mcafee DLP
. Hardcoded value:
Mcafee
. If
status_id
is in [
1
,
2
], the value is
NEW
. If
status_id
is in [
3
,
4
], the value is
CLOSED
. If
status_id
is in [
5
,
6
], the value is
REVIEWED
. Value is
StatusId
. Value is
Resolution Id
. Value is
Expected Action
.
process_name
target.process.file.full_path
Directly mapped from the
process_name
field.
resolution_id
security_result.about.labels[0].value
Directly mapped from the
resolution_id
field.
rule_name
security_result.rule_name
Directly mapped from the
rule_name
field.
rule_set
security_result.rule_labels.key
Value is
rule_set
.
rule_set
security_result.rule_labels.value
Directly mapped from the
rule_set
field.
sev
security_result.severity
Derived from the
sev
field. If
sev
is 1, it's INFORMATIONAL. If
sev
is 2, it's ERROR. If
sev
is 3, it's LOW. If
sev
is 4, it's HIGH. If
sev
is 5, it's CRITICAL.
sev
security_result.severity_details
Directly mapped from the
sev
field.
status_id
principal.labels.value
Directly mapped from the
status_id
field.
total_count
additional.fields[1].key
Value is
TotalCount
.
total_count
additional.fields[1].value.string_value
Directly mapped from the
total_count
field.
total_size
additional.fields[0].key
Value is
TotalSize
.
total_size
additional.fields[0].value.string_value
Directly mapped from the
total_size
field.
usb_serial_number
security_result.detection_fields[0].key
Value is
USBSerialNumber
.
usb_serial_number
security_result.detection_fields[0].value
Directly mapped from the
usb_serial_number
field.
user
principal.user.userid
Directly mapped from the
user
field.
user_ou
principal.user.group_identifiers
Directly mapped from the
user_ou
field.
volume_serial_number
security_result.detection_fields[2].key
Value is
VolumeSerialNumber
.
volume_serial_number
security_result.detection_fields[2].value
Directly mapped from the
volume_serial_number
field.
expected_action
security_result.about.labels[1].value
Directly mapped from the
expected_action
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
