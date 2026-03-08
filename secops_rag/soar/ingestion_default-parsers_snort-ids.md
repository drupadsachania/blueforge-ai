# Collect Snort logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snort-ids/  
**Scraped:** 2026-03-05T10:00:19.213639Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Snort logs
Supported in:
Google secops
SIEM
This document explains how to collect Snort logs to Google Security Operations by using Bindplane. The parser attempts to handle two different Snort log formats (SYSLOG + JSON) using
grok
patterns to extract relevant fields. Depending on the identified format, it further processes the data, mapping extracted fields to the unified data model (UDM) schema, normalizing values, and enriching the output with additional context.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Snort.
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
SNORT_IDS
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
Configure syslog export on Snort v2.x
Sign in to the Snort device using terminal.
Edit the following file:
/etc/snort/snort.conf
Go to
6) Configure output plugins
.
Add following entry:
# syslog
output alert_syslog: host=
BINDPLANE_IP_ADDRESS
:
PORT_NUMBER
, LOG_AUTH LOG_ALERT
Replace the following:
BINDPLANE_IP_ADDRESS
: Bindplane Agent IP address.
PORT_NUMBER
: Bindplane Agent port number.
Save the file.
Start the
snort
service.
Stop the
rsyslog
service.
Edit the following file:
/etc/rsyslogd.conf
# remote host is: name/ip:port
*.* @@
BINDPLANE_IP_ADDRESS
:
PORT_NUMBER
Replace the following:
BINDPLANE_IP_ADDRESS
: Bindplane Agent IP address.
PORT_NUMBER
: Bindplane Agent port number.
Start the
rsyslog
service.
Configure syslog export on Snort v3.1.53
Sign in to the Snort device using terminal.
Stop the
rsyslog
and
snort
services.
Go to the following Snort installation directory:
/usr/local/etc/snort/
Edit the following Snort configuration file:
snort.lua
In the
Configure outputs
options, append the following code (you can use any facility and level):
alert_syslog =
  {
    facility = 'local3',
    level = 'info',
  }
Save the Snort configuration file.
Go to the
rsyslog
service default configuration files directory:
/etc/rsyslog.d
Create a new file:
3-snort.conf
:
# cd /etc/rsyslog.d
# vi 3-snort.conf
To send logs over TCP or UDP, add the following configuration:
local3.* @@
BINDPLANE_IP_ADDRESS
:
PORT_NUMBER
Replace the following:
BINDPLANE_IP_ADDRESS
: Bindplane agent IP address.
PORT_NUMBER
: Bindplane agent port number.
Save the file.
Start
rsyslog
and then the
snort
service.
UDM Mapping Table
Log Field
UDM Mapping
Logic
agent.hostname
observer.hostname
Value taken from
agent.hostname
field in the raw log.
agent.id
observer.asset_id
Value taken from
agent.id
field in the raw log and concatenated with
agent.type
as follows:
agent.type:agent.id
.
agent.type
observer.application
Value taken from
agent.type
field in the raw log.
agent.version
observer.platform_version
Value taken from
agent.version
field in the raw log.
alert.category
security_result.category_details
Value taken from
alert.category
field in the raw log.
alert.rev
security_result.rule_version
Value taken from
alert.rev
field in the raw log.
alert.rule
security_result.summary
Value taken from
alert.rule
field in the raw log, with double quotes removed.
alert.severity
security_result.severity
If
alert.severity
is greater than or equal to 4, set to
LOW
. If
alert.severity
is 2 or 3, set to
MEDIUM
. If
alert.severity
is 1, set to
HIGH
. Otherwise, set to
UNKNOWN_SEVERITY
.
alert.signature
security_result.rule_name
Value taken from
alert.signature
field in the raw log.
alert.signature_id
security_result.rule_id
Value taken from
alert.signature_id
field in the raw log.
app_proto
network.application_protocol
If
app_proto
is
dns
,
smb
, or
http
, convert to uppercase and use that value. Otherwise, set to
UNKNOWN_APPLICATION_PROTOCOL
.
category
security_result.category
If
category
is
trojan-activity
, set to
NETWORK_MALICIOUS
. If
category
is
policy-violation
, set to
POLICY_VIOLATION
. Otherwise, set to
UNKNOWN_CATEGORY
.
classtype
security_result.rule_type
Value taken from
classtype
field in the raw log, if it's not empty or
unknown
.
community_id
network.community_id
Value taken from
community_id
field in the raw log.
date_log
Used to set the event timestamp if
time
field is empty.
desc
metadata.description
Value taken from
desc
field in the raw log.
dest_ip
target.ip
Value taken from
dest_ip
field in the raw log.
dest_port
target.port
Value taken from
dest_port
field in the raw log and converted to integer.
dstport
target.port
Value taken from
dstport
field in the raw log and converted to integer.
file.filename
security_result.about.file.full_path
Value taken from
file.filename
field in the raw log, if it's not empty or
/
.
file.size
security_result.about.file.size
Value taken from
file.size
field in the raw log and converted to unsigned integer.
host.name
principal.hostname
Value taken from
host.name
field in the raw log.
hostname
principal.hostname
Value taken from
hostname
field in the raw log.
inter_host
intermediary.hostname
Value taken from
inter_host
field in the raw log.
log.file.path
principal.process.file.full_path
Value taken from
log.file.path
field in the raw log.
metadata.version
metadata.product_version
Value taken from
metadata.version
field in the raw log.
proto
network.ip_protocol
Value taken from
proto
field in the raw log. If it's a number, it's converted to the corresponding IP protocol name using a lookup table.
rule_name
security_result.rule_name
Value taken from
rule_name
field in the raw log.
signature_id
security_result.rule_id
Value taken from
signature_id
field in the raw log.
signature_rev
security_result.rule_version
Value taken from
signature_rev
field in the raw log.
src_ip
principal.ip
Value taken from
src_ip
field in the raw log.
src_port
principal.port
Value taken from
src_port
field in the raw log and converted to integer.
srcport
principal.port
Value taken from
srcport
field in the raw log and converted to integer.
time
Used to set the event timestamp.
metadata.event_type
Always set to
SCAN_NETWORK
.
metadata.log_type
Hardcoded to
SNORT_IDS
.
metadata.product_name
Hardcoded to
SNORT_IDS
.
metadata.vendor_name
Hardcoded to
SNORT
.
security_result.action
Set to
ALLOW
if
alert.action
is
allowed
, otherwise set to
UNKNOWN_ACTION
.
Need more help?
Get answers from Community members and Google SecOps professionals.
