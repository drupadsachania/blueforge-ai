# Collect Broadcom SSL VA logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ssl-va/  
**Scraped:** 2026-03-05T09:51:36.213517Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Broadcom SSL VA logs
Supported in:
Google secops
SIEM
This document explains how to ingest Broadcom Secure Sockets Layer (SSL)
Visibility Appliance logs to Google Security Operations using Bindplane. The parser
extracts fields from the syslog messages using a series of
grok
patterns to
match various log formats, then maps the extracted fields to the corresponding
Unified Data Model (UDM) schema attributes using
mutate
filters for consistent
security event representation.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Broadcom SSL Visibility Appliance
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
'BROADCOM_SSL_VA'
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
Configure Syslog for Broadcom SSL Visibility Appliance
Sign in to the
SSL Visibility Appliance
Web UI.
Go to
Platform Management
>
Remote Logging
.
Click
Add
.
Provide the following configuration details:
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (default
514
).
Protocol
: Select
UDP
.
Facility
: Select a Syslog facility (for example,
local0
).
Log Set
: Select
Session and Appliance Logs
.
Click
Save
(the server entry will show
Connected
after the first heartbeat).
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.action_details
The value of this field is assigned to
security_result.action_details
.
ciphersuite
network.tls.cipher
The value of this field is assigned to
network.tls.cipher
.
data
This field is used for extracting other fields but not directly mapped to the UDM.
destip
target.ip
The value of this field is assigned to
target.ip
.
destport
target.port
The value of this field is converted to integer and assigned to
target.port
.
hostname
principal.hostname
The value of this field is assigned to
principal.hostname
.
pid
principal.process.pid
The value of this field is assigned to
principal.process.pid
.
prodlogid
metadata.product_log_id
The value of this field is assigned to
metadata.product_log_id
.
rule
security_result.rule_id
The value of this field is assigned to
security_result.rule_id
.
segment_id
about.labels.value
The value of this field is assigned to
about.labels.value
where
about.labels.key
is
segment_id
.
srcip
principal.ip
The value of this field is assigned to
principal.ip
.
srcPort
principal.port
The value of this field is converted to integer and assigned to
principal.port
.
status
security_result.action
The value of this field determines the value of
security_result.action
. If it contains
Success
, the value is set to
ALLOW
, otherwise
BLOCK
.
timestamp
metadata.event_timestamp.seconds
The value of this field is parsed to a timestamp and the seconds part is assigned to
metadata.event_timestamp.seconds
.
tlsversion
network.tls.version
The value of this field is assigned to
network.tls.version
.
about.resource.attribute.labels.key
The value of this field is set to
Flag list
.
about.resource.attribute.labels.value
The value of this field is taken from the
flag_list
field after undergoing some transformations.
metadata.event_type
The value of this field is set to
NETWORK_CONNECTION
if both
srcip
and
destip
fields are not empty.
metadata.log_type
The value of this field is set to
BROADCOM_SSL_VA
.
metadata.product_name
The value of this field is set to
SSL Visibility
.
metadata.vendor_name
The value of this field is set to
Broadcom
.
security_result.category
The value of this field is set to
SOFTWARE_MALICIOUS
.
target.application
The value of this field is set to
ssldata
.
Need more help?
Get answers from Community members and Google SecOps professionals.
