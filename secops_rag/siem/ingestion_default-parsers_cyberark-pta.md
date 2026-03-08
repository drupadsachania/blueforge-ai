# Collect CyberArk Privileged Threat Analytics logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pta/  
**Scraped:** 2026-03-05T09:22:55.106194Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CyberArk Privileged Threat Analytics logs
Supported in:
Google secops
SIEM
This document explains how to collect CyberArk Privileged Threat Analytics logs by using Bindplane. CyberArk Privileged Threat Analytics is a security solution that helps to detect and respond to malicious activities involving privileged accounts. It uses advanced analytics and machine learning to monitor, analyze, and flag abnormal behaviors that may indicate potential insider threats or compromised credentials.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Cyberark PTA.
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
creds
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
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
cyberark_pta
raw_log_field
:
body
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
Configure CyberArk Privileged Threat Analytics log export
Sign in to the
Privileged Threat Analytics
machine.
Run the
DEFAULTPARM
command to open the default
systemparm.properties
file.
Copy the line containing the
syslog_outbound
property and exit the
systemparm.properties
file.
Run the
LOCALPARM
command to open the local
systemparm.properties
file.
Press
i
on the keyboard to edit the file.
In the
systemparm.properties
file, uncomment the
syslog_outbound
property.
Paste the line that you copied earlier and edit the parameters according to the following example:
syslog_outbound=[{"siem": "Chronicle", "format": "CEF", "host": "
BINDPLANE_IP_ADDRESS
", "port":
BINDPLANE_PORT_NUMBER
, "protocol": "
PROTOCOL
"}]
Replace the following:
BINDPLANE_IP_ADDRESS
: enter the Bindplane IP address.
PORT_NUMBER
: enter the Bindplane port number (for example,
514
).
PROTOCOL
: Enter
UDP
as the protocol.
Save the configuration file and close it.
Restart the
Privileged Threat Analytics
machine.
Need more help?
Get answers from Community members and Google SecOps professionals.
