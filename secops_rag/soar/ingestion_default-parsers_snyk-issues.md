# Collect Snyk Group Issues logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-issues/  
**Scraped:** 2026-03-05T10:00:24.356177Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Snyk Group Issues logs
Supported in:
Google secops
SIEM
This document explains how to ingest Snyk Group Issues logs to Google Security Operations using Google Cloud Storage. Snyk is a developer security platform that helps organizations find and fix vulnerabilities in open source dependencies, container images, infrastructure as code configurations, and application code. Snyk Group Issues provide visibility into security vulnerabilities and license issues across all projects within a Snyk Group.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Snyk Group (API token with read access; Group ID)
Snyk Group Admin role assigned to the user with the API token (the user must be able to view Group Audit Logs and Group Issues)
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
snyk-group-logs
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
Collect Snyk Group ID and API token
Get Snyk API token
Sign in to the Snyk UI at
https://app.snyk.io
.
Go to
Account settings
>
API token
.
Click
Generate
to generate the API token.
Copy and save the token in a secure location to later use as
SNYK_TOKEN
.
Get Snyk Group ID
In the Snyk UI, switch to your Group.
Go to
Group settings
.
Copy and save the Group ID from the URL (
https://app.snyk.io/group/<GROUP_ID>/...
) to later use as
GROUP_ID
.
Assign Group Admin role
In the Snyk UI, go to
Group settings
>
Members
.
Locate the user associated with the API token.
Assign the
Group Admin
role to the user.
Note API endpoint
The REST API base endpoint varies by region. Identify your Snyk region and note the corresponding REST base URL:
Region
REST Base URL
SNYK-US-01
https://api.snyk.io/rest
SNYK-US-02
https://api.us.snyk.io/rest
SNYK-EU-01
https://api.eu.snyk.io/rest
SNYK-AU-01
https://api.au.snyk.io/rest
You will use this REST base URL as
API_BASE
in the Cloud Run function configuration. The function code constructs full endpoint URLs by appending paths like
/groups/{group_id}/audit_logs/search
to this base URL.
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
snyk-logs-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Snyk Group logs
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
These roles are required for:
Storage Object Admin
: Write logs to GCS bucket and manage state files
Cloud Run Invoker
: Allow Pub/Sub to invoke the function
Cloud Functions Invoker
: Allow function invocation
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
snyk-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
snyk-logs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Snyk Group API and writes them to GCS.
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
snyk-group-logs-collector
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
, choose the topic
snyk-logs-trigger
.
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
: Select the service account
snyk-logs-collector-sa
.
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
snyk-group-logs
GCS_PREFIX
snyk/group/
STATE_KEY
snyk/group/state.json
SNYK_TOKEN
your-snyk-api-token
GROUP_ID
your-group-uuid
API_BASE
https://api.snyk.io/rest
SNYK_AUDIT_API_VERSION
2024-10-15
SNYK_ISSUES_API_VERSION
2024-10-15
AUDIT_PAGE_SIZE
100
ISSUES_PAGE_LIMIT
100
MAX_PAGES
20
LOOKBACK_SECONDS
3600
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
Scroll down to
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
time
import
urllib.parse
from
urllib.request
import
Request
,
urlopen
from
urllib.parse
import
urlparse
,
parse_qs
from
urllib.error
import
HTTPError
# Initialize Storage client
storage_client
=
storage
.
Client
()
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch logs from Snyk Group API and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
# Get environment variables
bucket_name
=
os
.
environ
.
get
(
'GCS_BUCKET'
)
prefix
=
os
.
environ
.
get
(
'GCS_PREFIX'
,
'snyk/group/'
)
.
strip
()
state_key
=
os
.
environ
.
get
(
'STATE_KEY'
,
'snyk/group/state.json'
)
.
strip
()
# Snyk API credentials
api_base
=
os
.
environ
.
get
(
'API_BASE'
,
'https://api.snyk.io/rest'
)
.
rstrip
(
'/'
)
snyk_token
=
os
.
environ
.
get
(
'SNYK_TOKEN'
)
.
strip
()
group_id
=
os
.
environ
.
get
(
'GROUP_ID'
)
.
strip
()
# Page sizes & limits
audit_size
=
int
(
os
.
environ
.
get
(
'AUDIT_PAGE_SIZE'
,
'100'
))
issues_limit
=
int
(
os
.
environ
.
get
(
'ISSUES_PAGE_LIMIT'
,
'100'
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
'MAX_PAGES'
,
'20'
))
# API versions
audit_api_version
=
os
.
environ
.
get
(
'SNYK_AUDIT_API_VERSION'
,
'2024-10-15'
)
.
strip
()
issues_api_version
=
os
.
environ
.
get
(
'SNYK_ISSUES_API_VERSION'
,
'2024-10-15'
)
.
strip
()
# First-run lookback
lookback_seconds
=
int
(
os
.
environ
.
get
(
'LOOKBACK_SECONDS'
,
'3600'
))
if
not
all
([
bucket_name
,
snyk_token
,
group_id
]):
print
(
'Error: Missing required environment variables'
)
return
try
:
# Get GCS bucket
bucket
=
storage_client
.
bucket
(
bucket_name
)
# Load state
state
=
load_state
(
bucket
,
state_key
)
print
(
'Starting Snyk Group logs collection'
)
# Pull audit logs
audit_res
=
pull_audit_logs
(
bucket
,
prefix
,
state
,
api_base
,
snyk_token
,
group_id
,
audit_api_version
,
audit_size
,
max_pages
,
lookback_seconds
)
print
(
f
"Audit logs:
{
audit_res
}
"
)
# Pull issues
issues_res
=
pull_issues
(
bucket
,
prefix
,
state
,
api_base
,
snyk_token
,
group_id
,
issues_api_version
,
issues_limit
,
max_pages
)
print
(
f
"Issues:
{
issues_res
}
"
)
# Save state
save_state
(
bucket
,
state_key
,
state
)
print
(
'Successfully completed Snyk Group logs collection'
)
except
Exception
as
e
:
print
(
f
'Error processing logs:
{
str
(
e
)
}
'
)
raise
def
load_state
(
bucket
,
key
):
"""Load state from GCS."""
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
return
json
.
loads
(
state_data
)
except
Exception
as
e
:
print
(
f
'Warning: Could not load state:
{
str
(
e
)
}
'
)
return
{}
def
save_state
(
bucket
,
key
,
state
):
"""Save state to GCS."""
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
blob
.
upload_from_string
(
json
.
dumps
(
state
,
separators
=
(
','
,
':'
)),
content_type
=
'application/json'
)
except
Exception
as
e
:
print
(
f
'Warning: Could not save state:
{
str
(
e
)
}
'
)
def
_iso
(
ts
):
"""Convert timestamp to ISO format."""
return
time
.
strftime
(
'%Y-%m-
%d
T%H:%M:%SZ'
,
time
.
gmtime
(
ts
))
def
_http_get
(
url
,
headers
):
"""Make HTTP GET request with retry logic."""
req
=
Request
(
url
,
method
=
'GET'
,
headers
=
headers
)
try
:
with
urlopen
(
req
,
timeout
=
60
)
as
r
:
return
json
.
loads
(
r
.
read
()
.
decode
(
'utf-8'
))
except
HTTPError
as
e
:
if
e
.
code
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
delay
=
int
(
e
.
headers
.
get
(
'Retry-After'
,
'1'
))
time
.
sleep
(
max
(
1
,
delay
))
with
urlopen
(
req
,
timeout
=
60
)
as
r2
:
return
json
.
loads
(
r2
.
read
()
.
decode
(
'utf-8'
))
raise
def
_write_page
(
bucket
,
prefix
,
kind
,
payload
):
"""Write page to GCS."""
ts
=
time
.
gmtime
()
key
=
f
"
{
prefix
.
rstrip
(
'/'
)
}
/
{
time
.
strftime
(
'%Y/%m/
%d
/%H%M%S'
,
ts
)
}
-snyk-
{
kind
}
.json"
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
(
payload
,
separators
=
(
','
,
':'
)),
content_type
=
'application/json'
)
return
key
def
_next_href
(
links
):
"""Extract next href from links."""
if
not
links
:
return
None
nxt
=
links
.
get
(
'next'
)
if
not
nxt
:
return
None
if
isinstance
(
nxt
,
str
):
return
nxt
if
isinstance
(
nxt
,
dict
):
return
nxt
.
get
(
'href'
)
return
None
def
pull_audit_logs
(
bucket
,
prefix
,
state
,
api_base
,
snyk_token
,
group_id
,
audit_api_version
,
audit_size
,
max_pages
,
lookback_seconds
):
"""Pull audit logs from Snyk Group API."""
headers
=
{
'Authorization'
:
f
'token
{
snyk_token
}
'
,
'Accept'
:
'application/vnd.api+json'
,
}
cursor
=
state
.
get
(
'audit_cursor'
)
pages
=
0
total
=
0
base
=
f
"
{
api_base
}
/groups/
{
group_id
}
/audit_logs/search"
params
=
{
'version'
:
audit_api_version
,
'size'
:
audit_size
}
if
cursor
:
params
[
'cursor'
]
=
cursor
else
:
now
=
time
.
time
()
params
[
'from'
]
=
_iso
(
now
-
lookback_seconds
)
params
[
'to'
]
=
_iso
(
now
)
while
pages
<
max_pages
:
url
=
f
"
{
base
}
?
{
urllib
.
parse
.
urlencode
(
params
,
doseq
=
True
)
}
"
payload
=
_http_get
(
url
,
headers
)
_write_page
(
bucket
,
prefix
,
'audit'
,
payload
)
data_items
=
(
payload
.
get
(
'data'
)
or
{})
.
get
(
'items'
)
or
[]
if
isinstance
(
data_items
,
list
):
total
+=
len
(
data_items
)
nxt
=
_next_href
(
payload
.
get
(
'links'
))
if
not
nxt
:
break
q
=
parse_qs
(
urlparse
(
nxt
)
.
query
)
cur
=
(
q
.
get
(
'cursor'
)
or
[
None
])[
0
]
if
not
cur
:
break
params
=
{
'version'
:
audit_api_version
,
'size'
:
audit_size
,
'cursor'
:
cur
}
state
[
'audit_cursor'
]
=
cur
pages
+=
1
return
{
'pages'
:
pages
+
1
if
total
else
pages
,
'items'
:
total
,
'cursor'
:
state
.
get
(
'audit_cursor'
)
}
def
pull_issues
(
bucket
,
prefix
,
state
,
api_base
,
snyk_token
,
group_id
,
issues_api_version
,
issues_limit
,
max_pages
):
"""Pull issues from Snyk Group API."""
headers
=
{
'Authorization'
:
f
'token
{
snyk_token
}
'
,
'Accept'
:
'application/vnd.api+json'
,
}
cursor
=
state
.
get
(
'issues_cursor'
)
pages
=
0
total
=
0
base
=
f
"
{
api_base
}
/groups/
{
group_id
}
/issues"
params
=
{
'version'
:
issues_api_version
,
'limit'
:
issues_limit
}
if
cursor
:
params
[
'starting_after'
]
=
cursor
while
pages
<
max_pages
:
url
=
f
"
{
base
}
?
{
urllib
.
parse
.
urlencode
(
params
,
doseq
=
True
)
}
"
payload
=
_http_get
(
url
,
headers
)
_write_page
(
bucket
,
prefix
,
'issues'
,
payload
)
data_items
=
payload
.
get
(
'data'
)
or
[]
if
isinstance
(
data_items
,
list
):
total
+=
len
(
data_items
)
nxt
=
_next_href
(
payload
.
get
(
'links'
))
if
not
nxt
:
break
q
=
parse_qs
(
urlparse
(
nxt
)
.
query
)
cur
=
(
q
.
get
(
'starting_after'
)
or
[
None
])[
0
]
if
not
cur
:
break
params
=
{
'version'
:
issues_api_version
,
'limit'
:
issues_limit
,
'starting_after'
:
cur
}
state
[
'issues_cursor'
]
=
cur
pages
+=
1
return
{
'pages'
:
pages
+
1
if
total
else
pages
,
'items'
:
total
,
'cursor'
:
state
.
get
(
'issues_cursor'
)
}
```
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
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
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
snyk-group-logs-hourly
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
Select the topic
snyk-logs-trigger
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
snyk-group-logs-collector
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
Snyk Group Audit/Issues
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Snyk Group level audit/issues logs
as the
Log type
.
Click
Get Service Account
. A unique service account email is displayed, for example:
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
Configure a feed in Google SecOps to ingest Snyk Group logs
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
Snyk Group Audit/Issues
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Snyk Group level audit/issues logs
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://snyk-group-logs/snyk/group/
Replace:
snyk-group-logs
: Your GCS bucket name.
snyk/group/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/snyk-logs/
With subfolder:
gs://company-logs/snyk/group/
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
(for example,
snyk.group
).
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
Need more help?
Get answers from Community members and Google SecOps professionals.
