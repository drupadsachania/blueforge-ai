# Collect VMware Networking and Security Virtualization 
(NSX) Manager logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-nsx/  
**Scraped:** 2026-03-05T09:30:01.441495Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware Networking and Security Virtualization 
(NSX) Manager logs
Supported in:
Google secops
SIEM
This document describes how you can collect the VMware Networking and Security Virtualization (NSX) Manager logs. The parser extracts fields using various grok patterns based on the message format. It then performs key-value parsing, JSON parsing, and conditional logic to map the extracted fields to the UDM, handling different log formats and enriching the data with additional context.
Before you begin
Ensure you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure you have administrative access to VMWare NSX.
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
system where Bindplane Agent will be installed.
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
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
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
# Replace the below port <54525> and IP <0.0.0.0> with your specific values
listen_address
:
"0.0.0.0:54525"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the creds location below according the placement of the credentials file you downloaded
creds
:
'{
json
file
for
creds
}'
# Replace <customer_id> below with your actual ID that you copied
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# You can apply ingestion labels below as preferred
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
vmware_nsx
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
Restart Bindplane Agent to apply the changes
In Linux, to restart the Bindplane Agent, run the following command:
sudo
systemctl
restart
bindplane-agent
In Windows, to restart the Bindplane Agent, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Syslog Configuration for NSX Edge
Sign in to the
vSphere Web Client
.
Go to
Networking & Security
>
NSX Edges
.
Select the specific
NSX Edge
instance you want to configure.
Go to
Syslog Settings
:
For NSX 6.4.4 and later:
Go to
Manage
>
Settings
>
Appliance Settings
.
Click
Settings
>
Change Syslog Configuration
.
For NSX 6.4.3 and earlier:
Go to
Manage
>
Settings
>
Configuration
.
In the
Details
dialog, click
Change
.
Configure the Syslog server details:
Server
: enter the IP address or hostname of the Syslog server (Bindplane).
Protocol
: select
UDP
or
TCP
(depending on your Bindplane configuration).
Port
: enter the port number (depending on your Bindplane configuration).
Click
OK
to save the settings.
Syslog Configuration for NSX Manager
Sign in to the NSX Manager web interface with administrator credentials as follows:
https://<NSX-Manager-IP>
or
https://<NSX-Manager-Hostname>
.
Go to
Manage Appliance Settings
>
General
.
Click
Edit
to configure the Syslog server settings.
Enter the Syslog server details:
Server
: enter the IP address or hostname of the Syslog server (Bindplane).
Protocol
: select
UDP
or
TCP
(depending on your Bindplane configuration).
Port
: enter the port number (depending on your Bindplane configuration).
Click
OK
to save the settings.
Syslog Configuration for NSX Controller
Sign in to the vSphere Web Client.
Go to
Networking & Security
>
Installation and Upgrade
>
Management
>
NSX Controller Nodes
.
Select the
NSX Manager
that manages the controller nodes.
Click
Common Controller Attributes Edit
.
In the
Syslog Servers
dialog, click
Add
:
Enter the Syslog server name or IP address.
Select the
UDP
protocol (depending on your Bindplane configuration).
Set the
Log Level
(for example,
INFO
).
Click
OK
to save the settings.
UDM Mapping Table
Log Field
UDM Mapping
Logic
DST
event.idm.read_only_udm.target.ip
The destination IP address is extracted from the
DST
field in the raw log.
ID
event.idm.read_only_udm.metadata.product_log_id
The product log ID is extracted from the
ID
field in the raw log.
MAC
event.idm.read_only_udm.principal.mac
The MAC address is extracted from the
MAC
field in the raw log.
ModuleName
event.idm.read_only_udm.metadata.product_event_type
The product event type is extracted from the
ModuleName
field in the raw log.
Operation
event.idm.read_only_udm.principal.resource.attribute.labels.value
The operation is extracted from the
Operation
field in the raw log and added as a label with key "Operation".
PROTO
event.idm.read_only_udm.network.ip_protocol
The IP protocol is extracted from the
PROTO
field in the raw log.
RES
event.idm.read_only_udm.target.resource.name
The target resource name is extracted from the
RES
field in the raw log.
SRC
event.idm.read_only_udm.principal.ip
The source IP address is extracted from the
SRC
field in the raw log.
SPT
event.idm.read_only_udm.principal.port
The source port is extracted from the
SPT
field in the raw log.
UserName
event.idm.read_only_udm.principal.user.userid
The user ID is extracted from the
UserName
field in the raw log.
app_type
event.idm.read_only_udm.principal.application
The principal application is extracted from the
app_type
field in the raw log.
application
event.idm.read_only_udm.target.application
The target application is extracted from the
application
field in the raw log.
audit
event.idm.read_only_udm.principal.resource.attribute.labels.value
The audit value is extracted from the
audit
field in the raw log and added as a label with key "audit".
cancelTimeUTC
event.idm.read_only_udm.principal.resource.attribute.last_update_time
The last update time is derived from the
cancelTimeUTC
field in the raw log.
client
event.idm.read_only_udm.principal.ip
or
event.idm.read_only_udm.principal.administrative_domain
If the
client
field is an IP address, it's mapped to principal IP. Otherwise, it's mapped to principal administrative domain.
comp
event.idm.read_only_udm.principal.resource.attribute.labels.value
The component value is extracted from the
comp
field in the raw log and added as a label with key "Comp".
datetime
event.idm.read_only_udm.metadata.event_timestamp
The event timestamp is extracted from the
datetime
field in the raw log.
description
event.idm.read_only_udm.metadata.description
The description is extracted from the
description
field in the raw log.
details
event.idm.read_only_udm.principal.resource.attribute.labels
The details are extracted from the
details
field in the raw log and added as labels.
direction
event.idm.read_only_udm.network.direction
If the
direction
field is "OUT", it's mapped to "OUTBOUND".
dst_ip
event.idm.read_only_udm.target.ip
The destination IP address is extracted from the
dst_ip
field in the raw log.
DPT
event.idm.read_only_udm.target.port
The destination port is extracted from the
DPT
field in the raw log.
errorCode
event.idm.read_only_udm.security_result.detection_fields
The error code is extracted from the
errorCode
field in the raw log and added as a detection field.
eventType
event.idm.read_only_udm.metadata.product_event_type
The product event type is extracted from the
eventType
field in the raw log.
filepath
event.idm.read_only_udm.principal.process.file.full_path
The file path is extracted from the
filepath
field in the raw log.
hostname
event.idm.read_only_udm.principal.ip
The hostname is extracted from the
hostname
field in the raw log and, if it's an IP address, mapped to principal IP.
kv_data
Various UDM fields
The key-value pairs in
kv_data
are mapped to various UDM fields based on their keys.
kv_data1
Various UDM fields
The key-value pairs in
kv_data1
are mapped to various UDM fields based on their keys.
kv_data2
Various UDM fields
The key-value pairs in
kv_data2
are mapped to various UDM fields based on their keys.
kv_data3
Various UDM fields
The key-value pairs in
kv_data3
are mapped to various UDM fields based on their keys.
kv_data4
Various UDM fields
The key-value pairs in
kv_data4
are mapped to various UDM fields based on their keys.
level
event.idm.read_only_udm.security_result.severity
If the
level
field is "INFO", it's mapped to "INFORMATIONAL". If it's "ERROR", it's mapped to "ERROR".
managedExternally
event.idm.read_only_udm.principal.resource.attribute.labels.value
The managedExternally value is extracted from the
managedExternally
field in the raw log and added as a label with key "managedExternally".
message
Various UDM fields
The message field is parsed to extract various UDM fields.
message_data
event.idm.read_only_udm.principal.resource.attribute.labels.value
The message data is extracted from the
message_data
field in the raw log and added as a label with key "message".
network_status
event.idm.read_only_udm.additional.fields
The network status is extracted from the
network_status
field in the raw log and added as an additional field with key "Network_Connection_Status".
new_value
Various
event.idm.read_only_udm.target
fields
The new value is extracted from the
new_value
field in the raw log and used to populate various target fields.
node
event.idm.read_only_udm.principal.resource.attribute.labels.value
The node value is extracted from the
node
field in the raw log and added as a label with key "node".
old_value
Various UDM fields
The old value is extracted from the
old_value
field in the raw log and used to populate various UDM fields.
payload
Various UDM fields
The payload is extracted from the
payload
field in the raw log and used to populate various UDM fields.
pid
event.idm.read_only_udm.target.process.pid
The process ID is extracted from the
pid
field in the raw log.
reqId
event.idm.read_only_udm.metadata.product_log_id
The product log ID is extracted from the
reqId
field in the raw log.
resourceId
event.idm.read_only_udm.principal.resource.product_object_id
The product object ID is extracted from the
resourceId
field in the raw log.
s2comp
event.idm.read_only_udm.principal.resource.attribute.labels.value
The s2comp value is extracted from the
s2comp
field in the raw log and added as a label with key "s2comp".
ses
event.idm.read_only_udm.network.session_id
The session ID is extracted from the
ses
field in the raw log.
src_host
event.idm.read_only_udm.principal.hostname
The principal hostname is extracted from the
src_host
field in the raw log.
src_ip
event.idm.read_only_udm.principal.ip
The source IP address is extracted from the
src_ip
field in the raw log.
src_ip1
event.idm.read_only_udm.principal.ip
The source IP address is extracted from the
src_ip1
field in the raw log.
src_port
event.idm.read_only_udm.principal.port
The source port is extracted from the
src_port
field in the raw log.
startTimeUTC
event.idm.read_only_udm.principal.resource.attribute.creation_time
The creation time is derived from the
startTimeUTC
field in the raw log.
subcomp
event.idm.read_only_udm.network.application_protocol
or
event.idm.read_only_udm.principal.resource.attribute.labels.value
If the
subcomp
field is "http", it's mapped to "HTTP". Otherwise, it's added as a label with key "Sub Comp".
tname
event.idm.read_only_udm.principal.resource.attribute.labels.value
The tname value is extracted from the
tname
field in the raw log and added as a label with key "tname".
type
event.idm.read_only_udm.metadata.product_event_type
The product event type is extracted from the
type
field in the raw log.
uid
event.idm.read_only_udm.principal.user.userid
The user ID is extracted from the
uid
field in the raw log.
update
event.idm.read_only_udm.principal.resource.attribute.labels.value
The update value is extracted from the
update
field in the raw log and added as a label with key "update".
user
event.idm.read_only_udm.principal.user.user_display_name
The user display name is extracted from the
user
field in the raw log.
vmw_cluster
event.idm.read_only_udm.target.resource.name
The target resource name is extracted from the
vmw_cluster
field in the raw log.
vmw_datacenter
event.idm.read_only_udm.target.resource.attribute.labels.value
The vmw_datacenter value is extracted from the
vmw_datacenter
field in the raw log and added as a label with key "vmw_datacenter".
vmw_host
event.idm.read_only_udm.target.hostname
or
event.idm.read_only_udm.target.ip
If the
vmw_host
field is a hostname, it's mapped to target hostname. Otherwise, if it's an IP address, it's mapped to target IP.
vmw_object_id
event.idm.read_only_udm.target.resource.product_object_id
The product object ID is extracted from the
vmw_object_id
field in the raw log.
vmw_product
event.idm.read_only_udm.target.application
The target application is extracted from the
vmw_product
field in the raw log.
vmw_vcenter
event.idm.read_only_udm.target.cloud.availability_zone
The availability zone is extracted from the
vmw_vcenter
field in the raw log.
vmw_vcenter_id
event.idm.read_only_udm.target.resource.attribute.labels.value
The vmw_vcenter_id value is extracted from the
vmw_vcenter_id
field in the raw log and added as a label with key "vmw_vcenter_id".
vmw_vr_ops_appname
event.idm.read_only_udm.intermediary.application
The intermediary application is extracted from the
vmw_vr_ops_appname
field in the raw log.
vmw_vr_ops_clustername
event.idm.read_only_udm.intermediary.resource.name
The intermediary resource name is extracted from the
vmw_vr_ops_clustername
field in the raw log.
vmw_vr_ops_clusterrole
event.idm.read_only_udm.intermediary.resource.attribute.roles.name
The intermediary resource role name is extracted from the
vmw_vr_ops_clusterrole
field in the raw log.
vmw_vr_ops_hostname
event.idm.read_only_udm.intermediary.hostname
The intermediary hostname is extracted from the
vmw_vr_ops_hostname
field in the raw log.
vmw_vr_ops_id
event.idm.read_only_udm.intermediary.resource.product_object_id
The intermediary product object ID is extracted from the
vmw_vr_ops_id
field in the raw log.
vmw_vr_ops_logtype
event.idm.read_only_udm.intermediary.resource.attribute.labels.value
The vmw_vr_ops_logtype value is extracted from the
vmw_vr_ops_logtype
field in the raw log and added as a label with key "vmw_vr_ops_logtype".
vmw_vr_ops_nodename
event.idm.read_only_udm.intermediary.resource.attribute.labels.value
The vmw_vr_ops_nodename value is extracted from the
vmw_vr_ops_nodename
field in the raw log and added as a label with key "vmw_vr_ops_nodename". Determined by a series of conditional statements based on the values of other fields. Possible values are USER_LOGIN, NETWORK_CONNECTION, STATUS_UPDATE, and GENERIC_EVENT. Hardcoded to "VMWARE_NSX". Hardcoded to "VMWARE_NSX". Hardcoded to "VMWARE_NSX". Set to "AUTHTYPE_UNSPECIFIED" if
Operation
is "LOGIN" and
target_details
is not empty, or if the
message
contains "authentication failure" and
application
is not empty. Set to "SSH" if
PROTO
is "ssh2", or set to "HTTP" if
subcomp
is "http". Determined by a series of conditional statements based on the values of other fields. Possible values are ALLOW and BLOCK. Set to "VIRTUAL_MACHINE" if
vmw_cluster
is not empty.
Need more help?
Get answers from Community members and Google SecOps professionals.
