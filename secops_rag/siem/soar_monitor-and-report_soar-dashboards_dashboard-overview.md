# SOAR Dashboards overview

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/dashboard-overview/  
**Scraped:** 2026-03-05T09:36:38.146468Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
SOAR Dashboards overview
Supported in:
Google secops
SOAR
This document describes the
SOAR Dashboards
page in Google Security Operations, how you can manage these dashboards, and provides an overview of specified
data through the dashboard, including the various widgets. 
These widgets can show data for any specified SOC environment or case occurrence
time. A dashboard can hold up to 12 widgets, which display data in formats, such
as pie charts, bars, and tables. To display data related to your SOC status,
you can
add SOAR dashboard widgets
.
Monitor activity with predefined dashboards
Google SecOps provides the following predefined, customizable
dashboards to help you monitor and report SOC activities:
Playbooks dashboard
: Overview of playbook 
performance, including overall status, distribution, alert handling, and runtime 
metrics.
SOC Status
: Overview of the SOC's current state, 
highlighting important metrics for cases, alerts, incidents, and analyst 
activities.
Customize dashboards by data
You can customize a dashboard's display data by grouping widgets based on criteria, such as:
Analysts or playbooks associated with the case
Products or involved entities
Important or unimportant cases
You can filter the displayed data by applying built-in filters, such as tags, case status, case priority, case stage, and case close reasons.
Use-case: Add a new widget to a new dashboard
This section provides the steps for adding a
  new widget to a new dashboard. The widget provides a pie chart, (default format) showing
  the top five products that contribute to attacks across all environments in the
  last six months. This presentation is ordered by the number of attacks in
  descending order. No filters are applied in this example.
Go to
Dashboards & Reports
>
SOAR Dashboards
.
Click
filter_alt
Filter
and set the time to
Last 6 Months
and the environment as
All Environments
.
Click
keyboard_arrow_down
View all dashboards
and select
add
Create New Dashboard
.
Enter
Attacks
as the new dashboard name and click
Create
.
In the new dashboard, click
add
Add
.
In the
Widget Settings
dialog, enter
Top 5 Attacks by Products
as the title.
Select
Widget Width
.
In the data display,
Pie Chart
is set by default. Keep this setting.
Configure the
Pie Chart
fields as follows:
Number of
: Alerts
Calculate field
: Count
Group by
: Product
Number of Results
: 5
Order by
: Descending
Click
Save
.
The new widget is added to the dashboard as
Attacks
.
The pie chart displays the top five products associated with attacks across all environments in the last six months.
Need more help?
Get answers from Community members and Google SecOps professionals.
