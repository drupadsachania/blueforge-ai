# Collect Sophos Capsule8 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-capsule8/  
**Scraped:** 2026-03-05T10:00:29.089076Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sophos Capsule8 logs
Supported in:
Google secops
SIEM
This document explains how to collect Sophos Linux Sensor (formerly Capsule8) logs using Bindplane. Sophos Capsule8 provides runtime protection for Linux workloads, containers, and Kubernetes environments by detecting and responding to threats at the kernel level using eBPF technology. The parser first extracts and structures JSON-formatted log data. It then maps the extracted fields to their corresponding attributes within the Chronicle Unified Data Model (UDM), focusing on metadata, security results, and principal information.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
An additional Windows or Linux machine, capable of continuously running Python
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to Sophos Central Admin console
Sophos Linux Sensor (formerly Capsule8) deployed on your Linux systems
Configure Sophos Linux Sensor to export alerts to Sophos Central
Before configuring the integration, you must first configure Sophos Linux Sensor to send alert data to Sophos Central.
Prerequisites for Sophos Central integration
Sophos Linux Sensor version 5.5.2.22 or later.
One of the following licenses:
Intercept X Advanced for Server with XDR
Central Managed Detection and Response Essential Server
Central Managed Detection and Response Complete Server
Your Sophos Central MCS URL and tenant ID.
A valid SLS package repository API token.
Finding your MCS URL
Sign in to
Sophos Central
.
Click your
account name
>
Support settings
.
Look for the line that starts with
This account is located
in to find out what
geographical region
your Sophos Central account is in.
Use the following table to find your
MCS URL
based on your region:
Region
MCS URL
United States (Oregon)
mcs2-cloudstation-us-west-2.prod.hydra.sophos.com
United States (Ohio)
mcs2-cloudstation-us-east-2.prod.hydra.sophos.com
Ireland
mcs2-cloudstation-eu-west-1.prod.hydra.sophos.com
Germany
mcs2-cloudstation-eu-central-1.prod.hydra.sophos.com
Canada
mcs2.stn100yul.ctr.sophos.com
Australia
mcs2.stn100syd.ctr.sophos.com
Asia Pacific (Tokyo)
mcs2.stn100hnd.ctr.sophos.com
South America (Sao Paulo)
mcs2.stn100gru.ctr.sophos.com
If you don't see your region in the table, use
mcs2.stn100bom.ctr.sophos.com
as your MCS URL.
Configure Sophos Linux Sensor alert output
Open
/etc/sophos/runtimedetections.yaml
in a text editor.
Add the following lines, replacing the placeholder values with your actual Sophos Central details:
send_labs_telemetry
:
true
endpoint_telemetry_enabled
:
true
cloud_meta
:
auto
# Set your customer id:
customer_id
:
"{tenant-id}"
mcs
:
token
:
"{LINUX_REPO_API_KEY}"
url
:
"{MCS_URL}"
enabled
:
true
Save the changes and exit.
Restart the sensor:
systemctl
restart
sophoslinuxsensor
Optional: Configure Sophos Linux Sensor to send meta events to Data Lake
Starting from version 5.11.0, SLS supports sending event data to the Sophos Data Lake.
Open
/etc/sophos/runtimedetections.yaml
in a text editor.
Add the following configuration:
investigations
:
reporting_interval
:
5s
zeromq
:
topics
:
-
process_events
:
running_processes_linux_events
audit_user_msg
:
user_events_linux
sinks
:
-
backend
:
mcs
name
:
"mcs"
type
:
mcs
flight_recorder
:
enabled
:
true
tables
:
-
name
:
"process_events"
enabled
:
true
rows
:
1000
filter
:
-
match eventType == "PROCESS_EVENT_TYPE_EXEC"
-
match eventType == "BASELINE_TASK"
-
default ignore
-
name
:
"audit_user_msg"
enabled
:
true
rows
:
1000
filter
:
-
ignore programName == "cron"
-
ignore processPid == 1
-
default match
Save the changes and exit.
Restart the sensor:
systemctl
restart
sophoslinuxsensor
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
'SOPHOS_CAPSULE8'
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
Log Field
UDM Mapping
Logic
categories
read_only_udm.security_result.category_details
Each element in the categories array is added as a separate category_details.
comments
read_only_udm.security_result.description
Directly mapped from the comments field.
confidence
read_only_udm.security_result.severity_details
Directly mapped from the confidence field.
description
read_only_udm.security_result.summary
Directly mapped from the description field.
incident_id
read_only_udm.security_result.rule_id
Directly mapped from the incident_id field.
lineage
principal.process.parent_process...
The lineage array is used to populate a chain of parent processes, up to 15 levels deep. Each element in the lineage array represents a process in the chain, with index 0 being the immediate parent and higher indices representing further ancestors. The pid and name fields of each lineage element are mapped to the corresponding fields in the UDM.
location.container_id
principal.labels.value
Directly mapped from the location.container_id field. The corresponding key is set to "container_id".
location.container_labels.maintainer
principal.labels.value
Directly mapped from the location.container_labels.maintainer field. The corresponding key is set to "maintainer".
location.container_name
principal.labels.value
Directly mapped from the location.container_name field. The corresponding key is set to "container_name".
location.image_id
principal.labels.value
Directly mapped from the location.image_id field. The corresponding key is set to "image_id".
location.image_name
principal.labels.value
Directly mapped from the location.image_name field. The corresponding key is set to "image_name".
location.kubernetes_namespace
principal.labels.value
Directly mapped from the location.kubernetes_namespace field. The corresponding key is set to "kubernetes_namespace".
location.kubernetes_pod
principal.labels.value
Directly mapped from the location.kubernetes_pod field. The corresponding key is set to "kubernetes_pod".
matched_rule
read_only_udm.security_result.rule_name
Directly mapped from the matched_rule field.
metadata.gcp_instance_hostname
principal.hostname
Directly mapped from the metadata.gcp_instance_hostname field.
metadata.gcp_instance_zone
principal.cloud.availability_zone
The availability zone is extracted from the metadata.gcp_instance_zone field using a regular expression.
metadata.gcp_project_id
principal.cloud.project.name
Directly mapped from the metadata.gcp_project_id field.
metadata.gcp_project_numeric_id
principal.cloud.project.id
Directly mapped from the metadata.gcp_project_numeric_id field.
metadata.network_interface_eth0_addr_0
principal.ip
The IP address is extracted from the metadata.network_interface_eth0_addr_0 field using a regular expression.
metadata.network_interface_eth0_hardware_addr
principal.mac
Directly mapped from the metadata.network_interface_eth0_hardware_addr field.
policy_type
read_only_udm.metadata.product_event_type
Directly mapped from the policy_type field.
process_info.args
principal.labels.value
Each element in the process_info.args array is added as a separate label. The key is set to "process_info.arg[index]", where index is the position of the argument in the array.
process_info.name
principal.process.file.full_path
Directly mapped from the process_info.name field.
process_info.pid
principal.process.pid
Directly mapped from the process_info.pid field.
process_info.ppid
principal.process.parent_process.pid
Directly mapped from the process_info.ppid field.
priority
read_only_udm.security_result.severity
Directly mapped from the priority field, converted to uppercase.
timestamp
read_only_udm.metadata.event_timestamp
Directly mapped from the timestamp field.
uuid
read_only_udm.metadata.product_log_id
Directly mapped from the uuid field.
N/A
read_only_udm.metadata.log_type
Set to a constant value of "SOPHOS_CAPSULE8".
N/A
read_only_udm.metadata.event_type
Set to a constant value of "SCAN_HOST".
N/A
read_only_udm.metadata.vendor_name
Set to a constant value of "Sophos".
N/A
read_only_udm.metadata.product_name
Set to a constant value of "Capsule8".
Need more help?
Get answers from Community members and Google SecOps professionals.
