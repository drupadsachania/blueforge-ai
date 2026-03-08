# Collect BlueCat DDI logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-ddi/  
**Scraped:** 2026-03-05T09:51:26.972712Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BlueCat DDI logs
Supported in:
Google secops
SIEM
This parser handles both LEEF and non-LEEF formatted syslog messages from Bluecat DDI (DNS, DHCP, IPAM). It extracts fields from various log types (for example, named, dhcpd, audit, and CRON) using grok patterns and conditional logic, mapping them to the UDM based on the log type and populating DNS, DHCP, or user-related fields accordingly.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Bluecat.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
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
Install Bindplane Agent
For
Windows installation
, run the following script:
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane is installed.
Edit the
config.yaml
file as follows:
receivers:
    tcplog:
        # Replace the below port <54525> and IP <0.0.0.0> with your specific values
        listen_address: "0.0.0.0:54525" 

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        # Adjust the creds location below according the placement of the credentials file you downloaded
        creds: '{ json file for creds }'
        # Replace <customer_id> below with your actual ID that you copied
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        # You can apply ingestion labels below as preferred
        ingestion_labels:
        log_type: SYSLOG
        namespace: bluceat_ddi
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes:
sudo
systemctl
restart
bindplane
Configure Syslog on Bluecat DDI
Sign in to the Bluecat Address Manager (BAM).
From the
configuration
menu, select a configuration.
Select the
Servers
tab.
Under
Servers
, click the name of a
BDDS
.
The
Details
tab for the server should open.
Click the
server name
menu.
Select
Service Configuration
.
Click
Service Type
>
Syslog
(the Address Manager queries the server and returns the current values).
In
General
, set the following values:
Syslog Server
: the IP address of your Syslog server (Bindplane).
Syslog Port
: the port of your Syslog server (Bindplane).
Syslog Transport
: select either
TCP
or
UDP
(depending on your Bindplane configuration).
Click
Add
.
The newly added syslog server will appear in the list.
Click
Update
.
Configure Syslog Settings in BlueCat DDI
Sign in to the BlueCat Address Manager.
Go to
Configuration
>
System Settings
>
Logging
.
In the
Logging Settings
, locate the
Syslog Servers
section.
Click
Add Syslog Server
.
Provide the required values:
Server Name
: a unique name for the syslog server (for example,
BindplaneServer
).
IP Address
: the IP address or hostname of the syslog server.
Protocol
: select
TCP
,
UDP
(default), or
TLS
(based on your syslog configuration).
Port
: specify the port for syslog communication (default: 514 for UDP/TCP, 6514 for TLS).
Configure
Logging Level
. Choose the appropriate level based on your needs. Options include:
Emergency
: critical issues that require immediate attention
Alert
: alerts that need prompt action
Critical
: critical conditions
Error
: error events
Warning
: warning events
Notice
: normal but significant events
Info
: informational messages
Debug
: detailed debug information
Optional: Add a custom Syslog facility to categorize logs (for example,
local0
or
local1
).
Save the configuration.
Apply Syslog Settings to DDI Appliances
Navigate to
Servers
>
Manage Servers
.
Select the DNS/DHCP servers where the syslog should be enabled.
Click
Edit Server
.
In the
Logging
section:
Select the syslog server you configured earlier.
Enable logging for specific services (For example,
DNS queries
or
DHCP leases
).
Save the changes.
UDM Mapping Table
Log field
UDM mapping
Logic
client_ip
network.dhcp.ciaddr
Extracted from the DHCPREQUEST message. Only populated for DHCPREQUEST messages.
client_mac
principal.mac
Extracted from DHCP messages (DHCPDISCOVER, DHCPREQUEST, DHCPRELEASE).
client_mac
target.mac
Extracted from DHCP messages (DHCPOFFER, DHCPNAK).
client_mac
network.dhcp.chaddr
Extracted from DHCP messages (DHCPREQUEST, DHCPOFFER, DHCPACK, DHCPNAK, DHCPRELEASE).
cmd
target.process.command_line
Extracted from CRON logs.  Ampersands and spaces are removed.
description
metadata.description
Extracted from various log types, providing additional context.
description
metadata.description
Extracted from syslog-ng logs, providing additional context.
file_path
target.file.full_path
Extracted from various log types, representing the full path to a file.
file_path
target.process.file.full_path
Extracted from agetty logs, representing the full path to a file related to a process.
inner_message
metadata.description
Used as the description for GENERIC_EVENTs when the operation type is not defined and for MEM-MON logs.
metadata.event_type
Determined by the parser based on the log type and content. Possible values include: NETWORK_DNS, NETWORK_DHCP, USER_LOGIN, USER_LOGOUT, USER_UNCATEGORIZED, GENERIC_EVENT, STATUS_UPDATE, NETWORK_CONNECTION. Always "BLUECAT_DDI".
metadata.vendor_name
Always "Bluecat Networks".
metadata.product_name
Always "Bluecat DDI".
metadata.event_timestamp
Copied from the parsed timestamp of the log entry.
network.protocol
Set to "DNS" for DNS logs, "DHCP" for DHCP logs.
network.dns.answers
An array containing answer records. The
data
field within
answers
is populated with the
target_ip
if present.
network.dns.questions
An array containing question records. The
name
field is populated with the
target_host
, the
type
field is derived from the
query_type
or
question_type
fields, and the
class
field is derived from the
qclass
field.
network.dns.recursive
Set to "true" if the
rec_flag
is "+".
qclass
network.dns.questions.class
Extracted from DNS query logs and mapped to an integer value using the
dns_query_class_mapping.include
file.
query_type
network.dns.questions.type
Extracted from DNS query logs and mapped to an integer value using the
dhcp_qtype_mapping.include
file.
relay_ip
intermediary.ip
Extracted from DNS and DHCP logs, representing the IP address of a relay or intermediary server.
server_host
target.hostname
Extracted from various log types, representing the hostname of the server.
server_host
network.dhcp.sname
Extracted from DHCP logs, representing the server host name.
server_host
principal.hostname
Extracted from systemd, agetty, and some audit logs, representing the hostname of the principal.
server_ip
target.ip
Extracted from LEEF formatted logs, representing the IP address of the server.
src_ip
principal.ip
Extracted from various log types, representing the source IP address.
src_ip
network.dhcp.yiaddr
Used in DHCPINFORM messages to populate the yiaddr field.
src_port
principal.port
Extracted from various log types, representing the source port.
src_user
principal.user.userid
Extracted from CRON and audit logs, representing the user ID.
target_host
target.hostname
Extracted from various log types, representing the target hostname.
target_host
network.dns.questions.name
Used in DNS logs to populate the question name.
target_ip
target.ip
Extracted from various log types, representing the target IP address.
target_ip
network.dhcp.ciaddr
Used in BOOTREQUEST messages to populate the ciaddr field.
target_ip
network.dns.answers.data
Used in DNS logs to populate the answer data.
tgt_port
target.port
Extracted from syslog-ng logs, representing the target port.
Need more help?
Get answers from Community members and Google SecOps professionals.
