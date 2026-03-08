# Collect AWS CloudWatch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudwatch/  
**Scraped:** 2026-03-05T09:19:36.318073Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS CloudWatch logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS CloudWatch logs to Google Security Operations using Amazon S3.
AWS CloudWatch is a monitoring and observability service that collects operational data in the form of logs, metrics, and events from AWS resources and applications. This integration uses Amazon Data Firehose to stream CloudWatch log data to an S3 bucket, which Google SecOps then ingests using an Amazon S3 V2 feed.
Before you begin
A Google SecOps instance
Privileged access to the
AWS Management Console
with permissions to manage:
Amazon CloudWatch Logs
(log groups, subscription filters)
Amazon Data Firehose
(delivery streams)
Amazon S3
(buckets)
AWS IAM
(roles, policies, users)
Configure AWS S3 bucket
Create an
Amazon S3 bucket
following this user guide:
Creating a
bucket
.
Save the bucket
Name
and
Region
for future reference (for example,
cwlogs-to-secops
).
Configure the IAM role for Amazon Data Firehose
Amazon Data Firehose requires an IAM role to write logs to your S3 bucket.
Create the IAM policy
In the
AWS Console
, go to
IAM
>
Policies
>
Create policy
.
Select the
JSON
tab.
Paste the following policy (replace
cwlogs-to-secops
with your actual bucket name):
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
"S3Delivery"
,
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:AbortMultipartUpload"
,
"s3:GetBucketLocation"
,
"s3:GetObject"
,
"s3:ListBucket"
,
"s3:ListBucketMultipartUploads"
,
"s3:PutObject"
],
"Resource"
:
[
"arn:aws:s3:::cwlogs-to-secops"
,
"arn:aws:s3:::cwlogs-to-secops/*"
]
},
{
"Sid"
:
"CloudWatchLogging"
,
"Effect"
:
"Allow"
,
"Action"
:
[
"logs:PutLogEvents"
],
"Resource"
:
"arn:aws:logs:*:*:log-group:/aws/kinesisfirehose/cwlogs-to-secops:log-stream:*"
}
]
}
Click
Next
.
In the
Policy name
field, enter
FirehoseS3DeliveryPolicy
.
Click
Create policy
.
Create the IAM role
Go to
IAM
>
Roles
>
Create role
.
Select
Custom trust policy
.
Paste the following trust policy:
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
"Service"
:
"firehose.amazonaws.com"
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
Search for and select
FirehoseS3DeliveryPolicy
.
Click
Next
.
In the
Role name
field, enter
FirehoseToS3Role
.
Click
Create role
.
Create the Amazon Data Firehose stream
Open the
Kinesis console
at
https://console.aws.amazon.com/kinesis
.
In the navigation pane, select
Amazon Data Firehose
.
Click
Create Firehose stream
.
Under
Choose source and destination
, provide the following configuration:
Source
: Select
Direct PUT
.
Destination
: Select
Amazon S3
.
In the
Firehose stream name
field, enter
cwlogs-to-secops
.
Under
Transform records
, in the
Decompress source records from Amazon CloudWatch Logs
section:
Select
Turn on decompression
.
Do
not
select
Turn on message extraction
.
Under
Destination settings
:
S3 bucket
: Select the S3 bucket
cwlogs-to-secops
.
S3 bucket prefix
(optional): Enter
cloudwatch-logs/
.
S3 bucket error output prefix
(optional): Enter
firehose-errors/
.
Under
Buffer hints
:
Buffer size
:
5
MiB (default).
Buffer interval
:
300
seconds (default).
Under
Advanced settings
:
Server-side encryption
: Optional. Enable if encryption is required.
Error logging
: Select
Enabled
(recommended).
Permissions
: Select
Choose existing IAM role
, then select
FirehoseToS3Role
.
Click
Create Firehose stream
.
Wait for the stream
Status
to show
Active
.
Configure the IAM role for CloudWatch Logs
CloudWatch Logs requires an IAM role to send log data to the Firehose stream.
Create the IAM policy
Go to
IAM
>
Policies
>
Create policy
.
Select the
JSON
tab.
Paste the following policy (replace
<region>
and
<account-id>
with your AWS region and account ID):
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
"firehose:PutRecord"
,
"firehose:PutRecordBatch"
],
"Resource"
:
"arn:aws:firehose:<region>:<account-id>:deliverystream/cwlogs-to-secops"
}
]
}
Click
Next
.
In the
Policy name
field, enter
CWLtoFirehoseWritePolicy
.
Click
Create policy
.
Create the IAM role
Go to
IAM
>
Roles
>
Create role
.
Select
Custom trust policy
.
Paste the following trust policy (replace
<region>
with your AWS region):
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
"Service"
:
"logs.<region>.amazonaws.com"
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
Search for and select
CWLtoFirehoseWritePolicy
.
Click
Next
.
In the
Role name
field, enter
CWLtoFirehoseRole
.
Click
Create role
.
Create CloudWatch Logs subscription filter
In the
AWS Console
, go to
CloudWatch
>
Logs
>
Log groups
.
Select the target log group that you want to stream to Google SecOps.
Select the
Subscription filters
tab.
Click
Create
>
Create Amazon Data Firehose subscription filter
.
Provide the following configuration details:
Destination
: Select the Firehose stream
cwlogs-to-secops
.
Grant permission
: Select the role
CWLtoFirehoseRole
.
Subscription filter name
: Enter a descriptive name (for example,
secops-all-events
).
Log format
: Select
Other
.
Subscription filter pattern
: Leave empty to send all events, or enter a filter pattern to send only specific events.
Click
Start streaming
.
Configure IAM user for Google SecOps
Google SecOps needs an IAM user with access to the S3 bucket to ingest the delivered logs.
Create a
User
following this user guide:
Creating an IAM
user
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
Optional: Add description tag.
Click
Create access key
.
Click
Download .csv file
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
Configure a feed in Google SecOps to ingest AWS CloudWatch logs
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
Enter a unique name for the
Feed name
.
Select
Amazon S3 V2
as the
Source type
.
Select
AWS CloudWatch
as the
Log type
.
Click
Next
and then click
Submit
.
Specify values for the following fields:
S3 URI
:
s3://cwlogs-to-secops/cloudwatch-logs/
Source deletion option
: Select the deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days (default is 180 days).
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
and then click
Submit
.
UDM mapping table
Log Field
UDM Mapping
Logic
account
principal.user.userid
The value of
account
from the raw log is mapped to the
principal.user.userid
field.
account_id
principal.user.userid
The value of
account_id
from the raw log is mapped to the
principal.user.userid
field.
AlertId
metadata.product_log_id
The value of
AlertId
from the raw log is mapped to the
metadata.product_log_id
field.
arrivalTimestamp
metadata.event_timestamp
The value of
arrivalTimestamp
from the raw log is converted to a timestamp and mapped to the
metadata.event_timestamp
field.
attemptsMade
additional.fields
The value of
attemptsMade
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "Attempts Made".
awsAccountId
principal.asset_id
The value of
awsAccountId
from the raw log is prepended with "AWS Account id: " and mapped to the
principal.asset_id
field.
billed_duration
additional.fields
The value of
billed_duration
from the raw log is added as a key-value pair to the
additional.fields
with the key "billed_duration".
BytesIn
network.received_bytes
The value of
BytesIn
from the raw log is converted to an unsigned integer and mapped to the
network.received_bytes
field.
cipher
network.tls.cipher
The value of
cipher
from the raw log is mapped to the
network.tls.cipher
field.
Ciphers
network.tls.client.supported_ciphers
The value of
Ciphers
from the raw log is split by commas and each value is added to the
network.tls.client.supported_ciphers
array.
cloudwatchLog
security_result.description
The value of
cloudwatchLog
from the raw log is mapped to the
security_result.description
field.
CloudAccountId
metadata.product_deployment_id
The value of
CloudAccountId
from the raw log is mapped to the
metadata.product_deployment_id
field.
CloudType
target.resource.attribute.cloud.environment
The value of
CloudType
from the raw log determines the value of
target.resource.attribute.cloud.environment
. If
CloudType
is "gcp", the value is "GOOGLE_CLOUD_PLATFORM". If
CloudType
is "aws", the value is "AMAZON_WEB_SERVICES". If
CloudType
is "azure", the value is "MICROSOFT_AZURE".
Context.Execution.Id
target.resource.attribute.labels
The value of
Context.Execution.Id
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Context Id".
Context.Execution.Name
target.resource.attribute.labels
The value of
Context.Execution.Name
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Context Name".
Context.Execution.RoleArn
target.resource.product_object_id
The value of
Context.Execution.RoleArn
from the raw log is mapped to the
target.resource.product_object_id
field.
descr
metadata.description
The value of
descr
from the raw log, after removing extra whitespace, is mapped to the
metadata.description
field unless it is "-". If
descr
is empty, the value of
log
is used instead.
destination.name
target.location.country_or_region
The value of
destination.name
from the raw log is mapped to the
target.location.country_or_region
field.
destination.properties.prefix
target.resource.attribute.labels
The value of
destination.properties.prefix
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Destination properties prefix".
detail.additionalEventData.configRuleArn
security_result.rule_id
The value of
detail.additionalEventData.configRuleArn
from the raw log is mapped to the
security_result.rule_id
field.
detail.additionalEventData.configRuleName
security_result.rule_name
The value of
detail.additionalEventData.configRuleName
from the raw log is mapped to the
security_result.rule_name
field.
detail.additionalEventData.managedRuleIdentifier
additional.fields
The value of
detail.additionalEventData.managedRuleIdentifier
from the raw log is added as a key-value pair to the
additional.fields
with the key "managedRuleIdentifier".
detail.additionalEventData.notificationJobType
additional.fields
The value of
detail.additionalEventData.notificationJobType
from the raw log is added as a key-value pair to the
additional.fields
with the key "notificationJobType".
detail.awsAccountId
principal.asset_id
The value of
detail.awsAccountId
from the raw log is prepended with "AWS Account id: " and mapped to the
principal.asset_id
field.
detail.awsRegion
principal.location.name
The value of
detail.awsRegion
from the raw log is mapped to the
principal.location.name
field.
detail.configRuleArn
security_result.rule_id
The value of
detail.configRuleArn
from the raw log is mapped to the
security_result.rule_id
field.
detail.configRuleName
security_result.rule_name
The value of
detail.configRuleName
from the raw log is mapped to the
security_result.rule_name
field.
detail.configurationItem.awsAccountId
principal.user.userid
The value of
detail.configurationItem.awsAccountId
from the raw log is mapped to the
principal.user.userid
field.
detail.configurationItem.awsRegion
target.location.country_or_region
The value of
detail.configurationItem.awsRegion
from the raw log is mapped to the
target.location.country_or_region
field.
detail.configurationItem.configuration.complianceType
security_result.summary
The value of
detail.configurationItem.configuration.complianceType
from the raw log is mapped to the
security_result.summary
field.
detail.configurationItem.configuration.targetResourceId
target.resource.attribute.labels
The value of
detail.configurationItem.configuration.targetResourceId
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "configurationItem configuration targetResourceId".
detail.configurationItem.configuration.targetResourceType
target.resource.attribute.labels
The value of
detail.configurationItem.configuration.targetResourceType
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "configurationItem configuration targetResourceType".
detail.configurationItem.configurationItemCaptureTime
_target.asset.attribute.creation_time
The value of
detail.configurationItem.configurationItemCaptureTime
from the raw log is converted to a timestamp and mapped to the
_target.asset.attribute.creation_time
field.
detail.configurationItem.configurationItemStatus
target.resource.attribute.labels
The value of
detail.configurationItem.configurationItemStatus
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "configurationItem configurationItemStatus".
detail.configurationItem.configurationStateId
target.resource.attribute.labels
The value of
detail.configurationItem.configurationStateId
from the raw log is converted to a string and added as a key-value pair to the
target.resource.attribute.labels
with the key "configurationItem configurationStateId".
detail.configurationItem.resourceId
target.resource.id
The value of
detail.configurationItem.resourceId
from the raw log is mapped to the
target.resource.id
field.
detail.configurationItem.resourceType
target.resource.resource_subtype
The value of
detail.configurationItem.resourceType
from the raw log is mapped to the
target.resource.resource_subtype
field.
detail.configurationItemDiff.changedProperties.Configuration.configRuleList.1.updatedValue.configRuleArn
security_result.rule_id
The value of
detail.configurationItemDiff.changedProperties.Configuration.configRuleList.1.updatedValue.configRuleArn
from the raw log is mapped to the
security_result.rule_id
field.
detail.eventCategory
security_result.category_details
The value of
detail.eventCategory
from the raw log is mapped to the
security_result.category_details
field.
detail.eventID
metadata.product_log_id
The value of
detail.eventID
from the raw log is mapped to the
metadata.product_log_id
field.
detail.eventName
additional.fields
The value of
detail.eventName
from the raw log is added as a key-value pair to the
additional.fields
with the key "Event Name".
detail.eventSource
target.application
The value of
detail.eventSource
from the raw log is mapped to the
target.application
field.
detail.eventType
additional.fields
The value of
detail.eventType
from the raw log is added as a key-value pair to the
additional.fields
with the key "Event Type".
detail.eventVersion
metadata.product_version
The value of
detail.eventVersion
from the raw log is mapped to the
metadata.product_version
field.
detail.managementEvent
additional.fields
The value of
detail.managementEvent
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "detail managementEvent".
detail.messageType
target.resource.attribute.labels
The value of
detail.messageType
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Message Type".
detail.newEvaluationResult.complianceType
security_result.summary
The value of
detail.newEvaluationResult.complianceType
from the raw log is mapped to the
security_result.summary
field.
detail.newEvaluationResult.configRuleInvokedTime
additional.fields
The value of
detail.newEvaluationResult.configRuleInvokedTime
from the raw log is added as a key-value pair to the
additional.fields
with the key "newEvaluationResult_configRuleInvokedTime".
detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName
additional.fields
The value of
detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName
from the raw log is added as a key-value pair to the
additional.fields
with the key "newEvaluationResult_configRuleName".
detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId
additional.fields
The value of
detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId
from the raw log is added as a key-value pair to the
additional.fields
with the key "newEvaluationResult_resourceId".
detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType
additional.fields
The value of
detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType
from the raw log is added as a key-value pair to the
additional.fields
with the key "newEvaluationResult_resourceType".
detail.newEvaluationResult.resultRecordedTime
additional.fields
The value of
detail.newEvaluationResult.resultRecordedTime
from the raw log is added as a key-value pair to the
additional.fields
with the key "newEvaluationResult_resultRecordedTime".
detail.oldEvaluationResult.configRuleInvokedTime
additional.fields
The value of
detail.oldEvaluationResult.configRuleInvokedTime
from the raw log is added as a key-value pair to the
additional.fields
with the key "oldEvaluationResult_configRuleInvokedTime".
detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName
additional.fields
The value of
detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName
from the raw log is added as a key-value pair to the
additional.fields
with the key "oldEvaluationResult_configRuleName".
detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId
additional.fields
The value of
detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId
from the raw log is added as a key-value pair to the
additional.fields
with the key "oldEvaluationResult_resourceId".
detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType
additional.fields
The value of
detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType
from the raw log is added as a key-value pair to the
additional.fields
with the key "oldEvaluationResult_resourceType".
detail.oldEvaluationResult.resultRecordedTime
additional.fields
The value of
detail.oldEvaluationResult.resultRecordedTime
from the raw log is added as a key-value pair to the
additional.fields
with the key "oldEvaluationResult_resultRecordedTime".
detail.readOnly
additional.fields
The value of
detail.readOnly
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "detail readOnly".
detail.recipientAccountId
target.resource.attribute.labels
The value of
detail.recipientAccountId
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Recipient Account Id".
detail.recordVersion
metadata.product_version
The value of
detail.recordVersion
from the raw log is mapped to the
metadata.product_version
field.
detail.requestID
target.resource.attribute.labels
The value of
detail.requestID
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Detail Request ID".
detail.resourceType
target.resource.resource_subtype
The value of
detail.resourceType
from the raw log is mapped to the
target.resource.resource_subtype
field.
detail.s3Bucket
about.resource.name
The value of
detail.s3Bucket
from the raw log is mapped to the
about.resource.name
field.
detail.s3ObjectKey
target.resource.attribute.labels
The value of
detail.s3ObjectKey
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "s3ObjectKey".
detail.userAgent
network.http.user_agent
The value of
detail.userAgent
from the raw log is mapped to the
network.http.user_agent
field.
detail.userIdentity.accessKeyId
target.user.userid
The value of
detail.userIdentity.accessKeyId
from the raw log is mapped to the
target.user.userid
field.
detail.userIdentity.accountId
metadata.product_deployment_id
The value of
detail.userIdentity.accountId
from the raw log is mapped to the
metadata.product_deployment_id
field.
detail.userIdentity.arn
target.user.userid
The value of
detail.userIdentity.arn
from the raw log is mapped to the
target.user.userid
field.
detail.userIdentity.principalId
principal.user.product_object_id
The value of
detail.userIdentity.principalId
from the raw log is mapped to the
principal.user.product_object_id
field.
detail.userIdentity.sessionContext.attributes.mfaAuthenticated
principal.user.attribute.labels
The value of
detail.userIdentity.sessionContext.attributes.mfaAuthenticated
from the raw log is added as a key-value pair to the
principal.user.attribute.labels
with the key "mfaAuthenticated".
detail.userIdentity.sessionContext.sessionIssuer.userName
target.user.user_display_name
The value of
detail.userIdentity.sessionContext.sessionIssuer.userName
from the raw log is mapped to the
target.user.user_display_name
field.
detail.userIdentity.type
principal.resource.type
The value of
detail.userIdentity.type
from the raw log is mapped to the
principal.resource.type
field.
detail-type
metadata.product_event_type
The value of
detail-type
from the raw log is mapped to the
metadata.product_event_type
field.
device
principal.asset.product_object_id
The value of
device
from the raw log is mapped to the
principal.asset.product_object_id
field.
digestPublicKeyFingerprint
target.file.sha1
The value of
digestPublicKeyFingerprint
from the raw log is mapped to the
target.file.sha1
field.
digestS3Bucket
principal.resource.name
The value of
digestS3Bucket
from the raw log is mapped to the
principal.resource.name
field.
digestS3Object
principal.asset.asset_id
The value of
digestS3Object
from the raw log is prepended with "S3 Object: " and mapped to the
principal.asset.asset_id
field.
digestSignatureAlgorithm
network.tls.cipher
The value of
digestSignatureAlgorithm
from the raw log is mapped to the
network.tls.cipher
field.
digestStartTime
metadata.event_timestamp
The value of
digestStartTime
from the raw log is converted to a timestamp and mapped to the
metadata.event_timestamp
field.
dimensions.VolumeId
additional.fields
The value of
dimensions.VolumeId
from the raw log is added as a key-value pair to the
additional.fields
with the key "VolumeId".
duration
additional.fields
The value of
duration
from the raw log is added as a key-value pair to the
additional.fields
with the key "duration".
errorCode
security_result.rule_name
The value of
errorCode
from the raw log is mapped to the
security_result.rule_name
field.
errorMessage
security_result.summary
The value of
errorMessage
from the raw log is mapped to the
security_result.summary
field.
executionId
principal.process.pid
The value of
executionId
from the raw log is mapped to the
principal.process.pid
field.
host
principal.hostname
,
principal.ip
The value of
host
from the raw log, with hyphens replaced by dots, is parsed as an IP address and mapped to the
principal.ip
field if successful. Otherwise, it is mapped to the
principal.hostname
field.
http_verb
network.http.method
The value of
http_verb
from the raw log is converted to uppercase and mapped to the
network.http.method
field.
kubernetes.container_hash
additional.fields
The value of
kubernetes.container_hash
from the raw log is added as a key-value pair to the
additional.fields
with the key "container_hash".
kubernetes.container_image
additional.fields
The value of
kubernetes.container_image
from the raw log is added as a key-value pair to the
additional.fields
with the key "container_image".
kubernetes.container_name
additional.fields
The value of
kubernetes.container_name
from the raw log is added as a key-value pair to the
additional.fields
with the key "container_name".
kubernetes.docker_id
principal.asset_id
The value of
kubernetes.docker_id
from the raw log is prepended with "id: " and mapped to the
principal.asset_id
field.
kubernetes.host
principal.hostname
,
principal.ip
The value of
kubernetes.host
from the raw log, with hyphens replaced by dots, is parsed as an IP address and mapped to the
principal.ip
field if successful. Otherwise, it is mapped to the
principal.hostname
field.
kubernetes.namespace
principal.namespace
The value of
kubernetes.namespace
from the raw log is mapped to the
principal.namespace
field.
kubernetes.namespace_name
principal.namespace
The value of
kubernetes.namespace_name
from the raw log is mapped to the
principal.namespace
field.
kubernetes.pod_id
principal.asset.asset_id
The value of
kubernetes.pod_id
from the raw log is prepended with "pod_id: " and mapped to the
principal.asset.asset_id
field.
kubernetes.pod_name
additional.fields
The value of
kubernetes.pod_name
from the raw log is added as a key-value pair to the
additional.fields
with the key "pod name".
lambdaArn
principal.hostname
The value of
lambdaArn
from the raw log is mapped to the
principal.hostname
field.
level
security_result.severity
The value of
level
from the raw log determines the value of
security_result.severity
. If
level
is "Info", the value is "INFORMATIONAL". If
level
is "Error", the value is "ERROR". If
level
is "Warning", the value is "MEDIUM".
log
metadata.description
The value of
log
from the raw log is mapped to the
metadata.description
field if
descr
is empty.
logFiles
about
For each element in the
logFiles
array from the raw log, an
about
object is created with
file.full_path
set to
s3Object
,
asset.hostname
set to
s3Bucket
, and
file.sha256
set to
hashValue
.
log_processed.cause
security_result.summary
The value of
log_processed.cause
from the raw log is mapped to the
security_result.summary
field.
log_processed.ids
intermediary.hostname
For each element in the
log_processed.ids
array from the raw log, an
intermediary
object is created with
hostname
set to the element's value.
log_processed.level
security_result.severity
The value of
log_processed.level
from the raw log is mapped to the
security_result.severity
field.
log_processed.msg
metadata.description
The value of
log_processed.msg
from the raw log is mapped to the
metadata.description
field.
log_processed.ts
metadata.event_timestamp
The value of
log_processed.ts
from the raw log is converted to a timestamp and mapped to the
metadata.event_timestamp
field.
log_type
metadata.log_type
The value of
log_type
from the raw log is mapped to the
metadata.log_type
field. This is a custom field added for context.
logevent.message
security_result.description
The value of
logevent.message
from the raw log is mapped to the
security_result.description
field. It is also parsed using grok to extract additional fields.
logGroup
security_result.about.resource.name
The value of
logGroup
from the raw log is mapped to the
security_result.about.resource.name
field.
logStream
security_result.about.resource.attribute.labels
The value of
logStream
from the raw log is added as a key-value pair to the
security_result.about.resource.attribute.labels
with the key "logStream".
memory_used
additional.fields
The value of
memory_used
from the raw log is added as a key-value pair to the
additional.fields
with the key "memory_used".
metric_name
additional.fields
The value of
metric_name
from the raw log is added as a key-value pair to the
additional.fields
with the key "metric_name".
metric_stream_name
additional.fields
The value of
metric_stream_name
from the raw log is added as a key-value pair to the
additional.fields
with the key "metric_stream_name".
namespace
principal.namespace
The value of
namespace
from the raw log is mapped to the
principal.namespace
field.
owner
principal.user.userid
The value of
owner
from the raw log is mapped to the
principal.user.userid
field.
parameters
additional.fields
The value of
parameters
from the raw log is added as a key-value pair to the
additional.fields
with the key "Parameters".
Path
principal.process.file.full_path
The value of
Path
from the raw log is mapped to the
principal.process.file.full_path
field.
pid
principal.process.pid
The value of
pid
from the raw log is mapped to the
principal.process.pid
field.
PolicyName
security_result.rule_name
The value of
PolicyName
from the raw log is mapped to the
security_result.rule_name
field.
prin_host
principal.hostname
The value of
prin_host
from the raw log is mapped to the
principal.hostname
field.
principal_hostname
principal.hostname
The value of
principal_hostname
from the raw log is mapped to the
principal.hostname
field.
process
principal.application
The value of
process
from the raw log is mapped to the
principal.application
field.
rawData
additional.fields
The value of
rawData
from the raw log is added as a key-value pair to the
additional.fields
with the key "Raw Data".
Recommendation
security_result.detection_fields
The value of
Recommendation
from the raw log is added as a key-value pair to the
security_result.detection_fields
with the key "Recommendation".
referral_url
network.http.referral_url
The value of
referral_url
from the raw log is mapped to the
network.http.referral_url
field.
region
principal.location.name
The value of
region
from the raw log is mapped to the
principal.location.name
field.
resp_code
network.http.response_code
The value of
resp_code
from the raw log is converted to an integer and mapped to the
network.http.response_code
field.
resource_url
network.http.referral_url
The value of
resource_url
from the raw log is mapped to the
network.http.referral_url
field.
ResourceType
target.resource.resource_subtype
The value of
ResourceType
from the raw log is mapped to the
target.resource.resource_subtype
field.
response_body
additional.fields
The value of
response_body
from the raw log is added as a key-value pair to the
additional.fields
with the key "Response body".
Role
target.resource.product_object_id
The value of
Role
from the raw log is mapped to the
target.resource.product_object_id
field.
s3_bucket_path
target.file.full_path
The value of
s3_bucket_path
from the raw log is mapped to the
target.file.full_path
field.
sec_result.category
security_result.category
The value of
sec_result.category
is derived from the parser logic. If
descr
contains "authentication is required", the value is "AUTH_VIOLATION".
sec_result.description
security_result.description
The value of
sec_result.description
is derived from the parser logic. It is set to the value of
cloudwatchLog
if present.
sec_result.severity
security_result.severity
The value of
sec_result.severity
is derived from the parser logic. It is set based on the value of
severity
or
level
.
sec_result.summary
security_result.summary
The value of
sec_result.summary
is derived from the parser logic. It is set to the value of
log_processed.cause
or
errorMessage
if present.
security_result
security_result
The
security_result
object is constructed from various fields and parser logic.
serverId
additional.fields
The value of
serverId
from the raw log is added as a key-value pair to the
additional.fields
with the key "server_id".
severity
security_result.severity
The value of
severity
from the raw log, converted to uppercase and normalized, is mapped to the
security_result.severity
field.
Source
principal.hostname
The value of
Source
from the raw log is mapped to the
principal.hostname
field.
source
principal.hostname
The value of
source
from the raw log is mapped to the
principal.hostname
field.
SourceIP
principal.ip
The value of
SourceIP
from the raw log is mapped to the
principal.ip
field.
src_port
principal.port
If
src_port
is "80", it is converted to an integer and mapped to the
principal.port
field, and
network.application_protocol
is set to "HTTP".
stream
additional.fields
The value of
stream
from the raw log is added as a key-value pair to the
additional.fields
with the key "stream".
subscriptionFilters
security_result.about.resource.attribute.labels
For each element in the
subscriptionFilters
array from the raw log, a key-value pair is added to the
security_result.about.resource.attribute.labels
with the key "subscriptionFilter" and the value from the array.
support_contact
target.resource.attribute.labels
The value of
support_contact
from the raw log is added as a key-value pair to the
target.resource.attribute.labels
with the key "Support Contact".
t_ip
target.ip
The value of
t_ip
from the raw log, after removing hyphens, is parsed as an IP address and mapped to the
target.ip
field if successful.
time
metadata.event_timestamp
The value of
time
from the raw log is converted to a timestamp and mapped to the
metadata.event_timestamp
field.
timestamp
metadata.event_timestamp
The value of
timestamp
from the raw log is converted to a timestamp using various formats and mapped to the
metadata.event_timestamp
field.
tls
network.tls.version
The value of
tls
from the raw log is mapped to the
network.tls.version
field.
transferDetails.serverId
additional.fields
The value of
transferDetails.serverId
from the raw log is added as a key-value pair to the
additional.fields
with the key "server_id".
transferDetails.sessionId
network.session_id
The value of
transferDetails.sessionId
from the raw log is mapped to the
network.session_id
field.
transferDetails.username
principal.user.user_display_name
The value of
transferDetails.username
from the raw log is mapped to the
principal.user.user_display_name
field.
ts
metadata.event_timestamp
The value of
ts
from the raw log, combined with the timezone if available, is converted to a timestamp and mapped to the
metadata.event_timestamp
field.
type
metadata.product_event_type
The value of
type
from the raw log is mapped to the
metadata.product_event_type
field.
unit
additional.fields
The value of
unit
from the raw log is added as a key-value pair to the
additional.fields
with the key "unit".
url
target.url
The value of
url
from the raw log is mapped to the
target.url
field.
url_back_to_product
metadata.url_back_to_product
The value of
url_back_to_product
from the raw log is mapped to the
metadata.url_back_to_product
field.
User
principal.user.userid
The value of
User
from the raw log is mapped to the
principal.user.userid
field.
user
target.user.userid
,
metadata.event_type
,
extensions.auth.mechanism
If
user
is present,
metadata.event_type
is set to "USER_LOGIN",
extensions.auth.mechanism
is set to "NETWORK", and the value of
user
is mapped to
target.user.userid
.
value.count
additional.fields
The value of
value.count
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "count".
value.max
additional.fields
The value of
value.max
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "max".
value.min
additional.fields
The value of
value.min
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "min".
value.sum
additional.fields
The value of
value.sum
from the raw log is converted to a string and added as a key-value pair to the
additional.fields
with the key "sum".
workflowId
additional.fields
The value of
workflowId
from the raw log is added as a key-value pair to the
additional.fields
with the key "workflowId".
Need more help?
Get answers from Community members and Google SecOps professionals.
