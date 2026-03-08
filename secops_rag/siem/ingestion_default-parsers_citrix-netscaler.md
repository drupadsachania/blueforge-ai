# Collect Citrix NetScaler logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-netscaler/  
**Scraped:** 2026-03-05T09:26:50.000360Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Citrix NetScaler logs
Supported in:
Google secops
SIEM
This document explains how to ingest Citrix NetScaler logs to Google Security Operations using Bindplane.
The parser extracts fields from Citrix NetScaler syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Citrix NetScaler web interface
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
'CITRIX_NETSCALER'
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
CITRIX_NETSCALER
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
Configure Syslog forwarding on Citrix NetScaler
Sign in to the
Citrix NetScaler
web interface (NSIP).
Go to
System
>
Auditing
>
Syslog
.
Click
Servers
tab.
Click
Add
to create a new syslog server.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google-SecOps-Bindplane
).
Server IP
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Log Level
: Select all applicable levels:
ALL
(recommended for comprehensive logging)
Facility
: Select
LOCAL0
(or your preferred facility).
Date Format
: Select
MMDDYYYY
.
Time Zone
: Select
GMT_TIME
(UTC recommended).
TCP Logging
: Select
NONE
(for UDP).
Log Facility
: Select
LOCAL0
.
Click
Create
.
Go to the
Policies
tab.
Click
Add
to create a new syslog audit policy.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google-SecOps-Policy
).
Server
: Select the syslog server created earlier.
Click
Create
.
Bind the policy globally:
Go to
System
>
Auditing
.
Click
Global Bindings
under
Syslog Audit Policies
.
Click
Add Binding
.
Select the policy created earlier.
Click
Bind
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
Alternatively, configure via CLI:
add audit syslogAction Google-SecOps-Bindplane BINDPLANE_IP -serverPort 514 -logLevel ALL -dateFormat MMDDYYYY -timeZone GMT_TIME
add audit syslogPolicy Google-SecOps-Policy ns_true Google-SecOps-Bindplane
bind audit syslogGlobal -policyName Google-SecOps-Policy -priority 100
Replace
BINDPLANE_IP
with the IP address of the Bindplane agent host.
UDM mapping table
Log field
UDM mapping
aaa_info_flags
additional.fields
aaa_trans_id
security_result.detection.fields
aaad_flags
additional.fields
aaad_resp
additional.fields
aaaFlags
additional.fields
aaaFlags2
additional.fields
act
securtiy_result.action_details
,
security_result.action
action
security_result.action
ADM_User
additional.fields
allowed_interface
security_result.detection.fields
applicationname
target.application
auth_type
additional.fields
authActionLen
security_result.detection_fields
AuthAgent
additional.fields
AuthDuration
network.session_duration.seconds
authnvs
additional.fields
authorizationStatus
security_result.detection.fields
AuthStage
additional.fields
Authtype
additional.fields
C
principal.location.country_or_region
caseId
additional.fields
cfg_limit
additional.fields
cgp_tag
sec_result.detection_fields
channel_id_X
additional.fields
channel_id_X_val
additional.fields
channel_update_begin
additional.fields
channel_update_end
additional.fields
cipher_suite
network.tls.cipher
client_fip
target.ip
target.asset.ip
client_fport
target.port
client_ip
principal.ip
,
principal.asset.ip
client_port
principal.port
Client_security_expression
additional.fields
client_type
additional.fields
client_version
network.tls.version
client.nat.ip
principal.nat_ip
,
principal.asset.nat_ip
clientside_jitter
additional.fields
clientside_packet_retransmits
additional.fields
clientside_rtt
additional.fields
clientside_rxbytes
network.sent_bytes
clientside_txbytes
network.received_bytes
ClientVersion
network.tls.version_protocol
CN
principal.resource.attribute.labels
cn1
additional.fields
cn2
additional.fields
code
additional.fields
commandExecutionStatus
security_result.action_details
Compression_ratio_recv
additional.fields
Compression_ratio_send
additional.fields
configurationCmd
security_result.detection.fields
connectionId
network.session_id
copied_nsb
sec_result.detection_fields
core_id
additional.fields
core_refmask
additional.fields
cs1
additional.fields
cs2
additional.fields
cs4
additional.fields
cs5
additional.fields
cs6
additional.fields
CSappid
additional.fields
CSAppname
-
csg_flags
additional.fields
ctx_flags
additional.fields
cur_attempts
additional.fields
CurfactorPolname
additional.fields
customername
additional.fields
days_for_pwd_exp
additional.fields
days_for_pwd_exp_STR
additional.fields
delinkTime
additional.fields
Denied_by_policy
security_result.rule_name
desc
metadata.description
destination.ip
target.ip
,
target.asset.ip
destination.port
target.resource.attribute.labels
device_event_class_id
metadata.product_event_type
device_version
metadata.product_version
Deviceid
target.resource.product_object_id
Devicetype
additional.fields
dht_delete_status
additional.fields
diagnostic_info
additional.fields
digestSignatureAlgorithm
security_result.detection_fields
dns_additional_count
additional.fields
dns_answer_count
additional.fields
dns_authority_count
additional.fields
dns_flags
additional.fields
dns_flags_raw
network.dns.recursion_desired
dns_flags_raw
network.dns.recursion_available
dns_id
network.dns.id
dns_question_count
additional.fields
dns_question_name
network.dns.question.name
domain
security_result.detection.fields
,
additional.fields
domain
target.administrative_domain
ecs_version
additional.fields
encrypt_status
security_result.detection_fields
end_time
additional.fields
End_time
additional.fields
entityName
target.resource.name
Error Code
additional.fields
event_id
metadata.product_log_id
event_name
metadata.product_event_type
event_type
sec_result.summary
expired_refmask
additional.fields
factor
security_result.detection.fields
flags
additional.fields
flags2
additional.fields
flags3
additional.fields
flags4
additional.fields
func
security_result.detection_fields
geolocation
location.country_region
Group(s)
target.user.group_identifiers
Group(s)
target.user.group.identifiers
handshake_time
network.session_duration.seconds
HandshakeTime
additional.fields
host_hostname
principal.hostname
host_ip
principal.ip
principal.asset.ip
host.name
target.hostname
,
target.asset.hostname
hostname
intermediary.hostname
,
intermediary.asset.hostname
hostname
target.hostname
,
target.asset.hostname
hostname_1
target.hostname
,
target.asset.hostname
http_method
network.http.method
Http_resources_accessed
security_result.detection.fields
http_uri
target.url
HTTPS
network.application_protocol
ica_conn_owner_refmask
sec_result.detection_fields
ica_rtt
additional.fields
ica_uuid
network.session_id
ICAUUID
network.session_id
id
metadata.id
init_icamode_homepage
additional.fields
inter_hostname
intermediary.hostname
interfaceKind
security_result.detection.fields
ip
intermediary.asset.ip
ip_x
principal.ip
principal.asset.ip
ipaddress
target.ip
,
target.asset.ip
is_post
additional.fields
IssuerName
network.tls.server.certificate.issuer
L
principal.location.city
last_contact
additional.fields
loc
target.url
localdate
additional.fields
lock_duration
additional.fields
log_action
sec_result.detection_fields
log_action
security_result.detection.fields
log_category
additional.fields
log_data
additional.fields
log_format
additional.fields
log_timestamp
additional.fields
log_type
additional.fields
log.syslog.priority
additional.fields
login_count
sec_result.detection_fields
login_count
security_result.detection_fields
LogoutMethod
additional.fields
max_attempts
additional.fields
message_content
security_result.summary
message_id
metadata.product_log_id
message_status_code
additional.fields
method
network.http.method
monitored_resource
additional.fields
msg
metadata.description
msi_client_cookie
additional.fields
msticks
additional.fields
Nat_ip
additional.fields
,
principal.nat_ip
,
principal.asset.nat_ip
(If the
Nat_ip
isn't an IP address, it is in
additional.fields
.)
netscaler_principal_ip_context
principal.resource.attribute.labels
netscaler_tag
intermediary.asset.product_object_id
netscaler_target_ip_context
target.resource.attribute.labels
new_webview
additional.fields
newWebview
additional.fields
NonHttp_services_accessed
security_result.detection.fields
nsPartitionName
additional.fields
on_port
additional.fields
Organization
principal.resource.attribute.labels
OU
principal.resource.attribute.labels
owner_from
additional.fields
owner_id
additional.fields
pcb_devno
additional.fields
pcbdevno
additional.fields
Policyname
security_result.rule_name
port
principal.port
port_details
principal.port
prin_ip
principal.ip
principal.asset.ip
prin_user
principal.user.userid
principal_ip
principal.ip
,
principal.asset.ip
principal_port
principal.port
prod_event_type
metadata.product_event_type
protocol
network.ip_protocol
protocol_feature
security_result.detection.fields
ProtocolVersion
network.tls.protocol_version
pwdlen
additional.fields
pwdlen2
additional.fields
q_flags
additional.fields
reason_val
security_result.description
receiver_version
additional.fields
record_type
network.dns.question.type
refmask
additional.fields
remote_ip
principal.ip
principal.asset.ip
remote_port
principal.port
request
target.url
ReqURL
additional.fields
resource_cmd
target.resource.name
resource_name
principal.resource.name
response
additional.fields
response_code
additional.fields
rule_id
security_result.rule.id
rule_name
security_result.rule_name
SerialNumber
network.tls.server.certificate.serial
server_authenticated
additional.fields
serverside_jitter
additional.fields
serverside_packet_retransmits
additional.fields
serverside_rtt
additional.fields
service_name
principal.applications
sess_flags2:
additional.fields
sess_seq
network.session_id
sessFlags2
additional.fields
Session
additional.fields
session_cookie
security_result.detection_fields
session_guid
network.session_id
session_id_label
network.session_id
session_setup_time
additional.fields
session_type
sec_result.description
SessionId
network.session_id
skip_code
additional.fields
source_file
additional.fields
source_hostname
principal.hostname
,
principal.asset.hostname
source_line
additional.fields
source.ip
principal.ip
,
principal.asset.ip
source.port
principal.resource.attribute.labels
spcb_id
security_result.detecrion.fields
SPCBId
sec_result.detection_fields
spt
principal.port
src
principal.ip
principal.asset.ip
src_hostname
principal.hostname
principal.asset.hostname
src_ip
principal.ip
principal.asset.ip
src_ip1
src.ip
,
src.asset.ip
src_port
principal.port
ssid
network.session_id
SSLVPN_client_type
additional.fields
SSO
additional.fields
sso
additional.fields
sso_auth_type
additional.fields
sso_flags
security_result.detection_fields
sso_state
additional.fields
SSOduration
additional.fields
SSOurl
additional.fields
ssoUsername
additional.fields
ssoUsername2
additional.fields
ST
principal.location.state
sta_port
additional.fields
sta_ticket
additional.fields
start_time
additional.fields
Start_time
additional.fields
State
security_result.action_details
state
additional.fields
state_value
additional.fields
StatusCode
additional.fields
SubjectName
network.tls.client.certificate.subject
summ
security_result.summary
summary
security_result.summary
sysCmdPolLen
security_result.detection.fields
syslog_priority
additional.fields
tags
additional.fields
tar_ip
target.ip
target.asset.ip
tar_port
target.port
target_id
target.resource.id
target_port
target.port
TCP
network.ip_protocol
timeout_ms
additional.fields
timestamp
metadata.event_timestamp
Total_bytes_send
network.sent_bytes
Total_compressedbytes_recv
additional.fields
Total_compressedbytes_send
additional.fields
Total_policies_allowed
security_result.detection.fields
Total_policies_denied
security_result.detection.fields
Total_TCP_connections
security_result.detection.fields
Total_UDP_flows
security_result.detection.fields
track_flags
additional.fields
trans_id
-
tt
metadata.event_timestamp
User
principal.user.userid
user_agent.original
network.http.user_agent
user_email
principal.user.email_addresses
user_id
principal.user.userid
user.domain
target.administrative_domain
user.name
principal.user.user_display_name
userids
target.user.userid
ValidFrom
network.tls.server.certificate.not_before
ValidTo
network.tls.server.certificate.not_after
version
additional.fields
VPNexportState
additional.fields
Vport
target.port
Vserver Timestamp
additional.fields
vserver_id
target.resource.product_object_id
Vserver_ip
target.ip
,
target.asset.ip
vserver_port
target.port
Vserver_port
target.port
vserver_timestamp
additional.fields
vserver.ip
target.ip
,
target.asset.ip
wirep
additional.fields
wirep_name
additional.fields
wirep_ref_cnt
additional.fields
UDM mapping delta reference
On February 3, 2026, Google SecOps released a new version of the NetScaler parser, which includes significant changes to the mapping of NetScaler log fields to UDM fields and changes to the mapping of event types.
Log-field mapping delta
The following table lists the mapping delta for NetScaler log-to-UDM fields exposed prior to February 3, 2026 and subsequently (listed in the
Old mapping
and
Current mapping
columns respectively):
Log field
Old mapping
Current mapping
act
securit_.result.detetction_fields
securtiy_result.action_details
,
security_result.action
client_ip
additional.fields
principal.ip
,
principal.asset.ip
ClientVersion
network.tls.version
network.tls.version_protocol
connectionId
security_result.detection_fields
network.session_id
CSAppname
-
-
domain
target.user.administrative_domain
security_result.detection.fields
,
additional.fields
end_time
security_result.detection.fields security_result.last_discovered_time
additional.fields
event_id
additional.fields
metadata.product_log_id
geolocation
location.city
location.country_region
Group(s)
target.user.group_display_name
target.user.group_identifiers
HandshakeTime
network.session_duration.seconds
additional.fields
host.name
intermediary.hostname
target.hostname
,
target.asset.hostname
hostname
target.hostname
,
target.asset.hostname
intermediary.hostname
,
intermediary.asset.hostname
hostname
principal.hostname
,
principal.asset.hostname
target.hostname
,
target.asset.hostname
ipaddress
principal.ip
,
principal.asset.ip
target.ip
,
target.asset.ip
Nat_ip
principal.ip
,
principal.asset.ip
principal.nat_ip
,
principal.nat_ip
port_details
principal.labels
principal.port
principal_ip
target.ip
,
target.asset.ip
principal.ip
,
principal.asset.ip
request
security_result.summary
target.url
sess_seq
additional.fields
network.session_id
session_guid
metadata.product_log_id
network.session_id
source_hostname
target.hostname
,
target.asset.hostname
principal.hostname
,
principal.asset.hostname
spcb_id
additional.fields
security_result.detecrion.fields
ssid
additional.fields
network.session_id
start_time
security_result.detection.fields security_result.first_discovered_time
additional.fields
SubjectName
principal.resource.attribute.labels
network.tls.client.certificate.subject
summary
metadata.descritption
security_result.summary
target_port
principal.port
target.port
trans_id
security_result.detection.fields
-
user_id
target.user.userid
principal.user.userid
Event-type mapping delta
The following table lists the delta for the handling of NetScaler event types prior to February 3, 2026 and subsequently (listed in the
Old event_type
and
Current event_type
columns respectively):
Old event_type
Current event_type
Reason
NETWORK_CONNECTION
NETWORK_DNS
If
message_type
is
DNS_QUERY
or named when
has_network_dns
is
true
.
NETWORK_CONNECTION
NETWORK_HTTP
When
message_type
is
SSLVPN HTTPREQUEST
.
STATUS_UPDATE
NETWORK_CONNECTION
Mapped to an appropriate, specific event type.
STATUS_UPDATE
USER_RESOURCE_UPDATE_CONTENT
When
message_type
is SNMP
TRAP_SENT
and
has_target_resource
is
true
, this is mapped to an appropriate, specific event type.
STATUS_UPDATE
USER_UNCATEGORIZED
Mapped to an appropriate, specific event type when principal
userid
is present.
USER_RESOURCE_ACCESS
NETWORK_HTTP
When message_type is
SSLVPN HTTPREQUEST
USER_STATS
GENERIC_EVENT
USER_STATS
is deprecated, so this is mapped to an appropriate, specific event type.
USER_STATS
NETWORK_CONNECTION
USER_STATS
is deprecated, so this is mapped to an appropriate, specific event type.
USER_STATS
USER_LOGIN
USER_STATS
is deprecated, so this is mapped to an appropriate, specific event type.
USER_STATS
USER_LOGOUT
USER_STATS
is deprecated, so this is mapped to an appropriate, specific event type, when
message_type
is
LOGOUT
.
USER_UNCATEGORIZED
GENERIC_EVENT
The log doesn't have any principal machine field to map.
USER_UNCATEGORIZED
NETWORK_CONNECTION
Mapped to an appropriate, specific event type.
USER_UNCATEGORIZED
USER_LOGIN
Mapped to an appropriate, specific event type.
Need more help?
Get answers from Community members and Google SecOps professionals.
