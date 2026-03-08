# Collect Sophos UTM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-utm/  
**Scraped:** 2026-03-05T09:28:34.505049Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sophos UTM logs
Supported in:
Google secops
SIEM
This document explains how to ingest Sophos UTM logs to Google Security Operations using Bindplane.
Sophos UTM (Unified Threat Management) is an all-in-one network security appliance that provides firewall, VPN, intrusion prevention, web filtering, email filtering, and antivirus capabilities. It offers centralized security management for enterprise networks through a single web-based management console. The parser extracts fields from Sophos UTM KV formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Sophos UTM WebAdmin interface
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
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
udplog
:
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'SOPHOS_UTM'
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
Configuration parameters
Replace the following placeholders:
Receiver configuration:
udplog
: Use
udplog
for UDP syslog or
tcplog
for TCP syslog
0.0.0.0
: IP address to listen on (
0.0.0.0
to listen on all interfaces)
514
: Port number to listen on (standard syslog port)
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
YOUR_CUSTOMER_ID
: Customer ID from the Get customer ID section
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
: Log type exactly as it appears in Chronicle (
SOPHOS_UTM
)
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
To restart the Bindplane agent in Windows, choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Syslog forwarding on Sophos UTM
Sign in to the
Sophos UTM
WebAdmin interface.
Go to
Logging & Reporting
>
Log Settings
>
Remote Syslog Server
.
Click the toggle to
Enable
remote syslog.
Provide the following configuration details:
Remote Syslog Server
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
In the
Remote Syslog Log Selection
section, select the log types to forward:
Packet Filter
: Firewall packet filter logs
Web Filter
: Web filtering activity
IPS
: Intrusion Prevention System events
Authentication
: User authentication events
Email
: Email filtering and quarantine events
Network Protection
: Advanced threat protection logs
WebServer Protection
: WAF logs
VPN
: VPN connection events
HA/Cluster
: High availability and cluster events
System
: System-level events
DHCP
: DHCP server logs
DNS
: DNS query logs
Click
Apply
to save the configuration.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.action
If action is "pass" or "accept", map to "ALLOW". If action is "drop", map to "BLOCK".
ad_domain
target.administrative_domain
Direct mapping.
address
target.ip, target.asset.ip
Direct mapping, used when id is "2203".
app
target.application
Direct mapping.
app-id
additional.fields[].key, additional.fields[].value.string_value
Renamed to app_id. If not empty, the key is set to "app-id" and the value is the app-id itself.
application
principal.application
Direct mapping.
aptptime
additional.fields[].key, additional.fields[].value.string_value
If not empty, the key is set to "aptptime" and the value is the aptptime itself.
auth
extensions.auth.auth_details
Direct mapping.
authtime
additional.fields[].key, additional.fields[].value.string_value
If not empty and not "0", the key is set to "authtime" and the value is the authtime itself.
avscantime
additional.fields[].key, additional.fields[].value.string_value
If not empty and not "0", the key is set to "avscantime" and the value is the avscantime itself.
category
security_result.detection_fields[].key, security_result.detection_fields[].value
If not empty, the key is set to "category" and the value is the category itself. If name contains "portscan", security_result.category is set to "NETWORK_RECON" and a detection field with key "category" and value "NETWORK_RECON" is added.
categoryname
security_result.category_details
Direct mapping.
connection
security_result.rule_name
Direct mapping, used when id is "2203".
content-type data
(See other fields)
The data field contains key-value pairs that are parsed into individual fields.
datetime
metadata.event_timestamp
Parsed and mapped as seconds since epoch.
device
additional.fields[].key, additional.fields[].value.string_value
If not empty and not "0", the key is set to "device" and the value is the device itself.
dnstime
additional.fields[].key, additional.fields[].value.string_value
If not empty and not "0", the key is set to "dnstime" and the value is the dnstime itself.
dstip
target.ip, target.asset.ip
Direct mapping. Also extracted from the url field if present.
dstmac
target.mac
Direct mapping.
dstport
target.port
Direct mapping, converted to integer.
error event
security_result.summary
Direct mapping, used when id is "2201", "2202", or "2203".
exceptions
additional.fields[].key, additional.fields[].value.string_value
If not empty, the key is set to "exceptions" and the value is the exceptions itself.
file
about.file.full_path
Direct mapping.
filteraction
security_result.rule_name
Direct mapping.
fullreqtime
additional.fields[].key, additional.fields[].value.string_value
If not empty, the key is set to "fullreqtime" and the value is the fullreqtime itself.
fwrule
security_result.rule_id
Direct mapping.
group
target.group.group_display_name
Direct mapping.
id
metadata.product_log_id
Direct mapping.
info
security_result.description
Direct mapping. If present, metadata.event_type is set to "NETWORK_UNCATEGORIZED".
initf interface
security_result.about.labels[].key, security_result.about.labels[].value
If not empty, a label with key "Interface" and value interface is added to security_result.about.labels.
ip_address
target.ip, target.asset.ip
Direct mapping.
length line message
security_result.summary
Used when id is "0003". Also used for general grok parsing.
method
network.http.method
Direct mapping.
name
security_result.summary
Direct mapping.
outitf pid
target.process.pid
Direct mapping.
port
target.port
Direct mapping, converted to integer.
prec profile
security_result.rule_name
Direct mapping.
proto
network.ip_protocol
Converted to IP protocol name using a lookup table.
reason referer
network.http.referral_url
Direct mapping.
request
additional.fields[].key, additional.fields[].value.string_value
If not empty, the key is set to "request" and the value is the request itself.
reputation
additional.fields[].key, additional.fields[].value.string_value
If not empty, the key is set to "reputation" and the value is the reputation itself.
rx
network.received_bytes
Direct mapping, used when id is "2202", converted to unsigned integer.
sandbox severity
security_result.severity
If severity is "info", map to "LOW".
size
target.file.size
Direct mapping, converted to unsigned integer.
srcip
principal.ip, principal.asset.ip
Direct mapping.
srcmac
principal.mac
Direct mapping.
srcport
principal.port
Direct mapping, converted to integer.
statuscode
network.http.response_code
Direct mapping, converted to integer.
sub
network.application_protocol
If sub is "http", the metadata.event_type is set to "NETWORK_HTTP" and network.application_protocol is set to "HTTP". If sub is "packetfilter", metadata.description is set to sub. Otherwise, converted to application protocol name using a lookup table. If no match is found in the lookup table, the dstport is used for the lookup.
sys
metadata.product_event_type
Direct mapping.
tcpflags tos ttl tx
network.sent_bytes
Direct mapping, used when id is "2202", converted to unsigned integer.
ua
network.http.user_agent
Direct mapping.
url
network.http.referral_url, target.hostname, target.asset.hostname
Direct mapping for network.http.referral_url. Extracted hostname for target.hostname and target.asset.hostname. Also used to extract dstip.
user
target.user.userid
Direct mapping.
username
target.user.userid
Direct mapping, used when id is "2201" or "2202".
variant
Not included in final UDM, but used in description
Used in conjunction with sub to create the security_result.description when id is "2201", "2202", or "2203".
virtual_ip
target.ip, target.asset.ip
Direct mapping, used when id is "2201" or "2202".
metadata.event_type
metadata.event_type
Initialized to "GENERIC_EVENT". Set to specific values based on log content and parser logic.
metadata.log_type
metadata.log_type
Hardcoded to "SOPHOS_UTM".
metadata.product_name
metadata.product_name
Hardcoded to "SOPHOS UTM".
metadata.vendor_name
metadata.vendor_name
Hardcoded to "SOPHOS Ltd".
intermediary.hostname
intermediary.hostname
Extracted from the log message using grok and renamed.
Need more help?
Get answers from Community members and Google SecOps professionals.
