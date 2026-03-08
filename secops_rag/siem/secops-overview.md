# Google SecOps overview

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/secops-overview/  
**Scraped:** 2026-03-05T09:14:18.830475Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Google SecOps overview
Supported in:
Google secops
Google Security Operations is a cloud service, built as a specialized layer on
top of Google infrastructure, designed for enterprises to privately retain,
analyze, and search the large amounts of security and network telemetry they
generate.
Google SecOps normalizes, indexes, correlates, and analyzes the data to
provide instant analysis and context on risky activity. Google SecOps can
be used to detect threats, investigate the scope and cause of those threats, and
provide remediation using prebuilt integrations with enterprise workflow,
response, and orchestration platforms.
Google SecOps lets you examine the aggregated security
information for your enterprise going back for months or longer. Use
Google SecOps to search across all of the domains accessed within your
enterprise. You can narrow your search to any specific asset, domain, or IP
address to determine if any compromise has taken place.
The Google SecOps platform enables security analysts to
analyze and mitigate a security threat throughout its lifecycle by employing the
following capabilities:
Collection
: Data is ingested into the platform using forwarders, parsers, OpenTelemetry collectors, connectors, and webhooks.
Detection
: This data is aggregated, normalized using the Universal Data
Model (UDM), and linked to detections and threat intelligence.
Investigation
: Threats are investigated through case management, search,
collaboration, and
context-aware
analytics
.
Response
: Security analysts can respond quickly and provide resolutions
using automated playbooks and incident management.
Data collection
Google SecOps can ingest numerous security telemetry types through a
variety of methods, including the following:
Forwarder
: A lightweight software component, deployed in the customer's
network, that supports syslog, packet capture, and existing log management
or security information and event management (SIEM) data repositories.
Collector
: A software component, deployed in the customer's network, that supports many data sources routing to Google SecOps.
Ingestion APIs
: APIs that enable logs to be sent directly to the
Google SecOps platform, eliminating the need for additional
hardware or software in customer environments.
Third-party integrations
: Integration with third-party cloud APIs to
facilitate ingestion of logs, including sources like Office 365 and Azure
AD.
Threat analysis
The analytical capabilities of Google SecOps are delivered as a 
browser-based application. Many of these
capabilities are also accessible programmatically through Read APIs.
Google SecOps gives analysts a way, when they see a potential threat, to
investigate further and determine how best to respond.
Summary of Google SecOps features
This section describes some of the features available in
Google SecOps.
Search
UDM Search
: Lets you find Unified Data Model (UDM) events and alerts
within your Google SecOps instance.
Raw Log Scan
: Search your raw unparsed logs.
Regular Expressions
: Search your raw unparsed logs using regular
expressions.
Case management
Group related alerts into cases, sort and filter cases queue for triage and
prioritization, assign cases, collaborate on every case, case audit and
reporting.
Playbook designer
Build playbooks by selecting predefined actions and dragging and dropping them
into the playbook canvas without additional coding. Playbooks also enable you to
create dedicated views for each alert type and each SOC role. Case management
presents only the data relevant to a specific alert type and user role.
Graph investigator
Visualize the who, what, and when of an attack, identify opportunities for
threat hunting, capture the full picture and take action.
Dashboard and reporting
Effectively measure and manage operations, demonstrate value to stakeholders,
track real-time SOC metrics and KPIs. You can use built-in dashboards and
reports or build your own.
Integrated development environment (IDE)
Security teams with coding skills can modify and enhance existing playbook
actions, debug code, build new actions for existing integrations, and create
integrations that are not available in the Content Hub.
Investigative views
Asset view
: Investigate assets within your enterprise and whether or not
they have interacted with suspicious domains.
IP Address view
: Investigate specific IP addresses within your
enterprise and what impact they have on your assets.
Hash view
: Search for and investigate files based on their hash value.
Domain view
: Investigate specific domains within your enterprise and
what impact they have on your assets.
User view
: Investigate users within your enterprise who may have been
impacted by security events.
Procedural filtering
: Fine tune information about an asset, including by
event type, log source, network connection status, and Top Level Domain
(TLD).
Highlighted information
Asset insight blocks highlights the domains and alerts that you might want
to investigate further.
Prevalence graph shows the number of domains an asset has connected to over
a specified time period.
Alerts from other popular security products.
Detection engine
You can use the Google SecOps Detection Engine to automate the process of
searching across your data for security issues. You can specify rules to search
all of your incoming data and notify you when potential and known threats appear
in your enterprise.
Access control
You can both employ predefined roles and configure new roles to control access
to classes of data, alerts, and events stored within your Google SecOps
instance.
Identity and Access Management
provides access control for
Google SecOps.
Need more help?
Get answers from Community members and Google SecOps professionals.
