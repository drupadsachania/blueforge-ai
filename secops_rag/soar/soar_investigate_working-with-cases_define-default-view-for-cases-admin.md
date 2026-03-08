# Configure the default case view

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-default-view-for-cases-admin/  
**Scraped:** 2026-03-05T10:07:10.670185Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure the default case view
Supported in:
Google secops
SOAR
This document explains how administrators can configure a unified default view
  for all cases shown on the
Cases
page. This unified view helps analysts
  quickly assess and act on the most critical case information.
To define a default view, go to
Settings
>
Case Data
>
Views
>
Default Case View
Access the Default Case View
The
Default Case View
editor displays a set of system widgets—some of
which are provided by Google Security Operations Marketplace integrations—and a
layout template where you can place them. Use the editor to build a case overview
that meets your organization's needs.
Customize your view layout
You can customize the layout by dragging widgets from the side pane into the
layout area. Available widgets include the following:
Custom Fields Form
: displays any custom fields you've defined.
    Analysts can use this section to enter structured case data. Learn how to
create custom fields
.
Alerts
: displays alert-level information for all alerts
    grouped into the case, including alert name, number of events, and priority.
Case Description
:
    A free-text field for analysts to enter notes or context about the case.
Entities Highlights
: displays highlighted fields for each entity associated with the case.
Latest Case Wall Activity
: displays recent activities posted to the case wall within a configurable time window.
Pending Actions
: Lists all playbook actions that require analyst input to keep the playbook running.
Recommendations
: Displays similar cases and suggests 
    analysts and tags to assign to the case.
Statistics
: Displays the distribution of selected entity 
    fields.
HTML
: Supports HTML code to create insights and inject relevant information from playbook results. Gives the option to return safe code without potentially malicious JavaScript.
Key Value
: Displays a single key-value pair, such as `Key: Product`, `Value: [Alert.Product]`.
Free Text
: Lets you display static free-text content in the case overview.
Entities Graph
: Displays a visual graph and details of the case entities.
Insights:
Shows insights from playbooks, general logic, or manual analyst input in HTML format.
Quick Actions
: Displays action buttons that let 
  analysts run predefined actions on cases directly from the case 
  overview. For more information, see
Create a Quick Action
.
Gemini Summary
: Provides an AI-generated case summary and 
  remediation suggestions.
Composite Detections
: Available only for users of the Google SecOps unified platform. This widget 
  helps analysts understand the components of alerts within a case. For
composite alerts
(from chained rules), this 
  widget shows:
Contributing detections
Alert lineage
Associated UDM events
For single alerts, it displays only their specific UDM events. This helps analysts understand alert structure and root cause.
Rule Overview
: Available only for users of the Google SecOps unified platform. This widget 
  provides information on the curated or custom rule associated with an alert, including a
View Details
button that opens a rule-overview sidebar with comprehensive rule information, including Rule Details (Name, Description, State, Severity, MITRE tags) and YARA-L Rule Code. It also includes a friendly link to manage the rule in the 
  [Curated detections tab](/chronicle/docs/detection/use-curated-detections)
Add widgets
To add widgets to the layout, do the following:
Drag a widget from the pane to the template on the right.
You can rearrange the widgets as needed, to create your preferred layout.
Edit widgets
To configure or update a widget:
Click
settings
Configuration
. Some widgets offer additional 
fields for configuration. For example, in the latest wall activity, you can 
specify the timeframe and activity types.
On the
Cases
page, update the widget title, tooltip, or width (50% or 100%), as needed.
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
