# Collect AWS Key Management Service logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-kms/  
**Scraped:** 2026-03-05T09:50:37.218066Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Key Management Service logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Key Management Service (KMS) logs to Google Security Operations. AWS KMS is a fully managed service that lets you to create and control encryption keys used to encrypt your data. This integration helps in monitoring and auditing the usage of encryption keys.
Before you begin
Ensure you have the following prerequisites:
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
How to configure CloudTrail for AWS KMS
Sign in to the
AWS Management Console
.
In the search bar, type and select
CloudTrail
from the services list.
Click
Create trail
.
Provide a
Trail name
(for example,
KMS-Activity-Trail
).
Select the
Enable for all accounts in my organization
checkbox.
Type the S3 bucket URI created earlier (the format should be:
s3://your-log-bucket-name/
), or create a new S3 bucket.
If SSE-KMS enabled, provide a name for
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
How to set up the AWS Key Management Service feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Key Management Service
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
data.detail.awsRegion
principal.location.country_or_region
Directly mapped from the
data.detail.awsRegion
field in the raw log.
data.detail.eventCategory
security_result.category_details
Directly mapped from the
data.detail.eventCategory
field in the raw log.
data.detail.eventName
metadata.product_event_type
Directly mapped from the
data.detail.eventName
field in the raw log. This field determines the
metadata.event_type
value based on the logic: if eventName is "Decrypt" or "Encrypt", then event_type is "USER_RESOURCE_ACCESS", if eventName is "GenerateDataKey" then event_type is "USER_RESOURCE_CREATION", otherwise event_type is "GENERIC_EVENT".
data.detail.requestID
additional.fields.key
Value is hardcoded to "requestID" in the parser code.
data.detail.requestID
additional.fields.value.string_value
Directly mapped from the
data.detail.requestID
field in the raw log.
data.detail.requestParameters.encryptionAlgorithm
security_result.detection_fields.key
Value is hardcoded to "encryptionAlgorithm" in the parser code.
data.detail.requestParameters.encryptionAlgorithm
security_result.detection_fields.value
Directly mapped from the
data.detail.requestParameters.encryptionAlgorithm
field in the raw log.
data.detail.resources.ARN
target.resource.id
Directly mapped from the
data.detail.resources.ARN
field in the raw log.
data.detail.resources.type
target.resource.resource_subtype
Directly mapped from the
data.detail.resources.type
field in the raw log.
data.detail.userIdentity.sessionContext.attributes.mfaAuthenticated
principal.user.attribute.labels.key
Value is hardcoded to "mfaAuthenticated" in the parser code.
data.detail.userIdentity.sessionContext.attributes.mfaAuthenticated
principal.user.attribute.labels.value
Directly mapped from the
data.detail.userIdentity.sessionContext.attributes.mfaAuthenticated
field in the raw log.
data.detail.userIdentity.sessionContext.sessionIssuer.principalId
principal.user.userid
Directly mapped from the
data.detail.userIdentity.sessionContext.sessionIssuer.principalId
field in the raw log.
data.detail.userIdentity.sessionContext.sessionIssuer.userName
principal.user.user_display_name
Directly mapped from the
data.detail.userIdentity.sessionContext.sessionIssuer.userName
field in the raw log.
data.detail.userIdentity.type
principal.user.attribute.roles.name
Directly mapped from the
data.detail.userIdentity.type
field in the raw log.
data.id
metadata.product_log_id
Directly mapped from the
data.id
field in the raw log.
data.time
metadata.event_timestamp.seconds
The seconds value of the timestamp parsed from the
data.time
field in the raw log.
N/A
metadata.event_type
This field is derived by the parser logic based on the value of
data.detail.eventName
: if eventName is "Decrypt" or "Encrypt", then event_type is "USER_RESOURCE_ACCESS", if eventName is "GenerateDataKey" then event_type is "USER_RESOURCE_CREATION", otherwise event_type is "GENERIC_EVENT".
N/A
metadata.log_type
Value is hardcoded to "AWS_KMS" in the parser code.
N/A
metadata.product_name
Value is hardcoded to "AWS Key Management Service" in the parser code.
N/A
metadata.vendor_name
Value is hardcoded to "AMAZON" in the parser code.
N/A
principal.asset.attribute.cloud.environment
Value is hardcoded to "AMAZON_WEB_SERVICES" in the parser code.
Need more help?
Get answers from Community members and Google SecOps professionals.
