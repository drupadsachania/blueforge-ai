# Collect SentinelOne Alert logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-alert/  
**Scraped:** 2026-03-05T09:18:03.274458Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect SentinelOne Alert logs
Supported in:
Google secops
SIEM
This document describes how you can collect SentinelOne Alert logs by
setting up a Google Security Operations feed and how log fields map to
Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations overview
.
A typical deployment consists of SentinelOne Alert and the
Google SecOps feed configured to send logs to Google SecOps. Each
customer deployment can differ and might be more complex.
The deployment contains the following components:
SentinelOne
: The product from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches
logs from SentinelOne and writes logs to Google SecOps.
Google SecOps
: Google SecOps retains and analyzes the logs from
SentinelOne.
An ingestion label identifies the parser which normalizes raw log data to
structured UDM format. The information in this document applies to the parser
with the
SENTINELONE_ALERT
ingestion label.
Before you begin
Make sure you have the following prerequisites:
An active
Singularity Complete
subscription for
SentinelOne. Refer to
Platform Packages
for additional details.
GET Alerts and GET Threats API v2.1
An Admin role for the Global or Account level. To get an Admin role, contact your administrator user.
Administrator rights to install the SentinelOne agent. To get administrator rights, contact your administrator user.
How to set up SentinelOne:
To generate an API token, follow these steps:
    1. In the SentinelOne management console, go to
Settings
, and then click
Users
.
    1. Click the
Admin user
for which you want to generate the API token.
    1. Click
Actions
>
API token operations
>
Generate API token
. 
    You need this API token to populate
Authentication HTTP headers
in the Google SecOps platform.
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
How to set up the SentinelOne Alerts feed
Click the
SentinelOne
pack.
Locate the
SentinelOne Alerts
log type.
Specify the values for the following fields:
Source Type
: Third Party API (recommended)
Authentication HTTP headers
: Enter the API token you generated in the SentinelOne platform.
API hostname
: SentinelOne platform hostname
Initial start time
: Time to start fetching the alerts from
Is alert API subscribed
: Whether the alert AOI is subscribed to by the customer
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
Supported SentinelOne Alert log types
The SentinelOne Alert parser supports alert and threat log types.
Supported SentinelOne Alert log formats
The SentinelOne Alert parser supports logs in both JSON and CEF formats.
Supported SentinelOne Alert Sample Logs
JSON
{
    "accountId": "1235512064263015539",
    "accountName": "dummy",
    "agentComputerName": "dummy",
    "agentDomain": "WORKGROUP",
    "agentId": "1245680559492378683",
    "agentInfected": false,
    "agentIp": "198.51.100.0",
    "agentIsActive": false,
    "agentIsDecommissioned": true,
    "agentMachineType": "server",
    "agentNetworkStatus": "disconnecting",
    "agentOsType": "windows",
    "agentVersion": "21.6.2.272",
    "annotation": "Automatically resolved by SentinelOne Console",
    "automaticallyResolved": true,
    "browserType": null,
    "certId": "",
    "classification": "Malware",
    "classificationSource": "Static",
    "classifierName": "MANUAL",
    "cloudVerdict": null,
    "collectionId": "1251555311751427932",
    "commandId": "1251555264615838432",
    "createdAt": "2022-09-03T19:36:59.540349Z",
    "createdDate": "2021-09-23T19:36:57.867000Z",
    "description": "malware detected - not mitigated yet (cmd.exe (interactive session))",
    "engines": [
      "manual"
    ],
    "external_ticket_id": null,
    "fileContentHash": "c3d10d8d9fce936e5ca32f930f20c8e703619f71",
    "fileCreatedDate": null,
    "fileDisplayName": "Unknown file",
    "fileExtensionType": "None",
    "fileIsDotNet": null,
    "fileIsExecutable": false,
    "fileIsSystem": false,
    "fileMaliciousContent": null,
    "fileObjectId": "3EFA3EFA3EFA3EFA",
    "filePath": "/home/gitlab-runner/webshell_hits/old.hits-go-here/fedcd896ef45bf145d7e880edd4e5390.dll",
    "fileSha256": null,
    "fileVerificationType": "NotSigned",
    "fromCloud": false,
    "fromScan": false,
    "id": "1251555311717873499",
    "indicators": [
      {
        "categoryName": "test Hiding/Stealthiness",
        "description": "This binary may have Anti-sandboxing capabilities to evade detection in sandbox tools",
        "id": 126
      },
      {
        "categoryName": "Hiding/Stealthiness",
        "description": "sample desc There are signs of a backdoor in the PE header",
        "id": 127
      },
      {
        "categoryName": "Test category name Hiding/Stealthiness",
        "description": "This binary might try to schedule a task or modify a scheduled task",
        "id": 129
      }
    ],
    "initiatedBy": "dvCommand",
    "initiatedByDescription": "Deep Visibility Command",
    "initiatingUserId": "1245152494739966182",
    "isCertValid": false,
    "isInteractiveSession": true,
    "isPartialStory": false,
    "maliciousGroupId": "DEA2CA314B3AB7E4",
    "maliciousProcessArguments": "",
    "markedAsBenign": true,
    "mitigationMode": "protect",
    "mitigationReport": {
      "kill": {
        "status": "success"
      },
      "network_quarantine": {
        "status": null
      },
      "quarantine": {
        "status": "success"
      },
      "remediate": {
        "status": null
      },
      "rollback": {
        "status": null
      },
      "unquarantine": {
        "status": null
      }
    },
    "mitigationStatus": "mitigated",
    "publisher": "",
    "rank": null,
    "resolved": true,
    "siteId": "1235512064330124404",
    "siteName": "Default site",
    "threatAgentVersion": "21.6.2.272",
    "threatName": "cmd.exe (interactive session)",
    "updatedAt": "2021-10-23T20:34:15.668440Z",
    "username": "dummy\\\\Administrator",
    "whiteningOptions": []
  }
CEF
<86>Nov  5 11:53:06 abcdefg sshd[1475549]: reprocess config line 158: Deprecated option RhostsRSAAuthentication
Field mapping reference
This section explains how the Google SecOps parser maps
SentinelOne Alert fields to Google SecOps Unified Data Model
(UDM) fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
SENTINELONE_ALERT
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
BEHAVIORALINDICATORS
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
DNS
NETWORK_DNS
DUPLICATEPROCESS
PROCESS_UNCATEGORIZED
FILECREATION
FILE_CREATION
FILEDELETION
FILE_DELETION
FILEMODIFICATION
FILE_MODIFICATION
FILERENAME
FILE_MODIFICATION
FILESCAN
SCAN_FILE
HTTP
NETWORK_HTTP
MALICIOUSFILE
SCAN_FILE
SOFTWARE_MALICIOUS
OPENPROCESS
PROCESS_OPEN
PROCESSCREATION
PROCESS_LAUNCH
REGKEYCREATE
REGISTRY_CREATION
REGKEYDELETE
REGISTRY_DELETION
REGVALUECREATE
REGISTRY_CREATION
REGVALUEDELETE
REGISTRY_DELETION
REGVALUEMODIFIED
REGISTRY_MODIFICATION
SCHEDTASKSTART
SERVICE_START
SCHEDTASKTRIGGER
SERVICE_START
SCHEDTASKUPDATE
SERVICE_MODIFICATION
SCRIPTS
FILE_UNCATEGORIZED
TCPV4
NETWORK_UNCATEGORIZED
TCPV4LISTEN
NETWORK_UNCATEGORIZED
WINLOGONATTEMPT
USER_LOGIN
If the
threatInfo.filePath
log field is
not
empty or the
threatInfo.fileSize
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
FILE_UNCATEGORIZED
.
FILE_UNCATEGORIZED
Field mapping reference: SENTINELONE_ALERT
The following table lists the log fields of the
SENTINELONE_ALERT
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.vendor_name
metadata.product_name
metadata.url_back_to_product
If the
threatInfo.threatId
log field value is
not
empty and the
source_hostname
log field value is
not
empty, then the
https://source_hostname/incidents/threats/threatInfo.threatId/overview
log field is mapped to the
metadata.url_back_to_product
UDM field.
Else, if the
source_hostname
log field value is
not
empty, then the
https://source_hostname
log field is mapped to the
metadata.url_back_to_product
UDM field.
agentDetectionInfo.machineType
principal.asset.type
If the
agentDetectionInfo.machineType
log field value matches the regular expression pattern
laptop
, then the
principal.asset.type
UDM field is set to
LAPTOP
.
Else, if the
agentDetectionInfo.machineType
log field value matches the regular expression pattern
desktop
, then the
principal.asset.type
UDM field is set to
WORKSTATION
.
Else, if the
agentDetectionInfo.machineType
log field value matches the regular expression pattern
server
, then the
principal.asset.type
UDM field is set to
SERVER
.
Else, the
agentDetectionInfo.machineType
log field is mapped to the
principal.asset.attribute.labels.agent_detection_info_machine_type
UDM field.
agentRealtimeInfo.agentMachineType
principal.asset.type
If the
agentDetectionInfo.machineType
log field value is empty and the
agentRealtimeInfo.agentMachineType
log field value is
not
empty , then:
If the
agentRealtimeInfo.agentMachineType
log field value matches the regular expression pattern
laptop
, then the
principal.asset.type
UDM field is set to
LAPTOP
.
Else, if the
agentRealtimeInfo.agentMachineType
log field value matches the regular expression pattern
desktop
, then the
principal.asset.type
UDM field is set to
WORKSTATION
.
Else, if the
agentRealtimeInfo.agentMachineType
log field value matches the regular expression pattern
server
, then the
principal.asset.type
UDM field is set to
SERVER
.
Else, the
agentRealtimeInfo.agentMachineType
log field is mapped to the
principal.asset.attribute.labels.agent_detection_info_machine_type
UDM field.
agentRealtimeInfo.machineType
principal.asset.type
If the
agentDetectionInfo.machineType
log field value is empty and the
agentRealtimeInfo.agentMachineType
log field value is empty and the
agentRealtimeInfo.machineType
log field value is
not
empty , then:
If the
agentRealtimeInfo.machineType
log field value matches the regular expression pattern
laptop
, then the
principal.asset.type
UDM field is set to
LAPTOP
.
Else, if the
agentRealtimeInfo.machineType
log field value matches the regular expression pattern
desktop
, then the
principal.asset.type
UDM field is set to
WORKSTATION
.
Else, if the
agentRealtimeInfo.machineType
log field value matches the regular expression pattern
server
, then the
principal.asset.type
UDM field is set to
SERVER
.
Else, the
agentRealtimeInfo.machineType
log field is mapped to the
principal.asset.attribute.labels.agent_detection_info_machine_type
UDM field.
agentDetectionInfo.name
principal.hostname
If the
agentDetectionInfo.name
log field value is
not
empty, then the
agentDetectionInfo.name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
agentRealtimeInfo.agentComputerName
log field value is
not
empty, then the
agentRealtimeInfo.agentComputerName
log field is mapped to the
principal.hostname
UDM field.
Else, if the
agentRealtimeInfo.name
log field value is
not
empty, then the
agentRealtimeInfo.name
log field is mapped to the
principal.hostname
UDM field.
agentRealtimeInfo.agentComputerName
principal.hostname
If the
agentDetectionInfo.name
log field value is
not
empty, then the
agentDetectionInfo.name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
agentRealtimeInfo.agentComputerName
log field value is
not
empty, then the
agentRealtimeInfo.agentComputerName
log field is mapped to the
principal.hostname
UDM field.
Else, if the
agentRealtimeInfo.name
log field value is
not
empty, then the
agentRealtimeInfo.name
log field is mapped to the
principal.hostname
UDM field.
agentRealtimeInfo.name
principal.hostname
If the
agentDetectionInfo.name
log field value is
not
empty, then the
agentDetectionInfo.name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
agentRealtimeInfo.agentComputerName
log field value is
not
empty, then the
agentRealtimeInfo.agentComputerName
log field is mapped to the
principal.hostname
UDM field.
Else, if the
agentRealtimeInfo.name
log field value is
not
empty, then the
agentRealtimeInfo.name
log field is mapped to the
principal.hostname
UDM field.
agentDetectionInfo.name
principal.asset.hostname
If the
agentDetectionInfo.name
log field value is
not
empty, then the
agentDetectionInfo.name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
agentRealtimeInfo.agentComputerName
log field value is
not
empty, then the
agentRealtimeInfo.agentComputerName
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
agentRealtimeInfo.name
log field value is
not
empty, then the
agentRealtimeInfo.name
log field is mapped to the
principal.asset.hostname
UDM field.
agentRealtimeInfo.agentComputerName
principal.asset.hostname
If the
agentDetectionInfo.name
log field value is
not
empty, then the
agentDetectionInfo.name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
agentRealtimeInfo.agentComputerName
log field value is
not
empty, then the
agentRealtimeInfo.agentComputerName
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
agentRealtimeInfo.name
log field value is
not
empty, then the
agentRealtimeInfo.name
log field is mapped to the
principal.asset.hostname
UDM field.
agentRealtimeInfo.name
principal.asset.hostname
If the
agentDetectionInfo.name
log field value is
not
empty, then the
agentDetectionInfo.name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
agentRealtimeInfo.agentComputerName
log field value is
not
empty, then the
agentRealtimeInfo.agentComputerName
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
agentRealtimeInfo.name
log field value is
not
empty, then the
agentRealtimeInfo.name
log field is mapped to the
principal.asset.hostname
UDM field.
agentDetectionInfo.osFamily
principal.asset.platform_software.platform
If the
agentDetectionInfo.osFamily
log field value matches the regular expression pattern
(?i)win
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
agentDetectionInfo.osFamily
log field value matches the regular expression pattern
(?i)lin
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
Else, the
agentDetectionInfo.osFamily
log field is mapped to the
principal.asset.attribute.labels.agent_detection_info_os_family
UDM field.
agentRealtimeInfo.os
principal.asset.platform_software.platform
If the
agentDetectionInfo.osFamily
log field value is empty and the
agentRealtimeInfo.os
log field value is
not
empty , then:
If the
agentRealtimeInfo.os
log field value matches the regular expression pattern
(?i)win
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
agentRealtimeInfo.os
log field value matches the regular expression pattern
(?i)lin
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
Else, the
agentRealtimeInfo.os
log field is mapped to the
principal.asset.attribute.labels.agent_detection_info_os_family
UDM field.
agentDetectionInfo.osFamily
principal.platform
If the
agentDetectionInfo.osFamily
log field value matches the regular expression pattern
(?i)win
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
agentDetectionInfo.osFamily
log field value matches the regular expression pattern
(?i)lin
, then the
principal.platform
UDM field is set to
LINUX
agentRealtimeInfo.os
principal.platform
If the
agentDetectionInfo.osFamily
log field value is empty and the
agentRealtimeInfo.os
log field value is
not
empty , then:
If the
agentRealtimeInfo.os
log field value matches the regular expression pattern
(?i)win
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
agentRealtimeInfo.os
log field value matches the regular expression pattern
(?i)lin
, then the
principal.platform
UDM field is set to
LINUX
.
agentDetectionInfo.osName
principal.asset.platform_software.platform_version
If the
agentDetectionInfo.osName
log field value is
not
empty, then the
agentDetectionInfo.osName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
Else, if the
agentDetectionInfo.agentOsName
log field value is
not
empty, then the
agentDetectionInfo.agentOsName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
Else, if the
agentRealtimeInfo.agentOsName
log field value is
not
empty, then the
agentRealtimeInfo.agentOsName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
agentDetectionInfo.agentOsName
principal.asset.platform_software.platform_version
If the
agentDetectionInfo.osName
log field value is
not
empty, then the
agentDetectionInfo.osName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
Else, if the
agentDetectionInfo.agentOsName
log field value is
not
empty, then the
agentDetectionInfo.agentOsName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
Else, if the
agentRealtimeInfo.agentOsName
log field value is
not
empty, then the
agentRealtimeInfo.agentOsName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
agentRealtimeInfo.agentOsName
principal.asset.platform_software.platform_version
If the
agentDetectionInfo.osName
log field value is
not
empty, then the
agentDetectionInfo.osName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
Else, if the
agentDetectionInfo.agentOsName
log field value is
not
empty, then the
agentDetectionInfo.agentOsName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
Else, if the
agentRealtimeInfo.agentOsName
log field value is
not
empty, then the
agentRealtimeInfo.agentOsName
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
agentDetectionInfo.osRevision
principal.asset.platform_software.platform_patch_level
If the
agentDetectionInfo.osRevision
log field value is
not
empty, then the
agentDetectionInfo.osRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
Else, if the
agentDetectionInfo.agentOsRevision
log field value is
not
empty, then the
agentDetectionInfo.agentOsRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
Else, if the
agentRealtimeInfo.agentOsRevision
log field value is
not
empty, then the
agentRealtimeInfo.agentOsRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
agentDetectionInfo.agentOsRevision
principal.asset.platform_software.platform_patch_level
If the
agentDetectionInfo.osRevision
log field value is
not
empty, then the
agentDetectionInfo.osRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
Else, if the
agentDetectionInfo.agentOsRevision
log field value is
not
empty, then the
agentDetectionInfo.agentOsRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
Else, if the
agentRealtimeInfo.agentOsRevision
log field value is
not
empty, then the
agentRealtimeInfo.agentOsRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
agentRealtimeInfo.agentOsRevision
principal.asset.platform_software.platform_patch_level
If the
agentDetectionInfo.osRevision
log field value is
not
empty, then the
agentDetectionInfo.osRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
Else, if the
agentDetectionInfo.agentOsRevision
log field value is
not
empty, then the
agentDetectionInfo.agentOsRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
Else, if the
agentRealtimeInfo.agentOsRevision
log field value is
not
empty, then the
agentRealtimeInfo.agentOsRevision
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
agentDetectionInfo.siteId
principal.labels[agent_detection_info_siteId]
(deprecated)
agentDetectionInfo.siteId
additional.fields[agent_detection_info_siteId]
agentDetectionInfo.uuid
principal.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
agentDetectionInfo.agentUuid
principal.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
agentRealtimeInfo.uuid
principal.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
agentRealtimeInfo.agentUuid
principal.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset_id
UDM field.
agentDetectionInfo.uuid
principal.asset.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
agentDetectionInfo.agentUuid
principal.asset.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
agentRealtimeInfo.uuid
principal.asset.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
agentRealtimeInfo.agentUuid
principal.asset.asset_id
If the
agentDetectionInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentDetectionInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentDetectionInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.uuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.uuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
agentRealtimeInfo.agentUuid
log field value is
not
empty, then the
SentinelOne:%{agentRealtimeInfo.agentUuid}
log field is mapped to the
principal.asset.asset_id
UDM field.
agentDetectionInfo.version
principal.asset.attribute.labels[agent_version]
agentDetectionInfo.agentVersion
principal.asset.attribute.labels[agent_detection_info_agent_version]
agentRealtimeInfo.agentVersion
principal.asset.attribute.labels[agent_realtime_info_agent_version]
agentRealtimeInfo.id
principal.asset.attribute.labels[agent_realtime_info_id]
agentRealtimeInfo.infected
principal.asset.attribute.labels[agent_realtime_info_infected]
agentRealtimeInfo.agentInfected
principal.asset.attribute.labels[agent_realtime_info_infected]
agentRealtimeInfo.isActive
principal.asset.attribute.labels[agent_realtime_info_is_active]
agentRealtimeInfo.agentIsActive
principal.asset.attribute.labels[agent_realtime_info_is_active]
agentRealtimeInfo.isDecommissioned
principal.asset.attribute.labels[agent_realtime_info_is_decommissioned]
agentRealtimeInfo.agentIsDecommissioned
principal.asset.attribute.labels[agent_realtime_info_is_decommissioned]
alertInfo.alertId
metadata.product_log_id
id
metadata.product_log_id
metadata.product_event_type
If the log matches the regular expression pattern
alertInfo
, then the
metadata.product_event_type
UDM field is set to
Alerts
.
Else, if the log matches the regular expression pattern
threatInfo
, then the
metadata.product_event_type
UDM field is set to
Threats
.
alertInfo.analystVerdict
security_result.detection_fields[alert_info_analyst_verdict]
alertInfo.createdAt
metadata.event_timestamp
If the
alertInfo.createdAt
log field value is
not
empty, then the
alertInfo.createdAt
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
threatInfo.identifiedAt
log field value is
not
empty, then the
threatInfo.identifiedAt
log field is mapped to the
metadata.event_timestamp
UDM field.
threatInfo.identifiedAt
metadata.event_timestamp
If the
alertInfo.createdAt
log field value is
not
empty, then the
alertInfo.createdAt
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
threatInfo.identifiedAt
log field value is
not
empty, then the
threatInfo.identifiedAt
log field is mapped to the
metadata.event_timestamp
UDM field.
network.application_protocol
If the
alertInfo.dnsRequest
log field value is
not
empty, then the
network.application_protocol
UDM field is set to
DNS
.
alertInfo.dnsRequest
network.dns.questions.name
alertInfo.dnsResponse
network.dns.answers.name
alertInfo.dstIp
target.ip
alertInfo.dstPort
target.port
alertInfo.dvEventId
security_result.detection_fields[alert_info_dv_event_id]
alertInfo.eventType
security_result.detection_fields[alert_info_event_type]
alertInfo.hitType
security_result.detection_fields[alert_info_hit_type]
alertInfo.incidentStatus
security_result.detection_fields[alert_info_incident_status]
alertInfo.indicatorCategory
security_result.detection_fields[alert_info_indicator_category]
alertInfo.indicatorDescription
security_result.detection_fields[alert_info_indicator_description]
alertInfo.indicatorName
security_result.detection_fields[alert_info_indicator_name]
alertInfo.isEdr
security_result.detection_fields[alert_info_is_edr]
alertInfo.loginAccountDomain
security_result.detection_fields[alert_info_login_account_domain]
alertInfo.loginAccountSid
security_result.detection_fields[alert_info_login_account_sid]
alertInfo.loginIsAdministratorEquivalent
security_result.detection_fields[alert_info_login_is_administrator_equivalent]
security_result.action
If the
alertInfo.loginIsSuccessful
log field value is equal to
true
, then the
security_result.action
UDM field is set to
ALLOW
. else the
alertInfo.loginIsSuccessful
log field value is equal to
false
, then the
security_result.action
UDM field is set to
BLOCK
.
If the
threatInfo.mitigationStatus
log field value contain one of the following values, then the
security_result.action
UDM field is set to
BLOCK
.
mitigated
marked_as_benign
blocked
suspicious_resolved
Else, if the
threatInfo.mitigationStatus
log field value contain one of the following values, then the
security_result.action
UDM field is set to
ALLOW
.
active
suspicious
pending
not_mitigated
extensions.auth.mechanism
If the
alertInfo.loginType
log field value is equal to
NETWORK
, then the
extensions.auth.mechanism
UDM field is set to
NETWORK
.
Else, if the
alertInfo.loginType
log field value is equal to
SYSTEM
, then the
extensions.auth.mechanism
UDM field is set to
LOCAL
.
Else, if the
alertInfo.loginType
log field value is equal to
INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
INTERACTIVE
.
Else, if the
alertInfo.loginType
log field value is equal to
BATCH
, then the
extensions.auth.mechanism
UDM field is set to
BATCH
.
Else, if the
alertInfo.loginType
log field value is equal to
SERVICE
, then the
extensions.auth.mechanism
UDM field is set to
SERVICE
.
Else, if the
alertInfo.loginType
log field value is equal to
UNLOCK
, then the
extensions.auth.mechanism
UDM field is set to
UNLOCK
.
Else, if the
alertInfo.loginType
log field value is equal to
NETWORK_CLEAR_TEXT
, then the
extensions.auth.mechanism
UDM field is set to
NETWORK_CLEAR_TEXT
.
Else, if the
alertInfo.loginType
log field value is equal to
NEW_CREDENTIALS
, then the
extensions.auth.mechanism
UDM field is set to
NEW_CREDENTIALS
.
Else, if the
alertInfo.loginType
log field value is equal to
REMOTE_INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
Else, if the
alertInfo.loginType
log field value is equal to
CACHED_INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_INTERACTIVE
.
Else, if the
alertInfo.loginType
log field value is equal to
CACHED_REMOTE_INTERACTIVE
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_REMOTE_INTERACTIVE
.
Else, if the
alertInfo.loginType
log field value is equal to
CACHED_UNLOCK
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_UNLOCK
.
alertInfo.loginsUserName
target.user.user_display_name
alertInfo.modulePath
security_result.detection_fields[alert_info_module_path]
alertInfo.moduleSha1
security_result.detection_fields[alert_info_module_sha1]
alertInfo.netEventDirection
network.direction
If the
alertInfo.netEventDirection
log field value matches the regular expression pattern
OUTGOING
, then the
network.direction
UDM field is set to
OUTBOUND
.
Else, if the
alertInfo.netEventDirection
log field value matches the regular expression pattern
INCOMING
, then the
network.direction
UDM field is set to
INBOUND
.
alertInfo.registryKeyPath
target.registry.registry_key
alertInfo.registryOldValue
src.registry.registry_value_data
alertInfo.registryOldValueType
src.registry.registry_value_name
alertInfo.registryPath
src.registry.registry_key
alertInfo.registryValue
target.registry.registry_value_data
alertInfo.reportedAt
security_result.first_discovered_time
alertInfo.source
security_result.category_details
alertInfo.srcPort
principal.port
alertInfo.tiIndicatorComparisonMethod
security_result.detection_fields[alert_info_tiIndicator_comparison_method]
alertInfo.tiIndicatorSource
security_result.detection_fields[alert_info_tiIndicator_source]
alertInfo.tiIndicatorType
security_result.detection_fields[alert_info_tiIndicator_type]
alertInfo.tiIndicatorValue
security_result.detection_fields[alert_info_tiIndicator_value]
alertInfo.updatedAt
security_result.detection_fields[alert_info_updated_at]
containerInfo.id
target.resource.product_object_id
containerInfo.image
target.resource.attribute.labels[container_image]
containerInfo.labels
target.resource.attribute.labels[container_labels]
If the
containerInfo.labels
log field value is
not
empty, then the
containerInfo.labels
log field is mapped to the
target.resource.attribute.labels.container_labels
UDM field.
containerInfo.name
target.resource.name
target.resource.resource_type
If the
containerInfo.name
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
CONTAINER
.
kubernetesInfo.cluster
target.resource_ancestors.name
kubernetesInfo.controllerName
target.resource_ancestors.name
kubernetesInfo.node
target.resource_ancestors.name
kubernetesInfo.pod
target.resource_ancestors.name
target.resource_ancestors.resource_type
If the
kubernetesInfo.pod
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
POD
.
If the
kubernetesInfo.cluster
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
If the
kubernetesInfo.isContainerQuarantine
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
If the
kubernetesInfo.controllerName
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
If the
kubernetesInfo.node
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
kubernetesInfo.controllerKind
target.resource_ancestors.attribute.labels[kubernetes_controller_kind]
kubernetesInfo.controllerLabels
target.resource_ancestors.attribute.labels[kubernetes_controller_labels]
If the
kubernetesInfo.controllerLabels
log field value is
not
empty, then the
kubernetesInfo.controllerLabels
log field is mapped to the
target.resource_ancestors.attribute.labels.kubernetes_controller_labels
UDM field.
kubernetesInfo.namespace
target.resource_ancestors.attribute.labels[kubernetes_namespace]
kubernetesInfo.namespaceLabels
target.resource_ancestors.attribute.labels[kubernetes_namespace_labels]
kubernetesInfo.podLabels
target.resource_ancestors.attribute.labels[kubernetes_pod_labels]
If the
kubernetesInfo.podLabels
log field value is
not
empty, then the
kubernetesInfo.podLabels
log field is mapped to the
target.resource_ancestors.attribute.labels.kubernetes_pod_labels
UDM field.
ruleInfo.description
security_result.rule_set_display_name
ruleInfo.id
security_result.rule_id
ruleInfo.name
security_result.rule_name
ruleInfo.queryLang
security_result.rule_labels[query_lang]
ruleInfo.queryType
security_result.rule_labels[query_type]
ruleInfo.s1ql
security_result.rule_labels[s1ql]
ruleInfo.scopeLevel
security_result.rule_labels[scope_level]
security_result.severity
If the
ruleInfo.severity
log field value matches the regular expression pattern
(?i)low
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
ruleInfo.severity
log field value matches the regular expression pattern
(?i)medium
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
ruleInfo.severity
log field value matches the regular expression pattern
(?i)critical
, then the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
ruleInfo.severity
log field value matches the regular expression pattern
(?i)high
, then the
security_result.severity
UDM field is set to
HIGH
.
ruleInfo.severity
security_result.severity_details
ruleInfo.treatAsThreat
security_result.rule_type
sourceParentProcessInfo.commandline
principal.process.parent_process.command_line
sourceParentProcessInfo.fileHashMd5
principal.process.parent_process.file.md5
If the
sourceParentProcessInfo.fileHashMd5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
sourceParentProcessInfo.fileHashMd5
log field is mapped to the
principal.process.parent_process.file.md5
UDM field.
sourceParentProcessInfo.fileHashSha1
principal.process.parent_process.file.sha1
If the
sourceParentProcessInfo.fileHashSha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
sourceParentProcessInfo.fileHashSha1
log field is mapped to the
principal.process.parent_process.file.sha1
UDM field.
sourceParentProcessInfo.fileHashSha256
principal.process.parent_process.file.sha256
If the
sourceParentProcessInfo.fileHashSha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
sourceParentProcessInfo.fileHashSha256
log field is mapped to the
principal.process.parent_process.file.sha256
UDM field.
sourceParentProcessInfo.filePath
principal.process.parent_process.file.full_path
sourceParentProcessInfo.fileSignerIdentity
principal.process.parent_process.file.signature_info.sigcheck.signers.name
sourceParentProcessInfo.integrityLevel
principal.labels[source_parent_process_integrity_level]
(deprecated)
sourceParentProcessInfo.integrityLevel
additional.fields[source_parent_process_integrity_level]
sourceParentProcessInfo.name
principal.labels[source_parent_process_name]
(deprecated)
sourceParentProcessInfo.name
additional.fields[source_parent_process_name]
sourceParentProcessInfo.pid
principal.process.parent_process.pid
sourceParentProcessInfo.pidStarttime
principal.labels[source_parent_process_pid_start_time]
(deprecated)
sourceParentProcessInfo.pidStarttime
additional.fields[source_parent_process_pid_start_time]
sourceParentProcessInfo.storyline
principal.labels[source_parent_process_storyline]
(deprecated)
sourceParentProcessInfo.storyline
additional.fields[source_parent_process_storyline]
sourceParentProcessInfo.subsystem
principal.labels[source_parent_process_subsystem]
(deprecated)
sourceParentProcessInfo.subsystem
additional.fields[source_parent_process_subsystem]
principal.process.parent_process.product_specific_process_id
If the
sourceParentProcessInfo.uniqueId
log field value is
not
empty, then the
SO:%{agentDetectionInfo.siteId}:%{agentDetectionInfo.accountId}:%{agentDetectionInfo.uuid}:%{sourceParentProcessInfo.uniqueId}
log field is mapped to the
principal.process.parent_process.product_specific_process_id
UDM field.
sourceParentProcessInfo.user
principal.labels[source_parent_process_user]
(deprecated)
sourceParentProcessInfo.user
additional.fields[source_parent_process_user]
sourceProcessInfo.commandline
principal.process.command_line
sourceProcessInfo.fileHashMd5
principal.process.file.md5
If the
sourceProcessInfo.fileHashMd5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
sourceProcessInfo.fileHashMd5
log field is mapped to the
principal.process.file.md5
UDM field.
sourceProcessInfo.fileHashSha1
principal.process.file.sha1
If the
sourceProcessInfo.fileHashSha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
sourceProcessInfo.fileHashSha1
log field is mapped to the
principal.process.file.sha1
UDM field.
sourceProcessInfo.fileHashSha256
principal.process.file.sha256
If the
sourceProcessInfo.fileHashSha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
sourceProcessInfo.fileHashSha256
log field is mapped to the
principal.process.file.sha256
UDM field.
sourceProcessInfo.filePath
principal.process.file.full_path
sourceProcessInfo.fileSignerIdentity
principal.process.file.signature_info.sigcheck.signers.name
sourceProcessInfo.integrityLevel
principal.labels[source_process_integrity_level]
(deprecated)
sourceProcessInfo.integrityLevel
additional.fields[source_process_integrity_level]
sourceProcessInfo.name
principal.labels[source_process_name]
(deprecated)
sourceProcessInfo.name
additional.fields[source_process_name]
sourceProcessInfo.pid
principal.process.pid
sourceProcessInfo.pidStarttime
principal.labels[source_process_pid_start_time]
(deprecated)
sourceProcessInfo.pidStarttime
additional.fields[source_process_pid_start_time]
sourceProcessInfo.storyline
principal.labels[source_process_storyline]
(deprecated)
sourceProcessInfo.storyline
additional.fields[source_process_storyline]
sourceProcessInfo.subsystem
principal.labels[source_process_subsystem]
(deprecated)
sourceProcessInfo.subsystem
additional.fields[source_process_subsystem]
principal.process.product_specific_process_id
If the
sourceProcessInfo.uniqueId
log field value is
not
empty, then the
SO:%{agentDetectionInfo.siteId}:%{agentDetectionInfo.accountId}:%{agentDetectionInfo.uuid}:%{sourceProcessInfo.uniqueId}
log field is mapped to the
principal.process.product_specific_process_id
UDM field.
sourceProcessInfo.user
principal.user.user_display_name
threatInfo.initiatingUsername
principal.user.user_display_name
targetProcessInfo.tgtFileCreatedAt
target.process.file.first_seen_time
targetProcessInfo.tgtFileHashSha1
target.process.file.sha1
If the
targetProcessInfo.tgtFileHashSha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
targetProcessInfo.tgtFileHashSha1
log field is mapped to the
target.process.file.sha1
UDM field.
targetProcessInfo.tgtFileHashSha256
target.process.file.sha256
If the
targetProcessInfo.tgtFileHashSha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
targetProcessInfo.tgtFileHashSha256
log field is mapped to the
target.process.file.sha256
UDM field.
targetProcessInfo.tgtFileId
target.labels[target_file_id]
(deprecated)
targetProcessInfo.tgtFileId
additional.fields[target_file_id]
targetProcessInfo.tgtFileIsSigned
target.process.file.signature_info.sigcheck.verification_message
targetProcessInfo.tgtFileModifiedAt
target.process.file.last_modification_time
targetProcessInfo.tgtFileOldPath
target.labels[target_file_old_path]
(deprecated)
targetProcessInfo.tgtFileOldPath
additional.fields[target_file_old_path]
targetProcessInfo.tgtFilePath
target.process.file.full_path
targetProcessInfo.tgtProcCmdLine
target.process.command_line
targetProcessInfo.tgtProcImagePath
target.labels[target_process_image_path]
(deprecated)
targetProcessInfo.tgtProcImagePath
additional.fields[target_process_image_path]
targetProcessInfo.tgtProcIntegrityLevel
target.labels[target_process_integrity_level]
(deprecated)
targetProcessInfo.tgtProcIntegrityLevel
additional.fields[target_process_integrity_level]
targetProcessInfo.tgtProcName
target.labels[target_process_name]
(deprecated)
targetProcessInfo.tgtProcName
additional.fields[target_process_name]
targetProcessInfo.tgtProcPid
target.process.pid
targetProcessInfo.tgtProcSignedStatus
target.labels[target_process_signed_status]
(deprecated)
targetProcessInfo.tgtProcSignedStatus
additional.fields[target_process_signed_status]
targetProcessInfo.tgtProcStorylineId
target.labels[target_process_storyline_id]
(deprecated)
targetProcessInfo.tgtProcStorylineId
additional.fields[target_process_storyline_id]
target.process.product_specific_process_id
If the
targetProcessInfo.tgtProcUid
log field value is
not
empty, then the
SO:%{agentDetectionInfo.siteId}:%{agentDetectionInfo.accountId}:%{agentDetectionInfo.uuid}:%{targetProcessInfo.tgtProcUid}
log field is mapped to the
target.process.product_specific_process_id
UDM field.
targetProcessInfo.tgtProcessStartTime
target.labels[target_process_start_time]
(deprecated)
targetProcessInfo.tgtProcessStartTime
additional.fields[target_process_start_time]
source_hostname
intermediary.hostname
agentDetectionInfo.accountId
metadata.product_deployment_id
agentDetectionInfo.accountName
principal.labels[agent_detection_info_account_name]
(deprecated)
agentDetectionInfo.accountName
additional.fields[agent_detection_info_account_name]
agentDetectionInfo.agentDetectionState
principal.asset.attribute.labels[agent_detection_info_detection_state]
agentDetectionInfo.agentDomain
principal.administrative_domain
agentDetectionInfo.agentIpV4
principal.ip
agentDetectionInfo.agentIpV6
principal.ip
alertInfo.srcIp
principal.ip
alertInfo.srcMachineIp
principal.ip
agentDetectionInfo.agentIpV4
principal.asset.ip
agentDetectionInfo.agentIpV6
principal.asset.ip
alertInfo.srcIp
principal.asset.ip
alertInfo.srcMachineIp
principal.asset.ip
agentDetectionInfo.agentLastLoggedInUpn
principal.labels[agent_detection_info_last_logged_in_upn]
(deprecated)
agentDetectionInfo.agentLastLoggedInUpn
additional.fields[agent_detection_info_last_logged_in_upn]
agentDetectionInfo.agentLastLoggedInUserMail
principal.user.email_addresses
agentDetectionInfo.agentLastLoggedInUserName
principal.user.attribute.labels[agent_last_loggedIn_user_name]
agentDetectionInfo.agentMitigationMode
principal.asset.attribute.labels[agent_detection_info_mitigation_mode]
agentDetectionInfo.agentRegisteredAt
principal.asset.first_discover_time
agentDetectionInfo.externalIp
principal.nat_ip
agentDetectionInfo.groupId
principal.group.attribute.labels[agent_detection_info_group_id]
agentRealtimeInfo.groupId
principal.group.attribute.labels[agent_realtime_info_group_id]
agentDetectionInfo.groupName
principal.group.group_display_name
If the
agentDetectionInfo.groupName
log field value is
not
empty, then the
agentDetectionInfo.groupName
log field is mapped to the
principal.group.group_display_name
UDM field.
If the
agentDetectionInfo.groupName
log field value is empty and the
agentRealtimeInfo.groupName
log field value is
not
empty, then the
agentRealtimeInfo.groupName
log field is mapped to the
principal.group.group_display_name
UDM field.
Else, the
agentRealtimeInfo.groupName
log field is mapped to the
principal.group.attribute.labels.agent_realtime_info_group_name
UDM field.
agentRealtimeInfo.groupName
principal.group.group_display_name
If the
agentDetectionInfo.groupName
log field value is
not
empty, then the
agentDetectionInfo.groupName
log field is mapped to the
principal.group.group_display_name
UDM field.
If the
agentDetectionInfo.groupName
log field value is empty and the
agentRealtimeInfo.groupName
log field value is
not
empty, then the
agentRealtimeInfo.groupName
log field is mapped to the
principal.group.group_display_name
UDM field.
Else, the
agentRealtimeInfo.groupName
log field is mapped to the
principal.group.attribute.labels.agent_realtime_info_group_name
UDM field.
agentDetectionInfo.siteName
principal.labels[agent_detection_info_site_name]
(deprecated)
agentDetectionInfo.siteName
additional.fields[agent_detection_info_site_name]
agentRealtimeInfo.siteName
principal.labels[agent_realtime_info_site_name]
(deprecated)
agentRealtimeInfo.siteName
additional.fields[agent_realtime_info_site_name]
agentRealtimeInfo.accountId
principal.labels[agent_realtime_info_account_id]
(deprecated)
agentRealtimeInfo.accountId
additional.fields[agent_realtime_info_account_id]
agentRealtimeInfo.accountName
principal.labels[agent_realtime_info_account_name]
(deprecated)
agentRealtimeInfo.accountName
additional.fields[agent_realtime_info_account_name]
agentRealtimeInfo.activeThreats
security_result.detection_fields[agent_realtime_info_active_threats]
agentRealtimeInfo.agentDecommissionedAt
principal.asset.attribute.labels[agent_realtime_info_agent_decommissioned_at]
agentRealtimeInfo.agentDomain
principal.labels[agent_realtime_info_domain]
(deprecated)
agentRealtimeInfo.agentDomain
additional.fields[agent_realtime_info_domain]
agentRealtimeInfo.agentId
principal.asset.attribute.labels[agent_realtime_info_agent_id]
agentRealtimeInfo.agentMitigationMode
principal.asset.attribute.labels[agent_realtime_info_mitigation_mode]
agentRealtimeInfo.agentNetworkStatus
principal.labels[agent_realtime_info_network_status]
(deprecated)
agentRealtimeInfo.agentNetworkStatus
additional.fields[agent_realtime_info_network_status]
agentRealtimeInfo.agentOsType
principal.labels[agent_realtime_info_os_type]
(deprecated)
agentRealtimeInfo.agentOsType
additional.fields[agent_realtime_info_os_type]
agentRealtimeInfo.networkInterfaces.id
principal.labels[network_interface_id]
agentRealtimeInfo.networkInterfaces.name
principal.labels[network_interface_name]
agentRealtimeInfo.networkInterfaces.physical
principal.labels[network_interface_physical]
agentRealtimeInfo.operationalState
principal.asset.attribute.labels[agent_realtime_info_operational_State]
agentRealtimeInfo.rebootRequired
principal.labels[agent_realtime_info_reboot_required]
(deprecated)
agentRealtimeInfo.rebootRequired
additional.fields[agent_realtime_info_reboot_required]
agentRealtimeInfo.scanAbortedAt
security_result.detection_fields[agent_realtime_info_scan_aborted_at]
agentRealtimeInfo.scanFinishedAt
security_result.detection_fields[agent_realtime_info_scan_finished_at]
agentRealtimeInfo.scanStartedAt
security_result.detection_fields[agent_realtime_info_scan_started_at]
agentRealtimeInfo.scanStatus
security_result.detection_fields[agent_realtime_info_scan_status]
agentRealtimeInfo.siteId
principal.labels[agent_realtime_info_site_id]
(deprecated)
agentRealtimeInfo.siteId
additional.fields[agent_realtime_info_site_id]
agentRealtimeInfo.storageName
principal.resource.name
principal.resource.resource_type
If the
agentRealtimeInfo.storageName
log field value is
not
empty, then the
principal.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
agentRealtimeInfo.storageType
principal.resource.resource_subtype
agentRealtimeInfo.userActionsNeeded
security_result.detection_fields[agent_realtime_info_user_actions_needed]
If the
agentRealtimeInfo.userActionsNeeded
log field value is
not
empty, then the
agentRealtimeInfo.userActionsNeeded
log field is mapped to the
security_result.detection_fields.agent_realtime_info_user_actions_needed
UDM field.
containerInfo.isContainerQuarantine
target.resource.attribute.labels[container_is_container_quarantine]
indicators.category
security_result.category_details
indicators.categoryId
security_result.detection_fields[indicators_category_id]
indicators.description
security_result.description
indicators.ids
security_result.detection_fields[indicators_ids]
security_result.attack_details.tactics.id
indicators.tactics.name
security_result.attack_details.tactics.name
If the
indicators.tactics.name
log field value is
not
empty, then the
indicators.tactics.name
log field is mapped to the
security_result.attack_details.tactics.name
UDM field.
indicators.tactics.source
security_result.detection_fields[indicators_tactics_source]
indicators.tactics.techniques.link
security_result.detection_fields[indicators_tactics_techniques_link]
indicators.tactics.techniques.name
security_result.attack_details.techniques.id
If the
indicators.tactics.techniques.name
log field value is
not
empty, then the
indicators.tactics.techniques.name
log field is mapped to the
security_result.attack_details.techniques.id
UDM field.
security_result.attack_details.techniques.name
security_result.attack_details.techniques.subtechnique_id
security_result.attack_details.techniques.subtechnique_name
kubernetesInfo.isContainerQuarantine
target.resource_ancestors.attribute.labels[kubernetes_is_container_quarantine]
kubernetesInfo.nodeLabels
target.resource_ancestors.attribute.labels[kubernetes_node_labels]
mitigationStatus.action
security_result.detection_fields[mitigation_status_action]
mitigationStatus.actionsCounters.failed
security_result.detection_fields[mitigation_status_actions_counters_failed]
mitigationStatus.actionsCounters.notFound
security_result.detection_fields[mitigation_status_actions_counters_not_Found]
mitigationStatus.actionsCounters.pendingReboot
security_result.detection_fields[mitigation_status_actions_counters_pending_reboot]
mitigationStatus.actionsCounters.success
security_result.detection_fields[mitigation_status_actions_counters_success]
mitigationStatus.actionsCounters.total
security_result.detection_fields[mitigation_status_actions_counters_total]
mitigationStatus.agentSupportsReport
security_result.detection_fields[mitigation_status_agent_supports_report]
mitigationStatus.groupNotFound
security_result.detection_fields[mitigation_status_group_not_found]
mitigationStatus.lastUpdate
security_result.detection_fields[mitigation_status_last_update]
mitigationStatus.latestReport
security_result.detection_fields[mitigation_status_last_report]
mitigationStatus.mitigationEndedAt
security_result.detection_fields[mitigation_status_mitigation_ended_at]
mitigationStatus.mitigationStartedAt
security_result.detection_fields[mitigation_status_mitigation_started_at]
mitigationStatus.status
security_result.detection_fields[mitigation_status]
threatInfo.analystVerdict
security_result.detection_fields[analystVerdict]
threatInfo.analystVerdictDescription
security_result.detection_fields[analyst_verdict_description]
threatInfo.automaticallyResolved
security_result.detection_fields[automatically_resolved]
threatInfo.browserType
security_result.detection_fields[browser_type]
threatInfo.certificateId
security_result.detection_fields[certificate_id]
threatInfo.classification
security_result.category_details
security_result.category
If the
threatInfo.classification
log field value contain one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
Malware
Ransomware
Linux.Malware
OSX.Malware
Manual
Else, if the
threatInfo.classification
log field value contain one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_SUSPICIOUS
.
Trojan
miner
Virus
Malicious PDF
Worm
Rootkit
Infostealer
Lateral Movement
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
Remote shell
Else, if the
threatInfo.classification
log field value contain one of the following values, then the
security_result.category
UDM field is set to
NETWORK_SUSPICIOUS
.
Lateral Movement
Remote shell
Else, if the
threatInfo.classification
log field value is equal to
Exploit
, then the
security_result.category
UDM field is set to
EXPLOIT
.
Else, if the
threatInfo.classification
log field value is equal to
Application Control
, then the
security_result.category
UDM field is set to
UNKNOWN_CATEGORY
.
If the
alertInfo.eventType
log field value contain one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
BEHAVIORALINDICATORS
MALICIOUSFILE
threatInfo.classificationSource
security_result.detection_fields[classification_source]
threatInfo.cloudFilesHashVerdict
security_result.detection_fields[cloud_Files_hash_verdict]
threatInfo.collectionId
security_result.detection_fields[collection_id]
threatInfo.confidenceLevel
security_result.confidence_details
security_result.confidence
If the
threatInfo.confidenceLevel
log field value is equal to
malicious
, then the
security_result.confidence
UDM field is set to
HIGH_CONFIDENCE
.
Else, if the
threatInfo.confidenceLevel
log field value is equal to
suspicious
, then the
security_result.confidence
UDM field is set to
MEDIUM_CONFIDENCE
.
threatInfo.createdAt
metadata.collected_timestamp
threatInfo.detectionEngines
security_result.detection_fields[detection_engines]
If the
threatInfo.detectionEngines
log field value is
not
empty, then the
threatInfo.detectionEngines
log field is mapped to the
security_result.detection_fields.detection_engines
UDM field.
threatInfo.detectionEngines.key
security_result.detection_fields[detection_engines_key]
If the
threatInfo.detectionEngines.key
log field value is
not
empty, then the
threatInfo.detectionEngines.key
log field is mapped to the
security_result.detection_fields.detection_engines_key
UDM field.
threatInfo.detectionEngines.title
security_result.detection_fields[detection_engines_title]
If the
threatInfo.detectionEngines.title
log field value is
not
empty, then the
threatInfo.detectionEngines.title
log field is mapped to the
security_result.detection_fields.detection_engines_title
UDM field.
threatInfo.detectionType
security_result.detection_fields[detection_type]
threatInfo.engines
security_result.detection_fields[engines]
If the
threatInfo.engines
log field value is
not
empty, then the
threatInfo.engines
log field is mapped to the
security_result.detection_fields.engines
UDM field.
threatInfo.externalTicketExists
security_result.detection_fields[external_ticket_exists]
threatInfo.externalTicketExists.description
security_result.detection_fields[external_ticket_exists_description]
threatInfo.externalTicketExists.readOnly
security_result.detection_fields[external_ticket_exists_readOnly]
threatInfo.externalTicketId
security_result.detection_fields[external_ticket_id]
threatInfo.failedActions
security_result.detection_fields[failed_actions]
threatInfo.fileExtension
target.file.mime_type
threatInfo.fileExtensionType
security_result.detection_fields[file_extension_type]
threatInfo.filePath
target.file.full_path
threatInfo.filePath.description
security_result.detection_fields[file_path_description]
threatInfo.filePath.readOnly
security_result.detection_fields[file_path_readOnly]
threatInfo.fileSize
target.file.size
threatInfo.fileVerificationType
security_result.detection_fields[file_verification_type]
threatInfo.incidentStatus
security_result.detection_fields[incident_status]
threatInfo.incidentStatusDescription
security_result.detection_fields[incident_status_description]
threatInfo.incidentStatusDescription.description
security_result.detection_fields[incident_status_description]
threatInfo.incidentStatusDescription.readOnly
security_result.detection_fields[incident_status_description_readOnly]
threatInfo.initiatedBy
security_result.detection_fields[initiatedBy]
threatInfo.initiatedByDescription
security_result.detection_fields[initiatedBy_description]
threatInfo.initiatedByDescription.description
security_result.detection_fields[initiatedBy_description]
threatInfo.initiatedByDescription.readOnly
security_result.detection_fields[initiatedBy_description_readOnly]
threatInfo.initiatingUserId
principal.user.attribute.labels[initiating_user_id]
threatInfo.isFileless
security_result.detection_fields[is_fileless]
threatInfo.isFileless.description
security_result.detection_fields[is_fileless_description]
threatInfo.isFileless.readOnly
security_result.detection_fields[is_fileless_readOnly]
threatInfo.isValidCertificate
security_result.detection_fields[is_valid_certificate]
threatInfo.maliciousProcessArguments
security_result.detection_fields[malicious_process_arguments]
threatInfo.md5
target.file.md5
If the
threatInfo.md5
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
threatInfo.md5
log field is mapped to the
target.file.md5
UDM field.
threatInfo.mitigatedPreemptively
security_result.detection_fields[mitigated_preemptively]
threatInfo.mitigationStatus
security_result.action_details
security_result.threat_status
If the
threatInfo.mitigationStatus
log field value contain one of the following values, then the
security_result.threat_status
UDM field is set to
CLEARED
.
mitigated
marked_as_benign
blocked
suspicious_resolved
Else, if the
threatInfo.mitigationStatus
log field value contain one of the following values, then the
security_result.threat_status
UDM field is set to
ACTIVE
.
active
suspicious
pending
not_mitigated
threatInfo.mitigationStatusDescription
security_result.detection_fields[mitigation_status_description]
threatInfo.mitigationStatusDescription.description
security_result.detection_fields[mitigation_status_description]
threatInfo.mitigationStatusDescription.readOnly
security_result.detection_fields[mitigation_status_description_readOnly]
threatInfo.originatorProcess
principal.process.parent_process.file.names
threatInfo.pendingActions
security_result.detection_fields[pending_actions]
threatInfo.processUser
principal.user.userid
threatInfo.publisherName
security_result.threat_feed_name
threatInfo.reachedEventsLimit
security_result.detection_fields[reached_events_limit]
threatInfo.rebootRequired
security_result.detection_fields[reboot_required]
threatInfo.sha1
target.file.sha1
If the
threatInfo.sha1
log field value matches the regular expression pattern
^[a-f0-9]{40}$"
, then the
threatInfo.sha1
log field is mapped to the
target.file.sha1
UDM field.
threatInfo.sha256
target.file.sha256
If the
threatInfo.sha256
log field value matches the regular expression pattern
^[a-f0-9]{64}$"
, then the
threatInfo.sha256
log field is mapped to the
target.file.sha256
UDM field.
threatInfo.storyline
security_result.detection_fields[storyline]
threatInfo.threatId
security_result.threat_id
threatInfo.threatName
security_result.threat_name
threatInfo.threatName
target.file.names
threatInfo.updatedAt
security_result.detection_fields[updatedAt]
whiteningOptions
about.labels[whitening_options]
If the
whiteningOptions
log field value is
not
empty, then the
whiteningOptions
log field is mapped to the
about.labels.whitening_options
UDM field.
agentDetectionInfo.cloudProviders.AWS.awsRole
principal.resource.attribute.roles.name
agentDetectionInfo.cloudProviders.AWS.awsSecurityGroups
principal.resource.attribute.labels[cloud_providers_AWS_security_groups]
If the
agentDetectionInfo.cloudProviders.AWS.awsSecurityGroups
log field value is
not
empty, then the
agentDetectionInfo.cloudProviders.AWS.awsSecurityGroups
log field is mapped to the
principal.resource.attribute.labels.cloud_providers_AWS_security_groups
UDM field.
agentDetectionInfo.cloudProviders.AWS.awsSubnetIds
principal.resource.attribute.labels[cloud_providers_AWS_subnet_ids]
If the
agentDetectionInfo.cloudProviders.AWS.awsSubnetIds
log field value is
not
empty, then the
agentDetectionInfo.cloudProviders.AWS.awsSubnetIds
log field is mapped to the
principal.resource.attribute.labels.cloud_providers_AWS_subnet_ids
UDM field.
agentDetectionInfo.cloudProviders.AWS.cloudAccount
principal.resource.attribute.labels[cloud_providers_AWS_cloud_account]
agentDetectionInfo.cloudProviders.AWS.cloudImage
principal.resource.attribute.labels[cloud_providers_AWS_cloud_image]
agentDetectionInfo.cloudProviders.AWS.cloudInstanceId
principal.resource.attribute.labels[cloud_providers_AWS_cloud_instance_id]
agentDetectionInfo.cloudProviders.AWS.cloudInstanceSize
principal.resource.attribute.labels[cloud_providers_AWS_cloud_instance_size]
agentDetectionInfo.cloudProviders.AWS.cloudLocation
principal.resource.attribute.cloud.availability_zone
agentDetectionInfo.cloudProviders.AWS.cloudNetwork
principal.resource.attribute.labels[cloud_providers_AWS_cloud_network]
agentDetectionInfo.cloudProviders.AWS.cloudTags
principal.resource.attribute.labels[cloud_providers_AWS_cloud_tags]
If the
agentDetectionInfo.cloudProviders.AWS.cloudTags
log field value is
not
empty, then the
agentDetectionInfo.cloudProviders.AWS.cloudTags
log field is mapped to the
principal.resource.attribute.labels.cloud_providers_AWS_cloud_tags
UDM field.
modular_input_consumption_time
about.labels[modular_input_consumption_time]
(deprecated)
modular_input_consumption_time
additional.fields[modular_input_consumption_time]
timestamp
about.labels[timestamp]
(deprecated)
timestamp
additional.fields[timestamp]
updatedAt
about.labels[updatedAt]
(deprecated)
updatedAt
additional.fields[updatedAt]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
