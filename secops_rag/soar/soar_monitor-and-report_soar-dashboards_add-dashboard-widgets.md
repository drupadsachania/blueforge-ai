# Add SOAR dashboard widgets

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/add-dashboard-widgets/  
**Scraped:** 2026-03-05T10:09:49.690441Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Add SOAR dashboard widgets
Supported in:
Google secops
SOAR
This document describes the Google Security Operations SOAR dashboard widgets you can use to display data
related to the status of your SOC, derived from cases, alerts, and playbooks.
Widgets help visualize key metrics—such as alert reduction, case prioritization,
and automation performance—directly within a SOAR dashboard. Each dashboard can
contain up to 12 widgets, which you can add based on your
monitoring needs.
By showing the percentage of alerts that have been grouped into cases, the widgets
demonstrate how
alert grouping
helps reduce the number of individual alerts that require investigation.
For example, the
Alert Reduction
widget shows the ratio of 
cases to alerts using this formula:
1 - ( Cases / Alerts ) * 100% 

If four alerts are grouped into three cases, the number of alerts requiring
investigation is reduced by 25%, as three grouped cases replace four individual alerts.
Add a widget to a SOAR dashboard
Go to
Dashboards & Reports
>
SOAR Dashboards
.
Click
add
Add Widget
.
In the
Widget Settings
dialog:
Enter a title for the widget (required).
The
Time
and
Environment
fields are auto-filled based on
    the dashboard settings.
Select a
Widget Width
.
Select the
Data Display Form
:
Pie chart
(default format)
Horizontal bar graph
Vertical bar graph
Table
On the side pane, specify fields relevant to the selected display form.
For example, if using a
Pie Chart
, configure:
Number of
Calculate field
Group by
Number of Results
Order by
For a
Table
, fields include:
Number of
Calculate field
Axis A
Axis B
In the
Filters
pane, select the data filters to apply:
The top 15 filters are shown by default.
Use the search bar to add filters not listed.
Click
Save
to add the widget to the dashboard with the specified display format, fields, and filters.
For details about the data display form and corresponding fields,
    see
View data display forms and fields
.
View data display forms and fields
Data Display Form
Fields
Pie Chart
Horizontal Bar Graph
Vertical Bar Graph
Number of
Calculate field
Group by
Number of Results
Order by
<tr>
  <td>
    Table
  </td>
  <td>
    <ul>
      <li>
        Number of
      </li>
      <li>
        Calculate field
      </li>
      <li>
        Axis A
      </li>
      <li>
        Axis B
      </li>
    </ul>
  </td>
</tr>
Number of
Group by fields
If you choose
Alerts
Entity Identifier
Environment
Network
Playbook
Product
Rule Name
If you choose
Cases
Analyst
Environment
Importance
Priority
Tag
Stage
If you choose
Playbooks
Playbook Name
Environment
Blocks
Need more help?
Get answers from Community members and Google SecOps professionals.
