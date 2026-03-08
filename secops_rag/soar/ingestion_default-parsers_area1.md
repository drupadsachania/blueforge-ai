# Collect Area 1 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/area1/  
**Scraped:** 2026-03-05T09:50:00.317601Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Area 1 logs
Supported in:
Google secops
SIEM
This document explains how to ingest Area 1 Email Security (by Cloudflare) logs
to Google Security Operations using AWS S3. The parser processes the logs in JSON
format. It extracts relevant fields from the nested JSON structure, maps them to
the Unified Data Model (UDM), and enriches the data with geographical
information and security details like attachment hashes and disposition.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Area 1 Email Security (by Cloudflare)
Configure AWS IAM and S3 Bucket
Create
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
Enter a name for the bucket (for example,
area1-security-logs
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
Optional: Add a description tag.
Click
Create access key
.
Click
Download CSV file
and store the
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
In
Permissions policies
, click
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
Get Area 1 API Credentials
Sign in to the
Area 1 Security (Cloudflare)
dashboard.
Go to
Settings
>
API Access
.
Generate the
API Key
(Token).
Copy
and
Save
the Token in a secure place.
Configure the required Python packages
Sign in to your log collection host (for example, an
AWS VM
) and run the
following to configure AWS credentials:
pip
install
boto3
requests
aws
configure
Create the Area 1 Log Puller script
Create the following file by entering
sudo vi area1_to_s3.py
, and then
copy the following code:
Adjust the following:
#!/usr/bin/env python3
import
os
import
requests
import
boto3
import
datetime
import
json
# Configuration
AREA1_API_TOKEN
=
os
.
environ
.
get
(
"AREA1_API_TOKEN"
)
# Load securely from env
AWS_PROFILE
=
os
.
environ
.
get
(
"AWS_PROFILE"
,
None
)
# Optional, for named profiles
S3_BUCKET_NAME
=
"area1-security-logs"
LOG_TYPE
=
"events"
# Time range
end_time
=
datetime
.
datetime
.
utcnow
()
start_time
=
end_time
-
datetime
.
timedelta
(
days
=
1
)
def
fetch_area1_logs
():
url
=
f
"https://api.area1security.com/v1/
{
LOG_TYPE
}
"
headers
=
{
"Authorization"
:
f
"Bearer
{
AREA1_API_TOKEN
}
"
,
"Accept"
:
"application/json"
}
params
=
{
"startDate"
:
start_time
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
),
"endDate"
:
end_time
.
strftime
(
"%Y-%m-
%d
T%H:%M:%SZ"
)
}
response
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
response
.
raise_for_status
()
return
response
.
json
()
def
upload_to_s3
(
data
):
filename
=
f
"area1_
{
LOG_TYPE
}
_
{
start_time
.
strftime
(
'%Y%m
%d
'
)
}
.json"
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
s3
=
session
.
client
(
"s3"
)
s3
.
put_object
(
Bucket
=
S3_BUCKET_NAME
,
Key
=
f
"logs/
{
filename
}
"
,
Body
=
json
.
dumps
(
data
)
.
encode
(
"utf-8"
),
ContentType
=
"application/json"
)
print
(
f
"[✓] Uploaded
{
filename
}
to s3://
{
S3_BUCKET_NAME
}
/logs/"
)
if
__name__
==
"__main__"
:
logs
=
fetch_area1_logs
()
upload_to_s3
(
logs
)
Save and exit
vi
: click
esc
and then type
:wq
.
Store the environment variables
Create a secure file to store environment variables in
/etc/area1.env
(or
/home/user/.area1.env
)
export
AREA1_API_TOKEN
=
"your_actual_area1_api_token"
export
AWS_PROFILE
=
"<your_aws_programmatic_username>"
Make sure the file is secure:
chmod
600
/etc/area1.env
Run and test the script
Run the following script:
python3
area1_to_s3.py
You should see:
Uploaded
area1_events_20250701.json
to
s3://area1-security-logs/logs/
Automate with Cron
Create Wrapper Script for Cron by running
sudo vi /usr/local/bin/run_area1.sh
and then copy the following code:
#!/usr/bin/env bash
set
-euo
pipefail
source
/etc/area1.env
/usr/bin/python3
/opt/scripts/area1_to_s3.py
Make the file executable:
chmod
+x
/usr/local/bin/run_area1.sh
Set to run daily at 01:00 UTC:
crontab
-e
0
1
*
*
*
/usr/local/bin/run_area1.sh
>>
/var/log/area1_to_s3.log
2>&1
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
Content Hub
>
Content Packs
Set up feeds from SIEM Settings
>
Feeds
To configure a feed, follow these steps:
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
In the
Feed name
field, enter a name for the feed (for example,
Area1 Logs
).
Select
Amazon S3
as the
Source type
.
Select
Area1 Security
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
s3://<your-log-bucket-name>
).
Replace the following:
your-log-bucket-name
: the name of the bucket.
URI is a
: Select
Directory which includes subdirectories
.
Source deletion options
: select deletion option according to your preference.
Access Key ID
: the User access key with access to the s3 bucket.
Secret Access Key
: the User secret key with access to the s3 bucket.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Set up feeds from the Content Hub
Specify values for the following fields:
Region
: The region where the Amazon S3 bucket is located.
S3 URI
: The bucket URI (the format should be:
s3://<your-log-bucket-name>
).
Replace the following:
your-log-bucket-name
: the name of the bucket.
URI is a
: Select
Directory which includes subdirectories
.
Source deletion options
: select deletion option according to your preference.
Access Key ID
: the User access key with access to the s3 bucket.
Secret Access Key
: the User secret key with access to the s3 bucket.§
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Source Type
: Method used to collect logs into Google SecOps.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
UDM mapping table
Log Field
UDM Mapping
Logic
alert_id
security_result.rule_id
The value is taken from the
alert_id
field.
alert_reasons
security_result.description
The value is taken from the
alert_reasons
field.
attachments.att_size
security_result.about.file.size
The value is taken from the
attachments.att_size
field and converted to an unsigned integer.
attachments.disposition
security_result.about.user.attribute.labels.value
The value is taken from the
attachments.disposition
field.
attachments.extension
security_result.about.file.mime_type
The value is taken from the
attachments.extension
field.
attachments.md5
security_result.about.file.md5
The value is taken from the
attachments.md5
field.
attachments.name
security_result.about.file.full_path
The value is taken from the
attachments.name
field.
attachments.sha1
security_result.about.file.sha1
The value is taken from the
attachments.sha1
field.
attachments.sha256
security_result.about.file.sha256
The value is taken from the
attachments.sha256
field.
attachments.ssdeep
security_result.about.file.ssdeep
The value is taken from the
attachments.ssdeep
field.
delivery_mode
security_result.detection_fields.value
The value is taken from the
delivery_mode
field.
envelope_from
principal.user.email_addresses, network.email.from
The value is taken from the
envelope_from
field.
envelope_to
network.email.to, target.user.email_addresses
The value is taken from the
envelope_to
field.
final_disposition
security_result.category_details
The value is taken from the
final_disposition
field.
message_id
metadata.product_log_id
The value is taken from the
message_id
field after removing '<' and '>' characters.
replyto
network.email.bounce_address
The value is taken from the
replyto
field.
smtp_helo_server_ip
principal.ip
The value is taken from the
smtp_helo_server_ip
field.
smtp_helo_server_ip_as_name
principal.location.name
The value is taken from the
smtp_helo_server_ip_as_name
field.
smtp_helo_server_ip_as_number
principal.asset_id
The value is taken from the
smtp_helo_server_ip_as_number
field and prepended with
asset_id:
.
smtp_helo_server_ip_geo
principal.location.country_or_region, principal.location.state, principal.location.city
The value is extracted from the
smtp_helo_server_ip_geo
field using a Grok pattern.
smtp_helo_server_name
principal.administrative_domain
The value is taken from the
smtp_helo_server_name
field.
source
metadata.vendor_name
The value is taken from the
source
field. If the field is empty, the value is set to
area1security
.
subject
network.email.subject
The value is taken from the
subject
field.
time
metadata.event_timestamp
The value is taken from the
time
field and converted to a timestamp.
metadata.event_type
The value is set to
EMAIL_TRANSACTION
.
metadata.product_name
The value is set to
AREA1
.
metadata.log_type
The value is set to
AREA1
.
security_result.about.user.attribute.labels.key
The value is set to
disposition
.
security_result.category
The value is set to
SOFTWARE_MALICIOUS
.
security_result.detection_fields.key
The value is set to
delivery_mode
.
Need more help?
Get answers from Community members and Google SecOps professionals.
