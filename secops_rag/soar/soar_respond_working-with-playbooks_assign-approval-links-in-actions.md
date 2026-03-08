# Assign approval links in actions

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-approval-links-in-actions/  
**Scraped:** 2026-03-05T10:08:26.549325Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Assign approval links in actions
Supported in:
Google secops
SOAR
Use
Approval links
to send manual actions waiting for user
input (pending actions) to users
outside
of the platform.
For example, if you're working with an end user that doesn't have access to
Google Security Operations, you could email them the approval link and (similarly to the
Pending actions
widget or the
Pending Actions
tab in
Your
Workdesk
), they can approve or decline the action from wherever they are.
As a Managed Security Service Provider (MSSP), you want to quarantine an infected computer on
your end customer's site but you want the IT manager in the end customer's
company to approve this action first. To send out this request to approve or
decline the action to the IT Manager in an email, you'll need to assign an
approval link in the action.
Assign an approval link in an action
This use case describes how an MSSP can build a playbook based on a suspicious phishing alert.
In the playbook you're building, select the
Carbon Black Quarantine
Device
action. This action is the one you want the end user to approve.
Change the
Action Type
to
Manual
. The
Approval link
toggle appears.
Click the
Approval link
toggle to on. This automatically creates
placeholders (with links to approve or decline the Quarantine Device) which can
then be used in any action
preceding
this one in the playbook.
You can assign the manual action to a specific user or SOC role, or leave it
blank.
Optionally, you can enable the
Time to respond
toggle in conjunction
with the
Approval link
toggle. This will specify a specific time by which
the end user (or indeed anybody in the platform) must respond to the email by
clicking one of the links.
Drag a
Send Email
action to directly
before
the
Carbon
Black Quarantine Device
action in the playbook.
In the
Send Email
action, fill out the recipient email address.
While in the email body, click
data_array
Placeholder
and click individual
Approve
and
Decline
links to place them in the message.
Make sure you've written an email first before you add the
placeholders.
Pro Tip
: Wrap the sentence in HTML links so that the approval link appears as a
hypertext link.
Save your playbook.
After you save your playbook, an incoming alert that matches the trigger starts the execution. When the flow reaches the
Send Email
step, an email is sent to the recipient containing the
Approve
and
Decline
action links.
These approval links are fully portable; you can use them in various places, such as an
HTML
widget in a custom playbook view, a
Send to Slack
action, or a
Send SMS with Twilio
action.
Need more help?
Get answers from Community members and Google SecOps professionals.
