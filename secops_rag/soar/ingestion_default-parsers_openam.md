# Collect ForgeRock OpenAM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openam/  
**Scraped:** 2026-03-05T09:56:08.233285Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ForgeRock OpenAM logs
Supported in:
Google secops
SIEM
This document explains how to ingest ForgeRock OpenAM logs to
Google Security Operations using Bindplane. The parser extracts fields from the logs
in CSV, Syslog + KV, or JSON formats, normalizes them, and maps them to the
Unified Data Model (UDM). It handles various OpenAM event types, including
login/logout, access outcomes, and general logs, enriching the data with user,
group, and network information while also performing specific transformations
for different log formats and event types. The parser prioritizes JSON parsing,
then falls back to Syslog+KV, and finally CSV, dropping logs of unsupported
formats.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Forgerock OpenAM (for example, amAdmin)
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
ingestion_labels
:
log_type
:
'OPENAM'
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
Configure Audit Logging in Forgerock OpenAM
Sign in to the
AM
console.
Go to
Configure
>
Global Services
>
Audit Logging
.
Activate
Audit logging to start the audit logging feature.
In the Field allowlist filters and Field blocklist filters lists, enter values to include (allowlist) or exclude (blocklist) from the audit event logs.
Click
Save
.
Configure Syslog Handlers for Forgerock OpenAM
Sign in to the AM console as an administrator, for example
amAdmin
.
To create the event handler in the
global configuration
, go to
Configure
>
Global Services
>
Audit Logging
.
To create the event handler in a
realm
, go to
Realms
>
Realm Name
>
Services
>
Audit Logging
.
Click
Add a Secondary Configuration
>
Syslog
.
Provide the following configuration details:
Name
: Enter a name for the event handler (for example, Google SecOps
Syslog Event Handler
).
Server hostname
: Enter the Bindplane agent IP address.
Server port
: Enter the Bindplane agent port number (for example,
514
for UDP).
Transport Protocol
: Select
UDP
.
Connection timeout
: Enter the number of seconds to connect (for example,
120
).
Optional: Enable the
Buffering
option.
Click
Create
.
After the syslog audit event handler is created, several configuration tabs appear.
On the
General Handler Configuration
tab, select
Enabled
to activate the event handler, if disabled.
Select the topics for audit logs:
Access
Activity
Authentication
Configuration
Click
Save
.
On the
Syslog Configuration
tab, provide the following configuration details:
Server hostname: Enter the Bindplane agent IP address.
Server port: Enter the Bindplane agent port number.
Connection timeout
: Enter the number of seconds to connect (for example,
120
).
Transport Protocol: Select
UDP
.
Facility: Select
Local0
.
All topics set the severity to
INFORMATIONAL
.
Click
Save
.
On the
Buffering
tab, select
Buffering Enabled
to activate it.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
client.ip
principal.ip
The IP address of the client making the request.
client.ip
principal.asset.ip
The IP address of the client asset making the request.
client.port
principal.port
The port used by the client making the request.
entries[0].info.authLevel
principal.resource.resource_subtype
The authentication level associated with the event. Prefixed with "authLevel:".
entries[0].info.displayName
security_result.description
A descriptive name for the node in the authentication tree.
entries[0].info.ipAddress
principal.asset.ip
The IP address associated with the principal in the event.
entries[0].info.ipAddress
principal.ip
The IP address associated with the principal in the event.
entries[0].info.nodeId
principal.resource.id
The unique identifier of the node in the authentication tree. Prefixed with "nodeId:".
entries[0].info.nodeOutcome
principal.resource.attribute.labels.value
The outcome of the node in the authentication tree.
entries[0].info.nodeType
principal.resource.type
The type of the node in the authentication tree. Prefixed with "nodeType:".
entries[0].info.treeName
principal.resource.name
The name of the authentication tree. Prefixed with "treeName:".
eventName
metadata.product_event_type
The raw event name from the OpenAM logs.
http.request.headers.host[0]
target.asset.hostname
The hostname of the target server, extracted from the
host
header.
http.request.headers.host[0]
target.hostname
The hostname of the target server, extracted from the
host
header.
http.request.headers.user-agent[0]
network.http.user_agent
The user-agent of the HTTP request.
http.request.method
network.http.method
The HTTP method used in the request.
http.request.path
target.url
The path of the HTTP request URL.
info.failureReason
security_result.summary
The reason for an authentication failure. Hardcoded to "SSO". Determined by logic based on
eventName
and other fields. Can be
GENERIC_EVENT
,
USER_LOGIN
,
USER_LOGOUT
,
NETWORK_HTTP
, or
STATUS_UPDATE
. Hardcoded to "OPENAM". Hardcoded to "OpenAM". Hardcoded to "ForgeRock".
principal
target.user.userid
The user ID involved in the event, extracted from either
userId
,
principal
, or
runAs
fields.
result
security_result.action_details
The result of the event (e.g., "SUCCESSFUL", "FAILED").
response.detail.reason
security_result.summary
The reason for a failure in an access outcome event.
response.status
security_result.action_details
The status of the response in an access outcome event.
runAs
target.user.userid
The user ID involved in the event, extracted from either
userId
,
principal
, or
runAs
fields.
security_result.action
security_result.action
The action taken as a result of the security event (e.g., "ALLOW", "BLOCK").
server.ip
target.asset.ip
The IP address of the target server.
server.ip
target.ip
The IP address of the target server.
server.port
target.port
The port of the target server.
timestamp
metadata.event_timestamp
The timestamp of the event.
trackingIds
metadata.product_log_id
The tracking ID associated with the event.
transactionId
metadata.product_deployment_id
The transaction ID associated with the event.
userId
target.user.userid
The user ID involved in the event, extracted from either
userId
,
principal
, or
runAs
fields.
userId
target.user.group_identifiers
The group identifiers associated with the user.
am_group
target.user.group_identifiers
The group identifiers associated with the user.
am_user
target.user.email_addresses
The email address of the user, if present in the
am_user
field.
loginID[0]
target.user.userid
The login ID used in the event.
loginID[0]
target.user.email_addresses
The email address used for login, if present in the
loginID
field.
hostip
intermediary.hostname
The hostname of an intermediary device.
hostip
intermediary.ip
The IP address of an intermediary device.
src_ip
principal.asset.ip
The source IP address.
src_ip
principal.ip
The source IP address.
desc
metadata.description
The description of the event.
payload
metadata.description
The payload of the event.
Need more help?
Get answers from Community members and Google SecOps professionals.
