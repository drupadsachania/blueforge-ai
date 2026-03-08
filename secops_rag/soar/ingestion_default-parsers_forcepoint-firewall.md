# Collect Forcepoint NGFW logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-firewall/  
**Scraped:** 2026-03-05T09:56:02.682467Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forcepoint NGFW logs
Supported in:
Google secops
SIEM
This document explains how toingest Forcepoint NGFW logs to Google Security Operations using Bindplane. The parser extracts fields from the JSON logs or CEF formatted messages, normalizes them into the Unified Data Model (UDM), and enriches the data with vendor and product metadata. It handles both JSON and CEF formatted logs, using grok patterns and conditional logic to map raw log fields to UDM fields, including network connection details, security results, and metadata.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Forcepoint Security Management Center (SMC)
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
tcplog
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
YOUR_CUSTOMER_ID
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'FORCEPOINT_FIREWALL'
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
tcplog
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
Configure Syslog forwarding on Forcepoint NGFW
Sign in to the
Forcepoint Security Management Center (SMC)
.
Go to
Configuration
>
Log Server
>
Properties
.
Navigate to the
Log Forwarding
section.
Click
Add
to create a new forwarding rule.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps BindPlane Syslog
).
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (for example,
514
).
Protocol
: Select
TCP
or
UDP
, depending on your actual Bindplane agent configuration.
Format
: Select
JSON
.
Configure the log fields to forward:
Click
Select Fields
or access the field selection configuration.
Select the relevant log fields according to your requirements. The following fields are commonly required for security analysis:
TIMESTAMP
(Creation Time)
LOG_ID
(Data Identifier)
EVENT
(Event)
EVENT_ID
(Event ID)
SRC
(Source Address)
DST
(Destination Address)
Sport
(Source Port)
Dport
(Destination Port)
PROTOCOL
(Protocol)
SERVICE
(Service)
RULE_ID
(Rule Tag)
ACTION
(Action)
NAT_SRC
,
NAT_DST
,
NAT_SPORT
,
NAT_DPORT
(NAT fields)
ACC_RX_BYTES
,
ACC_TX_BYTES
,
ACC_ELAPSED
(Accounting fields)
NODE_ID
(Sender)
COMP_ID
(Component ID)
FACILITY
(Facility)
INFO_MSG
(Information Message)
SITUATION
(Situation)
APPLICATION
(Application)
For a complete list of exportable fields, refer to the
Forcepoint NGFW Exportable Firewall and Layer 2 Firewall log entry fields
documentation.
Go to the
Events
section and select
all
.
Save the configuration.
Apply the changes to the Log Server.
UDM Mapping Table
Log Field
UDM Mapping
Logic
AccElapsed
network.session_duration.seconds
Directly mapped from
AccElapsed
if not empty or 0. Converted to integer.
AccRxBytes
network.received_bytes
Directly mapped from
AccRxBytes
. Converted to unsigned integer.
AccTxBytes
network.sent_bytes
Directly mapped from
AccTxBytes
. Converted to unsigned integer.
Action
security_result.action_details
Directly mapped from
Action
.
Action
security_result.action
If
Action
is "Allow", set to "ALLOW". If
Action
is "Discard", set to "BLOCK".
CompId
target.hostname
Directly mapped from
CompId
.
Dport
target.port
Directly mapped from
Dport
if not 0. Converted to integer.
Dst
target.ip
Directly mapped from
Dst
.
Event
metadata.product_event_type
Directly mapped from
Event
.
Facility
metadata.description
Directly mapped from
Facility
.
InfoMsg
security_result.description
Directly mapped from
InfoMsg
.
LogId
metadata.product_log_id
Directly mapped from
LogId
.
NatDport
target.nat_port
Directly mapped from
NatDport
if not 0. Converted to integer.
NatDst
target.nat_ip
Directly mapped from
NatDst
.
NatSport
principal.nat_port
Directly mapped from
NatSport
if not 0. Converted to integer.
NatSrc
principal.nat_ip
Directly mapped from
NatSrc
.
NodeId
intermediary.ip
Directly mapped from
NodeId
if both
Src
or
Dst
and
NodeId
are present.
NodeId
principal.ip
Directly mapped from
NodeId
if
NodeId
is present but
Src
and
Dst
are not.
Protocol
network.ip_protocol
Mapped from
Protocol
after converting it to an integer and then using a lookup to convert the number to the protocol name (e.g., 6 becomes TCP).
RuleId
security_result.rule_id
Directly mapped from
RuleId
.
Service
principal.application
Directly mapped from
Service
if it's not "Dest. Unreachable (Port Unreachable)".
Service
network.application_protocol
If
Service
is "HTTP" or "HTTPS", set to the value of
Service
. If
Service
contains "DNS", set to "DNS".
Service
metadata.event_type
If
Service
is "HTTP" or "HTTPS", set
metadata.event_type
to "NETWORK_HTTP".
Situation
security_result.summary
Directly mapped from
Situation
.
Sport
principal.port
Directly mapped from
Sport
if not 0. Converted to integer.
Src
principal.ip
Directly mapped from
Src
.
Timestamp
metadata.event_timestamp
Directly mapped from
Timestamp
after parsing it as a date.
Type
security_result.severity_details
Directly mapped from
Type
.
Type
security_result.severity
If
Type
is "Notification", set to "LOW". If
Src
or
NodeId
and
Dst
or
CompId
are present, set to "NETWORK_CONNECTION". If only
principal.ip
is present, set to "STATUS_UPDATE". Otherwise, set to "GENERIC_EVENT". Set to "FORCEPOINT_FIREWALL". Set to "FORCEPOINT FIREWALL". Set to "FORCEPOINT".
rt
metadata.event_timestamp
Directly mapped from
rt
after parsing it as a date in the CEF block.
act
security_result.action_details
Directly mapped from
act
in the CEF block.
app
principal.application
Directly mapped from
app
in the CEF block.
deviceFacility
metadata.description
Directly mapped from
deviceFacility
in the CEF block.
destinationTranslatedAddress
target.nat_ip
Directly mapped from
destinationTranslatedAddress
in the CEF block.
destinationTranslatedPort
target.nat_port
Directly mapped from
destinationTranslatedPort
in the CEF block.
dst
target.ip
Directly mapped from
dst
in the CEF block.
dpt
target.port
Directly mapped from
dpt
in the CEF block.
dvchost
intermediary.ip
Directly mapped from
dvchost
in the CEF block.
event_name
metadata.product_event_type
Directly mapped from
event_name
in the CEF block.
msg
security_result.description
Directly mapped from
msg
in the CEF block.
proto
network.ip_protocol
Mapped from
proto
after converting it to an integer and then using a lookup to convert the number to the protocol name (e.g., 6 becomes TCP) in the CEF block.
sourceTranslatedAddress
principal.nat_ip
Directly mapped from
sourceTranslatedAddress
in the CEF block.
sourceTranslatedPort
principal.nat_port
Directly mapped from
sourceTranslatedPort
in the CEF block.
spt
principal.port
Directly mapped from
spt
in the CEF block.
src
principal.ip
Directly mapped from
src
in the CEF block.
Need more help?
Get answers from Community members and Google SecOps professionals.
