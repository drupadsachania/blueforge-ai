# Collect Cisco UCS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ucs/  
**Scraped:** 2026-03-05T09:52:41.851534Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco UCS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco UCS logs to Google Security Operations using Bindplane. The parser code first attempts to parse the raw log message as JSON. If that fails, it uses regular expressions (
grok
patterns) to extract fields from the message based on common Cisco UCS log formats.
.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Cisco UCS
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
```
cmd
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
```
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
```
bash
sudo
sh
-
c
"$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)"
install_unix
.
sh
```
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
CISCO_UCS
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
```bash
sudo systemctl restart bindplane-agent
```
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
```cmd
net stop BindPlaneAgent && net start BindPlaneAgent
```
Configure Syslog for Cisco UCS
Sign in to the
Cisco UCS
Manager.
Select the
Admin
tab.
Expand
Faults, Events, and Audit Log
.
Select
Syslog
.
Locate the
File
category, and select
Enabled
for the Admin State.
Select the alarm level from the menu (for example,
Warnings
).
Click
Save Changes
.
Locate
Remote Destinations
category on the right.
Select
Enabled
for
Server 1 Admin State
.
Provide the following configuration details:
Level
: Select
Informational
.
Hostname
: Enter the Bindplane IP address. The default port in UCS is
514
.
Facility
: Select
Local7
.
Click
Save Changes
.
UDM mapping table
Log field
UDM mapping
Logic
application
read_only_udm.principal.application
Value taken from the 'application' field extracted by the Grok pattern.
desc
read_only_udm.security_result.description
Value taken from the 'desc' field extracted by the Grok pattern.
desc
read_only_udm.security_result.severity
If 'desc' field contains
Warning
, set to
HIGH
.
filename
read_only_udm.principal.process.file.full_path
Value taken from the 'filename' field extracted by the Grok pattern.
file_size
read_only_udm.principal.process.file.size
Value taken from the 'file_size' field extracted by the Grok pattern and converted to an unsigned integer.
host
read_only_udm.principal.ip
Value taken from the 'host' field extracted by the Grok pattern.
hostname
read_only_udm.principal.hostname
Value taken from the 'hostname' field extracted by the Grok pattern.
prod_evt_type
read_only_udm.metadata.product_event_type
Value taken from the 'prod_evt_type' field extracted by the Grok pattern.
service
read_only_udm.target.application
Value taken from the 'service' field extracted by the Grok pattern.
severity
read_only_udm.security_result.severity
If 'severity' field contains
error
(case-insensitive), set to
ERROR
.
timestamp
read_only_udm.metadata.event_timestamp.seconds
Value taken from the 'timestamp' field extracted by the Grok pattern and parsed as a timestamp.
user
read_only_udm.principal.user.userid
Value taken from the 'user' field extracted by the Grok pattern.
read_only_udm.extensions.auth.type
Set to
MACHINE
if the 'user' field is not empty.
read_only_udm.metadata.event_type
Logic based on field presence:
-
USER_LOGIN
if 'user' field is not empty.
-
GENERIC_EVENT
if both 'hostname' and 'host' fields are empty.
-
STATUS_UPDATE
otherwise.
read_only_udm.metadata.log_type
Hardcoded to
CISCO_UCS
.
read_only_udm.metadata.product_name
Hardcoded to
Cisco UCS
.
read_only_udm.metadata.vendor_name
Hardcoded to
Cisco
.
Need more help?
Get answers from Community members and Google SecOps professionals.
