# Collect Thinkst Canary logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/thinkst-canary/  
**Scraped:** 2026-03-05T09:29:13.482565Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Thinkst Canary logs
Supported in:
Google secops
SIEM
This parser normalizes raw log messages from Thinkst Canary software by cleaning up line breaks and attempting to parse the message as JSON. Then, based on the presence of specific fields ("Description" for key-value format or "summary" for JSON), it determines the log format and includes the appropriate parsing logic from separate configuration files to map the data into the unified data model.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Thinkst Canary.
Configure REST API in Thinkst Canary
Sign in to Thinkst Canary management console.
Click the
Gear Icon
>
Global Settings
.
Click
API
.
Click
Enable API
.
Click
+
to add an API.
Give the API a descriptive name.
Copy the
Domain Hash
and
Auth Token
.
Set up feeds
To configure a feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed; for example,
Thinkst Canary Logs
.
Select
Third party API
as the
Source type
.
Select
Thinkst Canary
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Authentication HTTP Header:
the token previously generated in a
auth_token:<TOKEN>
format (for example,
auth_token:AAAABBBBCCCC111122223333
).
API Hostname:
the FQDN (fully qualified domain name) of your Thinks Canary REST API endpoint (for example
myinstance.canary.tools
).
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label applied to the events from this feed.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping
Log field
UDM mapping
Logic
AUDITACTION
read_only_udm.metadata.product_event_type
The value is taken from the description field if the format is json, otherwise it is determined by the eventid field
CanaryIP
read_only_udm.target.ip
CanaryName
read_only_udm.target.hostname
CanaryPort
read_only_udm.target.port
COOKIE
read_only_udm.security_result.about.resource.attribute.labels.value
created
read_only_udm.metadata.event_timestamp.seconds
created_std
read_only_udm.metadata.event_timestamp.seconds
DATA
description
read_only_udm.metadata.product_event_type
The value is taken from the description field if the format is json, otherwise it is determined by the eventid field
Description
read_only_udm.metadata.product_event_type
The value is taken from the description field if the format is json, otherwise it is determined by the eventid field
DOMAIN
read_only_udm.target.administrative_domain
dst_host
read_only_udm.target.ip
dst_port
read_only_udm.target.port
eventid
read_only_udm.metadata.product_event_type
The value is taken from the description field if the format is json, otherwise it is determined by the eventid field
events_count
read_only_udm.security_result.detection_fields.value
FILENAME
read_only_udm.target.file.full_path
FIN
read_only_udm.security_result.detection_fields.value
flock_id
read_only_udm.principal.resource.attribute.labels.value
flock_name
read_only_udm.principal.resource.attribute.labels.value
FunctionData
FunctionName
HEADERS
read_only_udm.security_result.about.resource.attribute.labels
HOST
read_only_udm.target.hostname
HOSTNAME
read_only_udm.target.hostname
id
read_only_udm.metadata.product_log_id
ID
read_only_udm.security_result.detection_fields.value
IN
read_only_udm.security_result.detection_fields.value
ip_address
KEY
LEN
read_only_udm.security_result.detection_fields.value
LOCALNAME
read_only_udm.target.hostname
LOCALVERSION
read_only_udm.target.platform_version
logtype
read_only_udm.security_result.detection_fields.value
LOGINTYPE
MAC
read_only_udm.principal.mac
matched_annotations
METHOD
read_only_udm.network.http.method
MODE
ms_macro_ip
read_only_udm.principal.ip
ms_macro_username
read_only_udm.principal.user.user_display_name
name
read_only_udm.target.hostname
node_id
read_only_udm.principal.resource.attribute.labels.value
OFFSET
OPCODE
OUT
read_only_udm.security_result.detection_fields.value
PASSWORD
PATH
read_only_udm.target.url
ports
read_only_udm.target.labels.value
PREC
read_only_udm.security_result.detection_fields.value
PreviousIP
read_only_udm.principal.ip
PROTO
read_only_udm.network.ip_protocol
PSH
read_only_udm.security_result.detection_fields.value
REALM
read_only_udm.target.administrative_domain
REMOTENAME
read_only_udm.principal.hostname
REMOTEVERSION
read_only_udm.principal.platform_version
REPO
read_only_udm.target.resource.attribute.labels.value
RESPONSE
read_only_udm.network.http.response_code
ReverseDNS
Settings
read_only_udm.target.labels
SHARENAME
SIZE
SKIN
SMBARCH
SMBREPEATEVENTMSG
SMBVER
SNAME
SourceIP
read_only_udm.principal.ip
src_host
read_only_udm.principal.ip
src_host_reverse
read_only_udm.principal.hostname
src_port
read_only_udm.principal.port
STATUS
summary
read_only_udm.metadata.product_event_type
The value is taken from the description field if the format is json, otherwise it is determined by the eventid field
SYN
read_only_udm.security_result.detection_fields.value
TCPBannerID
TERMSIZE
TERMTYPE
timestamp
read_only_udm.metadata.event_timestamp.seconds
timestamp_std
read_only_udm.metadata.event_timestamp.seconds
Timestamp
read_only_udm.metadata.event_timestamp.seconds
TKTVNO
read_only_udm.security_result.detection_fields.value
TOS
read_only_udm.security_result.detection_fields.value
TTL
read_only_udm.security_result.detection_fields.value
TYPE
USER
read_only_udm.principal.user.user_display_name
USERAGENT
read_only_udm.network.http.user_agent
USERNAME
read_only_udm.target.user.user_display_name
URG
read_only_udm.security_result.detection_fields.value
URGP
read_only_udm.security_result.detection_fields.value
WINDOW
read_only_udm.security_result.detection_fields.value
windows_desktopini_access_domain
read_only_udm.principal.group.group_display_name
windows_desktopini_access_username
read_only_udm.principal.user.user_display_name
read_only_udm.metadata.log_type
THINKST_CANARY - Hardcoded value
read_only_udm.metadata.vendor_name
Thinkst - Hardcoded value
read_only_udm.metadata.product_name
Canary - Hardcoded value
read_only_udm.security_result.severity
CRITICAL - Hardcoded value
read_only_udm.network.application_protocol
Determined by the port and product_event_type
read_only_udm.extensions.auth.mechanism
Determined by the authentication method used in the event
Need more help?
Get answers from Community members and Google SecOps professionals.
