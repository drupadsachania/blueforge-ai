# Collect NGINX logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nginx/  
**Scraped:** 2026-03-05T09:58:36.621655Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect NGINX logs
Supported in:
Google secops
SIEM
This NGINX parser handles JSON and syslog formatted logs. It extracts fields from various log formats and normalizes them into the UDM format. The parser enriches the event with metadata for server management and network activity, including user logins and HTTP requests. It also handles logic for SSH events and populates UDM fields based on extracted data.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
NGINX is running and generating logs
Root access to NGINX host machine
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
'NGINX'
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
Identify NGINX log files location
Typically NGINX logs are stored in:
Access logs
:
/var/log/nginx/access.log
Error logs
:
/var/log/nginx/error.log
Access NGINX host using administrative credentials.
Run the following command and look for the path to logs on your NGINX host:
sudo
cat
/etc/nginx/nginx.conf
|
grep
log
Configure NGINX to forward logs to Bindplane
Open the NGINX configuration file (for example,
/etc/nginx/nginx.conf
):
sudo
vi
/etc/nginx/nginx.conf
Edit the configuration, replacing
<BINDPLANE_SERVER>
and
<BINDPLANE_PORT>
with your values:
http {
    access_log syslog:server=<BINDPLANE_SERVER>:<BINDPLANE_PORT>,facility=local7,tag=nginx_access;
    error_log syslog:server=<BINDPLANE_SERVER>:<BINDPLANE_PORT>,facility=local7,tag=nginx_error;
}
Restart NGINX to apply the changes:
sudo
systemctl
reload
nginx
UDM Mapping Table
Log Field
UDM Mapping
Logic
_Internal_WorkspaceResourceId
target.resource.product_object_id
Directly mapped
Computer
principal.asset.hostname
Directly mapped
Facility
additional.fields[
facility
]
Directly mapped
HostName
principal.asset.hostname
Directly mapped if
src_ip
is not present
ProcessName
principal.application
Directly mapped
SeverityLevel
security_result.severity
Mapped to INFORMATIONAL if the value is
info
SourceSystem
principal.asset.platform
Mapped to LINUX if the value matches
Linux
SyslogMessage
Multiple fields
Parsed using grok to extract
time
,
method
,
target_path
,
protocol
,
response_code
,
referral_url
,
user_agent
,
target_ip
,
target_host
, and
cache
TenantId
additional.fields[
TenantId
]
Directly mapped
acct
principal.user.user_id
Directly mapped if not empty or
?
addr
principal.asset.ip
Directly mapped
audit_epoch
metadata.event_timestamp
Converted to timestamp using the
UNIX
format. Nanoseconds are extracted from the original log message.
cache
additional.fields[
cache
]
Directly mapped
collection_time.nanos
metadata.event_timestamp.nanos
Used for nanoseconds of the event timestamp if available
collection_time.seconds
metadata.event_timestamp.seconds
Used for seconds of the event timestamp if available
data
Multiple fields
The main source of data, parsed differently based on the log format (Syslog, JSON, or other)
exe
target.process.command_line
Directly mapped after removing backslashes and quotes
hostname
principal.asset.hostname
OR
principal.asset.ip
If it is an IP address, mapped to
principal.asset.ip
. Otherwise, mapped to
principal.asset.hostname
msg
metadata.description
Directly mapped as the description
node
target.asset.hostname
Directly mapped
pid
target.process.pid
Directly mapped
protocol
network.application_protocol
Mapped to HTTP if the value matches
HTTP
referral_url
network.http.referral_url
Directly mapped if not empty or
-
res
security_result.action_details
Directly mapped
response_code
network.http.response_code
Directly mapped and converted to integer
ses
network.session_id
Directly mapped
src_ip
principal.asset.ip
Directly mapped
target_host
target.asset.hostname
Directly mapped
target_ip
target.asset.ip
Directly mapped, after converting the string representation to a JSON array and then extracting individual IPs
target_path
target.url
Directly mapped
time
metadata.event_timestamp
Parsed to extract the timestamp using the format
dd/MMM/yyyy:HH:mm:ss Z
user_agent
network.http.user_agent
Directly mapped if not empty or
-
metadata.event_type
Set to
GENERIC_EVENT
initially, then potentially overwritten based on other fields like
terminal
and
protocol
. Defaults to
USER_UNCATEGORIZED
if the main grok pattern does not match. Set to
NETWORK_HTTP
if
protocol
is HTTP and
target_ip
is present, and
STATUS_UPDATE
if
protocol
is HTTP but
target_ip
is not present
metadata.log_type
Set to
NGINX
metadata.product_name
Set to
NGINX
metadata.vendor_name
Set to
NGINX
network.ip_protocol
Set to
TCP
if
terminal
is
sshd
or
ssh
, or if the main grok pattern does not match
principal.asset_id
Set to
GCP.GCE:0001
if
terminal
is
sshd
or
ssh
. Set to
GCP.GCE:0002
if the main grok pattern does not match
extensions.auth.type
Set to
MACHINE
if
terminal
is
sshd
or
ssh
Need more help?
Get answers from Community members and Google SecOps professionals.
