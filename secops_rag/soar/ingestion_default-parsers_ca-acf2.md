# Collect CA ACF2 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-acf2/  
**Scraped:** 2026-03-05T09:51:42.752020Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CA ACF2 logs
Supported in:
Google secops
SIEM
This document explains how to ingest CA ACF2 logs to Google Security Operations using Bindplane agent.
Broadcom ACF2 (Access Control Facility 2) for z/OS is a mainframe security product that provides access control, authentication, and auditing for IBM z/OS systems. ACF2 logs security events to IBM System Management Facility (SMF) records (default type 230), including authentication attempts, data set access violations, resource access events, TSO command logging, and database modifications. These SMF records must be forwarded to Chronicle using a third-party agent such as BMC AMI Defender for z/OS.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and the BMC AMI Defender for z/OS agent
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
BMC AMI Defender for z/OS installed and running on the z/OS LPAR where ACF2 is active
Access to modify the BMC AMI Defender parameter files in the
amihlq.CZAGENT.PARM
data set
Authority to start or modify the CZAGENT started task on z/OS
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
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/acf2_logs
:
compression
:
gzip
creds_file_path
:
'/etc/bindplane-agent/ingestion-auth.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
CA_ACF2
raw_log_field
:
body
ingestion_labels
:
env
:
production
source
:
acf2
service
:
pipelines
:
logs/acf2_to_chronicle
:
receivers
:
-
udplog
exporters
:
-
chronicle/acf2_logs
Replace the following placeholders:
Receiver configuration:
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on UDP port 514
For Linux systems running as non-root, use port
1514
or higher
Match this port with the BMC AMI Defender SERVER statement configuration
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
: Replace
YOUR_CUSTOMER_ID
with your
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
: Set to
CA_ACF2
(Chronicle ingestion label for ACF2 logs)
ingestion_labels
: Optional labels to categorize logs (customize as needed)
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
Configure BMC AMI Defender for z/OS to forward ACF2 SMF records
Edit the $$$SERVR parameter member
Sign in to the z/OS system using TSO/ISPF or a 3270 emulator.
Navigate to the BMC AMI Defender parameter library:
Enter
ISPF
at the TSO READY prompt.
Select option
2
(Edit).
In the
ISPF Library
field, enter the data set name:
amihlq.CZAGENT.PARM
(replace
amihlq
with your installation high-level qualifier).
Press
Enter
.
Edit the
$$$SERVR
member:
Type
E
next to the
$$$SERVR
member.
Press
Enter
.
Locate the SERVER statement section (approximately line 40-60).
Uncomment one of the SERVER statements by removing the leading semicolon (
;
).
Configure the SERVER statement with the Bindplane agent IP address and port:
SERVER bindplane-host-ip:514 TRANS(UDP) MAXMSG(2000)
Replace
bindplane-host-ip
with the IP address of the Bindplane agent host (for example,
192.168.1.100
).
If using a non-standard port (for example,
1514
), specify:
bindplane-host-ip:1514
.
TRANS(UDP)
specifies UDP transport protocol (recommended for syslog).
MAXMSG(2000)
sets the maximum message length to 2000 bytes (ACF2 records may require larger sizes).
Verify the OPTIONS statement for syslog format:
Scroll up to locate the OPTIONS statements (approximately line 10-30).
Ensure one of the following OPTIONS statements is uncommented based on your preferred format:
OPTIONS IF(RFC3164) SIEM(RFC3164) TIMESTAMP INSTNAME(SIEM.Agent)
RFC3164
: Standard syslog format (recommended for Chronicle)
CEF
: Common Event Format (alternative)
LEEF
: Log Event Extended Format (alternative)
JSON
: JSON format (alternative)
Save the changes:
Press
F3
to exit the editor.
Type
SAVE
when prompted.
Press
Enter
.
Edit the $$$CONFG parameter member to enable ACF2 SMF record collection
In the
amihlq.CZAGENT.PARM
data set member list, edit the
$$$CONFG
member:
Type
E
next to the
$$$CONFG
member.
Press
Enter
.
Locate the ACF2 SMF record selection switch (search for
ACF2
or
SMF 230
).
Uncomment the SELECT statement for ACF2:
SELECT IF(ACF2) SMF(ACF2)
This enables collection of ACF2 SMF records (default type 230).
If your site uses a different SMF record type for ACF2, verify the type with the command:
ACF SHOW SYSTEMS
in TSO.
Save the changes:
Press
F3
to exit the editor.
Type
SAVE
when prompted.
Press
Enter
.
Create or edit the SMF ACF2 statement parameter member
In the
amihlq.CZAGENT.PARM
data set member list, check if a member named
$$$ACF2
or
SMFACF2
exists.
If the member does not exist, create it:
Type
C
(Create) on the command line.
Enter the member name:
$$$ACF2
.
Press
Enter
.
Edit the member and add the following SMF ACF2 statement:
SMF ACF2(230) FACILITY(SECURITY4) SEVERITY(INFORMATIONAL)
ACF2(230)
: Specifies the SMF record type for ACF2 (default is 230; verify with
ACF SHOW SYSTEMS
).
FACILITY(SECURITY4)
: Sets the syslog facility to Security (4).
SEVERITY(INFORMATIONAL)
: Sets the default severity to Informational.
Invalid password or authority violations are automatically sent with severity ERROR.
Resource violations are automatically sent with severity ERROR.
Optionally, configure specific ACF2 subtypes and severities:
SMF ACF2(230) +
  FACILITY(SECURITY4) +
  SEVERITY(INFORMATIONAL) +
  SUBTYPES(P SEV(ERROR)) +
  SUBTYPES(V SEV(ERROR)) +
  SUBTYPES(D SEV(ERROR))
Subtype
P
: Invalid password or authority events (ERROR severity)
Subtype
V
: Resource violations (ERROR severity)
Subtype
D
: Data set access violations (ERROR severity)
Save the changes:
Press
F3
to exit the editor.
Type
SAVE
when prompted.
Press
Enter
.
Refresh the BMC AMI Defender parameter file
Exit ISPF and return to the TSO READY prompt.
Issue the MODIFY command to reload the parameter file:
F CZAGENT,PARMS
Replace
CZAGENT
with your BMC AMI Defender started task name if different.
This command reloads the parameter file without stopping the agent.
Verify the configuration by checking the CZAPRINT output:
In ISPF, select option
3.4
(DSLIST).
Enter the data set name pattern:
CZAGENT.CZAPRINT
(or your site-specific naming convention).
Press
Enter
.
Type
B
(Browse) next to the most recent CZAPRINT data set.
Press
Enter
.
Search for messages indicating successful connection to the syslog server:
CZA0070I Connected to server bindplane-host-ip:514
CZA0100I SMF ACF2 statement processed
If the CZAGENT started task is not running, start it:
S CZAGENT
Verify ACF2 log forwarding
Generate test ACF2 security events:
In TSO, attempt to access a data set you do not have permission to access.
Attempt to log on with an invalid password (use a test account).
Execute a TSO command that is logged by ACF2.
Check the Bindplane agent logs to verify receipt of ACF2 syslog messages:
Linux:
sudo
journalctl
-u
observiq-otel-collector
-f
|
grep
ACF2
Windows:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
|
findstr
ACF2
Sign in to the Google SecOps console and verify that ACF2 logs are being ingested:
Go to
Search
>
UDM Search
.
Enter the following query:
metadata.log_type = "CA_ACF2"
Verify that ACF2 security events appear in the search results.
UDM mapping table
Log Field
UDM Mapping
Logic
extensions.auth.mechanism
The authentication mechanism used.
extensions.auth.type
The type of authentication.
sum
metadata.description
A description of the event.
metadata.event_type
The type of event.
event_type, cat
metadata.product_event_type
The product-specific event type.
product_version
metadata.product_version
The version of the product.
terminal
principal.hostname
The hostname associated with the principal.
name
principal.user.user_display_name
The display name of the user.
usrName
principal.user.userid
The user ID.
security_result.action
The action taken by the security system.
security_result.category
The category of the security result.
class
security_result.category_details
Additional details about the security result category.
reason
security_result.severity
The severity level of the security result.
reason
security_result.severity_details
Detailed severity information.
logstr
security_result.summary
A summary of the security result.
job_id
target.application
The application being targeted.
job_group
target.group.group_display_name
The display name of the group.
target.namespace
The namespace of the target.
dsn
target.resource.name
The name of the resource.
vol
target.resource.parent
The parent resource.
res, dsn
target.resource.product_object_id
The product-specific object identifier.
target.resource.resource_type
The type of resource.
name
target.user.user_display_name
The display name of the target user.
usrName
target.user.userid
The user ID of the target user.
product_name
metadata.product_name
The name of the product generating the event.
vendor_name
metadata.vendor_name
The name of the vendor.
Need more help?
Get answers from Community members and Google SecOps professionals.
