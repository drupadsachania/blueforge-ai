# Dashboard filters

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters/  
**Scraped:** 2026-03-05T10:09:38.120745Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Dashboard filters
Supported in:
Google secops
SIEM
This document explains how you can apply filters to data source fields to refine the data displayed in applicable charts.
Add a filter
To add a filter, do the following:
On the
Edit Dashboard
page, click
filter_alt
Filter
to add a filter.
On the
Manage filters
window, click
add
Add
to add a new filter.
In the
Field to filter
field, enter the field you want to use to filter
the data. For more information about supported data sources and fields,
see
Supported data sources
.
In the
Filter name
field, enter a name for the filter.
In the
Apply to field
, select the charts where the filter should be applied.
Optional: Set a default value for the filter.
Click
Done
to add the filter and close the
Manage filters
window.
Manage the global time filter
The global time filter applies to all charts, regardless of the chart's
data source
.
To select the charts for which the global time filter can be applied, do the following:
On the
Edit Dashboard
page, click
filter_alt
Filter
to add a filter.
On the
Manage filters
window, select
Global time filter
from the filters list.
Click the toggle to ensure that the global time filter is enabled.
In the
Apply to
field, select the charts to apply the global time filter.
In the
Set default values
field, set a time range to view data, using
either absolute or relative values..
Click
Done
to enable the filter and close the
Manage Filters
window.
Apply a dashboard filter
To apply a filter, do the following:
On the
Edit Dashboard
page, click
Back
>
filter_alt
Filter
to view the dashboard filters.
On the
Dashboard filters
window, select the filter you created.
Enter a value for the selected field.
Click
Apply
. The charts for which the filter is applicable are refreshed with new data.
Change the global time filter
When you open a dashboard, the global time filter is applied on
the applicable charts with the default time range.
To change the global time filter value, do the following:
Click
schedule
Schedule
.
In the
Global Time Filter
dialog, select either the
past
or
between
operator.
Select the date range.
Click
Apply
. The selected charts update with new data based on the global time filter.
Need more help?
Get answers from Community members and Google SecOps professionals.
