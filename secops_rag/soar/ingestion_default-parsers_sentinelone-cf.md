# Collect SentinelOne Cloud Funnel logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-cf/  
**Scraped:** 2026-03-05T09:48:54.032107Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect SentinelOne Cloud Funnel logs
Supported in:
Google secops
SIEM
This document describes how you can export SentinelOne Cloud Funnel logs by setting up a Google Security Operations feed and how log fields map to Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations overview
.
A typical deployment consists of SentinelOne Cloud Funnel and the Google Security Operations feed configured to send logs to Google Security Operations. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
SentinelOne
: The platform from which you collect logs.
Google Security Operations feed
: The Google Security Operations feed that fetches logs from SentinelOne and writes logs to Google Security Operations.
Google Security Operations
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
SENTINELONE_CF
ingestion label.
Before you begin
Ensure you have the following prerequisites:
An active
Singularity Complete
subscription for
SentinelOne. Refer to
Platform Packages
for additional details.
An active license for the
Cloud Funnel
Data Lake Streaming Module.
SentinelOne Cloud Funnel v2.0
An Admin role for the Global or Account level. To get an Admin role, contact your administrator user.
Administrator rights to install the SentinelOne agent. To get administrator rights, contact your administrator user.
A configured Google Cloud Storage Bucket. For more information, see
Configure Your Google Cloud Storage Bucket
.
Replace
YOUR_CONSOLE_DOMAIN
in the URL with your specific console domain.
Set up SentinelOne Cloud Funnel
Sign in to the SentinelOne management console.
In the
Settings
toolbar, click
Integrations
>
Cloud Funnel
.
In the
Cloud Provider
list, select
Google Cloud
.
In the
GCS Storage Name
field, enter the name of the Cloud Storage bucket.
Click
Validate
to validate whether the bucket exists, and that SentinelOne has read and write access to the bucket.
Select
Enable Telemetry Streaming
to stream your XDR data to your bucket.
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
How to set up the SentinelOne Singularity Cloud Funnel feed
Click the
SentinelOne
pack.
Click the
SentinelOne Singularity Cloud Funnel
log type.
Specify the values for the following fields:
Source type
: Google Cloud Storage V2.
Storage bucket URI
: The Google Cloud Storage bucket source URI.
Source deletion option
: Whether to delete files or directories after transferring. Select the
Delete transferred files
option in
Source deletion option
.
Maximum File Age
: Include files modified within the last number of days. Default is 180 days.
Chronicle Service Account
: Copy the Service Account. You'll need it to add permissions in the bucket for this Service Account to let Google SecOps read or delete data in the bucket.
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
On the Google Cloud Storage Bucket, to add
Storage Object Admin
or
Storage Object User
permissions to this
Service Account
, follow these steps:
In your Google Cloud console, go to
Buckets
and select the bucket name.
In
Bucket Details
, go to
Permissions
>
Grant Access
.
In
New Principles
, paste
Service Account
that you copied.
In
Select a role
, select
Cloud Storage
, then select
Storage Object Admin
or
Storage Object User
role.
Click
Next
and then click
Submit
.
Supported SentinelOne Cloud Funnel log formats
The SentinelOne Cloud Funnel parser supports logs in JSON format.
Supported SentinelOne Cloud Funnel sample logs
JSON
{
  "src.process.parent.isStorylineRoot": true,
  "event.category": "group",
  "src.process.parent.image.sha1": "2d79a17a7f226b4a3bc25d47d73570f9a33aac1a",
  "site.id": "767524645468373018",
  "src.process.parent.displayName": "Services and Controller app",
  "src.process.image.binaryIsExecutable": true,
  "src.process.parent.subsystem": "SYS_WIN32",
  "src.process.user": "NT AUTHORITY\\\\SYSTEM",
  "src.process.indicatorRansomwareCount": 0,
  "src.process.crossProcessDupRemoteProcessHandleCount": 0,
  "src.process.tgtFileCreationCount": 0,
  "src.process.indicatorInjectionCount": 0,
  "src.process.moduleCount": 121,
  "i.version": "preprocess-lib-1.0",
  "src.process.parent.name": "services.exe",
  "src.process.image.md5": "b7f884c1b74a263f746ee12a5f7c9f6a",
  "src.process.indicatorReconnaissanceCount": 0,
  "src.process.storyline.id": "93CD8594B971B84A",
  "src.process.childProcCount": 0,
  "mgmt.url": "euce1-dummy.xyz.net",
  "src.process.crossProcessOpenProcessCount": 0,
  "src.process.subsystem": "SYS_WIN32",
  "meta.event.name": "GROUPCREATION",
  "src.process.parent.integrityLevel": "SYSTEM",
  "src.process.indicatorExploitationCount": 0,
  "src.process.parent.storyline.id": "31E78494B971B84A",
  "i.scheme": "edr",
  "src.process.integrityLevel": "SYSTEM",
  "site.name": "Dummy Corp",
  "src.process.netConnInCount": 0,
  "event.time": 1692575814995,
  "timestamp": "2023-08-20T23:56:54.995Z",
  "account.id": "767524645367709720",
  "dataSource.name": "SentinelOne",
  "endpoint.name": "Dummy Endpoint",
  "src.process.image.sha1": "1bc5066ddf693fc034d6514618854e26a84fd0d1",
  "src.process.isStorylineRoot": true,
  "src.process.parent.image.path": "C:\\\\windows\\\\System32\\\\services.exe",
  "dataSource.vendor": "SentinelOne",
  "src.process.pid": 21760,
  "tgt.file.isSigned": "signed",
  "dataSource.category": "security",
  "src.process.cmdline": "C:\\\\windows\\\\system32\\\\svchost.exe -k netsvcs -p -s wlidsvc",
  "src.process.publisher": "MICROSOFT WINDOWS",
  "src.process.crossProcessThreadCreateCount": 0,
  "src.process.parent.isNative64Bit": false,
  "src.process.parent.isRedirectCmdProcessor": false,
  "src.process.crossProcessCount": 0,
  "src.process.signedStatus": "signed",
  "event.id": "01H8B5MR9QQEYRC77NV97T2PR0_468",
  "src.process.parent.cmdline": "C:\\\\windows\\\\system32\\\\services.exe",
  "src.process.image.path": "C:\\\\windows\\\\System32\\\\svchost.exe",
  "src.process.tgtFileModificationCount": 0,
  "src.process.indicatorEvasionCount": 0,
  "src.process.netConnOutCount": 2,
  "src.process.crossProcessDupThreadHandleCount": 0,
  "endpoint.os": "windows",
  "src.process.tgtFileDeletionCount": 0,
  "src.process.startTime": 1692575814987,
  "mgmt.id": "12277",
  "os.name": "Windows 10 Enterprise",
  "src.process.displayName": "Host Process for Windows Services",
  "src.process.parent.sessionId": 0,
  "src.process.isNative64Bit": false,
  "src.process.uid": "92CD8594B971B84A",
  "src.process.parent.image.md5": "14b88ff4833012512278a5f3a5712bd2",
  "src.process.indicatorBootConfigurationUpdateCount": 0,
  "src.process.indicatorInfostealerCount": 20,
  "process.unique.key": "92CD8594B971B84A",
  "agent.version": "22.2.4.558",
  "src.process.parent.uid": "30E78494B971B84A",
  "src.process.parent.image.sha256": "e6fe9a94e8686e957dbcec2b89c1c1ddcf8e75d76e9200d0cbef74d510c71317",
  "src.process.sessionId": 0,
  "src.process.netConnCount": 2,
  "mgmt.osRevision": "19045",
  "group.id": "93CD8594B971B84A",
  "src.process.parent.publisher": "MICROSOFT WINDOWS PUBLISHER",
  "src.process.isRedirectCmdProcessor": false,
  "src.process.verifiedStatus": "verified",
  "src.process.parent.startTime": 1692333530832,
  "src.process.dnsCount": 4,
  "endpoint.type": "laptop",
  "trace.id": "01H8B5MR9QQEYRC77NV97T2PR0",
  "src.process.name": "svchost.exe",
  "agent.uuid": "615151318b7b4f8fb4fa1d1b28b7ad0f",
  "src.process.image.sha256": "add683a6910abbbf0e28b557fad0ba998166394932ae2aca069d9aa19ea8fe88",
  "src.process.indicatorGeneralCount": 8,
  "src.process.crossProcessOutOfStorylineCount": 0,
  "packet.id": "80BC84D0E056415C91A410DDA4B523CD",
  "src.process.registryChangeCount": 0,
  "src.process.indicatorPersistenceCount": 0,
  "src.process.parent.signedStatus": "signed",
  "src.process.parent.user": "NT AUTHORITY\\\\SYSTEM",
  "event.type": "Group Creation",
  "src.process.indicatorPostExploitationCount": 0,
  "src.process.parent.pid": 1568
}
Supported SentinelOne Cloud Funnel log types
The SentinelOne Cloud Funnel parser supports the following log types:
Event Type
Process Exit
Process Modification
Process Creation
Duplicate Process Handle
Duplicate Thread Handle
Open Remote Process Handle
Remote Thread Creation
Remote Process Termination
Command Script
IP Connect
IP Listen
File Modification
File Creation
File Scan
File Deletion
File Rename
Pre Execution Detection
Login
Logout
GET
OPTIONS
POST
PUT
DELETE
CONNECT
HEAD
DNS Resolved
DNS Unresolved
Task Register
Task Update
Task Start
Task Trigger
Task Delete
Registry Key Create
Registry Key Rename
Registry Key Delete
Registry Key Export
Registry Key Security Changed
Registry Key Import
Registry Value Modified
Registry Value Create
Registry Value Delete
Behavioral Indicators
Module Load
Driver Load
Not Reported
Group Creation
Firmware Test
Threat Intelligence Indicators
Named Pipe Creation
Named Pipe Connection
Windows Event Log Creation
Set up feeds from the Content Hub
Specify values for the following fields:
Storage bucket URI
: The Google Cloud Storage bucket source URI.
URI is a
: Select the URI TYPE according to log stream configuration (
Single file
|
Directory
|
Directory which includes subdirectories
).
Source deletion options
: Select the deletion option according to your ingestion preferences.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Source Type
: Method used to collect logs into Google SecOps.
Asset Namespace
:
Namespace associated with the feed
.
Ingestion Labels
: Labels applied to all events from this feed.
Field mapping reference
This section explains how the Google Security Operations parser maps SentinelOne fields to Google Security Operations Unified Data Model (UDM) fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
SENTINELONE_CF
log types and their corresponding UDM event types.
Event Identifier
Event Type
Process Exit
PROCESS_TERMINATION
Process Modification
PROCESS_UNCATEGORIZED
Process Creation
PROCESS_LAUNCH
Duplicate Process Handle
PROCESS_UNCATEGORIZED
Duplicate Thread Handle
PROCESS_UNCATEGORIZED
Open Remote Process Handle
PROCESS_UNCATEGORIZED
Remote Thread Creation
PROCESS_UNCATEGORIZED
Remote Process Termination
PROCESS_TERMINATION
Command Script
PROCESS_UNCATEGORIZED
IP Connect
NETWORK_CONNECTION
IP Listen
STATUS_UPDATE
File Modification
FILE_MODIFICATION
File Creation
FILE_CREATION
File Scan
SCAN_FILE
File Deletion
FILE_DELETION
File Rename
FILE_MOVE
Pre Execution Detection
STATUS_UPDATE
Login
USER_LOGIN
Logout
USER_LOGOUT
GET
NETWORK_HTTP
OPTIONS
NETWORK_HTTP
POST
NETWORK_HTTP
PUT
NETWORK_HTTP
DELETE
NETWORK_HTTP
CONNECT
NETWORK_HTTP
HEAD
NETWORK_HTTP
DNS Resolved
NETWORK_DNS
DNS Unresolved
NETWORK_DNS
Task Register
SCHEDULED_TASK_CREATION
Task Update
SCHEDULED_TASK_MODIFICATION
Task Start
SCHEDULED_TASK_UNCATEGORIZED
Task Trigger
SCHEDULED_TASK_UNCATEGORIZED
Task Delete
SCHEDULED_TASK_DELETION
Registry Key Create
REGISTRY_CREATION
Registry Key Rename
REGISTRY_UNCATEGORIZED
Registry Key Delete
REGISTRY_DELETION
Registry Key Export
REGISTRY_UNCATEGORIZED
Registry Key Security Changed
REGISTRY_MODIFICATION
Registry Key Import
REGISTRY_UNCATEGORIZED
Registry Value Modified
REGISTRY_MODIFICATION
Registry Value Create
REGISTRY_CREATION
Registry Value Delete
REGISTRY_DELETION
Behavioral Indicators
STATUS_UPDATE
Module Load
PROCESS_MODULE_LOAD
Driver Load
PROCESS_MODULE_LOAD
Not Reported
NETWORK_HTTP
Group Creation
GROUP_CREATION
Firmware Test
STATUS_UPDATE
Threat Intelligence Indicators
STATUS_UPDATE
Named Pipe Creation
RESOURCE_CREATION
Named Pipe Connection
STATUS_UPDATE
Field mapping reference: SENTINELONE_CF
The following table lists the log fields of the
SENTINELONE_CF
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
winEventLog.description
about.labels[win_event_log_description]
(deprecated)
winEventLog.description
additional.fields[win_event_log_description]
event.time
metadata.event_timestamp
winEventLog.creationDate
about.labels[win_event_log_creation_date]
(deprecated)
winEventLog.creationDate
additional.fields[win_event_log_creation_date]
account.id
metadata.product_deployment_id
event.type
metadata.product_event_type
event.id
metadata.product_log_id
winEventLog.id
about.labels[win_event_log_id]
(deprecated)
winEventLog.id
additional.fields[win_event_log_id]
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
SentinelOne
.
extensions.auth.auth_details
If the
event.type
log field value contain one of the following values, then the
event.type
log field is mapped to the
extensions.auth.auth_details
UDM field.
Login
Logout
extensions.auth.mechanism
If the
event.login.type
log field value is equal to
NETWORK
, then the
extensions.auth.mechanism
UDM field is set to
NETWORK
.
Else, if the
event.login.type
log field value is equal to
SYSTEM
, then the
extensions.auth.mechanism
UDM field is set to
LOCAL
.
Else, if the
event.login.type
log field value is equal to
INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
INTERACTIVE
.
Else, if the
event.login.type
log field value is equal to
BATCH
, then the
extensions.auth.mechanism
UDM field is set to
BATCH
.
Else, if the
event.login.type
log field value is equal to
SERVICE
, then the
extensions.auth.mechanism
UDM field is set to
SERVICE
.
Else, if the
event.login.type
log field value is equal to
UNLOCK
, then the
extensions.auth.mechanism
UDM field is set to
UNLOCK
.
Else, if the
event.login.type
log field value is equal to
NETWORK_CLEAR_TEXT
, then the
extensions.auth.mechanism
UDM field is set to
NETWORK_CLEAR_TEXT
.
Else, if the
event.login.type
log field value is equal to
NEW_CREDENTIALS
, then the
extensions.auth.mechanism
UDM field is set to
NEW_CREDENTIALS
.
Else, if the
event.login.type
log field value is equal to
REMOTE_INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
Else, if the
event.login.type
log field value is equal to
CACHED_INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_INTERACTIVE
.
Else, if the
event.login.type
log field value is equal to
CACHED_REMOTE_INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_REMOTE_INTERACTIVE
.
Else, if the
event.login.type
log field value is equal to
CACHED_UNLOCK
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_UNLOCK
.
network.application_protocol
If the
event.type
log field value contain one of the following values, then the
network.application_protocol
UDM field is set to
DNS
.
DNS Resolved
DNS Unresolved
network.direction
If the
event.network.direction
log field value is equal to
OUTGOING
, then the
network.direction
UDM field is set to
OUTBOUND
.
Else, if the
event.network.direction
log field value is equal to
INCOMING
, then the
network.direction
UDM field is set to
INBOUND
.
event.dns.response
network.dns.answers.name
event.dns.response
network.dns.answers.type
event.dns.request
network.dns.questions.name
event.url.action
network.http.method
event.login.sessionId
network.session_id
agent.uuid
principal.asset.asset_id
agent.uuid
principal.asset_id
agent.version
principal.asset.attribute.labels[agent_version]
winEventLog.description.accountDomain
principal.labels[win_event_log_description_account_domain]
(deprecated)
winEventLog.description.accountDomain
additional.fields[win_event_log_description_account_domain]
principal.asset.platform_software.platform
If the
endpoint.os
log field value is equal to
windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
endpoint.os
log field value is equal to
linux
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
principal.asset.type
If the
endpoint.type
log field value is equal to
laptop
, then the
principal.asset.type
UDM field is set to
LAPTOP
.
Else, if the
endpoint.type
log field value contain one of the following values, then the
principal.asset.type
UDM field is set to
SERVER
.
server
Kubernetes Node
Else, if the
endpoint.type
log field value is equal to
desktop
, then the
principal.asset.type
UDM field is set to
WORKSTATION
.
endpoint.name
principal.hostname
endpoint.name
principal.asset.hostname
src.endpoint.ip.address
principal.ip
src.ip.address
principal.ip
osSrc.process.activeContent.hash
principal.labels[os_src_process_active_content_hash]
(deprecated)
osSrc.process.activeContent.hash
additional.fields[os_src_process_active_content_hash]
osSrc.process.activeContent.id
principal.labels[os_src_process_active_content_id]
(deprecated)
osSrc.process.activeContent.id
additional.fields[os_src_process_active_content_id]
osSrc.process.activeContent.path
principal.labels[os_src_process_active_content_path]
(deprecated)
osSrc.process.activeContent.path
additional.fields[os_src_process_active_content_path]
osSrc.process.activeContent.signedStatus
principal.labels[os_src_process_active_content_signed_status]
(deprecated)
osSrc.process.activeContent.signedStatus
additional.fields[os_src_process_active_content_signed_status]
osSrc.process.activeContentType
principal.labels[os_src_process_active_content_type]
(deprecated)
osSrc.process.activeContentType
additional.fields[os_src_process_active_content_type]
osSrc.process.childProcCount
principal.labels[os_src_process_child_proc_count]
(deprecated)
osSrc.process.childProcCount
additional.fields[os_src_process_child_proc_count]
osSrc.process.crossProcessCount
principal.labels[os_src_process_cross_process_count]
(deprecated)
osSrc.process.crossProcessCount
additional.fields[os_src_process_cross_process_count]
osSrc.process.crossProcessDupRemoteProcessHandleCount
principal.labels[os_src_process_cross_process_dup_rmote_process_handle_count]
(deprecated)
osSrc.process.crossProcessDupRemoteProcessHandleCount
additional.fields[os_src_process_cross_process_dup_rmote_process_handle_count]
osSrc.process.crossProcessDupThreadHandleCount
principal.labels[os_src_process_cross_process_dup_thread_handle_count]
(deprecated)
osSrc.process.crossProcessDupThreadHandleCount
additional.fields[os_src_process_cross_process_dup_thread_handle_count]
osSrc.process.crossProcessOpenProcessCount
principal.labels[os_src_process_cross_process_open_process_count]
(deprecated)
osSrc.process.crossProcessOpenProcessCount
additional.fields[os_src_process_cross_process_open_process_count]
osSrc.process.crossProcessOutOfStorylineCount
principal.labels[os_src_process_cross_process_out_of_storyline_count]
(deprecated)
osSrc.process.crossProcessOutOfStorylineCount
additional.fields[os_src_process_cross_process_out_of_storyline_count]
osSrc.process.crossProcessThreadCreateCount
principal.labels[os_src_process_cross_process_thread_create_count]
(deprecated)
osSrc.process.crossProcessThreadCreateCount
additional.fields[os_src_process_cross_process_thread_create_count]
osSrc.process.displayName
principal.labels[os_src_process_display_name]
(deprecated)
osSrc.process.displayName
additional.fields[os_src_process_display_name]
osSrc.process.dnsCount
principal.labels[os_src_process_dns_count]
(deprecated)
osSrc.process.dnsCount
additional.fields[os_src_process_dns_count]
osSrc.process.image.binaryIsExecutable
principal.labels[os_src_process_image_binary_is_executable]
(deprecated)
osSrc.process.image.binaryIsExecutable
additional.fields[os_src_process_image_binary_is_executable]
osSrc.process.indicatorBootConfigurationUpdateCount
principal.labels[os_src_process_indicator_boot_configuration_update_count]
(deprecated)
osSrc.process.indicatorBootConfigurationUpdateCount
additional.fields[os_src_process_indicator_boot_configuration_update_count]
osSrc.process.indicatorEvasionCount
principal.labels[os_src_process_indicator_evasion_count]
(deprecated)
osSrc.process.indicatorEvasionCount
additional.fields[os_src_process_indicator_evasion_count]
osSrc.process.indicatorExploitationCount
principal.labels[os_src_process_indicator_exploitation_count]
(deprecated)
osSrc.process.indicatorExploitationCount
additional.fields[os_src_process_indicator_exploitation_count]
osSrc.process.indicatorGeneral.count
principal.labels[os_src_process_indicator_general_count]
(deprecated)
osSrc.process.indicatorGeneral.count
additional.fields[os_src_process_indicator_general_count]
osSrc.process.indicatorInfostealerCount
principal.labels[os_src_process_indicator_infostealer_count]
(deprecated)
osSrc.process.indicatorInfostealerCount
additional.fields[os_src_process_indicator_infostealer_count]
osSrc.process.indicatorInjectionCount
principal.labels[os_src_process_indicator_injection_count]
(deprecated)
osSrc.process.indicatorInjectionCount
additional.fields[os_src_process_indicator_injection_count]
osSrc.process.indicatorPersistenceCount
principal.labels[os_src_process_indicator_persistence_count]
(deprecated)
osSrc.process.indicatorPersistenceCount
additional.fields[os_src_process_indicator_persistence_count]
osSrc.process.indicatorPostExploitationCount
principal.labels[os_src_process_indicator_post_exploitation_count]
(deprecated)
osSrc.process.indicatorPostExploitationCount
additional.fields[os_src_process_indicator_post_exploitation_count]
osSrc.process.indicatorRansomwareCount
principal.labels[os_src_process_indicator_ransomware_count]
(deprecated)
osSrc.process.indicatorRansomwareCount
additional.fields[os_src_process_indicator_ransomware_count]
osSrc.process.indicatorReconnaissanceCount
principal.labels[os_src_process_indicator_reconnaissance_count]
(deprecated)
osSrc.process.indicatorReconnaissanceCount
additional.fields[os_src_process_indicator_reconnaissance_count]
osSrc.process.integrityLevel
principal.labels[os_src_process_integrity_level]
(deprecated)
osSrc.process.integrityLevel
additional.fields[os_src_process_integrity_level]
osSrc.process.isNative64Bit
principal.labels[os_src_process_is_native_64_bit]
(deprecated)
osSrc.process.isNative64Bit
additional.fields[os_src_process_is_native_64_bit]
osSrc.process.isRedirectCmdProcessor
principal.labels[os_src_process_is_redirect_cmd_processor]
(deprecated)
osSrc.process.isRedirectCmdProcessor
additional.fields[os_src_process_is_redirect_cmd_processor]
osSrc.process.isStorylineRoot
principal.labels[os_src_process_is_storyline_root]
(deprecated)
osSrc.process.isStorylineRoot
additional.fields[os_src_process_is_storyline_root]
osSrc.process.moduleCount
principal.labels[os_src_process_module_count]
(deprecated)
osSrc.process.moduleCount
additional.fields[os_src_process_module_count]
osSrc.process.netConnCount
principal.labels[os_src_process_net_conn_count]
(deprecated)
osSrc.process.netConnCount
additional.fields[os_src_process_net_conn_count]
osSrc.process.netConnInCount
principal.labels[os_src_process_net_conn_in_count]
(deprecated)
osSrc.process.netConnInCount
additional.fields[os_src_process_net_conn_in_count]
osSrc.process.netConnOutCount
principal.labels[os_src_process_net_conn_out_count]
(deprecated)
osSrc.process.netConnOutCount
additional.fields[os_src_process_net_conn_out_count]
osSrc.process.parent.activeContent.hash
principal.labels[os_src_process_parent_active_content_hash]
(deprecated)
osSrc.process.parent.activeContent.hash
additional.fields[os_src_process_parent_active_content_hash]
osSrc.process.parent.activeContent.id
principal.labels[os_src_process_parent_active_content_id]
(deprecated)
osSrc.process.parent.activeContent.id
additional.fields[os_src_process_parent_active_content_id]
osSrc.process.parent.activeContent.path
principal.labels[os_src_process_parent_active_content_path]
(deprecated)
osSrc.process.parent.activeContent.path
additional.fields[os_src_process_parent_active_content_path]
osSrc.process.parent.activeContent.signedStatus
principal.labels[os_src_process_parent_active_content_signed_status]
(deprecated)
osSrc.process.parent.activeContent.signedStatus
additional.fields[os_src_process_parent_active_content_signed_status]
osSrc.process.parent.activeContentType
principal.labels[os_src_process_parent_active_content_type]
(deprecated)
osSrc.process.parent.activeContentType
additional.fields[os_src_process_parent_active_content_type]
osSrc.process.parent.displayName
principal.labels[os_src_process_parent_display_name]
(deprecated)
osSrc.process.parent.displayName
additional.fields[os_src_process_parent_display_name]
osSrc.process.parent.integrityLevel
principal.labels[os_src_process_parent_integrity_level]
(deprecated)
osSrc.process.parent.integrityLevel
additional.fields[os_src_process_parent_integrity_level]
osSrc.process.parent.isNative64Bit
principal.labels[os_src_process_parent_is_native_64_bit]
(deprecated)
osSrc.process.parent.isNative64Bit
additional.fields[os_src_process_parent_is_native_64_bit]
osSrc.process.parent.isRedirectCmdProcessor
principal.labels[os_src_process_parent_is_redirect_cmd_processor]
(deprecated)
osSrc.process.parent.isRedirectCmdProcessor
additional.fields[os_src_process_parent_is_redirect_cmd_processor]
osSrc.process.parent.isStorylineRoot
principal.labels[os_src_process_parent_is_storyline_root]
(deprecated)
osSrc.process.parent.isStorylineRoot
additional.fields[os_src_process_parent_is_storyline_root]
osSrc.process.parent.publisher
principal.labels[os_src_process_parent_publisher]
(deprecated)
osSrc.process.parent.publisher
additional.fields[os_src_process_parent_publisher]
osSrc.process.parent.sessionId
principal.labels[os_src_process_parent_session_id]
(deprecated)
osSrc.process.parent.sessionId
additional.fields[os_src_process_parent_session_id]
osSrc.process.parent.signedStatus
principal.process_ancestors.parent_process.file.signature_info.sigcheck.verification_message
osSrc.process.parent.startTime
principal.labels[os_src_process_parent_start_time]
(deprecated)
osSrc.process.parent.startTime
additional.fields[os_src_process_parent_start_time]
osSrc.process.parent.storyline.id
principal.labels[os_src_process_parent_storyline_id]
(deprecated)
osSrc.process.parent.storyline.id
additional.fields[os_src_process_parent_storyline_id]
src.process.parent.storyline.id
principal.labels[src_process_parent_storyline_id]
(deprecated)
src.process.parent.storyline.id
additional.fields[src_process_parent_storyline_id]
osSrc.process.publisher
principal.labels[os_src_process_publisher]
(deprecated)
osSrc.process.publisher
additional.fields[os_src_process_publisher]
osSrc.process.registryChangeCount
principal.labels[os_src_process_registry_change_count]
(deprecated)
osSrc.process.registryChangeCount
additional.fields[os_src_process_registry_change_count]
osSrc.process.sessionId
principal.labels[os_src_process_session_id]
(deprecated)
osSrc.process.sessionId
additional.fields[os_src_process_session_id]
osSrc.process.signedStatus
principal.process_ancestors.file.signature_info.sigcheck.verification_message
osSrc.process.startTime
principal.labels[os_src_process_start_time]
(deprecated)
osSrc.process.startTime
additional.fields[os_src_process_start_time]
osSrc.process.storyline.id
principal.labels[os_src_process_storyline_id]
(deprecated)
osSrc.process.storyline.id
additional.fields[os_src_process_storyline_id]
osSrc.process.subsystem
principal.labels[os_src_process_subsystem]
(deprecated)
osSrc.process.subsystem
additional.fields[os_src_process_subsystem]
osSrc.process.tgtFileCreationCount
principal.labels[os_src_process_tgt_file_creation_count]
(deprecated)
osSrc.process.tgtFileCreationCount
additional.fields[os_src_process_tgt_file_creation_count]
osSrc.process.tgtFileDeletionCount
principal.labels[os_src_process_tgt_file_deletion_count]
(deprecated)
osSrc.process.tgtFileDeletionCount
additional.fields[os_src_process_tgt_file_deletion_count]
osSrc.process.tgtFileModificationCount
principal.labels[os_src_process_tgt_file_modification_count]
(deprecated)
osSrc.process.tgtFileModificationCount
additional.fields[os_src_process_tgt_file_modification_count]
osSrc.process.verifiedStatus
principal.labels[os_src_process_verified_status]
(deprecated)
osSrc.process.verifiedStatus
additional.fields[os_src_process_verified_status]
process.unique.key
principal.labels[process_unique_key]
(deprecated)
process.unique.key
additional.fields[process_unique_key]
site.name
principal.labels[site_name]
(deprecated)
site.name
additional.fields[site_name]
src.process.activeContent.hash
principal.labels[src_process_active_content_hash]
(deprecated)
src.process.activeContent.hash
additional.fields[src_process_active_content_hash]
src.process.activeContent.id
principal.labels[src_process_active_content_id]
(deprecated)
src.process.activeContent.id
additional.fields[src_process_active_content_id]
src.process.activeContent.path
principal.labels[src_process_active_content_path]
(deprecated)
src.process.activeContent.path
additional.fields[src_process_active_content_path]
src.process.activeContent.signedStatus
principal.labels[src_process_active_content_signed_status]
(deprecated)
src.process.activeContent.signedStatus
additional.fields[src_process_active_content_signed_status]
src.process.activeContentType
principal.labels[src_process_active_content_type]
(deprecated)
src.process.activeContentType
additional.fields[src_process_active_content_type]
src.process.childProcCount
principal.labels[src_process_child_proc_count]
(deprecated)
src.process.childProcCount
additional.fields[src_process_child_proc_count]
src.process.crossProcessCount
principal.labels[src_process_cross_process_count]
(deprecated)
src.process.crossProcessCount
additional.fields[src_process_cross_process_count]
src.process.crossProcessDupRemoteProcessHandleCount
principal.labels[src_process_cross_process_dup_remote_process_handle_count]
(deprecated)
src.process.crossProcessDupRemoteProcessHandleCount
additional.fields[src_process_cross_process_dup_remote_process_handle_count]
src.process.crossProcessDupThreadHandleCount
principal.labels[src_process_cross_process_dup_thread_handle_count]
(deprecated)
src.process.crossProcessDupThreadHandleCount
additional.fields[src_process_cross_process_dup_thread_handle_count]
src.process.crossProcessOpenProcessCount
principal.labels[src_process_cross_process_open_process_count]
(deprecated)
src.process.crossProcessOpenProcessCount
additional.fields[src_process_cross_process_open_process_count]
src.process.crossProcessOutOfStorylineCount
principal.labels[src_process_cross_process_out_of_storyline_count]
(deprecated)
src.process.crossProcessOutOfStorylineCount
additional.fields[src_process_cross_process_out_of_storyline_count]
src.process.crossProcessThreadCreateCount
principal.labels[src_process_cross_process_thread_create_count]
(deprecated)
src.process.crossProcessThreadCreateCount
additional.fields[src_process_cross_process_thread_create_count]
src.process.displayName
principal.labels[src_process_display_name]
(deprecated)
src.process.displayName
additional.fields[src_process_display_name]
src.process.dnsCount
principal.labels[src_process_dns_count]
(deprecated)
src.process.dnsCount
additional.fields[src_process_dns_count]
src.process.image.binaryIsExecutable
principal.labels[src_process_image_binary_is_executable]
(deprecated)
src.process.image.binaryIsExecutable
additional.fields[src_process_image_binary_is_executable]
src.process.indicatorBootConfigurationUpdateCount
principal.labels[src_process_indicator_boot_configuration_update_count]
(deprecated)
src.process.indicatorBootConfigurationUpdateCount
additional.fields[src_process_indicator_boot_configuration_update_count]
src.process.indicatorEvasionCount
principal.labels[src_process_indicator_evasion_count]
(deprecated)
src.process.indicatorEvasionCount
additional.fields[src_process_indicator_evasion_count]
src.process.indicatorExploitationCount
principal.labels[src_process_indicator_exploitation_count]
(deprecated)
src.process.indicatorExploitationCount
additional.fields[src_process_indicator_exploitation_count]
src.process.indicatorGeneralCount
principal.labels[src_process_indicator_general_count]
(deprecated)
src.process.indicatorGeneralCount
additional.fields[src_process_indicator_general_count]
src.process.indicatorInfostealerCount
principal.labels[src_process_indicator_infostealer_count]
(deprecated)
src.process.indicatorInfostealerCount
additional.fields[src_process_indicator_infostealer_count]
src.process.indicatorInjectionCount
principal.labels[src_process_indicator_injection_count]
(deprecated)
src.process.indicatorInjectionCount
additional.fields[src_process_indicator_injection_count]
src.process.indicatorPersistenceCount
principal.labels[src_process_indicator_persistence_count]
(deprecated)
src.process.indicatorPersistenceCount
additional.fields[src_process_indicator_persistence_count]
src.process.indicatorPostExploitationCount
principal.labels[src_process_indicator_post_exploitation_count]
(deprecated)
src.process.indicatorPostExploitationCount
additional.fields[src_process_indicator_post_exploitation_count]
src.process.indicatorRansomwareCount
principal.labels[src_process_indicator_ransomware_count]
(deprecated)
src.process.indicatorRansomwareCount
additional.fields[src_process_indicator_ransomware_count]
src.process.indicatorReconnaissanceCount
principal.labels[src_process_indicator_reconnaissance_count]
(deprecated)
src.process.indicatorReconnaissanceCount
additional.fields[src_process_indicator_reconnaissance_count]
src.process.integrityLevel
principal.labels[src_process_integrity_level]
(deprecated)
src.process.integrityLevel
additional.fields[src_process_integrity_level]
src.process.isNative64Bit
principal.labels[src_process_is_native_64_bit]
(deprecated)
src.process.isNative64Bit
additional.fields[src_process_is_native_64_bit]
src.process.isRedirectCmdProcessor
principal.labels[src_process_is_redirect_cmd_processor]
(deprecated)
src.process.isRedirectCmdProcessor
additional.fields[src_process_is_redirect_cmd_processor]
src.process.isStorylineRoot
principal.labels[src_process_is_storyline_root]
(deprecated)
src.process.isStorylineRoot
additional.fields[src_process_is_storyline_root]
src.process.lUserUid
principal.labels[src_process_l_user_uid]
(deprecated)
src.process.lUserUid
additional.fields[src_process_l_user_uid]
src.process.moduleCount
principal.labels[src_process_module_count]
(deprecated)
src.process.moduleCount
additional.fields[src_process_module_count]
src.process.netConnCount
principal.labels[src_process_net_conn_count]
(deprecated)
src.process.netConnCount
additional.fields[src_process_net_conn_count]
src.process.netConnInCount
principal.labels[src_process_net_conn_in_count]
(deprecated)
src.process.netConnInCount
additional.fields[src_process_net_conn_in_count]
src.process.netConnOutCount
principal.labels[src_process_net_conn_out_count]
(deprecated)
src.process.netConnOutCount
additional.fields[src_process_net_conn_out_count]
src.process.parent.activeContent.hash
principal.labels[src_process_parent_active_content_hash]
(deprecated)
src.process.parent.activeContent.hash
additional.fields[src_process_parent_active_content_hash]
src.process.parent.activeContent.id
principal.labels[src_process_parent_active_content_id]
(deprecated)
src.process.parent.activeContent.id
additional.fields[src_process_parent_active_content_id]
src.process.parent.activeContent.path
principal.labels[src_process_parent_active_content_path]
(deprecated)
src.process.parent.activeContent.path
additional.fields[src_process_parent_active_content_path]
src.process.parent.activeContent.signedStatus
principal.labels[src_process_parent_active_content_signed_status]
(deprecated)
src.process.parent.activeContent.signedStatus
additional.fields[src_process_parent_active_content_signed_status]
src.process.parent.activeContentType
principal.labels[src_process_parent_active_content_type]
(deprecated)
src.process.parent.activeContentType
additional.fields[src_process_parent_active_content_type]
src.process.parent.displayName
principal.labels[src_process_parent_display_name]
(deprecated)
src.process.parent.displayName
additional.fields[src_process_parent_display_name]
src.process.parent.integrityLevel
principal.labels[src_process_parent_integrity_level]
(deprecated)
src.process.parent.integrityLevel
additional.fields[src_process_parent_integrity_level]
src.process.parent.isNative64Bit
principal.labels[src_process_parent_is_native_64_bit]
(deprecated)
src.process.parent.isNative64Bit
additional.fields[src_process_parent_is_native_64_bit]
src.process.parent.isRedirectCmdProcessor
principal.labels[src_process_parent_is_redirect_cmd_processor]
(deprecated)
src.process.parent.isRedirectCmdProcessor
additional.fields[src_process_parent_is_redirect_cmd_processor]
src.process.parent.isStorylineRoot
principal.labels[src_process_parent_is_storyline_root]
(deprecated)
src.process.parent.isStorylineRoot
additional.fields[src_process_parent_is_storyline_root]
src.process.parent.publisher
principal.labels[src_process_parent_publisher]
(deprecated)
src.process.parent.publisher
additional.fields[src_process_parent_publisher]
src.process.parent.reasonSignatureInvalid
principal.labels[src_process_parent_reason_signature_invalid]
(deprecated)
src.process.parent.reasonSignatureInvalid
additional.fields[src_process_parent_reason_signature_invalid]
src.process.parent.sessionId
principal.labels[src_process_parent_session_id]
(deprecated)
src.process.parent.sessionId
additional.fields[src_process_parent_session_id]
src.process.parent.signedStatus
principal.process.parent_process.file.signature_info.sigcheck.verification_message
src.process.parent.startTime
principal.labels[src_process_parent_start_time]
(deprecated)
src.process.parent.startTime
additional.fields[src_process_parent_start_time]
src.process.parent.subsystem
principal.labels[src_process_parent_subsystem]
(deprecated)
src.process.parent.subsystem
additional.fields[src_process_parent_subsystem]
src.process.publisher
principal.labels[src_process_publisher]
(deprecated)
src.process.publisher
additional.fields[src_process_publisher]
src.process.reasonSignatureInvalid
principal.labels[src_process_reason_signature_invalid]
(deprecated)
src.process.reasonSignatureInvalid
additional.fields[src_process_reason_signature_invalid]
src.process.registryChangeCount
principal.labels[src_process_registry_change_count]
(deprecated)
src.process.registryChangeCount
additional.fields[src_process_registry_change_count]
src.process.rpid
principal.labels[src_process_rpid]
(deprecated)
src.process.rpid
additional.fields[src_process_rpid]
src.process.sessionId
principal.labels[src_process_session_id]
(deprecated)
src.process.sessionId
additional.fields[src_process_session_id]
src.process.signedStatus
principal.process.file.signature_info.sigcheck.verification_message
src.process.startTime
principal.labels[src_process_start_time]
(deprecated)
src.process.startTime
additional.fields[src_process_start_time]
src.process.storyline.id
principal.labels[src_process_storyline_id]
(deprecated)
src.process.storyline.id
additional.fields[src_process_storyline_id]
src.process.subsystem
principal.labels[src_process_subsystem]
(deprecated)
src.process.subsystem
additional.fields[src_process_subsystem]
src.process.tgtFileCreationCount
principal.labels[src_process_tgt_file_creation_count]
(deprecated)
src.process.tgtFileCreationCount
additional.fields[src_process_tgt_file_creation_count]
src.process.tgtFileDeletionCount
principal.labels[src_process_tgt_file_deletion_count]
(deprecated)
src.process.tgtFileDeletionCount
additional.fields[src_process_tgt_file_deletion_count]
src.process.tgtFileModificationCount
principal.labels[src_process_tgt_file_modification_count]
(deprecated)
src.process.tgtFileModificationCount
additional.fields[src_process_tgt_file_modification_count]
src.process.tid
principal.labels[src_process_tid]
(deprecated)
src.process.tid
additional.fields[src_process_tid]
principal.process.product_specific_process_id
If the
src.process.uid
log field value is
not
empty, then the
SO:%{site.id}:%{account.id}:%{agent.uuid}:%{src.process.uid}
log field is mapped to the
principal.process.product_specific_process_id
UDM field.
src.process.verifiedStatus
principal.labels[src_process_verified_status]
(deprecated)
src.process.verifiedStatus
additional.fields[src_process_verified_status]
site.id
principal.labels[site_id]
(deprecated)
site.id
additional.fields[site_id]
principal.platform
If the
os.name
log field value matches the regular expression pattern
(?i)win
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
os.name
log field value matches the regular expression pattern
(?i)lin
, then the
principal.platform
UDM field is set to
LINUX
.
src.port.number
principal.port
osSrc.process.cmdline
principal.process_ancestors.command_line
osSrc.process.image.path
principal.process_ancestors.file.full_path
osSrc.process.image.md5
principal.process_ancestors.file.md5
If the
osSrc.process.image.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
osSrc.process.image.md5
log field is mapped to the
principal.process_ancestors.file.md5
UDM field.
osSrc.process.name
principal.process_ancestors.file.names
osSrc.process.image.sha1
principal.process_ancestors.file.sha1
If the
osSrc.process.image.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
osSrc.process.image.sha1
log field is mapped to the
principal.process_ancestors.file.sha1
UDM field.
osSrc.process.image.sha256
principal.process_ancestors.file.sha256
If the
osSrc.process.image.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
osSrc.process.image.sha256
log field is mapped to the
principal.process_ancestors.file.sha256
UDM field.
osSrc.process.parent.cmdline
principal.process_ancestors.parent_process.command_line
osSrc.process.parent.image.path
principal.process_ancestors.parent_process.file.full_path
osSrc.process.parent.image.md5
principal.process_ancestors.parent_process.file.md5
If the
osSrc.process.parent.image.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
osSrc.process.parent.image.md5
log field is mapped to the
principal.process_ancestors.parent_process.file.md5
UDM field.
osSrc.process.parent.name
principal.process_ancestors.parent_process.file.names
osSrc.process.parent.image.sha1
principal.process_ancestors.parent_process.file.sha1
If the
osSrc.process.parent.image.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
osSrc.process.parent.image.sha1
log field is mapped to the
principal.process_ancestors.parent_process.file.sha1
UDM field.
osSrc.process.parent.image.sha256
principal.process_ancestors.parent_process.file.sha256
If the
osSrc.process.parent.image.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
osSrc.process.parent.image.sha256
log field is mapped to the
principal.process_ancestors.parent_process.file.sha256
UDM field.
osSrc.process.parent.pid
principal.process_ancestors.parent_process.pid
osSrc.process.pid
principal.process_ancestors.pid
principal.process_ancestors.product_specific_process_id
If the
osSrc.process.uid
log field value is
not
empty, then the
SO:%{site.id}:%{account.id}:%{agent.uuid}:%{osSrc.process.uid}
log field is mapped to the
principal.process_ancestors.product_specific_process_id
UDM field.
src.process.cmdline
principal.process.command_line
src.process.image.path
principal.process.file.full_path
src.process.image.md5
principal.process.file.md5
If the
src.process.image.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
src.process.image.md5
log field is mapped to the
principal.process.file.md5
UDM field.
src.process.name
principal.process.file.names
src.process.image.sha1
principal.process.file.sha1
If the
src.process.image.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
src.process.image.sha1
log field is mapped to the
principal.process.file.sha1
UDM field.
src.process.image.sha256
principal.process.file.sha256
If the
src.process.image.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
src.process.image.sha256
log field is mapped to the
principal.process.file.sha256
UDM field.
src.process.parent.cmdline
principal.process.parent_process.command_line
src.process.parent.image.md5
principal.process.parent_process.file.md5
If the
src.process.parent.image.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
src.process.parent.image.md5
log field is mapped to the
principal.process.parent_process.file.md5
UDM field.
src.process.parent.image.path
principal.process.parent_process.file.full_path
src.process.parent.name
principal.process.parent_process.file.names
src.process.parent.image.sha1
principal.process.parent_process.file.sha1
If the
src.process.parent.image.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
src.process.parent.image.sha1
log field is mapped to the
principal.process.parent_process.file.sha1
UDM field.
src.process.parent.image.sha256
principal.process.parent_process.file.sha256
If the
src.process.parent.image.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
src.process.parent.image.sha256
log field is mapped to the
principal.process.parent_process.file.sha256
UDM field.
src.process.parent.pid
principal.process.parent_process.pid
principal.process_ancestors.parent_process.product_specific_process_id
If the
osSrc.process.parent.uid
log field value is
not
empty, then the
SO:%{site.id}:%{account.id}:%{agent.uuid}:%{osSrc.process.parent.uid}
log field is mapped to the
principal.process_ancestors.parent_process.product_specific_process_id
UDM field.
principal.process.parent_process.product_specific_process_id
If the
src.process.parent.uid
log field value is
not
empty, then the
SO:%{site.id}:%{account.id}:%{agent.uuid}:%{src.process.parent.uid}
log field is mapped to the
principal.process.parent_process.product_specific_process_id
UDM field.
src.process.pid
principal.process.pid
osSrc.process.user
principal.user.attribute.labels[os_src_process_user]
src.process.eUserUid
principal.user.attribute.labels[src_process_e_user_uid]
src.process.lUserName
principal.user.attribute.labels[src_process_l_user_name]
src.process.parent.eUserUid
principal.user.attribute.labels[src_process_parent_e_user_uid]
src.process.parent.lUserUid
principal.user.attribute.labels[src_process_parent_l_user_uid]
src.process.parent.rUserUid
principal.user.attribute.labels[src_process_parent_r_user_uid]
src.process.rUserName
principal.user.attribute.labels[src_process_r_user_name]
src.process.rUserUid
principal.user.attribute.labels[src_process_r_user_uid]
src.process.eUserName
principal.user.attribute.labels[src_process_e_user_name]
src.process.parent.eUserName
principal.user.attribute.labels[src_process_parent_e_user_name]
src.process.parent.lUserName
principal.user.attribute.labels[src_process_parent_l_user_name]
src.process.parent.rUserName
principal.user.attribute.labels[src_process_parent_r_user_name]
osSrc.process.parent.user
principal.user.attribute.labels[os_src_process_parent_user]
src.process.parent.user
principal.user.attribute.labels[src_process_parent_user]
src.process.user
principal.user.userid
tiIndicator.value
security_result.about.file.md5
If the
tiIndicator.type
log field value is equal to
Md5
, then the
tiIndicator.value
log field is mapped to the
security_result.about.file.md5
UDM field.
tiIndicator.value
security_result.about.file.sha1
If the
tiIndicator.type
log field value is equal to
Sha1
, then the
tiIndicator.value
log field is mapped to the
security_result.about.file.sha1
UDM field.
tiIndicator.value
security_result.about.ip
If the
tiIndicator.type
log field value contain one of the following values, then the
tiIndicator.value
log field is mapped to the
security_result.about.ip
UDM field.
IPv4
IPV6
tiIndicator.value
security_result.about.labels[tiIndicator.value]
(deprecated)
If the
tiIndicator.type
log field value does not contain one of the following values, then the
tiIndicator.value
log field is mapped to the
security_result.about.labels
UDM field.
Md5
Sha1
IPV4
IPV6
DNS
URL
tiIndicator.value
additional.fields[tiIndicator.value]
If the
tiIndicator.type
log field value does not contain one of the following values, then the
tiIndicator.value
log field is mapped to the
additional.fields
UDM field.
Md5
Sha1
IPV4
IPV6
DNS
URL
tiIndicator.value
network.dns.questions.name
If the
tiIndicator.type
log field value is equal to
DNS
, then the
tiIndicator.value
log field is mapped to the
network.dns.questions.name
UDM field.
tiIndicator.value
security_result.about.url
If the
tiIndicator.type
log field value is equal to
URL
, then the
tiIndicator.value
log field is mapped to the
security_result.about.url
UDM field.
winEventLog.providerName
security_result.about.resource.attribute.labels[win_event_log_provider_name]
tiIndicator.addedBy
security_result.about.user.email_addresses
tiIndicator.threatActors
security_result.about.user.email_addresses
security_result.action
If the
event.login.loginIsSuccessful
log field value is equal to
true
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
event.login.loginIsSuccessful
log field value is equal to
false
, then the
security_result.action
UDM field is set to
BLOCK
.
If the
event.network.connectionStatus
log field value is equal to
SUCCESS
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
event.network.connectionStatus
log field value is equal to
FAILURE
, then the
security_result.action
UDM field is set to
FAIL
.
Else, if the
event.network.connectionStatus
log field value is equal to
BLOCKED
, then the
security_result.action
UDM field is set to
BLOCK
.
event.network.connectionStatus
security_result.action_details
tiIndicator.mitreTactics
security_result.attack_details.tactics.name
security_result.category
If the
indicator.category
log field value contain one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
malicious
Ransomware
OSX.Malware
Linux.Malware
Malware
Manual
Else, if the
indicator.category
log field value contain one of the following values, then the
security_result.category
UDM field is set to
NETWORK_SUSPICIOUS
.
Lateral Movement
Remote shell
Else, if the
indicator.category
log field value contain one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_SUSPICIOUS
.
miner
Trojan
Virus
Malicious Office Document
Malicious PDF
Worm
Rootkit
Infostealer
Generic.Heuristic
Downloader
Backdoor
Hacktool
Browser
Dialer
Installer
Packed
Network
Spyware
Interactive shell
Else, if the
indicator.category
log field value contain one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_PUA
.
Adware
PUA
Else, if the
indicator.category
log field value is equal to
Exploit
, then the
security_result.category
UDM field is set to
EXPLOIT
.
security_result.category
If the
tiIndicator.categories
log field value matches the regular expression pattern
malware
, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
indicator.category
security_result.category_details
tiIndicator.categories
security_result.category_details
indicator.description
security_result.description
event.login.failureReason
security_result.description
tiIndicator.description
security_result.descripton
indicator.metadata
security_result.detection_fields [indicator_metadata]
indicator.name
security_result.detection_fields [indicator_name]
tiIndicator.comparisonMethod
security_result.detection_fields [ti_indicator_comparison_method]
tiIndicator.creationTime
security_result.detection_fields [ti_indicator_creation_time]
tiIndicator.externalId
security_result.detection_fields [ti_indicator_external_id]
tiIndicator.metadata
security_result.detection_fields [ti_indicator_metadata]
tiIndicator.modificationTime
security_result.detection_fields [ti_indicator_modification_time]
tiindicator.originalEvent.id
security_result.detection_fields [ti_indicator_original_event_id]
tiindicator.originalEvent.index
security_result.detection_fields [ti_indicator_original_event_index]
tiindicator.originalEvent.time
security_result.detection_fields [ti_indicator_original_event_time]
tiindicator.originalEvent.traceId
security_result.detection_fields [ti_indicator_original_event_trace_id]
tiIndicator.references
security_result.detection_fields [ti_indicator_references]
tiIndicator.intrusionSets
security_result.detection_fields [ti_indicator_tiIndicator_intrusion_sets]
tiIndicator.type
security_result.detection_fields [ti_indicator_type]
tiIndicator.uid
security_result.detection_fields [ti_indicator_uid]
tiIndicator.uploadTime
security_result.detection_fields [ti_indicator_upload_time]
tiIndicator.validUntil
security_result.detection_fields [ti_indicator_valid_until]
osSrc.process.parent.reasonSignatureInvalid
security_result.detection_fields[os_src_process_parent_reason_signature_invalid]
osSrc.process.reasonSignatureInvalid
security_result.detection_fields[os_src_process_reason_signature_invalid]
tgt.process.reasonSignatureInvalid
security_result.detection_fields[tgt_process_reason_signature_invalid]
security_result.severity
If the
winEventLog.level
log field value matches the regular expression pattern
^(INFO|Informational|Information|Normal|NOTICE)$
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
winEventLog.level
log field value contain one of the following values, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Warning
DEBUG
Else, if the
winEventLog.level
log field value matches the regular expression pattern
Error
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
winEventLog.level
log field value matches the regular expression pattern
Critical
, then the
security_result.severity
UDM field is set to
CRITICAL
.
winEventLog.level
security_result.severity_details
tiIndicator.name
security_result.threat_name
tiIndicator.source
security_result.threat_feed_name
tgt.file.oldPath
src.file.full_path
tgt.file.oldMd5
src.file.md5
If the
tgt.file.oldMd5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
tgt.file.oldMd5
log field is mapped to the
src.file.md5
UDM field.
driver.peSha1
target.process.file.sha1
If the
driver.peSha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
driver.peSha1
log field is mapped to the
target.process.file.sha1
UDM field.
tgt.file.oldSha1
src.file.sha1
If the
tgt.file.oldSha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
tgt.file.oldSha1
log field is mapped to the
src.file.sha1
UDM field.
driver.peSha256
target.process.file.sha256
If the
driver.peSha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
driver.peSha256
log field is mapped to the
target.process.file.sha256
UDM field.
tgt.file.oldSha256
src.file.sha256
If the
tgt.file.oldSha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
tgt.file.oldSha256
log field is mapped to the
src.file.sha256
UDM field.
driver.certificate.thumbprintAlgorithm
target.labels[driver_certificate_thumbprint_algorithm]
(deprecated)
driver.certificate.thumbprintAlgorithm
additional.fields[driver_certificate_thumbprint_algorithm]
driver.certificate.thumbprint
target.labels[driver_certificate_thumbprint]
(deprecated)
driver.certificate.thumbprint
additional.fields[driver_certificate_thumbprint]
driver.isLoadedBeforeMonitor
target.labels[driver_is_loaded_before_monitor]
(deprecated)
driver.isLoadedBeforeMonitor
additional.fields[driver_is_loaded_before_monitor]
driver.loadVerdict
target.labels[driver_load_verdict]
(deprecated)
driver.loadVerdict
additional.fields[driver_load_verdict]
driver.startType
target.labels[driver_start_type]
(deprecated)
driver.startType
additional.fields[driver_start_type]
registry.oldValueFullSize
src.labels[registry_old_value_full_size]
(deprecated)
registry.oldValueFullSize
additional.fields[registry_old_value_full_size]
registry.oldValueIsComplete
src.labels[registry_old_valueIs_complete]
(deprecated)
registry.oldValueIsComplete
additional.fields[registry_old_valueIs_complete]
registry.oldValue
src.registry.registry_value_data
registry.oldValueType
src.registry.registry_value_name
tgt.file.location
target.labels[tgt_file_location]
(deprecated)
tgt.file.location
additional.fields[tgt_file_location]
cmdScript.applicationName
target.application
event.login.accountDomain
target.domain.name
tgt.file.path
target.file.full_path
tgt.file.modificationTime
target.file.last_modification_time
tgt.file.md5
target.file.md5
If the
tgt.file.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
tgt.file.md5
log field is mapped to the
target.file.md5
UDM field.
tgt.file.extension
target.file.mime_type
tgt.file.id
target.file.names
tgt.file.internalName
target.file.names
tgt.file.sha1
target.file.sha1
If the
tgt.file.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
tgt.file.sha1
log field is mapped to the
target.file.sha1
UDM field.
tgt.file.sha256
target.file.sha256
If the
tgt.file.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
tgt.file.sha256
log field is mapped to the
target.file.sha256
UDM field.
tgt.file.size
target.file.size
target.file.file_type
If the
tgt.file.type
log field value is equal to
PE
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PE_EXE
.
Else, if the
tgt.file.type
log field value is equal to
ELF
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ELF
.
Else, if the
tgt.file.type
log field value is equal to
MACH
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACH_O
.
Else, if the
tgt.file.type
log field value is equal to
PDF
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PDF
.
Else, if the
tgt.file.type
log field value is equal to
COM
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOS_COM
.
Else, if the
tgt.file.type
log field value is equal to
COM
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOS_COM
.
Else, if the
tgt.file.type
log field value is equal to
OPENXML
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XML
.
Else, if the
tgt.file.type
log field value is equal to
PKZIP
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZIP
.
Else, if the
tgt.file.type
log field value is equal to
RAR
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RAR
.
Else, if the
tgt.file.type
log field value is equal to
BZIP2
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BZIP
.
Else, if the
tgt.file.type
log field value is equal to
TAR
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TAR
.
Else, if the
tgt.file.type
log field value is equal to
LNK
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LNK
.
url.address
target.hostname
The
protocol
and
hostname
field is extracted from
url.address
log field using the Grok pattern, and the
hostname
extracted field is mapped to the
target.hostname
UDM field.
url.address
target.asset.hostname
The
protocol
and
hostname
field is extracted from
url.address
log field using the Grok pattern, and the
hostname
extracted field is mapped to the
target.hostname
UDM field.
dst.ip.address
target.ip
cmdScript.isComplete
target.labels[cmd_script_is_complete]
(deprecated)
cmdScript.isComplete
additional.fields[cmd_script_is_complete]
registry.keyUid
target.labels[registry_key_uid]
(deprecated)
registry.keyUid
additional.fields[registry_key_uid]
registry.valueFullSize
target.labels[registry_value_full_size]
(deprecated)
registry.valueFullSize
additional.fields[registry_value_full_size]
registry.valueIsComplete
target.labels[registry_value_is_complete]
(deprecated)
registry.valueIsComplete
additional.fields[registry_value_is_complete]
tgt.file.convictedBy
target.labels[tgt_file_convicted_by]
(deprecated)
tgt.file.convictedBy
additional.fields[tgt_file_convicted_by]
tgt.file.creationTime
target.labels[tgt_file_creation_time]
(deprecated)
tgt.file.creationTime
additional.fields[tgt_file_creation_time]
tgt.file.description
target.labels[tgt_file_description]
(deprecated)
tgt.file.description
additional.fields[tgt_file_description]
tgt.file.isExecutable
target.labels[tgt_file_is_executable]
(deprecated)
tgt.file.isExecutable
additional.fields[tgt_file_is_executable]
tgt.file.isSigned
target.labels[tgt_file_is_signed]
(deprecated)
tgt.file.isSigned
additional.fields[tgt_file_is_signed]
tgt.process.accessRights
target.labels[tgt_process_access_rights]
(deprecated)
tgt.process.accessRights
additional.fields[tgt_process_access_rights]
tgt.process.activeContent.hash
target.labels[tgt_process_active_content_hash]
(deprecated)
tgt.process.activeContent.hash
additional.fields[tgt_process_active_content_hash]
tgt.process.activeContent.id
target.labels[tgt_process_active_content_id]
(deprecated)
tgt.process.activeContent.id
additional.fields[tgt_process_active_content_id]
tgt.process.activeContent.path
target.labels[tgt_process_active_content_path]
(deprecated)
tgt.process.activeContent.path
additional.fields[tgt_process_active_content_path]
tgt.process.activeContent.signedStatus
target.labels [tgt_process_active_content_signed_status]
(deprecated)
tgt.process.activeContent.signedStatus
additional.fields [tgt_process_active_content_signed_status]
tgt.process.activeContentType
target.labels[tgt_process_active_content_type]
(deprecated)
tgt.process.activeContentType
additional.fields[tgt_process_active_content_type]
tgt.process.displayName
target.labels[tgt_process_display_name]
(deprecated)
tgt.process.displayName
additional.fields[tgt_process_display_name]
tgt.process.image.binaryIsExecutable
target.labels[tgt_process_image_binary_is_executable]
(deprecated)
tgt.process.image.binaryIsExecutable
additional.fields[tgt_process_image_binary_is_executable]
tgt.process.integrityLevel
target.labels[tgt_process_integrity_level]
(deprecated)
tgt.process.integrityLevel
additional.fields[tgt_process_integrity_level]
tgt.process.isNative64Bit
target.labels[tgt_process_is_native_64_bit]
(deprecated)
tgt.process.isNative64Bit
additional.fields[tgt_process_is_native_64_bit]
tgt.process.isRedirectCmdProcessor
target.labels[tgt_process_is_redirect_cmd_processor]
(deprecated)
tgt.process.isRedirectCmdProcessor
additional.fields[tgt_process_is_redirect_cmd_processor]
tgt.process.isStorylineRoot
target.labels[tgt_process_is_storyline_root]
(deprecated)
tgt.process.isStorylineRoot
additional.fields[tgt_process_is_storyline_root]
tgt.process.publisher
target.labels[tgt_process_publisher]
(deprecated)
tgt.process.publisher
additional.fields[tgt_process_publisher]
tgt.process.relation
target.labels[tgt_process_relation]
(deprecated)
tgt.process.relation
additional.fields[tgt_process_relation]
tgt.process.sessionId
target.labels[tgt_process_session_id]
(deprecated)
tgt.process.sessionId
additional.fields[tgt_process_session_id]
tgt.process.signedStatus
target.process.file.signature_info.sigcheck.verification_message
tgt.process.startTime
target.labels[tgt_process_start_time]
(deprecated)
tgt.process.startTime
additional.fields[tgt_process_start_time]
tgt.process.storyline.id
target.labels[tgt_process_storyline_id]
(deprecated)
tgt.process.storyline.id
additional.fields[tgt_process_storyline_id]
tgt.process.subsystem
target.labels[tgt_process_subsystem]
(deprecated)
tgt.process.subsystem
additional.fields[tgt_process_subsystem]
tgt.process.verifiedStatus
target.labels[tgt_process_verified_status]
(deprecated)
tgt.process.verifiedStatus
additional.fields[tgt_process_verified_status]
dst.port.number
target.port
cmdScript.content
target.process.command_line
tgt.process.cmdline
target.process.command_line
tgt.process.image.path
target.process.file.full_path
tgt.process.image.md5
target.process.file.md5
If the
tgt.process.image.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
tgt.process.image.md5
log field is mapped to the
target.process.file.md5
UDM field.
tgt.process.name
target.process.file.names
tgt.process.image.sha1
target.process.file.sha1
If the
tgt.process.image.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
tgt.process.image.sha1
log field is mapped to the
target.process.file.sha1
UDM field.
cmdScript.sha256
target.process.file.sha256
If the
cmdScript.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
cmdScript.sha256
log field is mapped to the
target.process.file.sha256
UDM field.
tgt.process.image.sha256
target.process.file.sha256
If the
tgt.process.image.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
tgt.process.image.sha256
log field is mapped to the
target.process.file.sha256
UDM field.
cmdScript.originalSize
target.process.file.size
tgt.process.pid
target.process.pid
target.process.product_specific_process_id
If the
tgt.process.uid
log field value is
not
empty, then the
SO:%{site.id}:%{account.id}:%{agent.uuid}:%{tgt.process.uid}
log field is mapped to the
target.process.product_specific_process_id
UDM field.
registry.keyPath
target.registry.registry_key
registry.value
target.registry.registry_value_data
registry.valueType
target.registry.registry_value_name
k8sCluster.namespaceLabels
target.resource_ancestors.attribute.labels[k8s_cluster_namespace_labels]
k8sCluster.namespace
target.resource_ancestors.attribute.labels[k8s_cluster_namespace]
k8sCluster.name
target.resource_ancestors.name
target.resource_ancestors.resource_type
If the
k8sCluster.name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
k8sCluster.controllerName
target.resource_ancestors.name
k8sCluster.controllerLabels
target.resource_ancestors.attribute.labels[k8s_cluster_controller_labels]
target.resource_ancestors.resource_type
If the
k8sCluster.controllerName
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
k8sCluster.controllerType
target.resource_ancestors.resource_subtype
k8sCluster.podName
target.resource_ancestors.name
k8sCluster.podLabels
target.resource_ancestors.attribute.labels[k8s_cluster_pod_labels]
target.resource_ancestors.resource_type
If the
k8sCluster.podName
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
POD
.
k8sCluster.nodeName
target.resource_ancestors.name
target.resource_ancestors.resource_type
If the
k8sCluster.nodeName
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
target.resource_ancestors.resource_subtype
If the
k8sCluster.nodeName
log field value is
not
empty, then the
target.resource_ancestors.resource_subtype
UDM field is set to
NODE
.
k8sCluster.containerName
target.resource.name
k8sCluster.containerId
target.resource.product_object_id
target.resource.resource_type
If the
k8sCluster.containerName
log field value is
not
empty or the
k8sCluster.containerId
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
CONTAINER
.
k8sCluster.containerImage.sha256
target.resource.attribute.labels[k8s_cluster_container_image_sha256]
k8sCluster.containerImage
target.resource.attribute.labels[k8s_cluster_container_image]
k8sCluster.containerLabels
target.resource.attribute.labels[k8s_cluster_container_labels]
namedPipe.name
target.resource.name
namedPipe.accessMode
target.resource.attribute.permission.name
namedPipe.connectionType
target.resource.attribute.labels[named_pipe_connection_type]
namedPipe.isFirstInstance
target.resource.attribute.labels[named_pipe_is_first_instance]
namedPipe.isOverlapped
target.resource.attribute.labels[named_pipe_is_overlapped]
namedPipe.isWriteThrough
target.resource.attribute.labels[named_pipe_is_write_through]
namedPipe.maxInstances
target.resource.attribute.labels[named_pipe_max_instances]
namedPipe.readMode
target.resource.attribute.labels[named_pipe_read_mode]
namedPipe.remoteClients
target.resource.attribute.labels[named_pipe_remote_clients]
namedPipe.securityGroups
target.resource.attribute.labels[named_pipe_security_groups]
namedPipe.securityOwner
target.resource.attribute.labels[named_pipe_security_owner]
namedPipe.typeMode
target.resource.attribute.labels[named_pipe_type_mode]
namedPipe.waitMode
target.resource.attribute.labels[named_pipe_wait_mode]
task.name
target.resource.name
task.path
target.resource.attribute.labels[task_path]
target.resource.resource_type
If the
event.category
log field value is equal to
scheduled_task
, then the
target.resource.resource_type
UDM field is set to
TASK
.
If the
event.type
log field value contain one of the following values, then the
target.resource.resource_type
UDM field is set to
PIPE
.
Named Pipe Creation
Named Pipe Connection
url.address
target.url
tgt.process.eUserName
target.user.attribute.labels[tgt_process_e_user_name]
tgt.process.eUserUid
target.user.attribute.labels[tgt_process_e_user_uid]
tgt.process.lUserName
target.user.attribute.labels[tgt_process_l_user_name]
tgt.process.lUserUid
target.user.attribute.labels[tgt_process_l_user_uid]
tgt.process.rUserName
target.user.attribute.labels[tgt_process_r_user_name]
tgt.process.rUserUid
target.user.attribute.labels[tgt_process_r_user_uid]
tgt.process.user
target.user.userid
event.login.accountName
target.user.user_display_name
target.user.user_role
If the
event.login.isAdministratorEquivalent
log field value is equal to
true
, then the
target.user.user_role
UDM field is set to
ADMINISTRATOR
.
event.login.userName
target.user.userid
event.login.accountSid
target.user.windows_sid
module.path
target.process.file.full_path
module.md5
target.process.file.md5
If the
module.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
module.md5
log field is mapped to the
target.process.file.md5
UDM field.
module.sha1
target.process.file.sha1
If the
module.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
module.sha1
log field is mapped to the
target.process.file.sha1
UDM field.
mgmt.url
about.url
dataSource.category
about.labels[data_source_category]
(deprecated)
dataSource.category
additional.fields[data_source_category]
dataSource.name
about.labels[data_source_name]
(deprecated)
dataSource.name
additional.fields[data_source_name]
dataSource.vendor
about.labels[data_source_vendor]
(deprecated)
dataSource.vendor
additional.fields[data_source_vendor]
event.category
about.labels[event_category]
(deprecated)
event.category
additional.fields[event_category]
event.login.baseType
about.labels[event_login_base_type]
(deprecated)
event.login.baseType
additional.fields[event_login_base_type]
event.network.protocolName
about.labels[event_network_protocol_name]
(deprecated)
event.network.protocolName
additional.fields[event_network_protocol_name]
event.repetitionCount
about.labels[event_repetition_count]
(deprecated)
event.repetitionCount
additional.fields[event_repetition_count]
event.login.isAdministratorEquivalent
about.labels[event_login_is_administrator_equivalent]
(deprecated)
event.login.isAdministratorEquivalent
additional.fields[event_login_is_administrator_equivalent]
group.id
about.labels[group_id]
(deprecated)
If the
event.type
log field value is equal to
Group Creation
, then the
group.id
log field is mapped to the
target.group.product_object_id
UDM field.
Else, the
group.id
log field is mapped to the
about.labels
UDM field.
group.id
additional.fields[group_id]
If the
event.type
log field value is equal to
Group Creation
, then the
group.id
log field is mapped to the
target.group.product_object_id
UDM field.
Else, the
group.id
log field is mapped to the
additional.fields
UDM field.
i.scheme
about.labels[i_scheme]
(deprecated)
i.scheme
additional.fields[i_scheme]
i.version
about.labels[i_version]
(deprecated)
i.version
additional.fields[i_version]
meta.event.name
about.labels[meta_event_name]
(deprecated)
meta.event.name
additional.fields[meta_event_name]
mgmt.id
about.labels[mgmt_id]
(deprecated)
mgmt.id
additional.fields[mgmt_id]
mgmt.osRevision
about.labels[mgmt_os_revision]
(deprecated)
mgmt.osRevision
additional.fields[mgmt_os_revision]
packet.id
about.labels[packet_id]
(deprecated)
packet.id
additional.fields[packet_id]
sca:atlantisIngestTime
about.labels[sca_atlantis_ingest_time]
(deprecated)
sca:atlantisIngestTime
additional.fields[sca_atlantis_ingest_time]
sca:ingestTime
about.labels[sca_ingest_time]
(deprecated)
sca:ingestTime
additional.fields[sca_ingest_time]
timestamp
about.labels[timestamp]
(deprecated)
timestamp
additional.fields[timestamp]
trace.id
about.labels[trace_id]
(deprecated)
trace.id
additional.fields[trace_id]
winEventLog.channel
about.labels[win_event_log_channel]
(deprecated)
winEventLog.channel
additional.fields[win_event_log_channel]
winEventLog.description.additionalInformation
about.labels[win_event_log_description_additional_information]
(deprecated)
winEventLog.description.additionalInformation
additional.fields[win_event_log_description_additional_information]
winEventLog.description.objectName
about.labels[win_event_log_description_object_name]
(deprecated)
winEventLog.description.objectName
additional.fields[win_event_log_description_object_name]
winEventLog.description.objectServer
about.labels[win_event_log_description_object_server]
(deprecated)
winEventLog.description.objectServer
additional.fields[win_event_log_description_object_server]
winEventLog.description.objectType
about.labels[win_event_log_description_object_type]
(deprecated)
winEventLog.description.objectType
additional.fields[win_event_log_description_object_type]
winEventLog.description.operationType
about.labels[win_event_log_description_operation_type]
(deprecated)
winEventLog.description.operationType
additional.fields[win_event_log_description_operation_type]
winEventLog.description.securityId
about.labels[win_event_log_description_security_id]
(deprecated)
winEventLog.description.securityId
additional.fields[win_event_log_description_security_id]
winEventLog.description.userId
about.labels[win_event_log_description_user_id]
(deprecated)
winEventLog.description.userId
additional.fields[win_event_log_description_user_id]
winEventLog.xml
about.labels[win_event_log_xml]
(deprecated)
winEventLog.xml
additional.fields[win_event_log_xml]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
