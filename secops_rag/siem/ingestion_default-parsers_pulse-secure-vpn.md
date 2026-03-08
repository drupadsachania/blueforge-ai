# Collect Ivanti Connect Secure (Pulse Secure) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pulse-secure-vpn/  
**Scraped:** 2026-03-05T09:27:32.350526Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Ivanti Connect Secure (Pulse Secure) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Ivanti Connect Secure (Pulse Secure) logs to Google Security Operations using Bindplane.
Ivanti Connect Secure (formerly Pulse Secure) is a SSL VPN solution that provides secure remote access to enterprise applications, resources, and networks. It supports multi-factor authentication, endpoint compliance checking, and granular access policies for remote workers and partners. Note: Pulse Secure was acquired by Ivanti in 2020. The parser extracts fields from Pulse Secure VPN syslog formatted logs. It uses grok to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Ivanti Connect Secure (Pulse Secure) admin console
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
'PULSE_SECURE_VPN'
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
PULSE_SECURE_VPN
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
Configure Syslog forwarding on Ivanti Connect Secure (Pulse Secure)
Sign in to the
Ivanti Connect Secure
(formerly Pulse Secure) admin console.
Go to
System
>
Log/Monitoring
>
Syslog Servers
.
Click
New Server
to add a syslog server.
Provide the following configuration details:
Server name/IP
: Enter the IP address of the Bindplane agent host.
Server Port
: Enter
514
.
Facility
: Select
LOCAL0
(or your preferred facility).
Type
: Select
UDP
.
In the
Event Filter
section, select the event types to forward:
Standard
: For standard syslog format
Select the log categories:
Events
: Select
User Access Logs
,
Admin Logs
,
Sensor Events
.
Severity levels
: Select
Info
and above for comprehensive logging.
Click
Save Changes
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.action_details
Directly mapped from the action field.
application
principal.application
Directly mapped from the application field.
bytes_read
network.received_bytes
Directly mapped from the bytes_read field and converted to unsigned integer.
bytes_written
network.sent_bytes
Directly mapped from the bytes_written field and converted to unsigned integer.
client_host
principal.hostname, principal.asset.hostname
Directly mapped from the client_host field.
cmd
principal.process.command_line
Directly mapped from the cmd field.
connection_status
security_result.detection_fields.value.string_value
Directly mapped from the connection_status field.
data_time
metadata.event_timestamp.seconds
Parsed from the data_time field using various timestamp formats (MM-dd-yyyy HH:mm:ss Z, RFC 3339, ISO8601, MMM d HH:mm:ss, MMM d HH:mm:ss).
devname
principal.hostname, principal.asset.hostname
Directly mapped from the devname field.
dstip
target.ip, target.asset.ip
Directly mapped from the dstip field.
dstport
target.port
Directly mapped from the dstport field and converted to integer.
dstcountry
target.location.country_or_region
Directly mapped from the dstcountry field if it's not "Reserved" or empty.
duration
network.session_duration.seconds
Directly mapped from the duration field and converted to integer.
dvc
intermediary.hostname or intermediary.ip
If the dvc field can be converted to an IP address, it's mapped to intermediary.ip. Otherwise, it's mapped to intermediary.hostname.
dvc_hostname
intermediary.hostname, principal.hostname, principal.asset.hostname or intermediary.ip, principal.ip, principal.asset.ip
If the dvc_hostname field can be converted to an IP address, it's mapped to the respective IP fields. Otherwise, it's mapped to the respective hostname fields.
event_type
metadata.product_event_type
Directly mapped from the event_type field.
failure_reason
security_result.description
Directly mapped from the failure_reason field. If the message contains "because host", the text "host" is prepended to the failure reason.
has_principal
event.idm.read_only_udm.principal (presence)
Set to "true" if any principal fields are populated, "false" otherwise. Derived by parser logic.
has_target
event.idm.read_only_udm.target (presence)
Set to "true" if any target fields are populated, "false" otherwise. Derived by parser logic.
has_target_user
event.idm.read_only_udm.target.user.userid (presence)
Set to "true" if target.user.userid is populated, "false" otherwise. Derived by parser logic.
host_ip
principal.ip, principal.asset.ip
Directly mapped from the host_ip field.
host_mac
principal.mac
Directly mapped from the host_mac field, replacing hyphens with colons.
http_method
network.http.method
Directly mapped from the http_method field.
http_response
network.http.response_code
Directly mapped from the http_response field and converted to integer.
info_desc
about.labels.value
Directly mapped from the info_desc field.
ip_new
target.ip, target.asset.ip
Directly mapped from the ip_new field.
level
security_result.severity, security_result.severity_details
The security_result.severity is derived from the level field ("error"/"warning" -> HIGH, "notice" -> MEDIUM, "information"/"info" -> LOW). The raw value of level is also mapped to security_result.severity_details.
logid
metadata.product_log_id
Directly mapped from the logid field.
locip
principal.ip, principal.asset.ip
Directly mapped from the locip field.
message
metadata.description
Used to extract various fields using grok and kv filters. If the message contains "EventID", it's processed as a Windows event log.
message_info
metadata.description
Directly mapped to metadata.description if not otherwise used in more specific grok patterns.
msg
metadata.product_event_type, metadata.description
If the msg field is present, the product type is extracted and mapped to metadata.product_event_type, and the remaining message is mapped to metadata.description.
msg_hostname
principal.hostname, principal.asset.hostname
Directly mapped from the msg_hostname field.
msg_ip
principal.ip, principal.asset.ip
Directly mapped from the msg_ip field.
msg_user_agent
network.http.user_agent, network.http.parsed_user_agent, metadata.product_version
The user agent string is mapped to network.http.user_agent, the parsed user agent is mapped to network.http.parsed_user_agent, and the product version (if present) is mapped to metadata.product_version.
network_duration
network.session_duration.seconds
Directly mapped from the network_duration field and converted to integer.
policyid
security_result.rule_id
Directly mapped from the policyid field.
policyname
security_result.rule_name
Directly mapped from the policyname field.
policytype
security_result.rule_type
Directly mapped from the policytype field.
priority_code
about.labels.value
Directly mapped from the priority_code field and also used to derive about.labels.value for the "Severity" key (see Logic).
prod_name
metadata.product_name
Directly mapped from the prod_name field.
product_type
metadata.product_event_type
Directly mapped from the product_type field.
product_version
metadata.product_version
Directly mapped from the product_version field.
proto
network.ip_protocol
Mapped to network.ip_protocol after being converted to an IP protocol name using a lookup.
pwd
principal.process.file.full_path
Directly mapped from the pwd field.
realm
principal.group.attribute.labels.value
Directly mapped from the realm field.
rcvdbyte
network.received_bytes
Directly mapped from the rcvdbyte field and converted to unsigned integer.
remip
target.ip
Directly mapped from the remip field.
resource_name
target.resource.name
Directly mapped from the resource_name field after removing leading/trailing whitespace and hyphens.
resource_status
security_result.description
Directly mapped from the resource_status field.
resource_user_group
principal.user.group_identifiers
Directly mapped from the resource_user_group field.
resource_user_name
principal.user.userid
Directly mapped from the resource_user_name field.
roles
principal.user.group_identifiers
Directly mapped from the roles field.
sentbyte
network.sent_bytes
Directly mapped from the sentbyte field and converted to unsigned integer.
session_id
network.session_id
Directly mapped from the session_id field.
sessionid
network.session_id
Directly mapped from the sessionid field.
srcip
principal.ip, principal.asset.ip
Directly mapped from the srcip field.
srcport
principal.port
Directly mapped from the srcport field and converted to integer.
srccountry
principal.location.country_or_region
Directly mapped from the srccountry field if it's not "Reserved" or empty.
subtype
metadata.product_event_type
Used in conjunction with type to form metadata.product_event_type.
target_file
target.file.full_path
Directly mapped from the target_file field.
target_host
target.hostname, target.asset.hostname
Directly mapped from the target_host field.
target_ip
target.ip, target.asset.ip
Directly mapped from the target_ip field.
target_port
target.port
Directly mapped from the target_port field and converted to integer.
target_url
target.url
Directly mapped from the target_url field.
time
metadata.event_timestamp.seconds
Parsed from the time field using the "yyyy-MM-dd HH:mm:ss" format.
type
metadata.product_event_type
Used in conjunction with subtype to form metadata.product_event_type.
u_event_source_ip
principal.ip, principal.asset.ip or target.ip
If target_ip or target_host are present, u_event_source_ip is mapped to principal.ip and principal.asset.ip. Otherwise, if target_ip, target_host, and target_url are all empty, u_event_source_ip is mapped to target.ip.
u_observer_ip
observer.ip
Directly mapped from the u_observer_ip field.
u_prin_ip
principal.ip, principal.asset.ip
Directly mapped from the u_prin_ip field.
user
target.user.userid
Directly mapped from the user field.
user_agent
network.http.user_agent, network.http.parsed_user_agent
The user agent string is mapped to network.http.user_agent, and the parsed user agent is mapped to network.http.parsed_user_agent.
user_group_identifier
target.user.group_identifiers or principal.user.group_identifiers
Mapped to target.user.group_identifiers in most cases. Mapped to principal.user.group_identifiers in the IP change (USER_UNCATEGORIZED) and Realm restrictions events.
user_ip
principal.ip, principal.asset.ip
Directly mapped from the user_ip field. If empty and u_event_source_ip is not empty, it takes the value of u_event_source_ip.
username
principal.user.userid or target.user.userid
Mapped to principal.user.userid in most cases. Mapped to target.user.userid in some specific scenarios (e.g., when detect_user_logout_failed is false and detect_policy_change_failed is false).
username_removed
target.user.userid
Directly mapped from the username_removed field.
vd
principal.administrative_domain
Directly mapped from the vd field.
Need more help?
Get answers from Community members and Google SecOps professionals.
