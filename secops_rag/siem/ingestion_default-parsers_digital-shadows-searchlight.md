# Collect Digital Shadows SearchLight logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight/  
**Scraped:** 2026-03-05T09:23:25.667814Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Digital Shadows SearchLight logs
Supported in:
Google secops
SIEM
This document explains how to ingest Digital Shadows SearchLight logs to Google Security Operations using Google Cloud Storage. The parser extracts security event data from the JSON logs. It initializes Unified Data Model (UDM) fields, parses the JSON payload, maps relevant fields to the UDM schema, extracts entities like email and hostname using grok patterns, and constructs the security_result and metadata objects within the UDM event.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Digital Shadows SearchLight tenant
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
digital-shadows-logs
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location (for example,
us-central1
)
Storage class
Standard (recommended for frequently accessed logs)
Access control
Uniform (recommended)
Protection tools
Optional: Enable object versioning or retention policy
Click
Create
.
Collect Digital Shadows SearchLight API credentials
Sign in to the
Digital Shadows SearchLight Portal
.
Go to
Settings
>
API Credentials
.
Create a new API client or key pair.
Copy and save in a secure location the following details:
API Key
: Your 6-character API key
API Secret
: Your 32-character API secret
Account ID
: Your account ID (required for most tenants)
API Base URL
:
https://api.searchlight.app/v1
or
https://portal-digitalshadows.com/api/v1
Create service account for Cloud Run function
The Cloud Run function needs a service account with permissions to write to GCS bucket.
Create service account
In the
GCP Console
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
digital-shadows-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Digital Shadows SearchLight logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section:
Click
Select a role
.
Search for and select
Storage Object Admin
.
Click
+ Add another role
.
Search for and select
Cloud Run Invoker
.
Click
+ Add another role
.
Search for and select
Cloud Functions Invoker
.
Click
Continue
.
Click
Done
.
Grant IAM permissions on GCS bucket
Grant the service account write permissions on the GCS bucket:
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
digital-shadows-collector-sa@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create Pub/Sub topic
Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.
In the
GCP Console
, go to
Pub/Sub
>
Topics
.
Click
Create topic
.
Provide the following configuration details:
Topic ID
: Enter
digital-shadows-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Digital Shadows SearchLight API and writes them to GCS.
In the
GCP Console
, go to
Cloud Run
.
Click
Create service
.
Select
Function
(use an inline editor to create a function).
In the
Configure
section, provide the following configuration details:
Setting
Value
Service name
digital-shadows-collector
Region
Select region matching your GCS bucket (for example,
us-central1
)
Runtime
Select
Python 3.12
or later
In the
Trigger (optional)
section:
Click
+ Add trigger
.
Select
Cloud Pub/Sub
.
In
Select a Cloud Pub/Sub topic
, choose the topic (
digital-shadows-trigger
).
Click
Save
.
In the
Authentication
section:
Select
Require authentication
.
Check
Identity and Access Management (IAM)
.
Scroll down and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select the service account (
digital-shadows-collector-sa
).
Go to the
Containers
tab:
Click
Variables & Secrets
.
Click
+ Add variable
for each environment variable:
Variable Name
Example Value
GCS_BUCKET
digital-shadows-logs
GCS_PREFIX
digital-shadows-searchlight
STATE_KEY
digital-shadows-searchlight/state.json
DS_API_KEY
your-6-character-api-key
DS_API_SECRET
your-32-character-api-secret
API_BASE
https://api.searchlight.app/v1
DS_ACCOUNT_ID
your-account-id
PAGE_SIZE
100
MAX_PAGES
10
Scroll down in the
Variables & Secrets
tab to
Requests
:
Request timeout
: Enter
600
seconds (10 minutes).
Go to the
Settings
tab in
Containers
:
In the
Resources
section:
Memory
: Select
512 MiB
or higher.
CPU
: Select
1
.
Click
Done
.
Scroll to
Execution environment
:
Select
Default
(recommended).
In the
Revision scaling
section:
Minimum number of instances
: Enter
0
.
Maximum number of instances
: Enter
100
(or adjust based on expected load).
Click
Create
.
Wait for the service to be created (1-2 minutes).
After the service is created, the
inline code editor
opens automatically.
Add function code
Enter
main
in
Function entry point
In the inline code editor, create two files:
First file:
main.py:
import
functions_framework
from
google.cloud
import
storage
import
json
import
os
import
base64
import
logging
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
from
urllib.parse
import
urlencode
import
urllib3
logger
=
logging
.
getLogger
()
logger
.
setLevel
(
logging
.
INFO
)
HTTP
=
urllib3
.
PoolManager
(
retries
=
False
)
storage_client
=
storage
.
Client
()
def
_basic_auth_header
(
key
:
str
,
secret
:
str
)
-
>
str
:
token
=
base64
.
b64encode
(
f
"
{
key
}
:
{
secret
}
"
.
encode
(
"utf-8"
))
.
decode
(
"utf-8"
)
return
f
"Basic
{
token
}
"
def
_load_state
(
bucket
,
key
,
default_days
=
30
)
-
>
str
:
"""Return ISO8601 checkpoint (UTC)."""
try
:
blob
=
bucket
.
blob
(
key
)
if
blob
.
exists
():
state_data
=
blob
.
download_as_text
()
state
=
json
.
loads
(
state_data
)
ts
=
state
.
get
(
"last_timestamp"
)
if
ts
:
return
ts
except
Exception
as
e
:
logger
.
warning
(
f
"State read error:
{
e
}
"
)
return
(
datetime
.
now
(
timezone
.
utc
)
-
timedelta
(
days
=
default_days
))
.
isoformat
()
def
_save_state
(
bucket
,
key
,
ts
:
str
)
-
>
None
:
blob
=
bucket
.
blob
(
key
)
blob
.
upload_from_string
(
json
.
dumps
({
"last_timestamp"
:
ts
}),
content_type
=
"application/json"
)
def
_get_json
(
url
:
str
,
headers
:
dict
,
params
:
dict
,
backoff_s
=
2
,
max_retries
=
3
)
-
>
dict
:
qs
=
f
"?
{
urlencode
(
params
)
}
"
if
params
else
""
for
attempt
in
range
(
max_retries
):
r
=
HTTP
.
request
(
"GET"
,
f
"
{
url
}{
qs
}
"
,
headers
=
headers
)
if
r
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
r
.
data
.
decode
(
"utf-8"
))
if
r
.
status
in
(
429
,
500
,
502
,
503
,
504
):
wait
=
backoff_s
*
(
2
**
attempt
)
logger
.
warning
(
f
"HTTP
{
r
.
status
}
from DS API, retrying in
{
wait
}
s"
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
"DS API error
{
r
.
status
}
:
{
r
.
data
[:
200
]
}
"
)
raise
RuntimeError
(
"Exceeded retry budget for DS API"
)
def
_collect
(
api_base
,
headers
,
path
,
since_ts
,
account_id
,
page_size
,
max_pages
,
time_param
):
items
=
[]
for
page
in
range
(
max_pages
):
params
=
{
"limit"
:
page_size
,
"offset"
:
page
*
page_size
,
time_param
:
since_ts
,
}
if
account_id
:
params
[
"account-id"
]
=
account_id
data
=
_get_json
(
f
"
{
api_base
}
/
{
path
}
"
,
headers
,
params
)
batch
=
data
.
get
(
"items"
)
or
data
.
get
(
"data"
)
or
[]
if
not
batch
:
break
items
.
extend
(
batch
)
if
len
(
batch
)
<
page_size
:
break
return
items
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch logs from Digital Shadows SearchLight API and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
bucket_name
=
os
.
environ
[
"GCS_BUCKET"
]
api_key
=
os
.
environ
[
"DS_API_KEY"
]
api_secret
=
os
.
environ
[
"DS_API_SECRET"
]
prefix
=
os
.
environ
.
get
(
"GCS_PREFIX"
,
"digital-shadows-searchlight"
)
state_key
=
os
.
environ
.
get
(
"STATE_KEY"
,
"digital-shadows-searchlight/state.json"
)
api_base
=
os
.
environ
.
get
(
"API_BASE"
,
"https://api.searchlight.app/v1"
)
account_id
=
os
.
environ
.
get
(
"DS_ACCOUNT_ID"
,
""
)
page_size
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
max_pages
=
int
(
os
.
environ
.
get
(
"MAX_PAGES"
,
"10"
))
try
:
bucket
=
storage_client
.
bucket
(
bucket_name
)
last_ts
=
_load_state
(
bucket
,
state_key
)
logger
.
info
(
f
"Checkpoint:
{
last_ts
}
"
)
headers
=
{
"Authorization"
:
_basic_auth_header
(
api_key
,
api_secret
),
"Accept"
:
"application/json"
,
"User-Agent"
:
"Chronicle-DigitalShadows-GCS/1.0"
,
}
records
=
[]
incidents
=
_collect
(
api_base
,
headers
,
"incidents"
,
last_ts
,
account_id
,
page_size
,
max_pages
,
time_param
=
"published-after"
)
for
incident
in
incidents
:
incident
[
'_source_type'
]
=
'incident'
records
.
extend
(
incidents
)
intel_incidents
=
_collect
(
api_base
,
headers
,
"intel-incidents"
,
last_ts
,
account_id
,
page_size
,
max_pages
,
time_param
=
"published-after"
)
for
intel
in
intel_incidents
:
intel
[
'_source_type'
]
=
'intelligence_incident'
records
.
extend
(
intel_incidents
)
indicators
=
_collect
(
api_base
,
headers
,
"indicators"
,
last_ts
,
account_id
,
page_size
,
max_pages
,
time_param
=
"lastUpdated-after"
)
for
indicator
in
indicators
:
indicator
[
'_source_type'
]
=
'ioc'
records
.
extend
(
indicators
)
if
records
:
newest
=
max
(
(
r
.
get
(
"updated"
)
or
r
.
get
(
"raised"
)
or
r
.
get
(
"lastUpdated"
)
or
last_ts
)
for
r
in
records
)
key
=
f
"
{
prefix
}
/digital_shadows_
{
datetime
.
now
(
timezone
.
utc
)
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
}
.json"
body
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
r
,
separators
=
(
","
,
":"
))
for
r
in
records
)
blob
=
bucket
.
blob
(
key
)
blob
.
upload_from_string
(
body
,
content_type
=
"application/x-ndjson"
)
_save_state
(
bucket
,
state_key
,
newest
)
msg
=
f
"Wrote
{
len
(
records
)
}
records to gs://
{
bucket_name
}
/
{
key
}
"
else
:
msg
=
"No new records"
logger
.
info
(
msg
)
print
(
msg
)
except
Exception
as
e
:
logger
.
error
(
f
"Error processing logs:
{
str
(
e
)
}
"
)
raise
Second file:
requirements.txt:
functions
-
framework
==
3
.*
google
-
cloud
-
storage
==
2
.*
urllib3
>
=
2.0
.
0
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
In the
GCP Console
, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Setting
Value
Name
digital-shadows-collector-hourly
Region
Select same region as Cloud Run function
Frequency
0 * * * *
(every hour, on the hour)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select the topic (
digital-shadows-trigger
)
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose frequency based on log volume and latency requirements:
Frequency
Cron Expression
Use Case
Every 5 minutes
*/5 * * * *
High-volume, low-latency
Every 15 minutes
*/15 * * * *
Medium volume
Every hour
0 * * * *
Standard (recommended)
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
0 0 * * *
Historical data collection
Test the scheduler job
In the
Cloud Scheduler
console, find your job.
Click
Force run
to trigger manually.
Wait a few seconds and go to
Cloud Run
>
Services
>
digital-shadows-collector
>
Logs
.
Verify the function executed successfully.
Check the GCS bucket to confirm logs were written.
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
Digital Shadows SearchLight logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Digital Shadows SearchLight
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle
-
12345678
@chronicle
-
gcp
-
prod
.
iam
.
gserviceaccount
.
com
Copy this email address for use in the next step.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email.
Assign roles
: Select
Storage Object Viewer
.
Click
Save
.
Configure a feed in Google SecOps to ingest Digital Shadows SearchLight logs
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
Digital Shadows SearchLight logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Digital Shadows SearchLight
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://digital-shadows-logs/digital-shadows-searchlight/
Replace:
digital-shadows-logs
: Your GCS bucket name.
digital-shadows-searchlight
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/digital-shadows-searchlight/
With subfolder:
gs://company-logs/vendor/application/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
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
Supported Digital Shadows SearchLight sample logs
Unauthorized code commit alert
{
"event-num"
:
36666
,
"event-created"
:
"2022-03-17T15:09:39.849631Z"
,
"event-action"
:
"create"
,
"triage-item-id"
:
"9d496163-93e1-4328-abf3-ad4ccb210f65"
,
"classification"
:
"unauthorized-code-commit-alert"
,
"state"
:
"unread"
,
"risk-level"
:
"medium"
,
"triage-item"
:
{
"id"
:
"9d496163-93e1-4328-abf3-ad4ccb210f65"
,
"classification"
:
"unauthorized-code-commit-alert"
,
"portal-id"
:
"B528C"
,
"title"
:
"Unauthorized commit to public code repository employee@example.com"
,
"risk-level"
:
"medium"
,
"raised"
:
"2022-03-17T15:09:39.777252Z"
},
"alert"
:
{
"id"
:
"f7bc5bd8-a9d4-4109-8953-0d72efb5e2ad"
,
"title"
:
"Unauthorized Code Commit employee@example.com"
,
"description"
:
"employee@example.com may have made an unauthorized code commit to a repository..."
,
"commit_url"
:
"https://github.com/internal-org/repo-name/commit/redacted_hash"
,
"source_repository"
:
"https://github.com/internal-org/repo-name"
,
"committer_details"
:
{
"user_profile"
:
"internal_user_01"
,
"email"
:
"employee@example.com"
}
},
"assets"
:
[
{
"type"
:
"domain"
,
"display-value"
:
"example.com"
}
]
}
Impersonating subdomain alert
{
"event-num"
:
36667
,
"event-created"
:
"2022-03-17T15:11:44.134972Z"
,
"event-action"
:
"create"
,
"classification"
:
"impersonating-subdomain-alert"
,
"risk-level"
:
"low"
,
"alert"
:
{
"id"
:
"106eb57b-5b4a-4717-bed0-90f4af27f876"
,
"title"
:
"Impersonating Subdomain brand-login.suspicious-domain.com"
,
"description"
:
"A subdomain possibly impersonating your assets was detected."
,
"impersonating_subdomain"
:
"brand-login.suspicious-domain.com"
,
"domain"
:
"suspicious-domain.com"
,
"dns_records"
:
{
"A"
:
"192.0.2.1"
},
"whois"
:
{
"registrar"
:
"Generic Registrar LLC"
,
"abuse_contact"
:
"abuse@registrar-example.com"
}
},
"assets"
:
[
{
"type"
:
"brand"
,
"display-value"
:
"CorporateBrand"
}
]
}
Exposed access key alert
{
"event-num"
:
36668
,
"event-created"
:
"2022-03-17T15:19:09.110662Z"
,
"event-action"
:
"update"
,
"classification"
:
"exposed-access-key-alert"
,
"risk-level"
:
"high"
,
"alert"
:
{
"id"
:
"cf6be201-928b-431d-b925-0b12ab5f4b41"
,
"title"
:
"Exposed Access Key Technical credential"
,
"description"
:
"An exposed Technical credential was detected on github.com"
,
"source_information"
:
{
"url"
:
"https://github.com/external-dev/public-repo/blob/main/config.yaml"
,
"repository_name"
:
"external-dev/public-repo"
},
"exposed_data"
:
{
"key_name"
:
"AWS_ACCESS_KEY_ID"
,
"secret_name"
:
"AWS_SECRET_ACCESS_KEY"
},
"committer_details"
:
{
"user_profile"
:
"external_dev_user"
,
"email"
:
"dev-account@example.net"
}
},
"assets"
:
[
{
"type"
:
"domain"
,
"display-value"
:
"example.com"
}
]
}
Need more help?
Get answers from Community members and Google SecOps professionals.
