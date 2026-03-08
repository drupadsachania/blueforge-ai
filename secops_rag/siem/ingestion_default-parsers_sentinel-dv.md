# Collect SentinelOne Deep Visibility logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-dv/  
**Scraped:** 2026-03-05T09:28:06.321355Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect SentinelOne Deep Visibility logs
Supported in:
Google secops
SIEM
This document explains how to export SentinelOne Deep Visibility logs to Google Security Operations using Cloud Funnel for exporting logs to Google Cloud Storage. The parser transforms raw JSON formatted security event logs into a structured format conforming to the UDM. It first initializes a set of variables, then extracts the event type and parses the JSON payload, mapping relevant fields to the UDM schema while handling Windows event logs separately.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to Google Cloud
SentinelOne Deep Visibility set up in your environment
Privileged access to SentinelOne
Create a Google Cloud Storage Bucket
Sign in to the
Google Cloud console
.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
On the
Create a bucket
page, enter your bucket information. After each of the following steps, click
Continue
to proceed to the next step:
In the
Get started
section, do the following:
Enter a unique name that meets the bucket name requirements; for example,
sentinelone-deepvisibility
.
To enable hierarchical namespace, click the expander arrow to expand the
Optimize for file oriented and data-intensive workloads
section, and then select
Enable Hierarchical namespace on this bucket
.
To add a bucket label, click the expander arrow to expand the
Labels
section.
Click
Add label
, and specify a key and a value for your label.
In the
Choose where to store your data
section, do the following:
Select a
Location type
.
Use the location type menu to select a
Location
where object data within your bucket will be permanently stored.
To set up cross-bucket replication, expand the
Set up cross-bucket replication
section.
In the
Choose a storage class for your data
section, either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management of your bucket's data.
In the
Choose how to control access to objects
section, select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the expander arrow labeled
Data encryption
, and select a
Data encryption method
.
Click
Create
.
Create a Google Cloud Service Account
Go to
IAM & Admin
>
Service Accounts
.
Create a new service account.
Give it a descriptive name; for example,
sentinelone-dv-logs
.
Grant the service account with
Storage Object Creator
role on the Cloud Storage bucket you created in the previous step.
Create an
SSH key
for the service account.
Download a JSON key file for the service account. Keep this file secure.
How to configure Cloud Funnel in SentinelOne DeepVisibility
Sign in to the
SentinelOne DeepVisibility
.
Click
Configure
>
Policy & Settings
.
In the
Singularity Data Lake
section, click
Cloud Funnel
.
Provide the following configuration details:
Cloud Provider
: Select Google Cloud.
Bucket Name
: Enter the name of the Cloud Storage bucket that you created for SentinelOne DeepVisibility log ingestion.
Telemetry Streaming
: Select
Enable
.
Query Filters
: Create a query that includes the agents that need to send data to a Cloud Storage bucket.
Click
Validate
.
Fields to include
: Select all fields.
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
How to set up the SentinelOne Deep Visibility feed
Click the
SentinelOne
pack.
In the
SentinelOne Deep Visibility
log type, specify the values for 
the following fields:
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
UDM Mapping Table
Log field
UDM mapping
Logic
AdapterName
security_result.about.resource.attribute.labels.value
The value is taken from the 'AdapterName' field in the raw log.
AdapterSuffixName
security_result.about.resource.attribute.labels.value
The value is taken from the 'AdapterSuffixName' field in the raw log.
agent_version
read_only_udm.metadata.product_version
The value is taken from the 'meta.agent_version' field in the raw log.
Channel
security_result.about.resource.attribute.labels.value
The value is taken from the 'Channel' field in the raw log.
commandLine
read_only_udm.principal.process.command_line
The value is taken from the 'event.Event.
.
.commandLine' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
computer_name
read_only_udm.principal.hostname
The value is taken from the 'meta.computer_name' field in the raw log.
destinationAddress.address
read_only_udm.target.ip
The value is taken from the 'event.Event.Tcpv4.destinationAddress.address' field in the raw log.
destinationAddress.port
read_only_udm.target.port
The value is taken from the 'event.Event.Tcpv4.destinationAddress.port' field in the raw log.
DnsServerList
read_only_udm.principal.ip
The value is taken from the 'DnsServerList' field in the raw log.
ErrorCode_new
security_result.detection_fields.value
The value is taken from the 'ErrorCode_new' field in the raw log.
EventID
security_result.about.resource.attribute.labels.value
The value is taken from the 'EventID' field in the raw log.
event.Event.Dns.query
read_only_udm.network.dns.questions.name
The value is taken from the 'event.Event.Dns.query' field in the raw log.
event.Event.Dns.results
read_only_udm.network.dns.answers.data
The value is taken from the 'event.Event.Dns.results' field in the raw log.
event.Event.Dns.source.fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.Dns.source.fullPid.pid' field in the raw log.
event.Event.Dns.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.Dns.source.user.name' field in the raw log.
event.Event.FileCreation.source.fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.FileCreation.source.fullPid.pid' field in the raw log.
event.Event.FileCreation.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.FileCreation.source.user.name' field in the raw log.
event.Event.FileCreation.targetFile.path
read_only_udm.target.file.full_path
The value is taken from the 'event.Event.FileCreation.targetFile.path' field in the raw log.
event.Event.FileDeletion.source.fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.FileDeletion.source.fullPid.pid' field in the raw log.
event.Event.FileDeletion.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.FileDeletion.source.user.name' field in the raw log.
event.Event.FileDeletion.targetFile.path
read_only_udm.target.file.full_path
The value is taken from the 'event.Event.FileDeletion.targetFile.path' field in the raw log.
event.Event.FileModification.file.path
read_only_udm.target.file.full_path
The value is taken from the 'event.Event.FileModification.file.path' field in the raw log.
event.Event.FileModification.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.FileModification.source.user.name' field in the raw log.
event.Event.FileModification.targetFile.path
read_only_udm.target.file.full_path
The value is taken from the 'event.Event.FileModification.targetFile.path' field in the raw log.
event.Event.Http.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.Http.source.user.name' field in the raw log.
event.Event.Http.url
read_only_udm.target.url
The value is taken from the 'event.Event.Http.url' field in the raw log.
event.Event.ProcessCreation.process.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.ProcessCreation.process.user.name' field in the raw log.
event.Event.ProcessCreation.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.ProcessCreation.source.user.name' field in the raw log.
event.Event.ProcessExit.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.ProcessExit.source.user.name' field in the raw log.
event.Event.ProcessTermination.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.ProcessTermination.source.user.name' field in the raw log.
event.Event.RegKeyCreate.source.fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.RegKeyCreate.source.fullPid.pid' field in the raw log.
event.Event.RegKeyCreate.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.RegKeyCreate.source.user.name' field in the raw log.
event.Event.RegKeyDelete.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.RegKeyDelete.source.user.name' field in the raw log.
event.Event.RegValueModified.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.RegValueModified.source.user.name' field in the raw log.
event.Event.SchedTaskDelete.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.SchedTaskDelete.source.user.name' field in the raw log.
event.Event.SchedTaskRegister.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.SchedTaskRegister.source.user.name' field in the raw log.
event.Event.SchedTaskStart.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.SchedTaskStart.source.user.name' field in the raw log.
event.Event.SchedTaskTrigger.source.fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.SchedTaskTrigger.source.fullPid.pid' field in the raw log.
event.Event.SchedTaskTrigger.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.SchedTaskTrigger.source.user.name' field in the raw log.
event.Event.Tcpv4.source.fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.Tcpv4.source.fullPid.pid' field in the raw log.
event.Event.Tcpv4.source.user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.Tcpv4.source.user.name' field in the raw log.
event.Event.Tcpv4Listen.local.address
read_only_udm.principal.ip
The value is taken from the 'event.Event.Tcpv4Listen.local.address' field in the raw log.
event.timestamp.millisecondsSinceEpoch
read_only_udm.metadata.event_timestamp.seconds
The value is taken from the 'event.timestamp.millisecondsSinceEpoch' field in the raw log, converted to seconds.
event.timestamp.millisecondsSinceEpoch
read_only_udm.metadata.event_timestamp.nanos
The value is taken from the 'event.timestamp.millisecondsSinceEpoch' field in the raw log, converted to nanoseconds.
event.timestamp.millisecondsSinceEpoch
security_result.about.resource.attribute.labels.value
The value is taken from the 'event.timestamp.millisecondsSinceEpoch' field in the raw log and used as the value for a label in the security_result.about.resource.attribute.labels array.
event_type
read_only_udm.metadata.product_event_type
The value is extracted from the 'message' field in the raw log using a grok pattern.
executable.hashes.md5
read_only_udm.principal.process.file.md5
The value is taken from the 'event.Event.
.
.executable.hashes.md5' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
executable.hashes.sha1
read_only_udm.principal.process.file.sha1
The value is taken from the 'event.Event.
.
.executable.hashes.sha1' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
executable.hashes.sha256
read_only_udm.principal.process.file.sha256
The value is taken from the 'event.Event.
.
.executable.hashes.sha256' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
executable.path
read_only_udm.principal.process.file.full_path
The value is taken from the 'event.Event.
.
.executable.path' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
executable.sizeBytes
read_only_udm.principal.process.file.size
The value is taken from the 'event.Event.
.
.executable.sizeBytes' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
fullPid.pid
read_only_udm.principal.process.pid
The value is taken from the 'event.Event.
.
.fullPid.pid' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
hashes.md5
read_only_udm.target.file.md5
The value is taken from the 'event.Event.ProcessCreation.hashes.md5' field in the raw log.
hashes.sha1
read_only_udm.target.file.sha1
The value is taken from the 'event.Event.ProcessCreation.hashes.sha1' field in the raw log.
hashes.sha256
read_only_udm.target.file.sha256
The value is taken from the 'event.Event.ProcessCreation.hashes.sha256' field in the raw log.
IpAddress
read_only_udm.target.ip
The value is taken from the 'IpAddress' field in the raw log.
local.address
read_only_udm.principal.ip
The value is taken from the 'event.Event.Tcpv4Listen.local.address' field in the raw log.
local.port
read_only_udm.principal.port
The value is taken from the 'event.Event.Tcpv4Listen.local.port' field in the raw log.
log_type
read_only_udm.metadata.log_type
The value is taken from the 'log_type' field in the raw log.
meta.agent_version
read_only_udm.metadata.product_version
The value is taken from the 'meta.agent_version' field in the raw log.
meta.computer_name
read_only_udm.principal.hostname
The value is taken from the 'meta.computer_name' field in the raw log.
meta.os_family
read_only_udm.principal.platform
The value is taken from the 'meta.os_family' field in the raw log and mapped to the corresponding platform (e.g.,
windows
to WINDOWS,
osx
to MAC,
linux
to LINUX).
meta.os_name
read_only_udm.principal.platform_version
The value is taken from the 'meta.os_name' field in the raw log.
meta.os_revision
read_only_udm.principal.platform_patch_level
The value is taken from the 'meta.os_revision' field in the raw log.
meta.uuid
read_only_udm.principal.asset_id
The value is taken from the 'meta.uuid' field in the raw log and prepended with
SENTINELONE:
.
name
read_only_udm.principal.application
The value is taken from the 'event.Event.
.
.name' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
parent.executable.hashes.md5
read_only_udm.target.process.parent_process.file.md5
The value is taken from the 'event.Event.
.parent.executable.hashes.md5' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit).
parent.executable.hashes.sha1
read_only_udm.target.process.parent_process.file.sha1
The value is taken from the 'event.Event.
.parent.executable.hashes.sha1' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit).
parent.executable.hashes.sha256
read_only_udm.target.process.parent_process.file.sha256
The value is taken from the 'event.Event.
.parent.executable.hashes.sha256' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit).
parent.executable.path
read_only_udm.target.process.parent_process.file.full_path
The value is taken from the 'event.Event.
.parent.executable.path' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit).
parent.fullPid.pid
read_only_udm.target.process.parent_process.pid
The value is taken from the 'event.Event.
.parent.fullPid.pid' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit).
path
read_only_udm.principal.process.file.full_path
The value is taken from the 'event.Event.
.
.path' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
process.commandLine
read_only_udm.target.process.command_line
The value is taken from the 'event.Event.ProcessCreation.process.commandLine' field in the raw log.
process.fullPid.pid
read_only_udm.target.process.pid
The value is taken from the 'event.Event.ProcessCreation.process.fullPid.pid' field in the raw log.
process.parent.fullPid.pid
read_only_udm.target.process.parent_process.pid
The value is taken from the 'event.Event.ProcessCreation.process.parent.fullPid.pid' field in the raw log.
ProviderGuid
security_result.about.resource.attribute.labels.value
The value is taken from the 'ProviderGuid' field in the raw log, with curly braces removed.
query
read_only_udm.network.dns.questions.name
The value is taken from the 'event.Event.Dns.query' field in the raw log.
RecordNumber
security_result.about.resource.attribute.labels.value
The value is taken from the 'RecordNumber' field in the raw log.
regKey.path
read_only_udm.target.registry.registry_key
The value is taken from the 'event.Event.RegKeyCreate.regKey.path' or 'event.Event.RegKeyDelete.regKey.path' field in the raw log.
regValue.path
read_only_udm.target.registry.registry_key
The value is taken from the 'event.Event.RegValueDelete.regValue.path' or 'event.Event.RegValueModified.regValue.path' field in the raw log.
results
read_only_udm.network.dns.answers.data
The value is taken from the 'event.Event.Dns.results' field in the raw log.
Sent UpdateServer
intermediary.hostname
The value is taken from the 'Sent UpdateServer' field in the raw log.
seq_id
This field is not directly mapped to the UDM.
signature.Status.Signed.identity
This field is not directly mapped to the UDM.
sizeBytes
read_only_udm.principal.process.file.size
The value is taken from the 'event.Event.
.
.sizeBytes' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
sourceAddress.address
read_only_udm.principal.ip
The value is taken from the 'event.Event.Tcpv4.sourceAddress.address' field in the raw log.
sourceAddress.port
read_only_udm.principal.port
The value is taken from the 'event.Event.Tcpv4.sourceAddress.port' field in the raw log.
SourceName
security_result.about.resource.attribute.labels.value
The value is taken from the 'SourceName' field in the raw log.
status
This field is not directly mapped to the UDM.
taskName
read_only_udm.target.resource.name
The value is taken from the 'event.Event.SchedTaskStart.taskName', 'event.Event.SchedTaskTrigger.taskName', or 'event.Event.SchedTaskDelete.taskName' field in the raw log.
targetFile.hashes.md5
read_only_udm.target.file.md5
The value is taken from the 'event.Event.FileDeletion.targetFile.hashes.md5' or 'event.Event.SchedTaskStart.targetFile.hashes.md5' field in the raw log.
targetFile.hashes.sha1
read_only_udm.target.file.sha1
The value is taken from the 'event.Event.FileDeletion.targetFile.hashes.sha1' or 'event.Event.SchedTaskStart.targetFile.hashes.sha1' field in the raw log.
targetFile.hashes.sha256
read_only_udm.target.file.sha256
The value is taken from the 'event.Event.FileDeletion.targetFile.hashes.sha256' or 'event.Event.SchedTaskStart.targetFile.hashes.sha256' field in the raw log.
targetFile.path
read_only_udm.target.file.full_path
The value is taken from the 'event.Event.FileDeletion.targetFile.path' or 'event.Event.SchedTaskStart.targetFile.path' field in the raw log.
Task
security_result.about.resource.attribute.labels.value
The value is taken from the 'Task' field in the raw log.
timestamp.millisecondsSinceEpoch
read_only_udm.metadata.event_timestamp.seconds
The value is taken from the 'event.timestamp.millisecondsSinceEpoch' field in the raw log, converted to seconds.
timestamp.millisecondsSinceEpoch
read_only_udm.metadata.event_timestamp.nanos
The value is taken from the 'event.timestamp.millisecondsSinceEpoch' field in the raw log, converted to nanoseconds.
trace_id
This field is not directly mapped to the UDM.
triggerType
This field is not directly mapped to the UDM.
trueContext
This field is not directly mapped to the UDM.
trueContext.key
This field is not directly mapped to the UDM.
trueContext.key.value
This field is not directly mapped to the UDM.
type
read_only_udm.network.dns.answers.type
The value is taken from the 'event.Event.Dns.results' field in the raw log and extracted using a regular expression.
url
read_only_udm.target.url
The value is taken from the 'event.Event.Http.url' field in the raw log.
user.name
read_only_udm.principal.user.userid
The value is taken from the 'event.Event.
.
.user.name' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
user.sid
read_only_udm.principal.user.windows_sid
The value is taken from the 'event.Event.
.
.user.sid' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
UserID
read_only_udm.target.user.windows_sid
The value is taken from the 'UserID' field in the raw log, only if it matches the Windows SID pattern.
UserSid
read_only_udm.target.user.windows_sid
The value is taken from the 'UserSid' field in the raw log, only if it matches the Windows SID pattern.
valueType
This field is not directly mapped to the UDM.
winEventLog.channel
security_result.about.resource.attribute.labels.value
The value is taken from the 'winEventLog.channel' field in the raw log.
winEventLog.description
This field is not directly mapped to the UDM.
winEventLog.id
security_result.about.resource.attribute.labels.value
The value is taken from the 'winEventLog.id' field in the raw log.
winEventLog.level
security_result.severity
The value is taken from the 'winEventLog.level' field in the raw log and mapped to the corresponding severity level (e.g.,
Warning
to MEDIUM).
winEventLog.providerName
security_result.about.resource.attribute.labels.value
The value is taken from the 'winEventLog.providerName' field in the raw log.
winEventLog.xml
This field is not directly mapped to the UDM.
read_only_udm.metadata.event_type
The value is determined based on the 'event_type' field and mapped to the corresponding UDM event type.
read_only_udm.metadata.vendor_name
The value is set to
SentinelOne
.
read_only_udm.metadata.product_name
The value is set to
Deep Visibility
.
read_only_udm.metadata.product_log_id
The value is taken from the 'trace.id' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.metadata.product_deployment_id
The value is taken from the 'account.id' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.metadata.url_back_to_product
The value is taken from the 'mgmt.url' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.metadata.ingestion_labels.key
The value is set to
Process eUserUid
or
Process lUserUid
for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.metadata.ingestion_labels.value
The value is taken from the 'src.process.eUserUid' or 'src.process.lUserUid' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.principal.administrative_domain
The domain portion of the 'event.Event.
.
.user.name' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit) and
is the field containing process information (e.g., process, source, parent).
read_only_udm.target.process.parent_process.command_line
The value is taken from the 'event.Event.
.parent.commandLine' field in the raw log, where
is the specific event type (e.g., ProcessCreation, ProcessExit).
read_only_udm.target.file
An empty object is created if the 'event_type' is not
FileCreation
,
FileDeletion
,
FileModification
,
SchedTaskStart
, or
ProcessCreation
.
read_only_udm.network.ip_protocol
The value is set to TCP for events with 'event_type' equal to
Tcpv4
,
Tcpv4Listen
, or
Http
.
read_only_udm.network.application_protocol
The value is set to DNS for events with 'event_type' equal to
Dns
.
read_only_udm.target.resource.type
The value is set to
TASK
for events with 'event_type' equal to
SchedTaskStart
,
SchedTaskTrigger
, or
SchedTaskDelete
.
read_only_udm.target.resource.resource_type
The value is set to TASK for events with 'event_type' equal to
SchedTaskStart
,
SchedTaskTrigger
, or
SchedTaskDelete
.
read_only_udm.principal.process.product_specific_process_id
The value is set to
ExecutionThreadID:<ExecutionThreadID>
if the 'ExecutionThreadID' field is present in the raw log.
read_only_udm.principal.asset.asset_id
The value is set to
Device ID:<agent.uuid>
if the 'agent.uuid' field is present in the raw log.
read_only_udm.principal.namespace
The value is taken from the 'site.id' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.principal.location.name
The value is taken from the 'site.name' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.principal.resource.attribute.labels.key
The value is set to
src.process.displayName
,
src.process.uid
,
isRedirectCmdProcessor
,
isNative64Bit
,
isStorylineRoot
,
signedStatus
,
src process subsystem
,
src process integrityLevel
, or
childProcCount
for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.principal.resource.attribute.labels.value
The value is taken from the corresponding field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.target.user.userid
The value is taken from the 'tgt.process.uid' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.target.user.user_display_name
The value is taken from the 'tgt.process.displayName' field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.target.resource.attribute.labels.key
The value is set to
isRedirectCmdProcessor
,
isNative64Bit
,
isStorylineRoot
,
signedStatus
,
file_isSigned
,
tgt process subsystem
, or
tgt process integrityLevel
for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.target.resource.attribute.labels.value
The value is taken from the corresponding field in the raw log, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.security_result.about.resource.attribute.labels.key
The value is set to
tgt.process.storyline.id
,
endpoint_type
,
packet_id
,
src.process.storyline.id
, or
src.process.parent.storyline.id
for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.security_result.about.resource.attribute.labels.value
The value is taken from the corresponding field in the raw log and prepended with
ID:
for storyline IDs, only for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.security_result.category_details
The value is set to
security
for events with 'meta.event.name' equal to
PROCESSCREATION
.
read_only_udm.target.asset.product_object_id
The value is taken from the 'AdapterName' field in the raw log, only for events with 'meta.event.name' equal to
EVENTLOG
.
security_result.about.resource.attribute.labels.key
The value is set to
TimeCreated SystemTime
,
EventID
,
Task
,
Channel
,
ProviderGuid
,
RecordNumber
,
SourceName
,
endpoint_type
, or
packet_id
for events with 'meta.event.name' equal to
EVENTLOG
.
security_result.detection_fields.key
The value is set to
Activity ID
for events with 'meta.event.name' equal to
EVENTLOG
and a non-empty 'ActivityID' field.
security_result.detection_fields.value
The value is taken from the 'ActivityID' field in the raw log, only for events with 'meta.event.name' equal to
EVENTLOG
and a non-empty 'ActivityID' field.
Need more help?
Get answers from Community members and Google SecOps professionals.
