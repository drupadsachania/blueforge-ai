# Collect WatchGuard Fireware logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/watchguard/  
**Scraped:** 2026-03-05T09:30:16.060040Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect WatchGuard Fireware logs
Supported in:
Google secops
SIEM
Overview
This parser extracts WatchGuard Fireware logs in JSON or key-value (KV) format, transforming them into UDM. It handles "Traffic" and "Event" logs differently, using grok and kv filters to extract fields and map them to UDM, with specific logic for various
msg_id
values and event names, handling network protocols, user actions, security results, and other relevant details. It also processes a second group of syslog entries, extracting similar information and mapping it to the UDM format.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have privileged access to Watchguard.
Ensure that you have a Windows 2012 SP2 or later or Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
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
For
Windows installation
, run the following script:
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
.
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
.
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane is installed.
Edit the
config.yaml
file as follows:
receivers:
  tcplog:
    # Replace the below port <54525> and IP (0.0.0.0) with your specific values
    listen_address: "0.0.0.0:54525" 

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        # Adjust the creds location below according the placement of the credentials file you downloaded
        creds: '{ json file for creds }'
        # Replace <customer_id> below with your actual ID that you copied
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        # You can apply ingestion labels below as preferred
        ingestion_labels:
        log_type: SYSLOG
        namespace: testNamespace
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart Bindplane Agent to apply the changes using the following command:
sudo systemctl bindplane restart
Add Syslog server configuration to Watchguard
Sign in to Watchguard UI.
Select
System
>
Logging
.
Click
Syslog Server
tab.
Select
Send log messages to these syslog servers
checkbox.
Click
Add
.
Specify values for the input parameters in the
Syslog Server
dialog:
IP Address
: type the server IP address.
Port
: change the default syslog server port (514), type a different port for your server.
Log Format
: select
Syslog
from the drop-down.
Optional:
Description
: type a description for the server (for example,
Google SecOps export
).
Optional:
The time stamp
: select the
check box
to include the date and time that the event occurs on your Firebox in the log message details.
Optional:
The serial number of the device
select the checkbox to include the serial number of the Firebox in the log message details.
Syslog facility
: for each type of log message, select a priority from the drop-down (for example, high-priority syslog messages, such as
alarms
, select
Local0
).
Optional:
Restore Defaults
: to restore the default settings.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.action_details
The value of
action
from the raw log is assigned to
security_result.action_details
.
action
target.labels.value
The value of
action
from the raw log is assigned to
target.labels.value
, with
target.labels.key
being "Action over resource".
arg
target.file.full_path
The value of
arg
from the raw log is assigned to
target.file.full_path
.
app_cat_id
about.labels.value
The value of
app_cat_id
from the raw log is assigned to
about.labels.value
, with
about.labels.key
being "app_cat_id".
app_cat_name
target.application
Used in combination with
app_name
to form the value of
target.application
(e.g., "Google - Web services").
app_id
about.labels.value
The value of
app_id
from the raw log is assigned to
about.labels.value
, with
about.labels.key
being "app_id".
app_name
target.application
Used in combination with
app_cat_name
to form the value of
target.application
(e.g., "Google - Web services").
cats
security_result.category_details
The value of
cats
from the raw log is assigned to
security_result.category_details
.
cert_issuer
network.tls.server.certificate.issuer
The value of
cert_issuer
from the raw log is assigned to
network.tls.server.certificate.issuer
.
cert_subject
network.tls.server.certificate.subject
The value of
cert_subject
from the raw log is assigned to
network.tls.server.certificate.subject
.
cn
network.tls.server.certificate.subject
The value of
cn
from the raw log is assigned to
network.tls.server.certificate.subject
.
conn_action
security_result.action_details
The value of
conn_action
from the raw log is assigned to
security_result.action_details
.
content_type
Not mapped
Not mapped to the IDM object in the provided UDM examples.
description
metadata.description
The value of
description
derived from the raw log is assigned to
metadata.description
.
dhcp_type
network.dhcp.type
The value of
dhcp_type
from the raw log is mapped to the corresponding DHCP type in
network.dhcp.type
(e.g., "REQUEST", "ACK").
dst_host
target.hostname
The value of
dst_host
from the raw log is assigned to
target.hostname
.
dst_ip
target.ip
The value of
dst_ip
from the raw log is assigned to
target.ip
.
dst_mac
target.mac
The value of
dst_mac
from the raw log is assigned to
target.mac
.
dst_port
target.port
The value of
dst_port
from the raw log is assigned to
target.port
.
dst_user
target.user.user_display_name
The value of
dst_user
from the raw log is assigned to
target.user.user_display_name
.
dstname
target.administrative_domain
The value of
dstname
from the raw log is assigned to
target.administrative_domain
.
duration
Not mapped
Not mapped to the IDM object in the provided UDM examples.
elapsed_time
Not mapped
Not mapped to the IDM object in the provided UDM examples.
endpoint
intermediary.labels.value
The value of
endpoint
from the raw log is assigned to
intermediary.labels.value
, with
intermediary.labels.key
being "Gateway-Endpoint".
event_name
principal.application
The value of
event_name
from the raw log is assigned to
principal.application
.
firewall_id
intermediary.asset_id
The value of
firewall_id
from the raw log is prepended with "Firewall ID : " and assigned to
intermediary.asset_id
.
firewall_name
principal.asset_id
The value of
firewall_name
from the raw log is prepended with "Firewall: " and assigned to
principal.asset_id
.
firewallname
intermediary.hostname
The value of
firewallname
from the raw log is assigned to
intermediary.hostname
.
firewallname
principal.hostname
The value of
firewallname
from the raw log is assigned to
principal.hostname
.
fqdn_dst_match
Not mapped
Not mapped to the IDM object in the provided UDM examples.
geo
Not mapped
Not mapped to the IDM object in the provided UDM examples.
geo_dst
target.location.country_or_region
The value of
geo_dst
from the raw log is assigned to
target.location.country_or_region
.
geo_src
principal.location.country_or_region
The value of
geo_src
from the raw log is assigned to
principal.location.country_or_region
.
host
Not mapped
Not mapped to the IDM object in the provided UDM examples.
ike_policy
security_result.rule_id
The value of
ike_policy
from the raw log is assigned to
security_result.rule_id
.
ike_policy_version
security_result.rule_version
The value of
ike_policy_version
from the raw log is assigned to
security_result.rule_version
.
intermediary_host
intermediary.hostname
The value of
intermediary_host
from the raw log is assigned to
intermediary.hostname
.
ipaddress
Not mapped
Not mapped to the IDM object in the provided UDM examples.
ipsec_policy
Not mapped
Not mapped to the IDM object in the provided UDM examples.
ipsec_policy_version
Not mapped
Not mapped to the IDM object in the provided UDM examples.
keyword
Not mapped
Not mapped to the IDM object in the provided UDM examples.
line
Not mapped
Not mapped to the IDM object in the provided UDM examples.
log_message
metadata.description
The value of
log_message
from the raw log is assigned to
metadata.description
when other more specific descriptions are not available.
log_reason
security_result.summary
The value of
log_reason
from the raw log is assigned to
security_result.summary
.
log_type
metadata.log_type
The value of
log_type
from the raw log is assigned to
metadata.log_type
.  Always set to "WATCHGUARD".
msg
security_result.summary
The value of
msg
from the raw log is assigned to
security_result.summary
.
msg_id
metadata.product_event_type
The value of
msg_id
from the raw log is assigned to
metadata.product_event_type
.
new_action
security_result.action_details
Used with
conn_action
to form the value of
security_result.action_details
(e.g., "ProxyReplace: IP protocol    - HTTPS-Client.DPI-Off").
op
network.http.method
The value of
op
from the raw log is assigned to
network.http.method
.
path
target.url
The value of
path
from the raw log is assigned to
target.url
.
pid
Not mapped
Not mapped to the IDM object in the provided UDM examples.
policy_name
intermediary.resource.name
The value of
policy_name
from the raw log is assigned to
intermediary.resource.name
.
policy_name
security_result.rule_name
The value of
policy_name
from the raw log is assigned to
security_result.rule_name
.
policyname_label.value
security_result.rule_labels.value
The value of
policy_name
from the raw log is assigned to
security_result.rule_labels.value
, with
security_result.rule_labels.key
being "PolicyName".
prin_host
principal.hostname
The value of
prin_host
from the raw log is assigned to
principal.hostname
.
proc_id
Not mapped
Not mapped to the IDM object in the provided UDM examples.
protocol
network.ip_protocol
The value of
protocol
from the raw log, converted to uppercase, is assigned to
network.ip_protocol
. Special handling for "EXTERNAL ICMP" which is mapped to "ICMP".
proxy_act
security_result.rule_id
The value of
proxy_act
from the raw log is assigned to
security_result.rule_id
.
proxy_act
security_result.rule_name
The value of
proxy_act
from the raw log is assigned to
security_result.rule_name
.
query_name
network.dns.questions.name
The value of
query_name
from the raw log is assigned to
network.dns.questions.name
.
query_type
network.dns.questions.type
The value of
query_type
from the raw log is assigned to
network.dns.questions.type
. Special handling for numeric query types and mapping to standard DNS query types.
rc
Not mapped
Not mapped to the IDM object in the provided UDM examples.
reason
security_result.summary
The value of
reason
from the raw log is assigned to
security_result.summary
.
record_type
network.dns.answers.type
The value of
record_type
from the raw log is mapped to the corresponding DNS record type in
network.dns.answers.type
.
redirect_action
Not mapped
Not mapped to the IDM object in the provided UDM examples.
reputation
additional.fields.value.string_value
The value of
reputation
from the raw log is assigned to
additional.fields.value.string_value
, with
additional.fields.key
being "reputation".
response
Not mapped
Not mapped to the IDM object in the provided UDM examples.
response_code
network.dns.response_code
The value of
response_code
from the raw log is mapped to the corresponding DNS response code in
network.dns.response_code
.
route_type
Not mapped
Not mapped to the IDM object in the provided UDM examples.
rule_name
security_result.rule_name
The value of
rule_name
from the raw log is assigned to
security_result.rule_name
.
rcvd_bytes
network.received_bytes
The value of
rcvd_bytes
from the raw log is assigned to
network.received_bytes
.
sent_bytes
network.sent_bytes
The value of
sent_bytes
from the raw log is assigned to
network.sent_bytes
.
server_ssl
Not mapped
Not mapped to the IDM object in the provided UDM examples.
severity
Not mapped
Not mapped to the IDM object in the provided UDM examples.
sig_vers
network.tls.server.certificate.version
The value of
sig_vers
from the raw log is assigned to
network.tls.server.certificate.version
.
signature_cat
additional.fields.value.string_value
The value of
signature_cat
from the raw log is assigned to
additional.fields.value.string_value
, with
additional.fields.key
being "signature_cat".
signature_id
additional.fields.value.string_value
The value of
signature_id
from the raw log is assigned to
additional.fields.value.string_value
, with
additional.fields.key
being "signature_id".
signature_name
additional.fields.value.string_value
The value of
signature_name
from the raw log is assigned to
additional.fields.value.string_value
, with
additional.fields.key
being "signature_name".
sni
network.tls.client.server_name
The value of
sni
from the raw log is assigned to
network.tls.client.server_name
.
src_ctid
Not mapped
Not mapped to the IDM object in the provided UDM examples.
src_host
principal.hostname
The value of
src_host
from the raw log is assigned to
principal.hostname
.
src_ip
principal.ip
The value of
src_ip
from the raw log is assigned to
principal.ip
.
src_ip_nat
Not mapped
Not mapped to the IDM object in the provided UDM examples.
src_mac
principal.mac
The value of
src_mac
from the raw log is assigned to
principal.mac
.
src_port
principal.port
The value of
src_port
from the raw log is assigned to
principal.port
.
src_user
principal.user.user_display_name
The value of
src_user
from the raw log is assigned to
principal.user.user_display_name
.
src_user_name
principal.user.user_display_name
The value of
src_user_name
from the raw log is assigned to
principal.user.user_display_name
.
src_vpn_ip
principal.ip
The value of
src_vpn_ip
from the raw log is assigned to
principal.ip
.
srv_ip
Not mapped
Not mapped to the IDM object in the provided UDM examples.
srv_port
Not mapped
Not mapped to the IDM object in the provided UDM examples.
ssl_offload
Not mapped
Not mapped to the IDM object in the provided UDM examples.
tcp_info
Not mapped
Not mapped to the IDM object in the provided UDM examples.
time
metadata.event_timestamp.seconds
,
timestamp.seconds
The value of
time
from the raw log is parsed and used to populate
metadata.event_timestamp.seconds
and
timestamp.seconds
.
time1
metadata.event_timestamp.seconds
,
timestamp.seconds
The value of
time1
from the raw log is parsed and used to populate
metadata.event_timestamp.seconds
and
timestamp.seconds
.
tls_profile
about.labels.value
The value of
tls_profile
from the raw log is assigned to
about.labels.value
, with
about.labels.key
being "tls_profile".
tls_version
Not mapped
Not mapped to the IDM object in the provided UDM examples.
user_name
principal.user.userid
,
principal.user.user_display_name
The value of
user_name
from the raw log is assigned to
principal.user.userid
or
principal.user.user_display_name
depending on the context.
user_type
Not mapped
Not mapped to the IDM object in the provided UDM examples.
(N/A)
intermediary.resource.type
Always set to "ACCESS_POLICY".
(N/A)
metadata.event_type
Determined by parser logic based on
msg_id
,
log_type
,
event_name
, and other fields. Can be
NETWORK_CONNECTION
,
SERVICE_MODIFICATION
,
NETWORK_SMTP
,
NETWORK_DNS
,
NETWORK_HTTP
,
USER_LOGIN
,
USER_LOGOUT
,
USER_RESOURCE_UPDATE_CONTENT
,
RESOURCE_PERMISSIONS_CHANGE
,
RESOURCE_CREATION
,
GENERIC_EVENT
,
STATUS_UPDATE
, or
USER_UNCATEGORIZED
.
(N/A)
metadata.product_name
Always set to "Fireware".
(N/A)
metadata.vendor_name
Always set to "Watchguard".
(N/A)
security_result.action
Determined by parser logic based on
disposition
. Can be "ALLOW" or "BLOCK".
(N/A)
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" for user login/logout events, and "VPN" for network events related to VPNs.
(N/A)
network.application_protocol
Determined by parser logic based on
msg_id
and
event_name
. Can be "DNS", "DHCP", "HTTP", or "HTTPS".
(N/A)
network.dns.questions.type
Set to 1 for "A" record queries.
(N/A)
target.labels.key
Set to "Action over resource" when
action
is mapped to
target.labels.value
.
(N/A)
intermediary.labels.key
Set to "Firewall Member Name" when
prin_host
is mapped to
intermediary.labels.value
.
(N/A)
intermediary.labels.key
Set to "Gateway-Endpoint" when
endpoint
is mapped to
intermediary.labels.value
.
(N/A)
principal.labels.key
Set to "Gateway" when
gateway
is mapped to
principal.labels.value
.
(N/A)
target.labels.key
Set to "Gateway" when
gateway
is mapped to
target.labels.value
.
(N/A)
principal.labels.key
Set to "state" when
status
is mapped to
principal.labels.value
.
(N/A)
target.labels.key
Set to "Gateway Status" when
status
is mapped to
target.labels.value
.
(N/A)
additional.fields.key
Set to "signature_name", "signature_cat", "signature_id", or "reputation" when the corresponding values are mapped from the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
