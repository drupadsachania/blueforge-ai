# Manage dashboards

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards/  
**Scraped:** 2026-03-05T09:36:25.511749Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage dashboards
Supported in:
Google secops
SIEM
This document explains how to manage dashboards.
View a list of dashboards
The
Dashboards
page shows a list of both curated and custom dashboards. When
you access it for the first time, only curated dashboards are visible.
You can perform the following actions on the
Dashboards
page:
Sort
: Click the column heading, in ascending or descending order, to sort the dashboards.
Search
: Search dashboards for a specific value. For example, to search for dashboards created by a specific owner, enter the owner ID in the search box.
Pin
: Pin the dashboards you use regularly or those that are important.
Click
push_pin
Pin
to pin a dashboard.
Pinned dashboards display first, followed by other dashboards.
Refresh
: Click
refresh
Refresh
to
refresh the list of dashboards.
Filter
: You can filter the list of dashboards as per your requirements.
Filter the list of dashboards
To filter the dashboard list, do the following:
Click
filter_alt
Filter
.
Select a logical operator and select a column.
Select a value in the
Show only
list, and then select the appropriate values.
Optional: Click
Add Filter
to add multiple filters.
Click
Apply
to apply the selected filters and filter the list of dashboards.
Delete filters
To delete filters, do the following:
Click
filter_alt
Filter
.
Click
delete
Delete
to delete a filter.
Click
Apply
to remove the filter and update the dashboard list based on the selected filters.
View a dashboard
To view a dashboard, do the following:
On the
Dashboards
page, click a dashboard name.
Create a new dashboard
You can create a new dashboard using the following methods:
Make a copy of an existing dashboard
Import a dashboard
To create a new dashboard, do the following:
On the
Dashboards
page, click
Create Dashboard
.
On the
Create Dashboard
window, enter a name and description for your dashboard.
In the
Start with Existing Dashboard
list, select
Blank Dashboard
.
Under
Access settings
, change the access for your dashboard to either
private
or
shared
.
Private dashboards are visible only to you, while shared dashboards are accessible
to all users within your Google SecOps instance.
Click
Create
to create a new dashboard. A blank dashboard is created.
With your blank dashboard, you can add charts to the dashboard. For more information about how to add a chart,
see
Add a chart to dashboards
.
Make a copy of an existing dashboard
To save time, you can copy an existing dashboard from the curated dashboards, private dashboards, or shared dashboards.
To make a copy of an existing dashboard, do the following:
On the
Dashboards
page, click
more_vert
Menu
next to the dashboard name, and then click
Duplicate
.
Edit an existing dashboard
After you create a dashboard, the
Edit Dashboard
page opens.
To edit an existing dashboard, do the following:
On the
Dashboards
page, click
more_vert
Menu
,
and then click
Edit Dashboard
.
On the
Edit Dashboard
window, click
Edit Details
to edit the dashboard details like name, description,
and access settings.
Click
Save
to save the details.
Click
filter_alt
Filter
to edit the filters.
For more information about filters,
see
Filters in dashboard
.
On the
Manage filters
screen, click
edit
Edit
to edit a chart.
Change dashboard access
By default, when you create a dashboard, the dashboards are private and are visible
only to you. Shared dashboards are visible to all members of the team who can
view dashboards in Google SecOps. Only the dashboard owner can change the dashboard access.
Select the dashboard you want to share, and then click
more_vert
Menu
next to the dashboard name.
Click
Share
>
Save
to share the dashboard with other users.
Delete a dashboard
To delete a dashboard, do the following:
On the
Dashboards
page, click
more_vert
Menu
next to the dashboard name, and then click
Delete
.
Click
Confirm
to delete the dashboard.
Import or export a dashboard
You can use the import and export dashboard feature to enhance collaboration and
sharing of dashboards among users and across instances.
Export dashboards
You can export private, shared, and curated dashboards to a JSON file and use it in another
instance of Google SecOps. The exported file contains the dashboard layout and filter settings.
To export a dashboard, do the following:
On the
Dashboards
page, click
more_vert
Menu
next to the dashboard name, and then click
Export
. The JSON file is downloaded on your machine.
Import dashboards
You can create a dashboard by importing a JSON file.
To import a dashboard, do the following:
On the
Dashboards
page, click
Create Dashboard
>
Import from JSON
.
On the
Import Dashboard
dialog, browse and select the appropriate JSON file.
Click
Edit
to update the name, description, and the dashboard access
you're importing.
Click
Save
.
Click
Import
to import the dashboard.
Download reports
You can download reports for each dashboard or chart to analyze the data. Reports
are available in CSV, PDF, and PNG formats, as follows:
When you download a report as a PDF or PNG, only the data visible on your screen
is included in the report, not the full chart dataset.
When you download a dashboard as a CSV, a ZIP file is generated that contains a separate CSV file for each chart.
You can download a report for a specific chart as a CSV file, independently.
To download report for a dashboard, do the following:
On the
Native Dashboards
page, click
more_vert
Menu
next to the dashboard name, and then click
Download report
.
Select the file type.
The report is downloaded on your machine.
To download report for a chart, do the following:
On the
Native Dashboards
page, click
more_vert
Menu
next to a chart, and then click
Download report
. Select the file type.
The report is downloaded on your machine.
Need more help?
Get answers from Community members and Google SecOps professionals.
