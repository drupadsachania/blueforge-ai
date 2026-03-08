# Understand rule quotas

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas/  
**Scraped:** 2026-03-05T10:03:50.335741Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand rule quotas
Supported in:
Google secops
SIEM
Google Security Operations enforces capacity limits on detection rules to ensure
consistent system performance and query speed.
Rule capacity is managed through the following two categories:
Custom rules
: Rules written and managed by your team.
Curated detections
: Rules written and managed by Google.
Track custom rule quota
Custom rules are subject to strict performance quotas based on their complexity.
To track custom rule quota, do the following:
In Google SecOps, go to
Detection > Rules & Detections
.
Go to the
Rules dashboard
tab.
Click
Rules capacity
to open the
Multiple events rules quota
dialog.
It displays the
Multiple events rules
and the
Total rules
quotas.
Quota type
Description
What counts toward the quota
Total rules quota
The maximum number of enabled rules allowed in the environment.
All active rules: Single-event and multi-event.
Multiple events rules quota
A restricted subset of the total quota reserved for multi-event rules.
Only multi-event rules: Rules that correlate multiple events over time, use joins, or perform
windowed aggregations
(for example, rules with a match section).
Single-event rules
count only toward the total active quota.
Multi-event rules
consume capacity from
both
the total active and multi-event quotas
simultaneously.
Multi-event rules consume significantly more resources than single
event rules. You might have available space in your
total
quota but be
blocked from enabling a new rule if you have exhausted your
multi-event
quota.
Track curated detections quota
Curated detections are available for Enterprise and Enterprise Plus customers.
The license entitlements are explicitly sized to accommodate the entire library
of curated rule sets. While the dashboard provides
Capacity
or
Weight
metrics, these figures are informational, and not hard limits.
For Enterprise and Enterprise Plus customers, license entitlements are
explicitly sized to accommodate the entire library of curated rule sets.
While the dashboard provides
Capacity
or
Weight
metrics, these figures
are informational, and not hard limits.
You can activate all curated rule sets simultaneously without risking
performance trade-offs or hitting a capacity ceiling. If a limit warning
triggers, verify your license package configuration.
Optimize system performance
This section outlines optimization strategies to maximize your rule capacity and
system performance.
Modularize complex logic
Create lightweight, single-event rules to flag atomic behaviors. That is, avoid
writing massive multi-event rules that attempt to detect every stage of an
attack from raw logs.
Detect signals with single-event rules
Create single-event rules for individual behaviors (for example,
User Login Failed
,
Process Launched
).
Impact
: Consumes the total active quota (abundant) and runs in near
real-time.
Correlate alerts with composite or multi-event rule
Write a composite rule which uses the detections generated in step 1 as
input.
Impact
: Consumes multi-event quota (expensive).
Benefit
: You use the multi-event quota once for the logic, rather than
reprocessing raw logs multiple times for different scenarios.
Create an efficient rule design
Prioritize single-event logic
: If a detection can be done with a single
log line (for example, "User visited a known bad domain"), write it as a
single-event rule to save your multi-event quota for correlations. Avoid using
a match window.
Use reference lists
: Instead of
N
rules for
N
indicators, use a
single rule that references a reference list (for example,
target.ip in %suspicious_ips
). This consumes only one unit of rule quota.
Perform regular audits:
Regularly audit paused or disabled rules.
While they don't count toward active quota, archiving them keeps the
environment clean.
Use case: Detect lateral movement through brute force
Scenario:
Detect an attacker who attempts to brute force their way into a
server through Risk Data Platform (RDP) and immediately executes a suspicious
administrative tool (like PsExec) to move laterally.
Step 1: Detect signals with single-event rules
Create two lightweight rules that run on the abundant total active quota.
These generate detections.
Rule A (brute force signal):
Logic
:
Check for
auth.status = FAILURE
.
Group login events.
Trigger if more than 5 failed attempts in 1 minute.
Input
: Raw UDM events.
Output
: A detection alert named
Possible_RDP_Brute_Force
.
Cost
: Low (uses total active quota).
Rule B (suspicious tool signal)
:
Logic
: Trigger if the process is
psexec.exe
.
Input
: Raw UDM events.
Output
: A detection alert named
PsExec_Usage
.
Cost:
Low (uses total active quota).
Step 2: Correlate alerts with composite rule
Write one composite rule that looks at the detections generated in step 1, not
the raw logs.
Rule C
:
Logic
: Look for
Possible_RDP_Brute_Force AND PsExec_Usage
occurring on the same
principal.hostname
within 10 minutes.
Input
: Detections from rules A and B.
Cost
: High (uses multi-event quota) but only processes the few
alerts generated in step 1.
This tiered approach optimizes for both performance and cost-efficiency by
decoupling initial signal generation from complex correlation logic. By
filtering billions of raw UDM events into high-fidelity detections using
single-event rules, you reduce the data volume processed by the multi-event
engine.
Need more help?
Get answers from Community members and Google SecOps professionals.
