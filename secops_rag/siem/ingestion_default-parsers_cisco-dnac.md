# Collect Cisco DNA Center Platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac/  
**Scraped:** 2026-03-05T09:21:22.945687Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco DNA Center Platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco DNA Center Platform logs to Google Security Operations using two different approaches. Choose the option that best fits your environment and requirements. The parser transforms Cisco DNA Center SYSLOG+JSON logs into a unified data model (UDM). It extracts fields from the raw log message and JSON payload, maps them to corresponding UDM attributes, and enriches the data with labels and security context based on event characteristics like severity and involved entities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to the Cisco DNA Center Platform management console
Choose your preferred integration method:
For
Option 2
: Network connectivity between Cisco DNA Center and Google SecOps webhook endpoint
For
Option 1
: Windows 2016 or later, or a Linux host with
systemd
for the Bindplane agent installation
Option 1: Syslog integration using Bindplane agent
This option uses syslog forwarding from Cisco DNA Center to Bindplane, which then forwards structured logs to Google SecOps.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the 
system where Bindplane will be installed.
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
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open the
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
Additional installation resources
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
YOUR_CUSTOMER_ID
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'CISCO_DNAC'
raw_log_field
:
body
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<YOUR_CUSTOMER_ID>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
This configuration uses the Bindplane agent Syslog (UDP) receiver to collect structured syslog messages from DNA Center.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding on Cisco DNA Center Platform
Sign in to the
Cisco DNA Center Platform
.
Go to
System
>
Settings
>
External Services
>
Destinations
>
Syslog
.
Click
+ Add
to create a new syslog destination.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps BindPlane
).
Host
: Enter the BindPlane Agent IP address.
Port
: Enter
514
(or the port configured in BindPlane).
Protocol
: Select
UDP
or
TCP
depending on your BindPlane configuration.
Facility
: Select appropriate facility (for example,
Local0
).
Severity
: Select
Information
to capture all event levels.
Click
Save
.
Option 2: Real-time webhook integration
This option uses Cisco DNA Center's native webhook capabilities to deliver structured JSON events directly to Google SecOps in real-time.
Overview
Cisco DNA Center natively supports webhook notifications for real-time event delivery. This option provides structured JSON payloads with rich event context, delivering events directly to Google SecOps without requiring Bindplane as an intermediary.
Configure Google SecOps webhook feed
In Google SecOps, go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Cisco DNA Center Webhook
).
Select
Webhook
as the
Source type
.
Select
Cisco DNA Center Platform
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
: Optional
\n
.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your feed configuration and click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy
and
save
the secret key as you cannot view this secret again.
Go to the
Details
tab.
Copy
the feed endpoint URL from the
Endpoint Information
field.
Click
Done
.
Create an API key for the webhook feed
Go to the
Google Cloud
console
Credentials
page.
Click
Create
credentials, and then select
API key
.
Restrict the API key
access
to the
Google SecOps API
.
Configure Webhook destination in Cisco DNA Center
Sign in to the
Cisco DNA Center Platform
.
Go to
System
>
Settings
>
External Services
>
Destinations
>
Webhook
.
Click
+ Add
to create a new webhook destination.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Webhook
).
Description
: Enter a description for the webhook.
URL
: Enter the Google SecOps webhook endpoint URL from previous step.
Method
: Select
POST
.
Trust Certificate
: Select
No
if using self-signed certificates.
Headers
: Add required headers:
Content-Type
:
application/json
X-goog-api-key
: Your Google Cloud API key
X-Webhook-Access-Key
: Your Google SecOps feed secret key
Click
Test Connection
to verify connectivity.
Click
Save
.
Subscribe events to webhook notifications
In Cisco DNA Center, go to
Platform
>
Developer Toolkit
>
Event Notifications
.
Click
+ Subscribe
.
Provide the following configuration details:
Subscription Name
: Enter a descriptive name (for example,
Google SecOps Events
).
Connector Type
: Select
REST Endpoint
.
Destination
: Select the webhook destination created in previous step.
Select the event types you want to monitor:
Network Events
: Device unreachable, interface down, configuration changes.
Security Events
: Security policy violations, authentication failures.
System Events
: Platform events, software updates, maintenance.
Assurance Events
: Performance degradation, connectivity issues.
Configure event filters if needed:
Severity
: Select minimum severity level (for example,
P1
,
P2
).
Domain
: Filter by specific domains (for example,
Connectivity
,
Performance
).
Click
Subscribe
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
category
security_result.severity_details
Directly mapped from the
category
field in the raw log.
ciscoDnaEventLink
target.url
Directly mapped from the
ciscoDnaEventLink
field in the raw log.
date_time
metadata.event_timestamp
Extracted from the raw log message using grok pattern and converted to timestamp format.
details.Assurance_Issue_Category
security_result.about.resource.attribute.labels[].value
Directly mapped from the
details.Assurance_Issue_Category
field in the raw log. The key for this label is "Assurance_Issue_Category".
details.Assurance_Issue_Details
security_result.summary
Directly mapped from the
details.Assurance_Issue_Details
field in the raw log.
details.Assurance_Issue_Name
security_result.about.resource.attribute.labels[].value
Directly mapped from the
details.Assurance_Issue_Name
field in the raw log. The key for this label is "Assurance_Issue_Name".
details.Assurance_Issue_Priority
security_result.about.resource.attribute.labels[].value
Directly mapped from the
details.Assurance_Issue_Priority
field in the raw log. The key for this label is "Assurance_Issue_Priority".
details.Assurance_Issue_Status
security_result.about.resource.attribute.labels[].value
Directly mapped from the
details.Assurance_Issue_Status
field in the raw log. The key for this label is "Assurance_Issue_Status".
details.Device
target.ip OR target.hostname
Mapped from the
details.Device
field in the raw log. If the value is an IP address, it's mapped to
target.ip
, otherwise to
target.hostname
.
dnacIp
target.ip
Directly mapped from the
dnacIp
field in the raw log, if it's an IP address.
domain
additional.fields[].value.string_value
Directly mapped from the
domain
field in the raw log. The key for this field is "domain".
eventId
metadata.product_event_type
Directly mapped from the
eventId
field in the raw log.
instanceId
target.resource.product_object_id
Directly mapped from the
instanceId
field in the raw log.
name
target.resource.attribute.labels[].value
Directly mapped from the
name
field in the raw log. The key for this label is "name".
namespace
target.namespace
Directly mapped from the
namespace
field in the raw log.
network.deviceId
target.asset.asset_id
Directly mapped from the
network.deviceId
field in the raw log and prefixed with "deviceId: ".
note
additional.fields[].value.string_value
Directly mapped from the
note
field in the raw log. The key for this field is "note".
metadata.event_type
Determined based on the presence and values of
has_principal
,
has_target
, and
userId
fields. Possible values: NETWORK_CONNECTION, USER_UNCATEGORIZED, STATUS_UPDATE, GENERIC_EVENT.
is_alert
True if severity is 0 or 1, False otherwise.
is_significant
True if severity is 0 or 1, False otherwise.
severity
Used to determine the value of
security_result.severity
,
is_alert
and
is_significant
.
source
target.resource.attribute.labels[].value
Directly mapped from the
source
field in the raw log. The key for this label is "source".
src_ip
principal.ip
Extracted from the raw log message using grok pattern.
subDomain
additional.fields[].value.string_value
Directly mapped from the
subDomain
field in the raw log. The key for this field is "subDomain".
tntId
target.resource.attribute.labels[].value
Directly mapped from the
tntId
field in the raw log. The key for this label is "tntId".
type
target.resource.attribute.labels[].value
Directly mapped from the
type
field in the raw log. The key for this label is "type".
userId
target.user.userid
Directly mapped from the
userId
field in the raw log.
version
metadata.product_version
Directly mapped from the
version
field in the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
