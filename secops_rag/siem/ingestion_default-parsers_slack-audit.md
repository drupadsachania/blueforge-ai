# Collect Slack Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/slack-audit/  
**Scraped:** 2026-03-05T09:28:17.244985Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Slack Audit logs
Supported in:
Google secops
SIEM
This guide explains how to ingest Slack Audit Logs to Google Security Operations using either Google Cloud Run Functions or Amazon S3 with AWS Lambda.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Slack Enterprise Grid
plan with
Organization Owner
or
Admin
access.
Privileged access to either:
Google Cloud
(for Option 1: Cloud Run Functions and Cloud Scheduler), or
AWS
(for Option 2: S3, IAM, Lambda, EventBridge).
Collect Slack Audit Logs prerequisites (App ID, OAuth Token, Organization ID)
The Slack Audit Logs API requires a User OAuth Token with the
auditlogs:read
scope. This token must be obtained by installing an app at the
Enterprise Grid organization level
, not at the workspace level.
Create Slack app for Audit Logs
Sign in to the
Slack Admin Console
with an
Enterprise Grid Organization Owner
or
Admin
account.
Go to
https://api.slack.com/apps
and click
Create New App
>
From scratch
.
Provide the following configuration details:
App Name
: Enter a descriptive name (for example,
Google SecOps Audit Integration
).
Pick a workspace to develop your app in
: Select your
Development Slack Workspace
(any workspace in the organization).
Click
Create App
.
Configure OAuth scopes
Navigate to
OAuth & Permissions
in the left sidebar.
Scroll down to the
Scopes
section.
Under
User Token Scopes
(NOT Bot Token Scopes), click
Add an OAuth Scope
.
Add the scope:
auditlogs:read
.
Enable public distribution
Navigate to
Manage Distribution
in the left sidebar.
Under
Share Your App with Other Workspaces
, ensure all four sections have green checkmarks:
Remove Hard Coded Information
Activate Public Distribution
Set a Redirect URL
Add an OAuth Scope
Click
Activate Public Distribution
.
Install app to Enterprise Grid organization
Navigate to
OAuth & Permissions
in the left sidebar.
Click
Install to Organization
(NOT "Install to Workspace").
Review the permissions requested and click
Allow
.
After authorization completes, you will be redirected back to the OAuth & Permissions page.
Retrieve credentials
Under
OAuth Tokens for Your Workspace
, locate the
User OAuth Token
.
Copy and securely save the token that starts with
xoxp-
(for example,
xoxp-1234567890-0987654321-1234567890-abc123def456
).
Note your
Organization ID
:
Go to the
Slack Admin Console
.
Navigate to
Settings & Permissions
>
Organization settings
.
Copy the
Organization ID
.
Option 1: Configure Slack Audit Logs export using Google Cloud Run Functions
This option uses Google Cloud Run Functions and Cloud Scheduler to collect Slack Audit Logs and ingest them directly into Google SecOps.
Setting up the directory
Create a new directory on your local machine for the Cloud Run function deployment.
Download the following files from the
Chronicle ingestion-scripts GitHub repository
:
From the
slack
folder, download:
.env.yml
main.py
requirements.txt
From the
root
of the repository, download the entire
common
directory with all its files:
common/__init__.py
common/auth.py
common/env_constants.py
common/ingest.py
common/status.py
common/utils.py
Place all downloaded files into your deployment directory.
Your directory structure should look like this:
deployment_directory
/
├─
common
/
│
├─
__init__
.
py
│
├─
auth
.
py
│
├─
env_constants
.
py
│
├─
ingest
.
py
│
├─
status
.
py
│
└─
utils
.
py
├─
.
env
.
yml
├─
main
.
py
└─
requirements
.
txt
Create secrets in Google Secret Manager
In the
Google Cloud console
, go to
Security
>
Secret Manager
.
Click
Create Secret
.
Provide the following configuration details for the
Chronicle service account
:
Name
: Enter
chronicle-service-account
.
Secret value
: Paste the contents of your Google SecOps ingestion authentication JSON file.
Click
Create secret
.
Copy the
secret resource name
in the format:
projects/<PROJECT_ID>/secrets/chronicle-service-account/versions/latest
.
Click
Create Secret
again to create a second secret.
Provide the following configuration details for the
Slack token
:
Name
: Enter
slack-admin-token
.
Secret value
: Paste your Slack User OAuth Token (starting with
xoxp-
).
Click
Create secret
.
Copy the
secret resource name
in the format:
projects/<PROJECT_ID>/secrets/slack-admin-token/versions/latest
.
Setting the required runtime environment variables
Open the
.env.yml
file in your deployment directory.
Configure the environment variables with your values:
CHRONICLE_CUSTOMER_ID
:
"<your-chronicle-customer-id>"
CHRONICLE_REGION
:
us
CHRONICLE_SERVICE_ACCOUNT
:
"projects/<PROJECT_ID>/secrets/chronicle-service-account/versions/latest"
CHRONICLE_NAMESPACE
:
""
POLL_INTERVAL
:
"5"
SLACK_ADMIN_TOKEN
:
"projects/<PROJECT_ID>/secrets/slack-admin-token/versions/latest"
Replace the following:
<your-chronicle-customer-id>
: Your Google SecOps customer ID.
<PROJECT_ID>
: Your Google Cloud project ID.
CHRONICLE_REGION
: Set to your Google SecOps region. Valid values:
us
,
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
,
southamerica-east1
.
POLL_INTERVAL
: Frequency interval (in minutes) at which the function executes. This duration must be the same as the Cloud Scheduler job interval.
Save the
.env.yml
file.
Deploying the Cloud Run function
Open a terminal or
Cloud Shell
in the Google Cloud console.
Navigate to your deployment directory:
cd
/path/to/deployment_directory
Execute the following command to deploy the Cloud Run function:
gcloud
functions
deploy
slack-audit-to-chronicle
\
--entry-point
main
\
--trigger-http
\
--runtime
python39
\
--env-vars-file
.env.yml
\
--timeout
300s
\
--memory
512MB
\
--service-account
<SERVICE_ACCOUNT_EMAIL>
Replace
<SERVICE_ACCOUNT_EMAIL>
with the email address of the service account you want your Cloud Run function to use.
Wait for the deployment to complete.
Once deployed, note the
function URL
from the output.
Set up Cloud Scheduler
In the
Google Cloud console
, go to
Cloud Scheduler
>
Create job
.
Provide the following configuration details:
Name
: Enter
slack-audit-scheduler
.
Region
: Select the same region where you deployed the Cloud Run function.
Frequency
: Enter
*/5 * * * *
(runs every 5 minutes, matching the
POLL_INTERVAL
value).
Timezone
: Select
UTC
.
Target type
: Select
HTTP
.
URL
: Enter the Cloud Run function URL from the deployment output.
HTTP method
: Select
POST
.
Auth header
: Select
Add OIDC token
.
Service account
: Select the same service account used for the Cloud Run function.
Click
Create
.
Option 2: Configure Slack Audit Logs export using AWS S3
This option uses AWS Lambda to collect Slack Audit Logs and store them in S3, then configures a Google SecOps feed to ingest the logs.
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save bucket
Name
and
Region
for future reference (for example,
slack-audit-logs
).
Create a
User
following this user guide:
Creating an IAM user
.
Select the created
User
.
Select
Security credentials
tab.
Click
Create Access Key
in section
Access Keys
.
Select
Third-party service
as
Use case
.
Click
Next
.
Optional: Add description tag.
Click
Create access key
.
Click
Download .csv file
to save the
Access Key
and
Secret Access Key
for future reference.
Click
Done
.
Select
Permissions
tab.
Click
Add permissions
in section
Permissions policies
.
Select
Add permissions
.
Select
Attach policies directly
.
Search for
AmazonS3FullAccess
policy.
Select the policy.
Click
Next
.
Click
Add permissions
.
Configure the IAM policy and role for S3 uploads
In the AWS console, go to
IAM
>
Policies
>
Create policy
>
JSON tab
.
Copy and paste the policy below.
Policy JSON
(replace
slack-audit-logs
if you entered a different bucket name):
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Sid"
:
"AllowPutObjects"
,
"Effect"
:
"Allow"
,
"Action"
:
"s3:PutObject"
,
"Resource"
:
"arn:aws:s3:::slack-audit-logs/*"
},
{
"Sid"
:
"AllowGetStateObject"
,
"Effect"
:
"Allow"
,
"Action"
:
"s3:GetObject"
,
"Resource"
:
"arn:aws:s3:::slack-audit-logs/slack/audit/state.json"
}
]
}
Click
Next
.
Enter the policy name
SlackAuditS3Policy
.
Click
Create policy
.
Go to
IAM
>
Roles
>
Create role
>
AWS service
>
Lambda
.
Attach the newly created policy
SlackAuditS3Policy
.
Name the role
SlackAuditToS3Role
and click
Create role
.
Create the Lambda function
In the
AWS Console
, go to
Lambda
>
Functions
>
Create function
.
Click
Author from scratch
.
Provide the following configuration details:
Setting
Value
Name
slack_audit_to_s3
Runtime
Python 3.13
Architecture
x86_64
Execution role
SlackAuditToS3Role
Click
Create function
.
After the function is created, open the
Code
tab, delete the stub and paste the code below (
slack_audit_to_s3.py
).
#!/usr/bin/env python3
# Lambda: Pull Slack Audit Logs (Enterprise Grid) to S3 (JSONL format)
import
os
,
json
,
time
,
urllib.parse
from
urllib.request
import
Request
,
urlopen
from
urllib.error
import
HTTPError
,
URLError
import
boto3
BASE_URL
=
"https://api.slack.com/audit/v1/logs"
TOKEN
=
os
.
environ
[
"SLACK_AUDIT_TOKEN"
]
# org-level user token with auditlogs:read
BUCKET
=
os
.
environ
[
"S3_BUCKET"
]
PREFIX
=
os
.
environ
.
get
(
"S3_PREFIX"
,
"slack/audit/"
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
"slack/audit/state.json"
)
LIMIT
=
int
(
os
.
environ
.
get
(
"LIMIT"
,
"200"
))
# Slack recommends <= 200
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
"MAX_PAGES"
,
"20"
))
LOOKBACK_SEC
=
int
(
os
.
environ
.
get
(
"LOOKBACK_SECONDS"
,
"3600"
))
# First-run window
HTTP_TIMEOUT
=
int
(
os
.
environ
.
get
(
"HTTP_TIMEOUT"
,
"60"
))
HTTP_RETRIES
=
int
(
os
.
environ
.
get
(
"HTTP_RETRIES"
,
"3"
))
RETRY_AFTER_DEFAULT
=
int
(
os
.
environ
.
get
(
"RETRY_AFTER_DEFAULT"
,
"2"
))
# Optional server-side filters (comma-separated 'action' values), empty means no filter
ACTIONS
=
os
.
environ
.
get
(
"ACTIONS"
,
""
)
.
strip
()
s3
=
boto3
.
client
(
"s3"
)
def
_get_state
()
-
>
dict
:
try
:
obj
=
s3
.
get_object
(
Bucket
=
BUCKET
,
Key
=
STATE_KEY
)
st
=
json
.
loads
(
obj
[
"Body"
]
.
read
()
or
b
"
{}
"
)
return
{
"cursor"
:
st
.
get
(
"cursor"
)}
except
Exception
:
return
{
"cursor"
:
None
}
def
_put_state
(
state
:
dict
)
-
>
None
:
body
=
json
.
dumps
(
state
,
separators
=
(
","
,
":"
))
.
encode
(
"utf-8"
)
s3
.
put_object
(
Bucket
=
BUCKET
,
Key
=
STATE_KEY
,
Body
=
body
,
ContentType
=
"application/json"
)
def
_http_get
(
params
:
dict
)
-
>
dict
:
qs
=
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
url
=
f
"
{
BASE_URL
}
?
{
qs
}
"
if
qs
else
BASE_URL
req
=
Request
(
url
,
method
=
"GET"
)
req
.
add_header
(
"Authorization"
,
f
"Bearer
{
TOKEN
}
"
)
req
.
add_header
(
"Accept"
,
"application/json"
)
attempt
=
0
while
True
:
try
:
with
urlopen
(
req
,
timeout
=
HTTP_TIMEOUT
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
"utf-8"
))
except
HTTPError
as
e
:
# Respect Retry-After on 429/5xx
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
)
and
attempt
<
HTTP_RETRIES
:
retry_after
=
0
try
:
retry_after
=
int
(
e
.
headers
.
get
(
"Retry-After"
,
RETRY_AFTER_DEFAULT
))
except
Exception
:
retry_after
=
RETRY_AFTER_DEFAULT
time
.
sleep
(
max
(
1
,
retry_after
))
attempt
+=
1
continue
# Re-raise other HTTP errors
raise
except
URLError
:
if
attempt
<
HTTP_RETRIES
:
time
.
sleep
(
RETRY_AFTER_DEFAULT
)
attempt
+=
1
continue
raise
def
_write_page
(
data
:
dict
,
page_idx
:
int
)
-
>
str
:
"""
Extract entries from Slack API response and write as JSONL (one event per line).
Chronicle requires newline-delimited JSON, not a JSON array.
"""
entries
=
data
.
get
(
"entries"
)
or
[]
if
not
entries
:
# No entries to write, skip file creation
return
None
# Convert each entry to a single-line JSON string
lines
=
[
json
.
dumps
(
entry
,
separators
=
(
","
,
":"
))
for
entry
in
entries
]
# Join with newlines to create JSONL format
body
=
"
\n
"
.
join
(
lines
)
.
encode
(
"utf-8"
)
# Write to S3
ts
=
time
.
strftime
(
"%Y/%m/
%d
/%H%M%S"
,
time
.
gmtime
())
key
=
f
"
{
PREFIX
}{
ts
}
-slack-audit-p
{
page_idx
:
05d
}
.json"
s3
.
put_object
(
Bucket
=
BUCKET
,
Key
=
key
,
Body
=
body
,
ContentType
=
"application/json"
)
return
key
def
lambda_handler
(
event
=
None
,
context
=
None
):
state
=
_get_state
()
cursor
=
state
.
get
(
"cursor"
)
params
=
{
"limit"
:
LIMIT
}
if
ACTIONS
:
params
[
"action"
]
=
[
a
.
strip
()
for
a
in
ACTIONS
.
split
(
","
)
if
a
.
strip
()]
if
cursor
:
params
[
"cursor"
]
=
cursor
else
:
# First run (or reset): fetch a recent window by time
params
[
"oldest"
]
=
int
(
time
.
time
())
-
LOOKBACK_SEC
pages
=
0
total
=
0
last_cursor
=
None
while
pages
<
MAX_PAGES
:
data
=
_http_get
(
params
)
# Write entries in JSONL format
written_key
=
_write_page
(
data
,
pages
)
entries
=
data
.
get
(
"entries"
)
or
[]
total
+=
len
(
entries
)
# Cursor for next page
meta
=
data
.
get
(
"response_metadata"
)
or
{}
next_cursor
=
meta
.
get
(
"next_cursor"
)
or
data
.
get
(
"next_cursor"
)
if
next_cursor
:
params
=
{
"limit"
:
LIMIT
,
"cursor"
:
next_cursor
}
if
ACTIONS
:
params
[
"action"
]
=
[
a
.
strip
()
for
a
in
ACTIONS
.
split
(
","
)
if
a
.
strip
()]
last_cursor
=
next_cursor
pages
+=
1
continue
break
if
last_cursor
:
_put_state
({
"cursor"
:
last_cursor
})
return
{
"ok"
:
True
,
"pages"
:
pages
+
(
1
if
total
or
last_cursor
else
0
),
"entries"
:
total
,
"cursor"
:
last_cursor
}
if
__name__
==
"__main__"
:
print
(
lambda_handler
())
Go to
Configuration
>
Environment variables
>
Edit
>
Add environment variable
.
Enter the environment variables provided below, replacing with your values.
Environment variables
Key
Example value
S3_BUCKET
slack-audit-logs
S3_PREFIX
slack/audit/
STATE_KEY
slack/audit/state.json
SLACK_AUDIT_TOKEN
xoxp-***
(org-level user token with
auditlogs:read
)
LIMIT
200
MAX_PAGES
20
LOOKBACK_SECONDS
3600
HTTP_TIMEOUT
60
HTTP_RETRIES
3
RETRY_AFTER_DEFAULT
2
ACTIONS
(optional, CSV)
user_login,app_installed
Click
Save
.
Select the
Configuration
tab.
In the
General configuration
panel click
Edit
.
Change
Timeout
to
5 minutes (300 seconds)
and click
Save
.
Create an EventBridge schedule
Go to
Amazon EventBridge
>
Scheduler
>
Create schedule
.
Provide the following configuration details:
Name
: Enter
slack-audit-1h
.
Recurring schedule
: Select
Rate-based schedule
.
Rate expression
: Enter
1
hours.
Flexible time window
: Select
Off
.
Click
Next
.
Select
Target
:
Target API
: Select
AWS Lambda Invoke
.
Lambda function
: Select
slack_audit_to_s3
.
Click
Next
.
Click
Next
(skip optional settings).
Review and click
Create schedule
.
(Optional) Create read-only IAM user & keys for Google SecOps
Go to
AWS Console
>
IAM
>
Users
>
Create user
.
Provide the following configuration details:
User name
: Enter
secops-reader
.
Access type
: Select
Programmatic access
.
Click
Next
.
Select
Attach policies directly
.
Click
Create policy
.
In the
JSON
tab, paste:
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:GetObject"
],
"Resource"
:
"arn:aws:s3:::slack-audit-logs/*"
},
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:ListBucket"
],
"Resource"
:
"arn:aws:s3:::slack-audit-logs"
}
]
}
Click
Next
.
Enter the policy name
secops-reader-policy
.
Click
Create policy
.
Return to the user creation page, refresh the policy list, and select
secops-reader-policy
.
Click
Next
.
Click
Create user
.
Select the created user
secops-reader
.
Go to
Security credentials
>
Access keys
>
Create access key
.
Select
Third-party service
.
Click
Next
.
Click
Create access key
.
Click
Download .csv file
to save the credentials.
Configure a feed in Google SecOps to ingest Slack Audit Logs
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed (for example,
Slack Audit Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Slack Audit
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://slack-audit-logs/slack/audit/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket (from
secops-reader
).
Secret Access Key
: User secret key with access to the S3 bucket (from
secops-reader
).
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
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
action
metadata.product_event_type
Directly mapped from the
action
field in the raw log.
actor.type
principal.labels.value
Directly mapped from the
actor.type
field, with the key
actor.type
added.
actor.user.email
principal.user.email_addresses
Directly mapped from the
actor.user.email
field.
actor.user.id
principal.user.product_object_id
Directly mapped from the
actor.user.id
field.
actor.user.id
principal.user.userid
Directly mapped from the
actor.user.id
field.
actor.user.name
principal.user.user_display_name
Directly mapped from the
actor.user.name
field.
actor.user.team
principal.user.group_identifiers
Directly mapped from the
actor.user.team
field.
context.ip_address
principal.ip
Directly mapped from the
context.ip_address
field.
context.location.domain
about.resource.attribute.labels.value
Directly mapped from the
context.location.domain
field, with the key
context.location.domain
added.
context.location.id
about.resource.id
Directly mapped from the
context.location.id
field.
context.location.name
about.resource.name
Directly mapped from the
context.location.name
field.
context.location.name
about.resource.attribute.labels.value
Directly mapped from the
context.location.name
field, with the key
context.location.name
added.
context.location.type
about.resource.resource_subtype
Directly mapped from the
context.location.type
field.
context.session_id
network.session_id
Directly mapped from the
context.session_id
field.
context.ua
network.http.user_agent
Directly mapped from the
context.ua
field.
context.ua
network.http.parsed_user_agent
Parsed user agent information derived from the
context.ua
field using the
parseduseragent
filter.
country
principal.location.country_or_region
Directly mapped from the
country
field.
date_create
metadata.event_timestamp.seconds
The epoch timestamp from the
date_create
field is converted to a timestamp object.
details.inviter.email
target.user.email_addresses
Directly mapped from the
details.inviter.email
field.
details.inviter.id
target.user.product_object_id
Directly mapped from the
details.inviter.id
field.
details.inviter.name
target.user.user_display_name
Directly mapped from the
details.inviter.name
field.
details.inviter.team
target.user.group_identifiers
Directly mapped from the
details.inviter.team
field.
details.reason
security_result.description
Directly mapped from the
details.reason
field, or if it's an array, concatenated with commas.
details.type
about.resource.attribute.labels.value
Directly mapped from the
details.type
field, with the key
details.type
added.
details.type
security_result.summary
Directly mapped from the
details.type
field.
entity.app.id
target.resource.id
Directly mapped from the
entity.app.id
field.
entity.app.name
target.resource.name
Directly mapped from the
entity.app.name
field.
entity.channel.id
target.resource.id
Directly mapped from the
entity.channel.id
field.
entity.channel.name
target.resource.name
Directly mapped from the
entity.channel.name
field.
entity.channel.privacy
target.resource.attribute.labels.value
Directly mapped from the
entity.channel.privacy
field, with the key
entity.channel.privacy
added.
entity.file.filetype
target.resource.attribute.labels.value
Directly mapped from the
entity.file.filetype
field, with the key
entity.file.filetype
added.
entity.file.id
target.resource.id
Directly mapped from the
entity.file.id
field.
entity.file.name
target.resource.name
Directly mapped from the
entity.file.name
field.
entity.file.title
target.resource.attribute.labels.value
Directly mapped from the
entity.file.title
field, with the key
entity.file.title
added.
entity.huddle.date_end
about.resource.attribute.labels.value
Directly mapped from the
entity.huddle.date_end
field, with the key
entity.huddle.date_end
added.
entity.huddle.date_start
about.resource.attribute.labels.value
Directly mapped from the
entity.huddle.date_start
field, with the key
entity.huddle.date_start
added.
entity.huddle.id
about.resource.attribute.labels.value
Directly mapped from the
entity.huddle.id
field, with the key
entity.huddle.id
added.
entity.huddle.participants.0
about.resource.attribute.labels.value
Directly mapped from the
entity.huddle.participants.0
field, with the key
entity.huddle.participants.0
added.
entity.huddle.participants.1
about.resource.attribute.labels.value
Directly mapped from the
entity.huddle.participants.1
field, with the key
entity.huddle.participants.1
added.
entity.type
target.resource.resource_subtype
Directly mapped from the
entity.type
field.
entity.user.email
target.user.email_addresses
Directly mapped from the
entity.user.email
field.
entity.user.id
target.user.product_object_id
Directly mapped from the
entity.user.id
field.
entity.user.name
target.user.user_display_name
Directly mapped from the
entity.user.name
field.
entity.user.team
target.user.group_identifiers
Directly mapped from the
entity.user.team
field.
entity.workflow.id
target.resource.id
Directly mapped from the
entity.workflow.id
field.
entity.workflow.name
target.resource.name
Directly mapped from the
entity.workflow.name
field.
id
metadata.product_log_id
Directly mapped from the
id
field.
ip
principal.ip
Directly mapped from the
ip
field. Determined by logic based on the
action
field. Defaults to
USER_COMMUNICATION
, but changes to other values like
USER_CREATION
,
USER_LOGIN
,
USER_LOGOUT
,
USER_RESOURCE_ACCESS
,
USER_RESOURCE_UPDATE_PERMISSIONS
, or
USER_CHANGE_PERMISSIONS
based on the value of
action
. Hardcoded to "SLACK_AUDIT".  Set to "Enterprise Grid" if
date_create
exists, otherwise set to "Audit Logs" if
user_id
exists. Hardcoded to "Slack". Hardcoded to "REMOTE". Set to "SSO" if
action
contains "user_login" or "user_logout". Otherwise, set to "MACHINE". Not mapped in the provided examples. Defaults to "ALLOW", but set to "BLOCK" if
action
is "user_login_failed". Set to "Slack" if
date_create
exists, otherwise set to "SLACK" if
user_id
exists.
user_agent
network.http.user_agent
Directly mapped from the
user_agent
field.
user_id
principal.user.product_object_id
Directly mapped from the
user_id
field.
username
principal.user.product_object_id
Directly mapped from the
username
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
