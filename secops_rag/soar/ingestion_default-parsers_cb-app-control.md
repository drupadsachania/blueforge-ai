# Collect Carbon Black App Control logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-app-control/  
**Scraped:** 2026-03-05T09:51:46.454604Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Carbon Black App Control logs
Supported in:
Google secops
SIEM
This document explains how to collect Carbon Black App Control logs. The parser supports both CEF and JSON formats. It first attempts to parse the input as JSON; if that fails, it treats the input as CEF, performs text substitutions, extracts CEF fields, maps them to UDM, and sets the event type to
GENERIC_EVENT
. Otherwise, it uses a separate JSON-specific UDM mapping include file.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Carbon Black App Control (CB Protection) Server (Version 8.x or later recommended).
Ensure that you have privileged access to Carbon Black App Control.
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
Install Bindplane Agent
Windows Installation
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
Linux Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:11592"
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
JSON
namespace
:
cb_app_control
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
Restart Bindplane Agent to apply the changes
To restart the Bindplane Agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane Agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure CB App Control to Send Syslog Logs
Sign in to the CB App Control console with an Administrator account.
Go to
Admin
>
System Configuration
>
External Logging
In the External Event Logging section:
Enable Syslog Logging
: select the
Syslog Enabled
checkbox.
Server Address
:
<Bindplane Server IP>
.
Port
:
<Bindplane Server PORT>
.
Protocol
: select
TCP
.
Syslog Format
: select
JSON
.
Under
Event Logging Options
, select the types of logs to send:
Policy Violations
File Integrity Monitoring (FIM) events
User Authentication Events
Threat Intelligence Data
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ABId
principal.asset.asset_id
The
ABId
from the JSON log is used as part of the asset ID in the format
PRODUCT_SPECIFIC_ID:{ABId}-{Bit9Server}
.
Bit9Server
principal.asset.asset_id
Used as part of the principal's asset ID, combined with
ABId
. Also used to construct the
metadata.url_back_to_product
field.
CommandLine
about.process.command_line
Directly mapped.
EventType
metadata.product_event_type
Mapped with the corresponding
EventTypeId
in square brackets (e.g.,
[5] - Discovery
).
EventTypeId
metadata.product_event_type
Used with
EventType
to populate
metadata.product_event_type
.
EventSubType
metadata.description
Appended to the
metadata.description
field.
EventSubTypeId
metadata.description
Not explicitly mapped, but potentially contributes to the description based on the parser's internal logic.
externalId
metadata.product_log_id
Directly mapped.
FileHash
about.file.sha256
Directly mapped.
FileName
additional.fields
(with key
FileName
)
Added as an additional field. Also used as part of file information in
metadata.description
for some events.
FilePath
about.file.full_path
Directly mapped.
FileThreat
additional.fields
(with key
fileThreat
)
Added as an additional field.
FileTrust
additional.fields
(with key
fileTrust
)
Added as an additional field.
HostId
principal.asset.asset_id
Used to construct the URL back to the product in
metadata.url_back_to_product
.
HostName
target.hostname
Directly mapped.
HostIP
target.ip
Directly mapped.
Message
metadata.description
Directly mapped.
PathName
about.file.full_path
Directly mapped.
Platform
target.platform
Mapped to the enum value
WINDOWS
.
Policy
additional.fields
(with key
Policy
)
Added as an additional field.
PolicyId
additional.fields
(with key
PolicyId
)
Added as an additional field.
ProcessKey
additional.fields
(with key
ProcessKey
)
Added as an additional field.
ProcessPath
about.process.command_line
Directly mapped.
ProcessPathName
about.process.command_line
Directly mapped.
ProcessThreat
additional.fields
(with key
ProcessThreat
)
Added as an additional field.
ProcessTrust
additional.fields
(with key
ProcessTrust
)
Added as an additional field.
RuleName
additional.fields
(with key
ruleName
)
Added as an additional field.
Timestamp
metadata.event_timestamp
Directly mapped.
UserName
target.user.user_display_name
Directly mapped.
UserSid
principal.user.userid
Directly mapped.
agent.ephemeral_id
observer.labels
(with key
ephemeral_id
)
Added as an observer label.
agent.name
principal.hostname
,
observer.hostname
,
observer.user.userid
Mapped to multiple fields.
agent.type
observer.application
Directly mapped.
agent.version
metadata.product_version
Directly mapped for JSON logs. For CEF logs, extracted from the CEF message.
cat
security_result.category_details
Directly mapped.
cs1
additional.fields
(with key
rootHash
or other cs1Label)
Added as an additional field with the key defined by
cs1Label
.
cs1Label
additional.fields
Used as the key for the additional field populated by
cs1
.
cs2
additional.fields
(with key
installerFilename
or other cs2Label)
Added as an additional field with the key defined by
cs2Label
.
cs2Label
additional.fields
Used as the key for the additional field populated by
cs2
.
cs3
additional.fields
(with key
Policy
or other cs3Label)
Added as an additional field with the key defined by
cs3Label
.
cs3Label
additional.fields
Used as the key for the additional field populated by
cs3
.
cs5
additional.fields
(with key
ruleName
or other cs5Label)
Added as an additional field with the key defined by
cs5Label
.
cs5Label
additional.fields
Used as the key for the additional field populated by
cs5
.
cfp1
additional.fields
(with key
fileTrust
or other cfp1Label)
Added as an additional field with the key defined by
cfp1Label
.
cfp1Label
additional.fields
Used as the key for the additional field populated by
cfp1
.
cfp2
additional.fields
(with key
processTrust
or other cfp2Label)
Added as an additional field with the key defined by
cfp2Label
.
cfp2Label
additional.fields
Used as the key for the additional field populated by
cfp2
.
deviceProcessName
about.process.command_line
Directly mapped.
dhost
target.hostname
Directly mapped.
dst
target.ip
Directly mapped.
duser
target.user.user_display_name
Directly mapped.
dvchost
about.hostname
Directly mapped.
eventId
additional.fields
(with key
eventId
)
Added as an additional field.
fileHash
about.file.sha256
Directly mapped.
flexString1
additional.fields
(with key
fileThreat
or other flexString1Label)
Added as an additional field with the key defined by
flexString1Label
.
flexString1Label
additional.fields
Used as the key for the additional field populated by
flexString1
.
flexString2
additional.fields
(with key
processThreat
or other flexString2Label)
Added as an additional field with the key defined by
flexString2Label
.
flexString2Label
additional.fields
Used as the key for the additional field populated by
flexString2
.
fname
additional.fields
(with key
fname
)
Added as an additional field. Also used as part of file information in
metadata.description
for some events.
host.architecture
target.asset.hardware.cpu_platform
Directly mapped.
host.hostname
target.asset.asset_id
Used as part of the target asset ID (
Host Id: {host.hostname}
). Also mapped to
target.hostname
.
host.id
target.asset.asset_id
Used as part of the target asset ID (
Host Id: {host.id}
).
host.ip
target.asset.ip
Directly mapped.
host.mac
target.mac
Directly mapped.
host.name
target.hostname
Directly mapped.
host.os.build
target.platform_patch_level
Directly mapped.
host.os.kernel
target.platform_patch_level
Appended to the
target.platform_patch_level
.
host.os.platform
target.platform
Mapped to the enum value
WINDOWS
.
host.os.type
target.platform
Mapped to the enum value
WINDOWS
.
host.os.version
target.platform_version
Directly mapped.
log.file.path
target.file.full_path
Directly mapped.
metadata.event_type
metadata.event_type
Set to
GENERIC_EVENT
for CEF logs,
SYSTEM_AUDIT_LOG_UNCATEGORIZED
for JSON logs.
metadata.log_type
metadata.log_type
Set to
CB_EDR
.
metadata.product_log_id
metadata.product_log_id
Mapped from
externalId
for CEF logs. Not applicable for JSON logs.
metadata.product_name
metadata.product_name
Set to
App Control
for CEF logs,
CB_APP_CONTROL
for JSON logs.
metadata.product_version
metadata.product_version
Extracted from the CEF message for CEF logs. Mapped from
agent.version
for JSON logs.
metadata.vendor_name
metadata.vendor_name
Set to
Carbon Black
.
msg
metadata.description
,
additional.fields
Used to populate
metadata.description
and potentially additional fields based on the parser's logic.
sproc
principal.process.command_line
Directly mapped.
metadata.url_back_to_product
metadata.url_back_to_product
Constructed using the
Bit9Server
and
HostId
fields for JSON logs. Not applicable for CEF logs.
security_result.severity
security_result.severity
Set to
MEDIUM
.
timestamp
events.timestamp
Directly mapped for JSON logs. For CEF logs, the parser logic determines the timestamp based on the raw log's
rt
field if available, or the
collection_time
if
rt
is not present.
Need more help?
Get answers from Community members and Google SecOps professionals.
