# Collect AWS Session Manager logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-session-manager/  
**Scraped:** 2026-03-05T09:19:54.369957Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Session Manager logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Session Manager logs to Google Security Operations. AWS Session Manager provides secure and auditable access to Amazon EC2 instances and on-premises servers. By integrating its logs into Google SecOps, you can enhance your security posture and track remote access events.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure AWS IAM and S3
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
Save the bucket
Name
and
Region
for later use.
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
.
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
How to configure AWS Session Manager to Save Logs in S3
Go to the
AWS Systems Manager console
.
In the navigation pane, select
Session Manager
.
Click the
Preferences
tab.
Click
Edit
.
Under S3 logging, select the
Enable
checkbox.
Deselect the
Allow only encrypted S3 buckets
checkbox.
Select an Amazon S3 bucket that has already been created in your account to store session log data.
Enter the name of an Amazon S3 bucket that has already been created in your account to store session log data.
Click
Save
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the AWS Session Manager feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Session Manager
log type.
Specify the values in the following fields.
Source Type
: Amazon SQS V2
Queue Name
: The SQS queue name to read from
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
SQS Queue Access Key ID
: An account access key that is a 20-character alphanumeric string.
SQS Queue Secret Access Key
: An account access key that is a 40-character alphanumeric string.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
--cid
metadata.description
Part of the description field when present in the log
--collector.filesystem.ignored-mount-points
metadata.description
Part of the description field when present in the log
--collector.vmstat.fields
metadata.description
Part of the description field when present in the log
--message-log
metadata.description
Part of the description field when present in the log
--name
metadata.description
Part of the description field when present in the log
--net
metadata.description
Part of the description field when present in the log
--path.procfs
metadata.description
Part of the description field when present in the log
--path.rootfs
metadata.description
Part of the description field when present in the log
--path.sysfs
metadata.description
Part of the description field when present in the log
-v /:/rootfs:ro
metadata.description
Part of the description field when present in the log
-v /proc:/host/proc
metadata.description
Part of the description field when present in the log
-v /sys:/host/sys
metadata.description
Part of the description field when present in the log
CID
metadata.description
Part of the description field when present in the log
ERROR
security_result.severity
Extracted from the log message using grok pattern matching.
falconctl
metadata.description
Part of the description field when present in the log
ip-1-2-4-2
principal.ip
Extracted from the log message using grok pattern matching and converted to a standard IP address format.
ip-1-2-8-6
principal.ip
Extracted from the log message using grok pattern matching and converted to a standard IP address format.
java
target.process.command_line
Extracted from the log message using grok pattern matching.
Jun13
metadata.event_timestamp.seconds
Part of the timestamp field when present in the log, combined with month_date and time_stamp fields.
[kworker/u16:8-kverityd]
target.process.command_line
Extracted from the log message using grok pattern matching.
root
principal.user.userid
Extracted from the log message using grok pattern matching.
metadata.event_type
Determined based on the presence and values of other fields:
- "STATUS_UPDATE" if src_ip is present.
- "NETWORK_CONNECTION" if both src_ip and dest_ip are present.
- "USER_UNCATEGORIZED" if user_id is present.
- "GENERIC_EVENT" otherwise.
metadata.log_type
Set to "AWS_SESSION_MANAGER".
metadata.product_name
Set to "AWS Session Manager".
metadata.vendor_name
Set to "Amazon".
target.process.pid
Extracted from the log message using grok pattern matching.
Need more help?
Get answers from Community members and Google SecOps professionals.
