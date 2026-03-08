# Collect Cloudflare logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare/  
**Scraped:** 2026-03-05T09:22:17.661199Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloudflare logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cloudflare logs to Google Security Operations
using either Webhook (HTTP destination) or Google Cloud Storage. Cloudflare
produces operational data in the form of logs for DNS, HTTP, Audit, Zero Trust,
and CASB. This integration lets you send these logs to Google SecOps
for analysis and monitoring. The parser first initializes a set of empty fields
and then parses JSON-formatted Cloudflare logs, dropping any messages that aren't
valid JSON. The code then uses conditional logic based on the presence and values
of specific fields to determine the Cloudflare product and event type, populating
the Unified Data Model (UDM) fields accordingly.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Cloudflare Enterprise account with LogPush enabled.
For Webhook method: Privileged access to Google Cloud console.
For Google Cloud Storage method: Privileged access to Google Cloud Storage.
Method 1: Configure Cloudflare logs export using Webhook (HTTP destination)
This method lets you stream Cloudflare logs directly to Google SecOps
without intermediate storage.
Configure a Webhook feed in Google SecOps
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed (for example,
Cloudflare Webhook
).
Select
Webhook
as the
Source type
.
Select
Cloudflare
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
:
\n
.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy
and
save
the secret key as you cannot view this secret again.
Go to the
Details
tab.
Copy
the feed endpoint URL from the
Endpoint Information
field.
Click
Done
.
Create an API key for the Webhook feed
Go to
Google Cloud console
>
APIs & services
>
Credentials
.
Click
Create credentials
, and then select
API key
.
Click
Edit API key
.
Under
API restrictions
, select
Restrict key
.
Select
Google SecOps API
from the list.
Click
Save
.
Copy
the API key value.
Configure Cloudflare LogPush HTTP destination
Sign in to the
Cloudflare dashboard
.
Select the
Enterprise account
or
domain
you want to use with LogPush.
Go to
Analytics & Logs
>
Logpush
.
Click
Create a Logpush job
.
In
Select a destination
, choose
HTTP destination
.
Enter the HTTP endpoint URL with authentication parameters:
<ENDPOINT_URL>?header_X-goog-api-key=<API_KEY>&header_X-Webhook-Access-Key=<SECRET_KEY>
Replace the following:
<ENDPOINT_URL>
: the feed endpoint URL from Google SecOps.
<API_KEY>
: the API key from Google Cloud console (URL-encoded if contains special characters).
<SECRET_KEY>
: the secret key from the Webhook feed (URL-encoded if contains special characters).
Click
Continue
.
Select the dataset to push (for example,
HTTP requests
,
DNS
,
Audit
,
Zero Trust
,
CASB
).
Configure your logpush job:
Enter the
Job name
.
Optional: Under
If logs match
, configure filters.
In
Send the following fields
, select the fields to include.
Choose the timestamp format (
RFC3 339
recommended).
Configure sampling rate if needed.
Click
Submit
to create the logpush job.
Verify the webhook integration
After configuration, logs should appear in Google SecOps within minutes. To verify:
Go to
Investigation
>
SIEM Search
.
Search for logs with your configured ingestion label.
Confirm Cloudflare logs are being parsed correctly.
Method 2: Configure Cloudflare logs export using Google Cloud Storage
Configure Cloudflare to push logs to it, which involves granting Cloudflare the
necessary permissions.
Create a Google Cloud Bucket
Sign in to the
Google Cloud console
.
Go to the
Cloud Storage Buckets
page.
Click
Create
.
On the
Create a bucket
page, enter your bucket information:
Name
: Enter a unique name that meets the bucket name requirements (for example,
cloudflare-data
).
Location type
: Select a location type and region.
To enable hierarchical namespace, click the expander arrow to expand
Optimize for file oriented and data-intensive workloads
, and then select
Enable Hierarchical namespace on this bucket
.
Click
Create
.
Grant permissions to the bucket
In the
Cloud Storage console
, select the bucket that you previously created.
Click the
Permissions
tab.
Click
Grant access
.
Add the account
logpush@cloudflare-data.iam.gserviceaccount.com
with
Storage Object Admin
permission.
Click
Save
.
Configure Cloudflare LogPush to Google Cloud Storage
Sign in to the
Cloudflare dashboard
.
Select the
Enterprise account
or
domain
you want to use with LogPush.
Go to
Analytics & Logs
>
Logpush
.
Click
Create a Logpush job
.
In
Select a destination
, choose
Google Cloud Storage
.
Enter your Google Cloud Storage bucket path (for example,
gs://cloudflare-data/logs/
).
Click
Continue
.
Enter the
Ownership Token
and click
Continue
.
Select the dataset to push to the storage.
Configure your logpush job:
Enter the
Job name
.
Under
If logs match
, you can select the events to include or remove from your logs.
In
Send the following fields
, choose which logs to push.
Choose the timestamp format (
RFC 339
recommended).
Configure sampling rate if needed.
Click
Submit
.
Configure a feed in Google SecOps to ingest Cloudflare logs from Google Cloud Storage
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed (for example,
Cloudflare GCS Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cloudflare
as the
Log type
.
Click
Get Service Account
.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Google Cloud bucket URL in
gs://my-bucket/<value>/
format. This URL must end with a trailing forward slash (/).
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM mapping table
Log field
UDM mapping
Logic
ClientIP
read_only_udm.principal.asset.ip
read_only_udm.principal.ip
The value is taken from the ClientIP field.
ClientRequestHost
read_only_udm.target.asset.hostname
read_only_udm.target.hostname
The value is taken from the ClientRequestHost field.
ClientRequestMethod
read_only_udm.network.http.method
The value is taken from the ClientRequestMethod field.
ClientRequestURI
read_only_udm.target.url
The value is taken from the ClientRequestURI field. If the ClientRequestHost field is not empty, the value is concatenated with the ClientRequestHost field.
ClientSrcPort
read_only_udm.principal.port
The value is taken from the ClientSrcPort field.
ClientRequestUserAgent
read_only_udm.network.http.user_agent
The value is taken from the ClientRequestUserAgent field.
ClientSSLCipher
read_only_udm.network.tls.cipher
The value is taken from the ClientSSLCipher field.
ClientSSLProtocol
read_only_udm.network.tls.version
The value is taken from the ClientSSLProtocol field.
Country
read_only_udm.target.location.country_or_region
The value is taken from the Country field.
CreatedAt
read_only_udm.metadata.event_timestamp
The value is taken from the CreatedAt field.
Datetime
read_only_udm.metadata.event_timestamp
The value is taken from the Datetime field.
DestinationIP
read_only_udm.target.asset.ip
read_only_udm.target.ip
The value is taken from the DestinationIP field.
DestinationPort
read_only_udm.target.port
The value is taken from the DestinationPort field.
DeviceID
read_only_udm.principal.asset_id
The value is taken from the DeviceID field and is prefixed with "Cloudflare:".
DeviceName
read_only_udm.principal.asset.hostname
read_only_udm.principal.hostname
The value is taken from the DeviceName field.
DstIP
read_only_udm.target.asset.ip
read_only_udm.target.ip
The value is taken from the DstIP field.
DstPort
read_only_udm.target.port
The value is taken from the DstPort field.
EdgeResponseBytes
read_only_udm.network.received_bytes
The value is taken from the EdgeResponseBytes field.
EdgeResponseStatus
read_only_udm.network.http.response_code
The value is taken from the EdgeResponseStatus field.
EdgeServerIP
read_only_udm.target.asset.ip
read_only_udm.target.ip
The value is taken from the EdgeServerIP field.
Email
read_only_udm.principal.user.email_addresses
read_only_udm.target.user.email_addresses
The value is taken from the Email field.
FirewallMatchesActions
read_only_udm.security_result.action
The value is set to "ALLOW" if the FirewallMatchesAction field is "allow", "Allow", "ALLOW", "skip", "SKIP", or "Skip", "ALLOW_WITH_MODIFICATION" if the FirewallMatchesAction field is "challengeSolved" or "jschallengeSolved", "BLOCK" if the FirewallMatchesAction field is "drop" or "block", "UNKNOWN_ACTION" if the FirewallMatchesAction field is not empty.
FirewallMatchesRuleIDs
read_only_udm.security_result.rule_id
The value is taken from the FirewallMatchesRuleIDs field.
FirewallMatchesSources
read_only_udm.security_result.rule_name
The value is taken from the FirewallMatchesSources field.
HTTPMethod
read_only_udm.network.http.method
The value is taken from the HTTPMethod field.
HTTPHost
read_only_udm.target.hostname
The value is taken from the HTTPHost field.
HTTPVersion
read_only_udm.network.application_protocol
The value is taken from the HTTPVersion field. If the value contains "HTTP", it is replaced with "HTTP".
IPAddress
read_only_udm.target.asset.ip
read_only_udm.target.ip
The value is taken from the IPAddress field.
IsIsolated
read_only_udm.about.labels
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the IsIsolated field and is converted to a string.
Location
read_only_udm.principal.location.name
The value is taken from the Location field.
OriginIP
read_only_udm.intermediary.ip
read_only_udm.target.asset.ip
read_only_udm.target.ip
The value is taken from the OriginIP field.
OriginPort
read_only_udm.target.port
The value is taken from the OriginPort field.
OwnerID
read_only_udm.target.user.product_object_id
The value is taken from the OwnerID field.
Policy
read_only_udm.security_result.rule_name
The value is taken from the Policy field.
PolicyID
read_only_udm.security_result.rule_id
The value is taken from the PolicyID field.
PolicyName
read_only_udm.security_result.rule_name
The value is taken from the PolicyName field.
Protocol
read_only_udm.network.ip_protocol
The value is taken from the Protocol field and is converted to uppercase.
QueryCategoryIDs
read_only_udm.security_result.about.labels
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the QueryCategoryIDs field.
QueryName
read_only_udm.network.dns.questions.name
The value is taken from the QueryName field.
QueryNameReversed
read_only_udm.network.dns.questions.name
The value is taken from the QueryNameReversed field.
QuerySize
read_only_udm.network.sent_bytes
The value is taken from the QuerySize field.
QueryType
read_only_udm.network.dns.questions.type
The value is taken from the QueryType field. If the value is one of the known DNS record types, it is mapped to its corresponding numeric value. Otherwise, the value is converted to a string.
RData
read_only_udm.network.dns.answers
The value is taken from the RData field. The type field is converted to an unsigned integer.
RayID
read_only_udm.metadata.product_log_id
The value is taken from the RayID field.
Referer
read_only_udm.network.http.referral_url
The value is taken from the Referer field.
RequestID
read_only_udm.metadata.product_log_id
The value is taken from the RequestID field.
ResolverDecision
read_only_udm.security_result.summary
The value is taken from the ResolverDecision field.
ResourceID
read_only_udm.target.resource.id
read_only_udm.target.resource.product_object_id
The value is taken from the ResourceID field.
ResourceType
read_only_udm.target.resource.resource_subtype
The value is taken from the ResourceType field.
SNI
read_only_udm.network.tls.client.server_name
The value is taken from the SNI field.
SecurityAction
read_only_udm.security_result.action
The value is set to "ALLOW" if the SecurityAction field is empty or the sec_action field is empty, "ALLOW_WITH_MODIFICATION" if the SecurityAction field is "challengeSolved" or "jschallengeSolved", "BLOCK" if the SecurityAction field is "drop" or "block".
SecurityLevel
read_only_udm.security_result.severity
The value is taken from the SecurityLevel field and is mapped to its corresponding UDM severity value.
SessionID
read_only_udm.network.session_id
The value is taken from the SessionID field.
SessionStartTime
read_only_udm.metadata.event_timestamp
The value is taken from the SessionStartTime field.
SourceIP
read_only_udm.principal.asset.ip
read_only_udm.principal.ip
read_only_udm.src.asset.ip
read_only_udm.src.ip
The value is taken from the SourceIP field.
SourcePort
read_only_udm.principal.port
read_only_udm.src.port
The value is taken from the SourcePort field.
SrcIP
read_only_udm.principal.asset.ip
read_only_udm.principal.ip
The value is taken from the SrcIP field.
SrcPort
read_only_udm.principal.port
The value is taken from the SrcPort field.
TemporaryAccessDuration
read_only_udm.network.session_duration.seconds
The value is taken from the TemporaryAccessDuration field.
Timestamp
read_only_udm.metadata.event_timestamp
The value is taken from the Timestamp field.
Transport
read_only_udm.network.ip_protocol
The value is taken from the Transport field and is converted to uppercase.
URL
read_only_udm.target.url
The value is taken from the URL field.
UserAgent
read_only_udm.network.http.user_agent
The value is taken from the UserAgent field.
UserID
read_only_udm.principal.user.product_object_id
The value is taken from the UserID field.
UserUID
read_only_udm.target.user.product_object_id
The value is taken from the UserUID field.
VirtualNetworkID
read_only_udm.principal.resource.product_object_id
The value is taken from the VirtualNetworkID field.
WAFAction
read_only_udm.security_result.about.labels
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFAction field.
WAFAttackScore
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFAttackScore field.
WAFFlags
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFFlags field.
WAFProfile
read_only_udm.security_result.about.labels
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFProfile field.
WAFRCEAttackScore
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFRCEAttackScore field.
WAFRuleID
read_only_udm.security_result.about.labels
read_only_udm.security_result.about.resource.attribute.labels
read_only_udm.security_result.threat_id
The value is taken from the WAFRuleID field.
WAFRuleMessage
read_only_udm.security_result.rule_name
read_only_udm.security_result.threat_name
The value is taken from the WAFRuleMessage field.
WAFSQLiAttackScore
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFSQLiAttackScore field.
WAFXSSAttackScore
read_only_udm.security_result.about.resource.attribute.labels
The value is taken from the WAFXSSAttackScore field.
ZoneID
read_only_udm.additional.fields
The value is taken from the ZoneID field.
read_only_udm.metadata.log_type
The value is set to "CLOUDFLARE".
read_only_udm.metadata.product_name
The value is set to "Cloudflare Gateway DNS" if the log is a DNS log, "Cloudflare Gateway HTTP" if the log is a Gateway HTTP log, "Cloudflare Audit" if the log is an Audit log, or "Web Application Firewall" otherwise.
read_only_udm.metadata.vendor_name
The value is set to "Cloudflare".
read_only_udm.network.application_protocol
The value is set to "DNS" if the log is a DNS log, "HTTP" if the HTTPVersion field contains "HTTP", or the value of the Protocol field converted to uppercase if the Protocol field is not empty and is not "tls" or "TLS".
read_only_udm.network.direction
The value is set to "OUTBOUND" if the EgressIP field is not empty.
read_only_udm.network.http.parsed_user_agent
The value is taken from the UserAgent or ClientRequestUserAgent field and is parsed using the parseduseragent filter.
read_only_udm.extensions.auth.type
The value is set to "MACHINE" if the Action field is "login" or "logout".
read_only_udm.metadata.event_type
The value is set to "NETWORK_DNS" if the log is a DNS log, "NETWORK_CONNECTION" if the log is a Gateway HTTP log, "USER_RESOURCE_ACCESS" if the log is an Audit log and the ActorIP and ActorEmail fields are empty, "USER_RESOURCE_UPDATE_CONTENT" if the log is an Audit log and the ResourceType and newvalue fields are not empty, "USER_LOGIN" if the Action field is "login", "USER_LOGOUT" if the Action field is "logout", "USER_RESOURCE_ACCESS" if the Email field is not empty and matches the email address format, or "NETWORK_CONNECTION" if the EgressIP and SourceIP fields are not empty or the OriginIP and SourceIP fields are not empty.
read_only_udm.target.file.mime_type
The value is taken from the EdgeResponseContentType field.
read_only_udm.target.location.country_or_region
The value is taken from the Country field.
read_only_udm.target.resource.id
The value is taken from the AccountID field or the ResourceID field.
read_only_udm.target.resource.product_object_id
The value is taken from the AccountID field, the AppUUID field, or the ResourceID field.
read_only_udm.target.user.product_object_id
The value is taken from the OwnerID field or the UserUID field.
Need more help?
Get answers from Community members and Google SecOps professionals.
