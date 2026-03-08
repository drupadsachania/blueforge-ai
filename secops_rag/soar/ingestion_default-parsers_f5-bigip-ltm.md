# Collect F5 BIG-IP LTM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-ltm/  
**Scraped:** 2026-03-05T09:55:27.489339Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 BIG-IP LTM logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 BIG-IP LTM logs to Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Administrative access to the F5 BIG-IP LTM device (TMSH or web UI)
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
# UDP syslog listener (RFC5424 over UDP)
udplog
:
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
"/opt/observiq-otel-collector/ingestion-auth.json"
# Replace with your actual customer ID from Step 2
customer_id
:
"<YOUR_CUSTOMER_ID>"
# Select the appropriate regional endpoint based on where your Google SecOps instance is provisioned
# For regional endpoints, see: [https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints](https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints)
endpoint
:
"<YOUR_REGIONAL_ENDPOINT>"
# Set the log_type to ensure the correct parser is applied
log_type
:
"F5_BIGIP_LTM"
raw_log_field
:
body
# You can optionally add other custom ingestion labels here if needed
ingestion_labels
:
service
:
pipelines
:
logs/f5ltm
:
receivers
:
[
udplog
]
exporters
:
[
chronicle/chronicle_w_labels
]
The
listen_address
is set to
0.0.0.0:514
to accept syslog from any source. Adjust if you need to restrict to specific interfaces.
UDP port 514 is the standard syslog port. If port 514 requires root privileges, you may use a port above 1024 (for example,
5514
) and adjust F5 configuration accordingly.
For TCP instead of UDP, create a
tcplog
receiver and set the F5 Remote High-Speed Log protocol to
tcp
.
Save the file and exit the editor.
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
Configure F5 BIG-IP LTM syslog forwarding
Option A: Using TMSH (Command Line Interface)
Create pool for syslog destination
Connect to the F5 BIG-IP LTM device via SSH.
Run the following commands:
tmsh
create
ltm
pool
f5_syslog_pool
members
add
{
<BINDPLANE_IP>:514
}
monitor
gateway_icmp
Replace
<BINDPLANE_IP>
with the IP address of your Bindplane agent host.
Create log destination
tmsh
create
sys
log-config
destination
remote-high-speed-log
f5_hsl_dest
protocol
udp
pool-name
f5_syslog_pool

tmsh
create
sys
log-config
destination
remote-syslog
f5_remote_syslog_dest
format
rfc5424
remote-high-speed-log
f5_hsl_dest
Create log publisher
tmsh
create
sys
log-config
publisher
f5_log_publisher
destinations
add
{
f5_remote_syslog_dest
}
Create request logging profile
tmsh
create
ltm
profile
request-log
f5_ltm_request_log
\
request-log-pool
f5_syslog_pool
request-log-protocol
mds-udp
\
request-log-template
'event_source="request_logging",hostname="$BIGIP_HOSTNAME",client_ip="$CLIENT_IP",server_ip="$SERVER_IP",http_method="$HTTP_METHOD",http_uri="$HTTP_URI",http_host="${host}",virtual_name="$VIRTUAL_NAME",event_timestamp="$DATE_HTTP"'
\
request-logging
enabled
\
response-log-pool
f5_syslog_pool
response-log-protocol
mds-udp
\
response-log-template
'event_source="response_logging",hostname="$BIGIP_HOSTNAME",client_ip="$CLIENT_IP",server_ip="$SERVER_IP",http_method="$HTTP_METHOD",http_uri="$HTTP_URI",http_host="${host}",virtual_name="$VIRTUAL_NAME",http_statcode="$HTTP_STATCODE",event_timestamp="$DATE_HTTP"'
\
response-logging
enabled
Apply logging profile to virtual server
tmsh
modify
ltm
virtual
<VIRTUAL_SERVER_NAME>
profiles
add
{
f5_ltm_request_log
}
Replace
<VIRTUAL_SERVER_NAME>
with the name of your virtual server.
Save configuration
tmsh
save
sys
config
Option B: Using F5 Web UI (Configuration Utility)
Create pool for syslog destination
Sign in to the
F5 BIG-IP LTM
web interface.
Go to
Local Traffic
>
Pools
>
Pool List
.
Click
Create
.
Provide the following configuration details:
Name
: Enter
f5_syslog_pool
.
Health Monitors
: Select
gateway_icmp
.
In the
Resources
section, under
New Members
:
Address
: Enter the Bindplane Agent IP address.
Service Port
: Enter
514
.
Click
Add
.
Click
Finished
.
Create remote high-speed log destination
Go to
System
>
Logs
>
Configuration
>
Log Destinations
.
Click
Create
.
Provide the following configuration details:
Name
: Enter
f5_hsl_dest
.
Type
: Select
Remote High-Speed Log
.
Protocol
: Select
UDP
.
Pool Name
: Select
f5_syslog_pool
.
Click
Finished
.
Create remote syslog destination
Go to
System
>
Logs
>
Configuration
>
Log Destinations
.
Click
Create
.
Provide the following configuration details:
Name
: Enter
f5_remote_syslog_dest
.
Type
: Select
Remote Syslog
.
Syslog Format
: Select
RFC5424
.
Remote High-Speed Log
: Select
f5_hsl_dest
.
Click
Finished
.
Create log publisher
Go to
System
>
Logs
>
Configuration
>
Log Publishers
.
Click
Create
.
Provide the following configuration details:
Name
: Enter
f5_log_publisher
.
Destinations
: Move
f5_remote_syslog_dest
from
Available
to
Selected
.
Click
Finished
.
Create request logging profile
Go to
Local Traffic
>
Profiles
>
Other
>
Request Logging
.
Click
Create
.
Provide the following configuration details:
Name
: Enter
f5_ltm_request_log
.
Parent Profile
: Select
request-log
.
Under
Request Settings
:
Request Logging
: Select
Enabled
.
Request Log Protocol
: Select
mds-udp
.
Request Log Pool
: Select
f5_syslog_pool
.
Request Log Template
: Enter the following:
event_source="request_logging",hostname="
$BIGIP_HOSTNAME
",client_ip="
$CLIENT_IP
",server_ip="
$SERVER_IP
",http_method="
$HTTP_METHOD
",http_uri="
$HTTP_URI
",http_host="
${
host
}
",virtual_name="
$VIRTUAL_NAME
",event_timestamp="
$DATE_HTTP
"
Under
Response Settings
:
Response Logging
: Select
Enabled
.
Response Log Protocol
: Select
mds-udp
.
Response Log Pool
: Select
f5_syslog_pool
.
Response Log Template
: Enter the following:
event_source="response_logging",hostname="
$BIGIP_HOSTNAME
",client_ip="
$CLIENT_IP
",server_ip="
$SERVER_IP
",http_method="
$HTTP_METHOD
",http_uri="
$HTTP_URI
",http_host="
${
host
}
",virtual_name="
$VIRTUAL_NAME
",http_statcode="
$HTTP_STATCODE
",event_timestamp="
$DATE_HTTP
"
Click
Finished
.
Apply request logging profile to virtual server
Go to
Local Traffic
>
Virtual Servers
>
Virtual Server List
.
Click the virtual server name.
Go to the
Resources
tab.
Under
iRules and Profiles
, click
Manage
next to
Profiles
.
Under
Available
, locate
f5_ltm_request_log
and move it to
Selected
.
Click
Finished
.
Click
Update
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
hostname
principal.hostname
Syslog hostname (device that emitted the log)
client_ip
principal.ip
Source IP address of the client
client_port
principal.port
Source port (if included in template)
server_ip
target.ip
Destination IP (pool member)
server_port
target.port
Destination port (pool member)
http_method
network.http.method
HTTP request method
http_uri
network.http.url
HTTP request URI (including path/query if present)
http_host
network.http.host
HTTP Host header
http_statcode
network.http.response_code
HTTP response status code
user_agent
network.http.user_agent
User-Agent header
virtual_name
target.application
Name of the F5 virtual server
event_timestamp
metadata.event_timestamp
Event time from device
event_source
metadata.product_event_type
Event type tag (request_logging, response_logging)
Need more help?
Get answers from Community members and Google SecOps professionals.
