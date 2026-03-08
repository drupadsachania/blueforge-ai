# Collect AWS VPC Flow Logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc/  
**Scraped:** 2026-03-05T09:19:55.971113Z

---

Home
Documentation
Security
Google Security Operations
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS VPC Flow Logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS VPC Flow Logs to Google Security Operations using three different methods: Amazon S3 (Text format), Amazon CloudWatch Logs with Kinesis Data Firehose, and CSV format in Amazon S3. AWS VPC Flow Logs is a feature that lets you capture information about the IP traffic going to and from network interfaces in your VPC. This integration lets you send these logs to Google SecOps for analysis and monitoring.
Supported AWS VPC Flow Log formats
Google SecOps supports the ingestion of AWS VPC Flow Logs in two primary text formats:
JSON Format
: The
AWS_VPC_FLOW
log type parses logs in JSON format. In this format, each log entry includes both a key and its corresponding value, making the data self-describing.
CSV Format
: Google SecOps also provides a parser for AWS VPC Flow Logs in CSV format. This format lists field keys only once in the header row, with subsequent rows containing only comma-separated values.
Because the CSV format doesn't include field keys in each log entry, the AWS_VPC_FLOW_CSV parser relies on a strict, predefined order of values. Your CSV files must adhere to the following field order for correct parsing:
Version,Account_id,Interface_id,Srcaddr,Dstaddr,Srcport,Dstport,Protocol,Packets,Bytes,Start,End,Action,Log_status,Vpc_id,Subnet_id,Instance_id,Tcp_flags,Type,Pkt_srcaddr,Pkt_dstaddr,Region,Az_id,Sublocation_type,Sublocation_id,Pkt_src_aws_service,Pkt_dst_aws_service,Flow_direction,Traffic_path,Ecs_cluster_arn,Ecs_cluster_name,Ecs_container_instance_arn,Ecs_container_instance_id,Ecs_container_id,Ecs_second_container_id,Ecs_service_name,Ecs_task_definition_arn,Ecs_task_arn,Ecs_task_id
The following is an example of a CSV log line:
7,369096419186,eni-0520bb5efed19d33a,10.119.32.34,10.119.223.3,51256,16020,6,14,3881,1723542839,1723542871,ACCEPT,OK,vpc-0769a6844ce873a6a,subnet-0cf9b2cb32f49f258,i-088d6080f45f5744f,0,IPv4,10.119.32.34,10.119.223.3,ap-northeast-1,apne1-az4,-,-,-,-,ingress,,-,-,-,-,-,-,-,-,-,-
For fields where no value is available, an empty value (for example, , ,) should be passed to maintain the correct positional order within the CSV row.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance.
Privileged access to AWS.
Option 1: Configure AWS VPC Flow Logs export using AWS S3 (Text format)
The following section outlines how to configure Amazon S3 and Identity and Access Management permissions to enable the export of VPC Flow Logs for analysis by Google SecOps.
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save bucket
Name
and
Region
for future reference (for example,
aws-vpc-flowlogs
).
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
AmazonS3FullAccess
policy.
Select the policy.
Click
Next
.
Click
Add permissions
.
Create VPC Flow Logs (destination: Amazon S3, Text format)
Open
AWS Console
>
VPC
>
Your VPCs/Subnets/Network interfaces
and select the scope you want to log.
Click
Actions
>
Create flow log
.
Provide the following configuration details:
Filter
: Choose
All
(or
Accept
/
Reject
) per your policy.
Maximum aggregation interval
: Select
1 minute
(recommended) or
10 minutes
.
Destination
:
Send to an Amazon S3 bucket
.
S3 bucket ARN
: Enter the bucket name created in the previous section in the following format:
arn:aws:s3:::<your-bucket>
.
Log record format
: Select
AWS default format
.
Log file format
: Select
Text (Plain)
.
Optional: Disable
Hive-compatible prefixes
and
Hourly partitions
unless you need them.
Click
Create flow log
.
Configure a feed in Google SecOps to ingest AWS VPC Flow Logs (S3 Text)
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
field, enter a name for the feed (for example,
AWS VPC Flow Logs - S3 (Text)
).
Select
Amazon S3 V2
as the
Source type
.
Select
AWS VPC Flow
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: Enter the S3 bucket address (for example,
s3://<your-bucket>/AWSLogs/<account-id>/vpcflowlogs/<region>/
).
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Default 180 Days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Option 2: Configure AWS VPC Flow Logs export using Amazon CloudWatch Logs and Kinesis Data Firehose
After setting up the flow logs to go to CloudWatch, this option provides an additional layer of data export by streaming that log data to a destination of your choice using Kinesis Data Firehose.
Create VPC Flow Logs (destination: Amazon CloudWatch Logs)
Open
AWS Console
>
VPC
>
Your VPCs/Subnets/Network interfaces
.
Click
Actions
>
Create flow log
.
Provide the following configuration details:
Filter
: Choose
All
(or
Accept
/
Reject
) per your policy.
Maximum aggregation interval
: Select
1 minute
(recommended) or
10 minutes
.
Destination
: Select
Send to CloudWatch Logs
.
Destination log group
: Select or create a log group (for example,
/aws/vpc/flowlogs
).
IAM role
: Select a role that can write to CloudWatch Logs.
Log record format
: Select
AWS default
(version 2) or
Custom
(includes additional fields).
Click
Create flow log
.
Create a feed in Google SecOps to get Endpoint URL and Secret Key
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
field, enter a name for the feed (for example,
AWS VPC Flow Logs - CloudWatch via Firehose
).
Select
Amazon Data Firehose
as the
Source type
.
Select
AWS VPC Flow
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
: The
asset namespace
(for example,
aws.vpc.flowlogs.cwl
).
Ingestion labels
: The label to be applied to the events from this feed (for example,
source=vpc_flow_firehose
).
Click
Next
.
Review the feed configuration and click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy
and
save
the secret key as you cannot view this secret again.
Go to the
Details
tab.
Copy
the feed endpoint URL from the
Endpoint Information
field.
Click
Done
.
Create an API key for the Amazon Data Firehose feed
Go to the
Google Cloud
console
Credentials
page.
Click
Create
credentials, and then select
API key
.
Copy and save the key in a secure location.
Restrict the API key
access
to the
Google SecOps API
.
Configure IAM permissions for CloudWatch Logs to Firehose
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
Paste the following policy JSON, replacing
<region>
and
<account-id>
with your AWS Region and account ID:
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
and paste:
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
Attach the policy
CWLtoFirehoseWrite
to the role.
Name the role
CWLtoFirehoseRole
and click
Create role
.
Configure Amazon Kinesis Data Firehose to Google SecOps
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
Name
:
cwlogs-to-secops
HTTP endpoint URL
: Enter the
Feed HTTPS endpoint URL
from Google SecOps with the API Key appended:
<ENDPOINT_URL>?key=<API_KEY>
HTTP method
: Select
POST
.
Under
Access key
:
Enter the
Secret key
generated in Google SecOps feed (this becomes the
X-Amz-Firehose-Access-Key
header).
Buffering hints
: set
Buffer size
=
1 MiB
,
Buffer interval
=
60 seconds
.
Compression
: select
Disabled
.
S3 backup
: select
Disabled
.
Leave
retry
and
logging
settings as
default
.
Click
Create delivery stream
.
Subscribe the CloudWatch Logs group to the Firehose stream
Go to
CloudWatch
>
Logs
>
Log groups
.
Select the target log group (for example,
/aws/vpc/flowlogs
).
Open the
Subscription filters
tab and click
Create
.
Choose
Create Amazon Kinesis Data Firehose subscription filter
.
Provide the following configuration details:
Destination
: Select delivery stream
cwlogs-to-secops
.
Grant permission
: Choose role
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
Option 3: Configure AWS VPC Flow Logs in CSV format using Amazon S3
Transform logs to CSV format (optional)
Ensure your CSV rows follow a
strict, consistent column order
that matches the fields you selected in your VPC Flow Log
custom format
(for example, the canonical v2 field set, or your v5/v7 set). Do
not
include a header row in production files unless your parser option expects one.
Write CSV files to a stable prefix, for example:
s3://<your-bucket>/vpcflowlogs-csv/<region>/year=<year>/month=<month>/day=<day>/
.
Configure a feed in Google SecOps to ingest AWS VPC Flow Logs (CSV)
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
field, enter a name for the feed (for example,
AWS VPC Flow Logs - S3 (CSV)
).
Select
Amazon S3 V2
as the
Source type
.
Select
AWS VPC Flow (CSV)
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: Enter the S3 bucket address (for example,
s3://<your-bucket>/vpcflowlogs-csv/<region>/
).
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Default 180 Days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM mapping table
Log field
UDM mapping
Logic
accountId
read_only_udm.metadata.product_log_id
Value extracted from the raw log field
accountId
.
action
read_only_udm.security_result.action_details
Value extracted from the raw log field
action
.
action
read_only_udm.security_result.action
Mapped to ALLOW if
action
is ACCEPT, mapped to BLOCK if
action
is
REJECT
.
az_id
read_only_udm.principal.cloud.availability_zone
Value extracted from the raw log field
az_id
.
bytes
read_only_udm.network.received_bytes
Value extracted from the raw log field
bytes
.
dstaddr
read_only_udm.target.ip
Value extracted from the raw log field
dstaddr
.
dstport
read_only_udm.target.port
Value extracted from the raw log field
dstport
.
end_time
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
end_time
.
end_time
read_only_udm.metadata.ingested_timestamp
Value extracted from the raw log field
end_time
.
flow_direction
read_only_udm.network.direction
Mapped to INBOUND if
flow_direction
is
ingress
, mapped to OUTBOUND if
flow_direction
is
egress
.
InstanceID
read_only_udm.principal.cloud.project.id
Value extracted from the raw log field
InstanceID
.
interfaceId
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
interfaceId
.
logStatus
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
logStatus
.
packets
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
packets
.
pkt_dst_aws_service
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
pkt_dst_aws_service
.
pkt_dstaddr
read_only_udm.intermediary.ip
Value extracted from the raw log field
pkt_dstaddr
.
pkt_srcaddr
read_only_udm.intermediary.ip
Value extracted from the raw log field
pkt_srcaddr
.
pkt_src_aws_service
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
pkt_src_aws_service
.
protocol
read_only_udm.network.ip_protocol
Mapped to TCP if
protocol
is 6, mapped to UDP if
protocol
is 17, otherwise mapped to UNKNOWN_IP_PROTOCOL.
Region
read_only_udm.principal.location.country_or_region
Value extracted from the raw log field
Region
.
srcaddr
read_only_udm.principal.ip
Value extracted from the raw log field
srcaddr
.
srcport
read_only_udm.principal.port
Value extracted from the raw log field
srcport
.
start_time
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
start_time
.
start_time
read_only_udm.metadata.event_timestamp
Value extracted from the raw log field
start_time
.
SubnetID
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
SubnetID
.
tcp_flags
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
tcp_flags
.
traffic_path
read_only_udm.about.resource.attribute.labels.value
Value extracted from the raw log field
traffic_path
.
version
read_only_udm.metadata.product_version
Value extracted from the raw log field
version
.
vpcID
read_only_udm.principal.cloud.vpc.id
Value extracted from the raw log field
vpcID
.
read_only_udm.metadata.vendor_name
Hardcoded to
AMAZON
.
read_only_udm.metadata.product_name
Hardcoded to
AWS VPC Flow
.
read_only_udm.metadata.log_type
Hardcoded to
AWS_VPC_FLOW
.
read_only_udm.metadata.event_type
Mapped to
NETWORK_CONNECTION
if
dstaddr
is not empty, otherwise mapped to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
