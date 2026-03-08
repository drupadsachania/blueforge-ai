# Collect Snowflake logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake/  
**Scraped:** 2026-03-05T10:00:20.546118Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Snowflake logs
Supported in:
Google secops
SIEM
This document explains how to ingest Snowflake logs to Google Security Operations
using AWS S3. The parser extracts fields from the log messages using a series of
Grok and KV pattern matching rules, specifically designed to handle Snowflake
log format. It then maps the extracted fields to the Unified Data Model (UDM),
enriching the data with additional context and standardizing the representation
for further analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Privileged access to Snowflake (ACCOUNTADMIN)
Configure an Amazon S3 Bucket
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
Save the bucket
Name
and
Region
for future reference.
Configure the Snowflake AWS IAM Policy
Sign in to the
AWS
Management Console.
Search for and select
IAM
.
Select
Account settings
.
Under
Security Token Service
(STS) in the
Endpoints
list, find the
Snowflake region
where your account is located.
If the
STS
status is
inactive
, move the toggle to
Active
.
Select
Policies
.
Select
Create Policy
.
In
Policy editor
, select
JSON
.
Copy and paste the following policy (in JSON format) to provide Snowflake with the required permissions to load or unload data using a single bucket and folder path. You can also purge data files using the
PURGE
copy option.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
              "s3:PutObject",
              "s3:GetObject",
              "s3:GetObjectVersion",
              "s3:DeleteObject",
              "s3:DeleteObjectVersion"
            ],
            "Resource": "arn:aws:s3:::<bucket>/<prefix>/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::<bucket>",
            "Condition": {
                "StringLike": {
                    "s3:prefix": [
                        "<prefix>/*"
                    ]
                }
            }
        }
    ]
}
Click
Next
.
Enter a
Policy name
(for example,
snowflake_access
) and an optional
Description
.
Click
Create policy
.
Configure Snowflake AWS IAM Role
In the AWS Identity and Access Management (IAM), select
Roles
.
Click
Create role
.
Select
AWS account
as the trusted entity type.
Select
Another AWS account
.
In the Account ID field, enter your own AWS account ID
temporarily
. Later, you modify the trust relationship and grant access to Snowflake.
Select the
Require external ID
option.
Enter a placeholder ID such as
0000
. In a later step, you will modify the trust relationship for your IAM role and specify the external ID for your storage integration.
Click
Next
.
Select the
IAM policy
you created earlier.
Click
Next
.
Enter a
name
and
description
for the role.
Click
Create role
.
On the role summary page, copy and save the
Role ARN value
.
Configure Snowflake S3 Integration
Connect to the
Snowflake
db.
Replace the following fields and run the command:
<integration_name>
is the name of the new integration (for example,
s3_integration
).
<iam_role>
is the Amazon Resource Name (ARN) of the role you created earlier.
<aws_s3_bucket_path>
is the path to the bucket you created earlier (for example,
s3://your-log-bucket-name/
).
CREATE OR REPLACE STORAGE INTEGRATION <integration_name>
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = '<iam_role>'
  STORAGE_ALLOWED_LOCATIONS = ('<aws_s3_bucket_path>')
Configure AWS IAM User Permissions to Access Bucket
Retrieve the
ARN
for the IAM user that was created automatically for your Snowflake account, replace
<integration_name>
with the actual name of the integration you created earlier:
none
DESC INTEGRATION <integration_name>;
For example:
none
DESC INTEGRATION s3_integration;
+---------------------------+---------------+--------------------------------------------------------------------------------+------------------+
| property                  | property_type | property_value                                                                 | property_default |
+---------------------------+---------------+--------------------------------------------------------------------------------+------------------|
| ENABLED                   | Boolean       | true                                                                           | false            |
| STORAGE_ALLOWED_LOCATIONS | List          | s3://mybucket1/mypath1/,s3://mybucket2/mypath2/                                | []               |
| STORAGE_BLOCKED_LOCATIONS | List          | s3://mybucket1/mypath1/sensitivedata/,s3://mybucket2/mypath2/sensitivedata/    | []               |
| STORAGE_AWS_IAM_USER_ARN  | String        | arn:aws:iam::123456789001:user/abc1-b-self1234                                 |                  |
| STORAGE_AWS_ROLE_ARN      | String        | arn:aws:iam::001234567890:role/myrole                                          |                  |
| STORAGE_AWS_EXTERNAL_ID   | String        | MYACCOUNT_SFCRole=2_a123456/s0aBCDEfGHIJklmNoPq=                               |                  |
+---------------------------+---------------+--------------------------------------------------------------------------------+------------------+
Copy and save the values for the following properties:
STORAGE_AWS_IAM_USER_ARN
STORAGE_AWS_EXTERNAL_ID
Go to the
AWS Management Console
.
Select
IAM
>
Roles
.
Select the
role
you created earlier.
Select the
Trust relationships
tab.
Click
Edit trust policy
.
Update the policy document with the
DESC INTEGRATION
output values:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "<snowflake_user_arn>"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<snowflake_external_id>"
        }
      }
    }
  ]
}
Replace:
snowflake_user_arn
is the
STORAGE_AWS_IAM_USER_ARN
value you recorded.
snowflake_external_id
is the
STORAGE_AWS_EXTERNAL_ID
value you recorded.
Click
Update policy
.
Configure JSON File Format in Snowflake
In Snowflake, enter the following command:
CREATE
OR
REPLACE
FILE
FORMAT
my_json_format
type
=
json
COMPRESSION
=
'
gzip
'
null_if
=
(
'
NULL
'
,
'
null
'
);
Create S3 Stage in Snowflake
In Snowflake, replace the following fields and enter the command:
<DB_NAME>
<DB_SCHEMA_NAME>
<AWS_S3_BUCKET_PATH>
use database '<DB_NAME>';
use schema '<DB_SCHEMA_NAME>';
CREATE OR REPLACE STAGE my_s3_stage
storage_integration = s3_integration
url = '<AWS_S3_BUCKET_PATH>'
file_format = my_json_format;
Configure Snowflake to export data
Run the unload command to export data from tables to stage and in turn to AWS S3:
use database '<DB_NAME>';
use WAREHOUSE '<WAREHOUSE_NAME>';

copy into @my_s3_stage/login_history from (SELECT OBJECT_CONSTRUCT('application', 'snowflake' ,'environment', '<PUT_HERE_ENV_NAME>', 'log_type', 'login_history', 'EVENT_TIMESTAMP', EVENT_TIMESTAMP, 'EVENT_TYPE', EVENT_TYPE, 'USER_NAME', USER_NAME, 'CLIENT_IP', CLIENT_IP, 'REPORTED_CLIENT_TYPE', REPORTED_CLIENT_TYPE, 'FIRST_AUTHENTICATION_FACTOR',FIRST_AUTHENTICATION_FACTOR, 'IS_SUCCESS', IS_SUCCESS, 'ERROR_CODE', ERROR_CODE, 'ERROR_MESSAGE', ERROR_MESSAGE) from snowflake.account_usage.Login_history) FILE_FORMAT = (TYPE = JSON) ;

copy into @my_s3_stage/access_history from (SELECT OBJECT_CONSTRUCT('application', 'snowflake' ,'environment', '<PUT_HERE_DB_NAME>', 'log_type', 'access_history', 'QUERY_START_TIME',QUERY_START_TIME, 'USER_NAME', USER_NAME, 'DIRECT_OBJECTS_ACCESSED',DIRECT_OBJECTS_ACCESSED, 'BASE_OBJECTS_ACCESSED', BASE_OBJECTS_ACCESSED, 'OBJECTS_MODIFIED', OBJECTS_MODIFIED) from snowflake.account_usage.Access_History ) FILE_FORMAT = (TYPE = JSON);
Repeat the export process for all the following tables in which Snowflake stores logs and audit related data:
Databases ;
WAREHOUSE_EVENTS_HISTORY ;
WAREHOUSE_LOAD_HISTORY ;
WAREHOUSE_METERING_HISTORY ;
DATABASE_STORAGE_USAGE_HISTORY ;
DATA_TRANSFER_HISTORY ;
GRANTS_TO_ROLES ;
GRANTS_TO_USERS ;
METERING_DAILY_HISTORY ;
PIPE_USAGE_HISTORY ;
REPLICATION_USAGE_HISTORY ;
STAGE_STORAGE_USAGE_HISTORY ;
STORAGE_USAGE ;
TASK_HISTORY ;
COPY_HISTORY ;
Configure AWS IAM for Google SecOps
Sign in to the
AWS
Management Console.
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
Download CSV file
for save the
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
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
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
Snowflake Logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Snowflake
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: The bucket URI (the format should be:
s3://your-log-bucket-name/
).
Replace the following:
your-log-bucket-name
: the name of the bucket.
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
Need more help?
Get answers from Community members and Google SecOps professionals.
