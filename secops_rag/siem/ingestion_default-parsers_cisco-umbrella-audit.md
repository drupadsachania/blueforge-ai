# Collect Cisco Umbrella audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-umbrella-audit/  
**Scraped:** 2026-03-05T09:21:48.796479Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Umbrella audit logs
Supported in:
Google secops
SIEM
This document explains how to collect Cisco Umbrella audit logs to a Google Security Operations feed using AWS S3 bucket. The parser normalizes the raw CSV log data, handling different delimiters and potential formatting inconsistencies. Then, based on the log type (DNS or Audit), it maps the extracted fields to the corresponding UDM schema, enriching the data with additional context and standardizing the representation for further analysis.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you privileged access to AWS IAM and S3.
Ensure that you have privileged access to Cisco Umbrella.
Configure a Cisco-managed Amazon S3 bucket
Sign in to the
Cisco Umbrella
dashboard.
Go to
Admin
>
Log management
.
Select
Use a Cisco-managed Amazon S3 bucket
option.
Provide the following configuration details:
Select a region
: select a region closer to your location for lower latency.
Select a retention duration
: select the time period. The retention duration is 7, 14, or 30 days. After the selected time period, data is deleted and cannot be recovered. If your ingestion cycle is regular, use a shorter time period. You can change the retention duration at a later time.
Click
Save
.
Click
Continue
to confirm your selections and to receive activation notification.
In the
Activation complete
window that appears, the
Access key
and
Secret key
values are displayed.
Copy the
Access key
and
Secret key
values. If you lose these keys, you must regenerate them.
Click
Got it
>
Continue
.
A summary page displays the configuration and your bucket name. You can turn logging off or on as required by your organization. However, logs are purged based on the retention duration, regardless of new data getting added.
Optional: Configure user access keys for self-managed AWS S3 bucket
Sign in to the
AWS Management Console
.
Create a
User
following this user guide:
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
Optional: Configure a self-managed Amazon S3 bucket
Sign in to the
AWS Management Console
.
Go to
S3
.
Click
Create bucket
.
Provide the following configuration details:
Bucket name
: provide a name for the Amazon S3 bucket.
Region
: select a region.
Click
Create
.
Optional: Configure a bucket policy for self-managed AWS S3 bucket
Click the newly created bucket to open it.
Select
Properties
>
Permissions
.
In the
Permissions
list, click
Add bucket policy
.
Enter the preconfigured bucket policy as follows:
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
/*"
    },
    {
      "Sid": "",
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
/*"},
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:GetBucketLocation",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
"
    },
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::568526795995:user/logs"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::
BUCKET_NAME
"
    }
  ]
}
Replace
BUCKET_NAME
with the Amazon S3 bucket name you provided.
Click
Save
.
Optional: Required Verification for self-managed Amazon S3 bucket
In the
Cisco Umbrella
dashboard, select
Admin
>
Log management
>
Amazon S3
.
In the
Bucket name
field, specify your exact Amazon S3 bucket name, and then click
Verify
.
As part of the verification process, a file named
README_FROM_UMBRELLA.txt
is uploaded from Cisco Umbrella to your Amazon S3 bucket. You may need to refresh your browser in order to see the readme file when it is uploaded.
Download the
README_FROM_UMBRELLA.txt
file, and open it using a text editor.
Copy and save the unique
Cisco Umbrella
token from the file.
Go to the
Cisco Umbrella
dashboard.
In the
Token number
field, specify the token and click
Save
.
If successful, you get a confirmation message in your dashboard indicating that the bucket was successfully verified. If you receive an error indicating that your bucket can't be verified, re-check the syntax of the bucket name and review the configuration.
Configure a feed in Google SecOps to ingest the Cisco Umbrella Audit logs
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed; for example,
Cisco Umbrella Audit Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select
Cisco Umbrella Audit
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: the bucket URI.
s3:/BUCKET_NAME
Replace
BUCKET_NAME
with the actual name of the bucket.
Source deletion options
: select deletion option according to your preference.
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
action_type
security_result.action_details
Directly mapped from the raw log field
action_type
.
action_type
security_result.action
If
action_type
contains
allow
(case-insensitive), set to
ALLOW
. If
action_type
contains
block
(case-insensitive), set to
BLOCK
.
additionalValue
additional.fields{}.key
Set to
Additional Value
.
additionalValue
additional.fields{}.value.string_value
Directly mapped from the raw log field
additionalValue
.
blocked_categories
additional.fields{}.key
Set to
blocked_categories
.
blocked_categories
additional.fields{}.value.string_value
Directly mapped from the raw log field
blocked_categories
.
categories
security_result.category_details
Directly mapped from the raw log field
categories
, after being split by comma.
column1
metadata.product_log_id
Mapped from the raw log field
column1
if the log is an audit log.
column1
date_time
Mapped from the raw log field
column1
if the log is a DNS log.
column10
categories
Directly mapped from the raw log field
column10
.
column11
most_granular_identity_type
Directly mapped from the raw log field
column11
.
column12
identity_types
Directly mapped from the raw log field
column12
.
column13
blocked_categories
Directly mapped from the raw log field
column13
.
column2
date_time
Mapped from the raw log field
column2
if the log is an audit log.
column2
most_granular_identity
Mapped from the raw log field
column2
if the log is a DNS log.
column3
principal.user.email_addresses
Mapped from the raw log field
column3
if the log is an audit log.
column3
identities
Mapped from the raw log field
column3
if the log is a DNS log.
column4
principal.user.userid
Mapped from the raw log field
column4
if the log is an audit log.
column4
internal_ip
Mapped from the raw log field
column4
if the log is a DNS log.
column5
security_result.rule_name
Mapped from the raw log field
column5
if the log is an audit log.
column5
external_ip
Mapped from the raw log field
column5
if the log is a DNS log.
column6
action_type
Directly mapped from the raw log field
column6
.
column7
principal.ip
Mapped from the raw log field
column7
if the log is an audit log.
column7
dns_query_type
Mapped from the raw log field
column7
if the log is a DNS log.
column8
additionalValue
Mapped from the raw log field
column8
if the log is an audit log.
column8
dns_response_code
Mapped from the raw log field
column8
if the log is a DNS log.
column9
domain
Directly mapped from the raw log field
column9
.
date_time
metadata.event_timestamp.seconds
The epoch timestamp extracted from the
date_time
field.
dns_query_type
network.dns.questions.type
Extracted from the
dns_query_type
field using a regular expression, converted to integer.
dns_response_code
network.dns.response_code
Mapped from the
dns_response_code
field, converted to integer based on DNS response code values.
domain
network.dns.questions.name
Directly mapped from the
domain
field.
external_ip
principal.ip
Mapped from the
external_ip
field if it's not empty and different from
internal_ip
.
identities
principal.location.name
Mapped from the
identities
field if the corresponding
identity_types
field is
Networks
.
identities
principal.hostname
Mapped from the
identities
field if the corresponding
identity_types
field is
AD Computers
,
Roaming Computers
, or
Anyconnect Roaming Client
.
identities
principal.asset.hostname
Mapped from the
identities
field if the corresponding
identity_types
field is
AD Computers
,
Roaming Computers
, or
Anyconnect Roaming Client
.
identities
principal.location.city
Mapped from the
identities
field if the corresponding
identity_types
field is
Sites
.
identity_types
additional.fields{}.key
Set to
identities_types
.
identity_types
additional.fields{}.value.string_value
Directly mapped from the raw log field
identity_types
.
internal_ip
principal.ip
Mapped from the
internal_ip
field if it's not empty.
most_granular_identity
additional.fields{}.key
Set to
most_granular_identity
.
most_granular_identity
additional.fields{}.value.string_value
Directly mapped from the raw log field
most_granular_identity
.
most_granular_identity_type
additional.fields{}.key
Set to
most_granular_identity_type
.
most_granular_identity_type
additional.fields{}.value.string_value
Directly mapped from the raw log field
most_granular_identity_type
.
metadata.event_type
Set to
NETWORK_DNS
if the log is a DNS log.
metadata.event_type
Set to
STATUS_UPDATE
if the log is an audit log and
principal_ip
is not empty.
metadata.event_type
Set to
GENERIC_EVENT
if the log is an audit log and
principal_ip
is empty.
metadata.vendor_name
Set to
CISCO UMBERLLA
.
metadata.product_name
Set to
CISCO UMBERLLA
.
metadata.log_type
Set to
AUDITD
.
network.application_protocol
Set to
DNS
if the log is a DNS log.
Need more help?
Get answers from Community members and Google SecOps professionals.
