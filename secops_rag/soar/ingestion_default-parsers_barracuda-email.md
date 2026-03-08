# Collect Barracuda Email Security Gateway logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-email/  
**Scraped:** 2026-03-05T09:51:10.154631Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Barracuda Email Security Gateway logs
Supported in:
Google secops
SIEM
This document explains how to collect Barracuda Email Security Gateway logs by using Bindplane. The parser extracts fields from the logs using Grok patterns and JSON parsing. Then, it maps the extracted fields to the Unified Data Model (UDM) schema, categorizes the email activity (for example, spam or phishing), and determines the security action taken (for example, allow, block, or quarantine).
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the Symantec DLP.
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
"0.0.0.0:54525"
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
barracuda_email
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
Configure Barracuda Email Security Gateway
Sign in to the
Barracuda ESG Interface
.
Select
Advanced
>
Advanced networking
>
Syslog Configuration
.
Provide the following details:
Enable Syslog logging by checking the
Enable Syslog
checkbox.
Syslog Server
: enter the
Bindplane
IP address.
Port
: specify the Syslog port (default is 514, but ensure this matches the configuration in Google Security Operations).
Syslog Facility
choose
Local0
.
Severity Level
: select
Error and Warning
for higher priority email security logs.
Click
Save Changes
to apply the configuration.
UDM Mapping Table
Log field
UDM mapping
Logic
account_id
Not Mapped
attachments
Not Mapped
dst_domain
target.hostname
Value of dst_domain field
dst_domain
target.asset.hostname
Value of dst_domain field
env_from
Not Mapped
geoip
target.location.country_or_region
Value of geoip field
hdr_from
network.email.from
Value of hdr_from field if it is an email address
hdr_to
network.email.to
Value of hdr_to field if it is an email address, otherwise parsed from JSON array in hdr_to field
host
principal.hostname
Value of host field
host
principal.asset.hostname
Value of host field
message_id
network.email.mail_id
Value of message_id field
product_log_id
metadata.product_log_id
Value of product_log_id field
queue_id
security_result.detection_fields.value
Value of queue_id field
recipient_email
network.email.to
Value of recipient_email field if it is not empty or
-
recipients
Not Mapped
recipients.action
security_result.action
Mapped to ALLOW if value is
allowed
, otherwise mapped to BLOCK
recipients.action
security_result.action_details
Value of recipients.action field
recipients.delivery_detail
security_result.detection_fields.value
Value of recipients.delivery_detail field
recipients.delivered
security_result.detection_fields.value
Value of recipients.delivered field
recipients.email
network.email.to
Value of recipients.email field if it is an email address
recipients.reason
security_result.detection_fields.value
Value of recipients.reason field
recipients.reason_extra
security_result.detection_fields.value
Value of recipients.reason_extra field
recipients.taxonomy
security_result.detection_fields.value
Value of recipients.taxonomy field
service
security_result.summary
Value of service field
size
network.received_bytes
Value of size field converted to an unsigned integer
src_ip
principal.ip
Value of src_ip field if it is not empty or
0.0.0.0
src_ip
principal.asset.ip
Value of src_ip field if it is not empty or
0.0.0.0
src_ip
security_result.about.ip
Value of src_ip field if it is not empty or
0.0.0.0
subject
network.email.subject
Value of subject field
target_ip
target.ip
Value of target_ip field
target_ip
target.asset.ip
Value of target_ip field
timestamp
metadata.event_timestamp
Parsed timestamp from the log entry
metadata.event_type
Hardcoded to
EMAIL_TRANSACTION
metadata.log_type
Hardcoded to
BARRACUDA_EMAIL
metadata.vendor_name
Hardcoded to
Barracuda
network.application_protocol
Set to
SMTP
if process field contains
smtp
network.direction
Set to
INBOUND
if process field contains
inbound
, set to
OUTBOUND
if process field contains
outbound
security_result.action
Set based on a combination of action, action_code, service, and delivered fields
security_result.category
Set based on a combination of action, reason, and other fields
security_result.confidence
Hardcoded to
UNKNOWN_CONFIDENCE
security_result.priority
Hardcoded to
UNKNOWN_PRIORITY
security_result.severity
Hardcoded to
UNKNOWN_SEVERITY
if category is
UNKNOWN_CATEGORY
Need more help?
Get answers from Community members and Google SecOps professionals.
