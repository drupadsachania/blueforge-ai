# Use Cloud Monitoring for ingestion insights

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics/  
**Scraped:** 2026-03-05T09:30:54.712424Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use Cloud Monitoring for ingestion insights
Supported in:
Google secops
SIEM
This document describes how to use
Cloud Monitoring
to receive ingestion notifications. Google SecOps uses Cloud Monitoring to send the ingestion notifications. Use this feature for ingestion notifications and ingestion volume viewing. You can integrate email notifications into existing workflows. Notifications are triggered when the ingestion values reach certain predefined levels.
In the Cloud Monitoring documentation, notifications are called
alerts
.
Before you begin
Be familiar with
Cloud Monitoring
.
Configure a Google Cloud project for Google SecOps
.
Verify that your Identity and Access Management role includes the permissions in the role
roles/monitoring.alertPolicyEditor
. For more information about roles, see
Control access with IAM
.
Familiarize yourself with creating alerting policies in Cloud Monitoring. For information about these steps, see
Create metric-threshold alerting policies
.
Configure the notification channel to receive ingestion notifications as email. For information about these steps, see
Create and manage notification channels
.
Set up ingestion notification for health metrics
To set up notifications that monitor ingestion health metrics specific to Google SecOps, do the following:
In the Google Cloud console, select
Monitoring
.
In the navigation pane, select
Alerting
and then click
Create policy
.
On the
Select a metric
page, click
Select a metric
.
In the
Select a metric
menu, click either of the following:
Active
toggle to filter and display only resources and metrics with data from the last 25 hours. If you don't select this, all resource and metric types are listed.
Org/folder level
toggle to monitor resources and metrics, such as consumer
quota usage or BigQuery slot allocation, for your organization and folders.
Select any of the following metrics:
Select
Chronicle Collector
>
Ingestion
and then select either
Total ingested log count
or
Total ingested log size
.
Select
Chronicle Collector
>
Normalizer
and then select either
Total record count
or
Total event count
.
Select
Chronicle Log Type
>
Outofband
and then select either
Total ingested log count (Feeds)
or
Total ingested log size (Feeds)
.
Click
Apply
.
Add a filter
On the
Select a metric
page, click
Add Filter
.
In the filter dialog, select the
collector_id
label, a comparator, and the filter value.
Select one or more of the following filters:
project_id
: ID of the Google Cloud project associated with this resource.
location
: Physical location of the cluster containing the collector object.
We recommend that you don't use this field. If you leave this field empty,
Google SecOps can use existing information to automatically determine where to store the data.
collector_id
: ID of the collector.
log_type
: Name of the log type.
Metric label
>
namespace
: Namespace of the log.
feed_name
: Name of the feed.
LogType
: Type of log.
Metric label
>
event_type
: Event type determines which fields are included with the event. The event type includes values, such as
PROCESS_OPEN
,
FILE_CREATION
,
USER_CREATION
, and
NETWORK_DNS
.
Metric label
>
state
: Final status of the event or log. The status is one of the following:
parsed
: The log is successfully parsed.
validated
. The log is successfully validated.
failed_parsing
. The log has parsing errors.
failed_validation
. The log has validation errors.
failed_indexing
. The log has batch indexing errors.
Metric label
>
drop_reason_code
: This field is populated if the ingestion source is the Google SecOps forwarder and indicates the reason why a log was dropped during normalization.
Metric label
>
ingestion_source
: The ingestion source present in the ingestion label when the logs are ingested using the Ingestion API.
Select a special collector ID. The
collector_id
can also be a forwarder ID or a special ID based on the ingestion method:
aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
:
Represents all feeds created using the Feed Management API or page. For more information about feed management, see
Feed management
and
Feed management API
.
aaaa1111-aaaa-1111-aaaa-1111aaaa1111
:
Represents Collection agent, including Bindplane (Google Edition).
aaaa1111-aaaa-1111-aaaa-1111aaaa1112
:
Bindplane Enterprise (Google Edition).
aaaa1111-aaaa-1111-aaaa-1111aaaa1113
:
Bindplane Enterprise.
aaaa1111-aaaa-1111-aaaa-1111aaaa1114
:
Headless collector.
aaaa2222-aaaa-2222-aaaa-2222aaaa2222
:
Logs ingested through the
HTTPS Push method, including includes Webhooks, Amazon Kinesis Firehose and Google Cloud Pub/Sub source type feeds.
aaaa3333-aaaa-3333-aaaa-3333aaaa3333
:
Cloud Storage logs and includes logs ingested through Event Threat Detection.
aaaa4444-aaaa-4444-aaaa-4444aaaa4444
:
Logs ingested through Azure Event Hub feed integration. This includes Microsoft Azure Event Hub source type feeds.
bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb
:
Represents all ingestion sources that use the Ingestion API
unstructuredlogentries
method. For more information about Ingestion APIs, see
Google SecOps Ingestion API
.
bbbb1111-bbbb-1111-bbbb-1111bbbb1111
:
Represents
ENTITY_RISK_CHANGE
events of the UDM log type generated within Google SecOps. For more information, see
Risk-based alerting with entity only rules
.
cccccccc-cccc-cccc-cccc-cccccccccccc
:
Represents all ingestion sources that use the Ingestion API
udmevents
method.
dddddddd-dddd-dddd-dddd-dddddddddddd
:
Represents any log ingested through the internal API, which is not through OutOfBand (OOB) processor ingestion, and not through Google Cloud log ingestion.
eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee
:
Represents the
collector_id
used for
CreateEntities
.
In the
Transform data
section, do the following:
Set the
Time series aggregation
field to
sum
.
Set the
Time series group by
field to
project_id
.
Optional: Set up an alert policy with multiple conditions. To create
ingestion notifications with multiple conditions within an alert policy, see
Policies with multiple
conditions
.
Google SecOps forwarder metrics and associated filters
The following table describes the available Google SecOps forwarder metrics and the associated filters.
Google SecOps forwarder metric
Filter
Container memory used
log_type
,
collector_id
Container disk used
log_type
,
collector_id
Container cpu_used
log_type
,
collector_id
Log drop_count
log_type
,
collector_id
,
input_type
,
reason
buffer_used
log_type
,
collector_id
,
buffer_type
,
input_type
last_heartbeat
log_type
,
collector_id
,
input_type
Set up a sample policy to detect silent Google SecOps forwarders
The following sample policy detects all the Google SecOps forwarders and sends alerts 
if the Google SecOps forwarders don't send logs for 60 minutes.
This may not be useful for all the Google SecOps forwarders which you want to monitor.
For example, you can monitor a single log source across one or many 
Google SecOps forwarders with a different threshold or exclude Google SecOps forwarders 
based upon their frequency of reporting.
In the Google Cloud console, select
Monitoring
.
Go to Cloud Monitoring
Click
Create Policy
.
On the
Select a metric
page, select
Chronicle Collector
>
Ingestion
>
Total ingested log count
.
Click
Apply
.
In the
Transform data
section, do the following:
Set the
Rolling window
to a time of up to 1 hour*.
Set the
Rolling window function
to
mean
.
Set the
Time series aggregation
to
mean
.
Set the
Time series group by
to
collector_id
. If this is not set 
to group by
collector_id
, then an alert triggers for each log source.
Click
Next
.
Select
Metric absence
and do the following:
Set
Alert trigger
to
Any time series violates
.
Set
Trigger absence time
to a time of up to 1 hour.
Enter a
name
for the condition and click
Next
.
In the
Notifications and name
section, do the following:
Select a notification channel in the
Use notification channel
field. We recommend that you configure multiple notification channels for redundancy purposes.
Configure notifications on incident closure.
Set policy user labels to an appropriate level. Use this setting to set the alert severity level for a policy.
Enter any documentation you want to send as part of the alert.
Enter a name for the alert policy.
Add exclusions to a catch-all policy
It may be necessary to exclude certain Google SecOps forwarders 
from a catch-all policy because they may just have low traffic volumes, or require 
a more custom alert policy.
In the Google Cloud console, select
Monitoring
.
On the navigation page, select
Alerting
and then in the
Policies
section, select the policy you want to edit.
On the
Policy details
page, click
Edit
.
On the
Edit alerting policy
page, under the
Add filters
section, select
Add a filter
and do the following:
Select the
collector_id
label and the collector you want to exclude from the policy.
Set the comparator to
!=
and the value to the
collector_id
you want to exclude, and click
Done
.
Repeat for each collector that needs to be excluded. You can also use a regular expression to exclude multiple collectors with only a single filter if you want to use the following format:
(?:aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|cccccccc-cccc-cccc-cccc-cccccccccccc)
Click
Save Policy
.
Set up a sample policy to detect silent Google SecOps collection agents
The following sample policy detects all the Google SecOps collection agents and sends alerts
if the Google SecOps collection agents don't send logs for 60 minutes.
This sample might not be useful for all the Google SecOps collection agents which you want to monitor.
For example, you can monitor a single log source across one or many 
Google SecOps collection agents with a different threshold or exclude Google SecOps collection agents based upon their frequency of reporting.
In the Google Cloud console, select
Monitoring
.
Go to Cloud Monitoring
Click
Create Policy
.
On the
Select a metric
page, select
Chronicle Collector
>
Agent
>
Exporter Accepted Spans Count
.
Click
Apply
.
In the
Transform data
section, do the following:
Set the
Rolling window
to up to 1 hour*.
Set the
Rolling window function
to
mean
.
Set the
Time series aggregation
to
mean
.
Set the
Time series group by
to
collector_id
. If this is not set 
to group by
collector_id
, then an alert is triggered for each log source.
Click
Next
.
Select
Metric absence
and do the following:
Set
Alert trigger
to
Any time series violates
.
Set
Trigger absence time
to up to 1 hour*.
Enter a
name
for the condition and click
Next
.
In the
Notifications and name
section, do the following:
Select a notification channel in the
Use notification channel
field. We recommend that you configure multiple notification channels for redundancy purposes.
Configure notifications on incident closure.
Set policy user labels to an appropriate level. This is used for setting the severity level of the alert for a policy.
Enter any documentation that you would like to be sent as part of the alert.
Enter a name for the alert policy.
Set up a sample policy to detect failure of a high-availability cluster of firewall servers
The following sample policy detects when both members of an active-passive, high-availability (HA) cluster of Linux firewall servers stop reporting—indicating a failure.
In the following sample policy, the HA cluster members are named
prod-linux-server-1
and
prod-linux-server-2
. To set up a sample policy to detect failure of a high-availability cluster of firewall servers, do the following:
In the Google Cloud console, select
Monitoring
.
Go to Cloud Monitoring
Click
Create Policy
.
Set the
Policy configuration mode
to
Builder
.
For
Select a metric
, select
Chronicle Collector
>
Ingestion
>
Total ingested log count
.
Click
Apply
.
In the
Add filters
section, enter the following:
ingestion_source one_of prod-linux-server-1, prod-linux-server-2
In the
Transform data
section, do the following:
Set the
Rolling window
to
5 min
.
Set the
Rolling window function
to
rate
.
Set the
Time series aggregation
to
mean
.
Set the
Time series group by
to
ingestion_source
.
Click
Next
.
From the
Condition Types
options, select
Metric absence
and do the following:
Set
Alert trigger
to
All time series violate
.
Set
Trigger absence time
to
5 min
.
Set the
Condition name
to
Linux-Active-Passive-Firewall-Cluster
.
Click
Next
.
In the
Notifications and name
section, do the following:
Select a notification channel in the
Use notification channel
field. We recommend that you configure multiple notification channels for redundancy purposes.
Configure notifications on incident closure.
Set policy user labels to an appropriate level. This is used for setting the severity level of the alert for a policy.
Enter any documentation that you want to be sent as part of the alert.
Enter a name for the alert policy.
View total ingestion by log type
To view ingestion volumes by log type in Cloud Monitoring, do the following:
On the
Settings
page, select
Profile
.
Select your Cloud Monitoring profile.
On the
Profile
page, type
Integrations
in the search bar.
Select
Metrics explorer
.
Click
promQL
to switch to promQL query mode.
In the
Queries
field, copy the following:
sum by (log_type) (increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}[1h]))
Optional: Filter a specific log type, and include it in the query.
For example, to view ingestion for the log type
GCP_CLOUDAUDIT
, the query would look like this:
sum(increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector",log_type="GCP_CLOUDAUDIT"}[1h]))
In the
Results
section, select the
Table
tab to view the summed data.
Optional: Adjust the time range, as needed.
Need more help?
Get answers from Community members and Google SecOps professionals.
