# Use custom fields in the Close Case dialog

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure/  
**Scraped:** 2026-03-05T10:07:05.513795Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use custom fields in the Close Case dialog
Supported in:
Google secops
SOAR
This document explains how to use custom fields to collect and manage 
information during the case closure process.
Create a custom field
You must create a custom field with a specific scope before it can be used in 
the
Close Case
dialog. The
Scope
,
Type
, and
Name
of 
a custom field are mandatory and can't be modified after it's saved.
To create a custom field for the
Close Case
dialog, follow these 
steps:
Go to
SOAR Settings
>
Case Data
>
Custom Fields
.
Click
Add
Add Custom Fields
.
Set the
Scope
to either
Case
or
All
. Custom fields 
  with an
Alert
scope can't be used in the
Close Case
dialog.
Enter a custom field
Name
.
Select a custom field
Type
from the list:
Free Text
: Enter any text, up to 1,024 characters.
Radio Button
: Provides two customizable options for selection.
Single Select
: List with a single option to select. This type 
      supports a maximum of 1,024 characters, with each option name limited to 
      255 characters.
Multi Select
: List with multiple options to select. This type 
      supports a maximum of 1,024 characters, with each option name limited to 
      255 characters.
Calendar
: A date and time field. The default format is
DD/MM/YYYY HH:MM:SS
.
Click
Save
.
Add a custom field to the Close Case dialog
After you create a custom field with the correct scope, you can add it to the
Close Case
dialog.
Go to
SOAR Settings
>
Case Data
>
Close Case
.
In the
Custom Fields
section, click
settings
Settings
.
In the
Case Closure Fields
side drawer, click
Manage Custom 
  Fields
.
Select the custom fields you want to display in the
Close Case
dialog. You can select up to 1,000 custom fields.
Click
Save
.
Close a single case
When you close a case individually, you can enter additional information for 
the custom fields you added to the
Close Case
dialog.
Go to the case you want to close, then click
Close Case
.
In the
Close Case
dialog, the standard
Reason
and
Root Cause
fields appear alongside any custom fields that have been 
  added. Select the appropriate options for your case and enter any additional 
  comments. These comments will be posted on the
Case Wall
.
Click
Close
.
Need more help?
Get answers from Community members and Google SecOps professionals.
