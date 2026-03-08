# Snipe-IT logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it/  
**Scraped:** 2026-03-05T09:28:18.544225Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Snipe-IT logs
Supported in:
Google secops
SIEM
This document explains how to ingest Snipe-IT logs to Google Security Operations using Google Cloud Storage. Snipe-IT is an open-source IT asset management system that tracks hardware, software licenses, accessories, consumables, and other IT assets throughout their lifecycle.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to the Snipe-IT tenant
Collect Snipe-IT prerequisites (API token and base URL)
Sign in to Snipe-IT.
Open your user menu (top-right avatar) and click
Manage API keys
.
Click
Create New Token
:
Name/Label
: Enter a descriptive label (for example,
Google SecOps export
).
Click
Generate
.
Copy the API token (it will be shown only once). Store it securely.
Determine your API base URL, typically:
https://<your-domain>/api/v1
Example:
https://snipeit.example.com/api/v1
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
snipe-it-logs
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
snipeit-assets-to-gcs-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Snipe-IT logs
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
snipeit-assets-to-gcs-sa@PROJECT_ID.iam.gserviceaccount.com
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
snipeit-assets-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch hardware assets from Snipe-IT API and writes them to GCS.
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
snipeit-assets-to-gcs
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
snipeit-assets-trigger
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
snipeit-assets-to-gcs-sa
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
snipe-it-logs
GCS_PREFIX
snipeit/assets
SNIPE_BASE_URL
https://snipeit.example.com/api/v1
SNIPE_API_TOKEN
your-api-token
PAGE_SIZE
500
MAX_PAGES
200
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
urllib.parse
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
Cloud Run function triggered by Pub/Sub to fetch hardware assets from Snipe-IT API and write to GCS.
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
'snipeit/assets'
)
base_url
=
os
.
environ
.
get
(
'SNIPE_BASE_URL'
,
''
)
.
rstrip
(
'/'
)
token
=
os
.
environ
.
get
(
'SNIPE_API_TOKEN'
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
'PAGE_SIZE'
,
'500'
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
'200'
))
if
not
all
([
bucket_name
,
base_url
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
# Fetch and write pages
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
offset
=
0
page
=
0
total
=
0
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
'Content-Type'
:
'application/json'
}
while
page
<
max_pages
:
# Fetch page from Snipe-IT API
params
=
{
'limit'
:
page_size
,
'offset'
:
offset
,
'sort'
:
'id'
,
'order'
:
'asc'
}
qs
=
urllib
.
parse
.
urlencode
(
params
)
url
=
f
"
{
base_url
}
/hardware?
{
qs
}
"
print
(
f
'Fetching page
{
page
}
from
{
url
}
'
)
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
# Get rows from response (Snipe-IT uses 'rows' field)
rows
=
data
.
get
(
'rows'
,
[])
total_available
=
data
.
get
(
'total'
,
0
)
# Write page to GCS
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
'
)
}
/snipeit-hardware-
{
page
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
blob_name
)
body
=
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
))
.
encode
(
'utf-8'
)
blob
.
upload_from_string
(
body
,
content_type
=
'application/json'
)
print
(
f
'Wrote page
{
page
}
with
{
len
(
rows
)
}
rows to
{
blob_name
}
'
)
total
+=
len
(
rows
)
# Check if we've reached the end
# Snipe-IT returns empty rows array when no more data
if
len
(
rows
)
==
0
:
print
(
f
'No more results (empty rows array)'
)
break
# Also check if we've fetched all available records
if
offset
+
len
(
rows
)
>
=
total_available
:
print
(
f
'Reached end of data (offset
{
offset
+
len
(
rows
)
}
>= total
{
total_available
}
)'
)
break
page
+=
1
offset
+=
page_size
print
(
f
'Successfully processed
{
page
+
1
}
pages with
{
total
}
total objects'
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
snipeit-assets-to-gcs-hourly
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
snipeit-assets-trigger
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
snipeit-assets-to-gcs
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
Snipe-IT logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Snipe-IT
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
Configure a feed in Google SecOps to ingest Snipe-IT logs
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
Snipe-IT logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Snipe-IT
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://snipe-it-logs/snipeit/assets/
Replace:
snipe-it-logs
: Your GCS bucket name.
snipeit/assets
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
