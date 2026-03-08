# Collect Sentry logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentry/  
**Scraped:** 2026-03-05T10:00:04.911302Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Sentry logs
Supported in:
Google secops
SIEM
This document explains how to ingest Sentry logs to Google Security Operations using Google Cloud Storage. Sentry produces operational data in the form of events, issues, performance monitoring data, and error tracking information. This integration lets you send these logs to Google SecOps for analysis and monitoring, providing visibility into application errors, performance issues, and user interactions within your Sentry-monitored applications.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Sentry tenant (Auth Token with API scopes)
Collect Sentry prerequisites (IDs, API keys, org IDs, tokens)
Sign in to Sentry.
Find your
Organization slug
:
Go to
Settings
>
Organization
>
Settings
>
Organization ID
(the slug appears next to the org name).
Create an
Auth Token
:
Go to
Settings
>
Developer Settings
>
Personal Tokens
.
Click
Create New Token
.
Scopes (minimum)
:
org:read
,
project:read
,
event:read
.
Click
Create Token
.
Copy the token value (shown once). This is used as:
Authorization: Bearer <token>
.
(If self-hosted): Note your base URL (for example,
https://<your-domain>
); otherwise use
https://sentry.io
.
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
sentry-logs
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
Create service account for Cloud Run function
The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.
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
sentry-logs-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Sentry logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
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
sentry-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
sentry-logs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Sentry API and writes them to GCS.
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
sentry-logs-collector
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
sentry-logs-trigger
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
sentry-logs-collector-sa
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
Description
GCS_BUCKET
sentry-logs
GCS bucket name where data will be stored.
GCS_PREFIX
sentry/events/
Optional GCS prefix (subfolder) for objects.
STATE_KEY
sentry/events/state.json
Optional state/checkpoint file key.
SENTRY_ORG
your-org-slug
Sentry organization slug.
SENTRY_AUTH_TOKEN
sntrys_************************
Sentry Auth Token with org:read, project:read, event:read.
SENTRY_API_BASE
https://sentry.io
Sentry API base URL (self-hosted:
https://<your-domain>
).
MAX_PROJECTS
100
Maximum number of projects to process.
MAX_PAGES_PER_PROJECT
5
Maximum pages per project per execution.
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
urllib3
from
datetime
import
datetime
,
timezone
import
time
# Initialize HTTP client
http
=
urllib3
.
PoolManager
()
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
Cloud Run function triggered by Pub/Sub to fetch Sentry events and write to GCS.
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
'sentry/events/'
)
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
'sentry/events/state.json'
)
org
=
os
.
environ
.
get
(
'SENTRY_ORG'
,
''
)
.
strip
()
token
=
os
.
environ
.
get
(
'SENTRY_AUTH_TOKEN'
,
''
)
.
strip
()
api_base
=
os
.
environ
.
get
(
'SENTRY_API_BASE'
,
'https://sentry.io'
)
.
rstrip
(
'/'
)
max_projects
=
int
(
os
.
environ
.
get
(
'MAX_PROJECTS'
,
'100'
))
max_pages_per_project
=
int
(
os
.
environ
.
get
(
'MAX_PAGES_PER_PROJECT'
,
'5'
))
if
not
all
([
bucket_name
,
org
,
token
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
state
.
setdefault
(
'projects'
,
{})
# Get list of projects
projects
=
list_projects
(
api_base
,
org
,
token
,
max_projects
)
print
(
f
'Found
{
len
(
projects
)
}
projects'
)
summary
=
[]
# Process each project
for
slug
in
projects
:
start_prev
=
state
[
'projects'
]
.
get
(
slug
,
{})
.
get
(
'prev_cursor'
)
res
=
fetch_project_events
(
api_base
,
org
,
token
,
slug
,
start_prev
,
max_pages_per_project
,
bucket
,
prefix
)
if
res
.
get
(
'store_prev_cursor'
):
state
[
'projects'
][
slug
]
=
{
'prev_cursor'
:
res
[
'store_prev_cursor'
]}
summary
.
append
(
res
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
f
'Successfully processed
{
len
(
projects
)
}
projects'
)
print
(
f
'Summary:
{
json
.
dumps
(
summary
)
}
'
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
if
state_data
else
{
'projects'
:
{}}
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
{
'projects'
:
{}}
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
sentry_request
(
api_base
,
token
,
path
,
params
=
None
):
"""Make request to Sentry API."""
url
=
f
"
{
api_base
}{
path
}
"
if
params
:
url
=
f
"
{
url
}
?
{
urllib3
.
request
.
urlencode
(
params
)
}
"
headers
=
{
'Authorization'
:
f
'Bearer
{
token
}
'
,
'Accept'
:
'application/json'
,
'User-Agent'
:
'chronicle-gcs-sentry-function/1.0'
}
response
=
http
.
request
(
'GET'
,
url
,
headers
=
headers
,
timeout
=
60.0
)
data
=
json
.
loads
(
response
.
data
.
decode
(
'utf-8'
))
link
=
response
.
headers
.
get
(
'Link'
)
return
data
,
link
def
parse_link_header
(
link_header
):
"""Parse Link header to extract cursors."""
if
not
link_header
:
return
None
,
False
,
None
,
False
prev_cursor
,
next_cursor
=
None
,
None
prev_more
,
next_more
=
False
,
False
parts
=
[
p
.
strip
()
for
p
in
link_header
.
split
(
','
)]
for
p
in
parts
:
if
'<'
not
in
p
or
'>'
not
in
p
:
continue
url
=
p
.
split
(
'<'
,
1
)[
1
]
.
split
(
'>'
,
1
)[
0
]
rel
=
'previous'
if
'rel="previous"'
in
p
else
(
'next'
if
'rel="next"'
in
p
else
None
)
has_more
=
'results="true"'
in
p
try
:
from
urllib.parse
import
urlparse
,
parse_qs
q
=
urlparse
(
url
)
.
query
cur
=
parse_qs
(
q
)
.
get
(
'cursor'
,
[
None
])[
0
]
except
Exception
:
cur
=
None
if
rel
==
'previous'
:
prev_cursor
,
prev_more
=
cur
,
has_more
elif
rel
==
'next'
:
next_cursor
,
next_more
=
cur
,
has_more
return
prev_cursor
,
prev_more
,
next_cursor
,
next_more
def
write_page
(
bucket
,
prefix
,
project_slug
,
payload
,
page_idx
):
"""Write page of events to GCS."""
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
'
,
ts
)
}
/sentry-
{
project_slug
}
-
{
page_idx
:
05d
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
list_projects
(
api_base
,
org
,
token
,
max_projects
):
"""List Sentry projects."""
projects
,
cursor
=
[],
None
while
len
(
projects
)
<
max_projects
:
params
=
{
'cursor'
:
cursor
}
if
cursor
else
{}
data
,
link
=
sentry_request
(
api_base
,
token
,
f
'/api/0/organizations/
{
org
}
/projects/'
,
params
)
for
p
in
data
:
slug
=
p
.
get
(
'slug'
)
if
slug
:
projects
.
append
(
slug
)
if
len
(
projects
)
>
=
max_projects
:
break
_
,
_
,
next_cursor
,
next_more
=
parse_link_header
(
link
)
cursor
=
next_cursor
if
next_more
else
None
if
not
next_more
:
break
return
projects
def
fetch_project_events
(
api_base
,
org
,
token
,
project_slug
,
start_prev_cursor
,
max_pages
,
bucket
,
prefix
):
"""Fetch events for a project."""
pages
=
0
total
=
0
latest_prev_cursor_to_store
=
None
def
fetch_one
(
cursor
):
nonlocal
pages
,
total
,
latest_prev_cursor_to_store
params
=
{
'cursor'
:
cursor
}
if
cursor
else
{}
data
,
link
=
sentry_request
(
api_base
,
token
,
f
'/api/0/projects/
{
org
}
/
{
project_slug
}
/events/'
,
params
)
write_page
(
bucket
,
prefix
,
project_slug
,
data
,
pages
)
total
+=
len
(
data
)
if
isinstance
(
data
,
list
)
else
0
prev_c
,
prev_more
,
next_c
,
next_more
=
parse_link_header
(
link
)
latest_prev_cursor_to_store
=
prev_c
or
latest_prev_cursor_to_store
pages
+=
1
return
prev_c
,
prev_more
,
next_c
,
next_more
if
start_prev_cursor
:
# Poll new pages toward "previous" until no more
cur
=
start_prev_cursor
while
pages
<
max_pages
:
prev_c
,
prev_more
,
_
,
_
=
fetch_one
(
cur
)
if
not
prev_more
:
break
cur
=
prev_c
else
:
# First run: start at newest, then backfill older pages
prev_c
,
_
,
next_c
,
next_more
=
fetch_one
(
None
)
cur
=
next_c
while
next_more
and
pages
<
max_pages
:
_
,
_
,
next_c
,
next_more
=
fetch_one
(
cur
)
cur
=
next_c
return
{
'project'
:
project_slug
,
'pages'
:
pages
,
'written'
:
total
,
'store_prev_cursor'
:
latest_prev_cursor_to_store
}
```
*
Second
file
:
**
requirements
.
txt
:
**
functions-framework
3.*
 google-cloud-storage
2.*
 urllib3>=2.0.0
 ```
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
sentry-logs-collector-hourly
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
sentry-logs-trigger
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
sentry-logs-collector
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
Sentry Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Sentry
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
Configure a feed in Google SecOps to ingest Sentry logs
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
Sentry Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Sentry
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://sentry-logs/sentry/events/
Replace:
sentry-logs
: Your GCS bucket name.
sentry/events/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/sentry-logs/
With subfolder:
gs://company-logs/sentry/events/
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
Need more help?
Get answers from Community members and Google SecOps professionals.
