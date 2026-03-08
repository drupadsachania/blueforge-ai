# Collect Symantec DLP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-dlp/  
**Scraped:** 2026-03-05T09:28:40.376991Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec DLP logs
Supported in:
Google secops
SIEM
This document explains how to collect Symantec DLP logs by using Bindplane. The parser code first attempts to parse the incoming Symantec DLP log data as XML. If the XML parsing fails, it assumes a SYSLOG + KV (CEF) format and uses a combination of
grok
and
kv
filters to extract key-value pairs and map them to the unified data model (UDM).
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the Symantec DLP.
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:54525"
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
SYSLOG
namespace
:
symantec_dlp
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
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Symantec DLP
Sign in to the
Symantec Server administration
console.
Select
Manage
>
Policies
>
Response rules
.
Select
Configure response rule
and enter a rule name.
Provide the following details:
Actions
: select
Log to a syslog server
.
Host
: enter the
Bindplane
IP address.
Port
: enter the
Bindplane
port number.
Message
: enter the following message:
|symcdlpsys|APPLICATION_NAME|$APPLICATION_NAME$|APPLICATION_USER|$APPLICATION_USER$|ATTACHMENT_FILENAME|$ATTACHMENT_FILENAME$|BLOCKED|$BLOCKED$|DATAOWNER_NAME|$DATAOWNER_NAME$|DATAOWNER_EMAIL|$DATAOWNER_EMAIL$|DESTINATION_IP|$DESTINATION_IP$|ENDPOINT_DEVICE_ID|$ENDPOINT_DEVICE_ID$|ENDPOINT_LOCATION|$ENDPOINT_LOCATION$|ENDPOINT_MACHINE|$ENDPOINT_MACHINE$|ENDPOINT_USERNAME|$ENDPOINT_USERNAME$|PATH|$PATH$|FILE_NAME|$FILE_NAME$|PARENT_PATH|$PARENT_PATH$|INCIDENT_ID|$INCIDENT_ID$|INCIDENT_SNAPSHOT|$INCIDENT_SNAPSHOT$|MACHINE_IP|$MACHINE_IP$|MATCH_COUNT|$MATCH_COUNT$|OCCURRED_ON|$OCCURRED_ON$|POLICY|$POLICY$|RULES|$RULES$|PROTOCOL|$PROTOCOL$|QUARANTINE_PARENT_PATH|$QUARANTINE_PARENT_PATH$|RECIPIENTS|$RECIPIENTS$|REPORTED_ON|$REPORTED_ON$|SCAN|$SCAN$|SENDER|$SENDER$|MONITOR_NAME|$MONITOR_NAME$|SEVERITY|$SEVERITY$|STATUS|$STATUS$|SUBJECT|$SUBJECT$|TARGET|$TARGET$|URL|$URL$|USER_JUSTIFICATION|$USER_JUSTIFICATION$|
Debugging
: select
Level 4
.
Click
Apply
.
UDM Mapping Table
Log field
UDM mapping
Logic
act
security_result.action
If
act
is
Passed
, set to
ALLOW
. If
act
is
Modified
, set to
ALLOW_WITH_MODIFICATION
. If
act
is
Blocked
, set to
BLOCK
. Otherwise, set to
UNKNOWN_ACTION
.
application_name
target.application
Directly mapped.
asset_ip
principal.ip, principal.asset.ip
Directly mapped.
asset_name
principal.hostname, principal.asset.hostname
Directly mapped.
attachment_name
security_result.about.file.full_path
Directly mapped.
blocked
security_result.action_details
Directly mapped.
calling_station_id
principal.mac, principal.asset.mac
If
calling_station_id
is a MAC address, map it directly after replacing
-
with
:
and converting to lowercase.
called_station_id
target.mac, target.asset.mac
If
called_station_id
is a MAC address, extract the MAC address part before the
:
and map it directly after replacing
-
with
:
and converting to lowercase.
category1
security_result.detection_fields
Create a label with key
category1
and value from
category1
.
category2
security_result.detection_fields
Create a label with key
category2
and value from
category2
.
category3
security_result.detection_fields
Create a label with key
category3
and value from
category3
.
client_friendly_name
target.user.userid
Directly mapped.
dataowner_mail
principal.user.email_addresses
Directly mapped if it's a valid email address.
description
metadata.description
Directly mapped.
dest_location
target.location.country_or_region
Directly mapped if it's not
RED
.
deviceId
target.asset_id
Mapped as
ID:%{deviceId}
.
device_version
metadata.product_version
Directly mapped.
dhost
network.http.referral_url
Directly mapped.
dlp_type
security_result.detection_fields
Create a label with key
dlp_type
and value from
dlp_type
.
DLP_EP_Incident_ID
security_result.threat_id, security_result.detection_fields
Directly mapped to
threat_id
. Also, create a label with key
Incident ID
and value from
DLP_EP_Incident_ID
.
domain
principal.administrative_domain
Directly mapped.
dst
target.ip, target.asset.ip
Directly mapped if it's a valid IP address.
endpoint_machine
target.ip, target.asset.ip
Directly mapped if it's a valid IP address.
endpoint_user_department
target.user.department
Directly mapped.
endpoint_user_email
target.user.email_addresses
Directly mapped.
endpoint_user_manager
target.user.managers
Create a manager object with
user_display_name
from
endpoint_user_manager
.
endpoint_user_name
target.user.user_display_name
Directly mapped.
endpoint_user_title
target.user.title
Directly mapped.
event_description
metadata.description
Directly mapped.
event_id
metadata.product_log_id
Directly mapped.
event_source
target.application
Directly mapped.
event_timestamp
metadata.event_timestamp
Directly mapped.
file_name
security_result.about.file.full_path
Directly mapped.
filename
target.file.full_path, src.file.full_path
Directly mapped to
target.file.full_path
. If
has_principal
is true, also map to
src.file.full_path
and set
event_type
to
FILE_COPY
.
host
src.hostname, principal.hostname, principal.asset.hostname
If
cef_data
contains
CEF
, map to all three fields. Otherwise, map to
principal.hostname
and
principal.asset.hostname
.
incident_id
security_result.threat_id, security_result.detection_fields
Directly mapped to
threat_id
. Also, create a label with key
Incident ID
and value from
incident_id
.
location
principal.resource.attribute.labels
Create a label with key
Location
and value from
location
.
match_count
security_result.detection_fields
Create a label with key
Match Count
and value from
match_count
.
monitor_name
additional.fields
Create a label with key
Monitor Name
and value from
monitor_name
.
nas_id
target.hostname, target.asset.hostname
Directly mapped.
occurred_on
principal.labels, additional.fields
Create a label with key
Occurred On
and value from
occurred_on
for both
principal.labels
and
additional.fields
.
policy_name
sec_result.detection_fields
Create a label with key
policy_name
and value from
policy_name
.
policy_rule
security_result.rule_name
Directly mapped.
policy_severity
security_result.severity
Mapped to
severity
after converting to uppercase. If
policy_severity
is
INFO
, map it as
INFORMATIONAL
. If
policy_severity
is not one of
HIGH
,
MEDIUM
,
LOW
, or
INFORMATIONAL
, set
severity
to
UNKNOWN_SEVERITY
.
policy_violated
security_result.summary
Directly mapped.
Protocol
network.application_protocol, target.application, sec_result.description
If
Protocol
is not
FTP
or
Endpoint
, map it to
network.application_protocol
after parsing it using the
parse_app_protocol.include
file. If
Protocol
is
FTP
, map it to
target.application
. If
Protocol
is
Endpoint
, set
sec_result.description
to
Protocol=%{Protocol}
.
recipient
target.user.email_addresses, about.user.email_addresses
For each email address in
recipient
, map it to both
target.user.email_addresses
and
about.user.email_addresses
.
recipients
network.http.referral_url, target.resource.attribute.labels
Directly mapped to
network.http.referral_url
. Also, create a label with key
recipients
and value from
recipients
.
reported_on
additional.fields
Create a label with key
Reported On
and value from
reported_on
.
rules
security_result.detection_fields
Create a label with key
Rules
and value from
rules
.
sender
network.email.from, target.resource.attribute.labels
If
sender
is a valid email address, map it to
network.email.from
. Also, create a label with key
sender
and value from
sender
.
server
target.application
Directly mapped.
Severity
security_result.severity
See
policy_severity
for mapping logic.
src
principal.ip, principal.asset.ip
Directly mapped if it's a valid IP address.
status
principal.labels, additional.fields
Create a label with key
Status
and value from
status
for both
principal.labels
and
additional.fields
.
subject
target.resource.attribute.labels, network.email.subject
Create a label with key
subject
and value from
subject
. Also, map
subject
to
network.email.subject
.
target_type
target.resource.attribute.labels
Create a label with key
Target Type
and value from
target_type
.
timestamp
metadata.event_timestamp
Directly mapped after parsing it using the
date
filter.
url
target.url
Directly mapped.
user
target.user.userid
Directly mapped.
user_id
principal.user.userid
Directly mapped.
username
principal.user.userid
Directly mapped.
N/A
metadata.product_name
Set to
SYMANTEC_DLP
.
N/A
metadata.vendor_name
Set to
SYMANTEC
.
N/A
metadata.event_type
If
event_type
is not empty, map it directly. Otherwise, if
host
is not empty and
has_principal
is true, set to
SCAN_NETWORK
. Otherwise, set to
GENERIC_EVENT
.
N/A
metadata.product_event_type
If
policy_violated
contains
-NM-
or
data
contains
DLP NM
, set to
Network Monitor
. If
policy_violated
contains
-EP-
or
data
contains
DLP EP
, set to
Endpoint
.
N/A
metadata.log_type
Set to
SYMANTEC_DLP
.
Need more help?
Get answers from Community members and Google SecOps professionals.
