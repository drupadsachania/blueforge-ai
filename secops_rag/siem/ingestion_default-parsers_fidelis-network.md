# Collect Fidelis Network logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fidelis-network/  
**Scraped:** 2026-03-05T09:24:15.197208Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fidelis Network logs
Supported in:
Google secops
SIEM
This document explains how to ingest Fidelis Network logs to Google Security Operations using Bindplane.
Fidelis Network is a network detection and response (NDR) solution that provides deep content inspection, session-level analysis, and automated threat response. It monitors network traffic in real-time to detect advanced threats, data exfiltration attempts, and policy violations across all ports and protocols. The parser extracts fields from Fidelis Network syslog formatted logs using KV and JSON patterns. It then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Windows Server 2016 or later, or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the Fidelis Network CommandPost web interface
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
tcplog
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
'FIDELIS_NETWORK'
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
tcplog
exporters
:
-
chronicle/chronicle_w_labels
Configuration parameters
Replace the following placeholders:
Receiver configuration:
tcplog
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
FIDELIS_NETWORK
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
Configure Fidelis Network syslog forwarding
Sign in to the
Fidelis Network
CommandPost web interface.
Go to
System
>
Export
>
Syslog
.
Click
Add Syslog Server
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google-SecOps-Bindplane
).
IP Address/Hostname
: Enter the IP address of the Bindplane agent host.
Port
: Enter
514
.
Protocol
: Select
TCP
.
Format
: Select
CEF
(Common Event Format) or
Syslog
based on your parsing requirements.
Facility
: Select
LOCAL0
(or your preferred facility).
Severity
: Select
Informational
(or your preferred severity level).
In the
Alert Types
section, select the events to forward:
Alert events
Malware events
DLP events
DNS events
Session events
Click
Save
.
Verify syslog messages are being sent by checking the Bindplane agent logs.
UDM mapping table
Log Field
UDM Mapping
Logic
aaction
event.idm.read_only_udm.security_result.action_details
Directly mapped if not "none" or empty string.
alert_threat_score
event.idm.read_only_udm.security_result.detection_fields[].key: "alert_threat_score", event.idm.read_only_udm.security_result.detection_fields[].value: value of alert_threat_score
Directly mapped as a detection field.
alert_type
event.idm.read_only_udm.security_result.detection_fields[].key: "alert_type", event.idm.read_only_udm.security_result.detection_fields[].value: value of alert_type
Directly mapped as a detection field.
answers
event.idm.read_only_udm.network.dns.answers[].data
Directly mapped for DNS events.
application_user
event.idm.read_only_udm.principal.user.userid
Directly mapped.
asset_os
event.idm.read_only_udm.target.platform
Normalized to WINDOWS, LINUX, MAC, or UNKNOWN_PLATFORM.
certificate.end_date
event.idm.read_only_udm.network.tls.client.certificate.not_after
Parsed and converted to timestamp.
certificate.extended_key_usage
event.idm.read_only_udm.additional.fields[].key: "Extended Key Usage", event.idm.read_only_udm.additional.fields[].value.string_value: value of certificate.extended_key_usage
Mapped as an additional field.
certificate.issuer_name
event.idm.read_only_udm.network.tls.server.certificate.issuer
Directly mapped.
certificate.key_length
event.idm.read_only_udm.additional.fields[].key: "Key Length", event.idm.read_only_udm.additional.fields[].value.string_value: value of certificate.key_length
Mapped as an additional field.
certificate.key_usage
event.idm.read_only_udm.additional.fields[].key: "Key Usage", event.idm.read_only_udm.additional.fields[].value.string_value: value of certificate.key_usage
Mapped as an additional field.
certificate.start_date
event.idm.read_only_udm.network.tls.client.certificate.not_before
Parsed and converted to timestamp.
certificate.subject_altname
event.idm.read_only_udm.additional.fields[].key: "Certificate Alternate Name", event.idm.read_only_udm.additional.fields[].value.string_value: value of certificate.subject_altname
Mapped as an additional field.
certificate.subject_name
event.idm.read_only_udm.network.tls.server.certificate.subject
Directly mapped.
certificate.type
event.idm.read_only_udm.additional.fields[].key: "Certificate_Type", event.idm.read_only_udm.additional.fields[].value.string_value: value of certificate.type
Mapped as an additional field.
cipher
event.idm.read_only_udm.network.tls.cipher
Directly mapped.
client_asset_name
event.idm.read_only_udm.principal.application
Directly mapped.
client_asset_subnet
event.idm.read_only_udm.additional.fields[].key: "client_asset_subnet", event.idm.read_only_udm.additional.fields[].value.string_value: value of client_asset_subnet
Mapped as an additional field.
client_ip
event.idm.read_only_udm.principal.ip
Directly mapped.
client_port
event.idm.read_only_udm.principal.port
Directly mapped and converted to integer.
ClientIP
event.idm.read_only_udm.principal.ip
Directly mapped.
ClientPort
event.idm.read_only_udm.principal.port
Directly mapped and converted to integer.
ClientCountry
event.idm.read_only_udm.principal.location.country_or_region
Directly mapped if not "UNKNOWN" or empty string.
ClientAssetID
event.idm.read_only_udm.principal.asset_id
Prefixed with "Asset:" if not "0" or empty string.
ClientAssetName
event.idm.read_only_udm.principal.resource.attribute.labels[].key: "ClientAssetName", event.idm.read_only_udm.principal.resource.attribute.labels[].value: value of ClientAssetName
Mapped as a principal resource label.
ClientAssetRole
event.idm.read_only_udm.principal.asset.attribute.roles[].name
Directly mapped.
ClientAssetServices
event.idm.read_only_udm.principal.resource.attribute.labels[].key: "ClientAssetServices", event.idm.read_only_udm.principal.resource.attribute.labels[].value: value of ClientAssetServices
Mapped as a principal resource label.
Client
event.idm.read_only_udm.principal.resource.attribute.labels[].key: "Client", event.idm.read_only_udm.principal.resource.attribute.labels[].value: value of Client
Mapped as a principal resource label.
Collector
event.idm.read_only_udm.security_result.detection_fields[].key: "Collector", event.idm.read_only_udm.security_result.detection_fields[].value: value of Collector
Mapped as a detection field.
command
event.idm.read_only_udm.network.http.method
Directly mapped for HTTP events.
Command
event.idm.read_only_udm.security_result.detection_fields[].key: "Command", event.idm.read_only_udm.security_result.detection_fields[].value: value of Command
Mapped as a detection field.
Connection
event.idm.read_only_udm.security_result.detection_fields[].key: "Connection", event.idm.read_only_udm.security_result.detection_fields[].value: value of Connection
Mapped as a detection field.
DecodingPath
event.idm.read_only_udm.security_result.detection_fields[].key: "DecodingPath", event.idm.read_only_udm.security_result.detection_fields[].value: value of DecodingPath
Mapped as a detection field.
dest_country
event.idm.read_only_udm.target.location.country_or_region
Directly mapped.
dest_domain
event.idm.read_only_udm.target.hostname
Directly mapped.
dest_ip
event.idm.read_only_udm.target.ip
Directly mapped.
dest_port
event.idm.read_only_udm.target.port
Directly mapped and converted to integer.
Direction
event.idm.read_only_udm.security_result.detection_fields[].key: "Direction", event.idm.read_only_udm.security_result.detection_fields[].value: value of Direction
Mapped as a detection field.
dns.host
event.idm.read_only_udm.network.dns.questions[].name
Directly mapped for DNS events.
DomainName
event.idm.read_only_udm.target.administrative_domain
Directly mapped.
DomainAlexaRank
event.idm.read_only_udm.security_result.detection_fields[].key: "DomainAlexaRank", event.idm.read_only_udm.security_result.detection_fields[].value: value of DomainAlexaRank
Mapped as a detection field.
dport
event.idm.read_only_udm.target.port
Directly mapped and converted to integer.
dnsresolution.server_fqdn
event.idm.read_only_udm.target.hostname
Directly mapped.
Duration
event.idm.read_only_udm.security_result.detection_fields[].key: "Duration", event.idm.read_only_udm.security_result.detection_fields[].value: value of Duration
Mapped as a detection field.
Encrypted
event.idm.read_only_udm.security_result.detection_fields[].key: "Encrypted", event.idm.read_only_udm.security_result.detection_fields[].value: value of Encrypted
Mapped as a detection field.
Entropy
event.idm.read_only_udm.security_result.detection_fields[].key: "Entropy", event.idm.read_only_udm.security_result.detection_fields[].value: value of Entropy
Mapped as a detection field.
event.idm.read_only_udm.additional.fields
event.idm.read_only_udm.additional.fields
Contains various additional fields based on parser logic.
event.idm.read_only_udm.metadata.description
event.idm.read_only_udm.metadata.description
Directly mapped from summary field.
event.idm.read_only_udm.metadata.event_type
event.idm.read_only_udm.metadata.event_type
Determined based on various log fields and parser logic. Can be GENERIC_EVENT, NETWORK_CONNECTION, NETWORK_HTTP, NETWORK_SMTP, NETWORK_DNS, STATUS_UPDATE, NETWORK_FLOW.
event.idm.read_only_udm.metadata.log_type
event.idm.read_only_udm.metadata.log_type
Set to "FIDELIS_NETWORK".
event.idm.read_only_udm.metadata.product_name
event.idm.read_only_udm.metadata.product_name
Set to "FIDELIS_NETWORK".
event.idm.read_only_udm.metadata.vendor_name
event.idm.read_only_udm.metadata.vendor_name
Set to "FIDELIS_NETWORK".
event.idm.read_only_udm.network.application_protocol
event.idm.read_only_udm.network.application_protocol
Determined based on server_port or protocol field. Can be HTTP, HTTPS, SMTP, SSH, RPC, DNS, NFS, AOLMAIL.
event.idm.read_only_udm.network.direction
event.idm.read_only_udm.network.direction
Determined based on direction field or keywords in summary. Can be INBOUND or OUTBOUND.
event.idm.read_only_udm.network.dns.answers
event.idm.read_only_udm.network.dns.answers
Populated for DNS events.
event.idm.read_only_udm.network.dns.id
event.idm.read_only_udm.network.dns.id
Mapped from number field for DNS events.
event.idm.read_only_udm.network.dns.questions
event.idm.read_only_udm.network.dns.questions
Populated for DNS events.
event.idm.read_only_udm.network.email.from
event.idm.read_only_udm.network.email.from
Directly mapped from From if it's a valid email address.
event.idm.read_only_udm.network.email.subject
event.idm.read_only_udm.network.email.subject
Directly mapped from Subject.
event.idm.read_only_udm.network.email.to
event.idm.read_only_udm.network.email.to
Directly mapped from To.
event.idm.read_only_udm.network.ftp.command
event.idm.read_only_udm.network.ftp.command
Directly mapped from ftp.command.
event.idm.read_only_udm.network.http.method
event.idm.read_only_udm.network.http.method
Directly mapped from http.command or Command.
event.idm.read_only_udm.network.http.referral_url
event.idm.read_only_udm.network.http.referral_url
Directly mapped from Referer.
event.idm.read_only_udm.network.http.response_code
event.idm.read_only_udm.network.http.response_code
Directly mapped from http.status_code or StatusCode and converted to integer.
event.idm.read_only_udm.network.http.user_agent
event.idm.read_only_udm.network.http.user_agent
Directly mapped from http.useragent or UserAgent.
event.idm.read_only_udm.network.ip_protocol
event.idm.read_only_udm.network.ip_protocol
Directly mapped from tproto if it's TCP or UDP.
event.idm.read_only_udm.network.received_bytes
event.idm.read_only_udm.network.received_bytes
Renamed from event1.server_packet_count and converted to unsigned integer.
event.idm.read_only_udm.network.sent_bytes
event.idm.read_only_udm.network.sent_bytes
Renamed from event1.client_packet_count and converted to unsigned integer.
event.idm.read_only_udm.network.session_duration.seconds
event.idm.read_only_udm.network.session_duration.seconds
Renamed from event1.session_size and converted to integer.
event.idm.read_only_udm.network.session_id
event.idm.read_only_udm.network.session_id
Directly mapped from event1.rel_sesid or UserSessionID.
event.idm.read_only_udm.network.tls.client.certificate.issuer
event.idm.read_only_udm.network.tls.client.certificate.issuer
Directly mapped from event1.certificate_issuer_name.
event.idm.read_only_udm.network.tls.client.certificate.not_after
event.idm.read_only_udm.network.tls.client.certificate.not_after
Parsed from event1.certificate_end_date and converted to timestamp.
event.idm.read_only_udm.network.tls.client.certificate.not_before
event.idm.read_only_udm.network.tls.client.certificate.not_before
Parsed from event1.certificate_start_date and converted to timestamp.
event.idm.read_only_udm.network.tls.client.certificate.subject
event.idm.read_only_udm.network.tls.client.certificate.subject
Directly mapped from event1.certificate_subject_name.
event.idm.read_only_udm.network.tls.client.ja3
event.idm.read_only_udm.network.tls.client.ja3
Directly mapped from event1.ja3digest and converted to string.
event.idm.read_only_udm.network.tls.cipher
event.idm.read_only_udm.network.tls.cipher
Directly mapped from event1.cipher, CipherSuite, cipher, or event1.tls_ciphersuite.
event.idm.read_only_udm.network.tls.server.certificate.issuer
event.idm.read_only_udm.network.tls.server.certificate.issuer
Directly mapped from certificate_issuer_name.
event.idm.read_only_udm.network.tls.server.certificate.subject
event.idm.read_only_udm.network.tls.server.certificate.subject
Directly mapped from certificate_subject_name.
event.idm.read_only_udm.network.tls.server.ja3s
event.idm.read_only_udm.network.tls.server.ja3s
Directly mapped from event1.ja3sdigest and converted to string.
event.idm.read_only_udm.network.tls.version
event.idm.read_only_udm.network.tls.version
Directly mapped from event1.version.
event.idm.read_only_udm.principal.application
event.idm.read_only_udm.principal.application
Directly mapped from event1.client_asset_name.
event.idm.read_only_udm.principal.asset.attribute.roles[].name
event.idm.read_only_udm.principal.asset.attribute.roles[].name
Directly mapped from ClientAssetRole.
event.idm.read_only_udm.principal.asset_id
event.idm.read_only_udm.principal.asset_id
Directly mapped from ClientAssetID or ServerAssetID (prefixed with "Asset:").
event.idm.read_only_udm.principal.hostname
event.idm.read_only_udm.principal.hostname
Directly mapped from event1.sld or src_domain.
event.idm.read_only_udm.principal.ip
event.idm.read_only_udm.principal.ip
Directly mapped from event1.src_ip6, client_ip, or ClientIP.
event.idm.read_only_udm.principal.location.country_or_region
event.idm.read_only_udm.principal.location.country_or_region
Directly mapped from ClientCountry or src_country if not "UNKNOWN" or empty string.
event.idm.read_only_udm.principal.port
event.idm.read_only_udm.principal.port
Directly mapped from event1.sport or client_port and converted to integer.
event.idm.read_only_udm.principal.resource.attribute.labels
event.idm.read_only_udm.principal.resource.attribute.labels
Contains various labels based on parser logic.
event.idm.read_only_udm.principal.user.userid
event.idm.read_only_udm.principal.user.userid
Directly mapped from ftp.user or AppUser.
event.idm.read_only_udm.security_result.action
event.idm.read_only_udm.security_result.action
Determined based on severity. Can be ALLOW, BLOCK, or UNKNOWN_ACTION.
event.idm.read_only_udm.security_result.action_details
event.idm.read_only_udm.security_result.action_details
Directly mapped from Action if not "none" or empty string.
event.idm.read_only_udm.security_result.category
event.idm.read_only_udm.security_result.category
Set to NETWORK_SUSPICIOUS if malware_type is present.
event.idm.read_only_udm.security_result.detection_fields
event.idm.read_only_udm.security_result.detection_fields
Contains various detection fields based on parser logic.
event.idm.read_only_udm.security_result.rule_name
event.idm.read_only_udm.security_result.rule_name
Directly mapped from rule_name.
event.idm.read_only_udm.security_result.severity
event.idm.read_only_udm.security_result.severity
Determined based on severity. Can be INFORMATIONAL, MEDIUM, ERROR, or CRITICAL.
event.idm.read_only_udm.security_result.summary
event.idm.read_only_udm.security_result.summary
Directly mapped from label.
event.idm.read_only_udm.security_result.threat_name
event.idm.read_only_udm.security_result.threat_name
Directly mapped from malware_type or parsed from summary if it contains "CVE-".
event.idm.read_only_udm.target.administrative_domain
event.idm.read_only_udm.target.administrative_domain
Directly mapped from DomainName.
event.idm.read_only_udm.target.asset.attribute.roles[].name
event.idm.read_only_udm.target.asset.attribute.roles[].name
Directly mapped from ServerAssetRole.
event.idm.read_only_udm.target.file.full_path
event.idm.read_only_udm.target.file.full_path
Directly mapped from ftp.filename or Filename.
event.idm.read_only_udm.target.file.md5
event.idm.read_only_udm.target.file.md5
Directly mapped from event1.md5 or md5.
event.idm.read_only_udm.target.file.mime_type
event.idm.read_only_udm.target.file.mime_type
Directly mapped from event1.filetype.
event.idm.read_only_udm.target.file.sha1
event.idm.read_only_udm.target.file.sha1
Directly mapped from event1.srvcerthash.
event.idm.read_only_udm.target.file.sha256
event.idm.read_only_udm.target.file.sha256
Directly mapped from event1.sha256 or sha256.
event.idm.read_only_udm.target.file.size
event.idm.read_only_udm.target.file.size
Renamed from event1.filesize and converted to unsigned integer if not 0.
event.idm.read_only_udm.target.hostname
event.idm.read_only_udm.target.hostname
Directly mapped from event1.sni, dest_domain, or Host.
event.idm.read_only_udm.target.ip
event.idm.read_only_udm.target.ip
Directly mapped from event1.dst_ip6 or server_ip or ServerIP.
event.idm.read_only_udm.target.location.country_or_region
event.idm.read_only_udm.target.location.country_or_region
Directly mapped from dest_country or ServerCountry.
event.idm.read_only_udm.target.platform
event.idm.read_only_udm.target.platform
Mapped from asset_os after normalization.
event.idm.read_only_udm.target.platform_version
event.idm.read_only_udm.target.platform_version
Directly mapped from os_version.
event.idm.read_only_udm.target.port
event.idm.read_only_udm.target.port
Directly mapped from event1.dport or server_port and converted to integer.
event.idm.read_only_udm.target.resource.attribute.labels
event.idm.read_only_udm.target.resource.attribute.labels
Contains various labels based on parser logic.
event.idm.read_only_udm.target.url
event.idm.read_only_udm.target.url
Directly mapped from url or URL.
event.idm.read_only_udm.target.user.product_object_id
event.idm.read_only_udm.target.user.product_object_id
Directly mapped from uuid.
event1.certificate_end_date
event.idm.read_only_udm.network.tls.client.certificate.not_after
Parsed and converted to timestamp.
event1.certificate_extended_key_usage
event.idm.read_only_udm.additional.fields[].key: "Extended Key Usage", event.idm.read_only_udm.additional.fields[].value.string_value: value of event1.certificate_extended_key_usage
Mapped as an additional field.
event1.certificate_issuer_name
event.idm.read_only_udm.network.tls.client.certificate.issuer
Directly mapped.
event1.certificate_key_length
event.idm.read_only_udm.additional.fields[].key: "Key Length", event.idm.read_only_udm.additional.fields[].value.string_value: value of event1.certificate_key_length
Mapped as an additional field.
event1.certificate_key_usage
event.idm.read_only_udm.additional.fields[].key: "Key Usage", event.idm.read_only_udm.additional.fields[].value.string_value: value of event1.certificate_key_usage
Mapped as an additional field.
event1.certificate_start_date
event.idm.read_only_udm.network.tls.client.certificate.not_before
Parsed and converted to timestamp.
event1.certificate_subject_altname
event.idm.read_only_udm.additional.fields[].key: "Certificate Alternate Name", event.idm.read_only_udm.additional.fields[].value.string_value: value of event1.certificate_subject_altname
Mapped as an additional field.
event1.certificate_subject_name
event.idm.read_only_udm.network.tls.client.certificate.subject
Directly mapped.
event1.client_asset_name
event.idm.read_only_udm.principal.application
Directly mapped.
event1.client_asset_subnet
event.idm.read_only_udm.additional.fields[].key: "client_asset_subnet", event.idm.read_only_udm.additional.fields[].value.string_value: value of event1.client_asset_subnet
Mapped as an additional field.
event1.client_packet_count
event.idm.read_only_udm.network.sent_bytes
Converted to unsigned integer and renamed.
event1.cipher
event.idm.read_only_udm.network.tls.cipher
Directly mapped.
event1.direction
event.idm.read_only_udm.network.direction
Mapped to INBOUND if "s2c" or OUTBOUND if "c2s".
event1.d
Need more help?
Get answers from Community members and Google SecOps professionals.
