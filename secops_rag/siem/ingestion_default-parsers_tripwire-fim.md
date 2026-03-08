# Collect Tripwire logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tripwire-fim/  
**Scraped:** 2026-03-05T09:29:39.084907Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tripwire logs
Supported in:
Google secops
SIEM
This document describes how you can collect the Tripwire logs by
using a Google Security Operations forwarder.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser with the
TRIPWIRE_FIM
ingestion label.
Configure Tripwire Enterprise
Sign in to the Tripwire Enterprise web console using administrator credentials.
To edit the
Log management
settings, click the
Settings
tab.
Select
Tripwire
>
System
>
Log management
.
In the
Log management preferences
window, do the following:
Select the
Forward TE log messages to syslog
checkbox.
In the
TCP host
field, enter the Google Security Operations forwarder IP address or hostname.
In the
TCP port
field, enter the port on which the log messages are sent through TCP.
To test the configuration, click
Test connection
.
To save the changes, click
Apply
.
Configure the Google Security Operations forwarder to ingest Tripwire logs
Go to
SIEM Settings
>
Forwarders
.
Click
Add new forwarder
.
In the
Forwarder Name
field, enter a unique name for the forwarder.
Click
Submit
. The forwarder is added and the
Add collector configuration
window appears.
In the
Collector name
field, type a name.
Select
Tripwire
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
: specify the connection protocol (TCP) that the collector uses to listen to syslog data.
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
Overview: This parser extracts fields from Tripwire File Integrity Manager (FIM) syslog messages, normalizing them into the UDM format. It handles various log categories, including system events, security events, changes, and audits, mapping them to corresponding UDM event types and enriching the data with details like user information, affected resources, and security outcomes.
UDM Mapping Table
Log Field
UDM Mapping
Logic
AffectedHost
principal.hostname
Directly mapped from
AffectedHost
field in CEF logs.
AffectedIP
principal.ip
Directly mapped from
AffectedIP
field in CEF logs.
AppType
target.file.full_path
Directly mapped from
AppType
field when
desc
contains "HKEY" and
AppType
is present.
ChangeType
target.resource.attribute.labels.key: Change Type
target.resource.attribute.labels.value: %{ChangeType}
Directly mapped from
ChangeType
field in CEF logs as a label.
ChangeType
sec_result.summary
Directly mapped from
change_type
field when present in the logs.
cs1
target.resource.attribute.labels.key: cs1Label
target.resource.attribute.labels.value: cs1
Directly mapped from
cs1
and
cs1Label
fields in CEF logs as a label.
cs2
target.resource.attribute.labels.key: cs2Label
target.resource.attribute.labels.value: cs2
Directly mapped from
cs2
and
cs2Label
fields in CEF logs as a label.
cs3
target.resource.attribute.labels.key: cs3Label
target.resource.attribute.labels.value: cs3
Directly mapped from
cs3
and
cs3Label
fields in CEF logs as a label.
cs4
target.resource.attribute.labels.key: cs4Label
target.resource.attribute.labels.value: cs4
Directly mapped from
cs4
and
cs4Label
fields in CEF logs as a label.
cs5
target.resource.attribute.labels.key: cs5Label
target.resource.attribute.labels.value: cs5
Directly mapped from
cs5
and
cs5Label
fields in CEF logs as a label.
cs6
target.resource.attribute.labels.key: cs6Label
target.resource.attribute.labels.value: cs6
Directly mapped from
cs6
and
cs6Label
fields in CEF logs as a label.
datetime
metadata.event_timestamp
Parsed and converted to timestamp from various formats like "MMM d HH:mm:ss", "yyyy-MM-dd HH:mm:ss".
device_event_class_id
principal.resource.product_object_id
Directly mapped from
device_event_class_id
field in CEF logs.
device_product
metadata.product_name
Directly mapped from
device_product
field in CEF logs.
device_vendor
metadata.vendor_name
Directly mapped from
device_vendor
field in CEF logs.
device_version
metadata.product_version
Directly mapped from
device_version
field in CEF logs.
dhost
target.hostname
Directly mapped from
dhost
field in CEF logs.
duser
target.user.userid
Directly mapped from
duser
field in CEF logs.
dvc
principal.ip
Directly mapped from
dvc
field in CEF logs.
elementOID
target.resource.attribute.labels.key: elementOIDLabel
target.resource.attribute.labels.value: elementOID
Directly mapped from
elementOID
and
elementOIDLabel
fields in CEF logs as a label.
event_name
metadata.product_event_type
Directly mapped from
event_name
field in CEF logs.
FileName
principal.process.file.full_path
Directly mapped from
FileName
field in CEF logs.
fname
target.file.full_path
Directly mapped from
fname
field in CEF logs.
HostName
principal.hostname
Directly mapped from
HostName
field when
desc
contains "TE:".
licurl
about.url
Directly mapped from
licurl
field in CEF logs.
log_level
security_result.severity
Mapped from
log_level
field. "Information" becomes "INFORMATIONAL", "Warning" becomes "MEDIUM", "Error" becomes "ERROR", "Critical" becomes "CRITICAL".
LogUser
principal.user.userid OR target.user.userid
Mapped to
principal.user.userid
if
event_type
is not empty and not "USER_LOGIN" and
principal_user
is empty. Otherwise, mapped to
target.user.userid
. Also extracted from
desc
field when it starts with "Msg="User".
MD5
target.file.md5
Directly mapped from
MD5
field in CEF logs when it's not empty or "Not available".
Msg
security_result.description
Directly mapped from
Msg
field when
desc
contains "TE:". Extracted from
desc
field in various scenarios based on
category
and other fields.
NodeIp
target.ip
Directly mapped from
NodeIp
field when
desc
contains "TE:".
NodeName
target.hostname
Directly mapped from
NodeName
field when
desc
contains "TE:".
OS-Type
principal.platform
Mapped from
OS-Type
field. "WINDOWS" (case-insensitive) becomes "WINDOWS", "Solaris" (case-insensitive) becomes "LINUX".
principal_user
principal.user.userid OR target.user.userid
Extracted from
message
field when it contains "CN=".  Processed to remove "CN=", parentheses, and trailing spaces. Mapped to
principal.user.userid
if
event_type
is not "USER_UNCATEGORIZED". Otherwise, mapped to
target.user.userid
. Also extracted from
desc
field in "Audit Event" category.
principal_user
principal.user.group_identifiers
Extracted from
principal_user
when
ldap_details
is not empty and contains "OU=".
principal_user
principal.administrative_domain
The domain part is extracted from
principal_user
when it matches the pattern
%{GREEDYDATA:adminsitrative_domain}\\\\%{WORD:principal_user}
.
product_logid
metadata.product_log_id
Directly mapped from
product_logid
field when
desc
contains "TE:".
rt
metadata.event_timestamp
Parsed and converted to timestamp from formats "MMM dd yyyy HH:mm:ss" and "MM dd yyyy HH:mm:ss ZZZ".
SHA-1
target.file.sha256
The value after "After=" is extracted from the
SHA-1
field and mapped.
Size
target.file.size
The value after "After=" is extracted from the
Size
field, mapped, and converted to an unsigned integer.
software_update
target.resource.name
Directly mapped from
software_update
field when it's not empty.
source_hostname
principal.hostname
Directly mapped from
source_hostname
field when
desc
contains "TE:".
source_ip
principal.ip
Directly mapped from
source_ip
field when
desc
contains "TE:".
sproc
src.process.command_line
Directly mapped from
sproc
field in CEF logs.
start
target.resource.attribute.creation_time
Parsed and converted to timestamp from format "MMM d yyyy HH:mm:ss".
target_hostname
target.hostname
Directly mapped from
target_hostname
field when present.
target_ip
target.ip
Directly mapped from
target_ip
field when present.
time
metadata.event_timestamp
Parsed from
temp_data
field using the format "<%{INT}>%{INT} %{TIMESTAMP_ISO8601:time}.*".
timezone
target.resource.attribute.labels.key: timezoneLabel
target.resource.attribute.labels.value: timezone
Directly mapped from
timezone
and
timezoneLabel
fields in CEF logs as a label.  Empty
about
object created when
licurl
is empty or "Not available". Empty
auth
object created within
extensions
when
event_type
is "USER_LOGIN". Set to "STATUS_UNCATEGORIZED" as a default value if
event_type
is not set by any other logic, or if
event_type
is "NETWORK_CONNECTION" and both
target_hostname
and
target_ip
are empty. Set to "TRIPWIRE_FIM". Set to "File Integrity Monitoring" as a default value, overridden by
device_product
if present. Set to "TRIPWIRE". Set to "ALLOW" as a default value. Set to "BLOCK" in certain scenarios based on
category
and
desc
content.
Need more help?
Get answers from Community members and Google SecOps professionals.
