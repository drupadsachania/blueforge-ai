# Collect Onfido logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onfido/  
**Scraped:** 2026-03-05T09:58:54.846169Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Onfido logs
Supported in:
Google secops
SIEM
This parser extracts fields from Onfido SYSLOG and JSON formatted logs, mapping them to the UDM. It parses the message field using grok, handles JSON payloads if present, and maps specific product event types to UDM event types. This includes setting the event type to
USER_LOGIN
for successful logins and
USER_UNCATEGORIZED
for other events. It also populates UDM fields for user information, source IP, and security result details.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Onfido Dashboard.
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
Onfido Logs
.
Select
Webhook
as the
Source type
.
Select
Onfido
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
: the API key to authenticate to Google SecOps.
SECRET
: the secret key that you generated to authenticate the feed.
Configure the Onfido webhook
Sign in to the Onfido Dashboard.
Go to
Settings
>
Webhooks
.
Click
Add Webhook
.
Specify values for the following input parameters:
Webhook URL
: enter the
<ENDPOINT_URL>
of the Google SecOps API endpoint.
Events:
select the events that should trigger the webhook (for example, select
check.completed
or
report.completed
).
Click
Save
to create the webhook.
UDM Mapping Table
Log Field
UDM Mapping
Logic
category
security_result.category_details
The value of the
category
field from the raw log is assigned to
security_result.category_details
.
check_id
metadata.product_log_id
The value of the
check_id
field extracted from the
json_data
field in the raw log is assigned to
metadata.product_log_id
. If
prod_evt_type
is "Successful login", the value "AUTHTYPE_UNSPECIFIED" is assigned.
metadata.event_timestamp
The timestamp from the raw log entry is converted to epoch seconds and assigned to
metadata.event_timestamp
.
metadata.event_type
If
prod_evt_type
is "Successful login", the value
USER_LOGIN
is assigned. Otherwise,
USER_UNCATEGORIZED
is assigned.
metadata.product_name
The parser code sets the value to "ONFIDO".
prod_evt_type
metadata.product_event_type
The value of the
prod_evt_type
field from the raw log is assigned to
metadata.product_event_type
.
metadata.vendor_name
The parser code sets the value to "ONFIDO".
metadata.product_version
The parser code sets the value to "ONFIDO".
security_result.action
security_result.action
If
prod_evt_type
is "Successful login", the value
ALLOW
is assigned.
src_ip
principal.ip
The value of the
src_ip
field from the raw log is assigned to
principal.ip
.
user_email
target.user.email_addresses
The value of the
user_email
field from the raw log is assigned to
target.user.email_addresses
.
user_name
target.user.user_display_name
The value of the
user_name
field from the raw log is assigned to
target.user.user_display_name
.
Need more help?
Get answers from Community members and Google SecOps professionals.
