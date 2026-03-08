# Discover the HTML widget

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-html-widget/  
**Scraped:** 2026-03-05T09:35:08.403136Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Discover the HTML widget
Supported in:
Google secops
SOAR
The
HTML
widget lets you define the content and style of the displayed
data. You can customize it using a variety of presets, including ready-made HTML
code to display the data in a predefined format. You can further personalize the
display with the code editor, which provides a tailored view of the data in the
case or alert overview.
The HTML widget comes with the following presets:
Empty
Clock
Map
Table
Video
Number
Score
Bar Chart
Conversation
Gallery
User Details
7 Layout options
Create an HTML widget
To create an HTML widget
that displays enrichment details about the target user in a phishing use case,
follow these steps:
On the
Playbooks
page, drag the
HTML
widget in the view.
Click
settings
Settings
and configure it with the relevant information. For this example,
name the widget
Target Profile
.
Select
User Details
.
Select
Empty
to customize your widget. This preset doesn't contain any predefined HTML code.
Define the optimal height of the widget. For this example, keep the default widget height as 425 pixels.
You can click the
Safe HTML Rendering
toggle to activate safe HTML rendering, returning code without potentially malicious JavaScript.
Highlight and customize the field/value in the preconfigured HTML code provided by the preset.
Click
to expand the code editor window.
Click
data_array
Data Array
to insert placeholders in the code.
Select the required value for each field from the list.
In this example, replace the fields with the following values from the playbook:
Variable
Value
Var field2 =
[Entity.AD_Image]
Var field3 =
[Entity.Ad_Displayname]
Var field4 =
[Entity.AD_role]
Var field5 =
[Environment.ContactEmail]
Var field6 =
[Entity.AD_address]
Var field7=
[Entity.AD_Displayname]
Var field8=
[Entity.AD_memberOf]
Var field9=
[Entity.IsFromLdapString]
Var field10=
[Entity.Environment]
Click
Save
. As data is ingested into the Google SecOps platform, the HTML widget populates with information captured during the playbook run.
Need more help?
Get answers from Community members and Google SecOps professionals.
