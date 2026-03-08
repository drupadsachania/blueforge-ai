# Manage unified rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/manage-unified-rules/  
**Scraped:** 2026-03-05T10:03:44.920476Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage unified rules
Supported in:
Google secops
SIEM
This document outlines the capabilities for managing both curated and custom
rules within the unified rules interface. It describes the
functionalities on the
Rules
page, the integrated development environment
(IDE) features within the Rules editor, and the management of curated rules.
Understand unified Rules page features
The
Rules
page provides a single, unified interface for managing both custom
and curated rules. The following table outlines the core capabilities
available to help you optimize your rule management workflow.
Feature
Description
Action
Unified rule list
Displays custom and curated rules in a combined list.
Browse and manage all rules from a single location.
Search
Supports structured search across all rule text by default.
See Search the rules page for advanced filtering options.
Quick filters
Provides initial filtering options to narrow the rule list.
Filter the list to display
All
rules,
Live
rules,
Alerting
rules,
Custom
rules,
   or
Non-archived
rules.
Column customization
Lets you customize the visibility of data columns in the rules table.
Click
view_column
view
   column to show or hide columns.
Rule preview
Displays the rule summary on the Rules dashboard.
View the rule summary by clicking a row in the rule list (anywhere except the rule name).
View pivoting
Enables quick navigation to related rule views (editor, detection, or rule pack management).
Hold the pointer over a row to view the
Actions
menu. Click the
Actions
menu and select the required view.
Multi-select actions
Updates the rule configuration for multiple rules simultaneously.
Click
view_column
view
   column and select
Actions
to view the selector box on each row. Then choose an action from the
Actions
menu.
Use the Rule editor
The Rules editor supports both curated and custom rules.
It provides real-time contextual assistance to improve the
rule development workflow. Hold the pointer over a UDM field to view its definition, or
over an error highlight to inspect specific error details.
Understand the rule details panel
When you select a rule from the table, the rule details panel opens. This panel
organizes rule information into the following tabs:
Overview tab
: Displays the rule's metadata (such as
created_time
,
author
, and
rule_type
) and applied tags. You can also use the built-in
tag assigner to add or remove MITRE tags.
Logic tab:
Provides an inline IDE where you can do the following:
View the rule text for both custom and curated rules.
Update rule text and scope (custom rules only).
Run rule testing (custom rules only).
Update alerting and detecting status (custom rules only).
Create a new rule from a default template.
Manage curated rules
The unified interface provides granular control and visibility over curated
rules, letting you to do the following:
Search for curated rules.
View curated rule text.
Control live status and alerting status of each curated rule independently
from the parent rule set deployment status.
Search for curated rules
You can view curated rules from the Rules dashboard. You can filter the
dashboard using the following methods:
Quick filter:
Select the
Curated
rule owner quick filter.
Structured search:
Use the filter query
rule_owner:GOOGLE
in the search
box. Additionally, structured search supports searching on logic within the curated
rule text. Use the filter query
text:keyword rule_owner:GOOGLE
to perform
keyword search on curated rules. See
Search the rules list
for more details.
View curated rule text
You can view curated rule texts from the rule preview panel in the Rules
dashboard. To access the preview panel, click a row in the Rules table
(any empty space on the row that's not the rule name), and view the text in
the preview panel.
Control deployment status of a curated rule
You can override the parent rule set's deployment configuration for individual
curated rules from the dashboard. Update live and alerting status for a single
curated rule using the following methods:
Status toggle:
On the Rules dashboard, open the column management panel
and enable the
Status with Toggle
column. Toggle between
live
or
alerting
statuses for a rule.
Multi-select actions:
On the Rules dashboard, open the column
management panel and enable the multi-select actions column. Select one or
more rules to update using the multi-select checkboxes, and then select an
action from the
Actions
menu.
Need more help?
Get answers from Community members and Google SecOps professionals.
