# Collect Radware WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-firewall/  
**Scraped:** 2026-03-05T09:59:29.498318Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Radware WAF logs
Supported in:
Google secops
SIEM
This document explains how to collect the Radware Web Application Firewall (WAF) logs by using a Google Security Operations forwarder.
The parser extracts fields from Radware firewall syslog messages using grok patterns, and maps them to the UDM. It handles various log formats, populates security result fields based on attack details, and categorizes events based on
attack_id
, enriching the data for Google SecOps ingestion.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that Radware Vision Reporter is installed and configured on AppWall.
Ensure that you have privileged access to Radware WAF portal.
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
system where Bindplane Agent will be installed.
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
Install Bindplane Agent
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
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
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
# Replace with your specific IP and port
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
# Path to the ingestion authentication file
creds
:
'/path/to/your/ingestion-auth.json'
# Your Chronicle customer ID
customer_id
:
'your_customer_id'
endpoint
:
malachiteingestion-pa.googleapis.com
ingestion_labels
:
log_type
:
SYSLOG
namespace
:
radware_waf
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
Restart Bindplane Agent to apply the changes
To restart the Bindplane Agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane Agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Radware AppWall WAF
To complete the tasks, do the following three configurations:
Configure the AppWall standalone using Vision Reporter.
Configure the integrated AppWall in Alteon using Vision Reporter (include HTTP request data in event details).
Configure Vision Reporter to Send Logs to Bindplane Agent.
Configure AppWall Standalone using Vision Reporter
Sign in to
Radware WAF
console using administrator credentials.
Go to
Configuration
>
Services
>
Vision Support
>
Vision Reporter
.
Enable logging by
selecting
the
Send events to Vision Reporter
checkbox.
Vision Reporter address
: enter the
IP address
of the Vision Reporter.
Port
: enter the port number.
Protocol
: select
UDP
or
TCP
.
To include
HTTP response data
, select the
Send replies to Vision Reporter
checkbox.
Click
Save
.
Configure Integrated AppWall in Alteon using Vision Reporter (preferred for HTTP Request Data Logging)
Sign in to Radware WAF console using administrator credentials.
Go to
Configuration
>
Security
>
Web Security
>
Vision Reporter
.
Enable logging by
selecting
the
Send events to Vision Reporter
checkbox.
Select the
Send events to Vision reporter
checkbox.
Vision Reporter IP address
: enter the IP address of the Vision Reporter.
Port
: enter a high port number.
Security
: select
UDP
or
TCP
.
Click
Save
.
Configure Vision Reporter to send logs to Bindplane Agent
Sign in to Radware Vision Reporter administrator console.
Go to
Configuration
>
SIEM & External Logging
.
Click
+ Add New SIEM Destination
.
Destination Name
: enter
Google SecOps Forwarder
.
Log Export Type
: select
Syslog
(RFC 5424 format) for structured logging.
Remote Syslog Server IP
enter the Bindplane Agent's IP address.
Port
: enter a port that the Bindplane Agent listens on (for example, 514 for UDP, 601 for TCP).
Protocol
: select
UDP
or
TCP
depending on the Bindplane configuration.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
event.idm.read_only_udm.security_result.action
If
action
is "drop", set to "BLOCK".
attack_desc
event.idm.read_only_udm.security_result.description
Directly mapped.
attack_type
event.idm.read_only_udm.security_result.threat_name
Directly mapped.
command
event.idm.read_only_udm.principal.process.command_line
Directly mapped.
description
event.idm.read_only_udm.security_result.description
Directly mapped if
attack_desc
is empty.
dst_ip
event.idm.read_only_udm.target.ip
Directly mapped.
dst_port
event.idm.read_only_udm.target.port
Directly mapped, converted to integer. Set to "MACHINE" if
username
is present and
command
is not. Copied from the
collection_time
field of the raw log.  Defaults to "NETWORK_CONNECTION". Set to "GENERIC_EVENT" if either
src_ip
or
dst_ip
are missing. Set to "USER_LOGIN" if
username
is present and
command
is not present. Can be overridden by logic based on
attack_id
. Set to "RADWARE_FIREWALL". Mapped from the
product
field. Set to "Radware".
intermediary_ip
event.idm.read_only_udm.intermediary.ip
Directly mapped.
obv_ip
event.idm.read_only_udm.observer.ip
Directly mapped.
product
event.idm.read_only_udm.metadata.product_name
Directly mapped.
protocol_number_src
event.idm.read_only_udm.network.ip_protocol
Parsed using the
parse_ip_protocol.include
logic.
rule_id
event.idm.read_only_udm.security_result.rule_id
Directly mapped. Derived based on the value of
attack_id
.  Values include "ACL_VIOLATION", "NETWORK_DENIAL_OF_SERVICE", "NETWORK_SUSPICIOUS", "NETWORK_RECON".
src_ip
event.idm.read_only_udm.principal.ip
Directly mapped.
src_port
event.idm.read_only_udm.principal.port
Directly mapped, converted to integer.
ts
event.idm.read_only_udm.metadata.event_timestamp
Parsed and converted to timestamp.
username
event.idm.read_only_udm.target.user.userid
Directly mapped if
command
is not present.
username
event.idm.read_only_udm.principal.user.userid
Directly mapped if
command
is present.
Need more help?
Get answers from Community members and Google SecOps professionals.
