# Collect Apache Tomcat logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat/  
**Scraped:** 2026-03-05T09:18:56.801152Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Apache Tomcat logs
Supported in:
Google secops
SIEM
This document explains how to ingest Apache Tomcat logs to
Google Security Operations using Bindplane. The parser extracts fields from
JSON-formatted logs, transforming them into the Unified Data Model (UDM).
It initializes default values, parses the JSON payload, handles potential
JSON parsing errors, and maps various fields from the raw log into 
corresponding UDM fields, including metadata, principal, observer, and security
result information, while also adding custom labels for environment context.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Apache Tomcat version 9.0.70 or later
Write access to
$CATALINA_BASE/conf
and
$CATALINA_BASE/logs
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
Install the Bindplane agent on the Tomcat server to collect log files
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
directory on Linux or in the installation
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
filelog/tomcat
:
include
:
[
/path/to/tomcat/logs/access-log.*.json
]
start_at
:
beginning
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
'TOMCAT'
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
filelog/tomcat
exporters
:
-
chronicle/chronicle_w_labels
Replace the
/path/to/tomcat/logs
.
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
Configure JSON Access Logs in Tomcat
Open the Tomcat file at
$CATALINA_BASE/conf/server.xml
.
Locate the
<Host>
tag and add this inside:
<Valve
className="org.apache.catalina.valves.JsonAccessLogValve"
directory="logs"
prefix="access-log"
suffix=".json"
rotatable="true"
maxDays="7"/>
Restart Tomcat to apply changes:
cd
/path/to/tomcat
bin/catalina.sh
stop
bin/catalina.sh
start
A new JSON log file will appear daily (for example,
logs/access-log.2025-07-02.json
).
UDM mapping table
Log Field
UDM Mapping
Logic
@timestamp
metadata.event_timestamp
The value of
@timestamp
from the raw log is directly mapped to this UDM field.  It represents the time the event occurred.
agent.ephemeral_id
additional.fields[ephemeral_id].value.string_value
The ephemeral ID from the agent is added as a key-value pair in the
additional
fields.
agent.hostname
observer.hostname
The agent's hostname is used as the observer hostname.
agent.id
observer.asset_id
The agent ID is combined with the agent type to create the observer asset ID (e.g.,
filebeat: <agent_id>
).
agent.type
observer.application
The agent type is used as the observer application.
agent.version
observer.platform_version
The agent version is used as the observer platform version.
host.hostname
principal.hostname
The host's hostname is used as the principal hostname.
host.id
principal.asset.asset_id
The host ID is prepended with
Host Id:
to create the principal asset ID.
host.ip
principal.ip
,
observer.ip
The host's IP address is used for both the principal and observer IP.  If multiple IPs are present, they are merged into an array.
host.mac
principal.mac
The host's MAC address is used as the principal MAC address. If multiple MACs are present, they are merged into an array.
host.os.family
principal.platform
If the host OS family is
rhel
or
redhat
, the principal platform is set to
LINUX
.
host.os.kernel
principal.platform_patch_level
The host OS kernel version is used as the principal platform patch level.
host.os.name
additional.fields[os_name].value.string_value
The host OS name is added as a key-value pair in the
additional
fields.
host.os.version
principal.platform_version
The host OS version is used as the principal platform version.
log.file.path
principal.process.file.full_path
The log path is used as the principal process file's full path.
log_level
security_result.severity
,
security_result.severity_details
,
security_result.action
The log level is used to determine the security result severity, severity details, and action.  DEBUG, INFO, and AUDIT map to INFORMATIONAL severity and ALLOW action. ERROR maps to ERROR severity and BLOCK action. WARNING and WARN map to MEDIUM severity and BLOCK action. The raw log_level value is also mapped to severity_details.
logstash.irm_environment
additional.fields[irm_environment].value.string_value
The Iron Mountain environment from Logstash is added as a key-value pair in the
additional
fields.
logstash.irm_region
additional.fields[irm_region].value.string_value
The Iron Mountain region from Logstash is added as a key-value pair in the
additional
fields.
logstash.irm_site
additional.fields[irm_site].value.string_value
The Iron Mountain site from Logstash is added as a key-value pair in the
additional
fields.
logstash.process.host
intermediary.hostname
The Logstash processing host is used as the intermediary hostname.
logstash.process.timestamp
metadata.collected_timestamp
The Logstash processing timestamp is used as the collected timestamp.
logstash.xyz_environment
additional.fields[xyz_environment].value.string_value
The xyz environment from Logstash is added as a key-value pair in the
additional
fields.
logstash.xyz_region
additional.fields[xyz_region].value.string_value
The xyz region from Logstash is added as a key-value pair in the
additional
fields.
logstash.xyz_site
additional.fields[xyz_site].value.string_value
The xyz site from Logstash is added as a key-value pair in the
additional
fields.
message
metadata.description
The message field is parsed as JSON and its
event_message
field is used as the metadata description. The intermediary application is hardcoded to
logstash
. The metadata event type is hardcoded to
USER_UNCATEGORIZED
. The metadata log type is set to
TOMCAT
from the raw log's batch.type or batch.log_type. The metadata product name is hardcoded to
Tomcat
. The metadata vendor name is hardcoded to
Tomcat
.
user
principal.user.userid
The user field from the raw log is used as the principal user ID.
Need more help?
Get answers from Community members and Google SecOps professionals.
