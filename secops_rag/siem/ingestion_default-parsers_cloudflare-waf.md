# Collect Cloudflare WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-waf/  
**Scraped:** 2026-03-05T09:22:20.039295Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloudflare WAF logs
Supported in:
Google secops
SIEM
This parser extracts fields from Cloudflare Web Application Firewall (WAF) JSON logs, transforms and maps them to the Unified Data Model (UDM). It handles various Cloudflare actions, enriching the data with metadata and network information before structuring the output into the UDM format.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Google Cloud.
Cloudflare Enterprise plan.
Privileged access to Cloudflare. For details, see
Cloudflare
.
Create a Google Cloud Storage Bucket
Sign in to the Google Cloud console.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
Configure the bucket:
Name
: enter a unique name that meets the bucket name requirements (for example,
cloudflare-waf
).
Choose where to store your data
: select a location.
Choose a storage class for your data
: either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management.
Choose how to control access to objects
: select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
Storage class
: Choose based on your needs (for example,
Standard
).
Click
Create
.
Grant bucket permissions to Cloudflare IAM user
In Google Cloud, go to
Storage
>
Browser
>
Bucket
>
Permissions
.
Add the account logpush@cloudflare-data.iam.gserviceaccount.com with Storage Object Admin permission.
Create a Logpush Job for WAF Logs using Cloudflare UI
Sign in to Cloudflare.
Go to
Analytics & Logs
>
Logpush
.
Select
Create a Logpush job
.
In
Select a destination
, choose
Google Cloud Storage
.
Enter the following destination details:
Bucket
: Google Cloud Storage bucket name
Path
: Bucket location within the storage container
Select
Organize logs into daily subfolders
Click
Continue
.
Select the
Security (WAF)
dataset to push to the storage.
Configure the logpush job:
Enter the
Job name
.
Under If logs match, you can select the events to include or remove from your logs. Refer to
Filters
for more information. Not all datasets have this option available.
In
Send the following
fields, you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.
Click
Submit
.
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
Cloudflare WAF Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Cloudflare WAF
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
: the Cloud Storage URL.
Source deletion options
: select the deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
Action
security_result.action_details
The value of
Action
from the raw log is directly assigned to this UDM field.
Action
security_result.action
The value of this field is derived from the
Action
field in the raw log.  If
Action
is "allow", the UDM field is set to
ALLOW
. If
Action
is "challengeSolved", "jschallengeSolved", "managedchallengenoninteractivesolved", or "managedchallengeinteractivesolved", the UDM field is set to
ALLOW_WITH_MODIFICATION
. If
Action
is "drop", "block", or "connectionclose", the UDM field is set to
BLOCK
. If
Action
is "challengefailed" or "jschallengefailed", the UDM field is set to
FAIL
. Otherwise, it's set to
UNKNOWN_ACTION
.
ClientASN
network.asn
The value of
ClientASN
from the raw log is directly assigned to this UDM field after converting it to a string.
ClientASNDescription
additional.fields.key
The key is statically set to "ClientASNDescription".
ClientASNDescription
additional.fields.value.string_value
The value of
ClientASNDescription
from the raw log is directly assigned to this UDM field.
ClientCountry
principal.location.country_or_region
The value of
ClientCountry
from the raw log is directly assigned to this UDM field.
ClientIP
principal.ip
The value of
ClientIP
from the raw log is directly assigned to this UDM field.
ClientRefererHost
intermediary.hostname
The value of
ClientRefererHost
from the raw log is directly assigned to this UDM field.
ClientRefererPath
network.http.referral_url
The value of
ClientRefererPath
from the raw log is directly assigned to this UDM field.
ClientRequestHost
target.hostname
The value of
ClientRequestHost
from the raw log is directly assigned to this UDM field.
ClientRequestMethod
network.http.method
The value of
ClientRequestMethod
from the raw log is directly assigned to this UDM field.
ClientRequestPath
target.file.full_path
The value of
ClientRequestPath
from the raw log is directly assigned to this UDM field.
ClientRequestProtocol
network.application_protocol
The protocol part of
ClientRequestProtocol
(e.g., "HTTP" from "HTTP/1.1") is extracted using grok, converted to uppercase, and assigned to this UDM field.
ClientRequestUserAgent
network.http.user_agent
The value of
ClientRequestUserAgent
from the raw log is directly assigned to this UDM field.
Datetime
metadata.event_timestamp
The value of
Datetime
from the raw log is parsed as an RFC 3339 timestamp and assigned to this UDM field.
EdgeColoCode
additional.fields.key
The key is statically set to "EdgeColoCode".
EdgeColoCode
additional.fields.value.string_value
The value of
EdgeColoCode
from the raw log is directly assigned to this UDM field.
EdgeResponseStatus
network.http.response_code
The value of
EdgeResponseStatus
from the raw log is directly assigned to this UDM field and converted to an integer.
Kind
metadata.product_event_type
The value of
Kind
from the raw log is directly assigned to this UDM field.
Metadata.filter
target.resource.attribute.labels.value
The value of
Metadata.filter
from the raw log is assigned to the
value
field of a label within
target.resource.attribute.labels
. The
key
for this label is statically set to "Metadata filter".
Metadata.type
target.resource.attribute.labels.value
The value of
Metadata.type
from the raw log is assigned to the
value
field of a label within
target.resource.attribute.labels
. The
key
for this label is statically set to "Metadata type". The value of this field is derived based on the presence and values of
ClientIP
,
ClientRequestHost
, and
app_protocol
.  See parser code for the specific logic.  Statically set to "Cloudflare". Statically set to "Cloudflare log Aggregator". Statically set to "CLOUDFLARE_WAF".
RayID
metadata.product_log_id
The value of
RayID
from the raw log is directly assigned to this UDM field.
RuleID
security_result.rule_id
The value of
RuleID
from the raw log is directly assigned to this UDM field.
Source
security_result.rule_name
The value of
Source
from the raw log is directly assigned to this UDM field.
timestamp
metadata.event_timestamp
,
events.timestamp
The value of
timestamp
from the raw log is directly assigned to these UDM fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
