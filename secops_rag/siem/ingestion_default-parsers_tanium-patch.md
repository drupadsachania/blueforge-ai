# Collect Tanium Patch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-patch/  
**Scraped:** 2026-03-05T09:29:04.623332Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Patch logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Patch logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Patch produces patch deployment, compliance, and vulnerability data in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser transforms the assessment JSON data into Google SecOps's Unified Data Model (UDM). It first normalizes key names, extracts data from the JSON structure, and then maps relevant fields to UDM attributes, including vulnerability details, security result information, and asset details like hostname and operating system.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Tanium Core Platform
7.0 or later
Tanium Patch
module installed and configured
Tanium Connect
module installed with valid license
Privileged access to
Tanium Console
with administrative rights
Privileged access to
AWS
(S3, IAM)
Configure Tanium Patch service account
Sign in to the
Tanium Console
.
Go to
Modules
>
Patch
.
Click
Settings
at the top right.
In the
Service Account
section, configure the following:
Service Account User
: Select a user with appropriate Patch permissions.
Verify
the account has Connect User role privilege.
Click
Save
to apply the service account configuration.
Collect Tanium Patch prerequisites
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
Patch Administrator
or
Patch Read Only User
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
tanium-patch-logs
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
Patch Data to S3 for SecOps
).
Description
: Optional description (for example,
Export Patch compliance and deployment data to AWS S3 for Google SecOps ingestion
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
: Select one of the following Patch-related saved questions:
Patch - Deployment Results
for patch deployment status.
Patch - Missing Patches
for vulnerability compliance data.
Patch - Installed Patches
for installed patch inventory.
Patch - Patch List
for comprehensive patch status.
Computer Group
: Select
All Computers
or specific computer groups to monitor.
Refresh Interval
: Set appropriate interval for data collection (for example,
1 hour
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
Google SecOps Patch S3 Destination
).
AWS Access Key
: Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
AWS Secret Access Key
: Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
Bucket Name
: Enter your S3 bucket name (for example,
tanium-patch-logs
).
Region
: Select the AWS region where your S3 bucket is located.
Key Prefix
: Enter a prefix for the S3 objects (for example,
tanium/patch/
).
Click
Next
.
Configure filters
In the
Filters
section, configure data filtering options:
Send new items only
: Select this option to send only new results since the last export.
Column filters
: Add filters based on specific patch attributes if needed (for example, filter by patch severity, deployment status).
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
Hourly
for regular patch data export.
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
Configure a feed in Google SecOps to ingest Tanium Patch logs
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
Tanium Patch logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Patch
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-patch-logs/tanium/patch/
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
Log field
UDM mapping
Logic
Bulletins
principal.asset.vulnerabilities.vendor_vulnerability_id
The value is taken from the "Bulletins" field in the raw log, for the corresponding index of the "Title" field. If the value is "None", the field is not mapped.
ComputerName
principal.hostname
The value is taken from the "ComputerName" field in the raw log.
ComputerName
principal.asset.hostname
The value is taken from the "ComputerName" field in the raw log.
CVEIDs
principal.asset.vulnerabilities.cve_id
The value is taken from the "CVEIDs" field in the raw log, for the corresponding index of the "Title" field. If the value is "None", the field is not mapped.
KBArticles
principal.asset.vulnerabilities.vendor_knowledge_base_article_id
The value is taken from the "KBArticles" field in the raw log, for the corresponding index of the "Title" field. If the value is empty, the field is not mapped.
KBArticles
security_result.summary
The value is taken from the "KBArticles" field in the raw log, for the corresponding index of the "Title" field. If the value is empty, the field is not mapped.
OSType
principal.asset.platform_software.platform
If the value contains "Windows", the platform is set to "WINDOWS". If the value contains "Linux", the platform is set to "LINUX". If the value contains "Mac", the platform is set to "MAC".
Severity
principal.asset.vulnerabilities.severity
The value is taken from the "Severity" field in the raw log, for the corresponding index of the "Title" field. If the value is "Critical", the severity is set to "HIGH". If the value is "Important", the severity is set to "MEDIUM". Otherwise, the severity is set to "UNKNOWN_SEVERITY".
Severity
principal.asset.vulnerabilities.severity_details
The value is taken from the "Severity" field in the raw log, for the corresponding index of the "Title" field. If the value is "Critical" or "Important", the severity details are set to the raw log value.
Title
principal.asset.vulnerabilities.name
The value is taken from the "Title" field in the raw log.
Title
security_result.description
The value is taken from the "Title" field in the raw log, for the corresponding index of the "InstallStatus" field. If the "InstallStatus" value is not "Installed", the description is set to the raw log value.
-
metadata.event_timestamp
The value is taken from the "create_time" field in the raw log.
-
metadata.event_type
The value is set to "SCAN_HOST".
-
metadata.log_type
The value is taken from the "log_type" field in the raw log.
-
metadata.product_name
The value is set to "Patch".
-
metadata.vendor_name
The value is set to "Tanium".
-
principal.asset.vulnerabilities.vendor
The value is set to "Tanium".
-
security_result.category
The value is set to "DATA_AT_REST".
Need more help?
Get answers from Community members and Google SecOps professionals.
