# Collect CA LDAP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-ldap/  
**Scraped:** 2026-03-05T09:20:50.529242Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CA LDAP logs
Supported in:
Google secops
SIEM
This document explains how to ingest CA LDAP logs to Google Security Operations using Bindplane agent.
CA Directory (formerly Symantec Directory) is an LDAP v2/v3 compliant directory server based on X.500 standards. It provides enterprise-level directory services with comprehensive logging capabilities including alarm, trace, warn, query, summary, connection, diagnostic, update, and statistics logs for monitoring directory operations and security events.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and CA Directory server
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the CA Directory server (root or administrator)
CA Directory installed and configured with logging enabled
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
system where Bindplane is to be installed.
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
chronicle/ca_directory
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
CA_LDAP
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
ca_directory
service
:
pipelines
:
logs/ca_directory_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/ca_directory
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on UDP port 514
For Linux non-root installations, use port
1514
or higher
Ensure the port matches the port configured in rsyslog forwarding
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
: Replace
YOUR_CUSTOMER_ID
with your
customer ID
. For details, see
Get Google SecOps customer ID
.
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
log_type
: Set to
CA_LDAP
(Chronicle ingestion label for CA Directory)
ingestion_labels
: Optional labels for filtering and organization
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
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux:
Run the following command:
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
To restart the Bindplane agent in Windows:
Choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press Enter.
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
Configure CA LDAP syslog forwarding using rsyslog
This section describes how to configure rsyslog on the CA Directory server to forward logs to the Bindplane agent.
Identify CA Directory log file locations
CA Directory stores log files in the following locations:
Linux
:
/opt/CA/Directory/dxserver/logs/
Windows
:
C:\Program Files\CA\Directory\dxserver\logs\
The log files follow naming patterns based on the DSA name (for example,
democorp_alarm
,
democorp_warn
,
democorp_trace
).
Available log types
CA Directory generates the following log types:
Alarm log
: Critical events (always enabled)
Warn log
: Errors and warnings
Trace log
: Detailed operation tracing
Query log
: Detailed operation information with timestamps
Summary log
: Operation summaries
Connection log
: Connection and disconnection events
Diagnostic log
: Rejected operations
Statistics log
: Per-minute operational statistics
Update log
: Add, modify, rename, and delete operations
Time log
: Operation timing information
Configure rsyslog on Linux
Sign in to the CA Directory server as root or with sudo privileges.
Install rsyslog if not already installed:
sudo
yum
install
rsyslog
Or for Debian/Ubuntu:
sudo
apt-get
install
rsyslog
Create a new rsyslog configuration file for CA Directory:
sudo
nano
/etc/rsyslog.d/ca-directory.conf
Add the following configuration to forward CA Directory logs:
# Load the imfile module for file monitoring
module(load="imfile" PollingInterval="10")

# Monitor CA Directory alarm logs
input(type="imfile"
    File="/opt/CA/Directory/dxserver/logs/*_alarm*"
    Tag="ca-directory-alarm"
    Severity="error"
    Facility="local0")

# Monitor CA Directory warn logs
input(type="imfile"
    File="/opt/CA/Directory/dxserver/logs/*_warn*"
    Tag="ca-directory-warn"
    Severity="warning"
    Facility="local0")

# Monitor CA Directory trace logs
input(type="imfile"
    File="/opt/CA/Directory/dxserver/logs/*_trace*"
    Tag="ca-directory-trace"
    Severity="info"
    Facility="local0")

# Monitor CA Directory query logs
input(type="imfile"
    File="/opt/CA/Directory/dxserver/logs/*_query*"
    Tag="ca-directory-query"
    Severity="info"
    Facility="local0")

# Monitor CA Directory connection logs
input(type="imfile"
    File="/opt/CA/Directory/dxserver/logs/*_connection*"
    Tag="ca-directory-connection"
    Severity="info"
    Facility="local0")

# Monitor CA Directory update logs
input(type="imfile"
    File="/opt/CA/Directory/dxserver/logs/*_update*"
    Tag="ca-directory-update"
    Severity="info"
    Facility="local0")

# Forward all CA Directory logs to Bindplane agent
if $syslogtag contains 'ca-directory' then @@BINDPLANE_AGENT_IP:514
& stop
Replace
BINDPLANE_AGENT_IP
with the IP address of the Bindplane agent host:
If Bindplane agent is on the same server:
127.0.0.1
If Bindplane agent is on a different server: Enter the IP address (for example,
192.168.1.100
)
Save the configuration file:
Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Verify the rsyslog configuration syntax:
sudo
rsyslogd
-N1
Restart the rsyslog service:
sudo
systemctl
restart
rsyslog
Verify rsyslog is running:
sudo
systemctl
status
rsyslog
Check rsyslog logs for errors:
sudo
tail
-f
/var/log/messages
Configure rsyslog on Windows
Download and install rsyslog for Windows from the
rsyslog website
.
Open the rsyslog configuration file:
notepad "C:\Program Files\rsyslog\rsyslog.conf"
Add the following configuration:
# Load the imfile module for file monitoring
module(load="imfile" PollingInterval="10")

# Monitor CA Directory alarm logs
input(type="imfile"
    File="C:\\Program Files\\CA\\Directory\\dxserver\\logs\\*_alarm*"
    Tag="ca-directory-alarm"
    Severity="error"
    Facility="local0")

# Monitor CA Directory warn logs
input(type="imfile"
    File="C:\\Program Files\\CA\\Directory\\dxserver\\logs\\*_warn*"
    Tag="ca-directory-warn"
    Severity="warning"
    Facility="local0")

# Monitor CA Directory trace logs
input(type="imfile"
    File="C:\\Program Files\\CA\\Directory\\dxserver\\logs\\*_trace*"
    Tag="ca-directory-trace"
    Severity="info"
    Facility="local0")

# Forward all CA Directory logs to Bindplane agent
if $syslogtag contains 'ca-directory' then @@BINDPLANE_AGENT_IP:514
& stop
Replace
BINDPLANE_AGENT_IP
with the IP address of the Bindplane agent host.
Save the configuration file.
Restart the rsyslog service:
net stop rsyslog
net start rsyslog
Enable CA Directory logging
Ensure that the required log types are enabled in CA Directory:
Edit the DSA configuration file:
Linux
:
/opt/CA/Directory/dxserver/config/servers/democorp.dxc
Windows
:
C:\Program Files\CA\Directory\dxserver\config\servers\democorp.dxc
Verify or add the following logging settings:
set alarm-log = true;
    set warn-log = true;
    set trace-log = true;
    set query-log = true;
    set connection-log = true;
    set update-log = true;
Save the configuration file.
Restart the CA Directory DSA:
Linux
:
dxserver
stop
democorp
dxserver
start
democorp
Windows
:
net stop "CA Directory DSA - democorp"
net start "CA Directory DSA - democorp"
Verify log forwarding
Generate test activity in CA Directory by performing LDAP queries or authentication attempts.
Check the Bindplane agent logs to verify logs are being received:
Linux
:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows
:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Sign in to the Google SecOps console and verify that CA Directory logs are appearing in the log viewer.
For more information about CA Directory logging, see the
Broadcom CA Directory documentation
.
For detailed rsyslog configuration examples, see the
Broadcom Knowledge Base article on centralized logging
.
UDM mapping table
Log Field
UDM Mapping
Logic
agent.ephemeral_id, logstash.irm_region, logstash.irm_environment, logstash.irm_site, host.os.name
additional.fields
Merged as labels with keys "ephemeral_id", "irm_region", "irm_environment", "irm_site", "os_name" respectively
host.architecture
hardware.cpu_platform
Value copied directly
logstash.process.host
intermediary.hostname
Value copied directly
logstash.collect.timestamp
metadata.collected_timestamp
Parsed as timestamp using date filter
msg
metadata.description
Value copied directly
metadata.event_type
Set to "STATUS_UPDATE"
agent.type, agent.version
observer.application
Concatenated as "%{agent.type} %{agent.version}" if both not empty, else "%{agent.type}"
agent.type, agent.id
observer.asset_id
Concatenated as "%{agent.type}: %{agent.id}"
agent.hostname
observer.hostname
Value copied directly
host.id
principal.asset.asset_id
Concatenated as "CA_LDAP:%{host.id}"
hardware
principal.asset.hardware
Merged from hardware object
host.hostname
principal.hostname
Value copied directly
host.ip
principal.ip
Merged from host.ip array
host.mac
principal.mac
Merged from host.mac array
host.os.family
principal.platform
Set to "LINUX" if matches "(rhel|redhat)"
host.os.kernel
principal.platform_patch_level
Value copied directly
host.os.version
principal.platform_version
Value copied directly
log.file.path
principal.process.file.full_path
Value copied directly
syslog_severity
security_result.severity
Set to "INFORMATIONAL" if matches "(?i)(DEFAULT|DEBUG|INFO|NOTICE)", "ERROR" if matches "(?i)ERROR", "MEDIUM" if matches "(?i)WARNING", "HIGH" if matches "(?i)(CRITICAL|ALERT|EMERGENCY)"
syslog_severity
security_result.severity_details
Value copied directly
metadata.product_name
Set to "CA_LDAP"
metadata.vendor_name
Set to "CA_LDAP"
Need more help?
Get answers from Community members and Google SecOps professionals.
