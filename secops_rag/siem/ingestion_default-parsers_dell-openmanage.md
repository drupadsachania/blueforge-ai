# Collect Dell OpenManage logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-openmanage/  
**Scraped:** 2026-03-05T09:23:18.556461Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Dell OpenManage logs
Supported in:
Google secops
SIEM
This document explains how to ingest Dell OpenManage logs to
Google Security Operations using Bindplane. The Logstash parser code first extracts
key-value pairs from raw DELL_OPENMANAGE logs using grok patterns and string
manipulation. Then, it maps the extracted fields to the corresponding Unified
Data Model (UDM) fields, enriching the data with security context and
standardizing its format for further analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Dell OpenManage
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
'DELL_OPENMANAGE'
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
Configure Syslog for ESET PROTECT on-premises
Sign in to the
ESET Protect
Web Console.
Go to
Alerts
>
Alert Policies
>
Create
.
Provide the following configuration details:
Create Alert Policy
dialog, enter a meaningful
Name
and
Description
for the policy.
Verify the
Enable Policy
checkbox is selected.
Click
Next
.
Category
: Expand
Application
and select all the categories and subcategories of the appliance logs.
Click
Next
.
Target
: The
Select Devices
option is selected by default. Don't select any target devices as the logs are forwarded to Bindplane.
Click
Next
.
Severity
: Select the
All
checkbox.
Click
Next
.
Actions
: Select
Syslog
.
Click
Enable
and enter the Bindplane agent IP address.
Click
Next
.
Click
Finish
.
Supported Dell OpenManage sample logs
SYSLOG + KV
<
156>2022
-
02
-
06
T05
:
00
:
33.181319
+
00
:
00
int
ernal
-
log
-
relay
-
01
EEMI
Audit
event
from
device
with
{
IP
}
192.168.100.100
{
HostName
}
workstation
-
prod
-
01
{
Severity
}
Warning
{
MessageID
}
CDEV9000
{
Message
}
This
device
and
several
others
has
become
non
compliant
after
run
ning
compliance
task
:
Alpha
.
{
Recommended
Action
}
Update
the
device
or
component
firmware
using
a
catalog
or
update
package
.
SYSLOG + KV + internal fields
<
158>2022
-
01
-
15
T15
:
59
:
55.576332
+
00
:
00
int
ernal
-
log
-
relay
-
01
EEMI
Configuration
event
from
device
with
{
IP
}
null
{
HostName
}
null
{
Severity
}
Info
{
MessageID
}
CSEC0053
{
Message
}
Description
:
Local
user
dummy_user
deleted
.
User
Name
:
admin_account
Received
from
address
:
172.16.254.1
{
Recommended
Action
}
Instrumentation
didn
'
t
provide
any
recommended
action
for
this
event
.
Protocol/diagnostic header
Client-ATV-Sharing-Version**: `1.2`
UDM mapping table
Log field
UDM mapping
Logic
data.HostName
read_only_udm.principal.hostname
The value of
HostName
from the raw log is directly mapped to
read_only_udm.principal.hostname
.
data.IP
read_only_udm.target.ip
The value of
IP
from the raw log is directly mapped to
read_only_udm.target.ip
.
data.Message
read_only_udm.metadata.description
The value of
Message
from the raw log is directly mapped to
read_only_udm.metadata.description
.
data.MessageID
read_only_udm.additional.fields.value.string_value
The value of
MessageID
from the raw log is directly mapped to
read_only_udm.additional.fields.value.string_value
.
data.Recommended Action
read_only_udm.additional.fields.value.string_value
The value of
Recommended Action
from the raw log is directly mapped to
read_only_udm.additional.fields.value.string_value
.
data.Severity
read_only_udm.security_result.severity
The value of
Severity
from the raw log is mapped to
read_only_udm.security_result.severity
after being converted to uppercase.
data.timestamp.nanos
read_only_udm.metadata.event_timestamp.nanos
The value of
timestamp.nanos
from the raw log is directly mapped to
read_only_udm.metadata.event_timestamp.nanos
.
data.timestamp.seconds
read_only_udm.metadata.event_timestamp.seconds
The value of
timestamp.seconds
from the raw log is directly mapped to
read_only_udm.metadata.event_timestamp.seconds
.
read_only_udm.metadata.event_type
This field is determined based on the content of the
Message
field from the raw log.
read_only_udm.metadata.log_type
This field is hardcoded to
DELL_OPENMANAGE
in the parser code.
read_only_udm.metadata.product_name
This field is hardcoded to
DELL_OPENMANAGE
in the parser code.
read_only_udm.metadata.vendor_name
This field is hardcoded to
DELL
in the parser code.
read_only_udm.additional.fields.key
This field name is hardcoded in the parser code. The value of this field  is
MessageID
or
Recommended_Action
.
Need more help?
Get answers from Community members and Google SecOps professionals.
