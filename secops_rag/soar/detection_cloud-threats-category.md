# Cloud Threats category overview

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category/  
**Scraped:** 2026-03-05T10:04:34.675415Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Cloud Threats category overview
Supported in:
Google secops
SIEM
This document provides an overview of the rule sets in the Cloud Threats category, the
required data sources, and configuration you can use to tune the alerts generated
by each rule set. These rule sets help identify threats in Google Cloud
environments using Google Cloud data and in AWS environments using AWS data.
Rule set descriptions
The following rule sets are available in the Cloud Threats category.
Rule sets for Google Cloud data
Rule sets for AWS data
Rule sets for Azure data
Rule sets for Office 365 data
Rule sets for Okta data
The
CDIR
abbreviation stands for
Cloud Detection, Investigation, and Response
.
Curated detections for Google Cloud data
Google Cloud rule sets help identify threats in Google Cloud environments using event
and context data, and includes the following rule sets:
Admin Action
: Activity associated with administrative actions, deemed
suspicious but potentially legitimate depending on organizational use.
CDIR SCC Enhanced Exfiltration
: Contains context-aware rules that correlate
Security Command Center Exfiltration findings with other log sources, including Cloud Audit Logs
logs, Sensitive Data Protection context, BigQuery context and Security Command Center
Misconfiguration logs.
CDIR SCC Enhanced Defense Evasion
: Contains context-aware rules that correlate
Security Command Center Evasion or Defense Evasion findings with data from other
Google Cloud data sources, including Cloud Audit Logs.
CDIR SCC Enhanced Malware
: Contains context-aware rules that correlate
Security Command Center Malware findings with data, including the occurrence of IP
addresses and domains and their prevalence scores, in addition to other data
sources, including Cloud DNS logs.
CDIR SCC Enhanced Persistence
: Contains context-aware rules that correlate
Security Command Center Persistence findings with data from sources, including Cloud DNS
logs and IAM analysis logs.
CDIR SCC Enhanced Privilege Escalation
: Contains context-aware rules that correlate
Security Command Center Privilege escalation findings with data from several other
data sources, including Cloud Audit Logs.
CDIR SCC Credential Access
: Contains context-aware rules that correlate
Security Command Center Credential Access findings with data from several other
data sources, including Cloud Audit Logs
CDIR SCC Enhanced Discovery
: Contains context-aware rules that correlate
Security Command Center Discovery escalation findings with data from sources such
as Google Cloud services and Cloud Audit Logs.
CDIR SCC Brute Force
: Contains context-aware rules that correlate Security Command Center
Brute Force escalation findings with data, including Cloud DNS logs.
CDIR SCC Data Destruction
: Contains context-aware rules that correlate Security Command Center
Data Destruction escalation findings with data from several other data sources, including Cloud Audit Logs.
CDIR SCC Inhibit System Recovery
: Contains context-aware rules that correlate Security Command Center
Inhibit System Recovery findings with data from several other data sources, including Cloud Audit Logs.
CDIR SCC Execution
: Contains context-aware rules that correlate Security Command Center
Execution findings with data from several other data sources, including Cloud Audit Logs.
CDIR SCC Initial Access
: Contains context-aware rules that correlate Security Command Center
Initial Access findings with data from several other data sources, including Cloud Audit Logs.
CDIR SCC Impair Defenses
: Contains context-aware rules that correlate Security Command Center
Impair Defenses findings with data from several other data sources, including Cloud Audit Logs.
CDIR SCC Impact
: Contains rules that detect
Impact
findings from Security Command Center with a Critical, High, Medium, and Low severity classification.
CDIR SCC Cloud IDS
: Contains rules that detect Cloud Intrusion Detection System findings from Security Command Center
with a Critical, High, Medium, and Low severity classification.
CDIR SCC Cloud Armor
: Contains rules that detect Google Cloud Armor findings from Security Command Center.
CDIR SCC Custom Module
: Contains rules that detect Event Threat Detection custom module findings from Security Command Center.
Cloud Hacktool
: Activity detected from known offensive security platforms or
from offensive tools or software used in the wild by threat actors that
specifically target cloud resources.
Cloud SQL Ransom
: Detects activity associated with exfiltration or ransom of
data within Cloud SQL databases.
Kubernetes Suspicious Tools
: Detects reconnaissance and exploitation behavior from open
source Kubernetes tools.
Kubernetes RBAC Abuse
: Detects Kubernetes activity associated with the abuse of
role-based access controls (RBAC) that attempt privilege escalation or lateral movement.
Kubernetes Certificate Sensitive Actions
: Detects Kubernetes Certificates and Certificate Signing Requests (CSR's) actions that could be used to establish persistence or escalate privileges.
IAM Abuse
: Activity associated with abusing IAM roles and permissions to
potentially privilege-escalate or laterally move within a given Cloud
project or across a Cloud organization.
Potential Exfil Activity
: Detects activity associated with potential
exfiltration of data.
Resource Masquerading
: Detects Google Cloud resources created with names or
characteristics of another resource or resource type. This could be
used to mask malicious activity carried out by or within the resource, with the
intention of appearing legitimate.
Serverless Threats
: Detects activity associated with potential compromise or abuse of Serverless
resources in Google Cloud, including Cloud Run and Cloud Run functions.
Service Disruption
: Detect destructive or disruptive actions that, if
performed in a functioning production environment, may cause a
significant outage. The detected behavior is common and likely benign in
testing and development environments.
Suspicious Behavior
: Activity that is thought to be uncommon and suspicious in
most environments.
Suspicious Infrastructure Change
: Detects modifications to production
infrastructure that align with known persistence tactics
Weakened Config
: Activity associated with weakening or degrading a
security control. Deemed suspicious, potentially legitimate depending on
organizational use.
Potential Insider Data Exfiltration from Chrome
: Detects activity associated
with potential insider threat behaviors, including data exfiltration or loss of
potentially sensitive data outside of a Google Workspace organization. This includes
behaviors from Chrome considered anomalous compared to a 30-day baseline.
Potential Insider Data Exfiltration from Drive
: Detects activity associated
with potential insider threat behaviors, including data exfiltration or loss of
potentially sensitive data outside of a Google Workspace organization. This includes
behaviors from Drive considered anomalous compared to a 30-day baseline.
Potential Insider Data Exfiltration from Gmail
: Detects activity associated with
potential insider threat behaviors, including data exfiltration or loss of potentially
sensitive data outside of a Google Workspace organization. This includes behaviors from
Gmail considered anomalous compared to a 30-day baseline.
Potential Workspace Account Compromise
: Detects insider threat behaviors indicating
that the account could have been potentially compromised and may lead to privilege
escalation attempts or lateral movement attempts within a Google Workspace organization.
This would include behaviors considered rare or anomalous compared to a 30-day baseline.
Suspicious Workspace Administrative Actions
: Detect behaviors indicating potential
evasion, security downgrading or rare and anomalous behaviors never seen in the
last 30 days from users with higher privileges, including administrators.
Supported devices and log types
The following sections describe the required data needed by rule sets in the Cloud
Threats category.
To ingest data from Google Cloud services, see
Ingest Cloud logs to Google SecOps
.
Contact your Google SecOps representative if you need to collect these logs
using a different mechanism.
Google SecOps provides default parsers that parse and normalize raw logs
from Google Cloud services to create UDM records with data required by these rule sets.
For a list of all Google SecOps supported data sources, see
Supported default parsers
.
All rule sets
To use any rule set, we recommend that you collect Google Cloud
Cloud Audit Logs. Certain rules require that customers enable Cloud DNS
logging. Make sure that Google Cloud services are configured to record
data to the following logs:
Cloud Audit Logs
Cloud DNS Logs
Cloud SQL Ransom rule set
To use the
Cloud SQL Ransom
rule set, we recommend that you collect the following Google Cloud data:
Log data listed in the
All rule sets
section.
Cloud SQL logs
.
CDIR SCC Enhanced rule sets
All rule sets that begin with the name
CDIR SCC Enhanced
use Security Command Center Premium
findings contextualized with several other Google Cloud log sources, including the following:
Cloud Audit Logs
Cloud DNS logs
Identity and Access Management (IAM) analysis
Sensitive Data Protection context
BigQuery context
Compute Engine context
To use the
CDIR SCC Enhanced
rule sets, we recommend that you collect the following Google Cloud data:
Log data listed in the
All rule
sets
section.
The following log data, listed by product name and Google SecOps ingestion label:
BigQuery (
GCP_BIGQUERY_CONTEXT
)
Compute Engine (
GCP_COMPUTE_CONTEXT
)
IAM (
GCP_IAM_CONTEXT
)
Sensitive Data Protection (
GCP_DLP_CONTEXT
)
Cloud Audit Logs (
GCP_CLOUDAUDIT
)
Google Workspace Activity (
WORKSPACE_ACTIVITY
)
Cloud DNS queries (
GCP_DNS
)
The following
Security Command Center finding
classes
, listed
by
findingClass
identifier and Google SecOps ingestion label:
Threat
(
GCP_SECURITYCENTER_THREAT
)
Misconfiguration
(
GCP_SECURITYCENTER_MISCONFIGURATION
)
Vulnerability
(
GCP_SECURITYCENTER_VULNERABILITY
)
SCC Error
(
GCP_SECURITYCENTER_ERROR
)
The
CDIR SCC Enhanced
rule sets also depend on data from Google Cloud services.
To send the required data to Google SecOps, make sure you complete
the following:
Enable logging for the required Google Cloud products and services.
Enable Security Command Center Premium and related services.
Configure the
Ingestion of Google Cloud
logs
to Google SecOps.
Configure the export of Event Threat Detection findings to Google SecOps.
By default, all Security Command Center findings are ingested.
See
Exporting Security Command Center findings
for more information about how Google SecOps default parsers map the data fields.
Enable Cloud Audit Logs and configure the export of Cloud Audit Logs to Google SecOps.
See
Collect Cloud Audit Logs
for more information.
Enable Google Workspace logs and send these logs to Google SecOps.
See
Collect Google Workspace logs
for more information.
Configure the export of Google Cloud asset metadata, and context-related data, to Google SecOps.
See
Exporting Google Cloud Asset Metadata to Google SecOps
and
Exporting Sensitive Data Protection data to Google SecOps
for more information.
The following rule sets create a detection when findings from
Security Command Center Event Threat Detection
,
Google Cloud Armor
,
Security Command Center Sensitive Actions Service
, and
Custom modules for Event Threat Detection
are identified:
CDIR SCC Cloud IDS
CDIR SCC Cloud Armor
CDIR SCC Impact
CDIR SCC Enhanced Persistence
CDIR SCC Enhanced Defense Evasion
CDIR SCC Custom Module
Kubernetes Suspicious Tools rule set
To use the
Kubernetes Suspicious Tools
rule set, we recommend that you collect
the data listed in the
All rule sets
section. Make sure that Google Cloud
services are configured to record data to
Google Kubernetes Engine (GKE) Node Logs
Kubernetes RBAC Abuse rule set
To use the
Kubernetes RBAC Abuse
rule set, we recommend that you collect
Cloud Audit Logs
,
listed in the
All rule sets
section.
Kubernetes Certificate Sensitive Actions rule set
To use the
Kubernetes Certificate Sensitive Actions
rule set, we recommend that you collect
Cloud Audit Logs
,
listed in the
All rule sets
section.
Google Workspace-related rule sets
The following rule sets detect patterns in Google Workspace data:
Potential Insider Data Exfiltration from Chrome
Potential Insider Data Exfiltration from Drive
Potential Insider Data Exfiltration from Gmail
Potential Workspace Account Compromise
Suspicious Workspace Administrative Actions
These rule sets require the following log types, listed by product name and
Google SecOps ingestion label:
Workspace Activities (
WORKSPACE_ACTIVITY
)
Workspace Alerts (
WORKSPACE_ALERTS
)
Workspace ChromeOS Devices (
WORKSPACE_CHROMEOS
)
Workspace Mobile Devices (
WORKSPACE_MOBILE
)
Workspace Users (
WORKSPACE_USERS
)
Google Chrome Browser Cloud Management (
CHROME_MANAGEMENT
)
Gmail logs (
GMAIL_LOGS
)
To ingest the required data, do the following:
Collect the data listed in the
All rule sets
section of this document.
See
Ingest Google Workspace data to Google SecOps
to collect
WORKSPACE_ACTIVITY
,
WORKSPACE_CHROMEOS
,
CHROME_MANAGEMENT
, and
GMAIL
logs.
See
Collect Google Workspace logs
to ingest the following logs:
WORKSPACE_ALERTS
WORKSPACE_MOBILE
WORKSPACE_USERS
Serverless Threats rule set
Collect the data listed in the
All rule sets
section of this
document.
Cloud Run logs
(
GCP_RUN
).
Cloud Run logs include
Request logs and Container
logs
which are ingested as the
GCP_RUN
log type in
Google SecOps.
GCP_RUN
logs can be ingested using direct ingestion or
using Feeds and Cloud Storage. For specific log filters and more ingestion
details, see
Exporting Google Cloud Logs to Google SecOps
. The following
export filter exports Google Cloud Cloud Run (
GCP_RUN
) logs, in
addition to the default logs both through the
direct ingestion mechanism
as well as through
Cloud Storage and
Sinks
:
log_id("run.googleapis.com/stdout") OR
log_id("run.googleapis.com/stderr") OR
log_id("run.googleapis.com/requests") OR
log_id("run.googleapis.com/varlog/system)
Curated detections for AWS rule sets
AWS rule sets in this category help identify threats in AWS environments using
event and context data, and includes the following rule sets:
AWS - Compute
: Detects anomalous activity surrounding AWS compute
resources, including EC2 and Lambda.
AWS - Data
: Detects AWS activity associated with data resources, including
RDS snapshots or S3 buckets made publicly available.
AWS - GuardDuty
: Context-aware AWS GuardDuty alerts for Behavior,
Credential Access, Cryptomining, Discovery, Evasion, Execution, Exfiltration,
Impact, Initial Access, Malware, Penetration Testing, Persistence, Policy,
Privilege Escalation, and Unauthorized Access.
AWS - Hacktools
: Detects the use of Hacktools in an AWS environment such
as scanners, toolkits, and frameworks.
AWS - Identity
: Detections for AWS activity associated with IAM and
authentication activity, including unusual logins from multiple geo-locations,
overly permissive role creation, or IAM activity from suspicious tools.
AWS - Logging and Monitoring
: Detects AWS activity related to the
disabling of logging and monitoring services, including CloudTrail, CloudWatch,
and GuardDuty.
AWS - Network
: Detects insecure alterations to AWS network settings such
as security groups and firewalls.
AWS - Organization
: Detects AWS activity associated with your organization
, including the addition or removal of accounts, and unexpected events related to
region usage.
AWS - Secrets
: Detects AWS activity associated with secrets, tokens, and
passwords, including deletion of KMS secrets or Secrets Manager secrets.
Supported devices and log types for AWS
These rule sets have been tested and are supported with the following Google SecOps
data sources, listed by product name and ingestion label.
AWS CloudTrail
(
AWS_CLOUDTRAIL
)
AWS GuardDuty
(
GUARDDUTY
)
AWS EC2 HOSTS
(
AWS_EC2_HOSTS
)
AWS EC2 INSTANCES
(
AWS_EC2_INSTANCES
)
AWS EC2 VPCS
(
AWS_EC2_VPCS
)
AWS IAM (IAM)
(
AWS_IAM
)
See
Configure the ingestion of AWS
data
for information
about setting up ingestion of AWS data.
For a list of all supported data sources,
see
Supported default parsers
.
The following sections describe the required data needed by rule sets that
identify patterns in data.
You can ingest AWS data using an Amazon Simple Storage Service (Amazon S3)
bucket as a source type or, optionally, using Amazon S3 with Amazon Simple Queue
Service (Amazon SQS). At a high level, you will need to do the following:
Configure Amazon S3 or Amazon S3 with Amazon SQS to collect log data.
Configure a
Google SecOps Feed
to ingest data from either Amazon S3 or Amazon SQS
See
Ingest AWS logs into Google SecOps
for the detailed steps required to configure AWS services and configure a
Google SecOps Feed to ingest AWS data.
You can use
AWS Managed Detection Testing
test rules to verify that AWS data
is being ingested to Google SecOps SIEM. These test rules help verify whether AWS
log data is being ingested as expected. After setting up the ingestion of AWS
data, you perform actions in AWS that should trigger the test rules.
See
Verify AWS data ingestion for Cloud Threats category
for information about how verify the ingestion of AWS data using
AWS Managed Detection Testing
test rules.
Curated detections for Azure data
Certain rule sets in this category are designed to work with Azure data to identify threats in Azure environments using event data, context data, and alerts. They include the following:
Azure - Compute
: Detects anomalous activity related to Azure compute
resources, including Kubernetes and virtual machines (VMs).
Azure - Data
: Detects activity associated with data resources, including
Azure blob permissions, modifications, and invitations to external users to
use Azure services on the tenant.
Azure - Defender for Cloud
: Identifies alerts received from context-aware
Microsoft Defender for Cloud related to user behavior, credential access,
cryptomining, discovery, evasion, execution, exfiltration, impact, initial access,
malware, penetration testing, persistence, policy, privilege escalation, or
unauthorized access across all Azure cloud services.
Azure - Hacktools
: Detects the use of hacking tools in an Azure environment,
, including Tor and VPN anonymizers, scanners, and red teaming toolkits.
Azure - Identity
: Detects activity related to authentication and authorization,
indicating unusual behavior, including concurrent access from
multiple geographic locations, overly permissive access management policies,
or Azure RBAC activity from suspicious tools.
Azure - Logging and Monitoring
: Detects activity related to the disabling
of logging and monitoring services within Azure.
Azure - Network
: Detects insecure and notable alterations to Azure
networking devices or settings, including security groups or firewalls, Azure
Web Application Firewall, and denial of service policies.
Azure - Organization
: Detects activity associated with your
organization, including the addition or removal of subscriptions and accounts.
Azure - Secrets
: Detects activity associated with secrets, tokens, and
passwords (for example modifications to Azure Key Vault or storage account access keys).
Supported devices and required log types for Azure
These rule sets have been tested and are supported with the following data
sources, listed by product name and
Google SecOps ingestion label
.
Azure Cloud Services
(
AZURE_ACTIVITY
)
Microsoft Entra ID
,
previously Azure Active Directory (
AZURE_AD
)
Microsoft Entra ID audit logs
,
previously Azure AD audit logs (
AZURE_AD_AUDIT
)
Microsoft Defender for Cloud
(
MICROSOFT_GRAPH_ALERT
)
Microsoft Graph API Activity
(
MICROSOFT_GRAPH_ACTIVITY_LOGS
)
Ingest Azure and Microsoft Entra ID data
You must ingest data from every data source to have maximum rule
coverage. See the following documentation for information about how to ingest
data from each source.
Ingest Azure Monitor Activity logs
from
Azure Cloud Services.
Collect Microsoft Entra ID data
(formerly called Azure AD), including the following:
Microsoft Entra ID logs
Microsoft Entra ID audit logs
Microsoft Entra ID context data
Collect Microsoft Graph security API alert logs
to Ingest Microsoft Defender for Cloud logs using the Microsoft Graph Security API.
Collect Microsoft Graph API activity logs
to Ingest Microsoft Graph API Activity logs using the Microsoft Graph API.
The following section describes how to verify the ingestion of Azure data using
predefined test rules.
Verify the ingestion of Azure data
The Google SecOps
Data Ingestion and Health dashboard
lets you see information about the type, volume, and health of all data being ingested
into Google SecOps using SIEM ingestion features.
You can use also
Azure Managed Detection Testing
test rules to
verify the ingestion of Azure data. After setting up the ingestion, you perform
actions in the Azure portal that should trigger the test rules.
They are intended to verify that data is ingested and in the expected format
to use the curated detections for Azure data.
Enable the Azure Managed Detection Testing test rules
In Google Security Operations, click
Detections
>
Rules & Detections
to
open the Curated Detections page
.
Select the
Managed Detection Testing
>
Azure Managed Detection
Testing
.
Enable both
Status
and
Alerting
for the
Broad
and
Precise
rules.
Send user action data to trigger the test rules
To verify that data is ingested as expected, create a user and login to verify that
these actions trigger the test rules. For information about creating users in Microsoft Entra ID, see
How to create, invite, and delete users
.
In Azure, create a new Microsoft Entra ID user.
Navigate to the Azure portal.
Open
Microsoft Entra ID
.
Click
Add
, then
Create New User
.
Do the following to define the user:
Enter the following information:
User principal name:
GCTI_ALERT_VALIDATION
User principal name:
GCTI_ALERT_VALIDATION
Display name:
GCTI_ALERT_VALIDATION
Select
Auto-generate Password
to auto-generate a password for this user.
Select the
Account Enabled
checkbox.
Open the
Review + Create
tab.
Remember the auto-generated password. You will use this in upcoming steps.
Click
Create
.
Open a browser window in incognito mode, and then navigate to the Azure portal.
Sign in with the newly created user and password.
Change the user password.
Set up multi-factor authentication (MFA), as required by your organization.
Sign out of the Azure portal and confirm your logout.
Do the following to verify that alerts are created in Google Security Operations:
In Google Security Operations, click
Detections
>
Rules & Detections
to
open the
Curated Detections
page
.
Click
Dashboard
.
In the list of detections, check that the following rules were triggered:
tst_azure_ad_user_creation
tst_azure_ad_user_login
After you confirm that data is sent and that these rules are triggered,
deactivate or deprovision the user account.
Send sample alerts to trigger the test rules
Perform the following steps to verify that generating sample security alerts in Azure
triggers the test rules. For more information about generating sample security
alerts in Microsoft Defender for Cloud, see
Alert validation in Microsoft Defender for Cloud
.
In the Azure Portal, navigate to
All Services
.
Under
Security
, open
Microsoft Defender for Cloud
.
Navigate to
Security Alerts
.
Click
Sample Alerts
, and then do the following:
Select your subscription.
Select
all
for
Defender for Cloud Plans
.
Click
Create Sample Alerts
.
Verify that test alerts are triggered.
In Google Security Operations, click
Detections
>
Rules & Detections
to
open the
Curated Detections
page
.
Click
Dashboard
.
In the list of detections, check that the following rules were triggered:
tst_azure_activity
tst_azure_defender_for_cloud_alerts
Execute a GET API request in Microsoft Graph Explorer to trigger the test rules
Perform the following steps to verify that generating sample security alerts in Azure
triggers the test rules.
Navigate to
Microsoft Graph Explorer
.
Verify that the appropriate tenant is selected.
Click
Run Query
.
Verify that test alerts are triggered.
In Google Security Operations, click
Detections
>
Rules & Detections
to
open the
Curated Detections
page
.
Click
Dashboard
.
In the list of detections, check that the
tst_microsoft_graph_api_get_activity
rule was triggered.
Disable the Azure Managed Detection Testing rule sets
In Google Security Operations, click
Detection
>
Rules & Detections
to
open the
Curated Detections
page
.
Select the
Managed Detection Testing
>
Azure Managed Detection
Testing
rules.
Disable both
Status
and
Alerting
for the
Broad
and
Precise
rules.
Curated detections for Office 365 data
Office 365 rule sets in this category help identify threats in Office 365 
environments using event and context data, and includes the following rule sets:
Office 365 - Administrative
: Detects malicious, suspicious 
and high-risk activities in Office 365, including backup policy changes, Microsoft 
Purview, and ATP detections.
Office 365 - eDiscovery
: Detects malicious, suspicious, 
and high-risk activities in Office 365 eDiscovery, including attempts to search for 
credentials or other sensitive data.
Office 365 - Email
: Detects malicious, suspicious, and high 
risk activities in Office 365 Email, including phishing attempts, risky email 
setting changes, and suspicious email activity.
Office 365 - Forms
: Detects malicious, suspicious, and high 
risk activities in Office 365 Forms, including phishing attempts, and status updates 
for forms accounts.
Office 365 - Identity
: Detects malicious, suspicious, and 
high-risk activities in Office 365 related to identity and access management, 
including potential token theft, risky authentication configurations, MFA attacks,
password attacks, and known hacking tools.
Office 365 - Sharepoint and OneDrive
: Detects malicious,
suspicious, and high-risk activities in Office 365 Sharepoint and OneDrive, 
including malware uploads, anonymous file sharing, and searches for credentials 
and financial data.
Office 365 - Teams
: Detects malicious, suspicious, and 
high-risk activities in Office 365 Teams, including impersonation of teams accounts,
exporting of recordings, and transcripts.
Supported devices and required log types for Office 365
These rule sets have been tested and are supported with the following data sources, 
listed by product name and
Google SecOps ingestion label
:
Curated detection for Okta rule sets
Okta rule sets in this category help detect threats within Okta environments by
analyzing event and context data. The rule set includes the following:
Okta
: Identifies a range of malicious and suspicious activities occurring 
within the Okta platform, including MFA attacks, brute force attempts, password 
spraying, login anomalies, and more.
Supported devices and required log types for Okta
These rule sets have been tested and are supported with the following data sources, 
listed by product name and
Google SecOps ingestion label
:
Tune alerts returned by rule sets
You can reduce the number of detections a rule or rule set generates using
rule exclusions
.
A rule exclusion defines the criteria used to exclude an event from being evaluated by
the rule set, or by specific rules in the rule set. Create one or more rule exclusions
to help reduce the volume of detections. See
Configure rule exclusions
for information about how to do this.
What's next
Ingest Google Cloud logs
Ingest AWS logs
Investigate an alert
Need more help?
Get answers from Community members and Google SecOps professionals.
