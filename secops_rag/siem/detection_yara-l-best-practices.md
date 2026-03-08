# YARA-L 2.0 rule structure and best practices

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices/  
**Scraped:** 2026-03-05T09:33:44.349480Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
YARA-L 2.0 rule structure and best practices
Supported in:
Google secops
SIEM
This document describes Google Security Operations's recommended best practices for writing rules in YARA-L 2.0.
Filter out zero values
Fields might be automatically omitted in the events you run your rules against. When fields are omitted, they default to their zero values.
For example, an omitted string value defaults to
""
.
If you equate two fields that are both omitted, they might both default to their zero values. This might lead to unintended matches where two fields match because they both have zero values. You can avoid this behavior by explicitly specifying the zero value.
For example, if you have a rule that equates two events based on two fields, there is a chance that both of those fields are empty, causing a match:
$e1.field1 = $e2.field2
If both
e1.field1
and
e2.field2
are omitted in the data,
"" = ""
is true, causing a match.
The following comparison expressions ensure that you don't get a match because
e1.field1
and
e2.field2
don't include any data:
$e1.field1 = $e2.field2
 $e1.field != ""
Zero values and enrichment-dependent rules
If a rule depends on enriched data it hasn't been updated yet, the value might be null or zero.
Therefore, it is good practice to filter out zero values (null checks) on enrichment-dependent rules. Learn
how Google SecOps enriches event and entity data
and
how to use context-enriched data in rules
.
Add an event type filter
In the following example, the IP addresses for each UDM event are checked against
the reference list, consuming a lot of resources:
events:
// For every UDM event, check if the target.ip is listed in
// the suspicious_ip_addresses reference list.
$e.target.ip in %suspicious_ip_addresses
If your YARA-L rule only detects on UDM events of a certain event type, adding an event type filter can help to optimize your rule by reducing the number of events the rule needs to evaluate.
events:
// For every UDM event of type NETWORK_DNS, check if the target.ip is
// listed in the suspicious_ip_addresses reference list.
$e.metadata.event_type = "NETWORK_DNS"
$e.target.ip in %suspicious_ip_addresses
Add these filters to the beginning of the events section. You should also put equality filters before regular expression or other comparisons. Filters are applied in the order they appear in the rule.
For Community blogs on working with YARA-L, see:
YARA-L basics
YARA-L rule variables
YARA-L operators and modifiers
Building a single event rule using a regular expression
Aggregating events in rules
Setting a threshold in conditions
Rules editor navigation
YARA-L Rule Options
Building a Single Event Rule - String Match
Building a Multi Event Rule - Joining Events
Building a Multi Event Rule - Ordering Events
Building a Multi Event Rule - Multiple Joins and Counts in Conditions
Building a Multi Event Rule - Sliding Windows
Introducing Outcomes in a Single Event Rule
Outcomes in a Multi Event Rule - Counts
Outcomes in Multi Event Rules - Arrays
Outcomes in a Multi Event Rule - Max, Min, Sum
Outcomes - Risk Score, Conditional Logic and Mathematical Operators
Functions - strings.concat
Functions - strings.coalesce
Functions - Network
Reference List
CIDR Reference Lists
Regex Reference Lists
Strings Function - Upper or Lower Case
Regular Expression Function - re.regex
Regular Expression Function - re.capture
String Function - strings.base64_decode
Regular Expression Function - re.replace
Getting started with Statistical Search
Statistical Search - More Than a Count
Need more help?
Get answers from Community members and Google SecOps professionals.
