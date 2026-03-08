# Collect CyberArk Privilege Cloud logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-privilege-cloud/  
**Scraped:** 2026-03-05T09:53:59.156534Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CyberArk Privilege Cloud logs
Supported in:
Google secops
SIEM
This document explains how to ingest CyberArk Privilege Cloud logs to
Google Security Operations using Bindplane. The parser code transforms the logs from
their raw SYSLOG + KV format into the Google SecOps Unified Data Model
(UDM) format. It first extracts fields from CEF formatted messages using grok
patterns and key-value parsing, then maps those fields and others to their
corresponding UDM fields, enriching the data with standardized values for vendor,
product, and severity.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to CyberArk Privilege Cloud
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
directory on Linux or in the installation directory
on Windows.
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:6514"
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
'CYBERARK_PRIVILEGE_CLOUD'
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
Install Secure Tunnel
Make sure that your
Machine ID
is unique, even when the machines are deployed in multiple domains.
Download the
Privilege Cloud software package
from
Deploy the Privilege Cloud Connector (Standard)
, copy the
Secure Tunnel
ZIP file, and
unzip
it.
Run the installation from the unzipped folder.
On the
Select Installation Folder
page, enter the location of the installation folder, and click
Next
.
On the
Ready to Install
page, click
Install
.
When the installation is complete, click
Finish
; the configuration tool is launched.
Configure Secure Tunnel
On the
Authenticate to Privilege Cloud
page, enter the following details
and then click
Next
:
Subdomain or Customer ID
: The subdomain is your system identifier in
the system address, as displayed in the Privilege Cloud Portal FQDN:
https://<subdomain>.Privilegecloud.cyberark.com
. Enter only the
<subdomain>
identifier, not the whole URL. Alternatively, use the Customer ID provided to you by CyberArk.
User name & Password
: Enter the credentials provided by CyberArk Support.
On the
Configure on-premise components
page, add the components that you
want to connect through the Secure Tunnel, and click
Configure Components
.
Provide the following configuration details:
Component Type
: Select
SIEM
.
Host Address
: Enter the Bindplane agent host address (SIEM component must include a hostname).
Destination Port
: Enter the Bindplane agent port number.
Remote Port
: The port used by the CyberArk to interface with your Secure Tunnel (The Remote Port is provided to you by CyberArk support, typically the port is
1468
).
Click
Advanced
to display this column.
Access through Secure Tunnels
: You can configure which Secure Tunnels your servers will access through, even if these Secure Tunnels are running on a different machine.
Click
Configure Components
>
Close
.
UDM mapping table
Log Field
UDM Mapping
Logic
act
security_result.action_details
Directly mapped from the
act
field in the raw log.
app
network.application_protocol
Mapped from the
app
field in the raw log and transformed using the logic in
parse_app_protocol.include
.
cn1
additional.fields.value.string_value
Directly mapped from the
cn1
field in the raw log.
cn1Label
additional.fields.key
Directly mapped from the
cn1Label
field in the raw log.
cn2
additional.fields.value.string_value
Directly mapped from the
cn2
field in the raw log.
cn2Label
additional.fields.key
Directly mapped from the
cn2Label
field in the raw log.
cs1
additional.fields.value.string_value
Directly mapped from the
cs1
field in the raw log.
cs1Label
additional.fields.key
Directly mapped from the
cs1Label
field in the raw log.
cs2
additional.fields.value.string_value
Directly mapped from the
cs2
field in the raw log.
cs2Label
additional.fields.key
Directly mapped from the
cs2Label
field in the raw log.
cs3
additional.fields.value.string_value
Directly mapped from the
cs3
field in the raw log.
cs3Label
additional.fields.key
Directly mapped from the
cs3Label
field in the raw log.
cs4
additional.fields.value.string_value
Directly mapped from the
cs4
field in the raw log.
cs4Label
additional.fields.key
Directly mapped from the
cs4Label
field in the raw log.
cs5
additional.fields.value.string_value
Directly mapped from the
cs5
field in the raw log.
cs5Label
additional.fields.key
Directly mapped from the
cs5Label
field in the raw log.
device_event_class_id
metadata.product_event_type
Directly mapped from the
device_event_class_id
field in the raw log.
device_version
metadata.product_version
Directly mapped from the
device_version
field in the raw log.
dhost
target.hostname
Directly mapped from the
dhost
field in the raw log.
duser
target.user.user_display_name
Directly mapped from the
duser
field in the raw log.
dvc
about.ip
Directly mapped from the
dvc
field in the raw log.
event_name
metadata.product_event_type
Directly mapped from the
event_name
field in the raw log.
externalId
metadata.product_log_id
Directly mapped from the
externalId
field in the raw log.
fname
additional.fields.value.string_value
Directly mapped from the
fname
field in the raw log.
msg
metadata.description
Directly mapped from the
msg
field in the raw log.
reason
security_result.summary
Directly mapped from the
reason
field in the raw log.
severity
security_result.severity
Mapped from the
severity
field in the raw log and transformed to "LOW", "MEDIUM", "HIGH", or "CRITICAL" based on its value.
shost
principal.ip
Directly mapped from the
shost
field in the raw log.
suser
principal.user.user_display_name
Directly mapped from the
suser
field in the raw log.
time
metadata.event_timestamp.seconds
Directly mapped from the
time
field in the raw log after being parsed and converted to a timestamp.
metadata.event_type
Set to "USER_UNCATEGORIZED" if
suser
is present and
duser
is not. Otherwise, set to "GENERIC_EVENT".
metadata.log_type
Set to "CYBERARK_PRIVILEGE_CLOUD".
metadata.product_name
Set to "CYBERARK_PRIVILEGE_CLOUD".
principal.asset.hostname
Value taken from either
shost
or
dvc
fields, if they contain a hostname.
principal.asset.ip
Value taken from either
shost
or
dvc
fields, if they contain an IP address.
principal.hostname
Value taken from either
shost
or
dvc
fields, if they contain a hostname.
target.asset.hostname
Value taken from
dhost
field, if it contains a hostname.
additional.fields.key
The key for additional fields is determined by the corresponding label field (e.g.,
cn1Label
for
cn1
).
Need more help?
Get answers from Community members and Google SecOps professionals.
