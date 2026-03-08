# Collect Google SecOps SOAR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/collect-secops-soar-logs/  
**Scraped:** 2026-03-05T09:15:34.272811Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google SecOps SOAR logs
Supported in:
Google secops
You can manage and monitor Google Security Operations SOAR logs in the
Google Cloud Logs Explorer
. You can
also use Google Cloud tools to set up special metrics and alerts
that are triggered by specific events in your SOAR operation logs.
The logs capture essential data from SOAR's
ETL
,
playbook
, and
Python
functions.
The types of captured data include the running of Python scripts, alert
ingestion, and playbook performance.
Enable SOAR log collection
Google SecOps provides operational logs for SOAR activities,
including playbook executions, connector runs, and Python script outputs.
Google SecOps (SIEM + SOAR Unified):
Collection of SOAR logs is enabled by
default. The platform automatically configures log sinks to route these logs to 
Cloud Logging in your Google Cloud project. No manual configuration is
required.
SOAR Standalone:
You must manually configure a service account and provide
the credentials to Google SecOps Support to enable log export.
For more information, see
Setup SOAR logs
.
Access Google SecOps SOAR logs
Google SecOps SOAR logs are written in a separate namespace called
chronicle-soar
and are categorized by the service which generated the log.
To access Google SecOps SOAR logs, do the following:
In the Google Cloud console, go to
Logging
>
Logs Explorer
.
Select the Google SecOps Google Cloud project.
Enter the following filter in the field and click
Run Query
:
resource.labels.namespace_name="chronicle-soar"
To filter logs from a specific service, enter the following filters in the box
and click
Run Query
:
resource.labels.namespace_name="chronicle-soar" 
    resource.labels.container_name="<container_name>"
where the values include
playbook
,
python
or
etl
.
Playbook step debugging
You can view execution logs for an individual playbook step directly from the
Playbook tab in the Cases page. This lets you inspect the logic and outcome of every step,
regardless of its execution status.
To view logs for a specific step:
In the
Case View
, open the
Playbook
tab.
Select a step to view its results.
Click
View Logs Explorer
.
The link opens the
Logs Explorer
in the Google Cloud console with a
pre-configured filter for the specific execution ID of that step.
Playbook labels
Playbook log labels provide a more efficient and convenient way to refine a query
scope. All labels are located in the labels section of each
log message:
To narrow the log scope, expand the log message, right-click each label, and 
hide or show specific logs:
The following labels are available:
playbook_definition
playbook_name
block_name
block_definition
case_id
correlation_id
integration_name
action_name
Python logs
The following logs are available for python service:
resource.labels.container_name="python"
Integration and Connector labels:
integration_name
integration_version
connector_name
connector_instance
Job labels:
integration_name
integration_version
job_name
Action labels:
integration_name
integration_version
integration_instance
correlation_id
action_name
ETL logs
The following logs are available for ETL service:
resource.labels.container_name="etl"
ETL labels:
correlation_id
For example, to provide the ingestion flow for an alert, filter by
correlation_id
:
Need more help?
Get answers from Community members and Google SecOps professionals.
