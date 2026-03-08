# Collect Tanium Insight logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-insight/  
**Scraped:** 2026-03-05T09:29:02.698558Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Insight logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Insight logs to Google Security Operations using Bindplane. The parser extracts fields from Tanium Insight syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Tanium Console (Connect module) to configure a Syslog (Socket/SIEM) destination
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
For additional installation options, consult this
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
'TANIUM_INSIGHT'
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
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding on Tanium Insight
Sign in to the
Tanium Console
with administrator privileges.
Go to
Modules
>
Connect
>
Overview
.
Select
Create Connection
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Insight Integration
).
Description
: Optional description for this connection.
Source
: Select a Tanium Insight source (for example, a saved report from the Insight module that outputs the fields you need).
Destination
: Select
Socket (SIEM) / Syslog
.
Host
: Enter the BindPlane Agent IP address.
Port
: Enter the BindPlane Agent port number (for example,
514
).
Transport
: Select
UDP
to match the receiver configuration (or configure TCP/TLS on both sides if required in your environment).
Format
: Select
Syslog RFC 5424
(KV format).
Timezone
: Select UTC timezone for universal consistency across systems.
Recommended: In
Configure Output
>
Columns
, add Insight fields and format them as
key=value
pairs to align with Google SecOps's
SYSLOG + KV
parser for
TANIUM_INSIGHT
.
Click
Save
to start forwarding.
Need more help?
Get answers from Community members and Google SecOps professionals.
