# Collect Vectra Detect logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-detect/  
**Scraped:** 2026-03-05T09:29:47.845347Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Vectra Detect logs
Supported in:
Google secops
SIEM
This document explains how to ingest Vectra Detect logs to Google Security Operations using Bindplane. The parser transforms the logs from SYSLOG, JSON, and CEF formats into a unified data model (UDM). It first normalizes the data by removing unnecessary characters and fields, then uses
grok
patterns to extract information from different log formats, and finally maps the extracted fields to the corresponding UDM attributes.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the BindPlane agent requirements
Privileged access to the Vectra UI
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
'VECTRA_DETECT'
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
Configure Vectra Detect to send Syslog
Sign in to the Vectra Detect UI.
Go to
Settings
>
Notification
.
Go to the
Syslog
section.
Click
Edit
to add or edit Syslog configuration.
Destination
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Protocol
: Select
UDP
or
TCP
based on your actual Bindplane agent configuration.
Format
: Select
JSON
.
Log Types
: Select the logs you want to send to Google SecOps.
Select the
Include Enhanced Details
checkbox.
On the right side, you can see three switch buttons for addtitional configuration:
Include triaged Detections
: When turned off, syslog messages won't be sent when triaged detections are created or updated.
Include detections in Info category
: When turned off, syslog messages won't be sent when detections in the info category are created or updated.
Include host/account score decreases
: When turned off, syslog messages won't be sent when threat and certainty scores are both decreasing and/or remain the same.
Click
Save
.
Click
Test
to test configuration.
UDM Mapping Table
Log field
UDM mapping
Logic
action
read_only_udm.security_result.action
Value taken from "action" field if [result] is "true" or "failure" in Audit Events.
category
read_only_udm.security_result.category_details
Value taken from "category" field.
certainty
read_only_udm.security_result.confidence
If [certainty] is between 0 and 35, set to "LOW_CONFIDENCE". If [certainty] is between 35 and 70, set to "MEDIUM_CONFIDENCE". If [certainty] is between 70 and 100, set to "HIGH_CONFIDENCE".
dd_bytes_rcvd
read_only_udm.network.received_bytes
Value taken from "dd_bytes_rcvd" field.
dd_bytes_sent
read_only_udm.network.sent_bytes
Value taken from "dd_bytes_sent" field.
dd_dst_dns
read_only_udm.target.hostname
Value taken from "dd_dst_dns" field.
dd_dst_dns
read_only_udm.target.asset.hostname
Value taken from "dd_dst_dns" field.
dd_dst_ip
read_only_udm.target.asset.ip
Value taken from "dd_dst_ip" field.
dd_dst_ip
read_only_udm.target.ip
Value taken from "dd_dst_ip" field.
dd_dst_port
read_only_udm.target.port
Value taken from "dd_dst_port" field.
detection_id
read_only_udm.metadata.product_log_id
Value taken from "detection_id" field.
detection_profile.name
read_only_udm.security_result.detection_fields
Key is "detection_profile name", value is taken from "detection_profile.name" field.
detection_profile.scoringDetections
read_only_udm.security_result.detection_fields
Key is "detection
profile scoringDetections
{index}", value is taken from each element in "detection_profile.scoringDetections" array.
detection_profile.vname
read_only_udm.security_result.detection_fields
Key is "detection_profile vname", value is taken from "detection_profile.vname" field.
dest_ip
read_only_udm.target.asset.ip
Value taken from "dest_ip" field in Campaigns Events.
dest_ip
read_only_udm.target.ip
Value taken from "dest_ip" field in Campaigns Events.
dest_name
read_only_udm.target.asset.hostname
Value taken from "dest_name" field in Campaigns Events.
dest_name
read_only_udm.target.hostname
Value taken from "dest_name" field in Campaigns Events.
d_type
read_only_udm.additional.fields
Key is "d_type", value is taken from "d_type" field.
d_type_vname
read_only_udm.additional.fields
Key is "d_type_vname", value is taken from "d_type_vname" field.
dvchost
read_only_udm.observer.hostname
Value taken from "dvchost" field.
dvchost
read_only_udm.principal.asset.hostname
Value taken from "dvchost" field if [host_name] is empty in HOST Events.
dvchost
read_only_udm.principal.hostname
Value taken from "dvchost" field if [host_name] is empty in HOST Events.
headend_addr
read_only_udm.observer.ip
Value taken from "headend_addr" field.
headend_addr
read_only_udm.principal.asset.ip
Value taken from "headend_addr" field if [host_ip] is empty in Detections Events.
headend_addr
read_only_udm.principal.ip
Value taken from "headend_addr" field if [host_ip] is empty in Detections Events.
href
read_only_udm.target.url
Value taken from "href" field.
host_id
read_only_udm.target.asset_id
Value is "VectraAI.DETECT:{host_id}" in HOST Events.
host_ip
read_only_udm.principal.asset.ip
Value taken from "host_ip" field in HOST and Detections Events.
host_ip
read_only_udm.principal.ip
Value taken from "host_ip" field in HOST and Detections Events.
host_name
read_only_udm.principal.asset.hostname
Value taken from "host_name" field.
host_name
read_only_udm.principal.hostname
Value taken from "host_name" field.
msg_data
read_only_udm.security_result.summary
Value taken from "msg_data" field in Audit and Health Events.
quadrant
read_only_udm.security_result.priority_details
Value taken from "quadrant" field.
result
read_only_udm.security_result.action
If [result] is "true", set to "ALLOW". If [result] is "failure", set to "BLOCK" in Audit Events.
result
read_only_udm.security_result.detection_fields
Key is "result", value is taken from "result" field in Audit and Health Events.
role
read_only_udm.target.user.attribute.roles.name
Value taken from "role" field in Audit Events.
severity
read_only_udm.security_result.severity
If [threat] is between 0 and 20, set to "INFORMATIONAL". If [threat] is between 20 and 40, set to "LOW". If [threat] is between 40 and 60, set to "MEDIUM". If [threat] is between 60 and 80, set to "HIGH". If [threat] is between 80 and 100, set to "CRITICAL".
severity
read_only_udm.security_result.severity_details
Value taken from "severity" field.
source_ip
read_only_udm.principal.asset.ip
Value taken from "source_ip" field in Audit and Health Events.
source_ip
read_only_udm.principal.ip
Value taken from "source_ip" field in Audit and Health Events.
src
read_only_udm.principal.asset.ip
Value taken from "src" field in CEF Events.
src
read_only_udm.principal.ip
Value taken from "src" field in CEF Events.
src_ip
read_only_udm.principal.asset.ip
Value taken from "src_ip" field in Campaigns Events.
src_ip
read_only_udm.principal.ip
Value taken from "src_ip" field in Campaigns Events.
src_name
read_only_udm.principal.asset.hostname
Value taken from "src_name" field if [host_name] and [dvchost] are empty.
src_name
read_only_udm.principal.hostname
Value taken from "src_name" field if [host_name] and [dvchost] are empty.
threat
read_only_udm.security_result.severity
If [threat] is between 0 and 20, set to "INFORMATIONAL". If [threat] is between 20 and 40, set to "LOW". If [threat] is between 40 and 60, set to "MEDIUM". If [threat] is between 60 and 80, set to "HIGH". If [threat] is between 80 and 100, set to "CRITICAL".
triaged
read_only_udm.additional.fields
Key is "triaged", value is taken from "triaged" field.
type
read_only_udm.metadata.product_event_type
Value taken from "type" field in Health Events.
user
read_only_udm.target.user.userid
Value taken from "user" field in Audit Events.
vectra_timestamp
read_only_udm.metadata.event_timestamp
Value taken from "vectra_timestamp" field.
version
read_only_udm.metadata.product_version
Value taken from "version" field.
read_only_udm.metadata.event_type
Set to "USER_LOGIN" if [msg_data] contains "log in" and [user] is not empty in Audit Events.
read_only_udm.metadata.event_type
Set to "SCAN_HOST" in HOST Events.
read_only_udm.metadata.event_type
Set to "NETWORK_HTTP" if [host_ip] is not empty, [principal_present] is true, and [target_present] is true in Detections Events.
read_only_udm.metadata.event_type
Set to "STATUS_UPDATE" if [principal_present] is true in Detections Events.
read_only_udm.metadata.event_type
Set to "NETWORK_CONNECTION" if [principal_present] is true and [target_present] is true in Detections Events.
read_only_udm.metadata.event_type
Set to "NETWORK_CONNECTION" if [event_type] is "GENERIC_EVENT", [principal_present] is true, and [target_present] is true.
read_only_udm.metadata.event_type
Set to "STATUS_UPDATE" if [event_type] is "GENERIC_EVENT" and [principal_present] is true.
read_only_udm.metadata.log_type
Set to "VECTRA_DETECT".
read_only_udm.metadata.vendor_name
Set to "Vectra.AI".
read_only_udm.metadata.product_name
Set to "DETECT".
read_only_udm.network.application_protocol
Set to "HTTP" if [dd_dst_port] is 80.
read_only_udm.network.application_protocol
Set to "HTTPS" if [dd_dst_port] is 443.
read_only_udm.network.application_protocol
Set to "UNKNOWN_APPLICATION_PROTOCOL" if [principal_present] is true and [target_present] is true in Detections Events.
read_only_udm.network.http.method
Set to "METHOD_OTHER".
read_only_udm.extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if [msg_data] contains "log in" in Audit Events.
is_alert
Set to "true" if [triaged] is true.
Need more help?
Get answers from Community members and Google SecOps professionals.
