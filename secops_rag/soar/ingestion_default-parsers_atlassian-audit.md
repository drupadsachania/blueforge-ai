# Collect Atlassian Cloud Admin Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit/  
**Scraped:** 2026-03-05T09:50:11.662906Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Atlassian Cloud Admin Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Atlassian Cloud Admin Audit logs to
Google Security Operations using AWS S3. The parser first attempts to process the
incoming message as a JSON object. If that fails, it uses regular expressions
(Grok patterns) to extract fields from various Atlassian Jira log formats,
ultimately mapping the extracted data to the unified data model (UDM).
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Privileged access to Atlassian
Configure AWS IAM and S3 Bucket
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
Sign in to the
AWS Console
.
Go to
S3
>
Create bucket
.
Provide a name for the bucket (for example,
atlassian-admin-audit-logs
).
Leave other defaults (or configure encryption and versioning if required).
Click
Create
.
Save the bucket
Name
and
Region
for future reference.
Create a
User
following this user guide:
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
as
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
Download CSV file
and store the
Access ID
and
Secret Access Key
for future reference.
Click
Done
.
In the
Permissions
tab under
Permissions policies
,
click
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
Configure API Key in Atlassian
Sign in to
Atlassian
.
Go to
Settings
>
API keys
.
Click
Create API key
in the top right.
Provide a unique and descriptive
name
for the Key.
Pick a new expiration date under
Expires on
.
Click
Create
to save.
Copy and save your
API Key
and
Organization ID
.
Click
Done
.
Configure the required packages
Sign in to your log collection host (for example, an
AWS VM
) and run the following to configure AWS credentials:
pip
install
boto3
requests
aws
configure
Create Atlassian Log Puller script
Create the following file by entering
sudo vi area1_to_s3.py
and copy the following code:
Adjust the following:
#!/usr/bin/env python3
import
os
,
requests
,
boto3
,
datetime
# Settings
TOKEN
=
os
.
environ
[
"ATL_TOKEN"
]
ORG_ID
=
os
.
environ
[
"ATL_ORG_ID"
]
AWS_PROFILE
=
os
.
getenv
(
"AWS_PROFILE"
)
BUCKET
=
"atlassian-admin-audit-logs"
def
fetch_events
(
cursor
=
None
):
url
=
f
"https://api.atlassian.com/admin/v1/orgs/
{
ORG_ID
}
/events"
headers
=
{
"Authorization"
:
f
"Bearer
{
TOKEN
}
"
}
params
=
{
"limit"
:
100
,
"cursor"
:
cursor
}
if
cursor
else
{
"limit"
:
100
}
resp
=
requests
.
get
(
url
,
headers
=
headers
,
params
=
params
)
resp
.
raise_for_status
()
return
resp
.
json
()
def
upload_json
(
data
,
filename
):
session
=
boto3
.
Session
(
profile_name
=
AWS_PROFILE
)
if
AWS_PROFILE
else
boto3
.
Session
()
session
.
client
(
"s3"
)
.
put_object
(
Bucket
=
BUCKET
,
Key
=
filename
,
Body
=
data
,
ContentType
=
"application/json"
)
print
(
f
"Uploaded
{
filename
}
"
)
def
main
():
today
=
datetime
.
datetime
.
utcnow
()
.
strftime
(
"%Y-%m-
%d
"
)
cursor
=
None
count
=
0
while
True
:
resp
=
fetch_events
(
cursor
)
key
=
f
"audits/
{
today
}
/events_
{
count
}
.json"
upload_json
(
resp
[
"data"
],
key
)
count
+=
1
cursor
=
resp
.
get
(
"links"
,{})
.
get
(
"next"
)
if
not
cursor
:
break
if
__name__
==
"__main__"
:
main
()
Save and exit
vi
by clicking
esc
>
type
:wq
**.
Store environment variables
Create a secure file to store environment variables in
/etc/atlassian_audit.env
:
export
ATL_TOKEN
=
"your_atlassian_key"
export
ATL_ORG_ID
=
"your_org_id"
export
AWS_PROFILE
=
"atlassian-logs"
Make sure the file is secure:
chmod
600
/etc/atlassian_audit.env
Automate with Cron
Create a Wrapper script for Cron by running
sudo vi /usr/local/bin/run_atlassian_audit.sh
and then copy the following code:
#!/usr/bin/env bash
source
/etc/atlassian_audit.env
python3
/opt/scripts/export_atlassian_audit.py
Make the file executable:
chmod
+x
/usr/local/bin/run_atlassian_audit.sh
Configure to run daily at 02:00 UTC:
crontab
-e
0
2
*
*
*
/usr/local/bin/run_atlassian_audit.sh
>>
/var/log/atl_audit.log
2>&1
Need more help?
Get answers from Community members and Google SecOps professionals.
