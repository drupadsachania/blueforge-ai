# Collect F5 AFM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-afm/  
**Scraped:** 2026-03-05T09:23:58.165759Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 AFM logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 Advanced Firewall Management logs to
Google Security Operations using Bindplane. The parser transforms the logs from
either SYSLOG and CSV or CSV formats into a Unified Data Model (UDM). It first
attempts to parse the log message using grok patterns specific to the SYSLOG
format and if unsuccessful, processes it as a CSV file, extracting and mapping
fields to the UDM structure.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to F5 BIG-IP and F5 Advanced Firewall Management
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
Configure the Bindplane Agent to ingest Syslog and send to Google SecOps
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:5145"
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
ingestion_labels
:
log_type
:
'F5_AFM'
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
tcplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual Customer ID.
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
Enable F5 BIG-IP Advanced Firewall Manager
Sign in to the
BIG-IP appliance
management console.
Go to
System
>
License
.
Verify that the
Advanced Firewall Manager
is
licensed
and
enabled
.
To enable the
Advanced Firewall Manager
, go to
System
>
Resource
>
Provisioning
.
Select the checkbox From the
Provisioning column
and select
Nominal
from the list.
Click
Submit
.
Configure Logging Pool in F5 AFM
Go to
Local Traffic
>
Pools
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a name for the logging pool (for example,
logging_pool
).
Health Monitor
: In the
Available
list, select
TCP
and click
<<
.
In the
Resource
tab, select the
Logging Pool
you created earlier from the
Node Name
list.
In the
Address
field, enter the Bindplane agent IP address.
In the
Service Port
field, enter
5145
or other port as you defined in the Bindplane agent.
Click
Add
.
Click
Finish
.
Configure the formatted log destination in F5 AFM
Go to
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
: Enter a name for the logging format destination (for example,
Logging_Format_Destination
).
Description
: Enter a description.
Type
: Select
Remote Syslog
.
Syslog Format
: Select
Syslog
.
High-Speed Log Destination
: Select your high-speed logging destination (for example,
Logging_HSL_Destination
).
Click
Finished
.
Configure Log Publisher in F5 AFM
Go to
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
: Enter a name for the publisher (for example,
Log_Publisher
).
Description
: Enter a description.
Destinations
: Select the
log destination name
that you created in the
Configure Logging Pool in F5 AFM
step and click
<<
to add items to the
Selected
list.
Configure Logging Profile in F5 AFM
Go to
Security
>
Event Logs
>
Logging Profile
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a name for the log profile (for example,
Logging_Profile
).
Network Firewall
: Select the
Enabled
checkbox.
Publisher
: Select the
log publisher
that you configured earlier (for example,
Log_Publisher
).
Log Rule Matches
: Select the
Accept, Drop, and Reject
checkboxes.
Log IP Errors
: Select the
Enabled
checkbox.
Log TCP Errors
: Select the
Enabled
checkbox.
Log TCP Events
: Select the
Enabled
checkbox.
Storage Format
: Select
Field-List
.
Delimiter
: Enter
,
(comma) as the delimiter for events.
Storage Options
: Select
all of the options
in the
Available Items
list and click
<<
.
In the
IP Intelligence
tab, select the
log publisher
that you configured (for example,
Log_Publisher
).
Click
Finished
.
Configure Virtual Server Profile Association in F5 AFM
Go to
Local Traffic
>
Virtual Servers
.
Select the
virtual server
to modify.
Go to the
Security tab
>
Policies
.
From the
Log Profile
list, select
Enabled
.
From the
Profile
field, select
Logging_Profile
and click
<<
.
Click
Update
.
UDM mapping table
Log field
UDM mapping
Logic
acl_policy_name
security_result.detection_fields.acl_policy_name
Value of column22 if the log format is SYSLOG, else value of column13
acl_policy_type
security_result.detection_fields.acl_policy_type
Value of column21 if the log format is SYSLOG, else value of column18
acl_rule_name
security_result.rule_name
Value of column23 if the log format is SYSLOG, else value of column11
acl_rule_uuid
security_result.rule_id
Value of acl_rule_uuid field from the grok pattern
action
security_result.action
If value of column25 is
Drop
,
Reject
or
Block
then BLOCK, else if value of column25 is
Accept
,
Accept decisively
,
Established
or
Allow
then ALLOW
attackID
security_result.detection_fields.attackID
Value of column12 if the log format is CSV with no src_ip
bigip_hostname
intermediary.hostname
Value of column2 if the log format is SYSLOG, else value of column3
bigip_ip
intermediary.ip
Value of column2 if the log format is SYSLOG, else value of column1
context_name
additional.fields.context_name.string_value
Value of column4 if the log format is SYSLOG, else value of column10 if there is src_ip, else value of column5
context_type
additional.fields.context_type.string_value
Value of column3 if the log format is SYSLOG, else value of column4 if there is src_ip, else value of column4
dest_fqdn
additional.fields.dest_fqdn.string_value
Value of column7 if the log format is SYSLOG, else value of column13
dest_geo
additional.fields.dest_geo.string_value
Value of column14
dest_ip
target.asset.ip, target.ip
Value of column8 if the log format is SYSLOG, else value of column6 if there is src_ip, else value of column6
dest_port
target.port
Value of column10 if the log format is SYSLOG, else value of column8 if there is src_ip, else value of column8
drop_reason
security_result.summary
Value of column26 if the log format is SYSLOG, else value of column19
eventId
additional.fields.eventId.string_value
Value captured in the grok pattern
flow_id
additional.fields.flow_id.string_value
Value of column29 if the log format is SYSLOG, else value of column17
loglevel
security_result.severity
If value of loglevel field from the grok pattern is
warning
,
debug
or
notice
then MEDIUM, else if value is
info
or
informational
then INFORMATIONAL, else if value is
err
or
error
then HIGH, else if value is
alert
,
crit
or
emer
then CRITICAL
packetsReceived
network.received_packets
Value of column15 if the log format is CSV with no src_ip
process
target.application
Value of process field from the grok pattern
protocol_number_src
network.ip_protocol
Value of column12 if the log format is SYSLOG, else value extracted from the ip_protocol_out variable
route_domain
additional.fields.route_domain.string_value
Value of column13 if the log format is SYSLOG, else value of column9
source_fqdn
additional.fields.source_fqdn.string_value
Value of column5 if the log format is SYSLOG, else value of column7
src_geo
additional.fields.src_geo.string_value
Value of column8
src_ip
principal.asset.ip, principal.ip
Value of column6 if the log format is SYSLOG, else value of column9 if the log format is CSV with no src_ip, else value of column5
src_port
principal.port
Value of column9 if the log format is SYSLOG, else value of column7 if the log format is CSV with no src_ip, else value of column7
ts
metadata.event_timestamp
Value of ts field from the grok pattern
vlan
additional.fields.vlan.string_value
Value of column11 if the log format is SYSLOG, else value of column21
metadata.event_type
If src_ip and dest_ip exist then NETWORK_CONNECTION, else if only src_ip exists then STATUS_UPDATE, else GENERIC_EVENT
metadata.log_type
F5_AFM
metadata.product_name
Advanced Firewall Management
metadata.vendor_name
F5
Need more help?
Get answers from Community members and Google SecOps professionals.
