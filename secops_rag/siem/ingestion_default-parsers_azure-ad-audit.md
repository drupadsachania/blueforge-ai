# Collect Microsoft Entra ID Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-audit/  
**Scraped:** 2026-03-05T09:26:18.894887Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Entra ID Audit logs
Supported in:
Google secops
SIEM
This document describes how you can collect Microsoft Entra ID (AD) logs by
setting up a Google Security Operations feed.
Azure Active Directory (
AZURE_AD
) is now called Microsoft Entra ID. Azure AD audit logs
(
AZURE_AD_AUDIT
) are now Microsoft Entra ID audit logs.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format.
Before you begin
Ensure you have the following prerequisites:
An Azure subscription that you can sign in to
A global administrator or Azure AD administrator role
An Azure AD (tenant) in Azure
How to configure Azure AD
Sign in to the
Azure
portal.
Go to
Home
>
App registration
, select a registered
application or register an application if you haven't created an application yet.
To register an application, in the
App registration
section, click
New registration
.
In the
Name
field, provide the display name for your application.
In the
Supported account types
section, select the required option to
specify who can use the application or access the API.
Click
Register
.
Go to the
Overview
page and copy the application (client) ID and the directory
(tenant) ID, which are required to configure the Google Security Operations feed.
Click
API permissions
.
Click
Add a permission
, and then select
Microsoft Graph
in the new pane.
Click
Application permissions
.
Select
AuditLog.Read.All
,
Directory.Read.All
, and
SecurityEvents.Read.All
permissions. Ensure that the permissions are
Application permissions
and not
Delegated permissions
.
Click
Grant admin consent for default directory
. Applications are authorized
to call APIs when they are granted permissions by users or administrators as part
of the consent process.
Go to
Settings
>
Manage
.
Click
Certificates and secrets
.
Click
New client secret
. In the
Value
field, the client secret appears.
Copy the client secret value. The value is displayed only at the time of
creation and it is required for the Azure app registration and to configure
the Google Security Operations feed.
For more information, see
How to set up Microsoft Entra ID app
.
For more information regarding the Microsoft Entra for permissions, see
Microsoft Entra for permissions
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
How to set up the Microsoft Entra ID (AZURE AD) Audit feed
Click the
Azure Platform
pack.
Locate the
Azure AD Directory Audit
log type.
Specify values for the following fields:
Source Type
: Third party API (recommended)
OAUTH client ID
: Specify the client ID that you obtained previously.
OAUTH client secret
: Specify the client secret that you obtained previously.
Tenant ID
: Specify the tenant ID that you obtained previously.
API Full path
: Microsoft Graph REST API endpoint URL.
API Authentication Endpoint
: Microsoft Active Directory Authentication Endpoint.
Advanced Options
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
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds,
contact Google Security Operations support
.
Field mapping reference
This parser processes Azure AD Directory Audit logs in JSON format. It extracts relevant fields, transforms them into a unified data model (UDM), and enriches the data with additional context like user details, IP addresses, and security outcomes. The parser also categorizes events based on their characteristics, mapping them to specific UDM event types for easier analysis.
Supported Microsoft Entra ID Audit sample logs
Standard JSON
{
"activityDateTime"
:
"2021-08-31T09:48:50.9118628Z"
,
"activityDisplayName"
:
"Update user"
,
"additionalDetails"
:
[
{
"key"
:
"UserType"
,
"value"
:
"Member"
}
],
"category"
:
"UserManagement"
,
"correlationId"
:
"f4f22805-48e7-492f-985b-9f18a93a7e07"
,
"id"
:
"Directory_f4f22805-48e7-492f-985b-9f18a93a7e07_P24U6_103572455"
,
"initiatedBy"
:
{
"app"
:
{
"appId"
:
null
,
"displayName"
:
"Company Portal"
,
"servicePrincipalId"
:
"9a3a85ee-a70c-40ea-81d0-3a4f7730ea87"
,
"servicePrincipalName"
:
null
},
"user"
:
null
},
"loggedByService"
:
"Core Directory"
,
"operationType"
:
"Update"
,
"result"
:
"success"
,
"resultReason"
:
""
,
"targetResources"
:
[
{
"displayName"
:
null
,
"groupType"
:
null
,
"id"
:
"9cec2a07-92e2-4b67-92a8-9b37f8bfd9c8"
,
"modifiedProperties"
:
[
{
"displayName"
:
"Included Updated Properties"
,
"newValue"
:
"\"\""
,
"oldValue"
:
null
},
{
"displayName"
:
"TargetId.UserType"
,
"newValue"
:
"\"Member\""
,
"oldValue"
:
null
}
],
"type"
:
"User"
,
"userPrincipalName"
:
"jdoe@example.com"
}
]
}
Azure Monitor / Event Hub
{
"records"
:
{
"time"
:
"2025-06-23T07:57:56.8133230Z"
,
"resourceId"
:
"/tenants/00000000-0000-0000-0000-000000000000/providers/Microsoft.aadiam"
,
"operationName"
:
"Sign-in activity"
,
"operationVersion"
:
"1.0"
,
"category"
:
"NonInteractiveUserSignInLogs"
,
"tenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"resultType"
:
"0"
,
"resultSignature"
:
"SUCCESS"
,
"durationMs"
:
0
,
"callerIpAddress"
:
"192.168.1.5"
,
"correlationId"
:
"43d402af-3b2d-41e6-95d6-0b4ca6318874"
,
"identity"
:
"John Doe"
,
"Level"
:
4
,
"location"
:
"US"
,
"properties"
:
{
"id"
:
"b121cd90-f75d-4f46-be80-71ad426f2a00"
,
"createdDateTime"
:
"2025-06-23T07:56:56.5587167+00:00"
,
"userDisplayName"
:
"John Doe"
,
"userPrincipalName"
:
"jdoe@example.com"
,
"userId"
:
"e670bfb4-2477-4967-be2b-ce0c37f1dacd"
,
"appId"
:
"c44b4083-3bb0-49c1-b47d-974e53cbdf3c"
,
"appDisplayName"
:
"Azure Portal"
,
"ipAddress"
:
"192.168.1.5"
,
"status"
:
{
"errorCode"
:
0
},
"location"
:
{
"city"
:
"Aliso Viejo"
,
"state"
:
"California"
,
"countryOrRegion"
:
"US"
,
"geoCoordinates"
:
{
"latitude"
:
33.57358169555664
,
"longitude"
:
-117.72956085205078
}
}
}
}
}
B2C Specific JSON
{
"activityDateTime"
:
"2021-08-31T08:54:05.64932Z"
,
"activityDisplayName"
:
"Exchange token"
,
"additionalDetails"
:
[
{
"key"
:
"TenantId"
,
"value"
:
"example.com"
},
{
"key"
:
"PolicyId"
,
"value"
:
"B2C_1A_my_signup_signin_example"
},
{
"key"
:
"ApplicationId"
,
"value"
:
"a03bbb51-cc9e-4a1d-9006-f06c03bd562a"
},
{
"key"
:
"Client"
,
"value"
:
"Some%20Company/2.0 CFNetwork/1240.0.4 Darwin/20.5.0"
},
{
"key"
:
"GrantType"
,
"value"
:
"authorization_code"
},
{
"key"
:
"ClientIpAddress"
,
"value"
:
"192.168.1.10"
},
{
"key"
:
"DomainName"
,
"value"
:
"https://example.b2clogin.com"
}
],
"category"
:
"Authentication"
,
"correlationId"
:
"6a0797dc-a455-4e96-9ba8-7c49071988f2"
,
"id"
:
"B2C_6a0797dc-a455-4e96-9ba8-7c49071988f2_L8GYQ_15740812"
,
"initiatedBy"
:
{
"app"
:
{
"appId"
:
"N/A"
,
"displayName"
:
null
,
"servicePrincipalId"
:
null
,
"servicePrincipalName"
:
"a03bbb51-cc9e-4a1d-9006-f06c03bd562a"
},
"user"
:
null
},
"loggedByService"
:
"B2C"
,
"operationType"
:
""
,
"result"
:
"success"
,
"resultReason"
:
"N/A"
}
SYSLOG + JSON
<
13
>
Jan
15
06
:
58
:
10
192.168.1.100
GO
AZEPLAPXXXX
[
azure
-
ad
-
audit
-
0
]
:
{
"operationVersion"
:
"1.0"
,
"name"
:
"adb2b.signin - SONAR"
,
"tenantId"
:
"853884de-cbbc-42b5-9576-56cac3b3be72"
,
"logcollector_timestamp"
:
"2026-01-15T06:58:10.458135Z"
,
"properties"
:
{
"appDisplayName"
:
"SG_iSmart+"
,
"agent"
:
{
"agentSubjectType"
:
"notAgentic"
,
"agentType"
:
"notAgentic"
}
,
"appliedConditionalAccessPolicies"
:
[
{
"id"
:
"74f961de-2f6d-4661-bb80-fc4f4b90050e"
,
"displayName"
:
"PersistentBrowser_CA"
,
"enforcedGrantControls"
:
[
"Mfa"
]
,
"conditionsNotSatisfied"
:
0
,
"enforcedSessionControls"
:
[
"PersistentBrowserSessionMode"
]
,
"conditionsSatisfied"
:
19
,
"result"
:
"success"
}
]
,
"id"
:
"6afd2a62-63e4-4ce5-ac9c-80ececce0600"
,
"tenantId"
:
"853884de-cbbc-42b5-9576-56cac3b3be72"
,
"createdDateTime"
:
"2026-01-15T06:54:13.618694+00:00"
,
"userPrincipalName"
:
"jdoe@example.com"
,
"ipAddress"
:
"192.168.1.50"
,
"status"
:
{
"failureReason"
:
"The session has expired or is invalid due to sign-in frequency checks by conditional access."
,
"additionalDetails"
:
"MFA requirement satisfied by claim in the token"
,
"errorCode"
:
70044
}
}
}
Provisioning Log
{
"time"
:
"2024-01-31T21:44:44.2211394Z"
,
"resourceId"
:
"/tenants/00000000-0000-0000-0000-000000000000/providers/Microsoft.aadiam"
,
"operationName"
:
"Synchronization rule action"
,
"category"
:
"AuditLogs"
,
"tenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"resultSignature"
:
"None"
,
"identity"
:
"Azure AD Cloud Sync"
,
"Level"
:
4
,
"properties"
:
{
"id"
:
"Sync_9242f76e-949e-4d91-a232-754605ff4fb0_PELZ1_47254401"
,
"category"
:
"ProvisioningManagement"
,
"correlationId"
:
"9242f76e-949e-4d91-a232-754605ff4fb0"
,
"result"
:
"success"
,
"resultReason"
:
"The Group 'Global - Citrix-2771-eComex-PROD' will be skipped..."
,
"activityDisplayName"
:
"Synchronization rule action"
,
"loggedByService"
:
"Account Provisioning"
,
"initiatedBy"
:
{
"app"
:
{
"appId"
:
null
,
"displayName"
:
"Azure AD Cloud Sync"
}
},
"targetResources"
:
[
{
"id"
:
"c6994033-55a1-4734-bdf4-56627768e208"
,
"displayName"
:
"ServiceNow Production"
,
"type"
:
"ServicePrincipal"
,
"modifiedProperties"
:
[
{
"displayName"
:
"members"
,
"oldValue"
:
"\"d708d89a-c322-405e-b8a8-50f48ead93b3\""
,
"newValue"
:
null
}
]
}
]
}
}
UDM Mapping Table
Log Field
UDM Mapping
Logic
activityDateTime
read_only_udm.metadata.event_timestamp
Direct mapping from the raw log field "activityDateTime".
activityDisplayName
read_only_udm.metadata.product_event_type
Direct mapping from the raw log field "activityDisplayName".
additionalDetails.ApplicationId
read_only_udm.additional.fields
Direct mapping from the raw log field "additionalDetails", where key is "ApplicationId".
additionalDetails.Client
read_only_udm.network.http.user_agent
Direct mapping from the raw log field "additionalDetails", where key is "Client".
additionalDetails.ClientIpAddress
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Direct mapping from the raw log field "additionalDetails", where key is "ClientIpAddress".
additionalDetails.DomainName
read_only_udm.target.hostname, read_only_udm.target.asset.hostname
Direct mapping from the raw log field "additionalDetails", where key is "DomainName".
additionalDetails.EmailAddress
read_only_udm.target.user.email_addresses
Direct mapping from the raw log field "additionalDetails", where key is "EmailAddress".
additionalDetails.GrantType
read_only_udm.additional.fields
Direct mapping from the raw log field "additionalDetails", where key is "GrantType".
additionalDetails.LocalAccountUsername
read_only_udm.additional.fields
Direct mapping from the raw log field "additionalDetails", where key is "LocalAccountUsername".
additionalDetails.PhoneNumber
read_only_udm.target.user.phone_numbers
Direct mapping from the raw log field "additionalDetails", where key is "PhoneNumber".
additionalDetails.PolicyId
read_only_udm.security_result.rule_name
Direct mapping from the raw log field "additionalDetails", where key is "PolicyId".
additionalDetails.Scopes
read_only_udm.additional.fields
Direct mapping from the raw log field "additionalDetails", where key is "Scopes".
additionalDetails.TenantId
read_only_udm.additional.fields
Direct mapping from the raw log field "additionalDetails", where key is "TenantId".
additionalDetails.VerificationMethod
read_only_udm.additional.fields
Direct mapping from the raw log field "additionalDetails", where key is "VerificationMethod".
appId
read_only_udm.target.process.pid
Direct mapping from the raw log field "appId".
appliedConditionalAccessPolicies
read_only_udm.about
The "displayName" field is mapped to "read_only_udm.about.user.user_display_name" and the "id" field is mapped to "read_only_udm.about.user.userid". The "result" field is mapped to "read_only_udm.about.labels", with the key set to "Result".
category
read_only_udm.additional.fields, read_only_udm.security_result.category_details
Direct mapping from the raw log field "category". The key for "read_only_udm.additional.fields" is set to "log_category".
callerIpAddress
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Direct mapping from the raw log field "callerIpAddress".
clientAppUsed
read_only_udm.principal.application
Direct mapping from the raw log field "clientAppUsed".
correlationId
read_only_udm.network.session_id
Direct mapping from the raw log field "correlationId".
id
read_only_udm.metadata.product_log_id
Direct mapping from the raw log field "id".
identity
read_only_udm.target.user.userid
Direct mapping from the raw log field "identity".
initiatedBy.app.appId
read_only_udm.principal.resource.attribute.labels
Direct mapping from the raw log field "initiatedBy.app.appId". The key for "read_only_udm.principal.resource.attribute.labels" is set to "App Id".
initiatedBy.app.displayName
read_only_udm.principal.application
Direct mapping from the raw log field "initiatedBy.app.displayName".
initiatedBy.app.servicePrincipalId
read_only_udm.principal.user.product_object_id
Direct mapping from the raw log field "initiatedBy.app.servicePrincipalId".
initiatedBy.app.servicePrincipalName
read_only_udm.principal.user.userid
Direct mapping from the raw log field "initiatedBy.app.servicePrincipalName".
initiatedBy.user.displayName
read_only_udm.principal.user.user_display_name, read_only_udm.principal.user.email_addresses
If the value contains "@" then it is parsed as an email address and mapped to "read_only_udm.principal.user.email_addresses". Otherwise, it is mapped to "read_only_udm.principal.user.user_display_name".
initiatedBy.user.id
read_only_udm.principal.user.product_object_id
Direct mapping from the raw log field "initiatedBy.user.id".
initiatedBy.user.ipAddress
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Direct mapping from the raw log field "initiatedBy.user.ipAddress".
initiatedBy.user.userPrincipalName
read_only_udm.principal.user.userid, read_only_udm.principal.user.email_addresses, read_only_udm.principal.administrative_domain, read_only_udm.principal.resource.attribute.labels
If the value contains "@" then it is parsed as an email address and mapped to "read_only_udm.principal.user.email_addresses". Otherwise, it is mapped to "read_only_udm.principal.user.userid". The domain part of the email address is mapped to "read_only_udm.principal.administrative_domain". The full value is also mapped to "read_only_udm.principal.resource.attribute.labels" with the key set to "User Principal Name".
ipAddress
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Direct mapping from the raw log field "ipAddress".
Level
read_only_udm.security_result.severity, read_only_udm.security_result.severity_details
The value is converted to a string and mapped to "read_only_udm.security_result.severity_details". The "read_only_udm.security_result.severity" field is set to "INFORMATIONAL".
location.city
read_only_udm.principal.location.city
Direct mapping from the raw log field "location.city".
location.countryOrRegion
read_only_udm.principal.location.country_or_region
Direct mapping from the raw log field "location.countryOrRegion".
location.geoCoordinates.latitude
read_only_udm.principal.location.region_latitude
Direct mapping from the raw log field "location.geoCoordinates.latitude".
location.geoCoordinates.longitude
read_only_udm.principal.location.region_longitude
Direct mapping from the raw log field "location.geoCoordinates.longitude".
location.state
read_only_udm.principal.location.state
Direct mapping from the raw log field "location.state".
loggedByService
read_only_udm.additional.fields
Direct mapping from the raw log field "loggedByService". The key for "read_only_udm.additional.fields" is set to "loggedByService".
operationName
read_only_udm.metadata.product_event_type
Direct mapping from the raw log field "operationName".
operationType
read_only_udm.security_result.action_details
Direct mapping from the raw log field "operationType".
properties.activityDateTime
read_only_udm.metadata.event_timestamp
Direct mapping from the raw log field "properties.activityDateTime".
properties.activityDisplayName
read_only_udm.metadata.product_event_type
Direct mapping from the raw log field "properties.activityDisplayName".
properties.appDisplayName
read_only_udm.target.application
Direct mapping from the raw log field "properties.appDisplayName".
properties.category
read_only_udm.security_result.category_details
Direct mapping from the raw log field "properties.category".
properties.id
read_only_udm.metadata.product_log_id
Direct mapping from the raw log field "properties.id".
properties.initiatedBy.app.appId
read_only_udm.principal.resource.attribute.labels
Direct mapping from the raw log field "properties.initiatedBy.app.appId". The key for "read_only_udm.principal.resource.attribute.labels" is set to "App Id".
properties.initiatedBy.app.displayName
read_only_udm.principal.application
Direct mapping from the raw log field "properties.initiatedBy.app.displayName".
properties.initiatedBy.app.servicePrincipalId
read_only_udm.principal.user.product_object_id
Direct mapping from the raw log field "properties.initiatedBy.app.servicePrincipalId".
properties.initiatedBy.app.servicePrincipalName
read_only_udm.principal.user.userid
Direct mapping from the raw log field "properties.initiatedBy.app.servicePrincipalName".
properties.initiatedBy.user.displayName
read_only_udm.principal.user.user_display_name, read_only_udm.principal.user.email_addresses
If the value contains "@" then it is parsed as an email address and mapped to "read_only_udm.principal.user.email_addresses". Otherwise, it is mapped to "read_only_udm.principal.user.user_display_name".
properties.initiatedBy.user.id
read_only_udm.principal.user.product_object_id
Direct mapping from the raw log field "properties.initiatedBy.user.id".
properties.initiatedBy.user.ipAddress
read_only_udm.principal.ip, read_only_udm.principal.asset.ip
Direct mapping from the raw log field "properties.initiatedBy.user.ipAddress".
properties.initiatedBy.user.userPrincipalName
read_only_udm.principal.user.userid, read_only_udm.principal.user.email_addresses, read_only_udm.principal.administrative_domain, read_only_udm.principal.resource.attribute.labels
If the value contains "@" then it is parsed as an email address and mapped to "read_only_udm.principal.user.email_addresses". Otherwise, it is mapped to "read_only_udm.principal.user.userid". The domain part of the email address is mapped to "read_only_udm.principal.administrative_domain". The full value is also mapped to "read_only_udm.principal.resource.attribute.labels" with the key set to "User Principal Name".
properties.loggedByService
read_only_udm.additional.fields
Direct mapping from the raw log field "properties.loggedByService". The key for "read_only_udm.additional.fields" is set to "loggedByService".
properties.operationType
read_only_udm.security_result.action_details
Direct mapping from the raw log field "properties.operationType".
properties.result
read_only_udm.security_result.summary
Direct mapping from the raw log field "properties.result".
properties.resultReason
read_only_udm.security_result.description
Direct mapping from the raw log field "properties.resultReason".
properties.userPrincipalName
read_only_udm.target.user.user_display_name
Direct mapping from the raw log field "properties.userPrincipalName".
result
read_only_udm.security_result.summary, read_only_udm.security_result.action
Direct mapping from the raw log field "result". If the value is "success" then "read_only_udm.security_result.action" is set to "ALLOW". If the value is "failure" then "read_only_udm.security_result.action" is set to "BLOCK".
resultDescription
read_only_udm.metadata.description, read_only_udm.security_result.description
Direct mapping from the raw log field "resultDescription".
resultReason
read_only_udm.security_result.description
Direct mapping from the raw log field "resultReason".
resultType
read_only_udm.security_result.rule_id, read_only_udm.security_result.summary, read_only_udm.security_result.action
Direct mapping from the raw log field "resultType". If the value is "0" then "read_only_udm.security_result.action" is set to "ALLOW" and "read_only_udm.security_result.summary" is set to "Successful login occurred". Otherwise, "read_only_udm.security_result.action" is set to "BLOCK", "read_only_udm.security_result.summary" is set to "Failed login occurred", "read_only_udm.security_result.description" is set to the value of "resultDescription", and "read_only_udm.security_result.severity" is set to "ERROR".
resourceDisplayName
read_only_udm.target.resource.name
Direct mapping from the raw log field "resourceDisplayName".
resourceId
read_only_udm.additional.fields
Direct mapping from the raw log field "resourceId". The key for "read_only_udm.additional.fields" is set to "resourceId".
riskDetail
read_only_udm.additional.fields
Direct mapping from the raw log field "riskDetail". The key for "read_only_udm.additional.fields" is set to "riskDetail".
riskEventTypes
read_only_udm.additional.fields
Direct mapping from the raw log field "riskEventTypes". The key for "read_only_udm.additional.fields" is set to "riskEventTypes".
riskEventTypes_v2
read_only_udm.additional.fields
Direct mapping from the raw log field "riskEventTypes_v2". The key for "read_only_udm.additional.fields" is set to "riskEventTypes_v2".
riskLevelAggregated
read_only_udm.additional.fields
Direct mapping from the raw log field "riskLevelAggregated". The key for "read_only_udm.additional.fields" is set to "riskLevelAggregated".
riskLevelDuringSignIn
read_only_udm.additional.fields, read_only_udm.security_result.priority
Direct mapping from the raw log field "riskLevelDuringSignIn". The key for "read_only_udm.additional.fields" is set to "riskLevelDuringSignIn". If the value is "medium" then "read_only_udm.security_result.priority" is set to "MEDIUM_PRIORITY".
riskState
read_only_udm.additional.fields
Direct mapping from the raw log field "riskState". The key for "read_only_udm.additional.fields" is set to "riskState".
targetResources.0.displayName
read_only_udm.target.resource.name, read_only_udm.target.user.user_display_name, read_only_udm.target.group.group_display_name
If the value of "targetResources.0.type" is "User" or "ServicePrincipal", then the value is mapped to "read_only_udm.target.user.user_display_name". If the value of "targetResources.0.type" is "Group", then the value is mapped to "read_only_udm.target.group.group_display_name". Otherwise, the value is mapped to "read_only_udm.target.resource.name".
targetResources.0.groupType
read_only_udm.target.group.attribute.labels
Direct mapping from the raw log field "targetResources.0.groupType". The key for "read_only_udm.target.group.attribute.labels" is set to "groupType".
targetResources.0.id
read_only_udm.target.resource.product_object_id, read_only_udm.target.user.product_object_id, read_only_udm.target.group.product_object_id
If the value of "targetResources.0.type" is "User" or "ServicePrincipal", then the value is mapped to "read_only_udm.target.user.product_object_id". If the value of "targetResources.0.type" is "Group", then the value is mapped to "read_only_udm.target.group.product_object_id". Otherwise, the value is mapped to "read_only_udm.target.resource.product_object_id".
targetResources.0.modifiedProperties.displayName
read_only_udm.additional.fields, read_only_udm.target.asset.asset_id, read_only_udm.target.user.title, read_only_udm.target.resource.attribute.roles, read_only_udm.target.user.user_display_name, read_only_udm.target.user.first_name, read_only_udm.target.user.last_name, read_only_udm.target.user.department, read_only_udm.target.user.office_address.name, read_only_udm.target.user.employee_id, read_only_udm.target.user.phone_numbers, read_only_udm.target.user.userid, read_only_udm.target.resource.attribute.labels, read_only_udm.src.resource.attribute.labels
The value is mapped to "read_only_udm.additional.fields" with the key set to "targetResources.modifiedProperties.displayname {index}". If the value is "TargetId.DeviceId", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.asset.asset_id" with the prefix "Device ID:". If the value is "DisplayName" or "jobTitle", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.title". If the value is "WellKnownObjectName", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.resource.attribute.roles" with the key set to "name". If the value is "displayName" and "targetResources.0.displayName" is null, then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.user_display_name". If the value is "givenName", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.first_name". If the value is "surname", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.last_name". If the value is "department", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.department". If the value is "physicalDeliveryOfficeName", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.office_address.name". If the value is "employeeId", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.employee_id". If the value is "mobile", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.phone_numbers". If the value is "MailNickname", then the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.user.userid". Otherwise, the value of "targetResources.0.modifiedProperties.newValue" is mapped to "read_only_udm.target.resource.attribute.labels" with the key set to the value of "targetResources.0.modifiedProperties.displayName". The value of "targetResources.0.modifiedProperties.oldValue" is mapped to "read_only_udm.src.resource.attribute.labels" with the key set to the value of "targetResources.0.modifiedProperties.displayName".
targetResources.0.modifiedProperties.newValue
read_only_udm.target.asset.asset_id, read_only_udm.target.user.title, read_only_udm.target.resource.attribute.roles, read_only_udm.target.user.user_display_name, read_only_udm.target.user.first_name, read_only_udm.target.user.last_name, read_only_udm.target.user.department, read_only_udm.target.user.office_address.name, read_only_udm.target.user.employee_id, read_only_udm.target.user.phone_numbers, read_only_udm.target.user.userid, read_only_udm.target.resource.attribute.labels, read_only_udm.additional.fields
If the value of "targetResources.0.modifiedProperties.displayName" is "TargetId.DeviceId", then the value is mapped to "read_only_udm.target.asset.asset_id" with the prefix "Device ID:". If the value of "targetResources.0.modifiedProperties.displayName" is "DisplayName" or "jobTitle", then the value is mapped to "read_only_udm.target.user.title". If the value of "targetResources.0.modifiedProperties.displayName" is "WellKnownObjectName", then the value is mapped to "read_only_udm.target.resource.attribute.roles" with the key set to "name". If the value of "targetResources.0.modifiedProperties.displayName" is "displayName" and "targetResources.0.displayName" is null, then the value is mapped to "read_only_udm.target.user.user_display_name". If the value of "targetResources.0.modifiedProperties.displayName" is "givenName", then the value is mapped to "read_only_udm.target.user.first_name". If the value of "targetResources.0.modifiedProperties.displayName" is "surname", then the value is mapped to "read_only_udm.target.user.last_name". If the value of "targetResources.0.modifiedProperties.displayName" is "department", then the value is mapped to "read_only_udm.target.user.department". If the value of "targetResources.0.modifiedProperties.displayName" is "physicalDeliveryOfficeName", then the value is mapped to "read_only_udm.target.user.office_address.name". If the value of "targetResources.0.modifiedProperties.displayName" is "employeeId", then the value is mapped to "read_only_udm.target.user.employee_id". If the value of "targetResources.0.modifiedProperties.displayName" is "mobile", then the value is mapped to "read_only_udm.target.user.phone_numbers". If the value of "targetResources.0.modifiedProperties.displayName" is "MailNickname", then the value is mapped to "read_only_udm.target.user.userid". Otherwise, the value is mapped to "read_only_udm.target.resource.attribute.labels" with the key set to the value of "targetResources.0.modifiedProperties.displayName". The value is also mapped to "read_only_udm.additional.fields" with the key set to "targetResources.modifiedProperties.newValue {index}".
targetResources.0.modifiedProperties.oldValue
read_only_udm.src.resource.attribute.labels, read_only_udm.additional.fields
The value is mapped to "read_only_udm.src.resource.attribute.labels" with the key set to the value of "targetResources.0.modifiedProperties.displayName". The value is also mapped to "read_only_udm.additional.fields" with the key set to "targetResources.modifiedProperties.oldValue {index}".
targetResources.0.type
read_only_udm.target.resource.resource_subtype, read_only_udm.target.resource.resource_type, read_only_udm.target.user.userid, read_only_udm.target.user.product_object_id, read_only_udm.target.user.user_display_name, read_only_udm.target.group.product_object_id, read_only_udm.target.group.group_display_name
Direct mapping from the raw log field "targetResources.0.type". If the value is "ServicePrincipal", then "read_only_udm.target.resource.resource_type" is set to "SERVICE_ACCOUNT". If the value is "Device", then "read_only_udm.target.resource.resource_type" is set to "DEVICE". Otherwise, "read_only_udm.target.resource.resource_type" is set to "UNSPECIFIED". If the value is "User" or "ServicePrincipal", then the value of "targetResources.0.userPrincipalName" is mapped to "read_only_udm.target.user.userid", the value of "targetResources.0.id" is mapped to "read_only_udm.target.user.product_object_id", and the value of "targetResources.0.displayName" is mapped to "read_only_udm.target.user.user_display_name". If the value is "Group", then the value of "targetResources.0.id" is mapped to "read_only_udm.target.group.product_object_id" and the value of "targetResources.0.displayName" is mapped to "read_only_udm.target.group.group_display_name".
targetResources.0.userPrincipalName
read_only_udm.target.user.userid, read_only_udm.target.user.email_addresses
If the value contains "@" then it is parsed as an email address and mapped to "read_only_udm.target.user.email_addresses". Otherwise, it is mapped to "read_only_udm.target.user.userid".
targetResources.displayName
read_only_udm.about.resource.name, read_only_udm.about.user.userid, read_only_udm.about.user.user_display_name, read_only_udm.about.group.group_display_name, read_only_udm.about.group.attribute.labels
If the value of "targetResources.type" is "User" or "ServicePrincipal", then the value is mapped to "read_only_udm.about.user.user_display_name" and "read_only_udm.about.user.userid". If the value of "targetResources.type" is "Group", then the value is mapped to "read_only_udm.about.group.group_display_name". The value of "targetResources.groupType" is mapped to "read_only_udm.about.group.attribute.labels" with the key set to "groupType". Otherwise, the value is mapped to "read_only_udm.about.resource.name".
targetResources.groupType
read_only_udm.about.group.attribute.labels, read_only_udm.target.user.group_identifiers
Direct mapping from the raw log field "targetResources.groupType". The key for "read_only_udm.about.group.attribute.labels" is set to "groupType".
targetResources.id
read_only_udm.about.resource.product_object_id, read_only_udm.about.user.product_object_id, read_only_udm.about.group.product_object_id
If the value of "targetResources.type" is "User" or "ServicePrincipal", then the value is mapped to "read_only_udm.about.user.product_object_id". If the value of "targetResources.type" is "Group", then the value is mapped to "read_only_udm.about.group.product_object_id". Otherwise, the value is mapped to "read_only_udm.about.resource.product_object_id".
targetResources.modifiedProperties.displayName
read_only_udm.additional.fields
The value is mapped to "read_only_udm.additional.fields" with the key set to "targetResources.modifiedProperties.displayname {index}".
targetResources.modifiedProperties.newValue
read_only_udm.additional.fields
The value is mapped to "read_only_udm.additional.fields" with the key set to "targetResources.modifiedProperties.newValue {index}".
targetResources.modifiedProperties.oldValue
read_only_udm.additional.fields
The value is mapped to "read_only_udm.additional.fields" with the key set to "targetResources.modifiedProperties.oldValue {index}".
targetResources.type
read_only_udm.about.resource.resource_subtype, read_only_udm.about.resource.resource_type, read_only_udm.about.user.userid, read_only_udm.about.user.product_object_id, read_only_udm.about.user.user_display_name, read_only_udm.about.group.product_object_id, read_only_udm.about.group.group_display_name
Direct mapping from the raw log field "targetResources.type". If the value is "ServicePrincipal", then "read_only_udm.about.resource.resource_type" is set to "SERVICE_ACCOUNT". If the value is "Device", then "read_only_udm.about.resource.resource_type" is set to "DEVICE". Otherwise, "read_only_udm.about.resource.resource_type" is set to "UNSPECIFIED". If the value is "User" or "ServicePrincipal", then the value of "targetResources.userPrincipalName" is mapped to "read_only_udm.about.user.userid", the value of "targetResources.id" is mapped to "read_only_udm.about.user.product_object_id", and the value of "targetResources.displayName" is mapped to "read_only_udm.about.user.user_display_name". If the value is "Group", then the value of "targetResources.id" is mapped to "read_only_udm.about.group.product_object_id" and the value of "targetResources.displayName" is mapped to "read_only_udm.about.group.group_display_name".
targetResources.userPrincipalName
read_only_udm.about.user.userid, read_only_udm.about.user.email_addresses
If the value contains "@" then it is parsed as an email address and mapped to "read_only_udm.about.user.email_addresses". Otherwise, it is mapped to "read_only_udm.about.user.userid".
tenantId
read_only_udm.additional.fields
Direct mapping from the raw log field "tenantId". The key for "read_only_udm.additional.fields" is set to "tenantId".
time
read_only_udm.metadata.event_timestamp
Direct mapping from the raw log field "time".
userId
read_only_udm.target.user.product_object_id
Direct mapping from the raw log field "userId". The value is set based on the values of other fields, including "activityDisplayName", "principal_userid_present", "target_userid_present", "principal_ip_present", "loggedByService", and "category". The logic for setting the value is complex and depends on the specific combination of values in these fields. The value is set to "SSO" if the value of "operationName" is "Sign-in activity". The value is set to "Microsoft". The value is set to "Azure AD Directory Audit". The value is set to "AZURE_AD_AUDIT".
Need more help?
Get answers from Community members and Google SecOps professionals.
