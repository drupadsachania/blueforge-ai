# Collect Symantec Endpoint Protection logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sep/  
**Scraped:** 2026-03-05T09:28:43.254407Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec Endpoint Protection logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec Endpoint Protection logs to
Google Security Operations using Bindplane. The parser processes logs in SYSLOG or
KV format, first extracting timestamps from various formats within the log data.
Then, it utilizes a separate configuration file (
sep_pt2.include
) to perform
further parsing and structuring of the log events, ensuring successful
processing only if the initial timestamp extraction is successful.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to the Symantec Endpoint Protection platform
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
The following sections describe how to install the Bindplane agent.
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
Configure the Bindplane agent to ingest syslog and send to Google SecOps
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
`
0.0.0.0:514`
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
'CES'
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
Configure Syslog in Symantec Endpoint Protection
Sign in to your
Symantec Endpoint Protection Manager
web UI.
Click the
Admin
icon.
Locate the
View Servers
section, and click
Servers
.
Click
Local Site
>
Configure External Logging
.
Select the
Enable Transmission of Logs to a Syslog Server
checkbox.
Provide the following configuration details:
Syslog Server
: Enter the Bindplane IP address.
UDP Destination Port
: Enter the Bindplane port number (for example,
514
for
UDP
).
Log Facility
: Enter
Local6
.
Select the
Audit Logs
checkbox.
Select the
Security Logs
checkbox.
Select the
Risks
checkbox.
Click
OK
.
UDM mapping table
Log field
UDM mapping
Remark
_DB_HOST
target.hostname
a_record
network.dns.questions.type
AccessCheckResults
security_result.detection_fields
Accesses
security_result.detection_fields
AccessList
security_result.detection_fields
AccessMask
security_result.detection_fields
AccessReason
security_result.description
AccountName
target.user.user_display_name
AccountType
principal.user.attribute.roles
ACTION
security_result.detection_fields
ACTION_TYPE
security_result.action_details
ActiveProfile
target.resource.name
ActivityID
additional.fields
AdditionalInfo2
security_result.detection_fields
ADMIN_NAME
principal.user.userid
AGENT_SECURITY_LOG_IDX
metadata.product_log_id
AgentVer
additional.fields
Alert
security_result.detection_fields
ALERT_IDX
security_result.rule_id
ALERTDATETIME
security_result.first_discovered_time
ALERTENDDATETIME
security_result.last_discovered_time
ALERTINSERTTIME
security_result.detection_fields
AlgorithmName
security_result.detection_fields
Allowedapplicationreason
security_result.detection_fields
APP_NAME
target.application
app_name
principal.application
AppPoolID
target.application
AuthenticationPackageName
additional.fields
AuthenticationSetId
security_result.detection_fields
AuthenticationSetName
target.resource.name
BitlockerUserInputTime
additional.fields
BootMenuPolicy
additional.fields
BootType
additional.fields
BU
additional.fields
BugcheckString
additional.fields
CALLER_PROCESS_ID
principal.process.pid
CALLER_PROCESS_NAME
principal.process.file.full_path
callerReturnAddress
additional.fields
callerReturnModuleName
additional.fields
Caption
target.application
Category
security_result.category_details
Channel
security_result.about.resource.attribute.labels
CIDS_SIGN_SUB_ID
additional.fields
CLIENT_USER2
principal.user.userid
Comment
metadata.description
Component
security_result.detection_fields
connection.ether_type
security_result.about.labels
ConnectionSecurityRuleName
target.resource.name
ConnectionSecurityRuleId
security_result.detection_fields
CryptographicSetId
security_result.detection_fields
CryptographicSetName
target.resource.name
CSPEID
additional.fields
DCName
intermediary.hostname
Desc
metadata.description
DesiredAccess
security_result.detection_fields
device.last_app_connection
target.asset.last_discover_time
device.wss_feature
target.asset.attribute.labels
DeviceName
target.resource.name
DeviceNameLength
additional.fields
DeviceTime
additional.fields
DeviceVersionMajor
additional.fields
DeviceVersionMinor
additional.fields
disposition
security_result.detection_fields
dns_direction
security_result.detection_fields
domain
target.administrative_domain
Domain
principal.administrative_domain
DOMAIN_ID
target.resource.product_object_id
EDate
additional.fields
EDateUTC
metadata.event_timestamp
elevated_token
additional.fields
EntryCount
additional.fields
Error
security_result.description
error
security_result.detection_fields
ErrorCode
security_result.description
ErrorDescription
security_result.description
Event
metadata.description
EVENT_DATA
additional.fields
event_type
metadata.product_event_type
EventData.Binary
additional.fields
eventDesc
metadata.description
eventInsertTime
metadata.collected_timestamp
EventReceivedTime
metadata.collected_timestamp
EventTime
metadata.event_timestamp
EventType
metadata.product_event_type
ExceptionCode
security_result.detection_fields
executionPolicy
security_result.rule_name
ExecutionProcessID
principal.process.pid
ExecutionThreadID
principal.process.product_specific_process_id
ExtensionId
security_result.detection_fields
ExtensionName
target.resource.name
ExtraInfoLength
additional.fields
ExtraInfoString
additional.fields
FailureId
security_result.detection_fields
faulting_application_name
principal.process.file.names
faulting_application_path
principal.process.file.full_path
FaultingModuleName
additional.fields
FaultingModulePath
additional.fields
FaultOffset
additional.fields
FILE_SIZE
about.file.size
FilterID
security_result.detection_fields
FinalStatus
security_result.description
GPODisplayName
target.resource.name
GPOFileSystemPath
target.file.full_path
Group
principal.resource.attribute.labels
HACK_TYPE
security_result.category_details
HandleId
target.resource.attribute.labels
HID_LEVEL
additional.fields
HN
additional.fields
host
principal.hostname
Hostname
principal.hostname
id
metadata.product_log_id
IdleImplementation
additional.fields
IdleStateCount
additional.fields
ImpersonationLevel
additional.fields
IntensiveProtectionLevel
security_result.detection_fields
Interface
security_result.detection_fields
intermediary_host
intermediary.ip
intermediary.hostname
Maps to
intermediary.ip
if the value is an IP address.  Maps to
intermediary.hostname
if the value is a hostname.
INTRUSION_PAYLOAD_URL
target.url
INTRUSION_URL
target.url
IP
principal.ip
IP_ADDR
src.ip
IpAddress
principal.ip
IpPort
principal.port
KERNEL
principal.platform_patch_level
KeyFilePath
target.file.full_path
KeyLength
additional.fields
KeyName
security_result.detection_fields
KeyType
security_result.detection_fields
lastUpdateTime
target.resource.attribute.last_update_time
LmPackageName
security_result.detection_fields
LoadOptions
additional.fields
LogonGuid
network.session_id
LogonProcessName
target.application
LogonType
extensions.auth.auth_details
MandatoryLabel
target.resource.attribute.labels
MasterKeyId
security_result.detection_fields
MaximumPerformancePercent
additional.fields
Message
metadata.description
MinimumPerformancePercent
additional.fields
MinimumThrottlePercent
additional.fields
Minutes
target.resource.attribute.labels
NewFile
target.file.full_path
NewGrp
target.group.group_display_name
NewModDt
target.file.last_modification_time
NewOwn
additional.fields
NewPerms
additional.fields
NewProcessId
target.process.pid
NewProcessName
target.process.file.full_path
NewSecurityDescriptor
security_result.description
NewSize
additional.fields
NominalFrequency
principal.resource.attribute.labels
Number
principal.resource.attribute.labels
NumberOfGroupPolicyObjects
additional.fields
ObjectName
target.resource.name
ObjectServer
target.resource.attribute.labels
ObjectType
target.resource.resource_type
ObjId
target.resource.attribute.labels
OldFile
src.file.full_path
OldGrp
src.group.group_display_name
OldModDt
src.file.last_modification_time
OldOwn
additional.fields
OldPerms
additional.fields
OldSize
additional.fields
omittedFiles
security_result.detection_fields
Opcode
additional.fields
OpcodeValue
metadata.product_event_type
Operation
security_result.description
Operation
additional.fields
OperationType
security_result.category_details
OriginalSecurityDescriptor
additional.fields
OS
principal.platform
OSVER
principal.platform_version
param2
security_result.detection_fields
param3
security_result.detection_fields
param4
security_result.detection_fields
PARAM_DEVICE_ID
principal.hostname
PARAMETER
target.file.full_path
parameters
additional.fields
PARENT_SERVER_TYPE
additional.fields
PerformanceImplementation
additional.fields
POLNm
additional.fields
prevalence
security_result.detection_fields
Priority
security_result.detection_fields
PrivilegeList
target.resource.attribute.permissions.name
PrivilegesUsedForAccessCheck
security_result.detection_fields
ProblemID
additional.fields
ProcessId
principal.process.pid
ProcessID
target.process.pid
ProcessingMode
additional.fields
ProcessingTimeInMilliseconds
additional.fields
ProcessName
principal.process.file.full_path
ProcName
principal.process.file.names
ProcPath
principal.process.file.full_path
product_event_type
metadata.product_event_type
PROFILE_SERIAL_NO
additional.fields
protected
security_result.detection_fields
ProviderGuid
metadata.product_deployment_id
ProviderName
security_result.detection_fields
PuaCount
additional.fields
PuaPolicyId
additional.fields
PUB_KEY
additional.fields
Reason
additional.fields
ReasonCode
additional.fields
RecordNumber
metadata.product_log_id
RecoveryReason
security_result.description
RecType
metadata.product_event_type
RelativeTargetName
target.user.user_display_name
report_id
metadata.product_log_id
request
additional.fields
restricted_admin_mode
additional.fields
restricted_sid_count
additional.fields
risks
security_result.detection_fields
Rule
security_result.rule_name
RuleName
security_result.rule_name
RuleType
additional.fields
scan_duration
security_result.detection_fields
scan_state
security_result.detection_fields
scan_type
security_result.detection_fields
scanned_number
security_result.detection_fields
ScriptType
additional.fields
SecurityPackageName
about.file.full_path
SEQ_ID
additional.fields
Service
target.application
SeverityValue
security_result.severity_details
sha256
principal.process.file.sha256
ShareLocalPath
target.file.full_path
ShareName
target.resource.name
SITE_IDX
additional.fields
skipped_files
security_result.detection_fields
SourceModuleName
additional.fields
SourceModuleType
additional.fields
SourceName
principal.application
spn1
target.resource.attribute.labels
spn2
target.resource.attribute.labels
standard_schemes
security_result.detection_fields
State
additional.fields
Status
target.resource.attribute.labels
StopTime
additional.fields
SubjectDomainName
principal.administrative_domain
SubjectLogonId
principal.user.userid
SubjectUserName
principal.user.userid
SubjectUserSid
principal.user.windows_sid
SupportInfo1
additional.fields
SupportInfo2
additional.fields
syslogServer
intermediary.ip
intermediary.hostname
The value (the IP address or hostname) is from header of the log, and it is associated with an intermediary.
TargetDomainName
target.administrative_domain
TargetLogonId
target.user.userid
TargetUserName
target.user.userid
TargetUserSid
target.user.windows_sid
TaskContentNew
additional.fields
TaskName
target.resource.name
TaskValue
metadata.description
THREATS
security_result.detection_fields
threats
security_result.detection_fields
TimeDifferenceMilliseconds
additional.fields
TimeSampleSeconds
additional.fields
timestamp
metadata.event_timestamp
TokenElevationType
target.resource.attribute.labels
transaction_id
metadata.product_log_id
TransitedServices
security_result.detection_fields
TSId
network.session_id
type
security_result.threat_name
UMDFDeviceInstallBegin.version
target.resource.attribute.labels
UMDFReflectorDependencyMissing.Dependency
additional.fields
updateGuid
target.process.product_specific_process_id
updateRevisionNumber
target.resource.attribute.labels
updateTitle
target.resource.name
UpdateType
additional.fields
Url
target.url
urlTrackingStatus
security_result.detection_fields
User
principal.user.userid
UserID
target.user.userid
UserSid
target.user.windows_sid
VAPI_NAME
security_result.summary
VAST
additional.fields
Version
metadata.product_version
virtual_account
additional.fields
VSAD
additional.fields
WorkstationName
additional.fields
N/A
metadata.log_type
The log type is hardcoded to
SEP
.
N/A
metadata.product_name
The product name is hardcoded to
SEP
.
N/A
metadata.vendor_name
The vendor name is hardcoded to
Symantec
.
UDM mapping delta reference
On August 26, 2025, Google SecOps released a new version of the Symantec Endpoint Protection parser, which includes significant changes to the mapping of Symantec Endpoint Protection log fields to UDM fields and changes to the mapping of event types.
Log-field mapping delta
The following table lists the mapping delta for Symantec Endpoint Protection log-to-UDM fields exposed prior to August 26, 2025 and subsequently (listed in the
Old mapping
and
Current mapping
columns respectively).
Log field
Old mapping
Current mapping
_DB_DRIVER
about.resource.id
about.resource.product_object_id
_ip
principal.ip
intermediary.ip
Actualaction: Quarantined
security_result.action : BLOCK
security_result.action : QUARANTINE
BEGIN_TIME
additional.fields
target.resource.attribute.labels
callerProcessId
target.process.pid
principal.process.pid
callerProcessName
target.file.full_path
principal.process.file.full_path
CATEGORY_DESC
additional.fields
security_result.category_details
CLIENT_TYPE
additional.fields
principal.user.attribute.roles
DESCRIPTION
security_result.detection_fields
security_result.summary
device.id
target.resource.id
target.resource.product_object_id
device_uid
principal.resource.id
principal.resource.product_object_id
DURATION
additional.fields
network.session_duration.seconds
END_TIME
additional.fields
target.resource.attribute.last_update_time
feature_name
about.labels
security_result.about.labels
REMOTE_HOST_MAC
additional.fields
principal.mac
resourceId
principal.resource.id
principal.resource.product_object_id
server_name_1
principal.hostname
intermediary.hostname
target.hostname
UUID
additional.fields
principal.asset.asset_id
Event-type mapping delta
Multiple events that were classified before as
generic events
are now properly classified with meaningful event types.
The following table lists the delta for the handling of Symantec Endpoint Protection event types prior to August 26, 2025 and subsequently (listed in the
Old event_type
and
Current event_type
columns respectively).
eventType from log
Old event_type
Current event_type
Administrator logout
GENERIC_EVENT
USER_LOGOUT
Block all other IP traffic and log
STATUS_UPDATE
NETWORK_CONNECTION
File Created
GENERIC_EVENT
FILE_CREATION
File Modified
GENERIC_EVENT
FILE_MODIFICATION
File Renamed
GENERIC_EVENT
FILE_MODIFICATION
Scan started on selected drives
GENERIC_EVENT
SCAN_HOST
Scan started on selected drives, and has a file
GENERIC_EVENT
SCAN_FILE
User accessing a resource, based on an event
USER_UNCATEGORIZED
USER_RESOURCE_ACCESS
User is attempting to terminate
GENERIC_EVENT
STATUS_SHUTDOWN
VAPI_NAME
=
File Delete
USER_UNCATEGORIZED
FILE_DELETION
VAPI_NAME
=
File Write
USER_UNCATEGORIZED
FILE_CREATION
Need more help?
Get answers from Community members and Google SecOps professionals.
