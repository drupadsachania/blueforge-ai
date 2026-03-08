# Map users with multiple control access parameters

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters/  
**Scraped:** 2026-03-05T09:46:00.975749Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Map users with multiple control access parameters
Supported in:
Google secops
SOAR
This document describes the algorithms that the Google Security Operations platform 
uses to apply multiple control access parameters for user groups.
Assign permission groups
You can assign a maximum of five permission groups for each user or user group.
The users get a combination of all the permissions from 
each of the permission groups.
Assigned landing page for permissions groups
Each permission group has a designated landing page that users are directed to 
when they first sign in to the Google SecOps platform. If a user 
(or user group) is assigned to multiple permission groups, Google SecOps 
selects the landing page based on the highest-ranking option in the following 
hierarchy:
Cases
>
Case Overview
Homepage (Workdesk)
>
My Cases
Cases
>
Case Wall
Homepage (Workdesk)
>
Pending Actions
Dashboards
Playbooks
Reports
Search
Homepage (Workdesk)
>
Requests
Command Center (Incident Manager)
Legacy SIEM Search
Restrict actions
Each permission group includes a section where the administrator can select 
actions that are restricted for that specific permission group. For a restricted 
action to apply, it must be selected in all permission groups assigned to the 
user group. That is, if a user group is mapped to multiple permission groups,
but the restricted action is only assigned in one of those groups, the 
restriction isn't enforced.
Map SOC roles
You can map each user with up to five SOC 
roles plus additional roles.
Create playbook views per SOC roles
Each playbook customized view is assigned to a specific SOC role. If a user 
is assigned to several SOC roles, then all widgets are displayed. 
Exception: If one SOC role includes another, the system displays the parent SOC role's playbook view
Assign environments
You can assign both environments and environment groups at the same time. You 
can assign each user to multiple environments and environment groups, granting 
them access to all cases and data within each assigned environment or environment 
group.
Need more help?
Get answers from Community members and Google SecOps professionals.
