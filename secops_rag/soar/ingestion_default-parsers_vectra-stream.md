# Collect Vectra Stream logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-stream/  
**Scraped:** 2026-03-05T10:02:00.192341Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Vectra Stream logs
Supported in:
Google secops
SIEM
This document explains how to ingest Vectra Stream logs to Google Security Operations using Bindplane. The parser extracts key-value pairs from Vectra Stream logs, normalizes various fields into a unified data model (UDM), and maps log types to specific UDM event types. It handles both JSON and syslog formatted logs, dropping malformed messages and enriching the data with additional context based on specific field values.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
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
'VECTRA_STREAM'
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
Configure Vectra Stream to send Syslog
Sign in to the Vectra (brain) UI.
Go to
Settings
>
Notifications
.
Go to the
Syslog
section.
Click
Edit
to add or edit Syslog configuration.
Provide the following configuration details:
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
Click
Save
.
Click
Test
to test configuration.
UDM Mapping Table
Log Field
UDM Mapping
Logic
AA
network.dns.authoritative
Converted to boolean from string value.
account_session_id
network.session_id
Direct mapping.
account_session_time
network.session_duration
Converted to timestamp from UNIX seconds.
answers
network.dns.answers.data
Direct mapping.
assigned_ip
network.dhcp.yiaddr
Direct mapping.
beacon_type
metadata.description
Direct mapping.
beacon_uid
network.session_id
Direct mapping.
calling_station_id
intermediary.asset.product_object_id
Direct mapping.
certificate.issuer
network.tls.client.certificate.issuer
Direct mapping.
certificate.not_valid_after
network.tls.client.certificate.not_after
Converted to timestamp from UNIX or UNIX_MS depending on format.
certificate.not_valid_before
network.tls.client.certificate.not_before
Converted to timestamp from UNIX or UNIX_MS depending on format.
certificate.serial
network.tls.client.certificate.serial
Direct mapping.
certificate.subject
network.tls.client.certificate.subject
Direct mapping.
certificate.version
network.tls.client.certificate.version
Direct mapping.
cipher
network.tls.cipher
Direct mapping.
cipher_alg
network.tls.cipher
Direct mapping.
client
principal.application
Direct mapping.
client_cipher
network.tls.client.supported_ciphers
Direct mapping.
community_id
network.community_id
Direct mapping.
compression_alg
additional.fields.value.string_value
Added to additional fields with key "compression_alg".
connect_info
security_result.description
Direct mapping.
conn_state
metadata.description
Mapped to a description based on the value of conn_state.
cookie
target.user.userid
Direct mapping.
curve
network.tls.curve
Direct mapping.
dhcp_server_ip
network.dhcp.giaddr
Direct mapping.
dns_server_ips
principal.ip
Each IP in the array is added to the principal.ip array.
domain
target.domain.name
Direct mapping.
dst_display_name
target.hostname, target.asset.hostname
Direct mapping.
dst_luid
target.asset.product_object_id
Direct mapping.
duration
network.session_duration.seconds
Converted to integer from string value.
endpoint
principal.application
Direct mapping.
established
network.tls.established
Converted to boolean from string value.
host
target.hostname, target.asset.hostname
Extracted hostname from the "host" field.
host_key
additional.fields.value.string_value
Added to additional fields with key "host_key".
host_key_alg
additional.fields.value.string_value
Added to additional fields with key "host_key_alg".
host_multihomed
additional.fields.value.string_value
Added to additional fields with key "host_multihomed" and value "subnet %{host_multihomed}".
hostname
target.hostname, target.asset.hostname
Direct mapping.
id.orig_h
principal.ip
Direct mapping.
id.orig_p
principal.port
Converted to integer from string value.
id.resp_h
target.ip, target.asset.ip
Direct mapping.
id.resp_p
target.port
Converted to integer from string value.
issuer
network.tls.client.certificate.issuer
Direct mapping.
ja3
network.tls.client.ja3
Direct mapping.
ja3s
network.tls.server.ja3s
Direct mapping.
kex_alg
additional.fields.value.string_value
Added to additional fields with key "kex_alg".
lease_time
network.dhcp.lease_time_seconds
Converted to unsigned integer from string value.
log_type
metadata.log_type
Direct mapping.
mac
principal.mac
Direct mapping.
mac_alg
additional.fields.value.string_value
Added to additional fields with key "mac_alg".
mail_from
network.email.from
Direct mapping.
metadata_type
metadata.product_event_type
Direct mapping.
method
network.http.method
Direct mapping.
name
target.file.full_path
Direct mapping.
nas_identifier
target.user.attribute.roles.name
Direct mapping.
next_protocol
network.tls.next_protocol
Direct mapping.
orig_hostname
principal.hostname
Direct mapping.
orig_ip_bytes
network.sent_bytes
Converted to unsigned integer from string value.
orig_sluid
principal.hostname
Direct mapping.
path
target.file.full_path
Direct mapping.
proto
network.ip_protocol
Mapped to IP protocol name based on numeric value.
proxied
principal.ip
If the value is an IP address, it is added to the principal.ip array.
qclass
network.dns.questions.class
Converted to unsigned integer from string value.
qclass_name
network.dns.questions.name
Direct mapping.
query
network.dns.questions.name, principal.process.command_line
Direct mapping.
qtype
network.dns.questions.type
Converted to unsigned integer from string value.
RA
network.dns.recursion_available
Converted to boolean from string value.
radius_type
metadata.description
Direct mapping.
rcode
network.dns.response_code
Converted to unsigned integer from string value.
RD
network.dns.recursion_desired
Converted to boolean from string value.
rcpt_to
network.email.reply_to, network.email.to
The first email address is mapped to reply_to, the rest are added to the to array.
referrer
network.http.referral_url
Direct mapping.
resp_domain
target.domain.name
Direct mapping.
resp_hostname
target.hostname, target.asset.hostname
Direct mapping.
resp_ip_bytes
network.received_bytes
Converted to unsigned integer from string value.
resp_mime_types
target.file.mime_type
Direct mapping.
result
security_result.description
Direct mapping.
result_code
security_result.action_details
Direct mapping.
rtt
network.session_duration.seconds
Converted to integer from string value.
security_result
security_result
Merged with existing security_result object.
sensor_uid
observer.asset_id
Formatted as "Sensor_UID:%{sensor_uid}".
server
target.application
Direct mapping.
server_name
network.tls.client.server_name
Direct mapping.
service
target.application
Direct mapping.
src_display_name
principal.hostname
Direct mapping.
src_luid
principal.asset.product_object_id
Direct mapping.
status
security_result.summary
Direct mapping.
status_code
network.http.response_code
Converted to integer from string value.
status_msg
security_result.summary
Direct mapping.
subject
network.email.subject
Direct mapping.
success
security_result.action
Mapped to "ALLOW" if true, "BLOCK" if false.
TC
network.dns.truncated
Converted to boolean from string value.
trans_id
network.dhcp.transaction_id, network.dns.id
Converted to unsigned integer from string value.
ts
metadata.event_timestamp
Converted to timestamp from various formats.
uid
metadata.product_log_id
Direct mapping.
uri
target.url
Direct mapping.
user_agent
network.http.user_agent
Direct mapping.
username
principal.user.userid
Direct mapping.
version
network.tls.version, principal.platform_version
Direct mapping.
version_num
network.tls.version_protocol
Direct mapping.
metadata.event_type
Determined by the parser logic based on the log and metadata types.
metadata.vendor_name
Hardcoded value: "Vectra".
metadata.product_name
Hardcoded value: "Vectra Stream".
Need more help?
Get answers from Community members and Google SecOps professionals.
