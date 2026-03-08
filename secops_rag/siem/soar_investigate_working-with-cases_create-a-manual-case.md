# Create a manual case

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case/  
**Scraped:** 2026-03-05T09:34:22.399380Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create a manual case
Supported in:
Google secops
SOAR
You can manually create a case to enter specific data. This is useful when you
  need to ingest information on an alert; for example, information that was reported
  from sources that aren't integrated with your detection pipeline (for example,
  alerts reported from non-cyber channels).
On the
Cases
page, click
add
Add
>
Create Manual Case
.
Enter the following case properties:
Case Title
: Enter a title for the new case.
Creation Reason
: Enter the reason for creating the case.
Environment
: Select the specific environment being 
        monitored.
Assigned To
: Assign the case to a specific role or user.
Priority
: Set the priority level for the case.
Mark as Important
: Click the
Mark as important
toggle on if the case should be flagged as important.
Click
Next
.
In the
Alert
step, enter the following alert information:
Alert Name
: Enter a name for the security alert.
Occurrence Time
: In the calendar, select the date and time the alert occurred.
SLA
: Specify a date and time by which the SOC team should resolve the case.
Click
Next
.
In
Entities
, select any required existing entities, as follows; you can:
Add an existing entity or create a new one with a corresponding identifier.
Mark an entity as suspicious (this highlights it in red).
Click
Next
.
In
Tags
, select any existing tags, create new tags, or leave 
    blank, according to your needs.
Click
Next
.
In
Playbooks
, select any relevant playbooks to be attached 
    to the alerts.
Click
Finish
.
Need more help?
Get answers from Community members and Google SecOps professionals.
