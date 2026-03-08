# Collect Darktrace logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/darktrace/  
**Scraped:** 2026-03-05T09:23:04.622261Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Darktrace logs
Supported in:
Google secops
SIEM
This document explains how to ingest Darktrace logs to Google Security Operations
using a Bindplane agent. This parser first extracts common fields from syslog
messages, then uses conditional logic to handle both CEF and JSON formatted
Darktrace logs. It maps extracted fields to the Unified Data Model (UDM) schema,
enriching the data with security context and standardizing event categorization
for downstream analysis.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Darktrace
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
`
https
:
//
github
.
com
/
observIQ
/
bindplane
-
agent
/
releases
/
latest
/
download
/
observiq
-
otel
-
collector
.
msi
`
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
`
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
`
install_unix.sh
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the Configuration File:
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
`
0.0.0.0:10282`
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
DARKTRACE
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
tcplog
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
Restart the Bindlane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on Darktrace
Sign in to the
Darktrace
web UI.
Go to
Admin
>
System Config
.
Click
Verify Alert Settings
.
Provide the following configuration details:
CEF Syslog Alerts
: Select
True
.
CEF Syslog Server
: Enter the Bindplane IP Address.
CEF Syslog Server Port
: Enter the Bindplane port number (for example,
10282
).
CEF Syslog TCP Alert
: Select
True
.
Click
Save
.
Supported Darktrace sample logs
SYSLOG + KV (CEF)
{
"acknowledged"
:
false
,
"commentCount"
:
0
,
"pbid"
:
900000001
,
"time"
:
1604055367000
,
"creationTime"
:
1604055367000
,
"model"
:
{
"name"
:
"Compromise::Agent Beacon to New Endpoint"
,
"uuid"
:
"dfd6f10b-b91c-4244-9fd5-7c35caf21b33"
,
"description"
:
"A device is initiating multiple connections to a new external endpoint..."
,
"priority"
:
2
,
"category"
:
"Informational"
,
"mitre"
:
{
"tactics"
:
[
"command-and-control"
],
"techniques"
:
[
"T1071.001"
]
}
},
"triggeredComponents"
:
[
{
"time"
:
1677679818000
,
"ip"
:
" "
,
"port"
:
443
,
"metric"
:
{
"name"
:
"externalconnections"
},
"triggeredFilters"
:
[
{
"filterType"
:
"Connection hostname"
,
"trigger"
:
{
"value"
:
"beacon.external.io"
}
}
]
}
],
"score"
:
0.85
,
"device"
:
{
"did"
:
90001
,
"macaddress"
:
" "
,
"ip"
:
" "
,
"hostname"
:
"user-laptop-1"
}
}
SYSLOG + JSON
{
"dpi_engine"
:
"dt-sensor-101"
,
"proto"
:
"tcp"
,
"source_ip"
:
" "
,
"source_port"
:
51000
,
"dest_ip"
:
" "
,
"dest_port"
:
389
,
"src"
:
" "
,
"dst"
:
" "
,
"details"
:
"AP request: srealm is [TESTDOMAIN.LOCAL], service is [LDAP/DC99.testdomain.local/testdomain.local], ST cipher is [aes256-cts-hmac-sha1-96]"
,
"epochdate"
:
1690471502.2252
,
"@host"
:
"log-collector-host"
,
"uid"
:
"ABCDEFGHIJ1234567890"
,
"note"
:
"KERBEROS::App"
,
"@type"
:
"notice"
}
UDM mapping table
Log field
UDM mapping
Logic
darktraceUrl
security_result.url_back_to_product
The value is taken from the
darktraceUrl
field.
darktrace_host
observer.hostname
The value is taken from the
darktrace_host
field if it is not an IP address.
darktrace_ip
observer.ip
The value is taken from the
darktrace_ip
field.
darktrace_user
observer.user.userid
The value is taken from the
darktrace_user
field.
description
security_result.summary, metadata.description
The value is taken from the
description
field.
device.customFields.DT-AUTO.macaddress
principal.mac
The value is taken from the
device.customFields.DT-AUTO.macaddress
field.
device.did
principal.asset.asset_id
The value is taken from the
device.did
field, converted to a string, and prefixed with
Device ID:
.
device.firstSeen
principal.asset.first_seen_time
The value is taken from the
device.firstSeen
field, converted to a string, and parsed as a UNIX timestamp in milliseconds.
device.hostname
principal.hostname, principal.asset.hostname
The value is taken from the
device.hostname
field.
device.ip
principal.ip, principal.asset.ip
The value is taken from the
device.ip
field if it matches the IP address format.
device.ips.0.subnet
additional.fields.subnet
The value is taken from the
device.ips.0.subnet
field and prefixed with
subnet
.
device.ips.ip
principal.ip, principal.asset.ip
The value is taken from the
device.ips.ip
field for each IP address in the list.
device.lastSeen
principal.asset.last_discover_time
The value is taken from the
device.lastSeen
field, converted to a string, and parsed as a UNIX timestamp in milliseconds.
device.macaddress
principal.mac
The value is taken from the
device.macaddress
field.
device.objecttype
principal.asset.type
If the value is
device
, the UDM field is set to
WORKSTATION
.
device.sid
principal.resource.attribute.labels.sid
The value is taken from the
device.sid
field and converted to a string.
device.typelabel
principal.resource.attribute.labels.typelabel
The value is taken from the
device.typelabel
field.
device.typename
principal.resource.attribute.labels.typename
The value is taken from the
device.typename
field.
dst
target.ip, target.asset.ip
The value is taken from the
dst
field.
dpt
target.port
The value is taken from the
dpt
field and converted to an integer.
dvc
principal.ip, principal.asset.ip
If the value of
dvc
is an IP address, it is added to the UDM field.
dvchost
principal.hostname, principal.asset.hostname
The value is taken from the
dvchost
field.
endpoint
target.url
The value is taken from the
endpoint
field.
event_time
metadata.event_timestamp
The value is taken from the
event_time
field and parsed as an ISO8601 timestamp.
externalId
metadata.product_log_id
The value is taken from the
externalId
field.
incidentEventUrl
principal.url
The value is taken from the
incidentEventUrl
field.
ip
principal.ip, principal.asset.ip
The value is taken from the
ip
field if it matches the IP address format.
issue_msg
security_result.summary
The value is taken from the
issue_msg
field.
message
security_result.description
The value is taken from the
message
field.
method
network.http.method
The value is taken from the
method
field.
model.description
metadata.description
The value is taken from the
model.description
field.
model.name
metadata.product_event_type
The value is taken from the
model.name
field.
model.now.category
security_result.severity
If the value is
critical
, the UDM field is set to
CRITICAL
. If the value is
Informational
, the UDM field is set to
INFORMATIONAL
. If the value is
Suspicious
, the UDM field is set to
HIGH
and the category is set to
NETWORK_SUSPICIOUS
.
model.now.description
metadata.description
The value is taken from the
model.now.description
field.
model.now.message
security_result.description
The value is taken from the
model.now.message
field.
model.now.name
metadata.product_event_type
The value is taken from the
model.now.name
field.
model.now.pid
principal.process.pid
The value is taken from the
model.now.pid
field and converted to a string.
model.now.uuid
principal.user.userid
The value is taken from the
model.now.uuid
field and the event type is set to
USER_UNCATEGORIZED
.
model.pid
principal.process.pid
The value is taken from the
model.pid
field and converted to a string.
model.then.description
principal.resource.attribute.labels.Model Then Description
The value is taken from the
model.then.description
field.
model.then.name
principal.resource.attribute.labels.Model Then Name
The value is taken from the
model.then.name
field.
model.then.pid
principal.resource.attribute.labels.Model Then Pid
The value is taken from the
model.then.pid
field and converted to a string.
model.then.uuid
principal.resource.attribute.labels.Model Then UUID
The value is taken from the
model.then.uuid
field.
model.uuid
principal.user.userid
The value is taken from the
model.uuid
field and the event type is set to
USER_UNCATEGORIZED
.
relatedBreaches.0.modelName
security_result.description
The value is taken from the
relatedBreaches.0.modelName
field.
score
security_result.priority, security_result.priority_details
If the value is between 0.8 and 1, the priority is set to
HIGH_PRIORITY
. If the value is between 0.5 and 0.79, the priority is set to
MEDIUM_PRIORITY
. If the value is between 0 and 0.49, the priority is set to
LOW_PRIORITY
. The priority details are set to
Score :
followed by the value of
score
converted to a string.
severity
security_result.severity
If the value is 2, the UDM field is set to
MEDIUM
. If the value is greater than 2, the UDM field is set to
HIGH
.
shost
principal.hostname, principal.asset.hostname
The value is taken from the
shost
field.
smac
principal.mac
The value is taken from the
smac
field.
src
principal.ip, principal.asset.ip
The value is taken from the
src
field.
status
network.http.response_code
The value is taken from the
status
field and converted to a string.
summary
metadata.description
The value is taken from the
summary
field.
time
The value is taken from the
time
field, converted to a string, and parsed as a UNIX timestamp in milliseconds.
timestamp
The value is taken from the
timestamp
field and parsed as either an ISO8601 timestamp or a UNIX timestamp in milliseconds.
title
security_result.summary
The value is taken from the
title
field.
triggeredComponents.ip
intermediary.ip
The value is taken from the
triggeredComponents.ip
field if it matches the IP address format.
triggeredComponents.port
intermediary.port
The value is taken from the
triggeredComponents.port
field and converted to an integer.
username
principal.user.userid
The value is taken from the
username
field.
metadata.vendor_name
Set to
DARKTRACE
.
metadata.product_name
Set to
DCIP
.
metadata.log_type
Set to
DARKTRACE
.
network.ip_protocol
Set to
TCP
if
issue_msg
doesn't contain
UDP
. Otherwise set to
UDP
.
security_result.action
Set to
BLOCK
if
status
is
401
, otherwise set to
ALLOW
.
security_result.severity
Set to
INFORMATIONAL
.
network.application_protocol
Set to
HTTP
if
method
is not empty.
metadata.event_type
Set to
NETWORK_HTTP
if
method
is not empty. Set to
USER_LOGIN
if
description
contains
logged into \\\\S+ over ssh
. Set to
NETWORK_CONNECTION
if
target_ip
is not empty. Otherwise, set to
STATUS_UPDATE
.
extensions.auth.type
Set to
MACHINE
if
description
contains
logged into \\\\S+ over ssh
.
security_result.category
Set to
DATA_EXFILTRATION
if
issue_msg
contains
Exfiltration
. Set to
NETWORK_MALICIOUS
if
issue_msg
contains
Compromise
. Otherwise, set to
NETWORK_SUSPICIOUS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
