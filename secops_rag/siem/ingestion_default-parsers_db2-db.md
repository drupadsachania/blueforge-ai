# Collect IBM DB2 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/db2-db/  
**Scraped:** 2026-03-05T09:25:24.654401Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect IBM DB2 logs
Supported in:
Google secops
SIEM
This document explains how to ingest IBM DB2 logs to Google Security Operations using Bindplane agent.
IBM Db2 is a relational database management system that provides an audit facility to assist in the detection of unknown or unanticipated access to data. The Db2 audit facility generates and permits the maintenance of an audit trail for a series of predefined database events.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between Bindplane agent and IBM DB2 instance
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
IBM DB2 instance (version 11.1 or later) with SYSADM privileges
Sufficient disk space for audit log storage and archival
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Click
Download
to download the
ingestion authentication file
.
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
/opt/observiq-otel-collector/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:1514"
exporters
:
chronicle/db2_audit
:
compression
:
gzip
creds_file_path
:
'/opt/observiq-otel-collector/ingestion-auth.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
DB2_DB
raw_log_field
:
body
ingestion_labels
:
env
:
production
service
:
pipelines
:
logs/db2_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/db2_audit
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:1514
to listen on all interfaces on port 1514 (non-privileged port recommended for Linux).
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/opt/observiq-otel-collector/ingestion-auth.json
Windows
:
C:\\Program Files\\observIQ OpenTelemetry Collector\\ingestion-auth.json
customer_id
: Customer ID from the previous step
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
: Set to
DB2_DB
ingestion_labels
: Optional labels in YAML format (for example,
env: production
)
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
Configure IBM DB2 audit facility
Configure the DB2 audit facility to capture security events and extract them to syslog.
Check current audit configuration
Connect to your DB2 instance as a user with SYSADM authority and run:
db2audit
describe
This displays the current audit configuration including audit status, categories, and paths.
Configure audit paths
Set the directories where audit logs will be stored:
db2audit
configure
datapath
/db2audit/data
db2audit
configure
archivepath
/db2audit/archive
Ensure these directories exist and have appropriate permissions for the DB2 instance owner:
mkdir
-p
/db2audit/data
/db2audit/archive
chown
db2inst1:db2iadm1
/db2audit/data
/db2audit/archive
chmod
750
/db2audit/data
/db2audit/archive
Configure audit scope and categories
Configure the audit facility to capture all security events:
db2audit
configure
scope
all
status
both
errortype
normal
This configures:
scope all
: Audits all categories (audit, checking, objmaint, secmaint, sysadmin, validate, context)
status both
: Captures both successful and failed events
errortype normal
: Standard error handling
Start the audit facility
Start auditing:
db2audit
start
Verify auditing is active:
db2audit
describe
The output should show
Audit active: "TRUE"
.
Configure syslog to receive DB2 audit logs
Configure the system syslog daemon to receive and store DB2 audit messages.
Linux (rsyslog)
Edit the rsyslog configuration file:
sudo
nano
/etc/rsyslog.conf
Add the following line to route DB2 audit messages to a dedicated file:
user
.
info
/
var
/
log
/
db2
/
db2audit
.
log
Create the log directory and file:
sudo
mkdir
-p
/var/log/db2
sudo
touch
/var/log/db2/db2audit.log
sudo
chmod
640
/var/log/db2/db2audit.log
Restart rsyslog:
sudo
systemctl
restart
rsyslog
AIX (syslogd)
Edit the syslog configuration file:
sudo
vi
/etc/syslog.conf
Add the following line:
user
.
info
/
var
/
log
/
db2
/
db2audit
.
log
Create the log directory and file:
sudo
mkdir
-p
/var/log/db2
sudo
touch
/var/log/db2/db2audit.log
sudo
chmod
640
/var/log/db2/db2audit.log
Restart syslogd:
sudo
refresh
-s
syslogd
Extract DB2 audit logs to syslog
Extract archived audit logs and send them to the system syslog daemon.
Flush and archive audit logs
Before extraction, flush any pending audit records and archive the current audit log:
db2audit
flush
db2audit
archive
The archive command creates timestamped files in the archive path (for example,
db2audit.instance.log.0.20250110123456
).
Extract audit logs to syslog
Extract the archived audit logs and send them to syslog using the
user.info
facility and priority:
db2audit
extract
syslog
user.info
from
files
/db2audit/archive/db2audit.instance.log.0.*
This command:
Extracts audit records from the archived log files
Sends them to the system syslog daemon with facility
user
and priority
info
The syslog daemon routes the messages according to
/etc/syslog.conf
or
/etc/rsyslog.conf
Verify logs are being sent
Check that audit messages are being written to the syslog file:
tail
-f
/var/log/db2/db2audit.log
You should see DB2 audit records appearing in the log file.
Configure rsyslog to forward logs to Bindplane agent
Configure rsyslog to forward DB2 audit logs to the Bindplane agent.
Create a new rsyslog configuration file:
sudo
nano
/etc/rsyslog.d/50-db2-forward.conf
Add the following configuration to forward logs to the Bindplane agent:
# Forward DB2 audit logs to Bindplane agent
user
.
info
@
@127.0.0.1
:
1514
The
@@
prefix indicates TCP forwarding. Use
@
for UDP if needed.
Restart rsyslog:
sudo
systemctl
restart
rsyslog
Automate audit log extraction
Create a script to automate the flush, archive, and extract process.
Create extraction script
Create a script to automate audit log extraction:
sudo
nano
/usr/local/bin/db2audit-extract.sh
Add the following content:
#!/bin/bash
# DB2 Audit Log Extraction Script
# Set DB2 environment
export
DB2INSTANCE
=
db2inst1
.
/home/db2inst1/sqllib/db2profile
# Flush pending audit records
db2audit
flush
# Archive current audit log
db2audit
archive
# Extract archived logs to syslog
db2audit
extract
syslog
user.info
from
files
/db2audit/archive/db2audit.instance.log.0.*
# Optional: Clean up old archived logs (older than 30 days)
find
/db2audit/archive
-name
"db2audit.instance.log.0.*"
-mtime
+30
-delete
exit
0
Make the script executable:
sudo
chmod
+x
/usr/local/bin/db2audit-extract.sh
Schedule with cron
Schedule the script to run periodically using cron:
sudo
crontab
-e
Add the following line to run the script every hour:
Choose one of the following options:
0
*
*
*
*
/
usr
/
local
/
bin
/
db2audit
-
extract
.
sh
>>
/
var
/
log
/
db2
/
db2audit
-
extract
.
log
2>&1
Or run every 15 minutes for more frequent extraction:
*/
15
*
*
*
*
/
usr
/
local
/
bin
/
db2audit
-
extract
.
sh
>>
/
var
/
log
/
db2
/
db2audit
-
extract
.
log
2>&1
Verify log ingestion in Google SecOps
Sign in to the Google SecOps console.
Go to
Search
.
Run a search query to verify DB2 logs are being ingested:
metadata
.
log_type
=
"DB2_DB"
Verify that logs appear with the correct timestamp and fields.
UDM mapping table
Log Field
UDM Mapping
Logic
msg
event.idm.read_only_udm.additional.fields
Value taken from msg if msg != ""
System
event.idm.read_only_udm.additional.fields
Value taken from System if System != ""
Subsystem
event.idm.read_only_udm.additional.fields
Value taken from Subsystem if Subsystem != ""
auth_mechanism
event.idm.read_only_udm.extensions.auth.mechanism
Set to "USERNAME_PASSWORD" for USER_LOGIN events
CorrelationUser
event.idm.read_only_udm.intermediary.user.userid
Value taken from CorrelationUser if CorrelationUser != ""
sum
event.idm.read_only_udm.metadata.description
Value taken from sum
date_time
event.idm.read_only_udm.metadata.event_timestamp
Converted from date and time fields to ISO8601 format if both != ""
leef_event_id
event.idm.read_only_udm.metadata.product_event_type
Value taken from leef_event_id
event.idm.read_only_udm.metadata.event_type
Derived from leef_event_id: if in ["102-87", "102-83"] → USER_LOGIN; if in ["102-6", "102-7", "102-8", "102-10", "102-24", "102-143"] → USER_RESOURCE_ACCESS or USER_RESOURCE_UPDATE_CONTENT based on intent; if "102-319" → USER_RESOURCE_ACCESS; else GENERIC_EVENT
event.idm.read_only_udm.metadata.product_name
Set to "DB2"
event.idm.read_only_udm.metadata.vendor_name
Set to "IBM"
SSID
event.idm.read_only_udm.network.session_id
Value taken from SSID if SSID != ""
job
event.idm.read_only_udm.principal.application
Value taken from job if job != ""
sourceServiceName
event.idm.read_only_udm.principal.application
Value taken from sourceServiceName
sourceHostName
event.idm.read_only_udm.principal.asset.hostname
Value taken from sourceHostName if sourceHostName != ""
principal_ip
event.idm.read_only_udm.principal.asset.ip
Value taken from principal_ip for 102-319 events
product_id
event.idm.read_only_udm.principal.asset_id
Set to "Product ID: %{product_id}" for 102-319 events
sourceHostName
event.idm.read_only_udm.principal.hostname
Value taken from sourceHostName if sourceHostName != ""
principal_ip
event.idm.read_only_udm.principal.ip
Value taken from principal_ip for 102-319 events
Creator
event.idm.read_only_udm.principal.user.user_display_name
Value taken from Creator
name
event.idm.read_only_udm.principal.user.user_display_name
Value taken from name if name != ""
AuthenticatedUser
event.idm.read_only_udm.principal.user.userid
Value taken from AuthenticatedUser if AuthenticatedUser != ""
sourceUserName
event.idm.read_only_udm.principal.user.userid
Value taken from sourceUserName
usrName
event.idm.read_only_udm.principal.user.userid
Value taken from usrName
_action
event.idm.read_only_udm.security_result.action
Derived from sum: if contains "successful" → ALLOW; else BLOCK for USER_LOGIN events
deviceHostName
event.idm.read_only_udm.target.asset.hostname
Value taken from deviceHostName
conn_location3
event.idm.read_only_udm.target.asset.hostname
Value taken from conn_location3 if conn_location3 != ""
file_name
event.idm.read_only_udm.target.file.full_path
Value taken from file_name if file_name != ""
deviceHostName
event.idm.read_only_udm.target.hostname
Value taken from deviceHostName
conn_location3
event.idm.read_only_udm.target.hostname
Value taken from conn_location3 if conn_location3 != ""
conn_location, conn_location2
event.idm.read_only_udm.target.location.name
Concatenated from conn_location and conn_location2 if both != ""
deviceProcessName
event.idm.read_only_udm.target.process.command_line
Value taken from deviceProcessName
SQL
event.idm.read_only_udm.target.process.command_line
Value taken from SQL if SQL != ""
Connection_Type
event.idm.read_only_udm.target.resource.attribute.labels
Key "Connection Type" with value from Connection_Type
Plan
event.idm.read_only_udm.target.resource.attribute.labels
Key "Plan" with value from Plan
DB2_Subsystem
event.idm.read_only_udm.target.resource.attribute.labels
Key "DB2 Subsystem" with value from DB2_Subsystem
Priv_Check_Code
event.idm.read_only_udm.target.resource.attribute.labels
Key "Priv Check Code" with value from Priv_Check_Code
Table_Name
event.idm.read_only_udm.target.resource.attribute.labels
Key "Table Name" with value from Table_Name
MessageType
event.idm.read_only_udm.target.resource.attribute.labels
Key "Message Type" with value from MessageType
Check_type
event.idm.read_only_udm.target.resource.attribute.labels
Key "Check Type" with value from Check_type
deviceAction
event.idm.read_only_udm.target.resource.attribute.labels
Key "Device Action" with value mapped from deviceAction: G → GRANT, R → REVOKE
SSID
event.idm.read_only_udm.target.resource.attribute.labels
Key "SSID" with value from SSID if value != ""
SQL
event.idm.read_only_udm.target.resource.attribute.labels
Key "SQL Query" with value from SQL if SQL != ""
messageid
event.idm.read_only_udm.target.resource.id
Value taken from messageid
Object_Class_Code
event.idm.read_only_udm.target.resource.parent
Value taken from Object_Class_Code
obj
event.idm.read_only_udm.target.resource.name
Value taken from obj
resource_name
event.idm.read_only_udm.target.resource.name
Value taken from resource_name extracted from SQL if SQL != "" and not empty
Database_Name
event.idm.read_only_udm.target.resource.name
Value taken from Database_Name
objtyp
event.idm.read_only_udm.target.resource.resource_subtype
Value taken from objtyp (uppercased) if objtyp != ""
Type
event.idm.read_only_udm.target.resource.resource_subtype
Derived from Type: T → TABLE, V → VIEW, X → AUXILIARY TABLE
event.idm.read_only_udm.target.resource.resource_type
Set to "DATABASE"
Need more help?
Get answers from Community members and Google SecOps professionals.
