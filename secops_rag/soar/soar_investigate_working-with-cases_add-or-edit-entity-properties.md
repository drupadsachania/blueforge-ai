# Add or edit entity properties

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-or-edit-entity-properties/  
**Scraped:** 2026-03-05T10:07:29.522455Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Add or edit entity properties
Supported in:
Google secops
SOAR
This document explains how you can add or edit entity enrichment properties directly from investigation pages as part of your 
    case investigation in Google Security Operations to work more efficiently during case analysis. You can add up to 100 entity properties to a single entity.
Add or edit entity properties across pages
Add or edit an entity enrichment property on the following pages:
Investigation
: In the case view, click
Explore
to open the
Investigation
page.
Entity Explorer
: In the case view, click the
Entity Highlights
widget and select the relevant entity.
Cases (Entities Highlights)
: In the case view, click an entity in
      the
Entity Highlights
widget and then click
View more
to
      open a side drawer with entity properties.
Cases (Entities Graph)
: In the case view, click the
Entities Graph
widget and then click
Entity
. A side drawer opens with entity
      properties.
Add an entity property
As part of the investigation, include other entity keys to enrich your case 
    investigation. Identify the kind of malware being used to better understand 
    the threat. This example shows how to create a new entity property called
Malware_family
.
To add an entity property, follow these steps:
Go to the
Cases
queue.
Select the
Virus Found or Security Risk Found
case, and click
Explore
to open the
Investigation
page.
Click
add
Add
.
Enter
Malware_family
as the
Key
and
Trojan.Generic
as the
Value
.
Click
Save
to add the new entity property.
The new enrichment provides an additional layer of understanding during 
  your case investigation.
Add new or existing entities
To add new or existing entities, follow these steps:
Click
more_vert
Alert Options
and select
Add Entity
.
In the
Add entities to alert
dialog, select an entity from 
    either
Add existing entities
or
Add new entity
.
Enter an identifier and click
add
Add
>
Apply
.
Edit an entity property
This example follows a use case where a file is marked as suspicious with
    low confidence in a case related to a potential malware threat. After
    running a TI enrichment block and investigation, you're confident that the
    file is malicious and want to update the
confidence_level
from
Low
to
High
.
To edit an entity property, follow these steps:
Go to the
Cases
page.
Go to the
Virus Found or security risk found
case, and 
    click
Explore
to open the
Investigation
page.
Click
tag
File Hash Entity
on the
Investigation
page.
Hold the pointer over the
confidence_level
value in the side 
    drawer.
Click
more_vert
More
and select
View or edit property
.
In the
View or Edit Entity Property
dialog, change the value of
Confidence_level
from
Low
to
High
to highlight the potential risk of the hash entity. You can
      also select a display format to control how the data appears in the side drawer.
Click
Save
.
The confidence level of the entity is updated and reflected in the side 
  drawer.
Need more help?
Get answers from Community members and Google SecOps professionals.
