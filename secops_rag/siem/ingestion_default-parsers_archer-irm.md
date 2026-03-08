# Collect Archer IRM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/archer-irm/  
**Scraped:** 2026-03-05T09:19:03.595579Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Archer IRM logs
Supported in:
Google secops
SIEM
This document explains how to ingest Archer IRM (Integrated Risk Management)
logs to Google Security Operations using Bindplane. The parser first attempts to
structure the SYSLOG data using a specific Grok pattern. If the pattern doesn't
match, it assumes a key-value format, extracts fields, and maps them to the
Unified Data Model (UDM), handling different event types and database resource
information along the way.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Archer IRM 6.x
on-premises instance with the
Audit Logging
feature licensed
Administrative access to the
Archer Control Panel
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
directory on Linux or in the installation directory
on Windows.
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:6514"
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
'ARCHER_IRM'
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
tcplog
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
Configure Syslog for Archer IRM Audit Logging
Open the
Archer Control Panel
on the application server.
Go to
Instance Management
>
All Instances
and double-click the target instance.
On the
General
tab, find the
Audit
section and select the
Enable Audit Logging for this instance
checkbox.
Provide the following configuration details:
HostName or IP Address
– Enter the Bindplane agent IP address.
Port
– Enter the Bindplane agent port number (for example,
6514
).
IP Version
– Select
IPv4
.
IP Traffic Method
– Select
TCP
.
Click
Test Connection
(only available when TCP is selected) to verify connectivity.
Click
Save
.
UDM mapping table
Log Field
UDM Mapping
Logic
ArcherInstance
additional.fields.ArcherInstance.string_value
Extracted from the
ArcherInstance
field in the raw log message.
ArcherLog
This field is parsed and its data is mapped to other UDM fields.
ArcherVersion
additional.fields.ArcherVersion.string_value
Extracted from the
ArcherVersion
field in the raw log message.
InputParameter
additional.fields.InputParameter.string_value
Extracted from the
InputParameter
field in the raw log message.
LogSourceIdentifier
This field is parsed and its data is mapped to other UDM fields.
MethodName
additional.fields.MethodName.string_value
Extracted from the
MethodName
field in the raw log message.
OutputValues
additional.fields.OutputValue.string_value
Extracted from the
OutputValues
field in the raw log message.
Success
security_result.summary
The value is set to
Success:
concatenated with the value of the
Success
field in the raw log message.
UserId
principal.user.userid
Extracted from the
UserId
field in the raw log message.
UserName
principal.user.user_display_name
Extracted from the
UserName
field in the raw log message.
DB_DRIVER
target.resource.attribute.labels.db_driver.value
Extracted from the
DB_DRIVER
field in the raw log message.
DB_HOST
target.resource.attribute.labels.db_host.value
Extracted from the
DB_HOST
field in the raw log message.
DB_NAME
target.resource.attribute.labels.db_name.value
Extracted from the
DB_NAME
field in the raw log message.
DB_PORT
target.resource.attribute.labels.db_port.value
Extracted from the
DB_PORT
field in the raw log message.
DB_URL
target.resource.attribute.labels.db_url.value
Extracted from the
DB_URL
field in the raw log message.
company_security_event_id
metadata.product_log_id
Extracted from the
company_security_event_id
field in the raw log message.
create_date
metadata.event_timestamp
Converted to timestamp from UNIX_MS format.
databasename
target.resource.attribute.labels.db_name.value
Extracted from the
databasename
field in the raw log message if
DB_NAME
is not present.
encrypt
security_result.detection_fields.encrypt.value
Extracted from the
encrypt
field in the raw log message.
eventid
metadata.product_event_type
Extracted from the
eventid
field in the raw log message.
eventtime
metadata.event_timestamp
Converted to timestamp from various formats.
integratedSecurity
security_result.detection_fields.integratedSecurity.value
Extracted from the
integratedSecurity
field in the raw log message.
N/A
extensions.auth.type
Set to
AUTHTYPE_UNSPECIFIED
for USER_LOGIN and USER_LOGOUT events.
N/A
metadata.event_type
Set to
USER_RESOURCE_ACCESS
if the log is parsed by the grok pattern. Set to
USER_LOGIN
if
security_event_name
is
User Login
. Set to
USER_LOGOUT
if
security_event_name
is
User Logout
. Set to
USER_RESOURCE_ACCESS
if
security_event_name
contains
Security Events
. Otherwise set to
GENERIC_EVENT
.
N/A
metadata.log_type
Set to
ARCHER_IRM
.
N/A
metadata.product_name
Set to
Archer
if the log is parsed by the grok pattern. Otherwise set to
RSA
.
N/A
metadata.vendor_name
Set to
RSA
if the log is parsed by the grok pattern. Otherwise set to
Archer
.
N/A
principal.ip
Set to
1.2.3.4
if the log is parsed by the grok pattern.
N/A
principal.port
Set to the value extracted from
LogSourceIdentifier
if the log is parsed by the grok pattern.
N/A
security_result.action
Set to
ALLOW
if
Success
is
True
, otherwise set to
BLOCK
.
N/A
target.resource.resource_type
Set to
DATABASE
if any database-related fields are present.
source_user
principal.user.userid
Extracted from the
source_user
field in the raw log message.
target_user
target.user.userid
Extracted from the
target_user
field in the raw log message.
trustServerCertificate
security_result.detection_fields.trustServerCertificate.value
Extracted from the
trustServerCertificate
field in the raw log message.
version
metadata.product_version
Extracted from the
version
field in the raw log message.
Need more help?
Get answers from Community members and Google SecOps professionals.
