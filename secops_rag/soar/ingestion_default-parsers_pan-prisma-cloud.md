# Collect Palo Alto Prisma Cloud logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-cloud/  
**Scraped:** 2026-03-05T09:59:08.017574Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Prisma Cloud logs
Supported in:
Google secops
SIEM
This document describes how you can collect Palo Alto Prisma Cloud logs by setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
PAN_PRISMA_CLOUD
ingestion label.
Configure Palo Alto Prisma Cloud
Sign in to the
Palo Alto Prisma Cloud Console
with an administrator account.
In the
Settings
menu, click
Access Keys
.
Click
Add New
and enter a
Name
.
Click
Create
. The
Access Key ID
and
Secret Key
values appear.
Save the
Access Key ID
and
Secret Key
values. These values are required when you configure the Google Security Operations feed.
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
Palo Alto Prisma Cloud Logs
.
Select
Third party API
as the
Source Type
.
Select
Palo Alto Prisma Cloud
as the
Log Type
.
Click
Next
.
Configure the following mandatory input parameters:
Username
: specify the access key ID that you obtained previously.
Password:
specify the secret key that you obtained previously.
API hostname
: specify the API hostname.
Click
Next
and then click
Submit
.
Field mapping reference
This parser code extracts fields from JSON formatted PAN PRISMA CLOUD logs, performs data transformations and mappings to structure the data into the Chronicle UDM schema. It handles various log message structures, including nested objects and arrays, to normalize diverse security events and contextual information for analysis within Chronicle.
UDM Mapping Table
Log Field
UDM Mapping
Logic
accountName
read_only_udm.target.resource.attribute.cloud.project.id
Directly mapped from
accountName
field.
accountId
read_only_udm.target.hostname
Directly mapped from
accountId
field.
accountId
read_only_udm.target.asset.hostname
Directly mapped from
accountId
field.
accountId
read_only_udm.principal.cloud.project.id
Directly mapped from
accountId
field in the
aggregatedAlerts
array.
action
read_only_udm.security_result.description
Directly mapped from
action
field after removing JSON part.
alertId
read_only_udm.metadata.product_log_id
Directly mapped from
alertId
field.
alertRules.0.allowAutoRemediate
read_only_udm.security_result.detection_fields.allowAutoRemediate_0
Directly mapped from
alertRules.0.allowAutoRemediate
field.
alertRules.0.enabled
read_only_udm.security_result.detection_fields.enabled_0
Directly mapped from
alertRules.0.enabled
field.
alertRules.0.name
read_only_udm.security_result.detection_fields.name_0
Directly mapped from
alertRules.0.name
field.
alertRules.0.notifyOnDismissed
read_only_udm.security_result.detection_fields.notifyOnDismissed_0
Directly mapped from
alertRules.0.notifyOnDismissed
field.
alertRules.0.notifyOnOpen
read_only_udm.security_result.detection_fields.notifyOnOpen_0
Directly mapped from
alertRules.0.notifyOnOpen
field.
alertRules.0.notifyOnResolved
read_only_udm.security_result.detection_fields.notifyOnResolved_0
Directly mapped from
alertRules.0.notifyOnResolved
field.
alertRules.0.notifyOnSnoozed
read_only_udm.security_result.detection_fields.notifyOnSnoozed_0
Directly mapped from
alertRules.0.notifyOnSnoozed
field.
alertRules.0.policyScanConfigId
read_only_udm.security_result.detection_fields.policyScanConfigId_0
Directly mapped from
alertRules.0.policyScanConfigId
field.
alertRules.0.scanAll
read_only_udm.security_result.detection_fields.scanAll_0
Directly mapped from
alertRules.0.scanAll
field.
alertRules.1.allowAutoRemediate
read_only_udm.security_result.detection_fields.allowAutoRemediate_1
Directly mapped from
alertRules.1.allowAutoRemediate
field.
alertRules.1.createdBy
read_only_udm.principal.user.email_addresses
Directly mapped from
alertRules.1.createdBy
field.
alertRules.1.enabled
read_only_udm.security_result.detection_fields.enabled_1
Directly mapped from
alertRules.1.enabled
field.
alertRules.1.name
read_only_udm.security_result.detection_fields.name_1
Directly mapped from
alertRules.1.name
field.
alertRules.1.notifyOnDismissed
read_only_udm.security_result.detection_fields.notifyOnDismissed_1
Directly mapped from
alertRules.1.notifyOnDismissed
field.
alertRules.1.notifyOnOpen
read_only_udm.security_result.detection_fields.notifyOnOpen_1
Directly mapped from
alertRules.1.notifyOnOpen
field.
alertRules.1.notifyOnResolved
read_only_udm.security_result.detection_fields.notifyOnResolved_1
Directly mapped from
alertRules.1.notifyOnResolved
field.
alertRules.1.notifyOnSnoozed
read_only_udm.security_result.detection_fields.notifyOnSnoozed_1
Directly mapped from
alertRules.1.notifyOnSnoozed
field.
alertRules.1.policyScanConfigId
read_only_udm.security_result.detection_fields.policyScanConfigId_1
Directly mapped from
alertRules.1.policyScanConfigId
field.
alertRules.1.scanAll
read_only_udm.security_result.detection_fields.scanAll_1
Directly mapped from
alertRules.1.scanAll
field.
alertRules.2.allowAutoRemediate
read_only_udm.security_result.detection_fields.allowAutoRemediate_2
Directly mapped from
alertRules.2.allowAutoRemediate
field.
alertRules.2.createdBy
read_only_udm.principal.user.email_addresses
Directly mapped from
alertRules.2.createdBy
field.
alertRules.2.enabled
read_only_udm.security_result.detection_fields.enabled_2
Directly mapped from
alertRules.2.enabled
field.
alertRules.2.name
read_only_udm.security_result.detection_fields.name_2
Directly mapped from
alertRules.2.name
field.
alertRules.2.notifyOnDismissed
read_only_udm.security_result.detection_fields.notifyOnDismissed_2
Directly mapped from
alertRules.2.notifyOnDismissed
field.
alertRules.2.notifyOnOpen
read_only_udm.security_result.detection_fields.notifyOnOpen_2
Directly mapped from
alertRules.2.notifyOnOpen
field.
alertRules.2.notifyOnResolved
read_only_udm.security_result.detection_fields.notifyOnResolved_2
Directly mapped from
alertRules.2.notifyOnResolved
field.
alertRules.2.notifyOnSnoozed
read_only_udm.security_result.detection_fields.notifyOnSnoozed_2
Directly mapped from
alertRules.2.notifyOnSnoozed
field.
alertRules.2.policyScanConfigId
read_only_udm.security_result.detection_fields.policyScanConfigId_2
Directly mapped from
alertRules.2.policyScanConfigId
field.
alertRules.2.scanAll
read_only_udm.security_result.detection_fields.scanAll_2
Directly mapped from
alertRules.2.scanAll
field.
alertRuleId
read_only_udm.security_result.rule_id
Directly mapped from
alertRuleId
field.
alertRuleName
read_only_udm.security_result.rule_name
Directly mapped from
alertRuleName
field.
alertStatus
read_only_udm.security_result.detection_fields.event message alertStatus
Directly mapped from
alertStatus
field in the
event_data.msg_data
object.
alertTs
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from
alertTs
field after converting to UNIX timestamp.
alertTs
read_only_udm.metadata.event_timestamp.nanos
Directly mapped from
alertTs
field after converting to UNIX timestamp.
callbackUrl
read_only_udm.metadata.url_back_to_product
Directly mapped from
callbackUrl
field.
cloudServiceName
read_only_udm.target.resource.attribute.labels.cloudServiceName
Directly mapped from
cloudServiceName
field.
cloudType
read_only_udm.target.resource.attribute.cloud.environment
Mapped from
cloudType
field. If
cloudType
is "gcp", the value is set to "GOOGLE_CLOUD_PLATFORM". If
cloudType
is "aws", the value is set to "AMAZON_WEB_SERVICES".
complianceMetadata.0.requirementId
read_only_udm.security_result.rule_id
Directly mapped from
complianceMetadata.0.requirementId
field.
complianceMetadata.0.requirementName
read_only_udm.security_result.summary
Directly mapped from
complianceMetadata.0.requirementName
field.
complianceMetadata.0.standardName
read_only_udm.security_result.rule_name
Directly mapped from
complianceMetadata.0.standardName
field.
complianceMetadata.1.requirementId
read_only_udm.security_result.rule_id
Directly mapped from
complianceMetadata.1.requirementId
field.
complianceMetadata.1.requirementName
read_only_udm.security_result.summary
Directly mapped from
complianceMetadata.1.requirementName
field.
complianceMetadata.1.standardName
read_only_udm.security_result.rule_name
Directly mapped from
complianceMetadata.1.standardName
field.
complianceMetadata.2.requirementId
read_only_udm.security_result.rule_id
Directly mapped from
complianceMetadata.2.requirementId
field.
complianceMetadata.2.requirementName
read_only_udm.security_result.summary
Directly mapped from
complianceMetadata.2.requirementName
field.
complianceMetadata.2.standardName
read_only_udm.security_result.rule_name
Directly mapped from
complianceMetadata.2.standardName
field.
complianceMetadata.3.requirementId
read_only_udm.security_result.rule_id
Directly mapped from
complianceMetadata.3.requirementId
field.
complianceMetadata.3.requirementName
read_only_udm.security_result.summary
Directly mapped from
complianceMetadata.3.requirementName
field.
complianceMetadata.3.standardName
read_only_udm.security_result.rule_name
Directly mapped from
complianceMetadata.3.standardName
field.
complianceMetadata.4.requirementId
read_only_udm.security_result.rule_id
Directly mapped from
complianceMetadata.4.requirementId
field.
complianceMetadata.4.requirementName
read_only_udm.security_result.summary
Directly mapped from
complianceMetadata.4.requirementName
field.
complianceMetadata.4.standardName
read_only_udm.security_result.rule_name
Directly mapped from
complianceMetadata.4.standardName
field.
event_data.app
read_only_udm.target.application
Directly mapped from
event_data.app
field.
event_data.msg_data.account.cloudType
read_only_udm.target.resource.attribute.cloud.environment
Mapped from
event_data.msg_data.account.cloudType
field. If the value is "aws", it is set to "AMAZON_WEB_SERVICES".
event_data.msg_data.account.id
read_only_udm.target.cloud.project.id
Directly mapped from
event_data.msg_data.account.id
field.
event_data.msg_data.account.name
read_only_udm.target.cloud.project.name
Directly mapped from
event_data.msg_data.account.name
field.
event_data.msg_data.accountIDs
read_only_udm.principal.resource.attribute.labels.event message accountId {index}
Directly mapped from
event_data.msg_data.accountIDs
array.
event_data.msg_data.aggregatedAlerts.0.category
read_only_udm.security_result.category_details
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.category
field.
event_data.msg_data.aggregatedAlerts.0.command
read_only_udm.principal.process.command_line
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.command
field.
event_data.msg_data.aggregatedAlerts.0.collections
read_only_udm.target.resource.attribute.labels.Collection {index}
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.collections
array.
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.category
read_only_udm.security_result.category_details
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.category
field.
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.description
read_only_udm.security_result.description
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.description
field.
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.severity
read_only_udm.security_result.severity
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.severity
field after converting to uppercase.
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.title
read_only_udm.security_result.action_details
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.complianceIssues.0.title
field.
event_data.msg_data.aggregatedAlerts.0.container
read_only_udm.target.resource.name
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.container
field.
event_data.msg_data.aggregatedAlerts.0.containerID
read_only_udm.target.resource.product_object_id
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.containerID
field.
event_data.msg_data.aggregatedAlerts.0.fqdn
read_only_udm.principal.domain.name
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.fqdn
field.
event_data.msg_data.aggregatedAlerts.0.host
read_only_udm.principal.hostname
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.host
field.
event_data.msg_data.aggregatedAlerts.0.host
read_only_udm.principal.asset.hostname
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.host
field.
event_data.msg_data.aggregatedAlerts.0.image
read_only_udm.target.resource.attribute.labels.image
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.image
field.
event_data.msg_data.aggregatedAlerts.0.imageID
read_only_udm.target.resource.attribute.labels.imageID
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.imageID
field.
event_data.msg_data.aggregatedAlerts.0.labels.controller-uid
read_only_udm.target.user.product_object_id
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.labels.controller-uid
field.
event_data.msg_data.aggregatedAlerts.0.labels.io.kubernetes.pod.name
read_only_udm.target.hostname
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.labels.io.kubernetes.pod.name
field.
event_data.msg_data.aggregatedAlerts.0.labels.io.kubernetes.pod.uid
read_only_udm.target.resource.product_object_id
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.labels.io.kubernetes.pod.uid
field.
event_data.msg_data.aggregatedAlerts.0.msg_data
read_only_udm.security_result.description
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.msg_data
field.
event_data.msg_data.aggregatedAlerts.0.rule
read_only_udm.security_result.rule_name
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.rule
field.
event_data.msg_data.aggregatedAlerts.0.startupProcess
read_only_udm.principal.application
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.startupProcess
field.
event_data.msg_data.aggregatedAlerts.0.time
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.time
field after converting to UNIX timestamp.
event_data.msg_data.aggregatedAlerts.0.time
read_only_udm.metadata.event_timestamp.nanos
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.time
field after converting to UNIX timestamp.
event_data.msg_data.aggregatedAlerts.0.type
read_only_udm.security_result.category_details
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.type
field.
event_data.msg_data.aggregatedAlerts.0.user
read_only_udm.principal.user.userid
Directly mapped from
event_data.msg_data.aggregatedAlerts.0.user
field.
event_data.msg_data.alertId
read_only_udm.security_result.detection_fields.event message alertId
Directly mapped from
event_data.msg_data.alertId
field.
event_data.msg_data.alertRuleId
read_only_udm.security_result.rule_id
Directly mapped from
event_data.msg_data.alertRuleId
field.
event_data.msg_data.alertRuleName
read_only_udm.security_result.rule_name
Directly mapped from
event_data.msg_data.alertRuleName
field.
event_data.msg_data.alertStatus
read_only_udm.security_result.detection_fields.event message alertStatus
Directly mapped from
event_data.msg_data.alertStatus
field.
event_data.msg_data.alertTs
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from
event_data.msg_data.alertTs
field after converting to UNIX timestamp.
event_data.msg_data.alertTs
read_only_udm.metadata.event_timestamp.nanos
Directly mapped from
event_data.msg_data.alertTs
field after converting to UNIX timestamp.
event_data.msg_data.category
read_only_udm.security_result.category_details
Directly mapped from
event_data.msg_data.category
field.
event_data.msg_data.collections
read_only_udm.target.resource.attribute.labels.Collection {index}
Directly mapped from
event_data.msg_data.collections
array.
event_data.msg_data.command
read_only_udm.principal.process.command_line
Directly mapped from
event_data.msg_data.command
field.
event_data.msg_data.complianceIssues.0.category
read_only_udm.security_result.category_details
Directly mapped from
event_data.msg_data.complianceIssues.0.category
field.
event_data.msg_data.complianceIssues.0.description
read_only_udm.security_result.description
Directly mapped from
event_data.msg_data.complianceIssues.0.description
field.
event_data.msg_data.complianceIssues.0.severity
read_only_udm.security_result.severity
Directly mapped from
event_data.msg_data.complianceIssues.0.severity
field after converting to uppercase.
event_data.msg_data.complianceIssues.0.title
read_only_udm.security_result.action_details
Directly mapped from
event_data.msg_data.complianceIssues.0.title
field.
event_data.msg_data.container
read_only_udm.target.resource.name
Directly mapped from
event_data.msg_data.container
field.
event_data.msg_data.containerID
read_only_udm.target.resource.product_object_id
Directly mapped from
event_data.msg_data.containerID
field.
event_data.msg_data.dropped
read_only_udm.security_result.detection_fields.dropped
Directly mapped from
event_data.msg_data.dropped
field after converting to string.
event_data.msg_data.fqdn
read_only_udm.principal.domain.name
Directly mapped from
event_data.msg_data.fqdn
field.
event_data.msg_data.firstSeen
read_only_udm.security_result.first_discovered_time.seconds
Directly mapped from
event_data.msg_data.firstSeen
field after converting to UNIX timestamp.
event_data.msg_data.firstSeen
read_only_udm.security_result.first_discovered_time.nanos
Directly mapped from
event_data.msg_data.firstSeen
field after converting to UNIX timestamp.
event_data.msg_data.host
read_only_udm.principal.hostname
Directly mapped from
event_data.msg_data.host
field.
event_data.msg_data.host
read_only_udm.principal.asset.hostname
Directly mapped from
event_data.msg_data.host
field.
event_data.msg_data.image
read_only_udm.target.resource.attribute.labels.image
Directly mapped from
event_data.msg_data.image
field.
event_data.msg_data.imageID
read_only_udm.target.resource.attribute.labels.imageID
Directly mapped from
event_data.msg_data.imageID
field.
event_data.msg_data.labels.controller-uid
read_only_udm.target.user.product_object_id
Directly mapped from
event_data.msg_data.labels.controller-uid
field.
event_data.msg_data.labels.io.kubernetes.pod.name
read_only_udm.target.hostname
Directly mapped from
event_data.msg_data.labels.io.kubernetes.pod.name
field.
event_data.msg_data.labels.io.kubernetes.pod.uid
read_only_udm.target.resource.product_object_id
Directly mapped from
event_data.msg_data.labels.io.kubernetes.pod.uid
field.
event_data.msg_data.lastSeen
read_only_udm.security_result.last_discovered_time.seconds
Directly mapped from
event_data.msg_data.lastSeen
field after converting to UNIX timestamp.
event_data.msg_data.lastSeen
read_only_udm.security_result.last_discovered_time.nanos
Directly mapped from
event_data.msg_data.lastSeen
field after converting to UNIX timestamp.
event_data.msg_data.metadata.cveCritical
read_only_udm.security_result.detection_fields.event_data metadata cveCritical
Directly mapped from
event_data.msg_data.metadata.cveCritical
field.
event_data.msg_data.metadata.cveHigh
read_only_udm.security_result.detection_fields.event_data metadata cveHigh
Directly mapped from
event_data.msg_data.metadata.cveHigh
field.
event_data.msg_data.metadata.cveLow
read_only_udm.security_result.detection_fields.event_data metadata cveLow
Directly mapped from
event_data.msg_data.metadata.cveLow
field.
event_data.msg_data.metadata.cveMedium
read_only_udm.security_result.detection_fields.event_data metadata cveMedium
Directly mapped from
event_data.msg_data.metadata.cveMedium
field.
event_data.msg_data.metadata.source
read_only_udm.principal.hostname
Directly mapped from
event_data.msg_data.metadata.source
field.
event_data.msg_data.metadata.source
read_only_udm.principal.asset.hostname
Directly mapped from
event_data.msg_data.metadata.source
field.
event_data.msg_data.msg_data
read_only_udm.security_result.description
Directly mapped from
event_data.msg_data.msg_data
field.
event_data.msg_data.policy.description
read_only_udm.security_result.description
Directly mapped from
event_data.msg_data.policy.description
field.
event_data.msg_data.policy.id
read_only_udm.security_result.detection_fields.policy_id
Directly mapped from
event_data.msg_data.policy.id
field.
event_data.msg_data.policy.name
read_only_udm.security_result.summary
Directly mapped from
event_data.msg_data.policy.name
field.
event_data.msg_data.policy.policyTs
read_only_udm.additional.fields.policy_ts
Directly mapped from
event_data.msg_data.policy.policyTs
field.
event_data.msg_data.policy.policyType
read_only_udm.security_result.threat_name
Directly mapped from
event_data.msg_data.policy.policyType
field.
event_data.msg_data.policy.recommendation
read_only_udm.security_result.action_details
Directly mapped from
event_data.msg_data.policy.recommendation
field.
event_data.msg_data.policy.severity
read_only_udm.security_result.severity
Directly mapped from
event_data.msg_data.policy.severity
field after converting to uppercase.
event_data.msg_data.reason
read_only_udm.security_result.detection_fields.event message reason
Directly mapped from
event_data.msg_data.reason
field.
event_data.msg_data.region
read_only_udm.target.cloud.availability_zone
Directly mapped from
event_data.msg_data.region
field.
event_data.msg_data.resource.resourceId
read_only_udm.target.resource.product_object_id
Directly mapped from
event_data.msg_data.resource.resourceId
field.
event_data.msg_data.resource.resourceName
read_only_udm.target.resource.name
Directly mapped from
event_data.msg_data.resource.resourceName
field.
event_data.msg_data.resource.resourceTs
read_only_udm.target.resource.attribute.creation_time.seconds
Directly mapped from
event_data.msg_data.resource.resourceTs
field after converting to UNIX timestamp.
event_data.msg_data.resource.resourceTs
read_only_udm.target.resource.attribute.creation_time.nanos
Directly mapped from
event_data.msg_data.resource.resourceTs
field after converting to UNIX timestamp.
event_data.msg_data.rule
read_only_udm.security_result.rule_name
Directly mapped from
event_data.msg_data.rule
field.
event_data.msg_data.service
read_only_udm.security_result.detection_fields.event message service
Directly mapped from
event_data.msg_data.service
field.
event_data.msg_data.startupProcess
read_only_udm.principal.application
Directly mapped from
event_data.msg_data.startupProcess
field.
event_data.msg_data.time
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from
event_data.msg_data.time
field after converting to UNIX timestamp.
event_data.msg_data.time
read_only_udm.metadata.event_timestamp.nanos
Directly mapped from
event_data.msg_data.time
field after converting to UNIX timestamp.
event_data.msg_data.type
read_only_udm.security_result.category_details
Directly mapped from
event_data.msg_data.type
field.
event_data.sentTs
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from
event_data.sentTs
field after converting to UNIX timestamp.
event_data.sentTs
read_only_udm.metadata.event_timestamp.nanos
Directly mapped from
event_data.sentTs
field after converting to UNIX timestamp.
event_data.type
read_only_udm.security_result.category_details
Directly mapped from
event_data.type
field.
ipAddress
read_only_udm.principal.ip
Directly mapped from
ipAddress
field after extracting IP address using grok.
ipAddress
read_only_udm.principal.asset.ip
Directly mapped from
ipAddress
field after extracting IP address using grok.
ipAddress
read_only_udm.additional.fields.ipAddress
Directly mapped from
ipAddress
field if it is not a valid IP address.
json_action.0.policy_id
read_only_udm.target.resource.attribute.labels.Policy Id 0
Directly mapped from
json_action.0.policy_id
field.
json_action.0.resource_name
read_only_udm.target.resource.attribute.labels.Resource Name 0
Directly mapped from
json_action.0.resource_name
field.
json_action.1.policy_id
read_only_udm.target.resource.attribute.labels.Policy Id 1
Directly mapped from
json_action.1.policy_id
field.
json_action.1.resource_name
read_only_udm.target.resource.attribute.labels.Resource Name 1
Directly mapped from
json_action.1.resource_name
field.
policy.policyId
read_only_udm.security_result.rule_id
Directly mapped from
policy.policyId
field.
policy.policyType
read_only_udm.security_result.rule_type
Directly mapped from
policy.policyType
field.
policy.recommendation
read_only_udm.metadata.description
Directly mapped from
policy.recommendation
field.
policy.severity
read_only_udm.security_result.severity
Mapped from
policy.severity
field. If the value is "info", it is set to "INFORMATIONAL".
policyName
read_only_udm.metadata.description
Directly mapped from
policyName
field.
reason
read_only_udm.metadata.product_event_type
Directly mapped from
reason
field.
resource.accountId
read_only_udm.target.resource.product_object_id
Directly mapped from
resource.accountId
field.
resource.cloudServiceName
read_only_udm.target.resource.attribute.labels.cloudServiceName
Directly mapped from
resource.cloudServiceName
field.
resource.data.architecture
read_only_udm.principal.asset.hardware.cpu_platform
Directly mapped from
resource.data.architecture
field.
resource.data.cpuPlatform
read_only_udm.additional.fields.CPU Platform
Directly mapped from
resource.data.cpuPlatform
field.
resource.data.labelFingerprint
read_only_udm.security_result.detection_fields.labelFingerprint
Directly mapped from
resource.data.labelFingerprint
field.
resource.data.metadata.items.key
read_only_udm.additional.fields.key
Directly mapped from
resource.data.metadata.items.key
field.
resource.data.metadata.items.value
read_only_udm.additional.fields.value.string_value
Directly mapped from
resource.data.metadata.items.value
field.
resource.data.networkInterfaces.0.accessConfigs.0.natIP
read_only_udm.target.nat_ip
Directly mapped from
resource.data.networkInterfaces.0.accessConfigs.0.natIP
field.
resource.data.networkInterfaces.0.networkIP
read_only_udm.target.ip
Directly mapped from
resource.data.networkInterfaces.0.networkIP
field.
resource.data.networkInterfaces.0.networkIP
read_only_udm.target.asset.ip
Directly mapped from
resource.data.networkInterfaces.0.networkIP
field.
resource.data.physicalBlockSizeBytes
read_only_udm.principal.resource.attribute.labels.physicalBlockSizeBytes
Directly mapped from
resource.data.physicalBlockSizeBytes
field after converting to string.
resource.data.selfLink
read_only_udm.about.url
Directly mapped from
resource.data.selfLink
field.
resource.data.serviceAccounts.0.email
read_only_udm.principal.user.email_addresses
Directly mapped from
resource.data.serviceAccounts.0.email
field.
resource.data.serviceAccounts.0.email
read_only_udm.principal.user.attribute.roles.type
If
resource.data.serviceAccounts.0.email
contains "serviceaccount", the value is set to "SERVICE_ACCOUNT".
resource.data.sizeGb
read_only_udm.principal.resource.attribute.labels.sizeGb
Directly mapped from
resource.data.sizeGb
field.
resource.data.sourceImage
read_only_udm.principal.resource.attribute.labels.sourceImage
Directly mapped from
resource.data.sourceImage
field.
resource.name
read_only_udm.target.resource.name
Directly mapped from
resource.name
field.
resource.regionId
read_only_udm.target.location.country_or_region
Directly mapped from `resource
Need more help?
Get answers from Community members and Google SecOps professionals.
