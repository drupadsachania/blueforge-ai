# Collect Microsoft Azure AD logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad/  
**Scraped:** 2026-03-05T09:57:53.897323Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Azure AD logs
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
section, select
Accounts in this organizational directory only (Single tenant)
Redirect URI
: Leave blank (not required for service principal authentication).
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
How to set up the Microsoft Entra ID (Azure AD) feed
Click the
Azure Platform
pack.
Locate the
Azure AD
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
Field mapping reference
This parser code transforms raw Azure AD logs in JSON format into a unified data model (UDM). It first normalizes the data by removing unnecessary fields and then extracts relevant information like user details, timestamps, and event specifics, mapping them to corresponding UDM fields for consistent representation and analysis.
UDM mapping table
Log field
UDM mapping
Remarks
about
about
accountEnabled
user.user_authentication_status
user.attribute.labels.value
(key:
accountEnabled
)
If
accountEnabled
is
true
,
user.user_authentication_status
is set to
ACTIVE
and a label with the key
accountEnabled
and value
true
is added. Otherwise, a label with the key
accountEnabled
and value
false
is added.
additionalDetails
additional.fields
appOwnerTenantId
target.resource.attribute.labels
authenticationAppDeviceDetails
additional.fields
authenticationContextClassReference
security_result.detection_fields
autonomousSystemNumber
principal.resource.attribute.labels
browser
network.http.user_agent
browser
network.http.user_agent
businessPhones
user.phone_numbers
Multiple phone numbers are extracted and mapped as separate entries.
city
user.personal_address.city
clientCredentialType
additional.fields
companyName
user.company_name
country
user.personal_address.country_or_region
If
country
is empty, the value is taken from
usageLocation
.
createdDateTime
user.attribute.creation_time
Converted to a timestamp from the
createdDateTime
field in the raw log using the RFC 3339 format.
cribl_pipe
additional.fields
crossTenantAccessType
additional.fields
department
user.department
Multiple departments are extracted and mapped as separate entries.
deviceDetail.displayName
principal.hostname,principal.asset.hostname
displayName
user.user_display_name
employeeId
user.employee_id
If
employeeId
is empty, the value is taken from
extension_employeeNumber
.
employeeType
user.attribute.labels.value
(key:
employeeType
)
Mapped from the
employeeType
field in the raw log and added as a label with the key
employeeType
.
empmanager-src.accountEnabled
user.user_authentication_status
user.attribute.labels.value
(key:
accountEnabled
)
If
manager
is empty and
empmanager-src.accountEnabled
is
true
,
user.user_authentication_status
is set to
ACTIVE
and a label with the key
accountEnabled
and value
true
is added. Otherwise, a label with the key
accountEnabled
and value
false
is added.
empmanager-src.onPremisesDistinguishedName
manager_role.type
If
gopher-manager
is empty and the OU portion of the manager's distinguished name contains
Users
, the
manager_role.type
is set to
ADMINISTRATOR
. If it contains
Service Accounts
, the
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
starts with
svc-
, the
manager_role.type
is set to
SERVICE_ACCOUNT
.
errorCode
security_result.detection_fields
extension_employeeNumber
user.employee_id
Mapped to
user.employee_id
if employeeId is empty.
extension_wfc_AccountingUnitName
event.idm.entity.entity.labels.value
(key:
extension_wfc_AccountingUnitName
)
Mapped from the
extension_wfc_AccountingUnitName
field in the raw log and added as a label with the key
extension_wfc_AccountingUnitName
.
extension_wfc_AccountType
event.idm.entity.entity.labels.value
(key:
wfc_AccountType
)
Mapped from the
extension_wfc_AccountType
field in the raw log and added as a label with the key
wfc_AccountType
.
extension_wfc_execDescription
event.idm.entity.entity.labels.value
(key:
extension_wfc_execDescription
)
Mapped from the
extension_wfc_execDescription
field in the raw log and added as a label with the key
extension_wfc_execDescription
.
extension_wfc_groupDescription
event.idm.entity.entity.labels.value
(key:
extension_wfc_groupDescription
)
Mapped from the
extension_wfc_groupDescription
field in the raw log and added as a label with the key
extension_wfc_groupDescription
.
extension_wfc_orgDescription
event.idm.entity.entity.labels.value
(key:
extension_wfc_orgDescription
)
Mapped from the
extension_wfc_orgDescription
field in the raw log and added as a label with the key
extension_wfc_orgDescription
.
failureReason
security_result.description
federatedCredentialId
additional.fields
flaggedForReview
additional.fields
givenName
user.first_name
gopher-devices
event.idm.entity.relations
Each device in the gopher-devices array is mapped to a separate relation entry. The
deviceId
is mapped to
product_object_id
,
operatingSystem
and
operatingSystemVersion
are combined to form
platform_version
model is directly mapped, and
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
Each group in the gopher-groups array is mapped to a separate relation entry. The
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
user.attribute.labels.value
(key:
gopher-manager onPremisesImmutableId
)
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
empmanager.email_addresses
empmanager.group_identifiers
If
manager
is empty, each address in the
gopher-manager.proxyAddresses
array is mapped to either
empmanager.email_addresses
or
empmanager.group_identifiers
based on whether it starts with
smtp
or
SMTP
.
gopher-manager.refreshTokensValidFromDateTime
empmanager.attribute.labels.value
(key:
refreshTokensValidFromDateTime
)
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
user.attribute.labels.value
(key:
manager_src_usageLocation
)
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
homeTenantId
target.resource.attribute.labels
homeTenantName
target.resource.attribute.labels
id
user.product_object_id
identities
user.attribute.labels.value
(key:
signInType
)
user.attribute.labels.value
(key:
userPrincipalName
)
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
identity
principal.user.user_display_name
incomingTokenType
additional.fields
initiatedBy.app.displayName
principal.application
initiatedBy.app.servicePrincipalId
principal.resource.product_object_id
initiatedBy.user.homeTenantId
target.resource.attribute.labels
initiatedBy.user.homeTenantName
target.resource.attribute.labels
initiatedBy.user.userType
additional.fields
ipAddressFromResourceProvider
principal.resource.attribute.labels
isTenantRestricted
additional.fields
jobTitle
user.title
loggedByService
observer.application
mail
user.email_addresses
If
mail
starts with
svc-
, the
user_role.type
is set to
SERVICE_ACCOUNT
.
mail
user_role.type
If
mail
starts with
svc-
, the
user_role.type
is set to
SERVICE_ACCOUNT
.
mailNickname
user.attribute.labels.value
(key:
mailNickname
)
Mapped from the
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
empmanager.email_addresses
empmanager.group_identifiers
If
gopher-manager
is empty, each address in the
manager.proxyAddresses
array is mapped to either
empmanager.email_addresses
or
empmanager.group_identifiers based on whether it starts with
smtp
or
SMTP`.
manager.refreshTokensValidFromDateTime
empmanager.attribute.labels.value
(key:
refreshTokensValidFromDateTime
)
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
user.attribute.labels.value
(key:
manager_src_usageLocation
)
empmanager.personal_address.country_or_region
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
mfaDetail.authDetail
principal.user.phone_numbers
onPremisesDistinguishedName
user.attribute.labels.value
(key:
onPremisesDistinguishedName
)
user.attribute.labels.value
(key:
onPremisesDistinguishedName-OU data
)
The full distinguished name is mapped as a label with the key
onPremisesDistinguishedName
. The
OU
portion of the distinguished name is extracted and mapped as a label with the key
onPremisesDistinguishedName-OU data
. If the
OU
portion contains
Admin
, the
user_role.type
is set to
ADMINISTRATOR
. If it contains
Service Accounts
, the
user_role.type
is set to
SERVICE_ACCOUNT
.
onPremisesDistinguishedName
user_role.type
If the
OU
portion of the distinguished name contains
Admin
, the
user_role.type
is set to
ADMINISTRATOR
. If it contains
Service Accounts
, the
user_role.type
is set to
SERVICE_ACCOUNT
.
onPremisesDomainName
user.group_identifiers
user.attribute.labels.value
(key:
onPremisesDomainName
)
Directly mapped to
user.group_identifiers
and added as a label with the key
onPremisesDomainName
.
onPremisesImmutableId
user.attribute.labels.value
(key:
onPremisesImmutableId
)
Mapped from the
onPremisesImmutableId
field in the raw log and added as a label with the key
onPremisesImmutableId
.
onPremisesSamAccountName
user.userid
user.attribute.labels.value
(key:
onPremisesSamAccountName
)
Mapped to
user.userid
if
sAMAccountName
is empty. Also added as a label with the key
onPremisesSamAccountName
.
onPremisesSecurityIdentifier
user.windows_sid
operationName
metadata.product_event_type
OrganizationId
principal.resource.product_object_id
originalRequestId
network.session_id
originalTransferMethod
additional.fields
Parser Logic
UDM Mapping
Logic
policies.enforcedGrantControls
security_result.detection_fields
processingTimeInMilliseconds
additional.fields
properties.__UDI_RequiredFields_RegionScope
target.location.country_or_region
properties.additionalDetails
additional.fields
properties.alternateSignInName
target.user.userid
properties.appId
principal.user.product_object_id
properties.atContentH
additional.fields
properties.atContentP
additional.fields
properties.authenticationContextClassReferences
additional.fields
properties.C_DeviceId
additional.fields
properties.C_Iat
additional.fields
properties.C_Idtyp
additional.fields
properties.C_Sid
additional.fields
properties.category
security_result.category_details
properties.clientAuthMethod
additional.fields
properties.clientCredentialType
additional.fields
properties.correlationId
security_result.detection_fields
properties.deviceDetail.browser
network.http.user_agent
properties.deviceDetail.deviceId
principal.asset.asset_id
properties.deviceDetail.displayName
principal.hostname,principal.asset.hostname
properties.deviceDetail.operatingSystem
principal.platform_version
If
operatingSystem
starts with
Win
,
Mac
, or
Lin
, then it's mapped to
principal.platform
.
properties.deviceDetail.trustType
principal.asset.attribute.labels
properties.EventData.AuthenticationPackageName
security_result.about.resource.name
properties.EventData.CallerProcessId
principal.process.pid
properties.EventData.CallerProcessName
principal.process.file.full_path
properties.EventData.CertIssuerName
additional.fields
properties.EventData.CertSerialNumber
about.artifact.last_https_certificate.serial_number
properties.EventData.CertThumbprint
additional.fields
properties.EventData.HandleId
target.resource.attribute.labels
properties.EventData.ImpersonationLevel
additional.fields
properties.EventData.IpAddress
principal.ip
principal.asset.ip
properties.EventData.IpPort
principal.port
properties.EventData.KeyLength
additional.fields
properties.EventData.LmPackageName
target.resource.attribute.labels
properties.EventData.LogonGuid
security_result.detection_fields
properties.EventData.LogonProcessName
target.process.file.names
properties.EventData.LogonType
extensions.auth.auth_details
properties.EventData.NewSd
security_result.detection_fields
properties.EventData.ObjectName
target.resource.name
properties.EventData.ObjectServer
target.resource.attribute.labels
properties.EventData.ObjectType
target.resource.resource_subtype
properties.EventData.OldSd
security_result.detection_fields
properties.EventData.PreAuthType
extensions.auth.mechanism
properties.EventData.ProcessId
target.process.pid
properties.EventData.ProcessName"
target.process.file.full_path
properties.EventData.ServiceName
target.application
properties.EventData.ServiceSid
target.resource.user.windows_sid
properties.EventData.Source
principal.ip
principal.asset.ip
properties.EventData.Status
security_result.detection_fields
properties.EventData.SubjectDomainName
principal.administrative_domain
properties.EventData.SubjectLogonId
principal.resource.attribute.labels
properties.EventData.SubjectUserName
principal.user.userid
properties.EventData.SubjectUserSid
principal.user.windows_sid
properties.EventData.TargetDomainName
target.administrative_domain
properties.EventData.TargetLogonId
target.resource.attribute.labels
properties.EventData.TargetSid
target.user.windows_sid
properties.EventData.TargetUserName
target.user.userid
properties.EventData.TargetUserSid
target.user.windows_sid
properties.EventData.TicketEncryptionType
security_result.detection_fields
properties.EventData.TicketOptions
security_result.detection_fields"
properties.EventData.TransmittedServices
security_result.detection_fields
properties.EventData.WorkstationName
target.hostname
target.asset.hostname
properties.flaggedForReview
additional.fields
properties.homeTenantId
target.resource.attribute.labels
properties.incomingTokenType
additional.fields
properties.initiatedBy.app.displayName
principal.user.user_display_name
properties.initiatedBy.user.displayName
principal.user.user_display_name
properties.initiatedBy.user.id
principal.user.product_object_id
properties.initiatedBy.user.ipAddress
principal.ip,principal.asset.ip
properties.ipAddressFromResourceProvider
principal.resource.attribute.labels
properties.isInteractive
additional.fields
properties.isTenantRestricted
additional.fields
properties.isThroughGlobalSecureAccess
additional.fields
properties.location.geoCoordinates.altitude
additional.fields
properties.loggedByService
observer.application
properties.mfaDetail.authDetail
principal.user.phone_numbers
properties.operationType
target.resource.attribute.labels
properties.originalRequestId
network.session_id
properties.originalTransferMethod
additional.fields
properties.processingTimeInMilliseconds
additional.fields
properties.RecordId
metadata.product_log_id
properties.requestId
security_result.detection_fields
properties.requestMethod
network.http.method
properties.requestUri
network.http.referral_url
properties.resourceDisplayName
target.resource.name
properties.resourceId
target.resource.attribute.labels
properties.resourceOwnerTenantId
target.resource.attribute.labels
properties.resourceTenantId
target.resource.attribute.labels
properties.responseSizeBytes
network.received_bytes
properties.responseStatusCode
network.http.response_code
properties.resultReason
additional.fields
security_result.summary
properties.resultType
additional.fields
properties.riskDetail
security_result.detection_fields
properties.riskEventType
security_result.detection_fields
properties.riskLastUpdatedDateTime
security_result.detection_fields
properties.riskLevel
security_result.detection_fields
properties.riskLevelAggregated
security_result.detection_fields
properties.riskLevelDuringSignIn
security_result.detection_fields
properties.riskState
security_result.detection_fields
properties.riskType
security_result.detection_fields
properties.rngcStatus
additional.fields
properties.roles
principal.user.attribute.roles
properties.scopes
security_result.detection_fields
properties.servicePrincipalCredentialKeyId
additional.fields
properties.sessionLifetimePolicies
security_result.detection_fields
properties.signInActivityId
additional.fields
properties.SignInBondData.DeviceDetails.DeviceTrustType
principal.asset.attribute.labels
properties.SignInBondData.DeviceDetails.IsCompliant
security_result.rule_labels
properties.SignInBondData.DeviceDetails.IsManaged
principal.asset.attribute.labels
properties.SignInBondData.DisplayDetails.AttemptedUsername
principal.user.email_addresses
properties.SignInBondData.DisplayDetails.ProxyRestrictionTargetTenantName
additional.fields
properties.SignInBondData.DisplayDetails.ResourceDisplayName
target.resource.name
properties.SignInBondData.LocationDetails.IPChain
target.ip
properties.SignInBondData.LocationDetails.Latitude
additional.fields
properties.SignInBondData.LocationDetails.Longitude
additional.fields
properties.SignInBondData.MfaDetails
additional.fields
properties.SignInBondData.ProtocolDetails.AuthenticationMethodsUsed
extensions.auth.auth_details
properties.SignInBondData.ProtocolDetails.DomainHintPresent
additional.fields
properties.SignInBondData.ProtocolDetails.IsInteractive
additional.fields
properties.SignInBondData.ProtocolDetails.LoginHintPresent
additional.fields
properties.SignInBondData.ProtocolDetails.NetworkLocation
additional.fields"
properties.SignInBondData.ProtocolDetails.Protocol
security_result.detection_fields
If
properties.SignInBondData.ProtocolDetails.Protocol
==
WSTrust
then it's mapped to
security_result.detection_fields
, else it's mapped to
network.application_protocol
.
properties.SignInBondData.RamDetails.RamRecommendedAction
additional.fields
properties.SignInBondData.RamDetails.RamRecommender
additional.fields
properties.signInTokenProtectionStatus
additional.fields
properties.ssoExtensionVersion
additional.fields
properties.status.errorCode
security_result.detection_fields
security_result.action
properties.targetResources
target.resource.attribute.labels
properties.tenantGeo
Geolocation.country_or_region
properties.tokenIssuerName
additional.fields
properties.tokenProtectionStatusDetails.signInSessionStatus
additional.fields
properties.tokenProtectionStatusDetails.signInSessionStatusCode
additional.fields
properties.userDisplayName
principal.user.user_display_name
properties.wids
additional.fields
proxyAddresses
user.email_addresses
user.group_identifiers
Each address in the
proxyAddresses
array is mapped to either
user.email_addresses
or
user.group_identifiers
based on whether it starts with
smtp
or
SMTP
. If the address starts with
smtp
or
SMTP
, the
smtp:
or
SMTP:
prefix is removed and the remaining email address is extracted and mapped to
user.email_addresses
.
record.CorrelationId
additional.fields
record.CrossTenantAccessType
additional.fields
record.DeviceDetail.deviceId
network.session_id
record.DeviceDetail.operatingSystem
principal.platform_version
If
operatingSystem
starts with
Win
,
Mac
, or
Lin
, then it's mapped to
principal.platform
.
record.IsInteractive
additional.fields
record.level
security_result.severity_details
If
record_level
is in
["INFORMATION", "INFORMATIONAL", "0", "4", "WARNING", "1", "3","ERROR", "2","CRITICAL"]
, then it's mapped to
security_result.severity
.
record.location
principal.location.name
record.properties.appServicePrincipalId
additional.fields
record.properties.authenticationProtocol
additional.fields
record.properties.autonomousSystemNumber
principal.resource.attribute.labels
record.properties.C_DeviceId
principal.asset.asset_id
record.properties.crossTenantAccessType
additional.fields
record.properties.deviceDetail.isCompliant
security_result.rule_labels
record.properties.deviceDetail.isManaged
principal.asset.attribute.labels
record.properties.deviceDetail.trustType
principal.asset.attribute.labels
record.properties.flaggedForReview
additional.fields
record.properties.incomingTokenType
additional.fields
record.properties.isInteractive
extensions.auth.mechanism
record.properties.isTenantRestricted
additional.fields
record.properties.isThroughGlobalSecureAccess
additional.fields
record.properties.location
target.location.name
record.properties.originalTransferMethod
additional.fields
record.properties.resourceDisplayName
principal.resource.name
record.properties.riskDetail
security_result.detection_fields
record.properties.riskLevelAggregated
security_result.detection_fields
record.properties.riskLevelDuringSignIn
security_result.detection_fields
record.properties.riskState
security_result.detection_fields
record.properties.rngcStatus
additional.fields
record.properties.roles
principal.user.attribute.roles
record.properties.scopes
security_result.detection_fields
record.properties.servicePrincipalId
target.resource.attribute.labels
record.properties.servicePrincipalId
principal.user.userid
record.properties.signInTokenProtectionStatus
additional.fields
record.properties.ssoExtensionVersion
additional.fields
record.properties.status.additionalDetails
additional.fields
record.properties.tokenProtectionStatusDetails.signInSessionStatus
additional.fields
record.properties.tokenProtectionStatusDetails.signInSessionStatusCode
additional.fields
record.RiskDetail
security_result.detection_fields
record.RiskEventTypes
security_result.detection_fields
record.RiskLevelAggregated
security_result.detection_fields
record.RiskLevelDuringSignIn
security_result.detection_fields
record.RiskState
security_result.detection_fields
refreshTokensValidFromDateTime
user.attribute.labels.value
(key:
refreshTokensValidFromDateTime
)
Mapped from the
refreshTokensValidFromDateTime
field in the raw log and added as a label with the key
refreshTokensValidFromDateTime
.
resourceOwnerTenantId
target.resource.attribute.labels
resourceTenantId
target.resource.attribute.labels
resultDescription
security_result.description
resultReason
additional.fields
resultType
additional.fields
riskDetail
security_result.detection_fields
riskLevelAggregated
security_result.detection_fields
riskLevelDuringSignIn
security_result.detection_fields
riskState
security_result.detection_fields
sAMAccountName
user.userid
servicePrincipalCredentialKeyId
additional.fields
servicePrincipalCredentialThumbprint
additional.fields
servicePrincipalId
target.resource.attribute.labels
servicePrincipalName
additional.fields
sessionId
network.session_id
signInIdentifier
target.user.userid
signInIdentifierType
additional.fields
signInTokenProtectionStatus
additional.fields
state
user.personal_address.state
status.additionalDetails
additional.fields
streetAddress
user.personal_address.name
surname
user.last_name
targets.modifiedProperties
target.resource.attribute.labels
tokenIssuerName
additional.fields
tokenIssuerType
additional.fields
tokenProtectionStatusDetails.signInSessionStatus
security_result.detection_fields
uniqueTokenIdentifier
additional.fields
usageLocation
user.personal_address.country_or_region
If
country
is empty, the value is mapped to
user.personal_address.country_or_region
.
userDisplayName
principal.user.user_display_name
userId
principal.user.product_object_id
userPrincipalName
user.email_addresses
If
userPrincipalName
starts with
svc-
, the
user_role.type
is set to
SERVICE_ACCOUNT
.
userPrincipalName
user_role.type
If
userPrincipalName
starts with
svc-
, the
user_role.type
is set to
SERVICE_ACCOUNT
.
userType
additional.fields
N/A
event.idm.entity.metadata.vendor_name
Set to
Microsoft
.
N/A
event.idm.entity.metadata.product_name
Set to
Azure Active Directory
.
N/A
event.idm.entity.metadata.entity_type
Set to
USER
.
N/A
event.idm.entity.metadata.collected_timestamp
Set to the
create_time
field from the raw log.
UDM mapping delta reference
On January 1, 2026, Google SecOps released a new version of the Azure AD parser, which includes significant changes to the mapping of Azure AD log fields to UDM fields and changes to the mapping of event types.
Log-field mapping delta
The following table lists the mapping delta for Azure AD log-to-UDM fields exposed prior to January 1, 2026 and subsequently (listed in the
Old mapping
and
Current mapping
columns respectively):
Log field
Old mapping
Current mapping
additionalDetails
security_result.description
additional.fields
browser
principal.resource.attribute.labels
network.http.user_agent
browser
principal.resource.attribute.labels
network.http.user_agent
deviceDetail.displayName
principal.asset.hardware
principal.hostname,principal.asset.hostname
errorCode
security_result.rule_id
security_result.detection_fields
failureReason
additional.fields
security_result.description
identity
target.user.user_display_name
principal.user.user_display_name
loggedByService
target.application
observer.application
operationName
additional.fields
metadata.product_event_type
OrganizationId
principal.resource.id
principal.resource.product_object_id
properties.homeTenantId
additional.fields
target.resource.attribute.labels
properties.initiatedBy.user.id
principal.user.windows_sid
principal.user.product_object_id
properties.resourceOwnerTenantId
additional.fields
target.resource.attribute.labels
properties.riskDetail
additional.fields
security_result.detection_fields
properties.riskEventType
additional.fields
security_result.detection_fields
properties.riskLastUpdatedDateTime
additional.fields
security_result.detection_fields
properties.riskLevel
additional.fields
security_result.detection_fields
properties.riskLevelAggregated
additional.fields
security_result.detection_fields
properties.riskLevelDuringSignIn
additional.fields
security_result.detection_fields
properties.riskState
additional.fields
security_result.detection_fields
properties.riskType
additional.fields
security_result.detection_fields
properties.userDisplayName
target.user.user_display_name
principal.user.user_display_name
record.CorrelationId
metadata.product_log_id
additional.fields
record.properties.C_DeviceId
additional.fields
principal.asset.asset_id
record.properties.resourceDisplayName
target.resource.attribute.labels
principal.resource.name
record.properties.riskDetail
additional.fields
security_result.detection_fields
record.properties.riskLevelAggregated
additional.fields
security_result.detection_fields
record.properties.riskLevelDuringSignIn
additional.fields
security_result.detection_fields
record.properties.riskState
additional.fields
security_result.detection_fields
record.properties.roles
target.user.role_name
principal.user.attribute.roles
record.properties.servicePrincipalId
additional.fields
target.resource.attribute.labels
record.properties.servicePrincipalId
additional.fields
principal.user.userid
record.RiskDetail
target.resource.attribute.labels
security_result.detection_fields
record.RiskEventTypes
target.resource.attribute.labels
security_result.detection_fields
record.RiskLevelAggregated
target.resource.attribute.labels
security_result.detection_fields
record.RiskState
target.resource.attribute.labels
security_result.detection_fields
resultType
security_result.rule_id
additional.fields
riskDetail
additional.fields
security_result.detection_fields
riskLevelAggregated
additional.fields
security_result.detection_fields
riskLevelDuringSignIn
additional.fields
security_result.detection_fields
riskState
additional.fields
security_result.detection_fields
riskState
additional.fields
security_result.detection_fields
status.additionalDetails
security_result.description
additional.fields
userDisplayName
target.user.user_display_name
principal.user.user_display_name
userId
target.user.product_object_id
principal.user.product_object_id
Event-type mapping delta
The following table lists the delta for the handling of Azure AD event types prior to January 1, 2026 and subsequently (listed in the
Old event_type
and
Current event-type
columns respectively):
Event ID from log
Old event_type
Current event_type
Remark
has_resource = true
GENERIC_EVENT
USER_RESOURCE_ACCESS
The event type maps to
USER_RESOURCE_ACCESS
for cases where the event pertains to a resource (indicated by
has_resource = true
).
operationName =  Add member to group
USER_CHANGE_PERMISSIONS
GROUP_MODIFICATION
The event type maps to
GROUP_MODIFICATION
for operations specifically involving adding a member to a group (where
operationName = Add member to group
).
Need more help?
Get answers from Community members and Google SecOps professionals.
