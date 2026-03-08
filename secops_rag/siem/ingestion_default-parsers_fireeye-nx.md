# Collect FireEye NX logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx/  
**Scraped:** 2026-03-05T09:24:27.823696Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FireEye NX logs
Supported in:
Google secops
SIEM
This document explains how to ingest Trellix Network Security (formerly FireEye NX) logs to Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Trellix Network Security (NX) management console
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed
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
chronicle/fireeye_nx
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
# Replace with your regional endpoint
endpoint
:
<
ENDPOINT
>
log_type
:
'FIREEYE_NX'
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
chronicle/fireeye_nx
Replace the port and IP address as required in your infrastructure.
Replace
<CUSTOMER_ID>
with the actual Customer ID.
Replace the
<ENDPOINT>
value with your regional endpoint:
United States
:
malachiteingestion-pa.googleapis.com
Europe (Frankfurt)
:
europe-west3-malachiteingestion-pa.googleapis.com
Europe (London)
:
europe-west2-malachiteingestion-pa.googleapis.com
Europe (Zurich)
:
europe-west6-malachiteingestion-pa.googleapis.com
Europe (Turin)
:
europe-west12-malachiteingestion-pa.googleapis.com
Asia (Tokyo)
:
asia-northeast1-malachiteingestion-pa.googleapis.com
Middle East (Tel Aviv)
:
me-west1-malachiteingestion-pa.googleapis.com
Australia (Sydney)
:
australia-southeast1-malachiteingestion-pa.googleapis.com
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
Configure Syslog forwarding on Trellix Network Security
Sign in to the
Trellix Network Security console
with an administrator account.
Go to
Settings
>
Notifications
.
Click the
rsyslog
tab.
Select the
Event type
checkbox to enable rsyslog notifications.
In the
Settings
panel, provide the following configuration details:
Default format
: Select
CEF
.
In the
Rsyslog Server Listing
section:
Type a descriptive name for the new entry (for example,
Google SecOps BindPlane
).
Click the
Add Rsyslog Server
button.
For the newly added server, provide the following configuration details:
Enabled
: Check the checkbox to enable the server.
IP Address
: Enter the BindPlane Agent IP address.
Port
: Enter the BindPlane Agent port number (for example,
514
).
Protocol
: Select
UDP
or
TCP
, depending on your BindPlane Agent configuration.
Event Types
: Select the event types to forward (or select
all
for comprehensive logging).
Click the
Update
button to save the configuration.
UDM Mapping Table
Log field
UDM mapping
Logic
alert.dst.ip
target.ip, target.asset.ip
Direct mapping from
alert.dst.ip
field
alert.dst.mac
target.mac, target.asset.mac
Direct mapping from
alert.dst.mac
field
alert.dst.port
target.port
Direct mapping from
alert.dst.port
field
alert.explanation.cnc-services.cnc-service.address
target.ip, target.asset.ip
Direct mapping from
alert.explanation.cnc-services.cnc-service.address
field
alert.explanation.cnc-services.cnc-service.port
target.port
Direct mapping from
alert.explanation.cnc-services.cnc-service.port
field
alert.explanation.cnc-services.cnc-service.url
target.url
Direct mapping from
alert.explanation.cnc-services.cnc-service.url
field
alert.explanation.malware-detected.malware.0.name
security_result.threat_name
Direct mapping from
alert.explanation.malware-detected.malware.0.name
field in case of multiple malware detection in array
alert.explanation.malware-detected.malware.md5sum
target.file.md5
Direct mapping from
alert.explanation.malware-detected.malware.md5sum
field
alert.explanation.malware-detected.malware.name
security_result.threat_name
Direct mapping from
alert.explanation.malware-detected.malware.name
field
alert.explanation.malware-detected.malware.sha1
target.file.sha1
Direct mapping from
alert.explanation.malware-detected.malware.sha1
field
alert.explanation.malware-detected.malware.sha256
target.file.sha256
Direct mapping from
alert.explanation.malware-detected.malware.sha256
field
alert.explanation.malware-detected.malware.url
target.url
Direct mapping from
alert.explanation.malware-detected.malware.url
field
alert.name
read_only_udm.metadata.product_event_type
Direct mapping from
alert.name
field
alert.occurred
read_only_udm.metadata.event_timestamp
Direct mapping from
alert.occurred
field
alert.src.domain
principal.hostname
Direct mapping from
alert.src.domain
field
alert.src.host
principal.hostname
Direct mapping from
alert.src.host
field
alert.src.ip
principal.ip, principal.asset.ip
Direct mapping from
alert.src.ip
field
alert.src.mac
principal.mac, principal.asset.mac
Direct mapping from
alert.src.mac
field
alert.src.port
principal.port
Direct mapping from
alert.src.port
field
alert.src.smtp-mail-from
network.email.from
Direct mapping from
alert.src.smtp-mail-from
field
alert.smtp-message.id
network.email.mail_id
Direct mapping from
alert.smtp-message.id
field
alert.smtp-message.subject
network.email.subject
Direct mapping from
alert.smtp-message.subject
field
client_ip
principal.ip
Direct mapping from
client_ip
field
client_src_port
principal.port
Direct mapping from
client_src_port
field
compression
additional.fields.value.string_value
Direct mapping from
compression
field
etag
additional.fields.value.string_value
Direct mapping from
etag
field
host
principal.hostname
Direct mapping from
host
field
log_id
read_only_udm.metadata.product_log_id
Direct mapping from
log_id
field
method
network.http.method
Direct mapping from
method
field
persistent_session_id
network.session_id
Direct mapping from
persistent_session_id
field
pool
additional.fields.value.string_value
Direct mapping from
pool
field
pool_name
additional.fields.value.string_value
Direct mapping from
pool_name
field
request_id
additional.fields.value.string_value
Direct mapping from
request_id
field
request_state
additional.fields.value.string_value
Direct mapping from
request_state
field
response_code
network.http.response_code
Direct mapping from
response_code
field
rewritten_uri_query
additional.fields.value.string_value
Direct mapping from
rewritten_uri_query
field
server_ip
target.ip
Direct mapping from
server_ip
field
server_name
target.hostname
Direct mapping from
server_name
field
server_src_port
target.port
Direct mapping from
server_src_port
field
service_engine
additional.fields.value.string_value
Direct mapping from
service_engine
field
ssl_cipher
network.tls.cipher
Direct mapping from
ssl_cipher
field
ssl_version
network.tls.version_protocol
Direct mapping from
ssl_version
field
uri_path
network.http.referral_url
Direct mapping from
uri_path
field
uri_query
additional.fields.value.string_value
Direct mapping from
uri_query
field
user_id
principal.user.userid
Direct mapping from
user_id
field
virtualservice
additional.fields.value.string_value
Direct mapping from
virtualservice
field
vs_name
additional.fields.value.string_value
Direct mapping from
vs_name
field
read_only_udm.metadata.event_type
Set to
SCAN_UNCATEGORIZED
if both principal and target IP addresses are present,
STATUS_UPDATE
if principal IP or hostname is present,
USER_UNCATEGORIZED
if principal user ID is present,
EMAIL_TRANSACTION
if both
alert.src.smtp-mail-from
and
alert.dst.smtp-to
are present, and
GENERIC_EVENT
otherwise.
read_only_udm.metadata.ingested_timestamp
Set to the current timestamp if
alert.attack-time
is not present.
read_only_udm.metadata.log_type
Set to
FIREEYE_NX
.
read_only_udm.metadata.vendor_name
Set to
FireEye
.
read_only_udm.network.application_protocol
Set to
HTTP
if the message contains "http" (case-insensitive).
read_only_udm.security_result.action
Set to
ALLOW
if
_source.action
is "notified" (case-insensitive),
BLOCK
if
_source.action
is "blocked" (case-insensitive), and
UNKNOWN_ACTION
otherwise.
read_only_udm.security_result.category
Set to
NETWORK_SUSPICIOUS
if
sec_category
contains "DOMAIN.MATCH" (case-insensitive),
NETWORK_MALICIOUS
if
sec_category
contains "INFECTION.MATCH" or "WEB.INFECTION" (case-insensitive),
SOFTWARE_MALICIOUS
if
sec_category
contains "MALWARE.OBJECT" (case-insensitive),
NETWORK_COMMAND_AND_CONTROL
if
sec_category
contains "MALWARE.CALLBACK" (case-insensitive), and
UNKNOWN_CATEGORY
otherwise.
read_only_udm.security_result.severity
Set to
MEDIUM
if
_source.severity
or
temp_severity
is "majr" (case-insensitive),
LOW
if
_source.severity
or
temp_severity
is "minr" (case-insensitive), and not set otherwise.
read_only_udm.security_result.summary
Set to the value of
security_result.threat_name
.
is_alert
Set to
true
.
is_significant
Set to
true
.
Need more help?
Get answers from Community members and Google SecOps professionals.
