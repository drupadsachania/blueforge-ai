# Collect MYSQL logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mysql/  
**Scraped:** 2026-03-05T09:58:25.166269Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect MYSQL logs
Supported in:
Google secops
SIEM
This document explains how to ingest MYSQL logs to Google Security Operations using
Bindplane. The parser first extracts common fields from MySQL SYSLOG messages
using
grok
. Then, it uses conditional branching (
if
,
else if
) and regular
expression matching to identify specific event types within the log messages,
extracting and mapping relevant information into the Unified Data Model (UDM) schema.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to MySQL host
Installed MySQL DB and Rsyslog
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
Install the Bindlane agent
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
'MYSQL'
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
Configure Syslog in MySQL
Sign in to the
MySQL
host using SSH.
Connect to MySQL database:
mysql
-u
root
-p
Verify for the
server_audit.so
audit plugin:
show
variables
like
'plugin_dir'
;
If you don't find the plugin file inside your plugin's directory,
install
the plugin using the command:
install
plugin
server_audit
soname
'server_audit.so'
;
Confirm the plugin is
Installed
and
Enabled
:
show
plugins
;
Edit the file
/etc/my.cnf
using
vi
, enable the following and save file:
server_audit_events
=
'CONNECT,QUERY,TABLE'
server_audit_file_path
=
server_audit.log
server_audit_logging
=
ON
server_audit_output_type
=
SYSLOG
server_audit_syslog_facility
=
LOG_LOCAL6
Verify the audit variables with the following command:
show
global
variables
like
"server_audit%"
;
Verify auditing is enabled, with the following command:
Show
global
status
like
'server_audit%'
;
Edit the file
/etc/rsyslog.conf
using
vi
, to enable using UDP and save file:
*.*
@@<bindplane-agent-ip>:<bindplane-agent-port>
Replace
<bindplane-agent-ip>
and
<bindplane-agent-port>
with your Bindplane agent configuration.
Restart MySQL service and connect to MySQL database.
/etc/init.d/mysqld
restart
UDM mapping table
Log field
UDM mapping
Logic
action
read_only_udm.metadata.event_type
If the value is
Created
then FILE_CREATION, if the value is
Deleted
then FILE_DELETION, otherwise no change.
database
read_only_udm.target.resource.parent
db_hostname
read_only_udm.target.hostname
db_user
read_only_udm.target.user.userid
description
read_only_udm.security_result.description
error_details
This is a temporary variable, ignore it
error_level
read_only_udm.security_result.severity
If the value is
error
then ERROR, if the value is
warning
then MEDIUM, if the value is
note
then INFORMATIONAL, otherwise no change.
error_message
read_only_udm.security_result.summary
file_path
read_only_udm.target.file.full_path
file_size
read_only_udm.target.file.size
hostname
read_only_udm.principal.hostname
inner_message
read_only_udm.security_result.description
summary
read_only_udm.metadata.product_event_type
table
read_only_udm.target.resource.name
table_not_found
This is a temporary variable, ignore it
timestamp
read_only_udm.metadata.event_timestamp
read_only_udm.extensions.auth.type
Static value -
MACHINE
read_only_udm.metadata.event_type
Static value -
USER_LOGIN
,
GENERIC_EVENT
,
STATUS_UPDATE
,
FILE_CREATION
,
FILE_DELETION
read_only_udm.metadata.log_type
Static value -
MYSQL
read_only_udm.metadata.product_name
Static value -
MySQL
read_only_udm.metadata.vendor_name
Static value -
Oracle Corporation
read_only_udm.security_result.action
Static value -
BLOCK
read_only_udm.target.resource.resource_type
Static value -
DATABASE
,
TABLE
Need more help?
Get answers from Community members and Google SecOps professionals.
