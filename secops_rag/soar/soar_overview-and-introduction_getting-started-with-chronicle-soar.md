# Get started with Google Security Operations SOAR

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/getting-started-with-chronicle-soar/  
**Scraped:** 2026-03-05T10:10:40.487501Z

---

Home
Documentation
Security
Google Security Operations
Stay organized with collections
Save and categorize content based on your preferences.
Get started with Google Security Operations SOAR
Supported in:
SOAR
To begin working in the Google SecOps SOAR platform, you must
  first understand the core concepts, which form the foundation of our documentation.
Connectors
Connectors
are the data ingestion points for
alerts
into Google SecOps SOAR. Their primary goal is to translate
  raw security data from third-party tools into normalized Google SecOps SOAR data. The
  connector gets alerts (or equivalent data) from third party tools, which is then forwarded to the Data Processing layer.
Cases, alerts, and events
Case
: The top-level container, composed of one or more alerts ingested from various sources using the connectors.
Alert
: A security notification containing one or more security events.
Entities
: After ingestion, the platform analyzes these events, and their indicators (IOCs, destinations, artifacts) are extracted and translated into dynamic objects called entities.
Entities
are dynamic objects that represent extracted points of interest (Indicators of Compromise [IoC], user accounts, IP addresses) from an alert.
Entities are key because they enable:
Automatic history tracking.
Grouping of related alerts without manual intervention.
Hunting for malicious activity based on relationships.
Entity creation (mapping and modeling)
In order to visually illustrate the entities and their connection in the
  platform, there is a configuration process of the ontology that involves
  mapping and modeling. During this process, you select the visual
  representation of alerts and the entities that should be extracted from it.
Google SecOps SOAR provides basic ontology rules for most popular SIEM products
  out-of-the-box. For details, see
Ontology overview
.
Create entities in Google SecOps SOAR
The process of mapping and modeling defines how entities are created and visually connected within a case (ontology). This process occurs once when a new alert type is first ingested:
It defines the visual representation of alerts and which entities should be extracted.
It sets entity properties, such as whether an entity is internal or external (based on configuration) or malicious (based on playbook results).
Google SecOps SOAR provides basic ontology rules out-of-the-box for most popular SIEM products.
For details about mapping and modeling, see
Create entities (mapping and modeling)
.
Using
mapping and modeling
, you can define the properties of an entity,
  such as whether it's internal or external, or if it's considered
malicious
.
  An entity's
internal
or
external
status is determined by the
  platform's settings. Its malicious status is decided by the product running
  within the playbook. The purpose of mapping and modeling is to specify key
  details like the data's
source
,
timestamp
, and
type
.
The mapping and modeling occurs once when data is first ingested. After that,
  the system applies the relevant rules to every new, incoming case.
Playbooks
A
Playbook
is an automation process that can be triggered by a predefined
  condition. For example, you can trigger a playbook for each alert that contains
  the product name "Mail": When triggered, the playbook attaches to each alert ingested into Google SecOps SOAR from this product.
It also executes a series of actions based on a defined tree of conditions (flows):
Actions are configured to run manually or automatically on the scope of the alert's entities.
Actions run in a defined order until a final resolution is reached for the triggering alert.
For example, you can configure the
VirusTotal - Scan URL
action to run automatically only on a specific entity type, such as URL entities.
Environments
Environments
are logical containers used to achieve data segregation.
Administrators can define different environments and assign platform users to one or more of them.
Users can only see cases and related information from the environments to which they are assigned.
Some user roles have access to
all environments
, granting them full access to all current and future data within the platform.
Need more help?
Get answers from Community members and Google SecOps professionals.
