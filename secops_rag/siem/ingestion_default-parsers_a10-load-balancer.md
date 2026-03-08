# Collect A10 Network Load Balancer logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/a10-load-balancer/  
**Scraped:** 2026-03-05T09:18:25.913396Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect A10 Network Load Balancer logs
Supported in:
Google secops
SIEM
This document explains how to export A10 Network Load Balancer logs to Google Security Operations using a Bindplane Agent. The parser first uses
grok
patterns to extract relevant fields. Then, it leverages conditional statements (
if
) to map the extracted fields to the unified data model (UDM) based on their presence and content, ultimately categorizing the event type.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to A10 Load Balancer.
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
A10_LOAD_BALANCER
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
Configure Syslog Server in the A10 Load Balancer
Establish an SSH connection to the A10 Load Balancer using an SSH client.
Enter configuration mode by running the following command:
config
Configure the remote syslog server, using the following command:
logging
host
<bindplane-server-ip>
<port-number>
Replace
<bindplane-server-ip>
with the Bindplane IP address and
<port-number>
with the configured in Bindplane; for example,
514
.
Set the
Severity level
, use the following command:
logging
level
information
This will send informational messages (such as warnings and errors) to the Bindplane agent.
Make sure syslog logging is
enabled
by running:
logging
enable
Save the configuration to ensure that it persists after a reboot:
write
memory
Example of a complete CLI configuration:
config
logging
host
192
.168.1.100
514
logging
level
info
logging
enable
write
memory
Supported A10 load balancer log formats
The A10 load balancer parser supports logs in a SYSLOG format.
Supported A10 load balancer Sample Logs
SYSLOG + KV
<
134
>
Jan
25
22
:
11
:
04
LTM_SAN_01
a10logd
:
[
audit
log
]
<
6
>
A
web
session
[
203
]
opened
,
username
:
sanitized_user
,
remote
host
:
0.0.0.0
UDM Mapping Table
Log field
UDM mapping
Logic
dns
additional.fields.dns.value.string_value
The value is taken from the
dns
field extracted by the grok pattern.
dns_server
additional.fields.dns_server.value.string_value
The value is taken from the
dns_server
field extracted by the grok pattern.
gslb
additional.fields.gslb.value.string_value
The value is taken from the
gslb
field extracted by the grok pattern.
host_name
principal.hostname
principal.asset.hostname
The value is taken from the
host_name
field extracted by the grok pattern.
httpmethod
network.http.method
The value is taken from the
httpmethod
field extracted by the grok pattern.
partion_id
additional.fields.partion_id.value.string_value
The value is taken from the
partion_id
field extracted by the grok pattern.
prin_ip
principal.ip
principal.asset.ip
The value is taken from the
prin_ip
field extracted by the grok pattern.
prin_mac
principal.mac
The value is taken from the
prin_mac
field extracted by the grok pattern, with dots removed and colons inserted every two characters.
prin_port
principal.port
The value is taken from the
prin_port
field extracted by the grok pattern and converted to an integer.
proto
network.ip_protocol
The value is taken from the
proto
field extracted by the grok pattern. If the
message
field contains
UDP
, the value is set to
UDP
.
sessionid
network.session_id
The value is taken from the
sessionid
field extracted by the grok pattern.
status_code
network.http.response_code
The value is taken from the
status_code
field extracted by the grok pattern and converted to an integer.
tar_ip
target.ip
target.asset.ip
The value is taken from the
tar_ip
field extracted by the grok pattern.
tar_mac
target.mac
The value is taken from the
tar_mac
field extracted by the grok pattern, with dots removed and colons inserted every two characters.
tar_port
target.port
The value is taken from the
tar_port
field extracted by the grok pattern and converted to an integer.
time
metadata.event_timestamp.seconds
The value is parsed from the
time
field extracted by the grok pattern, using multiple possible date formats.
url
target.url
The value is taken from the
url
field extracted by the grok pattern.
user
principal.user.userid
The value is taken from the
user
field extracted by the grok pattern.
N/A
metadata.event_type
Determined by the parser logic based on the presence of principal and target information:
-
NETWORK_CONNECTION
: if both principal and target information are present.
-
STATUS_UPDATE
: if only principal information is present.
-
GENERIC_EVENT
: otherwise.
N/A
metadata.log_type
Hardcoded to
A10_LOAD_BALANCER
.
N/A
network.application_protocol
Set to
HTTP
if the
proto
field is
HTTP
.
Need more help?
Get answers from Community members and Google SecOps professionals.
