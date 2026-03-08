# Collect VMware VeloCloud SD-WAN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-velocloud-sdwan/  
**Scraped:** 2026-03-05T10:02:19.704265Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware VeloCloud SD-WAN logs
Supported in:
Google secops
SIEM
This document explains how to ingest VMware VeloCloud SD-WAN logs to Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the VMware VeloCloud SD-WAN
A Cloud Virtual Private Network (branch-to-branch VPN) configured between the Edge and the Syslog collector (Bindplane agent)
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
'VELO_FIREWALL'
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
Configure Syslog for VMware VeloCloud SD-WAN
Sign in to the
VeloCloud Enterprise Portal
web UI.
Go to
SD-WAN service
>
Configure
>
Profiles
.
Click the link to the
Profile
to configure a profile or click the
View link
in the
Device
column of the profile.
Select
Configure Segment menu
>
Global Segment
to configure
Syslog
settings.
Under
Telemetry
, go to the
Syslog
area:
Select the
Enable Syslog
checkbox.
Click
+ Add
.
Provide the following configuration details:
Facility
: Select
local0
.
IP
: Enter the destination IP address of the Syslog collector.
Protocol
: Select either
TCP
or
UDP
as the Syslog protocol.
Port
: Enter the port number of the Syslog collector (default value is 514).
Source Interface
: This field is set to
Auto
at the profile level. The Edge will automatically select an interface with the
Advertise
field set.
Roles
: Select either
FIREWALL EVENT
or
EDGE AND FIREWALL EVENT
.
Syslog Level
: Select
INFO
.
All Segments
: Select the
All Segments
checkbox.
Save your changes.
Go to the
Firewall
page of the
Profile
configuration.
Click
Syslog Forwarding
to forward firewall logs originating from the enterprise Edge to your configured Syslog collectors.
Need more help?
Get answers from Community members and Google SecOps professionals.
