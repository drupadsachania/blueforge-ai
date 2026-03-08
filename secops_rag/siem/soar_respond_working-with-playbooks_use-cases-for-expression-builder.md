# Expression Builder use cases

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/use-cases-for-expression-builder/  
**Scraped:** 2026-03-05T09:35:11.124731Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Expression Builder use cases
Supported in:
Google secops
SOAR
This document provides uses cases that detail how to build and implement dynamic
expressions within playbook actions across the Google Security Operations platform.
It focuses on using the Expression Builder to parse, filter, and extract specific
data from previous action results—such as list data, entity details, and scan
reports—to drive complex automation logic in subsequent playbook steps.
Before you begin
Before you begin, follow these suggestions:
Use
Qualys – List Scans
to get all the latest scans from Qualys (30 days hard coded).
Use the Expression Builder to extract the ID (REF) of the newest scan as placeholder to download VM scan results. VM scan results download the relevant report.
Use
List Operations
to extract the list of the vulnerabilities' identifiers found on the network  common vulnerabilities and exposures (CVEs) from the report and compare it to the CVE from the case.
Use an IPS alert to trigger the playbook.
Use case: Intrusion Prevention System IPS
This use case assumes you're building a playbook that has found a malicious flow in
  a network.
Imagine that a vulnerability management tool, such as Qualys, has
  scheduled a daily scan.
Create a placeholder
To create a placeholder, do the following:
Begin with an
Active Directory_Enrich Entities
action to enrich all potentially affected entities.
Use
Qualys VM – List Scans
to retrieve the latest scan results for the network machines.
Determine if any of the results are vulnerable to the detected flow.
Look at
QualysVM_Download VM Scan Results_1
. You should see the placeholder and the added Expression Builder.
Add the placeholder
To add the placeholder, do the following:
Click [ ]
Placeholder
. The
Insert Placeholder
dialog appears.
Select
Playbook
>
QualysVM_list_Scans_1_JSONResult
.
Click the
Expression Builder
icon; the Expression Builder page appears.
In the
Expression
field, add the following: The expressions 
    use MAX to take the latest result by date
LAUNCH_DATETIME
and
    then extract the specific scan ID of the relevant scan
    where REF is the scan ID.
Example:
| max(LAUNCH_DATETIME) | REF
Click
Run
. The expected results should appear.
Click
Insert
to include the Expression Builder as part of the
    placeholder.
Click
Action
>
List operations
using CVEs from the cases + expression builder displays.
Once the playbook is triggered in real time, you can see the scan results in
    the side drawer, including the specific scan as a PDF file.
Use case: Too many failed login attempts
This use case addresses failed login attempts by enriching entity data to determine alert severity. The goal is to quickly find the user's department and their last password change date.
Start with the
ActiveDirectory_Enrich
entities action to gather detailed information on all internal entities associated with the alert.
In the subsequent Insight message, use the Expression Builder to extract the target user and their last login time.
Add the placeholder
To add these placeholders:
In the
Message
field, click
[ ] Placeholder
.
On the
Insert Placeholder
page, click the Expression Builder icon
    next to the
ActiveDirectory_Enrich entities_JSONResult
.
Add the following in the expression field: This will choose the entity
    identifier. If more than one entity returned results – we
    will get it as a comma separated list.
| Entity
Click
Run
; the sample result appears. In this case,
user@domain.com
.
Click
Insert
to use this as part of your placeholder message. Add the
    relevant free text to your message.
Click
[ ] Placeholder
and then click the Expression
    Builder icon next to the
ActiveDirectory_Enrich entities_JSONResult
.
Add the following expression. This captures the last logon time of the
    specified user. | EntityResult.lastLogon
Click
Insert
and then click
Save
.
Once the playbook is triggered in real time, a message on the
    Insight pane appears, showing the username and last login time.
Use case: VirusTotal hash analysis
This use case shows how to extract a file hash's reputation from a specific scan engine, such as Kaspersky, to determine if the file is malicious and create a corresponding entity.
Use the
VirusTotal_Scan Hash
action to retrieve the file report.
The subsequent action,
Siemplify_Create
or
Update Entity Properties
, creates or modifies an entity property, such as
Detected by Kaspersky
, based on the scan results.
To add this placeholder:
In the Field Value field, click
[] Placeholder
.
On the
Insert Placeholder
page, click the
Expression Builder
icon
    next to the
VirusTotal_ScanHash_JSONResult
.
Add the following expression:
|
    filter(EntityResult.scans.Kaspersky.detected, "=",
    "true") | Entity
If we scanned more than one hash, it filters the results by all the entity
    objects that Kaspersky marked as malicious, and then returns only the
    entity name.
Click
Insert
>
click
Save
. Results appear at run time.
Need more help?
Get answers from Community members and Google SecOps professionals.
