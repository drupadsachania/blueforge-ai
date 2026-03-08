# Collect Kiteworks (formally Accellion) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion/  
**Scraped:** 2026-03-05T09:57:36.267126Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Kiteworks (formally Accellion) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Kiteworks (formerly Accellion) logs to Google Security Operations using Bindplane. The parser extracts the
audit_message
field from the SYSLOG messages, handling both JSON-formatted messages (using
grok
to extract the
textPayload
) and plain text messages. It then applies a common set of transformations defined in
auditd.include
and adds specific mappings for
SYSCALL
type events, enriching the UDM fields with extracted data.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2012 SP2 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Kiteworks (formerly Accellion) management console or appliance
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'ACCELLION'
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
<CUSTOMER_ID>
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
Configure Syslog forwarding on Kiteworks (formerly Accellion)
Sign in to the
Kiteworks Management Console
as an administrator.
Navigate to the
Locations
page using one of these paths:
Legacy UI
: Go to
System
>
Locations
.
New UI
: Go to
System Setup
>
Locations
.
Select the target location from the list.
Go to the
External Services
section.
Expand the
Syslog Settings
panel.
Click
Add
to create a new syslog server configuration.
Provide the following configuration details:
Syslog Server
: Enter the Bindplane agent IP address.
Protocol
: Select
UDP
or
TCP
, depending on your actual Bindplane agent configuration.
Port
: Enter the Bindplane agent port number (for example,
514
).
Format
: Select
JSON Format
(recommended for structured parsing).
Timezone
: Select UTC timezone for universal consistency across systems.
Click
Save
to apply the configuration.
UDM Mapping Table
Log Field
UDM Mapping
Logic
acct
principal.user.user_display_name
The value of
acct
from the raw log's
msg
field.
acct
target.user.user_display_name
The value of
acct
from the raw log's
msg
field.
addr
principal.ip
The value of
addr
from the raw log's
msg
field.
a0
security_result.about.labels.value
The value of
a0
from the raw log's
msg
field, where the corresponding
key
is "a0".
a1
security_result.about.labels.value
The value of
a1
from the raw log's
msg
field, where the corresponding
key
is "a1".
a2
security_result.about.labels.value
The value of
a2
from the raw log's
msg
field, where the corresponding
key
is "a2".
a3
security_result.about.labels.value
The value of
a3
from the raw log's
msg
field, where the corresponding
key
is "a3".
arch
security_result.about.platform_version
The value of
arch
from the raw log's
msg
field. Only applicable for
type_name
SYSCALL.
auid
about.user.userid
The value of
auid
from the raw log's
msg
field.
auid
security_result.detection_fields.value
The value of
auid
from the raw log's
msg
field, where the corresponding
key
is "auid".
comm
principal.application
The value of
comm
from the raw log's
msg
field.
cmd
principal.process.command_line
The value of
cmd
from the raw log's
msg
field.
cwd
security_result.detection_fields.value
The value of
cwd
from the raw log's
msg
field, where the corresponding
key
is "cwd".
cwd
target.process.file.full_path
The value of
cwd
from the raw log's
msg
field.
exe
principal.process.file.full_path
The value of
exe
from the raw log's
msg
field.
exe
target.process.file.full_path
The value of
exe
from the raw log's
msg
field.
exit
security_result.about.labels.value
The value of
exit
from the raw log's
msg
field, where the corresponding
key
is "Exit Code".
hostname
principal.hostname
The value of
hostname
from the raw log's
msg
field.  Hardcoded value "zing-h2" from the raw log's
msg
field.
key
security_result.about.registry.registry_key
The value of
key
from the raw log's
msg
field. Only applicable for
type_name
SYSCALL.
log_type
metadata.log_type
The value of
log_type
from the raw log.
msg
security_result.action_details
The value after
res=
in the
msg
field of the raw log.
msg
security_result.summary
Combination of fields from the
msg
field of the raw log.  For example, "session_open success" or "setcred success". Parsed from the
audit
section of the
msg
field in the raw log. Mapped based on the
type
field in the raw log.  For example, "USER_START" maps to "USER_LOGIN", "CRED_DISP" maps to "USER_LOGOUT", "CRED_ACQ" maps to "USER_LOGIN", "USER_END" maps to "USER_LOGOUT", "CRED_REFR" maps to "USER_LOGIN", "USER_CMD" maps to "USER_LOGIN", "CWD" maps to "STATUS_UPDATE", "PROCTITLE" maps to "STATUS_UPDATE", "USER_ACCT" maps to "USER_UNCATEGORIZED", and "SYSCALL" maps to "USER_UNCATEGORIZED". The value of the
type
field from the raw log's
msg
field. Extracted from the
audit
section of the
msg
field in the raw log.
node
principal.hostname
The value of
node
from the raw log's
msg
field.
pid
principal.process.pid
The value of
pid
from the raw log's
msg
field.
ppid
principal.process.parent_process.pid
The value of
ppid
from the raw log's
msg
field.
proctitle
target.process.file.full_path
Decoded hexadecimal value of
proctitle
from the raw log's
msg
field. Hardcoded to "LINUX". Set to "ALLOW" if
res=success
is present in the raw log's
msg
field.
ses
network.session_id
The value of
ses
from the raw log's
msg
field.
syscall
security_result.about.labels.value
The value of
syscall
from the raw log's
msg
field, where the corresponding
key
is "Syscall".
success
security_result.summary
Combined with other fields to form the summary. For SYSCALL events, the logic is: if success=yes, then "yes, The System call succeeded", otherwise "no, The System call failed".
terminal
principal.terminal
The value of
terminal
from the raw log's
msg
field.
timestamp
timestamp
The value of
timestamp
from the raw log entry.
tty
principal.terminal
The value of
tty
from the raw log's
msg
field.
type
metadata.product_event_type
The value of
type
from the raw log's
msg
field.
uid
about.user.userid
The value of
uid
from the raw log's
msg
field. Only applicable for
type_name
SYSCALL.
uid
target.user.userid
The value of
uid
from the raw log's
msg
field. Set to "SETTING" if
type
is "USER_ACCT".
Need more help?
Get answers from Community members and Google SecOps professionals.
