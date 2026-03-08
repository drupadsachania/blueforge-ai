# Collect Cisco eStreamer logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer/  
**Scraped:** 2026-03-05T09:52:19.475487Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco eStreamer logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco eStreamer logs to Google Security Operations using Bindplane. The parser extracts fields from the SYSLOG messages in key-value format, using grok to parse the initial message and kv to handle the key-value data. It then maps these extracted fields to the Unified Data Model (UDM), handling various data types and enriching the event with metadata like event type based on the presence of principal and target information.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows Server 2012 SP2 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco Firepower Management Center (FMC)
A Linux system to run the eNcore CLI client
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
Install Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
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
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/opt/observiq-otel-collector/
directory on Linux or `C:\Program Files\observIQ OpenTelemetry Collector` directory on Windows.
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
# Add optional ingestion labels for better organization
log_type
:
'CISCO_ESTREAMER'
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
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding on Cisco eStreamer
Configure eStreamer on Firepower Management Center
Sign in to the
Firepower Management Center
.
Go to
System
>
Integration
>
eStreamer
.
Click
eStreamer
to access the eStreamer Event Configuration.
Select the check boxes next to the types of events you want to capture:
Intrusion Events
: For intrusion detection events
Intrusion Event Packet Data
: For packet captures associated with intrusion events
Connection Events
: For network connection data
Security Intelligence Events
: For threat intelligence data
File Events
: For file analysis events
Malware Events
: For malware detection events
Click
Save
.
Create eStreamer Client
In the
eStreamer
page, click
Create Client
.
Provide the following configuration details:
Hostname
: Enter the IP address of the Linux system where eNcore client will run.
Password
: Enter a password to encrypt the certificate file.
Click
Save
.
Download the generated PKCS12 certificate file and transfer it to your eNcore client system.
Install and Configure eNcore CLI Client
On your Linux system, download the eStreamer eNcore CLI client from Cisco.
Extract the eNcore package:
tar
-xzf
eStreamer-eNcore-*.tar.gz
cd
eStreamer-eNcore-*
Run the setup script:
./encore.sh
setup
When prompted, choose the output format for key-value pairs (compatible with SIEM systems).
Enter the FMC IP address and the PKCS12 certificate password.
Configure the
estreamer.conf
file to output syslog messages to your Bindplane agent:
Open the
estreamer.conf
file in a text editor.
Locate the outputters section and configure it to send syslog to your Bindplane agent:
{
"handler"
:
{
"outputters"
:
[
{
"name"
:
"syslog"
,
"adapter"
:
"kvpair"
,
"enabled"
:
true
,
"stream"
:
{
"uri"
:
"udp://BINDPLANE_AGENT_IP:514"
}
}
]
}
}
Replace
BINDPLANE_AGENT_IP
with the IP address of your Bindplane agent.
Start eNcore Client
Test the connection in foreground mode:
./encore.sh
foreground
Once verified, start eNcore as a background service:
./encore.sh
start
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action_details
The value of
act
from the raw log is assigned to this field.
act
security_result.action
If the value of
act
is "Allow" (case-insensitive), then the value "ALLOW" is assigned to this field.
app
network.http.user_agent
The value of
app
(renamed as
requestClientApplication
in the parser) from the raw log is assigned to this field.
blockLength
security_result.detection_fields[].key
The string "blocklength" is assigned to this field.
blockLength
security_result.detection_fields[].value
The value of
blockLength
from the raw log, converted to a string, is assigned to this field.
blockType
security_result.detection_fields[].key
The string "blockType" is assigned to this field.
blockType
security_result.detection_fields[].value
The value of
blockType
from the raw log, converted to a string, is assigned to this field.
bytesIn
network.received_bytes
The value of
bytesIn
from the raw log is assigned to this field and converted to an unsigned integer.
bytesOut
network.sent_bytes
The value of
bytesOut
from the raw log is assigned to this field and converted to an unsigned integer.
cat
security_result.category_details
The value of
cat
from the raw log is assigned to this field.
cs1
security_result.detection_fields[].value
The value of
cs1
from the raw log is assigned to this field.
cs1Label
security_result.detection_fields[].key
The value of
cs1Label
from the raw log is assigned to this field.
cs2
security_result.detection_fields[].value
The value of
cs2
from the raw log is assigned to this field.
cs2Label
security_result.detection_fields[].key
The value of
cs2Label
from the raw log is assigned to this field.
cs3
security_result.detection_fields[].value
The value of
cs3
from the raw log is assigned to this field.
cs3Label
security_result.detection_fields[].key
The value of
cs3Label
from the raw log is assigned to this field.
cs4
security_result.detection_fields[].value
The value of
cs4
from the raw log is assigned to this field.
cs4Label
security_result.detection_fields[].key
The value of
cs4Label
from the raw log is assigned to this field.
cs5
security_result.detection_fields[].value
The value of
cs5
from the raw log is assigned to this field.
cs5Label
security_result.detection_fields[].key
The value of
cs5Label
from the raw log is assigned to this field.
cs6
security_result.detection_fields[].value
The value of
cs6
from the raw log is assigned to this field.
cs6
security_result.rule_id
The value of
cs6
from the raw log is assigned to this field.
cs6Label
security_result.detection_fields[].key
The value of
cs6Label
from the raw log is assigned to this field.
data
security_result.detection_fields[].value
The value of
data
from the
suser
JSON object in the raw log is assigned to this field if the
suser
field is a JSON.
deviceInboundInterface
additional.fields[].key
The string "deviceInboundInterface" is assigned to this field.
deviceInboundInterface
additional.fields[].value.string_value
The value of
deviceInboundInterface
from the raw log is assigned to this field.
deviceOutboundInterface
additional.fields[].key
The string "deviceOutboundInterface" is assigned to this field.
deviceOutboundInterface
additional.fields[].value.string_value
The value of
deviceOutboundInterface
from the raw log is assigned to this field.
dpt
target.port
The value of
dpt
from the raw log is assigned to this field and converted to an integer.
dst
target.asset.ip
The value of
dst
from the raw log is assigned to this field.
dst
target.ip
The value of
dst
from the raw log is assigned to this field.
dvcpid
security_result.about.process.pid
The value of
dvcpid
from the raw log is assigned to this field.
dvchost
target.asset.hostname
The value of
dvchost
from the raw log is assigned to this field.
dvchost
target.hostname
The value of
dvchost
from the raw log is assigned to this field.
hostname
principal.asset.hostname
The value of
hostname
from the raw log is assigned to this field.
hostname
principal.hostname
The value of
hostname
from the raw log is assigned to this field. Determined by parser logic based on the presence of
principal
and
target
information.  If both are present, the value is "NETWORK_CONNECTION". If only
principal
is present, the value is "STATUS_UPDATE". If only
target
is present, the value is "USER_UNCATEGORIZED". Otherwise, the value is "GENERIC_EVENT".
product_event_type
metadata.product_event_type
The value of
product_event_type
from the raw log is assigned to this field.
product_name
metadata.product_name
The value of
product_name
from the raw log is assigned to this field.
proto
network.ip_protocol
The value of
proto
from the raw log is converted to an integer, then mapped to the corresponding IP protocol name (e.g., 6 becomes TCP, 17 becomes UDP) using a lookup included from "parse_ip_protocol.include".
severity
security_result.severity_details
The value of
severity
from the raw log is assigned to this field.
spt
principal.port
The value of
spt
from the raw log is assigned to this field and converted to an integer.
src
principal.asset.ip
The value of
src
from the raw log is assigned to this field.
src
principal.ip
The value of
src
from the raw log is assigned to this field.
suser
security_result.detection_fields[].value
The value of
suser
from the raw log is assigned to this field if it's not a JSON object. If it's a JSON, the
data
field from the
suser
object is used.
suser
security_result.detection_fields[].key
The string "suser" is assigned to this field.
ts
metadata.event_timestamp
The value of
ts
from the raw log is parsed as a timestamp and assigned to this field. Several timestamp formats are attempted until a successful parse is achieved.
vendor_name
metadata.vendor_name
The value of
vendor_name
from the raw log is assigned to this field.
version
metadata.product_version
The value of
version
from the raw log is assigned to this field.
Need more help?
Get answers from Community members and Google SecOps professionals.
