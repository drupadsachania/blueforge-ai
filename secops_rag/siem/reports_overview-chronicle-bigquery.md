# Export to a Google-managed BigQuery project

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery/  
**Scraped:** 2026-03-05T09:36:48.192874Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Export to a Google-managed BigQuery project
Supported in:
Google secops
SIEM
Google SecOps provides a managed data lake of normalized and threat intelligence enriched
telemetry by exporting data to BigQuery. This lets you do the
following:
Run ad-hoc queries directly in BigQuery.
Use your own business intelligence tools, such as Looker or Microsoft
Power BI, to create dashboards, reports, and analytics.
Join Google SecOps data with third-party datasets.
Run analytics using data science or machine learning tools.
Run reports using predefined default dashboards and custom dashboards.
Google SecOps exports the following categories of data to BigQuery:
UDM event records:
UDM records created from log data ingested by customers.
These records are enriched with aliasing information.
Rules matches (detections)
: instances where a rule matches one or
more events.
IoC matches
: artifacts (for example domains, IP addresses) from events that
match Indicator of Compromise (IoC) feeds. This includes matches to from global
feeds and customer-specific feeds.
Ingestion metrics:
include statistics, such as number of log lines
ingested, number of events produced from logs, number of log errors indicating
that logs couldn't be parsed, and the state of Google SecOps forwarders.
For more information, see
Ingestion metrics BigQuery schema
.
Entity graph and entity relationships
: stores the description of
entities and their relationships with other entities.
Overview of the tables
Google SecOps creates the
datalake
dataset in BigQuery and the following tables:
entity_enum_value_to_name_mapping
: for enumerated types in the
entity_graph
table, maps the numerical values to the string values.
entity_graph
: stores data about UDM entities.
events
: stores data about UDM events.
ingestion_metrics
:
stores statistics related to ingestion and normalization of data from specific
ingestion sources, such as Google SecOps forwarders, feeds, and Ingestion API.
ioc_matches
: stores IOC matches found against UDM events.
job_metadata
: an internal table used to track the export of data to
BigQuery.
rule_detections
: stores detections returned by rules run in Google SecOps.
rulesets
: stores information about Google SecOps curated detections,
including the category each rule set belongs to, whether it is enabled, and
the current alerting status.
udm_enum_value_to_name_mapping
: For enumerated types in the events
table, maps the numerical values to the string values.
udm_events_aggregates
: stores aggregated data summarized by hour of
normalized events.
Access data in BigQuery
You can run queries directly in BigQuery or connect your own business
intelligence tool, such as Looker or Microsoft Power BI, to BigQuery.
To enable access to the BigQuery instance, use the
Google SecOps BigQuery Access API
.
You can provide an email address for either a user or a group that you own. If you
configure access to a group, use the group to manage which team members can
access the BigQuery instance.
To connect Looker or another business intelligence tool to BigQuery, contact
your Google SecOps representative for service account credentials that enable you to
connect an application to the Google SecOps BigQuery dataset. The service
account will have IAM BigQuery Data Viewer role (
roles/bigquery.dataViewer
) and BigQuery Job Viewer role (
roles/bigquery.jobUser
).
Data retention
For Google SecOps Enterprise Plus customers using Google-managed BigQuery, the following
retention settings apply:
Legacy Google SecOps Enterprise Plus customers (on deprecation path):
ioc_matches
and
rule_detections
tables: no retention limit is set, due to
low volume.
entity_graph
,
udm_events_aggregates
, and other partitioned tables except
the
events
table: 180 days.
events
table (UDM events): data is retained according to your
Google SecOps contract, or the default of 366 days if not specified in the
contract.
New customers: retention duration is governed by the Google SecOps contract (consistent with the Advanced BigQuery Export feature).
Related API methods
To get self-service access to Google SecOps data in
BigQuery, use the API methods described in
Use the BigQuery Access API
.
What's next
Learn more about the following schemas:
events
ingestion_metrics
For information about accessing and running queries in BigQuery, see
Run interactive and batch query jobs
.
For information about how to query partitioned tables, see
Query partitioned tables
.
For information about how to connect Looker to BigQuery, see Looker
documentation about
connecting to BigQuery
.
Need more help?
Get answers from Community members and Google SecOps professionals.
