# Collect Cisco Wireless Security Management (WiSM) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm/  
**Scraped:** 2026-03-05T09:52:56.969682Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Wireless Security Management (WiSM) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Wireless Security Management (WiSM)
logs to Google Security Operations using Bindplane. The parser extracts fields from
the syslog messages, maps them to the Unified Data Model (UDM), and categorizes
events based on the
cisco_mnemonic
field. It handles various event types like
logins, logouts, network connections, and status updates, extracting relevant
information like usernames, IP addresses, MAC addresses, and security details.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to Cisco Wireless LAN COntroller (WLC)
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
Save the file securely on the system where BindPlane will be installed.
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
'CISCO_WSM'
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
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on Cisco WiSM
Sign in to the
Cisco Wireless LAN Controller
web UI.
Go to
Management > Logs > Config
.
Enter the Bindplane agent IP address in the
Syslog Server IP Address
field.
Click
Add
.
Provide the following configuration details:
Syslog Severity
: Select
Informational
.
Syslog Facility
: Select
Local Use 0
.
Buffered Log Level
: Select
Informational - Severity level 6
.
Console Log Level
: Select
Informational - Severity level 6
.
Select the
File Info
checkbox to include information about the source file.
Select the
Proc Info
checkbox to include process information.
Select the
Trace Info
checkbox to include trace back information.
Click
Apply
.
Click
Save Configuration
.
UDM mapping table
Log Field
UDM Mapping
Logic
cisco_facility
principal.resource.type
Extracted from the
cisco_tag
field using grok.
cisco_message
metadata.description
The original message from the raw log.
cisco_tag
metadata.product_event_type
The tag from the raw log, containing facility, severity, and mnemonic.
database
security_result.detection_fields.value
When present, the key is set to "Database".
hostname
intermediary.hostname
When present.
intermediary_ip
intermediary.ip
The IP address of the intermediary device.
principal_hostname
principal.hostname
When present.
principal_ip
principal.ip
When present.
principal_mac
principal.mac
When present.  Formatted to colon-separated hexadecimal.
principal_port
principal.port
When present. Converted to integer.
principal_process_id
principal.process.pid
When present.
profile
security_result.detection_fields.value
When present, the key is set to "Profile".
reason_message
security_result.summary
When present. Sometimes also used for
security_result.description
.
target_ip
target.ip
When present.
target_mac
target.mac
When present.
terminal
target.hostname
When present.
tls_local_ip
security_result.detection_fields.value
When present, the key is set to "TLS local".
tls_remote
security_result.detection_fields.value
When present, the key is set to "TLS Remote".
username
principal.user.userid
(or
target.user.userid
in logout events)
When present. Set to "MECHANISM_UNSPECIFIED" in certain cases by parser logic. Set to "MACHINE" for login/logout events by parser logic. Copied from the batch
create_time
. Determined by parser logic based on
cisco_mnemonic
and other fields. Set to "CISCO_WSM" by parser logic. Set to "CISCO_WSM" by parser logic. Set to "CISCO_WSM" by parser logic. Set to "BROADCAST" for specific events by parser logic. Set to "UDP" for specific events by parser logic. When present. Set to "ALLOW" or "BLOCK" for specific events by parser logic. Set to "AUTH_VIOLATION" for specific events by parser logic. Set for specific events by parser logic, sometimes using
reason_message
. Derived from
cisco_severity
by parser logic. Derived from
cisco_severity
by parser logic. Set for specific events by parser logic, sometimes using
reason_message
.
Need more help?
Get answers from Community members and Google SecOps professionals.
