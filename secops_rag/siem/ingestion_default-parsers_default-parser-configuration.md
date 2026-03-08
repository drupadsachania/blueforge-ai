# Default parser configuration and ingestion

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration/  
**Scraped:** 2026-03-05T09:16:46.760732Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Default parser configuration and ingestion
Default parsers are prebuilt configurations that ingest logs from various 
  sources and convert them into Unified Data Model (UDM) events. This page provides a list of default 
  parser documents. Each document includes detailed instructions on how to 
  configure data sources and ensure proper ingestion and processing of logs. While the documents describe the 
  validated configurations for each log source, alternative ingestion paths or configurations might also work.
This document only lists parsers that have corresponding documentation. For a complete list of all supported
parsers, see
Supported default parsers
.
Premium Parsers
Collect Apigee logs
Collect AWS CloudTrail logs
Collect AWS EC2 Hosts logs
Collect AWS EC2 Instance logs
Collect Chrome management logs
Collect Cisco ASA firewall logs
Collect Cloud SQL context logs
Collect Resource Manager context logs
Collect CrowdStrike Falcon logs
Collect Duo Activity logs
Collect Fluentd logs
Collect Fortinet Firewall logs
Collect Google Cloud BigQuery context logs
Collect Google Cloud Abuse Events logs
Collect Google Cloud Audit Logs
Collect Cloud DNS logs
Collect Google Cloud Firewall logs
Collect Google Cloud Kubernetes Context logs
Collect Google Cloud Load Balancing logs
Collect Google Cloud IAM context logs
Collect Google Cloud NAT logs
Collect Google Cloud Run functions context logs
Collect Google Workspace logs
Jamf parsers overview
Collect Jamf Protect logs
Collect Jamf Protect Telemetry v2 logs
Collect Jamf Telemetry logs
Collect Jamf Threat Events logs
Collect Google Kubernetes Engine (GKE) logs
Collect Cloud SQL logs
Collect Microsoft 365 logs
Collect Microsoft Defender for Endpoint logs
Collect Microsoft Graph API alerts logs
Collect Microsoft Windows AD logs
Collect Microsoft Windows DHCP logs
Collect Microsoft Windows DNS logs
Collect Microsoft Windows Sysmon logs
Collect Microsoft Windows Event logs
Collect Network Connectivity Center context logs
Collect NIX System logs
Collect OCSF logs
Collect OSSEC logs
Collect osquery logs
Collect Palo Alto Networks firewall logs
Collect Security Command Center findings
Collect SentinelOne Alert logs
Collect SentinelOne Cloud Funnel logs
Collect Splunk CIM logs
Zscaler parsers overview
Collect Zscaler CASB logs
Collect Zscaler Deception logs
Collect Zscaler DLP logs
Collect Zscaler DNS logs
Collect Zscaler Firewall logs
Collect Zscaler Internet Access logs
Collect Zscaler Tunnel logs
Collect Zscaler VPN logs
Collect Zscaler web proxy logs
Collect Zscaler ZPA logs
Collect Zscaler ZPA Audit logs
Collect Zeek (Bro) logs
Standard Parsers
Collect A10 Network Load Balancer logs
Collect Abnormal Security logs
Collect Absolute Secure Endpoint logs
Collect Acalvio logs
Collect Active Countermeasures AI-Hunter logs
Collect ADVA Fiber Service Platform logs
Collect AIDE (Advanced Intrusion Detection Environment) logs
Collect AIX system logs
Collect Akamai Cloud Monitor logs
Collect Akamai DataStream 2 logs
Collect Akamai DNS logs
Collect Akamai Enterprise Application Access logs
Collect Akamai SIEM Connector logs
Collect Akamai WAF logs
Collect Akeyless Vault logs
Collect Alcatel switch logs
Collect AlphaSOC alert logs
Collect AlgoSec Security Management logs
Collect Amazon CloudFront logs
Collect AMD Pensando DSS firewall logs
Collect Anomali ThreatStream IOC logs
Collect Ansible AWX logs
Collect Apache logs
Collect Apache Cassandra logs
Collect Apache Hadoop logs
Collect Apache Tomcat logs
Collect Appian Cloud logs
Collect Apple macOS syslog data
Collect Aqua Security logs
Collect Arbor Edge Defense logs
Collect Archer IRM logs
Collect ArcSight CEF logs
Collect Arista switch logs
Collect Armis Vulnerabilities logs
Collect Array Networks SSL VPN logs
Collect Aruba ClearPass logs
Collect Aruba EdgeConnect SD-WAN logs
Collect Aruba IPS logs
Collect Aruba switch logs
Collect Aruba Wireless Controller and Access Point logs
Collect Atlassian Bitbucket logs
Collect Atlassian Cloud Admin Audit logs
Collect Atlassian Confluence logs
Collect Atlassian Jira logs
Collect Attivo Networks BOTsink logs
Collect Auth0 logs
Collect Automation Anywhere logs
Collect Avatier logs
Collect Avaya Aura logs
Collect Avigilon Access Control Manager logs
Collect Aware audit logs
Collect AWS API Gateway access logs
Collect AWS Aurora logs
Collect AWS CloudWatch logs
Collect AWS Config logs
Collect AWS Control Tower logs
Collect AWS Elastic Load Balancing logs
Collect AWS Elastic MapReduce logs
Collect AWS GuardDuty logs
Collect AWS IAM logs
Collect AWS Key Management Service logs
Collect AWS Macie logs
Collect AWS Network Firewall logs
Collect AWS RDS logs
Collect AWS Route 53 logs
Collect AWS S3 server access logs
Collect AWS Security Hub logs
Collect AWS Session Manager logs
Collect AWS VPC flow logs
Collect AWS VPC Transit Gateway flow logs
Collect AWS VPN logs
Collect AWS WAF logs
Collect Azion firewall logs
Collect Azure AD Sign-In logs
Collect Azure API Management logs
Collect Azure APP Service logs
Collect Azure Application Gateway logs
Collect Azure Firewall logs
Collect Azure NSG Flow logs
Collect Azure Storage Audit logs
Collect Azure VPN logs
Collect Azure WAF logs
Collect Barracuda CloudGen Firewall logs
Collect Barracuda Email Security Gateway logs
Collect Barracuda WAF logs
Collect Barracuda Web Filter logs
Collect BeyondTrust BeyondInsight logs
Collect BeyondTrust EPM logs
Collect BeyondTrust Privileged Identity logs
Collect BeyondTrust Remote Support logs
Collect BeyondTrust Secure Remote Access logs
Collect Big Switch BigCloudFabric logs
Collect Bitdefender logs
Collect Bitwarden Enterprise event logs
Collect BloxOne Threat Defense logs
Collect BlueCat DDI logs
Collect BlueCat Edge logs
Collect Blue Coat ProxySG logs
Collect BMC AMI Defender logs
Collect BMC Helix Discovery logs
Collect Box Collaboration JSON logs
Collect Broadcom CA PAM logs
Collect Broadcom SSL VA logs
Collect Broadcom Support Portal Audit logs
Collect Broadcom Symantec SiteMinder Web Access logs
Collect Brocade ServerIron logs
Collect Brocade switch logs
Collect CA ACF2 logs
Collect CA LDAP logs
Collect Cambium Networks logs
Collect Carbon Black App Control logs
Collect Carbon Black EDR logs
Collect Cato Networks logs
Collect Censys logs
Collect Check Point Audit logs
Collect Check Point EDR logs
Collect Check Point firewall logs
Collect Check Point Harmony logs
Collect Check Point SmartDefense logs
Collect ChromeOS XDR logs
Collect Chronicle SOAR Audit logs
Collect CipherTrust Manager logs
Collect CircleCI audit logs
Collect Cisco Application Centric Infrastructure (ACI) logs
Collect Cisco AMP for Endpoints logs
Collect Cisco APIC logs
Collect Cisco Application Control Engine (ACE) logs
Collect Cisco CallManager logs
Collect Cisco CloudLock CASB logs
Collect Cisco CTS logs
Collect Cisco DNA Center Platform logs
Collect Cisco eStreamer logs
Collect Cisco Firepower NGFW logs
Collect Cisco FireSIGHT Management Center logs
Collect Cisco IOS logs
Collect Cisco IronPort logs
Collect Cisco ISE logs
Collect Cisco Meraki logs
Collect Cisco PIX logs
Collect Cisco Prime logs
Collect Cisco Router logs
Collect Cisco Secure ACS logs
Collect Cisco Secure Email Gateway logs
Collect Cisco Stealthwatch logs
Collect Cisco Switch logs
Collect Cisco UCS logs
Collect Cisco VCS logs
Collect Cisco Vision Dynamic Signage Director logs
Collect Cisco vManage SD-WAN logs
Collect Cisco VPN logs
Collect Cisco Web Security Appliance (WSA) logs
Collect Cisco Wireless Intrusion Prevention System (WIPS) logs
Collect Cisco Wireless LAN Controller (WLC) logs
Collect Cisco Wireless Security Management (WiSM) logs
Collect Citrix Analytics logs
Collect Citrix Monitor Service logs
Collect Citrix StoreFront logs
Collect Compute Engine context logs
Collect ClamAV logs
Collect Claroty CTD logs
Collect Claroty xDome logs
Collect Gmail logs
Collect Google Cloud Compute context logs
Collect Google Cloud Compute logs
Collect Cloud Identity Devices logs
Collect Cloud Identity Device Users logs
Collect Google Cloud IDS logs
Collect Google Cloud Monitoring alerting activity logs
Collect Google Cloud Network Connectivity Center logs
Collect Google Cloud IoT logs
Collect Google Cloud Secure Web Proxy logs
Collect Identity and Access Management (IAM) Analysis context logs
Collect Cloud Next Generation Firewall logs
Collect Cloud Run logs
Collect Security Command Center Error logs
Collect Security Command Center Observation logs
Collect Security Command Center Posture Violation logs
Collect Security Command Center Toxic Combination logs
Collect Security Command Center Unspecified logs
Collect Cloud Storage context logs
Collect Secure Web Proxy logs
Collect Cloudflare logs
Collect Cloudflare Page Shield logs
Collect Cloudflare WAF logs
Collect Cloudian HyperStore logs
Collect CloudPassage Halo logs
Code42 Incydr core datasets
Collect Cofense logs
Collect Cohesity logs
Collect Commvault logs
Collect CommVault Backup and Recovery logs
Collect Comodo AV logs
Collect context access aware data
Collect Corelight Sensor logs
Collect Cribl Stream logs
Collect CrowdStrike Falcon logs in CEF
Collect CrowdStrike Falcon Stream logs
Collect CrowdStrike FileVantage logs
Collect CrowdStrike IDP Services logs
Collect CrowdStrike IOC logs
Collect CrushFTP logs
Collect Custom Application Access logs
Collect Custom Security Data Analytics logs
Collect CSV Custom IOC files
Collect Cyber 2.0 IDS logs
Collect CyberArk EPM logs
Collect CyberArk logs
Collect CyberArk PAM logs
Collect CyberArk Privilege Cloud logs
Collect CyberArk Privileged Threat Analytics logs
Collect Cybereason EDR logs
Collect CyberX logs
Collect Cylance PROTECT logs
Collect Cynet 360 AutoXDR logs
Collect Cyolo OT logs
Collect Datadog logs
Collect Dataminr Alerts logs
Collect Darktrace logs
Collect Deep Instinct EDR logs
Collect Delinea Distributed Engine logs
Collect Delinea PAM logs
Collect Delinea Secret Server logs
Collect Delinea SSO logs
Collect Dell CyberSense logs
Collect Dell ECS logs
Collect Dell EMC Data Domain logs
Collect Dell EMC Isilon NAS logs
Collect Dell EMC PowerStore logs
Collect Dell OpenManage logs
Collect Dell switch logs
Collect DigiCert audit logs
Collect Digi Modems logs
Collect Digital Guardian EDR logs
Collect Digital Shadows Indicators logs
Collect Digital Shadows SearchLight logs
Collect DomainTools Iris Investigate results
Collect DNSFilter logs
Collect Dope Security SWG logs
Collect Druva Backup logs
Collect Duo administrator logs
Collect Duo authentication logs
Collect Duo entity context logs
Collect Duo Telephony logs
Collect Duo User context logs
Collect Edgio WAF logs
Collect EfficientIP DDI logs
Collect Elastic Auditbeat logs
Collect Elastic Defend logs
Collect Elastic Packet Beats logs
Collect Elasticsearch logs
Collect Elastic Windows Event Log Beats logs
Collect Endpoint Protector DLP logs
Collect Entrust nShield HSM audit logs
Collect Epic Systems logs
Collect Ergon Informatik Airlock IAM logs
Collect ESET AV logs
Collect ESET EDR logs
Collect ESET Threat Intelligence logs
Collect ExtraHop DNS logs
Collect ExtraHop RevealX logs
Collect Extreme Networks switch logs
Collect Extreme Networks Wireless logs
Collect F5 AFM logs
Collect F5 ASM logs
Collect F5 BIG-IP APM logs
Collect F5 BIG-IP ASM logs
Collect F5 BIG-IP LTM logs
Collect F5 DNS logs
Collect F5 Distributed Cloud Services logs
Collect F5 Shape logs
Collect F5 Silverline logs
Collect F5 VPN logs
Collect Falco IDS logs
Collect Fastly CDN logs
Collect Fastly WAF logs
Collect Fidelis Network logs
Collect File Scanning Framework logs
Collect FileZilla FTP logs
Collect FingerprintJS logs
Collect FireEye eMPS logs
Collect FireEye ETP logs
Collect FireEye HX logs
Collect FireEye HX Audit logs
Collect FireEye NX logs
Collect FireEye NX Audit logs
Collect Fivetran logs
Collect Forcepoint CASB logs
Collect Forcepoint DLP logs
Collect Forcepoint Email Security logs
Collect Forcepoint Mail Relay logs
Collect Forcepoint NGFW logs
Collect Forcepoint Web Security logs
Collect Forescout NAC logs
Collect ForgeRock OpenAM logs
Collect ForgeRock OpenIDM logs
Collect Forseti Open Source logs
Collect Fortinet FortiAnalyzer logs
Collect Fortinet FortiAuthenticator logs
Collect Fortinet FortiClient logs
Collect Fortinet FortiDDoS logs
Collect Fortinet FortiEDR logs
Collect Fortinet FortiMail logs
Collect Fortinet FortiManager logs
Collect Fortinet FortiSASE logs
Collect Fortinet Switch logs
Collect FortiWeb WAF logs
Collect Fortra Digital Guardian DLP logs
Collect Fortra Powertech SIEM Agent logs
Collect GitHub audit logs
Collect GitLab logs
Collect Google App Engine logs
Collect Google Cloud DNS Threat Detector logs
Collect H3C Comware Platform Switch logs
Collect HackerOne logs
Collect HAProxy logs
Collect Harness IO audit logs
Collect HashiCorp audit logs
Collect Hillstone Firewall logs
Collect Hitachi Content Platform logs
Collect HP ProCurve logs
Collect HPE Aruba Networking Central logs
Collect HPE BladeSystem c7000 logs
Collect HYPR MFA logs
Collect IBM DB2 logs
Collect IBM Guardium logs
Collect IBM Verify Identity Access logs
Collect Illumio Core logs
Collect Imperva Attack Analytics logs
Collect Imperva Advanced Bot Protection logs
Collect Imperva Audit Trail logs
Collect Imperva CEF logs
Collect Imperva Database logs
Collect Imperva Data Risk Analytics (DRA) logs
Collect Imperva FlexProtect logs
Collect Imperva SecureSphere Management logs
Collect Imperva WAF logs
Collect Infoblox logs
Collect Jamf Pro context logs
Collect Jenkins logs
Collect JFrog Artifactory logs
Collect Juniper Junos logs
Collect Juniper NetScreen Firewall logs
Collect Kaseya Datto File Protection logs
Collect Kaspersky AV logs
Collect Kemp Load Balancer logs
Collect Kiteworks (formally Accellion) logs
Collect Lacework Cloud Security logs
Collect LimaCharlie EDR logs
Collect Linux auditd and AIX systems logs
Collect ManageEngine AD360 logs
Collect ManageEngine ADAudit Plus logs
Collect ManageEngine ADManager Plus logs
Collect McAfee Firewall Enterprise logs
Collect McAfee Web Gateway logs
Collect Micro Focus NetIQ Access Manager logs
Collect Microsoft Azure Activity logs
Collect Microsoft Azure AD logs
Collect Microsoft Azure AD Audit logs
Collect Microsoft Azure AD Context logs
Collect Microsoft Azure DevOps audit logs
Collect Microsoft Azure Key Vault logging logs
Collect Microsoft Azure Resource logs
Collect Microsoft Defender for Cloud Alert logs
Collect Microsoft Defender for Identity logs
Collect Microsoft Exchange logs
Collect Microsoft Graph Activity logs
Collect Microsoft IIS logs
Collect Microsoft Intune logs
Collect Microsoft Intune Context logs
Collect Microsoft LAPS logs
Collect Microsoft Sentinel logs
Collect Microsoft SQL Server logs
Collect Microsoft Windows Defender ATP logs
Collect Mimecast Mail logs
Collect Mimecast Mail V2 logs
Collect MISP IOC logs
Collect MobileIron logs
Collect MuleSoft Anypoint logs
Collect MYSQL logs
Collect Nasuni File Services Platform logs
Collect NetApp ONTAP logs
Collect NetApp SAN logs
Collect pfSense logs
Collect Netscaler logs
Collect Netskope alert logs v1
Collect Netskope alert logs v2
Collect Netskope web proxy logs
Collect NGINX logs
Collect Nix Systems Red Hat logs
Collect Nix Systems Ubuntu Server (Unix System) logs
Collect Nokia Router logs
Collect ntopng logs
Collect Nutanix Prism logs
Collect Okta logs
Collect Okta User Context logs
Collect OneLogin Single Sign-On (SSO) logs
Collect 1Password logs
Collect 1Password Audit logs
Collect Onfido logs
Collect OpenCanary logs
Collect OPNsense firewall logs
Collect Oracle Cloud Infrastructure Audit logs
Collect Oracle DB logs
Collect Palo Alto Cortex XDR alerts logs
Collect Palo Alto Cortex XDR events logs
Collect Palo Alto Networks IOC logs
Collect Palo Alto Networks Traps logs
Collect Palo Alto Prisma Cloud logs
Collect Palo Alto Prisma Cloud alert logs
Collect Palo Alto Prisma SD-WAN logs
Collect PingOne Advanced Identity Cloud logs
Collect PowerShell logs
Collect Proofpoint Emerging Threats Pro IOC logs
Collect Proofpoint On-Demand logs
Collect Proofpoint TAP alerts logs
Collect Pulse Secure logs
Collect Qualys asset context logs
Collect Qualys Continuous Monitoring logs
Collect Qualys Scan logs
Collect Qualys Virtual Scanner logs
Collect Qualys Vulnerability Management logs
Collect Radware WAF logs
Collect Rapid7 InsightIDR logs
Collect reCAPTCHA Enterprise logs
Collect Recorded Future IOC logs
Collect RH-ISAC IOC logs
Collect Rippling activity logs
Collect RSA Authentication Manager logs
Collect SailPoint IAM logs
Collect Salesforce logs
Collect SecureAuth Identity Platform logs
Collect SentinelOne Deep Visibility logs
Collect SentinelOne EDR logs
Collect Sentry logs
Collect ServiceNow audit logs
Collect ServiceNow CMDB data
Collect ServiceNow Security logs
Collect Signal Sciences WAF logs
Collect Skyhigh Security logs
Collect Slack audit logs
Collect Snipe-IT logs
Collect Snort logs
Collect Snowflake logs
Collect Snyk group-level audit logs
Collect Snyk group-level audit and issues logs
Collect SonicWall logs
Collect Sophos AV logs
Collect Sophos Capsule8 logs
Collect Sophos Central logs
Collect Sophos DHCP logs
Collect Sophos Intercept EDR logs
Collect Sophos UTM logs
Collect Sophos XG Firewall logs
Collect Suricata Eve logs
Collect Swimlane Platform logs
Collect Symantec CloudSOC CASB logs
Collect Symantec DLP logs
Collect Symantec EDR logs
Collect Symantec Endpoint Protection logs
Collect Symantec Event Export logs
Collect Symantec VIP Authentication Hub logs
Collect Symantec VIP Enterprise Gateway logs
Collect Symantec Web Isolation logs
Collect Symantec WSS logs
Collect Synology logs
Collect Sysdig logs
Collect Tailscale logs
Collect Tanium Asset logs
Collect Tanium audit logs
Collect Tanium Comply logs
Collect Tanium Discover logs
Collect Tanium Insight logs
Collect Tanium Integrity Monitor logs
Collect Tanium Patch logs
Collect Tanium Question logs
Collect Tanium Reveal logs
Collect Tanium Stream logs
Collect Tanium Threat Response logs
Collect Team Cymru Scout Threat Intelligence data
Collect TeamViewer logs
Collect Thinkst Canary logs
Collect ThreatConnect IOC logs
Collect ThreatConnect IOC logs using the v3 API
Collect Tines audit logs
Collect Trellix DLP logs
Collect Trellix ePO logs
Collect Trellix IPS logs
Collect Trend Micro Apex One logs
Collect Trend Micro Cloud One logs
Collect Trend Micro DDI logs
Collect Trend Micro Deep Security logs
Collect Trend Micro Email Security logs
Collect Trend Micro Vision One logs
Collect Trend Micro Vision One Activity logs
Collect Trend Micro Vision One Audit logs
Collect Trend Micro Vision One Container Vulnerability logs
Collect Trend Micro Vision Detections logs
Collect Trend Micro Vision One Observed Attack Techniques logs
Collect Trend Micro Vision One Workbench logs
Collect Tripwire logs
Collect Twingate VPN logs
Collect Ubiquiti Unifi switch logs
Collect Uptycs EDR logs
Collect URLScan IO logs
Collect VanDyke VShell SFTP logs
Collect Varonis logs
Collect Veeam logs
Collect Vectra Detect logs
Collect Vectra Stream logs
Collect Venafi Zero Touch PKI logs
Collect Veridium ID logs
Collect Veritas NetBackup logs
Collect Versa Networks Secure Access Service Edge (SASE) logs
Collect VMware AirWatch logs
Collect VMware Avi Load Balancer WAF logs
Collect VMware ESXi logs
Collect VMware Horizon logs
Collect VMware Networking and Security Virtualization (NSX) Manager logs
Collect VMware Tanzu logs
Collect VMware vCenter logs
Collect VMware VeloCloud SD-WAN logs
Collect VMware vRealize logs
Collect VMware vSphere logs
Collect VMware Workspace ONE UEM logs
Collect Voltage SecureMail logs
Collect VPC Flow Logs
Collect VSFTPD logs
Collect VyOS logs
Collect Wallix Bastion logs
Collect WatchGuard Fireware logs
Collect Wazuh logs
Collect Wiz logs
Collect Wordpress CMS logs
Collect Workday audit logs
Collect Workday HCM logs
Collect Yamaha router logs
Collect Zendesk CRM logs
Collect ZeroFox Platform logs
Collect Zoom operation logs
Need more help?
Get answers from Community members and Google SecOps professionals.
