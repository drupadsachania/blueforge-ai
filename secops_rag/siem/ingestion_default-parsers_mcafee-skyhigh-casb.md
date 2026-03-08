# Collect Skyhigh Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-skyhigh-casb/  
**Scraped:** 2026-03-05T09:28:15.667316Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Skyhigh Security logs
Supported in:
Google secops
SIEM
This document explains how to ingest Skyhigh Security
(formerly McAfee Skyhigh CASB) logs to Google Security Operations using Bindplane.
The parser transforms logs from a SYSLOG + KV format into a Unified Data Model
(UDM). It first normalizes the log message into key-value pairs and then maps
the extracted fields to corresponding UDM attributes within the
event.idm.read_only_udm
object, categorizing the event type based on the
presence and values of specific fields.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Installed and configured Skyhigh Cloud Connector
Privileged access to Skyhigh Security Cloud Connector
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
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
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
creds_file_path
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
log_type
:
'MCAFEE_SKYHIGH_CASB'
raw_log_field
:
body
ingestion_labels
:
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
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Prerequisites before downloading the Logging Client
Make sure you have the following details:
Usage Analytics User privilege
: Your account must have the Usage Analytics Users role.
Customer ID
: Perform the following steps to find your
Customer ID
in
Skyhigh CASB
:
Sign in to
Skyhigh CASB
.
Go to
Settings
>
Infrastructure
>
Client Proxy Management
.
Click
Global Configuration
>
Tenant Authentication
.
Under
Global Settings
, find your
Customer ID
displayed.
Email address and password
: Your (or dedicated service account) log-on
credentials (If you sign in using SAML without submitting a password, you can't
install the Logging Client).
Download and install Skyhigh Logging Client
Download the
Logging Client
to a dedicated instance.
Install the Logging Client (unzip the downloaded EXE file if required).
After installation is completed, open the
Logging Client
.
On the
Configuration
page, provide the following configurations details:
Customer ID
: Enter you Skyhigh CASB customer ID obtained in the previous step.
Service
: Select
SSE
if you are using Skyhigh SSE, or
WGCS
if
you are using this product together with Trellix ePO.
Region
: Choose a regional or country code depending on where your data is stored:
EU — European Union
IN — India
SG — Singapore
UE — United Arab Emirates
UK — United Kingdom
US — United States
Name
: Enter the username, which is most commonly the email address used to sign in to Secure Web Gateway, or a dedicated instance.
Password
: Enter the password you use to log on to Secure Web Gateway. If you log on with SAML, you can't use the Logging Client.
API version
: Enter
version 13
.
Log Type
: You can download different types of logs, including logs with data originating from the Web, Remote Browser Isolation (RBI), Private Access, and Cloud Firewall.
Select
Send as Syslogs
and provide the following configuration details:
Syslog-Client Host: Enter the Bindplane agent IP address.
Syslog-Client Port: Enter the Bindplane agent port number.
Transport: Select
UDP
or
TCP
, depending on your Bindplane agent configuration.
UDM mapping table
Log field
UDM mapping
Logic
EventReceivedTime
metadata.event_timestamp
Converted to timestamp from
yyyy-MM-dd HH:mm:ss
format
FileSize
target.file.size
Directly mapped, converted to uinteger
Hostname
principal.hostname
Directly mapped
MessageSourceAddress
principal.ip
Directly mapped, merged if multiple instances
Severity
additional.fields.value.string_value (key: SEVERITY)
Directly mapped
SeverityValue
additional.fields.value.string_value (key: SEVERITY_VALUE)
Directly mapped
SourceModuleName
additional.fields.value.string_value (key: SOURCE_MODULE_NAME)
Directly mapped
SourceModuleType
principal.resource.resource_subtype
Directly mapped
SyslogFacility
security_result.about.resource.attribute.labels.value (key: SYSLOG_FACILITY)
Directly mapped
SyslogFacilityValue
security_result.about.resource.attribute.labels.value (key: SYSLOG_FACILITY_VALUE)
Directly mapped
SyslogSeverity
security_result.about.resource.attribute.labels.value (key: SYSLOG_SEVERITY)
Directly mapped
SyslogSeverityValue
security_result.about.resource.attribute.labels.value (key: SYSLOG_SEVERITY_VALUE)
Directly mapped
activityName
metadata.product_event_type
Directly mapped, brackets removed
actorId
principal.user.userid
Directly mapped, also added to email_addresses if it's an email
actorIdType
principal.user.attribute.roles.name
Directly mapped
collaborationSharedLink
security_result.about.resource.attribute.labels.value (key: COLLABORATION_SHARED_LINK)
Directly mapped
contentItemId
target.file.full_path (if contentItemType is FILE)
Directly mapped, quotes removed
contentItemId
target.url (if contentItemType is SAAS_RESOURCE)
Directly mapped, quotes removed
contentItemHierarchy
additional.fields.value.string_value (key: CONTENT_ITEM_HIERARCHY)
Directly mapped, quotes removed
contentItemName
target.resource.name
Directly mapped, quotes removed
contentItemType
additional.fields.value.string_value (key: CONTENT_ITEM_TYPE)
Directly mapped
incidentGroup
security_result.detection_fields.value (key: INCIDENT_GROUP)
Directly mapped
incidentId
metadata.product_log_id
Directly mapped
incidentRiskScore
security_result.detection_fields.value (key: INCIDENT_RISK_SCORE)
Directly mapped
incidentRiskSeverityId
Used in combination with riskSeverity to determine security_result.severity
informationAccountId
target.resource.product_object_id
Directly mapped
informationAnomalyCategory
security_result.category_details
Directly mapped, quotes removed
informationAnomalyCause
security_result.detection_fields.value (key: INFO_ANOMALY_CAUSE)
Directly mapped, quotes removed
informationCategory
security_result.category_details
Directly mapped
informationConfigType
additional.fields.value.string_value (key: INFORMATION_CONFIG_TYPE)
Directly mapped, quotes removed
informationContentItemParent
target.resource.parent
Directly mapped, quotes removed
informationEventId
additional.fields.value.string_value (key: INFORMATION_EVENT_ID)
Directly mapped
informationExternalCollaboratorsCount
additional.fields.value.string_value (key: INFORMATION_COLLAB_COUNT)
Directly mapped
informationFileTypes
additional.fields.value.list_value.values.string_value (key: FILE_TYPE)
Extracted from JSON-like string, brackets and quotes removed
informationLastExecutedResponseLabel
additional.fields.value.string_value (key: INFORMATION_LAST_RESPONSE)
Directly mapped
informationScanName
metadata.description
Directly mapped, quotes removed
informationScanRunDate
Not mapped to UDM
informationSource
additional.fields.value.string_value (key: INFORMATION_SOURCE)
Directly mapped
informationUniqueMatchCount
additional.fields.value.string_value (key: INFORMATION_UNQ_MATCH_COUNT)
Directly mapped
informationUserAttributesSAMAccountName
principal.user.user_display_name
Directly mapped, brackets removed
instanceId
principal.resource.product_object_id
Directly mapped
instanceName
principal.resource.name
Directly mapped, quotes removed
policyId
security_result.rule_id
Directly mapped
policyName
security_result.summary
Directly mapped, quotes removed
response
Used to determine security_result.action (ALLOW or BLOCK)
riskSeverity
Used in combination with incidentRiskSeverityId to determine security_result.severity, converted to uppercase
serviceNames
target.application
Directly mapped, brackets, quotes and extra spaces removed
sourceIps
principal.ip
Extracted from JSON-like string, merged if multiple instances
status
additional.fields.value.string_value (key: STATUS)
Directly mapped
threatCategory
security_result.threat_name
Directly mapped, quotes removed
totalMatchCount
security_result.detection_fields.value (key: TOTAL_MATCH_COUNT)
Directly mapped
N/A
metadata.vendor_name
MCAFEE
- Static value
N/A
metadata.product_name
MCAFEE_SKYHIGH_CASB
- Static value
N/A
metadata.log_type
MCAFEE_SKYHIGH_CASB
- Static value
N/A
principal.resource.type
VIRTUAL_MACHINE
-  Set if instanceName or instanceId are present
N/A
metadata.event_type
Determined based on a set of conditions:
-
USER_RESOURCE_UPDATE_CONTENT
if actorId, contentItemId or contentItemName are present
-
USER_UNCATEGORIZED
if actorId and target are present
-
STATUS_UPDATE
if Hostname or MessageSourceAddress are present
-
GENERIC_EVENT
otherwise
N/A
security_result.severity
Determined based on the combination of riskSeverity and incidentRiskSeverityId:
-
LOW
if riskSeverity is
LOW
and incidentRiskSeverityId is
0
-
MEDIUM
if riskSeverity is
MEDIUM
and incidentRiskSeverityId is
1
-
HIGH
if riskSeverity is
HIGH
and incidentRiskSeverityId is
2
-
INFORMATIONAL
if riskSeverity is
INFO
and incidentRiskSeverityId is
3
N/A
security_result.action
Determined based on the value of response:
-
ALLOW
if response contains
allow
(case-insensitive)
-
BLOCK
if response contains
Violation
(case-insensitive)
Need more help?
Get answers from Community members and Google SecOps professionals.
