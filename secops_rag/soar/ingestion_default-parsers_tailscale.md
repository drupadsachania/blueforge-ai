# Collect Tailscale logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale/  
**Scraped:** 2026-03-05T10:00:57.677698Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tailscale logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tailscale logs to Google Security Operations using Tailscale's native Amazon S3 log streaming feature. Tailscale produces operational data in the form of configuration audit logs and network flow logs. This integration uses Tailscale's built-in S3 streaming capability to automatically send these logs to Google SecOps for analysis and monitoring.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to
Tailscale Admin Console
(Owner, Admin, Network admin, or IT admin role)
Privileged access to
AWS
(S3, IAM)
Collect Tailscale prerequisites (tailnet information)
Sign in to the
Tailscale Admin Console
.
Note your
tailnet name
(for example,
example.com
or your organization name).
Ensure you have the required plan:
Configuration audit log streaming
: Available on Personal, Personal Plus, and Enterprise plans.
Network flow log streaming
: Available on Enterprise plan only.
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
tailscale-logs
).
Create a user following this user guide:
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
Search for and select the
AmazonS3FullAccess
policy.
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
Enter the following policy:
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
"AllowTailscalePutObjects"
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
"arn:aws:s3:::tailscale-logs/*"
}
]
}
Replace
tailscale-logs
if you entered a different bucket name.
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
Custom trust policy
.
Enter the following trust policy:
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
"arn:aws:iam::982722776073:role/tailscale-log-streaming"
},
"Action"
:
"sts:AssumeRole"
,
"Condition"
:
{
"StringEquals"
:
{
"sts:ExternalId"
:
"YOUR_TAILNET_NAME"
}
}
}
]
}
Replace
YOUR_TAILNET_NAME
with your actual tailnet name.
Click
Next
.
Attach the policy created in step 1.
Name the role
TailscaleS3StreamingRole
and click
Create role
.
Copy the
Role ARN
for use in Tailscale configuration.
Configure Tailscale native S3 log streaming
Setup Configuration Audit Log streaming
In the
Tailscale Admin Console
, go to
Logs
>
Configuration logs
.
Click
Start streaming
.
Select
Amazon S3
as the destination.
Provide the following configuration details:
AWS Account ID
: Your AWS Account ID.
S3 Bucket Name
:
tailscale-logs
.
Role ARN
: The ARN of the IAM role you created.
S3 Key Prefix
:
tailscale/configuration/
(optional).
Click
Start streaming
.
Verify the status shows as
Active
.
Setup Network Flow Log streaming (Enterprise plan only)
If not already enabled, go to
Settings
>
Network flow logs
and enable network flow logs for your tailnet.
Go to
Logs
>
Network flow logs
.
Click
Start streaming
.
Select
Amazon S3
as the destination.
Provide the following configuration details:
AWS Account ID
: Your AWS Account ID
S3 Bucket Name
:
tailscale-logs
Role ARN
: The ARN of the IAM role you created
S3 Key Prefix
:
tailscale/network/
(optional)
Click
Start streaming
.
Verify the status shows as
Active
.
Optional: Create read-only IAM user & keys for Google SecOps
In the
AWS Console
. go to
IAM
>
Users
>
Add users
.
Click
Add users
.
Provide the following configuration details:
User
:
secops-reader
Access type
:
Access key — Programmatic access
Click
Create user
.
Attach minimal read policy (custom):
Users
>
secops-reader
>
Permissions
>
Add permissions
>
Attach policies directly
>
Create policy
.
In the JSON editor, enter the following policy:
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
"arn:aws:s3:::tailscale-logs/*"
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
"arn:aws:s3:::tailscale-logs"
}
]
}
Set the name to
secops-reader-policy
.
Go to
Create policy
>
search/select
>
Next
>
Add permissions
.
Go to
Security credentials
>
Access keys
>
Create access key
.
Download the
CSV
(these values are entered into the feed).
Configure a feed in Google SecOps to ingest Tailscale logs
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
Tailscale logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tailscale
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tailscale-logs/tailscale/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label applied to the events from this feed.
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
