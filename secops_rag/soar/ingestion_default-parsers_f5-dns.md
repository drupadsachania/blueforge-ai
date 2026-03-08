# Collect F5 DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dns/  
**Scraped:** 2026-03-05T09:55:29.192610Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 DNS logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 DNS logs to Google Security Operations using
Bindplane. The parser extracts fields from F5 DNS syslog messages using grok
patterns based on the application field, then maps them to the Unified Data Model
(UDM). It handles various F5 applications like
gtmd
,
mcpd
,
big3d
, and
others, parsing specific fields and setting the appropriate UDM event type,
severity, and descriptions based on the log level and application.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to F5 BIG-IP
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
directory on Linux or in the installation directory
on Windows.
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
'F5_DNS'
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
to the path where the
authentication file was saved in the
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
Configure a pool of remote logging servers
Sign in to the
F5 BIG-IP
web UI.
On the
Main
tab, go to
DNS
>
Delivery
>
Load Balancing
>
Pools or Local Traffic
>
Pools
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a unique name for the pool.
Using
New Members
setting:
Enter the Bindplane agent IP address in the
Address
field.
Enter the Bindplane agent port number in the
Service Port
field.
Click
Add
>
Finished
.
Configure the remote log destination
On the
Main
tab, go to
System
>
Logs
>
Configuration
>
Log Destinations
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a unique name for this destination.
Type
: Select
Remote High-Speed Log
.
Pool Name
: Select the pool of remote log servers to which you want the BIG-IP system to send log messages.
Protocol
: Select the protocol used.
Click
Finished
.
Creating a formatted remote log destination
On the
Main
tab, go to
System
>
Logs
>
Configuration
>
Log Destinations
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a unique name for this destination.
Type
: Select
Remote Syslog
.
Format
: Select the log format.
Forward To
: Select
High-Speed Log Destination
>
the destination that points to the pool of remote Syslog servers
.
Click
Finished
.
Configure Log Publisher
On the
Main
tab, go to
System
>
Logs
>
Configuration
>
Log Publishers
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a unique name for this publisher.
Destinations
: Select the newly-created destination for
Remote Syslog
from the
Available
list, and then 
click
keyboard_double_arrow_left
Move
to move the destination to the
Selected
list.
Click
Finished
.
Configure a custom DNS logging profile
On the
Main
tab, go to
DNS
>
Delivery
>
Profiles
>
Other
>
DNS Logging or Local Traffic
>
Profiles
>
Other
>
DNS Logging
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a unique name for this profile.
Log Publisher
: Select the newly-created destination to which the system
sends DNS log entries.
Log Queries
: Select the
Enabled
checkbox.
Log Responses
: Select the
Enabled
checkbox.
Include Query ID
: Select the
Enabled
checkbox.
Click
Finished
.
Add the DNS profile to the DNS Listener
On the
Main
tab, go to
DNS
>
Delivery
>
Listeners
>
select DNS listener
.
From the
DNS profile
in the
Service
section, select the
DNS profile
that you configured previously.
Click
Update
.
UDM mapping table
Log Field
UDM Mapping
Logic
application
principal.application
Directly mapped from the
application
field.
cipher_name
network.tls.cipher
Directly mapped from the
cipher_name
field.
command_line
principal.process.command_line
Directly mapped from the
command_line
field.
desc
security_result.description
Directly mapped from the
desc
field.
desc_icrd
security_result.description
Directly mapped from the
desc_icrd
field.
dest_ip
target.ip
Directly mapped from the
dest_ip
field.
dest_port
target.port
Directly mapped from the
dest_port
field.
file_path
principal.process.file.full_path
Directly mapped from the
file_path
field. Set to
true
if
level
is "alert", otherwise not present. Set to
true
if
level
is "alert", otherwise not present.
msg3
security_result.description
Directly mapped from the
msg3
field when
application
is "run-parts".
metadata.event_type
Set to
GENERIC_EVENT
if
event_type
is empty, otherwise mapped from
event_type
. Hardcoded to "DNS". Hardcoded to "F5".
principal_hostname
principal.hostname
Directly mapped from the
principal_hostname
field.
proc_id
principal.process.pid
Directly mapped from the
proc_id
field.
received_bytes
network.received_bytes
Directly mapped from the
received_bytes
field.
resource_id
target.resource.id
Directly mapped from the
resource_id
field.
resource_parent
principal.resource.parent
Directly mapped from the
resource_parent
field.
response_code
network.http.response_code
Directly mapped from the
response_code
field. Determined based on the
level
field.
src_ip
principal.ip
Directly mapped from the
src_ip
field.
src_port
principal.port
Directly mapped from the
src_port
field.
tls_version
network.tls.version
Directly mapped from the
tls_version
field.
userName
principal.user.userid
Directly mapped from the
userName
field.
when
event.timestamp
Calculated from
datetime1
and
timezone
or
datetime
and
timezone
.
Need more help?
Get answers from Community members and Google SecOps professionals.
