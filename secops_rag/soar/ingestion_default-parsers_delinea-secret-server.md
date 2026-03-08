# Collect Delinea Secret Server logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-secret-server/  
**Scraped:** 2026-03-05T09:54:19.709095Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Delinea Secret Server logs
Supported in:
Google secops
SIEM
This document explains how to collect Delinea (previously Thycotic) Secret
Server logs. The parser transforms raw logs into a structured format conforming
to the Google Security Operations Unified Data Model (UDM). It first extracts key
fields like timestamps, event types, and user information, then uses conditional
logic based on the specific event type to map the data into the appropriate UDM
fields, ultimately enriching the data for analysis in Google SecOps.
Before you begin
Make sure you have the following prerequisites:
Google Security Operations instance
Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to Delinea Secrets Server
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
Save the file securely on the system where Bindplane will be installed.
Get Google SecOps customer ID
Sign in to the Google Security Operations console.
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
'THYCOTIC'
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
Update '/path/to/ingestion-authentication-file.json' to the path where the authentication file was saved in the
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
Configure Thycotic Secret Server to send logs using Syslog
Sign in to Thycotic Secret Server with administrator credentials.
Go to
Admin
>
Configuration
.
Click
Edit
.
Select the
Enable Syslog/CEF logging
checkbox and specify the following details:
Syslog/CEF server
: Enter the IP address of your Syslog server/Bindplane.
Syslog/CEF protocol
Select
UDP
or
TCP
(depending on your Syslog server or Bindplane configuration).
Syslog/CEF port
: Enter the port number that the Syslog server or Bindplane is configured to listen on.
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
Account_Domain
event1.idm.read_only_udm.principal.domain
The value is taken from the
Account_Domain
field in the
msg
field of the raw log.
By User
event1.idm.read_only_udm.principal.user.userid
The value is taken from the
By User
field in the
msg
field of the raw log.
Container Id
event1.idm.read_only_udm.principal.asset.asset_id
The value is taken from the
Container Id
field in the
msg
field of the raw log and is prefixed with
container_id:
.
Container name
event1.idm.read_only_udm.principal.resource.name
The value is taken from the
Container name
field in the
msg
field of the raw log.
cs2
event1.idm.read_only_udm.additional.fields[].value.string_value
The value is taken from the
cs2
field in the
msg
field of the raw log.
cs3
event1.idm.read_only_udm.target.file.full_path
The value is taken from the
cs3
field in the
msg
field of the raw log.
cs4
event1.idm.read_only_udm.principal.user.user_display_name
The value is taken from the
cs4
field in the
msg
field of the raw log.
Details
event1.idm.read_only_udm.additional.fields[].value.string_value
The value is taken from the
Details
field in the
msg
field of the raw log.
fname
event1.idm.read_only_udm.target.file.full_path
The value is taken from the
fname
field in the
msg
field of the raw log.
Host
event1.idm.read_only_udm.principal.hostname, event1.idm.read_only_udm.principal.asset.hostname
The value is taken from the
Host
field in the
msg
field of the raw log.
Item Name
event1.idm.read_only_udm.target.user.userid
The value is taken from the
Item Name
field in the
msg
field of the raw log.
event1.idm.read_only_udm.additional.fields[].key
The value is hardcoded to
fname
.
event1.idm.read_only_udm.additional.fields[].key
The value is hardcoded to
Group or User
.
event1.idm.read_only_udm.additional.fields[].key
The value is hardcoded to
Details
.
event1.idm.read_only_udm.additional.fields[].key
The value is hardcoded to
type_id
.
event1.idm.read_only_udm.extensions.auth.type
The value is hardcoded to
MACHINE
.
event1.idm.read_only_udm.metadata.description
The value is taken from the
thycotic_event
field, which is extracted from the raw log using a grok pattern.
event1.idm.read_only_udm.metadata.event_timestamp.seconds
The value is derived from the
rt
field if present, otherwise from the
ts
field. Both fields are extracted from the raw log using grok patterns.
event1.idm.read_only_udm.metadata.event_type
The value is determined based on the
thycotic_event
field and other conditions. For example, if
thycotic_event
is
USER - LOGIN
, the event type is set to
USER_LOGIN
.
event1.idm.read_only_udm.metadata.log_type
The value is hardcoded to
THYCOTIC
.
event1.idm.read_only_udm.metadata.product_event_type
The value is taken from the
thycotic_event
field, which is extracted from the raw log using a grok pattern.
event1.idm.read_only_udm.metadata.product_log_id
The value is taken from the
action_id
field, which is extracted from the raw log using a grok pattern.
event1.idm.read_only_udm.metadata.product_name
The value is taken from the
device_product
field, which is extracted from the raw log using a grok pattern. If the field is empty, the value is hardcoded to
Secret Server
.
event1.idm.read_only_udm.metadata.product_version
The value is taken from the
device_version
field, which is extracted from the raw log using a grok pattern.
event1.idm.read_only_udm.metadata.vendor_name
The value is hardcoded to
Thycotic
.
event1.idm.read_only_udm.network.ip_protocol
The value is set to
TCP
if the
input.type
field is
tcp
.
event1.idm.read_only_udm.observer.application
The value is taken from the
agent.type
field if present, otherwise it is hardcoded to
Secret Server
.
event1.idm.read_only_udm.observer.asset_id
The value is set to
Agent ID:
concatenated with the
agent.id
field.
event1.idm.read_only_udm.observer.hostname
The value is taken from the
agent.hostname
field if present, otherwise from the
server
field.
event1.idm.read_only_udm.observer.platform_version
The value is taken from the
agent.version
field.
event1.idm.read_only_udm.observer.user.userid
The value is taken from the
agent.name
field.
event1.idm.read_only_udm.principal.asset.asset_id
The value is set to
ID:
concatenated with the
host.id
field.
event1.idm.read_only_udm.principal.asset.hardware.cpu_platform
The value is taken from the
host.architecture
field.
event1.idm.read_only_udm.principal.asset.hostname
The value is taken from the
server
field if present, otherwise from the
host.hostname
field.
event1.idm.read_only_udm.principal.asset.ip
The value is taken from the
src
field if present, otherwise from the
src_ip
field.
event1.idm.read_only_udm.principal.hostname
The value is taken from the
host.hostname
field if present, otherwise from the
server
field.
event1.idm.read_only_udm.principal.ip
The value is taken from the
src
field if present, otherwise from the
src_ip
field or from the
host.ip
field.
event1.idm.read_only_udm.principal.mac
The value is taken from the
host.mac
field.
event1.idm.read_only_udm.principal.platform
The value is set to
LINUX
if the
host_os_platform
field is
centos
, otherwise it is set to the uppercase value of the
host_os_platform
field.
event1.idm.read_only_udm.principal.platform_patch_level
The value is taken from the
host.os.kernel
field.
event1.idm.read_only_udm.principal.platform_version
The value is taken from the
host.os.version
field.
event1.idm.read_only_udm.principal.port
The value is taken from the
src_port
field, which is extracted from the
log.source.address
field using a grok pattern.
event1.idm.read_only_udm.principal.user.user_display_name
The value is taken from the
cs4
field in the
msg
field of the raw log.
event1.idm.read_only_udm.principal.user.userid
The value is taken from the
suser
field in the
msg
field of the raw log, or from the
By User
field if
thycotic_event
is
USER - LOGIN
,
USER - LOGOUT
,
USER - LOGINFAILURE
, or
USER - EDIT
.
event1.idm.read_only_udm.security_result.action
The value is taken from the
Action
field in the
msg
field of the raw log. It can also be set to
ALLOW
or
BLOCK
based on the value of
thycotic_event
.
event1.idm.read_only_udm.security_result.description
The value is taken from the
temp_message
field, which contains the remaining part of the
msg
field after extracting other fields.
event1.idm.read_only_udm.security_result.severity
The value is determined based on the
syslog_severity
field. For example, if
syslog_severity
contains
error
or
warning
, the severity is set to
HIGH
. If
thycotic_event
is
System Log
, the severity is set to
INFORMATIONAL
.
event1.idm.read_only_udm.security_result.severity_details
The value is taken from the
syslog_severity
field.
event1.idm.read_only_udm.target.file.full_path
The value is constructed by concatenating the
cs3
and
fname
fields with a
/
separator if both fields are present. If only one field is present, the value is taken from that field.
event1.idm.read_only_udm.target.resource.product_object_id
The value is taken from the
type_id
field.
event1.idm.read_only_udm.target.user.userid
The value is taken from the
item_name
field in the
msg
field of the raw log, or from the
Item Name
field if
thycotic_event
is
USER - LOGIN
,
USER - LOGOUT
,
USER - LOGINFAILURE
, or
USER - EDIT
.
events.timestamp.seconds
The value is derived from the
rt
field if present, otherwise from the
ts
field. Both fields are extracted from the raw log using grok patterns.
rt
event1.idm.read_only_udm.metadata.event_timestamp.seconds
The value is taken from the
rt
field in the
msg
field of the raw log and is used to set the event timestamp.
src
event1.idm.read_only_udm.principal.asset.ip, event1.idm.read_only_udm.principal.ip
The value is taken from the
src
field in the
msg
field of the raw log.
src_ip
event1.idm.read_only_udm.principal.asset.ip, event1.idm.read_only_udm.principal.ip
The value is taken from the
src_ip
field, which is extracted from the
log.source.address
field using a grok pattern.
Need more help?
Get answers from Community members and Google SecOps professionals.
