# Collect Jamf Protect Telemetry V2 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry-v2/  
**Scraped:** 2026-03-05T09:17:30.084569Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Jamf Protect Telemetry V2 logs
Supported in:
Google secops
SIEM
This document describes how you can collect Jamf Protect Telemetry V2 logs by setting up a Google Security Operations
feed. It details the mapping of Jamf Protect Telemetry V2 log fields to the Unified Data Model (UDM) fields within Google SecOps, and lists the supported Jamf Protect Telemetry V2 version.
For more information, see
Data ingestion to Google SecOps
.
A typical deployment consists of Jamf Protect Telemetry V2 and the Google SecOps feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Jamf Protect Telemetry V2
. The Jamf Protect Telemetry V2 platform from which you collect logs.
Google SecOps feed
. The Google SecOps feed that fetches logs from Jamf Protect Telemetry and writes logs to Google SecOps.
Google SecOps
. Google SecOps retains and analyzes the logs from Jamf Protect Telemetry V2.
Each log is normalized to the Unified Data Model (UDM) using a specific parser. The information in this document applies to the parser associated with the JAMF_TELEMETRY_V2 ingestion label.
Before you begin
Ensure that you have the latest version of
Jamf Protect Telemetry V2
set up.
Ensure that you are using Jamf Protect version 6.3.2 or later.
Ensure that all systems in the deployment architecture are configured with the UTC time zone.
Configure a feed in Google SecOps to ingest Jamf Protect Telemetry V2 logs
You can use either Amazon S3 V2 or a webhook to set up an ingestion feed in Google SecOps.
Set up an ingestion feed in Google SecOps using Amazon S3 V2
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
JAMF
feed pack.
Locate the
JAMF Protect Telemetry V2
feed.
In the
Source type
list, select
Amazon S3 V2
.
Specify values for the following fields:
S3 URI
: the URI pointing to an S3 container.
Source deletion option
: whether to delete files or directories after transfer.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Select
Access key
or
Secret Access key
: Choose the appropriate credential type.
Key/Token
: the shared key or SAS token to access S3 resources.
Click
Create Feed
.
Set up an ingestion feed in Google SecOps using a webhook
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
JAMF
feed pack.
Locate the
JAMF Protect Telemetry V2
feed.
In the
Source type
list, select
Webhook
.
Specify values for the following fields:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label to be applied to the events from this feed.
Click
Create Feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Create an API key for a webhook feed
Go to
Google Cloud console
>
Credentials
.
Go to Credentials
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Google Security Operations API
.
Set up Jamf Protect Telemetry V2 for a webhook feed
In the Jamf Protect Telemetry V2 application, navigate to the related
Action configuration
.
Click
Create Actions
to add a new Data endpoint.
Select
HTTP
as the protocol.
In the
URL
field, enter the HTTPS URL of the Google Security Operations API endpoint. (This is the
Endpoint Information
field that you copied from the webhook feed setup. It's
already
in the required format.)
Enable authentication by specifying the
API key
and
Secret key
as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL. If your webhook client doesn't support custom headers, you can specify the
API key
and
Secret key
using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: The feed endpoint URL.
API_KEY
: The API key to authenticate to Google Security Operations.
SECRET
: The secret key that you generated to authenticate the feed.
In the
Collect Logs
section, select
Telemetry
.
Click
Submit
.
For more information about Google SecOps feeds, see
Google SecOps feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Field mapping reference
This section explains how the Google SecOps parser maps Jamf Protect Telemetry V2 fields to Google SecOps Unified Data Model (UDM) fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
JAMF_TELEMETRY_V2
log types and their corresponding UDM event types.
Event Identifier
Event Type
authentication
USER_LOGIN
bios_uefi
STATUS_UPDATE
btm_launch_item_add
PROCESS_LAUNCH
btm_launch_item_remove
PROCESS_TERMINATION
chroot
FILE_MODIFICATION
cs_invalidated
STATUS_UPDATE
exec
PROCESS_LAUNCH
file_collection
STATUS_UPDATE
gatekeeper_user_override
STATUS_UPDATE
kextload
STATUS_UPDATE
kextunload
STATUS_UPDATE
log_collection
STATUS_UPDATE
login_login
USER_LOGIN
login_logout
USER_LOGOUT
lw_session_lock
USER_LOGOUT
lw_session_login
USER_LOGIN
lw_session_logout
USER_LOGOUT
lw_session_unlock
USER_LOGIN
mount
STATUS_UPDATE
od_attribute_set
USER_RESOURCE_UPDATE_CONTENT
od_attribute_value_add
STATUS_UPDATE
od_attribute_value_remove
USER_RESOURCE_DELETION
od_create_group
GROUP_CREATION
od_create_user
USER_CREATION
od_delete_group
GROUP_DELETION
od_delete_user
USER_DELETION
od_disable_user
USER_UNCATEGORIZED
od_enable_user
USER_UNCATEGORIZED
od_group_add
GROUP_MODIFICATION
od_group_remove
GROUP_MODIFICATION
od_group_set
GROUP_MODIFICATION
od_modify_password
USER_CHANGE_PASSWORD
openssh_login
USER_LOGIN
openssh_logout
USER_LOGOUT
sudo
STATUS_UPDATE
system_performance
STATUS_UPDATE
unmount
STATUS_UPDATE
profile_add
SETTING_CREATION
profile_remove
SETTING_DELETION
remount
RESOURCE_CREATION
screensharing_attach
USER_LOGIN
screensharing_detach
USER_LOGOUT
settime
STATUS_UPDATE
su
USER_LOGIN
xp_malware_detected
SCAN_FILE
xp_malware_remediated
SCAN_FILE
pty_grant
PROCESS_LAUNCH
pty_close
STATUS_UPDATE
tcc_modify
RESOURCE_PERMISSIONS_CHANGE
network_connect
NETWORK_CONNECTION
Field mapping reference: JAMF_TELEMETRY_V2 - Common Fields
The following table lists common fields of the
JAMF_TELEMETRY_V2
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
action.result.result.auth
security_result.action
If the **event_type** log field value is < `8000`, and not equal to `113` or `112`, and the **action.result.result.auth** field is equal to **1**, then set `security_result.action` to **BLOCK**. Else, set `security_result.action` to **ALLOW**
principal.platform
The
principal.platform
UDM field is set to
MAC
.
uuid
metadata.product_log_id
time
metadata.event_timestamp
metadata.product
metadata.product_name
host.protectVersion
metadata.product_version
metadata.vendor
metadata.vendor_name
host.hostname
principal.asset.hostname
host.os
principal.platform_version
host.provisioningUDID
principal.asset_id
host.serial
principal.asset.hardware.serial_number
host.ips
principal.ip
Iterate through log field
host.ips
, then
host.ips
log field is mapped to the
principal.ip
UDM field.
event_type
additional.fields[event_type]
global_seq_num
additional.fields[global_seq_num]
process.executable.path
src.process.file.full_path
process.executable.stat.st_dev
src.process.file.stat_dev
process.executable.stat.st_flags
src.process.file.stat_flags
process.executable.stat.st_ino
src.process.file.stat_inode
process.executable.stat.st_mode
src.process.file.stat_mode
process.executable.stat.st_mtimespec
src.process.file.last_modification_time
process.executable.stat.st_atimespec
src.process.file.last_access_time
process.executable.stat.st_nlink
src.process.file.stat_nlink
process.executable.stat.st_size
src.process.file.size
process.executable.sha256
src.process.file.sha256
process.executable.sha1
src.process.file.sha1
process.signing_id
src.process.file.signature_info.codesign.id
process.team_id
additional.fields[process_team_id]
process.ppid
additional.fields[process_ppid]
process.codesigning_flags
additional.fields[process_codesigning_flags]
process.cdhash
additional.fields[process_cdhash]
process.is_platform_binary
additional.fields[process_is_platform_binary]
process.is_es_client
additional.fields[process_is_es_client]
process.group_id
additional.fields[process_group_id]
process.original_ppid
additional.fields[process_original_ppid]
process.session_id
additional.fields[process_session_id]
thread.uuid
additional.fields[thread_uuid]
thread.thread_id
additional.fields[thread_id]
seq_num
additional.fields[seq_num]
mach_time
additional.fields[mach_time]
version
additional.fields[version]
process.audit_token.euid
src.process.euid
process.audit_token.ruid
src.process.ruid
process.audit_token.egid
src.process.egid
process.audit_token.rgid
src.process.rgid
process.audit_token.pgid
src.process.pgid
process.audit_token.pid
src.process.pid
process.audit_token.uuid
src.process.product_specific_process_id
process.audit_token.signing_id
additional.fields[process_audit_token_signing_id]
process.parent_audit_token.euid
src.process.parent_process.euid
process.parent_audit_token.ruid
src.process.parent_process.ruid
process.parent_audit_token.egid
src.process.parent_process.egid
process.parent_audit_token.rgid
src.process.parent_process.rgid
process.parent_audit_token.pgid
src.process.parent_process.pgid
process.parent_audit_token.pid
src.process.parent_process.pid
process.parent_audit_token.uuid
src.process.parent_process.product_specific_process_id
process.parent_audit_token.signing_id
src.process.parent_process.file.signature_info.codesign.id
Field mapping reference: Rawlog fields to UDM fields by
event_type
.
event_type: remount
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
remount
.
metadata.description
A file system has been remounted.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
RESOURCE_CREATION
.
principal.user.userid
The
principal.user.userid
UDM field is set to
null
.
event.remount.statfs.f_owner
target.user.userid
event.remount.device.size
target.file.size
event.remount.statfs.f_fstypename
target.resource.resource_subtype
event.remount.statfs.f_mntfromname
src.resource.name
event.remount.statfs.f_mntonname
target.resource.name
event_type: screensharing_attach
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
screensharing_attach
.
metadata.description
A screen sharing session has attached to a graphical session.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
event.screensharing_attach.source_address
src.ip
event.screensharing_attach.authentication_username
target.user.user_display_name
event.screensharing_attach.session_username
principal.user.user_display_name
event.screensharing_attach.viewer_appleid
additional.fields[screensharing_attach_viewer_appleid]
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
security_result.category
If the
event.screensharing_attach.success
log field value is equal to
false
then, the
security_result.category
UDM field is set to
AUTH_VIOLATION
.
event_type: su
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
su
.
metadata.description
A user attempts to start a new shell using a substitute user identity.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.su.argv
target.process.command_line
If the
event.su.argc
log field value is
not
equal to
0
then,
iterate through log field
event.su.argv
, then
event.su.argv
log field is mapped to the
target.process.command_line
UDM field.
event.su.to_uid
target.user.userid
event.su.to_username
target.user.user_display_name
event.su.from_uid
principal.user.userid
event.su.from_username
principal.user.user_display_name
event_type: settime
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
settime
.
metadata.description
The system time was attempted to be set.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event_type: screensharing_detach
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
screensharing_detach
.
metadata.description
A screen sharing session has detached from a graphical session.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGOUT
.
target.user.user_display_name
The
target.user.user_display_name
UDM field is set to
null
.
event.screensharing_detach.source_address
src.ip
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
mechanism
.
event_type: xp_malware_remediated
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
xp_malware_remediated
.
metadata.description
Apple's XProtect remediated malware on the system.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_FILE
.
action.result.result.auth
security_result.action
event.xp_malware_remediated.remediated_path
target.file.full_path
event.xp_malware_remediated.action_type
additional.fields[xp_malware_remediated_action_type]
event.xp_malware_remediated.success
additional.fields[xp_malware_remediated_success]
event.xp_malware_remediated.incident_identifier
security_result.threat_id
event.xp_malware_remediated.malware_identifier
security_result.threat_name
event.xp_malware_remediated.signature_version
security_result.rule_id
event_type: xp_malware_detected
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
xp_malware_detected
.
metadata.description
Apple's XProtect detected malware on the system.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
SCAN_FILE
.
action.result.result.auth
security_result.action
event.xp_malware_detected.detected_path
target.file.full_path
event.xp_malware_detected.incident_identifier
security_result.threat_id
event.xp_malware_detected.malware_identifier
security_result.threat_name
event_type: authentication
Log field
UDM mapping
Logic
Check additional fields in conf
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
authentication
.
metadata.description
A user authentication has occurred.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
event.authentication.data.od.instigator.audit_token.pid
principal.process.pid
event.authentication.data.od.instigator.audit_token.uuid
principal.process.product_specific_process_id
JamfProtect:%{event.authentication.data.od.instigator.audit_token.uuid}
log field is mapped to the
principal.process.product_specific_process_id
UDM field.
event.authentication.data.od.instigator.audit_token.euid
principal.process.euid
event.authentication.data.od.instigator.audit_token.ruid
principal.process.ruid
event.authentication.data.od.instigator.audit_token.rgid
principal.process.rgid
event.authentication.data.od.instigator.audit_token.pgid
principal.process.pgid
event.authentication.data.od.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.authentication.data.od.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.authentication.data.od.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.authentication.data.od.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.authentication.data.od.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.authentication.data.od.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.authentication.data.od.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.authentication.data.od.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
JamfProtect:%{event.authentication.data.od.instigator.parent_audit_token.uuid}
log field is mapped to the
principal.process.parent_process.product_specific_process_id
UDM field.
event.authentication.data.od.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.authentication.data.od.instigator.executable.path
principal.process.file.full_path
event.authentication.data.od.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.authentication.data.od.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.authentication.data.od.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.authentication.data.od.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.authentication.data.od.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.authentication.data.od.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.authentication.data.od.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.authentication.data.od.instigator.executable.stat.st_size
principal.process.file.size
event.authentication.data.od.instigator.executable.sha256
principal.process.file.sha256
event.authentication.data.od.instigator.executable.sha1
principal.process.file.sha1
event.authentication.data.od.instigator.signing_id
additional.fields[authentication_data_od_instigator_signing_id]
event.authentication.data.od.instigator.team_id
additional.fields[authentication_data_od_instigator_team_id]
event.authentication.data.od.instigator.ppid
rincipal.process.parent_process.pid
event.authentication.data.od.instigator.codesigning_flags
additional.fields[codesigning_flags]
event.authentication.data.od.instigator.cdhash
additional.fields[cdhash]
event.authentication.data.od.instigator.is_platform_binary
additional.fields[is_platform_binary]
event.authentication.data.od.instigator.is_es_client
additional.fields[is_es_client]
event.authentication.data.od.instigator.group_id
additional.fields[group_id]
event.authentication.data.od.instigator.original_ppid
additional.fields[original_ppid]
event.authentication.data.od.instigator.session_id
additional.fields[session_id]
event.authentication.data.touchid.instigator.audit_token.euid
principal.process.euid
event.authentication.data.touchid.instigator.audit_token.ruid
principal.process.ruid
event.authentication.data.touchid.instigator.audit_token.egid
principal.process.egid
event.authentication.data.touchid.instigator.audit_token.rgid
principal.process.rgid
event.authentication.data.touchid.instigator.audit_token.pgid
principal.process.pgid
event.authentication.data.touchid.instigator.audit_token.pid
principal.process.pid
event.authentication.data.touchid.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.authentication.data.touchid.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.authentication.data.touchid.instigator.parent_audit_token.euid
principal.parent_process.parent_process.euid
event.authentication.data.touchid.instigator.parent_audit_token.ruid
principal.parent_process.parent_process.ruid
event.authentication.data.touchid.instigator.parent_audit_token.egid
principal.parent_process.parent_process.egid
event.authentication.data.touchid.instigator.parent_audit_token.rgid
principal.parent_process.parent_process.rgid
event.authentication.data.touchid.instigator.parent_audit_token.pgid
principal.parent_process.parent_process.pgid
event.authentication.data.touchid.instigator.parent_audit_token.pid
principal.parent_process.parent_process.pid
event.authentication.data.touchid.instigator.parent_audit_token.uuid
principal.parent_process.product_specific_process_id
event.authentication.data.touchid.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.authentication.data.touchid.instigator.executable.path
principal.process.file.full_path
event.authentication.data.touchid.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.authentication.data.touchid.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.authentication.data.touchid.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.authentication.data.touchid.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.authentication.data.touchid.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.authentication.data.touchid.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.authentication.data.touchid.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.authentication.data.touchid.instigator.executable.stat.st_size
principal.process.file.size
event.authentication.data.touchid.instigator.executable.sha256
principal.process.file.sha256
event.authentication.data.touchid.instigator.executable.sha1
principal.process.file.sha1
event.authentication.data.touchid.instigator.signing_id
additional.fields[authentication_data_touch_id_instigator_signing_id]
event.authentication.data.touchid.instigator.team_id
additional.fields[authentication_data_touch_id_instigator_team_id]
event.authentication.data.touchid.instigator.ppid
additional.fields[authentication_data_touch_id_instigator_ppid]
event.authentication.data.touchid.instigator.codesigning_flags
additional.fields[touchid_instigator_codesigning_flags]
event.authentication.data.touchid.instigator.cdhash
additional.fields[touchid_instigator_cdhash]
event.authentication.data.touchid.instigator.is_platform_binary
additional.fields[touchid_instigator_is_platform_binary]
event.authentication.data.touchid.instigator.is_es_client
additional.fields[touchid_instigator_is_es_client]
event.authentication.data.touchid.instigator.group_id
additional.fields[touchid_instigator_group_id]
event.authentication.data.touchid.instigator.original_ppid
additional.fields[touchid_instigator_original_ppid]
event.authentication.data.touchid.instigator.session_id
additional.fields[touchid_instigator_session_id]
event.authentication.data.token.instigator.audit_token.euid
principal.process.euid
event.authentication.data.token.instigator.audit_token.ruid
principal.process.ruid
event.authentication.data.token.instigator.audit_token.egid
principal.process.egid
event.authentication.data.token.instigator.audit_token.rgid
principal.process.rgid
event.authentication.data.token.instigator.audit_token.pgid
principal.process.pgid
event.authentication.data.token.instigator.audit_token.pid
principal.process.pid
event.authentication.data.token.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.authentication.data.token.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.authentication.data.token.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.authentication.data.token.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.authentication.data.token.instigator.parent_audit_token.egid
process.parent_process.egid
event.authentication.data.token.instigator.parent_audit_token.rgid
process.parent_process.rgid
event.authentication.data.token.instigator.parent_audit_token.pgid
process.parent_process.pgid
event.authentication.data.token.instigator.parent_audit_token.pid
process.parent_process.pid
event.authentication.data.token.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.authentication.data.token.instigator.parent_audit_token.signing_id
process.parent_process.file.signature_info.codesign.id
event.authentication.data.token.instigator.executable.path
principal.process.file.full_path
event.authentication.data.token.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.authentication.data.token.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.authentication.data.token.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.authentication.data.token.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.authentication.data.token.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.authentication.data.token.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.authentication.data.token.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.authentication.data.token.instigator.executable.stat.st_size
principal.process.file.size
event.authentication.data.token.instigator.executable.sha256
principal.process.file.sha256
event.authentication.data.token.instigator.executable.sha1
principal.process.file.sha1
event.authentication.data.token.instigator.signing_id
additional.fields[authentication_data_token_instigator_signing_id]
event.authentication.data.token.instigator.team_id
additional.fields[authentication_data_token_instigator_team_id]
event.authentication.data.token.instigator.ppid
additional.fields[authentication_data_token_instigator_ppid]
event.authentication.data.token.instigator.codesigning_flags
additional.fields[instigator_codesigning_flags]
event.authentication.data.token.instigator.cdhash
additional.fields[instigator_cdhash]
event.authentication.data.token.instigator.is_platform_binary
additional.fields[instigator_is_platform_binary]
event.authentication.data.token.instigator.is_es_client
additional.fields[instigator_is_es_client]
event.authentication.data.token.instigator.group_id
additional.fields[instigator_group_id]
event.authentication.data.token.instigator.original_ppid
additional.fields[instigator_original_ppid]
event.authentication.data.token.instigator.session_id
additional.fields[instigator_session_id]
event.authentication.data.od.record_name
target.user.user_display_name
event.authentication.data.od.db_path
additional.fields[db_path]
event.authentication.data.od.node_name
additional.fields[node_name]
event.authentication.data.od.record_type
additional.fields[record_type]
event.authentication.data.touchid.uid
target.user.userid
event.authentication.data.touchid.touchid_mode
additional.fields[authentication_data_touchid_touchid_mode]
event.authentication.data.token.pubkey_hash
additional.fields[authentication_data_token_pubkey_hash]
event.authentication.data.token.token_id
additional.fields[authentication_data_token_token_id]
event.authentication.data.token.kerberos_principal
additional.fields[authentication_data_token_kerberos_principal]
event.authentication.data.auto_unlock.username
target.user.user_display_name
event.authentication.data.auto_unlock.type
additional.fields[authentication_data_auto_unlock_type]
event.authentication.type
extensions.auth.mechanism
If the
event.authentication.type
log field value is equal to
0
then, the
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
Else If the
event.authentication.type
log field value is equal to
1
then, the
extensions.auth.mechanism
UDM field is set to
MECHANISM_OTHER
.
Else If the
event.authentication.type
log field value is equal to
2
then, the
extensions.auth.mechanism
UDM field is set to
HARDWARE_KEY
.
Else, the
extensions.auth.mechanism
UDM field is set to
MECHANISM_OTHER
.
event.authentication.success
security_result.category
If the
event.authentication.success
log field value is equal to
false
then, the
security_result.category
UDM field is set to
AUTH_VIOLATION
.
event_type: btm_launch_item_add
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
btm_launch_item_add
.
metadata.description
Apple's Background Task Manager notifies that a new persistence item has been added.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
PROCESS_LAUNCH
.
event.btm_launch_item_add.instigator.audit_token.euid
principal.process.euid
event.btm_launch_item_add.instigator.audit_token.ruid
principal.process.ruid
event.btm_launch_item_add.instigator.audit_token.egid
principal.process.egid
event.btm_launch_item_add.instigator.audit_token.rgid
principal.process.rgid
event.btm_launch_item_add.instigator.audit_token.pgid
principal.process.pgid
event.btm_launch_item_add.instigator.audit_token.pid
principal.process.pid
event.btm_launch_item_add.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.btm_launch_item_add.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.btm_launch_item_add.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.btm_launch_item_add.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.btm_launch_item_add.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.btm_launch_item_add.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.btm_launch_item_add.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.btm_launch_item_add.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.btm_launch_item_add.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.btm_launch_item_add.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.btm_launch_item_add.instigator.executable.path
principal.process.file.full_path
event.btm_launch_item_add.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.btm_launch_item_add.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.btm_launch_item_add.instigator.executable.stat.stat_inode
principal.process.file.stat_inode
event.btm_launch_item_add.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.btm_launch_item_add.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.btm_launch_item_add.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.btm_launch_item_add.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.btm_launch_item_add.instigator.executable.stat.st_size
principal.process.file.size
event.btm_launch_item_add.instigator.executable.sha256
principal.process.file.sha256
event.btm_launch_item_add.instigator.executable.sha1
principal.process.file.sha1
event.btm_launch_item_add.instigator.signing_id
additional.fields[btm_launch_item_add_data_token_instigator_signing_id]
event.btm_launch_item_add.instigator.team_id
additional.fields[btm_launch_item_add_data_token_instigator_team_id]
event.btm_launch_item_add.instigator.ppid
additional.fields[btm_launch_item_add_data_token_instigator_ppid]
event.btm_launch_item_add.instigator.codesigning_flags
additional.fields[btm_launch_item_add_instigator_codesigning_flags]
event.btm_launch_item_add.instigator.cdhash
additional.fields[btm_launch_item_add_instigator_cdhash]
event.btm_launch_item_add.instigator.is_platform_binary
additional.fields[btm_launch_item_add_instigator_is_platform_binary]
event.btm_launch_item_add.instigator.is_es_client
additional.fields[btm_launch_item_add_instigator_is_es_client]
event.btm_launch_item_add.instigator.group_id
additional.fields[btm_launch_item_add_instigator_group_id]
event.btm_launch_item_add.instigator.original_ppid
additional.fields[btm_launch_item_add_instigator_original_ppid]
event.btm_launch_item_add.instigator.session_id
additional.fields[btm_launch_item_add_instigator_session_id]
event.btm_launch_item_add.app.audit_token.euid
target.process.euid
event.btm_launch_item_add.app.audit_token.ruid
target.process.ruid
event.btm_launch_item_add.app.audit_token.egid
target.process.egid
event.btm_launch_item_add.app.audit_token.rgid
target.process.rgid
event.btm_launch_item_add.app.audit_token.pgid
target.process.pgid
event.btm_launch_item_add.app.audit_token.pid
target.process.pid
event.btm_launch_item_add.app.audit_token.uuid
target.process.product_specific_process_id
event.btm_launch_item_add.app.audit_token.signing_id
target.process.file.signature_info.codesign.id
event.btm_launch_item_add.app.parent_audit_token.euid
target.process.parent_process.euid
event.btm_launch_item_add.app.parent_audit_token.ruid
target.process.parent_process.ruid
event.btm_launch_item_add.app.parent_audit_token.egid
target.process.parent_process.egid
event.btm_launch_item_add.app.parent_audit_token.rgid
target.process.parent_process.rgid
event.btm_launch_item_add.app.parent_audit_token.pid
target.process.parent_process.pid
event.btm_launch_item_add.app.parent_audit_token.uuid
target.process.parent_process.product_specific_process_id
event.btm_launch_item_add.app.parent_audit_token.signing_id
target.process.parent_process.file.signature_info.codesign.id
event.btm_launch_item_add.app.executable.path
target.process.file.full_path
event.btm_launch_item_add.app.executable.stat.st_dev
target.process.file.stat_dev
event.btm_launch_item_add.app.executable.stat.st_flags
target.process.file.stat_flags
event.btm_launch_item_add.app.executable.stat.st_ino
target.process.file.stat_inode
event.btm_launch_item_add.app.executable.stat.st_mode
target.process.file.stat_mode
event.btm_launch_item_add.app.executable.stat.st_mtimespec
target.process.file.last_modification_time
event.btm_launch_item_add.app.executable.stat.st_atimespec
target.process.file.last_access_time
event.btm_launch_item_add.app.executable.stat.st_nlink
target.process.file.stat_nlink
event.btm_launch_item_add.app.executable.stat.st_size
target.process.file.size
event.btm_launch_item_add.app.executable.sha256
target.process.file.sha256
event.btm_launch_item_add.app.executable.sha1
target.process.file.sha1
event.btm_launch_item_add.app.signing_id
additional.fields[btm_launch_item_add_app_signing_id]
event.btm_launch_item_add.app.team_id
additional.fields[btm_launch_item_add_app_team_id]
event.btm_launch_item_add.app.ppid
additional.fields[btm_launch_item_add_app_ppid]
event.btm_launch_item_add.app.codesigning_flags
additional.fields[btm_launch_item_add_app_codesigning_flags]
event.btm_launch_item_add.app.cdhash
additional.fields[btm_launch_item_add_app_cdhash]
event.btm_launch_item_add.app.is_platform_binary
additional.fields[btm_launch_item_add_app_is_platform_binary]
event.btm_launch_item_add.app.is_es_client
additional.fields[btm_launch_item_add_app_is_es_client]
event.btm_launch_item_add.app.group_id
additional.fields[btm_launch_item_add_app_group_id]
event.btm_launch_item_add.app.original_ppid
additional.fields[btm_launch_item_add_app_group_id]
event.btm_launch_item_add.app.session_id
additional.fields[btm_launch_item_add_app_session_id]
event.btm_launch_item_add.executable_path
target.file.full_path
If the
event.btm_launch_item_add.item.item_type
log field value is equal to
4
or the
event.btm_launch_item_add.item.item_type
log field value is equal to
3
and if the
event.btm_launch_item_add.executable_path
log field value is
not
empty
and if the
event.btm_launch_item_add.executable_path
log field value matches the regular expression pattern
/^file:./
or the
event.btm_launch_item_add.executable_path
log field value does not match the regular expression pattern
/^[a-zA-Z0-9]
then,
event_btm_launch_item_add_executable_path
log field is mapped to the
target_file_full_path
UDM field_
Else,
%{event_btm_launch_item_add_item_app_url}%{event_btm_launch_item_add_executable_path}
log field is mapped to the
target_file_full_path
UDM field_
Else If the
event_btm_launch_item_add_item_item_url
log field value is
not
empty
and if the
event_btm_launch_item_add_item_item_url
log field value matches the regular expression pattern
/^file:_/
or the
event_btm_launch_item_add_item_item_url
log field value does not match the regular expression pattern
/^[a-zA-Z0-9]
then,
event.btm_launch_item_add.item.item_url
log field is mapped to the
target.resource.name
UDM field.
Else,
%{event.btm_launch_item_add.item.app_url}%{event.btm_launch_item_add.item.item_url}
log field is mapped to the
target.resource.name
UDM field.
event.btm_launch_item_add.item.item_url
target.file.full_path
If the
event.btm_launch_item_add.item.item_type
log field value is equal to
0
or the
event.btm_launch_item_add.item.item_type
log field value is equal to
1
or the
event.btm_launch_item_add.item.item_type
log field value is equal to
2
and if the
event.btm_launch_item_add.item.item_url
log field value is
not
empty and if the
event.btm_launch_item_add.item.item_url
log field value matches the regular expression pattern
/^file:.
/
or the
event.btm_launch_item_add.item.item_url
log field value does not match the regular expression pattern
/^[a-zA-Z0-9]
then the
event.btm_launch_item_add.item.item_url
log field is mapped to the
target.file.full_path
UDM field.
Else,
%{event.btm_launch_item_add.item.app_url}%{event.btm_launch_item_add.item.item_url}
log field is mapped to the
target.file.full_path
UDM field.
event.btm_launch_item_add.item.uid
target.user.userid
event.btm_launch_item_add.item.item_type
target.application
If the
event.btm_launch_item_add.item.item_type
log field value is equal to
0
then, the
target.application
UDM field is set to
USER_ITEM
.
Else, if
event.btm_launch_item_add.item.item_type
log field value is equal to
1
then, the
target.application
UDM field is set to
APP
.
Else, if
event.btm_launch_item_add.item.item_type
log field value is equal to
2
then, the
target.application
UDM field is set to
LOGIN_ITEM
.
Else, if
event.btm_launch_item_add.item.item_type
log field value is equal to
3
then, the
target.application
UDM field is set to
AGENT
.
Else, if
event.btm_launch_item_add.item.item_type
log field value is equal to
4
then, the
target.application
UDM field is set to
DAEMON
.
event.btm_launch_item_add.item.managed
additional.fields[btm_launch_item_add_item_managed]
event.btm_launch_item_add.item.legacy
additional.fields[btm_launch_item_add_item_legacy]
event_type: btm_launch_item_remove
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
btm_launch_item_remove
.
metadata.description
Apple's Background Task Manager notified that an item has been removed.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
PROCESS_TERMINATION
.
event.btm_launch_item_remove.instigator.audit_token.euid
principal.process.euid
event.btm_launch_item_remove.instigator.audit_token.ruid
principal.process.ruid
event.btm_launch_item_remove.instigator.audit_token.egid
principal.process.egid
event.btm_launch_item_remove.instigator.audit_token.rgid
principal.process.rgid
event.btm_launch_item_remove.instigator.audit_token.pgid
principal.process.pgid
event.btm_launch_item_remove.instigator.audit_token.pid
principal.process.pid
event.btm_launch_item_remove.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.btm_launch_item_remove.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.btm_launch_item_remove.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.btm_launch_item_remove.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.btm_launch_item_remove.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.btm_launch_item_remove.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.btm_launch_item_remove.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.btm_launch_item_remove.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.btm_launch_item_remove.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.btm_launch_item_remove.instigator.executable.path
principal.process.file.full_path
event.btm_launch_item_remove.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.btm_launch_item_remove.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.btm_launch_item_remove.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.btm_launch_item_remove.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.btm_launch_item_remove.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.btm_launch_item_remove.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.btm_launch_item_remove.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.btm_launch_item_remove.instigator.executable.stat.st_size
principal.process.file.size
event.btm_launch_item_remove.instigator.executable.sha256
principal.process.file.sha256
event.btm_launch_item_remove.instigator.executable.sha1
principal.process.file.sha1
event.btm_launch_item_remove.instigator.codesigning_flags
additional.fields[btm_launch_item_remove_instigator_codesigning_flags]
event.btm_launch_item_remove.instigator.cdhash
additional.fields[btm_launch_item_remove_instigator_cdhash]
event.btm_launch_item_remove.instigator.is_es_client
additional.fields[btm_launch_item_remove_instigator_is_es_client]
event.btm_launch_item_remove.instigator.group_id
additional.fields[btm_launch_item_remove_instigator_group_id]
event.btm_launch_item_remove.instigator.original_ppid
additional.fields[btm_launch_item_remove_instigator_original_ppid]
event.btm_launch_item_remove.instigator.session_id
additional.fields[btm_launch_item_remove_instigator_session_id]
event.btm_launch_item_remove.app.audit_token.euid
target.process.euid
event.btm_launch_item_remove.app.audit_token.ruid
target.process.ruid
event.btm_launch_item_remove.app.audit_token.egid
target.process.egid
event.btm_launch_item_remove.app.audit_token.rgid
target.process.rgid
event.btm_launch_item_remove.app.audit_token.pgid
target.process.pgid
event.btm_launch_item_remove.app.audit_token.pid
target.process.pid
event.btm_launch_item_remove.app.audit_token.uuid
target.process.product_specific_process_id
event.btm_launch_item_remove.app.audit_token.signing_id
target.process.file.signature_info.codesign.id
event.btm_launch_item_remove.app.parent_audit_token.euid
target.process.parent_process.euid
event.btm_launch_item_remove.app.parent_audit_token.ruid
target.process.parent_process.ruid
event.btm_launch_item_remove.app.parent_audit_token.egid
target.process.parent_process.egid
event.btm_launch_item_remove.app.parent_audit_token.rgid
target.process.parent_process.rgid
event.btm_launch_item_remove.app.parent_audit_token.pgid
target.process.parent_process.pgid
event.btm_launch_item_remove.app.parent_audit_token.pid
target.process.parent_process.pid
event.btm_launch_item_remove.app.parent_audit_token.uuid
target.process.parent_process.product_specific_process_id
event.btm_launch_item_remove.app.executable.path
target.process.file.full_path
event.btm_launch_item_remove.app.executable.stat.st_dev
target.process.file.stat_dev
event.btm_launch_item_remove.app.executable.stat.st_flags
target.process.file.stat_flags
event.btm_launch_item_remove.app.executable.stat.st_ino
target.process.file.stat_inode
event.btm_launch_item_remove.app.executable.stat.st_mode
target.process.file.stat_mode
event.btm_launch_item_remove.app.executable.stat.st_mtimespec
target.process.file.last_modification_time
event.btm_launch_item_remove.app.executable.stat.st_atimespec
target.process.file.last_access_time
event.btm_launch_item_remove.app.executable.stat.st_nlink
target.process.file.stat_nlink
event.btm_launch_item_remove.app.executable.stat.st_size
target.process.file.size
event.btm_launch_item_remove.app.executable.sha256
target.process.file.sha256
event.btm_launch_item_remove.app.executable.sha1
target.process.file.sha1
event.btm_launch_item_remove.app.signing_id
additional.fields[btm_launch_item_remove_app_signing_id]
event.btm_launch_item_remove.app.team_id
additional.fields[btm_launch_item_remove_app_team]
event.btm_launch_item_remove.app.ppid
additional.fields[btm_launch_item_remove_app_ppid]
event.btm_launch_item_remove.app.codesigning_flags
additional.fields[btm_launch_item_remove_app_codesigning_flags]
event.btm_launch_item_remove.app.cdhash
additional.fields[btm_launch_item_remove_app_cdhash]
event.btm_launch_item_remove.app.is_platform_binary
additional.fields[additional_fields[btm_launch_item_remove_app_cdhash]]
event.btm_launch_item_remove.app.is_es_client
additional.fields[additional_fields[btm_launch_item_remove_app_is_es_client]]
event.btm_launch_item_remove.app.group_id
target.process.pgid
event.btm_launch_item_remove.app.original_ppid
additional.fields[additional_fields[btm_launch_item_remove_app_original_ppid]]
event.btm_launch_item_remove.app.session_id
additional.fields[additional_fields[btm_launch_item_remove_app_session_id]]
event.btm_launch_item_remove.item.app_url
target.file.full_path
If the
event.btm_launch_item_remove.item.item_url
log field value is
not
empty
and if the
event.btm_launch_item_remove.item.item_url
log field value matches the regular expression pattern
/^file:./
or the
event.btm_launch_item_remove.item.item_url
log field value does not match the regular expression pattern
/^[a-zA-Z0-9]
then,
event.btm_launch_item_remove.item.item_url
log field is mapped to the
target.file.full_path
UDM field.
Else,
%{event.btm_launch_item_remove.item.app_url}%{event.btm_launch_item_remove.item.item_url}
log field is mapped to the
target.file.full_path
UDM field.
event.btm_launch_item_remove.item.item_url
target.file.full_path
If the
event.btm_launch_item_remove.item.item_url
log field value is
not
empty
and if the
event.btm_launch_item_remove.item.item_url
log field value matches the regular expression pattern
/^file:./
or the
event.btm_launch_item_remove.item.item_url
log field value does not match the regular expression pattern
/^[a-zA-Z0-9]
then,
event.btm_launch_item_remove.item.item_url
log field is mapped to the
target.file.full_path
UDM field.
Else,
%{event.btm_launch_item_remove.item.app_url}%{event.btm_launch_item_remove.item.item_url}
log field is mapped to the
target.file.full_path
UDM field.
event.btm_launch_item_remove.item.uid
target.user.userid
event.btm_launch_item_remove.executable_path
target.file.full_path
event.btm_launch_item_remove.item.item_type
target.application
If the
event.btm_launch_item_remove.item.item_type
log field value is equal to
0
then, the
target.application
UDM field is set to
USER_ITEM
.
Else, if
event.btm_launch_item_remove.item.item_type
log field value is equal to
1
then, the
target.application
UDM field is set to
APP
.
Else, if
event.btm_launch_item_remove.item.item_type
log field value is equal to
2
then, the
target.application
UDM field is set to
LOGIN_ITEM
.
Else, if
event.btm_launch_item_remove.item.item_type
log field value is equal to
3
then, the
target.application
UDM field is set to
AGENT
.
Else, if
event.btm_launch_item_remove.item.item_type
log field value is equal to
4
then, the
target.application
UDM field is set to
DAEMON
.
event.btm_launch_item_remove.item.managed
additional.fields[btm_launch_item_remove_item_managed]
event.btm_launch_item_remove.item.legacy
additional.fields[btm_launch_item_remove_item_legacy]
event.btm_launch_item_remove.app.parent_audit_token.signing_id
target.process.parent_process.file.signature_info.codesign.id
event_type: chroot
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
chroot
.
metadata.description
A piece of software has changed its apparent root directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
FILE_MODIFICATION
.
event.chroot.target.path
target.file.full_path
event.chroot.target.stat.st_dev
target.file.stat_dev
event.chroot.target.stat.st_flags
target.file.stat_flags
event.chroot.target.stat.st_ino
target.file.stat_inode
event.chroot.target.stat.st_mode
target.file.stat_mode
event.chroot.target.stat.st_mtimespec
target.file.last_modification_time
event.chroot.target.stat.st_atimespec
target.file.last_access_time
event.chroot.target.stat.st_nlink
target.file.stat_nlink
event.chroot.target.stat.st_size
target.file.size
event.chroot.target.sha256
target.file.sha256
event.chroot.target.sha1
target.file.sha1
event_type: exec
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
exec
.
metadata.description
An executable has been loaded into memory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
PROCESS_LAUNCH
.
process.responsible_audit_token.euid
principal.process.euid
process.responsible_audit_token.ruid
principal.process.ruid
process.responsible_audit_token.egid
principal.process.egid
process.responsible_audit_token.rgid
principal.process.rgid
process.responsible_audit_token.pgid
principal.process.pgid
process.responsible_audit_token.pid
principal.process.pid
process.responsible_audit_token.uuid
principal.process.product_specific_process_id
process.responsible_audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.exec.target.audit_token.euid
target.process.euid
event.exec.target.audit_token.ruid
target.process.ruid
event.exec.target.audit_token.egid
target.process.egid
event.exec.target.audit_token.rgid
target.process.rgid
event.exec.target.audit_token.pgid
target.process.pgid
event.exec.target.audit_token.pid
target.process.pid
event.exec.target.audit_token.uuid
target.process.product_specific_process_id
event.exec.target.parent_audit_token.euid
target.process.parent_process.euid
event.exec.target.parent_audit_token.ruid
target.process.parent_process.ruid
event.exec.target.parent_audit_token.egid
target.process.parent_process.egid
event.exec.target.parent_audit_token.rgid
target.process.parent_process.rgid
event.exec.target.parent_audit_token.pgid
target.process.parent_process.pgid
event.exec.target.parent_audit_token.pid
target.process.parent_process.pid
event.exec.target.parent_audit_token.uuid
target.process.parent_process.product_specific_process_id
event.exec.target.parent_audit_token.signing_id
target.process.parent_process.file.signature_info.codesign.id
event.exec.target.executable.path
target.process.file.full_path
event.exec.target.executable.stat.st_dev
target.process.file.stat_dev
event.exec.target.executable.stat.st_flags
target.process.file.stat_flags
event.exec.target.executable.stat.st_ino
target.process.file.stat_inode
event.exec.target.executable.stat.st_mode
target.process.file.stat_mode
event.exec.target.executable.stat.st_mtimespec
target.process.file.last_modification_time
event.exec.target.executable.stat.st_atimespec
target.process.file.last_access_time
event.exec.target.executable.stat.st_nlink
target.process.file.stat_nlink
event.exec.target.executable.stat.st_size
target.process.file.size
event.exec.target.executable.sha256
target.process.file.sha256
event.exec.target.executable.sha1
target.process.file.sha1
event.exec.target.signing_id
additional.fields[exec_target_signing_id]
event.exec.target.team_id
additional.fields[exec_target_team_id]
event.exec.target.ppid
additional.fields[exec_target_ppid]
event.exec.target.codesigning_flags
additional.fields[exec_target_codesigning_flags]
event.exec.target.cdhash
additional.fields[exec_target_cdhash]
event.exec.target.is_platform_binary
additional.fields[exec_target_is_platform_binary]
event.exec.target.is_es_client
additional.fields[exec_target_is_es_client]
event.exec.target.group_id
target.process.pgid
event.exec.target.original_ppid
additional.fields[exec_target_original_ppid]
event.exec.target.session_id
additional.fields[exec_target_session_id]
event.exec.args
target.process.command_line
event.exec.cwd.path
additional.fields[exec_cwd_path]
event.exec.dyld_exec_path
additional.fields[exec_dyld_exec_path]
event.exec.script.path
additional.fields[exec_script_path]
event.exec.tty.path
additional.fields[exec_tty_path]
event.exec.image_cpusubtype
additional.fields[exec_image_cpusubtype]
event.exec.image_cputype
additional.fields[exec_image_cputype]
event.exec.target.audit_token.signing_id
target.process.file.signature_info.codesign.id
event_type: file_collection
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
file_collection
.
metadata.description
Event occurs when data from a Diagnsostic or Crash Report file is collected from the system.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.file_collection.path
target.file.path
event.file_collection.size
target.file.size
event.file_collection.contents
additional.fields[file_collection_contents]
event_type: kextload
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
kextload
.
metadata.description
A kernel extension (kext) was loaded.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.kextload.identifier
target.resource.name
event_type: kextunload
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
kextunload
.
metadata.description
A kernel extension (kext) was unloaded.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.kextunload.identifier
target.resource.name
event_type: log_collection
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
log_collection
.
metadata.description
Collection of entries from a local log file.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.log_collection.texts
target.file.names
event.log_collection.path.0
target.file.full_path
event_type: login_login
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
login_login
.
metadata.description
A user attempted to log in via /usr/bin/login.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.login_login.uid
target.user.userid
event.login_login.username
target.user.user_display_name
event.login_login.success
security_result.category
If the
event.login_login.success
log field value is equal to
false
then, the
security_result.category
UDM field is set to
AUTH_VIOLATION
.
event.login_login.failure_message
security_result.category_details
If the
event.login_login.success
log field value is equal to
false
then,
event.login_login.failure_message
log field is mapped to the
security_result.category_details
UDM field.
event_type: login_logout
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
login_logout
.
metadata.description
A user logged out via /usr/bin/login.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGOUT
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.login_logout.uid
target.user.userid
event.login_logout.username
target.user.user_display_name
event_type: lw_session_login
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
lw_session_login
.
metadata.description
A user has logged in via the Login Window.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.lw_session_login.username
target.user.user_display_name
event_type: bios_uefi
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
bios_uefi
.
metadata.description
Information about the current version of bios and uefi on the device.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.bios_uefi.firmware-version
additional.fields[bios_uefi_firmware_version]
event.bios_uefi.system-firmware-version
additional.fields[bios_uefi_system_firmware_version]
event.bios_uefi.architecture
additional.fields[bios_uefi_architecture]
event.bios_uefi.bios.firmware-version
additional.fields[bios_uefi_bios_firmware_version]
event.bios_uefi.bios.vendor
additional.fields[bios_uefi_bios_vendor]
event.bios_uefi.bios.firmware-features
additional.fields[bios_uefi_bios_firmware_features]
event.bios_uefi.bios.rom-size
additional.fields[bios_uefi_bios_rom_size]
event.bios_uefi.bios.booter-version
additional.fields[bios_uefi_bios_booter_version]
event_type: cs_invalidated
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
cs_invalidated
.
metadata.description
A process has had its code signature marked as invalid.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event_type: gatekeeper_user_override
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
gatekeeper_user_override
.
metadata.description
A user overrides Gatekeeper.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.gatekeeper_user_override.file.path
target.file.full_path
event.gatekeeper_user_override.file.stat.st_dev
target.file.stat_dev
event.gatekeeper_user_override.file.stat.st_flags
target.file.stat_flags
event.gatekeeper_user_override.file.stat.st_ino
target.file.stat_inode
event.gatekeeper_user_override.file.stat.st_mode
target.file.stat_mode
event.gatekeeper_user_override.file.stat.st_mtimespec
target.file.last_modification_time
event.gatekeeper_user_override.file.stat.st_atimespec
target.file.last_access_time
event.gatekeeper_user_override.file.stat.st_nlink
target.file.stat_nlink
event.gatekeeper_user_override.file.stat.st_size
target.file.size
event.gatekeeper_user_override.file.sha256
target.file.sha256
event.gatekeeper_user_override.file.sha1
target.file.sha1
event.gatekeeper_user_override.signing_info.signing_id
additional.fields[exec_gatekeeper_user_override_signing_info_signing_id]
event.gatekeeper_user_override.signing_info.team_id
additional.fields[gatekeeper_user_override_signing_info_team_id]
event.gatekeeper_user_override.signing_info.cdhash
additional.fields[gatekeeper_user_override_signing_info_cdhash]
event.gatekeeper_user_override.file_type
additional.fields[gatekeeper_user_override_file_type]
event.gatekeeper_user_override.sha256
additional.fields[gatekeeper_user_override_sha256]
event_type: lw_session_unlock
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
lw_session_unlock
.
metadata.description
A user has unlocked the screen from the Login Window.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.lw_session_unlock.username
target.user.user_display_name
event_type:  lw_session_lock
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
lw_session_lock
.
metadata.description
A user has locked the screen.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGOUT
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.lw_session_lock.username
target.user.user_display_name
event_type: lw_session_logout
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
lw_session_logout
.
metadata.description
A user has logged out of an active graphical session.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGOUT
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
MACHINE
.
event.lw_session_logout.username
target.user.user_display_name
event_type: mount
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
mount
.
metadata.description
A file system has been mounted.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.mount.statfs.f_owner
principal.user.userid
event.mount.device.size
target.file.size
event.mount.statfs.f_fstypename
target.resource.resource_subtype
event.mount.statfs.f_mntfromname
src.resource.name
event.mount.statfs.f_mntonname
target.resource.name
event.mount.device.protocol
additional.fields[mount_device_protocol]
event.mount.disposition
additional.fields[mount_disposition]
event.mount.device.serial_number
target.asset.hardware.serial_number
If the
event.mount.device.serial_number
log field value is
not
empty
or the
event.mount.device.vendor_name
log field value is
not
empty
or the
event.mount.device.device_model
log field value is
not
empty
then,
event.mount.device.serial_number
log field is mapped to the
target.asset.hardware.serial_number
UDM field.
event.mount.device.vendor_name
target.asset.hardware.manufacturer
If the
event.mount.device.serial_number
log field value is
not
empty
or the
event.mount.device.vendor_name
log field value is
not
empty
or the
event.mount.device.device_model
log field value is
not
empty
then,
event.mount.device.vendor_name
log field is mapped to the
target.asset.hardware.manufacturer
UDM field.
event.mount.device.device_model
target.asset.hardware.model
If the
event.mount.device.serial_number
log field value is
not
empty
or the
event.mount.device.vendor_name
log field value is
not
empty
or the
event.mount.device.device_model
log field value is
not
empty
then,
event.mount.device.device_model
log field is mapped to the
target.asset.hardware.model
UDM field.
event_type: od_attribute_set
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_attribute_set
.
metadata.description
Attribute set on user or group using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
event.od_attribute_set.instigator.audit_token.euid
principal.process.euid
event.od_attribute_set.instigator.audit_token.ruid
principal.process.ruid
event.od_attribute_set.instigator.audit_token.egid
principal.process.egid
event.od_attribute_set.instigator.audit_token.rgid
principal.process.rgid
event.od_attribute_set.instigator.audit_token.pgid
principal.process.pgid
event.od_attribute_set.instigator.audit_token.pid
principal.process.pid
event.od_attribute_set.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_attribute_set.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_attribute_set.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_attribute_set.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_attribute_set.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_attribute_set.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_attribute_set.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_attribute_set.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_attribute_set.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_attribute_set.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_attribute_set.instigator.executable.path
principal.process.file.full_path
event.od_attribute_set.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_attribute_set.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_attribute_set.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_attribute_set.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_attribute_set.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_attribute_set.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_attribute_set.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_attribute_set.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_attribute_set.instigator.executable.stat.st_size
principal.process.file.size
event.od_attribute_set.instigator.executable.sha256
principal.process.file.sha256
event.od_attribute_set.instigator.executable.sha1
principal.process.file.sha1
event.od_attribute_set.instigator.signing_id
additional.fields[od_attribute_set_instigator_signing_id]
event.od_attribute_set.instigator.team_id
additional.fields[od_attribute_set_instigator_team_id]
event.od_attribute_set.instigator.ppid
additional.fields[od_attribute_set_instigator_codesigning_flags]
event.od_attribute_set.instigator.codesigning_flags
additional.fields[od_attribute_set_instigator_ppid]
event.od_attribute_set.instigator.cdhash
additional.fields[od_attribute_set_instigator_cdhash]
event.od_attribute_set.instigator.is_platform_binary
additional.fields[od_attribute_set_instigator_is_platform_binary]
event.od_attribute_set.instigator.is_es_client
additional.fields[od_attribute_set_instigator_is_es_client]
event.od_attribute_set.instigator.group_id
principal.process.pgid
event.od_attribute_set.instigator.original_ppid
additional.fields[od_attribute_set_instigator_original_ppid]
event.od_attribute_set.instigator.session_id
additional.fields[od_attribute_set_instigator_session_id]
event.od_attribute_set.attribute_name
target.resource.resource_subtype
event.od_attribute_value_add.attribute_value
target.resource.name
event.od_attribute_set.record_name
target.user.user_display_name
event.od_attribute_set.instigator_token.euid
principal.user.userid
event.od_attribute_set.db_path
additional.fields[event_od_attribute_set_db_path]
event.od_attribute_set.node_name
additional.fields[event_od_attribute_set_node_name]
event.od_attribute_set.record_type
additional.fields[event_od_attribute_set_record_type]
event.od_attribute_set.error_code
additional.fields[event_od_attribute_set_error_code]
event_type: od_attribute_value_add
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_attribute_value_add
.
metadata.description
Attribute set on user or group using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.od_attribute_value_add.instigator.audit_token.euid
principal.process.euid
event.od_attribute_value_add.instigator.audit_token.ruid
principal.process.ruid
event.od_attribute_value_add.instigator.audit_token.egid
principal.process.egid
event.od_attribute_value_add.instigator.audit_token.rgid
principal.process.rgid
event.od_attribute_value_add.instigator.audit_token.pgid
principal.process.pgid
event.od_attribute_value_add.instigator.audit_token.pid
principal.process.pid
event.od_attribute_value_add.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_attribute_value_add.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_attribute_value_add.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_attribute_value_add.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_attribute_value_add.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_attribute_value_add.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_attribute_value_add.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_attribute_set.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_attribute_value_add.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_attribute_value_add.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_attribute_value_add.instigator.executable.path
principal.process.file.full_path
event.od_attribute_value_add.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_attribute_value_add.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_attribute_value_add.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_attribute_value_add.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_attribute_value_add.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_attribute_value_add.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_attribute_value_add.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_attribute_value_add.instigator.executable.stat.st_size
principal.process.file.size
event.od_attribute_value_add.instigator.executable.sha256
principal.process.file.sha256
event.od_attribute_value_add.instigator.executable.sha1
principal.process.file.sha1
event.od_attribute_value_add.instigator.signing_id
additional.fields[od_attribute_value_add_instigator_signing_id]
event.od_attribute_value_add.instigator.team_id
additional.fields[od_attribute_value_add_instigator_team_id]
event.od_attribute_value_add.instigator.ppid
additional.fields[od_attribute_value_add_instigator_ppid]
event.od_attribute_value_add.instigator.codesigning_flags
additional.fields[od_attribute_set_instigator_codesigning_flags]
event.od_attribute_value_add.instigator.cdhash
additional.fields[od_attribute_value_add_instigator_codesigning_flags]
event.od_attribute_value_add.instigator.is_platform_binary
additional.fields[od_attribute_set_instigator_is_platform_binary]
event.od_attribute_value_add.instigator.is_es_client
additional.fields[od_attribute_value_add_instigator_is_es_client]
event.od_attribute_value_add.instigator.group_id
principal.process.pgid
event.od_attribute_value_add.instigator.original_ppid
additional.fields[od_attribute_value_add_instigator_original_pp]
event.od_attribute_value_add.instigator.session_id
additional.fields[od_attribute_value_add_instigator_session_id]
event.od_attribute_value_add.attribute_name
target.resource.resource_subtype
event.od_attribute_value_add.attribute_value
target.resource.name
event.od_attribute_value_add.record_name
target.user.user_display_name
event.od_attribute_value_add.db_path
additional.fields[od_attribute_value_add_db_path]
event.od_attribute_value_add.node_name
additional.fields[od_attribute_value_add_node_name]
event.od_attribute_value_add.record_type
additional.fields[od_attribute_value_add_record_type]
event.od_attribute_value_add.error_code
additional.fields[od_attribute_value_add_error_code]
event_type: od_attribute_value_remove
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_attribute_value_remove
.
metadata.description
Attribute removed from a user or group using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_RESOURCE_DELETION
.
event.od_attribute_value_remove.instigator.audit_token.euid
principal.process.euid
event.od_attribute_value_remove.instigator.audit_token.ruid
principal.process.ruid
event.od_attribute_value_remove.instigator.audit_token.egid
principal.process.egid
event.od_attribute_value_remove.instigator.audit_token.rgid
principal.process.rgid
event.od_attribute_value_remove.instigator.audit_token.pgid
principal.process.pgid
event.od_attribute_value_remove.instigator.audit_token.pid
principal.process.pid
event.od_attribute_value_remove.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_attribute_value_remove.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_attribute_value_remove.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_attribute_value_remove.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_attribute_value_remove.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_attribute_value_remove.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_attribute_value_remove.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_attribute_value_remove.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_attribute_value_remove.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_attribute_value_remove.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_attribute_value_remove.instigator.executable.path
principal.process.file.full_path
event.od_attribute_value_remove.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_attribute_value_remove.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_attribute_value_remove.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_attribute_value_remove.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_attribute_value_remove.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_attribute_value_remove.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_attribute_value_remove.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_attribute_value_remove.instigator.executable.stat.st_size
principal.process.file.size
event.od_attribute_value_remove.instigator.executable.sha256
principal.process.file.sha256
event.od_attribute_value_remove.instigator.executable.sha1
principal.process.file.sha1
event.od_attribute_value_remove.instigator.codesigning_flags
additional.fields[od_attribute_value_remove_instigator_codesigning_flags]
event.od_attribute_value_remove.instigator.cdhash
additional.fields[od_attribute_value_remove_instigator_codesigning_flags]
event.od_attribute_value_remove.instigator.is_platform_binary
additional.fields[od_attribute_value_remove_instigator_is_platform_binary]
event.od_attribute_value_remove.instigator.is_es_client
additional.fields[od_attribute_value_remove_instigator_is_es_client]
event.od_attribute_value_remove.instigator.group_id
principal.process.pgid
event.od_attribute_value_remove.instigator.original_ppid
additional.fields[od_attribute_value_remove_instigator_original_pp]
event.od_attribute_value_remove.instigator.session_id
additional.fields[od_attribute_value_remove_instigator_session_id]
event.od_attribute_value_remove.attribute_name
target.resource.resource_subtype
event.od_attribute_value_remove.attribute_value
target.resource.name
event.od_attribute_value_remove.record_name
target.user.user_display_name
event.od_attribute_value_remove.db_path
additional.fields[od_attribute_value_remove_db_path]
event.od_attribute_value_remove.node_name
additional.fields[od_attribute_value_remove_node_name]
event.od_attribute_value_remove.record_type
additional.fields[od_attribute_value_remove_record_type]
event.od_attribute_value_remove.error_code
additional.fields[od_attribute_value_remove_error_code]
event_type: od_create_group
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_create_group
.
metadata.description
A group has been created using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
GROUP_CREATION
.
event.od_create_group.instigator.audit_token.euid
principal.process.euid
event.od_create_group.instigator.audit_token.ruid
principal.process.ruid
event.od_create_group.instigator.audit_token.egid
principal.process.egid
event.od_create_group.instigator.audit_token.rgid
principal.process.rgid
event.od_create_group.instigator.audit_token.pgid
principal.process.pgid
event.od_create_group.instigator.audit_token.pid
principal.process.pid
event.od_create_group.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_create_group.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_create_group.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_create_group.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_create_group.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_create_group.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_create_group.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_create_group.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_create_group.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_create_group.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_create_group.instigator.executable.path
principal.process.file.full_path
event.od_create_group.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_create_group.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_create_group.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_create_group.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_create_group.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_create_group.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_create_group.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_create_group.instigator.executable.stat.st_size
principal.process.file.size
event.od_create_group.instigator.executable.sha256
principal.process.file.sha256
event.od_create_group.instigator.executable.sha1
principal.process.file.sha1
event.od_create_group.instigator.signing_id
additional.fields[od_create_group_instigator_signing_id]
event.od_create_group.instigator.team_id
additional.fields[od_create_group_instigator_team_id]
event.od_create_group.instigator.ppid
additional.fields[od_create_group_instigator_ppid]
event.od_create_group.instigator.codesigning_flags
additional.fields[od_create_group_instigator_codesigning_flags]
event.od_create_group.instigator.cdhash
additional.fields[od_create_group_instigator_cdhash]
event.od_create_group.instigator.is_platform_binary
additional.fields[od_create_group_instigator_is_platform_binary]
event.od_create_group.instigator.is_es_client
additional.fields[od_create_group_instigator_is_es_client]
event.od_create_group.instigator.group_id
principal.process.pgid
event.od_create_group.instigator.original_ppid
additional.fields[od_create_group_instigator_original_pp]
event.od_create_group.instigator.session_id
additional.fields[od_create_group_instigator_session_id]
event.od_create_group.group_name
target.group.group_display_name
event.od_create_group.instigator_token.euid
principal.user.userid
od_create_group.db_path
additional.fields[od_create_group_db_path]
event.od_create_group.node_name
additional.fields[od_create_group_node_name]
event.od_create_group.error_code
additional.fields[od_create_group_error_code]
event_type: od_delete_group
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_delete_group
.
metadata.description
A group has been deleted using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
GROUP_DELETION
.
event.od_delete_group.instigator.audit_token.euid
principal.process.euid
event.od_delete_group.instigator.audit_token.ruid
principal.process.ruid
event.od_delete_group.instigator.audit_token.egid
principal.process.egid
event.od_delete_group.instigator.audit_token.rgid
principal.process.rgid
event.od_delete_group.instigator.audit_token.pgid
principal.process.pgid
event.od_delete_group.instigator.audit_token.pid
principal.process.pid
event.od_delete_group.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_delete_group.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_delete_group.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_delete_group.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_delete_group.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_delete_group.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_delete_group.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_delete_group.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_delete_group.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_delete_group.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_delete_group.instigator.executable.path
principal.process.file.full_path
event.od_delete_group.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_delete_group.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_delete_group.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_delete_group.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_delete_group.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_delete_group.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_delete_group.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_delete_group.instigator.executable.stat.st_size
principal.process.file.size
event.od_delete_group.instigator.executable.sha256
principal.process.file.sha256
event.od_delete_group.instigator.executable.sha1
principal.process.file.sha1
event.od_delete_group.instigator.signing_id
additional.fields[od_delete_group_instigator_signing_id]
event.od_delete_group.instigator.team_id
additional.fields[od_delete_group_instigator_team_id]
event.od_delete_group.instigator.ppid
additional.fields[od_delete_group_instigator_ppid]
event.od_delete_group.instigator.codesigning_flags
additional.fields[od_delete_group_instigator_codesigning_flags]
event.od_delete_group.instigator.cdhash
additional.fields[od_delete_group_instigator_cdhash]
event.od_delete_group.instigator.is_platform_binary
additional.fields[od_delete_group_instigator_is_platform_binary]
event.od_delete_group.instigator.is_es_client
additional.fields[od_delete_group_instigator_is_es_client]
event.od_delete_group.instigator.group_id
principal.process.pgid
event.od_delete_group.instigator.original_ppid
additional.fields[od_delete_group_instigator_original_pp]
event.od_delete_group.instigator.session_id
additional.fields[od_delete_group_instigator_session_id]
event.od_delete_group.group_name
target.group.group_display_name
event.od_delete_group.instigator_token.euid
principal.user.userid
od_delete_group.db_path
additional.fields[od_delete_group_db_path]
event.od_delete_group.node_name
additional.fields[od_delete_group_node_name]
event.od_delete_group.error_code
additional.fields[od_delete_group_error_code]
event_type: od_create_user
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_create_user
.
metadata.description
A user has been created using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_CREATION
.
event.od_create_user.instigator.audit_token.euid
principal.process.euid
event.od_create_user.instigator.audit_token.ruid
principal.process.ruid
event.od_create_user.instigator.audit_token.egid
principal.process.egid
event.od_create_user.instigator.audit_token.rgid
principal.process.rgid
event.od_create_user.instigator.audit_token.pgid
principal.process.pgid
event.od_create_user.instigator.audit_token.pid
principal.process.pid
event.od_create_user.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_create_user.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_create_user.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_create_user.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_create_user.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_create_user.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_create_user.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_create_user.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_create_user.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_create_user.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_create_user.instigator.executable.path
principal.process.file.full_path
event.od_create_user.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_create_user.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_create_user.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_create_user.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_create_user.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_create_user.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_create_user.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_create_user.instigator.executable.stat.st_size
principal.process.file.size
event.od_create_user.instigator.executable.sha256
principal.process.file.sha256
event.od_create_user.instigator.executable.sha1
principal.process.file.sha1
event.od_create_user.instigator.signing_id
additional.fields[od_create_user_instigator_signing_id]
event.od_create_user.instigator.team_id
additional.fields[od_create_user_instigator_team_id]
event.od_create_user.instigator.ppid
additional.fields[od_create_user_instigator_ppid]
event.od_create_user.instigator.codesigning_flags
additional.fields[od_create_user_instigator_codesigning_flags]
event.od_create_user.instigator.cdhash
additional.fields[od_create_user_instigator_cdhash]
event.od_create_user.instigator.is_platform_binary
additional.fields[od_create_user_instigator_is_platform_binary]
event.od_create_user.instigator.is_es_client
additional.fields[od_create_user_instigator_is_es_client]
event.od_create_user.instigator.group_id
principal.process.pgid
event.od_create_user.instigator.original_ppid
additional.fields[od_create_user_instigator_original_pp]
event.od_create_user.instigator.session_id
additional.fields[od_create_user_instigator_session_id]
event.od_create_user.user_name
target.user.userid
event.od_create_user.instigator_token.euid
principal.user.userid
event.od_create_user.db_path
additional.fields[od_create_user_db_path]
event.od_create_user.node_name
additional.fields[od_create_user_node_name]
event.od_create_user.error_code
additional.fields[od_create_user_error_code]
event_type: od_delete_user
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_delete_user
.
metadata.description
A user has been deleted using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_DELETION
.
event.od_delete_user.instigator.audit_token.euid
principal.process.euid
event.od_delete_user.instigator.audit_token.ruid
principal.process.ruid
event.od_delete_user.instigator.audit_token.egid
principal.process.egid
event.od_delete_user.instigator.audit_token.rgid
principal.process.rgid
event.od_delete_user.instigator.audit_token.pgid
principal.process.pgid
event.od_delete_user.instigator.audit_token.pid
principal.process.pid
event.od_delete_user.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_delete_user.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_delete_user.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_delete_user.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_delete_user.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_delete_user.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_delete_user.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_delete_user.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_delete_user.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_delete_user.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_delete_user.instigator.executable.path
principal.process.file.full_path
event.od_delete_user.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_delete_user.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_delete_user.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_delete_user.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_delete_user.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_delete_user.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_delete_user.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_delete_user.instigator.executable.stat.st_size
principal.process.file.size
event.od_delete_user.instigator.executable.sha256
principal.process.file.sha256
event.od_delete_user.instigator.executable.sha1
principal.process.file.sha1
event.od_delete_user.instigator.signing_id
additional.fields[od_delete_user_instigator_signing_id]
event.od_delete_user.instigator.team_id
additional.fields[od_delete_user_instigator_team_id]
event.od_delete_user.instigator.ppid
additional.fields[od_delete_user_instigator_ppid]
event.od_delete_user.instigator.codesigning_flags
additional.fields[od_delete_user_instigator_codesigning_flags]
event.od_delete_user.instigator.cdhash
additional.fields[od_delete_user_instigator_cdhash]
event.od_delete_user.instigator.is_platform_binary
additional.fields[od_delete_user_instigator_is_platform_binary]
event.od_delete_user.instigator.is_es_client
additional.fields[od_delete_user_instigator_is_es_client]
event.od_delete_user.instigator.group_id
principal.process.pgid
event.od_delete_user.instigator.original_ppid
additional.fields[od_delete_user_instigator_original_pp]
event.od_delete_user.instigator.session_id
additional.fields[od_delete_user_instigator_session_id]
event.od_delete_user.user_name
target.user.userid
event.od_delete_user.instigator_token.euid
principal.user.userid
event.od_delete_user.db_path
additional.fields[od_delete_user_db_path]
event.od_delete_user.node_name
additional.fields[od_delete_user_node_name]
event.od_delete_user.error_code
additional.fields[od_delete_user_error_code]
event.od_disable_user.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event_type: od_disable_user
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_disable_user
.
metadata.description
A user has been disabled using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
event.od_disable_user.instigator.audit_token.euid
principal.process.euid
event.od_disable_user.instigator.audit_token.ruid
principal.process.ruid
event.od_disable_user.instigator.audit_token.egid
principal.process.egid
event.od_disable_user.instigator.audit_token.rgid
principal.process.rgid
event.od_disable_user.instigator.audit_token.pgid
principal.process.pgid
event.od_disable_user.instigator.audit_token.pid
principal.process.pid
event.od_disable_user.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_disable_user.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_disable_user.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_disable_user.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_disable_user.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_disable_user.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_disable_user.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_disable_user.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_disable_user.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_disable_user.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_disable_user.instigator.executable.path
principal.process.file.full_path
event.od_disable_user.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_disable_user.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_disable_user.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_disable_user.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_disable_user.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_disable_user.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_disable_user.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_disable_user.instigator.executable.stat.st_size
principal.process.file.size
event.od_disable_user.instigator.executable.sha256
principal.process.file.sha256
event.od_disable_user.instigator.executable.sha1
principal.process.file.sha1
event.od_disable_user.instigator.codesigning_flags
additional.fields[od_disable_user_instigator_codesigning_flags]
event.od_disable_user.instigator.cdhash
additional.fields[od_disable_user_instigator_codesigning_flags]
event.od_disable_user.instigator.is_platform_binary
additional.fields[od_disable_user_instigator_is_platform_binary]
event.od_disable_user.instigator.is_es_client
additional.fields[od_disable_user_instigator_is_es_client]
event.od_disable_user.instigator.group_id
principal.process.pgid
event.od_disable_user.instigator.original_ppid
additional.fields[od_disable_user_instigator_original_pp]
event.od_disable_user.instigator.session_id
additional.fields[od_disable_user_instigator_session_id]
event.od_disable_user.user_name
target.user.user_display_name
event.od_disable_user.instigator_token.euid
principal.user.userid
event.od_disable_user.db_path
additional.fields[od_disable_user_db_path]
event.od_disable_user.node_name
additional.fields[od_disable_user_node_name]
event.od_disable_user.error_code
additional.fields[od_disable_user_error_code]
event_type: od_enable_user
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_enable_user
.
metadata.description
A user has been enabled using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
event.od_enable_user.instigator.audit_token.euid
principal.process.euid
event.od_enable_user.instigator.audit_token.ruid
principal.process.ruid
event.od_enable_user.instigator.audit_token.egid
principal.process.egid
event.od_enable_user.instigator.audit_token.rgid
principal.process.rgid
event.od_enable_user.instigator.audit_token.pgid
principal.process.pgid
event.od_enable_user.instigator.audit_token.pid
principal.process.pid
event.od_enable_user.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_enable_user.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_enable_user.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_enable_user.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_enable_user.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_enable_user.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_enable_user.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_enable_user.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_enable_user.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_enable_user.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_enable_user.instigator.executable.path
principal.process.file.full_path
event.od_enable_user.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_enable_user.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_enable_user.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_enable_user.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_enable_user.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_enable_user.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_enable_user.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_enable_user.instigator.executable.stat.st_size
principal.process.file.size
event.od_enable_user.instigator.executable.sha256
principal.process.file.sha256
event.od_enable_user.instigator.executable.sha1
principal.process.file.sha1
event.od_enable_user.instigator.signing_id
additional.fields[od_enable_user_instigator_signing_id]
event.od_enable_user.instigator.team_id
additional.fields[od_enable_user_instigator_team_id]
event.od_enable_user.instigator.ppid
additional.fields[od_enable_user_instigator_ppid]
event.od_enable_user.instigator.codesigning_flags
additional.fields[od_enable_user_instigator_codesigning_flags]
event.od_enable_user.instigator.cdhash
additional.fields[od_enable_user_instigator_cdhash]
event.od_enable_user.instigator.is_platform_binary
additional.fields[od_enable_user_instigator_is_platform_binary]
event.od_enable_user.instigator.is_es_client
additional.fields[od_enable_user_instigator_is_es_client]
event.od_enable_user.instigator.group_id
principal.process.pgid
event.od_enable_user.instigator.original_ppid
additional.fields[od_enable_user_instigator_original_pp]
event.od_enable_user.instigator.session_id
additional.fields[od_enable_user_instigator_session_id]
event.od_enable_user.user_name
target.user.user_display_name
event.od_enable_user.instigator_token.euid
principal.user.userid
event.od_enable_user.db_path
additional.fields[od_enable_user_db_path]
event.od_enable_user.node_name
additional.fields[od_enable_user_node_name]
event.od_enable_user.error_code
additional.fields[od_enable_user_error_code]
event_type: od_group_add
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_group_add
.
metadata.description
A member has been added to a group using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
GROUP_MODIFICATION
.
event.od_group_add.instigator.audit_token.euid
principal.process.euid
event.od_group_add.instigator.audit_token.ruid
principal.process.ruid
event.od_group_add.instigator.audit_token.egid
principal.process.egid
event.od_group_add.instigator.audit_token.rgid
principal.process.rgid
event.od_group_add.instigator.audit_token.pgid
principal.process.pgid
event.od_group_add.instigator.audit_token.pid
principal.process.pid
event.od_group_add.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_group_add.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_group_add.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_group_add.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_group_add.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_group_add.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_group_add.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_group_add.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_group_add.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_group_add.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_group_add.instigator.executable.path
principal.process.file.full_path
event.od_group_add.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_group_add.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_group_add.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_group_add.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_group_add.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_group_add.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_group_add.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_group_add.instigator.executable.stat.st_size
principal.process.file.size
event.od_group_add.instigator.executable.sha256
principal.process.file.sha256
event.od_group_add.instigator.executable.sha1
principal.process.file.sha1
event.od_group_add.instigator.signing_id
additional.fields[od_group_add_instigator_signing_id]
event.od_group_add.instigator.team_id
additional.fields[od_group_add_instigator_team_id]
event.od_group_add.instigator.ppid
additional.fields[od_group_add_instigator_ppid]
event.od_group_add.instigator.codesigning_flags
additional.fields[od_group_add_instigator_codesigning_flags]
event.od_group_add.instigator.cdhash
additional.fields[od_group_add_instigator_cdhash]
event.od_group_add.instigator.is_platform_binary
additional.fields[od_group_add_instigator_is_platform_binary]
event.od_group_add.instigator.is_es_client
additional.fields[od_group_add_instigator_is_es_client]
event.od_group_add.instigator.group_id
principal.process.pgid
event.od_group_add.instigator.original_ppid
additional.fields[od_group_add_instigator_original_pp]
event.od_group_add.instigator.session_id
additional.fields[od_group_add_instigator_session_id]
event.od_group_add.group_name
target.group.group_display_name
event.od_group_add.member.member_value
target.user.user_display_name
event.od_group_add.instigator_token.euid
principal.user.userid
event.od_group_add.db_path
additional.fields[od_group_add_db_path]
event.od_group_add.node_name
additional.fields[od_group_add_node_name]
event.od_group_add.error_code
additional.fields[od_group_add_error_code]
event_type: od_group_remove
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_group_remove
.
metadata.description
A member has been removed from a group using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
GROUP_MODIFICATION
.
event.od_group_remove.instigator.audit_token.euid
principal.process.euid
event.od_group_remove.instigator.audit_token.ruid
principal.process.ruid
event.od_group_remove.instigator.audit_token.egid
principal.process.egid
event.od_group_remove.instigator.audit_token.rgid
principal.process.rgid
event.od_group_remove.instigator.audit_token.pgid
principal.process.pgid
event.od_group_remove.instigator.audit_token.pid
principal.process.pid
event.od_group_remove.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_group_remove.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_group_remove.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_group_remove.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_group_remove.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_group_remove.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_group_remove.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_group_remove.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_group_remove.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_group_remove.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_group_remove.instigator.executable.path
principal.process.file.full_path
event.od_group_remove.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_group_remove.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_group_remove.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_group_remove.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_group_remove.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_group_remove.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_group_remove.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_group_remove.instigator.executable.stat.st_size
principal.process.file.size
event.od_group_remove.instigator.executable.sha256
principal.process.file.sha256
event.od_group_remove.instigator.executable.sha1
principal.process.file.sha1
event.od_group_remove.instigator.signing_id
additional.fields[od_group_remove_instigator_signing_id]
event.od_group_remove.instigator.team_id
additional.fields[od_group_remove_instigator_team_id]
event.od_group_remove.instigator.ppid
additional.fields[od_group_remove_instigator_ppid]
event.od_group_remove.instigator.codesigning_flags
additional.fields[od_group_remove_instigator_codesigning_flags]
event.od_group_remove.instigator.cdhash
additional.fields[od_group_remove_instigator_cdhash]
event.od_group_remove.instigator.is_platform_binary
additional.fields[od_group_remove_instigator_is_platform_binary]
event.od_group_remove.instigator.is_es_client
additional.fields[od_group_remove_instigator_is_es_client]
event.od_group_remove.instigator.group_id
principal.process.pgid
event.od_group_remove.instigator.original_ppid
additional.fields[od_group_remove_instigator_original_pp]
event.od_group_remove.instigator.session_id
additional.fields[od_group_remove_instigator_session_id]
event.od_group_remove.group_name
target.group.group_display_name
event.od_group_remove.member.member_value
target.user.user_display_name
event.od_group_remove.instigator_token.euid
principal.user.userid
event.od_group_remove.db_path
additional.fields[od_group_remove_db_path]
event.od_group_remove.node_name
additional.fields[od_group_remove_node_name]
event.od_group_remove.error_code
additional.fields[od_group_remove_error_code]
event_type: od_group_set
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_group_set
.
metadata.description
A group has a member initialized or replaced using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
GROUP_MODIFICATION
.
event.od_group_set.instigator.audit_token.euid
principal.process.euid
event.od_group_set.instigator.audit_token.ruid
principal.process.ruid
event.od_group_set.instigator.audit_token.egid
principal.process.egid
event.od_group_set.instigator.audit_token.rgid
principal.process.rgid
event.od_group_set.instigator.audit_token.pgid
principal.process.pgid
event.od_group_set.instigator.audit_token.pid
principal.process.pid
event.od_group_set.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_group_set.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_group_set.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_group_set.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_group_set.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_group_set.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_group_set.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_group_set.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_group_set.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_group_set.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_group_set.instigator.executable.path
principal.process.file.full_path
event.od_group_set.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_group_set.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_group_set.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_group_set.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_group_set.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_group_set.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_group_set.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_group_set.instigator.executable.stat.st_size
principal.process.file.size
event.od_group_set.instigator.executable.sha256
principal.process.file.sha256
event.od_group_set.instigator.executable.sha1
principal.process.file.sha1
event.od_group_set.instigator.signing_id
additional.fields[od_group_set_instigator_signing_id]
event.od_group_set.instigator.team_id
additional.fields[od_group_set_instigator_team_id]
event.od_group_set.instigator.ppid
additional.fields[od_group_set_instigator_ppid]
event.od_group_set.instigator.codesigning_flags
additional.fields[od_group_set_instigator_codesigning_flags]
event.od_group_set.instigator.cdhash
additional.fields[od_group_set_instigator_cdhash]
event.od_group_set.instigator.is_platform_binary
additional.fields[od_group_set_instigator_is_platform_binary]
event.od_group_set.instigator.is_es_client
additional.fields[od_group_set_instigator_is_es_client]
event.od_group_set.instigator.group_id
principal.process.pgid
event.od_group_set.instigator.original_ppid
additional.fields[od_group_set_instigator_original_pp]
event.od_group_set.instigator.session_id
additional.fields[od_group_set_instigator_session_id]
event.od_group_set.group_name
target.group.group_display_name
event.od_group_set.member.member_array
target.user.user_display_name
event.od_group_set.instigator_token.euid
principal.user.userid
event.od_group_set.db_path
additional.fields[od_group_set_db_path]
event.od_group_set.node_name
additional.fields[od_group_set_node_name]
event.od_group_set.error_code
additional.fields[od_group_set_error_code]
event_type: od_modify_password
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
od_modify_password
.
metadata.description
A group has a member initialized or replaced using Open Directory.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_CHANGE_PASSWORD
.
event.od_modify_password.instigator.audit_token.euid
principal.process.euid
event.od_modify_password.instigator.audit_token.ruid
principal.process.ruid
event.od_modify_password.instigator.audit_token.egid
principal.process.egid
event.od_modify_password.instigator.audit_token.rgid
principal.process.rgid
event.od_modify_password.instigator.audit_token.pgid
principal.process.pgid
event.od_modify_password.instigator.audit_token.pid
principal.process.pid
event.od_modify_password.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.od_modify_password.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.od_modify_password.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.od_modify_password.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.od_modify_password.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.od_modify_password.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.od_modify_password.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.od_modify_password.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.od_modify_password.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.od_modify_password.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.od_modify_password.instigator.executable.path
principal.process.file.full_path
event.od_modify_password.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.od_modify_password.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.od_modify_password.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.od_modify_password.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.od_modify_password.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.od_modify_password.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.od_modify_password.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.od_modify_password.instigator.executable.stat.st_size
principal.process.file.size
event.od_modify_password.instigator.executable.sha256
principal.process.file.sha256
event.od_modify_password.instigator.executable.sha1
principal.process.file.sha1
event.od_modify_password.instigator.signing_id
additional.fields[od_modify_password_instigator_signing_id]
event.od_modify_password.instigator.team_id
additional.fields[od_modify_password_instigator_team_id]
event.od_modify_password.instigator.ppid
additional.fields[od_modify_password_instigator_ppid]
event.od_modify_password.instigator.codesigning_flags
additional.fields[od_modify_password_instigator_codesigning_flags]
event.od_modify_password.instigator.cdhash
additional.fields[od_modify_password_instigator_cdhash]
event.od_modify_password.instigator.is_platform_binary
additional.fields[od_modify_password_instigator_is_platform_binary]
event.od_modify_password.instigator.is_es_client
additional.fields[od_modify_password_instigator_is_es_client]
event.od_modify_password.instigator.group_id
principal.process.pgid
event.od_modify_password.instigator.original_ppid
additional.fields[od_modify_password_instigator_original_pp]
event.od_modify_password.instigator.session_id
additional.fields[od_modify_password_instigator_session_id]
event.od_modify_password.account_name
target.user.user_display_name
event.od_modify_password.instigator_token.euid
principal.user.userid
event.od_modify_password.db_path
additional.fields[od_modify_password_db_path]
event.od_modify_password.node_name
additional.fields[od_modify_password_node_name]
event.od_modify_password.error_code
additional.fields[od_modify_password_error_code]
event_type: openssh_login
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
openssh_login
.
metadata.description
A user has logged into the system via OpenSSH.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGIN
.
network.application_protocol
The
network.application_protocol
UDM field is set to
SSH
.
event.openssh_login.source_address
src.ip
event.openssh_login.uid
target.user.userid
openssh_login.username
target.user.user_display_name
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
event.openssh_login.success
security_result.category
If the
event.openssh_login.success
log field value is equal to
false
then, the
security_result.category
UDM field is set to
AUTH_VIOLATION
.
event_type: openssh_logout
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
openssh_logout
.
metadata.description
A user has logged out of an OpenSSH session.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_LOGOUT
.
network.application_protocol
The
network.application_protocol
UDM field is set to
SSH
.
event.openssh_logout.source_address
src.ip
event.openssh_logout.uid
target.user.userid
openssh_logout.username
target.user.user_display_name
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
event_type: profile_add
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
openssh_logout
.
metadata.description
A configuration profile is installed on the system.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
SETTING_CREATION
.
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
SETTING
.
event.profile_add.instigator.audit_token.euid
principal.process.euid
event.profile_add.instigator.audit_token.ruid
principal.process.ruid
event.profile_add.instigator.audit_token.egid
principal.process.egid
event.profile_add.instigator.audit_token.rgid
principal.process.rgid
event.profile_add.instigator.audit_token.pgid
principal.process.pgid
event.profile_add.instigator.audit_token.pid
principal.process.pid
event.profile_add.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.profile_add.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.profile_add.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.profile_add.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.profile_add.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.profile_add.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.profile_add.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.profile_add.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.profile_add.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.profile_add.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.profile_add.instigator.executable.path
principal.process.file.full_path
event.profile_add.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.profile_add.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.profile_add.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.profile_add.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.profile_add.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.profile_add.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.profile_add.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.profile_add.instigator.executable.stat.st_size
principal.process.file.size
event.profile_add.instigator.executable.sha256
principal.process.file.sha256
event.profile_add.instigator.executable.sha1
principal.process.file.sha1
event.profile_add.instigator.signing_id
additional.fields[profile_add_instigator_signing_id]
event.profile_add.instigator.team_id
additional.fields[profile_add_instigator_team_id]
event.profile_add.instigator.ppid
additional.fields[profile_add_instigator_ppid]
event.profile_add.instigator.codesigning_flags
additional.fields[profile_add_instigator_codesigning_flags]
event.profile_add.instigator.cdhash
additional.fields[profile_add_instigator_cdhash]
event.profile_add.instigator.is_platform_binary
additional.fields[profile_add_instigator_is_platform_binary]
event.profile_add.instigator.is_es_client
additional.fields[profile_add_instigator_is_es_client]
event.profile_add.instigator.group_id
principal.process.pgid
event.profile_add.instigator.original_ppid
additional.fields[profile_add_instigator_original_pp]
event.profile_add.instigator.session_id
additional.fields[profile_add_instigator_session_id]
event.profile_add.profile.scope
target.resource.resource_subtype
event.profile_add.profile.uuid
target.resource.product_object_id
event.profile_add.profile.display_name
target.resource.name
event.profile_add.is_update
additional.fields[profile_add_is_update]
event.profile_add.profile.identifier
additional.fields[profile_add_profile_identifier]
event.profile_add.profile.install_source
additional.fields[profile_add_profile_install_source]
event.profile_add.profile.organization
additional.fields[profile_add_profile_organization]
event_type: profile_remove
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
openssh_logout
.
metadata.description
A configuration profile is removed from the system.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
SETTING_DELETION
.
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
SETTING
.
event.profile_remove.instigator.audit_token.euid
principal.process.euid
event.profile_remove.instigator.audit_token.ruid
principal.process.ruid
event.profile_remove.instigator.audit_token.egid
principal.process.egid
event.profile_remove.instigator.audit_token.rgid
principal.process.rgid
event.profile_remove.instigator.audit_token.pgid
principal.process.pgid
event.profile_remove.instigator.audit_token.pid
principal.process.pid
event.profile_remove.instigator.audit_token.uuid
principal.process.product_specific_process_id
event.profile_remove.instigator.audit_token.signing_id
principal.process.file.signature_info.codesign.id
event.profile_remove.instigator.parent_audit_token.euid
principal.process.parent_process.euid
event.profile_remove.instigator.parent_audit_token.ruid
principal.process.parent_process.ruid
event.profile_remove.instigator.parent_audit_token.egid
principal.process.parent_process.egid
event.profile_remove.instigator.parent_audit_token.rgid
principal.process.parent_process.rgid
event.profile_remove.instigator.parent_audit_token.pgid
principal.process.parent_process.pgid
event.profile_remove.instigator.parent_audit_token.pid
principal.process.parent_process.pid
event.profile_remove.instigator.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
event.profile_remove.instigator.parent_audit_token.signing_id
principal.process.parent_process.file.signature_info.codesign.id
event.profile_remove.instigator.executable.path
principal.process.file.full_path
event.profile_remove.instigator.executable.stat.st_dev
principal.process.file.stat_dev
event.profile_remove.instigator.executable.stat.st_flags
principal.process.file.stat_flags
event.profile_remove.instigator.executable.stat.st_ino
principal.process.file.stat_inode
event.profile_remove.instigator.executable.stat.st_mode
principal.process.file.stat_mode
event.profile_remove.instigator.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.profile_remove.instigator.executable.stat.st_atimespec
principal.process.file.last_access_time
event.profile_remove.instigator.executable.stat.st_nlink
principal.process.file.stat_nlink
event.profile_remove.instigator.executable.stat.st_size
principal.process.file.size
event.profile_remove.instigator.executable.sha256
principal.process.file.sha256
event.profile_remove.instigator.executable.sha1
principal.process.file.sha1
event.profile_remove.instigator.signing_id
additional.fields[profile_remove_instigator_signing_id]
event.profile_remove.instigator.team_id
additional.fields[profile_remove_instigator_team_id]
event.profile_remove.instigator.ppid
additional.fields[profile_remove_instigator_ppid]
event.profile_remove.instigator.codesigning_flags
additional.fields[profile_remove_instigator_codesigning_flags]
event.profile_remove.instigator.cdhash
additional.fields[profile_remove_instigator_cdhash]
event.profile_remove.instigator.is_platform_binary
additional.fields[profile_remove_instigator_is_platform_binary]
event.profile_remove.instigator.is_es_client
additional.fields[profile_remove_instigator_is_es_client]
event.profile_remove.instigator.group_id
principal.process.pgid
event.profile_remove.instigator.original_ppid
additional.fields[profile_remove_instigator_original_pp]
event.profile_remove.instigator.session_id
additional.fields[profile_remove_instigator_session_id]
event.profile_remove.profile.scope
target.resource.resource_subtype
event.profile_remove.profile.uuid
target.resource.product_object_id
event.profile_remove.profile.display_name
target.resource.name
event.profile_remove.is_update
additional.fields[profile_remove_is_update]
event.profile_remove.profile.identifier
additional.fields[profile_remove_profile_identifier]
event.profile_remove.profile.install_source
additional.fields[profile_remove_profile_install_source]
event.profile_remove.profile.organization
additional.fields[profile_remove_profile_organization]
event_type: sudo
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
sudo
.
metadata.description
A sudo attempt occurred.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.sudo.reject_info.plugin_name
additional.fields[sudo_reject_info_plugin_name]
event.sudo.reject_info.failure_message
additional.fields[sudo_reject_info_failure_message]
event.sudo.reject_info.plugin_type
additional.fields[sudo_reject_info_plugin_type]
event.sudo.from_uid
principal.user.userid
event.sudo.from_username
principal.user.user_display_name
event.sudo.command
target.process.command_line
event.sudo.to_uid
target.user.userid
event.sudo.to_username
target.user.user_display_name
event.sudo.success
security_result.category
If the
event.sudo.success
log field value is equal to
false
then, the
security_result.category
UDM field is set to
AUTH_VIOLATION
.
event_type: system_performance
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
system_performance
.
metadata.description
Event occurs on a regular interval to collect application performance data.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.performance.metrics.hw_model
additional.fields[performance_metrics_hw_model]
event.performance.page_info.page
additional.fields[performance_page_info_page]
performance.page_info.total
additional.fields[performance_page_info_total]
event.performance.metrics.tasks.name
additional.fields[task_name]
event.performance.metrics.tasks.energy_impact
additional.fields[task_energy_impact]
event_type: unmount
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
unmount
.
metadata.description
A file system has been unmounted.
value is set to the
metadata.description
UDM field.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
event.unmount.statfs.f_owner
target.user.userid
event.unmount.device.size
target.file.size
event.unmount.statfs.f_fstypename
target.resource.resource_subtype
event.unmount.statfs.f_mntfromname
target.resource.name
event.unmount.device.protocol
additional.fields[unmount_device_protocol]
event.unmount.device.serial_number
target.asset.hardware.serial_number
If the
event.unmount.device.serial_number
log field value is
not
empty
or the
event.unmount.device.vendor_name
log field value is
not
empty
or the
event.unmount.device.device_model
log field value is
not
empty
then,
event.unmount.device.serial_number
log field is mapped to the
target.asset.hardware.serial_number
UDM field.
event.unmount.device.device_model
target.asset.hardware.model
If the
event.unmount.device.serial_number
log field value is
not
empty
or the
event.unmount.device.vendor_name
log field value is
not
empty
or the
event.unmount.device.device_model
log field value is
not
empty
then,
event.unmount.device.device_model
log field is mapped to the
target.asset.hardware.model
UDM field.
event.unmount.device.vendor_name
target.asset.hardware.manudacturer
If the
event.unmount.device.serial_number
log field value is
not
empty
or the
event.unmount.device.vendor_name
log field value is
not
empty
or the
event.unmount.device.device_model
log field value is
not
empty
then,
event.unmount.device.vendor_name
log field is mapped to the
target.asset.hardware.manufacturer
UDM field.
event_type: network_connect
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
network_connect
.
metadata.description
The
metadata.description
UDM field is set to
Network Telemetry
.
metadata.event_type
The
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
event_type
additional.fields[event_type]
event.authentication.data.od.instigator.audit_token.e_username
principal.user.user_display_name
event.network_connect.direction
network.direction
event.network_connect.instigator_token.uuid
principal.process.product_specific_process_id
JamfProtect:%{event.network_connect.instigator_token.uuid}
log field is mapped to the
principal.process.product_specific_process_id
UDM field.
event.network_connect.instigator.audit_token.e_username
principal.user.user_display_name
event.network_connect.local_endpoint.host
src.ip
event.network_connect.local_endpoint.port
src.port
event.network_connect.remote_endpoint.host
target.ip
event.network_connect.remote_endpoint.port
target.port
event.network_connect.remote_hostname
target.hostname
event.network_connect.socket_family
additional.fields[network_socket_family]
If the
event.network_connect.socket_family
log field value is equal to
1
, then the
additional.fields.key
UDM field is set to
network_socket_family
and the
additional.fields.value.string_value
UDM field is set to
1-AF_UNIX
.
Else, if the
event.network_connect.socket_family
log field value is equal to
2
, then the
additional.fields.key
UDM field is set to
network_socket_family
and the
additional.fields.value.string_value
UDM field is set to
2-AF_INET
.
Else, if the
event.network_connect.socket_family
log field value is equal to
30
, then the
additional.fields.key
UDM field is set to
network_socket_family
and the
additional.fields.value.string_value
UDM field is set to
30-AF_INET6
.
Else, the
additional.fields.key
UDM field is set to
network_socket_family
and the original
event.network_connect.socket_family
log field value is mapped to the
additional.fields.value.string_value
UDM field.
event.network_connect.socket_protocol
network.ip_protocol
If the
event.network_connect.socket_protocol
log field value is equal to
1
, then the
network.ip_protocol
UDM field is set to
ICMP
.
Else, if the
event.network_connect.socket_protocol
log field value is equal to
6
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
event.network_connect.socket_protocol
log field value is equal to
17
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
event.network_connect.socket_protocol
log field value is equal to
41
, then the
network.ip_protocol
UDM field is set to
IP6IN4
.
Else, if the
event.network_connect.socket_protocol
log field value is equal to
58
, then the
network.ip_protocol
UDM field is set to
ICMP6
.
Else, if the
event.network_connect.socket_protocol
log field value is equal to
255
, then the
network.ip_protocol
UDM field is set to
UNKNOWN_IP_PROTOCOL
.
Else, the
event.network_connect.socket_protocol
log field is mapped to the
network.ip_protocol
UDM field as an unknown enum value.
event.network_connect.socket_type
additional.fields[network_socket_type]
If the
event.network_connect.socket_type
log field value is equal to
1
, then the
additional.fields.key
UDM field is set to
network_socket_type
and the
additional.fields.value.string_value
UDM field is set to
1-SOCK_STREAM
.
Else, if the
event.network_connect.socket_type
log field value is equal to
2
, then the
additional.fields.key
UDM field is set to
network_socket_type
and the
additional.fields.value.string_value
UDM field is set to
2-SOCK_DGRAM
.
Else, if the
event.network_connect.socket_type
log field value is equal to
3
, then the
additional.fields.key
UDM field is set to
network_socket_type
and the
additional.fields.value.string_value
UDM field is set to
3-SOCK_RAW
.
Else, if the
event.network_connect.socket_type
log field value is equal to
4
, then the
additional.fields.key
UDM field is set to
network_socket_type
and the
additional.fields.value.string_value
UDM field is set to
4-SOCK_RDM
.
Else, if the
event.network_connect.socket_type
log field value is equal to
5
, then the
additional.fields.key
UDM field is set to
network_socket_type
and the
additional.fields.value.string_value
UDM field is set to
5-SOCK_SEQPACKET
.
Else, the
additional.fields.key
UDM field is set to
network_socket_type
and the original
event.network_connect.socket_type
log field value is mapped to the
additional.fields.value.string_value
UDM field.
event.network_connect.url
target.url
event.network_connect.uuid
network.session_id
global_seq_num
additional.fields[global_seq_num]
mach_time
additional.fields[mach_time]
process.audit_token.e_username
src.user.user_display_name
process.audit_token.egid
src.process.egid
process.audit_token.euid
src.process.euid
process.audit_token.pid
src.process.pid
process.audit_token.rgid
src.process.rgid
process.audit_token.ruid
src.process.ruid
process.audit_token.uuid
src.process.product_specific_process_id
JamfProtect:%{process.audit_token.uuid}
log field is mapped to the
src.process.product_specific_process_id
UDM field.
process.cdhash
additional.fields[src_cdhash]
process.codesigning_flags
additional.fields[src_codesiging_flags]
process.cs_validation_category
additional.fields[src_cs_validation_category]
process.executable.path
src.process.file.full_path
process.executable.sha1
src.process.file.sha1
process.executable.sha256
src.process.file.sha256
process.executable.stat.st_atimespec
src.process.file.last_access_time
process.executable.stat.st_ctimespec
src.process.file.create_time
process.executable.stat.st_mtimespec
src.process.file.last_modification_time
process.group_id
src.process.pgid
process.is_es_client
additional.fields[src_is_es_client]
process.is_platform_binary
additional.fields[src_is_platform_binary]
process.original_ppid
additional.fields[src_original_ppid]
process.parent_audit_token.egid
src.process.parent_process.egid
process.parent_audit_token.euid
src.process.parent_process.euid
process.parent_audit_token.exec_path
src.process.parent_process.file.full_path
process.parent_audit_token.pid
src.process.parent_process.pid
process.parent_audit_token.rgid
src.process.parent_process.rgid
process.parent_audit_token.ruid
src.process.parent_process.ruid
process.parent_audit_token.uuid
src.process.parent_process.product_specific_process_id
process.ppid
src.process.parent_pid
process.session_id
additional.fields[src_session_id]
process.signing_id
src.process.file.signature_info.codesign.id
process.team_id
src.process.file.signature_info.codesign.team_id
process.tty.path
src.process.tty
seq_num
additional.fields[seq_num]
version
additional.fields[protect_datamodel_version]
event_type: pty_close
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
pty_close
.
metadata.description
The
metadata.description
UDM field is set to
A pseudoterminal control device is closed.
metadata.event_type
The
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
process.audit_token.e_username
principal.user.userid
process.audit_token.euid
principal.process.euid
process.audit_token.ruid
principal.process.ruid
process.audit_token.egid
principal.process.egid
process.audit_token.rgid
principal.process.rgid
process.audit_token.pid
principal.process.pid
process.audit_token.uuid
principal.process.product_specific_process_id
process.parent_audit_token.euid
principal.process.parent_process.euid
process.parent_audit_token.ruid
principal.process.parent_process.ruid
process.parent_audit_token.egid
principal.process.parent_process.egid
process.parent_audit_token.rgid
principal.process.parent_process.rgid
process.parent_audit_token.pid
principal.process.parent_process.pid
process.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
process.parent_audit_token.exec_path
principal.process.parent_process.file.full_path
process.executable.path
principal.process.file.full_path
process.executable.stat.st_mtimespec
principal.process.file.last_modification_time
process.executable.stat.st_ctimespec
principal.process.file.create_time
process.executable.stat.st_atimespec
principal.process.file.last_access_time
process.executable.sha256
principal.process.file.sha256
process.executable.sha1
principal.process.file.sha1
process.signing_id
principal.process.file.signature_info.codesign.id
process.team_id
principal.process.file.signature_info.codesign.team_id
process.ppid
principal.process.parent_pid
process.group_id
principal.process.pgid
process.tty.path
principal.process.tty
process.codesigning_flags
additional.fields[principal_codesiging_flags]
process.cdhash
additional.fields[principal_cdhash]
process.is_platform_binary
additional.fields[principal_is_platform_binary]
process.is_es_client
additional.fields[principal_is_es_client]
process.original_ppid
additional.fields[principal_original_ppid]
process.session_id
additional.fields[principal_session_id]
event_type
additional.fields[event_type]
global_seq_num
additional.fields[global_seq_num]
version
additional.fields[protect_datamodel_version]
event.pty_close.dev
additional.fields[pty_close_dev]
event_type: pty_grant
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
pty_grant
.
metadata.description
The
metadata.description
UDM field is set to
A pseudoterminal control device is granted.
metadata.event_type
The
metadata.event_type
UDM field is set to
PROCESS_LAUNCH
.
process.audit_token.e_username
principal.user.user_display_name
process.cs_validation_category
additional.fields[principal_cs_validation_category]
process.audit_token.euid
principal.process.euid
process.audit_token.ruid
principal.process.ruid
process.audit_token.egid
principal.process.egid
process.audit_token.rgid
principal.process.rgid
process.audit_token.pid
principal.process.pid
process.audit_token.uuid
principal.process.product_specific_process_id
process.parent_audit_token.euid
principal.process.parent_process.euid
process.parent_audit_token.ruid
principal.process.parent_process.ruid
process.parent_audit_token.egid
principal.process.parent_process.egid
process.parent_audit_token.rgid
principal.process.parent_process.rgid
process.parent_audit_token.pid
principal.process.parent_process.pid
process.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
process.parent_audit_token.exec_path
principal.process.parent_process.file.full_path
process.executable.path
principal.process.file.full_path
process.executable.stat.st_mtimespec
principal.process.file.last_modification_time
process.executable.stat.st_ctimespec
principal.process.file.create_time
process.executable.stat.st_atimespec
principal.process.file.last_access_time
process.executable.sha256
principal.process.file.sha256
process.executable.sha1
principal.process.file.sha1
process.signing_id
principal.process.file.signature_info.codesign.id
process.team_id
principal.process.file.signature_info.codesign.team_id
process.ppid
principal.process.parent_pid
process.group_id
principal.process.pgid
process.tty.path
principal.process.tty
process.codesigning_flags
additional.fields[principal_codesiging_flags]
process.cdhash
additional.fields[principal_cdhash]
process.is_platform_binary
additional.fields[principal_is_platform_binary]
process.is_es_client
additional.fields[principal_is_es_client]
process.original_ppid
additional.fields[principal_original_ppid]
process.session_id
additional.fields[principal_session_id]
event.remount.statfs.f_ffree
additional.fields[remount_statfs_f_ffree]
version
additional.fields[protect_datamodel_version]
event.pty_grant.dev
additional.fields[pty_grant_dev]
event_type: tcc_modify
Log field
UDM mapping
Logic
metadata.product_event_type
The
metadata.product_event_type
UDM field is set to
tcc_modify
.
metadata.description
The
metadata.description
UDM field is set to
A Transparency Consent and Control (TCC) permission is granted or revoked.
metadata.event_type
The
metadata.event_type
UDM field is set to
RESOURCE_PERMISSIONS_CHANGE
.
event.tcc_modify.responsible.audit_token.e_username
principal.user.userid
event.tcc_modify.instigator.audit_token.e_username
target.user.userid
event.tcc_modify.instigator.cs_validation_category
additional.fields[target_cs_validation_category]
event.tcc_modify.responsible.cs_validation_category
additional.fields[principal_cs_validation_category]
event.tcc_modify.responsible.audit_token.euid
principal.process.euid
event.tcc_modify.responsible.audit_token.ruid
principal.process.ruid
event.tcc_modify.responsible.audit_token.egid
principal.process.egid
event.tcc_modify.responsible.audit_token.rgid
principal.process.rgid
event.tcc_modify.responsible.audit_token.pid
principal.process.pid
event.tcc_modify.responsible.audit_token.uuid
principal.process.product_specific_process_id
JamfProtect:%{event.tcc_modify.responsible.audit_token.uuid}
log field is mapped to the
principal.process.product_specific_process_id
UDM field.
event.tcc_modify.responsible.parent_audit_token.euid
principal.process.parent_process.euid
event.tcc_modify.responsible.parent_audit_token.ruid
principal.process.parent_process.ruid
event.tcc_modify.responsible.parent_audit_token.egid
principal.process.parent_process.egid
event.tcc_modify.responsible.parent_audit_token.rgid
principal.process.parent_process.rgid
event.tcc_modify.responsible.parent_audit_token.pid
principal.process.parent_process.pid
event.tcc_modify.responsible.parent_audit_token.uuid
principal.process.parent_process.product_specific_process_id
JamfProtect:%{event.tcc_modify.responsible.parent_audit_token.uuid}
log field is mapped to the
principal.process.parent_process.product_specific_process_id
UDM field.
event.tcc_modify.responsible.parent_audit_token.exec_path
principal.process.parent_process.file.full_path
event.tcc_modify.responsible.executable.path
principal.process.file.full_path
event.tcc_modify.responsible.executable.stat.st_dev
principal.process.file.stat_dev
event.tcc_modify.responsible.executable.stat.st_flags
principal.process.file.stat_flags
event.tcc_modify.responsible.executable.stat.st_ino
principal.process.file.stat_inode
event.tcc_modify.responsible.executable.stat.st_mode
principal.process.file.stat_mode
event.tcc_modify.responsible.executable.stat.st_mtimespec
principal.process.file.last_modification_time
event.tcc_modify.responsible.executable.stat.st_ctimespec
principal.process.file.create_time
event.tcc_modify.responsible.executable.stat.st_atimespec
principal.process.file.last_access_time
event.tcc_modify.responsible.executable.stat.st_nlink
principal.process.file.stat_nlink
event.tcc_modify.responsible.executable.stat.st_size
principal.process.file.size
event.tcc_modify.responsible.executable.sha256
principal.process.file.sha256
event.tcc_modify.responsible.executable.sha1
principal.process.file.sha1
event.tcc_modify.responsible.signing_id
principal.process.file.signature_info.codesign.id
event.tcc_modify.responsible.team_id
principal.process.file.signature_info.codesign.team_id
event.tcc_modify.responsible.ppid
principal.process.parent_pid
event.tcc_modify.responsible.group_id
principal.process.pgid
event.tcc_modify.responsible.tty.path
principal.process.tty
event.tcc_modify.responsible.codesigning_flags
additional.fields[principal_codesiging_flags]
event.tcc_modify.responsible.cdhash
additional.fields[principal_cdhash]
event.tcc_modify.responsible.is_platform_binary
additional.fields[principal_is_platform_binary]
event.tcc_modify.responsible.is_es_client
additional.fields[principal_is_es_client]
event.tcc_modify.responsible.original_ppid
additional.fields[principal_original_ppid]
event.tcc_modify.responsible.session_id
additional.fields[principal_session_id]
process.audit_token.euid
src.process.euid
process.audit_token.ruid
src.process.ruid
process.audit_token.egid
src.process.egid
process.audit_token.rgid
src.process.rgid
process.audit_token.pid
src.process.pid
process.audit_token.uuid
src.process.product_specific_process_id
JamfProtect:%{process.audit_token.uuid}
log field is mapped to the
src.process.product_specific_process_id
UDM field.
process.audit_token.e_username
src.user.user_display_name
process.parent_audit_token.euid
src.process.parent_process.euid
process.parent_audit_token.ruid
src.process.parent_process.ruid
process.parent_audit_token.egid
src.process.parent_process.egid
process.parent_audit_token.rgid
src.process.parent_process.rgid
process.parent_audit_token.pid
src.process.parent_process.pid
process.parent_audit_token.uuid
src.process.parent_process.product_specific_process_id
JamfProtect:%{process.parent_audit_token.uuid}
log field is mapped to the
src.process.parent_process.product_specific_process_id
UDM field.
process.parent_audit_token.exec_path
src.process.parent_process.file.full_path
process.executable.path
src.process.file.full_path
process.executable.stat.st_mtimespec
src.process.file.last_modification_time
process.executable.stat.st_ctimespec
src.process.file.create_time
process.executable.stat.st_atimespec
src.process.file.last_access_time
process.executable.sha256
src.process.file.sha256
process.executable.sha1
src.process.file.sha1
process.signing_id
src.process.file.signature_info.codesign.id
process.team_id
src.process.file.signature_info.codesign.team_id
process.ppid
src.process.parent_pid
process.group_id
src.process.pgid
process.tty.path
src.process.tty
process.codesigning_flags
additional.fields[src_codesiging_flags]
process.cs_validation_category
additional.fields[src_cs_validation_category]
process.cdhash
additional.fields[src_cdhash]
process.is_platform_binary
additional.fields[src_is_platform_binary]
process.is_es_client
additional.fields[src_is_es_client]
process.original_ppid
additional.fields[src_original_ppid]
process.session_id
additional.fields[src_session_id]
event.tcc_modify.instigator.audit_token.euid
target.process.euid
event.tcc_modify.instigator.audit_token.ruid
target.process.ruid
event.tcc_modify.instigator.audit_token.egid
target.process.egid
event.tcc_modify.instigator.audit_token.rgid
target.process.rgid
event.tcc_modify.instigator.audit_token.pid
target.process.pid
event.tcc_modify.instigator.audit_token.uuid
target.process.product_specific_process_id
JamfProtect:%{event.tcc_modify.instigator.audit_token.uuid}
log field is mapped to the
target.process.product_specific_process_id
UDM field.
event.tcc_modify.instigator.parent_audit_token.euid
target.process.parent_process.euid
event.tcc_modify.instigator.parent_audit_token.ruid
target.process.parent_process.ruid
event.tcc_modify.instigator.parent_audit_token.egid
target.process.parent_process.egid
event.tcc_modify.instigator.parent_audit_token.rgid
target.process.parent_process.rgid
event.tcc_modify.instigator.parent_audit_token.pid
target.process.parent_process.pid
event.tcc_modify.instigator.parent_audit_token.uuid
target.process.parent_process.product_specific_process_id
JamfProtect:%{event.tcc_modify.instigator.parent_audit_token.uuid}
log field is mapped to the
target.process.parent_process.product_specific_process_id
UDM field.
event.tcc_modify.instigator.parent_audit_token.exec_path
target.process.parent_process.file.full_path
event.tcc_modify.instigator.executable.path
target.process.file.full_path
event.tcc_modify.instigator.executable.stat.st_dev
target.process.file.stat_dev
event.tcc_modify.instigator.executable.stat.st_flags
target.process.file.stat_flags
event.tcc_modify.instigator.executable.stat.st_ino
target.process.file.stat_inode
event.tcc_modify.instigator.executable.stat.st_mode
target.process.file.stat_mode
event.tcc_modify.instigator.executable.stat.st_mtimespec
target.process.file.last_modification_time
event.tcc_modify.instigator.executable.stat.st_ctimespec
target.process.file.create_time
event.tcc_modify.instigator.executable.stat.st_atimespec
target.process.file.last_access_time
event.tcc_modify.instigator.executable.stat.st_nlink
target.process.file.stat_nlink
event.tcc_modify.instigator.executable.stat.st_size
target.process.file.size
event.tcc_modify.instigator.executable.sha256
target.process.file.sha256
event.tcc_modify.instigator.executable.sha1
target.process.file.sha1
event.tcc_modify.instigator.signing_id
target.process.file.signature_info.codesign.id
event.tcc_modify.instigator.team_id
target.process.file.signature_info.codesign.team_id
event.tcc_modify.instigator.ppid
target.process.parent_pid
event.tcc_modify.instigator.group_id
target.process.pgid
event.tcc_modify.instigator.tty.path
target.process.tty
event.tcc_modify.instigator.codesigning_flags
additional.fields[target_codesiging_flags]
event.tcc_modify.instigator.cdhash
additional.fields[target_cdhash]
event.tcc_modify.instigator.is_platform_binary
additional.fields[target_is_platform_binary]
event.tcc_modify.instigator.is_es_client
additional.fields[target_is_es_client]
event.tcc_modify.instigator.original_ppid
additional.fields[target_original_ppid]
event.tcc_modify.instigator.session_id
additional.fields[target_session_id]
event_type
additional.fields[event_type]
global_seq_num
additional.fields[global_seq_num]
version
additional.fields[protect_datamodel_version]
event.tcc_modify.identity_type
additional.fields[tcc_modify_identity_type]
event.tcc_modify.service
security_result.rule_name
event.tcc_modify.identity
security_result.about.process.file.signature_info.codesign.id
If the
event.tcc_modify.identity_type
log field value is equal to
0
then,
event.tcc_modify.identity
log field is mapped to the
security_result.about.process.file.signature_info.codesign.id
UDM field.
event.tcc_modify.identity
security_result.about.process.file.full_path
If the
event.tcc_modify.identity_type
log field value is equal to
1
then,
event.tcc_modify.identity
log field is mapped to the
security_result.about.process.file.full_path
UDM field.
event.tcc_modify.right
security_result.action_details
If the
event.tcc_modify.right
log field value is equal to
3
, then the
security_result.action_details
UDM field is set to
Limited
.
Else, if the
event.tcc_modify.right
log field value is equal to
4
, then the
security_result.action_details
UDM field is set to
Add_Modify_Added
.
Else, if the
event.tcc_modify.right
log field value is equal to
5
, then the
security_result.action_details
UDM field is set to
Session_PID
.
Else, if the
event.tcc_modify.right
log field value is equal to
6
, then the
security_result.action_details
UDM field is set to
Learn More
.
Else, the
event.tcc_modify.right
log field value is mapped to the
security_result.action_details
UDM field.
event.tcc_modify.reason
security_result.summary
If the
event.tcc_modify.reason
log field value is equal to
0
, then the
security_result.summary
UDM field is set to
None
.
Else, if the
event.tcc_modify.reason
log field value is equal to
1
, then the
security_result.summary
UDM field is set to
Error
.
Else, if the
event.tcc_modify.reason
log field value is equal to
2
, then the
security_result.summary
UDM field is set to
User_Consent
.
Else, if the
event.tcc_modify.reason
log field value is equal to
3
, then the
security_result.summary
UDM field is set to
User_Set
.
Else, if the
event.tcc_modify.reason
log field value is equal to
4
, then the
security_result.summary
UDM field is set to
System_Set
.
Else, if the
event.tcc_modify.reason
log field value is equal to
5
, then the
security_result.summary
UDM field is set to
Service_Policy
.
Else, if the
event.tcc_modify.reason
log field value is equal to
6
, then the
security_result.summary
UDM field is set to
MDM_Policy
.
Else, if the
event.tcc_modify.reason
log field value is equal to
7
, then the
security_result.summary
UDM field is set to
Service_Override_Policy
.
Else, if the
event.tcc_modify.reason
log field value is equal to
8
, then the
security_result.summary
UDM field is set to
Missing_Usage_String
.
Else, if the
event.tcc_modify.reason
log field value is equal to
9
, then the
security_result.summary
UDM field is set to
Prompt_Timeout
.
Else, if the
event.tcc_modify.reason
log field value is equal to
10
, then the
security_result.summary
UDM field is set to
Preflight_Unknown
.
Else, if the
event.tcc_modify.reason
log field value is equal to
11
, then the
security_result.summary
UDM field is set to
Entitled
.
Else, if the
event.tcc_modify.reason
log field value is equal to
12
, then the
security_result.summary
UDM field is set to
App_Type_Policy
.
Else, if the
event.tcc_modify.reason
log field value is equal to
13
, then the
security_result.summary
UDM field is set to
Prompt_Cancel
.
Else, the
event.tcc_modify.reason
log field value is mapped to the
security_result.summary
UDM field.
event.tcc_modify.update_type
security_result.description
If the
event.tcc_modify.update_type
log field value is equal to
0
, then the
security_result.description
UDM field is set to
Unknown
.
Else, if the
event.tcc_modify.update_type
log field value is equal to
1
, then the
security_result.description
UDM field is set to
Create
.
Else, if the
event.tcc_modify.update_type
log field value is equal to
2
, then the
security_result.description
UDM field is set to
Modify
.
Else, if the
event.tcc_modify.update_type
log field value is equal to
3
, then the
security_result.description
UDM field is set to
Delete
.
Else, the
event.tcc_modify.update_type
log field value is mapped to the
security_result.description
UDM field.
Need more help?
Get answers from Community members and Google SecOps professionals.
