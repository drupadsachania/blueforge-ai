# Collect Google App Engine logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-app-engine/  
**Scraped:** 2026-03-05T09:56:36.329914Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google App Engine logs
Supported in:
Google secops
SIEM
This document explains how to ingest Google App Engine logs to Google Security Operations using Google Cloud Storage V2.
Google App Engine is a fully managed serverless platform for building and deploying web applications and APIs. App Engine automatically generates request logs for HTTP requests and application logs from your code. These logs are sent to Cloud Logging and can be exported to Cloud Storage for ingestion into Google Security Operations.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Logging sinks (roles/logging.configWriter)
An active App Engine application (standard or flexible environment)
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
appengine-logs-export
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
Configure Cloud Logging to export App Engine logs to GCS
Cloud Logging uses log sinks to route log entries to supported destinations, including Cloud Storage buckets. The sink's writer identity requires the Storage Object Creator role (roles/storage.objectCreator) on the destination bucket.
Create a Cloud Logging sink
In the
Google Cloud Console
, go to
Logging
>
Log Router
.
Click
Create sink
.
Provide the following configuration details:
Sink name
: Enter a descriptive name (for example,
appengine-to-gcs
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
: Select
appengine-logs-export
from the dropdown.
Click
Next
.
In the
Choose logs to include in sink
section, enter a filter query to select App Engine logs. The resource type must be exactly "gae_app".
For all App Engine logs (request and application logs):
resource
.
type
=
"gae_app"
For App Engine request logs only:
resource
.
type
=
"gae_app"
logName
=
"projects/PROJECT_ID/logs/appengine.googleapis.com/request_log"
For App Engine application logs (stdout/stderr):
resource
.
type
=
"gae_app"
(
logName
=
"projects/PROJECT_ID/logs/stdout"
OR
logName
=
"projects/PROJECT_ID/logs/stderr"
)
Replace
PROJECT_ID
with your GCP project ID.
Click
Next
.
Review the configuration and click
Create sink
.
Grant permissions to the sink writer identity
After creating the sink, you must grant the sink's writer identity the Storage Object Creator role on the destination bucket. The writer identity for the service account looks similar to: serviceAccount:service-123456789012@gcp-sa-logging.iam.gserviceaccount.com
In the
Log Router
page, locate the newly created sink.
Click the menu icon (three vertical dots) next to the sink name.
Select
View sink details
.
Copy the
Writer identity
(service account email).
Go to
Cloud Storage
>
Buckets
.
Click the bucket name (
appengine-logs-export
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the sink's writer identity (service account email).
Assign roles
: Select
Storage Object Creator
.
Click
Save
.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest App Engine logs
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
App Engine Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
GCP_APP_ENGINE
as the
Log type
.
Click
Get Service Account
.
A unique service account email will be displayed, for example:
chronicle
-
12345678
@chronicle
-
gcp
-
prod
.
iam
.
gserviceaccount
.
com
Copy this email address. You will use it in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs
:
//
appengine
-
logs
-
export
/
Cloud Logging organizes exported log files in directory hierarchies by log type and date. The log type can be a compound name like appengine.googleapis.com/request_log. Files are sharded and named with time periods (for example, 08:00:00_08:59:59_S0.json).
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
Go to
Cloud Storage
>
Buckets
.
Click on the bucket name (
appengine-logs-export
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
Understanding App Engine log structure
App Engine automatically sends both request logs and app logs to Cloud Logging. App Engine automatically emits logs for requests sent to your app, so there is no need to write request logs. This section covers how to write app logs.
App Engine request logs have log entries containing protoPayload fields which hold objects of type RequestLog with @type "type.googleapis.com/google.appengine.logging.v1.RequestLog". The resource type is "gae_app".
By default, the log payload is a text string stored in the textPayload field of the log entry. The strings appear as messages in the Logs Explorer and are associated with the App Engine service and version that emitted them.
To write structured logs, you write logs in the form of a single line of serialized JSON. When you provide a structured log as a JSON dictionary, some special fields are stripped from the jsonPayload and are written to the corresponding field in the generated LogEntry. For example, if your JSON includes a severity property, it is removed from the jsonPayload and appears instead as the log entry's severity.
Known limitations
When you route logs from log sink to Cloud Storage, the Cloud Storage destination only contains request logs. App Engine writes app logs to different folders.
Routed log entries are saved to Cloud Storage buckets in hourly batches. It might take from 2 to 3 hours before the first entries begin to appear.
In the App Engine flexible environment, logging works automatically. However, the logs are collected in a different format. Logs will not be bundled by requests, and logs from stdout and stderr are collected separately.
UDM mapping table
Log field
UDM mapping
Logic
jsonPayload.logger, taskTypeName, jsonPayload.@type, jsonPayload.backendTargetProjectNumber, jsonPayload.cacheDecision, resource.labels.version_id, resource.labels.module_id, logName, spanId, trace, protoPayload.@type, labels.clone_id, operation.producer
additional.fields
Merged with key-value labels created from each field
metadata
metadata
Renamed from metadata
receiveTimestamp
metadata.collected_timestamp
Parsed using date filter with RFC3339
metadata.event_type
Set to "USER_LOGIN" if has_principal, has_target, has_principal_user; "NETWORK_CONNECTION" if has_principal and has_target; "USER_UNCATEGORIZED" if not has_principal and has_target; "STATUS_UPDATE" if has_principal; "USER_UNCATEGORIZED" if has_principal_user; else "GENERIC_EVENT"
metadata.extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if has_principal, has_target, has_principal_user
insertId
metadata.product_log_id
Value copied directly
httpRequest.requestMethod,protoPayload.method
network.http.method
Value from httpRequest.requestMethod if not empty, else protoPayload.method
httpRequest.userAgent
network.http.parsed_user_agent
Converted to parseduseragent
httpRequest.status
network.http.response_code
Converted to string then to integer
httpRequest.userAgent
network.http.user_agent
Value copied directly
httpRequest.responseSize
network.received_bytes
Converted to uinteger
httpRequest.requestSize
network.sent_bytes
Converted to uinteger
principal
principal
Renamed from principal if not empty
protoPayload.host
principal.asset.hostname
Value copied directly
httpRequest.serverIp, protoPayload.ip
principal.asset.ip
Merged with server_ip from httpRequest.serverIp or protoPayload.ip
protoPayload.host
principal.hostname
Value copied directly
httpRequest.serverIp, protoPayload.ip
principal.ip
Merged with server_ip from httpRequest.serverIp or protoPayload.ip
protoPayload.appId
principal.resource.attribute.labels
Merged with appId_label containing key "appId" and value from the field
requestUser
principal.user.email_addresses
Merged with requestUser if matches email pattern
security_result
security_result
Merged from security_result
resource.labels.forwarding_rule_name
security_result.rule_labels
Merged with rule_label containing key "forwarding_rule_name" and value from the field
severity
security_result.severity
Set to severity if matches (?i)ERROR|CRITICAL, INFORMATIONAL if matches (?i)INFO, MEDIUM if matches (?i)WARN, LOW if matches (?i)DEBUG, else UNKNOWN_SEVERITY
jsonPayload.statusDetails
security_result.summary
Value copied directly
target
target
Renamed from target if not empty
resource.labels.backend_service_name
target.application
Value copied directly
httpRequest.remoteIp, jsonPayload.remoteIp
target.asset.ip
Merged with remote_ip extracted from httpRequest.remoteIp or jsonPayload.remoteIp
resource.labels.project_id
target.cloud.project.name
Value copied directly
httpRequest.remoteIp, jsonPayload.remoteIp
target.ip
Merged with remote_ip extracted from httpRequest.remoteIp or jsonPayload.remoteIp
resource.labels.zone
target.resource.attribute.cloud.availability_zone
Value copied directly
resource.labels.target_proxy_name, resource.labels.url_map_name
target.resource.attribute.labels
Merged with labels from each source
resource.type
target.resource.type
Value copied directly
httpRequest.requestUrl
target.url
Value copied directly
metadata.product_name
Set to "GCP_APP_ENGINE"
metadata.vendor_name
Set to "GCP"
Need more help?
Get answers from Community members and Google SecOps professionals.
