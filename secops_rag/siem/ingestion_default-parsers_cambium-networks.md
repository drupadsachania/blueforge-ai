# Collect Cambium Networks logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cambium-networks/  
**Scraped:** 2026-03-05T09:20:51.627390Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cambium Networks logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cambium Networks logs to
Google Security Operations using Bindplane. The parser extracts key-value pairs
from Cambium Networks switch and router syslog messages, mapping them to a
Unified Data Model (UDM). It uses Grok to structure the initial message, KV to
separate key-value pairs, and conditional statements to map extracted fields to
specific UDM attributes, categorizing events as either "STATUS_UPDATE" or
"GENERIC_EVENT".
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Cambium Networks devices
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
'CAMBIUM_NETWORKS'
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
Configure Syslog on ePMP 1000/2000/Force 180/200 and ePMP Elevate
Sign in to the
Cambium Networks
GUI.
Go to
Configure
>
System
>
Syslog Logging
.
Provide the following configuration details:
Syslog Mask
: Click
Select All
.
Server 1
: Enter the Bindplane agent IP address.
Click
Save
.
Configure Syslog on ePMP 1000 HS and cnPilot E400/E500/E501
Sign in to the
Cambium Networks
GUI.
Go to the
Configure
>
System
>
Event Logging
.
Provide the following configuration details:
Syslog Server 1
: Enter the Bindplane agent IP address.
Click
Save
.
Login to the device
CLI
using
SSH
and enter the following command for enabling the debug level:
logging
cnmaestro
7
Save
and
Apply
the settings.
Enter the following command to verify the device agent logs from the cli:
service
show
debug-logs
device-agent
Configure Syslog on cnPilot R200/R201/R190
Sign in to the
Cambium Networks
GUI.
Go to
Administration
>
Management
>
System Log Settings
.
Provide the following configuration details:
Syslog Enable
: Select
Enable
.
Syslog Level
: Select
INFO
.
Remote Syslog Enable
: Select
Enable
.
Remote Syslog Server
: Enter the Bindplane agent IP address.
Click
Save
.
Configure Syslog on PMP 450/450i/450m AP
Sign in to the
Cambium Networks
GUI.
Go to
Configuration
>
cnMaestro
.
Provide the following configuration details:
cnMaestro Agent Debug Log Level
: Select
INFO
.
Go to
Configuration
>
Syslog
.
Provide the following configuration details:
Syslog DNS Server Usage
: Select
Disable DNS Domain Name
.
Syslog Server
: Enter the Bindplane agent IP address.
Syslog Server Port
: Enter the Bindplane agent port number.
AP Syslog Transmit
: Select
Enabled
.
SM Syslog Transmit
: Select
Enabled
.
Syslog Minimum Level
: Select
info
.
Click
Save
.
Configure Syslog on PMP 450/450i/450m SM
Sign in to the
Cambium Networks
GUI.
Go to
Configuration
>
cnMaestro
.
Provide the following configuration details:
cnMaestro Agent Debug Log Level
: Select
INFO
.
Go to
Configuration
>
Syslog
.
Provide the following configuration details:
Syslog Configuration Source
: Select
AP Preferred
.
Syslog DNS Server Usage
: Select
Disable DNS Domain Name
.
Syslog Server
: Enter the Bindplane agent IP address.
Syslog Server Port
: Enter the Bindplane agent port number.
Syslog Transmission
: Select
Obtain from AP
.
Syslog Minimum Level Source
: Select
AP Preferred
.
Syslog Minimum Level
: Select
info
.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
bssid
read_only_udm.principal.mac
Extracted from the
kv_fields
using the key
bssid
.
channel
read_only_udm.security_result.about.resource.attribute.labels.value
Extracted from the
kv_fields
using the key
channel
. Part of a label.
host_name
read_only_udm.principal.hostname
Extracted from the log message using the grok pattern.
ids_event
read_only_udm.security_result.summary
Extracted from the
kv_fields
using the key
ids_event
.
ids_status
read_only_udm.security_result.description
Extracted from the
kv_fields
using the key
ids_status
. Used as the description when present.
iap
read_only_udm.security_result.about.resource.attribute.labels.value
Extracted from the
kv_fields
using the key
iap
. Part of a label.
manufacturer
read_only_udm.security_result.about.resource.attribute.labels.value
Extracted from the
kv_fields
using the key
manufacturer
. Part of a label.
rssi
read_only_udm.security_result.about.resource.attribute.labels.value
Extracted from the
kv_fields
using the key
rssi
. Part of a label.
security
read_only_udm.security_result.about.resource.attribute.labels.value
Extracted from the
kv_fields
using the key
security
. Part of a label.
severity
read_only_udm.security_result.severity
Mapped from the log message using the grok pattern.
alert
maps to
HIGH
,
warn
maps to
MEDIUM
, everything else maps to
LOW
.
severity
read_only_udm.security_result.severity_details
Mapped from the log message using the grok pattern. Preserves the original severity value.
ssid
read_only_udm.principal.application
Extracted from the
kv_fields
using the key
ssid
.
timestamp
read_only_udm.metadata.event_timestamp
Extracted from the log message using the grok pattern and converted to a timestamp.
read_only_udm.metadata.event_type
Determined based on the presence of values in the
security_result
and
host_name
fields. If both fields are present, the event type is set to
STATUS_UPDATE
, otherwise it's
GENERIC_EVENT
.
read_only_udm.security_result.about.resource.attribute.labels.key
The value of this field is determined by the parser logic based on the specific key-value pair being processed. The possible values are:
Internet_Access_Provider
,
manufacturer
,
channel
,
received_signal_strength_indicator
, and
encryption_standard
.
read_only_udm.security_result.description
If the severity is
warn
this field takes the value of
kv_fields
, otherwise it takes the value of
ids_status
.
Need more help?
Get answers from Community members and Google SecOps professionals.
