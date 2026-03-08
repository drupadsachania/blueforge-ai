# Collect Apple macOS syslog data

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/macos/  
**Scraped:** 2026-03-05T09:18:59.489043Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Apple macOS syslog data
Supported in:
Google secops
SIEM
This parser uses grok patterns to extract fields from Apple macOS syslog messages and populates the Unified Data Model (UDM) with the extracted values, including the timestamp, hostname, intermediary host, command line, process ID, and description. The parser categorizes the event as
STATUS_UPDATE
if a hostname is present; otherwise, it assigns the category
GENERIC_EVENT
to the event. Finally, the parser enriches the UDM event with vendor and product information.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have root access to the Auditd host.
Ensure that you installed rsyslog on the Auditd host.
Ensure that you have a Windows 2012 SP2 or later or Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
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
        namespace: auditd
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
Exporting Syslog from macOS
Install
syslog-ng
using Homebrew:
brew
install
syslog-ng
Configure syslog-ng:
Edit
syslog-ng.conf
file (usually located at
/usr/local/etc/syslog-ng/syslog-ng.conf
):
sudo
vi
/usr/local/etc/syslog-ng/syslog-ng.conf
Add the following configuration block.
Depending on the Bindplane configuration, you can change the delivery method to
tcp
or leave it as
udp
.
Replace
<BindPlaneAgent_IP>
and
<BindPlaneAgent_Port>
with the actual IP address and port of your Bindplane Agent:
source s_local { system(); internal(); };
destination d_secops { tcp("<BindPlaneAgent_IP>:<BindPlaneAgent_Port>"); };
log { source(s_local); destination(d_secops); };
Restart the
syslog-ng
service:
brew
services
restart
syslog-ng
Check the status of
syslog-ng
(you should see
syslog-ng
listed as started):
brew
services
list
UDM Mapping Table
Log Field
UDM Mapping
Logic
data
read_only_udm.metadata.description
The value of the
description
field is extracted from the
data
field in the raw log using a grok pattern.
data
read_only_udm.principal.hostname
The hostname is extracted from the
data
field using a grok pattern.
data
read_only_udm.intermediary.hostname
The intermediary hostname is extracted from the
data
field using a grok pattern.
data
read_only_udm.principal.process.command_line
The process command line is extracted from the
data
field using a grok pattern.
data
read_only_udm.principal.process.pid
The process ID is extracted from the
data
field using a grok pattern.
data
read_only_udm.metadata.event_timestamp
The event timestamp is extracted from the
data
field using a grok pattern and converted to a timestamp object. Hardcoded to "MacOS" in the parser. Hardcoded to "Apple" in the parser. Set to "STATUS_UPDATE" if a hostname is extracted from the logs, otherwise set to "GENERIC_EVENT".
log_type
read_only_udm.metadata.log_type
Directly mapped from the
log_type
field of the raw log.
Need more help?
Get answers from Community members and Google SecOps professionals.
