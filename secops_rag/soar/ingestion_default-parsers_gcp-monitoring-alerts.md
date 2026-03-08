# Collect Google Cloud Monitoring alerting activity logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-monitoring-alerts/  
**Scraped:** 2026-03-05T09:53:12.405330Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud Monitoring alerting activity logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cloud Logging logs related to Cloud Monitoring alerting activity to Google Security Operations using Google Cloud Storage V2.
Cloud Monitoring provides alerting capabilities for Google Cloud resources. Log-based alerting policies notify you when a particular message appears in your logs. When a log entry meets the condition of the alerting policy, an incident is opened in Cloud Monitoring and you receive a notification for the incident. This integration lets you export Cloud Logging entries to Google Security Operations for security analysis and correlation.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Google Cloud project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to configure Cloud Logging sinks
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
monitoring-logs-export
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
gs://monitoring-logs-export
\
--location
=
us-central1
\
--default-storage-class
=
STANDARD
Replace:
monitoring-logs-export
: Your required bucket name (globally unique).
us-central1
: Your preferred region.
Configure Cloud Logging to export logs to GCS
Log entries are stored as JSON files when routed to Cloud Storage. You can export logs related to Cloud Monitoring alerting activity, such as audit logs for alert policy management.
Create a log sink
In the
Google Cloud Console
, go to
Logging
>
Logs Router
.
Click
Create sink
.
Provide the following configuration details:
Sink name
: Enter a descriptive name (for example,
monitoring-alerts-to-gcs
).
Sink description
: Optional description.
Click
Next
.
In the
Select sink service
section:
Sink service
: Select
Cloud Storage bucket
.
Select Cloud Storage bucket
: Select the bucket (for example,
monitoring-logs-export
) from the list.
Click
Next
.
In the
Choose logs to include in sink
section, enter a filter query to select the logs you want to export.
Example filter for Cloud Monitoring audit logs:
protoPayload.serviceName="monitoring.googleapis.com"
logName:"cloudaudit.googleapis.com/activity"
Example filter for log-based alerting policy triggers:
If you want to export the underlying logs that trigger your log-based alerting policies, use a filter that matches those specific logs. For example:
severity >= ERROR
resource.type="gce_instance"
Click
Next
.
Optional: Configure exclusion filters if needed.
Click
Create sink
.
New sinks that route log data to Cloud Storage buckets might take several hours to start routing log entries. Routed log entries are saved to Cloud Storage buckets in hourly batches. It might take from 2 to 3 hours before the first entries begin to appear.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest Cloud Monitoring logs
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
Google Cloud Monitoring Alerts Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
GCP_MONITORING_ALERTS
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI:
gs://monitoring-logs-export/
Replace
monitoring-logs-export
with your GCS bucket name.
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
Click the bucket name (for example,
monitoring-logs-export
).
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
gs://monitoring-logs-export
\
--member
=
"serviceAccount:SECOPS_SERVICE_ACCOUNT_EMAIL"
\
--role
=
"roles/storage.objectViewer"
Replace:
monitoring-logs-export
: Your bucket name.
SECOPS_SERVICE_ACCOUNT_EMAIL
: The Google SecOps service account email.
Using gsutil command-line tool (legacy)
Grant the SecOps service account the necessary permissions to read objects within your destination bucket:
gsutil
iam
ch
serviceAccount:SECOPS_SERVICE_ACCOUNT_EMAIL:objectViewer
\
gs://monitoring-logs-export
Verify permissions
To verify the permissions were granted correctly:
gcloud
storage
buckets
get-iam-policy
gs://monitoring-logs-export
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
jsonPayload.type_1
additional.fields.jsonPayload_type_1
Value copied directly
jsonPayload.debugInfo
additional.fields.number
Extracted from jsonPayload.debugInfo using grok pattern
jsonPayload.scheduledTime, receiveTimestamp, timestamp
metadata.event_timestamp
Value from jsonPayload.scheduledTime if not empty, else receiveTimestamp if not empty, else timestamp if not empty, converted using date match
event_type
metadata.event_type
Value from event_type if not empty, else set to "GENERIC_EVENT"
insertId
metadata.product_log_id
Value copied directly
jsonPayload.targetType
network.application_protocol
Value copied directly
httpRequest.status
network.http.response_code
Converted to integer
resource.labels.location
principal.location.name
Value copied directly
jsonPayload.jobName
principal.url
Value copied directly
jsonPayload.status
security_result.action
Set to "BLOCK" if jsonPayload.status == "PERMISSION_DENIED"
severity
security_result.severity
Set to INFORMATIONAL if severity =~ (?i)INFO; LOW if severity == "LOW"; MEDIUM if severity == "MEDIUM"; HIGH if severity == "HIGH"; CRITICAL if severity == "VERY-HIGH"
jsonPayload.debugInfo
security_result.summary
Extracted from jsonPayload.debugInfo using grok pattern
logName
src.url
Value copied directly
resource.labels.project_id
target.resource.attribute.labels.project_id
Value copied directly
resource.labels.job_id
target.resource.attribute.labels.resource_labels_job_id
Value copied directly
resource.type
target.resource.resource_subtype
Value copied directly
jsonPayload.url
target.url
Value copied directly
metadata.product_name
Set to "Gcp_monitoring_alerts"
metadata.vendor_name
Set to "GCP_MONITORING_ALERTS"
Need more help?
Get answers from Community members and Google SecOps professionals.
