# Collect Tanium Integrity Monitor logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-integrity-monitor/  
**Scraped:** 2026-03-05T10:01:06.662678Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Integrity Monitor logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Integrity Monitor logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Integrity Monitor produces file and registry integrity monitoring events in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser first extracts fields like "computer_name", "process_path", and "change_type" from the "message" field of Tanium Integrity Monitor JSON logs using pattern matching. Then, it structures these extracted fields and some directly parsed JSON fields into the unified data model (UDM) format, handling both single-value and multi-value fields.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to
Tanium Console
with Integrity Monitor and Connect modules installed
Privileged access to
AWS
(S3, IAM)
Collect Tanium Integrity Monitor prerequisites
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
Integrity Monitor Service Account
role.
Connect User
role privilege.
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
tanium-integrity-monitor-logs
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
Integrity Monitor to S3 for SecOps
).
Description
: Optional description (for example,
Export IM events to AWS S3 for Google SecOps ingestion
).
Enable
: Select to enable the connection to run on schedule.
Click
Next
.
Configure the connection source
Select
Integrity Monitor Events
as the source type.
Provide the following configuration details:
Source
: Select
Integrity Monitor - Monitor Events
.
Service Account
: The connection will use the Tanium Connect service account configured in Integrity Monitor settings.
Monitor
: Select
All Monitors
or choose specific monitors to export.
Event types
: Select event types to include:
File events
: Include file creation, modification, deletion events.
Registry events
: Include registry key changes (Windows only).
Permission events
: Include file permission changes.
Include labeled events
: Select to include events with labels.
Include unlabeled events
: Select to include events without labels.
Click
Next
.
Configure AWS S3 destination
Select
AWS S3
as the destination type.
Provide the following configuration details:
Destination name
: Enter a unique name (for example,
Google SecOps S3 Destination
).
AWS Access Key
: Enter the AWS access key from the previous step.
AWS Secret Access Key
: Enter the AWS secret access key from the previous step.
Bucket name
: Enter your S3 bucket name (for example,
tanium-integrity-monitor-logs
).
Region
: Select the AWS region where your S3 bucket is located.
Key prefix
: Enter a prefix for the S3 objects (for example,
tanium/integrity-monitor/
).
Advanced Settings
:
File naming
: Select
Date and time-based naming
.
File format
: Select
JSON Lines
for optimal Google SecOps ingestion.
Compression
: Select
Gzip
to reduce storage costs.
Click
Next
.
Optional: Configure filters
Configure data filters if needed:
New items only
: Select to send only new events since last export.
Event filters
: Add filters based on event attributes if specific filtering is required.
Computer group filters
: Select specific computer groups if needed.
Click
Next
.
Format data for AWS S3
Configure the data format:
Format
: Select
JSON
.
Include headers
: Deselect to avoid headers in JSON output.
Field mappings
: Use default field mappings or customize as needed.
Timestamp format
: Select
ISO 8601
format for consistent time representation.
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
Hourly
for regular data export.
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
Configure a feed in Google SecOps to ingest Tanium Integrity Monitor logs
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
Tanium Integrity Monitor logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Integrity Monitor
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-integrity-monitor-logs/tanium/integrity-monitor/
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
Computer Name
principal.hostname
Directly mapped from the "Computer Name" field in the raw log.
Count
additional.fields.value.string_value
Directly mapped from the "Count" field in the raw log.
CreateNewFile
security_result.category_details
Directly mapped from the "Change Type" field in the raw log when its value is "CreateNewFile".
Hash
target.file.sha256
Directly mapped from the "Hash" field in the raw log.
"No events matched the filters"
security_result.about.labels.value
Directly mapped from the "ID" field in the raw log when its value is "No events matched the filters".
additional.fields.key
Hardcoded to "Count" by the parser.
metadata.event_timestamp
Populated with the
create_time
field from the raw log.
metadata.event_type
Set to "STATUS_UPDATE" by the parser logic when the "principal_hostname" field is successfully extracted.
metadata.log_type
Hardcoded to "TANIUM_INTEGRITY_MONITOR" by the parser.
metadata.product_name
Hardcoded to "Tanium Integrity Monitor" by the parser.
metadata.vendor_name
Hardcoded to "Tanium Integrity Monitor" by the parser.
security_result.about.labels.key
Hardcoded to "ID" by the parser.
Need more help?
Get answers from Community members and Google SecOps professionals.
