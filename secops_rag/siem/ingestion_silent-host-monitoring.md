# Silent-host monitoring

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/silent-host-monitoring/  
**Scraped:** 2026-03-05T09:30:55.602052Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Silent-host monitoring
Supported in:
Google secops
SIEM
This document explains the methods of how Google Security Operations
silent-host monitoring
(
SHM
) lets you identify hosts in your environment that have gone silent.
A
silent
host can signal potential collector stoppages.
Use Google Cloud Monitoring with ingestion labels for SHM
This method uses Google Cloud Monitoring to monitor log ingestion rates based on ingestion labels for SHM.
This section describes how to set up this method using
Bindplane
, which includes the following steps:
Configure Bindplane for SHM with Google Cloud Monitoring
Configure the Google Cloud Monitoring threshold for SHM
After you set up a logs pipeline that applies ingestion labels for SHM, you can set up Google Cloud Monitoring alerts per collector—for when the ingestion rate falls below a specified threshold. You can configure the alerts to go to a variety of places outside of Google SecOps and integrate the alerts into a workflow.
Benefits of this method:
Monitors ingestion time, not event time.
Leverages Cloud Monitoring's advanced alerting capabilities.
Downsides of this method:
Requires a separate configuration outside of Google SecOps.
Limited by the number of
ingestion labels
.
Configure Bindplane for SHM with Google Cloud Monitoring
The prerequisites to configure Bindplane for SHM with Google Cloud Monitoring are as follows:
A deployed
Bindplane server
that is configured with a
Google SecOps Standardization
processor
.
The Google SecOps Standardization processor is configured to add a supported
log_type
and an ingestion label (for example,
ingestion_source
).
To configure Bindplane for SHM with Google Cloud Monitoring, complete the following steps:
Send the hostname of the collector server as an attribute in each log entry.
On the
Log
tab, select
Processors
>
Add Processors
>
Copy Field
.
Configure the
Copy Field
processor:
Enter a short description for the resource.
Choose the
Logs
telemetry type.
Set the
Copy From
field to
Resources
.
Set the
Resource field
field to
host.name
.
Set the
Copy To field
field to
Attributes
.
Set the
Attributes Field
field, for example, to
chronicle_ingestion_label["ingestion_source"]
.
Configure the Google Cloud Monitoring threshold for SHM
Define a threshold based on your expected ingestion rate. Lower thresholds detect collector outages; higher thresholds detect upstream log gaps.
After you configure the Google Cloud Monitoring threshold for SHM, we recommend that you monitor the
Chronicle Collector
>
Ingestion
>
Total Ingestion Log Count
metric. For detailed sample-setup instructions, go to
Set up a sample policy to detect silent Google SecOps collection agents
.
Use a Google SecOps dashboard for SHM
Use a Google SecOps dashboard to view daily counts for monitoring hosts that have gone silent.
This method is great for high-level daily overviews, but this method does not support alerts, and the results have a latency of up to 6 hours.
Need more help?
Get answers from Community members and Google SecOps professionals.
