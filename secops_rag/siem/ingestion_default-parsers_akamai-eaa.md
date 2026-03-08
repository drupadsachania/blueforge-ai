# Collect Akamai EAA (Enterprise Application Access) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa/  
**Scraped:** 2026-03-05T09:18:39.513567Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akamai EAA (Enterprise Application Access) logs
Supported in:
Google secops
SIEM
This document explains how to ingest Akamai Enterprise Application Access (EAA) logs to Google Security Operations using Akamai's Unified Log Streamer (ULS) and Bindplane. Akamai EAA produces operational data in the form of access logs, admin audit logs, authentication details, and connector health metrics. The parser extracts fields from the JSON logs, performs data transformations like string conversions and IP address extraction, and maps these fields to the UDM, handling various event types like
NETWORK_HTTP
and
USER_UNCATEGORIZED
based on the presence of specific fields. It also adds metadata like vendor and product names to the UDM event.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with
systemd
to run the Bindplane agent
Linux, macOS, or containerized environment (Docker/Kubernetes) to run Unified Log Streamer
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Akamai EAA tenant with administrative access
Akamai API credentials (EdgeGrid authentication):
Access Token
Client Token
Client Secret
API Base Hostname (for example,
akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx.luna.akamaiapis.net
)
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the 
system where Bindplane will be installed.
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
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open the
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Additional installation resources
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
tcplog
:
listen_address
:
"0.0.0.0:5140"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'AKAMAI_EAA'
raw_log_field
:
body
ingestion_labels
:
source
:
akamai_eaa
service
:
pipelines
:
logs/akamai_eaa
:
receivers
:
-
tcplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the following:
Replace
<CUSTOMER_ID>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
0.0.0.0:5140
: The IP address and port for Bindplane to listen on. Adjust as needed for your environment.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Install Akamai Unified Log Streamer
Unified Log Streamer (ULS) pulls logs from Akamai EAA via the Enterprise Application Access API and streams them to Bindplane using TCP or UDP.
Linux installation
Download the latest ULS release:
curl
-LO
https://github.com/akamai/uls/releases/latest/download/uls-linux-amd64
Make the binary executable:
chmod
+x
uls-linux-amd64
Move it to a standard location:
sudo
mv
uls-linux-amd64
/usr/local/bin/uls
macOS installation
Download the latest ULS release:
curl
-LO
https://github.com/akamai/uls/releases/latest/download/uls-darwin-amd64
Make the binary executable:
chmod
+x
uls-darwin-amd64
Move it to a standard location:
sudo
mv
uls-darwin-amd64
/usr/local/bin/uls
Docker installation
Pull the official ULS Docker image:
docker
pull
akamai/uls:latest
Configure Akamai EdgeGrid credentials
Create the EdgeGrid credentials file:
mkdir
-p
~/.edgerc
nano
~/.edgerc
Add your Akamai API credentials in the following format:
[default]
client_secret
=
your-client-secret
host
=
akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx.luna.akamaiapis.net
access_token
=
your-access-token
client_token
=
your-client-token
Secure the credentials file:
chmod
600
~/.edgerc
Replace the following:
your-client-secret
: Your Akamai Client Secret.
your-access-token
: Your Akamai Access Token.
your-client-token
: Your Akamai Client Token.
akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx.luna.akamaiapis.net
: Your Akamai API base hostname.
Configure ULS to stream EAA logs to BindPlane
Command-line execution (testing)
Run ULS with TCP output to stream logs to the Bindplane agent:
uls
--input
eaa
\
--feed
access
\
--output
tcp
\
--host
<BINDPLANE_HOST>
\
--port
5140
\
--edgerc
~/.edgerc
\
--section
default
Replace the following:
<BINDPLANE_HOST>
: The IP address or hostname of the server running Bindplane
5140
: The port configured in Bindplane's
tcplog
receiver
To stream multiple feed types, run separate ULS instances:
```bash
#
Access logs
uls --input eaa --feed access --output tcp --host <BINDPLANE_HOST> --port 5140 --edgerc ~/.edgerc --section default
#
Admin audit logs
uls --input eaa --feed admin --output tcp --host <BINDPLANE_HOST> --port 5140 --edgerc ~/.edgerc --section default
#
Connector health
uls --input eaa --feed conhealth --output tcp --host <BINDPLANE_HOST> --port 5140 --edgerc ~/.edgerc --section default
```
Systemd service (production)
For production deployments, configure ULS as a systemd service:
Create a ULS configuration file:
sudo
mkdir
-p
/etc/uls
sudo
nano
/etc/uls/eaa-access-tcp.conf
Add the following configuration:
ULS_INPUT
=
eaa
ULS_FEED
=
access
ULS_OUTPUT
=
tcp
ULS_HOST
=
<BINDPLANE_HOST>
ULS_PORT
=
5140
ULS_EDGERC
=
/root/.edgerc
ULS_SECTION
=
default
Create a systemd service file:
sudo
nano
/etc/systemd/system/uls-eaa-access.service
Add the following content:
[Unit]
Description
=
Unified Log Streamer - EAA Access Logs to BindPlane
After
=
network.target
[Service]
Type
=
simple
EnvironmentFile
=
/etc/uls/eaa-access-tcp.conf
ExecStart
=
/usr/local/bin/uls --input ${ULS_INPUT} --feed ${ULS_FEED} --output ${ULS_OUTPUT} --host ${ULS_HOST} --port ${ULS_PORT} --edgerc ${ULS_EDGERC} --section ${ULS_SECTION}
Restart
=
always
RestartSec
=
10
User
=
root
[Install]
WantedBy
=
multi-user.target
Enable and start the service:
sudo
systemctl
daemon-reload
sudo
systemctl
enable
uls-eaa-access.service
sudo
systemctl
start
uls-eaa-access.service
Verify the service is running:
sudo
systemctl
status
uls-eaa-access.service
View logs:
sudo
journalctl
-u
uls-eaa-access.service
-f
Repeat steps 1-7 for each additional feed type (admin, conhealth) by creating separate configuration and service files with different names (for example,
uls-eaa-admin.service
,
uls-eaa-conhealth.service
).
Docker deployment
Create a Docker Compose file:
nano
docker-compose.yml
Add the following configuration:
version
:
'3.8'
services
:
uls-eaa-access
:
image
:
akamai/uls:latest
container_name
:
uls-eaa-access
restart
:
unless-stopped
environment
:
-
ULS_INPUT=eaa
-
ULS_FEED=access
-
ULS_OUTPUT=tcp
-
ULS_HOST=<BINDPLANE_HOST>
-
ULS_PORT=5140
volumes
:
-
~/.edgerc:/root/.edgerc:ro
command
:
>
--input eaa
--feed access
--output tcp
--host "$${ULS_HOST}"
--port "$${ULS_PORT}"
--edgerc /root/.edgerc
--section default
uls-eaa-admin
:
image
:
akamai/uls:latest
container_name
:
uls-eaa-admin
restart
:
unless-stopped
environment
:
-
ULS_INPUT=eaa
-
ULS_FEED=admin
-
ULS_OUTPUT=tcp
-
ULS_HOST=<BINDPLANE_HOST>
-
ULS_PORT=5140
volumes
:
-
~/.edgerc:/root/.edgerc:ro
command
:
>
--input eaa
--feed admin
--output tcp
--host "$${ULS_HOST}"
--port "$${ULS_PORT}"
--edgerc /root/.edgerc
--section default
uls-eaa-conhealth
:
image
:
akamai/uls:latest
container_name
:
uls-eaa-conhealth
restart
:
unless-stopped
environment
:
-
ULS_INPUT=eaa
-
ULS_FEED=conhealth
-
ULS_OUTPUT=tcp
-
ULS_HOST=<BINDPLANE_HOST>
-
ULS_PORT=5140
volumes
:
-
~/.edgerc:/root/.edgerc:ro
command
:
>
--input eaa
--feed conhealth
--output tcp
--host "$${ULS_HOST}"
--port "$${ULS_PORT}"
--edgerc /root/.edgerc
--section default
Replace
<BINDPLANE_HOST>
with the IP address or hostname of your Bindplane server.
Start the containers:
docker-compose
up
-d
View logs:
docker-compose
logs
-f
UDM Mapping Table
Log field
UDM mapping
Logic
app
target.application
The value after the colon in the
app
field.
apphost
target.hostname
Directly mapped.
browser
network.http.user_agent
Directly mapped.
bytes_in
network.received_bytes
Directly mapped.
bytes_out
network.sent_bytes
Directly mapped.
cc
principal.location.country_or_region
Directly mapped.
client_id
additional.fields.key
: "Client Id",
additional.fields.value.string_value
:
client_id
Conditionally mapped if
client_id
is present.
clientip
principal.ip
Directly mapped.
cloud_zone
principal.cloud.availability_zone
Directly mapped.
connector_resp_time
security_result.detection_fields.key
: "Connector response time",
security_result.detection_fields.value
:
connector_resp_time
Conditionally mapped if
connector_resp_time
is not empty or "-".
content_type
additional.fields.key
: "Content type",
additional.fields.value.string_value
:
content_type
Conditionally mapped if
content_type
is present.
datetime
metadata.event_timestamp
Parsed from the
datetime
field using the RFC3339 format.
deny_reason
security_result.summary
Directly mapped.
device_type
principal.platform
,
principal.platform_version
Mapped to
WINDOWS
,
LINUX
, or
MAC
based on regex matching. The raw value is mapped to
principal.platform_version
.
di
metadata.ingestion_labels.key
: "di",
metadata.ingestion_labels.value
:
di
Directly mapped as an ingestion label.
error_code
additional.fields.key
: "Error code",
additional.fields.value.string_value
:
error_code
Conditionally mapped if
error_code
is present.
event
metadata.description
Directly mapped.
geo_city
principal.location.city
Directly mapped.
geo_country
principal.location.country_or_region
Directly mapped.
geo_state
principal.location.state
Directly mapped.
groups
principal.user.group_identifiers
Directly mapped.
http_method
network.http.method
Directly mapped.
http_ver
network.application_protocol
,
network.application_protocol_version
Parsed using grok to extract protocol and version.
idpinfo
additional.fields.key
: "IDP Info",
additional.fields.value.string_value
:
idpinfo
Conditionally mapped if
idpinfo
is present.
internal_host
additional.fields.key
: "Internal host",
additional.fields.value.string_value
:
internal_host
Conditionally mapped if
internal_host
is present.
metadata.log_type
metadata.log_type
Hardcoded to "AKAMAI_EAA".
metadata.product_name
metadata.product_name
Hardcoded to "AKAMAI_EAA".
metadata.vendor_name
metadata.vendor_name
Hardcoded to "AKAMAI_EAA".
metadata.event_type
metadata.event_type
Determined by logic:
USER_UNCATEGORIZED
if
uid
is present,
NETWORK_HTTP
if both
principal.ip
and
target
are set, or
GENERIC_EVENT
otherwise.
origin_host
additional.fields.key
: "Origin host",
additional.fields.value.string_value
:
origin_host
Conditionally mapped if
origin_host
is present.
origin_resp_time
security_result.detection_fields.key
: "Origin response time",
security_result.detection_fields.value
:
origin_resp_time
Conditionally mapped if
origin_resp_time
is not empty or "-".
os
principal.platform
Mapped to
WINDOWS
,
MAC
, or
LINUX
based on regex matching.
port
target.port
The value after the colon in the
app
field.
ral
metadata.description
Concatenated values of the
ral
array, separated by commas.
referer
network.http.referral_url
Directly mapped.
resource
principal.resource.attribute.labels.key
: "Resource",
principal.resource.attribute.labels.value
:
resource
Conditionally mapped if
resource
is present.
resource_type
principal.resource.attribute.labels.key
: "Resource Type",
principal.resource.attribute.labels.value
:
resource_type
Conditionally mapped if
resource_type
is present.
rscd
metadata.ingestion_labels.key
: "rscd",
metadata.ingestion_labels.value
:
rscd
Directly mapped as an ingestion label.
session_id
network.session_id
Directly mapped.
session_info
additional.fields.key
: "Session info",
additional.fields.value.string_value
:
session_info
Conditionally mapped if
session_info
is present.
state
principal.location.state
Directly mapped.
status_code
network.http.response_code
Directly mapped.
total_resp_time
security_result.detection_fields.key
: "Total response time",
security_result.detection_fields.value
:
total_resp_time
Conditionally mapped if
total_resp_time
is not empty or "-".
ts
metadata.event_timestamp
Parsed from the
ts
field as UNIX milliseconds or seconds if present, otherwise from the
datetime
field.
uid
principal.user.userid
Directly mapped.
uip
principal.ip
Directly mapped.
url_path
target.url
Directly mapped.
user_agent
network.http.user_agent
,
network.http.parsed_user_agent
Directly mapped and parsed into a structured
parsed_user_agent
field.
username
principal.user.email_addresses
or
principal.user.userid
Mapped to
email_addresses
if it looks like an email, otherwise to
userid
.
Need more help?
Get answers from Community members and Google SecOps professionals.
