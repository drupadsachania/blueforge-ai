# Collect Arista switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arista-switch/  
**Scraped:** 2026-03-05T09:19:06.301074Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Arista switch logs
Supported in:
Google secops
SIEM
This parser extracts fields from Arista switch logs, handling both JSON and syslog formats. It uses grok patterns to parse various log message types, mapping extracted fields to the UDM and enriching events with metadata like event type, severity, and principal/target information based on extracted details.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Installed and accessible Arista EOS 4.23.x and above.
Ensure that you have privileged access on Arista EOS Switch.
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
ARISTA_SWITCH
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
Configuring Syslog in Arista switch
Sign in to the
Arista
switch.
Go to
configuration
mode:
Arista#
config
terminal
Provide the switch with the following configuration to send logs to the Bindplane agent.
Arista
(
config
)
# logging host <bindplane-server-ip> <port-number> protocol [tcp/udp]
Arista
(
config
)
# logging trap information
Arista
(
config
)
# copy running-config startup-config
*
Replace
`
<
bindplane
-
server
-
ip
>
`
with
Bindplane
agent
IP
address
and
`
<
port
-
number
>
`
with
the
port
configured
to
listen
.
Enter additional configuration for command execution logs:
Arista
(
config
)
# aaa accounting commands all console start-stop logging
Arista
(
config
)
# aaa accounting commands all default start-stop logging
Arista
(
config
)
# aaa accounting exec console start-stop logging
Arista
(
config
)
# aaa accounting exec default start-stop logging
Arista
(
config
)
# copy running-config startup-config
Enter additional configuration for logon logs:
Arista
(
config
)
# aaa authentication policy on-success log
Arista
(
config
)
# aaa authentication policy on-failure log
Arista
(
config
)
# copy running-config startup-config
UDM Mapping Table
Log Field
UDM Mapping
Logic
appname
target.application
Directly mapped from the
appname
field.
description
metadata.description
Directly mapped from the
description
field, which is extracted from the
message
field using grok patterns based on the
product_event_type
.
dst_ip
target.ip
,
target.asset.ip
Directly mapped from the
dst_ip
field, which is extracted from the
message
field using grok patterns.
dst_mac
target.mac
Directly mapped from the
dst_mac
field, which is extracted from the
message
field using grok patterns.
dst_port
target.port
Directly mapped from the
dst_port
field, which is extracted from the
message
field using grok patterns.
facility
additional.fields[facility].string_value
Directly mapped from the
facility
field.
hostname
principal.hostname
,
principal.asset.hostname
Directly mapped from the
hostname
field.
inner_msg
metadata.description
Directly mapped from the
inner_msg
field, which is extracted from the
message
field using grok patterns.
ip_protocol
network.ip_protocol
Directly mapped from the
ip_protocol
field, which is extracted from the
message
field using grok patterns.  If the value is "tcp", it's converted to "TCP". If the event type is "NO_IGMP_QUERIER", it's set to "IGMP".
pid
principal.process.pid
Directly mapped from the
pid
field, which is extracted from the
message
field using grok patterns.
prin_ip
principal.ip
,
principal.asset.ip
Directly mapped from the
prin_ip
field, which is extracted from the
message
field using grok patterns.
product_event_type
metadata.product_event_type
Directly mapped from the
product_event_type
field, which is extracted from the
message
field using grok patterns.
proto
network.application_protocol
If the
proto
field is "sshd", the UDM field is set to "SSH".
severity
security_result.severity
,
security_result.severity_details
The
security_result.severity
is derived from the
severity
field based on these mappings:  "DEFAULT", "DEBUG", "INFO", "NOTICE" -> "INFORMATIONAL"; "WARNING", "ERROR", "ERR", "WARN" -> "MEDIUM"; "CRITICAL", "ALERT", "EMERGENCY" -> "HIGH". The raw value of
severity
is mapped to
security_result.severity_details
.
session_id
network.session_id
Directly mapped from the
session_id
field, which is extracted from the
message
field using grok patterns.
source_ip
principal.ip
,
principal.asset.ip
Directly mapped from the
source_ip
field, which is extracted from the
message
field using grok patterns.
source_port
principal.port
Directly mapped from the
source_port
field, which is extracted from the
message
field using grok patterns.
src_ip
principal.ip
,
principal.asset.ip
Directly mapped from the
src_ip
field, which is extracted from the
message
field using grok patterns.
table_name
target.resource.name
Directly mapped from the
table_name
field, which is extracted from the
message
field using grok patterns. If this field is populated,
target.resource.resource_type
is set to "TABLE".
target_host
target.hostname
,
target.asset.hostname
Directly mapped from the
target_host
field, which is extracted from the
message
field using grok patterns.
target_ip
target.ip
,
target.asset.ip
Directly mapped from the
target_ip
field, which is extracted from the
message
field using grok patterns.
target_package
target.process.command_line
Directly mapped from the
target_package
field, which is extracted from the
message
field using grok patterns.
target_port
target.port
Directly mapped from the
target_port
field, which is extracted from the
message
field using grok patterns.
timestamp
metadata.event_timestamp
Directly mapped from the
timestamp
field after being parsed into a timestamp object.
user
principal.user.userid
Directly mapped from the
user
field, which is extracted from the
message
field using grok patterns.
user_name
target.user.userid
Directly mapped from the
user_name
field, which is extracted from the
message
field using grok patterns.
vrf
additional.fields[vrf].string_value
Directly mapped from the
vrf
field, which is extracted from the
message
field using grok patterns. Derived from a combination of
has_principal
,
has_target
,
user
,
message
,
product_event_type
, and
description
fields using complex conditional logic as described in the parser code. Default value is "GENERIC_EVENT". Hardcoded to "ARISTA_SWITCH". Hardcoded to "Arista Switch". Hardcoded to "Arista". Set to "BLOCK" if the
description
field contains "connection rejected".
dpid
additional.fields[DPID].string_value
Directly mapped from the
dpid
field.
intf
additional.fields[intf].string_value
Directly mapped from the
intf
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
