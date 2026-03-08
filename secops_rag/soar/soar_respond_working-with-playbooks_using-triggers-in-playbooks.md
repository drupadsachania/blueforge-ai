# Use triggers in playbooks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-triggers-in-playbooks/  
**Scraped:** 2026-03-05T10:07:55.316482Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use triggers in playbooks
Supported in:
Google secops
SOAR
A
trigger
is defined during the beginning phase of creating a playbook. It
  specifies the instance for which a playbook must be triggered in case of an
  alert detection. To add the trigger to a playbook, you must drag one of the
  triggers to the
Drag a Trigger over here
box in the
Playbook
>page.
Here's a breakdown of the playbook trigger options:
All
: Triggers the playbook for every single alert generated within that environment.
Alert Type
: Triggers based on the
Rule Generator
field, which is configured during connector setup. For details, see
Configure the connector
.
Product Name
: Triggers when an alert originates from a specific product (connector).
Tag Name
: Triggers if Google Security Operations automatically added a
  tag during ingestion and processing. Tags can be managed under
SOAR Settings
>
Case Data
>
Tags
.
Alert Trigger Value
: Triggers based on a predefined field from the
  connector. We recommend using
Custom Trigger
instead.
Custom Trigger
: Lets you define custom placeholders for highly specific matches. For example,
if alert name INCLUDES 'malware activity'
.
Custom List
: Triggers based on a predefined custom list configured in your settings.
Network Name
: Triggers if an alert involves an entity within a subnet defined in your settings. This ensures the playbook runs for alerts from those specific subnets.
Add a trigger to a playbook
Create a new playbook. For details about playbooks, see
Create and edit a playbook with Gemini
.
On the
Step Selection
menu, select
Triggers
.
Click
Alert Type
and drag it to the first step in the playbook. (For details, see
Use an Alert Type trigger in a playbook
).
Double-click it to open a new
Alert Type
dialog.
Under
Parameters
, select
Equal
,
Contains
, or
Starts With
.
Select the required parameter. In this use case, choose an alert
    type based on any alert that contains a phishing email detector.
Once you specify the trigger parameter and save it, the parameter name
    appears in the trigger's description.
You can now continue building the playbook with actions. For more information, see
Manage actions in playbooks
.
Need more help?
Get answers from Community members and Google SecOps professionals.
