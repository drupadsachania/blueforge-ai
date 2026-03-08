# Collect Fortinet FortiEDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiedr/  
**Scraped:** 2026-03-05T09:56:19.662286Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiEDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest Fortinet FortiEDR logs to Google Security Operations using Google Cloud Storage V2 or Bindplane agent.
Fortinet FortiEDR is an endpoint detection and response solution that provides real-time protection, automated incident response, and threat intelligence for endpoints across an organization.
Collection method differences
This guide provides two collection methods:
Option 1: Syslog via Bindplane agent
: FortiEDR sends syslog messages to Bindplane agent, which forwards logs to Google SecOps. Recommended for real-time log ingestion with minimal infrastructure.
Option 2: Syslog to GCS via Cloud Function
: FortiEDR sends syslog messages to a Cloud Function, which writes logs to GCS for Google SecOps ingestion. Recommended for centralized log storage and batch processing.
Choose the method that best fits your infrastructure and requirements.
Option 1: Collect Fortinet FortiEDR logs using Bindplane agent
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows Server 2016 or later, or Linux host with systemd
Network connectivity between Bindplane agent and Fortinet FortiEDR Central Manager
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Fortinet FortiEDR management console
FortiEDR version 5.0 or later
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Click
Download
to download the
ingestion authentication file
.
Save the file securely on the system where Bindplane agent will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Install Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/fortiedr
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
FORTINET_FORTIEDR
raw_log_field
:
body
ingestion_labels
:
env
:
production
service
:
pipelines
:
logs/fortiedr_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/fortiedr
Configuration parameters
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on. Use
0.0.0.0:514
to listen on all interfaces on port 514.
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Customer ID from the previous step.
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
ingestion_labels
: Optional labels in YAML format.
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart Bindplane agent to apply the changes
Linux
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
Windows
Choose one of the following options:
Using Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Using Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Fortinet FortiEDR syslog forwarding
Configure syslog destination
Sign in to the
FortiEDR Central Manager
console.
Go to
Administration
>
Export Settings
>
Syslog
.
Click the
Define New Syslog
button.
In the
Syslog Name
field, enter a descriptive name (for example,
Chronicle-Integration
).
In the
Host
field, enter the IP address of the Bindplane agent host.
In the
Port
field, enter
514
.
In the
Protocol
dropdown, select
TCP
.
In the
Format
dropdown, select
Semicolon
(default format with semicolon-separated fields).
Click the
Test
button to test the connection to the Bindplane agent.
Verify the test is successful.
Click the
Save
button to save the syslog destination.
Enable syslog notifications per event type
In the
Syslog
page, select the syslog destination row you just created.
In the
NOTIFICATIONS
pane on the right, use the sliders to enable or disable the destination per event type:
System events
: Enable to send FortiEDR system health events.
Security events
: Enable to send security event aggregations.
Audit trail
: Enable to send audit log events.
For each enabled event type, click the button on the right of the event type.
Select the checkboxes for the fields you want to include in the syslog messages.
Click
Save
.
Configure playbook notifications
Syslog messages are only sent for security events that occur on devices assigned to a Playbook policy with the
Send Syslog Notification
option enabled.
Go to
Security Settings
>
Playbooks
.
Select the playbook policy that applies to the devices you want to monitor (for example,
Default Playbook
).
In the
Notifications
section, locate the
Syslog
row.
Enable the
Send Syslog Notification
option by selecting the checkboxes for the event classifications you want to send:
Malicious
: Security events classified as malicious.
Suspicious
: Security events classified as suspicious.
PUP
: Potentially unwanted programs.
Inconclusive
: Events with inconclusive classification.
Likely Safe
: Events classified as likely safe (optional).
Click
Save
.
Option 2: Collect Fortinet FortiEDR logs using GCS
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Privileged access to Fortinet FortiEDR management console
FortiEDR version 5.0 or later
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
fortiedr-logs
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
Create service account for Cloud Run function
The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.
Create service account
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
fortiedr-syslog-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect FortiEDR syslog logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
Click
Select a role
.
Search for and select
Storage Object Admin
.
Click
+ Add another role
.
Search for and select
Cloud Run Invoker
.
Click
+ Add another role
.
Search for and select
Cloud Functions Invoker
.
Click
Continue
.
Click
Done
.
These roles are required for:
Storage Object Admin
: Write logs to GCS bucket and manage state files
Cloud Run Invoker
: Allow Pub/Sub to invoke the function
Cloud Functions Invoker
: Allow function invocation
Grant IAM permissions on GCS bucket
Grant the service account write permissions on the GCS bucket:
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
: Enter the service account email (for example,
fortiedr-syslog-collector-sa@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create Pub/Sub topic
Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.
In the
GCP Console
, go to
Pub/Sub
>
Topics
.
Click
Create topic
.
Provide the following configuration details:
Topic ID
: Enter
fortiedr-syslog-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to receive syslog
The Cloud Run function will receive syslog messages from FortiEDR via HTTP and write them to GCS.
In the
GCP Console
, go to
Cloud Run
.
Click
Create service
.
Select
Function
(use an inline editor to create a function).
In the
Configure
section, provide the following configuration details:
Setting
Value
Service name
fortiedr-syslog-collector
Region
Select region matching your GCS bucket (for example,
us-central1
)
Runtime
Select
Python 3.12
or later
In the
Trigger (optional)
section:
Click
+ Add trigger
.
Select
HTTPS
.
In
Authentication
, select
Allow unauthenticated invocations
.
Click
Save
.
Scroll to and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select the service account (
fortiedr-syslog-collector-sa
).
Go to the
Containers
tab:
Click
Variables & Secrets
.
Click
+ Add variable
for each environment variable:
Variable Name
Example Value
Description
GCS_BUCKET
fortiedr-logs
GCS bucket name
GCS_PREFIX
fortiedr-syslog
Prefix for log files
In the
Variables & Secrets
section, scroll to
Requests
:
Request timeout
: Enter
60
seconds.
Go to the
Settings
tab:
In the
Resources
section:
Memory
: Select
256 MiB
or higher.
CPU
: Select
1
.
In the
Revision scaling
section:
Minimum number of instances
: Enter
0
.
Maximum number of instances
: Enter
10
(or adjust based on expected load).
Click
Create
.
Wait for the service to be created (1-2 minutes).
After the service is created, the
inline code editor
will open automatically.
Add function code
Enter
main
in the
Entry point
field.
In the inline code editor, create two files:
First file:
main.py:
import
functions_framework
from
google.cloud
import
storage
import
json
import
os
from
datetime
import
datetime
,
timezone
from
flask
import
Request
# Initialize Storage client
storage_client
=
storage
.
Client
()
# Environment variables
GCS_BUCKET
=
os
.
environ
.
get
(
'GCS_BUCKET'
)
GCS_PREFIX
=
os
.
environ
.
get
(
'GCS_PREFIX'
,
'fortiedr-syslog'
)
@functions_framework
.
http
def
main
(
request
:
Request
):
"""
Cloud Run function to receive syslog messages from FortiEDR and write to GCS.
Args:
request: Flask Request object containing syslog message
"""
if
not
GCS_BUCKET
:
print
(
'Error: Missing GCS_BUCKET environment variable'
)
return
(
'Missing GCS_BUCKET environment variable'
,
500
)
try
:
# Get request body
request_data
=
request
.
get_data
(
as_text
=
True
)
if
not
request_data
:
print
(
'Warning: Empty request body'
)
return
(
'Empty request body'
,
400
)
# Parse syslog messages (one per line)
lines
=
request_data
.
strip
()
.
split
(
'
\n
'
)
if
not
lines
:
print
(
'Warning: No syslog messages found'
)
return
(
'No syslog messages found'
,
400
)
# Get GCS bucket
bucket
=
storage_client
.
bucket
(
GCS_BUCKET
)
# Write to GCS as NDJSON
now
=
datetime
.
now
(
timezone
.
utc
)
timestamp
=
now
.
strftime
(
'%Y%m
%d
_%H%M%S_
%f
'
)
object_key
=
f
"
{
GCS_PREFIX
}
/logs_
{
timestamp
}
.ndjson"
blob
=
bucket
.
blob
(
object_key
)
# Convert each line to JSON object with raw syslog message
records
=
[]
for
line
in
lines
:
if
line
.
strip
():
records
.
append
({
'raw'
:
line
.
strip
(),
'timestamp'
:
now
.
isoformat
()})
ndjson
=
'
\n
'
.
join
([
json
.
dumps
(
record
,
ensure_ascii
=
False
)
for
record
in
records
])
+
'
\n
'
blob
.
upload_from_string
(
ndjson
,
content_type
=
'application/x-ndjson'
)
print
(
f
"Wrote
{
len
(
records
)
}
records to gs://
{
GCS_BUCKET
}
/
{
object_key
}
"
)
return
(
f
"Successfully processed
{
len
(
records
)
}
records"
,
200
)
except
Exception
as
e
:
print
(
f
'Error processing syslog:
{
str
(
e
)
}
'
)
return
(
f
'Error processing syslog:
{
str
(
e
)
}
'
,
500
)
Second file:
requirements.txt:
functions
-
framework
==
3
.*
google
-
cloud
-
storage
==
2
.*
flask
==
3
.*
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
After deployment, go to the
Trigger
tab and copy the
Trigger URL
(for example,
https://fortiedr-syslog-collector-abc123-uc.a.run.app
).
Configure Fortinet FortiEDR syslog forwarding to Cloud Function
Configure syslog destination
Sign in to the
FortiEDR Central Manager
console.
Go to
Administration
>
Export Settings
>
Syslog
.
Click the
Define New Syslog
button.
In the
Syslog Name
field, enter a descriptive name (for example,
Chronicle-GCS-Integration
).
In the
Host
field, enter the Cloud Function trigger URL hostname (for example,
fortiedr-syslog-collector-abc123-uc.a.run.app
).
In the
Port
field, enter
443
.
In the
Protocol
dropdown, select
TCP
.
In the
Format
dropdown, select
Semicolon
(default format with semicolon-separated fields).
Click the
Test
button to test the connection to the Cloud Function.
Verify the test is successful.
Click the
Save
button to save the syslog destination.
Enable syslog notifications per event type
In the
Syslog
page, select the syslog destination row you just created.
In the
NOTIFICATIONS
pane on the right, use the sliders to enable or disable the destination per event type:
System events
: Enable to send FortiEDR system health events.
Security events
: Enable to send security event aggregations.
Audit trail
: Enable to send audit log events.
For each enabled event type, click the button on the right of the event type.
Select the checkboxes for the fields you want to include in the syslog messages.
Click
Save
.
Configure playbook notifications
Syslog messages are only sent for security events that occur on devices assigned to a Playbook policy with the
Send Syslog Notification
option enabled.
Go to
Security Settings
>
Playbooks
.
Select the playbook policy that applies to the devices you want to monitor (for example,
Default Playbook
).
In the
Notifications
section, locate the
Syslog
row.
Enable the
Send Syslog Notification
option by selecting the checkboxes for the event classifications you want to send:
Malicious
: Security events classified as malicious.
Suspicious
: Security events classified as suspicious.
PUP
: Potentially unwanted programs.
Inconclusive
: Events with inconclusive classification.
Likely Safe
: Events classified as likely safe (optional).
Click
Save
.
Test the integration
In the
FortiEDR Central Manager
console, go to
Administration
>
Export Settings
>
Syslog
.
Select the syslog destination row.
Click the
Test
button to send a test message.
Go to
Cloud Run
>
Services
in the GCP Console.
Click on the function name (
fortiedr-syslog-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for:
Wrote X records to gs://fortiedr-logs/fortiedr-syslog/logs_YYYYMMDD_HHMMSS_MMMMMM.ndjson
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
fortiedr-syslog/
).
Verify that a new
.ndjson
file was created with the current timestamp.
If you see errors in the logs:
Empty request body
: FortiEDR is not sending data to the Cloud Function
Missing GCS_BUCKET environment variable
: Check environment variables are set
Permission denied
: Verify service account has Storage Object Admin role on bucket
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Configure a feed in Google SecOps to ingest Fortinet FortiEDR logs
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
FortiEDR Syslog Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Fortinet FortiEDR
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
gs://fortiedr-logs/fortiedr-syslog/
Replace:
fortiedr-logs
: Your GCS bucket name.
fortiedr-syslog
: Optional prefix/folder path where logs are stored (leave empty for root).
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
UDM mapping table
Log field
UDM mapping
Logic
Country
target.location.country_or_region
Value copied directly if not N/A or empty
srccountry
principal.location.country_or_region
Value copied directly if not Reserved or empty
dstcountry
target.location.country_or_region
Value copied directly if not empty
srcip
principal.ip
Value copied directly
dstip
target.ip
Value copied directly if not N/A
Destination
target.ip
Extracted as IP from Destination if valid
dst
target.ip
Extracted as IP from dst if valid
srcmac
principal.mac
Value copied directly
dstosname
target.platform
Set to LINUX if matches LINUX; WINDOWS if matches WINDOWS; MAC if matches MAC
srcport
principal.port
Converted to integer
dstport
target.port
Converted to integer
spt
principal.port
Converted to integer
dpt
target.port
Converted to integer
sessionid
network.session_id
Value copied directly
sentbyte
network.sent_bytes
Converted to unsigned integer
rcvdbyte
network.received_bytes
Converted to unsigned integer
duration
network.session_duration.seconds
Converted to integer
action
security_result.summary
Value copied directly
level
security_result.severity_details
Set to "level: %{level}"
policyid
security_result.rule_id
Value copied directly
policyname
security_result.rule_name
Value copied directly
policytype
security_result.rule_type
Value copied directly
service
target.application
Value copied directly
intermediary_ip
target.ip
Value copied directly if message_type is Audit or loginStatus not empty
intermediary
intermediary
Value copied directly
devname
target.hostname
Value copied directly
server_host
target.hostname
Value copied directly if message_type is Audit or loginStatus not empty
server_host
intermediary.hostname
Value copied directly as label if not Audit or loginStatus
deviceInformation
target.resource.name, target.resource.resource_type
Extracted device_name and set resource_type to DEVICE
component_name
additional.fields
Set as label with key "Component Name"
process_name
principal.application
Value copied directly
Process Path
target.file.full_path
Value copied directly
asset_os
target.platform
Set to WINDOWS if matches .
Windows.
; LINUX if matches .
Linux.
os_version
target.platform_version
Extracted from asset_os
asset_os
principal.platform
Set to WINDOWS if matches .
Windows.
; LINUX if matches .
Linux.
os_version
principal.platform_version
Extracted from asset_os
usr_name
userId
Value copied directly
Users
userId
Value copied directly if not WG or ADDC
id
userId
Value copied directly
userId
target.user.userid
Value copied directly if message_type is Audit or loginStatus not empty
userId
principal.user.userid
Value copied directly if not Audit or loginStatus
userDisplayName
target.user.user_display_name
Value copied directly if message_type is Audit or loginStatus not empty
userDisplayName
principal.user.user_display_name
Value copied directly if not Audit or loginStatus
userPrincipalName
principal.user.userid
Value copied directly
Description
metadata.description
Value copied directly if not empty
Details
metadata.description
Value copied directly if not empty
mfaResult
metadata.description
Value copied directly if not empty
data7
metadata.description
Value copied directly if not empty
message_type
metadata.description
Value copied directly if description_details empty
src_ip, srcip
principal.ip
Value from src_ip if not empty, else src, else Source, else ipAddress
src_ip
principal.ip
Extracted as IP from src_ip if valid
mac_address
principal.mac
Processed as array, converted to lowercase, merged if valid MAC
event_id
target.process.pid
Value copied directly if message_type is Audit or loginStatus not empty
event_id
metadata.product_log_id
Value copied directly if not Audit or loginStatus
event_type
metadata.event_type
Value copied directly
Severity
security_result.severity
Set to INFORMATIONAL if Low or empty; MEDIUM if Medium; HIGH if High; CRITICAL if Critical
Action
security_result.action
Set to ALLOW if matches (?i)Allow; BLOCK if matches (?i)Block; else action_details
security_action
security_result.action
Value copied directly
Rule
rules
Value copied directly
rules
security_result.rule_name
Value copied directly
Classification
security_result.summary
Value copied directly
First Seen
security_result.detection_fields
Set as label with key "First Seen"
Last Seen
security_result.detection_fields
Set as label with key "Last Seen"
Organization
target.administrative_domain
Value copied directly if message_type is Audit or loginStatus not empty
Organization
additional.fields
Set as label with key "Organization" if not Audit or loginStatus
security_result
security_result
Merged from sec_result
metadata.vendor_name
Set to "FORTINET"
metadata.product_name
Set to "FORTINET_FORTIEDR"
Need more help?
Get answers from Community members and Google SecOps professionals.
