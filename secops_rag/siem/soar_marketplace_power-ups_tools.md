# Tools

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/tools/  
**Scraped:** 2026-03-05T09:37:08.561465Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Tools
Supported in:
Google secops
SOAR
A set of utility actions for data manipulation to power up playbook capabilities.
Actions
The following lists the types of actions you can perform with the Tools power-up.
DNS Lookup
Description
Performs a DNS lookup using a specified DNS resolver.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
DNS Server
IP Address
N/A
Yes
Single or comma separated DNS servers.
Example
This example shows Google's public DNS address of
8.8.8.8
to search for external domain entities.
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
True/False
True
JSON Result
{
"Entity": "WWW.EXAMPLE.ORG",
 "EntityResult": [{"Type": "A", "Response": "176.9.157.114", "DNS Server": "8.8.8.8"}]
}
Add or update alert additional data
Description
Adds or updates fields in the alert additional data. Results display in the
Alerts
overview,
OFFENSE_ID
field.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Json Fields
JSON
N/A
Yes
Enter free text (for one variable) or a string that represents
        a JSON dictionary (can be nested).
Example
This example adds MITRE attack details to the alerts to display in the
Alerts overview
.
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
# of items in dictionary
2
JSON Result
{
"dict": {"mitre": " T1059"}, "list": []
}
Attach playbook to all case alerts
Description
Attaches a specific playbook or block to all alerts in a case.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Playbook Name
String
N/A
Yes
Playbook or block name to add to all alerts in a case.
Example
This example attaches a playbook called
Phishing playbookM
to all case alerts.
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
true
or
false
true
Attach a playbook to an alert
Description
Attaches a specific playbook or block to the current alert.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Playbook Name
String
N/A
Yes
Playbook or block name to add to all case alerts.
Example
This example attaches a block called
Containment Block
to the current case alerts.
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
true
or
false
true
Buffer
Description
Convert a JSON input to a JSON object.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
ResultValue
String
N/A
No
Placeholder value that returns as the
ScriptResult
value.
JSON
JSON
N/A
No
JSON displayed in the expression builder.
Example
This example displays the JSON input value in the JSON expression builder to use for further actions.
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
ResultValue
parameter input value
success
JSON Result
{
"domain" : "company.com",
"domain2" : "company2.com"
}
Get certificate details
Description
Retrieves certificate details of a given URL.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Url to check
URL
expired.badssk.com
Yes
Specify the URL to retrieve certificate details from.
Example
In this scenario, we're retrieving certificate details from
  expired.badssl.com site.
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON result
{
"hostname": "expired.badssl.com",
 "ip": "104.154.89.105", 
"commonName": "*.badssl.com",
 "is_self_signed": false, 
"SAN": [["*.badssl.com", "badssl.com"]], 
"is_expired": true, 
"issuer": "EXAMPLE CA", 
"not_valid_before": "04/09/2015", 
"not_valid_after": "04/12/2015", 
"days_to_expiration": -2762
}
Get Context Value
Description
Retrieves a value of a context key in a case or an alert.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Scope
Drop-down
Alert
Yes
Specify the scope of the key values whether it's in a case, alert
        or global.
Key
String
N/A
Yes
Specify the key.
Example
In this scenario, we're retrieving a context value from a key called
  impact in a case. This action is used along with the
Set Context
  Value
action that adds the key value pairs to the case or alert.
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Context value
High
Get Email templates
Description
Returns all email templates in the system.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Template Type
Drop-down
Standard
Yes
Specify the template type to return whether
Standard
or
HTML
.
Example
In this scenario, we're returning all HTML based email templates.
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
JSON Result containing HTML code
JSON Result shown in. next section
JSON Result
{
"templates": [{"type": 1, "name": "test 1", "content": "<html>\n    <head>\n    <style type=\"text/css\"> .title\n\n    { color: blue; text-decoration: bold; text-size: 1em; }\n    .author\n    { color: gray; }\n\n    </style>\n    </head>\n\n    <body>\n    <span class=\"title\">La super bonne</span>\n    {Text}\n    [Case.Id]\n    </h1> <br/>\n    </body>\n\n    </html>", "creatorUserName": "f00942-fa040-4422324-b2c43e-de40fdsff122b9c4", "forMigration": false, "environments": ["Default"], "id": 3, "creationTimeUnixTimeInMs": 1672054127271, "modificationTimeUnixTimeInMs": 1672054127279}]
}
Create Entities With Separator
Description
Creates entities and adds them to the alert.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Entities Identifiers
String
N/A
Yes
Specify the entity or entities to be added to the alert.
Entity Type
String
N/A
Yes
Specify the entity type.
Is Internal
Checkbox
Unselected
No
Check if the entity supplied is part of an internal network.
Entities Separator
String
,
Yes
Specify the delimiter used in the entities identifiers field.
Enrichment JSON
Drop-down
JSON
No
Specify enrichment data in JSON format.
PrefixForEnrichment
String
N/A
No
Specify the prefix to add to the enrichment data.
Example
In this scenario, we're creating three IP entities and enriching
      them with a field called “is_suspicious”.
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"created": ["0.0.0.0", "0.0.0.1", "0.0.0.2"], 
"enriched": ["0.0.0.0", "0.0.0.1", "0.0.0.2"],
"failed": []
}
Update Case Description
Description
Updates the description of a case.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Case Description
String
N/A
Yes
Specify the updated description.
Example
This example updates the case description to
      “This case is related to suspicious logins.“.
Action Results
Script Result
Script result name
Value options
Example
ScriptResult
True/False
True
Normalize entity enrichment
Description
Receives a list of keys from the entity and replaces them.
Parameters
Parameter
Type
Default value
Is Mandatory
Description
Normalization data
JSON
N/A
Yes
Specify the JSON in the following format example: [ {
            "entity_field_name": "AT_fields_Name",
            "new_name": "InternalEnrichment_Name" }, {
            "entity_field_name": "AT_fields_Direct-Manager",
            "new_name":
            "InternalEnrichment_DirectManager_Name" }, {
            "entity_field_name":
            "AT_Manager_fields_Work-Email", "new_name":
            "InternalEnrichment_DirectManager_Email" } ]
Example
In this scenario, we're replacing the entity key of
is_bad
to
malicious
.
Action results
Script result
Script result name
Value options
Example
ScriptResult
Number of enriched entities
5
Append to context value
Description
Appends a value to an existing context property or creates a new context
      property if it doesn't exist and adds the value.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Key
String
N/A
Yes
Specify the context property key
Value
String
N/A
Yes
Specify the value to append to the context property
Delimiter
String
N/A
Yes
Specify the delimiter used in the value field.
Example
In this scenario, we’re adding values “T1595” and
      “T1140” to an existing context key of “MITRE”.
Action results
Script result
Script result name
Value options
Example
ScriptResult
Context values
T1595, T1140
Create entity relationships
Description
Creates a relationship between the supplied entities and the linked
      entities. If the supplied entities don't exist, it creates them.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Entity Identifier(s)
String
N/A
Yes
Creates new or use existing entity identifiers or comma-separated
            list of identifiers.
Entity Identifier(s) Type
Drop-down
User Name
Yes
Specify the entity type.
Connect As
Drop-down
Source
Yes
Connects entity identifiers using source, destination, or linked
            relationships to the target entity identifiers.
Target Entity Type
Drop-down
Address
Yes
Specify the target entity type to connect the entity identifier(s)
            to.
Target Entity Identifier(s)
String
N/A
No
Entities in this comma separated list, of
The type from Target Entity Type will be linked to the entities
              in the Entities Identifier(s) parameter.
Enrichment JSON
JSON
N/A
No
An optional JSON object containing key /
Value pairs of attributes that can be added to the newly created
              entities.
Separator Character
String
N/A
No
Specify the character by which to separate the list of entities in Entity
            Identifiers and/or Target Entity Identifiers. Defaults to comma.
Example
In this scenario, we're creating a relationship between a user and a
      URL. In this case, Bola001 has accessed a URL of example.com.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"Entity": "Bola001", "EntityResult": {}
}
Extract URL domain
Description
Enriches all entities with a new field
siemplifytools_extracted_domain
containing the extracted
      domain out of the entity identifier. If the entity has no domain (file
      hash for example) it won't return anything. In addition to
      entities, the user can specify a list of URLs as a parameter and process
      them without enriching.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Separator
String
,
Yes
Specify the separator string to use to separate URLs.
URLs
String
N/A
No
Specify one or more URLs to extract the domain from.
Extract subdomain
Checkbox
N/A
No
Specify if you want to extract the subdomain as well.
Example
In this scenario, we're extracting the domain from the specified URL.
Action results
Script result
Script result name
Value options
Example
ScriptResult
Number of extracted domains
1
JSON result
{
"Entity": "https://sample.google.com", "EntityResult": {"domain": "sample.google.com", "source_entity_type": "DestinationURL"}
}
Check List Subset
Description
Checks if values in one list exist in another list.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Original
String
N/A
Yes
Specify the list of items to check against. Json list or comma
            separated.
Subset
List
N/A
Yes
Specify the subset list. Json list or comma separated.
Example
In this scenario, we're checking if values 1,2,3 exist in the
      original list of 1,2,3,4,5 resulting in a true result value.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
Add alert scoring information
Description
Adds an entry to the alert scoring database. Alert score is based on the
      ratio: 5 Low = 1 Medium. 3 Medium = 1 High. 2 High = 1 Critical. Optional
      tag added to case.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Name
String
N/A
Yes
Name of the check performed on the alert.
Description
String
N/A
Yes
Description of the check performed on the alert.
Severity
String
Informational
Yes
Severity.
Category
String
N/A
Yes
Category of the check performed.
Source
String
N/A
No
Part of the alert the score was derived from. Example:
            Files, user, Email.
Case Tag
String
N/A
No
Tags to add to the case.
Example
This example sets the alert score to "high" due to a suspicious result from VirusTotal.
Action Results
Script Result
Script Result Name
Value Options
Example
Alert_score
Informational, Low, Medium, High, Critical
High
JSON Result
{
"category": "File Enrichment",
 "score_data": [{"score_name": "File Enrichment", "description": "VT has found a file to be suspicious", "severity": "High", "score": 3, "source": "VirusTotal"}],
 "category_score": 3
}
Get Siemplify Users
Description
Returns list of all users configured in the system.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Hide Disabled Users
Checkbox
Selected
No
Specify whether to hide disabled users from the results.
Example
In this scenario, we're returning all users in the system including
      disabled users.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"siemplifyUsers": [{"permissionGroup": "Admins", "socRole": "@Administrator", "isDisabled": false, "loginIdentifier": "sample@domain.com", "firstName": "John", "lastName": "Doe", "permissionType": 0, "role": 0, "socRoleId": 1, "email": "sample@domain.com", "userName": "0b3423496fc2-0834302-42f33d-8523408-18c087d2347cf1e", "imageBase64": null, "userType": 1, "identityProvider": -1, "providerName": "Internal", "advancedReportsAccess": 0, "accountState": 2, "lastLoginTime": 1679831126656, "previousLoginTime": 1678950002044, "lastPasswordChangeTime": 0, "lastPasswordChangeNotificationTime": 0, "loginWrongPasswordCount": 0, "isDeleted": false, "deletionTimeUnixTimeInMs": 0, "environments": ["*"], "id": 245, "creationTimeUnixTimeInMs": 1675457504856, "modificationTimeUnixTimeInMs": 1674957504856
}
Check Entities Fields In Text
Description
Search for a specific field from each entity in scope (or multiple fields
      using regex) and compare it with one or more values. The compared values
      can also go through regular expression. A match is found if one of the post regular expression
      values from the entity enrichment is in one or more values searched in.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
SearchInData
JSON
[ { "Data": "[Event.from]", "RegEx":
            "(?<=@)[^.]+(?=\\.)" } ]
Yes
JSON that represents the string(s) you want to search in using this
            format: [ { "Data": "", "RegEx":
            "" } ]
FieldsInput
JSON
[ { "RegexForFieldName": "",
            "FieldName": "body",
            "RegexForFieldValue": "" }, {
            "RegexForFieldName": ".*(_url_).*",
            "FieldName": "", "RegexForFieldValue":
            "" }, { "RegexForFieldName": "",
            "FieldName": "body",
            "RegexForFieldValue": "HostName: (.*?)" } ]
Yes
A JSON that describes what fields should be tested for [
            "RegexForFieldName": “”,
"FieldName": "Field name to search",
"RegexForFieldValue": “”}]
ShouldEnrichEntity
String
domain_matched
No
If set to <VAL> will also put an enrichment value on the
            entity to be recognized as "matched” with the value.
The key will be <VAL>
IsCaseSensitive
Checkbox
Unselected
No
Specify if the field is case sensitive.
Example
In this scenario, we're checking if an entity with a field name of
malicious
is in the text specified.
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of findings
0
JSON Result
{
"Entity": "EXL88765-AD", "EntityResult": [{"RegexForFieldName": "", "FieldName": "malicious", "RegexForFieldValue": "", "ResultsToSearch": {"val_to_search": [[]], "found_results": [], "num_of_results": 0}}]
}
Get Integration Instances
Description
Returns all integration instances for an environment.
Parameters
No parameters applicable.
Example
In this scenario, all integration instances in all environments will be
      returned.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"instances": [{"identifier": "27dee746-1857-41b7-a722-b99699b8d6c8", "integrationIdentifier": "Tools", "environmentIdentifier": "Default", "instanceName": "Tools_1", "instanceDescription": "test", "isConfigured": true, "isRemote": false, "isSystemDefault": false},{...........}]
}
Delay Playbook V2
Description
Temporarily stops a playbook from completing for a specified period of
      time.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Seconds
Integer
0
No
Specify amount of seconds to delay a playbook.
Minutes
Integer
1
No
Specify amount of minutes to delay a playbook.
Hours
Integer
0
No
Specify amount of hours to delay a playbook.
Days
Integer
0
No
Specify amount of days to delay a playbook.
Cron Expression
String
N/A
No
Determines when the playbook should proceed using a cron expression.
            Will be prioritized over the other parameters.
Example
In this scenario, we're delaying the playbook for 12 and a half
      hours.
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
Get Original Alert Json
Description
Returns JSON result of the original alert (raw data).
Parameters
No Parameters Applicable
Example
In this scenario, the original raw json of the alert is returned.
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"CreatorUserId": null, "Events": [{"_fields": {"BaseEventIds": "[]", "ParentEventId": -1, "deviceEventClassId": "IRC Connections", "DeviceProduct": "IPS_Product", "StartTime": "1667497096184", "EndTime": "1667497096184"}, "_rawDataFields": {"applicationProtocol": "TCP", "categoryOutcome": "blocked", "destinationAddress": "104.131.182.103", "destinationHostName": "www.ircnet.org", "destinationPort": "770", "destinationProcessName": "MrlCS.sob", "destinationUserName": "XWTTRYzNr1l@gmail.com", "deviceAddress": "0.0.0.0", "deviceEventClassId": "IRC Connections", "deviceHostName": "ckIYC2", "Field_24": "B0:E7:DF:6C:EF:71", "deviceProduct": "IPS_Product", "deviceVendor": "Vendor", "endTime": "1667497110906", "eventId": "0aa16009-57b4-41a3-91ed-81347442ca29", "managerReceiptTime": "1522058997000", "message": "Connection to IRC Server", "name": "IRC Connections", "severity": "8", "sourceAddress": "0.0.0.0", "sourceHostName": "jhon@domain.local", "startTime": "1667497110906", "sourcetype": "Connection to IRC Server"}, "Environment": null, "SourceSystemName": null, "Extensions": []}], "Environment": "Default", "SourceSystemName": "Arcsight", "TicketId": "fab1b5a1-637f-4aed-a94f-c63137307505", "Description": "IRC Connections", "DisplayId": "fab1b5a1-637f-4aed-a94f-c63137307505", "Reason": null, "Name": "IRC Connections", "DeviceVendor": "IPS", "DeviceProduct": "IPS_Product", "StartTime": 1667497110906, "EndTime": 1667497110906, "Type": 1, "Priority": -1, "RuleGenerator": "IRC Connections", "SourceGroupingIdentifier": null, "PlaybookTriggerKeywords": [], "Extensions": [], "Attachments": null, "IsTrimmed": false, "DataType": 1, "SourceType": 1, "SourceSystemUrl": null, "SourceRuleIdentifier": null
}
Get Current Time
Description
Returns the current date and time.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Datetime Format
String
%d/%m/%Y %H:%M
Yes
Specify the format of the date and time.
Example
In this scenario, we're returning a date and time value using the
      following format: %d/%m/%Y %H:%M:%S
Action results
Script result
Script result name
Value options
Example
ScriptResult
Date time value
03/11/2022 20:33:43
Update alert score
Description
Updates the alert score by the amount provided.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Input
Integer
N/A
Yes
Specify the amount to increment or decrement (negative number) by.
Example
In this scenario, we're decreasing the alert score by 20.
Action results
Script result
Script result name
Value options
Example
ScriptResult
Input Value
-20
Add Comment to entity log
Description
Adds a comment to the entity log for each entity in score in the Entity
      Explorer.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
User
Drop-down
@Administrator
Yes
Specify the user created the comment.
Comment
String
N/A
Yes
Specify the comment that will be added to the entity log.
Example
Action results
Script result
Script result name
Value options
Example
N/A
N/A
N/A
Re-Attach Playbook
Description
Removes a playbook from a case, deletes any result data in the case from
      that playbook, and re-attaches the playbook so it will run again. Requires
      installation of PostgreSQL integration, configured to the Shared
      Environment with an instance name of Google SecOps SOAR. See CSM / Support for
      additional details.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Playbook Name
Drop-down
N/A
Yes
Specify the playbook to reattach.
Example
In this scenario, we're re-attaching a playbook called
      attach_playbook_test
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
True/False/Please configure the Google SecOps SOAR instance of the
                PostgreSQL integration.
True
Lock Playbook
Description
Pauses the current playbook until all playbooks from the previous alert
      complete.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Async Action Timeout
Integers
1 Day
No
The timeout for async actions defines the total time permitted for
            this action (sums up all iterations runtime).
Async Polling Interval
Integers
1 Hour
No
Set the duration between each polling attempt during an async action
            runtime.
Example
In this scenario, we're pausing the current playbook and checking
      every 30 seconds to see if all playbooks in the previous alert in the case
      are complete.
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
True/False
True
Find First Alert
Description
Returns the identifier of the first alert in a given case.
Parameters
No parameters applicable.
Example
In this scenario, it's returning the alert identifier of the first
      alert in the case.
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Alert Identifier Value
IRC CONNECTIONS9A33308C-AC62-4A41-8F73-20529895D567
Look-A-Like Domains
Description
Compares domain entities against the list of domains defined for the
      environment. If the domains are similar the entity will be marked as
      suspicious and enriched with the matching domain.
Parameters
No parameters applicable
Example
In this scenario, we're checking if external domain entities look
      similar to the domains configured in the domains list in settings.
Action results
Script result
Script result name
Value options
Example
look_a_like_domain_found
True/False
True
JSON Result
{
"Entity" : {"EntityResult" : { "look_a_like_domains" : ["outlooks.com"]}}
}
Change Case Name
Description
Changes a case name or title.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
New Name
String
N/A
No
Specify the new name of the case.
Only If First Alert
Checkbox
Unselected
No
If selected, will only change the case's name if the action was
            executed on the first alert in the case.
Example
In this scenario, the title of a case will be changed to “Phishing -
      Suspicious Email” only if it runs in the first alert.
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
True/False
True
Spell Check String
Description
Check the input string spelling. The output shows the accuracy percentage,
      total number of words, total number of misspelled words, list of each misspelled word and
      the correction, and a corrected version of the input string.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
String
String
N/A
Yes
Specify the string that will be checked for misspellings.
Example
This example spell checks the following input string:
“Testing if this is a mispelled wodr.”.
Action Results
Script Result
Script Result Name
Value Options
Example
accuracy_percentage
Percentage value
71
JSON Result
{"input_string": "Testing if this is a mispelled wodr.", "total_words": 7, "total_misspelled_words": 2, "misspelled_words": [{"misspelled_word": "mispelled", "correction": "misspelled"}, {"misspelled_word": "wodr", "correction": "word"}], "accuracy": 71, "corrected_string": "Testing if this is a misspelled word."}
Search Text
Description
Search for the 'Search For' parameter in the input text or loop
      through the 'Search For Regex' list and find matches in the input
      text. If there's a match, the action returns
true
.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Text
String
N/A
Yes
Specify the text that will be searched.
Search For
String
N/A
No
Specify the string to search in the “text” field.
Search For Regular expression
String
N/A
No
List of regexes that will be used to search the string. Regular expression should
            be wrapped in double quotes. Supports comma delimited list.
Case Sensitive
Checkbox
N/A
No
Specify whether the search should be case sensitive.
Example
In this scenario, we're checking if the word
malicious
exists in the
Text
field value.
Action results
Script result
Script Result Name
Value options
Example
match_found
True/False
True
JSON result
{
"matches": [{"search": "malicious", "input": "This IOC is malicious.", "match": true}]
}
Set Context Value
Description
Sets a key and value in a specific context. This action is often used with
      the “Get context Value” action to retrieve the value of the
      key.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Value
String
N/A
Yes
Specify the context value.
Key
String
N/A
Yes
Specify the context key.
Scope
Drop-down
Alert
Yes
Specify context assignment scope (Alert, Case, Global).
Example
In this scenario, we're setting a context key of
      “malicious” to “yes” value.
Action results
Script result
Script Result Name
Value options
Example
ScriptResult
True/False
True
Create Siemplify task
Description
Assigns a task to a user or role. The task will be related to the case the
      action ran on.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Task Title
String
N/A
No
Specify the title of the task.
SLA (in minutes)
Integer
480
Yes
Specify the amount of time in minutes the assigned user/role has to
            respond to the task.
Task Content
String
N/A
Yes
Specify the details of the task.
Assign To
Drop-down
N/A
Yes
Specify the user or role that task will be assigned to.
Example
In this scenario, a task is created instructing Tier 3 to run a virus
      scan.
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
Assign Case To User
Description
Assigns a case to a user.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Case Id
String
N/A
Yes
Specify the case id. Use [
Case.Id
] for
            the current case.
Assign To
String
@Admin
Yes
Specify the user to assign a case to. This is the user's ID. Use
            “Get Siemplify Users” action to retrieve ID for a
            specific user.
Alert Id
String
Yes
Specify the alert id. Use [Alert.Identifier].
Example
In this scenario, we're assigning the current case to a specific
      user using their ID.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
Get Case Data
Description
Retrieves all data from a case and returns a JSON result. The result
      includes comments, entity information, insights, playbooks that ran, alert
      information and events.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Case Id
Integer
N/A
No
Specify the case Id to query. If left blank, it will use the current
            case.
Example
In this scenario, we're retrieving case details from the current
      case.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"id"
:
11111
,
"creationTimeUnixTimeInMs"
:
1770209216367
,
"modificationTimeUnixTimeInMs"
:
1770209216367
,
"createTime"
:
1770209216367
,
"updateTime"
:
1770209216367
,
"name"
:
"Access Disabled Accounts"
,
"displayName"
:
"Access Disabled Accounts"
,
"priority"
:
-1
,
"important"
:
false
,
"incident"
:
false
,
"isImportant"
:
false
,
"isIncident"
:
false
,
"startTimeUnixTimeInMs"
:
1770209216367
,
"endTimeUnixTimeInMs"
:
null
,
"assignedUser"
:
"@SOC_Analyst"
,
"assignee"
:
"@SOC_Analyst"
,
"description"
:
""
,
"isTestCase"
:
true
,
"type"
:
"Test"
,
"stage"
:
"Triage"
,
"environment"
:
"Production_Environment"
,
"status"
:
1
,
"products"
:
[
{
"displayName"
:
"Windows:AccessDisabledAccounts"
,
"alert"
:
"ACCESS_DISABLED_ACCOUNTS_A1B2C3D4E5F6G7H8I9J0"
}
],
"score"
:
0
,
"involvedSuspiciousEntity"
:
false
,
"workflowStatus"
:
"InProgress"
,
"source"
:
"Simulated"
,
"tasks"
:
[],
"incidentId"
:
""
,
"lastModifyingUserId"
:
"System"
,
"tags"
:
[
"Simulated Case"
],
"relatedAlerts"
:
[],
"alertCount"
:
1
,
"wallData"
:
[
{
"caseId"
:
11111
,
"activityKind"
:
"Action"
,
"activityDataJson"
:
"{\"ActionTriggerType\":0,\"Integration\":\"Tools\",\"ExecutingUser\":null,\"PlaybookName\":\"Security_Workflow_Test\",\"PlaybookIsInDebugMode\":true,\"Status\":5,\"ActionProvider\":\"Scripts\",\"ActionIdentifier\":\"Tools_Get_Case_Data_1\",\"ActionName\":\"Tools_Get Case Data\",\"ActionResult\":\"Action started\",\"AlertIdentifiers\":[],\"TargetEntites\":[],\"Parameters\":{\"Case Id\":\"\",\"Fields to Return\":\"\",\"Nested Keys Delimiter\":\".\"},\"LoopIteration\":null,\"LoopName\":null,\"Properties\":{},\"CreatorUserId\":null,\"CreatorFullName\":null,\"Id\":222222,\"Type\":3,\"CaseId\":11111,\"IsFavorite\":false,\"ModificationTimeUnixTimeInMs\":1770209218163,\"CreationTimeUnixTimeInMs\":1770209218163,\"AlertIdentifier\":\"ACCESS_DISABLED_ACCOUNTS_A1B2C3D4E5F6G7H8I9J0\"}"
,
"favorite"
:
false
,
"name"
:
"projects/internal-project/locations/global/instances/default/cases/11111/caseWallRecords/ActionResults222222"
,
"id"
:
"ActionResults222222"
,
"activityId"
:
222222
,
"activityType"
:
"CaseAction"
,
"createTime"
:
1770209218163
,
"updateTime"
:
1770209218163
,
"alertIdentifier"
:
"ACCESS_DISABLED_ACCOUNTS_A1B2C3D4E5F6G7H8I9J0"
}
],
"entityCards"
:
[],
"entities"
:
[],
"isOverflowCase"
:
false
,
"overflowCase"
:
false
,
"isManualCase"
:
false
,
"manualCase"
:
false
,
"slaExpirationUnixTime"
:
null
,
"slaCriticalExpirationUnixTime"
:
null
,
"stageSlaExpirationUnixTimeInMs"
:
null
,
"stageSlaCriticalExpirationUnixTimeInMs"
:
null
,
"canOpenIncident"
:
false
,
"sla"
:
{
"slaExpirationTime"
:
-1
,
"criticalExpirationTime"
:
-1
,
"expirationStatus"
:
"NoSla"
,
"remainingTimeSinceLastPause"
:
-1
},
"stageSla"
:
{
"slaExpirationTime"
:
-1
,
"criticalExpirationTime"
:
-1
,
"expirationStatus"
:
"NoSla"
,
"remainingTimeSinceLastPause"
:
-1
},
"alertSla"
:
{
"slaExpirationTime"
:
-1
,
"criticalExpirationTime"
:
-1
,
"expirationStatus"
:
"NoSla"
,
"remainingTimeSinceLastPause"
:
-1
},
"alerts"
:
[
{
"id"
:
333333
,
"creationTimeUnixTimeInMs"
:
0
,
"modificationTimeUnixTimeInMs"
:
0
,
"identifier"
:
"ACCESS_DISABLED_ACCOUNTS_A1B2C3D4E5F6G7H8I9J0"
,
"status"
:
"Open"
,
"name"
:
"ACCESS DISABLED ACCOUNTS"
,
"priority"
:
"Informative"
,
"workflowsStatus"
:
1
,
"slaExpirationUnixTime"
:
null
,
"slaCriticalExpirationUnixTime"
:
null
,
"startTime"
:
1768587188938
,
"endTime"
:
1768587188938
,
"alertGroupIdentifier"
:
"Access_Disabled_Accounts_Group_Z1Y2X3"
,
"eventsCount"
:
1
,
"title"
:
"ACCESS DISABLED ACCOUNTS"
,
"ruleGenerator"
:
"Access Disabled Accounts"
,
"deviceProduct"
:
"Windows:AccessDisabledAccounts"
,
"deviceVendor"
:
"Microsoft"
,
"caseId"
:
11111
,
"playbookAttached"
:
null
,
"playbookRunCount"
:
1
,
"isManualAlert"
:
false
,
"sla"
:
{
"slaExpirationTime"
:
-1
,
"criticalExpirationTime"
:
-1
,
"expirationStatus"
:
"NoSla"
,
"remainingTimeSinceLastPause"
:
-1
},
"fieldsGroups"
:
[],
"sourceUrl"
:
null
,
"sourceRuleUrl"
:
null
,
"siemAlertId"
:
null
,
"additionalProperties"
:
"{\"Name\":\"Access Disabled Accounts\",\"Type\":\"ALERT\",\"EndTime\":\"1768587279109\",\"Alert_Id\":\"ID-99999-AAAAA\",\"TicketId\":\"TICKET-88888-BBBBB\",\"DisplayId\":\"DISPLAY-77777-CCCCC\",\"StartTime\":\"1768587279109\",\"IsArtifact\":\"False\",\"IsEnriched\":\"False\",\"IsTestCase\":\"True\",\"Description\":\"Access Disabled Accounts\",\"Environment\":\"Production_Environment\",\"IsSuspicious\":\"False\",\"IsVulnerable\":\"False\",\"DataAccessScope\":null,\"IsInternalAsset\":\"False\",\"AlertBaseEventIds\":\"EVENT-ID-66666-DDDDD\",\"EstimatedStartTime\":\"1768587279109\"}"
,
"ticketId"
:
"TICKET-UNIQUE-UUID-VALUE"
,
"closureDetails"
:
{
"reason"
:
"Unknown"
},
"productFamilies"
:
[],
"entityCards"
:
[],
"securityEventCards"
:
[
{
"fields"
:
[
{
"order"
:
0
,
"groupName"
:
"Highlighted Fields"
,
"isIntegration"
:
false
,
"isHighlight"
:
true
,
"items"
:
[
{
"originalName"
:
"categoryOutcome"
,
"name"
:
"CategoryOutcome"
,
"value"
:
"Allowed"
},
{
"originalName"
:
"destinationPort"
,
"name"
:
"DestinationPort"
,
"value"
:
"633"
},
{
"originalName"
:
"deviceProduct"
,
"name"
:
"DeviceProduct"
,
"value"
:
"Windows:AccessDisabledAccounts"
},
{
"originalName"
:
"deviceVendor"
,
"name"
:
"DeviceVendor"
,
"value"
:
"Windows"
},
{
"originalName"
:
"endTime"
,
"name"
:
"End Time"
,
"value"
:
"1768587279109"
},
{
"originalName"
:
"message"
,
"name"
:
"Message"
,
"value"
:
"Access Disabled Accounts"
},
{
"originalName"
:
"name"
,
"name"
:
"Name"
,
"value"
:
"Access Disabled Accounts"
},
{
"originalName"
:
"sourceAddress"
,
"name"
:
"Source Address"
,
"value"
:
"192.168.10.25"
},
{
"originalName"
:
"sourceHostName"
,
"name"
:
"Source Host Name"
,
"value"
:
"workstation-01.internal.corp"
},
{
"originalName"
:
"sourceUserName"
,
"name"
:
"Source User Name"
,
"value"
:
"user_account@internal"
},
{
"originalName"
:
"startTime"
,
"name"
:
"Start Time"
,
"value"
:
"1768587279109"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Application"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"applicationProtocol"
,
"name"
:
"Application Protocol"
,
"value"
:
"TCP"
}
]
},
{
"order"
:
0
,
"groupName"
:
"System"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"categoryOutcome"
,
"name"
:
"CategoryOutcome"
,
"value"
:
"Allowed"
},
{
"originalName"
:
"destinationPort"
,
"name"
:
"DestinationPort"
,
"value"
:
"633"
},
{
"originalName"
:
"deviceProduct"
,
"name"
:
"DeviceProduct"
,
"value"
:
"Windows:AccessDisabledAccounts"
},
{
"originalName"
:
"deviceVendor"
,
"name"
:
"DeviceVendor"
,
"value"
:
"Windows"
},
{
"originalName"
:
"name"
,
"name"
:
"Name"
,
"value"
:
"Access Disabled Accounts"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Destination"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"destinationNtDomain"
,
"name"
:
"Destination Domain"
,
"value"
:
""
}
]
},
{
"order"
:
0
,
"groupName"
:
"Device"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"deviceAddress"
,
"name"
:
"Device Address"
,
"value"
:
"10.10.20.50"
},
{
"originalName"
:
"deviceHostName"
,
"name"
:
"Device Host Name"
,
"value"
:
"SEC-SVR-04"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Event"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"deviceEventClassId"
,
"name"
:
"Device Event Class ID"
,
"value"
:
"Access Disabled Accounts"
},
{
"originalName"
:
"message"
,
"name"
:
"Message"
,
"value"
:
"Access Disabled Accounts"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Default"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"Field_29"
,
"name"
:
"Field_29"
,
"value"
:
"REDACTED_VAL"
},
{
"originalName"
:
"sourcetype"
,
"name"
:
"sourcetype"
,
"value"
:
"Access Disabled Accounts"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Time"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"endTime"
,
"name"
:
"End Time"
,
"value"
:
"1768587279109"
},
{
"originalName"
:
"managerReceiptTime"
,
"name"
:
"Manager Receipt Time"
,
"value"
:
"1522058625000"
},
{
"originalName"
:
"startTime"
,
"name"
:
"Start Time"
,
"value"
:
"1768587279109"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Threat"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"severity"
,
"name"
:
"Severity"
,
"value"
:
"9"
}
]
},
{
"order"
:
0
,
"groupName"
:
"Source"
,
"isIntegration"
:
false
,
"isHighlight"
:
false
,
"items"
:
[
{
"originalName"
:
"sourceAddress"
,
"name"
:
"Source Address"
,
"value"
:
"192.168.10.25"
},
{
"originalName"
:
"sourceHostName"
,
"name"
:
"Source Host Name"
,
"value"
:
"workstation-01.internal.corp"
},
{
"originalName"
:
"sourceUserName"
,
"name"
:
"Source User Name"
,
"value"
:
"user_account@internal"
}
]
}
],
"identifier"
:
"UID-AAA-BBB-CCC-DDD"
,
"caseId"
:
11111
,
"alertIdentifier"
:
"ACCESS_DISABLED_ACCOUNTS_A1B2C3D4E5F6G7H8I9J0"
,
"name"
:
"Access Disabled Accounts"
,
"product"
:
"Windows:AccessDisabledAccounts"
,
"port"
:
null
,
"sourceSystemName"
:
"Security_Information_Service"
,
"outcome"
:
null
,
"time"
:
1768587188938
,
"type"
:
"Access Disabled Accounts"
,
"artifactEntities"
:
[]
}
],
"involvedRelations"
:
[]
}
]
}
Wait For Playbook to Complete
Description
Pauses the current playbook until another playbook or block, that is
      running on the same alert, completes.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Playbook Name
String
N/A
No
Specify the name of the block or playbook that you want to complete
            first.
Example
In this scenario, we're pausing the current playbook until the
      “investigation block” that’s running on the same alert
      is complete.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
Convert Into Simulated Case
Description
Converts a case into a simulated case that can be loaded into the platform.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Push to Simulated Cases
Checkbox
Unselected
No
If selected, the case is added to the available simulated cases list.
Save JSON as Case Wall File
Checkbox
Selected
No
If selected, a JSON file which represents the case is saved to the case wall to be downloaded.
Override Alert Name
String
Empty
No
Specify a new alert name to be used. This parameter supersedes the
Full Path Name
parameter if selected.
Full name of path
Checkbox
Unselected
No
If selected, use the alert name as
source_product_eventtype
—for example,
QRadar_WinEventLog:Security_Remote fail login
.
     This parameter is ignored if
Override Alert Name
is set.
Example
In this example, a case is converted to a simulated case using "Risky Sign On" as the alert name, which will be displayed as one of the available simulated cases in the homescreen.
Action results
Script result
Script result name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
  "cases": [
    {
      "CreatorUserId": null,
      "Events": [
        {
          "_fields": {
            "BaseEventIds": "[]",
            "ParentEventId": -1,
            "DeviceProduct": "WinEventLog:Security",
            "StartTime": "1689266169689",
            "EndTime": "1689266169689"
          },
          "_rawDataFields": {
            "sourcetype": "Failed login",
            "starttime": "1689702001439",
            "endtime": "1689702001439"
          },
          "Environment": null,
          "SourceSystemName": null,
          "Extensions": []
        }
      ],
      "Environment": "default",
      "SourceSystemName": "QRadar",
      "TicketId": "de2e3913-e4d8-4060-ae2b-1c81ee64ba47",
      "Description": "This case created by SPLUNK query
",
      "DisplayId": "de2e3913-e4d8-4060-ae2b-1c81ee64ba47",
      "Reason": null,
      "Name": "Risky Sign On",
      "DeviceVendor": "WIN-24TBDNRMSVB",
      "DeviceProduct": "WinEventLog:Security",
      "StartTime": 1689702001439,
      "EndTime": 1689702001439,
      "Type": 1,
      "Priority": -1,
      "RuleGenerator": "Remote Failed login",
      "SourceGroupingIdentifier": null,
      "PlaybookTriggerKeywords": [],
      "Extensions": [
        {
          "Key": "KeyName",
          "Value": "TCS"
        }
      ],
      "Attachments": null,
      "IsTrimmed": false,
      "DataType": 1,
      "SourceType": 1,
      "SourceSystemUrl": null,
      "SourceRuleIdentifier": null,
      "SiemAlertId": null,
      "__CorrelationId": "7efd38feaea247ad9f5ea8d907e4387c"
    }
  ]
}
Jobs
Close Cases Based On Search
Description
This job will close all cases based on a search query. The Search Payload
      is the payload used in the 'CaseSearchEverything' API call. To get
      an example of this value, go to Search in the UI and open Developer Tools.
      Search for the cases to delete. Look for the
      "CaseSearchEverything" api call in DevTools. Copy the JSON
      payload of the POST request and paste in "Search Payload". The
      Close Reason should be 0 or 1. 0 = malicious 1 = not malicious. Root Cause
      comes from Settings -> Case Data -> Case Close Root Cause.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Search Payload
JSON
N/A
No
Specify JSON payload to search. Example:
            {"tags":[],"ruleGenerator":[],"caseSource":[],"stage":[],"environments":[],"assignedUsers":[],"products":[],"ports":[],"categoryOutcomes":[],"status":[],"caseIds":[],"incident":[],"importance":[],"priorities":[],"pageSize":50,"isCaseClosed":false,"title":"","startTime":"2023-01-22T00:00:00.000Z","endTime":"2023-01-22T23:59:59.999Z","requestedPage":0,"timeRangeFilter":1}
Close Comment
String
N/A
Yes
Specify a close comment.
Close Reason
String
N/A
Yes
Specify the closure reason. 0 = malicious, 1 = not malicious
Root Cause
Integer
N/A
Yes
Specify the root cause. Root Cause comes from
Settings
>
Case Data
>
Case Close Root Cause
.
Google SecOps SOAR Username
String
N/A
Yes
Specify Google SecOps SOAR username.
Google SecOps SOAR Password
Password
N/A
Yes
Specify Google SecOps SOAR password.
Need more help?
Get answers from Community members and Google SecOps professionals.
