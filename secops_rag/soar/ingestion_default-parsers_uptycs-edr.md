# Collect Uptycs EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uptycs-edr/  
**Scraped:** 2026-03-05T10:01:52.505212Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Uptycs EDR logs
Supported in:
Google secops
SIEM
This document explains how you can ingest Uptycs EDR logs to Google Security Operations using Amazon S3. The parser transforms raw JSON logs into a unified data model (UDM). It first extracts fields from the JSON, performs data cleaning and enrichment, then maps the relevant information to corresponding UDM fields, handling various data types and edge cases to ensure accurate and consistent representation within the UDM schema.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to
Uptycs
Privileged access to
AWS
(S3, IAM)
Get Uptycs prerequisites
Sign in to the
Uptycs Admin Console
.
Go to
Configuration
>
Users
.
Select your user or create a service account user.
Click
User API key
.
Copy and save in a secure location the following details:
API Key
API Secret
Customer ID
API Domain
(derived from your Uptycs URL, for example,
mystack.uptycs.io
)
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save bucket
Name
and
Region
for future reference (for example,
uptycs-telemetry-export
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
Optional: Add a description tag.
Click
Create access key
.
Click
Download CSV file
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
Configure the IAM policy and role for S3 uploads
In the
AWS console
, go to
IAM
>
Policies
.
Click
Create policy
>
JSON tab
.
Enter the following policy:
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Sid"
:
"AllowPutObjects"
,
"Effect"
:
"Allow"
,
"Action"
:
"s3:PutObject"
,
"Resource"
:
"arn:aws:s3:::uptycs-telemetry-export/*"
},
{
"Sid"
:
"AllowListBucket"
,
"Effect"
:
"Allow"
,
"Action"
:
"s3:ListBucket"
,
"Resource"
:
"arn:aws:s3:::uptycs-telemetry-export"
}
]
}
Replace
uptycs-telemetry-export
if you entered a different bucket name.
Click
Next
>
Create policy
.
Name the policy
uptycs-s3-write-policy
.
Go to
IAM
>
Users
.
Select the user created for Uptycs exports.
Click
Add permissions
>
Attach policies directly
.
Search for and select
uptycs-s3-write-policy
.
Click
Next
>
Add permissions
.
Configure Uptycs Export Raw Telemetry
Sign in to the
Uptycs Console
.
Go to the export configuration section.
Configure the S3 export destination.
Provide the following configuration details:
Export Type
: Select
Raw Telemetry
.
Destination
: Select
Amazon S3
.
Format
: Select
JSON
.
S3 Bucket
: Enter
uptycs-telemetry-export
.
S3 Path Prefix
: Enter
telemetry/
.
AWS Region
: Select your bucket region.
AWS Access Key ID
: Enter the Access Key from the IAM user.
AWS Secret Access Key
: Enter the Secret Access Key.
Event Types
: Select all required telemetry types.
Test and enable the export.
Create read-only IAM user for Google SecOps
Go to
AWS Console
>
IAM
>
Users
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
"arn:aws:s3:::uptycs-telemetry-export/*"
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
"arn:aws:s3:::uptycs-telemetry-export"
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
Configure a feed in Google SecOps to ingest Uptycs logs
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
Uptycs EDR logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Uptycs EDR
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://uptycs-telemetry-export/telemetry/
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
osquery_raw_data.answer
read_only_udm.network.dns.answers.name
Value taken from osquery_raw_data.answer if osquery_raw_data.answer is not empty.
osquery_raw_data.container_id
read_only_udm.metadata.product_log_id
Value taken from osquery_raw_data.container_id if osquery_raw_data.container_id is not empty.
osquery_raw_data.local_address
read_only_udm.principal.ip
Value taken from osquery_raw_data.local_address if osquery_raw_data.local_address is not empty and is a valid IP address.
osquery_raw_data.local
read_only_udm.principal.ip
Otherwise, value taken from osquery_raw_data.local if osquery_raw_data.local is not empty and is a valid IP address.
osquery_raw_data.local_port
read_only_udm.principal.port
Value taken from osquery_raw_data.local_port and converted to integer if osquery_raw_data.local_port is not empty.
osquery_raw_data.md5
read_only_udm.target.process.file.md5
Value taken from osquery_raw_data.md5 if osquery_raw_data.md5 is not empty.
osquery_raw_data.port
read_only_udm.target.port
Value taken from osquery_raw_data.port and converted to integer if osquery_raw_data.port is not empty.
osquery_raw_data.question
read_only_udm.network.dns.questions.name
Value taken from osquery_raw_data.question if osquery_raw_data.question is not empty.
osquery_raw_data.remote_address
read_only_udm.intermediary.ip
Value taken from osquery_raw_data.remote_address if osquery_raw_data.remote_address is not empty.
osquery_raw_data.remote_port
read_only_udm.intermediary.port
Value taken from osquery_raw_data.remote_port and converted to integer if osquery_raw_data.remote_port is not empty.
osquery_raw_data.type
read_only_udm.network.dns.questions.type
Value taken from osquery_raw_data.type and converted to integer if osquery_raw_data.type is not empty.
osquery_raw_data.uid
read_only_udm.principal.user.userid
Value taken from osquery_raw_data.uid if osquery_raw_data.uid is not empty and not equal to "0".
osquery_raw_data.worker_instance_id
read_only_udm.principal.user.userid
Otherwise, value taken from osquery_raw_data.worker_instance_id if osquery_raw_data.worker_instance_id is not empty.
upt_asset_group_id
read_only_udm.principal.user.group_identifiers
Value taken from upt_asset_group_id if upt_asset_group_id is not empty.
upt_asset_group_name
read_only_udm.principal.group.group_display_name
Value taken from upt_asset_group_name if upt_asset_group_name is not empty.
upt_asset_id
read_only_udm.principal.asset.asset_id
Concatenated string "UPT ASSET ID:" with the value of upt_asset_id if upt_asset_id is not empty.
upt_hash
read_only_udm.target.file.md5
All occurrences of "-" are replaced with "" in upt_hash. Then the value is assigned to read_only_udm.target.file.md5 if upt_hash is not empty.
upt_hostname
read_only_udm.principal.hostname
Value taken from upt_hostname if upt_hostname is not empty.
upt_resource_type
read_only_udm.target.resource.type
Value taken from upt_resource_type if upt_resource_type is not empty.
upt_time
read_only_udm.metadata.event_timestamp.seconds
Value taken from upt_time if upt_time is not empty.
read_only_udm.metadata.event_type
Value is set to "PROCESS_LAUNCH" if osquery_raw_data.pid is not empty. Value is set to "NETWORK_DNS" if osquery_raw_data.question is not empty. Value is set to "GENERIC_EVENT" if event_type is empty.
read_only_udm.metadata.log_type
Value is set to "UPTYCS_EDR".
read_only_udm.metadata.product_name
Value is set to "UPTYCS_EDR".
read_only_udm.metadata.vendor_name
Value is set to "UPTYCS".
read_only_udm.network.application_protocol
Value is set to "DNS" if osquery_raw_data.question is not empty.
read_only_udm.security_result.action
Value is set to "ALLOW" if osquery_raw_data.return_code is equal to "SUCCESS" or osquery_raw_data.success is equal to "1".
read_only_udm.target.process.command_line
Value taken from osquery_raw_data.cmdline if osquery_raw_data.cmdline is not empty.
read_only_udm.target.process.file.full_path
Value taken from osquery_raw_data.path if osquery_raw_data.path is not empty.
read_only_udm.target.process.parent_process
The value is constructed by iterating over the ancestor_list array in osquery_raw_data.ancestor_list. For each element in the array, the command_line, full_path of the file, and pid are extracted and formatted into a JSON structure representing the process chain.
read_only_udm.target.process.pid
Value taken from osquery_raw_data.pid if osquery_raw_data.pid is not empty.
Need more help?
Get answers from Community members and Google SecOps professionals.
