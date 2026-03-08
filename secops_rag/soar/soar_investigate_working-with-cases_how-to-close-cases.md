# Resolve and close cases

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases/  
**Scraped:** 2026-03-05T10:07:03.765291Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Resolve and close cases
Supported in:
Google secops
SOAR
This document describes how to close cases in Google Security Operations using various interface options, including the case details page, the case queue (side-by-side and list views), and the
Search
page. It also explains how to view the contents of closed cases. You can close a case once it's resolved. For information on what details to enter when closing a case, see
Use custom fields
.
Ways to close a case
You can close a case once it's resolved. You can do this from the following locations:
For a single case, use the
case details page (top menu)
.
For multiple cases, use bulk actions from one of the following locations:
Side-by-Side
or
List
views on the
Cases
page
the
Search
page
API Endpoint
Close a single case from the case details page
Open the case you want to close, then click
Close Case
.
In the
Close Case
dialog, select a valid reason and a root cause for
    closing the case, and enter any additional comments. You must select a reason before you can select a root cause. These comments will be posted on the Case Wall. If you create an action with a root cause, you need to add the parameter of the reason.
Click
Close
.
Close multiple cases at once
When you manage a high volume of cases, choose a method that matches your 
workflow and the number of cases you want to close.
The following guidelines are based on the approximate number of open cases in your case queue.
For a small number of cases (2-250 cases)
If you have a manageable number of cases to close (typically 2-250 cases, 
with the platform allowing you to close up to 50 at once from the
Cases
page views or the
Search
page), you can use these methods directly within 
the platform.
From the cases queue (side-by-side view)
In the cases queue, click
Select multiple cases
.
Select the relevant cases you want to close in the cases queue.
Click
format_list_bulleted
Close Cases/Merge Cases
and select
Close Cases
.
In the
Close Case
dialog, select a valid reason and a root cause.
   Optionally, enter comments to post on the Case Wall.
Click
Close
.
From the cases queue (list view)
Select the relevant cases you want to close in the cases queue.
Click
Close cases
.
In the
Close Case
dialog, select a valid reason and a root cause
    for closing the case and enter any additional comments. These comments will
    be posted on the Case Wall.
Click
Close
.
From the Search page
Go to the
Search
page.
Apply filters to find the relevant cases you want to close.
From the search results, select the cases you want to close.
Click
format_list_bulleted
Menu
and select
Close case
.
In the
Close Case
dialog, choose a valid reason and root cause. 
  Optionally, enter comments to post on the Case Wall. Click
Close
when 
  finished.
For a medium number of cases (250-2000 cases)
For a larger, but still manageable number of cases (typically 250-2000 cases, 
with the API allowing deletion in blocks of 50 per request), use the following 
API endpoint to bulk close cases:
/api/external/v1/cases-queue/bulk-operations/ExecuteBulkCloseCase
For a large number of cases (2000+ cases)
If you need to close a large volume of cases (2000+ cases), contact
Google Support
.
View the contents of a closed case
To view the contents of closed cases, follow these steps:
Go to the
SOAR Search
page.
In the
Filter
section, select
Status
>
Closed
.
Click
Apply
.
In the list of closed cases, click the ID number of the selected case; you're redirected to the original case contents.
Need more help?
Get answers from Community members and Google SecOps professionals.
