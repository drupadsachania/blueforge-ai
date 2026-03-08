# Collect Jamf Protect logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-protect/  
**Scraped:** 2026-03-05T09:17:28.830209Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Jamf Protect logs
Supported in:
Google secops
SIEM
This document describes how you can collect Jamf Protect logs by setting up a Google Security Operations
feed and how log fields map to Google Security Operations Unified Data Model (UDM) fields.
This document also lists the supported Jamf Protect version.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Jamf Protect and the Google Security Operations feed configured to send logs to Google Security Operations. Each customer deployment can differ and might be more
complex.
The deployment contains the following components:
Jamf Protect
. The Jamf Protect platform from which you collect logs.
Google Security Operations feed
. The Google Security Operations feed that fetches logs from Jamf Protect and writes logs to Google Security Operations.
Google Security Operations
. Google Security Operations retains and analyzes the logs from Jamf Protect.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
JAMF_PROTECT
ingestion label.
Before you begin
Ensure you have the following prerequisites:
A
Jamf Protect
set up
Jamf Protect version 4.0.0 or later
All systems in the deployment architecture are configured with the UTC time zone.
Set up feeds
You can use either Amazon S3 or a webhook to set up an ingestion feed in Google SecOps.
To configure this log type, follow these steps:
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
Specify the values for the following fields:
Source Type
: Webhook (Recommended)
Split delimiter
: The delimiter that is used to separate log lines, such as
\n
.
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
Set up Jamf Protect for a webhook feed
In the Jamf Protect application, navigate to the related
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
Alerts & Unified Logs
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
Supported Jamf Protect log types
The following table lists the log types that the Jamf Protect parser supports:
Event Type
Display name
GPClickEvent
Synthetic Click Events
GPDownloadEvent
Download Events
GPFSEvent
File System Events
GPGatekeeperEvent
Gatekeeper Events
GPKeylogRegisterEvent
Keylogger Events
GPMRTEvent
Monitor Events
GPPreventedExecutionEvent
Custom Prevent List Events
GPProcessEvent
Process Events
GPThreatMatchExecEvent
Threat Prevention Events
GPUSBEvent
USB Events
GPUnifiedLogEvent
Unified Log Events
Auth-mount
Device Controls Events
Supported Jamf Protect log formats
The Jamf Protect parser supports logs in JSON format.
Supported Jamf Protect sample logs
JSON
{
  "input": {
    "match": {
      "custom": false,
      "facts": [
        {
          "actions": [
            {
              "name": "CacheFile",
              "parameters": {}
            },
            {
              "name": "Report",
              "parameters": {}
            }
          ],
          "human": "Login Hook created for persistence",
          "context": [
            {
              "name": "ItemBinary",
              "value": "\\/path\\/to\\/suspiciousfile.sh",
              "valueType": "Binary"
            },
            {
              "name": "Itemname",
              "value": "\\/path\\/to\\/suspiciousfile.sh",
              "valueType": "String"
            }
          ],
          "uuid": "dummyuuid",
          "version": 2,
          "severity": 0,
          "tags": [
            "MITREattack",
            "T1037.002",
            "BootOrLogonAutostartExecution",
            "Persistence"
          ],
          "name": "LoginHook"
        }
      ],
      "event": {
        "timestamp": 1676994504.698714,
        "uid": 0,
        "eventID": 9141,
        "prevFile": "\\/private\\/var\\/folders\\/zz\\/zyxvpxvq6csfxvn_n0000000000000\\/T\\/TemporaryItems\\/com.apple.loginwindow.plist.X0YcxtR",
        "iNode": 62898,
        "dev": 16777220,
        "uuid": "AE7F101A-09AA-4CD6-940F-15EC2073E476",
        "path": "\\/var\\/root\\/Library\\/Preferences\\/com.dummy.path.plist",
        "type": 3,
        "gid": 0,
        "pid": 148
      },
      "uuid": "1263F6F0-6891-4105-993F-6889AB3A3555",
      "context": [
        {
          "name": "ItemBinary",
          "value": "\\/path\\/to\\/suspiciousfile.sh",
          "valueType": "Binary"
        },
        {
          "name": "Itemname",
          "value": "\\/path\\/to\\/suspiciousfile.sh",
          "valueType": "String"
        }
      ],
      "severity": 0,
      "tags": [
        "T1037.002",
        "Persistence",
        "BootOrLogonAutostartExecution",
        "MITREattack"
      ],
      "actions": [
        {
          "name": "CacheFile",
          "parameters": {}
        },
        {
          "name": "Report",
          "parameters": {}
        }
      ]
    },
    "host": {
      "ips": [
        "192.51.100.1"
      ],
      "provisioningUDID": "8AD54CA5-F0DC-5434-8147-26D1D8A426CD",
      "hostname": "dummy-hostname",
      "serial": "dummyserial"
    },
    "eventType": "GPFSEvent",
    "related": {
      "users": [
        {
          "uid": 0,
          "name": "root",
          "uuid": "dummyuid"
        }
      ],
      "files": [
        {
          "xattrs": [],
          "sha256hex": "67fc9bde97641361d3b521a01f8b907269a4d6434f2db10e163a71b70178b3d1",
          "modified": 1676985886,
          "uid": 0,
          "changed": 1676985886,
          "sha1hex": "e3bc8f9c241f86e7138ba6cfb0e0e206b131a7e3",
          "isAppBundle": false,
          "isScreenShot": false,
          "path": "\\/var\\/root\\/Library\\/Preferences\\/com.apple.loginwindow.plist",
          "size": 42,
          "gid": 0,
          "inode": 62898,
          "mode": 33152,
          "isDownload": false,
          "created": 1676985886,
          "accessed": 1676985886,
          "fsid": 16777220,
          "signingInfo": {
            "status": -67062,
            "authorities": [],
            "teamid": "",
            "signerType": 4,
            "statusMessage": "code object is not signed at all",
            "entitlements": [],
            "appid": ""
          },
          "isDirectory": false
        }
      ],
      "binaries": [
        {
          "xattrs": [],
          "sha256hex": "9a282c0623110b57953bb74238f02704f729eb9779381eef851b2ebe7626f890",
          "modified": 1675935593,
          "uid": 0,
          "changed": 1675935593,
          "sha1hex": "454634df6b7cd32a4dcca9d346eb3efb34dc780d",
          "isAppBundle": false,
          "isScreenShot": false,
          "path": "\\/usr\\/sbin\\/cfprefsd",
          "size": 200608,
          "gid": 0,
          "inode": 1152921500312430765,
          "mode": 33261,
          "isDownload": false,
          "created": 1675935593,
          "accessed": 1675935593,
          "fsid": 16777220,
          "signingInfo": {
            "status": 0,
            "cdhash": "SXboWMc7MOtMM0K3pOxRjqR59w0=",
            "authorities": [
              "Software Signing",
              "Apple Code Signing Certification Authority",
              "Apple Root CA"
            ],
            "teamid": "",
            "signerType": 0,
            "statusMessage": "No error.",
            "entitlements": [],
            "appid": "com.dummy.domain"
          },
          "isDirectory": false
        }
      ],
      "groups": [
        {
          "gid": 0,
          "name": "wheel",
          "uuid": "FVFZQ5FDLYWG0"
        }
      ],
      "processes": [
        {
          "originalParentPID": 1,
          "uuid": "06D1425D-082A-4E11-81E4-75A9E3F2B8EF",
          "ruid": 0,
          "uid": 0,
          "startTimestamp": 1676976036,
          "ppid": 1,
          "path": "\\/usr\\/sbin\\/cfprefsd",
          "gid": 0,
          "rgid": 0,
          "args": [
            "\\/usr\\/sbin\\/cfprefsd",
            "daemon"
          ],
          "signingInfo": {
            "status": 0,
            "cdhash": "SXboWMc7MOtMM0K3pOxRjqR59w0=",
            "authorities": [
              "Software Signing",
              "Apple Code Signing Certification Authority",
              "Apple Root CA"
            ],
            "teamid": "",
            "signerType": 0,
            "statusMessage": "No error.",
            "entitlements": [],
            "appid": "com.dummy.domain"
          },
          "pid": 148,
          "name": "dummyhostname",
          "pgid": 148
        }
      ]
    }
  },
  "caid": "a2afe04d1360c01a0758ad3319c9af305f794801917b0c04648e4d7a9d7d746b",
  "certid": "05f5b0fa822a2f5e9a29f018853e8f2d99b94c8af38f40268a9479f2e6038e6b"
}
Field mapping reference
This section explains how the Google Security Operations parser maps Jamf Protect fields to Google Security Operations Unified Data Model (UDM) fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
JAMF_PROTECT
log types and their corresponding UDM event types.
Event Identifier
Event Type
GPClickEvent
SCAN_UNCATEGORIZED
GPDownloadEvent
SCAN_FILE
GPFSEvent
SCAN_FILE
GPGatekeeperEvent
SCAN_UNCATEGORIZED
GPKeylogRegisterEvent
SCAN_UNCATEGORIZED
GPMRTEvent
SCAN_UNCATEGORIZED
GPPreventedExecutionEvent
SCAN_UNCATEGORIZED
GPProcessEvent
SCAN_PROCESS
GPThreatMatchExecEvent
SCAN_UNCATEGORIZED
GPUSBEvent
SCAN_UNCATEGORIZED
GPUnifiedLogEvent
SCAN_UNCATEGORIZED
GPScreenshotEvent
SCAN_UNCATEGORIZED
Auth-mount
SCAN_UNCATEGORIZED
Field mapping reference: JAMF_PROTECT
The following table lists the log fields of the
JAMF_PROTECT
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
about.platform
The
about.platform
UDM field is set to
MAC
.
caid
about.labels[caid]
(deprecated)
caid
additional.fields[caid]
certid
principal.asset.attribute.labels [certid]
context.identity.claims.certid
principal.user.attribute.permissions.description
context.identity.claims.clientid
principal.user.attribute.labels [context_identity_claims_clientid]
input.eventType
metadata.product_event_type
input.host.hostname
principal.hostname
input.host.ips
principal.ip
input.host.os
principal.platform_version
input.host.protectVersion
principal.asset.attribute.labels [input_host_protectversion]
input.match.version
additional.fields [input_match_version]
input.match.facts.matchReason
security_result.detection_fields [input_match_facts_matchreason]
input.related.files.objectType
additional.fields [input_related_files_objecttype]
input.host.provisioningUDID
principal.asset.product_object_id
input.host.serial
principal.asset.hardware.serial_number
input.match.actions.name
security_result.outcomes [input_match_actions_name]
input.match.actions.parameters.message
security_result.summary
If the
index
value is equal to
0
, then the
input.match.actions.parameters.message
log field is mapped to the
security_result.summary
UDM field.
Else, the
input.match.actions.parameters.message
log field is mapped to the
security_result.detection_fields.value
UDM field.
input.match.actions.parameters.title
security_result.description
If the
index
value is equal to
0
, then the
input.match.actions.parameters.title
log field is mapped to the
security_result.description
UDM field.
Else, the
input.match.actions.parameters.title
log field is mapped to the
security_result.detection_fields.value
UDM field.
input.match.context.name
security_result.detection_fields.key
input.match.context.value
security_result.detection_fields.value [Name]
input.match.context.valueType
input.match.custom
security_result.detection_fields [input_match_custom]
input.match.event.blocked
security_result.action
If the
input.match.event.blocked
log field value is
not
empty, then the
security_result.action
UDM field is set to
BLOCK
.
context.identity.claims.hd, input.match.uuid
security_result.url_back_to_product
The
security_result.url_back_to_product
UDM field is set to
https://context.identity.claims.hd.jamfcloud.com/Alerts/input.match.uuid
.
input.match.event.category
security_result.category_details
input.match.event.clickType
principal.labels[input_match_event_click_type]
(deprecated)
If the
input.match.event.clickType
log field value is equal to
0
, then the
principal.labels.value
UDM field is set to
0 - Other
.
Else, if the
input.match.event.clickType
log field value is equal to
1
, then the
principal.labels.value
UDM field is set to
1 - Left Down
.
Else, if the
input.match.event.clickType
log field value is equal to
2
, then the
principal.labels.value
UDM field is set to
2 - Left Up
.
Else, if the
input.match.event.clickType
log field value is equal to
3
, then the
principal.labels.value
UDM field is set to
3 - Right Down
.
Else, if the
input.match.event.clickType
log field value is equal to
4
, then the
principal.labels.value
UDM field is set to
4 - Right Up
.
input.match.event.clickType
additional.fields[input_match_event_click_type]
If the
input.match.event.clickType
log field value is equal to
0
, then the
additional.fields.value.string_value
UDM field is set to
0 - Other
.
Else, if the
input.match.event.clickType
log field value is equal to
1
, then the
additional.fields.value.string_value
UDM field is set to
1 - Left Down
.
Else, if the
input.match.event.clickType
log field value is equal to
2
, then the
additional.fields.value.string_value
UDM field is set to
2 - Left Up
.
Else, if the
input.match.event.clickType
log field value is equal to
3
, then the
additional.fields.value.string_value
UDM field is set to
3 - Right Down
.
Else, if the
input.match.event.clickType
log field value is equal to
4
, then the
additional.fields.value.string_value
UDM field is set to
4 - Right Up
.
input.match.event.composedMessage
principal.labels[input_match_event_composed_message]
(deprecated)
input.match.event.composedMessage
additional.fields[input_match_event_composed_message]
input.match.event.dev
principal.labels[input_match_event_dev]
(deprecated)
input.match.event.dev
additional.fields[input_match_event_dev]
input.match.event.eventID
principal.labels[input_match_event_eventID]
(deprecated)
input.match.event.eventID
additional.fields[input_match_event_eventID]
input.match.event.gid
principal.user.group_identifiers
input.match.event.iNode
target.file.stat_inode
input.match.event.matchType
principal.labels[input_match_event_match_type]
(deprecated)
input.match.event.matchType
additional.fields[input_match_event_match_type]
input.match.event.matchValue
security_result.threat_name
If the
input.match.event.matchType
log field value is
not
empty, then the
input.match.event.matchValue
log field is mapped to the
security_result.threat_name
UDM field.
input.match.event.name
about.labels[input_match_event_name]
(deprecated)
input.match.event.name
additional.fields[input_match_event_name]
input.match.facts.name
metadata.description
If the
index
value is equal to
0
, then the
input.match.facts.name
log field is mapped to the
metadata.description
UDM field.
input.match.event.path
target.process.file.full_path
input.match.event.pid
principal.process.pid
input.match.event.prevFile
src.file.full_path
If the
input.match.event.prevFile
log field value is
not
empty, then the
input.match.event.prevFile
log field is mapped to the
src.file.full_path
UDM field.
input.match.event.process
principal.process.file.names
input.match.event.process.args
target.process.command_line_history
input.match.event.process.gid
target.group.product_object_id
input.match.event.process.name
target.process.file.names
input.match.event.process.originalParentPID
target.process.parent_process.pid
input.match.event.process.path
target.process.file.full_path
input.match.event.process.pgid
target.labels[input_match_event_processes_pgid]
(deprecated)
input.match.event.process.pgid
additional.fields[input_match_event_processes_pgid]
input.match.event.process.pid
target.process.pid
input.match.event.process.ppid
target.labels[input_match_event_process_ppid]
(deprecated)
input.match.event.process.ppid
additional.fields[input_match_event_process_ppid]
input.match.event.process.responsiblePID
target.labels[input_match_event_process_responsible_pid]
(deprecated)
input.match.event.process.responsiblePID
additional.fields[input_match_event_process_responsible_pid]
input.match.event.process.rgid
target.labels[input_match_event_process_rgid]
(deprecated)
input.match.event.process.rgid
additional.fields[input_match_event_process_rgid]
input.match.event.process.ruid
target.labels[input_match_event_process_ruid]
(deprecated)
input.match.event.process.ruid
additional.fields[input_match_event_process_ruid]
input.match.event.process.signingInfo.appid
target.user.attribute.labels [input_match_event_process_sign_appid]
input.match.event.process.signingInfo.authorities
target.user.attribute.permissions
input.match.event.process.signingInfo.cdhash
target.user.attribute.labels [input_match_event_process_sign_cdhash]
input.match.event.process.signingInfo.entitlements
target.user.attributes.permissions
input.match.event.process.signingInfo.signerType
target.user.attribute.labels [input_match_event_process_sign_signer_type]
If the
input.related.process.signingInfo.signerType
log field value is equal to
0
, then the
target.user.attribute.labels.value
UDM field is set to
0 - Apple
.
Else, if the
input.related.process.signingInfo.signerType
log field value is equal to
1
, then the
target.user.attribute.labels.value
UDM field is set to
1 - App Store
.
Else, if the
input.related.process.signingInfo.signerType
log field value is equal to
2
, then the
target.user.attribute.labels.value
UDM field is set to
2 - Developer
.
Else, if the
input.related.process.signingInfo.signerType
log field value is equal to
3
, then the
target.user.attribute.labels.value
UDM field is set to
3 - Ad Hoc
.
Else, if the
input.related.process.signingInfo.signerType
log field value is equal to
4
, then the
target.user.attribute.labels.value
UDM field is set to
4 - Unsigned
.
input.match.event.process.signingInfo.status
target.user.attribute.labels [input_match_event_process_sign_status]
input.match.event.process.signingInfo.statusMessage
target.labels[input_match_event_process_sign_status_message]
(deprecated)
input.match.event.process.signingInfo.statusMessage
additional.fields[input_match_event_process_sign_status_message]
input.match.event.process.signingInfo.teamid
target.user.group_identifiers
input.match.event.process.startTimestamp
target.labels[input_match_event_process_start_time_stamp]
(deprecated)
input.match.event.process.startTimestamp
additional.fields[input_match_event_process_start_time_stamp]
input.match.event.process.uid
target.labels[input_match_event_process_uid]
(deprecated)
input.match.event.process.uid
additional.fields[input_match_event_process_uid]
input.match.event.process.uuid
target.process.product_specific_process_id
The
Process Uuid: input.match.event.process.uuid
log field is mapped to the
target.process.product_specific_process_id
UDM field.
input.match.event.processIdentifier
target.process.pid
input.match.event.processImagePath
target.process.file.full_path
input.match.event.rateLimitingSecs
principal.labels[input_match_event_rate_limiting_secs]
(deprecated)
input.match.event.rateLimitingSecs
additional.fields[input_match_event_rate_limiting_secs]
input.match.event.scriptPath
principal.labels[input_match_event_script_path]
(deprecated)
input.match.event.scriptPath
additional.fields[input_match_event_script_path]
input.match.event.sender
principal.labels[input_match_event_sender]
(deprecated)
input.match.event.sender
additional.fields[input_match_event_sender]
input.match.event.senderImagePath
principal.labels[input_match_event_sender_image_path]
(deprecated)
input.match.event.senderImagePath
additional.fields[input_match_event_sender_image_path]
input.match.event.subsystem
principal.labels[input_match_event_subsystem]
(deprecated)
input.match.event.subsystem
additional.fields[input_match_event_subsystem]
input.match.event.subType
principal.labels[input_match_event_sub_type]
(deprecated)
If the
input.match.event.subType
log field value is equal to
7
, then the
principal.labels.value
UDM field is set to
7 - Exec
.
Else, if the
input.match.event.subType
log field value is equal to
2
, then the
principal.labels.value
UDM field is set to
2 - Fork
.
Else, if the
input.match.event.subType
log field value is equal to
1
, then the
principal.labels.value
UDM field is set to
1 - Exit
.
Else, if the
input.match.event.subType
log field value is equal to
23
, then the
principal.labels.value
UDM field is set to
23 - Execve
.
Else, if the
input.match.event.subType
log field value is equal to
43190
, then the
principal.labels.value
UDM field is set to
43190 - Posix Spawn
.
input.match.event.subType
additional.fields[input_match_event_sub_type]
If the
input.match.event.subType
log field value is equal to
7
, then the
additional.fields.value.string_value
UDM field is set to
7 - Exec
.
Else, if the
input.match.event.subType
log field value is equal to
2
, then the
additional.fields.value.string_value
UDM field is set to
2 - Fork
.
Else, if the
input.match.event.subType
log field value is equal to
1
, then the
additional.fields.value.string_value
UDM field is set to
1 - Exit
.
Else, if the
input.match.event.subType
log field value is equal to
23
, then the
additional.fields.value.string_value
UDM field is set to
23 - Execve
.
Else, if the
input.match.event.subType
log field value is equal to
43190
, then the
additional.fields.value.string_value
UDM field is set to
43190 - Posix Spawn
.
input.match.event.tags
security_result.rule_labels [input_match_event_tags]
input.match.event.targetpid
target.process.pid
input.match.event.timestamp
metadata.event_timestamp
input.match.event.type
target.labels[input_match_event_type]
(deprecated)
If the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
0
, then the
target.labels.value
UDM field is set to
0 - Created
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
1
, then the
target.labels.value
UDM field is set to
1 - Deleted
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
3
, then the
target.labels.value
UDM field is set to
3 - Renamed
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
4
, then the
target.labels.value
UDM field is set to
4 - Modified
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
7
, then the
target.labels.value
UDM field is set to
7 - Created Dir
.
Else, if the
input.eventType
log field value is equal to
GPProcessEvent
and the
input.match.event.type
log field value is equal to
0
, then the
target.labels.value
UDM field is set to
0 - None
.
Else, if the
input.eventType
log field value is equal to
GPProcessEvent
and the
input.match.event.type
log field value is equal to
1
, then the
target.labels.value
UDM field is set to
1 - Create
.
Else, if the
input.eventType
log field value is equal to
GPProcessEvent
and the
input.match.event.type
log field value is equal to
2
, then the
target.labels.value
UDM field is set to
0 - Exit
.
input.match.event.type
additional.fields[input_match_event_type]
If the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
0
, then the
additional.fields.value.string_value
UDM field is set to
0 - Created
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
1
, then the
additional.fields.value.string_value
UDM field is set to
1 - Deleted
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
3
, then the
additional.fields.value.string_value
UDM field is set to
3 - Renamed
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
4
, then the
additional.fields.value.string_value
UDM field is set to
4 - Modified
.
Else, if the
input.eventType
log field value is equal to
GPFSEvent
and the
input.match.event.type
log field value is equal to
7
, then the
additional.fields.value.string_value
UDM field is set to
7 - Created Dir
.
Else, if the
input.eventType
log field value is equal to
GPProcessEvent
and the
input.match.event.type
log field value is equal to
0
, then the
additional.fields.value.string_value
UDM field is set to
0 - None
.
Else, if the
input.eventType
log field value is equal to
GPProcessEvent
and the
input.match.event.type
log field value is equal to
1
, then the
additional.fields.value.string_value
UDM field is set to
1 - Create
.
Else, if the
input.eventType
log field value is equal to
GPProcessEvent
and the
input.match.event.type
log field value is equal to
2
, then the
additional.fields.value.string_value
UDM field is set to
0 - Exit
.
input.match.event.uid
principal.user.userid
input.match.event.uuid
about.labels[input_match_event_uuid]
(deprecated)
input.match.event.uuid
additional.fields[input_match_event_uuid]
input.match.facts.actions.name
security_result.action_details
If the
index
value is equal to
0
, then the
input.match.facts.actions.name
log field is mapped to the
security_result.action_details
UDM field.
Else, the
input.match.facts.actions.name
log field is mapped to the
security_result.about.labels.value
UDM field.
input.match.facts.actions.parameters.id
security_result.detection_fields [input_match_facts_actions_parameters_id]
input.match.facts.actions.parameters.message
security_result.detection_fields [input_match_facts_actions_parameters_message]
input.match.facts.actions.parameters.title
security_result.detection_fields [input_match_facts_actions_parameters_title]
input.match.facts.context.name
security_result.detection_fields.key
input.match.facts.context.value
security_result.detection_fields.value [Name]
input.match.facts.context.valueType
input.match.facts.human
security_result.action
If the
input.match.facts.human
log field value is matched with regex
(?i)blocked
, then the
security_result.action
UDM field is set to
BLOCK
.
input.match.facts.human
security_result.description
If the
index
value is equal to
0
, then the
input.match.facts.human
log field is mapped to the
security_result.description
UDM field.
Else, the
input.match.facts.human
log field is mapped to the
security_result.detection_fields.value
UDM field.
input.match.facts.name
security_result.summary
If the
index
value is equal to
0
, then the
input.match.facts.name
log field is mapped to the
security_result.summary
UDM field.
Else, the
input.match.facts.name
log field is mapped to the
security_result.detection_fields.value
UDM field.
input.match.facts.severity
security_result.detection_fields [input_match_facts_severity]
input.match.facts.tags
security_result.rule_labels [input_match_facts_tags]
input.match.facts.uuid
about.labels [input_match_facts_uuid]
input.match.facts.version
about.labels [input_match_facts_version]
input.match.severity
security_result.severity
If the
severity
log field value is equal to
0
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
severity
log field value is equal to
1
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
severity
log field value is equal to
2
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value is equal to
3
, then the
security_result.severity
UDM field is set to
HIGH
.
input.match.tags
security_result.rule_labels [input_match_tags]
input.match.uuid
metadata.product_log_id
input.related.binaries.accessed
security_result.about.labels [input_related_binaries_accessed]
input.related.binaries.changed
security_result.about.labels [input_related_binaries_changed]
input.related.binaries.created
security_result.about.file.first_seen_time
If the
index
value is equal to
0
, then the
input.related.binaries.created
log field is mapped to the
security_result.about.file.first_seen_time
UDM field.
Else, the
input.related.binaries.created
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.fsid
security_result.about.labels [input_related_binaries_fsid]
input.related.binaries.gid
security_result.about.labels [input_related_binaries_gid]
input.related.binaries.inode
security_result.about.file.stat_inode
If the
index
value is equal to
0
, then the
input.related.binaries.inode
log field is mapped to the
security_result.about.file.stat_inode
UDM field.
Else, the
input.related.binaries.inode
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.isAppBundle
security_result.about.labels [isAppBundle]
input.related.binaries.isDirectory
security_result.about.labels [isDirectory]
input.related.binaries.isDownload
security_result.about.labels [isDownload]
input.related.binaries.isScreenShot
security_result.about.labels [isScreenShot]
input.related.binaries.mode
security_result.about.file.stat_mode
If the
index
value is equal to
0
, then the
input.related.binaries.mode
log field is mapped to the
security_result.about.file.stat_mode
UDM field.
Else, the
input.related.binaries.mode
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.modified
security_result.about.file.last_modification_time
If the
index
value is equal to
0
, then the
input.related.binaries.modified
log field is mapped to the
security_result.about.file.last_modification_time
UDM field.
Else, the
input.related.binaries.modified
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.path
security_result.about.file.full_path
If the
index
value is equal to
0
, then the
input.related.binaries.path
log field is mapped to the
security_result.about.file.full_path
UDM field.
Else, the
input.related.binaries.path
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.sha1hex
security_result.about.file.sha1
If the
index
value is equal to
0
, then the
input.related.binaries.sha1hex
log field is mapped to the
security_result.about.file.sha1
UDM field.
Else, the
input.related.binaries.sha1hex
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.sha256hex
security_result.about.file.sha256
If the
index
value is equal to
0
, then the
input.related.binaries.sha256hex
log field is mapped to the
security_result.about.file.sha256
UDM field.
Else, the
input.related.binaries.sha256hex
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.signingInfo.appid
security_result.about.application
If the
index
value is equal to
0
, then the
input.related.binaries.signingInfo.appid
log field is mapped to the
security_result.about.application
UDM field.
Else, the
input.related.binaries.signingInfo.appid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.signingInfo.authorities
security_result.about.user.attribute.permissions
input.related.binaries.signingInfo.cdhash
security_result.about.labels [input_related_binaries_sign_cdhash]
input.related.binaries.signingInfo.entitlements
security_result.about.user.attribute.permisisons
input.related.binaries.signingInfo.signerType
security_result.about.user.attribute.labels [input_related_binaries_sign_signer_type]
If the
input.related.binaries.signingInfo.signerType
log field value is equal to
0
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
0 - Apple
.
Else, if the
input.related.binaries.signingInfo.signerType
log field value is equal to
1
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
1 - App Store
.
Else, if the
input.related.binaries.signingInfo.signerType
log field value is equal to
2
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
2 - Developer
.
Else, if the
input.related.binaries.signingInfo.signerType
log field value is equal to
3
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
3 - Ad Hoc
.
Else, if the
input.related.binaries.signingInfo.signerType
log field value is equal to
4
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
4 - Unsigned
.
input.related.binaries.signingInfo.status
security_result.about.user.attribute.labels [input_related_binaries_sign_status]
input.related.binaries.signingInfo.statusMessage
security_result.about.user.attribute.labels [input_related_processes_sign_status_message]
input.related.binaries.signingInfo.teamid
security_result.about.user.group_identifiers
If the
index
value is equal to
0
, then the
input.related.binaries.signingInfo.teamid
log field is mapped to the
security_result.about.user.group_identifiers
UDM field.
Else, the
input.related.binaries.signingInfo.teamid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.binaries.size
security_result.about.file.size
If the
index
value is equal to
0
, then the
input.related.binaries.size
log field is mapped to the
security_result.about.file.size
UDM field.
Else, the
input.related.binaries.size
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.binaries.uid
security_result.about.user.userid
If the
index
value is equal to
0
, then the
input.related.binaries.uid
log field is mapped to the
security_result.about.user.userid
UDM field.
Else, the
input.related.binaries.uid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.binaries.xattrs
security_result.about.user.attribute.labels [input_related_binaries_xattrs]
input.related.files.accessed
security_result.about.labels [input_related_files_accessed]
input.related.files.changed
security_result.about.labels [input_related_files_changed]
input.related.files.created
security_result.about.labels [input_related_files_created]
input.related.files.downloadedFrom
security_result.about.labels [input_related_files_downloaded_from]
input.related.files.fsid
security_result.about.labels [input_related_files_downloaded_fsid]
input.related.files.gid
security_result.about.group.product_object_id
If the
index
value is equal to
0
, then the
input.related.files.gid
log field is mapped to the
security_result.about.group.product_object_id
UDM field.
Else, the
input.related.files.gid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.inode
security_result.about.file.stat_inode
If the
index
value is equal to
0
, then the
input.related.files.inode
log field is mapped to the
security_result.about.file.stat_inode
UDM field.
Else, the
input.related.files.inode
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.isAppBundle
security_result.about.labels [input_related_files_downloaded_is_app_bundle]
input.related.files.isDirectory
security_result.about.labels [input_related_files_is_directory]
input.related.files.isDownload
security_result.about.labels [input_related_files_is_download]
input.related.files.isScreenShot
security_result.about.labels [input_related_files_is_screenshot]
input.related.files.mode
security_result.about.file.stat_mode
If the
index
value is equal to
0
, then the
input.related.files.mode
log field is mapped to the
security_result.about.file.stat_mode
UDM field.
Else, the
input.related.files.mode
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.modified
security_result.about.file.last_modification_time
If the
index
value is equal to
0
, then the
input.related.files.modified
log field is mapped to the
security_result.about.file.last_modification_time
UDM field.
Else, the
input.related.files.modified
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.path
security_result.about.file.full_path
If the
index
value is equal to
0
, then the
input.related.files.path
log field is mapped to the
security_result.about.file.full_path
UDM field.
Else, the
input.related.files.path
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.sha1hex
security_result.about.file.sha1
If the
index
value is equal to
0
, then the
input.related.files.sha1hex
log field is mapped to the
security_result.about.file.sha1
UDM field.
Else, the
input.related.files.sha1hex
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.sha256hex
security_result.about.file.sha256
If the
index
value is equal to
0
, then the
input.related.files.sha256hex
log field is mapped to the
security_result.about.file.sha256
UDM field.
Else, the
input.related.files.sha256hex
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.signingInfo.appid
security_result.about.application
If the
index
value is equal to
0
, then the
input.related.files.signingInfo.appid
log field is mapped to the
security_result.about.application
UDM field.
Else, the
input.related.files.signingInfo.appid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.signingInfo.authorities
security_result.about.user.attribute.permissions
input.related.files.signingInfo.cdhash
security_result.about.labels [[input_related_files_sign_cdhash]
input.related.files.signingInfo.entitlements
security_result.about.user.attribute.permissions
input.related.files.signingInfo.signerType
security_result.about.user.attribute.labels [input_related_files_signing_info_signer_type]
If the
input.related.files.signingInfo.signerType
log field value is equal to
0
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
0 - Apple
.
Else, if the
input.related.files.signingInfo.signerType
log field value is equal to
1
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
1 - App Store
.
Else, if the
input.related.files.signingInfo.signerType
log field value is equal to
2
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
2 - Developer
.
Else, if the
input.related.files.signingInfo.signerType
log field value is equal to
3
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
3 - Ad Hoc
.
Else, if the
input.related.files.signingInfo.signerType
log field value is equal to
4
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
4 - Unsigned
.
input.related.files.signingInfo.status
security_result.about.user.attribute.labels [input_related_files_signing_info_status]
input.related.files.signingInfo.statusMessage
security_result.about.user.attribute.labels [input_related_files_signing_info_status_message]
input.related.files.signingInfo.teamid
security_result.about.user.group_identifiers
If the
index
value is equal to
0
, then the
input.related.files.signingInfo.teamid
log field is mapped to the
security_result.about.user.group_identifiers
UDM field.
Else, the
input.related.files.signingInfo.teamid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.files.size
security_result.about.file.size
If the
index
value is equal to
0
, then if the
input.related.files.size
log field value is
not
equal to
0
, then the
input.related.files.size
log field is mapped to the
security_result.about.file.size
UDM field.
Else, the
input.related.files.size
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.files.uid
security_result.about.user.userid
If the
index
value is equal to
0
, then the
input.related.files.uid
log field is mapped to the
security_result.about.user.userid
UDM field.
Else, the
input.related.files.uid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.files.xattrs
security_result.about.labels [input_related_files_xattrs]
input.related.groups.gid
security_result.about.group.attribute.labels [input_related_groups_gid]
input.related.groups.name
security_result.about.group.group_display_name
If the
index
value is equal to
0
, then the
input.related.groups.name
log field is mapped to the
security_result.about.group.group_display_name
UDM field.
Else, the
input.related.groups.name
log field is mapped to the
security_result.about.group.attribute.labels.value
UDM field.
input.related.groups.uuid
security_result.about.group.product_object_id
If the
index
value is equal to
0
, then the
input.related.groups.uuid
log field is mapped to the
security_result.about.group.product_object_id
UDM field.
Else, the
input.related.groups.uuid
log field is mapped to the
security_result.about.group.attribute.labels.value
UDM field.
input.related.processes.appPath
security_result.about.labels [input_related_processes_app_path]
input.related.processes.args
security_result.about.process.command_line_history
input.related.processes.exitCode
security_result.about.labels [input_related_processes_exit_code]
input.related.processes.gid
security_result.about.group.product_object_id
If the
index
value is equal to
0
, then the
input.related.processes.gid
log field is mapped to the
security_result.about.group.product_object_id
UDM field.
Else, the
input.related.processes.gid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.processes.name
security_result.about.process.file.names
input.related.processes.originalParentPID
security_result.about.process.parent_process.pid
If the
index
value is equal to
0
, then the
input.related.processes.originalParentPID
log field is mapped to the
security_result.about.process.parent_process.pid
UDM field.
Else, the
input.related.processes.originalParentPID
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.processes.path
security_result.about.process.file.full_path
If the
index
value is equal to
0
, then the
input.related.processes.path
log field is mapped to the
security_result.about.process.file.full_path
UDM field.
Else, the
input.related.processes.path
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.processes.pgid
security_result.about.labels [input_related_process_pgid]
input.related.processes.pid
security_result.about.process.pid
If the
index
value is equal to
0
, then the
input.related.processes.pid
log field is mapped to the
security_result.about.process.pid
UDM field.
Else, the
input.related.processes.pid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.processes.ppid
security_result.about.labels [input_related_processes_ppid]
input.related.processes.responsiblePID
security_result.about.labels [input_related_processes_responsible_pid]
input.related.processes.rgid
security_result.about.labels [input_related_processes_rgid]
input.related.processes.ruid
security_result.about.labels [input_related_processes_ruid]
input.related.processes.signingInfo.appid
security_result.about.application
If the
index
value is equal to
0
, then the
input.related.processes.signingInfo.appid
log field is mapped to the
security_result.about.application
UDM field.
Else, the
input.related.processes.signingInfo.appid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.processes.signingInfo.authorities
security_result.about.user.attributes.permission
input.related.processes.signingInfo.cdhash
security_result.about.user.attribute.labels [input_related_processes_sign_cdhash]
input.related.processes.signingInfo.entitlements
security_result.about.user.attributes.permission
input.related.processes.signingInfo.signerType
security_result.about.user.attribute.labels [input_related_processes_sign_signer_type]
If the
input.related.processes.signingInfo.signerType
log field value is equal to
0
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
0 - Apple
.
Else, if the
input.related.processes.signingInfo.signerType
log field value is equal to
1
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
1 - App Store
.
Else, if the
input.related.processes.signingInfo.signerType
log field value is equal to
2
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
2 - Developer
.
Else, if the
input.related.processes.signingInfo.signerType
log field value is equal to
3
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
3 - Ad Hoc
.
Else, if the
input.related.processes .signingInfo.signerType
log field value is equal to
4
, then the
security_result.about.user.attribute.labels.value
UDM field is set to
4 - Unsigned
.
input.related.processes.signingInfo.status
security_result.about.user.attribute.labels [input_related_processes_sign_status]
input.related.processes.signingInfo.statusMessage
security_result.about.user.attribute.labels [input_related_processes_sign_status_message]
input.related.processes.signingInfo.teamid
security_result.about.user.group_identifiers
If the
index
value is equal to
0
, then the
input.related.processes.signingInfo.teamid
log field is mapped to the
security_result.about.user.group_identifiers
UDM field.
Else, the
input.related.processes.signingInfo.teamid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.processes.startTimestamp
security_result.about.labels [input_related_processes_start_time_stamp]
input.related.processes.tty
security_result.about.labels [input_related_processes_tty]
input.related.processes.uid
security_result.about.user.userid
If the
index
value is equal to
0
, then the
input.related.processes.uid
log field is mapped to the
security_result.about.user.userid
UDM field.
Else, the
input.related.processes.uid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.processes.uuid
security_result.about.process.product_specific_process_id
If the
index
value is equal to
0
, then the
Process Uuid: input.related.processes.uuid
log field is mapped to the
security_result.about.process.product_specific_process_id
UDM field.
Else, the
input.related.processes.uuid
log field is mapped to the
security_result.about.labels.value
UDM field.
input.related.users.name
security_result.about.user.user_display_name
If the
index
value is equal to
0
, then the
input.related.users.name
log field is mapped to the
security_result.about.user.user_display_name
UDM field.
Else, the
input.related.users.name
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.users.uid
security_result.about.user.userid
If the
index
value is equal to
0
, then the
input.related.users.uid
log field is mapped to the
security_result.about.user.userid
UDM field.
Else, the
input.related.users.uid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
input.related.users.uuid
security_result.about.user.product_object_id
If the
index
value is equal to
0
, then the
input.related.users.uuid
log field is mapped to the
security_result.about.user.product_object_id
UDM field.
Else, the
input.related.users.uuid
log field is mapped to the
security_result.about.user.attribute.labels.value
UDM field.
key
about.labels[key]
(deprecated)
key
additional.fields[key]
path
target.file.full_path
If the
index
value is equal to
0
, then the
path
log field is mapped to the
target.file.full_path
UDM field.
Else, the
path
log field is mapped to the
target.labels.value
UDM field.
queue
principal.labels[queue]
(deprecated)
queue
additional.fields[queue]
region
principal.location.name
timestamp
metadata.creation_timestamp
topic
about.labels[topic]
(deprecated)
topic
additional.fields[topic]
topicType
about.labels[topicType]
(deprecated)
topicType
additional.fields[topicType]
version
metadata.product_version
input.eventType
metadata.event_type
metadata.product_name
The
metadata.product_name
UDM field is set to
JAMF_PROTECT
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
JAMF
.
principal.resource.resource_type
The
principal.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
input.match.event.options
about.labels[input_match_event_options]
(deprecated)
input.match.event.options
additional.fields[input_match_event_options]
input.match.event.sourcePID
principal.process.pid
input.match.event.destinationPID
target.process.pid
image.match.event.detection
security_result.detection_fields [image_match_event_detection]
input.match.type
target.asset.attribute.labels [input_match_type]
If the
input.match.type
log field value is equal to
0
, then the
target.asset.attribute.labels.value
UDM field is set to
0 - Device Inserted
.
Else, if the
input.match.type
log field value is equal to
1
, then the
target.asset.attribute.labels.value
UDM field is set to
1 - Device Removed
.
input.match.usbAddress
target.asset.attribute.labels [input_match_usb_address]
input.match.event.device.mediaPath
target.asset.attribute.labels [input_match_device_media_path]
input.match.event.device.protocol
target.asset.attribute.labels [input_match_device_protocol]
input.match.event.device.deviceModel
target.asset.hardware.model
input.match.event.device.isRemovable
target.asset.attribute.labels [input_match_device_is_removable]
input.match.event.device.mediaName
target.asset.attribute.labels [input_match_device_media_name]
input.match.event.device.bsdMinor
target.asset.attribute.labels [input_match_device_bsd_minor]
input.match.event.device.vendorName
target.asset.software.vendor_name
input.match.event.device.isWhole
target.asset.attribute.labels [input_match_device_is_whole]
input.match.event.device.unit
target.asset.attribute.labels [input_match_device_unit]
input.match.event.device.deviceSubclass
target.asset.attribute.labels [input_match_device_subclass]
input.match.event.device.serialNumber
target.asset.hardware.serial
input.match.event.device.bsdUnit
target.asset.attribute.labels [input_match_device_bsd_unit]
input.match.event.device.busPath
target.asset.attribute.labels [input_match_device_bus_path]
input.match.event.device.isLeaf
target.asset.attribute.labels [input_match_device_is_leaf]
input.match.event.device.isInternal
target.asset.attribute.labels [input_match_device_is_internal]
input.match.event.device.busName
target.asset.attribute.labels [input_match_device_bus_name]
input.match.event.device.bsdMajor
target.asset.attribute.labels [input_match_device_bsd_major]
input.match.event.device.isEjectable
target.asset.attribute.labels [input_match_device_is_ejectable]
input.match.event.device.isEncrypted
target.asset.attribute.labels [input_match_device_is_encrypted]
input.match.event.device.isEncryptable
target.asset.attribute.labels [input_match_device_is_encryptable]
input.match.event.device.devicePath
target.asset.attribute.labels [input_match_device_path]
input.match.event.device.bsdName
target.asset.attribute.labels [input_match_device_bsd_name]
input.match.event.device.vendorId
target.asset.attribute.labels [input_match_device_vendor_id]
input.match.event.device.content
target.asset.attribute.labels [input_match_device_content]
input.match.event.device.revision
target.asset.attribute.labels [input_match_device_revision]
input.match.event.device.size
target.asset.attribute.labels [input_match_device_size]
input.match.event.device.isNetworkVolume
target.asset.attribute.labels [input_match_device_is_network_volume]
input.match.event.device.blocksize
target.asset.attribute.labels [input_match_device_block_size]
input.match.event.device.productName
target.asset.attribute.labels [input_match_device_product_name]
input.match.event.device.mediaKind
target.asset.attribute.labels [input_match_device_media_kind]
input.match.event.device.isWritable
target.asset.attribute.labels [input_match_device_is_writable]
input.match.event.device.productId
target.asset.product_object_id
input.match.event.device.productId
target.asset.asset_id
The
Asset Id: input.match.event.device.productId
log field is mapped to the
target.asset.asset_id
UDM field.
input.match.event.device.deviceClass
target.asset.category
input.match.event.device.encryptionDetail
target.asset.attribute.labels [input_match_device_encryption_detail]
input.match.event.device.volumeKind
target.asset.attribute.labels [input_match_event_device_volume_kind]
input.match.event.device.volumeName
target.asset.attribute.labels [input_match_event_device_volume_name]
input.match.event.device.volumeType
target.asset.attribute.labels [input_match_event_device_volume_type]
input.match.event.device.isMountable
target.asset.attribute.labels [input_match_event_device_is_mountable]
input.match.event.device.encryptionDetail
target.asset.attribute.labels [input_match_event_device_encryption_detail]
input.match.event.fsid
principal.labels [input_match_event_fsid]
input.match.event.bfree
principal.labels[input_match_event_bfree]
(deprecated)
input.match.event.bfree
additional.fields[input_match_event_bfree]
input.match.event.bsize
principal.labels[input_match_event_bsize]
(deprecated)
input.match.event.bsize
additional.fields[input_match_event_bsize]
input.match.event.ffree
principal.labels[input_match_event_ffree]
(deprecated)
input.match.event.ffree
additional.fields[input_match_event_ffree]
input.match.event.files
principal.labels[input_match_event_files]
(deprecated)
input.match.event.files
additional.fields[input_match_event_files]
input.match.event.flags
principal.labels[input_match_event_flags]
(deprecated)
input.match.event.flags
additional.fields[input_match_event_flags]
input.match.event.owner
principal.user.user_display_name
input.match.event.bavail
principal.labels[input_match_event_bvail]
(deprecated)
input.match.event.bavail
additional.fields[input_match_event_bvail]
input.match.event.blocks
principal.labels[input_match_event_blocks]
(deprecated)
input.match.event.blocks
additional.fields[input_match_event_blocks]
input.match.event.iosize
principal.labels[input_match_event_iosize]
(deprecated)
input.match.event.iosize
additional.fields[input_match_event_iosize]
input.match.event.version
principal.labels[input_match_event_version]
(deprecated)
input.match.event.version
additional.fields[input_match_event_version]
input.match.event.deadline
principal.labels[input_match_event_deadline]
(deprecated)
input.match.event.deadline
additional.fields[input_match_event_deadline]
input.match.event.flagsExt
principal.labels[input_match_event_flags_ext]
(deprecated)
input.match.event.flagsExt
additional.fields[input_match_event_flags_ext]
input.match.event.fsSubType
principal.labels[input_match_event_fs_subtype]
(deprecated)
input.match.event.fsSubType
additional.fields[input_match_event_fs_subtype]
input.match.event.mntOnName
principal.labels[input_match_event_mnt_on_name]
(deprecated)
input.match.event.mntOnName
additional.fields[input_match_event_mnt_on_name]
input.match.event.fsTypeName
principal.labels[input_match_event_fs_type_name]
(deprecated)
input.match.event.fsTypeName
additional.fields[input_match_event_fs_type_name]
input.match.event.isReadOnly
principal.labels[input_match_event_is_read_only]
(deprecated)
input.match.event.isReadOnly
additional.fields[input_match_event_is_read_only]
input.match.event.mntFromName
principal.labels[input_match_event_mnt_from_name]
(deprecated)
input.match.event.mntFromName
additional.fields[input_match_event_mnt_from_name]
input.match.event.machTimestamp
principal.labels[input_match_event_mach_timestamp]
(deprecated)
input.match.event.machTimestamp
additional.fields[input_match_event_mach_timestamp]
input.match.event.sequenceNumber
principal.labels[input_match_event_seq_number]
(deprecated)
input.match.event.sequenceNumber
additional.fields[input_match_event_seq_number]
input.match.event.globalSequenceNumber
principal.labels[input_match_event_global_seq_number]
(deprecated)
input.match.event.globalSequenceNumber
additional.fields[input_match_event_global_seq_number]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
