# Download events

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/downloading-events/  
**Scraped:** 2026-03-05T10:03:57.396301Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Download events
Supported in:
Google secops
SIEM
You can display and download large numbers of the events associated with each threat detection. This lets you search across a broad set of the data stored in your Google Security Operations account to hunt for security issues.
Display and download events
Complete the following steps to display and download the events associated with a detection:
In the navigation bar, click
Detection > Rules & Detections
.
Click the
Rules Dashboard
tab.
Rules Dashboard
Click a rule to open the Rule Detections view.
Select a Detection from the Detections list and expand the sample events
list by clicking the arrow next to the list.
Each event variable in a rule can display up to 10 sample events. 
For example, a rule with two event variables (
$e1
,
$e2
) can show up to 20 
samples in total. Any samples beyond this limit are hidden on the
Detections
page., but they're included if you click
Download All
to view 
Unified Data Model (UDM) events associated with your detection.
The
Download as CSV
option appears if event samples were omitted from your
detection. A maximum of 100,000 events can be downloaded.
The event samples are sorted by event timestamp in the UI. Google does not
guarantee any sorting of event samples when reading detections from
Chronicle APIs.
Optional: Click
view_column
Columns
to add more fields to the sample events list. 
These fields are also included in the downloaded CSV.
Click the
Download as CSV
link. The event samples are downloaded as a CSV file which you can then open in most spreadsheet applications.
Need more help?
Get answers from Community members and Google SecOps professionals.
