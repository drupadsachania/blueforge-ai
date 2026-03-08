# Collect VyOS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vyos/  
**Scraped:** 2026-03-05T09:30:13.881056Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VyOS logs
Supported in:
Google secops
SIEM
This document explains how to ingest VyOS logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages, primarily focusing on DHCP events. It uses grok patterns to identify and categorize messages based on the process (dhcpd, kernel, etc.), then maps relevant information to UDM fields, handling DHCP requests, acknowledgments, offers, and other event types differently. It also populates generic event details for non-DHCP logs and maps network connection information when available.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to VyOS
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
For additional installation options, consult the
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
'VYOS'
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
Configure Syslog on VyOS
Sign in to the VyOS router using CLI.
Enter the following commands:
set
system
syslog
marker
interval
1200
set
system
syslog
remote
<bindplane-address>
facility
local0
level
info
port
<bindolane-port>
protocol
<udp-or-tcp>
format
include-timezone
Make sure to replace the following fields with your details:
<bindplane-address>
: Enter the Bindplane agent IP address.
<bindolane-port>
: Enter the Bindplane agent port number (for example,
514
).
<udp-or-tcp>
: Enter either UDP or TCP, depending on your Bindplane configuration (for example,
UDP
).
UDM Mapping Table
Log Field
UDM Mapping
Logic
clientIp
principal.ip
Client IP address extracted from the DHCP message.
clientMac
principal.mac
Client MAC address extracted from the DHCP message.
datetime
metadata.event_timestamp
The timestamp extracted from the log message.
dst_ipaddress
target.ip
Destination IP address extracted from the log message.
hostname
observer.hostname
Hostname extracted from the log message. Determined by the parser based on the
process
and other fields. Can be
GENERIC_EVENT
,
NETWORK_CONNECTION
,
NETWORK_DHCP
, or
STATUS_UPDATE
. Hardcoded to "VYOS".
msg
metadata.description
The original message from the log, or a portion of it, depending on the parsing logic. Set to "DHCP Event" if the
process
is "dhcpd". Hardcoded to "VYOS DHCP". Hardcoded to "VYOS".
network.dhcp.chaddr
network.dhcp.chaddr
Client MAC address extracted from DHCP messages.
network.dhcp.ciaddr
network.dhcp.ciaddr
Client IP address in a DHCPREQUEST message. DHCP message opcode. Set to "BOOTREQUEST" for DHCPREQUEST and DHCPINFORM, "BOOTREPLY" for DHCPACK and DHCPNAK. DHCP message type. Derived from
eventType
and can be
REQUEST
,
ACK
,
INFORM
,
NAK
, or
OFFER
.
network.dhcp.yiaddr
network.dhcp.yiaddr
Your (client) IP address in a DHCPACK or DHCPOFFER message. Set to "DHCP" if the
process
is "dhcpd".
pri_host
principal.hostname
Hostname associated with a client in DHCP messages.
rem_msg
metadata.description
Remaining part of the message after initial parsing, used for description in some cases.
src_ipaddress
principal.ip
Source IP address extracted from the log message.
timestamp
event.timestamp
The timestamp of the log entry.
Need more help?
Get answers from Community members and Google SecOps professionals.
