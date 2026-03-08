# Collect Forcepoint Email Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-emailsecurity/  
**Scraped:** 2026-03-05T09:24:35.048691Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Forcepoint Email Security logs
Supported in:
Google secops
SIEM
This document explains how to ingest Forcepoint Email Security logs to Google Security Operations using BindPlane. The parser first extracts fields from the JSON-formatted logs and initializes some UDM fields with empty values. Then, it maps the extracted fields to their corresponding fields within the Chronicle UDM structure based on specific conditions and data manipulations, ultimately creating a unified representation of the email security event.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the BindPlane agent requirements
Privileged access to the Forcepoint Email Security appliance or management console
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Download the
ingestion authentication file
.
Save the file securely on the system where BindPlane will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
customer ID
from the
Organization Details
section.
Install BindPlane Agent
Install the BindPlane agent on your Windows or Linux operating system according to the following instructions.
Windows Installation
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
Linux Installation
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
Additional Installation Resources
For additional installation options, consult this
installation guide
.
Alternative:
You can also use the
BindPlane OP managed installation workflow
for centralized agent management.
Configure BindPlane Agent to ingest Syslog and send to Google SecOps
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
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'FORCEPOINT_EMAILSECURITY'
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
<CUSTOMER_ID>
with the actual Customer ID.
Update
/path/to/ingestion-authentication-file.json
to the file path where the authentication file was saved in Step 1.
Restart BindPlane Agent to apply the changes
To restart the BindPlane agent in
Linux
, run the following command:
sudo
systemctl
restart
observiq-otel-collector
To restart the BindPlane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop observiq-otel-collector && net start observiq-otel-collector
Configure Syslog forwarding on Forcepoint Email Security
Sign in to the
Forcepoint Email Security Management Console
.
Go to
Settings
>
Integrations
>
SIEM Integration
.
Click
Enable SIEM Integration
.
Provide the following configuration details:
Format
: Select
LEEF
(Log Event Extended Format).
Syslog Server
: Enter the BindPlane Agent IP address.
Syslog Port
: Enter the BindPlane Agent port number (for example,
514
).
Protocol
: Select
UDP
or
TCP
, depending on your actual BindPlane Agent configuration.
Facility
: Select the syslog facility code (for example,
Local0
).
Severity
: Select the severity level for log events.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
Action
security_result.action_details
Directly mapped from the "Action" field in the raw log.
AttachmentFilename
additional.fields.value.list_value.values.string_value (key: Attachments_FileNames)
The "AttachmentFilename" field is split by comma and then each value is added as a string_value to the "additional.fields" array with the key "Attachments_FileNames".
AttachmentFileType
additional.fields.value.list_value.values.string_value (key: AttachmentsFileType)
The "AttachmentFileType" field is split by comma and then each value is added as a string_value to the "additional.fields" array with the key "AttachmentsFileType".
AttachmentSize
additional.fields.value.list_value.values.string_value (key: AttachmentsSize)
The "AttachmentSize" field is split by comma and then each value is added as a string_value to the "additional.fields" array with the key "AttachmentsSize".
DateTime
Not mapped in the provided UDM.
EnvelopeSender
network.email.from
Directly mapped from the "EnvelopeSender" field in the raw log.
EventReceivedTime
metadata.event_timestamp
Parsed to a timestamp format and mapped to "metadata.event_timestamp".
FilteringReason
security_result.category_details
Directly mapped from the "FilteringReason" field in the raw log.
MessageSandboxing
security_result.detection_fields.value (key: MessageSandboxing)
Directly mapped from the "MessageSandboxing" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.
MessageSize
security_result.detection_fields.value (key: MessageSize)
Directly mapped from the "MessageSize" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.
nxlog_filename
additional.fields.value.string_value (key: nxlog_filename)
Directly mapped from the "nxlog_filename" field in the raw log and added as a key-value pair to the "additional.fields" array.
RecipientAddress
network.email.to
Directly mapped from the "RecipientAddress" field in the raw log.
SenderIP
principal.asset.ip, principal.ip
Directly mapped from the "SenderIP" field in the raw log.
SenderIPCountry
principal.location.country_or_region
Directly mapped from the "SenderIPCountry" field in the raw log.
SourceModuleName
principal.resource.attribute.labels.value (key: SourceModuleName)
Directly mapped from the "SourceModuleName" field in the raw log and added as a key-value pair to the "principal.resource.attribute.labels" array.
SourceModuleType
principal.resource.attribute.labels.value (key: SourceModuleType)
Directly mapped from the "SourceModuleType" field in the raw log and added as a key-value pair to the "principal.resource.attribute.labels" array.
SpamScore
security_result.detection_fields.value (key: SpamScore)
Directly mapped from the "SpamScore" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.
Subject
network.email.subject
Directly mapped from the "Subject" field in the raw log.
VirusName
security_result.detection_fields.value (key: VirusName)
Directly mapped from the "VirusName" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.
metadata.event_type
The value is determined based on the presence of other fields. If "has_network_email_data" is true, the value is set to "EMAIL_TRANSACTION". If "has_principal" is true, the value is set to "STATUS_UPDATE". Otherwise, it defaults to "GENERIC_EVENT".
metadata.product_name
The value is set to "FORCEPOINT EMAILSECURITY".
metadata.vendor_name
The value is set to "FORCEPOINT EMAILSECURITY".
Need more help?
Get answers from Community members and Google SecOps professionals.
