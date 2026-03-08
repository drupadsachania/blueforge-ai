# Collect Atlassian Confluence logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-confluence/  
**Scraped:** 2026-03-05T09:19:21.120245Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Atlassian Confluence logs
Supported in:
Google secops
SIEM
This document explains how to ingest Atlassian Confluence logs to Google Security Operations. The parser first attempts to extract fields from the raw log message using regular expressions (grok patterns) designed for Atlassian Confluence logs. If the grok parsing fails or the log is in JSON format, the code then attempts to parse the message as JSON. Finally, the extracted fields are mapped to the Google SecOps UDM schema and enriched with additional context.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
An Atlassian Confluence Cloud account with audit log access OR Confluence Data Center/Server with administrative access
For GCP-based method: Privileged access to GCP (GCS, IAM, Cloud Run, Pub/Sub, Cloud Scheduler)
For Bindplane method: Windows Server 2016 or later, or Linux host with
systemd
Integration options overview
This guide provides two integration paths:
Option 1
: Confluence Data Center/Server via Bindplane + Syslog
Option 2
: Confluence Cloud Audit Logs via GCP Cloud Run function + GCS (JSON format)
Choose the option that best fits your Confluence deployment type and infrastructure.
Option 1: Confluence Data Center/Server via Bindplane + Syslog
This option configures Confluence Data Center or Server to send logs via syslog to a Bindplane agent, which then forwards them to Google SecOps.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
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
"https://github.com/observIQ/bindplane-otel-collector/releases/latest/download/observiq-otel-collector.msi"
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
https://github.com/observIQ/bindplane-otel-collector/releases/latest/download/install_unix.sh
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
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/confluence_logs
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
ATLASSIAN_CONFLUENCE
raw_log_field
:
body
ingestion_labels
:
service
:
confluence
service
:
pipelines
:
logs/confluence
:
receivers
:
-
udplog
exporters
:
-
chronicle/confluence_logs
Configuration parameters
Replace the following placeholders:
listen_address
: Replace the port and IP address as required in your infrastructure. Use
0.0.0.0:514
to listen on all interfaces on port 514.
creds_file_path
: Update to the path where the authentication file was saved:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Replace
YOUR_CUSTOMER_ID
with the actual customer ID from the previous step.
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
Restart the Bindplane agent to apply the changes
Restart the Bindplane agent in Linux
To restart the Bindplane agent in Linux, run the following command:
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
Restart the Bindplane agent in Windows
To restart the Bindplane agent in Windows, choose one of the following options:
Using Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Using Services console:
Press
Win+R
, type
services.msc
, and press Enter.
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
Configure Syslog forwarding on Confluence Data Center/Server
Option A: Configure rsyslog to forward local log files (Recommended)
Configure Confluence to write logs to files (default behavior).
Install rsyslog if not present:
sudo
apt-get
install
rsyslog
# Debian/Ubuntu
sudo
yum
install
rsyslog
# RHEL/CentOS
Create rsyslog configuration file
/etc/rsyslog.d/confluence.conf
:
#
Forward
Confluence
logs
to
Bindplane
$
ModLoad
imfile
#
Application
logs
$
InputFileName
/
opt
/
atlassian
/
confluence
/
logs
/
atlassian
-
confluence
.
log
$
InputFileTag
confluence
-
app
:
$
InputFileStateFile
stat
-
confluence
-
app
$
InputFileSeverity
info
$
InputFileFacility
local0
$
InputRunFileMonitor
#
Audit
logs
(
JSON
format
in
DC
/
Server
)
$
InputFileName
<
confluence
-
home
-
directory
>
/
log
/
audit
/
audit
.
log
$
InputFileTag
confluence
-
audit
:
$
InputFileStateFile
stat
-
confluence
-
audit
$
InputFileSeverity
info
$
InputFileFacility
local1
$
InputRunFileMonitor
#
Forward
to
Bindplane
agent
*
.
*
@@BINDPLANE_AGENT_IP
:
514
Replace
BINDPLANE_AGENT_IP
with the IP address of the Bindplane agent (for example,
192.168.1.100
).
Adjust log file paths based on your Confluence installation:
Application logs typically:
<confluence-install>/logs/
or
<local-home>/logs/
Audit logs:
<confluence-home-directory>/log/audit/
(JSON format)
To find your Confluence home directory, go to
Settings
>
General Configuration
>
System Information
and look for
Confluence Home
or
Local Home
.
Restart rsyslog:
sudo
systemctl
restart
rsyslog
Option B: Configure Log4j2 Syslog forwarding
This option requires modifying Log4j2 configuration. Option A (rsyslog) is recommended for simplicity.
Sign in to your Confluence server via SSH or RDP.
Locate the Log4j2 configuration file at:
<
confluence-install>/confluence/WEB-INF/classes/log4j2.xml
Edit the configuration file to add a Syslog appender:
<Configuration>
<Appenders>
<!--
Existing
appenders
-->
<Syslog
name="SyslogAppender"
host="BINDPLANE_AGENT_IP"
port="514"
protocol="UDP"
format="RFC5424"
facility="LOCAL0">
<PatternLayout
pattern="%d{ISO8601}
%p
[%t]
[%c{1}]
%m%n"/>
</Syslog>
</Appenders>
<Loggers>
<Root
level="info">
<AppenderRef
ref="SyslogAppender"/>
<!--
Other
appender
refs
-->
</Root>
<!--
Audit
logger
-->
<Logger
name="com.atlassian.confluence.event.events.security.AuditEvent"
level="info"
additivity="false">
<AppenderRef
ref="SyslogAppender"/>
</Logger>
</Loggers>
</Configuration>
Replace
BINDPLANE_AGENT_IP
with the IP address of the Bindplane agent (for example,
192.168.1.100
).
Restart Confluence to apply changes:
sudo
systemctl
restart
confluence
Option 2: Confluence Cloud Audit Logs via GCP Cloud Run function and GCS
This method uses GCP Cloud Run function to periodically fetch audit logs via the Confluence Audit REST API and store them in GCS for Google SecOps ingestion.
Collect Confluence Cloud API credentials
Sign in to your
Atlassian account
.
Go to
https://id.atlassian.com/manage-profile/security/api-tokens
.
Click
Create API token
.
Enter a label for the token (for example,
Google Security Operations Integration
).
Click
Create
.
Copy and save the API token securely.
Note your Confluence Cloud site URL (for example,
https://yoursite.atlassian.net
).
Note your Atlassian account email address (used for authentication).
Verify permissions
To verify the account has the required permissions:
Sign in to Confluence Cloud.
Click the
Settings
icon (⚙️) in the top-right corner.
If you can see
Monitoring
>
Audit log
in the left-hand navigation, you have the required permissions.
If you cannot see this option, contact your administrator to grant
Confluence Administrator
permission.
Test API access
Test your credentials before proceeding with the integration:
# Replace with your actual credentials
CONFLUENCE_EMAIL
=
"your-email@example.com"
CONFLUENCE_API_TOKEN
=
"your-api-token"
CONFLUENCE_URL
=
"https://yoursite.atlassian.net"
# Test API access
curl
-u
"
${
CONFLUENCE_EMAIL
}
:
${
CONFLUENCE_API_TOKEN
}
"
\
-H
"Accept: application/json"
\
"
${
CONFLUENCE_URL
}
/wiki/rest/api/audit"
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
confluence-audit-logs
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
confluence-audit-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect Confluence Cloud audit logs
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
confluence-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com
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
confluence-audit-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Confluence Cloud Audit API and writes them to GCS.
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
confluence-audit-collector
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
Cloud Pub/Sub
.
In
Select a Cloud Pub/Sub topic
, choose
confluence-audit-trigger
.
Click
Save
.
In the
Authentication
section:
Select
Require authentication
.
Check
Identity and Access Management (IAM)
.
Scroll down and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select
confluence-audit-collector-sa
.
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
confluence-audit-logs
GCS bucket name
GCS_PREFIX
confluence-audit
Prefix for log files
STATE_KEY
confluence-audit/state.json
State file path
CONFLUENCE_URL
https://yoursite.atlassian.net
Confluence site URL
CONFLUENCE_EMAIL
your-email@example.com
Atlassian account email
CONFLUENCE_API_TOKEN
your-api-token-here
API token
MAX_RECORDS
1000
Max records per run
In the
Variables & Secrets
section, scroll down to
Requests
:
Request timeout
: Enter
600
seconds (10 minutes).
Go to the
Settings
tab:
In the
Resources
section:
Memory
: Select
512 MiB
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
100
(or adjust based on expected load).
Click
Create
.
Wait for the service to be created (1-2 minutes).
After the service is created, the
inline code editor
opens automatically.
Add function code
Enter
main
in
Function entry point
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
import
urllib3
from
datetime
import
datetime
,
timezone
,
timedelta
import
time
import
base64
# Initialize HTTP client with timeouts
http
=
urllib3
.
PoolManager
(
timeout
=
urllib3
.
Timeout
(
connect
=
5.0
,
read
=
30.0
),
retries
=
False
,
)
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
'confluence-audit/'
)
STATE_KEY
=
os
.
environ
.
get
(
'STATE_KEY'
,
'confluence-audit/state.json'
)
CONFLUENCE_URL
=
os
.
environ
.
get
(
'CONFLUENCE_URL'
)
CONFLUENCE_EMAIL
=
os
.
environ
.
get
(
'CONFLUENCE_EMAIL'
)
CONFLUENCE_API_TOKEN
=
os
.
environ
.
get
(
'CONFLUENCE_API_TOKEN'
)
MAX_RECORDS
=
int
(
os
.
environ
.
get
(
'MAX_RECORDS'
,
'1000'
))
def
to_unix_millis
(
dt
:
datetime
)
-
>
int
:
"""Convert datetime to Unix epoch milliseconds."""
if
dt
.
tzinfo
is
None
:
dt
=
dt
.
replace
(
tzinfo
=
timezone
.
utc
)
dt
=
dt
.
astimezone
(
timezone
.
utc
)
return
int
(
dt
.
timestamp
()
*
1000
)
def
parse_datetime
(
value
:
str
)
-
>
datetime
:
"""Parse ISO datetime string to datetime object."""
if
value
.
endswith
(
"Z"
):
value
=
value
[:
-
1
]
+
"+00:00"
return
datetime
.
fromisoformat
(
value
)
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch Confluence Cloud audit logs and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
all
([
GCS_BUCKET
,
CONFLUENCE_URL
,
CONFLUENCE_EMAIL
,
CONFLUENCE_API_TOKEN
]):
print
(
'Error: Missing required environment variables'
)
return
try
:
# Get GCS bucket
bucket
=
storage_client
.
bucket
(
GCS_BUCKET
)
# Load state
state
=
load_state
(
bucket
,
STATE_KEY
)
# Determine time window
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
last_time
=
None
if
isinstance
(
state
,
dict
)
and
state
.
get
(
"last_event_time"
):
try
:
last_time
=
parse_datetime
(
state
[
"last_event_time"
])
# Overlap by 2 minutes to catch any delayed events
last_time
=
last_time
-
timedelta
(
minutes
=
2
)
except
Exception
as
e
:
print
(
f
"Warning: Could not parse last_event_time:
{
e
}
"
)
if
last_time
is
None
:
last_time
=
now
-
timedelta
(
hours
=
24
)
print
(
f
"Fetching logs from
{
last_time
.
isoformat
()
}
to
{
now
.
isoformat
()
}
"
)
# Convert to Unix milliseconds
start_millis
=
to_unix_millis
(
last_time
)
end_millis
=
to_unix_millis
(
now
)
# Fetch logs
records
,
newest_event_time
=
fetch_logs
(
api_base
=
CONFLUENCE_URL
,
email
=
CONFLUENCE_EMAIL
,
api_token
=
CONFLUENCE_API_TOKEN
,
start_time_ms
=
start_millis
,
end_time_ms
=
end_millis
,
max_records
=
MAX_RECORDS
,
)
if
not
records
:
print
(
"No new log records found."
)
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
return
# Write to GCS as NDJSON
timestamp
=
now
.
strftime
(
'%Y%m
%d
_%H%M%S'
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
# Update state with newest event time
if
newest_event_time
:
save_state
(
bucket
,
STATE_KEY
,
newest_event_time
)
else
:
save_state
(
bucket
,
STATE_KEY
,
now
.
isoformat
())
print
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
)
except
Exception
as
e
:
print
(
f
'Error processing logs:
{
str
(
e
)
}
'
)
raise
def
load_state
(
bucket
,
key
):
"""Load state from GCS."""
try
:
blob
=
bucket
.
blob
(
key
)
if
blob
.
exists
():
state_data
=
blob
.
download_as_text
()
return
json
.
loads
(
state_data
)
except
Exception
as
e
:
print
(
f
"Warning: Could not load state:
{
e
}
"
)
return
{}
def
save_state
(
bucket
,
key
,
last_event_time_iso
:
str
):
"""Save the last event timestamp to GCS state file."""
try
:
state
=
{
'last_event_time'
:
last_event_time_iso
}
blob
=
bucket
.
blob
(
key
)
blob
.
upload_from_string
(
json
.
dumps
(
state
,
indent
=
2
),
content_type
=
'application/json'
)
print
(
f
"Saved state: last_event_time=
{
last_event_time_iso
}
"
)
except
Exception
as
e
:
print
(
f
"Warning: Could not save state:
{
e
}
"
)
def
fetch_logs
(
api_base
:
str
,
email
:
str
,
api_token
:
str
,
start_time_ms
:
int
,
end_time_ms
:
int
,
max_records
:
int
):
"""
Fetch logs from Confluence Cloud Audit API with pagination and rate limiting.
Args:
api_base: Confluence site URL
email: Atlassian account email
api_token: API token
start_time_ms: Start time in Unix milliseconds
end_time_ms: End time in Unix milliseconds
max_records: Maximum total records to fetch
Returns:
Tuple of (records list, newest_event_time ISO string)
"""
# Clean up URL
base_url
=
api_base
.
rstrip
(
'/'
)
# Build authentication header
auth_string
=
f
"
{
email
}
:
{
api_token
}
"
auth_bytes
=
auth_string
.
encode
(
'utf-8'
)
auth_b64
=
base64
.
b64encode
(
auth_bytes
)
.
decode
(
'utf-8'
)
headers
=
{
'Authorization'
:
f
'Basic
{
auth_b64
}
'
,
'Accept'
:
'application/json'
,
'User-Agent'
:
'GoogleSecOps-ConfluenceCollector/1.0'
}
records
=
[]
newest_time
=
None
page_num
=
0
backoff
=
1.0
start_index
=
0
while
True
:
page_num
+=
1
if
len
(
records
)
>
=
max_records
:
print
(
f
"Reached max_records limit (
{
max_records
}
)"
)
break
# Build request URL
url
=
f
"
{
base_url
}
/wiki/rest/api/audit?startDate=
{
start_time_ms
}
&
endDate=
{
end_time_ms
}
&
start=
{
start_index
}
&
limit=100"
try
:
response
=
http
.
request
(
'GET'
,
url
,
headers
=
headers
)
# Handle rate limiting with exponential backoff
if
response
.
status
==
429
:
retry_after
=
int
(
response
.
headers
.
get
(
'Retry-After'
,
str
(
int
(
backoff
))))
print
(
f
"Rate limited (429). Retrying after
{
retry_after
}
s..."
)
time
.
sleep
(
retry_after
)
backoff
=
min
(
backoff
*
2
,
30.0
)
continue
backoff
=
1.0
if
response
.
status
!=
200
:
print
(
f
"HTTP Error:
{
response
.
status
}
"
)
response_text
=
response
.
data
.
decode
(
'utf-8'
)
print
(
f
"Response body:
{
response_text
}
"
)
return
[],
None
data
=
json
.
loads
(
response
.
data
.
decode
(
'utf-8'
))
page_results
=
data
.
get
(
'results'
,
[])
if
not
page_results
:
print
(
f
"No more results (empty page)"
)
break
print
(
f
"Page
{
page_num
}
: Retrieved
{
len
(
page_results
)
}
events"
)
records
.
extend
(
page_results
)
# Track newest event time
for
event
in
page_results
:
try
:
# creationDate is in Unix milliseconds
event_time_ms
=
event
.
get
(
'creationDate'
)
if
event_time_ms
:
event_dt
=
datetime
.
fromtimestamp
(
event_time_ms
/
1000
,
tz
=
timezone
.
utc
)
event_time
=
event_dt
.
isoformat
()
if
newest_time
is
None
or
parse_datetime
(
event_time
)
>
parse_datetime
(
newest_time
):
newest_time
=
event_time
except
Exception
as
e
:
print
(
f
"Warning: Could not parse event time:
{
e
}
"
)
# Check for more results
current_size
=
data
.
get
(
'size'
,
0
)
if
current_size
<
100
:
print
(
f
"Reached last page (size=
{
current_size
}
< limit=100)"
)
break
start_index
+=
current_size
except
Exception
as
e
:
print
(
f
"Error fetching logs:
{
e
}
"
)
return
[],
None
print
(
f
"Retrieved
{
len
(
records
)
}
total records from
{
page_num
}
pages"
)
return
records
[:
max_records
],
newest_time
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
urllib3
>
=
2.0
.
0
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
In the
GCP Console
, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Setting
Value
Name
confluence-audit-collector-hourly
Region
Select same region as Cloud Run function
Frequency
0 * * * *
(every hour, on the hour)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select
confluence-audit-trigger
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose frequency based on log volume and latency requirements:
Frequency
Cron Expression
Use Case
Every 5 minutes
*/5 * * * *
High-volume, low-latency
Every 15 minutes
*/15 * * * *
Medium volume
Every hour
0 * * * *
Standard (recommended)
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
0 0 * * *
Historical data collection
Test the integration
In the
Cloud Scheduler
console, find your job.
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click on
confluence-audit-collector
.
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
Page 1: Retrieved X events
Wrote X records to gs://bucket-name/prefix/logs_YYYYMMDD_HHMMSS.ndjson
Successfully processed X records
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the
confluence-audit/
folder.
Verify that a new
.ndjson
file was created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check API credentials in environment variables
HTTP 403
: Verify account has Confluence Administrator permissions
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set
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
Confluence Cloud Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Atlassian Confluence
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
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
Copy this email address for use in the next step.
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
Configure a feed in Google SecOps to ingest Confluence logs
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
Confluence Cloud Audit Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Atlassian Confluence
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://confluence-audit-logs/confluence-audit/
Replace:
confluence-audit-logs
: Your GCS bucket name.
confluence-audit
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://company-logs/
With prefix:
gs://company-logs/confluence-audit/
With subfolder:
gs://company-logs/confluence/audit/
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
UDM mapping table
Log Field
UDM Mapping
Logic
agent
read_only_udm.network.http.user_agent
Value taken from "agent" field.
app_protocol
read_only_udm.network.application_protocol
Derived from "app_protocol" field. If "app_protocol" contains "HTTPS", "HTTP", "SSH", or "RDP", the corresponding protocol is used. Otherwise, it defaults to "UNKNOWN_APPLICATION_PROTOCOL".
app_protocol
read_only_udm.network.application_protocol_version
Value taken from "app_protocol" field.
auditType.action
read_only_udm.security_result.action
Derived from "auditType.action" field. If "auditType.action" contains "successful", the value is set to "ALLOW". If it contains "restricted", the value is set to "BLOCK".
auditType.action
read_only_udm.security_result.summary
Value taken from "auditType.action" field when "auditType" is not empty and "auditType_area" is "SECURITY".
auditType.actionI18nKey
read_only_udm.metadata.product_event_type
Value taken from "auditType.actionI18nKey" field when "auditType" is not empty.
auditType.area
read_only_udm.security_result.detection_fields.value
Value taken from "auditType.area" field and assigned to the "value" field of a detection field with the "key" field set to "auditType area". This mapping is done when "auditType" is not empty.
auditType.category
read_only_udm.security_result.category_details
Value taken from "auditType.category" field when "auditType" is not empty.
auditType.categoryI18nKey
read_only_udm.security_result.detection_fields.value
Value taken from "auditType.categoryI18nKey" field and assigned to the "value" field of a detection field with the "key" field set to "auditType categoryI18nKey". This mapping is done when "auditType" is not empty.
auditType.level
read_only_udm.security_result.detection_fields.value
Value taken from "auditType.level" field and assigned to the "value" field of a detection field with the "key" field set to "auditType level". This mapping is done when "auditType" is not empty.
author.displayName
read_only_udm.principal.user.user_display_name
Value taken from "author.displayName" field.
author.externalCollaborator
read_only_udm.security_result.about.resource.attribute.labels.value
Value taken from "author.externalCollaborator" field and assigned to the "value" field of a label with the "key" field set to "externalCollaborator".
author.id
read_only_udm.principal.user.userid
Value taken from "author.id" field when "author.type" is "user" and "principal_user_present" is "false".
author.isExternalCollaborator
read_only_udm.security_result.about.resource.attribute.labels.value
Value taken from "author.isExternalCollaborator" field and assigned to the "value" field of a label with the "key" field set to "isExternalCollaborator".
author.name
read_only_udm.principal.user.user_display_name
Value taken from "author.name" field when "author.type" is "user" and "principal_user_present" is "false".
bytes_in
read_only_udm.network.received_bytes
Value taken from "bytes_in" field if it contains digits. Otherwise, it defaults to 0.
category
read_only_udm.security_result.category_details
Value taken from "category" field.
changedValues
read_only_udm.principal.resource.attribute.labels
Iterates through each element in "changedValues" and creates labels with keys like "changedValue [index] [key]" and values from the corresponding values in the "changedValues" array.
creationDate
read_only_udm.metadata.event_timestamp
Value taken from "creationDate" field, parsed as either UNIX or UNIX_MS timestamp.
extraAttributes
read_only_udm.principal.resource.attribute.labels
Iterates through each element in "extraAttributes" and creates labels with keys based on "name" and "nameI18nKey" fields and values from the corresponding "value" field.
http_verb
read_only_udm.network.http.method
Value taken from "http_verb" field.
ip
read_only_udm.target.ip
Value taken from "ip" field.
principal_host
read_only_udm.principal.hostname
Value taken from "principal_host" field.
referral_url
read_only_udm.network.http.referral_url
Value taken from "referral_url" field.
remoteAddress
read_only_udm.principal.ip
Value taken from "remoteAddress" field, parsed as an IP address.
response_code
read_only_udm.network.http.response_code
Value taken from "response_code" field.
session_duration
read_only_udm.additional.fields.value.string_value
Value taken from "session_duration" field and assigned to the "string_value" field of a label with the "key" field set to "Session Duration".
source
read_only_udm.principal.ip
Value taken from "source" field, parsed as an IP address.
src_ip
read_only_udm.principal.ip
Value taken from "src_ip" field if "remoteAddress" is empty.
summary
read_only_udm.security_result.summary
Value taken from "summary" field.
sysAdmin
read_only_udm.security_result.about.resource.attribute.labels.value
Value taken from "sysAdmin" field and assigned to the "value" field of a label with the "key" field set to "sysAdmin".
superAdmin
read_only_udm.security_result.about.resource.attribute.labels.value
Value taken from "superAdmin" field and assigned to the "value" field of a label with the "key" field set to "superAdmin".
target_url
read_only_udm.target.url
Value taken from "target_url" field.
timestamp
read_only_udm.metadata.event_timestamp
Value taken from "timestamp" field, parsed as a date and time string.
user_id
read_only_udm.principal.user.userid
Value taken from "user_id" field.
read_only_udm.metadata.event_type
This field's value is determined by a series of checks and defaults to "GENERIC_EVENT". It is set to specific values like "NETWORK_HTTP", "USER_UNCATEGORIZED", or "STATUS_UPDATE" based on the presence and content of other fields like "principal_host", "user_id", "has_principal", and "author.type".
read_only_udm.metadata.vendor_name
Set to "ATLASSIAN".
read_only_udm.metadata.product_name
Set to "CONFLUENCE".
read_only_udm.metadata.log_type
Set to "ATLASSIAN_CONFLUENCE".
read_only_udm.principal.user.user_display_name
This field's value can come from either "author.displayName" or "affectedObject.name" depending on the context.
read_only_udm.target.process.pid
This field's value can come from either "principal_host" or "pid" depending on the context.
read_only_udm.principal.resource.attribute.labels
This field is populated with various labels derived from fields like "affectedObjects", "changedValues", and "extraAttributes". The keys and values of these labels are dynamically generated based on the specific content of these fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
