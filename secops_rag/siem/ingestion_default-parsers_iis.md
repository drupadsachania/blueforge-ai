# Collect Microsoft IIS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iis/  
**Scraped:** 2026-03-05T09:26:30.785050Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft IIS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Microsoft Internet Information Services (IIS) logs to Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows Server 2016 or later with IIS installed
Administrative access to the IIS server
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
. Save the file securely on the system where Bindplane will be installed (for example,
C:\SecOps\ingestion-auth.json
).
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
Configure IIS W3C Extended Logging
You must enable the correct W3C fields in IIS Manager so Google SecOps can parse your logs properly and detections work reliably.
Open IIS Manager
Click
Start
.
Type
inetmgr
and press
Enter
.
The
Internet Information Services (IIS) Manager
window opens.
Alternative method:
Press
Windows Key + R
.
Type
inetmgr
and press
Enter
.
Navigate to Logging Configuration
In the
Connections
pane (left side), expand your server name.
To configure server-wide logging (recommended):
Click the
server name
at the root level.
To configure site-specific logging:
Expand
Sites
and then click the specific site (for example,
Default Web Site
).
In the
Features View
(center pane), double-click
Logging
.
Select W3C Extended Log Format
On the
Logging
page, under
Log File
section:
In the
Format
drop-down, select
W3C
.
Click
Select Fields
button.
Configure W3C Logging Fields
IMPORTANT:
The Google SecOps IIS parser supports
8 field configurations
. You must enable
ALL fields
from
ONE
of the following patterns. Enabling different fields or mixing patterns will cause parsing failures.
In the
W3C Logging Fields
dialog, select fields according to
ONE
of the following patterns:
Pattern 1: Full Site Context with Query String and Bytes
Enable these fields in this exact order:
Date
(date)
Time
(time)
Service Name
(s-sitename)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Server Port
(s-port)
User Name
(cs-username)
Client IP Address
(c-ip)
User Agent
(cs(User-Agent))
Referer
(cs(Referer))
Protocol Status
(sc-status)
Bytes Sent
(sc-bytes)
Bytes Received
(cs-bytes)
Use this pattern when:
Your downstream format includes site context + query string and you require sent/received bytes, and your pipeline expects the "username" and "referer" columns (even if values are
-
).
Pattern 2: Basic with Substatus, Win32 Status, and Performance (No Referer)
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Server Port
(s-port)
User Name
(cs-username)
Client IP Address
(c-ip)
User Agent
(cs(User-Agent))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Time Taken
(time-taken)
Use this pattern when:
Your pipeline does
not
include Referer, but you need detailed error codes and latency (
time-taken
).
Pattern 3: Basic with Substatus, Win32 Status, and Performance (With Referer)
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Server Port
(s-port)
User Name
(cs-username)
Client IP Address
(c-ip)
User Agent
(cs(User-Agent))
Referer
(cs(Referer))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Time Taken
(time-taken)
Use this pattern when:
Same as Pattern 2, but your pipeline includes Referer as a dedicated column.
Pattern 4: TLS/Protocol-Version Aware with Referrer and Performance
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Client Port
(c-port)
User Name
(cs-username)
Client IP Address
(c-ip)
Protocol Version
(cs-version)
User Agent
(cs(User-Agent))
Referer
(cs(Referer))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Time Taken
(time-taken)
Use this pattern when:
Your downstream format explicitly logs
cs-version
(e.g.,
HTTP/1.1
) and includes timing, and you also have client port as a dedicated column.
Pattern 5: TLS/Protocol-Version Aware with Referrer (No Performance)
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Client Port
(c-port)
User Name
(cs-username)
Client IP Address
(c-ip)
Protocol Version
(cs-version)
User Agent
(cs(User-Agent))
Referer
(cs(Referer))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Use this pattern when:
Same as Pattern 4, but your pipeline does not include
time-taken
.
Pattern 6: With Cookie and Referer (No Performance, No Bytes)
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Client Port
(c-port)
User Name
(cs-username)
Client IP Address
(c-ip)
User Agent
(cs(User-Agent))
Cookie
(cs(Cookie))
Referer
(cs(Referer))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Use this pattern when:
Your downstream format expects both Cookie and Referer as dedicated columns.
Pattern 7: Minimal with Referer (No Cookie, No Performance, No Bytes)
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Client Port
(c-port)
User Name
(cs-username)
Client IP Address
(c-ip)
User Agent
(cs(User-Agent))
Referer
(cs(Referer))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Use this pattern when:
Your downstream format includes Referer but does not include Cookie/time/bytes.
Pattern 8: Minimal without Referer (No Cookie, No Performance, No Bytes)
Enable these fields in this exact order:
Date
(date)
Time
(time)
Server IP Address
(s-ip)
Method
(cs-method)
URI Stem
(cs-uri-stem)
URI Query
(cs-uri-query)
Client Port
(c-port)
User Name
(cs-username)
Client IP Address
(c-ip)
User Agent
(cs(User-Agent))
Protocol Status
(sc-status)
Protocol Substatus
(sc-substatus)
Win32 Status
(sc-win32-status)
Use this pattern when:
Your downstream format does not include Referer and you only need core request context plus status codes.
Do NOT enable fields from multiple patterns.
The parser expects one of these exact configurations.
Apply Configuration
Click
OK
to close the
W3C Logging Fields
dialog.
Verify the
Directory
path where logs will be written.
Default:
%SystemDrive%\inetpub\logs\LogFiles
Under
Log File Rollover
, select
Daily
(recommended for Google SecOps ingestion).
Click
Apply
in the
Actions
pane (right side).
Verify IIS Logging
After configuring the W3C fields, verify that IIS is writing logs correctly:
Generate test traffic to your IIS site by opening a web page in a browser.
Navigate to the log directory:
C:\inetpub\logs\LogFiles\W3SVC1\
Note:
W3SVC1
corresponds to the first site (Default Web Site). For other sites, the folder name will be
W3SVC2
,
W3SVC3
, etc.
Open the most recent log file (for example,
u_ex251217.log
) in Notepad.
Verify the
#Fields:
line contains all the fields you enabled in the exact order from your chosen pattern.
Example for Pattern 3
If you configured
Pattern 3
(Basic with Substatus, Win32 Status, and Performance with Referer), the
#Fields:
line should be:
#Fields: date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken
Example log entry:
2025
-
12
-
17
14
:
23
:
15
192.168.1.10
GET
/
index
.
html
-
80
-
203.0.113.45
Mozilla
/
5.0
+
(
Windows
+
NT
+
10.0
)
https
:
//
example
.
com
/
previous
.
html
200
0
0
125
Important notes:
Empty fields are represented by a hyphen (
-
)
Field order must match the
#Fields:
header exactly
The parser will fail if fields are missing, reordered, or from multiple patterns
Install the Bindplane agent
Install the Bindplane agent on your Windows server according to the following instructions.
Windows Installation
Open
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
Configure the Bindplane agent to ingest IIS logs and send them to Google SecOps
Edit the Configuration File
Locate the
config.yaml
file.
Default path:
C:\Program Files\observIQ OpenTelemetry Collector\config.yaml
Open the file using a text editor (for example, Notepad, VS Code, or Notepad++) as Administrator.
Replace the entire contents with the following configuration:
receivers
:
iis
:
collection_interval
:
60s
processors
:
resourcedetection
:
detectors
:
[
"system"
]
system
:
hostname_sources
:
[
"os"
]
normalizesums
:
batch
:
exporters
:
chronicle/iis
:
endpoint
:
malachiteingestion-pa.googleapis.com
creds
:
'C:\SecOps\ingestion-auth.json'
log_type
:
'IIS'
override_log_type
:
false
raw_log_field
:
body
customer_id
:
'<CUSTOMER_ID>'
compression
:
gzip
service
:
pipelines
:
logs/iis
:
receivers
:
-
iis
processors
:
-
resourcedetection
-
normalizesums
-
batch
exporters
:
-
chronicle/iis
Update Configuration Values
Replace the following placeholders:
creds:
- Path to your ingestion authentication file (for example,
C:\SecOps\ingestion-auth.json
).
endpoint:
- your regional endpoint.
customer_id:
- Your actual Google SecOps customer ID from the
Get Google SecOps customer ID
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop observiq-otel-collector && net start observiq-otel-collector
UDM Mapping Table
Log field
UDM mapping
Logic
@timestamp
metadata.event_timestamp
The timestamp of the event as recorded in the raw log.
@version
metadata.product_version
The version of the IIS server.
AgentDevice
additional.fields.AgentDevice.value.string_value
The device that generated the log.
AgentLogFile
additional.fields.AgentLogFile.value.string_value
The name of the log file.
ASP.NET_SessionId
network.session_id
The session ID of the user.
c-ip
principal.ip
The IP address of the client.
Channel
security_result.about.resource.attribute.labels.Channel.value
The channel where the event was logged.
ChannelID
security_result.about.resource.attribute.labels.ChannelID.value
The ID of the channel where the event was logged.
Computer
target.hostname
The hostname of the target machine.
cs-bytes
network.received_bytes
The number of bytes received from the client.
cs-host
principal.hostname, principal.asset.hostname
The hostname of the client.
cs-method
network.http.method
The HTTP method used by the client.
cs-uri-query
target.url
The query string of the URL requested by the client.
cs-uri-stem
target.url
The path of the URL requested by the client.
cs-username
principal.user.user_display_name
The username of the client.
cs-version
network.tls.version_protocol
The HTTP version used by the client.
cs(Cookie)
Used to extract cookie information.
cs(Referer)
network.http.referral_url
The URL that referred the client to the current page.
cs(User-Agent)
network.http.user_agent
The user agent of the client.
csbyte
network.received_bytes
The number of bytes received from the client.
cshost
principal.hostname, principal.asset.hostname
The hostname of the client.
csip
principal.ip, principal.asset.ip
The IP address of the client.
csmethod
network.http.method
The HTTP method used by the client.
csreferer
network.http.referral_url
The URL that referred the client to the current page.
csuseragent
network.http.user_agent
The user agent of the client.
csusername
principal.user.user_display_name
The username of the client.
csversion
network.tls.version_protocol
The HTTP version used by the client.
date
Used to construct the event timestamp if the raw log timestamp is invalid.
description
security_result.description
A description of the event.
devicename
target.hostname
The hostname of the target machine.
dst_ip
target.ip, target.asset.ip
The IP address of the target machine.
dst_port
target.port
The port number of the target machine.
duration
The duration of the request in milliseconds.
EventEnqueuedUtcTime
additional.fields.EventEnqueuedUtcTime.value.string_value
The time when the event was enqueued in UTC.
EventID
metadata.product_log_id
The ID of the event.
EventProcessedUtcTime
additional.fields.EventProcessedUtcTime.value.string_value
The time when the event was processed in UTC.
EventTime
metadata.event_timestamp
The timestamp of the event.
EventType
metadata.product_event_type
The type of the event.
file_path
target.file.full_path
The full path of the file involved in the event.
FilterId
security_result.about.resource.attribute.labels.FilterId.value
The ID of the filter.
FilterKey
security_result.about.resource.attribute.labels.FilterKey.value
The key of the filter.
FilterName
security_result.about.resource.attribute.labels.FilterName.value
The name of the filter.
FilterType
security_result.about.resource.attribute.labels.FilterType.value
The type of the filter.
host
target.hostname
The hostname of the target machine.
host.architecture
principal.asset.hardware.cpu_platform
The architecture of the host machine.
host.geo.name
additional.fields.geo_name.value.string_value
The geographical location of the host machine.
host.hostname
target.hostname, target.asset.hostname
The hostname of the host machine.
host.id
observer.asset_id
The ID of the host machine.
host.ip
principal.ip, principal.asset.ip
The IP address of the host machine.
host.mac
principal.mac
The MAC address of the host machine.
host.os.build
additional.fields.os_build.value.string_value
The build number of the operating system on the host machine.
host.os.kernel
principal.platform_patch_level
The kernel version of the operating system on the host machine.
host.os.name
additional.fields.os_name.value.string_value
The name of the operating system on the host machine.
host.os.platform
principal.platform
The platform of the operating system on the host machine.
host.os.version
principal.platform_version
The version of the operating system on the host machine.
http_method
network.http.method
The HTTP method used by the client.
http_response
network.http.response_code
The HTTP response code.
http_status_code
network.http.response_code
The HTTP status code of the response.
http_substatus
additional.fields.sc_substatus.value.string_value
The HTTP substatus code of the response.
instance
additional.fields.instance.value.string_value
The instance ID of the task.
intermediary_devicename
intermediary.hostname, intermediary.asset.hostname
The hostname of the intermediary device.
json_message
The raw log message in JSON format.
kv_fields
Used to extract key-value pairs from the raw log message.
LayerKey
security_result.about.resource.attribute.labels.LayerKey.value
The key of the layer.
LayerName
security_result.about.resource.attribute.labels.LayerName.value
The name of the layer.
LayerId
security_result.about.resource.attribute.labels.LayerId.value
The ID of the layer.
log.file.path
target.file.full_path
The full path of the log file.
log.offset
metadata.product_log_id
The offset of the event in the log file.
logstash.collect.host
observer.hostname
The hostname of the machine that collected the log.
logstash.process.host
intermediary.hostname
The hostname of the machine that processed the log.
logstash_json_message
The raw log message in JSON format.
message
security_result.description
The raw log message.
ministry
additional.fields.ministry.value.string_value
The ministry associated with the event.
name
The name of the entity.
NewValue
additional.fields.NewValue.value.string_value
The new value of the configuration setting.
OldValue
additional.fields.OldValue.value.string_value
The old value of the configuration setting.
port
principal.port
The port number of the client.
priority_code
The priority code of the syslog message.
ProcessID
principal.process.pid
The process ID of the process that generated the event.
ProviderGuid
security_result.about.resource.attribute.labels.ProviderGuid.value
The GUID of the provider.
ProviderKey
security_result.about.resource.attribute.labels.ProviderKey.value
The key of the provider.
ProviderName
security_result.about.resource.attribute.labels.ProviderName.value
The name of the provider.
referrer_url
network.http.referral_url
The URL that referred the client to the current page.
request_url
target.url
The URL requested by the client.
s-computername
target.hostname
The hostname of the target machine.
s-ip
target.ip, target.asset.ip
The IP address of the target machine.
s-port
target.port
The port number of the target machine.
s-sitename
additional.fields.sitename.value.string_value
The name of the site.
sc-bytes
network.sent_bytes
The number of bytes sent to the client.
sc-status
network.http.response_code
The HTTP status code of the response.
sc-substatus
additional.fields.sc_substatus.value.string_value
The HTTP substatus code of the response.
sc-win32-status
The Windows status code of the response.
scbyte
network.sent_bytes
The number of bytes sent to the client.
scstatus
network.http.response_code
The HTTP status code of the response.
severity
security_result.severity
The severity of the event.
service.type
additional.fields.service_type.value.string_value
The type of the service.
sIP
principal.ip, principal.asset.ip
The IP address of the client.
sPort
principal.port
The port number of the client.
sSiteName
additional.fields.sitename.value.string_value
The name of the site.
src_ip
principal.ip, principal.asset.ip, observer.ip
The IP address of the client.
src_port
principal.port
The port number of the client.
sysdate
The date and time of the syslog message.
syslog_facility
security_result.severity_details
The facility of the syslog message.
syslog_pri
The priority of the syslog message.
syslog_severity
security_result.severity_details
The severity of the syslog message.
syslog_severity_code
The severity code of the syslog message.
tags
security_result.rule_name
Tags associated with the event.
task
additional.fields.task.value.string_value
The name of the task.
time
Used to construct the event timestamp if the raw log timestamp is invalid.
time-taken
The duration of the request in milliseconds.
uri_query
target.url
The query string of the URL requested by the client.
user_agent
network.http.user_agent
The user agent of the client.
UserName
target.user.userid
The username of the user.
UserSid
target.user.windows_sid
The Windows SID of the user.
Weight
security_result.about.resource.attribute.labels.Weight.value
The weight of the filter.
win32_status
The Windows status code of the response.
xforwardedfor
The X-Forwarded-For header, containing a comma-separated list of IP addresses.
metadata.log_type
"IIS"
network.direction
"INBOUND"
metadata.vendor_name
"Microsoft"
metadata.product_name
"Internet Information Server"
metadata.event_type
"NETWORK_HTTP", "USER_UNCATEGORIZED", "GENERIC_EVENT", "STATUS_UPDATE", "USER_LOGOUT", "USER_LOGIN"
extensions.auth.type
"MACHINE"
Need more help?
Get answers from Community members and Google SecOps professionals.
