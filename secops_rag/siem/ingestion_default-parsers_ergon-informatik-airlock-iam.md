# Collect Ergon Informatik Airlock IAM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam/  
**Scraped:** 2026-03-05T09:23:49.033718Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Ergon Informatik Airlock IAM logs
Supported in:
Google secops
SIEM
This document explains how to ingest Ergon Informatik Airlock IAM logs into Google Security Operations using the Bindplane agent.
Airlock IAM is an identity and access management solution that provides authentication, authorization, and user self-service capabilities. It generates structured JSON logs for authentication events, user trail activities, audit logs, and administrative actions across its Loginapp, Adminapp, Transaction Approval, Service Container, and API Policy Service modules.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or a Linux host with
systemd
Network connectivity between the Bindplane agent and Airlock IAM server
If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
Administrative access to the Airlock IAM instance
SSH or console access to the Airlock IAM server to edit configuration files
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
The service status should be
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
The service status should be
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
chronicle/airlock_iam
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
ERGON_INFORMATIK_AIRLOCK_IAM
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
airlock_iam
service
:
pipelines
:
logs/airlock_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/airlock_iam
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on port 51. For Linux systems running as non-root, use port
1514
or higher.
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
YOUR_CUSTOMER_ID
: Replace with your Google SecOps customer ID from the previous step
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
ingestion_labels
: Optional labels to categorize logs (modify as needed)
Example configuration for Windows
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/airlock_iam
:
compression
:
gzip
creds_file_path
:
'C:\Program
Files\observIQ
OpenTelemetry
Collector\ingestion-auth.json'
customer_id
:
'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
ERGON_INFORMATIK_AIRLOCK_IAM
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
airlock_iam
service
:
pipelines
:
logs/airlock_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/airlock_iam
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
Configure Airlock IAM syslog forwarding
Connect to the Airlock IAM server using SSH or console access.
Navigate to the instance directory:
cd
/opt/airlock/iam/instances/<instance_name>/
Edit the Log4j configuration file for all modules:
nano
log4j/all-modules.xml
Add the Syslog appender configuration in the
<Appenders>
section:
<Syslog
name="SYSLOG"
facility="LOCAL1"
host="BINDPLANE_AGENT_IP"
port="514"
protocol="UDP"
format="RFC5424"
includeMDC="true"
mdcId="mdc"
newLine="true">
<ExceptionPattern>%ex{full}</ExceptionPattern>
<ThresholdFilter
level="INFO"/>
</Syslog>
Configure the Syslog appender parameters:
host
: Replace
BINDPLANE_AGENT_IP
with the IP address of the Bindplane agent host (for example,
192.168.1.100
)
port
: Set to
514
(or
1514
if Bindplane agent is configured for non-privileged port)
protocol
: Set to
UDP
(or
TCP
if you configured tcplog receiver in Bindplane)
format
: Set to
RFC5424
for structured syslog format
facility
: Set to
LOCAL1
(or another facility code as needed:
LOCAL0
through
LOCAL7
)
ThresholdFilter level
: Set to
INFO
to send INFO and higher severity logs, or
DEBUG
for all logs
Add the appender reference inside the
<Root>
logger section:
<Loggers>
<Root
level="${sys:iam.log.level}">
<AppenderRef
ref="SYSLOG"/>
</Root>
</Loggers>
Complete example configuration:
<?xml
version="1.0"
encoding="UTF-8"?>
<Configuration
name="Custom
Log4j
2
Configuration
for
All
IAM
Modules">
<Appenders>
<Syslog
name="SYSLOG"
facility="LOCAL1"
host="192.168.1.100"
port="514"
protocol="UDP"
format="RFC5424"
includeMDC="true"
mdcId="mdc"
newLine="true">
<ExceptionPattern>%ex{full}</ExceptionPattern>
<ThresholdFilter
level="INFO"/>
</Syslog>
</Appenders>
<Loggers>
<Root
level="${sys:iam.log.level}">
<AppenderRef
ref="SYSLOG"/>
</Root>
</Loggers>
</Configuration>
Save the configuration file:
Press
Ctrl+O
, then
Enter
, then
Ctrl+X
The Log4j configuration is monitored for changes every 60 seconds by default. The new syslog forwarding will activate automatically without requiring a restart.
Verify that logs are being sent to the Bindplane agent:
sudo
journalctl
-u
observiq-otel-collector
-f
Verify that logs are arriving in Google SecOps:
Sign in to the Google SecOps console.
Go to
SIEM
>
Search
.
Run a search query:
metadata.log_type = "ERGON_INFORMATIK_AIRLOCK_IAM"
Verify that Airlock IAM logs appear in the search results.
Additional configuration options
Configure TCP syslog instead of UDP
If you prefer TCP delivery instead of UDP:
In the Bindplane agent
config.yaml
file, change the receiver to
tcplog
:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:514"
In the Airlock IAM
log4j/all-modules.xml
file, change the protocol to
TCP
:
<Syslog
name="SYSLOG"
facility="LOCAL1"
host="192.168.1.100"
port="514"
protocol="TCP"
format="RFC5424"
includeMDC="true"
mdcId="mdc"
newLine="true">
<ExceptionPattern>%ex{full}</ExceptionPattern>
<ThresholdFilter
level="INFO"/>
</Syslog>
Restart the Bindplane agent to apply the receiver change.
Configure different log levels
To send only WARNING and higher severity logs:
<ThresholdFilter
level="WARN"/>
To send all logs including DEBUG:
<ThresholdFilter
level="DEBUG"/>
Available log levels, from lowest to highest severity:
TRACE
DEBUG
INFO
WARN
ERROR
FATAL
Configure multiple Airlock IAM instances
If you have multiple Airlock IAM instances sending to the same Bindplane agent, use ingestion labels to differentiate them:
exporters
:
chronicle/airlock_iam_prod
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
ERGON_INFORMATIK_AIRLOCK_IAM
raw_log_field
:
body
ingestion_labels
:
env
:
production
instance
:
prod-iam-01
chronicle/airlock_iam_dev
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
ERGON_INFORMATIK_AIRLOCK_IAM
raw_log_field
:
body
ingestion_labels
:
env
:
development
instance
:
dev-iam-01
service
:
pipelines
:
logs/airlock_prod
:
receivers
:
-
udplog
exporters
:
-
chronicle/airlock_iam_prod
logs/airlock_dev
:
receivers
:
-
udplog
exporters
:
-
chronicle/airlock_iam_dev
Troubleshooting
Logs not appearing in Google SecOps
Verify that the Bindplane agent is receiving logs:
sudo
journalctl
-u
observiq-otel-collector
-f
Check for network connectivity from Airlock IAM to the Bindplane agent:
telnet
BINDPLANE_AGENT_IP
514
Verify that the Log4j configuration is valid:
cat
/opt/airlock/iam/instances/<instance_name>/log4j/all-modules.xml
Check Airlock IAM logs for errors:
tail
-f
/opt/airlock/iam/instances/<instance_name>/logs/loginapp.log
Bindplane agent errors
Check Bindplane agent logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-n
100
Verify that the
config.yaml
syntax is correct. YAML is indentation-sensitive.
Verify that the ingestion authentication file path is correct and that the file exists.
Test network connectivity to the Google SecOps endpoint:
curl
-v
https://malachiteingestion-pa.googleapis.com
Firewall configuration
Ensure the following firewall rules are configured:
Inbound to Bindplane agent:
Protocol: UDP (or TCP if using tcplog)
Port: 514 (or your configured port)
Source: Airlock IAM server IP address
Outbound from Bindplane agent:
Protocol: HTTPS (TCP 443)
Destination: Google SecOps regional endpoint
Purpose: Log delivery to Google SecOps
UDM mapping table
Log Field
UDM Mapping
Logic
expire_time
additional.fields
Merged as label with key "expire_time" if not empty
mobile
additional.fields
Merged as label with key "mobile" if not empty
sn
additional.fields
Merged as label with key "sn" if not empty
CONFIG_CONTEXT
additional.fields
Merged as label with key "CONFIG_CONTEXT" if not empty
department
additional.fields
Merged as label with key "department" if not empty
ctxData
additional.fields
Merged as label with key "ctxData" if not empty
displayLanguage
additional.fields
Merged as label with key "displayLanguage" if not empty
nrPwdTrialsForUserDeletion
additional.fields
Merged as label with key "nrPwdTrialsForUserDeletion" if not empty
authInstant
additional.fields
Merged as label with key "authInstant" if not empty
auditToken
additional.fields
Merged as label with key "auditToken" if not empty
authPlugin
additional.fields
Merged as label with key "authPlugin" if not empty
latestIdPropagation
additional.fields
Merged as label with key "latestIdPropagation" if not empty
service
additional.fields
Merged as label with key "service" if not empty
ldap_type
additional.fields
Merged as label with key "ldap_type" if not empty
report_message
additional.fields
Merged as label with key "report_message" if not empty
authenteeProvidedId
additional.fields
Merged as label with key "authenteeProvidedId" if not empty
representerId
additional.fields
Merged as label with key "representerId" if not empty
engine
additional.fields
Merged as label with key "engine" if not empty
channel
additional.fields
Merged as label with key "channel" if not empty
authnFactor
additional.fields
Merged as label with key "authnFactor" if not empty
authnFactorDetail
additional.fields
Merged as label with key "authnFactorDetail" if not empty
required_roles
additional.fields
Merged as label with key "required_roles" if not empty
target_pattern
additional.fields
Merged as label with key "target_pattern" if not empty
nameid
additional.fields
Merged as label with key "nameid" if not empty
plugin_name
additional.fields
Merged as label with key "plugin_name" if not empty
mechanism
additional.fields
Merged as label with key "mechanism" if not empty
new_session_id
additional.fields
Merged as label with key "new_session_id" if not empty
former_session_id
additional.fields
Merged as label with key "former_session_id" if not empty
req_id
additional.fields
Merged as label with key "req_id" if not empty
auth_method
additional.fields
Merged as label with key "auth_method" if not empty
otp
additional.fields
Merged as label with key "otp" if not empty
mob_num
additional.fields
Merged as label with key "mob_num" if not empty
jsessionid
additional.fields
Merged as label with key "jsessionid" if not empty
creationDate
additional.fields
Merged as label with key "creationDate" if not empty
lastLogin
additional.fields
Merged as label with key "lastLogin" if not empty
accountStatus
additional.fields
Merged as label with key "accountStatus" if not empty
companyAdministrator
additional.fields
Merged as label with key "companyAdministrator" if not empty
companyCustomer
additional.fields
Merged as label with key "companyCustomer" if not empty
privateCustomer
additional.fields
Merged as label with key "privateCustomer" if not empty
otpNotifyChannel
additional.fields
Merged as label with key "otpNotifyChannel" if not empty
nas_identifier
additional.fields
Merged as label with key "nas_identifier" if not empty
session_id
additional.fields
Merged as label with key "session_id" if not empty
authPluginClassName
extensions.auth.auth_details
Value copied directly if present
authenticator_type
extensions.auth.auth_details
Value copied directly if present and authPluginClassName is empty
logon_type
extensions.auth.mechanism
Value copied directly
N/A
intermediary
Merged from intermediary object
FORWARD_LOCATION
intermediary.url
Value copied directly
metadata_description
metadata.description
Value copied directly
N/A
metadata.event_type
Set based on event context; determined by parser logic
REQUEST_ID
metadata.product_log_id
Value copied directly
airlock_version
metadata.product_version
Value copied directly
method
network.http.method
Value copied directly
user_agent
network.http.user_agent
Value copied directly
packet_size
network.received_packets
Value converted to integer
GSID
network.session_id
Value copied directly
host
principal.hostname
Value copied directly
CLIENT_IP
principal.ip
Value copied directly
UID
principal.user.userid
Value copied directly
role_name
role.name
Value copied directly
authenteeType
role.type
Value copied directly
N/A
security_result
Merged from security_result object
action
security_result.action_details
Value copied directly if present
authMethodShortDesc
security_result.action_details
Value merged if present
action_detail
security_result.action_details
Value merged if present
category_value
security_result.category
Value copied directly
actionGroup
security_result.category_details
Value copied directly
result_description
security_result.description
Value copied directly
exception
security_result.summary
Value copied directly if present
STATLOG
security_result.summary
Value copied directly if present and exception is empty
mob_num
src.asset.type
Value copied directly
mail
src.email
Value copied directly if present
email
src.email
Value copied directly if present and mail is empty
src_ip
src.ip
Value copied directly
src_port
src.port
Value converted to integer
role
src.user.attribute.roles
Value copied directly
company
src.user.company_name
Value copied directly
firstName
src.user.first_name
Value copied directly
lastName
src.user.last_name
Value copied directly
status
src.user.user_authentication_status
Value copied directly
displayName
src.user.user_display_name
Value copied directly if present
username
src.user.user_display_name
Value copied directly if present and displayName is empty
src_user
src.user.user_display_name
Value copied directly if present and displayName/username are empty
authenteeId
src.user.userid
Value copied directly if present
src_userid
src.user.userid
Value copied directly if present and authenteeId is empty
UID
src.user.userid
Value copied directly if present and authenteeId/src_userid are empty
file_path
target.file.full_path
Value copied directly
target_hostname
target.hostname
Value copied directly
target_port
target.port
Value converted to integer
task_name
target.resource.name
Value copied directly
target_url
target.url
Value copied directly
N/A
metadata.product_name
Set to "Ergon Informatik Airlock IAM"
N/A
metadata.vendor_name
Set to "Ergon Informatik"
Need more help?
Get answers from Community members and Google SecOps professionals.
