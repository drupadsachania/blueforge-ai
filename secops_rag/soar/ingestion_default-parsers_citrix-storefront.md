# Collect Citrix StoreFront logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront/  
**Scraped:** 2026-03-05T09:53:01.721546Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Citrix StoreFront logs
Supported in:
Google secops
SIEM
This document explains how to ingest Citrix StoreFront logs to Google Security Operations using Bindplane. The parser extracts fields from Citrix StoreFront Windows Event Log formatted logs. It uses Windows Event Log collection to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type. The parser extracts data from Citrix StoreFront JSON logs by breaking down the message field into individual entities like
Session
,
User
,
AppInstance
,
App
,
Connection
, and
Machine
using a series of
grok
patterns. It then maps the extracted fields to a unified data model (UDM) structure, enriching it with network, principal, intermediary, and target information based on conditional logic and data transformations.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
A Windows 2016 or later host with
systemd
where Bindplane will be installed
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Citrix StoreFront server and management console
Administrative access to the Windows server hosting StoreFront
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
Additional installation resources
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Windows event logs and send to Google SecOps
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
windowseventlog/storefront
:
channel
:
Application
operators
:
-
type
:
filter
expr
:
'record["source_name"]
matches
"^Citrix"'
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
'C:/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
CUSTOMER_ID_PLACEHOLDER
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'CITRIX_STOREFRONT'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/storefront
:
receivers
:
-
windowseventlog/storefront
exporters
:
-
chronicle/chronicle_w_labels
Replace
CUSTOMER_ID_PLACEHOLDER
with the actual Customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the BindPlane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure StoreFront event logging
Sign in to the
StoreFront Server
with administrative privileges.
Open
PowerShell
as an administrator.
Load the StoreFront PowerShell module:
Add-PSSnapin
Citrix
.
DeliveryServices
.
Framework
.
Commands
Enable verbose logging for troubleshooting (optional):
Set-STFDiagnostics
-All
-TraceLevel
"Info"
-confirm
:
$False
Verify Windows Event Logging is enabled:
Open
Event Viewer
on the StoreFront server.
Navigate to
Application and Services Logs
>
Citrix Delivery Services
.
Verify that events are being logged for the authentication service, stores, and Receiver for Web sites.
Optional: Configure event log throttling
Navigate to the StoreFront configuration directories:
Authentication service:
C:/inetpub/wwwroot/Citrix/Authentication
Store:
C:/inetpub/wwwroot/Citrixstorename
Receiver for Web site:
C:/inetpub/wwwroot/Citrixstorename/Web
Open the
web.config
file in each directory using a text editor.
Locate the logger element and configure as needed:
<logger
duplicateInterval="00:01:00"
duplicateLimit="10">
duplicateInterval
: Set the time period in hours, minutes, and seconds over which duplicate log entries are monitored.
duplicateLimit
: Set the number of duplicate entries that must be logged within the specified time interval to trigger log throttling.
Save the configuration files.
Verify log collection
Open the
Windows Event Viewer
on the StoreFront server.
Navigate to
Windows Logs
>
Application
or
Application and Services Logs
>
Citrix Delivery Services
.
Verify that StoreFront events are being generated.
Check the Bindplane agent logs to confirm logs are being forwarded to Google SecOps.
UDM mapping table
Log field
UDM mapping
Logic
App.PublishedName
_principal.application
The value is taken from the App.PublishedName field.
Connection.ClientAddress
_principal.asset.ip
The value is taken from the Connection.ClientAddress field.
Connection.ClientName
_principal.asset.hostname
The value is taken from the Connection.ClientName field.
Connection.ClientPlatform
_principal.asset.platform_software.platform
The value is taken from the Connection.ClientPlatform field and converted to uppercase. If the value is "WINDOWS", "MAC", or "LINUX", it is used directly. Otherwise, the value is set to "UNKNOWN_PLATFORM".
Connection.ConnectedViaHostName
src.hostname
The value is taken from the Connection.ConnectedViaHostName field.
Connection.LaunchedViaHostName
_intermediary.hostname
The value is taken from the Connection.LaunchedViaHostName field. The namespace is set to "StoreFront server".
Connection.LaunchedViaIPAddress
_intermediary.ip
The value is taken from the Connection.LaunchedViaIPAddress field.
Connection.Protocol
network.application_protocol
The value is taken from the Connection.Protocol field. If the value is "HDX", it is set to "UNKNOWN_APPLICATION_PROTOCOL".
Machine.AgentVersion
metadata.product_version
The value is taken from the Machine.AgentVersion field.
Machine.AssociatedUserNames
_intermediary.user.userid
The value is taken from the Machine.AssociatedUserNames field. Each name is extracted and used as the userid for an intermediary user object.
Machine.AssociatedUserUPNs
_target.group.email_addresses
The value is taken from the Machine.AssociatedUserUPNs field. Each email address is extracted and added to the target group's email_addresses field.
Machine.ControllerDnsName
_intermediary.hostname
The value is taken from the Machine.ControllerDnsName field. The namespace is set to "Controller".
Machine.CreatedDate
_target.asset.attribute.creation_time
The value is taken from the Machine.CreatedDate field and converted to a timestamp.
Machine.DesktopGroupId
_target.group.product_object_id
The value is taken from the Machine.DesktopGroupId field.
Machine.DnsName
_target.asset.network_domain
The value is taken from the Machine.DnsName field.
Machine.HostedMachineName
_target.asset.hostname
The value is taken from the Machine.HostedMachineName field.
Machine.HostingServerName
_intermediary.hostname
The value is taken from the Machine.HostingServerName field. The namespace is set to "Hypervisor".
Machine.IPAddress
_target.asset.ip
The value is taken from the Machine.IPAddress field.
Machine.LastDeregisteredDate
_target.asset.last_discover_time
The value is taken from the Machine.LastDeregisteredDate field and converted to a timestamp.
Machine.ModifiedDate
_target.asset.system_last_update_time
The value is taken from the Machine.ModifiedDate field and converted to a timestamp.
Machine.Name
_target.asset.asset_id, _target.administrative_domain
The value is taken from the Machine.Name field and split into domain and asset parts. The domain part is used as the target administrative domain, and the asset part is used to construct the target asset ID in the format "machine:
".
Machine.OSType
_target.asset.platform_software.platform_version
The value is taken from the Machine.OSType field.
Machine.PoweredOnDate
_target.asset.last_boot_time
The value is taken from the Machine.PoweredOnDate field and converted to a timestamp.
Machine.RegistrationStateChangeDate
_target.asset.first_discover_time
The value is taken from the Machine.RegistrationStateChangeDate field and converted to a timestamp.
Session.EndDate
_vulns.last_found
The value is taken from the Session.EndDate field and converted to a timestamp.
Session.LifecycleState
extensions.auth.auth_details
The value is taken from the Session.LifecycleState field. If the value is 0, it is set to "ACTIVE". If the value is 1, it is set to "DELETED". If the value is 2 or 3, it is set to "UNKNOWN_AUTHENTICATION_STATUS".
Session.LogOnDuration
network.session_duration.seconds
The value is taken from the Session.LogOnDuration field and converted to an integer.
Session.SessionKey
network.session_id
The value is taken from the Session.SessionKey field.
Session.StartDate
_vulns.first_found
The value is taken from the Session.StartDate field and converted to a timestamp.
User.Domain
_principal.user.company_name, _principal.administrative_domain
The value is taken from the User.Domain field and used as both the principal user's company name and the principal administrative domain.
User.FullName
_principal.user.user_display_name
The value is taken from the User.FullName field.
User.Sid
_principal.user.windows_sid
The value is taken from the User.Sid field.
User.Upn
_principal.user.email_addresses
The value is taken from the User.Upn field and added to the principal user's email_addresses field.
User.UserName
_principal.user.userid
The value is taken from the User.UserName field.
metadata.event_type
The value is set to "USER_LOGIN".
metadata.vendor_name
The value is set to "Citrix".
metadata.product_name
The value is set to "Monitor Service OData".
extensions.auth.type
The value is set to "MACHINE".
_intermediary.namespace
The value is set to "StoreFront server", "Controller", or "Hypervisor" depending on the intermediary object.
_target.asset.type
The value is set to "WORKSTATION".
Need more help?
Get answers from Community members and Google SecOps professionals.
