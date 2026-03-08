# Collect Carbon Black EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-edr/  
**Scraped:** 2026-03-05T09:51:47.612038Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Carbon Black EDR logs
Supported in:
Google secops
SIEM
This document explains how to collect Carbon Black EDR logs from Cloud and on-premises environments using AWS S3. The parser extracts fields from JSON, CSV, or syslog formatted messages, normalizes them, and maps them to the UDM. It handles various Carbon Black event types, including network connections, process events, file modifications, registry changes, and IOC hits, enriching the data with threat intelligence and device information where available.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to AWS IAM and S3.
Privileged access to Cloud or on-premises Carbon Black EDR.
Configure Carbon Black EDR on-premises
Configure Amazon S3 bucket for on-premises
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
Install cb-event-forwarder on on-premises EDR Server
Install the
CbOpenSource
repository if it isn't already present:
cd
/etc/yum.repos.d
curl
-O
https://opensource.carbonblack.com/release/x86_64/CbOpenSource.repo
Install the
RPM
using
YUM
:
yum
install
cb-event-forwarder
If you're using EDR 7.1.0 or greater, run the following script to
set the appropriate permissions
needed by EDR:
/usr/share/cb/integrations/event-forwarder/cb-edr-fix-permissions.sh
Configure cb-event-forwarder to Output JSON Logs
Open the configuration file:
sudo
nano
/etc/cb/integrations/event-forwarder/cb-event-forwarder.conf
Modify the following parameters:
[event_forwarder]
output_format
=
json
# Enable JSON format
output_type
=
s3
# Send logs to AWS S3
s3_bucket_name
=
YOUR-S3-BUCKET-NAME
s3_region
=
YOUR-S3-BUCKET-NAME
s3_access_key_id
=
YOUR_AWS_ACCESS_KEY
s3_secret_access_key
=
YOUR_AWS_SECRET_KEY
s3_prefix
=
carbonblack/edr/logs
Save and exit using the keyboard:
Ctrl + X, then Y and Enter.
Start cb-event-forwarder:
sudo
systemctl
enable
cb-event-forwarder
sudo
systemctl
restart
cb-event-forwarder
sudo
systemctl
status
cb-event-forwarder
Configure Carbon Black Cloud Event Forwarder for S3
Create an AWS S3 Bucket
Sign in to the AWS Management Console.
Ensure that the AWS region matches the region of the Event Forwarder:
In the
AWS Console
page, locate the region.
Use the drop-down to select the correct region of your Event Forwarder.
The following list gives the applicable AWS Region for each Carbon Black EDR URL.
"instance-alias".my.carbonblack.io - Region:
US East (N. Virginia)
(us-east-1)
"instance-alias".my.cbcloud.de - Region:
Europe (Frankfurt)
(eu-central-1)
"instance-alias".my.cbcloud.sg Region:
Asia Pacific (Singapore)
(ap-southeast-1)
Select
Services
.
Go to the
S3
console.
Click
Create bucket
to open the
Create bucket
wizard.
In
Bucket name
, enter a unique name for your bucket (for example,
CB-EDR
).
Ensure the
Region
defaults to the one you selected earlier.
Update the
Block Public Access
defaults to allow public access (this is required for ingesting the logs into Google SecOps).
Select
Create Bucket
.
Configure S3 Bucket to allow the Event Forwarder to write events
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
Search for the
AmazonS3FullAccess
policy.
Select the policy.
Click
Next
.
Click
Add permissions
.
Configure Events forwarding in the EDR Console
Sign in to VMware Carbon Black Cloud.
Go to the
event forwarder
tab
Enable the events you would like the product to upload to S3.
Go to
Output and Type
and set to
S3
.
Provide the S3 bucket name in the following format
<region>:<bucket-name>
(for example,
us-east-1:cb-edr
).
Select
upload AWS credentials
file in INI format.
The following is an example of a profile:
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Click
Save
and restart the service for the changes to take effect.
Set up feeds
To configure a feed, follow these steps:
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
In the
Feed name
field, enter a name for the feed (for example,
Carbon Black EDR Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Carbon Black EDR
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
: select the deletion option according to your preference.
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
security_result.detection_fields[?key == 'action'].value
The value of the
action
field from the raw log.
cb_server
intermediary.hostname
The value of the
cb_server
field from the raw log.
cb_version
metadata.product_version
The value of the
cb_version
field from the raw log.
child_pid
target.process.pid
(for
ingress.event.childproc
events)
The value of the
child_pid
field from the raw log when the
type
is
ingress.event.childproc
.
child_process_guid
target.process.product_specific_process_id
(for
ingress.event.childproc
events)
"CB:" concatenated with the value of the
child_process_guid
field from the raw log when the
type
is
ingress.event.childproc
.
child_username
target.user.userid
(for
ingress.event.childproc
events)
The value of the
child_username
field from the raw log when the
type
is
ingress.event.childproc
.
childproc_guid
target.process.product_specific_process_id
(for
endpoint.event.procstart
events)
"CB:" concatenated with the value of the
childproc_guid
field from the raw log when the
type
is
endpoint.event.procstart
.
childproc_hash.0
target.process.file.md5
(for
endpoint.event.procstart
events)
The first element of the
childproc_hash
array from the raw log when the
type
is
endpoint.event.procstart
.
childproc_hash.1
target.process.file.sha256
(for
endpoint.event.procstart
events)
The second element of the
childproc_hash
array from the raw log when the
type
is
endpoint.event.procstart
.
childproc_name
target.process.file.full_path
(for
endpoint.event.procstart
events)
The value of the
childproc_name
field from the raw log when the
type
is
endpoint.event.procstart
.
childproc_pid
target.process.pid
(for
endpoint.event.procstart
events)
The value of the
childproc_pid
field from the raw log when the
type
is
endpoint.event.procstart
.
childproc_publisher.0.name
security_result.detection_fields[?key == 'childproc_publisher_name'].value
(for
endpoint.event.procstart
events)
"childproc_publisher_name:" concatenated with the value of
childproc_publisher.0.name
from the raw log when the
type
is
endpoint.event.procstart
.
childproc_publisher.0.state
security_result.detection_fields[?key == 'childproc_publisher_state'].value
(for
endpoint.event.procstart
events)
"childproc_publisher_state:" concatenated with the value of
childproc_publisher.0.state
from the raw log when the
type
is
endpoint.event.procstart
.
childproc_reputation
security_result.detection_fields[?key == 'childproc_reputation'].value
(for
endpoint.event.procstart
events)
The value of the
childproc_reputation
field from the raw log when the
type
is
endpoint.event.procstart
.
childproc_username
target.user.userid
(for
endpoint.event.procstart
events)
The value of the
childproc_username
field from the raw log when the
type
is
endpoint.event.procstart
.
clientIp
principal.ip
,
principal.asset.ip
The value of the
clientIp
field from the raw log.
cmdline
target.process.command_line
(for
feed.query.hit.process
and
feed.storage.hit.process
events),
additional.fields[?key == 'cmdline_*'].value.string_value
(for
watchlist.storage.hit.process
events)
The value of the
cmdline
field from the raw log when the
type
is
feed.query.hit.process
or
feed.storage.hit.process
. For
watchlist.storage.hit.process
events, it's stored in
additional.fields
with the key "cmdline_*".
command_line
target.process.command_line
(for
ingress.event.procstart
events)
The value of the
command_line
field from the raw log when the
type
is
ingress.event.procstart
.
comms_ip
intermediary.ip
The value of the
comms_ip
field from the raw log.
computer_name
principal.hostname
,
principal.asset.hostname
The value of the
computer_name
field from the raw log.
crossproc_api
additional.fields[?key == 'crossproc_api'].value.string_value
(for
endpoint.event.apicall
events)
The value of the
crossproc_api
field from the raw log when the
type
is
endpoint.event.apicall
.
crossproc_guid
additional.fields[?key == 'crossproc_guid'].value.string_value
(for
endpoint.event.crossproc
events)
The value of the
crossproc_guid
field from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_hash.0
additional.fields[?key == 'crossproc_md5'].value.string_value
(for
endpoint.event.crossproc
events)
The first element of the
crossproc_hash
array from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_hash.1
additional.fields[?key == 'crossproc_sha256'].value.string_value
(for
endpoint.event.crossproc
events)
The second element of the
crossproc_hash
array from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_name
target.process.file.full_path
(for
endpoint.event.crossproc
events)
The value of the
crossproc_name
field from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_publisher.0.name
security_result.detection_fields[?key == 'crossproc_publisher_name'].value
(for
endpoint.event.crossproc
events)
"crossproc_publisher_name:" concatenated with the value of
crossproc_publisher.0.name
from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_publisher.0.state
security_result.detection_fields[?key == 'crossproc_publisher_state'].value
(for
endpoint.event.crossproc
events)
"crossproc_publisher_state:" concatenated with the value of
crossproc_publisher.0.state
from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_reputation
additional.fields[?key == 'crossproc_reputation'].value.string_value
(for
endpoint.event.crossproc
events)
The value of the
crossproc_reputation
field from the raw log when the
type
is
endpoint.event.crossproc
.
crossproc_target
additional.fields[?key == 'crossproc_target'].value.string_value
(for
endpoint.event.crossproc
events)
The value of the
crossproc_target
field from the raw log when the
type
is
endpoint.event.crossproc
. Converted to a string "true" or "false".
Need more help?
Get answers from Community members and Google SecOps professionals.
