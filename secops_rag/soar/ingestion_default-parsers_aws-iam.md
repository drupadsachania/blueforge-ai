# Collect AWS IAM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-iam/  
**Scraped:** 2026-03-05T09:50:36.007758Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS IAM logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS IAM logs to Google Security Operations. The parser transforms raw JSON formatted logs into a structured Unified Data Model (UDM). It extracts relevant fields like user details, role information, permissions, and timestamps, mapping them to corresponding UDM fields for consistent security analysis.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to AWS console
Permissions to create IAM users, roles, and policies
Choose your integration method
Google SecOps supports two methods for ingesting AWS IAM data:
Method A: CloudTrail + Amazon S3
(Activity logs)
What it collects
: IAM activity logs (who performed which actions)
Data source
: AWS CloudTrail events
Latency
: Several minutes (polling-based)
Use case
: Historical audit trail, compliance reporting
Feed source type
: Amazon S3 V2
Method B: Third party API
(Configuration snapshot)
What it collects
: IAM configuration data (users, groups, roles, policies)
Data source
: AWS IAM API direct calls
Latency
: Near real-time (periodic polling)
Use case
: Real-time IAM configuration monitoring, access review
Feed source type
: Third party API
Method A: CloudTrail + Amazon S3 integration
This method uses AWS CloudTrail to capture IAM activity and stores logs in Amazon S3, which Google SecOps then ingests.
Create an Amazon S3 bucket
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save bucket
Name
and
Region
for future reference (for example,
iam-activity-logs-bucket
).
Configure S3 bucket policy for CloudTrail
CloudTrail needs permissions to write logs to your S3 bucket.
In the
Amazon S3 console
, select your bucket.
Go to
Permissions
>
Bucket policy
.
Click
Edit
and add the following policy:
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
"CloudTrailAclCheck"
,
"Effect"
:
"Allow"
,
"Principal"
:
{
"Service"
:
"cloudtrail.amazonaws.com"
},
"Action"
:
"s3:GetBucketAcl"
,
"Resource"
:
"arn:aws:s3:::iam-activity-logs-bucket"
},
{
"Sid"
:
"CloudTrailWrite"
,
"Effect"
:
"Allow"
,
"Principal"
:
{
"Service"
:
"cloudtrail.amazonaws.com"
},
"Action"
:
"s3:PutObject"
,
"Resource"
:
"arn:aws:s3:::iam-activity-logs-bucket/AWSLogs/*"
,
"Condition"
:
{
"StringEquals"
:
{
"s3:x-amz-acl"
:
"bucket-owner-full-control"
}
}
}
]
}
Replace
iam-activity-logs-bucket
with your actual bucket name.
Click
Save changes
.
Configure CloudTrail to capture IAM activity
Sign in to the
AWS Management Console
.
In the search bar, type and select
CloudTrail
from the services list.
Click
Create trail
.
Provide the following configuration details:
Trail name
: Enter a descriptive name (for example,
IAMActivityTrail
).
Apply trail to all regions
: Select
Yes
to capture activities across all regions.
Storage location
: Select
Use existing S3 bucket
and choose the bucket created earlier.
Log file prefix
(optional): Enter a prefix (for example,
iam-logs/
).
Log file SSE-KMS encryption
: Optional. If enabled, create or select a KMS key.
Click
Next
.
Configure event selection:
Management events
: Select
Read
and
Write
to capture both read and write events on IAM resources.
Data events
: Optional. Enable
S3
and
Lambda
data events if needed.
Insights events
: Optional. Enable for unusual activity detection.
Click
Next
.
Review the configuration and click
Create trail
.
Optional: Enable S3 bucket versioning (recommended)
In the
Amazon S3 console
, select your bucket.
Go to
Properties
>
Bucket Versioning
.
Click
Edit
.
Select
Enable
.
Click
Save changes
.
Create IAM user for Google SecOps S3 access
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
Select the
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
Click
Create policy
in a new tab.
In the
Policy editor
, select
JSON
tab.
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
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:GetObject"
,
"s3:ListBucket"
],
"Resource"
:
[
"arn:aws:s3:::iam-activity-logs-bucket"
,
"arn:aws:s3:::iam-activity-logs-bucket/*"
]
}
]
}
Replace
iam-activity-logs-bucket
with your actual bucket name.
Click
Next
.
Name the policy
chronicle-s3-read-policy
.
Click
Create policy
.
Return to the user creation tab and refresh the policies list.
Search for and select
chronicle-s3-read-policy
.
Click
Next
.
Click
Add permissions
.
Optional: Create the Lambda function for real-time export
If you need near real-time export of CloudTrail logs to S3:
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
ExportIAMLogsToS3
Runtime
Python 3.13
Architecture
x86_64
Execution role
Create a new role with basic Lambda permissions
Click
Create function
.
After the function is created, open the
Code
tab, delete the stub and enter the following code:
import
boto3
import
gzip
from
io
import
BytesIO
s3
=
boto3
.
client
(
's3'
)
logs
=
boto3
.
client
(
'logs'
)
def
lambda_handler
(
event
,
context
):
log_group
=
event
[
'logGroup'
]
log_stream
=
event
[
'logStream'
]
log_events
=
logs
.
get_log_events
(
logGroupName
=
log_group
,
logStreamName
=
log_stream
,
startFromHead
=
True
)
log_data
=
"
\n
"
.
join
([
event
[
'message'
]
for
event
in
log_events
[
'events'
]])
# Compress and upload to S3
compressed_data
=
gzip
.
compress
(
log_data
.
encode
(
'utf-8'
))
s3
.
put_object
(
Bucket
=
'iam-activity-logs-bucket'
,
Key
=
f
'iam-logs/
{
log_stream
}
.gz'
,
Body
=
compressed_data
)
return
{
'statusCode'
:
200
,
'body'
:
'Logs exported successfully'
}
Replace
iam-activity-logs-bucket
with your bucket name.
Click
Deploy
to save the function code.
Optional: Configure Lambda execution role permissions
In the same function, select the
Configuration
tab.
Select
Permissions
from the left menu.
Click the
Execution role
name to open it in IAM console.
Click
Add permissions
>
Attach policies
.
Click
Create policy
in a new tab.
Select
JSON
tab and paste the following policy:
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
"logs:GetLogEvents"
,
"logs:FilterLogEvents"
,
"logs:DescribeLogGroups"
,
"logs:DescribeLogStreams"
],
"Resource"
:
"*"
},
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:PutObject"
],
"Resource"
:
"arn:aws:s3:::iam-activity-logs-bucket/*"
}
]
}
Replace
iam-activity-logs-bucket
with your bucket name.
Click
Next
.
Name the policy
lambda-iam-logs-export-policy
.
Click
Create policy
.
Return to the role tab and refresh.
Search for and select
lambda-iam-logs-export-policy
.
Click
Add permissions
.
Optional: Configure Lambda timeout
In the Lambda function, stay on the
Configuration
tab.
Select
General configuration
from the left menu.
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
Optional: Configure Lambda trigger for CloudWatch Logs
In the Lambda function, select the
Function overview
section at the top.
Click
Add trigger
.
In the
Trigger configuration
drop-down, select
CloudWatch Logs
.
Provide the following configuration details:
Log group
: Select or enter the CloudWatch Logs log group associated with CloudTrail (for example,
/aws/cloudtrail/
).
Filter name
: Enter a descriptive name (for example,
IAM-events-filter
).
Filter pattern
: Leave empty to capture all events, or enter a specific pattern.
Click
Add
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the AWS IAM feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS IAM
log type.
Specify the values in the following fields.
Source Type
: Third party API
Username
: Username to authenticate with
Secret
: Secret to authenticate with
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Using SIEM Settings
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
AWS IAM CloudTrail Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
AWS IAM
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://iam-activity-logs-bucket/
Replace
iam-activity-logs-bucket
with your actual bucket name.
Source deletion option
: Select deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
On success
: Deletes all files and empty directories after successful transfer (for cost optimization).
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
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Method B: Third party API integration
This method uses direct AWS IAM API calls to collect current IAM configuration data (users, groups, roles, policies).
Get Google SecOps IP ranges
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Note the IP ranges displayed at the top of the page.
Alternatively, retrieve IP ranges programmatically using the
Feed Management API
.
Create IAM user with required permissions
Option A: Use AWS Managed Policy (Recommended)
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
Select the
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
IAMReadOnlyAccess
(AWS managed policy).
Select the policy.
Click
Next
.
Click
Add permissions
.
Important:
The
IAMReadOnlyAccess
policy includes all required permissions:
iam:GetUser
iam:ListUsers
iam:GetGroup
iam:ListGroups
iam:GetPolicy
iam:ListPolicies
iam:GetRole
iam:ListRoles
iam:ListAttachedUserPolicies
iam:ListAttachedGroupPolicies
iam:ListAttachedRolePolicies
iam:GetAccountSummary
Option B: Create Custom Policy (Least Privilege)
If your security policy requires minimal permissions instead of the managed policy:
In the AWS console, go to
IAM
>
Policies
>
Create policy
>
JSON tab
.
Paste the following policy:
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
"iam:GetUser"
,
"iam:ListUsers"
,
"iam:GetGroup"
,
"iam:ListGroups"
,
"iam:GetPolicy"
,
"iam:ListPolicies"
,
"iam:GetRole"
,
"iam:ListRoles"
,
"iam:ListAttachedUserPolicies"
,
"iam:ListAttachedGroupPolicies"
,
"iam:ListAttachedRolePolicies"
,
"iam:GetAccountSummary"
],
"Resource"
:
"*"
}
]
}
Click
Next
.
Name the policy
chronicle-iam-api-read-policy
.
Click
Create policy
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
Select the
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
Search for and select
chronicle-iam-api-read-policy
.
Click
Next
.
Click
Add permissions
.
Configure a feed in Google SecOps to ingest IAM configuration data
Using Content Hub (recommended)
Go to
Content Hub
>
Content Packs
>
Get Started
.
Click the
Amazon Cloud Platform
pack.
Locate the
AWS IAM
log type.
Select
Third party API
from the
Source Type
drop-down.
Provide the following configuration details:
Username
: The Access Key ID from the IAM user created earlier.
Secret
: The Secret Access Key from the IAM user created earlier.
Feed Name
: A prepopulated value that identifies the feed (for example,
AWS IAM API Configuration
).
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Using SIEM Settings
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
AWS IAM API Configuration
).
Select
Third party API
as the
Source type
.
Select
AWS IAM
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Username
: The Access Key ID from the IAM user created earlier.
Secret
: The Secret Access Key from the IAM user created earlier.
Region
: The AWS region (for example,
us-east-1
).
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM mapping table
Log Field
UDM Mapping
Logic
Arn
entity.entity.resource.name
Directly mapped from the ARN field. Applied to various entity types. For GROUP entity type, mapped from Group.Arn.
AssumeRolePolicyDocument
entity.entity.resource.attribute.permissions.name
Directly mapped from the AssumeRolePolicyDocument field, but only for RESOURCE entity type.
CreateDate
entity.entity.user.attribute.creation_time
Directly mapped from the CreateDate field and converted to Chronicle's timestamp format.
CreateDate
entity.entity.resource.attribute.creation_time
Directly mapped from the CreateDate field and converted to Chronicle's timestamp format.
Group.Arn
entity.entity.resource.name
Directly mapped from the Group.Arn field.
Group.CreateDate
entity.entity.group.attribute.creation_time
Directly mapped from the Group.CreateDate field and converted to Chronicle's timestamp format.
Group.GroupID
entity.entity.group.product_object_id
Directly mapped from the Group.GroupID field.
Group.GroupName
entity.entity.group.group_display_name
Directly mapped from the Group.GroupName field.
Group.GroupName
entity.entity.group.email_addresses
Directly mapped from the Group.GroupName field.
Group.Path
entity.entity.group.attribute.labels.value
Directly mapped from the Group.Path field, the key is hardcoded to path.
IsTruncated
entity.entity.group.attribute.labels.value
Directly mapped from the IsTruncated field converted to string, the key is hardcoded to is_truncated.
Marker
entity.entity.group.attribute.labels.value
Directly mapped from the Marker field, the key is hardcoded to marker.
PasswordLastUsed
entity.entity.user.last_login_time
Directly mapped from the PasswordLastUsed field and converted to Chronicle's timestamp format.
Path
entity.entity.user.attribute.labels.value
Directly mapped from the Path field for USER entity type, key is hardcoded to path.
Path
entity.entity.resource.attribute.labels.value
Directly mapped from the Path field for RESOURCE entity type, the key is hardcoded to path.
PermissionsBoundary.PermissionsBoundaryArn
entity.entity.resource.attribute.labels.value
Directly mapped from PermissionsBoundary.PermissionsBoundaryArn field, the key is hardcoded to permissions_boundary_arn.
PermissionsBoundary.PermissionsBoundaryType
entity.entity.resource.attribute.labels.value
Directly mapped from PermissionsBoundary.PermissionsBoundaryType field, the key is hardcoded to permissions_boundary_type.
RoleID
entity.entity.resource.product_object_id
Directly mapped from the RoleID field.
RoleLastUsed.LastUsedDate
entity.entity.resource.attribute.labels.value
Directly mapped from RoleLastUsed.LastUsedDate field, the key is hardcoded to role_last_used_date.
RoleLastUsed.Region
entity.entity.location.name
Directly mapped from the RoleLastUsed.Region field.
RoleName
entity.entity.resource.attribute.roles.name
Directly mapped from the RoleName field.
Tags.Key
entity.entity.user.attribute.labels.key
Used as the key for the labels in the user entity.
Tags.Value
entity.entity.user.attribute.labels.value
Used as the value for the labels in the user entity.
UserID
entity.entity.user.product_object_id
Directly mapped from the UserID field.
UserName
entity.entity.user.userid
Directly mapped from the UserName field.
Users.Arn
relations.entity.resource.name
Directly mapped from Users.Arn field within the user relation.
Users.CreateDate
relations.entity.user.attribute.creation_time
Directly mapped from Users.CreateDate field within the user relation and converted to Chronicle's timestamp format.
Users.PasswordLastUsed
relations.entity.user.last_login_time
Directly mapped from Users.PasswordLastUsed field within the user relation and converted to Chronicle's timestamp format.
Users.Path
relations.entity.user.attribute.labels.value
Directly mapped from Users.Path field within the user relation, the key is hardcoded to path.
Users.PermissionsBoundary.PermissionsBoundaryArn
relations.entity.resource.attribute.labels.value
Directly mapped from Users.PermissionsBoundary.PermissionsBoundaryArn field within the user relation, the key is hardcoded to permissions_boundary_arn.
Users.PermissionsBoundary.PermissionsBoundaryType
relations.entity.resource.attribute.labels.value
Directly mapped from Users.PermissionsBoundary.PermissionsBoundaryType field within the user relation, the key is hardcoded to permissions_boundary_type.
Users.UserID
relations.entity.user.product_object_id
Directly mapped from Users.UserID field within the user relation.
Users.UserName
relations.entity.user.userid
Directly mapped from Users.UserName field within the user relation.
N/A
entity.metadata.collected_timestamp
Populated with the event ingestion timestamp.
N/A
entity.metadata.vendor_name
Hardcoded to AWS.
N/A
entity.metadata.product_name
Hardcoded to AWS IAM.
N/A
entity.metadata.entity_type
Determined based on the presence of specific fields: USER if UserID exists, RESOURCE if RoleID exists, GROUP if Group.GroupName exists.
N/A
entity.entity.resource.resource_subtype
Set to User for USER and Role for RESOURCE entity types.
N/A
entity.entity.resource.resource_type
Set to ACCESS_POLICY for RESOURCE entity type.
N/A
entity.entity.resource.attribute.cloud.environment
Hardcoded to AMAZON_WEB_SERVICES.
N/A
relations.entity_type
Hardcoded to USER for user relations.
N/A
relations.relationship
Hardcoded to MEMBER for user group relations.
N/A
relations.direction
Hardcoded to UNIDIRECTIONAL.
N/A
relations.entity.resource.resource_subtype
Hardcoded to User for user relations.
Need more help?
Get answers from Community members and Google SecOps professionals.
