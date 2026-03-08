# View your billed ingestion volume

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/view-billed-ingestion-volume/  
**Scraped:** 2026-03-05T10:03:18.453571Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
View your billed ingestion volume
Supported in:
Google secops
SIEM
Google Security Operations billing is calculated based on the volume of raw log data 
ingested into the platform. This document outlines how to utilize specific ingestion metrics that align with the billing system to ensure accurate cost management and forecasting.
The following principles define how ingestion volume is calculated for billing purposes:
Billable volume
: Billing calculations are based exclusively on raw log data bytes. Metadata, internal labels, and enrichment tags associated with the logs are excluded from the billable total.
Authoritative data source
: The ingestion metrics provided within the billing system serve as the sole authoritative source for financial reporting. External metrics or internal dashboards outside of the specific billing module must not be used for budget reconciliation or cost auditing.
View ingestion volume
The ingestion volume data for billing purposes is accessible in three primary locations.
Each source uses the same underlying ingestion metrics data to maintain data consistency and alignment with financial statements.
Method 1: Main dashboard
The main dashboard provides a high-level visualization of ingestion trends over time. This view facilitates the monitoring of daily volume spikes and the identification of long-term ingestion patterns.
Sign in to
Google SecOps
.
Click
Dashboards & Reports
>
Dashboards
.
Use the
Search
tab to find and select the
Main
dashboard.
Go to the
Throughput
widget to monitor data ingestion rates. You can use the time range selector to calculate the total throughput over specific intervals.
Method 2: Data Health and Ingestion dashboard
The
Data Health and Ingestion
dashboard gives a granular view of ingestion telemetry, categorized by
log type
and
source
. This dashboard facilitates the auditing of ingestion volumes at a
per-log-source level
, which aids in identifying specific contributors to the total billable volume.
Sign in to
Google SecOps
.
Click
Dashboards & Reports
>
Dashboards
.
Use the
Search
tab to find and select the
Data Ingestion and Health
dashboard.
Go to the
Throughput
widget to analyze data ingestion rates. You can use the time range selector to calculate the total throughput over specific intervals.
Method 3: Cloud Monitoring
The Cloud Monitoring method is available to customers who use a Bring Your Own Project
(BYOP) setup. This approach permits the use of external monitoring tools to query ingestion telemetry directly from the underlying project infrastructure.
Go to the Google Cloud console and in the search bar, enter
Metrics Explorer
. Alternatively, click
menu
Menu
, select
Monitoring
>
Metrics explorer
.
Select your Cloud Monitoring profile.
On the
Profile
page's search bar, enter
Integrations
.
Select
Metrics explorer
.
Click
promQL
to switch to promQL query mode.
View the results in a table format: Find
Results
and then select
Table
.
View the ingestion volume (
ingestion_log_byte_count
): Copy and paste the following ingestion metric query into the query editor, and then run the query:
sum (increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}[1h]))
Optional: Filter a specific log type and include it in the query. For
example, to view ingestion for the log type
GCP_CLOUDAUDIT
, run the following
query:
sum(increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector",log_type="GCP_CLOUDAUDIT"}[1h]))
Create alerts on the amount of data ingested
When you create alerts for ingestion volume, it helps manage costs and supports a quick response to unexpected spikes.
Cloud Monitoring handles the alerting workflow. For configuration steps, see
Set up ingestion notification for health metrics
.
Monitor ingestion metrics across managed tenants
Cloud Monitoring scopes give you a centralized visibility into ingestion volumes across managed projects (tenants).
Metric scopes let you monitor data from multiple managed Google Cloud tenants
within a single console. The functionality requires the following configuration:
Managed tenants must provide the necessary permissions to the central Cloud Monitoring project.
The primary account must be configured as a
scoping project
.
With this configuration, the centralized view facilitates monitoring the total ingestion volume (
log_byte_count
) across the entire environment.
For more information, see
Metrics scopes overview
. To set up this view, see
Configure a metrics scope
.
Need more help?
Get answers from Community members and Google SecOps professionals.
