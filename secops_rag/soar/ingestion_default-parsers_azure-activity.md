# Collect Microsoft Azure Activity and Entra ID logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-activity/  
**Scraped:** 2026-03-05T09:57:52.425937Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Azure Activity and Entra ID logs
Supported in:
Google secops
SIEM
This document explains how to collect Microsoft Azure Activity and Entra ID logs by setting up Google Security Operations feeds using Microsoft Azure Blob Storage.
Azure Activity logs provide insight into subscription-level operations performed on Azure resources, such as creating storage accounts, deleting event hubs, or modifying virtual machines. Microsoft Entra ID (formerly Azure Active Directory) logs capture identity and access management events, including user sign-ins, audit logs, provisioning activities, and security risk detections.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to
Microsoft Azure
portal with permissions to:
Create Storage Accounts
Configure Diagnostic Settings for Azure Monitor and Entra ID
Manage access keys
Security Administrator role or higher in Entra ID (for Entra ID diagnostic settings)
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
secops-azure-logs
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
: Your storage account name (for example,
secops-azure-logs
)
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
https://secops-azure-logs.blob.core.windows.net/
Configure Azure Activity Logs diagnostic settings
To export Azure Activity logs to the storage account:
In the
Azure portal
, search for
Monitor
.
Click
Activity log
in the left navigation.
Click
Export Activity Logs
at the top of the window.
Click
Add diagnostic setting
.
Provide the following configuration details:
Diagnostic setting name
: Enter a descriptive name (for example,
activity-logs-to-secops
).
In the
Logs
section, select the following categories:
Administrative
Security
Service Health
Alert
Recommendation
Policy
Autoscale
Resource Health
In the
Destination details
section, select the
Archive to a storage account
checkbox.
Subscription
: Select the subscription containing your storage account.
Storage account
: Select the storage account you created earlier (for example,
secops-azure-logs
).
Click
Save
.
Configure Entra ID diagnostic settings
To export Entra ID logs to the storage account:
In the
Azure portal
, search for
Microsoft Entra ID
or
Azure Active Directory
.
In the left navigation, go to
Monitoring & health
>
Diagnostic settings
.
Click
Add diagnostic setting
.
Provide the following configuration details:
Diagnostic setting name
: Enter a descriptive name (for example,
entraid-logs-to-secops
).
In the
Logs
section, select the log categories you want to export:
SignInLogs
: Interactive user sign-ins
NonInteractiveUserSignInLogs
: Non-interactive user sign-ins (service principals, managed identities acting on behalf of users)
ServicePrincipalSignInLogs
: Service principal and application sign-ins
ManagedIdentitySignInLogs
: Managed identity sign-ins
AuditLogs
: Audit trail of all changes in Entra ID (user creation, role assignments, etc.)
ProvisioningLogs
: User and group provisioning events
RiskyUsers
: Users flagged by Identity Protection
UserRiskEvents
: Risk detections for user accounts
MicrosoftGraphActivityLogs
: Microsoft Graph API activity logs
In the
Destination details
section, select the
Archive to a storage account
checkbox.
Subscription
: Select the subscription containing your storage account.
Storage account
: Select the storage account you created earlier (for example,
secops-azure-logs
).
Click
Save
.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your Azure Blob Storage. You must grant this service account access to your storage account.
Get the service account email
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a temporary name.
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select any log type (you can change this later).
Click
Get Service Account
. A unique service account email is displayed, for example:
chronicle
-
12345678
@chronicle
-
gcp
-
prod
.
iam
.
gserviceaccount
.
com
Copy this email address for use in the next step.
Click
Cancel
to exit the feed creation (you will create the actual feeds later).
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Blob Data Reader
role on your storage account.
In the
Azure portal
, go to
Storage accounts
.
Click your storage account name (for example,
secops-azure-logs
).
Go to the
Access Control (IAM)
tab.
Click
+ Add
>
Add role assignment
.
In the
Role
tab, search for and select
Storage Blob Data Reader
.
Click
Next
.
In the
Members
tab, click
+ Select members
.
In the search box, paste the Google SecOps service account email.
Select the service account from the results.
Click
Select
.
Click
Review + assign
.
Review the assignment and click
Review + assign
again.
Configure feeds in Google SecOps
You must create a separate feed for each log type and container. The following table shows the mapping between Azure containers and Google SecOps log types:
Container Name
Chronicle Log Type
Data Source
insights-activity-logs
Azure Activity
Azure Activity Logs
insights-logs-signinlogs
Azure AD
Entra ID Interactive Sign-ins
insights-logs-noninteractiveusersigninlogs
Azure AD
Entra ID Non-interactive Sign-ins
insights-logs-serviceprincipalsigninlogs
Azure AD
Entra ID Service Principal Sign-ins
insights-logs-managedidentitysigninlogs
Azure AD
Entra ID Managed Identity Sign-ins
insights-logs-auditlogs
Azure AD Audit
Entra ID Audit Logs
insights-logs-provisioninglogs
Azure AD
Entra ID Provisioning Logs
insights-logs-riskyusers
Azure AD
Entra ID Risky Users
insights-logs-userriskevents
Azure AD
Entra ID User Risk Events
insights-logs-microsoftgraphactivitylogs
Microsoft Graph Activity Logs
Microsoft Graph Activity
Create feed for Azure Activity Logs
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
field, enter
Azure Activity Logs
.
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
Azure Activity
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Azure URI
: Enter the Blob Service endpoint URL with the container path:
https://secops-azure-logs.blob.core.windows.net/insights-activity-logs/
Replace
secops-azure-logs
with your Azure storage account name.
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
: Enter the shared key value (access key) you captured from the Storage Account earlier.
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
Create feeds for Entra ID logs
Repeat the following steps for each Entra ID log type you configured in the diagnostic settings:
For Interactive Sign-in Logs:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter
Azure AD Interactive Sign-in Logs
.
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
Azure AD
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-signinlogs/
Source deletion option
: Select according to your preference.
Maximum File Age
: 180 days (default).
Shared key
: Enter the shared key value.
Asset namespace
: The asset namespace.
Ingestion labels
: The label to be applied.
Click
Next
and then
Submit
.
For Non-interactive Sign-in Logs:
Create another feed with the following settings:
Feed name
:
Azure AD Non-interactive Sign-in Logs
Log type
:
Azure AD
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-noninteractiveusersigninlogs/
For Service Principal Sign-in Logs:
Create another feed with the following settings:
Feed name
:
Azure AD Service Principal Sign-in Logs
Log type
:
Azure AD
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-serviceprincipalsigninlogs/
For Managed Identity Sign-in Logs:
Create another feed with the following settings:
Feed name
:
Azure AD Managed Identity Sign-in Logs
Log type
:
Azure AD
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-managedidentitysigninlogs/
For Audit Logs:
Create another feed with the following settings:
Feed name
:
Azure AD Audit Logs
Log type
:
Azure AD Audit
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-auditlogs/
For Provisioning Logs:
Create another feed with the following settings:
Feed name
:
Azure AD Provisioning Logs
Log type
:
Azure AD
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-provisioninglogs/
For Risky Users:
Create another feed with the following settings:
Feed name
:
Azure AD Risky Users
Log type
:
Azure AD
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-riskyusers/
For User Risk Events:
Create another feed with the following settings:
Feed name
:
Azure AD User Risk Events
Log type
:
Azure AD
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-userriskevents/
For Microsoft Graph Activity Logs:
Create another feed with the following settings:
Feed name
:
Microsoft Graph Activity Logs
Log type
:
Microsoft Graph Activity Logs
Azure URI
:
https://secops-azure-logs.blob.core.windows.net/insights-logs-microsoftgraphactivitylogs/
Need more help?
Get answers from Community members and Google SecOps professionals.
