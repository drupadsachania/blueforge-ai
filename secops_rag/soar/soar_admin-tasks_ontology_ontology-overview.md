# Ontology overview

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview/  
**Scraped:** 2026-03-05T10:03:26.625256Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Ontology overview
Supported in:
Google secops
SOAR
The Google Security Operations ontology uses a formal specification that provides a
  shareable and reusable knowledgeable representation of alerts and events. The ontology lets Google SecOps build entities from events and define relationships
  between them. This process lets you see the full picture and  explore potential threats on the
Explore
page. Once entities have been defined using the ontology, you can run
  actions on them based on their role in the attack or event.
View the Ontology status
Go to
Settings
>
Ontology {and_then} Ontology Status
to see the
following information:
Number of product types
: The number of products that Google SecOps captures from your environment. This number changes as more products are added to your environments.
Number of event types
: The number of events that Google SecOps captures.
Number of events assigned to default families
: The number of events that Google SecOps has automatically assigned. You can reassign an event (at any time) by locating the default value in the
Family Name
column and click
settings
Configure
.
You can export selected ontology status rows as a ZIP file containing a JSON file. You can also import ontology status rows. Be sure to import a ZIP file that contains a JSON file with the ontology details.
Set up model families
After you've established an initial data connection, you'll need to do the following:
Complete the following procedures to ensure that the data is ingested into the
  Google SecOps data model.
Map and model new events and alerts according to your requirements.
To set up a model family, follow these high-level steps:
Define the family: click
Settings
>
Ontology
>
Visual Families
.
Assign the family to the Event (or Product/Source) from either
  the
Alerts events
tab or the
Ontology status
page, click
Event Configuration
>
Visualization
.
Map data fields
To map data fields, follow these high-level steps:
On the
Case Management
or
Explore
page, correct any missing or
  incorrect field information.
Check if this can be solved by attaching a new Visual Family; otherwise, edit and
  configure the rules that make up both the family and the general system fields
  on the
Event Configuration
>
Mapping page.
Need more help?
Get answers from Community members and Google SecOps professionals.
