# Collect FireEye NX Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit/  
**Scraped:** 2026-03-05T09:55:53.714282Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FireEye NX Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest FireEye NX Audit logs to Google Security Operations using Bindplane agent.
FireEye NX Audit is a network security appliance that detects and blocks attacks from the web, protecting against drive-by malware and highly targeted zero-day exploits. It leverages the Multi-Vector Virtual Execution (MVX) engine to identify malicious activity and command-and-control callbacks with extremely low false positive rates.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and FireEye NX Audit appliance
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the FireEye NX Audit management console or appliance
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
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/fireeye_nx
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
FIREEYE_NX_AUDIT
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
trellix_nx
service
:
pipelines
:
logs/fireeye_nx_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/fireeye_nx
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on:
0.0.0.0:514
to listen on all interfaces on port 514 (requires root/admin privileges)
0.0.0.0:1514
for unprivileged port (recommended for Linux non-root)
Specific IP address to listen on one interface
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
with the Customer ID from the previous step
endpoint
: Regional endpoint URL:
United States
:
malachiteingestion-pa.googleapis.com
Europe (Frankfurt)
:
europe-west3-malachiteingestion-pa.googleapis.com
Europe (London)
:
europe-west2-malachiteingestion-pa.googleapis.com
Europe (Zurich)
:
europe-west6-malachiteingestion-pa.googleapis.com
Asia (Tokyo)
:
asia-northeast1-malachiteingestion-pa.googleapis.com
Australia (Sydney)
:
australia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
: Set to
FIREEYE_NX_AUDIT
(exact match required)
ingestion_labels
: Optional labels in YAML format for categorizing logs
Example configuration for TCP syslog
If you prefer TCP for reliable delivery, modify the receiver section:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/fireeye_nx
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
FIREEYE_NX_AUDIT
raw_log_field
:
body
service
:
pipelines
:
logs/fireeye_nx_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/fireeye_nx
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
Configure FireEye NX Audit syslog forwarding
Sign in to the
FireEye NX Audit
console with an administrator account.
Go to
Settings
>
Notifications
.
Click the
rsyslog
tab.
Select the
Event type
checkbox to enable rsyslog notifications.
In the
Settings
panel, provide the following configuration details:
Default format
: Select
CEF
(Common Event Format).
In the
Rsyslog Server Listing
section:
Type a descriptive name for the new entry (for example,
Google SecOps BindPlane
).
Click the
Add Rsyslog Server
button.
For the newly added server, provide the following configuration details:
Enabled
: Check the checkbox to enable the server.
IP Address
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
Port
: Enter the Bindplane agent port number (for example,
514
).
Protocol
: Select
UDP
or
TCP
, depending on your Bindplane agent configuration.
Select
UDP
if you configured
udplog
receiver in Bindplane.
Select
TCP
if you configured
tcplog
receiver in Bindplane.
Delivery
: Select
Per Event
from the list.
Notifications
: Select
All Events
from the list to forward all event types.
Format
: Verify
CEF
is selected (should inherit from default format setting).
Account
: Leave this field empty.
Click the
Update
button to save the configuration.
Verify logs are being sent by checking the Bindplane agent logs:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
UDM mapping table
Log field
UDM mapping
Logic
alert.dst.ip
target.ip, target.asset.ip
Direct mapping from alert.dst.ip field
alert.dst.mac
target.mac, target.asset.mac
Direct mapping from alert.dst.mac field
alert.dst.port
target.port
Direct mapping from alert.dst.port field
alert.explanation.cnc-services.cnc-service.address
target.ip, target.asset.ip
Direct mapping from alert.explanation.cnc-services.cnc-service.address field
alert.explanation.cnc-services.cnc-service.port
target.port
Direct mapping from alert.explanation.cnc-services.cnc-service.port field
alert.explanation.cnc-services.cnc-service.url
target.url
Direct mapping from alert.explanation.cnc-services.cnc-service.url field
alert.explanation.malware-detected.malware.0.name
security_result.threat_name
Direct mapping from alert.explanation.malware-detected.malware.0.name field in case of multiple malware detection in array
alert.explanation.malware-detected.malware.md5sum
target.file.md5
Direct mapping from alert.explanation.malware-detected.malware.md5sum field
alert.explanation.malware-detected.malware.name
security_result.threat_name
Direct mapping from alert.explanation.malware-detected.malware.name field
alert.explanation.malware-detected.malware.sha1
target.file.sha1
Direct mapping from alert.explanation.malware-detected.malware.sha1 field
alert.explanation.malware-detected.malware.sha256
target.file.sha256
Direct mapping from alert.explanation.malware-detected.malware.sha256 field
alert.explanation.malware-detected.malware.url
target.url
Direct mapping from alert.explanation.malware-detected.malware.url field
alert.name
read_only_udm.metadata.product_event_type
Direct mapping from alert.name field
alert.occurred
read_only_udm.metadata.event_timestamp
Direct mapping from alert.occurred field
alert.src.domain
principal.hostname
Direct mapping from alert.src.domain field
alert.src.host
principal.hostname
Direct mapping from alert.src.host field
alert.src.ip
principal.ip, principal.asset.ip
Direct mapping from alert.src.ip field
alert.src.mac
principal.mac, principal.asset.mac
Direct mapping from alert.src.mac field
alert.src.port
principal.port
Direct mapping from alert.src.port field
alert.src.smtp-mail-from
network.email.from
Direct mapping from alert.src.smtp-mail-from field
alert.smtp-message.id
network.email.mail_id
Direct mapping from alert.smtp-message.id field
alert.smtp-message.subject
network.email.subject
Direct mapping from alert.smtp-message.subject field
read_only_udm.metadata.event_type
Set to SCAN_UNCATEGORIZED if both principal and target IP addresses are present, STATUS_UPDATE if principal IP or hostname is present, USER_UNCATEGORIZED if principal user ID is present, EMAIL_TRANSACTION if both alert.src.smtp-mail-from and alert.dst.smtp-to are present, and GENERIC_EVENT otherwise
read_only_udm.metadata.log_type
Set to FIREEYE_NX_AUDIT
read_only_udm.metadata.vendor_name
Set to FireEye
read_only_udm.security_result.action
Set to ALLOW if action is "notified", BLOCK if action is "blocked", and UNKNOWN_ACTION otherwise
read_only_udm.security_result.category
Set to NETWORK_SUSPICIOUS if sec_category contains "DOMAIN.MATCH", NETWORK_MALICIOUS if sec_category contains "INFECTION.MATCH" or "WEB.INFECTION", SOFTWARE_MALICIOUS if sec_category contains "MALWARE.OBJECT", NETWORK_COMMAND_AND_CONTROL if sec_category contains "MALWARE.CALLBACK", and UNKNOWN_CATEGORY otherwise
read_only_udm.security_result.severity
Set to MEDIUM if severity is "majr", LOW if severity is "minr"
Need more help?
Get answers from Community members and Google SecOps professionals.
