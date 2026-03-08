# Collect Check Point firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-firewall/  
**Scraped:** 2026-03-05T09:21:01.219679Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Check Point firewall logs
Supported in:
Google secops
SIEM
This parser extracts Check Point firewall logs. It handles both CEF and non-CEF formatted messages, including syslog, key-value pairs, and JSON. It normalizes fields, maps them to the UDM, and performs specific logic for login/logout, network connections, and security events. It enriches the data with contextual information like geolocation and threat intelligence.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to a Check Point Firewall.
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
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane is installed.
Edit the
config.yaml
file as follows:
receivers:
    udplog:
        # Replace the below port <54525> and IP <0.0.0.0> with your specific values
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
        namespace: Checkpoint_Firewall
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - udplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes:
sudo
systemctl
restart
bindplane
Configure Syslog Export in a Check Point Firewall
Sign in to the Check Point firewall UI using a privileged account.
Go to
Logs & Monitoring
>
Log Servers
.
Navigate to
Syslog Servers
.
Click
Configure
, and set the following values:
Protocol
: select
UDP
to send security logs and/or system logs.
Name
: provide a unique name (for example, Bindplane_Server).
IP Address
: provide your syslog server IP address (Bindplane IP).
Port
: provide your syslog server Port (Bindplane Port).
Select
Enable log server
.
Select logs to forward:
Both system and security logs
.
Click
Apply
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
Action
event.idm.read_only_udm.security_result.action_details
Directly mapped from the
Action
field.
Activity
event.idm.read_only_udm.security_result.summary
Directly mapped from the
Activity
field.
additional_info
event.idm.read_only_udm.security_result.description
Directly mapped from the
additional_info
field.
administrator
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
administrator
field. Key is "administrator".
aggregated_log_count
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
aggregated_log_count
field. Key is "aggregated_log_count".
appi_name
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
appi_name
field. Key is "appi_name".
app_category
event.idm.read_only_udm.security_result.category_details
Directly mapped from the
app_category
field.
app_properties
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
app_properties
field. Key is "app_properties".
app_risk
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
app_risk
field. Key is "app_risk".
app_session_id
event.idm.read_only_udm.network.session_id
Directly mapped from the
app_session_id
field, converted to a string.
attack
event.idm.read_only_udm.security_result.summary
Directly mapped from the
attack
field when
Info
is present.
attack
event.idm.read_only_udm.security_result.threat_name
Directly mapped from the
attack
field when
Info
is present.
attack_info
event.idm.read_only_udm.security_result.description
Directly mapped from the
attack_info
field.
auth_status
event.idm.read_only_udm.security_result.summary
Directly mapped from the
auth_status
field.
browse_time
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
browse_time
field. Key is "browse_time".
bytes
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
bytes
field. Key is "bytes".
bytes
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
bytes
field. Key is "bytes".
calc_service
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
calc_service
field. Key is "calc_service".
category
event.idm.read_only_udm.security_result.category_details
Directly mapped from the
category
field.
client_version
event.idm.read_only_udm.intermediary.platform_version
Directly mapped from the
client_version
field.
conn_direction
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
conn_direction
field. Key is "conn_direction".
conn_direction
event.idm.read_only_udm.network.direction
If
conn_direction
is "Incoming", maps to "INBOUND". Otherwise, maps to "OUTBOUND".
connection_count
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
connection_count
field. Key is "connection_count".
contract_name
event.idm.read_only_udm.security_result.description
Directly mapped from the
contract_name
field.
cs2
event.idm.read_only_udm.security_result.rule_name
Directly mapped from the
cs2
field.
date_time
event.idm.read_only_udm.metadata.event_timestamp
Parsed and converted to a timestamp using various date formats.
dedup_time
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
dedup_time
field. Key is "dedup_time".
desc
event.idm.read_only_udm.security_result.summary
Directly mapped from the
desc
field.
description
event.idm.read_only_udm.security_result.description
Directly mapped from the
description
field.
description_url
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
description_url
field. Key is "description_url".
destinationAddress
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
destinationAddress
field.
destinationPort
event.idm.read_only_udm.target.port
Directly mapped from the
destinationPort
field, converted to an integer.
destinationTranslatedAddress
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
destinationTranslatedAddress
field.
destinationTranslatedAddress
event.idm.read_only_udm.target.nat_ip
Directly mapped from the
destinationTranslatedAddress
field.
destinationTranslatedPort
event.idm.read_only_udm.target.port
Directly mapped from the
destinationTranslatedPort
field, converted to an integer.
destinationTranslatedPort
event.idm.read_only_udm.target.nat_port
Directly mapped from the
destinationTranslatedPort
field, converted to an integer.
deviceCustomString2
event.idm.read_only_udm.security_result.rule_name
Directly mapped from the
deviceCustomString2
field.
deviceDirection
event.idm.read_only_udm.network.direction
If
deviceDirection
is 0, maps to "OUTBOUND". If 1, maps to "INBOUND".
domain
event.idm.read_only_udm.principal.administrative_domain
Directly mapped from the
domain
field.
domain_name
event.idm.read_only_udm.principal.administrative_domain
Directly mapped from the
domain_name
field.
drop_reason
event.idm.read_only_udm.security_result.summary
Directly mapped from the
drop_reason
field.
ds
event.idm.read_only_udm.metadata.event_timestamp
Used with
ts
and
tz
to construct the event timestamp.
dst
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
dst
field.
dst_country
event.idm.read_only_udm.target.location.country_or_region
Directly mapped from the
dst_country
field.
dst_ip
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
dst_ip
field.
dpt
event.idm.read_only_udm.target.port
Directly mapped from the
dpt
field, converted to an integer.
duration
event.idm.read_only_udm.network.session_duration.seconds
Directly mapped from the
duration
field, converted to an integer, if greater than 0.
duser
event.idm.read_only_udm.target.user.email_addresses
,
event.idm.read_only_udm.target.user.user_display_name
Directly mapped from the
duser
field if it matches an email address format.
environment_id
event.idm.read_only_udm.target.resource.product_object_id
Directly mapped from the
environment_id
field.
event_type
event.idm.read_only_udm.metadata.event_type
Determined by logic based on the presence of certain fields and values. Defaults to
GENERIC_EVENT
if no specific event type is identified. Can be
NETWORK_CONNECTION
,
USER_LOGIN
,
USER_CHANGE_PASSWORD
,
USER_LOGOUT
,
NETWORK_HTTP
, or
STATUS_UPDATE
.
fieldschanges
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
fieldschanges
field. Key is "fieldschanges".
flags
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
flags
field. Key is "flags".
flexString2
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
flexString2
field. Key is the value of
flexString2Label
.
from_user
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
from_user
field.
fservice
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
fservice
field. Key is "fservice".
fw_subproduct
event.idm.read_only_udm.metadata.product_name
Directly mapped from the
fw_subproduct
field when
product
is empty.
geoip_dst.country_name
event.idm.read_only_udm.target.location.country_or_region
Directly mapped from the
geoip_dst.country_name
field.
hll_key
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
hll_key
field. Key is "hll_key".
hostname
event.idm.read_only_udm.target.hostname
,
event.idm.read_only_udm.target.asset.hostname
,
event.idm.read_only_udm.intermediary.hostname
Directly mapped from the
hostname
field when
inter_host
is empty.
http_host
event.idm.read_only_udm.target.resource.attribute.labels[].value
Directly mapped from the
http_host
field. Key is "http_host".
id
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
_id
field.
identity_src
event.idm.read_only_udm.target.application
Directly mapped from the
identity_src
field.
identity_type
event.idm.read_only_udm.extensions.auth.type
If
identity_type
is "user", maps to "VPN". Otherwise, maps to "MACHINE".
if_direction
event.idm.read_only_udm.network.direction
Directly mapped from the
if_direction
field, converted to uppercase.
ifdir
event.idm.read_only_udm.network.direction
Directly mapped from the
ifdir
field, converted to uppercase.
ifname
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
ifname
field. Key is "ifname".
IKE
event.idm.read_only_udm.metadata.description
Directly mapped from the
IKE
field.
inzone
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
inzone
field. Key is "inzone".
industry_reference
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
industry_reference
field. Key is "industry_reference".
instance_id
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
instance_id
field.
inter_host
event.idm.read_only_udm.intermediary.hostname
Directly mapped from the
inter_host
field.
ip_proto
event.idm.read_only_udm.network.ip_protocol
Determined based on the
proto
field or
service
field. Can be TCP, UDP, ICMP, IP6IN4, or GRE.
ipv6_dst
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
ipv6_dst
field.
ipv6_src
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
ipv6_src
field.
layer_name
event.idm.read_only_udm.security_result.rule_set_display_name
,
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
layer_name
field. Key is "layer_name".
layer_uuid
event.idm.read_only_udm.security_result.rule_set
,
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
layer_uuid
field after removing curly braces. Key is "layer_uuid".
layer_uuid_rule_uuid
event.idm.read_only_udm.security_result.rule_id
Directly mapped from the
layer_uuid_rule_uuid
field after removing brackets and quotes.
log_id
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
log_id
field.
log_type
event.idm.read_only_udm.metadata.log_type
Directly mapped from the
log_type
field. Hardcoded to "CHECKPOINT_FIREWALL".
loguid
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
loguid
field after removing curly braces.
logic_changes
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
logic_changes
field. Key is "logic_changes".
localhost
event.idm.read_only_udm.target.hostname
,
event.idm.read_only_udm.target.asset.hostname
Directly mapped from the
localhost
field.
dst_ip
is set to "127.0.0.1".
malware_action
event.idm.read_only_udm.security_result.detection_fields[].value
,
event.idm.read_only_udm.security_result.about.resource.attribute.labels[].value
Directly mapped from the
malware_action
field. Key is "malware_action".
malware_family
event.idm.read_only_udm.security_result.detection_fields[].value
,
event.idm.read_only_udm.security_result.about.resource.attribute.labels[].value
Directly mapped from the
malware_family
field. Key is "malware_family".
malware_rule_id
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
malware_rule_id
field after removing curly braces. Key is "Malware Rule ID".
malware_rule_name
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
malware_rule_name
field. Key is "Malware Rule Name".
match_id
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
match_id
field. Key is "match_id".
matched_category
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
matched_category
field. Key is "matched_category".
message_info
event.idm.read_only_udm.metadata.description
Directly mapped from the
message_info
field.
method
event.idm.read_only_udm.network.http.method
Directly mapped from the
method
field.
mitre_execution
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
mitre_execution
field. Key is "mitre_execution".
mitre_initial_access
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
mitre_initial_access
field. Key is "mitre_initial_access".
nat_rulenum
event.idm.read_only_udm.security_result.rule_id
Directly mapped from the
nat_rulenum
field, converted to a string.
objecttype
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
objecttype
field. Key is "objecttype".
operation
event.idm.read_only_udm.security_result.summary
Directly mapped from the
operation
field.
operation
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
operation
field. Key is "operation".
orig
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
orig
field.
origin
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
,
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
,
event.idm.read_only_udm.intermediary.ip
Directly mapped from the
origin
field.
origin_sic_name
event.idm.read_only_udm.intermediary.asset_id
,
event.idm.read_only_udm.intermediary.labels[].value
Directly mapped from the
origin_sic_name
field. Key is "Machine SIC". Asset ID is prefixed with "asset:".
originsicname
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
originsicname
field. Key is "originsicname".
originsicname
event.idm.read_only_udm.intermediary.asset_id
,
event.idm.read_only_udm.intermediary.labels[].value
Directly mapped from the
originsicname
field. Key is "Machine SIC". Asset ID is prefixed with "asset:".
os_name
event.idm.read_only_udm.principal.asset.platform_software.platform
If
os_name
contains "Win", maps to "WINDOWS". If it contains "MAC" or "IOS", maps to "MAC". If it contains "LINUX", maps to "LINUX".
os_version
event.idm.read_only_udm.principal.asset.platform_software.platform_patch_level
Directly mapped from the
os_version
field.
outzone
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
outzone
field. Key is "outzone".
packets
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
packets
field. Key is "packets".
packet_capture_name
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
packet_capture_name
field. Key is "packet_capture_name".
packet_capture_time
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
packet_capture_time
field. Key is "packet_capture_time".
packet_capture_unique_id
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
packet_capture_unique_id
field. Key is "packet_capture_unique_id".
parent_rule
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
parent_rule
field. Key is "parent_rule".
performance_impact
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
performance_impact
field. Key is "performance_impact".
policy_name
event.idm.read_only_udm.security_result.detection_fields[].value
Extracted from the
__policy_id_tag
field using grok and mapped. Key is "Policy Name".
policy_time
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
policy_time
field. Key is "policy_time".
portal_message
event.idm.read_only_udm.security_result.description
Directly mapped from the
portal_message
field.
principal_hostname
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
principal_hostname
field if it's a valid IP address.
principal_hostname
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
principal_hostname
field if it's not a valid IP address and not "Checkpoint".
prod_family_label
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
ProductFamily
field. Key is "ProductFamily".
product
event.idm.read_only_udm.metadata.product_name
Directly mapped from the
product
field.
product_family
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
product_family
field. Key is "product_family".
product_family
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
product_family
field. Key is "product_family".
ProductName
event.idm.read_only_udm.metadata.product_name
Directly mapped from the
ProductName
field when
product
is empty.
product_name
event.idm.read_only_udm.metadata.product_name
Directly mapped from the
product_name
field.
profile
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
profile
field. Key is "profile".
protocol
event.idm.read_only_udm.network.application_protocol
Directly mapped from the
protocol
field if it's "HTTP".
proxy_src_ip
event.idm.read_only_udm.principal.nat_ip
Directly mapped from the
proxy_src_ip
field.
reason
event.idm.read_only_udm.security_result.summary
Directly mapped from the
reason
field.
received_bytes
event.idm.read_only_udm.network.received_bytes
Directly mapped from the
received_bytes
field, converted to an unsigned integer.
Reference
event.idm.read_only_udm.security_result.about.resource.attribute.labels[].value
,
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
Reference
field. Key is "Reference". Used to construct
_vuln.name
with
attack
.
reject_id_kid
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
reject_id_kid
field. Key is "reject_id_kid".
resource
event.idm.read_only_udm.target.url
Parsed as JSON and mapped to the target URL. If parsing fails, it's directly mapped.
resource
event.idm.read_only_udm.additional.fields[].value.list_value.values[].string_value
Parsed as JSON and each value in the
resource
array is added to the list. Key is "Resource".
result
event.idm.read_only_udm.metadata.event_timestamp
Parsed with
date_time
to create the event timestamp.
rt
event.idm.read_only_udm.metadata.event_timestamp
Parsed as milliseconds since epoch and converted to a timestamp.
rule
event.idm.read_only_udm.security_result.rule_name
Directly mapped from the
rule
field.
rule_action
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
rule_action
field. Key is "rule_action".
rule_name
event.idm.read_only_udm.security_result.rule_name
Directly mapped from the
rule_name
field.
rule_uid
event.idm.read_only_udm.security_result.rule_id
Directly mapped from the
rule_uid
field.
s_port
event.idm.read_only_udm.principal.port
Directly mapped from the
s_port
field, converted to an integer.
scheme
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
scheme
field. Key is "scheme".
security_inzone
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
security_inzone
field. Key is "security_inzone".
security_outzone
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
security_outzone
field. Key is "security_outzone".
security_result_action
event.idm.read_only_udm.security_result.action
Directly mapped from the
security_result_action
field.
sendtotrackerasadvancedauditlog
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
sendtotrackerasadvancedauditlog
field. Key is "sendtotrackerasadvancedauditlog".
sent_bytes
event.idm.read_only_udm.network.sent_bytes
Directly mapped from the
sent_bytes
field, converted to an unsigned integer.
sequencenum
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
sequencenum
field. Key is "sequencenum".
ser_agent_kid
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
ser_agent_kid
field. Key is "ser_agent_kid".
service
event.idm.read_only_udm.target.port
Directly mapped from the
service
field, converted to an integer.
service_id
event.idm.read_only_udm.network.application_protocol
Directly mapped from the
service_id
field if it's "dhcp", "dns", "http", "https", or "quic", converted to uppercase.
service_id
event.idm.read_only_udm.principal.application
Directly mapped from the
service_id
field if it's not one of the network application protocols.
service_id
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
service_id
field. Key is "service_id".
session_description
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
session_description
field. Key is "session_description".
session_id
event.idm.read_only_udm.network.session_id
Directly mapped from the
session_id
field after removing curly braces.
session_name
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
session_name
field. Key is "session_name".
session_uid
event.idm.read_only_udm.network.session_id
Directly mapped from the
session_uid
field after removing curly braces.
Severity
event.idm.read_only_udm.security_result.severity
Mapped to "LOW", "MEDIUM", "HIGH", or "CRITICAL" based on the value of
Severity
.
severity
event.idm.read_only_udm.security_result.severity
Mapped to "LOW", "MEDIUM", "HIGH", or "CRITICAL" based on the value of
severity
.
site
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the
site
field.
smartdefense_profile
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
smartdefense_profile
field. Key is "smartdefense_profile".
snid
event.idm.read_only_udm.network.session_id
Directly mapped from the
snid
field if it's not empty or "0".
sourceAddress
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
sourceAddress
field.
sourcePort
event.idm.read_only_udm.principal.port
Directly mapped from the
sourcePort
field, converted to an integer.
sourceTranslatedAddress
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
sourceTranslatedAddress
field.
sourceTranslatedAddress
event.idm.read_only_udm.principal.nat_ip
Directly mapped from the
sourceTranslatedAddress
field.
sourceTranslatedPort
event.idm.read_only_udm.principal.port
Directly mapped from the
sourceTranslatedPort
field, converted to an integer.
sourceTranslatedPort
event.idm.read_only_udm.principal.nat_port
Directly mapped from the
sourceTranslatedPort
field, converted to an integer.
sourceUserName
event.idm.read_only_udm.principal.user.userid
,
event.idm.read_only_udm.principal.user.first_name
,
event.idm.read_only_udm.principal.user.last_name
Parsed using grok to extract userid, first name, and last name.
spt
event.idm.read_only_udm.principal.port
Directly mapped from the
spt
field, converted to an integer.
src
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
src
field.
src_ip
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
src_ip
field.
src_localhost
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
src_localhost
field.
src_ip
is set to "127.0.0.1".
src_machine_name
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
src_machine_name
field. Key is "src_machine_name".
src_port
event.idm.read_only_udm.principal.port
Directly mapped from the
src_port
field, converted to an integer.
src_user
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
src_user
field.
src_user_dn
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
src_user_dn
field. Key is "src_user_dn".
src_user_name
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
src_user_name
field.
sub_policy_name
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
sub_policy_name
field. Key is "sub_policy_name".
sub_policy_uid
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
sub_policy_uid
field. Key is "sub_policy_uid".
subject
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
subject
field. Key is "subject".
subscription_stat_desc
event.idm.read_only_udm.security_result.summary
Directly mapped from the
subscription_stat_desc
field.
tags
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
tags
field. Key is "tags".
tar_user
event.idm.read_only_udm.target.user.userid
Directly mapped from the
tar_user
field.
target_port
event.idm.read_only_udm.target.port
Directly mapped from the
target_port
field.
tcp_flags
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
tcp_flags
field. Key is "tcp_flags".
tcp_packet_out_of_state
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
tcp_packet_out_of_state
field. Key is "tcp_packet_out_of_state".
time
event.idm.read_only_udm.metadata.event_timestamp
Parsed and converted to a timestamp using various date formats.
ts
event.idm.read_only_udm.metadata.event_timestamp
Parsed with
ds
and
tz
to create the event timestamp.
type
event.idm.read_only_udm.security_result.rule_type
Directly mapped from the
type
field.
tz
event.idm.read_only_udm.metadata.event_timestamp
Used with
ds
and
ts
to construct the event timestamp.
update_count
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
update_count
field. Key is "update_count".
URL
event.idm.read_only_udm.security_result.about.url
Directly mapped from the
URL
field.
user
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
user
field.
user_agent
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the
user_agent
field. Also parsed and mapped to
event.idm.read_only_udm.network.http.parsed_user_agent
.
userip
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
userip
field if it's a valid IP address.
UUid
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
UUid
field after removing curly braces.
version
event.idm.read_only_udm.metadata.product_version
Directly mapped from the
version
field.
web_client_type
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the
web_client_type
field.
xlatedport
event.idm.read_only_udm.target.nat_port
Directly mapped from the
xlatedport
field, converted to an integer.
xlatedst
event.idm.read_only_udm.target.nat_ip
Directly mapped from the
xlatedst
field.
xlatesport
event.idm.read_only_udm.principal.nat_port
Directly mapped from the
xlatesport
field, converted to an integer.
xlatesrc
event.idm.read_only_udm.principal.nat_ip
Directly mapped from the
xlatesrc
field.
event.idm.read_only_udm.metadata.vendor_name
Check Point
Hardcoded value.
event.idm.read_only_udm.metadata.log_type
CHECKPOINT_FIREWALL
Hardcoded value.
event.idm.read_only_udm.security_result.rule_type
Firewall Rule
Default value, unless overridden by specific logic.
has_principal
true
Set to true when principal IP or hostname is extracted.
has_target
true
Set to true when target IP or hostname is extracted.
Need more help?
Get answers from Community members and Google SecOps professionals.
