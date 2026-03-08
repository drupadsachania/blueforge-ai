# Burst limits

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits/  
**Scraped:** 2026-03-05T09:47:30.258976Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Burst limits
This document describes the burst limits that apply to Google Security Operations resources, specifically the volume of data which can be ingested into Google SecOps by a single customer.
Burst limits restrict the use resources shared by all customers:
Upper limit on the amount of data ingestion which can be used by a single
customer. This ensures that a sudden influx of data from a single customer does
not impact others.
Monitors the use of shared resources for each customer.
Maintains configurations that automatically enforce the burst limits.
Provides a means to request or make changes to burst limits.
For surge protection, the burst limit is measured over periods of 5 minutes. It is not a daily ingestion limit.
Burst limit increase per customer
If you intend to rapidly increase your ingestion rate, we can help you pre-plan and ensure that your data ingestion remains stable. To request an increase in your burst limit, contact
Google SecOps Technical Support
in advance.
Burst limits overview
Data ingestion burst limits restrict the amount of data a customer can send to Google SecOps. These limits ensure fairness and prevent issues for other customers caused by ingestion spikes from a single customer. Burst limits ensure that customer data ingestion operates smoothly. You can adjust them using a support ticket. To apply burst limits, Google SecOps uses the following classifications based on ingestion volume:
Burst limit
Annual equivalent data at maximum per second burst limit
20 MBps
600 TB
88 MBps
2.8 PB
350 MBps
11 PB
886 MBps
28 PB
2.6 GBps
82 PB
The following guidelines apply to burst limits:
When your burst limit is reached, configure ingestion sources to
buffer
additional data. Don't configure them to drop data.
For pull-based ingestion, such as Google Cloud and API feeds, systems
automatically buffer ingestion and require no further configuration.
For push-based ingestion methods, such as forwarders, webhooks, and API
ingestion, configure the systems to automatically resend data when the
burst limit is reached. For systems like Bindplane and Cribl, set up
buffering to handle data overflow efficiently.
Before you reach your burst limit, you can increase it.
To determine if you are near your burst limit, see
View burst limit
usage
.
View burst limit usage
You can view your burst limit usage using Google SecOps or Cloud Monitoring.
Use Google SecOps dashboard to view your burst limits
To view the limit usage, use the following visualizations in the Google SecOps
Data Ingestion and Health
dashboard:
Burst Limit Graph - Ingestion Rate
: displays the ingestion rate.
Burst Limit Graph - Quota Limit
: displays the quota limit.
Burst Rejection Graph
: displays the volume of the logs that were rejected due to exceeding the burst limit.
To view the visualizations, do the following:
From the Google SecOps menu, select
Dashboards
.
From the
Default dashboards
section, select
Data Ingestion and Health
.
In the
Data Ingestion and Health
dashboard, you can view the visualizations.
Use Cloud Monitoring to view burst limits
To view Google SecOps burst limits in the Google Cloud console, you need
the same permissions as for any Google Cloud limit. For more information, see
Grant access to Cloud Monitoring
.
For information about how to view metrics using charts, see
Create charts with Metrics Explorer
.
To view your burst limit usage, use the following PromQL query:
100 * sum(rate(chronicle_googleapis_com:ingestion_log_bytes_count
{monitored_resource="chronicle.googleapis.com/Collector"}[10m]))/min(min_over_time(chronicle_googleapis_com:ingestion_quota_limit{monitored_resource="chronicle.googleapis.com/Collector"}[10m]))
To view the number of bytes that were rejected after exceeding
the burst limit, use the following PromQL query:
topk(5, sum by ("collector_id","log_type")(rate({"__name__"="chronicle.googleapis.com/ingestion/log/quota_rejected_bytes_count","monitored_resource"="chronicle.googleapis.com/Collector","quota_type"="SHORT_TERM_DATA_RATE"}[${__interval}])))
To
create an alert
when the ingested bytes
exceed 70% of the burst limit, use the following PromQL query:
100 * topk(5, sum by ("collector_id","log_type")(rate({"__name__"="chronicle.googleapis.com/ingestion/log/quota_rejected_bytes_count","monitored_resource"="chronicle.googleapis.com/Collector","quota_type"="SHORT_TERM_DATA_RATE"}[${__interval}]))) > 70
Buffer data at ingestion source
The following table describes the configuration needed to buffer (rather than drop) data from your enterprise depending on your ingestion source.
Ingestion source
Buffering configuration
Google Cloud and Chronicle API feeds
Buffering provided automatically
Forwarders
, webhooks, and API ingestion
Configure retries
Bindplane
,
Cribl
, and
Forwarders
Configure persistent queue
Troubleshooting
Strategies to avoid exceeding limits
The following guidelines help you avoid exceeding your burst limit:
Create an ingestion alert that notifies you when the volume of the bytes ingested exceeds
the burst limit threshold. For more information about setting up ingestion alerts,
see
Using Cloud Monitoring for ingestion notifications
.
To identify the ingestion sources and volume, create a monitoring alert with
collector_id
, and
log_type
along with the metric
chronicle.googleapis.com/ingestion/log/bytes_count
. To identify the ingestion sources and volume,
use the following PromQL query:
sum by (collector_id,log_type)(rate(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}[5m]))
If you expect your ingestion volume to increase more than four times your normal ingestion
volume, contact
Google SecOps Technical Support
ahead of time to increase your burst limit.
If you use a Google SecOps forwarder to ingest data, you can use
disk buffers
to buffer data when you exceed your burst limit. For more information, see
Using disk buffers for forwarders
.
Handle burst limit events
If you reach the burst limit, take the following actions for your ingestion method:
Ingestion mode
Suggested action
Ingestion API
Wait until you are back below your burst limit. If you want to resume ingestion sooner,
   contact
Google SecOps Technical Support
.
Feed management
Wait until you are back below your burst limit. If you want to resume ingestion sooner,
   contact
Google SecOps Technical Support
.
Forwarder
Use
disk buffers
to buffer data when you are exceed your burst limit.
HTTPS push ingestion that uses Amazon Data Kinesis, Pub/Sub, or webhooks.
Ensure that the retention time is set to the maximum possible value.
   For example, to set the retention time for Pub/Sub, see
Configure subscription message retention
Using disk buffers for forwarders
If you use Google SecOps SIEM forwarder, we recommend that you start
using
disk buffers
to buffer data when you exceed your burst limit. The maximum RAM size used by the collector is 4 GB.
You can set this limit using the
max_file_buffer_bytes
setting in the collector
configuration. To buffer data that is more than 4 GB, use disk buffers. To decide the disk buffer size,
identify the rate at which forwarders are ingesting by using the following MQL query:
sum(rate(chronicle_googleapis_com:ingestion_log_bytes_count
{monitored_resource="chronicle.googleapis.com/Collector", collector_id!~ "
(aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb
|cccccccc-cccc-cccc-cccc-cccccccccccc
|dddddddd-dddd-dddd-dddd-dddddddddddd
|aaaa2222-aaaa-2222-aaaa-2222aaaa2222)"}[5m]))
For example, if the rate of ingestion from the forwarder is 415 Kbps and the buffer
compression efficiency is 70%, then the buffer fill-up rate is calculated as
415 Kbps x (100% - 70%) = 124.5 Kbps. At this rate, a buffer size of 1 GB, which is
the default in-memory buffer value, fills up in 2 hours and 20 minutes. The calculation is
1024 x 1024 / 124.5 = 8422.297 seconds = 2 hours and 20 minutes. If you have exceeded your burst limit,
you need a 100 GB disk to buffer data for a day.
Frequently asked questions
What error is triggered when you exceed the burst limit?
When you exceed the burst limit, you get the HTTP 429 error.
How do you resolve the HTTP 429 error?
Retry the request after five minutes.
How often are burst limits refreshed?
Burst limits are refreshed after every five minutes.
