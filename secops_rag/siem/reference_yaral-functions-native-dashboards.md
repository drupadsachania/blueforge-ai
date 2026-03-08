# YARA-L 2.0 functions for dashboards

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/yaral-functions-native-dashboards/  
**Scraped:** 2026-03-05T09:37:45.890661Z

---

Home
Documentation
Security
Google Security Operations
Stay organized with collections
Save and categorize content based on your preferences.
YARA-L 2.0 functions for dashboards
Supported in:
Google secops
SIEM
This document explains how to use the following functions in queries to create
charts, alongside the YARA-L 2.0 functions supported by Google Security Operations
in the Detection Engine.
In addition to the YARA-L 2.0 functions that Google SecOps supports in
the Detection Engine, you can use the following functions in queries to build charts.
math.log
Returns the natural log value of an integer or float expression as follows:
math.log(numericExpression)
Parameter ype:
NUMBER
Return type:
NUMBER
Example
math.log($e1.network.sent_bytes) > 20
math.round
Returns the value of a float expression rounded to the specified number of decimal places.
math.round(numericExpression,decimalPlaces)
Parameter type:
NUMBER
Return type:
NUMBER
Example
math.round(10.7) // returns 11
math.round(1.2567, 2) // returns 1.25
math.round(-10.7) // returns -11
math.round(-1.2) // returns -1
math.round(4) // returns 4, math.round(integer) returns the integer
group
Groups fields of the same type into a placeholder.
group(field1, field2, field3…)
Parameter type:
Event type
Return type:
Grouped event fields
Example
In the following example, the
group()
function gathers all the IP addresses
found in the
principal.ip
,
target.ip
, and
src.ip
fields across all events
that triggered the detection. The IP addresses are then added to the placeholder
variable
$ip
. The rule then matches the IP address and returns a count of
distinct events for each unique IP address.
$ip = group(detection.collection_elements.references.event.principal.ip, detection.collection_elements.references.event.target.ip, detection.collection_elements.references.event.src.ip)
$ip != ""

match:
  $ip

outcome:
  $count = count_distinct(detection.id)

order:
  $count desc

// Detection1: principal.ip = 1.1.1.1
// Detection2: src.ip = 1.1.1.1, target.ip = 2.2.2.2
// Detection3: target.ip = 1.1.1.1
// Detection4: principal.ip = 2.2.2.2
Result:
$ip
$count
1.1.1.1
3
2.2.2.2
2
Aggregate functions
When events contain multiple values, you must use
aggregate functions
to summarize the data.
In addition to the existing aggregate functions, you can also use these aggregate functions:
avg()
: outputs the average over all possible values. Only works with
integer
and
float
.
stddev()
: calculates the standard deviation for all available values in the dataset. Only works with
integer
and
float
.
avg
Returns the average of values within a numeric column. It ignores NULL values
during the calculation. It's commonly used with
match
to calculate averages
within specific data groups.
avg(numericExpression)
Parameter type:
NUMBER
Return type:
NUMBER
Example
Find all the events where
target.ip
is not empty. For all the events that match
principal.ip
, store the average of
metadata.event_timestamp.seconds
in a variable called
avg_seconds
.
target.ip != ""
  match:
    principal.ip
  outcome:
    $avg_seconds = avg(metadata.event_timestamp.seconds)
stddev
Returns the standard deviation over all the possible values.
stddev(numericExpression)
Parameter type:
NUMBER
Return type:
NUMBER
Example
Finds all events where
target.ip
is not empty. For all events that match
principal.ip
, store the standard deviation of
metadata.event_timestamp.seconds
in a variable called
stddev_seconds
.
target.ip != ""
  match:
    principal.ip
  outcome:
    $stddev_seconds = stddev(metadata.event_timestamp.seconds)
IoC fields
Fields
Description
ioc_value
IOC indicator; can be either domain name or IP address
ioc_type
IOC type; can be either
IOC_TYPE_DOMAIN
or
IOC_TYPE_IP
feed_log_type
IOC feed log type; for example,
ET_PRO_IOC
is_global
Determines whether this a global IOC indicator
day_bucket_seconds
Specific day bucket when an IOC hit occurred, based on the event's timestamp
category
Category or type for this indicator
confidence_score
Raw confidence level from the IOC source
feed_name
Original feed from which the IOC indicator originated
severity
Raw severity level of the indicator
ioc_ingest_time
Time when the IOC was first ingested into the system
asset
Asset indicator
location
Physical location
Rule sets fields
Fields
Description
ruleset
Display name
ruleset_family
Family name
precise_alerting
Alerting status of precise rules within a specific rule set
precise_live
Status of precise rules
broad_alerting
Alerting status of broad rules within the rule set
broad_live
Status of live broad rules
detection_timestamp
Specific timestamp when a detection event was triggered
Rule fields
Fields
Description
name
Unique rule identifier (
ruleID
).
display_name
Name of the rule.
rule_text
Rule's logic or conditions in text form.
alerting
Indicates whether rule detections trigger alerts (
true
/
false
)
live_status
Current operational state of the rule, such as
ENABLED
,
DISABLED
.
author
Creator of the rule.
severity
Severity level assigned to the rule.
metadata
Additional details about the rule, such as description, author, severity,
mitre_attack_tactic
,
mitre_attack_technique
,
mitre_attack_url
,
mitre_attack_version
and other relevant fields.
total_detection_count
Number of times this rule has generated a detection.
create_time
Rule creation timestamp. The timestamp is in the
google.protobuf.Timestamp
format.
update_time
Latest rule update timestamp. The timestamp is in the
google.protobuf.Timestamp
format.
latest_detection_time
Timestamp of the most recent rule detection. The timestamp is in the
google.protobuf.Timestamp
format.
earliest_detection_time
Timestamp of the first rule detection. The timestamp is in the
google.protobuf.Timestamp
format.
archived
Indicates whether the rule is archived (
true
/
false
).
Need more help?
Get answers from Community members and Google SecOps professionals.
