# Collect Suricata EVE logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/suricata-eve/  
**Scraped:** 2026-03-05T09:28:36.795061Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Suricata EVE logs
Supported in:
Google secops
SIEM
This document explains how to ingest Suricata EVE logs to Google Security Operations using Bindplane.
Suricata is an open-source high-performance network threat detection engine that provides intrusion detection (IDS), intrusion prevention (IPS), and network security monitoring capabilities. The EVE (Extensible Event Format) log output provides comprehensive JSON-formatted logs covering alerts, flows, DNS, HTTP, TLS, and file transaction data. The parser extracts fields from Suricata EVE JSON formatted logs. It parses the JSON message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Suricata host (root or sudo)
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
'SURICATA_EVE'
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
SURICATA_EVE
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
Configure Suricata EVE syslog forwarding
Open the
Suricata
configuration file (typically
/etc/suricata/suricata.yaml
).
Locate the
outputs
section and configure the
EVE log
output for syslog:
outputs
:
-
eve-log
:
enabled
:
yes
filetype
:
syslog
identity
:
"suricata"
facility
:
local5
level
:
Info
types
:
-
alert
:
payload
:
yes
payload-printable
:
yes
packet
:
yes
metadata
:
yes
-
http
:
extended
:
yes
-
dns
:
query
:
yes
answer
:
yes
-
tls
:
extended
:
yes
-
files
:
force-magic
:
no
-
flow
-
netflow
-
anomaly
:
enabled
:
yes
-
stats
:
enabled
:
yes
If the syslog daemon is not configured to forward to Bindplane, configure rsyslog or syslog-ng:
For rsyslog
(edit
/etc/rsyslog.conf
or create
/etc/rsyslog.d/suricata.conf
):
local5.* @BINDPLANE_IP:514
Replace
BINDPLANE_IP
with the IP address of the Bindplane agent host.
Use
@
for UDP or
@@
for TCP.
For syslog-ng
(edit
/etc/syslog-ng/syslog-ng.conf
):
destination d_bindplane { udp("BINDPLANE_IP" port(514)); };
filter f_suricata { facility(local5); };
log { source(s_src); filter(f_suricata); destination(d_bindplane); };
Restart the syslog daemon:
sudo
systemctl
restart
rsyslog
Restart Suricata:
sudo
systemctl
restart
suricata
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
timestamp
metadata.event_timestamp
Event timestamp
event_type
metadata.product_event_type
Type of EVE event (e.g., alert, flow, dns, http, tls)
src_ip
principal.ip
Source IP address
src_port
principal.port
Source port number
dest_ip
target.ip
Destination IP address
dest_port
target.port
Destination port number
proto
network.ip_protocol
Network protocol (e.g., TCP, UDP, ICMP)
flow_id
network.session_id
Unique flow identifier
alert.signature
security_result.rule_name
Alert signature name
alert.signature_id
security_result.rule_id
Alert signature identifier
alert.severity
security_result.severity
Alert severity level
alert.category
security_result.category_details
Alert classification category
alert.action
security_result.action
Action taken (e.g., allowed, blocked)
alert.rev
security_result.rule_version
Rule revision number
http.hostname
target.hostname
HTTP request hostname
http.url
target.url
HTTP request URL
http.http_method
network.http.method
HTTP request method
http.status
network.http.response_code
HTTP response status code
http.http_user_agent
network.http.user_agent
HTTP user agent string
http.http_refer
network.http.referral_url
HTTP referrer URL
http.length
additional.fields
HTTP content length
dns.type
network.dns.type
DNS query or response
dns.rrname
network.dns.questions.name
DNS query name
dns.rrtype
network.dns.questions.type
DNS query type
dns.rdata
network.dns.answers.data
DNS response data
tls.subject
network.tls.client.subject
TLS certificate subject
tls.issuerdn
network.tls.client.issuer
TLS certificate issuer
tls.sni
network.tls.client.server_name
TLS Server Name Indication
tls.version
network.tls.version
TLS version
tls.ja3.hash
network.tls.client.ja3
JA3 client fingerprint hash
tls.ja3s.hash
network.tls.server.ja3s
JA3S server fingerprint hash
app_proto
network.application_protocol
Application layer protocol detected
flow.bytes_toserver
network.sent_bytes
Bytes sent from client to server
flow.bytes_toclient
network.received_bytes
Bytes sent from server to client
flow.pkts_toserver
additional.fields
Packets sent from client to server
flow.pkts_toclient
additional.fields
Packets sent from server to client
in_iface
additional.fields
Input network interface
community_id
network.community_id
Network community ID flow hash
Need more help?
Get answers from Community members and Google SecOps professionals.
