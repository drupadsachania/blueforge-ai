# Collect Forcepoint Mail Relay logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay/  
**Scraped:** 2026-03-05T09:56:00.656346Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forcepoint Mail Relay logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forcepoint Mail Relay logs to Google Security Operations using Amazon S3.
Forcepoint Mail Relay is a cloud-based email security solution that protects organizations from email-borne threats including spam, phishing, malware, and data loss. The solution provides comprehensive email filtering, data loss prevention (DLP), encryption, and advanced threat protection for both inbound and outbound email traffic.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
Privileged access to
Forcepoint Mail Relay Cloud
portal
Privileged access to
AWS
(S3, IAM)
Log Export
permission enabled for your Forcepoint administrator account
Configure Forcepoint Mail Relay Cloud SIEM storage
To configure Forcepoint Mail Relay Cloud to export logs to your AWS S3 bucket, do the following:
Create one or more AWS S3 buckets on the AWS portal.
Sign in to the
Forcepoint Cloud Security Gateway Portal
.
Go to
Account
>
SIEM Storage
.
In the
Storage type
section, select the
Bring your own storage
radio button.
Click
Add
to add your bucket to the
Storage List: Bring Your Own
table.
In the
Add Bucket
dialog, enter the following:
Bucket name
: Enter the bucket name from the AWS portal (for example,
forcepoint-email-logs
).
Prefix
(optional): Enter a prefix to organize log files. Use
/
to create a folder (for example,
email-logs/
). If no
/
is included, the prefix is prepended to the filename.
Click
Save
. The bucket information is added to the table.
In the
Storage List: Bring Your Own
table, click the
JSON
link in the row for the bucket you just added.
On the
Bucket Policy
page, click
Copy Text
to copy the contents of the JSON pane to a clipboard.
In the
AWS Management Console
, open the
S3
service.
Select your bucket (for example,
forcepoint-email-logs
).
Go to
Permissions
>
Bucket policy
.
Click
Edit
.
Paste the JSON policy copied from the Forcepoint portal.
Click
Save changes
.
Return to the Forcepoint portal
SIEM Storage
page.
In the
Storage List: Bring Your Own
table, click
Check connection
for your bucket.
After the connection test succeeds, select the
Active
radio button for your bucket in the
Storage List: Bring Your Own
table.
Click
Save
at the bottom of the page.
Enable SIEM logging and configure export format
In the Forcepoint portal, go to
Reporting
>
Account Reports
>
SIEM Integration
.
From the
Data type
list, select
Email Security
.
Set the
Enable data export
toggle to
ON
.
From the
Attributes
section on the left, drag the following attributes into the
Columns
section:
Direction
From: Address
Policy
Recipient Address
Recipient Domain
Sender Domain
Sender Name
Subject
Action
Black/Whitelisted
Blocked Attachment Ext
Filtering Reason
Sender IP
Sender IP Country
Attachment File Type
Attachment Filename
Emb. URL Risk Class
Emb. URL Severity
Advanced Encryption
File Sandbox status
Virus Name
Date & Time
Message Size
Spam score
Attachment Size
Click
Save
.
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
forcepoint-email-logs
).
Create a
User
following this user guide:
Creating an IAM user
.
Select the created
User
.
Select
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
Optional: Add description tag.
Click
Create access key
.
Click
Download .csv file
to save the
Access Key
and
Secret Access Key
for future reference.
Click
Done
.
Select
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
Configure a feed in Google SecOps to ingest Forcepoint Mail Relay logs
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
Enter a unique name for the
Feed name
.
Select
Amazon S3 V2
as the
Source type
.
Select
Forcepoint Mail Relay
as the
Log type
.
Click
Next
and then click
Submit
.
Specify values for the following fields:
S3 URI
:
s3://forcepoint-email-logs/email-logs/
.
Source deletion option
: Select the deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days (default is 180 days).
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
and then click
Submit
.
UDM mapping table
Log field
UDM mapping
Logic
hybridSpamScore_label.key
Set to "hybridSpamScore"
hybridSpamScore
hybridSpamScore_label.value
Value copied directly
localSpamScore_label.key
Set to "localSpamScore"
localSpamScore
localSpamScore_label.value
Value copied directly
metadata.event_type
Set to "GENERIC_EVENT" initially; set to "EMAIL_TRANSACTION" if has_network_email is true; else set to "NETWORK_CONNECTION" if has_principal and has_target are true; else set to "STATUS_UPDATE" if has_principal is true; else "GENERIC_EVENT"
product_event_type
metadata.product_event_type
Value copied directly
metadata.product_name
Set to "FORCEPOINT_MAIL_RELAY"
metadata.vendor_name
Set to "FORCEPOINT_MAIL_RELAY"
sender
network.email.from
Value copied directly
subject
network.email.subject
Value copied directly
recipient
network.email.to
Value copied directly
identHostName
principal.asset.hostname
Value copied directly
identSrc, trueSrc, src
principal.asset.ip
Value from src if not empty, else trueSrc if not empty, else identSrc
identHostName
principal.hostname
Value copied directly
identSrc, trueSrc, src
principal.ip
Value from src if not empty, else trueSrc if not empty, else identSrc
sender
principal.user.email_addresses
Value copied directly
summary
security_result.action
Set to "ALLOW" if summary matches (?i)clean
act
security_result.action_details
Value copied directly
hybridSpamScore_label, localSpamScore_label
security_result.detection_fields
Merged from hybridSpamScore_label and localSpamScore_label
summary
security_result.summary
Value copied directly
dst
target.asset.ip
Value copied directly
dst
target.ip
Value copied directly
recipient
target.user.email_addresses
Value copied directly
Need more help?
Get answers from Community members and Google SecOps professionals.
