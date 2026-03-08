# Collect Apache logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/apache/  
**Scraped:** 2026-03-05T09:49:46.186366Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Apache logs
Supported in:
Google secops
SIEM
This document explains how to ingest Apache logs to Google Security Operations using Bindplane. The parser code first attempts to parse the raw log message as JSON. If that fails, it uses regular expressions (
grok
patterns) to extract fields from the message based on common Apache log formats.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to an Apache instance.
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
'APACHE'
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
Configure Syslog in Apache
Sign in to the
Ubuntu
server using SSH.
Create a file under
/etc/rsyslog.d/
named
02-apache2.conf
:
vim
/etc/rsyslog.d/02-apache2.conf
Add the following code to the file:
module(load="imfile" PollingInterval="10" statefile.directory="/var/spool/rsyslog")
input(type="imfile"
        File="/var/log/apache2/access.log"
        Tag="http_access"
        Severity="info"
        Facility="local6")
Local6.info        @<bindplane-agnet-ip>:<vindplane-agent-port>
module(load="imfile" PollingInterval="10" statefile.directory="/var/spool/rsyslog")
input(type="imfile"
        File="/var/log/apache2/error.log"
        Tag="http_error"
Replace the
bindplane-agent-ip>
and
bindplane-agent-port
with the IP address and port configured for the Bindplane Agent
If you are using the TCP prototol, append an additional
@
to the host line so it will look like this:
@@<bindplane-agnet-ip>:<vindplane-agent-port>
.
Restart RSyslog services:
sudo
service
rsyslog
restart
UDM Mapping Table
Log field
UDM mapping
Logic
bytes
network.received_bytes
Bytes received from the client.
bytes
network.sent_bytes
Bytes sent to the client.
bytes_out
network.sent_bytes
Bytes sent to the client.
bytes_received
network.received_bytes
Bytes received from the client.
Content
network.http.method
HTTP method extracted from the "Content" field.
Content
target.url
Target URL extracted from the "Content" field.
cookie
additional.fields.value.string_value
Value of the "cookie" field.
dest_ip
target.ip
IP address of the target.
dest_name
target.hostname
Hostname of the target.
dest_port
target.port
Port of the target.
description
metadata.description
Description of the event.
duration_microseconds
additional.fields.value.string_value
Value of the "duration_microseconds" field.
file_full_path
target.file.full_path
Full path of the target file.
hostname
target.hostname
Hostname of the target.
http_content_type
additional.fields.value.string_value
Value of the "http_content_type" field.
http_host
principal.hostname
Hostname of the principal.
http_method
network.http.method
HTTP method.
http_referrer
network.http.referral_url
HTTP referrer URL.
http_user_agent
network.http.user_agent
HTTP user agent.
ID
metadata.id
ID of the event.
insertId
metadata.product_log_id
Product log ID.
ip
principal.ip
IP address of the principal.
jsonPayload.cIP
target.ip
IP address of the target.
jsonPayload.cPort
target.port
Port of the target.
jsonPayload.csBytes
network.sent_bytes
Bytes sent to the client.
jsonPayload.csMethod
network.http.method
HTTP method.
jsonPayload.csMimeType
target.file.mime_type
MIME type of the target file.
jsonPayload.csReferer
network.http.referral_url
HTTP referrer URL.
jsonPayload.csURL
target.url
Target URL.
jsonPayload.csUserAgent
network.http.user_agent
HTTP user agent.
jsonPayload.sHierarchy
additional.fields.value.string_value
Value of the "sHierarchy" field.
jsonPayload.sHostname
principal.hostname
Hostname of the principal.
jsonPayload.sIP
principal.ip
IP address of the principal.
jsonPayload.scBytes
network.received_bytes
Bytes received from the client.
jsonPayload.scHTTPStatus
network.http.response_code
HTTP response code.
jsonPayload.scResultCode
additional.fields.value.string_value
Value of the "scResultCode" field.
LastStatus
network.http.response_code
HTTP response code.
log_level
security_result.severity
Severity of the security result.
logName
security_result.category_details
Category details of the security result.
method
network.http.method
HTTP method.
pid
principal.process.pid
Process ID of the principal.
Port
target.port
Port of the target.
proto
network.application_protocol
Application protocol.
referer
network.http.referral_url
HTTP referrer URL.
RemoteHost
principal.ip
IP address of the principal.
RemoteUser
principal.user.userid
User ID of the principal.
resource.labels.instance_id
target.resource.product_object_id
Product object ID of the target resource.
resource.labels.project_id
target.resource.attribute.labels.value
Value of the "project_id" label.
resource.labels.zone
target.resource.attribute.cloud.availability_zone
Availability zone of the target resource.
resource.type
target.resource.resource_type
Resource type of the target.
response
network.http.response_code
HTTP response code.
SizeBytes
network.received_bytes
Bytes received from the client.
src_ip
principal.ip
IP address of the principal.
src_port
principal.port
Port of the principal.
ssl_cipher
network.tls.cipher
TLS cipher.
ssl_version
network.tls.version_protocol
TLS version protocol.
status
network.http.response_code
HTTP response code.
target
target.url
Target URL.
target_ip
target.ip
IP address of the target.
target_port
target.port
Port of the target.
time
metadata.event_timestamp
Event timestamp.
uri_path
target.process.file.full_path
Full path of the target file.
user
principal.user.userid
User ID of the principal.
useragent
network.http.user_agent
HTTP user agent.
version_protocol
network.tls.version_protocol
TLS version protocol.
Workername
principal.hostname
Hostname of the principal.
x_forwarded_for
Value of the "X-Forwarded-For" header.
metadata.log_type
The value is set to "APACHE" in the parser code.
metadata.product_name
The value is set to "Apache Web Server" in the parser code.
metadata.vendor_name
The value is set to "Apache" in the parser code.
metadata.event_type
The value is determined based on the presence of principal and target information. If both principal and target are present, the event type is set to "NETWORK_HTTP". If only principal is present, the event type is set to "STATUS_UPDATE". Otherwise, it is set to "GENERIC_EVENT".
additional.fields.key
The key is set to "keep_alive", "duration_microseconds", "cookie", "http_content_type", "sHierarchy", "scResultCode" in the parser code based on the field.
target.port
If the "proto" field is "HTTP", the port is set to 80. If the "proto" field is "HTTPS", the port is set to 443. If the "proto" field is "FTP", the port is set to 21.
target.resource.attribute.labels.key
The key is set to "project_id" in the parser code.
Need more help?
Get answers from Community members and Google SecOps professionals.
