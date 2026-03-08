# Collect Forescout NAC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-nac/  
**Scraped:** 2026-03-05T09:24:39.837759Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forescout NAC logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forescout Network Access Control (NAC) logs to
Google Security Operations using Bindplane. The parser handles both syslog and
CEF formatted logs from Forescout NAC. It extracts fields using grok patterns,
maps them to the Unified Data Model (UDM), and categorizes events based on
keywords and extracted fields, handling login/logout, network connections,
mail events, and system status updates. Specific logic is implemented for
handling "CounterACT" and "Virtual Firewall" events, including severity mapping
and user context enrichment.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
ForeScout CounterAct v8.0 or latest version should be installed
ForeScout CounterAct core extension module Syslog plugin v3.5 should be installed
Privileged access to Forescout Appliance and CounterACT plug-in
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
Install Bindplane agent
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
'FORESCOUT_NAC'
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
to the path where the authentication file was saved the
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
Install CounterACT Syslog Plugin
Go to the
Forescount Base Plugins
page and download the plugin
.fpi
file.
Save the file to the machine where the
CounterACT Console
is installed.
Sign in to the
CounterACT Console
.
Select
Options
>
Plugins
>
Install
.
Browse to and select the saved plugin FPI file.
Click
Install
.
Accept
the license agreement to proceed.
Once the installation is complete, click
Close
.
Select the plugin from the
Plugin
pane and click
Start
.
Select the
CounterACT Appliances
on which to start the plugin (It's
recommended to run the plugin on all Appliances in the environment).
Click
OK
.
Click
Close
.
Configure Syslog on Forescout CounterACT Syslog Plugin
In the
Plugins
pane, click
Syslog
>
Configure
.
Select any Appliance or the Enterprise Manager from the dialog and click
OK
.
In the
Send Events To
, click
Add
.
Provide the following configuration details:
Server Address
: Enter the Bindplane agent IP address.
Server Port
: Enter the Bindplane agent port number (for example,
514
for UDP).
Server Protocol
: Select
UDP
.
Identity
: Free-text field for identifying the syslog message.
Optional:
Facility
: Syslog message facility that is transmitted as part
of the message Priority field. If the facility value isn't mentioned, it's
set to
local5
.
Severity
: Select
Info
.
Go to the
Syslog Trigger
tab.
Do not select the
Only send messages generated by the "Send Message to Syslog" action
checkbox.
Select only the
Include timestamp and CounterACT device identifier in all messages
checkbox.
Click
Options
to define which event types trigger syslog messages:
Include NAC policy logs.
Include NAC policy match-unmatch events.
Select other events if available.
Go to the
Default Action Configuration
tab.
Provide the following configuration details:
Server Address
: Enter the Bindplane agent IP address.
Server Port
: Enter the Bindplane agent port number (for example,
514
for UDP).
Server Protocol
: Select
UDP
.
Message Identity
: Free-text field for identifying the Syslog message.
Optional:
Facility
: Syslog message facility that is transmitted as part of the message Priority field. If the facility value isn't mentioned, it's set to
local5
.
Severity
: Select
Info
.
Click
OK
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action_details
Directly mapped from the
act
field in CEF logs.
app
network.application_protocol
Directly mapped from the
app
field in CEF logs.
Available_memory
additional.fields
Extracted from
kv_data
when
event_type
is "System statistics".  The key is "Available memory" and the value is the extracted string.
Available_swap
additional.fields
Extracted from
kv_data
when
event_type
is "System statistics". The key is "Available swap" and the value is the extracted string.
application_status
additional.fields
Extracted from
kv_data
when
event_type
is "Application status". The key is "Application status" and the value is the extracted string.
Assigned_hosts
additional.fields
Extracted from
kv_log_data
when
event_type
is "Application status". The key is "Assigned hosts" and the value is the extracted string.
Category
security_result.description
Part of the
security_result.description
when
et_lower
is "nac policy log". Concatenated with other details.
command
principal.process.command_line
Extracted from the
rnmsg
field in CEF logs when it starts with "command:".
Connected_clients
additional.fields
Extracted from
kv_log_data
when
event_type
is "Application status". The key is "Connected clients" and the value is the extracted string.
CPU_usage
additional.fields
Extracted from
kv_data
when
event_type
is "System statistics". The key is "CPU usage" and the value is the extracted string.
cs1
additional.fields
Directly mapped from the
cs1
field in CEF logs. Key is "Compliancy Policy Name".
cs2
additional.fields
Directly mapped from the
cs2
field in CEF logs. Key is "Compliancy Policy Subrule Name".
cs3
additional.fields
Directly mapped from the
cs3
field in CEF logs. Key is "Host Compliancy Status".
cs4
additional.fields
Directly mapped from the
cs4
field in CEF logs. Key is "Compliancy Event Trigger".
data
security_result.description
Used in various parts of the parser to extract information and contribute to the final UDM fields. Not directly mapped to a single UDM field.
details
security_result.description
Used to populate
security_result.description
in several cases, including when parsing "Log" events and user session changes.  May be further parsed for specific information.
Destination
target.ip
,
target.hostname
Parsed from
kv_data
or
data
. If it can be converted to an IP address, it's mapped to
target.ip
. Otherwise, it's mapped to
target.hostname
.
deviceExternalId
about.asset.asset_id
Directly mapped from the
deviceExternalId
field in CEF logs, prefixed with "Forescout.CommandCenter:".
dhost
target.hostname
Directly mapped from the
dhost
field in CEF logs.
dmac
target.mac
Directly mapped from the
dmac
field in CEF logs.
dntdom
target.administrative_domain
Directly mapped from the
dntdom
field in CEF logs.
dst
target.ip
Directly mapped from the
dst
field in CEF logs.
dpt
target.port
Directly mapped from the
dpt
field in CEF logs.
duser
target.user.user_display_name
Directly mapped from the
duser
field in CEF logs.
dvc
about.ip
Directly mapped from the
dvc
field in CEF logs.
dvchost
about.hostname
Directly mapped from the
dvchost
field in CEF logs.
EM_connection_status
additional.fields
Extracted from
kv_log_data
when
event_type
is "Application status". The key is "EM connection status" and the value is the extracted string.
Engine_status
additional.fields
Extracted from
kv_log_data
when
event_type
is "Application status". The key is "Engine status" and the value is the extracted string.
event_type
metadata.description
,
security_result.summary
Parsed from the log message. Used to determine the UDM event type and other fields.  If the event is a "GENERIC_EVENT", it's also used for the description.
eventtype
additional.fields
Directly mapped from the
eventtype
field in CEF logs. The key is "eventtype".
externalId
metadata.product_log_id
Directly mapped from the
externalId
field in CEF logs.
from\[...\] to\[...\]
principal.ip
,
target.ip
Extracts source and destination IPs from the "from[...] to[...]" pattern.
Host
principal.ip
,
principal.hostname
Parsed from
kv_data
when
et_lower
is "block event". If convertible to an IP, mapped to
principal.ip
; otherwise, to
principal.hostname
.
Hostname
principal.hostname
,
principal.asset.hostname
Mapped to
principal.hostname
and
principal.asset.hostname
when present in property change detected events.
Installed_Plugins
additional.fields
Extracted from
kv_log_data
when
event_type
is "Application status". The key is "Installed Plugins" and the value is the extracted string.
iporhost
intermediary.ip
,
intermediary.hostname
Parsed from
header_data
. If convertible to an IP, mapped to
intermediary.ip
; otherwise, to
intermediary.hostname
.
Is Virtual Firewall blocking rule
security_result.action
,
security_result.rule_name
If "true", sets
security_result.action
to "BLOCK" and
security_result.rule_name
to "Virtual Firewall blocking".
log_description
security_result.summary
Directly mapped to
security_result.summary
when present.
log_type
metadata.log_type
Set to a constant value "FORESCOUT_NAC".
MAC
principal.mac
Parsed from
kv_data
in property change detected events and formatted as a MAC address.
mail_from
network.email.from
Directly mapped from the
mail_from
field extracted from
mail_details
.
mail_subject
network.email.subject
Directly mapped from the
mail_subject
field extracted from
mail_details
.
mail_to
network.email.to
Directly mapped from the
mail_to
field extracted from
mail_details
.
Match
security_result.rule_name
Directly mapped from the
Match
field when
et_lower
is "nac policy log".
metadata.event_type
metadata.event_type
Determined by various conditions in the parser, including the presence of specific fields and keywords in the log message.  Defaults to
GENERIC_EVENT
and is updated based on the parsed data.  Examples include
USER_LOGIN
,
USER_LOGOUT
,
NETWORK_CONNECTION
,
SCAN_NETWORK
,
STATUS_UPDATE
,
EMAIL_TRANSACTION
, and
USER_UNCATEGORIZED
.
metadata.product_name
metadata.product_name
Set to "FORESCOUT NAC" for most events, or to the value of the
product
field if it exists.  For CEF events, it's set to "CounterAct".
metadata.vendor_name
metadata.vendor_name
Set to "FORESCOUT" for most events. For CEF events, it's taken from the
cs1Label
field if it exists, or set to "ForeScout Technologies".
msg
metadata.description
Directly mapped from the
msg
field in CEF logs.
pid
intermediary.process.pid
Directly mapped from the
pid
field extracted from
header_data
.
policy_details
security_result.description
Part of the
security_result.description
when
et_lower
is "nac policy log". Concatenated with other details.
product
metadata.product_name
Directly mapped to
metadata.product_name
when present.
proto
network.ip_protocol
Directly mapped from the
proto
field in CEF logs.
Reason
security_result.description
Directly mapped from the
Reason
field when
et_lower
is "block event".
resource
principal.resource.name
Directly mapped from the
resource
field in CEF logs.
rnmsg
security_result.description
,
principal.process.command_line
If it starts with "command:", the part after "command:" is mapped to
principal.process.command_line
. Otherwise, it's mapped to
security_result.description
.
rt
metadata.event_timestamp
Directly mapped from the
rt
field in CEF logs, converted to a timestamp.
Rule
security_result.rule_id
Directly mapped from the
Rule
field when
et_lower
is "nac policy log".
security_result.severity
security_result.severity
Derived from the
severity_level
field.  0-3 maps to LOW, 4-6 maps to MEDIUM, 7-8 maps to HIGH, and 9-10 maps to CRITICAL.
security_result.severity_details
security_result.severity_details
Directly mapped from the
severity
field in CEF logs.
Service
target.port
,
network.ip_protocol
Parsed to extract port and protocol. Port is mapped to
target.port
and protocol to
network.ip_protocol
.
session_id
network.session_id
Directly mapped from the
session_id
field.
severity
security_result.severity_details
Directly mapped from the
severity
field in CEF logs.
severity_level
security_result.severity
Used to determine the
security_result.severity
.
Need more help?
Get answers from Community members and Google SecOps professionals.
