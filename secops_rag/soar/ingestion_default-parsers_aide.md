# Collect AIDE (Advanced Intrusion Detection Environment) logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aide/  
**Scraped:** 2026-03-05T09:49:23.443570Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AIDE (Advanced Intrusion Detection Environment) logs
Supported in:
Google secops
SIEM
This document explains how to ingest AIDE (Advanced Intrusion Detection Environment) logs to Google Security Operations using Bindplane. AIDE is a file integrity monitoring tool that detects changes to files on Linux/Unix systems.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Linux host with systemd running AIDE version 0.18 or later (for JSON format support)
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the AIDE configuration files
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
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
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
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'AIDE'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<CUSTOMER_ID>
with the actual customer ID.
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
Configure Syslog forwarding on AIDE
Open the AIDE configuration file:
sudo
vi
/etc/aide/aide.conf
Go to the reporting section.
Add the following configuration:
report_level
: Enter
list_entries
.
report_format
: Enter
json
(for AIDE 0.18+) or
plain
.
report_url
: Enter
syslog:authpriv
.
Example configuration:
report_level
=
list_entries
report_format
=
json
report_url
=
syslog:authpriv
Save the configuration.
Configure rsyslog to forward AIDE logs to the Bindplane agent. Open the rsyslog configuration:
sudo
vi
/etc/rsyslog.d/aide-forward.conf
Add the following configuration to forward
authpriv
facility logs to the Bindplane agent:
authpriv.* @<BINDPLANE_AGENT_IP>:514
Replace
<BINDPLANE_AGENT_IP>
with the IP address of the Bindplane agent host.
Use
@
for UDP or
@@
for TCP forwarding.
Restart rsyslog:
sudo
systemctl
restart
rsyslog
Initialize the AIDE database if this is a fresh installation:
sudo
aide
--init
sudo
mv
/var/lib/aide/aide.db.new
/var/lib/aide/aide.db
Test the configuration:
sudo
aide
--check
Set up automated checks using cron:
sudo
crontab
-e
Add the following line to run AIDE daily at 04:05 AM:
05
4
*
*
*
root
/
usr
/
sbin
/
aide
--
check
Need more help?
Get answers from Community members and Google SecOps professionals.
