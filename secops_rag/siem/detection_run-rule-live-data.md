# Learn how to apply a rule to live data

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data/  
**Scraped:** 2026-03-05T09:31:32.199840Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Learn how to apply a rule to live data
Supported in:
Google secops
SIEM
When you create a rule, it does not initially search for detections based on
events received in your Google Security Operations account in real time. However, you set the
rule to search for detections in real time by setting the
Live Rule
toggle
to enabled.
When a rule is configured to search for detections in real time, it prioritizes
live data for immediate threat detection.
To set a rule to live, complete the following steps:
Click
Detection
>
Rules & Detections
.
Click the
Rules Dashboard
tab.
Click the
more_vert
Rules
option icon for a rule and toggle the
Live Rule
to enabled.
Live Rule
Select
View Rule Detections
to view detections from a live rule.
Display Rules quota
At the top right of the Rules dashboard, click
Rules capacity
to display the limits to the number of rules that can be enabled as live.
Google SecOps imposes the following rule limits:
Multi-event rules quota
: Displays the current count of live-enabled multi-event rules and the maximum allowed. Learn more about the difference between
Single-event rules
and
Multi-event rules
.
Total Rules Quota
: Displays the current total count of rules enabled as "live" across all types, compared to the maximum allowed limit.
Rules executions
Live rules executions for a given event time bucket are triggered with decreasing frequency. A final cleanup run occurs, after which no further executions start.
Each execution runs over the latest versions of
reference lists
used in the rules, and against the latest
event and entity data enrichment
.
Some detections can be retrospectively generated if they're detected only by later executions. For example, the last execution might use the latest version of the reference list, which now detects more events, and events and entity data can be reprocessed due to new enrichments.
Deduplication
For rules that include a
match
section, Google SecOps
automatically identifies and removes detections and alerts that have identical
match variable
values and occur in
adjacent time windows. This deduplication feature helps reduce alert fatigue.
When you develop rules, be aware that the deduplication feature affects how many
detections and alerts are retained.
Deduplication exceptions
Google SecOps treats each rule version as distinct, new logic. As
a result, when you create a new version of a rule, it can trigger repeated
detections based on past events. Google SecOps does not remove
these detections, even if they appear to be duplicates.
Detection latencies
The time it takes for a live rule to generate a detection depends on various factors. For details, see
Understand rule detection delays
.
Rule status
Live rules can have one of the following statuses:
Enabled:
Rule is active and working normally as a live rule.
Disabled:
Rule is disabled.
Limited:
Live rules can be set to this status when they show
unusually high resource usage.
Limited
rules are isolated from the other live
rules in the system to maintain the stability of Google SecOps.
For
Limited
live rules, successful rule executions aren't always possible.
However, if the rule execution succeeds, detections are retained and available
for you to review.
Limited
live rules always generate an error message,
which includes recommendations about how to improve the performance of the rule.
If the performance of a
Limited
rule doesn't improve within 3 days, its
status is changed to
Paused
.
Note
: If there've been no recent changes to this rule, the errors might be intermittent
and could resolve automatically.
Paused:
Live rules enter this status when they've been in
Limited
status for 3 days and haven't shown any performance improvement. Executions for
this rule have been paused and error messages with suggestions on how to
improve the rule's performance are returned.
To return any live rule to the
Enabled
status, follow
YARA-L best practices
to
optimize its performance of your rule and save the changes. After the rule has been saved,
the rule is reset to the
Enabled
state, and it will take at least an hour
before it reaches the
Limited
status again.
You can potentially resolve performance issues with a rule by configuring it
to run less frequently. For example, you could reconfigure a rule from running
every 10 minutes to running once an hour or once every 24 hours. However,
changing the execution frequency of a rule won't change its status back to
Enabled
. If you make a small modification to the rule and save it, you can
automatically reset its status to
Enabled
.
Rule statuses are displayed in the
Rules Dashboard
and are also accessible
through the Detection Engine API. Errors generated by rules in the
Limited
or
Paused
status are available using the
ListErrors
API method.
The error indicates that the rule is either in the
Limited
or
Paused
status,
and provides a link to documentation on how to resolve the issue.
Need more help?
Get answers from Community members and Google SecOps professionals.
