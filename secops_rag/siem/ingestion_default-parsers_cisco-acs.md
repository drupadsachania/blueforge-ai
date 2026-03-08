# Collect Cisco Secure ACS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-acs/  
**Scraped:** 2026-03-05T09:21:42.327554Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco Secure ACS logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cisco Secure ACS logs to Google Security Operations using Bindplane.
The parser extracts fields from Cisco Secure ACS syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Cisco Secure ACS web interface
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the system where Bindplane will be installed.
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
chronicle/chronicle_w_labels
:
compression
:
gzip
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
'YOUR_CUSTOMER_ID'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'CISCO_ACS'
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
Configuration parameters
Replace the following placeholders:
Receiver configuration:
udplog
: Use
udplog
for UDP syslog or
tcplog
for TCP syslog
0.0.0.0
: IP address to listen on (
0.0.0.0
to listen on all interfaces)
514
: Port number to listen on (standard syslog port)
Exporter configuration:
creds_file_path
: Full path to ingestion authentication file:
Linux
:
/etc/bindplane-agent/ingestion-auth.json
Windows
:
C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json
YOUR_CUSTOMER_ID
: Customer ID from the Get customer ID section
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
: Log type exactly as it appears in Chronicle (
CISCO_ACS
)
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
To restart the Bindplane agent in Linux, run the following command:
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
To restart the Bindplane agent in Windows, choose one of the following options:
Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Services console:
Press
Win+R
, type
services.msc
, and press
Enter
.
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
Configure Syslog forwarding on Cisco Secure ACS
Sign in to the
Cisco Secure ACS
web interface.
Go to
System Administration
>
Configuration
>
Log Configuration
>
Remote Log Targets
.
Click
Create
to add a new remote log target.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google-SecOps-Bindplane
).
Description
: Enter a description (optional).
IP Address
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Facility Code
: Select
LOCAL6
(or your preferred facility).
Click
Submit
.
Go to
System Administration
>
Configuration
>
Log Configuration
>
Logging Categories
.
Select the log categories to forward:
AAA Audit
AAA Diagnostics
Administrative and Operational Audit
System Diagnostics
For each selected category, click the category name.
Go to the
Remote Log Target
tab.
Move the created remote log target (for example,
Google-SecOps-Bindplane
) from
Available
to
Selected
.
Click
Save
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
Acct-Authentic
additional.fields[].value.string_value
Value is taken from the Acct-Authentic field.
Acct-Delay-Time
additional.fields[].value.string_value
Value is taken from the Acct-Delay-Time field.
Acct-Input-Octets
additional.fields[].value.string_value
Value is taken from the Acct-Input-Octets field.
Acct-Input-Packets
additional.fields[].value.string_value
Value is taken from the Acct-Input-Packets field.
Acct-Output-Octets
additional.fields[].value.string_value
Value is taken from the Acct-Output-Octets field.
Acct-Output-Packets
additional.fields[].value.string_value
Value is taken from the Acct-Output-Packets field.
Acct-Session-Id
additional.fields[].value.string_value
Value is taken from the Acct-Session-Id field.
Acct-Session-Time
additional.fields[].value.string_value
Value is taken from the Acct-Session-Time field.
Acct-Status-Type
additional.fields[].value.string_value
Value is taken from the Acct-Status-Type field.
Acct-Terminate-Cause
additional.fields[].value.string_value
Value is taken from the Acct-Terminate-Cause field.
ACSVersion
additional.fields[].value.string_value
Value is taken from the ACSVersion field.
AD-Domain
principal.group.group_display_name
Value is taken from the AD-Domain field.
AD-IP-Address
principal.ip
Value is taken from the AD-IP-Address field.
Called-Station-ID
additional.fields[].value.string_value
Value is taken from the Called-Station-ID field.
Calling-Station-ID
additional.fields[].value.string_value
Value is taken from the Calling-Station-ID field.
Class
additional.fields[].value.string_value
Value is taken from the Class field.
CmdSet
(not mapped)
Not mapped to the IDM object.
ConfigVersionId
additional.fields[].value.number_value
Value is taken from the ConfigVersionId field and converted to a float.
DestinationIPAddress
target.ip, intermediary.ip
Value is taken from the DestinationIPAddress field. intermediary.ip is derived from Device IP Address.
DestinationPort
target.port
Value is taken from the DestinationPort field and converted to an integer.
Device IP Address
intermediary.ip
Value is taken from the Device IP Address field.
Device Port
intermediary.port
Value is taken from the Device Port field and converted to an integer.
DetailedInfo
security_result.summary, security_result.description, security_result.action
If DetailedInfo is "Authentication succeed", security_result.summary is "successful login occurred" and security_result.action is ALLOW. If DetailedInfo contains "Invalid username or password specified", security_result.summary is "failed login occurred" and security_result.action is BLOCK. security_result.description is derived from log_header.
Framed-IP-Address
principal.ip
Value is taken from the Framed-IP-Address field.
Framed-Protocol
additional.fields[].value.string_value
Value is taken from the Framed-Protocol field.
NAS-IP-Address
target.ip
Value is taken from the NAS-IP-Address field.
NAS-Port
additional.fields[].value.string_value
Value is taken from the NAS-Port field.
NAS-Port-Id
target.port
Value is taken from the NAS-Port-Id field and converted to an integer.
NAS-Port-Type
additional.fields[].value.string_value
Value is taken from the NAS-Port-Type field.
NetworkDeviceName
target.hostname
Value is taken from the NetworkDeviceName field.
Protocol
additional.fields[].value.string_value
Value is taken from the Protocol field.
RadiusPacketType
(not mapped)
Not mapped to the IDM object.
Remote-Address
principal.ip, target.ip
Value is taken from the Remote-Address field and parsed as an IP address. It is mapped to principal.ip for authentication events and target.ip for accounting and diagnostic events.
RequestLatency
additional.fields[].value.string_value
Value is taken from the RequestLatency field.
Response
principal.user.userid
If Response contains "User-Name", the username is extracted and mapped to principal.user.userid.
SelectedAccessService
additional.fields[].value.string_value
Value is taken from the SelectedAccessService field.
SelectedAuthenticationIdentityStores
security_result.detection_fields[].value
Value is taken from the SelectedAuthenticationIdentityStores field.
SelectedAuthorizationProfiles
security_result.detection_fields[].value
Value is taken from the SelectedAuthorizationProfiles field.
Service-Type
additional.fields[].value.string_value
Value is taken from the Service-Type field.
Tunnel-Client-Endpoint
additional.fields[].value.string_value
Value is taken from the Tunnel-Client-Endpoint field and parsed as an IP address.
User
target.user.userid
Value is taken from the User field.
UserName
target.user.userid, principal.mac
If UserName is a MAC address, it is parsed and mapped to principal.mac. Otherwise, it is mapped to target.user.userid.
ac-user-agent
network.http.user_agent
Value is taken from the ac-user-agent field.
cat
metadata.description
Value is taken from the cat field.
device-mac
principal.mac
Value is taken from the device-mac field, colons are added, and the value is converted to lowercase. If device-mac is "00", it is replaced with "00:00:00:00:00:00".
device-platform
principal.asset.platform_software.platform
If device-platform is "win", the value "WINDOWS" is assigned to principal.asset.platform_software.platform.
device-platform-version
principal.asset.platform_software.platform_version
Value is taken from the device-platform-version field.
device-public-mac
principal.mac
Value is taken from the device-public-mac field, hyphens are replaced with colons, and the value is converted to lowercase.
device-type
principal.asset.hardware.model
Value is taken from the device-type field.
device-uid
principal.asset.asset_id
Value is taken from the device-uid field and prepended with "ASSET ID: ".
device-uid-global
principal.asset.product_object_id
Value is taken from the device-uid-global field.
hostname
principal.hostname
Value is taken from the hostname field.
ip:source-ip
principal.ip
Value is taken from the ip:source-ip field.
kv.ADDomain
(not mapped)
Not mapped to the IDM object.
kv.Airespace-Wlan-Id
(not mapped)
Not mapped to the IDM object.
kv.AuthenticationIdentityStore
(not mapped)
Not mapped to the IDM object.
kv.AVPair
(not mapped)
Not mapped to the IDM object.
kv.CVPN3000/ASA/PIX7.x-DAP-Tunnel-Group-Name
(not mapped)
Not mapped to the IDM object.
kv.CVPN3000/ASA/PIX7.x-Group-Based-Address-Pools
(not mapped)
Not mapped to the IDM object.
kv.ExternalGroups
(not mapped)
Not mapped to the IDM object.
kv.FailureReason
(not mapped)
Not mapped to the IDM object.
kv.IdentityAccessRestricted
(not mapped)
Not mapped to the IDM object.
kv.IdentityGroup
(not mapped)
Not mapped to the IDM object.
kv.NAS-Identifier
(not mapped)
Not mapped to the IDM object.
kv.SelectedShellProfile
(not mapped)
Not mapped to the IDM object.
kv.ServiceSelectionMatchedRule
(not mapped)
Not mapped to the IDM object.
kv.State
(not mapped)
Not mapped to the IDM object.
kv.Step
(not mapped)
Not mapped to the IDM object.
kv.Tunnel-Medium-Type
(not mapped)
Not mapped to the IDM object.
kv.Tunnel-Private-Group-ID
(not mapped)
Not mapped to the IDM object.
kv.Tunnel-Type
(not mapped)
Not mapped to the IDM object.
kv.UseCase
(not mapped)
Not mapped to the IDM object.
kv.UserIdentityGroup
(not mapped)
Not mapped to the IDM object.
kv.VendorSpecific
(not mapped)
Not mapped to the IDM object.
kv.attribute-131
(not mapped)
Not mapped to the IDM object.
kv.attribute-89
(not mapped)
Not mapped to the IDM object.
kv.cisco-av-pair
(not mapped)
Not mapped to the IDM object.
kv.cisco-av-pair:CiscoSecure-Group-Id
(not mapped)
Not mapped to the IDM object.
leef_version
(not mapped)
Not mapped to the IDM object.
log_header
metadata.description
Value is taken from the log_header field.
log_id
metadata.product_log_id
Value is taken from the log_id field.
log_type
metadata.product_event_type
Value is taken from the log_type field.
message_severity
(not mapped)
Not mapped to the IDM object.
product
metadata.product_name
Value is taken from the product field.
product_version
metadata.product_version
Value is taken from the product_version field.
server_host
target.hostname
Value is taken from the server_host field.
timestamp
metadata.event_timestamp
Value is taken from the timestamp field and the timezone field (after removing the colon). The combined value is parsed as a timestamp.
url
network.dns.questions[].name
Value is taken from the url field.
vendor
metadata.vendor_name
Value is taken from the vendor field. Set to "GENERIC_EVENT" initially, then potentially overwritten based on the log_type and parsed fields. Can be "USER_LOGIN", "USER_UNCATEGORIZED", "NETWORK_DNS", "NETWORK_CONNECTION", "STATUS_UPDATE", or "STATUS_UNCATEGORIZED". Set to "Cisco" initially, then potentially overwritten by the vendor field. Set to "ACS" initially, then potentially overwritten by the product field. Set to "CISCO_ACS". Set to "USERNAME_PASSWORD". Set to "TACACS". Set to "UDP" for RADIUS accounting and diagnostic events. Set to "DNS" for DNS events. Derived from the security_action field, which is set based on whether the login was successful or not. Set to "successful login occurred" for successful logins and "failed login occurred" for failed logins. May also be set to "passed" for certain identity store diagnostic events. Set to "LOW" for failed login attempts. Constructed by prepending "ASSET ID: " to the device-uid field.
Need more help?
Get answers from Community members and Google SecOps professionals.
