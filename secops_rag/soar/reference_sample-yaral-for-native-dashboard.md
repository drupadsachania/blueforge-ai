# Sample YARA-L 2.0 queries for Dashboards

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard/  
**Scraped:** 2026-03-05T10:06:42.345375Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Sample YARA-L 2.0 queries for Dashboards
Supported in:
Google secops
SIEM
This document provides a library of YARA-L 2.0 query examples for common dashboard use cases. These examples are organized by data source to help you visualize security telemetry, track analyst workflows, and measure the effectiveness of your automated response playbooks. For more information about dashboards, see
Dashboards overview
.
By using these queries, you can transform raw event and case data into high-level metrics, such as:
Monitoring log volume and drop rates.
Tracking the Mean Time to Repair (MTTR) and analyst workload.
Identifying top IoCs and frequent rule detections.
For more information about building and customizing your visual interface, see the
Dashboards overview
.
Data sources supported
To build effective dashboard widgets, you must first identify the correct data source for the metrics you want to visualize. Each data source within Google Security Operations is accessed using a specific YARA-L prefix and has unique time-retention limits.
The following table serves as a reference guide for the available data sources. The data sources are ordered in the table based on current adoption metrics in dashboards. Use the table to go to prefix requirements, field schemas, and specific query examples.
Data source
Query time interval
YARA-L prefix
Schema
Dashboard query examples
Events
90 days
no prefix
Fields (UDM)
|
Template
Examples
Entity Graph
365 days
graph
Fields
|
Template
Examples
Ingestion metrics
365 days
ingestion
Fields
|
Template
Examples
Cases and alerts
365 days
case
Fields (SOAR)
|
Template
Examples
Case history
365 days
case_history
Fields (SOAR)
|
Template
Examples
Playbooks
365 days
playbook
Fields (SOAR)
|
Template
Examples
Detections
365 days
detection
Fields
|
Template
Examples
Rules
No Time limit
rules
Fields
|
Template
Examples
Rule sets
365 days
ruleset
Fields
|
Template
Examples
IoCs
365 days
ioc
Fields
|
Template
Examples
Analyze user login events
This section provides YARA-L query examples for monitoring user authentication activity. Use these patterns to identify successful logins, failed attempts, and potential credential abuse across your data sources.
Group by login status
The following YARA-L query counts user logins, grouping them by login status of
"ALLOW"
or
"BLOCK"
:
//USER_LOGIN by status
metadata.event_type = "USER_LOGIN"
$security_result = security_result.action
$security_result = "BLOCK" OR $security_result = "ALLOW"

match:
    $security_result

outcome:
    $event_count = count_distinct(metadata.id)
Example: Monitor login trends
The following YARA-L query counts successful user logins over time:
//successful sign-ins over time
metadata.event_type = "USER_LOGIN"
$security_result = security_result.action
$security_result = "ALLOW"
$date = timestamp.get_date(metadata.event_timestamp.seconds, "America/Los_Angeles")

match:
    $security_result, $date

outcome:
    $event_count = count_distinct(metadata.id)

order:
    $date desc
Track logins by location
The following YARA-L query counts user logins, grouped by countries:
//user sign-ins by country
metadata.event_type = "USER_LOGIN"
$country = principal.location.country_or_region
$country != ""

match:
    $country

outcome:
    $event_count = count_distinct(metadata.id)

order:
    $event_count desc
Cases and alerts
Use cases and alerts to monitor operational SOC metrics, including alert categorization, case statuses, and incident resolution trends.
The following templates demonstrate how to query cases and alerts to visualize the health of your incident response lifecycle and monitor SOAR performance.
Data source
:
Cases and Alerts
Query prefix
:
case
(fields must be prefixed; for example,
case.priority
)
Time interval
: 365 days
Schema reference
The following schema defines the fields available for monitoring cases and alerts within the platform. This data source provides the operational telemetry required to track incident volume, prioritize response efforts, and evaluate the workload distribution across your security team. Use this schema to build high-level SOC metrics, such as case distribution by status, priority, and assignee.
Field name (query ready)
Data type
Description
case.name
String
Unique identifier (GUID) for a SOAR case.
case.priority
Enum
Priority of the case (for example,
PRIORITY_HIGH
).
case.status
Enum
Current status (for example,
OPEN
,
CLOSED
).
case.stage
String
Current workflow stage.
case.assignee
String
User ID or name of the entity assigned to the case.
case.score
Double
Risk score associated with the case.
Query examples
The following queries let SOC managers and lead analysts visualize incident response velocity and workload distribution. These examples focus on isolating active incidents, categorizing them by priority to ensure high-risk threats are addressed, and analyzing the overall lifecycle of cases through status distribution. Use these templates to ensure your team is meeting service-level agreements (SLAs) and to identify bottlenecks in the remediation process.
For more information about field descriptions in the following examples, see
Cases and alerts
.
Total open incidents
The following example calculates the total number of active, open incidents, providing a baseline metric for active SOC workload:
case.incident = true
case.status = "OPENED"

outcome:
  $Count = count(case.name)
Incident priorities distribution
The following example groups all active incidents by their assigned priority level, allowing for a weighted view of current environmental risk:
case.incident = true

$Priority = case.priority

match:
  $Priority

outcome:
  $Count = count(case.name)

order:
  $Count desc
Case status distribution
The following example provides a comprehensive view of all cases (both incidents and alerts) across every lifecycle phase (for example,
Opened
,
Closed
,
Suspended
):
$Status = case.status

match:
  $Status

outcome:
  $Count = count(case.name)

order:
  $Count desc
Count cases by status
The following YARA-L queries help analyze cases and alert data:
match:
   case.status

outcome:
   $count=count(case.name)
Count cases tagged as
SUSPICIOUS
case.tags.name="SUSPICIOUS"

outcome:
   $count=count(case.name)
Calculate mean time to detect (in minutes)
$case_created_time = case.created_time.seconds
$alert_time = case.alerts.metadata.detection_time.seconds

outcome:
   $avg_time = math.round(window.avg($case_created_time - $alert_time)/60, 2)
Case history
Use a case history to track activity trends across the case lifecycle.
The following templates show how to query case history to visualize the lifecycle of security incidents and calculate critical SOC performance metrics like MTTR and MTTA:
Data source
:
Case History
Query prefix
:
case_history
(fields must be prefixed; for example,
case_history.case_activity
)
Time interval
: 365 days
Schema reference
The following schema defines the fields available for auditing the chronological actions taken within a SOAR case. Unlike the
cases and alerts schema
, which shows current state, case history tracks every transition, assignment, and status change over time. Use this schema to perform complex time-series analysis and identify operational bottlenecks within your incident handling process.
Field name (query ready)
Data type
Description
case_history.name
String
Unique identifier (GUID) for the specific history event.
case_history.case_response_platform_info.case_id
String
Unique identifier for the parent SOAR case.
case_history.case_activity
Enum
Type of activity performed (for example,
STAGE_CHANGE
,
ASSIGNEE_CHANGE
,
CREATE_CASE
).
case_history.event_time.seconds
Timestamp
Epoch timestamp indicating when the activity occurred.
case_history.assignee
String
Identity of the new assignee after the event.
case_history.stage
String
New workflow stage after the event.
Query examples
The following queries let SOC managers measure the efficiency of the security team using standard industry metrics. These examples focus on handling time (time spent in specific stages), Mean Time to Resolve (MTTA), and Mean Time to Acknowledge (MTTA). By analyzing the transitions between "Create," "Assign," and "Close" activities, these templates provide quantitative data on how quickly the organization responds to and neutralizes threats.
For more information about field descriptions in the following examples, see
Case history
.
Analyze case activity distribution
The following YARA-L query retrieves the case history by activity count:
match:
   case_history.case_activity

outcome:
   $count=count_distinct(case_history.name)
Handling time by case stage - last 7 days
The following example calculates the duration (in minutes) that cases spend in various workflow stages to identify where delays occur:
case_history.assignee.soc_roles != ""

$Case_ID = case_history.case_response_platform_info.case_id
$Case_Stage = case_history.stage

match:
  $Case_Stage

outcome:
  $Handling_Time_Minutes = (max(case_history.event_time.seconds) - min(case_history.event_time.seconds)) / 60
MTTR in minutes - last 7 days
The following example shows a multi-stage query that isolates cases that have both
CREATE_CASE
and
CLOSE_CASE
activities to calculate the average time-to-closure across the environment:
stage stage1 {
  $case_id = case_history.case_response_platform_info.case_id

  match:
    $case_id

  outcome:
    $case_close_time = max(if(case_history.case_activity = "CLOSE_CASE", case_history.event_time.seconds, 0))
    $status = array_distinct(case_history.case_activity)
    $TTC = $case_close_time - min(case_history.event_time.seconds)

  condition:
    arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "CLOSE_CASE")
}

outcome:
  $case_count = count($stage1.case_id)
  $MTTC = (math.round(avg($stage1.TTC)/60))
  $log_count desc
MTTA in minutes - last 7 days
The following example measures the average duration between the creation of a case and its first assignment to an analyst, reflecting the speed of initial SOC intake:
stage stage1 {
  $case_id = case_history.case_response_platform_info.case_id

  match:
    $case_id

  outcome:
    $case_assign_time = min(if(case_history.case_activity = "ASSIGNEE_CHANGE", case_history.event_time.seconds, 9999999999999999))
    $status = array_distinct(case_history.case_activity)
    $TTA = $case_assign_time - min(case_history.event_time.seconds)

  condition:
    arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "ASSIGNEE_CHANGE")
}

outcome:
  $case_count = count($stage1.case_id)
  $MTTA = (math.round((avg($stage1.TTA)/60)))
Detections
The following templates demonstrate how to query detection metrics for threat visibility and security performance visualizations:
Data Source
:
Detections
Query Prefix
:
detection
(fields must be prefixed; for example,
detection.rule_name
)
Time Interval
: 365 days
Schema reference
The following schema defines the structured format for monitoring security alerts. It's optimized for tracking detection frequency, risk distribution, and rule performance across the environment.
Field name (query ready)
Data type
Description
detection.rule_name
String
Name of the rule that generated the detection.
detection.id
String
Unique ID for a detection.
detection.severity
Enum
Severity of the detection (for example,
HIGH
,
CRITICAL
).
detection.risk_score
Float
Risk score associated with the detection.
detection.detection_timing_details
Enum
Rule execution context. Supported values include:
DETECTION_TIMING_DETAILS_UNSPECIFIED
: Standard rule execution.
DETECTION_TIMING_DETAILS_REPROCESSING
: Generated with a rule replay (late-arriving data, enrichment updates, or entity graph changes).
DETECTION_TIMING_DETAILS_RETROHUNT
: Generated through a rule Retro-Hunt.
detection.event_timestamp
Timestamp
Timestamp when the detection event occurred.
detection.rule_run_frequency
Enum
Frequency of rule execution (for example
RUN_FREQUENCY_HOURLY
,
RUN_FREQUENCY_REALTIME
,
RUN_FREQUENCY_DAILY
).
detection.rule_type
Enum
Rule logic and execution frequency. Supported values:
SINGLE_EVENT
MULTI_EVENT
detection.summary
String
Human-readable summary of the detection.
detection.latency_metrics.newest_ingestion_time.seconds
Timestamp
Timestamp of the most recent ingestion time of the events evaluated in the detection.
detection.latency_metrics.newest_event_time.seconds
Timestamp
Timestamp of the most recent raw events evaluated in the detection.
detection.latency_metrics.oldest_ingestion_time.seconds
Timestamp
Timestamp of the oldest ingestion time of the events evaluated in the detection.
detection.latency_metrics.oldest_event_time.seconds
Timestamp
Timestamp of the oldest raw events evaluated in the detection.
Query examples
The following queries are designed to transform raw Detections data into high-level security dashboards. By targeting the detections data source, these examples encourage security analysts and SOC managers to monitor the threat landscape in real-time.
These queries focus on critical security pillars: threat trends (tracking alert volume over time), top offenders (identifying frequent rule triggers across cloud providers), and IOC analysis (categorizing detections by IoC types). Use these templates to identify emerging attack patterns and ensure high-risk alerts are prioritized for investigation.
Example: Alerts over time
The following example tracks cloud-related security threats (specifically those involving secrets or KMS) to visualize how these specific risks trend daily:
detection.detection.ruleset_category_display_name = "Cloud Threats"
detection.detection.alert_state = "ALERTING"
detection.detection.rule_name = /Secrets|Key|KMS/ nocase

$Date = timestamp.get_date(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
$Rule_Name = detection.detection.rule_name

match:
  $Date, $Rule_Name

outcome:
  $Count = count(detection.id)

order:
  $Date desc
Top 10 detections
The following example provides a breakdown of the most frequent detections across major cloud providers (Google Cloud, Amazon Web Services (
AWS
), Microsoft Azure (
AZURE
)), limited to the top 10 most active rules:
$log_type = detection.collection_elements.references.event.metadata.log_type
$log_type = /GCP|AWS|AZURE/
$rule_name = detection.detection.rule_name
$rule_name != ""

match:
  $rule_name

outcome:
  $event_count = count(detection.id)

order:
  $event_count desc

limit:
  10
Detections over time by IoC type
The following example categorizes detections by their Indicator of Compromise (IoC) type, letting teams see which types of threats (for example, IP, Domain, Hash) are most prevalent:
detection.detection.rule_name = /ioc/ nocase

$Date = timestamp.get_date(detection.collection_elements.references.entity.metadata.event_metadata.event_timestamp.seconds)
$IOC_Type = detection.collection_elements.references.entity.metadata.entity_type

match:
  $Date , $IOC_Type

outcome:
  $Count = count(detection.id)

order:
  $Count desc
Detections by severity over time
The following YARA-L query counts detections, grouped by severity and date:
//Detection count by severity over time
$date = timestamp.get_date(detection.created_time.seconds)
$severity = detection.detection.severity

match:
    $date, $severity

outcome:
    $detection_count = count_distinct(detection.id)

order:
    $date asc
Top 10 rule names by detection count
The following YARA-L query retrieves the top 10 rule names, ranked by their detection count (or frequency):
//top ten rule names by detection count
$rule_name = detection.detection.rule_name

match:
    $rule_name

outcome:
    $count = count_distinct(detection.id)

order:
    $count desc

limit:
    10
Top 10 IP addresses
The following YARA-L query retrieves the top 10 IP addresses from
principal
,
target
and
source
fields, ranked by their detection count:
$ip = group(detection.collection_elements.references.event.principal.ip,detection.collection_elements.references.event.target.ip,detection.collection_elements.references.event.src.ip)

$ip != ""

match:
  $ip

outcome:
  $count = count(detection.id)

order:
  $count desc

limit:
  10
Entity Graph
The following templates demonstrate how to query the UDM entity model to visualize asset risk and threat intelligence context:
Data source
:
Entity Graph
Query prefix
:
graph
(fields must be prefixed; for example,
graph.metadata.entity_type
)
Time interval
: 365 days
Schema reference
The following schema defines the structured format for entities within the graph. While the Event schema captures point-in-time activity, the Entity schema provides the "state-in-time" context for users, assets, and indicators of compromise (IoCs). This lets developers correlate telemetry with business context.
Field name (query ready)
Data type
Description
graph.metadata.entity_type
Enum
The type of entity (for example, `USER`, `ASSET`).
graph.metadata.product_name
String
Product name that produced the entity information.
graph.entity.user.department
String
Department associated with a user entity.
graph.entity.asset.hostname
String
Hostname of an asset entity.
graph.entity.asset.location.name
String
Physical location or region of the asset.
graph.risk_score.risk_score
Float
Risk score associated with the entity.
For a list of additional Entity Graph-related fields, see
UDM field list
.
Query examples
The following queries use the Entity Graph to identify high-risk assets and track threat intelligence indicators.
Top PCI assets by risk
The following example identifies assets within the PCI scope and ranks them by their current risk score:
graph.metadata.entity_type = "ASSET"
graph.entity.hostname in %PCI_Assets

$Hostname = graph.entity.hostname
$Risk_Score = graph.risk_score.risk_score

match:
  $Hostname, $Risk_Score

order:
  $Risk_Score desc
IoCs with high risk score
The following example aggregates various indicator types (IP, URL, Hash) and calculates the average risk score from threat intelligence feeds:
$IOC_Type = graph.metadata.entity_type
$Risk_Score = graph.metadata.threat.risk_score
$Date = timestamp.get_date(graph.metadata.collected_timestamp.seconds)
$Hash = group(graph.entity.file.sha256, graph.entity.file.md5)

$IOC_Value = strings.coalesce(
  if(graph.entity.ip != "", graph.entity.ip, ""),
  if(graph.entity.url != "", graph.entity.url, ""),
  if($Hash != "", $Hash, "")
)

$IOC_Value != ""

match:
  $Date, $IOC_Type, $IOC_Value

outcome:
  $Total_Risk_Score = math.round(avg($Risk_Score), 2)
  $Count = count(graph.metadata.event_metadata.id)

order:
  $Total_Risk_Score desc
Recent ransomware intel sources events
The following example filters for ransomware-related threat intelligence and extracts the associated indicators for dashboard visualization:
graph.metadata.threat.description = /ransom/ nocase

$Hash = group(graph.entity.file.sha256, graph.entity.file.md5)

$IOC_Value = strings.coalesce(
  if(graph.entity.ip != "", graph.entity.ip, ""),
  if(graph.entity.url != "", graph.entity.url, ""),
  if($Hash != "", $Hash, "")
)

$IOC_Value != ""

$IOC_Type = graph.metadata.entity_type
$Threat = graph.metadata.threat.description
$Date = timestamp.get_date(graph.metadata.collected_timestamp.seconds)

match:
  $Date, $Threat, $IOC_Value, $IOC_Type

outcome:
  $Count = count(graph.metadata.event_metadata.id)

order:
  $Count desc
Events
The following templates demonstrate how to query UDM Event fields for dashboard visualizations.
Data source
:
Events
Query prefix
: None (fields referenced directly; for example,
metadata.event_type
)
Time interval
: 90 days
Schema reference
The following schema defines the structured format for security and system events used in data processing and analysis. It is designed to be
query ready
, making sure that security analysts and data engineers can efficiently filter, aggregate, and correlate logs across different sources. By standardizing fields, such as timestamps, identities (
principal
), and outcomes (
security_result
), this schema enables consistent visibility into activities like network traffic, process executions, and user authentication.
Field name (query ready)
Data type
Description
metadata.event_type
Enum
Type of event (for example,
PROCESS_LAUNCH
,
USER_LOGIN
).
metadata.event_timestamp.seconds
Integer
Epoch timestamp of the event in seconds.
metadata.product_name
String
Name of the product that generated the log.
metadata.vendor_name
String
Name of the product vendor.
principal.ip
String
IP address of the acting entity.
principal.user.userid
String
User ID of the acting entity.
target.ip
String
IP address of the target entity.
network.sent_bytes
Integer
Number of bytes sent.
security_result.action
Enum
Action taken, such as
BLOCK
or
ALLOW
.
For a list of UDM fields, see
UDM field list
.
Query examples
This section shows specific queries designed to power visual dashboards, transforming raw logs into actionable insights regarding application control and user activity.
By leveraging the Events schema, these queries let analysts track execution trends, identify blocked high-risk applications, and monitor authentication patterns across the enterprise in real-time.
Application executions over time
The following example tracks the volume of allowed (
allow
) and blocked (
block
) executions across the environment:
// Selection Criteria
metadata.product_event_type = /(execution|application) (allow|block)/ nocase or
security_result.threat_name = /application control/ nocase

// Logic
$Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F")

match:
  $Date

outcome:
  $Count = count(metadata.id)
Top 10 blocked application executions by reason
The following example identifies the specific files that are blocked and the policy reason for the action:
// Selection Criteria
(metadata.product_event_type = /(execution|application) block/ nocase or
security_result.threat_name = /application control/ nocase) and
security_result.action = "BLOCK"

// Logic
$Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
$Reason = strings.coalesce(target.resource.attribute.labels["categoryTupleDescription"], security_result.action_details, metadata.product_event_type)

match:
  $Application, $Reason

outcome:
  $Count = count(metadata.id)

order:
  $Count desc

limit:
  10
Top 10 successful user login trends
The following example monitors user login frequency across Workspace activity to detect abnormal patterns:
// Selection Criteria
metadata.log_type = "WORKSPACE_ACTIVITY"
metadata.product_event_type = "LOGIN_SUCCESS"
principal.user.email_addresses != ""

// Logic
$User_Account = principal.user.email_addresses
$Date = timestamp.get_date(metadata.event_timestamp.seconds)

match:
  $User_Account, $Date

outcome:
  $Count = count(metadata.id)

order:
  $Count desc

limit:
  10
Ingestion metrics
Use ingestion metrics to monitor the health and volume of data that enters the system.
The following templates demonstrate how to query ingestion metrics for health and performance visualizations:
Data Source
:
Ingestion Metrics
Query Prefix
:
ingestion
(fields must be prefixed; for example,
ingestion.log_type
)
Time Interval
: 365 days
Schema reference
The following schema defines the structured format for monitoring log flows. It's optimized for tracking ingestion health, volume, and normalization states across all collection mechanisms. For more information about field descriptions in the following examples, see
Ingestion metrics schema
.
Field name (query ready)
Data type
Description
ingestion.log_type
String
The log source type (for example,
WINDOWS_DNS
).
ingestion.component
String
TIngestion component (for example,
Forwarder
,
Ingestion API
).
ingestion.collector_id
String
Unique identifier of the collection mechanism.
ingestion.log_volume
Float
Volume of logs in bytes.
ingestion.log_count
Float
Number of logs ingested.
ingestion.drop_count
Float
Number of logs dropped.
For additional fields, see
Ingestion metrics schema
. Learn more about the
Ingestion API
,
ingestion methods
,
ingestion metrics schema reference
.
Query examples
The following queries are designed to transform raw ingestion metrics into high-level operational dashboards. By targeting the ingestion data source, these examples encourage platform administrators and data engineers to monitor the health of the entire data pipeline in real-time.
These queries focus on critical operational pillars:
volume tracking
(measure license consumption and throughput),
normalization health
(identify where logs fail to parse or validate), and
component reliability
(confirm the Ingestion API and Forwarders are communicating correctly). Use these templates to identify ingestion bottlenecks and make sure high-value logs are successfully converted into searchable UDM events.
Ingestion throughput over time
The following example tracks the total size of logs (in bytes) processed by the
Ingestion API
over time:
$Date = timestamp.get_date(ingestion.end_time)

match:
  $Date

outcome:
  $Total_Size_Bytes = sum(if(ingestion.component = "Ingestion API", ingestion.log_volume, 0))
Ingested events by log type
The following example breaks down the ingestion health, comparing raw volume to normalized success and specific parsing or indexing failures:
$Log_Type = ingestion.log_type

match:
  $Log_Type

outcome:
  $Total_Size_Bytes = sum(if(ingestion.component = "Ingestion API", ingestion.log_volume, 0))
  $Total_Logs = sum(if(ingestion.component = "Ingestion API", ingestion.log_count, 0))
  $Total_Normalized_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "validated", ingestion.event_count, 0))
  $Total_Parsing_Error_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "failed_parsing", ingestion.log_count, 0))
  $Total_Validation_Error_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "failed_validation", ingestion.event_count, 0))
  $Total_Indexing_Error_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "failed_indexing", ingestion.log_count, 0))

order:
  $Total_Size_Bytes desc
Ingestion throughput
The following example calculates the daily ingestion volume in GB, excluding heartbeat data and empty log types:
ingestion.component = "Ingestion API"
ingestion.log_type != ""
ingestion.log_type != "FORWARDER_HEARTBEAT"

$Date = timestamp.get_date(ingestion.end_time)

match:
  $Date

outcome:
  $Throughput_GB = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)

order:
  $Date desc
Aggregate ingestion metrics by log type
The following YARA-L query counts
log
,
event
, and
drop_count
, grouped by
log_type
:
//log count, event count, and drop count by log type
ingestion.log_type != ""
$log_type = ingestion.log_type
match:
    $log_type
outcome:
    $log_count = sum(ingestion.log_count)
    $event_count = sum(ingestion.event_count)
    $drop_count = sum(ingestion.drop_count)
order:
    $log_count desc
For more ingestion metrics examples, see
Ingestion metrics schema
.
IoCs
The following templates demonstrate how to query IoCs to visualize threat intelligence matches and monitor high-risk infrastructure patterns:
Data Source
:
IoCs
Query Prefix
:
ioc
(fields must be prefixed; for example,
ioc.ioc_value
)
Time Interval
: 365 days
Schema reference
The following schema defines the fields available for analyzing threat intelligence matches. This data source correlates your environment's telemetry with known malicious indicators, providing visibility into the severity, origin (feed), and type of threats detected. It's essential for quantifying the impact of external threat feeds on your internal ecosystem.
Field name (query ready)
Data type
Description
ioc.ioc_value
String
Domain, IP, or hash indicator value.
ioc.ioc_type
String
Type of IOC (for example,
IOC_TYPE_DOMAIN
,
IOC_TYPE_IP
).
ioc.feed_log_type
String
IOC feed log type (for example,
ET_PRO_IOC
).
ioc.is_global
Boolean
Determines whether this is a global IOC indicator.
ioc.day_bucket_seconds
Integer
Specific day bucket when an IOC hit occurred, based on the event's timestamp.
ioc.category
String
Category or type for this indicator (for example, malware, phishing).
ioc.confidence_score
Integer
Raw confidence level provided by the original IOC source.
ioc.feed_name
String
Original feed from which the IOC indicator originated.
ioc.severity
String
Raw severity level assigned to the indicator.
ioc.ioc_ingest_time
Timestamp
Timestamp indicating when the IOC was first ingested into the system.
ioc.asset
String
The asset indicator associated with the match.
ioc.location
String
The physical location associated with the indicator.
Query examples
The following queries allow analysts to prioritize threat hunting efforts by identifying outliers and trends within IOC match data. These examples focus on rare values—which often indicate targeted or sophisticated attacks—indicator distribution by type, and longitudinal trends across different threat categories. Use these templates to identify which threat feeds are providing the most value and which infrastructure categories are seeing increased malicious activity over time.
For more information about field descriptions in the following examples, see
IoC fields
.
Top 10 rarely seen values
The following example identifies the indicators that appear least frequently in the environment, helping to highlight unique or "low-and-slow" threat actor activity:
ioc.ioc_value != ""

$ioc_value = ioc.ioc_value

match:
  $ioc_value

outcome:
  $count = count_distinct(ioc.ioc_value)

order:
  $count

limit:
  10
Top 10 IoCs
The following YARA-L query retrieves the top 10 IOCs, ranked by count:
ioc.ioc_type = "IOC_TYPE_DOMAIN"
ioc.ioc_value != ""

//Top 10 IOCs by count
$ioc_value = ioc.ioc_value

match:
  $ioc_value

outcome:
  $count = count_distinct(ioc.ioc_value)

order:
  $count desc

limit:
  10
IoC matches over time by category
The following example tracks the volume of indicator matches across different threat categories (for example, Command and Control compared to Adware) to identify shifting threat landscapes:
ioc.category != ""

$category = ioc.category
$ioc_date = timestamp.get_date(ioc.day_bucket_seconds)

match:
  $ioc_date, $category

outcome:
  $count = count_distinct(ioc.ioc_value)
Top 10 IoC prevalence
The following YARA-L query retrieves the top 10 IoCs, ranked by count:
//Top 10 IOCs by count
$ioc_value = ioc.ioc_value

match:
    $ioc_value

outcome:
    $ioc_count = count(ioc.ioc_value)

order:
    $ioc_count desc

limit:
    10
Playbooks
Use Playbooks to monitor your automated response capabilities with queries designed to identify faulted actions and track real-time playbook performance.
The following templates demonstrate how to query playbooks to visualize the efficiency, success rates, and environmental distribution of your automated response workflows:
Data Source
:
Playbooks
Query Prefix
:
playbook
(fields must be prefixed; for example,
playbook.display_name
)
Time Interval
: 365 days
Schema reference
The following schema defines the fields available for monitoring playbook execution and SOAR automation. This data source provides the insights necessary to evaluate the ROI of automation, identify failing workflows, and ensure that response logic is correctly distributed across different organizational environments. Use this schema to track performance metrics like completion percentages and error rates across your automation library.
Field name (query ready)
Data type
Description
playbook.name
String
Unique identifier (GUID) of the specific playbook run.
playbook.display_name
String
Human-readable display name of the playbook instance.
playbook.status
Enum
Execution status of the run (for example,
COMPLETED
,
FAILED
).
playbook.start_time.seconds
Timestamp
Epoch timestamp indicating when the playbook execution started.
Query examples
The following queries help automation engineers and SOC managers quantify the impact of automation on the incident response lifecycle. These examples focus on efficiency (measuring the rate at which playbooks successfully resolve alerts), reliability (identifying workflows with high error rates), and distribution (analyzing where automation is triggered). Use these templates to optimize your SOAR workflows and reduce the manual burden on security analysts.
The following YARA-L queries provide insights into Playbook executions. For more information about field descriptions in the following examples, see
Playbooks
.
Retrieve percentage of faulted actions
1
=
1
outcome
:
$
faulted_action
=
sum
(
if
(
playbook
.
action
.
status
=
"FAULTED"
,
1
,
0
))
$
to
tal_actions
=
count
(
playbook
.
action
.
name
)
$
percentage
=
(
$
faulted_action
/
$
to
tal_actions
)
*
100
Count running playbooks
playbook
.
status
=
"IN_PROGRESS"
OR
playbook
.
status
=
"PENDING_FOR_USER"
outcome
:
$
count
=
count_distinct
(
playbook
.
name
)
% Alerts closed per playbook
The following example calculates the percentage of successful playbook runs that resulted in an alert being automatically closed:
match:
  playbook.display_name

outcome:
  $Total_Playbook_Runs = count(playbook.name)
  $Alerts_Closed = sum(if(playbook.status = "COMPLETED" and playbook.action.action = /close/ nocase, 1, 0))
  $Percentage = math.round(($Alerts_Closed / $Total_Playbook_Runs) * 100, 2)

order:
  $Percentage desc
% Error runs
The following example monitors the reliability of your automation by calculating the failure rate across all playbook executions:
outcome:
  $Total_Playbook_Runs = count(playbook.name)
  $PlaybookError = sum(if(playbook.status = "FAILED", 1, 0))
  $Percentage = math.round(($PlaybookError / $Total_Playbook_Runs) * 100, 2)
Automation distribution by environment
The following example breaks down playbook executions by environment and trigger type (automatic compared to manual) to ensure automation coverage is balanced:
$Automatic = playbook.metadata.automatic
$Environment = playbook.metadata.environments

match:
  $Environment, $Automatic

outcome:
  $Total_playbook_Runs = count(playbook.name)

order:
  $Total_playbook_Runs desc
Rules
Rule health and management metrics provide insights into rule performance, authorship trends, and operational status.
The following templates demonstrate how to query rules to visualize the performance, detection volume, and operational status of your custom and system detection logic:
Data Source
:
Rules
Query Prefix
:
rules
(fields must be prefixed; for example,
rules.display_name
)
Time Interval
: No Time Limit
Schema reference
The following schema defines the fields available for monitoring detection rules. This data source provides the metadata necessary to manage rule lifecycles and evaluate the impact of specific detections on your security posture. Use this schema to identify high-volume rules, manage severity distributions, and audit active rule counts.
Field name (query ready)
Data type
Description
rules.name
String
Unique rule identifier (
ruleID
).
rules.display_name
String
Human-readable name of the rule.
rules.rule_text
String
The rule's logic or conditions in text form.
rules.alerting
Boolean
Indicates whether rule detections trigger alerts (
true
/
false
).
rules.live_status
String
Current operational state of the rule, such as
ENABLED
or
DISABLED
.
rules.author
String
The creator of the rule.
rules.severity
String
Severity level assigned to the rule (for example,
CRITICAL
,
HIGH
,
LOW
).
rules.metadata
String/Map
Additional details, such as description,
mitre_attack_tactic
,
mitre_attack_technique
, and
mitre_attack_url
.
rules.total_detection_count
Integer
Total detections generated by the rule across its lifetime.
rules.create_time
Timestamp
Rule creation timestamp in
google.protobuf.Timestamp
format.
rules.update_time
Timestamp
Latest rule update timestamp in
google.protobuf.Timestamp
format.
rules.latest_detection_time
Timestamp
Timestamp of the most recent rule detection.
rules.earliest_detection_time
Timestamp
Timestamp of the first rule detection.
rules.archived
Boolean
Indicates whether the rule is archived (
true
/
false
).
Query examples
The following queries help security engineers optimize their detection strategy by surfacing rule activity and identifying "noisy" or highly effective logic. These examples bridge the gap between rule metadata and active detections, letting you rank your top-performing detections and identify which rules contribute most to your alert volume.
Top 10 active rules
The following example ranks rules by the number of unique detections they have generated:
$Rulename = detection.detection.rule_name

match:
  $Rulename

outcome:
  $Count = count_distinct(detection.id)

order:
  $Count desc

limit:
  10
Rules created per month
The following YARA-L query retrieves the rules created per month:
$month_wise = timestamp.get_timestamp(rules.create_time.seconds,"%y-%m")

match:
    $month_wise

outcome:
    $rule_count = count(rules.name)
Identify rule detection count
The following YARA-L query retrieves the rules with detection:
$rule_name = rules.display_name
$detection_count = rules.total_detection_count
$detection_count >0

match:
   $rule_name, $detection_count
Monitor rule status
The following YARA-L query retrieves the rules in
ENABLED
status:
$status = rules.live_status
$status = "ENABLED"

outcome:
 $rule_count = count(rules.name)
Analyze rule velocity by author
The following YARA-L query retrieves the rules created
by day
(by
author
):
$rule_author = rules.author

match:
 $rule_author by day

outcome:
 $count_of_rules = count(rules.name)

order:
   $count_of_rules desc
Retrieve rules with
text
and
time
query
The following YARA-L query retrieves the all rules
text
and
time
query:
$name= rules.name
$display_name = rules.display_name
$author = rules.author
$severity = rules.severity
$live_status = rules.live_status
$alerting_status = rules.alerting
$detection_time = rules.latest_detection_time.seconds
$latest_version_time = rules.update_time.seconds
$detection_count = rules.total_detection_count
$rule_text = rules.rule_text

match:
   $name, $display_name, $live_status, $alerting_status, $severity, $author, $detection_time, $latest_version_time, $detection_count, $rule_text

order:
 $detection_count desc
Identify non-triggering rules
The following YARA-L query retrieves the non-triggering rules (rules with no (
0
) detections):
$rule_name = rules.name
$display_name = rules.display_name
$detection_time = rules.latest_detection_time.seconds
$detection_time = 0

match:
      $rule_name, $display_name
For more information about field descriptions in the following examples, see
Rule fields
.
Rule sets
The following templates demonstrate how to query
rule sets
(
curated detections
) to visualize the health, status, and coverage of your detection content.
Data Source
:
Rule Sets
Query Prefix
:
ruleset
(fields must be prefixed; for example,
ruleset.ruleset_family
)
Time Interval
: 365 days
Schema reference
The following schema defines the fields used to monitor curated detections. This data source provides visibility into which rule families are active and whether they're configured for broad observation or precise alerting. Use this schema to map detection coverage across different threat families like "Cloud Threats" or "Linux Threats".
Field name (query ready)
Data type
Description
ruleset.ruleset_family
String
Family name of the rule set.
ruleset.ruleset
String
Display name of the rule set.
ruleset.broad_live
String
Status of live broad rules (for example,
ENABLED
,
DISABLED
).
ruleset.broad_alerting
String
Alerting status of broad rules within the rule set.
ruleset.precise_live
String
Status of precise rules (for example,
ENABLED
,
DISABLED
).
ruleset.precise_alerting
String
Alerting status of precise rules within the set.
ruleset.detection_timestamp
Timestamp
Specific timestamp when a detection event was triggered.
Query examples
The following queries let detection engineers audit their security posture by analyzing the deployment of curated detections. These examples focus on deployment health (calculating the percentage of enabled rule sets) and detection coverage, which tracks the most recent activity across different rule types. Use these examples to make sure your detection coverage remains aligned with your organizational threat model, specifically for high-priority families like Cloud Threats.
CDIR rulesets enabled
The following example calculates the percentage of rule sets within the "Cloud Threats" family that have both precise and broad live modes enabled:
ruleset.ruleset_family != ""
ruleset.ruleset_family = "Cloud Threats"
ruleset.precise_live = "ENABLED"
ruleset.broad_live = "ENABLED"

$rule_name = ruleset.ruleset

outcome:
  $total_ruleset_count = count_distinct(ruleset.ruleset)
  $ruleset_count = count_distinct(if(ruleset.ruleset_family = "Cloud Threats" and ruleset.precise_live = "ENABLED" and ruleset.broad_live = "ENABLED", ruleset.ruleset, "0"))
  $percentage = $ruleset_count / $total_ruleset_count * 100
Detection coverage
The following example lists rule sets in the
"Cloud Threats"
family and ranks them by their detection frequency and the time of their most recent detection:
$ruleset = ruleset.ruleset
$precise_live = ruleset.precise_live
$precise_alerting = ruleset.precise_alerting
$broad_live = ruleset.broad_live
$broad_alerting = ruleset.broad_alerting

ruleset.ruleset_family = "Cloud Threats"
timestamp.get_timestamp(ruleset.detection_timestamp.seconds) != ""

match:
  $ruleset, $precise_live, $precise_alerting, $broad_live, $broad_alerting

outcome:
  $latest_detection = timestamp.get_timestamp(max(ruleset.detection_timestamp.seconds))
  $count = count_distinct(ruleset.detection_timestamp.seconds)

order:
  $count desc
What's next
Learn more about how to use functions to build dashboards using
YARA-L 2.0 functions for Google Security Operations dashboards
.
