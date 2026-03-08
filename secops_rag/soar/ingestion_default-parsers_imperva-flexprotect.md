# Collect Imperva FlexProtect logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-flexprotect/  
**Scraped:** 2026-03-05T09:57:17.553387Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Imperva FlexProtect logs
Supported in:
Google secops
SIEM
This document explains how to ingest Imperva FlexProtect logs to Google Security Operations using Bindplane. The parser first cleans up and pre-processes incoming logs, then attempts to extract Common Event Format (CEF) data. Depending on the presence of specific fields like "src" and "sip", it assigns a UDM event type and maps relevant CEF fields to the UDM schema, finally enriching the output with additional custom fields. Imperva FlexProtect provides flexible deployment of Imperva security solutions (SecureSphere, Cloud WAF, Bot Protection) across hybrid cloud environments.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Imperva FlexProtect management console or individual product consoles
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'IMPERVA_FLEXPROTECT'
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
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding on Imperva FlexProtect
For SecureSphere Component (On-premises/Cloud)
Sign in to the
Imperva SecureSphere Management Console
.
Go to
Configuration
>
Action Sets
.
Click
Add
to create a new Action Set.
Click
Add Action
and provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Syslog
).
Action Type
: Select
Syslog
.
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (default
514
).
Protocol
: Select
UDP
or
TCP
.
Syslog Log Level
: Select
DEBUG
.
Syslog Facility
: Select
LOCAL0
.
Format
: Select
CEF
(Common Event Format).
Save the action configuration and apply it to relevant security policies.
For Cloud WAF/Incapsula Component
Sign in to the
Imperva Cloud Console
.
Go to
Logs
>
Log Setup
.
Configure syslog destination:
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (default
514
).
Protocol
: Select
UDP
or
TCP
.
Format
: Select
CEF
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
read_only_udm.security_result.action_details
Directly mapped from the
act
field.
app
read_only_udm.network.application_protocol
Directly mapped from the
app
field.
ccode
read_only_udm.principal.location.country_or_region
Directly mapped from the
ccode
field.
cicode
read_only_udm.principal.location.city
Directly mapped from the
cicode
field.
cn1
read_only_udm.network.http.response_code
Directly mapped from the
cn1
field after converting to integer.
cs1
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs1
field.
cs2
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs2
field.
cs3
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs3
field.
cs4
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs4
field.
cs5
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs5
field.
cs6
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs6
field.
cs7
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs7
field.
cs8
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs8
field.
cs9
read_only_udm.additional.fields.value.string_value
Directly mapped from the
cs9
field.
cpt
read_only_udm.principal.port
Directly mapped from the
cpt
field after converting to integer.
Customer
read_only_udm.principal.user.user_display_name
Directly mapped from the
Customer
field.
deviceExternalId
read_only_udm.about.asset.asset_id
The value is derived by concatenating "Incapsula.SIEMintegration:" with the
deviceExternalId
field.
deviceFacility
read_only_udm.principal.location.city
Directly mapped from the
deviceFacility
field.
dproc
read_only_udm.target.process.command_line
Directly mapped from the
dproc
field.
end
read_only_udm.security_result.detection_fields.value
Directly mapped from the
end
field.
fileId
read_only_udm.network.session_id
Directly mapped from the
fileId
field.
filePermission
read_only_udm.about.resource.attribute.permissions.name
Directly mapped from the
filePermission
field.
in
read_only_udm.network.received_bytes
Directly mapped from the
in
field.
qstr
read_only_udm.security_result.detection_fields.value
Directly mapped from the
qstr
field.
request
read_only_udm.target.url
Directly mapped from the
request
field.
requestClientApplication
read_only_udm.network.http.user_agent
Directly mapped from the
requestClientApplication
field.
requestMethod
read_only_udm.network.http.method
Directly mapped from the
requestMethod
field.
siteid
read_only_udm.security_result.detection_fields.value
Directly mapped from the
siteid
field.
sip
read_only_udm.target.ip
Directly mapped from the
sip
field.
sourceServiceName
read_only_udm.principal.application
Directly mapped from the
sourceServiceName
field.
spt
read_only_udm.target.port
Directly mapped from the
spt
field after converting to integer.
src
read_only_udm.principal.ip
Directly mapped from the
src
field.
start
read_only_udm.security_result.detection_fields.value
Directly mapped from the
start
field.
suid
read_only_udm.principal.user.userid
Directly mapped from the
suid
field.
ver
read_only_udm.network.tls.version
Directly mapped from the
ver
field.
read_only_udm.about.asset.asset_id
The value is derived by concatenating "Incapsula.SIEMintegration:" with the
deviceExternalId
field.
read_only_udm.additional.fields.key
Value is determined by the parser logic based on the field's label, for example:
-
cs1Label
maps to "Cap Support"
-
cs2Label
maps to "Javascript Support"
-
cs3Label
maps to "CO Support"
-
cs4Label
maps to "VID"
-
cs5Label
maps to "clappsig"
-
cs6Label
maps to "clapp"
-
cs7Label
maps to "latitude"
-
cs8Label
maps to "longitude"
-
cs9Label
maps to "Rule name"
read_only_udm.metadata.event_timestamp.nanos
Directly mapped from the
collection_time.nanos
field.
read_only_udm.metadata.event_timestamp.seconds
Directly mapped from the
collection_time.seconds
field.
read_only_udm.metadata.event_type
The value is determined based on the presence of
src
and
sip
fields:
- If both are present, the value is set to "NETWORK_HTTP".
- If only
src
is present, the value is set to "USER_UNCATEGORIZED".
- Otherwise, the value is set to "GENERIC_EVENT".
read_only_udm.metadata.product_event_type
The value is derived by concatenating "[", the numerical value from the CEF header field at index 4, "] - ", and the text description from the CEF header field at index 4.
read_only_udm.metadata.product_name
Value is statically set to "SIEMintegration".
read_only_udm.metadata.product_version
Value is statically set to "1".
read_only_udm.metadata.vendor_name
Value is statically set to "Incapsula".
read_only_udm.security_result.detection_fields.key
Value is statically set to either "siteid", "event_start_time", "event_end_time", or "qstr" based on the corresponding field being processed.
read_only_udm.security_result.severity
Value is statically set to "LOW".
read_only_udm.target.port
Directly mapped from the
spt
field after converting to integer.
Need more help?
Get answers from Community members and Google SecOps professionals.
