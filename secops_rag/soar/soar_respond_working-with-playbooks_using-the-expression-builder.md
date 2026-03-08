# Use the Expression Builder

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder/  
**Scraped:** 2026-03-05T10:08:02.439601Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the Expression Builder
Supported in:
Google secops
SOAR
The Expression Builder lets you parse and modify JSON results, for use in
  subsequent actions. The Expression Builder generates various dynamic
  transformation functions that you can chain together, preview, and test,
  providing an interactive experience for transforming and parsing raw action results.
After selecting a placeholder for the parameter in the playbook action, you
  can use the JSON results. These results give you comprehensive information
  returned by the action, which you can use in subsequent playbook actions and
  flow. For details, see
Use Cases for Expression Builder
.
View the Expression Builder
This example demonstrates potential data and doesn't reflect real-time results. The actual data may differ and might contain more or fewer fields. If an analyst knows of additional fields that will be returned at runtime, they can enter the corresponding key path in the
syntax
field.
Functions
The following pipe functions are supported:
First (x)
: Returns the first X elements of an array.
Example:
alerts | First(2)
(If
alerts
is
[{"id": "A"}, {"id": "B"}, {"id": "C"}]
, returns
[{"id": "A"}, {"id": "B"}]
)
Last (x)
: Returns the last X elements of an array.
Example:
alerts | Last(1)
(If
alerts
is
[{"id": "A"}, {"id": "B"}, {"id": "C"}]
, returns
[{"id": "C"}]
)
Min (KeyPath)
: Returns the item with the minimum value from an array. If a keyPath parameter is provided, it returns the object with the minimum value at the specified path.
Example:
alerts | Min("score")
(If
alerts
contains list of objects with a
score
field, returns the object with the lowest score)
Max (KeyPath)
: Returns the item with the maximum value from an array. If a keyPath parameter is provided, it returns the object with the maximum value at the specified path.
Example:
alerts | Max("score")
(If
alerts
contains list of objects with a
score
field, returns the object with the highest score)
Filter (ConditionKey, Operator, Value)
: Filters an array of objects, returning only the objects that match a condition on a specified field.
ConditionKey
: The field in each object to evaluate against the condition.
Operator
: Operator to use for the condition.
For string input:
=
,
!=
,
in
,
not in
.
For number/date input:
=
,
!=
,
>
,
>=
,
<
,
<=
.
Value
: Value to check in condition.
Example:
alerts | Filter("severity", "=", "HIGH")
(Returns all alerts where the
severity
field is "HIGH")
DateFormat ("pattern")
- Format a date in a given pattern (pattern is specified as parameter) to the following format:
YYYY-MM-DDThh:mm:ssZ
.
Example:
timestamp_field | DateFormat("yyyy/MM/ddTHH:mm:ss")
(If
timestamp_field
is "2024/07/20T10:00:00Z", returns "2024-07-20 10:00:00")
Count ()
: Returns the number of items in the input array.
Example:
alerts | Count()
(If
alerts
is an array with 4 elements, returns 4)
OrderBy ("keyPath", "direction")
: Orders an array of objects based on the values of a specified key path.
Example:
alerts | OrderBy("score", "DESC")
(Orders the
alerts
array by
score
in descending order)
toLower ()
: Convert an input to lowercase characters.
Example:
status_field | toLower()
(If
status_field
is "OPEN", returns "open")
toUpper ()
: Convert an input to uppercase characters.
Example:
severity_field | toUpper()
(If
severity_field
is "high", returns "HIGH")
Replace ("x", "y")
: Replaces a substring within a string with another string.
Example:
message_field | Replace("World", "Universe")
(If
message_field
is "Hello World", returns "Hello Universe")
Distinct ()
: Removes duplicate values from an array. For arrays of objects, performs a deep comparison to identify duplicated objects.
Example:
[10, 20, 30, 20, 40] | Distinct()
(Returns
[10, 20, 30, 40]
)
getByIndex ("index")
: Get items of an array by a specified index or a list of indexes.
Example:
alerts | getByIndex("0")
(Returns the first element of the
alerts
array)
Example:
alerts | getByIndex("0,2")
(Returns the first and third elements of the
alerts
array)
split ("delimiter")
: Divides a string into an array of substrings, using a specified delimiter.
Example:
"tag1,tag2,tag3" | split(",")
(Returns
["tag1", "tag2", "tag3"]
)
join ("delimiter")
: Concatenates an array of strings into a single string, using a specified delimiter.
Example:
["malware", "critical"] | join(" & ")
(Returns "malware & critical")
trim ()
: Removes leading and trailing whitespaces from a string.
Example:
"  hello world  " | trim()
(Returns "hello world")
trimChars ("characters")
: Removes specified characters from the beginning and end of a string. Leading and trailing whitespaces are always removed, even if not explicitly specified.
Example:
"--TEST--ABC--" | trimChars("-")
(Returns "TEST--ABC")
substring (start, end)
: Extracts a substring from a string, using a specified start index and an optional end index.
Example:
"Hello World" | substring(0, 5)
(Returns "Hello")
Example:
"Hello World" | substring(6)
(Returns "World")
incrementValue (value)
: Increases a numeric value by a specified amount. If no amount is specified, the value is incremented by 1.
Example:
score_field | incrementValue(5)
(If
score_field
is 90, returns 95)
Example:
counter_field | incrementValue()
(If
counter_field
is 10, returns 11)
setIfEmpty ("defaultValue")
: Returns the provided default value if the input value is empty.
Example:
optional_field | setIfEmpty("N/A")
(If
optional_field
is empty, returns "N/A"; otherwise, returns the value of
optional_field
)
toUnixtime ()
: Converts a human-readable date and time string (e.g. "2014/03/12T13:37:27Z" or "2014-03-12T13:37:27+01:00") to a Unix timestamp, expressed in UTC.
Example:
"2024-07-20T10:00:00Z" | toUnixtime()
(Returns 1721469600)
ifThenElse ("operator", "comparedValue", "trueResult", "falseResult")
- Evaluates a condition and returns the first expression if true, otherwise returns the second expression.
Example:
severity_field | ifThenElse("=", "HIGH", "High Priority", "Normal Priority")
(If
severity_field
is "HIGH", returns "High Priority"; otherwise, returns "Normal Priority")
Example:
score_field | ifThenElse(">", "70", "Above Threshold", "Below Threshold")
(If
score_field
is 90, returns "Above Threshold"; if
score_field
is 60, returns "Below Threshold")
Expression:
The Expression field is where you insert the JSON results together with the
  functions and pipes to add several functions together and build the
  expression.
Run / Results:
After filling in the Expression Builder, click
Run
to display the Results 
based on the JSON Sample Data displayed in the Expression Builder.
Need more help?
Get answers from Community members and Google SecOps professionals.
