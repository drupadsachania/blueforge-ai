# Collect Microsoft Exchange logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/exchange-mail/  
**Scraped:** 2026-03-05T09:26:27.934398Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Exchange logs
Supported in:
Google secops
SIEM
This document explains how to ingest Microsoft Exchange logs to Google Security Operations using Bindplane. An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
EXCHANGE_MAIL
ingestion label.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows Server 2016 or later with Microsoft Exchange Server installed
Administrative access to the Exchange Server
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
Install the Bindplane agent on your Windows operating system according
to the following instructions.
Windows Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to collect Windows Event Logs and send to Google SecOps
Access the Configuration File:
Locate the
config.yaml
file. Typically, it's in the `C:\Program Files\observIQ OpenTelemetry Collector` directory on Windows.
Open the file using a text editor (for example, Notepad or Notepad++).
Edit the
config.yaml
file as follows:
receivers
:
windowseventlog/exchange_application
:
channel
:
Application
raw
:
true
max_reads
:
100
poll_interval
:
5s
start_at
:
end
windowseventlog/exchange_system
:
channel
:
System
raw
:
true
max_reads
:
100
poll_interval
:
5s
start_at
:
end
windowseventlog/exchange_management
:
channel
:
MSExchange Management
raw
:
true
max_reads
:
100
poll_interval
:
5s
start_at
:
end
processors
:
batch
:
exporters
:
chronicle/exchange
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded earlier
creds_file_path
:
'C:\path\to\ingestion-authentication-file.json'
# Replace with your actual customer ID
customer_id
:
<
PLACEHOLDER_CUSTOMER_ID
>
endpoint
:
<
YOUR_REGIONAL_ENDPOINT
>
# Add ingestion labels for Exchange logs
log_type
:
'EXCHANGE_MAIL'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/exchange
:
receivers
:
-
windowseventlog/exchange_application
-
windowseventlog/exchange_system
-
windowseventlog/exchange_management
processors
:
-
batch
exporters
:
-
chronicle/exchange
Replace
<PLACEHOLDER_CUSTOMER_ID>
with the actual Customer ID obtained earlier.
Replace
<YOUR_REGIONAL_ENDPOINT>
with the appropriate regional endpoint from the
Regional Endpoints documentation
.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Configuration notes
Application channel
: Collects application-level events from Exchange Server, including service startup, errors, and warnings.
System channel
: Collects system-level events that may affect Exchange Server operation.
MSExchange Management channel
: Collects Exchange-specific management events, including PowerShell cmdlet executions and administrative actions.
raw: true
: Sends complete Windows Event Log entries in their original format for comprehensive parsing.
start_at: end
: Begins collecting new events from the current point forward (does not ingest historical logs).
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command as an administrator:
net stop "observIQ OpenTelemetry Collector" && net start "observIQ OpenTelemetry Collector"
Supported Microsoft Exchange sample logs
Syslog + W3C
<
13
>
Jul
16
19
:
36
:
22
10.10.10.1
2020
-
07
-
16
23
:
36
:
06
10.10.10.2
POS
T
/
mapi
/
nspi
/
MailboxId
=
00000000
-
0000
-
0000
-
0000
-
000000000000
@
example
.
com
&
FrontEnd
=
SERVER01
.
EXAMPLE
.
LOCAL
&
RequestId
=
11111111
-
2222
-
3333
-
4444
-
555555555555
&
ClientRequestInfo
=
R
:
{
244982
AA
-
6563
-
4272
-
8
A81
-
6435
F8C98736
}
:
362
;
RT
:
PING
;
CI
:
{
F1037E72
-
B035
-
4
F6F
-
9
EE2
-
CDC028A174BD
}
:
5
;
CID
:
{
C0C8D580
-
5
B1A
-
48
D2
-
9285
-
D0981B30BCAF
}
&
ResponseInfo
=
XRC
:
0
&
Stage
=
BegR
:
2020
-
07
-
16
T23
:
36
:
06.0762130
Z
;
Pos
tAR
:
14
;
PreH
:
15
;
Pos
tH
:
15
;
End
R
:
15
444
Anonymous
192.168.1.5
Microsoft
+
Office
/
16.0
+
(
Windows
+
NT
+
10.0
;
+
Microsoft
+
Outlook
+
16.0.4954
;
+
Pro
)
-
200
0
0
25
10.0.0.1
,
10.0.0.2
JSON
{
"EventReceivedTime"
:
"2020-06-28 06:20:18"
,
"SourceModuleName"
:
"ExLogs"
,
"SourceModuleType"
:
"im_file"
,
"date-time"
:
"2020-06-28T10:00:52.987Z"
,
"connector-id"
:
"server-relay\\Anonymous Relay"
,
"session-id"
:
"08D91C389539A23E"
,
"sequence-number"
:
"4397"
,
"local-endpoint"
:
"10.0.0.1:25"
,
"remote-endpoint"
:
"192.168.1.100:30165"
,
"event"
:
"<"
,
"data"
:
"MAIL FROM:<sender@example.com>"
}
Syslog + CSV
<
13
>
May
17
11
:
56
:
05
SERVER01
Microsoft_Exchange_Server
:
2023
-
05
-
17
T15
:
56
:
05.260
Z
,
,
SERVER02
.
EXAMPLE
.
LOCAL
,
,
SERVER01
,
08
DB548089C89C20
;
2023
-
05
-
17
T15
:
56
:
05.135
Z
;
ClientSubmitTime
:,
,
STOREDRIVER
,
DELIVER
,
135536282960527
,
<
835115255.9114241684338954615.
JavaMail
.
app
@
example
.
com
>
,
00000000
-
0000
-
0000
-
0000
-
000000000000
,
sender
@
example
.
com
,
,
48294
,
1
,
,
,
Webinar
Subject
Line
,
recipient
@
example
.
com
,
bounce
-
address
@
bounce
.
example
.
com
,
2023
-
05
-
17
T15
:
56
:
04.064
Z
;
SRV
=
SERVER01
.
EXAMPLE
.
LOCAL
:
TO
TAL
-
FE
=
0.153
|
...
,
Incoming
,
,
10.10.10.1
,
10.10.10.2
,
S
:
IncludeInSla
=
True
;
...
;
S
:
AccountForest
=
EXAMPLE
.
LOCAL
,
Email
,
f351e35a
-
80
b8
-
462
a
-
197
a
-
08
db56ef38c4
,
15.02.0986.042
Pure CSV
2023
-
05
-
04
T11
:
01
:
06.971
Z
,
Inbound
Proxy
Int
ernal
Send
Connector
,
08
DB4283F358F976
,
231
,
10.0.0.1
:
21
,
192.168.1.50
:
25
,
>
,
MAIL
FROM
:
user
@
example
.
nl
SIZE
=
0
AUTH
=
<>
XMESSAGEVALUE
=
MediumHigh
,
Syslog + Key-Value
<
13
>
Feb
08
12
:
43
:
54
SERVER01
AgentDevice
=
MicrosoftExchange
AgentLogFile
=
u_ex240208
.
log
PluginVersion
=
7.3.1.22
AgentLogFormat
=
W3C
AgentLogProtocol
=
OWA
date
=
2024
-
02
-
08
time
=
10
:
43
:
49
s
-
ip
=
10.0.0.1
cs
-
method
=
POS
T
cs
-
uri
-
stem
=/
mapi
/
emsmdb
/
cs
-
uri
-
query
=
MailboxId
=
00000000
-
0000
-
0000
-
0000
-
000000000000
@
example
.
com&CorrelationID
=
<
empty
>
;
&
ClientRequestInfo
=
R
:
{
19
C548BA
-
F616
-
4021
-
B925
-
5716
E62B5CB3
}
:
3105
;
RT
:
Not
if
icationWait
;
CI
:
{
518670
B4
-
ADF1
-
4
C59
-
8
A26
-
377
C3F9B7DAB
}
:
62560018
;
CID
:
{
111677
F0
-
FEB1
-
4194
-
9
DAC
-
CC0437A5AD5F
}
&
cafeReqId
=
310
eebda
-
23
e9
-
46
cd
-
9576
-
e9892bcaffd0
;
s
-
port
=
443
cs
-
username
=
EXAMPLE
\
user
c
-
ip
=
192.168.1.10
cs
(
User
-
Agent
)
=
Microsoft
+
Office
/
16.0
+
(
Windows
+
NT
+
10.0
;
+
Microsoft
+
Outlook
+
16.0.10382
;
+
Pro
)
cs
(
Referer
)
=-
sc
-
status
=
200
sc
-
substatus
=
0
sc
-
win32
-
status
=
0
time
-
taken
=
357708
CEF
CEF
:
0
|
Microsoft
|
Exchange
|
15.2
|
Mailbox
|
Deliver
|
3
|
src
=
10.10
.
10.5
dst
=
192.168
.
1.20
suser
=
sender
@
example
.
com
duser
=
recipient
@
example
.
com
suid
=
DOMAIN
\
sender
duid
=
DOMAIN
\
recipient
msg
=
Message
Subject
Line
cs1Label
=
OriginalIP
cs1
=
172.16
.
0.1
cn1Label
=
MessageSize
cn1
=
45000
UDM Mapping
Log field
UDM mapping
Logic
c-ip
read_only_udm.target.asset.ip
Value taken from 'c-ip' field
c-ip
read_only_udm.target.ip
Value taken from 'c-ip' field
client-hostname
read_only_udm.principal.asset.hostname
Value taken from 'client-hostname' field
client-hostname
read_only_udm.principal.hostname
Value taken from 'client-hostname' field
client-ip
read_only_udm.principal.asset.ip
Value taken from 'client-ip' field
client-ip
read_only_udm.principal.ip
Value taken from 'client-ip' field
column1
read_only_udm.metadata.event_timestamp
Value taken from 'column1' field
column10
read_only_udm.intermediary.resource.attribute.labels.value
Value taken from 'column10' field
column11
read_only_udm.network.email.mail_id
Value taken from 'column11' field
column12
read_only_udm.additional.fields.value.string_value
Value taken from 'column12' field
column13
read_only_udm.network.email.to
Value taken from 'column13' field
column13
read_only_udm.target.user.email_addresses
Value taken from 'column13' field
column15
read_only_udm.additional.fields.value.string_value
Value taken from 'column15' field
column16
read_only_udm.target.resource.attribute.labels.value
Value taken from 'column16' field
column19
read_only_udm.network.email.subject
Value taken from 'column19' field
column2
read_only_udm.principal.asset.ip
Value taken from 'column2' field
column2
read_only_udm.principal.ip
Value taken from 'column2' field
column20
read_only_udm.network.email.from
Value taken from 'column20' field
column20
read_only_udm.principal.user.email_addresses
Value taken from 'column20' field
column21
read_only_udm.security_result.detection_fields.value
Value taken from 'column21' field
column22
read_only_udm.security_result.description
Value taken from 'column22' field
column24
read_only_udm.additional.fields.value.string_value
Value taken from 'column24' field
column25
read_only_udm.principal.asset.ip
Value taken from 'column25' field
column25
read_only_udm.principal.ip
Value taken from 'column25' field
column26
read_only_udm.target.asset.ip
Value taken from 'column26' field
column26
read_only_udm.target.ip
Value taken from 'column26' field
column27
read_only_udm.security_result.detection_fields.value
Value taken from 'column27' field
column28
read_only_udm.additional.fields.value.string_value
Value taken from 'column28' field
column29
read_only_udm.metadata.product_log_id
Value taken from 'column29' field
column3
read_only_udm.principal.asset.hostname
Value taken from 'column3' field
column3
read_only_udm.principal.hostname
Value taken from 'column3' field
column30
read_only_udm.metadata.product_version
Value taken from 'column30' field
column4
read_only_udm.target.asset.ip
Value taken from 'column4' field
column4
read_only_udm.target.ip
Value taken from 'column4' field
column5
read_only_udm.target.asset.hostname
Value taken from 'column5' field
column5
read_only_udm.target.hostname
Value taken from 'column5' field
column6
read_only_udm.metadata.event_timestamp
Value taken from 'column6' field
column6
read_only_udm.network.http.response_code
Value taken from 'column6' field
column6
read_only_udm.network.session_id
Value taken from 'column6' field
column6
read_only_udm.metadata.description
Value taken from 'column6' field
column7
read_only_udm.additional.fields.value.string_value
Value taken from 'column7' field
column8
read_only_udm.additional.fields.value.string_value
Value taken from 'column8' field
column9
read_only_udm.metadata.product_event_type
Value taken from 'column9' field
connector_id
read_only_udm.additional.fields.value.string_value
Value taken from 'connector-id' field
cs-method
read_only_udm.network.http.method
Value taken from 'cs-method' field
cs-uri-query
read_only_udm.target.url
Value taken from 'cs-uri-query' field
cs-uri-stem
read_only_udm.target.url
Value taken from 'cs-uri-stem' field
csReferer
read_only_udm.network.http.referral_url
Value taken from 'csReferer' field
csUser-Agent
read_only_udm.network.http.user_agent
Value taken from 'csUser-Agent' field
cs-username
read_only_udm.principal.user.userid
Value taken from 'cs-username' field
custom-data
read_only_udm.security_result.detection_fields.value
Value taken from 'custom-data' field
data
read_only_udm.security_result.about.labels.value
Value taken from 'data' field
data
read_only_udm.security_result.description
Value taken from 'data' field
data
read_only_udm.network.email.from
Value taken from 'data' field
data
read_only_udm.network.email.to
Value taken from 'data' field
data
read_only_udm.target.hostname
Value taken from 'data' field
data
read_only_udm.security_result.description
Value taken from 'data' field
data
read_only_udm.network.sent_bytes
Value taken from 'data' field
data
read_only_udm.target.user.email_addresses
Value taken from 'data' field
date
read_only_udm.metadata.event_timestamp
Value taken from 'date' and 'time' fields
date-time
read_only_udm.metadata.event_timestamp
Value taken from 'date-time' field
DeliveryLatency
read_only_udm.security_result.detection_fields.value
Value taken from 'DeliveryLatency' field in 'custom-data' or 'message-info'
DeliveryPriority
read_only_udm.security_result.detection_fields.value
Value taken from 'DeliveryPriority' field in 'custom-data' or 'column21' field
DeliveryPriority
read_only_udm.security_result.priority
If 'DeliveryPriority' is 'Low' or 'Normal' then 'LOW_PRIORITY', if 'DeliveryPriority' is 'Medium' then 'MEDIUM_PRIORITY', if 'DeliveryPriority' is 'High' then 'HIGH_PRIORITY'
directionality
read_only_udm.network.direction
If 'directionality' is 'Incoming' then 'INBOUND', if 'directionality' is 'Originating' then 'OUTBOUND'
E2ELatency
read_only_udm.security_result.detection_fields.value
Value taken from 'E2ELatency' field in 'custom-data' or 'message-info'
event
read_only_udm.metadata.product_event_type
If 'event' is '+' then 'Connect', if 'event' is '-' then 'Disconnect', if 'event' is '*' then 'Information', if 'event' is '>' then 'Send', if 'event' is '<' then 'Receive'
event
read_only_udm.network.direction
If 'event' is '>' then 'OUTBOUND', if 'event' is '<' then 'INBOUND'
EventID
read_only_udm.security_result.detection_fields.value
Value taken from 'EventID' field
EventReceivedTime
read_only_udm.metadata.collected_timestamp
Value taken from 'EventReceivedTime' field
EventReceivedTime
read_only_udm.metadata.event_timestamp
Value taken from 'EventReceivedTime' field in 'column6'
FirstForestHop
read_only_udm.security_result.detection_fields.value
Value taken from 'FirstForestHop' field in 'custom-data'
FromEntity
read_only_udm.security_result.detection_fields.value
Value taken from 'FromEntity' field in 'custom-data' or 'message-info'
guid
read_only_udm.metadata.product_log_id
Value taken from 'guid' field
Hostname
read_only_udm.principal.asset.hostname
Value taken from 'Hostname' field
Hostname
read_only_udm.principal.hostname
Value taken from 'Hostname' field
IncludeInSla
read_only_udm.security_result.detection_fields.value
Value taken from 'IncludeInSla' field in 'custom-data' or 'message-info'
internal-message-id
read_only_udm.intermediary.resource.attribute.labels.value
Value taken from 'internal-message-id' field
IsProbe
read_only_udm.security_result.detection_fields.value
Value taken from 'IsProbe' field in 'custom-data' or 'column21' field
Keywords
read_only_udm.security_result.detection_fields.value
Value taken from 'Keywords' field
local-endpoint
read_only_udm.principal.asset.ip
Value taken from 'local-endpoint' field
local-endpoint
read_only_udm.principal.ip
Value taken from 'local-endpoint' field
local-endpoint
read_only_udm.principal.port
Value taken from 'local-endpoint' field
Mailboxes
read_only_udm.security_result.detection_fields.value
Value taken from 'Mailboxes' field in 'custom-data' or 'message-info'
MailboxDatabaseGuid
read_only_udm.security_result.detection_fields.value
Value taken from 'MailboxDatabaseGuid' field in 'custom-data' or 'message-info'
MAIL FROM
read_only_udm.network.email.from
Value taken from 'MAIL FROM' field in 'data'
MAIL FROM
read_only_udm.principal.user.email_addresses
Value taken from 'MAIL FROM' field in 'data'
MAIL From
read_only_udm.network.email.from
Value taken from 'MAIL From' field in 'data'
MAIL From
read_only_udm.principal.user.email_addresses
Value taken from 'MAIL From' field in 'data'
message-id
read_only_udm.network.email.mail_id
Value taken from 'message-id' field
message-info
read_only_udm.security_result.detection_fields.value
Value taken from 'message-info' field
message-info
read_only_udm.security_result.description
Value taken from 'message-info' field
MessageValue
read_only_udm.security_result.detection_fields.value
Value taken from 'MessageValue' field in 'custom-data'
message-subject
read_only_udm.network.email.subject
Value taken from 'message-subject' field
method
read_only_udm.network.http.method
Value taken from 'method' field
Microsoft_Exchange_Transport_MailRecipient_RequiredTlsAuthLevel
read_only_udm.security_result.detection_fields.value
Value taken from 'Microsoft_Exchange_Transport_MailRecipient_RequiredTlsAuthLevel' field in 'custom-data'
MsgRecipCount
read_only_udm.security_result.detection_fields.value
Value taken from 'MsgRecipCount' field in 'custom-data' or 'message-info'
network-message-id
read_only_udm.additional.fields.value.string_value
Value taken from 'network-message-id' field
OriginalFromAddress
read_only_udm.principal.user.email_addresses
Value taken from 'OriginalFromAddress' field in 'custom-data' or 'column21' field
P2RecipStat
read_only_udm.security_result.detection_fields.value
Value taken from 'P2RecipStat' field in 'custom-data' or 'message-info'
PersistProbeTrace
read_only_udm.security_result.detection_fields.value
Value taken from 'PersistProbeTrace' field in 'custom-data' or 'column21' field
PrioritizationReason
read_only_udm.security_result.detection_fields.value
Value taken from 'PrioritizationReason' field in 'custom-data'
ProbeType
read_only_udm.security_result.detection_fields.value
Value taken from 'ProbeType' field in 'custom-data' or 'column21' field
ProcessID
read_only_udm.principal.process.pid
Value taken from 'ProcessID' field
ProxiedClientHostname
read_only_udm.intermediary.hostname
Value taken from 'ProxiedClientHostname' field in 'custom-data'
ProxiedClientIPAddress
read_only_udm.intermediary.asset.ip
Value taken from 'ProxiedClientIPAddress' field in 'custom-data'
ProxiedClientIPAddress
read_only_udm.intermediary.ip
Value taken from 'ProxiedClientIPAddress' field in 'custom-data'
ProxyHop1
read_only_udm.security_result.detection_fields.value
Value taken from 'ProxyHop1' field in 'custom-data'
RCPT TO
read_only_udm.network.email.to
Value taken from 'RCPT TO' field in 'data'
RCPT TO
read_only_udm.target.user.email_addresses
Value taken from 'RCPT TO' field in 'data'
RCPT To
read_only_udm.network.email.to
Value taken from 'RCPT To' field in 'data'
RCPT To
read_only_udm.target.user.email_addresses
Value taken from 'RCPT To' field in 'data'
recipient-address
read_only_udm.target.user.email_addresses
Value taken from 'recipient-address' field
recipient-count
read_only_udm.target.resource.attribute.labels.value
Value taken from 'recipient-count' field
recipient-status
read_only_udm.target.resource.attribute.labels.value
Value taken from 'recipient-status' field
remote-endpoint
read_only_udm.target.asset.ip
Value taken from 'remote-endpoint' field
remote-endpoint
read_only_udm.target.ip
Value taken from 'remote-endpoint' field
remote-endpoint
read_only_udm.target.port
Value taken from 'remote-endpoint' field
res_code
read_only_udm.network.http.response_code
Value taken from 'res_code' field
s-ip
read_only_udm.principal.asset.ip
Value taken from 's-ip' field
s-ip
read_only_udm.principal.ip
Value taken from 's-ip' field
s-port
read_only_udm.principal.port
Value taken from 's-port' field
sc-status
read_only_udm.network.http.response_code
Value taken from 'sc-status' field
sc-substatus
read_only_udm.additional.fields.value.string_value
Value taken from 'sc-substatus' field
sender-address
read_only_udm.network.email.from
Value taken from 'sender-address' field
sender-address
read_only_udm.principal.user.email_addresses
Value taken from 'sender-address' field
sequence-number
read_only_udm.additional.fields.value.number_value
Value taken from 'sequence-number' field
server-hostname
read_only_udm.target.asset.hostname
Value taken from 'server-hostname' field
server-hostname
read_only_udm.target.hostname
Value taken from 'server-hostname' field
server-ip
read_only_udm.target.asset.ip
Value taken from 'server-ip' field
server-ip
read_only_udm.target.ip
Value taken from 'server-ip' field
session-id
read_only_udm.network.session_id
Value taken from 'session-id' field
sessionid
read_only_udm.network.session_id
Value taken from 'sessionid' field
Severity
read_only_udm.security_result.severity
If 'Severity' contains 'Info' then 'INFORMATIONAL', if 'Severity' contains 'Error' then 'ERROR', if 'Severity' contains 'Warning' then 'MEDIUM', else 'UNKNOWN_SEVERITY'
SeverityValue
read_only_udm.security_result.severity_details
Value taken from 'SeverityValue' field
SlaExclusionReason
read_only_udm.security_result.detection_fields.value
Value taken from 'SlaExclusionReason' field in 'custom-data'
source
read_only_udm.additional.fields.value.string_value
Value taken from 'source' field
SourceModuleName
read_only_udm.principal.resource.name
Value taken from 'SourceModuleName' field
SourceModuleType
read_only_udm.principal.resource.type
Value taken from 'SourceModuleType' field
SourceName
read_only_udm.principal.resource.attribute.labels.value
Value taken from 'SourceName' field
StoreObjectIds
read_only_udm.security_result.detection_fields.value
Value taken from 'StoreObjectIds' field in 'custom-data' or 'message-info'
Task
read_only_udm.security_result.detection_fields.value
Value taken from 'Task' field
ThreadID
read_only_udm.security_result.detection_fields.value
Value taken from 'ThreadID' field
time
read_only_udm.metadata.event_timestamp
Value taken from 'date' and 'time' fields
ToEntity
read_only_udm.security_result.detection_fields.value
Value taken from 'ToEntity' field in 'custom-data' or 'message-info'
total-bytes
read_only_udm.additional.fields.value.string_value
Value taken from 'total-bytes' field
TransportTrafficSubType
read_only_udm.security_result.detection_fields.value
Value taken from 'TransportTrafficSubType' field in 'custom-data'
TransportTrafficSubType
read_only_udm.metadata.product_version
Value taken from 'TransportTrafficSubType' field in 'custom-data'
ts
read_only_udm.metadata.event_timestamp
Value taken from 'ts' field
u_agent
read_only_udm.network.http.user_agent
Value taken from 'u_agent' field
u_param
read_only_udm.target.url
Value taken from 'u_param' field
u_path
read_only_udm.target.url
Value taken from 'u_path' field
u_path
read_only_udm.target.url
Value taken from 'u_path' and 'u_param' fields
user
read_only_udm.target.user.userid
Value taken from 'user' field
user
read_only_udm.target.user.email_addresses
Value taken from 'user' field
metadata.event_type
read_only_udm.metadata.event_type
If 'has_principal_email' is 'true' and 'has_target_email' is 'true' then 'EMAIL_TRANSACTION', if 'event_type' is 'GENERIC_EVENT' and 'principal_hostname' or 's_ip' or 'host' is not empty or 'has_principal' is 'true' then 'STATUS_UPDATE', if 'event_type' is 'GENERIC_EVENT' and 'has_principal_email' is 'true' or 'has_target_email' is 'true' then 'USER_UNCATEGORIZED', else value taken from 'event_type' field
metadata.log_type
read_only_udm.metadata.log_type
Hardcoded value 'EXCHANGE_MAIL'
metadata.product_name
read_only_udm.metadata.product_name
Hardcoded value 'Exchange Mail'
metadata.vendor_name
read_only_udm.metadata.vendor_name
Hardcoded value 'Microsoft'
network.application_protocol
read_only_udm.network.application_protocol
If 'app_protocol' is 'SMTP' or 'HTTP' or 'HTTPS' then value taken from 'app_protocol' field, if 'app_protocol' contains 'SMTP' then 'SMTP'
network.direction
read_only_udm.network.direction
If 's_ip' is not empty then 'INBOUND'
network.email.from
read_only_udm.network.email.from
Value taken from 'from_mail' field
network.email.mail_id
read_only_udm.network.email.mail_id
Value taken from 'msg_id' field
network.email.subject
read_only_udm.network.email.subject
Value taken from 'column19' field
network.email.to
read_only_udm.network.email.to
Value taken from 'to_mail' field
network.http.method
read_only_udm.network.http.method
Value taken from 'method' field
network.http.response_code
read_only_udm.network.http.response_code
Value taken from 'res_code' field
network.http.user_agent
read_only_udm.network.http.user_agent
Value taken from 'u_agent' field
network.sent_bytes
read_only_udm.network.sent_bytes
Value taken from 'sent_bytes' field
network.session_id
read_only_udm.network.session_id
Value taken from 'sessionid' field
principal.asset.hostname
read_only_udm.principal.asset.hostname
Value taken from 'principal_hostname' field
principal.asset.hostname
read_only_udm.principal.asset.hostname
Value taken from 'host' field
principal.asset.hostname
read_only_udm.principal.asset.hostname
Value taken from 'column3' field
principal.asset.ip
read_only_udm.principal.asset.ip
Value taken from 'column2' field
principal.asset.ip
read_only_udm.principal.asset.ip
Value taken from 'column25' field
principal.asset.ip
read_only_udm.principal.asset.ip
Value taken from 's_ip' field
principal.hostname
read_only_udm.principal.hostname
Value taken from 'principal_hostname' field
principal.hostname
read_only_udm.principal.hostname
Value taken from 'host' field
principal.hostname
read_only_udm.principal.hostname
Value taken from 'column3' field
principal.ip
read_only_udm.principal.ip
Value taken from 'column2' field
principal.ip
read_only_udm.principal.ip
Value taken from 'column25' field
principal.ip
read_only_udm.principal.ip
Value taken from 's_ip' field
principal.port
read_only_udm.principal.port
Value taken from 's-port' field
principal.user.email_addresses
read_only_udm.principal.user.email_addresses
Value taken from 'mail' field
principal.user.email_addresses
read_only_udm.principal.user.email_addresses
Value taken from 'email_address' field
principal.user.userid
read_only_udm.principal.user.userid
Value taken from 'cs-username' field
security_result.about.labels.key
read_only_udm.security_result.about.labels.key
Hardcoded value 'Response Code'
security_result.description
read_only_udm.security_result.description
Value taken from 'context' field
security_result.description
read_only_udm.security_result.description
Value taken from 'column22' field
security_result.priority
read_only_udm.security_result.priority
If 'severity' is '1' or '2' or '3' then 'LOW', if 'severity' is '4' or '5' or '6' then 'MEDIUM', if 'severity' is '7' or '8' or '9' then 'HIGH'
security_result.severity
read_only_udm.security_result.severity
If 'Severity' contains 'Info' then 'INFORMATIONAL', if 'Severity' contains 'Error' then 'ERROR', if 'Severity' contains 'Warning' then 'MEDIUM', else 'UNKNOWN_SEVERITY'
target.administrative_domain
read_only_udm.target.administrative_domain
Value taken from 'domain' field
target.asset.hostname
read_only_udm.target.asset.hostname
Value taken from 'column5' field
target.asset.hostname
read_only_udm.target.asset.hostname
Value taken from 'target_host' field
target.asset.ip
read_only_udm.target.asset.ip
Value taken from 'column4' field
target.asset.ip
read_only_udm.target.asset.ip
Value taken from 'column26' field
target.asset.ip
read_only_udm.target.asset.ip
Value taken from 'c-ip' field
target.hostname
read_only_udm.target.hostname
Value taken from 'column5' field
target.hostname
read_only_udm.target.hostname
Value taken from 'target_host' field
target.ip
read_only_udm.target.ip
Value taken from 'column4' field
target.ip
read_only_udm.target.ip
Value taken from 'column26' field
target.ip
read_only_udm.target.ip
Value taken from 'c-ip' field
target.port
read_only_udm.target.port
Value taken from 'c_port' field
target.resource.attribute.labels.key
read_only_udm.target.resource.attribute.labels.key
Hardcoded value 'Recipients Count'
target.user.email_addresses
read_only_udm.target.user.email_addresses
Value taken from 'user' field
target.user.user_display_name
read_only_udm.target.user.user_display_name
Value taken from 'username' field
target.user.userid
read_only_udm.target.user.userid
Value taken from 'user' field
target.url
read_only_udm.target.url
Value taken from 'u_path' field
Need more help?
Get answers from Community members and Google SecOps professionals.
