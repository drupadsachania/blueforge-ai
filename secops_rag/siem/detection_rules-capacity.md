# Google SecOps Rules Capacity

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/rules-capacity/  
**Scraped:** 2026-03-05T09:31:56.525011Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Google SecOps Rules Capacity
Supported in:
Google secops
SIEM
Overview
Google Security Operations Rules (also called curated detections) are rule sets created by Google Cloud Threat Intelligence (GCTI) that are used by Google SecOps customers. The Google SecOps Rules capacity limits how many rule sets can be enabled at any given time in a Google SecOps account.
Each rule set has a capacity value assigned to it. When any rules (Precise rules, Broad rules, or both) are enabled for a rule set, the rule set's full capacity is met and counted toward the Google SecOps Rules capacity. Additional rule sets can't be enabled when an account has reached its Google SecOps Rules capacity. The default Google SecOps Rules capacity for a Google SecOps account is 150.
Google SecOps rule capacity is not a count but the weight assigned to a
rule set. The weight of a rule set is based on its complexity. More complex rule
sets have a higher weight. The weight of a rule set is also affected by the number
of events that the rule set processes. Rule sets that process more events have
a higher weight.
The sum of weights must be less than 150. You cannot enable a rule set that
causes the sum of enabled sets to exceed 150. To view the weight of each
rule set in the console, go to
Detection
>
Rules & Detections
.
If you exceed the capacity for curated rules, you can continue to run the
existing rules, but you cannot create new rules. If you want a higher capacity,
contact your Google SecOps account team.
View capacity details
The
Rule Sets
tab on the
Curated Detections
page displays a
Capacity
column and a
Curated Detections Capacity
button (top-right).
The capacity value for a rule set represents the full capacity of the rule set. The rule set's full capacity is met if the rule set is enabled. A rule set is considered enabled when its Precise rules, Broad rules, or both, are enabled. When a rule set's capacity is met, the capacity is counted toward the Google SecOps rules capacity for the Google SecOps account. For example, if rule set A's capacity of 8 is met, and rule set B's capacity of 7 is met, then 15 is counted toward the total Google SecOps rules capacity. If the Google SecOps rules capacity is 150, then the rule set capacity is 15/150. To view the Google SecOps rules capacity for the account, click the
Curated Detections Capacity
status button. When the Google SecOps rules capacity is met, additional rule sets can't be enabled.
Check capacity before enabling all rule sets
You can enable all rules across all rule sets. However, this action requires that your account has a curated detections capacity that supports enabling all of your account's rule sets. For details on viewing the capacities of all of your rule sets to ensure that their total combined capacity when enabled won't exceed the total available Google SecOps rules capacity,
view capacity details
.
To enable all rule sets:
Click the
Quick Actions
pull-down menu.
Select
Set up recommended rule settings
.
Click
Enable all rules across all rule sets
.
Confirm your capacity usage: in
Rules & Detections
>
Rules Dashboard
, click
Rules Capacity
(top-right).
Need more help?
Get answers from Community members and Google SecOps professionals.
