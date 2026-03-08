# Collect Acalvio logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/acalvio/  
**Scraped:** 2026-03-05T09:49:19.609820Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Acalvio logs
Supported in:
Google secops
SIEM
This document explains how to ingest Acalvio logs to Google Security Operations
using Bindplane. The parser first extracts fields from raw syslog messages using
grok and key-value pattern matching, then maps those extracted fields to the
Google SecOps Unified Data Model (UDM) schema, categorizes the
event based on specific values, and finally enriches the data with
security-related information like severity and category.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Installed Acalvio ShadowPlex Integration Server
Privileged access to Acalvio ShadowPlex service and instance
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
'ACALVIO'
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
Configure Syslog in Acalvio ShadowPlex
Sign in to the
ShadowPlex Integration Server
UI.
Go to
Settings
>
SIEM
.
Provide the following configuration details:
Click the
Enable
toggle.
Hostname or IP
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Protocol
: Select
UDP
.
Sensor
: Select the Sensor from which the data is streamed.
Click
Test and Save
.
Supported Acalvio log formats
The Acalvio parser supports logs in a SYSLOG format.
Supported Acalvio Sample Logs
SYSLOG + KV
<
14
>
Jan
23
06
:
11
:
07
0.0.0.0
Jan
23
06
:
11
:
07
0.0.0.0
deviceVendor
=
FakeCorp
deviceProduct
=
FakeProduct
deviceVersion
=
eventClassId
=
3
severity
=
7
cat
=
"Lateral Movement Attempted"
startTime
=
"Jan 23 2020 06:10:01.000"
incidentSubCategory
=
"Auth Attempted"
externalId
=
00000000
-
0000
-
0000
-
0000
-
000000000000
customer_id
=
ffffffffffffffffffffffffffffffff
customer_display_name
=
FakeCorp
QA
decoy_source_type
=
ASSET_PROTECTION
srcIp
=
0.0.0.0
dstIp
=
0.0.0.0
dstPort
=
22
dstMAC
=
00
:
00
:
00
:
00
:
00
:
00
endTime
=
"Jan 23 2020 06:10:01.000"
subnet
=
0.0.0.0
/
24
dstHostName
=
sanitized_hostname
userIdsUsed
=
sanitized_user
Authentication_attempted
=
True
UDM mapping table
Log field
UDM mapping
Logic
adc_email
read_only_udm.target.user.email_addresses
Value taken from
adc_email
field.
app
read_only_udm.principal.application
Value taken from
app
field.
cat
read_only_udm.security_result.summary
Value taken from
cat
field. If
cat
is
Vulnerability Exploited
, the value is overwritten with the value of
Intrusion_method_used
field.
customer_id
read_only_udm.metadata.description
Value is added to the description field:
CustomerId: %{customer_id}, JobId: %{job_id}, InvestigationId: %{investigation_id}
deviceProduct
read_only_udm.metadata.product_name
Value taken from
deviceProduct
field.
deviceVendor
read_only_udm.metadata.vendor_name
Value taken from
deviceVendor
field.
deviceVersion
read_only_udm.metadata.product_version
Value taken from
deviceVersion
field.
dstHostName
read_only_udm.target.hostname
Value taken from
dstHostName
field.
dstIp
read_only_udm.target.ip
Value taken from
dstIp
field.
dstMAC
read_only_udm.target.mac
Value taken from
dstMAC
field.
dstPort
read_only_udm.target.port
Value taken from
dstPort
field and converted to integer.
incidentid
read_only_udm.metadata.product_log_id
Value taken from
incidentid
field.
incidentSubCategory
read_only_udm.metadata.product_event_type, read_only_udm.security_result.description
Value taken from
incidentSubCategory
field.
Intrusion_method_used
read_only_udm.security_result.summary
Value taken from
Intrusion_method_used
field if
cat
is
Vulnerability Exploited
.
investigation_id
read_only_udm.metadata.description
Value is added to the description field:
CustomerId: %{customer_id}, JobId: %{job_id}, InvestigationId: %{investigation_id}
job_id
read_only_udm.metadata.description
Value is added to the description field:
CustomerId: %{customer_id}, JobId: %{job_id}, InvestigationId: %{investigation_id}
read_only_udm.metadata.event_type
Set to
GENERIC_EVENT
if
srcIp
is
Unknown
or empty. Set to
STATUS_UPDATE
otherwise.
read_only_udm.principal.resource.type
Hardcoded to
scan_type
.
read_only_udm.security_result.category
Determined based on the values of
cat
,
incidentSubCategory
, and
sr_category
fields.
read_only_udm.security_result.severity
Set to
HIGH
if
severity
is greater than 7,
MEDIUM
if
severity
is greater than 3, and
LOW
otherwise.
srcIp
read_only_udm.principal.ip
Value taken from
srcIp
field.
startTime
read_only_udm.metadata.event_timestamp
Value taken from
startTime
field and parsed as a timestamp. If
startTime
is empty, the value is set to
%{ts_month} %{ts_day} %{ts_time}
.
userIdsUsed
read_only_udm.principal.user.userid
Value taken from
userIdsUsed
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
