# Configure data RBAC for Dashboards

**Source:** https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-dashboards/  
**Scraped:** 2026-03-05T09:14:50.232631Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure data RBAC for Dashboards
Supported in:
Google secops
SIEM
This document explains how Google Security Operations administrators can assign scopes 
to dashboards. The Dashboards feature of Google Security Operations
is built from charts populated using YARA-L 2.0 properties.
Scopes assigned to a user determine the results that appear on a user's dashboard.
Data RBAC implementation may vary based on the data source in the chart query.
For more information, see
Events, entity graph, and IoC matches
.
To understand how data RBAC works, see
Overview of Data RBAC
.
Before you begin
Review the core concepts of data RBAC, including access types, user roles, the function of labels and scopes, and the impact of
data RBAC on Google SecOps features. For details about data RBAC, see
Data RBAC overview
.
Onboard your Google SecOps instance. For more information, see
Onboard a Google SecOps instance
.
Confirm you have the
required roles
to manage Identity and Access Management permissions.
Grant user access to Dashboards
To grant a user or group access to Dashboards, follow these steps:
In the Google Cloud console, click
IAM
>
Grant Access
.
In the
New principals
field, enter the email address for the user or group.
To simplify management, we recommend to grant roles to Google groups, not individual users.
In the
Select a role
list, search for "Chronicle SIEM", and then select the
required predefined or custom role. For example,
Chronicle SIEM Restricted Viewer
.
If you assigned a scoped role (like
Restricted Viewer
), you must also assign the
user to a specific Log Scope to filter their data view. For more information, see
Configure data access control using Log Scopes
.
Click
Save
.
The user now has the granted permissions for all dashboards they're authorized to see within the project.
Need more help?
Get answers from Community members and Google SecOps professionals.
