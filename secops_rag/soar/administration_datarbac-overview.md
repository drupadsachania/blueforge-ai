# Data RBAC overview

**Source:** https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview/  
**Scraped:** 2026-03-05T09:45:35.944953Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Data RBAC overview
Supported in:
Google secops
SIEM
Data role-based access control
(
data RBAC
) is a security model that uses
individual user roles to restrict user access to data within an organization.
With data RBAC, administrators can define scopes and assign them
to users to help ensure that users can access only the necessary data for their job
functions.
This page provides an overview of data RBAC, and helps you understand how labels
and scopes work together to define data access permissions.
Difference between data RBAC and feature RBAC
Data RBAC and feature RBAC are both methods for controlling access within a
system, but they focus on different aspects.
Feature RBAC controls access to specific features or functionalities within a
system. It determines which features are accessible to users based on their
roles. For example, a junior analyst might have access to only view dashboards
but not to create or modify detection rules, while a senior analyst might have
the permissions to create and manage detection rules. For more information about
feature RBAC, see
Configure feature access control using IAM
.
Data RBAC controls access to specific data or information within a system. It
controls whether a user can view, edit, or delete data based on their roles. For
example, in a customer relationship management (CRM) system, a sales
representative might have access to customer contact data but not
finance data, while a finance manager might have access to the finance data
but not the customer contact data.
Data RBAC and feature RBAC are often used together to provide a comprehensive
access control system. For example, a user might be allowed to access a specific
feature (feature RBAC) and then, within that feature, their access to specific
data might be restricted based on their role (data RBAC).
Plan your implementation
To plan your implementation, review the list of Google Security Operations
predefined Google SecOps roles and permissions
and align them with your organization's needs. Devise a strategy to define scopes
and label incoming data. Ensure that you have the
Role Viewer (
roles/iam.roleViewer
) role to manage scopes.
Identify which members must have access to data within these scopes.
If your organization requires IAM policies beyond the
predefined Google SecOps roles, create
custom roles
to support specific requirements.
User roles
Users can have either scoped data access (scoped users) or global data access
(global users).
Scoped users have limited access to data based on the scopes assigned. These
scopes restrict their visibility and actions to specific data. The specific
permissions associated with scoped access are detailed in the following table.
Global users have no assigned scopes and have unrestricted access to all data
within Google SecOps. The specific permissions associated with global
access are detailed in the following table.
Global access overrides scoped access. If a user is assigned both a global role
and a scoped role, they have access to all data, regardless of any restrictions
imposed by the scoped role.
Data RBAC administrators can create scopes and assign them to users to control
their data access within Google SecOps. To restrict a user to certain
scopes, you
must
assign them the Chronicle API Restricted Data Access
(
roles/chronicle.restrictedDataAccess
) role along with
a predefined or a custom role. The Chronicle API Restricted Data Access role
identifies a user as a scoped user. You don't need to assign the Chronicle
Restricted Data Access role to users who need global data access.
The following roles can be assigned to users:
Access type
Roles
Permissions
Predefined global access
Global users can be granted any of the
predefined IAM roles
.
Predefined scoped read-only access
Chronicle API Restricted Data Access (
roles/chronicle.restrictedDataAccess
) and Chronicle API Restricted Data Access Viewer (
roles/chronicle.restrictedDataAccessViewer
)
Chronicle API Restricted Data Access Viewer
Custom scoped access
Chronicle API Restricted Data Access (
roles/chronicle.restrictedDataAccess
) and
custom role
(for feature RBAC definition)
Custom permissions within features
Custom global access
chronicle.globalDataAccessScopes.permit
permission and Chronicle API Global Data Access (
roles/globalDataAccess
)
Global permissions within features
The following is a description of each access type presented in the table:
Predefined global access:
this access is typically required for users who
need access to all the data. You can assign one or more roles to
a user based on the required permissions.
Predefined scoped read-only access:
this access is for users who need read-only
access. The Chronicle API Restricted Data Access role identifies a user as a
scoped user. The Chronicle API Restricted Data Access Viewer role gives view
access to users within their features.
Custom scoped access:
the Chronicle API Restricted Data Access role
identifies a user as a scoped user. The custom role specifies the features that
the user can access. The scopes added to the Chronicle API Restricted Data Access
role specify the data that the users can access in the features.
To verify RBAC custom scopes function correctly, include the
chronicle.dataAccessScopes.list
permission when creating the custom roles. However, don't include the
chronicle.DataAccessScopes.permit
or
chronicle.globalDataAccessScopes.permit
permissions. These permissions might be included
if you've used the prebuilt Chronicle API Editor or Chronicle API Admin as a
starting point for your custom roles.
Custom global access:
this access is for users who need unrestricted
permissions within their assigned features. To give custom global access to a
user, you must specify the
chronicle.globalDataAccessScopes.permit
permission
in addition to the custom role that is assigned to the user.
User roles for Dashboards
Access to dashboards is controlled by two main factors: a user's
functional role
and their
data access scope
. The combination of these two elements determines dashboard
access.
A user's assigned role directly changes their available user interface and capabilities.
Following are the most common predefined roles that give users access to dashboards:
Access type
Roles
Description
Viewer
roles/chroniclesiem.viewer
Grants read-only access. Users can open and
   interact with all dashboards but can't create or edit them.
Editor
roles/chroniclesiem.editor
Grants access to all data and all permissions, including the ability to
   create, edit, and delete custom dashboards.
Administrator
roles/chroniclesiem.admin
Grants full permissions, similar to the Editor role, with access to all data.
Restricted viewer
roles/chroniclesiem.restrictedViewer
Similar to the Viewer role, but all data displayed in the dashboard is filtered according to the user's assigned log scope (Data RBAC).
For more information about data RBAC and feature RBAC, see
Difference between data RBAC and feature RBAC
.
Permissions for custom roles
You can define granular permissions by creating custom roles.
The following permissions apply to Dashboards:
chronicle.dashboards.list
: Lets users see the list of available dashboards.
chronicle.dashboards.get
: Lets users open and view a dashboard content.
chronicle.dashboards.create
: Lets users create new dashboards.
chronicle.dashboards.update
: Lets users edit and save changes to existing dashboards.
chronicle.dashboards.delete
: Lets users delete custom dashboards.
For example, you can create a Dashboard Creator custom role with only
chronicle.dashboards.create
and
chronicle.dashboards.list permissions
.
A user with this role can create a new dashboard but can't edit an existing dashboard.
Access control with scopes and labels
Google SecOps lets you control data access to users by using scopes.
Scopes are defined with the help of
labels
that define the data that a user
within the scope has access to. During ingestion, metadata is assigned to data
in the form of labels such as namespace (optional), ingestion metadata (optional),
and log type (required). These are default labels that are applied to data
during ingestion. Additionally, you can
create custom labels
.
You can use both default and custom labels to define your scopes and the data
access level that the scopes will define.
Data visibility with allow and deny labels
Each scope contains one or more
allow access
labels and optionally,
deny access
labels. Allow access labels grant users access to the data that is
associated with the label. Deny access labels deny users access to the data that
is associated with the label. Deny access labels override the allow access
labels in restricting the user access.
In a scope definition, allow access labels of the same type (for example,
log type) are combined using the OR operator, while labels of different types
(for example, log type and a custom label) are combined using the AND operator.
Deny access labels are combined using the OR operator. When multiple deny access
labels are applied within a scope, access is denied if they match ANY of those
labels.
For example, consider a Cloud Logging system that categorizes logs using the
following label types:
Log type:
Access, System, Firewall
Namespace:
App1, App2, Database
Severity:
Critical, Warning
Consider a scope called Restricted logs that has the following access:
Label type
Allowed values
Denied values
Log type
Access, Firewall
System
Namespace
App1
App2, Database
Severity
Warning
Critical
The scope definition looks like this:
Allow:
(Log type: "Access" OR "Firewall") AND (Namespace: "App1") AND (Severity: "Warning")
Deny:
Log type: "System" OR Namespace: App2 OR Namespace: Database OR Severity: "Critical"
Examples of logs matching the scope:
Access log from App1 with Severity: Warning
Firewall log from App1 with Severity: Warning
Examples of logs not matching the scope:
System log from App1 with Severity: Warning
Access log from Database with Severity: Warning
Firewall log from App2 with Severity: Critical
Data visibility in enriched events
Enriched events are security events that have been enhanced with additional
context and information beyond what the raw log data contains. Enriched events
are accessible within a scope only if its base event is accessible within the scope
and any of the enriched labels don't include any of the scope's deny labels.
For example, consider a raw log that indicates a failed login attempt from an IP
address and has an enriched label
user_risk: high
(indicates a high-risk user).
A user with a scope that has the deny label
user_risk: high
can't see failed
login attempts by high-risk users.
Impact of data RBAC on Google Security Operations features
After data RBAC is configured, users start seeing filtered data in
Google Security Operations features. The impact depends on how the feature is integrated
with the underlying data. To understand how data RBAC impacts each feature, see
Impact of data RBAC Google Security Operations features
.
What's next
Impact of data RBAC on features
Configure data RBAC for users
Need more help?
Get answers from Community members and Google SecOps professionals.
