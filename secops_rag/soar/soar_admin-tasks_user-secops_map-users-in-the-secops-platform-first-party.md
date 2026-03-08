# Map users in the platform
using Cloud Identity

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party/  
**Scraped:** 2026-03-05T09:45:58.195697Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Map users in the platform
using Cloud Identity
Supported in:
Google secops
This document explains how to authenticate and map users with secure identification 
to Google Security Operations.
Control user access
There are multiple ways to manage user access to different aspects of the platform:
Permissions groups
: Set user access levels by assigning them to 
specific permission groups. These groups determine which modules and submodules 
users can view or edit. For example, a user might have access to
Cases
and
Workdesk
pages, but be restricted from
Playbooks
and
Settings
. 
For more information, see
Work with permission groups
.
SOC roles
: Define the role of a group of users. You can assign users 
to SOC roles to streamline task management. Instead of assigning cases, actions,
 or playbooks to individuals, they can be assigned to a SOC role. Users can see 
 cases assigned to them, their role, or additional roles.
For more information, see
Work with roles
.
Environments or environment groups
: Configure environments or environment 
groups to segment data across different networks or business units, commonly used 
by businesses and Managed Security Service Providers (MSSPs). Users can only access 
data within the environments or groups assigned to them. For more information, see
Work with environments
.
Map email user groups
The combination of permission groups, SOC roles, and environments determines the 
Google SecOps user journey for each group in the platform.
There are various options for mapping. You can map users with either single or 
multiple permission groups, SOC roles, and environments. This process makes sure that different 
users mapped to different groups inherit all the necessary permission levels.
By default, Google SecOps includes a group of default administrators.
To map email groups, follow these steps:
Go to
Settings
>
SOAR Settings
>
Advanced
>
Group Mapping.
Make sure you have the following available:
Group Names
: The name you assign to an email group, such as
T1 analysts
.
Group Members
: The collection of user emails that make up that group.
Click
Add
Add
and map the emails for each group. Press
Add
after 
you add each email.
Once you've finished, click
Add
. Each time a user signs in to the platform, 
they're automatically added to the
User Management
page, found under
Settings
>
Organization
.
When users attempt to sign in to the Google SecOps platform, but 
their email group hasn't been mapped, to prevent these users from being rejected,
we recommend enabling the
Default Access Settings
and 
setting administrator permissions on this page. After the initial administrator 
setup is complete, we suggest you adjust the administrator permissions to a more 
minimal level of permissions.
For information about multiple permission in group mapping, 
see
Map users with multiple control access parameters
.
Map groups to access control parameters
This section describes how to map different email groups to one or more access
control parameters within the
Group Mapping
page. This approach is
beneficial for customers who want to onboard and provision user groups based on
specific customizations, rather than adhering to the standardization of the Google SecOps 
platform. While mapping groups to parameters may require you to create more groups
initially, once the mapping is set, new users can join Google SecOps
without the need to create additional groups.
Delete a user
If you delete groups from here, make sure to delete the individual users from the
User Management
screen. For more information, see
Disable or delete a user account
.
Use case: Assign unique permission fields to each email group
The following use case illustrates how to use this feature to help onboard and provision 
users according to your company's needs.
Your company has three different personas:
Security analysts (containing group members Sasha and Tal)
SOC engineers (containing group members Quinn and Noam)
NOC engineers (containing group members Kim and Kai)
Security analysts and SOC engineers have the same Google SecOps 
permission groups (analyst) and SOC roles (Tier 1). While the security analysts have 
permissions for the London environment, the SOC engineers have permissions 
for the Manchester environment. Meanwhile, NOC engineers have permissions for the
London
environment, but are assigned the
Basic
Permission Group and
Tier 2
SOC role.
This scenario is illustrated in the following table:
Group
Permission Group
SOC Role
Environment
Group Members
Security analysts
Analyst
Tier 1
London
sasha@company.com, tal@company.com
SOC engineers
Analyst
Tier 1
Manchester
quinn@company.com, noam@company.com
NOC engineers
Basic
Tier 2
London
kim@company.com, kai@company.com
Set up email groups
To set up email groups in Google SecOps, do the following:
Create the following email groups:
Security analysts (containing Sasha and Tal)
SOC engineers (containing Quinn and Noam)
NOC engineers (containing Kim and Kai)
Go to
Settings
>
SOAR
Settings
>
Advanced
>
Group Mapping
.
Click
Add Group
.
Enter the following details in the dialog:
Group:
Security analysts
Permission Group:
Analyst
SOC Role:
Tier 1
Environment:
leave blank
Group Members:
sasha@company.com, tal@company.com
Enter the following details in the next dialog:
Group:
SOC engineers
Permission Group:
Analyst
SOC Role:
Tier 1
Environment:
leave blank
Group Members:
quinn@company.com, noam@company.com
Enter the following details in the next dialog:
Group:
NOC engineers
Permission Group:
Basic
SOC Role:
Tier 2
Environment:
Leave blank
Group Members:
kim@company.com
,
kai@company.com
Enter the following details in the next dialog:
Group:
London
Permission Group:
leave blank
SOC Role:
leave blank
Group Members:
leave blank
Environment:
London
Enter the following details in the next dialog:
Group:
Manchester
Permission Group:
leave blank
SOC Role:
leave blank
Group Members:
leave blank
Environment:
Manchester
For customers who use the Case Federation feature, see
Set up federated case access for Google SecOps
.
Need more help?
Get answers from Community members and Google SecOps professionals.
