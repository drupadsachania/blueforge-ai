# Collect Cisco Umbrella DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-dns/  
**Scraped:** 2026-03-05T09:52:45.313783Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Umbrella DNS logs
Supported in:
Google secops
SIEM
This document explains how to collect Cisco Umbrella DNS logs to a Google Security Operations feed using AWS S3 bucket. The parser handles both JSON and CSV formatted logs. It extracts fields, renames them to match the UDM, handles different log versions and formats (including proxy and IP logs), and performs specific logic for identities, security categories, and network events, ultimately merging the extracted data into the UDM schema.
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
Configure a feed in Google SecOps to ingest the Cisco Umbrella DNS logs
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
Cisco Umbrella DNS Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select
Cisco Umbrella DNS
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: the bucket URI.
s3:/BUCKET_NAME/
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
Log Field
UDM Mapping
Logic
action
security_result.action_details
The value is taken from the
action
field if it exists in the JSON logs, or from
column6
or
column7
in CSV logs, and converted to uppercase (ALLOW or BLOCK).
amp.disposition
security_result.detection_fields[].key
Value is
ampDisposition
.
amp.disposition
security_result.detection_fields[].value
The value is taken from the
amp.disposition
field.
amp.malware
security_result.detection_fields[].key
Value is
ampMalware
.
amp.malware
security_result.detection_fields[].value
The value is taken from the
amp.malware
field.
amp.score
security_result.detection_fields[].key
Value is
ampScore
.
amp.score
security_result.detection_fields[].value
The value is taken from the
amp.score
field.
blocked_categories
security_result.category_details
The value is taken from the
blocked_categories
field.
blockedfiletype
security_result.detection_fields[].key
Value is
egress type
.
blockedfiletype
security_result.detection_fields[].value
The value is taken from the
blockedfiletype
field.
bundleid
additional.fields[].key
Value is
bundleid
.
bundleid
additional.fields[].value.string_value
The value is taken from the
bundleid
field.
categories[]
security_result.category_details
The value is taken from the
categories[].label
field.
column1
metadata.event_timestamp.seconds
The value is parsed from the
column1
field as a timestamp.  For proxy logs, if
date
and
time
fields exist, they are combined and parsed as a timestamp.
column10
network.http.user_agent
The value is taken from the
column10
field.
column10
additional.fields[].value.string_value
The value is taken from the
column10
field.
column11
target.port
The value is taken from the
column11
field.
column12
principal.resource.name
The value is taken from the
column12
field.
column13
security_result.rule_id
The value is taken from the
column13
field.
column14
security_result.action_details
The value is taken from the
column14
field.
column2
principal.user.user_display_name
The value is taken from the
column2
field.
column2
principal.user.userid
The value is taken from the
column2
field.
column2
principal.location.name
The value is taken from the
column2
field.
column3
principal.hostname
The value is taken from the
column3
field.
column3
principal.user.product_object_id
The value is taken from the
column3
field.
column3
principal.location.city
The value is taken from the
column3
field.
column3
additional.fields[].value.string_value
The value is taken from the
column3
field.
column4
principal.asset.ip
The value is taken from the
column4
field.
column4
principal.ip
The value is taken from the
column4
field.
column4
principal.port
The value is taken from the
column4
field.
column5
principal.asset.ip
The value is taken from the
column5
field.
column5
principal.ip
The value is taken from the
column5
field.
column5
target.asset.ip
The value is taken from the
column5
field.
column5
target.ip
The value is taken from the
column5
field.
column6
security_result.action_details
The value is taken from the
column6
field.
column6
target.port
The value is taken from the
column6
field.
column7
network.received_bytes
The value is taken from the
column7
field.
column7
additional.fields[].value.string_value
The value is taken from the
column7
field.
column8
principal.asset.ip
The value is taken from the
column8
field.
column8
principal.ip
The value is taken from the
column8
field.
column8
target.url
The value is taken from the
column8
field.
column9
principal.port
The value is taken from the
column9
field.
column9
network.http.referral_url
The value is taken from the
column9
field.
data_center_name
principal.resource.name
The value is taken from the
data_center_name
field.
datacenter.label
security_result.detection_fields[].key
Value is
datacenter label
.
datacenter.label
security_result.detection_fields[].value
The value is taken from the
datacenter.label
field.
destinationip
target.asset.ip
The value is taken from the
destinationip
field.
destinationip
target.ip
The value is taken from the
destinationip
field.
direction
network.direction
The value is taken from the
direction
field and converted to uppercase.
domain
network.dns.questions[].name
The value is taken from the
domain
field, with the trailing dot removed if present.
dstPort
target.port
The value is taken from the
dstPort
field.
dstip
target.asset.ip
The value is taken from the
dstip
field.
dstip
target.ip
The value is taken from the
dstip
field.
egress.ip
security_result.detection_fields[].key
Value is
egress ip
.
egress.ip
security_result.detection_fields[].value
The value is taken from the
egress.ip
field.
egress.type
security_result.detection_fields[].key
Value is
egress type
.
egress.type
security_result.detection_fields[].value
The value is taken from the
egress.type
field.
externalip
principal.asset.ip
The value is taken from the
externalip
field.
externalip
principal.ip
The value is taken from the
externalip
field.
forwardingmethod
additional.fields[].key
Value is
forwardingmethod
.
forwardingmethod
additional.fields[].value.string_value
The value is taken from the
forwardingmethod
field.
granular_identity
principal.user.user_display_name
The value is taken from the
granular_identity
field if both
granular_identity
and
most_granular_identity
are present.  Otherwise, it's derived from the
_policy_identity
field and further parsed based on
identityType
.
granular_identity
principal.user.email_addresses
The value is extracted from the
granular_identity
field using a regular expression.
granular_identity
principal.user.first_name
The value is extracted from the
granular_identity
field using a regular expression.
granular_identity
principal.user.last_name
The value is extracted from the
granular_identity
field using a regular expression.
granular_identity
principal.user.userid
The value is extracted from the
granular_identity
field using a regular expression.
granular_identity
principal.hostname
The value is taken from the
granular_identity
field.
granular_identity
principal.location.name
The value is taken from the
granular_identity
field.
identity_types
additional.fields[].value.string_value
The value is taken from the
identity_types
field.
identities[]
principal.user.product_object_id
The value is taken from the
identities[]
field.
identities
principal.user.product_object_id
The value is taken from the
identities
field.
internalip
principal.asset.ip
The value is taken from the
internalip
field.
internalip
principal.ip
The value is taken from the
internalip
field.
isolated.fileaction
security_result.detection_fields[].key
Value is
isolated fileaction
.
isolated.fileaction
security_result.detection_fields[].value
The value is taken from the
isolated.fileaction
field.
isolated.state
security_result.detection_fields[].key
Value is
isolated state
.
isolated.state
security_result.detection_fields[].value
The value is taken from the
isolated.state
field.
most_granular_identity
principal.user.identityType
The value is taken from the
most_granular_identity
field if both
granular_identity
and
most_granular_identity
are present. Otherwise, it's taken from the
_policy_identity_type
field.
nat_destination_ip
principal.asset.ip
The value is taken from the
nat_destination_ip
field.
nat_destination_ip
principal.ip
The value is taken from the
nat_destination_ip
field.
odns_categories
security_result.category_details
The value is taken from the
odns_categories
field.
policy.ruleid
security_result.rule_id
The value is taken from the
policy.ruleid
field.
policy.rulesetid
security_result.detection_fields[].key
Value is
rulesetid
.
policy.rulesetid
security_result.detection_fields[].value
The value is taken from the
policy.rulesetid
field.
policy.timebasedrule
security_result.detection_fields[].key
Value is
timebasedrule
.
policy.timebasedrule
security_result.detection_fields[].value
The value is taken from the
policy.timebasedrule
field.
port
target.port
The value is taken from the
port
field.
query_type_name
network.dns.questions[].type
The numeric part is extracted from the
query_type_name
field using a regular expression and converted to an integer.
query_type_name
additional.fields[].value.string_value
The string part within parentheses is extracted from the
query_type_name
field using a regular expression.
querytype
network.dns.questions[].type
The value is taken from the
querytype
field and mapped to a numeric value based on the DNS record type.
referer
network.http.referral_url
The value is taken from the
referer
field.
requestmethod
network.http.method
The value is taken from the
requestmethod
field.
requestsize
network.sent_bytes
The value is taken from the
requestsize
field and converted to an unsigned integer.
response
additional.fields[].value.string_value
The value is taken from the
response
field.
responsecode
network.http.response_code
The value is taken from the
responsecode
field.
responsefilename
target.file.names
The value is taken from the
responsefilename
field.
responsesize
network.received_bytes
The value is taken from the
responsesize
field and converted to an unsigned integer.
returncode
network.dns.response_code
The value is taken from the
returncode
field and converted to an unsigned integer.
securityoverridden
additional.fields[].key
Value is
securityoverridden
.
securityoverridden
additional.fields[].value.string_value
The value is taken from the
securityoverridden
field.
sha256
target.file.sha256
The value is taken from the
sha256
field.
source_ip
principal.asset.ip
The value is taken from the
source_ip
field if it exists in the JSON logs, or from
column3
in CSV logs.
source_ip
principal.ip
The value is taken from the
source_ip
field if it exists in the JSON logs, or from
column3
in CSV logs.
srcPort
principal.port
The value is taken from the
srcPort
field.
statuscode
network.http.response_code
The value is taken from the
statuscode
field.
tenantcontrols
additional.fields[].key
Value is
tenantcontrols
.
tenantcontrols
additional.fields[].value.string_value
The value is taken from the
tenantcontrols
field.
timestamp
metadata.event_timestamp.seconds
The value is parsed from the
timestamp
field as a timestamp.
tunnel_name
additional.fields[].key
Value is
tunnel_name
.
tunnel_name
additional.fields[].value.string_value
The value is taken from the
tunnel_name
field.
tunnel_type
metadata.product_event_type
The value is taken from the
tunnel_type
field.
type
additional.fields[].key
Value is
type
.
type
additional.fields[].value.string_value
The value is taken from the
type
field.
url
target.url
The value is taken from the
url
field.
useragent
network.http.user_agent
The value is taken from the
useragent
field.
verdict
security_result.action_details
The value is taken from the
verdict
field.
warnstatus
security_result.detection_fields[].key
Value is
warnstatus
.
warnstatus
security_result.detection_fields[].value
The value is taken from the
warnstatus
field. Value is
DNS Lookup Type
. The string part within parentheses is extracted from the
query_type_name
field using a regular expression, or it's an empty string if the field is not present. Value is
DNS request and response were made.
Determined based on the presence of certain fields: NETWORK_DNS if
question.name
is present, NETWORK_CONNECTION if both
principal.ip
and
target.ip
are present, STATUS_UPDATE if only
principal.ip
is present, or GENERIC_EVENT otherwise. Value is
UMBRELLA_DNS
. Value is
Umbrella DNS
. Value is
Cisco
. Value is initially set to
DNS
. If
requestmethod
is a valid HTTP method, it's changed to
HTTP
. The numeric part is extracted from the
query_type_name
field using a regular expression and converted to an integer, or it's derived from the
querytype
field and mapped to a numeric value based on the DNS record type. The value is derived from the
useragent
or
column10
field using the
parseduseragent
filter. The value is taken from the last part of the
column3
field after splitting by commas, or it's an empty string if the field is not present. The value is taken from the first part of the
column3
field after splitting by commas, or it's taken from the
column2
field if
column3
is not present. The value is extracted from the
column2
or
column3
field using a regular expression. The value is extracted from the
column2
or
column3
field using a regular expression. The value is extracted from the
column2
or
column3
field using a regular expression. The value is extracted from the
column2
or
column3
field using a regular expression. The value is derived from the
action
,
column6
,
column7
, or
verdict
field and converted to uppercase (ALLOW or BLOCK). Value is set to
NETWORK_MALICIOUS
if
_categories
contains
Malware
, or
NETWORK_SUSPICIOUS
if
_categories
contains
Potentially Harmful
.
Need more help?
Get answers from Community members and Google SecOps professionals.
