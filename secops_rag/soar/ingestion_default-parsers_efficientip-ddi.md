# Collect EfficientIP DDI logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi/  
**Scraped:** 2026-03-05T09:54:58.161921Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect EfficientIP DDI logs
Supported in:
Google secops
SIEM
This document explains how to ingest EfficientIP DDI logs into Google Security Operations using the Bindplane agent.
EfficientIP SOLIDserver is a comprehensive DDI (DNS-DHCP-IPAM) solution that delivers highly scalable, secure, and robust virtual and hardware appliances for critical network services including DNS, DHCP, IP Address Management, NTP, and TFTP. The platform provides centralized management and automation for network infrastructure with advanced monitoring and security capabilities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or a Linux host with
systemd
Network connectivity between the Bindplane agent and EfficientIP SOLIDserver appliance
If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
Administrative access to the EfficientIP SOLIDserver web console
SOLIDserver version 8.0 or later (tested with 8.3.x and 8.4.x)
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
The service status should be
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
The service status should be
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
chronicle/efficientip_ddi
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
EFFICIENTIP_DDI
raw_log_field
:
body
ingestion_labels
:
env
:
production
source
:
solidserver
service
:
pipelines
:
logs/efficientip_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/efficientip_ddi
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on UDP port 514.
For Linux non-root deployments, use port
1514
or higher.
Ensure that the port matches the configuration in SOLIDserver.
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Replace
YOUR_CUSTOMER_ID
with the customer ID from the previous step.
endpoint
: Regional endpoint:
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
for a complete list.
log_type
: Set to
EFFICIENTIP_DDI
(exact match required).
ingestion_labels
: Optional labels for categorizing logs (customize as needed).
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
To restart the Bindplane agent in Linux:
Run the following command:
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
To restart the Bindplane agent in Windows:
Choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press Enter.
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
Configure EfficientIP DDI syslog forwarding
Sign in to the
EfficientIP SOLIDserver
web console.
In the left navigation, click
Administration
.
In the
Monitoring
section, click
Configuration
.
In the menu, click
+ Add
.
In the
Services
list, select the following services:
named
(for DNS logs)
In the
Target server
field, enter the IP address and port of the Bindplane agent host in the format
<ip-address>:<port>
.
Example:
192.168.1.100:514
If using a non-standard port on Linux, specify the port accordingly (for example,
192.168.1.100:1514
)
Click
OK
to save the configuration.
Verify log forwarding
Check the Bindplane agent logs to confirm logs are being received:
Linux
:
sudo journalctl -u observiq-otel-collector -f
Windows
:
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Look for log entries containing DNS query and answer events from SOLIDserver.
Sign in to the Google SecOps console and verify that EfficientIP DDI logs appear in the
Events
page.
Supported log types
This integration collects the following log types from EfficientIP SOLIDserver:
DNS query logs
: Client DNS queries with query type, domain name, and client IP
DNS answer logs
: DNS responses with answer records, TTL, and response codes
DHCP logs
: DHCP operations including DISCOVER, OFFER, REQUEST, ACK, NAK, RELEASE, and INFORM
DNS Guardian logs
: Security events including suspicious behavior detection, arming/disarming triggers
DNS zone transfer logs
: Zone transfer operations and notifications
DNS error logs
: Format errors, SERVFAIL, REFUSED, and other DNS errors
UDM mapping table
Log Field
UDM Mapping
Logic
ip_version
additional.fields
Merged as label with key "ip_version" if not empty
message_size
additional.fields
Merged as label with key "message_size" if not empty
domain_name
additional.fields
Merged as label with key "domain_name" if not empty
N/A
intermediary
Merged from intermediary object
description
metadata.description
Value copied directly if not empty
msg2
metadata.description
Set to msg2 if event_type is GENERIC_EVENT and description is empty
su_cmd
metadata.event_type
Set to "PROCESS_OPEN" if su_cmd is "sudo"
activity_type
metadata.event_type
Set to "NETWORK_DNS" if activity_type matches dns and has_dns_questions is true
message
metadata.event_type
Set to "NETWORK_DHCP" if message matches dhcp
inner_message
metadata.event_type
Set to "NETWORK_UNCATEGORIZED" if inner_message matches specific patterns and has_principal and has_target are true
process
metadata.event_type
Set to "NETWORK_DNS" if process is "named" and has_dns_questions is true; set to "STATUS_UPDATE" if process is "named" and has_principal is true; set to "GENERIC_EVENT" if process is "named"; set to "NETWORK_DHCP" if process is "dhcpd"
PWD
metadata.event_type
Set to "PROCESS_OPEN" if PWD not empty and has_target or has_principal is true
activity_type
metadata.product_event_type
Value copied directly
N/A
metadata.vendor_name
Set to "EFFICIENTIP_DDI"
N/A
metadata.product_name
Set to "EFFICIENTIP_DDI DHCP"
activity_type
network.application_protocol
Set to "DNS" if activity_type matches dns and has_dns_questions is true
message
network.application_protocol
Set to "DHCP" if message matches dhcp
process
network.application_protocol
Set to "DNS" if process is "named"; set to "DHCP" if process is "dhcpd"
src_mac
network.dhcp.chaddr
Value copied directly if process is "dhcpd"
src_ip
network.dhcp.ciaddr
Value copied directly if dhcp_info is "REQUEST"
giaddr
network.dhcp.giaddr
Value copied directly
dhcp_info
network.dhcp.opcode
Set to "BOOTREQUEST" if dhcp_info is "INFORM", "DISCOVER", or "REQUEST"; set to "BOOTREPLY" if dhcp_info is "OFFER" or "ACK"
siaddr
network.dhcp.siaddr
Value copied directly
transaction_id
network.dhcp.transaction_id
Value converted to uinteger if not empty or "0"
dhcp_info
network.dhcp.type
Set to "INFORM" if dhcp_info is "INFORM"; set to "DISCOVER" if "DISCOVER"; set to "OFFER" if "OFFER"; set to "REQUEST" if "REQUEST"; set to "ACK" if "PACK"
yiaddr
network.dhcp.yiaddr
Value copied directly
src_ip
network.dhcp.yiaddr
Set to src_ip if process is "dhcpd" and yiaddr is empty
answer_rrs
network.dns.answers
Merged from answer object for each rd in answer_rrs
N/A
network.dns.questions
Merged from questions object if has_dns_questions is true
rcode
network.dns.response_code
Value converted to uinteger
response_code
network.dns.response_code
Value mapped to numeric code and converted to uinteger
transport
network.ip_protocol
Value uppercased if matches udp or tcp
observer
observer.ip
Value converted to ipaddress
su_cmd
principal.application
Value copied directly if su_cmd is "sudo"
process
principal.application
Set to process if process is "named" or "dhcpd"
host
principal.asset.hostname
Value copied directly if not empty
hostname
principal.asset.hostname
Value copied directly if not empty and host is empty
src_ip
principal.asset.ip
Value copied directly
asset_id
principal.asset_id
Concatenated as "ID:" + asset_id
host
principal.hostname
Value copied directly if not empty
hostname
principal.hostname
Value copied directly if not empty and host is empty
domain_name
principal.hostname
Value copied directly if description contains hostname and host/hostname are empty
src_ip
principal.ip
Value copied directly if converted to ipaddress succeeds; extracted from description if src_ip is empty
src_mac
principal.mac
Value copied directly
src_port
principal.port
Value converted to integer
process_id
principal.process.pid
Value copied directly
source_user
principal.user.userid
Value copied directly
N/A
security_result
Merged from sec_result
dst_ip
target.asset.ip
Value copied directly
file_path
target.file.full_path
Value copied directly
dst_ip
target.hostname
Value copied directly if not a valid ipaddress
host
target.hostname
Value copied directly if inner_message matches specific patterns
dst_ip
target.ip
Value copied directly
dst_port
target.port
Value converted to integer
target_cmd_line
target.process.command_line
Value copied directly
target_user
target.user.userid
Value copied directly
Need more help?
Get answers from Community members and Google SecOps professionals.
