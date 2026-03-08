# Configure feature access control using IAM

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access/  
**Scraped:** 2026-03-05T09:45:32.712857Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure feature access control using IAM
Supported in:
Google secops
SIEM
Feature RBAC controls user access to specific features or functionalities within
a system and determines which features are accessible to users based on their
roles. This page describes how you can configure feature access control within
Google Security Operations.
In this document, the term
legacy RBAC
is used when referring to the previously available access control system
that is configured using Google SecOps, and not Identity and Access Management (IAM).
Feature RBAC
is used to describe feature-based access control
that you configure using IAM.
Google SecOps integrates with Google Cloud
IAM
to provide Google SecOps-specific
permissions
and
predefined roles
. Google SecOps administrators can
control access to features by creating IAM policies that bind
users or groups to predefined roles or can create custom IAM roles.
This feature does not control access to specific UDM records or fields in a UDM record.
This document does the following:
Describes how Google SecOps integrates with IAM.
Explains how feature RBAC roles are different from the legacy RBAC roles.
Provides steps to migrate a Google SecOps instance to feature RBAC.
Provides examples of how to assign permissions using IAM.
Summarizes the permissions and predefined roles available in IAM.
For a list of commonly used Google SecOps permissions and the audit
logs they produce, see
Permissions and API methods by resource group
.
For a list of all Google SecOps permissions, see
Identity and Access Management permissions reference
.
Each Google SecOps permission is associated with a Chronicle API
resource and method. When a user or group is granted a permission, the user can
access the feature in Google SecOps and send a request using the related API method.
How Google SecOps integrates with IAM
To use IAM, Google SecOps must be bound to a Google Cloud
project and must be configured with either Cloud Identity, Google Workspace,
or Google Cloud workforce identity federation as an intermediary in the authentication
flow to a third-party identity provider. For information about the third-party authentication
flow, see
Integrate Google SecOps with a third-party identity provider
.
Google SecOps performs the following steps to verify and control access to features:
After logging on to Google SecOps, a user accesses a Google SecOps
application page. Alternatively, the user may send an API request to Google SecOps.
Google SecOps verifies the permissions granted in the IAM
policies defined for that user.
IAM returns the authorization information. If the user accessed
an application page, Google SecOps enables access to only those features that
the user has been granted access to.
If the user sent an API request, and does not have permission to perform the
requested action, the API response includes an error. Otherwise, a standard response is returned.
Google SecOps provides a set of predefined roles with a defined set of permissions
that control whether a user can access the feature. The single IAM policy
controls access to the feature using the web interface and the API.
If there are other Google Cloud services in the Google Cloud project bound to
Google SecOps, and you want to limit a user with the Project IAM Admin role
to modify only the Google SecOps resources, make sure to add IAM
conditions to the allow policy. See
Assign roles to users and groups
for an example of how to do this.
Administrators tailor access to Google SecOps features based on an employee's
role in your organization.
Before you begin
Make sure that you are familiar with
Cloud Shell
,
the
gcloud CLI command
, and the Google Cloud console.
Familiarize yourself with IAM, including the following concepts:
Overview of IAM
.
Overview of
roles and permissions
,
predefined roles
versus
custom roles
, and
creating custom roles
.
IAM conditions
.
Perform all steps in
Bind Google SecOps to a Google Cloud project
to set up a project that binds to Google SecOps.
Configure your identity provider, using one of the following:
Configure a Google Cloud identity provider
Perform all steps in
Integrate Google SecOps with a third-party identity provider
to set up authentication through a third-party identity provider (IdP).
Bind a project to your Google SecOps instance and configure the identity provider.
Make sure you have the permissions to perform the steps in this document.
For information about required permissions for each phase of the onboarding process,
see
Required roles
.
Plan your implementation
Create IAM policies that support your organization's
deployment requirements. You can use either Google SecOps predefined roles or
custom roles that you create.
Review the list of Google SecOps predefined roles and permissions against
your organization requirements. Identify which members of your organization should
have access to each Google SecOps feature. If your organization requires
IAM policies that differ from the predefined Google SecOps
roles, create custom roles to support these requirements. For information about
IAM custom roles, see
Create and manage custom roles
.
Summary of Google SecOps roles and permissions
The following sections provides a high level summary of predefined roles.
The most current list of Google SecOps permissions is in
IAM permissions reference
. Under the
Search for a permission
section, search for the term
chronicle
.
The most current list of predefined Google Security Operations roles is in
IAM basic and predefined roles reference
. Under
the
Predefined roles
section, either select the
Chronicle API roles
service
or search for the term
chronicle
.
For information about API methods and permissions, the
pages where permissions are used, and information recorded in Cloud Audit Logs
when the API is called, see
Chronicle permissions in IAM
.
Google SecOps predefined roles in IAM
Google SecOps provides the following predefined roles as they appear in IAM.
Predefined role in IAM
Title
Description
roles/chronicle.admin
Chronicle API Admin
Full access to Google SecOps application and API services, including global settings.
roles/chronicle.editor
Chronicle API Editor
Modify access to Google SecOps application and API resources.
roles/chronicle.viewer
Chronicle API Viewer
Read-only access to Google SecOps application and API resources
roles/chronicle.limitedViewer
Chronicle API Limited Viewer
Grants read-only access to Google SecOps application and API
      resources, excluding detection engine rules and retrohunts.
Google SecOps permissions in IAM
Google SecOps permissions correspond one-to-one with Chronicle
API methods. Each Google SecOps permission enables a specific action on a
specific Google SecOps feature when using the web application or the API.
Google SecOps APIs used with IAM are in the
Alpha
launch stage.
Google SecOps permission names follow the format
SERVICE.FEATURE.ACTION
.
For example, the permission name
chronicle.dashboards.edit
consists of the
following:
chronicle
: the Chronicle API service name.
dashboards
: the feature name.
edit
: the action that can be performed on the feature.
The permission name describes the action you can perform on the feature in
Google SecOps. All Google SecOps permissions have the
chronicle
service name.
Assign roles to users and groups
The following sections provide example use cases for creating IAM
policies. The term
<project>
is used to represent the project ID of the project
that you bound to Google SecOps.
After you enable the
Chronicle API
, the Google SecOps predefined roles
and permissions are available in IAM and you can create policies
to support organization requirements.
If you have a newly created Google SecOps instance, begin creating
IAM policies to meet organization requirements.
If this is an existing Google SecOps instance, see
Migrate Google SecOps to IAM for feature access control
for information about migrating the instance to IAM.
Example: Assign the Project IAM Admin role in a dedicated project
In this example, the project is dedicated to your Google SecOps instance.
You grant the
Project IAM Admin
role to a user so they can grant and modify the project's IAM role
bindings. The user can administer all Google SecOps roles and permissions
in the project and perform tasks granted by the
Project IAM Admin
role.
Assign the role using Google Cloud console
The following steps describe how to grant a role to a user using Google Cloud console.
Open Google Cloud console.
Select the project that is bound to Google SecOps.
Select
IAM & Admin
.
Select
Grant Access
. The
Grant Access to
<project>
appears.
Under the
Add Principals section
, enter the managed account email address in the
New principals
field.
Under the
Assign Roles
section, in the
Select a role menu
, select the
Project IAM Admin
role.
Click
Save
.
Open the
IAM > Permissions
page to verify the user was granted the correct role.
Assign the role using the Google Cloud CLI
The following example command demonstrates how to grant a user the
chronicle.admin
role
when using workforce identity federation.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
principal://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/subject/
USER_EMAIL
\
--role
=
roles/chronicle.admin
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
WORKFORCE_POOL_ID
: the identifier for the Workforce pool created for your Identity Provider.
USER_EMAIL
: the user's email address.
The following example command demonstrates how to grant a group the
chronicle.admin
role
when using Cloud Identity or Google Workspace.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
"user:
USER_EMAIL
"
\
--role
=
roles/chronicle.admin
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
USER_EMAIL
: the user's email address.
Example: Assign the Project IAM Admin role in a shared project
In this example, the project is used for multiple applications. It is bound to a
Google SecOps instance and runs services that are not related to Google SecOps.
For example, a Compute Engine resource used for another purpose.
In this case, you can grant the
Project IAM Admin
role to a user so they can
grant and modify the project's IAM role bindings and configure Google SecOps. You will also add
IAM s to the role binding to limit their access to only Google SecOps-related
roles in the project. This user can only grant roles specified in the IAM condition.
For more information about IAM conditions, see
Overview of IAM Conditions
and
Manage conditional role bindings
.
Assign the role using Google Cloud console
The following steps describe how to grant a role to a user using Google Cloud console.
Open Google Cloud console.
Select the project that is bound to Google SecOps.
Select
IAM & Admin
.
Select
Grant Access
. The
Grant Access to
<project>
appears.
In the
Grant Access to
<project>
dialog, under the
Add Principals section
,
enter the user email address in the
New Principals
field.
Under the
Assign Roles
section, in the
Select a role menu
, select the
Project IAM Admin
role.
Click
+ Add IAM Condition
.
In the
Add condition
dialog, enter the following information:
Enter a
Title
for the condition.
Select the
Condition editor
.
Enter the following condition:
api.getAttribute(iam.googleapis.com/modifiedGrantsByRole,[]).hasOnly([roles/chronicle.googleapis.com/limitedViewer, roles/chronicle.googleapis.com/viewer, roles/chronicle.googleapis.com/editor, roles/chronicle.googleapis.com/admin])
Click
Save
in the
Add condition
dialog.
Click
Save
in the
Grant Access to
<project>
dialog.
Open the
IAM > Permissions
page to verify the user was granted the correct role.
Assign the role using the Google Cloud CLI
The following example command demonstrates how to grant a user the
chronicle.admin
role and apply IAM conditions when using workforce identity federation.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
principal://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/subject/
USER_EMAIL
\
--role
=
roles/chronicle.admin
\
--condition
=
^:^
'expression=api.getAttribute(iam.googleapis.com/modifiedGrantsByRole,[]).hasOnly([roles/chronicle.googleapis.com/limitedViewer, roles/chronicle.googleapis.com/viewer, roles/chronicle.googleapis.com/editor, roles/chronicle.googleapis.com/admin])'
:
'title=Chronicle Role Admin'
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
WORKFORCE_POOL_ID
: the identifier for the Workforce
pool created for your Identity Provider.
USER_EMAIL
: the user's email address.
The following example command demonstrates how to grant a group the
chronicle.admin
role and apply IAM conditions when using Cloud Identity or Google Workspace.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
user:
USER_EMAIL
\
--role
=
roles/chronicle.admin
\
--condition
=
^:^
'expression=api.getAttribute(iam.googleapis.com/modifiedGrantsByRole,[]).hasOnly([roles/chronicle.googleapis.com/limitedViewer, roles/chronicle.googleapis.com/viewer, roles/chronicle.googleapis.com/editor, roles/chronicle.googleapis.com/admin])'
:
'title=Chronicle Role Admin'
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
USER_EMAIL
: the user email address, such as
bob@example.com
.
Example: Assign the Chronicle API Editor role to a user
In this situation, you want to give a user the ability to modify access to Chronicle API resources.
Assign the role using Google Cloud console
Open Google Cloud console.
Select the project that is bound to Google SecOps.
Select
IAM & Admin
.
Select
Grant Access
. The
Grant Access to
<project>
dialog opens.
Under the
Add Principals section
, in the
New principals
field, enter the user email address.
Under the
Assign Roles
section, in the
Select a role menu
, select the
Chronicle API Editor
role.
Click
Save
in the
Grant Access to
<project>
dialog.
Open the
IAM > Permissions
page to verify the user was granted the correct role.
Assign the role using the Google Cloud CLI
The following example command demonstrates how to grant a user the
chronicle.editor
role
 when using workforce identity federation.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
principal://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/subject/
USER_EMAIL
\
--role
=
roles/chronicle.editor
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
WORKFORCE_POOL_ID
: the identifier for the Workforce pool created for your Identity Provider.
USER_EMAIL
: the user's email address.
The following example command demonstrates how to grant a user the
chronicle.editor
role
when using Cloud Identity or Google Workspace.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
user:
USER_EMAIL
\
--role
=
roles/chronicle.editor
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
WORKFORCE_POOL_ID
: the identifier for the Workforce pool created for your Identity Provider.
USER_EMAIL
: the user's email address.
Example: Create and assign a custom role to a group
If Google SecOps predefined roles don't provide the group of permissions
that meet your organization's use case, you can create a custom role and assign
Google SecOps permissions to that custom role. You assign the custom role
to a user or group. For more information about IAM custom roles,
see
Create and manage custom roles
.
The following steps let you create a custom role called
LimitedAdmin
.
Create a YAML or JSON file that defines the custom role, called
LimitedAdmin
,
and the permissions granted to this role. The following is an example YAML file.
title: "LimitedAdmin"
description: "Admin role with some permissions removed"
stage: "ALPHA"
includedPermissions:
- chronicle.collectors.create
- chronicle.collectors.delete
- chronicle.collectors.get
- chronicle.collectors.list
- chronicle.collectors.update
- chronicle.dashboards.copy
- chronicle.dashboards.create
- chronicle.dashboards.delete
- chronicle.dashboards.get
- chronicle.dashboards.list
- chronicle.extensionValidationReports.get
- chronicle.extensionValidationReports.list
- chronicle.forwarders.create
- chronicle.forwarders.delete
- chronicle.forwarders.generate
- chronicle.forwarders.get
- chronicle.forwarders.list
- chronicle.forwarders.update
- chronicle.instances.get
- chronicle.instances.report
- chronicle.legacies.legacyGetCuratedRulesTrends
- chronicle.legacies.legacyGetRuleCounts
- chronicle.legacies.legacyGetRulesTrends
- chronicle.legacies.legacyUpdateFinding
- chronicle.logTypeSchemas.list
- chronicle.multitenantDirectories.get
- chronicle.operations.cancel
- chronicle.operations.delete
- chronicle.operations.get
- chronicle.operations.list
- chronicle.operations.wait
- chronicle.parserExtensions.activate
- chronicle.parserExtensions.create
- chronicle.parserExtensions.delete
- chronicle.parserExtensions.generateKeyValueMappings
- chronicle.parserExtensions.get
- chronicle.parserExtensions.legacySubmitParserExtension
- chronicle.parserExtensions.list
- chronicle.parserExtensions.removeSyslog
- chronicle.parsers.activate
- chronicle.parsers.activateReleaseCandidate
- chronicle.parsers.copyPrebuiltParser
- chronicle.parsers.create
- chronicle.parsers.deactivate
- chronicle.parsers.delete
- chronicle.parsers.get
- chronicle.parsers.list
- chronicle.parsers.runParser
- chronicle.parsingErrors.list
- chronicle.validationErrors.list
- chronicle.validationReports.get
- resourcemanager.projects.get
Create the custom role. The following example gcloud CLI command
demonstrates how to create this custom role using the YAML file you created in
the previous step.
gcloud
iam
roles
create
ROLE_NAME
\
--project
=
PROJECT_ID
\
--file
=
YAML_FILE_NAME
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
YAML_FILE_NAME
: the name of the file you created in the
previous step.
ROLE_NAME
: the name of the custom role as defined in the YAML file.
Assign the custom role using the Google Cloud CLI.
The following example command demonstrates how to grant a group of users the
custom role,
limitedAdmin
when using workforce identity federation.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
principalSet://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/group/
GROUP_ID
\
--role
=
projects/
PROJECT_ID
/roles/limitedAdmin
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
WORKFORCE_POOL_ID
: the identifier for the Workforce pool created for your identity provider.
GROUP_ID
: the group identifier created in workforce
identity federation. See
Represent workforce pool users in IAM policies
for information
about the group identifier created in workforce
identity federation. See
Represent workforce pool users in IAM policies
for information
about the
GROUP_ID
.
The following example command demonstrates how to grant a group of users the
custom role,
limitedAdmin
when using Cloud Identity or .
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--member
=
groupid:
GROUP_ID
\
--role
=
projects/
PROJECT_ID
/roles/limitedAdmin
Replace the following:
PROJECT_ID
: the project ID of the Google SecOps-bound
project you created in
Binding a Google SecOps instance to Google Cloud   project
.
See
Creating and managing projects
for a description of fields that identify a project.
WORKFORCE_POOL_ID
: the identifier for the Workforce pool created for your identity provider.
GROUP_ID
: the group identifier created in workforce
identity federation. See
Represent workforce pool users in IAM policies
for information
about the group identifier created in workforce
identity federation. See
Represent workforce pool users in IAM policies
for information
about the
GROUP_ID
.
Verify audit logging
User actions in Google SecOps and requests to the Chronicle API
are recorded as Cloud Audit Logs. To verify that logs are being written, perform
the following steps:
Sign in to Google SecOps as a user with privileges to access any feature.
See
Sign in to Google SecOps
for more information.
Perform an action, such as perform a Search.
In Google Cloud console, use the Logs Explorer to view the audit logs in the
Google SecOps-bound Cloud project. Google SecOps audit logs have the
following service name
chronicle.googleapis.com
.
For more information about how to view Cloud Audit Logs,
see
Google SecOps audit logging information
.
The following is an example log written when the user
alice@example.com
viewed the list of parser extensions in Google SecOps.
{
"protoPayload"
:
{
"@type"
:
"type.googleapis.com/google.cloud.audit.AuditLog"
,
"authenticationInfo"
:
{
"principalEmail"
:
"alice@example.com"
},
"requestMetadata"
:
{
"callerIp"
:
"private"
,
"callerSuppliedUserAgent"
:
"abc_client"
,
"requestAttributes"
:
{
"time"
:
"2023-03-27T21:09:43.897772385Z"
,
"reason"
:
"8uSywAYeWhxBRiBhdXRoIFVwVGljay0-REFUIGV4Y2abcdef"
,
"auth"
:
{}
},
"destinationAttributes"
:
{}
},
"serviceName"
:
"chronicle.googleapis.com"
,
"methodName"
:
"google.cloud.chronicle.v1main.ParserService.ListParserExtensions"
,
"authorizationInfo"
:
[
{
"resource"
:
"projects/100000000000/locations/us/instances/aaaa0aa0-000A-00a0-0000-0000a0aa0a1/logTypes/-"
,
"permission"
:
"chronicle.parserExtensions.list"
,
"granted"
:
true
,
"resourceAttributes"
:
{}
}
],
"resourceName"
:
"projects/100000000000/locations/us/instances/aaaa0aa0-000A-00a0-0000-0000a0aa0a1/logTypes/-"
,
"numResponseItems"
:
"12"
,
"request"
:
{
"@type"
:
"type.googleapis.com/google.cloud.chronicle.v1main.ListParserExtensionsRequest"
,
"parent"
:
"projects/100000000000/locations/us/instances/aaaa0aa0-000A-00a0-0000-0000a0aa0a1/logTypes/-"
},
"response"
:
{
"@type"
:
"type.googleapis.com/google.cloud.chronicle.v1main.ListParserExtensionsResponse"
}
},
"insertId"
:
"1h0b0e0a0"
,
"resource"
:
{
"type"
:
"audited_resource"
,
"labels"
:
{
"project_id"
:
"dev-sys-server001"
,
"method"
:
"google.cloud.chronicle.v1main.ParserService.ListParserExtensions"
,
"service"
:
"chronicle.googleapis.com"
}
},
"timestamp"
:
"2023-03-27T21:09:43.744940164Z"
,
"severity"
:
"INFO"
,
"logName"
:
"projects/dev-sys-server001/logs/cloudaudit.googleapis.com%2Fdata_access"
,
"receiveTimestamp"
:
"2023-03-27T21:09:44.863100753Z"
}
Migrate Google SecOps to feature RBAC for feature access control
Use information in these sections to migrate an existing Google Security Operations SIEM
instance from the legacy RBAC system to feature RBAC.
After you migrate to feature RBAC, you can also audit activity on the
Google SecOps instance using
Cloud Audit Logs
.
Differences between legacy RBAC and feature RBAC
Although feature RBAC predefined role names are similar to the legacy RBAC
roles, the feature RBAC predefined roles don't
provide identical feature access as the legacy RBAC roles. The permissions
assigned to each predefined feature RBAC role are slightly different.
For more information, see
How feature RBAC IAM roles map to legacy RBAC roles
.
You can use Google SecOps predefined roles as is, change the
permissions defined in each predefined role, or create custom roles and assign a
different set of permissions.
After you migrate the Google SecOps instance, you manage roles, permissions,
and feature RBAC policies using IAM in Google Cloud console.
The following Google SecOps application pages are modified to direct users to Google Cloud console:
Users & Groups
Roles
In legacy RBAC, each permission is described by the feature name and
an action. IAM permissions in feature RBAC are described by the resource name
and method. The following table illustrates the difference with two examples,
one related to Dashboards and the second related to Feeds.
Dashboard example
: To control access to Dashboards, the legacy RBAC provides five actions
that you can perform on dashboards. Feature RBAC provides similar IAM permissions with
one additional,
dashboards.list
, that lets a user list available dashboards.
Feeds example
: To control access to Feeds, legacy RBAC provides
seven actions that you can enable or disable. With feature RBAC there are four:
feeds.delete
,
feeds.create
,
feeds.update
, and
feeds.view
.
Feature
Permission in legacy RBAC
IAM permission in feature RBAC
Description of user action
Dashboards
Edit
chronicle.dashboards.edit
Edit dashboards
Dashboards
Copy
chronicle.dashboards.copy
Copy dashboards
Dashboards
Create
chronicle.dashboards.create
Create dashboards
Dashboards
Schedule
chronicle.dashboards.schedule
Schedule reports
Dashboards
Delete
chronicle.dashboards.delete
Delete reports
Dashboards
None. This is available in feature RBAC only.
chronicle.dashboards.list
List available dashboards
Feeds
DeleteFeed
chronicle.feeds.delete
Delete a feed.
Feeds
CreateFeed
chronicle.feeds.create
Create a feed.
Feeds
UpdateFeed
chronicle.feeds.update
Update a feed.
Feeds
EnableFeed
chronicle.feeds.update
Update a feed.
Feeds
DisableFeed
chronicle.feeds.update
Update a feed.
Feeds
ListFeeds
chronicle.feeds.view
Return one or more feeds.
Feeds
GetFeed
chronicle.feeds.view
Return one or more feeds.
Steps to migrate existing access control permissions
After you complete steps to
migrate an existing Google SecOps instance
, you can also migrate your feature access control configuration.
Google SecOps provides auto-generated commands that create new
feature RBAC IAM policies equivalent to your legacy RBAC,
which is configured in Google SecOps, under the
SIEM Settings
>
Users and Groups
page.
Make sure you have the required permissions described in
Configure a Google Cloud project for Google SecOps
, and then follow the steps in
Migrate existing permissions and roles to IAM
.
How feature RBAC IAM roles map to legacy RBAC roles
The mapping information in this section illustrates some of the differences
in access for predefined roles before and after migration. Although legacy RBAC
role names are similar to feature RBAC IAM predefined roles, the actions
that each provide access to are different. This section provides an introduction
to some of these differences.
Chronicle API Limited Viewer
This role grants read-only access to the Google SecOps application and API resources,
excluding detection engine rules and retrohunts. The role name is
chronicle.limitedViewer
.
For a detailed list of the permissions, see
Chronicle API Viewer
.
Chronicle API Viewer
This role provides read-only access to the Google SecOps application and API
resources. The role name is
chronicle.viewer
.
The following permissions illustrate some of the differences between similar
legacy RBAC and feature RBAC roles. For a detailed list of the permissions,
see
Chronicle API Viewer
.
Feature RBAC IAM permission
Equivalent permission is mapped to this legacy RBAC role
chronicle.ruleDeployments.get
Viewer
chronicle.ruleDeployments.list
Viewer
chronicle.rules.verifyRuleText
Viewer
chronicle.rules.get
Viewer
chronicle.rules.list
Viewer
chronicle.legacies.legacyGetRuleCounts
Viewer
chronicle.legacies.legacyGetRulesTrends
Viewer
chronicle.rules.listRevisions
Viewer
chronicle.legacies.legacyGetCuratedRulesTrends
Viewer
chronicle.ruleExecutionErrors.list
Viewer
chronicle.curatedRuleSets.get
Viewer
chronicle.curatedRuleSetDeployments.get
Viewer
chronicle.curatedRuleSets.list
Viewer
chronicle.curatedRuleSetDeployments.list
Viewer
chronicle.curatedRuleSetCategories.get
Viewer
chronicle.curatedRuleSetCategories.list
Viewer
chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections
Viewer
chronicle.curatedRuleSets.countCuratedRuleSetDetections
Viewer
chronicle.curatedRules.get
Viewer
chronicle.curatedRules.list
Viewer
chronicle.referenceLists.list
Viewer
chronicle.referenceLists.get
Viewer
chronicle.referenceLists.verifyReferenceList
Viewer
chronicle.retrohunts.get
Viewer
chronicle.retrohunts.list
Viewer
chronicle.dashboards.schedule
Editor
chronicle.operations.get
None. This is available in feature RBAC only.
chronicle.operations.list
None. This is available in feature RBAC only.
chronicle.operations.wait
None. This is available in feature RBAC only.
chronicle.instances.report
None. This is available in feature RBAC only.
chronicle.collectors.get
None. This is available in feature RBAC only.
chronicle.collectors.list
None. This is available in feature RBAC only.
chronicle.forwarders.generate
None. This is available in feature RBAC only.
chronicle.forwarders.get
None. This is available in feature RBAC only.
chronicle.forwarders.list
None. This is available in feature RBAC only.
Chronicle API Editor
This role enables users to modify access to Google SecOps application and API
resources. The role name is
chronicle.editor
.
The following permissions illustrate some of the differences between the similar
legacy RBAC and feature RBAC roles. For a detailed list of the permissions,
see
Chronicle API Editor
.
Feature RBAC IAM permission
Equivalent permission is mapped to this legacy RBAC role
chronicle.ruleDeployments.update
Editor
chronicle.rules.update
Editor
chronicle.rules.create
Editor
chronicle.referenceLists.create
Editor
chronicle.referenceLists.update
Editor
chronicle.rules.runRetrohunt
Editor
chronicle.retrohunts.create
Editor
chronicle.curatedRuleSetDeployments.batchUpdate
Editor
chronicle.curatedRuleSetDeployments.update
Editor
chronicle.dashboards.copy
Editor
chronicle.dashboards.edit
Editor
chronicle.dashboards.create
Editor
chronicle.legacies.legacyUpdateFinding
Editor
chronicle.dashboards.delete
Editor
chronicle.operations.delete
None. This is available in feature RBAC only.
Chronicle API Admin
This role provides full access to the Google SecOps application and API services,
including global settings. The role name is
chronicle.admin
.
The following permissions illustrate some of the differences between the similar
legacy RBAC and feature RBAC roles. For a detailed list of the permissions,
see
Chronicle API Admin
.
Feature RBAC IAM permission
Equivalent permission is mapped to this legacy RBAC role
chronicle.parserExtensions.delete
Admin
chronicle.parsers.copyPrebuiltParser
Admin
chronicle.extensionValidationReports.get
Admin
chronicle.extensionValidationReports.list
Admin
chronicle.validationErrors.list
Admin
chronicle.parsers.runParser
Admin
chronicle.parserExtensions.get
Admin
chronicle.parserExtensions.list
Admin
chronicle.validationReports.get
Admin
chronicle.parserExtensions.create
Admin
chronicle.parserExtensions.removeSyslog
Admin
chronicle.parsers.activate
Admin
chronicle.parserExtensions.activate
Admin
chronicle.parsers.activateReleaseCandidate
Admin
chronicle.parsers.deactivate
Admin
chronicle.parsers.deactivate
Admin
chronicle.parserExtensions.generateKeyValuechronicle.Mappings
Admin
chronicle.parserExtensions.legacySubmitParserExtension
Admin
chronicle.parsers.activate
Admin
chronicle.parsers.activate
Admin
chronicle.parsers.activate
Admin
chronicle.parsers.list
Admin
chronicle.parsers.create
Admin
chronicle.parsers.delete
Admin
chronicle.feeds.delete
Admin
chronicle.feeds.create
Admin
chronicle.feeds.update
Admin
chronicle.feeds.enable
Admin
chronicle.feeds.disable
Admin
chronicle.feeds.list
Admin
chronicle.feeds.get
Admin
chronicle.feedSourceTypeSchemas.list
Admin
chronicle.logTypeSchemas.list
Admin
chronicle.operations.cancel
Editor
chronicle.collectors.create
None. This is available in feature RBAC only.
chronicle.collectors.delete
None. This is available in feature RBAC only.
chronicle.collectors.update
None. This is available in feature RBAC only.
chronicle.forwarders.create
None. This is available in feature RBAC only.
chronicle.forwarders.delete
None. This is available in feature RBAC only.
chronicle.forwarders.update
None. This is available in feature RBAC only.
chronicle.parsingErrors.list
None. This is available in feature RBAC only.
Need more help?
Get answers from Community members and Google SecOps professionals.
