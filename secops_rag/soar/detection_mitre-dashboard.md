# Understand threat coverage with the MITRE ATT&CK matrix

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/mitre-dashboard/  
**Scraped:** 2026-03-05T10:03:40.680511Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand threat coverage with the MITRE ATT&CK matrix
Supported in:
Google secops
SIEM
This document describes how to use the MITRE ATT&CK matrix dashboard in
Google Security Operations. The matrix helps you understand your organization's security
posture against the MITRE ATT&CK framework. It also helps you find gaps in your
threat coverage and prioritize your security tasks.
Understand tactics and techniques
In the
MITRE ATT&CK framework
,
the following are the fundamental concepts used to categorize adversary
behavior.
Tactic
: High-level goal that an attacker is trying to achieve. For example,
common tactics include
Initial Access
(getting into the network),
Persistence
(staying in the network), and
Exfiltration
(stealing data).
Technique
: The specific method used to achieve a tactic. For example, an
attacker might use the
Phishing
technique to gain
Initial Access
tactic.
Each tactic has different techniques that an adversary could use.
Sub-technique
: A sub-technique provides a more specific description of
how a technique is executed. It details the process or mechanism to accomplish
the goal of a tactic. For example,
Spearphishing Attachment
and
Spearphishing Link
are sub-techniques of the
Phishing
technique.
The following tactics are displayed in the MITRE ATT&CK matrix:
MITRE ATT&CK tactic
Description
Collection
Gather data.
Command and control
Contact controlled systems.
Credential access
Steal login and password information.
Defense evasion
Avoid detection.
Discovery
Figure out your environment.
Execution
Run malicious code.
Exfiltration
Steal data.
Impact
Manipulate, interrupt, or destroy systems and data.
Initial access
Gain entry to your environment.
Lateral movement
Move through your environment.
Persistence
Maintain foothold.
Privilege escalation
Gain higher-level permissions.
Reconnaissance
Gather information to use in future malicious operations.

This tactic displays in the matrix only when the
PRE
platform
is selected in your user preferences.
Resource development
Establish resources to support malicious operations.

This tactic displays in the matrix only when the
PRE
platform is selected in
your user preferences.
Common use cases
This section lists some common use cases for using the MITRE ATT&CK matrix.
Identify new detection opportunities
Goal
: as a security analyst, you want to proactively improve your
organization's security posture by expanding detection rule coverage.
Task
: find areas where you have the necessary
data to build new detections but have no rules in place.
Steps
:
Open the MITRE ATT&CK Matrix.
Scan the matrix for technique cards that show a low or zero rule
count.
Find a technique card that displays "0 rules" but lists available log types.
Click the card to open the technique details panel.
Review the log sources list to confirm that these are
reliable, high-volume data feeds.
Result
: identify a high-value detection opportunity. You
know you are successfully ingesting the correct data to detect this technique,
and you can now proceed with creating a new rule to close this coverage gap.
Respond to a new threat advisory
Goal
: the Cybersecurity and Infrastructure Security Agency (CISA)
issues an alert about a new ransomware attacking your industry.
Task
: as a detection engineer, you need to know if your current
security rules can detect the specific tactics, techniques, and procedures
(TTPs) used by this new threat.
Steps
:
Open the MITRE ATT&CK matrix.
Filter the matrix to highlight the techniques mentioned in
the CISA alert (for example,
T1486: Data Encrypted for Impact
,
T1059.001: PowerShell
).
Observe the matrix. You find that the matrix shows that
PowerShell
is
well-covered, but
Data Encrypted for Impact
is a critical gap with
"No Coverage".
Result
: you find a high-priority gap in your defenses. You
can now create a new detection rule to cover the ransomware behavior.
Tune and improve existing detections
Goal
: after a recent security incident, as a security engineer, you need
to improve the quality of the detections that were triggered.
Task
: you want to see all data points for a
specific technique. This helps you decide if your existing rules are using the best
data sources and logic.
Steps
:
Open the matrix and click the technique
T1003: OS Credential Dumping
.
The
Details
view shows the two rules for this technique.
Notice that both rules use older command-line logs. However, the
data source widget shows that the new EDR tool provides
higher-fidelity data for this technique.
Result
: you find a clear way to improve detection quality.
You can now create a new, more robust rule using the EDR
data. This leads to fewer false positives and a better chance of catching
complex credential dumping attacks.
Before you begin
For your custom rules to appear in the matrix and count toward threat coverage,
you must map them to one or more MITRE ATT&CK techniques.
To do this, add a
technique
key to the rule's
metadata
section. The value
must be a valid MITRE ATT&CK technique ID or multiple IDs as a comma-separated
string.
Example
:
metadata: technique="T1548,T1134.001"
New rules appear in the matrix within a few minutes.
Access the MITRE ATT&CK matrix
To access the MITRE ATT&CK matrix, do the following:
Log in to Google SecOps
.
From the navigation menu, click
Detection
>
Rules & Detections
.
Navigate to the
MITRE ATT&CK Matrix
tab.
The MITRE ATT&CK matrix appears.
Use the MITRE ATT&CK matrix
The matrix displays MITRE ATT&CK tactics as columns and techniques as
cards within those columns. Each technique card is color-coded to indicate
the current status and depth of your detection coverage for that technique.
On the technique cards, you can view the following:
Sub-technique indicators
: the small, colored indicators
represent the associated sub-techniques. The color of each indicator corresponds
to the number of rules for that sub-technique. Hold the pointer over an indicator to see
its name.
Sub-technique toggle
: to simplify the main matrix and reduce visual noise,
open the
View options
menu and clear the
Display sub-techniques
checkbox.
Log type count
: displays the log types associated with the technique.
If a technique has zero rules, the technique card can display a count of
associated log types (for example, "7 log types"). This indicates a detection
opportunity, showing that you have the necessary data to create rules for that
technique.
Refine the coverage calculation
To refine the coverage calculation, use the lists for
Rule type
,
Live status
, and
Alerting status
to refine your coverage calculations.
Search for techniques
Use the search bar to find a specific technique by name (for example,
Windows Command Shell
) or ID (for example,
T1059.003
). For rule names, log
types, or MITRE data sources, use the
Search by
menu to narrow the
results.
View technique details and log sources
Click any technique card to open the technique details side panel. This panel
provides information about the technique and your organization's ability to
detect it.
The panel contains the following information:
MITRE description
: the official description of the technique from the MITRE
ATT&CK framework.
Sub-techniques
: all the sub-techniques associated with the technique. The
colored chip next to each ID indicates the number of rules for that specific
sub-technique.
Curated rules
: a comprehensive list of all associated rules for that technique.
Log sources
: log sources that correspond to the MITRE data sources for the
technique that have actively sent data in the past 30 days.
Export data
Click
Export
to download the current matrix view as a
JSON
file. This file
is compatible with the official MITRE ATT&CK navigator tool for further analysis.
Need more help?
Get answers from Community members and Google SecOps professionals.
