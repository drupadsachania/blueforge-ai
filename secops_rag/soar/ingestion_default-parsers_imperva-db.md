# Collect Imperva Database logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-db/  
**Scraped:** 2026-03-05T09:57:14.353616Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Imperva Database logs
Supported in:
Google secops
SIEM
This document explains how to ingest Imperva Database logs to Google Security Operations using Bindplane. The parser first attempts to extract fields from various structured log formats like CEF, LEEF, and JSON. If those formats aren't found, it uses grok patterns to extract fields from unstructured syslog messages, ultimately mapping the extracted data to a unified data model (UDM). Imperva Database Security provides comprehensive database activity monitoring, auditing, and protection capabilities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Imperva SecureSphere management console
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
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'IMPERVA_DB'
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
Configure Syslog forwarding on Imperva Database
Sign in to the
Imperva SecureSphere Management Console
.
Go to
Configuration
>
Action Sets
.
Click
Add
to create a new Action Set or edit an existing one.
Click
Add Action
and provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Syslog
).
Action Type
: Select
GW Syslog
.
Host
: Enter the BindPlane Agent IP address.
Port
: Enter the BindPlane Agent port number (default
514
).
Protocol
: Select
UDP
or
TCP
, depending on your BindPlane Agent configuration.
Syslog Log Level
: Select
DEBUG
for comprehensive logging.
Syslog Facility
: Select
LOCAL0
or appropriate facility.
Action Interface
: Select
Gateway Log - Security Event - System Log (syslog) - JSON format (Extended)
for SYSLOG+JSON format, or
Gateway Log - Security Event - System Log (syslog)
for standard SYSLOG format.
Save the action configuration.
Go to
Policies
>
Security Policies
or
Policies
>
Database Audit Policies
.
Edit the relevant policies and add the Action Set containing your syslog action to ensure events are forwarded to Google SecOps.
UDM Mapping Table
Log field
UDM mapping
Logic
acct
principal.user.userid
If
acct
is "admin" then map to
target.user.userid
, else map to
principal.user.userid
. Remove quotes and spaces from
acct
before mapping.
action
security_result.action_details
Value of
action
field from raw log
alertSev
security_result.severity
If
alertSev
is "Informative" then map as "INFORMATIONAL", else map as uppercase of
alertSev
application
principal.application
If
application
is "pam_unix(sudo:session)" or
description
contains "pam_unix" then map as "pam_unix". If
message
contains " run-parts" then map as "run-parts". If
message
contains "audispd" then map as "audispd". If
message
contains "FSS audit" then map as "FSS audit". Else map as
application
field from raw log
application-name
target.application
Value of
application-name
field from raw log
audit-policy
security_result.category_details
Value of
audit-policy
field from raw log
bind-variables
additional.fields.bind_variables_label.value.string_value
Value of
bind-variables
field from raw log
category
security_result.category_details
Value of
category
field from raw log
COMMAND
target.process.command_line
If
exe
is not empty then map as
exe
field from raw log. Else map as
COMMAND
field from raw log
createTime
Not Mapped
db-schema-pair
additional.fields.
DB Name_{index}
.value.string_value, additional.fields.
Schema Name_{index}
.value.string_value
For each
db-schema-pair
object in the raw log, extract the
db-name
and
schema-name
fields and map them to
DB Name_{index}
and
Schema Name_{index}
respectively in the UDM, where
index
is the index of the object in the array.
db-user
principal.user.userid
If
db-user
is not empty then map as
db-user
field from raw log. Else if
os-user
is not empty and
db-user
is empty then map as
os-user
field from raw log
dbName
target.resource.name
Value of
dbName
field from raw log
dest-ip
target.ip, target.asset.ip
Value of
dest-ip
field from raw log
dest-port
target.port
Value of
dest-port
field from raw log
description
metadata.description
If
description
contains "user:" then extract the userid from
description
and map it to
userid
. If
userid
is not empty and
description
contains "Invalid" or "invalid" then replace "Invalid user" with "Invalid". If
application
is "sshd" then remove " from" and " by" from
description
. Else map as
description
field from raw log
dst
target.ip, target.asset.ip
Value of
dst
field from raw log
dstIP
target.ip, target.asset.ip
Value of
dstIP
field from raw log
dstPort
target.port
Value of
dstPort
field from raw log
event-type
metadata.product_event_type
Value of
event-type
field from raw log
eventType
metadata.product_event_type, metadata.event_type
If
eventType
is not empty and
srcIP
and
dstIP
are not empty then map
eventType
to
metadata.product_event_type
and map "NETWORK_CONNECTION" to
metadata.event_type
evntDesc
security_result.description
Value of
evntDesc
field from raw log
exe
target.process.command_line
Value of
exe
field from raw log
from
network.email.from
Remove "<" and ">" from
from
and map it to
network.email.from
group
target.user.group_identifiers
Value of
group
field from raw log
gw-ip
intermediary.ip, intermediary.asset.ip
Value of
gw-ip
field from raw log
host
target.hostname, target.asset.hostname
Value of
host
field from raw log
host-name
principal.hostname, principal.asset.hostname
Value of
host-name
field from raw log
hostname
principal.hostname, principal.asset.hostname
Value of
hostname
field from raw log
ip
target.ip, target.asset.ip
Value of
ip
field from raw log
mx-ip
intermediary.ip, intermediary.asset.ip
Value of
mx-ip
field from raw log
objects-list
additional.fields.
Object_{index}
.value.string_value
For each
objects-list
object in the raw log, extract the object and map it to
Object_{index}
in the UDM, where
index
is the index of the object in the array.
Operation
about.labels.Operation.value
Value of
Operation
field from raw log
Operation type
about.labels.
Operation Type
.value
Value of
Operation type
field from raw log
os-user
principal.user.userid, additional.fields.
OS User
.value.string_value
If
os-user
is not empty and
db-user
is empty then map as
os-user
field from raw log. Else map as
OS User
field from raw log
Parsed Query
target.process.command_line
Value of
Parsed Query
field from raw log
parsed-query
additional.fields.
Parsed Query
.value.string_value
Value of
parsed-query
field from raw log
pid
target.process.pid
Value of
pid
field from raw log
policy-id
security_result.detection_fields.
Policy_ID_{index}
.value
For each
policy-id
object in the raw log, extract the policy and map it to
Policy_ID_{index}
in the UDM, where
index
is the index of the object in the array.
policyName
security_result.detection_fields.policyName_label.value
Value of
policyName
field from raw log
port
target.port
Value of
port
field from raw log
Privileged
about.labels.Privileged.value
If
Privileged
is true then map as "True", else map as "False"
proto
network.ip_protocol
Value of
proto
field from raw log
protocol
network.ip_protocol
If
protocol
is "TCP" or "UDP" then map as
protocol
field from raw log
PWD
target.file.full_path
Value of
PWD
field from raw log
Raw Data
target.resource.attribute.labels.raw_Data.value
Value of
Raw Data
field from raw log
raw-query
additional.fields.
Raw Query
.value.string_value
Value of
raw-query
field from raw log
ruleName
security_result.rule_name
Value of
ruleName
field from raw log
server-group
additional.fields.serve_group_label.value.string_value
Value of
server-group
field from raw log
service-name
additional.fields.service_name_label.value.string_value
Value of
service-name
field from raw log
Service Type
additional.fields.
Service Type
.value.string_value
Value of
Service Type
field from raw log
size
network.received_bytes
Value of
size
field from raw log
Stored Proc
about.labels.Stored_Proc.value
If
Stored Proc
is true then map as "True", else map as "False"
Table Group
target.group.group_display_name
Value of
Table Group
field from raw log
timestamp
metadata.event_timestamp
Value of
timestamp
field from raw log
to
network.email.to
Remove "<" and ">" from
to
and map it to
network.email.to
USER
principal.user.userid, target.user.userid
If
USER
is not empty and
USER
is "admin" then map as
USER
field from raw log to
target.user.userid
. Else if
USER
is not empty then map as
USER
field from raw log to
principal.user.userid
user-authenticated
security_result.detection_fields.user_authenticated.value
Value of
user-authenticated
field from raw log
user-group
additional.fields.user_group_label.value.string_value
Value of
user-group
field from raw log
username
principal.user.user_display_name
Value of
username
field from raw log
usrName
principal.user.userid
Value of
usrName
field from raw log
extensions.auth.mechanism
Hardcoded to "USERNAME_PASSWORD" if
description
contains "authentication failure" or "check pass; user unknown" or "Invalid user" or "invalid user" or
error
is not empty
extensions.auth.type
Hardcoded to "AUTHTYPE_UNSPECIFIED" if
has_principal
is "true" and
has_target
is "true" and
event-type
is "Login"
metadata.event_type
Hardcoded to "PROCESS_OPEN" if
PWD
is not empty. Hardcoded to "PROCESS_OPEN" if
message
contains "starting" or
application
is "pman" or "CROND" or "run-parts" and
event_type
is empty. Hardcoded to "NETWORK_CONNECTION" if
description
is "Syslog connection established" or "Syslog connection broken" or "Syslog connection failed". Hardcoded to "EMAIL_UNCATEGORIZED" if
application
is "postfix/qmgr" or "postfix/local" or "postfix/pickup". Hardcoded to "EMAIL_TRANSACTION" if
application
is "postfix/local" or "postfix/pickup" and
status
is "sent (delivered to mailbox)". Hardcoded to "NETWORK_HTTP" if
application
is "sshd" and
description
does not contain "check pass; user unknown" and
description
does not contain "authentication failure" and
description
does not contain "invalid". Hardcoded to "USER_LOGIN" if
description
contains "authentication failure" or "check pass; user unknown" or "Invalid user" or "invalid user" or
error
is not empty. Hardcoded to "FILE_SYNC" if
file_path
is not empty. Hardcoded to "PROCESS_UNCATEGORIZED" if
message
contains "reconfigure" and
application
is "pman". Hardcoded to "PROCESS_TERMINATION" if
message
contains "exit code 1" and
application
is "pman". Hardcoded to "NETWORK_CONNECTION" if
eventType
is not empty and
srcIP
and
dstIP
are not empty. Hardcoded to "USER_LOGIN" if
has_principal
is "true" and
has_target
is "true" and
event-type
is "Login". Hardcoded to "NETWORK_CONNECTION" if
has_principal
is "true" and
has_target
is "true" and
protocol
is not empty. Hardcoded to "STATUS_UPDATE" if
has_principal
is "true". Hardcoded to "GENERIC_EVENT" if
event_type
is empty or "GENERIC_EVENT"
metadata.log_type
Hardcoded to "IMPERVA_DB"
metadata.product_name
Hardcoded to "IMPERVA DB"
metadata.vendor_name
Hardcoded to "IMPERVA DB"
security_result.action
Hardcoded to "ALLOW" if
description
does not contain "authentication failure" or "check pass; user unknown" or "Invalid user" or "invalid user" and
error
is empty. Hardcoded to "BLOCK" if
description
contains "authentication failure" or "check pass; user unknown" or "Invalid user" or "invalid user" or
error
is not empty
security_result.rule_id
If
description
contains "alert_score" or "new_alert_score" then extract the ruleid from
description
and map it to
security_result.rule_id
Need more help?
Get answers from Community members and Google SecOps professionals.
