# Work with playbook blocks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-blocks/  
**Scraped:** 2026-03-05T10:08:07.285225Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Work with playbook blocks
Supported in:
Google secops
SOAR
Blocks
are essentially reusable mini-playbooks that let you implement common workflows and logical decisions across multiple playbooks. This reusability makes maintenance and improvements efficient because any edit or change to a block automatically affects all playbooks that incorporate it.
You can configure input parameter fields in blocks to adjust their internal
  flow of actions when you use them in other playbooks. Blocks can also return
  output values to the parent playbook, which supports dynamic interaction and
  conditional logic within your larger workflows.
Before you begin
Before you create playbook blocks, we recommend that you take time to map out
  specific processes you anticipate reusing in parent playbooks. Also, consider
  the input fields you'll need to configure to make those blocks flexible and
  adaptable.
Add a new block
This example creates a block that manages communication between the SOC and its clients.
To add a new block, do the following:
On the
Playbooks
page, click
add
Add
, choose the folder and environment, and then click
Create
.
We recommend that administrator users click
All Environments
.
Enter the name of the new playbook block.
Add input:
Select
Input
.
Click
add
Add
and enter the input name and value fields. You can add as many fields as you need.
You'll use the following inputs to condition the flow of this block:
Communication Type
:
Require Approval
(This is one of two defined types; the other is
Investigate
).
Communication Method
:
Email
.
Additional Message
: Leave blank.
If you add values to these fields, they'll serve as default settings. While these defaults are established when you configure the block, you can modify them for each individual block instance once it's inserted into a parent playbook. This method supports adaptable and dynamic workflows.
Configure the flow step for input type
Add a flow step to your block. This step creates different branches, letting the playbook follow a specific path based on the
Input Type
you enter. You'll use placeholders to pick up the
Investigate
and
Requires Approval
input types.
Branch 1: Require Approval (default)
This branch handles the
Require Approval
input type and is your default branch.
Configure the
Require Approval
l condition to start this branch.
In the
Actions
column, select
Email
>
Send Email
, and enter the required parameters to send an email. This email typically requests user approval for a security analyst to remediate their machine.
Select
Flow
>
Condition
and enter the required parameters to confirm whether the customer has approved the request.
Output (Approved Path): In the output step for the
approved
path of this condition, add
Approved
. This value will be returned to the parent block.
Output (Else Branch - Not Approved): In the output step of the Else branch (where the customer responded negatively to the approval request), add
Not Approved
in the
Output
box.
Branch 2: Investigate
This branch defines the actions for the
Investigate
input type.
In the
Actions
column, select
Email
>
Send Email
and fill in the required parameters. A placeholder is added for the additional message. If you change the
Type
to
Investigate
in the parent playbook, enter a message in the
Input Additional Message
field.
Select
Siemplify
>
Assign Case
to assign the case to the
    customer. This action directs their Tier 1 analyst to review the incident, shifting the initial investigation responsibility to them.
Select
Siemplify
>
Change Case Stage
. This step assumes
    confirmation that the customer is actively investigating, so the case stage is
    changed to
Investigation
.
Select
Siemplify
>
Assign case
. This
    step assumes that the customer has completed their investigation and has requested the
    SOC to reclaim ownership of the case.
Select
Siemplify
>
Change Case Stage
.
    This step now changes the case stage from
Investigation
to
Assessment
, letting the SOC resume handling the case.
In the Output step, add the words
Investigation Completed
to return to the parent playbook.
This block is now configured with conditional logic and you can insert it into various parent playbooks, adapting its behavior based on the
Communication Type
input.
Insert an existing block
To insert an existing block, do the following:
On the
Playbooks
page, click
Add Step
.
In the
Step Selection
box, select the
Blocks
section.
Drag the required block into the center of the playbook.
Need more help?
Get answers from Community members and Google SecOps professionals.
