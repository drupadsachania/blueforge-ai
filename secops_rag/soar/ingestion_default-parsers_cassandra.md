# Collect Apache Cassandra logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cassandra/  
**Scraped:** 2026-03-05T09:49:47.085483Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Apache Cassandra logs
Supported in:
Google secops
SIEM
This document explains how to ingest Apache Cassandra logs to Google Security Operations
using Bindplane. The parser extracts fields, converting them into the Unified
Data Model (UDM). It uses grok patterns to parse the initial message, then uses
a JSON filter for nested data and performs conditional transformations to map
various fields to their UDM equivalents, handling different log levels and
enriching the output with metadata.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or Linux host with systemd
If running behind a proxy, firewall
ports
are open
Privileged access to an Apache Cassandra instance
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
`
https
:
//
github
.
com
/
observIQ
/
bindplane
-
agent
/
releases
/
latest
/
download
/
observiq
-
otel
-
collector
.
msi
`
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
`
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
`
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
`
0.0.0.0:514`
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
'CASSANDRA'
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
Configure Syslog export in Apache Cassandra
Sign in to the
Apache Cassandra
host using SSH.
Open the configuration file
logback.xml
and insert the following code on Line 28:
For most versions of Apache Cassandra, the location would be
$(CASSANDRA_HOME)/conf
.
Package installations of Datastax Enterprise, the location would be
/etc/dse
.
Tar file installations of DSE, the location would be
$(TARBALL_ROOT)/resources/cassandra/conf
.
Add the following
Appender
definition to the
logback.xml
file on Line 28:
<appender
name="SYSLOG"
class="ch.qos.logback.classic.net.SyslogAppender">
<syslogHost>bindplane-ip</syslogHost>
<port>bindplane-port</port>
<facility>LOCAL7</facility>
<throwableExcluded>true</throwableExcluded>
<suffixPattern>%thread:%level:%logger{36}:%msg</suffixPattern>
</appender>
Replace
bindplane-ip
and
bindplane-port
with the actual Bindplane agent IP address and port.
Add the following code to the root logger block
<root level=
INFO
>
in the
logback.xml
file:
The location where this line is inserted depends on your version of Apache Cassandra:
Apache Cassandra 5.0.x, Line 123.
Apache Cassandra 4.0.x and 4.1.x, Line 115.
Apache Cassandra 3.11.x and 3.0.x, Line 92.
Datastax Enterprise (All versions), Line 121.
<appender-ref
ref=`SYSLOG`
/>
UDM mapping table
Log Field
UDM Mapping
Logic
agent.ephemeral_id
observer.labels.value
Value of
agent.ephemeral_id
from the inner JSON message.
agent.hostname
observer.hostname
Value of
agent.hostname
from the inner JSON message.
agent.id
observer.asset_id
Concatenation of
filebeat:
and the value of
agent.id
from the inner JSON message.
agent.name
observer.user.userid
Value of
agent.name
from the inner JSON message.
agent.type
observer.application
Value of
agent.type
from the inner JSON message.
agent.version
observer.platform_version
Value of
agent.version
from the inner JSON message.
cloud.availability_zone
principal.cloud.availability_zone
Value of
cloud.availability_zone
from the inner JSON message.
cloud.instance.id
principal.resource.product_object_id
Value of
cloud.instance.id
from the inner JSON message.
cloud.instance.name
principal.resource.name
Value of
cloud.instance.name
from the inner JSON message.
cloud.machine.type
principal.resource.attribute.labels.value
Value of
cloud.machine.type
from the inner JSON message, where the corresponding
key
is
machine_type
.
cloud.provider
principal.resource.attribute.labels.value
Value of
cloud.provider
from the inner JSON message, where the corresponding
key
is
provider
.
event_metadata._id
metadata.product_log_id
Value of
event_metadata._id
from the inner JSON message.
event_metadata.version
metadata.product_version
Value of
event_metadata.version
from the inner JSON message.
host.architecture
target.asset.hardware.cpu_platform
Value of
host.architecture
from the inner JSON message.
host.fqdn
target.administrative_domain
Value of
host.fqdn
from the inner JSON message.
host.hostname
target.hostname
Value of
host.hostname
from the inner JSON message.
host.id
target.asset.asset_id
Concatenation of
Host Id:
and the value of
host.id
from the inner JSON message.
host.ip
target.asset.ip
Array of IP addresses from
host.ip
in the inner JSON message.
host.mac
target.mac
Array of MAC addresses from
host.mac
in the inner JSON message.
host.os.kernel
target.platform_patch_level
Value of
host.os.kernel
from the inner JSON message.
host.os.platform
target.platform
Set to
LINUX
if
host.os.platform
is
debian
.
host.os.version
target.platform_version
Value of
host.os.version
from the inner JSON message.
hostname
principal.hostname
Value of
hostname
extracted from the
message
field using grok.
key
security_result.detection_fields.value
Value of
key
extracted from the
message
field using grok, where the corresponding
key
is
key
.
log.file.path
principal.process.file.full_path
Value of
log.file.path
from the inner JSON message.
log_level
security_result.severity
Mapped based on the value of
log_level
:
DEBUG
,
INFO
,
AUDIT
map to
INFORMATIONAL
;
ERROR
maps to
ERROR
;
WARNING
maps to
MEDIUM
.
log_level
security_result.severity_details
Value of
log_level
extracted from the
message
field using grok.
log_type
metadata.log_type
Value of
log_type
from the raw log.
message
security_result.description
Description extracted from the
message
field using grok.
message
target.process.command_line
Command line extracted from the
message
field using grok.
now
security_result.detection_fields.value
Value of
now
extracted from the
message
field using grok, where the corresponding
key
is
now
. Parsed from the
event_time
field extracted from the
message
field using grok. Set to
USER_RESOURCE_ACCESS
if both
hostname
and
host.hostname
are present, otherwise set to
GENERIC_EVENT
. Set to
CASSANDRA
. Set to
CASSANDRA
. Set to
ephemeral_id
. Set to
VIRTUAL_MACHINE
if
cloud.instance.name
is present. Set to
key
and
now
for the corresponding detection fields.
timestamp
timestamp
From the raw log's
create_time
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
