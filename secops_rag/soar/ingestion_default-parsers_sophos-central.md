# Collect Sophos Central logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-central/  
**Scraped:** 2026-03-05T10:00:30.511446Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sophos Central logs
Supported in:
Google secops
SIEM
This document explains how to collect Sophos Central logs by using Bindplane. The parser transforms JSON logs into a unified data model (UDM). It extracts fields from nested JSON structures, maps them to UDM fields, and performs event categorization based on the
type
field, enriching the data with specific details and actions for different Sophos Central event types.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
Ensure that you have an additional Windows or Linux machine, capable of continuously running Python.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Sophos XG Firewall.
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
SYSLOG
namespace
:
sophos_central
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
. The
API Token Summary
for the provided token is displayed.
In the
API Token Summary
section, click
Copy
to copy the API access URL and headers.
Install Python on the additional machine
Open the web browser and go to the
Python website
.
Click
Download Python
for your operating system (Windows or Mac).
Install Python.
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
Find
and
Open
the
config.ini
file with a text editor.
Edit the configuration file:
API Token
: enter the API Key copied earlier from Sophos Central.
Syslog Server Details
: enter the details of your syslog server.
Host
: enter the Bindplane IP address.
Port
: enter the Bindplane port number.
Protocol: enter UDP (you can also use
TCP
or
TLS
depending on your setup).
Save
the file.
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
\
Users
\
YourName
\
Downloads
\
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
Name your task; for example,
Sophos Central Log Export
.
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
C:\PythonXX\python.exe
).
In the
Add arguments
field, type the path to the script; for example,
C:\Users\YourName\Downloads\Sophos-Central-SIEM-Integration\siem.py
.
Click
OK
to save the task.
Automate the script to run continuously on Mac (using Cron Jobs):
Open the Terminal.
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
Save
and exit the editor.
UDM Mapping Table
Log Field
UDM Mapping
Logic
customer_id
target.resource.id
Directly mapped from the
customer_id
field.
data.core_remedy_items.items.0.descriptor
target.process.file.full_path
Directly mapped from the
data.core_remedy_items.items.0.descriptor
field.
data.source_info.ip
principal.ip
principal.asset.ip
Directly mapped from the
data.source_info.ip
field.
description
metadata.description
Directly mapped from the
description
field when
metadata.event_type
is
GENERIC_EVENT
.
dhost
principal.hostname
principal.asset.hostname
Directly mapped from the
dhost
field.
duid
security_result.detection_fields.value
Directly mapped from the
duid
field.
end
metadata.event_timestamp
Parsed to RFC 3339 format and mapped to the
event_timestamp
field.
endpoint_id
target.asset_id
Mapped as
Device endpoint Id: {endpoint_id}
.
endpoint_type
security_result.about.labels.value
Directly mapped from the
endpoint_type
field.
group
security_result.category_details
Directly mapped from the
group
field.
name
security_result.description
security_result.summary
Directly mapped from the
name
field.
metadata.event_type
Determined based on the
type
field and additional logic within the parser. Possible values include: FILE_OPEN, SCAN_HOST, SETTING_MODIFICATION, STATUS_HEARTBEAT, SETTING_CREATION, NETWORK_CONNECTION, SCAN_PROCESS, SCAN_UNCATEGORIZED, USER_CREATION, USER_UNCATEGORIZED, STATUS_UPDATE.
metadata.log_type
Set to
SOPHOS_CENTRAL
.
metadata.product_event_type
Directly mapped from the
type
field.
metadata.product_name
Set to
Sophos Central
.
metadata.vendor_name
Set to
Sophos
.
network.direction
Set to
OUTBOUND
for specific
type
values indicating outbound network connections.
network.ip_protocol
Set to
TCP
for specific
type
values indicating TCP network connections.
security_result.action
Determined based on the
action
field extracted from the
name
field using grok patterns. Possible values include: ALLOW, BLOCK, ALLOW_WITH_MODIFICATION, UNKNOWN_ACTION.
security_result.detection_fields.key
Set to
duid
when the
duid
field is present.
security_result.rule_name
Extracted from the
name
field using grok patterns for specific
type
values.
security_result.severity
Mapped from the
severity
field with the following mapping: low -> LOW, medium -> MEDIUM, high/critical -> HIGH.
target.application
Extracted from the
name
field using grok patterns for specific
type
values.
target.asset.hostname
Mapped from the
dhost
field for specific
type
values.
target.file.full_path
Extracted from the
name
field using grok patterns for specific
type
values, or directly mapped from
data.core_remedy_items.items.0.descriptor
or
core_remedy_items.items.0.descriptor
.
target.file.size
Extracted from the
name
field using grok patterns and converted to
uinteger
for specific
type
values.
target.hostname
Mapped from the
dhost
field for specific
type
values.
target.resource.name
Set to specific values based on the
type
field, or extracted from the
name
field using grok patterns.
target.resource.type
Set to specific values based on the
type
field.
target.user.userid
Mapped from the
suser
field after extracting the username using grok patterns.
target.url
Extracted from the
name
field using grok patterns for specific
type
values.
source_info.ip
principal.ip
principal.asset.ip
Directly mapped from the
source_info.ip
field.
suser
principal.user.userid
target.user.userid
Extracted from the
suser
field using grok patterns to remove hostname prefixes.
type
metadata.product_event_type
Directly mapped from the
type
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
