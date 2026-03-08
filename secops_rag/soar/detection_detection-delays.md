# Understand rule detection delays

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/detection-delays/  
**Scraped:** 2026-03-05T10:04:03.126903Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand rule detection delays
Supported in:
Google secops
SIEM
This document explains rule detection delays in Google Security Operations,
identifies contributing factors, outlines troubleshooting approaches, and
suggests techniques to reduce delays where possible.
Detection rules
Detection rules examine both regular and entity Universal Data Model (UDM)
events, which are normalized raw logs, to generate detections according to the
rule's specifications. Entity UDM events typically contain
context information
like user or asset details. Rules also generate detections based on previously
generated detections.
Expected and unpredicted delays
Detection times are subject to processing delays. While some rules trigger in
near-real-time, others may take several minutes or hours to complete. Factors
like rule type, run frequency, and detection generation method affect these
delays. This document explores these and other delay factors.
We categorize delays as either
expected
or
unpredicted
.
Expected delays
: These delays result from the
ingestion
process and
the configuration choices you make when setting up the detection rule. For
example, the time taken to create a detection is a factor. These delays depend on known structural
factors, such as the
rule type
,
run frequency
, the
detection generation
method
,
known limitations
, and other predictable
factors.
You can minimize these delays by changing or tuning detection
rule configurations, as described in this document.
For details, see
Tips to shorten delays
.
Unpredicted delays
: These are rule-specific or event-specific delays
caused by many factors, including delays in event data
arriving at Google SecOps, transient slowness in processing
pipelines within Google SecOps services,
re-enrichment
, 
and other
data processing delays
.
Analyze rule detection delays
To analyze rule detection delays, find information about the rule and its
surrounding factors:
In the Google SecOps console, go to
Detection
>
Rules and detections
.
The
Rules dashboard
shows rule metadata like
Rule name
,
Rule type
, and
Run frequency
.
For more details, see
Viewing rules in Rules dashboard
.
In the
Rules dashboard
, click a rule name to view the detection history and other details for a specific rule.
For any particular rule execution, there are several factors that can
impact detection latency. Dimensions like
Rule type
,
Run frequency
,
Event type
,
Event time
, and
Ingested time
are good heuristics for
understanding why a particular detection was delayed.
A
lightbulb
icon in the
Detection Type
column identifies detections generated from event data that is delayed by more than 30 minutes, rule reprocessing runs, or retrohunts. This icon also appears on the
Alerts
page in Google SecOps.
Familiarize yourself with the following topics to understand how these
factors influence rule detection delays:
Detection generation methods
Known limitations
Factors contributing to rule detection delays
Detection generation methods
Learn how the system creates rule detections to understand how the detection generation method affects detection delays.
The system generates rule detections in the following ways:
Streaming engine
The Streaming engine is a fast pipeline that typically operates with
less than a five-minute delay. It processes
single-event
rules with
no
match section
and
no external data sets
like reference lists or data
tables.
Query engine
The Query engine processes rules as follows:
Complex
single-event
rules
:
Single-event rules
that reference ref-lists or data tables.
Windowed single-event rules
that use a match window with a simple condition. For example, "an event where our count of events > 0". These rules run on a high-frequency (near-real time) query rate as new data is ingested and made available for rule processing.
Multi-event rules
: These rules query data over blocks of
event time
(10-minute, hourly, daily), according to a schedule that you set.
For
example, for a 10-minute schedule, the rule re-queries
event time
blocks
after 5 to 8 hours and 24 to 48 hours, depending on upstream processing
timelines.
Rules run against historical data
For details, see
Retro hunts
.
Re-enrichment of UDM events
For details, see
Re-enrichment of UDM events
and
Entity context graph processing
.
Known limitations
Here are some standard limitations that contribute to rule detection delays:
Enrichment delays can sometimes take longer than expected. Enrichment reprocessing causes later rule runs to re-evaluate data. The system performs multiple enrichment runs, and enrichment can update UDM events up to 24 hours after the event has been ingested.
Multiple-event rules often join contextual data that arrives many hours after the primary event's event time. High latency in this contextual data can cause
re-enrichment
processing and
rule replays
to interact, resulting in a delayed detection. While Google SecOps uses this feature to handle extremely late-arriving data, it appears as a large span of time between the detection window (event time block) and the alert's created time.
Context-aware rules are rules that rely on enrichment sources such as asset and identity aliasing, or the
entity context graph
. Because these rules rely on multiple event sources, they are more susceptible to high latency.
The system re-executes rules between 5 and 8 hours, and again between 24 and 48 hours after the initial rule execution. These two separate
rule replays
are triggered based on the reprocessing pipeline execution times.
For additional detection limits, see
Understand detection limits
.
Troubleshoot rule detection delays
Troubleshoot rule detection delays through a process of elimination.
Follow this suggested approach to investigate and troubleshoot rule detection delays:
Check for obvious delays:
Determine if any ingestion delay exists:
In the Google SecOps console, go to
Detection
>
Rules and detections
.
Search for the rule to analyze in the
Rules Dashboard
.
Compare the
Event time
to the
Ingested time
.
For example, for a particular rule detection, if a large gap exists
between the
Event time
and the
Ingested time
, you can likely
attribute the detection delay to an
expected delay
. 
A
lightbulb
icon in the Detection Type column is applied when the
Ingestion time
is more than 30 minutes after the
Event time
.
Review the context source collection time:
Check the context source's collection time.
Context-aware rules can include the following context sources. Check their collection times:
Fields derived from UDM enrichment.
Events that include a
principal
field.
Rules that reference a
graph.entity
field.
Rules referencing the entity context graph (ECG) with
graph.entity
syntax can cause particularly high latency. For example, the ECG pipeline
generates context data, a process that can take 30 hours or, in some
cases, up to 8 days, depending on the data type.
For more details, see
Data processing delays
.
Examine the rule's run frequency and match window configuration:
Frequency:
Check the rule's run frequency. A rule configured to run less frequently naturally has longer detection delays.
Match window:
If a rule has a match window, the minimum delay is the duration of that window.
Frequency and match window relationship:
Ensure the run frequency is compatible with the match window. For example, if the match window is 5 minutes, a 10-minute run frequency is acceptable. However, if the match window is more than 10 minutes, use the next available run frequency, 1 hour.
Check for recent incidents:
Look for any recent incidents that could have caused delays or issues with data feeds.
Tips to shorten delays
To update detection rule configurations, see
Manage rules using the Rules editor
.
Use the following techniques to reduce delays where possible:
For latency-sensitive rules, use the most frequent run options:
Increase the rule frequency
:
To reduce delays, configure the highest possible frequency based on the rule type and match window:
For single-event rules: Use
Near-real time
.
For multiple-event rules with match windows less than 60 minutes: Use
10 minutes
.
For rules with match windows of 60 minutes or more: Use
1 hour
or
24 hours
, as appropriate.
For more details, see
Set the run frequency
.
Reduce match window duration
:
Reducing the match window doesn't directly affect latency, but it can increase efficiency by setting the minimum delay.
Avoid late-arriving data
:
Late-arriving data misses the initial query, and the system processes it only
when it re-queries its event time block 5 to 8 hours later, causing
significant delays. On-time data typically has about a 20-minute delay.
Factors contributing to rule detection delays
The
rule type
,
run frequency
, and the speed of
   Google SecOps's
ingestion
are key factors in rule detection delays.
The following factors contribute to rule detection delays.
Rule types
Rules fall into two main categories:
Single-event rules
Because
Single-event rules
are executed in near-real time using a streaming approach, use them to minimize delays, where possible.
These rules detect single events and don't use reference lists, data
tables, match windows, or User and Entity Behavior Analytics (UEBA). These
rules execute in near-real time, in a streaming fashion, and have
the shortest detection delays.
Complex single-event rules
These rules are more susceptible to detection delays because they include match windows or reference lists:
Windowed single-event rules
These are single-event rules that include a match window and typically have
a slightly longer delay than other single-event rules. A match window is
typically a period of time in which a rule examines one or more events.
Reference single-event rules
These are single-event rules that include reference lists or data tables.
Multiple-event rules
Multiple-event rules
execute on a scheduled basis, which results in longer delays due to the time between scheduled runs.
Multiple-event rules
These rules examine two or more UDM event conditions. They typically have a match window and multiple conditions.
Context-aware rules
Context-aware rules
help you join additional entity and detection context data to your events.
These rules consist of two or more data sources, where at least one condition is a UDM entity event (where the UDM event is of context type, such as
user_context
).
Context-aware rules are the most sensitive to late arriving data.
Context-aware rules generally have the longest delays because the system must first generate the necessary context data such as data in the
Entity Context Graph
.
For more details, see
Use context-enriched data in rules
.
Learn more about the difference between
Single-Event
and
Multiple-Event
rules.
Rule run frequency
Rule run frequency directly impacts detection delay.
Near-real time:
Rules execute more frequently for real-time data. This applies only to single-event rules.
Other frequencies:
For other rule types, you can set the following frequencies:
10-minute frequency is valid for match windows < 60 minutes.
1-hour and 24-hour frequencies are valid for match windows less than 48 hours.
24-hour frequency is valid for all match windows >= 48 hours.
Possible workaround:
To achieve faster detections, use a shorter run frequency. Reducing the match window doesn't directly affect latency, but it can increase efficiency by setting the minimum delay.
Match window
If a rule has a match window, the window's duration determines the minimum detection delay, as the system must wait for the entire window to occur.
Ingestion delay
Ingestion delay refers to the time Google SecOps takes to ingest data after the event occurs.
If data arrives late, it misses the initial query window. A subsequent historical processing query picks it up, but this can introduce delays of 5 to 8 hours.
For example: Event A (9:03 AM event time) and Event B (9:05 AM event time) are part of a rule looking for two events within 30 minutes. If Event A arrives at 10:05 AM (1 hour late), it misses the initial queries of the 9:00-9:30 AM block. A follow-up query for that block between 2-5 PM then generates the detection, resulting in delays of 5 to 8 hours.
Troubleshooting:
Verify that you send data to Google SecOps as soon as the event occurs. When reviewing a detection, carefully check the UDM event and ingestion timestamps.
Time zone issues
The Google SecOps SIEM default time zone is UTC. If logs don't include an explicit time zone definition, the system interprets them as UTC. Incorrect interpretation can cause the logs to be treated as late-arriving, which results in detection delays, even if the system receives them in real time.
For example, a log with an event time of 10:00 AM Eastern Time (15:00 UTC) arrives at 15:05 UTC, but it lacks a time zone. If the log lacks a time zone, the system interprets the event time as 10:00 UTC. The system then calculates a 5-hour delay between the interpreted event time (10:00 UTC) and the actual ingestion time (15:05 UTC). This calculated delay triggers detection delays because rules prioritize processing based on real time ingestion.
Workarounds:
If the original data's event timestamp is in a time zone other than UTC, try one of the following:
Update the original data's event time zone.
If you cannot update the time zone at the log source, contact
Support
to override the time zone.
Alternatively, use a BindPlane processor to correct the timestamp and format it as UTC, or add the appropriate time zone indicator. For details, see
Modifying log body timestamps using BindPlane
.
Contextual joins
Multiple-event rules that use contextual data, such as UEBA or entity context graph fields, might experience longer delays. Google SecOps must first generate the contextual data.
Enrichment system
Google SecOps enriches UDM events by adding contextual data from
other sources. This process usually completes within 30 minutes. Delays in
adding this enriched data to UDM events can increase detection times.
To check if a rule is evaluating an enriched field, review the
Event Viewer
. If the rule is
evaluating an enriched field, the detection might be delayed.
For more details, see
Data enrichment
.
Aliasing and enrichment
Aliasing
and
enrichment
are two steps in the Google SecOps security data enrichment process that correlates and adds context data to event records.
Aliasing
finds the connections, and
enrichment
populates the UDM fields with that connected data. The fields populated by this process are referred to as
aliased fields
or
enriched fields
.
Aliasing:
This is the process of identifying and linking different names or identifiers for the same entity. It finds additional context data that describes an indicator.
For example, aliasing can connect a single
hostname
(like
alex-macbook
) to other related indicators, such as its
IP addresses
and
MAC addresses
(from DHCP logs). Aliasing can also connect a
user ID
(like
alex
) to the user's
job title
and
employment status
(from user context data).
Enrichment:
This is the process that uses the information gathered from aliasing to add context to a UDM event.
For example, when a new event arrives with only an
IP address
, the enrichment process uses the aliased data to find the associated
hostname
(for example,
alex-macbook
) and populates the
$udm.event.principal.hostname
field.
Google SecOps supports aliasing and enrichment for several entity types, including: assets (for example, hostnames, IP addresses, MACs), users, processes, file hash metadata, geographic locations, and cloud resources. For more details, see
UDM enrichment and aliasing overview
.
Re-enrichment of UDM events
Underlying data changes:
If the underlying data changes after an event is ingested, the system reprocesses historical data and
updates events for up to 24 hours after ingestion.
Enrichment system updates:
If the enrichment system updates entity or process metadata, IP
geolocation, or VirusTotal indicators, the rules engine re-evaluates these
blocks 24 to 48 hours later to capture those updates.
For example, an event at 9:03 AM has
entity.asset.hostname = hostnameA
but
no IP. A DHCP log from 8:55 AM shows
hostnameA = IP 1.2.3.4
. The rules
engine runs at 9:10 AM, and the rule doesn't match. The enrichment processing
pipeline correlates
hostnameA
to
1.2.3.4
for that time window, updating
the UDM event. Now the rule matches, and the system creates a detection.
Delayed context data:
If you send context data, such as a
hostname
, one day after the initial log,
the system re-enriches the UDM event. Rules that look for this re-enriched data
then run again and create a detection. This feature ensures that the system
creates detections even when context is delayed.
Changes in enrichment data:
Changes in enrichment data can cause a rule to match later, even if it
didn't initially.
For example, an event at 9:03 AM has
entity.ip_geo_artifact.country_or_region = USA
. The rules engine runs at
9:10 AM, querying 9:00-10:00 AM, and the rule doesn't match. Later,
enrichment reprocessing updates the geolocation to Canada. When the rule
runs again, it now matches, and the system creates a detection.
Entity context graph processing
The system generates and adds
entity context graph (ECG)
information to log data
to provide context, for example, indicators of compromise (IOCs) or asset
context data. Because the ECG pipeline relies mostly on batch processing, entity
context information often updates only after a rule execution creates a
detection.
Retro hunts
When you run a rule against historical data using a retro hunt, the system
only creates the detection after the retro hunt process finishes. This process
can take a significant amount of time, which causes a detection delay.
Example of a retroactive update process:
Initial event:
An event arrives at 1:00 PM with
ip_address = 10.0.0.5
. At this time, the
hostname
is unknown.
Aliasing source arrives:
At 2:30 PM (more than an hour later), a DHCP log arrives for 1:00 PM, linking
10.0.0.5
to
workstation-123
.
Retroactive enrichment:
The aliasing system processes this new link. It retroactively updates the UDM event from 1:00 PM, enriching the previously empty
$udm.event.principal.hostname
field with the value
workstation-123
.
Detection:
Subsequent rule replays see the enriched value (
workstation-123
) and can trigger detections that were previously missed.
Note:
You cannot distinguish latency monitoring metrics for live detection
rules from retrohunt detection rules. To avoid skewing your detection latency
monitoring metrics, don't use a live rule to simulate a retrohunt rule. As a
best practice, create a dedicated detection rule and run it as a retrohunt
rule.
Reference lists
Rule executions always use the latest version of a reference list. When
scheduled rules run again, the system can create new detections based on updated
reference list contents. These detections might appear late because they're based on data ingested prior to the reference list update.
To shorten detection delays, do the following:
Send log data to Google SecOps as soon as the event occurs.
Review the audit rules to determine whether to use non-existence or context-enriched data.
Configure a smaller
run frequency
.
Non-existence rules
The system waits at least one hour before executing rules that check for
non-existence
(for example, rules that contain
!$e
or
#e=0
), ensuring data has time to arrive.
Data processing delays
The system might continue processing data even after creating an initial detection, potentially leading to new or updated detections. For details, see
When rule replays are triggered
.
Need more help?
Get answers from Community members and Google SecOps professionals.
