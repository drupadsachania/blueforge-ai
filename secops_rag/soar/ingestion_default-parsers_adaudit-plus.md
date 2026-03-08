# Collect ManageEngine ADAudit Plus logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adaudit-plus/  
**Scraped:** 2026-03-05T09:57:44.148838Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ManageEngine ADAudit Plus logs
Supported in:
Google secops
SIEM
This document explains how to ingest ManageEngine ADAudit Plus logs to Google Security Operations using a Bindplane agent. The parser handles logs from ADAudit Plus, converting them into UDM format. It uses grok patterns to extract fields from both SYSLOG (CEF) and key-value formatted messages, mapping them to UDM fields based on event types derived from alert and report profiles, and enriching the data with additional context. The parser also handles specific scenarios like login failures, user changes, and file modifications, adjusting the UDM mapping accordingly.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to ManageEngine ADAudit.
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
For additional installation options, consult this
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
ADAUDIT_PLUS
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
to the path where the authentication file was saved in the
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
Configuring ManageEngine ADAudit Plus Syslog
Sign in to the
ManageEngine ADAudit Plus
web UI.
Go to
Admin
>
Configuration
>
SIEM Integration
.
Select
Enable
to send the ADAudit Plus logs.
Select the
ArcSight (CEF)
format.
Provide the following configuration details:
IP Address
: Bindplane agent IP Address.
Port
: Bindplane port number; for example,
514
for UDP.
Target Type
: Select
UDP
(you can also select
TCP
, depending on your Bindplane agent configuration).
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ACCOUNT_DOMAIN
principal.administrative_domain
The value of
ACCOUNT_DOMAIN
from the raw log is assigned to this UDM field.
ACCOUNT_NAME
principal.user.userid
The value of
ACCOUNT_NAME
from the raw log is assigned to this UDM field.
ALERT_PROFILE
security_result.summary
The value of
ALERT_PROFILE
from the raw log is assigned to this UDM field.
APPLICATION_NAME
target.resource.name
The value of
APPLICATION_NAME
from the raw log is assigned to this UDM field. Also sets
target.resource.resource_type
to
TASK
and
has_target_resource
to true.
CALLER_DISPLAY_NAME
target.user.user_display_name
The value of
CALLER_DISPLAY_NAME
from the raw log is assigned to this UDM field.
CALLER_USER_NAME
target.user.userid
The value of
CALLER_USER_NAME
from the raw log is assigned to this UDM field.
CALLER_USER_SID
target.group.windows_sid
The value of
CALLER_USER_SID
from the raw log is assigned to this UDM field after removing characters
[%,{,}]
. This is only done if the value matches a Windows SID pattern.
Category
metadata.product_event_type
The value of
Category
from the raw log is assigned to this UDM field.
CLIENT_HOST_NAME
target.hostname
,
target.asset.hostname
The value of
CLIENT_HOST_NAME
from the raw log is assigned to these UDM fields.
CLIENT_IP_ADDRESS
target.ip
,
target.asset.ip
The value of
CLIENT_IP_ADDRESS
from the raw log is assigned to these UDM fields after validating it is a valid IP address.
CLIENT_PORT
target.port
The value of
CLIENT_PORT
from the raw log is assigned to this UDM field after converting it to an integer.
DOMAIN
target.administrative_domain
The value of
DOMAIN
from the raw log is assigned to this UDM field. This value might be overwritten later by
ACCOUNT_DOMAIN
if present.
FILE_LOCATION
target.file.full_path
The value of
FILE_LOCATION
from the raw log is assigned to this UDM field.
FILE_NAME
target.file.full_path
The value of
FILE_NAME
from the raw log is assigned to this UDM field if
FILE_LOCATION
is not present.
FORMAT_MESSAGE
security_result.description
The value of
FORMAT_MESSAGE
from the raw log is assigned to this UDM field. Parts of this field may be used to populate other UDM fields and then removed from the description.
IP
principal.ip
,
principal.asset.ip
The value of
IP
from the raw log is assigned to these UDM fields after validating it is a valid IP address.
loggerHost
intermediary.hostname
,
intermediary.asset.hostname
The value of
loggerHost
extracted from the raw log's message field is assigned to these UDM fields.
login_name
target.user.userid
or
target.user.email_addresses
or
target.user.user_display_name
If the value contains
@
, it's treated as an email address. If it contains spaces, it's treated as a display name. Otherwise, it's treated as a userid. Also sets
event_type
to
USER_LOGIN
,
extensions.auth.type
to
MACHINE
, and
extensions.auth.mechanism
to
USERNAME_PASSWORD
.
RECORD_NUMBER
principal.process.pid
The value of
RECORD_NUMBER
from the raw log is assigned to this UDM field.
REPORT_PROFILE
metadata.description
The value of
REPORT_PROFILE
from the raw log is assigned to this UDM field.
SEVERITY
security_result.severity
The value of
SEVERITY
determines the value of this UDM field: 1 maps to LOW, 2 maps to MEDIUM, and 3 maps to HIGH.
SOURCE
principal.hostname
,
principal.asset.hostname
The value of
SOURCE
from the raw log, combined with the
DOMAIN
if
SOURCE
doesn't contain a domain part, is assigned to these UDM fields. Also sets
has_principal_host
to true.
TIME_GENERATED
metadata.event_timestamp.seconds
The value of
TIME_GENERATED
from the raw log is used as the event timestamp.
UNIQUE_ID
metadata.product_log_id
The value of
UNIQUE_ID
from the raw log is assigned to this UDM field.
USERNAME
principal.user.userid
The value of
USERNAME
from the raw log is assigned to this UDM field if
ACCOUNT_NAME
is not present.
USER_OU_GUID
metadata.product_log_id
The value of
USER_OU_GUID
from the raw log, after removing curly braces, is assigned to this UDM field if
UNIQUE_ID
is not present.
access_mode
security_result.detection_fields.value
The value of
access_mode
from the raw log is assigned to this UDM field, with the key set to
ACCESS_MODE
.
action_name
security_result.description
The value of
action_name
from the raw log is assigned to this UDM field.
domain_name
principal.administrative_domain
The value of
domain_name
from the raw log is assigned to this UDM field.
event.idm.read_only_udm.extensions.auth.mechanism
event.idm.read_only_udm.extensions.auth.mechanism
Set to
USERNAME_PASSWORD
if
login_name
is present or if
event_type
is
USER_LOGIN
.
event.idm.read_only_udm.extensions.auth.type
event.idm.read_only_udm.extensions.auth.type
Set to
MACHINE
if
login_name
is present or if
event_type
is
USER_LOGIN
.
event.idm.read_only_udm.metadata.event_type
event.idm.read_only_udm.metadata.event_type
Determined by the parser based on the values of
ALERT_PROFILE
,
REPORT_PROFILE
, and
FORMAT_MESSAGE
. Can be one of several values, including
USER_CHANGE_PERMISSIONS
,
USER_STATS
,
USER_LOGIN
,
USER_CHANGE_PASSWORD
,
SETTING_MODIFICATION
,
FILE_DELETION
,
FILE_MODIFICATION
,
STATUS_SHUTDOWN
,
SCHEDULED_TASK_CREATION
,
FILE_READ
,
NETWORK_CONNECTION
,
GENERIC_EVENT
,
USER_UNCATEGORIZED
, or
STATUS_UPDATE
.
event.idm.read_only_udm.metadata.log_type
event.idm.read_only_udm.metadata.log_type
Always set to
ADAUDIT_PLUS
.
event.idm.read_only_udm.metadata.product_name
event.idm.read_only_udm.metadata.product_name
Always set to
ADAudit Plus
.
event.idm.read_only_udm.metadata.vendor_name
event.idm.read_only_udm.metadata.vendor_name
Always set to
Zoho Corporation
.
host
principal.hostname
,
principal.asset.hostname
The value of
host
from the raw log is assigned to these UDM fields. Also sets
has_principal_host
to true.
intermediary.hostname
,
intermediary.asset.hostname
intermediary.hostname
,
intermediary.asset.hostname
Set to the value of
loggerHost
.
principalHost
principal.hostname
,
principal.asset.hostname
The value of
principalHost
from the raw log is assigned to these UDM fields after checking if it's an IP. Also sets
has_principal_host
to true.
security_result.action
security_result.action
Set to
ALLOW
if
outcome
or
msg_data_2
contains
Success
, or if
FORMAT_MESSAGE
contains
Status:Success
. Set to
BLOCK
if
status
contains
denied
,
locked out
,
incorrect
,
does not meet
, or
Unable to validate
. Set to
BLOCK
if
ALERT_PROFILE
is
Logon Failures for Admin Users
.
security_result.category
security_result.category
Set to
POLICY_VIOLATION
if
event_type
is
USER_STATS
or if
ALERT_PROFILE
is
Logon Failures for Admin Users
.
security_result.rule_name
security_result.rule_name
Extracted from the
FORMAT_MESSAGE
field if it contains
Reason:
.
status
security_result.summary
The value of
status
from the raw log is assigned to this UDM field.
targetHost
target.hostname
,
target.asset.hostname
or
target.ip
,
target.asset.ip
The value of
targetHost
from the raw log is assigned to these UDM fields after checking if it's an IP.
targetUser
target.user.userid
The value of
targetUser
from the raw log is assigned to this UDM field.
_CNtargetUser
target.user.user_display_name
The value of
_CNtargetUser
from the raw log is assigned to this UDM field.
_user
principal.user.userid
or
target.user.userid
The value of
_user
from the raw log is assigned to
principal.user.userid
unless
event_type
is
USER_CHANGE_PASSWORD
, in which case it's assigned to
target.user.userid
.
Need more help?
Get answers from Community members and Google SecOps professionals.
