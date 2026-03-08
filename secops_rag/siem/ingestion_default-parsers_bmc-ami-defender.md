# Collect BMC AMI Defender logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-ami-defender/  
**Scraped:** 2026-03-05T09:20:37.688137Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BMC AMI Defender logs
Supported in:
Google secops
SIEM
This document explains how to ingest BMC AMI Defender logs to Google Security Operations using Bindplane agent.
BMC AMI Datastream for z/OS is a mainframe agent program that monitors z/OS system activity and collects, processes, and delivers System Management Facility (SMF) records to distributed SIEM systems in real time. The agent reformats SMF records from RACF, ACF2, Top Secret, TCP/IP, CICS, IMS, and other z/OS system and application events as RFC 3164 compliant syslog messages and transmits them via UDP, TCP, or TLS protocols.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
for the Bindplane agent
Network connectivity between the Bindplane agent host and the z/OS LPAR running BMC AMI Datastream
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
BMC AMI Datastream for z/OS version 6.1 or later installed and running on the z/OS LPAR
Access to edit parameter files in the amihlq.PARM data set on z/OS (typically requires TSO/ISPF access or batch job submission authority)
Authority to modify BMC AMI Datastream configuration (typically requires RACF READ access to the parameter data sets)
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
system where Bindplane is to be installed.
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
Open
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
Wait for the installation to complete.
Verify the installation by running:
sc query observiq-otel-collector
The service should show as
RUNNING
.
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
Wait for the installation to complete.
Verify the installation by running:
sudo
systemctl
status
observiq-otel-collector
The service should show as
active (running)
.
Additional installation resources
For additional installation options and troubleshooting, see
Bindplane agent installation guide
.
Configure Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/etc/bindplane-agent/config.yaml
Windows:
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
Edit the configuration file
Replace the entire contents of
config.yaml
with the following configuration:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:1514"
exporters
:
chronicle/bmc_datastream
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'your-customer-id-here'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
BMC_AMI_DEFENDER
raw_log_field
:
body
service
:
pipelines
:
logs/datastream_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/bmc_datastream
Replace the following placeholders:
Receiver configuration:
listen_address
: IP address and port to listen on:
0.0.0.0:1514
to listen on all interfaces on port 1514 (recommended for Linux non-root)
0.0.0.0:514
to listen on all interfaces on standard syslog port (requires root on Linux)
Specific IP address to listen on one interface
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
customer_id
: Your
customer ID
. For details, see
Get Google SecOps customer ID
.
endpoint
: Regional endpoint URL:
US
:
malachiteingestion-pa.googleapis.com
Europe
:
europe-malachiteingestion-pa.googleapis.com
Asia
:
asia-southeast1-malachiteingestion-pa.googleapis.com
See
Regional Endpoints
for complete list
log_type
:
BMC_AMI_DEFENDER
Example configuration for UDP syslog
If you prefer UDP transport (lower latency, fire-and-forget):
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/bmc_datastream
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
BMC_AMI_DEFENDER
raw_log_field
:
body
service
:
pipelines
:
logs/datastream_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/bmc_datastream
Save the configuration file
After editing, save the file:
Linux
: Press
Ctrl+O
, then
Enter
, then
Ctrl+X
Windows
: Click
File
>
Save
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux:
Run the following command:
sudo
systemctl
restart
observiq-otel-collector
Verify the service is running:
sudo
systemctl
status
observiq-otel-collector
Check logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
To restart the Bindplane agent in Windows:
Choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press Enter.
Locate
observIQ OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure BMC AMI Defender syslog forwarding
Edit the parameter file using TSO/ISPF
Sign in to TSO/ISPF on the z/OS LPAR where BMC AMI Datastream is installed.
From the
ISPF Primary Option Menu
, enter
2
to select
EDIT
.
On the
Edit - Entry Panel
, enter the following:
ISPF Library
: Enter the parameter data set name in the format
'amihlq.PARM'
where amihlq is the high-level qualifier chosen during installation (for example,
'PROD.CZAGENT.PARM'
).
Member
: Enter
$$$CONFG
.
Press
Enter
to open the member for editing.
Configure the SIEM type
In the
$$$CONFG
member, locate the section labeled
Switches for setting the SIEM type
.
Uncomment one SIEM type by removing the leading semicolon from the appropriate line:
For standard syslog format, uncomment:
SWITCH ON(RFC3164)
For Common Event Format, uncomment:
SWITCH ON(CEF)
For JSON format, uncomment:
SWITCH ON(JSON)
For IBM QRadar LEEF format, uncomment:
SWITCH ON(LEEF)
For Splunk format, uncomment:
SWITCH ON(Splunk)
Press
F3
to save and exit the member.
Configure the syslog server
From the
Edit - Entry Panel
, enter the following:
ISPF Library
: Enter
'amihlq.PARM'
(same as before).
Member
: Enter
$$$SERVR
.
Press
Enter
to open the member for editing.
Locate the section corresponding to your selected SIEM type. For example:
For RFC3164: Locate the section labeled
; RFC3164
For CEF: Locate the section labeled
; CEF - TRANS(TCP) Recommended
For JSON: Locate the section labeled
; JSON - TRANS(TCP) Recommended
Uncomment the SERVER statement by removing the leading semicolon.
Edit the SERVER statement with the following values:
Replace
ip.addr.example
with the IP address of the Bindplane agent host (for example,
192.168.1.100
).
If using TCP (recommended), the statement should look like:
SERVER 192.168.1.100:1514 TRANS(TCP) MAXMSG(2000)
If using UDP, the statement should look like:
SERVER 192.168.1.100:514 TRANS(UDP) MAXMSG(2000)
If you selected CEF, JSON, or Splunk format and are using TCP transport, locate the OPTIONS statement section and uncomment the FRAMING parameter:
OPTIONS FRAMING(OCTETCOUNT)
Press
F3
to save and exit the member.
Refresh the BMC AMI Datastream configuration
From the
ISPF Primary Option Menu
, enter
6
to select
COMMAND
.
On the
TSO Command Processor
screen, enter the following MVS console command:
F czagentname,PARMS
Replace
czagentname
with the name of the BMC AMI Datastream started task (typically
CZAGENT
or the instance name configured during installation).
Press
Enter
to execute the command.
Verify the configuration was refreshed by checking the system log for message
CZA0001I
indicating the parameter file was successfully processed.
Verify syslog transmission
From the
ISPF Primary Option Menu
, enter
6
to select
COMMAND
.
Enter the following command to display BMC AMI Datastream statistics:
F czagentname,STATS
Press
Enter
to execute the command.
Check the system log for message
CZA0350I
showing the number of messages sent to the syslog server.
Verify the Bindplane agent is receiving messages by checking the Bindplane agent logs:
Linux
:
sudo journalctl -u observiq-otel-collector -f
Windows
: Check
C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log
Alternative: Edit parameter file using batch job
If you do not have TSO/ISPF access, you can edit the parameter files using a batch job:
Create a batch job with the following JCL:
//
EDITPARM
JOB
(
ACCT
),
'EDIT DATASTREAM PARMS'
,
//
CLASS
=
A
,
MSGCLASS
=
X
,
NOTIFY
=
&
SYSUID
//
STEP1
EXEC
PGM
=
IEBGENER
//
SYSPRINT
DD
SYSOUT
=
*
//
SYSIN
DD
DUMMY
//
SYSUT1
DD
*
SWITCH ON(RFC3164)
/*
//
SYSUT2
DD
DSN
=
amihlq
.
PARM
(
$$$
CONFG
),
DISP
=
SHR
//
STEP2
EXEC
PGM
=
IEBGENER
//
SYSPRINT
DD
SYSOUT
=
*
//
SYSIN
DD
DUMMY
//
SYSUT1
DD
*
SERVER 192.168.1.100:1514 TRANS(TCP) MAXMSG(2000)
/*
//
SYSUT2
DD
DSN
=
amihlq
.
PARM
(
$$$
SERVR
),
DISP
=
SHR
Replace
amihlq
with the high-level qualifier for your BMC AMI Datastream installation.
Replace
192.168.1.100:1514
with the IP address and port of your Bindplane agent host.
Submit the job and verify successful completion (return code 0).
Issue the MODIFY command to refresh the configuration as described in the previous section.
UDM mapping table
Log Field
UDM Mapping
Logic
aceeadsp
security_result.detection_fields
Fields that were used to determine the security result
aceeaudt
security_result.detection_fields
Fields that were used to determine the security result
aceeflg1
security_result.detection_fields
Fields that were used to determine the security result
aceelogu
security_result.detection_fields
Fields that were used to determine the security result
aceeoper
security_result.detection_fields
Fields that were used to determine the security result
aceepriv
security_result.detection_fields
Fields that were used to determine the security result
aceeracf
security_result.detection_fields
Fields that were used to determine the security result
aceeroa
security_result.detection_fields
Fields that were used to determine the security result
aceespec
security_result.detection_fields
Fields that were used to determine the security result
additional.fields
additional.fields
Additional information about the event
auth
security_result.detection_fields
Fields that were used to determine the security result
auth_audit
security_result.detection_fields
Fields that were used to determine the security result
auth_bypass
security_result.detection_fields
Fields that were used to determine the security result
auth_exit
security_result.detection_fields
Fields that were used to determine the security result
auth_normal
security_result.detection_fields
Fields that were used to determine the security result
auth_oper
security_result.detection_fields
Fields that were used to determine the security result
auth_soft
security_result.detection_fields
Fields that were used to determine the security result
auth_special
security_result.detection_fields
Fields that were used to determine the security result
auth_trusted
security_result.detection_fields
Fields that were used to determine the security result
authinfo
security_result.description
Description of the security result
event
metadata.product_event_type
Product-specific event type
event_type
metadata.event_type
Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)
eventdesc
metadata.description
Description of the event
group
additional.fields
Additional information about the event
hostname
principal.hostname, principal.asset.hostname
Hostname of the principal, Hostname of the asset
jobid
security_result.detection_fields
Fields that were used to determine the security result
jobnm
additional.fields
Additional information about the event
jsauth
security_result.detection_fields
Fields that were used to determine the security result
name
principal.user.user_display_name
Display name of the user
pgm
security_result.detection_fields
Fields that were used to determine the security result
privstatd
security_result.detection_fields
Fields that were used to determine the security result
reas_always
security_result.detection_fields
Fields that were used to determine the security result
reas_audit
security_result.detection_fields
Fields that were used to determine the security result
reas_cmdviol
security_result.detection_fields
Fields that were used to determine the security result
reas_globalaudit
security_result.detection_fields
Fields that were used to determine the security result
reas_setropts
security_result.detection_fields
Fields that were used to determine the security result
reas_special
security_result.detection_fields
Fields that were used to determine the security result
reas_user
security_result.detection_fields
Fields that were used to determine the security result
reas_verify
security_result.detection_fields
Fields that were used to determine the security result
rtype
additional.fields
Additional information about the event
saf
additional.fields
Additional information about the event
safd
additional.fields
Additional information about the event
security_result.detection_fields
security_result.detection_fields
Fields that were used to determine the security result
severity
security_result.severity, security_result.severity_details
Severity of the security result, Detailed severity information
sid
additional.fields
Additional information about the event
timestamp
metadata.event_timestamp
Timestamp when the event occurred
tokflg1
security_result.detection_fields
Fields that were used to determine the security result
tokflg3
security_result.detection_fields
Fields that were used to determine the security result
tokpriv
security_result.detection_fields
Fields that were used to determine the security result
toksus
security_result.detection_fields
Fields that were used to determine the security result
tokudus
security_result.detection_fields
Fields that were used to determine the security result
userid
principal.user.userid
User ID
violation
security_result.detection_fields
Fields that were used to determine the security result
user_warning
security_result.detection_fields
Fields that were used to determine the security result
worktyped
additional.fields
Additional information about the event
metadata.product_name
Name of the product
metadata.vendor_name
Vendor/company name
Need more help?
Get answers from Community members and Google SecOps professionals.
