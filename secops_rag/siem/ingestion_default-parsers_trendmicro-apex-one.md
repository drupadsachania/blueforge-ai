# Collect Trend Micro Apex One logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-one/  
**Scraped:** 2026-03-05T09:29:22.846469Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trend Micro Apex One logs
Supported in:
Google secops
SIEM
This document explains how to collect the Trend Micro Apex One logs. The parser extracts data from syslog messages, specifically those formatted with key-value pairs and prefixed with
CEF:
. It uses regular expressions and conditional logic to map CEF fields to the UDM, categorizing events based on the presence of user or system information and identifying the operating system platform. Non-CEF formatted messages are dropped.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Ensure you have administrative access to the Apex Central console
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
directory on Linux or in the installation directory
on Windows.
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
# Using high port to avoid requiring root privileges
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/awx
:
endpoint
:
malachiteingestion-pa.googleapis.com
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
YOUR_CUSTOMER_ID
log_type
:
'TRENDMICRO_APEX_ONE'
raw_log_field
:
body
service
:
pipelines
:
logs/awx
:
receivers
:
-
udplog
exporters
:
-
chronicle/awx
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
Configure Syslog forwarding in Trend Micro Apex One
Sign in to Apex Central console using your administrator credentials:
Go to
Administration
>
Settings
>
Syslog Settings
.
Check the box labeled
Enable syslog forwarding
.
Configure
Syslog Server Details
:
Server Address
: Enter the Bindplane agent IP address or FQDN.
Port
: Enter the Bindplane agent port number (for example,
514
for
UDP
).
Protocol
: Select
UDP
as the transmission protocol.
Optional:
Configure Proxy Settings
: Check Use a SOCKS proxy server.
Log Format
: Select
CEF
.
Frequency
: Define how often logs are forwarded to the Syslog server.
Log Type
: Select
Security logs
and
Product information
.
Click
Test Connection
to ensure that Apex Central can communicate with the Syslog server (Bindplane).
Click
Save
to apply the settings.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action_details
Directly mapped from the
act
field.
ApexCentralHost
about.asset.asset_id
Used as part of the asset_id generation logic. The value "Trend Micro.Apex Central:" is prepended to the
deviceExternalId
field.
app
target.port
Directly mapped from the
app
field.
cat
security_result.category_details
Directly mapped from the
cat
field.
cn1
additional.fields[4].value.string_value
Directly mapped from the
cn1
field. Key is derived from
cn1Label
.
cn1Label
additional.fields[4].key
Directly mapped from the
cn1Label
field.
cn2
additional.fields[6].value.string_value
Directly mapped from the
cn2
field. Key is derived from
cn2Label
.
cn2Label
additional.fields[6].key
Directly mapped from the
cn2Label
field.
cn3
additional.fields[2].value.string_value
Directly mapped from the
cn3
field. Key is derived from
cn3Label
.
cn3Label
additional.fields[2].key
Directly mapped from the
cn3Label
field.
cs1
additional.fields[0].value.string_value
Directly mapped from the
cs1
field. Key is derived from
cs1Label
.
cs1Label
additional.fields[0].key
Directly mapped from the
cs1Label
field.
cs2
additional.fields[1].value.string_value
Directly mapped from the
cs2
field. Key is derived from
cs2Label
.
cs2Label
additional.fields[1].key
Directly mapped from the
cs2Label
field.
cs3
additional.fields[5].value.string_value
Directly mapped from the
cs3
field. Key is derived from
cs3Label
.
cs3Label
additional.fields[5].key
Directly mapped from the
cs3Label
field.
cs4
additional.fields[0].value.string_value
Directly mapped from the
cs4
field. Key is derived from
cs4Label
.
cs4Label
additional.fields[0].key
Directly mapped from the
cs4Label
field.
cs5
additional.fields[2].value.string_value
Directly mapped from the
cs5
field. Key is derived from
cs5Label
.
cs5Label
additional.fields[2].key
Directly mapped from the
cs5Label
field.
cs6
additional.fields[7].value.string_value
Directly mapped from the
cs6
field. Key is derived from
cs6Label
.
cs6Label
additional.fields[7].key
Directly mapped from the
cs6Label
field.
deviceExternalId
about.asset.asset_id
Used as part of the asset_id generation logic. The value "Trend Micro.Apex Central:" is prepended to this field.
deviceNtDomain
about.administrative_domain
Directly mapped from the
deviceNtDomain
field.
devicePayloadId
additional.fields[3].value.string_value
Directly mapped from the
devicePayloadId
field. Key is hardcoded as "devicePayloadId".
deviceProcessName
about.process.command_line
Directly mapped from the
deviceProcessName
field.
dhost
target.hostname
Directly mapped from the
dhost
field.
dntdom
target.administrative_domain
Directly mapped from the
dntdom
field.
dst
target.ip
Directly mapped from the
dst
field.
duser
target.user.userid
,
target.user.user_display_name
Directly mapped from the
duser
field.
dvchost
about.hostname
Directly mapped from the
dvchost
field.
fileHash
about.file.full_path
Directly mapped from the
fileHash
field.
fname
additional.fields[9].value.string_value
Directly mapped from the
fname
field. Key is hardcoded as "fname".
message
metadata.product_event_type
The CEF header is extracted from the message field.
request
target.url
Directly mapped from the
request
field.
rt
metadata.event_timestamp
Directly mapped from the
rt
field.
shost
principal.hostname
Directly mapped from the
shost
field.
src
principal.ip
Directly mapped from the
src
field.
TMCMdevicePlatform
principal.platform
Mapped based on logic in the parser.  Values are normalized to "WINDOWS", "MAC", or "LINUX".
TMCMLogDetectedHost
principal.hostname
Directly mapped from the
TMCMLogDetectedHost
field.
TMCMLogDetectedIP
principal.ip
Directly mapped from the
TMCMLogDetectedIP
field. Derived from parser logic based on the presence of other fields. Possible values are "USER_UNCATEGORIZED", "STATUS_UPDATE", or "GENERIC_EVENT". Hardcoded to "TRENDMICRO_APEX_ONE". Hardcoded to "TRENDMICRO_APEX_ONE". Extracted from the CEF header in the
message
field. Hardcoded to "LOW".
Need more help?
Get answers from Community members and Google SecOps professionals.
