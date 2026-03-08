# Manage permission groups

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups/  
**Scraped:** 2026-03-05T09:45:47.090708Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage permission groups
Supported in:
Google secops
SOAR
Google Security Operations lets you create groups of users and assign different permission levels to various modules.
The platform includes seven predefined permission groups:
Readers
Admins
Basic
View-Only
Collaborators
Managed User
Managed-Plus User
The built-in administrator group automatically has edit access to all environments,
letting its members view data from every environment in the system.
When you create a new permission group, carefully consider whether to grant edit
access to all environments.
Edit a permission group
To edit an existing permission group, follow these steps:
Go to
Settings
>
Organizations
>
Permissions
.
Select the permission group you want to edit.
Each module appears with a toggle to grant or deny a user access:
If the toggle is turned on, configure permissions for each feature you want to enable.
If the toggle is turned off, the module doesn't appear.
When finished, click
Save
.
Add a new permission group
To add a new permission group, follow these steps:
Go to
Settings
>
Organizations
>
Permissions
.
Click
Add Permission Group
.
Complete the following areas on the screen:
Your cursor is automatically placed next to the title of New
      Group. Delete the words New Group and enter your own name for the new
      Group. For example, Tier One.
From the list, select the License Type you want.
Select the Landing Page that you want this User Group to be directed to when they first sign in.
Select the permissions you want for each module.
When finished, click
Save
; the new permission group is added to the list. Note that at any time, you
  can make changes and click
Save
again. To simplify editing, click
content_copy
Duplicate
to create a copy of the permission group.
Restrict Actions
You can apply Restrict Actions to a permission group to prevent access to certain types 
of actions. For example, as a Managed Security Service Provider (MSSP), you might 
have separate SOC Manager groups for separate environments.
In
Settings
>
Organizations
>
Permissions
, select the permission group to prevent access.
In the
Restrict Actions
section, click
add
Add
, and select the actions to restrict for this permission group.
Click
Add
>
Save
.
Learn how to
control access to the platform
.
Need more help?
Get answers from Community members and Google SecOps professionals.
