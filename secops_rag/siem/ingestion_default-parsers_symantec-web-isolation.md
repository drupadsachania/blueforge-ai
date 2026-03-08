# Collect Symantec Web Isolation logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-web-isolation/  
**Scraped:** 2026-03-05T09:28:49.404705Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec Web Isolation logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec Web Isolation logs to
Google Security Operations using Bindplane. The parser handles two primary message
types from Symantec Web Isolation: data trace messages and device messages.
It extracts fields from JSON-formatted logs, performs data transformations like
date parsing and user agent conversion, and maps the extracted data to the
Unified Data Model (UDM) handling different log structures based on the
traceId
and
event_type
fields.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to the Symantec Web Isolation platform
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
```
cmd
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
```
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
```
bash
sudo
sh
-
c
"$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)"
install_unix
.
sh
```
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
'SYMANTEC_WEB_ISOLATION'
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
Configure Syslog in Symantec Web Isolation platform
Sign in to your
Symantec Web Isolation
web UI.
Go to
System Configuration
>
External Log Server
>
New External Log Server
>
Syslog Server
.
Provide the following configuration details:
Status
: Select the checkbox to
Enable
.
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (for example,
514
for
UDP
).
Protocol
: Select
UDP
.
Appname
: Enter a
Tag
to identify the Web Isolation platform.
Facility
: Syslog facility name related to Web Isolation logs.
Click
Create
.
Go to
Reports
>
Log Forwarding
.
Click
Edit
.
Provide the following configuration details:
Activity Logs
: Select the newly added Bindplane server.
Management Audit Logs
: Select the newly added Bindplane server.
Gateway Audit Logs
: Select the newly added Bindplane server.
Click
Update
.
UDM mapping table
Log Field
UDM Mapping
Logic
action
security_result.summary
Concatenated with
action_reason
to form the summary.
action_reason
security_result.summary
Concatenated with
action
to form the summary.
content_action
security_result.action_details
Direct mapping.
createdAt
metadata.event_timestamp
Converted to timestamp using UNIX_MS format.
creationDate
metadata.event_timestamp
Converted to timestamp using UNIX_MS format.
data.level
security_result.severity
Mapped to INFORMATIONAL, LOW, or HIGH based on value.
data.properties.environment.str
intermediary.location.name
Direct mapping.
data.properties.hostname.str
intermediary.hostname
Direct mapping.
destination_ip
target.ip
Direct mapping.
destination_ip_country_name
target.location.country_or_region
Direct mapping.
device.current_risk_warnings
security_result.category_details
Direct mapping.
device.identifier
target.asset.product_object_id
Direct mapping.
device.model
hardware.model
Direct mapping.
device.os_version
target.asset.platform_software.platform_version
Direct mapping.
device.serial_number
hardware.serial_number
Direct mapping.
device.udid
target.asset.asset_id
Prefixed with "UDID:" before mapping.
device.user.email
target.user.email_addresses
Direct mapping.
device.user.id
target.user.userid
Direct mapping.
device.user.name
target.user.user_display_name
Direct mapping.
device.user.organization.id
target.user.groupid
Direct mapping.
device.user.organization.name
target.user.group_identifiers
Direct mapping.
event
metadata.product_event_type
Direct mapping.
event_type
metadata.event_type
Set to "GENERIC_EVENT" or "NETWORK_HTTP" based on log data.
file_name
target.file.names
Direct mapping.
file_type
about.labels
,
about.resource.attribute.labels
Added as a label with key "file_type".
id
metadata.product_log_id
Direct mapping.
isolation_session_id
network.parent_session_id
Direct mapping.
level
security_result.severity
Mapped to INFORMATIONAL, LOW, or HIGH based on value.
original_source_ip
principal.ip
Direct mapping.
policy_version
security_result.rule_version
Direct mapping.
properties.environment
intermediary.location.name
Direct mapping.
properties.hostname
intermediary.hostname
Direct mapping.
referer_url
network.http.referral_url
Direct mapping.
request_method
network.http.method
Direct mapping.
resource_response_headers.x-nauthilus-traceid
network.community_id
Direct mapping.
response_status_code
network.http.response_code
Direct mapping.
rule_id
security_result.rule_id
Direct mapping.
rule_name_at_log_time
security_result.rule_name
Direct mapping.
rule_type
security_result.rule_type
Direct mapping.
service
principal.application
Direct mapping.
session_id
network.session_id
Direct mapping.
severity
security_result.severity
Mapped to LOW, MEDIUM, or HIGH based on value.
source_ip
principal.ip
Direct mapping.
source_ip_country_name
principal.location.country_or_region
Direct mapping.
source_port
principal.port
Direct mapping.
sub_type
security_result.summary
Direct mapping.
target.asset.type
target.asset.type
Set to "MOBILE" if
device.model
contains "ipad" or "iphone".
target.asset.platform_software.platform
target.asset.platform_software.platform
Set to "MAC" if
device.model
contains "ipad" or "iphone".
timestamp
metadata.event_timestamp
Parsed using
yyyy-MM-dd HH:mm:ss.SSS Z
format.
total_bytes
network.received_bytes
Direct mapping if greater than 0.
traceId
metadata.product_log_id
Direct mapping.
type
metadata.product_event_type
Direct mapping.
url
target.url
Direct mapping.
url_host
principal.hostname
Direct mapping.
user_download_usage_bytes
network.received_bytes
Direct mapping.
user_total_usage_bytes
about.labels
,
about.resource.attribute.labels
Added as a label with key "user_total_usage_bytes".
user_upload_usage_bytes
network.sent_bytes
Direct mapping.
username
principal.user.user_display_name
Direct mapping.
vendor_name
metadata.vendor_name
Set to "Broadcom Inc.".
product_name
metadata.product_name
Set to "Symantec Web Isolation".
log_type
metadata.log_type
Set to "SYMANTEC_WEB_ISOLATION".
sandbox
about.labels
,
about.resource.attribute.labels
Added as a label with key "Sandbox" and value extracted from the URL.
utub
about.labels
,
about.resource.attribute.labels
Added as a label with key "user_total_usage_bytes".
userid
target.user.userid
Extracted from the URL.
Need more help?
Get answers from Community members and Google SecOps professionals.
