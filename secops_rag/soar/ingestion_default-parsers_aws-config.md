# Collect AWS Config logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config/  
**Scraped:** 2026-03-05T09:50:29.610599Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Config logs
Supported in:
Google secops
SIEM
This document explains how to create a new S3 bucket to store the CloudTrail logs and how to create an IAM user to retrieve the log feeds from AWS.
AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure CloudTrail and AWS S3 bucket
Sign in to the AWS Management Console.
Go to the
Amazon S3 console
.
In the AWS console, search for
Cloudtrail
.
Click
Create trail
.
Provide a
Trail name
.
Select
Create new S3 bucket
(you may also choose to use an existing S3 bucket).
Provide a name for the
AWS KMS
alias, or choose an existing AWS KMS Key.
Click
Next
.
Choose
Event type
and add
Data events
.
Click
Next
.
Review the settings and click
Create trail
.
In the AWS console, search for
S3 Buckets
.
Click the newly created log bucket, and select the
AWSLogs
folder.
Click
Copy S3 URI
and save it.
Configure AWS Config API Calls Logging
In AWS, go to
AWS Config
>
Set up AWS Config
.
Select the bucket type (either select the existing bucket details or create a new one).
Select all required AWS-managed rules and click
Next
to select a bucket.
Refer to
AWS Config
for details on rule types to help you select the appropriate rule based on your requirements:
Compliance rules
: allow to evaluate the configurations of resources to ensure that they meet compliance standards or regulatory requirements.
Configuration rules
: allow to evaluate the configurations of resources to ensure that they meet the required configuration standards.
Performance rules
: allow to evaluate the configurations of resources to ensure that they are optimized for performance.
Security rules
: allow to evaluate the configurations of resources to ensure that they meet security standards or requirements.
Click
Create config
.
Go to
Amazon S3
.
Click the newly created log bucket, and select the folder
AWSLogs
.
Click
Copy S3 URI
and save it.
Configure AWS IAM User
In the AWS console, search for
IAM
.
Click
Users
.
Click
Add Users
.
Provide a name for the user (for example, chronicle-feed-user).
Select
Access key - Programmatic access
as the AWS credential type.
Click
Next: Permissions
.
Select
Attach existing policies directly
.
Select
AmazonS3ReadOnlyAccess
or
AmazonS3FullAccess
.
Click
Next: Tags
.
Optional: Add any tags if required.
Click
Next: Review
.
Review the configuration and click
Create user
.
Copy the Access key ID and Secret access key of the created user.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New
Content Hub
>
Content Packs
>
Get Started
How to set up the AWS Config feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Config
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
UDM Mapping
Log field
UDM mapping
Logic
ARN
target.resource.id
The value is taken from the
ARN
field.
awsAccountId
principal.user.userid
The value is taken from the
awsAccountId
field.
awsRegion
target.asset.location.country_or_region
The value is taken from the
awsRegion
field.
configurationItem.awsAccountId
principal.user.userid
The value is taken from the
configurationItem.awsAccountId
field.
configurationItem.configurationItemCaptureTime
target.asset.attribute.creation_time
The value is taken from the
configurationItem.configurationItemCaptureTime
field and converted to a timestamp.
configurationItem.configurationItemStatus
target.asset.attribute.labels.value
The value is taken from the
configurationItem.configurationItemStatus
field. The key is set to "Configuration Item Status".
configurationItem.relationships.name
additional.fields.value.list_value.values.string_value
The value is taken from the
configurationItem.relationships.name
field. The key is set to "configurationItem.relationships.resource_names".
configurationItem.relationships.resourceId
additional.fields.value.list_value.values.string_value
The value is taken from the
configurationItem.relationships.resourceId
field. The key is set to "configurationItem.relationships.resource_ids".
configurationItem.relationships.resourceType
additional.fields.value.list_value.values.string_value
The value is taken from the
configurationItem.relationships.resourceType
field. The key is set to "configurationItem.relationships.resource_types".
configurationItem.resourceId
target.resource.id
The value is taken from the
configurationItem.resourceId
field.
configurationItem.resourceType
target.resource.resource_subtype
The value is taken from the
configurationItem.resourceType
field.
N/A
metadata.event_type
If
configurationItemDiff.changeType
is "UPDATE",
metadata.event_type
is set to "RESOURCE_WRITTEN". If
configurationItemDiff.changeType
is "CREATE",
metadata.event_type
is set to "RESOURCE_CREATION". If
configurationItem.configurationItemStatus
is "OK" or "ResourceDiscovered",
metadata.event_type
is set to "RESOURCE_READ". If
configurationItem.configurationItemStatus
is "ResourceDeleted",
metadata.event_type
is set to "RESOURCE_DELETION". If none of these conditions are met,
metadata.event_type
is set to "GENERIC_EVENT".
N/A
metadata.log_type
Set to "AWS_CONFIG".
N/A
metadata.product_name
Set to "AWS Config".
N/A
metadata.vendor_name
Set to "AMAZON".
N/A
target.asset.attribute.cloud.environment
Set to "AMAZON_WEB_SERVICES".
N/A
target.resource.resource_type
Set to "VIRTUAL_MACHINE".
Need more help?
Get answers from Community members and Google SecOps professionals.
