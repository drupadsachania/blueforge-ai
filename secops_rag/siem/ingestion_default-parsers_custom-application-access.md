# Collect Custom Application Access logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-application-access/  
**Scraped:** 2026-03-05T09:22:47.461518Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Custom Application Access logs
Supported in:
Google secops
SIEM
This document explains how to ingest Custom Application Access logs into Google Security Operations using cloud storage or streaming ingestion methods.
Custom application access logs capture authentication events, authorization decisions, and access patterns from proprietary or custom-built applications. These logs are essential for monitoring user activity, detecting unauthorized access attempts, and maintaining compliance with security policies.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Custom application access logs in JSON, CSV, or structured text format
Access to one of the following:
Google Cloud Storage bucket (for GCS ingestion)
Amazon S3 bucket (for S3 ingestion)
Microsoft Azure Storage Account (for Azure Blob ingestion)
Webhook endpoint capability (for push-based ingestion)
Amazon Kinesis Data Firehose (for streaming ingestion)
Create a custom log type
The log type
CUSTOM_APPLICATION_ACCESS
does not exist as a prebuilt parser in Google SecOps. You must create a custom log type before ingesting logs.
Go to
SIEM Settings
>
Available Log Types
.
Click
Request a Log Type
.
Under
Create a custom log type on your own
, enter the following details:
Vendor/Product
: Enter
Custom Application Access Logs
Log Type
: Enter
CUSTOM_APPLICATION_ACCESS
Click
Create Log Type
.
Wait 10 minutes to ensure that the new log type is available in all components before creating feeds.
Choose your ingestion method
Select the ingestion method that best fits your infrastructure:
Google Cloud Storage (GCS)
: Use if your application writes logs to GCS buckets or you can export logs to GCS
Amazon S3
: Use if your application writes logs to S3 buckets or you can export logs to S3
Azure Blob Storage
: Use if your application writes logs to Azure Storage or you can export logs to Azure
Webhook
: Use if your application can send HTTP POST requests to an external endpoint
Amazon Kinesis Data Firehose
: Use if your application writes to CloudWatch Logs or you need real-time streaming
Option 1: Ingest from Google Cloud Storage
Create Google Cloud Storage bucket
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
custom-app-access-logs
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location (for example,
us-central1
)
Storage class
Standard (recommended for frequently accessed logs)
Access control
Uniform (recommended)
Protection tools
Optional: Enable object versioning or retention policy
Click
Create
.
Configure your application to write logs to GCS
Configure your custom application to write access logs to the GCS bucket you created. The logs should be written in one of the following formats:
JSON format (recommended):
{
"timestamp"
:
"2025-01-15T10:30:00Z"
,
"user"
:
"john.doe@example.com"
,
"action"
:
"login"
,
"result"
:
"success"
,
"source_ip"
:
"203.0.113.45"
,
"application"
:
"custom-app"
,
"resource"
:
"/api/users"
}
CSV format:
timestamp,user,action,result,source_ip,application,resource
2025-01-15T10:30:00Z,john.doe@example.com,login,success,203.0.113.45,custom-app,/api/users
Newline-delimited JSON (NDJSON):
{
"timestamp"
:
"2025-01-15T10:30:00Z"
,
"user"
:
"john.doe@example.com"
,
"action"
:
"login"
,
"result"
:
"success"
}
{
"timestamp"
:
"2025-01-15T10:30:05Z"
,
"user"
:
"jane.smith@example.com"
,
"action"
:
"access"
,
"result"
:
"denied"
}
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Custom Application Access Logs - GCS
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
CUSTOM_APPLICATION_ACCESS_CUSTOM
as the
Log type
.
Click
Get Service Account
.
A unique service account email will be displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs the
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email
Assign roles
: Select
Storage Object Viewer
Click
Save
.
Configure the feed in Google SecOps
Return to the feed creation page (or go to
SIEM Settings
>
Feeds
>
Add New Feed
).
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://custom-app-access-logs/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days).
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed (for example,
custom_app_access
).
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Option 2: Ingest from Amazon S3
Create an Amazon S3 bucket
Open the
Amazon S3 console
.
Click
Create Bucket
.
Provide the following configuration details:
Bucket Name
: Enter a meaningful name for the bucket (for example,
custom-app-access-logs
).
Region
: Select the Region where your application runs (for example,
us-east-1
).
Click
Create
.
Create an IAM user with S3 access
Open the
IAM console
.
Click
Users
>
Add user
.
Enter a
user name
(for example,
chronicle-s3-reader
).
Select
Programmatic access
.
Click
Next: Permissions
.
Choose
Attach existing policies directly
.
Search for and select the
AmazonS3FullAccess
policy.
Click
Next: Tags
.
Click
Next: Review
.
Click
Create user
.
Click
Download .csv file
to save the
Access Key
and
Secret Access Key
for future reference.
Click
Close
.
Configure your application to write logs to S3
Configure your custom application to write access logs to the S3 bucket you created. Use the same log formats as described in the GCS section (JSON, CSV, or NDJSON).
Configure a feed in Google SecOps to ingest logs from S3
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Custom Application Access Logs - S3
).
Select
Amazon S3 V2
as the
Source type
.
Select
CUSTOM_APPLICATION_ACCESS_CUSTOM
as the
Log type
.
Click
Next
and then click
Submit
.
Specify values for the following input parameters:
S3 URI
: Enter the bucket URI in format:
s3://custom-app-access-logs/
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
: The label to be applied to the events from this feed (for example,
custom_app_access
).
Click
Next
and then click
Submit
.
Option 3: Ingest from Azure Blob Storage
Create Azure Storage Account
In the
Azure portal
, search for
Storage accounts
.
Click
+ Create
.
Provide the following configuration details:
Setting
Value
Subscription
Select your Azure subscription
Resource group
Select existing or create new
Storage account name
Enter a unique name (for example,
customappaccesslogs
)
Region
Select the region (for example,
East US
)
Performance
Standard (recommended)
Redundancy
LRS (Locally redundant storage)
Click
Review + create
.
Review the overview of the account and click
Create
.
Wait for the deployment to complete.
Get Storage Account credentials
Go to the
Storage Account
you just created.
In the left navigation, select
Access keys
under
Security + networking
.
Click
Show keys
.
Copy and save the following for later use:
Storage account name
:
customappaccesslogs
Key 1
or
Key 2
: The shared access key
Create a blob container
In the same Storage Account, select
Containers
from the left navigation.
Click
+ Container
.
Provide the following configuration details:
Name
: Enter
access-logs
Public access level
: Select
Private (no anonymous access)
Click
Create
.
Configure your application to write logs to Azure Blob Storage
Configure your custom application to write access logs to the Azure Blob Storage container you created. Use the same log formats as described in the GCS section (JSON, CSV, or NDJSON).
Configure a feed in Google SecOps to ingest logs from Azure
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Custom Application Access Logs - Azure
).
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
CUSTOM_APPLICATION_ACCESS_CUSTOM
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Azure URI
: Enter the Blob Service endpoint URL with the container path:
https://customappaccesslogs.blob.core.windows.net/access-logs/
Source deletion option
: Select the deletion option according to your preference
Maximum File Age
: Include files modified in the last number of days (default is 180 days)
Shared key
: Enter the shared key value (access key) you captured from the Storage Account
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed (for example,
custom_app_access
)
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Option 4: Ingest using Webhook
Create webhook feed in Google SecOps
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Custom Application Access Logs - Webhook
).
Select
Webhook
as the
Source type
.
Select
CUSTOM_APPLICATION_ACCESS_CUSTOM
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
: Enter
\n
to split newline-delimited events (if sending multiple events per request).
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed (for example,
custom_app_access
).
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Generate and save secret key
On the feed details page, click
Generate Secret Key
.
A dialog displays the secret key.
Copy and save the secret key securely.
Get the feed endpoint URL
Go to the
Details
tab of the feed.
In the
Endpoint Information
section, copy the
Feed endpoint URL
.
The URL format is:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
Save this URL for the next steps.
Click
Done
.
Create Google Cloud API key
Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.
Go to the
Google Cloud Console Credentials page
.
Select your project (the project associated with your Chronicle instance).
Click
Create credentials
>
API key
.
An API key is created and displayed in a dialog.
Click
Edit API key
to restrict the key.
In the
API key
settings page:
Name
: Enter a descriptive name (for example,
Chronicle Webhook API Key
).
Under
API restrictions
:
Select
Restrict key
.
In the
Select APIs
dropdown, search for and select
Google SecOps API
(or
Chronicle API
).
Click
Save
.
Copy the API key value from the
API key
field at the top of the page.
Save the API key securely.
Configure your application to send logs via webhook
Configure your custom application to send HTTP POST requests to the Chronicle webhook endpoint.
Construct the webhook URL:
Append the API key to the feed endpoint URL:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=<API_KEY>
Replace
<API_KEY>
with the API key you created.
HTTP POST request format:
POST https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=<API_KEY> HTTP/1.1
Content-Type: application/json
x-chronicle-auth: <SECRET_KEY>
{"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success", "source_ip": "203.0.113.45"}
For multiple events (newline-delimited):
POST https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=<API_KEY> HTTP/1.1
Content-Type: application/json
x-chronicle-auth: <SECRET_KEY>
{"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success"}
{"timestamp": "2025-01-15T10:30:05Z", "user": "jane.smith@example.com", "action": "access", "result": "denied"}
Example using curl:
curl
-X
POST
\
"https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_API_KEY"
\
-H
"Content-Type: application/json"
\
-H
"x-chronicle-auth: YOUR_SECRET_KEY"
\
-d
'{"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success", "source_ip": "203.0.113.45"}'
Option 5: Ingest using Amazon Kinesis Data Firehose
Create a feed in Google SecOps
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Custom Application Access Logs - Firehose
).
Select
Amazon Data Firehose
as the
Source type
.
Select
CUSTOM_APPLICATION_ACCESS_CUSTOM
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
: Enter
\n
to split newline-delimited logs.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed (for example,
custom_app_access
).
Click
Next
.
Review the feed configuration and click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and save the secret key as you cannot view this secret again.
Go to the
Details
tab.
Copy the feed endpoint URL from the
Endpoint Information
field.
Click
Done
.
Create an API key for the Amazon Data Firehose feed
Go to the
Google Cloud console
Credentials
page at https://console.cloud.google.com/apis/credentials
Click
Create credentials
, and then select
API key
.
Click
Edit API key
to restrict the key.
Under
API restrictions
, select
Restrict key
.
Search for and select
Google SecOps API
.
Click
Save
.
Copy and save the API key.
Construct the endpoint URL
Append the API key to the feed endpoint URL in the following format:
<FEED_ENDPOINT_URL>?key=<API_KEY>
Replace the following:
<FEED_ENDPOINT_URL>
: The feed endpoint URL in a previous step
<API_KEY>
: The API key in a previous step
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
Save this full URL for the next step.
Create IAM policy for Firehose
In the
AWS Console
, go to
IAM
>
Policies
>
Create policy
>
JSON
tab.
Paste the following policy JSON:
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
"firehose:PutRecord"
,
"firehose:PutRecordBatch"
],
"Resource"
:
"arn:aws:firehose:us-east-1:123456789012:deliverystream/CustomAppAccessToChronicle"
}
]
}
Replace the following:
us-east-1
: Your AWS region
123456789012
: Your AWS account ID (12-digit number)
CustomAppAccessToChronicle
: Your Firehose delivery stream name (you will create this in the next step)
Name the policy
CustomAppAccessFirehoseWritePolicy
.
Click
Create policy
.
Create IAM role for CloudWatch Logs
Go to
IAM
>
Roles
>
Create role
.
Select
Custom trust policy
and paste:
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
"Principal"
:
{
"Service"
:
"logs.us-east-1.amazonaws.com"
},
"Action"
:
"sts:AssumeRole"
}
]
}
Replace
us-east-1
with your AWS region.
Click
Next
.
Search for and select the policy
CustomAppAccessFirehoseWritePolicy
that you created in the previous step.
Click
Next
.
Name the role
CloudWatchLogsToFirehoseRole
.
Click
Create role
.
Create Kinesis Data Firehose delivery stream
In the
AWS Console
, go to
Kinesis
>
Data Firehose
>
Create delivery stream
.
Provide the following configuration details:
Source and destination:
Source
: Select
Direct PUT or other sources
Destination
: Select
HTTP endpoint
Delivery stream name:
Delivery stream name
: Enter
CustomAppAccessToChronicle
HTTP endpoint destination:
HTTP endpoint URL
: Enter the full endpoint URL you constructed earlier (feed endpoint + API key)
Content encoding
: Select
GZIP
(recommended for bandwidth savings)
Custom HTTP headers:
Click
Add custom HTTP header
Header name
: Enter
X-Goog-Chronicle-Auth
Header value
: Enter the secret key you saved in a previous step
Backup settings:
Source record backup in Amazon S3
: Select
Failed data only
(recommended)
S3 bucket
: Select an existing bucket or create a new one for failed records
Buffer hints:
Buffer size
: Enter
1
MiB (minimum for HTTP endpoints)
Buffer interval
: Enter
60
seconds
Retry duration:
Retry duration
: Enter
300
seconds (5 minutes)
Click
Create delivery stream
.
Wait for the delivery stream status to change to
Active
(1-2 minutes).
Configure your application to write to CloudWatch Logs
Configure your custom application to write access logs to a CloudWatch Log Group. Then create a subscription filter to stream logs to Firehose.
In the
AWS Console
, go to
CloudWatch
>
Logs
>
Log groups
.
Create a new log group or select an existing one where your application writes logs.
Click the
Subscription filters
tab.
Click
Create
>
Create Amazon Kinesis Data Firehose subscription filter
.
Provide the following configuration details:
Destination
: Select delivery stream
CustomAppAccessToChronicle
.
Grant permission
: Select role
CloudWatchLogsToFirehoseRole
.
Subscription filter name
: Enter
CustomAppAccessToChronicle
.
Log format
: Select
Other
(Google SecOps handles parsing).
Subscription filter pattern
: Leave empty to send all events.
Click
Start streaming
.
Logs stream in real-time to Google SecOps through Firehose.
Create a custom parser
After ingesting logs, you must create a custom parser to normalize the data into UDM format.
Go to
SIEM Settings
>
Parsers
.
Click
Create Parser
.
Select
CUSTOM_APPLICATION_ACCESS_CUSTOM
as the
Log type
.
Use the parser editor to create Grok patterns or parser extensions that map your log fields to UDM fields.
Example parser mapping:
Custom Log Field
UDM Field
timestamp
metadata.event_timestamp
user
principal.user.email_addresses
action
security_result.action
result
security_result.summary
source_ip
principal.ip
application
target.application
resource
target.resource.name
Test the parser with sample logs.
Click
Save
to activate the parser.
For detailed parser creation instructions, see
Self-service parser options
.
Verify ingestion
After configuring the feed and parser, verify that logs are being ingested:
Go to
Search
>
UDM Search
.
Run the following query:
metadata.log_type = "CUSTOM_APPLICATION_ACCESS_CUSTOM"
Verify that events appear in the search results.
Check that UDM fields are populated correctly based on your parser configuration.
UDM mapping table
Log Field
UDM Mapping
Logic
additional
Merged with labels created from service, env, msg.attachment.fileName, msg.attachment.digest, msg.attachment.key, msg.attachment.authorizeId, msg.attachment.contentType, dest.type, type, msg.sortID, msg.refID, state.reported.applications_installed, state.reported.applications_status, state.reported.ota_queue, state.reported.VICMB_Deg_Battery_LimpHome, state.reported.VICMB_Inhibit_Propulsion, state.reported.VICMB_FA_LostComm_BPCM, state.reported.VICMB_FA_LostComm_SFAM1, state.reported.VICMB_Inhibit_HV, state.reported.VICMB_FA_LostComm_RIDM, state.reported.VICMB_FA_LostComm_RWAM1, state.reported.uname, meta.reported.battery_charging_rate_kw.timestamp, state.reported.battery_charging_rate_kw, meta.reported.cell.connected.timestamp, meta.reported.cell.packet_loss.timestamp, meta.reported.cell.average_ping_ms.timestamp, meta.reported.cell.bitrate.timestamp, meta.reported.cell.download_speed_bytes_per_sec.timestamp, meta.reported.cell.signal_strength.timestamp, meta.reported.cell.signal.timestamp, state.reported.cell.connected, state.reported.cell.packet_loss, state.reported.cell.average_ping_ms, state.reported.cell.bitrate, state.reported.cell.download_speed_bytes_per_sec, state.reported.cell.signal_strength, state.reported.cell.signal
request_time
metadata.collected_timestamp
Parsed from request_time using ISO8601 format
msg_1, msg.body
metadata.description
Value from msg_1 if not empty, else msg.body
user_id, src_email, otadata.1687965118.initiator
metadata.event_type
Set to "USER_UNCATEGORIZED" if any of user_id, src_email, otadata.1687965118.initiator are present, else "GENERIC_EVENT"
otadata.1687965118.deployment_id
metadata.product_deployment_id
Value copied directly
version
metadata.product_version
Value copied directly
response.status
network.http.response_code
Converted to integer
request_id
principal.resource.product_object_id
Value copied directly
msg.attachment.url, otadata.1687965118.download_url
principal.url
Value from msg.attachment.url if not empty, else otadata.1687965118.download_url
src_email, otadata.1687965118.initiator
principal.user.email_addresses
Value from src_email if matches email regex, else from otadata.1687965118.initiator
user_id
principal.user.userid
Value copied directly
level
security_result.severity
Set to "INFORMATIONAL" if level is "INFO"
metadata.product_name
Set to "Custom Application Access"
metadata.vendor_name
Set to "Custom Application Access"
Need more help?
Get answers from Community members and Google SecOps professionals.
