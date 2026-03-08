# Collect Elastic Windows Event Log Beats logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat/  
**Scraped:** 2026-03-05T09:23:44.884454Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Elastic Windows Event Log Beats logs
Supported in:
Google secops
SIEM
This document explains how to ingest Elastic Windows Event Log Beats logs into Google Security Operations using the Bindplane agent.
Winlogbeat is Elastic's Windows-specific event log shipping agent that collects Windows Event Logs and forwards them to various destinations. It runs as a Windows service on Windows systems and can collect events from Application, Security, System, and other Windows event log channels.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or a Linux host with
systemd
for running the Bindplane agent
Network connectivity between the Bindplane agent and the Logstash server
Network connectivity between Logstash and the Bindplane agent
If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
Windows systems where Winlogbeat will be installed to collect event logs
Administrator access to Windows systems for Winlogbeat installation
Logstash server (version 7.x or 8.x) for intermediary processing
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
tcplog
:
listen_address
:
"0.0.0.0:1514"
exporters
:
chronicle/winlogbeat
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
ELASTIC_WINLOGBEAT
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
winlogbeat
service
:
pipelines
:
logs/winlogbeat_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/winlogbeat
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:1514
to listen on all interfaces on port 1514 (TCP). You can change the port number if needed, but ensure that it matches the Logstash syslog output configuration.
Exporter configuration:
<CREDS_FILE_PATH>
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
<CUSTOMER_ID>
: Customer ID from the previous step
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
See
Regional Endpoints
for complete list
Example configuration:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:1514"
exporters
:
chronicle/winlogbeat
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
ELASTIC_WINLOGBEAT
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
winlogbeat
service
:
pipelines
:
logs/winlogbeat_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/winlogbeat
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
Install and configure Logstash
Logstash is required as an intermediary to receive events from Winlogbeat and forward them to the Bindplane agent via syslog. Winlogbeat does not have native syslog output capability.
Install Logstash
Download Logstash from the
Elastic downloads page
.
Install Logstash on a Windows or Linux server:
Linux (Debian/Ubuntu):
wget
-qO
-
https://artifacts.elastic.co/GPG-KEY-elasticsearch
|
sudo
apt-key
add
-
sudo
apt-get
install
apt-transport-https
echo
"deb https://artifacts.elastic.co/packages/8.x/apt stable main"
|
sudo
tee
-a
/etc/apt/sources.list.d/elastic-8.x.list
sudo
apt-get
update
&&
sudo
apt-get
install
logstash
Linux (RHEL/CentOS):
sudo
rpm
--import
https://artifacts.elastic.co/GPG-KEY-elasticsearch
sudo
tee
/etc/yum.repos.d/logstash.repo
<<EOF
[
logstash-8.x
]
name
=
Elastic
repository
for
8
.x
packages
baseurl
=
https://artifacts.elastic.co/packages/8.x/yum
gpgcheck
=
1
gpgkey
=
https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled
=
1
autorefresh
=
1
type
=
rpm-md
EOF
sudo
yum
install
logstash
Windows:
Download the ZIP file from the Elastic downloads page.
Extract to
C:\logstash
.
Configure Logstash pipeline
Create a new pipeline configuration file:
Linux:
sudo
nano
/etc/logstash/conf.d/winlogbeat-to-syslog.conf
Windows:
notepad "C:\logstash\config\winlogbeat-to-syslog.conf"
Add the following configuration:
input {
    beats {
        port => 5044
    }
}

output {
    syslog {
        host => "<BINDPLANE_AGENT_IP>"
        port => 1514
        protocol => "tcp"
        rfc => "rfc5424"
        appname => "winlogbeat"
        facility => "user-level"
        severity => "informational"
    }
}
Replace
<BINDPLANE_AGENT_IP>
with the IP address of the server running the Bindplane agent.
Example Logstash configuration
input {
    beats {
        port => 5044
    }
}

output {
    syslog {
        host => "192.168.1.100"
        port => 1514
        protocol => "tcp"
        rfc => "rfc5424"
        appname => "winlogbeat"
        facility => "user-level"
        severity => "informational"
    }
}
Start Logstash
Linux:
Start Logstash:
sudo
systemctl
start
logstash
sudo
systemctl
enable
logstash
Verify Logstash is running:
sudo
systemctl
status
logstash
Check Logstash logs:
sudo
tail
-f
/var/log/logstash/logstash-plain.log
Windows:
cd C:\logstash\bin
logstash.bat -f C:\logstash\config\winlogbeat-to-syslog.conf
For production use, install Logstash as a Windows service using NSSM or similar tools.
Install Winlogbeat on Windows systems
Download Winlogbeat
Download Winlogbeat from the
Elastic downloads page
.
Choose the ZIP or MSI installer for Windows.
Install Winlogbeat
Using MSI installer:
Run the MSI installer.
Follow the installation wizard.
Install to the default location:
C:\Program Files\Winlogbeat
.
Using ZIP file:
Extract the ZIP file to
C:\Program Files\Winlogbeat
.
Open
PowerShell
as an administrator.
Navigate to the Winlogbeat directory:
cd
'C:\Program Files\Winlogbeat'
Run the installation script:
.\
install-service
-winlogbeat
.
ps1
Configure Winlogbeat to send logs to Logstash
Open the Winlogbeat configuration file:
notepad "C:\Program Files\Winlogbeat\winlogbeat.yml"
Configure the event logs to collect. Locate the
winlogbeat.event_logs
section and configure as follows:
winlogbeat.event_logs
:
-
name
:
Application
ignore_older
:
72h
-
name
:
System
-
name
:
Security
-
name
:
Microsoft-Windows-Sysmon/Operational
ignore_older
:
72h
-
name
:
Windows PowerShell
event_id
:
400, 403, 600, 800
-
name
:
Microsoft-Windows-PowerShell/Operational
event_id
:
4103, 4104, 4105, 4106
-
name
:
ForwardedEvents
tags
:
[
forwarded
]
Comment out the Elasticsearch output section by adding
#
at the beginning of each line:
#output.elasticsearch:
#  hosts: ["localhost:9200"]
Uncomment and configure the Logstash output section:
output.logstash
:
hosts
:
[
"<LOGSTASH_SERVER_IP>:5044"
]
Replace
<LOGSTASH_SERVER_IP>
with the IP address of your Logstash server.
Example Winlogbeat configuration
winlogbeat.event_logs
:
-
name
:
Application
ignore_older
:
72h
-
name
:
System
-
name
:
Security
-
name
:
Microsoft-Windows-Sysmon/Operational
ignore_older
:
72h
output.logstash
:
hosts
:
[
"192.168.1.50:5044"
]
Save the configuration file
Save and close the file.
Start Winlogbeat service
Open
PowerShell
as an administrator.
Start the Winlogbeat service:
Start-Service
winlogbeat
Verify the service is running:
Get-Service
winlogbeat
The status should show as
Running
.
Check Winlogbeat logs for errors:
Get-Content
"C:\ProgramData\winlogbeat\Logs\winlogbeat"
-Tail
50
Verify log flow
Verify Winlogbeat to Logstash connection
On the Logstash server, check the Logstash logs:
Linux:
sudo
tail
-f
/var/log/logstash/logstash-plain.log
Windows:
type
C
:
\
logstash
\
logs
\
logstash
-
plain
.
log
Look for messages indicating Beats connections:
[INFO ][logstash.inputs.beats] Beats inputs: Starting input listener {:address=>"0.0.0.0:5044"}
Verify Logstash to Bindplane agent connection
On the Bindplane agent server, check the agent logs:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Look for messages indicating successful log ingestion.
Verify logs in Google SecOps
Sign in to the Google SecOps console.
Go to
Search
.
Run a search query to verify Winlogbeat logs are being ingested:
metadata.log_type = "ELASTIC_WINLOGBEAT"
Verify that Windows event logs appear in the search results.
Troubleshooting
Winlogbeat not connecting to Logstash
Verify network connectivity between Winlogbeat and Logstash:
Test-NetConnection
-ComputerName
<
LOGSTASH_IP
>
-Port
5044
Check Windows Firewall rules allow outbound connections on port 5044.
Verify Logstash is listening on port 5044:
Linux:
sudo
netstat
-tulpn
|
grep
5044
Windows:
netstat -an | findstr 5044
Logstash not forwarding to Bindplane agent
Verify network connectivity between Logstash and Bindplane agent:
Linux:
telnet
<BINDPLANE_IP>
1514
Windows:
Test-NetConnection -ComputerName <BINDPLANE_IP> -Port 1514
Check firewall rules allow TCP connections on port 1514.
Verify Bindplane agent is listening on port 1514:
Linux:
sudo
netstat
-tulpn
|
grep
1514
Windows:
netstat -an | findstr 1514
Logs not appearing in Google SecOps
Verify the customer ID and ingestion authentication file are correct.
Check the Bindplane agent logs for authentication errors.
Verify the regional endpoint matches your Google SecOps instance region.
Ensure the
log_type
is set to
ELASTIC_WINLOGBEAT
exactly as shown.
UDM mapping table
Field mapping information is not available for this parser.
Need more help?
Get answers from Community members and Google SecOps professionals.
