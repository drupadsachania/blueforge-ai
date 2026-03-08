# Collect Dell CyberSense logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-cybersense/  
**Scraped:** 2026-03-05T09:23:12.905080Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Dell CyberSense logs
Supported in:
Google secops
SIEM
This document explains how to ingest Dell PowerProtect CyberSense logs to
Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Dell PowerProtect
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
Access the Configuration File:
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
'DELL_CYBERSENSE'
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
Restart Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog for Dell CyberSense
Sign in to the
Dell PowerProtect
using CLI.
Edit the
/etc/audisp/plugins.d/syslog.conf
file so that
active = yes
, and then save and exit the file.
Open the file using
vi
, enter the following command, and then save and exit the file. You can save and exit file by typing
:wq
:
$ModLoad imfile
$InputFileName /var/log/audit/audit.log
$InputFileTag tag_audit_log:
$InputFileStateFile audit_log
$InputFileSeverity info
$InputFileFacility local6
$InputRunFileMonitor

*.* @<Bindplane_IP>:514
Replace
<Bindplane_IP>
with the Bindplane agent IP address.
Restart the rsyslog service:
service
rsyslog
restart
Supported Dell CyberSense sample logs
SYSLOG (Standard)
<
141
>
CVDataDomain
ddsh
:
NOT
ICE
:
MSG
-
DDSH
-
00009
:
(
tty
=
<>
,
session
=
000
,
client_IP
=
192.168.1.100
)
admin_user
:
command
"net config"
SYSLOG + CEF
<
142
>
Nov
11
00
:
36
:
30
int
ernal
-
host
-
01
mc_server
:
CEF
:
0
|
Index
Engines
|
Catalyst
|
8.6.0
-
1.27
|
iecrd
|
iecrd_job
-
done_ok
|
normal
|
{'
crjobids
'
:
[
0000
]
,
'
crpolicy
'
:
'
policy_id_01
'
,
'
lanjobinstid
'
:
0000
,
'
lanjobdefname
'
:
'
policy_name_01
'
,
'
message
'
:
'
Completed
LAN
indexing
job
.
'}
SYSLOG + CEF + JSON (Structured)
<
142
>
Ja
n
31
08
:
36
:
19
i
nternal
-
hos
t
-01
wri
te
De
ta
iledSyslog
:
CEF
:
0
|
I
n
dex
E
n
gi
nes
|
Ca
tal
ys
t
|
8.6.0-1.27
|
iecrd|
iecrd_i
nfe
c
t
io
n
-
i
n
progress|
de
ta
il|
{
"crjobid"
:
0000
,
"engine_id"
:
"A1B2C3D4E5F6"
,
"URL"
:
"https://cyber-sense-ui.internal.corp/CyberSenseUI"
,
"host"
:
"host_id_999"
,
"path"
:
"/data/volume1/backup-mount-point/"
,
"infection_classes"
:
[
"The file retains its original name and file extension, but the content has been encrypted."
]
}
SYSLOG + CEF + JSON (Single Line)
<
142
>
Dec
6
11
:
56
:
51
i
nternal
-
hos
t
-01
mc_server
:
CEF
:
0
|I
n
dex
E
n
gi
nes
|Ca
tal
ys
t
|
8.6.0-1.27
|dispa
t
ch|dispa
t
ch_seg
-
do
ne
_ok|
n
ormal|
{
"dbname"
:
"/opt/ie/var/segment_01.db"
,
"dbuuid"
:
"00000000-0000-0000-0000-000000000000"
}
Need more help?
Get answers from Community members and Google SecOps professionals.
