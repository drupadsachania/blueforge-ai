# Lists

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/  
**Scraped:** 2026-03-05T10:10:16.043251Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Lists
Supported in:
Google secops
SOAR
This document describes a set of actions to help you manage custom lists.
Search custom list
Description
Search for a specified string within the records of a custom list. If no values
  are provided, the search returns all custom list records.
Parameters
Parameter
Type
Default value
Is mandatory
Description
String to search
String
N/A
No
String to search for within the records in a custom list.
Categories
String
N/A
No
Custom list category to search within.
Example
In this example, the system checks whether
.com
is included in
any records in a custom list with the category "Blocked Domains".
Action Configurations
Parameter
Value
Entities
All entities
String to search
.com
Categories
Blocked domains
Action Results
Script Result
Script Result Name
Value Options
Example
Match_records
true
or
false
true
JSON Result
[{
"entityIdentifier": "sample.com", "category": "Blocked Domains", "forDBMigration": false, "environments": ["*"], "id": 1, "creationTimeUnixTimeInMs": 1674846992575, "modificationTimeUnixTimeInMs": 1674846992575
}]
Search for a specified string in an environment custom list
Description
Search a specified string within the records of the current case environment's
  custom list. If no values are provided, the search returns all custom lists records.
Parameters
Parameter
Type
Default value
Is mandatory
Description
String to search
String
N/A
No
String to search within the records in a custom list.
Categories
String
N/A
No
Category specification within the custom list for searching.
Example
In this example, the system checks whether
1.1.1.1
is included in any records in a custom list with the category "vuln_scanner".
Action Configurations
Parameter
Value
Entities
All entities
String to search
1.1.1.1
Categories
vuln_scanner
Action Results
Script Result
Script Result Name
Value Options
Example
Match_Records
true
or
false
true
JSON result
[
  {
    "entityIdentifier": "1.1.1.1",
    "category": "vuln_scanner",
    "environments": [
      "Default Environment"
    ],
    "id": 5,
    "name": "test",
    "creationTimeUnixTimeInMs": 1673953571935,
    "modificationTimeUnixTimeInMs": 1673953571935
  }
]
Is string in custom list
Description
Checks if a string is in a custom list.
Parameters
Parameter
Type
Default value
Is mandatory
Description
ListItem
String
N/A
Yes
String to add to a custom list.
Category
String
Allowlist
Yes
Custom list category or name.
Example
In this example, the system checks whether the IP address
0.0.0.0
exists in a list category named
bad_ips_list
.
Action Configurations
Parameter
Value
Entities
All entities
IdentifierList
0.0.0.0
Categories
bad_ips_list
Action Results
Script Result
Script Result Name
Value Options
Example
NumOf FoundResults
true
or
false
true
JSON result
{
"Entity" : "0.0.0.0",
"EntityResult" : "true"
}
Add string to custom list
Description
Adds a string to a custom list.
Parameters
Parameter
Type
Default value
Is mandatory
Description
ListItem
String
N/A
Yes
String to add to a custom list.
Category
String
Allowlist
Yes
Custom list category or name.
Example
In this example, an IP address of
0.0.0.1
is added to a custom list category
  named
bad_ips_list
.
Action Configurations
Parameter
Value
Entities
All entities
Listitem
0.0.0.1
Categories
bad_ips_list
Action Results
Script Result
Script Result Name
Value Options
Example
NumOf FoundResults
true
or
false
true
JSON result
{
"Entity" : "0.0.0.0",
"EntityResult" : "true"
}
Remove string from custom list
Description
Removes a string from a custom list.
Parameters
Parameter
Type
Default value
Is mandatory
Description
Category
String
Allowlist
Yes
Custom list category or name.
ListItem
String
N/A
Yes
String to remove from a custom list.
Example
In this example, an IP address
0.0.0.1
is removed from a custom list category
  named
bad_ips_list
.
Action Configurations
Parameter
Value
Entities
All entities
IdentifierList
0.0.0.1
Categories
bad_ips_list
Action Results
Script Result
Script Result Name
Value Options
Example
NumOfFoundResults
true
or
false
true
JSON result
{
"Entity" : "0.0.0.0",
"EntityResult" : "true"
}
Need more help?
Get answers from Community members and Google SecOps professionals.
