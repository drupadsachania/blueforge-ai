# Configure mapping and assign visual families

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/configure-mapping-and-assign-visual-families/  
**Scraped:** 2026-03-05T10:03:30.557578Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure mapping and assign visual families
Supported in:
Google secops
SOAR
The
Event Configuration
feature lets you assign visual families to events, providing
a graphic visualization of their relationships with other actions. This process
ensures events are correctly categorized and contain accurate and complete
information.
Event configuration contains the following capabilities:
Visualization
: Assign a
family
to an event. This family
acts as a visual map of relationships and entities, giving you the best graphic
explanation of what happened. The assigned family appears on the
Explore Cases
screen.
Mapping
: Edit or add specific field information to correct errors or fill in missing data.
Access the Event Configuration page
To access the
Event Configuration
page, do one of the following:
Select a case from the case queue, go to the alert
Events
tab, and click
settings
Configure
.
In
Settings
>
Ontology
>
Ontology Status
, click
settings
Configure
.
Assign a model family
The model family provides a graphic visualization of the relationship between
all the events and actions that take place.
The
Visualization
page is where you assign the
event, product, or source to a specific family. This visual family appears on the
Explore
page.
You can assign a model family at three levels:
Source Level
: The top level. A family assigned here is inherited by
all products and events within that source.
Product Level
: The second level. A family assigned here is inherited
by all events within that product.
Event Level
: The ground level.
The model family is inherited from the
parent
. If you assign a family at source level, the product and event inherit the model family from the source level. You can edit the mapped fields at each level to override the
  parent settings.
Mapping and visual family precedence
When an event is ingested, the system starts by looking for mapping
rules at the most specific level (the
event
level) and works 
its way up. This inheritance logic ensures completeness by sourcing rules up the 
chain:
event
>
product
>
vendor
.
However, the visual family (schema) assigned to the event always acts as the 
final validator, determining which entities are actually valid for that data.
The following use cases illustrate how this hierarchy works:
Use Case 1: Successful mapping inheritance
If a mapping for the
SourceIp
entity is not defined at the
event
level, the system automatically checks the next level (the
product
level) to find that mapping. If it's there, the rule is 
successfully applied to your event data.
Use Case 2: Schema conflict and entity failure
If
FileName
is mapped at the
product
level, the 
system inherits this rule. However, if the visual family assigned to the event 
doesn't have the necessary entity field for
FileName
in its schema, 
the entity creation fails.
The visual family at the lowest level (
event
level) acts as the 
final schema validator. If an inherited mapping references an entity that the 
event's visual family doesn't support, that validation blocks the entity 
creation.
Google Security Operations provides 24 standard model families, and you can
create more as needed. For more information, see
Map security event relationships with visual families
.
To assign a model family, follow these steps:
On the
Events Configuration
page, click
Visualization
.
Select the model family that most resembles the relationship between events
and actions that occur in this situation.
In the
Confirmation
dialog, click
Yes
to confirm the assignment.
Manage an event's specific field
The
Mapping
page is where you manage an event's specific field information.
It displays the fields that belong to the assigned model family.
For example, if an event is ingested and you can see missing or incorrect information, do the following:
On the
Alerts Events
tab, click
settings
Configure
and verify that it's assigned to the correct visual family.
Go to the
Mapping
page to edit or add specific field information.
You can perform various actions on these fields:
Click
more_vert
More
at the end of each row.
Click
edit
Edit Field
.
In the
Map Target Field
dialog, enter the name of the event field to extract and click
Save
.
Editable fields
Double-click the entity to edit the following fields:
Field
Description
Extracted Field
Main field name in the raw event field to take information from.
        Pro-tip: Use
Contains
or
Starts with
to divide data into
        separate entities. This is useful for multiple
        fields like
url_1
and
url_2
to create multiple entities.
Alternative Field 1
Fallback field in the raw event field to take information from if the
        primary field isn't found.
Alternative Field 2
Fallback field in the raw event field to take information from if both
        primary and secondary aren't found.
Extraction Function
Extracts or manipulates data from the raw event field, including these three options:
None
: the raw data is
        presented as is.
Delimiter
: Delimiter can be defined with a
        character (or up to 64 characters) to divide the data into separate
        entities. The default is Delimiter = , (comma)
Regular expression
: Uses a regular expression
        to divide data into separate entities.
Transformation Function
Transforms information from the data source to be compatible with the database. Available functions
        are:
TO_STRING
FROM_UNIXTIME_STRING_OR_LONG
FROM_CUSTOM_DATETIME
EXTRACT_BY_REGEX
TO_IP_ADDRESS
Once you've chosen the function, add the
        appropriate parameter.
For example, select
FROM_CUSTOM_DATETIME
and reformat the date and time to
%Y-%m-%DT%H:%M:%S
.
You can extract data from one source field and map it to different
  target fields. For example, if a source field has both a hostname and an IP
  address, you can separate them using regular expressions.
Show results after mapping
To view the values after the mapping process, click
more_vert
More
>
Show Result
.
Add enrichment data
Various SIEMs include enrichment data as part of the initial ingestion
  process. To add enrichment data, follow these steps:
Select
more_vert
More
>
database_upload
Add Enrichment
.
Choose which enrichment values you want to add to the entity.
Click
Save
. The next time this entity is ingested into the platform
  as part of the alert, click
View Details
and this enrichment field
  will appear under the
Raw Enrichment
heading in the side
  drawer.
Need more help?
Get answers from Community members and Google SecOps professionals.
