# Manage users

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-do-i-add-a-new-user-to-the-platform/  
**Scraped:** 2026-03-05T09:37:19.680001Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage users
Supported in:
SOAR
This document is intended for users of the Google Security Operations SOAR platform who want to add new users.
User types
The  Google Security Operations SOAR user types include:
Standard users
: can be given various permissions and have edit rights to the platform as you defined them.
View-only users
: can only view certain parts of the platform based on their assigned permissions. They require a special license. For details, see
Create a view-only user
.
Collaborator users
: can have edit or view permissions for specific platform modules. For more information on this user type, see
Benefits of adding a collaborator user
.
Managed users:
Have full case management permissions, letting them participate in a hybrid SOC model alongside a Managed Security Service Provider (MSSP).
For more information on managed users, see
Create a Managed or Managed-plus user
.
Managed-plus users
: Have the same case management permissions as managed users, with the additional ability to build and edit playbooks within their own environment. For more information on Managed-plus users, see
Create a Managed or Managed-plus user
.
Add a new user
To add a new user to the Google Security Operations SOAR platform, follow these steps:
Go to
Settings
>
Organization
>
User Management
.
Click
add
Add
.
Fill out the required information in the fields. You can edit this information after the user is created.
 The
Login ID
field must contain an email address for internal users. 
  If you edit the
Login ID
field, the user's status changes to
Pending
until the next sign-in.
Click
Add
. The new user appears in the user list, and an email invitation is automatically sent.
Set environment access
If you select a permission group with edit permissions for
All Environments
, the user is granted access to all environments by default. To change this at the permission group level, 
      follow these steps:
On the
Permissions
page, select
None
for
All Environments
.
Select one or more specific environments for the user to have access to.
Click
Add
. The new user appears in the list of users, 
  and an email invitation is automatically sent.
For internal users, the status remains
Pending
until they accept 
  the invitation and create a password.
The invitation link is valid for 3 days. The administrator can resend the invitation on the
User Management
page.
For SAML users, the status remains
Pending
until the initial login. 
  They can sign in directly to the platform without the need to use the invitation 
  email.
You can also
map users with multiple control access parameters
.
Need more help?
Get answers from Community members and Google SecOps professionals.
