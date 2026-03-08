# Collect File Scanning Framework logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/file-scanning-framework/  
**Scraped:** 2026-03-05T09:24:16.434155Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect File Scanning Framework logs
Supported in:
Google secops
SIEM
This document explains how to ingest File Scanning Framework logs to Google Security Operations using Google Cloud Storage V2.
File Scanning Framework (FSF) is an open-source, modular recursive file scanning solution developed by Emerson Electric Co. FSF uses a client-server architecture to analyze files and generate detailed JSON scan results including file metadata, YARA signature matches, extracted sub-objects, and module-specific metadata.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
A deployed FSF server instance with write access to log directory
Root or sudo access to the FSF server host
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
fsf-logs-secops
).
Location type
Choose based on your needs (Region, Dual-region, Multi-region).
Location
Select the location (for example,
us-central1
).
Storage class
Standard (recommended for frequently accessed logs).
Access control
Uniform (recommended).
Protection tools
Optional: Enable object versioning or retention policy.
Click
Create
.
Configure FSF log output directory
FSF writes JSON scan results to a configurable log directory. Configure a dedicated directory for Google SecOps ingestion.
Connect to the FSF server host via SSH.
Open the FSF server configuration file:
sudo
nano
/opt/fsf/fsf-server/conf/config.py
Locate the
SCANNER_CONFIG
dictionary.
Update the
LOG_PATH
parameter to a dedicated directory:
SCANNER_CONFIG
=
{
'LOG_PATH'
:
'/var/log/fsf'
,
'YARA_PATH'
:
'/opt/fsf/fsf-server/yara/rules.yara'
,
'PID_PATH'
:
'/tmp/scanner.pid'
,
'EXPORT_PATH'
:
'/tmp'
,
'TIMEOUT'
:
60
,
'MAX_DEPTH'
:
10
}
Save and close the file.
Create the log directory with appropriate permissions:
sudo
mkdir
-p
/var/log/fsf
sudo
chown
-R
fsf:fsf
/var/log/fsf
sudo
chmod
755
/var/log/fsf
Restart the FSF server to apply changes:
sudo
systemctl
restart
fsf
Verify FSF is writing logs to the new directory:
ls
-lh
/var/log/fsf/
Install and configure Fluentd
Fluentd will tail FSF log files and ship them to Google Cloud Storage.
Install Fluentd
On the FSF server host, install Fluentd (td-agent):
curl
-fsSL
https://toolbelt.treasuredata.com/sh/install-ubuntu-jammy-td-agent4.sh
|
sh
Install the GCS output plugin:
sudo
td-agent-gem
install
fluent-plugin-gcs
Verify the plugin installation:
td-agent-gem
list
|
grep
fluent-plugin-gcs
Create GCP service account for Fluentd
In the
GCP Console
, go to
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
fsf-fluentd-shipper
.
Service account description
: Enter
Service account for Fluentd to ship FSF logs to GCS
.
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
Create service account key
From the
Service Accounts
list, click the service account (
fsf-fluentd-shipper
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
The JSON key file will be downloaded to your computer.
Transfer the key file to the FSF server host:
scp
/path/to/downloaded-key.json
user@fsf-server:/etc/td-agent/gcp-key.json
Set appropriate permissions on the key file:
sudo
chown
td-agent:td-agent
/etc/td-agent/gcp-key.json
sudo
chmod
600
/etc/td-agent/gcp-key.json
Grant IAM permissions on GCS bucket
Go to
Cloud Storage
>
Buckets
.
Click the bucket name (
fsf-logs-secops
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
fsf-fluentd-shipper@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Configure Fluentd
On the FSF server host, create a Fluentd configuration file:
sudo
nano
/etc/td-agent/td-agent.conf
Add the following configuration:
# Tail FSF JSON logs
<source>
    @type tail
    path /var/log/fsf/*.log
    pos_file /var/log/td-agent/fsf.log.pos
    tag fsf.scan
    read_from_head true
    <parse>
        @type json
        time_key timestamp
        time_format %Y-%m-%dT%H:%M:%S.%L%z
    </parse>
</source>

# Ship to Google Cloud Storage
<match fsf.scan>
    @type gcs
    project YOUR_GCP_PROJECT_ID
    keyfile /etc/td-agent/gcp-key.json
    bucket fsf-logs-secops
    object_key_format %{path}%{time_slice}_%{index}.%{file_extension}
    path fsf-logs/
    <buffer tag,time>
        @type file
        path /var/log/td-agent/buffer/gcs
        timekey 3600
        timekey_wait 10m
        timekey_use_utc true
        chunk_limit_size 10MB
    </buffer>
    <format>
        @type json
    </format>
    store_as json
    auto_create_bucket false
</match>
Replace
YOUR_GCP_PROJECT_ID
with your actual GCP project ID.
Save and close the file.
Create the buffer directory:
sudo
mkdir
-p
/var/log/td-agent/buffer/gcs
sudo
chown
-R
td-agent:td-agent
/var/log/td-agent/buffer
Restart Fluentd to apply the configuration:
sudo
systemctl
restart
td-agent
Enable Fluentd to start on boot:
sudo
systemctl
enable
td-agent
Verify Fluentd is running:
sudo
systemctl
status
td-agent
Verify log shipping
Check Fluentd logs for errors:
sudo
tail
-f
/var/log/td-agent/td-agent.log
Trigger a test FSF scan to generate logs:
echo
"test content"
>
/tmp/test.txt
/opt/fsf/fsf-client/fsf_client.py
/tmp/test.txt
--suppress-report
Wait 1-2 minutes for Fluentd to process and ship logs.
In the
GCP Console
, go to
Cloud Storage
>
Buckets
.
Click the bucket name (
fsf-logs-secops
).
Navigate to the
fsf-logs/
prefix.
Verify that JSON files are being created with timestamps.
Download and inspect a file to confirm it contains FSF scan results in JSON format.
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
FSF File Scanning Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
File Scanning Framework
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
secops-12345678@secops-gcp-prod.iam.gserviceaccount.com
Copy the email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://fsf-logs-secops/fsf-logs/
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
Click the bucket name (
fsf-logs-secops
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
Verify ingestion
Wait 10-15 minutes for the initial ingestion to complete.
In Google SecOps, go to
SIEM Settings
>
Feeds
.
Locate the feed (
FSF File Scanning Logs
).
Verify the
Status
shows as
Active
.
Click the feed name to view ingestion metrics.
Verify that
Events ingested
count is increasing.
Go to
Search
in Google SecOps.
Run a search query to verify FSF logs are being ingested:
metadata.log_type = "FILE_SCANNING_FRAMEWORK"
Verify that FSF scan results appear in the search results.
Troubleshooting
No logs appearing in GCS
Verify FSF is writing logs to
/var/log/fsf/
:
ls
-lh
/var/log/fsf/
tail
-f
/var/log/fsf/*.log
Check Fluentd logs for errors:
sudo
tail
-f
/var/log/td-agent/td-agent.log
Verify the GCP service account key is valid and has correct permissions.
Check that the bucket name in the Fluentd configuration matches the actual bucket name.
Fluentd permission errors
Verify the service account (
fsf-fluentd-shipper
) has
Storage Object Admin
role on the bucket.
Check that the key path in the Fluentd configuration is correct.
Verify the key file has correct ownership and permissions:
ls
-l
/etc/td-agent/gcp-key.json
Google SecOps not ingesting logs
Verify the Google SecOps service account has
Storage Object Viewer
role on the bucket.
Check that the bucket URI in the feed configuration is correct and includes the trailing slash.
Verify files exist in the GCS bucket at the specified prefix path.
Check the feed status in
SIEM Settings
>
Feeds
for error messages.
FSF logs not in expected format
Verify FSF is configured to write JSON output (default behavior).
Check that the Fluentd
<parse>
section is configured with
@type json
.
Inspect a log file manually to verify it contains valid JSON:
head
-n
1
/var/log/fsf/*.log
|
jq
.
UDM mapping table
Log field
UDM mapping
Logic
CompressType_label, compressed_parents
about.labels
Merged from CompressType_label (key "Compress Type", value from Object.EXTRACT_ZIP.Object_0.Compress Type if message contains "Compress Type") and compressed_parents (key "Compressed Parent Files", concatenated from Object.EXTRACT_ZIP.Object_0.META_VT_CACHE.vt_data.additional_info.compressed_parents)
Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.MD5, Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.MD5, Object.EXTRACT_SWF.META_BASIC_INFO.MD5, Object.EXTRACT_GZIP.META_BASIC_INFO.MD5, Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.MD5
intermediary.file.md5
Value from Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.MD5 if EXTRACT_EMBEDDED present, else Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.MD5 if EXTRACT_ZIP present, else Object.EXTRACT_SWF.META_BASIC_INFO.MD5 if EXTRACT_SWF present, else Object.EXTRACT_GZIP.META_BASIC_INFO.MD5 if EXTRACT_GZIP present, else Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.MD5
Object.EXTRACT_EMBEDDED.Object_0.Description
intermediary.file.mime_type
Value copied directly
Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.SHA1, Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.SHA1, Object.EXTRACT_SWF.META_BASIC_INFO.SHA1, Object.EXTRACT_GZIP.META_BASIC_INFO.SHA1, Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.SHA1
intermediary.file.sha1
Value from Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.SHA1 if EXTRACT_EMBEDDED present, else Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.SHA1 if EXTRACT_ZIP present, else Object.EXTRACT_SWF.META_BASIC_INFO.SHA1 if EXTRACT_SWF present, else Object.EXTRACT_GZIP.META_BASIC_INFO.SHA1 if EXTRACT_GZIP present, else Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.SHA1
Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.SHA256, Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.SHA256, Object.EXTRACT_SWF.META_BASIC_INFO.SHA256, Object.EXTRACT_GZIP.META_BASIC_INFO.SHA256, Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.SHA256
intermediary.file.sha256
Value from Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.SHA256 if EXTRACT_EMBEDDED present, else Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.SHA256 if EXTRACT_ZIP present, else Object.EXTRACT_SWF.META_BASIC_INFO.SHA256 if EXTRACT_SWF present, else Object.EXTRACT_GZIP.META_BASIC_INFO.SHA256 if EXTRACT_GZIP present, else Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.SHA256
Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.Size, Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.Size, Object.EXTRACT_SWF.META_BASIC_INFO.Size, Object.EXTRACT_GZIP.META_BASIC_INFO.Size, Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.Size
intermediary.file.size
Value from Object.EXTRACT_EMBEDDED.Object_0.META_BASIC_INFO.Size if EXTRACT_EMBEDDED present, else Object.EXTRACT_ZIP.Object_0.META_BASIC_INFO.Size if EXTRACT_ZIP present, else Object.EXTRACT_SWF.META_BASIC_INFO.Size if EXTRACT_SWF present, else Object.EXTRACT_GZIP.META_BASIC_INFO.Size if EXTRACT_GZIP present, else Object.EXTRACT_CAB.Object_0.META_BASIC_INFO.Size; stripped of trailing " .*" and converted to uinteger
Object.EXTRACT_ZIP.Object_0.META_VT_CACHE.vt_data.scan_id
intermediary.resource.id
Value copied directly
Object.EXTRACT_ZIP.Object_0.META_VT_CACHE.vt_data.permalink
intermediary.url
Value copied directly
Object.META_EMERSON_INFO.results
intermediary.user.email_addresses
Merged from matched_email in results array
Summary.Observations
metadata.description
Concatenated from array with ", " separator, leading comma removed
Scan Time
metadata.event_timestamp
Converted using date filter with format yyyy-MM-dd HH:mm:ss
Source
metadata.event_type
Set to "SCAN_FILE" if Source not empty, else "GENERIC_EVENT"
Object.META_VT_CACHE._id
metadata.product_log_id
Value copied directly
result.ad_data.message
network.http.response_code
Extracted as integer using grok pattern INT from result.ad_data.message
Source
principal.hostname
Value copied directly
Object.META_EMERSON_INFO.result_summary, Object.EXTRACT_ZIP.Object_0.META_VT_CACHE.vt_data.verbose_msg
security_result.summary
Set to Object.META_EMERSON_INFO.result_summary if present, else Object.EXTRACT_ZIP.Object_0.META_VT_CACHE.vt_data.verbose_msg
Filename
target.file.full_path
Value copied directly
Object.META_BASIC_INFO.MD5
target.file.md5
Value copied directly
Summary.Yara
target.file.mime_type
Extracted from first index of Summary.Yara, uppercased and "FT_" removed if Yara present, else set to "ZIP" if EXTRACT_ZIP present, "SWF" if EXTRACT_SWF present, "GZIP" if EXTRACT_GZIP present, "CAB" if EXTRACT_CAB present
Object.META_BASIC_INFO.SHA1, Object.META_VT_CACHE.SHA1
target.file.sha1
Value from Object.META_BASIC_INFO.SHA1 if not empty, else Object.META_VT_CACHE.SHA1
Object.META_BASIC_INFO.SHA256
target.file.sha256
Value copied directly
Object.META_BASIC_INFO.Size
target.file.size
Stripped of trailing " .*" and converted to uinteger
metadata.vendor_name
Set to "EMERSON"
metadata.product_name
Set to "FILE SCANNING FRAMEWORK"
Need more help?
Get answers from Community members and Google SecOps professionals.
