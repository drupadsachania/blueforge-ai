# Collect VMware Horizon logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-horizon/  
**Scraped:** 2026-03-05T09:30:00.247752Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware Horizon logs
Supported in:
Google secops
SIEM
This document explains how to ingest Omnissa Horizon (previously known as VMware Horizon) logs to Google Security Operations using Bindplane. The parser first uses regular expressions (grok patterns) to extract fields from raw syslog messages. Then, it maps the extracted fields to the corresponding fields in the Chronicle UDM schema, normalizing and structuring the data for analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the Omnissa Horizon 8
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
'VMWARE_HORIZON'
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
Configure Syslog for Omnissa Horizon (formerly VMware Horizon)
Sign in to the
Onmissa Horizon
web UI,
Go to
Settings
>
Event Configuration
.
In the
Send to syslog servers
section, click
Add
.
Enter the Bindplane agent IP address and port number (make sure you configure Bindplane protocol as
UDP
).
Click
Save
.
UDM Mapping Table
Log field
UDM mapping
Logic
ActionId
metadata.product_log_id
The value of 'ActionId' from the raw log is mapped to 'metadata.product_log_id'.
admin_domain
principal.administrative_domain
The value of 'admin_domain' from the raw log is mapped to 'principal.administrative_domain'.
BrokerName
principal.hostname
The value of 'BrokerName' from the raw log is mapped to 'principal.hostname'.
BrokerSessionId
network.session_id
The value of 'BrokerSessionId' from the raw log is mapped to 'network.session_id'.
ClientIpAddress
principal.ip
The value of 'ClientIpAddress' from the raw log is mapped to 'principal.ip'.
CurrentSessionLength
network.session_duration.seconds
The value of 'CurrentSessionLength' from the raw log is converted to integer and then mapped to 'network.session_duration.seconds'.
description
metadata.description
The value of 'description' from the raw log is mapped to 'metadata.description'.
DesktopDisplayName
principal.hostname
The value of 'DesktopDisplayName' from the raw log is mapped to 'principal.hostname'.
EventType
metadata.product_event_type
The value of 'EventType' from the raw log is mapped to 'metadata.product_event_type'.
ForwardedClientIpAddress
principal.nat_ip
The value of 'ForwardedClientIpAddress' from the raw log is mapped to 'principal.nat_ip'.
GlobalEntitlementName
target.user.group_identifiers
The value of 'GlobalEntitlementName' from the raw log is mapped to 'target.user.group_identifiers'.
host
principal.hostname
The value of 'host' from the raw log is mapped to 'principal.hostname'.
MachineDnsName
principal.url
The value of 'MachineDnsName' from the raw log is mapped to 'principal.url'.
MachineName
intermediary.hostname
The value of 'MachineName' from the raw log is mapped to 'intermediary.hostname'.
Module
additional.fields
The key "Module" with the value of 'Module' from the raw log is added to 'additional.fields' array.
pid
principal.process.pid
The value of 'pid' from the raw log is mapped to 'principal.process.pid'.
PoolId
additional.fields
The key "PoolId" with the value of 'PoolId' from the raw log is added to 'additional.fields' array.
program
principal.application
The value of 'program' from the raw log is mapped to 'principal.application'.
SessionType
additional.fields
The key "SessionType" with the value of 'SessionType' from the raw log is added to 'additional.fields' array.
Severity
security_result.severity
The value of 'Severity' from the raw log is uppercased, mapped to generic Chronicle severities and then mapped to 'security_result.severity'.
timestamp
metadata.event_timestamp
The value of 'timestamp' from the raw log is converted to Chronicle format and then mapped to 'metadata.event_timestamp'.
UserDisplayName
target.user.user_display_name
The value of 'UserDisplayName' from the raw log is mapped to 'target.user.user_display_name'.
UserName
target.user.userid
The value of 'UserName' from the raw log is mapped to 'target.user.userid'.
UserSID
target.user.windows_sid
The value of 'UserSID' from the raw log is mapped to 'target.user.windows_sid'.
ViewApiMethodName
additional.fields
The key "ViewApiMethodName" with the value of 'ViewApiMethodName' from the raw log is added to 'additional.fields' array.
ViewApiServiceName
additional.fields
The key "ViewApiServiceName" with the value of 'ViewApiServiceName' from the raw log is added to 'additional.fields' array.
extensions.auth.type
The value is set to "SSO" if the 'EventType' field is one of "ADMIN_USERLOGGEDOUT", "AGENT_CONNECTED", "AGENT_DISCONNECTED", "AGENT_ENDED", "AGENT_PENDING", "AGENT_PENDING_EXPIRED", "AGENT_RECONNECTED", "BROKER_DESKTOP_REQUEST", "BROKER_LMV_REMOTE_POD_DESKTOP_LAUNCH", "BROKER_MACHINE_ALLOCATED", "BROKER_USER_AUTHFAILED_BAD_USER_PASSWORD", "BROKER_USER_LOCK_SSO", "BROKER_USERLOGGEDIN", "BROKER_USERLOGGEDOUT", "VLSI_USERLOGGEDIN", "VLSI_INSUFFICIENT_PERMISSION", "VLSI_USERLOGGEDIN_REST", "TIMING_PROFILER_TUNNEL_CONNECTION", "TIMING_PROFILER_GET_LAUNCH_ITEMS", "TIMING_PROFILER_USER_AUTHENTICATION".
metadata.event_type
The value is determined by the 'EventType' field. If 'EventType' is one of "ADMIN_USERLOGGEDOUT", "AGENT_DISCONNECTED", "AGENT_ENDED", "AGENT_PENDING_EXPIRED", "BROKER_USER_LOCK_SSO", "BROKER_USERLOGGEDOUT" then 'metadata.event_type' is "USER_LOGOUT". If 'EventType' is one of "AGENT_CONNECTED", "AGENT_PENDING", "AGENT_RECONNECTED", "BROKER_USERLOGGEDIN", "VLSI_USERLOGGEDIN", "VLSI_INSUFFICIENT_PERMISSION", "VLSI_USERLOGGEDIN_REST" then 'metadata.event_type' is "USER_LOGIN". If 'EventType' is "TIMING_PROFILER_GET_LAUNCH_ITEMS" then 'metadata.event_type' is "STATUS_UNCATEGORIZED". If 'EventType' is "AGENT_SHUTDOWN" then 'metadata.event_type' is "STATUS_SHUTDOWN". If 'EventType' is one of "AGENT_STARTUP", "BROKER_LMV_REMOTE_POD_DESKTOP_LAUNCH" then 'metadata.event_type' is "STATUS_STARTUP". Otherwise, 'metadata.event_type' is "GENERIC_EVENT".
metadata.log_type
The value is set to "VMWARE_HORIZON".
metadata.product_name
The value is set to "HORIZON".
metadata.vendor_name
The value is set to "VMWARE".
Need more help?
Get answers from Community members and Google SecOps professionals.
