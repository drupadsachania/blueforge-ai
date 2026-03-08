# Use metrics functions for Risk Analytics rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/metrics-functions/  
**Scraped:** 2026-03-05T09:31:51.167542Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use metrics functions for Risk Analytics rules
Use metrics functions for Risk Analytics rules
Supported in:
Google secops
SIEM
This document describes the major elements of YARA-L 2.0 syntax features, specifically designed for risk analytics. It provides a detailed overview of how to use specialized metric functions to aggregate large amounts of historical data, enabling more sophisticated detection and risk scoring. For more information about YARA-L, see
YARA-L 2.0 overview
.
Google Security Operations supports a number of metric functions, which can aggregate
large amounts of historical data. All rules that use the metric function are automatically categorized as
multi-event rules
, even if they don't have a
match
section and use only one event variable. This means that they count against multi-event rule quota.
Metric function parameters
You can use the metric functions for rules that perform entity behavioral
analytics.
Example: Calculate maximum daily outbound bytes per IP
The following example demonstrates a rule that calculates the maximum number of daily bytes sent by a specific IP address over the past month. In this instance, the IP address is represented by the placeholder variable (
$ip
). Learn more about
placeholder variables
.
$max_bytes_per_day = max(metrics.network_bytes_outbound(
    period:1d, window:30d,
    metric:value_sum,
    agg:max,
    principal.asset.ip:$ip
))
Due to the large number of arguments used in these functions, the example uses named
parameters, which can be specified in any order. The parameters are as follows:
Period
The length of time over which individual log events are combined into a single
observation. The only values allowed are
1h
and
1d
.
Window
The length of time over which individual observations are aggregated into a
single value, such as the average and the maximum. The allowed values for
window
are based on the period of the metric. The valid mapping is as follows:
period:1h
:
window:today
period:1d
:
window:30d
Example: Identify peak daily failed authentications for a specific user
Example: Identifying peak daily failed authentications for a specific user
The following example demonstrates a rule that identifies the greatest number of failed authentication attempts (
max(metrics.auth_attempts_fail
) recorded for a specific user (
alice
) within a single day (
1d
), calculated over a 30-day (
30d
) lookback period:
$user = "alice"
$max_fail = max(metrics.auth_attempts_fail(
    period:1d, window:30d,
        metric:event_count_sum,
        agg:max,
        target.user.userid:$user
))
Example: Detect first-seen user logins using hourly and daily metrics
The following example demonstrates how to combine hourly and daily metric functions to identify "first-seen" behaviors. This rule determines if a user is logging into a specific application for the first time by checking both the current day's hourly increments and a broader 30-day historical window.
events:
    $e.metadata.event_type = "USER_LOGIN"
    $e.security_result.action = "ALLOW"
    $userid = $e.target.user.userid
    $app = $e.target.application
match:
    // find events from now - 4h ago, which is the recommended look-back period
    $userid, $app over 4h
outcome:
    // check hourly analytics until daily analytics are available
    $first_seen_today = max(metrics.auth_attempts_success(
        period:1h, window:today, metric:first_seen, agg:max,
        target.user.userid:$userid, target.application:$app))
    $first_seen_monthly = max(metrics.auth_attempts_success(
        period:1d, window:30d, metric:first_seen, agg:max,
        target.user.userid:$userid, target.application:$app))
condition:
    $e and ($first_seen_today = 0) and ($first_seen_monthly = 0)
Metric
Within each period, each observation has a number of metrics associated with it.
One of these must be selected for aggregation over the entire window. Five
metric
types are supported:
event_count_sum
: Number of unique log events within each period.
first_seen
: First seen timestamp of a matching log event within each
period.
last_seen
: Last seen timestamp of a matching log event within each
period.
value_sum
: Represents the sum of the number of bytes in all the log
events combined within the period. You can only use this value for a metric
function with
bytes
in its name.
num_unique_filter_values
: Metric that is not pre-computed by
Google SecOps but can be computed during rule execution. For details, see
Count unique metrics
.
Agg
Which aggregation is applied to the metric. Aggregations are applied over the
entire window (e.g. the highest daily value over the past 30 days). The allowed
values are:
avg
—Average value per period. This is a statistical mean, which does not
include values of zero.
max
—Greatest value per period.
min
—Smallest value per period.
num_metric_periods
—Number of periods within the time window that had a
non-zero metric value.
stddev
—Standard deviation of the value per period. This is a statistical
standard deviation which does not include zero values.
sum
—Sum of each value per period, over the entire window.
For example, the following rule tells you the average number of failed
authentication attempts seen for a specific user (Alice) in any given day over
the last 30 days:
$user = "alice"
$avg_fail = max(metrics.auth_attempts_fail(
        period:1d, window:30d,
        metric:event_count_sum,
        agg:avg,
        target.user.userid:$user
))
The following rule tells you how many successful authentications a specific user
had over the last 30 days:
$total_success = max(metrics.auth_attempts_success(
        period:1d, window:30d,
        metric:event_count_sum,
        agg:sum,
        target.user.userid:$user
))
The following rule tells you whether a specific user successfully logged in at
least once over the last 30 days:
$days_success = max(metrics.auth_attempts_success(
        period:1d, window:30d,
        metric:event_count_sum,
        agg:num_metric_periods,
        target.user.userid:$user
))
The following rule tells you the first or last time a specific user logged in
successfully:
$first_seen = max(metrics.auth_attempts_success(
        period:1d, window:30d,
        metric:first_seen,
        agg:min,
        target.user.userid:$user
))
$last_seen = max(metrics.auth_attempts_success(
        period:1d, window:30d,
        metric:last_seen,
        agg:max,
        target.user.userid:$user
))
The following rule tells you the maximum number of bytes sent by a user in any
given day over the last 30 days:
$max_daily_bytes = max(metrics.network_bytes_outbound(
        period:1d, window:30d,
        metric:value_sum,
        agg:max,
        target.user.userid:$user
))
Filter
Filters allow filtering a metric before aggregation by a value in the
pre-computed metric (see values in
Metric
). Filters can be any valid
events expression (a single line in the event section) which does not contain
any event fields or placeholders. The only variables that can be included in
this condition are metric types.
The following rule includes only metrics where
value_sum > 10 AND
event_count_sum > 2
:
$max_bytes_per_day = max(metrics.network_bytes_outbound(
    period:1d, window:30d,
    metric:value_sum,
    agg:max,
    principal.asset.ip:$ip
    filter:value_sum > 10 AND event_count_sum > 2
))
Valid examples of filters
filter:value_sum > 10 AND event_count_sum != 5
filter:event_count_sum = 100 OR event_count_sum > 1000
filter:timestamp.get_day_of_week(first_seen) = 3
Invalid examples of filters
// No placeholders in filter expressions.
filter:value_sum > $ph

// No event fields in filter expressions.
filter:event_count_sum + $e.field > 10

// No event fields in filter expressions.
filter:timestamp.subtract(first_seen, $e.metadata.timestamp)
UDM fields
A metric is filtered by 1, 2, or 3 UDM fields, depending on the function. For
more information, see
Functions
.
The following types of UDM fields are used for metric functions:
Dimensions—(Required) Different combinations are listed in this
documentation. You cannot join a metric with a default value (
""
for
string and
0
for int).
Namespaces—(Optional) You can only use namespaces for entities that
you specify in dimensions. For example, if you use
principal.asset.hostname
filter
, you can use a
principal.namespace filter
as well. If you don't
include a namespace filter, the data across all namespaces is aggregated
together. You can use a default value as a namespace filter.
Window calculations
Google Security Operations calculates metrics using either a daily or hourly metric
window.
Daily windows
All daily windows, such as
30d
, are determined the same way.
Google Security Operations uses the latest available metrics data that has been
generated that does not overlap with the rule time range. Calculation of the
daily metrics can take up to 6 hours to complete and doesn't start until the end
of the day in UTC. Metric data for the day before will be available at or
before 6:00 UTC each day.
For example, for a rule that is running over event data from 2023-10-31 4:00 UTC
to 2023-10-31 7:00 UTC, the daily metrics for 2023-10-31 will likely have been
generated, so the metric calculation will use the data from 2023-10-01 to
2023-10-30 (inclusive). Whereas for a rule that is running over event data from
2023-10-31 1:00 UTC to 2023-10-31 3:00 UTC, the daily metrics for 2023-10-30
will likely not have been generated, so the metric calculation will use the data
from 2023-09-30 to 2023-10-29 (inclusive).
Hourly
today
window
The hourly metric window is calculated differently from the window for
daily metrics. The hourly metric window of
today
is not a static size like the
30d
window for daily metrics. The hourly metric window
today
fills in as
much data as possible between the end of the daily window and the start of the
rule time window.
For example, for a rule that is running over event data from 2023-10-31 4:00:00
UTC to 2023-10-31 7:00:00 UTC, the daily metric calculation will use the data
from 2023-10-01 to 2023-10-30 (inclusive) and the hourly metric window will use
data from 2023-10-31 00:00:00 UTC to 2023-10-31 4:00:00 UTC.
Count unique metrics
There is a special type of metric
num_unique_filter_values
that is not
pre-computed by Google SecOps
and is instead computed during a rule execution. This is done by aggregating
over an existing dimension in a pre-computed metric. For example, the metric
daily total count of distinct countries that a user attempted to authenticate
in can be derived from the pre-computed
auth_attempts_total
metric on the
dimensions
target.user.userid
and
principal.ip_geo_artifact.location.country_or_region
by performing a count
unique aggregation over the latter dimension.
The following example rule counts unique metrics:
$outcome_variable = max(metrics.auth_attempts_total(
    period: 1d,
    window: 30d,
    // This metric type indicates any filter with a wildcard value should be
    // aggregated over each day to produce a new metric on-the-fly.
    metric: num_unique_filter_values,
    agg: max,
    target.user.userid: $userid,
    // Filter whose value should be counted over each day to produce the
    // num_unique_filter_values metric.
    principal.ip_geo_artifact.location.country_or_region: *
))
Functions
This section includes documentation on the specific metrics functions supported
by Google Security Operations.
Alert Events
metrics.alert_event_name_count
precomputes historical values for UDM events
that have had alerts generated by Carbon Black, CrowdStrike Falcon, Microsoft
Graph API Alerts, or Microsoft Sentinel.
The full list of UDM fields available as filters
principal.asset.asset_id, principal.process.file.full_path, principal.user.email_addresses, security_result.rule_name
principal.asset.asset_id, principal.process.file.full_path, principal.user.employee_id, security_result.rule_name
principal.asset.asset_id, principal.process.file.full_path, principal.user.product_object_id, security_result.rule_name
principal.asset.asset_id, principal.process.file.full_path, principal.user.userid, security_result.rule_name
principal.asset.asset_id, principal.process.file.full_path, principal.user.windows_sid, security_result.rule_name
principal.asset.asset_id, principal.process.file.full_path, security_result.rule_name
principal.asset.asset_id, principal.process.file.sha256, principal.user.email_addresses, security_result.rule_name
principal.asset.asset_id, principal.process.file.sha256, principal.user.employee_id, security_result.rule_name
principal.asset.asset_id, principal.process.file.sha256, principal.user.product_object_id, security_result.rule_name
principal.asset.asset_id, principal.process.file.sha256, principal.user.userid, security_result.rule_name
principal.asset.asset_id, principal.process.file.sha256, principal.user.windows_sid, security_result.rule_name
principal.asset.asset_id, security_result.rule_name
principal.asset.hostname, principal.process.file.full_path, principal.user.email_addresses, security_result.rule_name
principal.asset.hostname, principal.process.file.full_path, principal.user.employee_id, security_result.rule_name
principal.asset.hostname, principal.process.file.full_path, principal.user.product_object_id, security_result.rule_name
principal.asset.hostname, principal.process.file.full_path, principal.user.userid, security_result.rule_name
principal.asset.hostname, principal.process.file.full_path, principal.user.windows_sid, security_result.rule_name
principal.asset.hostname, principal.process.file.full_path, security_result.rule_name
principal.asset.hostname, principal.process.file.sha256, principal.user.email_addresses, security_result.rule_name
principal.asset.hostname, principal.process.file.sha256, principal.user.employee_id, security_result.rule_name
principal.asset.hostname, principal.process.file.sha256, principal.user.product_object_id, security_result.rule_name
principal.asset.hostname, principal.process.file.sha256, principal.user.userid, security_result.rule_name
principal.asset.hostname, principal.process.file.sha256, principal.user.windows_sid, security_result.rule_name
principal.asset.hostname, security_result.rule_name
principal.asset.ip, principal.process.file.full_path, principal.user.email_addresses, security_result.rule_name
principal.asset.ip, principal.process.file.full_path, principal.user.employee_id, security_result.rule_name
principal.asset.ip, principal.process.file.full_path, principal.user.product_object_id, security_result.rule_name
principal.asset.ip, principal.process.file.full_path, principal.user.userid, security_result.rule_name
principal.asset.ip, principal.process.file.full_path, principal.user.windows_sid, security_result.rule_name
principal.asset.ip, principal.process.file.full_path, security_result.rule_name
principal.asset.ip, principal.process.file.sha256, principal.user.email_addresses, security_result.rule_name
principal.asset.ip, principal.process.file.sha256, principal.user.employee_id, security_result.rule_name
principal.asset.ip, principal.process.file.sha256, principal.user.product_object_id, security_result.rule_name
principal.asset.ip, principal.process.file.sha256, principal.user.userid, security_result.rule_name
principal.asset.ip, principal.process.file.sha256, principal.user.windows_sid, security_result.rule_name
principal.asset.ip, security_result.rule_name
principal.asset.mac, principal.process.file.full_path, principal.user.email_addresses, security_result.rule_name
principal.asset.mac, principal.process.file.full_path, principal.user.employee_id, security_result.rule_name
principal.asset.mac, principal.process.file.full_path, principal.user.product_object_id, security_result.rule_name
principal.asset.mac, principal.process.file.full_path, principal.user.userid, security_result.rule_name
principal.asset.mac, principal.process.file.full_path, principal.user.windows_sid, security_result.rule_name
principal.asset.mac, principal.process.file.full_path, security_result.rule_name
principal.asset.mac, principal.process.file.sha256, principal.user.email_addresses, security_result.rule_name
principal.asset.mac, principal.process.file.sha256, principal.user.employee_id, security_result.rule_name
principal.asset.mac, principal.process.file.sha256, principal.user.product_object_id, security_result.rule_name
principal.asset.mac, principal.process.file.sha256, principal.user.userid, security_result.rule_name
principal.asset.mac, principal.process.file.sha256, principal.user.windows_sid, security_result.rule_name
principal.asset.mac, security_result.rule_name
principal.asset.product_object_id, principal.process.file.full_path, principal.user.email_addresses, security_result.rule_name
principal.asset.product_object_id, principal.process.file.full_path, principal.user.employee_id, security_result.rule_name
principal.asset.product_object_id, principal.process.file.full_path, principal.user.product_object_id, security_result.rule_name
principal.asset.product_object_id, principal.process.file.full_path, principal.user.userid, security_result.rule_name
principal.asset.product_object_id, principal.process.file.full_path, principal.user.windows_sid, security_result.rule_name
principal.asset.product_object_id, principal.process.file.full_path, security_result.rule_name
principal.asset.product_object_id, principal.process.file.sha256, principal.user.email_addresses, security_result.rule_name
principal.asset.product_object_id, principal.process.file.sha256, principal.user.employee_id, security_result.rule_name
principal.asset.product_object_id, principal.process.file.sha256, principal.user.product_object_id, security_result.rule_name
principal.asset.product_object_id, principal.process.file.sha256, principal.user.userid, security_result.rule_name
principal.asset.product_object_id, principal.process.file.sha256, principal.user.windows_sid, security_result.rule_name
principal.asset.product_object_id, security_result.rule_name
Authentication Attempts
metrics.auth_attempts_total
precomputes historical values for UDM events with
a
USER_LOGIN
event
type
.
metrics.auth_attempts_success
further requires that the event had at least one
SecurityResult.Action
of
ALLOW
.
metrics.auth_attempts_fail
requires instead that none of the
SecurityResult.Actions
were
ALLOW
.
The full list of UDM fields available as filters
principal.asset.asset_id
principal.asset.asset_id
,
target.asset.asset_id
principal.asset.asset_id
,
target.asset.hostname
principal.asset.asset_id
,
target.asset.ip
principal.asset.asset_id
,
target.asset.mac
principal.asset.asset_id
,
target.asset.product_object_id
principal.asset.hostname
principal.asset.hostname
,
target.asset.asset_id
principal.asset.hostname
,
target.asset.hostname
principal.asset.hostname
,
target.asset.ip
principal.asset.hostname
,
target.asset.mac
principal.asset.hostname
,
target.asset.product_object_id
principal.asset.ip
principal.asset.ip
,
target.asset.asset_id
principal.asset.ip
,
target.asset.hostname
principal.asset.ip
,
target.asset.ip
principal.asset.ip
,
target.asset.mac
principal.asset.ip
,
target.asset.product_object_id
principal.asset.mac
principal.asset.mac
,
target.asset.asset_id
principal.asset.mac
,
target.asset.hostname
principal.asset.mac
,
target.asset.ip
principal.asset.mac
,
target.asset.mac
principal.asset.mac
,
target.asset.product_object_id
principal.asset.product_object_id
principal.asset.product_object_id
,
target.asset.asset_id
principal.asset.product_object_id
,
target.asset.hostname
principal.asset.product_object_id
,
target.asset.ip
principal.asset.product_object_id
,
target.asset.mac
principal.asset.product_object_id
,
target.asset.product_object_id
principal.user.email_addresses
principal.user.email_addresses
,
target.asset.asset_id
principal.user.email_addresses
,
target.asset.hostname
principal.user.email_addresses
,
target.asset.ip
principal.user.email_addresses
,
target.asset.mac
principal.user.email_addresses
,
target.asset.product_object_id
principal.user.employee_id
principal.user.employee_id
,
target.asset.asset_id
principal.user.employee_id
,
target.asset.hostname
principal.user.employee_id
,
target.asset.ip
principal.user.employee_id
,
target.asset.mac
principal.user.employee_id
,
target.asset.product_object_id
principal.user.product_object_id
principal.user.product_object_id
,
target.asset.asset_id
principal.user.product_object_id
,
target.asset.hostname
principal.user.product_object_id
,
target.asset.ip
principal.user.product_object_id
,
target.asset.mac
principal.user.product_object_id
,
target.asset.product_object_id
principal.user.userid
principal.user.userid
,
target.asset.asset_id
principal.user.userid
,
target.asset.hostname
principal.user.userid
,
target.asset.ip
principal.user.userid
,
target.asset.mac
principal.user.userid
,
target.asset.product_object_id
principal.user.windows_sid
principal.user.windows_sid
,
target.asset.asset_id
principal.user.windows_sid
,
target.asset.hostname
principal.user.windows_sid
,
target.asset.ip
principal.user.windows_sid
,
target.asset.mac
principal.user.windows_sid
,
target.asset.product_object_id
target.application
target.user.email_addresses
target.user.email_addresses
,
network.tls.client.certificate.sha256
target.user.email_addresses
,
principal.ip_geo_artifact.location.country_or_region
target.user.email_addresses
,
principal.ip_geo_artifact.network.organization_name
target.user.email_addresses
,
target.application
target.user.employee_id
target.user.employee_id
,
network.tls.client.certificate.sha256
target.user.employee_id
,
principal.ip_geo_artifact.location.country_or_region
target.user.employee_id
,
principal.ip_geo_artifact.network.organization_name
target.user.employee_id
,
target.application
target.user.product_object_id
target.user.product_object_id
,
network.tls.client.certificate.sha256
target.user.product_object_id
,
principal.ip_geo_artifact.location.country_or_region
target.user.product_object_id
,
principal.ip_geo_artifact.network.organization_name
target.user.product_object_id
,
target.application
target.user.userid
target.user.userid
,
network.tls.client.certificate.sha256
target.user.userid
,
principal.ip_geo_artifact.location.country_or_region
target.user.userid
,
principal.ip_geo_artifact.network.organization_name
target.user.userid
,
target.application
target.user.windows_sid
target.user.windows_sid
,
network.tls.client.certificate.sha256
target.user.windows_sid
,
principal.ip_geo_artifact.location.country_or_region
target.user.windows_sid
,
principal.ip_geo_artifact.network.organization_name
target.user.windows_sid
,
target.application
metrics.auth_attempts_total
has additional UDM fields available as filters
target.application
,
target.asset.asset_id
target.application
,
target.asset.hostname
target.application
,
target.asset.ip
target.application
,
target.asset.mac
target.application
,
target.asset.product_object_id
metrics.auth_attempts_success
has additional UDM fields available as filters
network.http.user_agent
principal.asset.asset_id
,
metadata.event_type
principal.asset.hostname
,
metadata.event_type
principal.asset.ip
,
metadata.event_type
principal.asset.mac
,
metadata.event_type
principal.asset.product_object_id
,
metadata.event_type
DNS Bytes Outbound
metrics.dns_bytes_outbound
precomputes historical values for UDM events where
network
.sent_bytes
is greater than 0,
and the target port is
53/udp
,
53/tcp
, or
3000/tcp
.
network
.sent_bytes
is
available as
value_sum
.
The full list of UDM fields available as filters
principal.asset.asset_id
principal.asset.asset_id
,
target.ip
principal.asset.hostname
principal.asset.hostname
,
target.ip
principal.asset.ip
principal.asset.ip
,
target.ip
principal.asset.mac
principal.asset.mac
,
target.ip
principal.asset.product_object_id
principal.asset.product_object_id
,
target.ip
principal.user.email_addresses
principal.user.email_addresses
,
target.ip
principal.user.employee_id
principal.user.employee_id
,
target.ip
principal.user.product_object_id
principal.user.product_object_id
,
target.ip
principal.user.userid
principal.user.userid
,
target.ip
principal.user.windows_sid
principal.user.windows_sid
,
target.ip
target.ip
DNS Queries
metrics.dns_queries_total
precomputes historical values for UDM events that
have a value in
network
.
dns.id
.
metrics.dns_queries_success
further requires that the
network
.
dns.response_code
was
0
(
NoError
).
metrics.dns_queries_fail
only considers events with a
network
.
dns.response_code
greater than
0
.
The full list of UDM fields available as filters
principal.asset.asset_id
principal.asset.asset_id
,
network.dns_domain
principal.asset.asset_id
,
network.dns.questions.type
principal.asset.hostname
principal.asset.hostname
,
network.dns_domain
principal.asset.hostname
,
network.dns.questions.type
principal.asset.ip
principal.asset.ip
,
network.dns_domain
principal.asset.ip
,
network.dns.questions.type
principal.asset.mac
principal.asset.mac
,
network.dns_domain
principal.asset.mac
,
network.dns.questions.type
principal.asset.product_object_id
principal.asset.product_object_id
,
network.dns_domain
principal.asset.product_object_id
,
network.dns.questions.type
principal.user.email_addresses
principal.user.email_addresses
,
network.dns_domain
principal.user.email_addresses
,
network.dns.questions.type
principal.user.employee_id
principal.user.employee_id
,
network.dns_domain
principal.user.employee_id
,
network.dns.questions.type
principal.user.product_object_id
principal.user.product_object_id
,
network.dns_domain
principal.user.product_object_id
,
network.dns.questions.type
principal.user.userid
principal.user.userid
,
network.dns_domain
principal.user.userid
,
network.dns.questions.type
principal.user.windows_sid
principal.user.windows_sid
,
network.dns_domain
principal.user.windows_sid
,
network.dns.questions.type
File Executions
metrics.file_executions_total
precomputes historical values for UDM events
with a
PROCESS_LAUNCH
event
type
.
metrics.file_executions_success
further requires that the event had at least
one
SecurityResult.Action
of
ALLOW
.
metrics.file_executions_fail
instead requires that none of the
SecurityResult.Actions
were
ALLOW
.
The full list of UDM fields available as filters
metadata.event_type
,
principal.process.file.sha256
metadata.event_type
,
principal.asset.asset_id
,
principal.process.file.sha256
metadata.event_type
,
principal.asset.hostname
,
principal.process.file.sha256
metadata.event_type
,
principal.asset.ip
,
principal.process.file.sha256
metadata.event_type
,
principal.asset.mac
,
principal.process.file.sha256
metadata.event_type
,
principal.asset.product_object_id
,
principal.process.file.sha256
metadata.event_type
,
principal.user.email_addresses
,
principal.process.file.sha256
metadata.event_type
,
principal.user.employee_id
,
principal.process.file.sha256
metadata.event_type
,
principal.user.product_object_id
,
principal.process.file.sha256
metadata.event_type
,
principal.user.userid
,
principal.process.file.sha256
metadata.event_type
,
principal.user.windows_sid
,
principal.process.file.sha256
HTTP Queries
metrics.http_queries_total
precomputes historical values for UDM events that
have a value in
network
.
http.method
.
metrics.http_queries_success
further requires that
network
.
http.response_code
is less than 400.
metrics.http_queries_fail
only considers events with a
network
.
http.response_code
is greater than or equal to 400.
The full list of UDM fields available as filters
principal.asset.asset_id
principal.asset.asset_id
,
network.http.user_agent
principal.asset.hostname
principal.asset.hostname
,
network.http.user_agent
principal.asset.ip
principal.asset.ip
,
network.http.user_agent
principal.asset.mac
principal.asset.mac
,
network.http.user_agent
principal.asset.product_object_id
principal.asset.product_object_id
,
network.http.user_agent
principal.user.email_addresses
principal.user.email_addresses
,
network.http.user_agent
principal.user.employee_id
principal.user.employee_id
,
network.http.user_agent
principal.user.product_object_id
principal.user.product_object_id
,
network.http.user_agent
principal.user.userid
principal.user.userid
,
network.http.user_agent
principal.user.windows_sid
principal.user.windows_sid
,
network.http.user_agent
Network Bytes
metrics.network_bytes_inbound
precomputes historical values for UDM events
that have a non-zero value for
network
.
received_bytes
,
and makes that field available as
value_sum
.
metrics.network_bytes_outbound
requires a non-zero value for
network
.
sent_bytes
, and
makes that field available as
value_sum
.
metrics.network_bytes_total
considers events that have a non-zero value for
either
network
.received_bytes
or
network
.sent_bytes
(or
both), and make the sum of those two fields available as
value_sum
.
The full list of UDM fields available as filters
principal.asset.asset_id
principal.asset.asset_id
,
principal.ip_geo_artifact.location.country_or_region
principal.asset.asset_id
,
security_result.category
principal.asset.asset_id
,
target.ip_geo_artifact.network.organization_name
principal.asset.hostname
principal.asset.hostname
,
principal.ip_geo_artifact.location.country_or_region
principal.asset.hostname
,
security_result.category
principal.asset.hostname
,
target.ip_geo_artifact.network.organization_name
principal.asset.ip
principal.asset.ip
,
principal.ip_geo_artifact.location.country_or_region
principal.asset.ip
,
security_result.category
principal.asset.ip
,
target.ip_geo_artifact.network.organization_name
principal.asset.mac
principal.asset.mac
,
principal.ip_geo_artifact.location.country_or_region
principal.asset.mac
,
security_result.category
principal.asset.mac
,
target.ip_geo_artifact.network.organization_name
principal.asset.product_object_id
principal.asset.product_object_id
,
principal.ip_geo_artifact.location.country_or_region
principal.asset.product_object_id
,
security_result.category
principal.asset.product_object_id
,
target.ip_geo_artifact.network.organization_name
principal.user.email_addresses
principal.user.email_addresses
,
principal.ip_geo_artifact.location.country_or_region
principal.user.email_addresses
,
security_result.category
principal.user.email_addresses
,
target.ip_geo_artifact.network.organization_name
principal.user.employee_id
principal.user.employee_id
,
principal.ip_geo_artifact.location.country_or_region
principal.user.employee_id
,
security_result.category
principal.user.employee_id
,
target.ip_geo_artifact.network.organization_name
principal.user.product_object_id
principal.user.product_object_id
,
principal.ip_geo_artifact.location.country_or_region
principal.user.product_object_id
,
security_result.category
principal.user.product_object_id
,
target.ip_geo_artifact.network.organization_name
principal.user.userid
principal.user.userid
,
principal.ip_geo_artifact.location.country_or_region
principal.user.userid
,
security_result.category
principal.user.userid
,
target.ip_geo_artifact.network.organization_name
principal.user.windows_sid
principal.user.windows_sid
,
principal.ip_geo_artifact.location.country_or_region
principal.user.windows_sid
,
security_result.category
principal.user.windows_sid
,
target.ip_geo_artifact.network.organization_name
Resource Creation
metrics.resource_creation_total
precomputes historical values for UDM events
with a
RESOURCE_CREATION
event
type
or a
USER_RESOURCE_CREATION
event
type
.
For a list of equivalent event types, see
Metadata Event Types
metrics.resource_creation_success
further requires that the event have at
least one
SecurityResult.Action
of
ALLOW
.
The full list of UDM fields available as filters
principal.user.email_addresses
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
target.user.email_addresses
,
metadata.vendor_name
,
metadata.product_name
target.user.employee_id
,
metadata.vendor_name
,
metadata.product_name
target.user.product_object_id
,
metadata.vendor_name
,
metadata.product_name
target.user.userid
,
metadata.vendor_name
,
metadata.product_name
target.user.windows_sid
,
metadata.vendor_name
,
metadata.product_name
Resource Deletion
metrics.resource_deletion_success
precomputes historical values for UDM events
with a
RESOURCE_DELETION
event
type
and further
requires that the event have at least one
SecurityResult.Actions
of
ALLOW
.
The full list of UDM fields available as filters
principal.user.email_addresses
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
target.user.email_addresses
,
metadata.vendor_name
,
metadata.product_name
target.user.employee_id
,
metadata.vendor_name
,
metadata.product_name
target.user.product_object_id
,
metadata.vendor_name
,
metadata.product_name
target.user.userid
,
metadata.vendor_name
,
metadata.product_name
target.user.windows_sid
,
metadata.vendor_name
,
metadata.product_name
Resource Read
metrics.resource_read_success
precomputes historical values for UDM events
with a
RESOURCE_READ
event
type
and further
requires that the event have at least one
SecurityResult.Action
of
ALLOW
.
metrics.resource_read_fail
instead requires that none of the
SecurityResult.Actions
are
ALLOW
.
The full list of UDM fields available as filters
principal.user.email_addresses
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
principal.ip
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.application
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.application
,
target.location.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.resource.name
,
metadata.vendor_name
,
metadata.product_name
principal.user.email_addresses
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.employee_id
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.product_object_id
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.userid
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
principal.user.windows_sid
,
target.resource.name
,
target.resource_type
,
metadata.vendor_name
,
metadata.product_name
target.user.email_addresses
,
metadata.vendor_name
,
metadata.product_name
target.user.employee_id
,
metadata.vendor_name
,
metadata.product_name
target.user.product_object_id
,
metadata.vendor_name
,
metadata.product_name
target.user.userid
,
metadata.vendor_name
,
metadata.product_name
target.user.windows_sid
,
metadata.vendor_name
,
metadata.product_name
Limitations with metrics
When creating YARA-L rules with metrics, be aware of the following limitations:
You cannot join a metric with a default value (
""
for string and
0
for
int).
Default values:
If there is no metric data that corresponds to an event, the returned
value from the metric function is 0.
If there is an event in the detection which has no metric data, using
min
to aggregate over the function might return 0.
To check whether there is data for an event, you can use the metric
num_metric_periods
aggregation on that same event with the same filters.
Metric functions can only be used in the outcome section.
Since metric functions are only used in the outcome section, they must be
aggregated just like any other value in rules with a match section.
Need more help?
Get answers from Community members and Google SecOps professionals.
