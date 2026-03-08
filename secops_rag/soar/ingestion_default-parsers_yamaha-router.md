# Collect Yamaha router logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/yamaha-router/  
**Scraped:** 2026-03-05T10:02:40.673712Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Yamaha router logs
Supported in:
Google secops
SIEM
This document explains how to ingest Yamaha router logs to Google Security Operations using Bindplane. The parser uses grok patterns to extract fields like timestamp, hostname, user, description, source and destination IP addresses from the syslog messages. It then maps these extracted fields to the UDM, categorizing the event type based on the presence of principal, target, and user information.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the Yamaha router appliance
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
'YAMAHA_ROUTER'
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
Configure Syslog for the Yamaha router
Connect to the router using SSH or CLI.
Set Syslog Host to the Bindplane agent IP:
Default port is
514/UDP
.
Replace
<BINDPLANE_IP>
with the actual Bindplane agent IP address.
syslog
host
<BINDPLANE_IP>
Optional: Set Syslog facility and level:
syslog
facility
local0
syslog
info
Save the configuration to ensure the changes persist after reboot:
save
Enable Syslog output for the required modules
Enable logging for specific features:
Firewall (IP filter) logging:
ip
filter
log
on
NAT logging:
Where 1000 is the NAT descriptor number you're using (adjust as needed).
nat
descriptor
log
on
1000
PPPoE / WAN connection logging:
pppoe
use
log
on
If you use DHCP WAN (instead of PPPoE), log DHCP events:
dhcp
service
log
on
For IPsec VPN logging:
ipsec
log
on
For L2TP and PPTP:
l2tp
log
on
pptp
log
on
Log interface up/down events:
log
state
on
You can also enable logging for ping keepalive if you're using link monitoring:
ping
keepalive
log
on
Enable logging for administrative access (such as SSH or Telnet):
console
notice
ssh
notice
telnet
notice
Log DHCP assignments:
dhcp
service
log
on
DNS logging (if using built-in DNS forwarder):
dns
service
log
on
Mail transfer logging (if using email alerts):
smtp
service
log
on
Dynamic DNS logging:
ddns
service
log
on
NTP events:
ntpdate
log
on
Authentication logging:
auth
log
on
Radius logging:
ppp
use
radius
log
on
Save configuration to ensure changes persist after reboot:
save
UDM Mapping Table
Log Field
UDM Mapping
Logic
data
metadata.description
The description is extracted from the
data
field of the raw log using grok patterns.  Different patterns are used depending on the format of the log message. Examples: "initiate ISAKMP phase", "Connection closed", "succeeded for SSH".
data
metadata.event_timestamp
The timestamp is extracted from the
data
field of the raw log using grok patterns and then converted to a timestamp object using the
date
filter. The
MMM dd HH:mm:ss
and
MMM  d HH:mm:ss
formats are supported.
data
principal.asset.hostname
The hostname is extracted from the
data
field of the raw log using grok patterns.
data
principal.asset.ip
The principal IP address is extracted from the
data
field of the raw log using grok patterns.  It is mapped to both
principal.asset.ip
and
principal.ip
.
data
principal.hostname
The hostname is extracted from the
data
field of the raw log using grok patterns.
data
principal.ip
The principal IP address is extracted from the
data
field of the raw log using grok patterns. It is mapped to both
principal.asset.ip
and
principal.ip
.
data
principal.user.userid
The user ID is extracted from the
data
field of the raw log using grok patterns.
data
target.asset.ip
The target IP address is extracted from the
data
field of the raw log using grok patterns.
data
target.ip
The target IP address is extracted from the
data
field of the raw log using grok patterns. The event type is determined by the parser logic based on the presence of certain fields. If both
principal
and
target
are present, the event type is
NETWORK_CONNECTION
. If
user
is present, the event type is
USER_UNCATEGORIZED
. If only
principal
is present, the event type is
STATUS_UPDATE
. Otherwise, it defaults to
GENERIC_EVENT
. Hardcoded to "YAMAHA_ROUTER". Hardcoded to "YAMAHA_ROUTER". Hardcoded to "YAMAHA_ROUTER".
log_type
metadata.log_type
Copied directly from the
log_type
field of the raw log.
timestamp
timestamp
This is the ingestion time of the log and is added automatically by the Chronicle platform. It's not parsed from the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
