# Collect Nasuni File Services Platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nasuni-file-services/  
**Scraped:** 2026-03-05T09:58:26.606346Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Nasuni File Services Platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest Nasuni File Services Platform logs to Google Security Operations using a Bindplane agent. The parser extracts fields from SYSLOG and JSON logs. It uses grok patterns to parse the initial message and then leverages a JSON filter for embedded JSON data, mapping extracted fields to the UDM, handling various event types like file reads, modifications, and generic events, and enriching the data with vendor and product information. It also performs conditional logic based on extracted fields to categorize events and populate UDM metadata.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Claroty CTD.
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
NASUNI_FILE_SERVICES
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
Configure Syslog in Nasuni File Service platform
Sign in to the
Nasuni Console
web UI.
Go to
Console Settings
>
Syslog Exports
.
Enter the following configuration details in the Network section:
Hostname
: enter a unique and meaningful name (for example,
Google SecOps syslog
).
IP Address
: enter the Bindplane IP address.
Port
: enter the Bindplane configure port number (for example,
514
for UDP).
Protocol: select
UDP
(you can also select
TCP
, depending on your Bindplane configuration).
Format: Select
SYSLOG+JSON
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
application
target.application
Populated when
msg
field exists and is not JSON, and
application
field is not empty.
event_type
metadata.product_event_type
Directly mapped from the
event_type
field in the raw log.
gid
target.group.product_object_id
Directly mapped from the
gid
field in the raw log, converted to string.
groupname
target.group.group_display_name
Directly mapped from the
groupname
field in the raw log.
host
principal.hostname
Directly mapped from the
host
field in the raw log.
ipaddr
principal.ip
Directly mapped from the
ipaddr
field in the raw log.
is_dir
additional.fields.value.string_value
(where key is
is_dir
)
Directly mapped from the
is_dir
field in the raw log, converted to string. Added as an additional field.
msg
metadata.description
Populated when
msg
field exists, is not JSON, and
ipaddr
and
prin_port
are not extracted from it. Also used for STATUS_UPDATE events.
newpath
additional.fields.value.string_value
(where key is
newpath
)
Directly mapped from the
newpath
field in the raw log. Added as an additional field.
offset
additional.fields.value.string_value
(where key is
offset
)
Directly mapped from the
offset
field in the raw log, converted to string. Added as an additional field.
path
target.file.full_path
Directly mapped from the
path
field in the raw log.
pid
target.process.pid
Directly mapped from the
pid
field in the raw log, converted to string.
prin_port
principal.port
Extracted from the
msg
field using grok when
msg
is not JSON, converted to integer.
proc_id
principal.process.pid
Directly mapped from the
proc_id
field in the raw log.
product_log_id
metadata.product_log_id
Directly mapped from the
product_log_id
field in the raw log.
proto
metadata.description
Directly mapped from the
proto
field in the raw log.
resource
target.resource.resource_subtype
Directly mapped from the
resource
field in the raw log.
sequence
additional.fields.value.string_value
(where key is
sequence
)
Directly mapped from the
sequence
field in the raw log, converted to string. Added as an additional field.
sid
principal.user.windows_sid
Directly mapped from the
sid
field in the raw log.
tid
target.resource.product_object_id
Directly mapped from the
tid
field in the raw log, converted to string.
time
metadata.event_timestamp.seconds
,
timestamp.seconds
The seconds part of the timestamp is extracted from the
time
field and used to populate both
metadata.event_timestamp
and the top-level
timestamp
. Determined by logic based on the values of
ipaddr
,
path
, and
event_type
. Can be
FILE_READ
,
FILE_MODIFICATION
,
FILE_UNCATEGORIZED
,
STATUS_UPDATE
, or
GENERIC_EVENT
. Hardcoded to
NASUNI_FILE_SERVICES
. Hardcoded to
Nasuni File Services Platform
. Hardcoded to
Nasuni
.
uid
additional.fields.value.string_value
(where key is
uid
)
Directly mapped from the
uid
field in the raw log, converted to string. Added as an additional field.
username
principal.user.user_display_name
Directly mapped from the
username
field in the raw log.
volume
additional.fields.value.string_value
(where key is
volume
)
Directly mapped from the
volume
field in the raw log. Added as an additional field.
Need more help?
Get answers from Community members and Google SecOps professionals.
