# Collect RSA Authentication Manager logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-auth-manager/  
**Scraped:** 2026-03-05T09:27:52.405372Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect RSA Authentication Manager logs
Supported in:
Google secops
SIEM
This document explains how to ingest RSA Authentication Manager logs to Google Security Operations using Bindplane.
RSA Authentication Manager (now RSA SecurID) is a multi-factor authentication platform that provides two-factor authentication using tokens, push notifications, and biometrics. It manages user identities, authentication policies, and generates audit logs for authentication attempts across the enterprise. The parser extracts fields from RSA Authentication Manager CSV formatted logs. It uses grok to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the RSA Security Console (Operations Console)
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
'RSA_AUTH_MANAGER'
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
RSA_AUTH_MANAGER
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
Configure Syslog forwarding on RSA Authentication Manager
Sign in to the
RSA Security Console
(Operations Console).
Go to
Setup
>
System Settings
>
Logging
.
Under
Remote Logging
, click
Add Remote Log Server
.
Provide the following configuration details:
Hostname/IP Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Protocol
: Select
UDP
.
In the
Log Level
section, configure the logging levels:
System Activity Log
: Select
Info
or higher.
Administrator Activity Log
: Select
Info
or higher.
Runtime Authentication Log
: Select
Info
or higher.
In the
Log Format
section:
Format
: Select
CSV
(Comma-Separated Values).
Click
Save
.
Alternatively, configure via CLI on the RSA appliance:
manage-logging --set-remote-logging --host BINDPLANE_IP --port 514 --protocol UDP
Replace
BINDPLANE_IP
with the IP address of the Bindplane agent host.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
clientip
principal.asset.ip
The value of column8 from the raw log.
clientip
principal.ip
The value of column8 from the raw log.
column1
metadata.event_timestamp.seconds
Parsed from the time field (column1) in the raw log, using formats "yyyy-MM-dd HH:mm:ss" and "yyyy-MM-dd HH: mm:ss".
column12
security_result.action
Mapped based on the operation_status field (column12). Values "SUCCESS" and "ACCEPT" map to ALLOW, "FAIL", "REJECT", "DROP", "DENY", "NOT_ALLOWED" map to BLOCK, and other values map to UNKNOWN_ACTION.
column18
principal.user.userid
The value of column18 from the raw log.
column19
principal.user.first_name
The value of column19 from the raw log.
column20
principal.user.last_name
The value of column20 from the raw log.
column25
principal.hostname
The value of column25 from the raw log.
column26
principal.asset.hostname
The value of column26 from the raw log.
column27
metadata.product_name
The value of column27 from the raw log.
column3
target.administrative_domain
The value of column3 from the raw log.
column32
principal.user.group_identifiers
The value of column32 from the raw log.
column5
security_result.severity
Mapped based on the severity field (column5). Values "INFO", "INFORMATIONAL" map to INFORMATIONAL, "WARN", "WARNING" map to WARNING, "ERROR", "CRITICAL", "FATAL", "SEVERE", "EMERGENCY", "ALERT" map to ERROR, "NOTICE", "DEBUG", "TRACE" map to DEBUG, and other values map to UNKNOWN_SEVERITY.
column8
target.asset.ip
The value of column8 from the raw log.
column8
target.ip
The value of column8 from the raw log.
event_name
security_result.rule_name
The value of column10 from the raw log.
host_name
intermediary.hostname
Extracted from the
portion of the raw log using grok patterns.
process_data
principal.process.command_line
Extracted from the
portion of the raw log using grok patterns.
summary
security_result.summary
The value of column13 from the raw log.
time_stamp
metadata.event_timestamp.seconds
Extracted from the
portion of the raw log using grok patterns. If not found, the timestamp is extracted from the timestamp field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
