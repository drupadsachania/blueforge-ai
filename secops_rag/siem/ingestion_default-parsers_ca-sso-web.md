# Collect Broadcom Symantec SiteMinder Web Access logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-sso-web/  
**Scraped:** 2026-03-05T09:20:45.070667Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Broadcom Symantec SiteMinder Web Access logs
Supported in:
Google secops
SIEM
This document explains how to collect Broadcom Symantec SiteMinder Web Access logs to Google Security Operations using a Bindplane agent. The parser transforms raw JSON formatted logs into a structured Unified Data Model (UDM). It extracts fields from the raw log messages using grok patterns, renames and maps them to the UDM schema, handles different event types and user formats, and ultimately enriches the data for security analysis.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Symantec SiteMinder.
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
creds
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
CA_SSO_WEB
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
Configure Syslog on Symantec SiteMinder - 12.8
Verify that an
X-windows server
is running on your system.
Open a terminal window.
Set the
DISPLAY
variable with the following command:
export DISPLAY=<IP_ADDRESS>:0.0
Replace
<IP_ADDRESS>
with the IP address of the system from which you are connecting to the console. (For example,
192.168.1.100
).
Sign in to the system hosting the console.
Go to the
<installation_directory>/siteminder/bin
directory.
Replace
<installation_directory>
with the location in the file system where the
Policy Server
is installed. (For example,
/opt/CA/siteminder
).
Open the console by running the following command:
./smconsole
Click the
Data
tab.
Click the
Database
drop-down list, and then select
Audit Logs
.
Click the
Storage
drop-down list, and then select
Syslog
.
Select the value
LOG_INFO
in the
Priority
field.
Select the value
LOG_LOCAL0
in the
Facility
field.
Click
OK
.
Restart the UNIX Policy Server
Sign in to the system hosting the Policy Server with the same user account that installed the Policy Server originally.
Open the Management Console.
Click the
Status
tab, and then click the
Stop
buttons.
Wait for all services to stop.
in the same
Status
tab, click the
Start
buttons.
UDM Mapping Table
Log Field
UDM Mapping
Logic
Action
event1.idm.read_only_udm.network.http.method
If the
Action
field is not empty, it is mapped to
event1.idm.read_only_udm.network.http.method
. If the value is
Visit
it is replaced with
GET
AgentName
event1.idm.read_only_udm.target.hostname
Directly mapped from the
AgentName
field.
ClientIp
event1.idm.read_only_udm.principal.ip
Extracted from the
ClientIp
field using a grok pattern to extract the IP address.
DomainName
event1.idm.read_only_udm.target.administrative_domain
Directly mapped from the
DomainName
field.
Event
event1.idm.read_only_udm.metadata.product_event_type
Directly mapped from the
Event
field.
Resource
event1.idm.read_only_udm.target.url
Directly mapped from the
Resource
field.
SessionId
event1.idm.read_only_udm.network.session_id
Directly mapped from the
SessionId
field.
Time
event1.idm.read_only_udm.metadata.event_timestamp
Parsed from the
Time
field using date filters to extract the timestamp.
UserName
event1.idm.read_only_udm.target.user.userid
The logic handles different formats of the
UserName
field and extracts the user ID.
UserName
event1.idm.read_only_udm.target.user.email_addresses
The logic handles different formats of the
UserName
field and extracts the user email address.
UserName
event1.idm.read_only_udm.target.user.group_identifiers
The logic handles different formats of the
UserName
field and extracts the group identifiers.
event1.idm.read_only_udm.extensions.auth.type
Set to
SSO
in the parser code.
event1.idm.read_only_udm.intermediary.hostname
Mapped from
logstash.process.host
.
event1.idm.read_only_udm.metadata.description
Set to the value of the
message
field in specific conditions related to the
Event
and
AgentName
fields.
event1.idm.read_only_udm.metadata.event_type
Determined based on the value of the
Event
field. Possible values: USER_LOGIN, USER_LOGOUT, USER_UNCATEGORIZED, GENERIC_EVENT
event1.idm.read_only_udm.metadata.log_type
Set to
CA_SSO_WEB
in the parser code.
event1.idm.read_only_udm.metadata.product_name
Set to
Web Access Management
in the parser code.
event1.idm.read_only_udm.metadata.vendor_name
Set to
Siteminder
in the parser code.
event1.idm.read_only_udm.observer.hostname
Set to the value of
logstash.collect.host
.
event1.idm.read_only_udm.security_result.action
Determined based on the value of the
Event
field. Possible values: ALLOW, BLOCK
Need more help?
Get answers from Community members and Google SecOps professionals.
