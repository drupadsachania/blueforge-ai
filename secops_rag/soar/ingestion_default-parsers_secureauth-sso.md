# Collect SecureAuth Identity Platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/secureauth-sso/  
**Scraped:** 2026-03-05T09:59:44.222347Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect SecureAuth Identity Platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest SecureAuth Identity Platform logs to Google Security Operations by using Bindplane. The parser extracts fields from various log formats (SYSLOG, XML, key-value pairs) using grok and xml filters. Then, it maps the extracted fields to the corresponding UDM (Unified Data Model) attributes, enriching the data with security event context and standardizing the output for further analysis.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to SecureAuth.
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
SECUREAUTH_SSO
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
Configure SecureAuth Identity Platform
Sign in to the
SecureAuth Identity console
.
Select
Logs
.
Provide the following configuration details in the
Log options
section:
Log instance ID
: enter the log instance ID, the Application Name or the realm name; for example,
SecureAuth1
.
Audit logs
: select the
Syslog
checkbox.
Error logs
: select the
Syslog
checkbox.
Syslog Server
: enter the IP Address of your Bindplane agent.
Syslog Port
: enter the Bindplane agent port number; for example,
514
.
Syslog RFC spec
: select
RFC 5424
.
Click
Save
.
Supported SecureAuth log formats
The SecureAuth parser supports logs in Syslog and XML formats.
Supported SecureAuth sample logs
SYSLOG + XML
<150>Nov
25
18:42:24
192.168.1.1
<Root>
<EventID>90010</EventID>
<Priority>4</Priority>
<Message>Session
-
Start</Message>
<Category>AUDIT</Category>
<UserHostAddress>10.0.0.1</UserHostAddress>
<BrowserSession>48a28fd1-b4c6-4d9e-b24e-b1fd0d3b9407</BrowserSession>
<RequestID>3e0e05e2-c2ef-41b1-8995-109676e653ed</RequestID>
<Realm>DUMMY_REALM</Realm>
<Appliance>DUMMY-APPLIANCE@dummycorp.com</Appliance>
<Company>DUMMY
CORP</Company>
<Version>19.07.1.18</Version>
<HostName>192.168.1.1</HostName>
</Root>
UDM mapping table
Log field
UDM mapping
Logic
action_msg
read_only_udm.target.process.command_line
Value of
action_msg
field
Appliance
read_only_udm.principal.domain.name
Value of
Appliance
field
Appliance
read_only_udm.target.administrative_domain
Value of
Appliance
field
BrowserSession
read_only_udm.network.session_id
Value of
BrowserSession
field
cat
read_only_udm.metadata.product_event_type
Value of
cat
field
Category
read_only_udm.metadata.product_event_type
Value of
Category
field
cn1
security_result.severity
Mapped based on the value of
cn1
when
cn1Label
is 'Priority': 1 - HIGH, 2 - MEDIUM, 3 or 4 - LOW
Company
read_only_udm.additional.fields.value.string_value
Value of
Company
field
cs1
read_only_udm.network.session_id
Value of
cs1
field when
cs1Label
is 'BrowserSession'
cs3
read_only_udm.additional.fields.value.string_value
Value of
cs3
field when
cs3Label
is 'CompanyName'
dst
read_only_udm.target.ip
Value of
dst
field
domain
read_only_udm.principal.domain.name
Value of
domain
field
dvc
read_only_udm.intermediary.ip
Value of
dvc
field
EventID
read_only_udm.metadata.product_log_id
Value of
EventID
field
HostName
read_only_udm.principal.hostname
Value of
HostName
field when grok fails to match IP address
HostName
read_only_udm.principal.ip
Value of
HostName
field when grok matches IP address
ip
read_only_udm.principal.ip
Value of
ip
field
Message
read_only_udm.metadata.description
Value of
Message
field
Message
security_result.description
Value of
Message
field
nat_ip
read_only_udm.principal.nat_ip
Value of
nat_ip
field
Priority
security_result.severity
Mapped based on the value of
Priority
: 1 - HIGH, 2 - MEDIUM, 3 or 4 - LOW
SAMLConsumerURL
read_only_udm.target.url
Value of
SAMLConsumerURL
field
sec_msg
security_result.description
Value of
sec_msg
field
SecureAuthIdPAppliance
read_only_udm.target.administrative_domain
Value of
SecureAuthIdPAppliance
field
SecureAuthIdPApplianceMachineName
read_only_udm.target.hostname
Value of
SecureAuthIdPApplianceMachineName
field
SecureAuthIdPDestinationSiteUrl
read_only_udm.target.url
Value of
SecureAuthIdPDestinationSiteUrl
field
SecureAuthIdPProductType
read_only_udm.additional.fields.value.string_value
Value of
SecureAuthIdPProductType
field
session
read_only_udm.network.session_id
Value of
session
field
spid
read_only_udm.target.process.pid
Value of
spid
field
src
read_only_udm.principal.ip
Value of
src
field
suser
read_only_udm.target.user.userid
Value of
suser
field
UserAgent
read_only_udm.network.http.user_agent
Value of
UserAgent
field
UserHostAddress
read_only_udm.principal.nat_ip
Value of
UserHostAddress
field
UserHostAddress
read_only_udm.target.ip
Value of
UserHostAddress
field
UserID
read_only_udm.principal.user.userid
Value of
UserID
field
Version
read_only_udm.metadata.product_version
Value of
Version
field
read_only_udm.additional.fields.key
Hardcoded value - 'CompanyName'
read_only_udm.additional.fields.key
Hardcoded value - 'Company'
read_only_udm.additional.fields.key
Hardcoded value - 'SecureAuthIdPProductType'
read_only_udm.extensions.auth.type
Hardcoded value - 'SSO'
read_only_udm.metadata.event_type
'USER_LOGIN' if
SecureAuthIdPAuthGuiMode
==
0
and
auth_result
==
Success
, 'USER_CHANGE_PERMISSIONS' if
SecureAuthIdPAuthGuiMode
==
0
and
auth_result
==
WS-Trust success.
, 'USER_LOGOUT' if
SecureAuthIdPAuthGuiMode
==
0
and
auth_result
==
Session Aborted
, 'NETWORK_CONNECTION' if
UserHostAddress
!=
and `HostName` !=
, 'STATUS_UPDATE' if
ip
!=
or `HostName` !=
, 'USER_UNCATEGORIZED' if
UserHostAddress
!=
and `HostName` ==
and
UserID
!= ``, otherwise - 'GENERIC_EVENT'
read_only_udm.metadata.log_type
Hardcoded value - 'SECUREAUTH_SSO'
read_only_udm.metadata.product_name
Hardcoded value - 'SECUREAUTH_SSO'
read_only_udm.metadata.vendor_name
Hardcoded value - 'SECUREAUTH_SSO'
read_only_udm.target.user.email_addresses
Value of
user_email
field when
not_email
is false
security_result.severity
'HIGH' if
cn1Label
==
Priority
and
cn1
==
1
, 'MEDIUM' if
cn1Label
==
Priority
and
cn1
==
2
, 'LOW' if
cn1Label
==
Priority
and
cn1
in [
3
,
4
], 'HIGH' if
Priority
==
1
, 'MEDIUM' if
Priority
==
2
, 'LOW' if
Priority
in [
3
,
4
]
Need more help?
Get answers from Community members and Google SecOps professionals.
