# Collect Microsoft Azure Key Vault logging logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-keyvault-audit/  
**Scraped:** 2026-03-05T09:26:22.364356Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Azure Key Vault logging logs
Supported in:
Google secops
SIEM
This document describes how you can collect the Azure Key Vault logging logs by setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google SecOps
.
An ingestion label identifies the parser which normalizes raw log data to structured
UDM format. The information in this document applies to the parser with the
AZURE_KEYVAULT_AUDI
ingestion label.
Before you begin
Ensure that you have the following prerequisites:
Azure subscription that you can sign in to
Azure Key Vault environment (tenant) in Azure
Global administrator or Azure Key Vault administrator role
Azure storage account to store the logs
Configure a storage account
Sign in to the
Azure
portal.
In the
Azure
console, search for
Storage accounts
.
Select the storage account that the logs must be pulled from, and then select
Access key
. To create a new storage account, do the following:
Click
Create.
Enter a name for the new storage account.
Select the subscription, resource group, region, performance, and redundancy for the account. We recommend setting the performance to
standard
, and the redundancy to
GRS
or
LRS
.
Click
Review + create
.
Review the overview of the account and click
Create.
Click
Show keys
and make a note of the shared key for the storage account.
Select
Endpoints
and make a note of the
Blob service
endpoint.
For more information about creating a storage account, see the
Create an Azure storage account
section in the
Microsoft documentation
.
Configure Azure Key Vault logging
In the
Azure
portal, go to
Key vaults
and select the key vault that you want to configure for logging.
In the
Monitoring
section, select
Diagnostic settings
.
Select
Add diagnostic setting
. The
Diagnostics settings
window provides the settings for the diagnostic logs.
In the
Diagnostic setting name
field, specify the name for diagnostic setting.
In the
Category groups
section, select the
audit
checkbox.
In the
Retention (days)
field, specify a log retention value that complies with your organization's policies.
Google SecOps recommends a minimum of one day of log retention.
You can store the Azure Key Vault logging logs in a storage account or stream the logs to Event Hubs. Google SecOps supports log collection using a storage account.
Archive to a storage account
To store logs in storage account, in the
Diagnostics settings
window, select the
Archive to a storage account
checkbox.
In the
Subscription
list, select the existing subscription.
In the
Storage account
list, select the existing storage account.
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
How to set up the Azure key vault logging feed
Click the
Azure Platform
pack.
Locate the
Azure Key Vault logging
log type and click
Add new feed
.
Specify values for the following fields:
Source Type
:
Microsoft Azure Blob Storage V2
.
Azure URI
: specify the
Blob service
endpoint that you obtained previously along with one of the container names of that storage account. For example,
https://xyz.blob.core.windows.net/abc/
.
Source deletion option
: specify the source deletion option.
Maximum File Age
: Includes files modified in the last number of days. 
Default is 180 days.
Key
: specify the shared key that you obtained previously.
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
For more information about Google SecOps feeds, see
Google SecOps feeds documentation
.
For information about requirements for each feed type, see
Feed configuration by type
.
Supported Microsoft Azure Key Vault logging sample logs
Azure Key Vault Audit
{
"time"
:
"2024-02-01T10:34:54.5732801Z"
,
"category"
:
"AuditEvent"
,
"operationName"
:
"Authentication"
,
"resultType"
:
"Success"
,
"correlationId"
:
"00000000-0000-0000-0000-000000000000"
,
"callerIpAddress"
:
"127.0.0.1"
,
"identity"
:
{},
"properties"
:
{
"clientInfo"
:
"azsdk-net-Security.KeyVault.Secrets/4.5.0 (.NET Framework 4.8.4645.0; Microsoft Windows 10.0.20348 )"
,
"httpStatusCode"
:
401
,
"requestUri"
:
"https://example-vault.vault.azure.net/secrets/?api-version=7.4"
,
"tlsVersion"
:
"TLS1_3"
},
"resourceId"
:
"/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/EXAMPLE-RG/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/EXAMPLE-VAULT"
,
"operationVersion"
:
"7.4"
,
"resultSignature"
:
"Unauthorized"
,
"durationMs"
:
"17"
}
Azure Diagnostics
{
"TenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"TimeGenerated"
:
"2025-01-07T20:00:00.0483028Z"
,
"ResourceId"
:
"/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/EXAMPLE-RG/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/EXAMPLE-VAULT"
,
"Category"
:
"AuditEvent"
,
"ResourceGroup"
:
"EXAMPLE-RG"
,
"SubscriptionId"
:
"00000000-0000-0000-0000-000000000000"
,
"ResourceProvider"
:
"MICROSOFT.KEYVAULT"
,
"Resource"
:
"EXAMPLE-VAULT"
,
"ResourceType"
:
"VAULTS"
,
"OperationName"
:
"SecretGet"
,
"ResultType"
:
"Success"
,
"CorrelationId"
:
"00000000-0000-0000-0000-000000000000"
,
"ResultDescription"
:
""
,
"requestUri_s"
:
"https://example-vault.vault.azure.net/secrets/example-secret/?api-version=7.3"
,
"DurationMs"
:
16
,
"CallerIPAddress"
:
"127.0.0.1"
,
"OperationVersion"
:
"7.3"
,
"ResultSignature"
:
"OK"
,
"id_s"
:
"https://example-vault.vault.azure.net/secrets/example-secret/00000000000000000000000000000000"
,
"clientInfo_s"
:
"azsdk-net-Security.KeyVault.Secrets/4.3.0 (.NET 6.0.35; Microsoft Windows 10.0.14393)"
,
"httpStatusCode_d"
:
200
,
"identity_claim_appid_g"
:
"00000000-0000-0000-0000-000000000000"
,
"isAccessPolicyMatch_b"
:
true
,
"identity_claim_oid_g"
:
"00000000-0000-0000-0000-000000000000"
,
"identity_claim_appidacr_s"
:
"2"
,
"identity_claim_xms_az_nwperimid_s"
:
"[]"
,
"identity_claim_idtyp_s"
:
"app"
,
"tlsVersion_s"
:
"TLS1_2"
,
"Type"
:
"AzureDiagnostics"
,
"_ResourceId"
:
"/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/example-rg/providers/microsoft.keyvault/vaults/example-vault"
}
Azure Resource Graph
{
"value"
:
[
{
"TenantId"
:
"00000000-0000-0000-0000-000000000000"
,
"TimeGenerated"
:
"2024-11-02T09:12:25.0852453Z"
,
"ResourceId"
:
"/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/EXAMPLE-RG/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/EXAMPLE-VAULT"
,
"Category"
:
"AuditEvent"
,
"ResourceGroup"
:
"EXAMPLE-RG"
,
"SubscriptionId"
:
"00000000-0000-0000-0000-000000000000"
,
"ResourceProvider"
:
"MICROSOFT.KEYVAULT"
,
"Resource"
:
"EXAMPLE-VAULT"
,
"ResourceType"
:
"VAULTS"
,
"OperationName"
:
"VaultGet"
,
"ResultType"
:
"Success"
,
"CorrelationId"
:
"00000000-0000-0000-0000-000000000000"
,
"ResultDescription"
:
""
,
"requestUri_s"
:
"https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.KeyVault/vaults/example-vault?api-version=2023-07-01&MaskCMKEnabledProperties=true"
,
"DurationMs"
:
30
,
"CallerIPAddress"
:
"127.0.0.1"
,
"OperationVersion"
:
"2023-07-01"
,
"ResultSignature"
:
"OK"
,
"id_s"
:
"https://example-vault.vault.azure.net/"
,
"clientInfo_s"
:
"AzureResourceGraph.IngestionWorkerService.global/1.24.1.672"
,
"httpStatusCode_d"
:
200
,
"identity_claim_appid_g"
:
"00000000-0000-0000-0000-000000000000"
,
"identity_claim_http_schemas_microsoft_com_identity_claims_objectidentifier_g"
:
"00000000-0000-0000-0000-000000000000"
,
"properties_sku_Family_s"
:
"A"
,
"properties_sku_Name_s"
:
"standard"
,
"properties_tenantId_g"
:
"00000000-0000-0000-0000-000000000000"
,
"properties_enabledForDeployment_b"
:
false
,
"properties_enabledForTemplateDeployment_b"
:
false
,
"properties_enabledForDiskEncryption_b"
:
false
,
"properties_enableSoftDelete_b"
:
true
,
"properties_enableRbacAuthorization_b"
:
false
,
"properties_enablePurgeProtection_b"
:
true
,
"Type"
:
"AzureDiagnostics"
,
"_ResourceId"
:
"/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/example-rg/providers/microsoft.keyvault/vaults/example-vault"
}
]
}
Need more help?
Get answers from Community members and Google SecOps professionals.
