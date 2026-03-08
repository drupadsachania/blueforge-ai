# Use flows in playbooks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks/  
**Scraped:** 2026-03-05T09:34:50.823239Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use flows in playbooks
Supported in:
Google secops
SOAR
This document explains how the
Flow
component directs the next steps of a
playbook by using a branching system to make decisions.
Condition flows are essential for allowing a playbook to make
decisions—routing a case down different paths based on incoming alert data,
previous action results, or user input.
The following flow options are available:
Condition
: Complex conditions based on placeholders, existing case data,
and the
Previous Actions
flow.
Multi-Choice Question
: Questions that analysts must answer manually.
Add Condition flows
This section describes how to use Condition flows to create dynamic, branching
logic within your playbooks.
Add a single Condition flow
To add a single Condition flow, follow these steps:
On the
Response
>
Playbooks
page, click
Open Step
Selection
.
In
Step Selection
, select the
Flow
section.
Drag the condition to the step or between two actions, depending on how
you're building your playbook.
Double-click the condition to open the dialog.
Select the required entities. If you are using placeholders, they are scoped to this group of entities.
Decide how many branches you want to create. Each branch has an
OR
between them.
Select and add parameters for each branch, as follows:
Select the relevant placeholder you would like to evaluate from the list of existing placeholders. For new users, this is
empty if you've not yet ingested any alerts.
Select the required operator: (for example,
Equals to
,
Does not contain
)
Choose a value.
Define a "fallback branch" to avoid failed conditions. If a condition is
based on previous actions, and one of those actions failed (and skipped),
the condition continues to the fallback branch, instead of stopping. To
select a fallback branch, see
Define a fallback branch
.
Click
Save
. The playbook now takes three branches: 1, 2, and E (Else).
Set the outcome for (at least) one branch to mark the playbook as complete.
Add a multi-choice question flow
Drag the
Multi-Choice Questions
condition to the
Final Step
box.
Click
Multi-Choice Questions
to open the dialog.
Add a question with as many answers as needed.
Click
Save
. The playbook opens four branches.
Set the outcome for at least one branch to mark it as complete.
Add a Conditions flow
To add a Conditions flow, follow these steps:
Drag the
Conditions
to the
Final Step
box.
Click
Conditions
to open the dialog.
Decide how many branches to create. Each branch has an
OR
between them.
Add a parameter: Select the required parameter. The list shows only the
action script results from this playbook.
Select the required operator:
Equals to/Does not equal to
,
Contains/Does not contain
,
Starts with
, or
Greater than/Smaller
than
.
Choose the value (the action result).
You can add more parameters to each branch and choose a logical operator:
AND
or
OR
.
Click
Save
. The playbook opens three branches:
1
,
2
, and
Else
.
Set the outcome for at least one branch to complete the playbook.
Define a fallback branch
In one of the flows (Condition), select the
branch to use as a fallback branch. This example uses
Branch – not
risky
.
You're not required to add a fallback branch.
When the playbook runs, and the previous actions fail, the playbook chooses
the fallback branch and continues.
Manage step failures
Playbook steps can fail during execution. By default, a playbook is designed to
stop if a step fails, which is a crucial safety mechanism to prevent continuing
with incomplete or incorrect data. However, there are cases where you want a
playbook to continue even if a step doesn't return the expected results. This is
especially true for enrichment actions where the data you're looking for might
not exist in every case. You can decide whether to stop the playbook or skip to
the next step. If the failed step was crucial for decision-making, you can then
check if the previous step failed in the next step and decide how to proceed
accordingly (for example, if a step fails, go to a fallback branch).
Skip on failure
For any action, you can configure it to skip the step if it fails. When you
enable this setting, the playbook will continue to the next step, even if the
action fails to run or returns an error.
To enable this setting, follow these steps:
Double-click the action block to open its settings drawer.
In the
Settings
tab, go to the
If step fails
section.
Select
Skip step
.
Use a condition for advanced error handling
The "skip if failed" option works well for basic cases, but a more robust method
is to use a
Condition
flow to create a dedicated error-handling path. This
lets the playbook take a different set of actions when a step fails, such as
notifying an analyst or logging the error.
To create an error-handling path, follow these steps:
After an action that might fail, and for which you want to define a specific
failure path, add a
Condition
flow block.
Double-click the
Condition
block to open its dialog.
Go to the
Settings
tab, and in the
If previous action fails
section,
select which branch to direct the flow to. Important: The
If previous
action fails
condition doesn't simply check for any previous failure; it
checks if a previous action whose results are being used in the current
condition's evaluation has failed. If that dependent action failed, the
condition can't be decided, and the flow is directed to the selected branch.
This lets you handle cases where a dependency failed, preventing the
condition from being resolved.
In this failure branch, you can add actions like sending a notification
email, creating a task, or logging the failure.
For example, consider a playbook that attempts to resolve a user's owner. If the
Resolve User Owner
action fails (for example, the user doesn't exist in
Active Directory), the playbook won't stop. Instead, the condition block will
detect the failure and direct the flow to a separate branch, where it can send
an email to the security team about the missing data, ensuring the playbook
continues running without interruption. <
Remove a flow
When removing a flow from within a playbook, the system prompts you to remove
the entire branch or just one aspect of it.
Merge branches
You can merge different branches of the playbook into one branch. To do so,
drag an action from one of the branches and drop it to the
Final Step
box
of another branch. The playbook can continue after this or end here.
How logical operators work in a condition
This section clarifies how
Conditional Operators
in playbooks evaluate
fields with single or multiple items (for example, Entities or Events in an
Alert). Understanding if a field is a
string
or a
list
is crucial for
playbook logic.
The role of data types in Condition evaluation
Operator behavior (
Equals
,
Contains
) varies with data type:
Single-Item Context:
fields like
[Entity.Identifier]
from an alert
with one entity are treated as a
single string
.
Multi-Item Context:
the same field from an alert with multiple entities
is a
list of strings
.
Operator behavior of
equals
and
contains
The following sections discuss how these operators work.
Equals
operator
The
Equals
operator directly compares two values.
Single-item field (string)
checks for an exact match.
Assuming that
[Entity.Identifier]
is
"Tom"
.
Then the condition
if [Entity.Identifier] equals "Tom"
is
True
.
Multi-item field (list)
checks if the entire list equals the
specified string. A list will
never
equal a single string.
Assuming that
[Entity.Identifier]
is a list
(Tom, Kai)
Then the condition
if [Entity.Identifier] equals "Tom, Kai"
is always
False
. This is because
[Entity.Identifier]
is a list and "Tom, Kai" is a string.
Contains
operator
The
Contains
operator also changes by data type:
Single-item field (string)
performs a
substring search
. Returns
True
if the string contains the value.
Assuming that
[Entity.Identifier]
is
"user-1234"
.
Then the condition,
if [Entity.Identifier] contains "user"
is
True
.
Multi-item field (list)
checks for an
exact match
of an item in
the list.
No substring search
is performed.
Assuming that
[Entity.Identifier]
is a list
(
"UserA@corp.com", "UserB@corp.com"
).
Then the condition,
if [Entity.Identifier] contains "corp"
is
False
.
Need more help?
Get answers from Community members and Google SecOps professionals.
