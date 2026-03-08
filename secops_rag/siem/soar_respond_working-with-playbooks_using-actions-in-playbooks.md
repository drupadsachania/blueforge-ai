# Manage actions in playbooks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks/  
**Scraped:** 2026-03-05T09:34:49.686706Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage actions in playbooks
Supported in:
Google secops
SOAR
Actions are the next set of components that you can define for a playbook.
Each action is categorized under an integration in the system. They include tasks
or actions to be performed by the playbook. For example, you can assign an
analyst to a case, or in case of an external product integration (such as
Trellix ePO product), you can set an action to update the Trellix Agent. For each
integration, there's a list of sub-actions.
Before you begin
To use the required actions, make sure you have the integrations downloaded
and configured from the Content Hub. For more information
about integrations, see
Configure integrations
.
When the playbook runs, each action returns information that can include the following:
Output message, tables, attachments, links, JSON
Script result (only valid within the playbook itself)
You can view this information on the case wall or on the cases page.
Understand key terms for actions
The following is a list of terms within actions:
Parameters
: Input of some type including text, placeholder (Google SecOps variable), or list options.
Placeholders
: Google SecOps variable which is populated at running time. For details about parameters and placeholders, see
Use the Expression Builder
.
Enrichment
: Gathers more information and attributes on an entity. Learn more about
using enrichment
.
Script Result
: Google SecOps-defined return value of an action.
JSON Result
: Raw data that the action returns.
Expression Builder
: Enables manipulating JSON results and extracting specific data to use in Playbook actions. For details, see
Use the Expression Builder
.
Add an action
To add an action to the playbook, do the following:
On the
Response
>
Playbooks
page, click
Add Step
.
On the
Step Selection
tab, select the
Actions
section.
In the
Actions
section, click
arrow_drop_down
Down Arrow
next to an integration
name and select the action item. In this example, select
Email
>
Send Email
.
Drag the
Send Email
item to
Drag a step over here
.
Double-click to open the sidebar. The sidebar displays the action's name and
description, along with the final action result (shown by the Output Name). For this
procedure, assume you're in the middle of a data loss protection (DLP) use case playbook and
configure the fields as required.
Choose the instance to use for this playbook. For more information, see
Support multiple instances
.
Define the entities the action will run on.
Set the email recipient for this action by inserting an
Entity Identifier
placeholder. For this example, add
an Entity Identifier placeholder.
Add a placeholder
To add a placeholder, do the following:
In the
Recipients
field, click the placeholder icon ([ ])
In
Placeholder Selection
, select
Object
>
Entity.Property
>
Identifier
.
Click
OK
.
Click
Save
. The action is saved as
Action name_Sub Action name
.
Assign actions
In the Playbook Designer, you can assign actions or playbook blocks
to a specific user or SOC role. The assignee determines the outcome of that step
in the playbook run. You also have the option to include a message about the
required action and enable a
Time to respond
countdown. The timer starts
as soon as the playbook reaches that point in the flow. For more information,
see
Assign actions and playbook blocks
.
To assign an action in a playbook, do the following:
Double-click on the required action in the playbook.
In the
Action Type
list, select
Manual
.
In the
Assign To
list, select the user or SOC role.
Add a clear message explaining the required action. You can insert a placeholder in this message, which is then displayed to the user in the
Pending Actions
widget on their homepage and on the
Cases Overview
page.
Optional: You can enable
Time to respond
to set a deadline for the action's completion. If the deadline isn't met, the action fails. To manage this outcome, configure the subsequent conditional step in your playbook to use the
If previous action fails
setting to control the flow.
Click
Save
.
After a playbook is triggered (usually by an ingested alert), it runs automatically until it reaches a
Manual Action
level. This action pauses the playbook and appears in the
Pending Actions
widget on the homepage and the
Case Overview
, which requires a user to execute or skip it to continue the flow.
Add enrichment to entities
Enrichment is additional data collected on an entity (such as hostnames, IP addresses, and artifacts).
On the
Cases
tab, click an entity to see all the existing attributes that belong to it. These attributes, also known as
enrichment parameters
, can also be used in placeholders. If an entity is missing attributes you need, use an action to execute enrichment. To do this, follow these steps:
Under the case top bar, click
settings
Manual Action
to open the
Manual Actions
dialog.
Select
Google Workspace > Enrich Entities
, and then select a specific entity. In this example, select the user
Javier
.
Click
Execute
. Once the green arrow appears, close this box.
In
Entities Highlights
, click the entity
Javier
. A new Entity Explorer page appears.
On the
Entity Explorer
page, scroll to see who Javier reports to.
Return to the main case page. All the enrichment attributes are now in the Google SecOps platform and are treated as entities in and of themselves. For example, the person that Javier reports to now can be chosen as an entity.
Create a new entity
The analyst chooses the required entity when building the playbook. There are different sets of entities that the action will run on. You can also choose to add new entity sets.
To create a new entity for a single playbook, do the following:
In the
Actions
column, select
Flow > Entity Selection
, and drag it into the final step.
Click
Entity Selection
.
Select the required entity parameters. In this example, select
Reports To entity
(now populated in the system due to the enrichment action you ran earlier).
Set its value to
Director
and click
Save
.
The new entity set is saved as
Entity_Selection_1
and is immediately available for use within this playbook. If you create additional sets, they are sequentially numbered (for example,
Entity_Selection_2
,
Entity_Selection_3
).
Edit and manage playbook steps
Cut, copy, delete, or paste
: Right-click the required step to access the
Edit
menu. You can copy and paste steps within the current playbook or to a different one.
Select multiple steps
: Press the
Shift
key while you left-click to select multiple steps. Then, right-click any highlighted step to perform a bulk action (
Cut
,
Copy
,
Delete
, or
Paste
).
Configure step
: Double-click any step to open its configuration settings.
Rerun an action
When an action fails and causes the playbook to stop, you can often fix the
issue and resume the flow. When this happens, select the failed action to view
the error message, correct any mistakenly entered parameters, and then rerun the
action.
Need more help?
Get answers from Community members and Google SecOps professionals.
