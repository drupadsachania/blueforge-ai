# Collect Aruba Wireless Controller and Access Point logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-wireless/  
**Scraped:** 2026-03-05T09:19:16.618351Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Aruba Wireless Controller and Access Point logs
Supported in:
Google secops
SIEM
This document explains how to collect Aruba Wireless Controller and Access Point logs by using Bindplane. The parser processes SYSLOG messages, extracting fields related to observer, intermediary, and access point details. It then maps these fields to the Unified Data Model (UDM), enriching the event data with security result severity and handling various error conditions during the process.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to an Aruba Wireless Controller.
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
ARUBA_WIRELESS
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
Configure Aruba Wireless Controller and Access Point
Sign in to the Aruba controller web UI.
Go to the top menu and select
Configuration
>
System
.
Select
Logging
to open the logging configuration page.
In the
Syslog servers
section, click
+ Add
to add a new syslog server.
A new form will appear where you need to enter the following details:
Name
: enter a unique name for the syslog server; for example,
Google SecOps Syslog
.
IP Address
: enter the Bindplane IP address.
Port
: enter the Bindplane port number (typically 514 for UDP).
Logging Facility
: select
local 6
from the menu (this is commonly used for network devices).
Logging Level
: select
Informational
to capture information logs.
Format
: select
bsd-standard
format (this is the default syslog format used by Aruba controllers).
Click
Submit
to save your settings.
Click
Pending Changes
.
Click
Deploy Changes
to apply the new syslog server configuration.
Go to the
Logging Level
settings and set the
Logging Level
to
Informational
for each of the following categories:
Network
All
Cluster
DHCP
GP
Mobility
Packet-Dump
SDN
UDM Mapping Table
Log Field
UDM Mapping
Logic
Additional Info
read_only_udm.security_result.description
The value of
Additional Info
from the raw log is mapped to the UDM field
security_result.description
.
AP
read_only_udm.target.hostname
When present in the raw log, the value after
AP:
is extracted and mapped to the UDM field
target.hostname
.
BSSID
read_only_udm.target.mac
,
read_only_udm.principal.resource.name
(when resource type is BSSID)
The BSSID value from the raw log is mapped to
target.mac
. It's also used as the resource name when the
principal.resource.type
is
BSSID
.
COMMAND
read_only_udm.principal.process.command_line
The command value from the raw log is mapped to the UDM field
principal.process.command_line
.
Dst-MAC
read_only_udm.target.mac
When present, the Dst-MAC value from the raw log is mapped to the UDM field
target.mac
.
SERVER
read_only_udm.target.hostname
When present, the server name from the raw log is mapped to the UDM field
target.hostname
.
SERVER-IP
read_only_udm.target.ip
When present, the server IP from the raw log is mapped to the UDM field
target.ip
.
Src-MAC
read_only_udm.principal.mac
When present, the Src-MAC value from the raw log is mapped to the UDM field
principal.mac
.
SSID
read_only_udm.target.resource.name
(when resource type is SSID)
The SSID value from the raw log is used as the resource name when the
target.resource.type
is
SSID
.
USER
read_only_udm.target.user.userid
When present, the user ID from the raw log is mapped to the UDM field
target.user.userid
.
USERIP
read_only_udm.principal.ip
,
read_only_udm.observer.ip
When present, the user IP from the raw log is mapped to the UDM field
principal.ip
and
observer.ip
.
USERMAC
read_only_udm.principal.mac
When present, the user MAC from the raw log is mapped to the UDM field
principal.mac
.
USERNAME
read_only_udm.principal.user.userid
When present, the username from the raw log is mapped to the UDM field
principal.user.userid
.
action
read_only_udm.security_result.action
The action value from the raw log (e.g.,
permit
,
deny
) is mapped to the UDM field
security_result.action
.
apname
read_only_udm.target.hostname
When present, the AP name from the raw log is mapped to the UDM field
target.hostname
.
bssid
read_only_udm.target.mac
When present, the BSSID value from the raw log is mapped to the UDM field
target.mac
.
collection_time.seconds
read_only_udm.metadata.event_timestamp.seconds
The seconds value of the collection time from the raw log is mapped to the UDM field
metadata.event_timestamp.seconds
.
device_ip
read_only_udm.intermediary.ip
The device IP from the raw log or from
logstash
is mapped to the UDM field
intermediary.ip
.
dstip
read_only_udm.target.ip
When present, the destination IP from the raw log is mapped to the UDM field
target.ip
.
dstport
read_only_udm.target.port
When present, the destination port from the raw log is mapped to the UDM field
target.port
.
event_id
read_only_udm.metadata.product_event_type
The event ID from the raw log is used to construct the
metadata.product_event_type
field in the UDM, prefixed with
Event ID:
.
event_message
read_only_udm.security_result.summary
The event message from the raw log is mapped to the UDM field
security_result.summary
.
log.source.address
read_only_udm.observer.ip
The log source address is mapped to the UDM field
observer.ip
.
log_type
read_only_udm.metadata.log_type
The log type from the raw log is mapped to the UDM field
metadata.log_type
.
logstash.collect.host
read_only_udm.observer.ip
or
read_only_udm.observer.hostname
The logstash collect host is mapped to either
observer.ip
if it's an IP address, or
observer.hostname
if it's a hostname.
logstash.ingest.host
read_only_udm.intermediary.hostname
The logstash ingest host is mapped to the UDM field
intermediary.hostname
.
logstash.process.host
read_only_udm.intermediary.hostname
The logstash process host is mapped to the UDM field
intermediary.hostname
.
program
read_only_udm.target.application
The program name from the raw log is mapped to the UDM field
target.application
.
serverip
read_only_udm.target.ip
When present, the server IP from the raw log is mapped to the UDM field
target.ip
.
servername
read_only_udm.target.hostname
When present, the server name from the raw log is mapped to the UDM field
target.hostname
.
srcip
read_only_udm.principal.ip
When present, the source IP from the raw log is mapped to the UDM field
principal.ip
.
srcport
read_only_udm.principal.port
When present, the source port from the raw log is mapped to the UDM field
principal.port
.
syslog_host
read_only_udm.intermediary.hostname
The syslog host from the raw log is mapped to the UDM field
intermediary.hostname
.
timestamp
read_only_udm.metadata.event_timestamp
The timestamp from the raw log is parsed and mapped to the UDM field
metadata.event_timestamp
.
userip
read_only_udm.principal.ip
,
read_only_udm.observer.ip
When present, the user IP from the raw log is mapped to the UDM field
principal.ip
and
observer.ip
.
usermac
read_only_udm.principal.mac
When present, the user MAC from the raw log is mapped to the UDM field
principal.mac
.
username
read_only_udm.principal.user.userid
When present, the username from the raw log is mapped to the UDM field
principal.user.userid
. Derived from the
event_id
and logic within the parser. Determined by the parser based on the event ID and log message content. Hardcoded to
Wireless
. Hardcoded to
Aruba
. Determined by the parser based on the event ID and log message content. Determined by the parser based on the event ID and log message content. Extracted from the raw log message using regex. Determined by the parser based on the event ID and log message content. An empty object is added when the event_type is USER_LOGIN or a related authentication event. Determined by the parser based on the network protocol used in the event (e.g., TCP, UDP, ICMP, IGMP).  Contains additional fields extracted from the raw log based on specific conditions. For example, the
ap_name
is added as a key-value pair when present. Set to
BSSID
when a BSSID is present in the principal's context. Set to
SSID
when an SSID is present in the target's context.  Contains key-value pairs of relevant detection information extracted from the raw log, such as BSSID or SSID.
Need more help?
Get answers from Community members and Google SecOps professionals.
