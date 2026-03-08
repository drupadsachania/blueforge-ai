# Collect Deep Instinct EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/deep-instinct-edr/  
**Scraped:** 2026-03-05T09:23:05.642733Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Deep Instinct EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest Deep Instinct EDR logs to Google Security Operations using Bindplane. The parser extracts fields from Deep Instinct EDR LEEF formatted logs. It uses grok to parse the log message, kv to separate key-value pairs, and then maps these values to the UDM, handling various data transformations and conditional logic for specific fields along the way. It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the Deep Instinct Management Console
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
yaml
receivers:
  udplog:
    # Replace the port and IP address as required
    listen_address: "0.0.0.0:514"

exporters:
  chronicle/chronicle_w_labels:
    compression: gzip
    # Adjust the path to the credentials file you downloaded in Step 1
    creds_file_path: '/path/to/ingestion-authentication-file.json'
    # Replace with your actual customer ID from Step 2
    customer_id: <customer_id>
    endpoint: malachiteingestion-pa.googleapis.com
    # Add optional ingestion labels for better organization
    log_type: 'DEEP_INSTINCT_EDR'
    raw_log_field: body
    ingestion_labels:

service:
  pipelines:
    logs/source0__chronicle_w_labels-0:
      receivers:
        - udplog
      exporters:
        - chronicle/chronicle_w_labels
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
Configure Syslog for Deep Instinct EDR
Sign in to the
Deep Instinct Management Console
.
Go to
Settings
>
Integrations
.
Click the
+ Add
button.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Bindplane
).
Host
: Enter the Bindplane Agent IP address.
Port
: Enter the Bindplane Agent port number.
Protocol
: Select
UDP
or
TCP
, depending on your actual Bindplane Agent configuration.
Format
: Select
LEEF
.
Timezone
: Select the UTC timezone for consistency across systems.
Go to the
Events
section and select
all
.
Click the
Save
.
Supported Deep Instinct EDR sample logs
LEEF
<81>1 2022-10-21T08:30:08.645Z 192.0.2.1 log-sender-01 - 2940383 - LEEF:2.0|Deep Instinct|D-Appliance|3.4.2.918|SecurityEvent_Detected|eventExternalId=2940383  act=Detected    sev=9   host=10.0.0.10  identHostName=WORKSTATION-A1    identSrc=10.0.0.11  srcMAC=00:00:00:00:00:00    dclientVersion=3.4.2.29 LoggedInUsers=DOMAIN\\analyst_user  usrName=NT AUTHORITY\\SYSTEM    identExternalId=386 deviceGroup=GROUP-A - Tier 1 Assets policy=Default-Endpoint-Policy  tdevTime=2022-10-21T08:30:08.645Z   eventType=Script Control - Path externalSeverity=1  MITRE ATT&CK=(TA0002.T1059.003|Execution|Command and Scripting Interpreter|Windows Command Shell|TA0002.T1059.001|Execution|Command and Scripting Interpreter|PowerShell)   processChain=<wininit.exe|980> <services.exe|104> <TaniumClient.exe|4956> <TaniumClient.exe|7184> <TaniumCX.exe|35516> <TaniumCX.exe|33508> <java.exe|23620> <cmd.exe|35176> <powershell.exe|27784> filePath=C:\\Windows\\System32\\generic_interpreter.exe -exec -file /temp/script.ps1    fileType=POWERSHELL_INTERACTIVE OSName=Windows  sOSName=Windows OSVersion=Windows 10 Pro    engineVersion=128w
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action_details
Directly mapped from the
act
field.
app
principal.application
Directly mapped from the
app
field.
devTime
metadata.event_timestamp
Directly mapped from the
devTime
field.
deviceGroup
principal.group.group_display_name
Directly mapped from the
deviceGroup
field.
eventExternalId
metadata.product_log_id
Directly mapped from the
eventExternalId
field.
eventType
metadata.product_event_type
Directly mapped from the
eventType
field.
filePath
principal.process.file.full_path
Directly mapped from the
filePath
field.
fileType
principal.process.file.file_type
Mapped from the
fileType
field. If
fileType
is "POWERSHELL_INTERACTIVE", the UDM value is set to "FILE_TYPE_POWERSHELL".
host
principal.hostname
Directly mapped from the
host
field.
identHostName
target.hostname
Directly mapped from the
identHostName
field.
identSrc
target.ip
Directly mapped from the
identSrc
field.
LoggedInUsers
principal.user.userid
Mapped from the
LoggedInUsers
field after removing "REGISGROUP" and any backslashes.
log_type
metadata.log_type
Directly mapped from the
log_type
field.
OSName
principal.asset.platform_software.platform
Mapped from the
OSName
field, converted to uppercase.
OSVersion
principal.asset.platform_software.platform_version
Directly mapped from the
OSVersion
field.
sev
security_result.severity_details
Directly mapped from the
sev
field.  Hardcoded to "STATUS_UPDATE" in the parser. Hardcoded to "Deep Instinct EDR" in the parser. Directly mapped from the
vendor_name
field extracted by grok. Directly mapped from the
srcMAC
field. Directly mapped from the
usrName
field. Hardcoded to "MEDIUM" in the parser.
srcMAC
principal.mac
Directly mapped from the
srcMAC
field.
usrName
principal.user.user_display_name
Directly mapped from the
usrName
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
