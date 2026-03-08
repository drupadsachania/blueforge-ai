# Collect BlueCat Edge DNS Resolver logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge/  
**Scraped:** 2026-03-05T09:20:35.225513Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BlueCat Edge DNS Resolver logs
Supported in:
Google secops
SIEM
This document explains how to ingest BlueCat Edge DNS Resolver to
Google Security Operations using Bindplane. The parser first attempts to parse the
input message as JSON. If successful, it extracts and structures various
fields into the Unified Data Model (UDM) schema, particularly focusing on
DNS-related information. If JSON parsing fails, it tries alternative parsing
methods like grok and key-value pairs to extract relevant data and map it to
the UDM schema.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to BlueCat DNS/DHCP
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
For additional installation options, consult the
installation guide
.
Configure the BindPlane agent to ingest Syslog and send to Google SecOps
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
ingestion_labels
:
log_type
:
'BLUECAT_EDGE'
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
Configure Syslog on BlueCat Edge DNS Resolver
Sign in to the
BDDS
web UI.
Go to
Configuration
>
Servers tab
.
Select the
name
of a
BDDS
to open the
Details tab
for the server.
Click the
server name menu
>
Service Configuration
.
Click
Service Type
>
Syslog
.
Provide the following configuration details:
Select the
ISO 8601 Timestamp
checkbox to use the ISO 8601 timestamp format for locally logged messages.
Server
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number.
Level
: Select
Informational
.
Select the
Use RFC5 424 Syslog Protocol
checkbox to use the RFC5 424 syslog protocol for syslog messages.
Select the
ISO 8601 Timestamp
checkbox to use the ISO 8601 timestamp format for syslog messages redirected to a remote syslog server.
Under
Service Type
, select
DNS
,
DHCP
and
All Other Services
.
Transport
: Select
UDP
.
Click
Add
.
Click
Update
.
UDM mapping table
Log Field
UDM Mapping
Logic
answer.domainName
network.dns.answers.name
The domain name from the
answer
section of the DNS response. The trailing
.
is removed.
answer.recordTypeId
network.dns.answers.type
The record type ID from the
answer
section of the DNS response, converted to an unsigned integer.
answer.ttl
network.dns.answers.ttl
The Time to Live (TTL) value from the
answer
section of the DNS response, converted to an unsigned integer.
customerId
target.user.userid
The customer ID from the log, representing the user who initiated the DNS request.
domain.domainName
network.dns.authority.data
The domain name from the
authority
or
additional
sections of the DNS response. The trailing
.
is removed.
hostname
principal.hostname
The hostname extracted from the
Host
header in the raw log, only if the log is not in JSON format.
method
network.http.method
The HTTP method extracted from the raw log, only if the log is not in JSON format.
parentDomain
principal.administrative_domain
The parent domain of the queried DNS name. The trailing
.
is removed.
port
principal.port
The port number extracted from the
Host
header in the raw log, only if the log is not in JSON format, converted to an integer.
question.domainName
network.dns.questions.name
The domain name from the
question
section of the DNS request. The trailing
.
is removed.
question.questionTypeId
network.dns.questions.type
The question type ID from the
question
section of the DNS request, converted to an unsigned integer.
responseData.header.aa
network.dns.authoritative
Whether the DNS response is authoritative, extracted from the
responseData
section.
responseData.header.id
network.dns.id
The DNS message ID, extracted from the
responseData
section, converted to an unsigned integer.
responseData.header.opcode
network.dns.opcode
The DNS message opcode, extracted from the
responseData
section, converted to an unsigned integer.
responseData.header.ra
network.dns.recursion_available
Whether recursion is available, extracted from the
responseData
section.
responseData.header.rcode
network.dns.response_code
The DNS response code, extracted from the
responseData
section, converted to an unsigned integer.
responseData.header.rd
network.dns.recursion_desired
Whether recursion is selected, extracted from the
responseData
section.
responseData.header.tc
network.dns.truncated
Whether the DNS message is truncated, extracted from the
responseData
section.
servicePointId
additional.fields.value.string_value
The service point ID from the log.
siteId
additional.fields.value.string_value
The site ID from the log.
socketProtocol
network.ip_protocol
The network protocol used for the DNS request (TCP or UDP).
sourceAddress
principal.ip
The IP address of the DNS client.
sourcePort
principal.port
The port number of the DNS client, converted to an integer.
threat.indicators
security_result.category_details
The indicators associated with a detected threat.
threat.type
security_result.threat_name
The type of detected threat.
time
metadata.event_timestamp.seconds
The timestamp of the DNS event, extracted from the
time
field and converted from milliseconds to seconds.
User-Agent
network.http.user_agent
The user agent string extracted from the raw log, only if the log is not in JSON format.
additional.fields.key
servicePointId
or
siteId
or
Content-Type
or
Content-Length
, depending on the content of the raw log.
metadata.event_type
The event type, set to
NETWORK_DNS
if a DNS question is present, otherwise set to
GENERIC_EVENT
.
metadata.log_type
The log type, always set to
BLUECAT_EDGE
.
network.application_protocol
The application protocol, set to
DNS
if a DNS question is present, otherwise set to
HTTP
if an HTTP method is extracted, or left empty.
Need more help?
Get answers from Community members and Google SecOps professionals.
