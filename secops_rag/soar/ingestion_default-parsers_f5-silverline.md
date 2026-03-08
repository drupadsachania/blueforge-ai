# Collect F5 Silverline logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline/  
**Scraped:** 2026-03-05T09:55:34.143316Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 Silverline logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 Silverline logs to Google Security Operations using Bindplane agent.
F5 Silverline is a cloud-based security service platform that provides DDoS protection, Web Application Firewall (WAF), and IP Intelligence services. The platform protects applications and infrastructure from distributed denial-of-service attacks, web application exploits, and malicious traffic through F5's global scrubbing centers and security operations center.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and the internet
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Access to the F5 Silverline portal with administrative privileges
Firewall rules allowing inbound TLS+TCP traffic on port 6514 to the Bindplane agent host
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
tcplog
:
listen_address
:
"0.0.0.0:6514"
exporters
:
chronicle/f5_silverline
:
compression
:
gzip
creds_file_path
:
'<CREDS_FILE_PATH>'
customer_id
:
'<CUSTOMER_ID>'
endpoint
:
<
REGION_ENDPOINT
>
log_type
:
F5_SILVERLINE
raw_log_field
:
body
ingestion_labels
:
env
:
production
service
:
pipelines
:
logs/silverline_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/f5_silverline
Configuration parameters
Replace the following placeholders:
<CREDS_FILE_PATH>
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
<CUSTOMER_ID>
: Your Google SecOps customer ID from the previous step
<REGION_ENDPOINT>
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
Example configuration
Example configuration:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:6514"
exporters
:
chronicle/f5_silverline
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
F5_SILVERLINE
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
silverline
service
:
pipelines
:
logs/silverline_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/f5_silverline
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
To restart the Bindplane agent in Linux, do the following:
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
To restart the Bindplane agent in Windows, do the following:
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
Configure F5 Silverline syslog forwarding
Sign in to the
F5 Silverline portal
at
https://portal.f5silverline.com
.
Go to
Config
>
Log Export
.
In the
IP address
field, enter the IP address of the Bindplane agent host.
In the
Port
field, enter
6514
.
From the
Protocol
list, select
TCP
.
From the
Format
list, select
Auto
.
Click
Save
to apply the configuration.
Log types forwarded
F5 Silverline forwards the following log types through syslog:
DDoS Mitigation Logs
: Information about DDoS attacks, mitigation actions, and filtered traffic
WAF Logs
: Web Application Firewall violation events, attack types, and blocked requests
IP Intelligence Logs
: Threat intelligence data about malicious IP addresses
Network Traffic Logs
: Network-level traffic analysis and anomaly detection
Proxy Logs
: HTTP/HTTPS proxy events and connection details
Verify log export
In the F5 Silverline portal, go to
Config
>
Log Export
.
Verify the connection status shows as
Active
or
Connected
.
Check the Bindplane agent logs to confirm syslog messages are being received:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
In the Google SecOps console, go to
SIEM
>
Search
and search for
metadata.log_type = "F5_SILVERLINE"
to verify logs are being ingested.
UDM mapping table
Log field
UDM mapping
Logic
content_length, geo_location, policy_apply_date, policy_name, flow_id, errdefs_msgno, ip_intelligence_threat_name, log_type, loglevel, msg_type, proxy_id, request_side, tmm_unit, disable_asm, disable_bot, policy_name, http_class_name, reason, protocol, mitigation, countermeasure, blacklisted, msg_type, proxy_id, request_side, route_domain, sa_translation_type, sa_translation_pool, translated_vlan, translated_source_port, translated_source_ip, translated_route_domain, translated_ip_protocol, translated_dest_port
additional.fields
Merged as labels into additional.fields if not empty
app_protocol_output
event.idm.read_only_udm.network.application_protocol
Value copied directly if not empty
method
event.idm.read_only_udm.network.http.method
Value copied directly
response_code
event.idm.read_only_udm.network.http.response_code
Value copied directly
source_ip, vs_ip
event.idm.read_only_udm.src.asset.ip
Value from vs_ip if not empty, else source_ip
vs_port, src_port
event.idm.read_only_udm.src.port
Value from vs_port if not empty, else src_port
x_forwarded_for_header_value, header_ip
intermediary.asset.ip
Value from header_ip if not empty, else x_forwarded_for_header_value
x_forwarded_for_header_value, header_ip
intermediary.ip
Value from header_ip if not empty, else x_forwarded_for_header_value
errdefs_msg_name
metadata.description
Value copied directly if not empty
ts
metadata.event_timestamp
Parsed from ts using date match with format MMM dd HH:mm:ss or MMM d HH:mm:ss
event_type
metadata.event_type
Value copied directly
support_id
metadata.product_log_id
Value copied directly if not empty
protocol
network.application_protocol
Set to protocol if equals HTTPS
method, uri_data
network.http.method
Value from uri_data if not empty, else method
response_code
network.http.response_code
Value copied directly, then converted to integer
user_agent
network.http.user_agent
Value copied directly
ip_protocol
network.ip_protocol
Set to "TCP" if matches tcp
virtualserver
network.tls.client.server_name
Value copied directly if not empty
web_application_name
principal.application
Value copied directly
hostname
principal.asset.hostname
Value copied directly
ip_client, source_ip, client_ip, addr, source_ip, vs_ip
principal.asset.ip
Value from ip_client if type=waf; source_ip if type=ipi; client_ip if type=irule; vs_ip if not empty in kvdata, else source_ip if not empty, else client_ip if not empty, else addr if not empty, else ip_client
host, hostname
principal.hostname
Value from hostname if not empty, else host
ip_client, source_ip, client_ip, addr, source_ip, vs_ip
principal.ip
Value from ip_client if type=waf; source_ip if type=ipi; client_ip if type=irule; vs_ip if not empty in kvdata, else source_ip if not empty, else client_ip if not empty, else addr if not empty, else ip_client
geo_location, client_ip_geo_location
principal.location.name
Value from client_ip_geo_location if not empty, else geo_location
snat_ip
principal.nat_ip
Value copied directly
snat_port
principal.nat_port
Value copied directly, then converted to integer
client_port, source_port, client_port
principal.port
Value from client_port if type=irule; source_port if not empty in kvdata, else client_port
host, data.uri, client_request_uri
principal.url
Value from data.uri if type=irule; client_request_uri if not empty in kvdata, else host
service_id
principal.user.product_object_id
Value copied directly
sec_action
security_result.action
Set to BLOCK if request_status in [Blocking, blocked, drop, challenged] or action in [Blocking, blocked, drop]; ALLOW if request_status in [allow, Allow] or action in [allow, Allow, accept]; else UNKNOWN_ACTION
action, request_status, data.action
security_result.action_details
Value from data.action if type=irule; request_status if kvdata; action if type=ipi
attack_type
security_result.category_details
Value copied directly if not empty
sub_violations, context_name, sub_violations
security_result.description
Value from sub_violations if type=waf or kvdata; context_name if type=ipi
request_status
security_result.detection_fields
Added as label to security_result.detection_fields
ip_intelligence_policy_name, irule, irule, ip_intelligence_policy_name
security_result.rule_name
Value from irule if type=irule or kvdata; ip_intelligence_policy_name if type=ipi or kvdata
irule-version
security_result.rule_version
Value copied directly
severity
security_result.severity
Set to CRITICAL if Critical; ERROR if Error; INFORMATIONAL if Informational; HIGH if 5
violations, data.action
security_result.summary
Value from violations if type=waf; data.action if type=irule
ip_intelligence_threat_name
security_result.threat_name
Value copied directly
source_ip
src.asset.ip
Value copied directly
src_port, source_port
src.port
Value copied directly, then converted to integer
dest_ip, bigip_mgmt_ip, dest_ip, server_ip, bigip_mgmt_ip, dest_ip, t_ip
target.asset.ip
Value from dest_ip if type=waf; dest_ip if type=ipi; server_ip if type=irule; bigip_mgmt_ip if not empty in kvdata, else dest_ip if not empty, else t_ip
dest_ip, bigip_mgmt_ip, dest_ip, server_ip, bigip_mgmt_ip, dest_ip, t_ip
target.ip
Value from dest_ip if type=waf; dest_ip if type=ipi; server_ip if type=irule; bigip_mgmt_ip if not empty in kvdata, else dest_ip if not empty, else t_ip
dest_port, dest_port, server_port, dest_port, dst_port
target.port
Value copied directly, then converted to integer
uri
target.url
Value copied directly
metadata.vendor_name
Set to "SILVERLINE"
metadata.product_name
Set to "SILVERLINE"
Need more help?
Get answers from Community members and Google SecOps professionals.
