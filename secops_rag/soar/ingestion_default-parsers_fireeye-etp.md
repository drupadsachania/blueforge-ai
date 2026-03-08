# Collect FireEye ETP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp/  
**Scraped:** 2026-03-05T09:55:47.778143Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FireEye ETP logs
Supported in:
Google secops
SIEM
This document explains how to ingest FireEye ETP (now Trellix Email Security - Cloud Edition) logs to Google Security Operations using Google Cloud Storage V2 via a Cloud Run function.
FireEye ETP (Email Threat Prevention), now Trellix Email Security - Cloud Edition, is a cloud-based email security gateway that protects against advanced email threats including phishing, malware, business email compromise, and impersonation attacks. The solution provides comprehensive inbound and outbound email security with URL defense, attachment sandboxing, and real-time threat intelligence powered by the Trellix Advanced Research Center.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
A Google Cloud project with the following APIs enabled:
Cloud Storage
Cloud Run functions
Cloud Scheduler
Pub/Sub
Cloud Build
Permissions to create and manage GCS buckets, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to the FireEye ETP (Trellix Email Security - Cloud Edition) admin console
Administrator permissions to create API keys in the Trellix portal
A FireEye ETP API key with access to the Alerts endpoint
Create Google Cloud Storage bucket
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
fireeye-etp-logs
).
Location type
Choose based on your needs (Region, Dual-region, Multi-region).
Location
Select the location (for example,
us-central1
).
Storage class
Standard (recommended for frequently accessed logs).
Access control
Uniform (recommended).
Protection tools
Optional: Enable object versioning or retention policy.
Click
Create
.
Collect FireEye ETP API credentials
To enable the Cloud Run function to retrieve alerts from FireEye ETP, you need to create an API key with appropriate permissions.
Create API key
Sign in to the
FireEye ETP
(Trellix Email Security - Cloud Edition) admin console.
In the top navigation bar, click
My Settings
.
Click the
API Keys
tab.
Click
Create API Key
.
In the
Products
section, select
Email Threat Prevention
.
In the
Entitlements
section, select all available entitlements to ensure the API key has access to alerts, email trace, and quarantine data.
Click
Create
or
Generate
.
Record API credentials
After creating the API key, record the following information:
API Key
: Your unique API key (for example,
a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
)
Base URL
: The fully qualified domain name for your region (for example,
etp.us.fireeye.com
)
Common base URLs include:
etp.us.fireeye.com
(US)
etp.eu.fireeye.com
(EU)
etp.ap.fireeye.com
(APAC)
Verify API permissions
The API key requires the following products and entitlements:
Product/Entitlement
Purpose
Email Threat Prevention
Access to email alerts, trace data, and threat information
All Entitlements
Full access to alerts, email trace, and quarantine APIs
Test API access
Verify that your API key is valid by running the following command:
curl
-s
-o
/dev/null
-w
"%{http_code}"
\
-H
"x-fireeye-api-key: YOUR_API_KEY"
\
"https://etp.us.fireeye.com/api/v1/alerts?size=1"
A
200
response code confirms that the API key is valid and has the required permissions.
Create service account for Cloud Run function
The Cloud Run function requires a service account with permissions to write logs to GCS and receive Pub/Sub messages.
In the
Google Cloud Console
, go to
IAM & Admin
>
Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter
fireeye-etp-ingestion
(or a descriptive name)
Service account description
: Enter
Service account for FireEye ETP log ingestion Cloud Run function
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
Click
Select a role
and search for
Storage Object Admin
. Select it.
Click
Add another role
and search for
Cloud Run Invoker
. Select it.
Click
Continue
.
Click
Done
.
Create Pub/Sub topic
Create a Pub/Sub topic that Cloud Scheduler will use to trigger the Cloud Run function.
In the
Google Cloud Console
, go to
Pub/Sub
>
Topics
.
Click
Create Topic
.
In the
Topic ID
field, enter
fireeye-etp-trigger
.
Leave the default settings and click
Create
.
Create Cloud Run function
Create a Cloud Run function that queries the FireEye ETP Alerts API, handles pagination and rate limiting, and writes results as NDJSON to GCS.
Prepare the function code
In the
Google Cloud Console
, go to
Cloud Run functions
.
Click
Create function
.
Provide the following configuration details:
Environment
: Select
2nd gen
.
Function name
: Enter
fireeye-etp-ingestion
.
Region
: Select the same region as your GCS bucket (for example,
us-central1
).
Trigger type
: Select
Cloud Pub/Sub
.
Cloud Pub/Sub topic
: Select
fireeye-etp-trigger
.
Service account
: Select
fireeye-etp-ingestion@PROJECT_ID.iam.gserviceaccount.com
.
Click
Next
.
Set the
Runtime
to
Python 3.11
(or later).
Set the
Entry point
to
main
.
In the
Source code
inline editor, replace the contents of
main.py
with the following code:
"""Cloud Run function to ingest FireEye ETP alerts into GCS."""
import
json
import
os
import
time
from
datetime
import
datetime
,
timedelta
,
timezone
import
functions_framework
import
urllib3
from
google.cloud
import
storage
GCS_BUCKET
=
os
.
environ
[
"GCS_BUCKET"
]
GCS_PREFIX
=
os
.
environ
.
get
(
"GCS_PREFIX"
,
"fireeye_etp"
)
STATE_KEY
=
os
.
environ
.
get
(
"STATE_KEY"
,
"fireeye_etp_state.json"
)
API_KEY
=
os
.
environ
[
"API_KEY"
]
API_BASE
=
os
.
environ
.
get
(
"API_BASE"
,
"etp.us.fireeye.com"
)
MAX_RECORDS
=
int
(
os
.
environ
.
get
(
"MAX_RECORDS"
,
"10000"
))
PAGE_SIZE
=
int
(
os
.
environ
.
get
(
"PAGE_SIZE"
,
"100"
))
LOOKBACK_HOURS
=
int
(
os
.
environ
.
get
(
"LOOKBACK_HOURS"
,
"1"
))
http
=
urllib3
.
PoolManager
()
gcs
=
storage
.
Client
()
def
_load_state
()
-
>
dict
:
"""Load the last event time from GCS state file."""
bucket
=
gcs
.
bucket
(
GCS_BUCKET
)
blob
=
bucket
.
blob
(
f
"
{
GCS_PREFIX
}
/
{
STATE_KEY
}
"
)
if
blob
.
exists
():
return
json
.
loads
(
blob
.
download_as_text
())
return
{}
def
_save_state
(
state
:
dict
)
-
>
None
:
"""Persist the state dict back to GCS."""
bucket
=
gcs
.
bucket
(
GCS_BUCKET
)
blob
=
bucket
.
blob
(
f
"
{
GCS_PREFIX
}
/
{
STATE_KEY
}
"
)
blob
.
upload_from_string
(
json
.
dumps
(
state
),
content_type
=
"application/json"
)
def
_api_get
(
path
:
str
,
params
:
dict
,
retries
:
int
=
5
)
-
>
dict
:
"""Execute a GET request against the FireEye ETP API with retry on 429."""
url
=
f
"https://
{
API_BASE
}{
path
}
"
headers
=
{
"x-fireeye-api-key"
:
API_KEY
,
"Accept"
:
"application/json"
,
}
backoff
=
2
for
attempt
in
range
(
retries
):
resp
=
http
.
request
(
"GET"
,
url
,
headers
=
headers
,
fields
=
params
)
if
resp
.
status
==
200
:
return
json
.
loads
(
resp
.
data
.
decode
(
"utf-8"
))
if
resp
.
status
==
429
:
wait
=
backoff
*
(
2
**
attempt
)
print
(
f
"Rate limited (429). Retrying in
{
wait
}
s "
f
"(attempt
{
attempt
+
1
}
/
{
retries
}
)."
)
time
.
sleep
(
wait
)
continue
raise
RuntimeError
(
f
"FireEye ETP API error:
{
resp
.
status
}
—
{
resp
.
data
.
decode
(
'utf-8'
)
}
"
)
raise
RuntimeError
(
"FireEye ETP API rate limit exceeded after maximum retries."
)
def
_fetch_alerts
(
since
:
str
)
-
>
list
:
"""Fetch alerts from FireEye ETP with offset-based pagination."""
all_alerts
=
[]
offset
=
0
while
len
(
all_alerts
)
<
MAX_RECORDS
:
params
=
{
"from_last_modified_on"
:
since
,
"size"
:
str
(
PAGE_SIZE
),
"offset"
:
str
(
offset
),
}
data
=
_api_get
(
"/api/v1/alerts"
,
params
)
alerts
=
data
.
get
(
"data"
,
[])
if
not
alerts
:
break
all_alerts
.
extend
(
alerts
)
offset
+=
len
(
alerts
)
if
len
(
alerts
)
<
PAGE_SIZE
:
break
return
all_alerts
[:
MAX_RECORDS
]
def
_write_ndjson
(
alerts
:
list
,
run_ts
:
str
)
-
>
str
:
"""Write alerts as NDJSON to GCS and return the blob path."""
bucket
=
gcgcs
.
bucket
CS_BUCKET
)
blob_path
=
(
f
"
{
GCS_PREFIX
}
/year=
{
run_ts
[:
4
]
}
/month=
{
run_ts
[
5
:
7
]
}
/"
f
"day=
{
run_ts
[
8
:
10
]
}
/
{
run_ts
}
_alerts.ndjson"
)
blob
=
bucket
.
blob
(
blob_path
)
ndjson
=
"
\n
"
.
join
(
json
.
dumps
(
a
,
separators
=
(
","
,
":"
))
for
a
in
alerts
)
blob
.
up
upload_from_string
djson
,
content_type
=
"application/x-ndjson"
)
return
blob_path
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""Entry point triggered by Pub/Sub via Cloud Scheduler."""
state
=
_load_state
()
now
=
datetime
.
now
(
timezone
.
utc
)
since
=
st
state
et
(
"last_event_time"
,
(
now
-
timedelta
(
hours
=
LOOKBACK_HOURS
))
.
strftime
(
"%Y-%m-
%d
T%H:%M:%S.000"
),
)
print
(
f
"Fetching FireEye ETP alerts since
{
since
}
."
)
alerts
=
_fetch_alerts
(
since
)
if
not
alerts
:
print
(
"No new alerts found."
)
return
"OK"
run_ts
=
now
.
strftime
(
"%Y-%m-
%d
T%H%M%SZ"
)
blob_path
=
_write_ndjson
(
alerts
,
run_ts
)
print
(
f
"Wrote
{
len
(
alerts
)
}
alerts to gs://
{
GCS_BUCKET
}
/
{
blob_path
}
."
)
latest
=
max
(
a
.
get
(
"attributes"
,
{})
.
get
(
"meta"
,
{})
.
get
(
"last_modified_on"
,
since
)
for
a
in
alerts
)
state
[
"last_event_time"
]
=
latest
_save_state
(
state
)
print
(
f
"State updated. last_event_time=
{
latest
}
."
)
return
"OK"
Replace the contents of
requirements.txt
with the following:
functions-framework==3.*
google-cloud-storage==2.*
urllib3==2.*
Configure environment variables
In the
Cloud Run function
configuration, expand the
Runtime, build, connections and security settings
section.
Under
Runtime environment variables
, add the following variables:
Variable
Value
GCS_BUCKET
Your GCS bucket name (for example,
fireeye-etp-logs
)
GCS_PREFIX
Prefix for log files (for example,
fireeye_etp
)
STATE_KEY
State filename (for example,
fireeye_etp_state.json
)
API_KEY
Your FireEye ETP API key
API_BASE
Your FireEye ETP base URL (for example,
etp.us.fireeye.com
)
MAX_RECORDS
Maximum records per invocation (for example,
10000
)
PAGE_SIZE
Records per API page (for example,
100
)
LOOKBACK_HOURS
Hours to look back on first run (for example,
1
)
Set
Memory allocated
to at least
256 MB
.
Set
Timeout
to
540
seconds.
Click
Deploy
.
Create Cloud Scheduler job
Create a Cloud Scheduler job to invoke the Cloud Run function on a recurring schedule.
In the
Google Cloud Console
, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Name
: Enter
fireeye-etp-ingestion-schedule
.
Region
: Select the same region as your Cloud Run function (for example,
us-central1
).
Frequency
: Enter
*/5 * * * *
(every 5 minutes).
Timezone
: Select your preferred timezone (for example,
UTC
).
Click
Continue
.
In the
Configure the execution
section:
Target type
: Select
Pub/Sub
.
Cloud Pub/Sub topic
: Select
fireeye-etp-trigger
.
Message body
: Enter
{"run": true}
.
Click
Create
.
Test the Cloud Scheduler job
In the
Cloud Scheduler
list, locate the job
fireeye-etp-ingestion-schedule
.
Click
Force Run
to trigger an immediate execution.
Go to
Cloud Run functions
>
fireeye-etp-ingestion
>
Logs
to verify successful execution.
Go to
Cloud Storage
>
Buckets
>
fireeye-etp-logs
to verify that NDJSON files are being created under the
fireeye_etp/
prefix.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Get the service account email
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
FireEye ETP Alerts
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
FireEye ETP
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
secops-12345678@secops-gcp-prod.iam.gserviceaccount.com
Copy the email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI:
gs://fireeye-etp-logs/fireeye_etp/
Replace
fireeye-etp-logs
with your GCS bucket name and
fireeye_etp
with your configured prefix.
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days).
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
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click the bucket name (for example,
fireeye-etp-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email
Assign roles
: Select
Storage Object Viewer
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
about
Merged from about_field
about.file.full_path
Value from entry.attributes.email.attachment if not empty, else set to %{entry.attributes.email.attachment}
about.file.md5
Value from entry.attributes.alert.malware_md5 if attachment is file, else from alert.malware_md5
about.hostname
Extracted from entry.attributes.email.attachment using grok pattern for domain
about.url
Set to %{about.file.full_path} after normalization if full_path starts with hxxp
additional.fields
Merged with process_label, ack_label, client_label, baleValue_bale_id_label, baleValue_name_label, os_change_id_label, bale_severity_label, bale_description_label, malware_application_label, malwareValue_downnloaded_at_label, malwareValue_executed_at_label, malwareValue_md5sum_label, malwareValue_original_label, malwareValue_profile_label, malwareValue_sha256_label, malwareValue_stype_label, malwareValue_type_label, parent_uuid_label, report_id_label, interface_interface_label, interface_mode_label, alert_sc_version_label, alert_smtp_message_date_label, alert_smtp_message_last_malware_label, alert_smtp_message_protocol_label, alert_smtp_message_queue_id_label, baleValue_bale_id_label, baleValue_name_label, os_change_id_label, bale_severity_label, bale_description_label, malware_application_label, malwareValue_downnloaded_at_label, malwareValue_executed_at_label, malwareValue_md5sum_label, malwareValue_original_label, malwareValue_profile_label, malwareValue_sha256_label, malwareValue_stype_label, malwareValue_type_label, parent_uuid_label, report_id_label, interface_interface_label, interface_mode_label, alert_sc_version_label, alert_smtp_message_date_label, alert_smtp_message_last_malware_label, alert_smtp_message_protocol_label, alert_smtp_message_queue_id_label
intermediary
Merged from intermediary
intermediary.ip
Merged from alert.smtp-message.ip_address
intermediary.location.country_or_region
Set to %{alert.smtp-message.country}
intermediary.user.email_addresses
Merged from src_email from header_cc grok
metadata.description
Set to %{alert.name}
metadata.event_timestamp
Date matched from accepted_timestamp with format yyyy-MM-ddTHH:mm:ss, or from entry.attributes.meta.last_modified_on with format yyyy-MM-ddTHH:mm:ss.SSS, or from entry.attributes.alert.timestamp with format yyyy-MM-ddTHH:mm:ss.SSS, or from alert.timestamp with format yyyy-MM-ddTHH:mm:ss.SSS, or from alert.attack-time with various formats, or from alert.occurred with various formats
metadata.event_type
Set to %{event_type1} based on conditions (NETWORK_CONNECTION if has_network, has_principal, has_principal_ip, has_target; USER_UNCATEGORIZED if has_principal_user; STATUS_UPDATE if has_principal_ip and has_principal or has_principal; GENERIC_EVENT otherwise), or set to EMAIL_TRANSACTION if has_principal and has_email_info or has_network, else SCAN_UNCATEGORIZED
metadata.product_log_id
Set to %{product_log_id}, or to %{email.etp_message_id}, or to %{entry.attributes.etp_message_id}, or to %{alert.uuid}
metadata.product_version
Set to %{version}
metadata.url_back_to_product
Set to %{entry.links.detail}
network.application_protocol
Set to "SMTP"
network.direction
Uppercased traffic_type if inbound or outbound
network.dns_domain
Set to %{attributes.domain}
network.email.cc
Merged from cc_email_1, cc_email_2, cc_email_3 from csv parsed header_cc, or from cc in ccs array
network.email.from
Set to %{smtp_from}, or to %{from_email} from grok on email.headers.from, or to %{from_email} from grok on entry.attributes.email.headers.from, or to %{alert.email-header.from} if matches email pattern, or to %{alert.smtp-message.from}
network.email.mail_id
Set to %{mail} from grok on attributes.downStreamMsgID, or set to %{entry.messages.0.attributes.originalMessageID} after gsub
network.email.subject
Merged from subject, or from entry.attributes.email.headers.subject, or from alert.email-header.subject
network.email.to
Merged from email in smtp_to if matches email pattern, or from to_email_1, to_email_2, to_email_3 from csv parsed header_to, or from recipient in email.smtp.recipients, or from emailTo in email_array after grok, or from alert.smtp-message.to, or from attributes.recipientHeader if matches email pattern
principal.administrative_domain
Set to %{etp_msg_id}, or to %{alert.src.domain}
principal.asset.hostname
Set to %{src_host}, or set to %{hostname} from grok on attributes.downStreamMsgID
principal.asset.ip
Merged from sender_ip, or from ip_value from grok on email.source_ip, or from attri_ip_value from grok on attributes.senderIP
principal.asset.mac
Merged from mac_value from grok on ent_source_mac if not empty and not 00:00:00:00:00:00
principal.hostname
Set to %{src_host}, or set to %{hostname} from grok on attributes.downStreamMsgID
principal.ip
Merged from sender_ip, or from ip_value from grok on email.source_ip, or from attri_ip_value from grok on attributes.senderIP, or from src_ip_value from grok on ent_source_ip if not empty and not 0.0.0.0
principal.labels
Merged with mail_from_label, rcpt_to_label
principal.location.country_or_region
Set to %{country_code}, or to %{email.source_country}, or to %{attributes.countryCode}
principal.mac
Merged from mac_value from grok on ent_source_mac if not empty and not 00:00:00:00:00:00
principal.user.email_addresses
Merged from alert.smtp-message.from
principal.user.user_display_name
Set to %{usr_display_name} from grok on header_from, or set to %{sender_real_name} from grok on entry.attributes.email.headers.from
principal.user.userid
Set to %{original_msg_id}
principal.email
Set to %{header_email} from grok on header_from if matches email pattern, or set to %{header_from} if matches email pattern
security_result
Merged from security_result, or from security_result_1
security_result.about.resource.attribute.creation_time
Date matched from entry.attributes.alert.timestamp with format yyyy-MM-ddTHH:mm:ss.SSS, or from alert.timestamp with format yyyy-MM-ddTHH:mm:ss.SSS
security_result.action
Set to "BLOCK" if parsed_email_status is dropped, quarantined, or deleted, or set to action_value if parsed_email_status is dropped, quarantined, or deleted
security_result.action_details
Set to %{alert.action}
security_result.attack_details.tactics
Merged from tactics_data based on technique_data.id matching various MITRE IDs or names
security_result.attack_details.techniques
Merged from technique_data based on technique_id or subtechnique_id or technique_name matching various MITRE techniques
security_result.category
Set to "MAIL_PHISHING" if threat_type matches (?i)Phishing
security_result.category_details
Merged from threat_type, or from verdict
security_result.detection_fields
Merged with email_label, status_label, verdict_at_label, verdict_av_label, verdict_pv_label, action_yara_label, verdict_yara_label, delivery_timestamp_label, attach_count_label, email_reject_label, id_label, client_label, ack_label, alert_label, downloaded_at_label, executed_at_label, submitted_at_label, sec_result.detection_fields, bale_severity_label, alert_analysis_label, alert_malware_analysis_os_label
security_result.risk_score
Set to 5.0 if alert_severity is CRITICAL, ERROR, HIGH, INFORMATIONAL, LOW, MEDIUM, majr, unkn, else set to 10.0 if majr
security_result.severity
Set to %{alert.severity} if in allowed list, or to HIGH if majr, or to UNKNOWN_SEVERITY if unkn, or lowercased alert_severity with risk_score set accordingly
security_result.severity_details
Set to %{alert_severity}
security_result.summary
Set to %{entry.attributes.meta.last_malware}, or to %{desc} from grok on attributes.downStreamMsgID
security_result.threat_id
Set to %{entry.attributes.meta.legacy_id} converted to string, or set to %{malware.trace_iden} for first malware in alert.explanation.malware_detected.malware
security_result.threat_name
Set to %{security_result.summary}, or to %{malware.name} for first malware in alert.explanation.malware_detected.malware
security_result.verdict_info
Merged with verdict_info if verdict is RISKWARE
target.asset.hostname
Set to %{target_host} from grok on delivery_msg
target.file.first_seen_time
Date matched from alert.attack-time with various formats
target.file.first_submission_time
Date matched from malwareValue.submitted-at with various formats
target.file.full_path
Set to %{malwareValue.original} if malwareValue.type is url and original not empty, else if has_target_file_full_path false, else additional fields
target.file.md5
Set to %{malwareValue.md5sum} if not empty and has_md5 false
target.file.names
Merged from malwareValue_name
target.file.sha256
Set to %{malwareValue.sha256} if not empty and has_sha256 false
target.file.size
Set to %{bytes} from grok on delivery_msg converted to uinteger
target.hostname
Set to %{target_host} from grok on delivery_msg
target.labels
Merged with alert_ack_label, alert_smtp_message_last_malware_label, alert_smtp_message_protocol_label, alert_smtp_message_queue_id_label
target.url
Set to %{malwareValue_original} if malwareValue.type is url and original not empty
target.user.email_addresses
Merged from target_email from grok on delivery_msg, or from to_email_3, or from emailTo if matches pattern, or from alert.dst.smtp-to if matches email pattern, or from alert.email-header.to if matches pattern
metadata.vendor_name
Set to "FireEye"
metadata.product_name
Set to "ETP"
Need more help?
Get answers from Community members and Google SecOps professionals.
