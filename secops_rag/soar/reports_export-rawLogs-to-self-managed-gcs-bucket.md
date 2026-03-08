# Export raw logs to self-managed Google Cloud Storage bucket

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/export-rawLogs-to-self-managed-gcs-bucket/  
**Scraped:** 2026-03-05T10:09:59.410527Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Export raw logs to self-managed Google Cloud Storage bucket
Supported in:
Google secops
SIEM
The Data Export API facilitates the bulk export of your security data from
Google Security Operations to a Google Cloud Storage bucket that you control.
This capability supports critical, long-term data retention, and supports historical
forensic analysis, and strict compliance requirements (such as, SOX, HIPAA,
GDPR).
Important
: After you enable the new enhanced API, you can't use the API to
access your old, existing jobs.
For more details on the Data Export API, see
Data Export API (enhanced)
The Data Export API provides a scalable and reliable solution for
point-in-time data exports and handles requests of up to 100 TB.
As a managed pipeline, it offers essential enterprise-grade features, including:
Automated retries on transient errors
Comprehensive job status monitoring
A full audit trail for each export job
The API logically partitions the exported data by date and time within your
Google Cloud Storage bucket.
This feature lets you build large-scale data offloading workflows.
Google SecOps manages the export process complexity to provide
stability and performance.
Key benefits
The Data Export API provides a resilient and auditable solution for managing the
lifecycle of your security data.
Reliability
: The service handles large-scale data transfers. The system
uses an exponential backoff strategy to automatically retry export jobs that
encounter transient issues (for example, temporary network problems), making
it resilient. If your export job fails due to a transient error, it
automatically retries several times. If a job fails permanently after all
retries, the system updates its status to
FINISHED_FAILURE
, and the API
response for that job contains a detailed error message that explains the
cause.
Comprehensive auditability
: To meet strict compliance and security
standards, the system captures every action related to an export job in an
immutable audit trail. This trail includes the creation, start, success, or
failure of every job, along with the user who initiated the action, a
timestamp, and the job parameters.
Optimized for performance and scale
: The API uses a robust job management
system. This system includes queuing and prioritization to provide platform
stability and prevent any single tenant from monopolizing resources.
Enhanced data integrity and accessibility
: The system automatically
organizes data into a logical directory structure within your Google
Cloud Storage bucket, which helps you locate and query specific time
windows for historical analysis.
Key terms and concepts
Export job
: A single, asynchronous operation to export a specific time
range of log data to a Google Cloud Storage bucket. The system tracks each
job with a unique
dataExportId
.
Job status
: The current state of an export job in its lifecycle (for
example,
IN_QUEUE
,
PROCESSING
,
FINISHED_SUCCESS
).
Google Cloud Storage bucket
: A user-owned Google Cloud Storage
bucket that serves as the destination for the exported data.
Log types
: These are the specific categories of logs you can export (for
example,
NIX_SYSTEM
,
WINDOWS_DNS
,
CB_EDR
). For more details, see the
list of all supported log types
.
Understand the exported data structure
When a job completes successfully, the system writes the data to your Google
Cloud Storage bucket. It uses a specific, partitioned directory structure to
simplify data access and querying.
Directory path structure:
gs://<gcs-bucket-name>/<export-job-name>/<logtype>/<event-time-bucket>/<epoch_execution_time>/<file-shard-name>.csv
gcs-bucket-name
: The name of your Google Cloud Storage bucket.
export-job-name
: The unique name of your export job.
logtype
: The name of the log type for the exported data.
event-time-bucket
: The hour range of the event timestamps of exported logs.
The format is a UTC timestamp:
year/month/day/UTC-timestamp
(where
UTC-timestamp
is
hour/minute/second
).
For example,
2025/08/25/01/00/00
refers to
UTC 01:00:00 AM, August 25, 2025
.
epoch-execution-time
: The Unix epoch time value, indicating when the
export job began.
file-shard-name
: The name of the sharded files containing raw logs. Each
file shard has an upper file size limit of 100 MB.
Performance and limitations
The service has specific limits to ensure platform stability and fair resource allocation.
Maximum data volume per job
: Each individual export job can request up to
100 TB of data. For larger datasets, we recommend breaking the export into
multiple jobs with smaller time ranges.
Concurrent jobs
: Each customer tenant can run or queue a maximum of 3
export jobs concurrently. The system rejects any new job creation request that
exceeds this limit.
Job completion times
: The volume of exported data determines job
completion times. A single job can take up to 18 hours.
Export format and data scope
: This API supports bulk, point-in-time
exports, with the following limitations and features:
Raw logs only
: You can only export raw logs, (not UDM logs, UDM events,
or detections). To export UDM data, see
Configure data export to
BigQuery in a self-managed Google Cloud
project
.
Data compression
: The API exports data as uncompressed text.
Prerequisites and architecture
This section outlines the system architecture and necessary requirements for
using the Data Export API and details the system architecture. Use this
information to verify that your environment is correctly configured.
Before you begin
Before using the Data Export API, complete these prerequisite steps to set up
your Google Cloud Storage destination and grant the necessary permissions.
Grant permissions to the API user
: To use the Data Export API, you need the following
IAM roles:
Chronicle API Admin
: Grants full permissions to
create, update, cancel, and view export jobs using the API. For more information, see the following:
chronicle.dataExports.fetchServiceAccountForDataExport
chronicle.dataExports.create
chronicle.dataExports.update
chronicle.dataExports.cancel
chronicle.dataExports.get
chronicle.dataExports.list
Chronicle API Viewer
: Grants read-only access to view job configurations and
history using the API. For more information, see the following:
chronicle.dataExports.fetchServiceAccountForDataExport
chronicle.dataExports.get
chronicle.dataExports.list
Create a Google Cloud Storage bucket
: In your Google Cloud
project, create a new Google Cloud Storage bucket (the destination for
your exported data) in the same region as your Google SecOps
tenant. Make it private to prevent unauthorized access. For details, see
Create a bucket
.
Grant permissions to the Service Account
: Grant the
Google SecOps Service Account, which is linked to your
Google SecOps tenant, the necessary IAM
roles to write data to your bucket.
Call the
FetchServiceAccountForDataExport
API endpoint to identify your
Google SecOps instance's unique Service Account. The
API returns the Service Account email.
Example request:
{
"parent"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
}
Example Response:
{
"service_account_email"
:
"service-1234@gcp-sa-chronicle.iam.gserviceaccount.com"
}
Grant the Google SecOps Service Account principal the
following IAM role for the destination Google
Cloud Storage bucket: This role lets the Google SecOps
service write exported data files to your Google Cloud Storage bucket.
Storage object administrator (roles/storage.objectAdmin)
Legacy bucket reader (roles/storage.legacyBucketReader)
For details, see
Grant access to the Google SecOps Service Account
.
Complete authentication
: The Data Export API authenticates your calls. 
To set up this authentication, follow the instructions in the following sections:
Authentication methods for Google Cloud services
Application default credentials
Key use cases
The Data Export API provides a suite of endpoints to create data export jobs and
manage the entire lifecycle of bulk data export. You perform all interactions
using API calls.
The following use cases describe how to create, monitor, and manage data
export jobs.
Core workflow
This section explains how to manage the lifecycle of your export jobs.
Create a new data export job
The system stores data export job specifications on the
parent resource
Google SecOps
instance. This instance is the source of the log data for the export job.
Identify the unique Service Account for your Google SecOps instance.
For details, see
FetchServiceAccountForDataExports
.
To start a new export, send a
POST
request to the
dataExports.create
endpoint.
For details, see
CreateDataExport
endpoint
.
Monitor data export job status
View data export job details and status for a specific export job, or set a filter to view certain types of jobs.
To view a specific export job, see
GetDataExport
.
To list certain types of data export jobs using a filter, see
ListDataExport
.
Manage queued jobs
You can modify or cancel a job when it is in the
IN_QUEUE
status.
To change parameters (such as the time range, list of log
types, or the destination bucket), see
UpdateDataExport
.
To cancel a queued job, see
CancelDataExport
.
Troubleshoot common issues
The API provides detailed error messages to help diagnose problems.
Canonical Code
Error Message
INVALID_ARGUMENT
INVALID_REQUEST: Invalid request parameter <Parameter1, Parameter2,..>. Please fix the request parameters and try again.
NOT_FOUND
BUCKET_NOT_FOUND: The destination Google Cloud Storage bucket <bucketName> does not exist. Please create the destination Google Cloud Storage bucket and try again.
NOT_FOUND
REQUEST_NOT_FOUND: The dataExportId:<dataExportId> does not exist. Please add a valid dataExportId and try again.
FAILED_PRECONDITION
BUCKET_INVALID_REGION: The Google Cloud Storage bucket <bucketId>'s region:<region1> is not the same region as the SecOps tenant region:<region2>. Please create the Google Cloud Storage bucket in the same region as SecOps tenant and try again.
FAILED_PRECONDITION
INSUFFICIENT_PERMISSIONS: The Service Account <P4SA> does not have
storage.objects.create
,
storage.objects.get
and
storage.buckets.get
permissions on the destination Google Cloud Storage bucket <bucketName>. Please provide the required access to the Service Account and try again.
FAILED_PRECONDITION
INVALID_UPDATE: The request status is in the <status> stage and can't be updated. You can only update the request if the status is in the IN_QUEUE stage.
FAILED_PRECONDITION
INVALID_CANCELLATION: The request status is in the <status> stage and can't be cancelled. You can only cancel the request if the status is in the IN_QUEUE stage.
RESOURCE_EXHAUSTED
CONCURRENT_REQUEST_LIMIT_EXCEEDED: Maximum concurrent requests limit <limit> reached for the request size <sizelimit>. Please wait for the existing requests to complete and try again.
RESOURCE_EXHAUSTED
REQUEST_SIZE_LIMIT_EXCEEDED: The estimated export volume: <estimatedVolume> for the request is greater than maximum allowed export volume: <allowedVolume> per request. Please try again with a request within the allowed export volume limit.
INTERNAL
INTERNAL_ERROR: An Internal error occurred. Please try again.
Need more help?
Get answers from Community members and Google SecOps professionals.
