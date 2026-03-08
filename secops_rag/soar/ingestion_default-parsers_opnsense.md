# Collect OPNsense firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opnsense/  
**Scraped:** 2026-03-05T09:58:57.241261Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect OPNsense firewall logs
Supported in:
Google secops
SIEM
This parser extracts fields from OPNsense firewall logs (syslog and CSV formats) and maps them to the UDM. It uses grok and CSV parsing for "filterlog" application logs, handling different log formats and network protocols (TCP, UDP, ICMP, etc.) to populate UDM fields like principal, target, network, and security_result. It also adds metadata like vendor and product name, and determines the event type based on the presence of principal and target information.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have privileged access to the OPNsense web interface.
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
        namespace: testNamespace
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
Add Syslog server configuration to OPNsense
Sign in to the OPNsense web interface.
Go to
System
>
Settings
>
Logging
.
In the
Remote Logging
section, enable
Send logs to remote syslog server
by checking the box.
In the
Remote Syslog Servers
field, enter the
IP address
of the syslog server, including the
PORT
(for example, 10.10.10.10:54525).
Select
Local0
as the
syslog facility
.
Set Syslog Level as
Alert
.
Click
Save
to apply the changes.
UDM Mapping Table
Log Field
UDM Mapping
Logic
column1
security_result.rule_id
Directly mapped from
column1
.
column10
additional.fields[].key
: "tos"
additional.fields[].value.string_value
: Value of
column10
Directly mapped from
column10
, nested under
additional.fields
with key "tos".
column12
additional.fields[].key
: "ttl"
additional.fields[].value.string_value
: Value of
column12
Directly mapped from
column12
, nested under
additional.fields
with key "ttl".
column13
additional.fields[].key
: "Id"
additional.fields[].value.string_value
: Value of
column13
Directly mapped from
column13
, nested under
additional.fields
with key "Id".
column14
additional.fields[].key
: "offset"
additional.fields[].value.string_value
: Value of
column14
Directly mapped from
column14
, nested under
additional.fields
with key "offset".
column15
additional.fields[].key
: "flags"
additional.fields[].value.string_value
: Value of
column15
Directly mapped from
column15
, nested under
additional.fields
with key "flags".
column17
network.ip_protocol
Directly mapped from
column17
after converting to uppercase.
column18
network.received_bytes
Directly mapped from
column18
after converting to unsigned integer.
column19
principal.ip
Directly mapped from
column19
.
column20
target.ip
Directly mapped from
column20
.
column21
principal.port
(if
column17
is TCP or UDP)
additional.fields[].key
: "data_length"
additional.fields[].value.string_value
: Extracted value (if
column17
is ICMP, GRE, ESP, or IGMP)
If
column17
is TCP/UDP, directly mapped from
column21
and converted to integer. Otherwise, the "datalength" value is extracted using grok and placed in
additional.fields
with key "data_length".
column22
target.port
Directly mapped from
column22
if
column17
is TCP or UDP, and converted to integer.
column24
additional.fields[].key
: "tcp_flags"
additional.fields[].value.string_value
: Value of
column24
Directly mapped from
column24
if
column17
is TCP, nested under
additional.fields
with key "tcp_flags".
column29
additional.fields[].key
: "tcp_options"
additional.fields[].value.string_value
: Value of
column29
Directly mapped from
column29
if
column17
is TCP, nested under
additional.fields
with key "tcp_options".
column4
additional.fields[].key
: "tracker"
additional.fields[].value.string_value
: Value of
column4
Directly mapped from
column4
, nested under
additional.fields
with key "tracker".
column5
additional.fields[].key
: "interface"
additional.fields[].value.string_value
: Value of
column5
Directly mapped from
column5
, nested under
additional.fields
with key "interface".
column6
security_result.rule_type
Directly mapped from
column6
.
column7
security_result.action
Mapped from
column7
. If "block", converted to uppercase "BLOCK". If "pass", set to "ALLOW".
column8
network.direction
Mapped from
column8
. If "in", set to "INBOUND". If "out", set to "OUTBOUND".
domain
principal.administrative_domain
Directly mapped from the grok-extracted
domain
. Set to "NETWORK_CONNECTION" if both principal and target IP addresses are present, otherwise "GENERIC_EVENT".  Hardcoded to "OPNSENSE". Hardcoded to "OPNSENSE".
message
Various fields
Parsed using grok and csv filters to extract various fields. See other rows for specific mappings.
ts
metadata.event_timestamp.seconds
,
timestamp.seconds
Parsed from the message field using grok and then converted to a timestamp. The seconds value is used to populate both
metadata.event_timestamp.seconds
and
timestamp.seconds
.
application
principal.application
Directly mapped from the grok-extracted
application
.
Need more help?
Get answers from Community members and Google SecOps professionals.
