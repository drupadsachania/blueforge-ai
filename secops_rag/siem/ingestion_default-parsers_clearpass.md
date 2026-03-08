# Collect Aruba ClearPass logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clearpass/  
**Scraped:** 2026-03-05T09:19:11.743909Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Aruba ClearPass logs
Supported in:
Google secops
SIEM
This document explains how to collect Aruba ClearPass logs by using Bindplane. The parser attempts to cleanse and structure the incoming logs by removing extraneous fields and standardizing the message format. Then, depending on whether the log follows the CEF format or a different structure, the code uses a combination of grok patterns, key-value extractions, and conditional logic to map relevant fields to the unified data model (UDM), ultimately categorizing each event into a specific security event type.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to an Aruba ClearPass.
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
CLEARPASS
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
Configure Aruba ClearPass syslog server
Sign in to the
ClearPass Policy Manager
console.
Select
Administration
>
External servers
>
Syslog targets
.
Click
Add
.
In the
Add syslog target
window that appears, specify the following details:
Host address
: enter the Bindplane IP address.
Server port
: enter the Bindplane port number.
Protocol
: select
UDP
(you can also select
TCP
, depending on your Bindplane configuration).
Click
Save
.
Configure syslog export filters
Go to
Administration
>
External servers
>
Syslog export filters
.
Click
Add
.
In the
Add Syslog Filters
window that appears, specify the following in the
General
tab:
Name
: enter the syslog export filter name based on the table in
Export template items
.
Export template
: select the appropriate export template based on the table in
Export template items
.
Export event format type
: select
Standard
.
Syslog servers
: select the Bindplane IP address.
In the
Export template
list, when you select the
Session
or
Insight
export templates, the
Filter and columns
tab is enabled. Complete the following steps:
Click the
Filter and columns
tab.
Data filter
: make sure the default value
All requests
is selected.
Column selection
: select the predefined field group based on the table in
Export template items
.
Selected columns
: verify that the automatically populated fields match the table in
Export template items
.
Click the
Summary
tab.
Click
Save
.
In the
Export template
list, when you select the
System events
and
Audit records
export templates, the
Filter and columns
tab is not enabled. Proceed to the
Summary
tab and click
Save
.
Repeat steps to add syslog export filters for all
Session
,
Insight
,
Audit records
and
System events
export templates based on the details from the table in
Summary of export template items
.
Export template items
The following table describes the items that you need to configure for each export template.
The default fields that are listed in Selected Columns are supported for event parsing.
Ensure all fields that are mentioned in the table under Selected columns (default) are present and in the same order. Make sure to create syslog export filter templates exactly as provided in table, including the case-sensitive name of the filter.
Syslog export filter name (case sensitive)
Export template
Predefined field groups
Selected columns (default)
ACPPM_radauth
Insight Logs
Radius Authentications
Auth.Username
Auth.Host-MAC-Address
Auth.Protocol
Auth.NAS-IP-Address
CppmNode.CPPM-Node
Auth.Login-Status
Auth.Service
Auth.Source
Auth.Roles
Auth.Enforcement-Profiles
ACPPM_radfailedauth
Insight Logs
Radius Failed Authentications
Auth.Username
Auth.Host-MAC-Address
Auth.NAS-IP-Address
CppmNode.CPPM-Node
Auth.Service
CppmErrorCode.Error-Code-Details
CppmAlert.Alerts
ACPPM_radacct
Insight Logs
RADIUS Accounting
Radius.Username
Radius.Calling-Station-Id
Radius.Framed-IP-Address
Radius.NAS-IP-Address
Radius.Start-Time
Radius.End-Time
Radius.Duration
Radius.Input-bytes
Radius.Output-bytes
ACPPM_tacauth
Insight Logs
tacacs Authentication
tacacs.Username
tacacs.Remote-Address
tacacs.Request-Type
tacacs.NAS-IP-Address
tacacs.Service
tacacs.Auth-Source
tacacs.Roles
tacacs.Enforcement-Profiles
tacacs.Privilege-Level
ACPPM_tacfailedauth
Insight Logs
tacacs Failed Authentication
tacacs.Username
tacacs.Remote-Address
tacacs.Request-Type
tacacs.NAS-IP-Address
tacacs.Service
CppmErrorCode.Error-Code-Details
CppmAlert.Alerts
ACPPM_webauth
Insight Logs
WEBAUTH
Auth.Username
Auth.Host-MAC-Address
Auth.Host-IP-Address
Auth.Protocol
Auth.System-Posture-Token
CppmNode.CPPM-Node
Auth.Login-Status
Auth.Service
Auth.Source
Auth.Roles
Auth.Enforcement-Profiles
ACPPM_webfailedauth
Insight Logs
WEBAUTH Failed Authentications
Auth.Username
Auth.Host-MAC-Address
Auth.Host-IP-Address
Auth.Protocol
Auth.System-Posture-Token
CppmNode.CPPM-Node
Auth.Login-Status
Auth.Service
CppmErrorCode.Error-Code-Details
CppmAlert.Alerts
ACPPM_appauth
Insight Logs
Application Authentication
Auth.Username
Auth.Host-IP-Address
Auth.Protocol
CppmNode.CPPM-Node
Auth.Login-Status
Auth.Service
Auth.Source
Auth.Roles
Auth.Enforcement-Profiles
ACPPM_failedappauth
Insight Logs
Failed Application Authentication
Auth.Username
Auth.Host-IP-Address
Auth.Protocol
CppmNode.CPPM-Node
Auth.Login-Status
Auth.Service
CppmErrorCode.Error-Code-Details
CppmAlert.Alerts
ACPPM_endpoints
Insight Logs
Endpoints
Endpoint.MAC-Address
Endpoint.MAC-Vendor
Endpoint.IP-Address
Endpoint.Username
Endpoint.Device-Category
Endpoint.Device-Family
Endpoint.Device-Name
Endpoint.Conflict
Endpoint.Status
Endpoint.Added-At
Endpoint.Updated-At
ACPPM_cpguest
Insight Logs
Clearpass Guest
Guest.Username
Guest.MAC-Address
Guest.Visitor-Name
Guest.Visitor-Company
Guest.Role-Name
Guest.Enabled
Guest.Created-At
Guest.Starts-At
Guest.Expires-At
ACPPM_onbenroll
Insight Logs
Onboard Enrollment
OnboardEnrollment.Username
OnboardEnrollment.Device-Name
OnboardEnrollment.MAC-Address
OnboardEnrollment.Device-Product
OnboardEnrollment.Device-Version
OnboardEnrollment.Added-At
OnboardEnrollment.Updated-At
ACPPM_onbcert
Insight Logs
Onboard Certificate
OnboardCert.Username
OnboardCert.Mac-Address
OnboardCert.Subject
OnboardCert.Issuer
OnboardCert.Valid-From
OnboardCert.Valid-To
OnboardCert.Revoked-At
ACPPM_onboscp
Insight Logs
Onboard OCSP
OnboardOCSP.Remote-Address
OnboardOCSP.Response-Status-Name
OnboardOCSP.Timestamp
ACPPM_cpsysevent
Insight Logs
Clearpass System Events
CppmNode.CPPM-Node
CppmSystemEvent.Source
CppmSystemEvent.Level
CppmSystemEvent.Category
CppmSystemEvent.Action
CppmSystemEvent.Timestamp
ACPPM_cpconfaudit
Insight Logs
Clearpass Configuration Audit
CppmConfigAudit.Name
CppmConfigAudit.Action
CppmConfigAudit.Category
CppmConfigAudit.Updated-By
CppmConfigAudit.Updated-At
ACPPM_possummary
Insight Logs
Posture Summary
Endpoint.MAC-Address
Endpoint.IP-Address
Endpoint.Hostname
Endpoint.Usermame
Endpoint.System-Agent-Type
Endpoint.System-Agent-Version
Endpoint.System-Client-OS
Endpoint.System-Posture-Token
Endpoint.Posture-Healthy
Endpoint.Posture-Unhealthy
ACPPM_posfwsummary
Insight Logs
Posture Firewall Summary
Endpoint.MAC-Address
Endpoint.IP-Address
Endpoint.Hostname
Endpoint.Usermame
Endpoint.System-Agent-Type
Endpoint.System-Agent-Version
Endpoint.System-Client-OS
Endpoint.System-Posture-Token
Endpoint.Firewall-APT
Endpoint.Firewall-Input
Endpoint.Firewall-Output
ACPPM_poavsummary
Insight Logs
Posture Antivirus Summary
Endpoint.MAC-Address
Endpoint.IP-Address
Endpoint.Hostname
Endpoint.Usermame
Endpoint.System-Agent-Type
Endpoint.System-Agent-Version
Endpoint.System-Client-OS
Endpoint.System-Posture-Token
Endpoint.Antivirus-APT
Endpoint.Antivirus-Input
Endpoint.Antivirus-Output
ACPPM_posassummary
Insight Logs
Posture Antispyware Summary
Endpoint.MAC-Address
Endpoint.IP-Address
Endpoint.Hostname
Endpoint.Usermame
Endpoint.System-Agent-Type
Endpoint.System-Agent-Version
Endpoint.System-Client-OS
Endpoint.System-Posture-Token
Endpoint.Antispyware-APT
Endpoint.Antispyware-Input
Endpoint.Antispyware-Output
ACPPM_posdskencrpsummary
Insight Logs
Posture DiskEncryption Summary
Endpoint.MAC-Address
Endpoint.IP-Address
Endpoint.Hostname
Endpoint.Usermame
Endpoint.System-Agent-Type
Endpoint.System-Agent-Version
Endpoint.System-Client-OS
Endpoint.System-Posture-Token
Endpoint.DiskEncryption-APT
Endpoint.DiskEncryption-Input
Endpoint.DiskEncryption-Output
ACPPM_loggedusers
Session Logs
Logged in Users
Common.Username
Common.Service
Common.Roles
Common.Host-MAC-Address
RADIUS.Acct-Framed-IP-Address
Common.NAS-IP-Address
Common.Request-Timestamp
ACPPM_failedauth
Session Logs
Failed Authentications
Common.Username
Common.Service
Common.Roles
RADIUS.Auth-Source
RADIUS.Auth-Method
Common.System-Posture-Token
Common.Enforcement-Profiles
Common.Host-MAC-Address
Common.NAS-IP-Address
Common.Error-Code
Common.Alerts
Common.Request-Timestamp
ACPPM_radacctsession
Session Logs
RADIUS Accounting
RADIUS.Acct-Username
RADIUS.Acct-NAS-IP-Address
RADIUS.Acct-NAS-Port
RADIUS.Acct-NAS-Port-Type
RADIUS.Acct-Calling-Station-Id
RADIUS.Acct-Framed-IP-Address
RADIUS.Acct-Session-Id
RADIUS.Acct-Session-Time
RADIUS.Acct-Output-Pkts
RADIUS.Acct-Input-Pkts
RADIUS.Acct-Output-Octets
RADIUS.Acct-Input.Octets
RADIUS.Acct-Service-Name
RADIUS.Acct-Timestamp
ACPPM_tacadmin
Session Logs
tacacs+ Administration
Common.Username
Common.Service
tacacs.Remote-Address
tacacs.Privilege.Level
Common.Request-Timestamp
ACPPM_tacacct
Session Logs
tacacs+ Accounting
Common.Username
Common.Service
tacacs.Remote-Address
tacacs.Acct-Flags
tacacs.Privilege.Level
Common.Request-Timestamp
ACPPM_webauthsession
Session Logs
Web Authentication
Common.Username
Common.Host-MAC-Address
WEBAUTH.Host-IP-Address
Common.Roles
Common.System-Posture-Token
Common.Enforcement-Profiles
Common.Request-Timestamp
ACPPM_guestacc
Session Logs
Guest Access
Common.Username
RADIUS.Auth-Method
Common.Host-MAC-Address
Common.Roles
Common.System-Posture-Token
Common.Enforcement-Profiles
Common.Request-Timestamp
ACPPM_auditrecords
Audit Records
Not Applicable
Not Applicable
ACPPM_systemevents
System Events
Not Applicable
Not Applicable
UDM Mapping Table
Log field
UDM mapping
Logic
Action
security_result.action
Value is mapped from 'Action' field if its value is 'ALLOW' or 'BLOCK'
Auth.Enforcement-Profiles
security_result.detection_fields.value
Value is mapped from 'Auth.Enforcement-Profiles' field
Auth.Host-MAC-Address
principal.mac
Value is mapped from 'Auth.Host-MAC-Address' field after converting it to colon-separated MAC address format
Auth.Login-Status
security_result.detection_fields.value
Value is mapped from 'Auth.Login-Status' field
Auth.NAS-IP-Address
target.ip
Value is mapped from 'Auth.NAS-IP-Address' field
Auth.Protocol
intermediary.application
Value is mapped from 'Auth.Protocol' field
Auth.Service
security_result.detection_fields.value
Value is mapped from 'Auth.Service' field
Auth.Source
principal.hostname
Value is mapped from 'Auth.Source' field after removing any leading alphanumeric characters and spaces
Auth.Username
principal.user.user_display_name
Value is mapped from 'Auth.Username' field
Category
metadata.event_type
If value is 'Logged in', UDM field is set to 'USER_LOGIN'. If value is 'Logged out', UDM field is set to 'USER_LOGOUT'
Common.Alerts
security_result.description
Value is mapped from 'Common.Alerts' field
Common.Enforcement-Profiles
security_result.detection_fields.value
Value is mapped from 'Common.Enforcement-Profiles' field
Common.Login-Status
security_result.detection_fields.value
Value is mapped from 'Common.Login-Status' field
Common.NAS-IP-Address
target.ip
Value is mapped from 'Common.NAS-IP-Address' field
Common.Roles
principal.user.group_identifiers
Value is mapped from 'Common.Roles' field
Common.Service
security_result.detection_fields.value
Value is mapped from 'Common.Service' field
Common.Username
principal.user.userid
Value is mapped from 'Common.Username' field
Component
intermediary.application
Value is mapped from 'Component' field
Description
metadata.description
Value is mapped from 'Description' field after replacing newline characters with pipe symbol. If 'Description' field contains 'User', 'Address', and 'Role', then it is parsed as key-value pairs and mapped to corresponding UDM fields. If 'Description' field contains 'Unable connection with', then the target hostname is extracted and mapped to 'target.hostname'
EntityName
principal.hostname
Value is mapped from 'EntityName' field
InterIP
target.ip
Value is mapped from 'InterIP' field
Level
security_result.severity
If value is 'ERROR' or 'FATAL', UDM field is set to 'HIGH'. If value is 'WARN', UDM field is set to 'MEDIUM'. If value is 'INFO' or 'DEBUG', UDM field is set to 'LOW'
LogNumber
metadata.product_log_id
Value is mapped from 'LogNumber' field
RADIUS.Acct-Framed-IP-Address
principal.ip
Value is mapped from 'RADIUS.Acct-Framed-IP-Address' field
Timestamp
metadata.event_timestamp
Value is mapped from 'Timestamp' field after converting it to UTC and parsing it as a timestamp
User
principal.user.userid
Value is mapped from 'User' field
agent_ip
principal.ip, principal.asset.ip
Value is mapped from 'agent_ip' field
community
additional.fields.value.string_value
Value is mapped from 'community' field
descr
metadata.description
Value is mapped from 'descr' field
enterprise
additional.fields.value.string_value
Value is mapped from 'enterprise' field
eventDescription
metadata.description
Value is mapped from 'eventDescription' field after removing quotes
generic_num
additional.fields.value.string_value
Value is mapped from 'generic_num' field
prin_mac
principal.mac
Value is mapped from 'prin_mac' field after converting it to colon-separated MAC address format
prin_port
principal.port
Value is mapped from 'prin_port' field and converted to integer
specificTrap_name
additional.fields.value.string_value
Value is mapped from 'specificTrap_name' field
specificTrap_num
additional.fields.value.string_value
Value is mapped from 'specificTrap_num' field
uptime
additional.fields.value.string_value
Value is mapped from 'uptime' field
version
metadata.product_version
Value is mapped from 'version' field
extensions.auth.type
Value is set to 'SSO'
metadata.event_type
Value is determined based on various log fields and parser logic. See parser code for details
metadata.log_type
Value is set to 'CLEARPASS'
metadata.product_name
Value is set to 'ClearPass'
metadata.vendor_name
Value is set to 'ArubaNetworks'
Need more help?
Get answers from Community members and Google SecOps professionals.
