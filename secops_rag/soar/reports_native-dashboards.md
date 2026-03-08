# Dashboards overview

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards/  
**Scraped:** 2026-03-05T10:09:29.881245Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Dashboards overview
Supported in:
Google secops
SIEM
This document provides a technical guide for using the Google Security Operations Dashboards engine to construct data visualizations across disparate telemetry streams.
The Dashboards framework is built on a modular architecture where individual widgets (charts) interface with specific data sources using the YARA-L 2.0 syntax. By using the YARA-L schema properties and aggregation functions, you can build visualizations for real-time monitoring, threat analysis, and operational auditing.
For a deeper dive into the underlying dashboard infrastructure, see the
Dashboards overview
.
Before you begin
Confirm that your Google SecOps instance meets the following configuration requirements:
Configure a Google Cloud project
or migrate your Google SecOps instance to an
existing cloud project
.
Configure a
Google Cloud Identity provider
or
third-party identify provider (IdP)
.
Configure feature access control using Identity and Access Management
.
IAM permissions required
The following permissions are required to access dashboards:
IAM permission
Purpose
chronicle.nativeDashboards.list
View the list of all dashboards
.
chronicle.nativeDashboards.get
View a dashboard
,
apply a dashboard filter
, and
apply the global filter
.
chronicle.nativeDashboards.create
Create a new dashboard.
chronicle.nativeDashboards.duplicate
Make a copy of an existing dashboard.
chronicle.nativeDashboards.update
Add and edit charts
,
add a filter
,
change dashboard access
, and
manage the global time filter
.
chronicle.nativeDashboards.delete
Delete a dashboard
.
Understand dashboards
Dashboards provide insights into security events, detections, and related data.
This section outlines the supported data sources and explains how role-based access
control (RBAC) affects visibility and data access within the dashboards.
investigation
response_platform_info
case_name
feedback_summary
feedback_history
soar_alert
soar_alert_metadata
Data sources supported
Dashboards include the following data sources, each with its corresponding YARA-L prefix:
Data source
Query time interval
YARA-L prefix
Schema
Dashboard examples
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
Impact of data RBAC
Data role-based access control (RBAC) is a security model that uses
individual user roles to restrict user access to data within an organization.
Data RBAC lets administrators define scopes and assign them to users, ensuring
access is limited to only the data necessary for their job functions.
All queries in dashboards follow data RBAC rules.
For more information about access controls and scopes, see
Access controls and scopes in data RBAC
.
For more information about data RBAC for dashboards, see
Configure data RBAC for dashboards
Events, entity graph, and IOC matches
The data returned from these sources is restricted to the user's assigned access scopes, ensuring that they only see results from authorized data.
If a user has multiple scopes, queries include data from all assigned scopes.
Data outside the user's accessible scopes doesn't appear in dashboard search results.
Rules
Users can only see rules that are associated with their assigned scopes.
Detection and rulesets with detections
Detections are generated when incoming security data matches the criteria defined
in a rule. Users can only see detections that originate from rules associated with
their assigned scopes. The rulesets with detections are only visible to
global users
.
SOAR data sources
Cases and alerts, playbooks, and case history are only visible to
global users
.
Ingestion metrics
Ingestion components are services or pipelines that bring logs into the platform
from source log feeds. Each component collects a specific set of log fields
within its own ingestion metrics schema.
Administrators can use RBAC for ingestion metrics to
restrict visibility of system health data, such as ingestion volume, errors, and
throughput, based on a user's business scope.
The Data Ingestion and Health dashboard uses Data Access scopes. When a scoped
user loads the dashboard, the system automatically filters metrics to show only
data that matches their assigned labels.
You can filter using the following labels:
Namespace
: The primary method for segregation (for example,
Eu-Prod
,
Alpha-Corp
).
Log Type
: Role-based segregation (for example,
GCP_VPC_FLOW
,
CROWDSTRIKE_EDR
).
Ingestion Source
: Granular source tracking (for example, specific forwarder ID).
Limitations
Custom label
: Assigning a user scope that contains a custom label—such as a label created using UDM regular expression or
data tables—automatically disables RBAC for ingestion metrics for that
user. As a result, the user won't see any data in their dashboards. For
ingestion monitoring scopes, you must use only standard labels such as Log
Type, Namespace, and Ingestion Source.
Ingestion source Limitation
: Filtering by ingestion source applies only
to the Log Count metric. Charts displaying bandwidth (bytes) or error rates
metrics might show no data if filtered strictly by ingestion source. Google
recommends filtering by Namespace for broader health monitoring.
Advanced features and monitoring
To fine-tune detections and improve visibility, you can use advanced configurations, such as YARA-L 2.0 rules and ingestion metrics. This section explores these feature insights, helping you optimize detection efficiency and monitor data processing.
YARA-L 2.0 properties
YARA-L 2.0 has the following unique properties when used in dashboards:
Additional data sources, such as entity graph, ingestion metrics, rule sets,
and detections are available in dashboards. Some of these data sources are not yet available
in YARA-L rules and Unified Data Model (UDM) search.
See
YARA-L 2.0 functions for Google Security Operations dashboards
and aggregate functions that include statistical measures.
The query in YARA-L 2.0 must contain a
match
or an
outcome
section, or both.
The
events
section of a YARA-L rule is implied and does not need to be declared in queries.
The
condition
section of a YARA-L rule is not available for dashboards.
Dashboards don't support rules from the Risk Analytics for UEBA category.
Need more help?
Get answers from Community members and Google SecOps professionals.
