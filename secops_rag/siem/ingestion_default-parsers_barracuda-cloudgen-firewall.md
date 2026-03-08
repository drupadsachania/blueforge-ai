# Collect Barracuda CloudGen Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-cloudgen-firewall/  
**Scraped:** 2026-03-05T09:20:16.843737Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Barracuda CloudGen Firewall logs
Supported in:
Google secops
SIEM
This document explains how to ingest Barracuda CloudGen Firewall logs to
Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Barracuda CloudGen Firewall running firmware
8.3 or later
Privileged access to the Barracuda Firewall
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
log_type
:
'BARRACUDA_CLOUDGEN_FIREWALL'
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
to the path where the
authentication file was saved in the
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
Enable Syslog for Barracuda CloudGen Firewall
Sign in to the
Barracuda Firewall Control Center
at the box level.
Go to
Configuration
>
Full Configuration
>
Box
>
Infrastructure Services
>
Syslog Streaming
.
Click the
Lock
icon to enable editing.
Switch
Enable Syslog Streaming
to
Yes
.
Click
Send Changes
>
Activate
.
Configure Logdata Filters for Barracuda CloudGen Firewall
Go to
Configuration
>
Full Configuration
>
Box
>
Infrastructure Services
>
Syslog Streaming
.
Select
Logdata Filters
.
Click the
Configuration Mode
menu and select
Switch to Advanced View
.
Click the
Lock
icon to enable editing.
Click
add
Add
to add a new entry.
Provide a unique name in the
Filters
dialog.
Click
OK
.
In the
Affected Box Logdata
section, select
logs sent via syslog
.
Click
add
Add
next to
Data Selection
.
Provide a unique name for the
group
.
Click
OK
.
Select the following items from the
Data Selection
or your specific categories for logging:
Auth-All
Config-All
Control-All
Event-All
Firewall-All
Network-All
Settings-All
SSH-All
System-All
Select the following items from
Message Types
or your specific severity for logging:
Panic
Security
Fatal
Error
Warning
Notice
Click
OK
.
Click
Send Changes
>
Activate
.
Configure Logstream Destination for Barracuda CloudGen Firewall
Go to
Configuration
>
Full Configuration
>
Box
>
Infrastructure Services
>
Syslog Streaming
.
Select
Logstream Destinations
.
Click the
Configuration Mode
menu and select
Switch to Advanced View
.
Click the
Lock
icon to enable editing.
Click the
add
Add
to add a new entry.
Provide a unique name for the
destination
.
Click
OK
.
Select the newly created
Logstream Destination
.
Click
Explicit IP
.
Provide the following configuration details:
Destination IP Address
: Enter the Bindplane agent IP address.
Destination Port
: Enter the Bindplane agent port number.
Transmission Mode
: Select
UDP
.
Click
OK
.
Click
Send Changes
>
Activate
.
Configure Logdata Streams for Barracuda CloudGen Firewall
Go to
Configuration
>
Full Configuration
>
Box
>
Infrastructure Services
>
Syslog Streaming
.
Select
Logdata Streams
.
Click the
Configuration Mode
menu and select
Switch to Advanced View
.
Click the
Lock
icon to enable editing.
Click the
add
Add
to add a new entry.
Provide a unique name for the
configuration
.
Click
OK
.
Set
Active Streams
to
Yes
.
Set
Log Destinations
to the destination created earlier.
Set
Log Filters
to the filter created earlier.
Click
OK
.
Click
Send Changes
>
Activate
.
Need more help?
Get answers from Community members and Google SecOps professionals.
