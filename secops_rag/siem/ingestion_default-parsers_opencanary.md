# Collect OpenCanary logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opencanary/  
**Scraped:** 2026-03-05T09:27:08.899689Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect OpenCanary logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from OpenCanary SYSLOG and JSON logs, normalizes them into the UDM format, and enriches the data with derived fields like
metadata.event_type
and
security_result.severity
. It handles various log formats, performs IP address validation, and maps fields to appropriate UDM objects like
principal
,
target
, and
network
.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to OpenCanary.
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
OpenCanary Logs
.
Select
Webhook
as the
Source type
.
Select
OpenCanary
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
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Setting up an OpenCanary Webhook for Google SecOps
Find the OpenCanary configuration file,
config.json
.
Open
config.json
file with a text editor.
Find the section labeled
alerters
within the configuration file.
If a
webhook
alerter already exists, modify it. Otherwise, add a new entry for the
webhook
alerter.
Use the following configuration (replace
ENDPOINT_URL
,
SECRET
and
API_KEY
with your values):
"handlers"
:
{
"Webhook"
:
{
"class"
:
"opencanary.logger.WebhookHandler"
,
"url"
:
"<ENDPOINT_URL>"
,
"method"
:
"POST"
,
"data"
:
{
"message"
:
"%(message)s"
},
"status_code"
:
200
,
"headers"
:
{
"X-Webhook-Access-Key"
:
"<SECRET>"
,
"X-goog-api-key"
:
"<API_KEY>"
}
}
}
Save the
config.json
file.
Restart the OpenCanary service to apply the changes. (for example,
sudo systemctl restart opencanary
).
UDM Mapping Table
Log Field
UDM Mapping
Logic
dst_host
target.asset.ip
The raw log's
dst_host
field is mapped to the UDM. Also mapped to
target.ip
.
dst_host
target.ip
The raw log's
dst_host
field is mapped to the UDM. Also mapped to
target.asset.ip
.
dst_port
target.port
The raw log's
dst_port
field is converted to a string and then to an integer and mapped to the UDM.
local_time
metadata.event_timestamp
The raw log's
local_time
field is used to populate the
metadata.event_timestamp
in the UDM. The parser uses the
create_time
from the batch object if the
local_time
field is not present.
local_time_adjusted
security_result.detection_fields
The raw log's
local_time_adjusted
field is added as a key-value pair to the
security_result.detection_fields
array in the UDM.
logdata.COMMUNITY_STRING
security_result.detection_fields
The raw log's
logdata.COMMUNITY_STRING
field is added as a key-value pair to the
security_result.detection_fields
array in the UDM.
logdata.DOMAIN
principal.administrative_domain
The raw log's
logdata.DOMAIN
field is mapped to the UDM.
logdata.FILENAME
target.file.full_path
The raw log's
logdata.FILENAME
field is mapped to the UDM.
logdata.HOSTNAME
principal.asset.hostname
If the
logdata.HOSTNAME
field is not an IP address, it's mapped to the UDM. Also mapped to
principal.hostname
.
logdata.HOSTNAME
principal.asset.ip
If the
logdata.HOSTNAME
field is an IP address, it's mapped to the UDM. Also mapped to
principal.ip
.
logdata.HOSTNAME
principal.hostname
If the
logdata.HOSTNAME
field is not an IP address, it's mapped to the UDM. Also mapped to
principal.asset.hostname
.
logdata.HOSTNAME
principal.ip
If the
logdata.HOSTNAME
field is an IP address, it's mapped to the UDM. Also mapped to
principal.asset.ip
.
logdata.LOCALNAME
principal.asset.hostname
The raw log's
logdata.LOCALNAME
field is mapped to the UDM. Also mapped to
principal.hostname
.
logdata.LOCALNAME
principal.hostname
The raw log's
logdata.LOCALNAME
field is mapped to the UDM. Also mapped to
principal.asset.hostname
.
logdata.LOCALVERSION
principal.platform_version
The raw log's
logdata.LOCALVERSION
field is mapped to the UDM.
logdata.PASSWORD
extensions.auth.mechanism
The presence of the
logdata.PASSWORD
field triggers the parser to set the
extensions.auth.mechanism
to
USERNAME_PASSWORD
in the UDM.
logdata.PATH
network.http.referral_url
The raw log's
logdata.PATH
field is mapped to the UDM.
logdata.REMOTENAME
target.asset.hostname
The raw log's
logdata.REMOTENAME
field is mapped to the UDM. Also mapped to
target.hostname
.
logdata.REMOTENAME
target.hostname
The raw log's
logdata.REMOTENAME
field is mapped to the UDM. Also mapped to
target.asset.hostname
.
logdata.REMOTEVERSION
target.platform_version
The raw log's
logdata.REMOTEVERSION
field is mapped to the UDM.
logdata.SMBVER
network.application_protocol
The presence of the
logdata.SMBVER
field triggers the parser to set the
network.application_protocol
to
SMB
in the UDM.
logdata.USERAGENT
network.http.parsed_user_agent
The raw log's
logdata.USERAGENT
field is converted to a parsed user agent and mapped to the UDM.
logdata.USERAGENT
network.http.user_agent
The raw log's
logdata.USERAGENT
field is mapped to the UDM.
logdata.USERNAME
target.user.userid
The raw log's
logdata.USERNAME
field is mapped to the UDM.
loglevel
security_result.severity
The raw log's
loglevel
field determines the
security_result.severity
in the UDM.
WARNING
maps to
HIGH
,
INFO
/
INFORMATION
maps to
LOW
.
logtype
security_result.detection_fields
The raw log's
logtype
field is added as a key-value pair to the
security_result.detection_fields
array in the UDM.
node_id
principal.asset.asset_id
The raw log's
node_id
field is prepended with "id:" and mapped to the UDM.
src_host
principal.asset.ip
The raw log's
src_host
field is mapped to the UDM. Also mapped to
principal.ip
.
src_host
principal.ip
The raw log's
src_host
field is mapped to the UDM. Also mapped to
principal.asset.ip
.
src_port
principal.port
The raw log's
src_port
field is converted to an integer and mapped to the UDM.
utc_time
security_result.detection_fields
The raw log's
utc_time
field is added as a key-value pair to the
security_result.detection_fields
array in the UDM.
Need more help?
Get answers from Community members and Google SecOps professionals.
