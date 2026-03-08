# Collect Cisco Vision Dynamic Signage Director logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stadiumvision/  
**Scraped:** 2026-03-05T09:21:53.791700Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Vision Dynamic Signage Director logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Vision Dynamic Signage Director logs to Google Security Operations using Bindplane agent.
Cisco Vision Dynamic Signage Director (formerly StadiumVision Director) is a digital signage and content management platform designed for stadiums, arenas, and large venues. It enables centralized control and distribution of multimedia content to digital displays, including video walls, scoreboards, and digital menu boards across venue networks.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and Cisco Vision Dynamic Signage Director server
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco Vision Dynamic Signage Director web interface with administrator role
Cisco Vision Dynamic Signage Director Release 6.4 or later (syslog support was added in Release 6.4)
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
chronicle/cisco_vision
:
compression
:
gzip
creds_file_path
:
'<PLACEHOLDER_CREDS_FILE_PATH>'
customer_id
:
'<PLACEHOLDER_CUSTOMER_ID>'
endpoint
:
<
PLACEHOLDER_REGION_ENDPOINT
>
log_type
:
CISCO_STADIUMVISION
raw_log_field
:
body
ingestion_labels
:
source
:
cisco_vision_director
service
:
pipelines
:
logs/cisco_vision_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/cisco_vision
Replace the following placeholders:
Receiver configuration:
The receiver is configured to listen on UDP port
514
on all network interfaces (
0.0.0.0:514
)
Cisco Vision Director sends syslog messages using RFC5424 format over UDP (RFC5426 transport)
Exporter configuration:
<PLACEHOLDER_CREDS_FILE_PATH>
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
<PLACEHOLDER_CUSTOMER_ID>
: Your
customer ID
. For details, see
Get Google SecOps customer ID
.
<PLACEHOLDER_REGION_ENDPOINT>
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
Example configuration
Example
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/cisco_vision
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
CISCO_STADIUMVISION
raw_log_field
:
body
ingestion_labels
:
source
:
cisco_vision_director
env
:
production
service
:
pipelines
:
logs/cisco_vision_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/cisco_vision
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
Configure Cisco Vision Dynamic Signage Director syslog forwarding
Enable syslog on Cisco Vision Director
Sign in to the Cisco Vision Dynamic Signage Director web interface with administrator credentials.
Go to
Configuration
>
System Configuration
>
Dynamic Signage Director Setting
>
Syslog Configuration
.
Select
Enable Syslog
from the Configuration Properties panel.
Click
Edit
. The Edit Configuration Setting dialog box appears.
Select
true
from the dropdown menu.
Click
Save
.
Configure syslog server IP address and port
In the same
Syslog Configuration
section, select
Syslog Server IP & Port
.
Click
Edit
. The Edit Configuration dialog box appears.
In the
Value
field, enter the IP address and port of the Bindplane agent host in the format
IP_ADDRESS:PORT
.
For example:
192.168.1.100:514
Replace
192.168.1.100
with the actual IP address of the Bindplane agent host
Use port
514
to match the Bindplane agent configuration
Click
Save
.
Verify the IP address and port now appear in the
Syslog Server IP & Port
field.
Enable DMP syslog forwarding through Director (optional)
If you want to forward Digital Media Player (DMP) system logs through Cisco Vision Director to the external syslog server:
In the
Syslog Configuration
section, select
Enable DMP Syslog through Director
.
Click
Edit
. The Edit Configuration Setting dialog box appears.
Change the
Value
to
true
.
Click
Save
.
Verify syslog configuration
After saving the configuration, verify that logs are being sent to the Bindplane agent.
Check the Bindplane agent logs for incoming syslog messages:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
You should see log entries indicating successful receipt and forwarding of Cisco Vision Director syslog messages.
Additional configuration resources
For more information about Cisco Vision Dynamic Signage Director syslog configuration, see the following Cisco documentation:
Cisco Vision Dynamic Signage Director Release Notes for Release 6.4
Cisco Vision Dynamic Signage Director Administration Guide Release 6.4
UDM mapping table
Log Field
UDM Mapping
Logic
intem_host
intermediary.hostname
Hostname of the intermediary device
desc, data
metadata.description
Additional description of the event
metadata.event_type
Type of event represented by the log entry
event_category
metadata.product_event_type
Product-specific event type
network.application_protocol
Application protocol used in the connection
method
network.http.method
HTTP method used in the request
response
network.http.response_code
HTTP response code
user_agent
network.http.user_agent
User agent string from the HTTP request
ses
network.session_id
Identifier for the network session
application
principal.application
Application associated with the principal
prin_ip
principal.ip
IP address associated with the principal
pid
principal.process.pid
Process ID of the principal
acct
principal.user.userid
User ID of the principal
action_result
security_result.action
Action taken by the security system
res, task
security_result.action_details
Details of the security action
msg_data, desc
security_result.description
Description of the security result
grantors, method_name, type, name, count, m1_rate, m5_rate, m15_rate, mean_rate, rate_unit, duration_unit
security_result.detection_fields
Additional fields related to detection
severity
security_result.severity
Severity level of the security result
op, act_detail
security_result.summary
Summary of the security result
exe, ENV
target.file.full_path
Full path to the target file
COMMAND
target.process.command_line
Command line of the target process
path, url
target.url
URL associated with the target
USER
target.user.userid
User ID of the target
Need more help?
Get answers from Community members and Google SecOps professionals.
