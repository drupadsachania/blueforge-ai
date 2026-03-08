# Collect Illumio Core logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/illumio-core/  
**Scraped:** 2026-03-05T09:25:37.163176Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Illumio Core logs
Supported in:
Google secops
SIEM
This document explains how to ingest Illumio Core logs to Google Security Operations using Bindplane.
The parser extracts fields from Illumio Core JSON, SYSLOG, SYSLOG+JSON and SYSLOG+CEF formatted logs. It uses grok and/or JSON parsing to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Illumio Policy Compute Engine (PCE) web console
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
tcplog
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
'ILLUMIO_CORE'
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
tcplog
exporters
:
-
chronicle/chronicle_w_labels
Configuration parameters
Replace the following placeholders:
Receiver configuration:
tcplog
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
ILLUMIO_CORE
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
Configure Syslog forwarding on Illumio Core
Sign in to the
Illumio Policy Compute Engine (PCE)
web console.
Go to
Settings
>
Event Settings
.
In the
Syslog Destinations
section, click
Add
.
Provide the following configuration details:
Description
: Enter a descriptive name (for example,
Google-SecOps-Bindplane
).
Remote Syslog Destination
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Protocol
: Select
TCP
.
Severity
: Select
Informational
(or your preferred severity level, Level 6 is recommended for comprehensive logging).
Format
: Select
CEF
(Common Event Format) for structured parsing.
In the
Event Types
section, select the events to forward:
Organization Events
: Organization-level changes
Auditable Events
: User and API audit trail
Traffic Flow Events
: Network flow summaries
Node Events
: VEN and workload status changes
Click
Save
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
Alternatively, configure via API:
curl -X POST "https://PCE_HOST:8443/api/v2/orgs/ORG_ID/settings/syslog/destinations" \
   -H "Content-Type: application/json" \
   -u "API_KEY:API_SECRET" \
   -d '{
      "description": "Google-SecOps-Bindplane",
      "remote_syslog": "BINDPLANE_IP",
      "remote_syslog_port": 514,
      "remote_syslog_protocol": 6,
      "severity": 6,
      "type": "cef"
   }'
Replace
PCE_HOST
,
ORG_ID
,
API_KEY
,
API_SECRET
, and
BINDPLANE_IP
with your values.
Need more help?
Get answers from Community members and Google SecOps professionals.
