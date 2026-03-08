# Rerun playbooks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/rerun-playbooks/  
**Scraped:** 2026-03-05T09:34:38.203484Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Rerun playbooks
Supported in:
Google secops
SOAR
This document describes how to rerun a playbook associated with a case alert. This feature allows for up to nine reruns (10 total runs, including the initial execution) per alert.
This feature can be useful in the following situations:
Data freshness
: Obtain more up-to-date results after the initial run.
Error recovery
: Rerun the entire playbook following one or more failed steps.
Logic updates
: Run the playbook with new logic after making changes on the
Playbooks
page.
To rerun a playbook, follow these steps:
On the
Cases
page, go to the
Playbooks
tab of the selected alert.
Locate the playbook you want to rerun.
Click
replay
Rerun Playbook
.
Each time you rerun the playbook, the system updates the iteration number and writes informative messages to the case wall.
Need more help?
Get answers from Community members and Google SecOps professionals.
