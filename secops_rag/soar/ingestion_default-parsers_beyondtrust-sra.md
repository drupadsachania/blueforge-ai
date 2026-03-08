# Collect BeyondTrust Secure Remote Access logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-sra/  
**Scraped:** 2026-03-05T09:51:19.703933Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BeyondTrust Secure Remote Access logs
Supported in:
Google secops
SIEM
This document explains how to collect BeyondTrust Secure Remote Access logs by using Bindplane. The parser handles two syslog formats. The first format uses key-value pairs within a structured message, while the second uses pipe-delimited fields; the parser extracts relevant fields from both formats and maps them to the UDM. It also performs event type categorization based on extracted keywords and handles specific logic for login/logout events and authentication types.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to a BeyondTrust Secure Remote Access.
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
BEYONDTRUST_REMOTE_ACCESS
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
Configure BeyondTrust remote support
Sign in to the
BeyondTrust
web UI.
Select
Appliance
>
Security
>
Appliance administration
.
In the
Syslog
section, do the following:
Message format
: Select
Legacy BSD format
.
Remote syslog server
: Enter the Bindplane IP address and Port.
Click
Submit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
datetime
metadata.event_timestamp
The timestamp is parsed from the
datetime
field using the RFC3 339 format if the
when
field is not present.
deviceHost
target.hostname
The value of
deviceHost
is directly mapped to
target.hostname
.
dstHost
target.ip
The value of
dstHost
is directly mapped to
target.ip
after being validated as a valid IP address.
dstPriv
additional.fields.[key=dstPriv].value.string_value
The value of
dstPriv
is placed in the
additional
field with key
dstPriv
.
dstUid
target.user.userid
The value of
dstUid
is directly mapped to
target.user.userid
.
dstUser
target.user.user_display_name
The value of
dstUser
is directly mapped to
target.user.user_display_name
.
eventName
metadata.event_type
If
eventName
is
login
(case-insensitive),
metadata.event_type
is set to
USER_LOGIN
. If
eventName
is
logout
(case-insensitive),
metadata.event_type
is set to
USER_LOGOUT
. Otherwise, if
eventName
is not empty,
metadata.event_type
is set to
USER_UNCATEGORIZED
. If
eventName
is empty, and the message matches the second grok pattern,
metadata.event_type
is set to
GENERIC_EVENT
. If
eventName
is empty, and the message matches the first grok pattern,
metadata.event_type
is set to
GENERIC_EVENT
. If
srcUid
,
userid
, or
who
are not empty,
metadata.event_type
is set to
USER_CHANGE_PERMISSIONS
. If
deviceHost
or
site
are not empty,
metadata.event_type
is set to
USER_UNCATEGORIZED
. Otherwise,
metadata.event_type
is set to
GENERIC_EVENT
.
event_name
additional.fields.[key=event_name].value.string_value
The value of
event_name
is placed in the
additional
field with key
event_name
.
event_name
metadata.product_event_type
The value of
event_name
is used in conjunction with the
id
field to populate
metadata.product_event_type
in the format
[
id
] -
event_name``.
externalKeyLabel
additional.fields.[key=externalKeyLabel].value.string_value
The value of
externalKeyLabel
is placed in the
additional
field with key
externalKeyLabel
.
id
metadata.product_event_type
The value of
id
is used in conjunction with the
event_name
field to populate
metadata.product_event_type
in the format
[
id
] -
event_name``.
jumpGroupId
additional.fields.[key=jumpGroupId].value.string_value
The value of
jumpGroupId
is placed in the
additional
field with key
jumpGroupId
.
jumpGroupName
additional.fields.[key=jumpGroupName].value.string_value
The value of
jumpGroupName
is placed in the
additional
field with key
jumpGroupName
.
jumpGroupType
additional.fields.[key=jumpGroupType].value.string_value
The value of
jumpGroupType
is placed in the
additional
field with key
jumpGroupType
.
jumpointId
additional.fields.[key=jumpointId].value.string_value
The value of
jumpointId
is placed in the
additional
field with key
jumpointId
.
jumpointName
additional.fields.[key=jumpointName].value.string_value
The value of
jumpointName
is placed in the
additional
field with key
jumpointName
.
kv_data
Various UDM fields
The
kv_data
field is parsed into key-value pairs, which are then mapped to various UDM fields based on their keys (e.g.,
eventName
,
when
,
who
,
who_ip
,
site
,
target
,
status
,
reason
).
kvdata
Various UDM fields
The
kvdata
field is parsed into key-value pairs, which are then mapped to various UDM fields based on their keys (e.g.,
msg
,
srcUser
,
srcUid
,
srcHost
,
dstUser
,
dstUid
,
dstHost
,
sessionId
,
jumpointId
,
jumpointName
,
jumpGroupId
,
jumpGroupName
,
jumpGroupType
,
externalKeyLabel
,
dstPriv
).
message
Various UDM fields
The
message
field is parsed using grok patterns to extract various fields, which are then mapped to UDM fields.
msg
metadata.description
The value of
msg
is directly mapped to
metadata.description
.
product_event_type
metadata.product_event_type
The value of
product_event_type
is directly mapped to
metadata.product_event_type
.
product_log_id
metadata.product_log_id
The value of
product_log_id
is directly mapped to
metadata.product_log_id
.
process_id
principal.process.pid
The value of
process_id
is directly mapped to
principal.process.pid
.
reason
security_result.description
The value of
reason
is directly mapped to
security_result.description
.
segment_number
additional.fields.[key=segment_number].value.string_value
The value of
segment_number
is placed in the
additional
field with key
segment_number
.
sessionId
network.session_id
The value of
sessionId
is directly mapped to
network.session_id
.
site
target.hostname
The value of
site
is directly mapped to
target.hostname
.
site_id
additional.fields.[key=site_id].value.string_value
The value of
site_id
is placed in the
additional
field with key
site_id
.
srcHost
principal.ip
The value of
srcHost
is directly mapped to
principal.ip
after being validated as a valid IP address.
srcUid
principal.user.userid
The value of
srcUid
is directly mapped to
principal.user.userid
.
srcUser
principal.user.user_display_name
The value of
srcUser
is directly mapped to
principal.user.user_display_name
.
status
security_result.action
If
status
is
failure
(case-insensitive),
security_result.action
is set to
BLOCK
. Otherwise,
security_result.action
is set to
ALLOW
.
status
security_result.action_details
The value of
status
is directly mapped to
security_result.action_details
.
target
target.application
The value of
target
is directly mapped to
target.application
.
rep_client
is replaced with
Representative Console
and
web/login
is replaced with
Web/Login
.
target
extensions.auth.type
If
target
is
rep_client
,
extensions.auth.type
is set to
MACHINE
. If
target
is
web/login
,
extensions.auth.type
is set to
SSO
. Otherwise,
extensions.auth.type
is set to
AUTHTYPE_UNSPECIFIED
.
timestamp
metadata.event_timestamp
The
timestamp
from the raw log is used as a fallback if neither
datetime
nor
when
are present.
total_segments
additional.fields.[key=total_segments].value.string_value
The value of
total_segments
is placed in the
additional
field with key
total_segments
.
device_product
additional.fields.[key=device_product].value.string_value
The value of
device_product
is placed in the
additional
field with key
device_product
.
device_vendor
additional.fields.[key=device_vendor].value.string_value
The value of
device_vendor
is placed in the
additional
field with key
device_vendor
.
device_version
metadata.product_version
The value of
device_version
is directly mapped to
metadata.product_version
.
when
metadata.event_timestamp
The timestamp is parsed from the
when
field using the UNIX format if present.
who
principal.user.userid
If the
who
field matches the regex pattern, the extracted
userid
is mapped to
principal.user.userid
. Otherwise, the entire
who
field is mapped to
principal.user.userid
.
who
principal.user.user_display_name
If the
who
field matches the regex pattern, the extracted
user_display_name
is mapped to
principal.user.user_display_name
.
who_ip
principal.ip
The value of
who_ip
is directly mapped to
principal.ip
.
(Parser Logic)
metadata.log_type
The log type is set to
BEYONDTRUST_REMOTE_ACCESS
.
(Parser Logic)
metadata.product_name
The product name is set to
BeyondTrust Secure Remote Access
.
(Parser Logic)
metadata.vendor_name
The vendor name is set to
BeyondTrust
.
(Parser Logic)
security_result.summary
The value is derived using the format
User %{eventName}
.
(Parser Logic)
extensions.auth.mechanism
If
method
contains
using password
, the mechanism is set to
USERNAME_PASSWORD
. If
method
contains
using elevate
, the mechanism is set to
REMOTE
.
Need more help?
Get answers from Community members and Google SecOps professionals.
