# Collect Digital Shadows Indicators logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-ioc/  
**Scraped:** 2026-03-05T09:23:24.644873Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Digital Shadows Indicators logs
Supported in:
Google secops
SIEM
This document explains how to ingest Digital Shadows Indicators logs into Google Security Operations using Amazon S3.
Digital Shadows Indicators (now part of ReliaQuest GreyMatter DRP) is a digital risk protection platform that continuously monitors and detects external threats, data exposures, and brand impersonation across the open web, deep web, dark web, and social media. It provides threat intelligence, incident alerts, and indicators of compromise (IOCs) to help organizations identify and mitigate digital risks.
Before you begin
A Google SecOps instance
Privileged access to
Digital Shadows Indicators
portal
Privileged access to
AWS
(S3, IAM)
Active subscription to Digital Shadows Indicators with API access enabled
Collect Digital Shadows Indicators API credentials
Sign in to the
Digital Shadows Indicators Portal
at
https://portal-digitalshadows.com
.
Go to
Settings
>
API Credentials
.
If you don't have an existing API key, click
Create New API Client
or
Generate API Key
.
Copy and save the following details in a secure location:
API Key
: Your 6-character API key
API Secret
: Your 32-character API secret
Account ID
: Your account ID (displayed in the portal or provided by your Digital Shadows representative)
API Base URL
:
https://api.searchlight.app/v1
or
https://portal-digitalshadows.com/api/v1
(depending on your tenant region)
Configure AWS S3 bucket and IAM for Google SecOps
Create an
Amazon S3 bucket
by following this user guide:
Creating a bucket
.
Save bucket
Name
and
Region
for future reference (for example,
digital-shadows-logs
).
Create a
User
by following this user guide:
Creating an IAM user
.
Select the created
User
.
Select the
Security credentials
tab.
Click
Create Access Key
in the
Access Keys
section.
Select
Third-party service
as the
Use case
.
Click
Next
.
Optional: Add a description tag.
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
Select the
Permissions
tab.
Click
Add permissions
in the
Permissions policies
section.
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
JSON
tab.
Copy and paste the policy below.
Policy JSON
(replace
digital-shadows-logs
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
"arn:aws:s3:::digital-shadows-logs/*"
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
"arn:aws:s3:::digital-shadows-logs/digital-shadows/state.json"
}
]
}
Click
Next
>
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
Attach the newly created policy.
Name the role
DigitalShadowsLambdaRole
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
DigitalShadowsCollector
Runtime
Python 3.13
Architecture
x86_64
Execution role
DigitalShadowsLambdaRole
After the function is created, open the
Code
tab, delete the stub, and paste the code below (
DigitalShadowsCollector.py
).
import
urllib3
import
json
import
boto3
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
boto3
.
client
(
's3'
)
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
response
=
storage_client
.
get_object
(
Bucket
=
bucket
,
Key
=
key
)
state_data
=
response
[
'Body'
]
.
read
()
.
decode
(
'utf-8'
)
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
storage_client
.
exceptions
.
NoSuchKey
:
logger
.
info
(
"No previous state found, starting from default lookback"
)
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
storage_client
.
put_object
(
Bucket
=
bucket
,
Key
=
key
,
Body
=
json
.
dumps
({
"last_timestamp"
:
ts
}),
ContentType
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
def
lambda_handler
(
event
,
context
):
bucket_name
=
os
.
environ
[
"S3_BUCKET"
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
"S3_PREFIX"
,
"digital-shadows"
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
"digital-shadows/state.json"
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
last_ts
=
_load_state
(
bucket_name
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
"Chronicle-DigitalShadows-S3/1.0"
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
storage_client
.
put_object
(
Bucket
=
bucket_name
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
"application/x-ndjson"
)
_save_state
(
bucket_name
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
records to s3://
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
return
{
'statusCode'
:
200
,
'body'
:
json
.
dumps
({
'message'
:
msg
,
'records'
:
len
(
records
)
if
records
else
0
})}
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
Go to
Configuration
>
Environment variables
>
Edit
>
Add new environment variable
.
Enter the environment variables provided below, replacing with your values.
Environment variables
Key
Example value
S3_BUCKET
digital-shadows-logs
S3_PREFIX
digital-shadows/
STATE_KEY
digital-shadows/state.json
DS_API_KEY
ABC123
(your 6-character API key)
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
After the function is created, stay on its page (or open
Lambda
>
Functions
>
DigitalShadowsCollector
).
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
, and click
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
Recurring schedule
:
Rate
(
1 hour
)
Target
: Your Lambda function
DigitalShadowsCollector
Name
:
DigitalShadowsCollector-1h
Click
Create schedule
.
Configure a feed in Google SecOps to ingest Digital Shadows Indicators logs
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
Enter a unique name for the
Feed name
.
Select
Amazon S3 V2
as the
Source type
.
Select
Digital Shadows Indicators
as the
Log type
.
Click
Next
and then click
Submit
.
Specify values for the following fields:
S3 URI
:
s3://digital-shadows-logs/digital-shadows/
Source deletion option
: Select the deletion option according to your preference
Maximum File Age
: Include files modified in the last number of days (default is 180 days)
Access Key ID
: User access key with access to the S3 bucket
Secret Access Key
: User secret key with access to the S3 bucket
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
Click
Next
and then click
Submit
.
UDM mapping table
Log Field
UDM Mapping
Logic
value
entity.entity.file.md5
Set if type == "MD5"
value
entity.entity.file.sha1
Set if type == "SHA1"
value
entity.entity.file.sha256
Set if type == "SHA256"
value
entity.entity.hostname
Set if type == "HOST"
value
entity.entity.ip
Value copied directly if type == "IP"
value
entity.entity.url
Set if type == "URL"
value
entity.entity.user.email_addresses
Value copied directly if type == "EMAIL"
type
entity.metadata.entity_type
Set to "DOMAIN_NAME" if type == "HOST", "IP_ADDRESS" if type == "IP", "URL" if type == "URL", "USER" if type == "EMAIL", "FILE" if type in ["SHA1","SHA256","MD5"], else "UNKNOWN_ENTITYTYPE"
lastUpdated
entity.metadata.interval.start_time
Converted from ISO8601 to timestamp if not empty
id
entity.metadata.product_entity_id
Value copied directly if not empty
attributionTag.id, attributionTag.name, attributionTag.type
entity.metadata.threat.about.labels
Merged with objects {key: tag field name, value: tag value} if not empty
sourceType
entity.metadata.threat.category_details
Value copied directly
entity.metadata.threat.threat_feed_name
Set to "Indicators"
id
entity.metadata.threat.threat_id
Value copied directly if not empty
sourceIdentifier
entity.metadata.threat.url_back_to_product
Value copied directly
entity.metadata.product_name
Set to "Indicators"
entity.metadata.vendor_name
Set to "Digital Shadows"
Need more help?
Get answers from Community members and Google SecOps professionals.
