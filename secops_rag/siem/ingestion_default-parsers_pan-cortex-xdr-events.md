# Collect Palo Alto Cortex XDR Events logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-cortex-xdr-events/  
**Scraped:** 2026-03-05T09:27:15.753762Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Cortex XDR Events logs
Supported in:
Google secops
SIEM
This document explains how to ingest Palo Alto Cortex XDR Event logs to
Google Security Operations using Google Cloud Storage. The parser extracts
security event data from Palo Alto Networks Cortex XDR JSON logs. It normalizes
the data into the Unified Data Model (UDM) by mapping fields, converting data
types, and enriching events with metadata like vendor, product, and event types
based on conditional logic tied to
event_type
and
event_sub_type
fields. It
also handles network connections, file and registry operations, process
information, and user activity.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Google Cloud Storage is set up and active in your Google Cloud environment
Privileged access to Google Cloud and appropriate permissions
Privileged access to Palo Alto Cortex XDR
Create a Google Cloud Storage Bucket
Sign in to the Google Cloud console.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
On the
Create a bucket
page, enter your bucket information. After each of the following steps, click
Continue
to proceed to the next step:
In the
Get started
section, do the following:
Enter a unique name that meets the bucket name requirements (for example,
cortex-xdr-events-secops
).
To enable hierarchical namespace, click the expander arrow to expand the
Optimize for file oriented and data-intensive workloads
section, and then select
Enable Hierarchical namespace on this bucket
.
To add a bucket label, click the expander arrow to expand the
Labels
section.
Click
Add label
and specify a key and a value for your label.
In the
Choose where to store your data
section, do the following:
Select a
Location type
.
Use the location type's menu to select a
Location
where object data within your bucket will be permanently stored.
To set up cross-bucket replication, expand the
Set up cross-bucket replication
section.
In the
Choose a storage class for your data
section, either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management of your bucket's data.
In the
Choose how to control access to objects
section, select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the
Data encryption
expander arrow, and select a
Data encryption method
.
Click
Create
.
Configure Cortex XDR Event Forwarding
Sign in to the
Cortex XDR
web UI.
Go to
Settings
>
Configurations
>
Data Management
>
Event Forwarding
.
Activate the licenses in the
Activation
section.
Enable
GB Event Forwarding
to export parsed logs for Cortex XDR Pro per GB to an external SIEM for storage.
Enable
Endpoints Event Forwarding
to export raw endpoint data for Cortex XDR Pro EP and Cloud Endpoints.
Save
the selection.
Copy
the storage path displayed.
Generate
and
download
the Service Account JSON WEB TOKEN, which contains the access key.
Save
it in a
secure location
.
Configure Google Cloud Secret Manager
Sign in to your
GCP
.
Go to the
Secret Manager
page.
If this your first time, you'll be prompted to
Enable
the
Secret Manager API
.
Create a secret called
EVENT_FRWD_CRTX_KEY
and copy the contents of the JSON
xdr_sa_key.json
you downloaded as the value of the secret.
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
PANW Cortex XDR Event Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Palo Alto Cortex XDR Events
as the
Log type
.
Click
Get Service Account
as the
Chronicle Service Account
.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Google Cloud storage bucket URL (for example,
gs://cortex-xdr-events-secops
/). This URL must end with a trailing forward slash (/).
Source deletion options
: Select a deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
After the Feed is created, find it on the
Feeds
list and click the three action dots to the right side of the line.
Select
Disable Feed
.
Configure Secret JSON Access to Cloud Storage
Sign in to your
GCP
.
Go to the
Secret Manager
page.
Select the secret
EVENT_FRWD_CRTX_KEY
.
Go to
Permissions
tab.
Provide the
Storage Object Admin
and
Storage Legacy Bucket Reader
access to the bucket
cortex-xdr-events-secops
created previously.
Configure Google SecOps Permissions for Cloud Storage
Go to
IAM & Admin
>
IAM
.
Locate the
Chronicle Service Account
.
Grant the
Storage Object Viewer
(roles/storage.objectViewer) access to the bucket
cortex-xdr-events-secops
created previously.
Configure PANW Cortex XDR Events logs ingestion to Project Cloud Storage
In Google Cloud, go to
APIs & Services
>
Library
.
Enable the
Cloud Run
and
Artifact Registry
APIs.
Open
Cloud Shell
by clicking the icon in the top navigation bar.
Download a custom code using the following command:
git
clone
https://github.com/PaloAltoNetworks/google-cloud-cortex-chronicle.git
Go to the directory by running the following command:
cd
google-cloud-cortex-chronicle/
Open the file
env.properties
with an editor like
vi
.
Provide the following configuration details:
REGION=us-central1 # Update according to your project region
REPO_NAME=panw-chronicle
IMAGE_NAME=sync_cortex_bucket
GCP_PROJECT_ID=chrxxxxxxxxx # Update according to your project ID
JOB_NAME=cloud-run-job-cortex-data-sync # The Cloud Job name 
ROJECT_NUMBER=80xxxxx9 # Update according to your project number
# JOB ENV VARIABLES
SRC_BUCKET=xdr-us-xxxxx-event-forwarding # Update with the Cortex XDR GCS bucket name
DEST_BUCKET=cortex-xdr-events-secops # Update with the GCS name of the bucket you created
SECRET_NAME=EVENT_FRWD_CRTX_KEY # Need to match the secret you created
JOB_SCHEDULE_MINS=30
Provide necessary permissions to the
deploy.sh
script:
chmod
744
deploy.sh
Run the
deploy.sh
script:
./deploy.sh
Identify the used Cloud Job service account from the script output.
Grant the
Cloud Job
service account
Secret Manager Secret Ancestor
permission to access the Secret you created before (as in our example,
EVENT_FRWD_CRTX_KEY
).
Go to
Secret Manager
>
EVENT_FRWD_CRTX_KEY (secret)
>
Permissions
.
In the Google SecOps platform, go to
SIEM Settings
>
Feeds
>
XDR Events Feed Name
>
Enable Feed
.
UDM mapping table
Log Field
UDM Mapping
Logic
action_file_path
target.file.full_path
Directly mapped
action_file_size
target.file.size
Directly mapped and converted to unsigned integer
action_local_ip
principal.ip
Directly mapped and merged with other IP addresses
action_local_port
principal.port
Directly mapped and converted to integer
action_module_path
target.process.file.full_path
Directly mapped
action_network_connection_id
network.session_id
Directly mapped
action_network_protocol
network.ip_protocol
Renamed to
protocol_number_src
, parsed using
parse_ip_protocol.include
, and mapped to
network.ip_protocol
action_process_image_command_line
target.process.command_line
Directly mapped
action_process_image_md5
target.process.file.md5
Directly mapped
action_process_image_path
target.process.file.full_path
Directly mapped
action_process_image_sha256
target.process.file.sha256
Directly mapped
action_process_os_pid
target.process.pid
Directly mapped and converted to string
action_process_user_sid
target.user.windows_sid
Directly mapped
action_process_username
target.user.userid
,
target.administrative_domain
Lowercased, parsed for domain and user, and mapped accordingly
action_registry_data
target.registry.registry_value_data
Directly mapped
action_registry_key_name
target.registry.registry_key
Directly mapped
action_registry_value_name
target.registry.registry_value_name
Directly mapped
action_remote_ip
target.ip
Directly mapped and merged with other IP addresses
action_remote_port
target.port
Directly mapped and converted to integer
action_total_download
network.received_bytes
Directly mapped and converted to unsigned integer
action_total_upload
network.sent_bytes
Directly mapped and converted to unsigned integer
agent_hostname
principal.hostname
,
observer.hostname
Lowercased and mapped
agent_ip_addresses
observer.ip
Parsed as JSON, split into individual IPs, and merged
agent_os_sub_type
target.platform_version
Directly mapped
event_id
metadata.product_log_id
Directly mapped
event_sub_type
metadata.product_event_type
Converted to string and used for conditional mapping of
metadata.event_type
and
metadata.product_event_type
event_timestamp
metadata.event_timestamp
,
timestamp
Converted to string, parsed as UNIX_MS timestamp, and mapped
event_type
metadata.event_type
Converted to string and used for conditional mapping of
metadata.event_type
and
metadata.product_event_type
os_actor_process_command_line
principal.process.command_line
Directly mapped
os_actor_process_image_md5
principal.process.file.md5
Directly mapped
os_actor_process_image_path
principal.process.file.full_path
Directly mapped
os_actor_process_image_sha256
principal.process.file.sha256
Directly mapped
os_actor_process_instance_id
principal.process.product_specific_process_id
Prefixed with "PAN:" and mapped
os_actor_process_os_pid
principal.process.pid
Converted to string and mapped
os_actor_primary_user_sid
principal.user.windows_sid
Mapped if it starts with "S-" or "s-"
os_actor_primary_username
principal.user.userid
,
principal.administrative_domain
Lowercased, parsed for domain and user, and mapped accordingly
_action
security_result.action
Merged into
_security_result
and then mapped
metadata.log_type
metadata.log_type
Hardcoded to "PAN_CORTEX_XDR_EVENTS"
metadata.product_name
metadata.product_name
Hardcoded to "Cortex XDR"
metadata.vendor_name
metadata.vendor_name
Hardcoded to "PAN"
target.platform
target.platform
Set to "WINDOWS" if
agent_os_sub_type
contains "Windows"
Need more help?
Get answers from Community members and Google SecOps professionals.
