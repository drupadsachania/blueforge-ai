# Collect Chronicle SOAR Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chronicle-soar-audit/  
**Scraped:** 2026-03-05T09:52:00.717515Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Chronicle SOAR Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Chronicle SOAR Audit logs to Google Security Operations using Google Cloud Storage V2.
Google Security Operations SOAR (Security Orchestration, Automation and Response) enables security teams to automate response to threats by ingesting, grouping, and prioritizing alerts from detection tools to automatically execute playbooks and coordinate hands-on response. SOAR logs capture essential data from ETL, Playbook, and Python functions, including Python script execution, alert ingestion, and playbook performance.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A Google Cloud project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create and manage Cloud Logging sinks
Access to the Google Cloud project where Chronicle SOAR is deployed
Logs Viewer
(
roles/logging.viewer
) IAM role on your Google Cloud project
Logging Admin
(
roles/logging.admin
) IAM role to create log sinks
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
chronicle-soar-audit-logs
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
Enable SOAR log collection (Standalone deployments only)
To enable SOAR log export for standalone deployments, follow these steps:
In the Google Cloud console, go to
IAM & Admin
>
Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter
soar-logs-export-sa
Service account description
: Enter
Service account for exporting SOAR logs to Cloud Logging
Click
Create and Continue
.
In the
Grant this service account access to project
section:
Click
Select a role
.
Search for and select
Logs Writer
.
Click
Continue
.
Click
Done
.
In the
Service Accounts
list, locate the service account (
soar-logs-export-sa
).
Click more_vert
More
>
Manage Permissions
.
In the
Permissions
section, click
Grant Access
.
In the
Add principals
field, enter the following principal:
gke-init-backgroundservices@{SOAR-GCP-Project-Id}.iam.gserviceaccount.com
In the
Assign roles
section:
Click
Select a role
.
Search for and select
Service Account Token Creator
.
Click
Save
.
Copy the full email address of the service account (
soar-logs-export-sa@PROJECT_ID.iam.gserviceaccount.com
).
Submit a ticket to Google SecOps Support with the service account email to enable log export.
Configure Cloud Logging sink to export SOAR logs to GCS
Chronicle SOAR logs are written to Google Cloud Logging in the
chronicle-soar
namespace. You must create a log sink to route these logs to your GCS bucket.
In the Google Cloud console, go to
Logging
>
Log Router
.
Select the Google Cloud project where Chronicle SOAR is deployed.
Click
Create sink
.
In the
Sink details
panel, provide the following configuration details:
Sink name
: Enter
chronicle-soar-to-gcs
Sink description
: Enter
Export Chronicle SOAR audit logs to GCS for Chronicle SIEM ingestion
Click
Next
.
In the
Sink destination
panel:
In the
Select sink service
menu, select
Cloud Storage bucket
.
In the
Select Cloud Storage bucket
menu, select the bucket (
chronicle-soar-audit-logs
).
Click
Next
.
In the
Choose logs to include in sink
panel:
In the
Build inclusion filter
field, enter the following filter:
resource.labels.namespace_name="chronicle-soar"
This filter matches all SOAR logs from ETL, Playbook, and Python services.
Click
Preview logs
to verify the filter matches the expected log entries.
Click
Next
.
Optional: In the
Choose logs to filter out of sink
panel, you can add exclusion filters if needed. For most deployments, no exclusions are required.
Click
Create sink
.
Verify log export to GCS
Wait 5-10 minutes for logs to be exported to the GCS bucket.
In the Google Cloud console, go to
Cloud Storage
>
Buckets
.
Click on the bucket name (
chronicle-soar-audit-logs
).
Verify that log files are being created in the bucket. The files are organized by date and time:
chronicle-soar/YYYY/MM/DD/HH:MM:SS_<unique-id>.json
Click on a log file to preview its contents. Each file contains JSON-formatted log entries.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Get the service account email
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
Chronicle SOAR Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
CHRONICLE_SOAR_AUDIT
as the
Log type
.
Click
Get Service Account
.
A unique service account email is displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://chronicle-soar-audit-logs/chronicle-soar/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days)
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
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
chronicle-soar-audit-logs
).
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
Filter SOAR logs by service type
Chronicle SOAR logs are categorized by the service that generated the log. You can filter logs in Cloud Logging or create separate sinks for different log types.
Available log services
The following service types are available:
playbook
: Logs from playbook executions, including block execution, action results, and workflow status
python
: Logs from Python script execution, including integration actions, connectors, and jobs
etl
: Logs from alert ingestion and data transformation processes
Filter by service in Cloud Logging
To view logs from a specific service:
In the Google Cloud console, go to
Logging
>
Logs Explorer
.
Select the Google Cloud project where Chronicle SOAR is deployed.
Enter the following filter to view logs from a specific service:
resource.labels.namespace_name="chronicle-soar"
resource.labels.container_name="playbook"
Replace
playbook
with
python
or
etl
to view logs from other services.
Create separate sinks for different log types
To route different log types to separate GCS buckets or prefixes, create additional sinks with service-specific filters:
Follow the steps in the
Configure Cloud Logging sink to export SOAR logs to GCS
section.
In the
Build inclusion filter
field, use one of the following filters:
Playbook logs only:
resource.labels.namespace_name="chronicle-soar"
resource.labels.container_name="playbook"
Python logs only:
resource.labels.namespace_name="chronicle-soar"
resource.labels.container_name="python"
ETL logs only:
resource.labels.namespace_name="chronicle-soar"
resource.labels.container_name="etl"
Available log labels for filtering
Chronicle SOAR logs include labels that provide additional context for filtering and analysis.
Playbook labels
The following labels are available for playbook logs:
playbook_definition
: Unique identifier for the playbook definition
playbook_name
: Human-readable name of the playbook
block_name
: Name of the playbook block being executed
block_definition
: Unique identifier for the block definition
case_id
: Chronicle SOAR case identifier
correlation_id
: Unique identifier for tracing the entire playbook execution across services
integration_name
: Name of the integration being used
action_name
: Name of the action being executed
Python labels
The following labels are available for Python service logs:
Integration and Connector labels:
integration_name
: Name of the integration
integration_version
: Version of the integration
connector_name
: Name of the connector
connector_instance
: Instance identifier for the connector
Job labels:
integration_name
: Name of the integration
integration_version
: Version of the integration
job_name
: Name of the scheduled job
Action labels:
integration_name
: Name of the integration
integration_version
: Version of the integration
integration_instance
: Instance identifier for the integration
correlation_id
: Unique identifier for tracing execution
action_name
: Name of the action being executed
ETL labels
The following labels are available for ETL service logs:
correlation_id
: Unique identifier for tracing alert ingestion flow
Use correlation_id for complete tracing
The
correlation_id
label is available in both playbook and Python service logs. Use this label to retrieve all associated logs from an entire playbook execution:
In the Google Cloud console, go to
Logging
>
Logs Explorer
.
Enter the following filter:
resource.labels.namespace_name="chronicle-soar"
labels.correlation_id="<correlation-id-value>"
Replace
<correlation-id-value>
with the actual correlation ID from a log entry.
This filter returns all logs from both playbook and Python services for the complete execution trace.
UDM mapping table
Log Field
UDM Mapping
Logic
module, screenSize, activityItem, modificationTimeUnixTimeInMs
additional.fields
Merged labels created from each field if present
user, operation
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if user not empty and operation is "Login"
creationTimeUnixTimeInMs
metadata.event_timestamp
Parsed as UNIX_MS timestamp
user, operation, address
metadata.event_type
Set to "USER_LOGIN" if user not empty and operation "Login"; "USER_RESOURCE_ACCESS" if user not empty; "STATUS_UNCATEGORIZED" if address empty; else "GENERIC_EVENT"
operation
metadata.product_event_type
Value copied directly
id
metadata.product_log_id
Converted to string
browser
network.http.parsed_user_agent
Converted to parsed user agent
browser
network.http.user_agent
Value copied directly
address
principal.hostname
Set if address does not match IP pattern
address
principal.ip
Extracted IP using grok pattern
source
principal.resource.resource_subtype
Value copied directly
user
principal.user.userid
Value copied directly
ContactEmails
security_result.about.user.email_addresses
Extracted email addresses using grok pattern
ContactPhone
security_result.about.user.phone_numbers
Value copied directly
ContactName
security_result.about.user.user_display_name
Value copied directly
Name
security_result.about.user.userid
Value copied directly
currentActivity, previousActivity
security_result.detection_fields
Merged labels from currentActivity and previousActivity if present
userGuid
target.user.product_object_id
Value copied directly
metadata.product_name
Set to "CHRONICLE_SOAR_AUDIT"
metadata.vendor_name
Set to "CHRONICLE_SOAR_AUDIT"
Need more help?
Get answers from Community members and Google SecOps professionals.
