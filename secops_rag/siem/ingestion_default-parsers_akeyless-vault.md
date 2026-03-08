# Collect Akeyless Vault logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault/  
**Scraped:** 2026-03-05T09:18:43.334851Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akeyless Vault logs
Supported in:
Google secops
SIEM
This document explains how to ingest Akeyless Vault logs to
Google Security Operations using direct ingestion or Bindplane. The parser first
normalizes the log messages, which can be in either key-value or JSON format,
into a consistent structure. Then, it extracts relevant fields and maps them to
the Unified Data Model (UDM) schema, categorizing the event type based on the
presence of IP addresses and actions performed.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to Akeyless Vault
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
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
Configure log forwarding for direct ingestion to Google SecOps in Akeyless Vault
Sign in to your
Akeyless Gateway
web UI.
Go to
Log Forwarding
.
Select
Enable
.
Provide the following configuration details:
Log Format
: Select
JSON
.
Audit Log Server
: Enter
https://audit.akeyless.io/
.
Service
: Select
Google Chronicle
.
Service Account Key
: Provide the JSON file holding service account credentials.
Customer ID
: Enter your Google SecOps unique identifier.
Region
: Enter the region where your Google SecOps is provisioned.
Log Type
: Enter
AKEYLESS_VAULT
.
Click
Save Changes
.
Optional: Ingest Syslog through Bindplane
Windows Bindplane installation
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
Linux Bindplane installation
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
'AKEYLESS_VAULT'
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
Restart the Bindlane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding to Bindplane in Akeyless Vault
Sign in to your
Akeyless Gateway
web UI.
Go to
Log Forwarding
.
Select
Enable
.
Provide the following configuration details:
Log Format
: Select
JSON
.
Audit Log Server
: Enter
https://audit.akeyless.io/
.
Service
: Select
Syslog
.
Syslog Network
: Select
UDP
. (You can select another option, depending on your Bindplane agent configuration).
Syslog Host
: Enter the Bindplane agent IP address.
Syslog Formatter
: Select
Text
.
(
Optional) TLS
: Select the
TLS
checkbox and upload the
TLS Certificate
.
Click
Save Changes
.
UDM mapping table
Log Field
UDM Mapping
Logic
access_id
read_only_udm.metadata.product_log_id
Directly mapped from
access_id
field. If not present, extracted from the
message
field using the regex
access_id:\s+(?<accessid>[\w-]+)
.
account_id
read_only_udm.target.user.userid
Directly mapped from
account_id
field.
action
read_only_udm.security_result.action_details
Directly mapped from
action
field.
component
read_only_udm.target.resource.name
Directly mapped from
component
field.
duration
read_only_udm.network.session_duration.seconds
Directly mapped from
duration
field and converted to integer.
remote_addr
read_only_udm.principal.ip
Extracted from
remote_addr
field, split by comma and added to the
principal.ip
array.
request_parameters.access_type
read_only_udm.target.resource.attribute.labels.value (where key is 'access_type')
Directly mapped from
request_parameters.access_type
field. If not present, extracted from the
message
field using the regex
access_type:\s+(?<accesstype>[\S]+)
.
request_parameters.comment
read_only_udm.target.resource.attribute.labels.value (where key is 'comment')
Directly mapped from
request_parameters.comment
field.
request_parameters.operation
read_only_udm.target.resource.attribute.labels.value (where key is 'operation')
Directly mapped from
request_parameters.operation
field.
request_parameters.product
read_only_udm.target.resource.attribute.labels.value (where key is 'product')
Directly mapped from
request_parameters.product
field. If not present, extracted from the
message
field using the regex
product:\s+(?<product>[\w\s]+)
.
request_parameters.token_id
read_only_udm.target.resource.attribute.labels.value (where key is 'token_id')
Directly mapped from
request_parameters.token_id
field.
request_parameters.transaction_type
read_only_udm.target.resource.attribute.labels.value (where key is 'transaction_type')
Directly mapped from
request_parameters.transaction_type
field and converted to string. If not present, extracted from the
message
field using the regex
transaction_type:\s+(?<transactiontype>[\S]+)
.
request_parameters.unique_id
read_only_udm.target.resource.attribute.labels.value (where key is 'unique_id')
Directly mapped from
request_parameters.unique_id
field. If not present, extracted from the
message
field using the regex
unique_id:\s+(?<uniqueid>[\w-]+)
.
request_parameters.universal_identity_rotate_type
read_only_udm.target.resource.attribute.labels.value (where key is 'universal_identity_rotate_type')
Directly mapped from
request_parameters.universal_identity_rotate_type
field.
request_parameters.user_agent
read_only_udm.target.resource.attribute.labels.value (where key is 'user_agent')
Directly mapped from
request_parameters.user_agent
field.
severity
Directly mapped from
severity
field.
status
read_only_udm.network.http.response_code
Directly mapped from
status
field and converted to integer.
timestamp
read_only_udm.metadata.event_timestamp
Directly mapped from the log entry
timestamp
field.
read_only_udm.metadata.log_type
Hardcoded to
AKEYLESS_VAULT
.
read_only_udm.metadata.event_type
Set to
STATUS_UPDATE
if
ip_present
is true, otherwise defaults to
GENERIC_EVENT
.
read_only_udm.metadata.vendor_name
Extracted from the
message
field using the regex
CEF:0|%{DATA:device_vendor}|%{DATA:device_product}|%{DATA:device_version}|%{DATA:device_event_class_id}\s+%{WORD}\[%{INT}\]:\s+%{GREEDYDATA:kv_data}
.
read_only_udm.metadata.product_name
Extracted from the
message
field using the regex
CEF:0|%{DATA:device_vendor}|%{DATA:device_product}|%{DATA:device_version}|%{DATA:device_event_class_id}\s+%{WORD}\[%{INT}\]:\s+%{GREEDYDATA:kv_data}
.
read_only_udm.metadata.product_version
Extracted from the
message
field using the regex
CEF:0|%{DATA:device_vendor}|%{DATA:device_product}|%{DATA:device_version}|%{DATA:device_event_class_id}\s+%{WORD}\[%{INT}\]:\s+%{GREEDYDATA:kv_data}
.
read_only_udm.metadata.product_event_type
Extracted from the
message
field using the regex
<%{INT}>%{TIMESTAMP_ISO8601:time}\s+%{DATA}\s+(?P<product_event_type>[\w-]+)\[%{INT}\]:\s+(?P<time2>\d{1,2}-%{MONTH}-\d{1,4}\s+\d{1,2}:\d{1,2}:\d{1,2}.\d+)\s+%{WORD}\s+%{WORD:severity}\s+CEF:0|%{DATA:device_vendor}|%{DATA:device_product}|%{DATA:device_version}|%{DATA:device_event_class_id}\s+%{WORD}\[%{INT}\]:\s+%{GREEDYDATA:kv_data}
.
read_only_udm.target.namespace
Extracted from the
message
field using the regex
namespace:\s+(?<namespace>[\S]+)
.
read_only_udm.security_result.severity
Mapped from
severity
field:
Info
to
INFORMATIONAL
,
Error
to
ERROR
,
Warning
to
MEDIUM
, otherwise
UNKNOWN_SEVERITY
.
read_only_udm.network.http.method
Mapped from
action
field:
get
to
GET
,
put
and
Authentication
to
PUT
,
post
to
POST
,
delete
to
DELETE
.
Need more help?
Get answers from Community members and Google SecOps professionals.
