# Collect AWS Aurora logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-aurora/  
**Scraped:** 2026-03-05T09:19:35.003015Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Aurora logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Aurora logs to Google Security Operations. AWS Aurora is a managed relational database service that offers high performance, scalability, and availability. In this integration, you will configure AWS Aurora to forward logs to Google SecOps for analysis, monitoring, and threat detection.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
AWS Aurora database cluster set up and running
Configure Amazon S3 bucket
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
Search for and select
AmazonS3FullAccess
and
CloudWatchLogsFullAccess
policies.
Click
Next
.
Click
Add permissions
.
Configure Enhanced Monitoring
Sign in to the
AWS Management Console
.
In the search bar, type
RDS
and select
RDS
from the services list.
In the
RDS Dashboard
, select
Databases
from the navigation pane.
Select the
Aurora cluster
you want to monitor.
Under the
Logs & monitoring
section, click
Modify
.
Go to the
Monitoring
section and enable
Enhanced Monitoring
.
Set the
Monitoring role
to the appropriate IAM role that has permissions to publish to
CloudWatch Logs
or
S3
.
Save the changes and apply them to your Aurora cluster.
How to configure AWS Aurora audit logs
In the
RDS Dashboard
, select
Databases
and click your
Aurora cluster
.
Under the
Logs & Monitoring
section, click
Modify
.
In the
Database Options
section, make sure that
Enable Audit Logs
is selected.
Under
Destination
, choose
S3
and specify the
S3 bucket
where logs will be stored.
Click
Save changes
to apply the settings.
Optional: AWS Aurora Logs Configuration using CloudWatch
For additional monitoring capabilities, you can configure
CloudWatch Logs
to capture Aurora logs.
In the
RDS Dashboard
, select your
Aurora cluster
.
Under the
Logs & Monitoring
section, make sure that
CloudWatch Logs
integration is enabled.
Go to
CloudWatch Logs
and create a new
Log Group
to store the Aurora logs.
On the
Log Groups
screen, choose the name of your new
Log Group
.
Select
Actions
>
Export data to Amazon S3
.
On the
Export data to Amazon S3
screen, under
Define data export
, set the time range for the data to export using
From
and
To
.
Choose S3 bucket
, select the account associated with the Amazon S3 bucket.
S3 bucket name
, select an Amazon S3 bucket.
S3 Bucket prefix
, enter the randomly generated string that you specified in the bucket policy.
Choose
Export
to export your log data to Amazon S3.
To view the status of the log data that you exported to Amazon S3, select
Actions
>
View all exports to Amazon S3
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New
Content Hub
>
Content Packs
>
Get Started
How to set up the AWS Aurora feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Aurora
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
account
principal.group.product_object_id
Directly mapped from the
account
field in the raw log.
column1
timestamp_epoch
Directly mapped from the
column1
field in the raw log. Used to derive
metadata.event_timestamp
.
column10
Varies
Can be
principal.process.command_line
,
object
or
number
depending on the log format.
column11
ddl
or
response
or
command_line2
Can be
principal.resource.resource_subtype
(ddl),
security_result.outcomes.value
(response) or part of
principal.process.command_line
(command_line2) depending on the log format.
column12
operation
or
response
or
command_line3
Can be
sr.summary
(operation),
security_result.outcomes.value
(response) or part of
principal.process.command_line
(command_line3) depending on the log format.
column13
database
or
response
Can be
target.resource.name
(database) or
security_result.outcomes.value
(response) depending on the log format.
column14
object
Directly mapped to
principal.resource.product_object_id
or
target_data.resource.name
depending on the log format.
column15
command_line
Directly mapped to
principal.process.command_line
.
column16
response
Directly mapped to
security_result.outcomes.value
.
column2
timestamp
or
timestamp_ms
Directly mapped from the
column2
field in the raw log.
column3
ip
or
hostname
Can be
principal.ip
or
principal.resource.name
depending on the log format.
column4
port
or
userid
Can be
principal.port
or
principal.user.userid
depending on the log format.
column5
userid
or
ip
Can be
principal.user.userid
or
principal.ip
depending on the log format.
column6
hostname
or
connection_id
Can be
principal.resource.name
or
network.session_id
depending on the log format.
column7
connection_id
or
query_id
Can be
network.session_id
or
principal.process.pid
depending on the log format.
column8
operation
Directly mapped to
sr.summary
or
metadata.product_event_type
.
column9
query_id
or
database
Can be
principal.process.pid
or
target_data.resource.name
depending on the log format.
command_line
principal.process.command_line
Directly mapped from the extracted
command_line
field.
connection_id
network.session_id
Directly mapped from the extracted
connection_id
field.
database
target.resource.name
Directly mapped from the extracted
database
field. Derived from several fields like
operation
,
command_line
,
has_principal_user
, and
has_principal_machine
through conditional logic in the parser.  Can be
RESOURCE_DELETION
,
RESOURCE_CREATION
,
RESOURCE_READ
,
RESOURCE_WRITTEN
,
USER_RESOURCE_ACCESS
,
USER_UNCATEGORIZED
, or
GENERIC_EVENT
. Hardcoded to "AWS_AURORA". Mapped from
column8
or derived from parser logic. Hardcoded to "AURORA". Hardcoded to "AMAZON".
has_principal_machine
has_principal_machine
Set to "true" if
principal.ip
is present, otherwise initialized to "false".
has_principal_user
has_principal_user
Set to "true" if
principal.user.userid
is present, otherwise initialized to "false".
hostname
principal.resource.name
Directly mapped from the extracted
hostname
field.
ip
principal.ip
Directly mapped from the extracted
ip
field.
logevent.id
security_result.detection_fields.value
Nested within
target.logEvents.logEvents
, mapped with key "id".
logevent.message
security_result.detection_fields.value
Nested within
target.logEvents.logEvents
, mapped with key "message". Used to extract
principal.ip
,
time_unix
,
operation
, and
user
.
logevent.timestamp
security_result.detection_fields.value
Nested within
target.logEvents.logEvents
, mapped with key "timestamp".
object
target_data.resource.name
or
principal.resource.product_object_id
Directly mapped from the extracted
object
field.
operation
sr.summary
Directly mapped from the extracted
operation
field.
port
principal.port
Directly mapped from the extracted
port
field.
query_id
principal.process.pid
Directly mapped from the extracted
query_id
field.
response
security_result.outcomes.value
Directly mapped from the extracted
response
field.
service
principal.application
Directly mapped from the
service
field in the raw log.
src_ip
principal.ip
Extracted from
logevent.message
within the nested
target.logEvents.logEvents
structure.
target.logEvents.logGroup
target.resource.attribute.labels.value
Mapped with key "logGroup".
target.logEvents.logStream
target.resource.attribute.labels.value
Mapped with key "logStream".
target.logEvents.messageType
target.resource.attribute.labels.value
Mapped with key "messageType".
target.logEvents.owner
target.resource.attribute.labels.value
Mapped with key "owner".
timestamp_epoch
metadata.event_timestamp
Converted to
metadata.event_timestamp
using the
date
filter.
user
principal.user.userid
Extracted from
logevent.message
within the nested
target.logEvents.logEvents
structure.
userid
principal.user.userid
Directly mapped from the extracted
userid
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
