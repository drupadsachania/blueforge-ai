# Manage rules using the Rules Editor

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules/  
**Scraped:** 2026-03-05T10:03:49.005510Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage rules using the Rules Editor
Supported in:
Google secops
SIEM
The Rules editor in Google Security Operations is the primary interface to create, view, test, and manage your YARA-L detection rules. It provides a dedicated environment for security engineers to author and refine detection logic that identifies threats and suspicious activity in ingested log data.
Create and edit rules
To open the
Rules editor
, click
Detections
>
Rules &
detections
>
the
Rules editor
tab.
Create a new rule
Rules use the YARA-L 2.0 query language. Before creating a new rule for the
first time, see
Get Started: YARA-L 2.0 in SecOps
.
To create a new rule, follow these steps:
In the
Rules editor
, click
New
to open the
Rules editor
window.
The system automatically populates the default rule template and generates a
unique name for the rule. Create your new rule in YARA-L.
In the
Bind to scope
menu, select the scope to add it to the rule. For
more information about adding a scope to a rule, see
data RBAC impact on Rules
.
Click
Save new rule
.
Google SecOps checks the syntax of your rule. If the rule is
valid, it saves and enables the rule automatically. If the rule is invalid,
it returns an error.
The run frequency for multi-event rules is automatically set based on the
rule's match window:
For a window size of 1 to 48 hours, the run frequency is set to 1 hour.
For a window size greater than 48 hours, the run frequency is set to 24
hours.
For more information, see
Set the run frequency
.
(Optional) To delete the new rule, click
Discard
.
Edit a rule
To edit an existing rule, follow these steps:
Use the
Search rules
field to find an existing rule, or scroll through the rules list. Click a rule in the side panel to view the details in the rule display panel.
Select the rule to edit from the
Rules list
.
The rule displays in the
Rule editing
window. The rule menu offers the following options for each rule:
Live rule
: Enable or disable the rule.
Duplicate rule
: Make a copy of the rule.
View rule detections
: Open the
Rule Detections
window to display 
detections captured by this rule.
To update the rule's scope, select the scope from the
Bind to scope
menu. For more information about adding a scope to a rule, 
see
data RBAC impact on Rules
.
View current detections
View information about current detections associated with a rule in one of these ways:
Click the rule in the rules list.
Click
View rule detections
to open
Rule detections
view. This view displays the rule's metadata and
a graph showing the number of detections found by the rule over recent days.
Click
Edit rule
to open the
Rules editor
.
The
Timeline
tab lists events detected by the rule. 
Select an event and open the associated raw log or UDM event.
To change the information shown on the
Timeline
tab, click
view_column
Columns
to open the
multicolumn view options. The multicolumn view lets you choose from various
categories of log information, including common types, such as
hostname
and
user
, and more specific categories provided by UDM.
Test your rule
Click
Run test
to test your rule. Google SecOps runs the 
rule on events in the specified time range, generates results, and 
displays them in the
Test rule results
window.
Click
Cancel test
at any time to stop the process.
For more information, see
View rule errors
.
For community blogs on managing rules, see:
Rules editor navigation
Need more help?
Get answers from Community members and Google SecOps professionals.
