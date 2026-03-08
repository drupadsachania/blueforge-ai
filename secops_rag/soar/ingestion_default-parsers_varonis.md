# Collect Varonis logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/varonis/  
**Scraped:** 2026-03-05T10:01:57.434466Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Varonis logs
Supported in:
Google secops
SIEM
This document explains how to ingest Varonis logs to Google Security Operations using
Bindplane. The parser extracts fields from the logs (SYSLOG + KV (CEF), LEEF)
using grok patterns, specifically handling CEF, LEEF, and other Varonis-specific
formats. It then maps the extracted fields to the Unified Data Model (UDM),
handling various data formats and edge cases to ensure consistent representation.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Varonis
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
Open the file using a text editor (for example, "nano", "vi", or Notepad).
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
'VARONIS'
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
Configure Syslog export in Varonis
Sign in to the
Varonis
web UI.
Go to
Tools
>
DatAlert
>
Select DatAlert
.
Select
Configuration
.
Provide the following configuration details:
Syslog Message IP Address
: Enter the Bindplane Agent IP address.
Port
: Enter the Bindplane agent port number (for example,
514
for
UDP
).
Facility name
: Select a facility.
Click
Apply
.
Configure Syslog format in Varonis
Go to
Tools
>
DatAlert
>
Alert Templates
.
Click
Edit Alert Template
and select
External system default template
.
In
Apply to alert methods
, select
Syslog message
from the list.
Select
Rules
>
Alert Method
from the menu.
Select
Syslog message
.
Click
OK
.
UDM mapping table
Log Field
UDM Mapping
Logic
act
security_result.summary
Value from the
act
field in the CEF message.
cn1
security_result.rule_id
Value from the
cn1
field in the CEF message.
cs1
network.email.to
Value from the
cs1
field in the CEF message, specifically the email recipient.
cs2
security_result.rule_name
Value from the
cs2
field in the CEF message.
device_version
metadata.product_version
Value from the
device_version
field in the CEF message.
dhost
principal.hostname
Value from the
dhost
field in the CEF message, representing the principal hostname.  If
file_server
is present and not "DirectoryServices", it overwrites this value.
duser
target.user.userid
Value from the
duser
field in the CEF message.  Undergoes gsub transformation to remove backslashes and split into
target.user.userid
and
target.administrative_domain
.
dvchost
target.hostname
Value from the
dvchost
field in the CEF message.
filePath
target.file.full_path
Value from the
filePath
field in the CEF message.
rt
metadata.event_timestamp
Value from the
rt
field in the CEF message, parsed as a timestamp.
severity
security_result.severity
Value from the
severity
field in the CEF message or LEEF message. Converted to uppercase. Mapped to UDM severity values (LOW, INFORMATIONAL, MEDIUM, HIGH, CRITICAL) based on numeric value or keyword.
Acting Object
target.user.user_display_name
Value from the
Acting Object
field in the key-value data. Split by "\" to extract the display name.
Acting Object SAM Account Name
target.user.userid
Value from the
Acting Object SAM Account Name
field in the key-value data.
Device hostname
target.hostname
Value from the
Device hostname
field in the key-value data.
Device IP address
target.ip
Value from the
Device IP address
field in the key-value data.
Event Time
metadata.event_timestamp
Value from the
Event Time
field in the key-value data, parsed as a timestamp.
Event Type
target.application
,
metadata.event_type
Value from the
Event Type
field in the key-value data. Used to derive
metadata.event_type
(FILE_OPEN, USER_CHANGE_PERMISSIONS, USER_CHANGE_PASSWORD, USER_UNCATEGORIZED).
File Server/Domain
principal.hostname
Value from the
File Server/Domain
field in the key-value data. If not "DirectoryServices", it overwrites the
principal.hostname
derived from
dhost
.
Path
target.file.full_path
Value from the
Path
field in the key-value data.
Rule Description
metadata.description
Value from the
Rule Description
field in the key-value data.
Rule ID
security_result.rule_id
Value from the
Rule ID
field in the key-value data.
Rule Name
security_result.rule_name
Value from the
Rule Name
field in the key-value data.
intermediary_host
intermediary.hostname
Value extracted by grok, representing the intermediary hostname.
log_type
metadata.log_type
Hardcoded to
VARONIS
.
metadata.event_type
metadata.event_type
Derived based on the values of
evt_typ
,
act
, and
filepath
. Defaults to STATUS_UPDATE if
event_type
is GENERIC_EVENT and
principal_hostname
is present.
metadata.product_name
metadata.product_name
Hardcoded to
VARONIS
, but can be overwritten by the
product_name
field from the LEEF message.
metadata.vendor_name
metadata.vendor_name
Hardcoded to
VARONIS
, but can be overwritten by the
vendor
field from the LEEF message.
prin_host
principal.hostname
Value extracted by grok, representing the principal hostname.
product_name
metadata.product_name
Value from the LEEF message.
security_result.action
security_result.action
Derived from the
result
or
Event Status
field. Set to "ALLOW" if the result is
Success
, otherwise set to
BLOCK
.
timestamp
timestamp
,
metadata.event_timestamp
The event timestamp is derived from various fields (
datetime1
,
event_time
,
start_datetime
,
datetime2
) based on availability. The
create_time
from the raw log is used as a fallback and mapped to both
timestamp
and
metadata.event_timestamp
if no other timestamp fields are available.
vendor
metadata.vendor_name
Value from the LEEF message.
Need more help?
Get answers from Community members and Google SecOps professionals.
