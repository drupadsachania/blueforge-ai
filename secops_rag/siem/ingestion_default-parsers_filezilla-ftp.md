# Collect FileZilla FTP logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/filezilla-ftp/  
**Scraped:** 2026-03-05T09:24:17.996287Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FileZilla FTP logs
Supported in:
Google secops
SIEM
This document explains how to ingest FileZilla logs to Google Security Operations
using Bindplane. The Logstash parser code extracts relevant fields like
timestamps, hostnames, user IDs, and descriptions from FileZilla FTP server logs.
It then structures these extracted fields into a Unified Data Model (UDM) for
consistent security analysis and correlation.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later, or a Linux host with
systemd
If running behind a proxy, firewall
ports
are open
Privileged access to an instance of FileZilla Server
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
Install the Bindplane agent on FileZilla Server instance
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
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
For additional installation options, consult the
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
filelog
:
# Adjust the path to the log file
file_path
:
<
PATH_TO>/filezilla-logs.log
log_type
:
'file'
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
ingestion_labels
:
log_type
:
'FILEZILLA_FTP'
raw_log_field
:
body
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
filelog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual Customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
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
Configure logging in FileZilla
Sign in to the server with
FileZilla
.
Open the FileZilla software.
Go to
Edit
>
Settings
.
Select
Logging
from the menu.
Provide the following configuration details:
Select the checkbox
Show timestamps in messagebox
.
Select the checkbox
Log to file
.
Filename
: Enter a filename and select the storage path (for example,
filezilla-logs
).
Optional:
Limit size of logfile
: Select this checkbox to limit the amount of space a log file can use.
Optional:
Limit
: You can enter a max file size for your log file here in Megabytes.
Click
OK
.
Restart FileZilla.
UDM mapping table
Log field
UDM mapping
Logic
data
read_only_udm.metadata.description
The raw log
data
field content.
data
read_only_udm.metadata.event_timestamp.seconds
Extracted from the
data
field using a grok pattern and converted to epoch seconds.
data
read_only_udm.network.http.response_code
Extracted from the
data
field using a grok pattern.
data
read_only_udm.principal.hostname
Extracted from the
data
field using a grok pattern.
data
read_only_udm.principal.port
Extracted from the
data
field using a grok pattern.
data
read_only_udm.principal.user.userid
Extracted from the
data
field using a grok pattern, only if the value is not
not logged in
.
data
read_only_udm.target.ip
Extracted from the
data
field using a grok pattern.
data
read_only_udm.target.process.pid
Extracted from the
data
field using a grok pattern.
read_only_udm.metadata.event_type
Set to
NETWORK_FTP
if target.ip exists, otherwise set to
GENERIC_EVENT
.
read_only_udm.metadata.log_type
Set to
FILEZILLA_FTP
.
read_only_udm.metadata.product_name
Set to
FILEZILLA
.
read_only_udm.metadata.vendor_name
Set to
FILEZILLA
.
Need more help?
Get answers from Community members and Google SecOps professionals.
