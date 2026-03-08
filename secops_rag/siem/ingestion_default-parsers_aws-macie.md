# Collect AWS Macie logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-macie/  
**Scraped:** 2026-03-05T09:19:46.652877Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Macie logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Macie logs to Google Security Operations. AWS Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data. This integration will allow you to send Macie logs to Google SecOps for enhanced analysis and monitoring.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure Amazon S3 and IAM
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
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
Optional: Configuring AWS Macie
Sign in to the
AWS Management Console
.
In the search bar, type and select
Macie
from the services list.
Click
Create job
.
Create a new bucket or proceed with the existing one.
Add
Schedule job
.
Select all Managed Data Identifiers.
Skip
Select Custom Data Identifiers
and click
Next
.
Skip
Select Allow list
and click
Next
.
Provide a meaningful name and description.
Click
Next
.
Review and click
Submit
.
How to configure CloudTrail for AWS Macie
Sign in to the
AWS Management Console
.
In the search bar, type and select
CloudTrail
from the services list.
If you want to proceed with a new trail, click
Create trail
.
Provide a
Trail name
(for example,
Macie-Activity-Trail
).
Select the
Enable for all accounts in my organization
checkbox.
Type the S3 bucket URI created earlier (the format should be:
s3://your-log-bucket-name/
), or create a new S3 bucket.
If SSE-KMS is enabled, provide a name for
AWS KMS alias
, or choose an
existing AWS KMS Key
.
You can leave the other settings as default.
Click
Next
.
Select
Management events
and
Data events
under
Event Types
.
Click
Next
.
Review the settings in
Review and create
.
Click
Create trail
.
Optional: if you created a new bucket, continue with the following process:
Go to
S3
.
Identify and select the newly created log bucket.
Select the folder
AWSLogs
.
Click
Copy S3 URI
and save it.
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
How to set up the AWS Macie feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Macie
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
accountId
principal.group.product_object_id
Directly mapped from the
accountId
field.
category
security_result.category_details
Directly mapped from the
category
field.
classificationDetails.jobArn
security_result.rule_name
Directly mapped from the
classificationDetails.jobArn
field.
classificationDetails.jobId
security_result.rule_id
Directly mapped from the
classificationDetails.jobId
field.
classificationDetails.originType
security_result.rule_type
Directly mapped from the
classificationDetails.originType
field.
classificationDetails.result.mimeType
target.file.mime_type
Directly mapped from the
classificationDetails.result.mimeType
field.
classificationDetails.result.sensitiveData.category
security_result.detection_fields.value
Directly mapped from the
classificationDetails.result.sensitiveData.category
field.  The parser iterates through the
sensitiveData
array and creates multiple
detection_fields
objects.
classificationDetails.result.sensitiveData.totalCount
security_result.detection_fields.value
Directly mapped from the
classificationDetails.result.sensitiveData.totalCount
field. The parser iterates through the
sensitiveData
array and creates multiple
detection_fields
objects.
createdAt
metadata.event_timestamp
Parsed and converted to UDM timestamp format from the
createdAt
field.
description
security_result.description
Directly mapped from the
description
field.
id
metadata.product_log_id
Directly mapped from the
id
field.  Hardcoded to
SCAN_FILE
in the parser. Taken from the top-level
log_type
field in the raw log. Hardcoded to
AWS Macie
in the parser. Directly mapped from the
schemaVersion
field. Hardcoded to
AMAZON
in the parser. Concatenated from
resourcesAffected.s3Bucket.name
,
region
, and the string ".s3.amazonaws.com".
region
target.location.name
Directly mapped from the
region
field.
resourcesAffected.s3Bucket.arn
target.resource_ancestors.product_object_id
Directly mapped from the
resourcesAffected.s3Bucket.arn
field.
resourcesAffected.s3Bucket.createdAt
target.resource_ancestors.attribute.creation_time
Parsed and converted to UDM timestamp format from the
resourcesAffected.s3Bucket.createdAt
field.
resourcesAffected.s3Bucket.name
target.resource_ancestors.name
Directly mapped from the
resourcesAffected.s3Bucket.name
field.
resourcesAffected.s3Bucket.owner.displayName
target.user.user_display_name
Directly mapped from the
resourcesAffected.s3Bucket.owner.displayName
field.
resourcesAffected.s3Bucket.owner.id
target.user.userid
Directly mapped from the
resourcesAffected.s3Bucket.owner.id
field.
resourcesAffected.s3Object.eTag
target.file.md5
Directly mapped from the
resourcesAffected.s3Object.eTag
field.
resourcesAffected.s3Object.key
target.file.names
Directly mapped from the
resourcesAffected.s3Object.key
field.
resourcesAffected.s3Object.key
target.resource.name
Directly mapped from the
resourcesAffected.s3Object.key
field.
resourcesAffected.s3Object.lastModified
target.resource.attribute.last_update_time
Parsed and converted to UDM timestamp format from the
resourcesAffected.s3Object.lastModified
field.
resourcesAffected.s3Object.path
target.file.full_path
Prefixed with "s3://" and mapped from the
resourcesAffected.s3Object.path
field.
resourcesAffected.s3Object.path
target.resource.product_object_id
Directly mapped from the
resourcesAffected.s3Object.path
field.
resourcesAffected.s3Object.size
target.file.size
Directly mapped from the
resourcesAffected.s3Object.size
field after converting to unsigned integer.
resourcesAffected.s3Object.storageClass
target.resource.attribute.labels.value
Directly mapped from the
resourcesAffected.s3Object.storageClass
field.  The key is hardcoded to "storageClass". Hardcoded to
DATA_AT_REST
in the parser.
security_result.detection_fields.key
category
,
totalCount
Hardcoded keys for the detection fields.
severity.description
security_result.severity
Mapped from the
severity.description
field.  "Low" is mapped to
LOW
, "Medium" to
MEDIUM
, and "High" to
HIGH
. Hardcoded to
AMAZON_WEB_SERVICES
in the parser. Hardcoded to
STORAGE_OBJECT
in the parser. Hardcoded to
STORAGE_BUCKET
in the parser.
title
security_result.summary
Directly mapped from the
title
field.
type
metadata.product_event_type
Directly mapped from the
type
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
