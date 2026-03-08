# Assign actions and playbook blocks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks/  
**Scraped:** 2026-03-05T10:08:22.628266Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Assign actions and playbook blocks
Supported in:
Google secops
SOAR
You can assign actions or playbook blocks to a specific user or SOC role in the
 playbook designer. The assignee decides the outcome of the manual action or
 playbook block for the playbook run. You can include a message about the action
 that needs to be taken by the assignee. You can also enable
Time to respond
and add the time they have to complete the action. The timer starts the
 countdown from when the playbook reaches that part of the flow.
If they don't respond in the time allotted to complete the action, the action will fail.
 When you build your playbook, make sure to use
If Step fails
to decide
 whether to stop the playbook entirely at this stage or skip this step. You can
 also use the conditional step
If previous Step failed
to push
 the playbook flow in a different direction.
For more information on assigning actions to end users, refer to
Assign Approval Links in Actions
.
Assign an action in a playbook
Double-click the required action in the playbook.
Select
Manual
from the
Action Type
list.
Select the user or SOC role from the
Assign To
list.
Add a message explaining what needs to be done. You have the option to
 insert a placeholder in your message. This message is displayed to the
 user in the
Pending Actions
widget in the case overview and in
Your Workdesk
Optionally, enable
Time to respond
and enter the time that the action
 needs to be completed by.
If the user doesn't respond in the time selected, you can choose to use
 the
If Step fails
together with
If previous action fails
in the
 next playbook conditional step to control the flow.
Click
Save
.
After a playbook is triggered, usually following an alert being ingested into
the platform, it runs until it gets to the manual action. This action appears
in the
Pending Actions
widget in the case overview and in
Your Workdesk
. The user needs to execute or skip the action.
Assign playbook blocks
Open the required playbook with an existing block.
Double-click the playbook block. Note that the block is displayed in green.
Select
Manual Action
from the
Action Type
list.
Select the user or SOC role from the
Assign To
list.
Add a message explaining what needs to be done. You have the option to insert a
placeholder in your message. The user will receive a message when their input is
required.
If required, enable the
Time to Save
field and enter the time for the
assignee to approve or decline the playbook block.
Click
Save
.
After a case has been ingested into the platform and an alert triggers the
playbook, it runs until it gets to the manual action. The manual action appears
in the
Pending Actions
widget in the case overview and alert overview or
on
Your Workdesk
. If the
Time to respond
field has been filled
out, then a ticker will appear with the time the user has left to respond to
this action.
Need more help?
Get answers from Community members and Google SecOps professionals.
