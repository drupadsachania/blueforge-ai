# Collect AlgoSec Security Management logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/algosec/  
**Scraped:** 2026-03-05T09:49:40.224398Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AlgoSec Security Management logs
Supported in:
Google secops
SIEM
This document explains how to ingest AlgoSec Security Management logs to Google Security Operations using a Bindplane Agent. The parser extracts the fields, handling both CEF and non-CEF formatted logs. It parses common fields like timestamps, IP addresses, and event details, then maps them to the UDM based on the product (Suite, Firewall Analyzer, FireFlow) and event ID, setting appropriate metadata and security result fields. It also handles specific event types like login/logout, administrative alerts, and analysis reports, extracting relevant details and setting severity levels.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to AlgoSec Firewall Analyzer, FireFlow and AppViz.
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
ALGOSEC
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
Configure Syslog for Firewall Analyzer
Sign in to the
AFA
appliance using SSH.
Go to the
syslog-ng
configuration directory:
cd
/etc/syslog-ng
Backup the existing configuration:
cp
syslog-ng.conf
syslog-ng.conf.orig
Edit the syslog-ng configuration file:
vi
syslog-ng.conf
Add the following lines to define the remote syslog server:
destination
d_remote
{
udp
(
"<bindplane-server-ip>"
port
(
514
))
;
}
;
log
{
source
(
s_sys
)
;
destination
(
d_remote
)
;
}
;
Replace
<bindplane-server-ip>
with the IP address of the Bindplane agent.
Save and exit the editor.
Restart the syslog-ng service to apply changes:
service
syslog-ng
restart
Optional: Verify Syslog Configuration:
Go to
Administration
>
Syslog Server Settings
.
Click
Test Connectivity
.
Configure Syslog for FireFlow
Sign in to the
FireFlow
machine as
root
.
Open the
/etc/syslog.conf
file for editing.
vi
/etc/syslog.conf
Add the following line to the file:
local0.*@<BindplaneAgent>
.
Replace
<BindplaneAgent>
with the IP address of the Bindplane agent server.
Configure Syslog for AppViz
Sign in to the
AppViz
appliance via SSH.
Go to the
syslog-ng
configuration directory:
cd
/etc/syslog-ng
Backup the existing configuration:
cp
syslog-ng.conf
syslog-ng.conf.orig
Edit the syslog-ng configuration file:
vi
syslog-ng.conf
Add the following to define the remote syslog server:
destination
d_remote
{
udp
(
"<bindplane-server-ip>"
port
(
514
))
;
}
;
log
{
source
(
s_sys
)
;
destination
(
d_remote
)
;
}
;
Replace
<bindplane-server-ip>
with the IP address of the Bindplane agent.
Save and exit the editor.
Restart the syslog-ng service to apply changes:
service
syslog-ng
restart
Verify Syslog Configuration:
In the AppViz interface, go to
Administration
>
Syslog Server Settings
.
Click
Test Connectivity
.
Configure Syslog for Login and Logout Events
Sign in to the
ASMS appliance
via SSH.
Go to the
syslog-ng
configuration directory:
cd
/etc/syslog-ng
Backup the existing configuration:
cp
syslog-ng.conf
syslog-ng.conf.orig
Edit the syslog-ng configuration file:
vi
syslog-ng.conf
Add the following to define the remote syslog server:
destination
d_remote
{
udp
(
"<bindplane-server-ip>"
port
(
514
))
;
}
;
log
{
source
(
s_sys
)
;
destination
(
d_remote
)
;
}
;
Replace
<bindplane-server-ip>
with the IP address of your syslog server.
Save and exit the editor.
Restart the syslog-ng service to apply changes:
service
syslog-ng
restart
UDM Mapping Table
Log Field
UDM Mapping
Logic
by_user
principal.user.user_display_name
The value of the
by_user
field from the raw log is assigned to this UDM field.
collection_time
metadata.event_timestamp
The seconds and nanos fields are combined to create a timestamp.
comm
target.process.command_line
The value of the
comm
field extracted from the
desc
field using grok is assigned to this UDM field.
datetime
metadata.event_timestamp
The date and time are extracted from the raw log and used to populate the event timestamp.
desc
metadata.description
The value of the
desc
field from the raw log is assigned to this UDM field when no other description is available.
dest_ip
target.ip
The value of the
dest_ip
field from the raw log is assigned to this UDM field.
dest_port
target.port
The value of the
dest_port
field from the raw log is assigned to this UDM field.
details
security_result.summary
The value of the
details
field from the raw log is assigned to this UDM field.
device
principal.asset.hostname
The value of the
device
field from the raw log is assigned to this UDM field.
dst_ip
target.ip
The value of the
dst_ip
field from the raw log is assigned to this UDM field.
dst_port
target.port
The value of the
dst_port
field from the raw log is assigned to this UDM field.
event_id
metadata.product_event_type
The value of the
event_id
field from the raw log is assigned to this UDM field.  It is also used in parser logic to determine the
metadata.event_type
and other fields.
event_name
metadata.product_event_type
The value of the
event_name
field from the raw log is assigned to this UDM field.
firewall
target.hostname
The value of the
firewall
field from the raw log is assigned to this UDM field.
host
principal.hostname
The value of the
host
field from the raw log is assigned to this UDM field.
host_type
principal.asset.category
The value of the
host_type
field from the raw log is assigned to this UDM field.
iporhost
principal.ip
/
principal.hostname
/
target.ip
/
target.hostname
/
observer.ip
/
observer.hostname
If the value is an IP address, it's mapped to
principal.ip
,
target.ip
, or
observer.ip
depending on the log source and event type. If it's a hostname, it's mapped to
principal.hostname
,
target.hostname
, or
observer.hostname
.
IP
principal.ip
The value of the
IP
field from the raw log is assigned to this UDM field.
kv_data
security_result.summary
The value of the
kv_data
field from the raw log is assigned to this UDM field.
log_type
metadata.log_type
Hardcoded to
ALGOSEC
.
metric
security_result.action_details
The value of the
metric
field from the raw log is assigned to this UDM field.
msg
security_result.summary
/
security_result.description
The value of the
msg
field from the raw log is used to populate either the summary or description of the security result, depending on the context. It is also used to extract
risk_level
,
risk_count
,
risk_code
, and
risk_title
fields.
pid
target.process.pid
The value of the
pid
field extracted from the
desc
field using grok is assigned to this UDM field.
product
metadata.product_name
The value of the
product
field from the raw log is assigned to this UDM field.
report
security_result.description
The value of the
report
field from the raw log is included in the description of the security result.
report_data.Device IP
target.ip
The value of the
Device IP
field from the parsed JSON data is assigned to this UDM field.
report_data.Highest Risk Level
security_result.description
The value of the
Highest Risk Level
field from the parsed JSON data is included in the description of the security result. It is also used to determine the severity of the security result.
report_data.Security Rating Score
security_result.description
The value of the
Security Rating Score
field from the parsed JSON data is included in the description of the security result.
Requestor.Email
principal.user.email_addresses
The value of the
Email
field within the
Requestor
object from the parsed JSON data is assigned to this UDM field.
Requestor.Name
principal.user.user_display_name
The value of the
Name
field within the
Requestor
object from the parsed JSON data is assigned to this UDM field.
RequestType
target.resource.attribute.labels
The value of the
RequestType
field from the raw log is added as a label to the target resource.
risk_title
security_result.summary
The value of the
risk_title
field from the raw log is assigned to this UDM field.
src_ip
principal.ip
The value of the
src_ip
field from the raw log is assigned to this UDM field.
src_port
principal.port
The value of the
src_port
field from the raw log is assigned to this UDM field.
status
security_result.description
/
security_result.action_details
The value of the
status
field from the raw log is included in the description of the security result or action details, depending on the context. It is also used to determine the severity of the security result.
target_app
target.application
The value of the
target_app
field from the raw log is assigned to this UDM field.
TemplateName
metadata.description
The value of the
TemplateName
field from the raw log is assigned to this UDM field.
url
security_result.url_back_to_product
The value of the
url
field from the raw log is assigned to this UDM field.
user
principal.user.userid
The value of the
user
field from the raw log is assigned to this UDM field.
vendor
metadata.vendor_name
The value of the
vendor
field from the raw log is assigned to this UDM field.
version
metadata.product_version
The value of the
version
field from the raw log is assigned to this UDM field.
WorkFlow
target.resource.attribute.labels
The value of the
WorkFlow
field from the raw log is added as a label to the target resource.
(Parser Logic)
extensions.auth.type
Hardcoded to
MACHINE
.
(Parser Logic)
security_result.action
Determined based on the
event_id
and other fields. Typically set to
ALLOW
or
BLOCK
.
(Parser Logic)
security_result.category
Hardcoded to
POLICY_VIOLATION
for Firewall Analyzer events.
(Parser Logic)
security_result.description
Constructed based on other fields, providing context and details about the event.
(Parser Logic)
security_result.severity
Determined based on the
event_id
,
msg
, and other fields. Typically set to
LOW
,
MEDIUM
, or
HIGH
.
(Parser Logic)
metadata.event_type
Determined based on the
event_id
and other fields. Examples include
USER_LOGIN
,
USER_LOGOUT
,
USER_RESOURCE_ACCESS
,
GENERIC_EVENT
,
STATUS_UNCATEGORIZED
,
SCAN_HOST
,
NETWORK_CONNECTION
, and
STATUS_UPDATE
.
Need more help?
Get answers from Community members and Google SecOps professionals.
