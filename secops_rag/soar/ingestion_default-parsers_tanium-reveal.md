# Collect Tanium Reveal logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal/  
**Scraped:** 2026-03-05T10:01:11.335955Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Reveal logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Reveal logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Reveal produces sensitive data discovery alerts, compliance findings, and data classification results in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser processes the JSON logs, transforming them into the UDM format. It parses the JSON message, extracts fields like Computer ID, Computer Name, and Rule Name, maps them to UDM fields, and handles specific Reveal events like "Endpoints with Confirmed Sensitive Data" to populate security result details.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Tanium Core Platform
7.0 or later
Tanium Reveal
module installed and configured
Tanium Connect
module installed with valid license
Tanium Trends
3.6.343 or later for reporting integration
Privileged access to
Tanium Console
with administrative rights
Privileged access to
AWS
(S3, IAM)
Configure Tanium Reveal service account
Sign in to the
Tanium Console
.
Go to
Modules
>
Reveal
.
Click
Settings
at the top right.
In the
Service Account
section, configure the following:
Service Account User
: Select a user with appropriate Reveal permissions.
Verify
the account has Connect User role privilege.
Confirm
access to Reveal data sources and rules.
Click
Save
to apply the service account configuration.
Collect Tanium Reveal prerequisites
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
Reveal Administrator
or
Reveal Read Only User
role.
Connect User
role privilege.
Access to monitored computer groups (recommended:
All Computers
group).
Read Saved Question
permission for Reveal content sets.
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
tanium-reveal-logs
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
Reveal Findings to S3 for SecOps
).
Description
: Optional description (for example,
Export sensitive data findings and compliance alerts to AWS S3 for Google SecOps ingestion
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
: Select one of the following Reveal-related saved questions:
Reveal - Endpoints with Confirmed Sensitive Data
for confirmed findings.
Reveal - Rule Matches
for detailed rule match results.
Reveal - Data Classification Results
for data type classification.
Reveal - Compliance Findings
for regulatory compliance status.
Computer Group
: Select
All Computers
or specific computer groups to monitor.
Refresh Interval
: Set appropriate interval for data collection (for example,
15 minutes
for sensitive data alerts).
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
Google SecOps Reveal S3 Destination
).
AWS Access Key
: Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
AWS Secret Access Key
: Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
Bucket Name
: Enter your S3 bucket name (for example,
tanium-reveal-logs
).
Region
: Select the AWS region where your S3 bucket is located.
Key Prefix
: Enter a prefix for the S3 objects (for example,
tanium/reveal/
).
Click
Next
.
Configure filters
In the
Filters
section, configure data filtering options:
Send new items only
: Select this option to send only new sensitive data findings since the last export.
Column filters
: Add filters based on specific finding attributes if needed (for example, filter by rule severity, data type, or compliance framework).
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
Every 15 minutes
for timely sensitive data alerts.
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
Configure a feed in Google SecOps to ingest Tanium Reveal logs
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
Tanium Reveal logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Reveal
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-reveal-logs/tanium/reveal/
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
