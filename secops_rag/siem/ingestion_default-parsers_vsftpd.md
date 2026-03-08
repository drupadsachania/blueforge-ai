# Collect VSFTPD logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vsftpd/  
**Scraped:** 2026-03-05T09:30:12.576372Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VSFTPD logs
Supported in:
Google secops
SIEM
This document explains how to ingest VSFTPD logs to Google Security Operations using Bindplane. The parser uses grok patterns to extract fields from the logs, mapping them to the UDM. It handles various log types, including logins, uploads, downloads, and directory operations, enriching the data with additional context like SSL/TLS information and actions (allow/block). It also performs specific transformations for different log message types, such as extracting response codes and descriptions, and converting file sizes to integers.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the host with VSFTPD
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
'VSFTPD'
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
Configure Syslog on VSFTPD
Sign in to the VSFTPD host.
To install rsyslog in
Ubuntu/Debian
, run the following command:
sudo
apt
install
rsyslog
To install rsyslog in
CentOS/RHEL
, run the following command:
sudo
yum
install
rsyslog
Edit the vsftpd configuration to use Syslog:
sudo
vi
/etc/vsftpd.conf
Ensure the following parameters are set:
syslog_enable
=
YES
xferlog_enable
=
NO
log_ftp_protocol
=
YES
Save and exit.
Restart vsftpd:
sudo
systemctl
restart
vsftpd
Edit the rsyslog configuration to forward logs to the Bindplane agent:
sudo
nano
/etc/rsyslog.d/90-vsftpd.conf
Add the following line to forward logs using
UDP
(default port
514
):
if
(
$programname
==
'vsftpd'
)
then
@@BINDPLANE_IP:514
Replace
BINDPLANE_IP
with the actual Bindplane agent IP address.
Use
@
for
UDP
,
@@
for
TCP
.
Restart rsyslog:
sudo
systemctl
restart
rsyslog
UDM Mapping Table
Log Field
UDM Mapping
Logic
certificate
security_result.detection_fields.key
: "cert"
security_result.detection_fields.value
:  value of
certificate
The value of the
certificate
field is mapped to a
security_result.detection_fields
object with the key "cert".
cipher
network.tls.cipher
The value of the
cipher
field is directly mapped.
client_ip
principal.ip
The value of the
client_ip
field is directly mapped.
date
metadata.event_timestamp
Used with
month
,
year
, and
time
to construct the
metadata.event_timestamp
. The format is derived from the
timestamp
field in the raw log, parsed, and converted to a timestamp object.
day
metadata.event_timestamp
Used with
month
,
year
, and
time
to construct the
metadata.event_timestamp
.
desc
metadata.description
The value of the
desc
field (extracted from the
type
field) is directly mapped. This applies to "MKDIR", "RMDIR", and "DELETE" operations.
description
network.ftp.command
security_result.description
target.file.full_path
If
type
is "FTP command", the value is mapped to
network.ftp.command
. If
type
is "DEBUG" and doesn't match specific SSL patterns, it's mapped to
security_result.description
. If
type
starts with "OK" and is not "OK LOGIN", and the log describes a file operation (MKDIR, RMDIR, DELETE), it's mapped to
target.file.full_path
.
file_name
target.file.full_path
The value of the
file_name
field is directly mapped.
file_size
network.received_bytes
network.sent_bytes
If
type
is "OK DOWNLOAD" or "FAIL DOWNLOAD", the value is converted to an unsigned integer and mapped to
network.received_bytes
. If
type
is "OK UPLOAD" or "FAIL UPLOAD", the value is converted to an unsigned integer and mapped to
network.sent_bytes
.  Set to "USER_LOGIN" if
type
is "OK LOGIN". Set to "FILE_UNCATEGORIZED" if
type
is related to file operations ("OK UPLOAD", "OK DOWNLOAD", "FAIL DOWNLOAD", "OK MKDIR", "OK RMDIR", "OK DELETE", "FAIL UPLOAD"). Set to "STATUS_UPDATE" for all other
type
values. Always set to "VSFTPD". Always set to "VSFTPD". Always set to "VSFTPD".
month
metadata.event_timestamp
Used with
day
,
year
, and
time
to construct the
metadata.event_timestamp
.
pid
principal.process.pid
The value of the
pid
field is directly mapped.
response_code
network.http.response_code
The value of the
response_code
field is converted to an integer and mapped.
reused_status
security_result.detection_fields.key
: "reused status"
security_result.detection_fields.value
: value of
reused_status
The value of the
reused_status
field is mapped to a
security_result.detection_fields
object with the key "reused status".
speed
additional.fields.key
: "download_speed" or "upload_speed"
additional.fields.value.string_value
: value of
speed
If
type
is "OK DOWNLOAD" or "FAIL DOWNLOAD", the value is mapped to
additional.fields
with the key "download_speed". If
type
is "OK UPLOAD" or "FAIL UPLOAD", the value is mapped to
additional.fields
with the key "upload_speed".
ssl_shutdown_state
security_result.detection_fields.key
: "SSL Shutdown State"
security_result.detection_fields.value
: value of
ssl_shutdown_state
The value of the
ssl_shutdown_state
field is mapped to a
security_result.detection_fields
object with the key "SSL Shutdown State".
ssl_version
network.tls.version
The value of the
ssl_version
field is directly mapped.
time
metadata.event_timestamp
Used with
day
,
month
, and
year
to construct the
metadata.event_timestamp
.
type
metadata.description
security_result.action_details
The value of the
type
field is mapped to
metadata.description
except when it's "OK LOGIN".  It is also mapped to
security_result.action_details
when it indicates an allow or block action (starts with "OK" or "FAIL").
userid
principal.user.userid
target.user.userid
If
type
is "OK LOGIN", the value is mapped to
target.user.userid
. Otherwise, it's mapped to
principal.user.userid
.
year
metadata.event_timestamp
Used with
day
,
month
, and
time
to construct the
metadata.event_timestamp
. Set to "NETWORK" if
type
is "OK LOGIN". Set to "MACHINE" if
type
is "OK LOGIN". Set to "ALLOW" if
type
starts with "OK". Set to "BLOCK" if
type
starts with "FAIL".
Need more help?
Get answers from Community members and Google SecOps professionals.
