# Collect Imperva Audit Trail logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-audit-trail/  
**Scraped:** 2026-03-05T09:57:12.006656Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Imperva Audit Trail logs
Supported in:
Google secops
SIEM
This document explains how to ingest Imperva Audit Trail logs to Google Security Operations using Amazon S3. Imperva Audit Trail provides comprehensive logging of all administrative actions performed in your Imperva account, including user logins, configuration changes, policy modifications, and system events. This integration lets you send these audit logs to Google SecOps for compliance monitoring and security analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to AWS
Privileged access to Imperva Console
Collect Imperva Audit Trail prerequisites (API credentials)
Sign in to the
Imperva Console
at
my.imperva.com
.
Go to
Account
>
Account Management
.
On the sidebar, click
SIEM Logs
>
Log Configuration
.
Click
Add connection
.
Select
Amazon S3
as the delivery method.
Configure the connection for Amazon S3:
Connection name
: Enter a descriptive name (for example,
Google SecOps Integration
).
Access key
: Your S3 access key.
Secret key
: Your S3 secret key.
Path
: The bucket path in format
<bucket-name>/<folder>
(for example,
imperva-audit-trail-logs/chronicle
).
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save bucket
Name
and
Region
for future reference (for example,
imperva-audit-trail-logs
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
Optional: Add a description tag.
Click
Create access key
.
Click
Download CSV file
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
.
Click
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
"arn:aws:s3:::imperva-audit-trail-logs/*"
},
{
"Sid"
:
"AllowGetObjects"
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
"arn:aws:s3:::imperva-audit-trail-logs/*"
},
{
"Sid"
:
"AllowListBucket"
,
"Effect"
:
"Allow"
,
"Action"
:
"s3:ListBucket"
,
"Resource"
:
"arn:aws:s3:::imperva-audit-trail-logs"
}
]
}
Replace
imperva-audit-trail-logs
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
AWS service
>
Lambda
.
Attach the newly created policy.
Name the role
imperva-audit-trail-s3-role
and click
Create role
.
Configure Imperva Audit Trail S3 connection
Return to the
Imperva Console
SIEM Logs configuration.
Update the Amazon S3 connection with the AWS credentials:
Access key
: The User access key with access to the S3 bucket.
Secret key
: The User secret key with access to the S3 bucket.
Path
: Enter the path in format
imperva-audit-trail-logs/chronicle
.
Click
Test connection
to verify connectivity.
Ensure the connection status shows
Available
.
Configure Audit Trail log export
In the
Connections table
, expand your Amazon S3 connection.
Click
Add log type
.
Provide the following configuration details:
Configuration name
: Enter a descriptive name (for example,
Audit Trail Logs to Chronicle
).
Select service
: Choose
Audit Trail
.
Select log types
: Select
AUDIT_TRAIL
log type.
Format
: JSON (structured format for audit trail logs).
State
: Set to
Enabled
.
Click
Add log type
to save the configuration.
Optional: Create read-only IAM user & keys for Google SecOps
Go to
AWS Console
>
IAM
>
Users
.
Click
Add users
.
Provide the following configuration details:
User
: Enter
secops-reader
.
Access type
: Select
Access key – Programmatic access
.
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
"arn:aws:s3:::imperva-audit-trail-logs/*"
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
"arn:aws:s3:::imperva-audit-trail-logs"
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
Configure a feed in Google SecOps to ingest Imperva Audit Trail logs
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
Imperva Audit Trail logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Imperva Audit Trail
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://imperva-audit-trail-logs/chronicle/
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
