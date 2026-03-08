# Collect NetApp ONTAP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-ontap/  
**Scraped:** 2026-03-05T09:26:47.426645Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect NetApp ONTAP logs
Supported in:
Google secops
SIEM
This document describes how you can collect the NetApp ONTAP logs through Syslog. The parser extracts fields from syslog messages using regular expressions. It then maps the extracted fields to the corresponding UDM (Unified Data Model) fields, effectively converting raw log data into a structured format for security analysis.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have administrative access to NetApp ONTAP cluster.
Ensure that ONTAP can communicate with the Syslog server (Bindplane).
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
system where Bindplane Agent will be installed.
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
Install Bindplane Agent
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
Linux Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Configure BindPlane Agent to ingest Syslog and send to Google SecOps
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
# Replace the below port <54525> and IP <0.0.0.0> with your specific values
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
# Adjust the creds location below according the placement of the credentials file you downloaded
creds
:
'{
json
file
for
creds
}'
# Replace <customer_id> below with your actual ID that you copied
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# You can apply ingestion labels below as preferred
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
netapp_ontap
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
Restart Bindplane Agent to apply the changes
In Linux, to restart the Bindplane Agent, run the following command:
sudo
systemctl
restart
bindplane-agent
In Windows, to restart the Bindplane Agent, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure a Syslog Destination in ONTAP
Access the ONTAP Cluster using SSH, and replace
<ontap-cluster-ip>
with the management IP of your ONTAP cluster:
ssh
admin@<ontap-cluster-ip>
Check
existing
event
filters and notifications
:
event
filter
show
event
notification
show
Create a
Syslog Destination
, replace
<syslog-server-ip>
and
<syslog-server-port>
with your Syslog server details (Bindplane):
event
notification
destination
create
-name
syslog-ems
-syslog
<syslog-server-ip>
-syslog-port
<syslog-server-port>
-syslog-transport
udp-unencrypted
Other options for -syslog-transport:
udp-unencrypted (default)
tcp-unencrypted
tcp-encrypted (for TLS).
Verify
the Syslog
Destination
:
event
notification
destination
show
Configure Existing Event Filters
Link
default filters
to the Syslog destination:
event
notification
create
-filter-name
no-info-debug-events
-destinations
syslog-ems
event
notification
create
-filter-name
default-trap-events
-destinations
syslog-ems
Optional: Create and configure custom filters
Authentication Events Filter (Logins/Logouts): Captures logs where description matches "Logging in" or "Logging out":
event
filter
create
-filter-name
auth_events
event
filter
rule
add
-filter-name
auth_events
-type
include
-message-name
*login*
-severity
info
event
filter
rule
add
-filter-name
auth_events
-type
include
-message-name
*logout*
-severity
info
Security Detection Fields Filter: Captures logs related to nmsdk_language, nmsdk_platform, nmsdk_version, and netapp_version:
event
filter
create
-filter-name
security_fields
event
filter
rule
add
-filter-name
security_fields
-type
include
-message-name
*nmsdk_language*
-severity
info
event
filter
rule
add
-filter-name
security_fields
-type
include
-message-name
*nmsdk_platform*
-severity
info
event
filter
rule
add
-filter-name
security_fields
-type
include
-message-name
*nmsdk_version*
-severity
info
event
filter
rule
add
-filter-name
security_fields
-type
include
-message-name
*netapp_version*
-severity
info
Severity-Based Logs Filter: Captures logs where severity is informational:
event
filter
create
-filter-name
severity_info
event
filter
rule
add
-filter-name
severity_info
-type
include
-message-name
*
-severity
info
Network Activity Filter: Captures logs with src_ip and src_port:
event
filter
create
-filter-name
network_activity
event
filter
rule
add
-filter-name
network_activity
-type
include
-message-name
*src_ip*
-severity
info
event
filter
rule
add
-filter-name
network_activity
-type
include
-message-name
*src_port*
-severity
info
URL Target Logs Filter: Captures logs with URL information:
event
filter
create
-filter-name
url_target
event
filter
rule
add
-filter-name
url_target
-type
include
-message-name
*url*
-severity
info
Apply Each Filter to the Syslog Destination:
event
notification
create
-filter-name
auth_events
-destinations
syslog-ems
event
notification
create
-filter-name
security_fields
-destinations
syslog-ems
event
notification
create
-filter-name
severity_info
-destinations
syslog-ems
event
notification
create
-filter-name
network_activity
-destinations
syslog-ems
event
notification
create
-filter-name
url_target
-destinations
syslog-ems
Verify Notifications:
event
notification
show
UDM Mapping Table
Log Field
UDM Mapping
Logic
code
Not Mapped
description
metadata.description
Extracted from the log message using a grok pattern. Present only when the description is "Logging out" or "Logging in".
intermediary_host
intermediary.hostname
Extracted from the log message using a grok pattern.
nmsdk_language
security_result.detection_fields.value
Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "nmsdk_language".
nmsdk_platform
security_result.detection_fields.value
Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "nmsdk_platform".
nmsdk_version
security_result.detection_fields.value
Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "nmsdk_version".
netapp_version
security_result.detection_fields.value
Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "netapp_version".
product_event_type
metadata.product_event_type
Extracted from the log message using a grok pattern.
security_result.summary
security_result.summary
Extracted from the log message using a grok pattern.
severity
security_result.severity
Set to "INFORMATIONAL" if severity is "info" (case-insensitive).
src_ip
principal.ip
Extracted from the log message using a grok pattern.
src_port
principal.port
Extracted from the log message using a grok pattern.
status
security_result.summary
Extracted from the log message using a grok pattern.
ts
metadata.event_timestamp.seconds
Extracted from the log message using a grok pattern and converted to a timestamp.
url
target.url
Extracted from the log message using a grok pattern.
user
target.user.userid
Extracted from the log message using a grok pattern.
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if description is "Logging out" or "Logging in".
metadata.event_type
Set to "USER_LOGIN" if description is "Logging in".
metadata.event_type
Set to "USER_LOGOUT" if description is "Logging out".
metadata.event_type
Set to "SCAN_UNCATEGORIZED" if description is not "Logging in" or "Logging out".
metadata.log_type
Set to "NETAPP_ONTAP".
metadata.product_name
Set to "NETAPP_ONTAP".
metadata.vendor_name
Set to "NETAPP_ONTAP".
target.platform
Set to "WINDOWS" if nmsdk_platform contains "windows" (case-insensitive).
Need more help?
Get answers from Community members and Google SecOps professionals.
