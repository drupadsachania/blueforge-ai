# Insights

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/insights/  
**Scraped:** 2026-03-05T09:37:05.781228Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Insights
Supported in:
Google secops
SOAR
This document lists the parameters used for entity insight actions to power up playbook capabilities.
Use these actions to generate insights within the case overview, providing high-visibility data points extracted from enrichment results.
Actions
Create Entity Insight From Enrichment
Generates an entity insight based on a formatted string, incorporating data from a previous enrichment step.
Description
Creates an entity insight from an enrichment action.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Message
String
N/A
Yes
Formatted string that incorporates entity enrichment.
Triggered By
String
Siemplify
No
Integration name associated with the insight.
Example
This example shows parsing output from a previous VirusTotal enrichment action to generate a system insight. The resulting message is surfaced within the
Insights
section of the case overview for analyst review.
Action Configurations
Parameter
Value
Entities
All entities
Message
Is Risky: [VirusTotalV3_Enrich IP_1.JsonResult | "is_risky"]
Triggered By
VirusTotal
Action results
Script Result Name
Value Options
Example
ScriptResult
true
or
false
true
Create Entity Insight From JSON
Description
Generates an entity insight by parsing a specific JSON object and mapping it to a target entity.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
JSON
JSON
N/A
Yes
Raw JSON object used to produce the insight.
Identifier KeyPath
String
N/A
Yes
Dot-notation path to the key that contains the entity identifier.
Message
String
N/A
Yes
Formatted string for the insight display.
Triggered By
String
Siemplify
No
Name of the integration associated with the insight.
Example
This example creates an entity insight based on an IP entity from a JSON.
Action Configurations
This configuration aggregates telemetry from VirusTotal into a unified view. It creates an entity insight based on an IP entity from a JSON.
Parameter
Value
Entities
All entities
JSON
[{"ip":"172.26.240.1","vt_score":"4"}]
Identifier KeyPath
ip
Message
VirusTotal Score
Triggered By
VirusTotal
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
true
or
false
true
Create Entity Insight From Multiple JSONs
Aggregates data from up to five separate JSON sources into a single, multi-section entity insight.
Description
Creates an entity insight from an enrichment action.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Fields
String
N/A
No
Fields to extract from the fourth JSON string.
JSON4
JSON
N/A
No
Fourth JSON string to parse for the insight.
Title5
String
N/A
No
Title for the fifth entity section.
Fields5
String
N/A
No
Fields to extract from the fifth JSON string.
JSON5
JSON
N/A
No
Fifth JSON string to parse for the insight.
Placeholder Separator
String
,
No
String to break the lines.
Title1
String
N/A
No
Title to use for the first entity section.
Fields1
String
N/A
No
Fields to extract from the first JSON string.
JSON1
JSON
N/A
No
First JSON string to parse for the insight.
Title2
String
N/A
No
Title to use for the second entity section.
Fields2
String
N/A
No
Fields to extract from the second JSON string.
JSON2
JSON
N/A
No
Second JSON string to parse for the insight.
Title3
String
N/A
No
Title to use for the third entity section.
Fields3
String
N/A
No
Fields to extract from the third JSON string.
JSON3
JSON
N/A
No
Third JSON string to parse for the insight.
Title4
String
N/A
No
Title to use for the fourth entity section.
Example
This example creates an entity insight based on an IP entity
  and enriches it with VirusTotal and Crowdstrike information.
Action Configurations
Parameter
Type
Entities
All entities
Fields4
Blank
JSON4
Blank
Title5
Blank
Fields5
Blank
JSON5
Blank
Placeholder Separator
Blank
Title1
Virustotal Score
Fields1
Entity
JSON1
[{"Entity": "172.26.240.1", "vt_score":"4",
"EntityResult":"true"}]
Title2
Crowdstrike Score
Fields2
Entity
JSON2
[{"Entity": "172.26.240.1", "crowdstrike_score":"4",
"EntityResult":"true"}]
Title3
Blank
Fields3
Blank
JSON3
Blank
Title4
Blank
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
true
or
false
true
Need more help?
Get answers from Community members and Google SecOps professionals.
