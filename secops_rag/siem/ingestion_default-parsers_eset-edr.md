# Collect ESET EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-edr/  
**Scraped:** 2026-03-05T09:23:50.903051Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ESET EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest ESET logs to Google Security Operations using
Bindplane. The Logstash parser code first attempts to extract fields from ESET
EDR logs in SYSLOG or JSON format using a series of
grok
patterns. Depending
on the extracted fields and their format, it further processes the data using
key-value (
kv
) filters or JSON parsing to structure the information into a
Unified Data Model (UDM) representation.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to ESET Protect
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
ingestion_labels
:
log_type
:
'ESET_EDR'
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
to the path where the
authentication file was saved in the
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
Configure Syslog for ESET PROTECT on-premises
Sign in to the
ESET Protect
web console.
Go to
More
>
Settings
>
Advanced Settings
>
Syslog Server
.
Select the toggle next to
Enable Syslog
.
Provide the following configuration details:
Host
: Enter the Bindplane agent IP address
Port
: Enter the Bindplane agent port number (
514
for UDP)
Format
: Select
Syslog
Transport
: Select
UDP
Trace log verbosity
: Select
Informational
Export logs to Syslog toggle
: Select
Enable
Exported logs format
: Select
JSON
Click
Save
.
Configure Syslog for ESET PROTECT Cloud
Sign in to the
ESET Protect
web console.
Go to
More
>
Settings
>
Syslog Server
.
Select the toggle next to
Enable Syslog
.
Provide the following configuration details:
Format of payload
: Select
JSON
Format of the envelope
: Select
Syslog
Minimum log Level
: Select
Informational
Event types to log
: Select
All
event types
Destination IP
: Enter the Bindplane agent IP address
Port
: Enter the Bindplane agent port number (
514
for UDP)
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
action
event1.idm.read_only_udm.security_result.action
Conditionally set to
BLOCK
if the value is
Blocked
.
actionTaken
event2.idm.read_only_udm.metadata.event_type
Conditionally set to
SCAN_PROCESS
if the value is
Cleaned by deleting
.
actionTaken
event1.idm.read_only_udm.security_result.action_details
Directly mapped from the
actionTaken
field.
actionTaken
event2.idm.read_only_udm.security_result.action_details
Directly mapped from the
actionTaken
field.
accountName
event2.idm.read_only_udm.additional.fields.value.string_value
Directly mapped from the
accountName
field. The key is set to
accountName
.
app
event3.idm.read_only_udm.principal.application
Directly mapped from the
app
field.
circumstances
event2.idm.read_only_udm.additional.fields.value.string_value
Directly mapped from the
circumstances
field. The key is set to
circumstances
.
Computer_name
event3.idm.read_only_udm.principal.hostname
Directly mapped from the
Computer_name
field.
Computer_name
event3.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
Computer_name
field.
date_time
Detection_name
event3.idm.read_only_udm.security_result.threat_name
Directly mapped from the
Detection_name
field.
Detectiontype
event3.idm.read_only_udm.security_result.category_details
Directly mapped from the
Detectiontype
field.
dst
event2.idm.read_only_udm.target.ip
Directly mapped from the
dst
field.
dst
event2.idm.read_only_udm.target.asset.ip
Directly mapped from the
dst
field.
dstPort
event2.idm.read_only_udm.target.port
Directly mapped from the
dstPort
field after converting it to an integer.
event
event1.idm.read_only_udm.metadata.description
Directly mapped from the
event
field.
event_type
event1.idm.read_only_udm.metadata.product_event_type
Directly mapped from the
event_type
field.
event_type
event1.idm.read_only_udm.metadata.event_type
Conditionally set to
NETWORK_CONNECTION
if the value is
FirewallAggregated_Event
.
hash
event1.idm.read_only_udm.target.file.sha1
Directly mapped from the
hash
field after converting it to lowercase.
hostname
event1.idm.read_only_udm.target.hostname
Directly mapped from the
hostname
field.
hostname
event1.idm.read_only_udm.target.asset.hostname
Directly mapped from the
hostname
field.
hostname
event.alert.devices.hostname
Directly mapped from the
hostname
field.
ipv4
event1.idm.read_only_udm.principal.ip
Directly mapped from the
ipv4
field. This field is first stored in a temporary field
udm_ip
.
ipv4
event1.idm.read_only_udm.principal.asset.ip
Directly mapped from the
ipv4
field. This field is first stored in a temporary field
udm_ip
.
ipv4
event.alert.devices.ip_addresses
Directly mapped from the
ipv4
field after converting it to an IP address.
Logged_user
event3.idm.read_only_udm.principal.user.userid
Directly mapped from the
Logged_user
field.
objectUri
event1.idm.read_only_udm.target.file.full_path
Directly mapped from the
objectUri
field.
objectUri
event2.idm.read_only_udm.target.file.full_path
Directly mapped from the
objectUri
field.
processName
event2.idm.read_only_udm.target.process.file.full_path
Directly mapped from the
processName
field.
processName
event1.idm.read_only_udm.principal.process.file.full_path
Directly mapped from the
processName
field.
process_id
event3.idm.read_only_udm.principal.process.pid
Directly mapped from the
process_id
field.
process_id
event2.idm.read_only_udm.target.process.pid
Directly mapped from the
process_id
field.
protocol
event1.idm.read_only_udm.network.ip_protocol
Directly mapped from the
protocol
field.
proto
event2.idm.read_only_udm.network.ip_protocol
Directly mapped from the
proto
field.
result
event2.idm.read_only_udm.security_result.action
Conditionally set to
ALLOW
if the value is
Success
.
Scanner
event3.idm.read_only_udm.security_result.description
Directly mapped from the
Scanner
field.
severity
event1.idm.read_only_udm.security_result.severity
Mapped from the
severity
field based on these conditions: -
INFO
,
Informational
,
DEBUG
,
info
:
INFORMATIONAL
-
ERROR
,
error
:
ERROR
-
WARNING
,
Warning
:
LOW
source_address
event1.idm.read_only_udm.principal.ip
Directly mapped from the
source_address
field.
source_address
event1.idm.read_only_udm.principal.asset.ip
Directly mapped from the
source_address
field.
source_port
event1.idm.read_only_udm.principal.port
Directly mapped from the
source_port
field after converting it to an integer.
source_uuid
event1.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
source_uuid
field.
src
event2.idm.read_only_udm.principal.ip
Directly mapped from the
src
field.
src
event2.idm.read_only_udm.principal.asset.ip
Directly mapped from the
src
field.
srcPort
event2.idm.read_only_udm.principal.port
Directly mapped from the
srcPort
field after converting it to an integer.
target_address
event1.idm.read_only_udm.target.ip
Directly mapped from the
target_address
field.
target_address
event1.idm.read_only_udm.target.asset.ip
Directly mapped from the
target_address
field.
target_port
event1.idm.read_only_udm.target.port
Directly mapped from the
target_port
field after converting it to an integer.
threatName
event2.idm.read_only_udm.security_result.threat_name
Directly mapped from the
threatName
field.
threatName
event.alert.alert_short_name
Directly mapped from the
threatName
field.
Time_of_occurrence
event3.idm.read_only_udm.additional.fields.value.string_value
Directly mapped from the
Time_of_occurrence
field. The key is set to
Time_of_occurrence
.
type
event2.idm.read_only_udm.security_result.category_details
Directly mapped from the
type
field.
type
event2.idm.read_only_udm.metadata.event_type
Conditionally set to
GENERIC_EVENT
if no other specific event type is matched.
user_id
event2.idm.read_only_udm.principal.user.userid
Directly mapped from the
user_id
field.
event1.idm.read_only_udm.metadata.event_type
Conditionally set to
FILE_UNCATEGORIZED
if the value of
event_type
is
Threat_Event
.
event1.idm.read_only_udm.metadata.log_type
Set to
ESET_EDR
.
event1.idm.read_only_udm.metadata.product_name
Conditionally set to
ESET
if the value of
event_type
is
FirewallAggregated_Event
.
event2.idm.read_only_udm.metadata.log_type
Set to
ESET_EDR
.
event2.idm.read_only_udm.metadata.product_name
Set to
EDR
.
event2.idm.read_only_udm.metadata.vendor_name
Set to
ESET
.
event3.idm.read_only_udm.metadata.event_type
Conditionally set based on these rules: -
USER_UNCATEGORIZED
if
principal_user_present
is
true
. -
STATUS_UPDATE
if
principal_machine_id_present
is
true
. -
GENERIC_EVENT
otherwise.
event3.idm.read_only_udm.metadata.log_type
Set to
ESET_EDR
.
event3.idm.read_only_udm.metadata.product_name
Set to
EDR
.
event3.idm.read_only_udm.metadata.vendor_name
Set to
ESET
.
event.alert.is_significant
Set to
true
and then converted to a boolean.
event3.idm.read_only_udm.security_result.description
Conditionally set to the value of
kv_data
if
Scanner
is empty.
Need more help?
Get answers from Community members and Google SecOps professionals.
