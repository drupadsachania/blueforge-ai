# Collect ExtraHop DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-dns/  
**Scraped:** 2026-03-05T09:23:53.279735Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ExtraHop DNS logs
Supported in:
Google secops
SIEM
This document explains how to ingest ExtraHop DNS logs to Google Security Operations using Bindplane. The parser extracts JSON-formatted logs from a raw message string, handling non-JSON data by dropping the event. Then, it maps specific fields from the extracted JSON to the corresponding fields in the Unified Data Model (UDM) schema, converting data types and handling different DNS response structures to ensure consistent representation.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to ExtraHop DNS
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
yaml
receivers:
    udplog:
        # Replace the port and IP address as required
        listen_address: "0.0.0.0:514"

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        # Adjust the path to the credentials file you downloaded in Step 1
        creds_file_path: '/path/to/ingestion-authentication-file.json'
        # Replace with your actual customer ID from Step 2
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        # Add optional ingestion labels for better organization
        log_type: 'EXTRAHOP_DNS'
        raw_log_field: body
        ingestion_labels:

service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - udplog
            exporters:
                - chronicle/chronicle_w_labels
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
Configure Syslog for ExtraHop Open Data Stream (DNS)
Sign in to the
ExtraHop Administration
using
https://<extrahop-hostname-or-IP-address>/admin
.
Go to
System Configuration
>
Open Data Streams
.
Click
Add Target
.
From the
Target Type
drop-down, select
Syslog
.
Provide the following configuration details:
Name
: Enter a unique name to identify the target.
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Protocol
: Select
UDP
, or
TCP
, depending on your Bindplane configuration.
(Optional) Select
Local Time
to send syslog information with timestamps in the local time zone.
Click
Test
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ans.data
network.dns.answers.data
Extracted from the
data
field within the
answers
array in the raw log.
ans.name
network.dns.answers.name
Extracted from the
name
field within the
answers
array in the raw log.
ans.ttl
network.dns.answers.ttl
Extracted from the
ttl
field within the
answers
array in the raw log. Converted to
uinteger
.
ans.typeNum
network.dns.answers.type
Extracted from the
typeNum
field within the
answers
array in the raw log. Converted to
uinteger
.
ans_data
network.dns.answers.data
Extracted from the
ans_data
field in the raw log when
answers
array is not present.
ans_name
network.dns.answers.name
Extracted from the
ans_name
field in the raw log when
answers
array is not present.
ans_ttl
network.dns.answers.ttl
Extracted from the
ans_ttl
field in the raw log when
answers
array is not present. Converted to
uinteger
.
client_ip
principal.ip
Extracted from the
client_ip
field in the raw log.
dns_type
network.dns.response
If the value is 'response' then 'true', otherwise it is not mapped. Converted to
boolean
.
dst_ip
target.ip
Extracted from the
dst_ip
field in the raw log.
ip_or_host
intermediary.hostname
If
ip_or_host
is not a valid IP address, it's mapped to
intermediary.hostname
.
ip_or_host
intermediary.ip
If
ip_or_host
is a valid IP address, it's mapped to
intermediary.ip
.
opcode
network.dns.opcode
Extracted from the
opcode
field in the raw log. Mapped to numerical values based on the opcode string (e.g., "QUERY" -> 0). Converted to
uinteger
.
qname
network.dns.questions.name
Extracted from the
qname
field in the raw log.
qtype
network.dns.questions.type
Extracted from the
qtype
field in the raw log. Mapped to numerical values based on the record type string (e.g., "A" -> 1). Converted to
uinteger
.
metadata.event_type
Set to
NETWORK_DNS
.
metadata.log_type
Set to
EXTRAHOP_DNS
.
network.application_protocol
Set to
DNS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
