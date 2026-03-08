# Collect PingOne Advanced Identity Cloud logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-identity-cloud/  
**Scraped:** 2026-03-05T09:59:12.298255Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect PingOne Advanced Identity Cloud logs
Supported in:
Google secops
SIEM
This document explains how to ingest PingOne Advanced Identity Cloud (formerly ForgeRock Identity Cloud) logs to Google Security Operations using Google Cloud Storage. PingOne Advanced Identity Cloud is an identity and access management platform that provides authentication, authorization, and user management capabilities for cloud-based applications.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to PingOne Advanced Identity Cloud tenant
Get PingOne API key and tenant FQDN
Sign in to the Advanced Identity Cloud admin console.
Click the user icon
>
Tenant Settings
.
On the
Global Settings
tab, click
Log API Keys
.
Click
New Log API Key
, provide a name for the key.
Click
Create Key
.
Copy and save the
api_key_id
and
api_key_secret
values in a secure location. The
api_key_secret
value is not displayed again.
Click
Done
.
Go to
Tenant Settings
>
Details
, and find your tenant FQDN (for example,
example.tomcat.pingone.com
).
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
pingone-aic-logs
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
pingone-aic-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect PingOne Advanced Identity Cloud logs
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
pingone-aic-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
pingone-aic-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from PingOne Advanced Identity Cloud API and writes them to GCS.
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
pingone-aic-collector
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
pingone-aic-trigger
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
pingone-aic-collector-sa
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
pingone-aic-logs
GCS bucket name
GCS_PREFIX
pingone-aic/logs
Prefix for log files
STATE_KEY
pingone-aic/logs/state.json
State file path
AIC_TENANT_FQDN
example.tomcat.pingone.com
Tenant FQDN
AIC_API_KEY_ID
your-api-key-id
API key ID
AIC_API_SECRET
your-api-key-secret
API key secret
SOURCES
am-everything,idm-everything
Comma-separated log sources (see note below)
PAGE_SIZE
500
Records per page
MAX_PAGES
20
Maximum pages per run
LOOKBACK_SECONDS
3600
Initial lookback period
In the
Variables & Secrets
section, scroll to
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
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch logs from PingOne Advanced Identity Cloud API and write to GCS.
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
'pingone-aic/logs'
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
'pingone-aic/logs/state.json'
)
fqdn
=
os
.
environ
.
get
(
'AIC_TENANT_FQDN'
,
''
)
.
strip
(
'/'
)
api_key_id
=
os
.
environ
.
get
(
'AIC_API_KEY_ID'
)
api_key_secret
=
os
.
environ
.
get
(
'AIC_API_SECRET'
)
sources
=
[
s
.
strip
()
for
s
in
os
.
environ
.
get
(
'SOURCES'
,
'am-everything,idm-everything'
)
.
split
(
','
)
if
s
.
strip
()]
page_size
=
min
(
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
'500'
)),
1000
)
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
fqdn
,
api_key_id
,
api_key_secret
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
'sources'
,
{})
summary
=
[]
for
source
in
sources
:
last_ts
=
state
[
'sources'
]
.
get
(
source
,
{})
.
get
(
'last_ts'
)
res
=
fetch_source
(
bucket
,
prefix
,
fqdn
,
api_key_id
,
api_key_secret
,
source
,
last_ts
,
page_size
,
max_pages
,
lookback_seconds
)
if
res
.
get
(
'newest_ts'
):
state
[
'sources'
][
source
]
=
{
'last_ts'
:
res
[
'newest_ts'
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
'Successfully processed logs:
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
'sources'
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
fetch_source
(
bucket
,
prefix
,
fqdn
,
api_key_id
,
api_key_secret
,
source
,
last_ts
,
page_size
,
max_pages
,
lookback_seconds
):
"""Fetch logs for a specific source."""
base_url
=
f
"https://
{
fqdn
}
/monitoring/logs"
now
=
time
.
time
()
begin_time
=
bounded_begin_time
(
last_ts
,
now
,
lookback_seconds
)
params
=
{
'source'
:
source
,
'_pageSize'
:
str
(
page_size
),
'_sortKeys'
:
'timestamp'
,
'beginTime'
:
begin_time
}
headers
=
{
'x-api-key'
:
api_key_id
,
'x-api-secret'
:
api_key_secret
}
pages
=
0
written
=
0
newest_ts
=
last_ts
cookie
=
None
while
pages
<
max_pages
:
if
cookie
:
params
[
'_pagedResultsCookie'
]
=
cookie
# Build query string
query_parts
=
[
f
"
{
k
}
=
{
v
}
"
for
k
,
v
in
params
.
items
()]
query_string
=
'&'
.
join
(
query_parts
)
url
=
f
"
{
base_url
}
?
{
query_string
}
"
# Make request with retry logic
data
=
http_get_with_retry
(
url
,
headers
)
# Write page to GCS
write_page
(
bucket
,
prefix
,
data
,
source
)
# Process results
results
=
data
.
get
(
'result'
)
or
data
.
get
(
'results'
)
or
[]
for
item
in
results
:
t
=
item
.
get
(
'timestamp'
)
or
item
.
get
(
'payload'
,
{})
.
get
(
'timestamp'
)
if
t
and
(
newest_ts
is
None
or
t
>
newest_ts
):
newest_ts
=
t
written
+=
len
(
results
)
cookie
=
data
.
get
(
'pagedResultsCookie'
)
pages
+=
1
if
not
cookie
:
break
return
{
'source'
:
source
,
'pages'
:
pages
,
'written'
:
written
,
'newest_ts'
:
newest_ts
}
def
http_get_with_retry
(
url
,
headers
,
timeout
=
60
,
max_retries
=
5
):
"""Make HTTP GET request with retry logic."""
attempt
=
0
backoff
=
1.0
while
True
:
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
,
timeout
=
timeout
)
if
response
.
status
==
429
and
attempt
<
max_retries
:
# Rate limited - check for X-RateLimit-Reset header
reset_header
=
response
.
headers
.
get
(
'X-RateLimit-Reset'
)
if
reset_header
:
delay
=
max
(
1
,
int
(
reset_header
)
-
int
(
time
.
time
()))
else
:
delay
=
int
(
backoff
)
print
(
f
'Rate limited, waiting
{
delay
}
seconds'
)
time
.
sleep
(
delay
)
attempt
+=
1
backoff
*=
2
continue
if
500
<
=
response
.
status
<
600
and
attempt
<
max_retries
:
print
(
f
'Server error
{
response
.
status
}
, retrying in
{
backoff
}
seconds'
)
time
.
sleep
(
backoff
)
attempt
+=
1
backoff
*=
2
continue
if
response
.
status
!=
200
:
raise
Exception
(
f
'HTTP
{
response
.
status
}
:
{
response
.
data
.
decode
(
"utf-8"
)
}
'
)
return
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
except
Exception
as
e
:
if
attempt
<
max_retries
:
print
(
f
'Request failed:
{
str
(
e
)
}
, retrying in
{
backoff
}
seconds'
)
time
.
sleep
(
backoff
)
attempt
+=
1
backoff
*=
2
continue
raise
def
write_page
(
bucket
,
prefix
,
payload
,
source
):
"""Write a page of logs to GCS."""
ts
=
datetime
.
now
(
timezone
.
utc
)
blob_name
=
f
"
{
prefix
}
/
{
ts
.
strftime
(
'%Y/%m/
%d
/%H%M%S'
)
}
-pingone-aic-
{
source
}
.json"
blob
=
bucket
.
blob
(
blob_name
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
'Wrote logs to
{
blob_name
}
'
)
def
bounded_begin_time
(
last_ts
,
now
,
lookback_seconds
):
"""Calculate begin time bounded by 24 hour limit."""
twenty_four_h_ago
=
now
-
24
*
3600
if
last_ts
:
try
:
# Parse ISO timestamp
t_struct
=
time
.
strptime
(
last_ts
[:
19
]
+
'Z'
,
'%Y-%m-
%d
T%H:%M:%SZ'
)
t_epoch
=
int
(
time
.
mktime
(
t_struct
))
except
Exception
:
t_epoch
=
int
(
now
-
lookback_seconds
)
begin_epoch
=
max
(
t_epoch
,
int
(
twenty_four_h_ago
))
else
:
begin_epoch
=
max
(
int
(
now
-
lookback_seconds
),
int
(
twenty_four_h_ago
))
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
begin_epoch
))
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
Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
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
pingone-aic-collector-hourly
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
pingone-aic-trigger
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
pingone-aic-collector-hourly
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
pingone-aic-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
Page 1: Retrieved X events
Wrote logs to gs://bucket-name/prefix/logs_YYYYMMDD_HHMMSS.json
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (
pingone-aic-logs
).
Navigate to the prefix folder (
pingone-aic/logs/
).
Verify that a new
.json
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables
HTTP 403
: Verify account has required permissions
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set
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
PingOne Advanced Identity Cloud
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
PingOne Advanced Identity Cloud
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
Click your bucket name (
pingone-aic-logs
).
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
Configure a feed in Google SecOps to ingest PingOne Advanced Identity Cloud logs
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
PingOne Advanced Identity Cloud
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
PingOne Advanced Identity Cloud
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://pingone-aic-logs/pingone-aic/logs/
Replace:
pingone-aic-logs
: Your GCS bucket name.
pingone-aic/logs/
: Optional prefix/folder path where logs are stored.
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
