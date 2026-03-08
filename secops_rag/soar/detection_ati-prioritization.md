# Applied Threat Intelligence priority overview

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/ati-prioritization/  
**Scraped:** 2026-03-05T10:05:55.030997Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Applied Threat Intelligence priority overview
Supported in:
Google secops
SIEM
Applied Threat Intelligence (ATI) alerts in Google Security Operations are IoC 
matches that have been contextualized by YARA-L rules using curated detection. 
The contextualization leverages Mandiant threat intelligence from Google SecOps 
context entities, which allows intelligence-driven alert prioritization.
ATI priorities are provided in the
Applied Threat Intelligence - Curated Prioritization
rule pack, which is available in Google SecOps Managed Content with the Google SecOps Enterprise Plus license.
ATI prioritization features
The most relevant ATI prioritization features include:
Google Threat Intelligence Verdict
: A unified threat
intelligence verdict based on Google's analysis.
Google Threat Intelligence Severity
: A calculated
severity rating based on Google's analysis.
Active IR
: Sourced from an active Incident Response (IR) engagement.
Prevalence
: Commonly observed by Mandiant.
Attribution
: Strongly associated with a threat tracked by Mandiant.
Blocked
: Indicator was not blocked by security controls.
Network Direction
: Shows inbound or outbound network
traffic.
You can view the ATI priority feature for an alert on the
IoC matches
>
Event viewer
page.
ATI priority models
ATI priority models use Google SecOps events and Mandiant threat intelligence to assign priority levels to IoCs. This prioritization is based on features relevant to both the priority level and IoC type, forming logic chains that classify the priority. The ATI actionable threat intelligence models can then help you respond to the generated alerts.
Priority models are used in the curated detection rules provided in the
Applied Threat 
Intelligence - Curated prioritization
rule pack. You can also create custom rules 
using Mandiant threat intelligence through Mandiant Fusion Intelligence, 
which requires the Google SecOps Enterprise Plus license. For more information about 
writing Fusion feed YARA-L rules, 
see
Applied Threat Intelligence fusion feed overview
.
The following priority models are available:
Active breach priority
The Active breach model prioritizes indicators Mandiant observed in
active or past compromises, where the GTI Verdict is
Malicious
and
GTI Severity is
High
.
Relevant features used by the model include:
GTI Verdict
,
GTI Severity
,
Active IR
,
Prevalence
, and
Attribution
.
High priority
The High model prioritizes indicators that weren't observed in Mandiant 
investigations, but were identified by Google Threat Intelligence as being associated 
with threat actors or malware. Network indicators in this model attempt to match 
only outbound direction network traffic.
Relevant features used by the model include:
GTI Verdict
,
GTI Severity
,
Prevalence
, and
Attribution
.
Medium priority
The Medium model prioritizes indicators identified by Google Threat Intelligence
with a
Malicious
GTI Verdict and
High
GTI Severity, even if they weren't
observed in Mandiant investigations.
Network indicators in this model match only outbound network traffic.
Relevant features used by the model include:
GTI Verdict
,
GTI Severity
,
Prevalence
, and
Blocked
.
Inbound IP address authentication
The Inbound IP address authentication model prioritizes IP addresses that authenticate to local infrastructure in an inbound network direction. The UDM authentication extension must exist in events for a match to occur. Although not enforced for all product types, this rule set also attempts 
to filter out some failed authentication events. For example, this rule set is not scoped for some SSO 
authentication types.
Relevant features used by the model include:
GTI Verdict
,
Blocked
,
Network Direction
, and
Active IR
.
Need more help?
Get answers from Community members and Google SecOps professionals.
