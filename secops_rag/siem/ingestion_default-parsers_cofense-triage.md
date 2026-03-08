# Collect Cofense logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cofense-triage/  
**Scraped:** 2026-03-05T09:22:24.815579Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cofense logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cofense logs into Google Security Operations using the Bindplane agent.
Cofense Triage is a phishing incident response platform that automates the detection, analysis, and response to phishing emails reported by employees. It clusters similar threats, assigns risk scores, extracts indicators of compromise (IOCs), and integrates with security orchestration tools to accelerate phishing incident resolution.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and the Cofense Triage server
If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
Privileged access to the Cofense Triage administration console
Cofense Triage version 1.20 or later
Get the Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
Get the Google SecOps customer ID
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
Configure Bindplane agent to ingest syslog and send logs to Google SecOps
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
chronicle/cofense
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'your-customer-id'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
COFENSE_TRIAGE
raw_log_field
:
body
service
:
pipelines
:
logs/cofense_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/cofense
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on:
0.0.0.0:514
to listen on all interfaces on port 514 (requires root on Linux)
0.0.0.0:1514
to listen on an unprivileged port (recommended for Linux non-root)
Receiver type options:
tcplog
for TCP syslog (recommended for Cofense Triage)
udplog
for UDP syslog
Exporter configuration:
creds_file_path
: Full path to the Google SecOps ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Google SecOps customer ID
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
for the complete list
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
Check the logs for errors:
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
Check the logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Cofense Triage syslog forwarding
Cofense Triage can forward phishing report events and alerts in CEF (Common Event Format) via syslog to external SIEM collectors.
Enable syslog output in Cofense Triage
Sign in to the
Cofense Triage
web interface with administrator credentials.
Go to
Administration
>
System
>
Syslog
.
Enable the
Syslog
toggle.
Configure the following syslog parameters:
Syslog Server
: Enter the IP address or hostname of the Bindplane agent host (for example,
192.168.1.100
).
Port
: Enter the port matching the Bindplane agent
listen_address
(for example,
514
).
Protocol
: Select
TCP
(recommended) or
UDP
to match the Bindplane agent receiver type.
Format
: Select
CEF
(Common Event Format).
Click
Save
.
Configure syslog alerts
In the Cofense Triage web interface, go to
Administration
>
System
>
Syslog Alerts
.
Select the event types to forward:
Phishing reports
: Forwarded when new phishing reports are received and processed
Cluster events
: Forwarded when reports are clustered
Threat indicator events
: Forwarded when IOCs are extracted from reports
Health alerts
: Forwarded for system health and performance events
Click
Save
.
Verify syslog forwarding
After saving the syslog configuration, trigger a test event in Cofense Triage (for example, process a phishing report).
Check the Bindplane agent logs for incoming syslog messages:
Linux
:
sudo journalctl -u observiq-otel-collector -f
Windows
:
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Verify that CEF-formatted messages appear in the logs, for example:
CEF:0|Cofense|Triage|1.0|100|Phishing Report Processed|5|suser=reporter@company.com duser=attacker@malicious.com cs4=Urgent: Account Verification cat=Processed:Threats
UDM mapping table
Log Field
UDM Mapping
Logic
msg, rule_id, start, rt
additional.fields
Merged with labels for msg if not empty, rule_id if not empty, start if not empty, rt if not empty
event_data, descrip
metadata.description
Value from event_data if not empty, else descrip
deviceCustomDate1, log_datetime
metadata.event_timestamp
Parsed from deviceCustomDate1 if not empty, else log_datetime using format MMM d yyyy HH:mm:ss or MMM d HH:mm:ss
suser, duser, has_principal
metadata.event_type
Set to EMAIL_TRANSACTION if suser and duser match email pattern, else GENERIC_EVENT, then STATUS_UPDATE if has_principal true and was GENERIC_EVENT
cs3
metadata.product_log_id
Extracted from cs3 using grok pattern /%{INT:productlogid}
metadata.product_name
Set to "Triage"
cs3
metadata.url_back_to_product
Value copied directly
metadata.vendor_name
Set to "Cofense"
suser
network.email.from
Value copied directly
cs4
network.email.subject
Value copied directly
duser
network.email.to
Value copied directly
host
principal.asset.hostname
Value copied directly
ipaddress
principal.asset.ip
Value copied directly
host
principal.hostname
Value copied directly
ipaddress
principal.ip
Value copied directly
processID
principal.process.pid
Value copied directly
descrip
principal.user.userid
Extracted from descrip using grok pattern User: (%{WORD:user_id})
cat, cs2
security_result.action
Set to ALLOW if cat in ["health","Processed:Marketing","Processed:Non-Malicious"], BLOCK if cat == "Processed:Spam" or "Processed:Threats" or cs2 in ["PM_Intel_CoronaVirus_Keywords","PM_Intel_CredPhish_106159","VU_Potential_Credential_Stealer"]
severity
security_result.alert_state
Set to ALERTING if severity in ["8","10","11","12","13","14"], else NOT_ALERTING
cat, cs2, severity
security_result.category
Set to MAIL_SPAM if cat == "Processed:Spam", MAIL_PHISHING if cs2 in ["PM_Intel_CoronaVirus_Keywords","PM_Intel_CredPhish_106159","VU_Potential_Credential_Stealer"] or severity in ["8","10","11","12","13","14"]
cat
security_result.description
Value copied directly
severity
security_result.rule_id
Value copied directly
cs2
security_result.rule_name
Value copied directly
cat, cs2
security_result.severity
Set to INFORMATIONAL if cat in ["health","Processed:Marketing","Processed:Non-Malicious"], HIGH if cat == "Processed:Spam", CRITICAL if cat == "Processed:Threats", else HIGH if cs2 in ["PM_Intel_CoronaVirus_Keywords","PM_Intel_CredPhish_106159","VU_Potential_Credential_Stealer"]
Need more help?
Get answers from Community members and Google SecOps professionals.
