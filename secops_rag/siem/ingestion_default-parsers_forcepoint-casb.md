# Collect Forcepoint CASB logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb/  
**Scraped:** 2026-03-05T09:24:31.291869Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forcepoint CASB logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forcepoint CASB (Cloud Access Security Broker)
logs to Google Security Operations using Bindplane. The parser extracts fields from
Forcepoint CASB syslog messages formatted with CEF. It uses Grok to parse the
message, KV to separate key-value pairs, and conditional logic to map extracted
fields to the Unified Data Model (UDM), handling various event types and
platform specifics.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
A Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Forcepoint CASB
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
'FORCEPOINT_CASB'
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
Download the Forcepoint SIEM tool
Sign in to the
Forcepoint CASB
management portal.
Go to
Settings
>
Tools and Agents
>
SIEM Tool
.
Click
Download
to download a zip file named
SIEM-Tool-\[operating system\]-\[release date\].zip
(for example,
SIEM-Tool-Windows-2021-10-19.zip
). The zip file contains one of the following
files, depending on the version you download:
SIEMClient.bat
(if you downloaded the Windows tool)
SIEMClient.sh
(if you downloaded the Linux tool)
Install the SIEM tool
For secure connection of the SIEM tool to the Forcepoint CASB service,
the tool requires the trust store file that can be downloaded from the Forcepoint
CASB management portal. Follow these steps:
Sign in to the
Forcepoint CASB
management portal.
Go to
Settings
>
Tools and Agents
>
SIEM Tool
.
Click
Download Trust Store
.
Save the downloaded trust store file in a location that the SIEM tool can
access after it's installed.
Extract the
SIEM tool
archive on a host that has
Java v1.8 or higher
installed and can access the organizational Forcepoint CASB management server.
Open a command prompt, go to the location of the
SIEMClient
files, and run the following command:
Windows:
SIEMClient.bat --set.credentials –-username <user> --password <password> --credentials.file <file>
Linux:
SIEMClient.sh --set.credentials –-username <user> --password <password> --credentials.file <file>
Provide the following configuration parameters:
<user>
and
<password>
: Forcepoint CASB administrator credentials. Optionally, if you omit the --username and --password arguments, you will be prompted to provide them interactively.
<file>
: Path and filename for the credentials store.
Run the SIEM tool from the command prompt:
<tool> --credentials.file <file> --host <host> --port <port#> --output.dir <dir> [ truststorePath=<trust> ] [ exportSyslog=true syslogHost=<bindplaneAgentIP> syslogFacility=<facility> ] [ cefVersion=<cef.version> ] [ cefCompliance=<cef.flag> ] [ --proxy.host <proxy.host> ] [ --proxy.port <proxy.port> ]
Provide the following configuration parameters:
<tool>
: On
Windows
:
SIEMClient.bat
, On
Linux
:
SIEMClient.sh
.
<file>
: Path and filename of the credentials store.
<host>
and
<port#>
: Connection details to the Forcepoint CASB management server. Port is usually 443.
<dir>
: Directory where the SIEM tool saves the produced activity files. Required even if pushing to syslog.
<trust>
: Path and filename of the trust store file downloaded previously.
<bindplaneAgentIP>
: IP address of the Bindplane agent.
<facility>
: Enter
local1
.
<cef.version>
: Set the version of CEF to
2
.
If cefVersion=1, the tool uses the legacy CEF format.
If cefVersion=2, the tool uses the true CEF format.
If cefVersion=3, the tool uses a newer version of CEF that supports the new activities columns (Target, Message, and Properties).
If the cefVersion parameter is included in the command, the tool ignores the cefCompliance parameter.
If the cefVersion parameter is omitted from the command, the tool uses the cef Compliance parameter.
<cef.flag>
: Enable the
true
CEF format.
If cefCompliance=true, the tool uses the true CEF format.
If cefCompliance=false, the tool uses the legacy CEF format.
If the parameter is omitted from the command, the value defaults to false and the tool uses the legacy CEF format.
<proxy.host>
and
<proxy.port>
: Connection details to the proxy server if connecting to the Forcepoint CASB management server through a proxy server.
UDM mapping table
Log Field
UDM Mapping
Logic
act
security_result.action
If
act
contains "ALLOW" (case-insensitive), set to "ALLOW". Otherwise, set to "BLOCK".
agt
principal.ip
Directly mapped.
ahost
principal.hostname
Directly mapped.
aid
principal.resource.id
Directly mapped.
amac
principal.mac
Directly mapped after replacing "-" with ":" and converting to lowercase.
at
principal.resource.name
Directly mapped.
atz
principal.location.country_or_region
Directly mapped.
av
principal.resource.attribute.labels.key
,
principal.resource.attribute.labels.value
av
is mapped to
key
and the value of
av
is mapped to
value
.
cs1
principal.user.email_addresses
Directly mapped.
deviceProcessName
target.resource.name
Directly mapped.
deviceZoneURI
target.url
Directly mapped.
dvc
target.ip
Directly mapped.
dvchost
target.hostname
Directly mapped.
event_name
metadata.product_event_type
,
metadata.event_type
Used in conjunction with
event_type
to populate
metadata.product_event_type
.  Also used to determine the
metadata.event_type
: "Login" ->
USER_LOGIN
, "Logout" ->
USER_LOGOUT
, "access event" ->
USER_UNCATEGORIZED
, otherwise (if
agt
is present) ->
STATUS_UPDATE
.
event_type
metadata.product_event_type
Used in conjunction with
event_name
to populate
metadata.product_event_type
.
msg
metadata.description
,
security_result.summary
Directly mapped to both fields.
product
metadata.vendor_name
Directly mapped.
request
extensions.auth.auth_details
,
extensions.auth.type
Directly mapped to
extensions.auth.auth_details
.
extensions.auth.type
is set to "SSO".
requestClientApplication
network.http.user_agent
Directly mapped.
shost
src.hostname
Directly mapped.
smb_host
intermediary.hostname
Directly mapped.
smb_uid
intermediary.user.userid
Directly mapped.
sourceServiceName
principal.platform_version
,
principal.platform
Directly mapped to
principal.platform_version
.
principal.platform
is derived based on the value of
sourceServiceName
: "Window" ->
WINDOWS
, "Linux" ->
LINUX
, "mac" or "iPhone" ->
MAC
.
sourceZoneURI
src.url
Directly mapped.
spriv
src.user.department
Directly mapped.
sproc
src.resource.attribute.labels.key
,
src.resource.attribute.labels.value
sproc
is mapped to
key
and the value of
sproc
is mapped to
value
.
src
src.ip
Directly mapped.
suid
principal.user.userid
Directly mapped.
timestamp
metadata.event_timestamp
Directly mapped.
ts_event
metadata.collected_timestamp
Directly mapped after parsing and converting to a timestamp.
value
metadata.product_name
Concatenated with "Forcepoint " to form the
metadata.product_name
. Set to "FORCEPOINT_CASB".
Need more help?
Get answers from Community members and Google SecOps professionals.
