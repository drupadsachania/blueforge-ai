# Collect Gmail logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gmail-logs/  
**Scraped:** 2026-03-05T09:56:34.699944Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Gmail logs
Supported in:
Google secops
SIEM
This document explains how to ingest Gmail logs to Google Security Operations using Google Cloud Storage V2.
Gmail is Google Workspace's email service that provides secure, intelligent email with built-in spam and phishing protection. Gmail logs capture detailed information about email delivery, security events, and message flow through the Gmail infrastructure.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
GCP project with Cloud Storage API and BigQuery API enabled
Google Workspace account with appropriate edition (Enterprise Standard, Enterprise Plus, Education Standard, or Education Plus)
Super administrator access to Google Workspace Admin console
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create BigQuery scheduled queries
The service account gapps-reports@system.gserviceaccount.com must have editor role on the BigQuery project
Create Google Cloud Storage bucket
Using Google Cloud Console
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
gmail-logs-export
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
Using gcloud command-line tool
Alternatively, create a bucket using the
gcloud
command:
gcloud
storage
buckets
create
gs://gmail-logs-export
\
--location
=
us-central1
\
--default-storage-class
=
STANDARD
Replace:
gmail-logs-export
: Your desired bucket name (globally unique).
us-central1
: Your preferred region (for example,
us-central1
,
europe-west1
).
Configure Google Workspace to export logs to BigQuery
Google Workspace logs, including Gmail logs, are exported to BigQuery through the unified Workspace logs and reports feature.
Enable BigQuery export for Workspace logs
Sign in with a super administrator account to the
Google Admin console
.
Go to
Menu
>
Reporting
>
Data integrations
.
Point to the
BigQuery Export
card and click
Edit
.
Check the
Enable Google Workspace data export to Google BigQuery
box.
Under
BigQuery project ID
, select the project where you want to store the logs.
Under
New dataset within project
, enter the name of the dataset to use for storing the logs (for example,
workspace_logs
).
Optional: Check the
Restrict the dataset to a specific geographic location
box and select the location from the menu.
Click
Save
.
After enabling the export, activity log events are typically available within 10 minutes. The data is exported to tables named
activity_YYYYMMDD
in the specified dataset.
Create scheduled query to export from BigQuery to GCS
To automatically export Gmail logs from BigQuery to Cloud Storage on a recurring schedule, create a scheduled query using the EXPORT DATA statement.
Using BigQuery Console
In the
Google Cloud Console
, go to
BigQuery
.
In the left navigation, click
Scheduled queries
.
Click
Create scheduled query
.
In the
Query editor
, enter the following SQL:
EXPORT
DATA
OPTIONS
(
uri
=
'gs://gmail-logs-export/gmail-logs/*.json'
,
format
=
'JSON'
,
overwrite
=
false
)
AS
SELECT
*
FROM
`
PROJECT_ID
.
workspace_logs
.
activity_
*`
WHERE
record_type
=
'gmail'
AND
_TABLE_SUFFIX
=
FORMAT_DATE
(
'%Y%m%d'
,
DATE_SUB
(
CURRENT_DATE
(),
INTERVAL
1
DAY
))
Replace:
gmail-logs-export
: Your GCS bucket name
PROJECT_ID
: Your GCP project ID
workspace_logs
: Your BigQuery dataset name
In the
Schedule options
section:
Repeat
: Select
Hours
.
Every
: Enter
1
.
Start date and run time
: Select current date and time.
In the
Destination for query results
section:
Dataset
: Select a dataset for query metadata (not the exported data).
Click
Save
.
Using bq command-line tool
Alternatively, create a scheduled query using the
bq
command:
bq
mk
\
--transfer_config
\
--project_id
=
PROJECT_ID
\
--data_source
=
scheduled_query
\
--display_name
=
'Gmail Logs Export to GCS'
\
--schedule
=
'every 1 hours'
\
--params
=
'{
"query":"EXPORT DATA OPTIONS(uri=\"gs://gmail-logs-export/gmail-logs/*.json\", format=\"JSON\", overwrite=false) AS SELECT * FROM `PROJECT_ID.workspace_logs.activity_*` WHERE record_type = \"gmail\" AND _TABLE_SUFFIX = FORMAT_DATE(\"%Y%m%d\", DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))",
"destination_table_name_template":"gmail_export_metadata",
"write_disposition":"WRITE_TRUNCATE"
}'
Replace:
PROJECT_ID
: Your GCP project ID
gmail-logs-export
: Your GCS bucket name
workspace_logs
: Your BigQuery dataset name
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest Gmail logs
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
Gmail Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
GMAIL Logs
as the
Log type
.
Click
Get Service Account
. A unique service account email is displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://gmail-logs-export/gmail-logs/
Replace:
gmail-logs-export
: Your GCS bucket name
gmail-logs
: The prefix/folder path where logs are stored
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Using Google Cloud Console
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
: Paste the Google SecOps service account email.
Assign roles
: Select
Storage Object Viewer
.
Click
Save
.
Using gcloud command-line tool
Alternatively, grant permissions using the
gcloud
command:
gcloud
storage
buckets
add-iam-policy-binding
gs://gmail-logs-export
\
--member
=
"serviceAccount:SECOPS_SERVICE_ACCOUNT_EMAIL"
\
--role
=
"roles/storage.objectViewer"
Replace:
gmail-logs-export
: Your bucket name.
SECOPS_SERVICE_ACCOUNT_EMAIL
: The Google SecOps service account email.
Using gsutil command-line tool (legacy)
Grant the SecOps service account Object Viewer access to the Gmail logs export bucket.
gsutil
iam
ch
serviceAccount:SECOPS_SERVICE_ACCOUNT_EMAIL:objectViewer
\
gs://gmail-logs-export
Verify permissions
To verify the permissions were granted correctly:
gcloud
storage
buckets
get-iam-policy
gs://gmail-logs-export
\
--flatten
=
"bindings[].members"
\
--filter
=
"bindings.role:roles/storage.objectViewer"
You should see the Google SecOps service account email in the output.
UDM mapping table
Log Field
UDM Mapping
Logic
attachment.file_extension_type, attachment.sha256, attachment.file_name, domains
about
Merged with attachment details and link domains
message_info.post_delivery_info.action_type, gmail.message_info.post_delivery_info.action_type, event_info.mail_event_type, gmail.event_info.mail_event_type, tok.product_bucket, tok.scope_name, record_type, token.client_type, message_info.num_message_attachments, gmail.message_info.num_message_attachments
additional.fields
Merged with various additional metadata fields
action_type, description, rule_id
metadata.description
Set to specific descriptions based on action_type values, or from description, or "Objectionable content" if rule_id == 7
metadata.event_type
Set to "EMAIL_TRANSACTION"
event_name
metadata.product_event_type
Value copied directly
metadata.product_name
Set to "GMAIL"
metadata.vendor_name
Set to "Google"
__incoming_message, __outcoming_message
network.direction
Set to "INBOUND" if incoming message detected, "OUTBOUND" if outcoming
destination.address
network.email.cc
Merged from destination addresses where index > 0
message_info.source.from_header_address, message_info.source.address
network.email.from
Value from from_header_address if not empty, else from source.address
message_info.rfc2822_message_id, gmail.message_info.rfc2822_message_id
network.email.mail_id
Extracted from rfc2822_message_id, removing < >, using grok
message_info.subject, gmail.message_info.subject
network.email.subject
Value from message_info.subject if not empty, else gmail.message_info.subject
destination.address
network.email.to
Merged from first destination address
network.ip_protocol
Set to "TCP"
_payload_size
network.received_bytes
Set to _payload_size if incoming message
_payload_size
network.sent_bytes
Set to _payload_size if outcoming message
token.app_name, message_info.source.service, message_info.source.selector, gmail.message_info.source.service, gmail.message_info.source.selector
principal.application
Value from token.app_name if not empty, else concatenated from source.service and source.selector
message_info.connection_info.client_host_zone, gmail.message_info.connection_info.client_host_zone
principal.asset.hostname
Value from client_host_zone
client_ip
principal.asset.ip
Value copied directly
message_info.connection_info.client_host_zone, gmail.message_info.connection_info.client_host_zone
principal.hostname
Value from client_host_zone
client_ip
principal.ip
Value copied directly
message_info.connection_info.ip_geo_country, gmail.message_info.connection_info.ip_geo_country
principal.location.country_or_region
Value from ip_geo_country
email, source_address
principal.user.email_addresses
Merged from email_address and source_address
token.client_id
principal.user.group_identifiers
Value copied directly
message_info.source.from_header_displayname, gmail.message_info.source.from_header_displayname
principal.user.user_display_name
Value from from_header_displayname
source_address
principal.user.userid
Value copied directly
action
security_result.action
Value copied directly
category
security_result.category
Value copied directly
category_details
security_result.category_details
Value copied directly
message_info.connection_info.smtp_response_reason, gmail.message_info.connection_info.smtp_response_reason, rule_description, reason
security_result.description
Set to smtp response reason, or rule description, or classification reason
stringMatch.predefined_detector_name, stringMatch.matched_string, stringMatch.match_expression, stringMatch.source, stringMatch.type
security_result.detection_fields
Merged with detection field objects
rule_id
security_result.rule_id
Value copied directly
rule_name
security_result.rule_name
Value copied directly
_err_summary, rule_id, description
security_result.summary
Set to error summary, or rule-specific summary, or description
_target_host
target.administrative_domain
Value copied directly
message_info.destination.0.service, message_info.destination.0.selector, gmail.message_info.destination.0.service, gmail.message_info.destination.0.selector
target.application
Concatenated from service and selector
Need more help?
Get answers from Community members and Google SecOps professionals.
