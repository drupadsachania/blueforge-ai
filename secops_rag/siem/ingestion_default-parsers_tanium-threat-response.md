# Collect Tanium Threat Response logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-threat-response/  
**Scraped:** 2026-03-05T09:29:12.496113Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Threat Response logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Threat Response logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Threat Response produces threat detection alerts, investigation findings, and incident response data in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser transforms raw JSON data from Tanium Threat Response into a unified data model (UDM). It first attempts to parse the incoming message as JSON, handles potential errors, and then extracts and maps relevant fields to the UDM structure, including details about the affected host, user, process, network activity, and security findings.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Tanium Core Platform
7.0 or later
Tanium Threat Response
module installed and configured
Tanium Connect
module installed with valid license
Tanium Direct Connect
1.9.30 or later for investigation capabilities
Privileged access to
Tanium Console
with administrative rights
Privileged access to
AWS
(S3, IAM)
Configure Tanium Threat Response service account
Sign in to the
Tanium Console
.
Go to
Modules
>
Threat Response
.
Click
Settings
at the top right.
In the
Service Account
section, configure the following:
Service Account User
: Select a user with appropriate Threat Response permissions.
Verify
the account has Connect User role privilege.
Confirm
access to Threat Response alerts and investigation data.
Click
Save
to apply the service account configuration.
Collect Tanium Threat Response prerequisites
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
Threat Response Administrator
or
Threat Response Read Only User
role.
Connect User
role privilege.
Access to monitored computer groups (recommended:
All Computers
group).
Read Saved Question
permission for Threat Response content sets.
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
tanium-threat-response-logs
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
Threat Response Alerts to S3 for SecOps
).
Description
: Optional description (for example,
Export threat detection alerts and investigation findings to AWS S3 for Google SecOps ingestion
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
: Select one of the following Threat Response-related saved questions:
Threat Response - Alerts
for threat detection alerts.
Threat Response - Investigation Results
for investigation findings.
Threat Response - Intel Matches
for threat intelligence matches.
Threat Response - Endpoint Activity
for suspicious endpoint activity.
Threat Response - Network Connections
for network-based threats.
Computer Group
: Select
All Computers
or specific computer groups to monitor.
Refresh Interval
: Set appropriate interval for data collection (for example,
10 minutes
for threat alerts).
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
Google SecOps ThreatResponse S3 Destination
).
AWS Access Key
: Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
AWS Secret Access Key
: Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
Bucket Name
: Enter your S3 bucket name (for example,
tanium-threat-response-logs
).
Region
: Select the AWS region where your S3 bucket is located.
Key Prefix
: Enter a prefix for the S3 objects (for example,
tanium/threat-response/
).
Click
Next
.
Configure filters
In the
Filters
section, configure data filtering options:
Send new items only
: Select this option to send only new threat alerts since the last export.
Column filters
: Add filters based on specific alert attributes if needed (for example, filter by alert severity, threat type, or investigation status).
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
Every 10 minutes
for timely threat response alerts.
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
Configure a feed in Google SecOps to ingest Tanium Threat Response logs
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
Tanium Threat Response logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Threat Response
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-threat-response-logs/tanium/threat-response/
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
Alert Id
security_result.rule_instance
The value of this field is taken from the "Alert Id" field in the raw log.
Computer IP
principal.ip
The value of this field is taken from the "Computer IP" field in the raw log.
Computer IP
target.ip
The value of this field is taken from the "Computer IP" field in the raw log.
Computer Name
principal.hostname
The value of this field is taken from the "Computer Name" field in the raw log.
Computer Name
target.hostname
The value of this field is taken from the "Computer Name" field in the raw log.
id
target.resource.attribute.labels
The value of this field is taken from the "id" field in the raw log. The key is hardcoded to "id".
Intel Id
security_result.rule_id
The value of this field is taken from the "Intel Id" field in the raw log.
Intel Labels
security_result.description
The value of this field is taken from the "Intel Labels" field in the raw log.
Intel Name
security_result.summary
The value of this field is taken from the "Intel Name" field in the raw log.
Intel Name
security_result.threat_name
The value of this field is taken from the "Intel Name" field in the raw log.
Intel Type
security_result.rule_type
The value of this field is taken from the "Intel Type" field in the raw log.
MatchDetails.finding.system_info.bits
principal.asset.platform_software.bits
The value of this field is taken from the "MatchDetails.finding.system_info.bits" field in the raw log.
MatchDetails.finding.system_info.os
principal.asset.platform_software.platform_version
The value of this field is taken from the "MatchDetails.finding.system_info.os" field in the raw log.
MatchDetails.finding.system_info.patch_level
principal.asset.platform_software.platform_patch_level
The value of this field is taken from the "MatchDetails.finding.system_info.patch_level" field in the raw log.
MatchDetails.finding.system_info.platform
principal.asset.platform_software.platform
The value of this field is taken from the "MatchDetails.finding.system_info.platform" field in the raw log.
MatchDetails.match.contexts.0.event.registrySet.keyPath
target.registry.registry_key
The value of this field is taken from the "MatchDetails.match.contexts.0.event.registrySet.keyPath" field in the raw log.
MatchDetails.match.contexts.0.event.registrySet.valueName
target.registry.registry_value_name
The value of this field is taken from the "MatchDetails.match.contexts.0.event.registrySet.valueName" field in the raw log.
MatchDetails.match.properties.args
security_result.about.process.command_line
The value of this field is taken from the "MatchDetails.match.properties.args" field in the raw log.
MatchDetails.match.properties.file.fullpath
target.process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.file.fullpath" field in the raw log.
MatchDetails.match.properties.file.md5
target.process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.file.md5" field in the raw log.
MatchDetails.match.properties.file.sha1
target.process.file.sha1
The value of this field is taken from the "MatchDetails.match.properties.file.sha1" field in the raw log.
MatchDetails.match.properties.file.sha256
target.process.file.sha256
The value of this field is taken from the "MatchDetails.match.properties.file.sha256" field in the raw log.
MatchDetails.match.properties.fullpath
target.process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.fullpath" field in the raw log.
MatchDetails.match.properties.local_port
principal.port
The value of this field is taken from the "MatchDetails.match.properties.local_port" field in the raw log.
MatchDetails.match.properties.md5
target.process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.md5" field in the raw log.
MatchDetails.match.properties.parent.args
security_result.about.process.command_line
The value of this field is taken from the "MatchDetails.match.properties.parent.args" field in the raw log.
MatchDetails.match.properties.parent.file.fullpath
target.process.parent_process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.parent.file.fullpath" field in the raw log.
MatchDetails.match.properties.parent.file.md5
target.process.parent_process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.parent.file.md5" field in the raw log.
MatchDetails.match.properties.parent.parent.file.fullpath
target.process.parent_process.parent_process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.file.fullpath" field in the raw log.
MatchDetails.match.properties.parent.parent.file.md5
target.process.parent_process.parent_process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.file.md5" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.file.fullpath
target.process.parent_process.parent_process.parent_process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.file.fullpath" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.file.md5
target.process.parent_process.parent_process.parent_process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.file.md5" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.parent.file.fullpath
target.process.parent_process.parent_process.parent_process.parent_process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.file.fullpath" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.parent.file.md5
target.process.parent_process.parent_process.parent_process.parent_process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.file.md5" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.parent.parent.file.fullpath
target.process.parent_process.parent_process.parent_process.parent_process.parent_process.file.full_path
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.parent.file.fullpath" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.parent.parent.file.md5
target.process.parent_process.parent_process.parent_process.parent_process.parent_process.file.md5
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.parent.file.md5" field in the raw log.
MatchDetails.match.properties.parent.pid
target.process.parent_process.pid
The value of this field is taken from the "MatchDetails.match.properties.parent.pid" field in the raw log.
MatchDetails.match.properties.parent.parent.pid
target.process.parent_process.parent_process.pid
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.pid" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.pid
target.process.parent_process.parent_process.parent_process.pid
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.pid" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.parent.pid
target.process.parent_process.parent_process.parent_process.parent_process.pid
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.pid" field in the raw log.
MatchDetails.match.properties.parent.parent.parent.parent.parent.pid
target.process.parent_process.parent_process.parent_process.parent_process.parent_process.pid
The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.parent.pid" field in the raw log.
MatchDetails.match.properties.pid
target.process.pid
The value of this field is taken from the "MatchDetails.match.properties.pid" field in the raw log.
MatchDetails.match.properties.protocol
network.ip_protocol
The value of this field is taken from the "MatchDetails.match.properties.protocol" field in the raw log.
MatchDetails.match.properties.remote_ip
target.ip
The value of this field is taken from the "MatchDetails.match.properties.remote_ip" field in the raw log.
MatchDetails.match.properties.remote_port
target.port
The value of this field is taken from the "MatchDetails.match.properties.remote_port" field in the raw log.
MatchDetails.match.properties.sha1
target.process.file.sha1
The value of this field is taken from the "MatchDetails.match.properties.sha1" field in the raw log.
MatchDetails.match.properties.sha256
target.process.file.sha256
The value of this field is taken from the "MatchDetails.match.properties.sha256" field in the raw log.
MatchDetails.match.properties.user
target.administrative_domain
The domain name is extracted from the "MatchDetails.match.properties.user" field in the raw log by looking for a backslash character (""). The characters before the backslash are considered as the domain name.
MatchDetails.match.properties.user
target.user.userid
The username is extracted from the "MatchDetails.match.properties.user" field in the raw log by looking for a backslash character (""). The characters after the backslash are considered as the username.
MITRE Techniques
security_result.threat_id
The value of this field is taken from the "MITRE Techniques" field in the raw log.
params
security_result.detection_fields
The value of this field is taken from the "params" field in the raw log. The key is hardcoded to "params_" concatenated with the index of the parameter.
Timestamp
metadata.event_timestamp
The value of this field is taken from the "Timestamp" field in the raw log.
N/A
is_alert
This field is hardcoded to "true" if the "Computer IP" field in the raw log is not empty.
N/A
metadata.log_type
This field is hardcoded to "TANIUM_THREAT_RESPONSE".
N/A
metadata.product_event_type
This field is hardcoded to "Tanium Signal".
N/A
metadata.product_name
This field is hardcoded to "Threat Response".
N/A
metadata.vendor_name
This field is hardcoded to "Tanium".
N/A
network.http.method
This field is hardcoded to "POST" if the value of the "method" field in the raw log is "submit".
Need more help?
Get answers from Community members and Google SecOps professionals.
