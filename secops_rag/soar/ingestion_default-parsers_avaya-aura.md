# Collect Avaya Aura logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avaya-aura/  
**Scraped:** 2026-03-05T09:50:21.316548Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Avaya Aura logs
Supported in:
Google secops
SIEM
This document explains how to ingest Avaya Aura logs to Google Security Operations
using Bindplane. The parser first extracts fields from raw Avaya Aura syslog
messages using regular expressions and the "grok" filter. Then, it maps the
extracted fields to a Unified Data Model (UDM), normalizes values like severity,
and identifies specific event types like user login or user logout based on keywords.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Avaya Aura
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
udolog
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
'AVAYA_AURA'
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
Configure Syslog in Avaya Aura
Sign in to the
Avaya Aura
console.
Go to
EM
>
System Configuration
>
Logging Settings
>
Syslog
.
Enable
SYSLOG Delivery of Logs
.
Click
Add
.
Provide the following configuration details:
Server Address
: Enter the Bindplane agent IP Address.
Port
: Enter the Bindplane agent listening port.
Click
Save
.
Click
Confirm
.
Restart
Avaya Aura.
UDM mapping table
Log field
UDM mapping
Logic
data{}.@timestamp
metadata.event_timestamp
The event timestamp is parsed from the data field using the grok pattern and assigned to the event_timestamp field in the metadata section of the UDM.
data{}.host
principal.hostname
The host value is extracted from the data field using the grok pattern and assigned to the hostname field within the principal section of the UDM.
data{}.portal
security_result.about.resource.attribute.labels.value
The portal value is extracted from the data field using the grok pattern and assigned as the value of the
Portal
label within the about.resource.attribute.labels section of the security_result in the UDM.
data{}.prod_log_id
metadata.product_log_id
The prod_log_id value is extracted from the data field using the grok pattern and assigned to the product_log_id field in the metadata section of the UDM.
data{}.sec_cat
security_result.category_details
The sec_cat value is extracted from the data field using the grok pattern and assigned to the category_details field within the security_result section of the UDM.
data{}.sec_desc
security_result.description
The sec_desc value is extracted from the data field using the grok pattern and assigned to the description field within the security_result section of the UDM.
data{}.severity
security_result.severity
The severity value is extracted from the data field using the grok pattern. If the severity is
warn
,
fatal
, or
error
(case-insensitive), it is mapped to
HIGH
in the security_result.severity field of the UDM. Otherwise, if the severity is
info
(case-insensitive), it is mapped to
LOW
.
data{}.summary
security_result.summary
The summary value is extracted from the data field using the grok pattern and assigned to the summary field within the security_result section of the UDM.
data{}.user_id
target.user.userid
The user_id value is extracted from the data field using the grok pattern and assigned to the userid field within the target.user section of the UDM.
extensions.auth.type
The auth.type field is set to
AUTHTYPE_UNSPECIFIED
if the event_name field contains
log(in|on)
or
logoff
(case-insensitive), or if the summary field contains
login
or
logoff
(case-insensitive) and the user_id field is not empty.
metadata.description
The description field is populated with the value of the desc field if it is not empty.
metadata.event_type
The event_type field is determined based on the following logic:  - If the event_name field contains
log(in|on)
or the summary field contains
login
(case-insensitive) and the user_id field is not empty, the event_type is set to
USER_LOGIN
.  - If the event_name field contains
logoff
or the summary field contains
logoff
(case-insensitive) and the user_id field is not empty, the event_type is set to
USER_LOGOUT
.  - If the has_principal field is
true
, the event_type is set to
STATUS_UPDATE
.  - Otherwise, the event_type remains as
GENERIC_EVENT
(default value).
metadata.log_type
The log_type is hardcoded to
AVAYA_AURA
.
metadata.product_event_type
The product_event_type field is populated with the value of the event_name field if it is not empty.
metadata.product_name
The product_name is hardcoded to
AVAYA AURA
.
metadata.vendor_name
The vendor_name is hardcoded to
AVAYA AURA
.
security_result.action
The action field within the security_result section is set based on the following logic:  - If the summary field contains
fail
or
failed
(case-insensitive), the action is set to
BLOCK
.  - If the summary field contains
success
(case-insensitive), the action is set to
ALLOW
.
security_result.severity_details
The severity_details field is populated with the value of the severity_details field if it is not empty.
timestamp.nanos
metadata.event_timestamp.nanos
The nanos value from the timestamp field is directly mapped to the nanos field within the event_timestamp section of the metadata in the UDM.
timestamp.seconds
metadata.event_timestamp.seconds
The seconds value from the timestamp field is directly mapped to the seconds field within the event_timestamp section of the metadata in the UDM.
Need more help?
Get answers from Community members and Google SecOps professionals.
