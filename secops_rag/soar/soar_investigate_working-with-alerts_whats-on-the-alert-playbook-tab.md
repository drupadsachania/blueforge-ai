# Explore the playbooks tab in alerts

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/whats-on-the-alert-playbook-tab/  
**Scraped:** 2026-03-05T10:07:35.069307Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Explore the playbooks tab in alerts
Supported in:
Google secops
SOAR
This document provides a reference for the
Playbooks
tab, which appears on the
Cases
page when a Playbook is attached to an alert.
When you select a Playbook from this tab, a side drawer opens to display the execution summary and key metrics.
Playbook name and status
: The name of the playbook and its 
    current run status.
Pending Action: waiting for user input
: The playbook is waiting 
    for an analyst to take action. A push notification also informs the relevant 
    user that the playbook is awaiting their input.
Time and length of playbook run
: Shows the start time and the 
    total duration of the playbook run.
Integrations
: List of integrations used by this playbook.
     When you click an integration, it marks the specific step in the
    playbook viewer, letting the analyst to focus on it.
Playbook flow
: Each step that was run with its status and step
    result.
Errors
: List of errors. Errors that stop the playbook are highlighted
    at the top of the summary, while skipped actions appear at the bottom. You
    can also choose to rerun the action or playbook from this point.
You can click any of the playbook steps to see information relating only to
  that step in the side drawer.
The following actions are available at the top of the
Playbooks
tab:
autorenew
Refresh
: Updates the
Playbooks
tab to display the latest information.
Jump to Case Wall
: Takes you to the case
    wall directly from the
Playbooks
tab.
add
Add Playbook
: Choose the playbook to add to the case.
Click
replay
Rerun Playbook
to rerun playbooks attached to alerts. For more information,
see
Rerun playbooks
.
Need more help?
Get answers from Community members and Google SecOps professionals.
