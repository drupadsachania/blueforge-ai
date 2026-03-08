# Collect Absolute Secure Endpoint logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/absolute-se/  
**Scraped:** 2026-03-05T09:18:28.348300Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Absolute Secure Endpoint logs
Supported in:
Google secops
SIEM
This document explains how to ingest Absolute Secure Endpoint (formerly Absolute Data & Device Security) logs to Google Security Operations using Bindplane. The parser extracts fields from the SIEM connector logs in either SYSLOG + KV (CEF) format. It uses grok patterns to identify and extract fields, then uses conditional logic based on the presence of
kv_pair
or
cef
data to map the extracted fields to the UDM schema. Specific mappings and transformations are applied depending on the identified fields and their values, handling both status heartbeat and security event data.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with systemd to run the Bindplane agent
A Windows Server (2012 or later) to host the Absolute SIEM Connector service
Microsoft .NET Framework 4.0 or higher installed on the Windows Server hosting the SIEM Connector
Privileged access to the Absolute Secure Endpoint console with SIEM integration enabled
If running behind a proxy, ensure firewall ports are open per the BindPlane agent requirements
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
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'ABSOLUTE'
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
Install the Absolute SIEM Connector on Windows Server
The Absolute SIEM Connector is a Windows service that retrieves alert event data from the Absolute Monitoring Center and forwards it using syslog in CEF format. The SIEM Connector is delivered as an MSI installer and is available as a free download to Absolute Data & Device Security (DDS) Professional and Premium customers through the Absolute Customer Center.
Sign in to the
Absolute Secure Endpoint Console
at
https://cc.absolute.com/
.
Go to the
Customer Center
or
Downloads
section.
Download the
Absolute SIEM Connector
MSI installer.
Transfer the installer to your Windows Server.
Run the installer on your Windows Server as an administrator.
Follow the installation wizard to complete the installation.
Note the installation directory (typically
C:\Program Files\Absolute Software\Absolute SIEM Connector
).
Enable SIEM integration in the Absolute Secure Endpoint Console
Before the SIEM Connector can retrieve events, you must enable SIEM integration in the Absolute Secure Endpoint Console.
Sign in to the
Absolute Secure Endpoint Console
at
https://cc.absolute.com/
.
Go to the
Settings
or
Administration
section.
Locate the
SIEM Integration
settings.
Click
Enable SIEM Integration
or toggle the SIEM integration setting to
On
.
Select the
event types
you want to forward to your SIEM:
Or select
All event types
to forward all available logs.
Click
Save
or
Apply
the configuration.
Configure the Absolute SIEM Connector
After installing the SIEM Connector and enabling SIEM integration in the console, configure the connector to send events to the BindPlane Agent.
On the Windows Server where the Absolute SIEM Connector is installed, open the
Absolute SIEM Connector Configuration Tool
.
You can find this in the
Start Menu
under
Absolute Software
or in the installation directory.
Provide the following configuration details:
Syslog Server Host
: Enter the IP address or hostname of the Bindplane agent.
Syslog Server Port
: Enter
514
(or the port configured in Bindplane).
Protocol
: Select
UDP
or
TCP
depending on the actual Bindplane configuration.
Format
: Confirm
CEF
(Common Event Format) is selected.
Update Interval
: Set how often the connector retrieves events from Absolute (minimum 2 minutes, maximum 1440 minutes/24 hours; default is 60 minutes).
Timezone
: Events are transmitted in
UTC
timezone for universal consistency across systems.
Click
Save
.
Start or restart the
Absolute SIEM Connector
service:
Open
Services
(services.msc).
Locate
Absolute SIEM Connector
service.
Click
Start
or
Restart
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
actorID
principal.user.product_object_id
The value of
actorID
from the raw log is mapped to this UDM field.
actorName
principal.hostname
If
actorType
is "Device", the value of
actorName
is mapped to this UDM field.
actorName
principal.user.userid
If
actorType
is "User", the value of
actorName
is mapped to this UDM field.
actorType
principal.user.attribute.roles.name
The value of
actorType
is mapped to this UDM field.
Alert ID
security_result.threat_id
The value of
Alert ID
from the raw log is mapped to this UDM field.
Alert Name
security_result.threat_name
The value of
Alert Name
from the raw log is mapped to this UDM field.
Alert Time
metadata.event_timestamp
The value of
Alert Time
from the raw log is parsed and mapped to this UDM field. Used as a fallback if the
date
field is not present or invalid.
cef
metadata.product_event_type
The
eventType
field extracted from the CEF string is mapped to this UDM field.
cef
principal.hostname
The
objectName
field extracted from the CEF string is mapped to this UDM field.
cef
principal.resource.product_object_id
The
objectID
field extracted from the CEF string is mapped to this UDM field.
cef
principal.user.product_object_id
The
actorID
field extracted from the CEF string is mapped to this UDM field.
cef
principal.user.userid
The
actorName
field extracted from the CEF string is mapped to this UDM field if
actorType
is "User".
cef
security_result.summary
The
verb
field extracted from the CEF string is mapped to this UDM field.
cef
target.labels.key
The parser sets the value to "objectProperties".
cef
target.labels.value
The
objectProperties
field extracted from the CEF string is mapped to this UDM field.
Computer Name
principal.hostname
The value of
Computer Name
from the raw log is mapped to this UDM field.
Condition
security_result.description
The value of
Condition
from the raw log is mapped to this UDM field.
date
metadata.event_timestamp
The value of
date
from the raw log is parsed and mapped to this UDM field.
datetime
timestamp.seconds
The epoch seconds extracted from the
datetime
field are used to populate the
timestamp.seconds
field.
dvc_ip
intermediary.ip
The value of
dvc_ip
from the raw log is mapped to this UDM field.
device_product
metadata.product_name
The value is set to "ABSOLUTE_PLATFORM".
device_vendor
metadata.vendor_name
The value is set to "ABSOLUTE".
device_version
metadata.product_version
The value of
device_version
from the raw log is mapped to this UDM field.
ESN
security_result.detection_fields.key
The parser sets the value to "ESN".
ESN
security_result.detection_fields.value
The value of
ESN
extracted from the
kv_pair
field is mapped to this UDM field.
event_class
metadata.product_event_type
The value of
event_class
from the raw log is mapped to this UDM field if
eventType
is not present.
eventType
metadata.product_event_type
The value of
eventType
from the raw log is mapped to this UDM field.
hostname
intermediary.hostname
The value of
hostname
from the raw log is mapped to this UDM field.
is_alert
is_alert
The value is set to "true" and converted to boolean.
is_significant
is_significant
The value is set to "true" and converted to boolean.
kv_pair
metadata.event_type
If
kv_pair
is present, the
metadata.event_type
is set to "STATUS_HEARTBEAT".
kv_pair
principal.asset.asset_id
The value of
Serial Number
extracted from the
kv_pair
field is used to construct the asset ID in the format "serialNumber:
".
log_type
metadata.log_type
The value is set to "ABSOLUTE".
objectID
principal.resource.product_object_id
The value of
objectID
from the raw log is mapped to this UDM field.
objectName
principal.hostname
The value of
objectName
from the raw log is mapped to this UDM field.
objectProperties
target.labels.key
The parser sets the value to "objectProperties".
objectProperties
target.labels.value
The value of
objectProperties
from the raw log is mapped to this UDM field.
objectType
principal.resource.resource_type
If
objectType
is "Device", it is converted to uppercase ("DEVICE") and mapped to this UDM field.
pid
about.process.pid
The value of
pid
from the raw log is mapped to this UDM field.
Serial Number
principal.asset.asset_id
The value of
Serial Number
from the raw log is used to construct the asset ID in the format "serialNumber:
".
verb
security_result.summary
The value of
verb
from the raw log is mapped to this UDM field.
Need more help?
Get answers from Community members and Google SecOps professionals.
