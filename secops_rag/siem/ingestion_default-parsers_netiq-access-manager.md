# Collect Micro Focus NetIQ Access Manager logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netiq-access-manager/  
**Scraped:** 2026-03-05T09:26:13.392398Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Micro Focus NetIQ Access Manager logs
Supported in:
Google secops
SIEM
This document explains how to collect Micro Focus NetIQ Access Manager logs to Google Security Operations using Bindplane. Micro Focus NetIQ Access Manager is an identity and access management (IAM) solution designed to secure applications and data by providing centralized authentication, authorization, and single sign-on (SSO) capabilities.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to NetIQ Access Manager.
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
receivers
:
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:5252"
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
SYSLOG
namespace
:
netiq_access
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
tcplog
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
Configure Identity Server audit events in NetIQ Access Manager
Sign in to the NetIQ administration console.
Select
Devices
>
Identity server
>
Servers
>
Edit
>
Auditing and logging
.
For
Audit logging
, select
Enabled
.
To audit all events, select
Select All
.
Click
Apply
>
OK
.
Click
Servers
>
Update servers
.
Configure Access Gateway audit events in NetIQ Access Manager
Sign in to the NetIQ administration console.
Go to
Devices
>
Access gateways
>
Edit
>
Auditing
.
Click
Select All
.
Click
OK
>
OK
.
On the
Access gateways
page, click
Update
.
Configure Logging Server in NetIQ Access Manager
Sign in to the NetIQ administration console.
Click
Auditing
.
Specify the following details:
Audit messages using syslog
: select this option to send audit events to the audit server.
Stop service on audit server failure
: leave blank.
Server listening address
: enter
Bindplane
IP Address.
Port
: specify the syslog port used to connect to
Bindplane
.
Format
: select
CSV
.
Management console audit events
: select
All
.
If syslog is selected for auditing, do the following:
In
nam.conf
, change the
SYSLOG_DAEMON
value to
rsyslog
. This changes the default syslog daemon to
rsyslog
.
To edit the
Auditlogging.cfg
file and set both
SERVERIP
and
SERVERPORT
macros as empty, run the following:
LOGDEST=syslog
FORMAT=JSON
SERVERIP=
SERVERPORT=
To configure UDP, run the following:
#$ModLoad imtcp # load TCP listener
  $InputTCPServerRun 1290
  $template ForwardFormat,"<%PRI%>%TIMESTAMP:::date-rfc3164% %HOSTNAME% %syslogtag:1:32%%msg:::sp-if-no-1st-sp%%msg%\n"
  $ModLoad imudp
  local0.* @FORWARDERIP:
PORT_NUMBER
;ForwardFormat
Restart the
rsyslog
service.
Supported NetIQ Access Manager sample logs
CEF (Common Event Format)
<
13>2025
-
11
-
04
T17
:
09
:
32.013686
-
05
:
00
San
-
Host
-
01
CEF
:
0
|
NetIQ
|
iManager
|
3.1.0
|
CEF150004
|
Authentication
|
1
|
sourceServiceName
=
a
.
a
.
b
.
u
.
b
src
=
10.0.0.1
cs2Label
=
MimeHint
cs2
=
0
cs6Label
=
host
cs6
=
10.0.0.1
cs3Label
=
eventID
cs3
=
0.0.11.0
cs4Label
=
eventName
cs4
=
Authentication
Session
flexString1Label
=
SubEvent
flexString1
=
150004
cs5Label
=
CorrelationID
cs5
=
iManager
#
0
#
DUMMY_SESSION_ID
outcome
=
Success
Syslog + JSON (Short-key Schema)
{
"syslog_header"
:
"Mar 03 08:57:52 san-dmz-nam-01 AccessManager"
,
"wrapper"
:
"@...@"
,
"payload"
:
{
"I"
:
"002E0514"
,
"A"
:
"002E"
,
"O"
:
"AG\\Application Access"
,
"L"
:
"7"
,
"G"
:
"0"
,
"B"
:
"ag-DUMMY_SESSION_ID_123"
,
"H"
:
"0"
,
"U"
:
"DEMO_SITE_USER"
,
"V"
:
"0"
,
"Y"
:
"https://demo.corp.biz/EWSCWebAppJ/jsp/EWSCLogin.jsp"
,
"S"
:
"cn=DEMO_USER ou=people ou=partners ou=identities o=corp-dmz"
,
"T"
:
"DUMMY_TOKEN_STRING_XYZ?Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; gdn/adcp; managedpc; rv:11.0) like Gecko"
,
"F"
:
"PS_QA_JBOSS_C2"
,
"1"
:
"894075914"
,
"2"
:
"0"
,
"3"
:
"0"
,
"M"
:
"0"
,
"D"
:
""
}
}
Syslog + JSON (Long-key Schema)
{
"syslog_header"
:
"Jun 04 07:01:35 san-dmz-nam-01"
,
"payload"
:
{
"appName"
:
"Novell Access Manager"
,
"timeStamp"
:
"Sun, 19 Jun 2025 07:01:35 +0000"
,
"eventId"
:
"002E0052"
,
"subTarget"
:
"impersonatorsessionid"
,
"stringValue1"
:
"sanitized_user"
,
"stringValue2"
:
"Impersonatee-session-ID-DUMMY"
,
"stringValue3"
:
"Description-of-the-event"
,
"numericValue1"
:
0
,
"numericValue2"
:
0
,
"numericValue3"
:
0
,
"data"
:
"MTAuMC4wLjE="
,
"description"
:
null
,
"message"
:
null
,
"component"
:
"nidp\\impersonation"
,
"originator"
:
"esp-DUMMY_ORIGIN_ID"
,
"target"
:
"target_user"
}
}
Need more help?
Get answers from Community members and Google SecOps professionals.
