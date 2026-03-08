# Collect Okta User Context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-user-context/  
**Scraped:** 2026-03-05T09:27:02.933212Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Okta User Context logs
Supported in:
Google secops
SIEM
This document explains how to collect Okta User Context logs by setting up a Google Security Operations feed using the Third party API.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to Okta tenant or admin console
API token creation privileges in Okta
Configure IP allowlisting
Before creating the feed, you must allowlist Google SecOps IP ranges in your Okta firewall or network settings.
Get Google SecOps IP ranges
Fetch IP ranges from the
Google IP address ranges JSON file
.
Add IP ranges to Okta User Context
Sign in to the
Okta Admin Console
.
Go to
Security
>
Networks
.
Under
IP Address Restrictions
, click
Edit
.
Add each Google SecOps IP range in CIDR notation to the trusted IP addresses.
Click
Save
.
Configure Okta User Context API access
To enable Google SecOps to pull user context data, you need to create an API token with read permissions.
Create API token
Sign in to the
Okta Admin Console
.
Go to
Security
>
API
.
Select the
Tokens
tab.
Click
Create Token
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Integration
).
Description
(optional): Enter a description.
Click
Create Token
.
Record API credentials
After creating the API token, you'll receive the following credential:
API Token
: Your API token value (for example,
00QCGr-1d1d1d1d1d1d1d1d1d1d1d1d1d1d1d1
)
Required API permissions
The API token requires the following permissions in Okta:
Permission/Role
Access Level
Purpose
Read-Only Administrator
Read
Access user profile data
Super Administrator
Read
Complete access to all user data
Set up feeds
To configure a feed, follow these steps:
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
Okta User Context
).
Select
Third party API
as the
Source type
.
Select
Okta User Context
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Authentication HTTP header
: Enter the authentication credentials in the following format:
Authorization
:
SSWS
your
-
api
-
token
For example:
Authorization:SSWS 00QCGr-1d1d1d1d1d1d1d1d1d1d1d1d1d1d1d1
API Hostname
: The fully qualified domain name of your Okta instance (e.g. example.okta.com, not any custom domain that may be configured).
For example:
company.okta.com
Manager ID Reference Field
: ID that is required when you use a non-Okta ID to reference managers (optional).
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
After setup, the feed begins to retrieve logs from the Okta User Context instance in chronological order.
Regional endpoints
Okta uses different API endpoints based on your organization's region:
Region
Base URL / Hostname
US (Default)
{org-name}.okta.com
EU (EMEA)
{org-name}.okta-emea.com
APAC
{org-name}.okta.com.au
Preview (Testing)
{org-name}.oktapreview.com
Use the hostname that corresponds to your Okta instance region.
API rate limits
Okta API has the following rate limits:
Default rate limit
: 600 requests per minute for most endpoints
System Log API
: 60 requests per minute
User endpoints
: 600 requests per minute
Google SecOps automatically handles rate limiting with exponential backoff. If you encounter issues, contact Okta support to increase your API limits.
UDM mapping table
Log Field
UDM Mapping
Logic
activated
event.idm.entity.entity.labels
If
activated
exists, its value is added as a key-value pair with the key "activated".
created
event.idm.entity.entity.labels
If
created
exists, its value is added as a key-value pair with the key "created".
profile.costCenter
event.idm.entity.entity.labels
If
profile.costCenter
exists, its value is added as a key-value pair with the key "costCenter".
profile.Function
event.idm.entity.entity.labels
If
profile.Function
exists, its value is added as a key-value pair with the key "Function".
statusChanged
event.idm.entity.entity.labels
If
statusChanged
exists, its value is added as a key-value pair with the key "statusChanged".
type.id
event.idm.entity.entity.labels
If
type.id
exists, its value is added as a key-value pair with the key "type_id".
profile.location
event.idm.entity.entity.location.name
Value taken from
profile.location
.
profile.AD_ObjectGUID
event.idm.entity.entity.user.attribute.labels
If
profile.AD_ObjectGUID
exists, its value is added as a key-value pair with the key "AD_ObjectGUID".
profile.ADpwdLastSet
event.idm.entity.entity.user.attribute.labels
If
profile.ADpwdLastSet
exists, its value is added as a key-value pair with the key "ADpwdLastSet".
profile.AFF_Code
event.idm.entity.entity.user.attribute.labels
If
profile.AFF_Code
exists, its value is added as a key-value pair with the key "AFF_Code".
profile.Desk_Location_WD
event.idm.entity.entity.user.attribute.labels
If
profile.Desk_Location_WD
exists, its value is added as a key-value pair with the key "Desk_Location_WD".
profile.Mailing_Address_WD
event.idm.entity.entity.user.attribute.labels
If
profile.Mailing_Address_WD
exists, its value is added as a key-value pair with the key "Mailing_Address_WD".
profile.Manager_UPN
event.idm.entity.entity.user.attribute.labels
If
profile.Manager_UPN
exists, its value is added as a key-value pair with the key "Manager_UPN".
profile.PRIVATE_CONF_Profile
event.idm.entity.entity.user.attribute.labels
If
profile.PRIVATE_CONF_Profile
exists, its value is added as a key-value pair with the key "PRIVATE_CONF_Profile".
profile.Region_WD
event.idm.entity.entity.user.attribute.labels
If
profile.Region_WD
exists, its value is added as a key-value pair with the key "Region_WD".
profile.Subsidiary_Company
event.idm.entity.entity.user.attribute.labels
If
profile.Subsidiary_Company
exists, its value is added as a key-value pair with the key "Subsidiary_Company".
profile.Telephone_Work
event.idm.entity.entity.user.attribute.labels
If
profile.Telephone_Work
exists, its value is added as a key-value pair with the key "Telephone_Work".
profile.Temp_WD_Primary_Email
event.idm.entity.entity.user.attribute.labels
If
profile.Temp_WD_Primary_Email
exists, its value is added as a key-value pair with the key "Temp_WD_Primary_Email".
profile.VMware_WS1_Username
event.idm.entity.entity.user.attribute.labels
If
profile.VMware_WS1_Username
exists, its value is added as a key-value pair with the key "VMware_WS1_Username".
profile.Work_Street_Address_WD
event.idm.entity.entity.user.attribute.labels
If
profile.Work_Street_Address_WD
exists, its value is added as a key-value pair with the key "Work_Street_Address_WD".
profile.Workato_WD_Primary_Email
event.idm.entity.entity.user.attribute.labels
If
profile.Workato_WD_Primary_Email
exists, its value is added as a key-value pair with the key "Workato_WD_Primary_Email".
profile.Workday_ID
event.idm.entity.entity.user.attribute.labels
If
profile.Workday_ID
exists, its value is added as a key-value pair with the key "Workday_ID".
profile.Worker_Type_WD
event.idm.entity.entity.user.attribute.labels
If
profile.Worker_Type_WD
exists, its value is added as a key-value pair with the key "Worker_Type_WD".
profile.businessUnit
event.idm.entity.entity.user.attribute.labels
If
profile.businessUnit
exists, its value is added as a key-value pair with the key "businessUnit".
profile.companyName
event.idm.entity.entity.user.attribute.labels
If
profile.companyName
exists, its value is added as a key-value pair with the key "companyName".
profile.contingentSupplierName
event.idm.entity.entity.user.attribute.labels
If
profile.contingentSupplierName
exists, its value is added as a key-value pair with the key "contingentSupplierName".
profile.conversationId
event.idm.entity.entity.user.attribute.labels
If
profile.conversationId
exists, its value is added as a key-value pair with the key "conversationId".
profile.distinguishedName
event.idm.entity.entity.user.attribute.labels
If
profile.distinguishedName
exists, its value is added as a key-value pair with the key "distinguishedName".
profile.division
event.idm.entity.entity.user.attribute.labels
If
profile.division
exists, its value is added as a key-value pair with the key "division".
profile.emailPrefix
event.idm.entity.entity.user.attribute.labels
If
profile.emailPrefix
exists, its value is added as a key-value pair with the key "emailPrefix".
profile.employeeType
event.idm.entity.entity.user.attribute.labels
If
profile.employeeType
exists, its value is added as a key-value pair with the key "employeeType".
profile.homePostalAddress
event.idm.entity.entity.user.attribute.labels
If
profile.homePostalAddress
exists, its value is added as a key-value pair with the key "homePostalAddress".
profile.isManager
event.idm.entity.entity.user.attribute.labels
If
profile.isManager
exists, its value is added as a key-value pair with the key "isManager".
lastLogin
event.idm.entity.entity.user.attribute.labels
If
lastLogin
exists, its value is added as a key-value pair with the key "lastLogin".
profile.leaveOfAbsence
event.idm.entity.entity.user.attribute.labels
If
profile.leaveOfAbsence
exists, its value is added as a key-value pair with the key "leaveOfAbsence".
profile.managerDn
event.idm.entity.entity.user.attribute.labels
If
profile.managerDn
exists, its value is added as a key-value pair with the key "managerDn".
profile.payGroup
event.idm.entity.entity.user.attribute.labels
If
profile.payGroup
exists, its value is added as a key-value pair with the key "payGroup".
profile.wdemployeeID
event.idm.entity.entity.user.attribute.labels
If
profile.wdemployeeID
exists, its value is added as a key-value pair with the key "wdemployeeID".
profile.zipCode
event.idm.entity.entity.user.attribute.labels
If
profile.zipCode
exists, its value is added as a key-value pair with the key "zipCode".
profile.userType
event.idm.entity.entity.user.attribute.roles
If
profile.userType
exists, its value is added to an array of roles.
profile.organization
,
profile.company
event.idm.entity.entity.user.company_name
Value taken from
profile.organization
, or
profile.company
if the former is not present.
profile.department
event.idm.entity.entity.user.department
Value taken from
profile.department
.
profile.email
,
profile.secondEmail
,
profile.login
event.idm.entity.entity.user.email_addresses
Values from
profile.email
,
profile.secondEmail
, and
profile.login
(if it's an email and not a duplicate) are merged into this field.
profile.employeeNumber
event.idm.entity.entity.user.employee_id
Value taken from
profile.employeeNumber
.
profile.firstName
,
profile.Preferred_First_Name
event.idm.entity.entity.user.first_name
Value taken from
profile.firstName
, or
profile.Preferred_First_Name
if the former is not present.
profile.EmployeeWorkGroup
event.idm.entity.entity.user.group_identifiers
Value taken from
profile.EmployeeWorkGroup
.
profile.HireDate
,
profile.hiredate
event.idm.entity.entity.user.hire_date
Value is parsed from
profile.HireDate
or
profile.hiredate
if the former is not present.
profile.lastName
,
profile.preferred_Last_Name
event.idm.entity.entity.user.last_name
Value taken from
profile.lastName
if either
profile.lastName
or
profile.preferred_Last_Name
exists.
lastLogin
event.idm.entity.entity.user.last_login_time
Value is parsed from
lastLogin
.
passwordChanged
event.idm.entity.entity.user.last_password_change_time
Value is parsed from
passwordChanged
.
profile.manager
,
profile.managerEmail
,
profile.managerId
event.idm.entity.entity.user.managers
Populated with an object containing
user_display_name
from
profile.manager
,
email_addresses
from
profile.managerEmail
, and
employee_id
from
profile.managerId
.
profile.city
,
profile.firstBaseCity
event.idm.entity.entity.user.office_address.city
Value taken from
profile.city
, or
profile.firstBaseCity
if the former is not present.
profile.countryCode
,
profile.country
event.idm.entity.entity.user.office_address.country_or_region
Value taken from
profile.countryCode
, or
profile.country
if the former is not present.
profile.streetAddress
event.idm.entity.entity.user.personal_address.name
Value taken from
profile.streetAddress
.
profile.state
event.idm.entity.entity.user.personal_address.state
Value taken from
profile.state
.
profile.primaryPhone
,
profile.mobilePhone
,
profile.mobile
event.idm.entity.entity.user.phone_numbers
Values from
profile.primaryPhone
,
profile.mobilePhone
, and
profile.mobile
are merged into this field.
profile.terminationDate
,
profile.terminationdate
event.idm.entity.entity.user.termination_date
Value is parsed from
profile.terminationDate
or
profile.terminationdate
if the former is not present.
profile.title
event.idm.entity.entity.user.title
Value taken from
profile.title
.
status
event.idm.entity.entity.user.user_authentication_status
Mapped from
status
:
ACTIVE
/
RECOVERY
/
LOCKED_OUT
/
PASSWORD_EXPIRED
->
ACTIVE
;
SUSPENDED
->
SUSPENDED
;
DEPROVISIONED
->
DELETED
; otherwise
UNKNOWN_AUTHENTICATION_STATUS
.
profile.displayName
event.idm.entity.entity.user.user_display_name
Value taken from
profile.displayName
.
profile.samAccountName
,
profile.samaccountname
,
profile.login
,
profile.ldapUid
event.idm.entity.entity.user.userid
Populated with precedence:
profile.samAccountName
,
profile.samaccountname
,
profile.login
(if not an email),
profile.ldapUid
(if
profile.login
is not an email).
event.idm.entity.metadata.entity_type
Set to
USER
.
id
event.idm.entity.metadata.product_entity_id
Value taken from
id
.
event.idm.entity.metadata.product_name
Set to
Identity Cloud
.
event.idm.entity.metadata.vendor_name
Set to
Okta
.
Need more help?
Get answers from Community members and Google SecOps professionals.
