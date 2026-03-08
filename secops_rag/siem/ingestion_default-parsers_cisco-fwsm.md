# Collect Cisco Firewall Service Module (FWSM) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-fwsm/  
**Scraped:** 2026-03-05T09:21:31.445551Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Firewall Service Module (FWSM) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Firewall Service Module (FWSM) logs
to Google Security Operations using Bindplane. The parser first extracts common
fields like timestamps, IP addresses, and event descriptions from the appliance
syslog messages using Grok patterns. Then, it maps the extracted information to
the standardized Unified Data Model (UDM) schema, converting data types,
renaming fields, and enriching the output with security-related classifications
based on specific values and keywords.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the
Cisco FWSM
appliance
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
ingestion authentication file
.
Save the file securely on the system where Bindplane will be installed.
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
Configure the Bindpolane agent to ingest Syslog and send to Google SecOps
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
'CISCO_FWSM'
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
Configure Syslog on Cisco FWSM
Sign in to Cisco FWSM using SSH or a console connection.
Configure logging:
logging
on
Configure the logging level:
logging
trap
<level>
Change the logging trap level to
6
(informational).
Configure the syslog settings:
logging
host
[
interface
]
bindplane_ip_address
udp
[
/bindplane_port
]
UDM mapping table
Log Field
UDM Mapping
Logic
1.1.1.1
observer.ip
Extracted from the log message using grok pattern.
2.2.2.2
principal.ip
target.ip
Extracted from the log message using grok pattern. The destination IP is mapped to either principal.ip or target.ip based on the direction of the connection. When
dst outside
it will be mapped to principal.ip, otherwise to target.ip.
3.3.3.3
principal.ip
target.ip
Extracted from the log message using grok pattern. The source IP is mapped to either principal.ip or target.ip based on the direction of the connection. When
dst outside
it will be mapped to principal.ip, otherwise to target.ip.
Apr  3 10:35:40
This timestamp is not captured in the UDM.
Apr  3 10:44:38
This timestamp is not captured in the UDM.
Apr  3 11:20:34
This timestamp is not captured in the UDM.
Apr  3 11:20:38
This timestamp is not captured in the UDM.
Apr 29 16:09:44
This timestamp is not captured in the UDM.
Deny
security_result.action_details
Extracted from the log message using grok pattern.
Denied
security_result.action_details
Extracted from the log message using grok pattern.
FWSM-3-106011
metadata.product_event_type
Extracted from the log message using grok pattern.
FWSM-3-313001
metadata.product_event_type
Extracted from the log message using grok pattern.
FWSM-4-106023
metadata.product_event_type
Extracted from the log message using grok pattern.
FWSM-4-302010
metadata.product_event_type
Extracted from the log message using grok pattern.
FWSM-4-302016
metadata.product_event_type
Extracted from the log message using grok pattern.
ICMP
network.ip_protocol
Extracted from the log message using grok pattern and converted to uppercase.
TCP
network.ip_protocol
Extracted from the log message using grok pattern and converted to uppercase.
Teardown
security_result.action_details
Extracted from the log message using grok pattern.
UDP
network.ip_protocol
Extracted from the log message using grok pattern and converted to uppercase.
111
target.port
Extracted from the log message using grok pattern and converted to integer. When
dst outside
it will be mapped to principal.port, otherwise to target.port.
17608
principal.port
Extracted from the log message using grok pattern and converted to integer. When
dst outside
it will be mapped to principal.port, otherwise to target.port.
3000
principal.port
Extracted from the log message using grok pattern and converted to integer. When
dst outside
it will be mapped to principal.port, otherwise to target.port.
33103
target.port
Extracted from the log message using grok pattern and converted to integer. When
dst outside
it will be mapped to principal.port, otherwise to target.port.
514
principal.port
target.port
Extracted from the log message using grok pattern and converted to integer. When
dst outside
it will be mapped to principal.port, otherwise to target.port.
metadata.description
The entire
descrip
field from the raw log is mapped to this field.
metadata.event_timestamp
The timestamp from the batch object is used as the event timestamp.
metadata.event_type
Determined based on the presence of source and destination IPs:
- NETWORK_CONNECTION: both source and destination IPs are present.
- STATUS_UPDATE: only source IP is present.
- GENERIC_EVENT: neither source nor destination IP is present.
metadata.product_name
Hardcoded to
CISCO_FWSM
.
metadata.vendor_name
Hardcoded to
CISCO
.
principal.resource.type
Mapped from the
facility
field extracted from the log message.
security_result.action
Set to
BLOCK
if the
action
field is one of
Deny
,
Teardown
,
denied
, or
Denied
.
security_result.severity
Determined based on the
severity_level
field:
- 7, 6: INFORMATIONAL
- 5: LOW
- 4: MEDIUM
- 3: ERROR
- 2: HIGH
- other: CRITICAL
network.direction
Mapped from the
direction
field extracted from the log message. If
direction
field is
inbound
, this field will be set to
INBOUND
.
Need more help?
Get answers from Community members and Google SecOps professionals.
