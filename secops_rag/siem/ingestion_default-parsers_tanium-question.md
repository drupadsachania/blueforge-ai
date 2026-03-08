# Collect Tanium Question logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-question/  
**Scraped:** 2026-03-05T09:29:06.138834Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Question logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Question logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Question logs contain query execution metadata, audit information, and question results data in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Tanium Core Platform
7.0 or later
Tanium Interact
module for question management
Tanium Connect
module installed with valid license
Privileged access to
Tanium Console
with administrative rights
Privileged access to
AWS
(S3, IAM).
Configure Tanium question audit service account
Sign in to the
Tanium Console
.
Go to
Administration
>
Global Settings
.
Navigate to
Question Audit
settings.
Configure audit logging to capture question execution metadata.
Ensure the service account has appropriate audit access permissions.
Collect Tanium Question prerequisites
Sign in to the
Tanium Console
as an administrator.
Go to
Administration
>
Permissions
>
Users
.
Create or identify a service account user with the following roles:
Question Author
or
Administrator
role for question access.
Connect User
role privilege.
Read Saved Question
permission for audit content sets.
Access to monitored computer groups (recommended:
All Computers
group).
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
tanium-question-logs
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
Configure Tanium Connect AWS S3 destination
Sign in to the
Tanium Console
.
Go to
Modules
>
Connect
.
Click
Create Connection
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Question Audit to S3 for SecOps
).
Description
: Optional description (for example,
Export question execution and audit data to AWS S3 for Google SecOps ingestion
).
Enable
: Select to enable the connection to run on schedule.
Click
Next
.
Configure the connection source
In the
Source
section, provide the following configuration details:
Source Type
: Select
Saved Question
.
Saved Question
: Select one of the following question audit-related saved questions:
Question Log
for question execution history.
Action History
for administrative actions and question deployment.
User Activity
for user interaction with questions.
System Status
for platform performance metrics.
Computer Group
: Select
All Computers
or specific computer groups to monitor.
Refresh Interval
: Set appropriate interval for data collection (for example,
30 minutes
).
Click
Next
.
Configure AWS S3 destination
In the
Destination
section, provide the following configuration details:
Destination Type
: Select
AWS S3
.
Destination Name
: Enter a unique name (for example,
Google SecOps Question S3 Destination
).
AWS Access Key
: Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
AWS Secret Access Key
: Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
Bucket Name
: Enter your S3 bucket name (for example,
tanium-question-logs
).
Region
: Select the AWS region where your S3 bucket is located.
Key Prefix
: Enter a prefix for the S3 objects (for example,
tanium/question/
).
Click
Next
.
Configure filters
In the
Filters
section, configure data filtering options:
Send new items only
: Select this option to send only new question data since the last export.
Column filters
: Add filters based on specific question attributes if needed (for example, filter by question type, user, or execution status).
Click
Next
.
Format data for AWS S3
In the
Format
section, configure the data format:
Format
: Select
JSON
.
Options
:
Include headers
: Deselect to avoid headers in JSON output.
Include empty cells
: Select based on your preference.
Advanced Options
:
File naming
: Use default timestamp-based naming.
Compression
: Select
Gzip
to reduce storage costs and transfer time.
Click
Next
.
Schedule the connection
In the
Schedule
section, configure the export schedule:
Enable schedule
: Select to enable automatic scheduled exports.
Schedule type
: Select
Recurring
.
Frequency
: Select
Every 30 minutes
for regular question audit data export.
Start time
: Set appropriate start time for the first export.
Click
Next
.
Save and verify connection
Review the connection configuration in the summary screen.
Click
Save
to create the connection.
Click
Test Connection
to verify the configuration.
If the test is successful, click
Run Now
to perform an initial export.
Monitor the connection status in the
Connect Overview
page.
Configure a feed in Google SecOps to ingest Tanium Question logs
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
Tanium Question logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Question
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-question-logs/tanium/question/
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
Need more help?
Get answers from Community members and Google SecOps professionals.
