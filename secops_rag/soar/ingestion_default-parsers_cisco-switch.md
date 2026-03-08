# Collect Cisco switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-switch/  
**Scraped:** 2026-03-05T09:52:40.061880Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco switch logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco switch logs to Google Security Operations using a Bindplane agent. The parser extracts fields from SYSLOG messages, mapping them to a unified data model (UDM) based on identified patterns and keywords. It handles a wide range of events, including DHCP, SSH, login attempts, network traffic, and system status updates, categorizing them and enriching the data with relevant security details.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to a Cisco switch.
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
CISCO_SWITCH
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
Configure Syslog on a Cisco switch
Sign in to the Cisco Switch.
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
with the Bindplane Agent IP address, and
<port-number>
with the configured port.
Replace
<tcp/udp>
with the configured listening protocol on the Bindplane Agent. (For example,
udp
).
Replace
<interface>
with the Cisco interface ID.
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
action
security_result.action_details
Value of this field is derived from the
action
field in the raw log.
day
description
metadata.description
Value of this field is derived from the
description
field in the raw log.
description
security_result.description
Value of this field is derived from the
description
field in the raw log.
destination_ip
target.asset.ip
Value of this field is derived from the
destination_ip
field in the raw log.
destination_ip
target.ip
Value of this field is derived from the
destination_ip
field in the raw log.
destination_port
target.port
Value of this field is derived from the
destination_port
field in the raw log.
device
principal.asset.hostname
Value of this field is derived from the
device
field in the raw log.
device
principal.hostname
Value of this field is derived from the
device
field in the raw log.
device
target.asset.hostname
Value of this field is derived from the
device
field in the raw log.
device
target.hostname
Value of this field is derived from the
device
field in the raw log.
device_ip
principal.asset.ip
Value of this field is derived from the
device_ip
field in the raw log.
device_ip
principal.ip
Value of this field is derived from the
device_ip
field in the raw log.
device_ip
target.asset.ip
Value of this field is derived from the
device_ip
field in the raw log.
device_ip
target.ip
Value of this field is derived from the
device_ip
field in the raw log.
facility
principal.resource.type
Value of this field is derived from the
facility
field in the raw log.
header_data
metadata.product_log_id
Value of this field is derived from the
header_data
field in the raw log.
header_data
target.asset.ip
Value of this field is derived from the
header_data
field in the raw log.
header_data
target.ip
Value of this field is derived from the
header_data
field in the raw log.
hostname
principal.asset.hostname
Value of this field is derived from the
hostname
field in the raw log.
hostname
principal.hostname
Value of this field is derived from the
hostname
field in the raw log.
ip
principal.asset.ip
Value of this field is derived from the
ip
field in the raw log.
ip
principal.ip
Value of this field is derived from the
ip
field in the raw log.
ip_address
principal.asset.ip
Value of this field is derived from the
ip_address
field in the raw log.
ip_address
principal.ip
Value of this field is derived from the
ip_address
field in the raw log.
ip_protocol
network.ip_protocol
Value of this field is derived from the
ip_protocol
field in the raw log.
mac
principal.mac
Value of this field is derived from the
mac
field in the raw log.
mnemonic
network.dhcp.opcode
Value of this field is derived from the
mnemonic
field in the raw log.
mnemonic
metadata.product_event_type
Value of this field is derived from the
mnemonic
field in the raw log.
month
p_ip
principal.asset.ip
Value of this field is derived from the
p_ip
field in the raw log.
p_ip
principal.ip
Value of this field is derived from the
p_ip
field in the raw log.
port
target.port
Value of this field is derived from the
port
field in the raw log.
priority
protocol
network.ip_protocol
Value of this field is derived from the
protocol
field in the raw log.
reason
rule
security_result.rule_id
Value of this field is derived from the
rule
field in the raw log.
sec_result_action
security_result.action
Value of this field is derived from the
sec_result_action
field in the raw log.
severity
source
principal.asset.ip
Value of this field is derived from the
source
field in the raw log.
source
principal.ip
Value of this field is derived from the
source
field in the raw log.
source_ip
network.dhcp.ciaddr
Value of this field is derived from the
source_ip
field in the raw log.
source_ip
principal.asset.ip
Value of this field is derived from the
source_ip
field in the raw log.
source_ip
principal.ip
Value of this field is derived from the
source_ip
field in the raw log.
source_mac
network.dhcp.chaddr
Value of this field is derived from the
source_mac
field in the raw log.
source_port
principal.port
Value of this field is derived from the
source_port
field in the raw log.
summary
security_result.summary
Value of this field is derived from the
summary
field in the raw log.
time
timezone
user
principal.user.userid
Value of this field is derived from the
user
field in the raw log.
user
target.user.userid
Value of this field is derived from the
user
field in the raw log.
when
year
extensions.auth.type
MACHINE
metadata.log_type
CISCO_SWITCH
metadata.vendor_name
Cisco
metadata.product_name
Cisco Switch
network.application_protocol
DHCP
network.dhcp.type
REQUEST
Need more help?
Get answers from Community members and Google SecOps professionals.
