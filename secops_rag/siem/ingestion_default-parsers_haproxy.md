# Collect HAProxy logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/haproxy/  
**Scraped:** 2026-03-05T09:25:13.197940Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect HAProxy logs
Supported in:
Google secops
SIEM
This document explains how to ingest HAProxy logs to Google Security Operations
using Bindplane. The Logstash parser extracts fields from HAProxy syslog
messages using a series of Grok pattern matching rules, specifically designed
to handle various HAProxy log formats. It then maps the extracted fields to the
Unified Data Model (UDM), enriching the data with additional context and
standardizing the representation for further analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to HAProxy
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
ingestion_labels
:
log_type
:
'HAPROXY'
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
Configure Syslog for HAProxy
Sign in to
HAproxy
using CLI.
Add the
log
directive in the
global
section to the
Configuration
to forward Syslog messages over
UDP
.
Replace
<bindplane-ips>
with the actual Bindplane agent IP address.
global
  log <bindplane-ip>:514 local0

defaults
  log global
UDM mapping table
Log field
UDM mapping
Logic
accept_date_ms
actconn
backend_name
backend_queue
beconn
bytes_read
network.received_bytes
Extracted from
bytes_read
field in the log and converted to an unsigned integer.
captured_request_headers
client_ip
principal.ip
Extracted from
client_ip
field in the log.
client_port
principal.port
Extracted from
client_port
field in the log and converted to an integer.
command_description
metadata.description
Extracted from
command_description
field in the log, if available. Otherwise, it's derived from other fields like
action
or
status
depending on the log message.
datetime
metadata.event_timestamp.seconds
Extracted from
datetime
field in the log, if available. Otherwise, it's derived from the
timestamp
field in the log entry.
description
metadata.description
Extracted from
description
field in the log, if available. Otherwise, it's derived from other fields like
command_description
or
action
depending on the log message.
feconn
frontend_name
http_request
target.url
Extracted from
http_request
field in the log.
http_status_code
network.http.response_code
Extracted from
http_status_code
field in the log and converted to an integer.
http_verb
network.http.method
Extracted from
http_verb
field in the log.
http_version
metadata.product_version
Extracted from
http_version
field in the log and formatted as
HTTP/{version}
.
initiator
target.application
Extracted from
initiator
field in the log.
module
msg
security_result.summary
Extracted from
msg
field in the log.
pid
target.process.pid
Extracted from
pid
field in the log.
process
process_name
target.application
Extracted from
process_name
field in the log.
retries
server_name
target.hostname
Extracted from
server_name
field in the log. If empty, it defaults to the value of
syslog_server
.
severity
security_result.severity
Mapped from
severity
field in the log.
WARNING
maps to
MEDIUM
,
ALERT
maps to
CRITICAL
, and
NOTICE
maps to
INFORMATIONAL
.
shell
srv_queue
srvconn
status
syslog_server
target.hostname, intermediary.hostname
Extracted from
syslog_server
field in the log. Used for both target hostname (if
server_name
is empty) and intermediary hostname.
syslog_timestamp
syslog_timestamp_1
syslog_timestamp_2
syslog_timestamp_4
target_ip
time_backend_connect
time_backend_response
time_duration
time_queue
time_request
timestamp
metadata.event_timestamp.seconds
Extracted from
timestamp
field in the log and parsed for date and time information. Used as the event timestamp.
unknown_parameters1
unknown_parameters2
user_name
target.user.userid
Extracted from
user_name
field in the log.
metadata.event_type
Set to
NETWORK_HTTP
by default. Changed to specific event types like
PROCESS_UNCATEGORIZED
,
STATUS_UPDATE
, or
USER_UNCATEGORIZED
based on the log message and parsed fields.
metadata.vendor_name
Set to
HAProxy Enterprise
.
metadata.product_name
Set to
HAProxy
.
network.application_protocol
Set to
HTTP
if the
message
field contains
HTTP
.
metadata.log_type
Set to
HAPROXY
.
Need more help?
Get answers from Community members and Google SecOps professionals.
