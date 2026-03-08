# Collect Zscaler Webproxy logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-webproxy/  
**Scraped:** 2026-03-05T09:49:10.398504Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler Webproxy logs
Supported in:
Google secops
SIEM
This document describes how you can export Zscaler Webproxy logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler Webproxy and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler Webproxy
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler Webproxy and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_WEBPROXY
ingestion label.
Before you begin
Ensure you have the following prerequisites:
Access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Zscaler Webproxy 2024 or later
All systems in the deployment architecture are configured with the UTC time zone.
The API key which is needed to complete feed setup in Google Security Operations. For more information, see
Setting up API keys
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
Content Hub
>
Content Packs
Set up feeds from SIEM Settings
>
Feeds
To configure multiple feeds for different log types within this product family, see
Configure feeds by product
.
To configure a single feed, follow these steps:
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
Zscaler Webproxy Logs
.
Select
Webhook
as the
Source Type
.
Select
Zscaler
as the
Log Type
.
Click
Next
.
Optional: Enter values for the following input parameters:
Split delimiter
: The delimiter that is used to separate the logs lines. Leave blank if a delimiter is not used.
Asset namespace
: The asset namespace.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate
this feed.
Set up feeds from the Content Hub
Specify values for the following fields:
Split delimiter
: The delimiter that is used to separate log lines, such as
\n
.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Source Type
: Method used to collect logs into Google SecOps.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Set up Zscaler Webproxy
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
Web Logs
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
"zscalernss-web"
,
"event"
:
\
{
"datetime"
:
"%d{yy}-%02d{mth}-%02d{dd} %02d{hh}:%02d{mm}:%02d{ss}"
,
"reason"
:
"%s{reason}"
,
"event_id"
:
"%d{recordid}"
,
"protocol"
:
"%s{proto}"
,
"action"
:
"%s{action}"
,
"transactionsize"
:
"%d{totalsize}"
,
"responsesize"
:
"%d{respsize}"
,
"requestsize"
:
"%d{reqsize}"
,
"urlcategory"
:
"%s{urlcat}"
,
"serverip"
:
"%s{sip}"
,
"requestmethod"
:
"%s{reqmethod}"
,
"refererURL"
:
"%s{ereferer}"
,
"useragent"
:
"%s{eua}"
,
"product"
:
"NSS"
,
"location"
:
"%s{elocation}"
,
"ClientIP"
:
"%s{cip}"
,
"status"
:
"%s{respcode}"
,
"user"
:
"%s{elogin}"
,
"url"
:
"%s{eurl}"
,
"vendor"
:
"Zscaler"
,
"hostname"
:
"%s{ehost}"
,
"clientpublicIP"
:
"%s{cintip}"
,
"threatcategory"
:
"%s{malwarecat}"
,
"threatname"
:
"%s{threatname}"
,
"filetype"
:
"%s{filetype}"
,
"appname"
:
"%s{appname}"
,
"app_status"
:
"%s{app_status}"
,
"pagerisk"
:
"%d{riskscore}"
,
"threatseverity"
:
"%s{threatseverity}"
,
"department"
:
"%s{edepartment}"
,
"urlsupercategory"
:
"%s{urlsupercat}"
,
"appclass"
:
"%s{appclass}"
,
"dlpengine"
:
"%s{dlpeng}"
,
"urlclass"
:
"%s{urlclass}"
,
"threatclass"
:
"%s{malwareclass}"
,
"dlpdictionaries"
:
"%s{dlpdict}"
,
"fileclass"
:
"%s{fileclass}"
,
"bwthrottle"
:
"%s{bwthrottle}"
,
"contenttype"
:
"%s{contenttype}"
,
"unscannabletype"
:
"%s{unscannabletype}"
,
"deviceowner"
:
"%s{deviceowner}"
,
"devicehostname"
:
"%s{devicehostname}"
,
"keyprotectiontype"
:
"%s{keyprotectiontype}"
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
Google SecOps feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Supported Zscaler Webproxy log formats
The Zscaler Webproxy parser supports logs in JSON format.
Supported Zscaler Webproxy Sample Logs
JSON
{
    "event": {
      "ClientIP": "198.51.100.0",
      "action": "Allowed",
      "appclass": "Sales and Marketing",
      "appname": "Trend Micro",
      "bwthrottle": "NO",
      "clientpublicIP": "198.51.100.1",
      "contenttype": "Other",
      "datetime": "2024-05-06 10:56:04",
      "department": "Mid-Continent%20Companies",
      "devicehostname": "dummyhostname",
      "deviceowner": "dummydeviceowner",
      "dlpdictionaries": "None",
      "dlpengine": "None",
      "event_id": "7365838693731467265",
      "fileclass": "None",
      "filetype": "None",
      "hostname": "dummyhostname.com",
      "keyprotectiontype": "N/A",
      "location": "Road%20Warrior",
      "pagerisk": "0",
      "product": "NSS",
      "protocol": "HTTP_PROXY",
      "reason": "Allowed",
      "refererURL": "None",
      "requestmethod": "CONNECT",
      "requestsize": "606",
      "responsesize": "65",
      "serverip": "198.51.10.2",
      "status": "200",
      "threatcategory": "None",
      "threatclass": "None",
      "threatname": "None",
      "threatseverity": "None",
      "transactionsize": "671",
      "unscannabletype": "None",
      "url": "dummyurl.com:443",
      "urlcategory": "SSL - DNI - Bypass",
      "urlclass": "Bandwidth Loss",
      "urlsupercategory": "User-defined",
      "user": "abc@xyz.com",
      "useragent": "dummyuseragent",
      "vendor": "Zscaler"
    },
    "sourcetype": "zscalernss-web"
  }
Field mapping reference
The following table lists the log fields of the
ZSCALER_WEBPROXY
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
metadata.event_type
If the
ClientIP
log field value is
not
empty and the
serverip
log field value is
not
empty and the
proto
log field value contain one of the following values, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
HTTPS
HTTP
Else, if the
ClientIP
log field value is
not
empty and the
serverip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
user
log field value is
not
empty or the
deviceowner
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Web Proxy
.
sourcetype
additional.fields[sourcetype]
datetime
metadata.event_timestamp
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
department
principal.user.department
b64dept
principal.user.department
edepartment
principal.user.department
user
principal.user.email_addresses
user
principal.user.userid
The
EMAILLOCALPART
field is extracted from
user
log field using the Grok pattern, and the
EMAILLOCALPART
log field is mapped to the
principal.user.userid
UDM field.
b64login
principal.user.email_addresses
b64login
principal.user.userid
The
EMAILLOCALPART
field is extracted from
b64login
log field using the Grok pattern, and the
EMAILLOCALPART
log field is mapped to the
principal.user.userid
UDM field.
elogin
principal.user.email_addresses
elogin
principal.user.userid
The
EMAILLOCALPART
field is extracted from
elogin
log field using the Grok pattern, and the
EMAILLOCALPART
log field is mapped to the
principal.user.userid
UDM field.
ologin
principal.user.email_addresses
ologin
principal.user.userid
The
EMAILLOCALPART
field is extracted from
ologin
log field using the Grok pattern, and the
EMAILLOCALPART
log field is mapped to the
principal.user.userid
UDM field.
cloudname
intermediary.resource.attribute.labels[cloudname]
company
principal.user.company_name
throttlereqsize
security_result.detection_fields[throttlereqsize]
throttlerespsize
security_result.detection_fields[throttlerespsize]
bwthrottle
security_result.detection_fields[bwthrottle]
security_result.category
If the
bwthrottle
log field value is equal to
Yes
, then the
security_result.category
UDM field is set to
POLICY_VIOLATION
.
bwclassname
security_result.detection_fields[bwclassname]
obwclassname
security_result.detection_fields[obwclassname]
bwrulename
security_result.rule_name
appname
target.application
appclass
security_result.detection_fields[appclass]
module
security_result.detection_fields[module]
app_risk_score
security_result.risk_score
If the
app_risk_score
log field value matches the regular expression pattern
[0-9]+
, then the
app_risk_score
log field is mapped to the
security_result.risk_score
UDM field.
datacenter
target.location.name
datacentercity
target.location.city
datacentercountry
target.location.country_or_region
dlpdictionaries
security_result.detection_fields[dlpdictionaries]
odlpdict
security_result.detection_fields[odlpdict]
dlpdicthitcount
security_result.detection_fields[dlpdicthitcount]
dlpengine
security_result.detection_fields[dlpengine]
odlpeng
security_result.detection_fields[odlpeng]
dlpidentifier
security_result.detection_fields[dlpidentifier]
dlpmd5
security_result.detection_fields[dlpmd5]
dlprulename
security_result.rule_name
b64dlprulename
security_result.rule_name
odlprulename
security_result.rule_name
fileclass
additional.fields[fileclass]
filetype
target.file.file_type
If the
filetype
log field value matches the regular expression
(?i)(xlsx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XLSX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(xls)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XLS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(cab)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CAB
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pcapng|pcap|cap)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CAP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(tar.gz|egg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYTHON_PKG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(gzip|tgz|gz)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GZIP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(zip)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZIP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(gif)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GIF
.
Else, if the log message matches the regular expression
(?i)(\\bdos\\b)
AND the
filetype
log field value matches the regular expression
(?i)(exe|com)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOS_EXE
.
Else, if the log message matches the regular expression
(?i)(\\bne_exe\\b)
AND the
filetype
log field value matches the regular expression
(?i)(exe)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_NE_EXE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(exe)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PE_EXE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(msi)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MSI
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ocx|sys)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PE_DLL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pdf|(portable\\s*document\\s*format))
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PDF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(docx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOCX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(doc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOC
.
Else, if the
filetype
log field value matches the regular expression
(?i)(html|htm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_HTML
.
Else, if the
filetype
log field value matches the regular expression
(?i)(jar)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAR
.
Else, if the
filetype
log field value matches the regular expression
(?i)(jpeg|jpg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JPEG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(mov)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MOV
.
Else, if the
filetype
log field value matches the regular expression
(?i)(mp3)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MP3
.
Else, if the
filetype
log field value matches the regular expression
(?i)(mp4)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MP4
.
Else, if the
filetype
log field value matches the regular expression
(?i)(png)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PNG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pptx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPTX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ppt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rar)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RAR
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ace)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ACE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(apk|aar|dex)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ANDROID
.
Else, if the
filetype
log field value matches the regular expression
(?i)(plist)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLE_PLIST
.
Else, if the
filetype
log field value matches the regular expression
(?i)(applescript)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLESCRIPT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(app)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(scpt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLESCRIPT_COMPILED
.
Else, if the
filetype
log field value matches the regular expression
(?i)(arc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ARC
.
Else, if the
filetype
log field value matches the regular expression
(?i)(arj)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ARJ
.
Else, if the
filetype
log field value matches the regular expression
(?i)(asd)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ASD
.
Else, if the
filetype
log field value matches the regular expression
(?i)(asf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ASF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(avi)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_AVI
.
Else, if the
filetype
log field value matches the regular expression
(?i)(awk)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_AWK
.
Else, if the
filetype
log field value matches the regular expression
(?i)(bmp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BMP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dib)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DIB
.
Else, if the
filetype
log field value matches the regular expression
(?i)(bz2)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BZIP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(chm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CHM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(cljc|cljs|clj)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CLJ
.
Else, if the
filetype
log field value matches the regular expression
(?i)(crt|cer)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CRT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(crx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CRX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(csv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CSV
.
Else, if the
filetype
log field value matches the regular expression
(?i)(deb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DEB
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dmg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DMG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(divx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DIVX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(com)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOS_COM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dwg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DWG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dxf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DXF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dyalog)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DYALOG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dzip)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DZIP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(epub|mobi|azw)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EBOOK
.
Else, if the
filetype
log field value matches the regular expression
(?i)(elf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ELF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(eml)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EMAIL_TYPE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(emf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EMF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(eot)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EOT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(eps)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EPS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(flac)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLAC
.
Else, if the
filetype
log field value matches the regular expression
(?i)(fla)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLA
.
Else, if the
filetype
log field value matches the regular expression
(?i)(fli)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLI
.
Else, if the
filetype
log field value matches the regular expression
(?i)(flc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLC
.
Else, if the
filetype
log field value matches the regular expression
(?i)(flv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLV
.
Else, if the
filetype
log field value matches the regular expression
(?i)(fpx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FPX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(xcf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GIMP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(go)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GOLANG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(gul)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GUL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(hwp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_HWP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ico)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ICO
.
Else, if the
filetype
log field value matches the regular expression
(?i)(indd|idml)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_IN_DESIGN
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ipa)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_IPHONE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ips)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_IPS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(iso)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ISOIMAGE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(java)
AND the
filetype
log field value does NOT match the regular expression
(?i)(javascript)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAVA
.
Else, if the
filetype
log field value matches the regular expression
(?i)(class)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAVA_BYTECODE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(jmod)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JMOD
.
Else, if the
filetype
log field value matches the regular expression
(?i)(jng)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JNG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(json)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JSON
.
Else, if the
filetype
log field value matches the regular expression
(?i)(js)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAVASCRIPT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(kgb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_KGB
.
Else, if the
filetype
log field value matches the regular expression
(?i)(tex)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LATEX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(lzfse)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LZFSE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(vmlinuz|ko)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LINUX_KERNEL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(bundle|framework)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACH_O
.
Else, if the log message matches the regular expression
(?i)(\\bmach\\b)
AND the
filetype
log field value matches the regular expression
(?i)(dylib|o)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACH_O
.
Else, if the
filetype
log field value matches the regular expression
(?i)(so|initrd|vmlinux|pkg.tar.zst|ext4|ext3|ext2|swap)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LINUX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ini)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_INI
.
Else, if the log message matches the regular expression
(?i)(\\blinux\\b)
AND the
filetype
log field value matches the regular expression
sfs
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LINUX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(lnk)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LNK
.
Else, if the
filetype
log field value matches the regular expression
(?i)(m4)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_M4
.
Else, if the
filetype
log field value matches the regular expression
(?i)(midi|mid)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MIDI
.
Else, if the
filetype
log field value matches the regular expression
(?i)(mkv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MKV
.
Else, if the
filetype
log field value matches the regular expression
(?i)(mpg|mpeg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MPEG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(sz_)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MSCOMPRESS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(dll)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_NE_DLL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(odg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(odp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ods)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(odt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ogg|oga|ogv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OGG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(one)
AND the
filetype
log field value does NOT match the regular expression
(?i)(none)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ONE_NOTE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pst|ost)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OUTLOOK
.
Else, if the log message matches the regular expression
(?i)(\\boutlook\\b)
AND the
filetype
log field value matches the regular expression
(?i)(msg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OUTLOOK
.
Else, if the log message matches the regular expression
(?i)(\\bemail\\b)
AND the
filetype
log field value matches the regular expression
(?i)(msg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EMAIL_TYPE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(prc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PALMOS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pdb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PDB
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pem)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PEM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pgp|gpg|asc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PGP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(php)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PHP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pkg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PKG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ps1|psm1)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_POWERSHELL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ppsx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPSX
.
Else, if the
filetype
log field value matches the regular expression
(?i)(psd)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PSD
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ps)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pyc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYC
.
Else, if the
filetype
log field value matches the regular expression
(?i)(py|pyw)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYTHON
.
Else, if the
filetype
log field value matches the regular expression
(?i)(whl)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYTHON_WHL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(qt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_QUICKTIME
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rm|rmvb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rom|bin)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ROM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rpm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RPM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rtf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RTF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RUBY
.
Else, if the
filetype
log field value matches the regular expression
(?i)(rz)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RZIP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(7z)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SEVENZIP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(sgml|sgm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SGML
.
Else, if the
filetype
log field value matches the regular expression
(?i)(bash|csh|zsh)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SHELLSCRIPT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(sql)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SQL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(sqfs|sfs)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SQUASHFS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(svg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SVG
.
Else, if the
filetype
log field value matches the regular expression
(?i)(swf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SWF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(sis|sisx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SYMBIAN
.
Else, if the
filetype
log field value matches the regular expression
(?i)(3gp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_T3GP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(tar)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TAR
.
Else, if the
filetype
log field value matches the regular expression
(?i)(tga)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TARGA
.
Else, if the
filetype
log field value matches the regular expression
(?i)(3ds|max)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_THREEDS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(tif|tiff)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TIFF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(torrent)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TORRENT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(ttf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TTF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(vba)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_VBA
.
Else, if the
filetype
log field value matches the regular expression
(?i)(vhd|vhdx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_VHD
.
Else, if the
filetype
log field value matches the regular expression
(?i)(wav)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WAV
.
Else, if the
filetype
log field value matches the regular expression
(?i)(webm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WEBM
.
Else, if the
filetype
log field value matches the regular expression
(?i)(webp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WEBP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(wer)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WER
.
Else, if the
filetype
log field value matches the regular expression
(?i)(wma)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WMA
.
Else, if the
filetype
log field value matches the regular expression
(?i)(wmv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WMV
.
Else, if the
filetype
log field value matches the regular expression
(?i)(woff|woff2)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WOFF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(xml)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XML
.
Else, if the
filetype
log field value matches the regular expression
(?i)(xpi)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XPI
.
Else, if the
filetype
log field value matches the regular expression
(?i)(xwd)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XWD
.
Else, if the
filetype
log field value matches the regular expression
(?i)(zst)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZST
.
Else, if the
filetype
log field value matches the regular expression
(?i)(Makefile|makefile|mk)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MAKEFILE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(zlib)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZLIB
.
Else, if the
filetype
log field value matches the regular expression
(?i)(hqx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACINTOSH
.
Else, if the
filetype
log field value matches the regular expression
(?i)(hfs|dsk|toast)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACINTOSH_HFS
.
Else, if the
filetype
log field value matches the regular expression
(?i)(bh|log|dat)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BLACKHOLE
.
Else, if the log message matches the regular expression
(?i)(\\bcookie\\b)
AND the
filetype
log field value matches the regular expression
(?i)(txt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_COOKIE
.
Else, if the
filetype
log field value matches the regular expression
(?i)(txt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TEXT
.
Else, if the
filetype
log field value matches the regular expression
(?i)(docx|xlsx|pptx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OOXML
.
Else, if the
filetype
log field value matches the regular expression
(?i)(odt|ods|odp|odg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODF
.
Else, if the
filetype
log field value matches the regular expression
(?i)(for|f90|f95)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FORTRAN
.
Else, if the log message matches the regular expression
(?i)(\\bwince\\b)
AND the
filetype
log field value matches the regular expression
(?i)(exe|cab|dll)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WINCE
.
Else, if the log message matches the regular expression
(?i)(\\bscript\\b)
AND the
filetype
log field value matches the regular expression
(?i)(py|js|pl|rb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SCRIPT
.
Else, if the log message matches the regular expression
(?i)(\\bapplesingle\\b)
AND the
filetype
log field value matches the regular expression
(?i)(as|bin)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLESINGLE
.
Else, if the log message matches the regular expression
(?i)(\\bmacintosh\\b)
AND the
filetype
log field value matches the regular expression
(?i)(dylib|a)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACINTOSH_LIB
.
Else, if the log message matches the regular expression
(?i)(\\bappledouble\\b)
AND the
filetype
log field value matches the regular expression
(?i)(ad|._)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLEDOUBLE
.
Else, if the log message matches the regular expression
(?i)(\\bobjetivec\\b)
AND the
filetype
log field value matches the regular expression
(?i)(m|mm|h)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OBJETIVEC
.
Else, if the
filetype
log field value matches the regular expression
(?i)(obj|lib)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_COFF
.
Else, if the log message matches the regular expression
(?i)(\\bcpp\\b)
AND the
filetype
log field value matches the regular expression
(?i)(hpp|cpp|cc|cxx|h)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CPP
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pas|pp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PASCAL
.
Else, if the
filetype
log field value matches the regular expression
(?i)(pl|pm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PERL
.
Else, if the
filetype
log field value matches the regular expression
(?i)\\bsh\\b
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SHELLSCRIPT
.
Else, if the
filetype
log field value matches the regular expression
(?i)\\bc\\b$
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_C
.
Else, if the
filetype
log field value matches the regular expression
(?i)\\bn\\b$
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_NEKO
.
Else, if the
filetype
log field value matches the regular expression
(?i)\\bf\\b
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FORTRAN
.
Else, the UDM field
additional.fields.key
is set to
file_type
and the log field value
filetype
is mapped to the
additional.fields.value
UDM field, provided the
filetype
value is not empty.
filename
target.file.full_path
b64filename
target.file.full_path
efilename
target.file.full_path
filesubtype
additional.fields[filesubtype]
upload_fileclass
additional.fields[upload_fileclass]
upload_filetype
target.file.file_type
If the
filetype
log field value is empty or equal to
None
and the
upload_filetype
log field value is
not
empty and
not
equal to
None
, then:
If the
upload_filetype
log field value matches the regular expression
(?i)(xlsx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XLSX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(xls)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XLS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(cab)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CAB
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pcapng|pcap|cap)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CAP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(tar.gz|egg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYTHON_PKG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(gzip|tgz|gz)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GZIP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(zip)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZIP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(gif)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GIF
.
Else, if the log message matches the regular expression
(?i)(\\bdos\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(exe|com)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOS_EXE
.
Else, if the log message matches the regular expression
(?i)(\\bne_exe\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(exe)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_NE_EXE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(exe)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PE_EXE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(msi)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MSI
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ocx|sys)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PE_DLL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pdf|(portable\\s*document\\s*format))
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PDF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(docx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOCX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(doc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOC
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(html|htm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_HTML
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(jar)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAR
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(jpeg|jpg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JPEG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(mov)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MOV
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(mp3)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MP3
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(mp4)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MP4
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(png)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PNG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pptx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPTX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ppt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rar)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RAR
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ace)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ACE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(apk|aar|dex)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ANDROID
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(plist)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLE_PLIST
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(applescript)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLESCRIPT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(app)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(scpt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLESCRIPT_COMPILED
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(arc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ARC
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(arj)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ARJ
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(asd)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ASD
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(asf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ASF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(avi)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_AVI
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(awk)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_AWK
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(bmp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BMP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dib)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DIB
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(bz2)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BZIP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(chm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CHM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(cljc|cljs|clj)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CLJ
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(crt|cer)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CRT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(crx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CRX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(csv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CSV
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(deb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DEB
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dmg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DMG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(divx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DIVX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(com)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DOS_COM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dwg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DWG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dxf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DXF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dyalog)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DYALOG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dzip)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_DZIP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(epub|mobi|azw)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EBOOK
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(elf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ELF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(eml)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EMAIL_TYPE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(emf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EMF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(eot)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EOT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(eps)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EPS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(flac)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLAC
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(fla)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLA
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(fli)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLI
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(flc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLC
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(flv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FLV
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(fpx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FPX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(xcf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GIMP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(go)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GOLANG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(gul)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_GUL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(hwp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_HWP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ico)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ICO
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(indd|idml)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_IN_DESIGN
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ipa)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_IPHONE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ips)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_IPS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(iso)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ISOIMAGE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(java)
AND the
upload_filetype
log field value does NOT match the regular expression
(?i)(javascript)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAVA
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(class)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAVA_BYTECODE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(jmod)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JMOD
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(jng)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JNG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(json)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JSON
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(js)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_JAVASCRIPT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(kgb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_KGB
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(tex)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LATEX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(lzfse)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LZFSE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(vmlinuz|ko)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LINUX_KERNEL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(bundle|framework)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACH_O
.
Else, if the log message matches the regular expression
(?i)(\\bmach\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(dylib|o)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACH_O
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(so|initrd|vmlinux|pkg.tar.zst|ext4|ext3|ext2|swap)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LINUX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ini)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_INI
.
Else, if the log message matches the regular expression
(?i)(\\blinux\\b)
AND the
upload_filetype
log field value matches the regular expression
sfs
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LINUX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(lnk)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_LNK
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(m4)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_M4
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(midi|mid)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MIDI
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(mkv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MKV
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(mpg|mpeg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MPEG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(sz_)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MSCOMPRESS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(dll)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_NE_DLL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(odg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(odp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ods)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(odt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ogg|oga|ogv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OGG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(one)
AND the
upload_filetype
log field value does NOT match the regular expression
(?i)(none)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ONE_NOTE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pst|ost)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OUTLOOK
.
Else, if the log message matches the regular expression
(?i)(\\boutlook\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(msg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OUTLOOK
.
Else, if the log message matches the regular expression
(?i)(\\bemail\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(msg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_EMAIL_TYPE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(prc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PALMOS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pdb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PDB
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pem)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PEM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pgp|gpg|asc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PGP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(php)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PHP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pkg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PKG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ps1|psm1)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_POWERSHELL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ppsx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPSX
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(psd)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PSD
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ps)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pyc)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYC
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(py|pyw)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYTHON
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(whl)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PYTHON_WHL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(qt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_QUICKTIME
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rm|rmvb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rom|bin)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ROM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rpm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RPM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rtf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RTF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RUBY
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(rz)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_RZIP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(7z)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SEVENZIP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(sgml|sgm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SGML
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(bash|csh|zsh)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SHELLSCRIPT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(sql)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SQL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(sqfs|sfs)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SQUASHFS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(svg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SVG
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(swf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SWF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(sis|sisx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SYMBIAN
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(3gp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_T3GP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(tar)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TAR
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(tga)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TARGA
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(3ds|max)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_THREEDS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(tif|tiff)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TIFF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(torrent)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TORRENT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(ttf)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TTF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(vba)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_VBA
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(vhd|vhdx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_VHD
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(wav)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WAV
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(webm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WEBM
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(webp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WEBP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(wer)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WER
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(wma)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WMA
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(wmv)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WMV
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(woff|woff2)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WOFF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(xml)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XML
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(xpi)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XPI
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(xwd)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_XWD
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(zst)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZST
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(Makefile|makefile|mk)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MAKEFILE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(zlib)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ZLIB
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(hqx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACINTOSH
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(hfs|dsk|toast)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACINTOSH_HFS
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(bh|log|dat)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_BLACKHOLE
.
Else, if the log message matches the regular expression
(?i)(\\bcookie\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(txt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_COOKIE
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(txt)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_TEXT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(docx|xlsx|pptx)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OOXML
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(odt|ods|odp|odg)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_ODF
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(for|f90|f95)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FORTRAN
.
Else, if the log message matches the regular expression
(?i)(\\bwince\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(exe|cab|dll)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_WINCE
.
Else, if the log message matches the regular expression
(?i)(\\bscript\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(py|js|pl|rb)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SCRIPT
.
Else, if the log message matches the regular expression
(?i)(\\bapplesingle\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(as|bin)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLESINGLE
.
Else, if the log message matches the regular expression
(?i)(\\bmacintosh\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(dylib|a)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_MACINTOSH_LIB
.
Else, if the log message matches the regular expression
(?i)(\\bappledouble\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(ad|._)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_APPLEDOUBLE
.
Else, if the log message matches the regular expression
(?i)(\\bobjetivec\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(m|mm|h)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_OBJETIVEC
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(obj|lib)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_COFF
.
Else, if the log message matches the regular expression
(?i)(\\bcpp\\b)
AND the
upload_filetype
log field value matches the regular expression
(?i)(hpp|cpp|cc|cxx|h)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_CPP
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pas|pp)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PASCAL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)(pl|pm)
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PERL
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)\\bsh\\b
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_SHELLSCRIPT
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)\\bc\\b$
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_C
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)\\bn\\b$
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_NEKO
.
Else, if the
upload_filetype
log field value matches the regular expression
(?i)\\bf\\b
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_FORTRAN
.
Else, the UDM field
additional.fields.key
is set to
file_type
and the log field value
upload_filetype
is mapped to the
additional.fields.value
UDM field, provided the
upload_filetype
value is not empty.
upload_filename
target.file.full_path
If the
filename
log field value is equal to
None
and the
upload_filename
log field value is
not
equal to
None
, then the
upload_filename
log field is mapped to the
target.file.full_path
UDM field.
Else, if the
filename
log field value is not equal to
None
and the
upload_filename
log field value is
not
equal to
None
, then the
upload_filename
log field is mapped to the
target.resource.attribute.labels[upload_filename]
UDM field.
b64upload_filename
target.file.full_path
If the
filename
log field value is equal to
None
and the
b64upload_filename
log field value is
not
equal to
None
, then the
b64upload_filename
log field is mapped to the
target.file.full_path
UDM field.
Else, if the
filename
log field value is not equal to
None
and the
b64upload_filename
log field value is
not
equal to
None
, then the
b64upload_filename
log field is mapped to the
target.resource.attribute.labels[upload_filename]
UDM field.
eupload_filename
target.file.full_path
If the
filename
log field value is equal to
None
and the
eupload_filename
log field value is
not
equal to
None
, then the
eupload_filename
log field is mapped to the
target.file.full_path
UDM field.
Else, if the
filename
log field value is not equal to
None
and the
eupload_filename
log field value is
not
equal to
None
, then the
eupload_filename
log field is mapped to the
target.resource.attribute.labels[upload_filename]
UDM field.
upload_filesubtype
additional.fields[upload_filesubtype]
upload_doctypename
additional.fields[upload_doctypename]
unscannabletype
security_result.detection_fields[unscannabletype]
rdr_rulename
security_result.rule_name
b64rdr_rulename
security_result.rule_name
ordr_rulename
security_result.rule_name
fwd_type
intermediary.resource.attribute.labels[fwd_type]
fwd_gw_name
intermediary.resource.name
b64fwd_gw_name
intermediary.resource.name
ofwd_gw_name
intermediary.resource.name
fwd_gw_ip
intermediary.ip
zpa_app_seg_name
additional.fields[zpa_app_seg_name]
b64zpa_app_seg_name
additional.fields[zpa_app_seg_name]
ozpa_app_seg_name
additional.fields[ozpa_app_seg_name]
reqdatasize
additional.fields[reqdatasize]
reqhdrsize
additional.fields[reqhdrsize]
requestsize
network.sent_bytes
respdatasize
additional.fields[respdatasize]
resphdrsize
additional.fields[resphdrsize]
responsesize
network.received_bytes
transactionsize
additional.fields[transactionsize]
contenttype
target.file.mime_type
df_hosthead
security_result.detection_fields[df_hosthead]
df_hostname
security_result.detection_fields[df_hostname]
hostname
target.hostnametarget.asset.hostname
b64host
target.hostnametarget.asset.hostname
ehost
target.hostnametarget.asset.hostname
refererURL
network.http.referral_url
b64referer
network.http.referral_url
ereferer
network.http.referral_url
erefererpath
additional.fields[erefererpath]
refererhost
additional.fields[refererhost]
erefererhost
additional.fields[refererhost]
requestmethod
network.http.method
reqversion
additional.fields[reqversion]
status
network.http.response_code
respversion
additional.fields[respversion]
ua_token
additional.fields[ua_token]
useragent
network.http.user_agent
b64ua
network.http.user_agent
eua
network.http.user_agent
useragent
network.http.parsed_user_agent
b64ua
network.http.parsed_user_agent
eua
network.http.parsed_user_agent
uaclass
additional.fields[uaclass]
url
target.url
b64url
target.url
eurl
target.url
eurlpath
additional.fields[eurlpath]
mobappname
additional.fields[mobappname]
b64mobappname
additional.fields[mobappname]
emobappname
additional.fields[mobappname]
mobappcat
security_result.detection_fields[mobappcat]
mobdevtype
security_result.detection_fields[mobdevtype]
clt_sport
principal.port
ClientIP
principal.ip
ocip
principal.ip
cpubip
principal.ip
ocpubip
principal.ip
clientpublicIP
principal.nat_ip
serverip
target.ip
network.application_protocol
If the
protocol
log field value contain one of the following values, then the
network.application_protocol
UDM field is set to
HTTP
.
HTTP
HTTP_PROXY
Else, if the
protocol
log field value contain one of the following values, then the
network.application_protocol
UDM field is set to
HTTPS
.
HTTPS
SSL
TUNNEL_SSL
DNSOVERHTTPS
TUNNEL
Else, the
network.application_protocol
UDM field is set to
UNKNOWN_APPLICATION_PROTOCOL
.
alpnprotocol
additional.fields[alpnprotocol]
trafficredirectmethod
intermediary.resource.attribute.labels[trafficredirectmethod]
location
principal.location.name
elocation
principal.location.name
userlocationname
principal.location.name
If the
userlocationname
log field value is
not
equal to
None
, then the
userlocationname
log field is mapped to the
principal.location.name
UDM field.
b64userlocationname
principal.location.name
euserlocationname
principal.location.name
rulelabel
security_result.rule_name
If the
action
log field value is equal to
Blocked
, then the
rulelabel
log field is mapped to the
security_result.rule_name
UDM field.
b64rulelabel
security_result.rule_name
erulelabel
security_result.rule_name
ruletype
security_result.rule_type
reason
security_result.description
If the
action
log field value is equal to
Blocked
, then the
reason
log field is mapped to the
security_result.description
UDM field.
action
security_result.action_details
security_result.action
If the
action
log field value is equal to
Allowed
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value is equal to
Blocked
, then the
security_result.action
UDM field is set to
BLOCK
.
urlfilterrulelabel
security_result.rule_name
b64urlfilterrulelabel
security_result.rule_name
eurlfilterrulelabel
security_result.rule_name
ourlfilterrulelabel
security_result.rule_name
apprulelabel
security_result.rule_name
eapprulelabel
security_result.rule_name
b64apprulelabel
security_result.rule_name
oapprulelabel
security_result.rule_name
bamd5
target.file.md5
sha256
target.file.sha256
ssldecrypted
security_result.detection_fields[ssldecrypted]
externalspr
security_result.detection_fields[externalspr]
keyprotectiontype
security_result.detection_fields[keyprotectiontype]
clientsslcipher
network.tls.client.supported_ciphers
clienttlsversion
network.tls.version
clientsslsessreuse
security_result.detection_fields[clientsslsessreuse]
cltsslfailreason
security_result.summary
cltsslfailcount
security_result.detection_fields[cltsslfailcount]
srvsslcipher
network.tls.cipher
srvtlsversion
security_result.detection_fields[srvtlsversion]
srvocspresult
security_result.detection_fields[srvocspresult]
srvcertchainvalpass
security_result.detection_fields[srvcertchainvalpass]
srvwildcardcert
security_result.detection_fields[srvwildcardcert]
serversslsessreuse
security_result.detection_fields[server_ssl_sess_reuse]
srvcertvalidationtype
security_result.detection_fields[srvcertvalidationtype]
srvcertvalidityperiod
security_result.detection_fields[srvcertvalidityperiod]
is_ssluntrustedca
security_result.detection_fields[is_ssluntrustedca]
is_sslselfsigned
security_result.detection_fields[is_sslselfsigned]
is_sslexpiredca
security_result.detection_fields[is_sslexpiredca]
pagerisk
security_result.risk_score
security_result.severity
If the
pagerisk
log field value is greater than or equal to
90
and the
pagerisk
log field value is less than or equal to
100
, then the
security_result.severity
UDM field is set to
CRITICAL
.
If the
pagerisk
log field value is greater than or equal to
75
and the
pagerisk
log field value is less than or equal to
89
, then the
security_result.severity
UDM field is set to
HIGH
.
If the
pagerisk
log field value is greater than or equal to
46
and the
pagerisk
log field value is less than or equal to
74
, then the
security_result.severity
UDM field is set to
MEDIUM
.
If the
pagerisk
log field value is greater than or equal to
1
and the
pagerisk
log field value &is less than or equal to
45
, then the
security_result.severity
UDM field is set to
LOW
.
If the
pagerisk
log field value is equal to
0
, then the
security_result.severity
UDM field is set to
NONE
.
threatseverity
security_result.severity_details
If the
pagerisk
log field value is
not
empty and the
threatseverity
log field value is
not
empty, then the
security_result.severity_details
UDM field is set to
%{pagerisk} - %{threatseverity}
.
Else, if the
threatseverity
log field value is
not
empty, then the
threatseverity
log field is mapped to the
security_result.severity_details
UDM field.
activity
metadata.product_event_type
is_dst_cntry_risky
security_result.detection_fields[is_dst_cntry_risky]
is_src_cntry_risky
security_result.detection_fields[is_src_cntry_risky]
prompt_req
additional.fields[prompt_req]
srcip_country
principal.ip_geo_artifact.location.country_or_region
pcapid
security_result.about.file.full_path
all_dlprulenames
security_result.rule_labels[all_dlprulenames]
other_dlprulenames
security_result.rule_labels[other_dlprulenames]
trig_dlprulename
security_result.rule_name
dstip_country
target.ip_geo_artifact.location.country_or_region
srv_dport
target.port
inst_level2_name
target.resource_ancestors.name
inst_level3_name
target.resource_ancestors.name
inst_level2_id
target.resource_ancestors.product_object_id
inst_level3_id
target.resource_ancestors.product_object_id
inst_level2_type
target.resource_ancestors.resource_subtype
inst_level3_type
target.resource_ancestors.resource_subtype
target.resource_ancestors.resource_type
If the
inst_level2_type
log field value matches the regular expression pattern
organization
then, the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
service
then, the
target.resource_ancestors.resource_type
UDM field is set to
BACKEND_SERVICE
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
policy
then, the
target.resource_ancestors.resource_type
UDM field is set to
ACCESS_POLICY
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
project
then, the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
cluster
then, the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
container
then, the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
pod
then, the
target.resource_ancestors.resource_type
UDM field is set to
POD
.
Else, if
inst_level2_type
log field value matches the regular expression pattern
repository
then, the
target.resource_ancestors.resource_type
UDM field is set to
REPOSITORY
.
If the
inst_level3_type
log field value matches the regular expression pattern
organization
then, the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
service
then, the
target.resource_ancestors.resource_type
UDM field is set to
BACKEND_SERVICE
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
policy
then, the
target.resource_ancestors.resource_type
UDM field is set to
ACCESS_POLICY
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
project
then, the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
cluster
then, the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
container
then, the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
pod
then, the
target.resource_ancestors.resource_type
UDM field is set to
POD
.
Else, if
inst_level3_type
log field value matches the regular expression pattern
repository
then, the
target.resource_ancestors.resource_type
UDM field is set to
REPOSITORY
.
inst_level1_name
target.resource.name
inst_level1_id
target.resource.product_object_id
inst_level1_type
target.resource.resource_subtype
target.resource.resource_type
If the
inst_level1_type
log field value matches the regular expression pattern
organization
then, the
target.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
service
then, the
target.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
policy
then, the
target.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
project
then, the
target.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
cluster
then, the
target.resource.resource_type
UDM field is set to
CLUSTER
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
container
then, the
target.resource.resource_type
UDM field is set to
CONTAINER
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
pod
then, the
target.resource.resource_type
UDM field is set to
POD
.
Else, if
inst_level1_type
log field value matches the regular expression pattern
repository
then, the
target.resource.resource_type
UDM field is set to
REPOSITORY
.
app_status
security_result.detection_fields[app_status]
threatname
security_result.threat_name
b64threatname
security_result.threat_name
threatcategory
security_result.associations.name
threatclass
security_result.associations.description
urlclass
security_result.detection_fields[urlclass]
urlsupercategory
security_result.category_details
urlcategory
security_result.category_details
b64urlcat
security_result.category_details
ourlcat
security_result.category_details
urlcatmethod
security_result.detection_fields[urlcatmethod]
bypassed_traffic
security_result.detection_fields[bypassed_traffic]
bypassed_etime
security_result.detection_fields[bypassed_etime]
deviceappversion
principal.asset.platform_software.platform_version
devicehostname
principal.asset.hostname
edevicehostname
principal.asset.hostname
odevicehostname
principal.asset.hostname
devicemodel
principal.asset.hardware.model
devicename
principal.asset.asset_id
edevicename
principal.asset.asset_id
odevicename
principal.asset.asset_id
principal.asset.platform_software.platform
If the
deviceostype
log field value matches the regular expression pattern
(?i)iOS
, then the
principal.asset.platform_software.platform
UDM field is set to
IOS
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)Android
, then the
principal.asset.platform_software.platform
UDM field is set to
ANDROID
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)Windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)MAC
, then the
principal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)Other
, then the
principal.asset.platform_software.platform
UDM field is set to
UNKNOWN_PLATFORM
.
deviceosversion
principal.asset.software.version
deviceowner
principal.asset.attribute.labels[deviceowner]
odeviceowner
principal.asset.attribute.labels[deviceowner]
devicetype
principal.asset.category
external_devid
additional.fields[external_devid]
flow_type
additional.fields[flow_type]
ztunnelversion
additional.fields[ztunnelversion]
event_id
metadata.product_log_id
productversion
metadata.product_version
nsssvcip
about.ip
eedone
additional.fields[eedone]
ssl_rulename
security_result.rule_name
client_tls_keyex_pqc_offers
additional.fields[client_tls_keyex_pqc_offers]
client_tls_keyex_hybrid_offers
additional.fields[client_tls_keyex_hybrid_offers]
client_tls_keyex_unknown_offers
additional.fields[client_tls_keyex_unknown_offers]
client_tls_sig_pqc_offers
additional.fields[client_tls_sig_pqc_offers]
client_tls_sig_non_pqc_offers
additional.fields[client_tls_sig_non_pqc_offers]
client_tls_sig_hybrid_offers
additional.fields[client_tls_sig_hybrid_offers]
client_tls_sig_unknown_offers
additional.fields[client_tls_sig_unknown_offers]
client_tls_keyex_alg
additional.fields[client_tls_keyex_alg]
client_tls_sig_alg
additional.fields[client_tls_sig_alg]
server_tls_keyex_alg
additional.fields[server_tls_keyex_alg]
server_tls_sig_alg
additional.fields[server_tls_sig_alg]
time
additional.fields[time]
ft_rulename
security_result.rule_name
upload_doc_sub_type
additional.fields[upload_doc_sub_type]
client_tls_keyex_non_pqc_offers
additional.fields[client_tls_keyex_non_pqc_offers]
Need more help?
Get answers from Community members and Google SecOps professionals.
