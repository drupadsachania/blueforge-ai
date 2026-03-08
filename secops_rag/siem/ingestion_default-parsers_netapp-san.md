# Collect NetApp SAN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-san/  
**Scraped:** 2026-03-05T09:26:48.734288Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect NetApp SAN logs
Supported in:
Google secops
SIEM
This document explains how to ingest NetApp SAN logs to Google Security Operations using a Bindplane agent. The parser extracts fields from NetApp SAN logs using Grok patterns, then maps those extracted fields to the Google SecOps UDM, enriching the data with static vendor and product information for standardized security analysis. If the log entry doesn't match the expected pattern, it's dropped as having no security value.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to NetApp SAN.
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
NETAPP_SAN
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
Configure Syslon in NetApp SAN
Sign in to the NetApp SAN web UI.
Go to
Configuration
>
Monitoring
>
Audit and syslog server
.
Click
Configure external syslog server
or
Edit external syslog server
.
Provide the following configuration details:
Host
: enter the Bindplane IP address.
Port
: enter the Bindplane port number; for example,
514
for UDP.
Protocol
: Select
UDP
.
Click
Continue
.
Enable and select the following Syslog content:
Send audit logs
: enable and set
Severity:Informational(6)
,
facility:local7
.
Send security events
: enable and set
Severity:Passthrough
,
facility:Passthrough
.
Send application logs
: keep this disabled.
Click
Continue
.
Send a log test message.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
datetime
metadata.event_timestamp.seconds
Extracted from the log message using the grok pattern
%{SYSLOGTIMESTAMP:datetime}
and converted to epoch seconds.
desc
metadata.description
Extracted from the log message using the grok pattern
%{GREEDYDATA:desc}
.
ip
principal.ip
Extracted from the log message using the grok pattern
%{IP:ip}
.
log_level
Used to determine the value of
security_result.severity
.
port
principal.port
Extracted from the log message using the grok pattern
%{INT:port}
and converted to an integer.
request
security_result.summary
Extracted from the log message using the grok pattern
%{DATA:request}
.
userid
principal.user.userid
Extracted from the log message using the grok pattern
%{WORD:userid}
.
N/A
metadata.event_type
Set to
STATUS_UPDATE
by the parser.
N/A
metadata.log_type
Populated from the incoming log metadata.
N/A
metadata.product_name
Set to
Storage Area Network
by the parser.
N/A
metadata.vendor_name
Set to
NetApp
by the parser.
N/A
security_result.severity
Set to
ERROR
if
log_level
is
Error
.
Need more help?
Get answers from Community members and Google SecOps professionals.
