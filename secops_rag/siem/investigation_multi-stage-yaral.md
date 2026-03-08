# Create multi-stage queries in YARA-L

**Source:** https://docs.cloud.google.com/chronicle/docs/investigation/multi-stage-yaral/  
**Scraped:** 2026-03-05T09:32:27.614289Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create multi-stage queries in YARA-L
Supported in:
Google secops
SIEM
This document describes how multi-stage queries in YARA-L let you feed the
output of one query stage directly into the input of a subsequent stage. This
process gives you greater control over data transformation than a single,
monolithic query.
Integrate multi-stage queries with existing features
Multi-stage queries work in conjunction with the following existing
features in Google Security Operations:
Composite detection rules
: Multi-stage queries complement
composite detection
rules
.
Unlike composite rules, multi-stage queries that use Search can return results 
in real-time.
Time ranges and multi-event rules:
You can use multi-stage queries to
detect anomalies by comparing different time windows within your data. For example,
you can use your initial query stages to establish a baseline over an 
extended period, and then use a later stage to evaluate recent activity against 
that baseline. You can also use
multi-event rules
to create a similar type of comparison.
Multi-stage queries in YARA-L are supported in both
Dashboards
and
Search
.
Joins help correlate data from multiple sources to provide more context for an
investigation. By linking related events, entities, and other data, you can
investigate complex attack scenarios. For more information, see
Use joins in Search
.
Define multi-stage YARA-L syntax
As you configure a multi-stage query, be aware of the following:
Limit stage
: Multi-stage queries must contain between 1 and 4 named
stages, in addition to the root stage.
Order syntax
: Always define the named stage syntax before defining the
root stage syntax.
Create a multi-stage YARA-L query
To create a multi-stage YARA-L query, complete the following steps.
Stage structure and syntax
Go to
Investigation > Search
. Follow these structural requirements when you
define your query stages:
Syntax
: Use the following syntax to name each stage and separate it from
other stages:
stage <stage name> { }
Braces
: Place all stage syntax inside curly braces {}.
Order
: Define the syntax for all named stages before defining the root
stage.
Referencing
: Each stage can reference stages defined earlier in the
query.
Root stage
: A query must have a root stage, which is processed after all
named stages.
The following example stage,
daily_stats
, collects daily network statistics:
stage daily_stats {
  metadata.event_type = "NETWORK_CONNECTION"
  $source = principal.hostname
  $target = target.ip
  $source != ""
  $target != ""
  $total_bytes = cast.as_int(network.sent_bytes + network.received_bytes)
  match:
    $source, $target by day
  outcome:
    $exchanged_bytes = sum($total_bytes)
}
Access stage Output
The output of a named stage is accessible to subsequent stages using stage
fields. Stage fields correspond with the stage's
match
and
outcome
variables and can be used similarly to Unified Data Model (UDM) fields.
Use the following syntax to access a stage field:
$<stage name>.<variable name>
Access window timestamps (optional)
If a named stage uses a hop, sliding, or tumbling window, access the window
start and window end for each output row using these reserved fields:
$<stage name>.window_start
$<stage name>.window_end
The
window_start
and
window_end
are integer fields expressed in seconds
since the Unix epoch. Windows in different stages can vary in size.
Limitations
Multi-stage queries have the following functional and structural constraints:
Structural and stage limits
Root stage
: Only one root stage is allowed per query.
Named stages
: A maximum of four named stages are supported.
Stage referencing
: A stage can only reference stages defined logically
before it in the same query.
Joins
: A maximum of four non-data-table joins are allowed across all
stages.
Outcome requirement
: Each named stage (excluding the root stage) must
include either a
match
section or an
outcome
section. The
outcome
section doesn't require aggregation.
Window and compatibility limits
Feature support
: Multi-stage queries are supported in
Search
and
Dashboards
, but not supported in
Rules
.
Window types
: Avoid mixing different window types within a single query.
Window dependency
: A stage using a hop or sliding window can't depend on
another stage that also uses a hop or sliding window.
Tumbling window size
: While tumbling windows in different stages can
vary in size, the difference in size must be less than 720x.
Example: Stage aggregation difference
The following example window configuration isn't allowed:
stage monthly_stats {
  metadata.event_type = "NETWORK_CONNECTION"
    $source = principal.hostname
    $target = target.ip
    $source != ""
    $target != ""
    $total_bytes = cast.as_int(network.sent_bytes + network.received_bytes)

  match:
    $source, $target by month

  outcome:
    $exchanged_bytes = sum($total_bytes)
}

$source = $monthly_stats.source
$target = $monthly_stats.target

match:
    $source, $target by minute
If the
monthly_stats
stage aggregates data by month, and the root stage
aggregates the output of
monthly_stats
by minute, then each row from
monthly_stats
maps to 43,200 rows in the root stage (because there are 43,200
minutes in one month).
Stage and query limitations
Each individual stage within a multi-stage query has the following constraints:
Most limitations that apply to a single-stage query also apply to each individual stage:
Output requirement
: Every stage must output at least one match or outcome variable (stage field).
Window in join
: The maximum window size (hop, tumbling, or sliding) used in a join is 2 days.
Maximum number of outcome variables
:
20 for customers not opted in to allow larger outcome variable limit
50 for customers opted in to allow larger outcome variable limit
Minimum and maximum size of a hop window
.
Maximum number of elements in an array-valued outcome variable
.
Multi-stage queries are subject to the same limitations as statistics
queries:
Statistics queries
: 120 QPH (API and UI)
Search views from Google SecOps
: 100 views per minute
Multi-stage joins are supported in the user interface and the
EventService.UDMSearch
API, but not in the
SearchService.UDMSearch
API. Multi-stage queries without joins are also supported in the user
interface.
Event and global limitations
Maximum events:
Multi-stage queries are strictly limited in the number of events they can
process simultaneously:
UDM events
: A maximum of 2 UDM events are allowed.
Entity Context Graph (ECG) events
: A maximum of one ECG event is allowed.
Global query limitations:
These limits are platform-wide constraints that control how far back and how
much data a multi-stage query can return.
For a query time range, the maximum time range for a standard query is 30 days.
The maximum total result set size is 10,000 results.
Multi-stage query examples
The examples in this section help to illustrate how you might create a complete
multi-stage YARA-L query.
Example: Search for unusually active network connections (hours)
This multi-stage YARA-L example identifies IP address pairs with
higher-than-normal network activity, targeting pairs that maintain high activity
for more than three hours. The query includes two required components: the named
stage,
hourly_stats
, and the
root
stage.
The
hourly_stats
stage searches for
principal.ip
and
target.ip
pairs with high
levels of network activity.
This stage returns a single hourly value for following fields:
Statistics for the source IP (string):
$hourly_stats.src_ip
Statistics for the destination IP (string):
$hourly_stats.dst_ip
Statistics for the count of events (integer):
$hourly_stats.count
Standard deviation received bytes (float):
$hourly_stats.std_recd_bytes
Average received bytes (float):
$hourly_stats.avg_recd_bytes
Hour bucket start time in seconds from the Unix epoch (integer):
$hourly_stats.window_start
Hour bucket end time in seconds from the Unix epoch (integer):
$hourly_stats.window_end
The root stage processes the output of the
hourly_stats
stage. It calculates
statistics for
principal.ip
and
target.ip
pairs with activity exceeding the
threshold specified by
$hourly_stats
. It then filters for pairs with more than
three hours of high activity.
stage hourly_stats {
  metadata.event_type = "NETWORK_CONNECTION"
  $src_ip = principal.ip
  $dst_ip = target.ip
  $src_ip != ""
  $dst_ip != ""

  match:
    $src_ip, $dst_ip by hour

  outcome:
    $count = count(metadata.id)
    $avg_recd_bytes = avg(network.received_bytes)
    $std_recd_bytes = stddev(network.received_bytes)

  condition:
    $avg_recd_bytes > 100 and $std_recd_bytes > 50
}

$src_ip = $hourly_stats.src_ip
$dst_ip = $hourly_stats.dst_ip
$time_bucket_count = strings.concat(timestamp.get_timestamp($hourly_stats.window_start), "|", $hourly_stats.count)

match:
 $src_ip, $dst_ip

outcome:
 $list = array_distinct($time_bucket_count)
 $count = count_distinct($hourly_stats.window_start)

condition:
 $count > 3
If you alter the match condition in the root stage as follows, you can introduce a windowed
aggregation by day for the multi-stage query.
match:
 $src_ip, $dst_ip by day
Example: Search for unusually active network connections (using Z-score)
This multi-stage query compares the daily average network activity against
today's activity using a Z-score calculation (measuring the number of standard
deviations away from the mean). This query effectively searches for unusually
high network activity between internal assets and external systems.
Prerequisite
: The query time window must be greater than or equal to 2 days
and include the current day for the calculated Z-score to be effective.
This multi-stage query includes the
daily_stats
stage and the
root
stage,
which work together to calculate the Z-score for network activity:
The
daily_stats
stage performs the initial daily aggregation. It
calculates the total bytes exchanged each day for each IP pair (
source
and
target
) and returns the following stage fields (corresponding with columns
in output rows):
$daily_stats.source
: singular, string
$daily_stats.target
: singular, string
$daily_stats.exchanged_bytes
: singular, integer
$daily_stats.window_start
: singular, integer
$daily_stats.window_end
: singular, integer
The root stage aggregates the
daily_stats
stage output for each IP pair.
It calculates the average and standard deviation of the daily bytes
exchanged across the entire search range, along with the bytes exchanged
today. It uses those three calculated values to determine the Z-score.
The output lists the Z-scores for all of today's IP pairs, sorted in descending
order.
// Calculate the total bytes exchanged per day by source and target

stage daily_stats {
  metadata.event_type = "NETWORK_CONNECTION"
  $source = principal.hostname
  $target = target.ip
  $source != ""
  $target != ""
  $total_bytes = cast.as_int(network.sent_bytes + network.received_bytes)
  match:
    $source, $target by day
  outcome:
    $exchanged_bytes = sum($total_bytes)
}

// Calculate the average per day over the time window and compare with the bytes
   exchanged today

$source = $daily_stats.source
$target = $daily_stats.target
$date = timestamp.get_date($daily_stats.window_start)

match:
  $source, $target

outcome:
  $today_bytes = sum(if($date = timestamp.get_date(timestamp.current_seconds()), $daily_stats.exchanged_bytes, 0))
  $average_bytes = window.avg($daily_stats.exchanged_bytes)
  $stddev_bytes = window.stddev($daily_stats.exchanged_bytes)
  $zscore = ($today_bytes - $average_bytes) / $stddev_bytes

order:
  $zscore desc
Export unaggregated variables from stages
Named stages can include an unaggregated
outcome
section. This means that
variables defined within that
outcome
section are output directly from the
stage, letting subsequent stages access them as stage fields without requiring a
grouped aggregation.
Example: Export unaggregated variable
This example demonstrates how to export unaggregated variables. Note the
following logic:
top_5_bytes_sent
stage searches for the five events with the highest network activity.
top_5_bytes_sent
stage outputs the following stage fields corresponding with columns in output rows:
$top_5_bytes_sent.bytes_sent
: singular, integer
$top_5_bytes_sent.timestamp_seconds
: singular, integer
The
root
stage computes the latest and earliest timestamps for the five events with the highest network activity.
stage top_5_bytes_sent {
  metadata.event_type = "NETWORK_CONNECTION"
  network.sent_bytes > 0

  outcome:
    $bytes_sent = cast.as_int(network.sent_bytes)
    $timestamp_seconds = metadata.event_timestamp.seconds

  order:
    $bytes_sent desc 
  
  limit:
    5
}

outcome:
  $latest_timestamp = timestamp.get_timestamp(max($top_5_bytes_sent.timestamp_seconds))
  $earliest_timestamp = timestamp.get_timestamp(min($top_5_bytes_sent.timestamp_seconds))
Implement windowing in multi-stage queries
Multi-stage queries support all types of windowing (hop, sliding, and tumbling)
in named stages. If a named stage includes a window, the window start and window
end for each output row is accessible using the following reserved fields:
$<stage name>.window_start
$<stage name>.window_end
Example: Hop window
The following example illustrates how you might use hop windows in a multi-stage query:
hourly_stats
stage searches for IP pairs that have high network activity within the same hour.
hourly_stats
outputs the following stage fields corresponding with columns in output rows:
$hourly_stats.src_ip
: singular, string
$hourly_stats.dst_ip
: singular, string
$hourly_stats.count
: singular, integer
$hourly_stats.std_recd_bytes
: singular, float
$hourly_stats.avg_recd_bytes
: singular, float
$hourly_stats.window_start
: singular, integer
$hourly_stats.window_end
: singular, integer
Root stage filters out IP pairs with more than 3 hours of high activity. The
hours could be overlapping due to usage of a hop window in the
hourly_stats
stage.
stage hourly_stats {
  metadata.event_type = "NETWORK_CONNECTION"
  $src_ip = principal.ip
  $dst_ip = target.ip
  $src_ip != ""
  $dst_ip != ""

  match:
    $src_ip, $dst_ip over 1h

  outcome:
    $count = count(metadata.id)
    $avg_recd_bytes = avg(network.received_bytes)
    $std_recd_bytes = stddev(network.received_bytes)

  condition:
    $avg_recd_bytes > 100 and $std_recd_bytes > 50
}

$src_ip = $hourly_stats.src_ip
$dst_ip = $hourly_stats.dst_ip
$time_bucket_count = strings.concat(timestamp.get_timestamp($hourly_stats.window_start), "|", $hourly_stats.count)

match:
 $src_ip, $dst_ip

outcome:
 $list = array_distinct($time_bucket_count)
 $count = count_distinct($hourly_stats.window_start)

condition:
 $count > 3
Joins in multi-stage queries
Inner joins are supported within and between the stages of multi-stage queries. The inner join functionality supports following types:
UDM and UDM
UDM and ECG
UDM and DataTable
In the context of joins, a windowed stage refers to a stage with a match section containing a window. In contrast, a table stage doesn't output windows.
The following example shows how to configure a matchless join between UDM events and a table stage in a multi-stage query.
median
stage calculates the median bytes sent for each source host and target IP pair
median
stage outputs the following stage fields corresponding with columns in output rows:
$median.host
: singular, string
$median.target
: singular, string
$median.median
: singular, float
absolute_deviations
stage joins each UDM event with the row from
median
for the same source host and target IP pair. For each UDM event, it calculates the absolute value of the bytes sent.
absolute_deviations
outputs the following stage fields corresponding with columns in output rows:
$absolute_deviations.host
: singular, string
$absolute_deviations.target
: singular, string
$absolute_deviations.absolute_deviation
: singular, float
Root stage calculates the mean of the absolute deviations of bytes sent across all UDM events
stage median {
  metadata.event_type = "NETWORK_CONNECTION"
  $host = principal.hostname
  $target = target.ip

  match:
    $host, $target

  outcome:
    $median = window.median(network.sent_bytes, true)
}

stage absolute_deviations {
  metadata.event_type = "NETWORK_CONNECTION"
  $join_host = principal.hostname
  $join_host = $median.host
  $join_target = target.ip[0]
  $join_target = $median.target

  outcome:
    $host = $join_host
    $target = $join_target
    $absolute_deviation = math.abs(network.sent_bytes - $median.median)
}

$host = $absolute_deviations.host
$target = $absolute_deviations.target

match:
  $host, $target

outcome:
  $mean_absolute_deviation = avg($absolute_deviations.absolute_deviation)
Example: Matchless join between windowed stage and table stage
The following example illustrates how to configure a matchless join between a windowed stage and a table stage in a multi-stage query.
hourly_stats
stage calculates the total bytes sent for each source and target host pair and hour bucket.
hourly_stats
stage outputs the following stage fields corresponding with columns in output rows:
$hourly_stats.source_host
: singular, string
$hourly_stats.dst_host
: singular, string
$hourly_stats.total_bytes_sent
: singular, float
$hourly_stats.window_start
: singular, integer
$hourly_stats.window_end
: singular, integer
agg_stats
stage calculates the average and standard deviation of bytes per hour for each source and target host pair.
agg_stats
outputs the following stage fields corresponding with columns in output rows:
$agg_stats.source_host
: singular, string
$agg_stats.dst_host
: singular, string
$agg_stats.avg_bytes_sent
: singular, float
$agg_stats.stddev_bytes_sent
: singular, float
Root stage joins each row from
hourly_stats
with the row from
agg_stats
for the same source and target host pair. For each source and target host pair, it calculates the z-score using the total bytes sent for that host pair bucket and the aggregate statistics.
stage hourly_stats {
 $source_host = principal.hostname
 $dst_host = target.hostname
 principal.hostname != ""
 target.hostname != ""
 match:
   $source_host, $dst_host by hour
 outcome:
   $total_bytes_sent = sum(cast.as_int(network.sent_bytes))
}

stage agg_stats {
  $source_host = $hourly_stats.source_host
  $dst_host = $hourly_stats.dst_host
  match:
    $source_host, $dst_host
  outcome:
   $avg_bytes_sent = avg($hourly_stats.total_bytes_sent)
   $stddev_bytes_sent = stddev($hourly_stats.total_bytes_sent)
}

$source_host = $agg_stats.source_host
$source_host = $hourly_stats.source_host

$dst_host = $agg_stats.dst_host
$dst_host = $hourly_stats.dst_host

outcome:
  $hour_bucket = timestamp.get_timestamp($hourly_stats.window_start)
  $z_score = ($hourly_stats.total_bytes_sent - $agg_stats.avg_bytes_sent)/$agg_stats.stddev_bytes_sent
Cross joins in multi-stage queries
When using Google SecOps Search or Dashboards, cross joins in multi-stage queries let you compare individual UDM event data against aggregated statistics calculated in other YARA-L stages.
In YARA-L, the
cross join
keyword works with a stage with a limit of 1. This returns only one row.
When a cross join is used between a stage with a limit of 1 and another dataset (for example, UDM events), the single row output from the stage is appended to each row of the other dataset. This enriches the event data with the overall statistics.
Example: Find unusual login activity
The following example identifies the users who log in more frequently than normal. It calculates this by comparing each user's login count (using the
user_login_counts
stage) against the average login count across all users (using the
total_users
stage). Users who login an unusual number of times can be sorted in the search results.
You then use the cross join keyword to link the results from the
total_users
stage to the results from the
user_login_counts
stage.
stage user_login_counts {
    $user = principal.user.userid
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"

    match:
        $user

    outcome:
        $login_count = count(metadata.id)
}

stage total_users {
    outcome:
        $count = count($user_login_counts.user)
    limit: 
        1
}

cross join $total_users, $user_login_counts

$login_count = $user_login_counts.login_count
$user = $user_login_counts.user
$tot_users = $total_users.count

// all users who logged in the same number of times are grouped together.
match:
    $login_count
outcome:
    $num_users = count($user)
    $frequency_percent = (count($user) / max($tot_users) ) * 100
Known issues
We recommend that you review the following limitations and recommended
workarounds when you implement multi-stage queries:
All multi-stage queries behave like
statistics Search queries
(the output
consists of aggregated statistics rather than unaggregated events or data
table rows).
The performance of joins with UDM and entity events on one side can
experience low performance due to the size of that dataset. We strongly
recommend filtering the UDM and entity events side of the join as much as
possible (for example, filter on event type).
For general guidance on recommended practices, see
Yara-L best practices
and for
information specific to joins, see
Best practices
.
Need more help?
Get answers from Community members and Google SecOps professionals.
