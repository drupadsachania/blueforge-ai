# Collect Forcepoint Web Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-webproxy/  
**Scraped:** 2026-03-05T09:24:38.752842Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forcepoint Web Security logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forcepoint Web Security logs to Google Security Operations using Bindplane.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
for the Bindplane agent
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Forcepoint Web Security management console or Forcepoint Security Manager
Network connectivity between Forcepoint Web Security and the Bindplane agent host
Forcepoint Web Security version 7.8 or later (recommended for CEF format support)
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
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
You can configure the Bindplane agent to receive syslog messages over
TCP
or
UDP
. Choose the protocol that best fits your environment and network requirements.
Choose your protocol
TCP (Recommended for reliability)
: Provides delivery and is suitable for most environments. Use TCP when reliable log delivery is critical and you want to ensure no logs are lost due to network issues.
UDP (Recommended for performance)
: Offers lower latency and less overhead. Use UDP when high throughput is required and occasional log loss is acceptable.
Configure the Bindplane agent
Access the Configuration File:
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
file with the configuration for your chosen protocol:
Option A: TCP Configuration (Recommended)
receivers
:
tcplog
:
# Replace with your desired port and IP address
listen_address
:
"0.0.0.0:514"
# Add operators if specific parsing is needed
operators
:
[]
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
YOUR_CUSTOMER_ID
>
# Replace with the appropriate regional endpoint
endpoint
:
<
CUSTOMER_REGION_ENDPOINT
>
# Log type for Forcepoint Web Security
log_type
:
'FORCEPOINT_WEBPROXY'
raw_log_field
:
body
# You can optionally add other custom ingestion labels here if needed
ingestion_labels
:
service
:
pipelines
:
logs/forcepoint_tcp_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/chronicle_w_labels
Option B: UDP Configuration
receivers
:
udplog
:
# Replace with your desired port and IP address
listen_address
:
"0.0.0.0:514"
# Add operators if specific parsing is needed
operators
:
[]
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
YOUR_CUSTOMER_ID
>
# Replace with the appropriate regional endpoint
endpoint
:
<
CUSTOMER_REGION_ENDPOINT
>
# Log type for Forcepoint Web Security
log_type
:
'FORCEPOINT_WEBPROXY'
raw_log_field
:
body
# You can optionally add other custom ingestion labels here if needed
ingestion_labels
:
service
:
pipelines
:
logs/forcepoint_udp_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure (default is
0.0.0.0:514
).
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
To verify the agent is running in Linux, run the following command:
sudo
systemctl
status
observiq-otel-collector
To verify the agent is running in Windows, run the following command:
sc query observiq-otel-collector
Configure Syslog forwarding on Forcepoint Web Security
Configure Forcepoint Web Security to forward logs to the Bindplane agent in CEF (Common Event Format) format.
Using Forcepoint Security Manager
Sign in to the
Forcepoint Security Manager
with administrative credentials.
Go to
Settings
>
Logging
.
In the left navigation, select
Log Servers
.
Click
Add
to create a new log server configuration.
Provide the following configuration details:
Server Type
: Select
Syslog Server
or
CEF Server
.
Name
: Enter a descriptive name (for example,
Google Security Operations Bindplane CEF
).
Host
: Enter the Bindplane agent IP address or hostname.
Port
: Enter the Bindplane agent port number (for example,
514
).
Protocol
: Select the protocol that matches your Bindplane configuration:
Select
TCP
if you configured
tcplog
receiver in Bindplane (recommended).
Select
UDP
if you configured
udplog
receiver in Bindplane.
Format
: Select
CEF
(Common Event Format).
Facility
: Select
Local0
(or another available facility).
Severity
: Select
Informational
(to capture all log levels).
Under
Log Categories
or
Event Types
, select the events to forward:
☑
Web Access Logs
(transaction logs)
☑
Security Events
(threat detections)
☑
Authentication Events
(user login/logout)
☑
System Events
(system and configuration changes)
Or select
All Events
to forward all available log types.
Optional: Configure additional settings:
Batch Size
: Set to
1
for real-time forwarding or higher for batch processing.
Message Format
: Ensure CEF format is selected.
Include User Information
: Enable to include user identity in logs.
Click
Test Connection
to verify connectivity to the Bindplane agent.
A test message should appear in the Bindplane agent logs.
If the test fails, verify network connectivity and firewall rules.
Click
Save
to apply the configuration.
Click
Deploy
to push the configuration to all Forcepoint Web Security gateways.
Using Forcepoint Web Security Appliance (direct configuration)
If you are configuring directly on the appliance:
Sign in to the
Forcepoint Web Security Appliance
management interface.
Go to
System
>
Log Server
.
Click
Add
or
Edit
to create or modify a log server.
Provide the following configuration details:
Server Address
: Enter the Bindplane agent IP address.
Port
: Enter
514
(or your custom port).
Protocol
: Select
TCP
or
UDP
to match your Bindplane configuration.
Format
: Select
CEF
or
Common Event Format
.
Facility
: Select
Local0
.
Under
Log Types
, select the logs to forward:
☑
Access Logs
☑
Security Logs
☑
Admin Logs
Click
Apply
or
Save
.
If using multiple appliances, repeat this configuration on each appliance.
CEF Format Verification
Forcepoint Web Security sends logs in CEF format with the following structure:
CEF:0|Forcepoint|Web Security|<version>|<event_id>|<event_name>|<severity>|<extensions>
Example CEF log:
CEF:0|Forcepoint|Web Security|8.5|100|Web Request|5|src=192.168.1.100 dst=93.184.216.34 spt=54321 dpt=80 requestMethod=GET request=http://example.com/ cs1=Allow cs1Label=Action cs2=News and Media cs2Label=Category suser=john.doe@company.com
 ```
The Google SecOps parser expects CEF format and will extract the following key fields:
src
- Source IP address
dst
- Destination IP address
spt
- Source port
dpt
- Destination port
requestMethod
- HTTP method
request
or
url
- Requested URL
cs1
- Action (Allow/Block)
cs2
- URL category
suser
- Username
Verify logs are being ingested
After configuration, verify that logs are flowing from Forcepoint Web Security to Google SecOps:
In the Forcepoint console, verify that logs are being sent:
Go to
Settings
>
Logging
>
Log Servers
.
Check the
Status
column for your configured server - it should show
Active
or
Connected
.
View
Statistics
to see the number of logs sent.
On the Bindplane agent host, check the agent logs for incoming syslog messages:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
Look for log entries containing CEF format messages:
CEF:0|Forcepoint|Web Security|...
Windows:
Select the Windows Event Viewer under
Applications and Services Logs
>
observIQ
.
In Google SecOps, verify logs are appearing:
Go to
Search
>
UDM Search
.
Use the following query:
metadata.vendor_name = "Forcepoint" AND metadata.product_name = "Forcepoint Webproxy"
Adjust the time range to recent hours (for example,
Last 1 hour
).
Verify that events appear in the results.
Verify specific fields are being parsed correctly:
metadata.vendor_name = "Forcepoint" AND principal.ip != "" AND target.url != ""
Go to
SIEM Settings
>
Collection Agents
to view ingestion statistics:
Select
Events received
count.
Verify
Last succeeded on
timestamp is recent.
Troubleshooting
No logs appearing in Google SecOps
Symptoms
: Bindplane agent is running, but no logs appear in Google SecOps.
Possible causes
:
Network connectivity issues between Forcepoint and Bindplane agent.
Firewall blocking the syslog port.
Protocol mismatch (TCP configured in Bindplane but UDP configured in Forcepoint, or vice versa).
Incorrect Bindplane agent IP address or port in Forcepoint configuration.
Incorrect regional endpoint configured in Bindplane.
CEF format not enabled in Forcepoint.
Solution
:
Verify network connectivity:
# From Forcepoint gateway, test connectivity to BindPlane host
telnet
<BINDPLANE_IP>
514
# Or for UDP
nc
-u
<BINDPLANE_IP>
514
Check firewall rules on the Bindplane host:
# Linux - Allow port 514 TCP
sudo
ufw
allow
514
/tcp
# Or for UDP
sudo
ufw
allow
514
/udp
# Verify firewall status
sudo
ufw
status
Verify protocol match:
Check Bindplane
config.yaml
for
tcplog
or
udplog
.
Check Forcepoint log server configuration for matching protocol.
Verify CEF format is enabled:
In Forcepoint Security Manager, go to
Settings
>
Logging
>
Log Servers
.
Verify
Format
is set to
CEF
or
Common Event Format
.
Verify regional endpoint:
Check that the
endpoint
in
config.yaml
matches your Google SecOps instance region.
See
Regional Endpoints documentation
.
Check the Bindplane agent logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-n
100
--no-pager
Look for error messages such as:
connection refused
- Network/firewall issue
authentication failed
- Credential issue
invalid endpoint
- Regional endpoint issue
Protocol mismatch errors
Symptoms
: Logs are not received, connection errors in Forcepoint test, or
Connection refused
errors in Bindplane logs.
Solution
:
Ensure the protocol configured in Bindplane (
tcplog
or
udplog
) matches the protocol configured in Forcepoint (TCP or UDP).
If using TCP and experiencing connection issues, verify the Bindplane agent is listening:
# Linux - Check if port is listening
sudo
netstat
-tuln
|
grep
514
# Or
sudo
ss
-tuln
|
grep
514
If the port is not listening, restart the Bindplane agent.
Authentication errors
Symptoms
: The Bindplane agent logs show authentication errors to Google SecOps.
Possible causes
:
Incorrect customer ID.
Invalid or expired ingestion authentication file.
Incorrect path to ingestion authentication file.
Incorrect regional endpoint.
Solution
:
Verify customer ID in
config.yaml
matches the ID from
SIEM Settings
>
Profile
.
Re-download the ingestion authentication file from
SIEM Settings
>
Collection Agents
.
Verify the path in
config.yaml
points to the correct location.
Verify the regional endpoint matches your Google SecOps instance region.
Ensure the Bindplane agent has read permissions on the authentication file:
sudo
chmod
644
/path/to/ingestion-authentication-file.json
sudo
chown
root:root
/path/to/ingestion-authentication-file.json
Logs appearing but fields not parsed
Symptoms
: Logs appear in Google SecOps but fields like
principal.ip
,
target.url
are empty.
Possible causes
:
Logs are not in CEF format.
CEF format is malformed or non-standard.
Log type mismatch in Bindplane configuration.
Solution
:
Verify CEF format in raw logs:
In Google SecOps, go to
Search
>
Raw Log Search
.
Search for recent Forcepoint logs.
Verify logs start with
CEF:0|Forcepoint|Web Security|
.
If logs are not in CEF format:
In Forcepoint, change
Format
to
CEF
or
Common Event Format
.
Redeploy the configuration.
Verify log type in Bindplane
config.yaml
:
Ensure
log_type: 'FORCEPOINT_PROXY'
is set correctly.
Check for CEF field name variations:
Some Forcepoint versions may use different CEF field names.
Verify field names match the expected CEF extensions in the UDM mapping table.
High latency or log delays
Symptoms
: Logs appear in Google SecOps with significant delay (more than 5 minutes).
Possible causes
:
Network latency between Forcepoint and the Bindplane agent.
Bindplane agent resource constraints (CPU/memory).
Batch processing enabled in Forcepoint.
Google SecOps ingestion backlog.
Solution
:
Verify network latency:
ping
<BINDPLANE_IP>
# Check for high latency (>50ms) or packet loss
Check Bindplane agent resource usage:
top
# Look for observiq-otel-collector process
# Verify CPU < 80% and memory is available
In Forcepoint, adjust batch settings:
Go to
Settings
>
Logging
>
Log Servers
.
Set
Batch Size
to
1
for real-time forwarding.
Or reduce batch interval for more frequent sends.
Consider scaling the Bindplane agent host (more CPU/memory) if resource-constrained.
If using UDP, verify network infrastructure supports the required throughput without packet loss.
Forcepoint test connection fails
Symptoms
: When clicking
Test Connection
in Forcepoint, the test fails.
Solution
:
Verify Bindplane agent is running:
sudo
systemctl
status
observiq-otel-collector
Verify the Bindplane agent is listening on the configured port:
sudo
netstat
-tuln
|
grep
514
Temporarily disable the firewall to test:
# Linux
sudo
ufw
disable
# Test connection from Forcepoint
# Then re-enable
sudo
ufw
enable
Check Bindplane agent logs during the test:
sudo
journalctl
-u
observiq-otel-collector
-f
You should see an incoming connection attempt.
If the test still fails, verify IP address and port are correct in Forcepoint configuration.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.summary
If
action_msg
is not empty, it is mapped to
security_result.summary
. Otherwise, if
action
is not empty, it is mapped to
security_result.summary
. Otherwise, if
act
is not empty, it is mapped to
security_result.summary
.
action_msg
security_result.summary
If
action_msg
is not empty, it is mapped to
security_result.summary
. Otherwise, if
action
is not empty, it is mapped to
security_result.summary
. Otherwise, if
act
is not empty, it is mapped to
security_result.summary
.
app
target.application
If
destinationServiceName
is not empty, it is mapped to
app_name
. Otherwise, if
app
is not empty and does not contain http or HTTP, it is mapped to
app_name
. Finally,
app_name
is mapped to
target.application
.
bytes_in
network.received_bytes
If
in
is not empty, it is mapped to
bytes_in
. Finally,
bytes_in
is mapped to
network.received_bytes
.
bytes_out
network.sent_bytes
If
out
is not empty, it is mapped to
bytes_out
. Finally,
bytes_out
is mapped to
network.sent_bytes
.
cat
security_result.category_details
If
cat
is not empty, it is mapped to
category
. Finally,
category
is mapped to
security_result.category_details
.
category_no
security_result.detection_fields.value
If
category_no
is not empty, it is mapped to
security_result.detection_fields.value
with key
Category Number
.
cn1
security_result.detection_fields.value
If
cn1
is not empty, it is mapped to
security_result.detection_fields.value
with key
Disposition Number
.
ContentType
target.file.mime_type
If
contentType
is not empty, it is mapped to
ContentType
. Finally,
ContentType
is mapped to
target.file.mime_type
.
cs1
target_role.description
cs1
is mapped to
target_role.description
.
cs2
security_result.category_details
If
cs2
is not empty and not
0
, it is mapped to
security_result.category_details
with the prefix
Dynamic Category:
.
cs3
target.file.mime_type
cs3
is mapped to
target.file.mime_type
.
description
metadata.description
If
description
is not empty, it is mapped to
metadata.description
.
destinationServiceName
target.application
If
destinationServiceName
is not empty, it is mapped to
app_name
. Finally,
app_name
is mapped to
target.application
.
deviceFacility
metadata.product_event_type
If
product_event
and
deviceFacility
are not empty, they are concatenated with
-
and mapped to
metadata.product_event_type
. Otherwise,
product_event
is mapped to
metadata.product_event_type
.
disposition
security_result.detection_fields.value
If
disposition
is not empty, it is mapped to
security_result.detection_fields.value
with key
Disposition Number
.
dst
target.ip
If
dst
is not empty and
dvchost
is empty, it is mapped to
dst_ip
. Finally,
dst_ip
is mapped to
target.ip
.
dst_host
target.hostname
If
dst
is not empty and
dvchost
is empty, it is mapped to
dst_host
. Finally,
dst_host
is mapped to
target.hostname
.
dst_ip
target.ip
If
dst
is not empty and
dvchost
is empty, it is mapped to
dst_ip
. Finally,
dst_ip
is mapped to
target.ip
.
dst_port
target.port
If
dst
is not empty and
dvchost
is empty, it is mapped to
dst_port
. Finally,
dst_port
is mapped to
target.port
.
duration
network.session_duration.seconds
If
duration
is not empty and not
0
, it is mapped to
network.session_duration.seconds
.
dvchost
intermediary.ip
If
dvchost
is not empty, it is mapped to
int_ip
. Finally,
int_ip
is mapped to
intermediary.ip
if it is a valid IP address, otherwise it is mapped to
intermediary.hostname
.
file_path
target.file.full_path
If
file_path
is not empty, it is mapped to
target.file.full_path
.
host
principal.ip
If
host
is not empty, it is mapped to
src
. Finally,
src
is mapped to
principal.ip
.
http_method
network.http.method
If
requestMethod
is not empty, it is mapped to
http_method
. Otherwise, if
method
is not empty, it is mapped to
http_method
. Finally,
http_method
is mapped to
network.http.method
.
http_proxy_status_code
network.http.response_code
If
http_response
is empty or
0
or
-
, and
http_proxy_status_code
is not empty, it is mapped to
network.http.response_code
.
http_response
network.http.response_code
If
http_response
is not empty and not
0
and not
-
, it is mapped to
network.http.response_code
.
http_user_agent
network.http.user_agent
If
http_user_agent
is not empty and not
-
it is mapped to
network.http.user_agent
.
in
network.received_bytes
If
in
is not empty, it is mapped to
bytes_in
. Finally,
bytes_in
is mapped to
network.received_bytes
.
int_host
intermediary.hostname
If
int_ip
is not empty and
int_host
is not empty and different from
int_ip
, it is mapped to
intermediary.hostname
.
int_ip
intermediary.ip
If
dvchost
is not empty, it is mapped to
int_ip
. Finally,
int_ip
is mapped to
intermediary.ip
if it is a valid IP address, otherwise it is mapped to
intermediary.hostname
.
level
target_role.name
If
level
is not empty and
role
is empty, it is mapped to
role
. Finally,
role
is mapped to
target_role.name
.
log_level
security_result.severity
If
severity
is
1
or
log_level
contains
info
or
message
contains
notice
,
security_result.severity
is set to
INFORMATIONAL
. If
severity
is
7
,
security_result.severity
is set to
HIGH
.
loginID
principal.user.userid
If
loginID
is not empty, it is mapped to
user
. Finally, if
user
is not empty and not
-
, and does not contain
LDAP
, it is mapped to
principal.user.userid
.
method
network.http.method
If
requestMethod
is not empty, it is mapped to
http_method
. Otherwise, if
method
is not empty, it is mapped to
http_method
. Finally,
http_method
is mapped to
network.http.method
.
NatRuleId
security_result.detection_fields.value
If
NatRuleId
is not empty, it is mapped to
security_result.detection_fields.value
with key
NatRuleId
.
out
network.sent_bytes
If
out
is not empty, it is mapped to
bytes_out
. Finally,
bytes_out
is mapped to
network.sent_bytes
.
pid
target.process.pid
If
pid
is not empty, it is mapped to
target.process.pid
.
policy
target_role.description
If
Policy
is not empty, it is mapped to
policy
. If
policy
is not empty and not
-
, it is mapped to
target_role.description
.
Policy
target_role.description
If
Policy
is not empty, it is mapped to
policy
. If
policy
is not empty and not
-
, it is mapped to
target_role.description
.
product_event
metadata.product_event_type
If
product
is not empty, it is mapped to
product_event
. If
product_event
and
deviceFacility
are not empty, they are concatenated with
-
and mapped to
metadata.product_event_type
. Otherwise,
product_event
is mapped to
metadata.product_event_type
.
proxyStatus-code
network.http.response_code
If
http_response
is empty or
0
or
-
, and
http_proxy_status_code
is empty and
proxyStatus-code
is not empty, it is mapped to
network.http.response_code
.
refererUrl
network.http.referral_url
If
refererUrl
is not empty and not
-
, it is mapped to
network.http.referral_url
.
requestClientApplication
network.http.user_agent
If
requestMethod
is not empty, it is mapped to
http_user_agent
. Finally,
http_user_agent
is mapped to
network.http.user_agent
.
requestMethod
network.http.method
If
requestMethod
is not empty, it is mapped to
http_method
. Finally,
http_method
is mapped to
network.http.method
.
role
target_role.name
If
level
is not empty and
role
is empty, it is mapped to
role
. Finally,
role
is mapped to
target_role.name
.
RuleID
security_result.rule_id
If
RuleID
is not empty, it is mapped to
security_result.rule_id
.
serverStatus-code
network.http.response_code
If
http_response
is empty or
0
or
-
, and
http_proxy_status_code
is empty and
proxyStatus-code
is not empty, it is mapped to
network.http.response_code
.
severity
security_result.severity
If
severity
is
1
or
log_level
contains
info
or
message
contains
notice
,
security_result.severity
is set to
INFORMATIONAL
. If
severity
is
7
,
security_result.severity
is set to
HIGH
.
spt
principal.port
If
spt
is not empty, it is mapped to
src_port
. Finally,
src_port
is mapped to
principal.port
.
src
principal.ip
If
src_host
is not empty, it is mapped to
source_ip_temp
. If
source_ip_temp
is a valid IP address and
src
is empty, it is mapped to
src
. If
host
is not empty, it is mapped to
src
. Finally,
src
is mapped to
principal.ip
.
src_host
principal.hostname
If
src_host
is not empty, it is mapped to
source_ip_temp
. If
source_ip_temp
is not a valid IP address, it is mapped to
principal.hostname
. If
source_ip_temp
is a valid IP address and
src
is empty, it is mapped to
src
. Finally,
src
is mapped to
principal.ip
.
src_port
principal.port
If
src_port
is not empty, it is mapped to
principal.port
.
suser
principal.user.userid
If
loginID
is not empty, it is mapped to
user
. If
suser
is not empty, it is mapped to
user
. Finally, if
user
is not empty and not
-
, and does not contain
LDAP
, it is mapped to
principal.user.userid
.
url
target.url
If
url
is not empty, it is mapped to
target.url
.
user
principal.user.userid
If
loginID
is not empty, it is mapped to
user
. If
suser
is not empty, it is mapped to
user
. Otherwise, if
usrName
is not empty, it is mapped to
user
. Finally, if
user
is not empty and not
-
, and does not contain
LDAP
, it is mapped to
principal.user.userid
.
usrName
principal.user.userid
If
loginID
is not empty, it is mapped to
user
. If
suser
is not empty, it is mapped to
user
. Otherwise, if
usrName
is not empty, it is mapped to
user
. Finally, if
user
is not empty and not
-
, and does not contain
LDAP
, it is mapped to
principal.user.userid
.
when
metadata.event_timestamp
If
when
is not empty, it is parsed and mapped to
metadata.event_timestamp
.
N/A
metadata.log_type
The value
FORCEPOINT_WEBPROXY
is hardcoded into
metadata.log_type
.
N/A
metadata.product_name
The value
Forcepoint Webproxy
is hardcoded into
metadata.product_name
.
N/A
metadata.vendor_name
The value
Forcepoint
is hardcoded into
metadata.vendor_name
.
N/A
network.application_protocol
If
dst_port
is
80
,
network.application_protocol
is set to
HTTP
. If
dst_port
is
443
,
network.application_protocol
is set to
HTTPS
.
N/A
principal.user.group_identifiers
If
user
is not empty and not
-
and contains
LDAP
, the OU part of the user string is extracted and mapped to
principal.user.group_identifiers
.
N/A
principal.user.user_display_name
If
user
is not empty and not
-
and contains
LDAP
, the username part of the user string is extracted and mapped to
principal.user.user_display_name
.
N/A
security_result.action
If
action_msg
,
action
, or
act
are not empty,
sec_action
is set to
ALLOW
or
BLOCK
based on their values. Finally,
sec_action
is mapped to
security_result.action
.
N/A
security_result.detection_fields.key
The value
Disposition Number
is hardcoded into
security_result.detection_fields.key
when mapping
disposition
or
cn1
. The value
NatRuleId
is hardcoded into
security_result.detection_fields.key
when mapping
NatRuleId
. The value
Category Number
is hardcoded into
security_result.detection_fields.key
when mapping
category_no
.
Need more help?
Get answers from Community members and Google SecOps professionals.
