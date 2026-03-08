# Collect Check Point SmartDefense logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-smartdefense/  
**Scraped:** 2026-03-05T09:21:03.704974Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Check Point SmartDefense logs
Supported in:
Google secops
SIEM
This document explains how to ingest Check Point SmartDefense logs to
Google Security Operations using Bindplane. The parser extracts fields from Check
Point SmartDefense syslog formatted logs. It uses grok or kv to parse the log
message and then maps these values to the Unified Data Model (UDM). It also sets
default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
A Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
Privileged access to the Check Point SmartDefense management console or appliance.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Download the
Ingestion Authentication File
.
Save the file securely on the system where Bindplane will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
customer ID
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
'CHECKPOINT_SMARTDEFENSE'
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
<CUSTOMER_ID>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the
authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
observiq-otel-collector
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
sc stop observiq-otel-collector && sc start observiq-otel-collector
Configure Syslog forwarding on Check Point SmartDefense
The following sections describe the steps for setting up Syslog forwarding
on CheckPoint SmartDefense,
Step 1: Create Log Exporter/SIEM Object in SmartConsole
Sign in to the
Check Point SmartConsole
.
Go to
Objects
>
More object types
>
Server
>
Log Exporter/SIEM
.
Click
New
to create a new Log Exporter object.
Provide the following configuration details:
Object Name
: Enter a descriptive name (for example,
Google SecOps Bindplane
).
Export Configuration
: Select
Enabled
.
Target Server
: Enter the Bindplane agent IP address.
Target Port
: Enter
514
(or your configured Bindplane agent port number).
Protocol
: Select
UDP
.
Go to the
Data Manipulation
page.
Provide the following configuration details:
Format
: Select
Common Event Format (CEF)
.
Timezone
: Select UTC time zone for universal consistency across systems.
Click
OK
to save the configuration.
Step 2: Configure Management Server or Log Server
In SmartConsole, go to
Gateways & Servers
.
Open your
Management Server
or
Dedicated Log Server/SmartEvent Server
object.
Go to
Logs
>
Export
.
Click
+
and select the Log Exporter/SIEM object you configured earlier.
Click
OK
.
Step 3: Install Database Policy
From the top menu, click
Install
>
Install database
.
Select
all objects
.
Click
Install
.
Step 4: Verify Log Export Configuration
Connect to the command line on the Management Server-Log Server.
Sign in to
Expert
mode.
Run the following command to verify the configuration:
cp_log_export
show
To restart the Log Exporter if needed:
cp_log_export
restart
Need more help?
Get answers from Community members and Google SecOps professionals.
