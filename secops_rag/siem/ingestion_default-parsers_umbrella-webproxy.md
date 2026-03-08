# Collect Cisco Umbrella Web Proxy logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-webproxy/  
**Scraped:** 2026-03-05T09:21:51.304732Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Umbrella Web Proxy logs
Supported in:
Google secops
SIEM
This document explains how to collect Cisco Umbrella Web Proxy logs to a Google Security Operations feed using AWS S3 bucket. The parser extracts fields from a CSV log, renaming columns for clarity and handling potential variations in the input data. It then uses included files (
umbrella_proxy_udm.include
and
umbrella_handle_identities.include
) to map the extracted fields to the UDM and process identity information based on the
identityType
field.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you privileged access to AWS IAM and S3.
Ensure that you have privileged access to Cisco Umbrella.
Configure a Cisco-managed Amazon S3 bucket
Sign in to the
Cisco Umbrella
dashboard.
Go to
Admin
>
Log management
.
Select
Use a Cisco-managed Amazon S3 bucket
option.
Provide the following configuration details:
Select a region
: select a region closer to your location for lower latency.
Select a retention duration
: select the time period. The retention duration is 7, 14, or 30 days. After the selected time period, data is deleted and cannot be recovered. If your ingestion cycle is regular, use a shorter time period. You can change the retention duration at a later time.
Click
Save
.
Click
Continue
to confirm your selections and to receive activation notification.
In the
Activation complete
window that appears, the
Access key
and
Secret key
values are displayed.
Copy the
Access key
and
Secret key
values. If you lose these keys, you must regenerate them.
Click
Got it
>
Continue
.
A summary page displays the configuration and your bucket name. You can turn logging off or on as required by your organization. However, logs are purged based on the retention duration, regardless of new data getting added.
Optional: Configure user access keys for self-managed AWS S3 bucket
Sign in to the
AWS Management Console
.
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
Optional: add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
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
section.
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
Optional: Configure a self-managed Amazon S3 bucket
Sign in to the
AWS Management Console
.
Go to
S3
.
Click
Create bucket
.
Provide the following configuration details:
Bucket name
: provide a name for the Amazon S3 bucket.
Region
: select a region.
Click
Create
.
Optional: Configure a bucket policy for self-managed AWS S3 bucket
Click the newly created bucket to open it.
Select
Properties
>
Permissions
.
In the
Permissions
list, click
Add bucket policy
.
Enter the preconfigured bucket policy as follows:
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
/*"
    },
    {
      "Sid": "",
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
/*"},
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:GetBucketLocation",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
"
    },
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
"
    }
  ]
}
Replace
BUCKET_NAME
with the Amazon S3 bucket name you provided.
Click
Save
.
Optional: Required Verification for self-managed Amazon S3 bucket
In the
Cisco Umbrella
dashboard, select
Admin
>
Log management
>
Amazon S3
.
In the
Bucket name
field, specify your exact Amazon S3 bucket name, and then click
Verify
.
As part of the verification process, a file named
README_FROM_UMBRELLA.txt
is uploaded from Cisco Umbrella to your Amazon S3 bucket. You may need to refresh your browser in order to see the readme file when it is uploaded.
Download the
README_FROM_UMBRELLA.txt
file, and open it using a text editor.
Copy and save the unique
Cisco Umbrella
token from the file.
Go to the
Cisco Umbrella
dashboard.
In the
Token number
field, specify the token and click
Save
.
If successful, you get a confirmation message in your dashboard indicating that the bucket was successfully verified. If you receive an error indicating that your bucket can't be verified, re-check the syntax of the bucket name and review the configuration.
Configure a feed in Google SecOps to ingest the Cisco Umbrella Web Proxy logs
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
field, enter a name for the feed; for example,
Cisco Umbrella Web Proxy Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select
Cisco Umbrella Web Proxy
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: the bucket URI.
s3:/BUCKET_NAME
Replace
BUCKET_NAME
with the actual name of the bucket.
Source deletion options
: select deletion option according to your preference.
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
ampDisposition
security_result.detection_fields[].value
The value of
ampDisposition
from the raw log.
ampMalware
security_result.detection_fields[].value
The value of
ampMalware
from the raw log.
ampScore
security_result.detection_fields[].value
The value of
ampScore
from the raw log.
avDetections
security_result.detection_fields[].value
The value of
avDetections
from the raw log.
blockedCategories
security_result.threat_name
The value of
blockedCategories
from the raw log.
certificateErrors
security_result.detection_fields[].value
The value of
certificateErrors
from the raw log.
contentType
security_result.detection_fields[].value
The value of
contentType
from the raw log.
destinationIp
target.ip
The value of
destinationIp
from the raw log.
destinationListID
security_result.detection_fields[].value
The value of
destinationListID
from the raw log.
dlpstatus
security_result.detection_fields[].value
The value of
dlpstatus
from the raw log.
externalIp
principal.ip
The value of
externalIp
from the raw log.
fileAction
security_result.detection_fields[].value
The value of
fileAction
from the raw log.
fileName
target.file.names
The value of
fileName
from the raw log.
identitiesV8
principal.hostname
The value of
identitiesV8
from the raw log.
identity
principal.location.name
The value of
identity
from the raw log.
internalIp
principal.ip
The value of
internalIp
from the raw log.
isolateAction
security_result.detection_fields[].value
The value of
isolateAction
from the raw log.
referer
network.http.referral_url
The value of
referer
from the raw log.
requestMethod
network.http.method
The value of
requestMethod
from the raw log.
requestSize
security_result.detection_fields[].value
The value of
requestSize
from the raw log.
responseBodySize
security_result.detection_fields[].value
The value of
responseBodySize
from the raw log.
responseSize
security_result.detection_fields[].value
The value of
responseSize
from the raw log.
ruleID
security_result.rule_id
The value of
ruleID
from the raw log.
rulesetID
security_result.detection_fields[].value
The value of
rulesetID
from the raw log.
sha
security_result.about.file.sha256
The value of
sha
from the raw log.
statusCode
network.http.response_code
The value of
statusCode
from the raw log.
ts
timestamp
The value of
ts
from the raw log, parsed into a timestamp.
url
target.url
The value of
url
from the raw log.
userAgent
network.http.user_agent
The value of
userAgent
from the raw log.
verdict
security_result.detection_fields[].value
The value of
verdict
from the raw log.
warnstatus
security_result.detection_fields[].value
The value of
warnstatus
from the raw log. The value of
collection_time
from the raw log.  Hardcoded to
NETWORK_HTTP
. Hardcoded to
Cisco
. Hardcoded to
Umbrella
. Hardcoded to
UMBRELLA_WEBPROXY
. Derived from the scheme of the URL field (
http
or
https
). Parsed from the
userAgent
field using a user-agent parsing library. The value of
requestSize
from the raw log, converted to an integer. The value of
responseSize
from the raw log, converted to an integer. Derived from the
identity
field when
identityType
(or
identityTypeV8
with
identitiesV8
) indicates a user.  Further parsed to extract user details like display name, first name, last name, and email address. Mapped from the
verdict
field:
allowed
or
allowed
->
ALLOW
, other values ->
BLOCK
. If
categories
is not empty, set to
NETWORK_CATEGORIZED_CONTENT
. The value of
categories
from the raw log. Based on the
verdict
and potentially other fields.  Usually
Traffic allowed
or
Traffic blocked
.  If
verdict
is not
allowed
or
blocked
and
statusCode
is present, the summary is
Traffic %{statusCode}
.
Need more help?
Get answers from Community members and Google SecOps professionals.
