# Collect Qualys Scan logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-scan/  
**Scraped:** 2026-03-05T09:27:38.661965Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Qualys Scan logs
Supported in:
Google secops
SIEM
This parser extracts fields from Qualys Scan JSON logs, normalizes timestamps, and maps them to the UDM. It handles various Qualys event types, including generic events and user logins, populating UDM fields with relevant security information and metadata.
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
Select the
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
Qualys Scan Logs
.
Select
Third Party API
as the
Source type
.
Select the
Qualys Scan
as the log type.
Click
Next
.
Specify values for the following input parameters:
Username
: enter the username for the dedicated user.
Secret
: enter the password for the dedicated user.
API Full Path
: provide plain Qualys API server URL (for example,
qualysapi.qg2.apps.qualys.eu
).
API Type
: select the scan type you want to ingest.
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
Category
security_result.category_details
Directly mapped from the
Category
field.
ID
metadata.product_log_id
Directly mapped from the
ID
field. Converted to string.
LaunchDatetime
metadata.event_timestamp
Used as event timestamp if
ScanInput.ScanDatetime
and
UpdateDate
are not present. Parsed in the "ISO8601" format.
Ref
additional.fields[1].key
additional.fields[1].value.string_value
Mapped to
additional.fields
with key "ScanReference" if
ScanReference
is not present.
ScanDetails.Status
security_result.detection_fields[0].key
security_result.detection_fields[0].value
Mapped to
security_result.detection_fields
with key "ScanDetails Status".
ScanInput.Network.ID
additional.fields[0].key
additional.fields[0].value.string_value
Mapped to
additional.fields
with key "ScanInput Network ID".
ScanInput.Network.Name
additional.fields[1].key
additional.fields[1].value.string_value
Mapped to
additional.fields
with key "ScanInput Network Name".
ScanInput.OptionProfile.ID
additional.fields[2].key
additional.fields[2].value.string_value
Mapped to
additional.fields
with key "ScanInput Option Profile ID".
ScanInput.OptionProfile.Name
additional.fields[3].key
additional.fields[3].value.string_value
Mapped to
additional.fields
with key "ScanInput Option Profile Name".
ScanInput.ScanDatetime
metadata.event_timestamp
Used as event timestamp if present. Parsed in the "ISO8601" format.
ScanInput.Title
metadata.description
Directly mapped from the
ScanInput.Title
field.
ScanInput.Username
principal.user.userid
Directly mapped from the
ScanInput.Username
field.
ScanReference
additional.fields[4].key
additional.fields[4].value.string_value
Mapped to
additional.fields
with key "ScanReference".
Statement
metadata.description
Directly mapped from the
Statement
field if
ScanInput.Title
and
Title
are not present.
Status
security_result.detection_fields[0].key
security_result.detection_fields[0].value
Mapped to
security_result.detection_fields
with key "Status".
SubCategory
security_result.description
Directly mapped from the
SubCategory
field.
Technologies[].ID
security_result.detection_fields[0].value
Directly mapped from the
Technologies[].ID
field. Converted to string. Part of a repeated
security_result
object.
Technologies[].Name
security_result.detection_fields[1].value
Directly mapped from the
Technologies[].Name
field. Part of a repeated
security_result
object.
Technologies[].Rationale
security_result.detection_fields[2].value
Directly mapped from the
Technologies[].Rationale
field. Part of a repeated
security_result
object.
Title
metadata.description
Directly mapped from the
Title
field if
ScanInput.Title
and
Statement
are not present.
Type
additional.fields[2].key
additional.fields[2].value.string_value
Mapped to
additional.fields
with key "Type".
UpdateDate
metadata.event_timestamp
Used as event timestamp if
ScanInput.ScanDatetime
is not present. Parsed in the "ISO8601" format.
Userlogin
target.user.userid
Directly mapped from the
Userlogin
field. Set to "AUTHTYPE_UNSPECIFIED" if
Userlogin
is present. Set to "GENERIC_EVENT". Changed to "USER_LOGIN" if
Userlogin
is present. Changed to "USER_UNCATEGORIZED" if
metadata_event_type
is "GENERIC_EVENT" and
ScanInput.Username
is present. Set to "QUALYS_SCAN". Set to "QUALYS_SCAN". Set to "ID" for each technology. Part of a repeated
security_result
object. Set to "Name" for each technology. Part of a repeated
security_result
object. Set to "Rationale" for each technology. Part of a repeated
security_result
object.
Need more help?
Get answers from Community members and Google SecOps professionals.
