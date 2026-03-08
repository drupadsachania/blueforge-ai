# Collect Imperva SecureSphere Management logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-securesphere/  
**Scraped:** 2026-03-05T09:57:18.938213Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Imperva SecureSphere Management logs
Supported in:
Google secops
SIEM
This document explains how to ingest Imperva SecureSphere Management logs to Google Security Operations using Bindplane. The parser extracts fields from the logs in either CEF or JSON format. It uses grok patterns and key-value parsing to map raw log fields to the UDM, handling both standard CEF fields and custom JSON structures, and prioritizing JSON data if available. Imperva SecureSphere provides comprehensive web application firewall, database security, and file security capabilities for on-premises and cloud deployments.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Imperva SecureSphere Management console
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
'IMPERVA_SECURESPHERE'
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
Configure Syslog forwarding on Imperva SecureSphere Management
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
to create a new Action Set.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Syslog
).
Configure Security Event Action
Click
Add Action
and configure:
Action Type
: Select
Syslog
.
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (default
514
).
Protocol
: Select
UDP
or
TCP
.
Syslog Log Level
: Select
DEBUG
.
Syslog Facility
: Select
LOCAL0
.
Message Format
: Select
Gateway Log - Security Event - System Log (syslog) using CEF standard
.
Configure System Event Action
Click
Add Action
and configure:
Action Type
: Select
System Log
.
Host
: Enter the BindPlane Agent IP address.
Port
: Enter the BindPlane Agent port number.
Protocol
: Select
UDP
or
TCP
.
Message Format
: Select
Log System Event to System Log (syslog) using CEF standard
.
Apply Action Sets to Policies
Go to
Policies
>
Security Policies
.
For each relevant policy, configure
Followed Actions
to use your Action Set.
Go to
Policies
>
System Events Policies
.
Configure system event policies to use the Action Set for comprehensive monitoring.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.action_details
The value of the
action
field is assigned to the
security_result.action_details
field.
application-name
target.application
The value of the
application-name
field is assigned to the
target.application
field.
cat
security_result.category_details
The value of the
cat
field is assigned to the
security_result.category_details
field.
class
security_result.detection_fields.value
The value of the
class
field is assigned to the
value
field within
security_result.detection_fields
. The corresponding
key
is "class".
collection_time.seconds
metadata.event_timestamp.seconds
The value of
collection_time.seconds
from the raw log is used as the seconds value for the
metadata.event_timestamp
.
create-time
metadata.event_timestamp.seconds
The value of
create-time
is parsed and its seconds value is used as the seconds value for the
metadata.event_timestamp
.
cs1
security_result.rule_name
The value of the
cs1
field is assigned to the
security_result.rule_name
field.
cs10
target.resource.attribute.labels.value
The value of the
cs10
field is assigned to the
value
field within
target.resource.attribute.labels
.
cs10Label
target.resource.attribute.labels.key
The value of the
cs10Label
field is assigned to the
key
field within
target.resource.attribute.labels
.
cs11
principal.application
The value of the
cs11
field is assigned to the
principal.application
field.
cs12
security_result.description
The value of the
cs12
field, after removing curly braces and dollar signs, is assigned to the
security_result.description
field.
cs14
target.resource.attribute.labels.value
The value of the
cs14
field is assigned to the
value
field within
target.resource.attribute.labels
.
cs14Label
target.resource.attribute.labels.key
The value of the
cs14Label
field is assigned to the
key
field within
target.resource.attribute.labels
.
cs15
security_result.summary
The value of the
cs15
field is assigned to the
security_result.summary
field.
cs16
principal.process.command_line
The value of the
cs16
field is assigned to the
principal.process.command_line
field.
cs17
target.resource.resource_subtype
The value of the
cs17
field is assigned to the
target.resource.resource_subtype
field.
cs2
principal.group.group_display_name
The value of the
cs2
field is assigned to the
principal.group.group_display_name
field.
cs3
principal.hostname
,
principal.asset.hostname
The value of the
cs3
field is assigned to both the
principal.hostname
and
principal.asset.hostname
fields.
cs4
target.application
The value of the
cs4
field is assigned to the
target.application
field, unless the value is "ProcessWitness".
cs5
metadata.description
The value of the
cs5
field is assigned to the
metadata.description
field.
cs6
target.resource_ancestors.name
The value of the
cs6
field is assigned to the
target.resource_ancestors.name
field.
cs7
target.resource_ancestors.resource_subtype
The value of the
cs7
field is assigned to the
target.resource_ancestors.resource_subtype
field.
cs8
target.resource.name
,
target.resource.resource_type
The value of the
cs8
field is assigned to the
target.resource.name
field, and the
target.resource.resource_type
is set to "DATABASE".
cs9
principal.user.userid
The value of the
cs9
field is assigned to the
principal.user.userid
field.
description
security_result.description
The value of the
description
field is assigned to the
security_result.description
field.
dest-ip
target.ip
,
target.asset.ip
The IP address extracted from the
dest-ip
field is assigned to both the
target.ip
and
target.asset.ip
fields.
dest-port
target.port
The value of the
dest-port
field, converted to an integer, is assigned to the
target.port
field.
deviceExternalId
intermediary.hostname
The value of the
deviceExternalId
field is assigned to the
intermediary.hostname
field.
dpt
target.port
The value of the
dpt
field, converted to an integer, is assigned to the
target.port
field.
dst
target.ip
,
target.asset.ip
The value of the
dst
field is assigned to both the
target.ip
and
target.asset.ip
fields.
duser
target.user.userid
The value of the
duser
field is assigned to the
target.user.userid
field.
eventId
metadata.product_log_id
The value of the
eventId
field is assigned to the
metadata.product_log_id
field.
gateway-name
security_result.detection_fields.value
The value of the
gateway-name
field is assigned to the
value
field within
security_result.detection_fields
. The corresponding
key
is "gateway-name".
http.request.method
network.http.method
The value of the
http.request.method
field is assigned to the
network.http.method
field.
http.request.user-agent
network.http.user_agent
The value of the
http.request.user_agent
field is assigned to the
network.http.user_agent
field.
http.response.code
network.http.response_code
The value of the
http.response.code
field, converted to an integer, is assigned to the
network.http.response_code
field.
http.session-id
network.session_id
The value of the
http.session-id
field is assigned to the
network.session_id
field.
http.user-name
principal.user.userid
The value of the
http.user-name
field, with surrounding quotes removed, is assigned to the
principal.user.userid
field.
log_type
metadata.log_type
The value of the
log_type
field from the raw log is assigned to the
metadata.log_type
field.
mx-ip
intermediary.ip
The value of the
mx-ip
field is assigned to the
intermediary.ip
field.
MxIP
intermediary.ip
The value of the
MxIP
field is assigned to the
intermediary.ip
field.
OSUser
principal.user.userid
The value of the
OSUser
field is assigned to the
principal.user.userid
field.
policy-name
security_result.detection_fields.value
The value of the
policy-name
field is assigned to the
value
field within
security_result.detection_fields
. The corresponding
key
is "policy-name".
pquery
target.resource.name
,
target.process.command_line
If
pquery
is not empty and contains the word "from", the table name is extracted and assigned to
target.resource.name
,
target.resource.resource_type
is set to "TABLE", and the entire
pquery
value is assigned to
target.process.command_line
. Otherwise, the entire
pquery
value is assigned to
target.resource.name
.
pro
security_result.description
The value of the
pro
field is assigned to the
security_result.description
field.
product
metadata.product_name
The value of the
product
field is assigned to the
metadata.product_name
field.
product_type
metadata.product_event_type
The value of the
product_type
field is assigned to the
metadata.product_event_type
field.
protocol
network.ip_protocol
If the value of the
protocol
field is "TCP" or "UDP", it is assigned to the
network.ip_protocol
field.
proto
network.ip_protocol
The value of the
proto
field is assigned to the
network.ip_protocol
field.
reason
security_result.rule_name
The value of the
reason
field is assigned to the
security_result.rule_name
field.
rt
metadata.event_timestamp.seconds
The value of
rt
is parsed and its seconds value is used as the seconds value for the
metadata.event_timestamp
.
server-group-name
target.resource.attribute.labels.value
The value of the
server-group-name
field is assigned to the
value
field within
target.resource.attribute.labels
. The corresponding
key
is "server-group-name".
server-group-simulation-mode
target.resource.attribute.labels.value
The value of the
server-group-simulation-mode
field is assigned to the
value
field within
target.resource.attribute.labels
. The corresponding
key
is "server-group-simulation-mode".
service-name
target.resource.attribute.labels.value
The value of the
service-name
field is assigned to the
value
field within
target.resource.attribute.labels
. The corresponding
key
is "service-name".
ServiceName
target.application
If
ApplicationName
is not empty and
ServiceName
is empty, the value of
ApplicationName
is assigned to
ServiceName
. The value of
ServiceName
is then assigned to
target.application
.
severity
security_result.severity
,
security_result.severity_details
The value of the
severity
field is converted to uppercase. If it's one of "LOW", "MEDIUM", "HIGH", "CRITICAL", it's assigned to
security_result.severity
. If it's "INFORMATIVE" or "INFO",
security_result.severity
is set to "INFORMATIONAL". The original value is also assigned to
security_result.severity_details
.
severity_data
security_result.severity
The value of the
severity_data
field is converted to uppercase. If it's one of "HIGH", "LOW", "MEDIUM", "CRITICAL", "ERROR", "INFORMATIONAL", it's assigned to
security_result.severity
.
source-ip
principal.ip
,
principal.asset.ip
The value of the
source-ip
field is assigned to both the
principal.ip
and
principal.asset.ip
fields.
source-port
principal.port
The value of the
source-port
field, converted to an integer, is assigned to the
principal.port
field.
spt
principal.port
The value of the
spt
field, converted to an integer, is assigned to the
principal.port
field.
src
principal.ip
,
principal.asset.ip
The value of the
src
field is assigned to both the
principal.ip
and
principal.asset.ip
fields.
srcapp
principal.application
The value of the
srcapp
field is assigned to the
principal.application
field.
srchost
principal.hostname
,
principal.asset.hostname
The value of the
srchost
field is assigned to both the
principal.hostname
and
principal.asset.hostname
fields.
vendor
metadata.vendor_name
The value of the
vendor
field is assigned to the
metadata.vendor_name
field.
version
metadata.product_version
The value of the
version
field is assigned to the
metadata.product_version
field.
violation-id
security_result.detection_fields.value
The value of the
violation-id
field is assigned to the
value
field within
security_result.detection_fields
. The corresponding
key
is "violation-id".
violation-type
security_result.detection_fields.value
The value of the
violation-type
field is assigned to the
value
field within
security_result.detection_fields
. The corresponding
key
is "violation-type".
Need more help?
Get answers from Community members and Google SecOps professionals.
