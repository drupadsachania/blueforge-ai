# Collect Aruba switch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-switch/  
**Scraped:** 2026-03-05T09:19:15.196342Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Aruba switch logs
Supported in:
Google secops
SIEM
This parser extracts fields from Aruba switch syslog messages using grok patterns and maps them to the UDM model. It handles various fields, including timestamps, hostnames, application names, process IDs, event IDs, and descriptions, populating the relevant UDM fields. The event type is set based on the presence of principal information.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have a Windows 2016 or later or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you privileged access to the Aruba switch.
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
          namespace: aruba_switch
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
Configure Syslog on the Aruba Switch
Connect to the
Aruba
switch through the
Console
:
ssh
admin@<switch-ip>
Connect to the
Aruba
switch through a
Web Interface
:
Go to the Aruba switch web GUI.
Authenticate with the switch's administrator credentials.
Enable
Syslog
using the
CLI
configuration:
Enter global configuration mode:
configure
terminal
Specify the external syslog server:
logging
<bindplane-ip>:<bindplane-port>
Replace
<bindplane-ip>
and
<bindplane-port>
with the address of your Bindplane agent.
Optional: Set the logging
severity level
:
logging
severity
<level>
Optional: Add a
custom
log source
identifier
(tag):
logging
facility
local5
Save the configuration:
write
memory
Enable
Syslog
using Web Interface Configuration:
Log in to the Aruba switch web interface.
Go to
System
>
Logs
>
Syslog
.
Add syslog server parameters:
Enter the
Bindplane IP
address.
Enter the
Bindplane Port
.
Set the
Severity Level
to control the verbosity of logs.
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
app
principal.application
The value of the
app
field from the raw log is directly assigned to
principal.application
.
description
security_result.description
The value of the
description
field from the raw log is directly assigned to
security_result.description
.
event_id
additional.fields.key
The string "event_id" is assigned to
additional.fields.key
.
event_id
additional.fields.value.string_value
The value of the
event_id
field from the raw log is directly assigned to
additional.fields.value.string_value
.
host
principal.asset.hostname
The value of the
host
field from the raw log is directly assigned to
principal.asset.hostname
.
host
principal.hostname
The value of the
host
field from the raw log is directly assigned to
principal.hostname
.
pid
principal.process.pid
The value of the
pid
field from the raw log is directly assigned to
principal.process.pid
.
ts
metadata.event_timestamp
The value of the
ts
field from the raw log is converted to a timestamp and assigned to
metadata.event_timestamp
.  The timestamp is also used for the top-level
timestamp
field in the UDM. The
metadata.event_type
is set to "STATUS_UPDATE" because the
principal_mid_present
variable is set to "true" in the parser when the
host
field is present in the raw log. The string "ARUBA_SWITCH" is assigned to
metadata.product_name
within the parser. The string "ARUBA SWITCH" is assigned to
metadata.vendor_name
within the parser. The parser attempts to extract and parse the user agent from the raw log using
client.userAgent.rawUserAgent
. If successful, the parsed user agent is assigned to
network.http.parsed_user_agent
. However, since the raw logs provided do not contain this field, this UDM field will likely be empty. The parser attempts to extract the raw user agent from the raw log using
client.userAgent.rawUserAgent
. If successful, the raw user agent is assigned to
network.http.user_agent
. However, since the raw logs provided do not contain this field, this UDM field will likely be empty.
Need more help?
Get answers from Community members and Google SecOps professionals.
