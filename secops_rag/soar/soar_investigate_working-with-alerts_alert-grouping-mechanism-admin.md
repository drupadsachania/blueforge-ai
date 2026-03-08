# Configure an alert grouping

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/alert-grouping-mechanism-admin/  
**Scraped:** 2026-03-05T10:07:39.091789Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure an alert grouping
Supported in:
Google secops
SOAR
The
alert grouping
mechanism groups alerts into cases, providing
  security analysts with better context to address issues effectively. The goal
  is to accentuate the importance of additional context to a security
  alert and avoid situations where analysts investigate the same incident
  without proper context, potentially wasting time or mishandling the incident.
You can configure the alert grouping mechanism
 in
SOAR Settings
>
Advanced
>
Alerts Grouping
.
The
General
section includes cross-platform settings:
Max. alerts grouped into a case
:
    Define the maximum number of alerts to group together into one case (30).
    After the maximum number is reached, a new case is started.
Timeframe for grouping alerts (in hours)
: Set the number of hours
    with which to group the alerts for the case (ranges from 0.5-24 hours in
    half-hour intervals). This doesn't apply to rules grouped by source
    grouping identifier.
Group entities and source grouping identifiers in the same case
: When
    enabled, an alert that should be grouped by source grouping identifier
    according to the grouping rule, first looks for alerts with the same
    source grouping identifier, and if it doesn't find any, it looks for all
    cases in the system with mutual entities and group alerts accordingly (and
    according to the cross-platform timeframe).
    Source Grouping Identifier alert grouping is solely based on
sourceGroupIdentifier
and
maxAlertsInCase
. 
    It doesn't use a timeframe.
Rules
The
Rules
section lets you create specific rules targeting
  different grouping options.
Grouping example
The alert grouping mechanism lets you create grouping rules controlling
  the exact type of alerts which are grouped together into cases. As a basic example
  of grouping, an alert
C&C traffic
with
  destination host
10.1.1.13
is added at 10:00 AM to a case called
Malware
  Found
.
Another alert,
User account changed
with the same destination host, is
  seen at 11:00 AM. Google Security Operations identifies the same entity which is
  involved in both alerts and within the configured timeframe, groups the
  second alert into the
Malware Found
case.
Rule hierarchy
The rules work on a hierarchical system whereby each incoming alert is matched against a
  rule in the following order:
Alert Type
: For example, a phishing alert.
Product
: For example, Cybereason EDR.
Data Source
: For example, Arcsight SIEM.
Fallback Rule
: Used when no match is found for the alert type,
  product, or data source.
Once a rule is matched, the system stops checking. If an alert
  matches a rule, and there's no existing case to group to, then it
  is added to a new case. You can't create two rules on the same hierarchy
  for the same value. For example: Data source - ArcSight can have one rule
  only.
Fallback rule
The platform has a prebuilt rule that can't be deleted. This
  fallback rule provides a general catchall for alerts to ensure that there's
  always grouping in cases. However, you can edit these options:
Group By
: Choose between
Entities
or
Source Grouping
    Identifier
(for alerts coming with a pre-existing group ID attached to
    them from the originating system. For example, QRadar alerts have an 
    identifier called
offense
, which is the group ID they belong to in
    QRadar.)
Grouping Entities
(by directions): Relevant for entities only.
Don't Group rule
The
Don't Group
rule let you treat alerts independently
(they won't be grouped with other alerts into cases). This is
useful when a specific alert needs to investigate independently without being
linked to other cases.
For more information about excluding specific entities from alert grouping,
 see
Create blocklist to exclude entities from alerts
.
When using
Grouping Entities
in a rule, the system requires only one 
  matching entity for alerts to be grouped together.
For example, a grouping rule specifies the following entities:
Source IP
Destination IP
Username
If an alert matches any one of these entities, it's grouped with an 
existing case containing that entity, even if the other entities don't match.
Consider the following two alerts:
Alert 1
:
Source IP address:
192.168.1.10
Destination IP address:
10.0.0.5
Username:
user123
Alert 2
:
Source IP address:
192.168.1.10
Destination IP address:
10.0.0.6
Username:
user456
Because both of these alerts have the same
Source IP address
(
192.168.1.10
), they'll be grouped into the same case, even 
  though the
Destination IP address
and
Username
are different.
Create rules for specific use cases
The next sections describe use cases for creating dynamic and context-aware alert grouping rules.
Use Case: Alert grouping by source and entity
An enterprise company using two connectors, Arcsight and Cybereason EDR, wants
  to group Arcsight alerts by both source and destination entities, and
  Cybereason EDR alerts by specific criteria:
Arcsight alerts
: Group by source and destination entities.
Cybereason EDR Phishing alerts
: Group by source entities only.
Group Cybereason EDR Failed Login alerts
: Group by destination
  entities only.
To capture this use case, build the following rules. Google SecOps provides the final rule as the
fallback
rule.
Rule One
:
Category = Data Source
Value = Arcsight
Group by = Entities
Grouping Entities = Source and Destination
Rule Two
:
Category = Alert Type
Value = Phishing
Group by = Entities
Grouping Entities = Source (SourceHostName, SourceAddress, SourceUserName)
Rule Three
:
Category = Alert Type
Value = Failed Login
Group by = Entities
Grouping Entities = Destination (DestinationAddress, DestinationUserName)
Rule Four (fallback)
:
Category = All
Value = All Alerts
Grouping Entities = All Entities
Use Case: Adaptive grouping logic
An MSSP has a customer who is using the QRadar connector, and wants to group
  alerts in the same way they appear in QRadar. They also have another customer
  using Arcsight, and want to group by common entities for this customer's
  alerts, except for phishing alerts, which should be grouped by destination
  entities.
To capture this use case, build the following rules:
Rule One
:
Category = Data Source
Value = QRadar
Group by = Source Grouping Identifier
Grouping Entities = (leave blank)
Rule Two
:
Category = Data Source
Value = Arcsight
Group by = Entities
Grouping Entities = All Entities
Rule Three
:
Category = Alert Type
Value = Phishing
Group by = Entities
Grouping Entities = Destination (DestinationAddress, DestinationUserName)
Rule Four (fallback)
:
Category = All
Value = All Alerts
Grouping Entities = All Entities
Need more help?
Get answers from Community members and Google SecOps professionals.
