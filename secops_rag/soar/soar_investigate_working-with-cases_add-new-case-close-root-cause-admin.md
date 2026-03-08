# Customize the Close Case dialog

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-new-case-close-root-cause-admin/  
**Scraped:** 2026-03-05T10:07:21.760068Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Customize the Close Case dialog
Supported in:
Google secops
SOAR
This document explains how to customize the
Close Case
dialog
in Google Security Operations (Google SecOps). By default, the dialog
includes the
Reason
,
Root Cause
, and
Comment
fields. Administrators can extend this dialog by adding
custom parameters and root causes to improve the consistency and quality of case
documentation.
Learn more about
how to resolve and close cases
.
Add a custom field
To customize the
Close Case
dialog with additional
   parameters, complete the following steps:
Go to
SOAR Settings
>
Case Data
>
Close Case
.
Click
add
Add 
    Custom Parameters
.
Complete the common fields:
Name:
Enter a name for the new parameter.
Type:
Select a field type to add from 
        the
Type
menu:
Free Text
: Enter a name for the field to let
            the analyst enter custom details for that case. For example, name the field
Customer phone number
, and the analyst can enter 
            the relevant contact details.
Radio Button
: Select one 
            of two options. For example, to specify whether a case was resolved 
            or needs escalation, in the
Radio Button Content
field, use
Mitigated
or
Escalated
to indicate the case resolution status.
Single choice list
: A list where the 
            analyst selects one option. For example, to categorize the type of 
            threat identified in a case, use options like
Malware
,
Phishing
, or
Insider Threat
to classify the threat type.
Multi choice List
: Select 
            multiple options. For example, to log incident actions, 
            include options such as
Containment 
            Measures Implemented
,
System Patches 
            Applied
,
User Education 
            Provided
,
Alerts Updated
, or
Access Revoked
.
Default Value:
Optionally set a default for the
Close Case
dialog. Leave the
Default Value
field blank
        if no option is pre-selected. To remove a default value you've 
        set, click
Reset
.
Description:
Enter a description that appears 
        as a tooltip when you hold the pointer over the
info
next to the 
        parameter in the
Close Case
dialog.
Add a new root cause
To add a new root cause to the
Root Cause
menu, follow these steps:
Go to
SOAR Settings
>
Case Data
>
Close Case
.
Click
add
Add Root Cause
. 
     The
Add Case Close Root Cause
dialog appears.
In the
Reason
list, select a reason, and enter 
     relevant information in the
Root Cause
field.
Click
Add
to save the root cause.
Case disposition and rule tuning
Disposition lets you identify "noisy" rules 
that produce high volumes of non-actionable alerts. 
When closing cases, you can categorize them as
Malicious
or
Non-Malicious
which corresponds to
True Positive
or
False Positive
.
To capture other closure types, or to keep the names
True and False Positive
, Google recommends creating a custom field (
Single Choice List
) labeled
Disposition
in the
Close Case
dialog. 
This approach ensures that the
Root Cause
field remains available to describe the technical origin of the case.
Recommended disposition values:
True Positive: A legitimate security threat that required mitigation.
Benign Positive: A correct detection of authorized activity (for example, a sanctioned pentest). These values are primary candidates for tuning or exclusion lists.
False Positive: An incorrect detection caused by logic errors or "noisy" software behavior.
Undetermined: Insufficient data to reach a conclusion.
Analysts can use these dispositions in SOC dashboards to visualize the False Positive Rate per Rule ID, allowing engineers to prioritize which rules require immediate logic refinement.
Need more help?
Get answers from Community members and Google SecOps professionals.
