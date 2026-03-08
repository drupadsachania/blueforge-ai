# Collect Veritas NetBackup logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veritas-netbackup/  
**Scraped:** 2026-03-05T10:02:06.626586Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Veritas NetBackup logs
Supported in:
Google secops
SIEM
This document explains how to ingest Veritas NetBackup logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages using grok patterns, then maps them to the Unified Data Model (UDM). It handles various log formats, including key-value pairs and JSON, and performs data transformations for consistent representation in the UDM.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the Veritas NetBackup appliance
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
'VERITAS_NETBACKUP'
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
Configure Syslog for Veritas NetBackup
Sign in to the
NetBackup Appliance Shell
web UI.
GO to
Main
>
Settings
>
LogForwarding
.
Select
Enable
.
Provide the following configuration details:
Server name or IP address
: Enter the Bindplane agent IP address.
Server port
: Enter the Bindplane agent port number (for example,
514
).
Protocol
: Select
UDP
or
TCP
, depending on your Bindplane agent configuration.
Interval
: Keep the default on
15
. If you set the interval to
0
, appliance continuously forwards syslogs to the target server.
TLS
: Select
No
.
Enter
Yes
to complete and save.
UDM Mapping Table
Log Field
UDM Mapping
Logic
data
additional.fields[0].value.string_value
The date and time from the raw log message, extracted using grok and formatted as "MM/DD/YY HH:MM:SS".
data
metadata.description
The description part of the message extracted using grok. Example: "(OdbcStatement::ExecDirect:962)::Error".
data
metadata.product_event_type
The product event type extracted using grok. Example: "Error::83".
data
principal.asset.hostname
The hostname extracted from the syslog message using grok.
data
principal.file.full_path
The pem file path extracted from the JSON data in the log.
data
principal.hostname
The hostname extracted from the syslog message using grok.
data
security_result.detection_fields[0].key
The key "SqlState" is added if the
SqlState
field is present in the raw log after the grok parsing.
data
security_result.detection_fields[0].value
The value of SqlState extracted from the raw log message using grok and kv.
data
security_result.detection_fields[1].key
The key "NativeError" is added if the
NativeError
field is present in the raw log after the grok parsing.
data
security_result.detection_fields[1].value
The value of NativeError extracted from the raw log message using grok and kv.
data
security_result.detection_fields[2].key
The key "sev" is added if the
sev
field is present in the raw log after the grok parsing.
data
security_result.detection_fields[2].value
The value of
sev
extracted from the JSON data in the log.
data
security_result.severity
Set to "LOW" if the
sev
field (extracted from JSON) is "normal".
data
security_result.summary
The error message or summary extracted from the raw log message using grok. The key "date_time" is hardcoded in the parser. The key "thread" is added if the
thread
field is present in the raw log after the grok parsing.
data
additional.fields[1].value.string_value
The value of
thread
extracted from the JSON data in the log. The key "m" is added if the
m
field is present in the raw log after the grok parsing.
data
additional.fields[2].value.string_value
The value of
m
extracted from the JSON data in the log. The key "fn" is added if the
fn
field is present in the raw log after the grok parsing.
data
additional.fields[3].value.string_value
The value of
fn
extracted from the JSON data in the log.
collection_time
metadata.event_timestamp
The timestamp from the
collection_time
field in the raw log. Set to "STATUS_UPDATE" if a principal hostname is present, otherwise "GENERIC_EVENT". Hardcoded to "Veritas Netbackup". Hardcoded to "VERITAS NETBACKUP".
collection_time
timestamp
The timestamp from the
collection_time
field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
