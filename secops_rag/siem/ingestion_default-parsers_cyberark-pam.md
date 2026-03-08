# Collect CyberArk PAM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pam/  
**Scraped:** 2026-03-05T09:22:52.995623Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CyberArk PAM logs
Supported in:
Google secops
SIEM
This parser code first extracts fields from CyberArk Privileged Access Manager (PAM) syslog messages using regular expressions. Then, it maps the extracted fields to a unified data model (UDM), enriching the data with additional context and standardizing the event type based on specific criteria.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
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
        namespace: Cyberark_PAM
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
Configure Syslog Export for CyberArk Vault
Log in to the Vault server.
Open the configuration file
dbparm.ini
, located at:
C:\Program Files (x86)\CyberArk\Vault\Server\dbparm.ini
.
Add or modify the following parameters:
SyslogServer=<syslog_server_ip>
SyslogPort=<syslog_server_port>
SyslogProtocol=<TCP or UDP>
SyslogFormat=Syslog
Save the
dbparm.ini
file.
Restart the Vault Server:
net stop CyberArkVault
net start CyberArkVault
Configure Syslog Export in PVWA
Log in to the PVWA Server.
Open the
Web.config
file, located at:
C:\inetpub\wwwroot\PasswordVault\
Add or modify the following keys:
<add key="SyslogServer" value="<syslog_server_ip>" />
<add key="SyslogPort" value="<syslog_server_port>" />
<add key="SyslogProtocol" value="<TCP or UDP>" />
<add key="SyslogFormat" value="Syslog" />
Save the changes to the
Web.config
file.
Restart the IIS service:
iisreset
Configure Syslog Export in PTA
Access the PTA server using SSH.
Open the
application.properties
file, located at:
/opt/cta/config/application.properties
Add or modify the following lines:
syslog.server.ip=<syslog_server_ip>
syslog.server.port=<syslog_server_port>
syslog.protocol=<TCP or UDP>
Save the
application.properties
file.
Restart the PTA service to apply the changes:
sudo service pta restart
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
metadata.description
Directly mapped from the
act
field.
cn1
additional.fields.value.string_value
Directly mapped from the
cn1
field when
cn1Label
is not empty.
cn1Label
additional.fields.key
Directly mapped from the
cn1Label
field when
cn1
is not empty.
cn2
additional.fields.value.string_value
Directly mapped from the
cn2
field when
cn2Label
is not empty.
cn2Label
additional.fields.key
Directly mapped from the
cn2Label
field when
cn2
is not empty.
cs1
additional.fields.value.string_value
Directly mapped from the
cs1
field when
cs1Label
is not empty.
cs1Label
additional.fields.key
Directly mapped from the
cs1Label
field when
cs1
is not empty.
cs2
additional.fields.value.string_value
Directly mapped from the
cs2
field when
cs2Label
is not empty.
cs2Label
additional.fields.key
Directly mapped from the
cs2Label
field when
cs2
is not empty.
cs3
additional.fields.value.string_value
Directly mapped from the
cs3
field when
cs3Label
is not empty.
cs3Label
additional.fields.key
Directly mapped from the
cs3Label
field when
cs3
is not empty.
cs4
additional.fields.value.string_value
Directly mapped from the
cs4
field when
cs4Label
is not empty.
cs4Label
additional.fields.key
Directly mapped from the
cs4Label
field when
cs4
is not empty.
cs5
additional.fields.value.string_value
Directly mapped from the
cs5
field when
cs5Label
is not empty.
cs5Label
additional.fields.key
Directly mapped from the
cs5Label
field when
cs5
is not empty.
dhost
target.hostname
Mapped from the
dhost
field if it's not an IP address. If
dhost
is empty, it's mapped from
shost
(IP or hostname).
dhost
target.asset.hostname
Mapped from the
dhost
field if it's not an IP address. If
dhost
is empty, it's mapped from
shost
(IP or hostname).
dhost
target.ip
Mapped from the
dhost
field if it's an IP address.
dhost
target.asset.ip
Mapped from the
dhost
field if it's an IP address.
duser
target.user.userid
Directly mapped from the
duser
field.
dvc
intermediary.ip
Mapped from the
dvc
field if it's an IP address.
externalId
metadata.product_log_id
Directly mapped from the
externalId
field.
fname
target.file.full_path
Directly mapped from the
fname
field.
name
metadata.event_type
Used to determine the
event_type
based on the combination of
name
,
shost
, and
dhost
fields. Possible values: USER_CHANGE_PASSWORD, FILE_READ, USER_LOGIN, FILE_OPEN, FILE_DELETION.  If no match is found, and
has_principal
is true and
has_target
is false, then
event_type
is set to STATUS_UPDATE. Otherwise, it defaults to GENERIC_EVENT.
prin_hostname
principal.hostname
Directly mapped from the
prin_hostname
field. If empty, it's mapped from
shost
if
shost
is not an IP address.
prin_hostname
principal.asset.hostname
Directly mapped from the
prin_hostname
field. If empty, it's mapped from
shost
if
shost
is not an IP address.
prin_ip
principal.ip
Directly mapped from the
prin_ip
field. If empty, it's mapped from
shost
if
shost
is an IP address.
prin_ip
principal.asset.ip
Directly mapped from the
prin_ip
field. If empty, it's mapped from
shost
if
shost
is an IP address.
product
metadata.product_name
Directly mapped from the
product
field. Defaults to "PAM" if not present in the log.
reason
security_result.description
Directly mapped from the
reason
field.
severity
security_result.severity
Mapped from the
severity
field based on the following logic: 1-3: INFORMATIONAL, 4: ERROR, 5: CRITICAL.
shost
principal.hostname
Mapped to
prin_hostname
if
prin_hostname
is empty and
shost
is not an IP address.
shost
principal.asset.hostname
Mapped to
prin_hostname
if
prin_hostname
is empty and
shost
is not an IP address.
shost
principal.ip
Mapped to
prin_ip
if
prin_ip
is empty and
shost
is an IP address.
shost
principal.asset.ip
Mapped to
prin_ip
if
prin_ip
is empty and
shost
is an IP address.
shost
target.hostname
Mapped to
target.hostname
if
dhost
is empty and
shost
is not an IP address.
shost
target.asset.hostname
Mapped to
target.hostname
if
dhost
is empty and
shost
is not an IP address.
shost
target.ip
Mapped to
target.ip
if
dhost
is empty and
shost
is an IP address.
shost
target.asset.ip
Mapped to
target.ip
if
dhost
is empty and
shost
is an IP address.
status
additional.fields.value.string_value
Directly mapped from the
status
field.
suser
principal.user.userid
Mapped from the
suser
field. If
duser
is empty, it's considered the target user ID.
time
metadata.event_timestamp.seconds
Directly mapped from the
time
field after converting to timestamp format.
time
metadata.event_timestamp.nanos
Directly mapped from the
time
field after converting to timestamp format.
vendor
metadata.vendor_name
Directly mapped from the
vendor
field. Defaults to "CYBERARK" if not present in the log.
version
metadata.product_version
Directly mapped from the
version
field.
metadata.log_type
Hardcoded to "CYBERARK_PAM".
extensions.auth.mechanism
Set to "USERNAME_PASSWORD" if
event_type
is "USER_LOGIN".
Need more help?
Get answers from Community members and Google SecOps professionals.
