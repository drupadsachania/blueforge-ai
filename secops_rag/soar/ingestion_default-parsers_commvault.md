# Collect Commvault logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault/  
**Scraped:** 2026-03-05T09:53:28.723750Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Commvault logs
Supported in:
Google secops
SIEM
This document explains how to ingest Commvault logs to Google Security Operations
using Bindplane. The parser extracts data from
COMMVAULT
logs, categorizing
it as Alerts, Events, or AuditTrails. It then normalizes and structures the
extracted fields into a Unified Data Model (UDM) by using key-value parsing,
timestamp extraction, and field mapping.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Commvault Cloud
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
'COMMVAULT'
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
Configure Syslog in Commvault Cloud
Sign in to the
Commvault
Management Console.
Go to
Manage
>
System
.
Click the
SIEM
connector tile.
Click
Add connector
.
On the
General
tab, enter the following details:
Connector name
: Enter a name for the connector.
Connector type
: Select
Syslog
.
Streaming data
: Select the data that you want to export.
Click
Next
.
On the
Connector Definition
tab, click
Add syslog server
.
Provide the following configuration details:
Syslog server: Enter the Bindplane agent IP address.
Port number: Enter the Bindplane agent port number.
Click
Submit
.
UDM mapping table
Log Field
UDM Mapping
Logic
AgentType
event.idm.read_only_udm.observer.application
Value taken from
AgentType
field in the log message.
Alertid
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
Alertid
field in the log message. This field is mapped under the
alert_id
key.
Alertname
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
Alertname
field in the log message. This field is mapped under the
alert_name
key.
Alertseverity
event.idm.read_only_udm.security_result.severity
This field is used to populate the
security_result.severity
field based on its value.
Alerttime
event.idm.read_only_udm.metadata.event_timestamp
Value taken from
Alerttime
field in the log message and converted to a timestamp.
BackupLevel
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
BackupLevel
field in the log message. This field is mapped under the
backup_level
key.
BackupSet
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
BackupSet
field in the log message. This field is mapped under the
backup_set
key.
Client
event.idm.read_only_udm.principal.hostname
Value taken from
Client
field in the log message.
CommCell
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
CommCell
field in the log message. This field is mapped under the
comcell_field
key.
Computer
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
Computer
field in the log message. This field is mapped under the
computer_field
key.
Description
event.idm.read_only_udm.metadata.description
Value taken from
Description
field in the log message after some processing and cleanup.
DetectedCriteria
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
DetectedCriteria
field in the log message. This field is mapped under the
detected_criteria
key.
DetectedTime
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
DetectedTime
field in the log message. This field is mapped under the
detected_time
key.
Details
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
Details
field in the log message. This field is mapped under the
details_field
key.
Eventid
event.idm.read_only_udm.metadata.product_log_id
Value taken from
Eventid
field in the log message.
Eventseverity
event.idm.read_only_udm.security_result.severity
This field is used to populate the
security_result.severity
field based on its value.
Failure
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
Failure
field in the log message. This field is mapped under the
failure_filed
key.
Instance
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
Instance
field in the log message. This field is mapped under the
instance_field
key.
Jobid
event.idm.read_only_udm.principal.process.pid
Value taken from
Jobid
field in the log message.
MonitoringCriteria
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
MonitoringCriteria
field in the log message. This field is mapped under the
monitoring_criteria
key.
Occurencetime
event.idm.read_only_udm.metadata.event_timestamp
Value taken from
Occurencetime
field in the log message and converted to a timestamp.
Opid
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
Opid
field in the log message. This field is mapped under the
op_id
key.
Program
event.idm.read_only_udm.principal.application
Value taken from
Program
field in the log message.
Severitylevel
event.idm.read_only_udm.security_result.severity
Value taken from
Severitylevel
field in the log message and mapped based on a predefined mapping.
StoragePoliciesUsed
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
StoragePoliciesUsed
field in the log message. This field is mapped under the
storage_policies_used
key.
Subclient
event.idm.read_only_udm.additional.fields.value.string_value
Value taken from
Subclient
field in the log message. This field is mapped under the
subclient_field
key.
Type
event.idm.read_only_udm.security_result.detection_fields.value
Value taken from
Type
field in the log message. This field is mapped under the
alert_type
key.
Username
event.idm.read_only_udm.principal.user.userid
Value taken from
Username
field in the log message.
anomaly_type
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
detected_anomaly_type
key.
errors
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
errors_field
key.
file_name
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
detected_malicious_file
key.
media_agent
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
detected_media_agent
key.
no_of_files_created
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
no_of_files_created_field
key.
no_of_files_deleted
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
no_of_files_deleted_field
key.
no_of_files_modified
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
no_of_files_modified_field
key.
no_of_files_renamed
event.idm.read_only_udm.security_result.detection_fields.value
Value extracted from the
Description
field using grok patterns. This field is mapped under the
no_of_files_renamed_field
key.
URL
event.idm.read_only_udm.network.http.referral_url
Value extracted from the
Description
field using grok patterns.
event.idm.read_only_udm.metadata.event_type
This field is set to
STATUS_UPDATE
if the
Client
field is present, otherwise it's set to
GENERIC_EVENT
.
event.idm.read_only_udm.metadata.product_name
This field is set to
COMMVAULT
.
event.idm.read_only_udm.metadata.vendor_name
This field is set to
COMMVAULT
.
event.idm.read_only_udm.principal.user.user_role
This field is set to
ADMINISTRATOR
if the
User
field is
Administrator
.
Need more help?
Get answers from Community members and Google SecOps professionals.
