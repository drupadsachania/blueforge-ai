# Collect Microsoft Graph API alert logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-alert/  
**Scraped:** 2026-03-05T09:48:28.045917Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Graph API alert logs
Supported in:
Google secops
SIEM
This document describes how you can export Microsoft Graph API alert logs to Google Security Operations
through a Google SecOps feed, and how Microsoft Graph API alert fields map to
Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
Overview
A typical deployment consists of Microsoft Graph API alerts and the Google SecOps feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Microsoft Graph API alerts
: The alerts that the Microsoft Graph API generates.
Google SecOps-managed feed
. The Google SecOps-managed feed that fetches logs from Microsoft Graph Providers (Cloud) and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the Microsoft Graph API alerts logs.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
MICROSOFT_GRAPH_ALERT
ingestion label.
Before you begin
Ensure you have the following prerequisite:
Access to Microsoft 365 E5
How to configure Microsoft Graph API alerts
Complete the following before you configure the Google SecOps feed:
Sign in to the Azure portal.
Click
Azure Active Directory
.
Click
App Registrations
.
Click
New registrations
and create an application.
Copy
Client ID
and
Tenant ID
, which are required when you configure the Google Security Operations feed.
Click
API permissions
.
Click
Add a permission
and then select
Microsoft Graph
in the new pane.
Click
Application Permissions
.
Expand the
SecurityActions
,
SecurityEvents
, and
SecurityIncident
sections, and select
Read.All
permissions.
Click
Add permissions
.
Click
Grant Admin consent for Default Directory
.
In the
Manage
menu, click
Certificates
&
secrets
.
Click
New Client secret
, and create a new key.
Copy the secret key from the
Value
field. The secret key is displayed only
at the time of creation and is required when you configure the Google Security Operations feed.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up Microsoft Graph API alerts
To configure a single feed, follow these steps:
Click the
Azure Cloud Compute Platform
pack.
Locate the
Microsoft Graph API alerts
feed.
Specify values for the following fields:
Source Type
: Third party API (recommended)
OAUTH client ID
: Specify the client ID that you obtained previously.
OAUTH client secret
: Specify the client secret that you obtained previously.
Tenant ID
: Specify the tenant ID that you obtained previously.
API Full path
: Specify the API path as
graph.microsoft.com/v1.0/security/alerts_v2
API Authentication Endpoint
: Microsoft Active Directory Authentication Endpoint.
Advanced Options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
:
Namespace associated with the feed
.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
To configure multiple feeds for different log types within this product family, see
Configure feeds by product
.
Supported Microsoft Graph API alerts log formats
The Microsoft Graph API alerts parser supports logs in JSON format.
Supported Microsoft Graph API alerts Sample Logs
JSON
{
    "activityGroupName": null,
    "assignedTo": null,
    "azureSubscriptionId": null,
    "azureTenantId": "azureTenantId",
    "category": "UnfamiliarLocation",
    "closedDateTime": null,
    "cloudAppStates": [],
    "comments": [],
    "confidence": null,
    "createdDateTime": "2020-09-09T10:37:20.3271044Z",
    "description": "Sign-in with properties we have not seen recently for the given user",
    "detectionIds": [],
    "eventDateTime": "2020-09-09T10:37:20.3271044Z",
    "feedback": null,
    "fileStates": [],
    "historyStates": [],
    "hostStates": [],
    "id": "ID",
    "incidentIds": [],
    "lastModifiedDateTime": "2020-09-09T10:40:08.8987903Z",
    "malwareStates": [],
    "networkConnections": [],
    "processes": [],
    "recommendedActions": [],
    "registryKeyStates": [],
    "riskScore": null,
    "securityResources": [],
    "severity": "medium",
    "sourceMaterials": [],
    "status": "newAlert",
    "tags": [],
    "title": "Unfamiliar sign-in properties",
    "triggers": [],
    "userStates": [
      {
        "aadUserId": "dummyuserid",
        "accountName": "USER1234",
        "domainName": "dummy_domain.com",
        "emailRole": "unknown",
        "isVpn": null,
        "logonDateTime": "2020-09-09T10:37:20.3271044Z",
        "logonId": null,
        "logonIp": "198.51.100.4",
        "logonLocation": "Chicago, Illinois, US",
        "logonType": null,
        "onPremisesSecurityIdentifier": null,
        "riskScore": null,
        "userAccountType": null,
        "userPrincipalName": "test@domain.com"
      }
    ],
    "vendorInformation": {
      "provider": "IPC",
      "providerVersion": null,
      "subProvider": null,
      "vendor": "Microsoft"
    },
    "vulnerabilityStates": []
  }
Field mapping reference
This section explains how the Google SecOps parser maps Microsoft Graph API alert fields to Google SecOps UDM fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
MICROSOFT_GRAPH_ALERT
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
Atypical travel
USER_UNCATEGORIZED
Anomalous Token
USER_RESOURCE_ACCESS
Default Mapping
USER_UNCATEGORIZED
Malware linked IP address
USER_LOGIN
Suspicious browser
USER_UNCATEGORIZED
Unfamiliar sign-in properties
USER_LOGIN
Malicious IP address
USER_LOGIN
Suspicious inbox manipulation rules
USER_UNCATEGORIZED
Password spray
USER_UNCATEGORIZED
AUTH_VIOLATION
Impossible travel
USER_UNCATEGORIZED
New country
USER_UNCATEGORIZED
Activity from anonymous IP address
USER_UNCATEGORIZED
Suspicious inbox forwarding
USER_UNCATEGORIZED
Mass Access to Sensitive Files
USER_RESOURCE_ACCESS
Additional risk detected
STATUS_UPDATE
Anonymous IP address
USER_LOGIN
Admin confirmed user compromised
USER_UNCATEGORIZED
Azure AD threat intelligence
USER_UNCATEGORIZED
Possible attempt to access Primary Refresh Token (PRT)
USER_RESOURCE_ACCESS
Verified threat actor IP
USER_LOGIN
Microsoft Entra threat intelligence (sign-in)
USER_UNCATEGORIZED
User reported suspicious activity
USER_UNCATEGORIZED
Suspicious API Traffic
USER_UNCATEGORIZED
Suspicious sending patterns
USER_UNCATEGORIZED
Leaked credentials
STATUS_UPDATE
Anomalous user activity
USER_UNCATEGORIZED
'Phish' malware was prevented
SCAN_HOST
MAIL_PHISHING
'AutoItinject' malware was detected
SCAN_HOST
'Agent' backdoor was detected
SCAN_UNCATEGORIZED
A malicious file was detected based on indication provided by O365
SCAN_FILE
An active 'Wacatac' malware was blocked
SCAN_UNCATEGORIZED
A suspicious file was observed
SCAN_FILE
'AutoItinject' malware was prevented
SCAN_HOST
'CoinMiner' unwanted software was prevented
SCAN_HOST
Right-to-Left-Override (RLO) technique observed
SCAN_FILE
SOCIAL_ENGINEERING
Connection to a custom network indicator
SCAN_UNCATEGORIZED
'Conteban' malware was detected
SCAN_HOST
SOFTWARE_PUA
EAF violation blocked by exploit protection
SCAN_UNCATEGORIZED
EXPLOIT
'EICAR_Test_File' malware was prevented
SCAN_HOST
SOFTWARE_MALICIOUS
'EncDoc' malware was prevented
SCAN_HOST
SOFTWARE_PUA
'Fuerboos' malware was detected
SCAN_HOST
SOFTWARE_PUA
'Laqma' malware was prevented
SCAN_HOST
SOFTWARE_PUA
'Locky' ransomware was prevented
SCAN_HOST
SOFTWARE_PUA
Microsoft Defender ATP detected 'Trojan.Generic.1218852' malware
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
'Oneeva' malware was prevented
SCAN_HOST
SOFTWARE_PUA
Password hashes dumped from LSASS memory
USER_UNCATEGORIZED
'PiriformBundler' unwanted software was prevented
SCAN_HOST
SOFTWARE_PUA
'Presenoker' unwanted software was prevented
SCAN_HOST
SOFTWARE_PUA
Sensitive credential memory read
SCAN_UNCATEGORIZED
Suspicious connection blocked by network protection
SCAN_UNCATEGORIZED
Test_Set Auditpol
SCAN_UNCATEGORIZED
Unsanctioned cloud app access was blocked
SCAN_UNCATEGORIZED
'Uwamson' malware was prevented
SCAN_HOST
SOFTWARE_PUA
'CoinMiner' unwanted software was detected
SCAN_HOST
SOFTWARE_PUA
Suspicious Microsoft Defender Antivirus exclusion
SCAN_UNCATEGORIZED
NT - Unknown process injecting dll into lsass or winlogon
SCAN_UNCATEGORIZED
Suspected SID-History injection
USER_CHANGE_PERMISSIONS
Suspected overpass-the-hash attack (Kerberos)
NETWORK_UNCATEGORIZED
Account enumeration reconnaissance
NETWORK_UNCATEGORIZED
Suspected Brute Force attack (LDAP)
USER_LOGIN
Suspected DCSync attack (replication of directory services)
NETWORK_UNCATEGORIZED
Network mapping reconnaissance (DNS)
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected over-pass-the-hash attack (forced encryption type)
NETWORK_UNCATEGORIZED
Suspected Golden Ticket usage (encryption downgrade)
USER_UNCATEGORIZED
Suspected Skeleton Key attack (encryption downgrade)
NETWORK_UNCATEGORIZED
User and IP address reconnaissance (SMB)
NETWORK_UNCATEGORIZED
Suspected Golden Ticket usage (forged authorization data)
USER_UNCATEGORIZED
Honeytoken authentication activity
USER_UNCATEGORIZED
Suspected identity theft (pass-the-hash)
USER_UNCATEGORIZED
DATA_EXFILTRATION
Suspected identity theft (pass-the-ticket)
USER_UNCATEGORIZED
EXPLOIT
Remote code execution attempt
USER_UNCATEGORIZED
Malicious request of Data Protection API master key
USER_UNCATEGORIZED
User and Group membership reconnaissance (SAMR)
USER_UNCATEGORIZED
Suspected Golden Ticket usage (time anomaly)
USER_UNCATEGORIZED
Suspected Brute Force attack (Kerberos, NTLM)
USER_LOGIN
Suspicious additions to sensitive groups
USER_CHANGE_PERMISSIONS
Suspicious VPN connection
USER_UNCATEGORIZED
Suspicious service creation
SERVICE_CREATION
Suspected Golden Ticket usage (nonexistent account)
USER_UNCATEGORIZED
Suspected DCShadow attack (domain controller promotion)
STATUS_UPDATE
Suspected DCShadow attack (domain controller replication request)
STATUS_UPDATE
Data exfiltration over SMB
STATUS_UPDATE
DATA_EXFILTRATION
Suspicious communication over DNS
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected Golden Ticket usage (ticket anomaly)
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected Brute Force attack (SMB)
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected use of Metasploit hacking framework
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected WannaCry ransomware attack
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Remote code execution over DNS
NETWORK_UNCATEGORIZED
Suspected NTLM relay attack
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Security principal reconnaissance (LDAP)
STATUS_UPDATE
Suspected NTLM authentication tampering
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected Golden Ticket usage (ticket anomaly using RBCD)
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected rogue Kerberos certificate usage
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspicious Kerberos delegation attempt using BronzeBit method (CVE-2020-17049 exploitation)
STATUS_UPDATE
NETWORK_SUSPICIOUS
Active Directory attributes reconnaissance (LDAP)
STATUS_UPDATE
Suspected SMB packet manipulation (CVE-2020-0796 exploitation)
STATUS_UPDATE
Suspected Kerberos SPN exposure
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected Netlogon privilege elevation attempt (CVE-2020-1472 exploitation)
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected AS-REP Roasting attack
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected AD FS DKM key read
STATUS_UPDATE
Exchange Server Remote Code Execution (CVE-2021-26855)
STATUS_UPDATE
Suspected exploitation attempt on Windows Print Spooler service
NETWORK_UNCATEGORIZED
Suspicious network connection over Encrypting File System Remote Protocol
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspected suspicious Kerberos ticket request
STATUS_UPDATE
Suspicious modification of a sAMNameAccount attribute (CVE-2021-42278 and CVE-2021-42287 exploitation)
STATUS_UPDATE
Suspected brute-force attack (Kerberos, NTLM)
USER_UNCATEGORIZED
AUTH_VIOLATION
Suspicious modification of the trust relationship of AD FS server
SETTING_MODIFICATION
Suspicious modification of a dNSHostName attribute (CVE-2022-26923)
SETTING_MODIFICATION
Suspicious Kerberos delegation attempt by a newly created computer
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspicious modification of the Resource Based Constrained Delegation attribute by a machine account
SETTING_MODIFICATION
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
USER_LOGIN
Suspicious certificate usage over Kerberos protocol (PKINIT)
STATUS_UPDATE
EXPLOIT
Suspected DFSCoerce attack using Distributed File System Protocol
USER_LOGIN
Honeytoken user attributes modified
SETTING_MODIFICATION
Honeytoken group membership changed
GROUP_MODIFICATION
Honeytoken was queried via LDAP
STATUS_UPDATE
Suspicious modification of domain AdminSdHolder
SETTING_MODIFICATION
Suspected account takeover using shadow credentials
USER_RESOURCE_ACCESS
EXPLOIT
Suspicious Domain Controller certificate request (ESC8)
STATUS_UPDATE
Suspicious deletion of the certificate database entries
STATUS_UPDATE
Suspicious disable of audit filters of AD CS
SETTING_MODIFICATION
Suspicious modifications to the AD CS security permissions/settings
SETTING_MODIFICATION
Account Enumeration reconnaissance (LDAP) (Preview)
STATUS_UPDATE
Directory Services Restore Mode Password Change (Preview)
SETTING_MODIFICATION
Honeytoken was queried via SAM-R
STATUS_UPDATE
User and group membership reconnaissance (SAMR)
USER_RESOURCE_ACCESS
A potentially malicious URL click was detected
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
A user clicked through to a potentially malicious URL
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Admin Submission result completed
STATUS_UPDATE
Admin triggered manual investigation of email
EMAIL_TRANSACTION
Admin triggered user compromise investigation
EMAIL_TRANSACTION
Administrative action submitted by an Administrator
EMAIL_UNCATEGORIZED
Creation of forwarding/redirect rule
USER_UNCATEGORIZED
eDiscovery search started or exported
USER_UNCATEGORIZED
Email messages containing malicious file removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Email messages containing malicious URL removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Email messages containing malware removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Email messages containing phish URLs removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Email messages from a campaign removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Email messages removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Messages containing malicious entity not removed after delivery
EMAIL_TRANSACTION
MAIL_PHISHING
Email reported by user as malware or phish
EMAIL_TRANSACTION
MAIL_PHISHING
Email sending limit exceeded
EMAIL_UNCATEGORIZED
Form blocked due to potential phishing attempt
STATUS_UPDATE
MAIL_PHISHING
Form flagged and confirmed as phishing
STATUS_UPDATE
MAIL_PHISHING
Messages have been delayed
EMAIL_UNCATEGORIZED
Malware campaign detected after delivery
EMAIL_TRANSACTION
Malware campaign detected and blocked
EMAIL_TRANSACTION
Malware campaign detected in SharePoint and OneDrive
STATUS_UPDATE
Malware not zapped because ZAP is disabled
STATUS_UPDATE
Phish delivered due to an ETR override
EMAIL_UNCATEGORIZED
NETWORK_SUSPICIOUS
Phish delivered due to an IP allow policy
EMAIL_TRANSACTION
NETWORK_SUSPICIOUS
Phish not zapped because ZAP is disabled
EMAIL_TRANSACTION
NETWORK_SUSPICIOUS
Phish delivered due to tenant or user override1
EMAIL_TRANSACTION
Suspicious email forwarding activity
EMAIL_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspicious email sending patterns detected
EMAIL_UNCATEGORIZED
EXPLOIT
Tenant Allow/Block List entry is about to expire
STATUS_UPDATE
Tenant restricted from sending email
EMAIL_UNCATEGORIZED
Tenant restricted from sending unprovisioned email
EMAIL_UNCATEGORIZED
Unusual external user file activity
FILE_UNCATEGORIZED
NETWORK_SUSPICIOUS
Unusual volume of external file sharing
FILE_UNCATEGORIZED
NETWORK_SUSPICIOUS
Unusual volume of file deletion
FILE_DELETION
DATA_DESTRUCTION
Unusual increase in email reported as phish
EMAIL_TRANSACTION
NETWORK_SUSPICIOUS
User impersonation phish delivered to inbox/folder
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
User requested to release a quarantined message
USER_UNCATEGORIZED
User restricted from sending email
USER_UNCATEGORIZED
User restricted from sharing forms and collecting responses
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Elevation of Exchange admin privilege
USER_UNCATEGORIZED
Activity by terminated user
USER_UNCATEGORIZED
ACL_VIOLATION
DLP-Detect Highly Sensitive Data Movement
USER_UNCATEGORIZED
NETWORK_MALICIOUS
DLP-Sensitive Data Movement
USER_UNCATEGORIZED
Email reported by user as junk
EMAIL_TRANSACTION
Suspicious massive data read
USER_UNCATEGORIZED
Activity from infrequent country
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Malware detection
USER_UNCATEGORIZED
Activity from anonymous IP addresses
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Ransomware activity
USER_UNCATEGORIZED
Activity performed by terminated user
USER_UNCATEGORIZED
POLICY_VIOLATION
Activity from suspicious IP addresses
USER_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspicious inbox forwarding
EMAIL_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspicious inbox manipulation rules
STATUS_UPDATE
NETWORK_SUSPICIOUS
Suspicious email deletion activity
EMAIL_UNCATEGORIZED
NETWORK_SUSPICIOUS
Suspicious OAuth app file download activities
SCAN_HOST
Unusual ISP for an OAuth App
NETWORK_UNCATEGORIZED
SOFTWARE_PUA
Unusual multiple file download activities
USER_UNCATEGORIZED
Unusual file share activities
USER_UNCATEGORIZED
Unusual file deletion activities
USER_UNCATEGORIZED
Unusual impersonated activities
USER_UNCATEGORIZED
Unusual administrative activities
USER_UNCATEGORIZED
Unusual Power BI report sharing activities (preview)
USER_UNCATEGORIZED
Unusual multiple VM creation activities (preview)
USER_UNCATEGORIZED
Unusual multiple storage deletion activities (preview)
USER_UNCATEGORIZED
Unusual region for cloud resource (preview)
USER_UNCATEGORIZED
Unusual file access
USER_UNCATEGORIZED
Multiple failed login attempts
USER_LOGIN
AUTH_VIOLATION
Data exfiltration to unsanctioned apps
USER_UNCATEGORIZED
DATA_EXFILTRATION
Multiple delete VM activities
USER_UNCATEGORIZED
DATA_DESTRUCTION
Misleading OAuth app name
SCAN_UNCATEGORIZED
POLICY_VIOLATION
Misleading publisher name for an OAuth app
SCAN_UNCATEGORIZED
POLICY_VIOLATION
Malicious OAuth app consent
SCAN_UNCATEGORIZED
Activity from a TOR IP address
USER_LOGIN
ACL_VIOLATION
Impossible travel activity
USER_UNCATEGORIZED
POLICY_VIOLATION
Activity from Nigeria
USER_UNCATEGORIZED
POLICY_VIOLATION
Activity from an anonymous proxy
USER_UNCATEGORIZED
Block download based on real-time content inspection
USER_UNCATEGORIZED
Investigation priority score increase
USER_UNCATEGORIZED
Mass delete
USER_UNCATEGORIZED
DATA_DESTRUCTION
Mass download by a single user - External users
USER_RESOURCE_ACCESS
Mass download by a single user - Internal
USER_RESOURCE_ACCESS
Mass share
USER_UNCATEGORIZED
Multiple Power BI report sharing activities
USER_UNCATEGORIZED
New high upload volume app
STATUS_UPDATE
POLICY_VIOLATION
New high volume app
STATUS_UPDATE
POLICY_VIOLATION
New risky app
STATUS_UPDATE
POLICY_VIOLATION
Ransomware activity
USER_UNCATEGORIZED
Suspicious administrative activity
USER_RESOURCE_ACCESS
Unknown login to Exchange Online
USER_UNCATEGORIZED
Unusual addition of credentials to an OAuth app
USER_RESOURCE_ACCESS
Tracking Online Meeting App Usage
STATUS_UPDATE
Mass download by a single user
USER_UNCATEGORIZED
Mass download
USER_UNCATEGORIZED
New popular app
STATUS_UPDATE
POLICY_VIOLATION
Compromised account
STATUS_UPDATE
New admin user
STATUS_UPDATE
New location
STATUS_UPDATE
Inactive account
STATUS_UPDATE
Ransomware activity
USER_UNCATEGORIZED
Unexpected admin location
STATUS_UPDATE
Suspicious activity alert
STATUS_UPDATE
Suspicious cloud use alert
STATUS_UPDATE
Activity policy violation
STATUS_UPDATE
POLICY_VIOLATION
File policy violation
STATUS_UPDATE
POLICY_VIOLATION
Proxy policy violation
STATUS_UPDATE
POLICY_VIOLATION
Field policy violation
STATUS_UPDATE
POLICY_VIOLATION
New service discovered
STATUS_UPDATE
Use of personal account
STATUS_UPDATE
Failed logon attempts
USER_UNCATEGORIZED
Anomalous SSH login detected
USER_LOGIN
Identity  - Suspicious granting of permissions to an account
USER_CHANGE_PERMISSIONS
Endpoint - NT - Suspicious Oracle Query - Attempted Password Hash Exfiltration
USER_UNCATEGORIZED
DATA_EXFILTRATION
Suspicious Resource deployment
USER_RESOURCE_ACCESS
Endpoint - NT - Anomalous BITS download URL destination - Rule
STATUS_UPDATE
Azure High Risk User account - Signin
USER_LOGIN
Azure VWAN Tunnel Down - Run the RRAS Scrip
STATUS_UPDATE
Brute force attack against Azure Portal
USER_LOGIN
Changes made to AWS CloudTrail logs
STATUS_UPDATE
Endpoint - NT - A .js file executed inside zip archive. Locky - Rule
STATUS_UPDATE
Endpoint - NT - New service created with anomalous name and  ImagePath under users. - Rul
SERVICE_CREATION
Endpoint - NT - New service created with possibly obfuscated powershell commandline ImagePath - Rule
SERVICE_CREATION
Endpoint - NT - Powershell CommandLine Longer than 2000 Characters
USER_UNCATEGORIZED
Endpoint - NT - Scheduled task created with anomalous location under user profile - Rule
SCHEDULED_TASK_CREATION
Failed AzureAD logons but success logon to AWS Console
USER_UNCATEGORIZED
General Policy - Deny Prior Threats
USER_UNCATEGORIZED
High count of failed attempts from same client IP
USER_UNCATEGORIZED
High count of failed logons by a user
USER_UNCATEGORIZED
High Risk Travel Alert
USER_UNCATEGORIZED
Identity - AD user created password not set with 24-48 hours
USER_UNCATEGORIZED
Identity - Attempts to sign in to disabled accounts
USER_LOGIN
Identity - Attempt to bypass conditional access rule in Azure AD
USER_UNCATEGORIZED
Identity - New user created and added to the built-in administrators group
USER_CREATION
Identity - NT - Pulse VPN Brute Force Attempt
USER_UNCATEGORIZED
Identity - User account created and deleted within 10 mins
USER_UNCATEGORIZED
Login to AWS Management Console without MFA
STATUS_UPDATE
Monitor AWS Credential abuse or hijacking
STATUS_UPDATE
Network - FirepowerAlertTest
STATUS_UPDATE
Network - NT - Email detected from tiscali.it may be part of phishing campaign - Rule
EMAIL_UNCATEGORIZED
Network - NT - Phishing attachment delivered - Rule
EMAIL_UNCATEGORIZED
Network - NT - Phishing Link Clicked
EMAIL_UNCATEGORIZED
Network - NT - Malware attachment delivered - Rule
EMAIL_UNCATEGORIZED
Network - NT - Possible Ursnif/Gozi Phish
EMAIL_UNCATEGORIZED
Network - NT - Recently Created Domain Referenced in Inbound Email
EMAIL_UNCATEGORIZED
Network - NT - Sender Domain in Inbound Email Recently Created
EMAIL_UNCATEGORIZED
Network - NT - StealthWatch Detected a Concerning Host
STATUS_UPDATE
Network - Rare RDP Connections
NETWORK_UNCATEGORIZED
Network - SSH Potential Brute Force
USER_LOGIN
NT - Anomalous attempt to reset Domain Admin or Enterprise Admin account password
USER_UNCATEGORIZED
NTC3 Testing Rule AR466
STATUS_UPDATE
NT - Degraded Workspace Performance Warning, Last 4 hours
STATUS_UPDATE
NT - LogSource Increasing or Decreasing over Last 4 Hour
STATUS_UPDATE
NT - StealthWatch Detected Potential Exploitation Activity
STATUS_UPDATE
NT - Usage of jsc.exe. Possible malware recompilation on endpoint - Endpoint
STATUS_UPDATE
Sign-ins from IPs that attempt sign-ins to disabled accounts
STATUS_UPDATE
Test
Endpoint - MDATP Machine Isolated
Test
USER_UNCATEGORIZED
Test- Security Event log Deleted/Cleared
USER_UNCATEGORIZED
Network - NT - Malware url delivered - Rule
STATUS_UPDATE
Endpoint - NT - New service created with anomalous name and  ImagePath under users. - Rule
STATUS_UPDATE
A logon from a malicious IP has been detected. [seen multiple times]
USER_LOGIN
NETWORK_MALICIOUS
Adaptive application control policy violation was audited
STATUS_UPDATE
POLICY_VIOLATION
Addition of Guest account to Local Administrators group
GROUP_MODIFICATION
An event log was cleared
STATUS_UPDATE
Antimalware Action Failed
STATUS_UPDATE
Antimalware Action Taken
STATUS_UPDATE
Antimalware broad files exclusion in your virtual machine
STATUS_UPDATE
Antimalware disabled and code execution in your virtual machine
STATUS_UPDATE
Antimalware disabled in your virtual machine
STATUS_UPDATE
Antimalware file exclusion and code execution in your virtual machine
STATUS_UPDATE
Antimalware file exclusion in your virtual machine
STATUS_UPDATE
Antimalware real-time protection was disabled in your virtual machine
STATUS_UPDATE
Antimalware real-time protection was disabled temporarily in your virtual machine
STATUS_UPDATE
Antimalware real-time protection was disabled temporarily while code was executed in your virtual machine
STATUS_UPDATE
Antimalware scans blocked for files potentially related to malware campaigns on your virtual machine (Preview)
STATUS_UPDATE
Antimalware temporarily disabled in your virtual machine
STATUS_UPDATE
Antimalware unusual file exclusion in your virtual machine
STATUS_UPDATE
Communication with suspicious domain identified by threat intelligence
STATUS_UPDATE
Detected actions indicative of disabling and deleting IIS log files
FILE_MODIFICATION
Detected anomalous mix of upper and lower case characters in command-line
PROCESS_UNCATEGORIZED
Detected change to a registry key that can be abused to bypass UAC
REGISTRY_MODIFICATION
Detected decoding of an executable using built-in certutil.exe tool
PROCESS_UNCATEGORIZED
Detected enabling of the WDigest UseLogonCredential registry key
REGISTRY_MODIFICATION
Detected encoded executable in command line data
PROCESS_UNCATEGORIZED
Detected obfuscated command line
PROCESS_UNCATEGORIZED
Detected possible execution of keygen executable
PROCESS_UNCATEGORIZED
Detected possible execution of malware dropper
STATUS_UPDATE
Detected possible local reconnaissance activity
PROCESS_UNCATEGORIZED
Detected potentially suspicious use of Telegram tool
DEVICE_PROGRAM_DOWNLOAD
SOFTWARE_SUSPICIOUS
Detected suppression of legal notice displayed to users at logon
REGISTRY_MODIFICATION
Detected suspicious combination of HTA and PowerShell
PROCESS_UNCATEGORIZED
Detected suspicious commandline arguments
PROCESS_UNCATEGORIZED
Detected suspicious commandline used to start all executables in a directory
PROCESS_UNCATEGORIZED
Detected suspicious credentials in commandline
PROCESS_UNCATEGORIZED
Detected suspicious document credentials
PROCESS_UNCATEGORIZED
Detected suspicious execution of VBScript.Encode command
PROCESS_UNCATEGORIZED
Detected suspicious execution via rundll32.exe
PROCESS_UNCATEGORIZED
Detected suspicious file cleanup commands
PROCESS_UNCATEGORIZED
Detected suspicious file creation
FILE_CREATION
Detected suspicious named pipe communications
PROCESS_UNCATEGORIZED
Detected suspicious network activity
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Detected suspicious new firewall rule
DEVICE_CONFIG_UPDATE
NETWORK_SUSPICIOUS
Detected suspicious use of Cacls to lower the security state of the system
PROCESS_UNCATEGORIZED
Detected suspicious use of FTP -s Switch
PROCESS_UNCATEGORIZED
Detected suspicious use of Pcalua.exe to launch executable code
PROCESS_UNCATEGORIZED
Detected the disabling of critical services
PROCESS_UNCATEGORIZED
Digital currency mining related behavior detected
PROCESS_UNCATEGORIZED
Dynamic PS script construction
PROCESS_UNCATEGORIZED
Executable found running from a suspicious location
PROCESS_UNCATEGORIZED
Fileless attack behavior detected
PROCESS_UNCATEGORIZED
Fileless attack technique detected
PROCESS_UNCATEGORIZED
Fileless attack toolkit detected
PROCESS_UNCATEGORIZED
High risk software detected
STATUS_UPDATE
Local Administrators group members were enumerated
GROUP_MODIFICATION
Malicious firewall rule created by ZINC server implant [seen multiple times]
SETTING_MODIFICATION
Malicious SQL activity
PROCESS_UNCATEGORIZED
Multiple Domain Accounts Queried
STATUS_UPDATE
Possible credential dumping detected [seen multiple times]
STATUS_UPDATE
Potential attempt to bypass AppLocker detected
PROCESS_UNCATEGORIZED
Rare SVCHOST service group executed
USER_UNCATEGORIZED
Sticky keys attack detected
STATUS_UPDATE
Successful brute force attack
USER_LOGIN
Suspect integrity level indicative of RDP hijacking
PROCESS_PRIVILEGE_ESCALATION
Suspect service installation
SERVICE_CREATION
Suspected Kerberos Golden Ticket attack parameters observed
STATUS_UPDATE
Suspicious Account Creation Detected
USER_CREATION
Suspicious Activity Detected
PROCESS_INJECTION
Suspicious authentication activity
USER_RESOURCE_ACCESS
Suspicious code segment detected
STATUS_UPDATE
Suspicious double extension file executed
PROCESS_UNCATEGORIZED
Suspicious download using Certutil detected [seen multiple times]
PROCESS_UNCATEGORIZED
Suspicious download using Certutil detected
PROCESS_UNCATEGORIZED
Suspicious PowerShell Activity Detected
PROCESS_UNCATEGORIZED
Suspicious PowerShell cmdlets executed
PROCESS_UNCATEGORIZED
Suspicious process executed [seen multiple times]
PROCESS_UNCATEGORIZED
Suspicious process executed
PROCESS_UNCATEGORIZED
Suspicious process name detected [seen multiple times]
PROCESS_UNCATEGORIZED
Suspicious process name detected
PROCESS_UNCATEGORIZED
Suspicious SQL activity
PROCESS_UNCATEGORIZED
Suspicious SVCHOST process executed
PROCESS_UNCATEGORIZED
Suspicious system process executed
PROCESS_UNCATEGORIZED
Suspicious Volume Shadow Copy Activity
RESOURCE_DELETION
Suspicious WindowPosition registry value detected
REGISTRY_MODIFICATION
Suspiciously named process detected
PROCESS_UNCATEGORIZED
Unusual config reset in your virtual machine
SETTING_MODIFICATION
Unusual process execution detected
PROCESS_UNCATEGORIZED
Unusual user password reset in your virtual machine
USER_CHANGE_PASSWORD
Unusual user SSH key reset in your virtual machine
STATUS_UPDATE
VBScript HTTP object allocation detected
FILE_CREATION
Suspicious installation of GPU extension in your virtual machine (Preview)
SERVICE_CREATION
A history file has been cleared
STATUS_UPDATE
Behavior similar to ransomware detected [seen multiple times]
SCAN_UNCATEGORIZED
Container with a miner image detected
SCAN_UNCATEGORIZED
Detected anomalous mix of upper and lower case characters in command line
PROCESS_UNCATEGORIZED
Detected file download from a known malicious source
SCAN_UNCATEGORIZED
Disabling of auditd logging [seen multiple times]
STATUS_UPDATE
Exploitation of Xorg vulnerability [seen multiple times]
STATUS_UPDATE
Failed SSH brute force attack
USER_LOGIN
Hidden file execution detected
PROCESS_UNCATEGORIZED
New SSH key added [seen multiple times]
SETTING_MODIFICATION
New SSH key added
SETTING_MODIFICATION
Possible backdoor detected [seen multiple times]
FILE_UNCATEGORIZED
Possible exploitation of the mailserver detected
SCAN_UNCATEGORIZED
Possible malicious web shell detected
SCAN_UNCATEGORIZED
Possible password change using crypt-method detected [seen multiple times]
USER_CHANGE_PASSWORD
Process associated with digital currency mining detected [seen multiple times]
PROCESS_UNCATEGORIZED
Process associated with digital currency mining detected
PROCESS_UNCATEGORIZED
Python encoded downloader detected [seen multiple times]
SCAN_UNCATEGORIZED
Screenshot taken on host [seen multiple times]
STATUS_UPDATE
Shellcode detected [seen multiple times]
PROCESS_UNCATEGORIZED
Successful SSH brute force attack
USER_LOGIN
Suspicious kernel module detected [seen multiple times]
PROCESS_MODULE_LOAD
Suspicious password access [seen multiple times]
STATUS_UPDATE
Suspicious password access
STATUS_UPDATE
Suspicious request to the Kubernetes Dashboard
STATUS_UPDATE
Anomalous network protocol usage
NETWORK_UNCATEGORIZED
Anonymity network activity
NETWORK_UNCATEGORIZED
Anonymity network activity using web proxy
NETWORK_UNCATEGORIZED
Attempted communication with suspicious sinkholed domain
NETWORK_UNCATEGORIZED
Communication with possible phishing domain
NETWORK_UNCATEGORIZED
Communication with suspicious algorithmically generated domain
NETWORK_UNCATEGORIZED
Communication with suspicious random domain name
NETWORK_UNCATEGORIZED
Digital currency mining activity
NETWORK_UNCATEGORIZED
Network intrusion detection signature activation
NETWORK_UNCATEGORIZED
Possible data download via DNS tunnel
NETWORK_UNCATEGORIZED
Possible data exfiltration via DNS tunnel
NETWORK_UNCATEGORIZED
DATA_EXFILTRATION
Possible data transfer via DNS tunnel
NETWORK_UNCATEGORIZED
Suspicious failure installing GPU extension in your subscription (Preview)
SCAN_UNCATEGORIZED
Suspicious installation of a GPU extension was detected on your virtual machine (Preview)
SCAN_UNCATEGORIZED
Run Command with a suspicious script was detected on your virtual machine (Preview)
PROCESS_UNCATEGORIZED
Suspicious unauthorized Run Command usage was detected on your virtual machine (Preview)
PROCESS_UNCATEGORIZED
Suspicious Run Command usage was detected on your virtual machine (Preview)
PROCESS_UNCATEGORIZED
Suspicious usage of multiple monitoring or data collection extensions was detected on your virtual machines (Preview)
SCAN_UNCATEGORIZED
Suspicious installation of disk encryption extensions was detected on your virtual machines (Preview)
SCAN_UNCATEGORIZED
Suspicious usage of VMAccess extension was detected on your virtual machines (Preview)
SCAN_UNCATEGORIZED
Desired State Configuration (DSC) extension with a suspicious script was detected on your virtual machine (Preview)
PROCESS_UNCATEGORIZED
Suspicious usage of a Desired State Configuration (DSC) extension was detected on your virtual machines (Preview)
PROCESS_UNCATEGORIZED
Custom script extension with a suspicious script was detected on your virtual machine (Preview)
PROCESS_UNCATEGORIZED
Suspicious failed execution of custom script extension in your virtual machine
PROCESS_UNCATEGORIZED
Unusual deletion of custom script extension in your virtual machine
PROCESS_UNCATEGORIZED
Unusual execution of custom script extension in your virtual machine
PROCESS_UNCATEGORIZED
Custom script extension with suspicious entry-point in your virtual machine
PROCESS_UNCATEGORIZED
Custom script extension with suspicious payload in your virtual machine
PROCESS_UNCATEGORIZED
An attempt to run Linux commands on a Windows App Service
PROCESS_UNCATEGORIZED
An IP that connected to your Azure App Service FTP Interface was found in Threat Intelligence
NETWORK_UNCATEGORIZED
Attempt to run high privilege command detected
PROCESS_UNCATEGORIZED
Connection to web page from anomalous IP address detected
SCAN_NETWORK
Dangling DNS record for an App Service resource detected
RESOURCE_DELETION
Detected suspicious file download
SCAN_UNCATEGORIZED
Executable decoded using certutil
PROCESS_UNCATEGORIZED
Microsoft Defender for Cloud test alert for App Service (not a threat)
STATUS_UPDATE
NMap scanning detected
SCAN_UNCATEGORIZED
Phishing content hosted on Azure Webapps
SCAN_UNCATEGORIZED
PHP file in upload folder
SCAN_UNCATEGORIZED
Possible Cryptocoinminer download detected
SCAN_UNCATEGORIZED
Possible data exfiltration detected
NETWORK_UNCATEGORIZED
DATA_EXFILTRATION
Potential dangling DNS record for an App Service resource detected
RESOURCE_DELETION
Potential reverse shell detected
SCAN_UNCATEGORIZED
Raw data download detected
SCAN_UNCATEGORIZED
Saving curl output to disk detected
PROCESS_UNCATEGORIZED
Spam folder referrer detected
SCAN_UNCATEGORIZED
Suspicious access to possibly vulnerable web page detected
SCAN_UNCATEGORIZED
Suspicious domain name reference
SCAN_UNCATEGORIZED
Suspicious PHP execution detected
SCAN_UNCATEGORIZED
Suspicious User Agent detected
SCAN_UNCATEGORIZED
Suspicious WordPress theme invocation detected
SCAN_UNCATEGORIZED
Vulnerability scanner detected
SCAN_UNCATEGORIZED
Web fingerprinting detected
SCAN_UNCATEGORIZED
Website is tagged as malicious in threat intelligence feed
STATUS_UPDATE
Exposed Postgres service with trust authentication configuration in Kubernetes detected (Preview)
SCAN_UNCATEGORIZED
Exposed Postgres service with risky configuration in Kubernetes detected (Preview)
SCAN_UNCATEGORIZED
Attempt to create a new Linux namespace from a container detected
SCAN_UNCATEGORIZED
Abnormal activity of managed identity associated with Kubernetes (Preview)
SCAN_UNCATEGORIZED
Abnormal Kubernetes service account operation detected
SCAN_UNCATEGORIZED
An uncommon connection attempt detected
SCAN_UNCATEGORIZED
Attempt to stop apt-daily-upgrade.timer service detected
SCAN_UNCATEGORIZED
Behavior similar to common Linux bots detected (Preview)
SCAN_UNCATEGORIZED
Command within a container running with high privileges
STATUS_UPDATE
Container running in privileged mode
STATUS_UPDATE
Container with a sensitive volume mount detected
SCAN_UNCATEGORIZED
CoreDNS modification in Kubernetes detected
SCAN_UNCATEGORIZED
Creation of admission webhook configuration detected
SCAN_UNCATEGORIZED
Detected suspicious use of the nohup command
SCAN_UNCATEGORIZED
Detected suspicious use of the useradd command
SCAN_UNCATEGORIZED
Digital currency mining container detected
SCAN_UNCATEGORIZED
Docker build operation detected on a Kubernetes node
SCAN_UNCATEGORIZED
Exposed Kubeflow dashboard detected
SCAN_UNCATEGORIZED
Exposed Kubernetes dashboard detected
SCAN_UNCATEGORIZED
Exposed Kubernetes service detected
SCAN_UNCATEGORIZED
Exposed Redis service in AKS detected
SCAN_UNCATEGORIZED
Indicators associated with DDOS toolkit detected
SCAN_UNCATEGORIZED
K8S API requests from proxy IP address detected
SCAN_UNCATEGORIZED
Kubernetes events deleted
STATUS_UPDATE
Kubernetes penetration testing tool detected
SCAN_UNCATEGORIZED
Microsoft Defender for Cloud test alert (not a threat).
STATUS_UPDATE
New container in the kube-system namespace detected
SCAN_UNCATEGORIZED
New high privileges role detected
SCAN_UNCATEGORIZED
Possible attack tool detected
SCAN_UNCATEGORIZED
Possible backdoor detected
SCAN_UNCATEGORIZED
Possible command line exploitation attempt
SCAN_UNCATEGORIZED
Possible credential access tool detected
SCAN_UNCATEGORIZED
Possible Log Tampering Activity Detected
SCAN_UNCATEGORIZED
Possible password change using crypt-method detected
SCAN_UNCATEGORIZED
Potential port forwarding to external IP address
SCAN_UNCATEGORIZED
Privileged container detected
SCAN_UNCATEGORIZED
Process seen accessing the SSH authorized keys file in an unusual way
FILE_READ
Role binding to the cluster-admin role detected
SCAN_UNCATEGORIZED
Security-related process termination detected
PROCESS_TERMINATION
SSH server is running inside a container
STATUS_UPDATE
Suspicious file timestamp modification
STATUS_UPDATE
Suspicious request to Kubernetes API
STATUS_UPDATE
Potential crypto coin miner started
STATUS_UPDATE
Possible malicious web shell detected.
SCAN_UNCATEGORIZED
Burst of multiple reconnaissance commands could indicate initial activity after compromise
STATUS_UPDATE
Suspicious Download Then Run Activity
STATUS_UPDATE
Access to kubelet kubeconfig file detected
SCAN_UNCATEGORIZED
Access to cloud metadata service detected
SCAN_UNCATEGORIZED
MITRE Caldera agent detected
SCAN_UNCATEGORIZED
A possible vulnerability to SQL Injection
USER_RESOURCE_ACCESS
EXPLOIT
Attempted logon by a potentially harmful application
USER_LOGIN
Log on from an unusual Azure Data Center
USER_LOGIN
Log on from an unusual location
USER_LOGIN
Login from a principal user not seen in 60 days
USER_LOGIN
Login from a domain not seen in 60 days
USER_LOGIN
Login from a suspicious IP
USER_LOGIN
Potential SQL injection
USER_RESOURCE_ACCESS
EXPLOIT
Suspected brute force attack using a valid user
USER_LOGIN
Suspected brute force attack
USER_LOGIN
Suspected successful brute force attack
USER_LOGIN
SQL Server potentially spawned a Windows command shell and accessed an abnormal external source
PROCESS_UNCATEGORIZED
Unusual payload with obfuscated parts has been initiated by SQL Server
STATUS_UPDATE
Logon from an unusual cloud provider
USER_LOGIN
Azure Resource Manager operation from suspicious IP address
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
Azure Resource Manager operation from suspicious proxy IP address
NETWORK_UNCATEGORIZED
NETWORK_SUSPICIOUS
MicroBurst exploitation toolkit used to enumerate resources in your subscriptions
PROCESS_UNCATEGORIZED
MicroBurst exploitation toolkit used to execute code on your virtual machine
PROCESS_UNCATEGORIZED
MicroBurst exploitation toolkit used to extract keys from your Azure key vaults
PROCESS_UNCATEGORIZED
MicroBurst exploitation toolkit used to extract keys to your storage accounts
PROCESS_UNCATEGORIZED
MicroBurst exploitation toolkit used to extract secrets from your Azure key vaults
PROCESS_UNCATEGORIZED
PowerZure exploitation toolkit used to elevate access from Azure AD to Azure
STATUS_UPDATE
PowerZure exploitation toolkit used to enumerate resources
RESOURCE_READ
PowerZure exploitation toolkit used to enumerate storage containers, shares, and tables
RESOURCE_READ
PowerZure exploitation toolkit used to execute a Runbook in your subscription
STATUS_UPDATE
PowerZure exploitation toolkit used to extract Runbooks content
STATUS_UPDATE
PREVIEW - Azurite toolkit run detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious creation of compute resources detected
RESOURCE_CREATION
PREVIEW - Suspicious key vault recovery detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious management session using an inactive account detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Credential Access' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Data Collection' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Defense Evasion' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Execution' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Impact' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Initial Access' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Lateral Movement Access' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'persistence' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious invocation of a high-risk 'Privilege Escalation' operation by a service principal detected
SCAN_UNCATEGORIZED
PREVIEW - Suspicious management session using PowerShell detected
SCAN_UNCATEGORIZED
PREVIEW â€" Suspicious management session using Azure portal detected
SCAN_UNCATEGORIZED
Privileged custom role created for your subscription in a suspicious way (Preview)
SCAN_UNCATEGORIZED
Suspicious Azure role assignment detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Credential Access' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Data Collection' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Defense Evasion' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Execution' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Impact' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Initial Access' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Lateral Movement' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious elevate access operation (Preview)(ARM_AnomalousElevateAccess)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Persistence' operation detected (Preview)
SCAN_UNCATEGORIZED
Suspicious invocation of a high-risk 'Privilege Escalation' operation detected (Preview)
SCAN_UNCATEGORIZED
Usage of MicroBurst exploitation toolkit to run an arbitrary code or exfiltrate Azure Automation account credentials
PROCESS_UNCATEGORIZED
Usage of NetSPI techniques to maintain persistence in your Azure environment
SCAN_UNCATEGORIZED
Usage of PowerZure exploitation toolkit to run an arbitrary code or exfiltrate Azure Automation account credentials
SCAN_UNCATEGORIZED
Usage of PowerZure function to maintain persistence in your Azure environment
SCAN_UNCATEGORIZED
Suspicious classic role assignment detected (Preview)
RESOURCE_PERMISSIONS_CHANGE
Access from a suspicious application
USER_RESOURCE_ACCESS
EXPLOIT
Access from a suspicious IP address
USER_RESOURCE_ACCESS
Phishing content hosted on a storage account
STATUS_UPDATE
Storage account identified as source for distribution of malware
STATUS_UPDATE
The access level of a potentially sensitive storage blob container was changed to allow unauthenticated public access
RESOURCE_PERMISSIONS_CHANGE
Authenticated access from a Tor exit node
USER_RESOURCE_ACCESS
Access from an unusual location to a storage account
USER_RESOURCE_ACCESS
Unusual unauthenticated access to a storage container
USER_RESOURCE_ACCESS
Potential malware uploaded to a storage account
STATUS_UPDATE
Publicly accessible storage containers successfully discovered
STATUS_UPDATE
Publicly accessible storage containers unsuccessfully scanned
STATUS_UPDATE
Unusual access inspection in a storage account
USER_RESOURCE_ACCESS
Unusual amount of data extracted from a storage account
STATUS_UPDATE
Unusual application accessed a storage account
USER_RESOURCE_ACCESS
Unusual data exploration in a storage account
STATUS_UPDATE
Unusual deletion in a storage account
STATUS_UPDATE
Unusual unauthenticated public access to a sensitive blob container (Preview)
USER_RESOURCE_ACCESS
Unusual amount of data extracted from a sensitive blob container (Preview)
STATUS_UPDATE
Unusual number of blobs extracted from a sensitive blob container (Preview)
STATUS_UPDATE
Access from a known suspicious application to a sensitive blob container (Preview)
USER_RESOURCE_ACCESS
Access from a known suspicious IP address to a sensitive blob container (Preview)
USER_RESOURCE_ACCESS
Access from a Tor exit node to a sensitive blob container (Preview)
USER_RESOURCE_ACCESS
Access from an unusual location to a sensitive blob container (Preview)
USER_RESOURCE_ACCESS
The access level of a sensitive storage blob container was changed to allow unauthenticated public access (Preview)
RESOURCE_PERMISSIONS_CHANGE
Suspicious external access to an Azure storage account with overly permissive SAS token (Preview)
USER_RESOURCE_ACCESS
Suspicious external operation to an Azure storage account with overly permissive SAS token (Preview)
USER_RESOURCE_ACCESS
Unusual SAS token was used to access an Azure storage account from a public IP address (Preview)
USER_RESOURCE_ACCESS
Malicious file uploaded to storage account
STATUS_UPDATE
Malicious blob was downloaded from a storage account (Preview)
STATUS_UPDATE
Access from a Tor exit node
USER_RESOURCE_ACCESS
Access from a suspicious IP
USER_RESOURCE_ACCESS
Access from an unusual location
USER_RESOURCE_ACCESS
Unusual volume of data extracted
STATUS_UPDATE
Extraction of Azure Cosmos DB accounts keys via a potentially malicious script
STATUS_UPDATE
Suspicious extraction of Azure Cosmos DB account keys (AzureCosmosDB_SuspiciousListKeys.SuspiciousPrincipal)
STATUS_UPDATE
SQL injection: potential data exfiltration
STATUS_UPDATE
EXPLOIT
SQL injection: fuzzing attempt
STATUS_UPDATE
EXPLOIT
Network communication with a malicious machine detected
NETWORK_UNCATEGORIZED
Possible compromised machine detected
NETWORK_UNCATEGORIZED
Possible incoming %{Service Name} brute force attempts detected
NETWORK_UNCATEGORIZED
Possible incoming SQL brute force attempts detected
NETWORK_UNCATEGORIZED
Possible outgoing denial-of-service attack detected
NETWORK_UNCATEGORIZED
NETWORK_DENIAL_OF_SERVICE
Suspicious incoming RDP network activity from multiple sources
NETWORK_UNCATEGORIZED
Suspicious incoming RDP network activity
NETWORK_UNCATEGORIZED
Suspicious incoming SSH network activity from multiple sources
NETWORK_UNCATEGORIZED
Suspicious incoming SSH network activity
NETWORK_UNCATEGORIZED
Suspicious outgoing %{Attacked Protocol} traffic detected
NETWORK_UNCATEGORIZED
Suspicious outgoing RDP network activity to multiple destinations
NETWORK_UNCATEGORIZED
Suspicious outgoing RDP network activity
NETWORK_UNCATEGORIZED
Suspicious outgoing SSH network activity to multiple destinations
NETWORK_UNCATEGORIZED
Suspicious outgoing SSH network activity
NETWORK_UNCATEGORIZED
Traffic detected from IP addresses recommended for blocking
SCAN_NETWORK
Access from a suspicious IP address to a key vault
USER_RESOURCE_ACCESS
Access from a TOR exit node to a key vault
USER_RESOURCE_ACCESS
High volume of operations in a key vault
USER_UNCATEGORIZED
Suspicious policy change and secret query in a key vault
USER_UNCATEGORIZED
Suspicious secret listing and query in a key vault
USER_UNCATEGORIZED
Unusual access denied - User accessing high volume of key vaults denied
USER_RESOURCE_ACCESS
Unusual access denied - Unusual user accessing key vault denied
USER_RESOURCE_ACCESS
Unusual application accessed a key vault
USER_RESOURCE_ACCESS
Unusual operation pattern in a key vault
USER_UNCATEGORIZED
Unusual user accessed a key vault
USER_RESOURCE_ACCESS
Unusual user-application pair accessed a key vault
USER_RESOURCE_ACCESS
User accessed high volume of key vaults
USER_RESOURCE_ACCESS
Denied access from a suspicious IP to a key vault
USER_RESOURCE_ACCESS
Unusual access to the key vault from a suspicious IP (Non-Microsoft or External)
USER_RESOURCE_ACCESS
DDoS Attack detected for Public IP
SCAN_UNCATEGORIZED
NETWORK_DENIAL_OF_SERVICE
DDoS Attack mitigated for Public IP
STATUS_UPDATE
NETWORK_DENIAL_OF_SERVICE
Suspicious population-level spike in API traffic to an API endpoint
SCAN_UNCATEGORIZED
Suspicious spike in API traffic from a single IP address to an API endpoint
SCAN_UNCATEGORIZED
Unusually large response payload transmitted between a single IP address and an API endpoint
SCAN_UNCATEGORIZED
Unusually large request body transmitted between a single IP address and an API endpoint
SCAN_UNCATEGORIZED
(Preview) Suspicious spike in latency for traffic between a single IP address and an API endpoint
SCAN_UNCATEGORIZED
API requests spray from a single IP address to an unusually large number of distinct API endpoints
NETWORK_UNCATEGORIZED
Parameter enumeration on an API endpoint
NETWORK_UNCATEGORIZED
Distributed parameter enumeration on an API endpoint
NETWORK_UNCATEGORIZED
Parameter value(s) with anomalous data types in an API call
NETWORK_UNCATEGORIZED
Previously unseen parameter used in an API call
NETWORK_UNCATEGORIZED
Access from a Tor exit node to an API endpoint
NETWORK_UNCATEGORIZED
API Endpoint access from suspicious IP
NETWORK_UNCATEGORIZED
Access from an unusual location to a storage blob container
USER_RESOURCE_ACCESS
Potentially Unsafe Action
USER_RESOURCE_ACCESS
Logon by an unfamiliar principal
USER_LOGIN
NT - Download requested by Powershell
USER_UNCATEGORIZED
Logon from an unusual location
USER_UNCATEGORIZED
NT - Anomalous Registry Persistence Value
USER_UNCATEGORIZED
NT - Suspicious powershell command with windowstyle hidden
USER_UNCATEGORIZED
NT - Unauthorized nmap usage
USER_UNCATEGORIZED
NT - Unusual process spawned from Chrome
USER_UNCATEGORIZED
NT - Encoded powershell command executed
USER_UNCATEGORIZED
NT - Powershell command with suspicious reference to AppData subfolder
USER_UNCATEGORIZED
NT - Powershell executing standard input (possible obfuscation)
USER_UNCATEGORIZED
NT - Anomalous bitsadmin transfer request
STATUS_UPDATE
NT - Anomalous reg import command - Rule
STATUS_UPDATE
NT - Anomalous usage of sdbinst.exe - possible shim database persistence
STATUS_UPDATE
NT - Folder name of nonbreaking space detected in commandline. possible Andromeda.
STATUS_UPDATE
NT - Rundll32.exe communicating with proxy
STATUS_UPDATE
NT - LogSource Increasing or Decreasing over Last 4 Hours
STATUS_UPDATE
Azure VWAN Tunnel Down - Run the RRAS Script
STATUS_UPDATE
Security incident with shared process detected
STATUS_UPDATE
Security incident detected on multiple resources
STATUS_UPDATE
Security incident detected
STATUS_UPDATE
PsExec execution detected
USER_UNCATEGORIZED
Field mapping reference: MICROSOFT_GRAPH_ALERT
The following table lists the log fields of the
MICROSOFT_GRAPH_ALERT
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
actorDisplayName
security_result.about.user.user_display_name
If the
actorDisplayName
log field value is
not
equal to
null
, then the
actorDisplayName
log field is mapped to the
security_result.about.user.user_display_name
UDM field.
additionalData
additional.fields [additionalData %{key}]
alertPolicyId
security_result.rule_id
If the
alertPolicyId
log field value is
not
equal to
null
, then the
alertPolicyId
log field is mapped to the
security_result.rule_id
UDM field.
alertWebUrl
metadata.url_back_to_product
assignedTo
security_result.about.user.userid
If the
assignedTo
log field value is
not
equal to
null
, then the
assignedTo
log field is mapped to the
security_result.about.user.userid
UDM field.
category
metadata.product_event_type
category
security_result.summary
classification
security_result.detection_fields[classification]
If the
classification
log field value is
not
equal to
null
, then the
classification
log field is mapped to the
security_result.detection_fields
UDM field.
comments.comment
security_result.about.investigation.comments
comments.createdByDisplayName
security_result.detection_fields[comments_created_by_display_name]
comments.createdDateTime
security_result.detection_fields[comments_created_date_time]
createdDateTime
metadata.event_timestamp
description
metadata.description
description
security_result.description
detectionSource
security_result.detection_fields[detection_source]
evidence.createdDateTime
principal.user.attribute.creation_time
The
evidence.createdDateTime
is mapped to
principal.user.attribute.creation_time
when all of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value doesn't contains any of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.createdDateTime
target.user.attribute.creation_time
The
evidence.createdDateTime
is mapped to
target.user.attribute.creation_time
when all of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value contains one of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.createdDateTime
principal.asset.attribute.creation_time
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)deviceEvidence
, then the
evidence.createdDateTime
log field is mapped to the
principal.asset.attribute.creation_time
UDM field.
evidence.createdDateTime
target.resource_ancestors.attribute.creation_time
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesPodEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence)
, then the
evidence.createdDateTime
log field is mapped to the
target.resource_ancestors.attribute.creation_time
UDM field.
evidence.createdDateTime
target.group.attribute.creation_time
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.createdDateTime
log field is mapped to the
target.group.attribute.creation_time
UDM field.
evidence.createdDateTime
security_result.detection_fields [created_date_time]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(cloudApplicationEvidence or amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence or kubernetesPodEvidence or deviceEvidence or mailClusterEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or analyzedMessageEvidence or securityGroupEvidence or userEvidence or mailboxEvidence or ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.createdDateTime
extracted field is mapped to the
security_result.detection_fields
UDM field.
evidence.remediationStatusDetails
principal.user.attribute.labels [remediation_status_details]
The
evidence.remediationStatusDetails
is mapped to
principal.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value doesn't contains any of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.remediationStatusDetails
target.user.attribute.labels [remediation_status_details]
The
evidence.remediationStatusDetails
is mapped to
target.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value contains one of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.remediationStatusDetails
principal.asset.attribute.labels [remediation_status_details]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)deviceEvidence
, then the
evidence.remediationStatusDetails
log field is mapped to the
principal.asset.attribute.labels
UDM field.
evidence.remediationStatusDetails
target.resource_ancestors.attribute.labels [remediation_status_details]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesPodEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence)
, then the
evidence.remediationStatusDetails
log field is mapped to the
target.resource_ancestors.attribute.labels
UDM field.
evidence.remediationStatusDetails
target.group.attribute.labels [remediation_status_details]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.remediationStatusDetails
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.remediationStatusDetails
security_result.detection_fields [remediation_status_details]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.remediationStatusDetails
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.remediationStatus
principal.user.attribute.labels [remediation_status]
The
evidence.remediationStatus
is mapped to
principal.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value doesn't contains any of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.remediationStatus
target.user.attribute.labels [remediation_status]
The
evidence.remediationStatus
is mapped to
target.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value contains one of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.remediationStatus
principal.asset.attribute.labels [remediation_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)deviceEvidence
, then the
evidence.remediationStatus
log field is mapped to the
principal.asset.attribute.labels
UDM field.
evidence.remediationStatus
target.resource_ancestors.attribute.labels [remediation_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesPodEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence)
, then the
evidence.remediationStatus
log field is mapped to the
target.resource_ancestors.attribute.labels
UDM field.
evidence.remediationStatus
target.group.attribute.labels [remediation_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.remediationStatus
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.remediationStatus
security_result.detection_fields [remediation_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.remediationStatus
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.tags
principal.user.attribute.labels [tags]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, then the
evidence.tags
log field is mapped to the
principal.user.attribute.labels
UDM field.
evidence.tags
target.user.attribute.labels [tags]
The
evidence.tags
is mapped to
target.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value contains one of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.tags
principal.asset.attribute.labels [tags]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)deviceEvidence
, then the
evidence.tags
log field is mapped to the
principal.asset.attribute.labels
UDM field.
evidence.tags
target.resource_ancestors.attribute.labels [tags]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesPodEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence)
, then the
evidence.tags
log field is mapped to the
target.resource_ancestors.attribute.labels
UDM field.
evidence.tags
target.group.attribute.labels [tags]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.tags
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.tags
security_result.detection_fields [tags]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.tags
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.detailedRoles
principal.user.attribute.labels [evidence_detailed_roles]
The
evidence.detailedRoles
is mapped to
principal.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value doesn't contains any of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.detailedRoles
target.user.attribute.labels [evidence_detailed_roles]
The
evidence.detailedRoles
is mapped to
target.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value contains one of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.detailedRoles
principal.asset.attribute.labels [evidence_detailed_roles]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)deviceEvidence
, then the
evidence.detailedRoles
log field is mapped to the
principal.asset.attribute.labels
UDM field.
evidence.detailedRoles
target.resource_ancestors.attribute.labels [evidence_detailed_roles]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesPodEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence)
, then the
evidence.detailedRoles
log field is mapped to the
target.resource_ancestors.attribute.labels
UDM field.
evidence.detailedRoles
target.group.attribute.labels [evidence_detailed_roles]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.detailedRoles
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.detailedRoles
security_result.detection_fields [detailed_roles]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.detailedRoles
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.verdict
principal.user.attribute.labels [verdict]
The
evidence.verdict
is mapped to
principal.user.attribute.labels
when all
  of the following conditions are met:
The
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
If the
title
field value contains one of the following values:
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.verdict
target.user.attribute.labels[verdict]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, and if the
target.user.attribute.labels
log field value is empty, then the
evidence.verdict
log field is mapped to the
target.user.attribute.labels
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.verdict
target.group.attribute.labels [verdict]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.verdict
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.verdict
security_result.detection_fields [verdict]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.verdict
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.roles
principal.user.attribute.roles.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value does not contain one of the following values, then the
evidence.roles
log field is mapped to the
principal.user.attribute.roles.name
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.roles
target.user.attribute.roles.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.roles
log field is mapped to the
target.user.attribute.roles.name
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.roles
principal.asset.attribute.roles.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)deviceEvidence
, then the
evidence.roles
log field is mapped to the
principal.asset.attribute.roles.name
UDM field.
evidence.roles
security_result.detection_fields [roles]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(ipEvidence or mailClusterEvidence or analyzedMessageEvidence or registryKeyEvidence or registryValueEvidence or urlEvidence or fileEvidence or processEvidence)
, then the
evidence.roles
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.roles
target.resource_ancestors.attribute.roles.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(amazonResourceEvidence or azureResourceEvidence or blobContainerEvidence or blobEvidence or googleCloudResourceEvidence or containerEvidence or containerImageEvidence or containerRegistryEvidence or kubernetesClusterEvidence or kubernetesControllerEvidence or kubernetesNamespaceEvidence or kubernetesPodEvidence or kubernetesSecretEvidence or kubernetesServiceAccountEvidence or kubernetesServiceEvidence or oauthApplicationEvidence)
, then The
evidence.roles
log field is mapped to the
target.resource_ancestors.attribute.roles.name
UDM field.
evidence.roles
target.group.attribute.roles.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)securityGroupEvidence
, then the
evidence.roles
log field is mapped to the
target.group.attribute.roles.name
UDM field.
evidence.createdDateTime
target.resource.attribute.creation_time
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)cloudApplicationEvidence
, then the
evidence.createdDateTime
log field is mapped to the
target.resource.attribute.creation_time
UDM field.
evidence.remediationStatusDetails
target.resource.attribute.labels [remediation_status_details]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)cloudApplicationEvidence
, then the
evidence.remediationStatusDetails
log field is mapped to the
target.resource.attribute.labels
UDM field.
evidence.remediationStatus
target.resource.attribute.labels [remediation_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)cloudApplicationEvidence
, then the
evidence.remediationStatus
log field is mapped to the
target.resource.attribute.labels
UDM field.
evidence.tags
target.resource.attribute.labels [tags]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)cloudApplicationEvidence
, then the
evidence.tags
log field is mapped to the
target.resource.attribute.labels
UDM field.
evidence.verdict
target.resource.attribute.labels [verdict]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)cloudApplicationEvidence
, then the
evidence.verdict
log field is mapped to the
target.resource.attribute.labels
UDM field.
evidence.roles
target.resource.attribute.roles.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)cloudApplicationEvidence
, then the
evidence.roles
log field is mapped to the
target.resource.attribute.roles.name
UDM field.
detectorId
security_result.detection_fields[detector_id]
If the
detectorId
log field value is
not
equal to
null
, then the
detectorId
log field is mapped to the
security_result.detection_fields
UDM field.
determination
security_result.detection_fields[determination]
If the
determination
log field value is
not
equal to
null
, then the
determination
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.@odata.type
evidence.azureAdDeviceId
security_result.detection_fields[azure_ad_device_id]
evidence.deviceDnsName
principal.asset.hostname
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, and if the
evidence.deviceDnsName
log field value is
not
empty, then the
principal.asset.hostname
UDM field is mapped to
evidence.deviceDnsName
.
evidence.hostName
principal.asset.hostname
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, and if the
evidence.deviceDnsName
log field value is empty, then the
principal.asset.hostname
UDM field is mapped to
evidence.hostName
.
evidence.deviceDnsName
principal.hostname
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, and if the
evidence.deviceDnsName
log field value is
not
empty, then the
principal.hostname
UDM field is mapped to
evidence.deviceDnsName
.
evidence.hostName
principal.hostname
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, and if the
evidence.deviceDnsName
log field value is empty, then the
principal.hostname
UDM field is mapped to
evidence.hostName
.
evidence.firstSeenDateTime
principal.asset.first_seen_time
principal.asset.deployment_status
The
principal.asset.deployment_status
UDM field is set to one of the following values:
ACTIVE
when the following conditions are met:
The value in the
evidence.healthStatus
field is
active
.
The value in the
evidence.@odata.type
field value matches the regular expression pattern
.*deviceEvidence
DECOMMISSIONED
when the following conditions are met:
The value in the
evidence.healthStatus
field is
inactive
.
The value in the
evidence.@odata.type
field value matches the regular expression pattern
.*deviceEvidence
evidence.healthStatus
principal.asset.attribute.labels[health_status]
evidence.amazonAccountId
target.resource_ancestors.attribute.labels[amazon_account_id]
evidence.amazonResourceId
target.resource_ancestors.product_object_id
evidence.resourceName
target.resource_ancestors.name
evidence.resourceType
target.resource_ancestors.resource_subtype
evidence.cloudResource.amazonAccountId
target.resource_ancestors.attribute.labels[cloud_resource_amazon_account_id]
evidence.cloudResource.amazonResourceId
target.resource_ancestors.attribute.labels[cloud_resource_amazon_resource_id]
evidence.cloudResource.remediationStatus
target.resource_ancestors.attribute.labels[cloud_resource_remediation_status]
evidence.cloudResource.remediationStatusDetails
target.resource_ancestors.attribute.labels[cloud_resource_remediation_status_details]
evidence.cloudResource.roles
target.resource_ancestors.attribute.labels[cloud_resource_roles]
evidence.cloudResource.tags
target.resource_ancestors.attribute.labels[cloud_resource_tags]
evidence.cloudResource.verdict
target.resource_ancestors.attribute.labels[cloud_resource_verdict]
evidence.cluster.cloudResource.amazonAccountId
target.resource_ancestors.attribute.labels[cluster_cloud_resource_amazon_account_id]
evidence.cluster.cloudResource.amazonResourceId
target.resource_ancestors.attribute.labels[cluster_cloud_resource_amazon_resource_id]
evidence.cluster.cloudResource.remediationStatus
target.resource_ancestors.attribute.labels[cluster_cloud_resource_remediation_status]
evidence.cluster.cloudResource.remediationStatusDetails
target.resource_ancestors.attribute.labels[cluster_cloud_resource_remediation_status_details]
evidence.cluster.cloudResource.roles
target.resource_ancestors.attribute.labels[cluster_cloud_resource_roles]
evidence.cluster.cloudResource.tags
target.resource_ancestors.attribute.labels[cluster_cloud_resource_tags]
evidence.cluster.cloudResource.verdict
target.resource_ancestors.attribute.labels[cluster_cloud_resource_verdict]
evidence.namespace.cluster.cloudResource.amazonAccountId
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_amazon_account_id]
evidence.namespace.cluster.cloudResource.amazonResourceId
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_amazon_resource_id]
evidence.namespace.cluster.cloudResource.remediationStatus
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_remediation_status]
evidence.namespace.cluster.cloudResource.remediationStatusDetails
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_remediation_status_details]
evidence.namespace.cluster.cloudResource.resourceName
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_resource_name]
evidence.namespace.cluster.cloudResource.resourceType
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_resource_type]
evidence.namespace.cluster.cloudResource.roles
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_roles]
evidence.namespace.cluster.cloudResource.tags
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_tags]
evidence.namespace.cluster.cloudResource.verdict
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_verdict]
evidence.pod.namespace.cluster.cloudResource.amazonAccountId
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_amazon_account_id]
evidence.pod.namespace.cluster.cloudResource.amazonResourceId
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_amazon_resource_id]
evidence.pod.namespace.cluster.cloudResource.remediationStatus
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_remediation_status]
evidence.pod.namespace.cluster.cloudResource.remediationStatusDetails
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_remediation_status_details]
evidence.pod.namespace.cluster.cloudResource.resourceName
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_resource_name]
evidence.pod.namespace.cluster.cloudResource.resourceType
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_resource_type]
evidence.pod.namespace.cluster.cloudResource.roles
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_roles]
evidence.pod.namespace.cluster.cloudResource.tags
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_tags]
evidence.pod.namespace.cluster.cloudResource.verdict
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_verdict]
evidence.location
target.location.country_or_region
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*googleCloudResourceEvidence
, then the
evidence.location
log field is mapped to the
target.location.country_or_region
UDM field.
evidence.locationType
target.resource_ancestors.attribute.labels[location_type]
evidence.projectId
target.resource_ancestors.attribute.labels[project_id]
evidence.projectNumber
target.resource_ancestors.attribute.labels[project_number]
evidence.resourceId
target.resource_ancestors.product_object_id
evidence.cloudResource.createdDateTime
target.resource_ancestors.attribute.labels[cloud_resource_created_date_time]
evidence.cloudResource.location
target.resource_ancestors.attribute.labels[cloud_resource_location]
evidence.cloudResource.locationType
target.resource_ancestors.attribute.labels[cloud_resource_location_type]
evidence.cloudResource.projectId
target.resource_ancestors.attribute.labels[cloud_resource_project_id]
evidence.cloudResource.projectNumber
target.resource_ancestors.attribute.labels[cloud_resource_project_number]
evidence.cloudResource.resourceId
target.resource_ancestors.attribute.labels[cloud_resource_resource_id]
evidence.cloudResource.resourceName
target.resource_ancestors.attribute.labels[cloud_resource_resource_name]
evidence.cloudResource.resourceType
target.resource_ancestors.attribute.labels[cloud_resource_resource_type]
evidence.cluster.cloudResource.createdDateTime
target.resource_ancestors.attribute.labels[cluster_cloud_resource_created_date_time]
evidence.cluster.cloudResource.location
target.resource_ancestors.attribute.labels[cluster_cloud_resource_location]
evidence.cluster.cloudResource.locationType
target.resource_ancestors.attribute.labels[cluster_cloud_resource_location_type]
evidence.cluster.cloudResource.projectId
target.resource_ancestors.attribute.labels[cluster_cloud_resource_project_id]
evidence.cluster.cloudResource.projectNumber
target.resource_ancestors.attribute.labels[cluster_cloud_resource_project_number]
evidence.cluster.cloudResource.resourceId
target.resource_ancestors.attribute.labels[cluster_cloud_resource_resource_id]
evidence.cluster.cloudResource.resourceName
target.resource_ancestors.attribute.labels[cluster_cloud_resource_resource_name]
evidence.cluster.cloudResource.resourceType
target.resource_ancestors.attribute.labels[cluster_cloud_resource_resource_type]
evidence.namespace.cluster.cloudResource.createdDateTime
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_created_date_time]
evidence.namespace.cluster.cloudResource.location
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_location]
evidence.namespace.cluster.cloudResource.locationType
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_location_type]
evidence.namespace.cluster.cloudResource.projectId
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_project_id]
evidence.namespace.cluster.cloudResource.projectNumber
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_project_number]
evidence.namespace.cluster.cloudResource.resourceId
target.resource_ancestors.attribute.labels[namespace_cluster_cloud_resource_resource_id]
evidence.pod.namespace.cluster.cloudResource.createdDateTime
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_created_date_time]
evidence.pod.namespace.cluster.cloudResource.location
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_location]
evidence.pod.namespace.cluster.cloudResource.locationType
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_location_type]
evidence.pod.namespace.cluster.cloudResource.projectId
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_project_id]
evidence.pod.namespace.cluster.cloudResource.projectNumber
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_project_number]
evidence.pod.namespace.cluster.cloudResource.resourceId
target.resource_ancestors.attribute.labels[pod_namespace_cluster_cloud_resource_resource_id]
evidence.blobContainer.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.fileHashes
target.resource_ancestors.attribute.labels [file_hashes]
evidence.blobContainer.name
target.resource_ancestors.name
evidence.blobContainer.remediationStatus
target.resource_ancestors.attribute.labels [blob_container_remediation_status]
evidence.blobContainer.remediationStatusDetails
target.resource_ancestors.attribute.labels [blob_container_remediation_status_details]
evidence.blobContainer.roles
target.resource_ancestors.attribute.labels [blob_container_roles]
evidence.blobContainer.tags
target.resource_ancestors.attribute.labels [blob_container_tags]
evidence.blobContainer.url
target.resource_ancestors.attribute.labels [blob_container_url]
evidence.blobContainer.verdict
target.resource_ancestors.attribute.labels [blob_container_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*kubernetesNamespaceEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.cluster.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.cluster.distribution
target.resource_ancestors.attribute.labels[cluster_distribution]
evidence.cluster.name
target.resource_ancestors.name
evidence.cluster.platform
target.resource_ancestors.attribute.labels[cluster_platform]
evidence.cluster.remediationStatus
target.resource_ancestors.attribute.labels[cluster_remediation_status]
evidence.cluster.remediationStatusDetails
target.resource_ancestors.attribute.labels[cluster_remediation_status_details]
evidence.cluster.roles
target.resource_ancestors.attribute.roles.name
evidence.cluster.tags
target.resource_ancestors.attribute.labels[cluster_tags]
evidence.cluster.verdict
target.resource_ancestors.attribute.labels[cluster_verdict]
evidence.cluster.version
target.resource_ancestors.attribute.labels[cluster_version]
target.resource_ancestors.resource_type
If the
evidence.cluster.name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
evidence.image.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.image.digestImage
target.resource_ancestors.attribute.labels [image_digest_image]
evidence.image.imageId
target.resource_ancestors.product_object_id
evidence.image.registry.createdDateTime
target.resource_ancestors.attribute.labels [image_registry_created_date_time]
evidence.image.registry.registry
target.resource_ancestors.attribute.labels [image_registry_registry]
evidence.image.registry.remediationStatus
target.resource_ancestors.attribute.labels [image_registry_remediation_status]
evidence.image.registry.remediationStatusDetails
target.resource_ancestors.attribute.labels [image_registry_remediation_status_details]
evidence.image.registry.roles
target.resource_ancestors.attribute.labels [image_registry_roles]
evidence.image.registry.tags
target.resource_ancestors.attribute.labels [image_registry_tags]
evidence.image.registry.verdict
target.resource_ancestors.attribute.labels [image_registry_verdict]
evidence.image.remediationStatus
target.resource_ancestors.attribute.labels [image_remediation_status]
evidence.image.remediationStatusDetails
target.resource_ancestors.attribute.labels [image_remediation_status_details]
evidence.image.roles
target.resource_ancestors.attribute.labels [image_roles]
evidence.image.tags
target.resource_ancestors.attribute.labels [image_tags]
evidence.image.verdict
target.resource_ancestors.attribute.labels [image_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*containerEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
IMAGE
.
evidence.pod.containers.args
target.resource_ancestors.attribute.labels [pod_containers_args]
evidence.pod.containers.command
target.resource_ancestors.attribute.labels [pod_containers_command]
evidence.pod.containers.containerId
target.resource_ancestors.product_object_id
evidence.pod.containers.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.pod.containers.isPrivileged
target.resource_ancestors.attribute.labels [pod_containers_is_privileged]
evidence.pod.containers.name
target.resource_ancestors.name
evidence.pod.containers.remediationStatus
target.resource_ancestors.attribute.labels [pod_containers_remediation_status]
evidence.pod.containers.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_containers_remediation_status_details]
evidence.pod.containers.roles
target.resource_ancestors.attribute.labels [pod_containers_roles]
evidence.pod.containers.tags
target.resource_ancestors.attribute.labels [pod_containers_tags]
evidence.pod.containers.verdict
target.resource_ancestors.attribute.labels [pod_containers_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*containerEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.pod.controller.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.pod.controller.labels
target.resource_ancestors.attribute.labels [pod_controller_labels]
evidence.pod.controller.name
target.resource_ancestors.name
evidence.pod.controller.remediationStatus
target.resource_ancestors.attribute.labels [pod_controller_remediation_status]
evidence.pod.controller.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_controller_remediation_status_details]
evidence.pod.controller.roles
target.resource_ancestors.attribute.labels [pod_controller_roles]
evidence.pod.controller.tags
target.resource_ancestors.attribute.labels [pod_controller_tags]
evidence.pod.controller.type
target.resource_ancestors.resource_subtype
evidence.pod.controller.verdict
target.resource_ancestors.attribute.labels [pod_controller_verdict]
evidence.pod.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.pod.name
target.resource_ancestors.name
evidence.pod.remediationStatus
target.resource_ancestors.attribute.labels [pod_remediation_status]
evidence.pod.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_remediation_status_details]
evidence.pod.roles
target.resource_ancestors.attribute.labels [pod_roles]
evidence.pod.tags
target.resource_ancestors.attribute.labels [pod_tags]
evidence.pod.verdict
target.resource_ancestors.attribute.labels [pod_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*containerEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
POD
.
evidence.pod.ephemeralContainers.args
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_args]
evidence.pod.ephemeralContainers.command
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_command]
evidence.pod.ephemeralContainers.containerId
target.resource_ancestors.product_object_id
evidence.pod.ephemeralContainers.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.pod.ephemeralContainers.isPrivileged
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_is_privileged]
evidence.pod.ephemeralContainers.name
target.resource_ancestors.name
evidence.pod.ephemeralContainers.remediationStatus
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_remediation_status]
evidence.pod.ephemeralContainers.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_remediation_status_details]
evidence.pod.ephemeralContainers.roles
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_roles]
evidence.pod.ephemeralContainers.tags
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_tags]
evidence.pod.ephemeralContainers.verdict
target.resource_ancestors.attribute.labels [pod_ephemeral_containers_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*containerEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.pod.serviceAccount.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.pod.serviceAccount.name
target.resource_ancestors.name
evidence.pod.serviceAccount.remediationStatus
target.resource_ancestors.attribute.labels [pod_service_account_remediation_status]
evidence.pod.serviceAccount.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_service_account_remediation_status_details]
evidence.pod.serviceAccount.roles
target.resource_ancestors.attribute.labels [pod_service_account_roles]
evidence.pod.serviceAccount.tags
target.resource_ancestors.attribute.labels [pod_service_account_tags]
evidence.pod.serviceAccount.verdict
target.resource_ancestors.attribute.labels [pod_service_account_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*containerEvidence
, and if the
evidence.pod.serviceAccount.name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
evidence.pod.initContainers.args
target.resource_ancestors.attribute.labels [pod_init_containers_args]
evidence.pod.initContainers.command
target.resource_ancestors.attribute.labels [pod_init_containers_command]
evidence.pod.initContainers.containerId
target.resource_ancestors.product_object_id
evidence.pod.initContainers.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.pod.initContainers.isPrivileged
target.resource_ancestors.attribute.labels [pod_init_containers_is_privileged]
evidence.pod.initContainers.name
target.resource_ancestors.name
evidence.pod.initContainers.remediationStatus
target.resource_ancestors.attribute.labels [pod_init_containers_remediation_status]
evidence.pod.initContainers.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_init_containers_remediation_status_details]
evidence.pod.initContainers.roles
target.resource_ancestors.attribute.labels [pod_init_containers_roles]
evidence.pod.initContainers.tags
target.resource_ancestors.attribute.labels [pod_init_containers_tags]
evidence.pod.initContainers.verdict
target.resource_ancestors.attribute.labels [pod_init_containers_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*containerEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.containers.args
target.resource_ancestors.attribute.labels [containers_args]
evidence.containers.command
target.resource_ancestors.attribute.labels [containers_command]
evidence.containers.containerId
target.resource_ancestors.product_object_id
evidence.containers.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.containers.isPrivileged
target.resource_ancestors.attribute.labels [containers_is_privileged]
evidence.containers.name
target.resource_ancestors.name
evidence.containers.remediationStatus
target.resource_ancestors.attribute.labels [containers_remediation_status]
evidence.containers.remediationStatusDetails
target.resource_ancestors.attribute.labels [containers_remediation_status_details]
evidence.containers.roles
target.resource_ancestors.attribute.labels [containers_roles]
evidence.containers.tags
target.resource_ancestors.attribute.labels [containers_tags]
evidence.containers.verdict
target.resource_ancestors.attribute.labels [containers_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*kubernetesNamespaceEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.controller.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.controller.name
target.resource_ancestors.name
evidence.controller.remediationStatus
target.resource_ancestors.attribute.labels [controller_remediation_status]
evidence.controller.remediationStatusDetails
target.resource_ancestors.attribute.labels [controller_remediation_status_details]
evidence.controller.roles
target.resource_ancestors.attribute.labels [controller_roles]
evidence.controller.tags
target.resource_ancestors.attribute.labels [controller_tags]
evidence.controller.type
target.resource_ancestors.resource_subtype
evidence.controller.verdict
target.resource_ancestors.attribute.labels [controller_verdict]
evidence.initContainers.args
target.resource_ancestors.attribute.labels [init_containers_args]
evidence.initContainers.command
target.resource_ancestors.attribute.labels [init_containers_command]
evidence.initContainers.containerId
target.resource_ancestors.product_object_id
evidence.initContainers.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.initContainers.isPrivileged
target.resource_ancestors.attribute.labels [init_containers_is_privileged]
evidence.initContainers.name
target.resource_ancestors.name
evidence.initContainers.remediationStatus
target.resource_ancestors.attribute.labels [init_containers_remediation_status]
evidence.initContainers.remediationStatusDetails
target.resource_ancestors.attribute.labels [init_containers_remediation_status_details]
evidence.initContainers.roles
target.resource_ancestors.attribute.labels [init_containers_roles]
evidence.initContainers.tags
target.resource_ancestors.attribute.labels [init_containers_tags]
evidence.initContainers.verdict
target.resource_ancestors.attribute.labels [init_containers_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*kubernetesNamespaceEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.ephemeralContainers.args
target.resource_ancestors.attribute.labels [ephemeral_containers_args]
evidence.ephemeralContainers.command
target.resource_ancestors.attribute.labels [ephemeral_containers_command]
evidence.ephemeralContainers.containerId
target.resource_ancestors.product_object_id
evidence.ephemeralContainers.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.ephemeralContainers.isPrivileged
target.resource_ancestors.attribute.labels [ephemeral_containers_is_privileged]
evidence.ephemeralContainers.name
target.resource_ancestors.name
evidence.ephemeralContainers.remediationStatus
target.resource_ancestors.attribute.labels [ephemeral_containers_remediation_status]
evidence.ephemeralContainers.remediationStatusDetails
target.resource_ancestors.attribute.labels [ephemeral_containers_remediation_status_details]
evidence.ephemeralContainers.roles
target.resource_ancestors.attribute.labels [ephemeral_containers_roles]
evidence.ephemeralContainers.tags
target.resource_ancestors.attribute.labels [ephemeral_containers_tags]
evidence.ephemeralContainers.verdict
target.resource_ancestors.attribute.labels [ephemeral_containers_verdict]
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*kubernetesNamespaceEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
CONTAINER
.
evidence.podIp.countryLetterCode
target.resource_ancestors.attribute.labels [podip_country_letter_code]
evidence.podIp.ipAddress
target.resource_ancestors.attribute.labels [podip_ip_address]
evidence.serviceAccount.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.serviceAccount.name
target.resource_ancestors.name
evidence.serviceAccount.remediationStatus
target.resource_ancestors.attribute.labels [service_account_remediation_status]
evidence.serviceAccount.remediationStatusDetails
target.resource_ancestors.attribute.labels [service_account_remediation_status_details]
evidence.serviceAccount.roles
target.resource_ancestors.attribute.labels [service_account_roles]
evidence.serviceAccount.tags
target.resource_ancestors.attribute.labels [service_account_tags]
evidence.serviceAccount.verdict
target.resource_ancestors.attribute.labels [service_account_verdict]
target.resource_ancestors.resource_type
If the
evi.@odata.type
log field value matches the regular expression pattern
(.*)(kubernetesNamespaceEvidence or kubernetesPodEvidence)
, then the
target.resource_ancestors.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
network.direction
If the
evidence.antiSpamDirection
log field value matches the regular expression pattern
(?i)(inbound)
, then the
network.direction
UDM field is set to
INBOUND
.
Else, If the
evidence.antiSpamDirection
log field value matches the regular expression pattern
(?i)(outbound)
, then the
network.direction
UDM field is set to
OUTBOUND
.
evidence.appId
target.application
If the
index
log field value is equal to
1
, then the
evidence.appId
log field is mapped to the
target.application
UDM field.
evidence.appId
target.resource_ancestors.attribute.labels[app_id]
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*oauthApplicationEvidence or .*cloudApplicationEvidence)
, then the
evidence.appId
log field is mapped to the
target.resource_ancestors.attribute.labels
UDM field.
evidence.args
target.resource_ancestors.attribute.labels[args]
evidence.attachmentsCount
security_result.detection_fields[attachments_count]
evidence.clusterBy
security_result.detection_fields[cluster_by]
evidence.clusterByValue
security_result.detection_fields[cluster_by_value]
evidence.clusterIP.countryLetterCode
about.location.country_or_region
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*kubernetesServiceEvidence
, then the
evidence.clusterIP.countryLetterCode
log field is mapped to the
about.location.country_or_region
UDM field.
evidence.clusterIP.ipAddress
about.ip
evidence.command
target.resource_ancestors.attribute.labels[command]
evidence.containerId
target.resource_ancestors.attribute.labels[container_id]
evidence.countryLetterCode
principal.location.country_or_region
The
protoPayload.metadata.event.eventName.parameter.value
is mapped to
principal.location.country_or_region
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*ipEvidence
The value in the
principal.location.country_or_region
field is
empty
.
The
protoPayload.metadata.event.eventName.parameter.value
is mapped to
about.location.country_or_region
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*ipEvidence
The value in the
principal.location.country_or_region
field is
not empty
.
evidence.defenderAvStatus
security_result.detection_fields [defender_av_status]
evidence.deliveryAction
security_result.detection_fields [delivery_action]
evidence.deliveryLocation
security_result.detection_fields [delivery_location]
evidence.detectionStatus
security_result.detection_fields[detection_status]
evidence.displayName
target.application
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*oauthApplicationEvidence or .*cloudApplicationEvidence)
, then the
evidence.displayName
log field is mapped to the
target.application
UDM field.
evidence.displayName
target.group.group_display_name
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*securityGroupEvidence
, then the
evidence.displayName
log field is mapped to the
target.group.group_display_name
UDM field.
evidence.displayName
principal.user.attribute.labels[display_name]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*mailboxEvidence
, and if the
title
log field value does not contain one of the following values, then the
evidence.displayName
log field is mapped to the
principal.user.attribute.labels
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.displayName
target.user.attribute.labels[display_name]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*mailboxEvidence
, and if the
title
log field value contain one of the following values, then the
evidence.displayName
log field is mapped to the
target.user.attribute.labels
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.distribution
target.resource_ancestors.attribute.labels[distribution]
evidence.emailCount
security_result.detection_fields [email_count]
evidence.externalIPs.countryLetterCode
about.location.country_or_region
evidence.externalIPs.ipAddress
about.ip
evidence.fileDetails.fileName
target.file.names
evidence.fileDetails.filePath
target.file.full_path
evidence.fileDetails.filePublisher
security_result.detection_fields [file_details_file_publisher]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*fileEvidence
, then the
evidence.fileDetails.filePublisher
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.fileDetails.fileSize
target.file.size
evidence.fileDetails.issuer
security_result.detection_fields [file_details_issuer]
evidence.fileDetails.sha1
target.file.sha1
evidence.fileDetails.sha256
target.file.sha256
evidence.fileDetails.signer
security_result.detection_fields [file_details_signer]
evidence.imageFile.fileName
target.process.file.names
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.imageFile.fileName
log field is mapped to the
target.process.file.names
UDM field.
evidence.imageFile.filePath
target.process.file.full_path
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.imageFile.filePath
log field is mapped to the
target.process.file.full_path
UDM field.
evidence.imageFile.filePublisher
security_result.detection_fields [image_file_file_publisher]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.imageFile.filePublisher
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.imageFile.fileSize
target.process.file.size
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.imageFile.fileSize
log field is mapped to the
target.process.file.size
UDM field.
evidence.imageFile.issuer
security_result.detection_fields[image_file_issuer]
evidence.imageFile.sha1
target.process.file.sha1
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.imageFile.sha1
log field is mapped to the
target.process.file.sha1
UDM field.
evidence.imageFile.sha256
target.process.file.sha256
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.imageFile.sha256
log field is mapped to the
target.process.file.sha256
UDM field.
evidence.imageFile.signer
security_result.detection_fields [image_file_signer]
evidence.instanceId
target.resource.product_object_id
evidence.instanceName
target.resource.name
evidence.internetMessageId
principal.network.email.mail_id
evidence.ipAddress
principal.ip
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*ipEvidence)
, then the
evidence.ipAddress
log field is mapped to the
principal.ip
UDM field.
evidence.ipInterfaces
principal.asset.attribute.labels[ip_interfaces]
evidence.isPrivileged
target.resource_ancestors.attribute.labels[is_privileged]
evidence.language
security_result.detection_fields[language]
evidence.location.city
principal.location.city
evidence.location.countryName
principal.location.name
evidence.location.latitude
principal.location.region_coordinates.latitude
evidence.location.longitude
principal.location.region_coordinates.longitude
evidence.location.state
principal.location.state
evidence.loggedOnUsers.accountName
target.user.userid
evidence.loggedOnUsers.domainName
principal.domain.name
evidence.mdeDeviceId
principal.asset.asset_id
evidence.mdeDeviceId
principal.asset_id
security_result.associations.type
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*malwareEvidence)
, then the
security_result.associations.type
UDM field is set to
MALWARE
.
evidence.name
security_result.associations.name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*malwareEvidence)
, then the
evidence.name
log field is mapped to the
security_result.associations.name
UDM field.
evidence.name
target.resource_ancestors.name
evidence.namespace.cluster.createdDateTime
target.resource_ancestors.attribute.labels[namespace_cluster_created_date_time]
evidence.namespace.cluster.distribution
target.resource_ancestors.attribute.labels[namespace_cluster_distribution]
evidence.namespace.cluster.name
target.resource_ancestors.attribute.labels[namespace_cluster_name]
evidence.namespace.cluster.platform
target.resource_ancestors.attribute.labels[namespace_cluster_platform]
evidence.namespace.cluster.remediationStatus
target.resource_ancestors.attribute.labels[namespace_cluster_remediation_status]
evidence.namespace.cluster.remediationStatusDetails
target.resource_ancestors.attribute.labels[namespace_cluster_remediation_status_details]
evidence.namespace.cluster.roles
target.resource_ancestors.attribute.labels[namespace_cluster_roles]
evidence.namespace.cluster.tags
target.resource_ancestors.attribute.labels[namespace_cluster_tags]
evidence.namespace.cluster.verdict
target.resource_ancestors.attribute.labels[namespace_cluster_verdict]
evidence.namespace.cluster.version
target.resource_ancestors.attribute.labels[namespace_cluster_version]
evidence.namespace.createdDateTime
target.resource_ancestors.attribute.labels[namespace_created_date_time]
evidence.namespace.name
target.resource_ancestors.attribute.labels[namespace_name]
evidence.namespace.remediationStatus
target.resource_ancestors.attribute.labels[namespace_remediation_status]
evidence.namespace.remediationStatusDetails
target.resource_ancestors.attribute.labels[namespace_remediation_status_details]
evidence.namespace.roles
target.resource_ancestors.attribute.labels[namespace_roles]
evidence.namespace.tags
target.resource_ancestors.attribute.labels[namespace_tags]
evidence.namespace.verdict
target.resource_ancestors.attribute.labels[namespace_verdict]
evidence.networkMessageId
security_result.detection_fields[network_message_id]
evidence.networkMessageIds
security_result.detection_fields[network_message_ids]
evidence.objectId
target.resource.product_object_id
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*oauthApplicationEvidence or .*cloudApplicationEvidence)
, then the
evidence.objectId
log field is mapped to the
target.resource.product_object_id
UDM field.
evidence.onboardingStatus
principal.asset.attribute.labels [onboarding_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, then the
evidence.onboardingStatus
log field is mapped to the
principal.asset.attribute.labels
UDM field.
evidence.osBuild
principal.asset.platform_software.platform_patch_level
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, then the
evidence.osBuild
log field is mapped to the
principal.asset.platform_software.platform_patch_level
UDM field.
evidence.osBuild
principal.platform_patch_level
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, then the
evidence.osBuild
log field is mapped to the
principal.platform_patch_level
UDM field.
principal.platform
The
principal.platform
UDM field is set to one of the following values:
WINDOWS
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)win
MAC
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)mac
LINUX
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)lin
ANDROID
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)android
IOS
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)ios
principal.asset.platform_software.platform
The
principal.asset.platform_software.platform
UDM field is set to one of the following values:
WINDOWS
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)win
MAC
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)mac
LINUX
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)lin
ANDROID
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)android
IOS
when the following conditions are met:
The value in the
evidence.@odata.type
field matches the regular expression pattern
.*deviceEvidence
The value in the
evidence.osPlatform
field matches the regular expression pattern
(?i)ios
evidence.osPlatform
principal.asset.attribute.labels[os_platform]
evidence.p1Sender.displayName
security_result.about.user.user_display_name
If the
evidence.p2Sender.displayName
log field value does not match the regular expression pattern
^.+@.+$
, then the
evidence.p1Sender.displayName
log field is mapped to the
security_result.about.user.user_display_name
UDM field.
evidence.p1Sender.displayName
security_result.about.user.email_addresses
evidence.p1Sender.domainName
security_result.about.domain.name
evidence.p1Sender.emailAddress
security_result.about.network.email.from
evidence.p2Sender.displayName
security_result.about.user.user_display_name
If the
evidence.p2Sender.displayName
log field value does not match the regular expression pattern
^.+@.+$
, then the
evidence.p2Sender.displayName
log field is mapped to the
security_result.about.user.user_display_name
UDM field.
evidence.p2Sender.displayName
security_result.about.user.email_addresses
evidence.p2Sender.domainName
security_result.about.domain.name
evidence.p2Sender.emailAddress
security_result.about.network.email.from
evidence.parentProcessCreationDateTime
security_result.detection_fields[parent_process_creation_date_time]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.parentProcessCreationDateTime
log field is mapped to the
security_result.detection_fields
UDM field.
evidence.parentProcessId
target.process.parent_process.pid
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.parentProcessId
log field is mapped to the
target.process.parent_process.pid
UDM field.
evidence.parentProcessImageFile.fileName
target.process.parent_process.file.names
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.parentProcessImageFile.fileName
log field is mapped to the
target.process.parent_process.file.names
UDM field.
evidence.parentProcessImageFile.filePath
target.process.parent_process.file.full_path
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.parentProcessImageFile.filePath
log field is mapped to the
target.process.parent_process.file.full_path
UDM field.
evidence.parentProcessImageFile.filePublisher
security_result.detection_fields [parent_process_image_file_file_publisher]
evidence.parentProcessImageFile.fileSize
target.process.parent_process.file.size
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*processEvidence
, then the
evidence.parentProcessImageFile.fileSize
log field is mapped to the
target.process.parent_process.file.size
UDM field.
evidence.parentProcessImageFile.issuer
security_result.detection_fields [parent_process_image_file_issuer]
evidence.parentProcessImageFile.sha1
target.process.parent_process.file.sha1
evidence.parentProcessImageFile.sha256
target.process.parent_process.file.sha256
evidence.parentProcessImageFile.signer
security_result.detection_fields [parent_process_image_file_signer]
evidence.platform
target.resource_ancestors.attribute.labels [platform]
evidence.pod.namespace.cluster.createdDateTime
target.resource_ancestors.attribute.labels[pod_namespace_cluster_created_date_time]
evidence.pod.namespace.cluster.distribution
target.resource_ancestors.attribute.labels[pod_namespace_cluster_distribution]
evidence.pod.namespace.cluster.name
target.resource_ancestors.attribute.labels[pod_namespace_cluster_name]
evidence.pod.namespace.cluster.platform
target.resource_ancestors.attribute.labels[pod_namespace_cluster_platform]
evidence.pod.namespace.cluster.remediationStatus
target.resource_ancestors.attribute.labels[pod_namespace_cluster_remediation_status]
evidence.pod.namespace.cluster.remediationStatusDetails
target.resource_ancestors.attribute.labels[pod_namespace_cluster_remediation_status_details]
evidence.pod.namespace.cluster.roles
target.resource_ancestors.attribute.labels[pod_namespace_cluster_roles]
evidence.pod.namespace.cluster.tags
target.resource_ancestors.attribute.labels[pod_namespace_cluster_tags]
evidence.pod.namespace.cluster.verdict
target.resource_ancestors.attribute.labels[pod_namespace_cluster_verdict]
evidence.pod.namespace.cluster.version
target.resource_ancestors.attribute.labels[pod_namespace_cluster_version]
evidence.pod.namespace.createdDateTime
target.resource_ancestors.attribute.labels[pod_namespace_created_date_time]
evidence.pod.namespace.name
target.resource_ancestors.attribute.labels[pod_namespace_name]
evidence.pod.namespace.remediationStatus
target.resource_ancestors.attribute.labels[pod_namespace_remediation_status]
evidence.pod.namespace.remediationStatusDetails
target.resource_ancestors.attribute.labels[pod_namespace_remediation_status_details]
evidence.pod.namespace.roles
target.resource_ancestors.attribute.labels[pod_namespace_roles]
evidence.pod.namespace.tags
target.resource_ancestors.attribute.labels[pod_namespace_tags]
evidence.pod.namespace.verdict
target.resource_ancestors.attribute.labels[pod_namespace_verdict]
evidence.pod.podIp.countryLetterCode
target.resource_ancestors.attribute.labels [pod_pod_ip_country_letter_code]
evidence.pod.podIp.ipAddress
target.resource_ancestors.attribute.labels [pod_pod_ip_ip_address]
evidence.primaryAddress
principal.user.email_addresses
If the
evidence.primaryAddress
log field value matches the regular expression pattern
^.+@.+$
, and if the
title
log field value does not contain one of the following values, then the
evidence.primaryAddress
log field is mapped to the
principal.user.email_addresses
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.primaryAddress
target.user.email_addresses
If the
evidence.primaryAddress
log field value matches the regular expression pattern
^.+@.+$
, and if the
title
log field value contain one of the following values, then the
evidence.primaryAddress
log field is mapped to the
target.user.email_addresses
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.primaryAddress
principal.user.attribute.labels[primary_address]
If the
evidence.primaryAddress
log field value does not match the regular expression pattern
^.+@.+$
, and if the
title
log field value does not contain one of the following values, then the
evidence.primaryAddress
log field is mapped to the
principal.user.attribute.labels
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.primaryAddress
target.user.attribute.labels[primary_address]
If the
evidence.primaryAddress
log field value does not match the regular expression pattern
^.+@.+$
, and if the
title
log field value contain one of the following values, then the
evidence.primaryAddress
log field is mapped to the
target.user.attribute.labels
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.processCommandLine
target.process.command_line
evidence.processCreationDateTime
security_result.detection_fields [process_creation_date_time]
evidence.processId
target.process.pid
The
evidence.processId
is mapped to
target.process.pid
when the following conditions are met:
The value in the
evidence.@odata.type
field value matches the regular expression pattern
.*processEvidence
The value in the
target.process.pid
field value is
empty
.
The
evidence.processId
is mapped to
about.process.pid
when the following conditions are met:
The value in the
evidence.@odata.type
field value matches the regular expression pattern
.*processEvidence
The value in the
target.process.pid
field value is
not empty
.
evidence.publisher
target.resource_ancestors.attribute.labels[publisher]
evidence.query
security_result.detection_fields[query]
evidence.rbacGroupId
security_result.detection_fields[rbac_group_id]
evidence.rbacGroupName
security_result.detection_fields[rbac_group_name]
evidence.receivedDateTime
security_result.detection_fields[received_date_time]
evidence.recipientEmailAddress
principal.network.email.to
evidence.registry.createdDateTime
target.resource_ancestors.attribute.labels[registry_created_date_time]
evidence.registry.registry
target.resource_ancestors.attribute.labels[registry_registry]
evidence.registry.remediationStatus
target.resource_ancestors.attribute.labels[registry_remediation_status]
evidence.registry.remediationStatusDetails
target.resource_ancestors.attribute.labels[registry_remediation_status_details]
evidence.registry.roles
target.resource_ancestors.attribute.labels[registry_roles]
evidence.registry.tags
target.resource_ancestors.attribute.labels[registry_tags]
evidence.registry.verdict
target.resource_ancestors.attribute.labels[registry_verdict]
evidence.registry
target.resource_ancestors.attribute.labels[registry]
evidence.registryHive
security_result.detection_fields[registry_hive]
evidence.registryKey
target.registry.registry_key
evidence.registryValue
target.registry.registry_value_data
evidence.registryValueName
target.registry.registry_value_name
evidence.registryValueType
security_result.detection_fields [registry_value_type]
evidence.remediationStatus
target.group.attribute.labels[remediation_status]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*securityGroupEvidence
, then the
evidence.remediationStatus
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.remediationStatus
target.resource_ancestors.attribute.labels[remediation_status]
evidence.remediationStatusDetails
target.group.attribute.labels[remediation_status_details]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*securityGroupEvidence
, then the
evidence.remediationStatusDetails
log field is mapped to the
target.group.attribute.labels
UDM field.
evidence.remediationStatusDetails
target.resource_ancestors.attribute.labels[remediation_status_details]
evidence.riskScore
security_result.detection_fields[risk_score]
evidence.saasAppId
target.resource.attribute.labels[saas_app_id]
evidence.secretType
target.resource_ancestors.attribute.labels[secret_type]
evidence.securityGroupId
target.group.product_object_id
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*securityGroupEvidence
, then the
evidence.securityGroupId
log field is mapped to the
target.group.product_object_id
UDM field.
evidence.senderIp
principal.ip
evidence.servicePorts.appProtocol
about.security_result.detection_fields [service_ports_app_protocol]
evidence.servicePorts.name
about.security_result.detection_fields [service_ports_name]
evidence.servicePorts.nodePort
about.security_result.detection_fields [service_ports_node_port]
evidence.servicePorts.port
about.port
evidence.servicePorts.protocol
about.network.ip_protocol
evidence.servicePorts.targetPort
about.security_result.detection_fields [service_ports_target_port]
evidence.serviceType
target.resource_ancestors.attribute.labels[service_type]
evidence.storageResource.createdDateTime
target.resource_ancestors.attribute.labels[storage_resource_created_date_time]
evidence.storageResource.detailedRoles
target.resource_ancestors.attribute.labels[storage_resource_detailed_roles]
evidence.storageResource.remediationStatus
target.resource_ancestors.attribute.labels[storage_resource_remediation_status]
evidence.storageResource.remediationStatusDetails
target.resource_ancestors.attribute.labels[storage_resource_remediation_status_details]
evidence.storageResource.resourceId
target.resource_ancestors.attribute.labels[storage_resource_resource_id]
evidence.storageResource.resourceName
target.resource_ancestors.attribute.labels[storage_resource_resource_name]
evidence.storageResource.resourceType
target.resource_ancestors.attribute.labels[storage_resource_resource_type]
evidence.storageResource.roles
target.resource_ancestors.attribute.labels[storage_resource_roles]
evidence.storageResource.tags
target.resource_ancestors.attribute.labels[storage_resource_tags]
evidence.storageResource.verdict
target.resource_ancestors.attribute.labels[storage_resource_verdict]
evidence.subject
principal.network.email.subject
evidence.threatDetectionMethods
security_result.detection_fields[threat_detection_methods]
evidence.threats
security_result.detection_fields[threats]
evidence.type
security_result.detection_fields[type]
evidence.url
target.url
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*urlEvidence
, then the
evidence.url
log field is mapped to the
target.url
UDM field.
evidence.url
target.resource_ancestors.attribute.labels[url]
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*blobContainerEvidence
, then the
evidence.url
log field is mapped to the
target.resource_ancestors.attribute.labels
UDM field.
evidence.urlCount
security_result.detection_fields[url_count]
evidence.urls
security_result.detection_fields[urls]
evidence.urn
security_result.detection_fields[urn]
evidence.userAccount.accountName
principal.user.userid
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value does not contain one of the following values, then the
evidence.userAccount.accountName
log field is mapped to the
principal.user.userid
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.accountName
target.user.userid
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.userAccount.accountName
log field is mapped to the
target.user.userid
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.azureAdUserId
principal.user.product_object_id
If the
title
log field value does not contain one of the following values, then the
evidence.userAccount.azureAdUserId
log field is mapped to the
principal.user.product_object_id
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.azureAdUserId
target.user.product_object_id
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.userAccount.azureAdUserId
log field is mapped to the
target.user.product_object_id
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.displayName
principal.user.user_display_name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value does not contain one of the following values, then the
evidence.userAccount.displayName
log field is mapped to the
principal.user.user_display_name
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.displayName
target.user.user_display_name
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.userAccount.displayName
log field is mapped to the
target.user.user_display_name
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.domainName
principal.administrative_domain
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value does not contain one of the following values, then the
evidence.userAccount.domainName
log field is mapped to the
principal.administrative_domain
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.domainName
target.administrative_domain
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.userAccount.domainName
log field is mapped to the
target.administrative_domain
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.userPrincipalName
principal.user.email_addresses
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value does not contain one of the following values, then the
evidence.userAccount.userPrincipalName
log field is mapped to the
principal.user.email_addresses
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.userPrincipalName
target.user.email_addresses
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.userAccount.userPrincipalName
log field is mapped to the
target.user.email_addresses
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.userSid
principal.user.windows_sid
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value does not contain one of the following values, then the
evidence.userAccount.userSid
log field is mapped to the
principal.user.windows_sid
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.userAccount.userSid
target.user.windows_sid
If the
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(userEvidence or mailboxEvidence)
, and if the
title
log field value contain one of the following values, then the
evidence.userAccount.userSid
log field is mapped to the
target.user.windows_sid
UDM field.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
evidence.version
principal.asset.platform_software.platform_version
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, then the
evidence.osPlatform
,
evidence.version
,
evidence.osBuild
log field is mapped to the
principal.asset.platform_software.platform_version
UDM field.
evidence.version
principal.platform_version
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*deviceEvidence
, then the
evidence.osPlatform
,
evidence.version
,
evidence.osBuild
log field is mapped to the
principal.platform_version
UDM field.
evidence.version
target.resource_ancestors.attribute.labels[version]
evidence.vmMetadata.cloudProvider
principal.asset.attribute.labels[vm_metadata_cloud_provider]
evidence.vmMetadata.resourceId
principal.asset.product_object_id
evidence.vmMetadata.subscriptionId
principal.asset.attribute.labels[vm_metadata_subscription_id]
evidence.vmMetadata.vmId
principal.asset.attribute.labels[vm_metadata_vm_id]
firstActivityDateTime
security_result.first_discovered_time
id
metadata.product_log_id
incidentId
security_result.detection_fields[incident_id]
incidentWebUrl
security_result.url_back_to_product
lastActivityDateTime
security_result.last_discovered_time
lastUpdateDateTime
security_result.last_updated_time
mitreTechniques
security_result.attack_details.techniques.id
mitreTechniques
security_result.attack_details.techniques.name
productName
metadata.product_name
providerAlertId
additional.fields[provider_alert_id]
recommendedActions
security_result.action_details
resolvedDateTime
security_result.detection_fields[resolved_date_time]
If the
resolvedDateTime
log field value is
not
equal to
null
, then the
resolvedDateTime
log field is mapped to the
security_result.detection_fields
UDM field.
serviceSource
additional.fields[service_source]
severity
security_result.severity
status
security_result.detection_fields[status]
systemTags
security_result.detection_fields[system_tags]
The
systemTags
log field is mapped to the
security_result.detection_fields
UDM field.
tenantId
metadata.product_deployment_id
threatDisplayName
security_result.threat_name
If the
threatDisplayName
log field value is
not
equal to
null
, then the
threatDisplayName
log field is mapped to the
security_result.threat_name
UDM field.
threatFamilyName
security_result.threat_feed_name
If the
threatFamilyName
log field value is
not
equal to
null
, then the
threatFamilyName
log field is mapped to the
security_result.threat_feed_name
UDM field.
title
security_result.rule_name
target.resource_ancestors.resource_type
If the
evidence.@odata.type
log field value matches the regular expression pattern
.*blobEvidence
, then the
target.resource_ancestors.resource_type
UDM field is set to
STORAGE_OBJECT
.
evidence.blobContainer.storageResource.createdDateTime
target.resource_ancestors.attribute.creation_time
evidence.blobContainer.storageResource.remediationStatus
target.resource_ancestors.attribute.labels [pod_storage_resource_remediation_status]
evidence.blobContainer.storageResource.remediationStatusDetails
target.resource_ancestors.attribute.labels [pod_storage_resource_remediation_status_details]
evidence.blobContainer.storageResource.resourceId
target.resource_ancestors.product_object_id
evidence.blobContainer.storageResource.resourceName
target.resource_ancestors.name
evidence.blobContainer.storageResource.resourceType
target.resource_ancestors.resource_subtype
evidence.blobContainer.storageResource.verdict
target.resource_ancestors.attribute.labels [pod_storage_resource_verdict]
evidence.category
security_result.detection_fields[category]
evidence.destinationPort
target.port
evidence.etag
target.resource_ancestors.attribute.labels[etag]
evidence.files.createdDateTime
security_result.detection_fields [files_created_date_time]
evidence.files.detectionStatus
security_result.detection_fields [files_detection_status]
evidence.files.fileDetails.fileName
target.file.names
evidence.files.fileDetails.filePath
target.file.full_path
evidence.files.fileDetails.filePublisher
security_result.detection_fields [files_file_details_file_publisher]
evidence.files.fileDetails.fileSize
target.file.size
evidence.files.fileDetails.issuer
security_result.detection_fields [files_file_details_issuer]
evidence.files.fileDetails.sha1
target.file.sha1
evidence.files.fileDetails.sha256
target.file.sha256
evidence.files.fileDetails.signer
security_result.detection_fields [files_file_details_signer]
evidence.files.mdeDeviceId
security_result.detection_fields [files_mde_device_id]
evidence.files.remediationStatus
security_result.detection_fields [files_remediation_status]
evidence.files.remediationStatusDetails
security_result.detection_fields [files_remediation_status_details]
evidence.files.verdict
security_result.detection_fields [files_verdict]
evidence.fullResourceName
target.resource_ancestors.attribute.labels[full_resource_name]
evidence.imageId
target.resource_ancestors.attribute.labels[image_id]
evidence.protocol
network.ip_protocol
evidence.sourceAddress.countryLetterCode
security_result.detection_fields[source_address_country_letter_code]
evidence.sourceAddress.createdDateTime
security_result.detection_fields[source_address_created_date_time]
evidence.sourceAddress.ipAddress
security_result.about.ip
evidence.sourceAddress.location.city
security_result.about.location.city
evidence.sourceAddress.location.countryName
security_result.about.location.name
evidence.sourceAddress.location.latitude
security_result.about.location.region_coordinates.latitude
evidence.sourceAddress.location.longitude
security_result.about.location.region_coordinates.longitude
evidence.sourceAddress.location.state
security_result.about.location.state
evidence.sourceAddress.remediationStatus
security_result.detection_fields[source_address_remediation_status]
evidence.sourceAddress.remediationStatusDetails
security_result.detection_fields[source_address_remediation_status_details]
evidence.sourceAddress.stream
security_result.detection_fields[source_address_stream]
evidence.sourceAddress.verdict
security_result.detection_fields[source_address_verdict]
evidence.sourcePort
principal.port
evidence.stream.name
target.resource.attribute.labels[stream_name]
evidence.algorithm
security_result.detection_fields[algorithm]
evidence.value
security_result.detection_fields[value]
evidence.lastExternalIpAddress
principal.asset.attribute.labels[last_external_ip_address]
security_result.action
The
evidence.serviceSource
log field is
microsoftDefenderForEndpoint
and
evidence.@odata.type
log field value matches the regular expression pattern
(.*)(fileEvidence or processEvidence)
If
evidence.detectionStatus
is
prevented or blocked
then the
security_result.action
UDM field is set to
BLOCK
.
If
evidence.detectionStatus
is
detected
:
If the
title
log field value matches the regular expression pattern
(.*)(block|prevented|denied|declined)
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, the
security_result.action
UDM field is set to
ALLOW
.
security_result.action
If the
title
log field value matches the regular expression pattern
(malware was blocked or Unsanctioned cloud app access was blocked or Activity from an anonymous proxy or Network - NT - Possible Ursnif/Gozi Phish or Network - SSH Potential Brute Force or Multiple failed login attempts or Brute force attack against Azure Portal or Block download based on real-time content inspection)
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, If the
title
log field value matches the regular expression pattern
(Failed SSH brute force attack)
, then the
security_result.action
UDM field is set to
FAIL
.
Else, If the
title
log field value contain one of the following values, then the
security_result.action
UDM field is set to
ALLOW
.
Mass delete
Multiple delete VM activities
Else, If the
title
log field value matches the regular expression pattern
(.*)(block|prevented|denied|declined)
, then the
security_result.action
UDM field is set to
BLOCK
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Microsoft
.
principal.hostname
The
src_host
field is extracted from
description
log field using the Grok pattern and the
src_host
extracted field is mapped to the
principal.hostname
UDM field.
principal.asset.hostname
The
src_host
field is extracted from
description
log field using the Grok pattern and the
src_host
extracted field is mapped to the
principal.asset.hostname
UDM field.
extensions.auth.type
If the
title
log field value contain one of the following values, then the
extensions.auth.type
UDM field is set to
AUTHTYPE_UNSPECIFIED
.
Malware linked IP address
Unfamiliar sign-in properties
Malicious IP address
Anonymous IP address
Verified threat actor IP
Suspected Brute Force attack (LDAP)
Suspected Brute Force attack (Kerberos, NTLM)
Abnormal Active Directory Federation Services (AD FS) authentication using a suspicious certificate
Suspected DFSCoerce attack using Distributed File System Protocol
Multiple failed login attempts
Activity from a TOR IP address
Anomalous SSH login detected
Azure High Risk User account - Signin
Brute force attack against Azure Portal
Identity - Attempts to sign in to disabled accounts
Network - SSH Potential Brute Force
A logon from a malicious IP has been detected. [seen multiple times]
Successful brute force attack
Failed SSH brute force attack
Successful SSH brute force attack
Attempted logon by a potentially harmful application
Log on from an unusual Azure Data Center
Log on from an unusual location
Login from a principal user not seen in 60 days
Login from a domain not seen in 60 days
Login from a suspicious IP
Suspected brute force attack using a valid user
Suspected brute force attack
Suspected successful brute force attack
Logon from an unusual cloud provider
Logon by an unfamiliar principal
network.application_protocol
If the
title
log field value is equal to
Network - Rare RDP Connections
, then the
network.application_protocol
UDM field is set to
RDP
.
security_result.alert_state
The
security_result.alert_state
UDM field is set to
ALERTING
.
security_result.attack_details.tactics.name
If the
title
log field value contain one of the following values, then the
security_result.attack_details.techniques.id
UDM field is set to
T1530 and T1567
values and the
security_result.attack_details.tactics.name
UDM field is set to
Exfiltration
.
Mass download by a single user
Mass delete
Mass share
Data exfiltration to an app that is not sanctioned
Else, If the
title
log field value contain one of the following values, then the
security_result.attack_details.techniques.id
UDM field is set to
T1078
.
Activity by terminated user
Suspicious administrative activity
UserAccessAdministrator-Flag
Else, If the
title
log field value contain one of the following values, then the
security_result.attack_details.techniques.id
UDM field is set to
T1090
.
Activity from a Tor IP address
Activity from infrequent country
Impossible travel activity
Login from unfriendly country
Else, If the
title
log field value contain one of the following values, then the
security_result.attack_details.techniques.id
UDM field is set to
T1098
.
Add user to GitHub repo
OAuth Application granted Sharepoint Sites.ReadWrite.All exessive permission
Role added or removed from a User
Unusual addition of credentials to an OAuth app
Else, If the
title
log field value contain one of the following values, then the
security_result.attack_details.techniques.id
UDM field is set to
T1589
.
IR - Multiple failed user log on attempts to an app within 2 minutes
Multiple failed login attempts
Multiple failed user logon attempts to a service
Else, If the
title
log field value is equal to
Failed login for admin account
, then the
security_result.attack_details.techniques.id
UDM field is set to
T1589
and the
security_result.attack_details.techniques.id
UDM field is set to
T1110
and the
security_result.attack_details.tactics.name
UDM field is set to
CredentialAccess
.
Else, If the
title
log field value is equal to
New risky app
, then the
security_result.attack_details.techniques.id
UDM field is set to
T1199
.
Else, If the
title
log field value is equal to
Creation of forwarding/redirect rule
, then the
security_result.attack_details.techniques.id
UDM field is set to
T1137
.
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Reconnaissance
.
T1595
T1592
T1589
T1590
T1591
T1598
T1597
T1596
T1593
T1594
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
ResourceDevelopment
.
T1583
T1586
T1584
T1587
T1585
T1588
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
InitialAccess
.
T1189
T1190
T1133
T1200
T1566
T1091
T1195
T1199
T1078
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Execution
.
T1059
T1203
T1559
T1106
T1053
T1129
T1072
T1569
T1204
T1047
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Persistence
.
T1098
T1197
T1547
T1037
T1176
T1554
T1136
T1543
T1546
T1133
T1574
T1525
T1137
T1542
T1053
T1505
T1205
T1078
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
PrivilegeEscalation
.
T1548
T1134
T1547
T1037
T1543
T1484
T1546
T1068
T1574
T1055
T1053
T1078
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
DefenseEvasion
.
T1548
T1134
T1197
T1140
T1006
T1484
T1480
T1211
T1222
T1564
T1574
T1562
T1070
T1202
T1036
T1556
T1578
T1112
T1601
T1599
T1027
T1542
T1055
T1207
T1014
T1218
T1216
T1553
T1221
T1205
T1127
T1535
T1550
T1078
T1497
T1600
T1220
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
CredentialAccess
.
T1110
T1555
T1212
T1187
T1606
T1056
T1557
T1556
T1040
T1003
T1528
T1558
T1539
T1111
T1552
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Discovery
.
T1087
T1010
T1217
T1580
T1538
T1526
T1482
T1083
T1046
T1135
T1040
T1201
T1120
T1069
T1057
T1012
T1018
T1518
T1082
T1016
T1049
T1033
T1007
T1124
T1497
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
LateralMovement
.
T1210
T1534
T1570
T1563
T1021
T1091
T1072
T1080
T1550
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Collection
.
T1560
T1123
T1119
T1115
T1530
T1602
T1213
T1005
T1039
T1025
T1074
T1114
T1056
T1185
T1557
T1113
T1125
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
CommandAndControl
.
T1071
T1092
T1132
T1001
T1568
T1573
T1008
T1105
T1104
T1095
T1571
T1572
T1090
T1219
T1205
T1102
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Exfiltration
.
T1020
T1030
T1048
T1041
T1011
T1052
T1567
T1029
T1537
If the
mitre_technique_data.id
log field value contain one of the following values, then the
security_result.attack_details.tactics.name
UDM field is set to
Impact
.
T1531
T1485
T1486
T1565
T1491
T1561
T1499
T1495
T1490
T1498
T1496
T1489
T1529
evidence.userAgent
network.http.user_agent
If
evidence.@odata.type
log field value matches the regular expression pattern
.*cloudLogonSessionEvidence
then the
evidence.userAgent
log field is mapped to the
network.http.user_agent
UDM field.
What's next
Data ingestion to Google SecOps
Need more help?
Get answers from Community members and Google SecOps professionals.
