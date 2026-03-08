# Collect Array Networks SSL VPN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arraynetworks-vpn/  
**Scraped:** 2026-03-05T09:19:10.474627Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Array Networks SSL VPN logs
Supported in:
Google secops
SIEM
This document explains how to ingest Array Networks SSL VPN logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages, mapping them to the UDM. It uses grok patterns to identify various log formats, including HTTP requests, SSL messages, and generic status updates, then conditionally parses key-value pairs and CSV data within the messages to populate UDM fields like principal, target, network information, and security results. The parser also handles different event types based on the extracted data, categorizing them as network events, user events, or generic events.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Array Networks SSL VPN management console or appliance (AG Series or vxAG)
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
'ARRAYNETWORKS_VPN'
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
Configure Syslog forwarding on Array Networks SSL VPN
Sign in to the
Array Networks SSL VPN Management Console
web UI.
In the left navigation menu, click
ADMIN TOOLS
.
Click
Monitoring
.
Click the
Logging
tab.
Click the
Syslog Servers
sub-tab.
In the
REMOTE SYSLOG SERVER CONFIGURATION
section, click
Add Server Entry
.
Provide the following configuration details:
Host IP
: Enter the Bindplane agent IP address.
Host Port
: Enter the Bindplane agent port number (for example,
514
).
Protocol
: Select
UDP
or
TCP
, depending on your Bindplane agent configuration.
Source Port
: Leave default or specify if required by your network configuration.
Level
: Select
Informational
.
Click
Save
to apply the configuration.
Click
Save Configuration
at the top of the page to persist the changes.
UDM Mapping Table
Log Field
UDM Mapping
Logic
clientip
principal.ip
The client's IP address extracted from the
clientip
field in the raw log message.
column1
principal.ip
IP address extracted from
column1
in the raw log.
column1
principal.asset.ip
IP address extracted from
column1
in the raw log.
column3
network.received_bytes
The number of received bytes, converted to an unsigned integer.
column4
network.http.method
The HTTP method extracted from
column4
in the raw log.
column7
target.ip
The target IP address extracted from
column7
in the raw log.
dport
target.port
Destination port, converted to an integer.
dst
target.ip
Destination IP address.
dst
target.asset.ip
Destination IP address.
hostname
principal.hostname
The hostname extracted from the
hostname
field in the raw log message.
hostname
principal.asset.hostname
The hostname extracted from the
hostname
field in the raw log message.
http_method
network.http.method
The HTTP method extracted from the raw log message.
id
principal.application
The application ID from the raw log.
mac
principal.mac
The MAC address extracted from the
mac
field in the raw log message.
msg
metadata.product_event_type
The message field from the raw log, used as the product event type. Also used for
security_result.description
after removing backslashes and quotes.
product_name
metadata.product_name
The product name extracted from the raw log message.
prxy_ip
intermediary.ip
Proxy IP address.
prxy_port
intermediary.port
Proxy port, converted to an integer.
response_code
network.http.response_code
The HTTP response code, converted to an integer.
security_result.action
security_result.action
Determined by the parser logic based on the value of
column2
.  "BLOCK" if
column2
contains "TCP_MISS", "UNKNOWN_ACTION" otherwise.
security_result.description
security_result.description
The message field from the raw log, after removing backslashes and quotes.
sport
principal.port
Source port, converted to an integer.
src
principal.ip
Source IP address.
src
principal.asset.ip
Source IP address.
target_hostname
target.hostname
The target hostname extracted from the raw log message.
timestamp
metadata.event_timestamp
The timestamp extracted from the raw log message and parsed into a timestamp object.
uri
target.url
Part of the target URL. Combined with
uri_param
to form the complete URL.
uri_param
target.url
Part of the target URL. Combined with
uri
to form the complete URL.
user
target.user.userid
The username extracted from the raw log message.
user_agent_string
network.http.user_agent
The user agent string extracted from the raw log message.
vpn
target.user.group_identifiers
The VPN name extracted from the raw log message.
metadata.event_type
metadata.event_type
Determined by the parser logic based on a combination of fields like
has_principal
,
has_target
,
has_http_value
, and
user
. Can be "NETWORK_HTTP", "NETWORK_CONNECTION", "STATUS_UPDATE", "USER_UNCATEGORIZED", or "GENERIC_EVENT".
network.ip_protocol
network.ip_protocol
Set to "TCP" if the message contains "TCP".
Need more help?
Get answers from Community members and Google SecOps professionals.
