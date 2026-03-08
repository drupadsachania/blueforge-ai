# Collect Cisco APIC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-apic/  
**Scraped:** 2026-03-05T09:21:12.199206Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco APIC logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco APIC logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco APIC management console
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
YOUR_CUSTOMER_ID
endpoint
:
malachiteingestion-pa.googleapis.com
# Specify the log type that matches your Chronicle feed configuration
# Commonly used: CISCO_ACI or CISCO_APIC depending on your setup
log_type
:
'CISCO_APIC'
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
Ensure the
log_type
value matches the Log type selected in your Google SecOps feed configuration.
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
Configure Syslog forwarding on Cisco APIC
Configure Management Contracts
Sign in to the
Cisco APIC console
.
Go to
Tenants
>
mgmt
>
Security Policies
.
Check that the management contracts allow UDP on port 514:
For Out-of-Band management
: Ensure the OOB contract permits
UDP
port
514
.
For In-Band management
: Ensure the INB contract permits
UDP
port
514
.
If required, create or modify filters to allow
UDP
port
514
for the selected management EPG.
Create Syslog Monitoring Destination Group
Go to
Admin
>
External Data Collectors
>
Monitoring Destinations
>
Syslog
.
Click the
+
sign to
Create Syslog Monitoring Destination Group
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Syslog
).
Description
: Enter a description (for example,
Syslog destination for Google SecOps
).
Admin State
: Select
enabled
.
Format
: Select
aci
(recommended) or
nxos
.
Click
Next
.
In the
Create Syslog Remote Destination
section, provide the following configuration details:
Host Name/IP
: Enter the BindPlane Agent IP address.
Name
: Enter a descriptive name for the destination.
Admin State
: Select
enabled
.
Severity
: Select
information
(or your preferred severity level).
Port
: Enter
514
(or the port configured on BindPlane Agent).
Management EPG
: Select appropriate management EPG:
default (Out-of-Band)
for OOB management
inb-default
for In-Band management
Forwarding Facility
: Select
local7
(or your preferred facility).
Click
OK
.
Review the configuration and click
Finish
.
Configure Fabric Policy Syslog Source
Go to
Fabric
>
Fabric Policies
>
Monitoring Policies
.
Expand
default
and select
Callhome/SNMP/Syslog
.
Click the
+
sign to create a syslog source.
Provide the following configuration details:
Source Name
: Enter a name (for example,
fabric-syslog-source
).
Min Severity
: Select
information
.
Include
: Select
Check All
to include Audit logs, Events, Faults, and Session logs.
Destination Group
: Select the syslog monitoring destination group created earlier.
Click
Submit
.
Configure Common Policy Syslog Source
Go to
Fabric
>
Fabric Policies
>
Monitoring Policies
.
Expand
common
and select
Callhome/SNMP/Syslog
.
Click
+
to create a syslog source.
Provide the following configuration details:
Source Name
: Enter a name (for example,
common-syslog-source
).
Min Severity
: Select
information
.
Include
: Select
Check All
to include Audit logs, Events, Faults, and Session logs.
Destination Group
: Select the syslog monitoring destination group created earlier.
Click
Submit
.
Configure Access Policy Syslog Source
Go to
Fabric
>
Access Policies
>
Monitoring Policies
.
Expand
default
and select
Callhome/SNMP/Syslog
.
Click the
+
sign to create a syslog source.
Provide the following configuration details:
Source Name
: Enter a name (for example,
access-syslog-source
).
Min Severity
: Select
information
.
Include
: Select
Check All
to include Audit logs, Events, Faults, and Session logs.
Destination Group
: Select the syslog monitoring destination group created earlier.
Click
Submit
.
Configure System Message Policy (Optional)
Go to
Fabric
>
Fabric Policies
>
Monitoring Policies
.
Expand
common
>
System Message Policies
.
Select
Policy for System Syslog Messages
.
Select the
default
facility.
Change
Severity
to
information
.
Click
Update
.
Need more help?
Get answers from Community members and Google SecOps professionals.
