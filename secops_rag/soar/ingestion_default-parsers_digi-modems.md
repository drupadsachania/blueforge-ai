# Collect Digi Modems logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digi-modems/  
**Scraped:** 2026-03-05T09:54:35.406880Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Digi Modems logs
Supported in:
Google secops
SIEM
This document explains how to ingest Digi Modems logs to
Google Security Operations using Bindplane. The parser code first extracts fields
like timestamp, hostname, product type, and log content from DIGI_MODEMS syslog
messages using grok patterns. Then, it further analyzes the content to identify
login attempts (successful or failed), extracting details like user, IP address,
port, and protocols, ultimately mapping these extracted fields into a Unified
Data Model (UDM) schema for security analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Digi Remote Manager or local Digi Modem web UI
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
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
Windows installation
Open the
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
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
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
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'DIGI_MODEMS'
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
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure the Syslog Server on Digi Modem
Sign in to the
Digi Remote Manager
, or the local
Digi Modem
web UI.
Access the device configuration with
Remote Manager
:
Locate the device you want to configure Syslog for.
Click
Device ID
>
Settings
>
Config
.
Access the device configuration with
local Digi Modem web UI
:
Click
System
>
Configuration
>
Device Configuration
.
Go to
System
>
Log
.
Click to expand
Server list
.
Click
Add Server +
.
Provide the following configuration details:
Server
: Enter the Bindplane agent IP address.
Select the event categories that will be sent to the server (all event categories are enabled by default).
Syslog egress Port
: Enter the Bindplane agent port number (default is
514
).
Protocol
: Select
UDP
.
Click
Apply
.
Supported Digi modems sample logs
SYSLOG
{
  "priority": 14,
  "timestamp": "Dec 28 17:27:45",
  "hostname": "host-device.router",
  "tag": "Eventlog",
  "message": "17:27:33, 28 Dec 2006,Login failure by Host: 10.0.0.25:23: CMD,Telnet"
}
SYSLOG
{
  "priority": 14,
  "timestamp": "May 25 11:03:55",
  "hostname": "internal-srv-01",
  "tag": "Eventlog",
  "message": "11:03:55, 25 May 2023,Login failure by sanitized_user: WEB"
}
SYSLOG
{
  "priority": 14,
  "timestamp": "Jun 11 23:58:26",
  "hostname": "internal-srv-01",
  "tag": "Eventlog",
  "message": "23:58:26, 11 Jun 2023,Login failure by GET /masked_path HTTP/1.0: CMD,Telnet"
}
SYSLOG
{
  "priority": 14,
  "timestamp": "Jun 19 19:52:19",
  "hostname": "gateway-device-02",
  "tag": "Eventlog",
  "message": "19:52:18, 19 Jun 2023,WEB Login OK by internal_admin lvl 0"
}
UDM mapping table
Log field
UDM mapping
Logic
content
security_result.description
Directly mapped from the
content
field after initial grok parsing.
http_method
network.http.method
Extracted from the
content
field using a grok pattern.
http_version
network.application_protocol_version
Extracted from the
content
field using a grok pattern.
hostname
principal.hostname
Extracted from the log message using a grok pattern.
ip
target.ip
Extracted from the
content
field using a grok pattern.
port
target.port
Extracted from the
content
field using a grok pattern and converted to an integer.
proto
network.application_protocol
Extracted from the
content
field using a grok pattern.
ts
metadata.event_timestamp
Extracted from the log message using a grok pattern and converted to a timestamp.
type
login_type_label.value
Extracted from the
content
field using a grok pattern.
extensions.auth.type
Set to
MACHINE
by parser logic.
login_type_label.key
Set to
Login type
by parser logic.
metadata.event_type
Determined by the presence of specific fields like
ip
or
user
and set accordingly to
NETWORK_CONNECTION
or
USER_LOGIN
.
metadata.log_type
Set to
DIGI_MODEMS
by parser logic.
metadata.product_event_type
Extracted from the
product_type
field in the log message.
metadata.product_name
Set to
DIGI_MODEMS
by parser logic.
metadata.vendor_name
Set to
DIGI_MODEMS
by parser logic.
security_result.action
Determined by the presence of
Login OK
or
Login failure
in the message and set to
ALLOW
or
BLOCK
respectively.
user
target.user.userid
Extracted from the
content
field using a grok pattern.
Need more help?
Get answers from Community members and Google SecOps professionals.
