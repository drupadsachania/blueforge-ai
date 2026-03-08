# Collect Hitachi Content Platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hitachi-cloud-platform/  
**Scraped:** 2026-03-05T09:56:55.418957Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Hitachi Content Platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest Hitachi Content Platform logs to Google Security Operations using Bindplane.
Hitachi Content Platform (HCP) is a distributed object storage system designed to support large, growing repositories of fixed-content data. HCP provides secure storage with features including data protection, compliance retention, versioning, and multi-protocol access through REST APIs, NFS, CIFS, and WebDAV. The platform supports multi-tenancy with namespace isolation and includes comprehensive system monitoring and logging capabilities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and Hitachi Content Platform
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
System-level user account with administrator or security role in HCP. The monitor or compliance role can view the Syslog page but cannot configure syslog logging or test connections
Access to the HCP System Management Console
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
Configure the Bindplane agent to ingest syslog and send to Google SecOps
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
chronicle/hcp
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
HITACHI_CLOUD_PLATFORM
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
logs/hcp_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/hcp
Configuration parameters
Replace the following placeholders:
Receiver configuration:
The receiver is configured as
udplog
to listen for UDP syslog messages on port 514.
listen_address: "0.0.0.0:514"
listens on all interfaces on port 51. If port 514 requires root privileges on Linux, use port 1514 instead and configure HCP to send to that port.
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
with the customer ID from the previous step.
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
for a complete list.
log_type
: Set to
HITACHI_CLOUD_PLATFORM
exactly as shown.
ingestion_labels
: Optional labels in YAML format (for example,
env: production
).
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
Configure Hitachi Content Platform syslog forwarding
Sign in to the
HCP System Management Console
using an account with administrator or security role.
In the top-level menu, select
Monitoring
>
Syslog
.
In the
Syslog Server IP Addresses
field, enter the IP address of the Bindplane agent host, optionally followed by a colon and port number (for example,
192.168.1.100:514
or
192.168.1.100:1514
). If you omit the port number, HCP uses port 514 by default.
Click
Add
. The specified IP address moves into the list below the field.
In the
Send log messages at this level or higher
field, select the severity level of messages to be sent to the syslog server:
NOTICE
: Sends messages with a severity level of Notice, Warning, or Error.
WARNING
: Sends messages with a severity level of Warning or Error.
ERROR
: Sends only messages with a severity level of Error.
In the
HTTP access Facility
field, select the syslog local facility to which to direct HTTP access log messages. The options are
local0
through
local7
.
To include log messages about HTTP-based data access events, select
Send log messages for HTTP-based data access requests
.
In the
MAPI access Facility
field, select the syslog local facility to which to direct management API log messages. The options are
local0
through
local7
.
To include log messages about management API request events, select
Send log messages for management API requests
.
To include log messages about security events (attempts to log into the System Management Console with an invalid username), select the option to send security events if available.
Click
Update Settings
to save the configuration.
To test the connection, click
Test
on the Syslog page. HCP sends a test message with severity level Notice to the syslog server. Check the Bindplane agent logs to verify the message was received.
UDM mapping table
Log Field
UDM Mapping
Logic
host_name
intermediary.hostname
Hostname of the intermediary device
event_type
metadata.event_type
Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)
product_event
metadata.product_event_type
Product-specific event type
network.application_protocol
Application protocol used (e.g., HTTP, HTTPS)
http_method
network.http.method
HTTP method (e.g., GET, POST)
url
network.http.referral_url
Referral URL for HTTP requests
response_code
network.http.response_code
HTTP response code
src_ip
principal.ip
Source IP address of the connection
metadata.product_name
Product name
metadata.vendor_name
Vendor/company name
Need more help?
Get answers from Community members and Google SecOps professionals.
