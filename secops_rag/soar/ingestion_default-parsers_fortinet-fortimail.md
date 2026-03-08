# Collect Fortinet FortiMail logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimail/  
**Scraped:** 2026-03-05T09:56:20.921265Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiMail logs
Supported in:
Google secops
SIEM
This document explains how to collect Fortinet FortiMail logs by using Bindplane. The parser extracts key-value pairs, normalizes various fields like timestamps and IP addresses, and maps them into a unified data model (UDM) for Google Security Operations, categorizing the event type based on the available information.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Fortinet Fortimail.
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
```
yaml
receivers
:
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:5252"
exporters
:
chronicle
/
chronicle_w_labels
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
malachiteingestion
-
pa
.
googleapis
.
com
# Add optional ingestion labels for better organization
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
fortinet_fortimail
raw_log_field
:
body
service
:
pipelines
:
logs
/
source0__chronicle_w_labels
-
0
:
receivers
:
-
udplog
exporters
:
-
chronicle
/
chronicle_w_labels
```
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
Configure Fortinet FortiMail syslog
Sign in to the FortiMail device web interface.
Select
Log & Report
>
Log Settings
>
Remote
.
Click
New
to create a new entry.
In a dialog that appears, select
Enable
to allow logging to a remote host.
Provide the following details:
Name
: enter a unique and meaningful name.
Server name/IP
: enter the
Bindplane
IP address.
Server port
: enter the
Bindplane
UDP port number.
Level
: select
Information
as severity level.
Facility
: enter a unique facility identifier and verify that no other network devices use the same facility identifier.
Deselect CSV format.
Log protocol
: select
Syslog
.
Logging policy configuration
: enable all types of events or logs to be forwarded.
Click
Create
.
UDM Mapping Table
Log field
UDM mapping
Logic
authid
read_only_udm.target.user.email_addresses
If
authid
field contains
@
then map to this field
authid
read_only_udm.target.user.userid
Map
authid
field to this field
cipher
read_only_udm.network.tls.cipher
Map
cipher
field to this field
client_ip
read_only_udm.principal.ip
Map
client_ip
field to this field
client_name
read_only_udm.principal.hostname
Map
client_name
field to this field
detail
read_only_udm.security_result.summary
Map
detail
field to this field
device_id
read_only_udm.principal.resource.id
Map
device_id
field to this field
devname
read_only_udm.principal.resource.name
Map
devname
field to this field
direction
read_only_udm.network.direction
If
direction
field is equal to
out
then map value
OUTBOUND
, if
direction
field is equal to
in
then map value
INBOUND
, else map value
UNKNOWN_DIRECTION
disposition
read_only_udm.security_result.detection_fields.value
Map
disposition
field to this field, when key field is equal to
Disposition
domain
read_only_udm.principal.administrative_domain
Map
domain
field to this field
dst_ip
read_only_udm.target.ip
Map
dst_ip
field to this field
from
read_only_udm.network.email.from
If
from
field contains
@
then map to this field
log_id
read_only_udm.metadata.product_log_id
Map
log_id
field to this field
message_id
read_only_udm.network.email.mail_id
Map
message_id
field to this field
message_length
read_only_udm.additional.fields.value.number_value
Map
message_length
field to this field, when key field is equal to
message_length
msg
read_only_udm.security_result.description
Map
msg
field to this field
polid
read_only_udm.security_result.detection_fields.value
Map
polid
field to this field, when key field is equal to
Polid
relay
read_only_udm.intermediary.ip
Map
relay
field to this field
resolved
read_only_udm.security_result.detection_fields.value
Map
resolved
field to this field, when key field is equal to
Resolved
session_id
read_only_udm.network.session_id
Map
session_id
field to this field
src_type
read_only_udm.additional.fields.value.string_value
Map
src_type
field to this field, when key field is equal to
src_type
stat
read_only_udm.metadata.description
Map
stat
field to this field
subject
read_only_udm.network.email.subject
Map
subject
field to this field
to
read_only_udm.network.email.to
If
to
field contains
@
then map to this field
user
read_only_udm.principal.user.userid
Map
user
field to this field
N/A
read_only_udm.extensions.auth.mechanism
The value of this field is hardcoded in the parser code as
USERNAME_PASSWORD
when
authid
field exists
N/A
read_only_udm.extensions.auth.type
The value of this field is hardcoded in the parser code as
AUTHTYPE_UNSPECIFIED
when
authid
field exists
N/A
read_only_udm.metadata.event_type
The value of this field is determined by the parser logic based on a combination of available fields. If
from
field exists then the value is
EMAIL_TRANSACTION
, else if
to
field exists then the value is
EMAIL_UNCATEGORIZED
, else if both
client_ip
and
dst_ip
fields exist then the value is
NETWORK_CONNECTION
, else if
authid
field exists then the value is
USER_LOGIN
, else if
user
field exists then the value is
USER_UNCATEGORIZED
, else if
client_ip
field exists then the value is
STATUS_UPDATE
, else the value is
GENERIC_EVENT
N/A
read_only_udm.metadata.log_type
The value of this field is hardcoded in the parser code as
FORTINET_FORTIMAIL
N/A
read_only_udm.metadata.product_name
The value of this field is hardcoded in the parser code as
FORTINET_FORTIMAIL
N/A
read_only_udm.metadata.vendor_name
The value of this field is hardcoded in the parser code as
FORTINET
N/A
read_only_udm.principal.resource.resource_type
The value of this field is hardcoded in the parser code as
DEVICE
Need more help?
Get answers from Community members and Google SecOps professionals.
