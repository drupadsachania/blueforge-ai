# Collect Zscaler DLP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dlp/  
**Scraped:** 2026-03-05T09:18:13.118005Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler DLP logs
Supported in:
Google secops
SIEM
This document explains how to export Zscaler DLP logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler DLP and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler DLP
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler DLP and writes logs to Google SecOps.
Google Security Operations
: retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_DLP
label.
Before you begin
Ensure you have the following prerequisites:
Access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Zscaler DLP 2024 or later
All systems in the deployment architecture are configured with the UTC time zone.
The API key which is needed to complete feed setup in Google Security Operations. For more information, see
Setting up API keys
.
Set up feeds
To configure this log type, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
Zscaler
feed pack.
Locate the required log type and click
Add New Feed
.
Enter values for the following input parameters:
Source Type
: Webhook (Recommended)
Split delimiter
: the character used to separate logs lines. Leave blank if no delimiter is used.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
:
Namespace associated with the feed
.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create Feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Set up Zscaler DLP
In Zscaler Internet Access console, go to
Administration
>
Nanolog Streaming Service
>
Cloud NSS Feeds
.
Click
Add Cloud NSS Feed
.
Enter a name for the feed in the
Feed Name
field.
Select
NSS for Web
in
NSS Type
.
Select the status from the
Status
list to activate or deactivate the NSS feed.
Keep the value in the
SIEM Rate
menu as
Unlimited
. To suppress the output stream due to licensing or other constraints, change the value.
Select
Other
in the
SIEM Type
list.
Select
Disabled
in the
OAuth 2.0 Authentication
list.
Enter a size limit for an individual HTTP request payload to the SIEM's best practice in
Max Batch Size
(for example,
512 KB
).
Enter the HTTPS URL of the Chronicle API endpoint in the API URL in the following format:
https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
CHRONICLE_REGION
: region where your Google SecOps instance is hosted (for example,
US
).
GOOGLE_PROJECT_NUMBER
: BYOP project number (obtain this from C4).
LOCATION
: Google SecOps region (for example,
US
).
CUSTOMER_ID
: Google SecOps customer ID (obtain this from C4).
FEED_ID
: Feed ID shown on the Feed UI on the new webhook created.
Sample API URL:
https://us-chronicle.googleapis.com/v1alpha/projects/12345678910/locations/US/instances/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/feeds/yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy:importPushLogs
Click
Add HTTP Header
, and then add HTTP headers in the following format:
Header 1
:
Key1:
X-goog-api-key
and
Value1:
API Key generated on Google Cloud BYOP's API Credentials.
Header 2
:
Key2:
X-Webhook-Access-Key
and
Value2:
API secret key generated on webhook's "SECRET KEY".
Select
Endpoint DLP
from the
Log Types
list.
Select
JSON
in the
Feed Output Type
list.
Disable
JSON Array Notation
.
Set
Feed Escape Character
to
, \ "
.
To add a new field to the
Feed Output Format,
select
Custom
in the
Feed Output Type
list.
Copy-paste the
Feed Output Format
and add new fields. Ensure the key names match the actual field names.
The following is the default
Feed Output Format
:
\{ "sourcetype" : "zscalernss-edlp", "event" :\{"time":"%s{time}","recordid":"%d{recordid}","login":"%s{user}","dept":"%s{department}","filetypename":"%s{filetypename}","filemd5":"%s{filemd5}","dlpdictnames":"%s{dlpdictnames}","dlpdictcount":"%s{dlpcounts}","dlpenginenames":"%s{dlpengnames}","channel":"%s{channel}","actiontaken":"%s{actiontaken}","severity":"%s{severity}","rulename":"%s{triggeredrulelabel}","itemdstname":"%s{itemdstname}"\}\}
Select the time zone for the
Time
field in the output file in the
Timezone
list. By default, the time zone is set to your organization's
time zone.
Review the configured settings.
Click
Save
to test connectivity. If the connection is successful, a green tick accompanied by the message
Test Connectivity Successful: OK (200)
appears.
For more information about Google SecOps feeds, see
Google SecOps feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Supported Zscaler DLP log formats
The Zscaler DLP parser supports logs in JSON format.
Supported Zscaler DLP sample logs
JSON:
{
  "sourcetype": "zscalernss-edlp",
  "event": {
    "time": "Thu Jun 20 21:14:56 2024",
    "recordid": "7382697059455533057",
    "login": "dummy@domain.com",
    "dept": "General Group",
    "filetypename": "xlsx",
    "filemd5": "9a2d0d62c22994a98f65939ddcd3eb8f",
    "dlpdictnames": "Social Security Number (US): Detect leakage of United States Social Security Numbers|Credit Cards: Detect leakage of credit card information|Aadhaar Card Number (India): Detect Leakage of Indian Aadhaar Card Numbers",
    "dlpdictcount": "1428|141|81",
    "dlpenginenames": "Dummy Engine|cc|PCI|GLBA|HIPAA",
    "channel": "Removable Storage",
    "actiontaken": "Confirm Allow",
    "severity": "High Severity",
    "rulename": "Endpoint_DLP_",
    "itemdstname": "Removable Storage"
  }
}
UDM Mapping Table
The following table lists the log fields of the
ZSCALER_DLP
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
mon
additional.fields[mon]
day
additional.fields[day]
scantime
additional.fields[scantime]
numdlpengids
security_result.detection_fields[numdlpengids]
numdlpdictids
security_result.detection_fields[numdlpdictids]
recordid
metadata.product_log_id
scanned_bytes
additional.fields[scanned_bytes]
dlpidentifier
security_result.detection_fields[dlpidentifier]
login
principal.user.user_display_name
b64user
principal.user.user_display_name
euser
principal.user.user_display_name
ouser
principal.user.user_display_name
dept
principal.user.department
b64department
principal.user.department
edepartment
principal.user.department
odepartment
principal.user.department
odevicename
security_result.detection_fields[odevicename]
devicetype
principal.asset.attribute.labels[devicetype]
principal.asset.platform_software.platform
If the
deviceostype
log field value matches the regular expression pattern
(?i)Windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
devicename, b64devicename, edevicename, odevicename
principal.asset.asset_id
If the
devicename
log field value is
not
empty, then the
asset_id:devicename
log field is mapped to the
principal.asset.asset_id
UDM field.
If the
b64devicename
log field value is
not
empty, then the
asset_id:b64devicename
log field is mapped to the
principal.asset.asset_id
UDM field.
If the
edevicename
log field value is
not
empty, then the
asset_id:edevicename
log field is mapped to the
principal.asset.asset_id
UDM field.
If the
odevicename
log field value is
not
empty, then the
asset_id:odevicename
log field is mapped to the
principal.asset.asset_id
UDM field.
deviceplatform
principal.asset.attribute.labels[deviceplatform]
deviceosversion
principal.asset.platform_software.platform_version
devicemodel
principal.asset.hardware.model
deviceappversion
principal.asset.software.version
deviceowner
principal.asset.attribute.labels[deviceowner]
b64deviceowner
principal.asset.attribute.labels[b64deviceowner]
edeviceowner
principal.asset.attribute.labels[edeviceowner]
odeviceowner
principal.asset.attribute.labels[odeviceowner]
devicehostname
principal.hostname
b64devicehostname
principal.hostname
edevicehostname
principal.hostname
odevicehostname
principal.hostname
datacenter
target.location.name
datacentercity
target.location.city
datacentercountry
target.location.country_or_region
dsttype
target.resource.resource_subtype
filedoctype
additional.fields[filedoctype]
filedstpath
target.file.full_path
b64filedstpath
target.file.full_path
efiledstpath
target.file.full_path
filemd5
target.file.md5
If the
filemd5
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
filemd5
log field is mapped to the
target.file.md5
UDM field.
filesha
target.file.sha256
If the
filesha
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
filesha
log field is mapped to the
target.file.sha256
UDM field.
filesrcpath
src.file.full_path
b64filesrcpath
src.file.full_path
efilesrcpath
src.file.full_path
filetypecategory
additional.fields[filetypecategory]
filetypename
target.file.mime_type
itemdstname
target.resource.name
b64itemdstname
target.resource.name
eitemdstname
target.resource.name
itemname
target.resource.attribute.labels[itemname]
b64itemname
target.resource.attribute.labels[b64itemname]
eitemname
target.resource.attribute.labels[eitemname]
itemsrcname
src.resource.name
b64itemsrcname
src.resource.name
eitemsrcname
src.resource.name
itemtype
target.resource.attribute.labels[itemtype]
ofiledstpath
target.file.full_path
ofilesrcpath
src.file.full_path
oitemdstname
target.resource.name
oitemname
target.resource.attribute.labels[oitemname]
odlpengnames
security_result.detection_fields[odlpengnames]
oitemsrcname
src.resource.name
srctype
src.resource.resource_subtype
actiontaken
security_result.action_details
security_result.action
If the
actiontaken
log field value matches the regular expression pattern
(?i)allow
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
actiontaken
log field value matches the regular expression pattern
(?i)block
, then the
security_result.action
UDM field is set to
BLOCK
.
activitytype
metadata.product_event_type
addinfo
additional.fields[addinfo]
channel
security_result.detection_fields[channel]
confirmaction
security_result.detection_fields[confirmaction]
confirmjust
security_result.description
dlpdictcount
security_result.detection_fields[dlpdictcount]
dlpdictnames
security_result.detection_fields[dlpdictnames]
b64dlpdictnames
security_result.detection_fields[b64dlpdictnames]
edlpdictnames
security_result.detection_fields[edlpdictnames]
dlpenginenames
security_result.detection_fields[dlpenginenames]
b64dlpengnames
security_result.detection_fields[b64dlpengnames]
edlpengnames
security_result.detection_fields[edlpengnames]
expectedaction
security_result.detection_fields[expectedaction]
logtype
security_result.category_details
odlpdictnames
security_result.detection_fields[odlpdictnames]
ootherrulelabels
security_result.rule_labels[ootherrulelabels]
otherrulelabels
security_result.rule_labels[otherrulelabels]
b64otherrulelabels
security_result.rule_labels[b64otherrulelabels]
eotherrulelabels
security_result.rule_labels[eotherrulelabels]
otriggeredrulelabel
security_result.rule_name
severity
security_result.severity_details
security_result.severity
If the
severity
log field value matches the regular expression pattern
(?i)High
, then the
security_result.severity
UDM field is set to
HIGH
.
Else, if the
severity
log field value matches the regular expression pattern
(?i)Medium
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value matches the regular expression pattern
(?i)Low
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
severity
log field value matches the regular expression pattern
(?i)Info
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
rulename
security_result.rule_name
b64triggeredrulelabel
security_result.rule_name
etriggeredrulelabel
security_result.rule_name
zdpmode
security_result.detection_fields[zdpmode]
tz
additional.fields[tz]
ss
additional.fields[ss]
mm
additional.fields[mm]
hh
additional.fields[hh]
dd
additional.fields[dd]
mth
additional.fields[mth]
yyyy
additional.fields[yyyy]
sourcetype
additional.fields[sourcetype]
eventtime
metadata.event_timestamp
time
metadata.collected_timestamp
rtime
additional.fields[rtime]
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
metadata.product_name
The
metadata.product_name
UDM field is set to
DLP
.
metadata.event_type
If the
activitytype
log field value is one of the following, then the
metadata.event_type
UDM field is set to
FILE_UNCATEGORIZED
:
Upload
Download
Else, if the
activitytype
log field value is
File Copy
, then the
metadata.event_type
UDM field is set to
FILE_COPY
.
Else, if the
activitytype
log field value is
File Read
, then the
metadata.event_type
UDM field is set to
FILE_READ
.
Else, if the
activitytype
log field value is
File Write
, then the
metadata.event_type
UDM field is set to
FILE_MODIFICATION
.
Else, if the
activitytype
log field value is
Email Sent
, then the
metadata.event_type
UDM field is set to
EMAIL_UNCATEGORIZED
.
Else, if the
activitytype
log field value is
Print
, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, if one of the
devicehostname
,
b64devicehostname
,
edevicehostname
, or
odevicehostname
log fields is not empty, and one of the
filedstpath
,
b64filedstpath
,
efiledstpath
,
ofiledstpath
,
filemd5
,
filesha
, or
filetypename
log fields is not empty, then if one of the
filesrcpath
,
b64filesrcpath
,
efilesrcpath
, or
ofiledstpath
log fields is not empty, the
metadata.event_type
UDM field is set to
FILE_COPY
, otherwise it is set to
FILE_UNCATEGORIZED
.
Else, if one of the
devicehostname
,
b64devicehostname
,
edevicehostname
, or
odevicehostname
log fields is not empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
