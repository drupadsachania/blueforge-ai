# Create entities (mapping and modeling)

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling/  
**Scraped:** 2026-03-05T10:03:28.017244Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create entities (mapping and modeling)
Supported in:
Google secops
SOAR
Entities are objects that represent points of interest extracted from alerts, such as Indicators of Compromise (IoCs) and artifacts. They help security analysts by:
Automatically tracking history.
Grouping alerts without human intervention.
Hunting for malicious activity based on relationships between entities.
Making cases easier to read and enabling seamless playbook creation.
Google Security Operations uses an automated system (ontology) to extract the main objects
  of interest from the raw alerts to create entities. Each entity is
  represented by an object that can track its own history for future reference.
Configure the entity ontology
To configure the ontology, you'll need to map and model your data. This
  involves selecting a visual representation for alerts and defining which
  entities should be extracted. Google SecOps provides pre-configured
  ontology rules for most popular SIEM products.
The best time to customize the ontology is after you have a connector pulling
  data into Google SecOps. The process involves two main steps:
Modeling
: Choose the visual representation (model/visual family) for your data.
Mapping
: Map the fields to support the selected model and extract entities.
Supported entities
The following entities are supported:
Address
Application
Cluster
Container
Credit Card
CVE
Database
Deployment
Destination URL
Domain
Email Subject
File Hash
Filename
Generic Entity
Hostname
IP Set
MAC Address
Phone Number
POD
Process
Service
Threat Actor
Threat Campaign
Threat Signature
USB
User Name
Use case: Map and model new data of ingested email
This use case shows how to map and model new data of an ingested email:
Go to
Content Hub
>
Use Cases
.
Run the
Zero to Hero
test case. For details on how to do this, see
Run use cases
.
In the
Cases
tab, select the
Mail
case from the
Cases Queue
and
    select the
Events
tab.
Next to the alert, click
settings
Event Configuration
to open the
Event Configuration
page.
In the hierarchy list, click
Mail
. This
    ensures that your configuration will automatically work for every piece of
    data coming from this product (Email box).
Assign the visual family that best represents the data. In this use case, because
MailRelayOrTAP
has previously been selected, you can skip this step.
Switch to
Mapping
and map the following entity fields. Double-click each entity and select the raw data field for that entity in the extracted field. You can provide
    alternative fields from which to extract the information:
SourceUserName
DestinationUserName
DestinationURL
EmailSubject
Click
Raw Event Properties
to view the original email fields.
Extract regular expressions
Google SecOps doesn't support regular expression groups. To extract
text from the event field using regular expression patterns, use
lookahead
and
lookbehind
in the extraction function logic.
In the following example, the event field displays a large chunk of text:
Suspicious activity on A16_WWJ - Potential Account Takeover (33120)
To extract only the text
Suspicious activity on A16_WWJ
, do the
following:
Enter the following regular expression in the
Extraction function
value field:
Suspicious activity on A16_WWJ(?=.*)
In the
Transformation function
field, select
To_String
.
To extract only the text after
Suspicious activity on A16_WWJ
,
do the following:
Enter the following regular expression in the
Extraction function
value field:
(?<=Suspicious activity on A16_WWJ).*
In the
Transformation function
field, select
To_String
.
Need more help?
Get answers from Community members and Google SecOps professionals.
