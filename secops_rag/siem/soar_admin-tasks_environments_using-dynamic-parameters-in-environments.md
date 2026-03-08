# Manage dynamic parameters in environments

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/using-dynamic-parameters-in-environments/  
**Scraped:** 2026-03-05T09:15:07.685868Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage dynamic parameters in environments
Supported in:
Google secops
SOAR
This document explains how to use dynamic parameters to create custom categories or groups for your environments in Google Security Operations.
  Dynamic parameters are especially useful for playbooks, letting you define custom triggers, actions, or conditions based on these parameters.  This enhanced customization
  benefits both enterprises and Managed Security Service Providers (MSSPs) who manage multiple tenants.
Add a dynamic parameter
To add a dynamic parameter, follow these steps:
Go to
Settings
>
Organization
>
Environments
.
On the
Environments
page, click
format_list_bulleted
List
and select
Add Dynamic Parameters
.
In the
Dynamic Parameters
dialog, click
add
Add
to add a new parameter.
Enter a name for the parameter (for example,
Service Package
).
Choose one of the following ways to set the parameter value:
Enter a string and a default value. The system applies the default value
      to all existing environments.
Select
List
, enter your values in the
List Content
field,
      and press
Enter
after each value. Then, select a default value from the list.
Click
Save
>
Done
. The system applies the dynamic
  parameter and its selected default value to all existing environments and displays
  it on the main page.
Edit parameter values in bulk
To update multiple parameter values at once, export them to a spreadsheet, make changes, and re-import them.
To edit parameters in bulk using export or import, follow these steps:
Click
format_list_bulleted
List
and select
Export Dynamic Parameters
.
In the spreadsheet, edit the values as needed. You can't change the
Parameter
names or
Environment
names.
When finished, click
format_list_bulleted
List
and select
Import Dynamic Parameters
.
Need more help?
Get answers from Community members and Google SecOps professionals.
