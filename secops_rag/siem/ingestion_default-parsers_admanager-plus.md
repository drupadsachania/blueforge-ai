# Collect ManageEngine ADManager Plus logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/admanager-plus/  
**Scraped:** 2026-03-05T09:26:09.676585Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ManageEngine ADManager Plus logs
Supported in:
Google secops
SIEM
This document explains how to ingest ManageEngine ADManager Plus logs to Google Security Operations using the Bindplane agent.
ManageEngine ADManager Plus offers a web-based solution for simplified AD management, including user creation and modification, role-based security, and detailed reports. ADManager Plus' integration with Splunk and Syslog servers enables organizations to forward logs of all Active Directory, Microsoft 365, and Google Workspace management actions performed in ADManager Plus.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
Network connectivity between the Bindplane agent and ManageEngine ADManager Plus
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the ManageEngine ADManager Plus management console
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Click
Download
to download the
Ingestion Authentication File
.
Save the file securely on the system where the Bindplane agent will be installed.
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
"https://github.com/observIQ/bindplane-otel-collector/releases/latest/download/observiq-otel-collector.msi"
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
https://github.com/observiq/bindplane-otel-collector/releases/latest/download/install_unix.sh
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
Configure the Bindplane agent to ingest syslog and send to Google SecOps
Locate the configuration file
Linux:
sudo
nano
/opt/observiq-otel-collector/config.yaml
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
"0.0.0.0:514"
exporters
:
chronicle/admanager_plus
:
compression
:
gzip
creds_file_path
:
'<CREDS_FILE_PATH>'
customer_id
:
'<CUSTOMER_ID>'
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
ADMANAGER_PLUS
raw_log_field
:
body
ingestion_labels
:
log_source
:
admanager_plus
service
:
pipelines
:
logs/admanager_to_chronicle
:
receivers
:
-
tcplog
exporters
:
-
chronicle/admanager_plus
Replace the following placeholders:
Receiver configuration:
The receiver uses
tcplog
to receive syslog data on TCP port 514.
listen_address
: Set to
0.0.0.0:514
to listen on all interfaces on port 514.
Exporter configuration:
<CREDS_FILE_PATH>
: Full path to ingestion authentication file:
Linux
:
/opt/observiq-otel-collector/ingestion-auth.json
Windows
:
C:\\Program Files\\observIQ OpenTelemetry Collector\\ingestion-auth.json
<CUSTOMER_ID>
: Customer ID from the previous step.
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
for complete list.
log_type
: Set to
ADMANAGER_PLUS
exactly as it appears in Chronicle.
ingestion_labels
: Optional labels in YAML format.
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
Linux
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
Windows
To restart the Bindplane agent in Windows, choose one of the following options:
Using Command Prompt or PowerShell as administrator:
net stop observiq-otel-collector && net start observiq-otel-collector
Using Services console:
Press
Win+R
, type
services.msc
, and press Enter.
Locate
observIQ Distro for OpenTelemetry Collector
.
Right-click and select
Restart
.
Verify the service is running:
sc query observiq-otel-collector
Check logs for errors:
type
"C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
Configure ManageEngine ADManager Plus syslog forwarding
Log in to ADManager Plus.
Navigate to the
Admin
tab.
Under
System Settings
, click
Integrations
.
Under
Log Forwarding
, click
Syslog
.
Configure the following fields:
Syslog Server
: Enter the syslog server name. Enter the IP address or hostname of the Bindplane agent host.
Port
: Enter the port number. Enter
514
.
Protocol
: Choose the appropriate protocol, TCP or UDP, for forwarding logs. Select
TCP
.
Syslog Standard
: Select the desired syslog message format, RFC 3164, RFC 5424, or RawLog. Select
RFC 5424
(recommended).
Data Format
: Enter the data format. Configure the data format as needed for your environment.
Click
Save
to save the configuration.
After configuration, ADManager Plus will begin forwarding logs of management actions to the Bindplane agent, which will then send them to Google SecOps.
UDM mapping table
Log Field
UDM Mapping
Logic
ipPhone
event.idm.read_only_udm.additional.fields
Merged as label with key "ipPhone" and value from ipPhone if ipPhone != ""
l
event.idm.read_only_udm.additional.fields
Merged as label with key "l" and value from l if l != ""
lockoutTime
event.idm.read_only_udm.additional.fields
Merged as label with key "lockoutTime" and value from lockoutTime if lockoutTime != ""
Move From
event.idm.read_only_udm.additional.fields
Merged as label with key "Move From" and value from Move_From if Move_From != ""
Move To
event.idm.read_only_udm.additional.fields
Merged as label with key "Move To" and value from Move_To if Move_To != ""
msg
event.idm.read_only_udm.additional.fields
Merged as label with key "member" and value from msg if msg != ""
sn
event.idm.read_only_udm.additional.fields
Merged as label with key "sn" and value from sn if sn != ""
st
event.idm.read_only_udm.additional.fields
Merged as label with key "st" and value from st if st != ""
Template Name
event.idm.read_only_udm.additional.fields
Merged as label with key "Template Name" and value from Template_Name if Template_Name != ""
Status
event.idm.read_only_udm.metadata.description
Value taken from Status if Status != ""
time
event.idm.read_only_udm.metadata.event_timestamp
Converted from time to timestamp format if time != ""
event.idm.read_only_udm.metadata.event_type
Derived: if has_principal_user == "true" then "USER_UNCATEGORIZED"; else if has_principal == "true" then "STATUS_UPDATE"; else "GENERIC_EVENT"
TechnicianName
event.idm.read_only_udm.metadata.product_event_type
Value taken from TechnicianName if TechnicianName != ""
event.idm.read_only_udm.metadata.product_name
Set to "ADMANAGER_PLUS"
event.idm.read_only_udm.metadata.vendor_name
Set to "ADMANAGER_PLUS"
Domain Name
event.idm.read_only_udm.principal.administrative_domain
Value taken from Domain_Name if Domain_Name != ""
hostname
event.idm.read_only_udm.principal.asset.hostname
Value taken from hostname if hostname != ""
mail
event.idm.read_only_udm.principal.email
Value taken from mail if mail != ""
hostname
event.idm.read_only_udm.principal.hostname
Value taken from hostname if hostname != ""
co
event.idm.read_only_udm.principal.location.city
Value taken from co if co != ""
Task
event.idm.read_only_udm.principal.resource.name
Value taken from Task if Task != ""
wWWHomePage
event.idm.read_only_udm.principal.url
Value taken from wWWHomePage if wWWHomePage != ""
Password Type
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "Password Type" and value from Password_Type if Password_Type != ""
countryCode
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "countryCode" and value from countryCode if countryCode != ""
password
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "password" and value from password if password != ""
postalCode
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "postalCode" and value from postalCode if postalCode != ""
primaryGroupID
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "primaryGroupID" and value from primaryGroupID if primaryGroupID != ""
userAccountControl
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "userAccountControl" and value from userAccountControl if userAccountControl != ""
userPrincipalName
event.idm.read_only_udm.principal.user.attribute.labels
Merged as label with key "userPrincipalName" and value from userPrincipalName if userPrincipalName != ""
company
event.idm.read_only_udm.principal.user.company_name
Value taken from company if company != ""
department
event.idm.read_only_udm.principal.user.department
Merged with department if department != ""
givenName
event.idm.read_only_udm.principal.user.first_name
Value taken from givenName if givenName != ""
physicalDeliveryOfficeName
event.idm.read_only_udm.principal.user.office_address.name
Value taken from physicalDeliveryOfficeName if physicalDeliveryOfficeName != ""
streetAddress
event.idm.read_only_udm.principal.user.personal_address.name
Value taken from streetAddress if streetAddress != ""
homePhone
event.idm.read_only_udm.principal.user.phone_numbers
Merged with homePhone if homePhone != ""
User Name
event.idm.read_only_udm.principal.user.user_display_name
Value taken from User_Name if User_Name != ""; else from Object_Name if Object_Name != ""
sAMAccountName
event.idm.read_only_udm.principal.user.userid
Value taken from sAMAccountName if sAMAccountName != ""
ACTION
event.idm.read_only_udm.security_result.action_details
Value taken from ACTION if ACTION != ""
description
event.idm.read_only_udm.security_result.description
Value taken from description if description != ""
Container Name
event.idm.read_only_udm.security_result.detection_fields
Derived from container_Name grok: merged as label with key "Container_Name_DC_value1" and value from dc_label_1 if dc_label_1 != ""
Container Name
event.idm.read_only_udm.security_result.detection_fields
Derived from container_Name grok: merged as label with key "Container_Name_DC_value2" and value from dc_label_2 if dc_label_2 != ""
Container Name
event.idm.read_only_udm.security_result.detection_fields
Derived from container_Name grok: merged as label with key "Container_Name_OU_value1" and value from ou_label_1 if ou_label_1 != ""
Container Name
event.idm.read_only_udm.security_result.detection_fields
Derived from container_Name grok: merged as label with key "Container_Name_OU_value2" and value from ou_label_2 if ou_label_2 != ""
Container Name
event.idm.read_only_udm.security_result.detection_fields
Derived from container_Name grok: merged as label with key "Container_Name_OU_value3" and value from ou_label_3 if ou_label_3 != ""
Primary Group
event.idm.read_only_udm.security_result.detection_fields
Derived from Primary_Group grok: merged as label with key "Primary_Group_CN_value1" and value from cn_label_1 if cn_label_1 != ""
Primary Group
event.idm.read_only_udm.security_result.detection_fields
Derived from Primary_Group grok: merged as label with key "Primary_Group_CN_value2" and value from cn_label_2 if cn_label_2 != ""
Primary Group
event.idm.read_only_udm.security_result.detection_fields
Derived from Primary_Group grok: merged as label with key "Primary_Group_DC_value1" and value from primary_dc_label_1 if primary_dc_label_1 != ""
Primary Group
event.idm.read_only_udm.security_result.detection_fields
Derived from Primary_Group grok: merged as label with key "Primary_Group_DC_value2" and value from primary_dc_label_2 if primary_dc_label_2 != ""
accountExpires
event.idm.read_only_udm.security_result.detection_fields
Merged as label with key "accountExpires" and value from accountExpires if accountExpires != ""
manager
event.idm.read_only_udm.security_result.detection_fields
Derived from manager grok: merged as label with key "manager_cn_value1" and value from manager_cn_value1 if manager_cn_value1 != ""
manager
event.idm.read_only_udm.security_result.detection_fields
Derived from manager grok: merged as label with key "manager_dc_value1" and value from manager_dc_value1 if manager_dc_value1 != ""
manager
event.idm.read_only_udm.security_result.detection_fields
Derived from manager grok: merged as label with key "manager_dc_value2" and value from manager_dc_value2 if manager_dc_value2 != ""
manager
event.idm.read_only_udm.security_result.detection_fields
Derived from manager grok: merged as label with key "manager_ou_value1" and value from manager_ou_value1 if manager_ou_value1 != ""
manager
event.idm.read_only_udm.security_result.detection_fields
Derived from manager grok: merged as label with key "manager_ou_value2" and value from manager_ou_value2 if manager_ou_value2 != ""
manager
event.idm.read_only_udm.security_result.detection_fields
Derived from manager grok: merged as label with key "manager_ou_value3" and value from manager_ou_value3 if manager_ou_value3 != ""
pwdLastSet
event.idm.read_only_udm.security_result.detection_fields
Merged as label with key "pwdLastSet" and value from pwdLastSet if pwdLastSet != ""
ModuleName
event.idm.read_only_udm.target.resource.name
Value taken from ModuleName if ModuleName != ""
Need more help?
Get answers from Community members and Google SecOps professionals.
