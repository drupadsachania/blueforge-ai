# Archive rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/archive-a-rule/  
**Scraped:** 2026-03-05T09:31:30.255780Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Archive rules
Supported in:
Google secops
SIEM
Archiving a rule enables you to hide the security data related to that rule (and all of its versions) without actually deleting the rule. Much of the functionality available for active rules (for example, enabling a rule) is not available for archived rules.
Note the following:
Rules Dashboard does not display archived rules.
Test Rule can be used on archived rules.
Viewing rules
Complete the following steps to navigate to the
View Rules
page:
In the navigation bar, click
Detection > Rules & Detections
.
Select the
Rules Editor
tab to view the rules page.
Click the filter icon at the top-right corner of the left navigation
tab. The menu provides the following options:
Show All
,
Active Rules
, and
Archived Rules
.
Viewing rule detections
On the
Rules Editor
tab, select
View Rule Detections
from the drop-down
list available on the top-right corner. The
Rule Detections
page appears.
Archiving a rule
To archive a rule, complete the following steps:
Select a rule in the left navigation and click the option icon in the top-
right corner of the Google Security Operations user interface. Select
Archive Rule
from the
menu.
Note the following:
Archiving is allowed even if the Alerting toggle is ON, it is automatically disabled.
Archiving is NOT allowed unless the Live toggle is disabled.
Archiving is NOT allowed unless there are NO Retrohunts in progress.
The following window is displayed with a message confirmation.
Confirm Archive message
Confirm Archive message continued
Unarchiving a rule
To unarchive a rule, complete the following steps:
Click the option icon for a specific rule in the left navigation pane. A menu
appears with the following options:
View Detections
,
Duplicate
, and
Unarchive
.
Select
Unarchive
.
Select a rule in the left navigation pane and click the option icon in the
top right corner of the Google SecOps user interface. A menu appears with
the following options:
View Detections
,
Duplicate
, and
Unarchive
.
Need more help?
Get answers from Community members and Google SecOps professionals.
