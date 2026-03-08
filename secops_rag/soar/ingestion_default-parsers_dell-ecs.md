# Collect Dell ECS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-ecs/  
**Scraped:** 2026-03-05T09:54:24.513729Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Dell ECS logs
Supported in:
Google secops
SIEM
This parser extracts fields from DELL ECS syslog messages, mapping them to the UDM. It handles
UPDATE
and
DELETE
event types specifically, extracting user and IP information for login/logout events. Other events are categorized as
GENERIC_EVENT
. It uses grok patterns to parse the message and mutate filters to populate UDM fields, dropping events that don't match the expected format.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Dell ECS.
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
system where Bindplane Agent will be installed.
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
Install Bindplane Agent
Windows Installation
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
Linux Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
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
tcplog
:
# Replace the below port <54525> and IP <0.0.0.0> with your specific values
listen_address
:
"0.0.0.0:54525"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the creds location below according the placement of the credentials file you downloaded
creds
:
'{
json
file
for
creds
}'
# Replace <customer_id> below with your actual ID that you copied
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# You can apply ingestion labels below as preferred
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
dell_ecs
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
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart Bindplane Agent to apply the changes
In Linux, to restart the Bindplane Agent, run the following command:
sudo
systemctl
restart
bindplane-agent
In Windows, to restart the Bindplane Agent, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Dell ECS to Forward Logs to the Syslog Server
Sign in to the ECS management portal using administrative credentials.
Go to
Settings
>
Event Notifications
>
Syslog
.
Click
New Server
.
Provide the following details:
Protocol
: select either
UDP
or
TCP
(ensure it matches the protocol configured on the Syslog server).
Target
: enter the
IP address
or
Fully Qualified Domain Name
(FQDN) of the Syslog server.
Port
: enter the
port number
.
Severity
: select
Informational
as the minimum severity level of logs to be forwarded.
Click
Save
.
Supported Dell ECS sample log
SYSLOG
<134>Mar 11 05:11:27 host.example.com LOGIN UPDATE 192.0.2.1 dummy_user User dummy_user logged in successfully
UDM Mapping Table
Log Field
UDM Mapping
Logic
data
read_only_udm.metadata.description
If
eventType
is
UPDATE
, the description is extracted from the
data
field using a regular expression. If
eventType
is
DELETE
, the description is extracted from the
data
field using a regular expression and further processed to extract the user ID.
data
read_only_udm.principal.ip
If
eventType
is
UPDATE
, the IP address is extracted from the
data
field using a regular expression.
data
read_only_udm.target.resource.product_object_id
If
eventType
is
DELETE
, the URN token is extracted from the
data
field using a regular expression.
data
read_only_udm.target.user.userid
If
eventType
is
UPDATE
, the user ID is extracted from the
data
field using a regular expression. If
eventType
is
DELETE
, the user ID is extracted from the description field after initial processing of the
data
field.
eventType
read_only_udm.metadata.event_type
If
eventType
is
UPDATE
and a
userid
is extracted, the event type is set to
USER_LOGIN
. If
eventType
is
DELETE
and a
userid
is extracted, the event type is set to
USER_LOGOUT
. Otherwise, the event type is set to
GENERIC_EVENT
.
eventType
read_only_udm.metadata.product_event_type
The value is derived by concatenating the
serviceType
and
eventType
fields from the raw log, enclosed in square brackets and separated by " - ".
hostname
read_only_udm.principal.asset.hostname
The hostname is copied from the
hostname
field.
hostname
read_only_udm.principal.hostname
The hostname is copied from the
hostname
field.
log_type
read_only_udm.metadata.log_type
The log type is set to
DELL_ECS
. The mechanism is hardcoded to
MECHANISM_UNSPECIFIED
. The event timestamp is copied from the
timestamp
field of the raw log entry. The product name is hardcoded to
ECS
. The vendor name is hardcoded to
DELL
. If
eventType
is
DELETE
, the resource type is hardcoded to
CREDENTIAL
.
timestamp
read_only_udm.metadata.event_timestamp
The event timestamp is taken from the
timestamp
field of the raw log entry.
timestamp
timestamp
The timestamp is parsed from the
timestamp
field of the raw log entry.
Need more help?
Get answers from Community members and Google SecOps professionals.
