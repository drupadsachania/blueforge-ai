# Collect Dell EMC Isilon NAS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-nas/  
**Scraped:** 2026-03-05T09:23:16.286199Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Dell EMC Isilon NAS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Dell EMC Isilon NAS logs to
Google Security Operations using Bindplane. The Logstash parser code first uses
grok
patterns to extract various fields like timestamps, IP addresses,
usernames, and file paths from DELL_EMC_NAS syslog messages. Then, it maps the
extracted fields to the corresponding attributes within the Unified Data Model
(UDM) schema, effectively transforming raw log data into a structured format for
analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Dell EMC Isilon
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
'DELL_EMC_NAS'
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
to the path where the authentication file was saved in Step 1.
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
Configure Syslog for OneFS Version 7.x:
Sign in to the
Dell Isilon
using CLI.
Enable auditing using the following commands (replace
zone_name
with actual host):
isi
audit
settings
modify
--protocol-auditing-enabled
yes
--audited-zones
<zone_names>
isi
zone
zones
modify
<zone_name>
--audit-success
create,delete,read,rename,set_security,write
isi
zone
zones
modify
<zone_name>
--audit-failure
create,delete,read,rename,set_security,write
isi
zone
zones
modify
<zone_name>
--syslog-audit-events
create,delete,read,rename,set_security,write
Enable syslog forwarding using the following command:
isi
zone
zones
modify
<zone_name>
--syslog-forwarding-enabled
=
yes
Connect to an Isilon node using an SSH client.
Open the
syslog.conf
file using
vi
, which is located in the
/etc/mcp/templates
directory.
vi
syslog.conf
Locate the
!audit_protocol
line and add the following line, replace
<bindplane-ip>
with the actual Bindplane agent IP address:
*.* @<bindplane-ip>
Save the
syslog.conf
file:
```bash
:wq
```
Configure Syslog for OneFS Versions 8.0 and 8.1:
Sign in to the
Dell Isilon
using CLI.
Enable auditing using the following commands (replace
zone_name
with actual host):
isi
audit
settings
global
modify
--protocol-auditing-enabled
yes
--audited-zones
<zone_names>
isi
audit
settings
modify
--zone
<zone_name>
--audit-success
create,delete,read,rename,set_security,write
isi
audit
settings
modify
--zone
<zone_name>
--audit-failure
create,delete,read,rename,set_security,write
isi
audit
settings
modify
--zone
<zone_name>
--syslog-audit-events
create,delete,read,rename,set_security,write
Enable syslog forwarding using the following command:
isi
audit
settings
modify
--syslog-forwarding-enabled
=
yes
--zone
=
<zone_name>
Connect to an Isilon node using an SSH client.
Open the
syslog.conf
file using
vi
, which is located in the
/etc/mcp/templates
directory.
vi
syslog.conf
Locate the
!audit_protocol
line and add the following line, replace
<bindplane-ip>
with the actual Bindplane Agent IP address:
*.* @<bindplane-ip>
Save the
syslog.conf
file:
:wq
Configure Syslog for OneFS Versions 8.2 to 9.4:
Enable auditing using the following commands (replace
<bindplane-ip
with Bindplane agent IP address and
zone_name
with actual host):
isi
audit
settings
global
modify
--protocol-auditing-enabled
yes
--audited-zones
<zone_name>
--protocol-syslog-servers
<bindplane-ip>
isi
audit
settings
modify
--zone
<zone_name>
--audit-success
create,delete,read,renam,set_security,write
isi
audit
settings
modify
--zone
<zone_name>
--audit-failure
create,delete,read,rename,set_security,write
isi
audit
settings
modify
--zone
<zone_name>
--syslog-audit-events
create,delete,read,rename,set_security,write
Enable syslog forwarding using the following command:
isi
audit
settings
modify
--syslog-forwarding-enabled
yes
--zone
<zone_name>
UDM mapping table
Log Field
UDM Mapping
Logic
COMMAND
target.process.command_line
The raw log field
COMMAND
is mapped to this UDM field.
PWD
target.file.full_path
The raw log field
PWD
is mapped to this UDM field when
message
doesn't contain
command not allowed
.
USER
principal.user.userid
The raw log field
USER
is mapped to this UDM field.
action_done
Temporary variable used for parsing logic.
application
target.application
The raw log field
application
is mapped to this UDM field.
data
This field is not mapped to the UDM.
description
metadata.description
The raw log field
description
is mapped to this UDM field. Additionally,
command not allowed
is mapped to this field when
message
contains
command not allowed
.
file_name
target.file.full_path
The raw log field
file_name
is mapped to this UDM field after removing any `
intermediary_ip
intermediary.ip
The raw log field
intermediary_ip
is mapped to this UDM field.
kv_data
Temporary variable used for parsing logic.
method
Temporary variable used for parsing logic.
pid
target.process.pid
The raw log field
pid
is mapped to this UDM field when it's not empty or
-
.
resource_type
target.resource.type
The raw log field
resource_type
is mapped to this UDM field.
src_host
principal.hostname
The raw log field
src_host
is mapped to this UDM field.
src_ip
principal.ip
The raw log field
src_ip
is mapped to this UDM field. It can also be extracted from the
description
field using a Grok pattern.
status
Temporary variable used for parsing logic.
ts
metadata.event_timestamp.seconds
The raw log field
ts
is parsed and its seconds value is mapped to this UDM field.
user
principal.user.userid
The raw log field
user
is mapped to this UDM field if
USER
is empty.
wsid
principal.user.windows_sid
The raw log field
wsid
is mapped to this UDM field after removing any characters after `
N/A
metadata.event_type
This UDM field is derived from the parser logic based on the values of
action_done
,
method
, and
PWD
. It can be one of the following:
PROCESS_UNCATEGORIZED
,
PROCESS_OPEN
,
FILE_CREATION
,
FILE_OPEN
,
FILE_DELETION
,
FILE_MODIFICATION
,
FILE_UNCATEGORIZED
, or
STATUS_SHUTDOWN
(default).
N/A
security_result.action
This UDM field is derived from the parser logic based on the value of
status
. It can be either
ALLOW
or
BLOCK
.
N/A
security_result.summary
This UDM field is derived from the parser logic and populated with the value of
action_done
.
N/A
security_result.description
This UDM field is derived from the parser logic by concatenating the values of
method
and
status
with a
-
separator.
N/A
metadata.vendor_name
This UDM field is hardcoded to
DELL
.
N/A
metadata.product_name
This UDM field is hardcoded to
DELL_EMC_NAS
.
N/A
metadata.log_type
This UDM field is hardcoded to
DELL_EMC_NAS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
