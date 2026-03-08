# Collect Broadcom Support Portal Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-support-portal/  
**Scraped:** 2026-03-05T09:51:37.293800Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Broadcom Support Portal Audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest Broadcom Support Portal Audit logs to Google Security Operations using Bindplane agent.
Broadcom Support Portal provides centralized access to support resources, case management, and product downloads for Broadcom enterprise products. The platform generates audit logs that capture user authentication events, job execution activities, resource access, and administrative operations across the portal infrastructure.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and the Broadcom Support Portal infrastructure
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Administrative access to the Broadcom Support Portal with permissions to configure syslog forwarding
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/broadcom
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'your-customer-id'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
BROADCOM_SUPPORT_PORTAL
raw_log_field
:
body
service
:
pipelines
:
logs/broadcom_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/broadcom
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on:
0.0.0.0:514
to listen on all interfaces on port 514 (requires root on Linux)
0.0.0.0:1514
to listen on an unprivileged port (recommended for Linux non-root)
Receiver type options:
udplog
for UDP syslog (default)
tcplog
for TCP syslog
Exporter configuration:
creds_file_path
: Full path to the Google SecOps ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Your
customer ID
. For details, see
Get Google SecOps customer ID
.
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for the complete list
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux:
Run the following command:
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
To restart the Bindplane agent in Windows:
Choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press Enter.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure Broadcom Support Portal syslog forwarding
Broadcom Support Portal can forward audit log events via syslog to external collectors for SIEM integration.
Configure remote syslog logging
Sign in to the
Broadcom Support Portal
administration console.
Go to
Administration
>
Logs
>
Remote Logging
.
Enable
Remote Syslog
.
Configure the following syslog parameters:
Syslog Server Address
: Enter the IP address or hostname of the Bindplane agent host (for example,
192.168.1.100
).
Port
: Enter the port matching the Bindplane agent
listen_address
(for example,
514
).
Protocol
: Select
UDP
(default) or
TCP
to match the Bindplane agent receiver type.
Click
Save
.
Select audit event categories
In the
Remote Logging
configuration, select the audit event categories to forward:
User authentication events
: Login and logout activities
Job events
: Job execution status and state changes
Resource access events
: Access to support resources and downloads
Administrative events
: Configuration changes and administrative operations
Click
Save
.
Verify syslog forwarding
After saving the syslog configuration, perform a test action in the Broadcom Support Portal (for example, sign in or access a resource).
Check the Bindplane agent logs for incoming syslog messages:
Linux
:
sudo journalctl -u observiq-otel-collector -f
Windows
:
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Verify that audit log messages appear in the logs.
UDM mapping table
Log Field
UDM Mapping
Logic
ParallelDestination, STORAGE_TYPE, JOB_NAME, kubernetes.docker_id, kubernetes.pod_id
target.resource.attribute.labels
Merged with corresponding labels
destinationName, responseDestinationName, DESTINATION_NAME
target.application
Value from DESTINATION_NAME if not empty, else responseDestinationName if not null or empty, else destinationName
kubernetes.container_hash
target.file.full_path
Extracted using grok pattern %{DATA:filepath}:%{GREEDYDATA:file_sha}
kubernetes.container_hash
target.file.sha256
Extracted using grok pattern %{DATA:filepath}:%{GREEDYDATA:file_sha}
groupId
target.user.group_identifiers
Merged from groupId
dispatch, companyId
additional.fields
Merged with dispatch_label and companyId_label
response, responseId
security_result.detection_fields
Merged with response_label and responseId_label
kubernetes.container_image, kubernetes.container_name, kubernetes.namespace_name, kubernetes.pod_name
principal.resource.attribute.labels
Merged with corresponding labels
GROUP_NAME
principal.group.group_display_name
Value copied directly
kubernetes.host
principal.asset.hostname
Value copied directly
kubernetes.host
principal.hostname
Value copied directly
payload
principal.resource.product_object_id
Value copied directly
severity
security_result.severity
Uppercased and set if in allowed list
description, JOB_STATE
security_result.description
Value from description if not empty, else JOB_STATE
timestramp
metadata.event_timestamp
Parsed using ISO8601, yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ, yyyy-MM-dd HH:mm:ss.SSS formats
metadata.event_type
Set to "USER_LOGIN" if has_principal, has_target, user_login; "USER_LOGOUT" if has_principal, has_target, user_logout; "STATUS_UPDATE" if has_principal; else "GENERIC_EVENT"
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if user login or logout event
metadata.product_name
Set to "BROADCOM_SUPPORT_PORTAL"
metadata.vendor_name
Set to "BROADCOM_SUPPORT_PORTAL"
Need more help?
Get answers from Community members and Google SecOps professionals.
