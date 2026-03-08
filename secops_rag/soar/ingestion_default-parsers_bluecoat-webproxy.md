# Collect Blue Coat ProxySG logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecoat-webproxy/  
**Scraped:** 2026-03-05T09:51:29.649490Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Blue Coat ProxySG logs
Supported in:
Google secops
SIEM
This document explains how to ingest Blue Coat ProxySG logs to
Google Security Operations using Bindplane. The parser handles Blue Coat web proxy
logs, supporting SYSLOG+JSON and SYSLOG+KV formats. It uses a series of
conditional checks and grok patterns to identify the log format, extracts
relevant fields, and maps them to the Unified Data Model (UDM), handling various 
log structures and edge cases.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to Blue Coat ProxySG
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
For additional installation options, consult the
installation guide
.
Configure the Bindlane agent to ingest Syslog and send to Google SecOps
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
tcplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:5145"
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
'BLUECOAT_WEBPROXY'
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
tcplog
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
Configure Syslog in Blue Coat ProxySG
Sign in to the
Blue Coat ProxySG
management console.
Go to
Maintenance
>
Event Logging
>
Syslog
.
Click
New
.
Provide the following configuration details:
Loghost
: Enter the Bindplane agent IP address.
Click
OK
.
Select the
Enable Syslog
checkbox.
Select
Level
.
Select the
Verbose
checkbox.
Click
Apply
.
Configure a Custom Client in Blue Coat ProxySG
Go to
Configuration
>
Access Logging
>
Logs
>
Upload Client
.
Select
Streaming
in the Log list.
Select
Custom Client
from the Client type list.
Click
Settings
.
Select to configure the
primary
or
alternate
custom server from the
Settings
list.
Provide the following configuration details:
Host
: Enter the hostname or IP address of the upload destination.
Port
: Set to
514
.
Use secure connections (SSL): Set to
Off
.
Click
OK
.
Click
Apply
to return to the
Upload Client
tab.
For each log format you want to use among main, im, and streaming, complete the following steps:
Select the
log
.
Assign the
Upload Client
to be the
Custom
client.
Select
<No Encryption>
and
<No Signing>
.
Save the log file as a text file.
Click
Upload Schedule
>
Upload Type
.
Select
Continuously
for
Upload the access log
to stream the access logs.
Click
OK
.
Click
Apply
.
UDM mapping table
Log Field
UDM Mapping
Logic
@timestamp
metadata.event_timestamp
The timestamp of the event as recorded by the Blue Coat appliance.  Parsed from the JSON data.
application-name
target.application
The name of the application associated with the network traffic. Parsed from the JSON data.
c-ip
principal.asset.ip
principal.ip
Client IP address. Parsed from the JSON data.
c_ip
principal.ip
principal.asset.ip
Client IP address. Parsed from various log formats.
c_ip_host
principal.hostname
principal.asset.hostname
Client hostname, if available. Parsed from the JSON data.
cs-auth-group
principal_user_group_identifiers
Client authentication group. Parsed from the JSON data.
cs-bytes
network.sent_bytes
Number of bytes sent by the client. Parsed from the JSON data.
cs-categories
security_result.category_details
Categories assigned to the web request by the Blue Coat appliance. Parsed from the JSON data.
cs-host
target_hostname
Hostname requested by the client. Parsed from the JSON data.
cs-icap-error-details
security_result.detection_fields
ICAP error details from the client side. Parsed from the JSON data, key is "cs-icap-error-details".
cs-icap-status
security_result.description
ICAP status from the client side. Parsed from the JSON data.
cs-method
network.http.method
HTTP method used in the request. Parsed from the JSON data.
cs-threat-risk
security_result.risk_score
Threat risk score assigned by the Blue Coat appliance. Parsed from the JSON data.
cs-uri-extension
cs_uri_extension
Extension of the requested URI. Parsed from the JSON data.
cs-uri-path
_uri_path
Path of the requested URI. Parsed from the JSON data.
cs-uri-port
cs_uri_port
Port of the requested URI. Parsed from the JSON data.
cs-uri-query
_uri_query
Query string of the requested URI. Parsed from the JSON data.
cs-uri-scheme
_uri_scheme
Scheme of the requested URI (e.g., http, https). Parsed from the JSON data.
cs-userdn
principal_user_userid
Client username. Parsed from the JSON data.
cs-version
cs_version
HTTP version used by the client. Parsed from the JSON data.
cs(Referer)
network.http.referral_url
Referrer URL. Parsed from the JSON data.
cs(User-Agent)
network.http.user_agent
User-agent string. Parsed from the JSON data.
cs(X-Requested-With)
security_result.detection_fields
Value of the X-Requested-With header. Parsed from the JSON data, key is "cs-X-Requested-With".
cs_auth_group
principal_user_group_identifiers
Client authentication group. Parsed from various log formats.
cs_bytes
network.sent_bytes
Number of bytes sent by the client. Parsed from various log formats.
cs_categories
security_result.category_details
Categories assigned to the web request. Parsed from various log formats.
cs_host
target_hostname
Hostname requested by the client. Parsed from various log formats.
cs_method
network.http.method
HTTP method used in the request. Parsed from various log formats.
cs_referer
network.http.referral_url
Referrer URL. Parsed from various log formats.
cs_threat_risk
security_result.risk_score
Threat risk score assigned by the Blue Coat appliance. Parsed from the KV log format.
cs_uri
target.url
Full requested URI. Parsed from the KV log format.
cs_uri_extension
cs_uri_extension
Extension of the requested URI. Parsed from the KV log format.
cs_uri_path
_uri_path
Path of the requested URI. Parsed from various log formats.
cs_uri_port
target_port
Port of the requested URI. Parsed from various log formats.
cs_uri_query
_uri_query
Query string of the requested URI. Parsed from various log formats.
cs_uri_scheme
_uri_scheme
Scheme of the requested URI (e.g., http, https). Parsed from various log formats.
cs_user
principal_user_userid
Client username. Parsed from the general log format.
cs_user_agent
network.http.user_agent
User-agent string. Parsed from various log formats.
cs_username
principal_user_userid
Client username. Parsed from various log formats.
cs_x_forwarded_for
_intermediary.ip
X-Forwarded-For header value. Parsed from the general log format.
deviceHostname
_intermediary.hostname
Hostname of the Blue Coat appliance. Parsed from the KV log format.
dst
ip_target
Destination IP address. Parsed from the KV log format.
dst_ip
ip_target
Destination IP address. Parsed from the SSL log format.
dst_user
target.user.userid
Destination user ID. Parsed from the Proxy Reverse log format.
dstport
target_port
Destination port. Parsed from the KV log format.
dstport
target.port
Destination port. Parsed from the SSL log format.
exception-id
_block_reason
Exception ID, indicating a blocked request. Parsed from the KV log format.
filter-category
_categories
Category of the filter that triggered the event. Parsed from the KV log format.
filter-result
_policy_action
Result of the filter applied to the request. Parsed from the KV log format.
hostname
principal.hostname
principal.asset.hostname
Hostname of the device generating the log. Parsed from the SSL and general log formats.
isolation-url
isolation-url
URL related to isolation, if applicable. Parsed from the JSON data.
ma-detonated
ma-detonated
Malware detonation status. Parsed from the JSON data.
page-views
page-views
Number of page views. Parsed from the JSON data.
r-ip
ip_target
Remote IP address. Parsed from the JSON data.
r-supplier-country
r-supplier-country
Country of the remote supplier. Parsed from the JSON data.
r_dns
target_hostname
Remote DNS name. Parsed from the JSON data.
r_ip
ip_target
Remote IP address. Parsed from various log formats.
r_port
target_port
Remote port. Parsed from the JSON data.
risk-groups
security_result.detection_fields
Risk groups associated with the event. Parsed from the JSON data, key is "risk-groups".
rs-icap-error-details
security_result.detection_fields
ICAP error details from the remote server side. Parsed from the JSON data, key is "rs-icap-error-details".
rs-icap-status
rs-icap-status
ICAP status from the remote server side. Parsed from the JSON data.
rs(Content-Type)
target.file.mime_type
Content-type of the response from the remote server. Parsed from the KV log format.
rs_content_type
target.file.mime_type
Content-type of the response from the remote server. Parsed from various log formats.
rs_server
rs_server
Remote server information. Parsed from the JSON data.
rs_status
_network.http.response_code
Response status code from the remote server. Parsed from the JSON data.
r_supplier_country
intermediary.location.country_or_region
Country of the remote supplier. Parsed from the general log format.
r_supplier_ip
intermediary.ip
IP address of the remote supplier. Parsed from the general log format.
s-action
_metadata.product_event_type
Action taken by the proxy. Parsed from the KV log format.
s-ip
_intermediary.ip
Server IP address. Parsed from the KV log format.
s-source-ip
_intermediary.ip
Source IP address of the server. Parsed from the JSON data.
s_action
_metadata.product_event_type
Action taken by the proxy. Parsed from various log formats.
s_ip
target.ip
target.asset.ip
Server IP address. Parsed from various log formats.
s_ip_host
_intermediary.hostname
Server hostname. Parsed from the JSON data.
s-supplier-country
intermediary.location.country_or_region
Country of the supplier server. Parsed from the JSON data.
s-supplier-failures
security_result.detection_fields
Supplier failures. Parsed from the JSON data, key is "s-supplier-failures".
s-supplier-ip
_intermediary.ip
Supplier server IP address. Parsed from the JSON data.
s_supplier_ip
intermediary.ip
Supplier server IP address. Parsed from the JSON data.
s_supplier_name
_intermediary.hostname
Supplier server name. Parsed from the general log format.
sc-bytes
network.received_bytes
Number of bytes received by the server. Parsed from the KV log format.
sc-filter-result
_policy_action
Filter result from the server side. Parsed from the KV log format.
sc-status
_network.http.response_code
Status code returned by the server. Parsed from the KV log format.
sc_bytes
network.received_bytes
Number of bytes received by the server. Parsed from various log formats.
sc_connection
sc_connection
Server connection information. Parsed from the general log format.
sc_filter_result
_policy_action
Filter result from the server side. Parsed from various log formats.
sc_status
_network.http.response_code
Status code returned by the server. Parsed from various log formats.
search_query
target.resource.attribute.labels
Search query, if present in the URL. Extracted from
target_url
, key is "search_query".
session_id
network.session_id
Session ID. Parsed from the Proxy Reverse log format.
src
ip_principal
Source IP address. Parsed from the KV log format.
src_hostname
principal.hostname
principal.asset.hostname
Source hostname. Parsed from the general log format.
src_ip
ip_principal
Source IP address. Parsed from the SSL log format.
srcport
principal_port
Source port. Parsed from the KV log format.
src_port
principal.port
Source port. Parsed from the SSL log format.
s_source_port
intermediary.port
Source port of the server. Parsed from the general log format.
summary
security_result.summary
Summary of the security result. Parsed from the Proxy Reverse and SSL log formats.
syslogtimestamp
syslogtimestamp
Syslog timestamp. Parsed from the KV log format.
target_application
target.application
Application targeted by the request. Derived from
x_bluecoat_application_name
or
application-name
.
target_hostname
target.hostname
target.asset.hostname
Target hostname. Derived from
r_dns
,
cs-host
, or other fields depending on the log format.
target_port
target.port
Target port. Derived from
r_port
,
cs_uri_port
, or
dstport
depending on the log format.
target_sip
target.ip
target.asset.ip
Target server IP address. Parsed from the general log format.
target_url
target.url
Target URL. Derived from
target_hostname
,
_uri_path
, and
_uri_query
or
cs_uri
.
time-taken
network.session_duration
Duration of the session or request. Parsed from the KV log format and converted to seconds and nanoseconds.
time_taken
network.session_duration
Duration of the session or request. Parsed from various log formats and converted to seconds and nanoseconds.
tls_version
network.tls.version
TLS version used in the connection. Parsed from the SSL log format.
upload-source
upload-source
Source of the upload. Parsed from the JSON data.
username
principal_user_userid
Username. Parsed from the KV log format.
verdict
security_result.detection_fields
Verdict of the security analysis. Parsed from the JSON data, key is "verdict".
wf-env
wf_env
Environment of the web filtering service. Parsed from the JSON data.
wf_id
security_result.detection_fields
Web filtering ID. Parsed from the JSON data, key is "wf_id".
wrong_cs_host
principal.hostname
principal.asset.hostname
Incorrectly parsed client hostname, used as principal hostname if it's not an IP address. Parsed from the general log format.
x-bluecoat-access-type
x-bluecoat-access-type
Type of access. Parsed from the JSON data.
x-bluecoat-appliance-name
intermediary.application
Name of the Blue Coat appliance. Parsed from the JSON data.
x-bluecoat-application-name
target_application
Name of the application. Parsed from the JSON data.
x-bluecoat-application-operation
x_bluecoat_application_operation
Application operation. Parsed from the JSON data.
x-bluecoat-location-id
x-bluecoat-location-id
Location ID. Parsed from the JSON data.
x-bluecoat-location-name
x-bluecoat-location-name
Location name. Parsed from the JSON data.
x-bluecoat-placeholder
security_result.detection_fields
Placeholder information. Parsed from the JSON data, key is "x-bluecoat-placeholder".
x-bluecoat-reference-id
security_result.detection_fields
Reference ID. Parsed from the JSON data, key is "x-bluecoat-reference-id".
x-bluecoat-request-tenant-id
x-bluecoat-request-tenant-id
Tenant ID of the request. Parsed from the JSON data.
x-bluecoat-transaction-uuid
metadata.product_log_id
Transaction UUID. Parsed from the JSON data.
x-client-agent-sw
software.name
Client agent software. Parsed from the JSON data and merged into
principal.asset.software
.
x-client-agent-type
principal.application
Client agent type. Parsed from the JSON data.
x-client-device-id
principal.resource.product_object_id
Client device ID. Parsed from the JSON data.
x-client-device-name
x-client-device-name
Client device name. Parsed from the JSON data.
x-client-device-type
x-client-device-type
Client device type. Parsed from the JSON data.
x-client-os
principal.asset.platform_software.platform
Client operating system. Parsed from the JSON data. If contains "Windows", sets platform to WINDOWS.
x-client-security-posture-details
x-client-security-posture-details
Client security posture details. Parsed from the JSON data.
x-client-security-posture-risk-score
security_result.detection_fields
Client security posture risk score. Parsed from the JSON data, key is "x-client-security-posture-risk-score".
x-cloud-rs
security_result.detection_fields
Cloud-related remote server information. Parsed from the JSON data, key is "x-cloud-rs".
x-cs-certificate-subject
x_cs_certificate_subject
Certificate subject from the client side. Parsed from the JSON data.
x-cs-client-ip-country
x-cs-client-ip-country
Client IP country. Parsed from the JSON data.
x-cs-connection-negotiated-cipher
network.tls.cipher
Negotiated cipher from the client side. Parsed from the JSON data.
x-cs-connection-negotiated-cipher-size
security_result.detection_fields
Negotiated cipher size from the client side. Parsed from the JSON data, key is "x-cs-connection-negotiated-cipher-size".
x-cs-connection-negotiated-ssl-version
network.tls.version_protocol
Negotiated SSL version from the client side. Parsed from the JSON data.
x-cs-ocsp-error
security_result.detection_fields
OCSP error from the client side. Parsed from the JSON data, key is "x-cs-ocsp-error".
x-cs(referer)-uri-categories
x-cs(referer)-uri-categories
Referrer URI categories from the client side. Parsed from the JSON data.
x-data-leak-detected
security_result.detection_fields
Data leak detection status. Parsed from the JSON data, key is "x-data-leak-detected".
x-exception-id
x_exception_id
Exception ID. Parsed from the JSON data.
x-http-connect-host
x-http-connect-host
HTTP connect host. Parsed from the JSON data.
x-http-connect-port
x-http-connect-port
HTTP connect port. Parsed from the JSON data.
x-icap-reqmod-header(x-icap-metadata)
x_icap_reqmod_header
ICAP request modification header containing metadata. Parsed from the JSON data.
x-icap-respmod-header(x-icap-metadata)
x_icap_respmod_header
ICAP response modification header containing metadata. Parsed from the JSON data.
x-rs-certificate-hostname
network.tls.client.server_name
Certificate hostname from the remote server side. Parsed from the JSON data.
x-rs-certificate-hostname-categories
x_rs_certificate_hostname_category
Certificate hostname categories from the remote server side. Parsed from the JSON data.
x-rs-certificate-hostname-category
x_rs_certificate_hostname_category
Certificate hostname category from the remote server side. Parsed from the JSON data.
x-rs-certificate-hostname-threat-risk
security_result.detection_fields
Certificate hostname threat risk from the remote server side. Parsed from the JSON data, key is "x-rs-certificate-hostname-threat-risk".
x-rs-certificate-observed-errors
x_rs_certificate_observed_errors
Certificate observed errors from the remote server side. Parsed from the JSON data.
x-rs-certificate-validate-status
network.tls.server.certificate.subject
Certificate validation status from the remote server side. Parsed from the JSON data.
x-rs-connection-negotiated-cipher
x_rs_connection_negotiated_cipher
Negotiated cipher from the remote server side. Parsed from the JSON data.
x-rs-connection-negotiated-cipher-size
security_result.detection_fields
Negotiated cipher size from the remote server side. Parsed from the JSON data, key is "x-rs-connection-negotiated-cipher-size".
x-rs-connection-negotiated-cipher-strength
x_rs_connection_negotiated_cipher_strength
Negotiated cipher strength from the remote server side. Parsed from the JSON data.
x-rs-connection-negotiated-ssl-version
x_rs_connection_negotiated_ssl_version
Negotiated SSL version from the remote server side. Parsed from the JSON data.
x-rs-ocsp-error
x_rs_ocsp_error
OCSP error from the remote server side. Parsed from the JSON data.
x-sc-connection-issuer-keyring
security_result.detection_fields
Connection issuer key ring. Parsed from the JSON data, key is "x-sc-connection-issuer-keyring".
x-sc-connection-issuer-keyring-alias
x-sc-connection-issuer-keyring-alias
Connection issuer key ring alias. Parsed from the JSON data.
x-sr-vpop-country
principal.location.country_or_region
VPOP country. Parsed from the JSON data.
x-sr-vpop-country-code
principal.location.country_or_region
VPOP country code. Parsed from the JSON data.
x-sr-vpop-ip
principal.ip
principal.asset.ip
VPOP IP address. Parsed from the JSON data.
x-symc-dei-app
x-symc-dei-app
Symantec DEI application. Parsed from the JSON data.
x-symc-dei-via
security_result.detection_fields
Symantec DEI via. Parsed from the JSON data, key is "x-symc-dei-via".
x-tenant-id
security_result.detection_fields
Tenant ID. Parsed from the JSON data, key is "x-tenant-id".
x-timestamp-unix
x-timestamp-unix
Unix timestamp. Parsed from the JSON data.
x_bluecoat_application_name
target_application
Application name. Parsed from various log formats.
x_bluecoat_application_operation
x_bluecoat_application_operation
Application operation. Parsed from various log formats.
x_bluecoat_transaction_uuid
metadata.product_log_id
Transaction UUID. Parsed from various log formats.
x_cs_certificate_subject
x_cs_certificate_subject
Client-side certificate subject. Parsed from the general log format.
x_cs_client_effective_ip
ip_principal
Client's effective IP address. Parsed from the general log format.
x_cs_connection_negotiated_cipher
network.tls.cipher
Client-side negotiated cipher. Parsed from the general log format.
x_cs_connection_negotiated_ssl_version
network.tls.version_protocol
Client-side negotiated SSL version. Parsed from the general log format.
x_exception_id
_block_reason
Exception ID. Parsed from various log formats.
x_icap_reqmod_header
x_icap_reqmod_header
ICAP request modification header. Parsed from the general log format.
x_icap_respmod_header
x_icap_respmod_header
ICAP response modification header. Parsed from the general log format.
x_rs_certificate_hostname
network.tls.client.server_name
Remote server certificate hostname. Parsed from the general log format.
x_rs_certificate_hostname_category
x_rs_certificate_hostname_category
Remote server certificate hostname category. Parsed from the general log format.
x_rs_certificate_observed_errors
x_rs_certificate_observed_errors
Remote server certificate observed errors. Parsed from the general log format.
x_rs_certificate_validate_status
network.tls.server.certificate.subject
Remote server certificate validation status. Parsed from various log formats.
x_rs_connection_negotiated_cipher_strength
x_rs_connection_negotiated_cipher_strength
Remote server negotiated cipher strength. Parsed from the general log format.
x_rs_connection_negotiated_ssl_version
x_rs_connection_negotiated_ssl_version
Remote server negotiated SSL version. Parsed from the general log format.
x_virus_id
security_result.detection_fields
Virus ID. Parsed from various log formats, key is "x-virus-id".
Derived Fields (from parser logic):
metadata.event_type
: Determined based on a complex set of conditions involving fields like
network.application_protocol
,
network.http.method
,
principal.*
,
target.*
, and
dst_user
.
metadata.vendor_name
: Static value:
Blue Coat Systems
.
metadata.product_name
: Static value:
ProxySG
.
metadata.log_type
: Static value:
BLUECOAT_WEBPROXY
.
principal.asset.platform_software.platform
: Set to
WINDOWS
if
x-client-os
contains
Windows
.
network.application_protocol
: Determined using a lookup table based on
_uri_scheme
or
target.port
. Defaults to
UNKNOWN_APPLICATION_PROTOCOL
.
network.ip_protocol
: Determined using a lookup table based on
_uri_scheme
. Defaults to
UNKNOWN_IP_PROTOCOL
.
security_result.action
: Determined based on
_policy_action
(
OBSERVED
->
ALLOW
,
DENIED
->
BLOCK
).
security_result.about.labels
: Contains labels derived from various fields like
rs_server
,
communication_type
, and the status from the SSL log format.
security_result.detection_fields
: Contains various key-value pairs derived from fields like
x_virus_id
,
x_rs_certificate_observed_errors
,
x_rs_connection_negotiated_cipher_strength
, and many others.
vulns.vulnerabilities
: Populated from the
proxy_reverse_info
field if present, containing vulnerability information like
cve_id
and
about.labels
.
Need more help?
Get answers from Community members and Google SecOps professionals.
