# Import and export Google SecOps SIEM dashboards

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/import-export-dashboards/  
**Scraped:** 2026-03-05T09:36:36.863349Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Import and export Google SecOps SIEM dashboards
Supported in:
Google secops
SIEM
You can share a dashboard file between instances or within an instance between
different users. The dashboard can be shared without manually creating copies.
With this functionality you can do the following:
Export a dashboard configuration
Import a dashboard exported through Google Security Operations
Export dashboards
You can export personal and shared dashboards. Default dashboards cannot be exported.
The exported file includes the dashboard layout and the filter settings. The
scheduled delivery settings are not exported.
Export dashboards from Google SecOps
To export a dashboard from Google SecOps, do the following:
Log in
to your Google SecOps instance.
In the navigation bar, click
Dashboards
.
From the list of personal or shared dashboards, click
more_vert
Menu
next to the dashboard that you want to export.
Select
Export
from the list.
The
Export dashboard
dialog appears.
Click
Export
.
The YAML file is downloaded to the browser's Downloads directory.
Export dashboards from Looker
To export a dashboard from Looker, do the following:
Get the dashboard's LookML content from enterprise Looker.
Open the dashboard that you want to export.
Click
more_vert
Menu
in the top right corner and select
Get LookML
.
A window showing the LookML code for the dashboard elements appears.
Copy the LookML file content to a
.yaml
file.
Add a new line with the text
lookml:
before the existing content.
For example, if the LookML content from the enterprise Looker is:
-
dashboard: example_dashboard
  description: ""
  layout: newspaper
  title: Example Dashboard
To import it to Google SecOps, modify it to:
lookml:
-
dashboard: example_dashboard
  description: ""
  layout: newspaper
  title: Example Dashboard
The modified YAML file is ready to be imported to Google SecOps.
Import dashboards
To import a dashboard, you need a dashboard file exported through Google SecOps
or Looker. When you import a dashboard, the dashboard's layout and the
filter settings are imported too. The scheduled delivery settings are not imported.
You can import a dashboard to personal or shared dashboards by doing the following:
Log in
to your Google SecOps instance.
In the navigation bar, click
Dashboards
.
Click
Add
next to personal or shared dashboards and then select
Import dashboard
.
The
Select file
dialog appears.
Select a file and click
Confirm
.
The
Import dashboard
confirmation dialog appears.
Click
Import
to continue importing the dashboard to personal or shared
dashboards.
The imported dashboard is added to the existing dashboards list.
Need more help?
Get answers from Community members and Google SecOps professionals.
