# View IOCs using Applied Threat Intelligence

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page/  
**Scraped:** 2026-03-05T10:05:57.754178Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
View IOCs using Applied Threat Intelligence
Supported in:
Google secops
SIEM
When Applied Threat Intelligence is enabled, the
IOC Matches
tab displays additional columns.
The
IOC matches
tab displays all the indicators of compromise (IOC) that were matched in your Google Security Operations data.
You can view and filter IOCs curated by Applied Threat Intelligence.
On the
IOC matches
page you can do the following.
View the IOCs
View data
Filter IOCs
View IOC details
View IOCs
The
IOC matches
page displays all the IOCs and their details, such as
type, priority, status, categories, assets, campaigns, sources, IOC ingest
time, first seen, and last seen. The color-coded icons and symbols help you to
quickly identify which IOCs need your attention.
View data
Click the
calendar_month
to display the calendar. You can adjust the time range for the
displayed data. Adjust the time range by
choosing one of the pre-set time ranges on the left side (ranging from last
five minutes to last month). You can also specify a custom time range by choosing
a start and end date anywhere on the calendar.
Filter IOCs
In the left column, select the category to filter by. You can use the following options to filter:
Type
GCTI Priority
Status
Categories
Sources
Associations
Campaigns
To select more advanced filters, click the
filter_alt
icon and then select the elements to filter on. You also need to select a logical operator:
OR. Must match any of the combined conditions
AND. Must match all of the combined conditions
To add more filters, click
add
Add filter.
When you add a filter, it appears as a chip above the table.
To use two filters from the same category, the filters appear in the same chip.
To find IOCs labeled as Active IR or High (both under the
GCTI Priority
label), complete the following steps:
Select a logical operator.
Select the first filter.
Select the second filter.
When you click the second filter, there are two new options:
Show only
and
Filter out
instead. Click
Show only
.
View applied intelligence IOCs
In the left column, click
Sources
.
Click
Mandiant
to filter the data and view applied intelligence IOCs.
Clear filters
Click the
delete
icon next to the filter you want to delete.
Click
Clear all
to clear all the existing filters from the page.
View IOC details
You can click an IOC to view details such as priority, type, source, IC-Score, and
category. If you are getting IOC mapping but there are no events, then there is a
mistake in the field mapping or there are no rules. For more information,
contact Google SecOps
Support
.
For a selected indicator, on the
IOC details
page, you can do the following:
View event prioritization
View associations
Event viewer
On the
Events
tab, on a selected indicator, you can view how an event is prioritized and the details for an event.
For each event, you can view priority and rationale, UDM fields, and event details.
The priority and rationale displays how priority is determined for the event.
Associations
On the
Associations
tab, on a selected indicator, you can investigate potential breaches.
You can view associations for any actor or malware. This also helps to prioritize alerts.
Need more help?
Get answers from Community members and Google SecOps professionals.
