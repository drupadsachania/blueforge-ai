# Timestamp Definitions

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/timestamp-definitions/  
**Scraped:** 2026-03-05T10:06:08.847932Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Timestamp Definitions
Supported in:
Google secops
SIEM
This document explains common timestamps for events and detections.
For more information about timestamps, see
Date function
.
The following timestamps are related to events:
Event timestamp
: Time when an event occurred and is stored in the
metadata.event_timestamp
UDM field. Rules and UDM searches use the
metadata.event_timestamp
field for queries.
Collected timestamp
: Time when an event was collected by the local collection
infrastructure, such as the forwarder. This is stored in the
metadata.collected_timestamp
UDM field.
Ingested timestamp
: Time when an event was ingested by Google Security Operations.
This is stored in the
metadata.ingested_timestamp
UDM field.
The following timestamps are stored with detections:
Detection window
: For rules with a
match
section
,
a detection is created over the time range, called
the
detection window
. The event timestamps for events that triggered the detection
are within the detection window.
Detection timestamp
: For rules with a
match
section, the detection
timestamp is the end time of the detection window. Otherwise, the detection
timestamp is the
metadata.event_timestamp
of the event that generated the
detection.
Detection created timestamp
: Date and time the detection was created by
detection engine.
Where timestamps appear in the application
The following sections define where you can view these timestamps in the UI.
UDM Event viewer
To open the
UDM Event
view, do the following:
Perform a UDM Search.
In the
Events
tab, select an event to open the
Event viewer
The
UDM event
pane displays the following data:
Event timestamp is stored in the
metadata.event_timestamp
UDM field (1).
Ingested timestamp is stored in the
metadata.ingested_timestamp
UDM field (2).
Detections panel
To open the
Detections
view, do the following:
Open
Detections
>
Rules & Detections
, and then click the
Dashboard
button.
Click the rule name link under the
Rule name
column. The
Detections
panel appears and displays the following:
Detection timestamp appears in rows that identify a detection (1).
Event timestamp appears in rows that identify events (2).
Alert view
To open the
Alert
view, do the following:
Open
Detections
>
Alerts & IOCs
.
Under the
Alerts
tab, click the alert name link in the
Name
column.
Click the
Overview
tab to display the following:
Alert (or Detection) created timestamp appears in the
Alert Details
pane >
Created
field (1).
Detection window appears in the
Detection Summary
pane >
Detection window
field (2).
Detection timestamp appears is in the
Detection Summary
pane >
Alerts detected at
field (3).
Need more help?
Get answers from Community members and Google SecOps professionals.
