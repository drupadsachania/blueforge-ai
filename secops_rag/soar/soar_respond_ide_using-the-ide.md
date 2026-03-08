# Use the IDE

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/using-the-ide/  
**Scraped:** 2026-03-05T10:08:31.491733Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the IDE
Supported in:
Google secops
SOAR
This document explains the Integrated Development Environment (IDE) production mode. 
  The IDE is a framework for viewing, editing, and testing code. You can view
  the code of commercial integrations and create custom integrations from
  scratch or by duplicating commercial integrations code.
IDE is where you manage, import and export custom integrations.
Open the IDE
To open the IDE, follow these steps:
To open the IDE, in the main menu, go to
Response
>
IDE
. The
IDE
page opens.
On the
IDE
page, you can access the following options:
Option
Description
Integrations
Types
Choose between
Integrations
or
Types
(connectors, actions, jobs, managers).
Export
Import
Export individual or multiple items from an integration. Dependent items are included when exporting individual items, but not when exporting a full package.
The exported file is a ZIP archive containing a JSON file. When importing, you can add individual items to an existing integration or import a full package. The package must include an integrations.def file and the folders:
ActionsDefinitions
,
ActionsScripts
,
Dependencies
, and
Managers
.
toggle_on
Click the
Hide Inactive/Show All
toggle to
Show
or
Hide
deactivated items (actions, connectors).
add
Add
a new
        custom integration, connector, action, job, or manager.
Add a connector
To add a connector, follow these steps:
Click
add
Create New Item
and 
    select
Connector
.
Enter a name and the required integration.
Click
Create
.
Add integration details.
Add the required parameters.
Click the
Connector
toggle to enable the connector.
Click
Save
when done, or press
Ctrl + S
.
The following options are available in the
Details
tab:
Option
Description
delete
Delete
Available only for items in custom integrations.
play_arrow
Play
Runs the script's test method. Results appear in the
Testing
tab, and debug output appears in the
Debug Output
section.
file_json
Manage JSON sample
In the JSON sample import/export dialog, ensure
Include JSON Result
is enabled. You can then import or export JSON result samples for actions.
Details
Enter user-supplied input and other parameters, such as integration name.
history
Version Control
Version Control
        - Select an action/job/connector and click to see the following options:
Save as New Version
: Save the object as a new version with optional comments.
View Version History
: View and restore previous versions. Only available if at least one version has been saved. Click Restore to revert to any of the previous versions
        anytime. This is only available if you have clicked
Save as New Version
on an action/job/connector/manager previously.
file_copy
Duplicate item
Duplicate an item (job, action, connector, manager). After saving, the duplicate appears in the list without a
lock
Lock
icon.
Create a custom integration
Click
add
Create New Item
and select
Integration
.
Enter a name and click
Create
.
Select the created integration from the list and provide the following information:
Description
: appears in Content Hub and is visible to all Google Security Operations
        users.
SVG icon
: upload an SVG icon that appears with the integration.
Image
: upload a Content Hub image for Google SecOps users.
Libraries
: add Python libraries using pip.
Script dependencies
: Upload `.WHL`, `.PY,` `.TAR`, or `.GZ` files. These scripts add more functionality to your integration.
Parameter
: Add configurable fields with defined types, default values, and required status.
Click
Save
when done.
Create a job
To create a job, follow these steps:
Click
add
Create New Item
and select
Job
.
Enter a name and the required integration.
Click
Create
.
Optional: Add parameters for user or script input.
Click
Save
or press
Ctrl + S
.
Click
arrow_right
Play Item
to run the script.
Go to
Response
>
Jobs Scheduler
.
Click
add
Create New Job
and select the job that you just created.
In
Response
>
Jobs Scheduler
, choose the required time to run the job (script) that you created.
Create a new action to be used in a playbook
To create a new action for a playbook, follow these steps:
Click
add
Create New Item
and select
Action
.
Enter a name and the required integration
>
click
Create
.
Edit the code as needed.
Enable
Include JSON Result
if the action should return a JSON result in a playbook.
Optional: Add parameters to display as input fields.
Enable the action and click
Save
.
In
Polling Configuration
, you can set a timeout and a default
    return value if the action times out. You can also set a default value to
    return if the action doesn't complete within the defined timeout period.
The action is now available for use in
Playbook
>
Actions
.
Create a custom manager
To create a custom manager, follow these steps:
Click
add
Create New Item
and select
Manager
. Enter a name and the required integration.
Click
Create
.
Edit the code as needed.
Click
Save
.
IDE custom code security
To ensure a secure code execution environment, all custom Python code within 
the IDE runs in a sandboxed environment. This environment is isolated from the 
main server and operates with a low-privilege user. Access to the underlying operating 
system is strictly limited to an allow-list of non-administrative commands and directories 
required for typical integration and automation tasks. This sandboxing approach allows 
for robust security while providing the flexibility to execute a wide range of Python code.
Need more help?
Get answers from Community members and Google SecOps professionals.
