# Collect Symantec Event Export logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-event-export/  
**Scraped:** 2026-03-05T09:28:44.864227Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Symantec Event Export logs
Supported in:
Google secops
SIEM
This document describes how you can collect Symantec Event Export logs by setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the following ingestion labels:
SYMANTEC_EVENT_EXPORT
and
SEP
.
Configure Symantec Event Export
Sign in to the SEP 15/14.2 console.
Select
Integration
.
Click
Client Application
and copy the
Customer ID
and
Domain ID
, which are used when you create a Google Security Operations feed.
Click
+ Add
and provide an application name.
Click
Add
.
Go to the
Details
page and perform the following actions:
In the
Devices Group Management
section, select
View
.
In the
Alerts & Events Rule Management
section, select
View
.
In the
Investigation Incident
section, select
View
.
Click
Save
.
Click the menu (vertical ellipses) located at the end of the application name and click
Client Secret
.
Copy the client ID and client secret, which are required when you configure the Google Security Operations feed.
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
Symantec Event Export Logs
.
Select
Google Cloud Storage V2
as the
Source Type
.
Select
Symantec Event export
as the
Log Type
.
Click
Get a Service Account
. Google Security Operations provides a unique service account that Google Security Operations uses to ingest data.
Configure access for the service account to access the Cloud Storage objects. For more information, see
Grant access to the Google Security Operations service account
.
Click
Next
.
Configure the following mandatory input parameters:
Storage bucket URI
: specify the storage bucket URI.
Source deletion option
: specify the source deletion option.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Click
Next
and then click
Submit
.
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
.
For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google Security Operations support
.
Field mapping reference
This parser extracts fields from Symantec Event Export logs in JSON or SYSLOG format, normalizing and mapping them to the UDM. It handles various log structures, using grok patterns for SYSLOG and JSON parsing for JSON formatted logs, and maps fields to UDM entities like
principal
,
target
,
network
, and
security_result
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
actor.cmd_line
principal.process.command_line
The raw log's
actor.cmd_line
is mapped directly to the UDM.
actor.file.full_path
principal.process.file.full_path
The raw log's
actor.file.path
or
file.path
is mapped directly to the UDM.
actor.file.md5
principal.process.file.md5
The raw log's
actor.file.md5
is converted to lowercase and mapped directly to the UDM.
actor.file.sha1
principal.process.file.sha1
The raw log's
actor.file.sha1
is converted to lowercase and mapped directly to the UDM.
actor.file.sha2
principal.process.file.sha256
The raw log's
actor.file.sha2
or
file.sha2
is converted to lowercase and mapped directly to the UDM.
actor.file.size
principal.process.file.size
The raw log's
actor.file.size
is converted to a string and then to an unsigned integer and mapped directly to the UDM.
actor.pid
principal.process.pid
The raw log's
actor.pid
is converted to a string and mapped directly to the UDM.
actor.user.domain
principal.administrative_domain
The raw log's
actor.user.domain
is mapped directly to the UDM.  If
connection.direction_id
is 1, it's mapped to
target.administrative_domain
.
actor.user.name
principal.user.user_display_name
The raw log's
actor.user.name
is mapped directly to the UDM. If
user_name
exists, it takes precedence.
actor.user.sid
principal.user.windows_sid
The raw log's
actor.user.sid
is mapped directly to the UDM.
connection.direction_id
network.direction
If
connection.direction_id
is 1 and
connection.dst_ip
exists,
network.direction
is set to
INBOUND
. If
connection.direction_id
is 2 and
connection.dst_ip
exists,
network.direction
is set to
OUTBOUND
.
connection.dst_ip
target.ip
The raw log's
connection.dst_ip
is mapped directly to the UDM.
connection.dst_port
target.port
The raw log's
connection.dst_port
is converted to an integer and mapped directly to the UDM.
connection.src_ip
principal.ip
The raw log's
connection.src_ip
is mapped directly to the UDM.
connection.src_port
principal.port
The raw log's
connection.src_port
is converted to an integer and mapped directly to the UDM. Handles cases where
connection.src_port
is an array.
device_domain
principal.administrative_domain
or
target.administrative_domain
The raw log's
device_domain
is mapped to
principal.administrative_domain
if
connection.direction_id
is not 1. If
connection.direction_id
is 1, it's mapped to
target.administrative_domain
.
device_group
principal.group.group_display_name
or
target.group.group_display_name
The raw log's
device_group
is mapped to
principal.group.group_display_name
if
connection.direction_id
is not 1. If
connection.direction_id
is 1, it's mapped to
target.group.group_display_name
.
device_ip
src.ip
The raw log's
device_ip
is mapped directly to the UDM.
device_name
principal.hostname
or
target.hostname
The raw log's
device_name
is mapped to
principal.hostname
if
connection.direction_id
is not 1. If
connection.direction_id
is 1, it's mapped to
target.hostname
.
device_networks
intermediary.ip
,
intermediary.mac
The raw log's
device_networks
array is processed.  IPv4 and IPv6 addresses are merged into
intermediary.ip
. MAC addresses are converted to lowercase, hyphens are replaced with colons, and then merged into
intermediary.mac
.
device_os_name
principal.platform_version
or
target.platform_version
The raw log's
device_os_name
is mapped to
principal.platform_version
if
connection.direction_id
is not 1. If
connection.direction_id
is 1, it's mapped to
target.platform_version
.
device_public_ip
principal.ip
The raw log's
device_public_ip
is mapped directly to the UDM.
device_uid
principal.resource.id
or
target.resource.id
The raw log's
device_uid
is mapped to
principal.resource.id
if
connection.direction_id
is not 1. If
connection.direction_id
is 1, it's mapped to
target.resource.id
.
feature_name
security_result.category_details
The raw log's
feature_name
is mapped directly to the UDM.
file.path
principal.process.file.full_path
The raw log's
file.path
is mapped directly to the UDM. If
actor.file.path
exists, it takes precedence.
file.sha2
principal.process.file.sha256
The raw log's
file.sha2
is converted to lowercase and mapped directly to the UDM. If
actor.file.sha2
exists, it takes precedence.
log_time
metadata.event_timestamp
The raw log's
log_time
is parsed using various date formats and used as the event timestamp.
message
security_result.summary
or
network.ip_protocol
or
metadata.description
The raw log's
message
field is processed. If it contains "UDP",
network.ip_protocol
is set to "UDP". If it contains "IP",
network.ip_protocol
is set to "IP6IN4". If it contains "ICMP",
network.ip_protocol
is set to "ICMP". Otherwise, it's mapped to
security_result.summary
. If the
description
field exists, the
message
field is mapped to
metadata.description
.
parent.cmd_line
principal.process.parent_process.command_line
The raw log's
parent.cmd_line
is mapped directly to the UDM.
parent.pid
principal.process.parent_process.pid
The raw log's
parent.pid
is converted to a string and mapped directly to the UDM.
policy.name
security_result.rule_name
The raw log's
policy.name
is mapped directly to the UDM.
policy.rule_name
security_result.description
The raw log's
policy.rule_name
is mapped directly to the UDM.
policy.rule_uid
security_result.rule_id
The raw log's
policy.rule_uid
is mapped directly to the UDM. If
policy.uid
exists, it takes precedence.
policy.uid
security_result.rule_id
The raw log's
policy.uid
is mapped directly to the UDM.
product_name
metadata.product_name
The raw log's
product_name
is mapped directly to the UDM.
product_uid
metadata.product_log_id
The raw log's
product_uid
is mapped directly to the UDM.
product_ver
metadata.product_version
The raw log's
product_ver
is mapped directly to the UDM.
severity_id
security_result.severity
If
severity_id
is 1, 2, or 3,
security_result.severity
is set to
INFORMATIONAL
. If it's 4, it's set to
ERROR
. If it's 5, it's set to
CRITICAL
.
threat.id
security_result.threat_id
The raw log's
threat.id
is converted to a string and mapped directly to the UDM.
threat.name
security_result.threat_name
The raw log's
threat.name
is mapped directly to the UDM.
type_id
metadata.event_type
,
metadata.product_event_type
Used in conjunction with other fields to determine the appropriate
metadata.event_type
and
metadata.product_event_type
.
user_email
principal.user.email_addresses
The raw log's
user_email
is merged into the UDM.
user_name
principal.user.user_display_name
The raw log's
user_name
is mapped directly to the UDM.
uuid
target.process.pid
The raw log's
uuid
is parsed to extract the process ID, which is mapped to
target.process.pid
.
N/A
metadata.vendor_name
Set to "SYMANTEC".
N/A
metadata.log_type
Set to "SYMANTEC_EVENT_EXPORT".
N/A
principal.resource.resource_type
Set to "DEVICE" when
connection.direction_id
is not 1 or is empty.
N/A
target.resource.resource_type
Set to "DEVICE" when
connection.direction_id
is 1.
Need more help?
Get answers from Community members and Google SecOps professionals.
