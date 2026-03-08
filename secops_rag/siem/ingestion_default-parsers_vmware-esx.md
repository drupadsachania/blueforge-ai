# Collect VMware ESXi logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-esx/  
**Scraped:** 2026-03-05T09:29:59.347037Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware ESXi logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from VMware ESXi syslog and JSON formatted logs. It normalizes the variety of ESXi log formats into a common structure, then populates UDM fields based on extracted values, including handling specific cases for different ESXi services like
crond
,
named
, and
sshd
using include files.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have privileged access to VMWare ESX.
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
Access the machine where Bindplane Agent is installed.
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
        namespace: 
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
Allow syslog ESXi firewall rule
Go to
Networking
>
Firewall rules
.
Find
syslog
in the
Name column
.
Click
Edit settings
.
Update the
tcp
or
udp
port you configured in Bindplane.
Click
Save
.
Keep the syslog line selected.
Select
Actions
>
Enable
.
Export Syslog from VMware ESXi using vSphere Client
Sign in to your ESXi host using vSphere Client.
Go to
Manage
>
System
>
Advanced Settings
.
Find the
Syslog.global.logHost
key in the list.
Select the key and click
Edit option
.
Enter
<protocol>://<destination_IP>:<port>
Replace
<protocol>
with
tcp
(if you configured Bindplane Agent to use UDP, then type
udp
).
Replace
<destination_IP>
with the IP address of your Bindplane Agent.
Replace
<port>
with the port previously setup in Bindplane Agent.
Click
Save
.
Optional: Export Syslog from VMware ESXi using SSH
Connect to your ESXi host using SSH.
Use the command
esxcli system syslog config set --loghost=<protocol>://<destination_IP>:<port>
.
Replace
<protocol>
with
tcp
(if you configured Bindplane Agent to use UDP, then type
udp
).
Replace
<destination_IP>
with the IP address of your Bindplane Agent.
Replace
<port>
with the port previously set up in Bindplane.
Restart the syslog service by entering the command
/etc/init.d/syslog restart
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
@fields.alias
event.idm.read_only_udm.principal.cloud.project.alias
Directly mapped from the JSON log's
@fields.alias
field.
@fields.company_name
event.idm.read_only_udm.principal.user.company_name
Directly mapped from the JSON log's
@fields.company_name
field.
@fields.facility
event.idm.read_only_udm.principal.resource.type
Directly mapped from the JSON log's
@fields.facility
field.
@fields.host
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the JSON log's
@fields.host
field.
@fields.privatecloud_id
event.idm.read_only_udm.principal.cloud.project.id
Directly mapped from the JSON log's
@fields.privatecloud_id
field.
@fields.privatecloud_name
event.idm.read_only_udm.principal.cloud.project.name
Directly mapped from the JSON log's
@fields.privatecloud_name
field.
@fields.procid
event.idm.read_only_udm.principal.process.pid
Directly mapped from the JSON log's
@fields.procid
field.
@fields.region_id
event.idm.read_only_udm.principal.location.country_or_region
Directly mapped from the JSON log's
@fields.region_id
field.
@fields.severity
event.idm.read_only_udm.security_result.severity
Mapped from the JSON log's
@fields.severity
field. If the value is "info" or similar, it's mapped to "INFORMATIONAL".
@timestamp
event.idm.read_only_udm.metadata.event_timestamp
Parsed and converted to a timestamp object from the log's
@timestamp
field using the
date
filter.
adapter
event.idm.read_only_udm.target.resource.name
Directly mapped from the raw log's
adapter
field.
action
event.idm.read_only_udm.security_result.action
Directly mapped from the raw log's
action
field.  Values like "ALLOW" and "BLOCK" are used.
action
event.idm.read_only_udm.security_result.action_details
Directly mapped from the raw log's
action
field. Values like "Redirect" are used.
administrative_domain
event.idm.read_only_udm.principal.administrative_domain
Directly mapped from the raw log's
administrative_domain
field.
agent.hostname
event.idm.read_only_udm.intermediary.hostname
Directly mapped from the JSON log's
agent.hostname
field.
agent.id
event.idm.read_only_udm.intermediary.asset.id
Directly mapped from the JSON log's
agent.id
field.
agent.name
event.idm.read_only_udm.intermediary.asset.name
Directly mapped from the JSON log's
agent.name
field.
agent.type
event.idm.read_only_udm.intermediary.asset.type
Directly mapped from the JSON log's
agent.type
field.
agent.version
event.idm.read_only_udm.intermediary.asset.version
Directly mapped from the JSON log's
agent.version
field.
app_name
event.idm.read_only_udm.principal.application
Directly mapped from the raw log's
app_name
field.
app_protocol
event.idm.read_only_udm.network.application_protocol
Directly mapped from the raw log's
app_protocol
field. If the value matches "http" (case-insensitive), it's mapped to "HTTP".
application
event.idm.read_only_udm.principal.application
Directly mapped from the JSON log's
program
field.
cmd
event.idm.read_only_udm.target.process.command_line
Directly mapped from the raw log's
cmd
field.
collection_time
event.idm.read_only_udm.metadata.event_timestamp
The nanoseconds from the
collection_time
field are added to the seconds from the
collection_time
field to create the
event_timestamp
.
data
event.idm.read_only_udm.metadata.description
The raw log message is parsed and relevant parts are extracted to populate the description field.
descrip
event.idm.read_only_udm.metadata.description
Directly mapped from the raw log's
descrip
field.
dns.answers.data
event.idm.read_only_udm.network.dns.answers.data
Directly mapped from the JSON log's
dns.answers.data
field.
dns.answers.ttl
event.idm.read_only_udm.network.dns.answers.ttl
Directly mapped from the JSON log's
dns.answers.ttl
field.
dns.answers.type
event.idm.read_only_udm.network.dns.answers.type
Directly mapped from the JSON log's
dns.answers.type
field.
dns.questions.name
event.idm.read_only_udm.network.dns.questions.name
Directly mapped from the JSON log's
dns.questions.name
field.
dns.questions.type
event.idm.read_only_udm.network.dns.questions.type
Directly mapped from the JSON log's
dns.questions.type
field.
dns.response
event.idm.read_only_udm.network.dns.response
Directly mapped from the JSON log's
dns.response
field.
ecs.version
event.idm.read_only_udm.metadata.product_version
Directly mapped from the JSON log's
ecs.version
field.
event_message
event.idm.read_only_udm.metadata.description
Directly mapped from the JSON log's
event_message
field.
event_metadata
event.idm.read_only_udm.principal.process.product_specific_process_id
The
event_metadata
field is parsed to extract the
opID
value, which is then prepended with "opID:" and mapped to the UDM.
event_type
event.idm.read_only_udm.metadata.event_type
Directly mapped from the JSON log's
event_type
field.
filepath
event.idm.read_only_udm.target.file.full_path
Directly mapped from the raw log's
filepath
field.
fields.company_name
event.idm.read_only_udm.principal.user.company_name
Directly mapped from the JSON log's
fields.company_name
field.
fields.facility
event.idm.read_only_udm.principal.resource.type
Directly mapped from the JSON log's
fields.facility
field.
fields.host
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the JSON log's
fields.host
field.
fields.privatecloud_id
event.idm.read_only_udm.principal.cloud.project.id
Directly mapped from the JSON log's
fields.privatecloud_id
field.
fields.privatecloud_name
event.idm.read_only_udm.principal.cloud.project.name
Directly mapped from the JSON log's
fields.privatecloud_name
field.
fields.procid
event.idm.read_only_udm.principal.process.pid
Directly mapped from the JSON log's
fields.procid
field.
fields.region_id
event.idm.read_only_udm.principal.location.country_or_region
Directly mapped from the JSON log's
fields.region_id
field.
fields.severity
event.idm.read_only_udm.security_result.severity
Mapped from the JSON log's
fields.severity
field. If the value is "info" or similar, it's mapped to "INFORMATIONAL".
host.architecture
event.idm.read_only_udm.principal.asset.architecture
Directly mapped from the JSON log's
host.architecture
field.
host.containerized
event.idm.read_only_udm.principal.asset.containerized
Directly mapped from the JSON log's
host.containerized
field.
host.hostname
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the JSON log's
host.hostname
field.
host.id
event.idm.read_only_udm.principal.asset.id
Directly mapped from the JSON log's
host.id
field.
host.ip
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the JSON log's
host.ip
field.
host.mac
event.idm.read_only_udm.principal.mac
,
event.idm.read_only_udm.principal.asset.mac
Directly mapped from the JSON log's
host.mac
field.
host.name
event.idm.read_only_udm.principal.asset.name
Directly mapped from the JSON log's
host.name
field.
host.os.codename
event.idm.read_only_udm.principal.asset.os.codename
Directly mapped from the JSON log's
host.os.codename
field.
host.os.family
event.idm.read_only_udm.principal.asset.os.family
Directly mapped from the JSON log's
host.os.family
field.
host.os.kernel
event.idm.read_only_udm.principal.asset.os.kernel
Directly mapped from the JSON log's
host.os.kernel
field.
host.os.name
event.idm.read_only_udm.principal.asset.os.name
Directly mapped from the JSON log's
host.os.name
field.
host.os.platform
event.idm.read_only_udm.principal.asset.os.platform
Directly mapped from the JSON log's
host.os.platform
field.
host.os.version
event.idm.read_only_udm.principal.asset.os.version
Directly mapped from the JSON log's
host.os.version
field.
iporhost
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the raw log's
iporhost
field.
iporhost
event.idm.read_only_udm.principal.ip
Directly mapped from the raw log's
iporhost
field if it's an IP address.
iporhost1
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the raw log's
iporhost1
field.
kv_data1
event.idm.read_only_udm.principal.process.product_specific_process_id
The
kv_data1
field is parsed to extract the
opID
or
sub
value, which is then prepended with "opID:" or "sub:" respectively and mapped to the UDM.
kv_msg
event.idm.read_only_udm.additional.fields
The
kv_msg
field is parsed as key-value pairs and added to the
additional_fields
array in the UDM.
kv_msg1
event.idm.read_only_udm.additional.fields
The
kv_msg1
field is parsed as key-value pairs and added to the
additional_fields
array in the UDM.
lbdn
event.idm.read_only_udm.target.hostname
Directly mapped from the raw log's
lbdn
field.
log.source.address
event.idm.read_only_udm.observer.hostname
Directly mapped from the JSON log's
log.source.address
field, taking only the hostname part.
log_event.original
event.idm.read_only_udm.metadata.description
Directly mapped from the JSON log's
event.original
field.
log_level
event.idm.read_only_udm.security_result.severity_details
Directly mapped from the JSON log's
log_level
field.
logstash.collect.host
event.idm.read_only_udm.observer.hostname
Directly mapped from the JSON log's
logstash.collect.host
field.
logstash.collect.timestamp
event.idm.read_only_udm.metadata.ingested_timestamp
Parsed and converted to a timestamp object from the log's
logstash.collect.timestamp
field using the
date
filter.
logstash.ingest.host
event.idm.read_only_udm.intermediary.hostname
Directly mapped from the JSON log's
logstash.ingest.host
field.
logstash.ingest.timestamp
event.idm.read_only_udm.metadata.ingested_timestamp
Parsed and converted to a timestamp object from the log's
logstash.ingest.timestamp
field using the
date
filter.
logstash.process.host
event.idm.read_only_udm.intermediary.hostname
Directly mapped from the JSON log's
logstash.process.host
field.
logstash.process.timestamp
event.idm.read_only_udm.metadata.ingested_timestamp
Parsed and converted to a timestamp object from the log's
logstash.process.timestamp
field using the
date
filter.
log_type
event.idm.read_only_udm.metadata.log_type
Directly mapped from the raw log's
log_type
field.
message
event.idm.read_only_udm.metadata.description
Directly mapped from the JSON log's
message
field.
message_to_process
event.idm.read_only_udm.metadata.description
Directly mapped from the raw log's
message_to_process
field.
metadata.event_type
event.idm.read_only_udm.metadata.event_type
Set to "GENERIC_EVENT" initially, then potentially overwritten based on the parsed
service
or other log content.  Can be values like
PROCESS_LAUNCH
,
NETWORK_CONNECTION
,
USER_LOGIN
, etc.
metadata.product_event_type
event.idm.read_only_udm.metadata.product_event_type
Directly mapped from the raw log's
process_id
or
prod_event_type
field.
metadata.product_log_id
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the raw log's
event_id
field.
metadata.product_name
event.idm.read_only_udm.metadata.product_name
Set to "ESX".
metadata.product_version
event.idm.read_only_udm.metadata.product_version
Directly mapped from the JSON log's
version
field.
metadata.vendor_name
event.idm.read_only_udm.metadata.vendor_name
Set to "VMWARE".
msg
event.idm.read_only_udm.metadata.description
Directly mapped from the raw log's
msg
field.
network.application_protocol
event.idm.read_only_udm.network.application_protocol
Set to "DNS" if the
service
is "named", "HTTPS" if the port is 443, or "HTTP" if the
app_protocol
matches "http".
network.direction
event.idm.read_only_udm.network.direction
Determined from keywords in the raw log, such as "IN", "OUT", "->".  Can be
INBOUND
or
OUTBOUND
.
network.http.method
event.idm.read_only_udm.network.http.method
Directly mapped from the raw log's
method
field.
network.http.parsed_user_agent
event.idm.read_only_udm.network.http.parsed_user_agent
Parsed from the
useragent
field using the
convert
filter.
network.http.referral_url
event.idm.read_only_udm.network.http.referral_url
Directly mapped from the raw log's
prin_url
field.
network.http.response_code
event.idm.read_only_udm.network.http.response_code
Directly mapped from the raw log's
status_code
field and converted to an integer.
network.http.user_agent
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the raw log's
useragent
field.
network.ip_protocol
event.idm.read_only_udm.network.ip_protocol
Determined from keywords in the raw log, such as "TCP", "UDP".
network.received_bytes
event.idm.read_only_udm.network.received_bytes
Directly mapped from the raw log's
rec_bytes
field and converted to an unsigned integer.
network.sent_bytes
event.idm.read_only_udm.network.sent_bytes
Extracted from the raw log's
message_to_process
field.
network.session_id
event.idm.read_only_udm.network.session_id
Directly mapped from the raw log's
session
field.
pid
event.idm.read_only_udm.target.process.parent_process.pid
Directly mapped from the raw log's
pid
field.
pid
event.idm.read_only_udm.principal.process.pid
Directly mapped from the JSON log's
pid
field.
pid
event.idm.read_only_udm.target.process.pid
Directly mapped from the raw log's
pid
field.
port
event.idm.read_only_udm.target.port
Directly mapped from the JSON log's
port
field.
principal.application
event.idm.read_only_udm.principal.application
Directly mapped from the raw log's
app_name
or
service
field.
principal.asset.hostname
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the raw log's
principal_hostname
or
iporhost
field.
principal.asset.ip
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the raw log's
syslog_ip
field.
principal.hostname
event.idm.read_only_udm.principal.hostname
Directly mapped from the raw log's
principal_hostname
or
iporhost
field.
principal.ip
event.idm.read_only_udm.principal.ip
Directly mapped from the raw log's
iporhost
or
syslog_ip
field.
principal.port
event.idm.read_only_udm.principal.port
Directly mapped from the raw log's
srcport
field.
principal.process.command_line
event.idm.read_only_udm.principal.process.command_line
Directly mapped from the raw log's
cmd
field.
principal.process.parent_process.pid
event.idm.read_only_udm.principal.process.parent_process.pid
Directly mapped from the raw log's
parent_pid
field.
principal.process.pid
event.idm.read_only_udm.principal.process.pid
Directly mapped from the raw log's
process_id
field.
principal.process.product_specific_process_id
event.idm.read_only_udm.principal.process.product_specific_process_id
Extracted from the raw log's
message_to_process
field, usually prefixed with "opID:".
principal.url
event.idm.read_only_udm.principal.url
Directly mapped from the raw log's
prin_url
field.
principal.user.company_name
event.idm.read_only_udm.principal.user.company_name
Directly mapped from the JSON log's
fields.company_name
field.
principal.user.userid
event.idm.read_only_udm.principal.user.userid
Directly mapped from the raw log's
USER
field.
priority
event.idm.read_only_udm.metadata.product_event_type
Directly mapped from the raw log's
priority
field.
program
event.idm.read_only_udm.principal.application
Directly mapped from the JSON log's
program
field.
qname
event.idm.read_only_udm.network.dns.questions.name
Directly mapped from the raw log's
qname
field.
response_data
event.idm.read_only_udm.network.dns.answers.data
Directly mapped from the raw log's
response_data
field.
response_rtype
event.idm.read_only_udm.network.dns.answers.type
Directly mapped from the raw log's
response_rtype
field. The numeric DNS record type is extracted.
response_ttl
event.idm.read_only_udm.network.dns.answers.ttl
Directly mapped from the raw log's
response_ttl
field.
rtype
event.idm.read_only_udm.network.dns.questions.type
Directly mapped from the raw log's
rtype
field. The numeric DNS record type is extracted.
security_result.action
event.idm.read_only_udm.security_result.action
Determined from keywords or status in the raw log. Can be
ALLOW
or
BLOCK
.
security_result.action_details
event.idm.read_only_udm.security_result.action_details
Extracted from the raw log message, providing more context about the action taken.
security_result.category
event.idm.read_only_udm.security_result.category
Set to
POLICY_VIOLATION
if the log indicates a firewall rule match.
security_result.description
event.idm.read_only_udm.security_result.description
Extracted from the raw log message, providing more context about the security result.
security_result.rule_id
event.idm.read_only_udm.security_result.rule_id
Directly mapped from the raw log's
rule_id
field.
security_result.severity
event.idm.read_only_udm.security_result.severity
Determined from keywords in the raw log, such as "info", "warning", "error". Can be
INFORMATIONAL
,
LOW
,
MEDIUM
, or
HIGH
.
security_result.severity_details
event.idm.read_only_udm.security_result.severity_details
Directly mapped from the raw log's
severity
or
log.syslog.severity.name
field.
security_result.summary
event.idm.read_only_udm.security_result.summary
Extracted from the raw log message, providing a concise summary of the security result.
service
event.idm.read_only_udm.principal.application
Directly mapped from the raw log's
service
field.
source
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the raw log's
source
field.
src.file.full_path
event.idm.read_only_udm.src.file.full_path
Extracted from the raw log message.
src.hostname
event.idm.read_only_udm.src.hostname
Directly mapped from the raw log's
src.hostname
field.
src_ip
event.idm.read_only_udm.principal.ip
Directly mapped from the raw log's
src_ip
field.
src_mac_address
event.idm.read_only_udm.principal.mac
Directly mapped from the raw log's
src_mac_address
field.
srcport
event.idm.read_only_udm.principal.port
Directly mapped from the raw log's
srcport
field.
srcip
event.idm.read_only_udm.principal.ip
Directly mapped from the raw log's
srcip
field.
subtype
event.idm.read_only_udm.metadata.event_type
Directly mapped from the raw log's
subtype
field.
tags
event.idm.read_only_udm.metadata.tags
Directly mapped from the JSON log's
tags
field.
target.application
event.idm.read_only_udm.target.application
Directly mapped from the raw log's
target_application
field.
target.file.full_path
event.idm.read_only_udm.target.file.full_path
Extracted from the raw log message.
target.hostname
event.idm.read_only_udm.target.hostname
,
event.idm.read_only_udm.target.asset.hostname
Directly mapped from the raw log's
target_hostname
or
iporhost
field.
target.ip
event.idm.read_only_udm.target.ip
Directly mapped from the raw log's
target_ip
field.
target.mac
event.idm.read_only_udm.target.mac
Directly mapped from the raw log's
target_mac_address
field.
target.port
event.idm.read_only_udm.target.port
Directly mapped from the raw log's
target_port
field.
target.process.command_line
event.idm.read_only_udm.target.process.command_line
Directly mapped from the raw log's
cmd
field.
target.process.parent_process.pid
event.idm.read_only_udm.target.process.parent_process.pid
Directly mapped from the raw log's
parent_pid
field.
target.process.pid
event.idm.read_only_udm.target.process.pid
Directly mapped from the raw log's
pid
field.
target.process.product_specific_process_id
event.idm.read_only_udm.target.process.product_specific_process_id
Extracted from the raw log's
message_to_process
field, usually prefixed with "opID:".
target.resource.name
event.idm.read_only_udm.target.resource.name
Directly mapped from the raw log's
adapter
field.
target.resource.resource_type
event.idm.read_only_udm.target.resource.resource_type
Set to
VIRTUAL_MACHINE
if the log indicates a VM operation.
target.resource.type
event.idm.read_only_udm.target.resource.type
Set to
SETTING
if the log indicates a setting modification.
target.user.userid
event.idm.read_only_udm.target.user.userid
Directly mapped from the raw log's
target_username
or
user1
field.
timestamp
event.timestamp
Parsed and converted to a timestamp object from the log's
timestamp
or
data
field using the
date
filter.
type
event.idm.read_only_udm.additional.fields
The log's
type
field is added to the
additional_fields
array in the UDM with the key "LogType".
user1
event.idm.read_only_udm.target.user.userid
Directly mapped from the raw log's
user1
field.
useragent
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the raw log's
useragent
field.
vmw_cluster
event.idm.read_only_udm.target.resource.name
Directly mapped from the raw log's
vmw_cluster
field.
vmw_datacenter
event.idm.read_only_udm.target.resource.name
Directly mapped from the raw log's
vmw_datacenter
field.
vmw_host
event.idm.read_only_udm.target.ip
Directly mapped from the raw log's
vmw_host
field.
vmw_object_id
event.idm.read_only_udm.target.resource.id
Directly mapped from the raw log's
vmw_object_id
field.
vmw_product
event.idm.read_only_udm.target.application
Directly mapped from the raw log's
vmw_product
field.
vmw_vcenter
event.idm.read_only_udm.target.cloud.availability_zone
Directly mapped from the raw log's
vmw_vcenter
field.
vmw_vcenter_id
event.idm.read_only_udm.target.cloud.availability_zone.id
Directly mapped from the raw log's
vmw_vcenter_id
field.
vmw_vr_ops_appname
event.idm.read_only_udm.target.application
Directly mapped from the raw log's
vmw_vr_ops_appname
field.
vmw_vr_ops_clustername
event.idm.read_only_udm.target.resource.name
Directly mapped from the raw log's
vmw_vr_ops_clustername
field.
vmw_vr_ops_clusterrole
event.idm.read_only_udm.target.resource.type
Directly mapped from the raw log's
vmw_vr_ops_clusterrole
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
