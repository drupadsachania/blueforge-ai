# Collect Fivetran logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran/  
**Scraped:** 2026-03-05T09:55:55.114793Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fivetran logs
Supported in:
Google secops
SIEM
This document explains how to configure Fivetran to push logs to Google Security Operations using webhooks.
Fivetran is a data integration platform that automates data pipelines from various sources to data warehouses. Fivetran generates operational events including connector sync events, transformation events, and connection status changes. These events can be sent to external endpoints via outbound webhooks for monitoring, alerting, and security analysis.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
A Fivetran account with admin or account-level permissions
Access to Google Cloud Console (for API key creation)
Fivetran account on Business Critical or Enterprise plan (for webhook functionality)
Create webhook feed in Google SecOps
Create the feed
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
Fivetran Events
).
Select
Webhook
as the
Source type
.
Select
Fivetran
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
(optional): Leave empty (each webhook request contains a single JSON event)
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Generate and save secret key
After creating the feed, you must generate a secret key for authentication:
On the feed details page, click
Generate Secret Key
.
A dialog displays the secret key.
Copy and save
the secret key securely.
Get the feed endpoint URL
Go to the
Details
tab of the feed.
In the
Endpoint Information
section, copy the
Feed endpoint URL
.
The URL format is:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
or
https://<REGION>-malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
Save this URL for the next steps.
Click
Done
.
Create Google Cloud API key
Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.
Create the API key
Go to the
Google Cloud Console Credentials page
.
Select your project (the project associated with your Google SecOps instance).
Click
Create credentials
>
API key
. An API key is created and displayed in a dialog.
Click
Edit API key
to restrict the key.
Restrict the API key
In the
API key
settings page:
Name
: Enter a descriptive name (for example,
Google SecOps Webhook API Key
)
Under
API restrictions
:
Select
Restrict key
.
In the
Select APIs
list, search for and select
Google SecOps API
(or
Chronicle API
).
Click
Save
.
Copy
the API key value from the
API key
field at the top of the page.
Save the API key securely.
Configure Fivetran webhook
Construct the webhook URL
Combine the Google SecOps endpoint URL and API key:
<ENDPOINT_URL>?key=<API_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
Create webhook using Fivetran REST API
Fivetran webhooks are configured via the REST API. You can create account-level webhooks (all groups) or group-level webhooks (specific destination group).
Get Fivetran API credentials
Sign in to your
Fivetran account
.
Click your username in the top-right corner.
Go to
Account Settings
>
API Config
.
If you don't have an API key:
Click
Generate API Key
.
Copy and save the
API Key
and
API Secret
securely.
Create account-level webhook
Use this method to receive events from all connectors across all groups in your account.
Open a terminal or API client.
Create the webhook using the following curl command:
curl
-X
POST
https://api.fivetran.com/v1/webhooks/account
\
-u
"API_KEY:API_SECRET"
\
-H
"Content-Type: application/json"
\
-H
"Accept: application/json"
\
-d
'{
"url": "https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_SECOPS_API_KEY",
"events": [
"sync_start",
"sync_end",
"transformation_start",
"transformation_succeeded",
"transformation_failed",
"connection_successful",
"connection_failure",
"create_connector",
"pause_connector",
"resume_connector",
"edit_connector",
"delete_connector",
"force_update_connector",
"resync_connector",
"resync_table"
],
"active": true,
"secret": "YOUR_SECOPS_SECRET_KEY"
}'
Replace the following values:
API_KEY
: Your Fivetran API key
API_SECRET
: Your Fivetran API secret
YOUR_SECOPS_API_KEY
: The Google Cloud API key created earlier
YOUR_SECOPS_SECRET_KEY
: The Google SecOps secret key from feed creation
The response will contain the webhook ID:
{
"code"
:
"Success"
,
"message"
:
"Operation performed."
,
"data"
:
{
"id"
:
"webhook_abc123"
,
"type"
:
"account"
,
"url"
:
"https://malachiteingestion-pa.googleapis.com/..."
,
"events"
:
[
"sync_start"
,
"sync_end"
,
...
],
"active"
:
true
,
"secret"
:
"******"
,
"created_at"
:
"2025-01-15T10:30:00Z"
,
"created_by"
:
"user_id"
}
}
Save the webhook ID for future reference.
Create group-level webhook (optional)
Use this method to receive events from connectors in a specific destination group.
Get your group ID:
Sign in to Fivetran.
Go to the destination group you want to monitor.
The group ID is in the URL:
https://fivetran.com/dashboard/groups/GROUP_ID
Create the webhook using the following curl command:
curl
-X
POST
https://api.fivetran.com/v1/webhooks/group/GROUP_ID
\
-u
"API_KEY:API_SECRET"
\
-H
"Content-Type: application/json"
\
-H
"Accept: application/json"
\
-d
'{
"url": "https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_SECOPS_API_KEY",
"events": [
"sync_start",
"sync_end",
"transformation_start",
"transformation_succeeded",
"transformation_failed",
"connection_successful",
"connection_failure"
],
"active": true,
"secret": "YOUR_SECOPS_SECRET_KEY"
}'
Replace
GROUP_ID
with your destination group ID.
Available webhook events
Select the events you want to monitor:
Event
Description
sync_start
Connector sync started
sync_end
Connector sync completed
transformation_start
Transformation started
transformation_succeeded
Transformation completed successfully
transformation_failed
Transformation failed
connection_successful
Connection test succeeded
connection_failure
Connection test failed
create_connector
New connector created
pause_connector
Connector paused
resume_connector
Connector resumed
edit_connector
Connector configuration edited
delete_connector
Connector deleted
force_update_connector
Connector force update triggered
resync_connector
Connector resync triggered
resync_table
Table resync triggered
Test the webhook
Test the webhook using the Fivetran API:
curl
-X
POST
https://api.fivetran.com/v1/webhooks/WEBHOOK_ID/test
\
-u
"API_KEY:API_SECRET"
\
-H
"Accept: application/json"
Replace
WEBHOOK_ID
with the webhook ID from the creation response.
Fivetran will send a test event to Google SecOps.
Verify the event in Google SecOps:
Go to
SIEM Settings
>
Feeds
.
Click your Fivetran feed.
Go to the
Logs
tab.
Verify that a test event was received.
Webhook payload format
Fivetran sends webhook events in the following JSON format:
{
"event"
:
"sync_end"
,
"created"
:
"2025-01-15T10:30:00.386Z"
,
"connector_type"
:
"salesforce"
,
"connector_id"
:
"mystified_presiding"
,
"connector_name"
:
"Salesforce Production"
,
"sync_id"
:
"abc123-def456-ghi789"
,
"destination_group_id"
:
"deck_enjoy"
,
"data"
:
{
"status"
:
"SUCCESSFUL"
}
}
Webhook authentication
Fivetran signs webhook payloads using HMAC SHA-256 with the secret you provided. The signature is sent in the
X-Fivetran-Signature-256
header.
Google SecOps automatically validates the signature using the secret key configured during feed creation.
Webhook retry behavior
Fivetran automatically retries failed webhooks:
Retry
Time After Initial Attempt
Initial attempt
0 minutes
1st retry
6 minutes
2nd retry
27 minutes
3rd retry
1 hour 45 minutes
4th retry
6 hours 25 minutes
5th retry
23 hours 13 minutes
Fivetran retries for up to 24 hours.
Webhooks have a 10-second timeout.
Webhooks are automatically deactivated after 3 days of consistent failures.
Manage webhooks
List all webhooks
bash
curl -X GET https://api.fivetran.com/v1/webhooks \
    -u "API_KEY:API_SECRET" \
    -H "Accept: application/json"
Get webhook details
bash
curl -X GET https://api.fivetran.com/v1/webhooks/WEBHOOK_ID \
    -u "API_KEY:API_SECRET" \
    -H "Accept: application/json"
Update webhook
bash
curl -X PATCH https://api.fivetran.com/v1/webhooks/WEBHOOK_ID \
    -u "API_KEY:API_SECRET" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{
        "active": true,
        "events": ["sync_start", "sync_end"]
    }'
Delete webhook
bash
curl -X DELETE https://api.fivetran.com/v1/webhooks/WEBHOOK_ID \
    -u "API_KEY:API_SECRET" \
    -H "Accept: application/json"
Authentication methods reference
Google SecOps webhook feeds support multiple authentication methods. Choose the method that your vendor supports.
Method 1: Query parameters (Recommended for Fivetran)
Fivetran does not support custom HTTP headers for outbound webhooks. Use query parameters to pass credentials.
URL format:
<ENDPOINT_URL>?key=<API_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
Authentication:
API key in URL query parameter
Secret key validated via HMAC signature in
X-Fivetran-Signature-256
header
Method 2: Custom headers (Not supported by Fivetran)
Fivetran outbound webhooks don't support custom HTTP headers. Use Method 1 instead.
Webhook limits and best practices
Request limits
Limit
Value
Max request size
4 MB
Max QPS (queries per second)
15,000
Request timeout
10 seconds (Fivetran) / 30 seconds (Google SecOps)
Retry behavior
Automatic with exponential backoff
Best practices
Subscribe only to events you need to minimize HTTP requests.
Monitor webhook delivery status in Fivetran dashboard.
Set up alerting for webhook deactivation.
Use account-level webhooks for centralized monitoring.
Use group-level webhooks for specific destination monitoring.
Regularly review and update event subscriptions.
Troubleshooting
Webhook creation fails
Error:
HTTP 400 Bad Request during webhook creation.
Cause:
Google SecOps endpoint is not reachable or returns non-2xx status.
Solution:
Verify the Google SecOps endpoint URL is correct.
Verify the API key is valid and has Google SecOps API access.
Test the endpoint manually:
curl
-X
POST
"https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_API_KEY"
\
-H
"Content-Type: application/json"
\
-H
"x-chronicle-auth: YOUR_SECRET_KEY"
\
-d
'{"test": "event"}'
Create the webhook with
"active": false
to skip initial validation, then activate it later.
Webhook is deactivated
Cause:
Webhook consistently failed for more than 3 days.
Solution:
Verify Google SecOps feed is active and healthy.
Check Google SecOps feed logs for errors.
Verify API key and secret key are still valid.
Reactivate the webhook:
curl
-X
PATCH
https://api.fivetran.com/v1/webhooks/WEBHOOK_ID
\
-u
"API_KEY:API_SECRET"
\
-H
"Content-Type: application/json"
\
-d
'{"active": true}'
Events not appearing in Google SecOps
Cause:
Events are being sent but not ingested.
Solution:
Go to
SIEM Settings
>
Feeds
in Google SecOps.
Click your Fivetran feed.
Go to the
Logs
tab.
Check for ingestion errors.
Verify the log type is set to
Fivetran
.
Verify the secret key matches the one configured in the webhook.
HMAC signature validation fails
Cause:
Secret key mismatch.
Solution:
Verify the secret key in Google SecOps feed matches the one used in webhook creation.
Regenerate the Google SecOps secret key if needed.
Update the Fivetran webhook with the new secret:
curl
-X
PATCH
https://api.fivetran.com/v1/webhooks/WEBHOOK_ID
\
-u
"API_KEY:API_SECRET"
\
-H
"Content-Type: application/json"
\
-d
'{"secret": "NEW_SECOPS_SECRET_KEY"}'
UDM mapping table
Log field
UDM mapping
Logic
jsonPayload.connector_id
additional.connector_id
Value copied directly
jsonPayload.connector_type
additional.connector_type
Value copied directly
jsonPayload.data.executionTime
additional.executionTime
Converted to string
insertId
additional.insertId
Value copied if not empty
labels.levelName
additional.levelName
Value copied if not empty
labels.levelValue
additional.levelValue
Value copied if not empty
jsonPayload.data.number
additional.number
Converted to string
jsonPayload.data.query
additional.query
Value copied directly
resource.type
additional.type
Value copied if not empty
metadata.event_type
Set to "RESOURCE_READ" if has_principal_user == "true" and has_target == "true", else if has_principal_user == "true" then "USER_COMMUNICATION", else if has_principal == "true" then "STATUS_UPDATE", else "GENERIC_EVENT"
jsonPayload.event
metadata.product_event_type
Value copied directly
jsonPayload.sync_id
metadata.product_log_id
Value copied directly
jsonPayload.connector_name
principal.asset.hostname
Value copied directly
jsonPayload.connector_name
principal.hostname
Value copied directly
resource.labels.email_id
principal.user.email_addresses
Merged if matches "^.+@.+$"
resource.labels.project_id
principal.user.product_object_id
Value copied if not empty
resource.labels.unique_id
principal.user.userid
Value copied if not in ["", "null", " "]
severity
security_result.severity
Set to "INFORMATIONAL" if matches "INFO"
logName
target.resource.name
Value copied if not empty
target.resource.type
Set to "DATABASE"
metadata.product_name
Set to "FIVETRAN"
metadata.vendor_name
Set to "FIVETRAN"
Need more help?
Get answers from Community members and Google SecOps professionals.
