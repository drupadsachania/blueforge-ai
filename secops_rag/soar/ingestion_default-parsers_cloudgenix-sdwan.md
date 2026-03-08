# Collect Palo Alto Prisma SD-WAN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudgenix-sdwan/  
**Scraped:** 2026-03-05T09:59:10.750819Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Prisma SD-WAN logs
Supported in:
Google secops
SIEM
This document explains how to ingest Palo Alto Prisma SD-WAN (formerly Cloudgenix SD-WAN) logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog and flow logs, mapping them to the Unified Data Model (UDM). It handles both structured and unstructured syslog messages, performing key-value parsing and Grok matching to extract relevant information like source/destination IPs, hostnames, event types, and security details, and populates UDM fields accordingly. The parser also processes flow logs, extracting network information and mapping it to the UDM's network, principal, target, intermediary, and security result schemas.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the Palo Alto Prisma SD-WAN (formerly Cloudgenix SD-WAN)
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
```
yaml
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
chronicle
/
chronicle_w_labels
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
malachiteingestion
-
pa
.
googleapis
.
com
# Add optional ingestion labels for better organization
log_type
:
'CLOUDGENIX_SDWAN'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs
/
source0__chronicle_w_labels
-
0
:
receivers
:
-
udplog
exporters
:
-
chronicle
/
chronicle_w_labels
```
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
Configure Prisma SD-WAN Syslog Profile
Sign in to the
Prisma SD-WAN
.
Go to
Manage
>
Resources
>
Configuration Profiles
.
Select
Syslog
.
Click
Create Syslog Profile
.
Provide the following configuration details:
Name
: Enter a name for this profile.
Select the
Enable Flow Logging
checkbox.
Severity
: Select the Severity Level from a severity level of Critical, Major, or Minor.
Protocol
: Select the protocol type as
UDP
, or
TCP
, depending on your Bindplane agent configuration.
Select the
Server IP
radio button.
Enter the Bindplane agent IP address.
Server Port
: Enter the Bindplane agent port number.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ACTION
security_result.action
If
ACTION_CODE
is "1", set to "ALLOW". Otherwise, if
ACTION_CODE
is not empty, set to "BLOCK". Otherwise, defaults to "UNKNOWN_ACTION" from earlier in the parser.
ACTION_CODE
security_result.action
Used in the logic to determine
security_result.action
.
APP_NAME
network.http.user_agent
Directly mapped.
BYTES_RECVD
network.received_bytes
Directly mapped, converted to unsigned integer.
BYTES_SENT
network.sent_bytes
Directly mapped, converted to unsigned integer.
CLOUDGENIX_HOST
principal.hostname
Directly mapped if
NAME
field is empty. Used as intermediary hostname if
NAME
is present.
CODE
metadata.product_event_type
Concatenated with
FACILITY
to form
metadata.product_event_type
. Also used to determine
metadata.event_type
(e.g., if
CODE
contains "DOWN",
metadata.event_type
is set to "STATUS_SHUTDOWN").
DESTINATION_ZONE_NAME
about.labels
Directly mapped as a label with key "DESTINATION_ZONE_NAME".
DEVICE_TIME
metadata.event_timestamp
Directly mapped after being parsed as a date.
DST_INTERFACE
target.hostname
Directly mapped.
DST_IP
target.ip
Directly mapped.
DST_PORT
target.port
Directly mapped, converted to integer.
ELEMENT_ID
about.labels
Directly mapped as a label with key "ELEMENT_ID".
EVENT_TIME
metadata.event_timestamp
Directly mapped after being parsed as a date.
FACILITY
metadata.product_event_type
Concatenated with
CODE
to form
metadata.product_event_type
.
FLOW_EVENT
security_result.summary
Used as part of the
security_result.summary
string.
IDENTIFIER
about.labels
Directly mapped as a label with key "IDENTIFIER".
ION_HOST
principal.hostname
Directly mapped if
CLOUDGENIX_HOST
and
NAME
fields are empty.
MSG
metadata.description
Directly mapped. Also used for regex matching to determine
metadata.event_type
and to extract
target.ip
.
NAME
principal.hostname
Directly mapped. If present,
CLOUDGENIX_HOST
becomes the
intermediary.hostname
.
PROCESS_NAME
principal.process.file.full_path
Directly mapped.
PROTOCOL_NAME
network.ip_protocol
Directly mapped, converted to uppercase.
REMOTE_HOSTNAME
target.hostname
Directly mapped.
REMOTE_IP
target.ip
Directly mapped.
RULE_NAME
security_result.rule_name
Directly mapped.
SEVERITY
security_result.severity
,
security_result.severity_details
Mapped to
security_result.severity_details
. Also used to determine
security_result.severity
(e.g., if
SEVERITY
is "minor",
security_result.severity
is set to "LOW").
SOURCE_ZONE_NAME
about.labels
Directly mapped as a label with key "SOURCE_ZONE_NAME".
SRC_INTERFACE
principal.hostname
Directly mapped.
SRC_IP
principal.ip
Directly mapped.
SRC_PORT
principal.port
Directly mapped, converted to integer.
VPN_LINK_ID
target.resource.id
Directly mapped.
(Parser Logic)
is_alert
Set to true if
log_type
is "alert" or "alarm".
(Parser Logic)
is_significant
Set to true if
log_type
is "alert" or "alarm".
(Parser Logic)
metadata.event_type
Determined by a series of conditional statements based on the values of
CODE
,
MSG
,
src_ip
, and
dest_ip
. Defaults to "GENERIC_EVENT".
(Parser Logic)
metadata.log_type
Set to "CLOUDGENIX_SDWAN".
(Parser Logic)
metadata.product_event_type
Defaults to the concatenation of
CODE
and
FACILITY
. Set to "cgxFlowLogV1" for flow logs.
(Parser Logic)
metadata.product_name
Set to "CloudGenix SD-WAN".
(Parser Logic)
metadata.vendor_name
Set to "Palo Alto Networks".
(Parser Logic)
principal.process.pid
Set to the value of
pid
from the raw log for flow logs.
(Parser Logic)
security_result.action
Defaults to "UNKNOWN_ACTION".
(Parser Logic)
security_result.severity
Defaults to "UNKNOWN_SEVERITY". Set based on the value of
SEVERITY
. Set to "INFORMATIONAL" for flow logs.
(Parser Logic)
security_result.summary
Set based on the value of
CODE
for syslog messages. Set to a descriptive string including
FLOW_EVENT
,
SRC_IP
, and
DST_IP
for flow logs.
Need more help?
Get answers from Community members and Google SecOps professionals.
