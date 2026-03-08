# Collect FireEye HX logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx/  
**Scraped:** 2026-03-05T09:24:25.107589Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FireEye HX logs
Supported in:
Google secops
SIEM
This document explains how to collect FireEye Endpoint Security (HX) logs to Google Security Operations by using Bindplane. The parser attempts to process the input message as JSON. If the message is not in JSON format, it uses grok patterns to extract fields and then performs conditional UDM mapping based on the extracted event type and other criteria.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to FireEye Endpoint Security.
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
'<customer_id>'
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
ingestion_labels
:
log_type
:
'FIREEYE_HX'
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
Configure FireEye HX Event Streamer syslog using the UI
Sign in to the FireEye HX management console.
Go to
Event Streamer
.
Select
Enable Event Streamer on the host
.
Save the policy changes.
Go to
Destinations
>
Server settings
>
Add syslog destination
.
Provide the following configuration details:
Name
: enter a unique name to label the Google SecOps log collector.
IP address
: enter the Bindplane agent IP address.
Port
: enter the Bindplane agent port number.
Save the changes to apply.
Configure FireEye HX Event Streamer syslog using CLI
Sign in to the
FireEye HX
appliance using the command line interface (CLI).
Run the following command to enable configuration mode:
enable
configure terminal
Run the following command to add a remote syslog server destination:
logging
BINDPLANE_IP_ADDRESS
port
PORT_NUMBER
port
Replace the following:
BINDPLANE_IP_ADDRESS
: the Google SecOps forwarder IP address
PORT_NUMBER
: the port number
Run the following command to save the configuration details:
write mem
UDM Mapping Table
Log Field
UDM Mapping
Logic
alert.agent._id
principal.asset.asset_id
The agent ID from the raw log, prefixed with
AGENT ID:
alert.agent.url
principal.labels.value
The agent URL from the raw log.
alert.condition._id
additional.fields.value.string_value
The condition ID from the raw log, with
=
characters removed.
alert.condition.url
additional.fields.value.string_value
The condition URL from the raw log, with
=
characters removed.
alert.decorators[].data.fireeye_report.indicator_verdict.malware_families.0
security_result.threat_name
The malware family from the FireEye report in the decorators field of the raw log.
alert.decorators[].data.fireeye_report.risk_summary
security_result.description
The risk summary from the FireEye report in the decorators field of the raw log.
alert.decorators[].data.fireeye_verdict
security_result.severity_details
The FireEye verdict from the decorators field of the raw log.
alert.event_at
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_id
read_only_udm.metadata.product_log_id
The event ID from the raw log.
alert.event_type
read_only_udm.metadata.product_event_type
The event type from the raw log.
alert.event_values.fileWriteEvent/fullPath
target.file.full_path
The full path of the file written from the raw log.
alert.event_values.fileWriteEvent/md5
target.file.md5
The MD5 hash of the file written from the raw log.
alert.event_values.fileWriteEvent/pid
principal.process.pid
The process ID that wrote the file from the raw log.
alert.event_values.fileWriteEvent/processPath
principal.process.file.full_path
The path of the process that wrote the file from the raw log. Combined with alert.event_values.fileWriteEvent/process to create the full path if the OS is Windows.
alert.event_values.fileWriteEvent/size
target.file.size
The size of the file written from the raw log.
alert.event_values.fileWriteEvent/username
principal.user.userid
The user that wrote the file from the raw log.
alert.event_values.ipv4NetworkEvent/localIP
principal.ip
The local IP address from the raw log.
alert.event_values.ipv4NetworkEvent/localPort
principal.port
The local port from the raw log.
alert.event_values.ipv4NetworkEvent/pid
principal.process.pid
The process ID from the raw log.
alert.event_values.ipv4NetworkEvent/process
principal.process.file.full_path
The process name from the raw log. Combined with alert.event_values.ipv4NetworkEvent/processPath to create the full path if the OS is Windows.
alert.event_values.ipv4NetworkEvent/processPath
principal.process.file.full_path
The process path from the raw log. Combined with alert.event_values.ipv4NetworkEvent/process to create the full path if the OS is Windows.
alert.event_values.ipv4NetworkEvent/protocol
network.ip_protocol
The network protocol from the raw log.
alert.event_values.ipv4NetworkEvent/remoteIP
target.ip
The remote IP address from the raw log.
alert.event_values.ipv4NetworkEvent/remotePort
target.port
The remote port from the raw log.
alert.event_values.ipv4NetworkEvent/timestamp
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_values.ipv4NetworkEvent/username
principal.user.userid
The user from the raw log.
alert.event_values.processEvent/md5
target.process.file.md5
The MD5 hash of the process from the raw log.
alert.event_values.processEvent/parentPid
principal.process.pid
The parent process ID from the raw log.
alert.event_values.processEvent/parentProcess
principal.process.file.full_path
The parent process name from the raw log.
alert.event_values.processEvent/parentProcessPath
principal.process.file.full_path
The parent process path from the raw log.
alert.event_values.processEvent/pid
target.process.pid
The process ID from the raw log.
alert.event_values.processEvent/process
target.process.file.full_path
The process name from the raw log.
alert.event_values.processEvent/processCmdLine
target.process.command_line
The process command line from the raw log.
alert.event_values.processEvent/processPath
target.process.file.full_path
The process path from the raw log.
alert.event_values.processEvent/timestamp
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_values.processEvent/username
principal.user.userid
The user from the raw log.
alert.event_values.urlMonitorEvent/hostname
target.hostname
The hostname from the raw log.
alert.event_values.urlMonitorEvent/localPort
principal.port
The local port from the raw log.
alert.event_values.urlMonitorEvent/pid
principal.process.pid
The process ID from the raw log.
alert.event_values.urlMonitorEvent/process
principal.process.file.full_path
The process name from the raw log. Combined with alert.event_values.urlMonitorEvent/processPath to create the full path if the OS is Windows.
alert.event_values.urlMonitorEvent/processPath
principal.process.file.full_path
The process path from the raw log. Combined with alert.event_values.urlMonitorEvent/process to create the full path if the OS is Windows.
alert.event_values.urlMonitorEvent/remoteIpAddress
target.ip
The remote IP address from the raw log.
alert.event_values.urlMonitorEvent/remotePort
target.port
The remote port from the raw log.
alert.event_values.urlMonitorEvent/requestUrl
target.url
The requested URL from the raw log.
alert.event_values.urlMonitorEvent/timestamp
read_only_udm.metadata.event_timestamp
The event timestamp from the raw log.
alert.event_values.urlMonitorEvent/urlMethod
network.http.method
The HTTP method from the raw log.
alert.event_values.urlMonitorEvent/userAgent
network.http.user_agent
The user agent from the raw log.
alert.event_values.urlMonitorEvent/username
principal.user.userid
The user from the raw log.
alert.indicator._id
security_result.about.labels.value
The indicator ID from the raw log.
alert.indicator.name
read_only_udm.security_result.summary
The indicator name from the raw log.
alert.indicator.url
security_result.about.labels.value
The indicator URL from the raw log.
alert.multiple_match
read_only_udm.metadata.description
The multiple match message from the raw log.
alert.source
additional.fields.value.string_value
The source of the alert from the raw log.
authmethod
extensions.auth.mechanism
The authentication method from the raw log. Set to
LOCAL
if the value is
local
or
LOCAL
, otherwise set to
MECHANISM_OTHER
.
authsubmethod
extensions.auth.auth_details
The authentication submethod from the raw log, converted to uppercase.
client
principal.ip
The client IP address from the raw log.
conditions.data.tests[].token
security_result.detection_fields.key
The token from the conditions tests in the raw log.
conditions.data.tests[].value
security_result.detection_fields.value
The value from the conditions tests in the raw log.
description
read_only_udm.metadata.description
The description from the raw log.
host.agent_version
read_only_udm.metadata.product_version
The agent version from the raw log.
host.containment_state
read_only_udm.principal.containment_state
The containment state from the raw log.
host.domain
read_only_udm.principal.administrative_domain
The domain from the raw log.
host.hostname
read_only_udm.principal.hostname
The hostname from the raw log.
host.os.platform
read_only_udm.principal.platform
The operating system platform from the raw log.
host.os.product_name
read_only_udm.principal.platform_version
The operating system product name from the raw log.
host.primary_ip_address
read_only_udm.principal.ip
The primary IP address from the raw log.
host.primary_mac
read_only_udm.principal.mac
The primary MAC address from the raw log, with
-
characters replaced with
:
.
host_
principal.hostname
The hostname from the raw log.
host_details.data.agent_version
read_only_udm.metadata.product_version
The agent version from the raw log.
host_details.data.containment_state
read_only_udm.security_result.severity_details
The containment state from the raw log.
host_details.data.domain
read_only_udm.principal.administrative_domain
The domain from the raw log.
host_details.data.hostname
read_only_udm.principal.hostname
The hostname from the raw log.
host_details.data.os.platform
read_only_udm.principal.platform
The operating system platform from the raw log.
host_details.data.os.product_name
read_only_udm.principal.platform_version
The operating system product name from the raw log.
host_details.data.primary_ip_address
read_only_udm.principal.ip
The primary IP address from the raw log.
host_details.data.primary_mac
read_only_udm.principal.mac
The primary MAC address from the raw log, with
-
characters replaced with
:
.
indicators.data.description
read_only_udm.metadata.description
The indicator description from the raw log.
line
target.application
The line from the raw log.
localusername
target.user.user_display_name
The local username from the raw log.
principal_ip
principal.ip
The principal IP address from the raw log.
process
read_only_udm.principal.application
The process name from the raw log.
process_id
read_only_udm.principal.process.pid
The process ID from the raw log.
referrer
network.http.referral_url
The referrer URL from the raw log.
remoteaddress
principal.ip
The remote address from the raw log.
request
additional.fields.value.string_value
The request from the raw log.
role
target.user.role_name
The role from the raw log.
server
target.resource.attribute.labels.value
The server from the raw log.
sessionID
network.session_id
The session ID from the raw log.
severity
security_result.severity
Set to
LOW
,
MEDIUM
, or
HIGH
based on the severity from the raw log.
target_host
read_only_udm.target.hostname
The target hostname from the raw log.
target_ip
target.ip
The target IP address from the raw log.
target_ip1
target.ip
The target IPv6 address from the raw log.
timestamp
timestamp
The timestamp from the raw log.
upstream
target.url
The upstream URL from the raw log.
username
target.user.userid
The username from the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
