# Collect Ubiquiti Unifi switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubiquiti-switch/  
**Scraped:** 2026-03-05T09:29:41.760178Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Ubiquiti Unifi switch logs
Supported in:
Google secops
SIEM
This document explains how to ingest Ubiquiti Unifi switch logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages using grok patterns, converting the raw log data into a structured format conforming to the Unified Data Model (UDM). It handles various log formats, extracts key information like timestamps, hostnames, descriptions, and network details, and enriches the data with additional context before merging it into the final UDM event.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the BindPlane agent requirements
Privileged access to the Ubiquiti Controller UI
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
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
/opt/observiq-otel-collector/
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
'UBIQUITI_SWITCH'
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
<CUSTOMER_ID
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
observiq-otel-collector
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop observiq-otel-collector && net start observiq-otel-collector
Configure Ubquiti switch to send Control Plane Syslog
Sign in to the Unifi Controller UI.
Open
Unifi Network
.
Go to
Settings
>
Control Plane
>
Integrations tab
.
Find the
Activity Logging
(Syslog) section.
Enable the
SIEM Server
option.
Provide the following configuration details:
Click
Edit
categories and add the log categories required.
Server Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (
UDP
is required).
Click
Apply Changes
.
Configure Ubquiti switch to send CyberSecure Syslog
Sign in to the Unifi Controller UI.
Open
Unifi Network
.
Go to
Settings
>
CyberSecure
>
Traffic Logging tab
.
Find the
Activity Logging
(Syslog) section.
Enable the
SIEM Server
option.
Provide the following configuration details:
Click
Edit
categories and add the log categories required.
Server Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (
UDP
is required).
Disable
Debug Logs
.
Click
Apply Changes
.
UDM Mapping Table
Log field
UDM mapping
Logic
anomalies
security_result.detection_fields[].key
: "anomalies"
security_result.detection_fields[].value
:
anomalies
value from the log
Directly mapped from the
anomalies
field in the raw log.
application
observer.application
Directly mapped from the
application
field in the raw log.
assoc_status
security_result.detection_fields[].key
: "assoc_status"
security_result.detection_fields[].value
:
assoc_status
value from the log
Directly mapped from the
assoc_status
field in the raw log.
asset_details
observer.asset.product_object_id
: Extracted using grok pattern
%{GREEDYDATA:asset_id},%{GREEDYDATA:asset_version}
asset_software.version
: Extracted using grok pattern
%{GREEDYDATA:asset_id},%{GREEDYDATA:asset_version}
The
asset_details
field is parsed using a grok pattern to extract the
asset_id
and
asset_version
.
asset_id
observer.asset.product_object_id
Directly mapped from the extracted
asset_id
field from
asset_details
.
asset_version
observer.asset.software.version
Directly mapped from the extracted
asset_version
field from
asset_details
.
bssid
principal.mac
Directly mapped from the
bssid
field in the raw log.
description
metadata.description
Directly mapped from the
description
field in the raw log.
device
metadata.product_name
Directly mapped from the
device
field in the raw log. If
device
is not present, the value "UBIQUITI_SWITCH" is used.
dns_resp_seen
security_result.detection_fields[].key
: "dns_resp_seen"
security_result.detection_fields[].value
:
dns_resp_seen
value from the log
Directly mapped from the
dns_resp_seen
field in the raw log.
DST
target.ip
Directly mapped from the
DST
field in the raw log.
DPT
principal.port
Directly mapped from the
DPT
field in the raw log after converting it to an integer.
event_type
security_result.detection_fields[].key
: "event_type"
security_result.detection_fields[].value
:
event_type
value from the log
Directly mapped from the
event_type
field in the raw log.
host
principal.hostname
Directly mapped from the
host
field in the raw log.
ID
additional.fields[].key
: "ID"
additional.fields[].value.string_value
:
ID
value from the log
Directly mapped from the
ID
field in the raw log.
IN
additional.fields[].key
: "IN"
additional.fields[].value.string_value
:
IN
value from the log
Directly mapped from the
IN
field in the raw log.
interface
additional.fields[].key
: "interface"
additional.fields[].value.string_value
:
interface
value from the log
Directly mapped from the
interface
field in the raw log.
LEN
additional.fields[].key
: "LEN"
additional.fields[].value.string_value
:
LEN
value from the log
Directly mapped from the
LEN
field in the raw log.
mac
principal.mac
Directly mapped from the
mac
field in the raw log.
metadata.event_type
metadata.event_type
Derived from parser logic. Set to "STATUS_SHUTDOWN" if
state
is "Down", "STATUS_STARTUP" if
state
is "Up", "STATUS_UPDATE" if
kv_msg
and
DST
are present or
principal_present
is true, and "GENERIC_EVENT" otherwise.
metadata.log_type
metadata.log_type
: "UBIQUITI_SWITCH"
Constant value set by the parser.
metadata.vendor_name
metadata.vendor_name
: "UBIQUITI"
Constant value set by the parser.
principal_ip
principal.ip
Directly mapped from the
principal_ip
field in the raw log.
process_id
observer.process.pid
Directly mapped from the
process_id
field in the raw log.
product_event_type
metadata.product_event_type
Directly mapped from the
product_event_type
field in the raw log.
PROTO
network.ip_protocol
Directly mapped from the
PROTO
field in the raw log. If
PROTO
is "ICMPv6", the value is changed to "ICMP".
query_1
target.administrative_domain
Directly mapped from the
query_1
field in the raw log.
query_server_1
target.ip
Directly mapped from the
query_server_1
field in the raw log.
radio
security_result.detection_fields[].key
: "radio"
security_result.detection_fields[].value
:
radio
value from the log
Directly mapped from the
radio
field in the raw log.
satisfaction_now
security_result.detection_fields[].key
: "satisfaction_now"
security_result.detection_fields[].value
:
satisfaction_now
value from the log
Directly mapped from the
satisfaction_now
field in the raw log.
source_port
principal.port
Directly mapped from the
source_port
field in the raw log after converting it to an integer.
SPT
target.port
Directly mapped from the
SPT
field in the raw log after converting it to an integer.
SRC
principal.ip
,
principal.hostname
Directly mapped from the
SRC
field in the raw log.
sta
principal.mac
Directly mapped from the
sta
field in the raw log.
state
additional.fields[].key
: "state"
additional.fields[].value.string_value
:
state
value from the log
Directly mapped from the
state
field in the raw log.
timestamp
metadata.event_timestamp
Directly mapped from the
timestamp
field in the raw log after being parsed by the date filter.
TTL
additional.fields[].key
: "TTL"
additional.fields[].value.string_value
:
TTL
value from the log
Directly mapped from the
TTL
field in the raw log.
vap
metadata.ingestion_labels[].key
: "Vap"
metadata.ingestion_labels[].value
:
vap
value from the log
Directly mapped from the
vap
field in the raw log.
version
metadata.product_version
Directly mapped from the
version
field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
