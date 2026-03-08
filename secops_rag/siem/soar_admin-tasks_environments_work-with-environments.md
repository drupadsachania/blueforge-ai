# Work with your environments

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments/  
**Scraped:** 2026-03-05T09:15:04.623879Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Work with your environments
Supported in:
Google secops
SOAR
Environments represent distinct networks, customers, or business units managed by your SOC or Managed Security Service Provider (MSSP). They help segment data, actions, and visibility across different operational contexts.

This document explains how to work with your environments to make it easier to manage security operations for multiple tenants or organizational divisions from a single platform.
Add a new environment
When you add a new environment, it lets your SOC or MSSP manage and monitor distinct networks, customers, or business units within the platform. This setup helps isolate data and workflows across different environments while maintaining centralized visibility and control.
The platform provides a predefined environment named
Default Environment
by default.
Use the following steps to configure and register a new environment in Google Security Operations
Go to
Settings
>
Organization
>
Environments
.
Click
add
Add
.
In the
Add Environment
dialog, enter the required information.
Optional: Select the
Append to all Users and API Keys
checkbox to automatically assign the new environment to all existing users and API keys. You can also add an alias if a third-party integration uses a different tenant name.
If the
Allow Data Retention Period per Environment
checkbox
    is not selected in
Settings
>
Advanced
>
General
, specify the time period for deleting information related to closed cases in this environment.
Click
Create
. The new environment appears in the list of environments.
Allow access to other environments
Google Security Operations offers you a way to create a customized Cross Environment Policy that works for your organization's needs. Use the
Cross Environment Policy
settings to choose the required permissions for assigning users to cases and moving cases between environments.
Assign cases in environments
With the
Assign Case
option, you can let users have access to a specific cases in environments where they don't have default permissions. This option is useful when you need to investigate or collaborate on cases outside your assigned environment. With this permission enabled, you can also assign manual actions, create case tasks, and add mentions in the case wall or chat. As a best practice, we recommend keeping the
Assign Case
setting at
Prevent
(default).
Move cases between environments
Under
Move Case
option, you can control whether users are granted permission to move cases between environments. This is helpful when you investigate alerts in the context of a different environment within the organization.
Assign cases across environments
To assign a case, follow these steps:
Go to
Settings
>
Advanced
>
General
.
In the
Cross Environment Policy
dialog, under
Assign Case
, select
Allow users to assign cases to users from other environments
.
Click
Save
.
Move cases to a different environment
To move cases to a different environment, follow these steps:
Click
Settings
>
Advanced
>
General
.
In the
Cross Environment Policy
dialog, under
Move Case
, select
Allow users to move cases between environments
.
Click
Save
.
Delete an environment
To delete an environment, follow these steps:
Go to
Settings
>
Organization
>
Environments
.
Select the required environment, and then click
edit
Edit
.
In the
Edit Environment
dialog, click
delete
Delete
. The
Delete
page lists all configurations and utilities associated with this environment. Once you delete this environment, you
    can't undo this action.
Click
Confirm
.
Need more help?
Get answers from Community members and Google SecOps professionals.
