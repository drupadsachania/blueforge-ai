# Collect Google Cloud DNS Threat Detector logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-dns-atd/  
**Scraped:** 2026-03-05T09:25:06.698023Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud DNS Threat Detector logs
Supported in:
Google secops
SIEM
This document explains how to ingest Google Cloud DNS Threat Detector logs to Google Security Operations using Google Cloud Storage V2.
DNS Armor, powered by Infoblox, is a fully managed service that provides DNS layer security for your Google Cloud workloads. Its advanced threat detector is designed to detect malicious activity at the earliest point in the attack chain, the DNS query, without adding operational complexity or performance overhead. After a threat is detected, you can gain actionable insights into DNS threats through Cloud Logging.
When you enable a DNS threat detector for a project, DNS Armor securely sends your internet bound DNS query logs to the Google Cloud based analysis engine powered by Infoblox. This engine uses a combination of threat intelligence feeds and AI based behavioral analysis to identify threats. Any malicious activity detected generates a DNS Armor threat log, which is then sent back to your project and written to Cloud Logging for you to view and act upon.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
GCP project with Cloud Storage API enabled.
Permissions to create and manage GCS buckets.
Permissions to manage IAM policies on GCS buckets.
Network Security API enabled in your project.
Required IAM roles to enable a DNS threat detector.
Permissions to view DNS threat logs:
resourcemanager.projects.get
,
resourcemanager.projects.list
,
networksecurity.dnsThreatDetectors.get
,
networksecurity.dnsThreatDetectors.list
or roles
roles/networksecurity.dnsThreatDetectorViewer
and
roles/logging.viewer
.
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
dns-threat-detector-logs
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
Create a DNS threat detector
This section describes how to create a DNS threat detector to monitor VPC networks for malicious, internet bound DNS activity.
You can have only one DNS threat detector enabled for a project.
Using Google Cloud Console
In the Google Cloud console, go to the
Advanced threat detection
page.
Click
Create DNS threat detector
.
Enter a name for your DNS threat detector.
Select
All VPC networks in the project
.
Click
Create
.
Using gcloud command-line tool
Alternatively, create a DNS threat detector using the
gcloud
command:
gcloud
beta
network-security
dns-threat-detectors
create
my-dns-threat-detector
\
--location
=
global
\
--project
=
PROJECT_ID
\
--provider
=
"infoblox"
Replace:
-
my-dns-threat-detector
: The name for your DNS threat detector.
-
PROJECT_ID
: Your project ID.
Configure Cloud Logging to export DNS Threat Detector logs to GCS
DNS Armor threat logs are written to Cloud Logging. You must configure a log sink to export these logs to your GCS bucket.
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
dns-threat-detector-to-gcs
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
dns-threat-detector-logs
) from the dropdown.
Click
Next
.
In the
Choose logs to include in sink
section, enter the following filter query:
resource
.
type
=
"networksecurity.googleapis.com/DnsThreatDetector"
logName
=
"projects/PROJECT_ID/logs/networksecurity.googleapis.com%2FDnsThreatDetector"
Replace
PROJECT_ID
with your GCP project ID.
Click
Next
.
Review the configuration and click
Create sink
.
Using gcloud command-line tool
Alternatively, create a log sink using the
gcloud
command:
gcloud
logging
sinks
create
dns-threat-detector-to-gcs
\
gs://dns-threat-detector-logs
\
--log-filter
=
'resource.type="networksecurity.googleapis.com/DnsThreatDetector" AND logName="projects/PROJECT_ID/logs/networksecurity.googleapis.com%2FDnsThreatDetector"'
\
--project
=
PROJECT_ID
Replace:
-
dns-threat-detector-logs
: Your GCS bucket name.
-
PROJECT_ID
: Your GCP project ID.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest Google Cloud DNS Threat Detector logs
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
GCP DNS Threat Detector Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Google Cloud DNS Threat Detector
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
gs://dns-threat-detector-logs/
Replace:
dns-threat-detector-logs
: Your GCS bucket name.
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
Click your bucket name (for example,
dns-threat-detector-logs
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
UDM mapping table
Log field
UDM mapping
Logic
record.jsonPayload.dnsQuery.responseCode, record.jsonPayload.dnsQuery.authAnswer, record.jsonPayload.dnsQuery.queryTime, record.jsonPayload.partnerId, record.jsonPayload.detectionTime, record.logName
additional.fields
Values copied to addition map, then merged as map entries with value.string_value if not empty
record.receiveTimestamp
metadata.collected_timestamp
Parsed as ISO8601 timestamp
metadata.event_type
Set to "NETWORK_CONNECTION" if has_principal and has_target, "STATUS_UPDATE" if has_principal, else "GENERIC_EVENT"
record.timestamp
metadata.event_timestamp
Parsed as ISO8601 timestamp
record.insertId
metadata.product_log_id
Value copied directly if not empty
record.jsonPayload.dnsQuery.rdata
network.dns.answers
Value copied to answer.data, then merged as array if not empty
record.jsonPayload.dnsQuery.queryName, record.jsonPayload.dnsQuery.queryType
network.dns.questions
questions.name from queryName, questions.type mapped from queryType string to integer, then merged as array if not empty
record.jsonPayload.dnsQuery.responseCode
network.dns.response_code
Mapped from string to integer using predefined table
record.jsonPayload.dnsQuery.protocol
network.ip_protocol
Value copied directly if not empty
record.jsonPayload.dnsQuery.sourceIp
principal.asset.ip
Value copied directly if not empty
record.jsonPayload.dnsQuery.sourceIp
principal.ip
Value copied directly if not empty
record.jsonPayload.dnsQuery.location
principal.location.country_or_region
Value copied directly if not empty
record.resource.labels.location
principal.location.name
Value copied directly if not empty
record.jsonPayload.dnsQuery.vmProjectNumber, record.jsonPayload.dnsQuery.projectNumber
principal.resource.attribute.labels
Values copied to addition map, then merged as map entries if not empty
record.jsonPayload.dnsQuery.vmInstanceId
principal.resource.id
Value copied directly if not empty
record.resource.labels.id
principal.resource.product_object_id
Value copied directly if not empty
record.resource.type
principal.resource.type
Value copied directly if not empty
security_result
Merged from built security_result map
record.jsonPayload.threatInfo.confidence
security_result.confidence
Mapped to LOW_CONFIDENCE if matches (?i)Low, MEDIUM_CONFIDENCE if (?i)Medium, HIGH_CONFIDENCE if (?i)High
record.jsonPayload.threatInfo.threatDescription
security_result.description
Value copied directly if not empty
record.jsonPayload.threatInfo.threatIndicatorType, record.jsonPayload.threatInfo.threatIndicator, record.jsonPayload.threatInfo.threatFeed, record.jsonPayload.threatInfo.category, record.jsonPayload.threatInfo.type, record.jsonPayload.threatInfo.threat, record.jsonPayload.threatInfo.severity, record.resource.labels.resource_container
security_result.detection_fields
Values copied to addition map, then merged as map entries if not empty
record.severity
security_result.severity
Mapped to LOW if (?i)Low, INFORMATIONAL if (?i)(Informational|Info), MEDIUM if (?i)Medium, CRITICAL if (?i)Critical, HIGH if (?i)High
record.jsonPayload.threatInfo.threatId
security_result.threat_id
Value copied directly if not empty
record.jsonPayload.dnsQuery.destinationIp
target.asset.ip
Value copied directly if not empty
record.jsonPayload.dnsQuery.destinationIp
target.ip
Value copied directly if not empty
metadata.vendor_name
Set to "Google Cloud"
metadata.product_name
Set to "Google Cloud DNS Threat Detector"
Need more help?
Get answers from Community members and Google SecOps professionals.
