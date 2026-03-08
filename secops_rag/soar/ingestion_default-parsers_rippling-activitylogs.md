# Collect Rippling activity logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs/  
**Scraped:** 2026-03-05T09:59:38.383599Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Rippling activity logs
Supported in:
Google secops
SIEM
This document explains how to ingest Rippling activity logs to Google Security Operations using Google Cloud Storage. Rippling is a workforce management platform that provides HR, IT, and Finance solutions including payroll, benefits, employee onboarding, device management, and application provisioning. The Company Activity API provides audit logs of administrative and user actions across the Rippling platform.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Rippling (API token with access to Company Activity)
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
rippling-activity-logs
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
Collect Rippling API credentials
Sign in to
Rippling Admin
.
Go to
Search
>
API Tokens
.
Alternative path:
Settings
>
Company Settings
>
API Tokens
.
Click
Create API token
.
Provide the following configuration details:
Name
: Enter a unique and meaningful name (for example,
Google SecOps GCS Export
).
API version
: Select
Base API (v1)
.
Scopes/Permissions
: Enable
company:activity:read
(required for Company Activity).
Click
Create
.
Copy and save the token value in a secure location. You will use it as a bearer token.
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
rippling-logs-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Rippling activity logs
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
rippling-logs-collector-sa@your-project.iam.gserviceaccount.com
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
rippling-activity-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Rippling Company Activity API and write them to GCS.
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
rippling-activity-collector
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
rippling-activity-trigger
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
rippling-logs-collector-sa
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
rippling-activity-logs
GCS_PREFIX
rippling/activity/
STATE_KEY
rippling/activity/state.json
RIPPLING_API_TOKEN
your-api-token
RIPPLING_ACTIVITY_URL
https://api.rippling.com/platform/api/company_activity
LIMIT
1000
MAX_PAGES
10
LOOKBACK_MINUTES
60
END_LAG_SECONDS
120
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
,
timedelta
import
time
# Initialize HTTP client
http
=
urllib3
.
PoolManager
(
timeout
=
urllib3
.
Timeout
(
connect
=
5.0
,
read
=
60.0
),
retries
=
False
)
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
Cloud Run function triggered by Pub/Sub to fetch logs from Rippling Company Activity API and write to GCS.
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
'rippling/activity/'
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
'rippling/activity/state.json'
)
# Rippling API configuration
api_token
=
os
.
environ
.
get
(
'RIPPLING_API_TOKEN'
)
activity_url
=
os
.
environ
.
get
(
'RIPPLING_ACTIVITY_URL'
,
'https://api.rippling.com/platform/api/company_activity'
)
limit
=
int
(
os
.
environ
.
get
(
'LIMIT'
,
'1000'
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
'10'
))
lookback_minutes
=
int
(
os
.
environ
.
get
(
'LOOKBACK_MINUTES'
,
'60'
))
end_lag_seconds
=
int
(
os
.
environ
.
get
(
'END_LAG_SECONDS'
,
'120'
))
if
not
all
([
bucket_name
,
api_token
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
# Load state (last processed timestamp and cursor)
state
=
load_state
(
bucket
,
state_key
)
since_iso
=
state
.
get
(
'since'
)
next_cursor
=
state
.
get
(
'next'
)
# Calculate time window
run_end
=
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
seconds
=
end_lag_seconds
)
end_iso
=
run_end
.
replace
(
microsecond
=
0
)
.
isoformat
()
.
replace
(
'+00:00'
,
'Z'
)
if
since_iso
is
None
:
since_iso
=
iso_from_epoch
(
time
.
time
()
-
lookback_minutes
*
60
)
else
:
try
:
since_iso
=
(
parse_iso
(
since_iso
)
+
timedelta
(
seconds
=
1
))
.
replace
(
microsecond
=
0
)
.
isoformat
()
.
replace
(
'+00:00'
,
'Z'
)
except
Exception
:
since_iso
=
iso_from_epoch
(
time
.
time
()
-
lookback_minutes
*
60
)
print
(
f
'Processing logs from
{
since_iso
}
to
{
end_iso
}
'
)
run_ts_iso
=
end_iso
pages
=
0
total
=
0
newest_ts
=
None
pending_next
=
None
# Fetch logs with pagination
while
pages
<
max_pages
:
params
=
{
'limit'
:
str
(
limit
)}
if
next_cursor
:
params
[
'next'
]
=
next_cursor
else
:
params
[
'startDate'
]
=
since_iso
params
[
'endDate'
]
=
end_iso
# Build URL with query parameters
url
=
build_url
(
activity_url
,
params
)
# Fetch data from Rippling API
headers
=
{
'Authorization'
:
f
'Bearer
{
api_token
}
'
,
'Accept'
:
'application/json'
}
# Implement exponential backoff for rate limiting
backoff
=
1.0
max_retries
=
3
retry_count
=
0
while
retry_count
<
max_retries
:
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
if
response
.
status
==
429
:
retry_after
=
int
(
response
.
headers
.
get
(
'Retry-After'
,
str
(
int
(
backoff
))))
print
(
f
'Rate limited (429). Retrying after
{
retry_after
}
s...'
)
time
.
sleep
(
retry_after
)
backoff
=
min
(
backoff
*
2
,
30.0
)
retry_count
+=
1
continue
break
if
response
.
status
!=
200
:
print
(
f
'Error: API returned status
{
response
.
status
}
'
)
break
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
# Write page to GCS
write_to_gcs
(
bucket
,
prefix
,
data
,
run_ts_iso
,
pages
)
# Extract events
events
=
data
.
get
(
'events'
)
or
[]
total
+=
len
(
events
)
if
isinstance
(
events
,
list
)
else
0
# Track newest timestamp
if
isinstance
(
events
,
list
):
for
ev
in
events
:
t
=
ev
.
get
(
'timestamp'
)
or
ev
.
get
(
'time'
)
or
ev
.
get
(
'event_time'
)
if
isinstance
(
t
,
str
):
try
:
dt_ts
=
parse_iso
(
t
)
if
newest_ts
is
None
or
dt_ts
>
newest_ts
:
newest_ts
=
dt_ts
except
Exception
:
pass
# Check for next page
nxt
=
data
.
get
(
'next'
)
pages
+=
1
if
nxt
:
next_cursor
=
nxt
pending_next
=
nxt
continue
else
:
pending_next
=
None
break
# Update state
new_since_iso
=
(
newest_ts
or
run_end
)
.
replace
(
microsecond
=
0
)
.
isoformat
()
.
replace
(
'+00:00'
,
'Z'
)
save_state
(
bucket
,
state_key
,
{
'since'
:
new_since_iso
,
'next'
:
pending_next
})
print
(
f
'Successfully processed
{
total
}
events across
{
pages
}
pages'
)
print
(
f
'Updated state: since=
{
new_since_iso
}
, next=
{
pending_next
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
write_to_gcs
(
bucket
,
prefix
,
payload
,
run_ts_iso
,
page_index
):
"""Write payload to GCS."""
try
:
day_path
=
parse_iso
(
run_ts_iso
)
.
strftime
(
'%Y/%m/
%d
'
)
key
=
f
"
{
prefix
.
strip
(
'/'
)
}
/
{
day_path
}
/
{
run_ts_iso
.
replace
(
':'
,
''
)
.
replace
(
'-'
,
''
)
}
-page
{
page_index
:
05d
}
-company_activity.json"
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
print
(
f
'Wrote page
{
page_index
}
to
{
key
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
'Error writing to GCS:
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
parse_iso
(
ts
):
"""Parse ISO 8601 timestamp."""
if
ts
.
endswith
(
'Z'
):
ts
=
ts
[:
-
1
]
+
'+00:00'
return
datetime
.
fromisoformat
(
ts
)
def
iso_from_epoch
(
sec
):
"""Convert epoch seconds to ISO 8601 timestamp."""
return
datetime
.
fromtimestamp
(
sec
,
tz
=
timezone
.
utc
)
.
replace
(
microsecond
=
0
)
.
isoformat
()
.
replace
(
'+00:00'
,
'Z'
)
def
build_url
(
base
,
params
):
"""Build URL with query parameters."""
if
not
params
:
return
base
query_string
=
'&'
.
join
([
f
'
{
k
}
=
{
v
}
'
for
k
,
v
in
params
.
items
()])
return
f
'
{
base
}
?
{
query_string
}
'
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
rippling-activity-hourly
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
rippling-activity-trigger
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
rippling-activity-collector
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
Rippling Activity Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Rippling Activity Logs
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
Configure a feed in Google SecOps to ingest Rippling Activity Logs
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
Rippling Activity Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Rippling Activity Logs
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://rippling-activity-logs/rippling/activity/
Replace:
rippling-activity-logs
: Your GCS bucket name.
rippling/activity/
: Prefix/folder path where logs are stored (must match
GCS_PREFIX
environment variable).
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
rippling.activity
).
Ingestion labels
: Optional label to be applied to the events from this feed.
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
