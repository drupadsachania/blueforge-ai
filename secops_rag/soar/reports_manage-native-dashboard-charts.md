# Manage chart settings in dashboards

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts/  
**Scraped:** 2026-03-05T10:09:36.667347Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage chart settings in dashboards
Supported in:
Google secops
SIEM
This document explains how you can manage chart settings in dashboards.
A dashboard is composed of charts that are populated with data using YARA-L queries.
Charts on dashboards simplify complex data, revealing trends and patterns through
visuals. The chart type used depends on the data and required insights.
Add a chart
To add a chart to your dashboard, do the following:
On the
Edit Dashboard
page, click
Add chart
.
In the query editor, enter a YARA-L query to explore and transform your data.
You can also view and use previous queries from
History
, your saved search,
or queries that have been shared with you earlier.
Select an
Absolute
or
Relative
time range.
Click
Run Search
. The results display
in a tabular format, which serve as the default chart type.
In the
Chart details
, enter a name for the chart.
Optional: Click
Chart type
and select a chart type to change the format
of your tabulated search results. For more information about the available chart types, see
Chart types
.
Change the chart settings according to your requirements.
Review the results and then click
Add to Dashboard
.
Edit a chart
On the
Edit Dashboard
page, click
edit
Edit
on a chart to edit it.
In the query editor, modify the YARA-L query to explore and transform your data.
You can also view and use previous queries from your history, saved searches, or shared queries.
Modify the time range as required, and then click
Run Query
.
Change the chart settings according to your requirements.
Review the results and click
Save
to save the changes to the chart.
Delete a chart
To delete a chart, do the following:
On the
Edit Dashboard
page, click
more_vert
Menu
on
the chart you want to delete, and then click
Delete
.
Click
Confirm
to delete the chart.
Refresh a chart
You can refresh a chart to clear its cache and display the most recent data.
On the
Dashboards
page, click
autorenew
Refresh
to refresh the chart.
View a chart as a table
You can view any chart in table format to see its underlying data.
To view a chart as a table, do the following:
On the
Dashboards
page, click
more_vert
Menu
next to a chart, and then click
View as table
.
View a query
You can view a query for any chart in a dashboard to understand how its data is
generated and displayed. You can copy, run, or modify the query, as needed.
To view the query, do the following:
On the
Dashboards
page, click
more_vert
Menu
next to a chart, and then click
View query
.
Optional: Click
Run in Search
to run the query in
Search
.
Optional: Click
content_copy
Copy
to copy the query to clipboard.
Add a button
You can add buttons to a dashboard, and then use them to open a link.
For example, you can add a button that links to a third-party ticketing system.
To add a button, do the following:
On the
Edit Dashboard
page, click
Add
>
Button
.
In the
Create Button
dialog, enter a name for the button in the
Button label
field.
Enter a link that opens when you click the button.
Only
http://
and
https://
links are supported.
Optional: Select the
Open the link in new tab
checkbox to open the link in a new tab.
In the
Description
field, enter a button description.
Select
Button style
and
Button color
.
Click
Save
. The button will appear on the dashboard once the changes are saved.
Edit a button
To edit an existing button, do the following:
On the
Edit Dashboard
page, click
edit
Edit
on the button.
In the
Edit button
dialog, make the required changes.
Click
Save
. The button will appear on the dashboard once the changes are saved.
Make a copy of a button
To make a copy of a button, do the following:
On the
Edit Dashboard
page, click
content_copy
Copy
.
Delete a button
To delete an existing button, do the following:
On the
Edit Dashboard
page, select the button to delete and then click
edit
Delete
.
In the
Edit Button
dialog, click
Remove
>
Confirm
to
delete the button.
Add a Markdown widget
You can add a Markdown widget to your dashboard to display additional information
about a chart or dashboard.
To add a Markdown widget, do the following:
On the
Edit Dashboard
page, click
Add
>
Markdown
.
In the
New Markdown
dialog, enter text about your widget in the
Markdown content
box.
In the
Background color
list, select a background color for the widget.
Preview the text, and click
Save
.
Edit a Markdown widget
To edit a Markdown widget, do the following:
On the
Edit Dashboard
page, select a Markdown widget to edit, and click
edit
Edit
.
Modify the text as needed, and then click
Save
.
Delete a Markdown widget
To delete a Markdown widget, do the following:
On the
Edit Dashboard
page, click
more_vert
Menu
on
the Markdown widget you want to delete, and then click
Delete
.
Click
Confirm
to delete the Markdown widget.
Select a chart type
Visualizations help you quickly identify anomalies and trends. Choose the right
chart to visualize your data effectively. To create unique charts, consider your
audience and choose a chart type that best represents your data. Ensure your data is
correctly formatted, and use clear, concise labels for axes and legends.
Bar chart
Bar charts are useful for comparing categories of data or tracking changes
in quantitative data across multiple groups over time. Data points are plotted on
two axes with categories on one axis and values on the other. Bars can
be oriented vertically (column charts) or horizontally.
Line Chart
Line charts show trends or changes over a continuous interval, such as time, or an area chart to emphasize the volume of change.
The horizontal (X) axis represents the continuous interval, and the vertical (Y)
axis shows the quantitative variable. Data points are connected by lines, highlighting
change patterns. Key features include an emphasis on trends, comparing multiple data series, and analyzing continuous data.
Area graph
Area graphs similar to line charts, emphasize the magnitude of change over time.
They visualize trends and show the cumulative contribution of components to the
overall trend. The horizontal (X) axis represents the continuous interval, like time,
while the vertical (Y) axis shows the quantitative variable. The area between the
line and the X-axis is filled, highlighting value magnitude. Key features include
an emphasis on magnitude, the use of stacked area charts to show individual and
contributions over time.
Scatter plot
Scatter plots display the relationship between two quantitative variables,
revealing correlations, patterns, and distributions in bivariate data. One
quantitative variable is plotted on the horizontal (X) axis, and the other on
the vertical (Y) axis. Each data point appears as a dot, positioned according to
its values for both the variables. Key features include identifying correlations,
detecting patterns, and analyzing data distribution.
Chart configuration
The following table describes the common configuration options for bar charts,
line charts, area graphs, and scatter plots.
Field
Description
Name
Enter a descriptive name for the chart.
Description
Add a brief explanation of the chart's purpose.
X-axis
Choose the data field to display along the X-axis (horizontal axis).
Y-axis
Choose the data field to display along the Y-axis (vertical axis).
Threshold coloring
Click the toggle to activate the threshold coloring. This option automatically 
    adjusts the color of chart elements based on defined numeric conditions.
Enter minimum and maximum values.
Select a color for the threshold range.
Optional: Click
add
Add Threshold
to add more thresholds.
Display axis in log scale
Click the toggle to display the X-axis using a logarithmic scale.
X-axis label
Specify the label for the X-axis (horizontal axis).
Y-axis label
Specify the label for the Y-axis (vertical axis).
Legend
Select where to display the chart's legend. For example, Top, Bottom, Left, Right, None.
Drill downs
Click
Customize drill downs
to configure drill downs. For more
  information, see
Drill down in charts
.
Table chart
Table charts display detailed, structured data in rows and columns, providing
precise values and enabling comparisons across multiple dimensions. They
support sorting, filtering, and pagination to enhance data exploration and usability.
Field
Description
Name
Enter a descriptive name for the chart.
Description
Add a brief explanation of the chart's purpose.
Table settings
Add a label for the event variables.
Drill downs
Click
Customize drill downs
to configure drill downs. For more
  information, see
Drill down in charts
.
Pie chart
Pie charts show how a whole is divided into parts, effectively visualizing the
relative size of each category within a single dataset. They represent data as
slices of a circle, where each slice's size corresponds to its proportion of the
whole. You can use pie charts for a quick, visual understanding of part-to-whole relationships,
but limit them to datasets with few categories.
Field
Description
Name
Enter a descriptive name for the chart.
Description
Add a brief explanation of the chart's purpose.
Field of data
Select an appropriate event variable.
Value of data
Select an appropriate event variable.
Donut chart
Click the
Donut Chart
toggle to display the data in donut shape.
Threshold coloring
Click the toggle to activate the threshold coloring. Threshold coloring
    in dashboard charts automatically adjusts the color of data elements based
    on numeric conditions.
Enter minimum and maximum values.
Select an appropriate color for the threshold.
Optional: Click
add
Add Threshold
to add more threshold coloring.
Legend
Select where to display the chart's legend. For example, Top, Bottom, Left, Right, None.
Drill downs
Click
Customize drill downs
to configure drill downs. For more
  information, see
Drill down in charts
.
Metric chart
Metric charts provide a quick snapshot of key performance indicators by displaying a single,
prominent numerical value, often accompanied by a label and optional trend indicators
for context. They highlight a specific data
point for immediate insight, focusing on a single value to provide a clear and
concise understanding of critical metrics.
Field
Description
Name
Enter a descriptive name for the chart.
Description
Add a brief explanation of the chart's purpose.
Metrics data type
Select an appropriate event variable.
Metrics label
Enter a descriptive name for the label.
Threshold coloring
Click the toggle to activate the threshold coloring. Threshold coloring
    in dashboard charts automatically adjusts the color of data elements based
    on numeric conditions.
Enter minimum and maximum values.
Select an appropriate color for the threshold.
Optional: Click
add
Add Threshold
to add more threshold coloring.
Metric format
Specifies how the metric value is displayed on the chart.
Plain text
: Displays the metric value as raw, unformatted text.
Number
: Displays the metric value as a formatted number with separators.
Show trend of data
Specifies whether to display the data trend.
The trend compares the current time range to the immediately
    preceding period of the same duration. For example, if you select a time range
    of
last 7 days
(August 12-18), the trend is compared to August 5-11. Similarly, for an absolute time range
    like May 16-20, the trend is based on May 11-15.
Display trend
Displays the metric trend.
Absolute value
: Displays the actual numerical value of the metric.
Percentage
: Displays the trend value as a percentage.
Both
: Displays both the absolute value and the percentage of the trend.
Trend type
Specifies the type of trend to display.
Regular
: Default. Displays increasing values
        in green with an up arrow, and decreasing values in red with a down arrow.
Inverse
: Displays increasing values
        in red with an up arrow, and decreasing values in green with a
        down arrow.
Drill downs
Click
Customize drill downs
to configure drill downs. For more
  information, see
Drill down in charts
.
Map chart
Map charts visualize geographic data by plotting coordinates to reveal
spatial patterns and distributions. With interactive features like zooming and panning, they're ideal for displaying and analyzing location-based information.
Field
Description
Name
Enter a descriptive name for the chart.
Description
Add a brief explanation of the chart's purpose.
Latitude
Select an appropriate event variable.
Longitude
Select an appropriate event variable.
Field to count
Select an appropriate event variable.
Plot mode
Select an appropriate plot mode to plot individual geographic points in terms of latitude and longitude.
    You can select
Heatmap
,
Points
, or
Both
.
Map position
Click the toggle to fit the data. The map automatically adjusts its zoom level and
    center point to verify all plotted data points are visible within the current view.
Point settings
Select an appropriate option to select the point size either to
Fixed
or
Proportional to size
.
Color
Select an appropriate color for the point settings.
Drill downs
Click
Customize drill downs
to configure drill downs. For more
  information, see
Drill down in charts
.
Threshold coloring
Click the toggle to activate the threshold coloring. Threshold coloring automatically
    adjusts the color of plot points and other data elements in dashboard charts
    based on numeric conditions.
Enter minimum and maximum values.
Select an appropriate color for the threshold.
Optional: Click
add
Add Threshold
to add more threshold coloring.
Gauge chart
Gauge charts visually represent a single value within a defined range, using dials or
bars, to indicate performance or progress towards a target or threshold.
Field
Description
Name
Enter a descriptive name for the chart.
Description
Add a brief explanation of the chart's purpose.
Field of data
Select an appropriate event variable.
Gauge display value
Select an appropriate event variable.
Display data values
Click the toggle to display the data values.
Gauge configuration
Enter an appropriate value for
Base value
and
Limit value
.
Select an appropriate color for the
Limit value
.
Click
add
Add Range
to add
Threshold value
.
Drill down in charts
Drill downs let you click a specific data point or element within a dashboard
chart to access more granular or related information. This action moves
you from a high-level summary to a more detailed view. You can configure drill downs
for all chart types except Gauge charts.
Customize drill downs
You can configure a drill down to activate with either a left-click or a
right-click on the chart element.
To customize drill downs, do the following:
On the
Edit Dashboard
page, click
edit
Edit
on a chart.
Click
Customize drill downs
.
In the
Drill downs
window, in the left pane, click
add
Add drill down
to create a new drill down.
Under
Drill down configuration
, enter a name for the drill down.
In the
Action
list, select an appropriate action for the drill down. You can select any of the following options:
Run Search
Apply dashboard filter
Open external link
Configure the drill down, and then click
Done
.
Run search
You can customize a drill down to run a query in Search.
In the
Drill downs
window, under
Drill down configuration
, enter name in the
Name
field.
In the
Action
list, select
Run search
.
Optional: Select the
Open in new tab
checkbox to open the search in a new tab.
In the
Show fields to copy
list, select an appropriate value for
which you want to configure the trigger. The values in the list are the values returned by the original search query.
In the
Search
field, type a query.
Select the appropriate time range.
Click
Test
to test the query in
Search
.
Click
Done
.
Open external link
You can customize a drill down to open an external link. For example, you can
customize the drill down to open the threat intelligence page for a clicked IP address.
To create an external link for a trigger, do the following:
In the
Drill downs
window, under
Drill down configuration
, enter name in the
Name
field.
In the
Action
list, select
Open external link
.
Optional: Select the
Open in new tab
checkbox to open the link in a new tab.
In the
Show fields to copy
list, select an appropriate value for
which you want to configure the drill down. The values in the list are the values returned by the original search query.
In the
Link
field, enter a link that opens when you click the trigger.
Click
Done
.
Apply dashboard filter
You can customize a drill down to select and edit existing filters.
To apply a dashboard filter to a trigger, do the following:
In the
Drill downs
window, under
Drill down configuration
, enter name in the
Name
field.
In the
Action
list, select
Apply dashboard filter
.
Click
add
Add filter
.
In the
Filter
list, select an existing filter.
Modify the filter as per your requirements.
Optional: Click
add
Add filter
to add more filters.
Optional: Click
delete
Delete
to delete a filter.
Click
Done
to save the changes.
Make a copy of drill down
To make a copy of a drill down, do the following:
In the
Drill downs
window, in the left pane, click the drill down you want to
make a copy of, and then click
content_copy
Duplicate.
Reorder a drill down
If you have multiple right-click drill downs, you can reorder them to control their display order in the context menu.
To reorder a drill down, do the following:
In the
Drill downs
window, in the left pane, drag a drill down to reorder.
Delete a drill down
To delete a drill down, do the following:
In the
Drill downs
window, in the left pane, click the drill down you want
to delete, and then click
delete
Delete.
Need more help?
Get answers from Community members and Google SecOps professionals.
