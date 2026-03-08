# Collect SentinelOne EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-edr/  
**Scraped:** 2026-03-05T09:28:07.725201Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect SentinelOne EDR logs
Supported in:
Google secops
SIEM
This document explains how to export SentinelOne logs to Google Cloud Storage using SentinelOne Cloud Funnel. Since SentinelOne doesn't offer a built-in integration to directly export logs to Google Cloud Storage, Cloud Funnel acts as an intermediary service to push logs to the Cloud Storage.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to the Google Cloud platform
Privileged access to SentinelOne
Configure Permissions for Cloud Funnel to Access Cloud Storage
Sign in to the
Google Cloud console
.
Go to
IAM & Admin
.
In the
IAM
page, add a
new IAM role
for the
Cloud Funnel service account
:
Assign
Storage Object Creator
permissions.
Optional: assign
Storage Object Viewer
if you need Cloud Funnel to read objects from the bucket.
Grant these permissions to the
Cloud Funnel service account
.
Create a Cloud Storage Bucket
Sign in to the
Google Cloud console
.
Go to
Storage
>
Browser
.
Click
Create bucket
.
Provide the following configurations:
Bucket Name
: Choose a unique name for your bucket (for example,
sentinelone-logs
).
Storage Location
: Select the region where the bucket will reside (for example,
US-West1
).
Storage Class
: Choose a
Standard
storage class.
Click
Create
.
Configure Cloud Funnel in SentinelOne
In the SentinelOne Console, go to
Settings
.
Locate the
Cloud Funnel
option (under
Integrations
).
If it's not already enabled, click
Enable Cloud Funnel
.
Once enabled, you're prompted to configure the
Destination
settings.
Destination Selection
: Choose
Google Cloud Storage
as the destination for exporting logs.
Google Cloud Storage
: Provide the Google Cloud Storage credentials.
Log Export Frequency
: set the
frequency
for exporting logs (for example, hourly or daily).
How to configure Cloud Funnel Log Export
In the
Cloud Funnel Configuration
section of the SentinelOne Console, set the following:
Log Export Frequency
: Choose how often logs should be exported (for example. every hour or every day).
Log Format
: Choose the
JSON
format.
Bucket Name
: Enter the name of the
Google Cloud Storage bucket
you created earlier (for example,
sentinelone-logs
).
Optional:
Log Path Prefix
: Specify a
prefix
to organize logs within the bucket (for example,
sentinelone-logs/
).
Once the settings are configured, click
Save
to apply the changes.
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
How to set up the SentinelOne EDR feed
Click the
SentinelOne
pack.
Locate the
SentinelOne EDR
feed.
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
UDM mapping table
Log Field
UDM Mapping
Logic
event.contentHash.sha256
target.process.file.sha256
The SHA-256 hash of the target process's file, extracted from the
event.contentHash.sha256
field in the raw log.
event.decodedContent
target.labels
The decoded content of a script, extracted from the
event.decodedContent
field in the raw log. It is added as a label with the key
Decoded Content
to the target object.
event.destinationAddress.address
target.ip
The IP address of the destination, extracted from the
event.destinationAddress.address
field in the raw log.
event.destinationAddress.port
target.port
The port of the destination, extracted from the
event.destinationAddress.port
field in the raw log.
event.method
network.http.method
The HTTP method of the event, extracted from the
event.method
field in the raw log.
event.newValueData
target.registry.registry_value_data
The new value data of the registry value, extracted from the
event.newValueData
field in the raw log.
event.process.commandLine
target.process.command_line
The command line of the process, extracted from the
event.process.commandLine
field in the raw log.
event.process.executable.hashes.md5
target.process.file.md5
The MD5 hash of the process's executable, extracted from the
event.process.executable.hashes.md5
field in the raw log.
event.process.executable.hashes.sha1
target.process.file.sha1
The SHA-1 hash of the process's executable, extracted from the
event.process.executable.hashes.sha1
field in the raw log.
event.process.executable.hashes.sha256
target.process.file.sha256
The SHA-256 hash of the process's executable, extracted from the
event.process.executable.hashes.sha256
field in the raw log.
event.process.executable.path
target.process.file.full_path
The full path of the process's executable, extracted from the
event.process.executable.path
field in the raw log.
event.process.executable.sizeBytes
target.process.file.size
The size of the process's executable, extracted from the
event.process.executable.sizeBytes
field in the raw log.
event.process.fullPid.pid
target.process.pid
The PID of the process, extracted from the
event.process.fullPid.pid
field in the raw log.
event.query
network.dns.questions.name
The DNS query, extracted from the
event.query
field in the raw log.
event.regKey.path
target.registry.registry_key
The path of the registry key, extracted from the
event.regKey.path
field in the raw log.
event.regValue.key.value
target.registry.registry_name
,
target.registry.registry_value_name
The name of the registry value, extracted from the
event.regValue.key.value
field in the raw log.
event.regValue.path
target.registry.registry_key
The path of the registry value, extracted from the
event.regValue.path
field in the raw log.
event.results
network.dns.answers.data
The DNS answers, extracted from the
event.results
field in the raw log. The data is split into individual answers using the "
;
" separator.
event.source.commandLine
principal.process.command_line
The command line of the source process, extracted from the
event.source.commandLine
field in the raw log.
event.source.executable.hashes.md5
principal.process.file.md5
The MD5 hash of the source process's executable, extracted from the
event.source.executable.hashes.md5
field in the raw log.
event.source.executable.hashes.sha1
principal.process.file.sha1
The SHA-1 hash of the source process's executable, extracted from the
event.source.executable.hashes.sha1
field in the raw log.
event.source.executable.hashes.sha256
principal.process.file.sha256
The SHA-256 hash of the source process's executable, extracted from the
event.source.executable.hashes.sha256
field in the raw log.
event.source.executable.path
principal.process.file.full_path
The full path of the source process's executable, extracted from the
event.source.executable.path
field in the raw log.
event.source.executable.signature.signed.identity
principal.resource.attribute.labels
The signed identity of the source process's executable, extracted from the
event.source.executable.signature.signed.identity
field in the raw log. It is added as a label with the key
Source Signature Signed Identity
to the principal resource attribute labels.
event.source.executable.sizeBytes
principal.process.file.size
The size of the source process's executable, extracted from the
event.source.executable.sizeBytes
field in the raw log.
event.source.fullPid.pid
principal.process.pid
The PID of the source process, extracted from the
event.source.fullPid.pid
field in the raw log.
event.source.parent.commandLine
principal.process.parent_process.command_line
The command line of the source parent process, extracted from the
event.source.parent.commandLine
field in the raw log.
event.source.parent.executable.hashes.md5
principal.process.parent_process.file.md5
The MD5 hash of the source parent process's executable, extracted from the
event.source.parent.executable.hashes.md5
field in the raw log.
event.source.parent.executable.hashes.sha1
principal.process.parent_process.file.sha1
The SHA-1 hash of the source parent process's executable, extracted from the
event.source.parent.executable.hashes.sha1
field in the raw log.
event.source.parent.executable.hashes.sha256
principal.process.parent_process.file.sha256
The SHA-256 hash of the source parent process's executable, extracted from the
event.source.parent.executable.hashes.sha256
field in the raw log.
event.source.parent.executable.signature.signed.identity
principal.resource.attribute.labels
The signed identity of the source parent process's executable, extracted from the
event.source.parent.executable.signature.signed.identity
field in the raw log. It is added as a label with the key
Source Parent Signature Signed Identity
to the principal resource attribute labels.
event.source.parent.fullPid.pid
principal.process.parent_process.pid
The PID of the source parent process, extracted from the
event.source.parent.fullPid.pid
field in the raw log.
event.source.user.name
principal.user.userid
The username of the source process's user, extracted from the
event.source.user.name
field in the raw log.
event.source.user.sid
principal.user.windows_sid
The Windows SID of the source process's user, extracted from the
event.source.user.sid
field in the raw log.
event.sourceAddress.address
principal.ip
The IP address of the source, extracted from the
event.sourceAddress.address
field in the raw log.
event.sourceAddress.port
principal.port
The port of the source, extracted from the
event.sourceAddress.port
field in the raw log.
event.target.executable.hashes.md5
target.process.file.md5
The MD5 hash of the target process's executable, extracted from the
event.target.executable.hashes.md5
field in the raw log.
event.target.executable.hashes.sha1
target.process.file.sha1
The SHA-1 hash of the target process's executable, extracted from the
event.target.executable.hashes.sha1
field in the raw log.
event.target.executable.hashes.sha256
target.process.file.sha256
The SHA-256 hash of the target process's executable, extracted from the
event.target.executable.hashes.sha256
field in the raw log.
event.target.executable.path
target.process.file.full_path
The full path of the target process's executable, extracted from the
event.target.executable.path
field in the raw log.
event.target.executable.signature.signed.identity
target.resource.attribute.labels
The signed identity of the target process's executable, extracted from the
event.target.executable.signature.signed.identity
field in the raw log. It is added as a label with the key
Target Signature Signed Identity
to the target resource attribute labels.
event.target.executable.sizeBytes
target.process.file.size
The size of the target process's executable, extracted from the
event.target.executable.sizeBytes
field in the raw log.
event.target.fullPid.pid
target.process.pid
The PID of the target process, extracted from the
event.target.fullPid.pid
field in the raw log.
event.targetFile.path
target.file.full_path
The full path of the target file, extracted from the
event.targetFile.path
field in the raw log.
event.targetFile.signature.signed.identity
target.resource.attribute.labels
The signed identity of the target file, extracted from the
event.targetFile.signature.signed.identity
field in the raw log. It is added as a label with the key
Target File Signature Signed Identity
to the target resource attribute labels.
event.trueContext.key.value
Not mapped to the UDM.
event.type
metadata.description
The type of the event, extracted from the
event.type
field in the raw log.
event.url
target.url
The URL of the event, extracted from the
event.url
field in the raw log.
meta.agentVersion
metadata.product_version
,
metadata.product_version
The version of the agent, extracted from the
meta.agentVersion
field in the raw log.
meta.computerName
principal.hostname
,
target.hostname
The hostname of the computer, extracted from the
meta.computerName
field in the raw log.
meta.osFamily
principal.asset.platform_software.platform
,
target.asset.platform_software.platform
The operating system family of the computer, extracted from the
meta.osFamily
field in the raw log. It is mapped to
LINUX
for
linux
and
WINDOWS
for
windows
.
meta.osRevision
principal.asset.platform_software.platform_version
,
target.asset.platform_software.platform_version
The operating system revision of the computer, extracted from the
meta.osRevision
field in the raw log.
meta.traceId
metadata.product_log_id
The trace ID of the event, extracted from the
meta.traceId
field in the raw log.
meta.uuid
principal.asset.product_object_id
,
target.asset.product_object_id
The UUID of the computer, extracted from the
meta.uuid
field in the raw log.
metadata_event_type
metadata.event_type
The type of the event, set by the parser logic based on the
event.type
field.
metadata_product_name
metadata.product_name
The name of the product, set to
Singularity XDR
by the parser logic.
metadata_vendor_name
metadata.vendor_name
The name of the vendor, set to
SentinelOne
by the parser logic.
network_application_protocol
network.application_protocol
The application protocol of the network connection, set to
DNS
for DNS events by the parser logic.
network_dns_questions.name
network.dns.questions.name
The name of the DNS question, extracted from the
event.query
field in the raw log.
network_direction
network.direction
The direction of the network connection, set to
OUTBOUND
for outgoing connections and
INBOUND
for incoming connections by the parser logic.
network_http_method
network.http.method
The HTTP method of the event, extracted from the
event.method
field in the raw log.
principal.process.command_line
target.process.command_line
The command line of the principal process, extracted from the
principal.process.command_line
field and mapped to the target process command line.
principal.process.file.full_path
target.process.file.full_path
The full path of the principal process's file, extracted from the
principal.process.file.full_path
field and mapped to the target process file full path.
principal.process.file.md5
target.process.file.md5
The MD5 hash of the principal process's file, extracted from the
principal.process.file.md5
field and mapped to the target process file MD5.
principal.process.file.sha1
target.process.file.sha1
The SHA-1 hash of the principal process's file, extracted from the
principal.process.file.sha1
field and mapped to the target process file SHA-1.
principal.process.file.sha256
target.process.file.sha256
The SHA-256 hash of the principal process's file, extracted from the
principal.process.file.sha256
field and mapped to the target process file SHA-256.
principal.process.file.size
target.process.file.size
The size of the principal process's file, extracted from the
principal.process.file.size
field and mapped to the target process file size.
principal.process.pid
target.process.pid
The PID of the principal process, extracted from the
principal.process.pid
field and mapped to the target process PID.
principal.user.userid
target.user.userid
The user ID of the principal, extracted from the
principal.user.userid
field and mapped to the target user ID.
principal.user.windows_sid
target.user.windows_sid
The Windows SID of the principal, extracted from the
principal.user.windows_sid
field and mapped to the target user Windows SID.
Need more help?
Get answers from Community members and Google SecOps professionals.
