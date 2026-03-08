# Collect Tanium Stream logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-th/  
**Scraped:** 2026-03-05T10:01:12.742614Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Stream logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Stream logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Stream provides real-time endpoint telemetry, threat hunting data, and behavioral analytics in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser transforms raw JSON logs from Tanium Stream into a unified data model (UDM). It first normalizes common fields and then applies specific logic based on the "logType" or "eventType" to map relevant information into the appropriate UDM fields, handling various event types like network connections, user logins, process launches, and file modifications.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Tanium Core Platform
7.0 or later
Tanium Stream
module installed and configured
Tanium Connect
module installed with valid license
Tanium Threat Response
3.4.346 or later (if using TR integration)
Privileged access to
Tanium Console
with administrative rights
Privileged access to
AWS
(S3, IAM)
Configure Tanium Stream service account
Sign in to the
Tanium Console
.
Go to
Modules
>
Stream
.
Click
Settings
at the top right.
In the
Service Account
section, configure the following:
Service Account User
: Select a user with appropriate Stream permissions.
Verify
the account has Connect User role privilege.
Confirm
access to Stream data sources and endpoints.
Click
Save
to apply the service account configuration.
Collect Tanium Stream prerequisites
Sign in to the
Tanium Console
as an administrator.
Go to
Administration
>
Permissions
>
Users
.
Create or identify a service account user with the following roles:
Stream Administrator
or
Stream Read Only User
role.
Connect User
role privilege.
Access to monitored computer groups (recommended:
All Computers
group).
Read Saved Question
permission for Stream content sets.
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save bucket
Name
and
Region
for future reference (for example,
tanium-stream-logs
).
Create a user following this user guide:
Creating an IAM user
.
Select the created
User
.
Select the
Security credentials
tab.
Click
Create Access Key
in the
Access Keys
section.
Select
Third-party service
as the
Use case
.
Click
Next
.
Optional: add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
Access Key
and
Secret Access Key
for later use.
Click
Done
.
Select the
Permissions
tab.
Click
Add permissions
in the
Permissions policies
section.
Select
Add permissions
.
Select
Attach policies directly
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
Configure Tanium Connect AWS S3 destination
Sign in to the
Tanium Console
.
Go to
Modules
>
Connect
.
Click
Create Connection
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Stream Telemetry to S3 for SecOps
).
Description
: Optional description (for example,
Export endpoint telemetry and threat hunting data to AWS S3 for Google SecOps ingestion
).
Enable
: Select to enable the connection to run on schedule.
Click
Next
.
Configure the connection source
In the
Source
section, provide the following configuration details:
Source Type
: Select
Saved Question
.
Saved Question
: Select one of the following Stream-related saved questions:
Stream - Endpoint Events
for real-time endpoint telemetry.
Stream - Network Events
for network activity monitoring.
Stream - Process Events
for process execution tracking.
Stream - File Events
for file system activity.
Stream - Threat Hunting Data
for behavioral analytics.
Computer Group
: Select
All Computers
or specific computer groups to monitor.
Refresh Interval
: Set appropriate interval for data collection (for example,
5 minutes
for real-time telemetry).
Click
Next
.
Configure AWS S3 destination
In the
Destination
section, provide the following configuration details:
Destination Type
: Select
AWS S3
.
Destination Name
: Enter a unique name (for example,
Google SecOps Stream S3 Destination
).
AWS Access Key
: Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
AWS Secret Access Key
: Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
Bucket Name
: Enter your S3 bucket name (for example,
tanium-stream-logs
).
Region
: Select the AWS region where your S3 bucket is located.
Key Prefix
: Enter a prefix for the S3 objects (for example,
tanium/stream/
).
Click
Next
.
Configure filters
In the
Filters
section, configure data filtering options:
Send new items only
: Select this option to send only new telemetry data since the last export.
Column filters
: Add filters based on specific event attributes if needed (for example, filter by event type, process name, or threat indicators).
Click
Next
.
Format data for AWS S3
In the
Format
section, configure the data format:
Format
: Select
JSON
.
Options
:
Include headers
: Deselect to avoid headers in JSON output.
Include empty cells
: Select based on your preference.
Advanced Options
:
File naming
: Use default timestamp-based naming.
Compression
: Select
Gzip
to reduce storage costs and transfer time.
Click
Next
.
Schedule the connection
In the
Schedule
section, configure the export schedule:
Enable schedule
: Select to enable automatic scheduled exports.
Schedule type
: Select
Recurring
.
Frequency
: Select
Every 5 minutes
for near real-time telemetry data.
Start time
: Set appropriate start time for the first export.
Click
Next
.
Save and verify connection
Review the connection configuration in the summary screen.
Click
Save
to create the connection.
Click
Test Connection
to verify the configuration.
If the test is successful, click
Run Now
to perform an initial export.
Monitor the connection status in the
Connect Overview
page.
Configure a feed in Google SecOps to ingest Tanium Stream logs
Go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Tanium Stream logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Stream
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-stream-logs/tanium/stream/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log field
UDM mapping
Logic
additional.event__AlgorithmName
additional.fields.key: event
AlgorithmName
additional.fields.value.string_value: %{additional.event
AlgorithmName}
Value taken directly from the raw log field
additional.event__AlgorithmName
.
additional.event__AuthenticationPackageName
target.resource.name: %{additional.event__AuthenticationPackageName}
Value taken directly from the raw log field
additional.event__AuthenticationPackageName
.
additional.event__CallerProcessId
principal.process.pid: %{additional.event__CallerProcessId}
Value taken directly from the raw log field
additional.event__CallerProcessId
.
additional.event__CallerProcessName
principal.process.file.full
path: %{additional.event
_CallerProcessName}
Value taken directly from the raw log field
additional.event__CallerProcessName
.
additional.event__ClientProcessId
principal.process.pid: %{additional.event__ClientProcessId}
Value taken directly from the raw log field
additional.event__ClientProcessId
.
additional.event__ClientProcessStartKey
additional.fields.key: event
ClientProcessStartKey
additional.fields.value.string_value: %{additional.event
ClientProcessStartKey}
Value taken directly from the raw log field
additional.event__ClientProcessStartKey
.
additional.event__CommandLine
target.process.command
line: %{additional.event
_CommandLine}
Value taken directly from the raw log field
additional.event__CommandLine
.
additional.event__ElevatedToken
additional.fields.key: event__ElevatedToken
additional.fields.value.string_value: Yes/No
Value taken directly from the raw log field
additional.event__ElevatedToken
.
If the value is "%%1842", it is replaced with "Yes".
If the value is "%%1843", it is replaced with "No".
additional.event__FQDN
principal.hostname: %{additional.event__FQDN}
Value taken directly from the raw log field
additional.event__FQDN
.
additional.event__FailureReason
additional.fields.key: event
FailureReason
additional.fields.value.string_value: %{additional.event
FailureReason}
Value taken directly from the raw log field
additional.event__FailureReason
.
additional.event__ImpersonationLevel
additional.fields.key: event
ImpersonationLevel
additional.fields.value.string_value: %{additional.event
ImpersonationLevel}
Value taken directly from the raw log field
additional.event__ImpersonationLevel
.
additional.event__IpAddress
target.ip: %{additional.event__IpAddress}
Value taken directly from the raw log field
additional.event__IpAddress
.
additional.event__IpPort
target.port: %{additional.event__IpPort}
Value taken directly from the raw log field
additional.event__IpPort
and converted to an integer.
additional.event__KeyLength
additional.fields.key: event
KeyLength
additional.fields.value.string_value: %{additional.event
KeyLength}
Value taken directly from the raw log field
additional.event__KeyLength
.
additional.event__KeyName
additional.fields.key: event
KeyName
additional.fields.value.string_value: %{additional.event
KeyName}
Value taken directly from the raw log field
additional.event__KeyName
.
additional.event__KeyType
additional.fields.key: event
KeyType
additional.fields.value.string_value: %{additional.event
KeyType}
Value taken directly from the raw log field
additional.event__KeyType
.
additional.event__LmPackageName
additional.fields.key: event
LmPackageName
additional.fields.value.string_value: %{additional.event
LmPackageName}
Value taken directly from the raw log field
additional.event__LmPackageName
.
additional.event__LogonGuid
target.resource.product_object
id: %{additional.event
_LogonGuid}
Value taken directly from the raw log field
additional.event__LogonGuid
with curly braces removed.
additional.event__LogonProcessName
target.process.file.full
path: %{additional.event
_LogonProcessName}
Value taken directly from the raw log field
additional.event__LogonProcessName
.
additional.event__LogonType
extensions.auth.auth
details: Logon Type: %{additional.event
_LogonType}
Value taken directly from the raw log field
additional.event__LogonType
.
additional.event__MandatoryLabel
additional.fields.key: event
MandatoryLabel
additional.fields.value.string_value: %{additional.event
MandatoryLabel}
Value taken directly from the raw log field
additional.event__MandatoryLabel
.
additional.event__NewProcessId
target.process.pid: %{additional.event__NewProcessId}
Value taken directly from the raw log field
additional.event__NewProcessId
.
additional.event__NewProcessName
target.process.file.full
path: %{additional.event
_NewProcessName}
Value taken directly from the raw log field
additional.event__NewProcessName
.
additional.event__ObjectServer
security_result.category
details: %{additional.event
_ObjectServer}
Value taken directly from the raw log field
additional.event__ObjectServer
.
additional.event__Operation
additional.fields.key: event
Operation
additional.fields.value.string_value: %{additional.event
Operation}
Value taken directly from the raw log field
additional.event__Operation
.
additional.event__ParentProcessId
principal.process.parent
process.pid: %{additional.event
_ParentProcessId}
Value taken directly from the raw log field
additional.event__ParentProcessId
.
additional.event__ParentProcessName
principal.process.parent_process.file.full
path: %{additional.event
_ParentProcessName}
Value taken directly from the raw log field
additional.event__ParentProcessName
.
additional.event__ProcessId
principal.process.pid: %{additional.event__ProcessId}
Value taken directly from the raw log field
additional.event__ProcessId
.
additional.event__ProcessName
principal.process.file.full
path: %{additional.event
_ProcessName}
Value taken directly from the raw log field
additional.event__ProcessName
.
additional.event__PrivilegeList
principal.user.attribute.permissions.name: %{additional.event__PrivilegeList}
Value taken directly from the raw log field
additional.event__PrivilegeList
.
additional.event__ProviderName
additional.fields.key: event
ProviderName
additional.fields.value.string_value: %{additional.event
ProviderName}
Value taken directly from the raw log field
additional.event__ProviderName
.
additional.event__RestrictedAdminMode
additional.fields.key: event
RestrictedAdminMode
additional.fields.value.string_value: %{additional.event
RestrictedAdminMode}
Value taken directly from the raw log field
additional.event__RestrictedAdminMode
.
additional.event__ReturnCode
additional.fields.key: event
ReturnCode
additional.fields.value.string_value: %{additional.event
ReturnCode}
Value taken directly from the raw log field
additional.event__ReturnCode
.
additional.event__RpcCallClientLocality
additional.fields.key: event
RpcCallClientLocality
additional.fields.value.string_value: %{additional.event
RpcCallClientLocality}
Value taken directly from the raw log field
additional.event__RpcCallClientLocality
.
additional.event__Service
security
result.description: %{additional.event
_Service}
Value taken directly from the raw log field
additional.event__Service
.
additional.event__Status
additional.fields.key: event
Status
additional.fields.value.string_value: %{additional.event
Status}
Value taken directly from the raw log field
additional.event__Status
.
additional.event__SubStatus
additional.fields.key: event
SubStatus
additional.fields.value.string_value: %{additional.event
SubStatus}
Value taken directly from the raw log field
additional.event__SubStatus
.
additional.event__SubjectDomainName
principal.administrative
domain: %{additional.event
_SubjectDomainName}
Value taken directly from the raw log field
additional.event__SubjectDomainName
.
additional.event__SubjectLogonId
additional.fields.key: event
SubjectLogonId
additional.fields.value.string_value: %{additional.event
SubjectLogonId}
Value taken directly from the raw log field
additional.event__SubjectLogonId
.
additional.event__SubjectUserName
principal.user.user_display
name: %{additional.event
_SubjectUserName}
Value taken directly from the raw log field
additional.event__SubjectUserName
.
additional.event__SubjectUserSid
principal.user.windows
sid: %{additional.event
_SubjectUserSid}
Value taken directly from the raw log field
additional.event__SubjectUserSid
.
additional.event__TaskContentNew
additional.fields.key: event
TaskContentNew
additional.fields.value.string_value: %{additional.event
TaskContentNew}
Value taken directly from the raw log field
additional.event__TaskContentNew
.
additional.event__TaskName
additional.fields.key: event
TaskName
additional.fields.value.string_value: %{additional.event
TaskName}
Value taken directly from the raw log field
additional.event__TaskName
.
additional.event__TargetDomainName
target.administrative
domain: %{additional.event
_TargetDomainName}
Value taken directly from the raw log field
additional.event__TargetDomainName
.
additional.event__TargetLinkedLogonId
additional.fields.key: event
TargetLinkedLogonId
additional.fields.value.string_value: %{additional.event
TargetLinkedLogonId}
Value taken directly from the raw log field
additional.event__TargetLinkedLogonId
.
additional.event__TargetLogonId
additional.fields.key: event
TargetLogonId
additional.fields.value.string_value: %{additional.event
TargetLogonId}
Value taken directly from the raw log field
additional.event__TargetLogonId
.
additional.event__TargetOutboundDomainName
additional.fields.key: event
TargetOutboundDomainName
additional.fields.value.string_value: %{additional.event
TargetOutboundDomainName}
Value taken directly from the raw log field
additional.event__TargetOutboundDomainName
.
additional.event__TargetOutboundUserName
additional.fields.key: event
TargetOutboundUserName
additional.fields.value.string_value: %{additional.event
TargetOutboundUserName}
Value taken directly from the raw log field
additional.event__TargetOutboundUserName
.
additional.event__TargetSid
target.user.windows
sid: %{additional.event
_TargetSid}
Value taken directly from the raw log field
additional.event__TargetSid
.
additional.event__TargetUserName
target.user.userid: %{additional.event__TargetUserName}
Value taken directly from the raw log field
additional.event__TargetUserName
.
additional.event__TargetUserSid
target.user.windows
sid: %{additional.event
_TargetUserSid}
Value taken directly from the raw log field
additional.event__TargetUserSid
.
additional.event__TokenElevationType
additional.fields.key: event
TokenElevationType
additional.fields.value.string_value: %{additional.event
TokenElevationType}
Value taken directly from the raw log field
additional.event__TokenElevationType
.
additional.event__TransmittedServices
additional.fields.key: event
TransmittedServices
additional.fields.value.string_value: %{additional.event
TransmittedServices}
Value taken directly from the raw log field
additional.event__TransmittedServices
.
additional.event__VirtualAccount
additional.fields.key: event
VirtualAccount
additional.fields.value.string_value: %{additional.event
VirtualAccount}
Value taken directly from the raw log field
additional.event__VirtualAccount
.
additional.event__WorkstationName
target.hostname: %{additional.event__WorkstationName}
Value taken directly from the raw log field
additional.event__WorkstationName
.
additional.event_id
security_result.rule_name: EventID: %{additional.event_id}
Value taken directly from the raw log field
additional.event_id
and converted to a string.
additional.query
network.dns.questions.name: %{additional.query}
Value taken directly from the raw log field
additional.query
.
additional.response
network.dns.answers.name: %{additional.response}
Value taken directly from the raw log field
additional.response
.
metadata.description
metadata.description: %{metadata.description}
Value taken directly from the raw log field
metadata.description
.
metadata.eventTimestamp
metadata.event_timestamp.seconds: Extracted from %{metadata.eventTimestamp}
metadata.event_timestamp.nanos: Extracted from %{metadata.eventTimestamp}
Seconds and nanoseconds are extracted from the raw log field
metadata.eventTimestamp
using date parsing.
metadata.eventType
metadata.product_event_type: %{metadata.eventType}
metadata.event_type: %{metadata.eventType}
Value taken directly from the raw log field
metadata.eventType
.
metadata.logType
metadata.product_event_type: %{metadata.logType}
metadata.event_type: %{metadata.logType}
Value taken directly from the raw log field
metadata.logType
.
network.applicationProtocol
network.application_protocol: %{network.applicationProtocol}
Value taken directly from the raw log field
network.applicationProtocol
.
network.direction
network.direction: %{network.direction}
Value taken directly from the raw log field
network.direction
.
network.ipProtocol
network.ip_protocol: %{network.ipProtocol}
Value taken directly from the raw log field
network.ipProtocol
.
principal.assetId
principal.asset_id: TANIUM:%{principal.assetId}
Value taken directly from the raw log field
principal.assetId
and prefixed with "TANIUM:".
principal.hostname
principal.hostname: %{principal.hostname}
Value taken directly from the raw log field
principal.hostname
.
principal.process.companySpecificParentProcessId
principal.process.product_specific_process_id: TANIUM:%{principal.assetId}:%{principal.process.companySpecificParentProcessId}
Value taken directly from the raw log field
principal.process.companySpecificParentProcessId
and formatted as "TANIUM:%{principal.assetId}:%{principal.process.companySpecificParentProcessId}".
principal.process.companySpecificProcessId
principal.process.product_specific_process_id: TANIUM:%{principal.assetId}:%{principal.process.companySpecificProcessId}
Value taken directly from the raw log field
principal.process.companySpecificProcessId
and formatted as "TANIUM:%{principal.assetId}:%{principal.process.companySpecificProcessId}".
principal.process.commandLine
target.process.command_line: %{principal.process.commandLine}
Value taken directly from the raw log field
principal.process.commandLine
with double quotes removed and hyphens replaced with ampersands.
principal.process.file.fullPath
target.process.file.full_path: %{principal.process.file.fullPath}
Value taken directly from the raw log field
principal.process.file.fullPath
.
principal.process.file.md5
target.process.file.md5: %{principal.process.file.md5}
Value taken directly from the raw log field
principal.process.file.md5
and converted to lowercase.
principal.process.parentPid
principal.process.pid: %{principal.process.parentPid}
Value taken directly from the raw log field
principal.process.parentPid
only for
PROCESS_LAUNCH
events.
principal.process.pid
target.process.pid: %{principal.process.pid}
Value taken directly from the raw log field
principal.process.pid
only for
PROCESS_LAUNCH
events.
principal.process.productSpecificProcessId
principal.process.product_specific_process_id: TANIUM:%{principal.assetId}:%{principal.process.productSpecificProcessId}
Value taken directly from the raw log field
principal.process.productSpecificProcessId
and formatted as "TANIUM:%{principal.assetId}:%{principal.process.productSpecificProcessId}".
principal.user.groupid
principal.user.group_identifiers: %{principal.user.groupid}
Value taken directly from the raw log field
principal.user.groupid
.
principal.user.userid
principal.user.userid: %{principal.user.userid}
Value taken directly from the raw log field
principal.user.userid
.
src.ip
principal.ip: %{src.ip}
Value taken directly from the raw log field
src.ip
.
src.port
principal.port: %{src.port}
Value taken directly from the raw log field
src.port
and converted to an integer.
target.file.fullPath
target.file.full_path: %{target.file.fullPath}
Value taken directly from the raw log field
target.file.fullPath
.
target.file.md5
target.file.md5: %{target.file.md5}
Value taken directly from the raw log field
target.file.md5
.
target.port
target.port: %{target.port}
Value taken directly from the raw log field
target.port
and converted to an integer.
target.registry.registryKey
target.registry.registry_key: %{target.registry.registryKey}
Value taken directly from the raw log field
target.registry.registryKey
.
target.registry.registryValue
target.registry.registry_value_data: %{target.registry.registryValue}
Value taken directly from the raw log field
target.registry.registryValue
.
target.user.userDisplayName
target.user.user_display_name: %{target.user.userDisplayName}
Value taken directly from the raw log field
target.user.userDisplayName
.
target.user.windowsSid
target.user.windows_sid: %{target.user.windowsSid}
Value taken directly from the raw log field
target.user.windowsSid
.
user-agent
network.http.user_agent: %{user-agent}
Value taken directly from the raw log field
user-agent
with double quotes removed.
N/A
extensions.auth.auth_mechanism: LOCAL/NETWORK/BATCH/SERVICE/UNLOCK/NETWORK_CLEAR_TEXT/NEW_CREDENTIALS/REMOTE_INTERACTIVE/CACHED_INTERACTIVE/MECHANISM_UNSPECIFIED
Determined by the parser code based on the value of
additional.event__LogonType
.
N/A
extensions.auth.type: MACHINE
Added by the parser code for
USER_LOGIN
and
USER_LOGOUT
events.
N/A
metadata.event_type: PROCESS_LAUNCH/NETWORK_CONNECTION/FILE_OPEN/FILE_DELETION/REGISTRY_MODIFICATION/USER_LOGIN/STATUS_UPDATE/USER_LOGOUT/PROCESS_MODULE_LOAD/PROCESS_TERMINATION/USER_CHANGE_PERMISSIONS/SCHEDULED_TASK_MODIFICATION/SCHEDULED_TASK_DISABLE/SCHEDULED_TASK_ENABLE/SCHEDULED_TASK_DELETION/SCHEDULED_TASK_CREATION/PROCESS_UNCATEGORIZED
Determined by the parser code based on the value of
metadata.logType
and
additional.event_id
.
N/A
metadata.log_type: TANIUM_TH
Hardcoded value added by the parser code.
N/A
metadata.product_name: Stream
Hardcoded value added by the parser code.
N/A
metadata.vendor_name: Tanium
Hardcoded value added by the parser code.
N/A
principal.hostname: %{principal_hostname}
Value taken from either
principal.hostname
or
additional.event__FQDN
.
N/A
principal.ip: %{srcIp}
Extracted from the raw log message using grok if
src.ip
is present.
N/A
security
result.about.resource.name: %{additional.event
_AuthenticationPackageName}
Value taken directly from the raw log field
additional.event__AuthenticationPackageName
for specific
additional.event_id
values.
N/A
security_result.category: AUTH_VIOLATION
Added by the parser code for specific
additional.event_id
values.
N/A
security_result.rule_name: EventID: %{additional.event_id}
Value taken directly from the raw log field
additional.event_id
and converted to a string.
N/A
target.hostname: %{query_host}
Extracted from the raw log field
additional.query
if it contains a hostname.
N/A
target.ip: %{dstIp}
Extracted from the raw log message using grok if
src.ip
is present.
N/A
target.ip: %{query_ip}
Extracted from the raw log field
additional.query
if it contains an IP address.
N/A
target.process.command_line: %{principal_process_commandLine}
Value taken from
principal.process.commandLine
if it is not empty.
N/A
target.process.file.full_path: %{principal_process_file_fullPath}
Value taken from
principal.process.file.fullPath
if it is not empty.
N/A
target.process.file.md5: %{principal_process_file_md5}
Value taken from
principal.process.file.md5
if it is not empty.
N/A
target.process.product_specific_process_id: TANIUM:%{principal.assetId}:%{principal.process.productSpecificProcessId}
Value taken from
principal.process.productSpecificProcessId
and formatted as "TANIUM:%{principal.assetId}:%{principal.process.productSpecificProcessId}".
N/A
target.resource.resource_type: TASK
Added by the parser code for specific
additional.event_id
values.
N/A
timestamp.seconds: Extracted from %{metadata.eventTimestamp}
timestamp.nanos: Extracted from %{metadata.eventTimestamp}
Seconds and nanoseconds are extracted from the raw log field
metadata.eventTimestamp
using date parsing.
Need more help?
Get answers from Community members and Google SecOps professionals.
