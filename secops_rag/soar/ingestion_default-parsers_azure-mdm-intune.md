# Collect Azure MDM Intune logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune/  
**Scraped:** 2026-03-05T09:58:09.615963Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure MDM Intune logs
Supported in:
Google secops
SIEM
This document explains how to collect Microsoft Azure Intune logs to Google Security Operations. You can configure ingestion using two methods: the Third Party API (recommended) or Microsoft Azure Blob Storage V2.
Microsoft Intune is a cloud-based endpoint management solution that manages user access to organizational resources and simplifies app and device management across devices including mobile devices, desktop computers, and virtual endpoints.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to the
Microsoft Azure
portal
A user with the
Intune Administrator
or
Global Administrator
Microsoft Entra role for the Intune tenant
An active Intune license for the tenant
Method 1: Third Party API (recommended)
This method uses the Microsoft Graph API to retrieve Intune audit and operational logs directly from your Microsoft tenant.
Configure Microsoft Entra app registration
Create app registration
Sign in to the
Microsoft Entra admin center
or
Azure portal
.
Go to
Identity
>
Applications
>
App registrations
.
Click
New registration
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Intune Integration
).
Supported account types
: Select
Accounts in this organizational directory only (Single tenant)
.
Redirect URI
: Leave blank (not required for service principal authentication).
Click
Register
.
After registration, copy and save the following values from the
Overview
page:
Application (client) ID
Directory (tenant) ID
Configure API permissions
In the app registration, go to
API permissions
.
Click
Add a permission
.
Select
Microsoft Graph
>
Application permissions
.
Search for and select the following permissions:
DeviceManagementApps.Read.All
DeviceManagementConfiguration.Read.All
DeviceManagementManagedDevices.Read.All
DeviceManagementServiceConfig.Read.All
DeviceManagementRBAC.Read.All
Click
Add permissions
.
Click
Grant admin consent for [Your Organization]
.
Verify that the
Status
column shows
Granted for [Your Organization]
for all permissions.
Required API permissions
Permission
Type
Purpose
DeviceManagementApps.Read.All
Application
Read app management data and audit events
DeviceManagementConfiguration.Read.All
Application
Read device configuration and compliance policies
DeviceManagementManagedDevices.Read.All
Application
Read managed device information
DeviceManagementServiceConfig.Read.All
Application
Read Intune service configuration
DeviceManagementRBAC.Read.All
Application
Read role-based access control settings
Create client secret
In the app registration, go to
Certificates & secrets
.
Click
New client secret
.
Provide the following configuration details:
Description
: Enter a descriptive name (for example,
Google SecOps Feed
).
Expires
: Select an expiration period.
Click
Add
.
Copy the client secret
Value
immediately.
Configure a feed in Google SecOps to ingest Microsoft Intune logs
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
Microsoft Intune Logs
).
Select
Third Party API
as the
Source type
.
Select
Microsoft Intune
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
OAuth Client ID
: Enter the
Application (client) ID
from the app registration (for example,
1234abcd-1234-abcd-1234-abcd1234abcd
).
OAuth Client Secret
: Enter the
client secret value
you copied earlier.
Tenant ID
: Enter the
Directory (tenant) ID
from the app registration in UUID format (for example,
0fc279f9-fe30-41be-97d3-abe1d7681418
).
API Full Path
: Enter the Microsoft Graph REST API endpoint URL. Default value:
graph.microsoft.com/beta/deviceManagement/auditEvents
API Authentication Endpoint
: Enter the Microsoft Active Directory authentication endpoint. Default value:
login.microsoftonline.com
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
After setup, the feed begins to retrieve Intune audit and operational logs from the Microsoft Graph API.
Regional endpoints
For Microsoft Intune deployments in sovereign clouds, use the appropriate regional endpoints:
Cloud Environment
API Full Path
API Authentication Endpoint
Global
graph.microsoft.com/beta/deviceManagement/auditEvents
login.microsoftonline.com
US Government L4
graph.microsoft.us/beta/deviceManagement/auditEvents
login.microsoftonline.us
US Government L5 (DOD)
dod-graph.microsoft.us/beta/deviceManagement/auditEvents
login.microsoftonline.us
China (21Vianet)
microsoftgraph.chinacloudapi.cn/beta/deviceManagement/auditEvents
login.chinacloudapi.cn
Method 2: Microsoft Azure Blob Storage V2
This method collects Microsoft Intune logs by exporting diagnostic data to an Azure Storage Account and configuring a Google SecOps feed to ingest from Azure Blob Storage.
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
intunelogs
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
Review the overview and click
Create
.
Wait for the deployment to complete.
Get Storage Account credentials
Go to the
Storage Account
you created.
In the left navigation, select
Access keys
under
Security + networking
.
Click
Show keys
.
Copy and save the following:
Storage account name
: The name you provided during creation.
Key 1
or
Key 2
: The shared access key.
Get Blob Service endpoint
In the same Storage Account, select
Endpoints
from the left navigation.
Copy and save the
Blob service
endpoint URL.
Example:
https://intunelogs.blob.core.windows.net/
Configure Microsoft Intune Diagnostic Settings
Sign in to the
Microsoft Intune admin center
.
Select
Reports
>
Diagnostic settings
.
Click
Add diagnostic setting
.
Provide the following configuration details:
Diagnostic setting name
: Enter a descriptive name (for example,
export-to-secops
).
In the
Logs
section, select the following categories:
AuditLogs
OperationalLogs
DeviceComplianceOrg
Devices
In the
Destination details
section, select the
Archive to a storage account
checkbox.
Subscription
: Select the subscription containing your storage account.
Storage account
: Select the storage account you created earlier.
Click
Save
.
Configure a feed in Google SecOps to ingest Microsoft Intune logs from Blob Storage
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
Microsoft Intune Blob Storage
).
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
Microsoft Intune
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Azure URI
: Enter the Blob Service endpoint URL with the container path. Create separate feeds for each log category:
For Audit Logs:
https://<storage-account>.blob.core.windows.net/insights-logs-auditlogs/
For Operational Logs:
https://<storage-account>.blob.core.windows.net/insights-logs-operationallogs/
For Device Compliance Organizational Logs:
https://<storage-account>.blob.core.windows.net/insights-logs-devicecomplianceorg/
For Devices:
https://<storage-account>.blob.core.windows.net/insights-logs-devices/
Replace
<storage-account>
with your Azure storage account name.
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers
Delete transferred files
: Deletes files after successful transfer
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Shared key
: Enter the shared access key value from the Storage Account.
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
Repeat steps 1-10 to create additional feeds for each Intune log category container.
Configure Azure Storage firewall (if enabled)
If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.
In the
Azure portal
, go to your
Storage Account
.
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
See
IP Allowlisting documentation
Or retrieve them programmatically using the
Feed Management API
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
properties.Actor.UserPermissions, properties.TargetObjectIds, properties.TargetDisplayNames
additional.fields
List of key-value pairs providing additional context for the event
time
metadata.event_timestamp
Timestamp when the event occurred
metadata.event_type
Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)
operationName
metadata.product_event_type
Event type as defined by the product
properties.AuditEventId
metadata.product_log_id
Product-specific log identifier
correlationId
network.session_id
Session identifier for the network connection
properties.Actor.Application
principal.application
Application identifier
properties.Actor.ApplicationName
principal.resource.name
Name of the resource
properties.Actor.isDelegatedAdmin, properties.Actor.PartnerTenantId
principal.user.attribute.labels
List of key-value pairs providing additional context for the user
category
security_result.category_details
Additional details about the security result category
resultDescription
security_result.description
Description of the security result
identity, properties.ActivityDate, properties.ActivityResultStatus, properties.ActivityType, properties.Actor.ActorType, properties.Category, properties.Targets.ModifiedProperties.Name, properties.Targets.ModifiedProperties.New, properties.Targets.ModifiedProperties.Old
security_result.detection_fields
List of key-value pairs providing additional context for the security result
resultType
security_result.summary
Summary of the security result
tenantId
target.user.userid
User ID of the target user
metadata.product_name
Product name
metadata.vendor_name
Vendor/company name
Need more help?
Get answers from Community members and Google SecOps professionals.
