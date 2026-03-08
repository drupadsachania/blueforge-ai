# Collect AIX system logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aix-system/  
**Scraped:** 2026-03-05T09:18:35.005531Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AIX system logs
Supported in:
Google secops
SIEM
This document explains how to ingest AIX system logs to Google Security Operations using Bindplane. The parser extracts fields from the logs using grok patterns, handling various log formats. It then maps the extracted fields to the UDM, converting data types and setting event types based on the presence of specific fields like source IP, hostname, and user.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2012 SP2 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the AIX system host
Network connectivity between AIX hosts and the Bindplane agent on UDP port 514
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
'AIX_SYSTEM'
raw_log_field
:
body
ingestion_labels
:
environment
:
prod
source
:
aix
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
Configure Syslog forwarding on AIX system
Sign in to the
AIX system host
with privileged access.
Edit the
/etc/syslog.conf
file using a text editor (for example,
vi
or
nano
).
Add the following line to forward logs to the Bindplane agent:
*
.
info
@<BINDPLANE_AGENT_IP>
Replace
<BINDPLANE_AGENT_IP>
with the IP address of the Bindplane agent.
Use one or more tabs or spaces as the separator between the selector (
*.info
) and the action (
@<BINDPLANE_AGENT_IP>
).
The selector
*.info
forwards all logs with
info
priority or higher. Adjust the facility and priority as needed per your requirements.
Save the configuration file.
Refresh the
syslogd
daemon to apply the changes:
refresh
-s
syslogd
If the
refresh
command does not work, restart the daemon using SRC commands:
stopsrc
-s
syslogd
startsrc
-s
syslogd
Verify that the
syslogd
daemon is running:
lssrc
-s
syslogd
Ensure that
UDP port 514
is allowed between the AIX host and the Bindplane agent.
UDM Mapping Table
Log Field
UDM Mapping
Logic
application
target.application
The value is extracted from the
message
field using grok patterns and assigned directly.
cmddata
target.process.command_line
The value is extracted from the
message
field using grok patterns and assigned directly.
command_line
principal.process.command_line
The value is extracted from the
description
field using grok patterns and assigned directly.
description
metadata.description
The value is extracted from the
message
field using grok patterns and assigned directly.
folder
target.process.file.full_path
The value is extracted from the
message
field using grok patterns and assigned directly.
hostname
principal.hostname
The value is extracted from the
message
field using grok patterns and assigned directly. The timestamp is extracted from the
ts
field in the log message using grok and the
date
filter. Determined by parser logic based on the presence of certain fields. If
src_ip
or
hostname
are present, it's
STATUS_UPDATE
. If
user
is present but not the others, it's
USER_UNCATEGORIZED
. Otherwise, it's
GENERIC_EVENT
.  Hardcoded to "AIX_SYSTEM". Hardcoded to "AIX_SYSTEM". Hardcoded to "AIX_SYSTEM".
intermediary_hostip
intermediary.ip
The value is extracted from the
message
field using grok patterns and assigned directly.
sc_summary
security_result.summary
The value is extracted from the
description
field using grok patterns and assigned directly.
severity
security_result.severity
The value is derived from the
severity
field. If
severity
is "info" (case-insensitive), the UDM value is "INFORMATIONAL". If
severity
is "Err" (case-insensitive), the UDM value is "ERROR".
src_ip
principal.ip
The value is extracted from the
message
or
description
field using grok patterns and assigned directly.
src_port
principal.port
The value is extracted from the
description
field using grok patterns and assigned directly.
sys_log_host
intermediary.hostname
The value is extracted from the
message
field using grok patterns and assigned directly.
syslog_priority
security_result.priority_details
The value is extracted from the
message
field using grok patterns and assigned directly.
ts
timestamp
The timestamp is extracted from the
ts
field in the log message using grok and the
date
filter.
user
principal.user.userid
The value is extracted from the
message
or
description
field using grok patterns and assigned directly.
Need more help?
Get answers from Community members and Google SecOps professionals.
