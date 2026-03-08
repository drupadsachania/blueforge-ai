# ANSIBLE_AWX

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ansible-awx/  
**Scraped:** 2026-03-05T09:18:51.925593Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
ANSIBLE_AWX
Supported in:
Google secops
SIEM
This document explains how to ingest Ansible AWX logs to Google Security Operations
using Bindplane. The parser extracts fields from JSON-formatted Ansible AWX logs.
It uses JSON parsing to extract log fields and then maps these values to the
Unified Data Model (UDM). It also sets default metadata values for the event
source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
A Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
Privileged access to the Ansible AWX management console or appliance with administrator permissions.
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
Install Bindplane agent
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
For additional installation options, see the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/opt/observiq-otel-collector/
directory on Linux or
C:Program FilesobservIQ OpenTelemetry Collector
directory on Windows.
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
# Using high port to avoid requiring root privileges
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/awx
:
endpoint
:
malachiteingestion-pa.googleapis.com
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
YOUR_CUSTOMER_ID
log_type
:
'ANSIBLE_AWX'
raw_log_field
:
body
service
:
pipelines
:
logs/awx
:
receivers
:
-
udplog
exporters
:
-
chronicle/awx
Replace the port and IP address as required in your infrastructure.
Replace
YOUR_CUSTOMER_ID
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the
authentication file was saved in Step 1.
Restart the Bindplane Agent to apply the changes
To restart the BindPlane agent in
Linux
, run the following command:
sudo
systemctl
restart
observiq-otel-collector
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
sc stop observiq-otel-collector && sc start observiq-otel-collector
Configure external logging on Ansible AWX
Sign in to the
Ansible AWX Management Console
.
Go to
Settings
from the navigation bar.
Select
Logging settings
from the
System
options.
Provide the following configuration details:
Logging Aggregator
: Enter the Bindplane agent IP address.
Logging Aggregator Port
: Enter the Bindplane agent port number (for example,
514
).
Logging Aggregator Type
: Select
Other
from the list.
Logging Aggregator Username
: Leave blank (not needed for syslog).
Logging Aggregator Password/Token
: Leave blank (not needed for syslog).
Logging Aggregator Protocol
: Select
UDP
(recommended for syslog).
Logging Aggregator Level Threshold
: Select
Info
or your preferred log level.
Enable External Logging
: Click the toggle
ON
.
Loggers to Send Data to the Log Aggregator
: Select the relevant log types:
awx
: Generic server logs
activity_stream
: Record of changes to AWX objects
job_events
: Ansible callback module data
system_tracking
: System facts and configuration data
Log System Tracking Facts Individually
: Toggle
OFF
(default).
Click
Save
to apply the settings.
Optional: Click
Test
to verify the connection to the Bindplane agent.
UDM mapping table
Log field
UDM mapping
Logic
agent.ephemeral_id
observer.labels.value
The value of
agent.ephemeral_id
from the raw log.
agent.hostname
observer.hostname
The value of
agent.hostname
from the raw log.
agent.id
observer.asset_id
Concatenation of "filebeat:" and the value of
agent.id
from the raw log.
agent.name
observer.user.userid
The value of
agent.name
from the raw log.
agent.type
observer.application
The value of
agent.type
from the raw log.
agent.version
observer.platform_version
The value of
agent.version
from the raw log.
cloud.availability_zone
principal.resource.attribute.labels.value
The value of
cloud.availability_zone
from the raw log.
cloud.instance.id
principal.resource.product_object_id
The value of
cloud.instance.id
from the raw log.
cloud.instance.name
principal.resource.name
The value of
cloud.instance.name
from the raw log.
cloud.machine.type
principal.resource.attribute.labels.value
The value of
cloud.machine.type
from the raw log.
cloud.provider
principal.resource.attribute.labels.value
The value of
cloud.provider
from the raw log.
event1
metadata.description
The value of
event1
from the raw log. If
event1
is not present, the value of
message
is used.
event1_data.host
principal.hostname
The value of
event1_data.host
from the raw log.
event1_data.remote_addr
principal.ip
The IP address extracted from
event1_data.remote_addr
using a grok pattern.
event1_data.task
security_result.detection_fields.value
The value of
event1_data.task
from the raw log.
event1_data.task_path
principal.process.file.full_path
The value of
event1_data.task_path
from the raw log.
event1_data.task_uuid
security_result.detection_fields.value
The value of
event1_data.task_uuid
from the raw log.
event1_data.uuid
metadata.product_log_id
The value of
event1_data.uuid
from the raw log.
event1_display
security_result.description
The value of
event1_display
from the raw log.
host
principal.hostname
The value of
host
from the raw log, used if
event1_data.host
and
host_name
are not present.
host.architecture
target.asset.hardware.cpu_platform
The value of
host.architecture
from the raw log.
host.fqdn
target.administrative_domain
The value of
host.fqdn
from the raw log.
host.hostname
target.hostname
The value of
host.hostname
from the raw log.
host.id
target.asset.asset_id
Concatenation of "Host Id: " and the value of
host.id
from the raw log.
host.ip
target.asset.ip
The values of
host.ip
from the raw log.
host.mac
target.mac
The values of
host.mac
from the raw log.
host.os.codename
target.asset.attribute.labels.value
The value of
host.os.codename
from the raw log.
host.os.kernel
target.platform_patch_level
The value of
host.os.kernel
from the raw log.
host.os.name
target.asset.attribute.labels.value
The value of
host.os.name
from the raw log.
host.os.platform
target.platform
Set to "LINUX" if
host.os.platform
is "debian".
host.os.version
target.platform_version
The value of
host.os.version
from the raw log.
host_name
principal.hostname
The value of
host_name
from the raw log, used if
event1_data.host
is not present.
input.type
network.ip_protocol
Set to "TCP" if
input.type
is "tcp".
level
security_result.severity
Mapped based on the value of
level
: "DEBUG", "INFO", "AUDIT" map to "INFORMATIONAL"; "ERROR" maps to "ERROR"; "WARNING" maps to "MEDIUM".
level
security_result.severity_details
The value of
level
from the raw log.
log.source.address
principal.ip
The IP address extracted from
log.source.address
using a grok pattern.
log.source.address
principal.port
The port extracted from
log.source.address
using a grok pattern.
logger_name
intermediary.application
The value of
logger_name
from the raw log.
message
metadata.description
The value of
message
from the raw log, used as a fallback if
event1
is not present.
parent_uuid
security_result.detection_fields.value
The value of
parent_uuid
from the raw log.
timestamp
metadata.event_timestamp
The value of
timestamp
from the raw log, parsed using date filter. Determined by logic: "NETWORK_CONNECTION" if
log.source.address
exists and
host.ip
exists in the JSON; "STATUS_UPDATE" if
principal_hostname
or
event1_data.remote_addr
exists; "GENERIC_EVENT" otherwise. Hardcoded to "ANSIBLE_AWX". Hardcoded to "ANSIBLE_AWX". Hardcoded to "ANSIBLE_AWX". Hardcoded to "ephemeral_id". Hardcoded to "machine_type", "provider", or "availability_zone" depending on the field being mapped. Hardcoded to "VIRTUAL_MACHINE". Hardcoded to "parent_uuid", "task", or "task_uuid" depending on the field being mapped. Hardcoded to "codename" or "os_name" depending on the field being mapped.
Need more help?
Get answers from Community members and Google SecOps professionals.
