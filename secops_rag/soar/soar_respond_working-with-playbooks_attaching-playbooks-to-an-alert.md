# Attach playbooks to an alert

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/attaching-playbooks-to-an-alert/  
**Scraped:** 2026-03-05T10:08:19.143454Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Attach playbooks to an alert
Supported in:
Google secops
SOAR
This document outlines the attachment limits and priority settings for playbooks associated with a single alert in Google Security Operations, followed by the steps necessary to manually add a playbook or playbook block to an active alert.
You can attach a total of 10 playbooks to any single alert in Google SecOps.
Only one playbook can be attached automatically (via an alert trigger).
An additional nine playbooks can be attached manually.
You can set the playbook's priority between
1
(highest priority) and
3
(lowest priority). If multiple playbooks are attached, the playbook
  with the highest priority is executed first. The default priority is
2
(medium).
Manually attach a playbook or playbook block
To add a playbook or playbook block to an alert, follow these steps:
On the
Cases
page, click the alert within the case where you wants to add the playbook.
On the
Playbooks
tab, click
add
Add Playbook
. Choose the playbook
 or the playbook block to be added.
Select the playbook or playbook block to add, and set the playbook priority (the default is
2
).
If the selected playbook block requires input parameters, the
Inputs
dialog appears. Confirm  or modify the existing inputs as needed. (If no inputs are required, this dialog is skipped.)
The added playbook block appears on the
Playbooks
tab in the case alert.
Need more help?
Get answers from Community members and Google SecOps professionals.
