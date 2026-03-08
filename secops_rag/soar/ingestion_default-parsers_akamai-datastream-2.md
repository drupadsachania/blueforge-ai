# Collect Akamai DataStream 2 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-datastream-2/  
**Scraped:** 2026-03-05T09:49:27.679663Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akamai DataStream 2 logs
Supported in:
Google secops
SIEM
This document explains how to ingest Akamai DataStream 2 logs to Google Security Operations using Amazon S3.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to
Akamai Control Center
(DataStream 2 configuration access)
Privileged access to
AWS
(S3, IAM)
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save bucket
Name
and
Region
for future reference (for example,
akamai-cloud-monitor
).
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
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
Configure the IAM policy and role for S3 uploads
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
"Sid"
:
"AllowAkamaiWriteToS3"
,
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
"arn:aws:s3:::akamai-datastream-2-logs/akamai/datastream2/json/*"
}
]
}
Replace
akamai-datastream-2-logs
if you entered a different bucket name.
Click
Next
>
Create policy
.
Go to
IAM
>
Users
>
Create user
.
Name the user
akamai-datastream-writer
.
Attach the newly created policy.
Create access keys for this user to use in Akamai DataStream 2 configuration.
Configure Akamai DataStream 2 to deliver logs to Amazon S3
In
Akamai Control Center
go to
DataStream 2
.
Click
Create a stream
.
Select log type
appropriate for your property (for example,
Delivery
,
Edge DNS
,
GTM
).
In
Data sets
, select the fields you require. Keep defaults unless you have a specific need.
Go to
Delivery
>
Destination
and select
Amazon S3
.
Fill the S3 destination details using the newly created bucket:
Bucket
:
akamai-datastream-2-logs
Folder path
:
akamai/datastream2/json/
Region
: Your bucket region
Access key ID
: The User access key created earlier
Secret access key
: The User secret access key created earlier
Set
Log format
to
JSON
.
Optional: In
Delivery options
, set
Push frequency
to
30 seconds
.
Click
Validate & Save
>
Next
>
Activate
.
Optional: Create read-only IAM user & keys for Google SecOps
Go to
AWS Console
>
IAM
>
Users
>
Add users
.
Click
Add users
.
Provide the following configuration details:
User
: Enter
secops-reader
.
Access type
: Select
Access key – Programmatic access
.
Click
Create user
.
Attach minimal read policy (custom):
Users
>
secops-reader
>
Permissions
>
Add permissions
>
Attach policies directly
>
Create policy
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
"s3:GetObject"
],
"Resource"
:
"arn:aws:s3:::akamai-datastream-2-logs/*"
},
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:ListBucket"
],
"Resource"
:
"arn:aws:s3:::akamai-datastream-2-logs"
}
]
}
Set the name to
secops-reader-policy
.
Go to
Create policy
>
search/select
>
Next
>
Add permissions
.
Go to
Security credentials
>
Access keys
>
Create access key
.
Download the
CSV
(these values are entered into the feed).
Configure a feed in Google SecOps to ingest Akamai DataStream 2 logs
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
Akamai DataStream 2 logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Akamai DataStream 2
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://akamai-datastream-2-logs/akamai/datastream2/json/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
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
Supported Akamai Datastream 2 Sample Logs
JSON
{
  "logName": "projects/monotaro-akamai-log/logs/akamai_data_stream",
  "resource": {
    "type": "cloud_run_revision",
    "labels": {
      "service_name": "akamai-datastream2",
      "configuration_name": "hhhhh",
      "location": "asia-northeast1",
      "project_id": "monotaro-akamai-log",
      "revision_name": "akamai-datastream2-brpwf"
    }
  },
  "jsonPayload": {
    "cliip": "0.0.0.0",
    "cookie": "sid=MASKED_SESSION_ID",
    "reqtimesec": "1704844800.068",
    "trace": "projects/monotaro-akamai-log/traces/acc4d1aeffecdf96896e5aff5cf1fbf5",
    "errorcode": "-",
    "totalbytes": "27489",
    "reqport": "443",
    "overheadbytes": "1160",
    "reqhost": "www.example.com",
    "tlsversion": "TLSv1.3",
    "referer": "masked URL",
    "reqendtimemsec": "15",
    "acclang": "-",
    "reqid": "80c241bc",
    "city": "TOKYO",
    "maxagesec": "-",
    "cp": "1219543",
    "uncompressedsize": "-",
    "proto": "HTTP/2",
    "querystr": "s=MASKED_QUERY_PARAM&v=other_param",
    "range": "-",
    "objsize": "25510",
    "transfertimemsec": "1",
    "reqmethod": "GET",
    "rspcontentlen": "25510",
    "statuscode": "200",
    "dnslookuptimemsec": "-",
    "turnaroundtimemsec": "83",
    "xforwardedfor": "-",
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) MASKED_UA",
    "cachestatus": "0",
    "rspcontenttype": "application/json",
    "bytes": "25510",
    "version": "3",
    "tlsoverheadtimemsec": "0",
    "country": "JP",
    "reqpath": "recsys/v1/recommend",
    "customfield": "MASKED_CUSTOM_FIELD_1,MASKED_CUSTOM_FIELD_2",
    "securityrules": "mntr_25916||"
  },
  "timestamp": "2024-01-10T00:00:00.068+00:00",
  "receiveTimestamp": "2024-01-10T00:00:19.987565+00:00",
  "insertId": "148w3lkg16liikb"
}
Need more help?
Get answers from Community members and Google SecOps professionals.
