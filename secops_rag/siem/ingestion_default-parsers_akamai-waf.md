# Collect Akamai WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-waf/  
**Scraped:** 2026-03-05T09:18:41.960910Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akamai WAF logs
Supported in:
Google secops
SIEM
This document explains how to ingest Akamai WAF logs to Google Security Operations using the Akamai CEF Connector and Bindplane.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2016 or later or Linux host with systemd for Bindplane agent installation
A Linux server (recommended CentOS/RHEL/Ubuntu) with at least 2 CPU cores, 6GB RAM, 2GB free disk space for the Akamai CEF Connector
Java 8 (JRE 1.8) or later installed on the CEF Connector host
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements and that the proxy allowlists
*.cloudsecurity.akamaiapis.net
and
*.luna.akamaiapis.net
Privileged access to Akamai Control Center
An Akamai security configuration with App & API Protector, Kona Site Defender, Web Application Protector, Bot Manager, or Account Protector enabled
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
Enable SIEM integration in Akamai Control Center
Sign in to
Akamai Control Center
.
Under
WEB & DATA CENTER SECURITY
, click
Security Configuration
.
Open the security configuration and the appropriate version for which you want to collect SIEM data.
Click
Advanced Settings
and expand
Data collection for SIEM Integrations
.
Click
On
to enable SIEM.
Choose the security policies for which you want to export data:
All Security policies
: Select this to send SIEM data for events that violate any or all security policies within the security configuration.
Specific security policies
: Select this to send data regarding one or more specific security policies. Select the appropriate policies from the dropdown list.
Optional: If you use Account Protector and want to include the unencrypted username, turn on the
Include username
checkbox.
Optional: If you want to receive JA4 fingerprint information in SIEM events, turn on the
Include the JA4 Client TLS Fingerprint
checkbox.
Optional: If you want to exclude events belonging to a specific protection type and action, click
Add exception
. Select the protection and the associated actions you don't want SIEM to collect. Click
Save
.
Copy the value in the
Web Security Configuration ID
field. Save this ID for later use.
Click
Activate
to push your security configuration changes to the production network. Under
Network
, click
Production
, and then click
Activate
.
Set up a user to manage SIEM in Akamai Control Center
In
Akamai Control Center
, under
ACCOUNT ADMIN
, click
Identity & access
.
On the
Users and API Clients
tab, find the user you want to assign the role to or click the
Create user
button.
To assign the SIEM role to an existing user:
Open the user's account and click the
Edit roles
tab.
Find the appropriate group, click the
Roles
menu, and select the
Manage SIEM
role.
Click
Submit
.
To assign the SIEM role to a new user:
Click
Create user
.
Enter basic information for the user and go to the
Assign Roles
section.
Find the appropriate group, click the
Roles
menu, and select the
Manage SIEM
role.
Click
Save
.
Provision SIEM API credentials in Akamai Control Center
Visit the
Create authentication credentials
page in Akamai documentation.
Follow the steps to provision the SIEM API for the user you assigned to manage SIEM.
Copy and save the following credentials securely:
Access Token
Client Token
Client Secret
Base URL
Install Akamai CEF Connector
On your Linux server, download the latest CEF Connector distribution package from the
Akamai GitHub repository
.
Transfer the package to your server using either
wget
or SFTP.
Verify the SHA256 hash of the downloaded file to ensure integrity.
Extract the distribution package:
unzip
CEFConnector-<version>.zip
Navigate to the extracted directory:
cd
CEFConnector-<version>
To install the service, create a symbolic link to the startup script:
sudo
ln
-s
/path/to/CEFConnector-<version>/bin/AkamaiCEFConnector.sh
/etc/init.d/AkamaiCEFConnector
Configure Akamai CEF Connector
Navigate to the
config
directory within the CEF Connector installation:
cd
config
Open the
CEFConnector.properties
file using a text editor (for example,
nano
,
vi
):
sudo
nano
CEFConnector.properties
Configure the following required parameters:
# Akamai API Configuration
akamai.data.requesturlhost
=
https://cloudsecurity.akamaiapis.net
akamai.data.configs
=
<
YOUR_SECURITY_CONFIG_ID
>
akamai.data.timebased
=
false
akamai.data.limit
=
200000
# API Credentials (from Step: Provision SIEM API credentials)
akamai.data.accesstoken
=
<
YOUR_ACCESS_TOKEN
>
akamai.data.clienttoken
=
<
YOUR_CLIENT_TOKEN
>
akamai.data.clientsecret
=
<
YOUR_CLIENT_SECRET
>
akamai.data.baseurl
=
<
YOUR_BASE_URL
>
# CEF Format Configuration
akamai.cefformatheader
=
CEF:0|Akamai|akamai_siem|1.0|eventClassId()|name()|severity()
akamai.cefformatextension
=
act=appliedAction() app=${httpMessage.protocol} c6a2=ipv6src() c6a2Label="Source IPv6 Address" cs1=${attackData.rules} cs1Label="Rules" cs2=${attackData.ruleMessages} cs2Label="Rule Messages" cs3=${attackData.ruleData} cs3Label="Rule Data" cs4=${attackData.ruleSelectors} cs4Label="Rule Selectors" cs5=${attackData.clientReputation} cs5Label="Client Reputation" cs6=${attackData.apiId} cs6Label="API ID" devicePayloadId=${httpMessage.requestId} dhost=${httpMessage.host} dpt=${httpMessage.port} flexString1=${attackData.configId} flexString1Label="Security Config ID" flexString2=${attackData.policyId} flexString2Label="Firewall Policy Id" out=${httpMessage.bytes} request=requestURL() requestMethod=${httpMessage.method} src=${attackData.clientIP} start=${httpMessage.start} AkamaiSiemSlowPostAction=${attackData.slowPostAction} AkamaiSiemSlowPostRate=${attackData.slowPostRate} AkamaiSiemRuleVersions=${attackData.ruleVersions} AkamaiSiemRuleTags=${attackData.ruleTags} AkamaiSiemJA4=${identity.ja4} AkamaiSiemRuleActions=${attackData.ruleActions}
# Connector Pull Configuration
connector.refresh.period
=
60
connector.consumer.count
=
3
connector.retry
=
5
# Proxy Configuration (if applicable)
# connector.proxy.host=
# connector.proxy.port=
Replace the following placeholders with your actual values:
<YOUR_SECURITY_CONFIG_ID>
: The Web Security Configuration ID you copied earlier. For multiple configurations, separate IDs with semicolons (for example,
12345;67890
).
<YOUR_ACCESS_TOKEN>
: The access token from Akamai API credentials
<YOUR_CLIENT_TOKEN>
: The client token from Akamai API credentials
<YOUR_CLIENT_SECRET>
: The client secret from Akamai API credentials
<YOUR_BASE_URL>
: The base URL from Akamai API credentials
Save and close the file.
Configure CEF Connector logging
Navigate to the
config
directory within the CEF Connector installation.
Open the
log4j2.xml
file using a text editor:
sudo
nano
log4j2.xml
Configure the following parameters for syslog output to Bindplane:
<!--
Syslog
Appender
Configuration
-->
<Syslog
name="SyslogAppender"
host="<BINDPLANE_IP_ADDRESS>"
port="<BINDPLANE_PORT>"
protocol="<PROTOCOL>"
facility="LOCAL0"
format="RFC5424">
<PatternLayout
pattern="%m%n"/>
</Syslog>
Replace the following placeholders:
<BINDPLANE_IP_ADDRESS>
: The IP address of the server where Bindplane agent is installed
<BINDPLANE_PORT>
: The port number where Bindplane agent listens (for example,
514
for UDP or
601
for TCP)
<PROTOCOL>
: Select either
UDP
or
TCP
Ensure the CEF Connector sends logs to the remote syslog server (BindPpane) by configuring the CEF-specific settings:
# In CEFConnector.properties, ensure these are set:
# Note: These settings are typically in log4j2.xml but referenced here for clarity
Save and close the file.
Start Akamai CEF Connector
Start the CEF Connector service:
sudo
/etc/init.d/AkamaiCEFConnector
start
Verify the service is running:
sudo
/etc/init.d/AkamaiCEFConnector
status
Monitor the logs to ensure the connector is pulling events from Akamai and sending them to Bindplane:
tail
-f
/path/to/CEFConnector-<version>/bin/logs/cefconnector.log
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
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
tcplog
:
# Alternative TCP receiver if using TCP protocol
listen_address
:
"0.0.0.0:601"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in the Get ingestion authentication file section
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from the Get customer ID section
customer_id
:
<
YOUR_CUSTOMER_ID
>
# Select the appropriate regional endpoint based on where your Google SecOps instance is provisioned
# For regional endpoints, see: https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints
endpoint
:
malachiteingestion-pa.googleapis.com
# Set the log_type to ensure the correct parser is applied
log_type
:
'AKAMAI_WAF'
raw_log_field
:
body
# Add optional ingestion labels for better organization
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
# - tcplog  # Uncomment if using TCP
exporters
:
-
chronicle/chronicle_w_labels
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
Verify log ingestion
Sign in to the Google SecOps console.
Go to
Search
or
Raw Log Scan
.
Search for recent Akamai WAF logs using the ingestion label:
metadata.log_type = "AKAMAI_WAF"
Verify that logs are appearing with the expected fields and timestamps.
Check that the CEF format fields are being properly parsed and mapped to UDM.
Troubleshooting
CEF connector issues
No events being pulled
: Check the
cefconnector.log
file for errors. Verify that the Akamai API credentials are correct and that the security configuration IDs are valid.
Connection errors
: Ensure that the proxy settings (if applicable) are correctly configured and that the required domains are allowlisted.
Database reset
: If you need to reset the offset tracking, run:
sudo
/etc/init.d/AkamaiCEFConnector
resetdb
Bindplane agent issues
Logs not reaching Bindplane
: Verify that the CEF Connector is configured to send syslog to the correct Bindplane IP address and port. Check firewall rules between the CEF Connector and Bindplane agent.
Logs not reaching Google SecOps
: Verify the Bindplane configuration file, customer ID, and ingestion authentication path. Check Bindplane logs for errors:
sudo
journalctl
-u
observiq-otel-collector
-f
Network and connectivity
Verify that the CEF Connector can reach the Akamai SIEM API endpoints.
Verify that the Bindplane agent can reach the Google SecOps ingestion endpoint (
malachiteingestion-pa.googleapis.com
).
Check that all required firewall ports are open.
Retrieve past security events
The Akamai CEF Connector operates in two modes:
Offset-based
(recommended): The connector automatically logs security events as they're collected in near real-time. This is the default mode when
akamai.data.timebased
is set to
false
.
Time-based
: Lets you to retrieve events that occurred within a specific time period (up to 12 hours in the past).
To retrieve missing or past security events:
Open the connector's configuration file:
sudo
nano
/path/to/CEFConnector-<version>/config/CEFConnector.properties
Change the time-based configuration:
akamai.data.timebased
=
true
akamai.data.timebased.from
=
<
EPOCH_START_TIME
>
akamai.data.timebased.to
=
<
EPOCH_END_TIME
>
Replace
<EPOCH_START_TIME>
with the start time in epoch format (within the last 12 hours).
Replace
<EPOCH_END_TIME>
with the end time in epoch format (optional; if left blank, pulls events up to the present).
Restart the CEF Connector:
sudo
/etc/init.d/AkamaiCEFConnector
restart
After the historical data is retrieved, revert to offset mode:
akamai.data.timebased
=
false
Restart the CEF Connector again.
UDM Mapping Table
Log Field
UDM Mapping
Logic
src
(attackData.clientIP)
principal.ip
Source IP address of the client making the request
c6a2
(ipv6src)
principal.ip
Source IPv6 address if attackData.clientIP is in IPv6 format
dhost
(httpMessage.host)
target.hostname
Hostname from the HTTP HOST header
dpt
(httpMessage.port)
target.port
Port number used by the incoming request
requestMethod
(httpMessage.method)
network.http.method
HTTP method of the incoming request (GET, POST, etc.)
request
(requestURL)
target.url
Calculated full URL from httpMessage fields
cs1
(attackData.rules)
security_result.rule_id
Rule IDs of rules that triggered for this request
cs2
(attackData.ruleMessages)
security_result.rule_name
Messages of rules that triggered
act
(appliedAction)
security_result.action
Action taken (alert, deny, abort, etc.)
severity
security_result.severity
Calculated severity (5 for detect, 10 for mitigate)
cs5
(attackData.clientReputation)
security_result.threat_name
Client IP scores for Client Reputation
cs6
(attackData.apiId)
security_result.detection_fields
API ID for API Protection
start
(httpMessage.start)
metadata.event_timestamp
Time when the Edge Server initiated the connection (epoch format)
devicePayloadId
(httpMessage.requestId)
metadata.product_log_id
Globally unique ID of the message
flexString1
(attackData.configId)
security_result.detection_fields
ID of the Security Configuration applied to this request
flexString2
(attackData.policyId)
security_result.detection_fields
ID of the Firewall Policy applied to this request
AkamaiSiemJA4
(identity.ja4)
network.tls.client.ja3
JA4 client TLS fingerprint
Need more help?
Get answers from Community members and Google SecOps professionals.
