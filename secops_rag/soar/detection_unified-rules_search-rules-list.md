# Search the rules list

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/search-rules-list/  
**Scraped:** 2026-03-05T10:03:46.082010Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Search the rules list
Supported in:
Google secops
SIEM
The rules search feature helps you locate specific rules across your unified rule list. You can find rules using basic keyword matching or leverage an advanced, AIP-160 compliant structured search syntax for highly targeted queries. These search capabilities are fully supported both in the Rules dashboard and through the
ListRules
API.
Search methods
Keyword search
: Performs a simple, broad search directly against the rule text.
Example:
my_rule_name
Structured search
: Filters your rules based on specific metadata facets, such as the display name, text, tags, live status, and so on.
Example:
display_name="my_rule_name" text:"$e.metadata.event_type = /"USER_LOGIN/"" tags:"ta0001"
Supported operators in Search
Operator
Example
Meaning
:
string_field: "str"
repeated_field: "str"
Field value contains substring
str
One of field elements contains substring
str
=
string_field = "str"
bool_field = true
enum_field = "VAL"
timestamp_field = "2025-01-01"
Field value is exactly
str
Field value is exactly the boolean value
TRUE
Field value is exactly the enum
VAL
Field value is exactly the date
2025-01-01
!=
string_field != "str"
bool_field != true
enum_field != "VAL"
Field value is NOT
str
Field value is NOT
TRUE
Field value is NOT the enum
VAL
>
string_field > "str"
timestamp_field > "2025-01-01"
Field value is lexically ordered after
str
Field value is after
2025-01-01
>=
string_field >= "str"
timestamp_field >= "2025-01-01"
Field value is lexically ordered after or equal to
str
Field value is on or after
2025-01-01
<
string_field < "str"
timestamp_field < "2025-01-01"
Field value is lexically ordered before
str
Field value is before
2025-01-01
<=
string_field <<>= "str"
timestamp_field <<>= "2025-01-01"
Field value is lexically ordered before or equal to
str
Field value is on or before
2025-01-01
Supported fields for structured search
rule_owner
Field description
: The creator entity of the rule
Field type:
enum
Supported values
:
customer
google
* (any owner)
Supported operators
Operator
Example
Meaning
:
rule_owner: "customer"
rule_owner: "google"
rule_owner:*
Return custom rules only
Return curated rules only
Return both custom and curated rules
=
rule_owner = "customer"
rule_owner = "google"
Return custom rules only
Return curated rules only
!=
rule_owner != "customer"
rule_owner != "google"
Return rules that are not custom rules
Return rules that are not curated rules
Note
: By default, API calls without any rule_owner filters will have the
filter
rule_owner: "customer"
applied to them. The wildcard
\*
value is
useful when fetching both custom and curated rules.
create_time
Field description
: The timestamp at which the rule was created.
Field type:
timestamp
Supported operators
:
Operator
Example
Meaning
>
create_time > "2025-11-19"
Return rules created after
2025-11-19
>=
create_time >= "2025-11-19"
Return rules created on or after
2025-11-19
<
create_time < "2025-11-19"
Return rules created before
2025-11-19
<=
create_time <= "2025-11-19"
Return rules created on or before
2025-11-19
revision_create_time
Field description
: The timestamp at which the latest rule version is created.
Field type:
timestamp
Supported operators
:
Operator
Example
Meaning
>
revision_create_time > "2025-11-19"
Return rules with last text update after
2025-11-19
>=
revision_create_time >= "2025-11-19"
Return rules with last text update on or after
2025-11-19
<
revision_create_time < "2025-11-19"
Return rules with last text update before
2025-11-19
<=
revision_create_time <= "2025-11-19"
Return rules with last text update on or before
2025-11-19
name
Field description
: The resource name of the rule which contains a unique
identifier.
Field type:
string
Supported operators
:
Operator
Example
Meaning
:
Name: "ru_7a22464f-e8e7-408e-b598-6aa4c61bb73b""
Return rules with the identifier "ru_7a22464f-e8e7-408e-b598-6aa4c61bb73b" in the resource name
display_name
Field description
: The human readable name of the rules extracted from the
first line of the rule text.
Field type
:
string
Supported operators
:
Operator
Example
Meaning
:
display_name: "aws"
Return rules with substring
aws
in the display name
=
display_name = "my_rule_7"
Return rules with display name exactly
my_rule_7
!=
display_name != "my_rule_7"
Return rules that do not have display name
my_rule_7
>
display_name > "b"
Return rules with display name starting with a character that's lexically ordered after the letter
b
>=
display_name > "b"
Return rules with display name starting with the letter "b" or a character that's lexically ordered after the letter
b
<
display_name < "b"
Return rules with display name starting with a character that's lexically ordered before the letter
b
<=
display_name  <= "b"
Return rules with display name starting with the letter "b" or a character that's lexically ordered before the letter
b
text
Field description
: The rule text.
Field type:
string
Supported operators
:
Operator
Example
Meaning
:
Text: "invoke-web request"
Text: "$ip = \"0.0.0.0\""
Return rules with substring
aws
in the rule text
Return rules with the substring
$ip = "0.0.0.0"
author
Field description
: The author of the rule as indicated in the metadata
section of the rule text.
Field type
:
string
Supported operators
:
Operator
Example
Meaning
:
author: "alice"
Return rules with substring "alice" in the author value
=
author = "alice@google.com"
Return rules with author value exactly "alice@google.com"
!=
author != "alice@google.com"
Return rules that do not have author "alice@google.com"
>
author > "b"
Return rules with author starting with a character that's lexically ordered after the letter "b"
>=
author > "b"
Return rules with author starting with the letter "b" or a character that's lexically ordered after the letter "b"
<
author < "b"
Return rules with author starting with a character that's lexically ordered before the letter "b"
<=
author  <= "b"
Return rules with author starting with the letter "b" or a character that's lexically ordered before the letter "b"
severity
**Field description: **the severity of the rule as indicated in the metadata section of the rule text
Field type:
Message
Supported operators
:
Operator
Example
Meaning
:
severity: "low"
Return rules with substring "low" in the severity value
=
severity = "medium"
Return rules with severity value exactly "medium"
!=
severity != "high"
Return rules that don't have "high" severity
tags
**Field description: **tags associated with the rule
Field type:
repeated string
Supported operators
Operator
Example
Meaning
:
Tag: "ta0001"
Return rules with at least 1 MITRE tag containing the substring "ta0001" in the tag name.
archived
**Field description: **whether the rule has been archived
Field type:
boolean
Supported operators
Operator
Example
Meaning
=
archived = true
Return rules that are marked archived
!=
archived != true
Return rules that are not marked archived
live_mode_enabled
**Field description: **whether the rule is running as a live rule
Field type:
boolean
Supported operators
Operator
Example
Meaning
=
live_mode_enabled = true
Return rules that are running as live rules
!=
live_mode_enabled != true
Return rules that are not running as live rules
alerting_enabled
**Field description: **whether new detections for the rule should be marked as alerting detections
Field type:
boolean
Supported operators
Operator
Example
Meaning
=
alerting_enabled = true
Return rules that are marked alerting
!=
alerting_enabled != true
Return rules that are not marked alerting
run_frequency
**Field description: **when the rule is enabled as a live rule, this refers to the frequency of live executions.
Field type:
enum
Supported values
Live
Hourly
Daily
Supported operators
Operator
Example
Meaning
=
run_frequency = hourly
Return rules that with hourly run_frequency
!=
run_frequency != hourly
Return rules with run_frequency other than hourly
execution_state
**Field description: **whether live rule executions are running as expected, throttled, or barred from executing.
Field type:
enum
Supported values
Default
Limited
Paused
Supported operators
Operator
Example
Meaning
=
execution_state = limited
execution_state = default
Return live rules that are currently throttled
Return live rules that are running as expected
!=
execution_state = limited
Return live rules that are not currently in a throttled state
Need more help?
Get answers from Community members and Google SecOps professionals.
