# Collect Broadcom CA PAM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam/  
**Scraped:** 2026-03-05T09:51:34.923384Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Broadcom CA PAM logs
Supported in:
Google secops
SIEM
This document explains how to ingest Broadcom CA PAM
Privileged Access Management (PAM) logs to Google Security Operations using Bindplane.
The parser extracts data from the SYSLOG, normalizes the extracted fields, and
maps them to the Google SecOps Unified Data Model (UDM). It
handles various event types, enriching the data with relevant context and
security outcomes.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Broadcom Privileged Access Management
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
Install the Bindplane the agent
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
'BROADCOM_CA_PAM'
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
Configure Remote Syslog on Broadcom PAM
Sign in to the
Privileged Access Management
web UI.
Go to
Configuration
>
Logs
>
Syslog
.
Select the
Syslog Enabled
toggle.
Select
Space Delimited
from the
Message Format
list.
Click
Add Server
.
Provide the following configuration details in the new row:
Server column field
: Enter the Bindplane agent IP address.
Enter a Port value for the Bindplane agent (If you leave the port blank, it defaults to
514
).
Select the
UDP
Protocol (If you select
TCP
, the
TLS
option becomes available).
Click
Update
to save the settings.
Need more help?
Get answers from Community members and Google SecOps professionals.
