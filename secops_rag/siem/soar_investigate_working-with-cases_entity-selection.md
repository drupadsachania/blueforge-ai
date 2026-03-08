# Entity selection

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/entity-selection/  
**Scraped:** 2026-03-05T09:34:27.713060Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Entity selection
Supported in:
Google secops
SOAR
This document explains how Google Security Operations extracts and uses entities
from ingested alerts. When Google SecOps ingests an alert,
it also includes the underlying security events. These events are analyzed to
extract key indicators—such as IP addresses, usernames, and domains—which are
then modeled as objects called
entities
. Each entity includes its own set
of properties.
View the properties of an entity
On the
Cases
page, select a case. In the default case view, the 
entities appear in the
Entity Highlights
section on the
Case Overview
and
Alerts
tabs.
Click
View Details
to open a side drawer that shows all properties of
the selected entity.
Click an entity name to open the
Entity Explorer
in a new tab. The
Entity Explorer
displays all cases associated with the selected entity.
Entity Selection action
When an alert is ingested, a playbook is automatically or semi-automatically
triggered, depending on the configured conditions. Google SecOps uses
these playbooks to determine how to handle the alert.
Each action within a playbook operates on a specific group of entities. The
Entity Selection
action lets you define these groups based on entity
properties. For example, you can create a group containing only internal
entities to be used with actions tailored for internal assets.
Use the
Entity Selection
action to build different groups depending on
the logic you want to apply. When you use this method, it helps each action
operate only on the relevant entities.
Create a new entity group
To create an entity group using the
Entity Selection
action, follow these steps:
Go to the
Playbooks
page and click
Open Step Selection
.
In the
Step Selection
tab, select
Actions
>
Flow
.
Drag
Entity Selection
into the second box labeled
Drag a step over 
here
.
Double-click the
Entity Selection
box to 
configure the new group of entities.
Add the conditions needed to select the new group of entities. For example, 
select all IP address entities that were enriched by VirusTotal v3 and flagged as
malicious by more than 10 engines.
Once defined, the new entity group becomes available for all subsequent actions in the playbook.
Need more help?
Get answers from Community members and Google SecOps professionals.
