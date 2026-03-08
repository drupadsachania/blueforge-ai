# Ingest data using SOAR connectors

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors/  
**Scraped:** 2026-03-05T10:03:19.698402Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Ingest data using SOAR connectors
Supported in:
Google secops
SOAR
The Google Security Operations platform functionality uses connectors
  to ingest alerts from a variety of data sources into the platform. A connector
  is an item in an integration package that you can download from
   the Content Hub. You configure connectors from
SOAR Settings
>
Ingestion
>
Connectors
.
Connectors are Python-based applications that pull
  alerts from third-party products into Google SecOps. Connectors also
  parse and normalize the raw data (alerts and events) into a Google SecOps
  format, which is then presented as a case in the case queue.
If you're running a third-party SIEM (a central place for all your alerts),
  one connector is sufficient. You can also pull data from multiple
  sources with several connectors. Each connector has a dedicated
  documentation link for additional help.
Use case: Set up an email connector
Go to
Content Hub
>
Integrations
.
Search for and install email integration.
Select
settings
Configure default instance
to open the
Email - Configure Instance
dialog.
Complete all required parameters.
Optional:  Go to
SOAR Settings
>
Response
>
Integrations Setup
to configure the integration to a different, relevant
    instance (not the default environment).
Go to
SOAR Settings
>
Ingestion
>
Connectors
.
Click
add
Create New Connector
.
Select the IMAP Email connector and click
Create
.
Complete the required fields. When prompted, click
Save
, and then click
Yes
.
Enable the connector and save it again. This makes it run periodically
    to pull any new emails according to the configuration.
Need more help?
Get answers from Community members and Google SecOps professionals.
