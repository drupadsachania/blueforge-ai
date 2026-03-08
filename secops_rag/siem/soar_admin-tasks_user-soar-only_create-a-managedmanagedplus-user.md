# Create a Managed or Managed-Plus user

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-managedmanagedplus-user/  
**Scraped:** 2026-03-05T09:14:59.374989Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create a Managed or Managed-Plus user
Supported in:
Google secops
SOAR
The
Managed
and
Managed-plus
user types are hybrid roles—combining aspects of the Collaborator and Full User roles—designed specifically for end-customers of a Managed Security Service Provider (MSSP). These roles enable flexible, scoped access to the platform.
.
Managed user
:
useful for an MSSP who wants to run a hybrid SOC together
with their end customers.
has full case management capabilities on their own
environment (similar to the MSSP analyst).
Managed-plus user
:
Has the same permissions as a managed user, but with the added ability
    to build and edit playbooks in their own environment.
Can view playbooks running in their environment such as
All environments
playbooks, 
but won't be able to edit playbooks if they don't have permissions to all the environments that the playbook is associated with. For example, a user with permissions to the environment "North England" only will be able to view but not edit a playbook that is running on "North England", "South England" and "East England" environments. This user won't see that this playbook is running on "South England" and "East England" environments.
The MSSP is responsible for managing the Content Hub, configuring the integrations and agents and customizing actions in the Integrated Development Environment (IDE) for the Managed-plus user.
The high-level steps to add a new managed or managed-plus user are the same as that of adding other types of users:
Purchase the license for the required number of users with your Account Manager.
Select the predefined
managed user
or
managed-plus user
permission groups, or create a new one.
Create a new user.
Purchase managed user or managed-plus user license
To purchase a license for a managed user or managed-plus user, follow these steps:
Arrange a license for the required number of managed users or managed-plus users.
Go to
Settings
>
Organizations
>
License Management
to view the details.
Set up a permission group
To set up a permission group for a managed user or managed-plus user, follow these steps:
Go to
Settings
>
Organization
>
Permissions
.
In the
License Types
list, select
Managed User
or
Managed-Plus User
, or create a new one.
Select the categories that you want to be accessible. Note that the playbooks module isn't available for the managed User.
Select the type of
Landing Page
from the list.
Click
Save
.
Create a Managed or Managed-plus user (SOAR standalone customers only)
To create a managed or managed-plus user, follow these steps:
Go to
Settings
>
Organization
>
User Management.
In the
User Management
page, click
add
Add
; the
Add User
dialog appears.
In the
License Type
field, select
Managed User
or
Managed-Plus User
.
In the
Permission Group
list, select the
Managed User
or
Managed-Plus User
Group or any new group that you created.
Select the
Read/Write
permissions as required.
Click
Add
. An email invitation is sent automatically to the user.
    The invitation status remains
Pending
until they accept the invitation
    to join Google SecOps SOAR and create a password.
Need more help?
Get answers from Community members and Google SecOps professionals.
