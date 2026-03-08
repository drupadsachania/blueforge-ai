# Risk-based alerting with entity-only rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting/  
**Scraped:** 2026-03-05T09:31:17.121442Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Risk-based alerting with entity-only rules
Supported in:
Google secops
SIEM
With the
ENTITY_RISK_CHANGE
Unified Data Model (UDM) event type, you can write YARA-L detection rules that trigger independently of ingested events. This capability lets you focus specifically on changes in an entity's risk score, significantly decreasing the time required for Google Security Operations to detect and alert on shifting entity risk levels. This document explains how to monitor risk scores using this UDM event type in your rules.
In Search, you can display events tagged with
ENTITY_RISK_CHANGE
using the following YARA-L syntax. Be aware that raw log search doesn't support entity search.
metadata.event_type = "ENTITY_RISK_CHANGE"
Examples: ENTITY_RISK_CHANGE rules
This section shows two single-event rule examples for efficient risk tracking, which helps you avoid the complexity and lower limits of multi-event rules. For information on your Rules quota, see
Display Rules quota
.
Detect when an entity's risk score exceeds 100
The following example rule uses the
ENTITY_RISK_CHANGE
event type to detect when an entity's risk score exceeds 100:
rule entity_only_risk_change {
  meta:
    author = "test@google.com"
    description = "Alert on entities crossing a threshold"
  events:
    // Check only Entity Risk Change events
    $e1.metadata.event_type = "ENTITY_RISK_CHANGE"

    // Check for a Risk Score change with 100 as the threshold 
    $e1.extensions.entity_risk.risk_score >= 100

  outcome:
    // Reset risk score to prevent feedback
    $risk_score = 0

  condition:
    $e1
}
Filter entities with risk scores over 0
The following example rule uses the
ENTITY_RISK_CHANGE
event type to track when the risk scores of entities exceed 0:
rule entity_only_risk {
  meta:
     author = "test@google.com"
     description = "Track changing risk per hostname"
  events:
     // Filter for Risk Change events with risk scores greater than 0
     $e1.metadata.event_type = "ENTITY_RISK_CHANGE"
     $e1.extensions.entity_risk.risk_score > 0

     // Deduplication
     $e1.extensions.entity_risk.risk_window_has_new_detections = true

     // Aggregation data
     $hostname = $e1.about.hostname
     $risk_score = $e1.extensions.entity_risk.risk_score
  match:
     $hostname over 5m
  outcome:
     $calculated_risk_score = sum($risk_score)
     $single_risk_score = max($risk_score)
  condition:
     $e1
}
Need more help?
Get answers from Community members and Google SecOps professionals.
