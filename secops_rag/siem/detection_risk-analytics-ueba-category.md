# Overview of Risk Analytics for UEBA category

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category/  
**Scraped:** 2026-03-05T09:32:09.621701Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Overview of Risk Analytics for UEBA category
Supported in:
Google secops
SIEM
This document provides an overview of the rule sets in the Risk Analytics for UEBA category, the
required data, and configuration you can use to tune the alerts generated
by each rule set. These rule sets help identify threats by evaluating the
supported log sources.
Rule set descriptions
The following rule sets are available in the Risk Analytics for UEBA category and are
grouped by the type of patterns detected:
Authentication
New Login by User to Device
: a user logged in to a new device.
Anomalous Authentication Events by User
: a single user entity had anomalous
authentication events recently, compared to historical usage.
Failed Authentications by Device
: a single-device entity had many
failed login attempts recently, compared to historical usage.
Failed Authentications by User
: a single-user entity had many failed
login attempts recently, compared to historical usage.
Network traffic analysis
Anomalous Inbound Bytes by Device
: significant amount of data recently
uploaded to single device entity, compared to historical usage.
Anomalous Outbound Bytes by Device
: significant amount of data recently
downloaded from a single device entity, compared to historical usage.
Anomalous Total Bytes by Device
: a device entity recently uploaded
and downloaded a significant amount of data, compared to historical usage.
Anomalous Inbound Bytes by User
: a single-user entity recently downloaded
a significant amount of data, compared to historical usage.
Anomalous Total Bytes by User
: a user entity recently uploaded and
downloaded a significant amount of data recently, compared to historical usage.
Brute Force then Successful Login by User
: a single-user entity from one
IP address had several failed authentication attempts to a certain application
before successfully logging in.
Peer group-based detections
Anomalous or Excessive Logins for a Newly Created User
: anomalous or excessive
authentication activity for a recently created user. This uses creation time from
AD Context data.
Anomalous or Excessive Suspicious Actions for a Newly Created User
:
anomalous or excessive activity (including, but not limited to, HTTP telemetry,
process execution, and group modification) for a recently created
user. This uses creation time from AD Context data.
Suspicious actions
Excessive Account Creation by Device
: a device entity created several
new user accounts.
Excessive Alerts by User
: a large number of security alerts from an antivirus
or endpoint device (for example,
connection was blocked
,
malware was detected
)
were reported about a user entity, which was much greater than historical patterns.
These are events where the
security_result.action
UDM field is set to
BLOCK
.
Data loss prevention-based detections
Anomalous or Excessive Processes with Data Exfiltration Capabilities
: anomalous or
excessive activity for processes associated with data exfiltration capabilities
such as keyloggers, screenshots, and remote access. This uses file metadata enrichment
from VirusTotal.
Required data needed by Risk Analytics for UEBA category
This section details the data required by each rule set category for optimal 
performance. While UEBA detections are designed to work with all supported default 
parsers, using the following specific data types maximizes their benefit. 
For a complete list of supported default parsers, see
Supported log types and default parsers
.
Authentication
To use any of these rule sets, collect log data from either
Azure AD Directory Audit (
AZURE_AD_AUDIT
) or Windows Event (
WINEVTLOG
).
For
WINEVTLOG
, you must configure your data collection configuration to include the following Windows
Event IDs
in the
Security
event log
Channel
.
 These events map directly to the
Event types
(for example,
USER_LOGIN
or
PROCESS_LAUNCH
) used by the detection engine.
Windows Event ID requirements
Event type
Windows Event ID
USER_LOGIN
529, 4624, 4625, 4626, 4648, 4672, 4768, 4769, 4770, 4771, 4777, 4820, 4821, 4964
USER_CREATION
4720
NETWORK_CONNECTION
4096, 4097, 4321, 5156, 5632, 5633, 5157
GROUP_MODIFICATION
4728, 4729, 4732, 4733, 4735, 4737, 4745, 4746, 4747, 4750, 4751, 4752, 4755, 4756, 4757, 4760, 4761, 4762, 4764, 4784, 4785, 4786, 4787, 4788, 4791
PROCESS_LAUNCH
4688
PROCESS_OPEN
4663, 4670, 4691, 8002
Network traffic analysis
To use any of these rule sets, collect log data that captures network activity.
For example, from devices such as FortiGate (
FORTINET_FIREWALL
),
Check Point (
CHECKPOINT_FIREWALL
), Zscaler (
ZSCALER_WEBPROXY
), CrowdStrike Falcon (
CS_EDR
),
or Carbon Black (
CB_EDR
).
Peer group-based detections
To use any of these rule sets, collect log data from either
Azure AD Directory Audit (
AZURE_AD_AUDIT
) or Windows Event (
WINEVTLOG
).
Suspicious actions
Rule sets in this group each use a different type of data.
Excessive Account Creation by Device rule set
To use this rule set, collect log data from either
Azure AD Directory Audit (
AZURE_AD_AUDIT
) or Windows Event (
WINEVTLOG
).
Excessive Alerts by User rule set
To use this rule set, collect log data that captures endpoint activities or
audit data, such as that recorded by CrowdStrike Falcon (
CS_EDR
),
Carbon Black (
CB_EDR
), or Azure AD Directory Audit (
AZURE_AD_AUDIT
).
Data loss prevention-based detections
To use any of these rule sets, collect log data that captures process and file activities,
such as that recorded by CrowdStrike Falcon (
CS_EDR
), Carbon Black (
CB_EDR
),
or SentinelOne EDR (
SENTINEL_EDR
).
Rule sets in this category depend on events with the following
metadata.event_type
values:
PROCESS_LAUNCH
,
PROCESS_OPEN
,
PROCESS_MODULE_LOAD
.
Tuning alerts returned by rule sets this category
You can reduce the number of detections a rule or rule set generates using
rule exclusions
.
A rule exclusion defines the criteria used to exclude an event from being evaluated by
the rule set, or by specific rules in the rule set. Create one or more rule exclusions
to help reduce the volume of detections. See
Configure rule exclusions
for information about how to do this.
Example of a rule for Risk Analytics for UEBA category
The following example shows how to create a rule to generate detections on
any entity hostname whose risk score is greater than
100
:
rule EntityRiskScore {
  meta:
  events:
    $e1.principal.hostname != ""
    $e1.principal.hostname = $hostname

    $e2.graph.entity.hostname = $hostname
    $e2.graph.risk_score.risk_window_size.seconds = 86400 // 24 hours
    $e2.graph.risk_score.risk_score >= 100

    // Run deduplication across the risk score.
    $rscore = $e2.graph.risk_score.risk_score

  match:
    // Dedup on hostname and risk score across a 4 hour window.
    $hostname, $rscore over 4h

  outcome:
    // Force these risk score based rules to have a risk score of zero to
    // prevent self feedback loops.
    $risk_score = 0

  condition:
    $e1 and $e2
}
This example rule also performs a self deduplication using the match
section. If a rule detection might trigger, but the hostname and risk score
remain unchanged within a 4-hour window, no new detections are created.
The only possible risk windows for entity risk score rules are either 24 hours
or 7 days (86,400 or 604,800 seconds respectively). If you don't include the
risk window size in the rule, the rule returns inaccurate results.
Entity risk score data is stored separately from entity context data. To use
both in a rule, the rule must have two separate entity events, one for the
entity context and one for the entity risk score, as shown as in the following
example:
rule EntityContextAndRiskScore {
  meta:
  events:
    $log_in.metadata.event_type = "USER_LOGIN"
    $log_in.principal.hostname = $host

    $context.graph.entity.hostname = $host
    $context.graph.metadata.entity_type = "ASSET"

    $risk_score.graph.entity.hostname = $host
    $risk_score.graph.risk_score.risk_window_size.seconds = 604800

  match:
    $host over 2m

  outcome:
    $entity_risk_score = max($risk_score.graph.risk_score.normalized_risk_score)

  condition:
    $log_in and $context and $risk_score and $entity_risk_score > 100
}
What's next
Investigate risk using the Risk Analytics dashboard
Need more help?
Get answers from Community members and Google SecOps professionals.
