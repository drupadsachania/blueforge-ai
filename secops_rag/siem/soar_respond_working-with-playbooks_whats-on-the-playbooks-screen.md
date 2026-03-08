# Explore the Playbooks page

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen/  
**Scraped:** 2026-03-05T09:34:47.083158Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Explore the Playbooks page
Supported in:
Google secops
SOAR
A playbook is built on triggers, actions, and flows, working together to automate incident response and other security operations tasks. When a trigger initiates a playbook, it proceeds through a series of defined actions to achieve a specific resolution.
The execution of a playbook follows an organized progression:
Trigger
(yellow box): This is the mandatory first component that initiates the playbook. It defines the conditions or events that cause the playbook to run.
Actions
(blue box): After the trigger, the playbook moves to a set of defined actions it must perform. These are the specific tasks or operations the playbook executes, such as enriching data, notifying users, or isolating a compromised host.
Flow
(purple box): The final component involves determining the flow of the playbook, typically using `if-then-else` conditions. This method gives the playbook the ability to make decisions based on the outcomes of previous actions and branch into different paths to reach a final resolution.
Open the Playbooks page
To open the
Playbooks
page, go to
Response
>
Playbooks
.
The following actions are available:
Plus
: Add a new playbook or block. Select the folder and
    environment for your new playbook or block. You can select one or multiple
    environments, environment groups, or a combination of both. If a
    playbook is associated with a specific environment group, its
    scope automatically updates if the environment group's scope changes.
Edit
: Select single or multiple playbooks and
    blocks for use with the
Actions
menu. To rename a folder, click
Edit
, hold the pointer over the folder name, and enter
     the new name. Once you edit a playbook, you can delete playbooks, as needed.
Filter
: Click
filter_alt
Filter
and filter the display based on the following criteria:
Playbook simulator is on
toggle
Show Active Playbooks
toggle
Priority
: Set the attachment order of playbooks for the alert.
        Only one playbook attaches automatically, based on priority.
Environments
: Multi-select option for environments and environment groups.
Menu
: Click
edit
Edit
and select the required playbooks or blocks before using
Menu
to perform bulk actions:
New Folder
: Add a new playbooks folder; the playbook automatically inherits any changes made to its associated environment groups. You can apply playbooks associated with environment groups to cases originating from any environment within those groups.
Duplicate
: Create a duplicate playbook with these options:
Keep or change priority
Keep in same folder or move to a different folder
Single
,
multiple
, or
all
environments, where
all
indicates all defined environments, present or future.
Export and Import
: Transfer playbooks and playbook blocks between
        staging and production servers. Playbooks are exported or imported with
        their customized views included. The system accepts only ZIP files for import.
Move to
: Move playbooks and blocks to a different folder, or create a new folder.
Delete
: Delete playbooks and blocks. After you click
Delete
, you can delete playbooks.
Search
: You can use the Search bar to find the playbook you are looking for.
Top section of Playbook Designer
The top section of the Playbook Designer provides a comprehensive overview and essential controls for your playbook. 
You'll find the following features:
Horizontal toggle to enable or disable the playbook, offering quick activation or deactivation.
Concise summary, detailing the playbook's name, creator, creation timestamp, and associated environment, along with a brief description.
Activate the simulator for testing and to add a customized view for enhanced visibility.
Using the Playbook Designer's features, you can do the following actions:
Icon
Description
Open Step Selection
Opens a side drawer with available
Triggers
,
Actions
,
Flow
, and
Blocks
.
Fits to screen
Automatically adjusts the playbook to fit entirely on the screen.
Rearrange
Reverts the playbook to its default arrangement.
Zoom
Zooms in to one or multiple steps in the playbook.
Download
Downloads the playbook as a PNG file.
Undo
Reverts any changes that you've made.
Redo
Revises any changes that you have previously undone.
Playbook monitoring
Displays the individual playbook statistics.
Playbook navigator
Displays all playbook actions and flows.
For more information about the
Playbooks
page and how to collaborate with it, see the following:
Define custom alert views from Playbook Designer
Work with the Playbook Simulator
Understand playbook
monitoring
Use the Playbook Navigator
Playbook icons legend
The following icons appear on the
Cases
>
Playbooks
tab when a playbook is attached.
Need more help?
Get answers from Community members and Google SecOps professionals.
