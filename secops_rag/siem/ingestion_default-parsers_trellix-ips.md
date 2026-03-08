# Collect Trellix IPS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-ips/  
**Scraped:** 2026-03-05T09:29:21.703049Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trellix IPS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Trellix (formerly McAfee) IPS (Intrusion
Prevention System) Network Security Manager logs to Google Security Operations using
Bindplane. The parser extracts security event data from McAfee IPS syslog messages.
It uses a series of grok patterns to identify and map fields like source and
destination IP, port, protocol, attack details, and severity,
structuring the information into the Google SecOps Unified Data
Model (UDM).
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to McAfee Network Security Platform Manager
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
ingestion_labels
:
log_type
:
'MCAFEE_IPS'
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
Configure McAfee Network Security Platform Manager Syslog
Sign in to the
McAfee Network Security Platform Manager
interface.
Click
Configure
>
Resource Tree
>
IPS Settings
.
Click the
Alert Notification tab
>
Syslog tab
.
Provide the following configuration details:
Select
Yes
to
enable syslog notifications
for McAfee Network Security Platform.
Admin Domain
: Select the
Current
checkbox to send syslog notifications for alerts in the current domain.
Server Name or IP Address
: Enter the Bindplane agent IP address.
UDP Port
: Enter the port
514
.
Facility
: Select syslog facility value
local0
.
Severity
: Select
informational
.
Send Notification If
: Select
all
the options to always receive syslog
IPS Quarantine Alert Notification
: Select
No
.
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
arrow
This field is used in the parser but not mapped to the final UDM.
data
This field is used in the parser but not mapped to the final UDM.
facility
This field is used in the parser but not mapped to the final UDM.
forwarderName
This field is used in the parser but not mapped to the final UDM.
message
This field is used in the parser but not mapped to the final UDM.
principal_ip
read_only_udm.principal.ip
Extracted from the
message
field using a grok pattern.
principal_port
read_only_udm.principal.port
Extracted from the
message
field using a grok pattern.
protocol
This field is used in the parser but not mapped to the final UDM.
result
This field is used in the parser but not mapped to the final UDM.
scanHost
read_only_udm.intermediary.hostname
Extracted from the
message
field using a grok pattern.
severity
This field is used in the parser but not mapped to the final UDM.
sysdate
This field is used in the parser but not mapped to the final UDM.
target_ip
read_only_udm.target.ip
Extracted from the
message
field using a grok pattern.
target_port
read_only_udm.target.port
Extracted from the
message
field using a grok pattern.
is_alert
Set to
true
if the
forwarderName
field contains the word
Alert
.
is_significant
Set to
true
if the
severity
field is
Medium
or
High
.
read_only_udm.metadata.event_timestamp
Copied from the
collection_time
field.
read_only_udm.metadata.event_type
Set to
NETWORK_CONNECTION
by default. Changed to
GENERIC_EVENT
if no IP addresses are found for principal and target.
read_only_udm.metadata.log_type
Set to
MCAFEE_IPS
.
read_only_udm.metadata.product_name
Set to
MCafee IPS
.
read_only_udm.metadata.vendor_name
Set to
MCafee
.
read_only_udm.network.application_protocol
Set to
HTTP
if the
protocol
field is
HTTP
. Set to
HTTPS
if the
protocol
field is
SSL
.
read_only_udm.network.direction
Set to
INBOUND
if the extracted
conn_direction
field is
Inbound
. Set to
OUTBOUND
if the extracted
conn_direction
field is
Outbound
.
read_only_udm.network.ip_protocol
Set to
TCP
if the
protocol
field is
HTTP
,
SSL
, or
TCP
. Set to
ICMP
if the
protocol
field is
ICMP
. Set to
UDP
if the
protocol
field is
SNMP
and the
alert_message
field contains
Empty UDP Attack DoS
.
read_only_udm.security_result.action
Set to
BLOCK
if the
result
field is
Attack Blocked
,
Attack Failed
, or
Attack SmartBlocked
. Set to
ALLOW
if the
result
field is
Attack Successful
. Set to
UNKNOWN_ACTION
if the
result
field is
Inconclusive
. Set to
QUARANTINE
if the
alert_message
field matches the regular expression
File Submitted .*? for Analysis
.
read_only_udm.security_result.category
Categorized based on the
alert_message
field. If the
result
field is
n/a
, it is set to
NETWORK_SUSPICIOUS
.
read_only_udm.security_result.description
The
alert_message
field concatenated with the value of the
_result
variable, which is set to
(result)
if the
result
field is not
n/a
.
read_only_udm.security_result.severity
Mapped from the
severity
field:
Informational
to
INFORMATIONAL
,
Low
to
LOW
,
Medium
to
MEDIUM
,
High
to
HIGH
.
read_only_udm.security_result.summary
The value of the
event_description
variable, which is set to
Detected {attack type}
based on the
message
field.
timestamp
Copied from the
collection_time
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
