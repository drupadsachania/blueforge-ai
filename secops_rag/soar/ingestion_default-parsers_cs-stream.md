# Collect CrowdStrike Falcon Stream logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream/  
**Scraped:** 2026-03-05T09:53:41.840126Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CrowdStrike Falcon Stream logs
Supported in:
Google secops
SIEM
This document describes how to collect Crowdstrike Falcon Stream logs using
Bindplane. The parser extracts key-value pairs and maps them to the Unified Data
Model (UDM), handling different delimiters and enriching the data with
additional context like severity and event types. It also performs specific
transformations for certain event types and fields, such as user logins and
security results.
Before you begin
Make sure you have the following prerequisites:
Google Security Operations instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the CrowdStrike Falcon console
Obtain API credentials for Falcon Stream (Client ID and Client Secret)
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
Save the file securely on the system where BindPlane will be installed.
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
'CS_STREAM'
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
to the path where the authentication file was saved in the
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
Configure and get a CrowdStrike API Key
Sign in to
CrowdStrike Falcon
with a privileged account.
Go to
Menu
>
Support
.
Click
API Clients
>
KeysSelect
.
Click
Add new API client
.
In the
API Scopes
section, select
Event streams
and then enable the
Read
option.
Click
Add
.
Copy and save the
Client ID, Client Secret
and
Base URL
.
Install the Falcon SIEM Connector
Download the RPM installer package for your operating system.
Package installation:
CentOS operating system:
sudo
rpm
-Uvh
<installer
package>
Ubuntu operating system:
sudo
dpkg
-i
<installer
package>
Default installation directories:
Falcon SIEM Connector -
/opt/crowdstrike/
.
Service -
/etc/init.d/cs.falconhoseclientd/
.
Configure the SIEM Connector to forward events to Bindplane
Sign into the machine with installed SIEM Connector as a
sudo
user.
Go to the
/opt/crowdstrike/etc/
directory.
Rename
cs.falconhoseclient.leef.cfg
to
cs.falconhoseclient.cfg
.
SIEM Connector uses
cs.falconhoseclient.cfg
configuration by default.
Edit the
cs.falconhoseclient.cfg
file and modify or set the following parameters:
api_url:
- Your Crowdstrike Falcon Base URL copied from previous step.
app_id:
- Any string as identifier for connecting to Falcon Streaming API (For example, set to
app_id: SECOPS-LEEF
).
client_id:
- The
client_id
value copied from previous step.
client_secret:
- The
client_secret
value copied from previous step.
send_to_syslog_server: true
- Enable push to Syslog server.
host:
- The IP or hostname of the BindPlane Agent.
port:
- The port of the BindPlane Agent.
Save the
cs.falconhoseclient.cfg
file.
Start the SIEM Connector service:
CentOS operating system
sudo
service
cs.falconhoseclientd
start
Ubuntu 16.04 or later operating system
sudo
systemctl
start
cs.falconhoseclientd.service
(Optional) Stop the SIEM Connector service:
CentOS operating system
sudo
service
cs.falconhoseclientd
stop
Ubuntu 16.04 or later operating system
sudo
systemctl
stop
cs.falconhoseclientd.service
(Optional): Restart the SIEM Connector service:
CentOS operating system
sudo
service
cs.falconhoseclientd
restart
Ubuntu 16.04 or later operating system
sudo
systemctl
restart
cs.falconhoseclientd.service
UDM mapping table
Log Field
UDM Mapping
Logic
cat
security_result.category_details
The value of the
cat
field is directly mapped to the
security_result.category_details
field.
commandLine
target.process.command_line
The value of the
commandLine
field is directly mapped to the
target.process.command_line
field.
cs1
security_result.summary
If
cs1Label
is "incidentType", the value of
cs1
is mapped to
security_result.summary
. Otherwise, it's mapped as a key-value pair in
security_result.detection_fields
with the key from
cs1Label
and value from
cs1
.
cs1Label
security_result.detection_fields.key
Used as the key in
security_result.detection_fields
when
cs1
is not an incident type.
cs2
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key from
cs2Label
and value from
cs2
.
cs2Label
security_result.detection_fields.key
Used as the key in
security_result.detection_fields
along with
cs2
.
cs3
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key from
cs3Label
and value from
cs3
.
cs3Label
security_result.detection_fields.key
Used as the key in
security_result.detection_fields
along with
cs3
.
cs4
security_result.about.url
If
cs4Label
is "falconHostLink", the value of
cs4
is mapped to
security_result.about.url
. Otherwise, it's mapped as a key-value pair in
security_result.detection_fields
with the key from
cs4Label
and value from
cs4
.
cs4Label
security_result.detection_fields.key
Used as the key in
security_result.detection_fields
when
cs4
is not a falconHostLink.
description
metadata.description
The value of the
description
field is directly mapped to the
metadata.description
field. If it's empty,
incidentDescription
or
msg
or
serviceName
are used instead.
devTime
metadata.event_timestamp
The value of the
devTime
field is parsed and mapped to the
metadata.event_timestamp
field.
deviceCustomDate1
metadata.event_timestamp
If
devTime
is not present, the value of the
deviceCustomDate1
field is parsed and mapped to the
metadata.event_timestamp
field.
domain
principal.administrative_domain
Extracted from the
userName
field using a regular expression and mapped to
principal.administrative_domain
.
duser
principal.user.userid
If present, the value of
duser
overwrites the
usrName
field and is then used for populating the user fields.
endpointName
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key "endpointName".
eventType
metadata.product_event_type
The value of the
eventType
field is directly mapped to the
metadata.product_event_type
field.
falconHostLink
security_result.about.url
The value of the
falconHostLink
field is directly mapped to the
security_result.about.url
field.
filePath
target.process.file.full_path
The value of the
filePath
field is directly mapped to the
target.process.file.full_path
field.
identityProtectionIncidentId
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key "identityProtectionIncidentId".
incidentDescription
metadata.description
If
description
is empty, the value of the
incidentDescription
field is mapped to the
metadata.description
field.
incidentType
security_result.summary
The value of the
incidentType
field is directly mapped to the
security_result.summary
field.
log_type
metadata.log_type
The value of the
log_type
field is directly mapped to the
metadata.log_type
field.
msg
metadata.description
If
description
and
incidentDescription
are empty, the value of the
msg
field is mapped to the
metadata.description
field.
numbersOfAlerts
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key "numbersOfAlerts".
numberOfCompromisedEntities
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key "numberOfCompromisedEntities".
product
metadata.product_name
The value of the
product
field is directly mapped to the
metadata.product_name
field.
resource
target.resource.name
The value of the
resource
field is directly mapped to the
target.resource.name
field.
serviceName
target.application
The value of the
serviceName
field is directly mapped to the
target.application
field. Also used as a fallback for
metadata.description
.
severityName
security_result.severity
The value of the
severityName
field is mapped to the
security_result.severity
field after being uppercased. The mapping logic includes specific conversions for different severity names.
sha256
target.file.sha256
The value of the
sha256
field is directly mapped to the
target.file.sha256
field.
src
principal.ip
The value of the
src
field is directly mapped to the
principal.ip
field.
srcMAC
principal.mac
The value of the
srcMAC
field is directly mapped to the
principal.mac
field after replacing hyphens with colons.
state
security_result.detection_fields.value
Mapped as a key-value pair in
security_result.detection_fields
with the key "state".
success
security_result.action
If
success
is "true",
security_result.action
is set to "ALLOW". If
success
is "false",
security_result.action
is set to "BLOCK".
userName
principal.user.userid
If
usrName
is not present, the value of the
userName
field is used for populating the user fields.  The domain is extracted if present.
usrName
principal.user.userid
/
target.user.userid
If present, the value of the
usrName
field is mapped to either
principal.user.userid
or
target.user.userid
depending on the
eventType
. If it's an email address, it's also added to the respective
email_addresses
field.
vendor
metadata.vendor_name
The value of the
vendor
field is directly mapped to the
metadata.vendor_name
field.
version
metadata.product_version
The value of the
version
field is directly mapped to the
metadata.product_version
field.
(Parser Logic)
extensions.auth.mechanism
Set to "USERNAME_PASSWORD" if
eventType
is "saml2Assert" or "twoFactorAuthenticate".
(Parser Logic)
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if
eventType
is "assert" or "userAuthenticate".
(Parser Logic)
metadata.event_timestamp
The timestamp from the raw log's
collection_time
or
timestamp
field is used as the event timestamp.
(Parser Logic)
metadata.event_type
Determined based on the
eventType
and other fields. Defaults to "GENERIC_EVENT" and can be changed to "USER_LOGIN", "GROUP_MODIFICATION", "GROUP_DELETION", "SERVICE_STOP", "SERVICE_START", or "USER_UNCATEGORIZED".
(Parser Logic)
target.resource.type
Set to "GROUP" if
eventType
is "remove_group", "update_group", or "delete_group".
Need more help?
Get answers from Community members and Google SecOps professionals.
