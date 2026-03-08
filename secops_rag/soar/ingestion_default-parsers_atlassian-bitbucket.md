# Collect Atlassian Bitbucket logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-bitbucket/  
**Scraped:** 2026-03-05T09:50:10.396503Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Atlassian Bitbucket logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Atlassian Bitbucket JSON logs and maps them to the UDM. It handles various log formats, populates principal or target entities based on available fields like IP addresses, user IDs, and asset information. It also categorizes events based on network and user activity and enriches the data with security findings, if present. The parser prioritizes
agentRealtimeInfo
over
agentDetectionInfo
when populating fields.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to a repository within.
Set up feeds
To configure a feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Atlassian Bitbucket Logs
).
Select
Webhook
as the
Source type
.
Select
Atlassian Bitbucket
as the
Log type
.
Click
Next
.
Optional: specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label applied to the events from this feed.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
On the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. You need to specify this endpoint URL in your client application.
Click
Done
.
Create an API key for the webhook feed
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
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Create a webhook in Atlassian Bitbucket
In Bitbucket, go to the repository settings.
Click
Webhooks
under
Workflow
.
Click
Add webhook
.
Configure the following fields:
Title
: Provide a descriptive name (For example,
Google SecOps
).
URL
: Enter the Google SecOps API endpoint URL.
Status
: Set to
Active
.
Triggers
: Select the relevant events.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
agentComputerName
principal.hostname
Populated from
agentRealtimeInfo.agentComputerName
.
agentDetectionInfo.accountId
metadata.product_deployment_id
Converted to string. Used if
agentRealtimeInfo.accountId
is not present.
agentDetectionInfo.accountName
metadata.product_name
Used if
agentRealtimeInfo.accountName
is not present.
agentDetectionInfo.agentDomain
principal.administrative_domain
Directly mapped.
agentDetectionInfo.agentIpV4
target.ip
Extracted from JSON array and merged into the
target.ip
field.
agentDetectionInfo.agentIpV6
principal.ip
Extracted from JSON array and merged into the
principal.ip
field.
agentDetectionInfo.agentLastLoggedInUserName
principal.user.userid
Parsed to extract userid and domain (if present). If no domain, directly mapped to
principal.user.userid
.
agentDetectionInfo.agentOsName
principal.platform_version
,
principal.asset.platform_software.platform_version
Used if
agentRealtimeInfo.agentOsName
is not present.
agentDetectionInfo.agentOsRevision
principal.platform_patch_level
,
principal.asset.platform_software.platform_patch_level
Used if
agentRealtimeInfo.agentOsRevision
is not present.
agentDetectionInfo.agentRegisteredAt
principal.asset.first_discover_time
Parsed as an ISO8601 timestamp.
agentDetectionInfo.agentUuid
principal.asset_id
,
principal.asset.asset_id
Used if
agentRealtimeInfo.agentUuid
is not present.  Prefixed with "agentUuid:".
agentDetectionInfo.agentVersion
metadata.product_version
Used if
agentRealtimeInfo.agentVersion
is not present.
agentDetectionInfo.externalIp
target.ip
Directly mapped.
agentDetectionInfo.groupId
principal.user.group_identifiers
Merged into the field if not empty or "-". Used if
agentRealtimeInfo.groupId
is not present.
agentDetectionInfo.groupName
principal.group.group_display_name
Used if
agentRealtimeInfo.groupName
is not present.
agentDetectionInfo.siteId
additional.fields
Added as a key-value pair with key "agentDetectionInfo.siteId". Used if
agentRealtimeInfo.siteId
is not present.
agentDetectionInfo.siteName
additional.fields
Added as a key-value pair with key "agentDetectionInfo.siteName". Used if
agentRealtimeInfo.siteName
is not present.
agentRealtimeInfo.accountId
metadata.product_deployment_id
Converted to string.
agentRealtimeInfo.accountName
metadata.product_name
Directly mapped.
agentRealtimeInfo.agentComputerName
principal.hostname
,
principal.asset.hostname
Directly mapped.
agentRealtimeInfo.agentId
principal.asset_id
,
principal.asset.asset_id
Prefixed with "agentId:".
agentRealtimeInfo.agentMachineType
principal.asset.category
Directly mapped.
agentRealtimeInfo.agentOsName
principal.platform_version
,
principal.asset.platform_software.platform_version
Directly mapped.
agentRealtimeInfo.agentOsRevision
principal.platform_patch_level
,
principal.asset.platform_software.platform_patch_level
Directly mapped.
agentRealtimeInfo.agentOsType
principal.asset.platform_software.platform
,
principal.platform
Mapped to WINDOWS, MAC, or LINUX based on the value.
agentRealtimeInfo.agentUuid
principal.asset_id
,
principal.asset.asset_id
Directly mapped. Prefixed with "agentUuid:".
agentRealtimeInfo.agentVersion
metadata.product_version
Directly mapped.
agentRealtimeInfo.groupId
principal.user.group_identifiers
Merged into the field if not empty or "-".
agentRealtimeInfo.groupName
principal.group.group_display_name
Directly mapped.
agentRealtimeInfo.siteId
additional.fields
Added as a key-value pair with key "agentDetectionInfo.siteId".
agentRealtimeInfo.siteName
additional.fields
Added as a key-value pair with key "agentDetectionInfo.siteName".
associatedItems.0.id
principal.resource.id
Directly mapped.
associatedItems.0.name
principal.resource.name
Directly mapped.
associatedItems.0.typeName
principal.resource.resource_subtype
Directly mapped.
authorAccountId
principal.user.userid
Directly mapped.
category
metadata.product_event_type
Directly mapped. If not present and message contains "threats", set to "Threats".
id
metadata.product_log_id
Converted to string.
indicators.0.description
security_result.description
Directly mapped.
objectItem.id
additional.fields
Added as a key-value pair with key "objectItem.id".
objectItem.name
additional.fields
Added as a key-value pair with key "objectItem.name".
objectItem.typeName
additional.fields
Added as a key-value pair with key "objectItem.typeName".
remoteAddress
principal.ip
Directly mapped.
summary
security_result.summary
Directly mapped.
threatInfo.classification
security_result.category_details
Directly mapped. Also used to determine
security_result.category
.
threatInfo.collectionId
metadata.ingestion_labels
Added as a key-value pair with key "alert_aggregation_value".
threatInfo.confidenceLevel
security_result.confidence_details
Directly mapped. Also used to determine
security_result.confidence
.
threatInfo.createdAt
metadata.collected_timestamp
Parsed as an ISO8601 timestamp.
threatInfo.detectionEngines
metadata.ingestion_labels
Each element's
key
and
title
are added as key-value pairs.
threatInfo.fileExtensionType
target.process.file.mime_type
Directly mapped.
threatInfo.filePath
target.file.full_path
Directly mapped.
threatInfo.fileSize
target.file.size
Converted to string then to unsigned integer.
threatInfo.identifiedAt
event_timestamp
Parsed as an ISO8601 timestamp.
threatInfo.maliciousProcessArguments
principal.process.command_line
Directly mapped. Also used in the
security_result.summary
field if
summary
is not present.
threatInfo.md5
target.file.md5
Directly mapped.
threatInfo.originatorProcess
target.process.parent_process.file.full_path
Directly mapped. Also used in the
security_result.summary
field if
summary
is not present.
threatInfo.processUser
target.user.userid
Directly mapped.
threatInfo.sha1
target.file.sha1
Directly mapped.
threatInfo.sha256
target.file.sha256
Directly mapped.
threatInfo.storyline
principal.process.product_specific_process_id
Prefixed with "ID:".
threatInfo.threatId
security_result.threat_id
Directly mapped.
threatInfo.threatName
security_result.threat_name
,
target.file.names
Directly mapped and merged into
target.file.names
. Also used in the
security_result.summary
field if
summary
is not present. Set to "GENERIC_EVENT" initially. Changed to "NETWORK_UNCATEGORIZED", "STATUS_UPDATE", or "USER_UNCATEGORIZED" based on the presence of principal and target IP/hostname/user. Copied from the
event.type
field. Set to "Atlassian Bitbucket". Set to "Atlassian Bitbucket" initially. Can be overridden by
agentRealtimeInfo.accountName
or
agentDetectionInfo.accountName
.
timestamp
metadata.event_timestamp
,
timestamp
Directly mapped.
Need more help?
Get answers from Community members and Google SecOps professionals.
