# Change alert priority instead of case priority

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/changing-alert-priority-instead-of-case-priority/  
**Scraped:** 2026-03-05T09:34:33.542440Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Change alert priority instead of case priority
Supported in:
Google secops
SOAR
This document outlines the best practice for managing priority within security cases. As such, we highly recommend setting and changing priority at the alert level instead of directly changing the case priority. This practice leverages the system's priority inheritance model to prevent severe issues from being misclassified.
Risk of direct case priority changes
If you change the case priority directly, each incoming alert and its attached playbook logic can override the established case severity.

For example, if a
Critical
alert is grouped with a subsequent
Low
alert, the case priority may drop to
Low
, causing important issues to go undetected.
Alert-level priority benefits
When you change the alert priority, the case automatically inherits the highest priority of all grouped alerts. This inheritance makes sure that a subsequent alert with a lower priority doesn't override a critical severity previously assigned by another alert.
Change the priority of an alert
There are two ways you can change the priority of the alert:
Action-based
: Use the
Change Alert Priority
action, configured either within a playbook or run as a manual action.
Direct modification
: Change the priority through the alert interface:
On the
Cases
page, click
more_vert
Alert Options
and select
Change Priority
.
On the
Change Alert Priority
dialog, select the required priority
    and click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
