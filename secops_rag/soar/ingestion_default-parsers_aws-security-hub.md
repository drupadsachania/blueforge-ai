# Collect AWS Security Hub logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-security-hub/  
**Scraped:** 2026-03-05T09:50:45.084494Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Security Hub logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Security Hub logs to Google Security Operations. AWS Security Hub provides a comprehensive view of security alerts and findings across AWS accounts. By sending these findings to Google SecOps, you can use Google SecOps capabilities to enhance monitoring and threat detection.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure AWS IAM and S3
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save the bucket
Name
and
Region
for later use.
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
Create a Lambda function
Sign in to the
AWS Management Console
.
Go to
Lambda
.
Click
Create Function
and select
Author from Scratch
.
Provide a name for your function; for example,
SecurityHubToS3
.
Choose
Python 3.x
for the runtime.
Enter the Lambda code that takes the findings from EventBridge and writes them to your S3 bucket:
import
json
import
boto3
from
datetime
import
datetime
# Initialize the S3 client
s3_client
=
boto3
.
client
(
's3'
)
# S3 bucket where findings will be stored
bucket_name
=
'aws-security-hub-findings-stream'
def
lambda_handler
(
event
,
context
):
# Extract Security Hub findings from the event
findings
=
event
[
'detail'
][
'findings'
]
# Generate a timestamp for the file name to avoid overwriting
timestamp
=
datetime
.
now
()
.
strftime
(
'%Y-%m-
%d
T%H-%M-%S'
)
# Generate the S3 object key (file name) based on the timestamp
object_key
=
f
"security_hub_findings_
{
timestamp
}
.json"
# Convert findings to JSON format
findings_json
=
json
.
dumps
(
findings
)
# Upload the findings to S3
try
:
response
=
s3_client
.
put_object
(
Bucket
=
bucket_name
,
Key
=
object_key
,
Body
=
findings_json
,
ContentType
=
'application/json'
)
print
(
f
"Successfully uploaded findings to S3:
{
response
}
"
)
except
Exception
as
e
:
print
(
f
"Error uploading findings to S3:
{
e
}
"
)
raise
e
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
(
'Successfully processed findings'
)
}
Set permissions for Lambda by adding an IAM role to the Lambda function with the following policy:
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
"s3:PutObject"
],
"Resource"
:
"arn:aws:s3:::aws-security-hub-findings-stream/*"
}
]
}
How to configure AWS Security Hub to forward findings with EventBridge
Sign in to the
AWS Management Console
.
In the search bar, type and select
Security Hub
from the services list.
Click
Settings
.
Under the
Integrations
section, find
EventBridge
and click
Enable
.
In the search bar, type and select
EventBridge
from the services list.
In the EventBridge console, click
Rules
>
Create rule
.
Provide the following Rule configuration:
Rule Name
: Provide a descriptive name for the rule; for example,
SendSecurityHubFindingsToS3
.
Event Source
: Select
AWS services
.
Service Name
: Choose
Security Hub
.
Event Type
: Select
Security Hub Findings
.
Set the Target
: Choose
Lambda function
.
Select the Lambda function you just created (
SecurityHubToS3
).
Click
Create
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
How to set up the AWS Security Hub feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Security Hub
log type.
Specify the values in the following fields.
Source Type
: Amazon SQS V2
Queue Name
: The SQS queue name to read from
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
SQS Queue Access Key ID
: An account access key that is a 20-character alphanumeric string.
SQS Queue Secret Access Key
: An account access key that is a 40-character alphanumeric string.
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
account
principal.group.product_object_id
The AWS account ID associated with the finding.
configurationItem.ARN
target.resource.id
The Amazon Resource Name (ARN) of the configuration item.
configurationItem.awsAccountId
principal.user.userid
The AWS account ID of the configuration item.
configurationItem.awsRegion
target.asset.location.country_or_region
The AWS region of the configuration item.
configurationItem.configuration.complianceType
security_result.summary
The compliance type of the configuration item.
configurationItem.configuration.configRuleList[].complianceType
security_result.summary
Compliance status for each config rule.
configurationItem.configuration.configRuleList[].configRuleArn
security_result.rule_id
The ARN of the AWS Config rule.
configurationItem.configuration.configRuleList[].configRuleId
security_result.about.labels.configRuleId
The ID of the AWS Config rule.
configurationItem.configuration.configRuleList[].configRuleName
security_result.rule_name
The name of the AWS Config rule.
configurationItem.configuration.privateIpAddress
target.ip
The private IP address of the configuration item.
configurationItem.configuration.publicIpAddress
target.ip
The public IP address of the configuration item.
configurationItem.configurationItemCaptureTime
target.asset.attribute.creation_time
The capture time of the configuration item, converted to a timestamp.
configurationItem.configurationItemStatus
target.asset.attribute.labels.Configuration Item Status
The status of the configuration item.
configurationItem.relationships[].resourceId
target.asset.attribute.cloud.vpc.id
The resource ID of the related resource, used for VPC ID if it matches
vpc
.
configurationItem.resourceId
target.resource.id
The resource ID of the configuration item.
configurationItem.resourceName
target.resource.name
The name of the resource.
configurationItem.resourceType
target.resource.resource_subtype
The resource type of the configuration item.
configurationItem.tags.Contact
principal.user.user_display_name
OR
principal.user.email_addresses
Contact details extracted from tags, parsed for email and username.
configurationItem.tags.OS
/
configurationItem.tags.Os
target.asset.platform_software.platform
The operating system from tags, mapped to platform if it's
Windows
or
Linux
.
configurationItemDiff.changeType
metadata.event_type
The type of change, mapped to RESOURCE_WRITTEN or RESOURCE_CREATION.
detail.accountId
principal.group.product_object_id
The AWS account ID associated with the finding.
detail.actionDescription
detail.actionName
detail.description
sec_result.description
The description of the finding.
detail.findings[].AwsAccountId
principal.group.product_object_id
The AWS account ID associated with the finding.
detail.findings[].CompanyName
detail.findings[].CreatedAt
detail.findings[].Description
sec_result.description
The description of the finding.
detail.findings[].FindingProviderFields.Severity.Label
sec_result.severity
The severity label of the finding, converted to uppercase.
detail.findings[].FindingProviderFields.Types[]
detail.findings[].FirstObservedAt
detail.findings[].GeneratorId
detail.findings[].Id
detail.findings[].LastObservedAt
detail.findings[].ProductArn
detail.findings[].ProductFields.
See below
Various fields used for additional fields, principal, and target information.
detail.findings[].ProductName
detail.findings[].RecordState
detail.findings[].Region
target.location.name
The AWS region of the finding.
detail.findings[].Resources[].Details.
See below
Details about the resources involved in the finding.
detail.findings[].Resources[].Id
target.resource.product_object_id
The ID of the resource.
detail.findings[].Resources[].Partition
detail.findings[].Resources[].Region
target.location.name
The AWS region of the resource.
detail.findings[].Resources[].Tags
detail.findings[].Resources[].Type
target.resource.resource_type
,
target.resource.resource_subtype
,
metadata.event_type
The type of resource, used for resource type, subtype, and event type mapping.
detail.findings[].Sample
detail.findings[].SchemaVersion
detail.findings[].Severity.Label
detail.findings[].SourceUrl
detail.findings[].Title
sec_result.summary
The title of the finding.
detail.findings[].Types[]
detail.findings[].UpdatedAt
detail.findings[].Workflow.Status
detail.findings[].WorkflowState
detail-type
metadata.product_event_type
The detail type of the event.
id
metadata.product_log_id
The ID of the event.
region
target.location.name
The AWS region of the event.
resources[]
source
time
version
(Parser Logic)
metadata.event_timestamp
The create time from the original log entry, used as event timestamp.
(Parser Logic)
metadata.log_type
Set to
AWS_SECURITY_HUB
.
(Parser Logic)
metadata.product_name
Set to
AWS Security Hub
.
(Parser Logic)
metadata.vendor_name
Set to
AMAZON
.
(Parser Logic)
target.asset.attribute.cloud.environment
Set to
AMAZON_WEB_SERVICES
.
(Parser Logic)
metadata.event_type
Set to
USER_RESOURCE_ACCESS
as a default if not mapped from
Resources[].Type
or
configurationItemDiff.changeType
. Set to
STATUS_UPDATE
if
configurationItems
is present and no other event type is set. Set to
RESOURCE_READ
if
configurationItem
or
configurationItems
is present and the status is
OK
or
ResourceDiscovered
. Set to
RESOURCE_DELETION
if
configurationItem
or
configurationItems
is present and the status is
ResourceDeleted
.
(Parser Logic)
metadata.description
Set to
guardduty
if
detail.findings[].ProductFields.aws/guardduty/service/serviceName
is present.
(Parser Logic)
target.asset.attribute.cloud.vpc.resource_type
Set to
VPC_NETWORK
if
configurationItems.relationships[].resourceId
matches
vpc
.
(Parser Logic)
target.resource.resource_type
Set to
VIRTUAL_MACHINE
if
configurationItem
or
configurationItems
is present. Set to
UNSPECIFIED
if no other resource type is set.
(Parser Logic)
target.asset.platform_software.platform
Set to
WINDOWS
or
LINUX
based on the presence of
Windows
or
(Linux|LINUX)
in the message for
configurationItem
. For
configurationItems
, it's set based on
configItem.tags.OS
or
configItem.tags.Os
.
(Parser Logic)
disambiguation_key
Added when multiple events are generated from a single log entry.
Need more help?
Get answers from Community members and Google SecOps professionals.
