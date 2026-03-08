# Collect AWS VPC Transit Gateway flow logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-transit-gateway/  
**Scraped:** 2026-03-05T09:50:49.361692Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS VPC Transit Gateway flow logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS VPC Transit Gateway flow logs to Google Security Operations using CloudWatch Logs and Kinesis Data Firehose. Transit Gateway flow logs capture detailed network traffic metadata across your Transit Gateway attachments. This integration streams these logs into Google SecOps for monitoring and security analytics.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Enable Transit Gateway flow logs (to CloudWatch logs)
Sign in to the
AWS Console
Go to
VPC
>
Transit gateways
(or
Transit gateway attachments
).
Select the target resource(s).
Click
Actions
>
Create flow log
.
Provide the following configuration details:
Destination
: Select
Send to CloudWatch Logs
.
Log group
: Choose or create a log group (for example,
/aws/tgw/flowlogs
).
IAM role
: Select a role that can write to CloudWatch Logs.
Maximum aggregation interval
: Choose
1 minute
(recommended) or
10 minutes
.
Log record format
: Select
Default
(or
Custom
if you need additional fields).
Click
Create flow log
.
Configure a Feed in Google SecOps to Ingest Transit Gateway Flow Logs
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
AWS Transit Gateway Flow Logs — CloudWatch via Firehose
.
Select
Amazon Data Firehose
as the
Source type
.
Select
Amazon VPC Transit Gateway Flow Logs
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
.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label applied to the events from this feed.
Click
Next
>
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
In
Google Cloud console
>
APIs & Services
>
Credentials
>
Create credentials
>
API key
, create an
API key
and
restrict it to Chronicle API
. Copy the
API key
.
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
. (Example name:
cwlogs-to-secops
)
Configure IAM Permissions and Subscribe the Log Group
In the
AWS console
, go to
IAM
>
Policies
>
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
.
Click
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
Select the Transit Gateway
log group
you enabled earlier.
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
