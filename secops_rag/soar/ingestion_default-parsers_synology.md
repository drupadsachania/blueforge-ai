# Collect Synology logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/synology/  
**Scraped:** 2026-03-05T10:00:53.852138Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Synology logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Synology SYSLOG messages using grok patterns, mapping them to the UDM. It handles various log formats, identifies user logins and resource access, and categorizes events based on keywords, enriching the data with vendor and product information.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Synology DSM.
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
Synology Logs
.
Select
Webhook
as the
Source type
.
Select
Synology
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
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Creating a Webhook in Synology for Google SecOps
Sign in to DiskStation Manager (DSM) on your Synology NAS.
Go to
Control Panel
>
Notification
>
Webhook
.
Click
Add
.
Specify values for the following parameters:
Provider
: Select
Custom
.
Rule
: Select what kind of messages you want to send in your webhook.
Click
Next
.
Provider name
: Give the webhook a distinctive name (for example,
Google SecOps
).
Subject
: Will be added as a prefix of the notification message.
Webhook URL
: Enter
ENDPOINT_URL
.
Select
Send notification messages in English
.
Click
Next
.
HTTP Method
: Select
POST
.
Add Header
X-Webhook-Access-Key
, with
SECRET
value.
Add Header
X-goog-api-key
, with
API_KEY
value.
Click
Apply
.
Click
Apply
to save the webhook.
UDM Mapping Table
Log field
UDM mapping
Logic
app
target.application
The value of the
app
field extracted by the grok filter is assigned to
target.application
.
desc
metadata.description
The value of the
desc
field extracted by the grok filter is assigned to
metadata.description
.
desc
target.file.names
If the
desc
field contains "Closed)", the file path within the parentheses is extracted and assigned to
target.file.names
.  If the
desc
field contains "accessed shared folder", the folder path within the brackets is extracted and assigned to
target.file.names
.
host
principal.hostname
The value of the
host
field extracted by the grok filter from the
host_and_ip
field is assigned to
principal.hostname
.
host_and_ip
principal.ip
The
host_and_ip
field is parsed. If an IP address (
ip1
) is found, it's assigned to
principal.ip
. If a second IP address (
ip2
) is found, it's also added to
principal.ip
.
intermediary_host
intermediary.hostname
The value of the
intermediary_host
field extracted by the grok filter is assigned to
intermediary.hostname
. An empty
auth
object is created within
extensions
if the message contains "signed in" or "sign in". The timestamp from the raw log's
collection_time
field is used. If the message contains "signed in" or "sign in", the value is set to
USER_LOGIN
. If the message contains "accessed shared folder", the value is set to
USER_RESOURCE_ACCESS
. Otherwise, it defaults to
GENERIC_EVENT
. The value of the
type
field extracted by the grok filter is assigned to
metadata.product_event_type
. The value is statically set to "SYNOLOGY". The value is statically set to "SYNOLOGY". If the message contains "failed to sign", the value is set to
BLOCK
. If the message contains "success", the value is set to
ALLOW
. If the
severity
field (extracted by grok) is "INFO", the value is set to
INFORMATIONAL
.
severity
security_result.severity
The value of the
severity
field extracted by the grok filter is used to determine the
security_result.severity
. If the value is "INFO", it's mapped to "INFORMATIONAL".
time
metadata.event_timestamp
The
time
field, extracted by the grok filter, is parsed and converted to a timestamp. This timestamp is then assigned to
metadata.event_timestamp
.
type
metadata.product_event_type
The value of the
type
field extracted by the grok filter is assigned to
metadata.product_event_type
.
user
target.administrative_domain
If a domain is extracted from the
user
field, it's assigned to
target.administrative_domain
.
user
target.user.userid
The username part of the
user
field (before the "\" if present) is extracted and assigned to
target.user.userid
. The timestamp from the raw log's
collection_time
field is used.
Need more help?
Get answers from Community members and Google SecOps professionals.
