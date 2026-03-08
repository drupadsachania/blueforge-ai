# Collect Juniper NetScreen Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-firewall/  
**Scraped:** 2026-03-05T09:25:56.676025Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Juniper NetScreen Firewall logs
Supported in:
Google secops
SIEM
This document explains how to set up Juniper NetScreen Firewall logs to be sent to Google Security Operations. The parser extracts fields using grok patterns, handling various syslog formats and JSON payloads. It then maps these extracted fields to the UDM, categorizing events as network connections, user logins, status updates, or generic events based on the presence of specific fields like IP addresses, usernames, and ports.
Before you begin
Ensure that you have administrative access to your Juniper NetScreen Firewall.
Ensure that you have a Google Security Operations instance.
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:54525"
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
SYSLOG
namespace
:
juniper_firewall
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
tcplog
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
Configure Juniper Networks NetScreen firewall
Sign in to the
Juniper NetScreen
web interface.
Select
Configuration
>
Report settings
>
Log settings
.
Select all the
Event severity
checkboxes.
Click
Apply
.
Select
Configuration
>
Report settings
>
Syslog
.
Select the
Enable syslog messages
checkbox.
In the
Source interface
list, select the
NetScreen
interface from which the syslog packets need to be sent.
In the
Syslog servers
section, select the
Enable
checkbox and provide the following:
IP/Hostname
: enter the
Bindplane
IP address.
Port
: enter the
Bindplane
port number.
MDR facility
: select
Local0
facility level.
Facility
: select
Local0
facility level.
Click
Apply
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ACTION
security_result.action_details
Directly mapped from the
ACTION
field extracted via GROK and KV filters.
APPLICATION
principal.application
Directly mapped from the
APPLICATION
field extracted via GROK and KV filters.
application
target.application
Directly mapped from the
application
field extracted via GROK.
attack-name
security_result.threat_name
Directly mapped from the
attack-name
field extracted via GROK.
bytes-from-client
network.sent_bytes
Directly mapped from the
bytes-from-client
field extracted via GROK.
bytes-from-server
network.received_bytes
Directly mapped from the
bytes-from-server
field extracted via GROK.
command
target.process.command_line
Directly mapped from the
command
field extracted via GROK.
destination-address
target.ip
Directly mapped from the
destination-address
field extracted via GROK.
destination-port
target.port
Directly mapped from the
destination-port
field extracted via GROK.
destination-zone
additional.fields[].value.string_value
Directly mapped from the
destination-zone
field extracted via GROK and KV filters. The
key
is set to
destination-zone
.
destination_zone-name
security_result.detection_fields[].value
Directly mapped from the
destination_zone-name
field extracted via GROK. The
key
is set to
dstzone
.
dst-nat-rule-name
security_result.detection_fields[].value
Directly mapped from the
dst-nat-rule-name
field extracted via GROK. The
key
is set to
dst-nat-rule-name
.
dst-nat-rule-type
security_result.detection_fields[].value
Directly mapped from the
dst-nat-rule-type
field extracted via GROK. The
key
is set to
dst-nat-rule-type
.
elapsed-time
network.session_duration.seconds
Directly mapped from the
elapsed-time
field extracted via GROK.
encrypted
security_result.detection_fields[].value
Directly mapped from the
encrypted
field extracted via GROK. The
key
is set to
encrypted
.
event_time
metadata.event_timestamp
The timestamp is extracted from the raw log using various GROK patterns, prioritizing
event_time
, then
TIMESTAMP_ISO8601
, and finally
SYSLOGTIMESTAMP
. It is then converted to a timestamp object.
host
principal.hostname
,
intermediary.hostname
If
type
is
NetScreen
, mapped to
intermediary.hostname
. Otherwise, mapped to
principal.hostname
.
host_ip
intermediary.ip
Directly mapped from the
host_ip
field extracted via GROK.
icmp-type
network.icmp_type
Directly mapped from the
icmp-type
field extracted via GROK.
ident
target.application
Directly mapped from the
ident
field extracted via GROK and JSON filters.
inbound-bytes
network.received_bytes
Directly mapped from the
inbound-bytes
field extracted via GROK.
inbound-packets
network.received_packets
Directly mapped from the
inbound-packets
field extracted via GROK.
ip
principal.ip
,
intermediary.ip
If
type
is
NetScreen
, mapped to
intermediary.ip
. Otherwise, mapped to
principal.hostname
.
message
security_result.description
If the message is JSON and the
log_message_data
field is not present, the
message
field is used as the description.
msg_data
security_result.summary
Directly mapped from the
msg_data
field extracted via GROK.
nat-destination-address
target.nat_ip
Directly mapped from the
nat-destination-address
field extracted via GROK.
nat-destination-port
target.nat_port
Directly mapped from the
nat-destination-port
field extracted via GROK.
nat-source-address
principal.nat_ip
Directly mapped from the
nat-source-address
field extracted via GROK.
nat-source-port
principal.nat_port
Directly mapped from the
nat-source-port
field extracted via GROK.
outbound-bytes
network.sent_bytes
Directly mapped from the
outbound-bytes
field extracted via GROK.
outbound-packets
network.sent_packets
Directly mapped from the
outbound-packets
field extracted via GROK.
packets-from-client
network.sent_packets
Directly mapped from the
packets-from-client
field extracted via GROK.
packets-from-server
network.received_packets
Directly mapped from the
packets-from-server
field extracted via GROK.
packet-incoming-interface
security_result.detection_fields[].value
Directly mapped from the
packet-incoming-interface
field extracted via GROK. The
key
is set to
packet-incoming-interface
.
pid
target.process.pid
Directly mapped from the
pid
field extracted via GROK and JSON filters.
policy-name
security_result.rule_name
Directly mapped from the
policy-name
field extracted via GROK.
PROFILE
additional.fields[].value.string_value
Directly mapped from the
PROFILE
field extracted via GROK and KV filters. The
key
is set to
PROFILE
.
protocol-id
,
protocol-name
network.ip_protocol
Mapped from the
protocol-id
or
protocol-name
field extracted via GROK. The value is converted to the corresponding IP protocol enum.
REASON
additional.fields[].value.string_value
Directly mapped from the
REASON
field extracted via GROK and KV filters. The
key
is set to
REASON
.
reason
security_result.description
Directly mapped from the
reason
field extracted via GROK.
rule-name
security_result.rule_name
Directly mapped from the
rule-name
field extracted via GROK.
SESSION_ID
network.session_id
Directly mapped from the
SESSION_ID
field extracted via GROK and KV filters.
service-name
security_result.detection_fields[].value
Directly mapped from the
service-name
field extracted via GROK. The
key
is set to
srvname
.
source-address
principal.ip
Directly mapped from the
source-address
field extracted via GROK.
source-port
principal.port
Directly mapped from the
source-port
field extracted via GROK.
source-zone
additional.fields[].value.string_value
Directly mapped from the
source-zone
field extracted via GROK and KV filters. The
key
is set to
source-zone
.
source_zone-name
security_result.detection_fields[].value
Directly mapped from the
source_zone-name
field extracted via GROK. The
key
is set to
srczone
.
src-nat-rule-name
security_result.detection_fields[].value
Directly mapped from the
src-nat-rule-name
field extracted via GROK. The
key
is set to
src-nat-rule-name
.
src-nat-rule-type
security_result.detection_fields[].value
Directly mapped from the
src-nat-rule-type
field extracted via GROK. The
key
is set to
src-nat-rule-type
.
subtype
metadata.product_event_type
Directly mapped from the
subtype
field extracted via GROK.
threat-severity
security_result.severity_details
Directly mapped from the
threat-severity
field extracted via GROK.
time
metadata.event_timestamp
Directly mapped from the
time
field extracted via GROK and JSON filters. Converted to timestamp object.
username
target.user.userid
Directly mapped from the
username
field extracted via GROK.
metadata.log_type
Hardcoded to
JUNIPER_FIREWALL
. Hardcoded to
JUNIPER_FIREWALL
or
NetScreen
based on the
type
field. Hardcoded to
JUNIPER_FIREWALL
. Set to ALLOW or BLOCK based on logic in the parser. Set to LOW, MEDIUM, HIGH, INFORMATIONAL, or CRITICAL based on the
subtype
and
severity_details
fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
