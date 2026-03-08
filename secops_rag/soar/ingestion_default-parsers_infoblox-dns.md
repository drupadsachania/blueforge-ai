# Collect Infoblox DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-dns/  
**Scraped:** 2026-03-05T09:57:22.529783Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Infoblox DNS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Infoblox DNS logs to Google Security Operations using Bindplane.
The parser extracts fields from Infoblox DNS SYSLOG and CEF formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Infoblox Grid Manager web interface
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
udplog
:
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'INFOBLOX_DNS'
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
Configuration parameters
Replace the following placeholders:
Receiver configuration:
udplog
: Use
udplog
for UDP syslog or
tcplog
for TCP syslog
0.0.0.0
: IP address to listen on (
0.0.0.0
to listen on all interfaces)
514
: Port number to listen on (standard syslog port)
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
YOUR_CUSTOMER_ID
: Customer ID from the Get customer ID section
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
: Log type exactly as it appears in Chronicle (
INFOBLOX_DNS
)
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
To restart the Bindplane agent in Windows, choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Syslog forwarding on Infoblox DNS
Sign in to the
Infoblox Grid Manager
web interface.
Go to
Grid
>
Grid Manager
>
Members
.
Select the member to configure and click
Edit
.
Go to the
Monitoring
tab.
Under
Syslog
, click
Add
to add a new syslog server.
Provide the following configuration details:
Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Transport
: Select
UDP
.
Node ID
: Select the Infoblox node (for HA pairs).
Severity
: Select
Info
(or your preferred severity level).
Facility
: Select
local0
(or your preferred facility).
Enable the following log categories:
DNS queries
: Select
Log DNS Queries
under
Grid DNS Properties
>
Logging
.
DNS responses
: Select
Log DNS Responses
.
DHCP
: Enable DHCP logging under
Grid DHCP Properties
.
Audit
: Enable audit logging under
Grid Properties
>
Monitoring
.
Click
Save & Close
.
Restart the DNS service if required.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
agent.hostname
principal.hostname
For CEF formatted logs, if agent.hostname exists, it's mapped to principal.hostname.
client_ip
principal.ip
For CEF formatted logs, if client_ip exists, it's mapped to principal.ip.
client_port
principal.port
For CEF formatted logs, if client_port exists, it's mapped to principal.port.
data
answers.data
Extracted from the data field of the answers section in the raw log. Multiple occurrences are mapped as separate answers objects.
description
metadata.description
Mapped directly from the raw log's description field or extracted using grok patterns from other fields like message and msg2.
dest_ip1
target.ip
Extracted from the raw log and mapped to target.ip.
destinationDnsDomain
dns_question.name
For CEF formatted logs, if destinationDnsDomain exists, it's mapped to dns_question.name.
dns_class
dns_question.class
Mapped using the dns_query_class_mapping.include lookup table.
dns_domain
dns_question.name
Extracted from the raw log's message field using grok patterns and mapped to dns_question.name.
dns_name
dns_question.name
Extracted from the dns_domain field using grok patterns and mapped to dns_question.name.
dns_records
answers.data
For CEF formatted logs, if dns_records exists, it's mapped to answers.data. Multiple occurrences are mapped as separate answers objects.
dst_ip
target.ip or target.hostname
Extracted from the raw log's message field using grok patterns. If it's a valid IP address, it's mapped to target.ip; otherwise, it's mapped to target.hostname.
dst_ip1
target.ip or target.hostname
Extracted from the raw log's message or msg2 field using grok patterns. If it's a valid IP address, it's mapped to target.ip; otherwise, it's mapped to target.hostname. Only mapped if different from dst_ip.
evt_type
metadata.product_event_type
Mapped directly from the raw log's evt_type field, which is extracted from the message field using grok patterns.
InfobloxB1OPHIPAddress
principal.ip
For CEF formatted logs, if InfobloxB1OPHIPAddress exists, it's mapped to principal.ip.
InfobloxB1Region
principal.location.country_or_region
For CEF formatted logs, if InfobloxB1Region exists, it's mapped to principal.location.country_or_region.
InfobloxDNSQType
dns_question.type
For CEF formatted logs, if InfobloxDNSQType exists, it's mapped to dns_question.type.
intermediary
intermediary.ip or intermediary.hostname
Extracted from the raw log's message field using grok patterns. If it's a valid IP address, it's mapped to intermediary.ip; otherwise, it's mapped to intermediary.hostname.
msg2
metadata.description, dns.response_code, dns_question.name, target.ip, target.hostname, answers.name, answers.ttl, answers.data, answers.class, answers.type, security_result.severity
Extracted from the raw log's message field using grok patterns. Used for extracting various fields but not directly mapped to UDM.
name1
answers.name
Extracted from the raw log's msg2 field using grok patterns and mapped to answers.name.
name2
answers.name
Extracted from the raw log's msg2 field using grok patterns and mapped to answers.name.
protocol
network.ip_protocol
Mapped directly from the raw log's protocol field if it matches known protocols.
qclass
dns_question.class
Intermediate field used for mapping dns_class to UDM.
qclass1
answers.class
Intermediate field used for mapping dns_class1 to UDM.
qclass2
answers.class
Intermediate field used for mapping dns_class2 to UDM.
query_type
dns_question.type
Mapped using the dns_record_type.include lookup table.
query_type1
answers.type
Mapped using the dns_record_type.include lookup table.
query_type2
answers.type
Mapped using the dns_record_type.include lookup table.
recursion_flag
network.dns.recursion_desired
If the recursion_flag contains a "+", it's mapped to network.dns.recursion_desired as true.
record_type
dns_question.type
Intermediate field used for mapping query_type to UDM.
record_type1
answers.type
Intermediate field used for mapping query_type1 to UDM.
record_type2
answers.type
Intermediate field used for mapping query_type2 to UDM.
res_code
network.dns.response_code
Mapped using the dns_response_code.include lookup table.
response_code
network.dns.response_code
For CEF formatted logs, if response_code exists, it's mapped to network.dns.response_code using the dns_response_code.include lookup table.
security_action
security_result.action
Derived from the status field. If status is "denied", security_action is set to "BLOCK"; otherwise, it's set to "ALLOW".
severity
security_result.severity
For CEF formatted logs, if severity exists and is "informational", it's mapped to security_result.severity as "INFORMATIONAL".
src_host
principal.hostname
Extracted from the raw log's description or message field using grok patterns and mapped to principal.hostname.
src_ip
principal.ip or principal.hostname
Extracted from the raw log's message field using grok patterns. If it's a valid IP address, it's mapped to principal.ip; otherwise, it's mapped to principal.hostname.
src_port
principal.port
Extracted from the raw log's message field using grok patterns and mapped to principal.port.
ttl1
answers.ttl
Extracted from the raw log's msg2 field using grok patterns and mapped to answers.ttl.
ttl2
answers.ttl
Extracted from the raw log's msg2 field using grok patterns and mapped to answers.ttl.
metadata.event_type
metadata.event_type
Derived from various fields and parser logic. Defaults to GENERIC_EVENT if no other event type is identified. Possible values include NETWORK_DNS, NETWORK_CONNECTION, and STATUS_UPDATE.
metadata.log_type
metadata.log_type
Set to "INFOBLOX_DNS" by the parser.
metadata.product_name
metadata.product_name
Set to "Infoblox DNS" by the parser.
metadata.vendor_name
metadata.vendor_name
Set to "INFOBLOX" by the parser.
metadata.product_version
metadata.product_version
Extracted from CEF messages.
metadata.event_timestamp
metadata.event_timestamp
Copied from the timestamp field.
network.application_protocol
network.application_protocol
Set to "DNS" if the event_type is not "GENERIC_EVENT" or "STATUS_UPDATE".
Need more help?
Get answers from Community members and Google SecOps professionals.
