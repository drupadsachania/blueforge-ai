# Collect AWS API Gateway access logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-api-gateway/  
**Scraped:** 2026-03-05T09:19:33.313097Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS API Gateway access logs
Supported in:
Google secops
SIEM
This document explains how to ingest Amazon API Gateway access logs to Google Security Operations using
AWS CloudWatch Logs and Kinesis Data Firehose
. Amazon API Gateway provides REST and HTTP APIs to build and manage APIs at scale. Access logs help monitor API usage and troubleshoot issues. This integration streams these logs into Google SecOps for analysis and monitoring.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Enable Amazon API Gateway Access Logging (to CloudWatch Logs)
Go to
AWS Console
>
API Gateway
.
For
REST APIs
:
Open your
Stage
>
Logs/Tracing
>
enable Access logging
.
Log format
: Select
JSON
.
{
"requestId"
:
"$context.requestId"
,
"ip"
:
"$context.identity.sourceIp"
,
"requestTime"
:
"$context.requestTime"
,
"httpMethod"
:
"$context.httpMethod"
,
"routeKey"
:
"$context.routeKey"
,
"status"
:
"$context.status"
,
"protocol"
:
"$context.protocol"
,
"responseLength"
:
"$context.responseLength"
,
"integrationLatency"
:
"$context.integrationLatency"
,
"error"
:
"$context.error.message"
}
CloudWatch Logs log group
: Choose or create a log group (for example,
/aws/apigateway/access
).
For
HTTP APIs
:
Select your
API
>
Monitor
>
Logging
.
Select
Stage
>
Edit
.
Enable
Access logging
.
Use the same JSON log format as above.
CloudWatch Logs log group
: Choose or create a log group (for example,
/aws/apigateway/access
).
Click
Save
.
Configure a Feed in Google SecOps to Ingest Amazon API Gateway logs
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
field, enter
Amazon API Gateway - CloudWatch via Firehose
.
Select
Amazon Data Firehose
as the
Source type
.
Select
Amazon API Gateway
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
: Optional
n
Asset namespace
:
aws.api_gateway
Ingestion labels
: For example,
source=apigw_access
,
aws_region=<your-region>
Click
Next
.
Review the feed configuration and click
Submit
.
In the feed
Details
, click
Generate Secret Key
and copy the
Secret Key
.
Copy the
Feed HTTPS endpoint URL
from
Endpoint Information
.
Create a
Google Cloud API key
in
APIs & Services
>
Credentials
>
Create credentials
>
API key
, and restrict it to
Chronicle API
.
Copy and save the API key in a secure location.
Configure Amazon Kinesis Data Firehose (Direct to Google SecOps)
In the
AWS Console
, go to
Kinesis
>
Data Firehose
>
Create delivery stream
.
Provide the following configuration details:
Source
: Select
Direct PUT or other sources
.
Destination
: Choose
HTTP endpoint
.
HTTP endpoint URL
: Enter
ENDPOINT_URL?key=API_KEY
(use the Feed HTTPS endpoint URL and the API key from the previous step).
HTTP method
: Select
POST
.
Access key
: Paste the Secret Key generated in the feed.
Buffering hints
: Set
Buffer size
=
1 MiB
,
Buffer interval
=
60 seconds
.
Compression
: Select
Disabled
.
S3 backup
: Select
Disabled
.
Leave
retry
and
logging
settings as default.
Click
Create delivery stream
. (For example,
cwlogs-to-secops
.)
Configure IAM Permissions and Subscribe the Log Group
In the
AWS Console
, go to
IAM
>
Policies
>
Create policy
>
JSON
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
Replace
<region>
and
<account-id>
with your AWS Region and account ID.
Name the policy
CWLtoFirehoseWrite
and click
Create policy
.
Go to
IAM
>
Roles
>
Create role
.
Select
Custom trust policy
and enter the following:
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
"logs.<your-region>.amazonaws.com"
},
"Action"
:
"sts:AssumeRole"
}
]
}
Attach the policy
CWLtoFirehoseWrite
to the role.
Name the role
CWLtoFirehoseRole
and click
Create role
.
Go to
CloudWatch
>
Logs
>
Log groups
.
Select the
API Gateway
log group you created earlier.
Open the
Subscription filters
tab and click
Create
.
Choose
Create Amazon Kinesis Data Firehose subscription filter
.
Configure the following:
Destination
: Delivery stream
cwlogs-to-secops
.
Grant permission
: Role
CWLtoFirehoseRole
.
Filter name
: Enter
all-events
.
Filter pattern
: Leave empty to send all events.
Click
Start streaming
.
Need more help?
Get answers from Community members and Google SecOps professionals.
