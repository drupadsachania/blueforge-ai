# Collect Comodo AV logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comodo-av/  
**Scraped:** 2026-03-05T09:53:31.207439Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Comodo AV logs
Supported in:
Google secops
SIEM
This document explains how to ingest Comodo AV logs to Google Security Operations
using Bindplane. The parser code first extracts fields from Comodo AV/Endpoint
logs using Grok patterns and key-value separation. Then, it maps the extracted
data to the corresponding fields in the Unified Data Model (UDM) schema,
enriching the raw logs with standardized security event information.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Comodo IT and Security Manager console
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
ingestion_labels
:
log_type
:
'COMODO_AV'
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
Configure Comodo Antivirus to Send Syslog
Sign in to the
Comodo IT and Security Manager
console.
Go to
Advanced Settings
>
General Settings
>
Logging
.
Provide the following configuration details:
Select the
Write to syslog server (CEF format)
checkbox.
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (for example.
514
for UDP).
Click
OK
to save changes.
UDM mapping table
Log Field
UDM Mapping
Logic
data3
principal.asset.platform_software.platform_version
The value of
data3
field, representing the product version, is mapped to
principal.asset.platform_software.platform_version
.
data4
principal.user.product_object_id
The value of
data4
field, representing a unique identifier for the user within the product, is mapped to
principal.user.product_object_id
.
data5
principal.application
The value of
data5
field, representing the application or event name, is mapped to
principal.application
.
datetime
metadata.event_timestamp.seconds
The
datetime
field, representing the event timestamp, is parsed and its epoch seconds value is mapped to
metadata.event_timestamp.seconds
.
dvc
principal.ip
The
dvc
field, representing the device IP address, is mapped to
principal.ip
.
dvchost
principal.hostname
The
dvchost
field, representing the device hostname, is mapped to
principal.hostname
.
filePath
target.file.full_path
The
filePath
field, representing the full path of the scanned file, is mapped to
target.file.full_path
.
fname
target.process.parent_process.file.full_path
The
fname
field, representing the filename of the parent process, is mapped to
target.process.parent_process.file.full_path
.
suser
target.user.userid
The
suser
field, representing the user associated with the event, is mapped to
target.user.userid
.
metadata.event_type
This field is derived based on the presence of
filePath
. If
filePath
is not empty, it's set to
SCAN_FILE
, otherwise
SCAN_HOST
.
metadata.log_type
This field is statically set to
COMODO_AV
.
metadata.vendor_name
This field is statically set to
COMODO
.
metadata.product_name
This field is statically set to
COMODO_AV
.
Need more help?
Get answers from Community members and Google SecOps professionals.
