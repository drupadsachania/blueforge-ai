# Collect Nutanix Prism logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nutanix-prism/  
**Scraped:** 2026-03-05T09:27:00.541589Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Nutanix Prism logs
Supported in:
Google secops
SIEM
Overview
This parser processes Nutanix Prism logs, handling both JSON and syslog formats. It extracts fields from various log structures, normalizes them into UDM, and enriches the data with additional context like user information, network details, and security severity. The parser also performs specific actions based on the HTTP method and log level, categorizing events into UDM event types like
USER_LOGIN
,
STATUS_UPDATE
, and
GENERIC_EVENT
.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have privileged access to Nutanix Prism Central.
Ensure that you have a Windows 2012 SP2 or later or Linux host with systemd.
If running behind a proxy, ensure the firewall
ports
are open.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
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
Install Bindplane Agent
For
Windows installation
, run the following script:
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
.
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
.
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane Agent is installed.
Edit the
config.yaml
file as follows:
receivers:
  tcplog:
    # Replace the below port <54525> and IP (0.0.0.0) with your specific values
    listen_address: "0.0.0.0:54525" 

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        # Adjust the creds location below according the placement of the credentials file you downloaded
        creds: '{ json file for creds }'
        # Replace <customer_id> below with your actual ID that you copied
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        # You can apply ingestion labels below as preferred
        ingestion_labels:
        log_type: SYSLOG
        namespace: Namespace
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart Bindplane Agent to apply the changes using the following command:
sudo systemctl bindplane restart
Exporting Syslog from Nutanix Prism
Sign in to Prism Central using privileged account.
Select
Prism Central Settings
from the menu.
Go to
Syslog Server
.
Click
+ Configure Syslog Server
.
Specify values for the input parameters in the
Syslog Servers
dialog:
Server Name
: Enter a name for the server (for example,
Google SecOps Bindplane Server
)
IP Address
: Enter the IP of your Bindplane Agent.
Port
: Enter the port on which Bindplane Agent is listening.
Transport Protocol
: Select
TCP
.
Click
Configure
.
Click
+ Edit
on the
Data Sources
option.
Specify values for the input parameters in the
Data Sources and Respective Severity Level
dialog:
Select
API Audit
,
Audit
and
Flow
.
Set Severity Level for each at
6 - Informational
.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
@timestamp
metadata.event_timestamp
The event timestamp is parsed from the
@timestamp
field. Formats
yyyy-MM-dd HH:mm:ss.SSS
,
yyyy-MM-ddTHH:mm:ssZ
, and
ISO8601
are supported.
agent.id
observer.asset_id
Combined with
agent.type
to form the observer asset ID in the format "agent.type:agent.id".
agent.type
observer.application
The application used for observation.
agent.version
observer.platform_version
The version of the observer application.
alertUid
security_result.detection_fields.value
The value of the alert UID is mapped to the
value
field within
detection_fields
. The
key
is set to "Alert Uid".
api_version
metadata.product_version
The API version.
clientIp
principal.ip
,
principal.asset.ip
Client IP address.
client_type
principal.labels.value
The value of the client type. The
key
is set to "client_type".
defaultMsg
metadata.description
The default message.
entity_uuid
metadata.product_log_id
Entity UUID.
http_method
network.http.method
The HTTP method. Converted to uppercase.
host.architecture
principal.asset.hardware.cpu_platform
The architecture of the host.
host.id
principal.asset_id
Prefixed with "NUTANIX:" to create the principal asset ID.
host.ip
principal.ip
,
principal.asset.ip
Host IP address.
host.mac
principal.mac
Host MAC address.
host.os.kernel
principal.platform_patch_level
The kernel version of the host operating system.
host.os.platform
principal.platform
The platform of the host operating system. Mapped to
LINUX
,
WINDOWS
,
MAC
, or
UNKNOWN_PLATFORM
.
host.os.version
principal.platform_version
The version of the host operating system.
input.type
network.ip_protocol
The network protocol. Mapped to "UDP" or "TCP".
log.source.address
principal.ip
,
principal.asset.ip
,
principal.port
Parsed to extract the source IP and port.
logstash.collect.host
observer.ip
The IP address of the logstash collector.
logstash.collect.timestamp
metadata.collected_timestamp
The timestamp when the log was collected.
logstash.ingest.host
intermediary.hostname
The hostname of the logstash ingest server.
logstash.ingest.timestamp
metadata.ingested_timestamp
The timestamp when the log was ingested.
logstash.irm_environment
principal.labels.value
The value of the irm environment. The
key
is set to "irm_environment".
logstash.irm_region
principal.labels.value
The value of the irm region. The
key
is set to "irm_region".
logstash.irm_site
principal.labels.value
The value of the irm site. The
key
is set to "irm_site".
logstash.process.host
intermediary.hostname
The hostname of the logstash processing server.
operationType
metadata.product_event_type
The operation type.
originatingClusterUuid
additional.fields.value.string_value
The originating cluster UUID. The
key
is set to "Originating Cluster Uuid".
params.mac_address
target.mac
The MAC address from the parameters.
params.requested_ip_address
target.ip
,
target.asset.ip
The requested IP address from the parameters.
params.vm_name
target.resource.name
The VM name from the parameters.
program
metadata.product_event_type
The program name.
rest_endpoint
target.url
The REST endpoint.
sessionId
additional.fields.value.string_value
The session ID. The
key
is set to "Session ID".
syslog_host
principal.hostname
,
principal.asset.hostname
Syslog host.
timestamp
metadata.event_timestamp
The event timestamp.
username
principal.user.user_display_name
or
principal.user.userid
Username. Used as user ID if
http_method
is "POST".
uuid
metadata.product_log_id
UUID.
N/A
metadata.vendor_name
Hardcoded to "Nutanix_Prism".
N/A
metadata.product_name
Hardcoded to "Nutanix_Prism".
N/A
metadata.event_type
Determined by parser logic based on the values of
has_principal
,
has_target
,
audit_log
,
network_set
, and
http_method
. Can be
GENERIC_EVENT
,
USER_LOGIN
,
STATUS_UPDATE
,
USER_RESOURCE_ACCESS
,
RESOURCE_CREATION
,
USER_RESOURCE_UPDATE_CONTENT
, or
USER_RESOURCE_DELETION
.
N/A
metadata.log_type
Hardcoded to "NUTANIX_PRISM".
N/A
extensions.auth.type
Set to "AUTHTYPE_UNSPECIFIED" if
metadata.event_type
is
USER_LOGIN
.
N/A
security_result.severity
Determined by parser logic based on
log_level
and
syslog_pri
. Can be
CRITICAL
,
ERROR
,
HIGH
,
MEDIUM
, or
INFORMATIONAL
.
Need more help?
Get answers from Community members and Google SecOps professionals.
