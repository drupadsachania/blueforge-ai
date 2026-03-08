# Collect McAfee Web Gateway logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-webproxy/  
**Scraped:** 2026-03-05T09:57:48.492596Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect McAfee Web Gateway logs
Supported in:
Google secops
SIEM
This document explains how to ingest the McAfee Web Gateway logs to Google Security Operations using a Bindplane agent. The parser extracts fields from the logs in SYSLOG + KV (CEF), JSON, and raw formats. It uses grok and csv filters to parse different log structures, and normalizes field names. It then maps the extracted fields to the Unified Data Model (UDM) schema, handling various edge cases and data inconsistencies to create a unified output.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to McAfee Web Gateway
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
`
https
:
//
github
.
com
/
observIQ
/
bindplane
-
agent
/
releases
/
latest
/
download
/
observiq
-
otel
-
collector
.
msi
`
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
`
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
`
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
`
0.0.0.0:514`
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
MCAFEE_WEBPROXY
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
Configure Syslog in McAfee Web Gateway
Sign in to your McAfee Web Gateway web UI.
Go to
Policy
>
Rule Sets
.
Click
Log Handler
, then expand the
Default
rule set, and select the nested
CEF Syslog
rule set.
Enable
Send to Syslog
rule.
Click
Save Changes
.
Go to
Configuration
>
Appliances
>
Log File Manager
>
Settings
.
Select
Write audit log to syslog
.
Go to
Configuration
>
File Editor
.
Select
rsyslog.conf
on the file tree.
Edit the file as follows:
Locate the line (or similar):
*.info;mail.none;authpriv.none;cron.none /var/log/messages
.
Add a daemon in this line and insert a - (dash) before the path information:
*.info;daemon.!=info;mail.none;authpriv.none;cron.none -/var/log/messages
Add a new line at the bottom of the file to send the info messages to the Bindplane agent IP address.
For syslog over
UDP
:
daemon.info;auth.=info @<bindplane-server-ip>:<bindplane-port>
For syslog over
TCP
:
daemon.info;auth.=info @@<bindplane-server-ip>:<bindplane-port>
Supported McAfee Web Gateway Sample Logs
Syslog + CEF
<
30
>
Nov
7
07
:
59
:
54
proxy
-
host
-
01
mwg
:
CEF
:
0
|
McAfee
|
Web
Gateway
|
7.1
|
200
|
Proxy
-
Def
ault
Allow
|
2
|
rt
=
Nov
07
2018
07
:
59
:
54
cat
=
Access
Log
src
=
10.0.0.5
dhost
=
api
.
go
ogle
-
dummy
.
com
requestMethod
=
GET
request
=
http
:
//
api
.
go
ogle
-
dummy
.
com
/
v1
/
projects
/
jobs
?
key
\
=
MASKED_API_KEY
app
=
HTTP
cs3
=
HTTP
/
1.1
cs3Label
=
Protocol
/
Version
spt
=
57065
cs2
=
Int
ernet
Services
cs2Label
=
URL
Category
cs6
=
Minimal
Risk
cs6Label
=
Reputation
fileType
=
application
/
json
in
=
2122
out
=
893
requestClientApplication
=
Mozilla
/
5.0
(
Macintosh
;
Int
el
Mac
OS
X
10
_15_7
)
cs1
=
cs1Label
=
Virus
Name
cn1
=
0
cn1Label
=
Block
Reason
suser
=
jdoe
dst
=
192.168.20.20
requestContext
=
https
:
//
console
.
cloud
.
go
ogle
.
com
/
cs5
=
cs5Label
=
Cont
ent
-
Disposition
flexString2
=
fn
ame
=
{}#
012
oldFileName
=
destinationDnsDomain
=-
JSON
{
"syslog_facility"
:
"user-level"
,
"user_id"
:
-1
,
"url"
:
"https://video.social-dummy.com/"
,
"username"
:
"region\\masked_user"
,
"reputation"
:
"Minimal Risk"
,
"media_type"
:
""
,
"category"
:
"Streaming Media, Social Networking"
,
"syslog_facility_code"
:
1
,
"system"
:
"windows"
,
"source_ip"
:
"10.0.0.1"
,
"@timestamp"
:
"2018-11-01T10:47:18.000Z"
,
"http_action"
:
"CONNECT"
,
"user_agent_comment"
:
""
,
"virus"
:
""
,
"location"
:
""
,
"host"
:
{
"id"
:
"a9b50f8b-xxxx-xxxx-xxxx-b440271f31d1"
,
"architecture"
:
"x86_64"
,
"os"
:
{
"platform"
:
"windows"
,
"kernel"
:
"10.0.14393.3630"
,
"family"
:
"windows"
,
"build"
:
"14393.3630"
,
"version"
:
"10.0"
,
"name"
:
"Windows Server 2016 Standard"
},
"hostname"
:
"PROXY_HOST_01"
,
"name"
:
"PROXY_HOST_01"
},
"@version"
:
"1"
,
"timestamp_epoch"
:
1589698038
,
"tags"
:
[
"send_json"
],
"last_rule"
:
"Block URLs whose category is in Category BlockList"
,
"user_agent_product"
:
"Other"
,
"server_to_client_bytes"
:
4211
,
"block_reason"
:
"Blocked by URL filtering"
,
"uri_scheme"
:
"https"
,
"message"
:
"\"-1\",\"region\\\\masked_user\",\"10.0.0.1\",\"CONNECT\",\"4211\",\"2224\",\"video.social-dummy.com\",\"/\",\"DENIED\",\"\",\"1589698038\",\"2020-05-17 06:47:18\",\"https\",\"Streaming Media, Social Networking\",\"\",\"\",\"Minimal Risk\",\"Block URLs whose category is in Category BlockList\",\"403\",\"192.168.1.100\",\"\",\"Blocked by URL filtering\",\"Other\",\"\",\"\",\"https://video.social-dummy.com/\""
,
"application_type"
:
""
,
"result"
:
"DENIED"
,
"requested_path"
:
"/"
,
"syslog_severity_code"
:
5
,
"user_agent_version"
:
""
,
"input"
:
{
"type"
:
"log"
},
"client_to_server_bytes"
:
2224
,
"ecs"
:
{
"version"
:
"1.4.0"
},
"client_ip"
:
"192.168.1.100"
,
"syslog_severity"
:
"notice"
,
"requested_host"
:
"video.social-dummy.com"
,
"agent"
:
{
"id"
:
"64f73b95-xxxx-xxxx-xxxx-4293d255db15"
,
"version"
:
"7.6.2"
,
"type"
:
"filebeat"
,
"hostname"
:
"PROXY_HOST_01"
,
"ephemeral_id"
:
"6f2c729c-xxxx-xxxx-xxxx-d6c97930c632"
},
"log"
:
{
"file"
:
{
"path"
:
"E:\\FullURL-PostProcessLogs\\Appended\\websaas12_1589697967.csv"
},
"offset"
:
774757
},
"http_status_code"
:
403
}
Syslog + Key-Value (Pipe Delimited)
<
30
>
Apr
14
03
:
49
:
56
PROXY01IM0001
mwg
:
McAfeeWG
|
time_stamp
=
[
01
/
Nov
/
2018
:
03
:
49
:
56
+
0530
]|
auth_user
=
|
src_ip
=
10.10.10.10
|
server_ip
=
192.168.1.100
|
host
=
detectportal
.
firefox
.
com
|
url_port
=
80
|
status_code
=
302
|
bytes_from_client
=
297
|
bytes_to_client
=
4134
|
categories
=
|
rep_level
=
|
method
=
GET
|
url
=
http
:
//
detectportal
.
firefox
.
com
/
success
.
txt
|
media_type
=
|
application_name
=
|
user_agent
=
Mozilla
/
5.0
(
Windows
NT
6.1
;
Win64
;
x64
;
rv
:
74.0
)
Gecko
/
20100101
Firefox
/
74.0
|
block_res
=
81
|
block_reason
=
Authentication
Required
|
virus_name
=
|
hash
=
|
filename
=
success
.
txt
|
filesize
=
0
|
CSV
"-1"
,
"domain\masked_user"
,
"192.168.100.50"
,
"GET"
,
"3004"
,
"80"
,
"s0.ads-dummy.net"
,
"/path/to/image.png"
,
"OBSERVED"
,
""
,
"1671176143"
,
"2018-11-16 07:35:43"
,
"https"
,
"Web Ads"
,
"image/png"
,
""
,
"Minimal Risk"
,
"Connection allowed"
,
"200"
,
"10.0.0.5"
,
""
,
""
,
"Chrome"
,
"108.0.0.0"
,
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
,
"chrome.exe"
,
"142.250.0.1"
,
"443"
Access Log (Space Delimited / Default)
<
30
>
Jan
1
18
:
16
:
31
mdp
-
proxy
-
010
mwg
:
2019
-
01
-
01
18
:
16
:
31
200
10.0
.
0.15
NoAuthProd
AllowListProd
"-"
"-"
Prod_NoAVScan
-
CONNECT
https
"us2-loadbalancer.acme.com"
443
10.100
.
2.3
"Business"
"Minimal Risk"
0
GTI_CLOUD
"US"
"-"
"-"
"-"
"-"
TCP_MISS
241476
6297
1170
6297
1170
1.2
.
3.4
-
0400
0
"-"
"Eternaty"
"-"
-
"-"
50931
33229
_EOL_
CSV-Encapsulated CEF
2026
-
01
-
14
T11
:
20
:
37.000000
Z
,
NETWORK_HTTP
,
"<30>Jan 14 13:20:37 MWG03 mwg: CEF:0|McAfee|Web Gateway|12.2.7|200|Proxy-Block If Virus was Found|2|
rt
=
Jan
14
2026
13
:
20
:
37
cat
=
Access
Log
dst
=
2.2.2.2
dhost
=
vstmr
.
dummy
-
host
.
com
suser
=
masked_user
src
=
1.1.1.1
requestMethod
=
GET
request
=
https
:
//
vstmr
.
dummy
-
host
.
com
/
_signalr
/
connect
?
to
ken
=
MASKED_TOKEN
app
=
HTTPS
cs3
=
HTTP
/
1.1
cs3Label
=
Protocol
/
Version
cs4
=
Business
,
Software
/
Hardware
cs4Label
=
URL
Categories
cs6
=
Minimal
Risk
cs6Label
=
Reputation
fileType
=
text
/
event
-
stream
out
=
19578
requestClientApplication
=
Mozilla
/
5.0
(
Windows
NT
10.0
;
Win64
;
x64
)
AppleWebKit
/
537.36
(
KHTML
,
like
Gecko
)
Chrome
/
143.0.0.0
Safari
/
537.36
cs1
=
cs1Label
=
Virus
Name
cn1
=
0
cn1Label
=
Block
Reason
cs5
=
Def
ault
cs5Label
=
Policy
"
UDM mapping table
Log Field
UDM Mapping
Logic
application_name
principal.application
Directly mapped from the
application_name
field in KV format or
user_agent_product
in JSON format.
auth_user
principal.user.userid
Directly mapped from the
auth_user
field in KV format.
block_reason
security_result.summary
Directly mapped from the
block_reason
field in JSON and CSV JSON formats, or
_block_reason
in raw format, or
block_reason
in KV format.
block_res
security_result.action
Mapped from
block_res
field in KV format. If
block_res
is
DENIED
or contains
Block
, the action is
BLOCK
. If
block_res
is
0
or contains
Allow
, the action is
ALLOW
. Special values like
50
,
51
,
52
,
53
,
58
,
59
,
81
,
80
,
82
,
83
,
84
,
110
,
111
are used to determine
security_result.category
.
bytes_from_client
network.sent_bytes
Directly mapped from the
bytes_from_client
field in KV format, or
sr_bytes
in raw format, or
client_to_server_bytes
in JSON and CSV JSON formats.
bytes_to_client
network.received_bytes
Directly mapped from the
bytes_to_client
field in KV format, or
rs_bytes
in raw format, or
server_to_client_bytes
in JSON and CSV JSON formats.
categories
security_result.category_details
Directly mapped from the
categories
field in KV format, or
_category
in raw format, or
category
in JSON and CSV JSON formats.
client_ip
principal.ip
,
intermediary.ip
Directly mapped from the
client_ip
field in JSON format.
clientIP
principal.ip
Directly mapped from the
clientIP
field in CEF format.
csmethod
network.http.method
Directly mapped from the
csmethod
field in raw format.
day
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format.
destination_ip
target.ip
Directly mapped from the
destination_ip
field in JSON format.
destination_port
target.port
Directly mapped from the
destination_port
field in JSON format.
domain
target.hostname
,
target.url
Directly mapped from the
domain
field in raw format. Used to construct the
target.url
if
uri
is present.
header
intermediary.hostname
Extracted from the beginning of the log message. Used to extract
intermediary.hostname
.
host
target.hostname
Directly mapped from the
host
field in KV format.
hostname
principal.hostname
Directly mapped from the
hostname
field in JSON format.
hour
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format.
http_action
network.http.method
Directly mapped from the
http_action
field in JSON format.
http_status_code
network.http.response_code
Directly mapped from the
http_status_code
field in JSON and CSV JSON formats, or
status_code
in raw and KV formats.
kv_entry.application_name
principal.application
Directly mapped from the
application_name
field within the KV entry.
kv_entry.auth_user
principal.user.userid
Directly mapped from the
auth_user
field within the KV entry.
kv_entry.block_reason
security_result.summary
Directly mapped from the
block_reason
field within the KV entry.
kv_entry.block_res
security_result.action
,
security_result.category
Mapped from
block_res
field within the KV entry. Logic for determining action and category is the same as for the top-level
block_res
field.
kv_entry.bytes_from_client
network.sent_bytes
Directly mapped from the
bytes_from_client
field within the KV entry.
kv_entry.bytes_to_client
network.received_bytes
Directly mapped from the
bytes_to_client
field within the KV entry.
kv_entry.categories
security_result.category_details
Directly mapped from the
categories
field within the KV entry.
kv_entry.host
target.hostname
Directly mapped from the
host
field within the KV entry.
kv_entry.method
network.http.method
Directly mapped from the
method
field within the KV entry.
kv_entry.rep_level
security_result.severity_details
Directly mapped from the
rep_level
field within the KV entry.
kv_entry.server_ip
target.ip
Directly mapped from the
server_ip
field within the KV entry.
kv_entry.status_code
network.http.response_code
Directly mapped from the
status_code
field within the KV entry.
kv_entry.time_stamp
metadata.event_timestamp
Directly mapped from the
time_stamp
field within the KV entry.
kv_entry.url
target.url
Directly mapped from the
url
field within the KV entry.
kv_entry.url_port
target.port
Directly mapped from the
url_port
field within the KV entry.
kv_entry.user_agent
network.http.parsed_user_agent
Directly mapped from the
user_agent
field within the KV entry, then parsed into a structured object.
last_rule
security_result.rule_name
Directly mapped from the
last_rule
field in JSON format.
loc
principal.location.country_or_region
Directly mapped from the
loc
field extracted from
tgt_ip_or_location
.
location
principal.location.country_or_region
Directly mapped from the
location
field in JSON format.
log.file.path
principal.process.file.full_path
Directly mapped from the
log.file.path
field in JSON format.
message
Various
The raw log message. Parsed differently depending on its format (raw, JSON, KV, CEF).
method
network.http.method
Directly mapped from the
method
field in KV and raw formats, or
http_action
in JSON format, or derived from CEF data. If the value is one of
GET
,
POST
,
HEAD
,
OPTIONS
,
PUT
,
CONNECT
, the
metadata.event_type
is set to
NETWORK_HTTP
. If the value is
-
or
CERTVERIFY
, the
metadata.event_type
is set to
NETWORK_CONNECTION
.
mins
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format.
month
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format, or
rt
field in CEF format.
monthday
metadata.event_timestamp
Part of the timestamp, extracted from the beginning of the log message.
protocol
network.application_protocol
Directly mapped from the
protocol
field in raw format, or
uri_scheme
in JSON format, or derived from the
url
field in KV format.
query
target.url
Directly mapped from the
query
field in raw format. Appended to the
url
field.
rep_level
security_result.severity_details
Directly mapped from the
rep_level
field in KV format, or
reputation
in JSON format, or
_risk
in raw format. Used to determine
security_result.severity
.
request
target.url
Directly mapped from the
request
field in CEF format.
requestClientApplication
network.http.user_agent
Directly mapped from the
requestClientApplication
field in CEF format.
requestContext
network.http.referral_url
Directly mapped from the
requestContext
field in CEF format.
requestMethod
network.http.method
Directly mapped from the
requestMethod
field in CEF format.
requested_host
target.url
Directly mapped from the
requested_host
field in JSON format. Used to construct the
target.url
if
requested_path
is also present.
requested_path
target.url
Directly mapped from the
requested_path
field in JSON format. Appended to
requested_host
to form the
target.url
.
request_timestamp
metadata.event_timestamp
Directly mapped from the
request_timestamp
field in JSON format.
result
security_result.action
,
security_result.category
Directly mapped from the
result
field in JSON and CSV JSON formats, or
block_res
in KV format. Used to determine
security_result.action
and
security_result.category
.
rt
metadata.event_timestamp
Directly mapped from the
rt
field in CEF format.
secs
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format.
server_ip
target.ip
Directly mapped from the
server_ip
field in KV format.
source_ip
principal.ip
Directly mapped from the
source_ip
field in JSON, CSV JSON, raw, and KV formats, or
src
in CEF format, or
src_ip
in raw format.
src
principal.ip
Directly mapped from the
src
field in CEF format.
status_code
network.http.response_code
Directly mapped from the
status_code
field in raw format.
summary
security_result.summary
Directly mapped from the
summary
field in CSV format, or
block_reason
in JSON format.
system
principal.platform
Directly mapped from the
system
field in JSON format. Converted to uppercase.
target_ip
target.ip
Directly mapped from the
target_ip
field in raw format, or
dst
in CEF format.
tgtport
target.port
Directly mapped from the
tgtport
field in raw format.
time
metadata.event_timestamp
Part of the timestamp, extracted from the beginning of the log message, or the
rt
field in CEF format, or the
time_stamp
field in KV format.
timestamp
metadata.event_timestamp
Directly mapped from the
@timestamp
field in JSON format.
timezone
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format.
uri
target.url
Directly mapped from the
uri
field in raw format. Used to construct the
target.url
.
uri_scheme
network.application_protocol
Directly mapped from the
uri_scheme
field in JSON format. Converted to uppercase.
url
target.url
Directly mapped from the
url
field in raw, KV, and JSON formats, or constructed from
domain
,
uri
, and
query
in raw format, or
requested_host
and
requested_path
in JSON format, or
request
in CEF format.
url_port
target.port
Directly mapped from the
url_port
field in KV format.
user
principal.user.userid
Directly mapped from the
user
field in JSON format, or
username
in JSON format, or
auth_user
in KV format, or
suser
in raw format.
user_agent
network.http.parsed_user_agent
Directly mapped from the
user_agent
field in raw and KV formats, or
user_agent_comment
in JSON format, or
requestClientApplication
in CEF format, or constructed from
agent.type
and
agent.version
in JSON format. Parsed into a structured object.
user_agent_comment
network.http.parsed_user_agent
Directly mapped from the
user_agent_comment
field in JSON format.
user_agent_product
principal.application
Directly mapped from the
user_agent_product
field in JSON format.
username
principal.user.userid
Directly mapped from the
username
field in JSON format.
year
metadata.event_timestamp
Part of the timestamp, extracted from the
time_stamp
field in KV format, or
rt
field in CEF format.
N/A
metadata.event_type
Determined by the parser based on the
method
field. Can be
NETWORK_HTTP
,
NETWORK_CONNECTION
,
GENERIC_EVENT
, or
STATUS_UPDATE
.
N/A
metadata.log_type
Hardcoded to
MCAFEE_WEBPROXY
.
N/A
metadata.product_name
Hardcoded to
MCAFEE_WEBPROXY
.
N/A
metadata.vendor_name
Hardcoded to
MCAFEE
.
N/A
network.direction
Hardcoded to
OUTBOUND
.
N/A
security_result.action
Determined by the parser based on the
block_reason
or
result
fields. Can be
ALLOW
or
BLOCK
.
N/A
security_result.category
Determined by the parser based on the
result
field. Can be
NETWORK_CATEGORIZED_CONTENT
,
NETWORK_DENIAL_OF_SERVICE
,
MAIL_SPAM
,
AUTH_VIOLATION
,
SOFTWARE_MALICIOUS
,
NETWORK_SUSPICIOUS
, or
NETWORK_MALICIOUS
.
N/A
security_result.severity
Determined by the parser based on the
risk
field. Can be
LOW
,
MEDIUM
, or
HIGH
.
Need more help?
Get answers from Community members and Google SecOps professionals.
