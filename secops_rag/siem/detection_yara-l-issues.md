# YARA-L 2.0 known issues and limitations

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/yara-l-issues/  
**Scraped:** 2026-03-05T09:33:45.320657Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
YARA-L 2.0 known issues and limitations
This document describes the known issues and limitations in YARA-L 2.0.
Outcome aggregations with repeated field unnesting
When a rule references a repeated field in an event variable with multiple elements, each element is split into a separate event row.
For example, the two IP addresses in the repeated field
target.ip
on event
$e
are split into two instances of
$e
, each with a different
target.ip
value.
rule outbound_ip_per_app {
  meta:
  events:
    $e.principal.application = $app
  match:
    $app over 10m
  outcome:
    $outbound_ip_count = count($e.target.ip) // yields 2.
  condition:
    $e
}
Event record before repeated field unnesting
The following table shows the event record before unnesting the repeated field:
metadata.id
principal.application
target.ip
aaaaaaaaa
Google SecOps
[192.0.2.20
,
192.0.2.28]
Event records after unnesting the repeated field
The following table shows the event record after unnesting the repeated field:
metadata.id
principal.application
target.ip
aaaaaaaaa
Google SecOps
192.0.2.20
aaaaaaaaa
Google SecOps
192.0.2.28
When a rule references a repeated field nested within another, like
security_results.action
, unnesting occurs at both the parent and child levels. The resulting instances from unnesting a single event form a Cartesian product of the elements in the parent and child fields.
In the following example rule, event
$e
with two repeated values on
security_results
and two repeated
values on
security_results.actions
are unnested into four instances.
rule security_action_per_app {
  meta:
  events:
    $e.principal.application = $app
  match:
    $app over 10m
  outcome:
    $security_action_count = count($e.security_results.actions) // yields 4.
  condition:
    $e
}
Event record before repeated field unnesting
The following table shows the event record before unnesting the repeated field:
metadata.id
principal.application
security_results
aaaaaaaaa
Google SecOps
[ { actions: [ ALLOW, FAIL ] }
,
{ actions: [ CHALLENGE, BLOCK ] } ]
Event records after repeated field unnesting
The following table shows the event record after unnesting the repeated field:
metadata.id
principal.application
security_results.actions
aaaaaaaaa
Google SecOps
ALLOW
aaaaaaaaa
Google SecOps
FAIL
aaaaaaaaa
Google SecOps
CHALLENGE
aaaaaaaaa
Google SecOps
BLOCK
This unnesting behavior in rule evaluation can produce unexpected
outcome aggregations when the rule references one or more repeated fields
with a parent field that is also a repeated field. Non-distinct aggregations
like
sum()
,
array()
, and
count()
cannot account for duplicate values on
other fields on the same event produced by the unnesting behavior. In the following example
rule, event
$e
has a single hostname
google.com
, but the outcome
hostnames
aggregates over unnested four instances of the same event
$e
, each with a duplicate
principal.hostname
value. This outcome yields four hostnames instead of one
due to the unnesting of repeated values on
security_results.actions
.
rule security_action_per_app {
  meta:
  events:
    $e.principal.application = $app
  match:
    $app over 10m
  outcome:
    $hostnames = array($e.principal.hostname) // yields 4.
    $security_action_count = count($e.security_results.action) // yields 4.
  condition:
    $e
}
Event record before repeated field unnesting
The following table shows the event record before unnesting the repeated field:
metadata.id
principal.application
principal.hostname
security_results
aaaaaaaaa
Google SecOps
google.com
[ { action: [ ALLOW, FAIL ] }
,
{ action: [ CHALLENGE, BLOCK ] } ]
Event record after repeated field unnesting
The following table shows the event record after unnesting the repeated field:
metadata.id
principal.application
principal.hostname
security_results.action
aaaaaaaaa
Google SecOps
google.com
ALLOW
aaaaaaaaa
Google SecOps
google.com
FAIL
aaaaaaaaa
Google SecOps
google.com
CHALLENGE
aaaaaaaaa
Google SecOps
google.com
BLOCK
Workaround
Aggregations that ignore duplicate values or eliminate duplicate values are not
affected by this unnesting behavior. Use the distinct version of an
aggregation if you're encountering unexpected outcome values due to unnesting.
The following aggregations are not affected by the unnesting behavior described previously.
max()
min()
array_distinct()
count_distinct()
Outcome aggregations with multiple event variables
If a rule contains multiple event variables, there is a separate item in the
aggregation for each combination of events that is included in the detection.
For example, if the following example rule is run against the listed events:
events:
  $e1.field = $e2.field
  $e2.somefield = $ph

match:
  $ph over 1h

outcome:
   $some_outcome = sum(if($e1.otherfield = "value", 1, 0))

condition:
  $e1 and $e2
event1:
  // UDM event 1
  field="a"
  somefield="d"

event2:
  // UDM event 2
  field="b"
  somefield="d"

event3:
  // UDM event 3
  field="c"
  somefield="d"
The sum is calculated over every combination of events, enabling you to use both
event variables in the outcome value calculations. The following elements are
used in the calculation:
1: $e1 = event1, $e2 = event2
2: $e1 = event1, $e2 = event3
3: $e1 = event2, $e2 = event1
4: $e1 = event2, $e2 = event3
5: $e1 = event3, $e2 = event1
5: $e1 = event3, $e2 = event2
This results in a potential maximum sum of 6, even though $e2 can only
correspond to 3 distinct events.
This affects sum, count, and array. For count and array, using
count_distinct
or
array_distinct
can solve the issue, but there is no workaround
for sum.
Parentheses at the start of an expression
Using parentheses at the start of an expression triggers the following error:
parsing: error with token: ")"
invalid operator in events predicate
The following example would generate this type of error:
($event.metadata.ingested_timestamp.seconds -
$event.metadata.event_timestamp.seconds) / 3600 > 1
The following syntax variations return the same result, but with valid syntax:
$event.metadata.ingested_timestamp.seconds / 3600 -
$event.metadata.event_timestamp.seconds / 3600 > 1
    1 / 3600 * ($event.metadata.ingested_timestamp.seconds -
$event.metadata.event_timestamp.seconds) > 1
    1 < ($event.metadata.ingested_timestamp.seconds -
$event.metadata.event_timestamp.seconds) / 3600
Index array in outcome requires aggregation for single values on repeated field
Array indexing in the outcome section still requires aggregation. For example,
the following does not work:
outcome:
  $principal_user_dept = $suspicious.principal.user.department[0]
However, you can save the output of the array index in a placeholder variable
and use that variable in the outcome section as shown here:
events:
  $principal_user_dept = $suspicious.principal.user.department[0]

outcome:
  $principal_user_department = $principal_user_dept
OR condition with non-existence
If an OR condition is applied between two separate event variables and if the
rule matches on non-existence, the rule successfully compiles, but can produce
false positive detections. For example, the following rule syntax can match
events having
$event_a.field = "something"
even though it shouldn't.
events:
     not ($event_a.field = "something" **or** $event_b.field = "something")
condition:
     $event_a and #event_b >= 0
The workaround is to separate the conditions into two blocks where each block
only applies the filter to a single variable as shown here:
events:
     not ($event_a.field = "something")
     not ($event_b.field = "something")
condition:
     $event_a and #event_b >= 0
Arithmetic with unsigned event fields
If you try to use an integer constant in an arithmetic operation with a UDM
field whose type is an unsigned integer, you will get an error. For example:
events:
  $total_bytes = $e.network.received_bytes * 2
The field
udm.network.received_bytes
is an unsigned integer. This happens due
to integer constants defaulting to signed integers, which don't work with
unsigned integers in arithmetic operations.
The workaround is to force the integer constant to a float which will then work
with the unsigned integer. For example:
events:
  $total_bytes = $e.network.received_bytes * (2/1)
Eventual consistency and false positives in GeoIP enrichment
The system prioritizes speed over immediate accuracy in the initial enrichment stages (Streaming and Latency-Sensitive), which can lead to missing data and potential false positives. The system will continue to enrich the data in the background, but the data may not be available when the rule is run. This is part of the normal
eventual consistency
process.
To avoid these types of false positives, don't rely on enriched fields to exist in events for triggering detections.
For example, consider this rule event:
$e.principal.ip_geo_artifact.network.asn = "16509" AND
$e.principal.ip_geo_artifact.location.country_or_region = "United Kingdom"
The rule relies on the fact that the event must have
$e.principal.ip_geo_artifact.network.asn = "16509"
AND
$e.principal.ip_geo_artifact.location.country_or_region = "United Kingdom"
which are both enriched fields. If the enrichment is not completed in time, the rule will produce a false positive.
To avoid this, a better check for this rule would be:
$e.principal.ip_geo_artifact.network.asn != "" AND
$e.principal.ip_geo_artifact.network.asn = "16509" AND
$e.principal.ip_geo_artifact.location.country_or_region != "" AND
$e.principal.ip_geo_artifact.location.country_or_region = "United Kingdom"
This rule eliminates the possibility of the event being triggered by IPs with the
ASN 16509
but located outside the UK. This improves the overall precision of the rule.
Need more help?
Get answers from Community members and Google SecOps professionals.
