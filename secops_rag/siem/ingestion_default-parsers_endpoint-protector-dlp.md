# Collect Endpoint Protector DLP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/endpoint-protector-dlp/  
**Scraped:** 2026-03-05T09:23:45.720491Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Endpoint Protector DLP logs
Supported in:
Google secops
SIEM
This document explains how to ingest Netwrix Endpoint Protector DLP
(Data Loss Protection) logs to Google Security Operations using Bindplane.
The parser extracts fields from the syslog messages, leveraging grok patterns to
identify key information. It then maps these extracted fields to the Unified
Data Model (UDM), handling various data types and enriching the output with
metadata like vendor and product information. The parser also performs several
data transformations, including string manipulation and conditional merging of
fields based on operating system and other criteria.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Netwrix Endpoint Protector
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
'ENDPOINT_PROTECTOR_DLP'
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
Configure Syslog on Netwrix Endpoint Protector
Sign in to the
Endpoint Protector
web UI.
Go to
Appliance
>
SIEM Integration
.
Click
Add New
.
Provide the following configuration details:
SIEM Status
: Toggle switch to
enable
the SIEM server.
Disable Logging
: Toggle switch to
enable
logging.
Server Name
: Enter a unique and meaningful server name.
Server Description
: Add a description for this integration.
Server IP or DNS
: Enter the Bindplane agent IP address.
Server Protocol
: Select
UDP
.
Server Port
: Enter the Bindplane agent port number (for example,
514
for UDP).
Exclude Headers
: Toggle switch to
enable
log headers.
Log Types
: Select the available logs to send to the SIEM.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
Client Computer
principal.asset.asset_id
The value of
Client Computer
is assigned to
principal.asset.asset_id
after prepending "Client Computer: ".
Client User
principal.user.userid
The value of
Client User
is assigned to
principal.user.userid
.
Content Policy
security_result.rule_name
The value of
Content Policy
is assigned to
security_result.rule_name
.
Content Policy Type
security_result.rule_id
The value of
Content Policy Type
is assigned to
security_result.rule_id
.
Destination
metadata.ingestion_labels.value
The value of
Destination
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Destination".
Destination Type
metadata.ingestion_labels.value
The value of
Destination Type
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Destination Type".
Device PID
metadata.ingestion_labels.value
The value of
Device PID
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Device PID".
Device Serial
metadata.ingestion_labels.value
The value of
Device Serial
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Device Serial". This is only done if
Device Serial
is not empty.
Device VID
metadata.ingestion_labels.value
The value of
Device VID
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Device VID".
File Name
target.file.full_path
The value of
File Name
is assigned to
target.file.full_path
.
File Size
target.file.size
The value of
File Size
is assigned to
target.file.size
and converted to an unsigned integer.
IP Address
principal.ip
The value of
IP Address
is assigned to
principal.ip
.
Item Details
metadata.ingestion_labels.value
The value of
Item Details
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Item Details".
Log ID
metadata.product_log_id
The value of
Log ID
is assigned to
metadata.product_log_id
.
MAC Address
principal.mac
The value of
MAC Address
is assigned to
principal.mac
after replacing all hyphens with colons.
Matched Item
metadata.ingestion_labels.value
The value of
Matched Item
is assigned to the
value
field of an
ingestion_labels
object where the
key
is "Matched Item".
Message
security_result.summary
The value of
Message
is assigned to
security_result.summary
.
OS
principal.platform
The value of
OS
is used to determine the value of
principal.platform
. If
OS
contains "Windows",
principal.platform
is set to "WINDOWS". If
OS
contains "Mac",
principal.platform
is set to "MAC". If
OS
contains "Lin",
principal.platform
is set to "LINUX".
Serial Number
principal.asset.hardware.serial_number
The value of
Serial Number
is assigned to
principal.asset.hardware.serial_number
. Extracted from the message field using grok and assigned to
intermediary.hostname
. Extracted from the message field using grok and assigned to
metadata.description
. The timestamp from the syslog message is parsed and assigned to
metadata.event_timestamp
. The value "SCAN_UNCATEGORIZED" is assigned to
metadata.event_type
. The value "ENDPOINT_PROTECTOR_DLP" is assigned to
metadata.log_type
. The value "ENDPOINT_PROTECTOR_DLP" is assigned to
metadata.product_name
. The value "ENDPOINT_PROTECTOR_DLP" is assigned to
metadata.vendor_name
. Extracted from the message field using grok and assigned to
principal.hostname
. Extracted from the message field using grok and assigned to
principal.ip
. The timestamp from the syslog message is parsed and assigned to the top-level
timestamp
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
