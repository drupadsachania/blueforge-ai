# Collect Fortinet FortiAnalyzer logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fana/  
**Scraped:** 2026-03-05T09:56:12.892539Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiAnalyzer logs
Supported in:
Google secops
SIEM
This document explains how to collect and ingest Fortinet FortiAnalyzer logs to Google Security Operations by using Bindplane. The parser transforms the logs into UDM format. It handles both CEF and key-value formatted messages, extracting fields, performing data transformations (like converting timestamps and enriching IP protocols), and mapping them to the appropriate UDM fields based on event type and subtype. The parser also includes specific logic for handling network connections, DNS queries, HTTP requests, and various security events, enriching the UDM with details like application protocols, user information, and security outcomes.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Fortinet FortiAnalyzer.
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
FORTINET_FORTIANALYZER
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
Configure Syslog on Fortinet FortiAnalyzer
Sign in to the
FortiAnalyzer
.
Activate
CLI
mode.
Run the following commands:
config system syslog
  edit
NAME
set ip
IP_ADDRESS
set port
PORT
set reliable
enable or disable
next
end
Update the following fields:
NAME
: the name of the syslog server.
IP_ADDRESS
: enter the IPv4 address of the Bindplane agent.
PORT
: enter the port number for the Bindplane agent; for example,
514
.
enable or disable
: if you set the value of reliable as enable, it sends as TCP; if you set the value of reliable as disable, it sends as UDP.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action_details
Value from the
act
field when the log is in CEF format.
action
security_result.action_details
Value from the
action
field when the log is not in CEF format.  Used to derive
security_result.action
and
security_result.description
.
action
security_result.action
Derived. If
action
is
accept
,
passthrough
,
pass
,
permit
,
detected
, or
login
, then
ALLOW
. If
deny
,
dropped
,
blocked
, or
close
, then
BLOCK
. If
timeout
, then
FAIL
. Otherwise,
UNKNOWN_ACTION
.
action
security_result.description
Derived. Set to
Action:
+ derived
security_result.action
.
ad.app
target.application
Value from the
ad.app
field when the log is in CEF format.  If the value is
HTTPS
,
HTTP
,
DNS
,
DHCP
, or
SMB
, it is mapped to
network.application_protocol
.
ad.appact
additional.fields
Value from the
ad.appact
field when the log is in CEF format, added as a key-value pair with key
appact
.
ad.appcat
additional.fields
Value from the
ad.appcat
field when the log is in CEF format, added as a key-value pair with key
appcat
.
ad.appid
additional.fields
Value from the
ad.appid
field when the log is in CEF format, added as a key-value pair with key
appid
.
ad.applist
additional.fields
Value from the
ad.applist
field when the log is in CEF format, added as a key-value pair with key
applist
.
ad.apprisk
additional.fields
Value from the
ad.apprisk
field when the log is in CEF format, added as a key-value pair with key
apprisk
.
ad.cipher_suite
network.tls.cipher
Value from the
ad.cipher_suite
field when the log is in CEF format.
ad.countapp
(not mapped)
Not mapped to the IDM object.
ad.countweb
(not mapped)
Not mapped to the IDM object.
ad.dstcity
target.location.city
Value from the
ad.dstcity
field when the log is in CEF format.
ad.dstcountry
target.location.country_or_region
Value from the
ad.dstcountry
field when the log is in CEF format.
ad.dstintf
security_result.detection_fields
Value from the
ad.dstintf
field when the log is in CEF format, added as a key-value pair with key
dstintf
.
ad.dstintfrole
security_result.detection_fields
Value from the
ad.dstintfrole
field when the log is in CEF format, added as a key-value pair with key
dstintfrole
.
ad.dstregion
target.location.state
Value from the
ad.dstregion
field when the log is in CEF format.
ad.duration
network.session_duration.seconds
Value from the
ad.duration
field when the log is in CEF format.
ad.eventtime
metadata.event_timestamp
Value from the
ad.eventtime
field when the log is in CEF format.
ad.http_agent
network.http.parsed_user_agent
Value from the
ad.http_agent
field when the log is in CEF format.
ad.http_method
network.http.method
Value from the
ad.http_method
field when the log is in CEF format.
ad.http_refer
network.http.referral_url
Value from the
ad.http_refer
field when the log is in CEF format.
ad.http_request_bytes
network.sent_bytes
Value from the
ad.http_request_bytes
field when the log is in CEF format.
ad.http_response_bytes
network.received_bytes
Value from the
ad.http_response_bytes
field when the log is in CEF format.
ad.http_retcode
(not mapped)
Not mapped to the IDM object.
ad.http_url
(not mapped)
Not mapped to the IDM object.
ad.lanin
(not mapped)
Not mapped to the IDM object.
ad.lanout
(not mapped)
Not mapped to the IDM object.
ad.logid
metadata.product_log_id
Value from the
ad.logid
field when the log is in CEF format.
ad.mastersrcmac
principal.mac
Value from the
ad.mastersrcmac
field when the log is in CEF format.
ad.original_src
(not mapped)
Not mapped to the IDM object.
ad.original_srccountry
(not mapped)
Not mapped to the IDM object.
ad.poluuid
(not mapped)
Not mapped to the IDM object.
ad.policyid
security_result.rule_id
Value from the
ad.policyid
field when the log is in CEF format.
ad.policyname
security_result.rule_name
Value from the
ad.policyname
field when the log is in CEF format.
ad.policytype
security_result.rule_type
Value from the
ad.policytype
field when the log is in CEF format.
ad.profile
target.resource.name
Value from the
ad.profile
field when the log is in CEF format. Also sets
target.resource.resource_type
to
ACCESS_POLICY
.
ad.proto
network.ip_protocol
Value from the
ad.proto
field when the log is in CEF format.  Parsed using the
parse_ip_protocol.include
file.
ad.qclass
network.dns.questions.class
Value from the
ad.qclass
field when the log is in CEF format. Mapped using the
dns_query_class_mapping.include
file.
ad.qname
network.dns.questions.name
Value from the
ad.qname
field when the log is in CEF format.
ad.qtype
(not mapped)
Not mapped to the IDM object.
ad.qtypeval
network.dns.questions.type
Value from the
ad.qtypeval
field when the log is in CEF format.
ad.rcvddelta
(not mapped)
Not mapped to the IDM object.
ad.rcvdpkt
additional.fields
Value from the
ad.rcvdpkt
field when the log is in CEF format, added as a key-value pair with key
receivedPackets
.
ad.sentdelta
(not mapped)
Not mapped to the IDM object.
ad.sentpkt
additional.fields
Value from the
ad.sentpkt
field when the log is in CEF format, added as a key-value pair with key
sentPackets
.
ad.server_pool_name
(not mapped)
Not mapped to the IDM object.
ad.sourceTranslatedAddress
principal.nat_ip
Value from the
ad.sourceTranslatedAddress
field when the log is in CEF format.
ad.sourceTranslatedPort
principal.nat_port
Value from the
ad.sourceTranslatedPort
field when the log is in CEF format.
ad.src
principal.ip
Value from the
ad.src
field when the log is in CEF format.
ad.srccountry
principal.location.country_or_region
Value from the
ad.srccountry
field when the log is in CEF format.
ad.srcintf
security_result.detection_fields
Value from the
ad.srcintf
field when the log is in CEF format, added as a key-value pair with key
srcintf
.
ad.srcintfrole
security_result.detection_fields
Value from the
ad.srcintfrole
field when the log is in CEF format, added as a key-value pair with key
srcintfrole
.
ad.srcmac
principal.mac
Value from the
ad.srcmac
field when the log is in CEF format.
ad.srcserver
(not mapped)
Not mapped to the IDM object.
ad.spt
principal.port
Value from the
ad.spt
field when the log is in CEF format.
ad.status
security_result.summary
Value from the
ad.status
field when the log is in CEF format.
ad.subtype
metadata.product_event_type
Used with
ad.logid
to create the
metadata.product_event_type
when the log is in CEF format.  Also used to derive
metadata.event_type
and to map specific fields for DNS and HTTP events.
ad.trandisp
(not mapped)
Not mapped to the IDM object.
ad.tz
(not mapped)
Not mapped to the IDM object.
ad.utmaction
security_result.action
Value from the
ad.utmaction
field when the log is in CEF format. Used to derive
security_result.action
and
security_result.description
.
ad.user_name
(not mapped)
Not mapped to the IDM object.
ad.vd
principal.administrative_domain
Value from the
ad.vd
field when the log is in CEF format.
ad.vwlid
(not mapped)
Not mapped to the IDM object.
ad.wanin
(not mapped)
Not mapped to the IDM object.
ad.wanout
(not mapped)
Not mapped to the IDM object.
ad.xid
(not mapped)
Not mapped to the IDM object.
ad.x509_cert_subject
(not mapped)
Not mapped to the IDM object.
agent
(not mapped)
Not mapped to the IDM object.
appid
additional.fields
Value from the
appid
field when the log is not in CEF format, added as a key-value pair with key
appid
.
app
target.application
Value from the
app
field when the log is not in CEF format. If the value is
HTTPS
,
HTTP
,
DNS
,
DHCP
, or
SMB
, it is mapped to
network.application_protocol
.
appact
additional.fields
Value from the
appact
field when the log is not in CEF format, added as a key-value pair with key
appact
.
appcat
additional.fields
Value from the
appcat
field when the log is not in CEF format, added as a key-value pair with key
appcat
.
applist
additional.fields
Value from the
applist
field when the log is not in CEF format, added as a key-value pair with key
applist
.
apprisk
additional.fields
Value from the
apprisk
field when the log is not in CEF format, added as a key-value pair with key
apprisk
.
cat
security_result1.rule_id
Value from the
cat
field when the log is not in CEF format.
catdesc
security_result.description
Value from the
catdesc
field when the log is not in CEF format. Only used if
catdesc
is not empty.
centralnatid
(not mapped)
Not mapped to the IDM object.
cipher_suite
network.tls.cipher
Value from the
cipher_suite
field when the log is not in CEF format.
countssl
(not mapped)
Not mapped to the IDM object.
crlevel
security_result.severity
Value from the
crlevel
field when the log is not in CEF format. Used to derive
security_result.severity
.
craction
security_result.about.labels
Value from the
craction
field when the log is not in CEF format, added as a key-value pair with key
craction
.
create_time
(not mapped)
Not mapped to the IDM object.
data
(not mapped)
The raw log data. Not directly mapped to UDM.
date
(not mapped)
Not mapped to the IDM object.
devname
principal.hostname
,
principal.asset.hostname
Value from the
devname
field when the log is not in CEF format.
devid
(not mapped)
Not mapped to the IDM object.
devtype
(not mapped)
Not mapped to the IDM object.
direction
network.direction
Value from the
direction
field when the log is not in CEF format. If
incoming
or
inbound
, then
INBOUND
. If
outgoing
or
outbound
, then
OUTBOUND
.
dpt
target.port
Value from the
dpt
field when the log is in CEF format.
dstip
target.ip
,
target.asset.ip
Value from the
dstip
field when the log is not in CEF format.
dstintf
security_result.detection_fields
Value from the
dstintf
field when the log is not in CEF format, added as a key-value pair with key
dstintf
.
dstintfrole
security_result.detection_fields
Value from the
dstintfrole
field when the log is not in CEF format, added as a key-value pair with key
dstintfrole
.
dstport
target.port
Value from the
dstport
field when the log is not in CEF format.
dstregion
target.location.state
Value from the
dstregion
field when the log is not in CEF format.
dstuuid
target.user.product_object_id
Value from the
dstuuid
field when the log is not in CEF format.
duration
network.session_duration.seconds
Value from the
duration
field when the log is not in CEF format.
dstcity
target.location.city
Value from the
dstcity
field when the log is not in CEF format.
dstcountry
target.location.country_or_region
Value from the
dstcountry
field when the log is not in CEF format.
dstmac
target.mac
Value from the
dstmac
field when the log is not in CEF format.
eventtime
metadata.event_timestamp
Value from the
eventtime
field when the log is not in CEF format. The value is reduced from microseconds to seconds.
eventtype
security_result2.rule_type
Value from the
eventtype
field when the log is not in CEF format.
externalID
(not mapped)
Not mapped to the IDM object.
group
principal.user.group_identifiers
Value from the
group
field when the log is not in CEF format.
hostname
target.hostname
,
target.asset.hostname
Value from the
hostname
field when the log is not in CEF format.
http_agent
network.http.parsed_user_agent
Value from the
http_agent
field when the log is not in CEF format. Converted to a parsed user agent object.
http_method
network.http.method
Value from the
http_method
field when the log is not in CEF format.
http_refer
network.http.referral_url
Value from the
http_refer
field when the log is not in CEF format.
http_request_bytes
network.sent_bytes
Value from the
http_request_bytes
field when the log is not in CEF format.
http_response_bytes
network.received_bytes
Value from the
http_response_bytes
field when the log is not in CEF format.
httpmethod
network.http.method
Value from the
httpmethod
field when the log is not in CEF format.
in
network.received_bytes
Value from the
in
field when the log is in CEF format.
incidentserialno
(not mapped)
Not mapped to the IDM object.
lanin
(not mapped)
Not mapped to the IDM object.
lanout
(not mapped)
Not mapped to the IDM object.
level
security_result.severity
,
security_result.severity_details
Value from the
level
field when the log is not in CEF format. Used to derive
security_result.severity
.  If
error
or
warning
, then
HIGH
. If
notice
, then
MEDIUM
. If
information
or
info
, then
LOW
. Also sets
security_result.severity_details
to
level:
+
level
.
locip
principal.ip
,
principal.asset.ip
Value from the
locip
field when the log is not in CEF format.
logdesc
metadata.description
Value from the
logdesc
field when the log is not in CEF format.
logid
metadata.product_log_id
Value from the
logid
field when the log is not in CEF format.
logver
(not mapped)
Not mapped to the IDM object.
mastersrcmac
principal.mac
Value from the
mastersrcmac
field when the log is not in CEF format.
method
(not mapped)
Not mapped to the IDM object.
msg
metadata.description
Value from the
msg
field when the log is not in CEF format.  Also used for
security_result.description
if
catdesc
is empty.
out
network.sent_bytes
Value from the
out
field when the log is in CEF format.
outintf
(not mapped)
Not mapped to the IDM object.
policyid
security_result.rule_id
Value from the
policyid
field when the log is not in CEF format.
policyname
security_result.rule_name
Value from the
policyname
field when the log is not in CEF format.
policytype
security_result.rule_type
Value from the
policytype
field when the log is not in CEF format.
poluuid
(not mapped)
Not mapped to the IDM object.
profile
target.resource.name
Value from the
profile
field when the log is not in CEF format. Also sets
target.resource.resource_type
to
ACCESS_POLICY
.
proto
network.ip_protocol
Value from the
proto
field when the log is not in CEF format. Parsed using the
parse_ip_protocol.include
file.
qclass
network.dns.questions.class
Value from the
qclass
field when the log is not in CEF format. Mapped using the
dns_query_class_mapping.include
file.
qname
network.dns.questions.name
Value from the
qname
field when the log is not in CEF format.
reason
security_result.description
Value from the
reason
field when the log is not in CEF format. Only used if
reason
is not
N/A
and not empty.
rcvdbyte
network.received_bytes
Value from the
rcvdbyte
field when the log is not in CEF format.
rcvdpkt
additional.fields
Value from the
rcvdpkt
field when the log is not in CEF format, added as a key-value pair with key
receivedPackets
.
remip
target.ip
,
target.asset.ip
Value from the
remip
field when the log is not in CEF format.
remport
(not mapped)
Not mapped to the IDM object.
reqtype
(not mapped)
Not mapped to the IDM object.
sentbyte
network.sent_bytes
Value from the
sentbyte
field when the log is not in CEF format.
sentpkt
additional.fields
Value from the
sentpkt
field when the log is not in CEF format, added as a key-value pair with key
sentPackets
.
service
network.application_protocol
,
target.application
Value from the
service
field when the log is not in CEF format. Parsed using the
parse_app_protocol.include
file. If the output of the parser is not empty, it is mapped to
network.application_protocol
. Otherwise, the original value is mapped to
target.application
.
sessionid
network.session_id
Value from the
sessionid
field when the log is not in CEF format.
sn
(not mapped)
Not mapped to the IDM object.
sourceTranslatedAddress
principal.nat_ip
Value from the
sourceTranslatedAddress
field when the log is in CEF format.
sourceTranslatedPort
principal.nat_port
Value from the
sourceTranslatedPort
field when the log is in CEF format.
spt
principal.port
Value from the
spt
field when the log is in CEF format.
src
principal.ip
Value from the
src
field when the log is in CEF format.
srcip
principal.ip
,
principal.asset.ip
Value from the
srcip
field when the log is not in CEF format.
srcintf
security_result.detection_fields
Value from the
srcintf
field when the log is not in CEF format, added as a key-value pair with key
srcintf
.
srcintfrole
security_result.detection_fields
Value from the
srcintfrole
field when the log is not in CEF format, added as a key-value pair with key
srcintfrole
.
srcmac
principal.mac
Value from the
srcmac
field when the log is not in CEF format.  Hyphens are replaced with colons.
srcport
principal.port
Value from the
srcport
field when the log is not in CEF format.
srccountry
principal.location.country_or_region
Value from the
srccountry
field when the log is not in CEF format. Only mapped if not
Reserved
and not empty.
srcuuid
principal.user.product_object_id
Value from the
srcuuid
field when the log is not in CEF format.
srcserver
(not mapped)
Not mapped to the IDM object.
start
(not mapped)
Not mapped to the IDM object.
status
security_result.summary
Value from the
status
field when the log is not in CEF format.
subtype
metadata.product_event_type
Used with
type
to create the
metadata.product_event_type
when the log is not in CEF format. Also used to derive
metadata.event_type
and to map specific fields for DNS and HTTP events.
time
(not mapped)
Not mapped to the IDM object.
timestamp
metadata.event_timestamp
Value from the
timestamp
field.
trandisp
(not mapped)
Not mapped to the IDM object.
transip
(not mapped)
Not mapped to the IDM object.
transport
(not mapped)
Not mapped to the IDM object.
type
metadata.product_event_type
Used with
subtype
to create the
metadata.product_event_type
when the log is not in CEF format. Also used to derive
metadata.event_type
.
tz
(not mapped)
Not mapped to the IDM object.
ui
(not mapped)
Not mapped to the IDM object.
url
target.url
Value from the
url
field when the log is not in CEF format.
user
principal.user.userid
Value from the
user
field when the log is not in CEF format. Only mapped if not
N/A
and not empty.
utmaction
security_result.action
,
security_result2.action_details
Value from the
utmaction
field when the log is not in CEF format. Used to derive
security_result.action
and
security_result.description
.
utmaction
security_result.action
Derived. If
utmaction
is
accept
,
allow
,
passthrough
,
pass
,
permit
, or
detected
, then
ALLOW
. If
deny
,
dropped
,
blocked
, or
block
, then
BLOCK
. Otherwise,
UNKNOWN_ACTION
.
utmaction
security_result.description
Derived. Set to
UTMAction:
+ derived
security_result.action
if
action1
is empty.
utmevent
(not mapped)
Not mapped to the IDM object.
vd
principal.administrative_domain
Value from the
vd
field when the log is not in CEF format.
vpntunnel
(not mapped)
Not mapped to the IDM object.
wanin
(not mapped)
Not mapped to the IDM object.
wanout
(not mapped)
Not mapped to the IDM object.
N/A (Parser Logic)
about.asset.asset_id
Derived.  Set to
Fortinet.
+
product_name
+
:
+
deviceExternalId
when the log is in CEF format.
N/A (Parser Logic)
about.hostname
Derived. Set to
auth0
when the log is in CEF format.
N/A (Parser Logic)
extensions.auth
Derived. An empty object is created when
metadata.event_type
is
USER_LOGIN
.
N/A (Parser Logic)
extensions.auth.type
Derived. Set to
AUTHTYPE_UNSPECIFIED
when
metadata.event_type
is
USER_LOGIN
.
N/A (Parser Logic)
metadata.event_type
Derived based on various log fields and logic within the parser. Can be
NETWORK_CONNECTION
,
STATUS_UPDATE
,
GENERIC_EVENT
,
NETWORK_DNS
,
NETWORK_HTTP
,
USER_LOGIN
,
USER_LOGOUT
, or
NETWORK_UNCATEGORIZED
.
N/A (Parser Logic)
metadata.log_type
Derived. Set to
FORTINET_FORTIANALYZER
.
N/A (Parser Logic)
metadata.product_event_type
Derived. Set to
type
+
-
+
subtype
.
N/A (Parser Logic)
metadata.product_name
Derived. Set to
Fortianalyzer
or extracted from the CEF message.
N/A (Parser Logic)
metadata.product_version
Extracted from the CEF message.
N/A (Parser Logic)
metadata.vendor_name
Derived. Set to
Fortinet
.
N/A (Parser Logic)
network.application_protocol
Derived from the
service
or
app
fields using the
parse_app_protocol.include
file, or set to
DNS
for DNS events. Also set based on
ad.app
if it's one of
HTTPS
,
HTTP
,
DNS
,
DHCP
, or
SMB
.
N/A (Parser Logic)
network.dns.questions
Derived. An array of question objects, each with
name
,
type
, and
class
fields, populated for DNS events.
N/A (Parser Logic)
network.http.parsed_user_agent
Derived from the
http_agent
field by converting it to a parsed user agent object.
N/A (Parser Logic)
network.ip_protocol
Derived from the
proto
field using the
parse_ip_protocol.include
file.
N/A (Parser Logic)
principal.administrative_domain
Value from the
vd
field.
N/A (Parser Logic)
principal.asset.ip
Copied from
principal.ip
.
N/A (Parser Logic)
principal.asset.hostname
Copied from
principal.hostname
.
N/A (Parser Logic)
security_result.about.labels
An array of key-value pairs, populated with
craction
if present.
N/A (Parser Logic)
security_result.action
Derived from
action
or
utmaction
.
N/A (Parser Logic)
security_result.description
Derived from
action
,
utmaction
,
msg
,
catdesc
, or
reason
, depending on the available fields and log format.
N/A (Parser Logic)
security_result.severity
Derived from
crlevel
or
level
.
N/A (Parser Logic)
security_result.severity_details
Derived. Set to
level:
+
level
.
N/A (Parser Logic)
security_result.detection_fields
An array of key-value pairs, populated with
srcintf
,
srcintfrole
,
dstintf
, and
dstintfrole
if present.
N/A (Parser Logic)
target.asset.ip
Copied from
target.ip
.
N/A (Parser Logic)
target.asset.hostname
Copied from
target.hostname
.
N/A (Parser Logic)
target.resource.resource_type
Derived. Set to
ACCESS_POLICY
when the
profile
field is present.
Need more help?
Get answers from Community members and Google SecOps professionals.
