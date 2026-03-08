# Collect Proofpoint TAP alerts logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail/  
**Scraped:** 2026-03-05T09:59:19.687270Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Proofpoint TAP alerts logs
Supported in:
Google secops
SIEM
This document describes how you can collect Proofpoint Targeted Attack Protection (TAP) alerts logs by
setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
PROOFPOINT_MAIL
ingestion label.
Configure Proofpoint TAP alerts
Sign in to the Proofpoint threat
insight portal
using your credentials.
On the
Settings
tab, select
Connected applications
. The
Service credentials
section appears.
In the
Name
section, click
Create new credential
.
Type the name of your organization, such as
altostrat.com
.
Click
Generate
. In the
Generated service credential
dialog, the
Service principal
and
Secret
values appear.
Copy the
Service principal
and
Secret
values. The values are displayed only at the time of creation and are required when you configure the Google Security Operations feed.
Click
Done
.
Set up feeds
To configure the feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
Proofpoint
feed pack.
Locate the
Proofpoint Tap Alerts
log type.
Specify the values for the following fields:
Source type
: Third party API
Username
: specify the service principal that you obtained previously.
Secret
: specify the secret that you obtained previously.
Advanced options
*
Feed Name
: A prepopulated value that identifies the feed.
*
Asset Namespace
: Namespace associated with the feed.
*
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create Feed
.
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google Security Operations support
.
Field mapping reference
This parser handles Proofpoint Mail logs in JSON or key-value format, extracting email and network activity details. It maps log fields to the UDM, categorizing events like email transactions and network HTTP requests, and enriching them with security details like actions, categories, and threat information.
UDM mapping table
Log Field
UDM Mapping
Remark
action
security_result.action_details
The value of
action
from the raw log is directly mapped.
adultscore
additional.fields[].key
: "adultscore"
additional.fields[].value.string_value
: Value of adultscore
The value of
adultscore
from the raw log is placed in
additional_fields
.
attachments
additional.fields[].key
: "attachments"
additional_fields[].value.string_value
: Value of attachments
The value of
attachments
from the raw log is placed in
additional_fields
.
campaignID
security_result.rule_id
The value of
campaignID
from the raw log is directly mapped.
ccAddresses
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
cid
additional.fields[].key
:
cid
additional_fields[].value.string_value
: Value of
cid
The value of
cid
from the raw log is placed in
additional_fields
.
cipher
/
tls
network.tls.cipher
If
cipher
is present and not "NONE", its value is used. Otherwise, if
tls
is present and not "NONE", its value is used.
classification
security_result.category_details
The value of
classification
from the raw log is directly mapped.
clickIP
principal.asset.ip
principal.ip
The value of
clickIP
from the raw log is directly mapped.
clicks.impostorScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
clicks.malwareScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
clicks.phishScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
clicks.quarantineFolder
security_result.priority
or
security_result.detection_fields
if
click.quarantineFolder
is equal to "low priority" or "high priority" then map to UDM field
security_result.priority
, else map to
security_result.detection_fields
clicks.quarantineRule
security_result.rule_name
Mapped to a key-value pair in
security_result.rule_name
clicks.sender
Not Mapped
clicks.senderIP
principal.ip
Mapped to a key-value pair in
principal.ip
clicks.spamScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
clicksBlocked[].campaignId
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksBlocked[].clickIP
principal.asset.ip
principal.ip
The value of
clickIP
within the
clicksBlocked
array is mapped.
clicksBlocked[].clickTime
metadata.event_timestamp.seconds
The parser converts the
clickTime
string to a timestamp and maps it.
clicksBlocked[].classification
security_result.category_details
The value of
classification
within the
clicksBlocked
array is mapped.
clicksBlocked[].GUID
metadata.product_log_id
The value of
GUID
within the
clicksBlocked
array is mapped.
clicksBlocked[].id
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksBlocked[].messageID
network.email.mail_id
The value of
messageID
within the
clicksBlocked
array is mapped.
clicksBlocked[].recipient
target.user.email_addresses
The value of
recipient
within the
clicksBlocked
array is mapped.
clicksBlocked[].sender
principal.user.email_addresses
The value of
sender
within the
clicksBlocked
array is mapped.
clicksBlocked[].senderIP
about.ip
The value of
senderIP
within the
clicksBlocked
array is mapped. The general
senderIP
entry maps to
principal.asset.ip
or
principal.ip
clicksBlocked[].threatID
security_result.threat_id
The value of
threatID
within the
clicksBlocked
array is mapped.
clicksBlocked[].threatTime
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksBlocked[].threatURL
security_result.url_back_to_product
The value of
threatURL
within the
clicksBlocked
array is mapped.
clicksBlocked[].threatStatus
security_result.threat_status
The value of
threatStatus
within the
clicksBlocked
array is mapped.
clicksBlocked[].url
target.url
The value of
url
within the
clicksBlocked
array is mapped.
clicksBlocked[].userAgent
network.http.user_agent
The value of
userAgent
within the
clicksBlocked
array is mapped.
clicksPermitted[].campaignId
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksPermitted[].clickIP
principal.asset.ip
principal.ip
The value of
clickIP
within the
clicksPermitted
array is mapped.
clicksPermitted[].clickTime
metadata.event_timestamp.seconds
The parser converts the
clickTime
string to a timestamp and maps it.
clicksPermitted[].classification
security_result.category_details
The value of
classification
within the
clicksPermitted
array is mapped.
clicksPermitted[].guid
metadata.product_log_id
The value of
guid
within the
clicksPermitted
array is mapped.
clicksPermitted[].id
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksPermitted[].messageID
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksPermitted[].recipient
target.user.email_addresses
The value of
recipient
within the
clicksPermitted
array is mapped.
clicksPermitted[].sender
principal.user.email_addresses
The value of
sender
within the
clicksPermitted
array is mapped.
clicksPermitted[].senderIP
about.ip
The value of
senderIP
within the
clicksPermitted
array is mapped.
clicksPermitted[].threatID
security_result.threat_id
The value of
threatID
within the
clicksPermitted
array is mapped.
clicksPermitted[].threatTime
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
clicksPermitted[].threatURL
security_result.url_back_to_product
The value of
threatURL
within the
clicksPermitted
array is mapped.
clicksPermitted[].url
target.url
The value of
url
within the
clicksPermitted
array is mapped.
clicksPermitted[].userAgent
network.http.user_agent
The value of
userAgent
within the
clicksPermitted
array is mapped.
clickTime
metadata.event_timestamp.seconds
The parser converts the
clickTime
string to a timestamp and maps it.
cmd
principal.process.command_line
or
network.http.method
If
sts
(HTTP status code) is present,
cmd
is mapped to
network.http.method
. Otherwise, it's mapped to
principal.process.command_line
.
collection_time.seconds
metadata.event_timestamp.seconds
The value of
collection_time.seconds
from the raw log is directly mapped.
completelyRewritten
security_result.detection_fields[].key
: "completelyRewritten"
security_result.detection_fields[].value
: Value of completelyRewritten
The value of
completelyRewritten
from the raw log is placed in
security_result.detection_fields
.
contentType
about.file.mime_type
The value of
contentType
from the raw log is directly mapped.
country
principal.location.country_or_region
The value of
country
from the raw log is directly mapped.
create_time.seconds
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
data
(Multiple fields)
The JSON payload in the
data
field is parsed and mapped to various UDM fields.
date
/
date_log_rebase
metadata.event_timestamp.seconds
The parser rebases the date to a timestamp using either
date_log_rebase
or
date
and
timeStamp
fields.
dict
security_result.category_details
The value of
dict
from the raw log is directly mapped.
disposition
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
dnsid
network.dns.id
The value of
dnsid
from the raw log is directly mapped and converted to an unsigned integer.
domain
/
hfrom_domain
principal.administrative_domain
If
domain
is present, its value is used. Otherwise, if
hfrom_domain
is present, its value is used.
duration
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
eid
additional.fields[].key
: "eid"
additional_fields[].value.string_value
: Value of eid
The value of
eid
from the raw log is placed in
additional_fields
.
engine
metadata.product_version
The value of
engine
from the raw log is directly mapped.
err
/
msg
/
result_detail
/
tls-alert
security_result.description
The first available value among
msg
,
err
,
result_detail
, or
tls-alert
(after removing quotes) is mapped.
file
/
name
principal.process.file.full_path
If
file
is present, its value is used. Otherwise, if
name
is present, its value is used.
filename
about.file.full_path
The value of
filename
from the raw log is directly mapped.
folder
additional.fields[].key
: "folder"
additional_fields[].value.string_value
: Value of folder
The value of
folder
from the raw log is placed in
additional_fields
.
from
/
hfrom
/
value
network.email.from
Complex logic applies (see parser code).  Handles
<
and
>
characters and checks for valid email format.
fromAddress
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
GUID
metadata.product_log_id
The value of
GUID
from the raw log is directly mapped.
headerCC
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
headerFrom
additional.fields[].key
: "headerFrom"
additional_fields[].value.string_value
: Value of headerFrom
The value of
headerFrom
from the raw log is placed in
additional_fields
.
headerReplyTo
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
headerTo
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
helo
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
hops-ip
/
lip
intermediary.ip
If
hops-ip
is present, its value is used. Otherwise, if
lip
is present, its value is used.
host
principal.hostname
The value of
host
from the raw log is directly mapped.
id
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
impostorScore
security_result.detection_fields
ip
principal.asset.ip
principal.ip
The value of
ip
from the raw log is directly mapped.
log_level
security_result.severity_details
The value of
log_level
is mapped and also used to derive
security_result.severity
.
m
network.email.mail_id
The value of
m
(after removing
<
and
>
characters) is mapped.
malwareScore
security_result.detection_fields
md5
about.file.md5
The value of
md5
from the raw log is directly mapped.
messageID
network.email.mail_id
The value of
messageID
(after removing
<
and
>
characters) is mapped.
messagesBlocked
(array)
(Multiple fields)
The array of
messagesBlocked
objects is iterated, and each object's fields are mapped to UDM fields.
messagesBlocked[].ccAddresses
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].cluster
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].completelyRewritten
security_result.detection_fields[].key
: "completelyRewritten"
security_result.detection_fields[].value
: Value of completelyRewritten
The value of
completelyRewritten
from the raw log is placed in
security_result.detection_fields
.
messagesBlocked[].fromAddress
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].GUID
metadata.product_log_id
The value of
GUID
from the raw log is directly mapped.
messagesBlocked[].headerFrom
additional.fields[].key
: "headerFrom"
additional_fields[].value.string_value
: Value of headerFrom
The value of
headerFrom
from the raw log is placed in
additional_fields
.
messagesBlocked[].headerReplyTo
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].id
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].impostorScore
additional.fields[].key
: "impostorScore"
additional_fields[].value.number_value
: Value of impostorScore
The value of
impostorScore
from the raw log is placed in
additional_fields
.
messagesBlocked[].malwareScore
additional.fields[].key
: "malwareScore"
additional_fields[].value.number_value
: Value of malwareScore
The value of
malwareScore
from the raw log is placed in
additional_fields
.
messagesBlocked[].messageID
network.email.mail_id
The value of
messageID
(after removing
<
and
>
characters) is mapped.
messagesBlocked[].messageParts
about.file
(repeated)
Each object in the
messageParts
array is mapped to a separate
about.file
object.
messagesBlocked[].messageParts[].contentType
about.file.mime_type
The value of
contentType
from the raw log is directly mapped.
messagesBlocked[].messageParts[].disposition
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].messageParts[].filename
about.file.full_path
The value of
filename
from the raw log is directly mapped.
messagesBlocked[].messageParts[].md5
about.file.md5
The value of
md5
from the raw log is directly mapped.
messagesBlocked[].messageParts[].sandboxStatus
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].messageParts[].sha256
about.file.sha256
The value of
sha256
from the raw log is directly mapped.
messagesBlocked[].messageSize
additional.fields[].key
: "messageSize"
additional_fields[].value.number_value
: Value of messageSize
The value of
messageSize
from the raw log is placed in
additional_fields
.
messagesBlocked[].messageTime
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].modulesRun
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].phishScore
additional.fields[].key
: "phishScore"
additional_fields[].value.number_value
: Value of phishScore
The value of
phishScore
from the raw log is placed in
additional_fields
.
messagesBlocked[].policyRoutes
additional.fields[].key
: "PolicyRoutes"
additional_fields[].value.list_value.values[].string_value
: Value of policyRoutes
The values of
policyRoutes
from the raw log are placed as a list in
additional_fields
.
messagesBlocked[].QID
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].quarantineFolder
additional.fields[].key
: "quarantineFolder"
additional_fields[].value.string_value
: Value of quarantineFolder
The value of
quarantineFolder
from the raw log is placed in
additional_fields
.
messagesBlocked[].quarantineRule
additional.fields[].key
: "quarantineRule"
additional_fields[].value.string_value
: Value of quarantineRule
The value of
quarantineRule
from the raw log is placed in
additional_fields
.
messagesBlocked[].recipient
target.user.email_addresses
The value of
recipient
from the raw log is directly mapped.
messagesBlocked[].replyToAddress
network.email.reply_to
The value of
replyToAddress
from the raw log is directly mapped.
messagesBlocked[].sender
principal.user.email_addresses
The value of
sender
from the raw log is directly mapped.
messagesBlocked[].senderIP
principal.asset.ip
principal.ip
The value of
senderIP
from the raw log is directly mapped.
messagesBlocked[].spamScore
additional.fields[].key
: "spamScore"
additional_fields[].value.number_value
: Value of spamScore
The value of
spamScore
from the raw log is placed in
additional_fields
.
messagesBlocked[].subject
network.email.subject
The value of
subject
from the raw log is directly mapped.
messagesBlocked[].threatsInfoMap
security_result
(repeated)
Each object in the
threatsInfoMap
array is mapped to a separate
security_result
object.
messagesBlocked[].threatsInfoMap[].classification
security_result.category_details
The value of
classification
from the raw log is directly mapped.
messagesBlocked[].threatsInfoMap[].threat
security_result.about.url
The value of
threat
from the raw log is directly mapped.
messagesBlocked[].threatsInfoMap[].threatID
security_result.threat_id
The value of
threatID
from the raw log is directly mapped.
messagesBlocked[].threatsInfoMap[].threatStatus
security_result.threat_status
The value of
threatStatus
from the raw log is directly mapped.
messagesBlocked[].threatsInfoMap[].threatTime
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesBlocked[].threatsInfoMap[].threatType
security_result.threat_name
The value of
threatType
from the raw log is directly mapped.
messagesBlocked[].threatsInfoMap[].threatUrl
security_result.url_back_to_product
The value of
threatUrl
from the raw log is directly mapped.
messagesBlocked[].toAddresses
network.email.to
The value of
toAddresses
from the raw log is directly mapped.
messagesBlocked[].xmailer
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
messagesDelivered
(array)
(Multiple fields)
The array of
messagesDelivered
objects is iterated, and each object's fields are mapped to UDM fields.  Similar logic as
messagesBlocked
.
message
(Multiple fields)
If the
message
field is valid JSON, it's parsed and mapped to various UDM fields.
metadata.event_type
metadata.event_type
Set to "EMAIL_TRANSACTION" if
message
is not JSON, otherwise derived from the JSON data.  Set to "GENERIC_EVENT" if the syslog message fails to parse.
metadata.log_type
metadata.log_type
Hardcoded to "PROOFPOINT_MAIL".
metadata.product_event_type
metadata.product_event_type
Set to "messagesBlocked", "messagesDelivered", "clicksPermitted", or "clicksBlocked" based on the JSON data.
metadata.product_name
metadata.product_name
Hardcoded to "TAP".
metadata.vendor_name
metadata.vendor_name
Hardcoded to "PROOFPOINT".
mime
principal.process.file.mime_type
The value of
mime
from the raw log is directly mapped.
mod
additional.fields[].key
: "module"
additional_fields[].value.string_value
: Value of mod
The value of
mod
from the raw log is placed in
additional_fields
.
msg.imposterScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
msg.malwareScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
msg.phishScore
security_result.detection_fields
Mapped to a key-value pair in
security_result.detection_fields
msg.quarantineFolder
security_result.priority
or
security_result.detection_fields
if
msg.quarantineFolder
is equal to "low priority" or "high priority" then map to UDM field
security_result.priority
, else map to
security_result.detection_fields
msg.quarantineRule
security_result.rule_name
msg.spamScore
security_result.detection_fields
msgPart.contentType
Not Mapped
oContentType
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
partData.contentType
about.file.mime_type
partData.disposition
additional.fields
partData.filename
about.file.full_path
partData.md5
about.file.md5
partData.sha256
about.file.sha256
partData.contentType
security_result.detection_fields
path
/
uri
principal.url
If
path
is present, its value is used. Otherwise, if
uri
is present, its value is used.
phishScore
security_result.detection_fields
pid
principal.process.pid
The value of
pid
from the raw log is directly mapped.
policy
network.direction
If
policy
is "inbound", UDM field is set to "INBOUND". If
policy
is "outbound", UDM field is set to "OUTBOUND".
policyRoutes
additional.fields[].key
: "PolicyRoutes"
additional_fields[].value.list_value.values[].string_value
: Value of policyRoutes
The values of
policyRoutes
from the raw log are placed as a list in
additional_fields
.
profile
additional.fields[].key
: "profile"
additional_fields[].value.string_value
: Value of profile
The value of
profile
from the raw log is placed in
additional_fields
.
prot
proto
The value of
prot
is extracted to
protocol
, converted to uppercase, and then mapped to
proto
.
proto
network.application_protocol
The value of
proto
(or the derived value from
prot
) is mapped. If the value is "ESMTP", it's changed to "SMTP" before mapping.
querydepth
additional.fields[].key
: "querydepth"
additional_fields[].value.string_value
: Value of querydepth
The value of
querydepth
from the raw log is placed in
additional_fields
.
queryEndTime
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
qid
additional.fields[].key
: "qid"
additional_fields[].value.string_value
: Value of qid
The value of
qid
from the raw log is placed in
additional_fields
.
quarantineFolder
security_result.priority
or
security_result.detection_fields
if
quarantineFolder
is equal to "low priority" or "high priority" then map to UDM field
security_result.priority
, else map to
security_result.detection_fields
rcpt
/
rcpts
network.email.to
If
rcpt
is present and a valid email address, it's merged into the
to
field.  Same logic for
rcpts
.
recipient
target.user.email_addresses
The value of
recipient
from the raw log is directly mapped.
relay
intermediary.hostname
intermediary.ip
The
relay
field is parsed to extract hostname and IP address, which are then mapped to
intermediary.hostname
and
intermediary.ip
respectively.
replyToAddress
network.email.reply_to
The value of
replyToAddress
from the raw log is directly mapped.
result
security_result.action
If
result
is "pass", UDM field is set to "ALLOW". If
result
is "fail", UDM field is set to "BLOCK".
routes
additional.fields[].key
: "routes"
additional_fields[].value.string_value
: Value of routes
The value of
routes
from the raw log is placed in
additional_fields
.
s
network.session_id
The value of
s
from the raw log is directly mapped.
sandboxStatus
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
selector
additional.fields[].key
: "selector"
additional_fields[].value.string_value
: Value of selector
The value of
selector
from the raw log is placed in
additional_fields
.
sender
principal.user.email_addresses
The value of
sender
from the raw log is directly mapped.
senderIP
principal.asset.ip
principal.ip
or
about.ip
If it's within a click event, it's mapped to
about.ip
. Otherwise, it's mapped to
principal.asset.ip
and
principal.ip
.
sha256
security_result.about.file.sha256
or
about.file.sha256
If it's within a threatInfoMap, it's mapped to
security_result.about.file.sha256
. Otherwise, it's mapped to
about.file.sha256
.
size
principal.process.file.size
or
additional.fields[].key
: "messageSize"
additional_fields[].value.number_value
: Value of messageSize
If it's within a message event, it's mapped to
additional.fields[].messageSize
and converted to an unsigned integer. Otherwise, it's mapped to
principal.process.file.size
and converted to an unsigned integer.
spamScore
security_result.detection_fields
stat
additional.fields[].key
: "status"
additional_fields[].value.string_value
: Value of stat
The value of
stat
from the raw log is placed in
additional_fields
.
status
additional.fields[].key
: "status"
additional_fields[].value.string_value
: Value of status
The value of
status
(after removing quotes) from the raw log is placed in
additional_fields
.
sts
network.http.response_code
The value of
sts
from the raw log is directly mapped and converted to an integer.
subject
network.email.subject
The value of
subject
from the raw log is directly mapped after removing quotes.
threatID
security_result.threat_id
The value of
threatID
from the raw log is directly mapped.
threatStatus
security_result.threat_status
The value of
threatStatus
from the raw log is directly mapped.
threatTime
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
threatType
security_result.threat_name
The value of
threatType
from the raw log is directly mapped.
threatUrl
/
threatURL
security_result.url_back_to_product
The value of
threatUrl
or
threatURL
from the raw log is directly mapped.
threatsInfoMap
security_result
(repeated)
Each object in the
threatsInfoMap
array is mapped to a separate
security_result
object.
tls
network.tls.cipher
If
cipher
is not present or is "NONE", the value of
tls
is used if it's not "NONE".
tls_verify
/
verify
security_result.action
If
verify
is present, its value is used to determine the action. Otherwise,
tls_verify
is used. "FAIL" maps to "BLOCK", "OK" maps to "ALLOW".
tls_version
/
version
network.tls.version
If
tls_version
is present and not "NONE", its value is used. Otherwise, if
version
matches "TLS", its value is used.
to
network.email.to
The value of
to
(after removing
<
and
>
characters) is mapped. If it's not a valid email address, it's added to
additional_fields
.
toAddresses
network.email.to
The value of
toAddresses
from the raw log is directly mapped.
timestamp.seconds
metadata.event_timestamp.seconds
The value of
timestamp.seconds
from the raw log is directly mapped.
type
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
url
target.url
or
principal.url
If it's within a click event, it's mapped to
target.url
. Otherwise, it's mapped to
principal.url
.
userAgent
network.http.user_agent
The value of
userAgent
from the raw log is directly mapped.
uri
principal.url
If
path
is not present, the value of
uri
is used.
value
network.email.from
If
from
and
hfrom
are not valid email addresses, and
value
is a valid email address (after removing
<
and
>
characters), it's mapped.
vendor
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
verify
security_result.action
If
verify
is present, it's used to determine the action. "NOT" maps to "BLOCK", other values map to "ALLOW".
version
network.tls.version
If
tls_version
is not present or is "NONE", and
version
contains "TLS", it's mapped.
virusthreat
security_result.threat_name
The value of
virusthreat
from the raw log is directly mapped if it's not "unknown".
virusthreatid
security_result.threat_id
The value of
virusthreatid
(after removing quotes) from the raw log is directly mapped if it's not "unknown".
xmailer
Not Mapped
Although present in raw logs, this field is not mapped to the IDM object in the provided UDM.
UDM mapping delta reference
On September 9, 2025, Google SecOps released a new version of the Symantec Endpoint Protection parser, which includes significant changes to the mapping of Symantec Endpoint Protection log fields to UDM fields and updates to event type classifications (mappings).
Log-field mapping delta
The following table shows the changes to how Symantec Endpoint Protection log fields are mapped to UDM fields.
The
Old mapping
column lists the fields exposed prior to September 9, 2025, and the
Current mapping
column lists the new fields.
Log field
Old mapping
Current mapping
clicks.impostorScore
additional.fields
security_result.detection_fields
clicks.malwareScore
additional.fields
security_result.detection_fields
clicks.phishScore
additional.fields
security_result.detection_fields
clicks.quarantineFolder
additional.fields
If
quarantineFolder
is equal to
low priority
or
high priority
,then map to
security_result.priority
. Otherwise, map to
security_result.detection_fields
.
clicks.quarantineRule
additional.fields
security_result.rule_name
clicks.sender
about.email
Not Mapped
clicks.senderIP
about.ip
principal.ip
clicks.spamScore
additional.fields
security_result.detection_fields
impostorScore
additional.fields
security_result.detection_fields
malwareScore
additional.fields
security_result.detection_fields
msg.impostorScore
additional.fields
security_result.detection_fields
msg.malwareScore
additional.fields
security_result.detection_fields
msg.phishScore
additional.fields
security_result.detection_fields
msg.quarantineFolder
additional.fields
If
quarantineFolder
is equal to
low priority
or
high priority
,then map to
security_result.priority
. Otherwise, map to
security_result.detection_fields
.
msg.quarantineRule
additional.fields
security_result.rule_name
msg.spamScore
additional.fields
security_result.detection_fields
msgPart.contentType
additional.fields
Not Mapped
partData.contentType
principal.process.file.mime_type
about.file.mime_type
partData.disposition
security_result.detection_fields
additional.fields
partData.filename
principal.process.file.full_path
about.file.full_path
partData.md5
principal.process.file.md5
about.file.md5
partData.sha256
about.file.sha1
about.file.sha256
phishScore
additional.fields
security_result.detection_fields
quarantineFolder
additional.fields
if
quarantineFolder
is equal to
low priority
or
high priority
then map to UDM field
security_result.priority
else security_result.detection_fields
spamScore
additional.fields
security_result.detection_fields
Event-type mapping delta
Multiple events that were previously classified as
generic events
are now properly classified with more meaningful event types.
The following table lists the delta for the handling of Symantec Endpoint Protection event types prior to September 9, 2025 and subsequently (listed in the
Old event_type
and
Current event_type
columns respectively).
Format
eventType from log
Old event_type
Current event_type
SYSLOG+KV
If the log has
fromAddress
,
toAddresses
,
hfrom
,
from
,
value
,
to
,
rcpt
,
rcpts
or
mailer
,
proto
,
mod
fields are present
EMAIL_TRANSACTION
If the log contains only
mail_id
details
EMAIL_TRANSACTION
EMAIL_UNCATEGORIZED
CEF
logs
eventname=
messagesDelivered
,
messagesBlocked
EMAIL_TRANSACTION
if the log has
emails
,
sender
,
headerReplyTo
,
orig_recipient
USER_UNCATEGORIED
if the log has
src
,
host
STATUS_UPDATE
SYSLOG+JSON
eventname=
messagesDelivered
,
messagesBlocked
,
clicksPermitted
,
clicksBlocked
EMAIL_TRANSACTION
JSON
record.address
USER_UNCATEGORIZED
lookalikeDomain.name
STATUS_UPDATE
Need more help?
Get answers from Community members and Google SecOps professionals.
