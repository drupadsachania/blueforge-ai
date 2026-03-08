# Collect OneLogin Single Sign-On (SSO) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onelogin-sso/  
**Scraped:** 2026-03-05T09:58:50.649709Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect OneLogin Single Sign-On (SSO) logs
Supported in:
Google secops
SIEM
This document describes how you can collect OneLogin Single Sign-On (SSO) logs
by configuring OneLogin Event Webhooks and Google Security Operations HTTPS Webhooks.
For more information, see
Data ingestion to Google Security Operations
.
Configure Google SecOps HTTPS Webhook
Create an HTTPS webhook feed
From the Google Security Operations menu, select
Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed.
In the
Source Type
list, select
Webhook
.
Select
OneLogin
as the
Log type
.
Click
Next
.
Optional: Enter values for the following input parameters:
Split delimiter
:
\n
.
Asset namespace
: the asset namespace.
Ingestion labels
: the label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key as you cannot view this secret again. You can
generate a new secret key, but regeneration of the secret key makes the
previous secret key obsolete.
From the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. Enter this endpoint URL in your OneLogin Event Webhook.
Click
Done
.
Create an API key for the HTTPS webhook feed
Go to the Google Cloud console console Credentials page.
Click
Create credentials
, and then select API key.
Copy and store the API key.
Restrict the API key access to the Chronicle API.
Configure OneLogin Event Webhook
The OneLogin Event Webhook lets you stream OneLogin event data to
Google Security Operations which accepts data in JSON format.
This integration lets you monitor activities, alert on threats, and execute
event-based identity related workflows across your OneLogin and Google Security Operations environment.
Log on to the OneLogin admin portal.
Go to the Developers tab >
Webhooks
>
New Webhook
, and then choose
Event Webhook for Log Management
.
Enter the following details:
In the
Name
field, enter
Google SecOps
.
In the
Format
field, enter
SIEM (NDJSON)
.
In the
Listener URL
, enter the Google SecOps Webhook endpoint that will receive the event data from OneLogin.
In the
Custom Headers
, enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key:API_KEY
X-Webhook-Access-Key:SECRET
Click
Save
. Refresh the page to see the new webhook in your OneLogin Event Broadcasters as connected.
Need more help?
Get answers from Community members and Google SecOps professionals.
