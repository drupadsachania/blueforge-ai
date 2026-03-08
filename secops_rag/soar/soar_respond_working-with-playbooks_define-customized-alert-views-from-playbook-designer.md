# Define custom alert views from Playbook Designer

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/define-customized-alert-views-from-playbook-designer/  
**Scraped:** 2026-03-05T10:08:13.521902Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Define custom alert views from Playbook Designer
Supported in:
Google secops
SOAR
This document explains how to create customized alert
  views on each playbook for specific Google SecOps roles. The
  customized alert views make sure that each Google SecOps user can
  see the alerts tailored to their specific needs.
You create the views in the playbook designer and are composed of various
  widgets that you can drag and edit to create the required view based on
  the playbook results. For a detailed description of all widgets, see
Default alert view
.
By creating customized alert views, you can decide, in
  advance, what information you want to display to different roles. For
  example, if you have a collaborator user and you created a Google SecOps
  role for that user called
Premium Customer Role
, you can then build a
  view that contains only the information that fits their role without compromising your organization's security.
If you don't define a view for a specific Google SecOps role,
  users with that role will see the default alert view.
The customized alert view configuration within the playbook designer may include 
the following widgets:
JSON results
: View a
JSON
result in the system.
Entity Highlights
: View entities associated with the alert.
If you're a unified Google SecOps customer, click
Explore
to 
be redirected to the alert
Asset
page to perform more actions. The page 
you land on depends on the type of entity. For more information, see
Investigation views
.
If you need more detailed information before taking action, click the entity 
to go to the
Entity Explorer
page and view its full details.
To have a quick look prior to taking action, click
View Details
and a 
side drawer opens with the entity's highlights.
To run a specific action on an entity, you can click
settings
Settings
and 
create a manual action from here.
Events Table
: View all alert events and their properties. 
Click any of the table rows to open a side drawer to see events details.
HTML
: View the HTML code that contains relevant information 
from the playbook results.
Free Text
: View Admin-defined information.
Key Value
: View specific details from various sources and 
display them in the view. For example: Key- Product Value- [Alert.Product]
Entities Graph
: View a visual graph and other case entity 
details. Click an entity and a side drawer opens.
Insights
: This widget contains all the Insights from the 
Playbook insights actions, general insights and any other insights you have 
added. They will be presented in HTML format.
Pending Actions
: Quickly view all actions awaiting your 
input to keep the playbook running.
Quick Actions
: This widget provides analysts with immediate 
access to relevant actions directly within the alert context. For detailed 
instructions on configuring Quick Actions, including defining actions and 
parameters, see
Take actions on a case
.
Rule Overview
: Available only for users of the Google SecOps unified platform. This widget 
  provides information on the curated or custom rule associated with an alert, including a
View Details
button that opens a rule-overview sidebar with comprehensive rule information, including Rule Details (Name, Description, State, Severity, MITRE tags) and YARA-L Rule Code. It also includes a friendly link to manage the rule in the 
  [Curated detections tab](/chronicle/docs/detection/use-curated-detections)
Create a customized alert view
This example shows how to build a customized alert view on
  a phishing email for a Tier 1 role.
To add a customized alert view, do the following:
Go to the alert's
Overview
tab.
On the
Playbooks
page, go to the
Phishing Email
playbook and
    click
Add View
.
Enter a template name, choose the required role, and then
    click
Add
; in this case,
Tier One
.
Create your customized view by selecting from the following widgets.
    Drag the selected widgets into the view and then configure them according to
    your requirements.
Add a
Pending Actions
widget.
Add two
Free Text
widgets. One is displayed, if
    there's an approval action. This contains the following placeholder:
[Case Outcome - Block approved .ScriptResult]
The other widget appears if the outcome isn't approved.
[Case Outcome - Block not approved .ScriptResult]
Add another
Free Text
widget and name it
Attack Details - Mitre
. This contains the following placeholder:
[Mitre Attack Details.ScriptResult]
.
Add the
Entities Highlights
widget.
Add a
JSON
widget, and add the following placeholder:
[Exchange_Search Mails_1.JsonResult]
.
Add the
HTML
widget.
Once the appropriate alert has been ingested into the system and the
    playbook has run, the Tier One role user can enter the platform and see the
    alert
Overview
with the playbook results.
Need more help?
Get answers from Community members and Google SecOps professionals.
