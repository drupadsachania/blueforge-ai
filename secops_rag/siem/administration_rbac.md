# Role-Based Access Control (RBAC) User Guide

**Source:** https://docs.cloud.google.com/chronicle/docs/administration/rbac/  
**Scraped:** 2026-03-05T09:14:44.734607Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Role-Based Access Control (RBAC) User Guide
Supported in:
Google secops
SIEM
Role-based access control (RBAC) enables an administrator to tailor access to
Google Security Operations features based on an employee's role in your organization.
Before you begin
RBAC reads the group information from the SAML response from the following case-insensitive default attribute names:
group
idpgroup group
memberof
If you use a custom attribute name, it must be provided to your Google Security Operations first to enable you to modify your RBAC settings.
Modify RBAC settings
To navigate to the RBAC profile and settings pages, click
Settings
in the navigation bar.
Profile
The
Profile
page displays the information from the user's profile (user ID, 
group ID, roles assigned) and some additional information about their organization (customer ID, Google Cloud project number, Google Cloud project ID).
Customer ID
Your customer ID is located in the
Organization Details
section of the
Profile
page.
Update the time zone
You can update the time zone as follows:
Locate the
Time Settings
section on your profile and click
Edit
.
Select the appropriate time zone for your location.
Users & Groups
The
Users & Groups
page enables an administrator to configure RBAC.
Click the
Users & Groups
link in the left navigation pane. A list of users and groups are displayed on the
Users and groups
page with the columns:
User/Group
,
Type
, and
Assigned role
.
Click
Assign new
to open the
Assign role
dialog. From this dialog you can complete the following tasks:
Assign a new user or users to a role.
Assign a new group or groups to a role.
The available roles are:
Default
ViewerWithNoDetectAccess
Viewer
Editor
Administrator
Once you have added your user or group IDs and selected the appropriate role from the
ASSIGN ROLE
drop-down menu, click
ASSIGN
.
As you assign roles, be aware of the following:
When adding users or groups, make sure they exist in your identity provider (IdP). When deleting users or groups, make sure you retain at least one user or group that has the Administrator role and is in your IdP; otherwise, you'll lose administrator access.
User and group IdP IDs are case sensitive.
You can't change the assigned role of an existing user or group using this dialog. See the steps that follow for how to change roles and delete users and groups.
Google Security Operations manages the mapping between users and groups and roles.
Use caution if the user or group ID contains special characters that, depending on the text source, might use UTF-8 encoding. Once you click
Assign
, Google recommends that you verify that the new assignment has been saved correctly.
You can change the role of an existing user or group by selecting a new role from the drop-down menu corresponding to that user or group in the
Assigned role
column.
You can change the default role assigned to new users and groups from the role drop-down menu in the top right corner.
You can delete a user or a group by clicking on the trash-can icon which appears on the far right side of the user or group row as you hold the pointer over it.
If you delete users and groups that are administrators, and the only remaining administrators are not in your IDP, you will lose administrator access.
Roles
Roles are associated with a set of product permissions. Assigning a role to a user grants the user the permissions associated with that role.
Google Security Operations includes the following predefined roles:
Administrator—Manages the role-based access control policies for your enterprise. Can also edit or view any Google Security Operations page.
Editor—Can edit Google Security Operations pages, including the ability to create and edit rules for the Detection Engine.
Viewer—Can view any Google Security Operations page, but cannot make any changes.
ViewerWithNoDetectAccess—Can view all Google Security Operations pages that don't include detections (principally the Rules and Reference Lists pages).
RBAC applications include the following:
Create and assign roles based on the job responsibilities.
Create and assign roles based on tenancies or organizations.
Assign temporary roles to analysts for investigating an issue.
Permissions
Permissions provide the authorization needed to perform a single controlled action in Google Security Operations, including (see the user interface for the complete list of permissions):
View rule
Modify rule
Edit feedback
Edit reference list
View RBAC permissions
If a user does not have permissions for an action, the associated feature is disabled. For example, if the user has the Viewer role, they are unable to create a new rule (the
New
button is disabled in the Rules Editor), duplicate a rule (the
Duplicate
option is disabled), or modify an existing rule.
To view the roles and permissions available to users and groups, complete the following:
Click the
Roles
link in the left navigation pane.
Select a role from the Roles column to view the permissions granted for that role. The permissions associated with each role cannot be changed.
The default role for newly added users and groups is Viewer. If you select one of the other roles (for example, Editor), the
Set as default
control becomes available. This lets you to make that role the default instead.
Need more help?
Get answers from Community members and Google SecOps professionals.
