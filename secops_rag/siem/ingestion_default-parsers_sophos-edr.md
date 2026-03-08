# Collect Sophos Intercept EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-edr/  
**Scraped:** 2026-03-05T09:28:32.908856Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sophos Intercept EDR logs
Supported in:
Google secops
SIEM
This document explains how to collect Sophos Intercept EDR logs using Bindplane. The parser extracts fields from Sophos EDR JSON logs, transforming them into the Unified Data Model (UDM). It parses the
message
field, maps Sophos fields to UDM fields (for example,
suser
to
principal.user.userid
), performs conditional merges based on field presence, and categorizes events based on the
type
field, setting appropriate UDM event types and security result actions.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
An additional Windows or Linux machine, capable of continuously running Python
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to Sophos Central Admin console
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
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'SOPHOS_EDR'
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
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Sophos Central API access
Sign in to
Sophos Central Admin
.
Select
Global Settings
>
API Token Management
.
Click
Add Token
to create a new token.
Enter a token name and click
Save
; (The
API Token Summary
for the provided token is displayed).
In the
API Token Summary
section, click
Copy
to copy the API access URL and headers.
Install Python on an additional machine
Open the web browser and go to the
Python website
.
Click
Download Python
for your operating system.
Install Python:
On Windows:
Run the installer.
Check the box that says
Add Python to PATH
.
Click
Install Now
.
On Mac:
Python may already be installed, if not you can install the latest version using the terminal.
Open
Terminal
and type the following command:
python
--version
Download the Sophos integration script
Go to the GitHub page for
Sophos Central SIEM Integration GitHub Repository
.
Click the green
Code button
>
Download ZIP
.
Extract the ZIP file.
Set up the script configuration
Open the
config.ini
file in the directory where you extracted the ZIP archive.
Edit the configuration file:
API Token
: Enter the API Key copied earlier from Sophos Central.
Syslog Server Details
: Enter the details of your syslog server.
Host
: Enter the BindPlane Agent IP address.
Port
: Enter the BindPlane Agent port number.
Protocol
: Enter UDP (you can also use
TCP
or
TLS
depending on your setup).
Save the file.
Run the script
Go to the script folder.
On Windows:
Press the
Windows
key and type
cmd
.
Click
Command Prompt
.
Go to the script folder:
cd
C
:
/
Users
/
YourName
/
Downloads
/
Sophos
-
Central
-
SIEM
-
Integration
On macOS:
Go to
Applications
>
Utilities
.
Open
Terminal
.
Go to the script folder:
cd
/Users/YourName/Downloads/Sophos-Central-SIEM-Integration
Run the script:
Type the following command to start the script:
python
siem.py
Automate the script to run continuously on Windows (using Task Scheduler):
Open the Task Scheduler by typing
Task Scheduler
in the Start menu.
Click
Create Task
.
In the
General
tab:
Name your task; (for example,
Sophos AV Log Export
).
In the
Triggers
tab:
Click
New
and set the task to run
Daily
or
At startup
(depending on your preference).
In the
Actions
tab:
Click
New
and select
Start a program
.
Browse for the
python.exe
executable (usually found at
C:/Python/XX/python.exe
).
In the
Add arguments
field, type the path to the script; (for example,
C:/Users/YourName/Downloads/Sophos-Central-SIEM-Integrationsiem.py
).
Click
OK
to save the task.
Automate the script to run continuously on Mac (using Cron Jobs):
Open Terminal.
Type
crontab -e
and press
Enter
.
Add a new line at the end of the file:
*
*
*
*
*
/usr/bin/python
/Users/YourName/Downloads/Sophos-Central-SIEM-Integration/siem.py
Click
Save
and exit the editor.
UDM mapping table
Log Field
UDM Mapping
Logic
appSha256
principal.process.file.sha256
The value of
appSha256
from the raw log is assigned to this UDM field.
core_remedy_items.items[].descriptor
principal.process.file.names
The value of each
descriptor
within the
items
array in
core_remedy_items
from the raw log is added as a separate
names
entry in the UDM.
customer_id
target.resource.id
The value of
customer_id
from the raw log is assigned to this UDM field.
detection_identity_name
security_result.threat_feed_name
The value of
detection_identity_name
from the raw log is assigned to this UDM field.
dhost
target.hostname
The value of
dhost
from the raw log is assigned to this UDM field.
endpoint_id
target.resource.attribute.labels[].value
The value of
endpoint_id
from the raw log is assigned as the value of a label in
target.resource.attribute.labels
. The key for this label is "endpoint_id".
endpoint_type
target.resource.attribute.labels[].value
The value of
endpoint_type
from the raw log is assigned as the value of a label in
target.resource.attribute.labels
. The key for this label is "endpoint_type".
filePath
target.file.full_path
The value of
filePath
from the raw log is assigned to this UDM field.
group
principal.group.group_display_name
The value of
group
from the raw log is assigned to this UDM field.
id
target.process.pid
The value of
id
from the raw log is assigned to this UDM field.
name
metadata.description
The value of
name
from the raw log is assigned to this UDM field. The value is derived from the
type
field in the raw log using conditional logic in the parser.  Default value is
NETWORK_UNCATEGORIZED
. Specific
type
values map to different UDM event types (e.g., "UpdateSuccess" maps to
STATUS_UPDATE
, "ServiceNotRunning" maps to
SERVICE_STOP
, etc.). Hardcoded to "SOPHOS_EDR". The value of
type
from the raw log is assigned to this UDM field. Hardcoded to "Sophos EDR". Hardcoded to "SOPHOS".
rt
metadata.event_timestamp
,
timestamp
The value of
rt
from the raw log, representing the event time, is parsed and used to populate both the
metadata.event_timestamp
and the top-level
timestamp
fields in the UDM.
security_result.severity
security_result.severity
The value of
severity
from the raw log is uppercased and assigned to this UDM field.
source_info.ip
principal.ip
The value of
ip
within
source_info
from the raw log is assigned to this UDM field.
suser
principal.user.userid
The value of
suser
from the raw log is assigned to this UDM field.
threat
security_result.threat_name
The value of
threat
from the raw log is assigned to this UDM field.
security_result.action
The value is derived from the
type
field in the raw log. If
type
contains "Blocked" or "Warn" (case-insensitive), the value is set to "BLOCK". If
type
contains "Allow" (case-insensitive), the value is set to "ALLOW". The value is set to "TASK" if the
type
field in the raw log is "ScheduledDataUploadResumed" or "ScheduledDailyLimitExceeded".
Need more help?
Get answers from Community members and Google SecOps professionals.
