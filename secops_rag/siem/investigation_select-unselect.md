# Control columns using select and unselect keywords

**Source:** https://docs.cloud.google.com/chronicle/docs/investigation/select-unselect/  
**Scraped:** 2026-03-05T09:32:28.724286Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Control columns using select and unselect keywords
Supported in:
Google secops
SIEM
In Search and Dashboards, you can use the
select
and
unselect
keywords to
customize the columns displayed in the
Events
table on the
Results
tab
in Search, and the tables within dashboard widgets.
The default columns are
Timestamp
and
Event
and are always displayed. The
select
and
unselect
keywords add and remove columns respectively next to the
Event
column.
select
: adds the specified columns to the
Events
table
unselect
: removes the specified columns from the
Events
table
These keywords alter how events are displayed only.
Usage examples
The examples in this section demonstrate common syntax for using the
select
and
unselect
keywords in Search queries.
For example, the following query searches for events tied to
alex-laptop
and adds
security_result.about.email
as a column to the
Events
table:
principal.hostname = "alex-laptop"
limit: 10
select: security_result.about.email
Multiple column example
The
Events
table includes
target.asset.hostname
as the first column (after the
Timestamp
and
Event
columns).
For example, you can add multiple columns:
principal.hostname = "alex-laptop"
limit: 10
select: network.sent_bytes, security_result.about.email
Outcome variable example
You can use a variable with the
select
keyword. The following example declares
$seconds
as an outcome variable equal to the
metadata.event_timestamp.seconds
Unified Data Model (UDM) field value. You can then specify it
using the
select
keyword and the
Seconds
value is displayed as one of the
columns.
principal.hostname = "alex-laptop"
outcome:
  $seconds = metadata.event_timestamp.seconds
limit: 10
select: $seconds, security_result.about.email
Aggregation and event example
The
select
and
unselect
sections are mutually exclusive and let users include or exclude outcome
variables, match variables, event fields, or entity fields.
All UDM searches are either single event searches or aggregated searches (also
known as
event statistics
). Aggregate searches specify the
match
keyword or
use aggregate functions in the output (for example,
sum
or
count
).
Single event search
This example adds a column for
metadata.event_timestamp
:
events:
  principal.hostname = "alex-laptop"
  metadata.event_type = "NETWORK_CONNECTION"
select:
  metadata.event_timestamp
Aggregated search
In this example, columns representing
$hostname
and
$count_id
are added to
the
Events
table:
events:
    $e.metadata.event_type != "RESOURCE_CREATION"
    $e.principal.hostname = $hostname
    $id = $e.network.session_id
match:
    $hostname over 1h
outcome:
    $count_hostname = count($hostname)
    $count_id = count($id)
unselect:
    $count_hostname
Need more help?
Get answers from Community members and Google SecOps professionals.
