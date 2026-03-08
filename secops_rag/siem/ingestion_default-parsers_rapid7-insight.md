# Collect Rapid7 InsightIDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-insight/  
**Scraped:** 2026-03-05T09:27:43.734741Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Rapid7 InsightIDR logs
Supported in:
Google secops
SIEM
This parser handles both JSON and SYSLOG formatted logs from Rapid7 InsightIDR. It extracts fields, normalizes them to the UDM, and performs specific logic for vulnerability data, including CVSS scores and exploit information, handling both JSON and syslog formats separately. It also maps authentication attempts and session events to appropriate UDM event types.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to the InsightIDR management console.
Configuring an API key in Rapid7 InsightIDR
Sign in to the InsightIDR Command Platform.
Click
Administration
.
Click
API Keys
.
Go to the
Organization Keys
tab.
Click
New Organization Key
.
Select an organization and provide a name for the key (for example,
Google SecOps
).
Generate the key.
Copy the key from a new window that displays the generated key.
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
Rapid7 InsightIDR Logs
.
Select
Third party API
as the
Source type
.
Select
Rapid7 Insight
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Authentication HTTP Header
: token previously generated in
X-Api-Key:<value>
format (for example,
X-Api-Key:AAAABBBBCCCC111122223333
).
API Endpoint
: enter
vulnerabilities
or
assets
.
API Hostname
: the FQDN (fully qualified domain name) of Rapid7 API endpoint in the
[region].api.insight.rapid7.com
format.
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
added
vulnerabilities.first_found
The
added
field is converted to a timestamp and mapped to
vulnerabilities.first_found
.
Authentication
security_result.detection_fields.value
The value of
Authentication
from the raw log is mapped to the
value
field within
security_result.detection_fields
. The corresponding
key
is set to "Authentication".
critical_vulnerabilities
asset.attribute.labels.value
The value of
critical_vulnerabilities
is mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Critical Vulnerabilities".
cves
vulnerabilities.cve_id
The value of
cves
is mapped to
vulnerabilities.cve_id
.
cvss_v2_access_complexity
asset.attribute.labels.value
The value of
cvss_v2_access_complexity
is mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Access Complexity(Ac)".
cvss_v2_availability_impact
asset.attribute.labels.value
The value of
cvss_v2_availability_impact
is mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Availability Impact (A)".
cvss_v2_confidentiality_impact
asset.attribute.labels.value
The value of
cvss_v2_confidentiality_impact
is mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Confidentiality Impact (C)".
cvss_v2_integrity_impact
asset.attribute.labels.value
The value of
cvss_v2_integrity_impact
is mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Integrity Impact (I)".
cvss_v2_score
vulnerabilities.cvss_base_score
The value of
cvss_v2_score
is converted to a string, then to a float, and mapped to
vulnerabilities.cvss_base_score
.
cvss_v2_vector
vulnerabilities.cvss_vector
The value of
cvss_v2_vector
is mapped to
vulnerabilities.cvss_vector
.
cvss_v3_availability_impact
asset.attribute.labels.value
The value of
cvss_v3_availability_impact
is mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Availability Impact (A)".
cvss_v3_score
vulnerabilities.cvss_base_score
The value of
cvss_v3_score
is converted to a string, then to a float, and mapped to
vulnerabilities.cvss_base_score
.
cvss_v3_vector
vulnerabilities.cvss_vector
The value of
cvss_v3_vector
is mapped to
vulnerabilities.cvss_vector
.
description
vulnerabilities.description
The value of
description
from the raw log is mapped to
vulnerabilities.description
.
exploits
asset.attribute.labels.value
The value of
exploits
is converted to a string and mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is either "Number of Exploits" or "Rank of Exploit" based on the presence of the "rank" field within the
exploits
object.
host_name
asset.hostname
The value of
host_name
is mapped to
asset.hostname
. If
host_name
is empty and both
ip
and
mac
are empty, the value of
id
is used instead.
id
asset.product_object_id
The value of
id
is mapped to
asset.product_object_id
. If
host_name
is empty and both
ip
and
mac
are empty, the value of
id
is used for
asset.hostname
.
ip
asset.ip
,
entity.asset.ip
The value of
ip
is mapped to both
asset.ip
and
entity.asset.ip
.
last_assessed_for_vulnerabilities
vulnerabilities.scan_end_time
The
last_assessed_for_vulnerabilities
field is converted to a timestamp and mapped to
vulnerabilities.scan_end_time
.
last_scan_end
vulnerabilities.last_found
The
last_scan_end
field is converted to a timestamp and mapped to
vulnerabilities.last_found
.
last_scan_start
vulnerabilities.first_found
The
last_scan_start
field is converted to a timestamp and mapped to
vulnerabilities.first_found
.
links
vulnerabilities.cve_id
,
vulnerabilities.vendor_knowledge_base_article_id
The
id
field within
links
is mapped to
vulnerabilities.cve_id
, and the
href
field within
links
is mapped to
vulnerabilities.vendor_knowledge_base_article_id
.
mac
asset.mac
,
entity.asset.mac
The value of
mac
is converted to lowercase and mapped to both
asset.mac
and
entity.asset.mac
.
MessageSourceAddress
principal.ip
,
principal.asset.ip
The IP address extracted from
MessageSourceAddress
is mapped to
principal.ip
and
principal.asset.ip
.
Method
network.http.method
The value of
Method
is mapped to
network.http.method
.
moderate_vulnerabilities
asset.attribute.labels.value
The value of
moderate_vulnerabilities
is converted to a string and mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Moderate Vulnerabilities".
os_architecture
asset.hardware.cpu_platform
The value of
os_architecture
is mapped to
asset.hardware.cpu_platform
.
os_description
asset.platform_software.platform_version
The value of
os_description
is mapped to
asset.platform_software.platform_version
.
os_family
asset.platform_software.platform
The value of
os_family
is converted to uppercase and mapped to
asset.platform_software.platform
. Special handling is done for "MAC OS X", "IOS", "WINDOWS", "MAC", and "LINUX". If it doesn't match any of these, it's set to "UNKNOWN_PLATFORM".
Port
principal.port
The value of
Port
is mapped to
principal.port
and converted to an integer.
Principal
principal.user.email_addresses
If
Principal
is an email address, it's mapped to
principal.user.email_addresses
.
product_event_type
metadata.product_event_type
The value of
product_event_type
is mapped to
metadata.product_event_type
.
Protocol
network.application_protocol
If
Protocol
is "HTTP" or "HTTPS", it's mapped to
network.application_protocol
.
published
vulnerabilities.last_found
The
published
field is converted to a timestamp and mapped to
vulnerabilities.last_found
.
Referer
network.http.referral_url
The value of
Referer
is mapped to
network.http.referral_url
.
risk_score
asset.attribute.labels.value
The value of
risk_score
is converted to a string and mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Risk Score".
security_result_summary
security_result.summary
The value of
security_result_summary
is mapped to
security_result.summary
. If it matches the pattern "Total sessions for principal:
", the number is extracted and mapped to a separate label with key "Session Count" within
security_result.detection_fields
.
Session
network.session_id
The value of
Session
is mapped to
network.session_id
.
severe_vulnerabilities
asset.attribute.labels.value
The value of
severe_vulnerabilities
is converted to a string and mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Severe Vulnerabilities".
severity
vulnerabilities.severity
,
security_result.severity
The value of
severity
is converted to uppercase. If it's "HIGH", "LOW", "CRITICAL", or "MEDIUM", it's mapped to
vulnerabilities.severity
. For syslog messages, if it's "Info", it's mapped to "INFORMATIONAL" in
security_result.severity
. If it's "Error", it's mapped to "ERROR" in
security_result.severity
.
severity_score
asset.attribute.labels.value
The value of
severity_score
is converted to a string and mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Severity Score".
SiloID
security_result.detection_fields.value
The value of
SiloID
is mapped to the
value
field within
security_result.detection_fields
. The corresponding
key
is set to "Silo ID".
SourceModuleName
target.resource.name
The value of
SourceModuleName
with quotes removed is mapped to
target.resource.name
.
SourceModuleType
observer.application
The value of
SourceModuleType
with quotes and closing brackets removed is mapped to
observer.application
.
Status
network.http.response_code
The value of
Status
is mapped to
network.http.response_code
and converted to an integer.
tags
asset.attribute.labels
For each element in the
tags
array, the
type
field is mapped to
key
and the
name
field is mapped to
value
within
asset.attribute.labels
.
Thread
security_result.detection_fields.value
The value of
Thread
is mapped to the
value
field within
security_result.detection_fields
. The corresponding
key
is set to "Thread".
timestamp
event.timestamp
,
metadata.collected_timestamp
,
read_only_udm.metadata.event_timestamp
The
timestamp
field is converted to a timestamp and mapped to
event.timestamp
for JSON logs and
metadata.collected_timestamp
for entity events. For syslog messages, it's mapped to
read_only_udm.metadata.event_timestamp
.
title
vulnerabilities.description
The value of
title
is mapped to
vulnerabilities.description
.
total_vulnerabilities
asset.attribute.labels.value
The value of
total_vulnerabilities
is converted to a string and mapped to the
value
field within
asset.attribute.labels
. The corresponding
key
is set to "Total Vulnerabilities".
URI
security_result.detection_fields.value
The value of
URI
is mapped to the
value
field within
security_result.detection_fields
. The corresponding
key
is set to "URI".
User-Agent
network.http.user_agent
,
network.http.parsed_user_agent
The value of
User-Agent
is mapped to
network.http.user_agent
. It's also mapped to
network.http.parsed_user_agent
and converted to a parsed user agent object.  Hardcoded to "Rapid7 Insight". Hardcoded to "Rapid7 Insight". Hardcoded to "ASSET" for JSON logs. Set to "GENERIC_EVENT" initially, then potentially changed to "PROCESS_UNCATEGORIZED", "STATUS_UPDATE", or "USER_LOGIN" based on other fields. Set to "AUTHTYPE_UNSPECIFIED" for "USER_LOGIN" events. Set to "ALLOW" or "BLOCK" based on
product_event_type
. Hardcoded to "RAPID7_INSIGHT" for syslog messages.
username
principal.user.user_display_name
The value of
username
, with quotes removed and potentially parsed for email address, is mapped to
principal.user.user_display_name
. The extracted email address, if present, is mapped to
principal.user.email_addresses
.
Need more help?
Get answers from Community members and Google SecOps professionals.
