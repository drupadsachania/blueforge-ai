# Collect Sophos AV logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-av/  
**Scraped:** 2026-03-05T10:00:27.249923Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sophos AV logs
Supported in:
Google secops
SIEM
This document explains how to collect Sophos AV logs using Bindplane. The parser transforms JSON logs into a unified data model (UDM). It extracts fields from nested JSON structures, maps them to UDM fields, and performs event categorization based on the type field, enriching the data with specific details and actions for different Sophos AV event types.
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
'SOPHOS_AV'
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
. The
API Token Summary
for the provided token is displayed.
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
Open
the
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
UDM Mapping Table
Log field
UDM mapping
Logic
customer_id
target.resource.id
Direct mapping
data.customer_id
target.resource.id
Direct mapping
data.dhost
principal.hostname
Direct mapping
data.end
timestamp
Direct mapping
data.endpoint_id
principal.resource.id
Direct mapping
data.group
security_result.category_details
Direct mapping
data.id
principal.resource.id
Direct mapping
data.location
principal.hostname
Direct mapping
data.name
metadata.description
Direct mapping
data.rt
timestamp
Direct mapping
data.severity
security_result.severity
Direct mapping
data.source
principal.user.user_display_name
Direct mapping
data.source_info.ip
principal.ip
Direct mapping
data.suser
principal.user.userid
Direct mapping
data.threat
security_result.rule_name
Direct mapping when data.group is "POLICY"
data.type
metadata.product_event_type
Direct mapping
data.user_id
principal.user.userid
Direct mapping
data.when
timestamp
Direct mapping
dhost
principal.hostname
Direct mapping
end
timestamp
Direct mapping
endpoint_id
principal.resource.id
Direct mapping
group
security_result.category_details
Direct mapping
id
principal.resource.id
Direct mapping
location
principal.hostname
Direct mapping
name
metadata.description
Direct mapping
rt
timestamp
Direct mapping
severity
security_result.severity
Direct mapping
source
principal.user.user_display_name
Direct mapping
source_info.ip
principal.ip
Direct mapping
suser
principal.user.userid
Direct mapping
type
metadata.product_event_type
Direct mapping
user_id
principal.user.userid
Direct mapping
when
timestamp
Direct mapping
-
is_alert
The is_alert field is set to true for events with "severity" of "medium" or "high", or when the "type" field indicates an alert-worthy event like "Event::Endpoint::UpdateRebootRequired".
-
is_significant
The is_significant field is set to true for events with "severity" of "medium" or "high".
-
metadata.description
The description field is populated with the value of the "name" field from the raw log.
-
metadata.event_timestamp
The event_timestamp field is populated with the value of the "end", "rt" or "when" field from the raw log.
-
metadata.event_type
The event_type field is derived from the "type" field in the raw log, mapping specific Sophos event types to Chronicle UDM event types.
-
metadata.log_type
The log_type field is set to "SOPHOS_AV" for all events.
-
metadata.product_event_type
The product_event_type field is populated with the value of the "type" field from the raw log.
-
metadata.product_name
The product_name field is set to "Sophos Anti-Virus" for all events.
-
metadata.vendor_name
The vendor_name field is set to "Sophos" for all events.
-
network.direction
The direction field is set to "OUTBOUND" for all "NETWORK_CONNECTION" events.
-
network.ip_protocol
The ip_protocol field is set to "TCP" for "NETWORK_CONNECTION" events where the "target.url" field is present.
-
principal.hostname
The hostname field is populated with the value of the "dhost" or "location" field from the raw log.
-
principal.ip
The ip field is populated with the value of the "source_info.ip" field from the raw log.
-
principal.resource.id
The id field is populated with the value of the "id" or "endpoint_id" field from the raw log.
-
principal.user.user_display_name
The user_display_name field is populated with the value of the "suser" or "source" field from the raw log.
-
principal.user.userid
The userid field is populated with the value of the "suser", "user_id" or "data.suser" field from the raw log.
-
security_result.action
The action field is derived from the "data.name" field in the raw log, mapping specific Sophos actions to Chronicle UDM actions.
-
security_result.category_details
The category_details field is populated with the value of the "group" field from the raw log.
-
security_result.rule_name
The rule_name field is extracted from the "data.name" field in the raw log, specifically looking for patterns like "Policy non-compliance: [rule_name]" or "Rule names: [rule_name]".
-
security_result.severity
The severity field is populated with the value of the "severity" field from the raw log, converting it to the corresponding Chronicle UDM severity level.
-
security_result.summary
The summary field is populated with the value of the "name" field from the raw log when the event type is "GENERIC_EVENT" or "STATUS_HEARTBEAT".
-
target.application
The application field is populated with the value of the "data.name" field from the raw log when the event type is "NETWORK_CONNECTION" and the description mentions an application being blocked.
-
target.asset_id
The asset_id field is populated with the value of the "data.endpoint_id" field from the raw log when the event type is "NETWORK_CONNECTION" and the description mentions an asset ID.
-
target.file.full_path
The full_path field is extracted from the "data.name" field in the raw log, specifically looking for patterns like "Source path: [full_path]".
-
target.file.size
The size field is extracted from the "data.name" field in the raw log, specifically looking for patterns like "File size: [size]".
-
target.hostname
The hostname field is populated with the value of the "data.dhost" field from the raw log when the event type is "NETWORK_CONNECTION" and the description mentions a target hostname.
-
target.process.file.full_path
The full_path field is extracted from the "data.name" field in the raw log, specifically looking for patterns like "Controlled application [action]: [full_path]".
-
target.resource.id
The id field is populated with the value of the "customer_id" field from the raw log.
-
target.resource.name
The name field is populated with specific values based on the event type. For "SETTING_CREATION" and "SETTING_MODIFICATION", it's set to "Device Registration" and "Real time protection" respectively. For "SCAN_UNCATEGORIZED", it's populated with the value of the "data.name" field from the raw log.
-
target.resource.type
The type field is populated with specific values based on the event type. For "SETTING_CREATION" and "SETTING_MODIFICATION", it's set to "SETTING". For "SCAN_UNCATEGORIZED", it's set to "Scan". For "SCAN_NETWORK", it's set to "Device".
-
target.url
The url field is extracted from the "data.name" field in the raw log, specifically looking for patterns like "'[url]' blocked".
-
target.user.userid
The userid field is populated with the value of the "data.user_id" field from the raw log when the event type is "USER_CREATION".
-
timestamp
The timestamp field is populated with the value of the "end", "rt" or "when" field from the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
