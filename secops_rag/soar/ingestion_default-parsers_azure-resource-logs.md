# Collect Microsoft Azure Resource logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-resource-logs/  
**Scraped:** 2026-03-05T09:58:01.011285Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Azure Resource logs
Supported in:
Google secops
SIEM
This document explains how to collect Microsoft Azure Resource logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.
Azure resource logs provide insight into operations performed within Azure resources. These logs capture detailed information about resource operations, status, and performance metrics. The content varies by resource type and includes data such as authentication events, configuration changes, access attempts, and operational metrics.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to
Microsoft Azure
portal with permissions to:
Create Storage Accounts
Configure Diagnostic Settings for Azure resources
Manage access keys
Configure Azure Storage Account
Create Storage Account
In the
Azure portal
, search for
Storage accounts
.
Click
+ Create
.
Provide the following configuration details:
Setting
Value
Subscription
Select your Azure subscription
Resource group
Select existing or create new
Storage account name
Enter a unique name (for example,
azureresourcelogs
)
Region
Select the region (for example,
East US
)
Performance
Standard (recommended)
Redundancy
GRS (Geo-redundant storage) or LRS (Locally redundant storage)
Click
Review + create
.
Review the overview of the account and click
Create
.
Wait for the deployment to complete.
Get Storage Account credentials
Go to the
Storage Account
you just created.
In the left navigation, select
Access keys
under
Security + networking
.
Click
Show keys
.
Copy and save the following for later use:
Storage account name
:
azureresourcelogs
Key 1
or
Key 2
: The shared access key (a 512-bit random string in base-64 encoding)
Get Blob Service endpoint
In the same Storage Account, select
Endpoints
from the left navigation.
Copy and save the
Blob service
endpoint URL.
Example:
https://azureresourcelogs.blob.core.windows.net/
Configure Azure Resource Diagnostic Settings
Azure resource logs are not collected by default. You must create a diagnostic setting for each Azure resource to route logs to the storage account.
In the
Azure portal
, navigate to the Azure resource you want to monitor.
In the left navigation, select
Diagnostic settings
under
Monitoring
.
Click
+ Add diagnostic setting
.
Provide the following configuration details:
Diagnostic setting name
: Enter a descriptive name (for example,
export-to-secops
).
In the
Logs
section, select the log categories you want to collect. The available categories vary by resource type. Common categories include:
Administrative
(for Activity Logs)
Security
(for Activity Logs)
AuditEvent
(for Key Vault)
ApplicationGatewayAccessLog
(for Application Gateway)
ApplicationGatewayFirewallLog
(for Application Gateway)
NetworkSecurityGroupEvent
(for Network Security Groups)
In the
Metrics
section (optional), select
AllMetrics
to send platform metrics to the storage account.
In the
Destination details
section, select
Archive to a storage account
checkbox.
Subscription
: Select the subscription containing your storage account.
Storage account
: Select the storage account you created (for example,
azureresourcelogs
).
Click
Save
.
After configuration, logs are automatically exported to containers in the storage account. Azure creates containers using the naming pattern
insights-logs-<log-category-name>
. For example:
Key Vault audit logs:
insights-logs-auditevent
Application Gateway access logs:
insights-logs-applicationgatewayaccesslog
Application Gateway firewall logs:
insights-logs-applicationgatewayfirewalllog
Network Security Group events:
insights-logs-networksecuritygroupevent
Configure a feed in Google SecOps to ingest Azure Resource logs
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
Azure Resource Logs - Key Vault
).
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
Microsoft Azure Resource
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Azure URI
: Enter the Blob Service endpoint URL with the container path:
https://azureresourcelogs.blob.core.windows.net/insights-logs-auditevent/
Replace the following:
azureresourcelogs
: Your Azure storage account name.
insights-logs-auditevent
: The blob container name where logs are stored (varies by resource type and log category).
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers.
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Shared key
: Enter the shared key value (access key) you captured from the Storage Account in step 3.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Configure Azure Storage firewall (if enabled)
If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.
In the
Azure portal
, go to your
Storage Account
(for example,
azureresourcelogs
).
Select
Networking
under
Security + networking
.
Under
Firewalls and virtual networks
, select
Enabled from selected virtual networks and IP addresses
.
In the
Firewall
section, under
Address range
, click
+ Add IP range
.
Add each Google SecOps IP range in CIDR notation.
To get the current IP ranges, choose one of the following options:
See
IP Allowlisting documentation
Retrieve them programmatically using the
Feed Management API
Click
Save
.
Supported Microsoft Azure Activity sample logs
Standard Azure Active Directory
{
"time"
:
"2023-11-23T11:27:52.4984929Z"
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
"None"
,
"durationMs"
:
0
,
"callerIpAddress"
:
"0.0.0.0"
,
"correlationId"
:
"00000000-0000-0000-0000-000000000000"
,
"identity"
:
"Masked User"
,
"Level"
:
4
,
"location"
:
"OM"
,
"properties"
:
{
"id"
:
"00000000-0000-0000-0000-000000000000"
,
"createdDateTime"
:
"2023-11-23T11:26:02.4737491+00:00"
,
"userDisplayName"
:
"Masked User"
,
"userPrincipalName"
:
"user@example.com"
,
"userId"
:
"00000000-0000-0000-0000-000000000000"
,
"appId"
:
"00000000-0000-0000-0000-000000000000"
,
"appDisplayName"
:
"QuestProd"
,
"ipAddress"
:
"0.0.0.0"
,
"status"
:
{
"errorCode"
:
0
},
"clientAppUsed"
:
"Browser"
,
"userAgent"
:
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
,
"deviceDetail"
:
{
"deviceId"
:
"00000000-0000-0000-0000-000000000000"
,
"displayName"
:
"MASKED-DEVICE"
,
"operatingSystem"
:
"Windows10"
,
"browser"
:
"Chrome 119.0.0"
,
"isManaged"
:
true
,
"trustType"
:
"Hybrid Azure AD joined"
},
"location"
:
{
"city"
:
"Masked City"
,
"state"
:
"Masked State"
,
"countryOrRegion"
:
"OM"
,
"geoCoordinates"
:
{
"latitude"
:
0.0
,
"longitude"
:
0.0
}
},
"correlationId"
:
"00000000-0000-0000-0000-000000000000"
,
"conditionalAccessStatus"
:
"success"
}
}
Azure Diagnostic with Embedded JSON
{
"operationName"
:
"Microsoft.ContainerService/managedClusters/diagnosticLogs/Read"
,
"category"
:
"kube-audit-admin"
,
"ccpNamespace"
:
"62608a387c46f70001a06545"
,
"resourceId"
:
"/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/MASKED-RG/PROVIDERS/MICROSOFT.CONTAINERSERVICE/MANAGEDCLUSTERS/MASKED-CLUSTER"
,
"properties"
:
{
"log"
:
{
"kind"
:
"Event"
,
"apiVersion"
:
"audit.k8s.io/v1"
,
"level"
:
"Metadata"
,
"auditID"
:
"00000000-0000-0000-0000-000000000000"
,
"stage"
:
"ResponseComplete"
,
"requestURI"
:
"/api/v1/namespaces/external-secrets/configmaps/external-secrets-controller"
,
"verb"
:
"update"
,
"user"
:
{
"username"
:
"system:serviceaccount:external-secrets:external-secrets"
,
"uid"
:
"00000000-0000-0000-0000-000000000000"
,
"groups"
:
[
"system:serviceaccounts"
,
"system:serviceaccounts:external-secrets"
,
"system:authenticated"
],
"extra"
:
{
"authentication.kubernetes.io/pod-name"
:
[
"external-secrets-56f8d94c7b-mp66g"
],
"authentication.kubernetes.io/pod-uid"
:
[
"00000000-0000-0000-0000-000000000000"
]
}
},
"sourceIPs"
:
[
"0.0.0.0"
],
"userAgent"
:
"external-secrets/v0.0.0 (linux/amd64) kubernetes/$Format/leader-election"
,
"objectRef"
:
{
"resource"
:
"configmaps"
,
"namespace"
:
"external-secrets"
,
"name"
:
"external-secrets-controller"
,
"uid"
:
"00000000-0000-0000-0000-000000000000"
,
"apiVersion"
:
"v1"
,
"resourceVersion"
:
"11942456"
},
"responseStatus"
:
{
"metadata"
:
{},
"code"
:
200
},
"requestReceivedTimestamp"
:
"2022-05-20T11:31:45.398328Z"
,
"stageTimestamp"
:
"2022-05-20T11:31:45.449142Z"
,
"annotations"
:
{
"authorization.k8s.io/decision"
:
"allow"
,
"authorization.k8s.io/reason"
:
"RBAC: allowed by RoleBinding \"external-secrets-leaderelection/external-secrets\" of Role \"external-secrets-leaderelection\" to ServiceAccount \"external-secrets/external-secrets\""
}
},
"stream"
:
"stdout"
,
"pod"
:
"kube-apiserver-776c8d479f-xgsg4"
},
"time"
:
"2022-05-20T11:31:45.0000000Z"
,
"Cloud"
:
"AzureCloud"
,
"Environment"
:
"prod"
,
"UnderlayClass"
:
"hcp-underlay"
,
"UnderlayName"
:
"hcp-underlay-southcentralus-cx-75"
}
Third-Party Wrapper
{
"_time"
:
1722359281.368
,
"_raw"
:
{
"time"
:
"2024-07-30T17:08:01.3688943Z"
,
"resourceId"
:
"/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/MASKED-RG/PROVIDERS/"
+
"MICROSOFT.DOCUMENTDB/DATABASEACCOUNTS/MASKED-COSMOS-DB"
,
"category"
:
"DataPlaneRequests"
,
"operationName"
:
"Create"
,
"properties"
:
{
"activityId"
:
"8e78e651-e6da-4f09-b8bf-c5d605ae8161"
,
"requestResourceType"
:
"Document"
,
"requestResourceId"
:
"/dbs/cdb-main01-prod/colls/Notifications/docs"
,
"collectionRid"
:
""
,
"databaseRid"
:
""
,
"statusCode"
:
"200"
,
"duration"
:
"0.583700"
,
"userAgent"
:
"cosmos-netstandard-sdk/3.9.1|3.9.0|01|X86|Microsoft Windows 10.0.20348|"
+
".NET Core 3.1.32|"
,
"clientIpAddress"
:
"0.0.0.0"
,
"requestCharge"
:
"0.000000"
,
"requestLength"
:
"803"
,
"responseLength"
:
"1163"
,
"resourceTokenPermissionId"
:
""
,
"resourceTokenPermissionMode"
:
""
,
"resourceTokenUserRid"
:
""
,
"region"
:
"East US"
,
"partitionId"
:
""
,
"aadAppliedRoleAssignmentId"
:
""
,
"aadPrincipalId"
:
""
,
"authTokenType"
:
"PrimaryMasterKey"
,
"keyType"
:
"PrimaryMasterKey"
,
"connectionMode"
:
"Gateway"
,
"subscriptionId"
:
"00000000-0000-0000-0000-000000000000"
,
"databaseName"
:
"cdb-main01-prod"
,
"collectionName"
:
"Notifications"
}
},
"cribl_pipe"
:
[
"pfe_azure_resource_logs_pre_unroll"
,
"passthru"
]
}
Azure Firewall
{
"category"
:
"AzureFirewallNetworkRule"
,
"time"
:
"2023-10-01T12:00:00.000Z"
,
"resourceId"
:
"/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/MASKED-RG/PROVIDERS/"
+
"MICROSOFT.NETWORK/AZUREFIREWALLS/MASKED-FW"
,
"operationName"
:
"AzureFirewallNetworkRuleLog"
,
"properties"
:
{
"msg"
:
"TCP request from 0.0.0.0:12345 to 0.0.0.0:443. Action: Deny. "
+
"Rule Collection: Block-Internet. Rule: Block-All"
,
"Action"
:
"Deny"
,
"Protocol"
:
"TCP"
,
"SourceIp"
:
"0.0.0.0"
,
"SourcePort"
:
"12345"
,
"DestinationIp"
:
"0.0.0.0"
,
"DestinationPort"
:
"443"
,
"Policy"
:
"Block-Internet"
}
}
UDM mapping table
Log Field
UDM Mapping
Logic
various additional
field
*_label fields
additional.fields
Merged from various additional
field
*_label fields
authenticationMethod
extensions.auth.mechanism
Set to USERNAME_PASSWORD if authenticationMethod is Password
category, event_type
extensions.auth.type
Set to MACHINE for SQLSecurityAuditEvents; SSO for specific categories; AUTHTYPE_UNSPECIFIED for others
properties.partialipaddress
intermediary.ip
Value from properties.partialipaddress if not empty
properties.event_time, stage_time, risk_time, last_update_time, time
metadata.collected_timestamp
Converted using ISO8601 from properties.event_time, or from stage_time, or from risk_time, or from last_update_time, or from time with fallback grok
properties.message, properties.activity, properties.log.stage
metadata.description
Value from properties.message if not empty; else from properties.activity; else from properties.log.stage
event_type
metadata.event_type
Value from event_type if not empty, else GENERIC_EVENT
category, record.category
metadata.product_event_type
Value copied directly from category or record.category
properties.event_id, properties.log.auditID
metadata.product_log_id
Value from properties.event_id if not empty; else from properties.log.auditID
properties.log.apiVersion
metadata.product_version
Value copied directly from properties.log.apiVersion
protocol
network.application_protocol
Value copied directly from protocol
properties.log.verb
network.dhcp.opcode
Value copied directly from properties.log.verb (uppercase)
properties.CsMethod, record.properties.CsMethod
network.http.method
Value copied directly from properties.CsMethod or record.properties.CsMethod
user_agent
network.http.parsed_user_agent
Converted from user_agent
properties.Referer, uri
network.http.referral_url
Value from properties.Referer if not empty; else from uri
properties.ScStatus, record.properties.ScStatus, properties.statusCode, record.properties.statusCode, responseStatus.code
network.http.response_code
Converted to integer from properties.ScStatus, record.properties.ScStatus, properties.statusCode, record.properties.statusCode, or responseStatus.code
user_agent
network.http.user_agent
Value copied directly from user_agent
properties.ScBytes, record.properties.ScBytes, properties.responseLength
network.received_bytes
Converted to uinteger from properties.ScBytes, record.properties.ScBytes, or properties.responseLength
properties.CsBytes, record.properties.CsBytes, properties.requestLength
network.sent_bytes
Converted to uinteger from properties.CsBytes, record.properties.CsBytes, or properties.requestLength
properties.session_id
network.session_id
Value copied directly from properties.session_id (converted to string)
properties.tlsVersion
network.tls.version
Value copied directly from properties.tlsVersion
domain_name_value
principal.administrative_domain
Value copied directly from domain_name_value
properties.clientAppUsed, target_application
principal.application
Value from properties.clientAppUsed if not empty; else from target_application
prop_device_id
principal.asset.asset_id
Set to Device ID: followed by prop_device_id if not null
hardware
principal.asset.hardware
Merged from hardware
properties.host_name, properties.CIp, record.properties.CIp, properties.ComputerName, record.properties.ComputerName, properties.CsHost, record.properties.CsHost, properties.server_instance_name, record.properties.server_instance_name, server_name
principal.asset.hostname
Value from properties.host_name if not empty; else from properties.CIp (grok IP), record.properties.CIp (grok IP), properties.ComputerName, record.properties.ComputerName, properties.CsHost, record.properties.CsHost, properties.server_instance_name, record.properties.server_instance_name, or server_name
src_ip, src_ip1, properties.client_ip, record.properties.clientIpAddress, properties.clientIpAddress, callerIpAddress, properties.ipAddress, ip
principal.asset.ip
Value from src_ip, src_ip1, properties.client_ip (grok IP), record.properties.clientIpAddress, properties.clientIpAddress (grok IP), record.properties.clientIpAddress, callerIpAddress (grok IP), properties.ipAddress, or ip
properties.host_name, properties.CsHost, record.properties.CsHost
principal.hostname
Value from properties.host_name if not empty; else from properties.CsHost or record.properties.CsHost
src_ip, src_ip1, properties.client_ip, record.properties.clientIpAddress, properties.clientIpAddress, callerIpAddress, properties.ipAddress, ip
principal.ip
Value from src_ip, src_ip1, properties.client_ip (grok IP), record.properties.clientIpAddress, properties.clientIpAddress (grok IP), record.properties.clientIpAddress, callerIpAddress (grok IP), properties.ipAddress, or ip
properties.location.city, provisioning_steps_city
principal.location.city
Value from properties.location.city if not empty; else from provisioning_steps_city
properties.location.countryOrRegion, provisioning_steps_country, location, Region
principal.location.country_or_region
Value from properties.location.countryOrRegion if not empty; else from provisioning_steps_country; else from location; else from Region
properties.location.geoCoordinates.latitude
principal.location.region_latitude
Value copied directly from properties.location.geoCoordinates.latitude
properties.location.geoCoordinates.longitude
principal.location.region_longitude
Value copied directly from properties.location.geoCoordinates.longitude
properties.location.state
principal.location.state
Value copied directly from properties.location.state
prop_os
principal.platform
Set to WINDOWS if prop_os matches (?i)Win; LINUX if (?i)Lin; MAC if (?i)Mac
properties.deviceDetail.operatingSystem
principal.platform_version
Value copied directly from properties.deviceDetail.operatingSystem
src_port
principal.port
Converted to integer from src_port
is_compliant_label, is_managed_label, serice_type_label, serice_credential_label
principal.resource.attribute.labels
Merged from is_compliant_label, is_managed_label, serice_type_label, serice_credential_label
properties.sourceSystem.Name
principal.resource.name
Value copied directly from properties.sourceSystem.Name
properties.sourceSystem.Id
principal.resource.product_object_id
Value copied directly from properties.sourceSystem.Id
properties.server_principal_name, source_user_principal_name, user_principal_name, local_account_username_value
principal.user.email_addresses
Merged from properties.server_principal_name (if matches email), source_user_principal_name (if matches email), user_principal_name (if matches email), or local_account_username_value (if matches email)
properties.sequence_group_id, grpname, properties.log.user.groups
principal.user.group_identifiers
Merged from properties.sequence_group_id, grpname, or properties.log.user.groups
properties.sourceIdentity.details.id, properties.userId, details_id_not_present
principal.user.product_object_id
Value from properties.sourceIdentity.details.id if not empty; else from properties.userId; else from details_id_not_present
properties.ServicePrincipalDisplayName, properties.servicePrincipalName, properties.sourceIdentity.details.DisplayName, properties.userDisplayName, record.properties.log.user.username
principal.user.user_display_name
Value from properties.ServicePrincipalDisplayName if not empty; else from properties.servicePrincipalName; else from properties.sourceIdentity.details.DisplayName; else from properties.userDisplayName; else from record.properties.log.user.username
properties.servicePrincipalId, user_userPrincipalName, source_user_principal_name, details_user_principal_name, user_principal_name, properties.accountName, record.properties.log.user.uid
principal.user.userid
Value from properties.servicePrincipalId if not empty; else from user_userPrincipalName; else from source_user_principal_name; else from details_user_principal_name; else from user_principal_name; else from properties.accountName; else from record.properties.log.user.uid
security_action, succeeded, statusText, resultType
security_result.action
Set to ALLOW if security_action is allow; else ALLOW if succeeded true or statusText Success or resultType success; else BLOCK if succeeded false or statusText failed or resultType failed
properties.action_name
security_result.action_details
Value copied directly from properties.action_name
status_label
security_result.about.resource.attribute.labels
Merged from status_label
properties_log_label, corr_key_label, resultType_label, resultSignature_label, networkName_label, networkType_label, method_label, authentication_step_requirement_label, authentication_step_result_detail_label, stepdate_label, initiatedby_name_label, initiatedby_id_label, initiatedby_type_label, targetSystem_id_label, targetSystem_name_label, containerID_label, pod_label, authentication_label, api_name_label, scale_unit_label, namespace_name_label, subscription_id_label, activity_id_label_1, task_name_label, environment_label, cookie, additional_field_event_ip, additional_field_event_primary_stamp, additional_field_event_stamp_type, source, correlationId_field, activityDateTime_field, detectedDateTime_field, lastUpdatedDateTime_field, count_label, total_label, minimum_label, maximum_label, average_label, metricName_label, timeGrain_label, ApiName_label, Authentication_label, GeoType_label, old_label, new_label, add_label, keyId_label, sr_result.rule_name, sr_result.rule_id, resultField, sr_result.detection_fields
security_result.detection_fields
Merged from properties_log_label, corr_key_label, resultType_label, resultSignature_label, networkName_label, networkType_label, method_label, authentication_step_requirement_label, authentication_step_result_detail_label, stepdate_label, initiatedby_name_label, initiatedby_id_label, initiatedby_type_label, targetSystem_id_label, targetSystem_name_label, containerID_label, pod_label, authentication_label, api_name_label, scale_unit_label, namespace_name_label, subscription_id_label, activity_id_label_1, task_name_label, environment_label, cookie, additional_field_event_ip, additional_field_event_primary_stamp, additional_field_event_stamp_type, source, correlationId_field, activityDateTime_field, detectedDateTime_field, lastUpdatedDateTime_field, count_label, total_label, minimum_label, maximum_label, average_label, metricName_label, timeGrain_label, ApiName_label, Authentication_label, GeoType_label, old_label, new_label, add_label, keyId_label, sr_result.rule_name, sr_result.rule_id, resultField, sr_result.detection_fields
resultDescription, sec_result.description, properties.queryexecutionstatus
security_result.description
Value from resultDescription (gsub newlines); else from sec_result.description; else from properties.queryexecutionstatus
policy_id_value
security_result.rule_id
Value copied directly from policy_id_value
properties.Result, statusText, properties.queryexecutionstatus
security_result.summary
Value from properties.Result if not empty; else from statusText; else from properties.queryexecutionstatus
target_application
target.application
Value from target_application
properties.ComputerName, record.properties.ComputerName, properties.server_instance_name, record.properties.server_instance_name
target.asset.hostname
Value from properties.ComputerName, record.properties.ComputerName, properties.server_instance_name, or record.properties.server_instance_name
(hardcoded)
target.cloud.environment
Set to "MICROSOFT_AZURE"
properties.SPort, record.properties.SPort
target.port
Converted to integer from properties.SPort or record.properties.SPort
properties.querytext.query
target.process.command_line
Value copied directly from properties.querytext.query
properties.processId
target.process.pid
Converted to string from properties.processId
subscription_id_label, resource_group_label, request_resource_type_label, request_resource_id_label, additional_objectKey, additional_clientRequestId, additional_RiskEventType, additional_tokenIssuerType, keyId_label, appid_label
target.resource.attribute.labels
Merged from subscription_id_label, resource_group_label, request_resource_type_label, request_resource_id_label, additional_objectKey, additional_clientRequestId, additional_RiskEventType, additional_tokenIssuerType, keyId_label, appid_label
properties_databasename, properties.resourceDisplayName, record.properties.databasename, record.properties.databaseName
target.resource.name
Value from properties_databasename if not empty; else from properties.resourceDisplayName; else from record.properties.databasename; else from record.properties.databaseName
resourceId, properties.resourceId
target.resource.product_object_id
Value from resourceId if not empty; else from properties.resourceId
properties_collectionname, properties.resourceDisplayName, record.properties.collectionname, record.properties.collectionName, properties.log.objectRef.resource
target.resource.resource_subtype
Value from properties_collectionname if not empty; else from properties.resourceDisplayName; else from record.properties.collectionname; else from record.properties.collectionName; else from properties.log.objectRef.resource
resourceId, message
target.resource.resource_type
Set to DATABASE if resourceId matches pattern; else CLUSTER if message matches MANAGEDCLUSTERS; else VIRTUAL_MACHINE if MANAGEDINSTANCES; else DATABASE if DATABASEACCOUNTS
resourceType
target.resource.type
Value copied directly from resourceType
properties.CsUriStem, properties.log.requestURI, value (from additionalInfo)
target.url
Value from properties.CsUriStem if not empty; else from properties.log.requestURI; else from value (from additionalInfo)
user_principal_name
target.user.email_addresses
Merged from user_principal_name (if matches email)
properties.userId
target.user.product_object_id
Value copied directly from properties.userId
properties.userDisplayName
target.user.user_display_name
Value copied directly from properties.userDisplayName
user_principal_name, properties.userPrincipalName
target.user.userid
Value from user_principal_name if not empty; else from properties.userPrincipalName
(hardcoded)
metadata.product_name
Set to "Azure Resource Logs"
(hardcoded)
metadata.vendor_name
Set to "Microsoft"
Need more help?
Get answers from Community members and Google SecOps professionals.
