# Track case response and closure times

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/measure-how-long-security-analysts-take-to-close-or-raise-a-case/  
**Scraped:** 2026-03-05T10:07:20.259090Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Track case response and closure times
Supported in:
Google secops
SOAR
This document explains how to measure case handling time in Google Security Operations using dashboards. You can track how long it takes to complete case-related processes, with breakdowns by attributes, such as
stage
or
priority
.
The following example demonstrates how to create a dashboard table widget
that displays the average case handling times, by case priority, for analysts
working in the default environment:
Go to
SOAR Dashboards
.
Click
add
Add Widget
.
In the
Widget Settings
dialog, enter
Case Handling Time
as the
Title
, and then choose a widget width.
Under
Chart Type
, select
Table
(the default is
Pie Chart
).
Configure the
Table
settings as follows:
Number of
=
Cases
Calculate field
=
Handling avg time
Axis A
=
Environment
Axis B
=
Priority
Click
Create
. The new widget appears on the dashboard and shows the average time analysts take to handle cases in the default environment, grouped by case priority.
Need more help?
Get answers from Community members and Google SecOps professionals.
