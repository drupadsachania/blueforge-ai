# Overview of context-aware analytics

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/context-aware-analytics/  
**Scraped:** 2026-03-05T09:31:42.804955Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Overview of context-aware analytics
Supported in:
Google secops
SIEM
Google SecOps lets you view telemetry, entity context, relationships, 
and vulnerabilities as a single detection within your Google SecOps account. 
It provides entity contextualization to enable you to understand both the 
behavioral patterns in telemetry and the context of those impacted entities 
from those patterns.
Examples:
Surfacing the permissions for an account on which a brute force login is being 
attempted.
Importance of data hosted by an asset that is also the source of outbound 
network activity.
Customers can use this contextualization for detection filtering, heuristic 
alert prioritization, triage, and investigation.
Security analysts and detection engineers typically work to craft a detection on 
a basic pattern of event telemetry (an outbound network connection), creating 
numerous detections for their analysts to triage. The analysts attempt to stitch 
together an understanding of what happened to trigger the alert and how 
significant the threat is.
Context-aware analytics incorporates advanced enrichment capabilities earlier in 
the detection authoring and execution workflow, enabling you to provide the 
following additional capabilities:
Making relevant context available for heuristic-driven contextual risk scoring 
of detections at detection execution time rather than at the human triage stage
Reducing time spent on triage and manually stitching together information from 
disparate IT security systems (EDR consoles, firewall or proxy logs, CMDB and 
IAM context, vulnerability scan results)
Enabling analysts and detection engineers to filter out entire clusters of 
threats that may be expected or represent little or no danger to the enterprise 
(malware testing in a sandbox environment, vulnerabilities and anomalous activity 
in a development network with no sensitive data or access, and more)
Writing rules for context-aware analytics
You can use Detection Engine rules to search for entity context data in your 
Google SecOps account.
To search for entity context data, complete the following:
Specify a source using either the udm or entity.
$eventname.[<source>].field1.field2
For an entity context, <source> is 'graph'. For a UDM event, <source> is 
'udm'.
If omitted, the <source> defaults to udm.
Specify the entity data:
$e1.graph.entity.hostname = "my-hostname"
$e1.graph.entity.relations.relationship = "OWNS"
Specify UDM event data. The following statements are equivalent.
$e1.udm.principal.asset_id = "my_asset_id"
$e1.principal.asset_id = "my_asset_id"
You can create many of the same types of rules for entity contexts as you would 
for UDM events, including the following:
Multiple event rules
Comparing entity contexts to other entity contexts
Comparing entity contexts to UDM events
Repeated fields in entity contexts
Sliding windows
Calculating a risk score for detections
Unlike a UDM event, an entity context does not have a specific timestamp.
Each entity context record has a time interval, entity.metadata.interval, over
which the entity context is valid. This time interval may not be a day boundary
and can be any duration.
A UDM event will be correlated with an entity context record only when the
timestamp of the UDM event falls within the time interval of the entity context
record. If this condition is not met, the UDM and entity are not evaluated for
detections. The detection engine implicitly enforces this and you don't need
to specify it as a condition in a rule.
When comparing UDM events to an entity context with windowing, an entity context 
represents a constant value over a specified window.
If there are adjacent day buckets where the entity context changes its value, 
Google SecOps attempts to match on all of the entity context values, and 
return any and all matches that are found.
Example rules
Searching for entities with administrator context
The following rule searches for entities that are also tied to administrator 
privileges. It is looking for times when someone with administrator privilege 
attempted to sign in to or log out of the system.
rule LoginLogout {
  meta:
  events:
    ($log_inout.metadata.event_type = "USER_LOGIN" or  $log_inout.metadata.event_type = "USER_LOGOUT")
    $log_inout.principal.user.user_display_name = $user

    $context.graph.entity.user.user_display_name = $user
    $context.graph.entity.resource.attribute.roles.type = "ADMINISTRATOR"

  match:
    $user over 2m

  condition:
    $log_inout and $context
}
Sliding window example
The following sliding window example is valid.
rule Detection {
  meta:
  events:
    $e1.graph.entity.hostname = $host
    $e2.udm.principal.hostname = $host

  match:
    // Using e2 (a UDM event) as a pivot.
    $host over 3h after $e2

  condition:
    $e1 and $e2
}
Invalid sliding window example
The following sliding window example is invalid. Entity context cannot be used 
as a pivot for a sliding window.
rule Detection {
  meta:
  events:
    $e1.graph.entity.hostname = $host
    $e2.udm.principal.hostname = $host

  match:
    // Attempting to use $e1 (an entity context) as a pivot. Invalid.
    $host over 3h after $e1

  condition:
    $e1 and $e2
}
Login example using outcome section
The following example uses the
outcome
section to calculate a risk score for
the detection.
rule Detection {
  meta:
  events:
    $auth.metadata.event_type = "USER_LOGIN"
    $auth.metadata.vendor_name = "Acme"
    $auth.metadata.product_name = "Acme SSO"
    $auth.target.user.userid = $user
    $auth.metadata.event_timestamp.seconds >
       $context.graph.entity.user.termination_date.seconds

    $context.graph.metadata.vendor_name = "Microsoft"
    $context.graph.metadata.product_name = "Azure Active Directory"
    $context.graph.metadata.entity_type = "USER"
    $context.graph.entity.user.userid = $user
    $context.graph.entity.user.termination_date.seconds > 0

  match:
    $user over 15m

  outcome:
    $risk_score = max(
        if ( $auth.metadata.event_type = "USER_LOGIN", 50) +
        if (
            $context.graph.entity.user.title = "Remote" nocase or
            $context.graph.entity.user.title = "Temp" nocase or
            $context.graph.entity.user.title = "Vendor" nocase, 40) +
        if ( $context.graph.entity.user.title = "Legal" nocase, 10)
    )

  condition:
    $auth and $context
}
Suspicious process launch example
The following example evaluates UDM event process data against IOC context data
stored as an entity context.
rule ProcessLaunch {
  meta:
  events:
    $ioc.graph.metadata.vendor_name = "ACME"
    $ioc.graph.metadata.product_name = "IOCs"
    $ioc.graph.metadata.entity_type = "FILE"
    $ioc.graph.entity.file.sha256 = $hash

    $process.metadata.event_type = "PROCESS_LAUNCH"
    $process.principal.hostname = $hostname
    (
        not $process.target.process.file.sha256 = "" and
        $process.target.process.file.sha256 = $hash
    )

  match:
    $hash over 15m

  condition:
    $ioc and $process
}
Additional qualifiers for entity context
To create an event variable that uses an entity context, you must provide a
<source>
after the event name. 
The
<source>
must be
graph
.
The following pattern refers to an entity context:
$e.graph.entity.hostname
Note that there are two equivalent methods of referring to a UDM event:
$u.udm.principal.asset_id
$u.principal.asset_id
You can mix and match all of these qualifiers in rule text. You can use 
different qualifiers for the same event as well.
Outcome section
Detection engine supports an
outcome
section that lets you derive more
information from a rule. The logic defined in the
outcome
section is evaluated
against each detection. If a rule generates
N
detections, each of the
N
detections may result in a different set of outcomes.
You can find an example rule that uses the
outcome
section under
rule with outcome selection
.
Detailed usage and syntax of an
outcome
section can be found in
the outcome section
.
Outcome section and detection deduplication / detection grouping
For rules with a match section, recall that detections are "grouped by" the
match variables. This causes detections to be deduplicated, such that one row
is returned for each unique set of match variables and time window.
The outcome variables are ignored when doing this deduplication. Thus, if
there are two different detections with the same values for the match variables
and time window, but with different values for outcome variables, these will
be deduplicated and you will see only one detection. This can happen when a
detection was created due to late arriving data, for example. Here's an example
that illustrates this case.
rule ExampleOutcomeRule {
  ...
  match:
    $hostname over <some window>
  outcome:
    $risk_score = <some logic here>
  ...
}
This rule results in the following matches:
Detection 1:
  hostname: test-hostname
  time window: [t1, t2]
  risk_score: 10
Detection 2:
  hostname: test-hostname
  time window: [t1, t2]
  risk_score: 73
Because the match variables and the time window are the same for
Detection 1 and Detection 2, these are deduplicated and you will
see only one detection, even though the outcome variable, risk_score, is
different.
What's next
For information about how Google SecOps ingests contextual data and
enriches entities, see
How Google SecOps enriches event and entity data
Need more help?
Get answers from Community members and Google SecOps professionals.
