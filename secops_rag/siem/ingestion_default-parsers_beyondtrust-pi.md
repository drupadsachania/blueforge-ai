# Collect BeyondTrust Privileged Identity logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-pi/  
**Scraped:** 2026-03-05T09:20:25.127098Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BeyondTrust Privileged Identity logs
Supported in:
Google secops
SIEM
This document explains how to ingest BeyondTrust Privileged Identity logs to
Google Security Operations using Bindplane. The parser extracts BeyondTrust Remote
Support logs, handling both CEF and non-CEF formatted syslog messages. It parses
key fields, maps them to the Unified Data Model (UDM), and determines the event
type based on extracted fields like
dst
,
src
,
suid
, and
sEventID
,
enriching the data with additional context like user details, IP addresses, and
security outcomes.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to BeyondTrust Privileged Remote Access Appliance
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
'BEYONDTRUST_PI'
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
Configure Syslog in BeyondTrust Privileged Identity
Sign in to the
Beyondtrust Privileged Appliance
.
Go to
Appliance
>
Security
>
Appliance Administration
.
Go to the
Syslog
section.
Provide the following configuration details:
Hostname
: Enter the Bindplane agent IP address.
Port
: Default port is set to
514 (UDP)
.
Format
: Select
RFC 5424
.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
cs1
additional.fields[0].key
Directly mapped from the raw log field
cs1Label
.
cs1Label
additional.fields[0].value.string_value
Directly mapped from the raw log field
cs1
.
cs3
additional.fields[1].value.string_value
Directly mapped from the raw log field
cs3Label
.
cs3Label
additional.fields[1].key
Directly mapped from the raw log field
cs3
.
cs4
additional.fields[2].value.string_value
Directly mapped from the raw log field
cs4Label
.
cs4Label
additional.fields[2].key
Directly mapped from the raw log field
cs4
.
data
metadata.description
For CEF messages, the
msg
field (extracted from
data
) is mapped to
metadata.description
. For non-CEF messages, the
sMessage
field (or parts of it, depending on the specific message format) is mapped to
metadata.description
.
dhost
target.hostname
Directly mapped from the raw log field
dhost
.
dntdom
target.administrative_domain
Directly mapped from the raw log field
dntdom
.
duser
target.user.user_display_name
Directly mapped from the raw log field
duser
.
msg
metadata.description
Directly mapped from the raw log field
msg
in CEF messages.
rt
metadata.event_timestamp.seconds
The epoch timestamp is extracted from the
rt
field in CEF messages.
sEventType
metadata.product_event_type
Directly mapped from the raw log field
sEventType
in non-CEF messages.
shost
principal.ip
Directly mapped from the raw log field
shost
.
sIpAddress
principal.ip
Directly mapped from the raw log field
sIpAddress
in non-CEF messages.
sLoginName
principal.user.userid
Extracted from the
sLoginName
field using a regular expression to separate the domain and user ID.
sMessage
security_result.description
Directly mapped from the raw log field
sMessage
in non-CEF messages, or extracted parts of it are used for
security_result.description
.
sntdom
principal.administrative_domain
Directly mapped from the raw log field
sntdom
.
sOriginatingAccount
principal.user.userid
Extracted from the
sOriginatingAccount
field using a regular expression to separate the domain and user ID.
sOriginatingApplicationComponent
principal.application
Used in combination with
sOriginatingApplicationName
to populate
principal.application
.
sOriginatingApplicationName
principal.application
Used in combination with
sOriginatingApplicationComponent
to populate
principal.application
.
sOriginatingSystem
principal.hostname
Directly mapped from the raw log field
sOriginatingSystem
in non-CEF messages.
suser
principal.user.user_display_name
Directly mapped from the raw log field
suser
. Determined by parser logic based on the presence and values of other fields like
dst
,
src
,
shost
, and
suid
. Possible values are
NETWORK_CONNECTION
,
STATUS_UPDATE
,
USER_UNCATEGORIZED
, and
GENERIC_EVENT
. Set to "BEYONDTRUST_PI". Set to "BeyondTrust Remote Support". Extracted from the CEF header in CEF messages. Set to "BeyondTrust". Set to "ALLOW" or "BLOCK" based on the
status
,
reason
, or
sMessage
fields. Set to
LOW
.
Need more help?
Get answers from Community members and Google SecOps professionals.
