# Collect Extreme Wireless logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-wireless/  
**Scraped:** 2026-03-05T09:55:20.264320Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Extreme Wireless logs
Supported in:
Google secops
SIEM
This document explains how to ingest Extreme Networks Wireless logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages using grok patterns based on the
prod_event_type
field. It then maps these extracted fields to the Unified Data Model (UDM), handling various log formats and enriching the data with metadata and labels for improved context.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to Extreme Networks CloudIQ
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
'EXTREME_WIRELESS'
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
Configure Syslog for Extreme Networks CloudIQ
Sign in to the CloudIQ web UI.
Go to
Configure
>
Common Objects
>
Management
>
Syslog Servers
.
Click
+
.
Provide the following configuration details:
Name: Provide a unique name for the server.
Severity: Select
Info
.
Select an existing syslog IP address from the
Select
menu, or click
+
.
Enter the Bindplane agent IP address.
Enter the Bindplane agent port number.
Click
ADD
.
Click
Save Syslog Server
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.detection_fields.key
The value of the
action
field from the raw log is mapped to the
security_result.detection_fields.key
.
action
security_result.detection_fields.value
The value of the
action
field from the raw log is mapped to the
security_result.detection_fields.value
.
BSSID
principal.resource.attribute.labels.key
The string "BSSID" is assigned to the
principal.resource.attribute.labels.key
.
BSSID
principal.resource.attribute.labels.value
The value of the
BSSID
field from the raw log is mapped to the
principal.resource.attribute.labels.value
.
collection_time.nanos
metadata.event_timestamp.nanos
The value of
collection_time.nanos
from the raw log is mapped to
metadata.event_timestamp.nanos
.
collection_time.seconds
metadata.event_timestamp.seconds
The value of
collection_time.seconds
from the raw log is mapped to
metadata.event_timestamp.seconds
.
collection_time.seconds
timestamp.seconds
The value of
collection_time.seconds
from the raw log is mapped to
timestamp.seconds
.
collection_time.nanos
timestamp.nanos
The value of
collection_time.nanos
from the raw log is mapped to
timestamp.nanos
.
data
security_result.description
The value of the
data
field from the raw log, after undergoing several
gsub
transformations to remove unwanted characters and "N/A" values, is mapped to the
security_result.description
field.
description
security_result.description
The value of the
description
field, extracted by the grok parser, is mapped to the
security_result.description
field.
first
security_result.detection_fields.key
The string "first" is assigned to the
security_result.detection_fields.key
.
first
security_result.detection_fields.value
The value of the
first
field from the raw log is mapped to the
security_result.detection_fields.value
.
hostname
principal.asset.hostname
The value of the
hostname
field from the raw log is mapped to the
principal.asset.hostname
and
principal.hostname
fields.
hostname
principal.hostname
The value of the
hostname
field from the raw log is mapped to the
principal.asset.hostname
and
principal.hostname
fields.
IP
principal.asset.ip
The value of the
IP
field from the raw log is mapped to the
principal.asset.ip
and
principal.ip
fields.
IP
principal.ip
The value of the
IP
field from the raw log is mapped to the
principal.asset.ip
and
principal.ip
fields.
MAC
principal.resource.attribute.labels.key
The string "MAC" is assigned to the
principal.resource.attribute.labels.key
.
MAC
principal.resource.attribute.labels.value
The value of the
MAC
field from the raw log is mapped to the
principal.resource.attribute.labels.value
.
medium
security_result.detection_fields.key
The string "medium" is assigned to the
security_result.detection_fields.key
.
medium
security_result.detection_fields.value
The value of the
medium
field from the raw log is mapped to the
security_result.detection_fields.value
. The
metadata.event_type
is determined by logic within the parser. If both
principal
and
target
machine IDs are present, it's set to
NETWORK_CONNECTION
. If either
principal
or
target
user IDs are present, it's set to
USER_UNCATEGORIZED
. If only the
principal
machine ID is present, it's set to
STATUS_UPDATE
. Otherwise, it defaults to
GENERIC_EVENT
. The string "EXTREME WIRELESS" is assigned to
metadata.product_name
.
prod_event_type
metadata.product_event_type
The value of the
prod_event_type
field from the raw log is mapped to the
metadata.product_event_type
field.
port
principal.port
The value of the
port
field from the raw log, converted to an integer, is mapped to the
principal.port
field.
problem_summary
security_result.summary
The value of the
problem_summary
field from the raw log is mapped to the
security_result.summary
field.
SSID
principal.resource.attribute.labels.key
The string "SSID" is assigned to the
principal.resource.attribute.labels.key
.
SSID
principal.resource.attribute.labels.value
The value of the
SSID
field from the raw log is mapped to the
principal.resource.attribute.labels.value
.
station
principal.asset.hostname
The value of the
station
field from the raw log is mapped to the
principal.asset.hostname
and
principal.hostname
fields.
station
principal.hostname
The value of the
station
field from the raw log is mapped to the
principal.asset.hostname
and
principal.hostname
fields.
target_host
target.asset.hostname
The value of the
target_host
field from the raw log is mapped to the
target.asset.hostname
and
target.hostname
fields.
target_host
target.hostname
The value of the
target_host
field from the raw log is mapped to the
target.asset.hostname
and
target.hostname
fields.
target_ip
target.asset.ip
The value of the
target_ip
field from the raw log is mapped to the
target.asset.ip
and
target.ip
fields.
target_ip
target.ip
The value of the
target_ip
field from the raw log is mapped to the
target.asset.ip
and
target.ip
fields.
target_port
target.port
The value of the
target_port
field from the raw log, converted to an integer, is mapped to the
target.port
field.
target_user
target.user.userid
The value of the
target_user
field from the raw log is mapped to the
target.user.userid
field.
user-profile
security_result.detection_fields.key
The string "user profile" is assigned to the
security_result.detection_fields.key
.
user-profile
security_result.detection_fields.value
The value of the
user-profile
field from the raw log is mapped to the
security_result.detection_fields.value
.
username
principal.user.userid
The value of the
username
field from the raw log is mapped to the
principal.user.userid
field. The string "EXTREME_WIRELESS" is assigned to
metadata.vendor_name
.
Need more help?
Get answers from Community members and Google SecOps professionals.
