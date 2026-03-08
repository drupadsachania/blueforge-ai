# Use Triage and Investigation Agent (TIN) to investigate alerts

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent/  
**Scraped:** 2026-03-05T09:45:19.882109Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use Triage and Investigation Agent (TIN) to investigate alerts
Supported in:
Google secops
The Triage and Investigation Agent (TIN) is an AI-powered investigation assistant embedded in
Google Security Operations. It determines if the alerts are true or false positives,
then provides a summarized explanation for its assessment.
TIN analyzes alerts in Google SecOps using Mandiant 
principles and industry best practices. It evaluates incoming
alerts, executes an investigation plan, and provides a structured analysis that
includes both its findings and reasoning.
For a list of IAM permissions required for using the
agent, see
Triage and Investigation Agent (TIN)
.
Investigation tools
The agent uses the following built-in tools to complete its analysis:
Dynamic search queries: Runs and refines searches in SecOps to collect additional
context for the alert.
GTI enrichment: Enriches IoCs with Google Threat Intelligence (GTI) data,
including domains, URLs, and hashes.
Command-line analysis: Analyzes command lines to explain actions in natural
language.
Process tree reconstruction: Analyzes the processes in the alert to show the
full sequence of related system activity.
Trigger TIN
You can trigger TIN automatically or manually. Each tenant can run
up to 10 investigations per hour (5 manual and 5 automatic). Each investigation
typically completes in an average of 60 seconds and runs for a maximum of 20 minutes.
There's no investigation queue. The agent doesn't automatically analyze alerts
generated beyond the limit.
Auto-investigation settings
Automatic investigations are enabled by default if you have the necessary
administrator permissions and are opted into the agent. To verify or modify
this setting, navigate to
Settings
>
SIEM Settings
>
Gemini Investigations
.
When enabled, the agent uses default settings to investigate all default
supported log types. You can customize the investigation timing and filter
criteria to control which alerts are investigated.
Investigation timing
You can configure when the investigation starts after an alert is generated. By
default, the investigation starts five minutes after the alert is generated to
account for any events that are still arriving and require correlation.
You can change this delay to a maximum of 20 minutes from the list in the
settings panel.
Investigation criteria
You can define custom criteria to trigger auto-investigations only for specific alerts.
If no custom criteria are defined, the agent investigates all alerts that match
the supported log types listed in
Default supported log types
.
To create custom auto-investigation settings:
Click
add
.
Select a UDM field from the list. Supported fields include:
detection.rule_id
detection.rule_name
udm.metadata.event_type
udm.metadata.log_type
udm.metadata.product_event_type
udm.metadata.product_name
udm.metadata.vendor_name
udm.about.entity_metadata.product_name
udm.principal.user.userid
Select an operator to evaluate the field (
=
or
!=
).
Enter or select the value for the field. The values in the list are based on
values observed in your environment.
Use a logic operator (
AND
or
OR
) to combine multiple criteria.
Click
Save
to apply your settings.
Default Supported Log Types
The agent supports automatic investigation for alerts that contain events with the
following
metadata.log_type
values:
Source
metadata.log_type
values
Amazon
AWS_CLOUDTRAIL
,
AWS_IAM
,
AWS_NETWORK_FIREWALL
,
AWS_VPC_FLOW
Cisco
CISCO_ASA_FIREWALL,
CISCO_FIREPOWER_FIREWALL,
CISCO_ISE,
CISCO_MERAKI
CrowdStrike
CROWDSTRIKE_IOC
,
CS_ALERTS
,
CS_CEF_EDR
,
CS_DETECTS
,
CS_EDR
,
CS_IDP
Fortinet
FORTINET_FIREWALL
,
FORTINET_FORTIEDR
,
FORTINET_WEBPROXY
Google
GCP_CLOUDAUDIT
,
GCP_CLOUDIDENTITY_DEVICES
,
GCP_CLOUDIDENTITY_DEVICEUSERS
,
GCP_DNS
,
GCP_NGFW_ENTERPRISE
,
GCP_VPC_FLOW
,
WORKSPACE_ACTIVITY
,
WORKSPACE_ALERTS
,
WORKSPACE_USERS
Microsoft
ADFS
,
AZURE_AD
,
AZURE_AD_AUDIT
,
AZURE_AD_CONTEXT
,
AZURE_AD_SIGNIN
,
AZURE_FIREWALL
,
AZURE_NSG_FLOW
,
GITHUB
,
MICROSOFT_DEFENDER_ATP
,
MICROSOFT_DEFENDER_ENDPOINT
,
MICROSOFT_DEFENDER_ENDPOINT_IOS
,
MICROSOFT_DEFENDER_IDENTITY
,
MICROSOFT_GRAPH_ALERT
,
OFFICE_365
,
SENTINELONE_ACTIVITY
,
SENTINELONE_ALERT
,
SENTINELONE_CF
,
SENTINEL_DV
,
SENTINEL_EDR
,
WINDOWS_AD
,
WINDOWS_DEFENDER_ATP
,
WINDOWS_DEFENDER_AV
,
WINDOWS_DHCP
,
WINDOWS_DNS
,
WINDOWS_FIREWALL
,
WINDOWS_SYSMON
,
WINEVTLOG
Okta
OKTA
,
OKTA_ACCESS_GATEWAY
,
OKTA_USER_CONTEXT
Other
BARRACUDA_FIREWALL
,
BOX
,
BRO_DNS
,
CB_APP_CONTROL
,
CB_DEFENSE
,
CB_EDR
,
CHECKPOINT_EDR
,
CHECKPOINT_FIREWALL
,
CLOUDFLARE_WAF
,
CYBERARK_EPM
,
CYBEREASON_EDR
,
DUO_AUTH
,
DUO_USER_CONTEXT
,
ELASTIC_EDR
,
F5_AFM
,
F5_ASM
,
F5_BIGIP_LTM
,
FIREEYE_HX
,
FIREEYE_NX
,
FORCEPOINT_FIREWALL
,
INFOBLOX_DNS
,
JUNIPER_FIREWALL
,
KEYCLOAK
,
LIMACHARLIE_EDR
,
MALWAREBYTES_EDR
,
MCAFEE_EDR
,
NETFILTER_IPTABLES
,
ONELOGIN_SSO
,
ONE_IDENTITY_IDENTITY_MANAGER
,
OPENSSH
,
PAN_FIREWALL
,
PING
,
SALESFORCE
,
SEP
,
SOPHOS_EDR
,
SOPHOS_FIREWALL
,
SQUID_WEBPROXY
,
SURICATA_EVE
,
SURICATA_IDS
,
SYMANTEC_EDR
,
TANIUM_EDR
,
TANIUM_THREAT_RESPONSE
,
TRENDMICRO_EDR
,
UMBRELLA_DNS
,
UMBRELLA_FIREWALL
,
UMBRELLA_WEBPROXY
,
ZEEK
,
ZSCALER_FIREWALL
,
ZSCALER_WEBPROXY
.
Manual investigations
To manually run an investigation:
In Google SecOps, go to the
Alerts & IoCs
page.
Select an alert and click
Run Investigation
.
You can also navigate to an alert in a case and run an investigation for it.
The banner updates to
View Investigation
once the process completes.
You can click this banner to view the details of an investigation.
Navigate to investigations
You can access past or in-progress investigations from anywhere in Google SecOps.
Click
in the Google SecOps interface.
Click
in the navigation panel.
Click
keyboard_arrow_down
next
to the investigation list to expand the panel.
In the list, select an item to open the investigation results.
Each investigation entry includes the alert name, the completion time, and the
Gemini investigation summary. If the same alert is investigated multiple times,
each investigation appears as a separate entry on the investigation list.
Review an investigation
Each investigation opens in a detailed view that summarizes Gemini's analysis,
its reasoning, and the supporting data it used.
This view has the following components:
Summary
Investigation timeline
View an alert or re-run an investigation
Suggested next steps
Feedback
Summary
At the top of the panel, the
Summary by Gemini
section provides a brief
description of the alert and the investigation's findings.
The summary provides the following information:
Disposition: Indicates if Gemini determined the alert to be a true
or false positive.
Confidence level: Describes Gemini's confidence in its assessment.
This assessment is based on the alert and available investigation data.
Summary explanation: Describes the alert and how Gemini reached its
conclusion.
Investigation timeline
TIN investigation follows a structured, multi-stage timeline
designed to transform raw alerts into actionable intelligence. While these
intermediate steps are primarily used by the agent to build context and refine
its analysis, they are also visible within the
Investigation timeline
in the
web interface, providing security analysts with clear visibility into the agent's
investigation progress.
Initial assessment and risk prioritization
The investigation begins with an immediate evaluation of the alert to establish
baseline context. During this stage, the agent automatically analyzes alert details
and metadata to identify high-confidence benign activity. If an alert is classified as low
risk, the agent concludes the investigation.
Contextual enrichment and evidence gathering
The agent executes several parallel analysis steps to build a comprehensive
picture of the suspicious activity by leveraging internal and external
intelligence:
Google Threat Intelligence (GTI) enrichment
: Identifies and evaluates
indicators of compromise (IoCs), such as file hashes, IP addresses, and
domains against Google Threat Intelligence and VirusTotal to identify
known malicious entities.
Entity Context Graph (ECG) analysis
: Retrieves prevalence data, such as when
an entity was first or last seen, to provide deeper environmental context and
analyze relationships between entities.
Network context gathering
: Extracts additional context related to network
traffic by performing targeted searches to identify
suspicious patterns.
Case metadata integration
: Retrieves broader context from the case the alert
belongs to, incorporating metadata such as tags and priority into the
investigation.
Process tree construction
: Constructs the execution hierarchy of system
processes to help analysts understand exactly how a suspicious action was
initiated and what subsequent actions it took.
Adaptive Investigation
Based on the findings from the earlier investigation steps, the agent dynamically
determines the next course of action:
Evaluates findings
: Assesses information gathered in previous steps to
identify potential gaps or new avenues for inquiry.
Performs deep-dive research
: Iteratively generates new plans and executes
specialized tools, such as GTI enrichment, ECG analysis, advanced
command-line analysis, or targeted searches to uncover hidden threats.
View an alert or re-run an investigation
The investigation panel lets you take the following actions:
View alert
: Opens the alert details in the
Google SecOps SIEM view.
Re-run investigation
: Reruns the analysis for the same alert.
Suggested next steps
For all investigations, Gemini provides further investigation steps.
These steps recommend additional actions or data sources for analysts to
explore.
As the agent is updated, these suggestions can expand to include remediation
guidance.
Feedback
Each investigation includes
thumb_up
Thumb Up
and
thumb_down
Thumb Down
icons
to collect feedback. Focus your feedback on
the severity verdict because this helps refine Gemini's threat
classification.
Cloud audit logging
To enable audit logging for TIN:
In the Google Google Cloud console, navigate to
IAM
>
Audit Logging
.
Search for
Chronicle API
.
In the
Permission Types
tab of the
Chronicle API
panel, select the
Admin Read
checkbox.
View audit logs
To view audit logs:
In the Google Google Cloud console, go to
Monitoring
>
Logs Explorer
.
Search for the logs you want to view.
To view all Google SecOps audit logs, search for
protoPayload.serviceName: "chronicle.googleapis.com"
.
To see only TIN logs, search for the related methods.
For example,
protoPayload.method: "google.cloud.chronicle.v1alpha.InvestigationService.TriggerInvestigation"
and
protoPayload.method: "google.cloud.chronicle.v1alpha.InvestigationService.GetInvestigation"
.
Need more help?
Get answers from Community members and Google SecOps professionals.
