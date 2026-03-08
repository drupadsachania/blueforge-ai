# Supported log types and default parsers

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers/  
**Scraped:** 2026-03-05T09:16:20.373831Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Supported log types and default parsers
This document contains information about Google Security Operations integrations 
for data ingestion. It summarizes the devices and the associated ingestion 
label (
log_type
) field in the Ingestion API and
data_type
in a Forwarder 
configuration) that Google SecOps supports.
For information on how to request or create log types, see
Request prebuilt and create custom log types
.
Supported log types with a default parser
Supported log types without a default parser
Supported log types with a default parser
Parsers normalize raw log data into structured Unified Data Model (UDM) format. This
section lists supported devices, and the associated ingestion label (
log_type
field in the
Ingestion API and
data_type
in a Forwarder configuration), that also have a prebuilt default parser.
The default parser is supported by Google SecOps as long as the device's
raw logs are received in the required format.
For a list of supported log types without a default parser, see
Supported log types without a default parser
.
The
Format
column indicates the high-level structure of the raw log, as:
CSV: Comma Separated Values
JSON: JavaScript Object Notation
SYSLOG: syslog formatted message
KV: key-value pair
XML: Extensible Markup Language
SYSLOG + KV: syslog header with key-value body
SYSLOG + JSON: syslog header with JSON body
SYSLOG + XML: syslog header with XML body
LEEF: Log Event Extended Format
CEF: Common Event Format
These changes are applied to newly ingested logs. Parser changes are not applied
retroactively to previously ingested logs.
Vendor / Product
Category
Ingestion label
Format
Latest Update
HCL BigFix
Network Management and Optimization
HCL_BIGFIX
JSON
2023-12-08
View Change
Atlassian Bitbucket
Atlassian Bitbucket
ATLASSIAN_BITBUCKET
JSON
2023-06-12
View Change
SailPoint IAM
Identity and Access Management
SAILPOINT_IAM
JSON
2025-08-29
View Change
Clearswift
Information Security
CLEARSWIFT
SYSLOG
2023-11-22
View Change
Ingrian Networks DataSecure Appliance
System and Audit Logs
INGRIAN_NETWORKS_DATASECURE_APPLIANCE
Syslog
2024-10-31
View Change
IBM Security Verify SaaS
SaaS Application
IBM_SECURITY_VERIFY_SAAS
JSON
2023-10-27
View Change
Microsoft Intune
Mobile Device Management
AZURE_MDM_INTUNE
JSON
2025-12-26
View Change
AWS S3 Server Access
AWS Specific
AWS_S3_SERVER_ACCESS
SYSLOG
2025-06-11
View Change
Kyriba Treasury Management
SaaS Application
KYRIBA
CSV
2021-02-24
Box
Collaboration
BOX
JSON
2026-01-12
View Change
Looker Audit
endpoints
LOOKER_AUDIT
JSON
2025-03-13
View Change
Trend Micro Apex one
Endpoint Security
TRENDMICRO_APEX_ONE
SYSLOG + KV
2025-10-01
View Change
Cloudflare Pageshield
OS Logs
CLOUDFLARE_PAGESHIELD
JSON
2025-03-05
View Change
Honeyd
Deception Software
HONEYD
SYSLOG
2024-05-26
View Change
Netscout Arbor Sightline
Monitoring
ARBOR_SIGHTLINE
SYSLOG + JSON
2025-04-22
View Change
HPE BladeSystem C7000
BladeSystem C7000
HPE_BLADESYSTEM_C7000
SYSLOG
2024-04-08
View Change
Proofpoint CASB
CASB
PROOFPOINT_CASB
JSON
2026-01-16
View Change
HP Aruba (ClearPass)
Identity and Access Management
CLEARPASS
SYSLOG + KV
2026-01-20
View Change
IBM CICS
Service Bus
IBM_CICS
LEEF
2021-10-27
Skybox Firewall Assurance
Firewall
SKYBOX_FIREWALL_ASSURANCE
SYSLOG + KV
2023-09-07
View Change
reCAPTCHA Enterprise
Access Management
GCP_RECAPTCHA_ENTERPRISE
JSON
2024-02-12
View Change
Ergon Informatik Airlock IAM
Application Whitelisting
ERGON_INFORMATIK_AIRLOCK_IAM
SYSLOG
2024-08-28
View Change
Cisco NX-OS
OS
CISCO_NX_OS
SYSLOG
2025-07-02
View Change
AMD Pensando DSS Firewall
Firewall
AMD_DSS_FIREWALL
SYSLOG + CSV
2023-05-08
View Change
Forgerock OpenIdM
DATA SECURITY
FORGEROCK_OPENIDM
JSON
2025-02-13
View Change
OSSEC
IDS/IPS
OSSEC
SYSLOG
2024-04-24
View Change
Salesforce Commerce Cloud
SaaS Application
SALESFORCE_COMMERCE_CLOUD
SYSLOG, JSON
2024-10-03
View Change
Ionix
SECURITY
IONIX
JSON
2025-10-22
View Change
VMware ESXi
Hypervisor
VMWARE_ESX
SYSLOG, JSON
2026-01-27
View Change
CA Privileged Access Manager
NA
BROADCOM_CA_PAM
SYSLOG
2024-11-07
View Change
Nexus Sonatype
Storage
NEXUS_SONATYPE
JSON+SYSLOG
2025-11-18
View Change
Infoblox
DHCP, DNS
INFOBLOX
SYSLOG
2025-08-28
View Change
URLScan IO
Vulnerability scanners
URLSCAN_IO
JSON
2024-10-25
View Change
Cato Networks
NDR
CATO_NETWORKS
JSON
2026-01-09
View Change
Emerging Threats Pro
IOC
ET_PRO_IOC
CSV
2022-11-28
View Change
OpenSSH
Logging and Troubleshooting
OPENSSH
SYSLOG
2024-01-23
View Change
Fortinet Fortimanager
Network Management and Optimization software.
FORTINET_FORTIMANAGER
KV + SYSLOG
2026-01-16
View Change
Thales Luna Hardware Security Module
THALES_LUNA_HSM specific
THALES_LUNA_HSM
JSON/SYSLOG
2025-09-12
View Change
Barracuda CloudGen Firewall
SaaS Applications
BARRACUDA_CLOUDGEN_FIREWALL
Syslog
2025-02-10
View Change
GMV Checker ATM Security
ATM Audit
GMV_CHECKER
SYSLOG, SYSLOG + KV
2025-11-07
View Change
Nagios Infrastructure Monitoring
NETWORK MONITORING
NAGIOS
CSV
2024-08-22
View Change
Alveo Risk Data Management
SaaS Applications
ALVEO_RDM
JSON
2025-03-06
View Change
Citrix Monitor
Monitoring of DaaS
CITRIX_MONITOR
JSON
2022-12-06
View Change
IBM-i Operating System
I Operating System
IBM_I
Syslog CEF
2025-07-30
View Change
Security Command Center Posture Violation
Google Cloud Specific
GCP_SECURITYCENTER_POSTURE_VIOLATION
JSON
2025-12-04
View Change
NetApp ONTAP
Rest api
NETAPP_ONTAP
SYSLOG
2026-01-01
View Change
Halcyon Anti Ransomware
AV and endpoint logs
HALCYON
JSON
2025-09-17
View Change
PostFix Mail
Email Server
POSTFIX_MAIL
SYSLOG
2026-01-23
View Change
CyberArk Endpoint Privilege Manager (EPM)
EPM
CYBERARK_EPM
JSON
2025-09-12
View Change
Ops Genie
Web Proxy log types
OPS_GENIE
JSON
2025-02-19
View Change
Duo User Context
Identity and Access Management
DUO_USER_CONTEXT
JSON
2024-05-31
View Change
HP Procurve Switch
Switches
HP_PROCURVE
SYSLOG
2025-11-12
View Change
Security Command Center Chokepoint
Google Cloud Specific
GCP_SECURITYCENTER_CHOKEPOINT
JSON
2025-12-04
View Change
F5 Distributed Cloud Services
SaaS Applications
F5_DCS
JSON
2025-12-18
View Change
GCP_APP_ENGINE
Cloud Computing
GCP_APP_ENGINE
JSON and KV
2025-12-29
View Change
Swift Alliance Messaging Hub
Finance
SWIFT_AMH
JSON
2025-11-26
View Change
Armis Activities
ACTIVITIES
ARMIS_ACTIVITIES
JSON
2025-10-23
View Change
Cloud SQL Context
Google Cloud Specific
GCP_SQL_CONTEXT
JSON
2023-07-26
View Change
Juniper
Firewall
JUNIPER_FIREWALL
SYSLOG + KV + JSON
2025-09-19
View Change
IBM Guardium
Database DLP
GUARDIUM
CSV, CEF, LEEF
2025-01-28
View Change
JAMF Security Cloud
Automation and DevOps Tools
JAMF_SECURITY_CLOUD
JSON
2025-03-23
View Change
Zix Email Encryption
Email Server
ZIX_EMAIL_ENCRYPTION
SYSLOG
2024-05-10
View Change
CircleCI
Automation and DevOps Tools
CIRCLECI
CSV + JSON
2025-05-15
View Change
F5 VPN
VPN
F5_VPN
SYSLOG, KV
2024-10-23
View Change
Windows Network Policy Server
Authentication
WINDOWS_NET_POLICY_SERVER
SYSLOG, JSON, SYSLOG + XML
2024-12-26
View Change
Cloudian hyperstore
Storage Solutions
CLOUDIAN_HYPERSTORE
SYSLOG
2021-05-05
Google Cloud IAM Analysis
Google Cloud Resources Contexts
N/A
JSON
2023-02-27
View Change
McAfee IPS
IDS/IPS
MCAFEE_IPS
SYSLOG
2025-08-13
View Change
Evision FircoSoft
Infrastructure
EVISION_FIRCOSOFT
SYSLOG
2023-11-22
View Change
IBM Cloud Activity Tracker
Security Log
IBM_CLOUD_ACTIVITY_TRACKER
JSON
2025-05-29
View Change
NetIQ eDirectory
Identity management deployments
NETIQ_EDIRECTORY
Syslog, CEF
2025-02-17
View Change
SAP Netweaver
Database
SAP_NETWEAVER
JSON
2023-05-03
View Change
SOTI MobiControl
Mobile Device Management
SOTI_MOBICONTROL
SYSLOG
2023-09-08
View Change
Colinet Trotta GAUS SEGUROS
Alert
CT_GAUS_SEGUROS
CSV
2024-12-06
View Change
Terraform Enterprise Audit
IT infrastructure
TERRAFORM_ENTERPRISE
JSON, KV, SYSLOG
2025-06-23
View Change
Rubrik Polaris
Data Security
RUBRIK_POLARIS
JSON
2024-05-27
View Change
Cisco Umbrella Web Proxy
Web Proxy
UMBRELLA_WEBPROXY
CSV
2025-11-11
View Change
Gitlab
SAAS
GITLAB
JSON,SYSLOG + JSON
2025-05-19
View Change
1Password Audit Events
Identity and Access Management
ONEPASSWORD_AUDIT_EVENTS
JSON
2025-02-17
View Change
Armis Vulnerabilities
VULNERABILITIES
ARMIS_VULNERABILITIES
JSON
2023-02-07
View Change
Imperva Attack Analytics
WAF
IMPERVA_ATTACK_ANALYTICS
KV
2024-11-07
View Change
IBM zSecure Alert
Alert log types
IBM_ZSECURE_ALERT
SYSLOG
2025-06-19
View Change
VyOS Open Source Router
DHCP
VYOS
SYSLOG
2022-10-12
View Change
Azure Storage Audit
Storage
AZURE_STORAGE_AUDIT
JSON
2025-08-28
View Change
Solaris system
OS
SOLARIS_SYSTEM
SYSLOG
2025-12-10
View Change
Trend Micro Vision One Workbench
Schema
TRENDMICRO_VISION_ONE_WORKBENCH
JSON
2026-01-21
View Change
Checkpoint Audit
AUDIT
CHECKPOINT_AUDIT
SYSLOG + KV (CEF)
2024-10-01
View Change
Ruckus Networks
Wireless
RUCKUS_WIRELESS
SYSLOG + KV
2025-10-31
View Change
Agiloft
SAAS Application
AGILOFT
JSON, Syslog
2025-02-27
View Change
Keycloak
Identity and Access Management
KEYCLOAK
JSON
2026-01-23
View Change
Intel Endpoint Management Assistant
Security
INTEL_EMA
SYSLOG
2025-02-07
View Change
Dell OpenManage
Systems Management Application
DELL_OPENMANAGE
SYSLOG + KV
2025-05-14
View Change
Symantec CloudSOC CASB
CASB
SYMANTEC_CASB
SYSLOG + JSON, JSON
2024-10-25
View Change
Hackerone
IT infrastructure
HACKERONE
JSON
2025-02-25
View Change
Check Point
Firewall
CHECKPOINT_FIREWALL
SYSLOG + KV, JSON
2026-01-21
View Change
Cisco DHCP
DHCP
CISCO_DHCP
SYSLOG + CSV
2022-02-07
Ntopng
NDR
NTOPNG
SYSLOG + JSON
2024-02-01
View Change
Zscaler NSS Feeds for Alerts
Alert log types
ZSCALER_NSS_FEEDS
JSON
2024-10-21
View Change
HP Linux
OS
HP_LINUX
SYSLOG
2025-10-27
View Change
AIX system
OS
AIX_SYSTEM
SYSLOG
2026-01-04
View Change
Cisco Prime
Network Management and Optimization
CISCO_PRIME
SYSLOG
2025-04-30
View Change
Auth0
Authentication log
AUTH_ZERO
JSON
2026-01-13
View Change
AWS Key Management Service
AWS Specific
AWS_KMS
JSON
2022-05-27
View Change
Linux Auditing System (AuditD)
OS
AUDITD
SYSLOG
2026-01-22
View Change
FortiGate
FIREWALL
FORTINET_FIREWALL
SYSLOG+KV, CEF
2026-01-19
View Change
Kubernetes Node
Kubernetes Container
KUBERNETES_NODE
JSON
2026-01-16
View Change
Comodo
AV / Endpoint
COMODO_AV
SYSLOG + KV (CEF)
2021-04-09
Bindplane Agent
Log Aggregation and SIEM Systems
BINDPLANE_AGENT
JSON
2025-11-26
View Change
BMC Helix Discovery
bmc helix discovery
BMC_HELIX_DISCOVERY
SYSLOG
2022-08-29
View Change
StackHawk
Vulnerability scanners
STACKHAWK
JSON
2025-02-18
View Change
Palo Alto Prisma Access
Cloud Security
PAN_CASB
JSON, SYSLOG + CSV
2025-07-09
View Change
ManageEngine AD360
Identity and Access Management
MANAGE_ENGINE_AD360
SYSLOG + KV
2025-08-05
View Change
Cisco APIC
Software-defined Networking (SDN)
CISCO_APIC
SYSLOG
2024-11-28
View Change
HID DigitalPersona
Audit Log
HID_DIGITALPERSONA
JSON, SYSLOG + KV
2024-05-23
View Change
Azure Cosmos DB
Database
AZURE_COSMOS_DB
JSON
2025-01-16
View Change
Dell EMC PowerStore
DATA STORAGE
DELL_EMC_POWERSTORE
SYSLOG + KV
2024-11-07
View Change
Cloud Run
Google Cloud Specific
GCP_RUN
JSON
2024-01-22
View Change
VPC Flow Logs
Google Cloud Specific
GCP_VPC_FLOW
JSON
2025-07-31
View Change
Linkshadow NDR
NDR
LINKSHADOW_NDR
SYSLOG + KV
2025-01-16
View Change
GCP_NETWORK_CONNECTIVITY
Computer Inventory
GCP_NETWORK_CONNECTIVITY_CONTEXT
JSON
2023-06-13
View Change
Twingate
VPN
TWINGATE
JSON
2024-12-11
View Change
Microsoft Azure Resource
Log Aggregator
AZURE_RESOURCE_LOGS
JSON
2025-03-12
View Change
IBM Safenet
IT infrastructure
IBM_SAFENET
SYSLOG
2023-05-24
View Change
Veeam
Backup software
VEEAM
SYSLOG
2024-10-24
View Change
Broadcom Support Portal Audit Logs
Security
BROADCOM_SUPPORT_PORTAL
SYSLOG + KV
2025-01-29
View Change
CommVault
Alert System
COMMVAULT
KV , SYSLOG
2025-02-20
View Change
Azure AD Directory Audit
Audit
AZURE_AD_AUDIT
JSON
2025-12-12
View Change
Mimecast
Email Server
MIMECAST_MAIL
KV,KV+JSON
2025-07-01
View Change
ForgeRock Identity Cloud
Cloud Security
FORGEROCK_IDENTITY_CLOUD
JSON
2025-08-06
View Change
Cyolo Secure Remote Access for OT
Remote Access Tools
CYOLO_OT
SYSLOG + KV , SYSLOG + KV + JSON
2025-12-22
View Change
Digicert
IT infrastructure
DIGICERT
JSON
2025-02-13
View Change
Akamai SIEM Connector
Log Aggregation and SIEM Systems
AKAMAI_SIEM_CONNECTOR
JSON
2025-10-24
View Change
Noname API Security
Security
NONAME_API_SECURITY
JSON
2025-04-17
View Change
Jamf Protect Telemetry
Endpoint Security
JAMF_TELEMETRY
JSON
2024-05-01
View Change
OpenCanary
Data Security
OPENCANARY
SYSLOG + JSON
2024-03-11
View Change
AWS Elastic Load Balancer
AWS Specific
AWS_ELB
SYSLOG, JSON
2026-01-23
View Change
Code42 Incydr
Data loss prevention (DLP)
CODE42_INCYDR
JSON
2025-09-24
View Change
Entrust nShield HSM
Hardware Security Module
ENTRUST_HSM
SYSLOG
2024-10-15
View Change
CommVault Commcell
Alert System
COMMVAULT_COMMCELL
KV , SYSLOG
2024-01-24
View Change
VMWare VSphere
virtualization
VMWARE_VSPHERE
SYSLOG + CSV
2025-05-15
View Change
Security Command Center Sensitive Data Risk
Google Cloud Specific
GCP_SECURITYCENTER_SENSITIVE_DATA_RISK
JSON
2025-11-14
Pure Storage
Data Storage
PURE_STORAGE
SYSLOG + KV
2024-10-01
View Change
FileZilla
File tranfser
FILEZILLA_FTP
SYSLOG
2024-06-09
View Change
Pharos
NA
PHAROS
JSON
2025-02-18
Opswat Metadefender
Threat Protection
OPSWAT_METADEFENDER
SYSLOG + KV (CEF)
2025-10-07
View Change
Windows Defender ATP
AV / Endpoint
WINDOWS_DEFENDER_ATP
SYSLOG + JSON, XML, JSON
2024-10-15
View Change
AWS CloudWatch
Cloud service monitoring
AWS_CLOUDWATCH
JSON, GROK
2025-12-24
View Change
Mongo Database
DATABASE
MONGO_DB
JSON
2025-03-12
View Change
Snoopy Logger
Log Aggregator
SNOOPY_LOGGER
SYSLOG
2022-08-10
View Change
Darktrace
NDR
DARKTRACE
SYSLOG + KV (CEF), SYSLOG + JSON
2025-12-02
View Change
SonicWall
Firewall
SONIC_FIREWALL
SYSLOG + KV
2025-11-07
View Change
ManageEngine ADAudit Plus
Active Directory Audit
ADAUDIT_PLUS
SYSLOG + KV (CEF)
2025-04-10
View Change
Kubernetes Auth Proxy
Kubernetes Specific
KUBERNETES_AUTH_PROXY
JSON
2022-09-08
View Change
Apple macOS
AV / Endpoint
MACOS
SYSLOG, JSON
2025-12-18
View Change
Shibboleth IDP
Identity and Access Management
SHIBBOLETH_IDP
SYSLOG, JSON
2024-11-14
View Change
Sophos Central
AV / Endpoint
SOPHOS_CENTRAL
JSON
2026-01-22
View Change
Duo Auth
Authentication
DUO_AUTH
JSON
2026-01-06
View Change
Workday Audit Logs
Audit And Compliance
WORKDAY_AUDIT
CSV
2025-12-17
View Change
Citrix Analytics
Monitoring of DaaS
CITRIX_ANALYTICS
JSON
2024-06-03
View Change
Peplink Firewall
Firewall
PEPLINK_FW
SYSLOG + KV
2023-08-17
View Change
Digital Shadows SearchLight
Threat Intelligence
DIGITAL_SHADOWS_SEARCHLIGHT
JSON
2022-05-02
KerioControl Firewall
Threat Management Firewall
KERIOCONTROL
SYSLOG
2024-02-28
View Change
Cloud Data Loss Prevention
Google Cloud Specific
N/A
JSON
2025-01-29
View Change
ISC DHCP
DHCP
ISC_DHCP
JSON + SYSLOG + KV
2024-11-27
View Change
Harness IO
Automation and DevOps Tools
HARNESS_IO
JSON
2025-04-16
View Change
Ubiquiti UniFi Switch
Switch
UBIQUITI_SWITCH
SYSLOG
2025-08-06
View Change
BeyondTrust Privileged Identity
Privilege Account Activity
BEYONDTRUST_PI
SYSLOG
2024-08-19
View Change
Saiwall VPN
VPN
SAIWALL_VPN
KV
2024-08-27
View Change
Rapid7 Insight
Vulnerability Scanner
RAPID7_INSIGHT
SYSLOG, JSON
2024-05-13
View Change
Apache
Security
APACHE
SYSLOG + JSON, SYSLOG, JSON
2026-01-12
View Change
Cisco WSA
WSA
CISCO_WSA
SYSLOG, SYSLOG+CSV
2025-11-23
View Change
Layer7 SiteMinder
SSO
SITEMINDER_SSO
KV+JSON, SYSLOG, JSON
2025-02-12
View Change
LogonBox
Authentication
LOGONBOX
SYSLOG + KV
2024-02-05
View Change
Netscout
NETWORK
ARBOR_EDGE_DEFENSE
SYSLOG + KV
2025-10-16
View Change
Trustwave webmarshal
Proxy Server
WEBMARSHAL
SYSLOG + CSV
2023-05-04
View Change
Forcepoint Proxy
Web Proxy
FORCEPOINT_WEBPROXY
SYSLOG + KV (CEF), LEEF, CSV
2025-10-14
View Change
Digi modems
Switches and Routers
DIGI_MODEMS
SYSLOG
2023-06-26
View Change
AWS GuardDuty
IDS/IPS
GUARDDUTY
JSON
2026-01-12
View Change
Velo Firewall
FIREWALL
VELO_FIREWALL
SYSLOG + KV
2024-10-10
View Change
Department of Homeland Security
Threat detection
DHS_IOC
XML
2023-07-31
View Change
Snyk Group level audit/issues logs
Security
SNYK_ISSUES
JSON
2025-12-22
View Change
Cisco CTS
Telephone Software
CISCO_CTS
SYSLOG + KV
2021-05-20
CipherTrust Manager
CIPHERTRUST_MANAGER
SYSLOG + CEF + JSON
2025-11-20
View Change
Fastly WAF
WAF
FASTLY_WAF
JSON
2025-05-08
View Change
Cisco FireSIGHT Management Center
SaaS Application
CISCO_FIRESIGHT
KV
2025-02-21
View Change
Medigate IoT
IoT
MEDIGATE_IOT
SYSLOG + JSON
2025-08-08
View Change
BeyondTrust Endpoint Privilege Management
Privileged Account Activity
BEYONDTRUST_ENDPOINT
JSON
2026-01-22
View Change
Qumulo FS
File System
QUMULO_FS
SYSLOG
2024-05-09
View Change
Semperis DSP
LDAP
SEMPERIS_DSP
SYSLOG
2025-09-12
View Change
Avaya Aura Experience Portal
Avaya Aura Experience Portal
AVAYA_AURA
SYSLOG
2022-12-30
View Change
Suricata EVE
IPS IDS
SURICATA_EVE
JSON
2025-12-03
View Change
Infoblox RPZ
RPZ
INFOBLOX_RPZ
SYSLOG
2024-02-13
View Change
Jenkins
Automation and DevOps
JENKINS
JSON, SYSLOG
2024-11-19
View Change
Forcepoint DLP
Forcepoint DLP
FORCEPOINT_DLP
CEF
2025-11-05
View Change
Cisco Stealthwatch
Log Aggregator
CISCO_STEALTHWATCH
JSON, CEF
2026-01-12
View Change
Cloudflare
SaaS Application
CLOUDFLARE
JSON
2026-01-23
View Change
VMware Horizon
VDI
VMWARE_HORIZON
SYSLOG
2025-07-17
View Change
NXLog Manager
Log Aggregator
NXLOG_MANAGER
SYSLOG
2022-01-13
Cisco Umbrella DNS
DNS
UMBRELLA_DNS
CSV, JSON
2025-12-17
View Change
Proofpoint Tap Alerts
Email Server
PROOFPOINT_MAIL
SYSLOG+KV, JSON, SYSLOG+JSON
2025-11-20
View Change
Trend Micro Vision One
AV and endpoint logs
TRENDMICRO_VISION_ONE
SYSLOG + KV, CEF, JSON
2026-01-08
View Change
Claroty Continuous Threat Detection
IoT
CLAROTY_CTD
KV, SYSLOG
2026-01-20
View Change
Metabase
Data Security
METABASE
JSON
2025-02-05
View Change
Nucleus Asset Metadata
Nucleus Specific
NUCLEUS_ASSET
JSON
2021-08-05
Sentry
Data Security
SENTRY
JSON
2025-01-16
View Change
Thales MFA
Authentication
THALES_MFA
SYSLOG + KV (CEF)
2025-11-07
View Change
SiteMinder Web Access Management
SSO
CA_SSO_WEB
JSON, SYSLOG
2024-06-25
View Change
Akeyless Vault Platform
Akeyless Vault Platform
AKEYLESS_VAULT
KV + JSON
2023-09-16
View Change
Men and Mice DNS
DNS
MENANDMICE_DNS
SYSLOG
2021-11-12
Extreme Wireless
Network Management and Optimization software
EXTREME_WIRELESS
SYSLOG
2025-11-20
View Change
Remediant SecureONE
Privileged Account Activity
REMEDIANT_SECUREONE
SYSLOG + JSON
2025-07-09
View Change
CA LDAP
Web server
CA_LDAP
JSON
2022-08-19
View Change
Netwrix StealthAudit
N/A
NETWRIX_STEALTHAUDIT
SYSLOG + KV
2025-01-20
View Change
Jamf Protect Threat Events
Threat Events Stream
JAMF_THREAT_EVENTS
JSON
2023-03-27
View Change
Tanium Audit
SCAN NETWORK
TANIUM_AUDIT
JSON
2025-11-13
View Change
Fidelis Network
NDR
FIDELIS_NETWORK
SYSLOG + KV, JSON
2025-08-07
View Change
Duo Administrator Logs
Authentication
DUO_ADMIN
JSON
2025-01-02
View Change
Open LDAP
LDAP
OPENLDAP
SYSLOG
2025-11-12
View Change
FortiMail Email Security
Email Security
FORTINET_FORTIMAIL
KV
2025-02-25
View Change
PAN Autofocus
IOC
PAN_IOC
JSON
2021-08-09
Squid Web Proxy
Web Proxy
SQUID_WEBPROXY
SYSLOG
2025-10-28
View Change
Workspace Groups
Google Cloud Specific
WORKSPACE_GROUPS
JSON
2023-11-29
View Change
ZeroFox Platform
Database
ZEROFOX_PLATFORM
JSON
2025-03-21
View Change
Palo Alto Networks Firewall
Firewall
PAN_FIREWALL
CSV + CEF + LEEF + JSON
2025-12-30
View Change
Stealthbits Defend
Security System for Active Directory and File Systems.
STEALTHBITS_DEFEND
SYSLOG + KV (LEEF, CEF)
2022-11-17
View Change
Azure VPN
VPN
AZURE_VPN
JSON
2024-10-11
View Change
RH-ISAC
IOC
RH_ISAC_IOC
JSON
2024-03-07
View Change
Microsoft IAS Server
Endpoint Security
MICROSOFT_IAS
CSV + KV
2024-04-25
One Identity TPAM
Privileged Account Activity
ONEIDENTITY_TPAM
KV ,CEF
2025-12-23
View Change
Microsoft IIS
Web Server
IIS
SYSLOG + KV, JSON , XML
2026-01-22
View Change
Stealthbits Audit
File system monitoring
STEALTHBITS_AUDIT
JSON
2021-11-09
ForgeRock OpenAM
Identity and Access Management
OPENAM
CSV, SYSLOG + KV
2024-11-28
View Change
Cisco Umbrella SWG DLP
DLP
CISCO_UMBRELLA_SWG_DLP
CSV
2025-10-07
View Change
Lenel Onguard Badge Management
Access Control System
LENEL_ONGUARD
JSON
2024-11-14
View Change
Netscout OCI
Alert log
NETSCOUT_OCI
SYSLOG + KV
2024-02-21
View Change
Kubernetes Audit Azure
Log Aggregator
KUBERNETES_AUDIT_AZURE
JSON
2024-12-11
View Change
Armis Devices
DEVICES
ARMIS_DEVICES
JSON
2023-03-02
View Change
McAfee Enterprise Security Manager
Log Aggregator
MCAFEE_ESM
SYSLOG + JSON
2024-03-21
Vectra Alerts
Content Management Software
VECTRA_ALERTS
JSON
2025-02-18
View Change
Snyk Group level audit Logs
Vulnerability Scanners
SNYK_SDLC
JSON
2025-03-04
View Change
Red Canary
EDR
REDCANARY_EDR
JSON
2022-09-15
View Change
CyberArk
Privilege Account Management
CYBERARK
KV (CEF)
2025-12-30
View Change
Rubrik
Backup software
RUBRIK
SYSLOG
2025-01-22
View Change
TeamViewer
Remote Support
TEAMVIEWER
JSON
2025-12-01
View Change
Cloud Identity Devices
Google Cloud Specific
GCP_CLOUDIDENTITY_DEVICES
JSON
2024-07-01
View Change
Bitwarden Events
Password Manager
BITWARDEN_EVENTS
JSON
2023-11-09
View Change
Chrome Management
Browser
N/A
JSON
2025-11-11
View Change
Qualys Virtual Scanner
Vulnerability Scanner
QUALYS_VIRTUAL_SCANNER
JSON
2023-08-21
View Change
LimaCharlie
EDR
LIMACHARLIE_EDR
JSON
2023-08-07
Cloud SQL
Google Cloud Specific
GCP_CLOUDSQL
JSON
2025-12-05
View Change
Azure VNET Flow
Netflow log type
AZURE_VNET_FLOW
JSON
2025-07-18
View Change
BeyondTrust Secure Remote Access
Remote Access Tools
BEYONDTRUST_REMOTE_ACCESS
SYSLOG + KV
2025-12-04
View Change
AWS WAF
AWS Specific
AWS_WAF
JSON
2026-01-10
View Change
Windows Defender AV
AV / Endpoint
WINDOWS_DEFENDER_AV
JSON, XML
2025-02-27
View Change
ESET
EDR
ESET_EDR
SYSLOG + JSON
2024-04-08
View Change
Azure Application Gateway
GATEWAY
AZURE_GATEWAY
JSON
2025-06-05
View Change
Citrix Storefront
Remote Access Tools
CITRIX_STOREFRONT
JSON
2025-02-12
View Change
Okta User Context
Identity and Access Management
OKTA_USER_CONTEXT
JSON
2025-02-07
View Change
Custom Application Access Logs
Security
CUSTOM_APPLICATION_ACCESS
JSON
2025-02-07
View Change
Google Cloud Identity Context
Identity and Access Management
CLOUD_IDENTITY_CONTEXT
JSON
2024-12-06
View Change
Fortinet FortiNAC
NAC
FORTINET_FORTINAC
SYSLOG,CSV
2025-05-15
View Change
Forescout NAC
NAC
FORESCOUT_NAC
SYSLOG, CEF
2025-10-13
View Change
TrendMicro Deep Discovery Inspector
Physical and virtual network
TRENDMICRO_DDI
SYSLOG
2026-01-21
View Change
Datto File Protection
DATTO_FILE_PROTECTION
DATTO_FILE_PROTECTION
SYSLOG
2022-08-22
View Change
Microsoft Intune Context
Mobile Device Management
AZURE_MDM_INTUNE_CONTEXT
Json
2024-09-19
View Change
Corelight
NDR
CORELIGHT
JSON
2025-11-25
View Change
Windows Hyper-V
Virtualization Software
WINDOWS_HYPERV
JSON
2025-06-17
View Change
Team Cymru Scout Threat Intelligence
Threat Intel
TEAM_CYMRU_SCOUT_THREATINTEL
JSON
2024-08-22
View Change
Microsoft Azure Activity
Misc Windows Specific
AZURE_ACTIVITY
JSON
2025-07-16
View Change
Netapp Storagegrid
Security
NETAPP_STORAGEGRID
SYSLOG + KV
2024-06-15
View Change
Netscope Client
CASB
NETSKOPE_CLIENT
JSON
2024-10-16
View Change
UpGuard
Vulnerability scanners
UPGUARD
JSON
2024-11-13
View Change
ServiceNow CMDB
Policy Management
SERVICENOW_CMDB
JSON
2025-03-27
View Change
Vectra XDR
NDR
VECTRA_XDR
JSON
2025-12-30
View Change
Asset Panda
SaaS Applications
ASSET_PANDA
JSON
2025-02-04
View Change
Microsoft ATA
IDS/IPS
MICROSOFT_ATA
SYSLOG + KV
2024-01-29
View Change
Firewall Rule Logging
Google Cloud Specific
N/A
JSON
2024-05-01
View Change
Barracuda Firewall
Firewall
BARRACUDA_FIREWALL
SYSLOG
2025-11-13
View Change
Elastic Packet Beats
Log Aggregator
ELASTIC_PACKETBEATS
SYSLOG + JSON , JSON
2025-02-13
View Change
ProofPoint Secure Email Relay
Email server
PROOFPOINT_SER
JSON
2025-01-02
View Change
Forcepoint  NGFW
Network
FORCEPOINT_FIREWALL
JSON
2025-11-12
View Change
Sangfor Proxy
Application server logs
SANGFOR_PROXY
SYSLOG
2025-02-18
View Change
Quest Active Directory
Authentication log
QUEST_AD
CEF SYSLOG + JSON
2025-08-13
View Change
FireEye ETP
Email Server
FIREEYE_ETP
JSON + SYSLOG
2025-11-28
View Change
Cisco Web Services Manager
CISCO_WSM
CISCO_WSM
SYSLOG
2023-10-05
View Change
wiz.io
Identity and Access Management
WIZ_IO
JSON
2026-01-12
View Change
Trend Micro Vision One Detections
Schema
TRENDMICRO_VISION_ONE_DETECTIONS
JSON
2025-11-04
View Change
Infoblox DNS
DNS
INFOBLOX_DNS
SYSLOG, CEF
2025-10-17
View Change
Seqrite Endpoint Security (EPS)
AV and endpoint logs
SEQRITE_ENDPOINT
LEEF
2023-03-24
View Change
Palo Alto Cortex XDR Events
Monitoring and Threat Detection
PAN_CORTEX_XDR_EVENTS
JSON
2025-09-24
View Change
Quest File Access Audit
Alert
QUEST_FILE_AUDIT
JSON
2024-01-13
View Change
Proofpoint On Demand
Email Server
PROOFPOINT_ON_DEMAND
JSON
2026-01-06
View Change
Google Threat Intelligence
Threat Intel
GCP_THREATINTEL
JSON
2025-11-25
View Change
Google Cloud DNS Threat Detector
DNS Security
GCP_DNS_ATD
JSON
2025-07-25
View Change
BeyondTrust
Privilege Account Activity
BOMGAR
SYSLOG
2025-12-17
View Change
Vsftpd
FTP Server
VSFTPD
GROK
2023-11-20
View Change
Cohesity
Backup Software
COHESITY
SYSLOG
2024-09-24
View Change
Citrix Netscaler
Load Balancer, Traffic Shaper, ADC
CITRIX_NETSCALER
SYSLOG + KV
2025-11-21
View Change
AWS EC2 Instances
AWS Specific
AWS_EC2_INSTANCES
JSON
2024-01-31
View Change
Aware Signals
SaaS Applications
AWARE_SIGNALS
JSON
2025-02-07
View Change
DMP
Physical Security
DMP_ENTRE
SYSLOG
2020-09-23
Thinkst Canary
Deception Software
THINKST_CANARY
JSON
2025-11-21
View Change
Imperva Audit Trail
IT infrastructure
IMPERVA_AUDIT_TRAIL
JSON, SYSLOG
2025-04-03
View Change
Linux Sysmon
DNS
LINUX_SYSMON
XML
2025-09-25
View Change
SEPPmail Secure Email
email encryption and signature solutions
SEPPMAIL
SYSLOG + KV
2024-06-04
View Change
AWS EMR
AWS Specific
AWS_EMR
SYSLOG, SYSLOG+JSON, JSON
2024-09-05
View Change
Microsoft Sentinel
Microsoft Sentinel
MICROSOFT_SENTINEL
JSON
2025-10-16
View Change
Vercel WAF
Firewall log
VERCEL_WAF
JSON
2024-12-20
Cisco TACACS+
Authentication
CISCO_TACACS
SYSLOG + KV
2024-11-07
View Change
Upstream Vehicle SOC Alerts
Schema
UPSTREAM_VSOC_ALERTS
JSON
2025-09-02
View Change
VMware NSX
Network and Security Virtualization
VMWARE_NSX
KV
2026-01-01
View Change
Microsoft CASB
CASB
MICROSOFT_CASB
SYSLOG + KV (CEF)
2025-03-26
View Change
Watchguard EDR
EDR
WATCHGUARD_EDR
JSON
2025-01-30
View Change
HAProxy
Load balancing
HAPROXY
SYSLOG
2025-07-30
View Change
Radware Alteon
Load Balancer
RADWARE_ALTEON
SYSLOG
2024-06-21
View Change
Armis Alerts
ALERTS
ARMIS_ALERTS
JSON
2023-02-07
View Change
Tetragon Ebpf Audit Logs
OS
TETRAGON_EBPF_AUDIT_LOGS
JSON
2024-03-15
View Change
Tanium Question
TANIUM Logs
TANIUM_QUESTION
JSON
2025-05-21
View Change
Recordia
Telephone software
RECORDIA
JSON
2024-01-30
View Change
Nucleus Unified Vulnerability Management
Nucleus Specific
NUCLEUS_VULNERABILITY
JSON
2021-06-30
Nokia Router
Switches and Routers
NOKIA_ROUTER
SYSLOG + KV
2025-05-15
View Change
COVID-19 Cyber Threat Coalition
IOC
COVID_CTC_IOC
Value Entry
2020-06-02
Workday
SaaS Application
WORKDAY
JSON, CSV
2025-06-05
View Change
Tanium Threat Response
Tanium Specific
TANIUM_THREAT_RESPONSE
JSON
2025-10-08
View Change
Amazon API Gateway
AWS-specific log types
AWS_API_GATEWAY
JSON
2026-01-22
View Change
Sierra Wireless
IOT Devices
SIERRA_WIRELESS
SYSLOG
2023-11-23
View Change
AWS Control Tower
Identity and Access Management
AWS_CONTROL_TOWER
JSON
2024-03-17
View Change
Azion
Firewall
AZION
JSON
2023-09-30
View Change
Okera Dynamic Access Platform
Data Security
OKERA_DAP
JSON
2023-01-29
View Change
Zscaler DLP
Data Loss Prevention
ZSCALER_DLP
JSON
2026-01-07
View Change
Recorded Future
IOC
RECORDED_FUTURE_IOC
JSON
2026-01-19
View Change
Aruba Airwave
Wireless
ARUBA_AIRWAVE
XML
2025-12-11
View Change
Tanium Reveal
Tanium Specific
TANIUM_REVEAL
JSON
2021-11-15
Compute Engine
Google Cloud Specific
GCP_COMPUTE
JSON
2026-01-16
View Change
Fortinet
DHCP
FORTINET_DHCP
KV
2022-11-21
View Change
Big Switch BigCloudFabric
Switches, Routers
BIGSWITCH_BCF
SYSLOG
2021-04-20
VanDyke SFTP
Data Transfer
VANDYKE_SFTP
JSON, SYSLOG
2025-05-15
View Change
Microsoft Defender for Identity
EDR
MICROSOFT_DEFENDER_IDENTITY
JSON
2025-07-29
View Change
BIND
DNS
BIND_DNS
SYSLOG
2026-01-11
View Change
F5 Advanced Firewall Management
Firewall
F5_AFM
SYSLOG + CSV, SYSLOG + KV
2026-01-13
View Change
Centripetal Networks IOC
IOC
CENTRIPETAL_IOC
SYSLOG + KV
2022-01-06
Digital Shadows Indicators
IOC
DIGITAL_SHADOWS_IOC
JSON
2022-04-23
IBM MaaS360
Security
IBM_MAAS360
JSON
2024-11-06
View Change
Malwarebytes
EDR
MALWAREBYTES_EDR
JSON
2024-08-14
View Change
CloudGenix SD-WAN
Switches, Routers
CLOUDGENIX_SDWAN
SYSLOG + KV
2022-09-08
View Change
Net Suite
WAF
NET_SUITE
kv
2023-08-02
View Change
Palo Alto Networks IoT Security
IoT
PAN_IOT
SYSLOG
2025-01-09
View Change
Proofpoint Web Browser Isolation
ATTACK PROTECTION ISOLATION
PROOFPOINT_WEB_BROWSER_ISOLATION
JSON
2023-05-25
View Change
Zeek TSV
Format Specific
BRO_TSV
SYSLOG + TSV
2024-05-17
View Change
Imperva FlexProtect
Cloud App & Network Security
IMPERVA_FLEXPROTECT
CEF + KV
2023-08-28
View Change
AWS RDS
Database
AWS_RDS
SYSLOG,JSON
2025-12-30
View Change
Teleport Access Plane
Remote Access
TELEPORT_ACCESS_PLANE
SYSLOG, JSON
2025-09-04
View Change
Microsoft PowerShell
Misc. Windows-specific
POWERSHELL
SYSLOG + JSON, XML
2025-12-03
View Change
Blue Coat Proxy
Web Proxy
BLUECOAT_WEBPROXY
SYSLOG + JSON, SYSLOG + KV, KV
2025-12-06
View Change
Symantec Event export
SEP
SYMANTEC_EVENT_EXPORT
JSON, SYSLOG
2025-03-06
View Change
F5 BIGIP LTM
Load Balancer, Traffic Shaper, ADC
F5_BIGIP_LTM
SYSLOG, KV
2026-01-23
View Change
HYPR MFA
Security SSO
HYPR_MFA
CSV
2024-04-26
View Change
Microsoft Defender For Cloud
Automation and DevOps Tools
MICROSOFT_DEFENDER_CLOUD_ALERTS
JSON
2025-12-24
View Change
Forcepoint Email Security
Email Server
FORCEPOINT_EMAILSECURITY
JSON
2025-12-23
View Change
Compute Context
Google Cloud Specific
N/A
JSON
2024-01-27
View Change
ManageEngine Reporter Plus
SaaS Application
MANAGE_ENGINE_REPORTER_PLUS
JSON
2022-08-29
View Change
Azure DevOps Audit
Automation and DevOps Tools
AZURE_DEVOPS
JSON
2025-03-10
View Change
Mobileiron
ENDPOINT MANAGEMENT
MOBILEIRON
JSON , SYSLOG
2025-12-05
View Change
Wazuh
Log Aggregator
WAZUH
SYSLOG + JSON
2025-03-21
View Change
Elastic Windows Event Log Beats
Log Aggregator
ELASTIC_WINLOGBEAT
SYSLOG + JSON
2025-04-29
View Change
ManageEngine Log360
Alert Log
MANAGE_ENGINE_LOG360
SYSLOG+KV
2024-10-28
View Change
Tenable Security Center
Vulnerability Scanner
TENABLE_SC
SYSLOG, JSON+SYSLOG
2025-08-11
View Change
ThreatLocker Platform
THREATLOCKER
THREATLOCKER
JSON
2023-06-18
View Change
Pivotal
PaaS Application
PIVOTAL
SYSLOG + KV
2022-08-17
View Change
Azure API Management
Schema
AZURE_API_MANAGEMENT
JSON
2025-01-21
View Change
TrendMicro Apex Central
Endpoint
TRENDMICRO_APEX_CENTRAL
CEF
2025-01-23
View Change
Absolute Mobile Device Management
Mobile Device Management
ABSOLUTE
SYSLOG + KV (CEF)
2024-12-03
View Change
F5 Shape
Security log
F5_SHAPE
JSON
2024-08-20
View Change
Zscaler Secure Private Access Audit Logs
AUDIT
ZSCALER_ZPA_AUDIT
JSON
2026-01-07
View Change
Unifi AP
Switches and Routers
UNIFI_AP
SYSLOG + KV, SYSLOG + JSON
2025-11-24
View Change
CIS Albert Alerts
Alerts
CIS_ALBERT_ALERT
SYSLOG, JSON
2025-05-19
View Change
Symantec Web Isolation
Secure Access Service Edge
SYMANTEC_WEB_ISOLATION
JSON
2022-07-08
View Change
Azure Front Door
Web server logs
AZURE_FRONT_DOOR
2026-01-07
View Change
Cloudflare WAF
Cloud Log
CLOUDFLARE_WAF
JSON
2025-10-03
View Change
SpyCloud
AV / Endpoint
SPYCLOUD
SYSLOG + JSON , JSON
2025-02-27
View Change
Barracuda Web Filter
Webfilter
BARRACUDA_WEBFILTER
SYSLOG
2024-11-14
View Change
Microsoft SQL Server
Database
MICROSOFT_SQL
SYSLOG + KV, JSON, SYSLOG + JSON, CSV, XML
2026-01-15
View Change
JumpCloud Directory Insights
CLOUD
JUMPCLOUD_DIRECTORY_INSIGHTS
JSON
2026-01-27
View Change
Vmware Avinetworks iWAF
Server
VMWARE_AVINETWORKS_IWAF
SYSLOG
2025-11-10
View Change
Trend Micro Deep Security
AV / Endpoint
TRENDMICRO_DEEP_SECURITY
LEEF + CEF
2025-04-16
View Change
Windows Applocker
Application Locker
WINDOWS_APPLOCKER
SYSLOG + KV + JSON + XML
2023-10-17
View Change
IBM Security Identity Manager
Security
IBM_SIM
JSON + KV
2024-03-11
View Change
Fortinet Proxy
Storage
FORTINET_WEBPROXY
SYSLOG + KV
2025-06-24
View Change
Sophos Capsule8
Container Security
SOPHOS_CAPSULE8
JSON
2021-12-22
Cisco ASA
firewall
CISCO_ASA_FIREWALL
SYSLOG
2025-12-16
View Change
Cyberark Privilege Cloud
Identity & Access Management
CYBERARK_PRIVILEGE_CLOUD
SYSLOG + KV
2025-09-30
View Change
FireEye HX
EDR
FIREEYE_HX
JSON
2025-05-14
View Change
Cloud Identity Device Users
Google Cloud Specific
GCP_CLOUDIDENTITY_DEVICEUSERS
JSON
2022-10-01
View Change
AWS VPC Flow (CSV)
AWS Specific
AWS_VPC_FLOW_CSV
CSV
2025-05-26
View Change
AlgoSec Security Management
Policy Management
ALGOSEC
SYSLOG + KV (CEF)
2025-12-05
View Change
Windows DNS
DNS
WINDOWS_DNS
JSON, XML, SYSLOG + KV
2026-01-13
View Change
Carbon Black App Control
Security log
CB_APP_CONTROL
CEF, JSON
2025-08-28
View Change
AWS Security Hub
IDS/IPS
AWS_SECURITY_HUB
JSON
2026-01-15
View Change
Dataminr Alerts
SAAS Security Application
DATAMINR_ALERT
JSON
2024-02-14
View Change
Aruba Switch
Network Infrastructure
ARUBA_SWITCH
SYSLOG
2026-01-16
View Change
NetIQ Access Manager
Security
NETIQ_ACCESS_MANAGER
SYSLOG + KV
2026-01-22
View Change
Kaspersky AV
AV / Endpoint
KASPERSKY_AV
KV + CEF
2025-10-24
View Change
Delinea PAM
Access Management
DELINEA_PAM
SYSLOG + CSV
2022-11-10
View Change
QNAP Systems NAS
Storage solutions
QNAP_NAS
SYSLOG, KV
2025-12-11
View Change
Advanced Intrusion Detection Environment
Alert
AIDE
SYSLOG
2025-03-10
View Change
Netskope
Cloud Security
NETSKOPE_ALERT
JSON
2024-08-14
View Change
Office 365 Message Trace
OFFICE_365 Specific
OFFICE_365_MESSAGETRACE
JSON
2025-08-21
View Change
Portnox CEF
Privileged Account Activity
PORTNOX_CEF
CEF Syslog
2024-05-31
View Change
ServiceNow Security
SaaS Application
SERVICENOW_SECURITY
JSON
2021-05-24
Strong Swan VPN
VPN
STRONGSWAN_VPN
JSON
2023-05-25
View Change
Qualys VM
Vulnerability Scanner
QUALYS_VM
KV + JSON
2025-07-03
View Change
Brocade ServerIron ADX
Load Balancer
BROCADE_SERVERIRON
SYSLOG
2022-01-13
Tenable CSPM
Cloud Security
TENABLE_CSPM
JSON
2025-02-17
View Change
PerimeterX Bot Protection
Security
PERIMETERX_BOT_PROTECTION
JSON
2024-03-27
View Change
Sublime Security
Vulnerability scanners
SUBLIMESECURITY
JSON
2025-12-22
View Change
pfSense
FIREWALL
PFSENSE
SYSLOG
2025-07-18
View Change
Accellion
DLP
ACCELLION
SYSLOG
2022-09-30
View Change
Ordr IoT
IoT
ORDR_IOT
SYSLOG + JSON
2024-03-05
View Change
Symantec Endpoint Protection
AV / Endpoint
SEP
SYSLOG, KV, JSON, SYSLOG + JSON
2025-11-27
View Change
ThreatX WAF
WAF
THREATX_WAF
SYSLOG, JSON
2025-01-28
View Change
Smartsheet
CASB
SMARTSHEET
JSON
2024-12-16
View Change
Cisco vManage SD-WAN
Switches and Routers
CISCO_SDWAN
JSON, SYSLOG
2025-11-18
View Change
Cisco UCM
Communication Manager
CISCO_UCM
SYSLOG + KV
2025-10-08
View Change
Oracle Cloud Infrastructure VCN Flow Logs
Oracle Cloud Infrastructure
OCI_FLOW
JSON
2025-08-05
View Change
SailPoint IdentityIQ
Identity and Access Management
SAILPOINT_IIQ
SYSLOG
2024-10-01
View Change
Kaspersky Endpoint
Security
KASPERSKY_ENDPOINT
SYSLOG
2025-09-18
View Change
Ipswitch MOVEit Transfer
Switches
IPSWITCH_MOVEIT_TRANSFER
SYSLOG + CSV
2025-11-04
View Change
STIX Threat Intelligence
Cybersecurity Threats
STIX
SYSLOG + KV (CEF), JSON
2025-11-24
View Change
Azure AD Organizational Context
LDAP
AZURE_AD_CONTEXT
JSON
2025-10-03
View Change
Appian Cloud
Collaboration log types
APPIAN_CLOUD
SYSLOG
2025-05-06
View Change
AlphaSOC
Alert
ASOC_ALERT
JSON
2021-06-21
Sophos Intercept EDR
EDR logs
SOPHOS_EDR
JSON
2024-07-31
View Change
Ansible AWX
Automation and DevOps Tools
ANSIBLE_AWX
JSON
2024-06-25
View Change
IBM WebSEAL
Web server
IBM_WEBSEAL
JSON, SYSLOG
2025-10-08
View Change
tenable.io
Vulnerability Scanner
TENABLE_IO
JSON
2026-01-19
View Change
Opnsense
Firewall and Routing Platform
OPNSENSE
Syslog, Syslog + CSV
2025-09-17
View Change
YAMAHA ROUTER RTX1200
Switches AND Routers
YAMAHA_ROUTER
SYSLOG
2024-04-19
View Change
BigQuery
Google Cloud Resources Contexts
N/A
JSON
2024-04-24
View Change
HPE Aruba Networking Central
Data Security
ARUBA_CENTRAL
SYSLOG , JSON
2025-03-24
View Change
H3C Comware Platform Switch
Switches, Routers
H3C_SWITCH
SYSLOG
2026-01-23
View Change
Microsoft Dynamics 365 User Activity
Authentication logs
MICROSOFT_DYNAMICS_365
CSV
2024-12-16
View Change
Trustwave SEC MailMarshal
Email server
MAILMARSHAL
SYSLOG
2023-04-06
View Change
Oracle Cloud Infrastructure Audit Logs
Oracle Cloud Infrastructure
OCI_AUDIT
JSON
2025-10-28
View Change
Tableau
Web server
TABLEAU
JSON, KV, SYSLOG
2026-01-09
View Change
Thales Digital Identity and Security
Digital Identity & Security
THALES_DIS
SYSLOG
2022-03-17
Microsoft Azure NSG Flow
Network Flow
AZURE_NSG_FLOW
JSON
2025-05-20
View Change
FireEye NX
NDR
FIREEYE_NX
JSON, SYSLOG+KV
2026-01-01
View Change
Voltage
Email Server
VOLTAGE
SYSLOG
2025-06-11
View Change
F5 DNS
DNS
F5_DNS
SYSLOG
2025-07-09
View Change
Silverfort Authentication Platform
Identity and Access Management
SILVERFORT
CEF SYSLOG
2025-08-01
View Change
Juniper Mist
Network Management and Optimization software
JUNIPER_MIST
JSON
2025-03-13
View Change
Symantec Messaging Gateway
Email server log types.
SYMANTEC_MAIL
JSON
2025-12-22
View Change
Ping Identity
Authentication
PING
JSON, SYSLOG + KV
2025-12-01
View Change
Custom DNS
DNS
CUSTOM_DNS
JSON
2022-08-05
View Change
Dummy LogType
DNS
DUMMY_LOGTYPE
CSV
2024-07-24
View Change
Azure Key Vault logging
Audit
AZURE_KEYVAULT_AUDIT
JSON
2025-07-08
View Change
Nutanix Prism
Firewall
NUTANIX_PRISM
JSON, SYSLOG
2025-12-30
View Change
McAfee Skyhigh CASB
CASB
MCAFEE_SKYHIGH_CASB
SYSLOG + KV
2023-06-17
View Change
ReviveSec
Application server logs
REVIVESEC
SYSLOG
2025-02-25
View Change
Delinea Distributed Engine
Application server logs
DELINEA_DISTRIBUTED_ENGINE
SYSLOG
2024-12-06
View Change
Mobile Endpoint Security
Mobile Endpoint Security
LOOKOUT_MOBILE_ENDPOINT_SECURITY
CEF
2024-11-20
View Change
Cloud IoT
Google Cloud Specific
GCP_CLOUDIOT
JSON
2022-06-06
View Change
Tanium Insight
Tanium Specific
TANIUM_INSIGHT
SYSLOG + KV
2021-03-10
ESET Threat Intelligence
IOC
ESET_IOC
JSON
2023-10-05
View Change
Illumio Core
Policy Management
ILLUMIO_CORE
JSON, SYSLOG, SYSLOG+JSON, SYSLOG+CEF and SYSLOG+KV+JSON.
2025-12-29
View Change
BMC Client Management
Security
BMC_CLIENT_MANAGEMENT
SYSLOG
2024-10-11
View Change
Aruba IPS
IPS
ARUBA_IPS
JSON
2022-06-16
View Change
Orca Cloud Security Platform
IDS/IPS log types
ORCA
JSON
2025-10-17
View Change
Cisco WLC/WCS
Wireless
CISCO_WIRELESS
SYSLOG
2026-01-23
View Change
Radware Web Application Firewall
Firewall
RADWARE_FIREWALL
SYSLOG, JSON
2025-11-26
View Change
iBoss Proxy
Webproxy
IBOSS_WEBPROXY
SYSLOG + JSON
2023-08-22
View Change
OpenVPN
Network
OPEN_VPN
SYSLOG + KV + JSON
2024-11-27
View Change
HCNET Account Adapter Plus
DHCP
HCNET_ACCOUNT_ADAPTER
SYSLOG
2024-11-04
View Change
Symantec Web Security Service
Web Proxy
SYMANTEC_WSS
JSON
2025-07-11
View Change
Barracuda WAF
Firewall
BARRACUDA_WAF
JSON, SYSLOG + KV
2025-11-26
View Change
ZScaler VPN
VPN
ZSCALER_VPN
SYSLOG + CSV
2023-06-08
View Change
Claroty Xdome
SaaS Applications
CLAROTY_XDOME
SYSLOG , JSON , KV
2025-12-19
View Change
Forescout eyeInspect
Network Monitoring
FORESCOUT_EYEINSPECT
SYSLOG, CEF
2025-12-05
View Change
Journald
Log Aggregation and SIEM Systems
JOURNALD
JSON
2025-10-03
View Change
FingerprintJS
Vulnerability scanners
FINGERPRINT_JS
JSON
2024-11-14
View Change
Salesforce
SaaS Application
SALESFORCE
KV (LEEF), CSV
2025-12-31
View Change
Cisco Application Centric Infrastructure
CISCO ACI
CISCO_ACI
JSON, SYSLOG
2025-12-05
View Change
Dell EMC Data Domain
Storage system
DELL_EMC_DATA_DOMAIN
SYSLOG + KV
2024-09-20
View Change
AWS Macie
AWS-specific logs
AWS_MACIE
JSON
2025-05-15
View Change
BloxOne Threat Defense
DNS
BLOXONE
SYSLOG + JSON
2025-01-07
View Change
Cylance Protect
Alerts
CYLANCE_PROTECT
SYSLOG + KV
2025-05-16
View Change
Winscp
Data Transfer
WINSCP
SYSLOG, CSV
2024-05-22
View Change
OneLogin
SSO
ONELOGIN_SSO
JSON
2026-01-01
View Change
1Password
Identity and Access Management
ONEPASSWORD
JSON
2025-10-01
View Change
McAfee Unified Cloud Edge
SaaS Application
MCAFEE_UCE
JSON
2021-07-20
Verba Recording System
Recording System
VERBA_REC
CSV
2024-05-24
View Change
NGINX
Server Management
NGINX
JSON + SYSLOG
2025-12-19
View Change
Netskope V2
Cloud Security
NETSKOPE_ALERT_V2
JSON, CSV
2025-12-11
View Change
Tanium Integrity Monitor
Tanium Specific
TANIUM_INTEGRITY_MONITOR
JSON
2025-10-28
View Change
CrowdStrike Detection Monitoring
EDR
CS_DETECTS
JSON
2026-01-06
View Change
ZScaler NGFW
Firewall
ZSCALER_FIREWALL
JSON
2026-01-07
View Change
Imperva Advanced Bot Protection
Bot Protection
IMPERVA_ABP
JSON
2024-12-05
View Change
Juniper Software Defined Wide Area Network
SYSLOG
JUNIPER_SDWAN
SYSLOG
2023-07-10
View Change
Microsoft Exchange
Email Server
EXCHANGE_MAIL
SYSLOG
2025-09-30
View Change
Apache Cassandra
Web server
CASSANDRA
JSON
2022-04-13
View Change
Oracle NetSuite
CASB
ORACLE_NETSUITE
JSON
2025-03-06
View Change
Microstrategy
Application server logs
MICROSTRATEGY
SYSLOG
2025-03-21
View Change
Nokia VitalQIP
DDI (DNS, DHCP, IPAM)
VITALQIP
SYSLOG
2022-03-01
Cloudflare Warp
Data Security
CLOUDFLARE_WARP
JSON
2025-10-29
View Change
Ipswitch SFTP
Data Transfer
IPSWITCH_SFTP
SYSLOG+KV, JSON
2025-05-14
View Change
NIMBLE OS
OS
NIMBLE_OS
SYSLOG
2022-07-21
View Change
TXOne Stellar
AV and Endpoint logs
TRENDMICRO_STELLAR
SYSLOG , JSON
2025-12-03
View Change
Azure App Service
SAAS
AZURE_APP_SERVICE
JSON
2024-10-18
View Change
GMAIL Logs
Google Cloud Specific
GMAIL_LOGS
JSON
2024-05-10
View Change
Oracle WebLogic Server
Web server logs
ORACLE_WEBLOGIC
SYSLOG
2024-10-30
View Change
TINTRI
Data Security
TINTRI
syslog
2024-09-17
View Change
CyberArk Privileged Access Manager (PAM)
CyberArk Privileged Access Manager
CYBERARK_PAM
SYSLOG, JSON
2026-01-16
View Change
Imperva SecureSphere Management
Data Security / Insider Threat
IMPERVA_SECURESPHERE
SYSLOG + KV (CEF)
2025-11-05
View Change
Fortinet Web Application Firewall
WEB
FORTINET_FORTIWEB
KV
2026-01-05
View Change
Office 365
SaaS Application
OFFICE_365
JSON
2026-01-22
View Change
Solarwinds Kiwi Syslog Server
Security Log
SOLARWINDS_KSS
SYSLOG + KV
2024-06-11
View Change
Extreme Networks Switch
Security
EXTREME_SWITCH
SYSLOG
2025-09-01
View Change
Fortinet FortiClient
Security
FORTINET_FORTICLIENT
KV
2025-01-13
View Change
Passwordstate
below is a catch all for tokens, phones, groups, and endpoints
PASSWORDSTATE
SYSLOG
2025-10-10
View Change
Akamai WAF
WAF
AKAMAI_WAF
SYSLOG
2025-07-22
View Change
Jamf Protect Alerts
Endpoint Security
JAMF_PROTECT
JSON
2024-10-08
View Change
Fortinet FortiDDoS
Network
FORTINET_FORTIDDOS
KV
2025-01-10
View Change
AWS ECS Metrics
Security
AWS_ECS_METRICS
SYSLOG + KV
2025-02-06
View Change
Palo Alto Cortex XDR Alerts
NDR
CORTEX_XDR
JSON, SYSLOG + KV
2025-10-08
View Change
CyberArk PTA Privileged Threat Analytics
AUDIT
CYBERARK_PTA
SYSLOG + KV (CEF)
2024-08-13
View Change
AWS CloudFront
CDN
AWS_CLOUDFRONT
SYSLOG, JSON, SYSLOG + KV
2025-09-12
View Change
Sentinelone Activity
Endpoint Security
SENTINELONE_ACTIVITY
JSON
2025-10-10
View Change
Sophos DHCP
DHCP
SOPHOS_DHCP
SYSLOG + KV
2022-02-10
IBM Websphere Application Server
Web server
IBM_WEBSPHERE_APP_SERVER
JSON, SYSLOG
2025-10-03
View Change
Micro Focus iManager
Network Management and Optimization
MICROFOCUS_IMANAGER
SYSLOG
2025-01-02
View Change
Yubico OTP
Audit event
YUBICO_OTP
SYSLOG, JSON, CSV
2023-02-20
View Change
Zendesk CRM
Ticketing Applications
ZENDESK_CRM
JSON
2025-09-02
View Change
Microsoft Defender for Endpoint
EDR
MICROSOFT_DEFENDER_ENDPOINT
JSON
2025-12-05
View Change
CrushFTP
Application server
CRUSHFTP
SYSLOG+KV
2025-01-23
View Change
NetDocuments Solutions
Threat Management Firewall
NETDOCUMENTS
Cloud-Based Document Management System
2024-05-06
View Change
Oort Security Tool
Identity and Access Management
OORT
JSON
2025-01-23
View Change
Aware Audit
Application server logs
AWARE_AUDIT
JSON
2025-02-10
View Change
RSA NetWitness
PLATFORM CONFIGURATION
RSA_NETWITNESS
SYSLOG
2022-10-18
View Change
Cisco Meraki
Wireless
CISCO_MERAKI
SYSLOG, JSON
2025-12-22
View Change
AWS Route 53 DNS
AWS Specific
AWS_ROUTE_53
JSON + SYSLOG
2025-04-22
View Change
Ping One
NA
PING_ONE
JSON
2025-11-06
View Change
Tenable OT
Vulnerability Scanners
TENABLE_OT
SYSLOG+CEF
2025-11-25
View Change
Kiteworks
Network
KITEWORKS
SYSLOG, CSV, SYSLOG+JSON, SYSLOG+KV, JSON
2025-11-14
View Change
RSA SecurID Access Identity Router
SECURITY
RSA_SECURID
SYSLOG + CSV
2024-12-23
View Change
Sangfor Next Generation Firewall
Firewall
SANGFOR_NGAF
SYSLOG + KV
2025-10-17
View Change
Preempt Auth
Identity and Access Management
PREEMPT_AUTH
SYSLOG + JSON
2021-06-16
UPX AntiDDoS
DDOS Mitigation
UPX_ANTIDDOS
JSON
2025-02-13
View Change
Check Point Sandblast
EDR
CHECKPOINT_EDR
SYSLOG + KV and SYSLOG + CEF
2025-09-12
View Change
Stealthbits PAM
Privileged Access Management Solution
STEALTHBITS_PAM
CEF + KV
2023-11-07
View Change
Intel 471 Malware Intelligence
INTEL471_MALWARE_INTEL
JSON
2024-11-21
View Change
Cambium Networks
Switches and Routers Log Type
CAMBIUM_NETWORKS
SYSLOG
2025-10-28
View Change
Virtru Email Encryption
EMAIL SERVER
VIRTRU_EMAIL_ENCRYPTION
JSON
2024-12-19
View Change
Trend Micro Vision One Container Vulnerabilities
Schema
TRENDMICRO_VISION_ONE_CONTAINER_VULNERABILITIES
JSON
2025-04-07
View Change
Tines
Data Security
TINES
JSON
2024-10-01
View Change
Lucid
Authentication log types.
LUCID
JSON
2024-06-19
View Change
SentinelOne Deep Visibility
EDR
SENTINEL_DV
JSON
2025-10-14
View Change
Kubernetes Audit
K8s cluster audit logs
KUBERNETES_AUDIT
JSON
2025-02-19
View Change
DomainTools Threat Intelligence
Threat intelligence
DOMAINTOOLS_THREATINTEL
JSON
2023-12-13
View Change
Duo Entity context data
Identity and Access Management
DUO_CONTEXT
JSON
2022-03-14
EfficientIP DDI
Network
EFFICIENTIP_DDI
SYSLOG + KV
2025-11-04
View Change
Cisco EStreamer
Network Monitoring
CISCO_ESTREAMER
SYSLOG + KV
2025-03-17
View Change
AWS Session Manager
AWS Specific
AWS_SESSION_MANAGER
SYSLOG/JSON
2025-04-30
View Change
Reserved LogType2
LDAP
RESERVED_LOG_TYPE_2
JSON
2024-12-09
View Change
Forcepoint Mail Relay
Email Server
FORCEPOINT_MAIL_RELAY
JSON
2025-04-09
View Change
ChromeOS XDR
SaaS Applications
CHROMEOS_XDR
JSON
2025-01-30
View Change
Zero Networks
Security
ZERO_NETWORKS
JSON
2025-03-13
View Change
Dell Switch
Switches, Routers
DELL_SWITCH
SYSLOG
2026-01-09
View Change
PostgreSQL
Database
POSTGRESQL
JSON,KV,SYSLOG
2025-12-02
View Change
Neosec
Security
NEOSEC
JSON
2023-07-31
View Change
Amazon VPC Transit Gateway Flow Logs
Network
AWS_VPC_TRANSIT_GATEWAY
JSON
2025-09-19
View Change
AWS Network Firewall
Firewall
AWS_NETWORK_FIREWALL
JSON
2025-03-12
View Change
Hitachi Cloud Platform
Hitachi Cloud Platform
HITACHI_CLOUD_PLATFORM
SYSLOG
2023-05-30
View Change
AWS Redshift
AWS
AWS_REDSHIFT
JSON + CSV + SYSLOG
2025-04-16
View Change
Workday User Activity
N/A
WORKDAY_USER_ACTIVITY
SYSLOG + JSON , JSON
2025-10-03
View Change
Teradata DB
Database log types
TERADATA_DB
SYSLOGgcert
2025-06-17
View Change
Imperva Database
Cloud Application and Edge Security
IMPERVA_DB
SYSLOG, SYSLOG+JSON
2025-02-19
View Change
Snare System Diagnostic Logs
Security
SNARE_SOLUTIONS
SYSLOG + KV , SYSLOG + JSON
2025-11-21
View Change
Cofense
Email Server
COFENSE_TRIAGE
SYSLOG + KV (CEF)
2024-06-18
View Change
Tanium Comply
Tanium Specific
TANIUM_COMPLY
JSON
2022-08-18
View Change
JAMF CMDB
Computer Inventory
JAMF
JSON
2024-05-28
View Change
Carbon Black
EDR
CB_EDR
JSON, SYSLOG
2025-12-18
View Change
F5 BIGIP Access Policy Manager
Access Policy Manager
F5_BIGIP_APM
SYSLOG
2025-12-15
View Change
Passive DNS
DNS
PASSIVE_DNS
JSON
2021-05-19
Cloudflare Network Analytics
SaaS Application
CLOUDFLARE_NETWORK_ANALYTICS
JSON
2025-09-11
View Change
Menlo Security
Web Proxy
MENLO_SECURITY
JSON
2025-07-29
View Change
Jamf pro context
Mobile Device Management
JAMF_PRO_CONTEXT
JSON
2025-11-28
View Change
Zoom Operation Logs
Operation-Specific
ZOOM_OPERATION_LOGS
SYSLOG
2025-11-06
View Change
Workspace Users
Google Cloud Specific
WORKSPACE_USERS
JSON
2025-08-27
View Change
Cisco Internetwork Operating System
Network Infrastructure
CISCO_IOS
SYSLOG
2026-01-20
View Change
Security Command Center Threat
Google Cloud Specific
N/A
JSON
2025-12-05
View Change
Fortinet FortiSandbox
AV and endpoint logs
FORTINET_SANDBOX
SYSLOG + KV
2025-02-26
View Change
FireEye PX
Firewall
FIREEYE_PX
JSON
2024-01-05
View Change
Palo Alto Prisma Cloud
SECURITY PLATFORM
PAN_PRISMA_CLOUD
JSON
2024-11-18
View Change
Vectra Detect
NDR
VECTRA_DETECT
JSON + SYSLOG + CEF
2025-12-30
View Change
Qualys Asset Context
Vulnerability Scanner
QUALYS_ASSET_CONTEXT
JSON
2023-08-01
View Change
EPIC Systems
Discovery and Monitoring
EPIC
LEEF + KV
2025-07-24
View Change
Cloud Functions Context
Google Cloud Specific
GCP_CLOUD_FUNCTIONS_CONTEXT
JSON
2023-07-26
View Change
Cisco Umbrella IP
Web Proxy
UMBRELLA_IP
SYSLOG
2025-10-07
View Change
Symantec VIP Authentication Hub
VPN
SYMANTEC_VIP_AUTHHUB
JSON
2025-03-11
View Change
Cisco Wireless IPS
Cisco Wips
CISCO_WIPS
SYSLOG + KV
2023-11-17
View Change
CloudM
Identity and Access Management
CLOUDM
JSON
2022-06-09
View Change
Cisco Umbrella Cloud Firewall
Firewall
UMBRELLA_FIREWALL
CSV
2025-10-06
View Change
Azure Firewall
Azure Firewall Application Rule
AZURE_FIREWALL
JSON
2025-09-29
View Change
GitGuardian Enterprise
SaaS Applications
GITGUARDIAN_ENTERPRISE
JSON
2024-10-16
View Change
Palo Alto Prisma Cloud Alert payload
Cloud Security
PAN_PRISMA_CA
JSON
2025-09-05
View Change
Bluecat DDI
DDI (DNS, DHCP, IPAM)
BLUECAT_DDI
SYSLOG
2022-11-08
View Change
Obsidian
NA
OBSIDIAN
JSON
2026-01-13
View Change
Trellix HX Event Streamer
Cybersecurity
TRELLIX_HX_ES
SYSLOG + KV
2026-01-08
View Change
Palo Alto Networks Traps
EDR
PAN_EDR
CSV + KV
2022-08-22
View Change
Mimecast URL Logs
Email server log types.
MIMECAST_URL_LOGS
JSON
2025-01-16
View Change
Ubika Waf
WAF
UBIKA_WAF
JSON + SYSLOG, SYSLOG
2025-11-02
View Change
Red Hat OpenShift
Kubernetes Container
REDHAT_OPENSHIFT
SYSLOG
2025-12-22
View Change
Static IP
DHCP
ASSET_STATIC_IP
CSV
2023-06-16
View Change
Network Policy Server
Network Policy Server
MICROSOFT_NPS
JSON + XML, JSON + CSV
2025-12-31
View Change
TCPWave DDI
Secure ddi
TCPWAVE_DDI
SYSLOG + JSON, SYSLOG
2025-12-02
View Change
IBM Security QRadar SOAR
Security
IBM_SOAR
SYSLOG + KV
2024-10-08
View Change
Forcepoint CASB
CASB
FORCEPOINT_CASB
SYSLOG + CEF
2022-08-23
View Change
Microsoft AD
LDAP
WINDOWS_AD
JSON
2025-07-08
View Change
McAfee Web Protection
SaaS Application
MCAFEE_WEB_PROTECTION
JSON
2025-04-16
View Change
ADVA Fiber Service Platform
Switches and Routers
ADVA_FSP
SYSLOG+KV
2023-12-18
View Change
NetApp SAN
Rest api
NETAPP_SAN
SYSLOG
2023-04-25
View Change
Area1 Security
Email server
AREA1
JSON
2024-09-23
View Change
ServiceNow Audit
SaaS Application
SERVICENOW_AUDIT
JSON, Syslog, kv
2025-12-19
View Change
Microsoft System Center Endpoint Protection
Malware Detection
MICROSOFT_SCEP
KV
2025-02-24
View Change
Fortinet FortiAuthenticator
Security
FORTINET_FORTIAUTHENTICATOR
SYSLOG + KV, KV
2025-05-06
View Change
Snowflake
Database
SNOWFLAKE
JSON, CSV
2025-04-15
View Change
Tanium Patch
Tanium Specific
TANIUM_PATCH
JSON
2022-02-08
Cisco Vision Dynamic Signage Director
Content and Delivery Management
CISCO_STADIUMVISION
SYSLOG, SYSLOG+KV
2023-05-12
View Change
TACACS Plus
Authentication log types
TACACS_PLUS
SYSLOG
2025-03-13
View Change
Dope Security SWG
Secure Access Service Edge
DOPE_SWG
CSV,JSON
2025-03-12
View Change
Deep Instinct EDR
EDR
DEEP_INSTINCT_EDR
LEEF
2023-12-27
View Change
IBM Security Verify
Endpoint Security
IBM_SECURITY_VERIFY
SYSLOG,SYSLOG+XML
2024-05-13
View Change
Linux DHCP
DHCP
LINUX_DHCP
SYSLOG
2024-09-05
View Change
Check Point Harmony
Remote Access Tools
CHECKPOINT_HARMONY
SYSLOG+KV
2025-01-08
View Change
Okta Scaleft
Identity and Access Management
OKTA_SCALEFT
JSON
2025-08-18
View Change
Pulse Secure
VPN
PULSE_SECURE_VPN
SYSLOG
2025-12-10
View Change
XAMS by Xiting
Log Aggregator
XITING_XAMS
SYSLOG
2024-09-26
View Change
Brocade Switch
Switches
BROCADE_SWITCH
SYSLOG, CSV
2025-06-03
View Change
Aqua Security
IaaS Applications
AQUA_SECURITY
JSON
2025-07-03
View Change
Splunk Attack Analyzer
CLOUD SECURITY
SPLUNK_ATTACK_ANALYZER
JSON
2024-08-05
View Change
Windows Firewall
Firewall
WINDOWS_FIREWALL
Space Separated Value
2021-08-26
Samba SMBD
Privileged Account Activity
SMBD
Syslog
2023-03-09
View Change
WindChill
Lifecycle Management Software
WINDCHILL
SYSLOG
2024-11-21
View Change
Zscaler CASB
CASB
ZSCALER_CASB
JSON
2026-01-06
View Change
Cisco Secure Workload
AV and Endpoint
CISCO_SECURE_WORKLOAD
JSON
2024-12-02
View Change
ProFTPD
Web Server
PROFTPD
SYSLOG
2025-01-12
View Change
Ciena Router logs
Application server logs
CIENA_ROUTER
SYSLOG
2024-10-31
View Change
Workspace Privileges
Google Cloud Specific
WORKSPACE_PRIVILEGES
JSON
2023-11-29
View Change
Tenable Audit
Application server
TENABLE_AUDIT
JSON
2024-08-09
View Change
Trend Micro Vision One Audit
Schema
TRENDMICRO_VISION_ONE_AUDIT
JSON
2025-09-29
View Change
Shrubbery TACACS+
NETWORK MANAGEMENT
SHRUBBERY_TACACS
SYSLOG + KV
2022-11-08
View Change
Thales Vormetric
Encryption
VORMETRIC
SYSLOG
2024-08-05
View Change
Tailscale
CASB
TAILSCALE
JSON
2024-11-21
View Change
McAfee ePolicy Orchestrator
Policy Management
MCAFEE_EPO
SYSLOG + XML, CSV, KV, JSON
2026-01-21
View Change
ThreatConnect
IOC
THREATCONNECT_IOC
JSON
2022-01-13
Azure AD
LDAP
AZURE_AD
JSON
2026-01-01
View Change
ExtraHop RevealX
Firewall IDS/IPS
EXTRAHOP
JSON, SYSLOG
2025-12-26
View Change
McAfee Web Gateway
Web Proxy
MCAFEE_WEBPROXY
SYSLOG + KV (CEF), JSON
2026-01-21
View Change
Kong API Gateway
Microservice management
KONG_GATEWAY
SYSLOG + JSON
2022-09-23
View Change
Imperva CEF
CEF
IMPERVA_CEF
SYSLOG + KV
2024-09-12
View Change
McAfee MVISION CASB
CLOUD SECURITY
MCAFEE_MVISION_CASB
KV
2023-06-22
View Change
Cisco Email Security
Email Server
CISCO_EMAIL_SECURITY
SYSLOG + KV, JSON
2025-12-12
View Change
Bluecat Edge DNS Resolver
DNS
BLUECAT_EDGE
JSON, KV, SYSLOG
2022-01-18
F5 Silverline
Application
F5_SILVERLINE
SYSLOG, SYSLOG + KV , JSON
2025-11-04
View Change
Comforte SecurDPS
Data loss prevention
COMFORTE_SECURDPS
SYSLOG + KV, JSON
2024-06-10
View Change
Cimcor | File Integrity Monitoring
Monitoring
CIMCOR
SYSLOG + KV
2024-06-18
View Change
Microsoft Defender for Office 365
Email server log types.
MICROSOFT_DEFENDER_MAIL
JSON
2025-09-19
View Change
Workspace Activities
Google Cloud Specific
WORKSPACE_ACTIVITY
JSON
2025-12-24
View Change
Symantec EDR
EDR
SYMANTEC_EDR
JSON
2025-04-18
View Change
RSA
Identity and Access Management
RSA_AUTH_MANAGER
CSV
2025-10-29
View Change
Cisco Firewall Services Module
Firewall
CISCO_FWSM
SYSLOG
2025-10-17
View Change
Cloud DNS
Google Cloud Specific
N/A
JSON
2025-07-01
View Change
IBM DB2
Database
DB2_DB
LEEF,Syslog+KV
2025-12-04
View Change
Windows Local Administrator Password Solution
Local Administrator Password Solution
MICROSOFT_LAPS
JSON
2024-10-10
View Change
Cloud NAT
Google Cloud Specific
N/A
JSON
2024-05-01
View Change
Slack Audit
Productivity
SLACK_AUDIT
JSON
2025-03-28
View Change
Fluentd Logs
Log Aggregator
FLUENTD
SYSLOG + JSON
2025-10-31
View Change
Cloud Passage
SaaS Application
CLOUD_PASSAGE
JSON
2022-06-30
View Change
Pulse Secure Virtual Traffic Manager
Traffic Shapers
PULSE_SECURE_VTM
SYSLOG
2023-11-03
View Change
WatchGuard
Syslog and KV
WATCHGUARD
JSON
2025-12-19
View Change
Cisco ACS
Authentication
CISCO_ACS
SYSLOG + KV
2024-11-14
View Change
AWS Cloudtrail
Cloud Log Aggregator
AWS_CLOUDTRAIL
JSON
2025-12-11
View Change
Microsoft Defender Endpoint for iOS Logs
MICROSOFT_DEFENDER_ENDPOINT_IOS
JSON
2025-03-10
View Change
Proofpoint Tap Threats
Email Server
PROOFPOINT_TAP_THREATS
JSON
2025-01-09
View Change
Openpath
AV / Endpoint
OPENPATH
SYSLOG
2025-06-10
View Change
AWS Aurora
AWS
AWS_AURORA
JSON
2026-01-26
View Change
Security Command Center Toxic Combination
Google Cloud Specific
GCP_SECURITYCENTER_TOXIC_COMBINATION
JSON
2025-12-04
View Change
Juniper MX Router
Routers and Switches
JUNIPER_MX
SYSLOG + KV
2025-11-18
View Change
Hillstone Firewall
Application server logs
HILLSTONE_NGFW
SYSLOG + KV
2025-02-04
View Change
F5 ASM
WAF
F5_ASM
SYSLOG, CSV, JSON
2025-12-23
View Change
GTB Technologies DLP
Security
GTB_DLP
SYSLOG+KV, SYSLOG+JSON
2025-10-28
View Change
IBM Mainframe Storage
Monitoring
IBM_MAINFRAME_STORAGE
SYSLOG
2024-10-03
View Change
Varonis
Data Security / Insider Threat
VARONIS
SYSLOG + KV (CEF), LEEF
2025-10-08
View Change
SAP SAST Suite
Security
SAP_SAST
SYSLOG
2023-12-28
View Change
Duo Telephony Logs
Identity and Access Management
DUO_TELEPHONY
JSON
2023-08-24
View Change
Zscaler
Web Proxy
ZSCALER_WEBPROXY
JSON
2026-01-12
View Change
Apigee
Google Cloud Specific
GCP_APIGEE
JSON
2025-10-23
View Change
Trend Micro Vision One Activity
Schema
TRENDMICRO_VISION_ONE_ACTIVITY
JSON
2025-08-08
View Change
Arista Switch
Switches
ARISTA_SWITCH
JSON+SYSLOG
2025-12-16
View Change
Zscaler Private Access
Security Service Edge
ZSCALER_ZPA
JSON
2026-01-07
View Change
Forseti Open Source
Google Cloud Specific
FORSETI
JSON
2021-12-23
Phishlabs
Digital Risk Protection
PHISHLABS
JSON
2024-03-22
View Change
Keeper Enterprise Security
Security
KEEPER
JSON
2024-12-12
View Change
Cisco IronPort
Gateway Security
CISCO_IRONPORT
SYSLOG + CSV
2025-11-13
View Change
Avigilon Access Logs
IaaS Applications
AVIGILON_ACCESS_LOGS
XML
2024-12-18
View Change
Zscaler Internet Access Audit Logs
Security Service Edge (SSE)
ZSCALER_INTERNET_ACCESS
JSON
2026-01-09
View Change
Tenable Active Directory Security
Tenable Active Directory Security
TENABLE_ADS
SYSLOG
2025-12-23
View Change
Bitdefender
AV / Endpoint
BITDEFENDER
CSV, SYSLOG
2025-10-30
View Change
Atlassian Jira
Ticketing Application
ATLASSIAN_JIRA
SYSLOG, JSON
2023-12-12
View Change
Dell CyberSense
Data Security
DELL_CYBERSENSE
SYSLOG
2025-02-13
View Change
MySQL
Database
MYSQL
SYSLOG, JSON
2025-12-04
View Change
IBM z/OS
OS
IBM_ZOS
LEEF
2025-11-05
View Change
JFrog Artifactory
DevOps
JFROG_ARTIFACTORY
SYSLOG
2025-10-24
View Change
Azure WAF
Log Aggregator
AZURE_WAF
JSON
2024-08-22
View Change
Microsoft SharePoint
Collaboration log types
SHAREPOINT
SYSLOG,CSV,JSON
2025-03-15
View Change
Apache Hadoop
open-source software
HADOOP
SYSLOG + KV
2023-06-05
View Change
Netwrix
Web Server
NETWRIX
JSON
2024-05-23
View Change
IBM Security Access Manager
WAF
IBM_SAM
SYSLOG
2025-04-02
View Change
Cisco ISE
Identity and Access Management
CISCO_ISE
SYSLOG , CSV
2026-01-15
View Change
IBM Security QRadar SIEM
Security Log
IBM_QRADAR
SYSLOG
2024-06-18
View Change
Delinea Secret Server
Privileged Account Activity
DELINEA_SECRET_SERVER
KV
2025-12-10
View Change
Precisely Ironstream IBM z/OS
ZOS
IRONSTREAM_ZOS
JSON
2024-11-27
View Change
VMware Workspace ONE
Logging and Troubleshooting
VMWARE_WORKSPACE_ONE
SYSLOG
2023-08-04
View Change
Okta
Identity and Access Management
OKTA
JSON
2026-01-09
View Change
Uptycs EDR
Endpoint detection and response
UPTYCS_EDR
JSON
2022-07-08
View Change
Juniper IPS
IDS/IPS
JUNIPER_IPS
SYSLOG + KV
2022-05-26
View Change
Island Browser logs
Web Browser
ISLAND_BROWSER
JSON, SYSLOG + KV (CEF), SYSLOG + KV(CEF) + JSON
2025-12-08
View Change
Abnormal Security
Email Server
ABNORMAL_SECURITY
JSON , SYSLOG
2025-09-18
View Change
Netskope Web Proxy
Web Proxy
NETSKOPE_WEBPROXY
SYSLOG, SYSLOG+JSON, JSON, CSV
2026-01-12
View Change
Checkpoint SmartDefense
SmartDefences
CHECKPOINT_SMARTDEFENSE
SYSLOG + CEF
2024-07-02
View Change
McAfee DLP
DLP
MCAFEE_DLP
CSV
2025-12-04
View Change
Anomali
IOC
ANOMALI_IOC
JSON, CEF
2024-02-09
View Change
ZScaler Deception
VPN
ZSCALER_DECEPTION
SYSLOG+JSON
2025-08-12
View Change
Digital Guardian DLP
DLP
DIGITALGUARDIAN_DLP
JSON,SYSLOG+XML
2025-03-27
View Change
Trend Micro Cloud one
Cloud Security
TRENDMICRO_CLOUDONE
SYSLOG, JSON
2025-07-29
View Change
Neo4j
Database management system
NEO4J
JSON
2023-12-07
View Change
Stormshield Firewall
FIREWALL
STORMSHIELD_FIREWALL
SYSLOG + KV
2026-01-22
View Change
Centrify
SSO
CENTRIFY_SSO
JSON
2022-08-10
View Change
Sophos AV
AV / Endpoint
SOPHOS_AV
CSV, JSON
2024-08-22
View Change
Saviynt Enterprise Identity Cloud
Endpoints
SAVIYNT_EIP
JSON, JSON+KV
2023-06-05
View Change
Edgio WAF
Web Application Firewall
EDGIO_WAF
JSON
2025-02-04
View Change
ClamAV
AV / Endpoint
CLAM_AV
JSON
2022-02-07
Rapid7
Vulnerability Scanner
RAPID7_NEXPOSE
JSON
2024-05-14
View Change
D3 Banking
BANKING
D3_BANKING
JSON
2022-03-23
View Change
Veritas NetBackup
Backup software
VERITAS_NETBACKUP
SYSLOG
2026-01-15
View Change
Ribbon Analytics Platform
Telephone Software
RIBBON_ANALYTICS_PLATFORM
SYSLOG
2022-09-09
View Change
Snipe-IT
SaaS Applications
SNIPE_IT
JSON
2025-02-12
View Change
Preempt Alert
Identity and Access Management
PREEMPT
SYSLOG + KV (CEF)
2022-06-22
View Change
FireEye
Alerts
FIREEYE_ALERT
SYSLOG + JSON, JSON, KV, SYSLOG
2025-08-12
View Change
File Scanning Framework
File scanning
FILE_SCANNING_FRAMEWORK
JSON
2021-09-27
Cisco Call Manager
NETWORKING
CISCO_CALL_MANAGER
SYSLOG
2024-10-23
View Change
CA Access Control
Access Management
CA_ACCESS_CONTROL
JSON+SYSLOG, SYSLOG
2023-07-25
View Change
Awake NDR
NDR
AWAKE_NDR
JSON
2024-01-11
View Change
GCP_MODEL_ARMOR
GCP-specific log types
GCP_MODEL_ARMOR
JSON
2025-11-19
View Change
Aruba EdgeConnect SD-WAN
Network Security
ARUBA_EDGECONNECT_SDWAN
SYSLOG + CSV
2026-01-05
View Change
HPE ILO
Server Management
HPE_ILO
SYSLOG
2023-11-27
View Change
FireEye eMPS
Email server log types.
FIREEYE_EMPS
JSON, CEF
2024-10-29
View Change
SentinelOne Singularity Cloud Funnel
EVENTS
SENTINELONE_CF
JSON
2025-03-20
View Change
Vectra Stream
NDR
VECTRA_STREAM
JSON + SYSLOG + CEF
2025-08-28
View Change
Tripwire
DLP
TRIPWIRE_FIM
SYSLOG
2025-06-30
View Change
Archer Integrated Risk Management
Risk Management Solution
ARCHER_IRM
SYSLOG
2024-08-27
View Change
Infoblox DHCP
DHCP
INFOBLOX_DHCP
SYSLOG
2025-09-01
View Change
Venafi ZTPKI
AV and Endpoint logs
VENAFI_ZTPKI
SYSLOG , JSON
2025-10-14
View Change
Oracle
DATABASE
ORACLE_DB
SYSLOG + KV, SYSLOG
2025-12-29
View Change
Windows DHCP
DHCP
WINDOWS_DHCP
JSON, SYSLOG, CSV
2025-06-10
View Change
LastPass Password Management
Identity and Access Management
LASTPASS
JSON
2025-05-29
View Change
Imperva DRA
Data Security
IMPERVA_DRA
SYSLOG,json
2026-01-16
View Change
Cisco VCS Expressway
Telephone software
CISCO_VCS
SYSLOG
2025-08-22
View Change
Cloud Intrusion Detection System
Google Cloud Specific
GCP_IDS
JSON
2024-05-01
View Change
Signal Sciences WAF
WAF
SIGNAL_SCIENCES_WAF
JSON
2024-05-13
View Change
Proofpoint Observeit
Email Server
OBSERVEIT
JSON, KV
2025-10-31
View Change
DNSFilter
Data Transfer
DNSFILTER
CSV
2023-10-27
View Change
GCP_MONITORING_ALERTS
Application server logs
GCP_MONITORING_ALERTS
JSON
2024-07-09
View Change
Cisco Secure Access
Remote Access Tools
CISCO_SECURE_ACCESS
CSV
2025-10-21
View Change
INTEL471 Watcher Alerts
Data Security
INTEL471_WATCHER_ALERTS
JSON
2025-04-03
View Change
DigitalArts i-Filter
Web Proxy
DIGITALARTS_IFILTER
SYSLOG
2025-10-16
View Change
Cisco Application Control Engine
Load Balancer, Traffic Shaper, ADC
CISCO_ACE
SYSLOG
2022-09-15
View Change
Resource Manager Context
Google Cloud Specific
GCP_RESOURCE_MANAGER_CONTEXT
JSON
2023-07-26
View Change
CA ACF2
Mainframe
CA_ACF2
LEEF
2022-05-24
View Change
Trend Micro Vision One Observerd Attack Techniques
Schema
TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES
JSON
2025-10-10
View Change
OpenTelemetry Netflow Receiver
OpenTelemetry Netflow Receiver
NETFLOW_OTEL
JSON
2025-04-23
View Change
Quest Change Auditor for EMC
Alert
QUEST_CHANGE_AUDITOR_EMC
JSON
2024-06-18
View Change
Suricata IDS
IDS/IPS
SURICATA_IDS
JSON
2024-12-03
View Change
Zywall
Network infrastructure
ZYWALL
KV
2025-12-08
View Change
Sendmail
Email Server
SENDMAIL
SYSLOG + KV
2023-09-20
View Change
Netskope CASB
CASB
NETSKOPE_CASB
JSON
2025-09-29
View Change
Snort
IDS/IPS
SNORT_IDS
SYSLOG + JSON
2024-12-04
View Change
Guardicore Centra
Deception Software
GUARDICORE_CENTRA
JSON
2025-06-10
View Change
Palo Alto Panorama
Firewall
PAN_PANORAMA
CSV
2026-01-26
View Change
WPEngine
Firewall log types
WPENGINE
SYSLOG
2025-02-11
View Change
KnowBe4 PhishER
Email server log types.
KNOWBE4_PHISHER
JSON
2025-12-12
View Change
Duo Activity Logs
Activity
DUO_ACTIVITY
JSON
2024-08-28
View Change
Sysdig
Security
SYSDIG
JSON
2025-08-07
View Change
TrendMicro Web Proxy
Web Proxy
TRENDMICRO_WEBPROXY
SYSLOG + KV
2024-03-26
View Change
Airlock Digital Application Allowlisting
Application Whitelisting
AIRLOCK_DIGITAL
SYSLOG,JSON
2024-11-07
View Change
Elastic Defend
Network Monitoring
ELASTIC_DEFEND
JSON
2025-08-08
View Change
Cybergatekeeper NAC
Security
CYBERGATEKEEPER_NAC
SYSLOG + KV
2024-04-23
View Change
AWS VPN
VPN
AWS_VPN
JSON
2024-09-19
View Change
SAP SM20
Security Audit Log
SAP_SM20
JSON
2025-07-07
View Change
CrowdStrike Falcon
EDR
CS_EDR
JSON
2026-01-20
View Change
Thycotic
Identity and Access Management
THYCOTIC
SYSLOG + KV (CEF)
2024-10-08
View Change
VMware AirWatch
Wireless
AIRWATCH
SYSLOG + KV
2025-06-05
View Change
Workspace ChromeOS Devices
Google Cloud Specific
WORKSPACE_CHROMEOS
JSON
2024-12-03
View Change
Tanium Discover
Tanium Specific
TANIUM_DISCOVER
JSON
2022-11-24
View Change
Splunk Platform
Security log
SPLUNK
JSON
2024-05-01
View Change
Mattermost
Alerts
MATTERMOST
JSON , SYSLOG
2023-12-15
View Change
AWS EC2 Hosts
AWS Specific
AWS_EC2_HOSTS
JSON
2024-01-31
View Change
Imperva
WAF
IMPERVA_WAF
SYSLOG+KV, JSON
2026-01-08
View Change
Cisco PIX Firewall
Firewall
CISCO_PIX_FIREWALL
SYSLOG
2025-12-23
View Change
Druva Backup
Security
DRUVA_BACKUP
JSON
2024-12-05
View Change
Akamai DataStream 2
SaaS Applications
AKAMAI_DATASTREAM_2
JSON
2025-04-10
View Change
Palantir
Foundry SaaS
PALANTIR
JSON
2024-12-12
View Change
Zscaler Tunnel
N/A
ZSCALER_TUNNEL
JSON
2026-01-06
View Change
Synology
DATA STORAGE
SYNOLOGY
SYSLOG
2024-01-16
View Change
IAM Context
Google Cloud Specific
N/A
JSON
2024-03-13
View Change
SentinelOne EDR
EDR
SENTINEL_EDR
SYSLOG + JSON
2025-07-23
View Change
Cisco Switch
Switches, Routers
CISCO_SWITCH
SYSLOG
2026-01-08
View Change
Microsoft Graph Activity Logs
AUDIT
MICROSOFT_GRAPH_ACTIVITY_LOGS
JSON
2024-10-08
View Change
Cisco DNA Center Platform
Network Management and Optimization
CISCO_DNAC
SYSLOG+JSON
2025-08-14
View Change
IBM Tivoli
Monitoring
IBM_TIVOLI
JSON, SYSLOG
2024-03-15
View Change
Kemp Load Balancer
Load Balancer, Traffic Shaper, ADC
KEMP_LOADBALANCER
SYSLOG + KV
2025-08-25
View Change
Crowdstrike Identity Protection Services
AV AND ENDPOINT LOGS
CS_IDP
JSON
2025-01-28
View Change
Okta Access Gateway
OKTA specific
OKTA_ACCESS_GATEWAY
SYSLOG + KV
2023-02-20
View Change
AWS EC2 VPCs
AWS Specific
AWS_EC2_VPCS
JSON
2024-01-31
Oracle Cloud Infrastructure
Oracle Cloud Infrastructure
ORACLE_CLOUD_AUDIT
JSON
2025-05-21
View Change
Claroty Enterprise Management Console
Cyber Security
CLAROTY_EMC
SYSLOG+KV
2024-04-30
View Change
CrowdStrike Falcon Stream
Alerts
CS_STREAM
KV (LEEF), JSON
2025-11-27
View Change
Maria Database
Databbase
MARIA_DB
SYSLOG
2024-12-03
View Change
Microsoft Netlogon
Authentication
MICROSOFT_NETLOGON
SYSLOG
2024-12-24
View Change
Kolide Endpoint Security
Security
KOLIDE
JSON
2026-01-16
View Change
MISP Threat Intelligence
Cybersecurity
MISP_IOC
JSON, CSV
2026-04-22
View Change
Opengear Remote Management
Secure Remote Access
OPENGEAR
SYSLOG
2024-09-13
View Change
Jamf Protect Telemetry V2
Endpoint Security
JAMF_TELEMETRY_V2
JSON
2025-11-19
View Change
Microsoft AD FS
LDAP
ADFS
JSON
2026-01-20
View Change
Sourcefire
IDS/IPS
SOURCEFIRE_IDS
JSON, CEF
2024-12-23
View Change
Windows Event
Endpoint
WINEVTLOG
JSON,XML,SYSLOG+KV,SYSLOG+JSON,SYSLOG+XML
2026-01-16
View Change
Fastly CDN
WAF
FASTLY_CDN
JSON
2026-01-02
View Change
Oracle Fusion
SaaS Application
ORACLE_FUSION
JSON
2024-10-18
View Change
Mandiant Custom IOC
IOC
MANDIANT_CUSTOM_IOC
JSON
2023-12-19
View Change
IBM AS/400
Application System
IBM_AS400
SYSLOG + KV, SYSLOG + JSON
2025-11-07
View Change
Open Cybersecurity Schema Framework (OCSF)
Schema
OCSF
JSON
2025-11-25
View Change
IBM DataPower Gateway
API Gateway
IBM_DATAPOWER
JSON, SYSLOG
2026-01-22
View Change
SAP Sybase Adaptive Server Enterprise Database
Database
SAP_ASE
SYSLOG+KV, SYSLOG + CSV
2026-01-22
View Change
Mimecast Mail V2
Email Server
MIMECAST_MAIL_V2
SYSLOG + JSON
2025-12-31
View Change
VMware vCenter
Server
VMWARE_VCENTER
SYSLOG + JSON, LEEF
2026-01-02
View Change
VMware Tanzu Kubernetes Grid
IDS/IPS
VMWARE_TANZU
JSON + SYSLOG+JSON
2023-09-08
View Change
Attivo Networks
NETWORK
ATTIVO
SYSLOG + KV (CEF)
2025-12-22
View Change
Sap Business Technology Platform
SaaS Applications
SAP_BTP
JSON
2024-07-19
View Change
macOS Endpoint Security
AV and endpoint logs
MACOS_ENDPOINT_SECURITY
SYSLOG + KV
2023-07-17
View Change
Tanium Stream
Tanium Specific
TANIUM_TH
JSON
2023-12-18
View Change
Kisi Access Management
Physical Security
KISI
JSON
2023-06-14
View Change
Cynet 360 AutoXDR
AV and endpoint logs
CYNET_360_AUTOXDR
JSON / CEF
2025-10-01
View Change
Nasuni File Services Platform
Data Transfer
NASUNI_FILE_SERVICES
SYSLOG + JSON , CSV
2025-03-24
View Change
Tanium Asset
Tanium Specific
TANIUM_ASSET
JSON, SYSLOG + KV
2025-01-08
View Change
Hashicorp Vault
Privileged Account Activity
HASHICORP
JSON, SYSLOG, SYSLOG+JSON, SYSLOG+KV
2025-12-11
View Change
Ping Federate
Authentication
PING_FEDERATE
CSV
2025-10-15
View Change
SAP Webdispatcher
Software WebSwitch
SAP_WEBDISP
SYSLOG
2024-03-15
View Change
Oracle Cloud Guard
Cloud
OCI_CLOUDGUARD
JSON
2025-02-06
View Change
Privacy-I
NA
PRIVACY_I
CSV + KV
2025-02-17
View Change
Qualys Continuous Monitoring
Monitoring
QUALYS_CONTINUOUS_MONITORING
JSON
2022-08-30
View Change
A10 Load Balancer
LOAD BALANCER
A10_LOAD_BALANCER
SYSLOG
2025-12-17
View Change
Cisco CloudLock
CASB
CISCO_CLOUDLOCK_CASB
JSON
2021-10-04
Netfilter IPtables
Firewall
NETFILTER_IPTABLES
SYSLOG + KV
2025-11-17
View Change
IBM Informix
DATABASE
INFORMIX
JSON + SYSLOG
2022-02-18
Microsoft Graph API Alerts
Gateway to data and intelligence
MICROSOFT_GRAPH_ALERT
JSON
2026-01-07
View Change
ForgeRock OpenDJ
LDAP
OPENDJ
SYSLOG + KV
2020-10-01
Cisco Umbrella Audit
Firewall and Security Management
CISCO_UMBRELLA_AUDIT
CSV
2025-09-30
View Change
Fortinet Switch
Switches and Routers
FORTINET_SWITCH
KV
2024-11-11
View Change
WordPress
Configuration Management
WORDPRESS_CMS
JSON
2024-05-07
View Change
Proofpoint Email Filter
Email Server
PROOFPOINT_MAIL_FILTER
SYSLOG + KV, SYSLOG + JSON
2025-12-02
View Change
Azure SQL
Database
AZURE_SQL
JSON
2024-12-04
View Change
ESET AV
ESET_AV
ESET_AV
SYSLOG + JSON
2025-06-03
View Change
InterSystems Cache
Database
INTERSYSTEMS_CACHE
SYSLOG + KV
2022-10-19
View Change
Dell EMC Isilon NAS
Storage
DELL_EMC_NAS
SYSLOG
2023-07-21
View Change
Sonicwall Secure Mobile Access
Authentication
SONICWALL_SMA
SYSLOG + KV, JSON
2025-03-27
View Change
Sophos Firewall (Next Gen)
Firewall
SOPHOS_FIREWALL
KV
2025-04-23
View Change
Acalvio
Deception Software
ACALVIO
SYSLOG + KV
2025-03-28
View Change
Zimperium
Mobile Device Management
ZIMPERIUM
SYSLOG + JSON
2025-11-27
View Change
Digital Guardian EDR
EDR
DIGITALGUARDIAN_EDR
KV
2025-11-13
View Change
Windows Sysmon
DNS
WINDOWS_SYSMON
JSON, XML
2025-11-04
View Change
Broadcom SSL Visibility Appliance
SSL Visibility
BROADCOM_SSL_VA
SYSLOG
2024-06-25
View Change
Automation Anywhere
Automation Tools
AUTOMATION_ANYWHERE
SYSLOG + KV, JSON
2026-01-09
View Change
Desynova Contido
Switches
DESYNOVA_CONTIDO
SYSLOG + JSON
2023-09-19
View Change
Proofpoint Threat Response
Email Server
PROOFPOINT_TRAP
SYSLOG, JSON
2025-08-14
View Change
Symantec Security Analytics
Vulnerability scanners
SYMANTEC_SA
SYSLOG + KV
2025-05-23
View Change
Cloud Load Balancing
Google Cloud Specific
GCP_LOADBALANCING
JSON
2025-08-13
View Change
Custom Security Data Analytics
Log Aggregation
CUSTOM_SECURITY_DATA_ANALYTICS
JSON
2025-05-30
View Change
Google Threat Intelligence IOC
IOC
GTI_IOC
JSON
2025-11-13
View Change
Workspace Alerts
Google Cloud Specific
WORKSPACE_ALERTS
JSON
2026-01-27
View Change
Cisco UCS
OS logs
CISCO_UCS
SYSLOG
2022-07-04
View Change
Crowdstrike IOC
IOC
CROWDSTRIKE_IOC
JSON
2025-05-30
View Change
CrowdStrike Alerts API
EDR
CS_ALERTS
JSON
2026-01-20
View Change
ManageEngine ADManager Plus
Miscellaneous Windows-specific log types.
ADMANAGER_PLUS
KV
2025-05-02
View Change
GCP_KUBERNETES_CONTEXT
Computer Inventory
GCP_KUBERNETES_CONTEXT
JSON
2023-11-01
View Change
Cribl Stream
Log Aggregation and SIEM Systems
CRIBL_STREAM
JSON
2024-06-05
View Change
Talon
Security
TALON
JSON
2023-12-21
CENSYS
NDR
CENSYS
SYSLOG + KV
2024-02-03
View Change
Elastic Audit Beats
ALERTING
ELASTIC_AUDITBEAT
JSON
2024-12-10
View Change
BeyondTrust BeyondInsight
Privileged Account Activity
BEYONDTRUST_BEYONDINSIGHT
KV , SYSLOG + JSON
2025-12-02
View Change
Proofpoint Tap Forensics
Email Server
PROOFPOINT_TAP_FORENSICS
JSON
2024-11-06
View Change
Cisco AMP
AV / Endpoint
CISCO_AMP
JSON
2025-10-06
View Change
GCP Cloud Audit
Google Cloud Specific
N/A
JSON
2026-01-22
View Change
Arcsight CEF
Security log
ARCSIGHT_CEF
CEF Syslog
2026-01-19
View Change
ThreatConnect IOC V3
IOC
THREATCONNECT_IOC_V3
JSON
2025-11-26
View Change
Fortinet FortiAnalyzer
Fortinet FortiAnalyzer
FORTINET_FORTIANALYZER
JSON, KV
2025-12-19
View Change
AWS Config
AWS Specific
AWS_CONFIG
JSON
2025-09-26
View Change
Juniper Junos
Network Device
JUNIPER_JUNOS
SYSLOG + KV
2025-10-10
View Change
Cyber 2.0 IDS
IDS
CYBER_2_IDS
SYSLOG+JSON
2025-09-04
View Change
Trend Micro Email Security Advanced
Email Security
TRENDMICRO_EMAIL_SECURITY
CEF
2025-02-20
View Change
Cybereason EDR
EDR
CYBEREASON_EDR
JSON
2025-10-13
View Change
BMC AMI Defender
Mainframe
BMC_AMI_DEFENDER
SYSLOG
2024-05-27
View Change
Barracuda Email
Email Server
BARRACUDA_EMAIL
SYSLOG+JSON, JSON
2026-01-22
View Change
Qualys Scan
Vulnerability scanner
QUALYS_SCAN
JSON
2023-04-21
View Change
Array Networks SSL VPN
VPN
ARRAYNETWORKS_VPN
SYSLOG, SYSLOG + KV
2024-05-14
View Change
Fortinet FortiEDR
EDR
FORTINET_FORTIEDR
SYSLOG + KV
2025-11-12
View Change
IBM Tape Storages
Monitoring
IBM_LTO
Syslog
2024-05-02
View Change
Microsoft CyberX
IoT
CYBERX
SYSLOG+KV
2025-04-14
View Change
GitHub Dependabot
Application server logs
GITHUB_DEPENDABOT
JSON
2025-12-17
View Change
Lacework Cloud Security
Cloud Security
LACEWORK
JSON
2025-06-27
View Change
VMware vRealize Suite (VMware Aria)
Cloud
VMWARE_VREALIZE
SYSLOG
2025-08-05
View Change
Aruba
Wireless
ARUBA_WIRELESS
SYSLOG
2026-01-08
View Change
ZScaler DNS
DNS
ZSCALER_DNS
JSON
2026-01-09
View Change
UKG
NA
UKG
JSON
2025-02-12
View Change
Akamai Enterprise Application Access
Enterprise Application Access
AKAMAI_EAA
JSON
2025-07-15
View Change
CrowdStrike Filevantage
IT infrastructure
CS_FILEVANTAGE
JSON
2025-04-16
View Change
IBM OpenPages
Data Security
IBM_OPENPAGES
SYSLOG
2024-10-10
View Change
NGFW Enterprise
Google Cloud Specific
GCP_NGFW_ENTERPRISE
JSON
2024-04-16
View Change
OpenAI AuditLog
NDR
OPENAI_AUDITLOG
JSON
2025-03-20
AppOmni
SAAS Security Application
APPOMNI
JSON
2025-11-24
View Change
UberAgent
Security
UBERAGENT
CSV
2024-12-29
View Change
Versa Firewall
FIREWALL
VERSA_FIREWALL
SYSLOG + KV
2025-12-10
View Change
Workspace Mobile Devices
Google Cloud Specific
WORKSPACE_MOBILE
JSON
2023-11-29
View Change
Avanan Email Security
Email Server
AVANAN_EMAIL
JSON
2025-11-17
View Change
FireEye HX Audit
Audits
FIREEYE_HX_AUDIT
XML
2022-11-04
View Change
Huawei Switches
Switches and Routers
HUAWEI_SWITCH
JSON+SYSLOG
2026-01-22
View Change
CSV Custom IOC
IOC
CSV_CUSTOM_IOC
CSV
2025-08-01
View Change
OSQuery
EDR
OSQUERY_EDR
SYSLOG + JSON
2024-05-01
View Change
Cisco Firepower NGFW
Firewall
CISCO_FIREPOWER_FIREWALL
SYSLOG + KV, SYSLOG + JSON, JSON, SYSLOG
2026-01-22
View Change
SAP SuccessFactors
Audit Log
SAP_SUCCESSFACTORS
CSV
2024-05-22
View Change
Sophos UTM
Unified Threat Management
SOPHOS_UTM
KV
2025-07-25
View Change
Open Policy Agent
NA
OPA
JSON
2025-01-16
View Change
Nozomi Networks Scada Guardian
Network Monitoring
NOZOMI_GUARDIAN
CEF and JSON, SYSLOG
2026-01-16
View Change
Zeek JSON
DNS
BRO_JSON
JSON
2024-05-01
View Change
Citrix Receiver
Application Server Logs
CSG_CITRIX_RX
CSV
2025-03-26
View Change
AWS Identity and Access Management (IAM)
AWS Specific
AWS_IAM
JSON
2023-12-14
View Change
Azure AD Sign-In
Misc Windows Specific
AZURE_AD_SIGNIN
JSON
2026-01-22
View Change
Avatier Password Management
SaaS Application
AVATIER
SYSLOG + KV
2021-08-05
GCP Abuse Events Logs
Google Cloud Specific
GCP_ABUSE_EVENTS
JSON
2025-08-27
View Change
ION Spectrum
Automation
ION_SPECTRUM
CSV
2025-10-10
View Change
Swimlane Platform
SOAR Tools
SWIMLANE
JSON
2025-02-19
View Change
IBM Security Verify Access
Security
IBM_SVA
Syslog
2025-08-29
View Change
Windows Event (XML)
AV / Endpoint
WINEVTLOG_XML
SYSLOG + XML, KV, SYSLOG + JSON, SYSLOG + CSV
2026-01-01
View Change
Symantec DLP
DLP
SYMANTEC_DLP
SYSLOG + KV (CEF), XML, CEF
2026-01-22
View Change
Elastic Search
Log Aggregator
ELASTIC_SEARCH
JSON
2023-11-02
View Change
AWS Inspector
AWS-specific log types
AWS_INSPECTOR
JSON, SYSLOG
2025-02-25
View Change
Akamai Cloud Monitor
Load Balancer, Traffic Shaper, ADC
AKAMAI_CLOUD_MONITOR
JSON
2026-01-16
View Change
Fivetran
SIEM Systems
FIVETRAN
JSON
2024-06-24
View Change
GCP_SWP
CLOUD
GCP_SWP
JSON
2024-04-15
View Change
SecureLink
Remote Access Tools
SECURELINK
SYSLOG
2025-04-02
View Change
Cequence Bot Defense
Log Aggregator
CEQUENCE_BOT_DEFENSE
JSON
2025-08-26
View Change
Fortra Powertech SIEM Agent
STATUS_UPDATE
FORTRA_POWERTECH_SIEM_AGENT
SYSLOG, CEF
2024-04-30
View Change
One Identity Identity Manager
unified identity security
ONE_IDENTITY_IDENTITY_MANAGER
kv , SYSLOG + JSON
2025-07-08
View Change
Apigee
Google Cloud Specific
GCP_APIGEE_X
JSON
2024-10-16
View Change
Red Hat Directory Server LDAP
Identity and Access Management
REDHAT_DIRECTORY_SERVER
JSON + SYSLOG + KV
2024-10-24
View Change
ExtraHop DNS
DNS
EXTRAHOP_DNS
JSON
2021-12-13
Nyansa Events
IoT
NYANSA_EVENTS
SYSLOG + KV
2023-03-01
View Change
Oracle Unified Directory
ORACLE OUD
ORACLE_OUD
SYSLOG
2023-09-11
View Change
Wallix Bastion
Privileged Account Activity
WALLIX_BASTION
SYSLOG, SYSLOG + KV
2025-04-10
View Change
Mikrotik Router
Router
MIKROTIK_ROUTER
SYSLOG + Grok
2025-09-09
View Change
Akamai DNS
DNS
AKAMAI_DNS
CSV, JSON
2024-11-25
View Change
IBM DS8000 Storage
Audit Logs
IBM_DS8000
Syslog, CSV
2024-07-24
View Change
Ubika WAAP
WAF
UBIKA_WAAP
SYSLOG
2024-06-03
View Change
Onfido
Authentication
ONFIDO
SYSLOG + JSON
2023-03-10
View Change
Datadog
NDR
DATADOG
JSON
2025-08-25
View Change
FireEye NX Audit
AUDIT
FIREEYE_NX_AUDIT
Syslog
2024-05-01
View Change
Dell ECS Enterprise Object Storage
ECS
DELL_ECS
SYSLOG
2026-01-12
View Change
Atlassian Cloud Admin Audit
Audit
ATLASSIAN_AUDIT
JSON
2025-01-09
View Change
Atlassian Confluence
Knowledge base
ATLASSIAN_CONFLUENCE
SYSLOG, JSON
2024-07-05
View Change
Cloudflare Audit
SaaS Application
CLOUDFLARE_AUDIT
JSON
2026-12-01
View Change
AWS VPC Flow
AWS Specific
AWS_VPC_FLOW
SYSLOG + JSON
2025-11-14
View Change
Symantec VIP Gateway
Email Server
SYMANTEC_VIP
SYSLOG
2023-03-03
View Change
Alcatel Switch
Privileged Account Activity
ALCATEL_SWITCH
SYSLOG
2024-03-11
View Change
Unbound DNS
DNS
UNBOUND_DNS
SYSLOG
2020-06-09
PingIdentity Directory Server Logs
Security
PING_DIRECTORY
SYSLOG + KV, JSON
2025-10-31
View Change
Proofpoint Sendmail Sentrion
Email server
PROOFPOINT_SENDMAIL_SENTRION
SYSLOG
2024-06-05
View Change
Spur data feeds
Vulnerability Management
SPUR_FEEDS
JSON
2024-05-10
View Change
Falco IDS
IDS/IPS
FALCO_IDS
JSON
2024-03-06
View Change
AWS Lambda Function
Web Proxy log types.
AWS_LAMBDA_FUNCTION
SYSLOG
2025-07-29
View Change
Chronicle SOAR Audit
SOAR
CHRONICLE_SOAR_AUDIT
JSON
2025-05-29
View Change
Cisco Router
Switches, Routers
CISCO_ROUTER
SYSLOG, SYSLOG+KV
2026-01-20
View Change
Apache Tomcat
Web server
TOMCAT
JSON
2025-02-07
View Change
Rippling Activity Logs
ACTIVITY_LOGS
RIPPLING_ACTIVITYLOGS
JSON
2024-08-01
View Change
Sentinelone Alerts
Endpoint Security
SENTINELONE_ALERT
JSON, CEF
2024-12-09
View Change
VeridiumID by Veridium
Authentication Software
VERIDIUM_ID
Syslog + KV
2024-06-19
View Change
Sonrai Enterprise Cloud Security Solution
Cloud Security Solution
SONRAI
JSON
2024-06-13
View Change
CoSoSys Protector
Endpoint Detection
ENDPOINT_PROTECTOR_DLP
SYSLOG + KV
2025-09-26
View Change
GitHub
SaaS Application
GITHUB
JSON,SYSLOG
2025-11-24
View Change
NetApp BlueXP
Security
NETAPP_BLUEXP
JSON
2024-10-23
View Change
Cloud Storage Context
Google Cloud Specific
N/A
JSON
2024-05-28
View Change
SecureAuth
SSO
SECUREAUTH_SSO
SYSLOG, XML
2025-07-24
View Change
Trend Micro AV
AV / Endpoint
TRENDMICRO_AV
SYSLOG + KV, CEF
2023-05-21
View Change
Cisco VPN
VPN
CISCO_VPN
SYSLOG
2025-03-13
View Change
JAMF Pro
Mac Endpoint Management System
JAMF_PRO
SYSLOG + KV, JSON
2025-10-20
View Change
Unix system
OS
NIX_SYSTEM
SYSLOG, JSON
2026-01-27
View Change
Onapsis
SAP
ONAPSIS
JSON , SYSLOG , KV
2025-11-25
View Change
Riverbed Steelhead
Network Management and Optimization
STEELHEAD
JSON , SYSLOG
2025-06-16
View Change
Trend Micro
SMS, UNITY_ONE
TIPPING_POINT
SYSLOG
2026-01-22
View Change
Active Countermeasures
Alert
AI_HUNTER
SYSLOG
2020-12-08
Kea DHCP
DHCP
KEA_DHCP
SYSLOG
2022-03-22
View Change
Cisco Unity Connection
Administration and Management
CISCO_UNITY_CONNECTION
SYSLOG + KV
2025-05-15
View Change
Supported log types without a default parser
Google Security Operations SIEM does not provide a default parser for these log types. You can ingest raw logs
from these devices using the Google Security Operations SIEM Ingestion API or the Google Security Operations SIEM forwarder.
Google Security Operations SIEM will not normalize the data to structured Unified Data Model format.
You can create a
custom parser
to normalize
these logs. You can also
search raw logs
.
Vendor / Product
Ingestion label
Absolute Secure Endpoint
ABSOLUTE_SECURE_ENDPOINT
Accenture Synthetic
ACCENTURE_SYNTHETIC
Accops Hysecure VPN
ACCOPS_HYSECURE_VPN
Acquia Cloud Platform
ACQUIA_CLOUD_PLATFORM
Acronis Backup
ACRONIS
Active Identity HID
ACTIVE_IDENTITY_HID
Microsoft ActiveSync
ACTIVE_SYNC
Adaptive Shield
ADAPTIVE_SHIELD
Adaxes
ADAXES
Addigy MDM
ADDIGY_MDM
Admin by request PAM
ADMIN_BY_REQUEST
Adobe Commerce
ADOBE_COMMERCE
Adobe Experience Manager
ADOBE_EXPERIENCE_MANAGER
Adobe I/O Runtime
ADOBE_IO_RUNTIME
ManageEngine ADSelfService Plus
ADSELFSERVICE_PLUS
ADTRAN NetVanta router
ADTRAN_NETVANTA
Adyen Platform
ADYEN
Agari Phishing Defense
AGARI_PHISHING_DEFENSE
Aikido
AIKIDO
Airbus Security Logging (ACD AISD)
AIRBUS_SECURITY_LOG
Extreme Networks AirDefense
AIRDEFENSE
Airwatch Context
AIRWATCH_CONTEXT
Air Table
AIR_TABLE
Akamai API Security
AKAMAI_API_SECURITY
Akamai Prolexic
AKAMAI_DDOS
Akamai DHCP
AKAMAI_DHCP
Akamai Enterprise Threat Protector
AKAMAI_ETP
Akamai Event Viewer
AKAMAI_EVT_VWR
Akamai Guardicore
AKAMAI_GUARDICORE
Akamai Kona Edge Grid
AKAMAI_KONA_EDGE_GRID
Akamai Log Delivery Service
AKAMAI_LDS
Akamai MFA
AKAMAI_MFA
AlertLogic Notifications
ALERTLOGIC_NOTIFICATIONS
Alert Enterprise Guardian
ALERT_GUARDIAN
AliCloud ActionTrail
ALICLOUD_ACTIONTRAIL
AliCloud Anti DDos
ALICLOUD_ANTI_DDOS
Alicloud ApsaraDB
ALICLOUD_APSARADB
AliCloud Firewall
ALICLOUD_FIREWALL
AliCloud WAF
ALICLOUD_WAF
AlienVault Open Threat Exchange
ALIENVAULT_OTX
Alkira IP Flow
ALKIRA_IP_FLOW
Allot NetEnforcer
ALLOT_NETENFORCER
Amavis
AMAVIS
Analyst1 IOC
ANALYST1_IOC
Anzenna
ANZENNA
Apache Kafka Audit
APACHE_KAFKA_AUDIT
Apache SpamAssassin
APACHE_SPAMASSASSIN
APC Automatic Transfer Switch
APC_ATS
APC Netbotz
APC_NETBOTZ
APC Power Distribution Unit
APC_PDU
APC Smart-UPS
APC_SMART_UPS
APC StruxureWare Portal
APC_STRUXUREWARE
Apiiro Cloud Application Security Platform
APIIRO
Appgate Software-defined Perimeter
APPGATE_SDP
Appsentinels
APPSENTINELS
AppSmith Audit
APPSMITH_AUDIT
AppViewX
APPVIEWX
Aptos Enterprise Order Management
APTOS_EOM
Arcon PAM
ARCON_PAM
Arctic Security Arctic Node
ARCTIC_NODE
Argo CD
ARGO_CD
Argo Workflows
ARGO_WORKFLOWS
Arista Guardian For Network Identity
ARISTA_AGNI
Arista CorvilNet DANZ Integration
ARISTA_CORVILNET
Arista CloudVision Portal
ARISTA_CVP
Arista Extensible Operating System
ARISTA_EOS
Arista NDR
ARISTA_NDR
Arize Cloud
ARIZE_CLOUD
Arkime Packet Capture
ARKIME_PCAP
Armis
ARMIS
Armorblox Email Security
ARMORBLOX_ESC
Armor Anywhere
ARMOR_ANYWHERE
Array Networks WAF
ARRAY_NETWORKS_WAF
Aruba Orchestrator
ARUBA_ORCHESTRATOR
Aruba Switches
ARUBA_SWT
Arxan Threat Analytics
ARXAN_THREAT_ANALYTICS
Asana
ASANA
Ascertia
ASCERTIA
Asimily
ASIMILY
AssetNote
ASSETNOTE
AstriX
ASTRIX
Atlan
ATLAN
Atlassian Beacon
ATLASSIAN_BEACON
Atlassian Jira Confluence Json
ATLASSIAN_CONFLUENCE_JSON
Atlassian Guard Detect
ATLASSIAN_GUARD_DETECT
Atlassian Jira Json
ATLASSIAN_JIRA_JSON
Attack IQ
ATTACK_IQ
AT&T Netbond
ATT_NETBOND
AudioCodes Voice DNA
AUDIOCODES
Authentic8 Silo
AUTHENTIC8_SILO
AuthMind
AUTHMIND
Authx Identity Management
AUTHX
Authx User Context
AUTHX_USER_CONTEXT
Autodesk Cad Cam
AUTODESK_CAD_CAM
Autodesk Vault
AUTODESK_VAULT
Automox
AUTOMOX_EPM
Avast Business
AVAST_HUB
Avaya Aura Session Manager
AVAYA_AURA_SESSION_MANAGER
Avaya Session Border Controller
AVAYA_BORDER
Avaya Interactive Voice Response
AVAYA_IVR
Avaya VSP Switch
AVAYA_VSP
Avaya Wireless
AVAYA_WIRELESS
Avaza
AVAZA
AvePoint EnPower
AVEPOINT_ENPOWER
Aviatrix Cloud Network Platform
AVIATRIX
Avigilon Alta Cloud Security
AVIGILON_ALTA_CLOUD_SECURITY
Avigilon Ava Security Camera
AVIGILON_AVA_SECURITY_CAMERA
AWS Dasha
AWS_DASHA
AWS Dynamo DB
AWS_DYNAMO_DB
AWS Elastic Kubernetes Service
AWS_EKS
Amazon ElastiCache
AWS_ELASTI_CACHE
Amazon FSx for Windows File Server
AWS_FSX
AWS Inspector2
AWS_INSPECTOR2
AWS NGINX
AWS_NGINX
AWS PY Tools
AWS_PY_TOOLS
AWS Simple Email Service
AWS_SES
AWS Shield
AWS_SHIELD
Axis Atmos
AXIS_ATMOS
Axis Camera
AXIS_CAMERA
Axis License Plate Reader
AXIS_LPR
Axis Security Audit
AXIS_OS
Axonius Cybersecurity Asset Management
AXONIUS
Axway
AXWAY
Microsoft Azure
AZURE
Azure AD Password Protection
AZURE_AD_PASSWORD_PROTECTION
Azure AD Provisioning
AZURE_AD_PROVISIONING
Azure App Configuration
AZURE_APPCONFIGURATION
Azure App Platform
AZURE_APPPLATFORM
Azure ArcData
AZURE_ARCDATA
Azure ATP
AZURE_ATP
Azure Authorization
AZURE_AUTHORIZATION
Azure Bastion
AZURE_BASTION
Azure Change Analysis
AZURE_CHANGEANALYSIS
Azure Compute
AZURE_COMPUTE
Azure Container Registry
AZURE_CONTAINER_REGISTRY
Azure DataFactory
AZURE_DATAFACTORY
Azure DNS logs
AZURE_DNS
Azure DocumentDB
AZURE_DOCUMENTDB
Azure Event Grid
AZURE_EVENTGRID
Azure Event Hub
AZURE_EVENTHUB
Azure Hybrid Compute
AZURE_HYBRIDCOMPUTE
Azure Log Analytics Workspace
AZURE_LOG_ANALYTICS_WORKSPACE
Azure Nix System
AZURE_NIX_SYSTEM
Azure Network Security Group Event
AZURE_NSG_EVENT
Azure Org Context
AZURE_ORG_CONTEXT
Azure PostgreSQL
AZURE_POSTGRESQL
Azure Recovery Services Vaults
AZURE_RECOVERY_SERVICES_VAULTS
Azure Risky Users
AZURE_RISKY_USERS
Azure Risk Events
AZURE_RISK_EVENTS
Azure Security Center
AZURE_SECURITY_CENTER
Azure Service Principal Logins
AZURE_SERVICE_PRINCIPAL_LOGINS
Azure Windows Virtual Desktop Connections Logs
AZURE_WVD_CONNECTIONS
Azure Windows Virtual Desktop Management Logs
AZURE_WVD_MANAGEMENT
Babelforce
BABELFORCE
Backbase Engagement Banking Platform
BACKBASE
Backbox
BACKBOX
Backstage
BACKSTAGE
OneIdentity Balabit
BALABIT
BambooHR
BAMBOO_HR
Banner dd
BANNER_DD
Barracuda CloudGen Access
BARRACUDA_CLOUDGEN_ACCESS
Barracuda Impersonation Protection
BARRACUDA_IMPERSONATION
Barracuda Incident Response
BARRACUDA_INCIDENTRESPONSE
Barracuda Load Balancer ADC
BARRACUDA_LOAD_BALANCER
Barracuda Content Shield
BARRACUDA_SHIELD
Belden Switch
BELDEN_SWITCH
Bettercloud
BETTERCLOUD
BetterStack Uptime
BETTERSTACK_UPTIME
BeyondTrust Cloud Privilege Broker
BEYONDTRUST_CPB
BeyondTrust Management console
BEYONDTRUST_MC
Beyond Identity
BEYOND_IDENTITY
BindPlane Audit Logs
BINDPLANE
Bitsight
BITSIGHT
Bitvise SFTP
BITVISE_SFTP
Bitvise SSHd
BITVISE_SSHD
Bitwarden Password Manager User Context
BITWARDEN_USER_CONTEXT
Biztalk
BIZTALK
Blackberry Workspaces
BLACKBERRY_WORKSPACES
BlinkOps
BLINKOPS
Blockdaemon API
BLOCKDAEMON_API
BloodHound
BLOODHOUND
Bluecat Address Manager
BLUECAT_AM
Bluecat Micetro IP Address Management
BLUECAT_MICETRO_IPAM
Blue Prism
BLUE_PRISM
Blue Voyant
BLUE_VOYANT
BMC Control-M
BMC_CONTROL_M
Boeing Onboard Network System Logging
BOEING_ONS
Core Privileged Access Manager (BoKS)
BOKS
Boomi App
BOOMI
Bricata NDR
BRICATA_NDR
Britive Audit API
BRITIVE_AUDIT_API
BRIVO
BRIVO
Broadcom Compliance Event Manager
BROADCOM_CEM
Broadcom Edge Secure Web Gateway
BROADCOM_EDGE_SWG
Brocade Fabric OS
BROCADE_FOS
Brocade SANnav Management Portal
BROCADE_SANNAV
Zeek DHCP
BRO_DHCP
Zeek HTTP
BRO_HTTP
BT IPControl
BT_IPCONTROL
Burpsuite Application Security testing tool
BURPSUITE
CallTower Audio Conferencing
CALLTOWER_AUDIO
Cameyo Activity Logs
CAMEYO_ACTIVITY_LOGS
Cameyo Bring Your Own Cloud
CAMEYO_BYO_CLOUD
Canary Audit Trail
CANARY_AUDIT_TRAIL
Canon Printers
CANON_PRINTERS
Canvas LMS
CANVAS_LMS
CATO SD-WAN
CATO_SDWAN
Celonis Audit Logs
CELONIS
Censornet CASB
CENSORNET_CASB
Cerberus FTP Server
CERBERUS_FTP
ChatGPT Audit Logs
CHATGPT_AUDIT_LOGS
Check Point CloudGuard
CHECKPOINT_CLOUDGUARD
Check Point Email
CHECKPOINT_EMAIL
Check Point FDE
CHECKPOINT_FDE
Checkpoint Gaia
CHECKPOINT_GAIA
Chopin PrePay Solutions
CHOPIN_PPS
Chronicle Feed
CHRONICLE_FEED
Cilium
CILIUM
Cisco Aironet
CISCO_AIRONET
Cisco Cyber Vision
CISCO_CYBER_VISION
Cisco DNS
CISCO_DNS
Cisco Firepower Threat Defense
CISCO_FIREPOWER_THREAT_DEFENSE
Cisco Meraki Camera
CISCO_MERAKI_CAMERA
Cisco NetFlow
CISCO_NETFLOW
Cisco Remote Access VPN
CISCO_RAVPN
Cisco Secure Access Zero Trust Access Flow
CISCO_SECURE_ACCESS_FLOW
Cisco Secure Email Threat Defense
CISCO_SECURE_EMAIL_THREAT_DEFENSE
Cisco Secure Endpoint
CISCO_SECURE_ENDPOINT
Cisco Secure Malware Analytics
CISCO_SECURE_MALWARE_ANALYTICS
Cisco Security Cloud Control
CISCO_SECURITY_CLOUD_CONTROL
Cisco Content Security Management Appliance
CISCO_SMA
Cisco SNMP Trapd
CISCO_SNMP
Cisco StarOS
CISCO_STAR_OS
Cisco Umbrella Firewall
CISCO_UMBRELLA_FIREWALL
Cisco Umbrella IPS
CISCO_UMBRELLA_IPS
Cisco Viptela
CISCO_VIPTELA
Cisco Vulnerability Management
CISCO_VULNERABILITY_MANAGEMENT
CiscoXDR
CISCO_XDR
Citadel Identity360
CITADEL_IDENTITY360
Citrix Netscaler Web Logs
CITRIX_NETSCALER_WEB_LOGS
Citrix SD-WAN
CITRIX_SDWAN
Citrix Session Metadata
CITRIX_SESSION_METADATA
Citrix Virtual Desktop Infrastructure
CITRIX_VDI
Citrix WAF
CITRIX_WAF
Citrix Web Gateway
CITRIX_WEB_GATEWAY
Citrix Workspace
CITRIX_WORKSPACE
Citrix XenCenter
CITRIX_XENCENTER
Claroty xDome Secure Access
CLAROTY_XDOME_SECURE_ACCESS
Clavistier Firewall
CLAVISTER_FIREWALL
Cleafy
CLEAFY
Clear Bank Portal Audit
CLEARBANK_PORTAL
Clearsense Healthcare Analytics
CLEARSENSE
ClickHouse
CLICKHOUSE
Click Studios Passwordstate
CLICK_STUDIOS_PASSWORDSTATE
Cloudaware
CLOUDAWARE
CloudBees
CLOUDBEES
CloudBolt
CLOUDBOLT
Cloudera Ranger
CLOUDERA_RANGER
Cloudflare Access
CLOUDFLARE_ACCESS
Cloudflare Bot Management
CLOUDFLARE_BOT_MANAGEMENT
CloudFlare CASB Findings
CLOUDFLARE_CASB_FINDINGS
Cloudflare Device posture results
CLOUDFLARE_DEVICE_POSTURE_RESULTS
Cloudflare DLP Forensic Copies
CLOUDFLARE_DLP_FORENSIC_COPIES
Cloudflare DNS Firewall Logs
CLOUDFLARE_DNS_FIREWALL_LOGS
Cloudflare DNS logs
CLOUDFLARE_DNS_LOGS
CloudFlare Email Security Alerts
CLOUDFLARE_EMAIL_SECURITY_ALERTS
Cloudflare Firewall Events
CLOUDFLARE_FIREWALL_EVENTS
Cloudflare Gateway DNS
CLOUDFLARE_GATEWAY_DNS
Cloudflare Gateway HTTP
CLOUDFLARE_GATEWAY_HTTP
Cloudflare Gateway Network
CLOUDFLARE_GATEWAY_NETWORK
Cloudflare HTTP requests
CLOUDFLARE_HTTP_REQUESTS
Cloudflare Magic IDS Detections
CLOUDFLARE_MAGIC_IDS_DETECTIONS
Cloudflare NEL reports
CLOUDFLARE_NEL_REPORTS
Cloudflare Sinkhole HTTP Logs
CLOUDFLARE_SINKHOLE_HTTP_LOGS
Cloudflare Spectrum
CLOUDFLARE_SPECTRUM
Cloudflare SSH Logs
CLOUDFLARE_SSH_LOGS
Cloudflare Workers Trace Events
CLOUDFLARE_WORKERS_TRACE_EVENTS
Cloudflare Zero Trust Network Session
CLOUDFLARE_ZERO_TRUST_NETWORK_SESSION
Cloud Passage (CSM)
CLOUDPASSAGE_CSM
Cloud Passage (FIM)
CLOUDPASSAGE_FIM
Cloud Passage (LIDS)
CLOUDPASSAGE_LIDS
Cloud Passage (SVM)
CLOUDPASSAGE_SVM
Cloudsek Alerts
CLOUDSEK_ALERTS
CloudWave Honeypot
CLOUDWAVE_HONEYPOT
cmd.com
CMD
Coalition Control API
COALITION
Cockroach DB
COCKROACH_DB
Coda Io
CODA_IO
Code42 CrashPlan
CODE42
Code Worldwide
CODE_WORLDWIDE
Cofense Vision
COFENSE_VISION
Cohesity Helios
COHESITY_HELIOS
Cohesity Smartfiles
COHESITY_SMARTFILES
ColorTokens
COLORTOKENS
Commvault Metallic
COMMVAULT_METALLIC
Conductor One
CONDUCTOR_ONE
Confluent Audit
CONFLUENT_AUDIT
ConnectWise Automate
CONNECTWISE_AUTOMATE
ConnectWise Control
CONNECTWISE_CONTROL
Contrast Security
CONTRAST_SECURITY
Control D DNS
CONTROL_D
Control Plane
CONTROL_PLANE
Control UP
CONTROL_UP
Conversational Agents and Dialogflow
CONVERSATIONAL_AGENT
Corero SmartWall One
CORERO_SMARTWALL_ONE
CoreView Audit-log SIEM integration
COREVIEW
Corrata
CORRATA
Pico Corvilnet Engine
CORVILNET_ENGINE
Cradlepoint Router Logs
CRADLEPOINT
Cradlepoint NetCloud
CRADLEPOINT_NETCLOUD
Cribl AppScope
CRIBL_APPSCOPE
Cribl Cloud
CRIBL_CLOUD
Cribl Edge
CRIBL_EDGE
Cribl Search
CRIBL_SEARCH
CrowdStrike DLP
CROWDSTRIKE_DLP
CrowdStrike Falcon Shield
CROWDSTRIKE_FALCON_SHIELD
Crowdstrike Recon (TI)
CROWDSTRIKE_RECON
Crowdstrike Spotlight
CROWDSTRIKE_SPOTLIGHT
ProLion CryptoSpike
CRYPTOSPIKE
CSG Custom Rules Engine
CSG_CUSTOMENGINE
CSG Singleview
CSG_SINGLEVIEW
CSV Custom CMDB
CSV_CUSTOM_CMDB
CrowdStrike Falcon CEF
CS_CEF_EDR
Crowdstrike Endpoint Security API
CS_ENDPOINT_SECURITY_API
CTERA Drive
CTERA_DRIVE
Cyware Threat Intelligence Exchange
CTIX
Cubist Audit
CUBIST_AUDIT
Culture AI
CULTURE_AI
Customer Alerts
CUSTOMER_ALERT
Custom CSV Log
CUSTOM_CSV_LOG
Custom Host Forensics
CUSTOM_HOST_FORENSICS
Cyberark Identity
CYBERARK_IDENTITY
Cyberark Identity Audit
CYBERARK_IDENTITY_AUDIT
CyberArk Secure Cloud Access
CYBERARK_SCA
CyberArk Identity Single Sign-On
CYBERARK_SSO
Connectsecure
CYBERCNS
Cyberhaven Data Detection and Response
CYBERHAVEN_DDR
Cyberhaven
CYBERHAVEN_EVENTS
Cyberint
CYBERINT
Cybersixgill
CYBERSIXGILL
Cycode Platform
CYCODE
CyCognito ASM
CYCOGNITO_ASM
Insider threat detection and response
CYDERES_INSIDER
Cyderes IOC
CYDERES_IOC
Cylance
CYLANCE
Cylera IOT
CYLERA_IOT
Cymulate
CYMULATE
Cynerio Healthcare NDR
CYNERIO_NDR_H
Cyolo Zero Trust
CYOLO_ZTNA
Cyral
CYRAL
Cytracom Control One
CYTRACOM_CONTROL_ONE
C Zentrix
C_ZENTRIX
D3 Security
D3_SECURITY
Databricks
DATABRICKS
Datadog Application Security Management
DATADOG_ASM
Dataiku DSS Logging
DATAIKU_DSS_LOGS
DataLocker SafeConsole
DATALOCKER_SAFECONSOLE
Datalust
DATALUST
Datasunrise Dam
DATASUNRISE_DAM
Datawatch
DATAWATCH
DBT Cloud
DBT_CLOUD
DealCloud
DEAL_CLOUD
Deepfence Network Monitoring
DEEPFENCE
DefectDojo
DEFECTDOJO
Delinea PBA
DELINEA_PBA
Delinea Privilege Manager
DELINEA_PRIVILEGE_MANAGER
Delinea Server Suite
DELINEA_SERVER_SUITE
Dell Compellent
DELL_COMPELLENT
Dell Cyber Recovery Manager
DELL_CRM
Dell EMC Avamar
DELL_EMC_AVAMAR
Dell EMC Cloudlink
DELL_EMC_CLOUDLINK
Dell Core Switch
DELL_EMC_NETWORKING
Dell EMC Unity
DELL_EMC_UNITY
Dell EMC UnityVSA
DELL_EMC_UNITY_VSA
Dell VxRail
DELL_VXRAIL
Dell SonicWALL WAF
DELL_WAF
Design Profit Central Server
DESIGN_PROFIT_CENTRAL_SERVER
Device 42
DEVICE_42
Devolutions Remote Desktop Manager
DEVOLUTIONS_RDM
Divvy Cloud
DIVVY_CLOUD
DLink Switch
DLINK_SWITCH
Dmarcian
DMARCIAN
Docker
DOCKER
Docker Hub Activity
DOCKER_HUB_ACTIVITY
DocuSign
DOCUSIGN
DOMO Business Cloud
DOMO
Doppel
DOPPEL
Dragos
DRAGOS
Draytek Firewall
DRAYTEK
Draytek Router
DRAYTEK_ROUTER
Dremio Data Lakehouse
DREMIO_DATA_LAKEHOUSE
Dropbox
DROPBOX
Drupal Logging
DRUPAL
Druva
DRUVA
DSP Toolkit audit
DSP_AUDIT
Dtex Audit
DTEX_AUDIT
Dtex Intercept
DTEX_INTERCEPT
Cisco Duo Authentication Proxy
DUO_AUTH_PROXY
Duo Access Gateway
DUO_CASB
Duo Network Gateway
DUO_NETWORK_GATEWAY
Duo Trust Monitor
DUO_TRUST_MONITOR
Dynatrace
DYNATRACE
E2 Guardian
E2_GUARDIAN
CWT SatoTravel
E2_SOLUTIONS
Easy NAC
EASY_NAC
Eaton UPS
EATON_UPS
eCAR
ECAR
eCAR Bro
ECAR_BRO
Edgecore Networks
EDGECORE_NETWORKS
Edgio CDN
EDGIO_CDN
Edgio Rate Limiting
EDGIO_RL
Efax
EFAX
Egnyte
EGNYTE
Egress Defend
EGRESS_DEFEND
Egress Prevent
EGRESS_PREVENT
EclecticIQ EDR
EIQ_EDR
Elastic Security
ELASTIC_EDR
Elastic File Beats
ELASTIC_FILEBEAT
Elastic Metric Beats
ELASTIC_METRICBEAT
Emerson Smart Firewall
EMERSON_FIREWALL
Emsisoft AntiVirus
EMSISOFT_ANTIVIRUS
Endgame
ENDGAME_EDR
Ensono Cloud Mainframe Solution
ENSONO
Entrust NTP Server
ENTRUST_NTP_SERVER
Entrust Secrets Vault
ENTRUST_SECRETS_VAULT
Entrust DataControl Audit
ENTR_DATACTRL_AUDIT
Erlang Shell Logs
ERLANG_SHELL
Ermes Web Protection
ERMES
Ermetic
ERMETIC
Eset Protect Platform
ESET_PROTECT_PLATFORM
E-Share platform
ESHARE_PLATFORM
Estar
ESTAR
ETQ Reliance
ETQ_RELIANCE
Evidos Firewall
EVIDOS_FIREWALL
Exabeam Fusion XDR
EXABEAM_FUSION_XDR
Exim Internet Mailer
EXIM_INTERNET_MAILER
Express NodeJS
EXPRESS_NODEJS
Exterro FTK Central
EXTERRO_FTK_CENTRAL
ExtraHop DHCP
EXTRAHOP_DHCP
ExtremeWare Operating System (OS)
EXTREMEWARE_NETWORKS
xtreme Networks ExtremeControl NAC Solution
EXTREME_CONTROL
Extreme Management Center
EXTREME_MANAGEMENT
EzProxy
EZPROXY
F5 Bot
F5_BOT
F5 Distributed Cloud WAF
F5_DCS_WAF
F5 IP Intelligence
F5_IP_INTELLIGENCE
F5 System Logs
F5_SYSTEM_LOGS
Fail2Ban Scan
FAIL2BAN
FairXchange Horizon
FAIRXCHANGE_HORIZON
Farsight DNSDB
FARSIGHT_DNSDB
FA Solutions
FA_SOLUTIONS
Featurespace Aric
FEATURESPACE_ARIC
Feenics Access Control
FEENICS_ACCESS_CONTROL
Fidelis Endpoint
FIDELIS_ENDPOINT
Figma Developers
FIGMA
FileMage SFTP
FILEMAGE_SFTP
Files dot com
FILES_DOT_COM
Firebase
FIREBASE
Fireblocks
FIREBLOCKS
FireEye CMS
FIREEYE_CMS
FireEye Helix
FIREEYE_HELIX
FireMon Firewall
FIREMON_FIREWALL
Fisglobal Quantum
FISGLOBAL_QUANTUM
Flashpoint IOC
FLASHPOINT_IOC
Fleet DM
FLEET_DM
FM Systems Workplace Management
FM_SYSTEMS
Forcepoint Insider Threat
FORCEPOINT_FIT
Forcepoint One
FORCEPOINT_ONE
Forcepoint V Series
FORCEPOINT_VSERIES
Fortanix Data Security Manager
FORTANIX_DSM
Fortinet ADC
FORTINET_ADC
Fortinet Wireless Access Point
FORTINET_AP
Fortinet FortiDeceptor
FORTINET_FORTIDECEPTOR
Fortinet FortiDLP
FORTINET_FORTIDLP
Fortinet Network Detection and Response
FORTINET_FORTINDR
Fortinet FortiSASE
FORTINET_FORTISASE
Fortinet FortiGate IPS
FORTINET_IPS
Fortra Vulnerability Management
FORTRA_VM
Foundry Fastiron
FOUNDRY_FASTIRON
FoxPass Audit Logs
FOXPASS_AUDIT_LOGS
Fox-IT
FOX_IT_STIX
FreeIPA
FREEIPA
FreeRADIUS
FREERADIUS
Front
FRONT
Digital Defense Frontline VM
FRONTLINE_VM
FS-ISAC IOC
FS_ISAC_IOC
Fusion Auth
FUSION_AUTH
Futurex HSM
FUTUREX_HSM
GCP Artifact Registry
GCP_ARTIFACT_REGISTRY
GCP Cloud Asset Inventory
GCP_CLOUD_ASSET_INVENTORY
GCP Identity Toolkit
GCP_IDENTITYTOOLKIT
GCP Google Kubernetes Container Security
GCP_KUBERNETES_CONTAINER_SECURITY
GCP Threat Detection
GCP_THREAT_DETECTION
Gemini Code Assist
GEMINI_CODE_ASSIST
Gene6 FTP Server
GENE6_FTP
Genea Access Control
GENEA_ACCESS_CONTROL
Genesys Audit
GENESYS_AUDIT
Genetec Audit
GENETEC_AUDIT
Genetec Synergis
GENETEC_SYNERGIS
Genian NAC
GENIAN_NAC
Ghangor DLP
GHANGOR_DLP
Gigamon
GIGAMON
Gigya CIAM
GIGYA_CIAM
Github Events
GITHUB_EVENTS
Glean
GLEAN
Globalscape SFTP
GLOBALSCAPE_SFTP
GlusterFS
GLUSTER_FS
GluWare Network Automation
GLUWARE_NETWORK_AUTOMATION
GL TRADE
GL_TRADE
GMV Checker User Context
GMV_CHECKER_CONTEXT
GoAnywhere MFT
GOANYWHERE_MFT
GoDaddy DNS
GODADDY_DNS
GoldiLock
GOLDILOCK
Gong
GONG
Google Ads
GOOGLE_ADS
Grafana
GRAFANA
GrayhatWarfare
GRAYHATWARFARE
Graylog Operations
GRAYLOG
GreatHorn Email Security
GREATHORN
Greenhouse Harvest
GREENHOUSE_HARVEST
GreyNoise
GREYNOISE
Guidewire Billing Center
GUIDEWIRE_BILLING_CENTER
Guidewire Claim Center
GUIDEWIRE_CLAIM_CENTER
Guidewire Policy Center
GUIDEWIRE_POLICY_CENTER
Gurucul Risk Analytics
GURUCUL
H3C Router
H3C_ROUTER
Halo
HALO
Halo Sensor
HALO_SENSOR
HaProxy LoadBalancer
HAPROXY_LOADBALANCER
Harbor
HARBOR
Harfanglab EDR
HARFANGLAB_EDR
Hashcast
HASHCAST
Hashicorp Boundary
HASHICORP_BOUNDARY
Hashicorp Nomad
HASHICORP_NOMAD
HAVI Connect
HAVI_CONNECT
Perforce Helix Core
HELIX_CORE
Heroku
HEROKU
Hex
HEX
HiBob
HIBOB
HaveIBeenPwned
HIBP
Hillstone NDR
HILLSTONE_NDR
Hirschmann Switch
HIRSCHMANN_SWITCH
Hitachi PAM
HITACHI_ID_PAM
HL7
HL7
Honeywell Cyber Insights
HONEYWELL_CYBERINSIGHTS
HoopDev
HOOPDEV
Hornet Email Security
HORNET_SECURITY
Hoxhunt
HOXHUNT
HPE Alletra
HPE_ALLETRA
Hewlett Packard Enterprise SAN
HPE_SAN
HP Inc MFP
HP_INC_MFP
HPE Oneview
HP_ONEVIEW
HP Poly
HP_POLY
HP Printer logs
HP_PRINTER
HP Router
HP_ROUTER
HP Tandem
HP_TANDEM
HP Wolf Pro Security
HP_WOLF
Huawei Campus Switch
HUAWEI_CAMPUS_SWITCH
Huawei CloudEngine
HUAWEI_CLOUDENGINE
Huawei Cloud Trace Service Audit
HUAWEI_CTS_AUDIT
Huawei NextGen Firewall
HUAWEI_FIREWALL
Huawei Fusion Sphere Hypervisor
HUAWEI_FUSIONSPHERE
Huawei NAC
HUAWEI_NAC
Huawei SecMaster
HUAWEI_SECMASTER
Huawei Versatile Routing Platform
HUAWEI_VRP
Huawei Wireless
HUAWEI_WIRELESS
HubSpot Activity Logs
HUBSPOT_ACTIVITY
HubSpot CRM Platform
HUBSPOT_CRM
HubSpot Authentication Logs
HUBSPOT_LOGIN
Human Security
HUMAN_SECURITY
Health ISAC
H_ISAC
3Com 8800 Series Switch
IBM_3COM
IBM Cleversafe Object Storage
IBM_CLEVERSAFE
IBM Cloud System
IBM_CLOUD_SYSTEM
IBM Cognos Analytics
IBM_COGNOS
IBM Copy Services Manager
IBM_CSM
IBM ILO
IBM_ILO
IBM Security Guardium Insights
IBM_INSIGHTS
IBM KNS
IBM_KNS
IBM MQ File Transfer
IBM_MQ_FILE_TRANSFER
IBM NS1
IBM_NS1
IBM Planning Analytics
IBM_PA
IBM Sense
IBM_SENSE
IBM Spectrum Protect
IBM_SPECTRUM_PROTECT
IBM Switch
IBM_SWITCH
IBM Tririga
IBM_TRIRIGA
IBM WinCollect
IBM_WINCOLLECT
Idecsi
IDECSI
Identity Security Cloud
IDENTITY_SECURITY_CLOUD
Dell iDRAC
IDRAC
IIJ_LanScope
IIJ_LANSCOPE
ImageNow
IMAGENOW
iManage Cloud Platform
IMANAGE_CLOUD
iManage Threat Manager
IMANAGE_THREAT_MANAGER
Imperva Cloud WAF
IMPERVA_CLOUD_WAF
Imperva Data Risk Analytics
IMPERVA_DATA_ANALYTICS
Imperva Sonar
IMPERVA_SONAR
Imprivata Confirm ID
IMPRIVATA_CONFIRM_ID
Imprivata Identity Governance
IMPRIVATA_IDG
Imprivata OneSign
IMPRIVATA_ONESIGN
IM Express
IM_EXPRESS
Incident Io
INCIDENT_IO
Indefend DLP
INDEFEND_DLP
Indusface WAF
INDUSFACE_WAF
INFINICO NetWyvern Series Appliance
INFINICO_NETWYVERN
Infinidat
INFINIDAT
Infisical
INFISICAL
Infoblox Loadbalancer
INFOBLOX_LOADBALANCER
Infoblox NetMRI
INFOBLOX_NETMRI
Informatica
INFORMATICA
Informatica Powercenter
INFORMATICA_POWERCENTER
INKY Secure Email
INKY
Intezer
INTEZER
Intruder.IO
INTRUDER_IO
Invicti
INVICTI
inWebo MFA
INWEBO_MFA
IPFire
IPFIRE
Ipswitch MOVEit Automation
IPSWITCH_MOVEIT_AUTOMATION
Ironclad
IRONCLAD
Ironscales
IRONSCALES
iSecurity | Security Services and Remediation
ISECURITY
Isonline ISL Light
ISL_LIGHT
Itential Pronghorn
ITENTIAL_PRONGHORN
iTop
ITOP
Ivanti Application Control
IVANTI_APP_CONTROL
Ivanti Connect Secure
IVANTI_CONNECT_SECURE
Ivanti Device Control
IVANTI_DEVICE_CONTROL
Ivanti Endpoint Manager Mobile
IVANTI_ENDPOINT_MANAGER_MOBILE
ISM Xtraction
IVANTI_XTRACTION
iverify
IVERIFY
Jamf Compliance Reporter
JAMF_COMPLIANCE_REPORTER
Jamf Connect
JAMF_CONNECT
Jamf Protect Network Traffic
JAMF_NETWORK_TRAFFIC
Jamf Pro MDM
JAMF_PRO_MDM
JBoss Web
JBOSS_WEB
IBM JDE
JDE
JiranSecurity MailScreen
JIRANSECURITY_MAILSCREEN
Jit
JIT
Joblogic
JOBLOGIC
JSCAPE SFTP
JSCAPE_SFTP
JumpCloud Directory as a Service
JUMPCLOUD_DAAS
JumpCloud Desktop
JUMPCLOUD_DESKTOP
Jumpcloud IAM
JUMPCLOUD_IAM
Juniper Edge
JUNIPER_EDGE
Juniper SSR Conductor
JUNIPER_SSR_CONDUCTOR
Juniper Secure Connect VPN
JUNIPER_VPN
Jupiter One
JUPITER_ONE
KACE Service Desk
KACE_SERVICE_DESK
KACE Systems Management Appliance
KACE_SMA
Kamailio
KAMAILIO
Kandji
KANDJI
Kandji Context
KANDJI_CONTEXT
Kaseya IT Management
KASEYA
Kaspersky for Microsoft Office 365
KASPERSKY_O365_EVENTS
Keepalived Routing software
KEEPALIVED
Kentik DDoS Detection
KENTIK_ALERTS
Keyfactor
KEYFACTOR
Keysight Packet Brokers
KEYSIGHT
Kibana audit logs
KIBANA
Kion
KION
KnowBe4 Audit Log
KNOWBE4
Kodem Security
KODEM_SECURITY
Kustomer CRM
KUSTOMER_CRM
Kyverno
KYVERNO
LangSmith Audit
LANGSMITH_AUDIT
Lansweeper Asset Management
LANSWEEPER
LaunchDarkly
LAUNCH_DARKLY
LayerX
LAYERX
LOAD_BALANCER_ADC
LB_ADC
LeanIX Enterprise
LEANIX
Leanix CMDB
LEANIX_CMDB
Lenels2 Elements Secure
LENELS2_ELEMENTS_SECURE
Lepide
LEPIDE
Lexmark Printer logs
LEXMARK_PRINTER
Liaison NuBridges Platform
LIAISON_NUBRIDGES
Libraesva Email Security
LIBRAESVA_EMAIL
LinOTP
LIN_OTP
Lira
LIRA
Lockself Lockpass
LOCKSELF_LOCKPASS
Apache LOG4J Java Application Log
LOG4J
LogicGate
LOGICGATE
Logic Monitor
LOGICMONITOR
LookingGlass Aenoik IDPS
LOOKINGGLASS_IPS
Looking Glass
LOOKING_GLASS_IOC
LSI Badge Management System
LSI_BMS
Lumen DDoS Hyper
LUMEN_DDOS_HYPER
Lumeta Spectre
LUMETA
Lumos
LUMOS
Lumu Universal SIEM
LUMU
Lenovo XClarity Orchestrator
LXC_ORCHESTRATOR
MacStadium
MACSTADIUM
Magento Cloud
MAGENTO_CLOUD
Magic Collaboration Studio
MAGIC_CS
MailScanner
MAILSCANNER
Maltiverse IOC
MALTIVERSE_IOC
Mambu
MAMBU
Manage Engine Endpoint
MANAGEENGINE_ENDPOINT
ManageEngine NCM
MANAGEENGINE_NCM
ManageEngine Remote Access Plus
MANAGEENGINE_RAP
ManageEngine Asset Explorer
MANAGE_ENGINE_ASSET_EXPLR
ManageEngine Endpoint Central
MANAGE_ENGINE_ENDPT_CNTRL
ManageEngine OpUtils
MANAGE_ENGINE_OPUTILS
ManageEngine PAM360
MANAGE_ENGINE_PAM360
ManageEngine Password Manager Pro
MANAGE_ENGINE_PASSWORD_MANAGER
Mandiant Attack Surface Management Entity
MANDIANT_ASM_ENTITY
Mandiant Attack Surface Management Discovered Issue
MANDIANT_ASM_ISSUE
Mandiant Attack Surface Management Technology
MANDIANT_ASM_TECHNOLOGY
Mandiant Digital Threat Monitoring
MANDIANT_DTM_ALERTS
Mango Apps
MANGOAPPS
Manhattan Warehouse Management System
MANHATTAN_WMS
Material Security
MATERIAL_SECURITY
Matrix Frontier Badge Management
MATRIX_FRONTIER
Mandiant Advantage Security Validation
MA_SV
McAfee Application Control
MCAFEE_APP_CONTROL
McAfee Advanced Threat Defense
MCAFEE_ATD
McAfee MVISION EDR
MCAFEE_EDR
McAfee Network Security Platform
MCAFEE_NSP
McAfee Solid Core
MCAFEE_SOLID_CORE
Medigate CMDB
MEDIGATE_CMDB
Melissa
MELISSA
Mellanox Switch
MELLANOX_SWITCH
Mend IO
MEND_IO
Metaswitch Perimeta
METASWITCH_PERIMETA
Meta Marketing
META_MARKETING
Miasma SecretScanner
MIASMA_SECRETSCANNER
MicroSemi NTP
MICROSEMI_NTP
Microsoft Ads
MICROSOFT_ADS
Microsoft CASB Files & Entities
MICROSOFT_CASB_CONTEXT
Microsoft Azure Databricks
MICROSOFT_DATABRICKS_WORKSPACES
Microsoft Defender for Cloud Apps
MICROSOFT_DEFENDER_CLOUD_APPS
Microsoft Dotnet Log Files
MICROSOFT_DOTNET
Microsoft Defender External Attack Surface Management
MICROSOFT_EASM
Microsoft Entra ID Protection
MICROSOFT_ENTRA_ID_PROTECTION
Microsoft Graph Incident
MICROSOFT_GRAPH_INCIDENT
Microsoft Graph Risky Users
MICROSOFT_GRAPH_RISKY_USERS
Microsoft Identity Protection
MICROSOFT_IDENTITY_PROTECTION
Microsoft Insights/Components
MICROSOFT_INSIGHTS_COMPONENTS
Power BI Activity Log
MICROSOFT_POWERBI_ACTIVITY_LOG
Microsoft Purview
MICROSOFT_PURVIEW
Microsoft Azure AD Risk Detections
MICROSOFT_RISK_DETECTIONS
Microsoft Security Actions
MICROSOFT_SECURITY_ACTIONS
Microsoft Security Advisories Alerts
MICROSOFT_SECURITY_ALERTS
Microsoft ServiceBus/Namespaces
MICROSOFT_SERVICEBUS_NAMESPACES
Microsoft Azure SQL Managed Instances
MICROSOFT_SQL_MANAGED_INSTANCES
Microsoft SSTP VPN
MICROSOFT_SSTP
Microsoft Threat Indicators
MICROSOFT_THREAT_INDICATORS
Mimecast Attachment Logs
MIMECAST_ATTACHMENT_LOGS
Mimecast Audit Logs
MIMECAST_AUDIT_LOGS
Mimecast DLP Logs
MIMECAST_DLP_LOGS
Mimecast impersonation Logs
MIMECAST_IMPERSONATION_LOGS
Mimecast Web Security
MIMECAST_WEBPROXY
Minerva AV
MINERVA_AV
Minsait Sigefi
MINSAIT_SIGEFI
Miro
MIRO
Miro Cloud
MIRO_CLOUD
Mirth OnPrem Appliances NextGen
MIRTH_NEXTGEN
Mitel Communications Director
MITEL_MCD
Mode Analytics
MODE_ANALYTICS
ModSecurity
MODSECURITY
Monday
MONDAY
Mongo Atlas Audit
MONGO_ATLAS_AUDIT
Mosyle
MOSYLE
Moveworks
MOVEWORKS
Microsoft Entra Recommendations
MS_ENTRA_RECOMMENDATIONS
Windows Performance Monitor
MS_PERFMON
Mulesoft
MULESOFT
Multicom Switch
MULTICOM_SWITCH
MultiPay
MULTIPAY
NCC Scout Suite
NCC_SCOUTSUITE
NCR Digital Insight FSG
NCR_DIGITAL_INSIGHT_FSG
NCR Digital Insight Global Logging
NCR_DIGITAL_INSIGHT_GL
Nessus
NESSUS
Nessus Network Monitor
NESSUS_NETWORK_MONITOR
NetApp ONTAP Audit
NETAPP_ONTAP_AUDIT
NetBrain
NETBRAIN
NetDisco
NETDISCO
Netenrich Entity Behaviour
NETENRICH_ENTITY_BEHAVIOR
Netenrich Entity Context
NETENRICH_ENTITY_CONTEXT
Netgate Firewall
NETGATE_FIREWALL
Netgear Switch
NETGEAR_SWITCH
Netlify Log Drains
NETLIFY_LOGDRAINS
Netmotion
NETMOTION
Netography Fusion
NETOGRAPHY_FUSION
Netscout Arbor Threat Mitigation System
NETSCOUT_TMS
Netskope One Secure SD-WAN
NETSKOPE_SDWAN
Netsurion ProtectWise
NETSURION_PROTECTWISE
Network Box Unified Threat Management+
NETWORKBOX_UTM
Netwrix Activity Monitor
NETWRIX_ACTIVITY_MONITOR
Netwrix Privilege Secure
NETWRIX_PRIVILEGE_SECURE
Netwrix Stealth Intercept
NETWRIX_STEALTH_INTERCEPT
Netwrix Threat Manager
NETWRIX_THREAT_MANAGER
Neustar SiteProtect
NEUSTAR_SITEPROTECT
NeuVector SUSE
NEUVECTOR
New Relic Platform
NEW_RELIC
Nextcloud Hub
NEXTCLOUD_HUB
Nextthink Finder
NEXTTHINK_FINDER
Ne Silent Log
NE_SILENT_LOG
Nightfall DLP
NIGHTFALL
Ninja One
NINJAONE
NIST National Vulnerability Database
NIST_NVD
NNT File Integrity monitoring
NNT_FIM
Nokia Home Device Manager
NOKIA_HDM
NordLayer VPN
NORD_LAYER
Nortel Secure Router
NORTEL_SR
Nortel Contivity VPN Switch
NORTEL_SWITCH
Notion
NOTION
Novidea Insurance Management System
NOVIDEA_CLAIM_HISTORY
NSFOCUS Next Generation Intrusion Prevention System
NSFOCUS_NGIPS
Nucleus Vulnerability Scan Delta
NUCLEUS_VULNERABILITY_DELTA
Nutanix Frame
NUTANIX_FRAME
Nxlog Agent
NXLOG_AGENT
Nxlog Fim
NXLOG_FIM
N-Able N-Central RMM
N_ABLE_N_CENTRAL_RMM
Oracle Cloud Infrastructure API Gateway
OCI_APIGATEWAY
Oracle Cloud Infrastructure Network Firewall
OCI_FIREWALL
Oracle Cloud Infrastructure Identity Cloud Service
OCI_IDENTITY_CLOUD_SERVICE
Okta RADIUS
OKTA_RADIUS
Okta Workflows
OKTA_WORKFLOWS
OnBase CMS
ONBASE_CMS
One Identity Active Role Service
ONEIDENTITY_ARS
One Identity Change Auditor
ONEIDENTITY_CHANGE_AUDITOR
One Identity Defender
ONEIDENTITY_DEFENDER
OneIdentity Safeguard
ONEIDENTITY_SAFEGUARD
1KOSMOS | Identity and Authentication
ONEKOSMOS
OneLogin User Context
ONELOGIN_USER_CONTEXT
OneTrust
ONETRUST
Oomnitza
OOMNITZA
Open CTI Platform
OPENCTI
Openpath Context
OPENPATH_CONTEXT
Opentelemetry
OPENTELEMETRY
OpenText Cordy
OPENTEXT_CORDY
Opentext Exstream
OPENTEXT_EXSTREAM
OpenText Fax2Mail
OPENTEXT_FAX2MAIL
IDnomic Public Key Infrastructure
OPENTRUST
OpenVAS
OPENVAS
OpsRamp
OPSRAMP
Opswat Kiosk
OPSWAT_KIOSK
Opus Codec
OPUS
Oracle Access Manager
ORACLE_AM
Oracle Audit Vault Database Firewall
ORACLE_AVDF
Oracle CPQ
ORACLE_CPQ
Oracle EBS
ORACLE_EBS
Oracle Exadata Database Machine
ORACLE_EXADATA
Oracle HCM Human resources platform solution
ORACLE_HCM
Oracle Enterprise Manager
ORACLE_OEM
Oracle SSO Audit Logging
ORACLE_SSO_AUDIT
Oracle Zero Data Loss Recovery Appliance
ORACLE_ZDLRA
Oscar Claims
OSCAR_CLAIMS
Open Source Intelligence
OSINT_IOC
Osirium PAM
OSIRIUM_PAM
Outline Activity Logs
OUTLINE_ACTIVITY_LOGS
Outpost24
OUTPOST24
OVHcloud
OVHCLOUD
OX Security
OX_SECURITY
Packetlight Dwdm
PACKETLIGHT_DWDM
Packet Viper
PACKET_VIPER
PACOM Systems
PACOM_SYSTEMS
PAGELY
PAGELY
PagerDuty
PAGERDUTY
Pagerduty Audit
PAGERDUTY_AUDIT
Panorays
PANORAYS
Palo Alto Cortex IIS
PAN_CORTEX_XDR_IIS
Palo Alto DNS Security
PAN_DNS_SECURITY
Palo Alto Networks Global Protect
PAN_GLOBAL_PROTECT
Palo Alto Global Protect SVC
PAN_GPSVC
Palo Alto Networks Prisma Access
PAN_PRISMA_ACCESS
Palo Alto Prisma Cloud Workload Protection
PAN_PRISMA_CWP
Palo Alto Prisma Dig Cloud DSPM
PAN_PRISMA_DIG_CLOUD_DSPM
Palo Alto SSLVPN Access
PAN_SSLVPN_ACCESS
Palo Alto Telemetry
PAN_TELEMETRY
Palo Alto Cortex XDR Management Audit
PAN_XDR_MGMT_AUDIT
Palo Alto Networks XSOAR Audit
PAN_XSOAR
PaperCut Printing Management System
PAPER_CUT
Passfort
PASSFORT
Pathlock Identity Security Platform
PATHLOCK
Pave
PAVE
Paxton Access Control Systems
PAXTON_ACS
SSL pcap
PCAP_SSL_CLIENT_HELLO
Pega Automation
PEGA
Penta Security Wapples
PENTA_WAPPLES
Pentera
PENTERA
Pentera ASV
PENTERA_ASV
Pentera Leef
PENTERA_LEEF
PeopleSoft
PEOPLESOFT
People Strong
PEOPLE_STRONG
Peplink Loadbalancer
PEPLINK_LOADBALANCER
Peplink Router
PEPLINK_ROUTER
Peplink Switch
PEPLINK_SWITCH
Perception Point XRay
PERCEPTION_POINT_XRAY
Perimeter 81
PERIMETER_81
Perplexity
PERPLEXITY
PhishAlarm
PHISHALARM
Domain Tools Phisheye
PHISHEYE_ALERT
Phosphorus
PHOSPHORUS
Pingcap TIDB
PINGCAP_TIDB
Pingdom
PINGDOM
PingOne Advanced Identity Cloud
PINGONE_AIC
PingOne Protect
PINGONE_PROTECT
Pingsafe
PINGSAFE
Ping Access
PING_ACCESS
Ping SDK
PING_SDK
Plaso Super Timeline
PLASO
Pleasant Password Server
PLEASANT_PASSWORD_SERVER
Plixer Scrutinizer
PLIXER_SCRUTINIZER
Pomerium
POMERIUM
Portnox Audit
PORTNOX_AUDIT
MS PowerShell Transcript
POWERSHELL_TRANSCRIPT
Power DNS
POWER_DNS
Preveil Enterprise
PREVEIL_ENTERPRISE
Prismatic IO
PRISMATIC_IO
Prisma SD-WAN
PRISMA_SD_WAN
Procore
PROCORE
Prompt Security
PROMPT_SECURITY
ProofID
PROOFID
Proofpoint DLP
PROOFPOINT_DLP
ProofPoint Email Protection
PROOFPOINT_EMAIL_PROTECTION
Proofpoint Endpoint Data Loss Prevention
PROOFPOINT_ENDPOINT_DLP
Proofpoint Identity Threat Platform
PROOFPOINT_IDENTITY_THREAT_PLATFORM
Proofpoint Meta
PROOFPOINT_META
Proofpoint Secure Share
PROOFPOINT_SECURE_SHARE
Proofpoint Security Awareness Training
PROOFPOINT_SECURITY_AWARENESS_TRAINING
Proofpoint Tap Campaign
PROOFPOINT_TAP_CAMPAIGN
Proofpoint Tap People
PROOFPOINT_TAP_PEOPLE
Proofpoint Tis IOC
PROOFPOINT_TIS_IOC
Protegrity Defiance
PROTEGRITY_DEFIANCE
Provision Asset Context
PROVISION_ASSET_CONTEXT
Honeywell Pro-Watch
PROWATCH
ProxMax
PROXMAX
Proxmox
PROXMOX
PRTG Network Monitor
PRTG_NETWORKMONITOR
Puppet
PUPPET
Push Security
PUSH_SECURITY
QLIK Audit
QLIK_AUDIT
Qualtrics Audit
QUALTRICS_AUDIT
Qualys User Activity
QUALYS_ACTIVITY
Qualys Knowledgebase
QUALYS_KNOWLEDGEBASE
Quest CA Audit
QUEST_CA_AUDIT
Rabbit MQ
RABBITMQ
Radiantone
RADIANTONE
RadiFlow IDS
RADIFLOW_IDS
RSA RADIUS
RADIUS
Radware Cloud WAF Service Access
RADWARE_ACCESS
Radware Bot
RADWARE_BOT
Radware DDoS Protection
RADWARE_DDOS
RAD ETX
RAD_ETX
Rancher API Audit Log
RANCHER_API_AUDIT_LOG
Ransomcare
RANSOMCARE
Rapid7 Cloud Security
RAPID7_CLOUDSEC
Rapid7 Insights Threat Command
RAPID7_INSIGHTS_THREAT_COMMAND
Rapid7 Security Onion
RAPID7_SECURITY_ONION
Rapid Identity
RAPID_IDENTITY
Raritan Dominion SX II
RARITAN_DOMINION
Raven DB
RAVEN_DB
RealiteQ
REALITEQ
Reblaze Web Application Firewall
REBLAZE_WAF
Recordedfuture Alerts
RECORDEDFUTURE_ALERTS
Red Canary Cloud Protection
REDCANARY_CLOUD_PROTECTION_RAW
Red Hat Identity Management
REDHAT_IM
Redhat Jboss
REDHAT_JBOSS
Red Hat Keycloak
REDHAT_KEYCLOAK
RedHat Satellite Server
REDHAT_SATELLITE
RedHat StackRox
REDHAT_STACKROX
Redis
REDIS
Redmine
REDMINE
RedSift BrandTrust
REDSIFT_BRANDTRUST
Red Access Browsing Security
RED_ACCESS
Relativity
RELATIVITY
ReliaQuest
RELIAQUEST
Research and Education Networks Information Sharing and Analysis Center
REN_ISAC
Reserved LogType1
RESERVED_LOG_TYPE_1
Reserved LogType10
RESERVED_LOG_TYPE_10
Reserved LogType11
RESERVED_LOG_TYPE_11
Reserved LogType12
RESERVED_LOG_TYPE_12
Reserved LogType13
RESERVED_LOG_TYPE_13
Reserved LogType14
RESERVED_LOG_TYPE_14
Reserved LogType15
RESERVED_LOG_TYPE_15
Reserved LogType16
RESERVED_LOG_TYPE_16
Reserved LogType17
RESERVED_LOG_TYPE_17
Reserved LogType18
RESERVED_LOG_TYPE_18
Reserved LogType19
RESERVED_LOG_TYPE_19
Reserved LogType20
RESERVED_LOG_TYPE_20
Reserved LogType21
RESERVED_LOG_TYPE_21
Reserved LogType22
RESERVED_LOG_TYPE_22
Reserved LogType23
RESERVED_LOG_TYPE_23
Reserved LogType24
RESERVED_LOG_TYPE_24
Reserved LogType25
RESERVED_LOG_TYPE_25
Reserved LogType26
RESERVED_LOG_TYPE_26
Reserved LogType27
RESERVED_LOG_TYPE_27
Reserved LogType28
RESERVED_LOG_TYPE_28
Reserved LogType29
RESERVED_LOG_TYPE_29
Reserved LogType3
RESERVED_LOG_TYPE_3
Reserved LogType30
RESERVED_LOG_TYPE_30
Reserved LogType31
RESERVED_LOG_TYPE_31
Reserved LogType32
RESERVED_LOG_TYPE_32
Reserved LogType33
RESERVED_LOG_TYPE_33
Reserved LogType34
RESERVED_LOG_TYPE_34
Reserved LogType35
RESERVED_LOG_TYPE_35
Reserved LogType36
RESERVED_LOG_TYPE_36
Reserved LogType37
RESERVED_LOG_TYPE_37
Reserved LogType38
RESERVED_LOG_TYPE_38
Reserved LogType39
RESERVED_LOG_TYPE_39
Reserved LogType4
RESERVED_LOG_TYPE_4
Reserved LogType40
RESERVED_LOG_TYPE_40
Reserved LogType41
RESERVED_LOG_TYPE_41
Reserved LogType42
RESERVED_LOG_TYPE_42
Reserved LogType43
RESERVED_LOG_TYPE_43
Reserved LogType44
RESERVED_LOG_TYPE_44
Reserved LogType45
RESERVED_LOG_TYPE_45
Reserved LogType46
RESERVED_LOG_TYPE_46
Reserved LogType47
RESERVED_LOG_TYPE_47
Reserved LogType48
RESERVED_LOG_TYPE_48
Reserved LogType49
RESERVED_LOG_TYPE_49
Reserved LogType5
RESERVED_LOG_TYPE_5
Reserved LogType50
RESERVED_LOG_TYPE_50
Reserved LogType6
RESERVED_LOG_TYPE_6
Reserved LogType7
RESERVED_LOG_TYPE_7
Reserved LogType8
RESERVED_LOG_TYPE_8
Reserved LogType9
RESERVED_LOG_TYPE_9
Retool
RETOOL
Ribbon Session Border Controller
RIBBON_SBC
Ring Central
RING_CENTRAL
RiskIQ Digital Footprint
RISKIQ_DIGITAL_FOOTPRINT
Risk Resecurity
RISK_RESECURITY
Riverbed
RIVERBED
Rublon
RUBLON
Rubrik Security Cloud
RUBRIK_SECURITY_CLOUD
Rumble Network Discovery
RUMBLE_NETWORK_DISCOVERY
S2W Quaxar
S2W_QUAXAR
SafeBreach
SAFEBREACH
SafeConnect NAC
SAFECONNECT_NAC
SafeNet Network HSM
SAFENET_HSM
Salesforce Context
SALESFORCE_CONTEXT
Salesforce Marketing Cloud Audit
SALESFORCE_MARKETING_CLOUD_AUDIT
Salesforce Shield
SALESFORCE_SHIELD
Sangfor IAG
SANGFOR_IAG
Sangfor Network Detection and Response
SANGFOR_NDR
Saporo
SAPORO
SAP Business Warehouse
SAP_BW
SAP Cloud for Customer
SAP_C4C
SAP Change Document
SAP_CHANGE_DOCUMENT
SAP ERP
SAP_ERP
SAP Enterprise Threat Detection
SAP_ETD
SAP Gateway
SAP_GATEWAY
SAP Commerce Cloud
SAP_HAC
SAP HANA
SAP_HANA
SAP Hana Audit
SAP_HANA_AUDIT
SAP IAS Context
SAP_IAS_CONTEXT
SAP Identity Management
SAP_IDM
SAP Insurance
SAP_INSURANCE
SAP Leasing
SAP_LEASING
SAS Institute
SAS_INSTITUTE
SAS Metadata Server log
SAS_METADATA_SERVER_LOG
Saturn Cloud
SATURN_CLOUD
Savvy Security
SAVVY_SECURITY
ScaleFusion for Windows MDM
SCALEFUSION
Scale Computing
SCALE_COMPUTING
Scality Ring Audit
SCALITY_RING_AUDIT
Microsoft System Center Configuration Manager
SCCM
Scylla
SCYLLA
Secberus Cloud Security Governance
SECBERUS
Sectigo SCM
SECTIGO_SCM
Securden
SECURDEN
SecurEnvoy SecurAccess
SECURENVOY_MFA
Securesoft Sniper IPS
SECURESOFT_SNIPER_IPS
Fiserv SecureNow
SECURE_NOW
SecurityBridge Dev
SECURITYBRIDGE_DEV
SecurityScorecard Platform
SECURITYSCORECARD
SecurityBridge
SECURITY_BRIDGE
Sekoia Ioc
SEKOIA_IOC
Schweitzer Engineering Laboratories Port Server
SEL_PORT_SERVER
Semperis ADFR
SEMPERIS_ADFR
Sendgrid Api
SENDGRID
Sendsafely
SENDSAFELY
Senhasegura PAM
SENHASEGURA_PAM
CloudWaves Sensato Nightingale Honeypot
SENSATO_HONEYPOT
Senseon Alerts
SENSEON_ALERTS
SensorFu Beacon
SENSORFU_BEACON
Sentra Data Loss Prevention
SENTRA_DLP
Sentrigo
SENTRIGO
Serpico
SERPICO
Servertech PDUs
SERVERTECH_PDUS
ServiceNow Node
SERVICENOW_NODE
ServiceNow Outbound HTTP
SERVICENOW_OUTBOUNDHTTP
ServiceNow Roles
SERVICENOW_ROLES
ServiceNow System log
SERVICENOW_SYSLOG
ServiceNow Transaction
SERVICENOW_TRANSACTION
Seti S4
SETI_S4
Sevco Security CMDB
SEVCO_CMDB
Sharefile Logs
SHAREFILE_LOGS
Sharepoint Unified Logging Service (ULS)
SHAREPOINT_ULS
Shield IoT
SHIELD_IOT
shodan.io
SHODAN_IO
Siebel Monitoring
SIEBEL
Siemens Simatic S7 PLC SNMP
SIEMENS_S7_PLC_SNMP
Siemens Simatic S7 PLC SYSLOG
SIEMENS_S7_PLC_SYSLOG
Siemens SiPass
SIEMENS_SIPASS
Siga Level Zero OT Resilience
SIGA
Silver Peak Firewall
SILVERPEAK_FIREWALL
Single Store
SINGLE_STORE
Site24x7
SITE24X7
SKYSEA Client View
SKYSEA
Slack API
SLACK_API
Smartsheet User Context
SMARTSHEET_USER_CONTEXT
Smart Simple
SMART_SIMPLE
Snapattack
SNAPATTACK
Winevtlog Snare
SNARE_WINEVTLOG
Snowflake Access
SNOWFLAKE_ACCESS
Snowplow
SNOWPLOW
Socomec UPS
SOCOMEC_UPS
SOCRadar Incidents
SOCRADAR_INCIDENTS
SoftEther VPN
SOFTETHER_VPN
Software House Access Control
SOFTWARE_HOUSE_ACS
Software House Ccure9000
SOFTWARE_HOUSE_CCURE9000
Solace PubSub Cloud
SOLACE_AUDIT
SolarWinds Network Performance Monitor
SOLARWINDS_NPM
SolarWinds Serv-U
SOLARWINDS_SERV_U
Solar System
SOLAR_SYSTEM
SolidServer
SOLIDSERVER
SonarQube
SONARQUBE
Sonatype Lifecycle
SONATYPE_LIFECYCLE
Sonic Switch
SONIC_SWITCH
Sophos Email Appliance
SOPHOS_EMAIL
Sophos URL filtering
SOPHOS_URL
Spacelift
SPACELIFT
Spamhaus
SPAMHAUS
Symantec Protection Engine
SPE
SpecterX
SPECTERX
Spirion
SPIRION
Splashtop Remote Access and Support software
SPLASHTOP
Splunk DNS
SPLUNK_DNS
Splunk Phantom
SPLUNK_PHANTOM
Splunk Intel Management
SPLUNK_TRUSTAR
Sprinkledata(DWH)
SPRINKLEDATA_DWH
Stairwell Inception
STAIRWELL_INCEPTION
Statusgator
STATUSGATOR
Stealthbits DLP
STEALTHBITS_DLP
Stellar Cyber
STELLAR_CYBER
Sterling Order Management System Data
STERLING_OMS_DATA
Strata Maverics Identity Orchestration Platform
STRATA_MAVERICKS
Stream Alert
STREAMALERT
Stripe Payments
STRIPE
Strivacity
STRIVACITY
StrongDM
STRONGDM
Supermicro IPMI
SUPERMICRO_IPMI
Superna Eyeglass
SUPERNA_EYEGLASS
SureView Systems Activity
SUREVIEW_SYSTEMS
Suridata
SURIDATA
Swift
SWIFT
Symantec Data Center Security
SYMANTEC_DCS
Symphony Summit AI
SYMPHONYAI
Syncplify SFTP 2 Events
SYNCPLIFY_SFTP
Syxsense
SYXSENSE
Tanium Deploy
TANIUM_DEPLOY
Tanium TanOS
TANIUM_TANOS
TeamT5 ThreatSonar EDR
TEAMT5_THREATSONAR_EDR
TeamViewer Tensor
TEAMVIEWER_TENSOR
Technitium DNS
TECHNITIUM_DNS
Tehtris EDR
TEHTRIS_EDR
Temenos Journey Manager System Event Publisher
TEMENOS_MANAGER_SYSTEMEVENT
Tenable Web App Scanning
TENABLE_WAS
Tencent CloudAudit
TENCENT_CLOUD_AUDIT
Tencent Cloud Firewall
TENCENT_CLOUD_FIREWALL
Tencent Cloud Waf
TENCENT_CLOUD_WAF
Tencent Cloud Workload Protection
TENCENT_CLOUD_WORKLOAD_PROTECTION
Teqtivity Assets
TEQTIVITY_ASSETS
Teradata Access
TERADATA_ACCESS
Teradata Aster
TERADATA_ASTER
Teradici PCoIP
TERADICI_PCOIP
Teramind
TERAMIND
Tessian Cloud Email Security Platform
TESSIAN_PLATFORM
TGDetect
TGDETECT
Thales payShield 10K HSM
THALES_PS10K_HSM
ThousandEyes
THOUSAND_EYES
ThreatQuotient
THREATQ_IOC
Thycotic devops secret vault
THYCOTIC_DEVOPS_SECRETVAULT
Tiktok for Developers
TIKTOK
Titan MFT
TITAN_MFT
Titan SFTP Server
TITAN_SFTP
Torq Audit Logs
TORQ_AUDIT_LOGS
TP Link Network Switches
TPLINK_SWITCH
Traceable API Security
TRACEABLE_PLATFORM
Traefik Labs
TRAEFIK
Transmit BindID
TRANSMIT_BINDID
Transmit Security FlexID
TRANSMIT_FLEXID
Transmit Security Mosaic CIAM
TRANSMIT_MOSAIC_CIAM
Transmit Security Mosaic Fraud Prevention
TRANSMIT_MOSAIC_FRAUD_PREVENTION
Transmit Security Mosaic Identity Verification
TRANSMIT_MOSAIC_IDENTITY_VERIFICATION
Transmit Security Mosaic Management
TRANSMIT_MOSAIC_MANAGEMENT
FIS Trax Payment Factory
TRAX
Trellix Malware Analysis
TRELLIX_AX
Trellix EX
TRELLIX_EX
Trend Micro Cloud App Security
TRENDMICRO_CLOUDAPPSECURITY
TrendMicro Cloud Email Gateway Protection
TRENDMICRO_CLOUD_EMAIL_GATEWAY_PROTECTION
Trend Micro EdgeIPS
TRENDMICRO_EDGEIPS
TrendMicro EDR
TRENDMICRO_EDR
Trend Micro Server Protect
TRENDMICRO_SERVER_PROTECT
TrendMicro Webproxy DSM
TRENDMICRO_WEBPROXY_DSM
Trend Micro TippingPoint Security Management System
TREND_MICRO_TIPPING_POINT
Tridium Niagara Framework
TRIDIUM_NIAGARA_FRAMEWORK
Tripp Lite
TRIPP_LITE
Tripwire Security Configuration Management
TRIPWIRE_SCM
TrueFort Platform
TRUEFORT
TrueNAS
TRUENAS
E-Motional Transparent Screen Lock TSL RFID
TSL_PRO
TT D365
TT_D365
TT MSAN DSLAM
TT_MSAN_DSLAM
TT Trio Chordiant
TT_TRIO_CHORDIANT
Tufin
TUFIN
Tufin Secure Track
TUFIN_SECURE_TRACK
Twilio Audit
TWILIO_AUDIT
Twilio Authy
TWILIO_AUTHY
Tyk IO
TYK_IO
Ubiquiti Accesspoint
UBIQUITI_ACCESSPOINT
Ubiquiti UDM Firewall
UBIQUITI_FIREWALL
UDM
UDM
Uipath
UIPATH
Everfox ULTRA
ULTRA
UltraDNS
ULTRADNS
Ultra Electronics CyberFence
ULTRA_CYBERFENCE
Unifi Router
UNIFI_ROUTER
Unifi Switch
UNIFI_SWITCH
Unifi System
UNIFI_SYSTEM
Unit 21
UNIT21
Uptivity
UPTIVITY
Upwind
UPWIND
USBAV Koramis
USBAV_KORAMIS
Valence Security
VALENCE
Valimail
VALIMAIL
Vanguard Active Alerts
VANGUARD
Vanta Context
VANTA_CONTEXT
Varnish Cache
VARNISH_CACHE
Vector Dev
VECTOR_DEV
Vectra AI
VECTRA_AI
Vectra Protect
VECTRA_PROTECT
Velociraptor - digital forensic & incident response tool
VELOCIRAPTOR
VMware VeloCloud SD-WAN
VELOCLOUD_SDWAN
Venafi
VENAFI
Vercara
VERCARA
Veriato Cerebral
VERIATO_CEREBRAL
Verizon Network Detection and Response
VERIZON_NDR
Verkada
VERKADA
Vertica Audit
VERTICA_AUDIT
Vertiv UPS
VERTIV_UPS
Very Good Security
VERY_GOOD_SECURITY
Veza Access Control Platform
VEZA
ViaControl Server Application
VIACONTROL
Vicarious VRX Events
VICARIUS_VRX_EVENTS
Virsec Event Logs
VIRSEC_EVENT
Virsec Attack and Threat Logs
VIRSEC_THREAT
Virtual Browser
VIRTUAL_BROWSER
Virtual Network Flow Logs
VIRTUAL_NETWORK_FLOW_LOGS
VirusTotal Threat Hunter
VIRUSTOTAL_THREAT_HUNTER
VMRay Analyzer
VMRAY_FLOG_XML
VMware Aria Logs
VMWARE_ARIA_LOGS
VMware Avi Vantage Platform
VMWARE_AVI_VANTAGE
VMware Cloud Director
VMWARE_CD
VMware HCX
VMWARE_HCX
VMware NSX AVI
VMWARE_NSX_AVI
VMware SDDC
VMWARE_SDDC
VMware SDWN Events
VMWARE_SDWN_EVENTS
VMware Unified Access Gateway
VMWARE_UNIFIED_ACCESS_GATEWAY
VMware vShield
VMWARE_VSHIELD
Vonage
VONAGE
VSFTPD Audit
VSFTPD_AUDIT
Wallarm Webhook Notifications
WALLARM_NOTIFICATIONS
Wallix Endpoint Privilege Management
WALLIX_EPM
Wallix Privileged Access Management
WALLIX_PAM
Waterfall Data Security Manager
WATERFALL_DSM
WebEx
WEBEX_SAAS
Web Methods Api Gateway
WEBMETHODS_API_GATEWAY
Webroot Endpoint Protection
WEBROOT
Webroot Identity Protection
WEBROOT_IDENTITY_PROTECTION
White Cloud
WHITECLOUD_EDR
WideField
WIDEFIELD_SECURITY
Windows Bindplane
WINDOWS_BINDPLANE
Windows NTP
WINDOWS_NTP
Windows Filtering Platform
WINDOWS_WFP
Winget Autoupdate
WINGET_AUTOUPDATE
Wing Security
WING_SECURITY
WireGuard VPN Logs
WIREGUARD_VPN
WithSecure Cloud Protection
WITHSECURE_CLOUD
WithSecure Elements Connector
WITHSECURE_ELEMENTS
Witness AI Control
WITNESS_AI_CONTROL
Wiz Audit
WIZ_AUDIT
Wiz Runtime Execution Data
WIZ_RUNTIME_EXECUTION_DATA
Wolters Kluwer Teammate
WOLTERS_KLUWER_TEAMMATE
Wordpress Simple History
WORDPRESS_SIMPLE_HISTORY
Workato Audit Logs
WORKATO
WorkDay User Sign In
WORKDAY_USER_SIGNIN
Workiva Wdesk
WORKIVA_WDESK
Workspot Control
WORKSPOT_CONTROL
WPass
WPASS
WP Engine
WP_ENGINE
WSO2 IS AM
WSO2_IS_AM
WS Ftp
WS_FTP
Western Telematic Inc Console Servers
WTI_CONSOLE_SERVERS
XDR.Net Digital Twin
XDRNET_DIGITALTWIN
Xirrus Wireless Controller
XIRRUS
XL Release
XLR
XM Cyber
XM_CYBER
Ysoft Data Security Manager
YSOFT_DSM
Konica Minolta YSoft SafeQ
YSOFT_SAFEQ
Yugabyte Database
YUGABYTE_DATABASE
Zabbix
ZABBIX
Zendesk Advanced Data Privacy and Protection
ZENDESK_ADPP
Zimbra Mail
ZIMBRA_MAIL
Zoho Assist
ZOHO_ASSIST
Zoho Analytics Audits
ZOHO_AUDIT
ZoomInfo
ZOOMINFO
Zoom Activity Logs
ZOOM_ACTIVITY
Zscaler Digital Experience
ZSCALER_DIGITAL_EXPERIENCE
Zscaler Email DLP
ZSCALER_EMAIL_DLP
Zscaler Email DLP Insights
ZSCALER_EMAIL_DLP_INSIGHTS
ZScaler NSS VM
ZSCALER_NSS_VM
Zscaler Sandbox
ZSCALER_SANDBOX
Zscaler Client Connector
ZSCALER_ZCC
Zscaler ZDX
ZSCALER_ZDX
Zuora App Logs
ZUORA_APP_LOGS
