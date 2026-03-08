# Collect Kaspersky AV logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaspersky-av/  
**Scraped:** 2026-03-05T09:57:33.445824Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Kaspersky AV logs
Supported in:
Google secops
SIEM
This document explains how to ingest Kaspersky Antivirus logs to Google Security Operations using Bindplane. The parser code first attempts to parse the raw log message as JSON. If that fails, it uses regular expressions (
grok
patterns) to extract fields from the message based on common Kaspersky AV log formats.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Kaspersky Antivirus
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
KASPERSKY_AV
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
Configure events export in Kaspersky AV
Sign in to the
Kaspersky Security Center
console.
Select the
Administration Server
which events you want to export.
In the
Administration Server
workspace, click the
Events
tab.
Click Configure notifications and event export link.
Select
Configure export to SIEM system
in the list.
Provide the following configuration details:
SIEM system
: Select
Arcsight (CEF format)
.
SIEM system server address
: Enter the Bindplane agent IP address.
SIEM system server port
: Enter the Bindplane agent port number (for example,
514
for
UDP
).
Protocol
: Select
UDP
.
Click
OK
.
UDM mapping table
Log field
UDM mapping
Logic
Application
network.http.user_agent
Directly mapped from the
Application
field in the raw log.
Application path
target.process.file.full_path
Used with the
Name
field to construct the full path if
Application path
is present in the raw log.
Component
target.resource.name
Directly mapped from the
Component
field in the raw log.
Content category
security_result.category_details
Added to the
security_result.category_details
field if
Content category
is present in the raw log.
Content category source
target.resource.type
If the value contains
databases
, the UDM field is set to
DATABASE
.
Erreur
security_result.summary
Directly mapped from the
Erreur
field in the raw log if the
summary
field is empty.
et
metadata.product_event_type
Directly mapped from the
et
field in the raw log if the
product_event_type
field is empty.
et
security_result.category_details
Added to the
security_result.category_details
field.
etdn
extensions.vulns.vulnerabilities.description
Directly mapped from the
etdn
field in the raw log.
File SHA256 hash
target.process.file.sha256
Directly mapped from the
File SHA256 hash
field in the raw log.
gn
security_result.about.labels
The
key
is set to
GN
and the
value
is set to the value of the
gn
field.
hdn
principal.hostname
Directly mapped from the
hdn
field in the raw log.
hip
principal.ip
Directly mapped from the
hip
field in the raw log.
host_name
principal.hostname
Directly mapped from the
host_name
field in the raw log.
intermediary_host
intermediary.hostname
Directly mapped from the
intermediary_host
field in the raw log.
intermediary_hostname
intermediary.hostname
Directly mapped from the
intermediary_hostname
field in the raw log.
kv_data1
This field is parsed and its values are mapped to other UDM fields.
kv_data2
This field is parsed and its values are mapped to other UDM fields.
label
network.http.user_agent
If the value is
User-Agent
, the UDM field is populated with the value of the
description
field.
label
principal.hostname
If the value is
Host
, the UDM field is populated with the hostname extracted from the
description
field.
label
security_result.description
For other values, the UDM field is populated with a string containing the
label
and
description
fields.
MD5
target.process.file.md5
Directly mapped from the
MD5
field in the raw log after converting it to lowercase.
MD5 file hash
target.process.file.md5
Directly mapped from the
MD5 file hash
field in the raw log.
message
This field is parsed and its values are mapped to other UDM fields.
method
network.http.method
Directly mapped from the
method
field in the raw log if it matches a list of HTTP methods.
name
target.file.full_path
Directly mapped from the
name
field in the raw log.
Nom
target.process.file.full_path
Used with the
application_path
field to construct the full path.
p1
target.process.file.sha256
Directly mapped from the
p1
field in the raw log after converting it to lowercase if the
SHA256
field is empty and the value is a hexadecimal string.
p2
target.process.file.full_path
Directly mapped from the
p2
field in the raw log.
p5
security_result.rule_name
Directly mapped from the
p5
field in the raw log.
p7
principal.user.user_display_name
Directly mapped from the
p7
field in the raw log if the
User
and
user_name
fields are empty.
Process ID
principal.process.pid
Directly mapped from the
Process ID
field in the raw log.
process_id
target.process.pid
Directly mapped from the
process_id
field in the raw log.
protocol
network.application_protocol
If the value contains
http
(case-insensitive), the UDM field is set to
HTTP
.
Reason
security_result.summary
Directly mapped from the
Reason
field in the raw log.
Requested web page
target.url
Directly mapped from the
Requested web page
field in the raw log.
Result
If the value is
Allowed
, the
sr_action
field is set to
ALLOW
.
rtid
security_result.about.labels
The
key
is set to
rtid
and the
value
is set to the value of the
rtid
field.
Rule
security_result.description
Directly mapped from the
Rule
field in the raw log.
SHA256
target.process.file.sha256
Directly mapped from the
SHA256
field in the raw log after converting it to lowercase.
sr_action
security_result.action
Merged into the
security_result.action
field.
summary
security_result.summary
Directly mapped from the
summary
field in the raw log.
task_name
security_result.about.labels
The
key
is set to
TaskName
and the
value
is set to the value of the
task_name
field.
threat_action_taken
If the value is
blocked
, the
security_action
field is set to
BLOCK
. If the value is
allowed
, the
security_action
field is set to
ALLOW
.
timestamp
metadata.event_timestamp
Used to populate the event timestamp.
Type
security_result.threat_name
Directly mapped from the
Type
field in the raw log.
URL
network.http.referral_url
Directly mapped from the
url
field in the raw log.
User
principal.user.user_display_name
The username is extracted from this field and mapped to the UDM field.
User
principal.administrative_domain
The domain is extracted from this field and mapped to the UDM field.
user_name
principal.user.user_display_name
Directly mapped from the
user_name
field in the raw log if the
User
field is empty.
metadata.event_type
Set to
SCAN_VULN_NETWORK
if
Application path
and
Name
are present,
STATUS_UNCATEGORIZED
if
hdn
or
host_name
are present, or
GENERIC_EVENT
otherwise.
metadata.vendor_name
Always set to
KASPERSKY
.
metadata.product_name
Always set to
KASPERSKY_AV
.
metadata.log_type
Always set to
KASPERSKY_AV
.
Need more help?
Get answers from Community members and Google SecOps professionals.
