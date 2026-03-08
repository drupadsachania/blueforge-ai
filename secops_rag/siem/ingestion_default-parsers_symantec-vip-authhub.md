# Collect Symantec VIP Authentication Hub logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip-authhub/  
**Scraped:** 2026-03-05T09:28:46.979091Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec VIP Authentication Hub logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec VIP Authentication Hub logs to
Google Security Operations using Bindplane. The parser code first cleans and
preprocesses the input log message, converting specific fields and restructuring
data from key-value pairs. Then, it extracts relevant information from various
fields using grok patterns and conditional logic, mapping them to the
corresponding attributes within the Unified Data Model (UDM) for standardized
security event representation.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Symantec VIP Authentication Hub
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the
system where Bindplane will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Install the Bindplane agent
Windows installation
Open the
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
ingestion_labels
:
log_type
:
'SYMANTEC_VIP_AUTHHUB'
raw_log_field
:
body
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the
authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog in Symantec VIP Authentication Hub
Sign in to your
Symantec VIP Gateway
web UI.
Go to
Logs
>
Syslog Configuration
.
If you are configuring Syslog for the first time, you are prompted to configure the Syslog settings. Select
Yes
.
If you have already configured Syslog, click
Edit
at the bottom of the page.
Provide the following configuration details:
Syslog Facility
: Select
LOG_LOCAL0
.
Syslog Host
: Enter the Bindplane agent IP address.
Syslog Port
: Enter the Bindplane agent port number (for example,
514
for
UDP
).
Click
Save
.
Go to
Identity providers
>
Self Service Portal Configuration
.
Edit the following configuration details:
Logging Level
: Select
Info
.
Enable Syslog
: Select
Yes
.
Click
Submit
.
Go to
Identity providers
>
VIP Manager Authentication Configuration
.
Edit the following configuration details:
Logging Level
: Select
Info
.
Enable Syslog
: Select
Yes
.
Click
Submit
.
Go to
User Store
>
LDAP Directory Synchronization
.
Edit the following configuration details:
Log Level
: Select
Info
.
Enable Syslog
: Select
Yes
.
Click
Submit
.
UDM mapping table
Log field
UDM mapping
Logic
/auth/v1/authenticate
security_result.detection_fields[].value
The value is taken from the
/auth/v1/authenticate
field in the raw log and assigned to a
security_result.detection_fields
object with the key
api
.
__isAuditIdLcmIdStore
additional.fields[].value.string_value
The value is taken from the
__isAuditIdLcmIdStore
field in the raw log and assigned to an
additional.fields
object with the key
__isAuditIdLcmIdStore
.
accessTokenScopes
security_result.detection_fields[].value
The value is taken from the
accessTokenScopes
field in the raw log and assigned to a
security_result.detection_fields
object with the key
accessTokenScopes
.
accessTokenTid
security_result.detection_fields[].value
The value is taken from the
accessTokenTid
field in the raw log and assigned to a
security_result.detection_fields
object with the key
accessTokenTid
.
api
security_result.detection_fields[].value
The value is taken from the
api
field in the raw log and assigned to a
security_result.detection_fields
object with the key
api
.
appId
additional.fields[].value.string_value
The value is taken from the
appId
field in the raw log and assigned to an
additional.fields
object with the key
appId
.
appName
principal.application
The value is taken from the
appName
field in the raw log.
azpName
additional.fields[].value.string_value
The value is taken from the
azpName
field in the raw log and assigned to an
additional.fields
object with the key
azpName
.
bytes_sent
network.sent_bytes
The value is taken from the
bytes_sent
field in the raw log.
client
principal.asset.ip
,
principal.ip
The IP address is extracted from the
client
field in the raw log using a grok pattern and added to the
principal.ip
and
principal.asset.ip
fields.
clientId
additional.fields[].value.string_value
,
principal.user.userid
The value is taken from the
clientId
field in the raw log and assigned to an
additional.fields
object with the key
clientId
. If the
clientId
field is not empty, it is also used to populate the
principal.user.userid
field.
clientIp
principal.asset.ip
,
principal.ip
The value is taken from the
clientIp
field in the raw log and added to the
principal.ip
and
principal.asset.ip
fields.
clientTid
additional.fields[].value.string_value
The value is taken from the
clientTid
field in the raw log and assigned to an
additional.fields
object with the key
clientTid
.
clientTxnId
additional.fields[].value.string_value
The value is taken from the
clientTxnId
field in the raw log and assigned to an
additional.fields
object with the key
clientTxnId
.
contentType
additional.fields[].value.string_value
The value is taken from the
contentType
field in the raw log and assigned to an
additional.fields
object with the key
contentType
.
countryISO
principal.location.country_or_region
The value is taken from the
countryISO
field in the raw log.
eventId
metadata.product_event_type
The value is taken from the
eventId
field in the raw log.
flowStateId
additional.fields[].value.string_value
The value is taken from the
flowStateId
field in the raw log and assigned to an
additional.fields
object with the key
flowStateId
.
geo.city_name
principal.location.city
The value is taken from the
geo.city_name
field in the raw log.
geo.country_name
principal.location.country_or_region
The value is taken from the
geo.country_name
field in the raw log.
geo.location.lat
principal.location.region_coordinates.latitude
The value is taken from the
geo.location.lat
field in the raw log, converted to a float, and renamed to
principal.location.region_coordinates.latitude
.
geo.location.lon
principal.location.region_coordinates.longitude
The value is taken from the
geo.location.lon
field in the raw log, converted to a float, and renamed to
principal.location.region_coordinates.longitude
.
guid
metadata.product_log_id
The value is taken from the
guid
field in the raw log.
host
principal.asset.hostname
,
principal.hostname
The value is taken from the
host
field in the raw log, stripped of any quotes, and added to the
principal.hostname
and
principal.asset.hostname
fields.
httpMethod
network.http.method
The value is taken from the
httpMethod
field in the raw log.
httpReferrer
network.http.referral_url
The value is taken from the
httpReferrer
field in the raw log.
identitySourceId
additional.fields[].value.string_value
The value is taken from the
identitySourceId
field in the raw log and assigned to an
additional.fields
object with the key
identitySourceId
.
internal-user-sync-ext-resourceGuid
target.user.userid
The value is taken from the
internal-user-sync-ext-resourceGuid
field in the raw log.
internal-user-sync-ext-resourceName
target.user.email_addresses
The value is taken from the
internal-user-sync-ext-resourceName
field in the raw log and added to the
target.user.email_addresses
field.
issuerUrl
target.url
The value is taken from the
issuerUrl
field in the raw log.
kubernetes.annotations.cni.projectcalico.org_containerID
target.resource.product_object_id
The value is taken from the
kubernetes.annotations.cni.projectcalico.org_containerID
field in the raw log.
kubernetes.annotations.cni.projectcalico.org_podIP
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.annotations.cni.projectcalico.org_podIP
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
podIP
.
kubernetes.annotations.cni.projectcalico.org_podIPs
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.annotations.cni.projectcalico.org_podIPs
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
podIPs
.
kubernetes.container_hash
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.container_hash
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
container_hash
.
kubernetes.container_image
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.container_image
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
container_image
.
kubernetes.container_name
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.container_name
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
container_name
.
kubernetes.docker_id
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.docker_id
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
docker_id
.
kubernetes.host
principal.asset.hostname
,
principal.hostname
The value is taken from the
kubernetes.host
field in the raw log and added to the
principal.hostname
and
principal.asset.hostname
fields.
kubernetes.labels.app
This field is not mapped to the IDM object in the UDM.
kubernetes.labels.app.kubernetes.io/component
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.app.kubernetes.io/component
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
io_component
.
kubernetes.labels.app.kubernetes.io/instance
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.app.kubernetes.io/instance
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
io_instance
.
kubernetes.labels.app.kubernetes.io/managed-by
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.app.kubernetes.io/managed-by
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
io_managed-by
.
kubernetes.labels.app.kubernetes.io/name
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.app.kubernetes.io/name
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
io_name
.
kubernetes.labels.app.kubernetes.io/part-of
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.app.kubernetes.io/part-of
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
io_part-of
.
kubernetes.labels.app.kubernetes.io/version
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.app.kubernetes.io/version
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
io_version
.
kubernetes.labels.helm.sh/chart
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.helm.sh/chart
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
helm_sh_chart
.
kubernetes.labels.helmChartName
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.helmChartName
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
helmChartName
.
kubernetes.labels.imageTag
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.imageTag
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
imageTag
.
kubernetes.labels.pod-template-hash
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.labels.pod-template-hash
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
pod-template-hash
.
kubernetes.namespace_name
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.namespace_name
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
namespace_name
.
kubernetes.pod_id
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.pod_id
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
pod_id
.
kubernetes.pod_name
target.resource.attribute.labels[].value
The value is taken from the
kubernetes.pod_name
field in the raw log and assigned to a
target.resource.attribute.labels
object with the key
pod_name
.
level
security_result.severity
If the
level
field in the raw log matches
notice
or
info
(case-insensitive), the
security_result.severity
field is set to
INFORMATIONAL
.
log
security_result.description
,
level
,
kv_data
The
level
and
kv_data
fields are extracted from the
log
field in the raw log using a grok pattern. The
security_result.description
field is populated with the entire
log
field.
logtag
additional.fields[].value.string_value
The value is taken from the
logtag
field in the raw log and assigned to an
additional.fields
object with the key
logtag
.
method
network.http.method
The value is taken from the
method
field in the raw log.
msg
metadata.event_type
,
security_result.description
The value is taken from the
msg
field in the raw log and used to populate the
security_result.description
field. The
metadata.event_type
field is determined based on the content of the
msg
field:  *
USER_CREATION
if
msg
contains
Internal user created or updated
. *
USER_LOGIN
if
msg
contains
Authorization Initiated Succesfully
,
Authentication Initiated Successfully
, or
Authentication Successful
. *
USER_RESOURCE_ACCESS
if
msg
contains
Token Generated
or
token verified
. *
NETWORK_CONNECTION
if both
has_principal
and
has_target
are true. *
STATUS_UPDATE
if
has_principal
is true. *
GENERIC_EVENT
otherwise.
path
principal.file.full_path
The value is taken from the
path
field in the raw log.
principalId
additional.fields[].value.string_value
,
principal.user.userid
The value is taken from the
principalId
field in the raw log and assigned to an
additional.fields
object with the key
principalId
. If the
principalId
field is not
clientId
and is not empty, it is also used to populate the
principal.user.userid
field.
principalType
additional.fields[].value.string_value
The value is taken from the
principalType
field in the raw log and assigned to an
additional.fields
object with the key
principalType
.
protocol
network.application_protocol
If the
protocol
field in the raw log matches
HTTP
(case-insensitive), the
network.application_protocol
field is set to
HTTP
.
referrer
network.http.referral_url
The value is taken from the
referrer
field in the raw log, stripped of any quotes, and assigned to the
network.http.referral_url
field.
relVersion
metadata.product_version
The value is taken from the
relVersion
field in the raw log.
remoteAddr
additional.fields[].value.string_value
The value is taken from the
remoteAddr
field in the raw log and assigned to an
additional.fields
object with the key
remoteAddr
.
requestId
additional.fields[].value.string_value
The value is taken from the
requestId
field in the raw log and assigned to an
additional.fields
object with the key
requestId
.
requestTime
additional.fields[].value.string_value
The value is taken from the
requestTime
field in the raw log and assigned to an
additional.fields
object with the key
requestTime
.
responseCode
network.http.response_code
The numeric value is extracted from the
responseCode
field in the raw log using a grok pattern, converted to an integer, and assigned to the
network.http.response_code
field.
request
method
,
path
,
protocol
The
method
,
path
, and
protocol
fields are extracted from the
request
field in the raw log using a grok pattern after stripping any quotes.
server
target.asset.hostname
,
target.hostname
The value is taken from the
server
field in the raw log and added to the
target.hostname
and
target.asset.hostname
fields.
service
additional.fields[].value.string_value
The value is taken from the
service
field in the raw log and assigned to an
additional.fields
object with the key
service
.
status
network.http.response_code
The value is taken from the
status
field in the raw log, converted to an integer, and assigned to the
network.http.response_code
field.
stream
additional.fields[].value.string_value
The value is taken from the
stream
field in the raw log and assigned to an
additional.fields
object with the key
stream
.
sub
additional.fields[].value.string_value
The value is taken from the
sub
field in the raw log and assigned to an
additional.fields
object with the key
sub
.
subType
additional.fields[].value.string_value
The value is taken from the
subType
field in the raw log and assigned to an
additional.fields
object with the key
subType
.
tid
additional.fields[].value.string_value
The value is taken from the
tid
field in the raw log and assigned to an
additional.fields
object with the key
tid
.
timestamp
metadata.event_timestamp
The value is taken from the
timestamp
field in the raw log and parsed as an ISO8601 timestamp.
tname
additional.fields[].value.string_value
The value is taken from the
tname
field in the raw log and assigned to an
additional.fields
object with the key
tname
.
txnId
additional.fields[].value.string_value
The value is taken from the
txnId
field in the raw log and assigned to an
additional.fields
object with the key
txnId
.
type
additional.fields[].value.string_value
The value is taken from the
type
field in the raw log and assigned to an
additional.fields
object with the key
type
.
userAgent
network.http.parsed_user_agent
,
network.http.user_agent
The value is taken from the
userAgent
field in the raw log and assigned to the
network.http.user_agent
and
network.http.parsed_user_agent
fields. The
network.http.parsed_user_agent
field is then converted to a parsed user agent object.
userDN
additional.fields[].value.string_value
The value is taken from the
userDN
field in the raw log and assigned to an
additional.fields
object with the key
userDN
.
userGuid
additional.fields[].value.string_value
The value is taken from the
userGuid
field in the raw log and assigned to an
additional.fields
object with the key
userGuid
.
userIdpGuid
additional.fields[].value.string_value
The value is taken from the
userIdpGuid
field in the raw log and assigned to an
additional.fields
object with the key
userIdpGuid
.
userIP
principal.asset.ip
,
principal.ip
,
target.asset.ip
,
target.ip
,
intermediary.ip
The IP addresses are extracted from the
userIP
field in the raw log using a grok pattern. The first IP address is added to the
principal.ip
and
principal.asset.ip
fields. The second IP address is added to the
target.ip
and
target.asset.ip
fields. The third IP address is added to the
intermediary.ip
field.
userLoginId
target.user.email_addresses
If the
userLoginId
field in the raw log is not empty and matches an email address pattern, it is added to the
target.user.email_addresses
field.
userLoginIdAttributeMappingName
target.user.user_display_name
The value is taken from the
userLoginIdAttributeMappingName
field in the raw log.
userRiskLevel
additional.fields[].value.string_value
The value is taken from the
userRiskLevel
field in the raw log and assigned to an
additional.fields
object with the key
userRiskLevel
.
userRiskScore
additional.fields[].value.string_value
The value is taken from the
userRiskScore
field in the raw log and assigned to an
additional.fields
object with the key
userRiskScore
.
userIp
principal.asset.ip
,
principal.ip
The value is taken from the
userIp
field in the raw log and added to the
principal.ip
and
principal.asset.ip
fields.
userUniversalId
additional.fields[].value.string_value
The value is taken from the
userUniversalId
field in the raw log and assigned to an
additional.fields
object with the key
userUniversalId
.
vhost
additional.fields[].value.string_value
The value is taken from the
vhost
field in the raw log and assigned to an
additional.fields
object with the key
vhost
.
N/A
extensions.auth.type
The value is set to
SSO
if the
metadata.event_type
field is
USER_LOGIN
.
N/A
metadata.log_type
The value is set to
SYMANTEC_VIP_AUTHHUB
.
Need more help?
Get answers from Community members and Google SecOps professionals.
