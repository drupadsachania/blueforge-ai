# Collect Trend Micro Deep Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-deep-security/  
**Scraped:** 2026-03-05T09:29:26.953103Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trend Micro Deep Security logs
Supported in:
Google secops
SIEM
This document describes how you can collect the Trend Micro Deep Security logs using Google Security Operations. This parser the logs, which can be in either LEEF+CEF or CEF format, into a unified data model (UDM). It extracts fields from the log messages using grok patterns and key-value pairs, then maps them to corresponding UDM fields, handling various data cleaning and normalization tasks along the way.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to TrendMicro Deep Security console.
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
system where Bindplane Agent will be installed.
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
udplog
:
# Replace the below port <54525> and IP <0.0.0.0> with your specific values
listen_address
:
"0.0.0.0:54525"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the creds location below according the placement of the credentials file you downloaded
creds
:
'{
json
file
for
creds
}'
# Replace <customer_id> below with your actual ID that you copied
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# You can apply ingestion labels below as preferred
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
trendmicro_deep_security
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
Restart Bindplane Agent to apply the changes
In Linux, to restart the Bindplane Agent, run the following command:
sudo
systemctl
restart
bindplane-agent
In Windows, to restart the Bindplane Agent, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog in TrendMicro Deep Security
Sign in to TrenMicro Deep Security console.
Go to
Policies
>
Common Objects
>
Other
>
Syslog Configurations
.
Click
New
>
New Configuration
.
Provide the following details for the configuration:
Name
: unique name that identifies the configuration (for example,
Google SecOps Bindplane
)
Optional:
Description
: add a description.
Log Source Identifier
: specify an identifier to use instead of Deep Security Manager's hostname, if desired.
Server Name
: enter the hostname or IP address of the Syslog server (Bindplane).
Server Port
: specify the listening port number on the server (Bindplane).
Transport
: select
UDP
as the transport protocol.
Event Format
: select
LEEF
or
CEF
(LEEF format requires that you set
Agents should forward logs
to
Via the Deep Security Manager
).
Optional:
Include time zone in events
: whether to add the full date (including year and time zone) to the event.
Optional:
Agents should forward logs
: select
Via the Deep Security Manager
if logs are formatted with LEEF.
Click
Apply
to finalize the settings.
Configure Security Events forwarding
Go to
Policies
and select the policy applied to the computers you want to configure.
Click
Details
.
In the
Policy editor
window, click
Settings
>
Event Forwarding
.
From the
Period between sending of events
section, set the period value to a time period between 10 and 60 seconds.
The default value is 60 seconds, and the recommended value is 10 seconds.
For each of these protection modules:
Anti-Malware Syslog Configuration
Web reputation Syslog Configuration
Firewall
Intrusion prevention Syslog Configuration
Log inspection and Integrity monitoring Syslog Configuration
Select the syslog configuration to use from the context menu:
Syslog Configuration Name
: Select the appropriate configuration.
Click
Save
to apply the settings.
Configure System Events forwarding
Go to
Administration
>
System Settings
>
Event Forwarding
.
From
Forward System Events to a remote computer (via Syslog) using configuration
, select the
existing configuration
created earlier.
Click
Save
.
UDM Mapping Table
Log field
UDM mapping
Logic
act
read_only_udm.security_result.action_details
aggregationType
read_only_udm.additional.fields.value.string_value
Converted to string.
cat
read_only_udm.security_result.category_details
cef_host
read_only_udm.target.hostname
read_only_udm.target.asset.hostname
Used as hostname if dvchost is empty.
cn1
read_only_udm.target.asset_id
Prefixed with "Host Id:".
cs1
read_only_udm.security_result.detection_fields.value
cs1Label
read_only_udm.security_result.detection_fields.key
cs2
read_only_udm.target.file.sha1
read_only_udm.security_result.detection_fields.value
Converted to lowercase and mapped to sha1 if cs2Label is "sha1", otherwise mapped to detection_fields.
cs2Label
read_only_udm.security_result.detection_fields.key
cs3
read_only_udm.target.file.md5
read_only_udm.security_result.detection_fields.value
Converted to lowercase and mapped to md5 if cs3Label is "md5", otherwise mapped to detection_fields.
cs3Label
read_only_udm.security_result.detection_fields.key
cs5
read_only_udm.security_result.detection_fields.value
cs5Label
read_only_udm.security_result.detection_fields.key
cs6
read_only_udm.security_result.detection_fields.value
cs6Label
read_only_udm.security_result.detection_fields.key
cs7
read_only_udm.security_result.detection_fields.value
cs7Label
read_only_udm.security_result.detection_fields.key
cnt
read_only_udm.additional.fields.value.string_value
Converted to string.
desc
read_only_udm.metadata.description
dst
read_only_udm.target.ip
read_only_udm.target.asset.ip
dstMAC
read_only_udm.target.mac
Converted to lowercase.
dstPort
read_only_udm.target.port
Converted to integer.
duser
read_only_udm.target.user.user_display_name
dvc
read_only_udm.about.ip
dvchost
read_only_udm.target.hostname
read_only_udm.target.asset.hostname
event_id
read_only_udm.metadata.product_event_type
Used as product_event_type if event_name is not empty, otherwise used alone.
event_name
read_only_udm.metadata.product_event_type
Prefixed with "[event_id] - " and used as product_event_type.
fileHash
read_only_udm.target.file.sha256
Converted to lowercase.
filePath
read_only_udm.target.file.full_path
"Program
Files
\(x86\)" replaced with "Program Files (x86)".
fsize
read_only_udm.target.file.size
Converted to unsigned integer.
hostname
read_only_udm.target.hostname
read_only_udm.target.asset.hostname
Used as hostname if target is empty.
in
read_only_udm.network.received_bytes
Converted to unsigned integer.
msg
read_only_udm.security_result.description
name
read_only_udm.security_result.summary
organization
read_only_udm.target.administrative_domain
read_only_udm.metadata.vendor_name
proto
read_only_udm.network.ip_protocol
Replaced with "ICMP" if it's "ICMPv6".
product_version
read_only_udm.metadata.product_version
result
read_only_udm.security_result.summary
sev
read_only_udm.security_result.severity
read_only_udm.security_result.severity_details
Mapped to severity based on its value, also mapped to severity_details.
shost
read_only_udm.principal.hostname
read_only_udm.principal.asset.hostname
src
read_only_udm.principal.ip
read_only_udm.principal.asset.ip
srcMAC
read_only_udm.principal.mac
Converted to lowercase.
srcPort
read_only_udm.principal.port
Converted to integer.
suid
read_only_udm.principal.user.userid
suser
read_only_udm.principal.user.user_display_name
target
read_only_udm.target.hostname
read_only_udm.target.asset.hostname
timestamp
read_only_udm.metadata.event_timestamp.seconds
read_only_udm.metadata.event_timestamp.nanos
Parsed to timestamp.
TrendMicroDsBehaviorType
read_only_udm.security_result.detection_fields.value
TrendMicroDsFileSHA1
read_only_udm.target.file.sha1
Converted to lowercase.
TrendMicroDsFrameType
read_only_udm.security_result.detection_fields.value
TrendMicroDsMalwareTarget
read_only_udm.security_result.detection_fields.value
TrendMicroDsMalwareTargetCount
read_only_udm.security_result.detection_fields.value
TrendMicroDsMalwareTargetType
read_only_udm.security_result.detection_fields.value
TrendMicroDsProcess
read_only_udm.security_result.detection_fields.value
"Program
Files
\(x86\)" replaced with "Program Files (x86)".
TrendMicroDsTenant
read_only_udm.security_result.detection_fields.value
TrendMicroDsTenantId
read_only_udm.security_result.detection_fields.value
usrName
read_only_udm.principal.user.userid
read_only_udm.metadata.event_type
Set to "NETWORK_HTTP" if both source and destination are present, otherwise set to "GENERIC_EVENT".
read_only_udm.metadata.log_type
Set to "TRENDMICRO_DEEP_SECURITY".
Need more help?
Get answers from Community members and Google SecOps professionals.
