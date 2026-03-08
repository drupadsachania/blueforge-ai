# Collect PowerShell logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/powershell/  
**Scraped:** 2026-03-05T09:59:14.895995Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect PowerShell logs
Supported in:
Google secops
SIEM
This document explains how to collect PowerShell logs to Google Security Operations by using Bindplane. The parser transforms raw Microsoft PowerShell logs into a unified data model (UDM). It first extracts fields from the raw log message, normalizes them into UDM fields, and then enriches the data with additional context based on specific event IDs, ultimately creating a structured UDM event for security analysis.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have a Windows 2016 or later.
If running behind a proxy, ensure firewall
ports
are open.
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
Install the Bindplane agent on Windows
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
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Before configuring the YAML file, stop the
observIQ Distro for Open Telemetry Collector
Service
in the Services Panel.
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
windowseventlog/powershell
:
channel
:
Microsoft-Windows-PowerShell/Operational
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
chronicle/powershell
:
endpoint
:
malachiteingestion-pa.googleapis.com
# Adjust the path to the credentials file you downloaded in Step 1
creds
:
'/path/to/ingestion-authentication-file.json'
log_type
:
'POWERSHELL'
override_log_type
:
false
raw_log_field
:
body
customer_id
:
'<customer_id>'
service
:
pipelines
:
logs/winpowershell
:
receivers
:
-
windowseventlog/powershell
processors
:
[
batch
]
exporters
:
[
chronicle/powershell
]
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
After saving the
config.yaml
file,
start
the
observIQ Distro for Open Telemetry Collector
Service
.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
UDM Mapping Table
Log Field
UDM Mapping
Logic
AccountName
principal.user.userid
Directly mapped from the
AccountName
field in the raw log.
ActivityID
security_result.detection_fields[0].value
Directly mapped from the
ActivityID
field in the raw log. The curly braces are removed.
Channel
Not mapped to the IDM object.
collection_time.nanos
Not mapped to the IDM object.
collection_time.seconds
Not mapped to the IDM object.
Command
Not mapped to the IDM object.
CommandLine
Not mapped to the IDM object.
Computer
principal.hostname
Directly mapped from the
Computer
field in the raw log if present.
ContextInfo
Not mapped to the IDM object.
ContextInfo_Command Name
security_result.detection_fields[0].value
Directly mapped from the
ContextInfo_Command Name
field in the raw log if present.
ContextInfo_Command Type
security_result.detection_fields[1].value
Directly mapped from the
ContextInfo_Command Type
field in the raw log if present.
ContextInfo_Host Application
target.process.command_line
Directly mapped from the
ContextInfo_Host Application
field in the raw log if
powershell.Host Application
is not present.
ContextInfo_Host ID
target.asset.asset_id
Directly mapped from the
ContextInfo_Host ID
field in the raw log if
powershell.Host ID
is not present. The value is prefixed with
Host ID:
.
ContextInfo_Host Name
target.hostname
Directly mapped from the
ContextInfo_Host Name
field in the raw log if
powershell.Host Name
is not present.
ContextInfo_Script Name
target.process.file.full_path
Directly mapped from the
ContextInfo_Script Name
field in the raw log if
script_name
is not present.
ContextInfo_Sequence Number
security_result.detection_fields[2].value
Directly mapped from the
ContextInfo_Sequence Number
field in the raw log if present. Converted to a string.
ContextInfo_Severity
Not mapped to the IDM object.
create_time.nanos
Not mapped to the IDM object.
create_time.seconds
Not mapped to the IDM object.
customer_id
Not mapped to the IDM object.
data
Not mapped to the IDM object.
Data
security_result.detection_fields[0].value
Directly mapped from the
Data
field in the raw log if present.
Data_1
security_result.detection_fields[1].value
Directly mapped from the
Data_1
field in the raw log if present.
Data_2
security_result.detection_fields[2].value
Directly mapped from the
Data_2
field in the raw log if present.
Domain
principal.administrative_domain
Directly mapped from the
Domain
field in the raw log.
entries
Not mapped to the IDM object.
ERROR_EVT_UNRESOLVED
Not mapped to the IDM object.
EventCategory
Not mapped to the IDM object.
EventData
Not mapped to the IDM object.
EventID
metadata.product_event_type, security_result.rule_name
Directly mapped from the
EventID
field in the raw log. The value is prefixed with
EventID:
for the
security_result.rule_name
field.
EventLevel
Not mapped to the IDM object.
EventLevelName
security_result.severity
Mapped based on the value of
EventLevelName
:
-
Information
maps to
INFORMATIONAL
.
-
Verbose
maps to
LOW
.
EventLog
Not mapped to the IDM object.
EventReceivedTime
Not mapped to the IDM object.
EventType
Not mapped to the IDM object.
EventTime
metadata.event_timestamp
Used to extract the timestamp if present.
ExecutionProcessID
principal.process.pid
Directly mapped from the
ExecutionProcessID
field in the raw log if present and not empty or 0. Converted to a string.
ExecutionThreadID
security_result.detection_fields[2].value
Directly mapped from the
ExecutionThreadID
field in the raw log if present and not empty or 0. Converted to a string.
File
target.process.file.full_path
Directly mapped from the
File
field in the raw log if present.
Host Application
Not mapped to the IDM object.
HostApplication
Not mapped to the IDM object.
Hostname
principal.hostname
Directly mapped from the
Hostname
field in the raw log.
id
Not mapped to the IDM object.
Keywords
Not mapped to the IDM object.
log_type
metadata.log_type
Directly mapped from the
log_type
field in the raw log.
Machine
principal.asset.asset_id, principal.asset.platform_software.platform_version
The
Machine
field is parsed to extract the machine ID and platform information. The machine ID is prefixed with
Machine ID:
. The platform is mapped to the UDM enum based on the value:
-
win
maps to
WINDOWS
.
-
mac
maps to
MAC
.
-
lin
maps to
LINUX
.
- Other values map to
UNKNOWN_PLATFORM
.
ManagementGroupName
additional.fields[0].value.string_value
Directly mapped from the
ManagementGroupName
field in the raw log if present.
Message.EventTime
metadata.event_timestamp
Used to extract the timestamp if present. Converted to a string.
Message.Message
security_result.description
Directly mapped from the
Message.Message
field in the raw log if
EventID
is in [
403
,
4103
,
4104
] and
message_message_not_found
. Carriage returns and tabs are replaced with commas.
Message
security_result.description
Directly mapped from the
Message
field in the raw log if present.
MessageNumber
Not mapped to the IDM object.
MessageSourceAddress
principal.ip
Directly mapped from the
MessageSourceAddress
field in the raw log if present.
MessageTotal
Not mapped to the IDM object.
MG
Not mapped to the IDM object.
Opcode
metadata.description
Directly mapped from the
Opcode
field in the raw log.
OpcodeValue
Not mapped to the IDM object.
Output
security_result.detection_fields[0].value
Directly mapped from the
Output
field in the raw log if present.
powershell.Command Name
security_result.detection_fields[0].value
Directly mapped from the
powershell.Command Name
field if present.
powershell.Command Type
security_result.detection_fields[1].value
Directly mapped from the
powershell.Command Type
field if present.
powershell.Host Application
target.process.command_line
Directly mapped from the
powershell.Host Application
field in the raw log if present.
powershell.Host ID
target.asset.asset_id
Directly mapped from the
powershell.Host ID
field in the raw log if present. The value is prefixed with
Host ID:
.
powershell.Host Name
target.hostname
Directly mapped from the
powershell.Host Name
field in the raw log if present.
powershell.HostApplication
target.process.command_line
Directly mapped from the
powershell.HostApplication
field in the raw log if present.
powershell.HostId
target.asset.asset_id
Directly mapped from the
powershell.HostId
field in the raw log if present. The value is prefixed with
Host ID:
.
powershell.HostName
target.hostname
Directly mapped from the
powershell.HostName
field in the raw log if present.
powershell.Script Name
target.process.file.full_path
Directly mapped from the
powershell.Script Name
field in the raw log if present.
powershell.ScriptName
target.process.file.full_path
Directly mapped from the
powershell.ScriptName
field in the raw log if present.
powershell.Sequence Number
security_result.detection_fields[2].value
Directly mapped from the
powershell.Sequence Number
field in the raw log if present.
powershell.SequenceNumber
security_result.detection_fields[0].value
Directly mapped from the
powershell.SequenceNumber
field in the raw log if present.
powershell.UserId
principal.user.userid
Directly mapped from the
powershell.UserId
field in the raw log if present.
Process ID
principal.process.pid
Directly mapped from the
Process ID
field in the raw log if
ExecutionProcessID
and
ProcessID
are not present or empty or 0. Converted to a string.
ProcessID
principal.process.pid
Directly mapped from the
ProcessID
field in the raw log if
ExecutionProcessID
is not present or empty or 0. Converted to a string.
ProviderGuid
metadata.product_deployment_id
Directly mapped from the
ProviderGuid
field in the raw log. The curly braces are removed.
PSEdition
Not mapped to the IDM object.
PSRemotingProtocolVersion
Not mapped to the IDM object.
PSVersion
Not mapped to the IDM object.
RecordNumber
metadata.product_log_id
Directly mapped from the
RecordNumber
field in the raw log. Converted to a string.
RenderedDescription
security_result.description
Directly mapped from the
RenderedDescription
field in the raw log if present.
RunAs User
Not mapped to the IDM object.
ScriptBlockId
Not mapped to the IDM object.
ScriptBlockText
security_result.detection_fields[0].value
Directly mapped from the
ScriptBlockText
field in the raw log if present.
ScriptBlock ID
Not mapped to the IDM object.
Severity
security_result.severity, security_result.severity_details
Mapped based on the value of
Severity
:
-
verbose
or
info
maps to
LOW
.
-
warn
or
err
maps to
MEDIUM
.
-
crit
maps to
HIGH
.
The raw value is also mapped to
security_result.severity_details
.
source.collector_id
Not mapped to the IDM object.
source.customer_id
Not mapped to the IDM object.
Source
additional.fields[1].value.string_value
Directly mapped from the
Source
field in the raw log if present.
SourceModuleName
principal.resource.name
Directly mapped from the
SourceModuleName
field in the raw log.
SourceModuleType
principal.resource.resource_subtype
Directly mapped from the
SourceModuleType
field in the raw log.
SourceName
metadata.product_name
Directly mapped from the
SourceName
field in the raw log.
start_time.nanos
Not mapped to the IDM object.
start_time.seconds
Not mapped to the IDM object.
TenantId
additional.fields[2].value.string_value
Directly mapped from the
TenantId
field in the raw log if present.
ThreadID
Not mapped to the IDM object.
timestamp.nanos
Not mapped to the IDM object.
timestamp.seconds
Not mapped to the IDM object.
type
Not mapped to the IDM object.
UserID
principal.user.windows_sid
Directly mapped from the
UserID
field in the raw log.
Username
principal.user.userid
Directly mapped from the
Username
field in the raw log if
AccountName
is not present.
metadata.vendor_name
Set to
Microsoft
.
metadata.event_type
Set to
PROCESS_LAUNCH
if
EventID
is
4104
and
_Path
is present in
Message
, or if
EventID
is
4103
, or if
EventID
is in [
800
,
600
,
400
] and
powershell.ScriptName
and
powershell.HostApplication
are present. Set to
PROCESS_TERMINATION
if
EventID
is
403
and
_HostApplication
is present in
Message
, or if
EventID
is
403
and
NewEngineState
is
Stopped
. Set to
STATUS_UPDATE
if
EventID
is
4104
and
_Path
is not present in
Message
, or if
EventID
is
4103
and
no_value
,
script_name
is empty,
script_name_not_found
, and
host_application_not_found
are all true, or if
EventID
is
53504
, or if
EventID
is
40962
, or if
EventID
is
40961
, or if
EventID
is empty and
MessageSourceAddress
is present. Set to
USER_UNCATEGORIZED
if
EventID
is empty and
Username
is present. Set to
GENERIC_EVENT
if
EventID
is empty and
MessageSourceAddress
and
Username
are not present.
metadata.product_name
Set to
Powershell
if
SourceName
is not present.
security_result.action
Set to
ALLOW
.
security_result.detection_fields[0].key
Set to
Activity ID
.
security_result.detection_fields[1].key
Set to
Sequence Number
.
security_result.detection_fields[2].key
Set to
ExecutionThreadID
.
additional.fields[0].key
Set to
Management Group Name
.
additional.fields[1].key
Set to
Source
.
additional.fields[2].key
Set to
TenantId
.
principal.asset.platform_software.platform
Set to
WINDOWS
if
platform_software
contains
win
,
MAC
if it contains
mac
,
LINUX
if it contains
lin
, and
UNKNOWN_PLATFORM
otherwise.
target.process.file.full_path
Set to
_Path
if
EventID
is
4104
and
_Path
is present in
Message
. Set to
file_path
if
EventID
is
4104
and
file_path
is present in
Message
. Set to
_HostApplication
if
EventID
is
403
and
_HostApplication
is present in
Message
.
Need more help?
Get answers from Community members and Google SecOps professionals.
