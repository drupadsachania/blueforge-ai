# Collect AlphaSOC alert logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asoc-alert/  
**Scraped:** 2026-03-05T09:18:46.310475Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AlphaSOC alert logs
Supported in:
Google secops
SIEM
This document explains how to ingest
AlphaSOC Alert
logs to
Google Security Operations using
Amazon S3
. The parser extracts security alert
data from ASOC alerts in JSON format, transforming it into the Unified Data Model
(UDM). It parses fields related to observer, principal, target, and metadata,
enriching the data with security results derived from threat information,
severity levels, and associated categories, before finally structuring the
output into the UDM format.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
Privileged access to the
AlphaSOC
platform.
Privileged access to
AWS
(S3, Identity and Access Management (IAM)).
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
alphasoc-alerts-logs
).
Create an
IAM user
with minimal required permissions for S3 access
following this user guide:
Creating an IAM user
.
Select the created
User
.
Select the
Security credentials
tab.
In the
Access Keys
section, click
Create Access Key
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
Download .CSV file
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
>
Create policy
>
JSON
.
Provide the following minimal policy for S3 access (replace
<BUCKET_NAME>
and
<OBJECT_PREFIX>
with your values):
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
"ListBucketPrefix"
,
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
"arn:aws:s3:::<BUCKET_NAME>"
,
"Condition"
:
{
"StringLike"
:
{
"s3:prefix"
:
[
"<OBJECT_PREFIX>/*"
]
}
}
},
{
"Sid"
:
"GetObjects"
,
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
"arn:aws:s3:::<BUCKET_NAME>/<OBJECT_PREFIX>/*"
}
]
}
Optional: If you plan to use the
Delete transferred files
option in the
feed, add this additional statement to the policy:
{
"Sid"
:
"DeleteObjectsIfEnabled"
,
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:DeleteObject"
],
"Resource"
:
"arn:aws:s3:::<BUCKET_NAME>/<OBJECT_PREFIX>/*"
}
Click
Next
>
Create policy
.
Return to the IAM user and click
Add permissions
>
Attach policies directly
.
Search for and select the policy you just created.
Click
Next
>
Add permissions
.
Configure IAM role for AlphaSOC to export findings into your S3 bucket
In the
AWS Console
, go to
IAM
>
Roles
>
Create role
.
Select
Custom trust policy
and paste the following policy:
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
"Principal"
:
{
"AWS"
:
"arn:aws:iam::610660487454:role/data-export"
},
"Action"
:
"sts:AssumeRole"
}
]
}
Click
Next
.
Click
Create policy
to add an
inline policy
that allows writes to
your chosen prefix (replace
<BUCKET_ARN>
and
<OBJECT_PREFIX>
such as
alphasoc/alerts
):
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
"InlinePolicy"
,
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:PutObject"
,
"s3:PutObjectAcl"
],
"Resource"
:
"<BUCKET_ARN>/<OBJECT_PREFIX>/*"
}
]
}
If your bucket uses
KMS encryption
, add this statement to the same policy
(replace
<AWS_REGION>
,
<AWS_ACCOUNT_ID>
, and
<AWS_KEY_ID>
with your values):
{
"Sid"
:
"KMSkey"
,
"Effect"
:
"Allow"
,
"Action"
:
"kms:GenerateDataKey"
,
"Resource"
:
"arn:aws:kms:<AWS_REGION>:<AWS_ACCOUNT_ID>:key/<AWS_KEY_ID>"
}
Name the role (for example,
AlphaSOC-S3-Export
), click
Create role
, and copy its
Role ARN
for the next step.
Provide S3 export configuration details to AlphaSOC
Contact
AlphaSOC support
(
support@alphasoc.com
) or your AlphaSOC
representative and provide the following configuration details to enable S3
export of findings:
S3 bucket name
(for example,
alphasoc-alerts-logs
)
S3 bucket AWS region
(for example,
us-east-1
)
S3 object prefix
(destination path for storing findings, for example,
alphasoc/alerts
)
IAM role ARN
created in the previous section
Request to enable
S3 export
for findings or alerts from your workspace
AlphaSOC will configure the S3 export integration on their side and provide
confirmation once the setup is complete.
Configure a feed in Google SecOps to ingest AlphaSOC Alerts
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
AlphaSOC Alerts
).
Select
Amazon S3 V2
as the
Source type
.
Select
AlphaSOC
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://alphasoc-alerts-logs/alphasoc/alerts/
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
(for example,
alphasoc.alerts
)
Optional:
Ingestion labels
: Add an ingestion label (for example,
vendor=alphasoc
,
type=alerts
).
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
