# Collect BloxOne Threat Defense logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone/  
**Scraped:** 2026-03-05T09:20:32.273189Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BloxOne Threat Defense logs
Supported in:
Google secops
SIEM
This document explains how to ingest BloxOne Threat Defense logs to
Google Security Operations using Bindplane. The Logstash parser extracts fields from
BLOXONE DNS
logs received in SYSLOG or JSON format. It first normalizes the
log message into a JSON object and then maps the extracted fields to the Unified
Data Model (UDM), enriching the data with geolocation and DNS details for
security analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Infoblox BloxOne
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
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the Configuration File:
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
'BLOXONE'
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
Configure Syslog in Infoblox BloxOne
Sign in to the
Infoblox Portal
.
Go to
Configure
>
Administration
>
Data Connector
.
Select
Destination Configuration
tab.
Click
Create
>
Syslog
.
Provide the following configuration details:
Name
: Provide a descriptive name (for example, Google SecOps collector).
Description
: Provide a brief description.
State
: Select
Enable
.
Tags
: Click
Add
and specify the following to associate a key with the destination:
KEY
: Enter a descriptive name for the key.
VALUE
: Enter your value for the key.
Format
: Select
CEF
.
Protocol
: Select
UDP
or
TCP
(depending on your Bindplane agent configuration).
FQDN/IP
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port (default is set to
514
for
UDP
).
Click
Save & Close
.
UDM mapping table
Log field
UDM mapping
Logic
additional_list.key
This field is used in a loop to iterate over the
additional_list
array and extract data based on the value of the
key
field. It is not directly mapped to the UDM.
additional_list.value
principal.location.region_latitude
,
principal.location.region_longitude
,
target.location.region_latitude
,
target.location.region_longitude
This field is used in conjunction with
additional_list.key
to extract specific values from the
additional_list
array. The logic for extracting and mapping the value depends on the corresponding
key
. For example:
- If
additional_list.key
is
intel:source:ip:geoIP:location
, extract latitude and longitude values using grok and map them to
principal.location.region_latitude
and
principal.location.region_longitude
, respectively.
- If
additional_list.key
is
intel:destination:ip:geoIP:location
, extract latitude and longitude values using grok and map them to
target.location.region_latitude
and
target.location.region_longitude
, respectively.
additional_string.key
Similar to
additional_list.key
, this field is used in a loop to iterate over the
additional_string
array and extract data based on the
key
value. It is not directly mapped to the UDM.
additional_string.value
additional.fields.value.string_value
,
principal.location.country_or_region
,
target.location.country_or_region
,
src.ip
,
src.port
,
src.hostname
,
network.ip_protocol
Used with
additional_string.key
to extract values from the
additional_string
array. The logic for mapping the value depends on the corresponding
key
. For example:
- If
additional_string.key
is
intel:source:ip:ip2asn:start_ip
,
intel:source:ip:ip2asn:finish_ip
,
intel:destination:ip:ip2asn:start_ip
, or
intel:destination:ip:ip2asn:finish_ip
, map the value to
additional.fields.value.string_value
with the corresponding key.
- If
additional_string.key
is
intel:source:ip:geoIP:country
, map the value to
principal.location.country_or_region
.
- If
additional_string.key
is
intel:destination:ip:geoIP:country
, map the value to
target.location.country_or_region
.
- If
additional_string.key
is
log:source:ip
, map the value to
src.ip
.
- If
additional_string.key
is
log:source:port
, map the value to
src.port
after converting it to an integer.
- If
additional_string.key
is
log:source:hostname
, map the value to
src.hostname
.
- If
additional_string.key
is
log:cdh:input:protocol
, map the value to
network.ip_protocol
after converting it to uppercase.
app_category
security_result.category_details
Directly mapped.
confidence
security_result.confidence
Mapped based on the following logic:
- If
confidence
is
LOW
, map to
LOW_CONFIDENCE
.
- If
confidence
is
MEDIUM
, map to
MEDIUM_CONFIDENCE
.
- If
confidence
is
HIGH
, map to
HIGH_CONFIDENCE
.
country
principal.location.name
Directly mapped, but only if
raw.infobloxb1region
is empty.
device
principal.ip
,
principal.asset.ip
Directly mapped, but only if
raw.dvc
is empty.
dhcp_fingerprint
security_result.detection_fields.value
Directly mapped with the key
dhcp_fingerprint
.
dns_view
security_result.detection_fields.value
Directly mapped with the key
dns_view
.
endpoint_groups
security_result.detection_fields.value
Directly mapped with the key
endpoint_groups
.
event_time
metadata.event_timestamp.seconds
Parsed as an ISO8601 timestamp and the seconds value is extracted. Used only if the
timestamp
field is empty.
feed_name
principal.resource.name
feed_name
is mapped to
principal.resource.name
.
feed_type
principal.resource.attribute.labels.value
Directly mapped with the key
feed_type
.
mac_address
principal.mac
Directly mapped after converting to lowercase.
network
principal.hostname
,
principal.asset.hostname
Directly mapped, but only if both
raw.dvchost
and
raw.dvc
are empty.
os_version
principal.platform_version
Directly mapped.
policy_action
security_result.action_details
,
security_result.action
policy_action
is directly mapped to
security_result.action_details
.
security_result.action
is derived based on the following logic:
- If
policy_action
is
Redirect
or
Log
, map to
ALLOW
.
- If
policy_action
is
BLOCK
, map to
BLOCK
.
policy_name
security_result.detection_fields.value
Directly mapped with the key
policy_name
.
qname
network.dns.questions.name
Directly mapped.
qtype
network.dns.questions.type
Mapped based on the following logic:
- If
qtype
is
A
, map to 1 (converted to unsigned integer).
- If
qtype
is
PTR
, map to 12 (converted to unsigned integer).
raw.act
security_result.action_details
Directly mapped.
raw.app
network.application_protocol
Directly mapped after converting to uppercase.
raw.deviceeventclassid
metadata.product_event_type
Concatenated with
raw.name
(separated by
-
) and mapped to
metadata.product_event_type
.
raw.devicevendor
metadata.vendor_name
Directly mapped.
raw.deviceproduct
metadata.product_name
Directly mapped.
raw.deviceversion
metadata.product_version
Directly mapped.
raw.deviceseverity
security_result.severity_details
,
security_result.severity
raw.deviceseverity
is directly mapped to
security_result.severity_details
.
security_result.severity
is derived based on the following logic:
- If
raw.deviceseverity
is in [
0
,
1
,
2
,
3
], map to
LOW
.
- If
raw.deviceseverity
is in [
4
,
5
,
6
], map to
MEDIUM
.
- If
raw.deviceseverity
is in [
7
,
8
], map to
HIGH
.
- If
raw.deviceseverity
is in [
9
,
10
], map to
CRITICAL
.
raw.dvc
principal.ip
,
principal.asset.ip
Directly mapped.
raw.dvchost
principal.hostname
,
principal.asset.hostname
Directly mapped, but only if it's not equal to
raw.dvc
.
raw.infobloxb1connectiontype
additional.fields.value.string_value
Directly mapped with the key
infobloxb1connectiontype
.
raw.infobloxb1ophname
observer.hostname
,
observer.asset.hostname
Directly mapped.
raw.infobloxb1ophipaddress
observer.ip
Directly mapped.
raw.infobloxb1policyname
security_result.detection_fields.value
Directly mapped with the key
infobloxb1policyname
.
raw.infobloxdnsqclass
dns_question.class
,
dns_answer.class
Used to derive
dns_question.class
and
dns_answer.class
based on a lookup table defined in the
dns_query_class_mapping.include
file.
raw.infobloxdnsqtype
dns_question.type
,
dns_answer.type
Used to derive
dns_question.type
and
dns_answer.type
based on a lookup table defined in the
dns_record_type.include
file.
raw.infobloxdnsrcode
network.dns.response_code
Used to derive
network.dns.response_code
based on a lookup table defined in the
dns_response_code.include
file.
raw.infobloxpolicyid
security_result.detection_fields.value
Directly mapped with the key
infobloxpolicyid
.
raw.msg
metadata.description
raw.msg
is directly mapped to
metadata.description
after removing leading and trailing quotes.
raw.name
metadata.product_event_type
Concatenated with
raw.deviceeventclassid
(separated by
-
) and mapped to
metadata.product_event_type
.
rcode
security_result.detection_fields.value
,
network.dns.response_code
rcode
is directly mapped to
security_result.detection_fields.value
with the key
rcode
.
If
rcode
is
NXDOMAIN
,
network.dns.response_code
is set to 3 (converted to unsigned integer).
rdata
network.dns.answers.data
Directly mapped.
rip
target.ip
,
target.asset.ip
Directly mapped.
severity
security_result.severity
Mapped based on the following logic:
- If
severity
is
INFO
(case-insensitive), map to
INFORMATIONAL
.
- If
severity
is
HIGH
, map to
HIGH
.
tclass
security_result.detection_fields.value
Directly mapped with the key
tclass
.
threat_indicator
security_result.detection_fields.value
Directly mapped with the key
threat_indicator
.
timestamp
metadata.event_timestamp.seconds
Parsed as an ISO8601 timestamp and the seconds value is extracted.
user
principal.user.user_display_name
Directly mapped.
user_groups
security_result.detection_fields.value
Directly mapped with the key
user_groups
.
N/A
principal.resource.resource_subtype
Set to
Feed
if
feed_name
is not empty.
N/A
metadata.log_type
Set to
BLOXONE
.
N/A
additional.fields.key
Set to
infobloxancount
,
infobloxarcount
,
infobloxb1connectiontype
,
infobloxnscount
,
intel:destination:ip:ip2asn:finish_ip
,
intel:destination:ip:ip2asn:start_ip
,
intel:source:ip:ip2asn:finish_ip
, or
intel:source:ip:ip2asn:start_ip
based on the corresponding
raw
fields.
N/A
metadata.event_type
Set to
STATUS_UPDATE
if
has_principal
is
true
, otherwise set to
GENERIC_EVENT
.
N/A
network.dns.questions.type
Set to 1 for
A
records and 12 for
PTR
records, converted to unsigned integer.
N/A
network.dns.answers.name
,
network.dns.answers.type
,
network.dns.answers.class
Extracted from
raw.msg
by parsing the DNS response string.
N/A
intermediary.hostname
,
intermediary.ip
,
intermediary.asset.ip
Extracted from
raw.msg
by parsing the DNS response string.
Note:
This table only includes fields that are mapped to the UDM. Some fields from the raw log might be used internally by the parser but are not directly reflected in the final UDM output.
Need more help?
Get answers from Community members and Google SecOps professionals.
