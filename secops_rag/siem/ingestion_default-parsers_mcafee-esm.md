# Collect McAfee Firewall Enterprise logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-esm/  
**Scraped:** 2026-03-05T09:26:10.876272Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect McAfee Firewall Enterprise logs
Supported in:
Google secops
SIEM
This document describes how you can collect McAfee Firewall Enterprise logs. The parser code first extracts fields using a series of Grok patterns, handling both SYSLOG and JSON formats. Then, depending on the identified log category, it applies specific Grok patterns and key-value extractions to map the data into the Google Security Operations UDM schema.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to McAfee ESM.
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
Additional installation resources
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
# Replace with your specific IP and port
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
# Path to the ingestion authentication file
creds
:
'/path/to/your/ingestion-auth.json'
# Your Chronicle customer ID
customer_id
:
'your_customer_id'
endpoint
:
malachiteingestion-pa.googleapis.com
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
mcafee_esm
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
Configure McAfee ESM to Forward Syslog
Sign in to the McAfee ESM console.
Go to the
System Properties
>
Event Forwarding
.
Click
Add
to create a new syslog forwarding rule.
Configure the following settings:
Name
: enter a descriptive name (for example, Google SecOps Forwarding).
Destination IP Address
: enter the IP of your Syslog server (or Bindplane Agent).
Destination Port
: use
514
for UDP (you can specify another port, depending on your Syslog server/Bindplane configuration).
Protocol
: select
UDP
(other choices are TCP or TLS, depending on your Syslog server/Bindplane configuration).
Format
: choose CEF (Common Event Format) or ASCII (recommended format for McAfee logs).
Filters
: define event types you want to forward, for example. firewall logs, authentication events, or threat detections.
Click
Save
.
Restart the
McAfee ESM
service for changes to take effect.
UDM Mapping Table
Log field
UDM mapping
Logic
act
security_result.action_details
The value is taken from the "act" field in the parsed JSON payload.
cat
security_result.category_details
The value is taken from the "cat" field in the parsed JSON payload.
data.AppID
target.application
The value is taken from the "AppID" field in the parsed JSON payload.
data.Destination_Hostname
target.hostname
The value is taken from the "Destination_Hostname" field in the parsed JSON payload.
data.Destination_UserID
target.user.windows_sid
The value is taken from the "Destination_UserID" field in the parsed JSON payload.
data.DomainID
target.administrative_domain
The value is taken from the "DomainID" field in the parsed JSON payload.
data.dst_ip
target.ip
The value is taken from the "dst_ip" field in the parsed JSON payload.
data.dst_mac
target.mac
The value is taken from the "dst_mac" field in the parsed JSON payload.
data.dst_port
target.port
The value is taken from the "dst_port" field in the parsed JSON payload and converted to an integer.
data.HostID
target.hostname
The value is taken from the "HostID" field in the parsed JSON payload.
data.norm_sig.name
This field determines the event type based on its value.
data.PID
target.process.pid
The value is taken from the "PID" field in the parsed JSON payload.
data.Process_Name
target.process.command_line
The value is taken from the "Process_Name" field in the parsed JSON payload.
data.severity
security_result.severity
The value is taken from the "severity" field in the parsed JSON payload, converted to an integer, and mapped to a UDM severity level based on its value: LOW (1-32), MEDIUM (33-65), HIGH (66-100).
data.sig.name
security_result.description
The value is taken from the "sig.name" field in the parsed JSON payload.
data.Source_Logon_ID
about.labels.value
The value is taken from the "Source_Logon_ID" field in the parsed JSON payload.
data.Source_UserID
principal.user.windows_sid
The value is taken from the "Source_UserID" field in the parsed JSON payload.
data.src_ip
principal.ip
The value is taken from the "src_ip" field in the parsed JSON payload.
data.src_mac
principal.mac
The value is taken from the "src_mac" field in the parsed JSON payload.
data.src_port
principal.port
The value is taken from the "src_port" field in the parsed JSON payload and converted to an integer.
data.UserIDDst
target.user.userid
The value is taken from the "UserIDDst" field in the parsed JSON payload.
data.UserIDSrc
principal.user.userid
The value is taken from the "UserIDSrc" field in the parsed JSON payload.
deviceExternalId
about.asset.asset_id
The value is taken from the "deviceExternalId" field in the parsed JSON payload and combined with the product name to create a unique asset ID.
deviceTranslatedAddress
about.nat_ip
The value is taken from the "deviceTranslatedAddress" field in the parsed JSON payload.
dst
target.ip
The value is taken from the "dst" field in the parsed JSON payload.
dpt
target.port
The value is taken from the "dpt" field in the parsed JSON payload and converted to an integer.
eventId
additional.fields.value.string_value
The value is taken from the "eventId" field in the parsed JSON payload.
externalId
metadata.product_log_id
The value is taken from the "externalId" field in the parsed JSON payload.
hostname
principal.hostname
The value is taken from the "hostname" field extracted by the grok pattern.
log_category
metadata.log_type
The value is taken from the "log_category" field extracted by the grok pattern.
log_type
metadata.product_event_type
The value is taken from the "log_type" field extracted by the grok pattern.
message
This field is parsed to extract various fields depending on the log category.
nitroURL
This field is not mapped to the IDM object in the UDM.
pid
principal.process.pid
The value is taken from the "pid" field extracted by the grok pattern.
process_id
about.process.pid
The value is taken from the "process_id" field extracted by the grok pattern.
proto
network.ip_protocol
The value is taken from the "proto" field in the parsed JSON payload and mapped to the corresponding IP protocol.
rhost
principal.ip
The value is taken from the "rhost" field extracted by the grok pattern and parsed as an IP address.
shost
principal.hostname
The value is taken from the "shost" field in the parsed JSON payload.
sntdom
principal.administrative_domain
The value is taken from the "sntdom" field in the parsed JSON payload.
spt
principal.port
The value is taken from the "spt" field in the parsed JSON payload and converted to an integer.
src
principal.ip
The value is taken from the "src" field in the parsed JSON payload.
time
timestamp
The value is taken from the "time" field extracted by the grok pattern and parsed as a timestamp.
type
metadata.product_event_type
The value is taken from the "type" field extracted by the kv filter.
uid
principal.user.userid
The value is taken from the "uid" field extracted by the kv filter.
metadata.event_type
metadata.event_type
The value is set based on the event name and other fields in the log. The logic for determining the event type is as follows: - If the event name contains "TCP", the event type is set to "NETWORK_CONNECTION". - If the event name contains "Mail", the event type is set to "EMAIL_TRANSACTION". - If the event name contains "HTTP" or "http", the event type is set to "NETWORK_HTTP". - If the event name contains "User Accessed" or "denied by access-list", the event type is set to "USER_RESOURCE_ACCESS". - If the event name contains "Data Source Idle", the event type is set to "STATUS_UPDATE". - If the event name contains "Comm with snowflex", the event type is set to "SERVICE_UNSPECIFIED". - If the event name contains "An account was successfully logged on", the event type is set to "USER_LOGIN". - If the event name contains "Initialization status for service objects", the event type is set to "GENERIC_EVENT". - If none of the above conditions are met, the event type is set to "GENERIC_EVENT".
metadata.vendor_name
metadata.vendor_name
The value is set to "MCAFEE".
network.direction
network.direction
The value is set to "INBOUND" if the "deviceDirection" field in the parsed JSON payload is 0. Otherwise, it is set to "OUTBOUND".
security_result.severity
security_result.severity
The value is set to "LOW" if the "cef_event_severity" field in the parsed JSON payload is 1, "MEDIUM" if it is 2, "HIGH" if it is 3, and "CRITICAL" if it is 9.
Need more help?
Get answers from Community members and Google SecOps professionals.
