# Collect Kaseya Datto File Protection logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datto-file-protection/  
**Scraped:** 2026-03-05T09:57:32.102266Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Kaseya Datto File Protection logs
Supported in:
Google secops
SIEM
This document explains how to ingest Kaseya Datto File Protection logs to
Google Security Operations using Bindplane. The parser extracts fields from
Datto S4P4 syslog messages using grok patterns, maps them to the Unified Data
Model (UDM), and categorizes events based on syslog severity. It specifically
handles CEF formatted data within the syslog message, extracting key fields like
vendor, product, version, and event details for enrichment and classification.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, firewall
ports
are open
Privileged access to Datto Siris or Alto
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
For additional installation options, consult the
installation guide
.
Configure Bindplane agent to ingest Syslog and send to Google SecOps
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
tcplog
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
ingestion_labels
:
log_type
:
'DATTO_FILE_PROTECTION'
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
tcplog
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
Configure Syslog for Datto Siris and Alto
Sign in to the
Datto
Web Console.
Go to
Configure
>
Device Settings
>
Remote Logging
.
Enable
Remote Logging
.
Provide the following configuration details:
Make sure the
Bindplane Agent
is configured to listen on
port 514
over the
TCP
connection.
IP Address
: Enter the Bindplane agent IP address.
Click
Apply
.
UDM mapping table
Log Field
UDM Mapping
Logic
act
security_result.category_details
The value of
act
from the raw log's extensions field.
desc
metadata.description
The value of the
description
field extracted from the
desc
field using grok.
dvc
target.ip
The value of
dvc
from the raw log's extensions field.
extensions
security_result.category_details
,
target.ip
Parsed using kv filter to extract
act
and
dvc
which are then mapped to UDM fields.
hostname
principal.hostname
The hostname extracted from the raw log message.
log_id
metadata.product_log_id
The log ID extracted from the raw log message.
prod_dvc_version
metadata.product_version
The product version extracted from the raw log's
desc
field. Same value as
principal.hostname
. Set to
STATUS_UPDATE
if
hostname
or
dvc
are present in the raw log, otherwise "GENERIC_EVENT". Hardcoded value
\n\n\0017
when
extensions
field exists in the raw log. The timestamp extracted from the raw log message. Same value as
edr.raw_event_name
. Hardcoded value
DATTO_FILE_PROTECTION
. Hardcoded value
S4P4
. Hardcoded value
Datto
. Derived from
syslog_severity_code
. If < 3, severity is LOW. If > 2 and < 6, severity is MEDIUM. If > 5, severity is HIGH.
timestamp
metadata.event_timestamp
The timestamp extracted from the raw log message.
Need more help?
Get answers from Community members and Google SecOps professionals.
