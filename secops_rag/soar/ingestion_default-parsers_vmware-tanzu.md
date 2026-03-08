# Collect VMware Tanzu logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu/  
**Scraped:** 2026-03-05T10:02:16.781773Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware Tanzu logs
Supported in:
Google secops
SIEM
This document explains how to ingest VMware Tanzu logs to Google Security Operations using Bindplane. The parser extracts the audit logs from either JSON or SYSLOG+JSON formatted messages. It parses the log data, normalizes fields into the UDM format, and enriches the event with metadata like user details, resource information, network activity, and security results, handling both single JSON objects and JSON embedded within syslog messages.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to VMware Tanzu
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
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'VMWARE_TANZU'
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
Configure Syslog for VMware Tanzu
Sign in to the
Tanzu Operations Manager
web UI.
Select your
User name
and then click
Settings
.
Select
Syslog
.
Click
Yes
to send system logs to a remote server.
Provide the following configuration details:
Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Transport Protocol
: Select
UDP
or
TCP
, depending on your actual Bindplane agent configuration.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
annotations.authorization.k8s.io/decision
security_result.action
If the annotation
authorization.k8s.io/decision
exists, its value is converted to uppercase. If the uppercase value is "ALLOW", the UDM field is set to ALLOW. Otherwise, it's set to BLOCK.
annotations.authorization.k8s.io/reason
security_result.description
If the annotation
authorization.k8s.io/reason
exists, its value (with double quotes removed) is used.
apiVersion
metadata.product_version
Directly mapped.
auditID
metadata.product_log_id
Directly mapped.
kind
metadata.product_event_type
Directly mapped.
objectRef.name
target.resource.name
Directly mapped.
objectRef.namespace
target.resource.attribute.labels.key
,
target.resource.attribute.labels.value
The
key
is set to "namespace", and the
value
is taken from
objectRef.namespace
.
objectRef.resource
target.resource.resource_subtype
Directly mapped.
objectRef.resourceVersion
target.resource.attribute.labels.key
,
target.resource.attribute.labels.value
The
key
is set to "resourceVersion", and the
value
is taken from
objectRef.resourceVersion
.
objectRef.uid
target.resource.product_object_id
Directly mapped.
requestReceivedTimestamp
/
timestamp
metadata.event_timestamp
The parser tries to parse
requestReceivedTimestamp
first. If it's not present, it uses the
timestamp
field extracted from the syslog prefix.
requestURI
target.url
Directly mapped.
responseStatus.code
network.http.response_code
Directly mapped after being converted to an integer.
sourceIPs
principal.ip
All IP addresses in the
sourceIPs
array are added to the
principal.ip
array.
stage
metadata.description
Directly mapped.
stageTimestamp
metadata.collected_timestamp
Directly mapped.
user.groups
principal.user.group_identifiers
All groups in the
user.groups
array are added to the
principal.user.group_identifiers
array.
user.uid
principal.user.userid
Directly mapped.
user.username
principal.user.user_display_name
Directly mapped.
verb
network.http.method
Directly mapped after being converted to uppercase. Determined by the
verb
field. If
verb
is "CREATE", the event type is
USER_RESOURCE_CREATION
. If
verb
is "PATCH" or "UPDATE", the event type is
USER_RESOURCE_UPDATE_CONTENT
. If
verb
is "DELETE", the event type is
USER_RESOURCE_DELETION
. Otherwise, if
verb
is not empty, the event type is
USER_RESOURCE_ACCESS
. If none of these conditions are met, the event type is set to
GENERIC_EVENT
. Hardcoded to "VMWARE_TANZU". Hardcoded to "VMWARE". Hardcoded to "VMWARE_TANZU". Hardcoded to "CLUSTER".
Need more help?
Get answers from Community members and Google SecOps professionals.
