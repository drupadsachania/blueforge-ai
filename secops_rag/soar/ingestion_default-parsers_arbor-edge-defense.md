# Collect Arbor Edge Defense logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-edge-defense/  
**Scraped:** 2026-03-05T09:49:55.216747Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Arbor Edge Defense logs
Supported in:
Google secops
SIEM
This document explains how to collect the Netscout (Arbor Edge Defense) logs to Google Security Operations using a Bindplane agent. The parser first extracts fields from raw syslog messages using a grok pattern matching specific vendor-defined formats. Then, it maps the extracted fields and their values to corresponding attributes within the Google SecOps UDM schema, enabling standardized representation and analysis of security events.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Netscout.
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
ARBOR_EDGE_DEFENSE
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
Configure Syslog export on Netscout (Arbor Edge Defense)
Sign in to the
Netscout
web UI.
Select
Administration
>
Notification
>
Groups
.
In the
Notification group
window, click
Add notification group
.
Provide the following configuration details:
Destination
: enter Bindplane agent IP address.
Port
: enter the Bindplane agent port number.
Facility
: select facility
Local0
.
Severity
: select
Informational
.
Click
Save
.
Go to
Administration
>
Configuration Management
>
Commit
, or select
Config Commit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
cn2
principal.group.attribute.labels.value
Mapped if not empty. Part of the conditional logic that involves
cn2Label
.
cn2Label
principal.group.attribute.labels.key
Mapped if
cn2
is not empty.
cs2
principal.group.attribute.labels.value
Mapped if not empty. Part of the conditional logic that involves
cs2Label
.
cs2Label
principal.group.attribute.labels.key
Mapped if
cs2
is not empty.
cs3
security_result.detection_fields.value
Mapped if not empty. Part of the conditional logic that involves
cs3Label
.
cs3Label
security_result.detection_fields.key
Mapped if
cs3
is not empty.
cs6
security_result.threat_name
Mapped if not empty.
cs7
security_result.category_details
Concatenated with the prefix
Threat Category:
if not empty.
dpt
target.port
Converted to integer and mapped if not empty or
0
.
dst
target.ip
Mapped if not empty.
msg
metadata.description
Mapped directly.
principal.group.attribute.labels.key
Set to
Traffic Level
if
traffic_level
(extracted from
msg
) is not empty.
principal.group.attribute.labels.value
Set to the extracted
traffic_level
from
msg
if not empty.
principal.group.attribute.labels.key
Set to
Protection Group Name
if
group_name
(extracted from
msg
) is not empty.
principal.group.attribute.labels.value
Set to the extracted
group_name
from
msg
if not empty.
proto
network.ip_protocol
Converted to uppercase and mapped if value is
TCP
or
UDP
.
rt
metadata.event_timestamp.seconds
Converted to timestamp using date filter.
src
principal.ip
Mapped if not empty.
spt
principal.port
Converted to integer and mapped if not empty or
0
.
metadata.log_type
Hardcoded to
ARBOR_EDGE_DEFENSE
.
metadata.vendor_name
Hardcoded to
NETSCOUT
.
metadata.product_name
Hardcoded to
ARBOR_EDGE_DEFENSE
.
metadata.product_version
Extracted from
device_version
field from CEF header.
metadata.product_event_type
Extracted from
event_name
field from CEF header.
intermediary.hostname
Extracted from
intermediary_hostname
field from CEF header.
security_result.rule_name
Extracted from
security_rule_name
field from CEF header.
security_result.action
Set to
BLOCK
if
event_name
is
Blocked Host
.
security_result.action_details
Set to value of
event_name
if
event_name
is
Blocked Host
.
security_result.severity
Mapped from
severity
field based on predefined logic and converted to uppercase.
metadata.event_type
Set to
NETWORK_CONNECTION
if both
dst
and
src
are not empty, set to
STATUS_UPDATE
if only
src
is not empty, otherwise defaults to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
