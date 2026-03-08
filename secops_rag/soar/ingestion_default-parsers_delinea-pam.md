# Collect Delinea PAM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-pam/  
**Scraped:** 2026-03-05T09:54:18.320818Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Delinea PAM logs
Supported in:
Google secops
SIEM
This document explains how to ingest Delinea Privileged Access Manager (PAM)
logs to Google Security Operations using Bindplane. The Logstash parser code
extracts security event data from DELINEA_PAM logs in either SYSLOG or CSV format.
It then uses Grok patterns and CSV parsing to structure the data, maps the
extracted fields to the Unified Data Model (UDM), and finally outputs the
transformed event data.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Delinea Privileged Access Manager
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
'DELINEA_PAM'
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
Configure Syslog in Delinea Privilege Manager
Sign in to the
Delinea PAM
web UI.
Go to
Admin
>
Configuration
>
Foreign Systems
.
Click
Create
on
Syslog Page
.
Provide the following configuration details:
Name
: Enter a descriptive name for the Server.
Protocol
: Select
UDP
(you can also select
TCP
, depending on your Bindplane agent configuration).
Host
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number. (
514
for UDP).
Click
Save Changes
.
Configure SysLog Server Tasks in Delinea Privilege Manager
Go to
Admin
>
Tasks
>
expand Server Tasks folder
>
expand Foreign Systems folder
.
Select
Syslog
.
Click
Create
.
Template options:
Send SysLog Application Action Events
: Use this template to send application action events to your SysLog system. Application Action Events contain generic information about the application that run, which policy was triggered, the date and timestamp, computer, and user for example.
Send SysLog Application Justification Events
: Use this template to send application justification events to your SysLog system. For example, if a user runs an application requiring a justification workflow.
Send SysLog Bad Rated Application Action Events
: Use this template to send an event to your SysLog system, when an application is being installed or executed, that is identified with a bad security rating.
Send SysLog Change History Events
: Use this template to send change history events to your SysLog system. When this task runs for the first time, it sends all change history to your SysLog server. On subsequent runs it only sends the delta of new change history events.
Send SysLog Events
: Use this template to send all SysLog events to your SysLog system. These events are based on the different options you selected on the SysLog server during setup.
Send SysLog Newly Discovered File Events
: Use this template to send newly discovered file events to your SysLog system. For this to produce any events the Default File Inventory Policy needs to be enabled and resource discovery schedules need to be customized.
Send SysLog Password Disclosure Events
: Use this template to send all password disclosure events to your SysLog system.
Provide the following configuration details:
Template
: Select a syslog template (for example,
Send Syslog Events
to send all the events).
Name
: Enter a meaningful name for the task (for example, you can enter the same name as the selected template).
Event Name
: Enter a name for the events.
Event Severity
: Enter a severity level threshold for the events to be sent.
Syslog System
: Select the Syslog server foreign system Bindplane agent server you created in the previous step.
Click
Create
.
Supported Delinea PAM sample logs
SYSLOG + CSV
2023-10-24T22:25:00.219Z DELINEA-PAM-HOST-01 CEF:0|Delinea Software|Secret Server|11.5.000002|500|System Log|7|msg=Delinea.PAM.Business.Autofac.Modules.MessageQueue.PublishToExternalMessageQueueModule`2+NoOpExternalBusUnavailableException[Delinea.PAM.Business.DistributedEngine.ISessionRecordingAgentResponseBusConnectionInformationProvider,Delinea.PAM.Business.Autofac.Modules.MessageQueue.SessionRecordingWorkerPublishMessageQueueModule+BusInjectionTarget]: Bus is not available because of a startup issue.   at Delinea.PAM.Business.Autofac.Modules.MessageQueue.PublishToExternalMessageQueueModule`2.NoOpExternalCommonBus.BasicPublish(String exchangeName, IBasicConsumable request, Boolean persistent, IDictionary`2 customProperties, Action`1 prePublishCallback)   at Delinea.PAM.Business.Logic.MessageQueue.Buses.RoleRequestBus.BasicPublish(IBasicConsumable request, Boolean persistent, IDictionary`2 customProperties)   at Delinea.PAM.BackgroundScheduler.Logic.Areas.SessionRecording....
UDM mapping table
Log Field
UDM Mapping
Logic
CEF:0|...|column1
metadata.vendor_name
Extracted from the CEF string, specifically the value after the first "
CEF:0|...|column2
metadata.product_name
Extracted from the CEF string, specifically the value after the second "
CEF:0|...|column3
metadata.product_version
Extracted from the CEF string, specifically the value after the third "
CEF:0|...|column5
metadata.product_event_type
Extracted from the CEF string, specifically the value after the fifth "
CEF:0|...|column7
security_result.description
Extracted from the CEF string, specifically the value after the seventh "
%{HOSTNAME}
principal.hostname
Extracted from the log message using the grok pattern "%{HOSTNAME}".
%{TIMESTAMP_ISO8601}
metadata.event_timestamp
Extracted from the log message using the grok pattern "%{TIMESTAMP_ISO8601}".
metadata.event_type
Hardcoded to "STATUS_UPDATE" in the parser code.
metadata.log_type
Hardcoded to "DELINEA_PAM" in the parser code.
timestamp
timestamp
The event timestamp is parsed from the "timestamp" field in the raw log, converting it to a UDM timestamp format.
Need more help?
Get answers from Community members and Google SecOps professionals.
