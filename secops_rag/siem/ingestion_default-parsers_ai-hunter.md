# Collect Active Countermeasures AI-Hunter logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter/  
**Scraped:** 2026-03-05T09:18:30.982563Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Active Countermeasures AI-Hunter logs
Supported in:
Google secops
SIEM
This document explains how to ingest Active Countermeasures AI-Hunter logs to Google Security Operations using Bindplane. The parser extracts security alert data from the syslog messages. It parses fields like IP address, current and previous scores, and various contributing factors to the score, then maps these fields to the UDM, enriching the principal with labels representing the extracted data points.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Active Countermeasures AI-Hunter server to edit the configuration file
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
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'AI_HUNTER'
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
<CUSTOMER_ID>
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
Configure Syslog forwarding in Active Countermeasures AI-Hunter
Sign in to the
AI-Hunter server
via SSH with privileged access.
Back up the existing configuration file:
sudo
cp
/etc/AI-Hunter/config.yaml
/etc/AI-Hunter/config.yaml.backup
Edit the configuration file:
sudo
nano
/etc/AI-Hunter/config.yaml
Locate the
Alert:
section and the nested
Syslog:
section. Provide the following configuration details:
Alert
:
Syslog
:
Threshold
:
20
Protocol
:
"udp"
Address
:
"bindplane_host:514"
Tag
:
"
AC-Hunter
"
Threshold
: Enter the minimum threat score to trigger alerts (for example,
20
). Systems with scores at or above this value will generate syslog alerts.
Protocol
: Select
udp
or
tcp
to match your Bindplane configuration. Use
""
(empty string) to write to the host's
/dev/log
for rsyslog forwarding.
Address
: Enter the Bindplane agent IP address and port (for example,
10.1.2.3:514
).
Tag
: Enter an optional tag for log identification (for example,
AC-Hunter
). The vendor recommends including a trailing space before the closing quote.
Save the configuration file and exit the editor.
Restart AI-Hunter to apply the changes:
hunt
up
-d
--force-recreate
Need more help?
Get answers from Community members and Google SecOps professionals.
