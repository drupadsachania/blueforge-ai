# Collect Kemp Load Balancer logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kemp-loadbalancer/  
**Scraped:** 2026-03-05T09:57:34.842920Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Kemp Load Balancer logs
Supported in:
Google secops
SIEM
This document describes how you can collect Kemp Load Balancer logs by using a
Google Security Operations forwarder.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data to structured
UDM format. The information in this document applies to the parser with the
KEMP_LOADBALANCER
ingestion label.
Configure Kemp Load Balancer
Sign in to the
Kemp Load Balancer
console.
Select
Logging options
>
Syslog options
.
In the
Syslog options
section, in any of the available fields specify the
IP address of the Google Security Operations forwarder.
It is recommended to specify the IP address in the
Info host
field.
Click
Change syslog parameters
.
Configure Google Security Operations forwarder to ingest Kemp Load Balancer logs
Select
SIEM Settings
>
Forwarders
.
Click
Add new forwarder
.
In the
Forwarder name
field, enter a unique name for the forwarder.
Click
Submit
and then click
Confirm
. The forwarder is added and the
Add collector configuration
window appears.
In the
Collector name
field, type a unique name for the collector.
Select
Kemp Load Balancer
as the
Log type
.
Select
Syslog
as the
Collector type
.
Configure the following mandatory input parameters:
Protocol
: specify the connection protocol that the collector uses to listen to syslog data.
Address
: specify the target IP address or hostname where the collector resides and listens to syslog data.
Port
: specify the target port where the collector resides and listens to syslog data.
Click
Submit
.
For more information about the Google Security Operations forwarders, see
Manage forwarder configurations through the Google Security Operations UI
.
If you encounter issues when you create forwarders, contact
Google Security Operations support
.
Field mapping reference
This parser extracts fields from Kemp Load Balancer syslog messages based on the
log_number
field, mapping them to the UDM. It handles various log formats using
grok
patterns and conditional logic, converting data types and enriching events with metadata like event type, application protocol, and security results.
UDM mapping table
Log Field
UDM Mapping
Logic
collection_time.seconds
metadata.event_timestamp.seconds
Log collection time is used as event timestamp if
timestamp
is not present.  Nanoseconds are truncated.
data
metadata.description | network.http.method | principal.ip | principal.port | target.ip | target.port | network.http.response_code | target.user.userid | target.file.full_path | target.file.size | network.ftp.command | metadata.product_event_type | target.url | security_result.summary
The raw log message.  Various fields are extracted from this field based on the log number and parsing logic.
dstip
target.ip
Destination IP address.
dstport
target.port
Destination port.
filename
target.file.full_path
Filename for FTP events.
file_size
target.file.size
File size for FTP events. Converted to unsigned integer.
ftpmethod
network.ftp.command
FTP command/method.
hostname
intermediary.hostname
Hostname from CEF formatted logs.
http_method
network.http.method
HTTP method.
http_response_code
network.http.response_code
HTTP response code. Converted to integer.
kv_data
principal.ip | principal.port | target.ip | target.port | metadata.product_event_type | target.url
Key-value pairs from CEF formatted logs.  Used to extract various fields.
log_event
metadata.product_event_type
Event type from CEF formatted logs.
log_time
metadata.event_timestamp.seconds
Log timestamp. Converted to Chronicle format and used as event timestamp. Nanoseconds are truncated.
msg/message
See
data
Contains the main log message. See
data
for UDM mapping details.
pid
target.process.pid
Process ID.
resource
target.url
Resource accessed.
srcip
principal.ip
Source IP address.
src_ip
principal.ip
Source IP address.
srcport
principal.port
Source port.
src_port
principal.port
Source port.
sshd
target.application
SSH daemon name.
summary
security_result.summary
Summary of the security result.
timestamp.seconds
events.timestamp.seconds
Log entry timestamp. Used as event timestamp if present.
user
target.user.userid
Username.
vs
target.ip | target.port
Virtual server IP and port.  IP is mapped to
target.ip
. Port is mapped to
target.port
if
dstport
is not present.
vs_port
target.port
Virtual server port. Determined by logic based on
log_number
,
dest_port
,
login_status
, and
log_event
. Possible values include
GENERIC_EVENT
,
NETWORK_HTTP
,
NETWORK_CONNECTION
,
USER_LOGIN
, and
USER_UNCATEGORIZED
. Hardcoded to "KEMP_LOADBALANCER". Hardcoded to "KEMP_LOADBALANCER". Hardcoded to "KEMP". Determined by
dest_port
. Possible values are
HTTP
(port 80) and
HTTPS
(port 443). Determined by
login_status
and
audit_msg
. Possible values are
ALLOW
and
BLOCK
. Determined by
audit_msg
. Possible value is
ERROR
. Set to "AUTHTYPE_UNSPECIFIED" for USER_LOGIN events.
Need more help?
Get answers from Community members and Google SecOps professionals.
