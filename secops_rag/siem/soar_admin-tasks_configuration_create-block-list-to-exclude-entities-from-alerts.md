# Create a blocklist to exclude entities from alerts

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/create-block-list-to-exclude-entities-from-alerts/  
**Scraped:** 2026-03-05T09:15:41.559964Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create a blocklist to exclude entities from alerts
Supported in:
Google secops
SOAR
You can create a blocklist of items to prevent the system from grouping
alerts by specific entities, or to exclude entities from being displayed in the system.
Add a new blocklist item
To add a new blocklist item, follow these steps:
Go to
SOAR Settings
>
Environments
>
Blocklist
.
Click
add
Add Blocklist
.
Enter the
Entity Identifier
.
Select the
Entity Type
.
Choose the appropriate
Action
:
Do not group alerts
: The entity won't be used to group 
          alerts. Alerts containing this entity remain visible.
Do not create entity
: The system doesn't create or process 
          this entity.
Choose the relevant
Environment
.
Click
Add
.
For more information about how grouped alerts are managed, see
Configure alert grouping
.
Need more help?
Get answers from Community members and Google SecOps professionals.
