# Use the Health Hub

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard/  
**Scraped:** 2026-03-05T10:03:13.177502Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the Health Hub
Supported in:
Google secops
SIEM
This document describes the
Health Hub
, which is the central location in Google Security Operations for you to monitor the status and health of all configured data sources. The
Health Hub
provides critical information on failed sources and log types, offering the context needed to diagnose and remediate data pipeline issues.
The
Health Hub
includes information about the following:
Ingestion volumes and ingestion health.
Parsing volumes from raw logs to
Unified Data Model (UDM) events
.
Context and links to interfaces with additional relevant information and functionality.
Failed sources and log types. The
Health Hub
detects failures on a per-customer basis.
Key benefits
You can use the
Health Hub
to do the following:
Monitor overall data health at a glance. View the core health status and associated metrics for each feed, data source, log type, and source (that is, the feed ID).
Monitor aggregated data-health metrics for ingestion and parsing over time with highlighted events that link to filtered dashboards.
Access related dashboards, filtered by timeframe, log type, or feed.
Access the feed configuration to edit and fix or remediate a problem.
Access the parser configuration to edit and fix or remediate a problem.
Click the
Set Up Alerts
link to open the
Cloud Monitoring
interface, and from there, configure custom API-based alerts using
Status
and log-volume metrics.
Key questions
This section refers to
Health Hub
components and parameters, which are described in the
Interface
section.
You can use the
Health Hub
to answer the following questions about your data pipeline:
What were the last runs of my feed or last errors from my parser?
The
Health Hub
has a deep-dive dashboard that shows the last 200 feed runs and last 200 parser errors for the specific row you click into.
Are my logs reaching Google SecOps?
You can verify whether logs are reaching Google SecOps by using the
Last Ingested
and
Last Normalized
metrics. These metrics confirm the last time data was successfully delivered. Additionally, the ingestion-volume metrics (per source and per log type) show you the amount of data being ingested.
Are my logs being parsed correctly?
To confirm correct parsing, view the
Last Normalized
metric. This metric indicates when the last successful transformation from raw log into a
UDM event
occurred.
Why is ingestion or parsing not happening?
The text in the
Latest Issue Details
column identifies specific problems, which helps you pinpoint whether the action is
actionable
(you fix it) or
non-actionable
(requires support). The text
Forbidden 403: Permission denied
is an example of an actionable error, where the auth account provided in the feed configuration lacks required permissions. The text
Internal_error
is an example of a non-actionable error, where the recommended action is to open a support case with Google SecOps.
Are there significant changes in the number of ingested logs and parsed logs?
The
Status
field shows your data's health (
Healthy
or
Failed
), based on data volume. You can also identify sudden or sustained surges or drops by viewing the
Total Ingested Logs
graph.
How can I get alerted if my sources are failing?
The
Health Hub
feeds the
Status
and log-volume metrics into Cloud Monitoring. In one of the
Health Hub
tables, click the relevant
Alerts
link to open the
Cloud Monitoring
interface. There, you can configure custom API-based alerts using
Status
and log-volume metrics.
How do I infer a delay in a log-type ingestion?
A delay is indicated when the
Last Event Time
is significantly behind the
Last Ingested
timestamp. The
Health Hub
exposes the 95
th
percentile of the
Last Ingested
–
Last Event Time
delta—per log type. A high value suggests a latency problem within the Google SecOps pipeline, whereas a normal value might indicate that the source is pushing old data.
Have any recent changes in my configuration caused feed failures?
If the
Config Last Updated
timestamp is close to the
Last Ingested
timestamp, it suggests that a recent configuration update may be the cause of a failure. This correlation helps in root-cause analysis.
How has the health of ingestion and parsing been trending over time?
The
Data Source Health Overview
,
Parsing Health Overview
, and
Total Ingested Logs
graphs show the historical trend of your data's health, letting you observe long-term patterns.
Interface
To open the
Health Hub
, in the side navigation menu, click
Health Hub
.
The
Health Hub
is a read-only
default dashboard
and can't be modified directly. To customize, create a copy of the
Health Hub
, and then modify the duplicated dashboard for your specific use case.
The
Health Hub
displays the following widgets:
Big number widgets:
Healthy Sources
: The number of data sources performing with no failures.
Failed Sources
: The number of data sources that need immediate attention.
Healthy Parsers
: The number of parsers performing with no failures.
Failed Parsers
: The number of parsers that need immediate attention.
Data Source Health Overview
: A line graph showing the
Healthy
and
Critical
data-sources-per-day curves over time.
Parsing Health Overview
: A line graph showing the
Healthy
and
Critical
parsers-per-day curves over time.
Total Ingested Logs
: A line graph showing the
Ingested Logs
logs-per-day curve over time.
Failing Parser by Log Type
: A line graph showing a curve for each parser with a critical health status, per day over time. In this context, the
critical
health status is due to a very low parsing-success rate.
Health Status by Data Source
table—includes the following columns:
Status
: The cumulative status of the feed (
Healthy
or
Failed
), derived from data volume, configuration errors, and API errors.
Source Type
: The source type (ingestion mechanism)—for example,
Ingestion API
,
Feeds
,
Native Workspace Ingestion
, or
Azure Event Hub Feeds
.
Name
: The feed name.
Log Type
: The log type—for example,
CS_EDR
,
UDM
,
GCP_CLOUDAUDIT
, or
WINEVTLOG
.
Latest Issue Details
: The details about the latest issue in the specified timeframe—for example,
Failed parsing logs
,
Config credential issue
, or
Normalization issue
. The stated issue can be actionable (for example,
Incorrect Auth
) or non-actionable (for example,
Internal_error
). If the issue is non-actionable, the recommended action is to open a support case with Google SecOps. When there has been no issue in the specified timeframe, the value is empty or displays
OK
.
Issue Duration
: The number of days that the data source has been in a failed state. When the
Status
is
Healthy
, the value is empty or displays
N/A
.
Last Collected
: The timestamp of the last data collection.
Last Ingested
: The timestamp of the last successful ingestion. Use this metric to identify whether your logs are reaching Google SecOps.
Config Last Updated
: The timestamp of the last change to the metric. Use this value to correlate configuration updates with observed failures, helping you determine the root cause of ingestion problems or parsing problems.
View Ingestion Details
: A link that opens a new tab with another dashboard, which contains additional, historical information—for deeper analysis.
Edit Data Source
: A link that opens a new tab with the corresponding
feed configuration
—where you can fix configuration-related failures.
Set Up Alerts
: A link, which opens a new tab with the corresponding
Cloud Monitoring
interface.
Health Status by Parser
table—includes the following columns:
Status
: The cumulative status of the log type (
Healthy
or
Failed
).
Failure Parsing Rate
: The percentage of logs of the corresponding type that weren't parsed.
Log Type
: The log type—for example,
DNS
,
USER
,
GENERIC
,
AZURE_AD
,
BIND_DNS
,
GCP SECURITYCENTER THREAT
, or
WEBPROXY
.
Latest Issue Details
: The details about the latest parsing problem in the specified timeframe—for example,
Failed parsing logs
,
Config credential issue
, or
Normalization issue
. The stated issue can be actionable (for example,
Incorrect Auth
) or non-actionable (for example,
Internal_error
). If the issue is non-actionable, the recommended action is to open a support case with Google SecOps. When there has been no issue in the specified timeframe, the value is empty or displays
OK
.
Issue Duration
: The number of days that the data source has been in a failed state. When the
Status
is
Healthy
, the value is empty.
Last Ingested
: The timestamp of the last successful ingestion. You can use this metric to determine whether logs are reaching Google SecOps.
Last Event Time
: The event timestamp of the last normalized log.
Last Normalized
: The timestamp of the last parsing and normalization action for the log type. You can use this metric to determine whether raw logs are successfully transformed into
UDM events
.
Config Last Updated
: The timestamp of the last change to the metric. Use this value to correlate configuration updates with observed failures, helping you determine the root cause of ingestion problems or parsing problems.
View Parsing Details
: A link, which opens a new tab with another dashboard, which contains additional, historical information—for deeper analysis.
Edit Parser
: A link, which opens a new tab with the corresponding
parser configuration
—where you can fix configuration-related failures.
Set Up Alert
: A link, which opens a new tab with the corresponding
Cloud Monitoring
interface.
Irregularity-detection engine
The
Health Hub
uses the Google SecOps irregularity-detection engine to automatically identify significant changes in your data, letting you quickly detect and address potential problems.
Data ingestion irregularity-detection
Google SecOps analyzes daily volume changes, while considering normal weekly patterns.
The irregularity-detection engine uses the following calculations to detect unusual surges or drops in your data ingestion:
Daily and weekly comparisons
: Google SecOps calculates the difference in ingestion volume between the current day and the previous day, and also the difference between the current day and the average volume over the past week.
Standardization
: To understand the significance of these changes, Google SecOps standardizes them using the following z-score formula:
z = (x
i
− x_bar) / stdev
where
z
is the standardized score (or z-score) for an individual difference
x
i
is an individual difference value
x_bar
is the mean of the differences
stdev
is the standard deviation of the differences
Irregularity flagging
: Google SecOps flags an irregularity if both the daily and weekly standardized changes are statistically significant. Specifically, Google SecOps searches for:
Drops
: Both the daily and weekly standardized differences are less than -1.645.
Surges
: Both the daily and weekly standardized differences are greater than 1.645.
Normalization ratio
When calculating the ratio of ingested events to normalized events, the irregularity-detection engine uses a combined approach to ensure that only significant drops in normalization rates are flagged. The irregularity-detection engine generates an alert only when the following two conditions are met:
There is a statistically significant drop in the normalization ratio compared to the previous day.
The drop is also significant in absolute terms, with a magnitude of 0.05 or greater.
Parsing error irregularity detection
For errors that occur during data parsing, the irregularity-detection engine uses a ratio-based method. The irregularity-detection engine triggers an alert if the proportion of parser errors relative to the total number of ingested events increases by 5 percentage points or more compared to the previous day.
What's next
Learn more about dashboards
Learn how to create a custom dashboard
Use Cloud Monitoring for ingestion notifications
Need more help?
Get answers from Community members and Google SecOps professionals.
