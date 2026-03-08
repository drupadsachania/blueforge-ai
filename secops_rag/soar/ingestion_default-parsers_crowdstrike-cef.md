# Collect CrowdStrike Falcon logs in CEF

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-cef/  
**Scraped:** 2026-03-05T09:53:40.818447Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CrowdStrike Falcon logs in CEF
Supported in:
Google secops
SIEM
This document explains how to collect CrowdStrike Falcon logs in CEF format using Bindplane. The parser extracts key-value pairs and maps them to the Unified Data Model (UDM), handling different delimiters and enriching the data with additional context like severity and event types. It also performs specific transformations for certain event types and fields, such as user logins and security results.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the CrowdStrike Falcon console.
Obtain API credentials for Falcon Stream (Client ID and Client Secret).
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
For additional installation options, consult this
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:54525"
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
SYSLOG
namespace
:
cs_falcon
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
tcplog
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
Configure and get a CrowdStrike API Key
Sign in to
CrowdStrike Falcon
with a privileged account.
Go to
Menu
>
Support
.
Click
API Clients
>
KeysSelect
.
Click
Add new API client
.
In the
API Scopes
section, select
Event streams
and
Alerts
>
enable the
Read
option.
Click
Add
.
Copy and save the
Client ID
,
Secret
, and
Base URL
.
Install the Falcon SIEM Connector
Download the RPM installer package for your operating system.
Package installation:
CentOS operating system:
sudo
rpm
-Uvh
<installer
package>
Ubuntu operating system:
sudo
dpkg
-i
<installer
package>
Default installation directories:
Falcon SIEM Connector -
/opt/crowdstrike/
.
Service -
/etc/init.d/cs.falconhoseclientd/
.
Configure the SIEM Connector to forward CEF logs to Bindplane
Sign into the machine with installed SIEM Connector as a
sudo
user.
Go to the
/opt/crowdstrike/etc/
directory.
Rename
cs.falconhoseclient.cef.cfg
to
cs.falconhoseclient.cfg
.
SIEM Connector uses
cs.falconhoseclient.cfg
configuration by default.
Edit the
cs.falconhoseclient.cfg
file and modify/set the following parameters:
api_url:
- your CrowdStrike Falcon Base URL copied from previous step.
app_id:
- any string as identifier for connecting to Falcon Streaming API (For example, set to
app_id: SECOPS-CEF
).
client_id:
- the
client_id
value copied from previous step.
client_secret:
- the
client_secret
value copied from previous step.
send_to_syslog_server: true
- enable push to Syslog server.
host:
- the IP or hostname of the Bindplane agent.
port:
- the port of the Bindplane agent.
Save the
cs.falconhoseclient.cfg
file.
Start the SIEM Connector service:
CentOS operating system
sudo
service
cs.falconhoseclientd
start
Ubuntu 16.04 or later operating system
sudo
systemctl
start
cs.falconhoseclientd.service
Optional: Stop the SIEM Connector service:
CentOS operating system
sudo
service
cs.falconhoseclientd
stop
Ubuntu 16.04 or later operating system
sudo
systemctl
stop
cs.falconhoseclientd.service
Optional: Restart the SIEM Connector service:
CentOS operating system
sudo
service
cs.falconhoseclientd
restart
Ubuntu 16.04 or later operating system
sudo
systemctl
restart
cs.falconhoseclientd.service
UDM Mapping Table
Log Field
UDM Mapping
Logic
AccountCreationTimeStamp
event.idm.read_only_udm.metadata.event_timestamp
The raw log field
AccountCreationTimeStamp
is renamed to
event.idm.read_only_udm.metadata.event_timestamp
.
AccountDomain
event.idm.read_only_udm.principal.administrative_domain
The raw log field
AccountDomain
is renamed to
event.idm.read_only_udm.principal.administrative_domain
.
AccountObjectGuid
event.idm.read_only_udm.metadata.product_log_id
The raw log field
AccountObjectGuid
is renamed to
event.idm.read_only_udm.metadata.product_log_id
.
AccountObjectSid
event.idm.read_only_udm.principal.user.windows_sid
The raw log field
AccountObjectSid
is renamed to
event.idm.read_only_udm.principal.user.windows_sid
.
AccessType
-
Not mapped to the IDM object.
action_taken
event.idm.read_only_udm.additional.fields[0].value.string_value
Part of
AuditKeyValues
array.
ActiveCpuCount
-
Not mapped to the IDM object.
ActiveDirectoryAuthenticationMethod
-
Not mapped to the IDM object.
ActiveDirectoryDataProtocol
-
Not mapped to the IDM object.
AddressFamily
-
Not mapped to the IDM object.
AdminStatus
-
Not mapped to the IDM object.
AllocateVirtualMemoryCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
agent-windows
event.idm.read_only_udm.target.file.full_path
Part of TargetFileName.
AgentIdString
event.idm.read_only_udm.principal.asset_id
Prefixed with
CS:
.
AgentLoadFlags
-
Not mapped to the IDM object.
AgentLocalTime
-
Not mapped to the IDM object.
AgentOnline
AgentTimeOffset
-
Not mapped to the IDM object.
AgentVersion
AggregationActivityCount
AggregationEarliestTimestamp
-
Not mapped to the IDM object.
aid
event.idm.read_only_udm.principal.asset_id
Prefixed with
CS:
.
aip
event.idm.read_only_udm.principal.nat_ip
When
_aid_is_target
is false, if
aip
is not null, create an ip entity with the value of
aip
and add it to
event.idm.read_only_udm.principal.nat_ip
.
aipCount
AllocVmEtw
AllocationType
-
Not mapped to the IDM object.
AllowHardTerminate
-
Not mapped to the IDM object.
AllowStartOnDemand
-
Not mapped to the IDM object.
ApcArgument1
-
Not mapped to the IDM object.
ApcArgument2
-
Not mapped to the IDM object.
ApcContextAddress
-
Not mapped to the IDM object.
ApcContextFileName
-
Not mapped to the IDM object.
ApcContext
-
Not mapped to the IDM object.
ApplicationName
ApplicationUniqueIdentifier
-
Not mapped to the IDM object.
ApplicationVersion
-
Not mapped to the IDM object.
AppIs64Bit
-
Not mapped to the IDM object.
AppName
AppPath
AppPathFlag
-
Not mapped to the IDM object.
AppProductId
-
Not mapped to the IDM object.
AppType
-
Not mapped to the IDM object.
AppUpdateIds
-
Not mapped to the IDM object.
AppVendor
-
Not mapped to the IDM object.
AppVersion
ArchiveFileWrittenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
AsepClass
-
Not mapped to the IDM object.
AsepFileChange
AsepFlags
-
Not mapped to the IDM object.
AsepIndex
-
Not mapped to the IDM object.
AsepKeyUpdate
AsepValueUpdate
AsepValueType
-
Not mapped to the IDM object.
AsepWrittenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
AssociateIndicator
AssociateTreeIdWithRoot
AssemblyFlags
-
Not mapped to the IDM object.
AssemblyId
-
Not mapped to the IDM object.
AssemblyName
AuthenticationId
event.idm.read_only_udm.principal.user.product_object_id
Prefixed with
CS:
.
AuthenticationPackage
AuthenticationUuid
-
Not mapped to the IDM object.
AuthenticationUuidAsString
-
Not mapped to the IDM object.
AuthenticodeHashData
AuthenticodeMatch
automated_remediation
assessments.automated_remediation
Part of
ZeroTrustHostAssessment
event.
BaseReachableTime
-
Not mapped to the IDM object.
BaseTime
-
Not mapped to the IDM object.
BatchDataNumber
-
Not mapped to the IDM object.
BatchDataTotal
-
Not mapped to the IDM object.
BatchTimestamp
BatteryLevel
-
Not mapped to the IDM object.
BatteryStatus
-
Not mapped to the IDM object.
BehaviorWhitelisted
benchmarks
BenignCount
-
Not mapped to the IDM object.
beta_build_disabled
assessments.beta_build_disabled
Part of
ZeroTrustHostAssessment
event.
BinaryExecutableWrittenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
BillingInfo
BillingType
-
Not mapped to the IDM object.
BiosManufacturer
BiosReleaseDate
-
Not mapped to the IDM object.
BiosVersion
BITSJobCreated
BootArgs
-
Not mapped to the IDM object.
BootId
-
Not mapped to the IDM object.
BootStatusDataAabEnabled
-
Not mapped to the IDM object.
BootStatusDataBootAttemptCount
-
Not mapped to the IDM object.
BootStatusDataBootGood
-
Not mapped to the IDM object.
BootStatusDataBootShutdown
-
Not mapped to the IDM object.
BootTimeFunctionalityLevel
-
Not mapped to the IDM object.
BrowserInjectedThread
BundleID
-
Not mapped to the IDM object.
CallStackModuleNames
CallStackModuleNamesVersion
ChannelId
-
Not mapped to the IDM object.
ChannelVersion
-
Not mapped to the IDM object.
ChannelVersionRequired
ChasisManufacturer
-
Not mapped to the IDM object.
ChassisType
cid
City
CLICreationCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
ClassifiedModuleLoad
CloudAssociateTreeIdWithRoot
CloudErrorCode
-
Not mapped to the IDM object.
CNAMERecords
CodeIntegrity
-
Not mapped to the IDM object.
CommandLine
CommandSequence
-
Not mapped to the IDM object.
CompletionEventId
-
Not mapped to the IDM object.
ComputerName
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
If
ComputerName
is not null, an empty string or a dash, create a hostname entity with the value of
ComputerName
and add it to
event.idm.read_only_udm.principal.hostname
and
event.idm.read_only_udm.principal.asset.hostname
.
ConfigBuild
ConfigIDBase
-
Not mapped to the IDM object.
ConfigIDBuild
-
Not mapped to the IDM object.
ConfigIDPlatform
-
Not mapped to the IDM object.
ConfigurationVersion
-
Not mapped to the IDM object.
ConfigStateData
-
Not mapped to the IDM object.
ConfigStateHash
ConfigStateUpdate
ConnectTime
-
Not mapped to the IDM object.
ConnectType
-
Not mapped to the IDM object.
Connected
-
Not mapped to the IDM object.
ConnectionCipher
-
Not mapped to the IDM object.
ConnectionCipherStrength
-
Not mapped to the IDM object.
ConnectionDirection
-
Not mapped to the IDM object.
ConnectionExchange
-
Not mapped to the IDM object.
ConnectionExchangeStrength
-
Not mapped to the IDM object.
ConnectionFlags
-
Not mapped to the IDM object.
ConnectionHash
-
Not mapped to the IDM object.
ConnectionHashStrength
-
Not mapped to the IDM object.
ConnectionProtocol
-
Not mapped to the IDM object.
ConnectionType
-
Not mapped to the IDM object.
Continent
ContentSHA256HashData
ContextData
-
Not mapped to the IDM object.
ContextProcessId
event.idm.read_only_udm.principal.process.product_specific_process_id
,
event.idm.read_only_udm.target.process.product_specific_process_id
Prefixed with
CS:%{cid}:%{aid}:
.
ContextThreadId
-
Not mapped to the IDM object.
ContextTimeStamp
ContextTimeStamp_decimal
Country
CrashDumpFilePath
-
Not mapped to the IDM object.
CrashNotification
CreateProcessArgs
CreateProcessCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
CreateService
CreateThreadNoStartImage
CreationTimeStamp
-
Not mapped to the IDM object.
CriticalFileAccessed
CriticalFileModified
CsaProcessDataCollectionInstanceId
-
Not mapped to the IDM object.
CurrentFunctionalityLevel
-
Not mapped to the IDM object.
CurrentLocalIP
-
Not mapped to the IDM object.
CurrentSystemTags
CustomerIdString
CycleTime
-
Not mapped to the IDM object.
DadState
-
Not mapped to the IDM object.
DadTransmits
-
Not mapped to the IDM object.
DcName
event.idm.read_only_udm.principal.user.userid
The raw log field
DcName
is renamed to
event.idm.read_only_udm.principal.user.userid
.
DcNumAttachments
-
Not mapped to the IDM object.
DcNumBlockingPolicies
-
Not mapped to the IDM object.
DcOnline
DcPropertyIdInterfaceType
-
Not mapped to the IDM object.
DcPropertyIdInterfaceVersion
-
Not mapped to the IDM object.
DcSensorInterfaceType
-
Not mapped to the IDM object.
DcSensorInterfaceVersion
-
Not mapped to the IDM object.
DcStatus
DcUsbConfigurationDescriptor
DcUsbDeviceConnected
DcUsbDeviceDisconnected
DcUsbEndpointDescriptor
DcUsbHIDDescriptor
DcUsbInterfaceDescriptor
DCSyncAttempted
Debug
-
Not mapped to the IDM object.
DefaultGatewayIP4
-
Not mapped to the IDM object.
DefaultGatewayIP6
-
Not mapped to the IDM object.
DefaultGatewayPhysicalAddress
-
Not mapped to the IDM object.
DeepHashBlacklistClassification
DeepHashBlacklistVersion
-
Not mapped to the IDM object.
DeliverLocalFXToCloud
DesiredAccess
detectionId
detectionName
DetectDescription
DetectId
-
Not mapped to the IDM object.
DetectName
DeviceActiveConfigurationNumber
-
Not mapped to the IDM object.
DeviceConnectionStatus
-
Not mapped to the IDM object.
DeviceDescriptorNumber
-
Not mapped to the IDM object.
DeviceDescriptorSetHash
-
Not mapped to the IDM object.
DeviceDescriptorUniqueIdentifier
-
Not mapped to the IDM object.
DeviceId
-
Not mapped to the IDM object.
DeviceInstanceId
event.idm.read_only_udm.target.asset_id
Prefixed with
Device Instance Id:
.
DeviceManufacturer
DeviceProduct
DeviceProductId
-
Not mapped to the IDM object.
DevicePropertyClassName
-
Not mapped to the IDM object.
DevicePropertyClassGuid
-
Not mapped to the IDM object.
DevicePropertyDeviceDescription
DevicePropertyFriendlyName
-
Not mapped to the IDM object.
DevicePropertyLocationInformation
DevicePropertyManufacturer
-
Not mapped to the IDM object.
DeviceProtocol
-
Not mapped to the IDM object.
DeviceSerialNumber
DeviceTimeStamp
DeviceType
-
Not mapped to the IDM object.
DeviceUsbClass
-
Not mapped to the IDM object.
DeviceUsbSubclass
-
Not mapped to the IDM object.
DeviceUsbVersion
-
Not mapped to the IDM object.
DeviceVendorId
-
Not mapped to the IDM object.
DeviceVersion
-
Not mapped to the IDM object.
DirectoryCreate
DirectoryCreatedCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
DirectoryEnumeratedCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
DisableRealtimeMonitoring
DisallowStartIfOnBatteries
-
Not mapped to the IDM object.
DisallowStartOnRemoteAppSession
-
Not mapped to the IDM object.
DiskParentDeviceInstanceId
DllCharacteristics
-
Not mapped to the IDM object.
DllInjection
DlpPolicy
-
Not mapped to the IDM object.
DlpVerdict
-
Not mapped to the IDM object.
DmpFileWritten
DnsRequest
DnsRequestCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
DnsResponseType
-
Not mapped to the IDM object.
DnsResponseTtl
-
Not mapped to the IDM object.
DocumentFileWrittenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
DomainName
event.idm.read_only_udm.target.hostname
,
event.idm.read_only_udm.target.asset.hostname
,
event.idm.read_only_udm.network.dns.questions[0].name
If
DomainName
is not null, create a hostname entity with the value of
DomainName
and add it to
event.idm.read_only_udm.target.hostname
,
event.idm.read_only_udm.target.asset.hostname
and
event.idm.read_only_udm.network.dns.questions[0].name
.
DotnetModuleFlags
-
Not mapped to the IDM object.
DotnetModuleId
-
Not mapped to the IDM object.
DotnetModuleLoadDetectInfo
DownloadPath
-
Not mapped to the IDM object.
DownloadPort
-
Not mapped to the IDM object.
DownloadServer
DriverLoad
DualRequest
-
Not mapped to the IDM object.
EffectiveTransmissionClass
Effective
-
Not mapped to the IDM object.
EfiSupported
-
Not mapped to the IDM object.
EfiVariableCustomMode
-
Not mapped to the IDM object.
EfiVariableCustomModeAttributes
-
Not mapped to the IDM object.
EfiVariableDbAttributes
-
Not mapped to the IDM object.
EfiVariableDbxAttributes
-
Not mapped to the IDM object.
EfiVariableDbxSha256Hash
-
Not mapped to the IDM object.
EfiVariableKekAttributes
-
Not mapped to the IDM object.
EfiVariableKekSha256Hash
-
Not mapped to the IDM object.
EfiVariablePkAttributes
-
Not mapped to the IDM object.
EfiVariablePkSha256Hash
-
Not mapped to the IDM object.
EfiVariableSecureBoot
-
Not mapped to the IDM object.
EfiVariableSecureBootAttributes
-
Not mapped to the IDM object.
EfiVariableSetupMode
-
Not mapped to the IDM object.
EfiVariableSetupModeAttributes
-
Not mapped to the IDM object.
EfiVariableSignatureSupport
-
Not mapped to the IDM object.
EfiVariableSignatureSupportAttributes
-
Not mapped to the IDM object.
EndpointDescriptorAddress
-
Not mapped to the IDM object.
EndpointDescriptorAttributes
-
Not mapped to the IDM object.
EndpointDescriptorInterval
-
Not mapped to the IDM object.
EndpointDescriptorMaxPacketSize
-
Not mapped to the IDM object.
EndOfProcess
Entitlements
ErrorEvent
ErrorCode
-
Not mapped to the IDM object.
ErrorLocation
-
Not mapped to the IDM object.
ErrorReason
-
Not mapped to the IDM object.
ErrorSource
-
Not mapped to the IDM object.
ErrorStatus
-
Not mapped to the IDM object.
ErrorText
-
Not mapped to the IDM object.
EventLogCleared
EventMax
-
Not mapped to the IDM object.
EventMin
-
Not mapped to the IDM object.
EventOrigin
-
Not mapped to the IDM object.
EventType
event.idm.read_only_udm.metadata.product_event_type
If
event_simpleName
is null and
EventType
is not null, create a product_event_type entity with the value of
EventType
and add it to
event.idm.read_only_udm.metadata.product_event_type
.
EtwErrorEvent
EtwRawProcessId
-
Not mapped to the IDM object.
EtwRawThreadId
-
Not mapped to the IDM object.
ExecutableDeleted
ExecutableDeletedCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
ExeAndServiceCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
ExitCode
-
Not mapped to the IDM object.
Exploit
ExternalApiType
event.idm.read_only_udm.metadata.product_event_type
,
event.idm.read_only_udm.extensions.auth.auth_details
If
message
contains
event1
,
ExternalApiType
is renamed to
event.idm.read_only_udm.metadata.product_event_type
. Otherwise, it is renamed to
event.idm.read_only_udm.extensions.auth.auth_details
.
Facility
-
Not mapped to the IDM object.
FailedConnectCount
-
Not mapped to the IDM object.
FalconHostLink
FalconServiceComponent
-
Not mapped to the IDM object.
FalconServiceServletErrors
-
Not mapped to the IDM object.
FalconServiceServletStarts
-
Not mapped to the IDM object.
FalconServiceState
-
Not mapped to the IDM object.
FalconServiceStatus
FeatureExtractionVersion
-
Not mapped to the IDM object.
FeatureVector
-
Not mapped to the IDM object.
File
-
Not mapped to the IDM object.
FileAttributes
-
Not mapped to the IDM object.
FileCreateInfo
FileDeletedCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
FileDeleteInfo
FileEcpBitmask
-
Not mapped to the IDM object.
FileEventType
-
Not mapped to the IDM object.
FileIdentifier
FileObject
-
Not mapped to the IDM object.
FileName
FileOpenInfo
FileRenameInfo
FileSigningTime
-
Not mapped to the IDM object.
FirewallAction
-
Not mapped to the IDM object.
FirewallChangeOption
FirewallDeleteRule
FirewallDeleteRuleIP4
FirewallDeleteRuleIP6
FirewallEnabled
FirewallOption
FirewallOptionNumericValue
-
Not mapped to the IDM object.
FirewallProfile
-
Not mapped to the IDM object.
FirewallRule
FirewallRuleId
FirewallSetRule
FirewallSetRuleIP4
FirewallSetRuleIP6
FirmwareAnalysisErrorEvent
FirmwareAnalysisErrorLocation
-
Not mapped to the IDM object.
FirmwareAnalysisErrorReason
-
Not mapped to the IDM object.
FirmwareAnalysisErrorSource
-
Not mapped to the IDM object.
FirmwareAnalysisHardwareData
FirmwareAnalysisStatus
FirmwareAnalysisCpuSupported
-
Not mapped to the IDM object.
FirmwareAnalysisEclControlInterfaceVersion
-
Not mapped to the IDM object.
FirmwareAnalysisEclConsumerInterfaceVersion
-
Not mapped to the IDM object.
FirmwareImageAnalyzed
FirmwareRegionMeasured
FirmwareSize
-
Not mapped to the IDM object.
FirmwareType
-
Not mapped to the IDM object.
FirstDiscoveredDate
-
Not mapped to the IDM object.
FirstIP4Record
Flags
-
Not mapped to the IDM object.
FltCallbackData
-
Not mapped to the IDM object.
FltCompletionContext
-
Not mapped to the IDM object.
FltRelatedObjects
-
Not mapped to the IDM object.
FontBuffer
-
Not mapped to the IDM object.
FontBufferLength
-
Not mapped to the IDM object.
FontFileCount
-
Not mapped to the IDM object.
FontFileName
FontLoadOperation
-
Not mapped to the IDM object.
FsOperationBlocked
event1.PatternDispositionFlags.FsOperationBlocked
Part of
Event_DetectionSummaryEvent
.
FsPostOpenSnapshotFile
FsVolumeMounted
FsVolumeUnmounted
FullContext
-
Not mapped to the IDM object.
FullExceptionRecord
-
Not mapped to the IDM object.
GcpCreationTimestamp
GenericFileWrittenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
GID
-
Not mapped to the IDM object.
GrandparentCommandLine
GrandparentImageFileName
GrandParentBaseFileName
GroupIdentity
GroupRid
GzipFileWritten
HandleCreated
-
Not mapped to the IDM object.
HIDDescriptorCountryCode
-
Not mapped to the IDM object.
HIDDescriptorNumDescriptors
-
Not mapped to the IDM object.
HIDDescriptorVersion
-
Not mapped to the IDM object.
HIPHandlers.dll
event.idm.read_only_udm.target.file.full_path
Part of TargetFileName.
HostGroups
-
Not mapped to the IDM object.
HostHiddenStatus
HostInfo
HostnameChanged
hostname
HostProcessType
-
Not mapped to the IDM object.
HostUrl
HttpRequestDetect
HttpRequestHeader
HttpUrl
IcmpCode
-
Not mapped to the IDM object.
IcmpType
-
Not mapped to the IDM object.
id
IdleSettings
-
Not mapped to the IDM object.
ImageFileName
ImageSubsystem
-
Not mapped to the IDM object.
Image
-
Not mapped to the IDM object.
ImpersonatedUserName
InBroadcastOctets
-
Not mapped to the IDM object.
InContext
-
Not mapped to the IDM object.
InDiscards
-
Not mapped to the IDM object.
Indicator
event1.PatternDispositionFlags.Indicator
Part of
Event_DetectionSummaryEvent
.
InddetMask
event1.PatternDispositionFlags.InddetMask
Part of
Event_DetectionSummaryEvent
.
InErrors
-
Not mapped to the IDM object.
Information
-
Not mapped to the IDM object.
InjectedDll
InjectedThread
InjectedThreadCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
InjectedThreadFlag
-
Not mapped to the IDM object.
InMulticastOctets
-
Not mapped to the IDM object.
InNUcastPkts
-
Not mapped to the IDM object.
InOctets
-
Not mapped to the IDM object.
InstallDate
-
Not mapped to the IDM object.
InstalledApplication
InstalledUpdateExtendedStatus
-
Not mapped to the IDM object.
InstalledUpdateIds
-
Not mapped to the IDM object.
InstalledUpdates
InstanceMetadata
InstanceMetadataProvider
-
Not mapped to the IDM object.
InstanceMetadataRequest
-
Not mapped to the IDM object.
InstanceMetadataSignature
-
Not mapped to the IDM object.
InUcastOctets
-
Not mapped to the IDM object.
InUcastPkts
-
Not mapped to the IDM object.
InUnknownProtos
-
Not mapped to the IDM object.
IntegrityLevel
-
Not mapped to the IDM object.
InterfaceAlias
-
Not mapped to the IDM object.
InterfaceDescription
-
Not mapped to the IDM object.
InterfaceFlags
-
Not mapped to the IDM object.
InterfaceGuid
-
Not mapped to the IDM object.
InterfaceIdentifier
-
Not mapped to the IDM object.
InterfaceIndex
-
Not mapped to the IDM object.
InterfaceMtu
-
Not mapped to the IDM object.
InterfaceType
-
Not mapped to the IDM object.
InterfaceVersion
-
Not mapped to the IDM object.
InjectedDllCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
InjectedThreadFlag
-
Not mapped to the IDM object.
InkDiv.dll
event.idm.read_only_udm.target.file.full_path
Part of
ExecutablesWritten
.
InkObj.dll
event.idm.read_only_udm.target.file.full_path
Part of
ExecutablesWritten
.
InMulticastPkts
-
Not mapped to the IDM object.
InOctets
-
Not mapped to the IDM object.
InUcastPkts
-
Not mapped to the IDM object.
IOARuleGroupName
IOARuleInstanceID
-
Not mapped to the IDM object.
IOARuleInstanceVersion
-
Not mapped to the IDM object.
IOARuleName
IOServiceClass
-
Not mapped to the IDM object.
IOServiceName
-
Not mapped to the IDM object.
IOServicePath
-
Not mapped to the IDM object.
IOServiceProperties
-
Not mapped to the IDM object.
IOServiceRegister
IoSessionConnected
IoSessionLoggedOn
IpEntryFlags
-
Not mapped to the IDM object.
IrpFlags
-
Not mapped to the IDM object.
IsCpuDataCommonOnAllCores
-
Not mapped to the IDM object.
IsNorthBridgeSupported
-
Not mapped to the IDM object.
IsOnClearCaseMvfs
-
Not mapped to the IDM object.
IsOnNetwork
IsOnRemovableDisk
IsOn
-
Not mapped to the IDM object.
IsRemote
-
Not mapped to the IDM object.
IsSouthBridgeSupported
-
Not mapped to the IDM object.
IsTransactedFile
-
Not mapped to the IDM object.
IsUnique
-
Not mapped to the IDM object.
JavaInjectedThread
JarFileWritten
KernelModeLoadImage
KernelTime
-
Not mapped to the IDM object.
KextUnload
K8SCreationTimestamp
K8SDetectionEvent
LanguageId
-
Not mapped to the IDM object.
LastAdded
-
Not mapped to the IDM object.
LastDiscoveredBy
-
Not mapped to the IDM object.
LastDisplayed
-
Not mapped to the IDM object.
LastLoggedOnHost
-
Not mapped to the IDM object.
LastUpdateInstalledTime
-
Not mapped to the IDM object.
LateralMovement
-
Not mapped to the IDM object.
LdapSearchAttributes
-
Not mapped to the IDM object.
LdapSearchBaseObjectSample
-
Not mapped to the IDM object.
LdapSearchFilterSample
-
Not mapped to the IDM object.
LdapSearchFilterShape
-
Not mapped to the IDM object.
LdapSearchQueryClassification
-
Not mapped to the IDM object.
LdapSearchQueryToken
-
Not mapped to the IDM object.
LdapSearchScope
-
Not mapped to the IDM object.
LdapSearchSizeLimit
-
Not mapped to the IDM object.
LdapSecurityType
-
Not mapped to the IDM object.
LightningLatencyInfo
LightningLatencyState
-
Not mapped to the IDM object.
Line
-
Not mapped to the IDM object.
LinkLocalAddressBehavior
-
Not mapped to the IDM object.
LinkLocalAddressTimeout
-
Not mapped to the IDM object.
LinkName
LocalAccount
-
Not mapped to the IDM object.
LocalAddressIP4
LocalAddressIP6
LocalAddressMaskIP4
-
Not mapped to the IDM object.
LocalAddressMaskIP6
-
Not mapped to the IDM object.
LocalAdminAccess
-
Not mapped to the IDM object.
LocalIpAddressIP4
LocalIpAddressIP6
LocalIpAddressRemovedIP4
LocalIpAddressRemovedIP6
LocalPort
LocalSession
-
Not mapped to the IDM object.
localipCount
LockScreenEnabled
-
Not mapped to the IDM object.
LockScreenStatus
LogoffTime
LogonDomain
LogonId
-
Not mapped to the IDM object.
LogonInfo
security_result.summary
Sets
event_type
to
USER_LOGIN
.
LogonServer
LogonTime
LogonType
event.idm.read_only_udm.extensions.auth.mechanism
Mapped to a UDM enum value based on the
LogonType
value.
LogoffTime
LsassHandleFromUnsignedModule
MAC
event.idm.read_only_udm.principal.mac
Converted to lowercase and colons are replaced with hyphens.
MACAddress
event.idm.read_only_udm.principal.mac
Hyphens are replaced with colons.
MACPrefix
-
Not mapped to the IDM object.
MachOFileWritten
MachOSubType
-
Not mapped to the IDM object.
MachineDn
MachineDomain
MajorFunction
-
Not mapped to the IDM object.
MajorVersion
-
Not mapped to the IDM object.
Malicious
-
Not mapped to the IDM object.
ManagedPdbBuildPath
MappedFromUserMode
-
Not mapped to the IDM object.
MaxReassemblySize
-
Not mapped to the IDM object.
MaxRouterAdvertisementInterval
-
Not mapped to the IDM object.
MaxThreadCount
-
Not mapped to the IDM object.
MD5HashData
event.idm.read_only_udm.target.file.md5
,
event.idm.read_only_udm.target.process.file.md5
If
MD5HashData
is a valid MD5 hash and not all zeros, create an MD5 hash entity with the value of
MD5HashData
and add it to
event.idm.read_only_udm.target.file.md5
and
event.idm.read_only_udm.target.process.file.md5
.
MD5String
MediaConnectState
-
Not mapped to the IDM object.
MediaType
-
Not mapped to the IDM object.
MemoryAvailable
-
Not mapped to the IDM object.
MemoryRegionProtection
-
Not mapped to the IDM object.
MemoryRegionStart
-
Not mapped to the IDM object.
MemoryTotal
-
Not mapped to the IDM object.
MmioDataSmiEn
-
Not mapped to the IDM object.
MmioDataTco1Cnt
-
Not mapped to the IDM object.
MLModelVersion
-
Not mapped to the IDM object.
MobileDetection
MobileDetectionId
-
Not mapped to the IDM object.
MobileOsIntegrityIntact
-
Not mapped to the IDM object.
MobileOsIntegrityStatus
MobilePowerStats
MoboManufacturer
-
Not mapped to the IDM object.
MoboProductName
-
Not mapped to the IDM object.
ModelPrediction
-
Not mapped to the IDM object.
ModuleBaseAddress
-
Not mapped to the IDM object.
ModuleCharacteristics
-
Not mapped to the IDM object.
ModuleDetectInfo
ModuleLoadCount
-
Not mapped to the IDM object.
ModuleLoadMechanism
-
Not mapped to the IDM object.
ModuleLoadTelemetryClassification
-
Not mapped to the IDM object.
ModuleNativePath
-
Not mapped to the IDM object.
ModuleSize
-
Not mapped to the IDM object.
ModifyServiceBinary
MostRecentActivityTimeStamp
-
Not mapped to the IDM object.
MotwWritten
mskssrv.sys
event.idm.read_only_udm.principal.process.file.full_path
Part of OriginalFilename.
MultipleInstancesPolicy
-
Not mapped to the IDM object.
name
namespace
NativePdbBuildPath
-
Not mapped to the IDM object.
NegateInterface
-
Not mapped to the IDM object.
NegateLocalAddress
-
Not mapped to the IDM object.
NegateRemoteAddress
-
Not mapped to the IDM object.
NeighborList
-
Not mapped to the IDM object.
NeighborListIP4
NeighborListIP6
NeighborName
NetLuidIndex
-
Not mapped to the IDM object.
NetShareAdd
NetShareDelete
NetShareSecurityModify
NetworkBindCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkCapableAsepWriteCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkCloseCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkCloseIP4
NetworkCloseIP6
NetworkConnectCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkConnectCountUdp
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkConnectIP4
NetworkConnectIP6
NetworkContainmentState
NetworkInterfaceGuid
-
Not mapped to the IDM object.
NetworkListenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkListenIP4
NetworkListenIP6
NetworkModuleLoadCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkRecvAcceptCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NetworkReceiveAcceptIP4
NetworkReceiveAcceptIP6
NewExecutableRenamed
NewExecutableWritten
NewExecutableWrittenCount
security_result.detection_fields[0].value
Part of
EndOfProcess
event.
NewFileIdentifier
-
Not mapped to the IDM object.
NewScriptWritten
NlMtu
-
Not mapped to the IDM object.
NorthBridgeDeviceId
-
Not mapped to the IDM object.
NorthBridgeVendorId
-
Not mapped to the IDM object.
NumberOfMeasurements
-
Not mapped to the IDM object.
OciContainerId
-
Not mapped to the IDM object.
OciContainerTelemetry
OciContainersStartedCount
-
Not mapped to the IDM object.
OciContainersStoppedCount
-
Not mapped to the IDM object.
OleFileWritten
OnLinkPrefixLength
-
Not mapped to the IDM object.
OoxmlFileWritten
OperStatus
-
Not mapped to the IDM object.
OperationFlags
-
Not mapped to the IDM object.
OperationName
OriginalContentLength
-
Not mapped to the IDM object.
OriginalEventTimeStamp
-
Not mapped to the IDM object.
OriginalFilename
OriginalParentAuthenticationId
-
Not mapped to the IDM object.
OriginalUserName
OriginalUserSid
OsfmDownloadComplete
OsVersionInfo
OU
OutBroadcastOctets
-
Not mapped to the IDM object.
OutDiscards
-
Not mapped to the IDM object.
OutErrors
-
Not mapped to the IDM object.
OutMulticastOctets
-
Not mapped to the IDM object.
OutNUcastPkts
-
Not mapped to the IDM object.
OutOctets
-
Not mapped to the IDM object.
OutUcastOctets
-
Not mapped to the IDM object.
OutUcastPkts
-
Not mapped to the IDM object.
PackedExecutableWritten
Parameter64_1
-
Not mapped to the IDM object.
Parameter64_2
-
Not mapped to the IDM object.
Parameter64_3
-
Not mapped to the IDM object.
ParameterSizedBuffer_1
-
Not mapped to the IDM object.
Parameter1
-
Not mapped to the IDM object.
Parameter2
-
Not mapped to the IDM object.
Parameter3
-
Not mapped to the IDM object.
ParentAuthenticationId
-
Not mapped to the IDM object.
ParentBaseFileName
ParentCommandLine
event1.ParentCommandLine
Part of
Event_DetectionSummaryEvent
.
ParentHubInstanceId
-
Not mapped to the IDM object.
ParentHubPort
-
Not mapped to the IDM object.
ParentImageFileName
event.idm.read_only_udm.principal.process.file.full_path
,
event1.ParentImageFileName
Part of
Event_DetectionSummaryEvent
.
ParentProcessId
event.idm.read_only_udm.principal.process.product_specific_process_id
,
event1.ParentProcessId
Prefixed with
CS:%{cid}:%{aid}:
. Part of
Event_DetectionSummaryEvent
.
PasswordLastSet
-
Not mapped to the IDM object.
PathMtuDiscoveryTimeout
-
Not mapped to the IDM object.
PatternDispositionFlags
-
Not mapped to the IDM object.
PatternDispositionValue
`PatternDisposition
Need more help?
Get answers from Community members and Google SecOps professionals.
