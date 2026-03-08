# Collect Cisco Wireless Intrusion Prevention System (WIPS) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wips/  
**Scraped:** 2026-03-05T09:52:54.570881Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Wireless Intrusion Prevention System (WIPS) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Wireless Intrusion Prevention
System (WIPS) logs to Google Security Operations using Bindplane. The parser
extracts key-value pairs from the syslog messages, then maps those values to
Unified Data Model (UDM) fields. It determines the appropriate
event_type
based on the presence of principal, target, and user information, and categorizes
security events based on
eventType
and other fields.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to Cisco Access Point (AP) / Wireless LAN Controller (WLC)
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
Save the file securely on the system where BindPlane will be installed.
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
'CISCO_WIPS'
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
Configure Adaptive Wireless Intrusion Prevention System (aWIPS) on Cisco Catalyst
Sign in to Cisco Catalyst using SSH.
Enter global config to enable aWIPS under the AP profile:
configure
terminal
ap
profile
<profile-name>
awips
Configure syslog throttle interval for 60 seconds:
awips-syslog
throttle
period
60
Configure Syslog using Cisco AP profiles
In AP-join profile (via CLI):
configure
terminal
ap
profile
<profile-name>
syslog
host
<Bindplane_IP_address>
syslog
level
informational
syslog
facility
local0
end
Configure Syslog on Cisco WLC (GUI)
Sign in to the
WLC
web UI.
Go to
Management
>
Logs
>
Config
.
Enter the Bindplane agent IP address in the
Syslog Server IP Address
field.
Click
Add
.
Provide the following configuration details:
Syslog Severity
: Select
Informational
.
Syslog Facility
: Select
Local Use 0
.
Click
Apply
.
Click
Save Configuration
.
Configure Syslog on Access Points using WLC (CLI)
Global AP syslog host:
config
ap
syslog
host
global
<Bindplane_IP_address>
Configure the specific AP syslog host:
config
ap
syslog
host
specific
<AP-name>
<Bindplane_IP_address>
Set the AP syslog severity:
config
ap
logging
syslog
level
informational
Set the facility for AP messages:
config
logging
syslog
facility
local0
UDM mapping table
Log Field
UDM Mapping
Logic
applicationCategoryData
security_result.summary
Directly mapped.
applicationSpecificAlarmID
target.resource.attribute.labels.applicationSpecificAlarmID
Converted to a label on the target resource.
attackerMacAddr
target.mac
Directly mapped.
authEntityId
principal.resource.attribute.labels.authEntityId
Converted to a label on the principal resource.
category
security_result.category_details
Directly mapped.
detectingApCount
target.resource.attribute.labels.detectingApCount
Converted to a label on the target resource.
description
metadata.description
Directly mapped.
displayName
principal.user.userid
Extracted using regular expression
host/(?P<user_id>[\\w-]+)
from
displayName
if the pattern matches.
eventType
metadata.product_event_type
Directly mapped.
instanceId
principal.resource.attribute.labels.instanceId
Converted to a label on the principal resource.
instanceUuid
metadata.product_log_id
Directly mapped.
instanceVersion
principal.resource.attribute.labels.instanceVersion
Converted to a label on the principal resource.
macInfo
target.resource.attribute.labels.macInfo
Converted to a label on the target resource.
notificationDeliveryMechanism
target.resource.attribute.labels.notificationDeliveryMechanism
,
network.ip_protocol
Converted to a label on the target resource. If the value contains "snmp" (case-insensitive),
network.ip_protocol
is set to "UDP".
previousSeverity
target.resource.attribute.labels.previousSeverity
Converted to a label on the target resource. Set to "AUTHTYPE_UNSPECIFIED" if
eventType
is "USER_AUTHENTICATION_FAILURE" and
user_id
is not empty. Copied from the log's
timestamp
. Determined by parser logic based on several conditions:
"USER_LOGIN" if
eventType
is "USER_AUTHENTICATION_FAILURE" and
user_id
is not empty.
"NETWORK_CONNECTION" if both
is_target_present
and
is_principal_present
are true.
"STATUS_UPDATE" if
is_principal_present
is true.
"USER_UNCATEGORIZED" if
user_id
is not empty.
"GENERIC_EVENT" otherwise. Hardcoded to "CISCO_WIPS". Hardcoded to "Wireless Intrusion Prevention System (WIPS)". Hardcoded to "Cisco". Set to "UDP" if
notificationDeliveryMechanism
contains "snmp" (case-insensitive). Mapped from either
reportingEntityAddress
or
source
if they are not IPs. Mapped from either
reportingEntityAddress
or
source
if they are IPs. Extracted using regular expression from
source
if it is a MAC address. Converted to a label on the principal resource. Converted to a label on the principal resource.
reportingEntityAddress
principal.ip
,
principal.hostname
If it's an IP address, mapped to
principal.ip
. Otherwise, mapped to
principal.hostname
.
severity
security_result.severity
Mapped based on these conditions:
"CRITICAL" if
severity
is "0", "1", "CRITICAL", or "VERY-HIGH".
"HIGH" if
severity
is "2", "3", "4", or "HIGH".
"MEDIUM" if
severity
is "5" or "MEDIUM".
"LOW" if
severity
is "6", "7", or "LOW".
sigAlertDescription
security_result.description
Directly mapped.
signatureName
target.resource.attribute.labels.signatureName
Converted to a label on the target resource.
source
principal.hostname
,
principal.ip
,
principal.mac
If it's an IP address, mapped to
principal.ip
. If it's a MAC address, mapped to
principal.mac
. Otherwise, mapped to
principal.hostname
.
srcObjectClassId
principal.resource.attribute.labels.srcObjectClassId
Converted to a label on the principal resource.
srcObjectId
principal.resource.attribute.labels.srcObjectId
Converted to a label on the principal resource.
subclassName
security_result.rule_name
Directly mapped. Set to "BLOCK" if
applicationSpecificAlarmID
contains "BlockList" (case-insensitive) or if
eventType
is one of "SIGNATURE_ATTACK", "MALICIOUS_ROGUE_AP_DETECTED", or "USER_AUTHENTICATION_FAILURE". Determined by parser logic based on
eventType
:
"NETWORK_MALICIOUS" if
eventType
is "MALICIOUS_ROGUE_AP_DETECTED".
"NETWORK_SUSPICIOUS" if
eventType
is "SIGNATURE_ATTACK".
"AUTH_VIOLATION" if
eventType
is "USER_AUTHENTICATION_FAILURE".
timestamp
metadata.event_timestamp
The
seconds
and
nanos
fields are directly mapped.
Need more help?
Get answers from Community members and Google SecOps professionals.
