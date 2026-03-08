# Manage properties metadata

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/manage-properties-metadata/  
**Scraped:** 2026-03-05T09:46:54.636908Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage properties metadata
Supported in:
Google secops
SOAR
This document explains how to use the properties metadata to change how the system presents event fields
  and the category where they appear, such as
Case overview
>
Event fields
and
Entity screen
>
Enrichment fields
. For
  example, you can configure properties metadata such that the system groups all events or
  enrichments fields that start with the
VT_
prefix in the
VirusTotal
category.
You can validate the metadata property after you create it.
Add properties metadata
To add properties metadata, follow these steps:
Go to
Settings
>
Data Configuration
>
Properties Metadata
.
Click
add
Add
.
Add the following required information:
System Name
: The name of the raw field.
Display Name
: How the field appears on the screen.
Group Name
: The name of group or category where the field appears.
Prefix
: The prefix used to group multiple fields.
Trim Prefix
: Removes the prefix from the field name.
For example, if you define and trim the
VT_
prefix,
        the system displays
VT_department
as department.
Is displayed
: Displays the field on the page.
Is highlighted
: Displays the field in the
Highlighted
section of the page.
Click
add
Add
.
Validate properties metadata
You can validate properties metadata in two ways, depending on whether you used a prefix.
Validate without a prefix
To validate the properties metadata without a prefix, follow these steps:
Add properties metadata for a specific field without a prefix, and then
  click
add
Add
.
Go to
Cases
>
Alerts Event
tab.
Click
View More
. The
Category File
appears in the side drawer.
Validate with a prefix
To validate the properties metadata with a prefix, follow these steps:
Add properties metadata for multiple fields including a
VT_
prefix, and then click
Save
.
Go to
Cases
>
Entities Highlights
widget in either the
Cases Overview
or
Alerts Overview
tab.
Click an entity to open the
Entity Details
page.
Use cases
This section describes use cases that demonstrate the system's flexibility to manage and display events within cases.
Set the default appearance of events in cases
In Google SecOps, cases contain a subset of alerts. These alerts
provide access to events, which include specific fields that describe the event.
To test this, create a new case:
Select
Cases
>
Add
>
Simulate Cases
.
Create a new
Malware Detected
case in your preferred environment. If you don't have another case, use the
Default Environment
.
In the case description, select an alert
Virus Found
and then select the
Events
tab. The system displays a single event, also named
Virus Found
.
Click the
Virus Found
event to view the list of fields.
Scroll to find the fields related to the event date.
Modify the appearance of the events in cases
You can modify event appearance, rename fields, and group them.
To modify the appearance of an event, you need to update the
Properties Metadata
.
The following example describes the steps to reconfigure the following fields to appear in Spanish.
Open a new browser tab and click
SOAR Settings
>
Data Configuration
>
Properties Metadata
.
Click
add
Add
and redefine the
Display name
field values according to the following table.
Reconfigure the following fields to appear in Spanish:
date_hour
date_mday
date_minute
date_month
date_second
date_wday
date_year
date_zone
Select one of the following options:
Is displayed
: Displays the field in the event description.
Is highlighted
: Moves the field to a dedicated group of highlighted fields.
System name
Display name
Group name
Is displayed
Is highlighted
date_hour
Hora
Fecha del evento
yes
yes
date_mday
Día del mes
Fecha del evento
yes
no
date_minute
Minuto
Fecha del evento
yes
yes
date_month
Mes
Fecha del evento
yes
no
date_second
Segunda
Fecha del evento
no
no
date_wday
Día de la semana
Fecha del evento
no
no
date_year
Año
Fecha del evento
no
no
date_zone
Zona horaria
Fecha del evento
yes
no
Need more help?
Get answers from Community members and Google SecOps professionals.
