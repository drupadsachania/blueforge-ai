# Collect Palo Alto Prisma Cloud alert logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca/  
**Scraped:** 2026-03-05T09:59:09.397991Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Prisma Cloud alert logs
Supported in:
Google secops
SIEM
Overview
This parser extracts alert logs from Palo Alto Prisma Cloud in JSON format, transforming them into the UDM. The parser performs data normalization, type conversions, and conditional logic to populate the appropriate UDM fields. It also handles nested JSON structures and arrays within the log data to extract relevant information. The information in this document applies to the parser with the PAN_PRISMA_CA ingestion label.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Palo Alto Prisma Cloud.
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
field, enter a name for the feed; for example,
PAN Prisma Cloud Alerts
.
Select
Webhook
as the
Source type
.
Select
Palo Alto Prisma Cloud Alerts payload
as the
Log type
.
Click
Next
.
Optional: Specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
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
From the
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
: Specify the API key as a header instead of specifying it in the URL.
If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
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
Configure Palo Alto Prisma Cloud webhook to Google SecOps
Sign in to Palo Alto Prisma Cloud.
Select
Settings
>
Integrations & Notification
((and_then))
Integrations
.
Click
Add Integration
.
Select
Webhook
.
Specify values for the following input parameters:
Integration Name
: Provide a unique and descriptive name (for example,
Google SecOps
)
Webhook URL
: Enter the ENDPOINT_URL.
Optional: Provide a
Description
of the integration.
Optional: Enable
Custom Payload
>
click
Next
to review or revise the custom payload.
Click
Next
.
Test
and
Save Integration
.
Configure Palo Alto Prisma Cloud Alerts
In the Palo Alto Prisma Cloud console, go to
Alerts
>
View Alert Rules
.
Select an existing alert rule to edit.
Optional:
Create new Alert for
Cloud Infrastructure
.
Optional:
Create new Alert for
Cloud Workload
.
Go to
Configure Notifications
.
Select
Webhook
.
Optional: Select the Channels that you want to send notifications of alerts triggered by the alert rule.
Click
Next
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
accountId
target.resource.id
The value of
accountId
from the raw log.
accountId
target.resource.product_object_id
The value of
accountId
from the raw log. This overrides the deprecated
resource.id
field.
alertId
security_result.detection_fields[].key
The key is set to "alert id".
alertId
security_result.detection_fields[].value
The value of
alertId
from the raw log.
alertRuleId
security_result.rule_id
The value of
alertRuleId
from the raw log.
alertRuleName
security_result.rule_name
The value of
alertRuleName
from the raw log.
alertStatus
security_result.detection_fields[].key
The key is set to "alert status".
alertStatus
security_result.detection_fields[].value
The value of
alertStatus
from the raw log.
alertTs
security_result.detection_fields[].key
The key is set to "alertTs".
alertTs
security_result.detection_fields[].value
The value of
alertTs
from the raw log, converted to a string.
callbackUrl
metadata.url_back_to_product
The value of
callbackUrl
from the raw log.
cloudType
principal.cloud.environment
If
cloudType
is "gcp" (case-insensitive), the value is set to "GOOGLE_CLOUD_PLATFORM".
complianceMetadata[].complianceId
security_result.detection_fields[].key
The key is set to "complianceId".
complianceMetadata[].complianceId
security_result.detection_fields[].value
The value of
complianceMetadata[].complianceId
from the raw log.
complianceMetadata[].customAssigned
security_result.detection_fields[].key
The key is set to "customAssigned".
complianceMetadata[].customAssigned
security_result.detection_fields[].value
The value of
complianceMetadata[].customAssigned
from the raw log, converted to a string.
complianceMetadata[].policyId
security_result.detection_fields[].key
The key is set to "Policy Id".
complianceMetadata[].policyId
security_result.detection_fields[].value
The value of
complianceMetadata[].policyId
from the raw log.
complianceMetadata[].requirementId
security_result.rule_id
The value of
complianceMetadata[].requirementId
from the raw log.
complianceMetadata[].requirementName
security_result.summary
The value of
complianceMetadata[].requirementName
from the raw log.
complianceMetadata[].requirementViewOrder
security_result.detection_fields[].key
The key is set to "requirementViewOrder".
complianceMetadata[].requirementViewOrder
security_result.detection_fields[].value
The value of
complianceMetadata[].requirementViewOrder
from the raw log, converted to a string.
complianceMetadata[].sectionDescription
security_result.detection_fields[].key
The key is set to "sectionDescription".
complianceMetadata[].sectionDescription
security_result.detection_fields[].value
The value of
complianceMetadata[].sectionDescription
from the raw log.
complianceMetadata[].sectionId
security_result.detection_fields[].key
The key is set to "sectionId".
complianceMetadata[].sectionId
security_result.detection_fields[].value
The value of
complianceMetadata[].sectionId
from the raw log.
complianceMetadata[].sectionLabel
security_result.detection_fields[].key
The key is set to "sectionLabel".
complianceMetadata[].sectionLabel
security_result.detection_fields[].value
The value of
complianceMetadata[].sectionLabel
from the raw log.
complianceMetadata[].sectionViewOrder
security_result.detection_fields[].key
The key is set to "sectionViewOrder".
complianceMetadata[].sectionViewOrder
security_result.detection_fields[].value
The value of
complianceMetadata[].sectionViewOrder
from the raw log, converted to a string.
complianceMetadata[].standardDescription
security_result.detection_fields[].key
The key is set to "standardDescription".
complianceMetadata[].standardDescription
security_result.detection_fields[].value
The value of
complianceMetadata[].standardDescription
from the raw log.
complianceMetadata[].standardName
security_result.rule_name
The value of
complianceMetadata[].standardName
from the raw log.
complianceMetadata[].systemDefault
security_result.detection_fields[].key
The key is set to "systemDefault".
complianceMetadata[].systemDefault
security_result.detection_fields[].value
The value of
complianceMetadata[].systemDefault
from the raw log, converted to a string.
create_time
metadata.event_timestamp
,
events[].timestamp
The value of
create_time
from the raw log.
data.allocationId
principal.resource.product_object_id
The value of
data.allocationId
from the raw log.
data.publicIp
principal.ip
The value of
data.publicIp
from the raw log.
deleted
additional.fields[].key
The key is set to "deleted".
deleted
additional.fields[].value.string_value
The value of
deleted
from the raw log, converted to a string.
description
metadata.description
The value of
description
from the raw log.
firstSeen
principal.asset.first_seen_time
The value of
firstSeen
from the raw log, parsed as a timestamp (UNIX_MS or UNIX format).
hasFinding
security_result.detection_fields[].key
The key is set to "hasFinding".
hasFinding
security_result.detection_fields[].value
The value of
hasFinding
from the raw log, converted to a string.
lastSeen
principal.asset.last_discover_time
The value of
lastSeen
from the raw log, parsed as a timestamp (UNIX_MS or UNIX format).
N/A
metadata.event_type
Set to "USER_RESOURCE_ACCESS" if not overridden by a specific event type from the log. Otherwise set to "GENERIC_EVENT".
N/A
metadata.product_name
Hardcoded to "CASB".
N/A
metadata.vendor_name
Hardcoded to "Palo Alto Networks".
policyDescription
security_result.detection_fields[].key
The key is set to "policyDescription".
policyDescription
security_result.detection_fields[].value
The value of
policyDescription
from the raw log.
policyId
security_result.detection_fields[].key
The key is set to "Policy Id".
policyId
security_result.detection_fields[].value
The value of
policyId
from the raw log.
policyLabels
additional.fields[].key
The key is set to "policyLabels".
policyLabels
additional.fields[].value.string_value
The value of
policyLabels
from the raw log.
policyName
security_result.description
The value of
policyName
from the raw log.
policyRecommendation
security_result.detection_fields[].key
The key is set to "policy recommendation".
policyRecommendation
security_result.detection_fields[].value
The value of
policyRecommendation
from the raw log.
policyType
security_result.detection_fields[].key
The key is set to "Policy Type".
policyType
security_result.detection_fields[].value
The value of
policyType
from the raw log.
reason
security_result.summary
The value of
reason
from the raw log.
recommendation
security_result.detection_fields[].key
The key is set to "Recommendation".
recommendation
security_result.detection_fields[].value
The value of
recommendation
from the raw log.
resource.additionalInfo
principal.resource.attribute.labels[].key
The key is set to "resource additionalInfo".
resource.additionalInfo
principal.resource.attribute.labels[].value
The value of
resource.additionalInfo
from the raw log.
resource.cloudAccountGroups
principal.resource.attribute.labels[].key
The key is set to "resource cloudAccountGroups {index}".
resource.cloudAccountGroups
principal.resource.attribute.labels[].value
The value of
resource.cloudAccountGroups[]
from the raw log.
resource.cloudType
principal.resource.attribute.labels[].key
The key is set to "resource cloudType".
resource.cloudType
principal.resource.attribute.labels[].value
The value of
resource.cloudType
from the raw log.
resource.data
principal.resource.attribute.labels[].key
The key is set to "resource data {nested_key}".
resource.data
principal.resource.attribute.labels[].value
The value of
resource.data[]
from the raw log.
resource.id
principal.resource.product_object_id
The value of
resource.id
from the raw log.
resource.name
principal.resource.name
The value of
resource.name
from the raw log.
resource.region
principal.location.country_or_region
The value of
resource.region
from the raw log.
resource.regionId
principal.cloud.availability_zone
The value of
resource.regionId
from the raw log.
resource.resourceApiName
principal.resource.attribute.labels[].key
The key is set to "resource resourceApiName".
resource.resourceApiName
principal.resource.attribute.labels[].value
The value of
resource.resourceApiName
from the raw log.
resource.resourceTags
principal.resource.attribute.labels[].key
The key is set to "resource resourceTags {nested_key}".
resource.resourceTags
principal.resource.attribute.labels[].value
The value of
resource.resourceTags[]
from the raw log.
resource.resourceTs
principal.resource.attribute.labels[].key
The key is set to "resource resourceTs".
resource.resourceTs
principal.resource.attribute.labels[].value
The value of
resource.resourceTs
from the raw log.
resource.resourceType
principal.resource.attribute.labels[].key
The key is set to "resource resourceType".
resource.resourceType
principal.resource.attribute.labels[].value
The value of
resource.resourceType
from the raw log.
resource.rrn
principal.resource.attribute.labels[].key
The key is set to "resource rrn".
resource.rrn
principal.resource.attribute.labels[].value
The value of
resource.rrn
from the raw log.
resource.url
principal.url
The value of
resource.url
from the raw log.
resourceCloudService
principal.resource.attribute.labels[].key
The key is set to "resource cloud service".
resourceCloudService
principal.resource.attribute.labels[].value
The value of
resourceCloudService
from the raw log.
resourceName
principal.resource.name
The value of
resourceName
from the raw log.
resourceRegion
principal.location.country_or_region
The value of
resourceRegion
from the raw log.
resourceRegionId
principal.cloud.availability_zone
The value of
resourceRegionId
from the raw log.
resourceType
target.resource.resource_subtype
The value of
resourceType
from the raw log.
severity
security_result.severity
The value of
severity
from the raw log, converted to uppercase. Mapped to UDM severity values (CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL).
source
principal.application
The value of
source
from the raw log.
unifiedAssetId
principal.asset.asset_id
The value of
unifiedAssetId
from the raw log, prefixed with "ASSETID:".
Need more help?
Get answers from Community members and Google SecOps professionals.
