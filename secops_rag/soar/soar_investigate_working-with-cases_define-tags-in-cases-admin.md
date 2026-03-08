# Manage tags in cases and alerts

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-tags-in-cases-admin/  
**Scraped:** 2026-03-05T10:07:09.427703Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage tags in cases and alerts
Supported in:
Google secops
SOAR
This document explains how to manage tags in Google Security Operations cases.
Tags help classify and organize cases for easier filtering and analysis. They
  can be assigned automatically based on predefined rules or added manually from
  the case and alert views.
While you can remove tags from individual cases, the tags themselves remain
  available in the system's autocomplete list unless an administrator removes 
  them from the table in the
Case Data
>
Tags
settings.
You may also want to import tags—for example, when migrating from a staging
to a production environment or for backup purposes. For more information, see
Import tags
.
Manage tags in cases and alerts
Tags help you track and categorize your cases. You can quickly identify 
    cases by searching for them by their tags.
You can manage tags from the following places:
Case or Alert
: Manually add and remove tags from a specific case or 
    an individual alert.
Main menu
: Click
Settings
>
Case Data
>
Tags
. 
    For more information, see
Create an automatic 
    tagging rule
.
Playbooks
: Trigger a playbook on a tag name using the tag trigger. 
    You can also add a case tag to a playbook block: select a playbook block, 
    click
Open Step Selection
, and in the
Triggers
tab, select
Tag Name
.
Add a tag to a case
To add a tag to a case, follow these steps:
Go to the
Cases
page and select a case you want to tag.
Click
sell
Manage Tags
.
In the
Manage Tags
dialog, enter the name of the tag and press
Enter
, or select a tag from the list and click
Add
.
Add a tag to an alert
To add a tag to an alert, follow these steps:
Go to the
Cases
page and select a case.
Select the alert you want to tag.
Click
more_vert
Alert Options
and then select
Manage tags
.
In the
Manage Tags
dialog, enter the name of the tag and press
Enter
, or select a tag from the list and click
Add
.
Alert tag behavior during case changes
Manually assigned alert-level tags remain attached to the specific alert 
during case management actions:
Moving alerts
: If you move an alert to a different case, any tags 
  manually assigned to that alert move with it.
Merging cases
: When cases are merged, individual alerts within the 
  consolidated case retain their manually assigned alert-level tags.
Configure tag settings
Import tags
To import a tag, follow these steps:
Go to
SOAR Settings
>
Case Data
>
Tags
.
Click
vertical_align_bottom
Download template
. The CSV file shows the required tag import structure.
Enter the tag information.
Click
login
Import
. The imported tags should appear in the platform.
Remove a tag from autocomplete
To prevent a tag from appearing in autocomplete suggestions, you must remove 
it from the Tag table in the Case Data settings.
Go to
SOAR Settings
>
Case Data
>
Tags
.
Locate the tag in the table and click
delete
Delete
.
Create an automatic tagging rule
To create a rule that automatically assigns tags to incoming alerts based on 
specific conditions, follow these steps:
Go to
SOAR Settings
>
Case Data
>
Tags
.
Click
add
Add Tag
.
In the
Tag name
field, enter a name for the tag.
Select a match source from
Entities
,
Product
,
Rule Generator
and
Vendor
.
From the menu, choose a qualifier that defines how to match the value:
contains
exact
starts with
ends with
Select the specific entity or product source. Enter the appropriate
Property
and
Value
, if applicable.  Alternatively, select the
Product
,
Rule Generator
, or
Vendor
.
Select the priority for the tag.
Note: Google SecOps merges priority with other alerts and entities and events so that the priority here is not an absolute.
Optional: Select
Can be a case name
if required. When selected, 
    the tag is assigned as the title of the case if it meets the conditions.
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
