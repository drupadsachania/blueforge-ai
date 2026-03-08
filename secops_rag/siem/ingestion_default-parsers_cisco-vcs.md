# Collect Cisco VCS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vcs/  
**Scraped:** 2026-03-05T09:21:52.554836Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco VCS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco VCS (Video Communication Service),
(controlled through ExpressWay) logs to Google Security Operations using Bindplane.
The parser extracts fields from the syslog messages, normalizes them into a
Unified Data Model (UDM), and categorizes the event type based on extracted
details like IP addresses, ports, and actions. It handles various log formats,
extracts key-value pairs, and maps severity levels to standardized values for
security analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to the
Cisco ExpressWay
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
ingestion authentication file
. Save the file securely on th
system where BindPlane will be installed.
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
'CISCO_VCS'
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
Configure Syslog for Cisco ExpressWay
Sign in to the
Cisco ExpressWay
web UI.
Go to
Maintenance
>
Logging
.
Enter the Bindplane agent IP addresses as the
Remote syslog server
.
Click
Options
.
Provide the following configuration details:
Transport
: Select
UDP
.
Port
: Enter the Bindplane agent port number.
Message Format
: Select
BSD
, the other possible option is
IETF
.
Filter by Severity
: Select
Informational
.
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
Action
read_only_udm.security_result.action_details
The value of
Action
field from the raw log.
Code
read_only_udm.network.http.response_code
The value of
Code
field from the raw log, converted to integer. Used when
Response-code
is not present.
Detail
read_only_udm.security_result.description
The value of
Detail
field from the raw log.
Dst-ip
read_only_udm.target.ip
The value of
Dst-ip
field from the raw log. Used when
Action
is not
Received
.
Dst-port
read_only_udm.target.port
The value of
Dst-port
field from the raw log, converted to integer. Used when
Action
is not
Received
.
Event
read_only_udm.metadata.product_event_type
The value of
Event
field from the raw log.
Level
read_only_udm.security_result.severity_details
The value of
Level
field from the raw log.
Level
read_only_udm.security_result.severity
Mapped based on the value of
Level
field from the raw log:
-
9
,
10
,
VERY-HIGH
: CRITICAL
-
error
,
warning
,
7
,
8
,
HIGH
: HIGH
-
notice
,
4
,
5
,
6
,
MEDIUM
: MEDIUM
-
information
,
info
,
0
,
1
,
2
,
3
,
LOW
: LOW
Local-ip
read_only_udm.principal.ip
The value of
Local-ip
field from the raw log. Used when
Action
is not
Received
.
Local-ip
read_only_udm.target.ip
The value of
Local-ip
field from the raw log. Used when
Action
is
Received
.
Local-port
read_only_udm.principal.port
The value of
Local-port
field from the raw log, converted to integer. Used when
Action
is not
Received
.
Local-port
read_only_udm.target.port
The value of
Local-port
field from the raw log, converted to integer. Used when
Action
is
Received
.
Method
read_only_udm.network.http.method
The value of
Method
field from the raw log.
Module
read_only_udm.additional.fields.value.string_value
The value of
Module
field from the raw log.
Node
read_only_udm.additional.fields.value.string_value
The value of
Node
field from the raw log.
Protocol
read_only_udm.network.ip_protocol
The value of
Protocol
field from the raw log, parsed and mapped to the corresponding IP protocol name using the
parse_ip_protocol.include
logic.
Response-code
read_only_udm.network.http.response_code
The value of
Response-code
field from the raw log, converted to integer.
Src-ip
read_only_udm.principal.ip
The value of
Src-ip
field from the raw log. Used when
Action
is
Received
.
Src-ip
read_only_udm.principal.ip
The value of
Src-ip
field from the raw log. Used when
Action
is not
Received
and
Local-ip
is not present.
Src-port
read_only_udm.principal.port
The value of
Src-port
field from the raw log, converted to integer. Used when
Action
is
Received
.
Src-port
read_only_udm.principal.port
The value of
Src-port
field from the raw log, converted to integer. Used when
Action
is not
Received
and
Local-port
is not present.
application
read_only_udm.target.application
The value of
application
field from the raw log.
description
read_only_udm.security_result.description
The value of
description
field from the raw log.
inner_msg
read_only_udm.security_result.description
The value of
inner_msg
field from the raw log. Used when
inner_msg_grok_failure
occurs.
principal_hostname
read_only_udm.principal.hostname
The value of
principal_hostname
field from the raw log.
timestamp
read_only_udm.metadata.event_timestamp.seconds
The epoch timestamp extracted from the
timestamp
field in the raw log.
timestamp
read_only_udm.events.timestamp.seconds
The epoch timestamp extracted from the
timestamp
field in the raw log.
read_only_udm.additional.fields.key
Hardcoded value:
Module
,
Node
read_only_udm.metadata.log_type
Hardcoded value:
CISCO_VCS
read_only_udm.metadata.product_name
Hardcoded value:
CISCO VCS
read_only_udm.metadata.vendor_name
Hardcoded value:
CISCO VCS
read_only_udm.metadata.event_type
Determined based on the values of
Action
,
Src-ip
,
principal_hostname
,
Local-ip
, and
Dst-ip
fields:
-
NETWORK_CONNECTION
: if either (
Action
is
Received
and
Local-ip
is present) or (
Action
is not
Received
and
Dst-ip
is present)
-
STATUS_UPDATE
: otherwise
Need more help?
Get answers from Community members and Google SecOps professionals.
