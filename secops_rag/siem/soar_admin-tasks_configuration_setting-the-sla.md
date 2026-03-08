# Set SLA expectations

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/setting-the-sla/  
**Scraped:** 2026-03-05T09:15:52.643254Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set SLA expectations
Supported in:
Google secops
SOAR
A Service Level Agreement (SLA) represents a commitment by the SOC to perform
  specific tasks, such as investigating or remediating a case within
  a set timeframe. You can configure SLAs for alerts, cases, or both.
Understand the SLA types
Alert SLA
: the maximum time to close an alert. An alert SLA is
      mainly based on alert attributes (for example,
Alert Type
or
Alert Priority
),
      but can also be based on case attributes. The start time begins when the alert is created.
Case SLA
: the maximum time to close a case. A Case SLA is
      mainly based on case attributes (for example,
Case Stage
or
Case Priority
), but can also be based on alert attributes. The start time begins when the case is created, unless the SLA is configured by
Case Stage
—in which case it begins when the stage starts.
You can configure an SLA in
Settings
or automatically using a playbook action.
Manage SLAs
This section explains how to manage SLAs in your environment, including how
to create new rules and how to pause and resume them during an investigation.
Set SLA priorities
If multiple SLA rules are set, the system follows a clear priority order:
Case SLAs
: Playbook action
>
Case Stage
>
Case Priority
Alert SLAs
: Playbook action
>
Alert Type
>
Alert Priority
Add an SLA
To add an SLA, follow these steps:
Go to
Settings
>
Environments
>
SLA
.
Click
add
Add
.
Select whether the SLA is based on alert attributes (type or priority) or case attributes (stage or priority).
Define the timeframes for the
SLA Period
(the time before an SLA is breached)
     and the
SLA Time to Critical Period
(the time before the SLA enters a critical phase). For example, an
SLA Period
of 10 minutes and an
SLA Time to Critical Period
of 6 minutes results in a 4-minute critical period.
Click
Add
.
Interpret an SLA Status
An SLA status is indicated by an
hourglass
hourglass icon. A
'C'
next to the
hourglass
hourglass icon indicates a
Case
SLA, while an
A
indicates an
Alert SLA
. The icon's color shows its status as follows:
Green: The SLA is active.
Gray: The SLA is paused.
In the
Cases
tab, a green countdown timer indicates an active case SLA at the top. For cases with multiple alerts, the
Alerts
icon in the header displays all alert SLAs. Each Alert SLA
  can be clicked to view the individual alert.
Pause and resume an SLA
You can pause SLAs to provide flexibility during investigations. Pausing a
case SLA doesn't affect an alert SLA, and the other way around. All pause and
resume events are recorded on the
Case Wall
.
Pause an alert SLA
To pause an alert SLA, do the following:
On the
Cases
page, select the case with the relevant 
  alert.
In the alert tab, click
more_vert
More
>
Alert Options
.
Select
Pause alert SLA
.
Optional: In the
Pause alert SLA
dialog, 
  enter a reason for pausing the SLA.
Click
Pause
.
A gray
hourglass
hourglass
    in the
Alert
tab indicates that the SLA is paused and a tooltip also
    indicates the paused status.
Resume an Alert SLA
To resume the Alert SLA, do the following:
Click
more_vert
More
Alert Options
.
Select
Resume alert SLA
.
The green hourglass in the
Alert
tab indicates that the SLA is running again. 
The alerts icon in the case top bar also shows a countdown timer that has 
resumed ticking for the resumed Alert SLA.
Pause a case SLA
To pause a case SLA, do the following:
On the
Cases
page, select the relevant case.
Click
format_list_bulleted
Menu
>
Case Actions
.
Select
Pause Case SLA
.
Optional: In the
Pause Case SLA
dialog, 
  enter a reason for pausing the SLA.
Click
Pause
.
The case SLA timer in the header turns gray and stops. 
A tooltip also indicates the paused status.
Resume a case SLA
To resume a paused case SLA, do the following:
In the case top bar, click
format_list_bulleted
Case Actions
.
Select
Resume Case SLA
.
The timer turns green and resumes the countdown.
Need more help?
Get answers from Community members and Google SecOps professionals.
