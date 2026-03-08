# Collect Akamai SIEM Connector logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector/  
**Scraped:** 2026-03-05T09:18:40.753174Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akamai SIEM Connector logs
Supported in:
Google secops
SIEM
This document explains how to ingest Akamai SIEM Connector logs to Google Security Operations using Amazon S3. Akamai SIEM Integration provides security events from the Akamai platform in JSON format through the SIEM Integration API. This integration uses AWS Lambda to periodically fetch events from the Akamai API and store them in S3, where Google SecOps ingests them.
Before you begin
A Google SecOps instance
Privileged access to
Akamai Control Center
with
Manage SIEM
user role
Akamai API credentials with
SIEM API
service enabled (READ-WRITE access level)
Privileged access to
AWS
(S3, IAM, Lambda, EventBridge)
Enable SIEM Integration in Akamai Control Center
Sign in to
Akamai Control Center
.
Go to
WEB & DATA CENTER SECURITY
>
Security Configuration
.
Open the
Security configuration
(and the appropriate version) for which you want to collect SIEM data.
Click
Advanced settings
and expand
Data collection for SIEM Integrations
.
Click
On
to enable SIEM.
Choose the security policies for which you want to export data:
All security policies
: Send SIEM data for events that violate any or all security policies within the security configuration.
Specific security policies
: Select one or more specific security policies from the dropdown list.
Optional: If you use
Account Protector
and want to include the unencrypted
Username
, turn on the
Include username
checkbox.
Optional: If you want to exclude events belonging to a specific protection type and action, click
Add exception
, select the protection and the associated actions you don't want SIEM to collect.
Click
Save
.
Copy and save the
Security Configuration ID (configId)
from the SIEM Integration section. You'll need this for Lambda configuration.
Create Akamai API credentials for SIEM Integration
Sign in to
Akamai Control Center
.
Go to
ACCOUNT ADMIN
>
Identity & access
>
API clients
.
Click
Create API client
.
Provide the following configuration details:
API client name
: Enter a descriptive name (for example,
Google SecOps Poller
).
API service
: Select
SIEM
and set access level to
READ-WRITE
.
Click
Create API client
.
Copy and save the following credentials securely:
Client Token
Client Secret
Access Token
Host
(for example,
example.luna.akamaiapis.net
)
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
akamai-siem-logs
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
In the
AWS console
, go to
IAM
>
Policies
>
Create policy
>
JSON tab
.
Copy and paste the following policy, and replace
akamai-siem-logs
with your bucket name:
Policy JSON
:
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
"arn:aws:s3:::akamai-siem-logs/*"
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
"arn:aws:s3:::akamai-siem-logs/akamai-siem/state.json"
}
]
}
Click
Next
.
Enter policy name
AkamaiSIEMtoS3Policy
and click
Create policy
.
Go to
IAM
>
Roles
>
Create role
.
Select
AWS service
.
Select
Lambda
as the use case.
Click
Next
.
Search for and select the policy
AkamaiSIEMtoS3Policy
you just created.
Click
Next
.
Enter role name
AkamaiSIEMtoS3Role
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
AkamaiSIEMtoS3Function
Runtime
Python 3.13
Architecture
x86_64
Execution role
Use an existing role
Existing role
AkamaiSIEMtoS3Role
Click
Create function
.
After the function is created, open the
Code
tab, delete the stub and paste the following code:
import
json
import
boto3
import
os
import
urllib3
import
hmac
import
hashlib
import
base64
from
datetime
import
datetime
from
urllib.parse
import
urlparse
,
urljoin
# Configuration from environment variables
S3_BUCKET
=
os
.
environ
[
'S3_BUCKET'
]
S3_PREFIX
=
os
.
environ
.
get
(
'S3_PREFIX'
,
'akamai-siem/'
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
'akamai-siem/state.json'
)
AKAMAI_HOST
=
os
.
environ
[
'AKAMAI_HOST'
]
AKAMAI_CLIENT_TOKEN
=
os
.
environ
[
'AKAMAI_CLIENT_TOKEN'
]
AKAMAI_CLIENT_SECRET
=
os
.
environ
[
'AKAMAI_CLIENT_SECRET'
]
AKAMAI_ACCESS_TOKEN
=
os
.
environ
[
'AKAMAI_ACCESS_TOKEN'
]
AKAMAI_CONFIG_IDS
=
os
.
environ
[
'AKAMAI_CONFIG_IDS'
]
.
split
(
','
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
'LIMIT'
,
'10000'
))
s3_client
=
boto3
.
client
(
's3'
)
http
=
urllib3
.
PoolManager
()
def
load_state
():
"""Load offset state from S3"""
try
:
response
=
s3_client
.
get_object
(
Bucket
=
S3_BUCKET
,
Key
=
STATE_KEY
)
return
json
.
loads
(
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
))
except
s3_client
.
exceptions
.
NoSuchKey
:
return
{}
except
Exception
as
e
:
print
(
f
"Error loading state:
{
e
}
"
)
return
{}
def
save_state
(
state
):
"""Save offset state to S3"""
try
:
s3_client
.
put_object
(
Bucket
=
S3_BUCKET
,
Key
=
STATE_KEY
,
Body
=
json
.
dumps
(
state
,
indent
=
2
)
.
encode
(
'utf-8'
),
ContentType
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
"Error saving state:
{
e
}
"
)
def
make_edgegrid_auth_header
(
url
,
method
=
'GET'
):
"""Create EdgeGrid authentication header"""
timestamp
=
datetime
.
utcnow
()
.
strftime
(
'%Y%m
%d
T%H:%M:%S+0000'
)
nonce
=
base64
.
b64encode
(
os
.
urandom
(
16
))
.
decode
(
'utf-8'
)
parsed_url
=
urlparse
(
url
)
relative_url
=
parsed_url
.
path
if
parsed_url
.
query
:
relative_url
+=
'?'
+
parsed_url
.
query
auth_header
=
f
'EG1-HMAC-SHA256 '
\
f
'client_token=
{
AKAMAI_CLIENT_TOKEN
}
;'
\
f
'access_token=
{
AKAMAI_ACCESS_TOKEN
}
;'
\
f
'timestamp=
{
timestamp
}
;'
\
f
'nonce=
{
nonce
}
;'
data_to_sign
=
'
\t
'
.
join
([
method
,
parsed_url
.
scheme
,
parsed_url
.
netloc
,
relative_url
,
''
,
# Request body for GET
''
,
# No additional headers
])
signing_key
=
hmac
.
new
(
AKAMAI_CLIENT_SECRET
.
encode
(
'utf-8'
),
timestamp
.
encode
(
'utf-8'
),
hashlib
.
sha256
)
.
digest
()
auth_signature
=
base64
.
b64encode
(
hmac
.
new
(
signing_key
,
(
data_to_sign
+
auth_header
)
.
encode
(
'utf-8'
),
hashlib
.
sha256
)
.
digest
()
)
.
decode
(
'utf-8'
)
return
auth_header
+
f
'signature=
{
auth_signature
}
'
def
fetch_akamai_events
(
config_id
,
offset
=
None
):
"""Fetch events from Akamai SIEM API"""
base_url
=
f
'https://
{
AKAMAI_HOST
}
'
endpoint
=
f
'/siem/v1/configs/
{
config_id
}
'
params
=
f
'limit=
{
LIMIT
}
'
if
offset
:
params
+=
f
'&offset=
{
offset
}
'
url
=
f
'
{
base_url
}{
endpoint
}
?
{
params
}
'
try
:
headers
=
{
'Authorization'
:
make_edgegrid_auth_header
(
url
)
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
120
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
"Error response
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
'utf-8'
)
}
"
)
return
[],
offset
# Parse multi-JSON response (newline-delimited JSON)
lines
=
response
.
data
.
decode
(
'utf-8'
)
.
strip
()
.
split
(
'
\n
'
)
events
=
[]
new_offset
=
offset
for
line
in
lines
:
if
not
line
.
strip
():
continue
try
:
obj
=
json
.
loads
(
line
)
# Check if this is offset context (metadata object with offset)
if
'offset'
in
obj
and
(
'total'
in
obj
or
'responseContext'
in
obj
):
new_offset
=
obj
.
get
(
'offset'
)
continue
# This is an event
events
.
append
(
obj
)
except
json
.
JSONDecodeError
as
e
:
print
(
f
"Warning: Failed to parse line:
{
e
}
"
)
continue
return
events
,
new_offset
except
Exception
as
e
:
print
(
f
"Error fetching events for config
{
config_id
}
:
{
e
}
"
)
return
[],
offset
def
lambda_handler
(
event
,
context
):
"""Lambda handler - fetches Akamai events and writes to S3"""
print
(
f
"Starting Akamai SIEM fetch at
{
datetime
.
utcnow
()
.
isoformat
()
}
Z"
)
state
=
load_state
()
total_events
=
0
for
config_id
in
AKAMAI_CONFIG_IDS
:
config_id
=
config_id
.
strip
()
if
not
config_id
:
continue
print
(
f
"Fetching events for config:
{
config_id
}
"
)
current_offset
=
state
.
get
(
config_id
)
events
,
new_offset
=
fetch_akamai_events
(
config_id
,
current_offset
)
if
events
:
print
(
f
"Fetched
{
len
(
events
)
}
events for config
{
config_id
}
"
)
# Write events to S3 as newline-delimited JSON
timestamp
=
datetime
.
utcnow
()
.
strftime
(
'%Y%m
%d
_%H%M%S'
)
s3_key
=
f
'
{
S3_PREFIX
}{
config_id
}
/
{
timestamp
}
.json'
payload
=
'
\n
'
.
join
(
json
.
dumps
(
event
)
for
event
in
events
)
try
:
s3_client
.
put_object
(
Bucket
=
S3_BUCKET
,
Key
=
s3_key
,
Body
=
payload
.
encode
(
'utf-8'
),
ContentType
=
'application/json'
)
print
(
f
"Wrote
{
len
(
events
)
}
events to s3://
{
S3_BUCKET
}
/
{
s3_key
}
"
)
# Update offset only after successful write
if
new_offset
:
state
[
config_id
]
=
new_offset
total_events
+=
len
(
events
)
except
Exception
as
e
:
print
(
f
"Error writing to S3:
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
"No new events for config
{
config_id
}
"
)
# Save updated state
save_state
(
state
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
f
'Successfully processed
{
total_events
}
events'
,
'configs_processed'
:
len
(
AKAMAI_CONFIG_IDS
)
})
}
Click
Deploy
to save the code.
Go to
Configuration
>
Environment variables
.
Click
Edit
.
Click
Add environment variable
for each of the following:
Environment variables
Key
Example value
S3_BUCKET
akamai-siem-logs
S3_PREFIX
akamai-siem/
STATE_KEY
akamai-siem/state.json
AKAMAI_HOST
example.luna.akamaiapis.net
AKAMAI_CLIENT_TOKEN
your-client-token
AKAMAI_CLIENT_SECRET
your-client-secret
AKAMAI_ACCESS_TOKEN
your-access-token
AKAMAI_CONFIG_IDS
12345,67890
LIMIT
10000
Click
Save
.
Go to
Configuration
>
General configuration
.
Click
Edit
.
Change
Timeout
to
5 minutes (300 seconds)
.
Click
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
Schedule name
: Enter
AkamaiSIEMtoS3-5min
.
Schedule pattern
: Select
Recurring schedule
.
Schedule type
: Select
Rate-based schedule
.
Rate expression
: Enter
5
and select
Minutes
.
Click
Next
.
Provide the following configuration details:
Target
: Select
AWS Lambda Invoke
.
Lambda function
: Select
AkamaiSIEMtoS3Function
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
Configure a feed in Google SecOps to ingest Akamai SIEM Connector logs
Go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Akamai SIEM Connector
).
Select
Amazon S3 V2
as the
Source type
.
Select
Akamai SIEM Connector
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://akamai-siem-logs/akamai-siem/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
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
Need more help?
Get answers from Community members and Google SecOps professionals.
