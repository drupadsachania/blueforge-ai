# Collect Veridium ID logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veridium-id/  
**Scraped:** 2026-03-05T10:02:05.230702Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Veridium ID logs
Supported in:
Google secops
SIEM
This document explains how to ingest Veridium ID logs to Google Security Operations using Bindplane. The parser first extracts fields from syslog messages and categorizes them based on the "log_identifier". Then, it uses conditional logic and key-value parsing to map the extracted fields into a unified data model (UDM) structure, handling both
ActionLog
and
EventLog
formats.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to Veridium ID
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
'VERIDIUM_ID'
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
Configure Syslog for Veridium ID
Sign in to
Veridium ID
host using SSH or CLI.
Edit the
/etc/rsyslog.conf
or
/etc/rsyslog.d/events.conf
file using VI.
vi
/etc/rsyslog.conf
Enter the following details, replacing
<bindplane-ip>
and
<bindplane-port>
with the actual Bindplane agent details.
module
(
load
=
"imfile"
PollingInterval
=
"10"
)
input
(
type
=
"imfile"
File
=
"/var/log/veridiumid/websecadmin/events.log"
Tag
=
"ver-adminevents"
reopenOnTruncate
=
"on"
)
input
(
type
=
"imfile"
File
=
"/var/log/veridiumid/tomcat/events.log"
Tag
=
"ver-events"
reopenOnTruncate
=
"on"
)
if
$programname
==
'ver-events'
then
@@<bindplane-ip>:<bindplane-port>
if
$programname
==
'ver-adminevents'
then
@@<bindplane-ip>:<bindplane-port>
Save the file and exit VI.
UDM Mapping Table
Log Field
UDM Mapping
Logic
_caller.accountId
principal.user.userid
Directly mapped from the
_caller.accountId
field.
_caller.accountEmailAddressInfo
principal.user.email_addresses
Directly mapped from the
_caller.accountEmailAddressInfo
field.
_caller.accountExternalId
principal.user.email_addresses
Directly mapped from the
_caller.accountExternalId
field.
_caller.accountStatus
principal.user.attribute.labels[account_status].value
Directly mapped from the
_caller.accountStatus
field.
_caller.deviceId
principal.asset.asset_id
Prefixed with "VERIDIUM_ID:" and mapped from the
_caller.deviceId
field.
_caller.deviceDescription
principal.asset.attribute.labels[device_description].value
Directly mapped from the
_caller.deviceDescription
field.
_caller.deviceManufacturer
principal.asset.attribute.labels[device_manufacturer].value
Directly mapped from the
_caller.deviceManufacturer
field.
_caller.deviceName
principal.asset.attribute.labels[device_name].value
Directly mapped from the
_caller.deviceName
field.
_caller.deviceOs
principal.asset.platform_software.platform
Mapped from the
_caller.deviceOs
field. If the value is "iOS", it is mapped to "IOS". If the value is "Android", it is mapped to "ANDROID". If the value is "WIN" or "Windows", it is mapped to "WINDOWS".
_caller.deviceStatus
principal.asset.attribute.labels[device_status].value
Directly mapped from the
_caller.deviceStatus
field.
_caller.deviceType
principal.asset.attribute.labels[device_type].value
Directly mapped from the
_caller.deviceType
field.
actionDate
additional.fields[action_date].value.string_value
Directly mapped from the
actionDate
field.
actionName
metadata.product_event_type
Directly mapped from the
actionName
field.
accountEmail
principal.user.email_addresses
Directly mapped from the
accountEmail
field.
accountExternalId
principal.user.email_addresses
Directly mapped from the
accountExternalId
field.
accountId
principal.user.userid
Directly mapped from the
accountId
field.
authenticatorDeviceContext.deviceMake
intermediary.asset.hardware.manufacturer
Directly mapped from the
authenticatorDeviceContext.deviceMake
field.
authenticatorDeviceContext.ip
intermediary.ip
Directly mapped from the
authenticatorDeviceContext.ip
field.
authenticatorDeviceContext.location.city
intermediary.asset.location.city
Directly mapped from the
authenticatorDeviceContext.location.coordinates.latitude
field.
authenticatorDeviceContext.location.coordinates.latitude
intermediary.asset.location.region_latitude
Directly mapped from the
authenticatorDeviceContext.location.coordinates.latitude
field.
authenticatorDeviceContext.location.coordinates.longitude
intermediary.asset.location.region_longitude
Directly mapped from the
authenticatorDeviceContext.location.coordinates.longitude
field.
authenticatorDeviceContext.location.countryName
intermediary.asset.location.country_or_region
Directly mapped from the
authenticatorDeviceContext.location.countryName
field.
authenticatorDeviceContext.location.ip
intermediary.ip
Directly mapped from the
authenticatorDeviceContext.location.ip
field.
authenticationDeviceDescription
intermediary.asset.attribute.labels[authentication_device_description].value
Directly mapped from the
authenticationDeviceDescription
field.
authenticationDeviceName
intermediary.asset.asset_id
Prefixed with "VERIDIUM_ID:" and mapped from the
authenticationDeviceName
field.
authenticationDeviceOs
intermediary.asset.platform_software.platform
Mapped from the
authenticationDeviceOs
field. If the value is "iOS", it is mapped to "IOS". If the value is "Android", it is mapped to "ANDROID". If the value is "WIN" or "Windows", it is mapped to "WINDOWS".
authenticationDeviceOsVersion
intermediary.asset.platform_software.platform_version
Directly mapped from the
authenticationDeviceOsVersion
field.
authenticationDevicePhone
intermediary.asset.attribute.labels[authentication_device_phone].value
Directly mapped from the
authenticationDevicePhone
field.
authenticationDevicePhoneModel
intermediary.asset.attribute.labels[authentication_device_phone_model].value
Directly mapped from the
authenticationDevicePhoneModel
field.
authenticationDeviceRegistrationTime
intermediary.asset.attribute.labels[authentication_device_registeration_time].value
Directly mapped from the
authenticationDeviceRegistrationTime
field.
authenticationDeviceType
intermediary.asset.attribute.labels[authentication_device_type].value
Directly mapped from the
authenticationDeviceType
field.
authenticationResult
extensions.auth.auth_details
Directly mapped from the
authenticationResult
field.
context.deviceMake
principal.asset.hardware.manufacturer
Directly mapped from the
context.deviceMake
field.
context.ip
principal.ip
Directly mapped from the
context.ip
field.
context.location.countryName
principal.location.country_or_region
Directly mapped from the
context.location.countryName
field.
context.location.ip
principal.ip
Directly mapped from the
context.location.ip
field.
context.osVersion
principal.asset.platform_software.platform_version
Directly mapped from the
context.osVersion
field.
context.userAgentRaw
network.http.user_agent
Directly mapped from the
context.userAgentRaw
field.
exploiterDeviceContext.deviceMake
src.asset.hardware.manufacturer
Directly mapped from the
exploiterDeviceContext.deviceMake
field.
exploiterDeviceContext.ip
src.ip
Directly mapped from the
exploiterDeviceContext.ip
field.
exploiterDeviceContext.location.city
src.asset.location.city
Directly mapped from the
exploiterDeviceContext.location.city
field.
exploiterDeviceContext.location.coordinates.latitude
src.asset.location.region_latitude
Directly mapped from the
exploiterDeviceContext.location.coordinates.latitude
field.
exploiterDeviceContext.location.coordinates.longitude
src.asset.location.region_longitude
Directly mapped from the
exploiterDeviceContext.location.coordinates.longitude
field.
exploiterDeviceContext.location.countryName
src.asset.location.country_or_region
Directly mapped from the
exploiterDeviceContext.location.countryName
field.
exploiterDeviceContext.location.ip
src.ip
Directly mapped from the
exploiterDeviceContext.location.ip
field.
exploiterDeviceContext.osName
src.asset.platform_software.platform
Mapped from the
exploiterDeviceContext.osName
field. If the value is "WIN" or "Windows", it is mapped to "WINDOWS". If the value is "iOS", it is mapped to "IOS". If the value is "Android", it is mapped to "ANDROID".
exploiterDeviceContext.osVersion
src.asset.platform_software.platform_version
Directly mapped from the
exploiterDeviceContext.osVersion
field.
exploiterDeviceName
src.asset.attribute.labels[exploiter_device_name].value
Directly mapped from the
exploiterDeviceName
field.
hostname
principal.hostname
Directly mapped from the
hostname
field.
ipAddress
principal.ip
Directly mapped from the
ipAddress
field.
location
principal.location.city
Directly mapped from the
location
field.
location.city
about.location.city
Directly mapped from the
location.city
field.
location.coordinates.latitude
about.location.region_latitude
Directly mapped from the
location.coordinates.latitude
field.
location.coordinates.longitude
about.location.region_longitude
Directly mapped from the
location.coordinates.longitude
field.
location.countryName
about.location.country_or_region
Directly mapped from the
location.countryName
field.
location.ip
about.ip
Directly mapped from the
location.ip
field.
metadata.collected_timestamp
metadata.collected_timestamp
Directly mapped from the
collected_time
field.
metadata.event_timestamp
metadata.event_timestamp
Directly mapped from the
event_time
field.
metadata.event_type
metadata.event_type
Set to "USER_UNCATEGORIZED".
metadata.product_event_type
metadata.product_event_type
Directly mapped from the
actionName
field.
metadata.product_name
metadata.product_name
Set to "VERIDIUM_ID".
namespace
principal.namespace
Directly mapped from the
namespace
field.
pid
principal.process.pid
Directly mapped from the
pid
field.
request.context.userAgentRaw
network.http.user_agent
Directly mapped from the
request.context.userAgentRaw
field.
request.sessionId
network.session_id
Directly mapped from the
request.sessionId
field.
requestMethod
network.http.method
Directly mapped from the
requestMethod
field.
requestURI
network.http.referral_url
Directly mapped from the
requestURI
field.
security_result.severity
security_result.severity
Mapped from the
severity
field. If the value is "INFO", it is mapped to "INFORMATIONAL".
principal.application
Directly mapped from the
application
field.
principal.asset.hostname
Directly mapped from the
hostname
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
