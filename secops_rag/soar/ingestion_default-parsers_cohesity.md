# Collect Cohesity logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cohesity/  
**Scraped:** 2026-03-05T09:53:27.427958Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cohesity logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Cohesity backup software syslog messages using grok patterns. It handles both standard syslog messages and JSON-formatted logs, mapping extracted fields to the UDM and dynamically assigning an
event_type
based on the presence of principal and target identifiers.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Cohesity management.
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
field, feed (for example,
Cohesity Logs
).
Select
Webhook
as the
Source type
.
Select
Cohesity
as the
Log type
.
Click
Next
.
Optional: Specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
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
From the
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
Go to Credentials
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Chronicle API
.
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL.
If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google SecOps.
SECRET
: the secret key that you generated to authenticate the feed.
Configuring a Webhook in Cohesity for Google SecOps
Sign in to the Cohesity cluster management.
Go to the
Protection Jobs
section.
Select the protection job for which you want to configure the webhook.
Click
Actions
menu (three vertical dots) next to the protection job
>
Edit
.
Select the
Alerting
tab.
Click
+ Add Webhook
.
Specify values for the following parameters:
Name
: Provide a descriptive name for the webhook (for example,
Google SecOps
).
URL
: Enter the Google SecOps
<ENDPOINT_URL>
.
Method
: Select
POST
.
Content Type
: Select
application/json
.
Payload
: This field depends on the specific data you want to send.
Enable Webhook
: Check the box to
enable
the webhook.
Save the Configuration:
Click
Save
to apply the webhook configuration to the protection job.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ClientIP
principal.asset.ip
Directly mapped from
ClientIP
field.
ClientIP
principal.ip
Directly mapped from
ClientIP
field.
description
security_result.description
Directly mapped from
description
field.
DomainName
target.asset.hostname
Directly mapped from
DomainName
field.
DomainName
target.hostname
Directly mapped from
DomainName
field.
EntityPath
target.url
Directly mapped from
EntityPath
field.
host
principal.asset.hostname
Directly mapped from
host
field.
host
principal.hostname
Directly mapped from
host
field. Copied from the
ts
field after it's parsed to a timestamp. Determined by parser logic based on the presence of
principal_mid_present
,
target_mid_present
, and
principal_user_present
.  Possible values:
NETWORK_CONNECTION
,
USER_UNCATEGORIZED
,
STATUS_UPDATE
,
GENERIC_EVENT
. Hardcoded to "Cohesity".
product_event_type
metadata.product_event_type
Directly mapped from
product_event_type
field. Hardcoded to "COHESITY".
pid
principal.process.pid
Directly mapped from
pid
field.
Protocol
network.application_protocol
Directly mapped from
Protocol
field, converted to uppercase.
RecordID
additional.fields
(key: "RecordID", value:
RecordID
)
Directly mapped from
RecordID
field, nested under
additional.fields
.
RequestType
security_result.detection_fields
(key: "RequestType", value:
RequestType
)
Directly mapped from
RequestType
field, nested under
security_result.detection_fields
.
Result
security_result.summary
Directly mapped from
Result
field.
sha_value
additional.fields
(key: "SHA256", value:
sha_value
)
Directly mapped from
sha_value
field, nested under
additional.fields
.
target_ip
target.asset.ip
Directly mapped from
target_ip
field.
target_ip
target.ip
Directly mapped from
target_ip
field.
target_port
target.port
Directly mapped from
target_port
field, converted to integer.
Timestamp
metadata.collected_timestamp
Directly mapped from
Timestamp
field after it's parsed to a timestamp.
ts
events.timestamp
Directly mapped from
ts
field after it's parsed to a timestamp.
UserID
principal.user.userid
Directly mapped from
UserID
field, converted to string.
UserName
principal.user.user_display_name
Directly mapped from
UserName
field.
UserSID
principal.user.windows_sid
Directly mapped from
UserSID
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
