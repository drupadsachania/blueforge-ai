# Collect Alcatel switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alcatel-switch/  
**Scraped:** 2026-03-05T09:49:37.375852Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Alcatel switch logs
Supported in:
Google secops
SIEM
This document explains how to ingest Alcatel switch logs to Google Security Operations using a Bindplane agent. The parser extracts fields using a series of
grok
patterns based on different log formats. It then maps the extracted fields to the corresponding fields in the Unified Data Model (UDM) and enriches the data with metadata like vendor and event type.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged credentials to an Alcatel switch.
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
ALCATEL_SWITCH
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
Configure Alcatel switch Syslog Export
Connect using SSH or console cable to the switch.
Sign in with
administrator
credentials.
Enter
global configuration
mode:
enable
configure
terminal
Set the Bindplane (syslog) server IP address:
swlog
output
socket
<syslog-server-ip>
Replace
<syslog-server-ip>
with Bindplane Agent IP address.
Enable logging to the syslog server:
swlog
remote
enable
Configure the logging level:
swlog
console
level
info
Enable command logging:
command-log
enable
Save the changes to the startup configuration:
write
memory
UDM Mapping Table
Log Field
UDM Mapping
Logic
1.1.1.1
principal.ip
principal.asset.ip
Extracted from the log message.
1.1.1.2
target.ip
target.asset.ip
Extracted from the log message.
1.1.2.7
target.ip
target.asset.ip
Extracted from the log message.
1035
target.port
Extracted from the log message.
2266
additional.fields.value.string_value
Extracted from the log message and mapped as
vlan
.
3036
principal.port
Extracted from the log message.
59300
target.port
Extracted from the log message.
60588
target.port
Extracted from the log message.
997
principal.resource.attribute.labels.value
Extracted from the log message and mapped as
limit
.
A6450-L2-K4B-01
principal.application
Extracted from the log message.
A6450-L2-X1B-02-01
principal.application
Extracted from the log message.
A6450-L2-X2A-01-01
principal.application
Extracted from the log message.
A6450-L2-X4B-02-01
principal.application
Extracted from the log message.
A6900-L3-LTX0A
principal.application
Extracted from the log message.
Accepted keyboard-interactive/pam
security_result.summary
Part of the extracted
sec_summary
field.
b8:53:ac:6e:c9:bc
principal.mac
Extracted from the log message.
BRIDGE(10)
additional.fields.value.string_value
Extracted from the log message and mapped as
id_protocol
.
CLI log,
security_result.summary
Part of the extracted
sec_summary
field.
cmd: show configuration snapshot all,
security_result.detection_fields.value
Extracted from the log message and mapped as
cmd
.
Connection reset by 1.1.2.7 port 60505
security_result.summary
Extracted from the log message.
Dec  7 14:28:40
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Dec  8 04:21:22
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Dec  9 20:08:29
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Dec  9 20:51:34
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Dec 11 10:18:30
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Dec 17 02:14:22
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Dec 19 10:27:33
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Did not receive identification string from 1.1.2.7 port 60588
security_result.summary
Extracted from the log message.
esmSetRateLimit: Txing
additional.fields.value.string_value
Extracted from the log message and mapped as
esm_set_rate_limit
.
Feb 15 16:29:29
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Feb 16 11:08:45
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
Feb 16 11:08:49
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
flashManager FlashMgr Main info(5) flashMgrValidateImage_exec: valid
security_result.summary
Extracted from the log message.
for ncmadmin from 1.1.1.2 port 59300 ssh2
security_result.summary
Part of the extracted
sec_summary
field.
from port 3036 to port 1035
security_result.summary
Part of the extracted
sec_summary
field.
IVDELCSW03
principal.hostname
principal.asset.hostname
Extracted from the log message when
principal_ip
is not an IP address.
IP-HELPER(22)
additional.fields.value.string_value
Extracted from the log message and mapped as
id_protocol
.
Jan 16 02:14:13
metadata.event_timestamp.seconds
metadata.event_timestamp.nanos
Parsed from the
ts
field.
LLDP(42)
additional.fields.value.string_value
Extracted from the log message and mapped as
id_protocol
.
limit=997,
principal.resource.attribute.labels.value
Extracted from the log message and mapped as
limit
.
limitType=1
principal.resource.attribute.labels.value
Extracted from the log message and mapped as
limitType
.
lldpProcessLocationIdTLV: Error, LLDP-MED Civic Address LCI len 39 invalid, tlvL
security_result.summary
Extracted from the log message.
Mac Movement for  MacAddr: a0:29:19:c0:55:18
security_result.summary
Extracted from the log message.
MacAddr: a0:29:19:c0:55:18
principal.mac
Extracted from the log message.
ncmadmin
principal.user.userid
Extracted from the log message.
OS6360
principal.hostname
principal.asset.hostname
Extracted from the log message when
principal_ip
is not an IP address.
result: SUCCESS
security_result.detection_fields.value
Extracted from the log message and mapped as
result
.
SES CMD info(5)
security_result.summary
Part of the extracted
sec_summary
field.
STACK-MANAGER
principal.application
Extracted from the log message.
Stack Port A MAC Frames TX/RX Enabled
security_result.summary
Extracted from the log message.
STP(11)
additional.fields.value.string_value
Extracted from the log message and mapped as
id_protocol
.
SWCONSOLE-L2-K0A-01
target.hostname
target.asset.hostname
Extracted from the log message.
trafficType=2,
principal.resource.attribute.labels.value
Extracted from the log message and mapped as
trafficType
.
user: ncmadmin
security_result.summary
Part of the extracted
sec_summary
field.
zslot=0,
principal.resource.attribute.labels.value
Extracted from the log message and mapped as
zslot
.
-
additional.fields.key
Hardcoded value:
id_protocol
-
additional.fields.key
Hardcoded value:
esm_set_rate_limit
-
additional.fields.key
Hardcoded value:
vlan
-
metadata.event_type
Set to
GENERIC_EVENT
if no other type is matched.
-
metadata.product_name
Hardcoded value:
Alcatel Switch
-
metadata.vendor_name
Hardcoded value:
ALCATEL SWITCH
-
network.application_protocol
Set to
SSH
when
id_protocol
matches
ssh
(case-insensitive).
-
principal.resource.attribute.labels.key
Hardcoded value:
limit
-
principal.resource.attribute.labels.key
Hardcoded value:
trafficType
-
principal.resource.attribute.labels.key
Hardcoded value:
limitType
-
principal.resource.attribute.labels.key
Hardcoded value:
zslot
-
security_result.detection_fields.key
Hardcoded value:
cmd
-
security_result.detection_fields.key
Hardcoded value:
result
-
security_result.severity
Set to
INFORMATIONAL
when
prod_severity
matches
info
(case-insensitive).
Need more help?
Get answers from Community members and Google SecOps professionals.
