# Collect Microsoft Defender for Endpoint logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint/  
**Scraped:** 2026-03-05T09:17:37.753704Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Defender for Endpoint logs
Supported in:
Google secops
SIEM
This document describes how you can collect Microsoft Defender for Endpoint logs by setting up a Google Security Operations feed and how log fields map to Google SecOps unified data model (UDM) fields.
For more information, see
Data ingestion to Google SecOps
.
A typical deployment consists of Microsoft Defender for Endpoint and the Google SecOps feed configured to send logs to Google SecOps. Your deployment might be different from the typical deployment that is described in this document.
The deployment contains the following components:
Microsoft Defender for Endpoint
: The platform that collects logs.
Azure Storage
: The platform that stores logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Microsoft Defender for Endpoint and writes logs to Google SecOps.
Google SecOps
: The platform that retains and analyzes the logs from Microsoft Defender for Endpoint.
An ingestion label identifies the parser that normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
MICROSOFT_DEFENDER_ENDPOINT
ingestion label.
Before you begin
Ensure you have the following prerequisites:
All systems in the deployment architecture are configured with the UTC time zone.
You meet the prerequisites for using Microsoft Defender for Endpoint. For more information, see
Microsoft Defender XDR prerequisites
.
Configured
Microsoft Defender for Endpoint
Configured
storage account
in your tenant
Set up Microsoft Defender for Endpoint
Sign in to
security.microsoft.com
as a global administrator or security administrator.
In the left pane, click
Settings
.
Select the
Microsoft Defender XDR
tab.
Select
Streaming API
from the general section and click
Add
.
Select
Forward events to Azure Storage
.
Navigate to the storage account of your choice.
Select
Overview
>
JSON View
and enter the
Resource ID
.
After you enter the resource ID, select all the required data types.
Click
Save
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the Microsoft Defender for Endpoint feed
Click the
Microsoft Defender
pack.
Locate the
Microsoft Defender for Endpoint
log type.
Specify values in the following fields:
Source Type
: Microsoft Azure Blob Storage V2.
Azure URI
: The URI pointing to an Azure Blob Storage blob or container.
Source deletion option
: whether to delete files or directories after transferring.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Select
Shared key
or
SAS token
.
Key
: The shared key or SAS token to access Azure resources.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Supported Microsoft Defender for Endpoint log types
The Microsoft Defender for Endpoint parser supports the following tables:
AlertEvidence
AlertInfo
CloudAppEvents
DeviceAlertEvents
DeviceEvents
DeviceFileCertificateInfo
DeviceFileEvents
DeviceIdentityLogonEvents
DeviceImageLoadEvents
DeviceInfo
DeviceLogonEvents
DeviceNetworkEvents
DeviceNetworkInfo
DeviceProcessEvents
DeviceRegistryEvents
DeviceTvmInfoGathering
DeviceTvmInfoGatheringKB
DeviceTvmSecureConfigurationAssessment
DeviceTvmSecureConfigurationAssessmentKB
DeviceTvmSoftwareEvidenceBeta
DeviceTvmSoftwareInventory
DeviceTvmSoftwareVulnerabilities
DeviceTvmSoftwareVulnerabilitiesKB
EmailAttachmentInfo
EmailEvents
EmailPostDeliveryEvents
EmailUrlInfo
IdentityInfo
Supported Microsoft Defender for Endpoint log formats
The Microsoft Defender for Endpoint parser supports logs in JSON format.
Supported Microsoft Defender for Endpoint sample logs
JSON:
{
  "time": "2021-07-16T09:57:38.1599837Z",
  "tenantId": "ed236696-8612-40d7-8b49-xxxxxxxxxxx",
  "operationName": "Publish",
  "category": "AdvancedHunting-DeviceInfo",
  "properties": {
    "OSBuild": null,
    "RegistryDeviceTag": null,
    "IsAzureADJoined": null,
    "PublicIP": "198.51.100.0",
    "OSArchitecture": null,
    "OSVersion": null,
    "OSPlatform": null,
    "LoggedOnUsers": "[{\\"UserName\\":\\"bob\\",\\"DomainName\\":\\"DESKTOP-BOB\\",\\"Sid\\":\\"S-1-5-21-1695909852-106810125-1651530144-1001\\"}]",
    "AdditionalFields": "{\\"IsLocalLogon\\":true}",
    "DeviceObjectId": null,
    "DeviceId": "e93c25ad74cc1dd30afeb642696a2559824589e5",
    "MachineGroup": null,
    "Timestamp": "2021-07-16T09:54:41.0662159Z",
    "DeviceName": "desktop-dummy",
    "ReportId": 193010,
    "ClientVersion": "10.7431.19041.746"
  }
}
Field mapping reference
This section explains how the Google Security Operations parser maps Microsoft Defender for Endpoint fields to Google Security Operations UDM fields.
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - Common Fields for UDM Event Model
The following table lists the common log fields for the
MICROSOFT_DEFENDER_ENDPOINT
log type and their corresponding UDM fields:
Common log field
UDM mapping
Logic
time
metadata.collected_timestamp
category
metadata.product_event_type
metadata.product_name
The
metadata.product_name
UDM field is set to
Microsoft Defender for Endpoint
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Microsoft
.
Tenant
observer.resource_ancestors.name
tenantId
observer.resource_ancestors.product_object_id
operationName
additional.fields[operation_name]
properties.ActionType
security_result.summary
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - Common Fields for UDM Entity Model
The following table lists the common log fields for the
MICROSOFT_DEFENDER_ENDPOINT
log type and their corresponding UDM fields:
Common log field
UDM mapping
Logic
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Microsoft
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Microsoft Defender for Endpoint
.
time
metadata.collected_timestamp
tenantId
relations.entity.resource.product_object_id
operationName
additional.fields[operation_name]
category
metadata.description
Tenant
relations.entity.resource.name
relations.entity_type
The
relations.entity_type
UDM field is set to
RESOURCE
.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
.
relations.direction
The
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
Field mapping reference: DeviceEvents Event Identifier to Event Type
The following table lists the
DeviceEvents
log action types and their corresponding UDM event types.
Event Identifier
Event Type
UsbDriveDriveLetterChanged
DEVICE_CONFIG_UPDATE
AppControlAppInstallationAudited
SCAN_HOST
AsrExecutableOfficeContentAudited
SCAN_HOST
ShellLinkCreateFileEvent
FILE_CREATION
FileTimestampModificationEvent
FILE_MODIFICATION
PlistPropertyModified
FILE_MODIFICATION
SensitiveFileRead
FILE_READ
AsrUntrustedExecutableAudited
SCAN_HOST
AsrUntrustedExecutableBlocked
SCAN_HOST
DlpPocPrintJob
FILE_UNCATEGORIZED
RemovableStorageFileEvent
FILE_UNCATEGORIZED
DpapiAccessed
GENERIC_EVENT
ScreenshotTaken
GENERIC_EVENT
SecurityGroupCreated
GROUP_CREATION
SecurityGroupDeleted
GROUP_DELETION
UserAccountAddedToLocalGroup
GROUP_MODIFICATION
UserAccountRemovedFromLocalGroup
GROUP_MODIFICATION
ExploitGuardNetworkProtectionAudited
SCAN_HOST
ExploitGuardNetworkProtectionBlocked
SCAN_HOST
FirewallInboundConnectionBlocked
NETWORK_CONNECTION
FirewallInboundConnectionToAppBlocked
NETWORK_CONNECTION
FirewallOutboundConnectionBlocked
NETWORK_CONNECTION
RemoteDesktopConnection
NETWORK_CONNECTION
RemoteWmiOperation
NETWORK_CONNECTION
UntrustedWifiConnection
NETWORK_CONNECTION
DnsQueryRequest
NETWORK_DNS
DnsQueryResponse
NETWORK_DNS
NetworkShareObjectAdded
NETWORK_UNCATEGORIZED
AppGuardBrowseToUrl
SCAN_HOST
BrowserLaunchedToOpenUrl
NETWORK_UNCATEGORIZED
NetworkProtectionUserBypassEvent
NETWORK_UNCATEGORIZED
NetworkShareObjectAccessChecked
NETWORK_UNCATEGORIZED
NetworkShareObjectDeleted
NETWORK_UNCATEGORIZED
NetworkShareObjectModified
NETWORK_UNCATEGORIZED
AsrOfficeProcessInjectionAudited
SCAN_HOST
AppGuardCreateContainer
SCAN_HOST
AppGuardLaunchedWithUrl
SCAN_HOST
AsrAdobeReaderChildProcessAudited
SCAN_HOST
AsrAdobeReaderChildProcessBlocked
SCAN_HOST
AsrExecutableEmailContentAudited
SCAN_HOST
AsrOfficeChildProcessAudited
SCAN_HOST
AsrOfficeCommAppChildProcessAudited
SCAN_HOST
AsrPsexecWmiChildProcessAudited
SCAN_HOST
AsrScriptExecutableDownloadAudited
SCAN_HOST
AsrUntrustedUsbProcessAudited
SCAN_HOST
ExploitGuardChildProcessAudited
SCAN_HOST
ExploitGuardLowIntegrityImageAudited
SCAN_HOST
PowerShellCommand
PROCESS_LAUNCH
ProcessCreatedUsingWmiQuery
PROCESS_LAUNCH
QueueUserApcRemoteApiCall
PROCESS_LAUNCH
GetClipboardData
STATUS_UPDATE
OpenProcessApiCall
PROCESS_OPEN
ScriptContent
PROCESS_LAUNCH
AppControlAppInstallationBlocked
SCAN_HOST
AppGuardSuspendContainer
SCAN_HOST
AppGuardStopContainer
SCAN_HOST
AppLockerBlockExecutable
PROCESS_UNCATEGORIZED
AsrObfuscatedScriptAudited
SCAN_HOST
AsrObfuscatedScriptBlocked
SCAN_HOST
AsrOfficeChildProcessBlocked
SCAN_HOST
AsrOfficeProcessInjectionBlocked
SCAN_HOST
AsrPsexecWmiChildProcessBlocked
SCAN_HOST
AsrScriptExecutableDownloadBlocked
SCAN_HOST
AsrUntrustedUsbProcessBlocked
SCAN_HOST
ExploitGuardChildProcessBlocked
SCAN_HOST
ExploitGuardLowIntegrityImageBlocked
SCAN_HOST
ExploitGuardSharedBinaryAudited
SCAN_HOST
ExploitGuardSharedBinaryBlocked
SCAN_HOST
MemoryRemoteProtect
PROCESS_UNCATEGORIZED
NamedPipeEvent
PROCESS_UNCATEGORIZED
NtAllocateVirtualMemoryApiCall
PROCESS_UNCATEGORIZED
NtAllocateVirtualMemoryRemoteApiCall
PROCESS_UNCATEGORIZED
NtMapViewOfSectionRemoteApiCall
PROCESS_UNCATEGORIZED
NtProtectVirtualMemoryApiCall
PROCESS_UNCATEGORIZED
ProcessPrimaryTokenModified
PROCESS_UNCATEGORIZED
PTraceDetected
PROCESS_UNCATEGORIZED
ReadProcessMemoryApiCall
PROCESS_UNCATEGORIZED
SetThreadContextRemoteApiCall
PROCESS_UNCATEGORIZED
WriteProcessMemoryApiCall
PROCESS_UNCATEGORIZED
WriteToLsassProcessMemory
PROCESS_UNCATEGORIZED
AsrOfficeCommAppChildProcessBlocked
SCAN_HOST
AppControlCIScriptAudited
SCAN_HOST
AppControlCIScriptBlocked
SCAN_HOST
AppControlCodeIntegrityImageAudited
SCAN_HOST
AppControlCodeIntegrityImageRevoked
SCAN_HOST
AppControlCodeIntegrityOriginAllowed
SCAN_HOST
AppControlCodeIntegrityOriginAudited
SCAN_HOST
AppControlCodeIntegrityOriginBlocked
SCAN_HOST
AppControlScriptAudited
SCAN_HOST
AppControlScriptBlocked
SCAN_HOST
AsrExecutableEmailContentBlocked
SCAN_HOST
SafeDocFileScan
SCAN_FILE
AntivirusDefinitionsUpdated
SCAN_HOST
AntivirusDefinitionsUpdateFailed
SCAN_HOST
AntivirusDetection
SCAN_HOST
AntivirusDetectionActionType
SCAN_HOST
AntivirusEmergencyUpdatesInstalled
SCAN_HOST
AntivirusError
SCAN_HOST
AntivirusMalwareActionFailed
SCAN_HOST
AntivirusMalwareBlocked
SCAN_HOST
AntivirusReport
SCAN_HOST
AntivirusScanCancelled
SCAN_HOST
AntivirusScanCompleted
SCAN_HOST
AntivirusScanFailed
SCAN_HOST
AntivirusTroubleshootModeEvent
SCAN_HOST
AppControlCodeIntegrityDriverRevoked
SCAN_HOST
AppControlCodeIntegrityPolicyAudited
SCAN_HOST
AppControlCodeIntegrityPolicyBlocked
SCAN_HOST
AppControlCodeIntegrityPolicyLoaded
SCAN_HOST
AppControlCodeIntegritySigningInformation
SCAN_HOST
AppControlExecutableAudited
SCAN_HOST
AppControlExecutableBlocked
SCAN_HOST
AppControlPackagedAppAudited
SCAN_HOST
AppControlPackagedAppBlocked
SCAN_HOST
AccountCheckedForBlankPassword
SCAN_UNCATEGORIZED
SmartScreenAppWarning
SCAN_UNCATEGORIZED
SmartScreenExploitWarning
SCAN_HOST
SmartScreenUrlWarning
SCAN_UNCATEGORIZED
SmartScreenUserOverride
SCAN_UNCATEGORIZED
ScheduledTaskCreated
SCHEDULED_TASK_CREATION
ScheduledTaskDeleted
SCHEDULED_TASK_DELETION
ScheduledTaskDisabled
SCHEDULED_TASK_DISABLE
ScheduledTaskEnabled
SCHEDULED_TASK_ENABLE
ScheduledTaskUpdated
SCHEDULED_TASK_MODIFICATION
ServiceInstalled
SERVICE_CREATION
DirectoryServiceObjectCreated
SERVICE_MODIFICATION
DirectoryServiceObjectModified
SERVICE_MODIFICATION
AuditPolicyModification
SERVICE_MODIFICATION
CreateRemoteThreadApiCall
PROCESS_UNCATEGORIZED
CredentialsBackup
SERVICE_START
FirewallServiceStopped
SERVICE_STOP
BitLockerAuditCompleted
SERVICE_UNSPECIFIED
AppControlPolicyApplied
SCAN_HOST
AppGuardResumeContainer
SCAN_HOST
AppLockerBlockPackagedApp
STATUS_UPDATE
AppLockerBlockPackagedAppInstallation
STATUS_UPDATE
AppLockerBlockScript
STATUS_UPDATE
AsrExecutableOfficeContentBlocked
SCAN_HOST
AsrLsassCredentialTheftAudited
SCAN_HOST
AsrLsassCredentialTheftBlocked
SCAN_HOST
AsrOfficeMacroWin32ApiCallsAudited
SCAN_HOST
AsrOfficeMacroWin32ApiCallsBlocked
SCAN_HOST
AsrPersistenceThroughWmiAudited
SCAN_HOST
AsrPersistenceThroughWmiBlocked
SCAN_HOST
AsrRansomwareAudited
SCAN_HOST
AsrRansomwareBlocked
SCAN_HOST
AsrVulnerableSignedDriverAudited
SCAN_HOST
AsrVulnerableSignedDriverBlocked
SCAN_HOST
BluetoothPolicyTriggered
STATUS_UPDATE
ClrUnbackedModuleLoaded
PROCESS_MODULE_LOAD
ControlFlowGuardViolation
STATUS_UPDATE
DeviceBootAttestationInfo
STATUS_UPDATE
DriverLoad
PROCESS_MODULE_LOAD
ExploitGuardEafViolationAudited
SCAN_HOST
ExploitGuardEafViolationBlocked
SCAN_HOST
ExploitGuardIafViolationAudited
SCAN_HOST
ExploitGuardIafViolationBlocked
SCAN_HOST
ExploitGuardNonMicrosoftSignedAudited
SCAN_HOST
ExploitGuardNonMicrosoftSignedBlocked
SCAN_HOST
ExploitGuardRopExploitAudited
SCAN_HOST
ExploitGuardRopExploitBlocked
SCAN_HOST
ExploitGuardWin32SystemCallAudited
SCAN_HOST
ExploitGuardWin32SystemCallBlocked
SCAN_HOST
GetAsyncKeyStateApiCall
STATUS_UPDATE
OtherAlertRelatedActivity
STATUS_UPDATE
PnpDeviceAllowed
DEVICE_CONFIG_UPDATE
PnpDeviceBlocked
STATUS_UPDATE
PnpDeviceConnected
STATUS_UPDATE
PrintJobBlocked
STATUS_UPDATE
RemovableStoragePolicyTriggered
STATUS_UPDATE
SecurityLogCleared
SYSTEM_AUDIT_LOG_WIPE
TvmAxonTelemetryEvent
STATUS_UPDATE
UsbDriveMount
DEVICE_CONFIG_UPDATE
UsbDriveMounted
DEVICE_CONFIG_UPDATE
UsbDriveUnmount
DEVICE_CONFIG_UPDATE
UsbDriveUnmounted
DEVICE_CONFIG_UPDATE
WmiBindEventFilterToConsumer
STATUS_UPDATE
TamperingAttempt
SETTING_MODIFICATION
PasswordChangeAttempt
USER_CHANGE_PASSWORD
LogonRightsSettingEnabled
USER_CHANGE_PERMISSIONS
UserAccountCreated
USER_CREATION
UserAccountDeleted
USER_DELETION
LdapSearch
STATUS_UPDATE
ControlledFolderAccessViolationAudited
SCAN_FILE
ControlledFolderAccessViolationBlocked
SCAN_FILE
ExploitGuardAcgAudited
SCAN_HOST
ExploitGuardAcgEnforced
SCAN_HOST
UserAccountModified
USER_UNCATEGORIZED
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceEvents
The following table lists the log fields for the
DeviceEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
properties.ActionType
metadata.event_type
properties.ReportId
metadata.product_log_id
properties.LogonId
network.session_id
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.InitiatingProcessAccountDomain
principal.administrative_domain
If the
properties.ActionType
log field contains one of the following values, and the
properties.InitiatingProcessAccountDomain
log field value is
not
empty, then the
properties.InitiatingProcessAccountDomain
log field is mapped to the
target.administrative_domain
UDM field.
PasswordChangeAttempt
UserAccountCreated
UserAccountDeleted
Else, if the
properties.InitiatingProcessAccountDomain
log field value is
not
empty, then the
properties.InitiatingProcessAccountDomain
log field is mapped to the
principal.administrative_domain
UDM field.
properties.AccountDomain
principal.administrative_domain
If the
properties.ActionType
log field contains one of the following values, and the
properties.InitiatingProcessAccountDomain
log field value is empty, then the
properties.AccountDomain
log field is mapped to the
target.administrative_domain
UDM field.
PasswordChangeAttempt
UserAccountCreated
UserAccountDeleted
Else, if the
properties.InitiatingProcessAccountDomain
log field value is empty, then the
properties.AccountDomain
log field is mapped to the
principal.administrative_domain
UDM field.
properties.DeviceName
principal.hostname
properties.LocalIP
principal.ip
properties.FileOriginIP
principal.ip
properties.LocalPort
principal.port
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessId
principal.process.pid
properties.FileOriginUrl
principal.url
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
properties.InitiatingProcessAccountName
principal.user.userid
If the
properties.ActionType
log field contains one of the following values, and the
properties.InitiatingProcessAccountName
log field value is
not
empty, then the
properties.InitiatingProcessAccountName
log field is mapped to the
target.user.userid
UDM field.
PasswordChangeAttempt
UserAccountCreated
UserAccountDeleted
Else, if the
properties.InitiatingProcessAccountName
log field value is
not
empty, then the
properties.InitiatingProcessAccountName
log field is mapped to the
principal.user.userid
UDM field.
properties.AccountName
principal.user.userid
If the
properties.ActionType
log field contains one of the following values, and the
properties.InitiatingProcessAccountName
log field value is empty, then the
properties.AccountName
log field is mapped to the
target.user.userid
UDM field.
PasswordChangeAttempt
UserAccountCreated
UserAccountDeleted
Else, if the
properties.InitiatingProcessAccountName
log field value is empty, then the
properties.AccountName
log field is mapped to the
principal.user.userid
UDM field.
properties.InitiatingProcessAccountSid
principal.user.windows_sid
If the
properties.ActionType
log field contains one of the following values, and the
properties.InitiatingProcessAccountSid
log field value is
not
empty, then the
properties.InitiatingProcessAccountSid
log field is mapped to the
target.user.windows_sid
UDM field.
PasswordChangeAttempt
UserAccountCreated
UserAccountDeleted
Else, if the
properties.InitiatingProcessAccountSid
log field value is
not
empty, then the
properties.InitiatingProcessAccountSid
log field is mapped to the
principal.user.windows_sid
UDM field.
properties.AccountSid
principal.user.windows_sid
If the
properties.ActionType
log field contains one of the following values, and the
properties.InitiatingProcessAccountSid
log field value is empty, then the
properties.AccountSid
log field is mapped to the
target.user.windows_sid
UDM field.
PasswordChangeAttempt
UserAccountCreated
UserAccountDeleted
Else, if the
properties.InitiatingProcessAccountSid
log field value is empty, then the
properties.AccountSid
log field is mapped to the
principal.user.windows_sid
UDM field.
properties.ActionType
security_result.action
If the
properties.ActionType
log field value matches the regular expression pattern
(?i)Allow
, then the
security_result.action
UDM field is set to
ALLOW
.
Else if the
properties.ActionType
log field value matches the regular expression pattern
(?i)Block
, then the
security_result.action
UDM field is set to
BLOCK
.
Else if the
properties.ActionType
log field value matches the regular expression pattern
(?i)Fail
, then the
security_result.action
UDM field is set to
FAIL
.
properties.FolderPath
target.file.full_path
If the
properties.RemoteDeviceName
log field value contain one of the following values
ProcessCreatedUsingWmiQuery
OpenProcessApiCall
MemoryRemoteProtect
NtAllocateVirtualMemoryApiCall
NtAllocateVirtualMemoryRemoteApiCall
NtMapViewOfSectionRemoteApiCall
NtProtectVirtualMemoryApiCall
ProcessPrimaryTokenModified
ReadProcessMemoryApiCall
SetThreadContextRemoteApiCall
WriteProcessMemoryApiCall
WriteToLsassProcessMemory
CreateRemoteThreadApiCall
AsrOfficeProcessInjectionAudited
AsrAdobeReaderChildProcessAudited
AsrAdobeReaderChildProcessBlocked
AsrOfficeChildProcessAudited
AsrOfficeCommAppChildProcessAudited
AsrPsexecWmiChildProcessAudited
AsrUntrustedUsbProcessAudited
ExploitGuardChildProcessAudited
AsrOfficeChildProcessBlocked
AsrOfficeProcessInjectionBlocked
AsrPsexecWmiChildProcessBlocked
AsrUntrustedUsbProcessBlocked
ExploitGuardChildProcessBlocked
AsrOfficeCommAppChildProcessBlocked
and if the
properties.FolderPath
log field value matches the regular expression pattern
the
properties.FileName
log field value
then,
properties.FolderPath
log field is mapped to the
target.process.file.full_path
UDM field. Else,
%{properties.FolderPath}\%{properties.FileName}
log field is mapped to the
target.process.file.full_path
UDM field.
Else, if the
properties.FolderPath
log field value matches the regular expression pattern
the
properties.FileName
log field value
then,
properties.FolderPath
log field is mapped to the
target.file.full_path
UDM field. Else,
%{properties.FolderPath}\%{properties.FileName}
log field is mapped to the
target.file.full_path
UDM field.
properties.MD5
target.file.md5
If the
properties.RemoteDeviceName
log field value contain one of the following values
ProcessCreatedUsingWmiQuery
OpenProcessApiCall
MemoryRemoteProtect
NtAllocateVirtualMemoryApiCall
NtAllocateVirtualMemoryRemoteApiCall
NtMapViewOfSectionRemoteApiCall
NtProtectVirtualMemoryApiCall
ProcessPrimaryTokenModified
ReadProcessMemoryApiCall
SetThreadContextRemoteApiCall
WriteProcessMemoryApiCall
WriteToLsassProcessMemory
CreateRemoteThreadApiCall
AsrOfficeProcessInjectionAudited
AsrAdobeReaderChildProcessAudited
AsrAdobeReaderChildProcessBlocked
AsrOfficeChildProcessAudited
AsrOfficeCommAppChildProcessAudited
AsrPsexecWmiChildProcessAudited
AsrUntrustedUsbProcessAudited
ExploitGuardChildProcessAudited
AsrOfficeChildProcessBlocked
AsrOfficeProcessInjectionBlocked
AsrPsexecWmiChildProcessBlocked
AsrUntrustedUsbProcessBlocked
ExploitGuardChildProcessBlocked
AsrOfficeCommAppChildProcessBlocked
and if the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.MD5
log field is mapped to the
target.process.file.md5
UDM field.
Else, if the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.MD5
log field is mapped to the
target.file.md5
UDM field.
properties.FileName
target.file.names
If the
properties.RemoteDeviceName
log field value contain one of the following values
ProcessCreatedUsingWmiQuery
OpenProcessApiCall
MemoryRemoteProtect
NtAllocateVirtualMemoryApiCall
NtAllocateVirtualMemoryRemoteApiCall
NtMapViewOfSectionRemoteApiCall
NtProtectVirtualMemoryApiCall
ProcessPrimaryTokenModified
ReadProcessMemoryApiCall
SetThreadContextRemoteApiCall
WriteProcessMemoryApiCall
WriteToLsassProcessMemory
CreateRemoteThreadApiCall
AsrOfficeProcessInjectionAudited
AsrAdobeReaderChildProcessAudited
AsrAdobeReaderChildProcessBlocked
AsrOfficeChildProcessAudited
AsrOfficeCommAppChildProcessAudited
AsrPsexecWmiChildProcessAudited
AsrUntrustedUsbProcessAudited
ExploitGuardChildProcessAudited
AsrOfficeChildProcessBlocked
AsrOfficeProcessInjectionBlocked
AsrPsexecWmiChildProcessBlocked
AsrUntrustedUsbProcessBlocked
ExploitGuardChildProcessBlocked
AsrOfficeCommAppChildProcessBlocked
and if the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.FileName
log field is mapped to the
target.process.file.names
UDM field.
Else, if the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.FileName
log field is mapped to the
target.file.names
UDM field.
properties.SHA1
target.file.sha1
If the
properties.RemoteDeviceName
log field value contain one of the following values
ProcessCreatedUsingWmiQuery
OpenProcessApiCall
MemoryRemoteProtect
NtAllocateVirtualMemoryApiCall
NtAllocateVirtualMemoryRemoteApiCall
NtMapViewOfSectionRemoteApiCall
NtProtectVirtualMemoryApiCall
ProcessPrimaryTokenModified
ReadProcessMemoryApiCall
SetThreadContextRemoteApiCall
WriteProcessMemoryApiCall
WriteToLsassProcessMemory
CreateRemoteThreadApiCall
AsrOfficeProcessInjectionAudited
AsrAdobeReaderChildProcessAudited
AsrAdobeReaderChildProcessBlocked
AsrOfficeChildProcessAudited
AsrOfficeCommAppChildProcessAudited
AsrPsexecWmiChildProcessAudited
AsrUntrustedUsbProcessAudited
ExploitGuardChildProcessAudited
AsrOfficeChildProcessBlocked
AsrOfficeProcessInjectionBlocked
AsrPsexecWmiChildProcessBlocked
AsrUntrustedUsbProcessBlocked
ExploitGuardChildProcessBlocked
AsrOfficeCommAppChildProcessBlocked
and if the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.SHA1
log field is mapped to the
target.process.file.sha1
UDM field.
Else, if the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.SHA256
target.file.sha256
If the
properties.RemoteDeviceName
log field value contain one of the following values
ProcessCreatedUsingWmiQuery
OpenProcessApiCall
MemoryRemoteProtect
NtAllocateVirtualMemoryApiCall
NtAllocateVirtualMemoryRemoteApiCall
NtMapViewOfSectionRemoteApiCall
NtProtectVirtualMemoryApiCall
ProcessPrimaryTokenModified
ReadProcessMemoryApiCall
SetThreadContextRemoteApiCall
WriteProcessMemoryApiCall
WriteToLsassProcessMemory
CreateRemoteThreadApiCall
AsrOfficeProcessInjectionAudited
AsrAdobeReaderChildProcessAudited
AsrAdobeReaderChildProcessBlocked
AsrOfficeChildProcessAudited
AsrOfficeCommAppChildProcessAudited
AsrPsexecWmiChildProcessAudited
AsrUntrustedUsbProcessAudited
ExploitGuardChildProcessAudited
AsrOfficeChildProcessBlocked
AsrOfficeProcessInjectionBlocked
AsrPsexecWmiChildProcessBlocked
AsrUntrustedUsbProcessBlocked
ExploitGuardChildProcessBlocked
AsrOfficeCommAppChildProcessBlocked
and if the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
then,
properties.SHA256
log field is mapped to the
target.process.file.sha256
UDM field.
Else, if the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
then,
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.file.size
If the
properties.RemoteDeviceName
log field value contain one of the following values
ProcessCreatedUsingWmiQuery
OpenProcessApiCall
MemoryRemoteProtect
NtAllocateVirtualMemoryApiCall
NtAllocateVirtualMemoryRemoteApiCall
NtMapViewOfSectionRemoteApiCall
NtProtectVirtualMemoryApiCall
ProcessPrimaryTokenModified
ReadProcessMemoryApiCall
SetThreadContextRemoteApiCall
WriteProcessMemoryApiCall
WriteToLsassProcessMemory
CreateRemoteThreadApiCall
AsrOfficeProcessInjectionAudited
AsrAdobeReaderChildProcessAudited
AsrAdobeReaderChildProcessBlocked
AsrOfficeChildProcessAudited
AsrOfficeCommAppChildProcessAudited
AsrPsexecWmiChildProcessAudited
AsrUntrustedUsbProcessAudited
ExploitGuardChildProcessAudited
AsrOfficeChildProcessBlocked
AsrOfficeProcessInjectionBlocked
AsrPsexecWmiChildProcessBlocked
AsrUntrustedUsbProcessBlocked
ExploitGuardChildProcessBlocked
AsrOfficeCommAppChildProcessBlocked
and if the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.FileSize
log field is mapped to the
target.process.file.size
UDM field.
Else, if the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
then,
properties.FileSize
log field is mapped to the
target.file.size
UDM field.
properties.RemoteDeviceName
target.hostname
properties.RemoteIP
target.ip
properties.RemotePort
target.port
properties.ProcessCommandLine
target.process.command_line
properties.ProcessId
target.process.pid
properties.ProcessTokenElevation
target.process.token_elevation_type
If the
properties.ProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
target.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.ProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
target.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.ProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
target.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.RegistryKey
target.registry.registry_key
properties.RegistryValueData
target.registry.registry_value_data
properties.RegistryValueName
target.registry.registry_value_name
properties.RemoteUrl
target.url
properties.AdditionalFields
additional.fields[additional_fields]
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessLogonId
additional.fields[initiating_process_logon_id]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
properties.ProcessCreationTime
additional.fields[process_creation_time]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[process_version_info_product_version]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - AlertEvidence
The following table lists the log fields for the
AlertEvidence
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Application
additional.fields[application]
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_HOST
.
properties.DeviceId
principal.asset_id
If the
properties.DeviceId
log field value is
not
empty, then the
DeviceID:properties.DeviceId
log field is mapped to the
principal.asset_id
UDM field.
properties.DeviceName
principal.hostname
If the
properties.DeviceName
log field value is
not
empty then,
properties.DeviceName
log field is mapped to the
principal.hostname
UDM field.
Else, if the
properties.AdditionalFields.HostName
log field value is
not
empty then,
properties.AdditionalFields.HostName
log field is mapped to the
principal.hostname
UDM field.
Else, if the
properties.AdditionalFields.Host.HostName
log field value is
not
empty then,
properties.AdditionalFields.Host.HostName
log field is mapped to the
principal.hostname
UDM field.
Else, if the
properties.AdditionalFields.ImageFile.Host.HostName
log field value is
not
empty then,
AdditionalFields.ImageFile.Host.HostName
log field is mapped to the
principal.hostname
UDM field.
properties.LocalIP
principal.asset.ip
If the
properties.LocalIP
log field value is
not
empty, then the
properties.LocalIP
log field is mapped to the
principal.asset.ip
UDM field.
properties.FolderPath
target.file.full_path
If the
properties.FileName
log field value matches the regular expression pattern the
properties.FolderPath
, then the
properties.FolderPath
log field is mapped to the
target.file.full_path
UDM field.
Else, the
properties.FolderPath/properties.FileName
log field is mapped to the
target.file.full_path
UDM field.
properties.FileName
target.file.names
properties.SHA1
target.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^the
0-9a-f
log field value+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.SHA256
target.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^the
a-f0-9
, then 64$
, then the
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.file.size
properties.AccountDomain
principal.administrative_domain
properties.RemoteIP
target.ip
properties.AdditionalFields
additional.fields[additionalfields]
properties.ProcessCommandLine
target.process.command_line
properties.RegistryKey
target.registry.registry_key
properties.RegistryValueData
target.registry.registry_value_data
properties.RegistryValueName
target.registry.registry_value_name
properties.CloudPlatform
principal.resource.attribute.cloud.environment
If the
properties.CloudPlatform
log field value matches the regular expression pattern
/(?i)Amazon Web Services/
, then the
principal.resource.attribute.cloud.environment
UDM field is set to
AMAZON_WEB_SERVICES
.
Else, if the
properties.CloudPlatform
log field value matches the regular expression pattern
/(?i)Google Cloud Platform/
, then the
principal.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
Else, if the
properties.CloudPlatform
log field value matches the regular expression pattern
/(?i)Azure/
, then the
principal.resource.attribute.cloud.environment
UDM field is set to
MICROSOFT_AZURE
.
Else, the
principal.resource.attribute.cloud.environment
UDM field is set to
UNSPECIFIED_CLOUD_ENVIRONMENT
.
properties.SubscriptionId
principal.resource.attribute.labels[subscription_id]
properties.CloudResource
principal.resource.name
properties.ResourceID
principal.resource.product_object_id
principal.resource.resource_type
The
principal.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
properties.Categories
security_result.category_details
properties.Severity
security_result.severity
properties.Title
security_result.summary
properties.Title
security_result.threat_name
properties.Title
security_result.rule_name
properties.ThreatFamily
security_result.detection_fields[threat_family]
properties.RemoteUrl
target.url
properties.EvidenceDirection
principal.user.attribute.labels[evidence_direction]
properties.EvidenceRole
principal.user.attribute.labels[evidence_role]
properties.AccountObjectId
additional.fields[account_object_id]
properties.AccountUpn
principal.user.user_display_name
properties.AccountName
principal.user.userid
properties.AccountSid
principal.user.windows_sid
properties.Timestamp
metadata.event_timestamp
properties.EntityType
principal.resource.resource_subtype
properties.AlertId
metadata.product_log_id
properties.DetectionSource
security_result.about.resource.attribute.labels[detection_source]
properties.ServiceSource
security_result.about.resource.attribute.labels[service_source]
properties.AttackTechniques
security_result.attack_details.techniques.name
properties.ApplicationId
additional.fields[application_id]
properties.EmailSubject
network.email.subject
properties.NetworkMessageId
network.email.mail_id
properties.OAuthApplicationId
additional.fields[oauth_application_id]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - AlertInfo
The following table lists the log fields for the
AlertInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.AlertId
metadata.product_log_id
properties.AttackTechniques
security_result.attack_details.techniques.name
properties.DetectionSource
security_result.detection_fields[detection_source]
properties.ServiceSource
security_result.detection_fields[service_source]
properties.Severity
security_result.severity
If the
properties.Severity
log field value matches the regular expression pattern
(?i)(informational)
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
properties.Severity
log field value matches the regular expression pattern
(?i)(low)
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
properties.Severity
log field value matches the regular expression pattern
(?i)(medium)
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
properties.Severity
log field value matches the regular expression pattern
(?i)(high)
, then the
security_result.severity
UDM field is set to
HIGH
.
properties.Category
security_result.category_details
properties.Title
security_result.threat_name
properties.Title
security_result.rule_name
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceAlertEvents
The following table lists the log fields for the
DeviceAlertEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_HOST
.
properties.ReportId
security_result.detection_fields[report_id]
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.MachineGroup
principal.group.group_display_name
properties.DeviceName
principal.hostname
properties.AttackTechniques
security_result.attack_details.techniques.name
properties.Category
security_result.category_details
properties.AlertId
metadata.product_log_id
properties.MitreTechniques
security_result.detection_fields[mitre_techniques]
properties.Severity
security_result.severity
If the
properties.Severity
log field value is equal to
High
, then the
security_result.severity
UDM field is set to
HIGH
.
Else, if the
properties.Severity
log field value is equal to
Medium
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
properties.Severity
log field value is equal to
Low
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
properties.Severity
log field value is equal to
Informational
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
properties.Title
security_result.threat_name
properties.Title
security_result.rule_name
properties.RemoteIp
target.ip
properties.FileName
target.file.names
properties.SHA1
target.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.RemoteUrl
target.url
properties.Table
additional.fields[table]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileCertificateInfo
The following table lists the log fields for the
DeviceFileCertificateInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
properties.ReportId
metadata.product_log_id
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.SHA1
principal.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.Issuer
principal.file.signature_info.sigcheck.signers.cert_issuer
properties.Signer
principal.file.signature_info.sigcheck.signers.name
properties.IsSigned
principal.file.signature_info.sigcheck.verified
If the
properties.IsSigned
log field value is equal to
true
, then the
principal.file.signature_info.sigcheck.verified
UDM field is set to
TRUE
.
Else, the
principal.file.signature_info.sigcheck.verified
UDM field is set to
FALSE
.
properties.DeviceName
principal.hostname
properties.CertificateCountersignatureTime
additional.fields[certificate_countersignature_time]
properties.CertificateSerialNumber
additional.fields[certificate_serial_number]
properties.CertificateCreationTime
additional.fields[certification_creation_time]
properties.CertificateExpirationTime
additional.fields[certification_expiration_time]
properties.CrlDistributionPointUrls
additional.fields[crl_distribution_point_urls]
properties.IsRootSignerMicrosoft
additional.fields[is_root_signer_microsoft]
properties.IsTrusted
additional.fields[is_trusted]
properties.IssuerHash
additional.fields[issuer_hash]
properties.SignatureType
additional.fields[signature_type]
properties.SignerHash
additional.fields[signer_hash]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceImageLoadEvents
The following table lists the log fields for the
DeviceImageLoadEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
PROCESS_MODULE_LOAD
.
properties.ReportId
metadata.product_log_id
properties.InitiatingProcessAccountDomain
principal.administrative_domain
principal.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{principal.DeviceId}
.
properties.DeviceName
principal.hostname
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessId
principal.process.pid
properties.InitiatingProcessTokenElevation
principal.process.token_elevation_type
If the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
properties.InitiatingProcessAccountName
principal.user.userid
properties.InitiatingProcessAccountSid
principal.user.windows_sid
properties.FolderPath
target.process.file.full_path
If the
properties.FolderPath
log field value matches the regular expression pattern the
properties.FileName
, then the
properties.FolderPath
log field is mapped to the
target.process.file.full_path
UDM field.
Else, the
target.process.file.full_path
is set to
%{properties.FolderPath}/%{properties.FileName}
.
properties.MD5
target.process.file.md5
If the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.MD5
log field is mapped to the
target.process.file.md5
UDM field.
properties.FileName
target.process.file.names
properties.SHA1
target.process.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
target.process.file.sha1
UDM field.
properties.SHA256
target.process.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.SHA256
log field is mapped to the
target.process.file.sha256
UDM field.
properties.FileSize
target.process.file.size
properties.FolderPath
target.file.full_path
If the
properties.FolderPath
log field value matches the regular expression pattern the
properties.FileName
, then the
properties.FolderPath
log field is mapped to the
target.file.full_path
UDM field.
Else, the
target.file.full_path
is set to
%{properties.FolderPath}/%{properties.FileName}
.
properties.MD5
target.file.md5
If the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.MD5
log field is mapped to the
target.process.file.md5
UDM field.
properties.FileName
target.file.names
properties.SHA1
target.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.SHA256
target.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.file.size
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessIntegrityLevel
additional.fields[initiating_process_integrity_level]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[initiating_process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[initiating_process_version_info_product_version]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileEvents
The following table lists the log fields for the
DeviceFileEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
properties.ActionType
metadata.event_type
If the
properties.ActionType
log field value is equal to
FileCreated
, then the
metadata.event_type
UDM field is set to
FILE_CREATION
.
Else, if the
properties.ActionType
log field value is equal to
FileDeleted
, then the
metadata.event_type
UDM field is set to
FILE_DELETION
.
Else, if the
properties.ActionType
log field value is equal to
FileModified
, then the
metadata.event_type
UDM field is set to
FILE_MODIFICATION
.
Else, if the
properties.ActionType
log field value is equal to
FileRenamed
, then the
metadata.event_type
UDM field is set to
FILE_MOVE
.
properties.ReportId
metadata.product_log_id
properties.RequestProtocol
network.application_protocol
If the
properties.RequestProtocol
log field value is equal to
SMB
, then the
network.application_protocol
UDM field is set to
SMB
.
Else, if the
properties.RequestProtocol
log field value is equal to
NFS
, then the
network.application_protocol
UDM field is set to
NFS
.
Else, if the
properties.RequestProtocol
log field value is equal to
Local
, then the
network.application_protocol
UDM field is set to
UNKNOWN_APPLICATION_PROTOCOL
.
properties.FileOriginReferrerUrl
network.http.referral_url
properties.InitiatingProcessAccountDomain
principal.administrative_domain
If the
properties.InitiatingProcessAccountDomain
log field value is
not
empty, then the
properties.InitiatingProcessAccountDomain
log field is mapped to the
principal.administrative_domain
UDM field.
properties.RequestAccountDomain
principal.administrative_domain
If the
properties.InitiatingProcessAccountDomain
log field value is empty, then the
properties.RequestAccountDomain
log field is mapped to the
principal.administrative_domain
UDM field.
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceName
principal.hostname
properties.FileOriginIP
principal.ip
properties.RequestSourceIP
principal.ip
properties.RequestSourcePort
principal.port
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessId
principal.process.pid
properties.InitiatingProcessTokenElevation
principal.process.token_elevation_type
If the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.FileOriginUrl
principal.url
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
properties.InitiatingProcessAccountName
principal.user.userid
If the
properties.InitiatingProcessAccountName
log field value is
not
empty, then the
properties.InitiatingProcessAccountName
log field is mapped to the
principal.user.userid
UDM field.
properties.RequestAccountName
principal.user.userid
If the
properties.InitiatingProcessAccountName
log field value is empty, then the
properties.RequestAccountName
log field is mapped to the
principal.user.userid
UDM field.
properties.InitiatingProcessAccountSid
principal.user.windows_sid
If the
properties.InitiatingProcessAccountSid
log field value is
not
empty, then the
properties.InitiatingProcessAccountSid
log field is mapped to the
principal.user.windows_sid
UDM field.
properties.RequestAccountSid
principal.user.windows_sid
If the
properties.InitiatingProcessAccountSid
log field value is empty, then the
properties.RequestAccountSid
log field is mapped to the
principal.user.windows_sid
UDM field.
properties.PreviousFolderPath
src.file.full_path
If the
properties.PreviousFolderPath
log field value matches the regular expression pattern the
properties.PreviousFileName
log field value, then the
properties.PreviousFolderPath
log field is mapped to the
src.file.full_path
UDM field.
Else,
src.file.full_path
set to the
%{properties.PreviousFolderPath}/%{properties.PreviousFileName}
.
properties.PreviousFileName
src.file.names
properties.FolderPath
target.file.full_path
If the
properties.FolderPath
log field value matches the regular expression pattern the
properties.FileName
log field value, then the
properties.FolderPath
log field is mapped to the
target.file.full_path
UDM field.
Else, the
target.file.full_path
set to
%{properties.FolderPath}/%{properties.FileName}
.
properties.MD5
target.file.md5
If the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.MD5
log field is mapped to the
target.file.md5
UDM field.
properties.FileName
target.file.names
properties.SHA1
target.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.SHA256
target.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.file.size
properties.SensitivityLabel
target.file.tags
properties.SensitivitySubLabel
target.file.tags
properties.AdditionalFields
additional.fields[additional_fields]
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessIntegrityLevel
additional.fields[initiating_process_integrity_level]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[initiating_process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[initiating_process_version_info_product_version]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
properties.IsAzureInfoProtectionApplied
additional.fields[is_azure_info_protection_applied]
properties.ShareName
additional.fields[share_name]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceInfo
The following table lists the log fields for the
DeviceInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.DeviceId
entity.asset_id
The
entity.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceId
entity.asset.asset_id
The
entity.asset.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.AadDeviceId
entity.asset.attribute.labels[aad_device_id]
properties.AdditionalFields
entity.asset.attribute.labels[additional_fields]
properties.ConnectivityType
entity.asset.attribute.labels[connectivity_type]
properties.DeviceDynamicTags
entity.asset.attribute.labels[device_dynamic_tags]
properties.DeviceManualTags
entity.asset.attribute.labels[device_manual_tags]
properties.DeviceSubtype
entity.asset.attribute.labels[device_subtype]
properties.HostDeviceId
entity.asset.attribute.labels[host_device_id]
properties.IsAzureADJoined
entity.asset.attribute.labels[is_azure_ad_joined]
properties.IsInternetFacing
entity.asset.attribute.labels[is_internet_facing]
properties.JoinType
entity.asset.attribute.labels[join_type]
properties.MergedDeviceIds
entity.asset.attribute.labels[merged_device_ids]
properties.MergedToDeviceId
entity.asset.attribute.labels[merged_to_device_id]
properties.OnboardingStatus
entity.asset.attribute.labels[onboarding_status]
properties.OSArchitecture
entity.asset.attribute.labels[os_architecture]
properties.OSDistribution
entity.asset.attribute.labels[os_distribution]
properties.OSVersionInfo
entity.asset.attribute.labels[os_version_info]
properties.RegistryDeviceTag
entity.asset.attribute.labels[registry_divice_tag]
properties.ReportId
entity.asset.attribute.labels[report_id]
properties.SensorHealthState
entity.asset.attribute.labels[sensor_health_state]
properties.DeviceCategory
entity.asset.category
properties.Vendor
entity.asset.hardware.manufacturer
properties.Model
entity.asset.hardware.model
properties.DeviceName
entity.asset.hostname
properties.PublicIP
entity.asset.nat_ip
properties.OSBuild
entity.asset.platform_software.plateform_patch_level
properties.OSPlatform
entity.asset.platform_software.platform
If the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)macos
, then the
entity.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)windows
, then the
entity.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)linux
, then the
entity.asset.platform_software.platform
UDM field is set to
LINUX
.
properties.OSVersion
entity.asset.platform_software.platform_version
properties.ClientVersion
entity.asset.software.version
properties.DeviceType
entity.asset.type
If the
properties.DeviceType
log field value is equal to
NetworkDevice
, then the
entity.asset.type
UDM field is set to
NETWORK_ATTACHED_STORAGE
.
Else, if the
properties.DeviceType
log field value is equal to
Workstation
, then the
entity.asset.type
UDM field is set to
WORKSTATION
.
Else, if the
properties.DeviceType
log field value is equal to
Server
, then the
entity.asset.type
UDM field is set to
SERVER
.
Else, if the
properties.DeviceType
log field value is equal to
Mobile
, then the
entity.asset.type
UDM field is set to
MOBILE
.
Else if the
properties.DeviceType
log field value is equal to
Printer
, then the
entity.asset.type
UDM field is set to
PRINTER
.
properties.DeviceType
entity.asset.attribute.labels
if the
properties.DeviceType
log field value is equal to
GamingConsole
, then the
properties.DeviceType
log field is mapped to the
entity.asset.attribute.labels
UDM field.
properties.MachineGroup
entity.group.group_display_name
properties.ExclusionReason
entity.security_result.detection_fields[exclusion_reason]
properties.ExposureLevel
entity.security_result.detection_fields[exposure_level]
properties.IsExcluded
entity.security_result.detection_fields[is_excluded]
properties.AssetValue
entity.security_result.priority
If the
properties.AssetValue
log field value is equal to
High
, then the
entity.security_result.priority
UDM field is set to
HIGH_PRIORITY
.
Else, if the
properties.AssetValue
log field value is equal to
Medium
, then the
entity.security_result.priority
UDM field is set to
MEDIUM_PRIORITY
.
Else, if the
properties.AssetValue
log field value is equal to
Low
, then the
entity.security_result.priority
UDM field is set to
LOW_PRIORITY
.
Else, the
properties.AssetValue
log field is mapped to the
entity.security_result.detection_fields.asset_value
UDM field.
properties.Timestamp
metadata.creation_timestamp
metadata.entity_type
The
metadata.entity_type
UDM field is set to
ASSET
.
properties.DeviceId
metadata.product_entity_id
The
metadata.product_entity_id
is set to
DeviceID:%{properties.DeviceId}
.
relations.direction
The
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
relations.entity_type
The
relations.entity_type
UDM field is set to
USER
.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
.
properties.LoggedOnUsers.DomainName
relations.entity.domain.name
properties.LoggedOnUsers.UserName
relations.entity.user.userid
properties.LoggedOnUsers.Sid
relations.entity.user.windows_sid
properties.LoggedOnUsers
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceIdentityLogonEvents
The following table lists the log fields for the
DeviceIdentityLogonEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Application
additional.fields[application]
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_HOST
.
properties.DeviceId
principal.asset_id
If the
properties.DeviceId
log field value is
not
empty, then the
AssetID:properties.DeviceId
log field is mapped to the
principal.asset_id
UDM field. else, then the
AssetID:properties.AdditionalFields.MachineId
log field is mapped to the
principal.asset_id
UDM field.
properties.DeviceName
principal.hostname
If the
properties.DeviceName
log field value is
not
empty, then the
properties.DeviceName
log field is mapped to the
principal.hostname
UDM field.
properties.LocalIP
principal.asset.ip
If the
properties.LocalIP
log field value is
not
empty, then the
properties.LocalIP
log field is mapped to the
principal.asset.ip
UDM field.
properties.FolderPath
target.file.full_path
If the
properties.FileName
log field value matches the regular expression pattern the
properties.FolderPath
, then the
properties.FolderPath
log field is mapped to the
target.file.full_path
UDM field.
Else, the
properties.FolderPath/properties.FileName
log field is mapped to the
target.file.full_path
UDM field.
properties.FileName
target.file.names
properties.SHA1
target.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^the
0-9a-f
log field value+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.SHA256
target.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^the
a-f0-9
, then 64$
, then the
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.file.size
properties.AccountDomain
principal.administrative_domain
properties.RemoteIP
target.ip
properties.AdditionalFields
additional.fields[additionalfields]
properties.ProcessCommandLine
target.process.command_line
properties.RegistryKey
target.registry.registry_key
properties.RegistryValueData
target.registry.registry_value_data
properties.RegistryValueName
target.registry.registry_value_name
properties.CloudPlatform
principal.resource.attribute.cloud.environment
If the
properties.CloudPlatform
log field value matches the regular expression pattern
/(?i)Amazon Web Services/
, then the
principal.resource.attribute.cloud.environment
UDM field is set to
AMAZON_WEB_SERVICES
.
Else, if the
properties.CloudPlatform
log field value matches the regular expression pattern
/(?i)Google Cloud Platform/
, then the
principal.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
Else, if the
properties.CloudPlatform
log field value matches the regular expression pattern
/(?i)Azure/
, then the
principal.resource.attribute.cloud.environment
UDM field is set to
MICROSOFT_AZURE
.
Else, the
principal.resource.attribute.cloud.environment
UDM field is set to
UNSPECIFIED_CLOUD_ENVIRONMENT
.
properties.SubscriptionId
principal.resource.attribute.labels[subscription_id]
properties.CloudResource
principal.resource.name
properties.ResourceID
principal.resource.product_object_id
principal.resource.resource_type
The
principal.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
properties.Categories
security_result.category_details
properties.Severity
security_result.severity
properties.Title
security_result.summary
properties.ThreatFamily
security_result.threat_name
properties.RemoteUrl
target.url
properties.EvidenceDirection
principal.user.attribute.labels[evidence_direction]
properties.EvidenceRole
principal.user.attribute.labels[evidence_role]
properties.AccountObjectId
additional.fields[account_object_id]
properties.AccountUpn
principal.user.user_display_name
properties.AccountName
principal.user.userid
properties.AccountSid
principal.user.windows_sid
properties.Timestamp
metadata.event_timestamp
properties.EntityType
principal.resource.resource_subtype
properties.AlertId
metadata.product_log_id
properties.DetectionSource
security_result.about.resource.attribute.labels[detection_source]
properties.ServiceSource
security_result.about.resource.attribute.labels[service_source]
properties.AttackTechniques
security_result.attack_details.techniques.name
properties.ApplicationId
additional.fields[application_id]
properties.EmailSubject
network.email.subject
properties.NetworkMessageId
network.email.mail_id
properties.OAuthApplicationId
additional.fields[oauth_application_id]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceLogonEvents
The following table lists the log fields for the
DeviceLogonEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.LogonType
extensions.auth.mechanism
If the
properties.LogonType
log field value is equal to
Interactive
, then the
extensions.auth.mechanism
UDM field is set to
INTERACTIVE
.
Else, if the
properties.LogonType
log field value is equal to
Network
, then the
extensions.auth.mechanism
UDM field is set to
NETWORK
.
Else, if the
properties.LogonType
log field value is equal to
Batch
, then the
extensions.auth.mechanism
UDM field is set to
BATCH
.
Else, if the
properties.LogonType
log field value is equal to
Service
, then the
extensions.auth.mechanism
UDM field is set to
SERVICE
.
Else, if the
properties.LogonType
log field value is equal to
RemoteInteractive
, then the
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
properties.ReportId
metadata.product_log_id
properties.Protocol
network.ip_protocol
If the
properties.Protocol
log field value is equal to
Tcp
, then the
network.ip_protocol
UDM field is set to
TCP
.
If the
properties.Protocol
log field value is equal to
Udp
, then the
network.ip_protocol
UDM field is set to
UDP
.
If the
properties.Protocol
log field value is equal to
Icmp
, then the
network.ip_protocol
UDM field is set to
ICMP
.
properties.LogonId
network.session_id
properties.InitiatingProcessAccountDomain
principal.administrative_domain
properties.DeviceId
target.asset_id
The
target.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceName
target.hostname
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessId
principal.process.pid
properties.InitiatingProcessTokenElevation
principal.process.token_elevation_type
If the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
properties.InitiatingProcessAccountName
principal.user.userid
properties.InitiatingProcessAccountSid
principal.user.windows_sid
properties.FailureReason
security_result.description
properties.AccountDomain
target.administrative_domain
properties.RemoteDeviceName
principal.hostname
properties.RemoteIP
principal.ip
properties.RemotePort
principal.port
properties.IsLocalAdmin
target.resource.attribute.labels[is_local_admin]
properties.AccountName
target.user.userid
properties.AccountSid
target.user.windows_sid
properties.RemoteIPType
additional.fields[remote_ip_type]
properties.AdditionalFields
additional.fields[additional_fields]
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessIntegrityLevel
additional.fields[initiating_process_integrity_level]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[initiating_process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[initiating_process_version_info_product_version]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceNetworkEvents
The following table lists the log fields for the
DeviceNetworkEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
properties.ReportId
metadata.product_log_id
properties.Protocol
network.ip_protocol
If the
properties.Protocol
log field value is equal to
Tcp
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
properties.Protocol
log field value is equal to
Udp
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
properties.Protocol
log field value is equal to
Icmp
, then the
network.ip_protocol
UDM field is set to
ICMP
.
properties.InitiatingProcessAccountDomain
principal.administrative_domain
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceName
principal.hostname
properties.LocalIP
principal.ip
properties.LocalPort
principal.port
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessId
principal.process.pid
properties.InitiatingProcessTokenElevation
principal.process.token_elevation_type
If the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
properties.InitiatingProcessAccountName
principal.user.userid
properties.InitiatingProcessAccountSid
principal.user.windows_sid
properties.RemoteIP
target.ip
properties.RemotePort
target.port
properties.RemoteUrl
target.url
properties.LocalIPType
additional_fields[LocalIPType]
properties.RemoteIPType
additional_fields[RemoteIPType]
properties.AdditionalFields
additional.fields[additional_fields]
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessIntegrityLevel
additional.fields[initiating_process_integrity_level]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[initiating_process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[initiating_process_version_info_product_version]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceNetworkInfo
The following table lists the log fields for the
DeviceNetworkInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
DeviceNetworkInfo
properties.DeviceId
entity.asset_id
The
entity.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceId
entity.asset.asset_id
The
entity.asset.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.ReportId
entity.asset.attribute.labels[report_id]
properties.ConnectedNetworks
entity.asset.attribute.labels[connected_networks]
properties.MacAddress
entity.asset.mac
properties.NetworkAdapterName
entity.asset.attribute.labels[network_adapter_name]
properties.NetworkAdapterStatus
entity.asset.attribute.labels[network_adapter_status]
properties.NetworkAdapterType
entity.asset.attribute.labels[network_adapter_type]
properties.NetworkAdapterVendor
entity.asset.attribute.labels[network_adapter_vendor]
properties.TunnelType
entity.asset.attribute.labels[tunnel_type]
properties.DefaultGateways
entity.asset.attribute.labels[default_gateways]
properties.DeviceName
entity.asset.hostname
properties.IPAddresses
entity.asset.ip
entity.asset.type
The
entity.asset.type
UDM field is set to
WORKSTATION
.
properties.DnsAddresses
entity.domain.last_dns_records.type
The
entity.domain.last_dns_records.type
UDM field is set to
ip_address
.
properties.DnsAddresses
entity.domain.last_dns_records.value
The
properties.DnsAddresses
log field is mapped to the
entity.domain.last_dns_records.value
UDM field.
properties.IPv4Dhcp
entity.network.dhcp.ciaddr
If the
properties.IPv4Dhcp
log field value is
not
empty, then the
properties.IPv4Dhcp
log field is mapped to the
entity.network.dhcp.ciaddr
UDM field.
Else, the
properties.IPv6Dhcp
log field is mapped to the
entity.network.dhcp.ciaddr
UDM field.
properties.Timestamp
metadata.creation_time
metadata.entity_type
The
metadata.entity_type
UDM field is set to
ASSET
.
properties.DeviceId
metadata.product_entity_id
The
metadata.product_entity_id
is set to
DeviceID:%{properties.DeviceId}
.
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceProcessEvents
The following table lists the log fields for the
DeviceProcessEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
properties.ActionType
metadata.event_type
If the
properties.ActionType
log field value matches the regular expression pattern
(?i)ProcessCreated
, then the
metadata.event_type
UDM field is set to
PROCESS_LAUNCH
.
Else, if the
properties.ActionType
log field value matches the regular expression pattern
(?i)OpenProcess
, then the
metadata.event_type
UDM field is set to
PROCESS_OPEN
.
properties.ReportId
metadata.product_log_id
properties.LogonId
network.session_id
properties.InitiatingProcessAccountDomain
principal.administrative_domain
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceName
principal.hostname
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessSignatureStatus
principal.process.file.signature_info.sigcheck.signers.status
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessId
principal.process.pid
properties.InitiatingProcessTokenElevation
principal.process.token_elevation_type
If the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_3
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
properties.InitiatingProcessAccountName
principal.user.userid
properties.InitiatingProcessAccountSid
principal.user.windows_sid
properties.AccountDomain
target.administrative_domain
properties.FolderPath
target.file.full_path
If the
properties.FolderPath
log field value matches the regular expression pattern the
properties.FileName
log field value, then the
properties.FolderPath
log field is mapped to the
target.file.full_path
UDM field.
Else, the
target.file.full_path
set to
%{properties.FolderPath}/%{properties.FileName}
.
properties.MD5
target.process.file.md5
If the
properties.MD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.MD5
log field is mapped to the
target.file.md5
UDM field.
properties.FileName
target.process.file.names
properties.SHA1
target.process.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
target.file.sha1
UDM field.
properties.SHA256
target.process.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.process.file.size
properties.ProcessCommandLine
target.process.command_line
properties.ProcessId
target.process.pid
properties.ProcessTokenElevation
target.process.token_elevation_type
If the
properties.ProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
target.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.ProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
target.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.ProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
target.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.ProcessIntegrityLevel
target.resource.attribute.labels[process_integrity_level]
properties.AccountUpn
target.user.user_display_name
properties.AccountName
target.user.userid
properties.AccountSid
target.user.windows_sid
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
properties.AccountObjectId
additional.fields[account_object_id]
properties.AdditionalFields
additional.fields[additional_fields]
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessIntegrityLevel
additional.fields[initiating_process_integrity_level]
properties.InitiatingProcessLogonId
additional.fields[initiating_process_logon_id]
properties.InitiatingProcessSignerType
additional.fields[initiating_process_signer_type]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[initiating_process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[initiating_process_version_info_product_version]
properties.ProcessCreationTime
additional.fields[process_creation_time]
properties.ProcessVersionInfoCompanyName
target.process.file.exif_info.company
properties.ProcessVersionInfoFileDescription
target.process.file.exif_info.file_description
properties.ProcessVersionInfoInternalFileName
additional.fields[process_version_info_internal_file_name]
properties.ProcessVersionInfoOriginalFileName
target.process.file.exif_info.original_file
properties.ProcessVersionInfoProductName
target.process.file.exif_info.product
properties.ProcessVersionInfoProductVersion
additional.fields[process_version_info_product_version]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGathering
The following table lists the log fields for the
DeviceTvmInfoGathering
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_HOST
.
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.OSPlatform
principal.asset.platform_software.platform
If the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)macos
, then the
principal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)linux
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
properties.OSPlatform
principal.asset.platform_software.platform_version
properties.DeviceName
principal.hostname
properties.LastSeenTime
security.result.last_discovered_time
properties.AdditionalFields
additional.fields[additional_fields]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceRegistryEvents
The following table lists the log fields for the
DeviceRegistryEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
properties.ActionType
metadata.event_type
If the
properties.ActionType
log field value matches the regular expression pattern
(?i)RegistryKeyCreated
, then the
metadata.event_type
UDM field is set to
REGISTRY_CREATION
.
Else, if the
properties.ActionType
log field value matches the regular expression pattern
(?i)RegistryKeyDeleted
, then the
metadata.event_type
UDM field is set to
REGISTRY_DELETION
.
Else, if the
properties.ActionType
log field value matches the regular expression pattern
(?i)RegistryKeyRenamed
, then the
metadata.event_type
UDM field is set to
REGISTRY_MODIFICATION
.
Else, if the
properties.ActionType
log field value matches the regular expression pattern
(?i)RegistryValueDeleted
, then the
metadata.event_type
UDM field is set to
REGISTRY_DELETION
.
Else, if the
properties.ActionType
log field value matches the regular expression pattern
(?i)RegistryValueSet
, then the
metadata.event_type
UDM field is set to
REGISTRY_MODIFICATION
.
Else, the
metadata.event_type
UDM field is set to
REGISTRY_UNCATEGORIZED
.
properties.ReportId
metadata.product_log_id
properties.InitiatingProcessAccountDomain
principal.administrative_domain
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DeviceName
principal.hostname
properties.InitiatingProcessCommandLine
principal.process.command_line
properties.InitiatingProcessFolderPath
principal.process.file.full_path
If the
properties.InitiatingProcessFolderPath
log field value matches the regular expression pattern the
properties.InitiatingProcessFileName
log field value, then the
properties.InitiatingProcessFolderPath
log field is mapped to the
principal.process.file.full_path
UDM field.
Else, the
principal.process.file.full_path
is set to
%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}
.
properties.InitiatingProcessMD5
principal.process.file.md5
If the
properties.InitiatingProcessMD5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessMD5
log field is mapped to the
principal.process.file.md5
UDM field.
properties.InitiatingProcessFileName
principal.process.file.names
properties.InitiatingProcessSHA1
principal.process.file.sha1
If the
properties.InitiatingProcessSHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.InitiatingProcessSHA1
log field is mapped to the
principal.process.file.sha1
UDM field.
properties.InitiatingProcessSHA256
principal.process.file.sha256
If the
properties.InitiatingProcessSHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.InitiatingProcessSHA256
log field is mapped to the
principal.process.file.sha256
UDM field.
properties.InitiatingProcessFileSize
principal.process.file.size
properties.InitiatingProcessParentFileName
principal.process.parent_process.file.names
properties.InitiatingProcessParentId
principal.process.parent_process.pid
properties.InitiatingProcessId
principal.process.pid
properties.PreviousRegistryValueData
principal.registry.registry_value_data
properties.PreviousRegistryKey
principal.registry.registry_key
properties.PreviousRegistryValueName
principal.registry.registry_value_name
properties.InitiatingProcessAccountObjectId
principal.user.attribute.labels[initiating_process_account_object_id]
properties.InitiatingProcessAccountUpn
principal.user.attribute.labels[initiating_process_account_upn]
properties.InitiatingProcessAccountName
principal.user.userid
properties.InitiatingProcessAccountSid
principal.user.windows_sid
properties.InitiatingProcessTokenElevation
principal.process.token_elevation_type
If the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeFull
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_1
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeDefault
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_2
.
Else, if the
properties.InitiatingProcessTokenElevation
log field value is equal to
TokenElevationTypeLimited
, then the
principal.process.token_elevation_type
UDM field is set to
TYPE_3
.
properties.RegistryValueData
target.registry.registry_value_data
properties.RegistryKey
target.registry.registry_key
properties.RegistryValueName
target.registry.registry_value_name
properties.InitiatingProcessCreationTime
additional.fields[initiating_process_creation_time]
properties.InitiatingProcessIntegrityLevel
additional.fields[initiating_process_integrity_level]
properties.InitiatingProcessParentCreationTime
additional.fields[initiating_process_parent_creation_time]
properties.AppGuardContainerId
additional.fields[app_guard_container_id]
properties.InitiatingProcessVersionInfoCompanyName
principal.process.file.exif_info.company
properties.InitiatingProcessVersionInfoFileDescription
principal.process.file.exif_info.file_description
properties.InitiatingProcessVersionInfoInternalFileName
additional.fields[initiating_process_version_info_internal_file_name]
properties.InitiatingProcessVersionInfoOriginalFileName
principal.process.file.exif_info.original_file
properties.InitiatingProcessVersionInfoProductName
principal.process.file.exif_info.product
properties.InitiatingProcessVersionInfoProductVersion
additional.fields[initiating_process_version_info_product_version]
properties.RegistryValueType
additional.fields[registry_value_type]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGatheringKB
The following table lists the log fields for the
DeviceTvmInfoGatheringKB
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Description
metadata.description
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.IgId
metadata.product_log_id
properties.Categories
principal.resource.attribute.labels[categories]
properties.DataStructure
principal.resource.attribute.labels[data_structure]
properties.FieldName
principal.resource.name
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSecureConfigurationAssessment
The following table lists the log fields for the
DeviceTvmSecureConfigurationAssessment
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_UNCATEGORIZED
.
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.OSPlatform
principal.asset.platform_software.platform
If the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)macos
, then the
prinipal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)linux
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
properties.DeviceName
principal.hostname
properties.ConfigurationCategory
principal.resource.attribute.labels[configuration_category]
properties.ConfigurationImpact
principal.resource.attribute.labels[configuration_impact]
properties.Context
principal.resource.attribute.labels[contex]
properties.IsApplicable
principal.resource.attribute.labels[is_applicable]
properties.IsCompliant
principal.resource.attribute.labels[is_compliant]
properties.IsExpectedUserImpact
principal.resource.attribute.labels[is_expected_user_impact]
properties.ConfigurationId
principal.resource.product_object_id
properties.ConfigurationSubcategory
principal.resource.resource_subtype
principal.resource.resource_type
The
principal.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSecureConfigurationAssessmentKB
The following table lists the log fields for the
DeviceTvmSecureConfigurationAssessmentKB
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.ConfigurationBenchmarks
principal.resource.attribute.labels[configuration_benchmarks]
properties.ConfigurationCategory
principal.resource.attribute.labels[configuration_category]
properties.ConfigurationDescription
principal.resource.attribute.labels[configuration_description]
properties.ConfigurationImpact
principal.resource.attribute.labels[configuration_impact]
properties.RemediationOptions
principal.resource.attribute.labels[remediation_options]
properties.RiskDescription
principal.resource.attribute.labels[risk_description]
properties.Tags
principal.resource.attribute.labels[tags]
properties.ConfigurationName
principal.resource.name
properties.ConfigurationId
principal.resource.product_object_id
properties.ConfigurationSubcategory
principal.resource.resource_subtype
principal.resource.resource_type
The
principal.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareEvidenceBeta
The following table lists the log fields for the
DeviceTvmSoftwareEvidenceBeta
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.DiskPaths
principal.asset.attribute.labels[disk_paths]
The
properties.DiskPaths
log field is mapped to the
principal.asset.attribute.labels.disk_paths
UDM field.
properties.RegistryPaths
principal.asset.attribute.labels[registry_paths]
The
properties.RegistryPaths
log field is mapped to the
principal.asset.attribute.labels.registry_paths
UDM field.
properties.LastSeenTime
principal.asset.last_discover_time
properties.SoftwareName
principal.asset.software.name
properties.SoftwareVendor
principal.asset.software.vendor_name
properties.SoftwareVersion
principal.asset.software.version
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareInventory
The following table lists the log fields for the
DeviceTvmSoftwareInventory
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.EndOfSupportDate
principal.asset.attribute.labels[end_of_support_date]
properties.EndOfSupportStatus
principal.asset.attribute.labels[end_of_support_status]
properties.OSArchitecture
principal.asset.attribute.labels[os_architecture]
properties.ProductCodeCpe
principal.asset.attribute.labels[product_code_cpe]
properties.OSPlatform
principal.asset.platform_software.platform
If the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)macos
, then the
prinipal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)linux
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
properties.OSVersion
principal.asset.platform_software.platform_version
properties.SoftwareName
principal.asset.software.name
properties.SoftwareVendor
principal.asset.software.vendor_name
properties.SoftwareVersion
principal.asset.software.version
properties.DeviceName
principal.hostname
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareVulnerabilities
The following table lists the log fields for the
DeviceTvmSoftwareVulnerabilities
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.CveId
extensions.vulns.vulnerabilities.cve_id
properties.VulnerabilityLevel
extensions.vulns.vulnerabilities.severity
If the
properties.VulnerabilityLevel
log field value is equal to
High
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
HIGH
.
Else, if the
properties.VulnerabilityLevel
log field value is equal to
Medium
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
MEDIUM
.
Else, if the
properties.VulnerabilityLevel
log field value is equal to
Low
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
LOW
.
Else, if the
properties.VulnerabilityLevel
log field value is equal to
Informational
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
INFORMATIONAL
.
properties.SeverityLevel
extensions.vulns.vulnerablitities.severity_details
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_VULN_HOST
.
properties.DeviceId
principal.asset_id
The
principal.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.OSPlatform
principal.asset.platform_software.platform
If the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)macos
, then the
principal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)linux
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
properties.OSVersion
principal.asset.platform_software.platform_version
properties.SoftwareName
principal.asset.software.name
properties.SoftwareVendor
principal.asset.software.vendor_name
properties.SoftwareVersion
principal.asset.software.version
properties.DeviceName
principal.hostname
properties.RecommendedSecurityUpdateId
security_result.detection_fields[recommended_security_update_id]
properties.RecommendedSecurityUpdate
security_result.detection_fields[recommended_security_update]
properties.CveTags
additional.fields[cve_tags]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareVulnerabilitiesKB
The following table lists the log fields for the
DeviceTvmSoftwareVulnerabilitiesKB
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.CveId
extensions.vulns.vulnerabilities.cve_id
properties.CvssScore
extensions.vulns.vulnerablities.cvss_base_score
properties.IsExploitAvailable
extensions.vulns.vulnerablities.cvss_vector
properties.VulnerabilitySeverityLevel
extensions.vulns.vulnerabilities.severity
If the
properties.VulnerabilitySeverityLevel
log field value is equal to
High
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
HIGH
.
Else, if the
properties.VulnerabilitySeverityLevel
log field value is equal to
Medium
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
MEDIUM
.
Else, if the
properties.VulnerabilitySeverityLevel
log field value is equal to
Low
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
LOW
.
Else, if the
properties.VulnerabilitySeverityLevel
log field value is equal to
Informational
, then the
extensions.vulns.vulnerabilities.severity
UDM field is set to
INFORMATIONAL
.
Else, the
extensions.vulns.vulnerabilities.severity
UDM field is set to
UNKNOWN_SEVERITY
.
properties.VulnerabilitySeverityLevel
extensions.vulns.vulnerablitities.severity_details
properties.LastModifiedTime
extensions.vulns.vulnerabilities.scan_end_time
properties.PublishedDate
extensions.vulns.vulnerabilities.first_found
properties.VulnerabilityDescription
extensions.vulns.vulnerabilities.cve_description
properties.AffectedSoftware
extensions.vulns.vulnerabilities.description
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailAttachmentInfo
The following table lists the log fields for the
EmailAttachmentInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.FileType
target.file.mime_type
properties.FileName
target.file.names
properties.SHA256
target.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.SHA256
log field is mapped to the
target.file.sha256
UDM field.
properties.FileSize
target.file.size
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
properties.ReportId
metadata.product_log_id
properties.SenderFromAddress
network.email.from
If the
properties.SenderFromAddress
log field value matches the regular expression pattern
^.+@.+$
and the length of the value is 256 characters or less, then the
properties.SenderFromAddress
log field is mapped to the
network.email.from
UDM field.
Else, the
additional.fields.key
UDM field is set to
SenderFromAddress
and the
properties.SenderFromAddress
log field value is mapped to the
additional.fields.value.string_value
UDM field.
properties.NetworkMessageId
network.email.mail_id
properties.RecipientEmailAddress
network.email.to
If the
properties.RecipientEmailAddress
log field value matches the regular expression pattern
^.+@.+$
and the length of the value is 256 characters or less, then the
properties.RecipientEmailAddress
log field is mapped to the
network.email.to
UDM field.
Else, the
additional.fields.key
UDM field is set to
RecipientEmailAddress
and the
properties.RecipientEmailAddress
log field value is mapped to the
additional.fields.value.string_value
UDM field.
properties.SenderFromAddress
principal.user.email_addresses
If the
properties.SenderFromAddress
log field value matches the regular expression pattern
^.+@.+$
, then the
properties.SenderFromAddress
log field is mapped to the
principal.user.email_addresses
UDM field.
properties.SenderObjectId
principal.user.product_object_id
properties.SenderDisplayName
principal.user.user_display_name
properties.ThreatTypes
security_result.category
If the
properties.ThreatTypes
log field value is equal to
Phish
, then the
security_result.category
UDM field is set to
MAIL_PHISHING
.
properties.DetectionMethods
security_result.detection_fields[detection_methods]
properties.ThreatNames
security_result.threat_name
properties.RecipientEmailAddress
target.user.email_addresses
If the
properties.RecipientEmailAddress
log field value matches the regular expression pattern
^.+@.+$
, then the
properties.RecipientEmailAddress
log field is mapped to the
target.user.email_addresses
UDM field.
properties.RecipientObjectId
target.user.product_object_id
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailEvents
The following table lists the log fields for the
EmailEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
properties.ReportId
metadata.product_log_id
properties.EmailDirection
network.direction
If the
properties.EmailDirection
log field value is equal to
Inbound
, then the
network.direction
UDM field is set to
INBOUND
.
Else, if the
properties.EmailDirection
log field value is equal to
Outbound
, then the
network.direction
UDM field is set to
OUTBOUND
.
Else, the
network.direction
UDM field is set to
UNKNOWN_DIRECTION
.
properties.NetworkMessageId
network.email.mail_id
properties.Subject
network.email.subject
properties.RecipientEmailAddress
network.email.to
properties.SenderFromDomain
principal.administrative_domain
properties.SenderIPv4
principal.ip
properties.SenderIPv6
principal.ip
properties.SenderMailFromAddress
principal.user.attribute.labels[sender_mail_from_address]
properties.SenderFromAddress
network.email.from
If the
properties.SenderFromAddress
log field value matches the regular expression pattern
^.+@.+$
and the length of the value is 256 characters or less, then the
properties.SenderFromAddress
log field is mapped to the
network.email.from
UDM field.
Else, the
additional.fields.key
UDM field is set to
SenderFromAddress
and the
properties.SenderFromAddress
log field value is mapped to the
additional.fields.value.string_value
UDM field.
properties.SenderFromAddress
principal.user.email_addresses
If the
properties.SenderFromAddress
log field value matches the regular expression pattern
^.+@.+$
, then the
properties.SenderFromAddress
log field is mapped to the
principal.user.email_addresses
UDM field.
properties.SenderMailFromDomain
principal.user.attribute.labels[sender_mail_from_domain]
properties.SenderObjectId
principal.user.product_object_id
properties.SenderDisplayName
principal.user.user_display_name
properties.ThreatTypes
security_result.category
If the
properties.ThreatTypes
log field value is equal to
Phish
, then the
security_result.category
UDM field is set to
MAIL_PHISHING
.
properties.ThreatTypes
security_result.category_details
properties.ConfidenceLevel
security_result.confidence_details
properties.EmailAction
security_result.description
properties.AuthenticationDetails
security_result.detection_fields[authentication_details]
properties.BulkComplaintLevel
security_result.detection_fields[bulk_complaint_level]
properties.DetectionMethods
security_result.detection_fields[detection_methods]
properties.EmailActionPolicyGuid
security_result.rule_id
properties.EmailActionPolicy
security_result.rule_name
properties.ThreatNames
security_result.threat_name
properties.OrgLevelAction
security_result.rule_labels[org_level_action]
properties.OrgLevelPolicy
security_result.rule_labels[org_level_policy]
properties.UserLevelAction
security_result.rule_labels[user_level_action]
properties.UserLevelPolicy
security_result.rule_labels[user_level_policy]
properties.RecipientEmailAddress
network.email.to
If the
properties.RecipientEmailAddress
log field value matches the regular expression pattern
^.+@.+$
and the length of the value is 256 characters or less, then the
properties.RecipientEmailAddress
log field is mapped to the
network.email.to
UDM field.
Else, the
additional.fields.key
UDM field is set to
RecipientEmailAddress
and the
properties.RecipientEmailAddress
log field value is mapped to the
additional.fields.value.string_value
UDM field.
properties.RecipientEmailAddress
target.user.email_addresses
If the
properties.RecipientEmailAddress
log field value matches the regular expression pattern
^.+@.+$
, then the
properties.RecipientEmailAddress
log field is mapped to the
target.user.email_addresses
UDM field.
properties.RecipientObjectId
target.user.product_object_id
properties.AdditionalFields
additional.fields[additional_fields]
properties.DeliveryAction
additional.fields[delivery_action]
properties.DeliveryLocation
additional.fields[delivery_location]
The
properties.DeliveryLocation
log field is mapped to the
additional.fields.delivery_location
UDM field.
properties.EmailClusterId
additional.fields[email_cluster_id]
properties.EmailLanguage
additional.fields[email_language]
properties.InternetMessageId
additional.fields[internet_message_id]
properties.LatestDeliveryLocation
additional.fields[last_delivery_location]
properties.UrlCount
additional.fields[connectors]
properties.Connectors
additional.fields[attachment_count]
properties.AttachmentCount
additional.fields[latest_delivery_action]
properties.LatestDeliveryAction
additional.fields[latest_delivery_action]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailPostDeliveryEvents
The following table lists the log fields for the
EmailPostDeliveryEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
EMAIL_UNCATEGORIZED
.
properties.ReportId
security_result.detection_fields[report_id]
properties.NetworkMessageId
network.email.mail_id
properties.ActionResult
security_result.summary
properties.ThreatTypes
security_result.category
If the
properties.ThreatTypes
log field value is equal to
Phish
, then the
security_result.category
UDM field is set to
MAIL_PHISHING
.
properties.ThreatTypes
security_result.category_details
properties.ActionTrigger
security_result.detection_fields[action_trigger]
properties.DeliveryLocation
security_result.detection_fields[delivery_location]
properties.DetectionMethods
security_result.detection_fields[detection_methods]
properties.Action
security_result.action_details
properties.ActionType
security_result.verdict_info.verdict_type
If the
properties.ActionType
log field value is equal to
Manual Remediation
, then the
security_result.verdict_info.verdict_type
UDM field is set to
ANALYST_VERDICT
.
Else, if the
properties.ActionType
log field contains one of the following values, then the
security_result.verdict_info.verdict_type
UDM field is set to
PROVIDER_ML_VERDICT
.
Phish ZAP
Malware ZAP
Spam ZAP
.
properties.RecipientEmailAddress
target.user.email_addresses
If the
properties.RecipientEmailAddress
log field value matches the regular expression pattern
^.+@.+$
, then the
properties.RecipientEmailAddress
log field is mapped to the
target.user.email_addresses
UDM field.
properties.InternetMessageId
additional.fields[internet_message_id]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailUrlInfo
The following table lists the log fields for the
EmailUrlInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.UrlDomain
target.hostname
properties.Url
target.url
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
properties.ReportId
metadata.product_log_id
properties.NetworkMessageId
network.email.mail_id
properties.UrlLocation
additional.fields[url_location]
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - IdentityInfo
The following table lists the log fields for the
IdentityInfo
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.SourceSystem
entity.resource.parent
properties.AccountDomain
entity.administrative_domain
properties.TenantId
entity.resource.product_object_id
properties.CreatedDateTime
entity.user.attribute.creation_time
properties.AccountUpn
entity.user.attribute.labels[account_upn]
properties.ChangeSource
entity.user.attribute.labels[change_source]
properties.CloudSid
entity.user.attribute.labels[cloud_sid]
properties.ReportId
entity.user.attribute.labels[report_id]
properties.SipProxyAddress
entity.user.attribute.labels[sip_proxy_address]
properties.SourceProvider
entity.user.attribute.labels[source_provider]
properties.Tags
entity.user.attribute.labels[tags]
properties.Type
entity.user.attribute.role.name
properties.DistinguishedName
entity.user.attributes.labels[distinguished_name]
properties.Department
entity.user.department
properties.EmailAddress
entity.user.email_addresses
If the
properties.EmailAddress
log field value matches the regular expression pattern
^.+@.+$
, then the
properties.EmailAddress
log field is mapped to the
entity.user.email_addresses
UDM field.
properties.GivenName
entity.user.first_name
properties.Surname
entity.user.last_name
properties.Manager
entity.user.managers.user_display_name
properties.City
entity.user.personal_address.city
properties.Country
entity.user.personal_address.country_or_region
properties.Address
entity.user.personal_address.name
properties.Phone
entity.user.phone_numbers
properties.AccountObjectId
entity.user.product_object_id
properties.AssignedRoles
entity.user.role_description
properties.JobTitle
entity.user.title
properties.IsAccountEnabled
entity.user.user_authentication_status
If the
properties.IsAccountEnabled
log field value is equal to
1
or
true
, then the
entity.user.user_authentication_status
UDM field is set to
ACTIVE
.
Else, the
entity.user.user_authentication_status
UDM field is set to
SUSPENDED
.
properties.AccountDisplayName
entity.user.user_display_name
properties.AccountName
entity.user.userid
properties.OnPremSid
entity.user.attribute.labels[on_prem_sid]
properties.Timestamp
metadata.creation_time
metadata.entity_type
The
metadata.entity_type
UDM field is set to
USER
.
properties.AccountObjectId
metadata.product_entity_id
Field mapping reference: MICROSOFT DEFENDER ENDPOINT - CloudAppEvents
The following table lists the log fields for the
CloudAppEvents
log type and their corresponding UDM fields:
Log field
UDM mapping
Logic
properties.Timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
properties.ActionType
security_result.summary
properties.Application
additional.fields[application]
properties.ApplicationId
additional.fields[application_id]
properties.AppInstanceId
additional.fields[app_instance_id]
properties.AccountObjectId
principal.user.product_object_id
properties.AccountId
principal.user.userid
properties.AccountDisplayName
principal.user.user_display_name
properties.IsAdminOperation
principal.user.attribute.role.type
If the
properties.IsAdminOperation
is equal to
true
, then the
principal.user.attribute.role.type
is set to
ADMINISTRATOR
.
properties.DeviceType
principal.asset.type
If the
properties.DeviceType
log field value is equal to
NetworkDevice
, then the
principal.asset.type
UDM field is set to
NETWORK_ATTACHED_STORAGE
.
Else, if the
properties.DeviceType
log field value is equal to
Workstation
, then the
principal.asset.type
UDM field is set to
WORKSTATION
.
Else, if the
properties.DeviceType
log field value is equal to
Server
, then the
principal.asset.type
UDM field is set to
SERVER
.
Else, if the
properties.DeviceType
log field value is equal to
Mobile
, then the
principal.asset.type
UDM field is set to
MOBILE
.
Else if the
properties.DeviceType
log field value is equal to
Printer
, then the
principal.asset.type
UDM field is set to
PRINTER
.
properties.DeviceType
principal.asset.attribute.labels
if the
properties.DeviceType
log field value is equal to
GamingConsole
, then the
properties.DeviceType
log field is mapped to the
principal.asset.attribute.labels
UDM field.
properties.OSPlatform
principal.asset.platform_software.platform
If the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)macos
, then the
principal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
properties.OSPlatform
log field value matches the regular expression pattern
(?i)linux
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
properties.OSPlatform
principal.asset.platform_software.platform_version
properties.IPAddresses
principal.ip
properties.IsAnonymousProxy
principal.asset.attribute.labels[is_anonymous_proxy]
The
properties.IsAnonymousProxy
log field is mapped to the
principal.asset.attribute.labels[is_anonymous_proxy]
UDM field.
properties.CountryCode
principal.ip_geo_artifact.location.country_or_region
properties.City
principal.ip_geo_artifact.location.city
properties.Isp
principal.asset.attribute.labels[isp]
The
properties.Isp
log field is mapped to the
principal.asset.attribute.labels[isp]
UDM field.
properties.UserAgent
network.http.user_agent
properties.ActivityType
additional.fields[activity_type]
properties.ActivityObjects
additional.fields[activity_objects]
properties.ObjectName
target.resource.name
properties.ObjectType
target.resource.resource_subtype
properties.ObjectId
target.resource.product_object_id
properties.ReportId
metadata.product_log_id
properties.AccountType
principal.asset.attribute.labels[account_type]
The
properties.AccountType
log field is mapped to the
principal.asset.attribute.labels[account_type]
UDM field.
properties.IsExternalUser
principal.asset.attribute.labels[is_external_user]
The
properties.IsExternalUser
log field is mapped to the
principal.asset.attribute.labels[is_external_user]
UDM field.
properties.IsImpersonated
principal.asset.attribute.labels[is_impersonated]
The
properties.IsImpersonatedr
log field is mapped to the
principal.asset.attribute.labels[is_impersonated]
UDM field.
properties.IPTags
principal.asset.attribute.labels[ip_tags]
The
properties.IPTags
log field is mapped to the
principal.asset.attribute.labels[ip_tags]
UDM field.
properties.IPCategory
principal.asset.attribute.labels[ip_category]
The
properties.IPCategory
log field is mapped to the
principal.asset.attribute.labels[ip_category]
UDM field.
properties.UserAgentTags
principal.asset.attribute.labels[user_agent_tags]
The
properties.UserAgentTags
log field is mapped to the
principal.asset.attribute.labels[user_agent_tags]
UDM field.
properties.RawEventData
additional.fields[raw_event_data]
Iterate for each key, value pair of log field
properties.RawEventData
, then
value
log field is mapped to the
additional.fields.key
UDM field.
Iterate for each key1, value1 pair of log field
value
, then
value1
log field is mapped to the
additional.fields.key
UDM field.
Iterate for each key2, value2 pair of log field
value1
, then
value2
log field is mapped to the
additional.fields.key
UDM field.
Iterate for each key3, value3 pair of log field
value2
, then
value3
log field is mapped to the
additional.fields.key
UDM field.
properties.AdditionalFields
additional.fields[additional_fields]
Iterate for each key, value pair of log field
properties.AdditionalFields
, then
value
log field is mapped to the
additional.fields.key
UDM field.
properties.LastSeenForUser
additional.fields[last_seen_for_user]
Iterate for each key, value pair of log field
properties.LastSeenForUser
, then
value
log field is mapped to the
additional.fields.key
UDM field.
properties.UncommonForUser
additional.fields[uncommon_for_user]
Iterate for each key, value pair of log field
properties.UncommonForUser
, then
value
log field is mapped to the
additional.fields.key
UDM field.
properties.AuditSource
additional.fields[audit_source]
properties.SessionData
additional.fields[session_data]
properties.OAuthAppId
additional.fields[oauth_app_id]
UDM Mapping Delta
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT
The following tables lists the delta between the old UDM Mapping of
Microsoft Defender Endpoint
and the new UDM Mapping of
Microsoft Defender Endpoint
.
UDM Mapping Delta reference: DeviceEvents Event Identifier to Event Type
The following table lists the delta of
DeviceEvents
log action types and their corresponding UDM event types.
Event Identifier
Old UDM Event Type Mapping
New UDM Event Type Mapping
AppControlPolicyApplied
SCAN_HOST
DEVICE_CONFIG_UPDATE
NetworkProtectionUserBypassEvent
NETWORK_UNCATEGORIZED
DEVICE_CONFIG_UPDATE
AppControlCodeIntegritySigningInformation
SCAN_HOST
GENERIC_EVENT
DeviceBootAttestationInfo
STATUS_UPDATE
GENERIC_EVENT
LdapSearch
STATUS_UPDATE
NETWORK_CONNECTION
ExploitGuardNetworkProtectionAudited
SCAN_HOST
NETWORK_UNCATEGORIZED
ExploitGuardNetworkProtectionBlocked
SCAN_HOST
NETWORK_UNCATEGORIZED
FirewallInboundConnectionBlocked
NETWORK_CONNECTION
NETWORK_UNCATEGORIZED
FirewallInboundConnectionToAppBlocked
NETWORK_CONNECTION
NETWORK_UNCATEGORIZED
FirewallOutboundConnectionBlocked
NETWORK_CONNECTION
NETWORK_UNCATEGORIZED
AsrOfficeProcessInjectionAudited
SCAN_HOST
PROCESS_INJECTION
AppGuardCreateContainer
SCAN_HOST
PROCESS_LAUNCH
AppGuardLaunchedWithUrl
SCAN_HOST
PROCESS_LAUNCH
AsrExecutableEmailContentAudited
SCAN_HOST
PROCESS_LAUNCH
AsrExecutableOfficeContentAudited
SCAN_HOST
PROCESS_LAUNCH
AsrOfficeChildProcessAudited
SCAN_HOST
PROCESS_LAUNCH
AsrOfficeCommAppChildProcessAudited
SCAN_HOST
PROCESS_LAUNCH
AsrPsexecWmiChildProcessAudited
SCAN_HOST
PROCESS_LAUNCH
AsrScriptExecutableDownloadAudited
SCAN_HOST
PROCESS_LAUNCH
AsrUntrustedExecutableAudited
SCAN_HOST
PROCESS_LAUNCH
AsrUntrustedUsbProcessAudited
SCAN_HOST
PROCESS_LAUNCH
BrowserLaunchedToOpenUrl
NETWORK_UNCATEGORIZED
PROCESS_LAUNCH
ExploitGuardChildProcessAudited
SCAN_HOST
PROCESS_LAUNCH
ExploitGuardLowIntegrityImageAudited
SCAN_HOST
PROCESS_LAUNCH
ExploitGuardNonMicrosoftSignedAudited
SCAN_HOST
PROCESS_LAUNCH
ExploitGuardSharedBinaryAudited
SCAN_HOST
PROCESS_LAUNCH
AppControlCIScriptBlocked
SCAN_HOST
PROCESS_TERMINATION
AppControlExecutableBlocked
SCAN_HOST
PROCESS_TERMINATION
AppControlPackagedAppBlocked
SCAN_HOST
PROCESS_TERMINATION
AppControlScriptBlocked
SCAN_HOST
PROCESS_TERMINATION
AppGuardStopContainer
SCAN_HOST
PROCESS_TERMINATION
AppGuardSuspendContainer
SCAN_HOST
PROCESS_TERMINATION
AppLockerBlockExecutable
PROCESS_UNCATEGORIZED
PROCESS_TERMINATION
AppLockerBlockPackagedApp
STATUS_UPDATE
PROCESS_TERMINATION
AppLockerBlockPackagedAppInstallation
STATUS_UPDATE
PROCESS_TERMINATION
AppLockerBlockScript
STATUS_UPDATE
PROCESS_TERMINATION
AsrAdobeReaderChildProcessBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrExecutableEmailContentBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrExecutableOfficeContentBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrLsassCredentialTheftBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrObfuscatedScriptBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrOfficeChildProcessBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrOfficeCommAppChildProcessBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrOfficeMacroWin32ApiCallsBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrOfficeProcessInjectionBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrPersistenceThroughWmiBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrPsexecWmiChildProcessBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrRansomwareBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrScriptExecutableDownloadBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrUntrustedExecutableBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrUntrustedUsbProcessBlocked
SCAN_HOST
PROCESS_TERMINATION
AsrVulnerableSignedDriverBlocked
SCAN_HOST
PROCESS_TERMINATION
ControlFlowGuardViolation
STATUS_UPDATE
PROCESS_TERMINATION
ExploitGuardAcgEnforced
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardChildProcessBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardEafViolationBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardIafViolationBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardLowIntegrityImageBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardNonMicrosoftSignedBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardRopExploitBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardSharedBinaryBlocked
SCAN_HOST
PROCESS_TERMINATION
ExploitGuardWin32SystemCallBlocked
SCAN_HOST
PROCESS_TERMINATION
PrintJobBlocked
STATUS_UPDATE
PROCESS_TERMINATION
AppControlAppInstallationBlocked
SCAN_HOST
PROCESS_TERMINATION
ControlledFolderAccessViolationBlocked
SCAN_FILE
PROCESS_TERMINATION
RemoteWmiOperation
NETWORK_CONNECTION
PROCESS_UNCATEGORIZED
AntivirusTroubleshootModeEvent
SCAN_HOST
PROCESS_UNCATEGORIZED
AppControlAppInstallationAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AppControlCIScriptAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AppControlExecutableAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AppControlPackagedAppAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AppControlScriptAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AppGuardBrowseToUrl
SCAN_HOST
PROCESS_UNCATEGORIZED
AppGuardResumeContainer
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrAdobeReaderChildProcessAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrLsassCredentialTheftAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrObfuscatedScriptAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrOfficeMacroWin32ApiCallsAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrPersistenceThroughWmiAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrRansomwareAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
AsrVulnerableSignedDriverAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
DpapiAccessed
GENERIC_EVENT
PROCESS_UNCATEGORIZED
ExploitGuardEafViolationAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
ExploitGuardIafViolationAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
ExploitGuardRopExploitAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
ExploitGuardWin32SystemCallAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
GetAsyncKeyStateApiCall
STATUS_UPDATE
PROCESS_UNCATEGORIZED
GetClipboardData
STATUS_UPDATE
PROCESS_UNCATEGORIZED
QueueUserApcRemoteApiCall
PROCESS_LAUNCH
PROCESS_UNCATEGORIZED
ControlledFolderAccessViolationAudited
SCAN_FILE
PROCESS_UNCATEGORIZED
ExploitGuardAcgAudited
SCAN_HOST
PROCESS_UNCATEGORIZED
RemovableStoragePolicyTriggered
STATUS_UPDATE
PROCESS_UNCATEGORIZED
NetworkShareObjectAdded
NETWORK_UNCATEGORIZED
RESOURCE_CREATION
DirectoryServiceObjectCreated
SERVICE_MODIFICATION
RESOURCE_CREATION
NetworkShareObjectDeleted
NETWORK_UNCATEGORIZED
RESOURCE_DELETION
DirectoryServiceObjectModified
SERVICE_MODIFICATION
RESOURCE_WRITTEN
NetworkShareObjectAccessChecked
NETWORK_UNCATEGORIZED
RESOURCE_READ
PnpDeviceAllowed
DEVICE_CONFIG_UPDATE
RESOURCE_READ
PnpDeviceBlocked
STATUS_UPDATE
RESOURCE_READ
PnpDeviceConnected
STATUS_UPDATE
RESOURCE_READ
NetworkShareObjectModified
NETWORK_UNCATEGORIZED
RESOURCE_WRITTEN
AppControlCodeIntegrityOriginAllowed
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityOriginAudited
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityOriginBlocked
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityPolicyAudited
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityPolicyBlocked
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityPolicyLoaded
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityDriverRevoked
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityImageAudited
SCAN_HOST
SCAN_FILE
AppControlCodeIntegrityImageRevoked
SCAN_HOST
SCAN_FILE
ContainedDeviceConnectionBlocked
NETWORK_UNCATEGORIZED
SCAN_HOST
SmartScreenAppWarning
SCAN_UNCATEGORIZED
SCAN_HOST
SmartScreenExploitWarning
SCAN_UNCATEGORIZED
SCAN_HOST
SmartScreenUrlWarning
SCAN_UNCATEGORIZED
SCAN_HOST
AntivirusDefinitionsUpdated
SCAN_HOST
SERVICE_STOP
BitLockerAuditCompleted
SERVICE_UNSPECIFIED
SERVICE_STOP
AntivirusDefinitionsUpdated
SCAN_HOST
SETTING_MODIFICATION
AntivirusDefinitionsUpdateFailed
SCAN_HOST
SETTING_MODIFICATION
AntivirusEmergencyUpdatesInstalled
SCAN_HOST
SETTING_MODIFICATION
AuditPolicyModification
SERVICE_MODIFICATION
SETTING_MODIFICATION
BluetoothPolicyTriggered
STATUS_UPDATE
SETTING_MODIFICATION
SmartScreenUserOverride
SCAN_UNCATEGORIZED
SETTING_MODIFICATION
WmiBindEventFilterToConsumer
STATUS_UPDATE
SETTING_MODIFICATION
UsbDriveMounted
DEVICE_CONFIG_UPDATE
STATUS_UNCATEGORIZED
UsbDriveUnmounted
DEVICE_CONFIG_UPDATE
STATUS_UNCATEGORIZED
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceEvents
The following table lists the delta of log fields for the
DeviceEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.DeviceId
principal.asset_id
If the
properties.ActionType
log field contains one of the following values, then
DeviceID:%{properties.DeviceId}
is mapped to the
target.asset_id
and
target.asset.asset_id
UDM fields:
AppControlPolicyApplied
NetworkProtectionUserBypassEvent
UsbDriveDriveLetterChanged
AppControlCodeIntegrityOriginAllowed
AppControlCodeIntegrityOriginAudited
AppControlCodeIntegrityOriginBlocked
AppControlCodeIntegrityPolicyAudited
AppControlCodeIntegrityPolicyBlocked
AppControlCodeIntegrityPolicyLoaded
SafeDocFileScan
AppControlCodeIntegrityDriverRevoked
AppControlCodeIntegrityImageAudited
AppControlCodeIntegrityImageRevoked
AntivirusDetection
AntivirusDetectionActionType
AntivirusMalwareActionFailed
AntivirusMalwareBlocked
AntivirusReport
AntivirusScanCancelled
AntivirusScanCompleted
AntivirusScanFailed
ContainedDeviceConnectionBlocked
SmartScreenAppWarning
SmartScreenExploitWarning
SmartScreenUrlWarning
AntivirusError
AccountCheckedForBlankPassword
Else,
DeviceID:%{properties.DeviceId}
is mapped to the
principal.asset_id
and
principal.asset.asset_id
UDM fields.
properties.DeviceName
principal.hostname
If the
properties.ActionType
log field contains one of the following values, then the
properties.DeviceName
log field is mapped to the
target.hostname
and
target.asset.hostname
UDM fields:
AppControlPolicyApplied
NetworkProtectionUserBypassEvent
UsbDriveDriveLetterChanged
AppControlCodeIntegrityOriginAllowed
AppControlCodeIntegrityOriginAudited
AppControlCodeIntegrityOriginBlocked
AppControlCodeIntegrityPolicyAudited
AppControlCodeIntegrityPolicyBlocked
AppControlCodeIntegrityPolicyLoaded
SafeDocFileScan
AppControlCodeIntegrityDriverRevoked
AppControlCodeIntegrityImageAudited
AppControlCodeIntegrityImageRevoked
AntivirusDetection
AntivirusDetectionActionType
AntivirusMalwareActionFailed
AntivirusMalwareBlocked
AntivirusReport
AntivirusScanCancelled
AntivirusScanCompleted
AntivirusScanFailed
ContainedDeviceConnectionBlocked
SmartScreenAppWarning
SmartScreenExploitWarning
SmartScreenUrlWarning
AntivirusError
AccountCheckedForBlankPassword
Else, the
properties.DeviceName
log field is mapped to the
principal.hostname
and
principal.asset.hostname
UDM fields.
properties.LocalIP
principal.ip
If the
properties.ActionType
log field contains one of the following values, then the
properties.LocalIP
log field is mapped to the
target.ip
and
target.asset.ip
UDM fields:
AppControlPolicyApplied
NetworkProtectionUserBypassEvent
UsbDriveDriveLetterChanged
AppControlCodeIntegrityOriginAllowed
AppControlCodeIntegrityOriginAudited
AppControlCodeIntegrityOriginBlocked
AppControlCodeIntegrityPolicyAudited
AppControlCodeIntegrityPolicyBlocked
AppControlCodeIntegrityPolicyLoaded
SafeDocFileScan
AppControlCodeIntegrityDriverRevoked
AppControlCodeIntegrityImageAudited
AppControlCodeIntegrityImageRevoked
AntivirusDetection
AntivirusDetectionActionType
AntivirusMalwareActionFailed
AntivirusMalwareBlocked
AntivirusReport
AntivirusScanCancelled
AntivirusScanCompleted
AntivirusScanFailed
ContainedDeviceConnectionBlocked
SmartScreenAppWarning
SmartScreenExploitWarning
SmartScreenUrlWarning
AntivirusError
AccountCheckedForBlankPassword
Else, the
properties.LocalIP
log field is mapped to the
principal.ip
and
principal.asset.ip
UDM fields.
properties.FileOriginIP
principal.ip
If the
properties.ActionType
log field contains one of the following values, then the
properties.FileOriginIP
log field is mapped to the
target.ip
and
target.asset.ip
UDM fields:
AppControlPolicyApplied
NetworkProtectionUserBypassEvent
UsbDriveDriveLetterChanged
AppControlCodeIntegrityOriginAllowed
AppControlCodeIntegrityOriginAudited
AppControlCodeIntegrityOriginBlocked
AppControlCodeIntegrityPolicyAudited
AppControlCodeIntegrityPolicyBlocked
AppControlCodeIntegrityPolicyLoaded
SafeDocFileScan
AppControlCodeIntegrityDriverRevoked
AppControlCodeIntegrityImageAudited
AppControlCodeIntegrityImageRevoked
AntivirusDetection
AntivirusDetectionActionType
AntivirusMalwareActionFailed
AntivirusMalwareBlocked
AntivirusReport
AntivirusScanCancelled
AntivirusScanCompleted
AntivirusScanFailed
ContainedDeviceConnectionBlocked
SmartScreenAppWarning
SmartScreenExploitWarning
SmartScreenUrlWarning
AntivirusError
AccountCheckedForBlankPassword
Else, the
properties.FileOriginIP
log field is mapped to the
principal.ip
and
principal.asset.ip
UDM fields.
properties.LocalPort
principal.port
If the
properties.ActionType
log field contains one of the following values, then the
properties.LocalPort
log field is mapped to the
target.port
UDM field:
AppControlPolicyApplied
NetworkProtectionUserBypassEvent
UsbDriveDriveLetterChanged
AppControlCodeIntegrityOriginAllowed
AppControlCodeIntegrityOriginAudited
AppControlCodeIntegrityOriginBlocked
AppControlCodeIntegrityPolicyAudited
AppControlCodeIntegrityPolicyBlocked
AppControlCodeIntegrityPolicyLoaded
SafeDocFileScan
AppControlCodeIntegrityDriverRevoked
AppControlCodeIntegrityImageAudited
AppControlCodeIntegrityImageRevoked
AntivirusDetection
AntivirusDetectionActionType
AntivirusMalwareActionFailed
AntivirusMalwareBlocked
AntivirusReport
AntivirusScanCancelled
AntivirusScanCompleted
AntivirusScanFailed
ContainedDeviceConnectionBlocked
SmartScreenAppWarning
SmartScreenExploitWarning
SmartScreenUrlWarning
AntivirusError
AccountCheckedForBlankPassword
Else, the
properties.LocalPort
log field is mapped to the
principal.port
UDM field.
properties.InitiatingProcessAccountObjectId
principal.user.product_object_id
If the
properties.ActionType
log field contains one of the following values, then the
properties.InitiatingProcessAccountObjectId
log field is mapped to the
target.user.product_object_id
UDM field:
ServiceInstalled
CredentialsBackup
FirewallServiceStopped
BitLockerAuditCompleted
PasswordChangeAttempt
LogonRightsSettingEnabled
UserAccountCreated
UserAccountDeleted
BruteForceActivityDetected
UserAccountModified
Else, the
properties.InitiatingProcessAccountObjectId
log field is mapped to the
principal.user.product_object_id
UDM field.
properties.InitiatingProcessAccountUpn
principal.user.user_display_name
If the
properties.ActionType
log field contains one of the following values, then the
properties.InitiatingProcessAccountUpn
log field is mapped to the
target.user.user_display_name
UDM field:
ServiceInstalled
CredentialsBackup
FirewallServiceStopped
BitLockerAuditCompleted
PasswordChangeAttempt
LogonRightsSettingEnabled
UserAccountCreated
UserAccountDeleted
BruteForceActivityDetected
UserAccountModified
Else, the
properties.InitiatingProcessAccountUpn
log field is mapped to the
principal.user.user_display_name
UDM field.
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - AlertEvidence
The following table lists the delta of log fields for the
AlertEvidence
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.Application
additional.fields[application]
principal.application
properties.EvidenceDirection
principal.user.attribute.labels[evidence_direction]
additional.fields[evidence_direction]
properties.EvidenceRole
principal.user.attribute.labels[evidence_role]
additional.fields[evidence_role]
The
metadata.event_type
UDM field is set to
SCAN_HOST
.
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - AlertInfo
The following table lists the delta of log fields for the
AlertInfo
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.AlertId
metadata.product_log_id
security_result.threat_id
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileCertificateInfo
The following table lists the delta of log fields for the
DeviceFileCertificateInfo
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.Timestamp
metadata.event_timestamp
metadata.creation_timestamp
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
The
metadata.entity_type
UDM field is set to
FILE
.
properties.ReportId
metadata.product_log_id
metadata.product_entity_id
properties.DeviceId
principal.asset_id
The
entity.asset_id
is set to
DeviceID:%{properties.DeviceId}
.
properties.SHA1
principal.file.sha1
If the
properties.SHA1
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
properties.SHA1
log field is mapped to the
entity.file.sha1
UDM field.
properties.Issuer
principal.file.signature_info.sigcheck.signers.cert_issuer
entity.file.signature_info.sigcheck.signers.cert_issuer
properties.Signer
principal.file.signature_info.sigcheck.signers.name
entity.file.signature_info.sigcheck.signers.name
properties.IsSigned
principal.file.signature_info.sigcheck.verified
If the
properties.IsSigned
log field value is equal to
true
, then the
entity.file.signature_info.sigcheck.verified
UDM field is set to
TRUE
.
Else, the
entity.file.signature_info.sigcheck.verified
UDM field is set to
FALSE
.
properties.DeviceName
principal.hostname
entity.asset.hostname
properties.CertificateSerialNumber
additional.fields[certificate_serial_number]
entity.file.signature_info.sigcheck.x509.serial_number
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileEvents
The following table lists the delta of log fields for the
DeviceFileEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.FileOriginIP
principal.ip
src.ip
properties.RequestSourceIP
principal.ip
src..ip
properties.RequestSourcePort
principal.port
src.port
properties.FileOriginUrl
principal.url
src.url
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceLogonEvents
The following table lists the delta of log fields for the
DeviceLogonEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.LogonId
network.session_id
extensions.auth.auth_details
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGathering
The following table lists the delta of log fields for the
DeviceTvmInfoGathering
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.LastSeenTime
security.result.last_discovered_time
principal.asset.last_discover_time
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceRegistryEvents
The following table lists the delta of log fields for the
DeviceRegistryEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.PreviousRegistryValueData
principal.registry.registry_value_data
src.registry.registry_value_data
properties.PreviousRegistryKey
principal.registry.registry_key
src.registry.registry_key
properties.PreviousRegistryValueName
principal.registry.registry_value_name
src.registry.registry_value_name
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareVulnerabilitiesKB
The following table lists the delta of log fields for the
DeviceTvmSoftwareVulnerabilitiesKB
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.IsExploitAvailable
extensions.vulns.vulnerablities.cvss_vector
additional.fields[is_exploit_available]
properties.LastModifiedTime
extensions.vulns.vulnerabilities.scan_end_time
additional.fields[last_modified_time]
properties.PublishedDate
extensions.vulns.vulnerabilities.first_found
additional.fields[published_date]
properties.AffectedSoftware
extensions.vulns.vulnerabilities.description
target.application
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - EmailAttachmentInfo
The following table lists the delta of log fields for the
EmailAttachmentInfo
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.FileType
target.file.mime_type
entity.file.mime_type
properties.FileName
target.file.names
entity.file.names
properties.SHA256
target.file.sha256
If the
properties.SHA256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
properties.SHA256
log field is mapped to the
entity.file.sha256
UDM field.
properties.FileSize
target.file.size
entity.file.size
properties.Timestamp
metadata.event_timestamp
metadata.creation_timestamp
The
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
The
metadata.entity_type
UDM field is set to
FILE
.
properties.ReportId
metadata.product_log_id
metadata.product_entity_id
properties.SenderFromAddress
network.email.from
If the
properties.SenderFromAddress
log field value matches the regular expression pattern
^.+@.+$
and the length of the value is 256 characters or less, then the
properties.SenderFromAddress
log field is mapped to the
entity.user.email_addresses
UDM field.
Else, the
additional.fields.key
UDM field is set to
SenderFromAddress
and the
properties.SenderFromAddress
log field value is mapped to the
additional.fields.value.string_value
UDM field.
properties.SenderFromAddress
principal.user.email_addresses
If the
properties.SenderFromAddress
log field value matches the regular expression pattern
^.+@.+$
and the length of the value is 256 characters or less, then the
properties.SenderFromAddress
log field is mapped to the
entity.user.email_addresses
UDM field.
Else, the
additional.fields.key
UDM field is set to
SenderFromAddress
and the
properties.SenderFromAddress
log field value is mapped to the
additional.fields.value.string_value
UDM field.
properties.NetworkMessageId
network.email.mail_id
additional.fields[network_message_id]
properties.RecipientEmailAddress
network.email.to
additional.fields[recipient_email_address]
properties.RecipientEmailAddress
target.user.email_addresses
additional.fields[recipient_email_address]
properties.SenderObjectId
principal.user.product_object_id
entity.user.attribute.labels[sender_object_id]
properties.SenderDisplayName
principal.user.user_display_name
entity.user.attribute.labels[sender_display_name]
properties.ThreatTypes
security_result.category
If the
properties.ThreatTypes
log field value is equal to
Phish
, then the
entity.security_result.category
UDM field is set to
MAIL_PHISHING
.
Else, the
entity.security_result.category
UDM field is set to
UNKNOWN_CATEGORY
properties.DetectionMethods
security_result.detection_fields[detection_methods]
entity.security_result.detection_fields[detection_methods]
properties.ThreatNames
security_result.threat_name
entity.security_result.threat_name
properties.RecipientObjectId
target.user.product_object_id
entity.user.attribute.labels[recipient_object_id]
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - EmailEvents
The following table lists the delta of log fields for the
EmailEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.SenderMailFromAddress
principal.user.attribute.labels[sender_mail_from_address]
network.email.reply_to
properties.DeliveryAction
additional.fields[delivery_action]
If the
properties.DeliveryAction
log field is equal to
Delivered
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
properties.DeliveryAction
log field contains one of the following values:
Junked
Replaced
then the
security_result.action
UDM field is set to
ALLOW_WITH_MODIFICATION
.
Else, if the
properties.DeliveryAction
log field is equal to
Blocked
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, the
security_result.action
UDM field is set to
UNKNOWN_ACTION
.
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - EmailPostDeliveryEvents
The following table lists the delta of log fields for the
EmailPostDeliveryEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
The
metadata.event_type
UDM field is set to
EMAIL_UNCATEGORIZED
.
The
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - EmailUrlInfo
The following table lists the delta of log fields for the
EmailUrlInfo
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.UrlDomain
target.hostname
entity.domain.name
properties.Url
target.url
entity.URL
properties.Timestamp
metadata.event_timestamp
metadata.creation_timestamp
The
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
The
metadata.entity_type
UDM field is set to
URL
.
properties.ReportId
metadata.product_log_id
metadata.product_entity_id
properties.NetworkMessageId
network.email.mail_id
additional.fields[network_message_id]
properties.UrlLocation
additional.fields[url_location]
metadata.threat.detection_fields[url_location]
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - IdentityInfo
The following table lists the delta of log fields for the
IdentityInfo
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.Type
entity.user.attribute.role.name
If the
properties.Type
log field is equal to
User
, then the
entity.user.account_type
UDM field is set to
DOMAIN_ACCOUNT_TYPE
.
Else, if the
properties.Type
log field is equal to
ServiceAccount
, then the
entity.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
properties.Type
entity.user.attribute.role.name
entity.user.attribute.labels[type]
UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - IdentityLogonEvents
The following table lists the delta of log fields for the
IdentityLogonEvents
log type and their corresponding UDM fields:
Raw Field
Old UDM Mapping
New UDM Mapping
properties.Application
additional.fields[application]
principal.application
properties.AccountObjectId
additional.fields[account_object_id]
principal.user.product_object_id
properties.DestinationDeviceName
src.hostname
intermediary.hostname
properties.DestinationPort
src.port
intermediary.port
properties.DestinationIPAddress
src.ip
intermediary.ip
properties.AccountUpn
principal.user.user_display_name
principal.user.email_addresses
What's next
Data ingestion to Google SecOps
Need more help?
Get answers from Community members and Google SecOps professionals.
