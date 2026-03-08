# Let Google Support access your instance

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/allow-google-support-access/  
**Scraped:** 2026-03-05T09:46:25.980238Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Let Google Support access your instance
Supported in:
Google secops
SOAR
Google Support may require access to your Google Security Operations instance to troubleshoot SOAR functionality issues. Use the following steps to grant access:
Go to
Settings
>
Advanced
>
Support Access
.
Click the
Allow Access
toggle to the on position.
Select the required
SOC Role
,
Permission Group
, and
Environments
. 
  These settings determine the access privileges for the Google Support user. The selected permission group must have the correct
Edit
and
View
settings for the required modules.
Select a time period. This period determines how long a Google Support user has access to your system. We recommend that this matches the period you defined in your local settings. You can shorten the access period at any time by clicking the
Allow Access
toggle to the off position.
Click
Save
. The user is created with the specified details and appears on the page.
Need more help?
Get answers from Community members and Google SecOps professionals.
