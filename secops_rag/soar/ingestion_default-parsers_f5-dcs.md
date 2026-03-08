# Collect F5 Distributed Cloud Services logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs/  
**Scraped:** 2026-03-05T09:55:30.555985Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 Distributed Cloud Services logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 Distributed Cloud Services logs into Google Security Operations using Google Cloud Storage V2.
F5 Distributed Cloud Services is a SaaS-based security, networking, and application management platform that provides distributed cloud infrastructure, application delivery, API security, and web application firewall capabilities across multi-cloud and edge locations.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Google Cloud project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Privileged access to F5 Distributed Cloud console
Permissions to create Global Log Receiver objects in F5 Distributed Cloud
Create a Google Cloud Storage bucket
Go to the
Google Cloud console
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
f5-dcs-logs
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
Configure F5 Distributed Cloud to export to GCS
Add GCS bucket to firewall allowlist
F5 Distributed Cloud Global Log Receiver requires the following IP address ranges to be added to your firewall allowlist:
193.16.236.64/29
185.160.8.152/29
If your GCS bucket uses VPC Service Controls or firewall rules, add these IP ranges to your allowlist.
Create a Google Cloud service account for F5 Distributed Cloud
In the
Google Cloud console
, go to
IAM & Admin > Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter
f5-dcs-log-writer
(or a descriptive name)
Service account description
: Enter
Service account for F5 Distributed Cloud to write logs to GCS
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
Storage Object Admin
.
Click
Continue
.
Click
Done
.
Create a service account key
In the
Service Accounts
list, click on the service account you created (for example,
f5-dcs-log-writer
).
Go to the
Keys
tab.
Click
Add Key
>
Create new key
.
Select
JSON
as the key type.
Click
Create
.
The JSON key file is downloaded to your computer.
Save this file securely. You will need it in the next steps.
Grant IAM permissions on the GCS bucket
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name (for example,
f5-dcs-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
f5-dcs-log-writer@PROJECT_ID.iam.gserviceaccount.com
)
Assign roles
: Select
Storage Object Admin
Click
Save
.
Create Google Cloud credentials in F5 Distributed Cloud console
Sign in to the
F5 Distributed Cloud console
at
https://<tenant>.console.ves.volterra.io
.
Select the
Multi-Cloud Network Connect
service from the homepage.
Go to
Manage
>
Site Management
>
Cloud Credentials
.
Click
Add Cloud Credentials
.
In the
Metadata
section:
Name
: Enter a descriptive name (for example,
gcp-chronicle-logs
)
Description
(optional): Enter
Cloud Storage credentials for Google SecOps log export
In the
Cloud Credentials Type
section, select
GCP Credentials
.
Click
Configure
in the
GCP Credentials
field.
In the
Credential Type
dropdown, select
Service Account Credentials File
.
Click
Upload File
and select the JSON key file you downloaded in the previous steps.
Click
Apply
.
Click
Save and Exit
.
Create a Global Log Receiver
In the
F5 Distributed Cloud Console
, ensure you are in the
Multi-Cloud Network Connect
service.
Go to
Manage
>
Log Management
>
Global Log Receiver
.
Click
Add Global Log Receiver
.
In the
Metadata
section:
Name
: Enter a descriptive name (for example,
chronicle-gcs-receiver
)
Description
(optional): Enter
Global log receiver for Google SecOps SIEM
In the
Log Type
dropdown, select the log types you want to export:
Request Logs
: HTTP request/response logs with user, path, method, response codes
Security Events
: WAF events, DDoS, API Protection, Bot Defense events
Audit Logs
: Configuration changes via public APIs
DNS Request Logs
: DNS query logs
In the
Log Message Selection
dropdown, select one of the following:
Select logs from current namespace
: Sends logs from the current namespace only
Select logs from all namespaces
: Sends logs from all namespaces (recommended for comprehensive visibility)
Select logs in specific namespaces
: Sends logs from specified namespaces (click
Add item
to add namespace names)
In the
Receiver Configuration
dropdown, select
GCP Bucket Receiver
.
In the
GCP Bucket Name
field, enter the name of your GCS bucket (for example,
f5-dcs-logs
).
In the
GCP Cloud Credentials
dropdown, select the cloud credentials you created earlier (for example,
gcp-chronicle-logs
).
Optional: Expand
Show Advanced Fields
to configure batch options:
Batch Timeout Options
: Select
Timeout Seconds
and enter a value (default:
300
seconds)
Batch Max Events
: Select
Max Events
and enter a value between 32 and 2000 (leave unset for no limit)
Batch Bytes
: Select
Max Bytes
and enter a value between 4096 and 1048576 (default:
10485760
bytes / 10 MB)
Click
Save and Exit
.
Test the connection
In the
Global Log Receiver
list, locate the receiver you created (for example,
chronicle-gcs-receiver
).
Click the three dots (
...
) in the
Actions
column.
Select
Test Connection
.
Wait for the test to complete.
A message indicating successful connection should appear.
Verify logs in the GCS bucket
Go to
Cloud Storage
>
Buckets
in the GCP console.
Click on your bucket name (for example,
f5-dcs-logs
).
Verify that log files are being created in the bucket.
F5 Distributed Cloud organizes logs in the following folder structure:
YYYY/MM/DD/HH/
A folder is created for each day (YYYY/MM/DD)
Within each day folder, a subfolder is created for each hour (HH)
Every 5 minutes, new compressed gzip files are written to the hourly subfolder
Files are in NDJSON format (newline-delimited JSON)
Click on a gzip file to download and inspect the log format.
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
F5 DCS Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
F5 Distributed Cloud Services
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
gs://f5-dcs-logs/
Replace
f5-dcs-logs
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
The Google SecOps service account needs the
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click on your bucket name (for example,
f5-dcs-logs
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
UDM mapping table
Log Field
UDM Mapping
Logic
_id
metadata.product_log_id
Value copied directly
src
principal.namespace
Value copied directly
kubernetes_labels_app
target.resource.attribute.labels
Merged from app_label (derived from kubernetes_labels_app)
kubernetes_host
target.hostname
Value copied directly
kubernetes_container_name
target.resource.product_object_id
Value copied directly
bot_info.classification
security_result.detection_fields
Merged from bot_info_classification_label (derived from bot_info.classification)
bot_info.name
security_result.detection_fields
Merged from bot_info_name_label (derived from bot_info.name)
bot_info.type
security_result.detection_fields
Merged from bot_info_type_label (derived from bot_info.type)
timestamp
@timestamp
Parsed using date filter with RFC3339, UNIX, ISO8601
visitor_id
security_result.detection_fields
Merged from visitor_id_label (derived from visitor_id)
tag
security_result.detection_fields
Merged from tag_label (derived from tag)
action
security_result.action
Set to ALLOW if matches allow, BLOCK if matches deny
severity
security_result.severity
Set to HIGH if in error/warning; CRITICAL if critical; MEDIUM if notice; LOW if information/info
severity
security_result.severity_details
Value copied directly
api_endpoint
target.labels
Merged from api_endpoint_label (derived from api_endpoint)
app_firewall_name
principal.process.command_line
Value copied directly
app_type
security_result.detection_fields
Merged from about_app_type (derived from app_type)
as_org
security_result.detection_fields
Merged from about_as_org (derived from as_org)
asn
security_result.detection_fields
Merged from about_asn (derived from asn)
kubernetes.pod_id
security_result.detection_fields
Merged from about_pod_id (derived from kubernetes.pod_id)
kubernetes.pod_name
security_result.detection_fields
Merged from about_pod_name (derived from kubernetes.pod_name)
latitude
principal.location.region_latitude
Converted to float
longitude
principal.location.region_longitude
Converted to float
req_params
additional.fields
Merged from about_req_params (derived from req_params)
as_number
additional.fields
Merged from about_as_number (converted to string from as_number)
x_forwarded_for
intermediary.ip
Merged if valid IP
x_forwarded_for
security_result.about.resource.attribute.labels
Merged from x_forwarded_for_label if not IP
policy_hit.malicious_user_mitigate_action
security_result.detection_fields
Merged from malicious_user_label (derived from policy_hit.malicious_user_mitigate_action)
policy_hit.policy
security_result.about.resource.attribute.labels
Merged from policy_label (derived from policy_hit.policy)
policy_hit.policy_namespace
additional.fields
Merged from policy_namespace_label (derived from policy_hit.policy_namespace)
policy_hit.policy_rule
security_result.rule_name
Value copied directly
policy_hit.policy_rule_description
security_result.description
Value copied directly
policy_hit.policy_set
target.resource.name
Value copied directly
policy_hit.result
additional.fields
Merged from result_label (derived from policy_hit.result)
vhost_id
security_result.detection_fields
Merged from vhostlabel (derived from vhost_id)
messageid
security_result.detection_fields
Merged from messageid_label (derived from messageid)
sec_event_name
security_result.detection_fields
Merged from sec_event_name_label (derived from sec_event_name)
sec_event_type
security_result.detection_fields
Merged from sec_event_type_label (derived from sec_event_type)
vh_name
security_result.detection_fields
Merged from vhost_name_label (derived from vh_name)
tls_fingerprint
security_result.detection_fields
Merged from tls_fingerprint_label (derived from tls_fingerprint)
time
additional.fields
Merged from time_label (derived from time)
kubernetes.namespace_name
additional.fields
Merged from namespace_name_label (derived from kubernetes.namespace_name)
src_instance
additional.fields
Merged from src_instance_label (derived from src_instance)
violation_rating
additional.fields
Merged from violation_rating_label (derived from violation_rating)
req_size
additional.fields
Merged from req_size_label (converted to string from req_size)
rsp_code
additional.fields
Merged from rsp_code_label (converted to string from rsp_code)
rsp_code_class
additional.fields
Merged from rsp_code_class_label (converted to string from rsp_code_class)
rsp_size
additional.fields
Merged from rsp_size_label (converted to string from rsp_size)
original_path
additional.fields
Merged from original_path_label (derived from original_path)
req_path
target.url
Value copied directly
req_headers_size
additional.fields
Merged from req_headers_size_label (derived from req_headers_size)
recommended_action
additional.fields
Merged from recommended_action_label (derived from recommended_action)
enforcement_mode
additional.fields
Merged from enforcement_mode_label (derived from enforcement_mode)
src_ip
principal.ip, principal.asset.ip
Merged if matches IPv4 regex
host
principal.ip, principal.asset.ip
Merged if matches IPv4 regex
hostname
principal.hostname, principal.asset.hostname
Value copied directly if not empty or -
http_version
network.application_protocol_version
Value copied directly
http_version
network.application_protocol
Set to HTTP if contains HTTP, HTTPS if contains HTTPS
network
principal.nat_ip
Merged if matches IPv4 regex
dst_ip
target.ip, target.asset.ip
Merged if matches IPv4 regex
dst_port
target.port
Converted to integer
src_port
principal.port
Converted to integer
src_site
additional.fields
Merged from src_site_field (derived from src_site)
site
additional.fields
Merged from site_field (derived from site)
cluster_name
additional.fields
Merged from cluster_name_field (derived from cluster_name)
domain
principal.administrative_domain
Value copied directly
method
network.http.method
Value copied directly if not empty or N/A
namespace
target.namespace
Value copied directly
city
principal.location.city
Value copied directly
stream
security_result.detection_fields
Merged from stream_label (derived from stream)
region
principal.location.country_or_region
Value copied directly
user
principal.user.userid
Extracted from user using grok pattern for user_id
user_ip
target.ip, target.asset.ip
Merged from extracted user_ip
Cookie
additional.fields
Merged from cookie (derived from Cookie in req_headers)
X-F5-Request-Id
security_result.detection_fields
Merged from x_f5_request_id (derived from X-F5-Request-Id in req_headers)
X-Request-Id
security_result.detection_fields
Merged from request_id (derived from X-Request-Id in req_headers)
security_result
security_result
Merged directly
has_network, has_principal, has_target
metadata.event_type
Set to NETWORK_CONNECTION if all true; STATUS_UPDATE if has_principal true; else GENERIC_EVENT
metadata.vendor_name
Set to "F5_DCS"
metadata.product_name
Set to "F5 DCS"
intermediary
intermediary
Merged directly
Need more help?
Get answers from Community members and Google SecOps professionals.
