# Collect BMC Helix Discovery logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-helix-discovery/  
**Scraped:** 2026-03-05T09:51:32.366704Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BMC Helix Discovery logs
Supported in:
Google secops
SIEM
This parser extracts fields from BMC Helix Discovery syslog messages using grok patterns. It focuses on login/logout events and status updates. It maps extracted fields like timestamps, usernames, source IPs, and descriptions to the UDM. Events are categorized based on the extracted
product_event_type
and log details.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to the BeyondTrust instance.
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
        namespace: BMC_HELIX_DISCOVERY
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
Export Syslog from BMC Helix Discovery
Access the BMC Discovery instance as a
root user
.
Edit the
syslog configuration
file:
etc/rsyslog.conf
Add the following entry at the top:
# Send everything to the remote syslog server
.
Replace the IP address with that of your syslog server:
# Send everything to the remote syslog server

*.* @192.168.1.100
Restart the syslog service on the appliance:
sudo
/usr/bin/systemctl
restart
rsyslog.service
Test the forwarding configuration.
Use the logger utility to send a syslog message:
logger
this
is
a
test
of
remote
logging
Verify this has been logged:
su
-
Password:

tail
-n5
/var/log/messages
Jan
17
11
:42:10
localhost
seclab:
this
is
a
test
of
remote
logging
Sign in to Google SecOps and check that the same messages appear.
UDM Mapping Table
Log Field
UDM Mapping
Logic
data
metadata.description
The description of the event, extracted from the log message.
data
metadata.product_event_type
The raw event type, extracted from the log message.
data
principal.ip
The source IP address, extracted from the description field in the log message.
data
security_result.summary
A summary of the event, extracted from the log message.
data
target.user.userid
The username, extracted from the log message. An empty object is created by the parser. Copied from the top-level
timestamp
field in the raw log. Determined by the parser based on
product_event_type
and
desc
fields. If
product_event_type
is "logon" or
desc
contains "logged on", it's set to "USER_LOGIN". If
product_event_type
is "logoff" or
desc
contains "logged off", it's set to "USER_LOGOUT". Otherwise, if
src_ip
is present, it's set to "STATUS_UPDATE".  Defaults to "GENERIC_EVENT". Hardcoded to "BMC_HELIX_DISCOVERY". Hardcoded to "BMC_HELIX_DISCOVERY". Hardcoded to "BMC_HELIX_DISCOVERY".
Need more help?
Get answers from Community members and Google SecOps professionals.
