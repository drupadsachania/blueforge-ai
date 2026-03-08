# Manage custom fields

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields/  
**Scraped:** 2026-03-05T09:33:54.763662Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage custom fields
Supported in:
Google secops
SOAR
This document describes how to create and manage custom fields, and how to use them for
advanced reporting
. 
Custom fields let administrators add specific information to cases and alerts.
You can organize these custom fields using a
Custom Fields Form
widget, which
defines the default views for cases and alerts. Analysts can then enter
information directly into this widget from the
Overview
tab of cases and
alerts, based on the custom field's configured scope.
Create a custom field
Administrators can create up to 1,000 custom fields. Once a custom field is saved,
you can't modify its
Scope
,
Type
, or
Name
.
To create a custom field, do the following:
Go to
SOAR Settings
>
Case Data
>
Custom Fields
.
Click
Add
Add
to create a new custom field.
Select
Scope
and then select
Case
,
Alert
, or
All
(both). The
Scope
field is required and can't be changed once the custom field is created.
Enter a custom field
Name
. The
Name
field is required and can't be changed after the custom field is created.
In the list, select a custom field
Type
:
Free Text
: Enter any text, up to 1,024 characters.
Radio Button
: Provides two customizable options for selection.
Single Select
: List with a single option to select.
This type supports a maximum of 1,024 characters, with each option name limited to 255 characters.
Multi Select
: List with multiple options to select.
This type supports a maximum of 1,024 characters, with each option name limited to 255 characters.
Calendar
: A date and time field. The default format is
DD/MM/YYYY HH:MM:SS
.
Click
Save
.
Use case: use custom fields to enhance phishing resistance
This use case outlines the steps to define three custom fields: a radio button,
a single-select list, and a calendar, and how to add them to the
Custom Field Form
widget. These fields enrich the default alert view with additional
information for phishing alerts.
Define the False Positive custom field
For
Scope
, select
Alert
.
In the
Name
field, enter
False Positive
.
In the
Type
list, select
Radio Button
.
In the
Options
field, enter
True Positive
(then press
Enter
), and
then enter
False Positive
(then press
Enter
).
Click
Save
.
Define the User Action custom field
Click
Add
to create another new custom field.
For
Scope
, select
Alert
.
In the
Name
field, enter
User Action
.
In the
Type
list, select
Single Select
.
In the
Options
field, enter
Clicked
(then press
Enter
),
Reported
(then press
Enter
), and then
Ignored
(then press
Enter
).
Click
Save
.
Define the Report Time custom field
Click
Add
to create another new custom field.
For
Scope
, select
Alert
.
In the
Name
field, enter
Report Time
.
In the
Type
list, select
Calendar
.
Click
Save
.
Add custom fields to the alert-level widget
After defining custom fields, add them to the
Custom Fields Form
widget.
Each widget can hold up to 50 custom fields. The following steps show how to add
the three custom fields you created previously to the
Custom Fields Form
widget to enrich the default alert view.
Go to
SOAR Settings
>
Case Data
>
Views
>
Default Alert View
. The
Default Alert View
opens with the available the widgets.
On the
General
tab, drag the
Custom Fields Form
widget to the
Default Alert View
.
In the
Custom Fields Form
widget, click
Settings
Configuration
to open its settings.
In the
Widget Title
field, enter
True or False Positive Alert
.
Select
Manage Custom Fields
.
Select the
False Positive
,
User Action
, and
Report Time
checkboxes,
and then click
Save
. The system adds these custom fields to the
Custom Fields Form
widget.
Click the
Mandatory
toggle.
Select
Save
to save the configuration and close the window.
Click
Save View
.
Use the Custom Fields Form widget
After you add custom fields to the
Custom Fields Form
widget, it appears in
the
Overview
tab of cases and alerts. Analysts can then enter the required
information directly. Building on the previous example, follow these steps to
use the widget:
On the
Alert Overview
tab, select the
Custom Fields
widget, and click
edit
Edit
.
Fill in the relevant information for the three custom fields:
False Positive
: Select the radio button to indicate if the alert is a
true
or
false
positive.
User Action
: Select
Clicked
,
Reported
, or
Ignored
.
Report Time
: Select the date the alert was reported.
Click
Save
.
Use custom fields in playbooks
You can use the custom fields you define on this page as part of playbook actions and placeholders.
For more information about playbook actions, see
Integrate Siemplify with Google SecOps
.
Placeholders for custom fields
Custom fields are available under the
Custom Fields
placeholder category. Use the following format for these placeholders:
\[AlertCustom.{custom field name}\]
\[CaseCustom.{custom field name}\]
Use custom fields in advanced reports
Custom fields created for cases can be used in advanced reports to gain 
deeper insights from your data.
Note:
Advanced reports support only custom fields 
that have a
Case
scope.
Create custom fields for single-select values in Looker
To reference a single-select custom field (for example,
"Country"
) in a 
Looker report, use the following LookML formula as a calculated 
field:
if(
      contains(${vw_cases_custom_values.custom_field_json},"\"Country\":"),
      replace(
      replace(
      replace(
        if(position(
          replace(
            ${vw_cases_custom_values.custom_field_json},
            substring(
              ${vw_cases_custom_values.custom_field_json},
              0,
              ( position(
                ${vw_cases_custom_values.custom_field_json},
                "\"Country\":")
                +
                length("\"Country\":")
              )
            ),
            ""
          ),
          "\","
        )>0,

        substring(
          replace(
            ${vw_cases_custom_values.custom_field_json},
            substring(
              ${vw_cases_custom_values.custom_field_json},
              0,
              ( position(
                ${vw_cases_custom_values.custom_field_json},
                "\"Country\":")
                +
                length("\"Country\":")
              )
            ),
            ""
          ),
          0,
          position(
            replace(
              ${vw_cases_custom_values.custom_field_json},
              substring(
                ${vw_cases_custom_values.custom_field_json},
                0,
                ( position(
                  ${vw_cases_custom_values.custom_field_json},
                  "\"Country\":")
                  +
                  length("\"Country\":")
                )
              ),
              ""
            ),
            "\","
          )
        ),
        replace(
          ${vw_cases_custom_values.custom_field_json},
          substring(
            ${vw_cases_custom_values.custom_field_json},
            0,
            ( position(
              ${vw_cases_custom_values.custom_field_json},
              "\"Country\":")
              +
              length("\"Country\":")
            )
          ),
          ""
        )),
        " \"",
        ""
      ),
      "\"",
      ""
    ),
    "}",""),
    null
    )
Create custom fields for multi-select values in Looker
To reference a multi-select custom field (for example,
"Department"
) in a 
Looker report, use the following LookML formula as a calculated field:
if(contains(${vw_cases_custom_values.custom_field_json},"\"Department\""),

    substring(

    replace(
    replace(

    substring(${vw_cases_custom_values.custom_field_json},
    position(
    ${vw_cases_custom_values.custom_field_json},
    "\"Department\""),length(${vw_cases_custom_values.custom_field_json}))

    ,"\", \"Department\":\"",","),

    "\"Department\":\"","")

    ,0, position(replace(
    replace(

    substring(${vw_cases_custom_values.custom_field_json},
    position(
    ${vw_cases_custom_values.custom_field_json},
    "\"Department\""),length(${vw_cases_custom_values.custom_field_json}))

    ,"\", \"Department\":\"",","),

    "\"Department\":\"",""),"\"")-1)

    , null)
Filter custom fields in Looker
To effectively filter custom fields in Looker, the method you use depends on whether you are working with a Look or a dashboard.
Filtering in a Look
To filter both single-select and multi-select custom fields in a Look, you 
can directly use the custom dimension field created with the preceding formulas.
Filtering on dashboards
To filter custom fields on dashboards, you must reference the underlying JSON 
value from
Explore
and use the appropriate values in the filter, as follows:
Single-select fields:
For example, to filter for cases 
    where the
Country
custom field is
China
, use the filter 
    condition:
%"Country": "China"%
(where the exact syntax might 
    vary slightly depending on the Looker version).
Multi-select fields:
To filter multi-select fields with 
    dashboards, reference and use the JSON value and appropriate syntax, 
    which can vary based on your filtering needs (for example, matching any or 
    all selected values).
Need more help?
Get answers from Community members and Google SecOps professionals.
