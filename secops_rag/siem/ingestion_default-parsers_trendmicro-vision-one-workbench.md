# Collect Trend Micro Vision One Workbench logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-workbench/  
**Scraped:** 2026-03-05T09:29:38.182262Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trend Micro Vision One Workbench logs
Supported in:
Google secops
SIEM
This document explains how to ingest Trend Micro Vision One Workbench logs to
Google Security Operations using AWS S3. The parser transforms Trend Micro Vision
One Workbench logs from JSON format into a Unified Data Model (UDM).
Before you begin
Google SecOps instance
Privileged access to Trend Micro Vision One
Configure Logging on Trend Micro Vision One
Sign in to the
Trend Micro Vision One
console.
Go to
Workflow and Automation
>
Third-Party Integration
.
Click
Google Security Operations SIEM
.
Under
Access key
, click
Generate key
.
Copy and save the
access key ID
and
secret access key
.
Under
Data transfer
, enable the toggle next to
Workbench Data
.
An S3 URI is generated and the data begins to be sent to the corresponding S3 bucket.
Copy and save the S3 URL for use at a later time.
Set up feeds
To configure a feed, follow these steps:
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
In the
Feed name
field, enter a name for the feed (for example,
Trend Micro Vision One Workbench Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Trend Micro Vision One Workbench
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: The bucket URI (the format should be:
s3://log-bucket-name/
).
Replace the following:
log-bucket-name
: the name of the bucket.
Source deletion options
: Select
Never delete files
. Data in the S3 bucket is retained for 7 days before being purged.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Need more help?
Get answers from Community members and Google SecOps professionals.
