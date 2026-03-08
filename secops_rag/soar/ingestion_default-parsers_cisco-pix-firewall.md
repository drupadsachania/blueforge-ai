# Collect Cisco PIX logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-pix-firewall/  
**Scraped:** 2026-03-05T09:52:30.758726Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco PIX logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco PIX logs to Google Security Operations
using Bindplane. The parser extracts fields from the firewall syslog messages
using regular expressions (grok patterns) and conditional logic. It then maps
these extracted fields to the Unified Data Model (UDM), categorizing events as
network connections, status updates, or generic events based on the presence of
source and destination IP addresses.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the
Cisco PIX Firewall
appliance
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
Save the file securely on the system where Bindplane will be installed.
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
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'CISCO_PIX_FIREWALL'
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
to the path where the
authentication file was saved in the
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
Configure Syslog on Cisco PIX Firewall
Sign in to your Cisco PIX appliance using SSH or a console connection.
Enter the following for
privileged
mode:
enable
Enter the following command for configuration mode:
conf
t
Enter the following commands to enable logging and timestamp:
logging
on
logging
timestamp
Enter the following command to configure log level:
logging
trap
information
Enter the following command to configure syslog information:
logging
host
<interface>
<bindplane_IP_address>
Change
<interface>
to the interface that has access to your Bindplane agent.
Change
<bindplane_IP_address>
to your actual Bindplane agent IP address.
UDM mapping table
Log Field
UDM Mapping
Logic
datetime
metadata.event_timestamp.seconds
Convert the extracted timestamp to epoch seconds
datetime
metadata.event_timestamp.nanos
Convert the extracted timestamp to epoch nanoseconds
descrip
metadata.description
Directly mapped from the extracted
descrip
field
observer_ip
observer.ip
Directly mapped from the extracted
observer_ip
field
proto
network.ip_protocol
Directly mapped from the extracted
proto
field after converting to uppercase. Only mapped if the value is one of
UDP
,
TCP
, or
ICMP
.
src_ip
principal.ip
Directly mapped from the extracted
src_ip
field
src_port
principal.port
Directly mapped from the extracted
src_port
field after converting to integer
facility
principal.resource.type
Directly mapped from the extracted
facility
field
action
security_result.action_details
Directly mapped from the extracted
action
field
severity_level
security_result.severity
Mapped based on the value of
severity_level
:
- 7, 6: INFORMATIONAL
- 5: LOW
- 4: MEDIUM
- 3: ERROR
- 2: HIGH
- Otherwise: CRITICAL
dest_ip
target.ip
Directly mapped from the extracted
dest_ip
field
dest_port
target.port
Directly mapped from the extracted
dest_port
field after converting to integer
direction
network.direction
Mapped to
INBOUND
if the
direction
field is
inbound
metadata.event_timestamp.seconds
Value taken from the top level 'create_time.seconds' field
metadata.event_timestamp.nanos
Value taken from the top level 'create_time.nanos' field
metadata.event_type
Determined based on the presence of src_ip and dest_ip:
- Both present: NETWORK_CONNECTION
- Only src_ip present: STATUS_UPDATE
- Otherwise: GENERIC_EVENT
metadata.product_event_type
Concatenation of
facility
,
-
,
severity_level
,
-
, and
mnemonic
fields.
metadata.product_name
Hardcoded value:
CISCO_FWSM
metadata.vendor_name
Hardcoded value:
CISCO
security_result.action
Mapped to
BLOCK
if the
action
field is one of
Deny
,
Teardown
,
denied
, or
Denied
.
Need more help?
Get answers from Community members and Google SecOps professionals.
