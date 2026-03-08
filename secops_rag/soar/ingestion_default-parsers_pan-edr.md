# Collect Palo Alto Networks Traps logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-edr/  
**Scraped:** 2026-03-05T09:59:06.526158Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Networks Traps logs
Supported in:
Google secops
SIEM
This document explains how to collect Palo Alto Networks Traps logs to Google Security Operations by using Bindplane. The parser handles logs in CSV and key-value formats, transforming them into UDM. It uses grok and CSV parsing to extract fields, performs conditional logic based on specific log messages or field values to map to UDM fields, and handles various event types like status updates, network scans, and process creations.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Cortex XDR.
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
PAN_EDR
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
Configure Palo Alto Networks Traps
Sign in to the
Cortex XDR ESM console
.
Select
Settings
>
ESM
>
Syslog
.
Select the
Enable syslog
checkbox.
Provide the following configuration details:
Syslog server
: enter the IP address of the Bindplane agent.
Syslog port
: enter the port number configured in Bindplane; for example,
514
.
Syslog protocol
: select
CEF
.
Set
Keep-alive timeout
as 0.
Communication protocol
: select
UDP
.
In the
Security events
section, select the following checkboxes:
Prevention event
Notification event
Post detection event
Click
Check connectivity
>
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
agentId
event.idm.read_only_udm.additional.fields.value.string_value
The value of
agentId
from the raw log is mapped to the
string_value
field within a nested structure under
additional.fields
. The
key
for this field is set to
Agent ID
.
agentIp
event.idm.read_only_udm.target.ip
The value of
agentIp
from the raw log is mapped to the
target.ip
field.
cat
event.idm.read_only_udm.security_result.rule_name
The value of
cat
from the raw log is mapped to the
security_result.rule_name
field.
class
event.idm.read_only_udm.security_result.category_details
Used in conjunction with
subClass
to populate
security_result.category_details
with the format
class: subClass
.
cs1
event.idm.read_only_udm.principal.application
,
event.idm.read_only_udm.principal.user.email_addresses
If
cs1Label
is
email
, and
cs1
is a valid email address, it's mapped to
principal.user.email_addresses
. If
cs1Label
is
Initiated by
, it's mapped to
principal.application
.
cs2
event.idm.read_only_udm.principal.process.command_line
,
event.idm.read_only_udm.security_result.description
If
cs2Label
is
subtype
, it's mapped to
security_result.description
. If
cs2Label
is
Initiator CMD
, it's mapped to
principal.process.command_line
.
cs3
event.idm.read_only_udm.security_result.action_details
If
cs3Label
is
result
, it's mapped to
security_result.action_details
.
customerId
event.idm.read_only_udm.additional.fields.value.string_value
The value of
customerId
from the raw log is mapped to the
string_value
field within a nested structure under
additional.fields
. The
key
for this field is set to
Customer ID
.
date_time
event.idm.read_only_udm.metadata.event_timestamp.seconds
Parsed and converted to a timestamp, then mapped to
metadata.event_timestamp.seconds
.
desc
event.idm.read_only_udm.metadata.description
The value of
desc
from the raw log is mapped to the
metadata.description
field.
deviceName
event.idm.read_only_udm.target.hostname
The value of
deviceName
from the raw log is mapped to the
target.hostname
field.
email_receiver
event.idm.read_only_udm.network.email.to
Extracted from the
msg
field if it contains an email address and mapped to
network.email.to
.
endpoint_desc
event.idm.read_only_udm.target.resource.attribute.labels.value
Derived from
isEndpoint
:
Yes, host is an endpoint.
if
isEndpoint
is 1,
No, host is not an endpoint
if
isEndpoint
is 0. The
key
is set to
Is Endpoint
.
eventType
event.idm.read_only_udm.metadata.product_event_type
,
event.idm.read_only_udm.metadata.event_type
The value of
eventType
from the raw log is mapped to the
metadata.product_event_type
field. Also used to derive
metadata.event_type
based on its value (e.g.,
Management Audit Logs
results in
EMAIL_TRANSACTION
,
XDR Analytics BIOC
or
Behavioral Threat
results in
SCAN_NETWORK
).
facility
event.idm.read_only_udm.additional.fields.value.string_value
The value of
facility
from the raw log is mapped to the
string_value
field within a nested structure under
additional.fields
. The
key
for this field is set to
Facility
.
fileHash
event.idm.read_only_udm.principal.process.file.sha256
The value of
fileHash
from the raw log, converted to lowercase, is mapped to the
principal.process.file.sha256
field.
filePath
event.idm.read_only_udm.principal.process.file.full_path
The value of
filePath
from the raw log is mapped to the
principal.process.file.full_path
field.
friendlyName
event.idm.read_only_udm.metadata.description
The value of
friendlyName
from the raw log is mapped to the
metadata.description
field.
interm_ip
event.idm.read_only_udm.intermediary.ip
The value of
interm_ip
from the raw log is mapped to the
intermediary.ip
field.
isEndpoint
event.idm.read_only_udm.target.resource.attribute.labels.value
Used to derive
target.resource.attribute.labels.value
.
isVdi
event.idm.read_only_udm.target.resource.resource_type
If
isVdi
is 1,
target.resource.resource_type
is set to
VIRTUAL_MACHINE
.
msg
event.idm.read_only_udm.security_result.summary
The value of
msg
from the raw log is mapped to the
security_result.summary
field. Also used to extract
email_receiver
.
msgTextEn
event.idm.read_only_udm.security_result.description
The value of
msgTextEn
from the raw log is mapped to the
security_result.description
field.
osType
event.idm.read_only_udm.target.platform
,
event.idm.read_only_udm.target.resource.attribute.labels.value
If
osType
is 1,
target.platform
is set to
WINDOWS
. If
osType
is 2,
target.platform
is set to
MAC
. If
osType
is 4,
target.platform
is set to
LINUX
. If
osType
is 3, its value is mapped to
target.resource.attribute.labels.value
with the
key
OS
.
osVersion
event.idm.read_only_udm.target.platform_version
The value of
osVersion
from the raw log is mapped to the
target.platform_version
field.
product_version
event.idm.read_only_udm.metadata.product_version
The value of
product_version
from the raw log is mapped to the
metadata.product_version
field.
proto
event.idm.read_only_udm.network.ip_protocol
If
proto
is
udp
,
network.ip_protocol
is set to
UDP
.
recordType
event.idm.read_only_udm.additional.fields.value.string_value
The value of
recordType
from the raw log is mapped to the
string_value
field within a nested structure under
additional.fields
. The
key
for this field is set to
Record Type
.
regionId
event.idm.read_only_udm.principal.location.country_or_region
If
regionId
is 10,
principal.location.country_or_region
is set to
Americas (N. Virginia)
. If
regionId
is 70,
principal.location.country_or_region
is set to
EMEA (Frankfurt)
.
request
event.idm.read_only_udm.target.url
The value of
request
from the raw log is mapped to the
target.url
field.
sec_category_details
event.idm.read_only_udm.security_result.category_details
The value of
sec_category_details
from the raw log is mapped to the
security_result.category_details
field.
sec_desc
event.idm.read_only_udm.security_result.description
The value of
sec_desc
from the raw log is mapped to the
security_result.description
field.
serverHost
event.idm.read_only_udm.principal.hostname
The value of
serverHost
from the raw log is mapped to the
principal.hostname
field.
severity
event.idm.read_only_udm.security_result.severity
Mapped to
security_result.severity
with the following logic: 2 -> CRITICAL, 3 -> ERROR, 4 -> MEDIUM, 5 -> LOW, 6 -> INFORMATIONAL.
severity_val
event.idm.read_only_udm.security_result.severity
,
event.idm.read_only_udm.security_result.severity_details
If
severity_val
is 0,
security_result.severity_details
is set to
UNKNOWN_SEVERITY
. Otherwise, it's mapped to
security_result.severity
with the following logic: 6 -> LOW, 8 -> MEDIUM, 9 -> HIGH.
shost
event.idm.read_only_udm.principal.hostname
The value of
shost
from the raw log is mapped to the
principal.hostname
field.
src_ip
event.idm.read_only_udm.principal.ip
The value of
src_ip
from the raw log is mapped to the
principal.ip
field.
subClass
event.idm.read_only_udm.security_result.category_details
Used in conjunction with
class
to populate
security_result.category_details
.
suser
event.idm.read_only_udm.principal.user.user_display_name
The value of
suser
from the raw log, with brackets, backslashes, and single quotes removed, is mapped to the
principal.user.user_display_name
field.
targetprocesscmd
event.idm.read_only_udm.target.process.command_line
The value of
targetprocesscmd
from the raw log is mapped to the
target.process.command_line
field.
targetprocessname
event.idm.read_only_udm.target.application
The value of
targetprocessname
from the raw log is mapped to the
target.application
field.
targetprocesssha256
event.idm.read_only_udm.target.process.file.sha256
The value of
targetprocesssha256
from the raw log, converted to lowercase, is mapped to the
target.process.file.sha256
field.
tenantname
event.idm.read_only_udm.target.resource.attribute.labels.value
The value of
tenantname
from the raw log is mapped to the
value
field within a nested structure under
target.resource.attribute.labels
. The
key
for this field is set to
Tenant name
.
event.idm.read_only_udm.metadata.event_type
Set to
STATUS_UPDATE
by default. Changed to
EMAIL_TRANSACTION
if
eventType
is
Management Audit Logs
. Changed to
SCAN_NETWORK
if
eventType
is
XDR Analytics BIOC
or
Behavioral Threat
, or if
desc
is
Behavioral Threat
. Changed to
SCAN_PROCESS
if
desc
is
Suspicious Process Creation
. Set to
Palo Alto Networks
. Set to
Cortex XDR
. Set to
PAN_EDR
. Set to
NETWORK_SUSPICIOUS
if
eventType
is
XDR Analytics BIOC
or
Behavioral Threat
, or if
desc
is
Behavioral Threat
.
Need more help?
Get answers from Community members and Google SecOps professionals.
