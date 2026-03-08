# Collect Barracuda WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-waf/  
**Scraped:** 2026-03-05T09:20:19.325150Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Barracuda WAF logs
Supported in:
Google secops
SIEM
This document explains how to collect Barracuda Web Application Firewall (WAF) logs using Bindplane. The parser extracts fields from logs in JSON and Syslog formats, normalizes them, and maps them to the Unified Data Model (UDM). It handles various log types (traffic, web firewall) and performs conditional transformations based on field values, including IP address/hostname resolution, directionality mapping, and severity normalization.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the Barracuda WAF.
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:54525"
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
SYSLOG
namespace
:
barracuda_waf
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
Configure Barracuda WAF
Sign in to the
Barracuda WAF
console using administrator credentials.
Click the
Advanced tab
>
Export logs
.
In the
Export logs
section, click
Add export log server
.
Provide the following values:
Name
: enter a name for the Google SecOps forwarder.
Log server type
: select
Syslog
.
IP Address or hostname
: enter the
Bindplane
IP address.
Port
: enter the
Bindplane
port.
Connection type
: select
TCP
connection type (TCP is recommended. However, UDP or SSL protocols can also be used).
Validate server certificate
: select
No
.
Client certificate
: select
None
.
Log timestamp and hostname
: select
Yes
.
Click
Add
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.action
If
action
is
DENY
, set to
BLOCK
. Otherwise, set to
ALLOW
(specifically for
WF
log type). Also used for generic firewall events.
appProtocol
network.application_protocol
If
appProtocol
matches
TLSv
, set to
HTTPS
. Otherwise, use the value of
appProtocol
.
attackDetails
security_result.description
Extracted from the raw log for
WF
log type.
attackType
security_result.summary
Part of the
security_result.summary
, combined with
ruleType
.
bytesReceived
network.received_bytes
Converted to unsigned integer and mapped for
TR
log type.
bytesSent
network.sent_bytes
Converted to unsigned integer and mapped for
TR
log type.
hostName
target.hostname
If
hostName
is not an IP address, use its value. Otherwise, it's merged into
target.ip
.
httpMethod
loginId
principal.user.userid
Mapped for
TR
log type when not equal to
emptyToken
.
logType
metadata.product_event_type
If
TR
, set
metadata.product_event_type
to
Barracuda Access Log
. If
WF
, set to
Barracuda Web Firewall Log
.
message
metadata.description
Used when
desc
is not empty.
referrer
network.http.referral_url
Mapped for
TR
log type when not equal to
emptyToken
.
responseCode
network.http.response_code
Converted to integer and mapped for
TR
log type.
rule
security_result.rule_name
Mapped for
WF
log type.
ruleType
security_result.summary
Part of the
security_result.summary
, combined with
attackType
.
sec_desc
security_result.rule_name
Used for generic firewall events.
server
target.ip
Merged into
target.ip
.
serv
target.ip
Merged into
target.ip
.
severity
security_result.severity
For
WF
log type: Converted to uppercase. If
EMERGENCY
,
ALER
, or
CRITICAL
, set
security_result.severity
to
CRITICAL
.  If
ERROR
, set to
HIGH
. If
WARNING
, set to
MEDIUM
. If
NOTICE
, set to
LOW
. Otherwise, set to
INFORMATIONAL
.
src
principal.ip
Also used for generic firewall events and some status updates.
srcPort
principal.port
Converted to integer.
target
targetPort
target.port
Converted to integer.
time
metadata.event_timestamp.seconds
,
metadata.event_timestamp.nanos
,
timestamp.seconds
,
timestamp.nanos
Combined with
tz
and parsed to create the event timestamp. The seconds and nanos are extracted and populated in the respective fields.
url
urlParams
target.url
Appended to
url
if not equal to
emptyToken
for
TR
log type.
userAgent
userName
target.user.userid
,
target.user.user_display_name
Used for generic firewall events. If not equal to
emptyToken
for
TR
log type, mapped to
target.user.user_display_name
.  Hardcoded to
Barracuda
. Set to
NETWORK_HTTP
if both
src
and
target
are present. Set to
STATUS_UPDATE
if only
src
is present. Set to
GENERIC_EVENT
as a default or for other scenarios like CEF parsing. Hardcoded to
BARRACUDA_WAF
.
Need more help?
Get answers from Community members and Google SecOps professionals.
