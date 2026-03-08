# Collect Aqua Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aqua-security/  
**Scraped:** 2026-03-05T09:19:00.686726Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Aqua Security logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Aqua Security logs, transforming them into the Unified Data Model (UDM). It parses the
message
field as JSON, extracts user, source IP, and other relevant fields, maps them to UDM fields, and categorizes events based on the
action
field, enriching the data with security context like rule names, descriptions, and CVE details.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Aqua Security management console.
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
field, enter a name for the feed (for example,
Aqua Security Logs
).
Select
Webhook
as the
Source type
.
Select
Aqua Security
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
Creating a Webhook in Aqua Security for Google SecOps
Sign in to Aqua Security console.
Go to
Settings
>
Image Scan Results Webhook
.
Check the
Enable sending image scan results
checkbox.
Enter the
<ENDPOINT_URL>
, followed by
<API_KEY>
and
<SECRET>
.
Click
Save
.
UDM Mapping Table
Log Field (Ascending)
UDM Mapping
Logic
jsonPayload.action
metadata.event_type
Mapped based on the value of 'jsonPayload.action'. See parser code for specific mappings.
jsonPayload.action
security_result.summary
Directly mapped.
jsonPayload.adjective
target.file.full_path
Directly mapped if 'jsonPayload.container' is empty.
jsonPayload.category
target.asset.category
Directly mapped.
jsonPayload.cfappname
target.application
Directly mapped.
jsonPayload.cfspace
principal.user.userid
Directly mapped if 'jsonPayload.user' is empty.
jsonPayload.command
principal.ip
Extracted using grok pattern "user %{GREEDYDATA:user_id} \(%{IP:src_ip}\)".
jsonPayload.command
principal.user.userid
Extracted using grok pattern "user %{GREEDYDATA:user_id} \(%{IP:src_ip}\)".
jsonPayload.container
target.asset.product_object_id
Directly mapped.
jsonPayload.data
security_result.detection_fields
Parsed as key-value pairs and mapped to individual fields within 'security_result.detection_fields'.
jsonPayload.description
security_result.description
Directly mapped if 'jsonPayload.reason' is empty.
jsonPayload.host
principal.hostname
Directly mapped.
jsonPayload.hostgroup
target.group.group_display_name
Directly mapped.
jsonPayload.hostid
target.asset_id
Mapped as "host id: %{jsonPayload.hostid}".
jsonPayload.hostip
target.ip
Directly mapped.
jsonPayload.image
target.file.full_path
Directly mapped.
jsonPayload.level
security_result.action
Set to "ALLOW" if 'jsonPayload.level' is "success".
jsonPayload.reason
security_result.description
Directly mapped.
jsonPayload.rule
security_result.rule_name
Directly mapped.
jsonPayload.user
principal.user.userid
Directly mapped.
jsonPayload.vm_location
target.asset.location.name
Directly mapped.
jsonPayload.vm_name
target.resource.name
Directly mapped.
resource.labels.instance_id
target.resource.id
Directly mapped.
resource.labels.project_id
target.asset.attribute.cloud.project.id
Directly mapped.
resource.labels.zone
target.asset.attribute.cloud.availability_zone
Directly mapped.
timestamp
metadata.event_timestamp
Directly mapped after converting to ISO8601 format.
extensions.auth.type
Set to "SSO" if 'jsonPayload.description' contains "SAML", otherwise set to "AUTHTYPE_UNSPECIFIED" if 'jsonPayload.action' is "login" or "Login".
metadata.log_type
Set to "AQUA_SECURITY".
metadata.product_name
Set to "AQUA_SECURITY".
metadata.vendor_name
Set to "AQUA_SECURITY".
target.asset.attribute.cloud.environment
Set to "GOOGLE_CLOUD_PLATFORM".
target.resource.type
Set to "VIRTUAL_MACHINE".
Need more help?
Get answers from Community members and Google SecOps professionals.
