# Collect Trend Micro Cloud One logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-cloudone/  
**Scraped:** 2026-03-05T09:29:24.040263Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trend Micro Cloud One logs
Supported in:
Google secops
SIEM
Overview
This parser handles syslog and JSON formatted logs from Trend Micro Cloud One. It extracts key-value pairs from LEEF formatted messages, normalizes severity values, identifies principal and target entities (IP, hostname, user), and maps the data into the UDM schema. If the LEEF format is not detected, the parser attempts to process the input as JSON and extract relevant fields accordingly.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have privileged access to Trend Micro Cloud One.
Ensure that you have a Windows 2012 SP2 or later or Linux host with systemd.
If running behind a proxy, ensure firewall
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
Access the machine with Bindplane Agent.
Edit the
config.yaml
file as follows:
receivers:
  udplog:
    # Replace the below port <5514> and IP (0.0.0.0) with your specific values
    listen_address: "0.0.0.0:514" 

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
        namespace: 
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - udplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes using the following command:
sudo systemctl bindplane restart
Configure Syslog from Trend Micro Cloud One
Go to
Policies
>
Common Objects
>
Other
>
Syslog Configurations
.
Click
New
>
New Configuration
>
General
Specify values for the following parameters:
Name
: Unique name that identifies the configuration (for example,
Google SecOps BindPlance server
).
Server Name
: Enter the IP address of the Bindplane Agent.
Server Port
: Enter the port of the Bindplane Agent (for example,
514
).
Transport
: Select
UDP
.
Event Format
: Select
Syslog
.
Include time zone in events
: Keep
unselected
.
Facility
: Type of process with which events will be associated.
Agents should forward logs
: Select
Syslog
server.
Click
Save
.
Export system events in Trend Micro Cloud One
Go to
Administration
>
System Settings
>
Event Forwarding
.
Forward System Events to a remote computer
(via Syslog) using configuration, select the configuration created in the previous step.
Click
Save
.
Export security events in Trend Micro Cloud One
Go to
Policies
.
Click the policy used by the computers.
Go to
Settings
>
Event Forwarding
.
Event Forwarding Frequency (from the Agent/Appliance)
: choose
Period between sending of events
and select how often the security events will be forwarded.
Event Forwarding Configuration (from the Agent/Appliance)
: choose
Anti-Malware Syslog Configuration
and select the configuration created in the previous step.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action
If
act
is "deny" or "block" (case-insensitive), then
BLOCK
. If
act
is "pass" or "allow" (case-insensitive), then
ALLOW
. If
act
is "update" or "rename" (case-insensitive), then
ALLOW_WITH_MODIFICATION
. If
act
is "quarantine" (case-insensitive), then
QUARANTINE
. Otherwise,
UNKNOWN_ACTION
.
act
security_result.action_details
Directly mapped.
cat
security_result.category_details
Directly mapped.
cn1
target.asset_id
Prefixed with "Host Id:" if
cn1Label
is "Host ID".
desc
metadata.description
Directly mapped.
dvchost
target.asset.hostname
Directly mapped.
dvchost
target.hostname
Directly mapped.
log_type
metadata.product_name
Directly mapped.
msg
security_result.description
Directly mapped.
name
security_result.summary
Directly mapped.
organization
target.administrative_domain
Directly mapped.
proto
additional.fields.key
Set to "Protocol" if the
proto
field cannot be converted to an integer.
proto
additional.fields.value.string_value
Directly mapped if the
proto
field cannot be converted to an integer.
proto
network.ip_protocol
Mapped using the
parse_ip_protocol.include
logic, which converts the protocol number to its corresponding name (e.g., "6" becomes "TCP").
product_version
metadata.product_version
Directly mapped.
sev
security_result.severity
If
sev
is "0", "1", "2", "3" or "low" (case-insensitive), then
LOW
. If
sev
is "4", "5", "6" or "medium" (case-insensitive), then
MEDIUM
. If
sev
is "7", "8" or "high" (case-insensitive), then
HIGH
. If
sev
is "9", "10" or "very high" (case-insensitive), then
CRITICAL
.
sev
security_result.severity_details
Directly mapped.
src
principal.asset.hostname
Directly mapped if it's not a valid IP address.
src
principal.asset.ip
Directly mapped if it's a valid IP address.
src
principal.hostname
Directly mapped if it's not a valid IP address.
src
principal.ip
Directly mapped if it's a valid IP address.
TrendMicroDsTenant
security_result.detection_fields.key
Set to "TrendMicroDsTenant".
TrendMicroDsTenant
security_result.detection_fields.value
Directly mapped.
TrendMicroDsTenantId
security_result.detection_fields.key
Set to "TrendMicroDsTenantId".
TrendMicroDsTenantId
security_result.detection_fields.value
Directly mapped.
usrName
principal.user.userid
Directly mapped. If
has_principal
is true and
has_target
is true, then
NETWORK_CONNECTION
. Else if
has_principal
is true, then
STATUS_UPDATE
. Else if
has_target
is true and
has_principal
is false, then
USER_UNCATEGORIZED
. Otherwise,
GENERIC_EVENT
. Set to
AUTHTYPE_UNSPECIFIED
if
event_type
is
USER_UNCATEGORIZED
. Set to "true" if a principal IP, hostname, or MAC address is extracted. Otherwise, initialized to "false". Set to "true" if a target IP, hostname, or MAC address is extracted. Otherwise, initialized to "false". Same as the top-level event timestamp. Set to "Trend Micro".
Need more help?
Get answers from Community members and Google SecOps professionals.
