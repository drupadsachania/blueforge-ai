# Collect Attivo Networks BOTsink logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo/  
**Scraped:** 2026-03-05T09:50:15.451147Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Attivo Networks BOTsink logs
Supported in:
Google secops
SIEM
This document explains how to ingest Attivo Networks BOTsink logs to
Google Security Operations using Bindplane. The parser first attempts to parse
incoming log messages as JSON. If that fails, it uses a series of Grok patterns
to extract fields from Common Event Format (CEF) formatted messages, handling
various formats and potential errors. Finally, it maps the extracted fields to
the Unified Data Model (UDM) schema, enriching the data with additional context
and standardizing the output.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Attivo Networks
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
'ATTIVO'
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
Configure Syslog in Attivo Networks BOTsink
Sign in to your
Attiva Networks
web UI.
Go to
Administration
>
Management
>
Syslog
.
Click
Add
to create a new Syslog profile.
Provide a descriptive name for the profile.
In
Event Forwarding
, select
Enabled
.
Provide BOTsink Standards configuration:
Very Low
: Select
Informational
.
Low
: Select
Warning
.
Medium
: Select
Alert
.
High
: Select
Critical
.
Very High
: Select
Emergency
.
For
Message Format
: Select
CEF
.
Select
Add New Connection
in the profile section.
Provide the following configuration details:
Server Name
: Enter a descriptive name that helps you identify Google SecOps.
Profile Name
: Select the CEF syslog profile you created earlier.
IP address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (for example, enter
514
for
UDP
).
Protocol
: Select
UDP
.
Click
Test Connection
and verify you receive the test data in Bindplane agent and Google SecOps.
Click
OK
.
UDM mapping table
Log Field
UDM Mapping
Logic
alertID
read_only_udm.metadata.product_log_id
Value is taken from the
alertID
field.
cat
read_only_udm.security_result.action_details
Value is taken from the
cat
field.
CEFDeviceProduct
read_only_udm.metadata.product_name
Value is taken from the
CEFDeviceProduct
field.
CEFDeviceVendor
read_only_udm.metadata.vendor_name
Value is taken from the
CEFDeviceVendor
field.
CEFDeviceVersion
read_only_udm.metadata.product_version
Value is taken from the
CEFDeviceVersion
field.
CEFName
Used to extract
operation
,
result
,
module
and
descrip
fields.
CEFSeverity
read_only_udm.security_result.severity
Mapped from the
CEFSeverity
field based on these rules:
-
error
or
warning
:
HIGH
-
(?i)critical
:
CRITICAL
-
(?i)notice
or
(?i)MEDIUM
:
MEDIUM
-
information
,
info
,
Very-Low
, or
Low
:
LOW
CEFSignatureID
read_only_udm.security_result.rule_id
Value is taken from the
CEFSignatureID
field.
cef_version
read_only_udm.additional.fields.value.string_value
Value is taken from the
cef_version
field.
read_only_udm.additional.fields.key
Static value:
CEFVersion
descrip
read_only_udm.metadata.description
Value is taken from the
descrip
field.
dest_domain
read_only_udm.target.domain.name
Value is taken from the
dest_domain
field.
dhost
read_only_udm.target.hostname
Value is taken from the
dhost
field if
service
is
NETBIOS
.
dIPDomain
read_only_udm.target.domain.name
Value is taken from the
dIPDomain
field if
dest_domain
is empty.
dst
read_only_udm.target.ip
Value is taken from the
dst
field.
dst_os
read_only_udm.target.asset.platform_software.platform_version
Value is taken from the
dst_os
field.
dpt
read_only_udm.target.port
Value is taken from the
dpt
field and converted to an integer.
dvc
read_only_udm.principal.hostname, read_only_udm.target.ip, read_only_udm.intermediary.hostname
Logic depends on the values of
dvc
,
src
, and
sip
fields. It can be mapped to principal hostname, target IP, or intermediary hostname based on the availability and format of these fields.
intf
read_only_udm.additional.fields.value.string_value
Value is taken from the
intf
field and converted to a string.
read_only_udm.additional.fields.key
Static value:
intf
mitreTacticName
read_only_udm.security_result.rule_name
Value is taken from the
mitreTacticName
field.
mitreTechniqueId
read_only_udm.security_result.detection_fields.value
Value is taken from the
mitreTechniqueId
field.
read_only_udm.security_result.detection_fields.key
Static value:
Technique name
mitreTechniqueName
read_only_udm.security_result.detection_fields.value
Value is taken from the
mitreTechniqueName
field.
read_only_udm.security_result.detection_fields.key
Static value:
Technique name
module
read_only_udm.additional.fields.value.string_value
Value is taken from the
module
field.
read_only_udm.additional.fields.key
Static value:
module
msg
read_only_udm.metadata.description
Value is taken from the
msg
field after extracting the
protocol
field.
operation
read_only_udm.additional.fields.value.string_value
Value is taken from the
operation
field.
read_only_udm.additional.fields.key
Static value:
operation
protocol
read_only_udm.network.ip_protocol
Value is taken from the
protocol
field if it's either
TCP
or
UDP
.
result
read_only_udm.security_result.action
Mapped from the
result
field based on these rules:
-
(?i)SUCCESS
or
(?i)ALLOW
:
ALLOW
-
CHALLENGE
:
CHALLENGE
-
FAILURE
,
DENY
,
SKIPPED
, or
RATE_LIMIT
:
BLOCK
rt
read_only_udm.metadata.event_timestamp
Value is taken from the
rt
field and parsed as a UNIX timestamp in milliseconds.
shost
read_only_udm.principal.hostname
Value is taken from the
shost
field.
sip
read_only_udm.principal.hostname, read_only_udm.principal.ip
Logic depends on the values of
dvc
and
sip
fields. It can be mapped to principal hostname or IP based on the availability and format of these fields.
smac
read_only_udm.principal.mac
Value is taken from the
smac
field.
source
read_only_udm.principal.hostname
Value is taken from the
source
field.
source_domain
read_only_udm.principal.domain.name
Value is taken from the
source_domain
field.
src
read_only_udm.principal.ip
Value is taken from the
src
field.
subscriberName
read_only_udm.additional.fields.value.string_value
Value is taken from the
subscriberName
field.
read_only_udm.additional.fields.key
Static value:
Subscriber Name
suser
read_only_udm.principal.user.userid, read_only_udm.principal.user.user_display_name
Value is taken from the
suser
field after extracting the username.
threshold
read_only_udm.additional.fields.value.string_value
Value is taken from the
threshold
field.
read_only_udm.additional.fields.key
Static value:
arp-scan-threshold
usrname
read_only_udm.principal.user.email_addresses
Value is taken from the
usrname
field if it's not empty or
N/A
.
vlan
read_only_udm.principal.labels.value
Value is taken from the
vlan
field.
read_only_udm.principal.labels.key
Static value:
vlan
read_only_udm.metadata.event_type
Determined based on the values of
src
,
smac
,
shost
,
dst
,
protocol
,
dvc
, and
service
fields. It can be one of the following:
SCAN_NETWORK
,
NETWORK_CONNECTION
,
NETWORK_UNCATEGORIZED
,
STATUS_UPDATE
, or
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
