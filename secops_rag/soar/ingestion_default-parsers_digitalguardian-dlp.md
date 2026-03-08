# Collect Fortra Digital Guardian DLP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-dlp/  
**Scraped:** 2026-03-05T09:56:28.990500Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortra Digital Guardian DLP logs
Supported in:
Google secops
SIEM
This document explains how to collect Fortra Digital Guardian DLP logs to Google Security Operations using a Bindplane agent. The parser code transforms raw JSON formatted logs into a unified data model (UDM). It first extracts fields from the raw JSON, performs data cleaning and normalization, then maps the extracted fields to their corresponding UDM attributes, enriching the data with specific event types based on the identified activity.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Fortra Digital Guardian DLP.
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
DIGITALGUARDIAN_DLP
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
Configure Fortra Digital Guardian Syslog Export
Sign in to the
Digital Guardian Management Console
.
Go to
Workspace
>
Data Export
>
Create Export
.
Select
Alerts
or
Events
as the data source from the
Data Sources
list.
Select
Syslog
as the Export Type.
From the
Type list
, select
UDP
(you can also select TCP as the transport protocol, depending on your Bindplane configuration).
Under the
Server
field, enter the Bindplane agent IP address.
In the
Port
field, enter
514
(you can provide another port, depending on your Bindplane agent configuration).
Select a severity level, from the
Severity Level
list.
Select the
Is Active
checkbox.
Click
Next
.
From the list of available fields, add
All
Alert and Event fields for the data export.
Select
Criteria
for the fields in your data export.
Click
Next
.
Select a
Group
for the criteria.
Click
Next
.
Click
Test Query
.
Click
Next
.
Click
Save
.
Supported Fortra Digital Guardian DLP sample logs
JSON format (event: network transfer)
{
"Server Process Time"
:
1667425746701
,
"Unique ID"
:
"00000000-0000-0000-0000-000000000000"
,
"Event End Time"
:
"2022-11-02 09:26:27 PM"
,
"Application"
:
"msedge.exe"
,
"Machine ID"
:
"machine-id-placeholder"
,
"Computer Name"
:
"ORGANIZATION\\WORKSTATION-01"
,
"Machine Type"
:
"Windows"
,
"MAC Address"
:
"00:00:00:00:00:00"
,
"Operation Type"
:
"Network Transfer Download"
,
"DNS Hostname"
:
"download.external.com"
,
"IP Address"
:
"192.0.2.1"
,
"Network Direction"
:
"Outbound"
,
"Protocol"
:
"HTTP"
,
"Remote Port"
:
"443"
,
"User"
:
"dummy_user"
,
"Process PID"
:
13460
,
"Source File Name"
:
"update.js"
,
"Source IP Address"
:
"198.51.100.1"
,
"Destination File Path"
:
"C:\\Users\\dummy_user\\Downloads\\log.old"
,
"Command Line"
:
"\"C:\\Program Files (x86)\\Browser\\msedge.exe\" --profile-directory=Default"
,
"Agent Version"
:
"7.7.0.0635"
,
"_time"
:
1667425746701
}
SYSLOG + XML format (event: message classification)
<110>1
2026-02-09T14:23:00.00Z
HOST-ABC-01
TMC
-
2200
-
<Event
DateTime="2026-02-09T14:23:00.000Z"
EventId="2200"
EventType="CustomXHeader"
User="sanitized_user"
Machine="HOST-ABC-01"
IPV4="10.0.0.50"
Source="TMC"
Subject="Project
Alpha
[Internal]"
Sender="user@example.com"
ProductName="Titus
Message
Classification">
<Metadata>
<Classification
value="INTERNAL"
/>
</Metadata>
<Recipients>
<Recipient
RecipientType="TO"
Name="John
Doe"
Address="recipient@example.com"
/>
</Recipients>
</Event>
CEF format (identified from change log)
CEF
:
0
|
Fortra
|
Digital
Guardian
|
7.7
.
0
|
100
|
File
Exfiltration
|
5
|
src
=
10.0
.
0.25
dst
=
192.168
.
1.100
suser
=
employee_name
msg
=
User
attempted
to
move
sensitive
document
to
USB
drive
shost
=
endpoint
-
04
sproc
=
explorer
.
exe
UDM mapping table
Log field
UDM mapping
logic
Agent Version
observer.platform_version
Directly mapped from raw log field
Agent Version
.
Application
principal.process.command_line
Directly mapped from raw log field
Application
if not empty.
Command Line
target.process.command_line
Directly mapped from raw log field
Command Line
.
Company Name
principal.user.company_name
Directly mapped from raw log field
Company Name
.
Computer Name
principal.hostname
Directly mapped from raw log field
Computer Name
.
DNS Hostname
target.asset.hostname
Directly mapped from raw log field
DNS Hostname
.
Destination Drive Type
about.labels.value
Directly mapped from raw log field
Destination Drive Type
. The corresponding key is set to
Destination Drive Type
.
Destination File Extension
target.file.mime_type
Directly mapped from raw log field
Destination File Extension
if it's not
no extension
or
[no extension]
.
Destination File Path
target.file.full_path
Directly mapped from raw log field
Destination File Path
.
Device GUID
src.resource.id
Mapped from raw log field
Device GUID
with prefix
GUID:
.
Email Sender
network.email.from
Directly mapped from raw log field
Email Sender
if not empty.
Email Subject
network.email.subject
Directly mapped from raw log field
Email Subject
if
Email Sender
is not empty.
Event Display Name
target.resource.type
Directly mapped from raw log field
Event Display Name
.
Event Time
metadata.event_timestamp.seconds
Converted to timestamp from raw log field
Event Time
using formats
yyyy-MM-dd HH:mm:ss A
and
TIMESTAMP_ISO8601
.
File Description
metadata.description
Directly mapped from raw log field
File Description
.
File Size
about.labels.value
Directly mapped from raw log field
File Size
. The corresponding key is set to
File Size
.
File Version
about.labels.value
Directly mapped from raw log field
File Version
. The corresponding key is set to
File Version
.
IP Address
principal.ip
Directly mapped from raw log field
IP Address
if
Source IP Address
is empty.
Local Port
principal.port
Directly mapped from raw log field
Local Port
if not empty and converted to integer.
MAC Address
target.mac
Directly mapped from raw log field
MAC Address
if not empty.
Machine ID
principal.asset.asset_id
Mapped from raw log field
Machine ID
with prefix
MachineId:
.
Machine Type
principal.asset.category
Directly mapped from raw log field
Machine Type
.
MD5 Hash
target.process.file.md5
Directly mapped from raw log field
MD5 Hash
after converting to lowercase.
Network Direction
network.direction
Mapped from raw log field
Network Direction
. If
Inbound
, set to
INBOUND
. If
Outbound
, set to
OUTBOUND
.
Operation Type
security_result.action_details
Directly mapped from raw log field
Operation Type
.
Parent Application
principal.process.parent_process.command_line
Directly mapped from raw log field
Parent Application
if not empty.
Parent MD5 Hash
target.process.parent_process.file.md5
Directly mapped from raw log field
Parent MD5 Hash
after converting to lowercase if it matches a hexadecimal string pattern.
Process Domain
target.administrative_domain
Directly mapped from raw log field
Process Domain
.
Process File Extension
target.process.file.mime_type
Directly mapped from raw log field
Process File Extension
if it's not
no extension
or
[no extension]
.
Process Path
target.process.file.full_path
Directly mapped from raw log field
Process Path
.
Process PID
principal.process.pid
Directly mapped from raw log field
Process PID
after converting to string.
Product Name
metadata.product_name
Directly mapped from raw log field
Product Name
.
Product Version
metadata.product_version
Directly mapped from raw log field
Product Version
.
Protocol
network.application_protocol
If
HTTP
or
HTTPS
, set to
HTTPS
.
Printer Name
src.resource.name
Directly mapped from raw log field
Printer Name
.
Remote Port
target.port
Directly mapped from raw log field
Remote Port
if not empty and converted to integer.
SHA1 Hash
target.process.file.sha1
Directly mapped from raw log field
SHA1 Hash
after converting to lowercase.
SHA256 Hash
target.process.file.sha256
Directly mapped from raw log field
SHA256 Hash
after converting to lowercase.
Signature Issuer
network.tls.server.certificate.issuer
Directly mapped from raw log field
Signature Issuer
.
Signature Subject
network.tls.server.certificate.subject
Directly mapped from raw log field
Signature Subject
.
Source File Extension
src.file.mime_type
Directly mapped from raw log field
Source File Extension
if it's not
no extension
or
[no extension]
.
Source File Path
src.file.full_path
Directly mapped from raw log field
Source File Path
.
Source IP Address
principal.ip
Directly mapped from raw log field
Source IP Address
if not empty.
Total Size
about.labels.value
Directly mapped from raw log field
Total Size
. The corresponding key is set to
Total Size
.
URL Path
target.url
Directly mapped from raw log field
URL Path
.
Unique ID
metadata.product_log_id
Directly mapped from raw log field
Unique ID
.
User
principal.user.userid
Directly mapped from raw log field
User
.
Was Detail Blocked
security_result.action
If
Yes
, set to
BLOCK
. If
No
, set to
ALLOW
.
dg_dst_dev.dev_prdname
target.asset.hardware.model
Directly mapped from raw log field
dg_dst_dev.dev_prdname
.
dg_dst_dev.dev_sernum
target.asset.hardware.serial_number
Directly mapped from raw log field
dg_dst_dev.dev_sernum
.
dg_recipients.uad_mr
network.email.to
Directly mapped from raw log field
dg_recipients.uad_mr
if it matches an email address pattern.
dg_src_dev.dev_prdname
principal.asset.hardware.model
Directly mapped from raw log field
dg_src_dev.dev_prdname
.
dg_src_dev.dev_sernum
principal.asset.hardware.serial_number
Directly mapped from raw log field
dg_src_dev.dev_sernum
.
metadata.event_type
metadata.event_type
Set to
GENERIC_EVENT
initially. Changed based on specific conditions:
-
NETWORK_HTTP
: if hostname, HTTP/HTTPS protocol, and MAC address are present.
-
FILE_COPY
: if destination and source file paths exist and
Operation Type
is
File Copy
.
-
FILE_MOVE
: if destination and source file paths exist and
Operation Type
is
File Move
.
-
FILE_UNCATEGORIZED
: if destination file path, process path/command line exist, and
Operation Type
contains
File
.
-
USER_LOGOUT
: if user ID exists and
Operation Type
contains
Logoff
.
-
USER_LOGIN
: if user ID exists and
Operation Type
contains
Logon
.
-
NETWORK_UNCATEGORIZED
: if process path/command line, process ID, outbound network direction, and MAC address are present.
-
SCAN_PROCESS
: if process path/command line and process ID are present.
-
PROCESS_UNCATEGORIZED
: if process path/command line exists.
metadata.log_type
metadata.log_type
Set to
DIGITALGUARDIAN_DLP
.
metadata.product_log_id
metadata.product_log_id
Directly mapped from raw log field
Unique ID
.
metadata.product_name
metadata.product_name
Directly mapped from raw log field
Product Name
.
metadata.product_version
metadata.product_version
Directly mapped from raw log field
Product Version
.
metadata.vendor_name
metadata.vendor_name
Set to
DigitalGuardian
.
network.application_protocol
network.application_protocol
Set to
HTTPS
if
Protocol
is
HTTP
or
HTTPS
.
network.direction
network.direction
Mapped from raw log field
Network Direction
. If
Inbound
, set to
INBOUND
. If
Outbound
, set to
OUTBOUND
.
network.email.from
network.email.from
Directly mapped from raw log field
Email Sender
if not empty.
network.email.subject
network.email.subject
Directly mapped from raw log field
Email Subject
if
Email Sender
is not empty.
network.email.to
network.email.to
Directly mapped from raw log field
dg_recipients.uad_mr
if it matches an email address pattern.
network.tls.server.certificate.issuer
network.tls.server.certificate.issuer
Directly mapped from raw log field
Signature Issuer
.
network.tls.server.certificate.subject
network.tls.server.certificate.subject
Directly mapped from raw log field
Signature Subject
.
observer.platform_version
observer.platform_version
Directly mapped from raw log field
Agent Version
.
principal.asset.asset_id
principal.asset.asset_id
Mapped from raw log field
Machine ID
with prefix
MachineId:
.
principal.asset.category
principal.asset.category
Directly mapped from raw log field
Machine Type
.
principal.asset.hardware.model
principal.asset.hardware.model
Directly mapped from raw log field
dg_src_dev.dev_prdname
.
principal.asset.hardware.serial_number
principal.asset.hardware.serial_number
Directly mapped from raw log field
dg_src_dev.dev_sernum
.
principal.hostname
principal.hostname
Directly mapped from raw log field
Computer Name
.
principal.ip
principal.ip
Directly mapped from raw log field
Source IP Address
if not empty. Otherwise, mapped from
IP Address
if not empty.
principal.port
principal.port
Directly mapped from raw log field
Local Port
if not empty and converted to integer.
principal.process.command_line
principal.process.command_line
Directly mapped from raw log field
Application
if not empty.
principal.process.parent_process.command_line
principal.process.parent_process.command_line
Directly mapped from raw log field
Parent Application
if not empty.
principal.process.parent_process.file.md5
principal.process.parent_process.file.md5
Directly mapped from raw log field
Parent MD5 Hash
after converting to lowercase if it matches a hexadecimal string pattern.
principal.process.pid
principal.process.pid
Directly mapped from raw log field
Process PID
after converting to string.
principal.user.company_name
principal.user.company_name
Directly mapped from raw log field
Company Name
.
principal.user.userid
principal.user.userid
Directly mapped from raw log field
User
.
security_result.action
security_result.action
If
Was Detail Blocked
is
Yes
, set to
BLOCK
. If
Was Detail Blocked
is
No
, set to
ALLOW
.
security_result.action_details
security_result.action_details
Directly mapped from raw log field
Operation Type
.
src.file.full_path
src.file.full_path
Directly mapped from raw log field
Source File Path
.
src.file.mime_type
src.file.mime_type
Directly mapped from raw log field
Source File Extension
if it's not
no extension
or
[no extension]
.
src.resource.id
src.resource.id
Mapped from raw log field
Device GUID
with prefix
GUID:
.
src.resource.name
src.resource.name
Directly mapped from raw log field
Printer Name
.
target.administrative_domain
target.administrative_domain
Directly mapped from raw log field
Process Domain
.
target.asset.hardware.model
target.asset.hardware.model
Directly mapped from raw log field
dg_dst_dev.dev_prdname
.
target.asset.hardware.serial_number
target.asset.hardware.serial_number
Directly mapped from raw log field
dg_dst_dev.dev_sernum
.
target.asset.hostname
target.asset.hostname
Directly mapped from raw log field
DNS Hostname
.
target.asset.product_object_id
target.asset.product_object_id
Directly mapped from raw log field
Adapter Name
.
target.file.full_path
target.file.full_path
Directly mapped from raw log field
Destination File Path
.
target.file.mime_type
target.file.mime_type
Directly mapped from raw log field
Destination File Extension
if it's not
no extension
or
[no extension]
.
target.mac
target.mac
Directly mapped from raw log field
MAC Address
if not empty.
target.port
target.port
Directly mapped from raw log field
Remote Port
if not empty and converted to integer.
target.process.command_line
target.process.command_line
Directly mapped from raw log field
Command Line
.
target.process.file.full_path
target.process.file.full_path
Directly mapped from raw log field
Process Path
.
target.process.file.md5
target.process.file.md5
Directly mapped from raw log field
MD5 Hash
after converting to lowercase.
target.process.file.mime_type
target.process.file.mime_type
Directly mapped from raw log field
Process File Extension
if it's not
no extension
or
[no extension]
.
target.process.file.sha1
target.process.file.sha1
Directly mapped from raw log field
SHA1 Hash
after converting to lowercase.
target.process.file.sha256
target.process.file.sha256
Directly mapped from raw log field
SHA256 Hash
after converting to lowercase.
target.process.parent_process.command_line
target.process.parent_process.command_line
Directly mapped from raw log field
Parent Application
if not empty.
target.process.parent_process.file.md5
target.process.parent_process.file.md5
Directly mapped from raw log field
Parent MD5 Hash
after converting to lowercase if it matches a hexadecimal string pattern.
target.resource.type
target.resource.type
Directly mapped from raw log field
Event Display Name
.
target.url
target.url
Directly mapped from raw log field
URL Path
.
extensions.auth.type
extensions.auth.type
Set to
AUTHTYPE_UNSPECIFIED
if
Operation Type
is
User Logoff
or
User Logon
.
Need more help?
Get answers from Community members and Google SecOps professionals.
