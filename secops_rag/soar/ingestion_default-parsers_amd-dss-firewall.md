# Collect AMD Pensando DSS firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/amd-dss-firewall/  
**Scraped:** 2026-03-05T09:49:42.532731Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AMD Pensando DSS firewall logs
Supported in:
Google secops
SIEM
This guide explains how you can ingest AMD Pensando DSS firewall logs to Google Security Operations using Bindplane. The parser first extracts fields from the syslog messages using grok patterns and CSV parsing. Then, it maps the extracted fields to the corresponding UDM (Unified Data Model) attributes, enriching the data with additional context and standardizing its format for security analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the AMD Pensando Policy and Services Manager (PSM) or Aruba CX 10000 switch management interface
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
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'AMD_DSS_FIREWALL'
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
<CUSTOMER_ID>
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
Configure Syslog forwarding on AMD Pensando DSS Firewall
The Aruba CX 10000 uses Distributed Services Switch (DSS) integration to offload 
firewall logs. Follow these steps to forward these logs to Bindplane.
Configure via AOS-CX CLI on Aruba CX 10000
Connect to the
Aruba CX 10000 switch
via SSH or console.
Enter configuration mode:
configure terminal
Configure remote syslog server with UDP (replace
<BINDPLANE_IP>
with your Bindplane agent IP address):
logging <BINDPLANE_IP> udp 514 severity info
Or for TCP:
logging <BINDPLANE_IP> tcp 514 severity info
Or for TLS (if available):
logging <BINDPLANE_IP> tls 6514 severity info
Set the syslog facility:
logging facility local0
Save the configuration:
write memory
exit
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
read_only_udm.metadata.product_event_type
Direct mapping.
action
read_only_udm.security_result.action
If action is "deny", set to "BLOCK". If action is "allow", set to "ALLOW".
column10
read_only_udm.network.session_id
Direct mapping.
column11
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "security_policy_id".
column12
read_only_udm.security_result.rule_id
Direct mapping.
column13
read_only_udm.security_result.rule_name
Direct mapping.
column14
read_only_udm.network.sent_packets
Direct mapping.
column15
read_only_udm.network.sent_bytes
Direct mapping.
column16
read_only_udm.network.received_packets
Direct mapping.
column17
read_only_udm.network.received_bytes
Direct mapping.
column18
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "vlan".
column19
read_only_udm.principal.asset.software.vendor_name
Direct mapping.
column19
read_only_udm.principal.asset.software.name
Direct mapping.
column2
read_only_udm.metadata.product_event_type
Direct mapping.
column20
read_only_udm.principal.asset.software.version
Direct mapping.
column21
read_only_udm.principal.asset_id
Concatenates "asset_id:" with the value of column21.
column22
read_only_udm.principal.asset.attribute.labels.value
Direct mapping. Key is hardcoded as "device_name".
column23
read_only_udm.principal.asset.attribute.labels.value
Direct mapping. Key is hardcoded as "unit_id".
column24
read_only_udm.metadata.product_version
Direct mapping.
column25
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "policy_name".
column25
read_only_udm.security_result.rule_type
Direct mapping.
column4
read_only_udm.principal.resource.product_object_id
Direct mapping.
column5
read_only_udm.principal.ip
Direct mapping.
column6
read_only_udm.principal.port
Direct mapping.
column7
read_only_udm.target.ip
Direct mapping.
column8
read_only_udm.target.port
Direct mapping.
column9
read_only_udm.network.ip_protocol
Maps the numeric protocol number to its corresponding name (e.g., 6 to TCP, 17 to UDP).
dip
read_only_udm.target.ip
Direct mapping.
dport
read_only_udm.target.port
Direct mapping.
dvc
read_only_udm.intermediary.hostname
If dvc is not an IP address, map to hostname. Otherwise, map to IP.
iflowbytes
read_only_udm.network.sent_bytes
Direct mapping.
iflowpkts
read_only_udm.network.sent_packets
Direct mapping.
msg_id
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "msg_id".
policy_name
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "policy_name".
policy_name
read_only_udm.security_result.rule_type
Direct mapping.
proc_id
read_only_udm.target.process.pid
Direct mapping.
proc_name
read_only_udm.target.application
Direct mapping.
protocol_number_src
read_only_udm.network.ip_protocol
Maps the numeric protocol number to its corresponding name (e.g., 6 to TCP, 17 to UDP).
rflowbytes
read_only_udm.network.received_bytes
Direct mapping.
rflowpkts
read_only_udm.network.received_packets
Direct mapping.
rule_id
read_only_udm.security_result.rule_id
Direct mapping.
rule_name
read_only_udm.security_result.rule_name
Direct mapping.
sd
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "sd".
security_policy_id
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "security_policy_id".
session_id
read_only_udm.network.session_id
Direct mapping.
session_state
read_only_udm.metadata.product_event_type
Direct mapping.
sip
read_only_udm.principal.ip
Direct mapping.
software_version
read_only_udm.principal.asset.software.version
Direct mapping.
sport
read_only_udm.principal.port
Direct mapping.
ts
read_only_udm.metadata.event_timestamp
The timestamp from the log is parsed and formatted into the UDM timestamp format.
vlan
read_only_udm.additional.fields.value.string_value
Direct mapping. Key is hardcoded as "vlan".
read_only_udm.metadata.event_type
If both sip and dip are present, set to "NETWORK_UNCATEGORIZED". If only sip is present, set to "STATUS_UPDATE". Otherwise, set to "GENERIC_EVENT".
read_only_udm.metadata.log_type
Hardcoded to "AMD_DSS_FIREWALL".
read_only_udm.metadata.product_name
Hardcoded to "AMD_DSS_FIREWALL".
read_only_udm.metadata.vendor_name
Hardcoded to "AMD_DSS_FIREWALL".
read_only_udm.principal.resource.resource_type
Hardcoded to "VPC_NETWORK".
Need more help?
Get answers from Community members and Google SecOps professionals.
