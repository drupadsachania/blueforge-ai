# Collect Zscaler Internet Access logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-internet-access/  
**Scraped:** 2026-03-05T09:18:17.575975Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler Internet Access logs
Supported in:
Google secops
SIEM
This document describes how you can export Zscaler Internet Access logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler Internet Access and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler Internet Access
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler Internet Access and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_INTERNET_ACCESS
ingestion label.
Before you begin
Ensure you have the following prerequisites:
Access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Zscaler Internet Access 2024 or later
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
Set up Zscaler Internet Access
In the Zscaler Internet Access console, click
Administration
>
Nanolog Streaming Service
>
Cloud NSS Feeds
and then click
Add Cloud NSS Feed
.
The
Add Cloud NSS Feed
window appears. In the
Add Cloud NSS Feed
window, enter the details.
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
drop-down as
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
. For example, 512 KB.
Enter the HTTPS URL of the Chronicle API endpoint in the API URL in the following format:
https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
CHRONICLE_REGION
: Region where your Chronicle instance is hosted. For example, US.
GOOGLE_PROJECT_NUMBER
: BYOP project number. Obtain this from C4.
LOCATION
: Chronicle region. For example, US.
CUSTOMER_ID
: Chronicle customer ID. Obtain from C4.
FEED_ID
: Feed ID shown on Feed UI on the new webhook created
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
Admin Audit Logs
in the
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
Following is the default
Feed Output Format
:
\
{
"sourcetype"
:
"zscalernss-audit"
,
"event"
:
\
{
"time"
:
"%s{time}"
,
"recordid"
:
"%d{recordid}"
,
"action"
:
"%s{action}"
,
"category"
:
"%s{category}"
,
"subcategory"
:
"%s{subcategory}"
,
"resource"
:
"%s{resource}"
,
"interface"
:
"%s{interface}"
,
"adminid"
:
"%s{adminid}"
,
"clientip"
:
"%s{clientip}"
,
"result"
:
"%s{result}"
,
"errorcode"
:
"%s{errorcode}"
,
"auditlogtype"
:
"%s{auditlogtype}"
,
"preaction"
:
%
s
{
preaction
},
"postaction"
:
%
s
{
postaction
}
\
}
\
}
Select the timezone for the
Time
field in the output file in the
Timezone
list. By default, the timezone is set to your organization's
time zone.
Review the configured settings.
Click
Save
to test connectivity. If the connection is successful, a green tick accompanied by the message
Test Connectivity Successful: OK (200)
appears.
For more information about Google SecOps feeds, see
Google Security Operations feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google Security Operations support
.
Supported Zscaler Internet Access log formats
The Zscaler Internet Access parser supports logs in JSON format.
Supported Zscaler Internet Access sample logs
JSON
{
  "sourcetype": "zscalernss-audit",
  "event": {
    "time": "Wed May 29 17:45:03 2024",
    "recordid": "6095",
    "action": "UPDATE",
    "category": "ACCESS_CONTROL_RESOURCE",
    "subcategory": "URL_CATEGORY",
    "resource": "Custom SSL Bypass",
    "interface": "UI",
    "adminid": "abc@xyz.com",
    "clientip": "198.51.100.1",
    "result": "SUCCESS",
    "errorcode": "None",
    "auditlogtype": "ZIA",
    "preaction": "{"id":{"val":130%2c"mask":255%2c"parent":"CUSTOM_SUPERCATEGORY"%2c"deprecated":false%2c"backendName":"custom_03"%2c"name":"CUSTOM_03"%2c"userConfiguredName":""}%2c"configuredName":"Custom%20SSL%20Bypass"%2c"superCategory":"USER_DEFINED"%2c"keywords":[]%2c"keywordsRetainingParentCategory":[]%2c"customUrlsToAdd":[]%2c"customUrlsToDelete":[]%2c"urlsRetainingParentCategoryToAdd":[]%2c"urlsRetainingParentCategoryToDelete":[]%2c"customIpRangesToAdd":[]%2c"customIpRangesToDelete":[]%2c"ipRangesRetainingParentCategoryToAdd":[]%2c"ipRangesRetainingParentCategoryToDelete":[]%2c"customCategory":true%2c"editable":true%2c"description":"https: //help.zscaler.com/zia/url-format-guidelines"%2c"type":"URL_CATEGORY"%2c"customUrlsCount":1%2c"urlsRetainingParentCategoryCount":60%2c"customIpRangesCount":0%2c"ipRangesRetainingParentCategoryCount":0%2c"urlsToAdd":[]%2c"urlsToDelete":[]%2c"dbCategorizedUrlsToAdd":[]%2c"dbCategorizedUrlsToDelete":[]}","postaction":"{"id":{"val":130%2c"mask":255%2c"parent":"CUSTOM_SUPERCATEGORY"%2c"deprecated":false%2c"backendName":"custom_03"%2c"name":"CUSTOM_03"%2c"userConfiguredName":""}%2c"configuredName":"Custom%20SSL%20Bypass"%2c"superCategory":"USER_DEFINED"%2c"customUrlsToAdd":[]%2c"customUrlsToDelete":[]%2c"urlsRetainingParentCategoryToAdd":["webcast.temoinproduction.com"]%2c"urlsRetainingParentCategoryToDelete":[]%2c"customIpRangesToAdd":[]%2c"customIpRangesToDelete":[]%2c"ipRangesRetainingParentCategoryToAdd":[]%2c"ipRangesRetainingParentCategoryToDelete":[]%2c"customCategory":true%2c"editable":true%2c"description":"https://help.zscaler.com/zia/url-format-guidelines"%2c"type":"URL_CATEGORY"%2c"customUrlsCount":1%2c"urlsRetainingParentCategoryCount":61%2c"customIpRangesCount":0%2c"ipRangesRetainingParentCategoryCount":0%2c"urlsToAdd":[]%2c"urlsToDelete":[]%2c"dbCategorizedUrlsToAdd":[]%2c"dbCategorizedUrlsToDelete":[]}"}
}
Field mapping reference
The following table lists the log fields of the
ZSCALER_INTERNET_ACCESS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.event_type
If the
action
log field value is equal to
SIGN_IN
, then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
SIGN_OUT
, then the
metadata.event_type
UDM field is set to
USER_LOGOUT
.
Else, the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
extensions_token.auth.type
If the
action
log field value contains one of the following values, then the
extensions_token.auth.type
UDM field is set to
MACHINE
.
SIGN_IN
SIGN_OUT
metadata.product_name
The
metadata.product_name
UDM field is set to
Admin Audit
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
sourcetype
additional.fields[sourcetype]
time
metadata.event_timestamp
recordid
metadata.product_log_id
action
security_result.action_details
category
security_result.category_details
subcategory
security_result.category_details
resource
target.resource.name
interface
principal.resource.attribute.labels[interface]
If the
action
log field value contain one of the following values, then the
interface
log field is mapped to
target.resource.attribute.labels[interface]
UDM field.
SIGN_IN
SIGN_OUT
Otherwise, the
interface
log field is mapped to
principal.resource.attribute.labels[interface]
UDM field.
adminid
principal.user.userid
If the
action
log field value contains one of the following values, then the
adminid
log field is mapped to
target.user.userid
UDM field.
SIGN_IN
SIGN_OUT
Otherwise, the
adminid
log field is mapped to
principal.user.userid
UDM field.
clientip
principal.ip
security_result.action
If the
event.result
log field value is equal to
SUCCESS
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
event.result
log field value is equal to
FAILURE
, then the
security_result.action
UDM field is set to
BLOCK
.
errorcode
security_result.summary
auditlogtype
additional.fields[auditlogtype]
preaction
security_result.detection_fields[preaction]
Iterate through preaction object: The
preaction object key
is mapped to the
security_result.detection_fields.key
UDM field and
preaction object value
is mapped to the
security_result.detection_fields.value
UDM field.
postaction
security_result.detection_fields[postaction]
Iterate through postaction object: The
postaction object key
is mapped to the
security_result.detection_fields.key
UDM field and
postaction object value
is mapped to the
security_result.detection_fields.value
UDM field.
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
mon
additional.fields[mon]
day
additional.fields[day]
intlogtime
additional.fields[intlogtime]
Need more help?
Get answers from Community members and Google SecOps professionals.
