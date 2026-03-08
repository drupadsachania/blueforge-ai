# Collect Claroty CTD logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-ctd/  
**Scraped:** 2026-03-05T09:53:05.066235Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Claroty CTD logs
Supported in:
Google secops
SIEM
This document explains how to ingest Claroty Continuous Threat Detection (CTD) logs to Google Security Operations by using Bindplane.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with
systemd
.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to Claroty CTD.
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
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds
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
CLAROTY_CTD
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
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
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
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog on Claroty Continuous Threat Detection (CTD)
Sign in to the
Claroty CTD
Web UI.
Go to
Menu
>
Integrations
>
Syslog
.
Repeat the following steps for each syslog
message content
type:
Alerts
Events
Health Monitoring
Insights
Activity Logs
Vulnerabilities
Click
+
to add a new configuration.
In the
Message Content
menu, select the required content to export.
Provide the following configuration details:
Category
: select
All
.
Type
: select
Select All
types.
Format
: select
CEF (Latest)
.
System URL
: do not update the system URL/IP, unless you're behind a proxy server.
Send to
: select
External Syslog server (e.g SIEM, SOAR systems)
.
Vendor
: select
Other
.
Syslog Server IP
: enter the Bindplane agent IP address.
Port
: enter the Bindplane agent port (for example,
514
).
Protocol
: select
UDP
(other options include TCP, TLS, or mTLS, depending on your Bindplane configuration).
Click
Save
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
CtdRealTime
metadata.event_timestamp
Parsed using
MMM dd yyyy HH:mm:ss
from CtdRealTime and used as the event timestamp.
CtdTimeGenerated
metadata.event_timestamp
If CtdRealTime is empty, parsed using
MMM dd yyyy HH:mm:ss
from CtdTimeGenerated to set the event timestamp.
CtdMessage
metadata.description
Sets metadata.description from the CtdMessage field.
CtdMessage
security_result.description
Sets security_result.description from the CtdMessage field when applicable.
Port (from CtdMessage KV)
principal.port
Extracted from the key
Port
in CtdMessage; converted to integer and set as principal.port.
Category (from CtdMessage KV)
security_result.detection_fields (Category_label)
Extracted from CtdMessage as key
Category
and merged into detection fields.
Access (from CtdMessage KV)
security_result.detection_fields (Access_label)
Extracted from CtdMessage as key
Access
and merged into detection fields.
CtdSite
principal.hostname
Maps CtdSite to principal.hostname.
CtdSite
principal.asset.hostname
Maps CtdSite to principal.asset.hostname.
CtdCpu
principal.resource.attribute.labels (CtdCpu_label)
Creates a label with key
CtdCpu
using CtdCpu's value and merges it into principal.resource.attribute.labels.
CtdMem
principal.resource.attribute.labels (CtdMem_label)
Creates a label with key
CtdMem
using CtdMem's value and merges it into principal.resource.attribute.labels.
CtdUsedOptIcsranger
principal.resource.attribute.labels (CtdUsedOptIcsranger_label)
Creates a label from CtdUsedOptIcsranger and merges it.
CtdUsedVar
principal.resource.attribute.labels (CtdUsedVar_label)
Creates a label from CtdUsedVar and merges it.
CtdUsedTmp
principal.resource.attribute.labels (CtdUsedTmp_label)
Creates a label from CtdUsedTmp and merges it.
CtdUsedEtc
principal.resource.attribute.labels (CtdUsedEtc_label)
Creates a label from CtdUsedEtc and merges it.
CtdBusyFd
principal.resource.attribute.labels (CtdBusyFd_label)
Creates a label from CtdBusyFd and merges it.
CtdBusySda
principal.resource.attribute.labels (CtdBusySda_label)
Creates a label from CtdBusySda and merges it.
CtdBusySdaA
principal.resource.attribute.labels (CtdBusySdaA_label)
Creates a label from CtdBusySdaA and merges it.
CtdBusySdaB
principal.resource.attribute.labels (CtdBusySdaB_label)
Creates a label from CtdBusySdaB and merges it.
CtdBusySr
principal.resource.attribute.labels (CtdBusySr_label)
Creates a label from CtdBusySr and merges it.
CtdBusyDm
principal.resource.attribute.labels (CtdBusyDm_label)
Creates a label from CtdBusyDm and merges it.
CtdBusyDmA
principal.resource.attribute.labels (CtdBusyDmA_label)
Creates a label from CtdBusyDmA and merges it.
CtdQuPreprocessingNg
principal.resource.attribute.labels (CtdQuPreprocessingNg_label)
Creates a label from CtdQuPreprocessingNg and merges it.
CtdQuBaselineTracker
principal.resource.attribute.labels (CtdQuBaselineTracker_label)
Creates a label from CtdQuBaselineTracker and merges it.
CtdQuBridge
principal.resource.attribute.labels (CtdQuBridge_label)
Creates a label from CtdQuBridge and merges it.
CtdQuCentralBridge
principal.resource.attribute.labels (CtdQuCentralBridge_label)
Creates a label from CtdQuCentralBridge and merges it.
CtdQuConcluding
principal.resource.attribute.labels (CtdQuConcluding_label)
Creates a label from CtdQuConcluding and merges it.
CtdQuDiodeFeeder
principal.resource.attribute.labels (CtdQuDiodeFeeder_label)
Creates a label from CtdQuDiodeFeeder and merges it.
CtdQuDissector
principal.resource.attribute.labels (CtdQuDissector_label)
Creates a label from CtdQuDissector and merges it.
CtdQuDissectorA
principal.resource.attribute.labels (CtdQuDissectorA_label)
Creates a label from CtdQuDissectorA and merges it.
CtdQuDissectorNg
principal.resource.attribute.labels (CtdQuDissectorNg_label)
Creates a label from CtdQuDissectorNg and merges it.
CtdQuIndicatorService
principal.resource.attribute.labels (CtdQuIndicatorService_label)
Creates a label from CtdQuIndicatorService and merges it.
CtdQuLeecher
principal.resource.attribute.labels (CtdQuLeecher_label)
Creates a label from CtdQuLeecher and merges it.
CtdQuMonitor
principal.resource.attribute.labels (CtdQuMonitor_label)
Creates a label from CtdQuMonitor and merges it.
CtdQuNetworkStatistics
principal.resource.attribute.labels (CtdQuNetworkStatistics_label)
Creates a label from CtdQuNetworkStatistics and merges it.
CtdQuPackets
principal.resource.attribute.labels (CtdQuPackets_label)
Creates a label from CtdQuPackets and merges it.
CtdQuPacketsErrors
principal.resource.attribute.labels (CtdQuPacketsErrors_label)
Creates a label from CtdQuPacketsErrors and merges it.
CtdQuPreprocessing
principal.resource.attribute.labels (CtdQuPreprocessing_label)
Creates a label from CtdQuPreprocessing and merges it.
CtdQuPriorityProcessing
principal.resource.attribute.labels (CtdQuPriorityProcessing_label)
Creates a label from CtdQuPriorityProcessing and merges it.
CtdQuProcessing
principal.resource.attribute.labels (CtdQuProcessing_label)
Creates a label from CtdQuProcessing and merges it.
CtdQuProcessingHigh
principal.resource.attribute.labels (CtdQuProcessingHigh_label)
Creates a label from CtdQuProcessingHigh and merges it.
CtdQuZordonUpdates
principal.resource.attribute.labels (CtdQuZordonUpdates_label)
Creates a label from CtdQuZordonUpdates and merges it.
CtdQuStatisticsNg
principal.resource.attribute.labels (CtdQuStatisticsNg_label)
Creates a label from CtdQuStatisticsNg and merges it.
CtdQueuePurge
principal.resource.attribute.labels (CtdQueuePurge_label)
Creates a label from CtdQueuePurge and merges it.
CtdQuSyslogAlerts
principal.resource.attribute.labels (CtdQuSyslogAlerts_label)
Creates a label from CtdQuSyslogAlerts and merges it.
CtdQuSyslogEvents
principal.resource.attribute.labels (CtdQuSyslogEvents_label)
Creates a label from CtdQuSyslogEvents and merges it.
CtdQuSyslogInsights
principal.resource.attribute.labels (CtdQuSyslogInsights_label)
Creates a label from CtdQuSyslogInsights and merges it.
CtdRdDissector
principal.resource.attribute.labels (CtdRdDissector_label)
Creates a label from CtdRdDissector and merges it.
CtdRdDissectorA
principal.resource.attribute.labels (CtdRdDissectorA_label)
Creates a label from CtdRdDissectorA and merges it.
CtdRdDissectorNg
principal.resource.attribute.labels (CtdRdDissectorNg_label)
Creates a label from CtdRdDissectorNg and merges it.
CtdRdPreprocessing
principal.resource.attribute.labels (CtdRdPreprocessing_label)
Creates a label from CtdRdPreprocessing and merges it.
CtdRdPreprocessingNg
principal.resource.attribute.labels (CtdRdPreprocessingNg_label)
Creates a label from CtdRdPreprocessingNg and merges it.
CtdSvcMariaDb
principal.resource.attribute.labels (CtdSvcMariaDb_label)
Creates a label from CtdSvcMariaDb and merges it.
CtdSvcPostgres
principal.resource.attribute.labels (CtdSvcPostgres_label)
Creates a label from CtdSvcPostgres and merges it.
CtdSvcRedis
principal.resource.attribute.labels (CtdSvcRedis_label)
Creates a label from CtdSvcRedis and merges it.
CtdSvcRabbitMq
principal.resource.attribute.labels (CtdSvcRabbitMq_label)
Creates a label from CtdSvcRabbitMq and merges it.
CtdSvcIcsranger
principal.resource.attribute.labels (CtdSvcIcsranger_label)
Creates a label from CtdSvcIcsranger and merges it.
CtdSvcWatchdog
principal.resource.attribute.labels (CtdSvcWatchdog_label)
Creates a label from CtdSvcWatchdog and merges it.
CtdSvcFirewalld
principal.resource.attribute.labels (CtdSvcFirewalld_label)
Creates a label from CtdSvcFirewalld and merges it.
CtdSvcNetunnel
principal.resource.attribute.labels (CtdSvcNetunnel_label)
Creates a label from CtdSvcNetunnel and merges it.
CtdSvcJwthenticator
principal.resource.attribute.labels (CtdSvcJwthenticator_label)
Creates a label from CtdSvcJwthenticator and merges it.
CtdSvcDocker
principal.resource.attribute.labels (CtdSvcDocker_label)
Creates a label from CtdSvcDocker and merges it.
CtdExceptions
principal.resource.attribute.labels (CtdExceptions_label)
Creates a label from CtdExceptions and merges it.
CtdInputPacketDrops
principal.resource.attribute.labels (CtdInputPacketDrops_label)
Creates a label from CtdInputPacketDrops and merges it.
CtdOutputPacketDrops
principal.resource.attribute.labels (CtdOutputPacketDrops_label)
Creates a label from CtdOutputPacketDrops and merges it.
CtdFullOutputPacketDrops
principal.resource.attribute.labels (CtdFullOutputPacketDrops_label)
Creates a label from CtdFullOutputPacketDrops and merges it.
CtdDissectorNgPacketDrops
principal.resource.attribute.labels (CtdDissectorNgPacketDrops_label)
Creates a label from CtdDissectorNgPacketDrops and merges it.
CtdTagArtifactsDropsPreprocessor
principal.resource.attribute.labels (CtdTagArtifactsDropsPreprocessor_label)
Creates a label from CtdTagArtifactsDropsPreprocessor and merges it.
CtdTagArtifactsDropsPreprocessorSum
principal.resource.attribute.labels (CtdTagArtifactsDropsPreprocessorSum_label)
Creates a label from CtdTagArtifactsDropsPreprocessorSum and merges it.
CtdTagArtifactsDropsProcessor
principal.resource.attribute.labels (CtdTagArtifactsDropsProcessor_label)
Creates a label from CtdTagArtifactsDropsProcessor and merges it.
CtdTagArtifactsDropsProcessorSum
principal.resource.attribute.labels (CtdTagArtifactsDropsProcessorSum_label)
Creates a label from CtdTagArtifactsDropsProcessorSum and merges it.
CtdTagArtifactsDropsSniffer
principal.resource.attribute.labels (CtdTagArtifactsDropsSniffer_label)
Creates a label from CtdTagArtifactsDropsSniffer and merges it.
CtdTagArtifactsDropsSnifferSum
principal.resource.attribute.labels (CtdTagArtifactsDropsSnifferSum_label)
Creates a label from CtdTagArtifactsDropsSnifferSum and merges it.
CtdTagArtifactsDropsDissectorPypy
principal.resource.attribute.labels (CtdTagArtifactsDropsDissectorPypy_label)
Creates a label from CtdTagArtifactsDropsDissectorPypy and merges it.
CtdTagArtifactsDropsDissectorPypySum
principal.resource.attribute.labels (CtdTagArtifactsDropsDissectorPypySum_label)
Creates a label from CtdTagArtifactsDropsDissectorPypySum and merges it.
CtdCapsaverFolderCleanup
principal.resource.attribute.labels (CtdCapsaverFolderCleanup_label)
Creates a label from CtdCapsaverFolderCleanup and merges it.
CtdCapsaverUtilzationTest
principal.resource.attribute.labels (CtdCapsaverUtilzationTest_label)
Creates a label from CtdCapsaverUtilzationTest and merges it.
CtdYaraScannerTest
principal.resource.attribute.labels (CtdYaraScannerTest_label)
Creates a label from CtdYaraScannerTest and merges it.
CtdWrkrWorkersStop
principal.resource.attribute.labels (CtdWrkrWorkersStop_label)
Creates a label from CtdWrkrWorkersStop and merges it.
CtdWrkrWorkersRestart
principal.resource.attribute.labels (CtdWrkrWorkersRestart_label)
Creates a label from CtdWrkrWorkersRestart and merges it.
CtdWrkrActiveExecuter
principal.resource.attribute.labels (CtdWrkrActiveExecuter_label)
Creates a label from CtdWrkrActiveExecuter and merges it.
CtdWrkrSensor
principal.resource.attribute.labels (CtdWrkrSensor_label)
Creates a label from CtdWrkrSensor and merges it.
CtdWrkrAuthentication
principal.resource.attribute.labels (CtdWrkrAuthentication_label)
Creates a label from CtdWrkrAuthentication and merges it.
CtdWrkrMitre
principal.resource.attribute.labels (CtdWrkrMitre_label)
Creates a label from CtdWrkrMitre and merges it.
CtdWrkrNotifications
principal.resource.attribute.labels (CtdWrkrNotifications_label)
Creates a label from CtdWrkrNotifications and merges it.
CtdWrkrProcessor
principal.resource.attribute.labels (CtdWrkrProcessor_label)
Creates a label from CtdWrkrProcessor and merges it.
CtdWrkrCloudAgent
principal.resource.attribute.labels (CtdWrkrCloudAgent_label)
Creates a label from CtdWrkrCloudAgent and merges it.
CtdWrkrCloudClient
principal.resource.attribute.labels (CtdWrkrCloudClient_label)
Creates a label from CtdWrkrCloudClient and merges it.
CtdWrkrScheduler
principal.resource.attribute.labels (CtdWrkrScheduler_label)
Creates a label from CtdWrkrScheduler and merges it.
CtdWrkrknownThreats
principal.resource.attribute.labels (CtdWrkrknownThreats_label)
Creates a label from CtdWrkrknownThreats and merges it.
CtdWrkrCacher
principal.resource.attribute.labels (CtdWrkrCacher_label)
Creates a label from CtdWrkrCacher and merges it.
CtdWrkrInsights
principal.resource.attribute.labels (CtdWrkrInsights_label)
Creates a label from CtdWrkrInsights and merges it.
CtdWrkrActive
principal.resource.attribute.labels (CtdWrkrActive_label)
Creates a label from CtdWrkrActive and merges it.
CtdWrkrEnricher
principal.resource.attribute.labels (CtdWrkrEnricher_label)
Creates a label from CtdWrkrEnricher and merges it.
CtdWrkrIndicators
principal.resource.attribute.labels (CtdWrkrIndicators_label)
Creates a label from CtdWrkrIndicators and merges it.
CtdWrkrIndicatorsApi
principal.resource.attribute.labels (CtdWrkrIndicatorsApi_label)
Creates a label from CtdWrkrIndicatorsApi and merges it.
CtdWrkrConcluder
principal.resource.attribute.labels (CtdWrkrConcluder_label)
Creates a label from CtdWrkrConcluder and merges it.
CtdWrkrPreprocessor
principal.resource.attribute.labels (CtdWrkrPreprocessor_label)
Creates a label from CtdWrkrPreprocessor and merges it.
CtdWrkrLeecher
principal.resource.attribute.labels (CtdWrkrLeecher_label)
Creates a label from CtdWrkrLeecher and merges it.
CtdWrkrSyncManager
principal.resource.attribute.labels (CtdWrkrSyncManager_label)
Creates a label from CtdWrkrSyncManager and merges it.
CtdWrkrBridge
principal.resource.attribute.labels (CtdWrkrBridge_label)
Creates a label from CtdWrkrBridge and merges it.
CtdWrkrWebRanger
principal.resource.attribute.labels (CtdWrkrWebRanger_label)
Creates a label from CtdWrkrWebRanger and merges it.
CtdWrkrWebWs
principal.resource.attribute.labels (CtdWrkrWebWs_label)
Creates a label from CtdWrkrWebWs and merges it.
CtdWrkrWebAuth
principal.resource.attribute.labels (CtdWrkrWebAuth_label)
Creates a label from CtdWrkrWebAuth and merges it.
CtdWrkrWebNginx
principal.resource.attribute.labels (CtdWrkrWebNginx_label)
Creates a label from CtdWrkrWebNginx and merges it.
CtdWrkrConfigurator
principal.resource.attribute.labels (CtdWrkrConfigurator_label)
Creates a label from CtdWrkrConfigurator and merges it.
CtdWrkrConfiguratorNginx
principal.resource.attribute.labels (CtdWrkrConfiguratorNginx_label)
Creates a label from CtdWrkrConfiguratorNginx and merges it.
CtdWrkrCapsaver
principal.resource.attribute.labels (CtdWrkrCapsaver_label)
Creates a label from CtdWrkrCapsaver and merges it.
CtdWrkrBaselineTracker
principal.resource.attribute.labels (CtdWrkrBaselineTracker_label)
Creates a label from CtdWrkrBaselineTracker and merges it.
CtdWrkrDissector
principal.resource.attribute.labels (CtdWrkrDissector_label)
Creates a label from CtdWrkrDissector and merges it.
CtdWrkrDissectorA
principal.resource.attribute.labels (CtdWrkrDissectorA_label)
Creates a label from CtdWrkrDissectorA and merges it.
CtdWrkrDissectorNg
principal.resource.attribute.labels (CtdWrkrDissectorNg_label)
Creates a label from CtdWrkrDissectorNg and merges it.
CtdWrkrPreprocessing
principal.resource.attribute.labels (CtdWrkrPreprocessing_label)
Creates a label from CtdWrkrPreprocessing and merges it.
CtdWrkrPreprocessingNg
principal.resource.attribute.labels (CtdWrkrPreprocessingNg_label)
Creates a label from CtdWrkrPreprocessingNg and merges it.
CtdWrkrStatisticsNg
principal.resource.attribute.labels (CtdWrkrStatisticsNg_label)
Creates a label from CtdWrkrStatisticsNg and merges it.
CtdWrkrSyslogAlerts
principal.resource.attribute.labels (CtdWrkrSyslogAlerts_label)
Creates a label from CtdWrkrSyslogAlerts and merges it.
CtdWrkrSyslogEvents
principal.resource.attribute.labels (CtdWrkrSyslogEvents_label)
Creates a label from CtdWrkrSyslogEvents and merges it.
CtdWrkrSyslogInsights
principal.resource.attribute.labels (CtdWrkrSyslogInsights_label)
Creates a label from CtdWrkrSyslogInsights and merges it.
CtdWrkrRdDissector
principal.resource.attribute.labels (CtdWrkrRdDissector_label)
Creates a label from CtdWrkrRdDissector and merges it.
CtdWrkrRdDissectorA
principal.resource.attribute.labels (CtdWrkrRdDissectorA_label)
Creates a label from CtdWrkrRdDissectorA and merges it.
CtdSensorName
principal.resource.attribute.labels (CtdSensorName_label)
Creates a label from CtdSensorName and merges it.
CtdCtrlSite
principal.resource.attribute.labels (CtdCtrlSite_label)
Creates a label from CtdCtrlSite and merges it.
CtdLoopCallDurationBaselineTrackerWrkerHandleNetworkStatistics
principal.resource.attribute.labels (CtdLoopCallDurationBaselineTrackerWrkerHandleNetworkStatistics_label)
Creates a label from CtdLoopCallDurationBaselineTrackerWrkerHandleNetworkStatistics and merges it.
CtdDissectionCoverage
principal.resource.attribute.labels (CtdDissectionCoverage_label)
Creates a label from CtdDissectionCoverage and merges it.
CtdDissectionEfficiencyModbus
principal.resource.attribute.labels (CtdDissectionEfficiencyModbus_label)
Creates a label from CtdDissectionEfficiencyModbus and merges it.
CtdDissectionEfficiencySmb
principal.resource.attribute.labels (CtdDissectionEfficiencySmb_label)
Creates a label from CtdDissectionEfficiencySmb and merges it.
CtdDissectionEfficiencyDcerpc
principal.resource.attribute.labels (CtdDissectionEfficiencyDcerpc_label)
Creates a label from CtdDissectionEfficiencyDcerpc and merges it.
CtdDissectionEfficiencyZabbix
principal.resource.attribute.labels (CtdDissectionEfficiencyZabbix_label)
Creates a label from CtdDissectionEfficiencyZabbix and merges it.
CtdDissectionEfficiencyFactorytalkRna
principal.resource.attribute.labels (CtdDissectionEfficiencyFactorytalkRna_label)
Creates a label from CtdDissectionEfficiencyFactorytalkRna and merges it.
CtdDissectionEfficiencySsl
principal.resource.attribute.labels (CtdDissectionEfficiencySsl_label)
Creates a label from CtdDissectionEfficiencySsl and merges it.
CtdDissectionEfficiencyVrrpProtocolMatcher
principal.resource.attribute.labels (CtdDissectionEfficiencyVrrpProtocolMatcher_label)
Creates a label from CtdDissectionEfficiencyVrrpProtocolMatcher and merges it.
CtdDissectionEfficiencyRdp
principal.resource.attribute.labels (CtdDissectionEfficiencyRdp_label)
Creates a label from CtdDissectionEfficiencyRdp and merges it.
CtdDissectionEfficiencySsh
principal.resource.attribute.labels (CtdDissectionEfficiencySsh_label)
Creates a label from CtdDissectionEfficiencySsh and merges it.
CtdDissectionEfficiencyHttp
principal.resource.attribute.labels (CtdDissectionEfficiencyHttp_label)
Creates a label from CtdDissectionEfficiencyHttp and merges it.
CtdDissectionEfficiencyTcpHttp
principal.resource.attribute.labels (CtdDissectionEfficiencyTcpHttp_label)
Creates a label from CtdDissectionEfficiencyTcpHttp and merges it.
CtdDissectionEfficiencyLdap
principal.resource.attribute.labels (CtdDissectionEfficiencyLdap_label)
Creates a label from CtdDissectionEfficiencyLdap and merges it.
CtdDissectionEfficiencyJrmi
principal.resource.attribute.labels (CtdDissectionEfficiencyJrmi_label)
Creates a label from CtdDissectionEfficiencyJrmi and merges it.
CtdDissectionEfficiencyGeIfix
principal.resource.attribute.labels (CtdDissectionEfficiencyGeIfix_label)
Creates a label from CtdDissectionEfficiencyGeIfix and merges it.
CtdDissectionEfficiencyLlc
principal.resource.attribute.labels (CtdDissectionEfficiencyLlc_label)
Creates a label from CtdDissectionEfficiencyLlc and merges it.
CtdDissectionEfficiencyMatrikonNopc
principal.resource.attribute.labels (CtdDissectionEfficiencyMatrikonNopc_label)
Creates a label from CtdDissectionEfficiencyMatrikonNopc and merges it.
CtdDissectionEfficiencyVnc
principal.resource.attribute.labels (CtdDissectionEfficiencyVnc_label)
Creates a label from CtdDissectionEfficiencyVnc and merges it.
CtdUnhandledEvents
principal.resource.attribute.labels (CtdUnhandledEvents_label)
Creates a label from CtdUnhandledEvents and merges it.
CtdConcludeTime
principal.resource.attribute.labels (CtdConcludeTime_label)
Creates a label from CtdConcludeTime and merges it.
CtdMysqlQuery
principal.resource.attribute.labels (CtdMysqlQuery_label)
Creates a label from CtdMysqlQuery and merges it.
CtdPostgresQuery
principal.resource.attribute.labels (CtdPostgresQuery_label)
Creates a label from CtdPostgresQuery and merges it.
CtdPsqlIdleSessions
principal.resource.attribute.labels (CtdPsqlIdleSessions_label)
Creates a label from CtdPsqlIdleSessions and merges it.
CtdPsqlIdleInTransactionSessions
principal.resource.attribute.labels (CtdPsqlIdleInTransactionSessions_label)
Creates a label from CtdPsqlIdleInTransactionSessions and merges it.
CtdSnifferStatus
principal.resource.attribute.labels (CtdSnifferStatus_label)
Creates a label from CtdSnifferStatus and merges it.
CtdLoopCallDurationPollObjects
principal.resource.attribute.labels (CtdLoopCallDurationPollObjects_label)
Creates a label from CtdLoopCallDurationPollObjects and merges it.
CtdLoopCallDurationCloudClientWrkrBaseRunCloudConnected
principal.resource.attribute.labels (CtdLoopCallDurationCloudClientWrkrBaseRunCloudConnected_label)
Creates a label from CtdLoopCallDurationCloudClientWrkrBaseRunCloudConnected and merges it.
CtdSnifferStatusCentral
principal.resource.attribute.labels (CtdSnifferStatusCentral_label)
Creates a label from CtdSnifferStatusCentral and merges it.
CtdSnifferStatusSite
principal.resource.attribute.labels (CtdSnifferStatusSite_label)
Creates a label from CtdSnifferStatusSite and merges it.
CtdWrkrMailer
principal.resource.attribute.labels (CtdWrkrMailer_label)
Creates a label from CtdWrkrMailer and merges it.
CtdDroppedEntities
principal.resource.attribute.labels (CtdDroppedEntities_label)
Creates a label from CtdDroppedEntities and merges it.
externalId
metadata.product_log_id
Maps externalId to metadata.product_log_id.
proto
protocol_number_src
Converts proto to uppercase and assigns it to protocol_number_src for lookup.
protocol_number_src
ip_protocol_out; app_protocol_out
Initializes ip_protocol_out to
UNKNOWN_IP_PROTOCOL
and app_protocol_out to
UNKNOWN_APPLICATION_PROTOCOL
, then updates based on lookup.
ip_protocol_out
network.ip_protocol
Sets network.ip_protocol from ip_protocol_out.
app_protocol_out
network.application_protocol
Sets network.application_protocol from app_protocol_out.
CtdExternalId
metadata.product_log_id
Overwrites metadata.product_log_id with CtdExternalId if provided.
CtdDeviceExternalId
principal.resource.attribute.labels (ctd_device_label)
Creates a label from CtdDeviceExternalId (prefixed with
CtdDeviceExternalId
) and merges it.
(if has_principal_device is true and ctdeventtype =
Login
)
security_result.category; security_result.action
For Login events, sets security_result.category to
AUTH_VIOLATION
and action to
BLOCK
.
(if has_principal_device is true and ctdeventtype =
Memory Reset
)
security_result.category
Sets security_result.category to
SOFTWARE_SUSPICIOUS
.
(if target_machine_id_present is true, has_principal_device is true, and ctdeventtype in [
Known Threat Alert
,
Known Threat Event
,
Man-in-the-Middle Attack
,
Suspicious Activity
])
security_result.category
Sets security_result.category to
NETWORK_MALICIOUS
.
(if target_machine_id_present is true, has_principal_device is true, and ctdeventtype =
Suspicious File Transfer
)
security_result.category
Sets security_result.category to
NETWORK_SUSPICIOUS
.
(if target_machine_id_present is true, has_principal_device is true, and ctdeventtype =
Denial Of Service
)
security_result.category
Sets security_result.category to
NETWORK_DENIAL_OF_SERVICE
.
(if has_principal_device is true and ctdeventtype in [
Host Scan
,
Port Scan
])
security_result.category
Sets security_result.category to
NETWORK_RECON
.
(if target_machine_id_present is true, has_principal_device is true, and ctdeventtype in [
Policy Rule Match
,
Policy Violation Alert
,
Policy Violation
])
security_result.category
Sets security_result.category to
POLICY_VIOLATION
.
(default if has_principal_device is true)
security_result.category
Sets security_result.category to
NETWORK_SUSPICIOUS
by default.
Derived security_result_category
security_result.category
Merges the derived security category into security_result.category.
Derived security_result_action
security_result.action
Merges the derived security action into security_result.action (if set).
cs6 (with cs6Label
CTDlink
)
metadata.url_back_to_product; security_result.url_back_to_product
Sets URL fields from cs6 for back-linking to product details.
cs1 (with cs1Label
SourceAssetType
)
principal.asset.category; principal.asset.type
Sets principal.asset.category from cs1 and determines principal.asset.type based on its value.
cs2 (with cs2Label
DestAssetType
)
target.asset.category; target.asset.type
Sets target.asset.category from cs2 and determines target.asset.type based on its value.
cfp1 (with cfp1Label
CVEScore
)
vulns.vulnerabilities.cvss_base_score
Sets vulns.vulnerabilities.cvss_base_score (converted to float) and marks vul_fields_present true.
cs6 (with cs6Label
CVE
)
vulns.vulnerabilities.cve_id
Sets vulns.vulnerabilities.cve_id and marks vul_fields_present true.
cn1 (with cn1Label
IndicatorScore
)
security_result.confidence_score
Extracts indicator score from cn1, converts to float, and assigns it as the confidence score.
filepath
about.file.full_path; security_result.about.file.full_path
Maps filepath to about.file.full_path and security_result.about.file.full_path.
(if eventclass =
HealthCheck
and cs1Label =
Site
)
intermediary.location.name
Sets intermediary.location.name from cs1 when used as a site identifier.
cn1 (with cn1Label)
additional.fields (cn1_label)
Creates an additional field label from cn1 and merges it into additional.fields.
cs1 (with cs1Label)
additional.fields (cs1_label)
Creates an additional field label from cs1 and merges it into additional.fields.
cs2 (with cs2Label)
additional.fields (cs2_label)
Creates an additional field label from cs2 and merges it into additional.fields.
cs3 (with cs3Label)
additional.fields (cs3_label)
Creates an additional field label from cs3 and merges it.
cs4 (with cs4Label)
additional.fields (cs4_label)
Creates an additional field label from cs4 and merges it.
cs6 (with cs6Label)
additional.fields (cs6_label)
Creates an additional field label from cs6 and merges it.
(for Insight events based on event_name and vul_fields_present)
event_type
Derives event_type for Insight events (e.g. SCAN_VULN_HOST, STATUS_UNCATEGORIZED, STATUS_UPDATE).
(for Event/Alert events based on ctdeventtype, has_principal_device, etc.)
event_type; (optionally target.resource.type or auth.type)
Derives event_type for Event/Alert events such as DEVICE_CONFIG_UPDATE, DEVICE_PROGRAM_DOWNLOAD/UPLOAD, NETWORK_UNCATEGORIZED, USER_RESOURCE_CREATION, SCAN_HOST, SCAN_NETWORK, SETTING_MODIFICATION, USER_LOGIN, NETWORK_CONNECTION or STATUS_UPDATE.
(if event_type remains empty)
event_type
Sets event_type to NETWORK_CONNECTION, USER_RESOURCE_ACCESS, or STATUS_UPDATE based on available flags.
event_type (final)
metadata.event_type
Copies the final event_type into metadata.event_type; defaults to
GENERIC_EVENT
if empty.
device_vendor
metadata.vendor_name
Sets metadata.vendor_name from device_vendor; defaults to
CLAROTY
if missing.
device_product
metadata.product_name
Sets metadata.product_name from device_product; defaults to
CTD
if missing.
device_version
metadata.product_version
Sets metadata.product_version from device_version.
security_description (if matching
ET TROJAN …
)
security_result.threat_name
Extracts threat_name using the pattern
ET TROJAN (?P<threat_name>\S+)
from security_description and maps it to security_result.threat_name.
metadata
event.idm.read_only_udm.metadata
Renames metadata to event.idm.read_only_udm.metadata.
principal
event.idm.read_only_udm.principal
Renames principal to event.idm.read_only_udm.principal.
target
event.idm.read_only_udm.target
Renames target to event.idm.read_only_udm.target.
network
event.idm.read_only_udm.network
Renames network to event.idm.read_only_udm.network.
additional
event.idm.read_only_udm.additional
Renames additional to event.idm.read_only_udm.additional.
security_result
event.idm.read_only_udm.security_result
Merges security_result into event.idm.read_only_udm.security_result.
about
event.idm.read_only_udm.about
Merges about into event.idm.read_only_udm.about.
intermediary
event.idm.read_only_udm.intermediary
Merges intermediary into event.idm.read_only_udm.intermediary.
vulns.vulnerabilities
event.idm.read_only_udm.extensions.vulns.vulnerabilities
Merges vulns.vulnerabilities into event.idm.read_only_udm.extensions.vulns.vulnerabilities.
@output
event
Merges the complete UDM event structure into the final
event
field.
Need more help?
Get answers from Community members and Google SecOps professionals.
