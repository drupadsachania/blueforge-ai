# Use an Alert Type trigger in a playbook

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-alert-type-trigger-in-a-playbook/  
**Scraped:** 2026-03-05T09:35:05.703889Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use an Alert Type trigger in a playbook
Supported in:
Google secops
SOAR
This document describes how to use the
Alert Type
trigger to trigger a
  playbook, based on the
Rule Generator
name.
Go to the
Response
>
Playbooks
page and create a new playbook.
Drag the
Alert Type
trigger to a playbook step and double-click it to
    open it.
The
Parameters
field requires the Rule Generator name of each alert
    that can trigger this playbook. Select the Rule Generator name from the menu.
If you don't remember the Rule Generator name of the alert you want to trigger, go to
Cases
>
Overview
.
In the
Alerts
widget, click
View Details
. The side drawer opens with case details.
Copy and paste this Rule Generator name, or select it from the menu.
Continue building the playbook. Once you've finished, this Rule Generator triggers the
  playbook for generated alerts.
Need more help?
Get answers from Community members and Google SecOps professionals.
