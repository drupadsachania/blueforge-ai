# Use Looker Explores in SOAR reports

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-reports/using-looker-explores-in-soar-reports/  
**Scraped:** 2026-03-05T10:09:53.191604Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use Looker Explores in SOAR reports
Supported in:
Google secops
SOAR
Looker Explores are interactive data analysis tools in Google Security Operations that let you build custom reports and visualizations without writing complex code. They serve as the foundation for advanced reporting, providing a flexible way to analyze your security data. This document does not provide information about how to create and edit Looker Explores. For details on Explores, see
Create and edit Looker Explores
.
For a comprehensive reference of the underlying data fields and column names
  used in these reports, see
Siemplify Search Everything database
.
Explore advanced SOAR reports
You can find Looker Explores in the Advanced SOAR Reports tab, each providing specialized data and visualization capabilities that can be used to build advanced reports.
The default advanced SOAR reports are a set of dashboards and reports to help
track SOC performance, case handling, analyst workload, and automation
efficiency. These reports provide both high-level and detailed insights across
your environments, supporting use cases from daily monitoring to executive-level
summaries.
Many reports require specific flags or configurations to ensure accurate
data, which are noted in each description.
This section describes these commonly used reports. Each report includes
visual dashboards that support data-driven decisions and continuous SOC
improvement. Performance about key reports follows the table.
Report Type
Description
Alerts and Entities
Monitors and analyzes entities, alerts, cases, and incidents. It
provides key metrics and filtering options to help you understand
your security data. You can:
Monitor metrics like case count, average handling time, and
incident count.
Filter data using dimensions such as case priority, stage, and
root cause.
Track case handling efficiency through time-based measures like
handling time and SLA status.
Identify incidents in cases
:
Use the
Incident
flag to identify incidents in
cases.
Analysts Case Load Tracker
Shows the workload distribution across analysts at a given time,
helping you monitor staffing and performance in your SOC.
Workload Analysis:
Visualize and analyze
caseloads by tracking the time of day and the day of the week.
Performance Monitoring:
Monitor performance
across different time periods.
Individual Tracking:
Track each user's workload
per day, week, and month.
Cases
Monitors and analyzes cases from creation to closure. It
provides comprehensive details to help you track the entire case
lifecycle. You can:
Search for key dimensions, such as case priority, status, stage,
environment, and close reason.
Track metrics, such as case counts, Mean Time to Assignment
(MTTA), and Mean Time to Resolution (MTTR).
View user and assignee details, including their roles and email,
along with assignment start dates.
Cases and Alerts
Combines case and alert data to help you analyze how security
events are processed into cases, including:
Key Dimensions
: Filter by case priority, stage,
root cause, alert rule name, and product.
Filter Options
: Filter by playbook actions and
incident status.
Measures
: Use case and alert counts to gain
insight into the flow of security incidents.
Case History
Tracks the entire lifecycle of cases, providing a detailed
analysis of case handling efficiency and process timelines.
Lifecycle Tracking:
Follow cases from stage
transitions to analyst assignments.
Detailed Insights:
Analyze time-based metrics
across various phase combinations.
Filter Capabilities:
Filter cases by name,
priority, status, and environment.
Customer Report
A summary dashboard that offers a high-level view of SOC
coverage across key operational areas.
Prerequisites
:
Use the
Mark as Important
flag to identify important cases.
Use the
Incident
flag to identify incidents.
Define SLA targets for case closure.
All non-malicious cases are considered false positives.
Executive Dashboard
Designed to monitor key performance indicators (KPIs), this
dashboard summarizes incident counts, resolution times, SLA
compliance, and other key metrics.
Prerequisites
:
Use the Incidents flag to identify incidents.
Define SLA targets for case closure.
Escalated cases must be identified using the
Stage Escalated
flag.
Managed Detection Response
Ideal for daily, weekly, or monthly reporting. Tracks alerts,
case creations, triage, resolution, and SLA data in a compact format,
such as:
SLA Monitoring:
Use
Triage Time
and
SLA Met
flag to monitor SLA compliance and improve
case handling.
Prioritization and Review:
Use
Case
Priority
and
Close Case Root Cause
to prioritize
cases and review closures.
Prerequisites
:
Use the
Stage Escalated
flag for identifying
escalated cases.
Triage time is defined as the time a case is acknowledged.
Monthly Threat Monitoring
A monthly summary of alerts, affected products, alert
severities, and other key indicators.
MTTX Dashboard
A time-tracking dashboard designed to show elapsed time between
key case lifecycle stages—from creation to the start and end of
specific incident handling phases. You can customize parameters, such
as
stages
and
timestamps
.
Analyst Workload Report
Visualizes SOC workload metrics, such as alert and event
distributions, open and closed case trends, alert grouping
performance, and false positive trends. See
performance
details
.
Performance Handling Times Report
Tracks mean time to detect (MTTD) and mean time to remediate
(MTTR) across various dimensions such as teams, alert types, and
response stages, offering insight into operational efficiency. See
performance details and
examples
.
Playbook Analysis Report
Measures automation effectiveness and highlights how
playbook-based actions improve SOC performance and reduce handling
times. See
performance
details
.
ROI Report
A single-page dashboard that quantifies the time and effort
saved through automation. It includes a breakdown of automated versus
manual actions and their distribution across products.
Security Operations Center Report
Built for clients managing multiple tenants (for example,
MSSPs), this report supports tenant switching and flexible time
filtering. Its concise charts are well suited for weekly or monthly
summaries.
Security Posture and Sensors Performance
Report
Provides visibility into threat trends and sensor performance
over time, helping identify false positives and fine-tune sensor
configurations. See
performance
details
.
Overall Clearance Tracker tier performance
This
dashboard tracks case volume and resolution across different tiers in
your SOC.
Tier Performance
Analyzes the efficiency of any
SOC Role
categories by tracking alert counts over a specified time
period.
Key Dimensions:
Use
SOC Role
Name
and
Environment
to filter and assess team
performance.
Metrics:
Track the number of alerts created,
closed, and pending to gain insight into workload distribution and alert
management.
View Dashboard Cases
Provides a comprehensive view of case management and performance
that combines case, alert, entity, stage progression, and analyst
assignment details. This view supports in-depth analysis using
tag-based dimensions and metrics. This Explore offers a wide range of
performance tracking KPIs and detailed search options,
including:
Search dimensions
: Case Priority, Case Closed
Reason, First/Last Handling Analyst, Alert Rule Name, and Product.
KPIs
: Automatically/Manually Closed Cases,
Average Detection Time, Average Handling Time, Average Remediation Time,
and Case Summary by Priority.
Explore performance analysis for advanced SOAR reports
Each report includes visual dashboards that support data-driven decisions and
continuous SOC improvement.
Performance Handling Times report
This report highlights how long cases spend at various stages of the response
lifecycle. It includes metrics, such as mean time to detect (MTTD), mean time to
remediate (MTTR), and average handling time by SOC role or stage. These insights
help teams identify delays, assess operational efficiency, and improve case
triage and remediation workflows.
Mean time to detect (MTTD)
: The average time from case creation until the case is assigned to a user.
Format:
days-hours-minutes-seconds
The widget displays
0
if the case
is not assigned.
Mean time to remediate (MTTR)
: The average time from case
creation until it moves to the remediation stage.
Format:
days-hours-minutes-seconds
The widget displays
N/A
if no remediation stage exists.
Avg. Handling time by SOC role
: Shows the average time a SOC
role spends on a case from assignment to either closure or
reassignment.
Avg. handling time by stage
: Displays the average time spent
in each stage, from the moment a stage begins until the case is
either closed or moves to a different stage.
Mean time to triage
: Displays the average handling time for
the Triage stage by date across different rules
Avg. handling time triage stage
: Displays the average handling time of the triage stage by
date.
Avg. handling time per SOC role per date
: Displays the average handling time per SOC role by date.
Analyst Workload report
The
Analyst Workload
report provides visibility into how
alerts, events, and cases are distributed across rules and how they impact SOC
analyst workload. It helps identify trends in alert volume, case status, false
positives, and time spent on handling cases—enabling teams to optimize staffing,
rule tuning, and response efficiency.
Alert distribution across rules:
Displays the
distribution and percentage of alerts per rule type.
Event Distribution across rules:
Displays the percentage of
events per rule type.
Open vs. closed cases:
Displays the distribution of the
number of open and closed cases.
Cases vs. alerts:
Displays the distribution between the
number of cases and alerts.
False positives vs. handling time:
A dual-axis graph
displays the
false positive
rate compared to the average handling time.
The false positive rate is the percentage of non-malicious cases out of
all cases.
The
average handling
time measures the duration from case creation
to case closure.
The graph displays information for closed cases only.
Security Posture and Sensors Performance report
The
Security Posture and Sensors Performance
report focuses
on the effectiveness of detection rules and security sensors across your
environment. It shows how alerts are distributed by rule and product, tracks
alert volume over time, and visualizes false positive rates. These insights help
evaluate detection coverage, identify noisy rules or underperforming products,
and fine-tune your security posture.
% of alerts by Rule:
Displays the distribution and
percentage of alerts by rule type.
Number of alerts by rule by Date:
Displays the number of
alerts by rule type over time.
% of alerts by product:
Displays the distribution and
percentage of alerts by product.
Number of alerts by product by date:
Displays the number of
alerts by product by date.
False positive rate vs. product:
Displays the false
positive rate by product type.
The false positive rate is the percentage of non-malicious cases out of
all cases.
The graph displays information about closed cases only.
Playbook Analysis
The
Playbook Analysis
report evaluates the effectiveness of
automation through playbooks. It highlights the most frequently automated
alerts, the top alerts closed by automation, and compares false positive rates
and handling times for alerts with and without playbook automation. Use these
insights to assess the impact of automation on case resolution and identify
opportunities to expand playbook coverage.
Top 10 automated alerts:
Displays the top 10 rules
with the highest percentage of automated alerts.An automated alert is one that
is linked to a playbook automatically.
Top 10 alerts closed by automation:
Displays the top 10
rules with the highest percentage of alerts that were automatically closed by a
playbook. The graph displays information for closed cases only.
False positives vs. handling time for non automated alerts:
For alerts without an automatically attached playbook, this widget has a
dual-axis graph that displays the false positive rate compared to the average
handling time.
The graph displays information about closed cases only.
This graph includes data for closed cases only and will be empty if there
are no alerts without playbooks.
Manage advanced SOAR reports in Looker
Assign access and permissions
On the
Permissions
page, you can assign users these
permissions:
View
: Select the
View Advanced
Reports
checkbox to grant access to view reports in the
Advanced Reports
tab.
Edit
: Select the
Allow editing Advanced
reports
checkbox to grant access to create, edit, duplicate, share,
download, and delete advanced reports.
Advanced reports
are accessible to all platform users
through the
Reports
tab without any prior setup.
Manage advanced reports
The following folders in the
Advanced Reports
tab are
available:
Default (Admins only)
: Predefined reports that can't
be edited directly. However, you can duplicate them into a different folder for
editing.
Personal
: Reports that you create yourself using the Looker
components. You can also duplicate and save reports from the
Default
or
Shared
folders.
Shared
: Reports that you created and shared with others or
that others created and shared with you.
You can manage your advanced reports by sharing them with other users,
duplicating them into different folders or environments, or renaming reports
you've created or copied. This section describes how to perform these actions in
the
Advanced Reports
interface.
Share reports
Click
share
Share
.
Select the environments to share the report with.
Optional: Check the corresponding box to grant view-only users access.
Duplicate reports
Click
content_copy
Duplicate Report
.
Select the destination folder and the required environments.
Optional: Rename the duplicated report.
Rename Looker reports
You can only rename reports that you've duplicated, located in your personal
or shared folder.
Open the report you want to rename.
Click
more_vert
Dashboard actions
, and select
Edit dashboard
.
Click in the report name field, enter a new name, and click
Save
.
Use custom fields in advanced reports
You can use custom fields created in Google SecOps within advanced reports to
gain deeper insights into your cases and alerts. To learn how to use custom
fields in Looker reports, including LookML formulas and filtering techniques,
see
Manage
custom fields
.
Create a report with SOAR Explores
SOAR Explores let you define and visualize specific data by selecting the
relevant fields. While similar to standard Looker dashboards, SOAR Explores
include additional SOAR-specific fields. For more information, see
Add
a chart visualization to a dashboard
.
To create a report using SOAR Explores, follow these steps:
Go to
Dashboards and Reports > SOAR Reports
.
Click
Advanced Reports
.
Click
add
Add report
.
In the
Create new report
dialog, enter a name for the
report, select a folder, and choose an environment.
Click
Create
and display the new report.
Select the report and click
Edit Dashboard
.
Click
Add
, located under the report name.
In the list, select
Visualization
.
In the
Choose an Explore
dialog, choose the relevant SOAR
Explore to access data fields specific to your report.
In the
All Fields
tab, select the dimensions and measures
relevant to your report.
Customize the report as needed and click
Save
. The
visualization tile is added to the dashboard.
Note:
To edit each dashboard tile, click
Edit
in the tile from the dashboard.
Troubleshooting tips
The following error may appear on the
Advanced reports
page:
You are not authenticated to view this page.
If you're authenticated and see this error, your browser may be blocking
Looker cookies.
The method to enable Looker cookies depends on your browser.
To enable Looker cookies and access the
Advanced
reports
page in Google Chrome, follow these steps:
Right-click anywhere on the page and select
Inspect
.
Click one of the reports and copy the URL to your clipboard.
In Chrome, go to
Settings > Privacy and Security > Third-party
cookies
.
In
Allowed to use third-party cookies
, click
Add
and paste the Looker URL.
You should now be able to access and view the advanced reports.
Known issues and limitations
SOAR advanced reports have the following known issues and limitations:
Deleting reports
: The
Move to trash
option in the
Dashboard actions
menu doesn't work. To delete a
report, click
Delete Report
above the report.
Test now in scheduled delivery
: The
Test
now
action doesn't function. To test report delivery, click
Send now
in the
Schedules
dialog.
Merge queries limitation
: Reports using the
Merge
queries
action can't be exported or imported.
Need more help?
Get answers from Community members and Google SecOps professionals.
