# Collect Microsoft LAPS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-laps/  
**Scraped:** 2026-03-05T09:58:12.323394Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft LAPS logs
Supported in:
Google secops
SIEM
This document explains how to ingest the Microsoft LAPS (Local Administrator Password Solution) logs to Google Security Operations using Bindplane. The parser first extracts JSON formatted data from the
message
field and then further parses the
EventData
field within the extracted JSON. It then maps the extracted fields to the Unified Data Model (UDM) schema, categorizes the event type based on the
EventId
, and finally merges all the processed data into the output event.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
if running behind a proxy, firewall
ports
are open
Privileged access to a Microsoft Windows Server with LAPS
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
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the installation directory on Windows.
Open the file using a text editor (for example, Notepad).
Edit the
config.yaml
file as follows:
receivers
:
windowseventlog/laps_operational
:
channel
:
Microsoft-Windows-LAPS/Operational
max_reads
:
100
poll_interval
:
5s
raw
:
true
start_at
:
end
processors
:
batch
:
exporters
:
chronicle/laps
:
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
log_type
:
'WINDOWS_LAPS'
override_log_type
:
false
raw_log_field
:
body
service
:
pipelines
:
logs/laps
:
receivers
:
-
windowseventlog/laps_operational
processors
:
[
batch
]
exporters
:
[
chronicle/laps
]
Replace
<customer_id>
with the actual Customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Microsoft Windows LAPS
Type
eventvwr.msc
at an elevated
command prompt
and press ENTER to open
Event Viewer
.
Go to
Applications and Services Logs
>
Microsoft
>
Windows
>
LAPS
.
Expand
LAPS
.
Right-click
LAPS
, and then click
Properties
.
Select the
Enable logging
checkbox.
Click
OK
when asked if the log is enabled.
Click
OK
.
UDM mapping table
Log Field
UDM Mapping
Logic
Channel
read_only_udm.additional.fields.key
Value is taken from the
Channel
field in the raw log and assigned to the
key
field.
Channel
read_only_udm.additional.fields.value.string_value
Value is taken from the
Channel
field in the raw log and assigned to the
string_value
field.
Computer
read_only_udm.principal.hostname
Value is taken from the
Computer
field in the raw log.
Computer
read_only_udm.principal.asset.hostname
Value is taken from the
Computer
field in the raw log.
EventData.%1
read_only_udm.additional.fields.value.string_value
Value is taken from the
EventData.%1
field in the raw log and assigned to the
string_value
field.
EventId
read_only_udm.metadata.product_event_type
Value is taken from the
EventId
field in the raw log.
EventId
read_only_udm.security_result.rule_name
Value is taken from the
EventId
field in the raw log and appended to
EventID:
.
EventRecordID
read_only_udm.metadata.product_log_id
Value is taken from the
EventRecordID
field in the raw log.
Keywords
read_only_udm.additional.fields.key
Value is taken from the
Keywords
field in the raw log and assigned to the
key
field.
Keywords
read_only_udm.additional.fields.value.string_value
Value is taken from the
Keywords
field in the raw log and assigned to the
string_value
field.
Level
read_only_udm.security_result.severity
Value is taken from the
Level
field in the raw log and mapped to:
INFORMATIONAL
for
INFO
,
Informational
,
Information
,
Normal
,
NOTICE
;
ERROR
for
ERROR
,
Error
;
CRITICAL
for
Critical
.
Opcode
read_only_udm.additional.fields.key
Value is taken from the
Opcode
field in the raw log and assigned to the
key
field.
Opcode
read_only_udm.additional.fields.value.string_value
Value is taken from the
Opcode
field in the raw log and assigned to the
string_value
field.
ProcessID
read_only_udm.principal.process.pid
Value is taken from the
ProcessID
field in the raw log.
ProviderName
read_only_udm.metadata.product_name
Value is taken from the
ProviderName
field in the raw log.
Task
read_only_udm.additional.fields.key
Value is taken from the
Task
field in the raw log and assigned to the
key
field.
Task
read_only_udm.additional.fields.value.string_value
Value is taken from the
Task
field in the raw log and assigned to the
string_value
field.
ThreadID
read_only_udm.additional.fields.key
Value is taken from the
ThreadID
field in the raw log and assigned to the
key
field.
ThreadID
read_only_udm.additional.fields.value.string_value
Value is taken from the
ThreadID
field in the raw log and assigned to the
string_value
field.
TimeCreated
read_only_udm.metadata.event_timestamp
Value is taken from the
TimeCreated
field in the raw log, parsed as UNIX_MS timestamp.
TimeCreated
events.timestamp
Value is taken from the
TimeCreated
field in the raw log, parsed as UNIX_MS timestamp.
Version
read_only_udm.additional.fields.key
Value is taken from the
Version
field in the raw log and assigned to the
key
field.
Version
read_only_udm.additional.fields.value.string_value
Value is taken from the
Version
field in the raw log and assigned to the
string_value
field.
read_only_udm.additional.fields.key
Assigned the value
EventData_P1
.
read_only_udm.metadata.event_type
Conditionally assigned
STATUS_UNCATEGORIZED
if EventId is
7
or
2
, else
GENERIC_EVENT
.
read_only_udm.metadata.vendor_name
Assigned the value
Microsoft
.
Need more help?
Get answers from Community members and Google SecOps professionals.
