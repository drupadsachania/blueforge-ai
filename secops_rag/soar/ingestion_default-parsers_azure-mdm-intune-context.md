# Collect Microsoft Intune logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context/  
**Scraped:** 2026-03-05T09:58:10.949092Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Intune logs
Supported in:
Google secops
SIEM
This document explains how to collect Microsoft Intune logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.
Microsoft Intune is a cloud-based endpoint management solution that manages user access to organizational resources and simplifies app and device management across devices including mobile devices, desktop computers, and virtual endpoints.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to
Microsoft Azure
portal with permissions to:
Create Storage Accounts
Configure Diagnostic Settings for Microsoft Intune
Manage access keys
User with the
Intune Administrator
or
Global Administrator
Microsoft Entra role for the Intune tenant
Azure subscription to set up the storage account
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
intunelogsstorage
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
: The name you provided during creation
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
https://intunelogsstorage.blob.core.windows.net/
Configure Microsoft Intune Diagnostic Settings
Sign in to the
Microsoft Intune admin center
. Select
Reports
>
Diagnostic settings
. The first time you open it, turn it on. Otherwise, add a setting.
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
☑
AuditLogs
☑
OperationalLogs
☑
DeviceComplianceOrg
☑
Devices
In the
Destination details
section, select
Archive to a storage account
checkbox.
Subscription
: Select the subscription containing your storage account.
Storage account
: Select the storage account you created earlier.
Click
Save
.
After configuration, logs will be automatically exported to the storage account.
Audit Logs show a record of activities that generate a change in Intune.
Operational Logs show details on users and devices that successfully (or failed) to enroll, and details on noncompliant devices.
Device Compliance Organizational Logs show an organizational report for device compliance in Intune, and details on noncompliant devices.
IntuneDevices show device inventory and status information for Intune enrolled and managed devices.
The Intune Audit Logs and Operational Logs are sent immediately from Intune to Azure Monitor services. The Intune Device Compliance Organizational Logs and IntuneDevices report data is sent from Intune to Azure Monitor services once every 24 hours. So, it can take up to 24 hours to get the logs in the Azure Monitor services. Once the data is sent from Intune, then it typically shows in the Azure Monitor service within 30 minutes.
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
: Enter the Blob Service endpoint URL with the container path. Since Intune creates multiple containers for different log categories, you will need to create separate feeds for each container.
Use the following format and replace
intunelogsstorage
with your Azure storage account name.
For Audit Logs:
https://intunelogsstorage.blob.core.windows.net/insights-logs-auditlogs/
For Operational Logs:
https://intunelogsstorage.blob.core.windows.net/insights-logs-operationallogs/
For Device Compliance Organizational Logs:
https://intunelogsstorage.blob.core.windows.net/insights-logs-devicecomplianceorg/
For Devices:
https://intunelogsstorage.blob.core.windows.net/insights-logs-devices/
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
: Enter the shared key value (access key) you captured from the Storage Account.
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
To get the current IP ranges choose one of the following options:
See
IP Allowlisting documentation
Retrieve the current IP ranges programmatically using the
Feed Management API
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
@output
event
Merged to @output
properties.Actor.UserPermissions
event.idm.read_only_udm.additional.fields
Looped, each permission converted to string, added as string_value to list with key "UserPermissions", merged
properties.TargetDisplayNames
event.idm.read_only_udm.additional.fields
Looped, each TargetDisplayNames if not null, added as string_value to list with key "TargetDisplayNames", merged
properties.TargetObjectIds
event.idm.read_only_udm.additional.fields
Looped, each TargetObjectIds converted to string, added as string_value to list with key "TargetObjectIds", merged
metadata
event.idm.read_only_udm.metadata
Renamed from metadata
time
event.idm.read_only_udm.metadata.event_timestamp
Converted from time to ISO8601
has_user
event.idm.read_only_udm.metadata.event_type
Derived: if has_user == "true" then "USER_UNCATEGORIZED" else "GENERIC_EVENT"
operationName
event.idm.read_only_udm.metadata.product_event_type
Value taken from operationName
properties.AuditEventId
event.idm.read_only_udm.metadata.product_log_id
Value taken from properties.AuditEventId
correlationId
event.idm.read_only_udm.network.session_id
Value taken from correlationId
principal
event.idm.read_only_udm.principal
Renamed from principal
properties.Actor.Application
event.idm.read_only_udm.principal.application
Value taken from properties.Actor.Application
properties.Actor.ApplicationName
event.idm.read_only_udm.principal.resource.name
Value taken from properties.Actor.ApplicationName
properties.Actor.isDelegatedAdmin
event.idm.read_only_udm.principal.user.attribute.labels
Converts to string, creates label with key "isDelegatedAdmin" and value, merged
properties.Actor.PartnerTenantId
event.idm.read_only_udm.principal.user.attribute.labels
Creates label with key "PartnerTenantId" and value, merged
security_result
event.idm.read_only_udm.security_result
Merged from security_result
category
event.idm.read_only_udm.security_result.category_details
Value taken from category
resultDescription
event.idm.read_only_udm.security_result.description
Value taken from resultDescription
identity
event.idm.read_only_udm.security_result.detection_fields
Creates label with key "identity" and value from identity, merged
properties.ActivityDate
event.idm.read_only_udm.security_result.detection_fields
Creates label with key "ActivityDate" and value from properties.ActivityDate, merged
properties.ActivityResultStatus
event.idm.read_only_udm.security_result.detection_fields
Converts to string, creates label with key "ActivityResultStatus" and value, merged
properties.ActivityType
event.idm.read_only_udm.security_result.detection_fields
Converts to string, creates label with key "ActivityType" and value, merged
properties.Actor.ActorType
event.idm.read_only_udm.security_result.detection_fields
Converts to string, creates label with key "ActorType" and value, merged
properties.Category
event.idm.read_only_udm.security_result.detection_fields
Converts to string, creates label with key "Category" and value, merged
properties.Targets.ModifiedProperties.Name
event.idm.read_only_udm.security_result.detection_fields
Creates label with key "Name" and value from mproper.Name, merged
properties.Targets.ModifiedProperties.New
event.idm.read_only_udm.security_result.detection_fields
Creates label with key "New" and value from mproper.New, merged
properties.Targets.ModifiedProperties.Old
event.idm.read_only_udm.security_result.detection_fields
Creates label with key "Old" and value from mproper.Old, merged
resultType
event.idm.read_only_udm.security_result.summary
Value taken from resultType
target
event.idm.read_only_udm.target
Renamed from target
tenantId
event.idm.read_only_udm.target.user.userid
Value taken from tenantId
event.idm.read_only_udm.metadata.product_name
Set to "Microsoft Intune Context"
event.idm.read_only_udm.metadata.vendor_name
Set to "Microsoft"
Need more help?
Get answers from Community members and Google SecOps professionals.
