# Understand rule replays and MTTD

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/rule-replays/  
**Scraped:** 2026-03-05T09:31:35.067958Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand rule replays and MTTD
Supported in:
Google secops
SIEM
This document explains how
rule replays
(also called
cleanup runs
) manage late-arriving data and
context updates, and how this affects the Mean Time To Detect (MTTD) metrics.
Rule replays
Google SecOps processes large volumes of security data. To ensure
accurate detections for rules that depend on contextual or correlated data, the
rule engine automatically runs a
rule replay
process.
The rule replay process handles two different categories of rules:
Single-event rules:
When the UDM enrichment process updates a previously
evaluated event, the system replays
single-event rules
.
Multi-event rules:
Multi-event
rules
execute
on a schedule selected by you, processing blocks of event time. These rules
repeatedly re-evaluate the same time block at different intervals to capture
late enrichment updates, such as matching user or asset context data or an
Indicator of Compromise (IOC).
For example, a rule might run at least two or three times (at 5-8 hours and again at 24-48 hours later) to account for late-arriving event and context data.
Rule replay triggers
The system re-evaluates (re-runs) rules when relevant context data arrives or when context data is processed
later than the initial event data.
Common reasons for replay include the following:
Late-arriving enrichment data:
Data enrichment pipelines, such as the
entity context graph (ECG)
, often process data in batches. When a UDM event
arrives before its related contextual data (like asset information or user
context), the initial rule execution might miss a detection.
Retroactive UDM enrichment updates:
Rules using
aliased fields
(enriched fields)
in
their detection logic, such as
$udm.event.principal.hostname
, can trigger
replays when source data (for example, DHCP records) are delayed. This late arrival retroactively updates those field values.
Subsequent rule replays use these newly enriched
values, potentially triggering a previously missed detection.
Impact on timing metrics
When a detection results from a rule replay, we use the following terminology:
The alert's
Detection Window
or
Event Timestamp
refers to the time of
the original malicious activity.
The
Created Time
is the time the system creates the detection, which can
be much later, sometimes hours or days later.
Detection latency
is the time difference between the
Event Timestamp
and the detection's
Created Time
.
Re-enrichment due to late-arriving data, or latency with a context source update
such as the
entity context graph (ECG)
typically causes high detection latency.
This time difference can make a detection appear "late" or "delayed", which can
confuse analysts and distort performance metrics like MTTD.
Metric component
Source of time
How replays affect MTTD
Detection Window / Event Timestamp
Time the original security event occurred.
This remains accurate to the event time.
Detection Time / Created Time
Time the detection was actually emitted by the engine.
This time appears "late" or "delayed" relative to the Event Timestamp because it relies on a secondary (replay) run that incorporates late enrichment data. This delta negatively affects the MTTD calculation.
Best practices for measuring MTTD
MTTD quantifies the time from initial compromise to the effective detection of the threat. When you analyze detections triggered by rule replays, apply the following best practices to maintain accurate MTTD metrics.
Google SecOps provides several user-queryable metrics to measure MTTD accurately. For details about these metrics, see
Sample YARA-L 2.0 queries for Dashboards page
.
A
lightbulb
icon in the
Detection Type
column identifies detections generated from event data that is delayed by more than 30 minutes, rule reprocessing runs, or retrohunts. This icon also appears on the
Alerts
page in Google SecOps.
Prioritize real-time detection systems
For the fastest detections, use single-event rules. These rules run
in near-real time, typically with a delay of less than 5 minutes.
This also supports more comprehensive use of
Composite detections
.
Account for rule replay in multi-event rules
Multi-event rules inherently incur higher latency due to their scheduled
run frequency
. When you measure MTTD for
detections from multi-event rules, recognize that automated rule replays increase
coverage and accuracy. These replays often catch threats requiring late
context, which increases the reported latency for those detections.
For critical, time-sensitive alerting:
Use single-event rules or
  multi-event rules with the shortest practical run frequencies. Reducing
  the match window doesn't directly affect latency, but it can increase
  efficiency by setting the minimum delay.
For complex, long-duration correlation (UEBA, multi-stage attacks):
These rules rely on extensive contextual joins or reference lists, which
  might update asynchronously. They can experience high latency with
  late-arriving contextual or event data, but they offer the benefit of
  higher fidelity detection rather than absolute speed.
Optimize rules to reduce reliance on late enrichment
To optimize for detection speed and minimize the impact of retroactive enrichment runs, consider using
non-aliased fields
(fields that are not subject to downstream enrichment pipelines) in your rule logic where possible.
Need more help?
Get answers from Community members and Google SecOps professionals.
