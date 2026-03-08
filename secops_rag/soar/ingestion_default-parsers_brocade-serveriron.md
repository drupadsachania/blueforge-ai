# Collect Brocade ServerIron logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-serveriron/  
**Scraped:** 2026-03-05T09:51:40.352447Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Brocade ServerIron logs
Supported in:
Google secops
SIEM
This parser extracts fields from Brocade ServerIron syslog messages using regular expression matching and maps them to the Unified Data Model (UDM). It handles various log formats, including network status, user authentication, and security events. The parser performs data type conversions and enrichment where necessary.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the Brocade ServerIron instance.
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
        namespace: Brocade_ServerIron
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
Configure Syslog Export from Brocade ServerIron ADX
Sign in to the ADX device and enter global configuration mode:
enable
configure
terminal
Enable Syslog Logging:
logging
on
Specify the IP address or hostname and port of the syslog server, including the desired protocol (Bindplane):
logging
host
<syslog-server-ip>
[
udp
|
tcp
]
port
<port-number>
Example for TCP on port 54525:
logging
host
10
.10.10.10
tcp
port
54525
Optional: set the
Syslog Facility
(
local0
to
local7
):
logging
facility
local0
Define the minimum severity level of logs to send to the syslog server:
logging
trap
<severity-level>
Save the configuration:
write
memory
UDM Mapping Table
Log Field
UDM Mapping
Logic
%{GREEDYDATA}
metadata.description
The %{GREEDYDATA} field is mapped to metadata.description when it matches the "-- %{GREEDYDATA} --" pattern.
%{GREEDYDATA:auth_result}
security_result.description
The %{GREEDYDATA:auth_result} field is concatenated with the %{GREEDYDATA:desc} field to form the security_result.description when %{GREEDYDATA:desc} is present.
%{GREEDYDATA:desc}
security_result.description
The %{GREEDYDATA:desc} field is used to populate the security_result.description field. It can be concatenated with other fields depending on the raw log format.
%{GREEDYDATA:login_to}
security_result.description
The %{GREEDYDATA:login_to} field is concatenated with the %{GREEDYDATA:desc} field to form the security_result.description when %{GREEDYDATA:desc} is present.
%{GREEDYDATA:user}
target.user.userid
The %{GREEDYDATA:user} field is mapped to target.user.userid.
%{HOST:principal_host}
principal.hostname
The %{HOST:principal_host} field is mapped to principal.hostname.
%{HOST:target_host}
target.hostname
The %{HOST:target_host} field is mapped to target.hostname.
%{INT:http_port}
additional.fields.value.string_value
The %{INT:http_port} field is mapped to additional.fields.value.string_value with key "HTTP Port".
%{INT:target_port}
target.port
The %{INT:target_port} field is mapped to target.port and converted to an integer.
%{INT:telnet_port}
additional.fields.value.string_value
The %{INT:telnet_port} field is mapped to additional.fields.value.string_value with key "Telnet Port".
%{INT:tftp_port}
additional.fields.value.string_value
The %{INT:tftp_port} field is mapped to additional.fields.value.string_value with key "TFTP Port".
%{IP:principal_ip}
principal.ip
The %{IP:principal_ip} field is mapped to principal.ip.
%{IP:target_ip}
target.ip
The %{IP:target_ip} field is mapped to target.ip.
%{IPV4:principal_ip}
principal.ip
The %{IPV4:principal_ip} field is mapped to principal.ip.
%{IPV4:target_ip}
target.ip
The %{IPV4:target_ip} field is mapped to target.ip.
%{MAC:principal_mac}
principal.mac
The %{MAC:principal_mac} field is mapped to principal.mac after converting it to the format [0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}.
%{USERNAME:target_host}
target.hostname
The %{USERNAME:target_host} field is mapped to target.hostname.
%{USERNAME:user}
target.user.userid
The %{USERNAME:user} field is mapped to target.user.userid.
%{WORD:auth_result}
security_result.description
The %{WORD:auth_result} field is concatenated with the %{GREEDYDATA:desc} field to form the security_result.description when %{GREEDYDATA:desc} is present.
%{WORD:proto}
network.application_protocol
The %{WORD:proto} field is mapped to network.application_protocol when its value is 'SSH'.
timestamp
metadata.event_timestamp
The timestamp field is parsed from the raw log data using a grok pattern and converted to a timestamp object.
extensions.auth.type
The value is set to "MACHINE" if the proto field is not empty and the auth_action field is either "logout" or "login".
metadata.description
The field is populated with the value of the "metadata_description" field if it's not empty.
metadata.event_type
The field is populated based on the values of other fields using conditional logic:
- STATUS_STARTUP: if target_port_status is "up".
- STATUS_SHUTDOWN: if target_port_status is "down".
- USER_LOGOUT: if proto is not empty and auth_action is "logout".
- USER_LOGIN: if proto is not empty and auth_action is "login".
- STATUS_UPDATE: if metadata_description matches "state changed".
- GENERIC_EVENT: if none of the above conditions are met.
metadata.log_type
The value is hardcoded to "BROCADE_SERVERIRON".
metadata.product_name
The value is hardcoded to "ServerIron".
metadata.vendor_name
The value is hardcoded to "Brocade".
security_result.action
The value is set to "BLOCK" if the desc field contains "fail", or the auth_result field contains "fail" or "rejected".
Need more help?
Get answers from Community members and Google SecOps professionals.
