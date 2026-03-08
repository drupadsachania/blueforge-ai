# Collect Atlassian Jira logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-jira/  
**Scraped:** 2026-03-05T09:19:22.439090Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Atlassian Jira logs
Supported in:
Google secops
SIEM
Overview
This parser handles Atlassian Jira logs in SYSLOG and JSON formats. It first attempts to parse the message as JSON. If that fails, it uses grok patterns to parse SYSLOG formatted messages, extracting various fields like IP addresses, usernames, HTTP methods, and response codes before mapping them to the UDM. The parser also handles specific Jira audit events, including login successes and failures, and maps relevant fields to security result attributes within the UDM.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Atlassian Jira.
Set up feeds from SIEM Settings > Feeds
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
field, enter a name for the feed (for example,
Atlassian Jira Logs
).
Select
Webhook
as the
Source type
.
Select
Atlassian Jira
as the
Log type
.
Click
Next
.
Optional: specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
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
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
On the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. You need to specify this endpoint URL in your client application.
Click
Done
.
Create an API key for the webhook feed
Go to
Google Cloud console
>
Credentials
.
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Google Security Operations API
.
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Create a webhook in Atlassian Jira for Google SecOps
Access your Jira instance as an administrator.
Go to
Settings
settings
>
System
>
WebHooks
.
Click
Create a WebHook
.
Configure the following webhook details:
Name
: Provide a descriptive name for the webhook (For example,
Google SecOps Integration
).
URL
: Enter the Google SecOps API endpoint URL.
Events
: Select the Jira events that should trigger the webhook. Choose the events relevant to your security monitoring needs (For example, issue created, issue updated, comment added). You can select
All Events
if needed.
Optional:
JQL Filter
: Use a JQL filter to further refine which events trigger the webhook. This is useful for focusing on specific projects, issue types, or other criteria.
Exclude body
: Leave this unchecked. The webhook needs to send the event data in JSON format to Google SecOps.
Click
Create
to save the webhook configuration.
UDM Mapping Table
Log Field
UDM Mapping
Logic
affectedObjects.id
target.resource.attribute.labels.value
The
id
field within each object of the
affectedObjects
array is mapped to a label with key "ID_[index]" where [index] is the position of the object in the array.
affectedObjects.name
target.resource.attribute.labels.value
The
name
field within each object of the
affectedObjects
array is mapped to a label with key "Name_[index]" where [index] is the position of the object in the array.
affectedObjects.type
target.resource.attribute.labels.value
The
type
field within each object of the
affectedObjects
array is mapped to a label with key "Type_[index]" where [index] is the position of the object in the array.
associatedItems.0.id
target.user.userid
If
associatedItems.0.typeName
is "USER", this field is mapped to
target.user.userid
. Otherwise, it's mapped to a label with key "associatedItems Id" in
security_result.detection_fields
.
associatedItems.0.name
target.user.user_display_name
If
associatedItems.0.typeName
is "USER", this field is mapped to
target.user.user_display_name
. Otherwise, it's mapped to a label with key "associatedItems Name" in
security_result.detection_fields
.
associatedItems.0.parentId
target.process.parent_process.pid
If
associatedItems.0.typeName
is "USER", this field is mapped to
target.process.parent_process.pid
.
associatedItems.0.parentName
target.resource.parent
If
associatedItems.0.typeName
is "USER", this field is mapped to
target.resource.parent
.
associatedItems.0.typeName
security_result.detection_fields.value
Mapped to a label with key "associatedItems TypeName" in
security_result.detection_fields
.
author.id
principal.user.userid
Mapped to
principal.user.userid
.
author.name
principal.user.user_display_name
Mapped to
principal.user.user_display_name
.
author.type
principal.resource.attribute.labels.value
Mapped to a label with key "Author Type" in
principal.resource.attribute.labels
.
author.uri
principal.url
Mapped to
principal.url
.
authorAccountId
principal.user.userid
Mapped to
principal.user.userid
.
authorKey
target.resource.attribute.labels.value
Mapped to a label with key "Author Key" in
target.resource.attribute.labels
.
auditType.action
security_result.summary
Mapped to
security_result.summary
. Also used to derive
security_result.action
and
metadata.event_type
(USER_LOGIN if action contains "login", ALLOW if "successful", BLOCK if "failed").
auditType.area
metadata.product_event_type
Mapped to
metadata.product_event_type
.
auditType.category
security_result.category_details
Mapped to
security_result.category_details
.
category
metadata.product_event_type
Mapped to
metadata.product_event_type
.
changedValues.changedFrom
security_result.about.resource.attribute.labels.value
Mapped to a label with key "Changed From" in
security_result.about.resource.attribute.labels
.
changedValues.changedTo
security_result.about.resource.attribute.labels.value
Mapped to a label with key "Changed To" in
security_result.about.resource.attribute.labels
.
changedValues.fieldName
security_result.about.resource.attribute.labels.value
Mapped to a label with key "FieldName" in
security_result.about.resource.attribute.labels
.
changedValues.i18nKey
security_result.about.resource.attribute.labels.value
Mapped to a label with key "FieldName" in
security_result.about.resource.attribute.labels
.
changedValues.key
security_result.about.resource.attribute.labels.value
Mapped to a label with key "Changed From" in
security_result.about.resource.attribute.labels
.
changedValues.to
security_result.about.resource.attribute.labels.value
Mapped to a label with key "Changed To" in
security_result.about.resource.attribute.labels
.
created
metadata.event_timestamp
Parsed and mapped to
metadata.event_timestamp
.
dst_ip
target.ip
Mapped to
target.ip
.
extraAttributes.name
principal.resource.attribute.labels.value
Mapped to a label with key "Name" in
principal.resource.attribute.labels
.
extraAttributes.value
principal.resource.attribute.labels.value
Mapped to a label with key "Value" in
principal.resource.attribute.labels
.
http_method
network.http.method
Mapped to
network.http.method
.
http_referral_url
network.http.referral_url
Mapped to
network.http.referral_url
.
id
metadata.product_log_id
Mapped to
metadata.product_log_id
.
objectItem.id
security_result.detection_fields.value
Mapped to a label with key "objectItem Id" in
security_result.detection_fields
.
objectItem.name
security_result.detection_fields.value
Mapped to a label with key "objectItem Name" in
security_result.detection_fields
.
objectItem.typeName
security_result.detection_fields.value
Mapped to a label with key "objectItem TypeName" in
security_result.detection_fields
.
path
principal.url
If not "-" or "/status", mapped to
principal.url
.
protocol
network.ip_protocol
If "HTTP", mapped to
network.ip_protocol
.
remoteAddress
principal.ip
Mapped to
principal.ip
.
response_code
network.http.response_code
Mapped to
network.http.response_code
.
sent_bytes
network.sent_bytes
Mapped to
network.sent_bytes
.
source
principal.ip
Parsed to extract IP addresses and merged into
principal.ip
.
src_ip1
,
src_ip2
,
src_ip3
principal.ip
Mapped to
principal.ip
.
summary
metadata.description
Mapped to
metadata.description
.
user_agent
network.http.user_agent
Mapped to
network.http.user_agent
.
user_name
principal.user.userid
Mapped to
principal.user.userid
. Set to "MACHINE" if
auditType.action
contains "login". Derived from
date_time
if parsing syslog, or
created
if parsing JSON. If
timestamp
is available in JSON, it's used instead of
created
.  If none of these are present, the
create_time
from the batch is used. Derived based on the presence of other fields: NETWORK_HTTP if
dst_ip
is present, USER_UNCATEGORIZED if
user_name
or (
associatedItems.0.typeName
is "USER" and
associatedItems.0.id
is present) is present, STATUS_UPDATE if
src_ip1
,
src_ip2
,
src_ip3
, or
remoteAddress
is present, or GENERIC_EVENT otherwise.  Overridden to USER_LOGIN if
auditType.action
contains "login". Always set to "ATLASSIAN_JIRA". Always set to "ATLASSIAN_JIRA". Set to "ALLOW" if
auditType.action
contains "login successful", "BLOCK" if
auditType.action
contains "login failed".
Need more help?
Get answers from Community members and Google SecOps professionals.
