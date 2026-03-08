# Collect Cisco Router logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-router/  
**Scraped:** 2026-03-05T09:21:40.978545Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Router logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Router logs to Google Security Operations using a Bindplane agent. The parser first extracts common fields from various syslog message formats using a series of Grok patterns, handling different timestamp and key-value data variations. Then, it applies specific logic based on the extracted event type (facility, mnemonics, message_type), enriching the data with additional fields and mapping them to the UDM model.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to a Cisco Router.
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
CISCO_ROUTER
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
Configure Syslog on a Cisco Router
Sign in to the Cisco Router.
Escalate privileges by entering the
enable
command:
Switch>
enable
Switch#
Switch to configuration mode by entering the
conf t
command:
Switch#
conf
t
Switch
(
config
)
#
Enter the following commands:
logging
host
<bindplane-server-ip>
transport
<tcp/udp>
port
<port-number>
logging
source-interface
<interface>
Replace
<bindplane-server-ip>
with the Bindplane agent IP address, and
<port-number>
with the configured port.
Replace
<tcp/udp>
with the configured listening protocol on the Bindplane agent; for example,
udp
.
Replace
<interface>
with the Cisco interface ID; for example,
Ethernet1/1
.
Set the priority level by entering the following command:
logging
trap
Informational
logging
console
Informational
logging
severity
Informational
Set the syslog facility:
logging
facility
local6
Enable timestamps by entering the following command:
service
timestamps
log
datetime
Save and exit.
Configure the settings to survive restart by entering the following command:
copy
running-config
startup-config
UDM Mapping Table
Log field
UDM mapping
Logic
client_ip
target.ip, target.asset.ip
The value is taken from the
client_ip
field extracted by the grok parser.
client_mac
target.mac
The value is taken from the
client_mac
field extracted by the grok parser.
dst_ip
target.ip, target.asset.ip
The value is taken from the
dst_ip
field extracted by the grok parser.
dst_port
target.port
The value is taken from the
dst_port
field extracted by the grok parser and converted to an integer.
duration
-
This field is not mapped to the UDM.
host_ip
target.ip, target.asset.ip
The value is taken from the
host_ip
field extracted by the grok parser.
local_proxy
intermediary.ip
The value is taken from the
local_proxy
field extracted by the grok parser.
message_data
metadata.description
The value is taken from the
message_data
field extracted by the grok parser.
protocol
network.ip_protocol
The value is taken from the
protocol
field extracted by the grok parser and converted to uppercase.
received_bytes
network.received_bytes
The value is taken from the
received_bytes
field extracted by the grok parser and converted to an unsigned integer.
referral_url
network.http.referral_url
The value is taken from the
referral_url
field extracted by the grok parser.
remote_proxy
intermediary.ip
The value is taken from the
remote_proxy
field extracted by the grok parser.
send_bytes
network.sent_bytes
The value is taken from the
send_bytes
field extracted by the grok parser and converted to an unsigned integer.
sent_bytes
network.sent_bytes
The value is taken from the
sent_bytes
field extracted by the grok parser and converted to an unsigned integer.
server_host
target.hostname, target.asset.hostname
The value is taken from the
server_host
field extracted by the grok parser.
server_ip
target.ip, target.asset.ip
The value is taken from the
server_ip
field extracted by the grok parser.
src_ip
principal.ip, principal.asset.ip
The value is taken from the
src_ip
field extracted by the grok parser.
src_port
principal.port
The value is taken from the
src_port
field extracted by the grok parser and converted to an integer.
user_ip
target.ip, target.asset.ip
The value is taken from the
user_ip
field extracted by the grok parser.
user_mail
principal.user.userid, principal.user.email_addresses
The value is taken from the
user_mail
field extracted by the grok parser.
username
target.user.userid
The value is taken from the
username
field extracted by the grok parser.
-
metadata.event_timestamp
The value is taken from the
create_time
field.
-
metadata.event_type
The value is set to
GENERIC_EVENT
by default, and changed to specific event types based on the parsed log message.
-
metadata.log_type
The value is set to
CISCO_ROUTER
.
-
metadata.product_event_type
The value is taken from the
message_type
field, which is generated by combining the
facility
,
priority
, and
mnemonics
fields.
-
metadata.product_name
The value is set to
Router
.
-
metadata.vendor_name
The value is set to
Cisco
.
-
network.application_protocol
The value is set to
HTTP
or
HTTPS
if the
protocol
field is
http
or
https
, respectively.
-
extensions.auth.type
The value is set to
AUTHTYPE_UNSPECIFIED
by default, and changed to specific authentication types based on the parsed log message.
-
security_result.action
The value is set to
ALLOW
for successful logins and
BLOCK
for failed logins.
-
security_result.category
The value is set to
NETWORK_SUSPICIOUS
for events with IP options and
AUTH_VIOLATION
for failed logins.
-
security_result.description
The value is set to specific messages for different events.
-
security_result.severity
The value is set to
LOW
for successful logins,
MEDIUM
for failed logins, and
INFORMATIONAL
for other events.
-
security_result.severity_details
The value is taken from the
fail_reason
field for failed logins, and set to
Informational message
for events with IP options.
-
security_result.summary
The value is set to specific messages for different events.
Need more help?
Get answers from Community members and Google SecOps professionals.
