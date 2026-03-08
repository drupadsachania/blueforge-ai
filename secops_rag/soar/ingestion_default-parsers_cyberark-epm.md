# Collect CyberArk EPM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-epm/  
**Scraped:** 2026-03-05T09:53:55.214916Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CyberArk EPM logs
Supported in:
Google secops
SIEM
This document explains how to ingest CyberArk EPM logs to Google Security Operations using AWS S3. The parser transforms CyberArk EPM log data into a unified data model (UDM). It iterates through each event in the log, maps relevant fields to their corresponding UDM fields, handles specific data structures like
exposedUsers
, and enriches the output with static vendor and product information.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have privileged access to AWS.
Ensure that you have privileged access to the EPM Server Management Console.
Configure AWS IAM for Google SecOps ingestion
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
Download CSV file
for save the
Access Key
and
Secret Access Key
for later use.
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
section .
Select
Add permissions
.
Select
Attach policies directly
.
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
Configure CyberArk EPM for API access
Sign in to the
CyberArk EPM
web console as an Administrator.
Go to
Administration
>
Account Management
.
Click
+ Add User
.
Provide the following details:
Username
: epm_api_user
Password
: strong secret
Email/Full Name
: optional
Under
Permissions
, grant
ViewOnlySetAdmin
on every
Set
of logs pulled.
Click
Save
.
Optional: Extend Session Timeout:
Go to
Administration
>
Account Configuration
.
Set
Timeout for inactive session
to 60 minutes.
Click
Save
.
Go to
Policy & Sets
>
select your Set
>
Properties
.
Copy and save the
Set ID (a GUID)
. You'll use it in the script as
EPM_SET_ID
.
Create an AWS S3 Bucket
Sign in to the
AWS Management Console
.
Go to
AWS Console
>
Services
>
S3
>
Create bucket
.
Provide the following configuration details:
Bucket name
: my-cyberark-epm-logs
Region
: your choice
>
Create
Create an IAM Role for EC2
Sign in to the
AWS Management Console
.
Go to
Services
.
In the search bar, type
IAM
and select it.
In the
IAM
dashboard, click
Roles
.
Click
Create role
.
Provide the following configuration details:
Trusted entity
:
AWS service
>
EC2
>
Next
.
Attach permission
:
AmazonS3FullAccess
(or a scoped policy to your bucket)
>
Next
.
Role name
: EC2-S3-EPM-Writer
>
Create role
.
Optional: Launch & configure your EC2 Collector VM
Sign in to the
AWS Managmenet Console
.
Go to
Services
.
In the search bar, type EC2 and select it.
In the EC2 dashboard, click
Instances
.
Click
Launch instances
.
Provide the following configuration details:
Name
: Enter
EPM-Log-Collector
.
AMI
: Select
Ubuntu Server 22.04 LTS
.
Instance type
: Choose
t3.micro
(or larger), and then click
Next
Network
: Ensure the Network setting is set to your default VPC.
IAM role
: Select the
EC2-S3-EPM-Writer`
IAM role from the menu.
Auto-assign Public IP
: Set this to
Enable
. If you will be 
connecting through a VPN, you can leave this disabled.
Add Storage
: Leave the default storage configuration (8 GiB), and then click
Next
.
Select
Create a new security group
.
Inbound rule: Click
Add Rule
.
Type: Select SSH.
Port: 22.
Source: your IP
Click
Review and Launch
.
Select or create a key pair.
Click
Download Key Pair
.
Save the downloaded PEM file. You will need this file to connect to your instance via SSH.
Connect to your Virtual Machine (VM) using SSH:
chmod
400
~/Downloads/your-key.pem
ssh
-i
~/Downloads/your-key.pem
ubuntu@<EC2_PUBLIC_IP>
Install Collector prerequisites
Update the Operating System:
# Update OS
sudo
apt
update
&&
sudo
apt
upgrade
-y
# Install Python, Git
sudo
apt
install
-y
python3
python3-venv
python3-pip
git
# Create & activate virtualenv
python3
-m
venv
~/epm-venv
source
~/epm-venv/bin/activate
# Install libraries
pip
install
requests
boto3
Create directory & state file:
sudo
mkdir
-p
/var/lib/epm-collector
sudo
touch
/var/lib/epm-collector/last_run.txt
sudo
chown
ubuntu:ubuntu
/var/lib/epm-collector/last_run.txt
Initialize it (for example to 1 hour ago):
echo
"
$(
date
-u
-d
'1 hour ago'
+%Y-%m-%dT%H:%M:%SZ
)
"
>
/var/lib/epm-collector/last_run.txt
Deploy the Collector Script
Create project folder:
mkdir
~/epm-collector
&&
cd
~/epm-collector
Set environment variables (for example, in ~/.bashrc):
export
EPM_URL
=
"https://epm.mycompany.com"
export
EPM_USER
=
"epm_api_user"
export
EPM_PASS
=
"YourPasswordHere"
export
EPM_SET_ID
=
"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
export
S3_BUCKET
=
"my-cyberark-epm-logs"
export
S3_PREFIX
=
"epm/"
Create collector.py and paste the following:
#!/usr/bin/env python3
import
os
import
sys
import
json
import
boto3
import
requests
from
datetime
import
datetime
,
timezone
,
timedelta
# ── LOAD CONFIG FROM ENV ───────────────────────────────────────────────────────
def
must_env
(
var
):
v
=
os
.
getenv
(
var
)
if
not
v
:
print
(
f
"ERROR: environment variable
{
var
}
is required"
,
file
=
sys
.
stderr
)
sys
.
exit
(
1
)
return
v
EPM_URL
=
must_env
(
"EPM_URL"
)
# for example, https://epm.mycompany.com
USERNAME
=
must_env
(
"EPM_USER"
)
# API username
PASSWORD
=
must_env
(
"EPM_PASS"
)
# API password
SET_ID
=
must_env
(
"EPM_SET_ID"
)
# GUID of the Set to pull
S3_BUCKET
=
must_env
(
"S3_BUCKET"
)
# for example, my-cyberark-epm-logs
S3_PREFIX
=
os
.
getenv
(
"S3_PREFIX"
,
""
)
# optional, for example "epm/"
STATE_FILE
=
os
.
getenv
(
"STATE_FILE"
,
"/var/lib/epm-collector/last_run.txt"
)
PAGE_SIZE
=
int
(
os
.
getenv
(
"PAGE_SIZE"
,
"100"
))
# ── END CONFIG ────────────────────────────────────────────────────────────────
def
read_last_run
():
try
:
ts
=
open
(
STATE_FILE
)
.
read
()
.
strip
()
return
datetime
.
fromisoformat
(
ts
.
replace
(
"Z"
,
"+00:00"
))
except
:
# default to 1 hour ago
return
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
hours
=
1
)
def
write_last_run
(
dt
):
with
open
(
STATE_FILE
,
"w"
)
as
f
:
f
.
write
(
dt
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
))
def
logon
():
r
=
requests
.
post
(
f
"
{
EPM_URL
}
/REST/EPMService.svc/Logon"
,
json
=
{
"username"
:
USERNAME
,
"password"
:
PASSWORD
},
headers
=
{
"Content-Type"
:
"application/json"
}
)
r
.
raise_for_status
()
return
r
.
json
()
.
get
(
"SessionToken"
)
def
logoff
(
token
):
requests
.
post
(
f
"
{
EPM_URL
}
/REST/EPMService.svc/Logoff"
,
headers
=
{
"Authorization"
:
f
"Bearer
{
token
}
"
}
)
def
fetch_raw_events
(
token
,
start
,
end
):
headers
=
{
"Authorization"
:
f
"Bearer
{
token
}
"
}
page
=
1
while
True
:
params
=
{
"setId"
:
SET_ID
,
"startDate"
:
start
,
"endDate"
:
end
,
"pageSize"
:
PAGE_SIZE
,
"pageNumber"
:
page
}
resp
=
requests
.
get
(
f
"
{
EPM_URL
}
/REST/EPMService.svc/GetRawEvents"
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
events
=
resp
.
json
()
.
get
(
"RawEvents"
,
[])
if
not
events
:
break
yield from
events
page
+=
1
def
upload_to_s3
(
obj
,
key
):
boto3
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
S3_BUCKET
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
(
obj
)
.
encode
(
"utf-8"
)
)
def
main
():
# determine time window
start_dt
=
read_last_run
()
end_dt
=
datetime
.
now
(
timezone
.
utc
)
START
=
start_dt
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
)
END
=
end_dt
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
)
token
=
logon
()
try
:
for
idx
,
raw_evt
in
enumerate
(
fetch_raw_events
(
token
,
START
,
END
),
start
=
1
):
key
=
f
"
{
S3_PREFIX
}{
end_dt
.
strftime
(
'%Y/%m/
%d
'
)
}
/raw_
{
int
(
end_dt
.
timestamp
())
}
_
{
idx
}
.json"
upload_to_s3
(
raw_evt
,
key
)
print
(
f
"Uploaded raw event to
{
key
}
"
)
finally
:
logoff
(
token
)
# persist for next run
write_last_run
(
end_dt
)
if
__name__
==
"__main__"
:
main
()
Make the script executable:
chmod
+x
collector.py
Automate with Cron
Open crontab:
crontab
-e
Add the daily job:
0
0
*
*
*
cd
~/epm-collector
&&
source
~/epm-venv/bin/activate
&&
python
collector.py
>>
~/epm-collector/epm.log
2>&1
Configure a feed in Google SecOps to ingest Cyberark EPM logs
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
Cyberark EPM Logs
).
Select
Amazon S3
as the
Source type
.
Select
Cyberark EPM
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Region
: The region where the Amazon S3 bucket is located.
S3 URI
: The bucket URI (the format should be:
s3://your-log-bucket-name/
).
Replace the following:
your-log-bucket-name
: the name of the bucket.
URI is a
: Select
Directory
or
Directory which includes subdirectories
.
Source deletion options
: select deletion option according to your preference.
Access Key ID
: the User access key with access to the s3 bucket.
Secret Access Key
: the User secret key with access to the s3 bucket.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label to be applied to the events from this feed.
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
agentId
principal.asset.asset_id
Concatenates "agentId:" with the value of the agentId field.
computerName
principal.hostname
Directly maps the computerName field.
displayName
metadata.description
Directly maps the displayName field.
eventType
metadata.product_event_type
Directly maps the eventType field.
exposedUsers.[].accountName
target.user.attribute.labels
Creates a label with key "accountName_[index]" and value from exposedUsers.[index].accountName.
exposedUsers.[].domain
target.user.attribute.labels
Creates a label with key "domain_[index]" and value from exposedUsers.[index].domain.
exposedUsers.[].username
target.user.attribute.labels
Creates a label with key "username_[index]" and value from exposedUsers.[index].username.
filePath
target.file.full_path
Directly maps the filePath field.
hash
target.file.sha1
Directly maps the hash field.
operatingSystemType
principal.platform
Maps "Windows" to "WINDOWS" if the operatingSystemType field is "Windows".
policyName
security_result.rule_name
Directly maps the policyName field.
processCommandLine
target.process.command_line
Directly maps the processCommandLine field.
publisher
additional.fields
Creates a field with key "Publisher" and string_value from the publisher field.
sourceProcessCommandLine
target.process.parent_process.command_line
Directly maps the sourceProcessCommandLine field.
sourceProcessHash
target.process.parent_process.file.sha1
Directly maps the sourceProcessHash field.
sourceProcessSigner
additional.fields
Creates a field with key "sourceProcessSigner" and string_value from the sourceProcessSigner field.
threatProtectionAction
security_result.action_details
Directly maps the threatProtectionAction field.
metadata.event_timestamp
Sets the event timestamp to the log entry's create_time.
metadata.event_type
Hardcoded to "STATUS_UPDATE".
metadata.log_type
Hardcoded to "CYBERARK_EPM".
metadata.product_name
Hardcoded to "EPM".
metadata.vendor_name
Hardcoded to "CYBERARK".
security_result.alert_state
Hardcoded to "ALERTING".
userName
principal.user.userid
Directly maps the userName field.
Need more help?
Get answers from Community members and Google SecOps professionals.
