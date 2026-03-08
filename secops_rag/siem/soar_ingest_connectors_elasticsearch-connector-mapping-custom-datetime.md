# Map date and time fields for Elasticsearch

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/elasticsearch-connector-mapping-custom-datetime/  
**Scraped:** 2026-03-05T09:31:01.281130Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Map date and time fields for Elasticsearch
Supported in:
Google secops
SOAR
After you and configure an integration, you must map its fields to
  Google Security Operations fields to accurately display the information on the
  platform. More specifically, this document explains how to map a custom date
  and time for the Elasticsearch connector.
When you configure the
Elasticsearch
connector, you must
convert
or map the custom date and time fields, such as
\_source\_@timestamps
, to
startTime
and
endTime
of Google SecOps cases.
Go to
SOAR Settings
>
Ontology
>
Ontology
  Status
.
Click
settings
Configure
in the same row as the Elasticsearch connector.
On the
Event Configuration
page, select
Mapping
.
Under
System Fields
, select the
StartTime
row and choose
Edit Field
from the menu.
In the
Map Target Field: StartTime
dialog, set the following fields:
Extracted
: Select
\_source\_@timestamp
, which is
        from the ELK stack.
Transformation Function
: Select
FROM_CUSTOM_DATETIME
.
Enter Parameters
: Enter
YYYY-MM-DDTHH:MM:SS:zzzZ
.
In the
Map Target Field: EndTime
dialog, set the following fields:
Extracted Field
: Select
\_source\_@timestamp
, which is
        from the ELK stack.
Transformation Function
: Select
FROM_CUSTOM_DATETIME
.
Enter Parameters
: Enter
YYYY-MM-DDTHH:MM:SS:zzzZ
to generalize the time
        format.
Click
Save
.
The Elasticsearch timestamp fields are now converted to the standardized time
  and date fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
