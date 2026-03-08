# Collect Brocade switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-switch/  
**Scraped:** 2026-03-05T09:51:41.414382Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Brocade switch logs
Supported in:
Google secops
SIEM
This parser extracts fields from Brocade switch logs using grok patterns matching various log formats. It then maps these extracted fields to UDM fields, handling different log structures and enriching the data with metadata like vendor and product information. The parser also performs data transformations, such as converting severity levels and handling repeated messages, before generating the final UDM output.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have CLI Admin access to the Brocade Switch.
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
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane is installed.
Edit the
config.yaml
file as follows:
receivers:
    tcplog:
        # Replace the below port <54525> and IP <0.0.0.0> with your specific values
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
        namespace: Brocade_Switch
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes:
sudo
systemctl
restart
bindplane
Configure Syslog Export from a Brocade Switch
Connect to the Brocade switch using SSH or Telnet with the appropriate credentials.
Run the following command to specify the
IP
address or hostname and the
Port
of the syslog server (Bindplane):
syslogadmin --set -ip <IP> -port <Port>
For example:
syslogadmin --set -ip 10.10.10.10 -port 54525
Run the following command to display the configured syslog servers:
syslogadmin --show -ip
UDM Mapping Table
Log Field
UDM Mapping
Logic
application
additional.fields[].key
: "application"
additional.fields[].value.string_value
:
Value extracted from the
application@1588
field in the raw log when the KV_DATA field exists.
class
additional.fields[].key
: "class"
additional.fields[].value.string_value
:
Value extracted from the
class@1588
field in the raw log when the KV_DATA field exists.
domain
principal.administrative_domain
Value extracted from the grok pattern matching the
domain
field.
Event
additional.fields[].key
: "event_category"
additional.fields[].value.string_value
:
Value extracted from the
arg0@1588
field in the raw log when the KV_DATA field exists.
event_id
metadata.product_log_id
Value extracted from the grok pattern matching the
event_id
field.
event_type
metadata.product_event_type
Value extracted from the grok pattern matching the
event_type
field.
flags
additional.fields[].key
: "flags"
additional.fields[].value.string_value
:
Value extracted from the grok pattern matching the
flags
field.
Info
metadata.description
Value extracted from the
Info
field, parsed using grok.
interface
app_protocol_src
Value extracted from the
interface@1588
field in the raw log when the KV_DATA field exists. Used to derive
network.application_protocol
.
ip
principal.ip
Value extracted from the
ip
field, parsed using grok. Merged into
principal.ip
if it's not the same as the IP extracted from the
Info
field.
Info
,
IP Addr
principal.ip
Value extracted from the
IP Addr
field within the
Info
field, parsed using grok.
log
additional.fields[].key
: "log"
additional.fields[].value.string_value
:
Value extracted from the
log@1588
field in the raw log when the KV_DATA field exists.
msg
metadata.description
Value extracted from the
msg
field, parsed using grok.
msgid
additional.fields[].key
: "msgid"
additional.fields[].value.string_value
:
Value extracted from the
msgid@1588
field in the raw log when the KV_DATA field exists.
prin_host
principal.hostname
principal.asset.hostname
Value extracted from the grok pattern matching the
prin_host
field.
product_version
metadata.product_version
Value extracted from the grok pattern matching the
product_version
field.
repeat_count
additional.fields[].key
: "repeat_count"
additional.fields[].value.string_value
:
Value extracted from the
msg
field, parsed using grok.
role
,
user_role
principal.user.attribute.roles[].name
Value extracted from the
role@1588
or
user_role
field. If the value is "admin", it's replaced with "Admin".
sequence_number
additional.fields[].key
: "sequence_number"
additional.fields[].value.string_value
:
Value extracted from the grok pattern matching the
sequence_number
field.
severity
security_result.severity
Value extracted from the
severity
field, parsed using grok. Mapped to UDM severity values (INFORMATIONAL, ERROR, CRITICAL, MEDIUM).
Status
security_result.summary
Value extracted from the
Status
field.
switch_name
additional.fields[].key
: "switch_name"
additional.fields[].value.string_value
:
Value extracted from the grok pattern matching the
switch_name
field.
target_application
target.application
Value extracted from the grok pattern matching the
target_application
field.
time
additional.fields[].key
: "time"
additional.fields[].value.string_value
:
Value extracted from the
time
field within the
kv_data3
field.
timestamp
metadata.event_timestamp.seconds
Value extracted from the
timestamp
field, parsed using the date filter.
user
principal.user.userid
principal.user.user_display_name
Value extracted from the
user
or
user@1588
field, parsed using grok. Copied from
principal.hostname
. Copied from
principal.ip
. Copied from
metadata.product_event_type
or set to "STATUS_UPDATE" based on conditions. Copied from the log's
create_time.nanos
. Determined by parser logic based on the values of
has_principal
,
has_target
,
has_userid
, and
event_type
. Can be "SYSTEM_AUDIT_LOG_UNCATEGORIZED", "STATUS_UPDATE", or "GENERIC_EVENT". Hardcoded to "BROCADE_SWITCH". Hardcoded to "BROCADE". Hardcoded to "BROCADE_SWITCH". Derived from the
interface
field or set to "SSH" if the
interface
field contains "SSH".
Need more help?
Get answers from Community members and Google SecOps professionals.
