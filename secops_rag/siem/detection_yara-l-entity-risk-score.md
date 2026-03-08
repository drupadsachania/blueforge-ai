# Specify entity risk score in rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/yara-l-entity-risk-score/  
**Scraped:** 2026-03-05T09:31:52.745767Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Specify entity risk score in rules
Supported in:
Google secops
SIEM
This document describes how to use entity risk scores in rules. In rules, entity
risk scores behave in a way that is similar to entity context. You can write YARA-L
2.0 rules to use risk scores as the main detection method. For more
information about rules on risk analytics, see
Create rules for Risk 
Analytics
. For more information 
on more risk-based context, see
Creating context-aware
analytics
.
To retrieve an entity risk score, join an entity with a UDM event and retrieve
the specified field from
EntityRisk
.
The following example shows how to create a rule to generate detections on
any entity hostname whose risk score is greater than 100.
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
remain unchanged within a 4-hour window, no new detections will be created.
The only supported risk windows for entity risk score rules are either 24 hours 
(86,400 seconds) or 7 days (604,800 seconds), respectively. If you don't specify 
a risk window size in the rule, it will be set by default to either 24 hours or 
7 days.
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
Need more help?
Get answers from Community members and Google SecOps professionals.
