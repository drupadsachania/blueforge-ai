# Investigate entities and alerts

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/explore-entities-and-alerts-investigation/  
**Scraped:** 2026-03-05T09:34:13.760354Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Investigate entities and alerts
Supported in:
Google secops
SOAR
This document explains how to investigate case-related entities and alerts
using the
Security Graph
page in Google Security Operations. The
Security Graph
page
provides a visual representation of entity relationships and alert activity,
helping you understand the context, sequence, and impact of suspicious events.
This document also explains how to interpret entity types, explore correlations,
and perform follow-up actions based on the visual analysis.
You can explore the entities and alerts associated with a case using the
Security Graph
page. In the center of the page, a visual representation—called a visual
family—displays how alerts and entities relate to one another.
This view helps you:
Understand the cause-and-effect relationships between entities and alerts
See the chronological order of events
Identify connections between suspicious activities
events
Identify visual family elements
The visual family includes two types of nodes:
Entities
: Displayed as hexagons
Artifacts
: Displayed as circles
Color is used to convey meaning:
Blue hexagons
: Internal entities
Green circles
: Internal artifacts
Red
: Indicates suspicious items
Identify internal and external entities
Entities can appear in two styles:
Color-filled shapes represent internal entities
Outlined-only shapes represent external entities
For example, an IP address that belongs to a known internal network would
appear as a color-filled hexagon, signaling it's internal. Conversely, an IP
from outside the network appears as an outlined hexagon, indicating it's external.
Understand entity relationships in the visual family
The
Security Graph
page shows how entities and artifacts relate to each other
using visual cues and connections. To identify different types of entities and
artifacts, click
help
Help
.
This opens the
Entity Legend
, which defines each shape and color used in
the visual.
Relationship types
Entities and artifacts may be linked by lines that represent their relationships.
There are two types of relationships:
Actions
: Displayed as arrows; indicate a direct action (for example,
sending an email)
Connections
: Displayed as dotted lines; show general associations
(for example, a user tied to a machine hostname)
For example:
An arrow may connect two user entities if one sends an email to the other.
A dotted line might connect a user entity with a host entity they've accessed
Visual families and mapping rules
Entities and artifacts are derived from mapping rules, and their relationships (connected by lines) are defined by visual families.
If visual families aren't configured, entities and artifacts still appear in the center workspace. However, no connecting lines are displayed between them.
Configure mapping and visual families
To configure mapping rules or assign visual families on the
Event Configuration
page, click
settings
Settings
in one of the following places in the Google SecOps platform:
Alerts Events tab
Ontology Status page
For more details about how to configure mapping and assign visual families,
see
Configure mapping and assign visual families
.
Use the Security Graph page
To analyze entities and alerts visually, open a case and on the
Cases
page, click
View Security Graph
. The
Security Graph
page contains the following workspace elements:
Left pane
: displays the alerts associated with the selected case and their corresponding timestamps.
Middle pane
: displays a graph of interconnected entities, a graphical alert timeline, and playback controls.
Side drawer
: shows details of the selected alerts or
entities, including raw enrichment data (if available). When you select an alert or
an event, the side drawer displays the relevant information.
If you're a Google SecOps user, you'll see an
Explore
button at the bottom of this drawer. Click it to continue investigating the alert
on a dedicated page. For more information,
see
Investigation views
.
Bottom of page
: displays video control buttons to play the
events, together with a visual time range (which can be manipulated further
using
add
Add
and
remove
Remove
). Click
play_arrow
Play Event
to go through the events in chronological
order on the graph.
Click an alert in the left pane to highlight the related entities highlighted in the
middle pane. The node indicating this alert appears bigger than the other nodes
(alerts) on the graph. Hold the pointer over the nodes to see their
respective alert names. Entities not involved in the selected alert appear dimmed (unavailable).
The following options are available on the
Security Graph
page:
Options
Descriptions
Fit to Screen
: autofits
    the graph to fit the entire visible area.
Circular layout
: default graph layout. Click
Change Graph Layout
for other options.
Play Event
: plays all alerts of the case in sequence.
    Highlights associated entities for each step. The graph displays the alert flow, highlighting each played alert with a larger node.
Next Event
: plays the next alert in order. Starts from the top of the list.
Previous Event
: steps back to the previous alert. Disabled until the first alert is played.
Fast Forward
and
Fast Backward
: plays alerts at 3× speed, in chronological (ascending) or reverse chronological (descending) order, respectively.
Time Range Slider
: expands or narrows the visible time range on the X-axis.
This opens an entity legend.
Take manual action after investigation
After reviewing the visual timeline, you can take further manual actions for
    further investigation. For example, you can scan IP addresses to check for
    known threats or investigate downstream effects like data exfiltration.
Common follow-up actions include:
Quarantine computers
Check and scan infected systems
Investigate suspicious emails
Identify missing or exfiltrated data.
Supported entity types in Google SecOps
This section provides a list of the supported entity types that can be utilized within the Google Security Operations platform for security investigation, analysis, and enrichment.
0: "SourceHostName"
1: "SourceAddress"
2: "SourceUserName"
3: "SourceProcessName"
4: "SourceMacAddress"
5: "DestinationHostName"
6: "DestinationAddress"
7: "DestinationUserName"
8: "DestinationProcessName"
9: "DestinationMacAddress"
10: "DestinationURL"
11: "Process"
12: "FileName"
13: "FileHash"
14: "EmailSubject"
15: "ThreatSignature"
16: "USB"
17: "Deployment"
18: "CreditCard"
19: "PhoneNumber"
20: "CVE"
21: "ThreatActor"
22: "ThreatCampaign"
23: "GenericEntity"
24: "ParentProcess"
25: "ParentHash"
26: "ChildProcess"
27: "ChildHash"
28: "SourceDomain"
29: "DestinationDomain"
30: "IPSET"
31: "Cluster"
32: "Application"
33: "Database"
34: "Pod"
35: "Container"
36: "Service"
Need more help?
Get answers from Community members and Google SecOps professionals.
