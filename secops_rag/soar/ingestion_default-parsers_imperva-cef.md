# Collect Imperva CEF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-cef/  
**Scraped:** 2026-03-05T09:57:13.167909Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Imperva CEF logs
Supported in:
Google secops
SIEM
This document explains how to ingest Imperva CEF logs to Google Security Operations using Bindplane. The parser extracts the logs in CEF format from syslog messages, converting them into the UDM format. It handles various log formats, extracts key-value pairs from the payload, performs data transformations and enrichments, and maps the extracted fields to the corresponding UDM fields, including network information, user details, geolocation, and security results.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Imperva management console or appliance
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
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'IMPERVA_CEF'
raw_log_field
:
body
ingestion_labels
:
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
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
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
Configure Imperva WAF Gateway (SecureSphere) to send CEF over syslog
In the MX console, create an Action Set:
Navigate to
Policies
>
Action Sets
.
Click
New
and name it (for example,
Google SecOps CEF
).
Add the CEF syslog Action Interface:
In
Available Action Interfaces
, open
System Log
and add one or more of the following (as needed):
Log Security Event to System Log (syslog) using the CEF standard
Log Network Security Event to System Log (syslog) using the CEF standard
Log System Event to System Log (syslog) using the CEF standard
Log Custom Security Event to System Log (syslog) using the CEF standard
Configure Action Interface parameters:
Syslog Host
: Enter your Bindplane agent IP address. To use a non-default port, append
:PORT
(default is 514 if you don't specify one). Example:
10.0.0.10:514
.
Facility
/
Log Level
: Set per your policy requirements.
Message
: Leave vendor defaults for CEF unless you have a custom mapping.
Attach the Action Set to policies:
For
Security / Network Security
events: Open the relevant policy(ies) and set
Followed Action
to your Action Set.
For
System Events
: Create or verify a
System Events
policy and set
Followed Action
to your Action Set so those events are also sent via CEF.
Optional: Configure gateway-specific targets:
If different gateway groups must send to different syslog servers, configure each
Gateway Group
>
External Logger
and enable
"Use gateway configuration if exists"
in the policy.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action
Derived. If
act
is "allowed", "alert", starts with "REQ_PASSED", or starts with "REQ_CACHED", then
action
is "ALLOW". If
act
is "deny", "blocked", starts with "REQ_BLOCKED", or starts with "REQ_CHALLENGE", then
action
is "BLOCK". If
act
matches regex
(?i)REQ_BAD
, then
action
is "FAIL". Otherwise,
action
is "UNKNOWN_ACTION".
security_result.action
is then set to the value of
action
.
act
security_result.action_details
Derived. Based on the value of
act
, a detailed description is generated. Examples: "REQ_CACHED_FRESH: response was returned from the data center's cache", "REQ_BLOCKED: the request was blocked".
app
network.application_protocol
Directly mapped after being converted to uppercase.
cs1
security_result.detection_fields.value
Conditionally mapped if
cs1
is not empty or "NA".
security_result.detection_fields.key
is set to the value of
cs1Label
.
cs1Label
security_result.detection_fields.key
Conditionally mapped if
cs1
is not empty or "NA".
security_result.detection_fields.value
is set to the value of
cs1
.
cs2
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to the value of
cs2Label
.
cs2Label
security_result.detection_fields.key
Conditionally mapped if
cs2
is not empty.
security_result.detection_fields.value
is set to the value of
cs2
.
cs3
security_result.detection_fields.value
Conditionally mapped if not empty or "-".
security_result.detection_fields.key
is set to the value of
cs3Label
.
cs3Label
security_result.detection_fields.key
Conditionally mapped if
cs3
is not empty or "-".
security_result.detection_fields.value
is set to the value of
cs3
.
cs4
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to the value of
cs4Label
.
cs4Label
security_result.detection_fields.key
Conditionally mapped if
cs4
is not empty.
security_result.detection_fields.value
is set to the value of
cs4
.
cs5
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to the value of
cs5Label
.
cs5Label
security_result.detection_fields.key
Conditionally mapped if
cs5
is not empty.
security_result.detection_fields.value
is set to the value of
cs5
.
cs6
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to the value of
cs6Label
.
cs6Label
security_result.detection_fields.key
Conditionally mapped if
cs6
is not empty.
security_result.detection_fields.value
is set to the value of
cs6
.
cs7
principal.location.region_latitude
Conditionally mapped if
cs7Label
is "latitude".
cs8
principal.location.region_longitude
Conditionally mapped if
cs8Label
is "longitude".
cn1
security_result.detection_fields.value
Conditionally mapped if not empty and
cn1Label
is not empty.
security_result.detection_fields.key
is set to the value of
cn1Label
.
cn1Label
security_result.detection_fields.key
Conditionally mapped if
cn1
and
cn1Label
are not empty.
security_result.detection_fields.value
is set to the value of
cn1
.
fileType
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to "fileType".
filePermission
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to "filePermission".
request
target.url
Directly mapped.
requestClientApplication
network.http.user_agent
Conditionally mapped if not empty. Overwrites the value mapped from the
user_agent
field extracted from the
requestContext
or
requestClientApplication
key-value pairs in the CEF payload.
requestMethod
network.http.method
Directly mapped.
siteid
security_result.detection_fields.value
Conditionally mapped if not empty.
security_result.detection_fields.key
is set to "siteid".
sourceServiceName
target.hostname
Directly mapped. Overwrites the value of
dhost
if present.
src
principal.ip
Directly mapped.
start
metadata.event_timestamp.seconds
Extracted using a grok pattern and converted to a timestamp. Used as a fallback for
deviceReceiptTime
if it's not present.  If both
deviceReceiptTime
and
start
are empty, the log timestamp is used.
suid
principal.user.userid
Conditionally mapped if not empty.
N/A
metadata.event_type
Hardcoded to "NETWORK_HTTP".
N/A
metadata.log_type
Directly mapped from the top-level
log_type
field.
N/A
metadata.product_event_type
Mapped from
csv.event_id
if not empty.
N/A
metadata.product_name
Hardcoded to "Web Application Firewall".
N/A
metadata.vendor_name
Hardcoded to "Imperva".
Need more help?
Get answers from Community members and Google SecOps professionals.
