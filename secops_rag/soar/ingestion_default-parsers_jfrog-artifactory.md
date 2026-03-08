# Collect JFrog Artifactory logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory/  
**Scraped:** 2026-03-05T09:57:26.906568Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect JFrog Artifactory logs
Supported in:
Google secops
SIEM
This document explains how to ingest Jfrog Artifactory logs to Google Security Operations using Bindplane. The parser handles two different JFrog Artifactory log formats. It uses grok patterns to identify and extract fields from each format. It then maps those fields to the UDM, handling JSON payloads within one of the formats and dropping logs that don't match either format.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Jfrog Artifactory instance.
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
```
yaml
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
chronicle
/
chronicle_w_labels
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
malachiteingestion
-
pa
.
googleapis
.
com
# Add optional ingestion labels for better organization
ingestion_labels
:
log_type
:
'JFROG_ARTIFACTORY'
raw_log_field
:
body
service
:
pipelines
:
logs
/
source0__chronicle_w_labels
-
0
:
receivers
:
-
udplog
exporters
:
-
chronicle
/
chronicle_w_labels
```
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
Configure Jfrog Artifactory Syslog
Connect to the
Jfrog Artifactory
instance.
Edit the file
$JFROG_HOME/artifactory/var/etc/artifactory/logback.xml
using vi:
vi
$JFROG_HOME
/artifactory/var/etc/artifactory/logback.xml
Add the following syslog appender to the file:
<appender
name
=
"SYSLOG"
class
=
"ch.qos.logback.classic.net.SyslogAppender"
>
<syslogHost>Bindplane-Agent-IP</syslogHost>
<facility>SYSLOG</facility>
<suffixPattern>
[
%thread
]
%logger
%msg</suffixPattern>
</appender>
Replace
Bindplane-Agent-IP
in syslogHost, with the actual IP address configured for the Bindplane agent.
Add additional configuration data to the file:
<root>
<
level
value
=
"debug"
/>
<appender-ref
ref
=
"CONSOLE"
/>
<appender-ref
ref
=
"FILE"
/>
<appender-ref
ref
=
"SYSLOG"
/>
</root>
Save the file by clicking the
ESC
(escape) button on your keyboard and typing
:wq
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
read_only_udm.metadata.product_event_type
The value of
action
from the raw log is converted to lowercase and mapped.
datetime
read_only_udm.metadata.event_timestamp
The raw log's
datetime
field is parsed and converted to a timestamp.
hostname
read_only_udm.principal.hostname
Directly mapped from the raw log's
hostname
field.
id
read_only_udm.metadata.product_log_id
Directly mapped from the raw log's
id
field (from JSON payload).
ip
read_only_udm.principal.ip
Directly mapped from the raw log's
ip
field. Hardcoded to "USER_RESOURCE_ACCESS". Hardcoded to "JFROG_ARTIFACTORY". Hardcoded to "Artifactory". Hardcoded to "JFROG".
owner
read_only_udm.principal.user.userid
Mapped if
username
is not present in the raw log (from JSON payload).
repo_name
read_only_udm.target.resource.name
Directly mapped from the raw log's
repo_name
field.
repo_type
read_only_udm.target.resource.resource_subtype
Directly mapped from the raw log's
repo_type
field.
scope
read_only_udm.target.resource.name
Directly mapped from the raw log's
scope
field (from JSON payload).
scope
read_only_udm.target.resource.resource_subtype
Hardcoded to "scope" if
scope
is present in the raw log.
sequenceId
read_only_udm.metadata.product_log_id
Quotes are removed from the
sequenceId
field and then mapped.
subject
read_only_udm.about.labels.key
Hardcoded to "subject" if
subject
is present in the raw log.
subject
read_only_udm.about.labels.value
Directly mapped from the raw log's
subject
field (from JSON payload).
type
read_only_udm.metadata.product_event_type
Directly mapped from the raw log's
type
field (from JSON payload).
user
read_only_udm.principal.user.userid
Directly mapped from the raw log's
user
field.
username
read_only_udm.principal.user.userid
Directly mapped from the raw log's
username
field (from JSON payload).
Need more help?
Get answers from Community members and Google SecOps professionals.
