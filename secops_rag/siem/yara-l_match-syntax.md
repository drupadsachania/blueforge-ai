# Match section syntax

**Source:** https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax/  
**Scraped:** 2026-03-05T09:33:27.301050Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Match section syntax
Supported in:
Google secops
SIEM
In YARA-L 2.0, the
match
section provides the mechanism for multi-event correlation. It defines the logic for grouping events into a single detection by linking common attributes, such as users, IP addresses, or file hashes, within a specific
temporal boundary
.
You use the
match
section for the following use cases:
Link two or more distinct events within a rule.
Aggregate data in Search and Dashboards, such as counting failed login attempts over a specific timeframe.
Define correlation criteria
Use it to define the criteria for this correlation by specifying the following:
Grouping fields (keys)
: Variables (like
$user
or
$ip
) that must have identical values across events (defined in the
events
section) to trigger a match.
Time constraint
: The duration
window
in which grouped events must occur to satisfy the rule or aggregation. In Rules, this defines the detection window; in Search and Dashboards, this defines the aggregation or correlation window.
Compare feature requirements
The following table details the comparisons for Rules to Search and Dashboards.
Feature
Rules requirement
Search and Dashboards support
Variable types
Must use placeholders defined in
events
section.
Supports both placeholders and direct UDM fields.
Time window
Defines the detection boundary.
Defines the aggregation or correlation bucket.
Syntax
over <number><m/h/d>
(for example,
10m
,
2h
,
1d
)
over <number><m/h/d>
Limits
Min:
1m
/ Max:
48h
Min:
1m
/ Max:
48h
Supported window types
YARA-L 2.0 uses different windowing behaviors to determine how time is sliced and how events are grouped. You can group event fields and placeholders in the
match
section by a specified
time granularity
using one of the following supported windows.
Supported window type
Syntax
Description
Common use case
Hop
$key over <duration>
Overlapping time intervals (default behavior).
General correlation of multiple events.
Tumbling
$key by <duration> tumbling
Fixed-size, non-overlapping, and continuous time intervals.
Quantifying activity in blocks of up to 1 hour (for example,
$user by 30m
).
Sliding
$key over <duration> [before|after] $pivot
Time intervals anchored to a specific "pivot" event.
Strict sequencing (for example,
File Download after Login
).
Example syntax:
match:
  $user, $source_ip over 5m  // Groups events by user and IP within a 5-minute window
Hop window
A
hop window
is the default behavior for multi-event rules. It creates overlapping time intervals to make sure events happen near the boundaries of a window aren't missed.
Syntax
:
$key over <duration>
(for example,
$user over 30m
)
Use case
: Best for detection where you need to make sure that a specific scenario is caught regardless of exactly when the window interval starts or ends.
Support
: Supported for aggregation in search and dashboards (for example,
count
).
By default, YARA-L queries with a
match
section use
hop windows
to correlate multiple events over time. The time range of the query's execution is divided into a set of fixed, overlapping hop windows. While the duration of these windows is specified in the
match
section, the overlap interval and window alignment are system-defined and not user-configurable. Events are then correlated within each of these predetermined windows.
Example: Overlapping hop windows for continuous correlation
The following example shows a query that's run over the time range [1:00, 2:00], with a
match
section
$user over 30m
, where a possible set of overlapping hop windows that could be generated is [1:00, 1:30], [1:03, 1:33] and [1:06, 1:36].
rule hop_window_brute_force_example {
meta:
  description = "Detects multiple failed logins within a shifting 30-minute window."
  severity = "Medium"

events:
  $login.metadata.event_type = "USER_LOGIN"
  $login.extensions.auth.auth_status = "FAILURE"
  $login.principal.user.userid = $user

match:
  // This creates the overlapping windows (e.g., 1:00-1:30, 1:03-1:33)
  $user over 30m

condition:
  // This will trigger if 10 or more failures fall into any single 30m hop
  #login >= 10
}
Example: Multi-event correlation using a hop window
The following example represents the default for most
multi-event rules
. It captures events that occur within the same general timeframe.
rule hop_window_example {
meta:
  description = "Detect a user with a failed login followed by a success within 30m"

events:
  $e1.metadata.event_type = "USER_LOGIN"
  $e1.extensions.auth.auth_status = "FAILURE"
  $e1.principal.user.userid = $user

  $e2.metadata.event_type = "USER_LOGIN"
  $e2.extensions.auth.auth_status = "SUCCESS"
  $e2.principal.user.userid = $user

match:
  $user over 30m  // This is a hop window

condition:
  $e1 and $e2
}
Example: hop window comparison
To identify a brute-force attempt, a
10m
window groups all
USER_LOGIN
failures. The
condition
then evaluates if the count (
#e
) within that specific 10-minute bucket exceeds your threshold.
rule failed_logins
{
meta:
  author = "Security Team"
  description = "Detects multiple failed user logins within 10-minute windows."
  severity = "HIGH"

events:
  $e.metadata.event_type = "USER_LOGIN"
  $e.security_result.action = "FAIL"
  $user = $e.target.user.userid

match:
  $user over 10m

condition:
  #e >= 5
}
The
match
section finds users with a failed login in a new location over a
10-minute (
10m
) interval:
match:
  $user over 10m
Tumbling window
A
tumbling window
segments a stream of data into fixed-size, non-overlapping, and continuous time intervals. Each data event is assigned to only one window. This is in contrast to a sliding or hop window, which can have overlapping time intervals.
Syntax
: Use the
by
operator (
$key by <duration>
), for example,
$user by 30m
.
Use case
: Best for reporting and building dashboards where you want to count events in distinct blocks (for example,
"How many alerts per hour?"
).
Search and dashboards
: Frequently used to create clean bar charts without deduplicating events.
Example: Fixed-interval counting with tumbling windows
The following example shows a 30-minute tumbling window, where events that occur between 1:00:00 and 1:29:59 are processed together. Then, the next set of events, from 1:30:00 to 1:59:59, are processed separately.
rule tumbling_window_threshold_example {
meta:
  description = "Detect more than 50 failed logins from a single IP within a fixed 1-hour block."
  severity = "Medium"

events:
  $login.metadata.event_type = "USER_LOGIN"
  $login.extensions.auth.auth_status = "FAILURE"
  $login.principal.ip = $ip

match:
// This creates distinct, 1-hour blocks (e.g., 1:00-1:59, 2:00-2:59)
  $ip by 1h

condition:
  #login > 50
}
Sliding window
Use a
sliding window
when you need to search for events that occur in a strict, relative order (for example,
e1
occurs up to two minutes after
e2
). Unlike fixed windows, a sliding window is triggered by every occurrence of the designated
$pivot_event
using this syntax:
after
: The window begins at the pivot event's timestamp and extends forward.
before
: The window ends at the pivot event's timestamp and extends backward.
Specify sliding windows in the
match
section of a query as follows:
<match-var-1>, <match-var-2>, ... over <duration> [before|after] <pivot-event-var>
Syntax
:
$key over <duration> before|after $<pivot_event>
Grouping keys
: Common fields (for example,
$user
,
$ip
) used to link events together.
Duration
: Time offset from the pivot event (for example,
5m
,
1h
).
Use cases
:
Strict sequencing: Detect an attack chain where order is required (for example, a user creation followed by a privilege escalation).
Relative timing: Find an event that occurs within a specific offset of a "trigger" (for example, a
Process Start
event followed by a
Network Connection
within 30 seconds).
Absence detection: Identify when a required "cleanup" or "heartbeat" event fails to occur after a start event (for example, a
Database Backup Start
without a corresponding
End
event).
Valid sliding window examples
The following examples show valid sliding windows:
$var1, $var2 over 5m after $e1
$user over 1h before $e2
$host, $ip over 1h before $e2
Example: Forward-looking correlation with sliding windows (
after
)
The following example demonstrates how to detect a sequence of events where the second event must occur within a specific timeframe after a primary "trigger" or pivot event. This is useful for detecting rapid lateral movement or automated follow-on actions.
rule sliding_window_after_example {
meta:
  description = "Detect a network connection occurring within 1 minute after a suspicious process launch."
  severity = "High"

events:
  $proc.metadata.event_type = "PROCESS_LAUNCH"
  $proc.principal.hostname = $host

  $net.metadata.event_type = "NETWORK_HTTP"
  $net.principal.hostname = $host

match:
  // $proc is the pivot; the 1-minute window starts at the $proc timestamp
  $host over 1m after $proc

condition:
  $proc and $net
}
Example: Backward-looking correlation with sliding windows (
before
)
Use a
"before"
sliding window to investigate the activity leading up to a specific alert. This is often used in root-cause analysis to identify what happened immediately preceding a critical detection.
rule sliding_window_before_example {
meta:
  description = "Identify file modifications occurring in the 5 minutes before a ransomware alert."
  severity = "Critical"

events:
  $file.metadata.event_type = "FILE_MODIFICATION"
  $file.principal.hostname = $host

  $alert.metadata.event_type = "ANTIVIRUS_DETECTION"
  $alert.metadata.product_name = "Premium_AV"
  $alert.principal.hostname = $host

match:
  // $alert is the pivot; the 5-minute window ends at the $alert timestamp
  $host over 5m before $alert

condition:
  $file and $alert
}
Performance and best practices
Sliding windows require more processing power than standard (hop) windows because they're calculated for every occurrence of the pivot event, and can result in slower performance.
Follow these guidelines for optimal performance in rules, search, and dashboards:
Prioritize hop windows
: Use the default hop window unless the specific sequence of events (order A then order B) is required for the detection logic. Only use sliding windows when event sequencing is critical or when you're searching for missing events.
Use timestamp filters for performance
: If you only need to make sure one event happened after another, a timestamp comparison in the
events
or
condition
section is often more efficient than a sliding window, for example:
$e1.metadata.event_timestamp.seconds <
$e2.metadata.event_timestamp.seconds
Multi-event design
: Avoid using sliding windows for single-event queries. Sliding windows are designed for multi-event correlation. For single-event logic, the following guidelines apply:
Use multiple event variables and update the
condition
section.
Remove the
match
section entirely if correlation isn't required.
Optionally, consider adding timestamp filters instead of using a sliding window, for example:
$permission_change.metadata.event_timestamp.seconds < $file_creation.metadata.event_timestamp.seconds
Understand the temporal boundary
The
match
section partitions events into groups based on your grouping keys. The specified duration defines the temporal boundary for each group:
Inclusion
: Only events within the window are passed to the
condition
evaluation for that specific match.
Exclusion
: Events outside the window are ignored for that specific match group, preventing unrelated events from triggering a false positive.
Zero values in the
match
section
Google SecOps implicitly filters out zero values for all placeholders that are used in the
match
section (
""
for string,
0
for numbers,
false
for booleans, the value in position
0
for
enumerated types
).
Example: Filter out zero values
The following example illustrates queries that filter out the zero values.
rule ZeroValuePlaceholderExample {

events:
  // Because $host is used in the
match
section, the query behaves
  // as if the following predicate was added to the
events
section:
  // $host != ""
  $host = $e.principal.hostname

  // Because $otherPlaceholder was not used in the
match
,
  // there is no implicit filtering of zero values for $otherPlaceholder.
  $otherPlaceholder = $e.principal.ip

match:
  $host over 5m

condition:
  $e
}
However, if a placeholder is assigned to a function, queries don't
implicitly filter out the zero values of placeholders that are used in
the
match
section.
To disable the implicit filtering of zero values,
you can use the
allow_zero_values
option in the
options section
. The
allow_zero_values
option is only available in Rules.
Example: Allow zero values
The following example illustrates queries that don't implicitly filter out the zero values of placeholders that are used in the
match
section:
rule AllowZeroValuesExample {

events:
  // Because allow_zero_values is set to true, there is no implicit filtering
  // of zero values for $host.
  $host = $e.principal.hostname

  // Because $otherPlaceholder was not used in the match,
  // there is no implicit filtering of zero values for $otherPlaceholder.
  $otherPlaceholder = $e.principal.ip

match:
  $host over 5m

condition:
  $e

options:
  allow_zero_values = true
}
What's next
Explore the following resources to continue your YARA-L logic or dive deeper into advanced query functions:
Syntax and logic
outcome
section syntax
condition
section syntax
options
section syntax
References and examples
Expressions, operators, and constructs used in YARA-L 2.0
Functions in YARA-L 2.0
Build composite detection rules
Examples: YARA-L 2.0 queries
Need more help?
Get answers from Community members and Google SecOps professionals.
