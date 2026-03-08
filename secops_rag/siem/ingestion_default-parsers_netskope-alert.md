# Collect Netskope alert logs v1

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert/  
**Scraped:** 2026-03-05T09:26:51.230044Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Netskope alert logs v1
Supported in:
Google secops
SIEM
Overview
This parser extracts Netskope alert logs from JSON-formatted messages, transforming them into the Google Security Operations UDM. It normalizes fields, parses timestamps, handles alerts and severities, extracts network information (IPs, ports, protocols), enriches user and file data, and maps fields to the UDM structure. The parser also handles specific Netskope activities like logins and DLP events and adds custom labels for enhanced context.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Netskope.
Enable Netskope REST API access
Sign in to the Netskope tenant using your administrator credentials.
Go to
Settings
>
Tools
>
REST API v1
.
Create a new API key specifically for Google SecOps.
Provide a descriptive name (for example,
Google SecOps Key
).
Copy and save the generated
key
and
secret
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
Netskope Alert Logs
.
Select
Third party API
as the
Source type
.
Select
Netskope
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Authentication HTTP Header:
key pair generated previously in
<key>:<secret>
format, used to authenticate against the Netskope API.
API Hostname:
The FQDN (fully qualified domain name) of your Netskope REST API endpoint (for example
myinstance.goskope.com
).
API Endpoint:
Enter
alerts
.
Content Type:
Enter
all
.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Optional: Add a feed configuration to ingest Netskope Event logs
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed (for example,
Netskope Event Logs
).
Select
Third party API
as the
Source type
.
Select
Netskope
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Authentication HTTP Header:
key pair generated previously in
<key>:<secret>
format, used to authenticate against the Netskope API.
API Hostname:
The FQDN (fully qualified domain name) of your Netskope REST API endpoint (for example
myinstance.goskope.com
).
API Endpoint:
Enter
events
.
Content Type:
Enter
page
,
application
,
audit
,
infrastructure
or
network
depending on which events you want to parse.
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
access_method
extensions.auth.auth_details
Directly mapped from the
access_method
field.
action
security_result.action
Directly mapped from the
action
field, or set to
QUARANTINE
if
action
is "alert" or "bypass".
ALLOW
if
action
is allow.
BLOCK
if
action
is block.
action
security_result.action_details
Mapped from the
action
field if it's "alert" or "bypass".
activity
security_result.description
Directly mapped from the
activity
field.
alert
is_alert
Set to
true
if
alert
is "yes",
false
otherwise.
alert_name
-
Not mapped to the IDM object.
alert_type
security_result.category_details
Directly mapped from the
alert_type
field.
app
target.application
Directly mapped from the
app
field.
app_activity
additional.fields
{key:"app_activity", value:{string_value:
}}
Directly mapped from the
app_activity
field as a key-value pair in
additional.fields
.
app_session_id
target.resource.attribute.labels
{key:"App Session Id", value:
}
Extracted from the
message
field using grok and added as a label.
appcategory
security_result.category_details
Directly mapped from the
appcategory
field if
category
is empty.
browser
network.http.user_agent
Directly mapped from the
browser
field if not "unknown".
browser_version
network.http.parsed_user_agent.browser_version
Directly mapped from the
browser_version
field.
browser_version
network.http.parsed_user_agent.family
Set to "USER_DEFINED" if
browser_version
is present.
category
security_result.category_details
Directly mapped from the
category
field.
cci
security_result.detection_fields
{key:"cci", value:
}
Directly mapped from the
cci
field as a key-value pair in
detection_fields
.
ccl
security_result.confidence
Set based on the value of
ccl
: "poor" or "low" maps to
LOW_CONFIDENCE
, "medium" to
MEDIUM_CONFIDENCE
, "high" or "excellent" to
HIGH_CONFIDENCE
.
ccl
security_result.confidence_details
Directly mapped from the
ccl
field.
client_bytes
network.sent_bytes
Directly mapped from the
client_bytes
field after converting to unsigned integer.
count
additional.fields
{key:"count", value:{string_value:
}}
Directly mapped from the
count
field as a key-value pair in
additional.fields
.
device
principal.resource.resource_subtype
Directly mapped from the
device
field.
device
principal.resource.type
Set to "DEVICE" if
device
field is present.
dlp_file
target.file.full_path
Directly mapped from the
dlp_file
field if present, otherwise from
file_path
.
dlp_profile
security_result.rule_type
Directly mapped from the
dlp_profile
field.
dlp_rule
security_result.rule_name
Directly mapped from the
dlp_rule
field.
dlp_rule_severity
security_result.severity
Directly mapped from the
dlp_rule_severity
field if
alert_type
is DLP.
dlp_rule_severity
_severity
Mapped from the
dlp_rule_severity
field if
severity
is empty.
domain
target.asset.hostname
Directly mapped from the
domain
field.
domain
target.hostname
Directly mapped from the
domain
field.
dsthost
target.asset.hostname
Directly mapped from the
dsthost
field if it's not an IP and
dstip
is empty, otherwise mapped to
target.hostname
.
dsthost
target.hostname
Directly mapped from the
dsthost
field if it's not an IP and
dstip
is not empty.
dstip
target.asset.ip
Directly mapped from the
dstip
field.
dstip
target.ip
Directly mapped from the
dstip
field.
dstport
target.port
Directly mapped from the
dstport
field after converting to integer.
dst_country
target.location.country_or_region
Directly mapped from the
dst_country
field.
dst_location
target.location.city
Directly mapped from the
dst_location
field.
dst_region
target.location.name
Directly mapped from the
dst_region
field.
file_path
target.file.full_path
Directly mapped from the
file_path
field if
dlp_file
is empty.
file_size
target.file.size
Directly mapped from the
file_size
field after converting to unsigned integer.
file_type
target.file.mime_type
Directly mapped from the
file_type
field if not "Unknown".
from_user
network.email.from
Directly mapped from the
from_user
field if it's an email address.
from_user_category
principal.resource.attribute.labels
{key:"From User Category", value:
}
Directly mapped from the
from_user_category
field as a key-value pair in
principal.resource.attribute.labels
.
hostname
principal.asset.hostname
Directly mapped from the
hostname
field if not empty, otherwise from
instance_id
.
hostname
principal.hostname
Directly mapped from the
hostname
field if not empty, otherwise from
instance_id
.
id.time
metadata.event_timestamp
Parsed and mapped to event_timestamp in metadata.
instance_id
principal.asset.hostname
Directly mapped from the
instance_id
field if
hostname
is empty.
instance_id
principal.hostname
Directly mapped from the
instance_id
field if
hostname
is empty.
intermediary
intermediary
Directly mapped from the
intermediary
field.
ip_protocol
network.ip_protocol
Mapped from the
ip_protocol
field after being parsed by the
parse_ip_protocol.include
file.
ja3
network.tls.client.ja3
Directly mapped from the
ja3
field if it matches a hexadecimal pattern.
ja3s
network.tls.server.ja3s
Directly mapped from the
ja3s
field if it matches a hexadecimal pattern.
malware_id
security_result.threat_id
Directly mapped from the
malware_id
field.
malware_name
security_result.threat_name
Directly mapped from the
malware_name
field.
malware_severity
security_result.severity
Directly mapped from the
malware_severity
field after converting to uppercase.
malware_type
security_result.detection_fields
{key:"Malware Type", value:
}
Directly mapped from the
malware_type
field as a key-value pair in
detection_fields
.
matched_username
principal.user.email_addresses
Directly mapped from the
matched_username
field if it's an email address.
md5
target.file.md5
Directly mapped from the
md5
field if it's not empty or "Not available".
metadata.event_type
metadata.event_type
Set to "GENERIC_EVENT" initially, then potentially overridden based on other fields. Set to
NETWORK_HTTP
if
srcip
or
hostname
and
dstip
or
dsthost
or
domain
are present. Set to
STATUS_UPDATE
if
srcip
or
hostname
are present but not
dstip
,
dsthost
, or
domain
. Set to
USER_UNCATEGORIZED
if
user
is present. Set to
EMAIL_UNCATEGORIZED
if
activity
is "Introspection Scan" and
shared_with
or
from_user
are present. Set to
USER_LOGIN
if
activity
is "Login Failed", "Login Successful", or "Login Attempt".
metadata.log_type
metadata.log_type
Set to "NETSKOPE_ALERT".
metadata.product_log_id
metadata.product_log_id
Directly mapped from the
_id
field.
metadata.product_name
metadata.product_name
Set to "Netskope Alert".
metadata.vendor_name
metadata.vendor_name
Set to "Netskope".
netskope_pop
observer.hostname
Directly mapped from the
netskope_pop
field.
object
additional.fields
{key:"Object", value:{string_value:
}}
Directly mapped from the
object
field as a key-value pair in
additional.fields
.
object_id
additional.fields
{key:"Object id", value:{string_value:
}}
Directly mapped from the
object_id
field as a key-value pair in
additional.fields
.
object_type
additional.fields
{key:"Object type", value:{string_value:
}}
Directly mapped from the
object_type
field as a key-value pair in
additional.fields
.
organization_unit
principal.administrative_domain
Directly mapped from the
organization_unit
field.
os
principal.platform
Mapped from the
os
field: "Windows" maps to
WINDOWS
, "MAC" to
MAC
, "LINUX" to
LINUX
.
os_version
principal.platform_version
Directly mapped from the
os_version
field.
other_categories
-
Not mapped to the IDM object.
page
network.http.referral_url
Directly mapped from the
page
field if
referer
is empty.
policy
security_result.summary
Directly mapped from the
policy
field.
principal.user.email_addresses
principal.user.email_addresses
Merged from the
user
field if it's an email address.
protocol
network.application_protocol
Directly mapped from the
protocol
field after removing everything after the first "/". Converted to uppercase.
publisher_cn
additional.fields
{key:"publisher_cn", value:{string_value:
}}
Directly mapped from the
publisher_cn
field as a key-value pair in
additional.fields
.
publisher_name
additional.fields
{key:"publisher_name", value:{string_value:
}}
Directly mapped from the
publisher_name
field as a key-value pair in
additional.fields
.
referer
network.http.referral_url
Directly mapped from the
referer
field.
security_result.alert_state
security_result.alert_state
Set to "ALERTING" if
alert
is "yes", "NOT_ALERTING" if
alert
is "no", "UNSPECIFIED" otherwise.
security_result.category_details
security_result.category_details
Merged from the
category
or
appcategory
or
alert_type
fields.
security_result.confidence
security_result.confidence
Derived from the
ccl
field.
security_result.confidence_details
security_result.confidence_details
Directly mapped from the
ccl
field.
security_result.description
security_result.description
Directly mapped from the
activity
field.
security_result.rule_name
security_result.rule_name
Directly mapped from the
dlp_rule
field.
security_result.rule_type
security_result.rule_type
Directly mapped from the
dlp_profile
field.
security_result.severity
security_result.severity
Derived from the
_severity
or
malware_severity
or
dlp_rule_severity
fields.
security_result.summary
security_result.summary
Directly mapped from the
policy
field.
security_result.threat_id
security_result.threat_id
Directly mapped from the
malware_id
field.
security_result.threat_name
security_result.threat_name
Directly mapped from the
malware_name
field.
server_bytes
network.received_bytes
Directly mapped from the
server_bytes
field after converting to unsigned integer.
severity
_severity
Directly mapped from the
severity
field.
sha256
target.file.sha256
Directly mapped from the
sha256
field.
shared_with
network.email.to
Parsed from the
shared_with
field and added to the
network.email.to
array if it's an email address.
site
additional.fields
{key:"site", value:{string_value:
}}
Directly mapped from the
site
field as a key-value pair in
additional.fields
.
src_country
principal.location.country_or_region
Directly mapped from the
src_country
field.
src_latitude
principal.location.region_latitude
Directly mapped from the
src_latitude
field.
src_location
principal.location.city
Directly mapped from the
src_location
field.
src_longitude
principal.location.region_longitude
Directly mapped from the
src_longitude
field.
src_region
principal.location.name
Directly mapped from the
src_region
field.
srcip
principal.asset.ip
Extracted from the
srcip
field using grok and merged into the
principal.asset.ip
and
principal.ip
arrays.
srcip
principal.ip
Extracted from the
srcip
field using grok and merged into the
principal.asset.ip
and
principal.ip
arrays.
srcport
principal.port
Directly mapped from the
srcport
field after converting to integer.
target.user.email_addresses
target.user.email_addresses
Merged from the
to_user
field if it's an email address.
threat_match_field
security_result.detection_fields
{key:"Threat Match Field", value:
}
Directly mapped from the
threat_match_field
field as a key-value pair in
detection_fields
.
timestamp
metadata.event_timestamp
Parsed from the
timestamp
or
id.time
fields.
to_user
target.user.email_addresses
Parsed from the
to_user
field and added to the
target.user.email_addresses
array if it's an email address.
to_user_category
target.resource.attribute.labels
{key:"To User Category", value:
}
Directly mapped from the
to_user_category
field as a key-value pair in
target.resource.attribute.labels
.
traffic_type
security_result.detection_fields
{key:"traffic_type", value:
}
Directly mapped from the
traffic_type
field as a key-value pair in
detection_fields
.
tunnel_id
additional.fields
{key:"tunnel_id", value:{string_value:
}}
Directly mapped from the
tunnel_id
field as a key-value pair in
additional.fields
.
tunnel_type
additional.fields
{key:"tunnel_type", value:{string_value:
}}
Directly mapped from the
tunnel_type
field as a key-value pair in
additional.fields
.
type
security_result.detection_fields
{key:"type", value:
}
Directly mapped from the
type
field as a key-value pair in
detection_fields
.
ur_normalized
-
Not mapped to the IDM object.
url
target.url
Directly mapped from the
url
field.
user
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
user
field.
user
principal.user.email_addresses
Directly mapped from the
user
field if it's an email address.
useragent
network.http.user_agent
Directly mapped from the
useragent
field.
useragent
network.http.parsed_user_agent
Converted to parseduseragent and mapped to
network.http.parsed_user_agent
.
user_agent
network.http.user_agent
Directly mapped from the
user_agent
field.
user_agent
network.http.parsed_user_agent
Converted to parseduseragent and mapped to
network.http.parsed_user_agent
.
Need more help?
Get answers from Community members and Google SecOps professionals.
