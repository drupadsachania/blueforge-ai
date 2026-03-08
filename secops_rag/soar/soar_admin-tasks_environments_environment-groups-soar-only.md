# Create environment groups

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/environment-groups-soar-only/  
**Scraped:** 2026-03-05T10:10:48.641365Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create environment groups
Supported in:
Google secops
SOAR
This document explains how to create and manage environment groups in
Google Security Operations. Environment groups let you organize multiple environments
into logical categories, making it easier to manage large organizations or multiple
customers as a Managed Security Service Provider (MSSP).
Environment group use cases
MSSPs, government entities, and enterprises with multiple sub-organizations can all benefit from using environment groups. Common use cases include:
MSSP service-level tiers
: Differentiating services based on customer tiers (for example, Gold, Silver).
Government sectors
: Customize security solutions for specific industries (for example, communication, transportation).
Enterprise sub-organizations
: Manage security for individual sub-organizations within a larger entity (for example, Sub Org 1, Sub Org 2).
Understand supported modules for environment groups
The following modules support environment groups:
Settings
: Speeds up onboarding of new users and simplifies adding new environments to existing groups.
Playbooks or blocks
: Streamlines playbook creation. You can adjust the scope of your playbooks by grouping environments together. Playbooks automatically update the scope when you modify the environment groups.
Case filters
: Enables targeted issue and efficient issue resolution by filtering cases by environment group.
Limitations
The following modules don't support environment groups as a filter:
SOAR Search
: When searching for cases, you can't filter by 
  environment groups. You must manually select individual environments.
SOAR Reports
: When creating reports, environment groups aren't 
  available as a filter. You must select individual environments to define the 
  report scope.
Create an environment group
To create an environment group:
Go to
SOAR Settings
>
Organization
>
Environments
.
Click the
Groups
tab.
Click
add
Add
.
Enter the environment group name and description.
Add as many environments to the group as needed.
You can modify environment groups at any time. To do so, select
Manage Groups
and edit existing groups as needed.
Delete environment groups
When you delete an environment group, the action doesn't delete its associated environments.
However, if the deleted environment group is the only one associated with a playbook, the system also deletes the playbook.
To delete an environment group:
Go to
SOAR Settings
>
Organization
>
Environments
.
Click the
Groups
tab.
Click
Manage Groups
.
Click
delete
Delete
.
Need more help?
Get answers from Community members and Google SecOps professionals.
