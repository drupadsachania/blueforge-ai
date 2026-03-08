# Configure Bindplane for Silent Host Monitoring

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/bindplane-silent-host-monitoring/  
**Scraped:** 2026-03-05T09:16:30.344052Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure Bindplane for Silent Host Monitoring
Supported in:
Google secops
SIEM
Google Security Operations Silent Host Monitoring lets you create alerts for ingestion rate changes using Google Cloud Monitoring. It generates alerts per collector and notifies you when the ingestion rate falls below your defined threshold, signaling potential collector stoppages. This feature works with the gRPC API.
Prerequisites
This guide assumes you already use a
Google SecOps Standardization processor
.
Configure Bindplane for Silent Host Monitoring
To enable Bindplane for Silent Host Monitoring, send the collector server's hostname as an attribute within the log entry.
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
field to
chronicle_ingestion_label["ingestion_source"]
.
Google Cloud Monitoring threshold
Set the threshold according to your needs:
A very low threshold alerts you when the collector might be down.
A very high threshold indicates potential source collection issues.
We recommend that you monitor the
Chronicle Collector
>
Ingestion
>
Total Ingestion Log Count
metric.
For detailed setup instructions, see
Set up a sample policy to detect silent Google SecOps forwarders
.
Need more help?
Get answers from Community members and Google SecOps professionals.
