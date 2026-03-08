# Default detection rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/default-rules/  
**Scraped:** 2026-03-05T10:04:15.992087Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Default detection rules
Supported in:
Google secops
SIEM
YARA-L rules language
YARA-L is a detection rules language developed by Google. The purpose of YARA-L
is to move away from detections as just data queries to actual event-driven
investigations. YARA-L is derived from the YARA language commonly used in
malware analysis. The
L
stands for logs. YARA-L enables you to take advantage
of all the information from multiple sources within detections, and correlate
those events into actionable alerts. For more information, see the
Overview of
the YARA-L 2.0 language
.
Google Security Operations sample detection rules
To help accelerate your adoption of the Google SecOps Detection Engine,
there is a
GitHub repository with sample
rules
. This repository contains
several different categories of detection rules, including the following:
Google Cloud CloudAudit
Google Workspace
Informational warnings
Malware
MITRE ATT&CK
SOC prime rules
Suspicious events
Each category takes a specific approach in how it views data sources and
specifies what events and matching statements to use.
Example rules and tuning
The following rule creates an event variable
$e1
which is used to track the
event type. The event variable can be any value which has meaning to the data
being evaluated. The UDM field being evaluated in this event is
metadata.eventype
so it makes sense to just call it
e1
. The next lines
searches for specific occurrences of regular expression matches within
e1
. The condition that
creates a detection in Google SecOps is any time the event
$e1
takes
place. For tuning purposes, a
not
condition is provided to exclude certain
non-malicious paths for the command line argument. Further
not
conditions
could be added to this rule if you identify frequent false positives coming from
other known file paths.
rule suspicious_unusual_location_svchost_execution

{
 meta:
   author = "Google Cloud Security"
   description = "Windows 'svchost' executed from an unusual location"
   yara_version = "YL2.0"
   rule_version = "1.0"

 events:
   $e1.metadata.event_type = "PROCESS_LAUNCH"
   re.regex($e1.principal.process.command_line, `\bsvchost(\.exe)?\b`) nocase
   not re.regex($e1.principal.process.command_line, `\\Windows\\System32\\`) nocase

condition:
   $e1
}
Specify more than one event variable
YARA-L enables you to have more than one event variable in a rule. In the
following example, the rule has events
$e1
and
$e2
. The condition states the
logical condition that triggers the detection.
rule ExcludeZeroValues {
  meta:
    author = "noone@google.com"

  events:
    $e1.metadata.event_type = "NETWORK_DNS"
    $e1.principal.hostname = $hostname

    // $e1.principal.user.userid may be empty string.
    $e1.principal.user.userid != "Guest"

    $e2.metadata.event_type = "NETWORK_HTTP"
    $e2.principal.hostname = $hostname

    // $e2.target.asset_id cannot be empty string as explicitly specified.
    $e2.target.asset_id != ""

  match:
    // $hostname cannot be empty string.
    $hostname over 1h

  condition:
    $e1 and $e2
}
Rules outcome section
Use the outcome section to set holding variables within the rule detection to
provide enrichment for downstream consumption. For example, you can add severity
scoring information that relies on data from the events being analyzed. The
following detection examines two events to attribute the
$hostname
value. If
the value
$hostnames
match over a 5 minute period, a severity score is
applied. When using time periods, the Google SecOps Detection Engine only
examines the discrete blocks of time you specify.
rule OutcomeRuleMultiEvent {
    meta:
      author = "noone@google.com"
    events:
      $u.udm.principal.hostname = $hostname
      $asset_context.graph.entity.hostname = $hostname

      $severity = $asset_context.graph.entity.asset.vulnerabilities.severity

    match:
      $hostname over 5m

    outcome:
      $risk_score =
        max(
            100
          +   if($hostname = "my-hostname", 100, 50)
          +   if($severity = "HIGH", 10)
          +   if($severity = "MEDIUM", 5)
          +   if($severity = "LOW", 1)
        )

      $asset_id_list =
        array(
          if($u.principal.asset_id = "",
             "Empty asset id",
             $u.principal.asset_id
          )
        )

      $asset_id_distinct_list = array_distinct($u.principal.asset_id)

      $asset_id_count = count($u.principal.asset_id)

      $asset_id_distinct_count = count_distinct($u.principal.asset_id)

    condition:
      $u and $asset_context and $risk_score > 50 and not arrays.contains($asset_id_list, "id_1234")
}
Conclusion
YARA-L is a flexible detection language which enables you to examine security
events and not simply just return a data query. The event variable is used to
track what field values are being used in the condition section of the rule. You
can use a single event, multiple events over time, correlate sources for a
single value (such as $hostname from different data sources), and even use tools
such as regular expressions to provide matches. It is essential to tune the rules to your own
environment and this can be done by specifying exclusions within the logic. You
can also use reference lists to group items together and then reference that
list in the rule. Don't forget that Google SecOps does not need every
detection to be alerted on. You can keep track of detections for multiple
purposes and only alert on those you determine are most critical in your
environment.
Need more help?
Get answers from Community members and Google SecOps professionals.
