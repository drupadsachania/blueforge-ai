# Collect Qualys Vulnerability Management logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-vm/  
**Scraped:** 2026-03-05T09:59:28.140691Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Qualys Vulnerability Management logs
Supported in:
Google secops
SIEM
This parser handles Qualys Vulnerability Management logs in either key-value (KV) or JSON format. It extracts vulnerability details, host information, and scan metadata, mapping them to the UDM. The parser also handles different log structures, prioritizing KV parsing and falling back to JSON if necessary, and splits the
DetectionList
array into individual vulnerability events.
Before you begin
Ensure that you have the following prerequisites:
Google Security Operations instance.
Privileged access to Qualys VMDR console.
Optional: Create a dedicated API User in Qualys
Sign in to the Qualys console.
Go to
Users
.
Click
New
>
User
.
Enter the
General Information
required for the user.
Select
User Role
tab.
Make sure the role has the
API Access
checkbox selected.
Click
Save
.
Identify your specific Qualys API URL
Option 1
Identify your URLs as mentioned in the
platform identification
.
Option 2
Sign in to the Qualys console.
Go to
Help
>
About
.
Scroll to see this information under Security Operations Center (SOC).
Copy the Qualys API URL.
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
Qualys VM Logs
.
Select
Third Party API
as the
Source type
.
Select the
Qualys VM
as the log type.
Click
Next
.
Specify values for the following input parameters:
Username
: enter the username.
Secret
: enter the password.
API Full Path
: provide the Qualys API server URL (for example,
<qualys_base_url>/api/2.0/fo/asset/host/?action=list
) where
<qualys_base_url>
is the base URL to the Qualys API server where your account is located.
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
DETECTION.FIRST_FOUND_DATETIME
extensions.vulns.vulnerabilities.first_found
Parsed from
DETECTION.FIRST_FOUND_DATETIME
field, converting the string value to a timestamp.
DETECTION.LAST_FOUND_DATETIME
extensions.vulns.vulnerabilities.last_found
Parsed from
DETECTION.LAST_FOUND_DATETIME
field, converting the string value to a timestamp.
DETECTION.QID
extensions.vulns.vulnerabilities.name
Concatenates "QID: " with the value of
DETECTION.QID
.
DETECTION.RESULTS
extensions.vulns.vulnerabilities.description
Directly maps to the description field.  Also used to extract
network.ip_protocol
and
principal.port
using grok.
DETECTION.SEVERITY
extensions.vulns.vulnerabilities.severity
Mapped from
DETECTION.SEVERITY
. Values 0, 1, 2 become "LOW"; 3, 4 become "MEDIUM"; 5, 6, 7 become "HIGH".
DETECTION.STATUS
extensions.vulns.vulnerabilities.about.labels
Added as a label with key "Detection status".
DETECTION.TYPE
extensions.vulns.vulnerabilities.about.labels
Added as a label with key "Detection type".
DNS
principal.hostname
Directly maps to
principal.hostname
.
DNSData.DOMAIN
principal.domain.name
Directly maps to
principal.domain.name
.
HOST.ASSET_ID
principal.asset_id
Concatenates "QUALYS:" with the value of
HOST.ASSET_ID
.
HOST.DNS
principal.hostname
Directly maps to
principal.hostname
if
DNS
is empty.
HOST.DNS_DATA.DOMAIN
principal.domain.name
Directly maps to
principal.domain.name
if
DNSData.DOMAIN
is empty.
HOST.ID
metadata.product_log_id
Directly maps to
metadata.product_log_id
.
HOST.IP
principal.ip
Directly maps to
principal.ip
if
IP
is empty.
HOST.LAST_SCAN_DATETIME
extensions.vulns.vulnerabilities.scan_start_time
Parsed from
HOST.LAST_SCAN_DATETIME
field, converting the string value to a timestamp.
HOST.LAST_VM_SCANNED_DATE
extensions.vulns.vulnerabilities.scan_end_time
Parsed from
HOST.LAST_VM_SCANNED_DATE
field, converting the string value to a timestamp.
HOST.NETBIOS
additional.fields
Added as a label with key "HOST NETBIOS".
HOST.OS
principal.platform_version
Directly maps to
principal.platform_version
if
OS
is empty.
HOST.QG_HOSTID
additional.fields
Added as a label with key "HOST QG_HOSTID".
HOST.TRACKING_METHOD
additional.fields
Added as a label with key "HOST TRACKING_METHOD".
HOST_ID
principal.asset_id
Concatenates "QUALYS:" with the value of
HOST_ID
.
ID
metadata.product_log_id
Directly maps to
metadata.product_log_id
.
IP
principal.ip
Directly maps to
principal.ip
.
LastScanDateTime
extensions.vulns.vulnerabilities.scan_start_time
Parsed from
LastScanDateTime
field, converting the string value to a timestamp.
LastVMAuthScanDuration
additional.fields
Added as a label with key "LastVMAuthScanDuration".
LastVMScanDate
extensions.vulns.vulnerabilities.scan_end_time
Parsed from
LastVMScanDate
field, converting the string value to a timestamp.
LastVMScanDuration
additional.fields
Added as a label with key "LastVMScanDuration".
LAST_FOUND_DATETIME
extensions.vulns.vulnerabilities.last_found
Parsed from
LAST_FOUND_DATETIME
field, converting the string value to a timestamp.
LAST_SCAN_DATETIME
extensions.vulns.vulnerabilities.scan_start_time
Parsed from
LAST_SCAN_DATETIME
field, converting the string value to a timestamp.
LAST_VM_SCANNED_DATE
extensions.vulns.vulnerabilities.scan_end_time
Parsed from
LAST_VM_SCANNED_DATE
field, converting the string value to a timestamp.
NETBIOS
additional.fields
Added as a label with key "NETBIOS".
NetworkID
additional.fields
Added as a label with key "NetworkID".
NETWORK_ID
additional.fields
Added as a label with key "NetworkID".
OS
principal.platform_version
Directly maps to
principal.platform_version
.
Os
principal.platform_version
Directly maps to
principal.platform_version
if
OS
is empty.
QID
extensions.vulns.vulnerabilities.name
Concatenates "QID: " with the value of
QID
.
QgHostID
principal.asset_id
Sets
principal.asset_id
to "Host Id:%{QgHostID}".
SEVERITY
extensions.vulns.vulnerabilities.severity
Mapped from
SEVERITY
. Values 0, 1, 2 become "LOW"; 3, 4 become "MEDIUM"; 5, 6, 7 become "HIGH".
TRACKING_METHOD
additional.fields
Added as a label with key "TRACKING_METHOD".
TrackingMethod
additional.fields
Added as a label with key "TRACKING_METHOD".
N/A
metadata.vendor_name
Hardcoded to "Qualys".
N/A
metadata.product_name
Hardcoded to "Vulnerability Management".
N/A
metadata.event_type
Set to "SCAN_VULN_HOST" if
_vulns
is not empty, "STATUS_UPDATE" if either
prin_host
or
IP
are not empty, and "GENERIC_EVENT" otherwise.
N/A
metadata.log_type
Taken from the raw log's
log_type
field.
N/A
principal.platform
Determined from
OS
,
Os
, or
HOST.OS
.  If any of these contain "Linux", the platform is set to "LINUX". If any contain "Windows", the platform is set to "WINDOWS". If any contain "mac" or "IOS", the platform is set to "MAC".
detection.DType
extensions.vulns.vulnerabilities.about.resource.attribute.labels
Added as a label with key "Detection Type" within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.FirstFoundTime
extensions.vulns.vulnerabilities.first_found
Parsed from
detection.FirstFoundTime
field, converting the string value to a timestamp within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.LastFoundTime
extensions.vulns.vulnerabilities.last_found
Parsed from
detection.LastFoundTime
field, converting the string value to a timestamp within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.LastProcessedDatetime
extensions.vulns.vulnerabilities.about.resource.attribute.labels
Added as a label with key "LastProcessedDatetime" within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.LastTestDateTime
extensions.vulns.vulnerabilities.about.resource.attribute.labels
Added as a label with key "LastTestDateTime" within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.LastUpdateDateTime
extensions.vulns.vulnerabilities.about.resource.attribute.labels
Added as a label with key "LastUpdateDateTime" within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.Qid
extensions.vulns.vulnerabilities.name
Concatenates "QID: " with the value of
detection.Qid
within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.Results
extensions.vulns.vulnerabilities.description
Directly maps to the description field within the vulnerabilities array for events parsed from the
DetectionList
field.  Tabs and newlines are replaced with spaces.
detection.Severity
extensions.vulns.vulnerabilities.severity
Mapped from
detection.Severity
. Values 0, 1, 2 become "LOW"; 3, 4 become "MEDIUM"; 5, 6, 7 become "HIGH" within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.Status
extensions.vulns.vulnerabilities.about.resource.attribute.labels
Added as a label with key "Detection status" within the vulnerabilities array for events parsed from the
DetectionList
field.
detection.TimesFound
extensions.vulns.vulnerabilities.about.resource.attribute.labels
Added as a label with key "TimesFound" within the vulnerabilities array for events parsed from the
DetectionList
field.
timestamp
metadata.event_timestamp
,
timestamp
The raw log's
timestamp
field is used for both the event timestamp and the top-level timestamp.
Need more help?
Get answers from Community members and Google SecOps professionals.
