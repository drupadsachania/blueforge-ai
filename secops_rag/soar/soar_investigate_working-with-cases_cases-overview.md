# Cases overview

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview/  
**Scraped:** 2026-03-05T10:06:45.007942Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Cases overview
Supported in:
Google secops
SOAR
Google Security Operations ingests alerts from a wide range of sources. Each
  alert includes its underlying security events and key indicators (such as
  sources, destinations, artifacts), which are parsed and analyzed. During this
  analysis, key indicators—such as source and destination IPs, file hashes, or
  user accounts—are extracted and represented as entities.
  Entities are persistent objects in the platform. They collect enrichment data,
  analyst comments, and historical context, letting analysts track entity
  behavior over time and across cases. Entities also appear on the visual
  canvas to help illustrate relationships in the threat landscape.
Case creation and grouping
The
Cases
page is where analysts can investigate incoming alerts and
  manage incident workflows. You can also automatically group additional alerts
  into existing cases based on shared entities and configurable rules. Analysts can also:
Automatically group additional alerts into existing cases based on shared
  entities and configurable rules.
Manually create cases or simulate cases for testing and training purposes.
Case queue header and views
All active cases from various connectors appear in the case queue. Each case
  entry shows key metadata, such as:
Case name and unique ID
Case timestamp
Number of associated alerts
Assigned analyst (with avatar)
Case priority and stage (optional, depending on view)
Analysts can toggle between these views:
Default view
: Shows case cards with essential information.
Compact view
: Reduces visual footprint for faster scanning.
List view
: Displays all cases in a table format for bulk operations or filtering.
Case top bar
The
Case Top Bar
displays case-level context and available actions,
  as follows:
The case queue header displays the case title, ID,
priority, stage
, timestamp, change environment, and
tags
.
It also shows the assigned analyst (name or role), and includes controls for
Chat
,
Close Case
,
Refresh
,
Explore
, and the
Case Actions
menu.
For details see
What's on the Cases page?
Case tab
Each case includes several tabs that help analysts review, investigate, and act on case data. These tabs organize key information—from high-level summaries to detailed logs and alert data—into a consistent, navigable format.
Case overview tab
The
Case Overview
tab displays case-specific widgets configured by the administrator. For details see
Explore the Case Overview tab
.
Case Wall tab
The
Case Wall
tab displays a chronological log of all case-related
  events and actions, from creation to closure. When you open this tab, you can
  view case-related information such as tasks, user comments, pinned chat
  messages, manual and system actions, and file attachments (up to 50 MB per file).
  Each type of content is represented by an icon in the upper section of the
  Case Wall.
Actions you can do with this tab:
Click
View More
to display both the standard UI results and the corresponding JSON data.
To view event details, click one or more of the event icons.
Use the next to the icons to select a specific alert.
To view events for all alerts in the case, select
All Alerts
.
Icon
Description
Displays actions taken on alerts in a table, including the action name, timestamp, alert name, result, and status (
Completed
or
Faulted
).
Click
Show More
to expand the results, parameters, and affected entities. Click
Show Less
to collapse the view.
Displays all system- and user-generated case status changes, such as updates to the title, stage, priority, assignment, and closure.
Displays task-related activity. When a task is completed, click
Complete Task
. The status updates to
Completed
along with a timestamp and your comments.
Displays comments added manually or by the
Case Comment
action.
Displays pinned messages from the
Instant Message
dialog.
Displays items marked as favorites in the Case Wall by clicking the yellow star icon.
Sorts event logs by timestamp, either from newest to oldest or oldest to newest.
Displays general insights and warnings about the case and associated entities.
For details, see
What's on the Case Wall tab?
Alert Overview
tab: Lists all alerts linked to the case, including associated events and metadata.
  This tab displays crucial information and events associated with the case.
The case queue—automatically refreshed every minute—lists all active cases
  and lets you manually refresh, sort, filter, add, or close cases as needed.
Playbook automation
Playbooks
are predefined sets of actions that collect information
  from internal and external alert sources. They then make decisions on how to
  handle these alerts or perform operations on remote systems, such as blocking
  a firewall port or disabling an Active Directory user.
  Google SecOps performs these actions automatically or semi-automatically
  based on the playbook triggers on any alert ingestion.
Need more help?
Get answers from Community members and Google SecOps professionals.
