# Take actions on a case

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action/  
**Scraped:** 2026-03-05T10:06:57.200777Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Take actions on a case
Supported in:
Google secops
SOAR
This document outlines the various actions you can perform on a case, including updating its status or priority, managing associated alerts, generating reports, and taking individual or bulk actions to streamline case handling.
Mark a case as important
When you want to highlight a case, you can mark it as important. You can also
  remove the
Important
tag from the same 
  menu.
To mark a case as important, follow these steps:
Click
format_list_bulleted
Case Actions
, select a case to tag, and select
Mark as important
;
a yellow
arrow_drop_up
appears with the case.
Mark a case as an Incident
If a case you're assigned is urgent and requires immediate action, mark it as an
Incident
. This automatically:
Sets the case priority to
Critical
Changes the case stage to
Incident
Assigns the case to the SOC Manager
Sends a notification to all analysts
To mark a case as an incident, follow these steps:
On the
Cases
page, go to the relevant case.
Click
format_list_bulleted
Case Actions
and select
Incident
.
In the
Confirmation
dialog, click
Yes
. The page refreshes
   and the new incident appears in the case list with the incident icon and a red critical sidebar. The case is automatically assigned to a user with the SOC Manager role.
Change the case stage
If you're assigned a case, you can update its stage, based on your team's workflow.
To change a case stage, follow these steps:
Select a case from the queue.
Click
format_list_bulleted
Case Actions
and select
Stage
.
Select one of the following stages:
Triage
: Initial phase when the case is created. This is the default.
Assessment
: The case is escalated to the next tier for evaluation.
Investigation
: The case is assigned an active investigation of alerts and entities.
Improvement
: The case is flagged for refining SOC detection rules or follow-up review.
Research
: The case is assigned a deeper investigation into external access or threat behavior to your organization.
Incident
: The final case stage for critical events. Once you select
Incident
, you can't change it.
Click
Save
.
Change the case priority
To change the case priority, follow these steps:
Select a case from the queue.
Click
format_list_bulleted
Case Actions
and select
Priority
.
Choose one of the following levels, each has a corresponding case color indicator:
Informative
(gray)
Low
(blue)
Medium
(yellow)
High
(orange)
Critical
(red)
Click
OK
. The case priority is changed.
Optional: Click the color swatch to change the case bar color.
Download a case report
You can download a case report in DOC, XLSX, or CSV format. Reports include the following details:
Case details
Alerts, entities, and insights
User and system activities
Playbook actions and case activity
All entries included in the case wall
To download a report, follow these steps:
Select a case from the queue.
Click
format_list_bulleted
Case Actions
and select
Report
.
In the
Select Report Type
dialog, select the file type and then click
Select
.
Open the downloaded file to view the report.
Manage alerts within a case
To manage specific alerts within a case, do the following:
On the
Alert Options
menu
Cases
page >
Alert
tab, click
more_vert
Alert Options
.
Select one of the available options:
Explore Alert
: For more information about the
Alerts Results
page, click
Investigate an alert
.
Ingest alert as test case
: Click
Ingest alert as test case
to add a new test case to the system. The system marks it as a
Test Case
for identification. Ingested alerts excluded from dashboards and reports and are not grouped with other alerts.
Change Priority:
We recommend changing the alert priority rather than the case's. Changing the alert priority doesn't affect the case's priority. For more information, see
Change alert priority instead of case priority.
Move Alert
: If you're assigned a case with multiple alerts, you can either
Move the Alert to new case
or
Move Alert to existing case
. If you select
Move Alert to existing case
, choose the destination case from the menu and click
Move
.
Manage Alert Detection Rule
: Available only for Google Security Operations users.
If the rule is a predefined Google SecOps rule, the system redirects you to the
Rules Detection
page. For more information, see
Filter data in the Rule Detections view
.
If the rule is a customer rule, the system redirects you to the
Rules Editor
page. For more information, see
Manage rules using the Rules Editor
.
Close Alert:
Closes the alert within the case. Select a value from the
Reason
,
Root Cause
, or
Usefulness
field.
The
Usefulness
field appears only for Google SecOps users and helps rule analysts get more precise feedback on alert rules from customer input.
Closed alerts in a case appear unavailable and display a
Closed
tag. You can only close an alert if other alerts are present in the case and it's assigned to you.
Add Entity:
Manually add an existing or new entity to an alert.
Run a manual action in a case
Manual actions and playbook actions become available after you install the corresponding integration from the Content Hub.
To run a manual action in a case, follow these steps:
In the selected case, click
Manual Action
.
In the
Manual Action
dialog, select the required action. For example, select
VirusTotalV3
>
Enrich URL
. Enter the required information.
Select the alerts and entities the action should apply to.
Click
Execute
to display the action details on the case wall.
Simulate cases in Google SecOps
You can simulate a case populated with
system-generated default alerts. Simulated cases are useful in staging
environments or for demonstrations.
You can also create custom cases or import existing cases in JSON format
using files with the `.CASE` suffix.
To simulate a case, follow these steps:
In the
Case queue
header, click
add
Add a Case
, then select
Simulate Cases
.
In the
Simulate Cases
dialog, select a case from the 
  list.
Click
Create
.
Create a new case
To create a new, simulated case, follow these steps:
In the
Simulate Cases
dialog, click
add
Add or import case
, then click
Add New Case
.
In the
Add New Case
dialog, enter the
Source/SIEM Name
,
Rule Name
(Rule
    Generator),
Alert Product
,
Alert Name
,
Event Name
Optionally, you can also provide:
Additional Alert Fields
Additional Event Fields
Click
Save
. The case appears in the
Simulate Cases
list.
Select the newly created case and click
Create
.
Select the target environment and click
Simulate
. The new case 
  appears in the queue.
Import a case to a JSON file
To import a case to a JSON file, follow these steps:
In the
Simulate Cases
dialog, click
add
Add or import case
, 
    then click
Import Case
.
Select the required case and click
Open
. The case is imported in 
    JSON format.
Perform batch actions on multiple cases
You can perform batch actions on multiple cases on the
Search
page.
Available batch actions include the following:
Export to CSV
: Downloads a list of selected cases and their metadata in CSV format for offline review or reporting.
Close case
: You can close cases using various interface options, including the case details page, the case queue (side-by-side and list views), and the Search page. You can close a case once it's resolved.
Reopen case
: Reopens previously closed cases to resume investigation or follow-up actions.
Change priority
: Updates the priority level (Low, Medium, High, or Critical) of selected cases to reflect urgency or severity.
Assign case
: Assigns a case to a specific user or group for further investigation.
Add tag
: Applies one or more tags to selected cases to support filtering, categorization, or automation rules.
Merge cases
: Combines multiple related cases into a single case to reduce duplication and centralize investigation.
Change stage
: Updates the stage of selected cases to reflect their progress or status.
To perform a batch action, follow these steps:
Go to
Investigation
and click
SOAR Search
.
Select the timeframe for the relevant cases.
Select the cases using the required filter.
Select the checkboxes to apply the relevant filters
>
Apply
.
In the
Results
list, select the checkboxes for the cases you want to modify.
Select an action from the
Search Results
menu.
Quick actions
The
Quick Actions
widget lets you define reusable actions that you can
execute directly from cases and alerts. You can add this widget to the default
case view, default alert view, and custom alert views in playbooks.
Defining parameters for Quick Actions is optional. If provided, you can
review and modify them before execution. If left blank, parameters must be
filled in at runtime.
If an integration is removed after a Quick Action is configured, the 
corresponding
Quick Action
button is hidden, and the widget is flagged in the 
configuration view to indicate a missing integration.
For setup instructions, see the following:
Define default case view
Define default alert view
Define customized alert views from Playbook Designer
Use case: Configure Quick Action for malicious file investigation
This use case shows how to create a Quick Action that helps investigate potentially malicious files within a case.
Add the Quick Actions widget
Go to
SOAR Settings
>
Case Data
>
Views
.
Select
Default Case View
.
Select the
General
tab.
Drag the
Quick Actions
widget into the
Default Case View
.
Configure the widget
Click
settings
Configuration
.
In the
Quick Actions
side drawer, enter
File Investigation
for the widget title.
For the widget description, enter
Quickly scan file hashes.
Optional: choose a widget width.
Click
Advanced Settings
.
In the
Conditions
section, define the criteria for displaying the 
  widget. To show the widget only when a case is tagged with
malicious-file
, use the condition
Case.Tags
contains
malicious-file
.
Add a Scan Hash button
In
Text
, you can provide instructions or context for
  directly within the widget. For this use case, add the following 
  text:
Use the 'Scan Hash' button to check suspicious files.
In
Buttons
, click
+ Add New Button
to create a 
   new Quick Action. You can add up to six buttons, each corresponding to a 
   different Quick Action.
In the
Add Button
dialog that appears, configure the Quick Action 
  (
Scan Hash
):
Name
: Scan Hash
Button Color
: Choose a color.
Action
: Select
Scan Hash
from the VirusTotal section in 
      the
Action
list.
Optional: choose the relevant
Instance
for VirusTotal.
Optional: in
Parameters
, define the
Hash
parameter:
Hash:
[Case.FileHash]
In the
Add Button
dialog, click
Close
.
In the
Quick Actions
side drawer, click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
