# Collect OSSEC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ossec/  
**Scraped:** 2026-03-05T09:48:46.409462Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect OSSEC logs
Supported in:
Google secops
SIEM
This document describes how you can collect OSSEC logs by configuring OSSEC
and a Google Security Operations forwarder. This document also lists the supported log types
and supported OSSEC version.
For more information, see
Data ingestion to Google Security Operations
.
Overview
The following deployment architecture diagram shows how OSSEC agents and servers
are configured to send logs to Google Security Operations. Each customer deployment might
differ from this representation and might be more complex.
The architecture diagram shows the following components:
Linux system
. The Linux system to be monitored. The Linux system conists of
the files to monitor and the OSSEC agent.
Microsoft Windows system
. The Microsoft Windows system to be monitored in which the OSSEC agent
is installed.
OSSEC agent
. The OSSEC agent collects information from the Microsoft Windows or Linux
system and forwards the information to the OSSEC server.
OSSEC server
. The OSSEC server monitors and receives information from the
OSSEC agents. analyzes the logs, and forwards the logs to the Google Security Operations forwarder.
Bindplane agent
: The Bindplane agent fetches logs from osquery and sends logs to Google SecOps.
Google Security Operations forwarder
. The Google Security Operations forwarder is a lightweight
software component, deployed in the customer's network, that supports syslog.
The Google Security Operations forwarder forwards the logs to Google Security Operations.
Google Security Operations
. Google Security Operations retains and analyzes the logs from
the OSSEC server.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
OSSEC
ingestion label.
Before you begin
Ensure that the OSSEC agent is installed on the Microsoft Windows or Linux systems that
you plan to monitor. For more information about installing OSSEC agent, see
OSSEC installation
Use a OSSEC version that the Google Security Operations parser supports. The Google Security Operations
parser supports OSSEC version 3.6.0.
Ensure that the OSSEC server is installed and configured on the central Linux server.
Verify the log types that the Google Security Operations parser supports.
The following table list the products and log file paths that the Google Security Operations parser supports:
Operating system
Product
Log file path
Microsoft Windows
Microsoft Windows
Event logs
Linux
Linux
/var/log/audit/audit.log
Linux
Linux
/var/log/syslog
Linux
Linux
/var/log/ulog/syslogemu.log
Linux
apache2
/var/log/apache2/access.log
Linux
apache2
/var/log/apache2/error.log
Linux
apache2
/var/log/apache2/other_vhosts_access.log
Linux
apache2
/var/log/apache2/novnc-server-access.log
Linux
OpenVpn
/var/log/openvpnas.log
Linux
Nginx
/var/log/nginx/access.log
Linux
Nginx
/var/log/nginx/error.log
Linux
rkhunter
/var/log/rkhunter.log
Linux - OSSEC Server
OSSEC
/var/ossec/logs/ossec.log
Linux
Linux
/var/log/auth.log
Linux
Linux
/var/log/kern.log
Linux
rundeck
/var/log/rundeck/rundeck.api.log
Linux
rundeck
/var/log/rundeck/service.log
Linux
Samba
/var/log/samba/log.winbindd
Linux
Linux
/var/log/mail.log
Ensure that all systems in the deployment architecture are configured
in the UTC time zone.
Configure OSSEC agent and server, and Google Security Operations forwarder
To configure OSSEC agent and server, and the Google Security Operations forwarder, do the following:
To monitor the logs that the Linux systems generate, create an
ossec.conf
file to specify the log monitoring
configuration for the agent. Here is an example configuration file
for the agent on the Linux system:
<
ossec_config
>

<
!--
Files
to
monitor
(
localfiles
)
--
>
<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
ossec
/
logs
/
ossec
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
auth
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
kern
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
mail
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
syslog
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>apache
<
/
log_format
>
<
location
>
/
var
/
log
/
apache2
/
error
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>apache
<
/
log_format
>
<
location
>
/
var
/
log
/
apache2
/
access
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>apache
<
/
log_format
>
<
location
>
/
var
/
log
/
apache2
/
other_vhost_access
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>apache
<
/
log_format
>
<
location
>
/
var
/
log
/
apache2
/
nonvnc
-
server
-
access
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
nginx
/
access
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
nginx
/
error
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
openvpnas
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
rkhunter
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
rundeck
/
service
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
samba
/
log
.
winbindd
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>command
<
/
log_format
>
<
command>df
-
P
<
/
command
>
<
/
localfile
>

<
localfile
>
<
log_format>syslog
<
/
log_format
>
<
location
>
/
var
/
log
/
audit
/
audit
.
log
<
/
location
>
<
/
localfile
>

<
localfile
>
<
log_format>full_command
<
/
log_format
>
<
command>netstat
-
tan
|
grep
LISTEN
|
egrep
-
v
'(192.0.2.1| ::1)'
|
sort
<
/
command
>
<
/
localfile
>

<
localfile
>
<
log_format>full_command
<
/
log_format
>
<
command>last
-
n
5
<
/
command
>
<
/
localfile
>
<
/
ossec_config
>
To monitor the logs that the Microsoft Windows systems generate, create an
ossec.conf
file to specify the log monitoring configuration for the agent. Here is an example
configuration file for the agent on the Microsoft Windows system:
<ossec_config>
<!-- Channels to monitor (localfiles) -->
<localfile>
 <log_format>Security</log_format>
 <location>eventchannel</location>
</localfile>

<localfile>
 <log_format>System</log_format>
 <location>eventchannel</location>
</localfile>

<localfile>
 <log_format>Application</log_format>
 <location>eventchannel</location>
</localfile>
</ossec_config>
To forward the logs from the OSSEC server to Google Security Operations using the syslog protocol,
create the
syslog.conf
OSSEC server configuration file in the following format:
.
*
.
@<CHRONICLE_FORWARDER_IP>
:
<
CHRONICLE_FORWARDER_PORT
>
Configure the Google Security Operations forwarder to send logs to
Google Security Operations.
For more information, see
Installing and configuring the forwarder on Linux
.
The following is an example of a Google Security Operations forwarder configuration:
- syslog:
      common:
        enabled: true
        data_type: OSSEC
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 0.0.0.0:10514
      connection_timeout_sec: 60
Forward Logs to Google SecOps using Bindplane agent
Install and set up a
Linux Virtual Machine
.
Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see the
Bindplane agent installation and configuration instructions
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Supported OSSEC log formats
The OSSEC parser supports logs in SYSLOG+JSON, SYSLOG and SYSLOG+KV format.
Supported OSSEC sample logs
SYSLOG+JSON:
2022 Jan 30 23: 13: 05 (wintest) 198.51.100.0->EventChannel {
  "win": {
    "system": {
      "providerName": "Microsoft-Windows-PowerShell",
      "providerGuid": "{A0C1853B-5C40-ABCD-1234-3CF1C58F985A}",
      "eventID": "4104",
      "version": "1",
      "level": "5",
      "task": "2",
      "opcode": "15",
      "keywords": "0x0",
      "systemTime": "2021-07-29T12:57:03.579362300Z",
      "eventRecordID": "150518739",
      "processID": "16520",
      "threadID": "6036",
      "channel": "Microsoft-Windows-PowerShell/Operational",
      "computer": "WINTEST.cbn.local",
      "severityValue": "VERBOSE",
      "message": "\\"Creating Scriptblock text (1 of 1):\\""
    },
    "eventdata": {
      "messageNumber": "1",
      "messageTotal": "1",
      "scriptBlockText": "$global:?",
      "scriptBlockId": "8d4870bf-4032-5432-1234-51ae1e6a05d5"
    }
  }
}
SYSLOG:
2024/04/02 15:31:58 ossec-testrule: INFO: Reading local decoder file.
SYSLOG+KV:
2022 Jan 30 12:57:02 (ossectest) 198.51.100.0->/var/log/audit/audit.log type=LOGIN msg=audit(1627367436.123:8618732): pid=18281 uid=0 old-auid=1234967321 auid=996 tty=(none) old-ses=1234967321 ses=102952 res=1
Field mapping reference
This section explains how the Google Security Operations parser applies grok patterns for
Linux and Microsoft Windows systems and how it maps OSSEC log fields to Google Security Operations Unified Data Model (UDM) fields for each log type.
For information about mapping reference of common fields, see
Common fields
For reference information about log paths, grok patterns for example logs, event types,
and UDM fields on Linux systems, refer to the following sections:
Linux
Audit
Audit log event type
Mail
Mail log event type
For information about supported Microsoft Windows events and the corresponding UDM fields,
see
Microsoft Windows events data
Common fields
The following table lists the common log fields and their corresponding UDM fields.
Common log field
UDM field
collected_time
metadata.collected_timestamp
application
principal.application
log
metadata.description
ip
target.ip or principal.ip
hostname
target.hostname or principal.hostname
Linux system
The following table lists the log paths for Linux system, grok pattern for example logs,
event type, and UDM mappings:
Log path
Example log
Grok pattern
Event type
UDM mapping
/var/log/apache2/error.log
[Thu Apr 28 16:13:01.283342 2022] [core:notice] [pid 18394:tid 140188660751296] [client 1.200.32.47:59840] failed to make connection
[{timestamp}][{log_module}:{log_level}][pid{pid}(<optional_field>:tid{tid}|)](<optional_field> [client {client_ip}:{client_port}]|) (?<error_message>.*)
NETWORK_UNCATEGORIZED
timestamp is mapped to metadata.event_timestamp
log_module is mapped to target.resource.name
log_level is mapped to security_result.severity
pid is mapped to target.process.parent_process.pid
tid is mapped to target.process.pid
client_ip is mapped to principal.ip
client_port is mapped to principal.port
error_message is mapped to security_result.description
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/error.log
[Thu Apr 28 16:13:01.283342 2022] [core:notice] [pid 18394:tid 140188660751296] failed to make connection
[{timestamp}][{log_module}:{severity}][pid{pid}(<optional_field>:tid{tid}|)]{error_message}
NETWORK_UNCATEGORIZED
timestamp is mapped to metadata.event_timestamp
log_module is mapped to target.resource.name
log_level is mapped to security_result.severity
pid is mapped to target.process.parent_process.pid
tid is mapped to target.process.pid
error_message is mapped to security_result.description
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/error.log
[Thu Apr 28 16:13:01.283342 2022] [core:notice] [pid 18394:tid 140188660751296] AH00094: Command line: '/usr/sbin/apache2'
[{timestamp}][{log_module}:{log_level}][pid{pid}(<optional_field>:tid{tid}|)](<optional_field> [client {client_ip}:{client_port}]|) (?<error_message>.*),referer{referer_url}
NETWORK_UNCATEGORIZED
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
timestamp is mapped to metadata.event_timestamp
log_module is mapped to target.resource.name
log_level is mapped to security_result.severity
pid is mapped to target.process.parent_process.pid
tid is mapped to target.process.pid
client_ip is mapped to principal.ip
client_port is mapped to principal.port
error_message is mapped to security_result.description
target.platform is set to "LINUX"
referer_url is mapped to network.http.referral_url
/var/log/apache2/error.log
Sun Jan 30 15:14:47.260309 2022] [proxy_http:error] [pid 12515:tid 140035781285632] [client 1.200.32.47:59840] AH01114: HTTP: failed to make connection to backend: 192.0.2.1 , referer altostrat.com
[{timestamp}] [{log_module}:{log_level}] [pid {pid}(<optional_field>:tid{tid}|)] [client {client_ip}:{client_port}]( <message_text>HTTP: )?{error_message}:( {target_ip})(<optional_field>,referer{referer_url})?"
NETWORK_HTTP
timestamp is mapped to metadata.event_timestamp
log_module is mapped to target.resource.name
log_level is mapped to security_result.severity
pid is mapped to target.process.parent_process.pid
tid is mapped to target.process.pid
client_ip is mapped to principal.ip
client_port is mapped to principal.port
error_message is mapped to security_result.description
target_ip is mapped to target.ip
referer_url is mapped to network.http.referral_url
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/error.log
[Sat Feb 02 00:30:55 2019] New connection: [connection: gTxkX8Z6tjk] [client 192.0.2.1:50786]
[{timestamp}]<message_text>connection:[connection:{connection_id}][client{client_ip}:{client_port}]
NETWORK_UNCATEGORIZED
timestamp is mapped to metadata.event_timestamp
client_ip is mapped to principal.ip
client_port is mapped to principal.port
connection_id is mapped to network.session_id
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/error.log
[Sat Feb 02 00:30:55 2019] New request: [connection: j8BjX4Z5tjk] [request: ACtkX1Z5tjk] [pid 8] [client 192.0.2.1:50784]
[{timestamp}]<message_text>request:[connection:{connection_id}][request:{request_id}][pid{pid}][client{client_ip}:{client_port}]
NETWORK_UNCATEGORIZED
timestamp is mapped to metadata.event_timestamp
request_id is mapped to security_result.detection_fields.(key/value)
client_ip is mapped to principal.ip
client_port is mapped to principal.port
pid is mapped to target.process.parent_process.pid
connection_id is mapped to network.session_id
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/error.log
[Sat Feb 02 00:30:55 2019] [info] [C: j8BjX4Z5tjk] [R: p7pjX4Z5tjk] [pid 8] core.c(4739): [client 192.0.2.1:50784] AH00128: File does not exist: /usr/local/apache2/htdocs/favicon.ico
[{timestamp}] [{log_level}][C:{connection_id}][R:{request_id}][pid {pid}(<optional_field>:tid{tid}|)]<message_text>[client {client_ip}:{client_port}]{error_message}:{file_path}
NETWORK_UNCATEGORIZED
timestamp is mapped to metadata.event_timestamp
log_level is mapped to security_result.severity
request_id is mapped to security_result.detection_fields.(key/value)
client_ip is mapped to principal.ip
client_port is mapped to principal.port
pid is mapped to target.process.parent_process.pid
connection_id is mapped to network.session_id
error_message is mapped to security_result.description
file_path is mapped to target.file.full_path
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/access.log
10.50.0.1 - - [28/Apr/2022:18:02:13 +0530] "POST /test/first.html HTTP/1.1" 200 491 "http://192.0.2.1/test/first.html" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
({client_ip})?<message_text>{userid}[{timestamp}](<optional_field>{method}/(<optional_field>{resource}?) {client_protocol}?){result_status}{object_size}(<optional_field>(<optional_field>{referer_url}?)(<optional_field>{user_agent}?)?
NETWORK_HTTP
client_ip is mapped to principal.ip
userid is mapped to principal.user.userid
host is mapped to principal.hostname
timestamp is mapped to metadata.event_timestamp
method is mapped to network.http.method
resource is mapped to principal.resource.name
client_protocol is mapped to network.application_protocol
result_status is mapped to network.http.response_code
object_size is mapped to network.sent_bytes
referer_url is mapped to network.http.referral_url
user_agent is mapped to network.http.user_agent
network.ip_protocol is set to "TCP"
network.direction is set to "OUTBOUND"
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
var/log/apache2/other_vhosts_access.log
wintest.example.com:80 ::1 - - [14/Jan/2022:14:08:16 -0700] \"GET /server-status?auto HTTP/1.1\" 200 1415 \"-\" \"Python-urllib/2.7\"
{target_host}:{NUMBER:target_port} {client_ip} - (<optional_field>{host}?) [{timestamp}](<optional_field>{method}/(<optional_field>{resource}?){client_protocol}?){result_status}{object_size}(<optional_field>{referer_url}?)(<optional_field>{user_agent}?)
NETWORK_HTTP
target_host is mapped to target.hostname
target_port is mapped to target.port
client_ip is mapped to principal.ip
userid is mapped to principal.user.userid
host is mapped to principal.hostname
timestamp is mapped to metadata.event_timestamp
method is mapped to network.http.method
resource is mapped to principal.resource.name
result_status is mapped to network.http.response_code
object_size is mapped to network.sent_bytes
referer_url is mapped to network.http.referral_url
user_agent is mapped to network.http.user_agent
network.ip_protocol is set to "TCP"
network.direction is set to "OUTBOUND"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
network.application_protocol is set to "HTTP"
/var/log/apache2/access.log
"http://192.0.2.1/test/first.html" -> /altostrat.com
(<optional_field>{referer_url}?)->(<optional_field>{path}?)
GENERIC_EVENT
path is mapped to target.url
referer_url is mapped to network.http.referral_url
network.direction is set to "OUTBOUND"
target.platform is set to "LINUX"
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
/var/log/apache2/access.log
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Code/1.67.0 Chrome/98.0.4758.141 Electron/17.4.1 Safari/537.36
(<optional_field>{user_agent})
GENERIC_EVENT
user_agent is mapped to network.http.user_agent
network.direction is set to "OUTBOUND"
target.platform is set to "LINUX"
network.application_protocol is set to "HTTP"
target.platform is set to "LINUX"
metadata.vendor_name is set to "Apache"
metadata.product_name is set to "Apache HTTP Server"
var/log/nginx/access.log
172.16.19.228 - admin [05/May/2022:11:53:27 +0530] "GET /icons/ubuntu-logo.png HTTP/1.1" 404 209 "http://192.0.2.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
{principal_ip} - (<optional_field>{principal_user_userid}?) [{timestamp}] {http_method} /(<optional_field>{resource_name}?|) {protocol}(<message_text>){response_code} {received_bytes}(<optional_field>{referer_url}) ({user_agent}|{user_agent})?
NETWORK_HTTP
time is mapped to metadata.timestamp
ip is mapped to target.ip
principal_ip is mapped to principal.ip
principal_user_userid is mapped to principal.user.userid
metadata_timestamp is mapped to timestamp
http_method is mapped to network.http.method
resource_name is mapped to principal.resource.name
protocol is mapped to network.application_protocol = (HTTP)
response_code is mapped to network.http.response_code
received_bytes is mapped to network.sent_bytes
referer_url is mapped to network.http.referral_url
user_agent is mapped to network.http.user_agent
target.platform is set to "LINUX"
metadata.vendor_name is set to "NGINX"
metadata.product_name is set to "NGINX"
network.ip_protocol is set to "TCP"
network.direction is set to "OUTBOUND"
var/log/nginx/error.log
2022/01/29 13:51:48 [error] 593#593: *62432 open() \"/usr/share/nginx/html/nginx_status\" failed (2: No such file or directory), client: 192.0.2.1, server: localhost, request: \"GET /nginx_status HTTP/1.1\", host: \"192.0.2.1:8080\"
"{year}\/{month}\/{day}{time}[{severity}]{pid}#{thread_id}:{inner_message2}"
inner_message2 is mapped to "{security_result_description_2},client:{principal_ip},server:(<optional_field>{target_hostname}?),request:"{http_method} /(<optional_field>{resource_name}?) {protocol}/1.1",host:"({target_ip}:{target_port})?"
"bind() to ({target_ip}|[{target_ip}]):{target_port} failed ({security_description})",
"\*{cid}{security_description}",
"{security_description}"
NETWORK_HTTP
thread_id is mapped to principal.process.pid
severity is mapped to security_result.severity
(debug is mapped to UNKNOWN_SEVERITY, info is mapped to INFORMATIONAL, notice is mapped to LOW, warn is mapped to MEDIUM, error is mapped to ERROR, crit is mapped to CRITICAL, alert is mapped to HIGH)
target_file_full_path is mapped to target.file.full_path
principal_ip is mapped to principal.ip
target_hostname is mapped to target.hostname
http_method is mapped to network.http.method
resource_name is mapped to principal.resource.name
protocol is mapped to "TCP"
target_ip is mapped to target.ip
target_port is mapped to target.port
security_description + security_result_description_2 is mapped to security_result.description
pid is mapped to principal.process.parent_process.pid
network.application_protocol is set to "HTTP"
timestamp is mapped to %{year}/%{day}/%{month} %{time}
target.platform is set to "LINUX"
metadata.vendor_name is set to "NGINX"
metadata.product_name is set to "NGINX"
network.ip_protocol is set to "TCP"
network.direction is set to "OUTBOUND"
var/log/rkhunter.log
[14:10:40] Required commands check failed
[<message_text>]{security_description}
STATUS_UPDATE
time is mapped to metadata.timestamp
securtiy_description is mapped to security_result.description
principal.platform is set to "LINUX"
metadata.vendor_name is set to "RootKit Hunter"
metadata.product_name is set to "RootKit Hunter"
var/log/rkhunter.log
[14:09:52] Checking for file '/dev/.oz/.nap/rkit/terror' [ Not found ]
[<message_text>] {security_description} {file_path}[{metadata_description}]
FILE_UNCATEGORIZED
metadata_description is mapped to metadata.description
file_path is mapped to target.file.full_path
security_description is mapped to security_result.description
principal.platform is set to "LINUX"
metadata.vendor_name is set to "RootKit Hunter"
metadata.product_name is set to "RootKit Hunter"
var/log/rkhunter.log
ossec: File size reduced (inode remained): '/var/log/rkhunter.log'.
(<optional_field><message_text>:){metadata_description}:'{file_path}'
FILE_UNCATEGORIZED
time is mapped to metadata.timestamp
metadata_description is mapped to metadata.description
file_path is mapped to target.file.full_path
principal.platform is set to "LINUX"
metadata.vendor_name is set to "RootKit Hunter"
metadata.product_name is set to "RootKit Hunter"
/var/log/kern.log
Jul 7 18:48:32 zynvpnsvr kernel: [2081387.006876] IPv4: martian source 1.20.32.39 from 192.0.2.1, on dev as0t5
{timestamp}{principal_hostname}{metadata_product_event_type}: [<message_text>?] <message_text>?{target_ip}\from{principal_ip}, on dev {target_user_userid}
NETWORK_CONNECTION
timestamp is mapped to "metadata.event_timestamp"
principal_hostname is mapped to "principal.hostname"
metadata_product_event_type is mapped to "metadata.product_event_type"
target_ip is mapped to "target.ip"
principal_ip is mapped to "principal.ip"
target_user_userid is mapped to "target.user.userid"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
/var/log/kern.log
Oct 25 10:10:51 localhost kernel: [ 31.974576] audit: type=1400 audit(1635136846.152:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/lxc-start" pid=752
{timestamp}{principal_hostname}{metadata_product_event_type}: <message_text>\operation="{metadata_description}"\profile="<message_text>"\name="{file_path}"\pid={pid}
STATUS_UPDATE
timestamp is mapped to "metadata.event_timestamp"
principal_hostname is mapped to "principal.hostname"
metadata_product_event_type is mapped to "metadata.product_event_type"
metadata_description is mapped to "metadata.description"
file_path is mapped to "principal.process.file"
pid is mapped to "principal.process.pid"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
/var/log/kern.log
Apr 28 12:41:35 localhost kernel: [ 5079.912215] ctnetlink v0.93: registering with nfnetlink.
{timestamp}{principal_hostname}{metadata_product_event_type}:[<message_text>?]{metadata_description}
STATUS_UPDATE
timestamp is mapped to "metadata.event_timestamp"
principal_hostname is mapped to "principal.hostname"
metadata_product_event_type is mapped to "metadata.product_event_type"
metadata_description is mapped to "metadata.description"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
/var/log/kern.log
Apr 28 11:17:01 localhost kernel: [ 0.030139] smpboot: CPU0: Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz (family: 0x6, model: 0x55, stepping: 0x7)
{timestamp}{principal_hostname}{metadata_product_event_type}:([<message_text>])<message_text>:\CPU0:{principal_asset_hardware_cpu_model}({metadata_description})
STATUS_UPDATE
timestamp is mapped to "metadata.event_timestamp"
principal_hostname is mapped to "principal.hostname"
metadata_product_event_type is mapped to "metadata.product_event_type"
principal_asset_hardware_cpu_model is mapped to "principal.asset.hardware.cpu_model"
metadata_description is mapped to "metadata.description"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
cpu_model is mapped to principal.asset.hardware.cpu_model
/var/log/syslog.log
Jan 29 13:51:46 winevt env[29194]: [29/Jan/2022:13:51:46] REQUES GET 200 /api/systems/0000-0041 (10.0.1.1) 3179
{collected_timestamp}{hostname}{command_line}[{pid}]:[{date}<message_text>]REQUES{http_method}{response_code}(<optional_field>{resource}?)({target_ip}){received_bytes}
NETWORK_CONNECTION
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
http_method is mapped to network.http.method
response_code is mapped to network.http.response_code
resource is mapped to target.url
target_ip is mapped to target.ip
received_bytes is mapped to network.received_bytes
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
command_line is mapped to principal.process.command_line
/var/log/syslog.log
Jul 26 23:13:03 zynossec ossec-authd[1096]: 2021/07/26 23:13:03 ossec-authd: INFO: Received request for a new agent (zsecmgr0000-0719) from: 3.4.5.6
{collected_timestamp}<message_text>{command_line}[{pid}]:{date} {time} {command_line}:{log_level}:{message}({hostname})from: {target_ip}
STATUS_UPDATE
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
log_level is mapped to security_result.severity
message is mapped to metadata.description
command_line is mapped to principal.process.command_line
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
target_ip is mapped to target.ip
/var/log/syslog.log
Jul 26 23:13:03 zynossec ossec-authd[1096]: 2021/07/26 23:13:03 ossec-authd: INFO: New connection from 3.4.5.6
{collected_time}{hostname}{command_line}[{pid}]:{date} {time} {command_line}:{log_level}:{description}from {target_ip}
STATUS_UPDATE
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
log_level is mapped to security_result.severity
description is mapped to security_result.description
command_line is mapped to principal.process.command_line
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
/var/log/syslog.log
Jan 29 13:51:46 zynossec ossec-authd[1096]: 2021/07/26 23:13:03 ossec-authd: ERROR: Invalid agent name zsecmgr0000-0719 (duplicated)
{collected_timestamp}<message_text>{command_line}[{pid}]:{date}<message_text>:{log_level}:{description}{hostname}({reason})
STATUS_UPDATE
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
log_level is mapped to security_result.severity
description + reason is mapped to security_result.description
command_line is mapped to principal.process.command_line
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
/var/log/syslog.log
May 2 06:25:01 localhost apachectl[64942]: AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using ::1. Set the 'ServerName' directive globally to suppress this message
{collected_timestamp}{hostname}{command_line}(<optional_field>|[{pid}]):{message}
STATUS_UPDATE
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
message is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
command_line is mapped to principal.process.command_line
/var/log/syslog.log
May 2 00:00:45 localhost fstrim[64727]: /: 6.7 GiB (7205015552 bytes) trimmed
{collected_timestamp}{hostname}{command_line}(<optional_field>|[{pid}]):{message}
STATUS_UPDATE
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
message is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
command_line is mapped to principal.process.command_line
/var/log/syslog.log
May 3 10:14:37 localhost rsyslogd: rsyslogd's userid changed to 102
{collected_timestamp}{hostname}{command_line}:{message}to{user_id}
STATUS_UPDATE
collected_time is mapped to metadata.collected_timestamp
hostname is mapped to principal.hostname
message is mapped to metadata.description
user_id is mapped to principal.user.userid
command_line is mapped to principal.process.command_line
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
/var/log/syslog.log
May 5 10:36:48 localhost systemd[1]: Starting System Logging Service...
{collected_timestamp}{hostname}{command_line}(<optional_field>|[{pid}]):{message}
STATUS_UPDATE
collected_time is mapped to metadata.event_timestamp
hostname is mapped to principal.hostname
pid is mapped to principal.process.pid
message is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
command_line is mapped to principal.process.command_line
/var/log/mail.log
Mar 16 11:40:56 Ubuntu18 sendmail[9341]: 22G6AtwH009341: from=<ossecm@Ubuntu18>, size=377, class=0, nrcpts=1, metadata_descriptionid=<202203160610.22G6AtwH009341@Ubuntu18.cdsys.local>, proto=SMTP, daemon=MTA-v4, relay=localhost [192.0.2.1]
{timestamp} {target_hostname} {application}[{pid}]: <message_text>:{KV}
STATUS_UPDATE
target_hostname is mapped to target.hostname
application is mapped to target.application
pid is mapped to target.process.pid
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/mail.log
Apr 7 13:44:01 prod postfix/pickup[22580]: AE4271627DB: uid=0 from=<root>
{timestamp} {target_hostname} {application}[{pid}]: <message_text>{KV}
EMAIL_UNCATEGORIZED
target_hostname is mapped to target.hostname
application is mapped to target.application
pid is mapped to target.process.pid
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/mail.log
Apr 7 13:44:01 prod postfix/cleanup[23434]: AE4271627DB: message-id=<20150207184401.AE4271627DB@server.hostname.01>
{timestamp} {target_hostname} {application}[{pid}]: <message_text> message-id=<{resource_name}>
STATUS_UPDATE
target_hostname is mapped to target.hostname
application is mapped to target.application
pid is mapped to target.process.pid
resource_name is mapped to target.resource.name
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/mail.log
Apr 7 13:44:01 prod postfix/qmgr[3539]: AE4271627DB: from=<root@server.hostname.01>, size=565, nrcpt=1 (queue active)
{timestamp} {target_hostname} {application}[{pid}]: <message_text>{KV}
EMAIL_UNCATEGORIZED
target_hostname is mapped to target.hostname
application is mapped to target.application
pid is mapped to target.process.pid
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/mail.log
Apr 7 13:44:01 prod postfix/smtp[23436]: connect to gmail-smtp-in.l.google.com[2607:f8b0:400d:c03::1b]:25: Network is unreachable
{timestamp} {target_hostname} {application}[{pid}]: <message_text>{KV}
STATUS_UPDATE
target_hostname is mapped to target.hostname
application is mapped to target.application
pid is mapped to target.process.pid
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/mail.log
Apr 7 13:44:02 prod postfix/local[23439]: E62521627DC: to=<root@server.hostname.01>, relay=local, delay=0.01, delays=0/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
{timestamp} {target_hostname} {application}[{pid}]: <message_text>{KV}
EMAIL_UNCATEGORIZED
target_hostname is mapped to target.hostname
application is mapped to target.application
pid is mapped to target.process.pid
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/rundeck/service.log
[2022-05-04T17:03:11,166] WARN config.NavigableMap - Accessing config key '[filterNames]' through dot notation is deprecated, and it will be removed in a future release. Use 'config.getProperty(key, targetClass)' instead.
[{timestamp}]{severity}{summary}\-{security_description}
, at {command_line}\({file_path}:<message_text>\)
STATUS_UPDATE
command_line is mapped to "target.process.command_line"
file_path is mapped to "target.process.file.full_path"
timestamp is mapped to "metadata.event_timestamp"
severity is mapped to "security_result.severity"
summary is mapped to "security_result.summary"
security_description is mapped to "security_result.description"
metadata.product_name is set to "OSSEC"
metadata.vendor_name is set to "OSSEC"
/var/log/auth.log
Apr 27 21:03:03 Ubuntu18 systemd-logind[836]: Removed session 3080.
{timestamp} {principal_hostname}{principal_application}(<optional_field>[{pid}]):{security_description}{network_session_id}?(of user{principal_user_userid})?
USER_LOGOUT
timestamp is mapped to "metadata.timestamp"
If metadata.event_type is USER_LOGOUT, then principal_hostname is mapped to "target.hostname" else it is mapped to "principal.hostname".
If metadata.event_type is USER_LOGOUT, then principal_application is mapped to "target.application" else it is mapped to "principal.application".
If metadata.event_type is USER_LOGOUT, then pid is mapped to "target.process.pid" else it is mapped to "principal.process.pid".
security_description is mapped to "security_result.description"
network_session_id is mapped to "network.session_id"
If metadata.event_type is USER_LOGOUT, principal_user_userid is mapped to "principal.user.userid" else it is mapped to "target.user.userid".
"principal.platform" is mapped to "LINUX"
if(removed_session) event_type is set to USER_LOGOUT
extensions.auth.type is set to AUTHTYPE_UNSPECIFIED
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/auth.log
Apr 28 11:33:24 Ubuntu18 systemd-logind[836]: New session 3205 of user root.
{timestamp} {principal_hostname}{principal_application}(<optional_field>[{pid}]):{security_description}{network_session_id}?(of user{principal_user_userid})?
USER_LOGIN
timestamp is mapped to "metadata.timestamp"
If metadata.event_type is USER_LOGOUT, then principal_hostname is mapped to "target.hostname" else it is mapped to "principal.hostname".
If metadata.event_type is USER_LOGOUT, then principal_application is mapped to "target.application" else it is mapped to "principal.application".
If metadata.event_type is USER_LOGOUT, then pid is mapped to "target.process.pid" else it is mapped to "principal.process.pid".
security_description is mapped to "security_result.description"
network_session_id is mapped to "network.session_id"
If metadata.event_type is USER_LOGOUT, principal_user_userid is mapped to "principal.user.userid" else it is mapped to "target.user.userid".
"principal.platform" is mapped to "LINUX"
"network.application_protocol" is mapped to "SSH"
if(new_session) event_type is set to USER_LOGIN
extensions.auth.type is set to AUTHTYPE_UNSPECIFIED
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/auth.log
Apr 28 11:35:31 Ubuntu18 sshd[23573]: Accepted password for root from 10.0.1.1 port 40503 ssh2
{timestamp} {principal_hostname}{principal_application}(<optional_field>[{pid}])<optional_field> {security_description} for (invalid user )?{principal_user_userid} from {principal_ip} port {principal_port} ssh2(:{security_result_detection_fileds_ssh_kv}SHA256:{security_result_detection_fileds_kv})?
USER_LOGIN
timestamp is mapped to "metadata.timestamp"
If metadata.event_type is USER_LOGOUT, then principal_hostname is mapped to "target.hostname" else it is mapped to "principal.hostname".
If metadata.event_type is USER_LOGOUT, then principal_application is mapped to "target.application" else it is mapped to "principal.application".
If metadata.event_type is USER_LOGOUT, then pid is mapped to "target.process.pid" else it is mapped to "principal.process.pid".
security_description is mapped to "security_result.description"
If metadata.event_type is USER_LOGOUT, principal_user_userid is mapped to "principal.user.userid" else it is mapped to "target.user.userid".
principal_ip is mapped to "principal.ip"
principal_port is mapped to "principal.port"
security_result_detection_fields_ssh_kv is mapped to "security_result.detection_fields.key/value"
security_result_detection_fields_kv is mapped to "security_result.detection_fields.key/value"
"principal.platform" is set to "LINUX"
"network.application_protocol" is set to "SSH"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/auth.log
Apr 28 11:50:20 Ubuntu18 sshd[24145]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=10.0.1.1 user=root
{timestamp} {principal_hostname}{principal_application}([{pid}])<optional_field> <message_text>: {security_description};logname=(<message_text>)?uid=({principal_user_userid})?euid=({principal_user_attribute_labels_euid_kv})?tty=(<message_text>)?ruser=({principal_ruser_userid})?rhost=({target_ip})?(user=(<optional_field>{principal_user_userid}|{principal_user_userid})?)?
USER_LOGIN
timestamp is mapped to "metadata.timestamp"
If metadata.event_type is USER_LOGOUT, then principal_hostname is mapped to "target.hostname" else it is mapped to "principal.hostname".
If metadata.event_type is USER_LOGOUT, then principal_application is mapped to "target.application" else it is mapped to "principal.application".
If metadata.event_type is USER_LOGOUT, then pid is mapped to "target.process.pid" else it is mapped to "principal.process.pid".
security_description is mapped to "security_result.description"
principal_user_uuserid is mapped to "principal.user.attribute.labels"
principal_user_attribute_labels_euid_kv is mapped to "principal.user.attribute.labels.key/value"
principal_ruser_userid is mapped to "principal.user.attribute.labels.key/value"
target_ip is mapped to "target.ip"
If metadata.event_type is is USER_LOGOUT, then principal_user_userid is mapped to "principal.user.userid" else it is mapped to "target.user.userid"
"principal.platform" is set to "LINUX"
"network.application_protocol" is set to "SSH"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/auth.log
Feb 24 00:13:02 precise32 sudo: tsg : user NOT in sudoers ; TTY=pts/1 ; PWD=/home/vagrant ; USER=root ; COMMAND=/bin/ls
{timestamp} {principal_hostname}{principal_application}(<optional_field>[{pid}])<optional_field> {principal_user_userid} :( {security_description} ;)? TTY=<message_text> ; PWD={principal_process_command_line_1} ; USER={principal_user_attribute_labels_uid_kv} ; COMMAND={principal_process_command_line_2}
STATUS_UPDATE
timestamp is mapped to metadata.timestamp
principal_hostname is mapped to principal.hostname
principal_application is mapped to principal.application
pid is mapped to principal.process.pid
principal_user_userid is mapped to target.user.userid
security_description is mapped to "security_result.description"
principal_process_command_line_1 is mapped to "principal.process.command_line"
principal_process_command_line_2 is mapped to "principal.process.command_line"
principal_user_attribute_labels_uid_kv is mapped to "principal.user.attribute.labels.key/value"
"principal.platform" is set to "LINUX"
/var/log/auth.log
Apr 26 07:39:01 Ubuntu18 CRON[2126]: pam_unix(cron:session): session opened for user root by (uid=0)
{timestamp} {principal_hostname}{principal_application}(<optional_field>[{pid}])<optional_field> {security_description} for (invalid user|user)?{principal_user_userid}(by (uid={principal_user_attribute_labels_uid_kv}))?$
USER_LOGIN
timestamp is mapped to metadata.timestamp
If metadata.event_type is USER_LOGOUT, then principal_hostname is mapped to "target.hostname" else it is mapped to "principal.hostname".
If metadata.event_type is USER_LOGOUT, then principal_application is mapped to "target.application" else it is mapped to "principal.application".
If metadata.event_type is USER_LOGOUT, then pid is mapped to "target.process.pid" else it is mapped to "principal.process.pid".
security_description is mapped to "security_result.description"
If metadata.event_type is USER_LOGOUT, principal_user_userid is mapped to "principal.user.userid" else it is mapped to "target.user.userid".
principal_user_attribute_labels_uid_kv is mapped to "principal.user.attribute.labels.key/value"
"principal.platform" is set to "LINUX"
"network.application_protocol" is set to "SSH"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/auth.log
Apr 26 07:39:01 Ubuntu18 CRON[2126]: pam_unix(cron:session): session closed for user root
{timestamp} {principal_hostname}{principal_application}(<optional_field>[{pid}])<optional_field> {security_description} for (invalid user|user)?{principal_user_userid}(by (uid={principal_user_attribute_labels_uid_kv}))?$
USER_LOGOUT
timestamp is mapped to metadata.timestamp
If metadata.event_type is USER_LOGOUT, then principal_hostname is mapped to "target.hostname" else it is mapped to "principal.hostname".
If metadata.event_type is USER_LOGOUT, then principal_application is mapped to "target.application" else it is mapped to "principal.application".
If metadata.event_type is USER_LOGOUT, then pid is mapped to "target.process.pid" else it is mapped to "principal.process.pid".
security_description is mapped to "security_result.description"
If metadata.event_type is USER_LOGOUT, principal_user_userid is mapped to "principal.user.userid" else it is mapped to "target.user.userid".
principal_user_attribute_labels_uid_kv is mapped to principal.user.attribute.labels.key/value
"principal.platform" is set to "LINUX"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
/var/log/auth.log
May 24 12:56:31 ip-10-50-2-176 sshd[119931]: Timeout, client not responding.
{timestamp} {principal_hostname}{principal_application}([{pid}])<optional_field> {security_result_description}
STATUS_UPDATE
timestamp is mapped to metadata.timestamp
principal_hostname is mapped to principal.hostname
principal_application is mapped to principal.application
pid is mapped to principal.process.pid
security_result_description is mapped to security_result_description
"principal.platform" is set to "LINUX"
metadata.vendor_name is set to OSSEC
metadata.product_name is set to OSSEC
var/log/samba/log.winbindd
[2022/05/05 13:51:22.212484, 0] ../source3/winbindd/winbindd_cache.c:3170(initialize_winbindd_cache)initialize_winbindd_cache: clearing cache and re-creating with version number 2
{timestamp},{severity}(<optional_field>,pid={pid},effective({principal_user_attribute_labels_kv},{principal_group_attribute_labels_kv}),real({principal_user_userid},{principal_group_product_object_id}))?]<message_text>:{security_description}
STATUS_UPDATE
timestamp is mapped to "metadata.timestamp"
pid is mapped to "principal.process.pid"
principal_user_attribute_labels_kv is mapped to "principal.user.attribute.labels"
principal_group_attribute_labels_kv is mapped to "principal.group.attribute.labels"
principal_user_userid is mapped to "principal.user.userid"
principal_group_product_object_id is mapped to "principal.group.product_object_id"
security_description is mapped to "security_result.description"
metadata_description is mapped to "metadata.description"
metadata.product_name is set to "OSSEC"
"metadata.vendor_name" is set to "OSSEC"
var/log/samba/log.winbindd
messaging_dgm_init: bind failed: No space left on device
{user_id}: {desc}
STATUS_UPDATE
metadata.product_name is set to "OSSEC"
metadata.vendor_name" is set to "OSSEC"
user_id is mapped to principal.user.userid
desc is mapped to metadata.description
var/log/openvpnas.log
2022-04-29T10:51:22+0530 [stdout#info] [OVPN 4] OUT: '2022-04-29 05:21:22 mohit_AUTOLOGIN/10.50.0.1:16245 MULTI: Learn: 172.27.232.2 -> mohit_AUTOLOGIN/10.50.0.1:16245'
{timestamp}[stdout#{log_level}][OVPN <message_text>]OUT:(<optional_field>'|")<message_text>-<message_text>{user}\/{ip}:{port}MULTI:Learn:{local_ip}->{target_hostname}?{target_ip}:{port}(<optional_field>'|")
NETWORK_HTTP
timestamp is mapped to metadata.timestamp
log_level is mapped to security_result.severity
local_ip is mapped to principal.ip
target_ip is mapped to target.ip
target_hostname is mapped to principal.hostname
port is mapped to target.port
user is mapped to principal.user.user_display_name
metadata.vendor_name is set to "OpenVPN"
metadata.product_name is set to "OpenVPN Access Server"
principal.platform is set to "LINUX"
var/log/openvpnas.log
2022-04-28T16:14:13+0530 [stdout#info] [OVPN 6] OUT: '2022-04-28 16:14:13 library versions: OpenSSL 1.1.1 11 Sep 2018, LZO 2.08'
{timestamp}[stdout#{log_level}][OVPN <message_text>]OUT:(<optional_field>'|")<message_text>{msg}(<optional_field>'|")
STATUS_UPDATE
timestamp is mapped to metadata.timestamp
log_level is mapped to security_result.severity
msg is mapped to security_result.description
metadata.vendor_name is set to "OpenVPN"
metadata.product_name is set to "OpenVPN Access Server"
principal.platform is set to "LINUX"
var/log/openvpnas.log
2022-04-29T10:51:22+0530 [stdout#info] [OVPN 4] OUT: '2022-04-29 05:21:22 10.50.0.1:16245 [mohit_AUTOLOGIN] Peer Connection Initiated with [AF_INET]10.50.0.1:16245 (via [AF_INET]10.50.2.175%ens160)'
{timestamp}[stdout#{log_level}][OVPN <message_text>]OUT:(<optional_field>'|")<message_text>{message}(<optional_field>'|")
message is mapped to <message_text>with[<message_text>]<message_text>:{port}<message_text>
STATUS_UPDATE
timestamp is mapped to metadata.timestamp
log_level is mapped to security_result.severity
message is mapped to security_result.description
metadata.vendor_name is set to "OpenVPN"
metadata.product_name is set to "OpenVPN Access Server"
principal.platform is set to "LINUX"
var/log/openvpnas.log
2022-04-29T10:51:22+0530 [stdout#info] [OVPN 4] OUT: "2022-04-29 05:21:22 mohit_AUTOLOGIN/10.50.0.1:16245 SENT CONTROL [mohit_AUTOLOGIN]: 'PUSH_REPLY,explicit-exit-notify,topology subnet,route-delay 5 30,dhcp-pre-release,dhcp-renew,dhcp-release,route-metric 101,ping 12,ping-restart 50,redirect-gateway def1,redirect-gateway bypass-dhcp,redirect-gateway autolocal,route-gateway 172.27.232.1,dhcp-option DNS 10.0.1.99,dhcp-option DNS 10.0.1.94,register-dns,block-ipv6,ifconfig 172.27.232.2 255.255.254.0,peer-id 0,auth-tokenSESS_ID,cipher AES-256-GCM,key-derivation tls-ekm' (status=1)"
{timestamp}[stdout#{log_level}][OVPN <message_text>]OUT:(<optional_field>'|")<message_text>{user}\/{ip}:{message}(<optional_field>'|")
STATUS_UPDATE
timestamp is mapped to metadata.timestamp
log_level is mapped to security_result.severity
message is mapped to security_result.description
user is mapped to principal.user.user_display_name
ip is mapped to principal.ip
metadata.vendor_name is set to "OpenVPN"
metadata.product_name is set to "OpenVPN Access Server"
principal.platform is set to "LINUX"
var/log/openvpnas.log
2022-04-29T10:51:22+0530 [stdout#info] AUTH SUCCESS {'status': 0, 'user': 'mohit', 'reason': 'AuthAutoLogin: autologin certificate auth succeeded', 'proplist': {'prop_autogenerate': 'true', 'prop_autologin': 'true', 'pvt_password_digest': '[redacted]', 'type': 'user_connect'}, 'common_name': 'mohit_AUTOLOGIN', 'serial': '3', 'serial_list': []} cli='win'/'3.git::d3f8b18b'/'OCWindows_3.3.6-2752'
{timestamp}[stdout#{log_level}]{summary}{'<message_text>':({status})?'<message_text>':({user})?'<message_text>':({reason})?<message_text>}, 'common_name':'{user_name}'<message_text>}cli='{cli}'
STATUS_UPDATE
timestamp is mapped to metadata.timestamp
log_level is mapped to security_result.severity
message is mapped to security_result.description
summary is mapped to security_result.summary
user_name is mapped to principal.user.user_display_name
cli is mapped to principal.process.command_line
status is mapped to principal.user.user_authentication_status
metadata.vendor_name is set to "OpenVPN"
metadata.product_name is set to "OpenVPN Access Server"
principal.platform is set to "LINUX"
/var/log/audit.log
type=SYSTEM_RUNLEVEL metadata_description=audit(1651576133.423:202): pid=1571 uid=0 auid=4294967295 ses=4294967295 metadata_description='old-level=N new-level=5 comm="systemd-update-utmp" exe="/lib/systemd/systemd-update-utmp" hostname=? addr=? terminal=? res=success'
type={audit_log_type}
=audit((<optional_field>{metadata_ingested_timestamp}|{metadata_ingested_timestamp})<message_text>:<message_text>):{audit_message}
EventType in current sheet Audit log EventType mapping tab
audit_log_type is mapped to metadata.product_event_type
metadata_ingested_timestamp is mapped to "metadata.event_timestamp"
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.plateform is set to "LINUX"
data is mapped to key value pair-> UDM mapping in current sheet audit.log tab
var/ossec/logs/ossec.log
2022/05/12 18:15:34 ossec-syscheckd: INFO: Starting syscheck scan
{timestamp} {application}(({pid}))<optional_field>{severity}:{metadata_description}
STATUS_UPDATE
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
metadata_description is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:34:27 ossec-logcollector: INFO: Monitoring full output of command(360): last -n 5
{timestamp} {application}(({pid}))<optional_field>{severity}:(?<metadata_description>.*command.*(<message_text>)):{command_line}
PROCESS_UNCATEGORIZED
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
command_line is mapped to target.process.command_line
metadata_description is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:34:27 ossec-analysisd(1210): ERROR: Queue '/queue/alerts/ar' not accessible: 'Connection refused'.
{timestamp} {application}(({pid}))<optional_field>{severity}: Queue '{resource}'<message_text>:'{metadata_description}'
USER_RESOURCE_ACCESS
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
metadata_description is mapped to metadata.description
resource is mapped to target.resource.name
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:34:27 ossec-logcollector(1950): INFO: Analyzing file: '/var/log/rundeck/rundeck.log'.
{timestamp} {application}(({pid}))<optional_field>{severity}:(?<metadata_description><message_tewxt>file<message_text>):'{file_path}'
FILE_UNCATEGORIZED
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
file_path is mapped to target.file.full_path
metadata_description is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:34:25 ossec-syscheckd: INFO: ignoring: 'C:\WINDOWS/PCHEALTH/HELPCTR/DataColl'
{timestamp} {application}(({pid}))<optional_field>{severity}:<message_text>ignoring<message_text>:'{file_path}'
SCAN_PROCESS
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
file_path is mapped to target.file.full_path
metadata.vendor_name is set to OSSEC
metadata.product_name is set to OSSEC
var/ossec/logs/ossec.log
2022/05/11 19:34:21 ossec-remoted(1410): INFO: Reading authentication keys file.
{timestamp} {application}(({pid}))<optional_field>{severity}:{metadata_description}
STATUS_UPDATE
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
metadata_description is mapped to metadata.description
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:34:21 ossec-remoted(1103): ERROR: Could not open file '/queue/rids/004' due to [(13)-(Permission denied)].
{timestamp} {application}(({pid}))<optional_field>{severity}:(?<metadata_description><message_text>file<message_text>) '{file_path}'<message_text>[({error_code})-({error_metadata_description})]
FILE_UNCATEGORIZED
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
file_path is mapped to target.file.full_path
metadata_description is mapped to metadata.description
error_code is mapped to security_result.summary
error_metadata_description is mapped to security_result.summary
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/03/23 13:00:51 ossec-remoted(1206): ERROR: Unable to Bind port '1514'
{timestamp} {application}(({pid}))<optional_field>{severity}:{metadata_description}port'{port}'
STATUS_UPDATE
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
metadata_description is mapped to metadata.description
port is mapped to target.port
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:32:05 ossec-analysisd: INFO: Reading rules file: 'ms-se_rules.xml'
{timestamp} {application}(({pid}))<optional_field>{severity}:{metadata_description}:'{file_path}'
FILE_READ
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
metadata_description is mapped to metadata.description
file_path is mapped to target.file.full_path
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
var/ossec/logs/ossec.log
2022/05/11 19:32:06 ossec-analysisd: INFO: Ignoring file: '/etc/mnttab'
{timestamp} {application}(({pid}))<optional_field>{severity}:<message_text>(ignoring|Ignoring file)<message_text>:'{file_path}'
FILE_UNCATEGORIZED
application is mapped to target.application
pid is mapped to target.process.pid
severity is mapped to security_result.severity
file_path is mapped to target.file.full_path
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
ntpd process
udp6 0 0 fe80::c59:3eff:fe14:123 :::* 999 20209 570/ntpd
{protocol}{rec}{send}{ip}:{port}<message_text>{pid}/{process_name}
STATUS_UPDATE
protocol is mapped to network.ip_protocol
pid is mapped to principal.process.pid
metadata.description is set to Program name: %{process_name}
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
syscheck
File '/usr/bin/fwts' modified
File '{file_path}' {description}
FILE_MODIFICATION
description is mapped to metadata.description
file_path is mapped to target.file.full_path
metadata.vendor_name is set to "OSSEC"
metadata.product_name is set to "OSSEC"
principal.platform is set to "LINUX"
Audit
Audit log fields to UDM fields
The following table lists the log fields of the audit log type
and their corresponding UDM fields.
Log field
UDM field
acct
target.user.user_display_name
addr
principal.ip
arch
about.labels.key/value
auid
target.user.userid
cgroup
principal.process.file.full_path
cmd
target.process.command_line
comm
target.application
cwd
target.file.full_path
data
about.labels.key/value
devmajor
about.labels.key/value
devminor
about.labels.key/value
egid
target.group.product_object_id
euid
target.user.userid
exe
target.process.file.full_path
exit
target.labels.key/value
family
network.ip_protocol is set to "IP6IN4" if "ip_protocol" == 2 else it is set to
     "UNKNOWN_IP_PROTOCOL"
filetype
target.file.mime_type
fsgid
target.group.product_object_id
fsuid
target.user.userid
gid
target.group.product_object_id
hostname
target.hostname
icmptype
network.ip_protocol is set to "ICMP"
id
If [audit_log_type] == "ADD_USER", target.user.userid is set to "%{id}"
If [audit_log_type] == "ADD_GROUP", target.group.product_object_id is set to "%{id}"
else target.user.attribute.labels.key/value is set to id
inode
target.resource.product_object_id
key
security_result.detection_fields.key/value
list
security_result.about.labels.key/value
mode
target.resource.attribute.permissions.name
target.resource.attribute.permissions.type
name
target.file.full_path
new-disk
target.resource.name
new-mem
target.resource.attribute.labels.key/value
new-vcpu
target.resource.attribute.labels.key/value
new-net
pincipal.mac
new_gid
target.group.product_object_id
oauid
target.user.userid
ocomm
target.process.command_line
opid
target.process.pid
oses
network.session_id
ouid
target.user.userid
obj_gid
target.group.product_object_id
obj_role
target.user.attribute.role.name
obj_uid
target.user.userid
obj_user
target.user.user_display_name
ogid
target.group.product_object_id
ouid
target.user.userid
path
target.file.full_path
perm
target.asset.attribute.permissions.name
pid
target.process.pid
ppid
target.parent_process.pid
proto
If [ip_protocol] == 2, network.ip_protocol is set to "IP6IN4"
else network.ip_protocol is set to "UNKNOWN_IP_PROTOCOL"
res
security_result.summary
result
security_result.summary
saddr
security_result.detection_fields.key/value
sauid
target.user.attribute.labels.key/value
ses
network.session_id
sgid
target.group.product_object_id
sig
security_result.detection_fields.key/value
subj_user
target.user.user_display_name
success
If success=='yes', securtiy_result.summary is set to 'system call was successful'
else securtiy_result.summary is set to 'systemcall was failed'
suid
target.user.userid
syscall
about.labels.key/value
terminal
target.labels.key/value
tty
target.labels.key/value
uid
If [audit_log_type] in [SYSCALL, SERVICE_START, ADD_GROUP, ADD_USER, MAC_IPSEC_EVENT, MAC_UNLBL_STCADD, OBJ_PID, CONFIG_CHANGE, SECCOMP, USER_CHAUTHTOK, USYS_CONFIG, DEL_GROUP, DEL_USER, USER_CMD, USER_MAC_POLICY_LOAD] uid is set to principal.user.userid
else uid is set to target.user.userid
vm
target.resource.name
Audit log types to UDM event type
The following table lists the audit log types and their corresponding UDM event types.
Audit log type
UDM event type
Description
ADD_GROUP
GROUP_CREATION
Triggered when a user-space group is added.
ADD_USER
USER_CREATION
Triggered when a user-space user account is added.
ANOM_ABEND
GENERIC_EVENT / PROCESS_TERMINATION
Triggered when a processes ends abnormally (with a signal that could cause a core dump, if enabled).
AVC
GENERIC_EVENT
Triggered to record an SELinux permission check.
CONFIG_CHANGE
USER_RESOURCE_UPDATE_CONTENT
Triggered when the Audit system configuration is modified.
CRED_ACQ
USER_LOGIN
Triggered when a user acquires user-space credentials.
CRED_DISP
USER_LOGOUT
Triggered when a user disposes of user-space credentials.
CRED_REFR
USER_LOGIN
Triggered when a user refreshes their user-space credentials.
CRYPTO_KEY_USER
USER_RESOURCE_ACCESS
Triggered to record the cryptographic key identifier used for cryptographic purposes.
CRYPTO_SESSION
PROCESS_TERMINATION
Triggered to record parameters set during a TLS session establishment.
CWD
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Triggered to record the current working directory.
DAEMON_ABORT
PROCESS_TERMINATION
Triggered when a daemon is stopped due to an error.
DAEMON_END
PROCESS_TERMINATION
Triggered when a daemon is successfully stopped.
DAEMON_RESUME
PROCESS_UNCATEGORIZED
Triggered when the auditd daemon resumes logging.
DAEMON_ROTATE
PROCESS_UNCATEGORIZED
Triggered when the auditd daemon rotates the Audit log files.
DAEMON_START
PROCESS_LAUNCH
Triggered when the auditd daemon is started.
DEL_GROUP
GROUP_DELETION
Triggered when a user-space group is deleted
Pending
USER_DELETION
Triggered when a user-space user is deleted
EXECVE
PROCESS_LAUNCH
Triggered to record arguments of the execve(2) system call.
MAC_CONFIG_CHANGE
GENERIC_EVENT
Triggered when an SELinux Boolean value is changed.
MAC_IPSEC_EVENT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Triggered to record information about an IPSec event, when one is detected, or when the IPSec configuration changes.
MAC_POLICY_LOAD
GENERIC_EVENT
Triggered when a SELinux policy file is loaded.
MAC_STATUS
GENERIC_EVENT
Triggered when the SELinux mode (enforcing, permissive, off) is changed.
MAC_UNLBL_STCADD
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Triggered when a static label is added when using the packet labeling capabilities of the kernel provided by NetLabel.
NETFILTER_CFG
GENERIC_EVENT
Triggered when Netfilter chain modifications are detected.
OBJ_PID
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Triggered to record information about a process to which a signal is sent.
PATH
FILE_OPEN/GENERIC_EVENT
Triggered to record file name path information.
SELINUX_ERR
GENERIC_EVENT
Triggered when an internal SELinux error is detected.
SERVICE_START
SERVICE_START
Triggered when a service is started.
SERVICE_STOP
SERVICE_STOP
Triggered when a service is stopped.
SYSCALL
GENERIC_EVENT
Triggered to record a system call to the kernel.
SYSTEM_BOOT
STATUS_STARTUP
Triggered when the system is booted up.
SYSTEM_RUNLEVEL
STATUS_UPDATE
Triggered when the system's run level is changed.
SYSTEM_SHUTDOWN
STATUS_SHUTDOWN
Triggered when the system is shut down.
USER_ACCT
SETTING_MODIFICATION
Triggered when a user-space user account is modified.
USER_AUTH
USER_LOGIN
Triggered when a user-space authentication attempt is detected.
USER_AVC
USER_UNCATEGORIZED
Triggered when a user-space AVC message is generated.
USER_CHAUTHTOK
USER_RESOURCE_UPDATE_CONTENT
Triggered when a user account attribute is modified.
USER_CMD
USER_COMMUNICATION
Triggered when a user-space shell command is executed.
USER_END
USER_LOGOUT
Triggered when a user-space session is terminated.
USER_ERR
USER_UNCATEGORIZED
Triggered when a user account state error is detected.
USER_LOGIN
USER_LOGIN
Triggered when a user logs in.
USER_LOGOUT
USER_LOGOUT
Triggered when a user logs out.
USER_MAC_POLICY_LOAD
RESOURCE_READ
Triggered when a user-space daemon loads an SELinux policy.
USER_MGMT
USER_UNCATEGORIZED
Triggered to record user-space management data.
USER_ROLE_CHANGE
USER_CHANGE_PERMISSIONS
Triggered when a user's SELinux role is changed.
USER_START
USER_LOGIN
Triggered when a user-space session is started.
USYS_CONFIG
USER_RESOURCE_UPDATE_CONTENT
Triggered when a user-space system configuration change is detected.
VIRT_CONTROL
STATUS_UPDATE
Triggered when a virtual machine is started, paused, or stopped.
VIRT_MACHINE_ID
USER_RESOURCE_ACCESS
Triggered to record the binding of a label to a virtual machine.
VIRT_RESOURCE
USER_RESOURCE_ACCESS
Triggered to record resource assignment of a virtual machine.
Mail
Mail log fields to UDM fields
The following table lists the log fields of the mail log type
and their corresponding UDM fields.
Log field
UDM field
Class
about.labels.key/value
Ctladdr
principal.user.user_display_name
From
network.email.from
Msgid
network.email.mail_id
Proto
network.application_protocol
Relay
intermediary.hostname
intermediary.ip
Size
network.received_bytes
Stat
security_result.summary
to
network.email.to
Mail log types to UDM event type
The following table lists the mail log types and their corresponding UDM event types.
Mail log type
UDM event type
sendmail
GENERIC_EVENT
pickup
EMAIL_UNCATEGORIZED
cleanup
GENERIC_EVENT
qmgr
EMAIL_UNCATEGORIZED
smtp
GENERIC_EVENT
local
EMAIL_UNCATEGORIZED
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
