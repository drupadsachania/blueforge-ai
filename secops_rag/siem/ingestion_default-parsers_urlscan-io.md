# Collect URLScan IO logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/urlscan-io/  
**Scraped:** 2026-03-05T09:29:44.268328Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect URLScan IO logs
Supported in:
Google secops
SIEM
This document explains how to ingest URLScan IO logs to Google Security Operations using Google Cloud Storage. URLScan IO is a service that analyzes websites and provides detailed information about their behavior, security, and performance. It scans URLs and generates comprehensive reports including screenshots, HTTP transactions, DNS records, and threat intelligence data.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to URLScan IO tenant
Get URLScan IO prerequisites
Sign in to
URLScan IO
.
Click your profile icon.
Select
API Key
from the menu.
If you don't have an API key yet:
Click
Create API Key
button.
Enter a description for the API key (for example,
Google SecOps Integration
).
Click
Generate API Key
.
Copy and save in a secure location the following details:
API_KEY
: The generated API key string (format:
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
)
API Base URL
:
https://urlscan.io/api/v1
(this is constant for all users)
Note your API quota limits:
Free and Pro accounts are subject to per-minute, per-hour, and per-day limits that vary per action. Check your personal quotas or the API rate-limit headers for your exact limits.
For details, see the
URLScan IO API Rate Limits documentation
.
If you need to restrict searches to your organization's scans only, note down:
User identifier
: Your username or email (for use with
user:
search filter)
Team identifier
: If using teams feature (for use with
team:
search filter)
Verify API access
Test your API key before proceeding with the integration:
# Replace with your actual API key
API_KEY
=
"your-api-key-here"
# Test API access
curl
-v
-H
"API-Key:
${
API_KEY
}
"
"https://urlscan.io/api/v1/search/?q=date:>now-1h&size=1"
Expected response: HTTP 200 with JSON containing search results.
If you receive HTTP 401 or 403, verify your API key is correct and has not expired.
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
urlscan-logs-bucket
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
urlscan-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect URLScan IO logs
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
urlscan-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
urlscan-logs-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from URLScan IO API and writes them to GCS.
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
urlscan-collector
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
, choose the Pub/Sub topic (
urlscan-logs-trigger
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
urlscan-collector-sa
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
urlscan-logs-bucket
GCS bucket name
GCS_PREFIX
urlscan/
Prefix for log files
STATE_KEY
urlscan/state.json
State file path
API_KEY
your-urlscan-api-key
URLScan IO API key
API_BASE
https://urlscan.io/api/v1
API base URL
SEARCH_QUERY
date:>now-1h
Search query filter
PAGE_SIZE
100
Records per page
MAX_PAGES
10
Maximum pages to fetch
In the
Variables & Secrets
section, scroll down to
Requests
:
Request timeout
: Enter
600
seconds (10 minutes).
Go to the
Settings
tab:
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
timedelta
,
timezone
import
time
# Initialize HTTP client with timeouts
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
30.0
),
retries
=
False
,
)
# Initialize Storage client
storage_client
=
storage
.
Client
()
# Environment variables
GCS_BUCKET
=
os
.
environ
.
get
(
'GCS_BUCKET'
)
GCS_PREFIX
=
os
.
environ
.
get
(
'GCS_PREFIX'
,
'urlscan/'
)
STATE_KEY
=
os
.
environ
.
get
(
'STATE_KEY'
,
'urlscan/state.json'
)
API_KEY
=
os
.
environ
.
get
(
'API_KEY'
)
API_BASE
=
os
.
environ
.
get
(
'API_BASE'
,
'https://urlscan.io/api/v1'
)
SEARCH_QUERY
=
os
.
environ
.
get
(
'SEARCH_QUERY'
,
'date:>now-1h'
)
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
'PAGE_SIZE'
,
'100'
))
MAX_PAGES
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
def
parse_datetime
(
value
:
str
)
-
>
datetime
:
"""Parse ISO datetime string to datetime object."""
if
value
.
endswith
(
"Z"
):
value
=
value
[:
-
1
]
+
"+00:00"
return
datetime
.
fromisoformat
(
value
)
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch URLScan IO results and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
API_KEY
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
GCS_BUCKET
)
# Load state
state
=
load_state
(
bucket
,
STATE_KEY
)
last_run
=
state
.
get
(
'last_run'
)
# Adjust search query based on last run
search_query
=
SEARCH_QUERY
if
last_run
:
try
:
search_time
=
parse_datetime
(
last_run
)
time_diff
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
search_time
hours
=
int
(
time_diff
.
total_seconds
()
/
3600
)
+
1
search_query
=
f
'date:>now-
{
hours
}
h'
except
Exception
as
e
:
print
(
f
'Warning: Could not parse last_run:
{
e
}
'
)
print
(
f
'Searching with query:
{
search_query
}
'
)
# Fetch logs
records
,
newest_event_time
=
fetch_logs
(
api_base
=
API_BASE
,
api_key
=
API_KEY
,
search_query
=
search_query
,
page_size
=
PAGE_SIZE
,
max_pages
=
MAX_PAGES
,
)
if
not
records
:
print
(
"No new log records found."
)
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
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
return
# Write to GCS as NDJSON
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
file_key
=
f
"
{
GCS_PREFIX
}
year=
{
now
.
year
}
/month=
{
now
.
month
:
02d
}
/day=
{
now
.
day
:
02d
}
/hour=
{
now
.
hour
:
02d
}
/urlscan_
{
now
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
}
.json"
ndjson_content
=
'
\n
'
.
join
([
json
.
dumps
(
r
,
separators
=
(
','
,
':'
))
for
r
in
records
])
blob
=
bucket
.
blob
(
file_key
)
blob
.
upload_from_string
(
ndjson_content
,
content_type
=
'application/x-ndjson'
)
print
(
f
"Uploaded
{
len
(
records
)
}
results to gs://
{
GCS_BUCKET
}
/
{
file_key
}
"
)
# Update state with newest event time
if
newest_event_time
:
save_state
(
bucket
,
STATE_KEY
,
newest_event_time
)
else
:
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
print
(
f
'Successfully processed
{
len
(
records
)
}
scan results'
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
last_event_time_iso
:
str
):
"""Save the last event timestamp to GCS state file."""
try
:
state
=
{
'last_run'
:
last_event_time_iso
}
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
indent
=
2
),
content_type
=
'application/json'
)
print
(
f
"Saved state: last_run=
{
last_event_time_iso
}
"
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
fetch_logs
(
api_base
:
str
,
api_key
:
str
,
search_query
:
str
,
page_size
:
int
,
max_pages
:
int
):
"""
Fetch logs from URLScan IO API with pagination and rate limiting.
Args:
api_base: API base URL
api_key: URLScan IO API key
search_query: Search query string
page_size: Number of records per page
max_pages: Maximum total pages to fetch
Returns:
Tuple of (records list, newest_event_time ISO string)
"""
headers
=
{
'API-Key'
:
api_key
,
'Accept'
:
'application/json'
,
'User-Agent'
:
'GoogleSecOps-URLScanCollector/1.0'
}
all_results
=
[]
newest_time
=
None
page_num
=
0
backoff
=
1.0
offset
=
0
while
page_num
<
max_pages
:
page_num
+=
1
# Build search URL with pagination
search_url
=
f
"
{
api_base
}
/search/"
params
=
[
f
"q=
{
search_query
}
"
,
f
"size=
{
page_size
}
"
,
f
"offset=
{
offset
}
"
]
url
=
f
"
{
search_url
}
?
{
'&'
.
join
(
params
)
}
"
try
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
)
# Handle rate limiting with exponential backoff
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
"Rate limited (429). Retrying after
{
retry_after
}
s..."
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
continue
backoff
=
1.0
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
"Search failed:
{
response
.
status
}
"
)
response_text
=
response
.
data
.
decode
(
'utf-8'
)
print
(
f
"Response body:
{
response_text
}
"
)
break
search_data
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
results
=
search_data
.
get
(
'results'
,
[])
if
not
results
:
print
(
f
"No more results (empty page)"
)
break
print
(
f
"Page
{
page_num
}
: Retrieved
{
len
(
results
)
}
scan results"
)
# Fetch full result for each scan
for
result
in
results
:
task
=
result
.
get
(
'task'
,
{})
uuid
=
task
.
get
(
'uuid'
)
if
uuid
:
result_url
=
f
"
{
api_base
}
/result/
{
uuid
}
/"
try
:
result_response
=
http
.
request
(
'GET'
,
result_url
,
headers
=
headers
)
# Handle rate limiting
if
result_response
.
status
==
429
:
retry_after
=
int
(
result_response
.
headers
.
get
(
'Retry-After'
,
'5'
))
print
(
f
"Rate limited on result fetch. Retrying after
{
retry_after
}
s..."
)
time
.
sleep
(
retry_after
)
result_response
=
http
.
request
(
'GET'
,
result_url
,
headers
=
headers
)
if
result_response
.
status
==
200
:
full_result
=
json
.
loads
(
result_response
.
data
.
decode
(
'utf-8'
))
all_results
.
append
(
full_result
)
# Track newest event time
try
:
event_time
=
task
.
get
(
'time'
)
if
event_time
:
if
newest_time
is
None
or
parse_datetime
(
event_time
)
>
parse_datetime
(
newest_time
):
newest_time
=
event_time
except
Exception
as
e
:
print
(
f
"Warning: Could not parse event time:
{
e
}
"
)
else
:
print
(
f
"Failed to fetch result for
{
uuid
}
:
{
result_response
.
status
}
"
)
except
Exception
as
e
:
print
(
f
"Error fetching result for
{
uuid
}
:
{
e
}
"
)
# Check if we have more pages
total
=
search_data
.
get
(
'total'
,
0
)
if
offset
+
len
(
results
)
>
=
total
or
len
(
results
)
<
page_size
:
print
(
f
"Reached last page (offset=
{
offset
}
, results=
{
len
(
results
)
}
, total=
{
total
}
)"
)
break
offset
+=
len
(
results
)
except
Exception
as
e
:
print
(
f
"Error fetching logs:
{
e
}
"
)
return
[],
None
print
(
f
"Retrieved
{
len
(
all_results
)
}
total records from
{
page_num
}
pages"
)
return
all_results
,
newest_time
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
urlscan-collector-hourly
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
Select the Pub/Sub topic (
urlscan-logs-trigger
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
Test the integration
In the
Cloud Scheduler
console, find your job (
urlscan-collector-hourly
).
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click the function name (
urlscan-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Searching
with
query
:
date
:
>
now
-
1
h
Page
1
:
Retrieved
X
scan
results
Uploaded
X
results
to
gs
:
//
bucket
-
name
/
urlscan
/
year
=
YYYY
/
month
=
MM
/
day
=
DD
/
hour
=
HH
/
urlscan_YYYYMMDD_HHMMSS
.
json
Successfully
processed
X
scan
results
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
urlscan/
).
Verify that a new
.json
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API key in environment variables
HTTP 403
: Verify API key has not expired
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set
Search failed
: Verify search query syntax is correct
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
URLScan IO logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
URLScan IO
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
Configure a feed in Google SecOps to ingest URLScan IO logs
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
URLScan IO logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
URLScan IO
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://urlscan-logs-bucket/urlscan/
Replace:
urlscan-logs-bucket
: Your GCS bucket name.
urlscan/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://urlscan-logs-bucket/
With prefix:
gs://urlscan-logs-bucket/urlscan/
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
