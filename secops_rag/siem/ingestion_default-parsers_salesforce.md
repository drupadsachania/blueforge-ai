# Collect Salesforce logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce/  
**Scraped:** 2026-03-05T09:27:55.974792Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Salesforce logs
Supported in:
Google secops
SIEM
This document explains how to collect Salesforce logs by setting up a Google Security Operations feed using the Third Party API.
Salesforce is a cloud-based customer relationship management (CRM) platform that provides tools for sales, service, marketing, and analytics. Salesforce logs capture user activity, security events, system changes, and API usage across the platform.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Salesforce Enterprise Edition or higher (API access enabled)
Salesforce System Administrator permissions
OpenSSL installed (for certificate generation)
Generate RSA key pair and certificate
Generate an RSA private key and self-signed X.509 certificate for JWT signing.
Generate private key
```bash
openssl genrsa -out salesforce_private.key 2048
```
Generate self-signed certificate
```bash
openssl req -new -x509 -key salesforce_private.key -out salesforce_certificate.crt -days 365
```
When prompted, enter certificate details:
Country Name
: Enter your 2-letter country code (for example,
US
).
State or Province Name
: Enter your state (for example,
California
).
Locality Name
: Enter your city (for example,
San Francisco
).
Organization Name
: Enter your organization name (for example,
Acme Corp
).
Organizational Unit Name
: Enter department (for example,
IT Security
).
Common Name
: Enter a descriptive name (for example,
Chronicle Integration
).
Email Address
: Enter contact email.
Create Salesforce External Client App
External Client Apps are the recommended method for OAuth authentication in Salesforce (Spring '26 and later).
Sign in to
Salesforce
.
Go to
Setup
(gear icon in top right).
In the
Quick Find
box, enter
External Client Apps
.
Click
External Client App Manager
.
Click
New External Client App
.
Configure basic information
Provide the following configuration details:
External Client App Name
: Enter a descriptive name (for example,
Google SecOps Integration
).
API Name
: Auto-populated based on app name. Leave as default or customize.
Contact Email
: Enter your email address.
Distribution State
: Select
Local
.
Click
Continue
.
Enable OAuth settings
Select the
Enable OAuth
checkbox.
Provide the following configuration details:
Callback URL
: Enter
https://login.salesforce.com/services/oauth2/callback
.
In the
OAuth Scopes
section, move the following scopes from
Available OAuth Scopes
to
Selected OAuth Scopes
:
Manage user data via APIs (api)
Perform requests on your behalf at any time (refresh_token, offline_access)
Enable JWT Bearer Flow and upload certificate
In the
Flow Enablement
section, select the
Enable JWT Bearer Flow
checkbox.
The
Certificate Upload
section appears.
Click
Upload Files
or drag and drop your certificate file.
Select the
salesforce_certificate.crt
file generated earlier.
Wait for the upload to complete. The certificate filename should appear below the upload button.
Configure OAuth policies
In the
OAuth Policies
section:
Permitted Users
: Select
Admin approved users are pre-authorized
.
Click
Save
.
Get Consumer Key
After creating the External Client App, retrieve the Consumer Key for Chronicle configuration.
In the
External Client App Manager
, click on your app name (for example,
Google SecOps Integration
).
Go to the
Settings
tab.
In the
OAuth Settings
section, click
Consumer Key and Secret
.
Copy and save the
Consumer Key
value.
Example Consumer Key format:
```
3MVG9IKcPoNiNVBIPjdw4z.pcfRjTFBp7xC8x9k4U8jZ0HlLQdPqX5bKjR8yNzQ9_YvY.8xD3F2W6nXb5YgNx
```
Pre-authorize the External Client App
Salesforce requires pre-authorization for JWT Bearer Flow. Pre-authorize by assigning the External Client App to a user via permission set.
Create permission set
Go to
Setup
>
Users
>
Permission Sets
.
Click
New
.
Provide the following configuration details:
Label
: Enter
Chronicle Integration Users
(for example).
API Name
: Auto-populated based on label.
Click
Save
.
Assign permission set to External Client App
Go to
Setup
>
External Client App Manager
.
Click on your External Client App (for example,
Google SecOps Integration
).
Click the
Policies
tab.
In the
App Policies
section, under
Select Permission Sets
:
Move your permission set (for example,
Chronicle Integration Users
) from
Available Permission Sets
to
Selected Permission Sets
.
Click
Save
.
Assign permission set to user
From the permission set detail page, click
Manage Assignments
.
Click
Add Assignments
.
Select the checkbox next to the user account that will be used for Chronicle integration (for example,
integration@acme.com
).
Click
Assign
.
Click
Done
.
Configure a feed in Google SecOps to ingest Salesforce logs
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
Salesforce EventLogFile
).
Select
Third Party API
as the
Source type
.
Select
SALESFORCE
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
API Hostname
: Enter your Salesforce instance hostname (for example,
acme.my.salesforce.com
).
*
**
OAuth
JWT
Endpoint
**
:
Enter
the
OAuth
token
endpoint
URL
:
-
Production
orgs
:
`
https
:
//
login
.
salesforce
.
com
/
services
/
oauth2
/
token
`
-
Sandbox
orgs
:
`
https
:
//
test
.
salesforce
.
com
/
services
/
oauth2
/
token
`
-
My
Domain
:
`
https
:
//
acme
.
my
.
salesforce
.
com
/
services
/
oauth2
/
token
`
*
**
JWT
Claims
Issuer
**
:
Enter
the
Consumer
Key
from
the
External
Client
App
.
*
**
JWT
Claims
Subject
**
:
Enter
the
Salesforce
username
of
the
pre
-
authorized
user
(
for
example
,
`
integration
@acme
.
com
`
).
*
**
JWT
Claims
Audience
**
:
Enter
the
authorization
server
URL
:
-
Production
orgs
:
`
https
:
//
login
.
salesforce
.
com
`
-
Sandbox
orgs
:
`
https
:
//
test
.
salesforce
.
com
`
-
My
Domain
:
`
https
:
//
acme
.
my
.
salesforce
.
com
`
*
**
RSA
Private
Key
**
:
Paste
the
complete
private
key
contents
including
`
-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` markers.
To get the private key contents:
```bash
cat salesforce_private.key
```
Copy the entire output including the header and footer lines.
*
**
Asset
namespace
**:
The
[
asset
namespace
](
/
chronicle
/
docs
/
investigation
/
asset
-
namespaces
).
*
**
Ingestion
labels
**:
The
label
to
be
applied
to
the
events
from
this
feed
.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Salesforce instance types reference
The OAuth JWT endpoint and audience values depend on your Salesforce instance type:
| Instance Type       | OAuth JWT Endpoint                                      | JWT Claims Audience              | API Hostname Format                    |
| ------------------- | ------------------------------------------------------- | -------------------------------- | -------------------------------------- |
| **Production**      |
`https://login.salesforce.com/services/oauth2/token`
|
`https://login.salesforce.com`
|
`company.my.salesforce.com`
|
| **Sandbox**         |
`https://test.salesforce.com/services/oauth2/token`
|
`https://test.salesforce.com`
|
`company--sandbox.sandbox.my.salesforce.com`
|
| **My Domain**       |
`https://domain.my.salesforce.com/services/oauth2/token`
|
`https://domain.my.salesforce.com`
|
`domain.my.salesforce.com`
|

Note: "My Domain" is recommended for production deployments. "My Domain" provides a custom, branded login URL and is required for certain Salesforce features.
UDM mapping table
Log Field
UDM Mapping
Logic
Account.Name
target.resource.name
The value of
Account.Name
from the raw log.
AccountId
target.resource.id
The value of
AccountId
from the raw log.
Action
security_result.description
The value of
Action
from the raw log.
AdditionalInfo
-
Not mapped to the IDM object.
ApiType
target.application
The value of
ApiType
from the raw log.
ApiVersion
-
Not mapped to the IDM object.
Application
principal.application
The value of
Application
from the raw log, or "Browser" for LoginAsEvent, or "Integration JWT Token" for LoginEvent, or "SfdcSiqActivityPlatform" for LoginHistory with objecttype LoginHistory, or "N/A" for ApiEvent, or "Browser" for LoginAsEventStream.
attributes.url
target.url
The value of
attributes.url
from the raw log, or specific URLs for various event types from the raw log.
attributes.type
metadata.product_event_type
The value of
attributes.type
from the raw log.
AuthSessionId
network.session_id
The value of
AuthSessionId
from the raw log.
Browser
principal.resource.name
The value of
Browser
from the raw log, or "Unknown" if
Browser
is not available in raw log and
Application
is "Insights", or "Java (Salesforce.com)" for LoginHistory with
ApiType
as "SOAP Partner", or "Unknown" for LoginHistory with
Application
as "SfdcSiqActivityPlatform", or from data.properties.Browser.str for LoginAsEventStream.
Case.Subject
target.resource.name
The value of
Case.Subject
from the raw log.
CaseId
target.resource.id
The value of
CaseId
from the raw log.
cat
metadata.product_event_type
The value of
cat
from the raw log.
City
principal.location.city
The value of
City
from the raw log, or from
LoginGeo.City
for LoginHistory.
Client
principal.labels
The value of
Client
from the raw log, formatted as a label.
CLIENT_IP
principal.ip
,
principal.asset.ip
The value of
CLIENT_IP
from the raw log.
ClientVersion
-
Not mapped to the IDM object.
CipherSuite
network.tls.cipher
The value of
CipherSuite
from the raw log.
ColumnHeaders
principal.labels
The value of
ColumnHeaders
from the raw log, formatted as a label.
ConnectedAppId
principal.labels
The value of
ConnectedAppId
from the raw log, formatted as a label.
Contact.Name
target.resource.name
The value of
Contact.Name
from the raw log.
ContactId
target.resource.id
The value of
ContactId
from the raw log.
Country
principal.location.country_or_region
The value of
Country
from the raw log, or
LoginGeo.Country
for LoginHistory.
CreatedByContext
principal.user.userid
The value of
CreatedByContext
from the raw log.
CreatedById
principal.resource.attribute.labels
The value of
CreatedById
from the raw log, formatted as a label.
CreatedDate
metadata.collected_timestamp
The value of
CreatedDate
from the raw log, or the current timestamp if not available.
CPU_TIME
target.resource.attribute.labels
The value of
CPU_TIME
from the raw log, formatted as a label.
data
-
Contains various fields that are extracted and mapped individually.
DATASET_IDS
target.resource.name
The value of
DATASET_IDS
from the raw log.
DelegatedOrganizationId
target.administrative_domain
The value of
DelegatedOrganizationId
from the raw log.
DelegatedUsername
observer.user.userid
The value of
DelegatedUsername
from the raw log.
Description
metadata.description
The value of
Description
from the raw log.
DevicePlatform
principal.resource.type
The value of
DevicePlatform
from the raw log, parsed to extract the resource type.
Display
metadata.description
The value of
Display
from the raw log.
DOWNLOAD_FORMAT
target.resource.attribute.labels
The value of
DOWNLOAD_FORMAT
from the raw log, formatted as a label.
Duration
target.resource.attribute.labels
The value of
Duration
from the raw log, formatted as a label.
ENTITY_NAME
target.resource.attribute.labels
The value of
ENTITY_NAME
from the raw log, formatted as a label.
ErrorCode
security_result.action
The value of
ErrorCode
from the raw log, transformed to ALLOW or BLOCK.
EventDate
timestamp
The value of
EventDate
from the raw log, or
data.properties.TIMESTAMP_DERIVED.str
if available, or
data.properties.TIMESTAMP_DERIVED_FIRST.str
if available, or
@timestamp
if available, or
created_date
if available, or
timestamp
if available, or
LoginTime
for LoginHistory.
EventIdentifier
metadata.product_log_id
The value of
EventIdentifier
from the raw log.
EventType
metadata.product_event_type
The value of
EventType
from the raw log.
Id
principal.user.userid
The value of
Id
from the raw log, or
metadata.product_log_id
for SetupAuditTrail and other events.
IdentityUsed
principal.user.email_addresses
The value of
IdentityUsed
from the raw log.
Lead.Name
target.resource.name
The value of
Lead.Name
from the raw log.
LeadId
target.resource.id
The value of
LeadId
from the raw log.
LoginAsCategory
-
Not mapped to the IDM object.
LoginGeo.Country
principal.location.country_or_region
The value of
LoginGeo.Country
from the raw log.
LoginHistoryId
-
Not mapped to the IDM object.
LoginKey
principal.user.userid
,
network.session_id
The value of
LoginKey
from the raw log, or
CreatedByContext
for SetupAuditTrail.
LoginTime
timestamp
The value of
LoginTime
from the raw log.
LoginType
security_result.description
The value of
LoginType
from the raw log, or "Other Apex API" for LoginHistory with
ApiType
as "SOAP Partner", or "Remote Access 2.0" for LoginHistory with
Application
as "SfdcSiqActivityPlatform".
LoginUrl
target.url
,
principal.url
The value of
LoginUrl
from the raw log.
LogFile
principal.resource.attribute.labels
The value of
LogFile
from the raw log, formatted as a label.
LogFileContentType
principal.resource.attribute.labels
The value of
LogFileContentType
from the raw log, formatted as a label.
LogFileLength
principal.resource.attribute.labels
The value of
LogFileLength
from the raw log, formatted as a label.
Message
-
Not mapped to the IDM object.
METHOD
network.http.method
The value of
METHOD
from the raw log.
Name
target.application
The value of
Name
from the raw log.
NewValue
-
Used in conjunction with
OldValue
to generate
security_result.summary
.
NUMBER_FIELDS
target.resource.attribute.labels
The value of
NUMBER_FIELDS
from the raw log, formatted as a label.
OldValue
-
Used in conjunction with
NewValue
to generate
security_result.summary
.
Operation
security_result.description
,
target.resource.attribute.labels
The value of
Operation
from the raw log, or
Display
for SetupAuditTrail.
OperationStatus
security_result.action
The value of
OperationStatus
from the raw log, transformed to ALLOW or BLOCK.
ORGANIZATION_ID
target.administrative_domain
The value of
ORGANIZATION_ID
from the raw log.
OsName
principal.platform
The value of
OsName
from the raw log.
OsVersion
principal.platform_version
The value of
OsVersion
from the raw log.
Platform
principal.platform
The value of
Platform
from the raw log, or from
data.properties.OsName.str
for LightningUriEventStream, or from
data.properties.OsName.str
for LoginEventStream.
QueriedEntities
target.resource.name
,
principal.labels
The value of
QueriedEntities
from the raw log, or
component_name
for UriEvent and ApiEvent.
Query
target.process.command_line
,
principal.labels
The value of
Query
from the raw log.
RecordId
target.resource.id
The value of
RecordId
from the raw log.
Records
principal.labels
The value of
Records
from the raw log, formatted as a label.
REQUEST_ID
metadata.product_log_id
,
target.resource.product_object_id
The value of
REQUEST_ID
from the raw log.
REQUEST_SIZE
network.sent_bytes
The value of
REQUEST_SIZE
from the raw log.
REQUEST_STATUS
security_result.summary
The value of
REQUEST_STATUS
from the raw log.
RESPONSE_SIZE
network.received_bytes
The value of
RESPONSE_SIZE
from the raw log.
RowsProcessed
target.resource.attribute.labels
The value of
RowsProcessed
from the raw log, formatted as a label.
RUN_TIME
target.resource.attribute.labels
The value of
RUN_TIME
from the raw log, formatted as a label.
SamlEntityUrl
-
Not mapped to the IDM object.
SdkAppType
-
Not mapped to the IDM object.
SdkAppVersion
-
Not mapped to the IDM object.
SdkVersion
-
Not mapped to the IDM object.
Section
security_result.summary
The value of
Section
from the raw log.
SessionKey
network.session_id
The value of
SessionKey
from the raw log.
SessionLevel
target.resource.attribute.labels
The value of
SessionLevel
from the raw log, formatted as a label.
SourceIp
principal.ip
,
principal.asset.ip
The value of
SourceIp
from the raw log.
src
principal.ip
,
principal.asset.ip
The value of
src
from the raw log.
SsoType
target.resource.attribute.labels
The value of
SsoType
from the raw log, formatted as a label.
STATUS_CODE
network.http.response_code
The value of
STATUS_CODE
from the raw log.
Status
security_result.action
,
security_result.action_details
The value of
Status
from the raw log, transformed to ALLOW or BLOCK, or used as action details for LoginEventStream.
Subject
target.resource.name
The value of
Subject
from the raw log.
TargetUrl
-
Not mapped to the IDM object.
TIMESTAMP
metadata.collected_timestamp
The value of
TIMESTAMP
from the raw log.
TIMESTAMP_DERIVED
timestamp
The value of
TIMESTAMP_DERIVED
from the raw log.
TlsProtocol
network.tls.version_protocol
The value of
TlsProtocol
from the raw log.
URI
target.url
The value of
URI
from the raw log.
USER_AGENT
network.http.user_agent
The value of
USER_AGENT
from the raw log.
USER_ID
principal.user.userid
The value of
USER_ID
from the raw log.
USER_ID_DERIVED
principal.user.product_object_id
,
target.resource.attribute.labels
The value of
USER_ID_DERIVED
from the raw log.
UserId
principal.user.userid
The value of
UserId
from the raw log.
USER_TYPE
target.resource.attribute.labels
The value of
USER_TYPE
from the raw log, formatted as a label.
Username
principal.user.userid
,
principal.user.email_addresses
,
target.user.email_addresses
The value of
Username
from the raw log, or
src_email
for various events, or
IdentityUsed
for IdentityProviderEventStore, or
data.properties.Email.str
for Search and SearchAlert, or
data.properties.Username.str
for LoginAsEventStream and LoginEventStream.
UserType
target.resource.attribute.labels
The value of
UserType
from the raw log, formatted as a label.
usrName
principal.user.userid
,
principal.user.email_addresses
,
target.user.email_addresses
The value of
usrName
from the raw log.
VerificationMethod
target.resource.attribute.labels
The value of
VerificationMethod
from the raw log, formatted as a label.
Parser Logic
metadata.event_type
Derived based on the
event_id
and
operation
fields, or set to "USER_LOGIN" for LoginEventStream, "USER_LOGOUT" for Logout and LogoutEvent, "USER_RESOURCE_UPDATE_CONTENT" for various events, "USER_RESOURCE_UPDATE_PERMISSIONS" for PlatformEncryption, "RESOURCE_READ" for QueuedExecution, ApexExecution, LightningInteraction, LightningPerformance, LightningPageView, URI, RestApi, API, AuraRequest, ApexCallout, OneCommerceUsage, Sites, MetadataApiOperation, OneCommerceUsage, VisualforceRequest, Dashboard, Search, ListViewEvent, "RESOURCE_CREATION" for UriEvent and TimeBasedWorkflow with
Operation
as "Create" or "INSERT", "RESOURCE_WRITTEN" for UriEvent and LightningUriEvent with
Operation
as "Update", "RESOURCE_DELETION" for UriEvent with
Operation
as "Delete" or "ROLLBACK", "USER_UNCATEGORIZED" for SetupAuditTrail and AuditTrail, "USER_CHANGE_PASSWORD" for SetupAuditTrail with
operation
as "namedCredentialEncryptedFieldChange", "GENERIC_EVENT" for ApiEventStream and LightningUriEventStream, or based on network and principal presence.
Parser Logic
metadata.ingestion_labels
Labels indicating the source of the event, either "Event Log File" or "Real-Time Event Monitoring" or "SetupAuditTrail".
Parser Logic
metadata.log_type
Always set to "SALESFORCE".
Parser Logic
metadata.product_name
Always set to "SALESFORCE".
Parser Logic
metadata.vendor_name
Always set to "SALESFORCE".
Parser Logic
metadata.url_back_to_product
Constructed from various fields like
LoginUrl
,
attributes.url
,
data.properties.PageUrl.str
,
data.properties.LoginUrl.str
.
Parser Logic
network.application_protocol
Set to "HTTPS" if the
uri
field starts with "http".
Parser Logic
network.http.referral_url
Extracted from the
user_agent
field if it contains "Referer=".
Parser Logic
network.http.response_code
Derived from
request_status
for various events.
Parser Logic
network.http.user_agent
The value of
user_agent
from the raw log, or from
data.properties.UserAgent.str
for ApiEventStream and LoginEventStream, or from
Sites
events, or "User-Agent" from
Sites
events.
Parser Logic
network.session_id
The value of
session_key
or
SESSION_KEY
from the raw log, or constructed from other fields like
LoginKey
or
AuthSessionId
.
Parser Logic
network.tls.version
The value of
tls_protocol
from the raw log, or from
data.properties.TlsProtocol.str
for LoginEventStream.
Parser Logic
principal.application
The value of
application
from the raw log, or "Salesforce for Outlook" for Login: Success events, or "Insights" for Login: Success events with no Application, or extracted from
device_platform
for Lightning events.
Parser Logic
principal.asset.hostname
The value of
client_ip
if it is a hostname.
Parser Logic
principal.asset.ip
The value of
client_ip
or
src_ip
or
SourceIp
or
CLIENT_IP
if it is an IP address.
Parser Logic
principal.hostname
The value of
client_ip
if it is a hostname.
Parser Logic
principal.ip
The value of
client_ip
or
src_ip
or
SourceIp
or
CLIENT_IP
if it is an IP address.
Parser Logic
principal.labels
Labels constructed from various fields like
FederationIdentifier
,
ApiType
,
OrgId
,
channel
.
Parser Logic
principal.location.city
The value of
geoip_src.city_name
or
City
or
LoginGeo.City
from the raw log.
Parser Logic
principal.location.country_or_region
The value of
geoip_src.country_name
or
Country
or
LoginGeo.Country
or
client_geo
from the raw log.
Parser Logic
principal.location.region_latitude
The value of
data.properties.LoginLatitude.number
from the raw log.
Parser Logic
principal.location.region_longitude
The value of
data.properties.LoginLongitude.number
from the raw log.
Parser Logic
principal.location.state
The value of
geoip_src.region_name
from the raw log.
Parser Logic
principal.platform
The value of
Platform
or
OsName
or
os_name
from the raw log, or "WINDOWS" for LoginEventStream with
Platform
containing "Windows".
Parser Logic
principal.platform_version
The value of
OsVersion
or
os_version
from the raw log, or extracted from
Platform
for LoginEventStream with
Platform
containing "Windows".
Parser Logic
principal.resource.attribute.labels
Labels constructed from various fields like
CreatedById
,
ApiVersion
,
LogFile
,
LogFileContentType
,
LogFileLength
.
Parser Logic
principal.resource.name
The value of
Browser
or
browser_name
from the raw log, or "Java (Salesforce.com)" for LoginHistory with
ApiType
as "SOAP Partner".
Parser Logic
principal.resource.type
Extracted from
device_platform
for Lightning events, or "Browser" for LoginAsEvent and LoginAsEventStream.
Parser Logic
principal.url
The value of
LoginUrl
from the raw log.
Parser Logic
principal.user.email_addresses
The value of
usrName
or
Username
or
src_email
or
IdentityUsed
or
data.properties.Username.str
or
data.properties.Email.str
from the raw log.
Parser Logic
principal.user.product_object_id
The value of
attrs.USER_ID_DERIVED
or
data.properties.USER_ID_DERIVED.str
from the raw log.
Parser Logic
principal.user.userid
The value of
usrName
or
Username
or
user_id
or
UserId
or
USER_ID
or
Id
or
LoginKey
or
CreatedByContext
or
data.properties.Username.str
or
data.properties.USER_ID.str
or
data.properties.LoginKey.str
from the raw log.
Parser Logic
security_result.action
Derived from
Status
or
OperationStatus
or
ErrorCode
or
action
or
operation_status
from the raw log, transformed to ALLOW or BLOCK.
Parser Logic
security_result.action_details
The value of
Status
from the raw log for LoginEventStream.
Parser Logic
security_result.description
The value of
LoginType
or
logintype
or
Operation
or
Action
or
Display
from the raw log.
Parser Logic
security_result.rule_name
The value of
Policy
or
rule_name
from the raw log.
Parser Logic
security_result.summary
Constructed from
NewValue
and
OldValue
or
REQUEST_STATUS
or
Section
or
forecastcategory
from the raw log.
Parser Logic
target.administrative_domain
The value of
ORGANIZATION_ID
or
DelegatedOrganizationId
or
organization_id
or
data.properties.OrgName.str
from the raw log.
Parser Logic
target.application
The value of
Application
or
app_name
or
ApiType
or
Name
or
data.properties.Application.str
from the raw log.
Parser Logic
target.asset.hostname
The value of
target_hostname
extracted from the
uri
field.
Parser Logic
target.asset.ip
The value of
data.properties.CLIENT_IP.str
from the raw log.
Parser Logic
target.asset_id
Constructed from
device_id
or
REQUEST_ID
.
Parser Logic
target.file.mime_type
The value of
file_type
from the raw log.
Parser Logic
target.file.size
The value of
size_bytes
from the raw log.
Parser Logic
target.hostname
The value of
target_hostname
extracted from the
uri
field.
Parser Logic
target.process.command_line
The value of
query_exec
or
Query
or
data.properties.Query.str
from the raw log.
Parser Logic
target.process.pid
The value of
job_id
from the raw log.
Parser Logic
target.resource.attribute.labels
Labels constructed from various fields like
CPU_TIME
,
RUN_TIME
,
USER_TYPE
,
DB_TOTAL_TIME
,
MEDIA_TYPE
,
ROWS_PROCESSED
,
NUMBER_FIELDS
,
DB_BLOCKS
,
DB_CPU_TIME
,
ENTITY_NAME
,
EXCEPTION_MESSAGE
,
USER_ID_DERIVED
,
DOWNLOAD_FORMAT
,
USER_TYPE
,
CPU_TIME
,
RUN_TIME
,
WAVE_SESSION_ID
,
SessionLevel
,
verification_method
,
cpu_time
,
run_time
,
db_total_time
,
db_cpu_time
,
exec_time
,
callout_time
,
number_soql_queries
,
duration
,
user_type
,
entry_point
,
operation
,
session_level
,
rows_processed
,
sso_type
,
dashboard_type
,
Operation
,
SessionLevel
.
Parser Logic
target.resource.id
The value of
REQUEST_ID
or
RecordId
or
caseid
or
leadid
or
contactid
or
opportunityid
or
accountid
from the raw log.
Parser Logic
target.resource.name
The value of
QueriedEntities
or
resource_name
or
component_name
or
DATASET_IDS
or
field
or
StageName
or
Subject
from the raw log.
Parser Logic
target.resource.product_object_id
The value of
REQUEST_ID
from the raw log.
Parser Logic
target.resource.resource_type
Set to "ACCESS_POLICY" for ApexCallout and PlatformEncryption, or "DATABASE" for ApexTrigger, or "FILE" for ContentTransfer, or "TABLE" for ApiEvent.
Parser Logic
target.resource.type
Set to "BATCH" for QueuedExecution and ApexExecution, or "FILE" for ContentTransfer, or "DATABASE_TRIGGER" for ApexTrigger, or "Case", "Lead", "Contact", "Opportunity", "Account" based on the presence of corresponding ID fields.
Parser Logic
target.url
The value of
LoginUrl
or
URI
or
attributes.url
or
login_url
or
uri
from the raw log.
Parser Logic
target.user.email_addresses
The value of
Username
or
attrs.usrName
or
email_address
from the raw log.
Parser Logic
target.user.user_display_name
The value of
target_user_display_name
or
user_name
or
username
from the raw log.
Parser Logic
target.user.userid
The value of
target_user_name
or
data.properties.UserId.str
or
data.properties.CreatedById.str
from the raw log.
Parser Logic
extensions.auth.auth_details
Set to "ACTIVE" if
Status
is not "Success", otherwise set to "UNKNOWN_AUTHENTICATION_STATUS".
Parser Logic
extensions.auth.mechanism
Set to "REMOTE" for Login: Success and Login events with
logintype
containing "Remote", or "USERNAME_PASSWORD" for LoginEventStream, or "MECHANISM_OTHER" for events with
login_url
present, or "AUTHTYPE_UNSPECIFIED" for Login: Success and Logout events.
Parser Logic
extensions.auth.type
Set to "SSO" for Login, Logout, LogoutEvent, LoginAs, IdentityProviderEventStore, LoginHistory, LoginAsEvent with LoginType as "SAML Sfdc Initiated SSO", or "AUTHTYPE_UNSPECIFIED" for Login: Success, Logout, LoginAsEvent with LoginType as "Application".
Need more help?
Get answers from Community members and Google SecOps professionals.
