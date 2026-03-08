# Configure timeouts for playbook async actions

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/how-do-i-configure-timeouts-for-playbook-async-actions/  
**Scraped:** 2026-03-05T09:35:13.709066Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure timeouts for playbook async actions
Supported in:
Google secops
SOAR
This document explains how to configure and manage timeout settings for Asynchronous
(
Async
) playbook actions. Async actions, which execute over an extended
period or require periodic checks, can have individual timeouts defined in the
Integrated Development Environment (IDE) and then customized within each playbook
step to facilitate workflow control and prevent resource blocking.
In the Google Security Operations platform, go to
Response
>
IDE
.
Click
add
Create New Item
to create a new action.
Enter the required details.
On the
Action Type
menu, select
Async
and click
Create
.
In the
Timeout configuration
section, various timeouts appear that you can define:
Script Timeout
: The amount of time for a single iteration of the action
to run to get a result (20 minutes maximum).
Async Action Timeout
: The amount of time until the action should stop
running altogether.
Async Polling Interval
: The amount of time the action waits before
trying again.
You can also add individual parameters in the
Details
tab.
Enable the action and click
Save
.
Go to
Response
>
Playbooks
.
Choose an existing playbook or create a new one, and then drag it into your new action.
Click the action. The
Async Action Timeout
and
Async Polling Interval
fields appear with the amounts configured in the IDE.
Need more help?
Get answers from Community members and Google SecOps professionals.
