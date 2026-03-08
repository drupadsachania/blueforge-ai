# Collect VanDyke VShell SFTP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vandyke-sftp/  
**Scraped:** 2026-03-05T10:01:55.700023Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VanDyke VShell SFTP logs
Supported in:
Google secops
SIEM
This document explains how to ingest VanDyke VShell SFTP logs to Google Security Operations using Bindplane with Syslog or Amazon S3 with a log shipper. The parser transforms raw logs into a structured UDM format. It handles both JSON and SYSLOG formats, extracts relevant fields like IP addresses, ports, and event details, and enriches the data with contextual information like platform details and security severity.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to the VanDyke VShell server or management console
For Option 1: A Windows 2016 or later or Linux host with
systemd
for the Bindplane agent
For Option 2: AWS account with S3 access and NXLog/Fluent Bit on the VShell server
Option 1: Integration via Bindplane and Syslog
This option provides real-time log streaming with minimal latency and is recommended for most deployments.
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the 
system where Bindplane will be installed or where you'll configure the feed.
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
# Custom log type - requires parser extension
log_type
:
'VANDYKE_SFTP'
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
For TCP instead of UDP, replace
udplog
with
tcplog
.
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
Configure Syslog forwarding on VanDyke VShell
For VShell on Windows
Sign in to the
VShell Control Panel
.
Go to
Logging
settings.
Configure remote syslog logging:
Enable logging to
remote syslog server
.
Server address
: Enter the Bindplane agent IP address.
Port
: Enter 514 (or your configured port).
Protocol
: Select
UDP
(or TCP if configured).
Message groups
: Select
Connection
,
Authentication
,
SFTP
,
FTPS
,
HTTPS
,
Errors
,
Warnings
, and
Informational
.
Click
Apply
>
OK
.
For VShell on Linux/macOS
Edit the
vshelld_config
file (typically
/etc/vshell/vshelld_config
).
Configure the following parameters:
SyslogFacility LOG_LOCAL3
LogLevel INFO
Configure your system's
syslog
to forward LOG_LOCAL3 to the Bindplane agent:
Edit
/etc/rsyslog.conf
or
/etc/syslog-ng/syslog-ng.conf
.
Add:
local3.*  @bindplane-agent-ip:514
(for UDP) or
local3.*  @@bindplane-agent-ip:514
(for TCP).
Restart the VShell service and syslog service:
sudo
systemctl
restart
vshelld
sudo
systemctl
restart
rsyslog
Option 2: Integration via AWS S3
This option is useful for environments that require log archival or where direct syslog forwarding is not feasible. Note that this requires a log shipper on the VShell server since AWS Lambda cannot access on-premise files.
Configure AWS S3 bucket and IAM for Google SecOps
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save bucket
Name
and
Region
for future reference (for example,
vandyke-sftp-logs
).
Create a
User
following this user guide:
Creating an IAM user
.
Select the created
User
.
Select
Security credentials
tab.
Click
Create Access Key
in section
Access Keys
.
Select
Third-party service
as
Use case
.
Click
Next
.
Optional: Add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
Access Key
and
Secret Access Key
for future reference.
Click
Done
.
Select
Permissions
tab.
Click
Add permissions
in section
Permissions policies
.
Select
Add permissions
.
Select
Attach policies directly
.
Search for
AmazonS3FullAccess
policy.
Select the policy.
Click
Next
.
Click
Add permissions
.
Install and Configure Log Shipper on VShell Server
Choose one of the following options based on your operating system:
Option A: Using NXLog (Windows)
Download and install
NXLog Community Edition
from
nxlog.co
.
Edit
C:\Program Files\nxlog\conf\nxlog.conf
:
<Extension
json>
Module
xm_json
</Extension>

<Extension
syslog>
Module
xm_syslog
</Extension>

<Input
vshell_log>
Module
im_file
File
"C:\\Program
Files\\VanDyke
Software\\VShell\\Log\\VShell.log"
SavePos
TRUE
<Exec>
#
Parse
VShell
log
format
if
$raw_event
=~
/^(\d{4}-\d{2}-\d{2}
\d{2}:\d{2}:\d{2})
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
(\S+)
"(.*)"$/
{
$EventTime
=
$1;
$Protocol
=
$2;
$EventType
=
$3;
$SessionID
=
$4;
$ClientIP
=
$5;
$ClientPort
=
$6;
$Username
=
$7;
$Filename
=
$9;
$BytesDown
=
$10;
$BytesUp
=
$11;
$ServerIP
=
$14;
$ServerPort
=
$15;
$EventMessage
=
$16;
#
Convert
to
JSON
to_json();
}
</Exec>
</Input>

<Output
s3>
Module
om_exec
Command
C:\scripts\upload_to_s3.ps1
Args
%FILEPATH%
</Output>

<Route
vshell_to_s3>
Path
vshell_log
=>
s3
</Route>
Create PowerShell script
C:\scripts\upload_to_s3.ps1
:
param
(
[string]
$FilePath
)
$bucket
=
"vandyke-sftp-logs"
$key
=
"vshell/
$(
Get-Date
-Format
'yyyy/MM/dd/HH'
)
/
$(
Get-Date
-Format
'yyyyMMddHHmmss'
)
.json"
# Batch logs
$logs
=
Get-Content
$FilePath
|
ConvertFrom-Json
$jsonLines
=
$logs
|
ForEach
-Object
{
$_
|
ConvertTo-Json
-Compress
}
$content
=
$jsonLines
-join
"
`n
"
# Upload to S3
Write-S3Object
-BucketName
$bucket
-Key
$key
-Content
$content
-ProfileName
default
Create AWS credentials profile:
Set-AWSCredential
-AccessKey
YOUR_ACCESS_KEY
-SecretKey
YOUR_SECRET_KEY
-StoreAs
default
Schedule the PowerShell script to run every 5 minutes using Task Scheduler.
Option B: Using Fluent Bit (Linux)
Install
Fluent Bit
:
curl
https://raw.githubusercontent.com/fluent/fluent-bit/master/install.sh
|
sh
Configure
/etc/fluent-bit/fluent-bit.conf
:
[SERVICE]
Flush        5
Daemon       On
Log_Level    info
[INPUT]
Name              tail
Path              /var/log/vshell/vshell.log
Parser            vshell_parser
Tag               vshell.*
Refresh_Interval  5
Mem_Buf_Limit     10MB
[PARSER]
Name        vshell_parser
Format      regex
Regex       ^(?<timestamp>\d{4}-\d{2}-\d{2} \d{2}
:
\d{2}:\d{2}) (?<protocol>\S+) (?<event_type>\S+) (?<session_id>\S+) (?<client_ip>\S+) (?<client_port>\S+) (?<username>\S+) (?<dash>\S+) (?<filename>\S+) (?<bytes_down>\S+) (?<bytes_up>\S+) (?<field1>\S+) (?<field2>\S+) (?<server_ip>\S+) (?<server_port>\S+) "(?<event_message>[^"]*)"
[OUTPUT]
Name                  s3
Match                 vshell.*
bucket                vandyke-sftp-logs
region                us-east-1
use_put_object        On
total_file_size       5M
upload_timeout        10s
compression           gzip
s3_key_format         /vshell/%Y/%m/%d/%H/%{hostname}_%{uuid}.json.gz
Configure AWS credentials:
export
AWS_ACCESS_KEY_ID
=
YOUR_ACCESS_KEY
export
AWS_SECRET_ACCESS_KEY
=
YOUR_SECRET_KEY
Start Fluent Bit:
sudo
systemctl
enable
fluent-bit
sudo
systemctl
start
fluent-bit
Configure a feed in Google SecOps to ingest VanDyke VShell logs
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
VanDyke VShell SFTP logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
VanDyke SFTP
as the
Log type
(custom).
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://vandyke-sftp-logs/vshell/
Source deletion options
: Select
Retain
(recommended) or the deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log field
UDM mapping
Logic
agent.id
read_only_udm.observer.asset_id
Concatenates "filebeat:" with the value of agent.id field
agent.type
read_only_udm.observer.application
Directly maps the value of agent.type field
agent.version
read_only_udm.observer.platform_version
Directly maps the value of agent.version field
ecs.version
read_only_udm.metadata.product_version
Directly maps the value of ecs.version field
host.architecture
read_only_udm.target.asset.hardware.cpu_platform
Directly maps the value of host.architecture field
host.hostname
read_only_udm.target.hostname
Directly maps the value of host.hostname field
host.id
read_only_udm.principal.asset_id
Concatenates "VANDYKE_SFTP:" with the value of host.id field
host.ip
read_only_udm.target.ip
Directly maps each IP address in the host.ip array to a separate read_only_udm.target.ip field
host.mac
read_only_udm.target.mac
Directly maps each MAC address in the host.mac array to a separate read_only_udm.target.mac field
host.os.kernel
read_only_udm.target.platform_patch_level
Directly maps the value of host.os.kernel field
host.os.platform
read_only_udm.target.platform
Maps the value of host.os.platform to WINDOWS, LINUX, MAC, or UNKNOWN_PLATFORM based on the value
host.os.version
read_only_udm.target.platform_version
Directly maps the value of host.os.version field
log.file.path
read_only_udm.principal.process.file.full_path
Directly maps the value of log.file.path field
logstash.collect.timestamp
read_only_udm.metadata.collected_timestamp
Parses the timestamp from logstash.collect.timestamp field and converts it to a timestamp object
logstash.irm_environment
read_only_udm.additional.fields.value.string_value
Directly maps the value of logstash.irm_environment field. The key is set to "irm_environment"
logstash.irm_region
read_only_udm.additional.fields.value.string_value
Directly maps the value of logstash.irm_region field. The key is set to "irm_region"
logstash.irm_site
read_only_udm.additional.fields.value.string_value
Directly maps the value of logstash.irm_site field. The key is set to "irm_site"
logstash.process.host
read_only_udm.observer.hostname
Directly maps the value of logstash.process.host field
message
Used for extracting various fields using grok patterns and regular expressions
read_only_udm.metadata.event_type
Set to "NETWORK_FTP"
read_only_udm.metadata.log_type
Set to "VANDYKE_SFTP"
read_only_udm.metadata.product_event_type
Extracted from the message field using a grok pattern
read_only_udm.metadata.product_name
Set to "VANDYKE_SFTP"
read_only_udm.metadata.vendor_name
Set to "VANDYKE SOFTWARE"
read_only_udm.network.application_protocol
Set to "SSH" if the description field contains "SSH2" or "SSH", otherwise set to "HTTP" if the method field matches HTTP methods
read_only_udm.network.http.method
Extracted from the message field using a grok pattern, only if it matches common HTTP methods
read_only_udm.network.http.referral_url
Extracted from the message field using a grok pattern
read_only_udm.network.http.response_code
Extracted from the message field using a grok pattern and converted to an integer
read_only_udm.network.ip_protocol
Set to "TCP" if the description field contains "TCP"
read_only_udm.principal.ip
Extracted from the message field using a grok pattern
read_only_udm.principal.port
Extracted from the message field using a grok pattern and converted to an integer
read_only_udm.security_result.description
Extracted from the message field using a grok pattern
read_only_udm.security_result.severity
Set to "HIGH" if syslog_severity is "error" or "warning", "MEDIUM" if it's "notice", and "LOW" if it's "information" or "info"
read_only_udm.security_result.severity_details
Directly maps the value of syslog_severity field
read_only_udm.target.ip
Extracted from the message field using a grok pattern
read_only_udm.target.port
Extracted from the message field using a grok pattern and converted to an integer
read_only_udm.target.process.pid
Extracted from the message field using a grok pattern
syslog_severity
Used for determining the severity of the security_result
Need more help?
Get answers from Community members and Google SecOps professionals.
