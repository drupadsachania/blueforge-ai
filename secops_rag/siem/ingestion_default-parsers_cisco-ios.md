# Collect Cisco IOS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios/  
**Scraped:** 2026-03-05T09:21:34.123614Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco IOS logs
Supported in:
Google secops
SIEM
This document explains how you can ingest Cisco IOS logs to
Google Security Operations using Bindplane. The parser transforms raw syslog
messages into a structured format conforming to the Unified Data Model (UDM).
It first initializes and extracts fields using grok patterns based on common
Cisco IOS syslog formats. Then, it maps the extracted fields to corresponding
UDM fields, categorizes events, and enriches the data with additional context
before finally outputting the structured log, in UDM format.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to the
Cisco IOS
router, switch or server
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
Save the file securely on the system where Bindplane will be installed.
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
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
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
log_type
:
'CISCO_IOS'
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
with the actual Customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on Cisco IOS device
Sign in to the Cisco IOS device using SSH or a console connection.
Enter the following command for privileged mode:
enable
Enter the following command for configuration mode:
conf
t
Enter the following commands to configure syslog:
logging
<bindplane_IP_address>
logging
source-interface
<interface>
Change
<bindplane_IP_address>
to the actual Bindplane Agent IP address.
Change
<interface>
to the actual communication interface.
Enter the following commands to configure the priority level:
logging
trap
information
logging
console
information
Enter the following command to configure the syslog facility:
logging
facility
syslog
Enter the following command to copy the running-config to startup-config:
copy
running-config
startup-config
UDM mapping table
Log field
UDM mapping
Logic
AcsSessionID
network.session_id
Value taken from AcsSessionID field.
AcctRequest-Flags
security_result.summary
Value taken from AcctRequest-Flags field.
AcctRequest-Flags
security_result.action
If AcctRequest-Flags contains
Start
, set to
ALLOW
. If AcctRequest-Flags contains
Stop
, set to
BLOCK
.
AuthenticationIdentityStore
additional.fields.key =
AuthenticationIdentityStore
, value = AuthenticationIdentityStore
Value taken from AuthenticationIdentityStore field.
AuthenticationMethod
additional.fields.key =
AuthenticationMethod
, value = AuthenticationMethod
Value taken from AuthenticationMethod field.
AuthenticationStatus
security_result.summary
Value taken from AuthenticationStatus field.
Authen-Method
security_result.detection_fields.key =
Authen-Method
, value = Authen-Method
Value taken from Authen-Method field.
Authen-Method
extensions.auth.type
If Authen-Method contains
TacacsPlus
, set to
TACACS
.
AVPair_priv-lvl
security_result.detection_fields.key =
AVPair_priv-lvl
, value = AVPair_priv-lvl
Value taken from AVPair_priv-lvl field.
AVPair_start_time
additional.fields.key =
AVPair_start_time
, value = AVPair_start_time
Value taken from AVPair_start_time field.
AVPair_task_id
additional.fields.key =
AVPair_task_id
, value = AVPair_task_id
Value taken from AVPair_task_id field.
AVPair_timezone
additional.fields.key =
AVPair_timezone
, value = AVPair_timezone
Value taken from AVPair_timezone field.
auditid
metadata.product_log_id
Value taken from auditid field.
cisco_facility
Not mapped to the IDM object.
cisco_message
metadata.description
Value taken from cisco_message field.
cisco_mnemonic
security_result.rule_name
Value taken from cisco_mnemonic field.
cisco_severity
security_result.severity
Mapped to different severity levels based on the value: 0: ALERT, 1: CRITICAL, 2: HIGH, 3: ERROR, 4: MEDIUM, 5: LOW, 6: INFORMATIONAL, 7: INFORMATIONAL.
cisco_severity
security_result.severity_details
Mapped to different severity details based on the value: 0:
System unusable
, 1:
Immediate action needed
, 2:
Critical condition
, 3:
Error condition
, 4:
Warning condition
, 5:
Normal but significant condition
, 6:
Informational message only
, 7:
Appears during debugging only
.
cisco_tag
metadata.product_event_type
Value taken from cisco_tag field.
cisco_tag
metadata.event_type
Mapped to different event types based on the value: SYS-6-LOGGINGHOST_STARTSTOP, TRACK-6-STATE, SYS-3-LOGGINGHOST_FAIL, CRYPTO-4-IKMP_NO_SA, HA_EM-3-FMPD_ACTION_NOTRACK, HA_EM-3-FMPD_ERROR: GENERIC_EVENT; IPSEC-3-REPLAY_ERROR, CRYPTO-4-RECVD_PKT_INV_SPI, IPSEC-3-HMAC_ERROR, FW-6-DROP_PKT, SEC-6-IPACCESSLOGP: NETWORK_UNCATEGORIZED; CRYPTO-4-IKMP_BAD_MESSAGE, CRYPTO-6-IKMP_NOT_ENCRYPTED, CRYPTO-6-IKMP_MODE_FAILURE: STATUS_UNCATEGORIZED; SYS-5-CONFIG_I: USER_UNCATEGORIZED.
ClientLatency
additional.fields.key =
ClientLatency
, value = ClientLatency
Value taken from ClientLatency field.
CmdSet
additional.fields.key =
CmdSet
, value = CmdSet
Value taken from CmdSet field.
command
principal.process.command_line
Value taken from command field.
CPMSessionID
additional.fields.key =
CPMSessionID
, value = CPMSessionID
Value taken from CPMSessionID field.
description
metadata.description
Value taken from description field.
DestinationIPAddress
target.asset.ip
Value taken from DestinationIPAddress field.
DestinationIPAddress
target.ip
Value taken from DestinationIPAddress field.
DestinationPort
target.port
Value taken from DestinationPort field.
Device_IP_Address
principal.asset.ip
Value taken from Device_IP_Address field.
Device_IP_Address
principal.ip
Value taken from Device_IP_Address field.
Device_Type
additional.fields.key =
Device_Type
, value = Device_Type
Value taken from Device_Type field.
dst_ip
target.asset.ip
Value taken from dst_ip field.
dst_ip
target.ip
Value taken from dst_ip field.
dst_port
target.port
Value taken from dst_port field.
dst_user
target.user.userid
Value taken from dst_user field.
EnableFlag
security_result.detection_fields.key =
EnableFlag
, value = EnableFlag
Value taken from EnableFlag field.
IdentityGroup
additional.fields.key =
IdentityGroup
, value = IdentityGroup
Value taken from IdentityGroup field.
IdentitySelectionMatchedRule
security_result.detection_fields.key =
IdentitySelectionMatchedRule
, value = IdentitySelectionMatchedRule
Value taken from IdentitySelectionMatchedRule field.
intermediary_host
intermediary.hostname
Value taken from intermediary_host field.
intermediary_ip
intermediary.ip
Value taken from intermediary_ip field.
IPSEC
additional.fields.key =
IPSEC
, value = IPSEC
Value taken from IPSEC field.
ISEPolicySetName
extensions.auth.type
If ISEPolicySetName contains
Tacacs
, set to
TACACS
.
IsMachineAuthentication
additional.fields.key =
IsMachineAuthentication
, value = IsMachineAuthentication
Value taken from IsMachineAuthentication field.
IsMachineIdentity
security_result.detection_fields.key =
IsMachineIdentity
, value = IsMachineIdentity
Value taken from IsMachineIdentity field.
Location
additional.fields.key =
Location
, value = Location
Value taken from Location field.
MatchedCommandSet
additional.fields.key =
MatchedCommandSet
, value = MatchedCommandSet
Value taken from MatchedCommandSet field.
message
Not mapped to the IDM object.
metadata_event_type
metadata.event_type
Value taken from metadata_event_type field. If empty or
GENERIC_EVENT
, set to NETWORK_UNCATEGORIZED if principal_mid_present and target_mid_present are true, USER_UNCATEGORIZED if principal_userid_present is true, STATUS_UPDATE if principal_mid_present is true, or GENERIC_EVENT otherwise. If Service contains
Login
, set to USER_LOGIN if principal_userid_present, principal_mid_present, and target_mid_present are true, or USER_UNCATEGORIZED if principal_userid_present is true.
Model_Name
additional.fields.key =
Model_Name
, value = Model_Name
Value taken from Model_Name field.
Name
additional.fields.key =
Name
, value = Name
Value taken from Name field.
Network_Device_Profile
additional.fields.key =
Network_Device_Profile
, value = Network_Device_Profile
Value taken from Network_Device_Profile field.
NetworkDeviceGroups
additional.fields.key =
NetworkDeviceGroups
, value = NetworkDeviceGroups
Value taken from NetworkDeviceGroups field.
NetworkDeviceName
principal.asset.hostname
Value taken from NetworkDeviceName field.
NetworkDeviceName
principal.hostname
Value taken from NetworkDeviceName field.
NetworkDeviceProfileId
principal.resource.product_object_id
Value taken from NetworkDeviceProfileId field.
pid
principal.process.pid
Value taken from pid field.
Port
principal.resource.attribute.labels.key =
Port
, value = Port
Value taken from Port field.
Privilege-Level
security_result.detection_fields.key =
Privilege-Level
, value = Privilege-Level
Value taken from Privilege-Level field.
product_event_type
metadata.product_event_type
Value taken from product_event_type field.
Protocol
additional.fields.key =
Protocol
, value = Protocol
Value taken from Protocol field.
protocol
network.application_protocol
If protocol is
HTTPS
, set to
HTTPS
.
protocol
network.ip_protocol
If protocol is
TCP
or
UDP
, set to the uppercase value of protocol.
reason
security_result.summary
Value taken from reason field.
region
principal.location.country_or_region
Value taken from region field.
Remote-Address
target.asset.ip
Value taken from Remote-Address field after validating it as an IP address.
Remote-Address
target.ip
Value taken from Remote-Address field after validating it as an IP address.
RequestLatency
security_result.detection_fields.key =
RequestLatency
, value = RequestLatency
Value taken from RequestLatency field.
Response
additional.fields.key =
Response
, value = Response
Value taken from Response field.
SelectedAccessService
security_result.action_details
Value taken from SelectedAccessService field.
SelectedAuthenticationIdentityStores
security_result.detection_fields.key =
SelectedAuthenticationIdentityStores
, value = SelectedAuthenticationIdentityStores
Value taken from SelectedAuthenticationIdentityStores field.
SelectedCommandSet
additional.fields.key =
SelectedCommandSet
, value = SelectedCommandSet
Value taken from SelectedCommandSet field.
Service
additional.fields.key =
Service
, value = Service
Value taken from Service field.
Service-Argument
additional.fields.key =
Service-Argument
, value = Service-Argument
Value taken from Service-Argument field.
severity
security_result.severity
If severity contains
Notice
, set to INFORMATIONAL.
Software_Version
additional.fields.key =
Software_Version
, value = Software_Version
Value taken from Software_Version field.
source_facility
principal.asset.hostname
Value taken from source_facility field.
source_facility
principal.hostname
Value taken from source_facility field.
src_ip
principal.asset.ip
Value taken from src_ip field.
src_ip
principal.ip
Value taken from src_ip field.
src_mac
principal.mac
Value taken from src_mac field after replacing
.
with
:
.
src_port
principal.port
Value taken from src_port field.
src_user_id
principal.user.userid
Value taken from src_user_id field. If empty, take value from User field. If still empty, take value from StepData_9 field.
src_user_name
principal.user.user_display_name
Value taken from src_user_name field.
Step
additional.fields.key =
Step
, value = Step
Value taken from Step field.
StepData_10
principal.asset.hostname
Value taken from StepData_10 field.
StepData_10
principal.hostname
Value taken from StepData_10 field.
StepData_13
security_result.summary
Value taken from StepData_13 field.
StepData_14
security_result.detection_fields.key =
StepData_14
, value = StepData_14
Value taken from StepData_14 field.
StepData_15
security_result.detection_fields.key =
StepData_15
, value = StepData_15
Value taken from StepData_15 field.
StepData_20
security_result.detection_fields.key =
StepData_20
, value = StepData_20
Value taken from StepData_20 field.
StepData_21
security_result.detection_fields.key =
StepData_21
, value = StepData_21
Value taken from StepData_21 field.
StepData_3
additional.fields.key =
StepData_3
, value = StepData_3
Value taken from StepData_3 field.
StepData_4
security_result.detection_fields.key =
StepData_4
, value = StepData_4
Value taken from StepData_4 field.
StepData_6
security_result.detection_fields.key =
StepData_6
, value = StepData_6
Value taken from StepData_6 field.
StepData_7
security_result.detection_fields.key =
StepData_7
, value = StepData_7
Value taken from StepData_7 field.
StepData_8
security_result.detection_fields.key =
StepData_8
, value = StepData_8
Value taken from StepData_8 field.
StepData_9
principal.user.userid
Value taken from StepData_9 field if src_user_id and User fields are empty.
target_host
target.asset.hostname
Value taken from target_host field.
target_host
target.hostname
Value taken from target_host field.
timestamp
metadata.event_timestamp
Value taken from timestamp field after removing extra spaces and parsing the date.
TotalAuthenLatency
additional.fields.key =
TotalAuthenLatency
, value = TotalAuthenLatency
Value taken from TotalAuthenLatency field.
ts
metadata.event_timestamp
Value taken from ts field after parsing the date.
Type
security_result.category_details
Value taken from Type field.
User
principal.user.userid
Value taken from User field if src_user_id is empty.
UserType
additional.fields.key =
UserType
, value = UserType
Value taken from UserType field.
metadata.vendor_name
Set to
CISCO
.
metadata.product_name
Set to
CISCO_IOS
.
metadata.log_type
Set to
CISCO_IOS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
