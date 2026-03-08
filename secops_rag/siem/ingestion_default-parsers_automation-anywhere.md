# Collect Automation Anywhere logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/automation-anywhere/  
**Scraped:** 2026-03-05T09:19:27.271189Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Automation Anywhere logs
Supported in:
Google secops
SIEM
This document explains how you to ingest Automation Anywhere logs to Google Security Operations by using a Bindplane agent. The parser extracts key information from SYSLOG + KV format logs, transforms it into a structured format, and maps it to the Unified Data Model (UDM) fields, enabling standardized security analysis and event correlation. It specifically focuses on identifying user actions, resource interactions, and security outcomes from the log data.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Automation Anywhere.
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
AUTOMATION_ANYWHERE
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
Configure Syslog on Automation Anywhere
Sign in to the
Automation Anywhere Control Room
web UI.
Go to
Administration
>
Settings
>
Network settings
.
Click
plus (+)
.
Provide the syslog configuration details:
Syslog server
: Bindplane IP address.
Port
: Bindplane port number (for example,
514
for
UDP
).
Protocol
: Select
UDP
.
Optional:
User Secure Connection
: This configuration is available only for
TCP
communication.
Click
Save changes
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ACTIVITY AT
metadata.event_timestamp
The timestamp of the event is taken from the
ACTIVITY AT
field in the raw log.
ACTION TAKEN BY
target.user.userid
The user who performed the action is taken from the
ACTION TAKEN BY
field in the raw log.
ACTION TYPE
security_result.summary
A summary of the action taken is taken from the
ACTION TYPE
field in the raw log.
ITEM NAME
target.file.full_path
The name of the file or item involved in the event is taken from the
ITEM NAME
field in the raw log.
REQUEST ID
target.user.product_object_id
A unique identifier for the request is taken from the
REQUEST ID
field in the raw log.
SOURCE
metadata.product_event_type
The source of the event is taken from the
SOURCE
field in the raw log.
SOURCE DEVICE
target.hostname | target.ip
If the
SOURCE DEVICE
field contains a valid IP address, it is mapped to target.ip. Otherwise, it is mapped to target.hostname.
STATUS
security_result.action
The security action (ALLOW, BLOCK, UNKNOWN_ACTION) is determined based on the
STATUS
field in the raw log:
Successful
maps to ALLOW,
Unsuccessful
maps to BLOCK,
Unknown
maps to UNKNOWN_ACTION.
-
metadata.event_type
The event type is determined based on the
ACTION TYPE
field in the raw log using a series of regular expression matches. If no match is found, it defaults to
GENERIC_EVENT
.
-
metadata.log_type
Set to
AUTOMATION_ANYWHERE
.
-
metadata.product_name
Set to
AUTOMATION_ANYWHERE
.
-
metadata.vendor_name
Set to
AUTOMATION_ANYWHERE
.
-
extensions.auth
An empty object is added for USER_LOGIN events.
Need more help?
Get answers from Community members and Google SecOps professionals.
