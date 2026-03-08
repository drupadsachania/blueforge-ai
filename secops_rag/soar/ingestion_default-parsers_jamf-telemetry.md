# Collect Jamf Protect Telemetry logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry/  
**Scraped:** 2026-03-05T09:48:19.630328Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Jamf Protect Telemetry logs
Supported in:
Google secops
SIEM
This document describes how you can collect Jamf Protect Telemetry logs by setting up a Google Security Operations
feed and how log fields map to Google Security Operations Unified Data Model (UDM) fields.
This document also lists the supported Jamf Protect Telemetry version.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Jamf Protect Telemetry and the Google Security Operations feed configured to send logs to Google Security Operations. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Jamf Protect Telemetry
. The Jamf Protect Telemetry platform from which you collect logs.
Google Security Operations feed
. The Google Security Operations feed that fetches logs from Jamf Protect Telemetry and writes logs to Google Security Operations.
Google Security Operations
. Google Security Operations retains and analyzes the logs from Jamf Protect Telemetry.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
JAMF_TELEMETRY
ingestion label.
Before you begin
Ensure you have the following prerequisites:
A
Jamf Protect Telemetry
set up
Jamf Protect version 4.0.0 or later
All systems in the deployment architecture are configured with the UTC time zone.
Set up feeds from SIEM Settings
>
Feeds
You can use either Amazon S3 V2 or a webhook to set up an ingestion feed in Google Security Operations.
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
Jamf Protect Telemetry
log type.
Select
Amazon S3 V2
as the
Source type
.
Specify values for the following fields:
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Access Key ID
: The user's access key with permissions to read from the S3 bucket.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Secret Access Key
: The user's secret key with permissions to read from the S3 bucket.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
:
Namespace associated with the feed
.
Ingestion Labels
: Labels applied to all events from this feed.
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
Jamf Protect Telemetry
log type.
In the
Source type
list, select
Webhook
.
Specify values for the following fields:
Split delimiter
: The delimiter that is used to separate log lines, such as
\n
.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Create Feed
.
To configure multiple feeds for different log types within this product family, see
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
Set up Jamf Protect Telemetry for a webhook feed
In the Jamf Protect Telemetry application, navigate to the related
Action configuration
.
To add a new Data endpoint, click
Create Actions
.
Select
HTTP
as the protocol.
Enter the HTTPS URL of the Google Security Operations API endpoint in the
URL
field. (This is the
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
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google Security Operations support
.
Supported Jamf Protect Telemetry log types
The Jamf Protect Telemetry parser supports the following log types:
Event Type
AUE_add_to_group
AUE_AUDITCTL
AUE_AUDITON_SPOLICY
AUE_AUTH_USER
AUE_BIND
AUE_BIOS_FIRMWARE_VERSIONS
AUE_CHDIR
AUE_CHROOT
AUE_CONNECT
AUE_create_group
AUE_delete_group
AUE_create_user
AUE_delete_user
AUE_EXECVE
AUE_EXIT
AUE_FORK
AUE_GETAUID
AUE_KILL
AUE_LISTEN
AUE_LOGOUT
AUE_LW_LOGIN
AUE_MAC_SET_PROC
AUE_modify_group
AUE_modify_password
AUE_modify_user
AUE_MOUNT
AUE_openssh
AUE_PIDFORTASK
AUE_POSIX_SPAWN
AUE_REMOVE_FROM_GROUP
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_SESSION_UPDATE
AUE_SETPRIORITY
AUE_SETSOCKOPT
AUE_SETTIMEOFDAY
AUE_SHUTDOWN
AUE_SOCKETPAIR
AUE_SSAUTHINT
AUE_SSAUTHMECH
AUE_SSAUTHORIZE
AUE_TASKFORPID
AUE_TASKNAMEFORPID
AUE_UNMOUNT
AUE_WAIT4
PLAINTEXT_LOG_COLLECTION_EVENT
SYSTEM_PERFORMANCE_METRICS
Supported Jamf Protect Telemetry log formats
The Jamf Protect Telemetry parser supports logs in JSON format.
Supported Jamf Protect Telemetry sample logs
JSON
{
  "exec_chain": {
    "uuid": "F6095AEA-C5CB-4AAB-8FC7-70B9D454319E"
  },
  "exec_chain_child": {
    "parent_path": "/sbin/launchd",
    "parent_pid": 1,
    "parent_uuid": "4AB281FE-6D4A-4E79-8508-E91FCA39BA02"
  },
  "header": {
    "time_seconds_epoch": 1657906179,
    "time_milliseconds_offset": 848,
    "version": 11,
    "event_modifier": 0,
    "event_id": 45018,
    "event_name": "AUE_add_to_group"
  },
  "host_info": {
    "serial_number": "C03WG0H4HDTS",
    "host_name": "Test_MacBook_Pro",
    "osversion": "Version 12.4 (Build 21F79)",
    "host_uuid": "8891C1E2-0AC0-4E4A-844B-EA491B14D115"
  },
  "identity": {
    "signer_id": "dummy.domain.opendirectoryd",
    "team_id_truncated": false,
    "signer_id_truncated": false,
    "cd_hash": "68d22bdec020f20010bfa9d27cd5f69d78427636",
    "team_id": "",
    "signer_type": 1
  },
  "key": "21E48D3B-4965-4072-81BF-83BE04A329C2",
  "return": {
    "error": 0,
    "description": "success",
    "return_value": 0
  },
  "subject": {
    "session_id": 100003,
    "group_id": 20,
    "process_name": "/System/Library/PreferencePanes/Accounts.prefPane/Contents/XPCServices/com.apple.preferences.users.remoteservice.xpc/Contents/MacOS/com.apple.preferences.users.remoteservice",
    "parent_pid": 1,
    "effective_user_name": "jamf",
    "user_id": 501,
    "group_name": "staff",
    "parent_uuid": "4AB281FE-6D4A-4E79-8508-E91FCA39BA02",
    "uuid": "F6095AEA-C5CB-4AAB-8FC7-70B9D454319E",
    "effective_group_id": 20,
    "process_hash": "507494616e05a5eb909794354fe69f29e432f2a7",
    "audit_id": 501,
    "responsible_process_id": 1391,
    "parent_path": "/sbin/launchd",
    "process_id": 1701,
    "effective_group_name": "staff",
    "audit_user_name": "jamf",
    "effective_user_id": 501,
    "terminal_id": {
      "type": 4,
      "ip_address": "198.51.100.0",
      "port": 4278
    },
    "responsible_process_name": "/System/Applications/System Preferences.app/Contents/MacOS/System Preferences",
    "user_name": "jamf"
  },
  "texts": [
    "Added Groups membership username to '_lpadmin' node '/Local/Default', value = 'baddie'"
  ]
}
Field mapping reference
This section explains how the Google Security Operations parser maps Jamf Protect Telemetry fields to Google Security Operations Unified Data Model (UDM) fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
JAMF_TELEMETRY
log types and their corresponding UDM event types.
Event Identifier
Event Type
AUE_add_to_group
GROUP_MODIFICATION
AUE_AUDITCTL
RESOURCE_READ
AUE_AUDITON_SPOLICY
RESOURCE_READ
AUE_AUTH_USER
USER_LOGIN
AUE_BIND
NETWORK_CONNECTION
AUE_BIOS_FIRMWARE_VERSIONS
USER_RESOURCE_ACCESS
AUE_CHDIR
USER_RESOURCE_ACCESS
AUE_CHROOT
USER_RESOURCE_ACCESS
AUE_CONNECT
NETWORK_CONNECTION
AUE_create_group
GROUP_CREATION
AUE_delete_group
GROUP_DELETION
AUE_create_user
USER_CREATION
AUE_delete_user
USER_DELETION
AUE_EXECVE
PROCESS_LAUNCH
AUE_EXIT
PROCESS_TERMINATION
AUE_FORK
PROCESS_LAUNCH
AUE_GETAUID
SCHEDULED_TASK_CREATION
AUE_KILL
PROCESS_TERMINATION
AUE_LISTEN
NETWORK_CONNECTION
AUE_LOGOUT
USER_LOGOUT
AUE_LW_LOGIN
USER_LOGIN
AUE_MAC_SET_PROC
PROCESS_UNCATEGORIZED
AUE_modify_group
GROUP_MODIFICATION
AUE_modify_password
USER_CHANGE_PASSWORD
AUE_modify_user
USER_UNCATEGORIZED
AUE_MOUNT
RESOURCE_READ
AUE_openssh
USER_LOGIN
AUE_PIDFORTASK
PROCESS_LAUNCH
AUE_POSIX_SPAWN
PROCESS_LAUNCH
AUE_REMOVE_FROM_GROUP
GROUP_MODIFICATION
AUE_SESSION_CLOSE
USER_LOGOUT
AUE_SESSION_END
USER_LOGOUT
AUE_SESSION_START
USER_LOGIN
AUE_SESSION_UPDATE
USER_UNCATEGORIZED
AUE_SETPRIORITY
SETTING_MODIFICATION
AUE_SETSOCKOPT
NETWORK_CONNECTION
AUE_SETTIMEOFDAY
SETTING_MODIFICATION
AUE_SHUTDOWN
STATUS_SHUTDOWN
AUE_SOCKETPAIR
NETWORK_CONNECTION
AUE_SSAUTHINT
USER_LOGIN
AUE_SSAUTHMECH
USER_LOGIN
AUE_SSAUTHORIZE
USER_LOGIN
AUE_TASKFORPID
PROCESS_INJECTION
AUE_TASKNAMEFORPID
PROCESS_INJECTION
AUE_UNMOUNT
RESOURCE_READ
AUE_WAIT4
PROCESS_UNCATEGORIZED
PLAINTEXT_LOG_COLLECTION_EVENT
GENERIC_EVENT
SYSTEM_PERFORMANCE_METRICS
GENERIC_EVENT
Field mapping reference: JAMF_TELEMETRY
The following table lists the log fields of the
JAMF_TELEMETRY
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.event_type
metadata.product_name
The
metadata.product_name
UDM field is set to
JAMF_TELEMETRY
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
JAMF
.
header.time_seconds_epoch
metadata.event_timestamp
header.time_milliseconds_offset
about.labels[time_milliseconds_offset]
(deprecated)
header.time_milliseconds_offset
additional.fields[time_milliseconds_offset]
header.version
about.labels[header_version]
(deprecated)
header.version
additional.fields[header_version]
header.event_modifier
about.labels[event_modifier]
(deprecated)
header.event_modifier
additional.fields[event_modifier]
header.event_uuid
metadata.product_log_id
header.event_name,header.event_id
metadata.product_event_type
If the
header.event_name
and
header.event_id
log field values are
not
empty, then the
header.event_name-header.event_id
log fields are mapped to the
metadata.product_event_type
UDM field.
Else, if the
header.event_name
log field value is
not
empty, then the
header.event_name
log field is mapped to the
metadata.product_event_type
UDM field.
Else, if the
header.event_id
log field value is
not
empty, then the
header.event_id
log field is mapped to the
metadata.product_event_type
UDM field.
exec_chain.thread_uuid
principal.labels[exec_chain_thread_uuid]
(deprecated)
exec_chain.thread_uuid
additional.fields[exec_chain_thread_uuid]
exec_chain.uuid
principal.labels[exec_chain_uuid]
(deprecated)
exec_chain.uuid
additional.fields[exec_chain_uuid]
exec_chain_child.parent_path
principal.process.parent_process.file.full_path
exec_chain_child.parent_pid
principal.process.parent_process.pid
exec_chain_child.parent_uuidsubject.parent
(deprecated)
principal.labels[exec_chain_child_parent_uuid]
exec_chain_child.parent_uuid
additional.fields[exec_chain_child_parent_uuid]
host_info.serial_number
principal.asset.hardware.serial_number
host_info.host_name
principal.hostname
host_info.osversion
principal.asset.software.version
host_info.host_uuid
principal.asset.product_object_id
host_info.primary_mac_address
principal.asset.mac
identity.signer_id
principal.labels[identity_signer_id]
(deprecated)
identity.signer_id
additional.fields[identity_signer_id]
identity.team_id_truncated
principal.labels[identity_team_id_truncated]
(deprecated)
identity.team_id_truncated
additional.fields[identity_team_id_truncated]
identity.signer_id_truncated
principal.labels[identity_signer_id_truncated]
(deprecated)
identity.signer_id_truncated
additional.fields[identity_signer_id_truncated]
identity.cd_hash
principal.labels[identity_cd_hash]
(deprecated)
identity.cd_hash
additional.fields[identity_cd_hash]
identity.team_id
principal.labels[team_id]
(deprecated)
identity.team_id
additional.fields[team_id]
identity.signer_type
principal.labels[signer_type]
(deprecated)
identity.signer_type
additional.fields[signer_type]
key
about.labels[key]
(deprecated)
key
additional.fields[key]
return.error,return.description
security_result.description
If the
return.error
and
return.description
log field values are
not
empty, then the
return.error-return.description
log fields are mapped to the
security_result.description
UDM field.
Else, if the
return.error
log field value is
not
empty, then the
return.error
log field is mapped to the
security_result.description
UDM field.
Else, if the
return.description
log field value is
not
empty, then the
return.description
log field is mapped to the
security_result.description
UDM field.
return.return_value
security_result.detection_fields
subject.session_id
network.session_id
subject.group_id
principal.user.group_identifiers
If the
header.event_name
log field value contains one of the following values, then the
subject.group_id
log field is mapped to the
target.user.group_identifiers
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
Else, the
subject.group_id
log field is mapped to the
principal.user.group_identifiers
UDM field.
subject.effective_group_id
target.user.group_identifiers
If the
header.event_name
log field value does not contain one of the following values, then the
subject.effective_group_id
log field is mapped to the
target.user.group_identifiers
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
subject.group_name
principal.group.group_display_name
If the
header.event_name
log field value contains one of the following values, then the
subject.group_name
log field is mapped to the
target.group.group_display_name
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
Else, the
subject.group_name
log field is mapped to the
principal.group.group_display_name
UDM field.
subject.effective_group_name
target.group.group_display_name
If the
header.event_name
log field value does not contain one of the following values, then the
subject.effective_group_name
log field is mapped to the
target.group.group_display_name
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
subject.user_name
principal.user.user_display_name
If the
header.event_name
log field value contains one of the following values,  then the
subject.user_name
log field is mapped to the
target.user.user_display_name
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
Else, the
subject.user_name
log field is mapped to the
principal.user.user_display_name
UDM field.
subject.effective_user_name
target.user.user_display_name
If the
header.event_name
log field value does not contain one of the following values,  then the
subject.effective_user_name
log field is mapped to the
target.user.user_display_name
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
subject.user_id
principal.user.userid
If the
header.event_name
log field value contains one of the following values, then the
subject.user_id
log field is mapped to the
target.user.userid
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
Else, the
subject.user_id
log field is mapped to the
principal.user.userid
UDM field.
subject.effective_user_id
target.user.userid
If the
header.event_name
log field value does not contain one of the following values, then the
subject.effective_user_id
log field is mapped to the
target.user.userid
UDM field:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
subject.audit_id
principal.labels[audit_id]
(deprecated)
subject.audit_id
additional.fields[audit_id]
subject.responsible_process_id,metrics.tasks.pid
principal.process.pid
If the
header.event_name
log field value is equal to
SYSTEM_PERFORMANCE_METRICS
, then the
metrics.tasks.pid
log field is mapped to the
principal.process.pid
UDM field.
Else, the
subject.responsible_process_id
log field is mapped to the
principal.process.pid
UDM field.
subject.process_id
principal.process_ancestors.pid
If the
subject.responsible_process_id
log field value is
not
empty, then the
subject.process_id
log field is mapped to the
principal.process_ancestors.pid
UDM field.
Else, the
subject.process_id
log field is mapped to the
principal.process.pid
UDM field.
subject.audit_user_name
principal.labels[audit_user_name]
(deprecated)
subject.audit_user_name
additional.fields[audit_user_name]
subject.process_name
principal.process_ancestors.file.full_path
If the
subject.responsible_process_name
log field value is
not
empty, then the
subject.process_name
log field is mapped to the
principal.process_ancestors.file.full_path
UDM field.
Else, the
subject.process_name
log field is mapped to the
principal.process.file.full_path
UDM field.
subject.responsible_process_name
principal.process.file.full_path
subject.process_hash
principal.process.file.sha1
subject.terminal_id.type
principal.labels[type]
(deprecated)
If the
subject.terminal_id.type
log field value is equal to
4
, then the
principal.labels.key
UDM field is set to
subject_terminal_id_type
and the
principal.labels.value
UDM field is set to
4-IPv4
.
Else, if the
subject.terminal_id.type
log field value is equal to
6
, then the
principal.labels.key
UDM field is set to
subject_terminal_id_type
and the
principal.labels.value
UDM field is set to
6-IPv6
.
Else, the
principal.labels.key
UDM field is set to
subject_terminal_id_type
and the
subject.terminal_id.type
log field is mapped to the
principal.labels.value
UDM field.
subject.terminal_id.type
additional.fields[type]
If the
subject.terminal_id.type
log field value is equal to
4
, then the
additional.fields.key
UDM field is set to
subject_terminal_id_type
and the
additional.fields.value.string_value
UDM field is set to
4-IPv4
.
Else, if the
subject.terminal_id.type
log field value is equal to
6
, then the
additional.fields.key
UDM field is set to
subject_terminal_id_type
and the
additional.fields.value.string_value
UDM field is set to
6-IPv6
.
Else, the
additional.fields.key
UDM field is set to
subject_terminal_id_type
and the
subject.terminal_id.type
log field is mapped to the
additional.fields.value.string_value
UDM field.
subject.terminal_id.ip_address
principal.ip
subject.terminal_id.port
principal.port
texts
metadata.description
If the
index
value is equal to
0
, then the
texts
log field is mapped to the
metadata.description
UDM field.
Else, the
texts
log field is mapped to the
about.labels.value
UDM field.
attributes.device
principal.asset.attribute.labels[device]
attributes.owner_group_name
about.group.group_display_name
attributes.owner_group_id
about.user.group_identifiers
attributes.owner_user_id
about.user.userid
attributes.owner_user_name
about.user.user_display_name
attributes.file_system_id
principal.labels[attributes_file_system_id]
(deprecated)
attributes.file_system_id
additional.fields[attributes_file_system_id]
attributes.file_access_mode
principal.labels[attributes_file_access_mode]
(deprecated)
attributes.file_access_mode
additional.fields[attributes_file_access_mode]
attributes.node_id
principal.asset.asset_id
path
about.labels[path]
arguments.cmd
principal.labels[arguments_cmd]
(deprecated)
arguments.cmd
additional.fields[arguments_cmd]
arguments.policy
principal.labels[arguments_policy]
(deprecated)
arguments.policy
additional.fields[arguments_policy]
arguments.length
principal.labels[arguments_length]
(deprecated)
arguments.length
additional.fields[arguments_length]
_event_score
security_result.severity_details
architecture
principal.asset.hardware.cpu_model
arguments.addr
principal.labels[arguments_addr]
(deprecated)
arguments.addr
additional.fields[arguments_addr]
arguments.am_failure
principal.labels[arguments_am_failure]
(deprecated)
arguments.am_failure
additional.fields[arguments_am_failure]
arguments.am_success
principal.labels[arguments_am_success]
(deprecated)
arguments.am_success
additional.fields[arguments_am_success]
arguments.authenticated_as_test
principal.labels[arguments_authenticated_as_test]
(deprecated)
arguments.authenticated_as_test
additional.fields[arguments_authenticated_as_test]
arguments.child_PID
principal.labels[arguments_child_PID]
(deprecated)
arguments.child_PID
additional.fields[arguments_child_PID]
arguments.data
principal.labels[arguments_data]
(deprecated)
arguments.data
additional.fields[arguments_data]
arguments.domain
principal.labels[arguments_domain]
(deprecated)
arguments.domain
additional.fields[arguments_domain]
arguments.fd
principal.labels[arguments_fd]
(deprecated)
arguments.fd
additional.fields[arguments_fd]
arguments.flags
principal.labels[arguments_flags]
(deprecated)
arguments.flags
additional.fields[arguments_flags]
arguments.authenticated_as_allen.golbig
principal.labels[authenticated_as_allen_golbig]
(deprecated)
arguments.authenticated_as_allen.golbig
additional.fields[authenticated_as_allen_golbig]
arguments.known_UID_
principal.labels[argument_known_uid]
(deprecated)
arguments.known_UID_
additional.fields[argument_known_uid]
arguments.pid
principal.labels[arguments_pid]
(deprecated)
arguments.pid
additional.fields[arguments_pid]
arguments.port
principal.labels[arguments_port]
(deprecated)
arguments.port
additional.fields[arguments_port]
arguments.priority
security_result.priority_details
arguments.process
principal.labels[argument_process]
(deprecated)
arguments.process
additional.fields[argument_process]
arguments.protocol
principal.labels[argument_protocol]
(deprecated)
arguments.protocol
additional.fields[argument_protocol]
arguments.request
principal.labels[argument_request]
(deprecated)
arguments.request
additional.fields[argument_request]
arguments.sflags
principal.labels[arguments_sflags]
(deprecated)
arguments.sflags
additional.fields[arguments_sflags]
arguments.signal
principal.labels[argument_signal]
(deprecated)
arguments.signal
additional.fields[argument_signal]
arguments.target_port,process.terminal_id.port,socket_inet.port
target.port
If the
header.event_name
log field value is equal to
AUE_KILL
or
AUE_TASKFORPID
, then the
process.port
log field is mapped to the
target.port
UDM field.
Else, if the
header.event_name
log field value is equal to
AUE_BIND
or
AUE_CONNECT
, then the
socket_inet.port
log field is mapped to the
target.port
UDM field.
Else, the
agument.target_port
log field is mapped to the
target.port
UDM field.
arguments.task_port
principal.labels[task_port]
(deprecated)
arguments.task_port
additional.fields[task_port]
arguments.type
principal.labels[argument_type]
(deprecated)
arguments.type
additional.fields[argument_type]
arguments.which
principal.labels[which]
(deprecated)
arguments.which
additional.fields[which]
arguments.who
principal.labels[who]
(deprecated)
arguments.who
additional.fields[who]
bios_firmware_versions.booter-version
principal.asset.attribute.labels[booter_version]
bios_firmware_versions.firmware-features
principal.asset.attribute.labels[firmware_features]
bios_firmware_versions.firmware-version
principal.asset.attribute.labels[firmware_version]
bios_firmware_versions.release-date
principal.asset.attribute.labels[release_date]
bios_firmware_versions.rom-size
principal.asset.attribute.labels[rom_size]
bios_firmware_versions.system-firmware-version
principal.asset.attribute.labels[system_firmware_version]
bios_firmware_versions.vendor
principal.asset.attribute.labels[vendor]
bios_firmware_versions.version
principal.asset.attribute.labels[version]
exec_args.args_compiled
principal.process.command_line
exec_chain_parent.uuid
principal.labels[parent_uuid]
(deprecated)
exec_chain_parent.uuid
additional.fields[parent_uuid]
exec_env.env_compiled
about.labels[env_compiled]
(deprecated)
exec_env.env_compiled
additional.fields[env_compiled]
exec_env.env.PATH
about.labels[env_path]
(deprecated)
exec_env.env.PATH
additional.fields[env_path]
exit.return_value
principal.labels[return_value]
(deprecated)
exit.return_value
additional.fields[return_value]
exit.status
principal.labels[exit_status]
(deprecated)
exit.status
additional.fields[exit_status]
process.audit_id
about.labels[process_audit_id]
(deprecated)
process.audit_id
additional.fields[process_audit_id]
process.audit_user_name
about.labels[audit_user_name]
(deprecated)
process.audit_user_name
additional.fields[audit_user_name]
process.group_idprocess.effective_group_id
about.user.group_identifiers
process.group_name
about.group.group_display_name
process.process_hash
target.process.file.sha1
process.process_id
target.process.pid
process.process_name
target.process.file.full_path
process.session_id
target.labels[process_session_id]
(deprecated)
process.session_id
additional.fields[process_session_id]
process.terminal_id.addr
target.labels[addr]
process.terminal_id.ip_address
target.ip
process.terminal_id.type
target.labels[process_terminal_id_type]
(deprecated)
If the
process.terminal_id.type
log field value is equal to
4
, then the
target.labels.key
UDM field is set to
process_terminal_id_type
and the
target.labels.value
UDM field is set to
4-IPv4
.
Else, if the
subject.terminal_id.type
log field value is equal to
6
, then the
target.labels.key
UDM field is set to
process_terminal_id_type
and the
target.labels.value
UDM field is set to
6-IPv6
.
Else, the
target.labels.key
UDM field is set to
process_terminal_id_type
and the
process.terminal_id.type
log field is mapped to the
target.labels.value
UDM field.
process.terminal_id.type
additional.fields[process_terminal_id_type]
If the
process.terminal_id.type
log field value is equal to
4
, then the
additional.fields.key
UDM field is set to
process_terminal_id_type
and the
additional.fields.value.string_value
UDM field is set to
4-IPv4
.
Else, if the
subject.terminal_id.type
log field value is equal to
6
, then the
additional.fields.key
UDM field is set to
process_terminal_id_type
and the
additional.fields.value.string_value
UDM field is set to
6-IPv6
.
Else, the
additional.fields.key
UDM field is set to
process_terminal_id_type
and the
process.terminal_id.type
log field is mapped to the
additional.fields.value.string_value
UDM field.
process.user_id
about.user.userid
process.user_name
about.user.user_display_name
rateLimitingSeconds
about.labels[rate_limiting_seconds]
(deprecated)
rateLimitingSeconds
additional.fields[rate_limiting_seconds]
socket_inet.family
target.labels[socket_inet_family]
(deprecated)
socket_inet.family
additional.fields[socket_inet_family]
socket_inet.id
target.labels[socket_inet_id]
(deprecated)
If the
socket_inet.id
log field value is equal to
128
, then the
target.labels.key
UDM field is set to
socket_inet_id
and the
target.labels.value
UDM field is set to
128-IPv4
.
Else, if the
socket_inet.id
log field value is equal to
129
, then the
target.labels.key
UDM field is set to
socket_inet_id
and the
target.labels.value
UDM field is set to
129-IPv6
.
Else, the
target.labels.key
UDM field is set to
socket_inet_id
and the
socket_inet.ip
log field is mapped to the
target.labels.value
UDM field.
socket_inet.id
additional.fields[socket_inet_id]
If the
socket_inet.id
log field value is equal to
128
, then the
additional.fields.key
UDM field is set to
socket_inet_id
and the
additional.fields.value.string_value
UDM field is set to
128-IPv4
.
Else, if the
socket_inet.id
log field value is equal to
129
, then the
additional.fields.key
UDM field is set to
socket_inet_id
and the
additional.fields.value.string_value
UDM field is set to
129-IPv6
.
Else, the
additional.fields.key
UDM field is set to
socket_inet_id
and the
socket_inet.ip
log field is mapped to the
additional.fields.value.string_value
UDM field.
socket_inet.ip_address
target.ip
socket_unix.family
target.labels[socket_unix_family]
(deprecated)
socket_unix.family
additional.fields[socket_unix_family]
socket_unix.path
target.file.full_path
subject.terminal_id.addr
target.labels[addr]
metrics.hw_model
principal.asset.hardware.model
metrics.tasks.bytes_received
network.received_bytes
If the
index
value is equal to
0
, then the
metrics.tasks.bytes_received
log field is mapped to the
network.received_bytes
UDM field.
Else, the
metrics.tasks.bytes_received
log field is mapped to the
principal.asset.attribute.labels.value
UDM field.
metrics.tasks.bytes_received_per_s
principal.asset.attribute.labels[bytes_received_per_s]
metrics.tasks.bytes_sent
network.sent_bytes
If the
index
value is equal to
0
, then the
metrics.tasks.bytes_sent
log field is mapped to the
network.sent_bytes
UDM field.
Else, the
metrics.tasks.bytes_sent
log field is mapped to the
principal.asset.attribute.labels.value
UDM field.
metrics.tasks.bytes_sent_per_s
principal.asset.attribute.labels[bytes_sent_per_s]
metrics.tasks.cputime_ms_per_s
principal.asset.attribute.labels[cputime_ms_per_s]
metrics.tasks.cputime_ns
principal.asset.attribute.labels[cputime_ns]
metrics.tasks.cputime_sample_ms_per_s
principal.asset.attribute.labels[cputime_sample_ms_per_s]
metrics.tasks.cputime_userland_ratio
principal.asset.attribute.labels[cputime_userland_ratio]
metrics.tasks.diskio_bytesread
principal.asset.attribute.labels[diskio_bytesread]
metrics.tasks.diskio_bytesread_per_s
principal.asset.attribute.labels[diskio_bytesread_per_s]
metrics.tasks.diskio_byteswritten
principal.asset.attribute.labels[diskio_byteswritten]
metrics.tasks.diskio_byteswritten_per_s
principal.asset.attribute.labels[diskio_byteswritten_per_s]
metrics.tasks.energy_impact
principal.asset.attribute.labels[energy_impact]
metrics.tasks.energy_impact_per_s
principal.asset.attribute.labels[energy_impact_per_s]
metrics.tasks.idle_wakeups
principal.asset.attribute.labels[idle_wakeups]
metrics.tasks.interval_ns
principal.asset.attribute.labels[interval_ns]
metrics.tasks.intr_wakeups_per_s
principal.asset.attribute.labels[intr_wakeups_per_s]
metrics.tasks.name
principal.asset.attribute.labels[name]
metrics.tasks.packets_received
network.received_packets
If the
index
value is equal to
0
, then the
metrics.tasks.packets_received
log field is mapped to the
network.received_packets
UDM field.
Else, the
metrics.tasks.packets_received
log field is mapped to the
principal.asset.attribute.labels.value
UDM field.
metrics.tasks.packets_received_per_s
principal.asset.attribute.labels[packets_received_per_s]
metrics.tasks.packets_sent
network.sent_packets
If the
index
value is equal to
0
, then the
metrics.tasks.packets_sent
log field is mapped to the
network.sent_packets
UDM field.
Else, the
metrics.tasks.packets_sent
log field is mapped to the
principal.asset.attribute.labels.value
UDM field.
metrics.tasks.packets_sent_per_s
principal.asset.attribute.labels[packets_sent_per_s]
metrics.tasks.pageins
principal.asset.attribute.labels[pageins]
metrics.tasks.pageins_per_s
principal.asset.attribute.labels[pageins_per_s]
metrics.tasks.qos_background_ms_per_s
principal.asset.attribute.labels[qos_background_ms_per_s]
metrics.tasks.qos_background_ns
principal.asset.attribute.labels[qos_background_ns]
metrics.tasks.qos_default_ms_per_s
principal.asset.attribute.labels[qos_default_ms_per_s]
metrics.tasks.qos_default_ns
principal.asset.attribute.labels[qos_default_ns]
metrics.tasks.qos_disabled_ms_per_s
principal.asset.attribute.labels[qos_disabled_ms_per_s]
metrics.tasks.qos_disabled_ns
principal.asset.attribute.labels[qos_disabled_ns]
metrics.tasks.qos_maintenance_ms_per_s
principal.asset.attribute.labels[qos_maintenance_ms_per_s]
metrics.tasks.qos_maintenance_ns
principal.asset.attribute.labels[qos_maintenance_ns]
metrics.tasks.qos_user_initiated_ms_per_s
principal.asset.attribute.labels[qos_user_initiated_ms_per_s]
metrics.tasks.qos_user_initiated_ns
principal.asset.attribute.labels[qos_user_initiated_ns]
metrics.tasks.qos_user_interactive_ms_per_s
principal.asset.attribute.labels[qos_user_interactive_ms_per_s]
metrics.tasks.qos_user_interactive_ns
principal.asset.attribute.labels[qos_user_interactive_ns]
metrics.tasks.qos_utility_ms_per_s
principal.asset.attribute.labels[qos_utility_ms_per_s]
metrics.tasks.qos_utility_ns
principal.asset.attribute.labels[qos_utility_ns]
metrics.tasks.started_abstime_ns
principal.asset.attribute.labels[started_abstime_ns]
metrics.tasks.timer_wakeups.wakeups
principal.asset.attribute.labels[timer_wakeups]
page_info.page
about.labels[page_info_page]
(deprecated)
page_info.page
additional.fields[page_info_page]
page_info.total
about.labels[page_info_total]
(deprecated)
page_info.total
additional.fields[page_info_total]
exec_env.env._
about.labels[env]
(deprecated)
exec_env.env._
additional.fields[env]
exec_env.env.__CF_USER_TEXT_ENCODING
about.labels[env__CF_USER_TEXT_ENCODING]
(deprecated)
exec_env.env.__CF_USER_TEXT_ENCODING
additional.fields[env__CF_USER_TEXT_ENCODING]
exec_env.env.__CFBundleIdentifier
about.labels[env__CFBundleIdentifier]
(deprecated)
exec_env.env.__CFBundleIdentifier
additional.fields[env__CFBundleIdentifier]
exec_env.env.ASDF_DIR
about.labels[env_ASDF_DIR]
(deprecated)
exec_env.env.ASDF_DIR
additional.fields[env_ASDF_DIR]
exec_env.env.HOME
about.labels[env_HOME]
(deprecated)
exec_env.env.HOME
additional.fields[env_HOME]
exec_env.env.LANG
about.labels[env_LANG]
(deprecated)
exec_env.env.LANG
additional.fields[env_LANG]
exec_env.env.LC_TERMINAL
about.labels[env_LC_TERMINAL]
(deprecated)
exec_env.env.LC_TERMINAL
additional.fields[env_LC_TERMINAL]
exec_env.env.LC_TERMINAL_VERSION
about.labels[env_LC_TERMINAL_VERSION]
(deprecated)
exec_env.env.LC_TERMINAL_VERSION
additional.fields[env_LC_TERMINAL_VERSION]
exec_env.env.MAIL
about.labels[env_MAIL]
(deprecated)
exec_env.env.MAIL
additional.fields[env_MAIL]
exec_env.env.MallocSpaceEfficient
about.labels[env_MallocSpaceEfficient]
(deprecated)
exec_env.env.MallocSpaceEfficient
additional.fields[env_MallocSpaceEfficient]
exec_env.env.OLDPWD
about.labels[env_OLDPWD]
(deprecated)
exec_env.env.OLDPWD
additional.fields[env_OLDPWD]
exec_env.env.PWD
about.file.full_path
exec_env.env.SHELL
about.labels[env_SHELL]
(deprecated)
exec_env.env.SHELL
additional.fields[env_SHELL]
exec_env.env.SHLVL
about.labels[env_SHLVL]
(deprecated)
exec_env.env.SHLVL
additional.fields[env_SHLVL]
exec_env.env.SSH_AUTH_SOCK
about.labels[env_SSH_AUTH_SOCK]
(deprecated)
exec_env.env.SSH_AUTH_SOCK
additional.fields[env_SSH_AUTH_SOCK]
exec_env.env.SSH_CLIENT
about.labels[env_SSH_CLIENT]
(deprecated)
exec_env.env.SSH_CLIENT
additional.fields[env_SSH_CLIENT]
exec_env.env.SSH_CONNECTION
about.labels[env_SSH_CONNECTION]
(deprecated)
exec_env.env.SSH_CONNECTION
additional.fields[env_SSH_CONNECTION]
exec_env.env.SSH_TTY
about.labels[env_SSH_TTY]
(deprecated)
exec_env.env.SSH_TTY
additional.fields[env_SSH_TTY]
exec_env.env.SUDO_COMMAND
about.labels[env_SUDO_COMMAND]
(deprecated)
exec_env.env.SUDO_COMMAND
additional.fields[env_SUDO_COMMAND]
exec_env.env.SUDO_GID
about.user.group_identifiers
exec_env.env.SUDO_UID
about.user.userid
exec_env.env.SUDO_USER
about.user.user_display_name
exec_env.env.TERM
about.labels[env_TERM]
(deprecated)
exec_env.env.TERM
additional.fields[env_TERM]
exec_env.env.LOGNAME
about.labels[env_LOGNAME]
(deprecated)
exec_env.env.LOGNAME
additional.fields[env_LOGNAME]
exec_env.env.USER
about.labels[env_USER]
(deprecated)
exec_env.env.USER
additional.fields[env_USER]
exec_env.env.TERM_PROGRAM
about.labels[env_TERM_PROGRAM]
(deprecated)
exec_env.env.TERM_PROGRAM
additional.fields[env_TERM_PROGRAM]
exec_env.env.TERM_PROGRAM_VERSION
about.labels[env_TERM_PROGRAM_VERSION]
(deprecated)
exec_env.env.TERM_PROGRAM_VERSION
additional.fields[env_TERM_PROGRAM_VERSION]
exec_env.env.TERM_SESSION_ID
about.labels[env_TERM_SESSION_ID]
(deprecated)
exec_env.env.TERM_SESSION_ID
additional.fields[env_TERM_SESSION_ID]
exec_env.env.TMPDIR
about.labels[env_TMPDIR]
(deprecated)
exec_env.env.TMPDIR
additional.fields[env_TMPDIR]
exec_env.env.XPC_FLAGS
about.labels[env_XPC_FLAGS]
(deprecated)
exec_env.env.XPC_FLAGS
additional.fields[env_XPC_FLAGS]
exec_env.env.XPC_SERVICE_NAME
about.labels[env_XPC_SERVICE_NAME]
(deprecated)
exec_env.env.XPC_SERVICE_NAME
additional.fields[env_XPC_SERVICE_NAME]
target.resource.resource_type
If the
header.event_name
log field value is equal to
AUE_GETAUID
, then the
target.resource.resource_type
UDM field is set to
TASK
.
Else, if the
header.event_name
log field value is equal to
AUE_SETPRIORITY or AUE_SETTIMEOFDAY
, then the
target.resource.resource_type
UDM field is set to
SETTING
.
extensions.auth.mechanism
If the
header.event_name
log field value contains one of the following values,  then the
mechanism
UDM field is set to
USERNAME_PASSWORD
:
AUE_auth_user
AUE_logout
AUE_lw_login
AUE_openssh
AUE_SESSION_CLOSE
AUE_SESSION_END
AUE_SESSION_START
AUE_ssauthint
AUE_ssauthmech
AUE_ssauthorize
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
