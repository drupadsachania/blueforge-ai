# Collect Microsoft Graph activity logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-activity-logs/  
**Scraped:** 2026-03-05T09:26:29.108866Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Graph activity logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Microsoft Graph activity logs, transforming them into the Unified Data Model (UDM). It initializes UDM fields, parses the payload, extracts timestamps, maps various properties to UDM fields, handles IP addresses and ports, and categorizes the event type based on the presence of principal and network information.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Microsoft Entra ID and Azure storage accounts.
Configure Azure storage account
In the Azure console, search for storage accounts.
Click
Create
.
Specify values for the following input parameters:
Subscription
: select the subscription.
Resource Group
: select the resource group.
Region
: select the region.
Performance
: select the performance level that you want (standard is recommended).
Redundancy
: select the redundancy level that you want (GRS or LRS is recommended).
Storage account name
: enter a name for the new storage account.
Click
Review + create
.
Review the overview of the account and click
Create
.
From the
Storage Account Overview
page, select submenu
Access keys
in
Security + networking
.
Click
Show
next to
key1
or
key2
Click
Copy to clipboard
to copy the key.
Save the key in a secure location for future reference.
From the
Storage Account Overview
page, select submenu
Endpoints
in
Settings
.
Click
Copy to clipboard
to copy the
Blob service
endpoint URL (for example,
https://
.blob.core.windows.net
).
Save the endpoint URL in a secure location for future reference.
Configure Microsoft Graph activity logs export to storage account
In the Azure console, search for
Entra ID
.
Select
Monitoring
>
Diagnostic settings
.
Click
+ Add diagnostic setting
.
Give the setting a unique name (for example,
ms-graph-activity
).
Select the
MicrosoftGraphActivityLog
category you want to export to Google SecOps.
Under
Destination details
, select
Archive to a storage account
.
Select your subscription and the storage account you created in the previous step.
Click
Save
.
How to set up the Microsoft Graph Activity logs
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
Microsoft Graph Activity Logs
.
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
Microsoft Graph Activity Logs
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Azure uri
: the blob endpoint URL.
ENDPOINT_URL/BLOB_NAME
Replace the following:
ENDPOINT_URL
: the blob endpoint URL (
https://<storageaccountname>.blob.core.windows.net
)
BLOB_NAME
: the name of the blob (for example,
insights-logs-
)
Source deletion options
: select deletion option according to your preference.
Maximum File Age
: Files modified in the last number of days. Default is 180 days.
Shared key
: the access key to the Azure Blob Storage.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Supported Microsoft Graph Activity Logs sample logs
Standard JSON
{
"time"
:
"2024-02-24T02:36:04.9540786Z"
,
"resourceId"
:
"/TENANTS/00000000-0000-0000-0000-000000000000/PROVIDERS/MICROSOFT.AADIAM"
,
"operationName"
:
"Microsoft Graph Activity"
,
"operationVersion"
:
"v1.0"
,
"category"
:
"MicrosoftGraphActivityLogs"
,
"tenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"resultSignature"
:
"200"
,
"durationMs"
:
856631
,
"callerIpAddress"
:
"192.0.2.1"
,
"correlationId"
:
"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
,
"Level"
:
4
,
"location"
:
"South Central US"
,
"properties"
:
{
"timeGenerated"
:
"2024-02-24T02:36:04.9540786Z"
,
"location"
:
"South Central US"
,
"requestId"
:
"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
,
"operationId"
:
"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
,
"clientRequestId"
:
"ffffffff-gggg-hhhh-iiii-jjjjjjjjjjjj"
,
"apiVersion"
:
"v1.0"
,
"requestMethod"
:
"GET"
,
"responseStatusCode"
:
200
,
"tenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"ipAddress"
:
"192.0.2.1"
,
"userAgent"
:
"Internal-Service-Scanner"
,
"requestUri"
:
"https://graph.microsoft.com/v1.0/subscribedSkus"
,
"durationMs"
:
856631
,
"responseSizeBytes"
:
11808
,
"signInActivityId"
:
"REDACTED_ACTIVITY_ID"
,
"roles"
:
"Organization.Read.All Policy.Read.All User.Read.All"
,
"tokenIssuedAt"
:
"2024-02-23T23:48:42Z"
,
"appId"
:
"00000000-0000-0000-0000-000000000000"
,
"userId"
:
null
,
"servicePrincipalId"
:
"11111111-2222-3333-4444-555555555555"
,
"identityProvider"
:
"https://sts.windows.net/00000000-0000-0000-0000-000000000000/"
,
"clientAuthMethod"
:
"2"
}
}
Azure Monitor PascalCase Format
{
"TimeGenerated"
:
"2024-06-07T11:52:40.4216173Z"
,
"Location"
:
"East US"
,
"RequestId"
:
"bbbbbbbb-1111-2222-3333-cccccccccccc"
,
"OperationId"
:
"bbbbbbbb-1111-2222-3333-cccccccccccc"
,
"ClientRequestId"
:
"dddddddd-4444-5555-6666-eeeeeeeeeeee"
,
"ApiVersion"
:
"v1.0"
,
"RequestMethod"
:
"GET"
,
"ResponseStatusCode"
:
200
,
"AadTenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"IPAddress"
:
"198.51.100.50"
,
"UserAgent"
:
"LokiServer/1.2024"
,
"RequestUri"
:
"https://graph.microsoft.com/v1.0/users/user@example.com"
,
"DurationMs"
:
1309774
,
"ResponseSizeBytes"
:
192
,
"SignInActivityId"
:
"REDACTED_ACTIVITY_ID"
,
"TokenIssuedAt"
:
"2024-0G-07T11:47:39.0000000Z"
,
"AppId"
:
"00000000-0000-0000-0000-000000000000"
,
"UserId"
:
"user_id_9999"
,
"Scopes"
:
"User.Read User.Read.All"
,
"ClientAuthMethod"
:
2
,
"_ItemId"
:
"unique_item_id_001"
,
"Type"
:
"MicrosoftGraphActivityLogs"
,
"TenantId"
:
"00000000-0000-0000-0000-000000000000"
}
UDI Required Fields
{
"time"
:
"2024-08-14T19:37:39.2484449Z"
,
"resourceId"
:
"/TENANTS/00000000-0000-0000-0000-000000000000/PROVIDERS/MICROSOFT.AADIAM"
,
"operationName"
:
"Microsoft Graph Activity"
,
"resultSignature"
:
"200"
,
"callerIpAddress"
:
"203.0.113.10"
,
"properties"
:
{
"__UDI_RequiredFields_TenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"__UDI_RequiredFields_UniqueId"
:
"uuid-123456-7890"
,
"timeGenerated"
:
"2024-08-14T19:37:39.2484449Z"
,
"requestId"
:
"uuid-123456-7890"
,
"requestMethod"
:
"GET"
,
"responseStatusCode"
:
200
,
"ipAddress"
:
"203.0.113.10"
,
"userAgent"
:
"Security-Audit-Tool"
,
"requestUri"
:
"https://graph.microsoft.com/v1.0/auditLogs/directoryAudits"
,
"UserPrincipalObjectID"
:
"user_obj_8888"
,
"appId"
:
"00000000-0000-0000-0000-000000000000"
},
"tenantId"
:
"00000000-0000-0000-0000-000000000000"
}
UDI Beta Format
{
"time"
:
"2024-08-14T18:37:12.8698765Z"
,
"operationVersion"
:
"beta"
,
"callerIpAddress"
:
"2001:db8::ff00:42:8329"
,
"level"
:
"Informational"
,
"properties"
:
{
"__UDI_RequiredFields_TenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"apiVersion"
:
"beta"
,
"requestMethod"
:
"GET"
,
"responseStatusCode"
:
404
,
"ipAddress"
:
"2001:db8::ff00:42:8329"
,
"requestUri"
:
"https://graph.microsoft.com/beta/users/user_id_masked/photos"
,
"userId"
:
"user_id_7777"
,
"appId"
:
"00000000-0000-0000-0000-000000000000"
}
}
UDM Mapping Table
Log Field
UDM Mapping
Logic
callerIpAddress
principal.asset.ip
The raw log field
callerIpAddress
is copied to the UDM field.
callerIpAddress
principal.ip
The raw log field
callerIpAddress
is copied to the UDM field.
category
security_result.category_details
The raw log field
category
is copied to the UDM field.
correlationId
security_result.detection_fields.value
The raw log field
correlationId
is copied to the UDM field, where key is
correlationId
.
Level
security_result.detection_fields.value
The raw log field
Level
is converted to string and copied to the UDM field, where key is
Level
.
operationName
metadata.product_event_type
The raw log field
operationName
is copied to the UDM field.
operationVersion
additional.fields.value.string_value
The raw log field
operationVersion
is copied to the UDM field, where key is
operationVersion
.
properties.apiVersion
metadata.product_version
The raw log field
properties.apiVersion
is copied to the UDM field.
properties.appId
target.resource.product_object_id
The raw log field
properties.appId
is copied to the UDM field.
properties.atContent
additional.fields.value.string_value
The raw log field
properties.atContent
is copied to the UDM field, where key is
atContent
.
properties.clientAuthMethod
extensions.auth.auth_details
Based on the value of
properties.clientAuthMethod
, the UDM field is set to "Public Client" (0), "Client ID/Client Secret" (1), or "Client Certificate" (2).
properties.clientRequestId
additional.fields.value.string_value
The raw log field
properties.clientRequestId
is copied to the UDM field, where key is
clientRequestId
.
properties.durationMs
network.session_duration.seconds
The raw log field
properties.durationMs
is converted from milliseconds to seconds and copied to the UDM field.
properties.identityProvider
security_result.detection_fields.value
The raw log field
properties.identityProvider
is copied to the UDM field, where key is
identityProvider
.
properties.ipAddress
principal.asset.ip
The IP address from the raw log field
properties.ipAddress
is extracted and copied to the UDM field.
properties.ipAddress
principal.ip
The IP address from the raw log field
properties.ipAddress
is extracted and copied to the UDM field.
properties.location
principal.location.name
The raw log field
properties.location
is copied to the UDM field.
properties.operationId
security_result.detection_fields.value
The raw log field
properties.operationId
is copied to the UDM field, where key is
operationId
.
properties.requestMethod
network.http.method
The raw log field
properties.requestMethod
is copied to the UDM field.
properties.requestId
metadata.product_log_id
The raw log field
properties.requestId
is copied to the UDM field.
properties.responseSizeBytes
network.received_bytes
The raw log field
properties.responseSizeBytes
is converted to an unsigned integer and copied to the UDM field.
properties.responseStatusCode
network.http.response_code
The raw log field
properties.responseStatusCode
is converted to an integer and copied to the UDM field.
properties.roles
additional.fields.value.string_value
The raw log field
properties.roles
is copied to the UDM field, where key is
roles
.
properties.scopes
additional.fields.value.string_value
The raw log field
properties.scopes
is copied to the UDM field, where key is
Scopes
.
properties.servicePrincipalId
principal.user.userid
The raw log field
properties.servicePrincipalId
is copied to the UDM field if
properties.userId
is empty.
properties.signInActivityId
network.session_id
The raw log field
properties.signInActivityId
is copied to the UDM field.
properties.tenantId
metadata.product_deployment_id
The raw log field
properties.tenantId
is copied to the UDM field.
properties.tokenIssuedAt
additional.fields.value.string_value
The raw log field
properties.tokenIssuedAt
is copied to the UDM field, where key is
tokenIssuedAt
.
properties.userAgent
network.http.user_agent
The raw log field
properties.userAgent
is copied to the UDM field.
properties.userId
principal.user.userid
The raw log field
properties.userId
is copied to the UDM field.
properties.wids
security_result.detection_fields.value
The raw log field
properties.wids
is copied to the UDM field, where key is
wids
.
resourceId
target.resource.attribute.labels.value
The raw log field
resourceId
is copied to the UDM field, where key is
Resource ID
.
resultSignature
additional.fields.value.string_value
The raw log field
resultSignature
is copied to the UDM field, where key is
resultSignature
.
time
metadata.event_timestamp
The raw log field
time
is parsed and converted to a timestamp and copied to the UDM field. The UDM field
event.idm.read_only_udm.metadata.event_type
is set to "NETWORK_HTTP" if
has_principal
is true and
network.http
is not empty, "STATUS_UPDATE" if
has_principal
is true and
network.http
is empty, or "GENERIC_EVENT" otherwise. The UDM field is set to "Microsoft Graph". The UDM field is set to "Microsoft".
Need more help?
Get answers from Community members and Google SecOps professionals.
