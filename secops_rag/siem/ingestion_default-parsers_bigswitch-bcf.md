# Collect Big Switch BigCloudFabric logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bigswitch-bcf/  
**Scraped:** 2026-03-05T09:20:28.338271Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Big Switch BigCloudFabric logs
Supported in:
Google secops
SIEM
This document explains how to ingest Big Switch BigCloudFabric logs to Google Security Operations using Bindplane agent.
Arista Networks Big Cloud Fabric (BCF), now known as Converged Cloud Fabric (CCF), is a software-defined networking (SDN) solution that provides automated data center fabric management through a centralized controller. The BCF/CCF controller manages leaf-spine network architectures, providing centralized configuration, monitoring, and troubleshooting capabilities for enterprise data center networks. This product was originally developed by Big Switch Networks before being acquired by Arista Networks.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and BCF/CCF Controller
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Administrative access to the BCF/CCF Controller via GUI or CLI
BCF/CCF Controller version 2.5 or later (for syslog support)
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
Save the file securely on the 
system where Bindplane is to be installed.
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
chronicle/bigswitch_bcf
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
BIGSWITCH_BCF
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
bcf_controller
service
:
pipelines
:
logs/bcf_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/bigswitch_bcf
Replace the following placeholders:
Receiver configuration:
The receiver is configured to listen on UDP port 514 for syslog messages from the BCF/CCF Controller
To use a different port, change
514
to your desired port number (for example,
1514
for unprivileged Linux installations)
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
: Replace with your
Customer ID
. For details, see
Get Google SecOps customer ID
.
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
: Set to
BIGSWITCH_BCF
(do not change)
ingestion_labels
: Optional labels for categorizing logs (customize as needed)
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
Configure Big Switch BigCloudFabric syslog forwarding
Configure the BCF/CCF Controller to forward syslog messages to the Bindplane agent using either the GUI or CLI method.
Method 1: Configure syslog using the GUI
Sign in to the BCF/CCF Controller web interface using your administrator credentials.
Go to
Maintenance
>
Logging
.
Click the
Remote Logging
tab.
Click
Add
to create a new remote syslog server configuration.
Provide the following configuration details:
Server
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
).
Port
: Enter
514
(or the port configured in the Bindplane agent config.yaml).
Protocol
: Select
UDP
.
Click
Save
or
Apply
to save the configuration.
Verify the configuration appears in the Remote Logging list.
Method 2: Configure syslog using the CLI
Connect to the BCF/CCF Controller via SSH using your administrator credentials.
Enter enable mode:
controller-1> enable
Enter configuration mode:
controller-1# configure
Configure the remote syslog server:
controller-1(config)# logging remote 192.168.1.100
Replace
192.168.1.100
with the IP address of the Bindplane agent host.
Exit configuration mode:
controller-1(config)# exit
Verify the syslog configuration:
controller-1# show logging
The output should display the configured remote syslog server IP address.
Verify log forwarding
Generate test log events on the BCF/CCF Controller by performing configuration changes or viewing system status.
Check the Bindplane agent logs to verify syslog messages are being received:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Sign in to the Google SecOps console and verify logs are appearing in the
Search
interface with the ingestion label
BIGSWITCH_BCF
.
UDM mapping table
Log Field
UDM Mapping
Logic
description
metadata.description
Value copied directly, with leading and trailing spaces removed
target_host, time, product_event_type, description, application
metadata.event_type
Set to STATUS_HEARTBEAT if target_host and time not empty; SERVICE_STOP if product_event_type == PORT_DOWN; SERVICE_START if description matches ".
Running job.
" or product_event_type == PORT_UP or application == snmpd-execstart; STATUS_SHUTDOWN if description matches ".
status down.
"; SERVICE_DELETION if product_event_type == Removing Endpoint; SERVICE_CREATION if product_event_type == Adding Endpoint; SERVICE_MODIFICATION if product_event_type == Moving Endpoint or description matches ".
change instances.
"; NETWORK_CONNECTION if target_host not empty; else GENERIC_EVENT
product_event_type
metadata.product_event_type
Value copied directly
application_protocol
network.application_protocol
Set to "UNKNOWN_APPLICATION_PROTOCOL" if application_protocol == "lldpa"
host
principal.hostname
Value copied directly
ip
principal.ip
Value copied directly
process_id
principal.process.pid
Value copied directly
USER
principal.user.userid
Value copied directly
log_level
security_result
Object with severity set to INFORMATIONAL if INFO, MEDIUM if WARN, HIGH if ERROR; action set to ALLOW if INFO or WARN, BLOCK if ERROR
application
target.application
Value copied directly
target_host
target.hostname
Value copied directly
port
target.port
Converted to integer
COMMAND
target.process.command_line
Value copied directly
product_specific_id
target.process.product_specific_process_id
Prefixed with "Bigswitch:"
kv_1, kv2, kv3
target.user.group_identifiers
Merged from kv_1 if not empty, kv2 if not empty, kv3 if not empty
metadata.product_name
Set to "Big Cloud Fabric"
metadata.vendor_name
Set to "Big Switch"
Need more help?
Get answers from Community members and Google SecOps professionals.
