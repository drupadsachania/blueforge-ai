# Collect Cylance PROTECT logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect/  
**Scraped:** 2026-03-05T09:22:58.701421Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cylance PROTECT logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cylance PROTECT logs to
Google Security Operations using Bindplane. The Logstash parser code transforms
Cylance PROTECT syslog messages into a Unified Data Model (UDM). It extracts
fields from the syslog message, normalizes them, maps them to UDM fields, and
enriches the data with threat severity and category information.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Cylance PROTECT
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
'CYLANCE_PROTECT'
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
Configure Syslog in Cylance Protect
Sign in to the
Cylance
management console.
Go to
Settings
>
Application
.
Select the
Syslog/SIEM
checkbox.
Select all
events
.
Provide the following configuration details:
SIEM
: Select
Syslog
.
Protocol
: Select
UDP
.
Select the
Allow messages over 2KB
checkbox.
IP/Domain
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (for example,
514
for UDP).
Facility
: Select the type of application logging.
Click
Test Connection
.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
Agent Version
metadata.product_version
Value extracted from
Agent Version: <value>
Cylance Score
security_result.severity_details
Value extracted from
Cylance Score: <value>
security_result.severity
Mapped based on the following logic:
- HIGH: if Cylance Score > 67
- MEDIUM: if Cylance Score > 33
- LOW: if Cylance Score <= 33
Detected By
security_result.detection_fields.value
Value extracted from
Detected By: <value>
Device Id
principal.asset_id
Value extracted from
Device Id: <value>
and prepended with
Cylance:
Device Ids
principal.asset_id
Value extracted from
Device Ids: <value>
and prepended with
Cylance:
, used when
Device Id
is not present
Device Name
principal.hostname
Value extracted from
Device Name: <value>
Device Name
target.hostname
Value extracted from
Device Name: <value>
, used for specific event types like
ScriptControl
Device Names
principal.hostname
Value extracted from
Device Names: <value>
, used when
Device Name
is not present
Description
security_result.summary
Value extracted from
Description: <value>
, used for specific event types like
OpticsCaeNetworkEvent
Destination IP
target.ip
Value extracted from
Destination IP: <value>
Destination Port
target.port
Value extracted from
Destination Port: <value>
Event Id
metadata.product_log_id
Value extracted from
Event Id: <value>
Event Name
Used to determine specific event subtypes and apply corresponding logic
Event Type
metadata.product_event_type
Value extracted from
Event Type: <value>
metadata.event_type
Mapped based on the
Event Type
and
Event Name
fields, default value is
GENERIC_EVENT
File Name
principal.process.file.full_path
Value extracted from
File Name: <value>
and combined with
Path: <value>
to form the full path
File Path
target.file.full_path
Value extracted from
File Path: <value>
Instigating Process ImageFileSha256
principal.process.file.sha256
Value extracted from
Instigating Process ImageFileSha256: <value>
Instigating Process Name
principal.process.file.full_path
Value extracted from
Instigating Process Name: <value>
Instigating Process Owner
principal.user.userid
Value extracted from
Instigating Process Owner: <value>
, the username is extracted after splitting by
//
if present
Instigating Process Owner
principal.administrative_domain
Domain name extracted from
Instigating Process Owner: <value>
by splitting by
//
if present
IP Address
principal.ip
IP address(es) extracted from
IP Address: (<value>)
Interpreter
security_result.rule_labels.value
Value extracted from
Interpreter: <value>
Interpreter Version
security_result.rule_labels.value
Value extracted from
Interpreter Version: <value>
Logged On Users
about.user.userid
Usernames extracted from
Logged On Users: (<value>)
MAC Address
principal.mac
MAC address extracted from
MAC Address: (<value>)
and formatted with colons
MD5
principal.process.file.md5
Value extracted from
MD5: <value>
Message
Used for extracting data for specific event types like
AuditLog
OS
principal.platform
Mapped to
WINDOWS
if the
OS
field contains
Windows
Path
principal.process.file.full_path
Value extracted from
Path: <value>
and combined with
File Name: <value>
to form the full path
Policy Name
security_result.rule_name
Value extracted from
Policy Name: <value>
Process ID
principal.process.pid
Value extracted from
Process ID: <value>
Process Name
principal.process.file.full_path
Value extracted from
Process Name: <value>
Resolved Address
network.dns.answers.name
Value extracted from
Resolved Address: <value>
SHA256
principal.process.file.sha256
Value extracted from
SHA256: <value>
Source IP
principal.ip
Value extracted from
Source IP: <value>
, used for specific event types
Status
security_result.action
Mapped to specific UDM actions based on the value:
-
Quarantined
: QUARANTINE
-
Cleared
: ALLOW_WITH_MODIFICATION
Target Domain Name
network.dns.questions.name
Value extracted from
Target Domain Name: <value>
Target Process ImageFileSha256
target.process.file.sha256
Value extracted from
Target Process ImageFileSha256: <value>
Target Process Name
target.process.file.full_path
Value extracted from
Target Process Name: <value>
Target Process Owner
target.user.userid
Value extracted from
Target Process Owner: <value>
, the username is extracted after splitting by
//
if present
Target Process Owner
target.administrative_domain
Domain name extracted from
Target Process Owner: <value>
by splitting by
//
if present
Target Registry KeyPath
target.registry.registry_key
Value extracted from
Target Registry KeyPath: <value>
Threat Classification
security_result.threat_name
Value extracted from
Threat Classification: <value>
User
principal.user.userid
Username extracted from
User: <value>
if present, used when
User Name
is not present
User
principal.user.email_addresses
Email address extracted from
User: <value>
if present, used when
User Name
is not present
User Name
principal.user.userid
Value extracted from
User Name: <value>
Violation Type
security_result.summary
Value extracted from
Violation Type: <value>
and prepended with
ExploitAttempt:
Violation Type
security_result.threat_name
Value extracted from
Violation Type: <value>
Zone Names
security_result.description
Value extracted from
Zone Names: (<value>)
and prepended with
Zone_Names:
metadata.vendor_name
Hardcoded to
Cylance
metadata.product_name
Value extracted from the log message, either
PROTECT
or
OPTICS
metadata.log_type
Hardcoded to
CYLANCE_PROTECT
network.ip_protocol
Hardcoded to
TCP
for
OpticsCaeNetworkEvent
events
network.application_protocol
Hardcoded to
DNS
for
OpticsCaeDnsEvent
events
security_result.rule_labels.key
Set to
Interpreter
or
Interpreter Version
based on the available field
security_result.detection_fields.key
Hardcoded to
Detected By
security_result.category
Mapped based on the event type, possible values include:
- SOFTWARE_SUSPICIOUS
- AUTH_VIOLOATION
- POLICY_VIOLATION
- NETWORK_SUSPICIOUS
- EXPLOIT
- SOFTWARE_MALICIOUS
security_result.action
Mapped based on the event type and specific conditions, possible values include:
- ALLOW
- BLOCK
- QUARANTINE
- ALLOW_WITH_MODIFICATION
Need more help?
Get answers from Community members and Google SecOps professionals.
