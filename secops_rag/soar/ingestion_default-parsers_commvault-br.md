# Collect CommVault Backup and Recovery logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault-br/  
**Scraped:** 2026-03-05T09:53:29.987865Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CommVault Backup and Recovery logs
Supported in:
Google secops
SIEM
This document explains how to ingest CommVault Backup and Recovery logs to Google Security Operations using Bindplane. The parser extracts data from three different log types (Alerts, Events, AuditTrail) within Commvault logs. Then, it maps the extracted fields to the Google SecOps UDM schema, handling various data cleaning and transformation tasks along the way to ensure consistent representation.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Commvault CommCell.
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
COMMVAULT_COMMCELL
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
Configure the Commvault Syslog Server
Sign in to the
Commvault CommCell
web UI.
Select
Manage
>
System
.
Click
Syslog server
.
Specify the following details of the syslog server:
Hostname
: enter the IP address of the Bindplane agent.
Port
: enter the Bindplane port; for example,
514
.
Click
Enable
toggle to activate the syslog server setting.
In the
Forward to syslog
field, select
Alerts
,
Audit trails
and
Events
.
Click
Submit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
AgentType
observer.application
Directly mapped from the
AgentType
field in the event log.
Alertid
security_result.detection_fields.Alertid.value
Directly mapped from the
Alertid
field in the alert log.
Alertname
security_result.detection_fields.Alertname.value
Directly mapped from the
Alertname
field in the alert log.
Alertseverity
security_result.severity
Mapped from the
Alertseverity
field in the alert log. Translated to UDM severity levels (INFORMATIONAL, HIGH, LOW, CRITICAL).
Alerttime
metadata.event_timestamp
Parsed from the
Alerttime
field in the alert log and converted to a timestamp.
Audittime
metadata.event_timestamp
Parsed from the
Audittime
field in the audit log and converted to a timestamp.
Client
principal.hostname, principal.asset.hostname
Directly mapped from the
Client
field in the event, alert, or audit log.
CommCell
This UDM field does not come from the raw log. It is set to
backupcv
if extracted from alert description.
Computer
This UDM field does not come from the raw log. It is set to
backupcv
if extracted from event log.
Description
security_result.description
Mapped from either the
Description
field in the event log or the parsed
event_description
field from the
Alertdescription
field in the alert log. If the
Description
field contains
A suspicious file
, it is overwritten with
A suspicious file is Detected
.
Details
Used to extract the
Client
field using grok.
duration
This UDM field does not come from the raw log. It is set to the duration extracted from event description.
Eventid
metadata.product_log_id
Directly mapped from the
Eventid
field in the event log.
Eventseverity
security_result.severity
Mapped from the
Eventseverity
field in the event log. Translated to UDM severity levels (INFORMATIONAL, HIGH, LOW, CRITICAL).
file_name
security_result.detection_fields.SuspiciousFileName.value
Extracted from the
Alertdescription
field in the alert log using grok.
Jobid
principal.process.pid
Directly mapped from the
Jobid
field in the event or alert log.
media_agent
security_result.detection_fields.MediaAgent.value
Extracted from the
Alertdescription
field in the alert log using grok.
no_of_files_created
security_result.detection_fields.no_of_files_created.value
Extracted from the
Alertdescription
field in the alert log using grok.
no_of_files_deleted
security_result.detection_fields.no_of_files_deleted.value
Extracted from the
Alertdescription
field in the alert log using grok.
no_of_files_modified
security_result.detection_fields.no_of_files_modified.value
Extracted from the
Alertdescription
field in the alert log using grok.
no_of_files_renamed
security_result.detection_fields.no_of_files_renamed.value
Extracted from the
Alertdescription
field in the alert log using grok.
Occurrencetime
metadata.event_timestamp
Parsed from the
Occurrencetime
field in the event log and converted to a timestamp.
Operation
security_result.detection_fields.Operation.value
Directly mapped from the
Operation
field in the audit log.
Opid
security_result.detection_fields.Opid.value
Directly mapped from the
Opid
field in the audit log.
Program
principal.application
Directly mapped from the
Program
field in the event log.
Severitylevel
security_result.severity
Mapped from the
Severitylevel
field in the audit log. Translated to UDM severity levels (INFORMATIONAL, HIGH, LOW, CRITICAL).
Type
security_result.detection_fields.Type.value
Directly mapped from the
Type
field extracted from the
Alertdescription
field in the alert log.
url
network.http.referral_url
Directly mapped from the
url
field extracted from the
Alertdescription
field in the alert log.
Username
principal.user.userid
Directly mapped from the
Username
field in the audit log. If the username is
Administrator
, the
principal.user.user_role
field is set to
ADMINISTRATOR
instead.
-
metadata.vendor_name
This UDM field does not come from the raw log. It is set to
COMMVAULT
.
-
metadata.product_name
This UDM field does not come from the raw log. It is set to
COMMVAULT_COMMCELL
.
-
metadata.log_type
This UDM field does not come from the raw log. It is set to
COMMVAULT_COMMCELL
.
-
metadata.event_type
This UDM field does not come from the raw log. It is set to
STATUS_UPDATE
if the
Client
field is present, otherwise set to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
