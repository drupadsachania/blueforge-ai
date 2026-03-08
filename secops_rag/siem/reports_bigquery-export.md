# Stream data with Advanced BigQuery Export

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export/  
**Scraped:** 2026-03-05T09:36:45.773533Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Stream data with Advanced BigQuery Export
Supported in:
Google secops
This document describes how to access and use your Google SecOps data in BigQuery with the
Advanced BigQuery Export
feature. As an Enterprise Plus customer, you can use the feature to access your security data in near real-time through a fully managed, streaming data pipeline. This capability can help address the critical challenge of data latency in security operations, and lead to more timely and effective threat detection and response.
Before you begin
We recommend that you review the following points that define eligibility requirements and necessary actions:
Enterprise Plus customers only
: This feature is available for Google SecOps Enterprise Plus customers only. For all other customers, see
Configure data export to BigQuery in a self-managed Google Cloud project
.
Feature activation required
: This feature is enabled on request and may require initial configuration in your organization's Google SecOps instance. Contact your Google SecOps representative to confirm feature enablement, if necessary.
Migration alert
: When you activate this feature, it overrides the older method, which is described in
Google SecOps data in BigQuery
. During the migration to Advanced BigQuery Export, we'll keep your older pipeline active for a transitional period. This dual operation is designed to support your move to the new feature without disruption. You'll be notified before the old export pipeline is disabled for your account.
Feature overview
Advanced BigQuery Export automatically provisions and manages essential Google SecOps datasets—including
Unified Data Model (UDM) events
, rule detections, and Indicator of Compromise (IoC) matches—in a secure, Google-managed BigQuery project. You gain secure, read-only access to this data through a BigQuery linked dataset, which appears directly in your own Google Cloud project. This functionality lets you query your security data as if it were stored locally, but without the overhead of managing the data pipeline or storage.
Google SecOps exports the following categories of security data to BigQuery:
UDM event records
: UDM records created from log data ingested by customers. These records are enriched with aliasing information.
Rule matches (detections)
: Instances where a rule matches one or more events.
IoC matches
: Artifacts (for example, domains or IP addresses) from events that match IoC feeds. This includes matches to and from global feeds and customer-specific feeds.
Ingestion metrics
: Statistics, such as the number of log lines ingested, the number of events produced from logs, and the number of log errors indicating that logs couldn't be parsed.
Entity graph and entity relationships
: The description of entities and their relationships with other entities.
Key benefits
The core benefits of Advanced BigQuery Export include:
Near real-time data freshness
: A streaming architecture makes your security data available for querying within minutes of ingestion. UDM events, rule detections, and IoC matches are available with an expected latency of 5-10 minutes.
Simplified and predictable cost model
: Google SecOps covers all data ingestion and storage costs within the managed BigQuery project. Your organization is responsible only for the BigQuery analysis costs incurred when you run queries.
Zero-maintenance data access
: The underlying infrastructure is fully managed by Google, which lets your team focus on data analysis rather than data engineering.
Typical use cases
Advanced BigQuery Export is designed for security analysts, threat hunters, data scientists, and security engineers who require direct, high-performance access to fresh security data for ad hoc investigations, custom analytics, and integration with business intelligence tools.
Typical use cases for Advanced BigQuery Export include the following:
Run ad hoc queries directly in BigQuery.
Use your own business intelligence tools, such as Microsoft Power BI, to create dashboards, reports, and analytics.
Join Google SecOps data with third-party datasets.
Architecture
The Advanced BigQuery Export architecture uses a continuous streaming pipeline. Data from your Google SecOps instance is pushed to a secure, Google-managed tenant project using the high-throughput BigQuery Storage Write API.
Google SecOps uses BigQuery sharing to create a secure
data listing
and provide you with access. In your BigQuery
Explorer
pane, your Google Cloud project is automatically subscribed to this listing, which is displayed as the
secops_linked_data
linked dataset
.
This model supports strong data isolation while giving you seamless, read-only query access.
Use Advanced BigQuery Export
This section describes how to access and use your Google SecOps data in BigQuery.
Key terms and concepts
The following are some key terms and concepts for Advanced BigQuery Export:
Linked dataset
: A read-only BigQuery dataset that serves as a symbolic link or pointer to a shared dataset in another project. It lets you query data without copying it, providing secure access while the data provider manages the physical storage.
BigQuery sharing
: The Google Cloud service that enables organizations to securely share data and analytics assets, such as BigQuery datasets, both internally and externally.
Tenant project
: A Google Cloud project that is owned and managed by Google SecOps. This project is where your exported security data is physically stored and managed. You don't have direct access to this project.
Your project
: The Google Cloud project that your organization owns and links to your Google SecOps instance. This is the project where the linked dataset appears and where you run your queries and incur analysis costs.
Project ID
: The globally unique identifier for your project.
Unified Data Model (UDM)
: Google's extensible, standard schema for parsing and normalizing security telemetry data from hundreds of vendor products into a consistent format.
Set up your system
Follow these steps to set up your system to use Advanced BigQuery Export and begin querying your data:
Confirm your license
: Make sure that your organization has a Google SecOps Enterprise Plus license.
Identify your project
: Sign in to the Google Cloud console and select the Google Cloud project that is linked to your Google SecOps instance.
Locate the linked dataset
: In the BigQuery console, use the
Explorer
pane to navigate to your project's resources. You'll see a linked dataset named
secops_linked_data
. This dataset is a read-only pointer to the live security data managed by Google SecOps.
Verify Identity and Access Management (IAM) permissions
: To query the data, your user or service account must have the following IAM roles granted on your project:
roles/bigquery.dataViewer
roles/bigquery.jobUser
These roles allow users (such as security analysts and data consumers) to query data in the linked dataset and run BigQuery jobs within their project.
Run a test query
: Open the BigQuery SQL workspace and run a basic query to verify that your access is configured correctly. You can use the following code snippet (replacing
PROJECT_ID
with your actual Google Cloud Project ID):
SELECT
*
FROM
`
PROJECT_ID
.
secops_linked_data
.
events
`
LIMIT
10
;
Query your BigQuery data
You can run queries directly in BigQuery or connect your own business intelligence tool, such as Microsoft Power BI, to BigQuery.
See the following for more information about queries:
For information about accessing and running queries in BigQuery, open
Run a query
and learn how to
run an interactive query
and
run a batch query
.
For information about how to query partitioned tables, see
Query partitioned tables
.
Data retention period in BigQuery
The retention period for your data in BigQuery is identical to the data retention period configured for your Google SecOps tenant. There is no separate, configurable setting to customize your retention policy for data in BigQuery. Data is automatically purged from the BigQuery tables as it ages past your tenant's retention window.
Linked datasets
The linked datasets contain several tables, each corresponding to a different type of security data.
The following table provides a summary of the available datasets, their target data freshness, and the primary keys used for ensuring data integrity:
Dataset name
Description
Best expected freshness
Primary keys for deduplication
events
Normalized security events in the UDM schema.
For information about the schema, see
Google SecOps events schema
.
< 5 minutes
metadata.id
(String representation)
Sample queries
The following examples demonstrate how to query the datasets for common security use cases. Remember to replace
PROJECT_ID
with your actual Google Cloud Project ID.
Example—Find all network connections from a specific IP address in the last 24 hours
This query searches the
events
table for recent network activity from a suspicious IP address.
SELECT
  metadata.product_event_type,
  principal.ip,
  target.ip,
  network.application_protocol
FROM
  `
PROJECT_ID
.secops_linked_data.events`
WHERE
  principal.ip = '192.0.2.1'
  AND metadata.event_timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR);
Example—Count the top 10 most frequent rule detections
This query on the
rule_detections
table helps identify the most-common threats or policy violations that are detected in your environment.
SELECT
  rule_name,
  COUNT(*) AS detection_count
FROM
  `
PROJECT_ID
.secops_linked_data.rule_detections`
WHERE
  detection.id IS NOT NULL
GROUP BY
  1
ORDER BY
  2 DESC
LIMIT
  10;
Best practices
The following are some best practices for querying with Advanced BigQuery Export:
Optimize for cost:
Avoid
SELECT *
. In your query, specify only the columns you need to reduce the amount of data scanned and lower query costs.
Use partition filters:
The
events
table is partitioned by the
hour_time_bucket
column. Always include a
WHERE
clause filter on this column to limit queries to the smallest possible time window, which significantly improves performance and reduces cost.
Write efficient queries:
The UDM schema is wide and sparse. To efficiently filter for specific event types, use
WHERE...  IS NOT NULL
on relevant fields. For example, to find only DNS queries, filter
WHERE  network.dns.questions.name IS NOT NULL
.
Validate queries:
Use the query validator in the BigQuery UI before you run a query. The query validator provides an estimate of the data process, helping you avoid unexpectedly large and costly queries.
Known limitations
The following are known limitations of the Advanced BigQuery Export feature:
Entity-graph latency:
The
entity_graph
dataset is exported using a batch process and has a data freshness of approximately four hours.
Customer-Managed Encryption Keys (CMEK):
Advanced BigQuery Export is not available for customers who have enabled CMEK on their Google SecOps instance.
UDM schema columns:
BigQuery has a soft limit of 10,000 columns per table. The UDM schema contains over 27,000 fields and is sparsely populated. The export pipeline intelligently includes only
populated columns
for a given event, keeping most customers well under the limit. Google SecOps monitors column usage and proactively requests a limit increase for your tenant project if it approaches this threshold.
Retention policy:
The data-retention period for all security data exported to BigQuery is automatically synchronized with the data-retention period of your Google SecOps project, and isn't configurable separately.
Late-arriving data:
In rare circumstances, if data arrives significantly late to the processing pipeline, there's a small chance that the data might not be correctly merged. The system is designed to minimize this, but it's a known characteristic of high-throughput streaming systems that rely on eventual consistency.
Enriched data:
Coverage is limited to single-time enriched UDM events. Re-enriched UDM events aren't exported to your tenant project's BigQuery instance.
Historical data:
Data export begins from the moment that Advanced BigQuery Export is enabled, and older data remains accessible in your existing project. To query data exported prior to the activation of the Advanced BigQuery Export, you need either to
use a single query
that joins data across both projects, or
run two separate queries
on the respective projects (one for the older dataset and one for the new dataset).
Troubleshooting and support
The following table provides solutions for common problems that you may encounter:
Observed symptom
Possible cause
Recommended action
Queries fail with
Access Denied: User does not have permission.
The user or service account lacks the necessary BigQuery IAM roles on the Google Cloud project that is linked to your Google SecOps instance.
Grant the
BigQuery Data Viewer
and
BigQuery Job User
roles to the principal. Verify this using
gcloud projects get-iam-policy YOUR_PROJECT_ID --flatten="bindings.members" --format='table(bindings.role)' --filter="bindings.members:user:your-user@example.com"
The
secops_linked_data
dataset is not visible in my BigQuery project.
1. You are not in the correct Google Cloud project.
2. Your organization is not on the Enterprise Plus tier.
3. Your organization is on the Enterprise Plus tier, but Advanced BigQuery Export is not enabled in your Google SecOps instance.
1. In the Google Cloud console, verify you have selected the project linked to your Google SecOps instance.
2. Contact your Google representative to confirm your Google SecOps license tier.
3. Contact your Google SecOps representative and ask them to enable Advanced BigQuery Export in your Google SecOps instance.
Seeing what appear to be duplicate events in query results.
This may be due to late-arriving data in a high-throughput stream. The system uses
at-least-once
delivery semantics.
If you suspect duplicates, group your query by the primary keys listed in
Datasets
to get a  count.
Need more help?
Get answers from Community members and Google SecOps professionals.
