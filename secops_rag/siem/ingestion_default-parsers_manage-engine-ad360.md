# Collect ManageEngine AD360 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360/  
**Scraped:** 2026-03-05T09:26:07.140303Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ManageEngine AD360 logs
Supported in:
Google secops
SIEM
This document explains how you can ingest ManageEngine AD360 logs to
Google Security Operations using Bindplane. The parser first cleans up and prepares
the incoming log data and then uses a series of
grok
patterns to extract
relevant fields based on specific event types and message formats. After
extraction, the code maps the extracted fields to the Unified Data Model (UDM),
handles specific data transformations, and enriches the data with additional
context like geolocation and security severity.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to ManageEngine AD360
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
'MANAGE_ENGINE_AD360'
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
Configure ManageEngine AD360 Syslog Export
Sign in to the
AD360
web UI.
Go to
Admin
>
Administration
>
SIEM Integration
.
Click the
Configure Now
link beside the
ADSelfService
component.
Provide the following configuration details:
Server Type
: Select
Syslog
.
Server Name/IP
: Enter the Bindplane agent IP Address.
Port
: Enter the Bindplane agent port number.
Protocol
: Select
UDP
.
Syslog Standard
: Select
RFC5 424
.
Click the
Advanced
list.
Severity
: Select
Informational
.
Click
Configure
to save.
UDM mapping table
Log Field
UDM Mapping
Logic
AccessControlRuleName
security_result.rule_name
Value taken from the field
AccessControlRuleName
if exists, else from the field
rule_name
ACPolicy
security_result.rule_labels.value
Value taken from the field
ACPolicy
action
security_result.action_details
Directly mapped to UDM
action_id
security_result.detection_fields.value
Value taken from the field
action_id
application_protocol
network.application_protocol
Directly mapped to UDM
bytes
network.sent_bytes
Directly mapped to UDM
client_ip
principal.ip
Directly mapped to UDM
ConnectionID
network.session_id
Value taken from the field
connection_id
if exists, else from the field
ConnectionID
, else from the field
ses
destination_ip
target.ip
Directly mapped to UDM
destination_port
target.port
Directly mapped to UDM
DeviceUUID
target.asset_id
Value taken from the field
DeviceUUID
if exists, else from the field
distinguished_name_device_id
distinguished_name_device_id
target.asset_id
Value taken from the field
DeviceUUID
if exists, else from the field
distinguished_name_device_id
distinguished_name_user
target.user.userid
Directly mapped to UDM
DST
target.ip
Value taken from the field
DST
if exists, else from the field
DstIP
DPT
target.port
Value taken from the field
DPT
if exists, else from the field
DstPort
, else from the field
destination_port
DstIP
target.ip
Value taken from the field
DST
if exists, else from the field
DstIP
DstPort
target.port
Value taken from the field
DPT
if exists, else from the field
DstPort
, else from the field
destination_port
EgressInterface
additional.fields.value.string_value
Directly mapped to UDM
EgressZone
target.location.name
Directly mapped to UDM
EventPriority
security_result.severity
Mapped to different severity levels based on the value of
EventPriority
field.
exe
principal.process.command_line
Directly mapped to UDM
geoip.city_name
principal.location.city
Directly mapped to UDM
geoip.country_name
principal.location.country_or_region
Directly mapped to UDM
geoip.latitude
principal.location.region_latitude
Directly mapped to UDM
geoip.longitude
principal.location.region_longitude
Directly mapped to UDM
http_status
network.http.response_code
Directly mapped to UDM
id
metadata.product_log_id
Directly mapped to UDM
IngressInterface
additional.fields.value.string_value
Directly mapped to UDM
IngressZone
principal.location.name
Directly mapped to UDM
LEN
additional.fields.value.string_value
Directly mapped to UDM
message_number
Not Mapped
NAPPolicy
security_result.rule_labels.value
Value taken from the field
NAPPolicy
network_direction
network.direction
Directly mapped to UDM
OUT
additional.fields.value.string_value
Directly mapped to UDM
pid
target.process.pid
Directly mapped to UDM
ppid
target.process.parent_process.pid
Directly mapped to UDM
PREC
additional.fields.value.string_value
Directly mapped to UDM
principal_hostname
principal.hostname
Directly mapped to UDM
product_event_type
metadata.product_event_type
Directly mapped to UDM
protocol
network.ip_protocol
Used to populate the
PROTO
field and then mapped to UDM using a lookup table.
PROTO
network.ip_protocol
Mapped to UDM using a lookup table based on the protocol number.
request_method
network.http.method
Directly mapped to UDM
rule_name
security_result.rule_name
Value taken from the field
AccessControlRuleName
if exists, else from the field
rule_name
ses
network.session_id
Value taken from the field
connection_id
if exists, else from the field
ConnectionID
, else from the field
ses
source_ip
principal.ip
Directly mapped to UDM
source_port
principal.port
Directly mapped to UDM
SPT
principal.port
Value taken from the field
SPT
if exists, else from the field
SrcPort
, else from the field
source_port
SRC
principal.ip
Value taken from the field
SRC
if exists, else from the field
SrcIP
, else from the field
client_ip
SrcIP
principal.ip
Value taken from the field
SRC
if exists, else from the field
SrcIP
, else from the field
client_ip
SrcPort
principal.port
Value taken from the field
SPT
if exists, else from the field
SrcPort
, else from the field
source_port
timestamp
metadata.event_timestamp
Directly mapped to UDM
TOS
additional.fields.value.string_value
Directly mapped to UDM
TTL
additional.fields.value.string_value
Directly mapped to UDM
URL
target.url
Directly mapped to UDM
user_agent
network.http.user_agent
Directly mapped to UDM
WINDOW
additional.fields.value.string_value
Directly mapped to UDM
metadata.vendor_name
Value is hardcoded to
MANAGE_ENGINE_AD360
metadata.product_name
Value is hardcoded to
MANAGE_ENGINE_AD360
metadata.log_type
Value is hardcoded to
MANAGE_ENGINE_AD360
metadata.event_type
Value set to
NETWORK_CONNECTION
if both
SRC
and
DST
fields are present, else set to
STATUS_UPDATE
if either
SRC
or
principal_hostname
is present. If none of these conditions are met, it defaults to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
