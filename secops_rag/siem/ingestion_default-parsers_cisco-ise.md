# Collect Cisco ISE logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ise/  
**Scraped:** 2026-03-05T09:21:35.415128Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco ISE logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco ISE logs to Google Security Operations using Bindplane.
The parser extracts fields from Cisco ISE syslog and CSV formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco ISE Administration portal
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
udplog
:
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'CISCO_ISE'
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
Configuration parameters
Replace the following placeholders:
Receiver configuration:
udplog
: Use
udplog
for UDP syslog or
tcplog
for TCP syslog
0.0.0.0
: IP address to listen on (
0.0.0.0
to listen on all interfaces)
514
: Port number to listen on (standard syslog port)
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
YOUR_CUSTOMER_ID
: Customer ID from the Get customer ID section
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
: Log type exactly as it appears in Chronicle (
CISCO_ISE
)
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
To restart the Bindplane agent in Windows, choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Syslog forwarding on Cisco ISE
Sign in to the
Cisco ISE Administration
portal.
Go to
Administration
>
System
>
Logging
>
Remote Logging Targets
.
Click
Add
to create a new remote logging target.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google-SecOps-Bindplane
).
Description
: Enter a description (optional).
IP Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Facility Code
: Select
LOCAL6
(or your preferred facility).
Maximum Length
: Enter
8192
(or the maximum supported value).
Include Alarms in Syslog Messages
: Check if you want to include alarms.
Click
Save
.
Go to
Administration
>
System
>
Logging
>
Logging Categories
.
Select each logging category you want to forward and click
Edit
:
AAA Audit
AAA Diagnostics
Accounting
Administrator Audit
Posture and Client Provisioning Audit
Profiler
System Diagnostics
In the
Targets
section, move the remote logging target
Google-SecOps-Bindplane
from
Available
to
Selected
.
Click
Save
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log field
UDM mapping
Remark
AAA_Event
security_result.detection_fields
AAA_Security_Result.detection_fields
aaa_service
ac-user-agent
network.http.user_agent
Acct-Authentic
security_result.detection_fields
Acct-Delay-Time
security_result.detection_fields
Acct-Input-Octets
security_result.detection_fields
Acct-Input-Packets
security_result.detection_fields
Acct-Output-Octets
security_result.detection_fields
Acct-Output-Packets
security_result.detection_fields
Acct-Session-Id
sec_result.detection_fields
additional.fields
Acct-Session-Time
security_result.detection_fields
Acct-Status-Type
security_result.detection_fields
Acct-Terminate-Cause
security_result.detection_fields
AcctReply-Status
security_result.detection_fields
AcctRequest-Flags
security_result.detection_fields
ACS_CiscoSecure_Defined_ACL
security_result.detection_fields
AcsSessionID
sec_result.detection_fields
additional.fields
Action
security_result.action_details
action_details
security_result.action_details
ActiveSessionCount
security_result.detection_fields
ad_identifier
about.hostname
ad_join_point
principal.administrative_domain
ad_operating_system
principal.platform
AD-Account-Name
principal.user.userid
target.hostname
AD-Domain
principal.group.group_display_name
AD-Domain-Controller
target.administrative_domain
AD-Error-Details
security_result.description
AD-Forest
target.resource.attribute.labels
AD-Groups-Names
principal.user.group_identifiers
AD-Host-Candidate-Identities
sec_result.detection_fields
AD-IP-Address
target.ip
target.asset.ip
AD-Log-Id
sec_result.detection_fields
AD-Site
target.location.name
AD-Srv-Query
security_result.detection_fields
AD-Srv-Record
security_result.detection_fields
AD-User-Candidate-Identities
principal.user.attribute.labels
AD-User-DNS-Domain
network.dns_domain
AD-User-Join-Point
target.hostname
target.asset.hostname
AD-User-NetBios-Name
principal.user.attribute.labels
AD-User-Qualified-Name
principal.user.email_addresses
AD-User-Resolved-DNs
principal.user.attribute.labels
AD-User-Resolved-Identities
sec_result.detection_fields
principal.user.userid
AD-User-Resolved-Identities
AD-User-SamAccount-Name
principal.user.attribute.labels
Admin
principal.user.userid
AdminInterface
principal.user.attribute.labels
AdminIPAddress
principal.ip
AdminName
principal.user.userid
affected-dn
target.resource.name
target.resource.attribute.labels
target.resource.resource_type
target.resource.resource_type
=>
"USER"
Airespace-Wlan-Id
additional.fields
allowEasyWiredSession
sec_result.detection_fields
additional.fields
AMInstalled
security_result.detection_fields
assetDeviceType
principal.resource.name
assetIncidentScore
security_result.detection_fields
Audit_session_id
sec_result.detection_fields
AuditSessionId
sec_result.detection_fields
Authen-Reply-Status
security_result.detection_fields
AuthenticationIdentityStore
sec_result.detection_fields
additional.fields
AuthenticationMethod
security_result.detection_fields
AuthenticationResult
security_result.action
AuthenticationStatus
security_result.action
security_result.action_details
Author-Reply-Status
additional.fields
AuthorizationFailureReason
security_result.detection_fields
AuthorizationPolicyMatchedRule
security_result.rule_name
av-pair-severity
security_result.detection_fields
BYODRegistration
sec_result.detection_fields
CacheUpdateTime
security_result.detection_fields
Called-Station-ID
security_result.detection_fields
target.ip
target.mac
Calling-Station-ID
security_result.detection_fields
principal.ip
principal.mac
cdpCacheAddressType
security_result.detection_fields
cdpCacheVersion
security_result.detection_fields
cdpUndefined28
security_result.detection_fields
change-set
additional.fields
Chargeable-User-Identity
principal.user.attribute.labels
cisco-av-pair
additional.fields
security_result.detection_fields
CiscoIOS
security_result.detection_fields
Class
sec_result.detection_fields
client_type
additional.fields
client-iif-id
security_result.detection_fields
ClientLatency
security_result.detection_fields
additional.fields
CmdSet
target.process.command_line
coa-push
security_result.detection_fields
CoAClientInstanceDestinationIPAddress
target.ip
target.asset.ip
coaReason
security_result.detection_fields
coaSourceComponent
security_result.detection_fields
coaType
security_result.detection_fields
Component
security_result.detection_fields
ConfigChangeData
security_result.detection_fields
ConfigVersionId
sec_result.detection_fields
additional.fields
connect-progress
security_result.detection_fields
ConnectionStatus
sec_result.detection_fields
ConnectionStatus=Failed
security_result.action ="BLOCK"
Constructeurs
principal.asset.hardware.manufacturer
counters_kvp
event.idm.read_only_udm.target.asset.attribute.labels
CPMSessionID
security_result.detection_fields
additional.fields
network.session_id
CreateTime
event.idm.read_only_udm.principal.asset.attribute.creation_time
cts_security_group_tag
security_result.detection_fields
cts-pac-opaque
security_result.detection_fields
datetime
metadata.event_timestamp
days_to_expiry
security_result.detection_fields
DeltaRadiusRequestCount
security_result.detection_fields
DeltaTacacsRequestCount
security_result.detection_fields
Description
security_result.detection_fields
DestinationIPAddress
target.ip
target.asset.ip
DestinationIPAddress
target.ip
target.asset.ip
DestinationPort
target.port
DetailedInfo
sec_result.description
Device_IP_Address
principal.ip
principal.asset.ip
device-mac
principal.mac
device-platform
principal.platform
device-platform-version
principal.platform_version
device-public-mac
principal.mac
device-type
principal.asset.hardware.model
device-uid
principal.resource.product_object_id
device-uid-global
principal.asset.product_object_id
DeviceIPAddress
principal.ip
target.ip
intermediary.ip
DevicePort
principal.port
target.port
intermediary.port
DeviceRegistrationStatus
sec_result.detection_fields
dhcp-class-identifier
security_result.detection_fields
dhcp-parameter-request-list
additional.fields
Domaines
additional.fields
DoReplicate
security_result.detection_fields
DTLSSupport
security_result.detection_fields
EAP-Key-Name
additional.fields
EapTunnel
additional.fields
EmailAddress
principal.user.email_addresses
EnableFlag
additional.fields
EnableSingleConnect
security_result.detection_fields
End-of-LLDPDU
security_result.detection_fields
endpoint_id
principal.mac
principal.asset.mac
EndpointCertainityMetric
sec_result.detection_fields
EndpointIdentityGroup
principal.group.group_display_name
EndpointIPAddress
principal.asset.ip
EndPointMACAddress
principal.mac
principal.asset.mac
EndPointMatchedProfile
security_result.about.labels
additional.fields
EndpointNADAddress
sec_result.detection_fields
EndpointOUI
sec_result.detection_fields
EndpointPolicy
principal.asset.platform_software.platform_version
security_result.detection_fields
EndPointPolicyID
security_result.detection_fields
EndPointProfilerServer
target.hostname
EndpointProperty
sec_result.detection_fields
EndPointSource
target.resource.attribute.labels
EndpointSourceEvent
sec_result.detection_fields
EndpointUserAgent
network.http.user_agent
EndPointVersion
security_result.detection_fields
epid
security_result.detection_fields
Error Message
additional.fields
event
additional.fields
extended_key_usage_oid
additional.fields
external_groups
additional.fields
FailureFlag
security_result.detection_fields
FailureReason
sec_result.detection_fields
additional.fields
FeedService
security_result.detection_fields
FirstCollection
event.idm.read_only_udm.principal.asset.first_discover_time
foreign_ip
intermediary.ip
FQSubjectName
security_result.detection_fields
Framed-MTU
additional.fields
Framed-Protocol
sec_result.detection_fields
FramedIPAddress
security_result.detection_fields
group_name
principal.group.group_display_name
Header-Flags
security_result.detection_fields
HostIdentityGroup
additional.fields
IdentityAccessRestricted
security_result.detection_fields
IdentityGroup
principal.group.group_display_name
IdentityGroupID
principal.group.product_object_id
IdentityPolicyMatchedRule
sec_result.about.labels
additional.fields
IdentitySelectionMatchedRule
sec_result.detection_fields
Idle-Timeout
security_result.detection_fields
idletime
security_result.detection_fields
IMEI
target.asset.product_object_id
inacl_rule
security_result.detection_fields
intermediary_hostname
intermediary.hostname
ionTimeStamp
security_result.detection_fields
ios-version
principal.asset.software.version
ip_inacl_rule
security_result.detection_fields
ip_source_ip
principal.ip
principal.asset.ip
IpAddress
principal.ip
principal.asset.ip
IPSEC
additional.fields
ise_port
principal.port
intermediary.port
ISELocalAddress
intermediary.ip
principal.ip
ISEModuleName
sec_result.detection_fields
ISEPolicySetName
target.resource.name
ISEServiceName
sec_result.detection_fields
IsMachineAuthentication
security_result.detection_fields
IsMachineIdentity
security_result.detection_fields
IsRegistered
security_result.detection_fields
Issuer
about.labels
IsThirdPartyDeviceFlow
sec_result.detection_fields
additional.fields
key_usage
additional.fields
LastActivity
event.idm.read_only_udm.principal.asset.last_discover_time
LastNmapScanTime
sec_result.detection_fields
LicenseType
additional.fields
lldpManAddress
security_result.detection_fields
lldpPortDescription
security_result.detection_fields
lldpPortId
security_result.detection_fields
lldpSystemCapabilitiesMap
security_result.detection_fields
lldpSystemDescription
security_result.detection_fields
lldpTimeToLive
security_result.detection_fields
lldpUndefined127
security_result.detection_fields
localport
principal.port
Location
principal.location.country_or_region
target.location.country_or_region
security_result.detection_fields
log-id
metadata.product_log_id
logstash.ingest.host
intermediary.hostname
logstash.ingest.timestamp
metadata.ingested_timestamp
logstash.irm_environment
additional.fields
logstash.irm_region
additional.fields
logstash.irm_site
additional.fields
logstash.process.host
intermediary.hostname
logstash.process.timestamp
metadata.collected_timestamp
MAC
principal.mac
mac_UserName
principal.mac
MacAddress
principal.mac
MajorVersion
security_result.detection_fields
Manufacturer
target.asset.hardware.manufacturer
MatchedPolicy
security_result.detection_fields
MatchedPolicyID
security_result.rule_id
MDMFailureReason
sec_result.detection_fields
MDMServerName
metadata.product_name
mDNS
security_result.detection_fields
MESSAGE
security_result.description
MFCInfoEndpointType
principal.asset.asset_type
principal.asset.attribute.labels
MinorVersion
security_result.detection_fields
MisconfiguredClientFixReason
security_result.detection_fields
Model
target.asset.hardware.model
Model_Name
principal.asset.attribute.labels
msg_class
metadata.description
msg_sev
security_result.severity
sec_result.severity_details
msg_text
metadata.description
security_result.severity
sec_result.severity_details,security_result.action
msg_text
security_result.action
NAD Address
principal.ip
NADAddress
intermediary.ip
Name
principal.group.group_identifiers
nas_ip_address
principal.nat_ip
NAS-Identifier
principal.labels
NAS-IP-Address
principal.nat_ip
principal.ip
NAS-Port
principal.port
principal.labels
nas-update
security_result.detection_fields
NASIdentifier
security_result.detection_fields
principal.labels
NASPort
principal.nat_port if valid else to security_result.detection_fields
principal.labels
NASPortId
security_result.detection_fields
principal.labels
NASPortType
security_result.detection_fields
principal.labels
Network Device Name
target.hostname
target.asset.hostname
network_adapter
target.resource.name
network_application_protocol_result
network.application_protocol
NetworkDeviceGroups
sec_result.detection_fields
NetworkDeviceGroups_IPSEC
additional.fields
NetworkDeviceProfileId
principal.asset.asset_id
NetworkDeviceProfileName
principal.asset.attribute.labels
NmapScanCount
security_result.detection_fields
ntp_server_1
target.ip
target.asset.ip
ntp_server_2
target.ip
target.asset.ip
ntp_server_3
target.ip
target.asset.ip
ObjectInternalID
security_result.detection_fields
ObjectName
security_result.about.labels
ObjectType
security_result.labout.abels
additional.fields
operating-system-result
target.asset.platform_software.platform_version
target.platform
=
WINDOWS
OperatingSystem
target.asset.platform_software.platform_version
OperationMessageText
sec_result.detection_fields
OperationMessageText
about.labels
OUI
security_result.detection_fields
pad
security_result.detection_fields
PeerAddress
target.mac
target.asset.mac
PeerName
target.hostname
target.asset.hostname
PhoneNumber
principal.user.phone_numbers
platform-version
principal.platform_version
PolicyVersion
security_result.detection_fields
Port
principal.port
target.port
Portal_Name
additional.fields
PortalName
target.url
PortalUser
principal.user.userid
PortalUser_GuestSponsor
principal.user.attribute.labels
PortalUser_GuestType
principal.user.attribute.labels
PostureApplicable
security_result.detection_fields
PostureAssessmentStatus
sec_result.detection_fields
additional.fields
PostureExpiry
sec_result.detection_fields
PostureStatus
sec_result.detection_fields
principal_hostname
principal.hostname
principal_ip
principal.ip
principal.asset.ip
profile-name
security_result.detection_fields
ProfilerServer
sec_result.detection_fields
Protocol
security_result.detection_fields
r_ip_or_host
observer.ip
observer.hostname
intermediary.hostname
intermediary.ip
r_seg_num
metadata.product_log_id
RadiusFlowType
security_result.about.labels
additional.fields
RadiusPacketType
security_result.detection_fields
received_b
network.received_bytes
RegisterStatus
security_result.rule_name
RegistrationTimeStamp
sec_result.detection_fields
RemoteAddress
principal.ip
principal.asset.ip
RequestLatency
sec_result.detection_fields
additional.fields
RequestResponseTypes
security_result.detection_fields
ResponseTime
sec_result.detection_fields
SelectedAccessService
sec_result.detection_fields
additional.fields
SelectedAuthenticationIdentityStores
security_result.detection_fields
SelectedAuthorizationProfiles
sec_result.detection_fields
additional.fields
SelectedShellProfile
additional.fields
sent_b
network.sent_bytes
sequence_num
metadata.product_log_id
Sequence-Number
security_result.detection_fields
serial_number
about.labels
network.tls.server.certificate.serial
server_label
principal.asset.attribute.labels
Service-Type
sec_result.detection_fields
additional.fields
session-id
network.session_id
Session-Timeout
network.session_duration
shell_role
principal.user.attribute.roles.name
ShutdownReason
security_result.detection_fields
SkipProfiling
security_result.detection_fields
software_version
principal.asset.platform_software.platform_version
Source
principal.ip
principal.hostname
source_ip
src.ip
source_port
src.port
SSID
additional.fields
start_time
security_result.first_discovered_time
StaticAssignment
security_result.detection_fields
StaticGroupAssignment
sec_result.detection_fields
Step
additional.fields
StepData
about.hostname
additional.fields
StepLatency
additional.fields
stop_time
security_result.last_discovered_time
Subject
about.labels
subject_alt_name
about.labels
subscriber_command
security_result.detection_fields
syslog_host
principal.ip
principal.asset.ip
SysStatsCpuCount
target.asset.hardware.cpu_number_cores
SysStatsProcessMemoryMB
target.asset.hardware.ram
SysStatsUtilizationDiskIO
target.asset.attribute.labels
SysStatsUtilizationDiskSpace
target.asset.attribute.labels
SysStatsUtilizationLoadAvg
target.asset.attribute.labels
SystemDomain
principal.asset.network_domain
SystemName
principal.hostname
principal.hostname
SystemUser
principal.user.userid
SystemUserDomain
principal.administrative_domain
target_email
target.user.email_addresses
target_group_identifiers
target.user.group_identifiers
target_hostname
target.hostname
target_ip
target.ip
target.asset.ip
target_port
target.port
target_user
target.user.userid
target.resource.resource_type
DEVICE
task_id
additional.fields
TaskId
security_result.detection_fields
Template_Name
additional.fields
Termination-Action
security_result.detection_fields
threshold_value
additional.fields
TimeToProfile
sec_result.detection_fields
TLSCipher
network.tls.cipher
TLSVersion
network.tls.version
total_certainty_factor
sec_result.detection_fields
TotalAuthenLatency
security_result.detection_fields
additional.fields
TotalFailedTime
sec_result.detection_fields
Tunnel-Client-Endpoint
sec_result.detection_fields
Type
additional.fields
undefined-151
additional.fields
UniqueConnectionIdentifier
sec_result.detection_fields
UpdateTime
sec_result.detection_fields
url-redirect
target.url
url-redirect-acl
security_result.detection_fields
UseCase
sec_result.detection_fields
used_space_value
additional.fields
User
principal.user.userid
user
principal.user.userid
user_display_name
principal.user.user_display_name
User-AD-Last-Fetch-Time
principal.user.attribute.labels
User-Agent
network.http.user_agent
network.http.parsed_user_agent
User-Fetch-Email
sec_result.detection_fields
User-Fetch-Last-Name
principal.user.last_name
User-Fetch-LocalityName
sec_result.detection_fields
User-Fetch-StateOrProvinceName
sec_result.detection_fields
User-Name
target.user.userid
UserAccountControl
principal.user.attribute.labels
UserAgreementStatus
security_result.detection_fields
UserName
target.user.userid
UserType
principal.user.attribute.labels
UseSingleConnect
security_result.detection_fields
vlan-id
security_result.detection_fields
principal.resource.resource_type
Statically mapped to
DEVICE
.
UDM mapping delta reference
On December 1, 2025, Google SecOps released a new version of the Cisco ISE parser, which includes significant changes to the mapping of Cisco ISE log fields to UDM fields and changes to the mapping of event types.
Log-field mapping delta
Globally, the timestamp that the Cisco ISE parser displays now is the raw log field
Event-Timestamp
. Previously, the timestamp that the Cisco ISE parser displayed was from the header.
The following table lists the mapping delta for Cisco ISE log-to-UDM fields exposed prior to December 1, 2025 and subsequently (listed in the
Old mapping
and
Current mapping
columns respectively):
Log field
Old mapping
Current mapping
Acct-Input-Gigawords
additional.fields
network.received_bytes
Acct-Input-Packets
security_result.detection_fields
network.received_packets
Acct-Output-Gigawords
additional.fields
network.sent_bytes
Acct-Output-Packets
security_result.detection_fields
network.sent_packets
Acct-Session-Id
security_result.detection_fields
additional.fields
security_result.detection_fields
AcsSessionID
security_result.detection_fields
additional.fields
network.session_id
security_result.detection_fields
AD-Log-Id
security_result.detection_fields
metadata.product_log_id
AD-User-SamAccount-Name
principal.user.attribute.labels
principal.user.user_display_name
allowEasyWiredSession
security_result.detection_fields
additional.fields
security_result.detection_fields
AuthenticationIdentityStore
security_result.detection_fields
additional.fields
security_result.detection_fields
Calling-Station-ID
security_result.detection_fields
additional.fields
principal.ip
security_result.detection_fields
ClientLatency
security_result.detection_fields
additional.fields
`
security_result.detection_fields
ConfigVersionId
security_result.detection_fields
additional.fields
security_result.detection_fields
CPMSessionID
security_result.detection_fields
additional.fields
network.sesson_id
network.sesson_id
DeviceIPAdresstarget.ip
target.ip
principal.ip
EndPointMatchedProfile
security_result.about.labels
additional.fields
security_result.about.resource.attribute.labels
HostIdentityGroup
additional.fields
principal.group.group_display_name
IdentityGroup
principal.group.group_display_name
principal.user.group_identifiers
IdentityPolicyMatchedRule
security_result.about.labels
additional.fields
security_result.rule_labels
IsThirdPartyDeviceFlow
security_result.detection_fields
additional.fields
security_result.detection_fields
Issuer
about.labels
network.tls.server.certificate.issuer
Location
principal.location.country_or_region
target.location.country_or_region,security_result.detection_fields
principal.location.country_or_region,
NAS Identifier
principal.labels
principal.asset.attribute.labels
NAS-IP-Address
principal.nat_ip,principal.ip
intermediary.ip
principal.nat_ip,principal.ip,
NAS-Port
principal.labels
principal.resource.attribute.labels
NAS-Port-Id
security_result.detection_fields
principal.labels
security_result.detection_fields
NAS-Port-Type
security_result.detection_fields
principal.labels
`
security_result.detection_fields
NASIdentifier
principal.resource.attribute.labels,security_result.detection_fields
principal.resource.attribute.labels
NASIdentifier
security_result.detection_fields
principal.labels
security_result.detection_fields
NetworkDeviceGroups_Location
intermediary.location.country_or_region
principal.location.country_or_region,
Object Name
security_result.about.labels
security_result.about.resource.attribute.labels
principal.mac
if it is a MAC
Object Type
security_result.about.labels
additional.fields
security_result.about.resource.attribute.labels
PostureAssessmentStatus
security_result.detection_fields
additional.fields
security_result.detection_fields
Privilege-Level
additional.fields
target.user.attribute.permissions.description
ProfilerServer
principal.hostname
security_result.detection_fields
principal.hostname
RadiusFlowType
security_result.detection_fields
additional.fields
security_result.detection_fields
RequestLatency
security_result.detection_fields
additional.fields
security_result.detection_fields
r_msg_id
security_result.detection_fields
metadata.product_log_id
r_seg_num
security_result.detection_fields
additional.fields
additional.fields
r_total_seg
security_result.detection_fields
additional.fields
additional.fields
SelectedAccessService
security_result.detection_fields
additional.fields
security_result.detection_fields
SelectedAuthorizationProfiles
security_result.detection_fields
additional.fields
security_result.detection_fields
Sequence-Number
metadata.product_log_id
security_result.detection_fields
if
AD-Log-Id
is not null
Server
principal.asset.attribute.labels
principal.hostname
principal.asset.hostname
Service-Type
security_result.detection_fields
additional.fields
security_result.detection_fields
serial_number
about.labels
about.resource.attribute.labels
ShutdownReason
security_result.detection_fields
security_result.description
Subject
about.labels
about.resource.attribute.labels
subject_alt_name
about.labels
about.resource.attribute.labels
subject_alt_name
about.labels
about.resource.attribute.labels
TotalAuthenLatency
security_result.detection_fields
additional.fields
security_result.detection_fields
total_certainty_factor
security_result.detection_fields
security_result.confidence_score
UniqueSubjectID
additional.fields
principal.user.userid.product_object_id
Update Time
security_result.detection_fields
principal.asset.attribute.last_update_time
User-Fetch-Email
security_result.detection_fields
principal.user.email_addresses
User-Fetch-LocalityName
security_result.detection_fields
principal.location.name
User-Fetch-StateOrProvinceName
security_result.detection_fields
principal.location.state
User Name when [r_cat_name] =~ "CISE_Passed_Authentications"
principal.user.userid
target.user.userid
principal.user.userid
wlan-profile-name
security_result.detection_fields
principal.user.userid
Event-type mapping delta
Multiple events that were classified generically are now properly classified with meaningful event types.
The following table lists the delta for the handling of Cisco ISE event types prior to December 1, 2025 and subsequently (listed in the
Old event_type
and
Current event-type
columns respectively):
Event ID from log and logic
Old event_type
Current event_type
(Based on event)
[has_resource] == "true"
GENERIC_EVENT
USER_RESOURCE_ACCESS
[Action] == "Login"
NETWORK_CONNECTION
USER_LOGIN
[PRAAction] =~ "logoff"
NETWORK_CONNECTION
USER_LOGOUT
[message] =~ "Administrator-Login"
USER_UNCATEGORIZED
USER_LOGIN
[message] =~ "Change password failed"
USER_LOGIN
USER_CHANGE_PASSWORD
[msg_text] =~ "Login Success"
USER_UNCATEGORIZED
USER_LOGIN
Need more help?
Get answers from Community members and Google SecOps professionals.
