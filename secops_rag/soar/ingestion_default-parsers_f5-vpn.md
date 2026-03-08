# Collect F5 VPN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-vpn/  
**Scraped:** 2026-03-05T09:55:35.550343Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 VPN logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 VPN logs to Google Security Operations using
Bindplane. The parser extracts security-relevant information from the logs.
It uses regular expressions to identify and parse key fields like timestamps,
IP addresses, and hostnames, then structures this data into the
Google SecOps Unified Data Model (UDM) format for analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to F5 BIG-IP APM (Access Policy Manager)
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
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'F5_VPN'
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
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog for F5 BIG-IP APM v11.x and newer
Sign in to the
F5 BIG-IP APM
using
CLI
or
SSH
.
Enter the following command to add the syslog server:
tmsh
syslog
remote
server
{
<Name>
{
host
<bindplane-ip>
remote-port
<bindplane-port>
}}
Make sure to replace the following parameters:
<Name>
: Enter the name of the F5 BIG-IP APM source (for example
BIGIP_APM
).
<bindplane-ip>
: Enter the Bindplane agent IP address.
<bindplane-port>
: Enter the Bindplane agent port number.
Enter the following command to save changes:
tmsh
save
sys
config
partitions
all
UDM mapping table
Log field
UDM mapping
Logic
cmd_data
principal.process.command_line
The value is extracted from the msg field
errdefs_msgno
additional.fields.errdefs_msgno.string_value
The value is extracted from the msg field
event_time
metadata.event_timestamp
The value is parsed and converted to a timestamp
hostname
principal.hostname, observer.hostname, principal.asset.hostname, observer.asset.hostname, hostip
The value is extracted from the message field and used to populate the hostname fields in the UDM. Also used to populate the hostip field
msg
security_result.description
The value is extracted from the message field and used to populate the description field in the security_result object
prin_ip
principal.ip, principal.asset.ip
The value is extracted from the message field and used to populate the IP address fields in the UDM
additional.fields.Canonical_Info.string_value
The value is derived from the log message
additional.fields.IDP.string_value
The value is derived from the log message
additional.fields.Plugin_Support.string_value
The value is derived from the log message
additional.fields.SMB Stage.string_value
The value is derived from the log message
additional.fields.SP.string_value
The value is derived from the log message
additional.fields.Timezone.string_value
The value is derived from the log message
additional.fields.Tunnel Type.string_value
The value is derived from the log message
additional.fields.UI_Mode.string_value
The value is derived from the log message
additional.fields.Version.string_value
The value is derived from the log message
additional.fields.from_rule_item.string_value
The value is derived from the log message
additional.fields.policy_result.string_value
The value is derived from the log message
additional.fields.ppp_id.string_value
The value is derived from the log message
additional.fields.resource.string_value
The value is derived from the log message
additional.fields.rule.string_value
The value is derived from the log message
additional.fields.server_vip_ip.string_value
The value is derived from the log message
additional.fields.server_vip_name.string_value
The value is derived from the log message
additional.fields.to_rule_item.string_value
The value is derived from the log message
additional.fields.tunnel_resource.string_value
The value is derived from the log message
metadata.description
The value is derived from the log message
metadata.event_type
The value is hardcoded in the parser code for some events and is derived from the log message for others
metadata.log_type
The value is set to the batch type
metadata.product_event_type
The value is derived from the log message
metadata.product_name
The value is hardcoded in the parser code
metadata.vendor_name
The value is hardcoded in the parser code
network.application_protocol
The value is derived from the log message
network.direction
The value is derived from the log message
network.http.method
The value is derived from the log message
network.http.parsed_user_agent
The value is derived from the network.http.user_agent field
network.http.referral_url
The value is derived from the log message
network.http.response_code
The value is derived from the log message
network.http.user_agent
The value is derived from the log message
network.ip_protocol
The value is derived from the log message
network.received_bytes
The value is derived from the log message
network.sent_bytes
The value is derived from the log message
network.session_id
The value is derived from the log message
network.tls.cipher
The value is derived from the log message
network.tls.version
The value is derived from the log message
observer.asset.hostname
The value is set to the hostname field
observer.asset.ip
The value is set to the hostip field
observer.hostname
The value is set to the hostname field
observer.ip
The value is set to the hostip field
principal.application
The value is derived from the log message
principal.asset.hostname
The value is set to the hostname field
principal.asset.ip
The value is set to the hostip field or prin_ip field if it exists
principal.asset.product_object_id
The value is derived from the log message
principal.hostname
The value is set to the hostname field
principal.ip
The value is set to the hostip field or prin_ip field if it exists
principal.location.country_or_region
The value is derived from the log message
principal.platform
The value is derived from the log message
principal.port
The value is derived from the log message
principal.process.command_line
The value is derived from the log message
principal.process.pid
The value is derived from the log message
principal.resource.name
The value is derived from the log message
principal.resource.type
The value is hardcoded in the parser code for some events and is derived from the log message for others
principal.user.email_addresses
The value is derived from the log message
principal.user.userid
The value is derived from the log message
security_result.action
The value is derived from the log message
security_result.description
The value is derived from the log message
security_result.rule_name
The value is derived from the log message
security_result.severity
The value is derived from the log message
security_result.severity_details
The value is derived from the log message
security_result.summary
The value is derived from the log message
src.ip
The value is derived from the log message
src.location.country_or_region
The value is derived from the log message
src.port
The value is derived from the log message
target.asset.hostname
The value is derived from the log message
target.asset.ip
The value is derived from the log message
target.hostname
The value is derived from the log message
target.ip
The value is derived from the log message
target.port
The value is derived from the log message
target.process.command_line
The value is derived from the log message
target.process.pid
The value is derived from the log message
target.resource.id
The value is derived from the log message
target.url
The value is derived from the log message
target.user.userid
The value is derived from the log message
Need more help?
Get answers from Community members and Google SecOps professionals.
