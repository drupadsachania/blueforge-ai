# Collect Apache Hadoop logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hadoop/  
**Scraped:** 2026-03-05T09:49:48.445006Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Apache Hadoop logs
Supported in:
Google secops
SIEM
This document explains how to ingest Apache Hadoop logs to Google Security Operations using Bindplane. The parser first extracts fields from raw Hadoop logs using Grok patterns based on common Hadoop log formats. Then, it maps the extracted fields to the corresponding fields in the Unified Data Model (UDM) schema, performs data type conversions, and enriches the data with additional context.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Apache Hadoop cluster configuration files
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
'HADOOP'
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
Configure Syslog forwarding on Apache Hadoop
Apache Hadoop uses
Log4j
for logging. Configure the appropriate
Syslog appender
based on your Log4j version so that Hadoop daemons (NameNode, DataNode, ResourceManager, NodeManager, etc.) forward logs directly to your syslog receiver (Bindplane host). Log4j is configured via files (no web UI).
Option 1: Log4j 1.x configuration
Locate the
log4j.properties
file (typically in
$HADOOP_CONF_DIR/log4j.properties
).
Add the following
SyslogAppender
configuration to the file:
# Syslog appender (UDP example)
log4j.appender.SYSLOG
=
org.apache.log4j.net.SyslogAppender
log4j.appender.SYSLOG.SyslogHost
=
<
BINDPLANE_HOST_IP>:514
log4j.appender.SYSLOG.Facility
=
LOCAL0
log4j.appender.SYSLOG.FacilityPrinting
=
true
log4j.appender.SYSLOG.layout
=
org.apache.log4j.PatternLayout
log4j.appender.SYSLOG.layout.ConversionPattern
=
%d{ISO8601} level=%p logger=%c thread=%t msg=%m%n
# Example: send NameNode logs to syslog
log4j.logger.org.apache.hadoop.hdfs.server.namenode
=
INFO,SYSLOG
log4j.additivity.org.apache.hadoop.hdfs.server.namenode
=
false
# Or attach to root logger to send all Hadoop logs
# log4j.rootLogger=INFO, SYSLOG
Replace
<BINDPLANE_HOST_IP>
with the IP address of your Bindplane host.
Save the file.
Restart Hadoop daemons
to apply the configuration changes.
Option 2: Log4j 2.x configuration
Locate the
log4j2.xml
file (typically in
$HADOOP_CONF_DIR/log4j2.xml
).
Add the following
Syslog appender
configuration to the file:
<Configuration
status="WARN">
<Appenders>
<!--
UDP
example;
for
TCP
use
protocol="TCP"
-->
<Syslog
name="SYSLOG"
format="RFC5424"
host="<BINDPLANE_HOST_IP>"
port="514"
protocol="UDP"
facility="LOCAL0"
appName="hadoop"
enterpriseNumber="18060"
mdcId="mdc">
<PatternLayout
pattern="%d{ISO8601}
level=%p
logger=%c
thread=%t
msg=%m
%X%n"/>
</Syslog>
</Appenders>
<Loggers>
<!--
Send
NameNode
logs
to
syslog
-->
<Logger
name="org.apache.hadoop.hdfs.server.namenode"
level="info"
additivity="false">
<AppenderRef
ref="SYSLOG"/>
</Logger>
<!--
Or
send
all
Hadoop
logs
-->
<Root
level="info">
<AppenderRef
ref="SYSLOG"/>
</Root>
</Loggers>
</Configuration>
Replace
<BINDPLANE_HOST_IP>
with the IP address of your Bindplane host.
Save the file.
Restart Hadoop daemons
to apply the configuration changes.
UDM Mapping Table
Log Field
UDM Mapping
Logic
allowed
security_result.action
If "false", action is "BLOCK". If "true", action is "ALLOW".
auth_type
additional.fields.key = "auth_type", additional.fields.value.string_value
Extracted from "ugi" field using grok pattern "%{DATA:suser}@.*auth:%{WORD:auth_type}". Parentheses and "auth:" are removed.
call
additional.fields.key = "Call#", additional.fields.value.string_value
Directly mapped.
call_context
additional.fields.key = "callerContext", additional.fields.value.string_value
Directly mapped.
cliIP
principal.ip
Mapped only when "json_data" field exists and is successfully parsed as JSON.
cmd
principal.process.command_line
Directly mapped.
cluster_name
target.hostname
Used as target hostname if present.
day
metadata.event_timestamp.seconds
Used with month, year, hours, minutes, and seconds to construct event_timestamp.
description
metadata.description
Directly mapped.
driver
additional.fields.key = "driver", additional.fields.value.string_value
Directly mapped.
dst
target.ip OR target.hostname OR target.file.full_path
If successfully parsed as IP, mapped to target IP. If the value starts with "/user", mapped to target file path. Otherwise, mapped to target hostname.
dstport
target.port
Directly mapped and converted to integer.
enforcer
security_result.rule_name
Directly mapped.
event_count
additional.fields.key = "event_count", additional.fields.value.string_value
Directly mapped and converted to string.
fname
src.file.full_path
Directly mapped.
hours
metadata.event_timestamp.seconds
Used with month, day, year, minutes, and seconds to construct event_timestamp.
id
additional.fields.key = "id", additional.fields.value.string_value
Directly mapped.
ip
principal.ip
Mapped to principal IP after removing any leading "/" character.
json_data
Parsed as JSON. Extracted fields are mapped to corresponding UDM fields.
logType
additional.fields.key = "logType", additional.fields.value.string_value
Directly mapped.
message
Used for extracting various fields using grok patterns.
method
network.http.method
Directly mapped.
minutes
metadata.event_timestamp.seconds
Used with month, day, year, hours, and seconds to construct event_timestamp.
month
metadata.event_timestamp.seconds
Used with day, year, hours, minutes, and seconds to construct event_timestamp.
observer
observer.hostname OR observer.ip
If successfully parsed as IP, mapped to observer IP. Otherwise, mapped to observer hostname.
perm
additional.fields.key = "perm", additional.fields.value.string_value
Directly mapped.
policy
security_result.rule_id
Directly mapped and converted to string.
product
metadata.product_name
Directly mapped.
product_event
metadata.product_event_type
Directly mapped. If "rename", the "dst" field is mapped to "target.file.full_path".
proto
network.application_protocol
Directly mapped and converted to uppercase if it's not "webhdfs".
reason
security_result.summary
Directly mapped.
repo
additional.fields.key = "repo", additional.fields.value.string_value
Directly mapped.
resType
additional.fields.key = "resType", additional.fields.value.string_value
Directly mapped.
result
additional.fields.key = "result", additional.fields.value.string_value
Directly mapped and converted to string.
Retry
additional.fields.key = "Retry#", additional.fields.value.string_value
Directly mapped.
seconds
metadata.event_timestamp.seconds
Used with month, day, year, hours, and minutes to construct event_timestamp.
seq_num
additional.fields.key = "seq_num", additional.fields.value.string_value
Directly mapped and converted to string.
severity
security_result.severity
Mapped to different severity levels based on the value: "INFO", "Info", "info" -> "INFORMATIONAL"; "Low", "low", "LOW" -> "LOW"; "error", "Error", "WARN", "Warn" -> "MEDIUM"; "High", "high", "HIGH" -> "HIGH"; "Critical", "critical", "CRITICAL" -> "CRITICAL".
shost
principal.hostname
Used as principal hostname if different from "src".
src
principal.ip OR principal.hostname OR observer.ip
If successfully parsed as IP, mapped to principal and observer IP. Otherwise, mapped to principal hostname.
srcport
principal.port
Directly mapped and converted to integer.
summary
security_result.summary
Directly mapped.
suser
principal.user.userid
Directly mapped.
tags
additional.fields.key = "tags", additional.fields.value.string_value
Directly mapped.
thread
additional.fields.key = "thread", additional.fields.value.string_value
Directly mapped.
tip
target.ip
Directly mapped.
ugi
target.hostname
Used as target hostname if "log_data" field doesn't contain "·".
url
target.url
Directly mapped.
vendor
metadata.vendor_name
Directly mapped.
version
metadata.product_version
Directly mapped.
year
metadata.event_timestamp.seconds
Used with month, day, hours, minutes, and seconds to construct event_timestamp.
N/A
metadata.event_type
Set to "NETWORK_CONNECTION" by default. Changed to "STATUS_UPDATE" if no target is identified.
N/A
metadata.log_type
Set to "HADOOP".
N/A
security_result.alert_state
Set to "ALERTING" if severity is "HIGH" or "CRITICAL".
N/A
is_alert
Set to "true" if severity is "HIGH" or "CRITICAL".
N/A
is_significant
Set to "true" if severity is "HIGH" or "CRITICAL".
Need more help?
Get answers from Community members and Google SecOps professionals.
