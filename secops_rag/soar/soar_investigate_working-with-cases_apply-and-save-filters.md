# Apply and save filters

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters/  
**Scraped:** 2026-03-05T10:07:30.757448Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Apply and save filters
Supported in:
Google secops
SOAR
This document explains how filters can help narrow your search in the case
  queue to target only the cases you want to review. Case queue filters help
  streamline your workflow by surfacing only the cases you need to act on. 
  Whether you're triaging high-priority alerts, reviewing cases in a specific
  environment, or collaborating with a SOC team, filters offer flexible control
  using `AND`, `OR`, `IS`, and `IS_NOT` conditions.
The following filters are available: Timeframe, Alert names, Analysts,
Environments, Priorities, Products, Stages, Tags, and Playbook Status.
Add a filter
Define custom filters to customize your case queue view.
To add a new filter, follow these steps:
Click
Cases Filter
.
In the
Case Queue Filter
dialog, fill in the required filter conditions. For 
    example, to display high-priority cases that are
not
in the 
    investigation stage in the past 24 hours:
Set the
Time Frame
to
Last 24 hours
.
Set the first condition to
Priorities
IS
High
.
Set the second condition
Stages
IS_NOT
Investigation
.
Optional: To save the filter for future use, click
Save Filter
and enter a name. The filter is saved under
keyboard_arrow_down
Saved Filters
in the case queue header for future use.
Click
Apply
.
Share case queue filters
You can share your case queue filters with other individual users, 
    specific SOC roles (like Tier 1 analysts), or all users.
Filters shared with you or by you display a
Shared
icon next 
  to their name.
To share a filter, your permission group must have the
Allow sharing case queue filters
permission enabled. This permission is enabled by default for the
Admin
group. For more information about enabling permissions, see
Edit a permission group
.
To share your case queue filters, follow these steps:
Add a new filter by following the steps in
Add a filter
.
Click
Save Filter
.
In the
Save filter
dialog, enter a name for the filter and then 
    choose one of the three sharing options:
Private (only me):
This is the default setting. The 
            filter remains private and visible only to you.
Public (all users):
The filter is visible to all 
            users who have access to cases.
Specify users & roles:
Select this option to search for 
            and add specific users or predefined SOC roles.
Click
Save
.
Manage your saved filters
You can edit, rename, change sharing settings, or delete filters you've created. Changes to shared filters apply to everyone they're shared with.
Edit a filter
To edit a filter you created, follow these steps:
In the case queue header, click
keyboard_arrow_down
Saved Filters
.
Hold your pointer over the filter you want to manage and click
edit
Edit
.
If the filter is shared, a confirmation dialog appears. Click
Yes
to continue to the
Edit filter
dialog.
Modify the filter criteria or change its sharing configuration.
Click
Save
.
Temporarily modify a shared filter
To temporarily modify a shared filter, follow these steps:
In the case queue header, click
keyboard_arrow_down
Saved Filters
.
Click the shared filter you want to modify.
In the case queue header, click
filter_alt
Cases Filter
to modify the filter, and apply changes.
Delete a filter
You can delete any filter you created. If the filter is shared, 
it will also be removed from other users' filter lists.
To delete a filter, follow these steps:
Hold your pointer over the filter you want to delete and click
delete
Delete
.
In the confirmation dialog, click
Yes
to delete the filter.
Need more help?
Get answers from Community members and Google SecOps professionals.
