# Collect AWS RDS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-rds/  
**Scraped:** 2026-03-05T09:50:41.739931Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS RDS logs
Supported in:
Google secops
SIEM
This document describes how you can collect AWS RDS logs by
setting up a Google SecOps feed.
For more information, see
Data ingestion to Google SecOps
.
An ingestion label identifies the parser that normalizes raw log data
to structured UDM format. The information in this document applies to the parser with the
AWS_RDS
ingestion label.
Before you begin
Ensure you have the following prerequisites:
An AWS account that you can sign in to
A global administrator or RDS administrator
How to configure AWS RDS
Use an existing database or create a new database:
To use an existing database, select the database, click
Modify
, and then select
Log exports
.
To use a new database, when you create the database, select
Additional configuration
.
To publish to Amazon CloudWatch, select the following log types:
Audit log
Error log
General log
Slow query log
To specify log export for AWS Aurora PostgreSQL and PostgreSQL, select
PostgreSQL log
.
To specify log export for AWS Microsoft SQL server, select the following log types:
Agent log
Error log
Save the log configuration.
Select
CloudWatch
>
Logs
to view the collected logs. The log groups are
automatically created after the logs are available through the instance.
To publish the logs to CloudWatch, configure IAM user and KMS key policies. For more information, see
IAM user and KMS key policies
.
Based on the service and region, identify the endpoints for connectivity by referring to the following AWS documentation:
For information about any logging sources, see
AWS Identity and Access Management endpoints and quotas
.
For information about CloudWatch logging sources, see
CloudWatch logs endpoints and quotas
.
For engine-specific information, see the following documentation:
Publishing MariaDB logs to Amazon CloudWatch Logs
.
Publishing MySQL logs to Amazon CloudWatch Logs
.
Publishing Oracle logs to Amazon CloudWatch Logs
.
Publishing PostgreSQL logs to Amazon CloudWatch Logs
.
Publishing SQL Server logs to Amazon CloudWatch Logs
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
How to set up the AWS RDS feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS RDS
log type.
Google SecOps supports log collection using an access key ID and secret method.
To create the access key ID and secret, see
Configure tool authentication with AWS
.
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
Field mapping reference
This parser extracts fields from AWS RDS syslog messages, primarily focusing on timestamp, description, and client IP. It uses grok patterns to identify these fields and populates corresponding UDM fields, classifying events as either
GENERIC_EVENT
or
STATUS_UPDATE
based on the presence of a client IP.
UDM mapping table
Log Field
UDM Mapping
Logic
client_ip
principal.ip
Extracted from the raw log message using the regular expression
\\[CLIENT: %{IP:client_ip}\\]
.
create_time.nanos
N/A
Not mapped to the IDM object.
create_time.seconds
N/A
Not mapped to the IDM object.
metadata.description
The descriptive message from the log, extracted using grok patterns. Copied from
create_time.nanos
. Copied from
create_time.seconds
. Set to "GENERIC_EVENT" by default. Changed to "STATUS_UPDATE" if
client_ip
is present. Static value "AWS_RDS", set by the parser. Static value "AWS_RDS", set by the parser.
pid
principal.process.pid
Extracted from the
descrip
field using the regular expression
process ID of %{INT:pid}
.
Need more help?
Get answers from Community members and Google SecOps professionals.
