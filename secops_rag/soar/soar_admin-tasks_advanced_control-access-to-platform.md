# Control access to the platform using SOAR permissions

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform/  
**Scraped:** 2026-03-05T09:45:44.287378Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Control access to the platform using SOAR permissions
Supported in:
Google secops
SOAR
This document explains how these mechanisms—SOC roles, environments, and either permission groups or IAM roles—work together to control user access to different parts of the platform.
It also describes how these mechanisms determine who can view cases.
Assign SOC roles
You can assign different access rights to SOC roles to control the scope of
responsibility for each user group in Google Security Operations.
Google SecOps includes predefined SOC roles, but you can also add custom roles.
The predefined SOC roles are defined as follows:
Tier 1
: Perform basic triage on the alerts.
Tier 2
: Review high-priority security threats.
Tier 3
: Handle major incidents.
SOC Manager
: Manage  the SOC team.
CISO
: Serve as the top-level manager within your organization.
Administrator
: Access the entire Google SecOps platform.
You can set one of these SOC roles as the default, and the system automatically
assigns it to incoming cases. Each SOC role can also have additional SOC roles
attached to it, letting users monitor all cases assigned to those roles.
For example, a Tier 1 analyst can see cases assigned to their Tier 1 role and any additional roles.
After a case is created, you can reassign it from the default SOC role to a
specific SOC role or an individual user—manually or with a playbook automated action. Assigning a case to a SOC role makes sure that a group of people is aware
of it. When an analyst self-assigns the case, they indicate that they're
handling it.
For more information about SOC roles, see
Manage SOC roles
.
Environments and environment groups
You can define different environments and environment groups to create logical data segregation.
This separation applies to most platform modules, such as cases, playbooks, ingestion,
and dashboards. This process is useful for businesses and Managed Security Service Providers
(MSSPs) who need to segment their operations and networks. Each environment or
group can have its own unique automation processes and settings. For MSSPs with
many different customers, each environment or group can represent a separate customer.
You can configure platform settings so that only analysts associated with a
specific environment or group can see its cases. For example, you can configure
the playbooks module for multiple environments. The system uses the default
environment as the platform baseline when you've not defined or selected
other environments. Platform administrators have access to all current and
future environments and environment groups.
For more information about environment groups, see
Work with environments
Permission groups or IAM roles
Google SecOps lets you create groups of users and assign different permission levels to various modules. Prior to
migrating SOAR to Google Cloud
, these are controlled by permission groups in the SOAR Settings. After you complete the SOAR migration to Google Cloud, these are controlled by IAM roles.
Permission groups (pre migration)
The Google SecOps platform includes predefined permission groups,
and you can add permission groups, as needed. The predefined groups are as follows:
Admin
Basic
Readers
View Only
Collaborators
Managed
Managed-Plus
Permission groups control the level of access each group has to different
modules and settings in the platform. You can set permissions at a granular level.
For example:
Top level
: Enable access to the Reports module for a specific permission group.
Mid level
: Enable access only to view advanced reports.
Granular level
: Let users edit advanced reports.
For more information about permission groups, see
Manage permission groups
IAM roles (post migration)
After you complete SOAR Migration to Google Cloud, the permission groups are migrated into IAM roles.
For more information on migrating permission groups to IAM roles, see
Migrate SOAR permissions.
The Google SecOps platform supports predefined IAM roles
as well as custom roles, which you can add, as needed. The predefined IAM SOAR roles are as follows:
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
roles/chronicle.soarAdmin
Chronicle SOAR Admin
Full administrative access to SOAR settings and management.
Map users
There are different ways to map users depending on whether or not you have migrated to Google Cloud:
Pre SOAR migration - SOC roles, permission groups and environments map to different IdP groups,
or user email groups depending on how you have authenticated to the product.
Post SOAR migration - SOC roles and environments map to different IAM roles.
For more information about how to map users in the platform, see the document that applies to you:
If you have set up authentication using Workforce Identity Federation, and are pre-migration, map IdP Groups to Permission Groups, SOC Roles and Environments. See
Map users in the platform
.
If you have set up authentication using Cloud Identity, and are pre migration, map user email groups to Permission Groups, SOC Roles and Environments. See
Map users in the platform using Cloud Identity
.
If you have set up authentication using Cloud Identity, and are post migration, map IAM roles to SOC Roles and Environments. See
Map users in the platform using Cloud Identity
.
Google SecOps SOAR standalone customers, see
Manage users
.
Need more help?
Get answers from Community members and Google SecOps professionals.
