# Collect MobileIron logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mobileiron/  
**Scraped:** 2026-03-05T09:26:41.319898Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect MobileIron logs
Supported in:
Google secops
SIEM
This document explains how to ingest MobileIron logs to Google Security Operations using a Bindplane agent. The parser transforms JSON formatted logs into a unified data model (UDM). It extracts fields from the raw JSON, maps them to corresponding UDM attributes, and enriches the data with platform-specific details and security event context.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to MobileIron.
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
# Select the appropriate regional endpoint based on where your Google SecOps instance is provisioned
# For regional endpoints, see: https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints
endpoint
:
malachiteingestion-pa.googleapis.com
# Set the log_type to ensure the correct parser is applied
log_type
:
MOBILEIRON
raw_log_field
:
body
# You can optionally add other custom ingestion labels here if needed
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
Configuring Syslog Servers in MobileIron
Sign in to the
System Manager
.
Go to
Settings
>
Data Export
>
SysLog Servers
.
Click
Add
.
The
Add SysLog
window should open.
Provide the following configuration details:
Server
: enter the Bindplane IP address and port.
Protocol
: select
UDP
(you can also select
TCP
or
TLS over TCP
depending on your Bindplane configuration).
Optional:
Trusted Server Certificate
: this field displays only if you select
TLS over TCP
in the
Protocol
.
Admin State
: Select
Enable
.
Severity (facility.level)
: Enter
*.info
for all messages with a severity of info or higher.
Click
Apply
>
OK
to save the changes.
UDM Mapping Table
Log Field
UDM Mapping
Logic
complianceViolationTypeToReason.BLACKLIST_APPS
security_result.description
Value from
complianceViolationTypeToReason.BLACKLIST_APPS
field, prefixed with
Compliance Violation Type To Reason BLACKLIST APPS -
.
complianceViolationTypeToReason.PC
security_result.description
Value from
complianceViolationTypeToReason.PC
field, prefixed with
Compliance Violation Type To Reason PC -
.
complianceViolationTypeToReason.SA
security_result.description
Value from
complianceViolationTypeToReason.SA
field, prefixed with
Compliance Violation Type To Reason SA -
.
displayName
principal.user.user_display_name
Directly mapped from
displayName
.
emailAddress
principal.user.email_addresses
Directly mapped from
emailAddress
.
firstName
principal.user.first_name
Directly mapped from
firstName
.
id
principal.asset.product_object_id
Directly mapped from
id
.
lastName
principal.user.last_name
Directly mapped from
lastName
.
platformType
principal.asset.platform_software.platform
Mapped from
platformType
with the following logic:
- If
platformType
matches
Windows
(case-insensitive), set to
WINDOWS
.
- If
platformType
matches
MAC
,
OS X
, or
IOS
(case-insensitive), set to
MAC
.
- If
platformType
matches
Linux
(case-insensitive), set to
LINUX
.
- Otherwise, set to
UNKNOWN_PLATFORM
.
platformType
principal.asset.platform_software.platform_version
Concatenation of
platformType
and
platformVersion
with a
-
delimiter.
platformVersion
principal.asset.platform_software.platform_version
Concatenation of
platformType
and
platformVersion
with a
-
delimiter.
policyViolatedAt
metadata.event_timestamp
Converted to a timestamp from milliseconds since epoch.
policyViolatedAt
security_result.about.labels.value
Directly mapped from
policyViolatedAt
after converting to a string.
policyViolatedID
security_result.rule_id
Directly mapped from
policyViolatedID
.
prettyModel
principal.asset.hardware.model
Directly mapped from
prettyModel
.
N/A
metadata.event_type
Hardcoded to
USER_UNCATEGORIZED
.
N/A
metadata.log_type
Hardcoded to
MOBILEIRON
.
N/A
metadata.product_name
Hardcoded to
MOBILEIRON
.
N/A
metadata.vendor_name
Hardcoded to
MOBILEIRON
.
N/A
principal.asset.type
Hardcoded to
MOBILE
.
N/A
security_result.about.labels.key
Hardcoded to
Policy Violated At
.
N/A
security_result.category
Hardcoded to
POLICY_VIOLATION
.
Need more help?
Get answers from Community members and Google SecOps professionals.
