# Manage API keys

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-api-keys/  
**Scraped:** 2026-03-05T09:15:35.563009Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage API keys
Supported in:
Google secops
SOAR
To authenticate and connect using the Google Security Operations SOAR API,
you must first create an API key.
You can access the SOAR API over port 443.
To create a new API key:
Go to
Settings
>
Advanced
>
API keys
.
Click
add
Add
.
On the
API
page, enter the name for
  the application that requires API access to Google SecOps SOAR.
Select the required permission group for this API key. The
  groups on this menu are defined on the
Organizations
>
Permissions
page.
Select the environments to associate with the API key. If you select all current environments, the key only applies to environments that exist at the time of creation. To confirm access to new environments, use a permission group with
All Environments
enabled.
Select the SOC role. For information about SOC roles, see
Control access to the platform
.
Click
Save
. The new key appears on the
API keys
page.
Need more help?
Get answers from Community members and Google SecOps professionals.
