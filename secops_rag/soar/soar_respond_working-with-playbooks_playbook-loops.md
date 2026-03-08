# Automate tasks with Playbook Loops

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops/  
**Scraped:** 2026-03-05T10:08:08.666795Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Automate tasks with Playbook Loops
Supported in:
Google secops
SOAR
The
Playbook Loops
feature focuses on
for-each
loops to iterate over 
lists and execute a set of actions once for each item.
With Playbook Loops, you can efficiently process multiple items, such as 
entities, by running a single action or a series of actions multiple times. This 
eliminates the need to customize actions or manually duplicate actions when you 
need to perform repetitive steps across multiple entities or other data types. 
You can also streamline workflows by placing blocks inside loops, or embedding 
loops within blocks.
Supported loop types
Playbook loops support iteration over the following data types:
Entities
: You can iterate over a list of entities within an 
    alert.
Lists
: You can iterate over a user-defined list of items or a 
    dynamically resolved list using a placeholder.
Structure your loops
A Playbook loop consists of a
Loop Start
step and a corresponding
Loop End
step. The actions you want to repeat for each item in your list are placed 
between these two steps.
Loop Start
The
Loop Start
step marks the beginning of your loop and includes its 
configuration.
You can assign a name to your loop in the
Loop Start
step. This 
    name is shown in both the
Loop Start
and
Loop End
steps.
This step defines the
Loop Over
parameter
    (
Entities
or
List
) and configures the specific settings for 
    the selected type.
This step lets you configure the loop's behavior when it reaches its 
    iteration limit (up to 1,000 iterations) or encounters an issue.
When the loop starts successfully, a checkmark appears.
Loop End
The
Loop End
step marks the endpoint of your loop.
You can't directly edit the
Loop End
step; its configuration is 
    tied to the
Loop Start
step.
When the loop completes all its iterations successfully, the
Loop End
step returns a success status (indicated by a checkmark) and 
    a JSON result includes the number of executed iterations.
If the loop stops before processing all items (due to reaching the 
    maximum iteration limit), the JSON result includes a list of skipped items.
Define actions within the loop
Actions placed between the
Loop Start
and
Loop End
steps run 
repeatedly. You can drag any standard playbook action into this area, including 
conditional actions and blocks.
Loops that iterate over entities
By default, when a loop iterates over entities, actions within that loop are 
only applied to the current entity in each iteration. The action processes one 
entity at a time as the loop progresses.
For actions that operate on entities (for example,
VirusTotal - Enrich 
Hash
), 
the action is automatically scoped to the current entity within the loop. Entity 
placeholders used within the loop also reference only the current loop entity.
To illustrate this, consider this use case:
Scan hashes and create tickets for malicious 
ones
.
Advanced loops that iterate over entities
In some use cases, you might need to access both the information of the 
current iterated entity and other alert entities. To achieve this, turn the
Lock scope to iteration
toggle to off for that specific loop action.
When the toggle is on, entity data and placeholders are restricted to the 
current looped entity only.
When the toggle is off, entity data and placeholders can access all alert 
entities, based on the configuration in the
Entities
menu.
Use
Entity
placeholders to access alert-wide entity data.
Use
Loop.Entity
to reference only the current looped entity.
To illustrate this, consider this use case:
Create priority tickets for malicious 
files based on user job title
.
Loops that iterate over lists
A loop can run a set of actions for each item in a defined list, where you 
can do the following:
Define the list directly or use a placeholder that resolves to a list.
Customize the delimiter based on your needs (for example, a comma or a 
  slash).
Reference the iterated item using the
Loop.item
placeholder.
To illustrate this, consider this use case:
Notify users about leaked passwords
.
Work with blocks inside loops
You can include
playbook blocks
directly within a loop. When a block is dragged into a loop, its actions run 
once for each item or entity the loop processes.
If the loop iterates over entities, the block includes a
Lock scope to iteration
toggle. This toggle controls how the actions 
 within the block access entity data:
Toggle on:
All steps inside the block are scoped to the current 
  entity in that specific loop iteration. This ensures that any entity 
  placeholders and actions in the block operate only on the relevant data for 
  that iteration.
Toggle off:
Steps inside the block have access to all alert 
  entities. The block receives all entities from the alert, not just the one 
  being processed by the parent loop. In this case,
loop.entity
placeholders are displayed in the menu and can be used to access the 
  iterated entity only.
Work with loops inside blocks
You can place loops inside playbook blocks to perform repeating tasks as 
part of the block's logic. This lets you iterate over items or entities within a 
scoped section of the playbook.
Configuring a loop inside a block follows the same process as setting up any 
other loop in a playbook.
For more details, see
Configure Playbook Loop actions
.
Configure Playbook Loop actions
To configure Playbook Loop actions, follow these steps:
In the
Navigation
menu, go to
Response
>
Playbooks
.
Open the playbook you want to modify or
create a new one
.
Click
+ Open Step Selection
.
Click the
Loops
tab.
Drag the
For Each Loop
action onto your playbook canvas. This 
    automatically creates the
Loop Start
and
Loop End
steps 
    with a designated area to add actions in between.
Configure the
Loop Start
:
Click the
Loop Start
step to open the
For Each Loop
side 
  drawer.
On the
Parameters
tab, select what to
Loop over
(
Entities
or
List
).
Entities:
Select the entity scope (
All Entities
,
Suspicious Entities
, or custom scope).
List:
In the
Items
field, enter your list of items, 
          either manually or with a placeholder. Define the
Delimiter
(for example, comma or slash) to separate items.
On the
Settings
tab, configure the loop's behavior:
Action type:
Choose between
Automatic
(starts 
          immediately) or
Manual
(requires user action).
If step fails or max iterations exceeded:
Select whether 
          the loop should
Skip
the remaining items and continue or
Stop playbook
.
Add actions before or after the loop to prepare data or process the loop's 
  results.
Limitations
Approval links
are not supported within playbook loops.
The number of steps supported within a loop is 100.
Work with Views and playbook Loops
This section explains how custom and prebuilt widgets display information 
from playbook loops within views, and covers important aspects of visualizing 
data from generated by loops.
Custom widgets
While you can't directly reference placeholders from internal loop steps, 
you can aggregate results during loop execution and display them in the 
widget. To display aggregated results in a custom widget, use context values 
within the loop (for example, use the
Append to Context Value
action from 
the
Tools
powerup).
Prebuilt widgets
Google provides prebuilt widgets that integrate seamlessly with supported 
actions in the playbook designer. When you drag a supported 
action into the playbook designer, the system suggests relevant prebuilt 
widgets. These widgets connect directly to the action, even when used inside a 
loop.
Loops in the playbook simulator
The playbook simulator offers detailed visualization for playbooks that 
include loops and blocks. It also supports nested structures, such as loops 
nested within blocks, and blocks nested within loops. Within the simulator 
viewer, steps display from top to bottom (oldest at the top, newest at the 
bottom), with automatic scrolling to show the latest activity.
For more information, see
Work with the Playbook Simulator
.
Case overview
When a playbook containing a loop runs, information about its progress and 
the results of each iteration can be found in several areas of the
Cases
page.
The following sections describe how widgets, the playbook viewer, and the 
Case Wall present information related to these loops.
Widgets
Prebuilt widgets in
Case Overview
results from their 
corresponding actions. If the action runs inside a loop, the widget updates 
dynamically to show results from the latest loop iteration.
Playbook viewer
When you run a playbook with a loop, you can track its progress and results 
of each iteration in the playbook viewer. To access this, select the relevant 
alert within the case and click the
Playbooks
tab.
The playbook viewer displays loops and blocks in a hierarchical structure. 
This organization helps you visualize the flow of nested processes and 
understand the context of each step.
Within the playbook viewer, you can do the following:
Review each iteration, as loop steps are grouped together.
Navigate between iterations to examine individual outcomes.
Select a step within a loop to display an iteration number in the side 
  drawer.
Click
View Results
to show the loop name and iteration number.
Click
Terminate Playbook
to manually end the playbook execution 
  to handle unwanted or excessive iterations.
Case Wall
Each result from the loop iterations appears on the
Case Wall
, along 
with a loop indication, such as the iteration number. This helps track and 
differentiate actions taken during each iteration.
Use case examples
This section provides practical examples of how playbook loops can be used to 
automate different types of workflows.
Scan hashes and create tickets for malicious ones
In this use case, perform the following steps:
Scan the hashes of all files in the alert using VirusTotal.
Automatically create a unique ticket for each file identified as malicious.
Create a playbook using the following steps:
Complete the following steps to create a playbook:
Drag the
VirusTotal - Enrich Hash
action onto the playbook canvas 
    and configure it before adding the loop.
Drag the
For Each Loop
onto the canvas.
Click
Loop Start
.
On the
Parameters
tab, select
Entities
as the
Loop over
type.
Select
All entities marked suspicious
from the
Entities
menu. 
        This step makes sure that the loop execution is scoped to only those 
        entities marked as suspicious by the
VirusTotal - Enrich Hash
action in the preceding step.
Drag a
Create Ticket
action into the loop. The exact name and 
    configuration of this action varies, based on the ticketing system 
    integration being used.
In the
Create Ticket
action's configuration:
Enter a ticket title, such as
Malicious File Detected
.
In the
Description
field, use the placeholder menu to 
            insert details about the current entity in the loop (for example,
Entity.Identifier
or
Entity.Type
). Include 
            any relevant information from the VirusTotal enrichment, now 
            associated with the suspicious entity.
For each file hash that VirusTotal identified as malicious, a unique ticket 
is created with the relevant details.
Create priority tickets for malicious files 
based on user job title
In this use case, after identifying malicious files (as done in the previous 
use case), create a new ticket with different priorities based on whether the 
internal user associated with the file has a job title containing "CEO."
Before you begin, ensure you have completed the initial steps from the 
previous use case:
A
VirusTotal - Enrich Hash
action before the loop, targeting all 
    file hash entities.
A
For Each Loop
action iterating over Entities with the scope 
    set to
All entities marked suspicious
.
To create priority tickets for malicious files, complete the following steps:
Add a conditional action inside the loop.
Turn off the
Lock scope to iteration
toggle to allow access to 
    other alert entities in addition to the looped entity.
Select
Internal Users
from the
Entities
menu.
Configure the condition to check if
Entity.job
contains
CEO
. This action sets the priority to
CRITICAL
.
Use the
ELSE
branch to handle a scenario where the
CEO
isn't involved (this will set the priority to
HIGH
).
Drag a
Create Ticket
action into the first branch:
Create the title (for example,
CRITICAL: Malicious File 
            Detected - Potential CEO Impact
).
Configure the incident priority to
CRITICAL
.
In the
Description
field, include relevant details about the 
        user and information from the VirusTotal enrichment.
Drag another
Create Ticket
action into the
ELSE
branch:
Create the title (for example,
Attention: Malicious File 
            Detected
).
Configure the incident priority to
HIGH
.
In the
Description
field, include relevant details about the 
        user and information from the VirusTotal enrichment.
For each malicious file, the playbook checks the associated internal user's 
job title. If the title contains
CEO
, it creates a
CRITICAL
priority ticket. Otherwise, it creates a
HIGH
priority ticket.
Notify users about leaked passwords
A data leak detection solution provides a list of usernames (email addresses) 
whose passwords have been compromised in a recent data leak. You want to send a 
personalized email notification to each affected user, rather than sending 
a single email to all users. The list of affected users is available in the
alert.affected_users
field.
Create a playbook using the following steps:
Drag a
For Each
Loop action onto the playbook canvas.
Click the
Loop Start
step.
On the
Parameters
tab, select
List
as the
Loop over
type.
In the
Items
field, use the
alert.affected_users
placeholder.
If the list in
alert.affected_users
uses a delimiter other 
    than a comma, update that delimiter in the
Delimiter
field.
Drag the
Email - Send Email
action into the loop.
In the
Email - Send Email
action's configuration:
In the
Recipients
field, use the
Loop.Item
placeholder. When the List loop iterates over the
alert.affected_users
list, the
Loop.Item
placeholder represents the current email address being processed, so 
            that each user receives a unique email.
Configure the
Subject
and
Content
of the email to 
            inform the user about the compromised password.
Each user (email address) in the
alert.affected_users
list 
receives a personalized email notification about their compromised password.
Need more help?
Get answers from Community members and Google SecOps professionals.
