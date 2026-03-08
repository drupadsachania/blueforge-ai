# Collect Zscaler CASB logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb/  
**Scraped:** 2026-03-05T09:18:09.255816Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler CASB logs
This document describes how you can export Zscaler CASB logs by setting up a Google Security Operations feed and mapping log fields to the Unified Data Model (UDM).
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler CASB and a Google SecOps Webhook feed configured to send logs to Google SecOps. However, deployment details can differ by customer and could be more complex.
The deployment contains the following components:
Zscaler CASB
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler CASB and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser that normalizes raw log data into the structured UDM format. This document applies specifically to the parser associated with the ZSCALER_CASB ingestion label.
Before you begin
Ensure that you have access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Ensure that you're using Zscaler CASB version 1.0 or 2.0.
Ensure that all systems in the deployment architecture are configured with the UTC time zone.
Ensure that you have the API key required to complete feed setup in Google SecOps. For more information, see
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
Set up Zscaler CASB
In the Zscaler Internet Access Console, click
Administration
>
Nanolog Streaming Service
>
Cloud NSS Feeds
>
Add Cloud NSS Feed
.
In the
Add Cloud NSS Feed window
, enter the details.
In the
Feed Name
field, enter a unique name for the feed.
Select
Zscaler for Web
in
NSS Type
.
In the
Status
list, select a status to activate or deactivate the NSS feed.
Leave
SIEM Rate
as
Unlimited
, unless you need to throttle the output stream due to licensing or other constraints.
In the
SIEM Type
list, select
Other
.
In the
OAuth 2.0 Authentication
list, select
Disabled
.
In the
Max Batch Size
field, enter a size limit for an individual HTTP request payload to the SIEM's best practice; for example,
512 KB
.
In the
API URL
field, enter the HTTPS URL of the Chronicle API endpoint using the following format:
https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
CHRONICLE_REGION
: Region where your Google SecOps instance is hosted. For example,
US
.
GOOGLE_PROJECT_NUMBER
: Your BYOP project number. Obtain this from C4.
LOCATION
: Chronicle (Google SecOps) region (same as
CHRONICLE_REGION
). For example,
US
.
CUSTOMER_ID
: Your Google SecOps customer ID. Obtain from C4.
FEED_ID
: ID of the newly created webhook feed (shown in the Feed UI).
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
API Key generated from Google Cloud BYOP's API Credentials.
Header 2
:
Key2:
X-Webhook-Access-Key
and
Value2:
API secret key generated in webhook's "SECRET KEY".
In the
Log Types
list, select
SaaS Security
or
SaaS Security Activity
.
In the
Feed Output Type
list, select
JSON
.
Disable
JSON Array Notation
.
Set
Feed Escape Character
to
, \ "
.
In the
Feed Output Type
list, select
Custom
to add a new field to the
Feed Output Format
.
Copy and paste the
Feed Output Format
, and then add new fields, as needed. Ensure the key names match the actual field names.
Following are the default
Feed Output Formats
:
SaaS Security
\
{
"sourcetype"
:
"zscalernss-casb"
,
"event"
:
\
{
"datetime"
:
"
%s
{time}"
,
"recordid"
:
"
%d
{recordid}"
,
"company"
:
"
%s
{company}"
,
"tenant"
:
"
%s
{tenant}"
,
"login"
:
"
%s
{user}"
,
"dept"
:
"
%s
{department}"
,
"applicationname"
:
"
%s
{applicationname}"
,
"filename"
:
"
%s
{filename}"
,
"filesource"
:
"
%s
{filesource}"
,
"filemd5"
:
"
%s
{filemd5}"
,
"threatname"
:
"
%s
{threatname}"
,
"policy"
:
"
%s
{policy}"
,
"dlpdictnames"
:
"
%s
{dlpdictnames}"
,
"dlpdictcount"
:
"
%s
{dlpdictcount}"
,
"dlpenginenames"
:
"
%s
{dlpenginenames}"
,
"fullurl"
:
"
%s
{fullurl}"
,
"lastmodtime"
:
"
%s
{lastmodtime}"
,
"filescantimems"
:
"
%d
{filescantimems}"
,
"filedownloadtimems"
:
"
%d
{filedownloadtimems}"
\
}
\
}
SaaS Security Activity
\
{
"sourcetype"
:
"zscalernss-casb"
,
"event"
:
\
{
"login"
:
"%s{username}"
,
"tenant"
:
"%s{tenant}"
,
"object_type"
:
"%d{objtype1}"
,
"applicationname"
:
"%s{appname}"
,
"object_name_1"
:
"%s{objnames1}"
,
"object_name_2"
:
"%s{objnames2}"
\
}
\
}
From the
Timezone
list, select the time zone for the
Time
field in 
the output file. By default, the time zone is set to your organization's time 
zone.
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
Field mapping reference
Field mapping reference: ZSCALER_CASB
The following table lists the log fields of the
ZSCALER_CASB
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
sourcetype
additional.fields[sourcetype]
objnames2
about.resource.name
object_name_2
about.resource.name
objtypename2
about.resource.resource_subtype
externalownername
additional.fields[externalownername]
act_cnt
additional.fields[act_cnt]
attchcomponentfiletypes
additional.fields[attchcomponentfiletypes]
channel_name
additional.fields[channel_name]
collabscope
additional.fields[collabscope]
day
additional.fields[day]
dd
additional.fields[dd]
dlpdictcount
security_result.detection_fields[dlpdictcount]
If the
dlpdictcount
log field value is
not
empty and the
dlpdictcount
log field value is not equal to
None
, then the
dlpdictcount
log field is mapped to the
security_result.detection_fields.dlpdictcount
UDM field.
dlpenginenames
security_result.detection_fields[dlpenginenames]
If the
dlpenginenames
log field value is
not
empty and the
dlpenginenames
log field value is not equal to
None
, then the
dlpenginenames
log field is mapped to the
security_result.detection_fields.dlpenginenames
UDM field.
epochlastmodtime
additional.fields[epochlastmodtime]
extcollabnames
additional.fields[extcollabnames]
extownername
additional.fields[extownername]
file_msg_id
additional.fields[file_msg_id]
fileid
additional.fields[fileid]
filescantimems
additional.fields[filescantimems]
filetypecategory
additional.fields[filetypecategory]
hh
additional.fields[hh]
messageid
additional.fields[messageid]
mm
additional.fields[mm]
mon
additional.fields[mon]
msgsize
additional.fields[msgsize]
mth
additional.fields[mth]
num_ext_recpts
additional.fields[num_ext_recpts]
num_int_recpts
additional.fields[num_int_recpts]
numcollab
additional.fields[numcollab]
rtime
additional.fields[rtime]
ss
additional.fields[ss]
suburl
additional.fields[suburl]
tenant
additional.fields[tenant]
tz
additional.fields[tz]
upload_doctypename
additional.fields[upload_doctypename]
yyyy
additional.fields[yyyy]
collabnames
additional.fields[collabnames]
companyid
additional.fields[companyid]
component
additional.fields[component]
intcollabnames
additional.fields[intcollabnames]
If
intcollabnames
log field value does not match the regular expression pattern
None
then, for
index
in
intcollabnames
, the
index
is mapped to the
additional.fields.value.list_value
UDM field.
internal_collabnames
additional.fields[internal_collabnames]
external_collabnames
additional.fields[external_collabnames]
num_external_collab
additional.fields[num_external_collab]
num_internal_collab
additional.fields[num_internal_collab]
repochtime
additional.fields[repochtime]
eventtime
metadata.event_timestamp
If the
eventtime
log field value is
not
empty, then the
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
epochtime
metadata.event_timestamp
If the
epochtime
log field value is
not
empty, then the
epochtime
log field is mapped to the
metadata.event_timestamp
UDM field.
time
metadata.event_timestamp
If the
time
log field value is
not
empty, then the
time
log field is mapped to the
metadata.event_timestamp
UDM field.
datetime
metadata.event_timestamp
If the
datetime
log field value is
not
empty, then the
datetime
log field is mapped to the
metadata.event_timestamp
UDM field.
metadata.event_type
If
principal.ip
is not empty or
principal.hostname
is not empty, and
target.ip
is not empty, then
metadata.event_type
is set to
NETWORK_CONNECTION
.
Else if any of the following UDM fields are empty:
principal.user.userid
,
principal.user.email_addresses
,
principal.hostname
,
principal.asset_id
,
principal.ip
,
principal.mac
,
target.hostname
,
target.asset_id
,
target.ip
,
target.mac
,
target.user.email_addresses
,
target.user.userid
, then
metadata.event_type
is set to
USER_UNCATEGORIZED
.
Else if any of the following UDM fields are empty:
principal.hostname
,
principal.asset_id
,
principal.ip
,
principal.mac
, then
metadata.event_type
is set to
STATUS_UPDATE
.
act_type_name
metadata.product_event_type
recordid
metadata.product_log_id
metadata.product_name
The
metadata.product_name
UDM field is set to
CASB
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
sender
network.email.from
If the
sender
log field value matches the regular expression pattern
(^.*@.*$)
, then the
sender
log field is mapped to the
network.email.from
UDM field.
extrecptnames
network.email.to
For
index
in
extrecptnames
, the
index
is mapped to the
network.email.to
UDM field.
internal_recptnames
network.email.to
For
index
in
internal_recptnames
, the
index
is mapped to the
network.email.to
UDM field.
external_recptnames
network.email.to
For
index
in
external_recptnames
, the
index
is mapped to the
network.email.to
UDM field.
intrecptnames
network.email.to
For
index
in
intrecptnames
, the
index
is mapped to the
network.email.to
UDM field.
applicationname
principal.application
If the
applicationname
log field value is
not
empty, then the
applicationname
log field is mapped to the
principal.application
UDM field.
Else, the
appname
log field is mapped to the
principal.application
UDM field.
appname
principal.application
If the
applicationname
log field value is
not
empty, then the
applicationname
log field is mapped to the
principal.application
UDM field.
Else, the
appname
log field is mapped to the
principal.application
UDM field.
src_ip
principal.ip
fullurl
principal.url
If the
fullurl
log field is
not
empty and the
fullurl
log field value is not equal to
Unknown URL
, then the
fullurl
log field is mapped to the
principal.url
UDM field.
is_admin_act
principal.user.attribute.labels[is_admin_act]
principal.user.attribute.roles.type
If the
is_admin_act
log field value is equal to
1
, then the
principal.user.attribute.roles.type
UDM field is set to
ADMINISTRATOR
.
company
principal.user.company_name
department
principal.user.department
If the
dept
log field value is
not
empty, then the
dept
log field is mapped to the
principal.user.department
UDM field. Else, the
department
log field is mapped to the
principal.user.department
UDM field.
dept
principal.user.department
If the
dept
log field value is
not
empty, then the
dept
log field is mapped to the
principal.user.department
UDM field. Else, the
department
log field is mapped to the
principal.user.department
UDM field.
user
principal.user.email_addresses
If the
user
log field value matches the regular expression pattern
(^.*@.*$)
, then the
user
log field is mapped to the
principal.user.email_addresses
UDM field.
username
principal.user.email_addresses
If the
username
log field value matches the regular expression pattern
(^.*@.*$)
, then the
username
log field is mapped to the
principal.user.email_addresses
UDM field.
owner
principal.user.email_addresses
If the
owner
log field value matches the regular expression pattern
(^.*@.*$)
, then the
owner
log field is mapped to the
principal.user.email_addresses
UDM field.
login
principal.user.email_addresses
If the
login
log field value matches the regular expression pattern
(^.*@.*$)
, then the
login
log field is mapped to the
principal.user.email_addresses
UDM field.
login
principal.user.userid
If the
login
log field value does not match the regular expression pattern
^.+@.+$
, then the
login
log field is mapped to the
principal.user.userid
UDM field.
malware
security_result.associations.name
security_result.associations.type
If the
malware
log field value is
not
empty, then the
security_result.associations.type
UDM field is set to
MALWARE
.
dlpdictnames
security_result.detection_fields[dlpdictnames]
dlpidentifier
security_result.detection_fields[dlpidentifier]
filedownloadtimems
additional.fields[filedownloadtimems]
malwareclass
security_result.threat_name
msgid
additional.fields[msgid]
oattchcomponentfilenames
target.file.names
obucketname
target.resource.name
obucketowner
target.resource.attribute.labels[obucketowner]
ochannel_name
additional.fields[ochannel_name]
ocollabnames
additional.fields[ocollabnames]
odlpdictnames
security_result.detection_fields[odlpdictnames]
odlpenginenames
security_result.detection_fields[odlpenginenames]
oextcollabnames
additional.fields[oextcollabnames]
oexternal_collabnames
additional.fields[oexternal_collabnames]
oexternal_recptnames
network.email.to
oexternalownername
additional.fields[oexternalownername]
oextownername
additional.fields[oextownername]
oextrecptnames
network.email.to
ofile_msg_id
additional.fields[ofile_msg_id]
ofileid
additional.fields[ofileid]
ofullurl
principal.url
If the
ofullurl
log field is
not
empty and the
ofullurl
log field value is not equal to
Unknown URL
, then the
ofullurl
log field is mapped to the
principal.url
UDM field.
ohostname
target.hostname
ointcollabnames
additional.fields[ointcollabnames]
ointernal_collabnames
additional.fields[ointernal_collabnames]
ointernal_recptnames
network.email.to
ointrecptnames
network.email.to
omessageid
additional.fields[omessageid]
omsgid
additional.fields[omsgid]
oowner
principal.user.email_addresses
If the
oowner
log field value matches the regular expression pattern
(^.*@.*$)
, then the
oowner
log field is mapped to the
principal.user.email_addresses
UDM field.
orulelabel
security_result.rule_name
osender
network.email.from
If the
osender
log field value matches the regular expression pattern
(^.*@.*$)
, then the
osender
log field is mapped to the
network.email.from
UDM field.
osharedchannel_hostname
target.hostname
otenant
additional.fields[otenant]
ouser
principal.user.email_addresses
If the
ouser
log field value matches the regular expression pattern
(^.*@.*$)
, then the
ouser
log field is mapped to the
principal.user.email_addresses
UDM field.
any_incident
security_result.detection_fields[any_incident]
is_inbound
security_result.detection_fields[is_inbound]
policy
security_result.rule_labels[policy]
ruletype
security_result.rule_labels[ruletype]
rulelabel
security_result.rule_name
security_result.severity
If the
severity
log field value is equal to
High
, then the
security_result.severity
UDM field is set to
HIGH
.
Else, if the
severity
log field value is equal to
Medium
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value is equal to
Low
, then the
security_result.sevrity
UDM field is set to
LOW
.
Else, if the
severity
log field value is equal to
Information
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
threatname
security_result.threat_name
If the
threatname
log field value is
not
empty and the
dlpdictcount
log field value is not equal to
None
, then the
threatname
log field is mapped to the
security_result.threat_name
UDM field.
filesource
target.file.full_path
If
filepath
is not empty, then the
filepath
log field is mapped to the
target.file.full_path
UDM field. Else if
filesource
is not empty, then the
filesource
log field is mapped to the
target.file.full_path
UDM field.
filepath
target.file.full_path
If
filepath
is not empty, then the
filepath
log field is mapped to the
target.file.full_path
UDM field. Else if
filesource
is not empty, then the
filesource
log field is mapped to the
target.file.full_path
UDM field.
lastmodtime
If the
file_msg_mod_time
log field value is
not
empty, then the
file_msg_mod_time
log field is mapped to the
target.file.last_modification_time
UDM field.
Else if the
lastmodtime
log field value is
not
empty, then the
lastmodtime
log field is mapped to the
target.file.last_modification_time
UDM field.
file_msg_mod_time
target.file.last_modification_time
If the
file_msg_mod_time
log field value is
not
empty, then the
file_msg_mod_time
log field is mapped to the
target.file.last_modification_time
UDM field.
Else if the
lastmodtime
log field value is
not
empty, then the
lastmodtime
log field is mapped to the
target.file.last_modification_time
UDM field.
filemd5
target.file.md5
If the
attchcomponentmd5s
log field value is
not
equal to empty and the
attchcomponentmd5s
log field value matches the regular expression pattern
^[a-fA-F0-9]{32}$
, then the
attchcomponentmd5s
log field is mapped to the
target.file.md5
UDM field.
Else, if the
filemd5
log field value matches the regular expression pattern
^[a-fA-F0-9]{32}$
, then the
filemd5
log field is mapped to the
target.file.md5
UDM field.
filetypename
target.file.mime_type
filename
target.file.names
attchcomponentfilenames
target.file.names
attchcomponentfilesizes
target.file.size
If the
filesize
log field value is
not
empty, then the
filesize
log field is mapped to the
target.file.size
UDM field.
Else if the
attchcomponentfilesizes
log field value is
not
empty, then the
attchcomponentfilesizes
log field is mapped to the
target.file.size
UDM field.
b64attchcomponentfilesizes
target.file.size
If the
filesize
log field value is
not
empty, then the
filesize
log field is mapped to the
target.file.size
UDM field.
Else if the
b64attchcomponentfilesizes
log field value is
not
empty, then the
b64attchcomponentfilesizes
log field is mapped to the
target.file.size
UDM field.
sha
target.file.sha256
If the
sha
log field value matches the regular expression pattern
^[0-9a-f]+$
, then the
sha
log field is mapped to the
target.file.sha256
UDM field.
filesize
target.file.size
If the
filesize
log field value is
not
empty, then the
filesize
log field is mapped to the
target.file.size
UDM field.
Else if the
attchcomponentfilesizes
log field value is
not
empty, then the
attchcomponentfilesizes
log field is mapped to the
target.file.size
UDM field.
sharedchannel_hostname
target.hostname
hostname
target.hostname
If the
sharedchannel_hostname
log field value is empty and the
osharedchannel_hostname
log field value is empty, then the
hostname
log field is mapped to the
target.hostname
UDM field.
datacentercity
target.location.city
datacentercountry
target.location.country_or_region
datacenter
target.location.name
bucketowner
target.resource.attribute.labels[bucketowner]
projectname
target.resource.attribute.labels[projectname]
bucketname
target.resource.name
If the
bucketname
log field value is
not
empty, then the
bucketname
log field is mapped to the
target.resource.name
UDM field.
objnames1
target.resource.name
If the
objnames1
log field value is
not
empty, then the
objnames1
log field is mapped to the
target.resource.name
UDM field.
objectname
target.resource.name
If the
objectname
log field value is
not
empty, then the
objectname
log field is mapped to the
target.resource.name
UDM field.
reponame
target.resource.name
If the
reponame
log field value is
not
empty, then the
reponame
log field is mapped to the
target.resource.name
UDM field.
object_name_1
target.resource.name
If the
object_name_1
log field value is
not
empty, then the
object_name_1
log field is mapped to the
target.resource.name
UDM field.
bucketid
target.resource.product_object_id
objtypename1
target.resource.resource_subtype
If the
objtypename1
log field value is
not
empty, then the
objtypename1
log field is mapped to the
target.resource.resource_subtype
UDM field.
objecttype
target.resource.resource_subtype
If the
objecttype
log field value is
not
empty, then the
objecttype
log field is mapped to the
target.resource.resource_subtype
UDM field.
object_type
target.resource.resource_subtype
target.resource.resource_type
If the
bucketname
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
If the
reponame
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
REPOSITORY
.
departmentname
principal.user.department
extusername
target.user.userid
download_time
additional.fields[download_time]
runid
additional.fields[runid]
scan_time
additional.fields[scan_time]
scanid
additional.fields[scanid]
file_doctype
additional.fields[file_doctype]
filesha
additional.fields[filesha]
sender_type
additional.fields[sender_type]
last_edit_user
security_result.detection_fields[last_edit_user]
last_share_user
security_result.detection_fields[last_share_user]
last_shared_on
security_result.detection_fields[last_shared_on]
botname
security_result.detection_fields[botname]
dlpengnames
security_result.detection_fields[dlpengnames]
filetype
target.file.file_type
If the
filetype
log field value is equal to
pdf
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PDF
.
Else if the
filetype
log field value is equal to
ppt
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PPT
.
Else, the
additional.fields.key
UDM field is set to
filetype
and the
filetype
log field is mapped to the
additional.fields.value.string_value
UDM field.
extcollab_groups
security_result.detection_fields[extcollab_groups]
intcollab_groups
security_result.detection_fields[intcollab_groups]
oextcollab_groups
security_result.detection_fields[oextcollab_groups]
ointcollab_groups
security_result.detection_fields[ointcollab_groups]
dlpdictcnts
security_result.detection_fields[dlpdictcnts]
attchcomponentmd5s
target.file.md5
If the
attchcomponentmd5s
log field value is
not
equal to empty and the
attchcomponentmd5s
log field value matches the regular expression pattern
^[a-fA-F0-9]{32}$
, then the
attchcomponentmd5s
log field is mapped to the
target.file.md5
UDM field.
Else, if the
filemd5
log field value matches the regular expression pattern
^[a-fA-F0-9]{32}$
, then the
filemd5
log field is mapped to the
target.file.md5
UDM field.
b64attchcomponentfilenames
target.file.names
b64attchcomponentfiletypes
additional.fields[b64attchcomponentfiletypes]
b64attchcomponentmd5s
target.file.md5
If the
b64attchcomponentmd5s
log field value is
not
equal to empty and the
b64attchcomponentmd5s
log field value matches the regular expression pattern
^[a-fA-F0-9]{32}$
, then the
b64attchcomponentmd5s
log field is mapped to the
target.file.md5
UDM field.
Else, if the
filemd5
log field value matches the regular expression pattern
^[a-fA-F0-9]{32}$
, then the
filemd5
log field is mapped to the
target.file.md5
UDM field.
b64bucketname
target.resource.name
b64collabnames
additional.fields[b64collabnames]
b64department
principal.user.department
If the
dept
log field value is
not
empty, then the
dept
log field is mapped to the
principal.user.department
UDM field. Else, the
b64department
log field is mapped to the
principal.user.department
UDM field.
b64dlpdictnames
security_result.detection_fields[b64dlpdictnames]
b64dlpenginenames
security_result.detection_fields[b64dlpenginenames]
b64external_collabnames
additional.fields[b64external_collabnames]
b64external_recptnames
network.email.to
b64extownername
additional.fields[b64extownername]
b64extrecptnames
network.email.to
b64filename
target.file.names
b64filepath
target.file.full_path
If
b64filepath
is not empty, then the
b64filepath
log field is mapped to the
target.file.full_path
UDM field. Else if
filesource
is not empty, then the
filesource
log field is mapped to the
target.file.full_path
UDM field.
b64filesource
target.file.full_path
If
filepath
is not empty, then the
filepath
log field is mapped to the
target.file.full_path
UDM field. Else if
b64filesource
is not empty, then the
b64filesource
log field is mapped to the
target.file.full_path
UDM field.
b64fullurl
principal.url
If the
b64fullurl
log field is
not
empty and the
b64fullurl
log field value is not equal to
Unknown URL
, then the
b64fullurl
log field is mapped to the
principal.url
UDM field.
b64hostname
target.hostname
If the
sharedchannel_hostname
log field value is empty and the
osharedchannel_hostname
log field value is empty, then the
b64hostname
log field is mapped to the
target.hostname
UDM field.
b64internal_collabnames
additional.fields[b64internal_collabnames]
b64internal_recptnames
network.email.to
b64intrecptnames
network.email.to
b64objectname
target.resource.name
b64owner
principal.user.email_addresses
If the
b64owner
log field value matches the regular expression pattern
(^.*@.*$)
, then the
b64owner
log field is mapped to the
principal.user.email_addresses
UDM field.
b64projectname
target.resource.attribute.labels[b64projectname]
b64reponame
target.resource.name
b64rulelabel
security_result.rule_name
b64sender
network.email.from
If the
b64sender
log field value matches the regular expression pattern
(^.*@.*$)
, then the
b64sender
log field is mapped to the
network.email.from
UDM field.
b64tenant
additional.fields[b64tenant]
b64threatname
security_result.threat_name
b64intcollab_groups
security_result.detection_fields[b64intcollab_groups]
b64extcollab_groups
security_result.detection_fields[b64extcollab_groups]
eattchcomponentfilenames
target.file.names
eattchcomponentfiletypes
additional.fields[eattchcomponentfiletypes]
ebucketname
target.resource.name
ebucketowner
target.resource.attribute.labels[ebucketowner]
ecollabnames
additional.fields[ecollabnames]
edepartment
principal.user.department
If the
dept
log field value is
not
empty, then the
dept
log field is mapped to the
principal.user.department
UDM field. Else, the
edepartment
log field is mapped to the
principal.user.department
UDM field.
edlpdictnames
security_result.detection_fields[edlpdictnames]
edlpenginenames
security_result.detection_fields[edlpenginenames]
eexternal_collabnames
additional.fields[eexternal_collabnames]
eextownername
additional.fields[eextownername]
eextrecptnames
network.email.to
efilename
target.file.names
efilepath
target.file.full_path
If
efilepath
is not empty, then the
efilepath
log field is mapped to the
target.file.full_path
UDM field. Else if
filesource
is not empty, then the
filesource
log field is mapped to the
target.file.full_path
UDM field.
efilesource
target.file.full_path
If
filepath
is not empty, then the
filepath
log field is mapped to the
target.file.full_path
UDM field. Else if
efilesource
is not empty, then the
efilesource
log field is mapped to the
target.file.full_path
UDM field.
efullurl
principal.url
If the
efullurl
log field is
not
empty and the
efullurl
log field value is not equal to
Unknown URL
, then the
efullurl
log field is mapped to the
principal.url
UDM field.
ehostname
target.hostname
einternal_collabnames
additional.fields[einternal_collabnames]
eintrecptnames
network.email.to
eobjectname
target.resource.name
eowner
principal.user.email_addresses
If the
eowner
log field value matches the regular expression pattern
(^.*@.*$)
, then the
eowner
log field is mapped to the
principal.user.email_addresses
UDM field.
eprojectname
target.resource.attribute.labels[eprojectname]
ereponame
target.resource.name
esender
network.email.from
If the
esender
log field value matches the regular expression pattern
(^.*@.*$)
, then the
esender
log field is mapped to the
network.email.from
UDM field.
ethreatname
security_result.threat_name
What's next
Data ingestion to Google SecOps
Need more help?
Get answers from Community members and Google SecOps professionals.
