# Collect Azure DevOps audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-devops/  
**Scraped:** 2026-03-05T09:26:20.970704Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure DevOps audit logs
Supported in:
Google secops
SIEM
Overview
This parser handles Azure DevOps audit logs in JSON format. It extracts fields from nested and top-level JSON structures, mapping them to the UDM. Conditional logic based on specific field values categorizes events and enriches the output with relevant security information. The parser also handles non-JSON formatted messages by attempting to extract a JSON payload using grok patterns.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
An active Azure DevOps Organization
Privileged access to Azure Devops Organization and Azure
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
How to set up the Azure DevOps audit feed
Click the
Azure Platform
pack.
Locate the
Azure DevOps audit
log type and click
Add new feed
.
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
: Includes files modified in the last number of days. Default is 180 days.
Shared key
: The shared key (a 512-bit random string in base-64 encoding) used to access Azure resources.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
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
: The feed endpoint URL.
API_KEY
: The API key to authenticate to Google Security Operations.
SECRET
: The secret key that you generated to authenticate the feed.
Configure Auditing feature in Azure Devops
Sign in to your organization (
https://dev.azure.com/{yourorganization}
).
Select the gear icon for
Organization settings
.
Select
Policies
under
Security
.
Toggle the
Log Audit Events
button to
ON
.
Configure an Event Grid Topic in Azure
Sign in to the Azure Portal.
Search for and access
Event Grid
.
Locate
Topics
under
Custom events
.
Click
+ Create
.
Select your
Subscription
and
Resource Group
. Provide a name (for example,
DevopsAuditLog
) and select the region. Click
Review and create
.
Access the new
Topic
and copy the
Topic Endpoint URL
.
Go to
Settings
>
Access Keys
and copy
Key 1
.
Configure Azure Devops Log Stream to Event Grid
Sign in to your organization (
https://dev.azure.com/{yourorganization}
).
Select the gear icon for
Organization settings
.
Select
Auditing
.
Go to the
Streams
tab and select
New stream
>
Event Grid
.
Enter the
topic endpoint
and
access key
created in
Configure an Event Grid Topic in Azure
.
Configure a Webhook in Azure DevOps for Google SecOps
In the Azure Portal, search for and access
Event Grid
.
Select previously created
Topic
.
Go to
Entities
>
Event Subscription
.
Click
+ Event Subscription
.
Provide a descriptive name (for example, *
Google SecOps Integration
).
Select
Web Hook
and click
Configure an endpoint
.
Configure the endpoint:
Subscriber endpoint
: Enter the Google SecOps API endpoint URL.
In the
HTTP headers
section, add the following headers:
Header 1
:
Key
:
X-goog-api-key
Value
: The API key you created in the
Create an API key for the webhook feed
section.
Header 2
:
Key
:
X-Webhook-Access-Key
Value
: The secret key you generated in the
Configure a feed in Google SecOps to ingest the Azure Devops logs
section.
Set the
Content-Type
header to
application/json
.
Click
Create
.
Supported Azure DevOps Audit sample logs
Standard Audit JSON
{
"ActivityId"
:
"aeec0738-ebbf-4e62-9a44-83dd7b704e75"
,
"ActorCUID"
:
"e0729319-5632-78c1-9625-b53fe559bcd7"
,
"ActorDisplayName"
:
"User Name"
,
"ActorUPN"
:
"user@example.com"
,
"ActorUserId"
:
"e0729319-5632-68c1-9625-b53fe559bcd7"
,
"Area"
:
"Group"
,
"AuthenticationMechanism"
:
"SessionToken_Unscoped authorizationId: f5729c3d-951b-4a52-88d9-a"
,
"Category"
:
"Modify"
,
"CategoryDisplayName"
:
"Modify"
,
"CorrelationId"
:
"a26a652e-1596-4c83-bb0f-946ff3ccc91c"
,
"Data"
:
{
"CallerProcedure"
:
"prc_UpdateGroupMembership"
,
"EventAuthor"
:
"b33f1e32-f5e3-4210-9fde-6e61f7a761b3"
,
"Idempotent"
:
"True"
,
"Incremental"
:
"True"
,
"InsertInactiveUpdates"
:
"False"
,
"ScopeId"
:
"1b713128-b6f0-4fd7-91af-94ed1f69c464"
,
"Updates"
:
[
{
"GroupId"
:
"BE656E6C-7C01-47DB-BC03-CD7E82610AFE"
,
"MemberId"
:
"9D4E1A54-8B4C-42E2-BECC-94BEDC6E2F4B"
,
"Active"
:
true
}
],
"GroupId"
:
"be656e6c-7c01-47db-bc03-cd7e82610afe"
,
"GroupName"
:
"[Project_Alpha]\\Project Administrators"
,
"MemberId"
:
"9d4e1a54-8b4c-42e2-becc-94bedc6e2f4b"
,
"MemberDisplayName"
:
"Member Name"
},
"Details"
:
"Member Name was added as a member of group [Project_Alpha]\\Project Administrators"
,
"Id"
:
"0b11aadb-0bcc-47ef-9038-b091140dcbe5"
,
"IpAddress"
:
"192.168.1.10"
,
"OperationName"
:
"Group.UpdateGroupMembership.Add"
,
"ProjectId"
:
"00000000-0000-0000-0000-000000000000"
,
"ScopeDisplayName"
:
"Organization_X"
,
"ScopeId"
:
"1b713128-b6f0-4fd7-91af-94ed1f69c464"
,
"ScopeType"
:
"Enterprise"
,
"SourceSystem"
:
"Azure"
,
"TenantId"
:
"5ca654a4-807f-4676-9c9f-0b7335cea18e"
,
"TimeGenerated"
:
"2022-06-20T00:43:35.7370000Z"
,
"Type"
:
"AzureDevOpsAuditing"
,
"UserAgent"
:
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
,
"_Internal_WorkspaceResourceId"
:
"/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg-event-grid/providers/microsoft.operationalinsights/workspaces/logging-workspace"
}
Event Grid Wrapped JSON
{
"id"
:
"9362f75d-b450-47e0-a54b-4fd51d08798e"
,
"subject"
:
"AzureDevOps/Auditing"
,
"data"
:
{
"Id"
:
"9362f75d-b450-47e0-a54b-4fd51d08798e"
,
"CorrelationId"
:
"848f8abd-9f91-479e-857b-454efa0bf393"
,
"ActivityId"
:
"0b7078f1-87bb-441d-8dcc-780c6d0a0511"
,
"ActorCUID"
:
"00000000-0000-0000-0000-000000000000"
,
"ActorUserId"
:
"0000000d-0000-8888-8000-000000000000"
,
"ActorClientId"
:
"00000000-0000-0000-0000-000000000000"
,
"ActorUPN"
:
"Azure DevOps Service"
,
"Timestamp"
:
"2023-08-03T23:34:31.037Z"
,
"ScopeType"
:
4
,
"ScopeDisplayName"
:
"Organization_X"
,
"ScopeId"
:
"1bf2d4d0-3f60-4f08-b217-ce48cebc6816"
,
"ProjectId"
:
"b87f0d76-bb83-4274-a865-5ebdc6fe0500"
,
"ProjectName"
:
"IT_Project"
,
"UserAgent"
:
"TFS JobAgent(TfsJobAgent.exe, 19.224.33927.8)"
,
"ActionId"
:
"Release.DeploymentCompleted"
,
"Data"
:
{
"CallerProcedure"
:
"Release.prc_OnDeploymentCompleted"
,
"DeploymentResult"
:
"Succeeded"
,
"PipelineId"
:
"18"
,
"PipelineName"
:
"digital-client-app-dvlp"
,
"ReleaseName"
:
"23.07.38"
,
"RequesterId"
:
"0000000D-0000-8888-8000-000000000000"
,
"StageName"
:
"Build browser"
},
"Details"
:
"Deployment of release \"23.07.38\" on pipeline \"digital-client-app-dvlp\" to \"Build browser\" in Project IT_Project was Succeeded"
,
"Area"
:
"Release"
,
"Category"
:
5
,
"CategoryDisplayName"
:
"Execute"
,
"ActorDisplayName"
:
"Azure DevOps Service"
},
"eventType"
:
"AzureDevOpsAuditEvent"
,
"dataVersion"
:
"1.0"
,
"metadataVersion"
:
"1"
,
"eventTime"
:
"2023-08-03T23:34:31.037Z"
,
"topic"
:
"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-prod/providers/Microsoft.EventGrid/topics/audit-topic"
}
Event Grid JSON Array
[
{
"id"
:
"14b02dab-67eb-4d9d-acd2-4487aac05b14"
,
"subject"
:
"AzureDevOps/Auditing"
,
"data"
:
{
"Id"
:
"14b02dab-67eb-4d9d-acd2-4487aac05b14"
,
"CorrelationId"
:
"e0475568-bd77-484b-b065-5170561f0bf5"
,
"ActivityId"
:
"a2a70439-18dd-4bbb-be20-2844600feaca"
,
"ActorCUID"
:
"712594c0-94c1-779b-af6c-80752141078d"
,
"ActorUserId"
:
"712594c0-94c1-679b-af6c-80752141078d"
,
"ActorClientId"
:
"00000000-0000-0000-0000-000000000000"
,
"ActorUPN"
:
"user@example.com"
,
"AuthenticationMechanism"
:
"Basic_AAD"
,
"Timestamp"
:
"2023-12-20T18:33:21.9375261Z"
,
"ScopeType"
:
4
,
"ScopeDisplayName"
:
"Organization_X"
,
"ScopeId"
:
"021edafa-0760-4e1d-ba33-00b910e811e9"
,
"ProjectId"
:
"00000000-0000-0000-0000-000000000000"
,
"IpAddress"
:
"10.0.0.50"
,
"UserAgent"
:
"python/3.11.5 (Windows-10-10.0.19045-SP0) msrest/0.7.1 azure-devops/5.1.0b4 devOpsCli/0.25.0"
,
"ActionId"
:
"Security.ModifyPermission"
,
"Data"
:
{
"NamespaceId"
:
"b7e84409-6553-448a-bbb2-af228e07cbeb"
,
"NamespaceName"
:
"Library"
,
"Token"
:
"Library/Collection/VariableGroup/4693"
,
"Permissions"
:
[
{
"baseEntry"
:
{
"descriptor"
:
"Microsoft.TeamFoundation.Identity;S-1-9-1551374245..."
,
"allow"
:
19
,
"deny"
:
0
,
"isEmpty"
:
false
},
"inheritedAllow"
:
0
,
"inheritedDeny"
:
0
,
"effectiveAllow"
:
0
,
"effectiveDeny"
:
0
,
"includesExtendedInfo"
:
false
,
"descriptor"
:
"Microsoft.TeamFoundation.Identity;S-1-9-1551374245..."
,
"allow"
:
19
,
"deny"
:
0
,
"isEmpty"
:
false
}
],
"EventSummary"
:
[
{
"PermissionNames"
:
"View library item"
,
"Change"
:
"allow"
,
"SubjectDescriptor"
:
"Microsoft.TeamFoundation.Identity;S-1-9-1551374245..."
,
"SubjectDisplayName"
:
"[Team_Project]\\Project Administrators"
}
],
"EventSummaryType"
:
"ChangedPermission"
,
"SubjectDisplayName"
:
"[Team_Project]\\Project Administrators"
},
"Details"
:
"3 permissions were modified for [Team_Project]\\Project Administrators"
,
"Area"
:
"Permissions"
,
"Category"
:
1
,
"CategoryDisplayName"
:
"Modify"
,
"ActorDisplayName"
:
"User Name"
},
"eventType"
:
"AzureDevOpsAuditEvent"
,
"dataVersion"
:
"1.0"
,
"metadataVersion"
:
"1"
,
"eventTime"
:
"2023-12-20T18:33:21.9375261Z"
,
"topic"
:
"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-prod/providers/Microsoft.EventGrid/topics/audit-topic"
}
]
UDM Mapping Table
Log Field
UDM Mapping
Logic
ActivityId
metadata.product_log_id
Directly mapped from the
Id
field in the raw log when the
records
field is not present, or from the
ActivityId
field within the
data
object when
records
is present.
ActionId
metadata.product_event_type
Directly mapped from the
ActionId
field within the
data
object.
ActorCUID
additional.fields
Included as an additional field with key "Actor CUID".
ActorDisplayName
principal.user.user_display_name
Directly mapped from the
ActorDisplayName
field if it's not "Azure DevOps Service". If it is "Azure DevOps Service", it's added as a label to
principal.resource.attribute.labels
.
ActorUPN
principal.user.email_addresses
Directly mapped from the
ActorUPN
field if it matches an email address pattern.
ActorUserId
principal.user.userid
Directly mapped from the
ActorUserId
field.
Area
target.application
Used to construct the
target.application
field by prepending "DevOps " to the
Area
value.
AuthenticationMechanism
extensions.auth.auth_details
,
security_result.rule_id
Parsed to extract authentication details and rule ID. The authentication details are mapped to
extensions.auth.auth_details
. The extracted rule ID is mapped to
security_result.rule_id
.
CategoryDisplayName
security_result.action_details
Directly mapped to
security_result.action_details
.
City
principal.location.city
Directly mapped from the
City
field.
Conditions
additional.fields
Added as an additional field with key "Conditions".
Country
principal.location.country_or_region
Directly mapped from the
Country
field.
Data.*
Various
Fields within the
Data
object are mapped to different UDM fields based on their names and context. See below for specific examples.
Data.AccessLevel
target.resource.attribute.labels
Added as a label with key "AccessLevel".
Data.AgentId
target.resource.product_object_id
Mapped to
target.resource.product_object_id
if
PipelineId
and
AuthorizationId
are not present.
Data.AgentName
target.resource.name
Mapped to
target.resource.name
if
PipelineName
,
NamespaceName
, and
DisplayName
are not present.
Data.AuthorizationId
target.resource.product_object_id
Mapped to
target.resource.product_object_id
if
PipelineId
is not present.
Data.CallerProcedure
additional.fields
Added as an additional field with key "CallerProcedure".
Data.CheckSuiteId
additional.fields
Added as an additional field with key "CheckSuiteId".
Data.CheckSuiteStatus
additional.fields
Added as an additional field with key "CheckSuiteStatus".
Data.ConnectionId
additional.fields
Added as an additional field with key "ConnectionId".
Data.ConnectionName
additional.fields
Added as an additional field with key "ConnectionName".
Data.ConnectionType
additional.fields
Added as an additional field with key "ConnectionType".
Data.DefinitionId
additional.fields
Added as an additional field with key "DefinitionId".
Data.DeploymentResult
additional.fields
Added as an additional field with key "DeploymentResult".
Data.DisplayName
target.resource.name
Mapped to
target.resource.name
if
PipelineName
and
NamespaceName
are not present.
Data.EndpointIdList
additional.fields
Added as an additional field with key "EndpointIdList".
Data.EnvironmentName
additional.fields
Added as an additional field with key "EnvironmentName".
Data.Filter.continuationToken
target.resource.attribute.labels
Added as a label with key "continuation_token".
Data.Filter.endTime
target.resource.attribute.labels
Added as a label with key "filter_end_time".
Data.Filter.startTime
target.resource.attribute.labels
Added as a label with key "filter_start_time".
Data.FinishTime
additional.fields
Added as an additional field with key "FinishTime".
Data.GroupId
target.group.product_object_id
Directly mapped to
target.group.product_object_id
when
Data.Updates.0.GroupId
is not present.
Data.GroupName
target.group.group_display_name
Directly mapped to
target.group.group_display_name
.
Data.JobName
additional.fields
Added as an additional field with key "JobName".
Data.MemberId
target.user.userid
Directly mapped to
target.user.userid
when
Data.Updates.0.MemberId
is not present.
Data.MemberDisplayName
target.user.user_display_name
Directly mapped to
target.user.user_display_name
.
Data.NamespaceId
target.resource.product_object_id
Mapped to
target.resource.product_object_id
if
PipelineId
,
AuthorizationId
, and
AgentId
are not present.
Data.NamespaceName
target.resource.name
Mapped to
target.resource.name
if
PipelineName
is not present.
Data.ownerDetails
additional.fields
Added as an additional field with key "OwnerDetails".
Data.OwnerId
additional.fields
Added as an additional field with key "OwnerId".
Data.PipelineId
target.resource.product_object_id
Directly mapped to
target.resource.product_object_id
.
Data.PipelineName
target.resource.name
Directly mapped to
target.resource.name
.
Data.PipelineRevision
target.resource.attribute.labels
Added as a label with key "PipelineRevision".
Data.PipelineScope
target.resource.attribute.labels
Added as a label with key "PipelineScope".
Data.PlanType
additional.fields
Added as an additional field with key "PlanType".
Data.PreviousAccessLevel
target.resource.attribute.labels
Added as a label with key "PreviousAccessLevel".
Data.PublisherName
target.resource.attribute.labels
Added as a label with key "PublisherName".
Data.Reason
additional.fields
Added as an additional field with key "Reason".
Data.ReleaseId
additional.fields
Added as an additional field with key "ReleaseId".
Data.ReleaseName
additional.fields
Added as an additional field with key "ReleaseName".
Data.RequesterId
additional.fields
Added as an additional field with key "RequesterId".
Data.RetentionLeaseId
additional.fields
Added as an additional field with key "RetentionLeaseId".
Data.RetentionOwnerId
additional.fields
Added as an additional field with key "RetentionOwnerId".
Data.RunName
additional.fields
Added as an additional field with key "RunName".
Data.Scopes
target.resource.attribute.labels
Added as labels with key "Scope".
Data.StageName
additional.fields
Added as an additional field with key "StageName".
Data.StartTime
additional.fields
Added as an additional field with key "StartTime".
Data.TargetUser
target.user.userid
Directly mapped to
target.user.userid
.
Data.Timestamp
metadata.event_timestamp
Parsed and mapped to
metadata.event_timestamp
.
Data.TokenType
target.resource.attribute.labels
Added as a label with key "TokenType".
Data.Updates.0.GroupId
target.group.product_object_id
Directly mapped to
target.group.product_object_id
.
Data.Updates.0.MemberId
target.user.userid
Directly mapped to
target.user.userid
.
Data.ValidFrom
target.resource.attribute.labels
Added as a label with key "ValidFrom".
Data.ValidTo
target.resource.attribute.labels
Added as a label with key "ValidTo".
DewPoint
additional.fields
Added as an additional field with key "DewPoint".
Details
metadata.description
Directly mapped to
metadata.description
.
Humidity
additional.fields
Added as an additional field with key "Humidity".
Icon
additional.fields
Added as an additional field with key "Icon".
Id
metadata.product_log_id
Directly mapped to
metadata.product_log_id
.
IpAddress
principal.ip
Directly mapped to
principal.ip
.
MoonPhase
additional.fields
Added as an additional field with key "MoonPhase".
Moonrise
additional.fields
Added as an additional field with key "Moonrise".
Moonset
additional.fields
Added as an additional field with key "Moonset".
OperationName
metadata.product_event_type
Directly mapped to
metadata.product_event_type
.
Precipitation
additional.fields
Added as an additional field with key "Precipitation".
Pressure
additional.fields
Added as an additional field with key "Pressure".
ProjectId
target.resource_ancestors.product_object_id
Used to populate the
product_object_id
field within
target.resource_ancestors
when the ancestor is of type
CLOUD_PROJECT
.
ProjectName
target.resource_ancestors.name
,
target.resource.attribute.labels
Used to populate the
name
field within
target.resource_ancestors
when the ancestor is of type
CLOUD_PROJECT
. Also added as a label to
target.resource.attribute.labels
with key "ProjectName".
RoleLocation
target.location.name
Directly mapped to
target.location.name
.
ScopeDisplayName
target.resource_ancestors.name
Used to populate the
name
field within
target.resource_ancestors
when the ancestor is of type
CLOUD_ORGANIZATION
.
ScopeId
target.resource_ancestors.product_object_id
Used to populate the
product_object_id
field within
target.resource_ancestors
when the ancestor is of type
CLOUD_ORGANIZATION
.
ScopeType
additional.fields
Added as an additional field with key "ScopeType".
Sunrise
additional.fields
Added as an additional field with key "Sunrise".
Sunset
additional.fields
Added as an additional field with key "Sunset".
Temperature
additional.fields
Added as an additional field with key "Temperature".
TenantId
metadata.product_deployment_id
,
additional.fields
Directly mapped to
metadata.product_deployment_id
. Also added as an additional field with key "TenantId".
TimeGenerated
metadata.event_timestamp
Parsed and mapped to
metadata.event_timestamp
.
UserAgent
network.http.user_agent
,
network.http.parsed_user_agent
Directly mapped to
network.http.user_agent
. Also parsed and mapped to
network.http.parsed_user_agent
.
UVIndex
additional.fields
Added as an additional field with key "UVIndex".
Visibility
additional.fields
Added as an additional field with key "Visibility".
WindDirection
additional.fields
Added as an additional field with key "WindDirection".
WindSpeed
additional.fields
Added as an additional field with key "WindSpeed".
_Internal_WorkspaceResourceId
additional.fields
Added as an additional field with key "workspace_resource_id".
N/A
metadata.event_type
Determined by logic based on the
OperationName
and other fields. Defaults to "GENERIC_EVENT" if no specific event type is matched. Possible values include "STATUS_SHUTDOWN", "RESOURCE_CREATION", "STATUS_UPDATE", "USER_RESOURCE_DELETION", "RESOURCE_READ", "RESOURCE_WRITTEN", "RESOURCE_DELETION", and "GROUP_MODIFICATION".
N/A
metadata.vendor_name
Set to "Microsoft".
N/A
metadata.product_name
Set to "Azure DevOps".
N/A
metadata.log_type
Set to "AZURE_DEVOPS".
N/A
principal.user.account_type
Set to "SERVICE_ACCOUNT_TYPE" if
AuthenticationMechanism
contains "ServicePrincipal", otherwise set to "CLOUD_ACCOUNT_TYPE".
N/A
target.asset.attribute.cloud.environment
Set to
MICROSOFT_AZURE
.
N/A
security_result.action
Set to "ALLOW" for successful operations (Succeeded, Created, Modified, executed, updated, removed) and "BLOCK" for failed operations (Failed, TimedOut).
N/A
extensions.auth.mechanism
Set to "USERNAME_PASSWORD" if
summary
is "UserAuthToken".
N/A
target.resource.resource_type
Set to "SETTING" if
pipeline_id
is present, "CREDENTIAL" if
authorization_id
is present, "DEVICE" if
agent_id
is present, or "DATABASE" if
namespace_id
is present. Otherwise, it is set to "STORAGE_BUCKET" in some cases based on
operationName
.
N/A
target.resource.resource_subtype
Set to "Pipeline" if
pipeline_id
is present, "Token" if
authorization_id
is present, "Agent" if
agent_id
is present, or "Namespace" if
namespace_id
is present.
Need more help?
Get answers from Community members and Google SecOps professionals.
