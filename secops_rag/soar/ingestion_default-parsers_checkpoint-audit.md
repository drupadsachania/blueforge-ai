# Collect Check Point Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-audit/  
**Scraped:** 2026-03-05T09:51:52.763279Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Check Point Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Check Point Audit logs to
Google Security Operations using Bindplane. The parser extracts fields from Check
Point firewall audit logs in SYSLOG or CEF format, performs data transformations
and mapping, and structures the output into the Google Security Operations Unified
Data Model (UDM) for security analytics. It specifically handles user
login-logout events, status updates, and enriches the data with additional
context from the logs.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Check Point Appliance
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
'CHECKPOINT_AUDIT'
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
Configure Syslog in Check Point
Sign in to the
Checkpoint Management Console
.
Go to
Logs and Monitoring
>
Log Export
.
Click
Add
.
Choose
Syslog
as the
export type
.
Provide the following configuration details:
Name
: Enter a name for your configuration (for example,
Google SecOps Export
).
Destination
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Log Export
: Select
Audit Logs
or
All
.
Syslog Format
: Select
RFC 3164
or
RFC 5424
.
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
act
read_only_udm.security_result.action
Value from
act
field in the raw log.
additional_info
read_only_udm.security_result.description
Value from
additional_info
field in the raw log.
administrator
read_only_udm.target.user.user_display_name
Value from
administrator
field in the raw log.
comment
read_only_udm.additional.fields.value.string_value
Value from
comment
field in the raw log. The key is hardcoded as
comment
.
deviceDirection
read_only_udm.network.direction
If
deviceDirection
=1 then OUTBOUND else INBOUND.
ifname
read_only_udm.additional.fields.value.string_value
Value from
ifname
field in the raw log. The key is hardcoded as
ifname
.
loguid
read_only_udm.metadata.product_log_id
Value from
loguid
field in the raw log.
log_sys_message
read_only_udm.metadata.description
Value from
log_sys_message
field in the raw log.
msg
read_only_udm.metadata.description
Value from
msg
field in the raw log.
operation
read_only_udm.security_result.action_details
Value from
operation
field in the raw log.
origin
read_only_udm.intermediary.ip
Value from
origin
field in the raw log.
originsicname
read_only_udm.additional.fields.value.string_value
Value from
originsicname
field in the raw log. The key is hardcoded as
originsicname
.
outcome
read_only_udm.security_result.outcomes.value
Value from
outcome
field in the raw log. The key is hardcoded as
outcome
.
product
read_only_udm.metadata.product_name
Value from
product
field in the raw log.
rt
read_only_udm.metadata.event_timestamp.seconds
Value from
rt
field in the raw log, converted to seconds.
sendtotrackerasadvancedauditlog
read_only_udm.additional.fields.value.string_value
Value from
sendtotrackerasadvancedauditlog
field in the raw log. The key is hardcoded as
sendtotrackerasadvancedauditlog
.
sequencenum
read_only_udm.additional.fields.value.string_value
Value from
sequencenum
field in the raw log. The key is hardcoded as
sequencenum
.
session_uid
read_only_udm.additional.fields.value.string_value
Value from
session_uid
field in the raw log. The key is hardcoded as
session_uid
.
sntdom
read_only_udm.principal.administrative_domain
Value from
sntdom
field in the raw log.
src
read_only_udm.principal.ip
Value from
src
field in the raw log.
subject
read_only_udm.security_result.summary
Value from
subject
field in the raw log.
update_service
read_only_udm.additional.fields.value.string_value
Value from
update_service
field in the raw log. The key is hardcoded as
update_service
.
version
read_only_udm.additional.fields.value.string_value
Value from
version
field in the raw log. The key is hardcoded as
version
.
N/A
read_only_udm.metadata.event_type
If
host
field exists in the raw log, then
STATUS_UPDATE
. If
operation
field equals to
Log Out
then
USER_LOGOUT
. If
operation
field equals to
Log In
then
USER_LOGIN
. Otherwise
GENERIC_EVENT
.
N/A
read_only_udm.metadata.vendor_name
Hardcoded value:
Check Point
.
N/A
read_only_udm.metadata.product_version
Hardcoded value:
Check Point
.
N/A
read_only_udm.metadata.product_event_type
Hardcoded value:
[Log] - Log
.
N/A
read_only_udm.metadata.log_type
Hardcoded value:
CHECKPOINT_FIREWALL
.
N/A
read_only_udm.principal.hostname
Value from
host
field in the raw log.
N/A
read_only_udm.principal.asset.hostname
Value from
host
field in the raw log.
N/A
read_only_udm.extensions.auth.type
If
operation
field equals to
Log Out
or
Log In
then
AUTHTYPE_UNSPECIFIED
.
N/A
read_only_udm.extensions.auth.mechanism
If
operation
field equals to
Log Out
or
Log In
then
MECHANISM_UNSPECIFIED
.
Need more help?
Get answers from Community members and Google SecOps professionals.
