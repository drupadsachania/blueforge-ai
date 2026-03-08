# Collect HPE BladeSystem c7000 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000/  
**Scraped:** 2026-03-05T09:56:59.844525Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect HPE BladeSystem c7000 logs
Supported in:
Google secops
SIEM
This document explains how to ingest HPE BladeSystem C7000 logs to
Google Security Operations using Bindplane. The parser code extracts fields from
HPE BladeSystem c7000 syslog messages using regular expressions, then maps those
fields to a Unified Data Model (UDM) while enriching the data with additional
context like severity levels and descriptive labels. It handles various log
message structures, providing consistent representation for security monitoring
and analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to HPE Grid Manager
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
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
'HPE_BLADESYSTEM_C7000'
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
Configure Syslog directly in HPE BladeSystem
Sign in to the
BladeSystem
UI.
Go to
Configuration
>
System Log
.
Click
Log Options
tab.
Select the
Enable remote system logging
checkbox.
Provide the following configuration details:
Syslog Server Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (default port is
514
).
Protocol
: The protocol is always
UDP
.
Click
Test Remote Log
and verify logs are received.
Click
Apply
to save.
Configure Syslog in StorageGRID Software
You can configure both the audit message levels within StorageGRID and set up
external Syslog servers for forwarding these messages.
Configure StorageGRID Audit Message Levels
Sign in to the
GRID Manage
web UI.
Go to
Configuration
>
Monitoring
>
Audit and syslog server
.
For each category of audit message, select the
Normal
audit level from the list.
Click
Save
.
Configure StorageGRID External Syslog Server
From the
Audit and syslog server
page, click
Configure external syslog server
.
Provide the following configuration details:
Enter syslog info: Enter the Bindplane agent IP address.
Enter the Bindplane agent port number (default port is
514
).
Select the
UDP
or
TCP
protocol, depending on your Bindplane agent configuration.
Click
Continue
.
Configure Syslog Events
From the
Manage syslog content
step of the wizard, select each type of
audit information you want to send to the external syslog server.
Send audit logs
Send security events
Send application logs
Send access logs
For
Severity
, select
Passthrough
or
7
(Informational).
For
Facility
, select
Passthrough
.
Click
Continue
.
UDM mapping table
Log Field
UDM Mapping
Logic
command
principal.process.command_line
Directly mapped from the raw log field "command".
component
metadata.product_event_type
Directly mapped from the raw log field "component".
component_name
additional.fields[0].value.string_value
Directly mapped from the raw log field "component_name".
description
security_result.description
Directly mapped from the raw log field "description" after optional grok parsing.
description
security_result.detection_fields[0].value
Extracted from the "description" field using a grok pattern. Represents the current state.
description
security_result.detection_fields[1].value
Extracted from the "description" field using a grok pattern. Represents the previous state.
description
security_result.detection_fields[2].value
Extracted from the "description" field using a grok pattern. Represents the cause of the state change.
event_timestamp
metadata.event_timestamp
Directly mapped from the raw log field "event_timestamp" after date parsing.
hostname
principal.hostname
Directly mapped from the raw log field "hostname".
hostname
principal.asset.hostname
Copied from the mapped "principal.hostname" field.
internal_code
additional.fields[1].value.string_value
Directly mapped from the raw log field "internal_code".
priority_id
additional.fields[2].value.string_value
Directly mapped from the raw log field "priority_id".
additional.fields[0].key
Static value: "Component Name".
additional.fields[1].key
Static value: "Internal Code".
additional.fields[2].key
Static value: "Priority Id".
metadata.event_type
Set to "STATUS_UPDATE" if "principal.hostname" is successfully extracted, otherwise set to "GENERIC_EVENT".
metadata.vendor_name
Static value: "HP".
metadata.product_name
Static value: "HPE BladeSystem c7000".
metadata.log_type
Static value: "HPE_BLADESYSTEM_C7000".
security_result.severity
Mapped from the "severity" field based on the following logic:
- "Critical" -> "CRITICAL"
- "Major" -> "HIGH"
- "Warning" -> "MEDIUM"
- "Info", "Minor" -> "LOW"
- Default -> "UNKNOWN_SEVERITY"
security_result.detection_fields[0].key
Static value: "Current State".
security_result.detection_fields[1].key
Static value: "Previous State".
security_result.detection_fields[2].key
Static value: "Cause".
Need more help?
Get answers from Community members and Google SecOps professionals.
