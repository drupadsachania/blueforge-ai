# Collect VMware Workspace ONE UEM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-workspace-one/  
**Scraped:** 2026-03-05T10:02:23.957191Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware Workspace ONE UEM logs
Supported in:
Google secops
SIEM
This parser extracts logs from VMware Workspace ONE UEM (formerly known as VMware AirWatch) in Syslog, CEF, or key-value pair formats. It normalizes fields such as usernames, timestamps, and event details, mapping them to the UDM. The parser handles various Workspace ONE UEM event types, populating principal, target, and other UDM fields based on specific event data and logic for different log formats.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have privileged access to the VMware Workspace ONE console.
Ensure that you have a Windows or Linux host with systemd.
If running behind a proxy, ensure that the firewall
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
Copy and Save the
customer ID
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
        namespace: 
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
Configuring syslog in VMware Workspace ONE UEM
Sign in to the Workspace ONE UEM Console:
Go to
Settings
>
System
>
Advanced
>
Syslog
.
Check the option to
Enable Syslog
.
Specify values for the following input parameters:
IP Address/Hostname
: enter the address of your Bindplane Agent.
Port
: enter the designated port (default: 514).
Protocol
: select
UDP
or
TCP
depending on your Bindplane agent configuration.
Select Log Types
: select the logs you want to send to Google SecOps - Device Management Logs, Console Activity Logs, Compliance Logs, Event Logs
Set the log level (for example,
Info
,
Warning
,
Error
).
Click
Save
to apply settings
UDM Mapping Table
Log Field
UDM Mapping
Logic
AdminAccount
principal.user.userid
The
AdminAccount
from the raw log is mapped to the
principal.user.userid
field.
Application
target.application
The
Application
field from the raw log is mapped to the
target.application
field.
ApplicationUUID
additional.fields
The
ApplicationUUID
field from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "ApplicationUUID".
BytesReceived
network.received_bytes
The
BytesReceived
field from the raw log is mapped to the
network.received_bytes
field.
Device
target.hostname
The
Device
field from the raw log is mapped to the
target.hostname
field.
FriendlyName
target.hostname
The
FriendlyName
field from the raw log is mapped to the
target.hostname
field when
Device
is not available.
GroupManagementData
security_result.description
The
GroupManagementData
field from the raw log is mapped to the
security_result.description
field.
Hmac
additional.fields
The
Hmac
field from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "Hmac".
LoginSessionID
network.session_id
The
LoginSessionID
field from the raw log is mapped to the
network.session_id
field.
LogDescription
metadata.description
The
LogDescription
field from the raw log is mapped to the
metadata.description
field.
MessageText
metadata.description
The
MessageText
field from the raw log is mapped to the
metadata.description
field.
OriginatingOrganizationGroup
principal.user.group_identifiers
The
OriginatingOrganizationGroup
field from the raw log is mapped to the
principal.user.group_identifiers
field.
OwnershipType
additional.fields
The
OwnershipType
field from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "OwnershipType".
Profile
target.resource.name
The
Profile
field from the raw log is mapped to the
target.resource.name
field when
ProfileName
is not available.
ProfileName
target.resource.name
The
ProfileName
field from the raw log is mapped to the
target.resource.name
field.
Request Url
target.url
The
Request Url
field from the raw log is mapped to the
target.url
field.
SmartGroupName
target.group.group_display_name
The
SmartGroupName
field from the raw log is mapped to the
target.group.group_display_name
field.
Tags
additional.fields
The
Tags
field from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "Tags".
User
target.user.userid
The
User
field from the raw log is mapped to the
target.user.userid
field. The
Event Category
from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "Event Category". The
Event Module
from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "Event Module". The
Event Source
from the raw log is added as a key-value pair to the
additional.fields
array in the UDM. The key is "Event Source". Set to "SSO" by the parser for specific events. Derived from the raw log's timestamp.  The parser extracts the date and time from the raw log and converts it to a UDM timestamp. Determined by the parser based on the
event_name
and other fields.  See parser code for the mapping logic. Set to "AIRWATCH" by the parser. The
event_name
from the raw log is mapped to the
metadata.product_event_type
field. Set to "AirWatch" by the parser. Set to "VMWare" by the parser. The
domain
from the raw log is mapped to the
principal.administrative_domain
field. The
hostname
is extracted from the
device_name
field in the raw log or mapped from the
Device
or
FriendlyName
fields. The
sys_ip
from the raw log is mapped to the
principal.ip
field. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. The
user_name
from the raw log is mapped to the
principal.user.userid
field. Extracted from the raw log for certain event types. Set by the parser for specific events. Set by the parser for specific events. The
event_category
from the raw log is mapped to the
security_result.category_details
field. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. The
domain
from the raw log is mapped to the
target.administrative_domain
field. Constructed by combining
DeviceSerialNumber
and
DeviceUdid
from the raw log for the "DeleteDeviceRequested" event. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. The
sys_ip
or other IP addresses from the raw log are mapped to the
target.ip
field. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. Set by the parser for specific events. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types.
Need more help?
Get answers from Community members and Google SecOps professionals.
