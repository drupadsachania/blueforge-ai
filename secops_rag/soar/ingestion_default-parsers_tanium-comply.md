# Collect Tanium Comply logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-comply/  
**Scraped:** 2026-03-05T10:01:01.702188Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Comply logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Comply logs to Google Security Operations using Amazon S3 using Tanium Connect's native S3 export capability. The parser transforms JSON log data into a unified data model (UDM). It extracts key vulnerability information like CVE ID, CVSS scores, affected IP addresses, and timestamps, then restructures them into the standardized UDM format for consistent security analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to
Tanium Connect
and
Tanium Console
Tanium Comply
2.1 or later installed and configured
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
tanium-comply-logs
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
Configure permissions on Amazon S3 bucket
In the
Amazon S3 console
, choose the bucket that you previously created.
Click
Permissions
>
Bucket policy
.
In the
Bucket Policy Editor
, add the following policy:
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
"AWS"
:
"arn:aws:iam::YOUR_ACCOUNT_ID:user/tanium-connect-s3-user"
},
"Action"
:
[
"s3:PutObject"
,
"s3:PutObjectAcl"
,
"s3:GetObject"
,
"s3:ListBucket"
],
"Resource"
:
[
"arn:aws:s3:::tanium-comply-logs"
,
"arn:aws:s3:::tanium-comply-logs/*"
]
}
]
}
Replace the following variables:
Change
YOUR_ACCOUNT_ID
to your AWS account ID.
Change
tanium-comply-logs
to your actual bucket name if different.
Change
tanium-connect-s3-user
to your actual IAM username if different.
Click
Save
.
Configure Tanium Connect for S3 export
Sign in to the
Tanium Console
as an administrator.
Go to
Tanium Connect
>
Connections
.
Click
Create Connection
.
In the
General Information
section, provide the following configuration details:
Name
: Enter a descriptive name (for example,
Tanium Comply to S3
).
Description
: Enter a meaningful description (for example,
Export Tanium Comply findings to S3 for Google SecOps ingestion
).
Enable
: Select to enable the connection.
Log Level
: Select
Information
(default) or adjust as needed.
In the
Configuration
section, for
Source
, select
Tanium Comply (Findings)
.
Configure the Comply source settings:
Finding Type
: Select the type of findings to export (All, Compliance, or Vulnerability).
Include Resolved Findings
: Select whether to include findings that have been resolved.
Computer Groups
: Select the computer groups to include in the export (default: All Computers).
For
Destination
, select
AWS S3
.
Provide the following configuration details:
Destination Name
: Enter a name (for example,
Google SecOps S3 Bucket
).
AWS Access Key
: Enter the Access Key ID from the IAM user created earlier.
AWS Secret Key
: Enter the Secret Access Key from the IAM user created earlier.
Bucket Name
: Enter your S3 bucket name (for example,
tanium-comply-logs
).
Bucket Path
: Optional. Enter a path prefix (for example,
tanium/comply/
).
Region
: Select the AWS region where your bucket resides (for example,
us-east-1
).
In the
Format
section, configure the output format:
Format Type
: Select
JSON
.
Include Column Headers
: Select if you want column headers included.
Generate Document
: Deselect this option to send raw JSON data.
Optional: In the
Configure Output
section, configure filters and custom columns as needed.
In the
Schedule
section, configure when the connection runs:
Schedule Type
: Select
Cron
.
Cron Expression
: Enter a cron expression for regular exports (for example,
0 */4 * * *
for every 4 hours).
Start Date
: Set the start date for the schedule.
Click
Save Changes
.
From the
Connect Overview
page, go to
Connections
.
Click the connection you created (
Tanium Comply to S3
).
Click
Run Now
to test the connection.
Confirm that you want to run the connection.
Monitor the connection status and verify that compliance findings are being exported to your S3 bucket.
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
"arn:aws:s3:::tanium-comply-logs/*"
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
"arn:aws:s3:::tanium-comply-logs"
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
Configure a feed in Google SecOps to ingest Tanium Comply logs
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
Tanium Comply logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Comply
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-comply-logs/tanium/comply/
(adjust path if you used a different bucket name or path).
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket (from the read-only user created above).
Secret Access Key
: User secret key with access to the S3 bucket (from the read-only user created above).
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log field
UDM mapping
Logic
Computer Name
entity.entity.asset.hostname
Directly mapped from "Computer Name" field after replacing spaces with underscores.
CVE
entity.entity.asset.vulnerabilities.cve_id
Directly mapped from "CVE" field.
CVSS v3 Score
entity.entity.asset.vulnerabilities.cvss_base_score
Directly mapped from "CVSS v3 Score" field after renaming to cvss_base_score.
CVSS v3 Severity
entity.entity.asset.vulnerabilities.severity_details
Directly mapped from "CVSS v3 Severity" field.
CVSS v3 Vector
entity.entity.asset.vulnerabilities.cvss_vector
Directly mapped from "CVSS v3 Vector" field.
First Found Date
entity.entity.asset.vulnerabilities.first_found
Parsed from "First Found Date" field and converted to RFC 3339 UTC format. If the date contains "-", it's appended with "T00:00:00Z". Otherwise, the date is extracted using grok and then converted.
IP Address
entity.entity.asset.ip
Each IP address from the "IP Address" array is mapped to a separate "ip" field in the UDM.
Last Found Date
entity.entity.asset.vulnerabilities.last_found
Parsed from "Last Found Date" field and converted to RFC 3339 UTC format. If the date contains "-", it's appended with "T00:00:00Z". Otherwise, the date is extracted using grok and then converted.
Title
entity.entity.asset.vulnerabilities.name
Directly mapped from "Title" field.
collection_time.nanos
entity.metadata.collected_timestamp.nanos
Directly mapped from the "collection_time.nanos" field.
collection_time.seconds
entity.metadata.collected_timestamp.seconds
Directly mapped from the "collection_time.seconds" field.
time
entity.metadata.interval.start_time
Parsed from "time" field and converted to RFC 3339 UTC format.
-
entity.metadata.entity_type
Set to "ASSET".
-
entity.metadata.product_entity_id
Set to "Tanium: " concatenated with the value of the "computerName" field.
-
entity.metadata.product_name
Set to "Comply".
-
entity.metadata.vendor_name
Set to "Tanium".
Need more help?
Get answers from Community members and Google SecOps professionals.
