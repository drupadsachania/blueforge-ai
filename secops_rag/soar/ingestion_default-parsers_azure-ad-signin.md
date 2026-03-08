# Collect Azure AD Sign-In logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin/  
**Scraped:** 2026-03-05T09:50:56.952077Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure AD Sign-In logs
Supported in:
Google secops
SIEM
This document explains how to export Azure AD Sign-In logs to Google Security Operations using an Azure Storage Account. The parser takes raw logs in JSON format and transforms them into a structured format compliant with the Unified Data Model (UDM). It extracts relevant fields, normalizes values, handles different timestamps, and enriches the data with security-related context like user information, IP addresses, and conditional access policies.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
An active Azure tenant
Privileged access to Azure
Configure Azure Storage Account
In the Azure console, search for
Storage accounts
.
Click
+ Create
.
Specify values for the following input parameters:
Subscription
: Select the subscription.
Resource Group
: Select the resource group.
Region
: Select the region.
Performance
: Select the performance (Standard recommended).
Redundancy
: Select the redundancy (GRS or LRS recommended).
Storage account name
: Enter a name for the new storage account.
Click
Review + create
.
Review the overview of the account and click
Create
.
From the
Storage Account Overview
page, select the
Access keys
submenu in
Security + networking
.
Click
Show
next to
key1
or
key2
.
Click
Copy to clipboard
to copy the key.
Save the key in a secure location for later use.
From the
Storage Account Overview
page, select the
Endpoints
submenu in
Settings
.
Click
Copy to clipboard
to copy the
Blob service
endpoint URL; for example,
https://<storageaccountname>.blob.core.windows.net
.
Save the endpoint URL in a secure location for later use.
How to configure Log Export for Azure AD Sign-In Logs
Sign in to the
Azure Portal
using your privileged account.
Go to
Microsoft Entra ID
>
Monitoring
>
Diagnostic settings
.
Click
Add diagnostic setting
.
Enter a descriptive name for the diagnostic setting.
Select
Sign-in logs
.
Select the
Archive to a storage account
checkbox as the destination.
Specify the
Subscription
and
Storage Account
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
How to set up the Azure AD Sign-In feed
Click the
Azure Platform
pack.
Locate the
Azure AD Sign-In
log type.
Specify values for the following fields:
Source Type
: Microsoft Azure Blob Storage V2.
Azure URI
: The blob endpoint URL.
ENDPOINT_URL/BLOB_NAME
Replace the following:
ENDPOINT_URL
: The blob endpoint URL (
https://<storageaccountname>.blob.core.windows.net
)
BLOB_NAME
: The name of the blob (such as,
insights-logs-<logname>
)
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Files modified in the last number of days. Default is 180 days.
Shared key
: The access key to the Azure Blob Storage.
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
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
UDM Mapping Table
Log field
UDM mapping
Logic
AppDisplayName
read_only_udm.target.application
Directly mapped from the
AppDisplayName
field in the raw log.
AppId
read_only_udm.security_result.detection_fields.value
Directly mapped from the
AppId
field in the raw log. The key is set to
appId
.
Category
read_only_udm.security_result.category_details
Directly mapped from the
Category
field in the raw log.
ConditionalAccessPolicies[].displayName
read_only_udm.security_result.rule_name
Directly mapped from the
displayName
field within the
ConditionalAccessPolicies
array in the raw log.
ConditionalAccessPolicies[].enforcedGrantControls[]
read_only_udm.security_result.rule_labels.value
Directly mapped from the
enforcedGrantControls
array within the
ConditionalAccessPolicies
array in the raw log. The key is set to
applied_conditional_access_policies_enforced_grant_controls
.
ConditionalAccessPolicies[].enforcedSessionControls[]
read_only_udm.security_result.rule_labels.value
Directly mapped from the
enforcedSessionControls
array within the
ConditionalAccessPolicies
array in the raw log. The key is set to
applied_conditional_access_policies_enforced_session_controls
.
ConditionalAccessPolicies[].id
read_only_udm.security_result.rule_id
Directly mapped from the
id
field within the
ConditionalAccessPolicies
array in the raw log.
ConditionalAccessPolicies[].Result
read_only_udm.security_result.rule_labels.value
Directly mapped from the
Result
field within the
ConditionalAccessPolicies
array in the raw log. The key is set to
applied_conditional_access_policies_result
.
ConditionalAccessStatus
read_only_udm.additional.fields.value.string_value
Directly mapped from the
ConditionalAccessStatus
field in the raw log. The key is set to
conditionalAccessStatus
.
CorrelationId
read_only_udm.security_result.detection_fields.value
Directly mapped from the
CorrelationId
field in the raw log. The key is set to
correlationId
.
DurationMs
read_only_udm.additional.fields.value.string_value
Directly mapped from the
DurationMs
field in the raw log. The key is set to
durationMs
.
HomeTenantId
read_only_udm.security_result.detection_fields.value
Directly mapped from the
HomeTenantId
field in the raw log. The key is set to
HomeTenantId
.
IPAddress
read_only_udm.principal.asset.ip, read_only_udm.principal.ip
Directly mapped from the
IPAddress
field in the raw log.
Id
read_only_udm.security_result.detection_fields.value
Directly mapped from the
Id
field in the raw log. The key is set to
id
.
Identity
read_only_udm.target.resource.attribute.labels.value
Directly mapped from the
Identity
field in the raw log. The key is set to
identity
.
Level
read_only_udm.security_result.severity, read_only_udm.security_result.severity_details
Directly mapped from the
Level
field in the raw log. The severity is determined based on the value of
Level
:
Information
,
Informational
,
0
, or
4
maps to
INFORMATIONAL
;
Warning
,
1
, or
3
maps to
MEDIUM
;
Error
or
2
maps to
ERROR
;
Critical
maps to
CRITICAL
.
OperationName
read_only_udm.metadata.product_event_type
Directly mapped from the
OperationName
field in the raw log.
ResourceGroup
read_only_udm.security_result.detection_fields.value
Directly mapped from the
ResourceGroup
field in the raw log. The key is set to
ResourceGroup
.
ResultSignature
read_only_udm.additional.fields.value.string_value
Directly mapped from the
ResultSignature
field in the raw log. The key is set to
resultSignature
.
ResultType
read_only_udm.additional.fields.value.string_value
Directly mapped from the
ResultType
field in the raw log. The key is set to
resultType
.
TenantId
read_only_udm.metadata.product_deployment_id
Directly mapped from the
TenantId
field in the raw log.
TimeGenerated
read_only_udm.metadata.event_timestamp.seconds, read_only_udm.metadata.event_timestamp.nanos
Directly mapped from the
TimeGenerated
field in the raw log. The field is parsed as a timestamp and used to populate the
seconds
and
nanos
fields.
TokenIssuerType
read_only_udm.security_result.detection_fields.value
Directly mapped from the
TokenIssuerType
field in the raw log. The key is set to
TokenIssuerType
.
UniqueTokenIdentifier
read_only_udm.security_result.detection_fields.value
Directly mapped from the
UniqueTokenIdentifier
field in the raw log. The key is set to
UniqueTokenIdentifier
.
UserAgent
read_only_udm.network.http.user_agent, read_only_udm.network.http.parsed_user_agent
Directly mapped from the
UserAgent
field in the raw log. The field is parsed as a user agent string and used to populate the
parsed_user_agent
object.
UserDisplayName
read_only_udm.target.user.user_display_name
Directly mapped from the
UserDisplayName
field in the raw log.
UserId
read_only_udm.target.user.userid
Directly mapped from the
UserId
field in the raw log.
UserPrincipalName
read_only_udm.target.user.email_addresses
Directly mapped from the
UserPrincipalName
field in the raw log, but only if it matches the email address pattern.
UserType
read_only_udm.target.user.attribute.roles.name
Directly mapped from the
UserType
field in the raw log.
_Internal_WorkspaceResourceId
read_only_udm.security_result.detection_fields.value
Directly mapped from the
_Internal_WorkspaceResourceId
field in the raw log. The key is set to
Internal_WorkspaceResourceId
.
_ItemId
read_only_udm.security_result.detection_fields.value
Directly mapped from the
_ItemId
field in the raw log. The key is set to
ItemId
.
properties.appId
read_only_udm.security_result.detection_fields.value
Directly mapped from the
appId
field within the
properties
object in the raw log. The key is set to
appId
.
properties.authenticationDetails[].authenticationMethod
read_only_udm.security_result.detection_fields.value
Directly mapped from the
authenticationMethod
field within the
authenticationDetails
array in the raw log. The key is set to
authenticationMethod
.
properties.authenticationDetails[].authenticationMethodDetail
read_only_udm.security_result.detection_fields.value
Directly mapped from the
authenticationMethodDetail
field within the
authenticationDetails
array in the raw log. The key is set to
authenticationMethodDetail
.
properties.authenticationDetails[].authenticationStepDateTime
read_only_udm.security_result.detection_fields.value
Directly mapped from the
authenticationStepDateTime
field within the
authenticationDetails
array in the raw log. The key is set to
authenticationStepDateTime
.
properties.authenticationDetails[].authenticationStepRequirement
read_only_udm.security_result.detection_fields.value
Directly mapped from the
authenticationStepRequirement
field within the
authenticationDetails
array in the raw log. The key is set to
authenticationStepRequirement
.
properties.authenticationDetails[].authenticationStepResultDetail
read_only_udm.security_result.detection_fields.value
Directly mapped from the
authenticationStepResultDetail
field within the
authenticationDetails
array in the raw log. The key is set to
authenticationStepResultDetail
.
properties.authenticationDetails[].succeeded
read_only_udm.security_result.action, read_only_udm.security_result.action_details
Directly mapped from the
succeeded
field within the
authenticationDetails
array in the raw log. If the value is
true
, the action is set to
ALLOW
; otherwise, it is set to
BLOCK
.
properties.conditionalAccessStatus
read_only_udm.additional.fields.value.string_value
Directly mapped from the
conditionalAccessStatus
field within the
properties
object in the raw log. The key is set to
conditionalAccessStatus
.
properties.id
read_only_udm.security_result.detection_fields.value
Directly mapped from the
id
field within the
properties
object in the raw log. The key is set to
id
.
properties.status.errorCode
read_only_udm.security_result.action
If the value is 0, the action is set to
ALLOW
; otherwise, it is set to
BLOCK
.
properties.userId
read_only_udm.target.user.userid
Directly mapped from the
userId
field within the
properties
object in the raw log.
properties.userPrincipalName
read_only_udm.target.user.email_addresses
Directly mapped from the
userPrincipalName
field within the
properties
object in the raw log, but only if it matches the email address pattern.
resourceId
read_only_udm.target.resource.name
Directly mapped from the
resourceId
field in the raw log.
time
read_only_udm.metadata.event_timestamp.seconds, read_only_udm.metadata.event_timestamp.nanos
Directly mapped from the
time
field in the raw log. The field is parsed as a timestamp and used to populate the
seconds
and
nanos
fields.
read_only_udm.extensions.auth.type
The value is set to
AUTHTYPE_UNSPECIFIED
.
read_only_udm.metadata.event_type
The value is determined based on the presence of
principal.ip
and
target.user.userid
fields: if both are present, the type is set to
USER_LOGIN
; if only
principal.ip
is present, the type is set to
STATUS_UPDATE
; otherwise, it is set to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
