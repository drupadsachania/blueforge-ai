# Collect Fortinet FortiClient logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-forticlient/  
**Scraped:** 2026-03-05T09:24:46.484074Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiClient logs
Supported in:
Google secops
SIEM
This document explains how to ingest Fortinet FortiClient logs to Google Security Operations using Bindplane agent.
FortiClient is an endpoint security solution that provides antivirus, web filtering, VPN, vulnerability scanning, and application firewall capabilities for Windows, macOS, Linux, and Chromebook endpoints. FortiClient is centrally managed through FortiClient EMS (Endpoint Management Server), which pushes security policies and configuration profiles to endpoints.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with systemd
Network connectivity between Bindplane agent and FortiClient endpoints
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the FortiClient EMS management console
FortiClient EMS version 7.0 or later with licensed FortiClient endpoints
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Click
Download
to download the ingestion authentication file.
Save the file securely on the system where Bindplane agent will be installed.
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
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/forticlient
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'your-customer-id-here'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
FORTINET_FORTICLIENT
raw_log_field
:
body
ingestion_labels
:
env
:
production
source
:
forticlient
service
:
pipelines
:
logs/forticlient_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/forticlient
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on. Use
0.0.0.0:514
to listen on all interfaces on port 514.
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Customer ID from the Google SecOps console
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
:
FORTINET_FORTICLIENT
ingestion_labels
: Optional labels in YAML format
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart Bindplane agent to apply the changes
Linux
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows
Choose one of the following options:
Using Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Using Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure FortiClient endpoint logging to send logs to Bindplane agent
FortiClient endpoint logging is configured centrally through FortiClient EMS by editing endpoint profiles with XML configuration. EMS pushes the logging configuration to FortiClient endpoints, which then send logs directly to the Bindplane agent syslog listener.
Sign in to FortiClient EMS
Sign in to the FortiClient EMS web console.
Go to
Endpoint Profiles
>
Manage Profiles
.
Edit or create an endpoint profile
Select an existing profile to edit, or click
Add
to create a new profile.
In the
Profile Name
field, enter a descriptive name (for example,
Chronicle-Logging-Profile
).
Click
Advanced
.
Click the
XML Configuration
tab.
Click
Edit
.
Configure remote logging in XML
EMS displays two panes. Use the pane on the right to edit the XML configuration.
Locate the
<log_settings>
section within
<system>
. If it does not exist, add it. Within
<log_settings>
, locate or add the
<remote_logging>
section and configure it as follows:
<forticlient_configuration>
<system>
<log_settings>
<onnet_local_logging>1</onnet_local_logging>
<level>6</level>
<log_events>ipsecvpn,sslvpn,scheduler,update,firewall,av,proxy,shield,webfilter,endpoint,fssoma,configd,vuln,sandboxing,antiexploit</log_events>
<remote_logging>
<log_upload_enabled>1</log_upload_enabled>
<log_protocol>syslog</log_protocol>
<netlog_server>192.168.1.100</netlog_server>
<netlog_categories>7</netlog_categories>
<log_upload_freq_minutes>5</log_upload_freq_minutes>
</remote_logging>
</log_settings>
</system>
</forticlient_configuration>
Configuration parameters:
<log_upload_enabled>
: Set to
1
to enable remote logging.
<log_protocol>
: Set to
syslog
to send logs to a syslog server. Use
faz
to send logs to FortiAnalyzer instead.
<netlog_server>
: Enter the IP address of the Bindplane agent host (for example,
192.168.1.100
). This parameter is used only when
<log_protocol>
is set to
syslog
.
<netlog_categories>
: Enter the bitmask of log categories to upload:
1
= Traffic logs
2
= Vulnerability logs
4
= Event logs
7
= All categories (1 + 2 + 4)
<log_upload_freq_minutes>
: Enter the log upload frequency in minutes (for example,
5
for every 5 minutes).
<level>
: FortiClient logging level. Enter one of the following:
0
= Emergency
1
= Alert
2
= Critical
3
= Error
4
= Warning
5
= Notification
6
= Information (recommended)
7
= Debug
<log_events>
: Comma-separated list of FortiClient events or processes to log. Include the events you want to capture (for example,
ipsecvpn,sslvpn,firewall,av,webfilter,endpoint
).
Save the profile
Click
Test XML
to validate the XML configuration.
Click
Save
to save the profile.
Apply the profile to endpoints
Go to
Endpoint Policies
>
Manage Policies
.
Select an existing policy or click
Add
to create a new policy.
In the
Profile
dropdown, select the profile you created or edited.
In the
Endpoint Groups
section, select the endpoint groups to which you want to apply the policy.
Click
Save
.
EMS pushes the profile configuration to endpoints with the next Telemetry communication. FortiClient endpoints will begin sending logs to the Bindplane agent syslog listener.
Verify log forwarding
On the Bindplane agent host, check the agent logs to verify that logs are being received:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
On a FortiClient endpoint, verify that remote logging is enabled by checking the FortiClient logs:
Windows:
C:\Program Files\Fortinet\FortiClient\logs\
macOS:
/Library/Application Support/Fortinet/FortiClient/logs/
Linux:
/
var
/
log
/
forticlient
/
In the Google SecOps console, verify that FortiClient logs are being ingested:
Go to
Search
.
Enter a search query for FortiClient logs (for example,
metadata.log_type = "FORTINET_FORTICLIENT"
).
Verify that logs appear in the search results.
UDM mapping table
Log field
UDM mapping
Logic
emsserial, devid, usingpolicy, itime, fctsn, logver, site, fctver, browsetime, event_id, SubjectUserName, SubjectLogonId, ThreadID
additional.fields
Labels created with key and value from each field, merged into additional.fields
timestamp
metadata.collected_timestamp
Parsed as UNIX timestamp
ts
metadata.event_timestamp
Parsed with date filter using formats "MMM d HH:mm:ss", "MMM  d HH:mm:ss", "yyyy-MM-dd HH:mm:ss"
deviceip, client_ip, devicemac, hostname, user, uid
metadata.event_type
Set to USER_RESOURCE_ACCESS if user/uid present and machine id present; USER_UNCATEGORIZED if machine id present; GENERIC_EVENT otherwise
eventtype
metadata.product_event_type
Value copied directly
id
metadata.product_log_id
Converted to string, value copied
service
network.application_protocol
Uppercased, then set to predefined protocol if matches list (e.g., "SSH" for "22", "SSH", "SSHD"; "HTTP" for "80", "8080", "HTTP"), else to service if in extended list, else empty
direction
network.direction
Set to INBOUND if matches (?i)inbound; OUTBOUND if matches (?i)outbound
proto
network.ip_protocol
Set to "TCP" if proto == "6"
rcvdbyte
network.received_bytes
Converted to uinteger, value copied if not empty/0
sentbyte
network.sent_bytes
Converted to uinteger, value copied if not empty/0
sessionid
network.session_id
Value copied directly
pcdomain
principal.administrative_domain
Value copied directly
srcproduct
principal.application
Value copied directly
hostname
principal.hostname
Value copied directly
deviceip, client_ip
principal.ip
Value from deviceip if not empty, else from client_ip if valid IP
devicemac
principal.mac
Converted to MAC format, value copied if valid
os, source
principal.platform
Set to WINDOWS if os/source matches (?i)windows; MAC if matches (?i)mac|ios; LINUX if matches (?i)linux
source_ver
principal.platform_version
Value copied directly
srcport
principal.port
Converted to integer, value copied
ProcessId
principal.process.pid
Value copied directly
srcname, source_type, type
principal.resource.attribute.labels
Labels created with key and value from each field, merged into attribute.labels
devname
principal.resource.name
Value copied directly
ProviderGuid
principal.resource.product_object_id
Value copied directly
subtype
principal.resource.resource_subtype
Value copied directly
url
principal.url
Value copied directly
uid, fctuid
principal.user.product_object_id
Value from uid if not empty, else fctuid
user
principal.user.user_display_name
Value copied directly
user
principal.user.userid
Value copied directly
SubjectUserSid
principal.user.windows_sid
Value copied if matches SID regex
utmaction
security_result.action
Set to ALLOW if in [accept,allow,passthrough,pass,permit,detected]; BLOCK if in [deny,dropped,blocked,block]; UNKNOWN_ACTION otherwise
utmevent
security_result.category_details
Value copied directly
utmaction
security_result.description
Set to "utmaction:
"
userinitiated
security_result.detection_fields
Label created with key "userinitiated" and value from userinitiated, merged
level
security_result.severity
Set to INFORMATIONAL if level == "info"
threat
security_result.threat_name
Value copied directly
emshostname, remotename
target.hostname
Value from emshostname if not empty, else remotename
dstip
target.ip
Extracted valid IP from dstip
dstport
target.port
Converted to integer, value copied if not 0
metadata.product_name
Set to "FORTINET_FORTICLIENT"
metadata.vendor_name
Set to "FORTINET_FORTICLIENT"
Need more help?
Get answers from Community members and Google SecOps professionals.
