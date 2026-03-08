# Map security event relationships with visual families

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/visual-families/  
**Scraped:** 2026-03-05T09:31:07.529589Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Map security event relationships with visual families
Supported in:
Google secops
SOAR
Google Security Operations provides a collection of predefined visual families 
that cater to many common alert types. The default visual family includes all entity 
types and fundamental relationships.
Visual families
represent relationships between entities in a security event 
and help identify key actors and the flow of a security incident.
Each visual family consists of multiple rules. Each rule contains up to four 
sources, up to four destinations, and a connection type. Both sources and destinations 
represent entity types relevant to the alert, and connections between them are 
either
Typed
or
Linked
.
Typed
connections link the primary entities (actors) within an alert. They typically represent an action performed by one entity on another (or itself) 
and are displayed as an arrowed line. Each visual family must contain a single typed connection rule.
Linked
connections connect two or more logically related entities,
such as a hostname and IP address, or an email and username. They are represented
by a dotted line, signifying this logical relationship.
Additionally, visual families define which entity types can be involved in the event. 
When you map event fields to entities, the allowable entity types are predetermined 
by the visual family assigned to that event type.
Visual families are applied to events from a specific type or product, and are 
dynamically aggregated with other events to create a visual entity graph for the entire alert and case. 
You can view this graph on the
Event configuration > visualization
page or the
Explore
page.
Define a visual family
Follow these steps to create a visualization that shows the relationships and connections between entities:
Identify the event requiring a visual family.
Classify and map the fields 
    to their respective entity types. For this example, use the following
Suspicious Connection
event:
{
  "name": "Suspicious Connection", 
  "product": "SecOps", 
  "event_type": "Suspicious connection", 
  "hostname": "USER_PC", 
  "process_sha256": "6857fee8812490499164bb7efb7f457d038e82140bb1fa0adbd0dc018e404f84", 
  "process_name": "notepad.exe", 
  "destination_domain": "google.com",
  "destination_ip_address": "8.8.8.8" 
}
Classify event fields to specific entity types as follows:
Field
Entity type
hostname
SourceHostName
process_name
SourceProcessName
process_sha256
FileHash
destination_domain
DestinationDomain
destination_ip_address
DestinationAddress
Go to
Settings
>
Ontology
>
Visual Families
.
Select
add
Add
and enter a name and description.
Define the mandatory typed connection rule by identifying the primary action. In this example, because a process created a connection to a domain, the
process
entity is the source and the
domain
entity is the destination.
Define logically related entities with linked connection rules.
Using the same event example, you can observe several relations:
SourceProcessName
was executed on the
SourceHostName
.
The
SourceProcessName
hash is the
FileHash
entity
DestinationDomain
and
DestinationAddress
represent the process destination.
Save the visual family. Once saved, you can optionally add an image that represents the 
visual family in the
Settings
>
Ontology
>
Visual Families
table.
Floating entities
A
floating entity
is one that appears in a graph visualization without
any connections to other entities. This can happen for a few key reasons, and
understanding why is crucial for effective data analysis and visualization:
Missing a connection rule in the visual family
: The visual family, which defines how events are displayed, might not have a rule to link the floating entity type to an existing entity type within the event. For example, a User entity might be defined, but there's no rule specifying that it should be connected to a File entity in a "File Access" event.
Incomplete Event Data
: The event data itself may be missing the information needed to create a link. For example, an event for a network connection might lack a destination IP address, preventing it from being connected to a Host entity.
Isolated Entities
: An entity might be created but never referenced by any other event, making it "isolated". For example, a new user account is created but hasn't performed any actions yet that would generate events to link to it.
To address floating entities, you can do the following actions:
Review the Visual Family
: Check if the visual family has the necessary rules to connect the entity types. If not, you may need to create a new rule to establish the relationship.
Inspect the raw event data
: Examine the raw data of the event to see if the required fields for mapping (for example, source IP, destination port, user ID) are present.
Adjust the field mapping
: If the data exists but isn't being mapped correctly, adjust the field mapping to ensure the right event fields are populating the entity properties.
Learn more about how to
create entities (mapping and modeling)
and
configure mapping and assign visual families
.
Need more help?
Get answers from Community members and Google SecOps professionals.
