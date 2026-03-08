# Export to a self-managed BigQuery project

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project/  
**Scraped:** 2026-03-05T09:36:44.580090Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Export to a self-managed BigQuery project
Google Security Operations lets you export Unified Data Model (UDM) data to a self-managed project 
that you own and manage. You can link your own Google Cloud project to your 
Google SecOps instance and independently manage IAM 
permissions with no dependency on Google-managed settings. You can also enable and
configure the
Bring Your Own BigQuery
(BYOBQ) feature by selecting
SIEM Settings
>
Data Export
.
Google SecOps exports the following categories of data to your
BigQuery project:
udm_events
: log data normalized into the UDM schema.
udm_events_aggregates
: aggregated data that is summarized by each hour of normalized
events.
entity_graph
: There are three dimensions (contextual data, derived data, and global 
context) to the entity graph. All of contextual data and derived data,
as well as part of global context data is data written and stored as 
UDM.
rule_detections
: detections that are returned by rules run in Google SecOps.
ioc_matches
: IOC matches that are found against UDM events.
ingestion_metrics
: metrics related to the ingestion and normalization pipeline (exported by default).
udm_enum_value_to_name_mapping
: maps enum values to UDM field names (exported by default).
entity_enum_value_to_name_mapping
: maps enum values to entity field names (exported by default).
Retention period
If you're an existing customer, the retention period you set defines how long the
exported data for your BigQuery stays in your Google-managed project.
The retention period begins from the date of the earliest exported record. You can 
configure a separate retention period for each data source, up to a maximum that 
matches the default log retention period in Google SecOps.
If no retention period is specified, the default behavior is to keep exporting 
data without any cleanup or purging, to limit the retention period.
In this case, you can set the retention period to
Unlimited
:
Click
SIEM Settings
>
Data Export
.
In the
Retention Period
column of the
Data Export
table, select
Unlimited
from the list for the relevant data type.
You can then set up an
object lifecycle rule
in your Google Cloud storage bucket to delete objects as needed.
Data migration for existing customers
If you're an existing customer, your data from the existing Google-managed
project isn't migrated to the self-managed project. Because data isn't migrated, your data is
located in two separate projects. To query the data across a time range that
includes the self-managed project activation date, you need to complete one of
the following actions:
Use a single query that joins data across both projects.
Run two separate queries on the respective projects, one for data before
the self-managed project activation date and one for data after.
When the retention period for your Google-managed project expires, that data
is deleted. You can only query data that is within your Google Cloud
project after that point.
Permissions required to export data
To access your BigQuery data, run your queries within BigQuery
itself. Assign the following IAM roles to any user who needs access:
BigQuery Data Viewer
(
roles/bigquery.dataViewer
)
BigQuery Job User
(
roles/bigquery.jobUser
)
Storage Object Viewer
(
roles/storage.objectViewer
)
You can also assign roles at the dataset level. For more information, see
BigQuery IAM roles and permissions
.
Initiate BigQuery data export to your self-managed project
Create a Google Cloud project where you want your data to be exported.
For more information, see
Configure a Google Cloud project for Google SecOps
.
Link your self-managed project to your Google SecOps instance
to establish a connection between Google SecOps and your self-managed
project. For more information, see
Link Google Security Operations to Google Cloud services
.
You can also enable and configure the
Bring Your Own BigQuery
(BYOBQ) feature 
by selecting
SIEM Settings
>
Data Export
.
To validate that the data is exported to your self-managed project, check the
tables under the
datalake
dataset in BigQuery.
You can write ad-hoc queries against Google SecOps data stored
in BigQuery tables. You can also create more advanced analytics using 
other third-party tools that integrate with BigQuery.
All the resources created in the your self-managed Google Cloud project to enable
exports, including Cloud Storage bucket and BigQuery tables, are in the same
region as Google SecOps.
If you get an error like
Unrecognized name: <field_name> at [<some_number>:<some_number>]
when querying BigQuery, it means the field you're trying to access isn't
in your dataset and because your schema is dynamically generated
during the export process.
For more information about Google SecOps data in BigQuery,
see
Google SecOps data in BigQuery
.
Related API methods
Use the API methods described in the following topics to access export configurations
and manage how your data is sent to BigQuery:
BigQueryExport
REST Resource: projects.locations.instances.bigQueryExport
Need more help?
Get answers from Community members and Google SecOps professionals.
