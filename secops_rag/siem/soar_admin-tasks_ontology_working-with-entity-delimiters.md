# Work with entity delimiters

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/working-with-entity-delimiters/  
**Scraped:** 2026-03-05T09:31:10.029597Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Work with entity delimiters
Supported in:
Google secops
SOAR
Entity delimiters
let you decide for each entity type and data source how to map the incoming entity. You can disable
  delimiters for incoming entities, map a specific delimiter (up to 64
  characters), or use a regular expression instead.
For example, if you have several files separated by commas in a single entity,
you can set the delimiter to a comma so the system treats each file as a separate entity.
You can use entity delimiters in two places:
On the
Event Configuration
>
Mapping
page.
On the
Playbook action
>
Siemplify
>
Create Entity
page.
Event configuration & mapping
The Event Configuration feature lets you assign visual families to events,
providing a graphic visualization of their relationships with other actions. This
process ensures events are correctly categorized and contain accurate and
complete information. For details, see
configure mapping and assign visual families
.
Need more help?
Get answers from Community members and Google SecOps professionals.
