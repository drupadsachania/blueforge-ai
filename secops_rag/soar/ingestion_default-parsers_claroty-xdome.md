# Collect Claroty xDome logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-xdome/  
**Scraped:** 2026-03-05T09:53:06.240883Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Claroty xDome logs
Supported in:
Google secops
SIEM
This document explains how to ingest Claroty xDome logs to Google Security Operations using Bindplane. The parser extracts fields from Claroty xDome syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Claroty xDome management console or appliance.
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
Option A: UDP configuration
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
'CLAROTY_XDOME'
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
```
Option B: TCP with TLS configuration (recommended for security)
receivers
:
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
tls
:
# Path to the server's public TLS certificate file when using self-signed certificates
cert_file
:
/etc/bindplane/certs/cert.pem
key_file
:
/etc/bindplane/certs/key.pem
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
'CLAROTY_XDOME'
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
tcplog
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
For TLS configuration, ensure the certificate files exist at the specified paths or generate self-signed certificates if needed.
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
Detailed Syslog Configuration
Sign in to the
Claroty xDome
Web UI.
Click the
Settings
tab in the navigation bar.
Select
System Settings
from the drop-down menu.
Click
My Integrations
in the Integrations section.
Click
+ Add Integration
.
Select
Internal Services
from the Category drop-down menu.
Select
SIEM
and
Syslog
from the
Integration
drop-down menu.
Click
Add
.
Enter the following configuration details:
Destination IP
: Enter the Bindplane Agent IP address.
Transport Protocol
: Select
UDP
or
TCP
, or
TLS
depending on your Bindplane configuration.
If you select the TLS security protocol, do the following:
Check the
Check Hostnames
option to verify if the server's hostname matches any of the names present in the
X.509 certificate
.
Check the
Use Custom Certificate Authority
option to use a custom Certificate Authority (CA) instead of the default CA. Upload the custom certificate file or insert the certificate (in PEM format) into the space provided.
Destination Port
: The default value for TCP, TLS, and UDP is
514
. (Hover over the field to use the clickable arrows to select a different destination port).
Advanced Options
: Enter the Advanced Options settings:
Message Format
: Select
CEF
(other options include JSON, or LEEF format).
Syslog Protocol Standard
: Select
RFC 5424
or
RFC 3164
.
Integration Name
: Enter a meaningful name for the integration (for example,
Google SecOps syslog
).
Deployment options
: Select
Run from the collection server
or
Run from the cloud
option depending on your xDome configuration.
Go to the
Integration Tasks
parameters.
Turn on the
Export Claroty xDome Communication Events Using Syslog
option to enable exporting Claroty xDome communication events.
From the
Event Types Selection
drop-down menu, click
Select All
.
Choose the device conditions to export
: Select
All Devices
option to export the communication event data of all affected devices.
Turn on the
Export Claroty xDome Device Changes Alerts Change Log to Syslog
option to export Claroty xDome change events.
In the
Change Event Types Selection
drop-down, select the
change event types
you want to export.
Choose the device conditions you want to export
: Select
All Devices
to export the change event data of all the affected devices.
Turn on the
Export Claroty xDome Alert Information for Affected Devices Using Syslog
option to export alert information for any alert type, including custom alerts.
From
Alert Types
, click
Select All
.
Turn on the
Export Claroty xDome Vulnerability Information for Affected Devices Using Syslog
option to export Claroty xDome vulnerability types.
In the
Vulnerability Types Selection
drop-down menu, select the
vulnerability types
you want to export.
Specify the
CVSS Threshold
number. This parameter lets you set a CVSS threshold to send a vulnerability using Syslog. Only vulnerabilities greater or equal to this threshold will be exported. The threshold will revert to the CVSS V3 Base Score by default and CVSS V2 Base Score if the CVSS V3 score is unknown.
Choose the device conditions to export
: Select
All Devices
to export the data of all affected devices.
Turn on the
Export Claroty xDome Server Incidents Information to Syslog
option to export Claroty xDome server incidents.
Select the collection server types you want to export from the
Collection Server Selection
drop-down menu.
Select the server incidents you want to export on the
Server Incidents Selection
drop-down menu.
Click
Apply
to save the configuration settings.
Need more help?
Get answers from Community members and Google SecOps professionals.
