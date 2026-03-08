# Collect Symantec VIP Enterprise Gateway logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip/  
**Scraped:** 2026-03-05T09:28:47.943618Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec VIP Enterprise Gateway logs
Supported in:
Google secops
SIEM
This document explains how to ingest Symantec VIP Enterprise Gateway logs to
Google Security Operations using Bindplane. The parser code first attempts to process
the input log message as a JSON object. If this fails, it assumes a syslog format
and uses regular expressions (grok patterns) to extract relevant fields like
timestamps, IP addresses, usernames, and event descriptions. Finally, it maps
the extracted information to the Unified Data Model (UDM) fields for standardized
security event representation.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Symantec VIP Enterprise Gateway
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
'SYMANTEC_VIP'
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
to the path where the
authentication file was saved in the
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
Configure Syslog in Symantec VIP Enterprise Gateway
Sign in to your
Symantec VIP Gateway
web UI.
Go to
Logs
>
Syslog Configuration
.
If you are configuring Syslog for the first time, you are prompted to configure the Syslog settings. Select
Yes
.
If you have already configured Syslog, click
Edit
at the bottom of the page.
Provide the following configuration details:
Syslog Facility
: Select
LOG_LOCAL0
.
Syslog Host
: Enter the Bindplane agent IP address.
Syslog Port
: Enter the Bindplane agent port number (for example,
514
for
UDP
).
Click
Save
.
Go to
Settings
>
Console Settings
.
Provide the following configuration details:
Logging Level
: Select
Info
.
Enable Syslog
: Select
Yes
.
Click
Submit
.
Go to
Settings
>
Health Check Settings
.
Select
Yes
to enable the Health Check Service.
Provide the following configuration details:
Logging Level
: Select
Info
.
Enable Syslog
: Select
Yes
.
Click
Submit
.
Go to
User Store
>
LDAP Directory Synchronization
.
Edit the following configuration details:
Log Level
: Select
Info
.
Enable Syslog
: Select
Yes
.
Click
Submit
.
UDM mapping table
Log field
UDM mapping
Logic
application
read_only_udm.principal.application
Value taken from
application
field extracted by json filter.
command
read_only_udm.target.process.command_line
Value taken from
command
field extracted by grok pattern.
credentialType
This field is not directly mapped to the UDM. It is used to derive the value of read_only_udm.extensions.auth.mechanism.
data
This field is not directly mapped to the UDM. It is parsed to extract other fields.
data2
This field is not directly mapped to the UDM. It is parsed to extract other fields.
datetime
read_only_udm.metadata.event_timestamp.seconds
read_only_udm.metadata.event_timestamp.nanos
Seconds and nanoseconds since epoch extracted from the
datetime
field.
desc
read_only_udm.metadata.description
Value taken from
desc
field extracted by json filter.
description
read_only_udm.security_result.description
Value taken from
description
field extracted by json filter.
filename
read_only_udm.target.process.file.full_path
Value taken from
filename
field extracted by grok pattern.
hostname
read_only_udm.principal.hostname
Value taken from
hostname
field extracted by json filter.
host_name
read_only_udm.intermediary.hostname
Value taken from
host_name
field extracted by json filter.
log_level
This field is not directly mapped to the UDM. It is used to derive the value of read_only_udm.security_result.severity.
log_type
read_only_udm.metadata.product_event_type
Value taken from
log_type
field extracted by json filter.
msg
This field is not directly mapped to the UDM. It is parsed to extract other fields.
operation
read_only_udm.security_result.summary
Value taken from
operation
field extracted by grok pattern.
processid
read_only_udm.target.process.pid
Value taken from
processid
field extracted by grok pattern.
product
read_only_udm.metadata.product_name
Value taken from
product
field extracted by json filter.
reason
read_only_udm.metadata.description
Value taken from
reason
field extracted by grok pattern.
request_id
read_only_udm.target.resource.id
Value taken from
request_id
field extracted by grok pattern.
src_ip
read_only_udm.principal.ip
Value taken from
src_ip
field extracted by grok pattern.
status
read_only_udm.metadata.description
Value taken from
status
field extracted by grok pattern.
summary
read_only_udm.security_result.summary
Value taken from
summary
field extracted by json filter.
timestamp.nanos
read_only_udm.metadata.event_timestamp.nanos
Nanoseconds from the original log timestamp.
timestamp.seconds
read_only_udm.metadata.event_timestamp.seconds
Seconds from the original log timestamp.
time
This field is not directly mapped to the UDM. It is used to derive the values of read_only_udm.metadata.event_timestamp.seconds and read_only_udm.metadata.event_timestamp.nanos.
user
read_only_udm.target.user.userid
Value taken from
user
field extracted by json filter or grok pattern.
vendor
read_only_udm.metadata.vendor_name
Value taken from
vendor
field extracted by json filter.
read_only_udm.extensions.auth.mechanism
Determined by the
credentialType
field. If
credentialType
is
SMS_OTP
or
STANDARD_OTP
, then
OTP
is used. If
credentialType
matches the regular expression
PASSWORD
, then
USERNAME_PASSWORD
is used.
read_only_udm.extensions.auth.type
If the
reason
field matches the regular expression
LDAP
, then
SSO
is used. Otherwise,
AUTHTYPE_UNSPECIFIED
is used.
read_only_udm.metadata.event_type
Determined by the presence of certain fields. If
user
or
processid
is not empty, then
USER_LOGIN
is used. If
user
is empty and
src_ip
is not empty or
0.0.0.0
, then
STATUS_UPDATE
is used. Otherwise,
GENERIC_EVENT
is used.
read_only_udm.metadata.log_type
Hardcoded to
SYMANTEC_VIP
.
read_only_udm.security_result.action
Determined by the
status
field. If
status
is
Authentication Success
,
GRANTED
,
Authentication Completed
,
After Services Authenticate call
, or
CHALLENGED
, then
ALLOW
is used. If
status
is
DENIED
,
Acces-Reject
,
Unknown Error
,
Service Unavailable
, or
FAILED
, then
BLOCK
is used. If
status
is
PUSH request sent for user
or
Trying to fetch attribute
, then
QUARANTINE
is used.
read_only_udm.security_result.severity
Determined by the
log_level
field. If
log_level
is
DEBUG
,
INFO
, or
AUDIT
, then
INFORMATIONAL
is used. If
log_level
is
ERROR
, then
ERROR
is used. If
log_level
is
WARNING
, then
MEDIUM
is used.
Need more help?
Get answers from Community members and Google SecOps professionals.
