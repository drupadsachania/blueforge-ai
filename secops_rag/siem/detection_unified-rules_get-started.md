# Get started with unified rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started/  
**Scraped:** 2026-03-05T09:31:20.214354Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Get started with unified rules
Supported in:
Google secops
SIEM
The unified rules interface provides deployment and management capabilities for
custom and curated rules. This document provides information on getting
started with the unified rules interface, and the required permissions for
access.
The interface consists of the following components:
Rules dashboard:
A centralized management and monitoring console. It
provides real-time visibility into rule status, execution metrics, and
deployment history across all environments.
Rules editor:
A unified interface for viewing and authoring rules.
Rules API:
API endpoints for Create, Read, Update, and Delete (CRUD)
operations on rules.
Required permissions
This section lists the permissions you need for accessing the unified rules
dashboard and editor.
Rules dashboard
Permission
Required IAM permission
View
chronicle.rules.list
chronicle.retrohunts.list
chronicle.ruleDeployments.list
chronicle.legacies.legacySearchCustomerStats
chronicle.legacies.legacyGetRuleCounts
chronicle.legacies.legacyGetRulesTrends
chronicle.legacies.legacyGetCuratedRulesTrends
Edit
chronicle.retrohunts.create
chronicle.ruleDeployments.update
chronicle.ModifyRules
Rules editor
Component
IAM permission (if you use IAM)
Analyst permission (if you use legacy RBAC)
Rules editor
page
chronicle.ruleDeployments.list
chronicle.rules.list
detectRulesView
Related reference list section
chronicle.referenceLists.get
chronicle.referenceLists.list
referenceListView
Related data table section
chronicle.dataTables.get
chronicle.dataTables.list
N/A
Create new rule
button
chronicle.rules.verifyRuleText
chronicle.rules.create
detectRulesCreate
Test rule
button
chronicle.legacies.legacyRunTestRule
detectRulesRun
Rule scope
menu
chronicle.rules.update
detectRulesEdit
Save rule
button
chronicle.rules.update
detectRulesEdit
Save as new rule
button
chronicle.rules.create
detectRulesCreate
Rule retro hunt
button
chronicle.retrohunts.create
detectRulesRun
Rule live
toggle
chronicle.ruleDeployments.update
detectRulesEdit
Rule alert
toggle
chronicle.ruleDeployments.update
detectRulesEdit
Rule run frequency
toggle
chronicle.ruleDeployments.update
detectRulesEdit
Rule archive and unarchive
toggle
chronicle.ruleDeployments.update
detectRulesEdit
View curated rule in editor
chronicle.featuredContentRules.list
N/A
Opt-in to the unified Rules dashboard
Go to the
Rules dashboard
page.
Click
Try Our New Unified Rules Page
.
Your instance always loads the unified
Rules dashboard
page by default.
Opt-out of the unified Rules dashboard
To return to the legacy Rules dashboard, do the following:
Go to the
Rules dashboard
page.
Click
Go back to the Legacy Rules Dashboard
.
Your instance always loads the legacy
Rules dashboard
page by default.
Opt-in to the unified Rules editor
Go to the
Rules editor
page.
Click
New Rule Editor page
.
Your instance loads the unified
Rules editor
page by default.
Opt-out of unified Rules editor
To return to the legacy
Rules editor
page, do the following:
Go to the
Rules editor
page.
Click
Legacy Rules Editor page
.
Your instance loads the legacy
Rules editor
page by default.
What's next
Manage unified rules
Search the unified rules list
Need more help?
Get answers from Community members and Google SecOps professionals.
