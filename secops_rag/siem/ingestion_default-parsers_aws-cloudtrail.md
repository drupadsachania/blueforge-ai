# Collect AWS CloudTrail logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudtrail/  
**Scraped:** 2026-03-05T09:16:49.341299Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS CloudTrail logs
Supported in:
Google secops
SIEM
This document describes how to collect AWS CloudTrail logs by setting
up a Google Security Operations feed and how log fields map to
Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps
.
A typical deployment consists of AWS CloudTrail and the
Google SecOps feed configured to send logs to
Google SecOps. Your deployment might be different from the
typical deployment described in this document.
The deployment contains the following components:
AWS CloudTrail
: The platform that collects logs.
AWS S3
: The platform that stores logs.
Google SecOps feed
: The Google SecOps feed
that fetches logs from AWS S3 and writes logs to Google SecOps.
Google SecOps
: The platform that retains and analyzes the
logs from AWS CloudTrail.
An ingestion label identifies the parser that normalizes raw log data
to structured UDM format. The information into this document applies to the
parser with the
AWS_CLOUDTRAIL
ingestion label.
Before you begin
Make sure you have the following prerequisites:
AWS Account
prerequisites for using AWS CloudTrail are met. For more information, see
AWS CloudTrail setup
.
All systems in the deployment architecture use the UTC time zone
Basic steps to ingest logs from S3 with SQS
This section describes the basic steps for ingesting AWS CloudTrail logs into
your Google SecOps instance. The steps describe how to do this
using Amazon S3 with Amazon SQS as the feed source type.
Configure AWS CloudTrail and S3
In this procedure, you configure AWS CloudTrail logs to be written to an S3 bucket.
In the AWS console, search for
CloudTrail
.
Click
Create trail
.
Provide a
Trail name
.
Select
Create new S3 bucket
. You may also choose to use an existing S3 bucket.
Provide a name for
AWS KMS alias
, or choose an existing
AWS KMS Key
.
You can leave the other settings as default, and click
Next
.
Choose
Event type
, add
Data events
as required, and click
Next
.
Review the settings in
Review and create
, and click
Create trail
.
In the AWS console, search for
Amazon S3 Buckets
.
Click the newly created log bucket, and select the folder
AWSLogs
. Then click
Copy S3 URI
and save it for use in the following steps.
Set up a Standard SQS Queue and SNS
If you use an SQS queue, it must be a
Standard
queue, not a FIFO queue.
Enable AWS CloudTrail and configure it to deliver logs to an S3 bucket using a new or existing trail.
Open the AWS SNS console and create a new Standard topic. Name it, e.g., CloudTrail-Notification-Topic.
Create a SQS queue using the AWS SQS console, e.g., CloudTrail-Notification-Queue, and update its access policy to allow the SNS topic ARN to send messages. For details about creating SQS queues, see
Getting started with Amazon SQS
.
Example SQS policy snippet:
{
   "Version": "2012-10-17",
   "Id": `
PolicyForSNS
`,
   "Statement": [
      {
         "Sid": "AllowSNS",
         "Effect": "Allow",
         "Principal": { "Service": "sns.amazonaws.com" },
         "Action": "SQS:SendMessage",
         "Resource": "arn:aws:sqs:
REGION
:
ACCOUNT_ID
:
CloudTrail-Notification-Queue
",
         "Condition": {
         "ArnEquals": { "aws:SourceArn": "arn:aws:sns:
REGION
:
ACCOUNT_ID
:
CloudTrail-Notification-Topic
"}
         }
      }
   ]
}
Go to the
SNS topic
→
Subscriptions
→
Create subscription
, set Protocol to SQS, and Endpoint to the ARN of the SQS queue.
CloudTrail doesn't natively push new logs to SNS. To enable notifications, you can use a
CloudTrail Event Selector for Management Events
, or use
CloudTrail integration with CloudWatch Logs
and then create a CloudWatch Event Rule that triggers notifications by setting an SNS topic as the target. For more details, see
set up notifications on your S3 bucket
.
Example event pattern:
{
   "source": ["aws.s3"],
   "detail-type": ["AWS API Call via CloudTrail"],
   "detail": {
      "eventName": ["PutObject"],
      "requestParameters": {
         "bucketName": [`
CloudTrail-Notification-Topic
`]
      }
   }
}
Make sure IAM roles or policies allow CloudWatch Events to publish to SNS, and make sure SNS is allowed to send messages to SQS.
Configure AWS IAM user
Configure an AWS IAM user which Google SecOps will be used to access both the SQS queue (if used) and the S3 bucket.
In the AWS console, search for
IAM
.
Click
Users
, and then in the following screen, click
Create Users
.
Provide a name for the user, for example,
chronicle-feed-user
, and select
Provide user access to the AWS Management Console
.
Select
Attach existing policies directly
and select
AmazonS3ReadOnlyAccess
or
AmazonS3FullAccess
, as required.
AmazonS3FullAccess
would be used if Google SecOps should clear the S3 buckets after reading logs, to optimize AWS S3 storage costs.
As a recommended alternative to the previous step, you can further restrict access to only the specified S3 bucket by creating a custom policy. Click
Create policy
and follow the
AWS documentation
to create a custom policy.
When you apply a policy, make sure that you have included
sqs:DeleteMessage
.
Google SecOps isn't able to delete messages if the
sqs:DeleteMessage
permission isn't attached to the SQS queue. All the messages are accumulated on
the AWS side, which causes a delay as Google SecOps repeatedly attempts to transfer the same files.
Click
Next:Tags
.
Add any tags if required, and click
Next:Review
.
Review the configuration and click
Create user
.
Once the user is created, go to the
Security Credentials
tab, and click
Create Access Key
.
Choose
CLI
and click
Next:Tags
.
Add any tags if required, then click
Create Access Key: Review
.
Copy the
Access Key ID
and
Secret Access Key
of the created user, for use in the next step.
To find the
SubjectID
, follow these steps:
Initiate the AWS CloudTrail feed setup in Google SecOps.
Check the AWS CloudTrail logs for entries related to the feed setup attempt.
Identify the log entry showing a numeric username. This number is the
SubjectID
.
Use this
SubjectID
in your AWS IAM role's trust policy to grant the necessary permissions.
Configuring KMS key permissions
A KMS key is required to decrypt CloudTrail logs, which are encrypted server-side.
AWS KMS provides enhanced encryption and security for sensitive data stored in Amazon S3.
In the AWS console, search for
Key Management Service (KMS)
.
Click
Create Key:Next
.
Add an
Alias
for the key. Optionally, add a
Description
and
Tags
if required. Click
Next: Review
.
After reviewing the configuration, click
Next
.
Select the
Key Users
who should have access to this key, then click
Finish
.
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
How to set up the AWS CloudTrail feed
Click the
Amazon Cloud Platform
pack.
In the
AWS CloudTrail
log type, specify the following values:
Specify values for the following fields:
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
Supported  AWS CloudTrail log types
The AWS CloudTrail parser supports the following services:
apigateway.amazonaws.com
appconfig.amazonaws.com
autoscaling.amazonaws.com
cloud9.amazonaws.com
cloudsearch.amazonaws.com
cloudshell.amazonaws.com
cloudtrail.amazonaws.com
config.amazonaws.com
devicefarm.amazonaws.com
ds.amazonaws.com
dynamodb.amazonaws.com
ec2-instance-connect.amazonaws.com
ec2.amazonaws.com
ecr-public.amazonaws.com
ecr.amazonaws.com
ecs.amazonaws.com
eks.amazonaws.com
elasticache.amazonaws.com
elasticloadbalancing.amazonaws.com
firehose.amazonaws.com
guardduty.amazonaws.com
health.amazonaws.com
iam.amazonaws.com
imagebuilder.amazonaws.com
kinesis.amazonaws.com
kinesisanalytics.amazonaws.com
kinesisvideo.amazonaws.com
kms.amazonaws.com
lambda.amazonaws.com
logs.amazonaws.com
macie2.amazonaws.com
monitoring.amazonaws.com
network-firewall.amazonaws.com
organizations.amazonaws.com
quicksight.amazonaws.com
ram.amazonaws.com
rds.amazonaws.com
resource-explorer-2.amazonaws.com
resource-groups.amazonaws.com
route53-recovery-readiness.amazonaws.com
route53.amazonaws.com
route53domains.amazonaws.com
route53resolver.amazonaws.com
s3-outposts.amazonaws.com
s3.amazonaws.com
s3express.amazonaws.com
secretsmanager.amazonaws.com
securityhub.amazonaws.com
ses.amazonaws.com
signin.amazonaws.com
ssm.amazonaws.com
sts.amazonaws.com
waf-regional.amazonaws.com
waf.amazonaws.com
wafv2.amazonaws.com
Supported AWS CloudTrail log formats
The AWS CloudTrail parser supports logs in JSON format.
Supported AWS CloudTrail sample logs
JSON:
{
  "Records": [{
      "eventVersion": "1.08",
      "userIdentity": {
          "type": "AssumedRole",
          "principalId": "AROAXELJRGZMPHEYTK4Q4:redlock",
          "arn": "arn:aws:sts::111111111111:assumed-role/PrismaCloudReadOnlyRole/redlock",
          "accountId": "111111111111",
          "accessKeyId": "ASIAXELJRGZMNUCV3DC4",
          "sessionContext": {
              "sessionIssuer": {
                  "type": "Role",
                  "principalId": "AROAXELJRGZMPHEYTK4Q4",
                  "arn": "arn:aws:iam::111111111111:role/PrismaCloudReadOnlyRole",
                  "accountId": "111111111111",
                  "userName": "PrismaCloudReadOnlyRole"
              },
              "webIdFederationData": {},
              "attributes": {
                  "creationDate": "2021-07-01T03:20:01Z",
                  "mfaAuthenticated": "false"
              }
          }
      },
      "eventTime": "2021-07-01T03:35:42Z",
      "eventSource": "kms.amazonaws.com",
      "eventName": "DescribeKey",
      "awsRegion": "eu-west-1",
      "sourceIPAddress": "198.51.100.0",
      "userAgent": "aws-sdk-java/1.11.1025Linux/4.14.232-176.381.amzn2.x86_64OpenJDK_64-Bit_Server_VM/11.0.10+9java/11.0.10groovy/2.5.12vendor/AdoptOpenJDKcfg/retry-mode/legacy",
      "requestParameters": {
          "keyId": "11a011a1-1010-11a1-a0aa-c4e1a9367642"
      },
      "responseElements": null,
      "requestID": "11a011a1-1010-11a1-a0aa-604ac86fc50e",
      "eventID": "11a011a1-1010-11a1-a0aa-17ef2bdeb889",
      "readOnly": true,
      "resources": [{
          "accountId": "111111111111",
          "type": "AWS::KMS::Key",
          "ARN": "arn:aws:kms:eu-west-1:111111111111:key/11a011a1-1010-11a1-a0aa-c4e1a9367642"
      }],
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111111111111",
      "eventCategory": "Management"
  }]
}
For more information on Field mapping and UDM mapping, refer to
AWS Cloudtrail field mapping
Need more help?
Get answers from Community members and Google SecOps professionals.
