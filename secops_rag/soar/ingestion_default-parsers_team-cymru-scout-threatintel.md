# Collect Team Cymru Scout Threat Intelligence logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-threatintel/  
**Scraped:** 2026-03-05T10:01:21.333277Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Team Cymru Scout Threat Intelligence logs
Supported in:
Google secops
SIEM
This document explains how to ingest Team Cymru Scout Threat Intelligence data to Google Security Operations using Google Cloud Storage. Team Cymru Scout provides threat intelligence data including account usage metrics, query limits, and foundation query statistics to help organizations monitor their security posture and threat intelligence consumption.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Team Cymru Scout tenant
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
team-cymru-scout-ti
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
Collect Team Cymru Scout API credentials
Sign in to the
Team Cymru Scout Platform
.
Go to the
API Keys
page.
Click the
Create
button.
Provide the description for the key, if needed.
Click the
Create Key
button to generate the API key.
Copy and save in a secure location the following details:
SCOUT_API_TOKEN
: API access token
SCOUT_BASE_URL
: Scout API base URL (typically
https://scout.cymru.com
)
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
SCOUT_API_TOKEN
=
"your-api-token"
SCOUT_BASE_URL
=
"https://scout.cymru.com"
# Test API access to usage endpoint
curl
-v
--request
GET
\
--url
"
${
SCOUT_BASE_URL
}
/api/scout/usage"
\
--header
"Authorization: Token
${
SCOUT_API_TOKEN
}
"
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
team-cymru-scout-ti-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Team Cymru Scout Threat Intelligence data
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
team-cymru-scout-ti-sa@PROJECT_ID.iam.gserviceaccount.com
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
team-cymru-scout-ti-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect threat intelligence data
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch threat intelligence data from Team Cymru Scout API and writes them to GCS.
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
team-cymru-scout-ti-collector
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
In*
Select a Cloud Pub/Sub topic
*, choose the topic
team-cymru-scout-ti-trigger
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
team-cymru-scout-ti-sa
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
team-cymru-scout-ti
GCS_PREFIX
team-cymru/scout-ti/
STATE_KEY
team-cymru/scout-ti/state.json
SCOUT_BASE_URL
https://scout.cymru.com
SCOUT_API_TOKEN
your-scout-api-token
COLLECTION_INTERVAL_HOURS
1
HTTP_TIMEOUT
60
HTTP_RETRIES
3
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
Cloud Run function triggered by Pub/Sub to fetch usage data from Team Cymru Scout API and write to GCS.
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
'team-cymru/scout-ti/'
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
'team-cymru/scout-ti/state.json'
)
collection_interval_hours
=
int
(
os
.
environ
.
get
(
'COLLECTION_INTERVAL_HOURS'
,
'1'
))
http_timeout
=
int
(
os
.
environ
.
get
(
'HTTP_TIMEOUT'
,
'60'
))
http_retries
=
int
(
os
.
environ
.
get
(
'HTTP_RETRIES'
,
'3'
))
# Team Cymru Scout API credentials
scout_base_url
=
os
.
environ
.
get
(
'SCOUT_BASE_URL'
,
'https://scout.cymru.com'
)
scout_api_token
=
os
.
environ
.
get
(
'SCOUT_API_TOKEN'
)
if
not
all
([
bucket_name
,
scout_api_token
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
# Load state (last collection timestamp)
state
=
load_state
(
bucket
,
state_key
)
now
=
time
.
time
()
last_collection
=
state
.
get
(
'last_collection_ts'
,
now
-
(
collection_interval_hours
*
3600
))
print
(
f
'Collecting usage data at
{
iso_format
(
now
)
}
(last collection:
{
iso_format
(
last_collection
)
}
)'
)
# Fetch usage data from Team Cymru Scout API
usage_data
=
fetch_usage_data
(
scout_base_url
,
scout_api_token
,
http_timeout
,
http_retries
)
if
usage_data
:
# Add timestamp and event type
usage_data
[
'event_type'
]
=
'account_usage'
usage_data
[
'collection_timestamp'
]
=
iso_format
(
now
)
# Write to GCS
write_to_gcs
(
bucket
,
prefix
,
usage_data
,
now
)
# Update state
save_state
(
bucket
,
state_key
,
{
'last_collection_ts'
:
now
})
print
(
f
'Successfully collected and stored usage data'
)
else
:
print
(
'No usage data retrieved'
)
except
Exception
as
e
:
print
(
f
'Error processing usage data:
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
iso_format
(
ts
):
"""Convert Unix timestamp to ISO 8601 format."""
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
http_request
(
url
,
method
=
'GET'
,
body
=
None
,
headers
=
None
,
timeout
=
60
,
retries
=
3
):
"""Make HTTP request with retry logic."""
attempt
=
0
while
True
:
try
:
req_headers
=
headers
or
{}
if
body
is
not
None
:
req_headers
[
'Content-Type'
]
=
'application/json'
body_bytes
=
body
.
encode
(
'utf-8'
)
if
isinstance
(
body
,
str
)
else
body
else
:
body_bytes
=
None
response
=
http
.
request
(
method
,
url
,
body
=
body_bytes
,
headers
=
req_headers
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
200
:
return
response
.
data
,
response
.
headers
.
get
(
'Content-Type'
,
'application/json'
)
elif
response
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
)
and
attempt
<
retries
:
delay
=
1
+
attempt
retry_after
=
response
.
headers
.
get
(
'Retry-After'
)
if
retry_after
:
try
:
delay
=
int
(
retry_after
)
except
:
pass
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
attempt
+=
1
continue
else
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
except
urllib3
.
exceptions
.
HTTPError
as
e
:
if
attempt
<
retries
:
time
.
sleep
(
1
+
attempt
)
attempt
+=
1
continue
raise
def
fetch_usage_data
(
base_url
,
api_token
,
timeout
,
retries
):
"""
Fetch usage data from Team Cymru Scout API.
Implementation mirrors the official Scout API example:
curl --request GET --url 'https://scout.cymru.com/api/scout/usage' --header 'Authorization: Token valid_api_token'
"""
# Use the documented /api/scout/usage endpoint
url
=
f
'
{
base_url
}
/api/scout/usage'
# Use Token authentication as documented
headers
=
{
'Authorization'
:
f
'Token
{
api_token
}
'
,
'Accept'
:
'application/json'
}
print
(
f
'Fetching usage data from
{
url
}
'
)
try
:
# Fetch data
blob_data
,
content_type
=
http_request
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
,
timeout
=
timeout
,
retries
=
retries
)
# Parse response
usage_data
=
json
.
loads
(
blob_data
.
decode
(
'utf-8'
))
print
(
f
'Retrieved usage data: used_queries=
{
usage_data
.
get
(
"used_queries"
)
}
, query_limit=
{
usage_data
.
get
(
"query_limit"
)
}
'
)
return
usage_data
except
Exception
as
e
:
print
(
f
'Error fetching usage data:
{
e
}
'
)
return
None
def
write_to_gcs
(
bucket
,
prefix
,
data
,
timestamp
):
"""Write data to GCS."""
# Create date-based path
date_path
=
time
.
strftime
(
'%Y/%m/
%d
'
,
time
.
gmtime
(
timestamp
))
key
=
f
'
{
prefix
}{
date_path
}
/usage_
{
int
(
timestamp
)
}
.json'
# Write as JSON
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
data
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
'Wrote data to gs://
{
bucket
.
name
}
/
{
key
}
'
)
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
team-cymru-scout-ti-hourly
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
team-cymru-scout-ti-trigger
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose frequency based on data volume and latency requirements:
Frequency
Cron Expression
Use Case
Every 5 minutes
*/5 * * * *
High-frequency monitoring
Every 15 minutes
*/15 * * * *
Medium frequency
Every hour
0 * * * *
Standard (recommended)
Every 6 hours
0 */6 * * *
Low frequency
Daily
0 0 * * *
Daily usage tracking
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
team-cymru-scout-ti-collector
>
Logs
.
Verify the function executed successfully.
Check the GCS bucket to confirm usage data was written.
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
Team Cymru Scout Threat Intelligence
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Team Cymru Scout Threat Intelligence
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
Configure a feed in Google SecOps to ingest Team Cymru Scout Threat Intelligence data
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
Team Cymru Scout Threat Intelligence
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Team Cymru Scout Threat Intelligence
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://team-cymru-scout-ti/team-cymru/scout-ti/
Replace:
team-cymru-scout-ti
: Your GCS bucket name.
team-cymru/scout-ti/
: Prefix/folder path where logs are stored.
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
