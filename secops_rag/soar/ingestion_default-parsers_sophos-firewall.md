# Collect Sophos XG Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-firewall/  
**Scraped:** 2026-03-05T10:00:35.776685Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sophos XG Firewall logs
Supported in:
Google secops
SIEM
This document explains how to collect Sophos Next Gen (XG) Firewall logs by using Bindplane. The parser extracts logs, normalizes the key-value pairs, and maps them to the UDM. It handles various log formats, converting timestamps, enriching network data, and categorizing events based on log IDs and network activity.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Sophos XG Firewall.
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
SYSLOG
namespace
:
sophos_firewall
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
Configure Sophos Firewall syslog servers
Sign in to the Sophos XG Firewall.
Go to
Configure
>
System services
>
Log settings
.
In the
Syslog servers
section, click
Add
.
Provide the following configuration details:
Name
: enter a unique name for the Google SecOps collector.
IP address/Domain
: enter the Bindplane IP address.
Port
: enter the Bindplane port number.
Facility
: select
DAEMON
.
Severity level
: select
Information
.
Format
: select
Device standard format
.
Click
Save
.
Return to the
Log Settings
page and select the specific log types to forward to the syslog server.
Configure Sophos XG Firewall Log Settings
Select the following
Base firewall (security policy log)
logs:
Policy rules
Invalid traffic
Local ACLs
DoS attack
Dropped ICMP redirected packet
Dropped source routed packet
Dropped fragmented traffic
MAC filtering
IP-MAC pair filtering
IP spoof prevention
SSL VPN tunnel
Protected application server
Heartbeat
Select the following
Web protection
(web filtering log and application filtering log) logs:
Web filter
Application filter
Select the following
Network protection
(IPS log) logs:
Anomaly
Signature
Select the following
System log
log:
System events
UDM Mapping Table
Log Field
UDM Mapping
Logic
activityname
security_result.detection_fields.activityname
Value from the
activityname
field.
app_category
security_result.detection_fields.Application Category
,
application_category
Value from the
app_category
field.
app_filter_policy_id
security_result.detection_fields.app_filter_policy_id
Value from the
app_filter_policy_id
field.
app_is_cloud
security_result.detection_fields.app_is_cloud
Value from the
app_is_cloud
field.
app_name
principal.application
Value from the
app_name
field.
app_resolved_by
security_result.detection_fields.app_resolved_by
Value from the
app_resolved_by
field.
app_risk
security_result.detection_fields.Application Risk
,
application_risk
Value from the
app_risk
field.
app_technology
application_technology
Value from the
app_technology
field.
application
principal.application
Value from the
application
field.
application_category
security_result.detection_fields.Application Category
Value from the
application_category
field.
application_risk
security_result.detection_fields.Application Risk
Value from the
application_risk
field.
application_technology
security_result.detection_fields.Application Technology
Value from the
application_technology
field.
bytes_received
network.received_bytes
Value from the
bytes_received
field.
bytes_sent
network.sent_bytes
Value from the
bytes_sent
field.
category
application_category
Value from the
category
field.
category_type
security_result.detection_fields.category_type
Value from the
category_type
field.
client_host_name
network.dhcp.client_hostname
Value from the
client_host_name
field.
client_physical_address
network.dhcp.chaddr
Value from the
client_physical_address
field.
con_event
security_result.detection_fields.con_event
Value from the
con_event
field.
con_id
security_result.detection_fields.con_id
Value from the
con_id
field.
connevent
security_result.detection_fields.connevent
Value from the
connevent
field.
connid
security_result.detection_fields.connid
Value from the
connid
field.
date
event.timestamp
Parsed from the
date
and
time
fields, adjusted for timezone.
device_id
intermediary.asset.asset_id
Value from the
device_id
field, prefixed with
ID:
.
device_model
intermediary.hostname
Value from the
device_model
field.
device_name
intermediary.hostname
Value from the
device_name
field.
device_serial_id
intermediary.asset.asset_id
Value from the
device_serial_id
field, prefixed with
ID:
.
domain
principal.administrative_domain
,
target.hostname
Value from the
domain
field.
dst_country
target.location.country_or_region
Value from the
dst_country
field.
dst_country_code
target.location.country_or_region
Value from the
dst_country_code
field.
dst_ip
target.ip
Value from the
dst_ip
field.
dst_mac
target.mac
Value from the
dst_mac
field.
dst_port
target.port
Value from the
dst_port
field.
dst_trans_ip
target.nat_ip
Value from the
dst_trans_ip
field.
dst_trans_port
target.nat_port
Value from the
dst_trans_port
field.
dst_zone
security_result.detection_fields.dst_zone
Value from the
dst_zone
field.
dstzone
security_result.detection_fields.dstzone
Value from the
dstzone
field.
dstzonetype
security_result.detection_fields.dstzonetype
Value from the
dstzonetype
field.
duration
network.session_duration.seconds
Value from the
duration
field.
ether_type
security_result.detection_fields.ether_type
Value from the
ether_type
field.
exceptions
security_result.detection_fields.exceptions
Value from the
exceptions
field.
fw_rule_id
security_result.rule_id
Value from the
fw_rule_id
field.
fw_rule_name
security_result.rule_name
Value from the
fw_rule_name
field.
fw_rule_section
security_result.rule_set
Value from the
fw_rule_section
field.
fw_rule_type
security_result.rule_type
Value from the
fw_rule_type
field.
gw_id_request
security_result.detection_fields.gw_id_request
Value from the
gw_id_request
field.
gw_name_request
security_result.detection_fields.gw_name_request
Value from the
gw_name_request
field.
hb_health
security_result.detection_fields.hb_health
Value from the
hb_health
field.
hb_status
security_result.detection_fields.hb_status
Value from the
hb_status
field.
http_category
security_result.detection_fields.http_category
Value from the
http_category
field.
http_category_type
security_result.detection_fields.http_category_type
Value from the
http_category_type
field.
http_status
network.http.response_code
Value from the
http_status
field.
in_display_interface
security_result.detection_fields.in_display_interface
Value from the
in_display_interface
field.
in_interface
security_result.detection_fields.in_interface
Value from the
in_interface
field.
ipaddress
principal.ip
,
network.dhcp.ciaddr
Value from the
ipaddress
field.
log_component
metadata.product_event_type
,
security_result.detection_fields.log_component
Value from the
log_component
field.
log_id
metadata.product_log_id
Value from the
log_id
field.
log_msg
metadata.description
Value from the
message
field after removing
message=
.
log_occurrence
security_result.detection_fields.log_occurrence
Value from the
log_occurrence
field.
log_subtype
security_result.detection_fields.log_subtype
,
security_result.action
Value from the
log_subtype
field.
log_type
security_result.detection_fields.log_type
Value from the
log_type
field.
log_version
security_result.detection_fields.log_version
Value from the
log_version
field.
message
metadata.description
Value from the
message
field.
nat_rule_id
security_result.detection_fields.nat_rule_id
Value from the
nat_rule_id
field.
nat_rule_name
security_result.detection_fields.nat_rule_name
Value from the
nat_rule_name
field.
out_display_interface
security_result.detection_fields.out_display_interface
Value from the
out_display_interface
field.
out_interface
security_result.detection_fields.out_interface
Value from the
out_interface
field.
packets_received
network.received_packets
Value from the
packets_received
field.
packets_sent
network.sent_packets
Value from the
packets_sent
field.
priority
security_result.severity
Mapped from the
priority
or
severity
field based on a lookup table.
protocol
network.ip_protocol
Parsed from the
protocol
field using a lookup table.
reason
security_result.detection_fields.reason
,
security_result.summary
Value from the
reason
field.
recv_bytes
network.received_bytes
Value from the
recv_bytes
field.
recv_pkts
network.received_packets
Value from the
recv_pkts
field.
referer
network.http.referral_url
Value from the
referer
field.
rule_id
security_result.rule_id
Value from the
rule_id
field.
rule_name
security_result.rule_name
Value from the
rule_name
field.
sent_bytes
network.sent_bytes
Value from the
sent_bytes
field.
sent_pkts
network.sent_packets
Value from the
sent_pkts
field.
severity
priority
Value from the
severity
field.
src_country
principal.location.country_or_region
Value from the
src_country
field.
src_country_code
principal.location.country_or_region
Value from the
src_country_code
field.
src_ip
principal.ip
Value from the
src_ip
field.
src_mac
principal.mac
Value from the
src_mac
field.
src_port
principal.port
Value from the
src_port
field.
src_trans_ip
principal.nat_ip
Value from the
src_trans_ip
field.
src_trans_port
principal.nat_port
Value from the
src_trans_port
field.
src_zone
security_result.detection_fields.src_zone
Value from the
src_zone
field.
srczone
security_result.detection_fields.srczone
Value from the
srczone
field.
srczonetype
security_result.detection_fields.srczonetype
Value from the
srczonetype
field.
status
security_result.action_details
,
security_result.action
Value from the
status
field.
status_code
network.http.response_code
Value from the
status_code
field.
target.url
target.url
Value from the
url
field.
time
event.timestamp
Parsed from the
date
and
time
fields, adjusted for timezone.
timestamp
event.timestamp
Parsed from the
timestamp
field.
tran_dst_ip
target.nat_ip
Value from the
tran_dst_ip
field.
tran_dst_port
target.nat_port
Value from the
tran_dst_port
field.
tran_src_ip
principal.nat_ip
Value from the
tran_src_ip
field.
tran_src_port
principal.nat_port
Value from the
tran_src_port
field.
url
target.url
Value from the
url
field.
used_quota
security_result.detection_fields.used_quota
Value from the
used_quota
field.
user_agent
network.http.user_agent
,
network.http.parsed_user_agent
Value from the
user_agent
field. Parsed version also generated.
user_gp
extensions.auth.type
If
user_gp
is
vpn
, sets
extensions.auth.type
to
VPN
.
user_name
principal.user.userid
,
principal.user.email_addresses
Value from the
user_name
field. If it contains
@
, also added to
email_addresses
.
web_policy_id
security_result.detection_fields.web_policy_id
Value from the
web_policy_id
field.
N/A
event.idm.read_only_udm.metadata.event_timestamp
Copied from
event.timestamp
.
N/A
event.idm.read_only_udm.metadata.log_type
The Chronicle ingestion schema specifies the log type as
SOPHOS_FIREWALL
.
N/A
event.idm.read_only_udm.metadata.vendor_name
Constant value
SOPHOS
.
N/A
event.idm.read_only_udm.metadata.product_name
Constant value
SOPHOS Firewall
.
N/A
event.idm.read_only_udm.network.application_protocol
Set to
DHCP
if
ipaddress
field is present. Otherwise, derived from the
protocol
field.
N/A
event.idm.read_only_udm.metadata.event_type
Determined by logic based on the presence of other fields (e.g.,
NETWORK_HTTP
,
NETWORK_CONNECTION
,
NETWORK_DHCP
,
STATUS_UPDATE
,
GENERIC_EVENT
).
N/A
event.idm.read_only_udm.security_result.action
Derived from the
status
or
log_subtype
fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
