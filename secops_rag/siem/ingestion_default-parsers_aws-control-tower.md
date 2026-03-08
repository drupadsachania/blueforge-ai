# Collect AWS Control Tower logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-control-tower/  
**Scraped:** 2026-03-05T09:19:38.746891Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Control Tower logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Control Tower logs to Google Security Operations. AWS Control Tower enables governance, compliance, and security monitoring across multiple AWS accounts. This integration let you to analyze logs from AWS Control Tower for better visibility and security posture.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure Amazon S3 bucket
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
Search for and select
AmazonS3FullAccess
and
CloudWatchLogsFullAccess
policies.
Click
Next
.
Click
Add permissions
.
Configure CloudTrail in AWS Control Tower
Sign in to the
AWS Management Console
.
Go to
AWS Control Tower
.
In the search bar, type
CloudTrail
and select it from the
services list
.
Click
Create Trail
to create a new trail.
Specify Trail Settings:
Trail name
: Provide a meaningful name for the trail (for example,
ControlTowerTrail
).
Apply trail to all regions
: Ensure that you select
Yes
for
Apply trail to all regions
.
Management events
: Ensure that
Read/Write
events are set to
All
..
Optional:
Data events
: Enable S3 data events and Lambda data events to capture detailed data activity.
Optional:
Log file validation
: Enable this to ensure that log files are not tampered with once they're stored.
In the
Event
selector, choose to log
Management events
and
Data events
.
How to configure CloudTrail
Go to the AWS IAM Console.
Click
Roles
.
Search for the role that
CloudTrail
uses
AWSServiceRoleForCloudTrail
(the role is automatically created when you set up CloudTrail).
In the
Permissions tab
for the role, click
Attach policies
.
Search for
CloudTrailS3DeliveryPolicy
.
Select the checkbox next to the
CloudTrailS3DeliveryPolicy
policy.
Click
Attach policy
.
Go to the AWS
CloudTrail
Console.
In the
Storage location
section, select
S3
as the destination for log files.
Select the
S3 bucket
you created earlier.
Click
Allow
when prompted to grant CloudTrail permission to write logs to your chosen bucket.
Review your settings and click
Create
(or
Save changes
if you're editing an existing trail).
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
How to set up the AWS Control Tower feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Control Tower
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
Log field
UDM mapping
Logic
awsAccountId
target.user.group_identifiers
The AWS account ID associated with the event.
digestPublicKeyFingerprint
target.file.sha1
The fingerprint of the public key used to sign the digest.
digestPublicKeyFingerprint
target.resource.attribute.labels.value
The fingerprint of the public key used to sign the digest.
digestS3Bucket
target.resource.name
The name of the S3 bucket where the digest is stored.
digestS3Object
target.file.full_path
The path to the digest object in the S3 bucket.
digestSignatureAlgorithm
network.tls.cipher
The algorithm used to sign the digest.
digestSignatureAlgorithm
target.resource.attribute.labels.value
The algorithm used to sign the digest.
digestStartTime
metadata.event_timestamp
The start time of the digest period. Used as event time if eventTime is not available.
eventCategory
security_result.category_details
The category of the event.
eventID
metadata.product_log_id
The unique ID of the event.
eventName
metadata.product_event_type
The name of the event.
eventName
security_result.summary
The name of the event, used to generate the security result summary.
eventSource
target.application
The source of the event.
eventTime
metadata.event_timestamp
The time the event occurred.
eventType
additional.fields.value.string_value
The type of the event.
logFiles.hashValue
about.file.sha256
The SHA-256 hash of the log file.
logFiles.s3Bucket
about.resource.name
The name of the S3 bucket where the log file is stored.
logFiles.s3Object
about.file.full_path
The path to the log file object in the S3 bucket.
previousDigestHashValue
target.file.sha256
The SHA-256 hash of the previous digest.
recipientAccountId
target.resource.attribute.labels.value
The AWS account ID of the recipient of the event.
Records.awsRegion
principal.location.name
The AWS region where the event occurred.
Records.errorCode
security_result.rule_id
The error code, if any, associated with the request.
Records.errorMessage
security_result.description
The error message, if any, associated with the request.
Records.eventCategory
security_result.category_details
The category of the event.
Records.eventID
metadata.product_log_id
The unique ID of the event.
Records.eventName
metadata.product_event_type
The name of the event.
Records.eventName
security_result.summary
The name of the event, used to generate the security result summary.
Records.eventSource
target.application
The source of the event.
Records.eventTime
metadata.event_timestamp
The time the event occurred.
Records.eventType
additional.fields.value.string_value
The type of the event.
Records.requestID
target.resource.attribute.labels.value
The ID of the request.
Records.requestParameters.groupName
target.group.group_display_name
The name of the group, if any, associated with the request.
Records.requestParameters.userName
src.user.userid
The name of the user, if any, associated with the request.
Records.requestParameters.userName
src.user.user_display_name
The name of the user, if any, associated with the request.
Records.responseElements.ConsoleLogin
security_action
The result of the console login attempt.
Records.responseElements.ConsoleLogin
security_result.summary
The result of the console login attempt, used to generate the security result summary.
Records.sourceIPAddress
principal.hostname
The IP address of the principal. Used as hostname if not a valid IP.
Records.sourceIPAddress
principal.ip
The IP address of the principal.
Records.tlsDetails.cipherSuite
network.tls.cipher
The cipher suite used for the TLS connection.
Records.tlsDetails.tlsVersion
network.tls.version
The TLS version used for the connection.
Records.userAgent
network.http.user_agent
The user agent of the request.
Records.userIdentity.accessKeyId
additional.fields.value.string_value
The access key ID used for the request.
Records.userIdentity.accountId
principal.user.group_identifiers
The AWS account ID of the user.
Records.userIdentity.arn
principal.user.attribute.labels.value
The ARN of the user.
Records.userIdentity.arn
target.user.userid
The ARN of the user. Used as userid if userName is not available.
Records.userIdentity.principalId
principal.user.product_object_id
The principal ID of the user.
Records.userIdentity.sessionContext.attributes.mfaAuthenticated
principal.user.attribute.labels.value
Whether MFA was used for the request.
Records.userIdentity.sessionContext.sessionIssuer.userName
principal.user.userid
The username of the user who issued the session.
Records.userIdentity.type
principal.resource.type
The type of identity used for the request.
Records.userIdentity.userName
target.user.userid
The username of the user.
-
extensions.auth.mechanism
Set to "REMOTE".
-
metadata.event_type
Set to "STATUS_UPDATE", "USER_RESOURCE_ACCESS", "USER_LOGIN", or "GENERIC_EVENT" based on the eventName.
-
metadata.log_type
Set to "AWS_CONTROL_TOWER".
-
metadata.product_name
Set to "AWS Control Tower".
-
metadata.vendor_name
Set to "AWS".
-
principal.asset.attribute.cloud.environment
Set to "AMAZON_WEB_SERVICES".
-
security_result.action
Set to "ALLOW" or "BLOCK" based on the errorCode.
-
security_result.severity
Set to "INFORMATIONAL".
Need more help?
Get answers from Community members and Google SecOps professionals.
