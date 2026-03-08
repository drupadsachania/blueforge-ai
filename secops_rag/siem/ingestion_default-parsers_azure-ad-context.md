# Collect Microsoft Azure AD Context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context/  
**Scraped:** 2026-03-05T09:26:19.955014Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Azure AD Context logs
Supported in:
Google secops
SIEM
This document describes how you can collect Microsoft Azure Active Directory (AD) logs by
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
How to set up the Microsoft Azure AD Context feed
Click the
Azure Platform
pack.
Locate the
Azure AD Organizational Context
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
Retrieve Devices
: Whether to retrieve device information within user context.
Retrieve Groups
: Whether to retrieve group membership information within user context.
API Full path
: Microsoft Graph REST API endpoint URL.
API Authentication Endpoint
: Microsoft Active Directory Authentication Endpoint.
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
This parser code transforms raw JSON formatted logs from Azure Active Directory into a unified data model (UDM). It extracts user and manager information, including attributes, roles, relations, and labels, while handling various data inconsistencies and enriching the output with standardized fields.
UDM Mapping Table
Log Field
UDM Mapping
Logic
businessPhones
user.phone_numbers
Directly mapped from the
businessPhones
field in the raw log. Multiple phone numbers are extracted and mapped as separate entries.
city
user.personal_address.city
Directly mapped from the
city
field in the raw log.
companyName
user.company_name
Directly mapped from the
companyName
field in the raw log.
country
user.personal_address.country_or_region
Directly mapped from the
country
field in the raw log. If
country
is empty, the value is taken from
usageLocation
.
createdDateTime
user.attribute.creation_time
Converted to a timestamp from the
createdDateTime
field in the raw log using the RFC 3339 format.
department
user.department
Directly mapped from the
department
field in the raw log. Multiple departments are extracted and mapped as separate entries.
displayName
user.user_display_name
Directly mapped from the
displayName
field in the raw log.
employeeId
user.employee_id
Directly mapped from the
employeeId
field in the raw log. If
employeeId
is empty, the value is taken from
extension_employeeNumber
.
employeeType
user.attribute.labels.value (key: employeeType)
Directly mapped from the
employeeType
field in the raw log and added as a label with the key
employeeType
.
extension_employeeNumber
user.employee_id
Mapped to
user.employee_id
if
employeeId
is empty.
extension_wfc_AccountType
event.idm.entity.entity.labels.value (key: wfc_AccountType)
Directly mapped from the
extension_wfc_AccountType
field in the raw log and added as a label with the key
wfc_AccountType
.
extension_wfc_AccountingUnitName
event.idm.entity.entity.labels.value (key: extension_wfc_AccountingUnitName)
Directly mapped from the
extension_wfc_AccountingUnitName
field in the raw log and added as a label with the key
extension_wfc_AccountingUnitName
.
extension_wfc_execDescription
event.idm.entity.entity.labels.value (key: extension_wfc_execDescription)
Directly mapped from the
extension_wfc_execDescription
field in the raw log and added as a label with the key
extension_wfc_execDescription
.
extension_wfc_groupDescription
event.idm.entity.entity.labels.value (key: extension_wfc_groupDescription)
Directly mapped from the
extension_wfc_groupDescription
field in the raw log and added as a label with the key
extension_wfc_groupDescription
.
extension_wfc_orgDescription
event.idm.entity.entity.labels.value (key: extension_wfc_orgDescription)
Directly mapped from the
extension_wfc_orgDescription
field in the raw log and added as a label with the key
extension_wfc_orgDescription
.
givenName
user.first_name
Directly mapped from the
givenName
field in the raw log.
gopher-devices
event.idm.entity.relations
Each device in the
gopher-devices
array is mapped to a separate relation entry. The
deviceId
is mapped to
product_object_id
,
operatingSystem
and
operatingSystemVersion
are combined to form
platform_version
,
model
is directly mapped, and
createdDateTime
is converted to a timestamp and mapped to
created_timestamp
. The relationship is set to
OWNS
and the direction is set to
UNIDIRECTIONAL
.
gopher-groups
event.idm.entity.relations
Each group in the
gopher-groups
array is mapped to a separate relation entry. The
id
is mapped to
product_object_id
, and
displayName
is mapped to
group_display_name
. The relationship is set to
MEMBER
and the direction is set to
UNIDIRECTIONAL
.
gopher-manager.businessPhones
empmanager.phone_numbers
Mapped to
empmanager.phone_numbers
if
manager
is empty.
gopher-manager.country
empmanager.personal_address.country_or_region
Mapped to
empmanager.personal_address.country_or_region
if
manager
is empty. If both
gopher-manager.country
and
gopher-manager.usageLocation
are empty, the field is left empty.
gopher-manager.department
empmanager.department
Mapped to
empmanager.department
if
manager
is empty.
gopher-manager.displayName
empmanager.user_display_name
Mapped to
empmanager.user_display_name
if
manager
is empty.
gopher-manager.employeeId
empmanager.employee_id
Mapped to
empmanager.employee_id
if
manager
is empty and
gopher-manager.employeeId
is not empty.
gopher-manager.extension_employeeNumber
empmanager.employee_id
Mapped to
empmanager.employee_id
if
manager
and
gopher-manager.employeeId
are empty, and
gopher-manager.extension_employeeNumber
is not empty.
gopher-manager.givenName
empmanager.first_name
Mapped to
empmanager.first_name
if
manager
is empty.
gopher-manager.id
empmanager.product_object_id
Mapped to
empmanager.product_object_id
if
manager
is empty.
gopher-manager.jobTitle
empmanager.title
Mapped to
empmanager.title
if
manager
is empty.
gopher-manager.mail
empmanager.email_addresses
Mapped to
empmanager.email_addresses
if
manager
is empty.
gopher-manager.onPremisesImmutableId
user.attribute.labels.value (key: gopher-manager onPremisesImmutableId)
Mapped as a label with the key
gopher-manager onPremisesImmutableId
.
gopher-manager.onPremisesSamAccountName
empmanager.userid
Mapped to
empmanager.userid
if
manager
is empty.
gopher-manager.onPremisesSecurityIdentifier
empmanager.windows_sid
Mapped to
empmanager.windows_sid
if
manager
is empty.
gopher-manager.proxyAddresses
empmanager.email_addresses, empmanager.group_identifiers
If
manager
is empty, each address in the
gopher-manager.proxyAddresses
array is mapped to either
empmanager.email_addresses
or
empmanager.group_identifiers
based on whether it starts with "smtp" or "SMTP".
gopher-manager.refreshTokensValidFromDateTime
empmanager.attribute.labels.value (key: refreshTokensValidFromDateTime)
Mapped as a label with the key
refreshTokensValidFromDateTime
if
manager
is empty.
gopher-manager.streetAddress
empmanager.personal_address.name
Mapped to
empmanager.personal_address.name
if
manager
is empty.
gopher-manager.surname
empmanager.last_name
Mapped to
empmanager.last_name
if
manager
is empty.
gopher-manager.usageLocation
user.attribute.labels.value (key: manager_src_usageLocation)
Mapped as a label with the key
manager_src_usageLocation
.
gopher-manager.userType
empmanager.attribute.roles.name
Mapped to
empmanager.attribute.roles.name
if
manager
is empty.
id
user.product_object_id
Directly mapped from the
id
field in the raw log.
identities
user.attribute.labels.value (key: signInType), user.attribute.labels.value (key: userPrincipalName)
The
signInType
is mapped as a label with the key
signInType
. If
signInType
and
userPrincipalName
are not empty, they are combined and mapped as a label with the key
userPrincipalName
.
jobTitle
user.title
Directly mapped from the
jobTitle
field in the raw log.
mail
user.email_addresses
Directly mapped from the
mail
field in the raw log. If
mail
starts with "svc-", the
user_role.type
is set to
SERVICE_ACCOUNT
.
mailNickname
user.attribute.labels.value (key: mailNickname)
Directly mapped from the
mailNickname
field in the raw log and added as a label with the key
mailNickname
.
manager.businessPhones
empmanager.phone_numbers
Mapped to
empmanager.phone_numbers
if
gopher-manager
is empty.
manager.city
empmanager.personal_address.city
Mapped to
empmanager.personal_address.city
if
gopher-manager
is empty.
manager.companyName
empmanager.company_name
Mapped to
empmanager.company_name
if
gopher-manager
is empty.
manager.country
empmanager.personal_address.country_or_region
Mapped to
empmanager.personal_address.country_or_region
if
gopher-manager
is empty. If both
manager.country
and
manager.usageLocation
are empty, the field is left empty.
manager.department
empmanager.department
Mapped to
empmanager.department
if
gopher-manager
is empty.
manager.displayName
empmanager.user_display_name
Mapped to
empmanager.user_display_name
if
gopher-manager
is empty.
manager.employeeId
empmanager.employee_id
Mapped to
empmanager.employee_id
if
gopher-manager
is empty and
manager.employeeId
is not empty.
manager.extension_employeeNumber
empmanager.employee_id
Mapped to
empmanager.employee_id
if
gopher-manager
and
manager.employeeId
are empty, and
manager.extension_employeeNumber
is not empty.
manager.givenName
empmanager.first_name
Mapped to
empmanager.first_name
if
gopher-manager
is empty.
manager.id
empmanager.product_object_id
Mapped to
empmanager.product_object_id
if
gopher-manager
is empty.
manager.jobTitle
empmanager.title
Mapped to
empmanager.title
if
gopher-manager
is empty.
manager.mail
empmanager.email_addresses
Mapped to
empmanager.email_addresses
if
gopher-manager
is empty.
manager.onPremisesSamAccountName
empmanager.userid
Mapped to
empmanager.userid
if
gopher-manager
is empty.
manager.onPremisesSecurityIdentifier
empmanager.windows_sid
Mapped to
empmanager.windows_sid
if
gopher-manager
is empty.
manager.proxyAddresses
empmanager.email_addresses, empmanager.group_identifiers
If
gopher-manager
is empty, each address in the
manager.proxyAddresses
array is mapped to either
empmanager.email_addresses
or
empmanager.group_identifiers
based on whether it starts with "smtp" or "SMTP".
manager.refreshTokensValidFromDateTime
empmanager.attribute.labels.value (key: refreshTokensValidFromDateTime)
Mapped as a label with the key
refreshTokensValidFromDateTime
if
gopher-manager
is empty.
manager.state
empmanager.personal_address.state
Mapped to
empmanager.personal_address.state
if
gopher-manager
is empty.
manager.streetAddress
empmanager.personal_address.name
Mapped to
empmanager.personal_address.name
if
gopher-manager
is empty.
manager.surname
empmanager.last_name
Mapped to
empmanager.last_name
if
gopher-manager
is empty.
manager.usageLocation
user.attribute.labels.value (key: manager_src_usageLocation), empmanager.personal_address.country_or_region
Mapped as a label with the key
manager_src_usageLocation
. If
manager.country
is empty, the value is also mapped to
empmanager.personal_address.country_or_region
.
manager.userType
empmanager.attribute.roles.name
Mapped to
empmanager.attribute.roles.name
if
gopher-manager
is empty.
onPremisesDistinguishedName
user.attribute.labels.value (key: onPremisesDistinguishedName), user.attribute.labels.value (key: onPremisesDistinguishedName-OU data)
The full distinguished name is mapped as a label with the key
onPremisesDistinguishedName
. The OU portion of the distinguished name is extracted and mapped as a label with the key
onPremisesDistinguishedName-OU data
. If the OU portion contains "Admin", the
user_role.type
is set to
ADMINISTRATOR
. If it contains "Service Accounts", the
user_role.type
is set to
SERVICE_ACCOUNT
.
onPremisesDomainName
user.group_identifiers, user.attribute.labels.value (key: onPremisesDomainName)
Directly mapped to
user.group_identifiers
and added as a label with the key
onPremisesDomainName
.
onPremisesImmutableId
user.attribute.labels.value (key: onPremisesImmutableId)
Directly mapped from the
onPremisesImmutableId
field in the raw log and added as a label with the key
onPremisesImmutableId
.
onPremisesSamAccountName
user.userid, user.attribute.labels.value (key: onPremisesSamAccountName)
Mapped to
user.userid
if
sAMAccountName
is empty. Also added as a label with the key
onPremisesSamAccountName
.
onPremisesSecurityIdentifier
user.windows_sid
Directly mapped from the
onPremisesSecurityIdentifier
field in the raw log.
proxyAddresses
user.email_addresses, user.group_identifiers
Each address in the
proxyAddresses
array is mapped to either
user.email_addresses
or
user.group_identifiers
based on whether it starts with "smtp" or "SMTP". If the address starts with "smtp" or "SMTP", the "smtp:" or "SMTP:" prefix is removed and the remaining email address is extracted and mapped to
user.email_addresses
.
refreshTokensValidFromDateTime
user.attribute.labels.value (key: refreshTokensValidFromDateTime)
Directly mapped from the
refreshTokensValidFromDateTime
field in the raw log and added as a label with the key
refreshTokensValidFromDateTime
.
sAMAccountName
user.userid
Directly mapped from the
sAMAccountName
field in the raw log.
state
user.personal_address.state
Directly mapped from the
state
field in the raw log.
streetAddress
user.personal_address.name
Directly mapped from the
streetAddress
field in the raw log.
surname
user.last_name
Directly mapped from the
surname
field in the raw log.
usageLocation
user.personal_address.country_or_region
If
country
is empty, the value is mapped to
user.personal_address.country_or_region
.
userPrincipalName
user.email_addresses
Directly mapped from the
userPrincipalName
field in the raw log. If
userPrincipalName
starts with "svc-", the
user_role.type
is set to
SERVICE_ACCOUNT
.
userType
user.attribute.roles.name
Directly mapped from the
userType
field in the raw log and added to
user.attribute.roles.name
.
Parser Logic
UDM Mapping
Logic
N/A
event.idm.entity.metadata.vendor_name
Set to "Microsoft".
N/A
event.idm.entity.metadata.product_name
Set to "Azure Active Directory".
N/A
event.idm.entity.metadata.entity_type
Set to "USER".
N/A
event.idm.entity.metadata.collected_timestamp
Set to the
create_time
field from the raw log.
accountEnabled
user.user_authentication_status, user.attribute.labels.value (key: accountEnabled)
If
accountEnabled
is true,
user.user_authentication_status
is set to "ACTIVE" and a label with the key
accountEnabled
and value "true" is added. Otherwise, a label with the key
accountEnabled
and value "false" is added.
empmanager-src.accountEnabled
user.user_authentication_status, user.attribute.labels.value (key: accountEnabled)
If
manager
is empty and
empmanager-src.accountEnabled
is "true",
user.user_authentication_status
is set to "ACTIVE" and a label with the key
accountEnabled
and value "true" is added. Otherwise, a label with the key
accountEnabled
and value "false" is added.
onPremisesDistinguishedName
user_role.type
If the OU portion of the distinguished name contains "Admin", the
user_role.type
is set to
ADMINISTRATOR
. If it contains "Service Accounts", the
user_role.type
is set to
SERVICE_ACCOUNT
.
userPrincipalName
user_role.type
If
userPrincipalName
starts with "svc-", the
user_role.type
is set to
SERVICE_ACCOUNT
.
empmanager-src.onPremisesDistinguishedName
manager_role.type
If
gopher-manager
is empty and the OU portion of the manager's distinguished name contains "Users", the
manager_role.type
is set to
ADMINISTRATOR
. If it contains "Service Accounts", the
manager_role.type
is set to
SERVICE_ACCOUNT
.
empmanager-src.userPrincipalName
manager_role.type
If
gopher-manager
is empty and
empmanager-src.userPrincipalName
starts with "svc-", the
manager_role.type
is set to
SERVICE_ACCOUNT
.
mail
user_role.type
If
mail
starts with "svc-", the
user_role.type
is set to
SERVICE_ACCOUNT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
