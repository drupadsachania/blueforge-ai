# Risk Analytics Quickstart guide

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/ueba-getting-started/  
**Scraped:** 2026-03-05T09:31:47.128448Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Risk Analytics Quickstart guide
Supported in:
Google secops
SIEM
Learn how to use the
Risk Analytics dashboard
to identify unusual behavior 
and understand the potential risk that entities pose to your enterprise. 
On systems that use role-based access control (RBAC), only users with global 
scope can access risk analytics. For more information, see
User roles
.
The Risk Analytics dashboard consists of the following sections:
Behavioral Analytics
: lists entities according to
Google Security Operations Entities risk scores
risk scores.
Watchlist
: 
lists entities according to internal enterprise risk calculations.
A
Risk Calculation window
at the top right changes the calculated risk score displayed in the Risk Analytics 
dashboard. You can change this setting depending on the type of attack you are 
searching. For example, brute force attacks are more visible by setting the
Risk Calculation Window
to
24 Hours
. 
To see long-term attack, set the
Risk Calculation Window
to
7 days
.
You can view historical risk scores by selecting a specific date and time in the 
date selector next to the
Risk Calculation Window
. This displays the 
entity risks calculated for the 24-hour or 7-day window, ending at the chosen 
date and time.
Before you begin
To navigate to the Risk Analytics dashboard, follow these steps:
In the navigation bar, click
Detection
.
From
Detection
, click
Risk Analytics
.
Behavioral Analytics
Behavioral Analytics consists of:
The
Behavioral Analytics
page consists of:
Summary Metrics
section: a top-level view of the
Risk Analytics
dashboard
that lets you investigate risk entities based on Google SecOps 
entity risk modeling. You can view up to 10,000 entities in the summary.
Entities
: a table that complements the existing risk score used for 
tracking an entity's risk over time, as a metric for detection use cases, and as 
investigative context. Also called
entity risk metrics
, an entity is a contextual 
representation of elements in your environment. Examples for entities are user 
accounts, servers, laptops or phones. You can drill down to each entity by 
clicking the entity name. This will take you to the
Entity Analytics
page.
For more information about entities, see
Logical objects: Event and Entity
. 
For more information on how risk scores are calculated, see
Risk score calculation
.
Entity Analytics
The
Entity Analytics
page consists of an
Event range
window at the top 
right corner, a
Findings Timeline
section, and a detailed
Findings
table.
Select a time range to analyze risks
In the
Event range
window, select a time range of up to 90 days 
("Last 3 months").
For
Selection
, click
View analytics for Selection
. This opens a 
sidebar that shows you the analytics associated with this entity within the 
selected time range. Each analytic displays an aggregate of all the analytic 
values within the time range.
Click
View more
to open the corresponding Alerts or Detection view. When 
detected, an analytic includes a list of related alerts and detections that can 
be examined further.
View composite detections
The
Detections
table displays all detections for an entity that
occurred within the selected time range. An alert is a
composite detection
when:
The
Inputs
column shows
Detection
as a source.
The
Detection type
column displays an
Alert
or
Detection
label
with a number next to it (for example,
Alert (3)
).
This indicates that a detection, or a chain of detections, triggered the alert,
rather than raw events or entities alone.
You can view and analyze these underlying detections in the
Detections
table
by using the following features:
Expand rows to view nested detections, associated event data, and related
entity information.
Customize your view by using the column manager to select and arrange
columns in the table.
For more information, see
Investigate an alert
.
Use Cases
Here are a few use cases for the Risk Analytics dashboard.
Use case 1: High download volume
A high download volume of data poses the risk of confidential information leaking. 
Google SecOps calculates high risk score numbers for entities 
with high download volumes.
Use case 2: Suspicious number of failed login attempts
Suspicious numbers of failed login attempts indicate that a hacker or malware is 
attempting to gain access to a user account. Google SecOps will 
calculate high risk score numbers for entities with suspicious numbers of failed 
login attempts. However, if this is done internally, as part of penetration 
testing, you can
modify the entity risk score
.
Use case 3: Dialog message impersonating Google
A dialog message impersonating Google asking to update the Chrome Browser is 
attempting to gain access to user accounts. Google SecOps 
calculates high risk score numbers for entities where these dialog messages are 
detected in the code.
What's next
Modify an entity risk score
Investigate an asset
Need more help?
Get answers from Community members and Google SecOps professionals.
