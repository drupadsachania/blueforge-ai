# Functions

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace-and-integrations/power-ups/functions/  
**Scraped:** 2026-03-05T09:37:00.178109Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Functions
Supported in:
Google secops
SOAR
Overview
A set of math and data manipulation actions to power up playbook capabilities.
Actions
Calculate Timestamp
Description
Finds a new point in time by moving forward or backward from a specified
starting time.
This action doesn't run on Google SecOps entities.
Due to platform limitations, output timestamps in the format
YYYY-MM-DDThh:mm:ss
are automatically converted to the local
format
MM/DD/YYYY hh:mm:ss
when used as a placeholder.
To maintain the correct
YYYY-MM-DDThh:mm:ss
format when
referencing the output in subsequent actions, the placeholder must explicitly
include the
dateFormat
option:
[Functions_Calculate Timestamp_1.JsonResult| "calculated_timestamps.timestamp+30M" | dateFormat("YYYY-MM-DDThh:mm:ss")]
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Input Type
DDL
Current Time
No
The baseline
      time for the timestamp offset calculation.
The possible values are as follows:
Current Time
Alert Creation Time
Case Creation Time
Custom Timestamp
Custom Timestamp
String
N/A
No
The specific date and time value that the
      action uses as its starting point when
Input Type
is set to
Custom Timestamp
.
Custom Timestamp Format
String
%Y-%m-%dT%H:%M:%S%z
No
The format of the
Custom Timestamp
when
Input Type
is set to
Custom Timestamp
.
Timestamp Delta
CSV
+30M,-30M
No
A comma-separated list of time offsets that
      dictates the calculated time change, requiring a supported unit
      (
m
- months,
d
- days,
H
- hours,
M
- minutes,
S
- seconds) and an operator
      (
+
for future,
-
for past) for each
      independently processed entry.
For example:
+30M, -30M, +1d, -24H
.
Output Timestamp Format
String
%Y-%m-%dT%H:%M:%S%z
No
A specified structure for the resulting
      calculated timestamp.
If no value is provided, the action defaults to epoch time.
Action Results
JSON Result
{
   "original_timestamp": "",
   "calculated_timestamps": {
       "timestamp+30M": "",
       "timestamp-30M": ""
   }
}
Convert Time Format
Description
Converts a datetime value from one format to another.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Input
String
N/A
Yes
Specify the input datetime value that will be converted.
From Format
String
N/A
Yes
Specify the datetime format the input string is in.
https://strftime.org
To Format
String
YYYY/MM/DD
Yes
Specify the desired time format of the output. Use arrow time format.
        https://arrow.readthedocs.io/en/stable/#supported-tokens
Time Delta In Seconds
Integer
0
Yes
Specify the number of seconds you want to shift the output to. Use
        positive value for future time/date and negative value for the past.
Timezone
String
N/A
No
Specify the output timezone.
Example
In this scenario, a datetime input of 11/23/2002 07:23:09 with an arrow time
  format of MM/DD/YYYY HH:mm:ss is converted to a time only, going back 5
  seconds and using UTC timezone.
Action Configurations
Parameter
Type
Entities
All entities
Input
11/23/2002 07:23:09
From Format
MM/DD/YYYY HH:mm:ss
To Format
HH:mm:ss
Time Delta In Seconds
-5
Timezone
EST
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Time Result
07:23:04
Create Thumbnail
Description
Converts a Base64 thumbnail of an image.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Base64 Image
String
N/A
No
Specify the Base64 string of the image.
Thumbnail Size
String
250,250
Yes
Specify the size of the thumbnail comma separated (W,L).
Input JSON
JSON
N/A
No
Specify the JSON input. Example: {“image” :”<base64
        of image>”}
Image Key Path
String
N/A
No
If using Input JSON, specify the key path for the image field.
Example
In this scenario we are creating a 500x500 thumbnail from a Base64 input.
Action Configurations
Parameter
Value
Entities
All entities
Base64 Image
iVBORWOKGgoAAAANSUhEUgAAAIgAAAH3CAYAAABnXCF6AAABXGIDQ1BJQ0MgUHJvZmIsZQAAK]FtkD9LQnEUhh9Nkf5ADhEVDQ4tgUmoBBFEdiMRCkyLr016NRXUflyNaGto6gNESOtBLc251mcoCpqDaA5cKm7naqVWBw7w8s5h5cDTq+uVNEFIMpVM×Gd96U2NnZeZ1y46cP]jGSUVCQeX5IRvrWz6vc4bL2dsG/NDi30qZvDEyOSemMBO//zndUTyZbMUTfpacMZVbBERa071aV/zQfCA6aEEj620d fkS5vTTb5uzKwmNOE7Ya+R1zPCT8L+dJufa+NSccf4ymCn78uW15Ki|9KiL]Mkhk80QpQQYYJor]CQP/2/F27saWyi2MOkQ|48VbkREUdRICsco4×BAL9wkEnpkP3v339seWoQpheg66zIpSVTTIMd7e8sQ VOTSHVvt]N/ee7jrqrshUKNrm3Buj3pdB884fDxY1|vNsj705f4jXNc/AQraYUmHWN3rAAAAmVYSWZNTOAqAAAACAABIZkABAAAAAEAAAAAAAAAAAADKOYABWAAABIAAABEOAIABAAAAAEAAAJY
OAMABAAAAAAAAHAAAAEFTQO|JAAAAU2NyZwVuc2hvdBNik6MAAAHWAVRYdFhNTDpib20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9|mFkb2|10m5zOm1 IdGEvliB40nhtcHR rPSJYTVAgQ29ZSA2LjAuMCI+CiAgIDxyZ
Thumbnail Size
500x500
Input JSON
Blank
Image Key Path
Blank
Action Results
JSON Result
{
"Thumbnail" : "<base 64 string>"
}
Detect Hash Type
Description
This action detects the most likely hash type of entities. Supported types are
  SHA256, MD5, SHA1, SHA-512.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Hashes
String
N/A
Yes
Specify hash value. Supports comma separated list.
Example
In this scenario, we’re identifying hash types for two hashes resulting
  in MD5 and SHA256.
Action Configurations
Parameter
Value
Entities
All entities
Hashes
b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7aceZefcde9,ed076287532e86365e841e92bfc50d8c
Action Results
Script Result
Script Result Name
Value options
Example
IsSuccess
True/False
True
JSON Result
[{
"Hash": "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9", "HashType": "SHA-256"}, {"Hash": "ed076287532e86365e841e92bfc50d8c", "HashType": "MD5"
}]
Detect IP Type
Description
Checks if an IP is an IPv4 or IPv6 address. IP Address entities will be
  enriched with IPType field.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
IP Addresses
String
N/A
Yes
Specify IP value. Supports comma separated list.
Example
In this scenario, we’re checking two different IP Addresses to identify
  their type.
Action Configurations
Parameter
Value
Entities
All entities
IP Addresses
2001:0db8:85a3:0000:0000:8a2e:0370:7334,
0.0.0.0
Action Results
Script Result
Script Result Name
Value options
Example
IsSuccess
True/False
True
JSON Result
[{
"Address": "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPType": "IPV6"}, {"Address": "0.0.0.0", "IPType": "IPV4"}
}]
IP to Integer
Description
Converts an IP Address or a list of IP addresses to integers.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
IP Addresses
String
N/A
Yes
Specify list of IP addresses separated by comma to be converted to
        integers.
Example
In this scenario, IP addresses of 1.1.1.1 and 2.2.2.2 are converted to their
  integer form.
Action Configurations
Parameter
Value
Entities
All entities
IP Addresses
1.1.1.1,2.2.2.2
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Integer values
16843009,33686018
JSON Result
{
"1.1.1.1" : 16843009, 
"2.2.2.2" : 33686018
}
Math Arithmetic
Description
A set of built in math operators:
Plus - returns a result for the sum of 2 arguments
Sub - returns a result for 1 argument minus the other
Multi - returns a result for 1 argument multiplied by the other
Div - returns a result for 1 argument divided by the other
Mod - returns the result of the percentage between 2 arguments
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Function
Dropdown
Plus
Yes
Specify the function you would like to run on two given arguments.
Arg 2
Integer
N/A
Yes
Specify the second argument
Arg 1
Integer
N/A
Yes
Specify the first argument
Example 1: Plus
In this scenario, 200 + 100 resulting in 300.
Action Configurations
Parameter
Value
Entities
All entities
Function
Plus
Arg 2
100
Arg 1
200
Example 2: Sub
In this scenario, 1000 - 300 resulting in 700.
Action Configurations
Parameter
Value
Entities
All entities
Function
Sub
Arg 2
300
Arg 1
1000
Example 3: Multi
In this scenario, 30 x 20 resulting in 600.
Action Configurations
Parameter
Value
Entities
All entities
Function
Multi
Arg 2
20
Arg 1
30
Example 4: Div
In this scenario, 500 / 5 resulting in 100.
Action Configurations
Parameter
Value
Entities
All entities
Function
Div
Arg 2
5
Arg 1
500
Example 5: Mod
In this scenario , 100 % 23 resulting in 8.
Action Configurations
Parameter
Value
Entities
All entities
Function
Mod
Arg 2
23
Arg 1
100
Action Result
Script Result
Script Result Name
Value options
Example
ScriptResult
Calculated result
300
Math Functions
Description
A set of built-in Python functions:
Abs - returns the absolute value of a number
Float - returns a floating point number
Display - converts the number to include commas where needed
Hex - converts a number into a hexadecimal value
Int - returns an integer number
Max - returns the largest item in an iterable
Min - returns the smallest item in an iterable
Round - rounds a number
Sort - returns a sorted number
Sum - sums the items of an iterator
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Function
Dropdown
Max
Yes
Specify the Math function you would like to run on the numbers.
Numbers
Integer
N/A
Yes
Specify the numbers you would like to run the math function on separated
        by comma.
Example 1: Max
In this scenario, the max value out of the numbers: 13.5, -90, 556, 11.32
  results in 556.
Action Configurations
Parameter
Value
Entities
All entities
Function
Max
Numbers
13.5,-90,566,11.32
Example 2: Min
In this scenario, the min value out of the numbers: 13.5, -90, 556, 11.32
  results in -90.
Action Configurations
Parameter
Value
Entities
All entities
Function
Min
Numbers
13.5,-90,566,11.32
Example 3: Round
In this scenario, 57.63 is rounded and resulting in 58.
Action Configurations
Parameter
Value
Entities
All entities
Function
Round
Numbers
57.63
Example 4: Sort
In this scenario, numbers [13.5, -90.0, 556.0, 11.32] are sorted in ascending
  order to [-90.0, 11.32, 13.5, 556.0].
Action Configurations
Parameter
Value
Entities
All entities
Function
Sort
Numbers
13.5,-90,566,11.32
Example 5: Sum
In this scenario, the sum of the following numbers [10, 20, 30, 40, 50] is
  150.
Action Configurations
Parameter
Value
Entities
All entities
Function
Sum
Numbers
10, 20, 30, 40, 50
Example 6: Float
In this scenario, numbers [100,200] are converted to float values of [100.0,
  200.0].
Action Configurations
Parameter
Value
Entities
All entities
Function
Float
Numbers
100,200
Example 6: Hex
In this scenario, numbers [100,200] are converted to hexadecimal values of
  ['0x64', '0xc8'].
Action Configurations
Parameter
Value
Entities
All entities
Function
Hex
Numbers
100,200
Example 7: Int
In this scenario, a float value of 100.23 is converted to an inter of 100.
Action Configurations
Parameter
Value
Entities
All entities
Function
Int
Numbers
100.23
Example 8: Abs
In this scenario, a negative integer of -53 is converted to an absolute value
  of 53.
Action Configurations
Parameter
Value
Entities
All entities
Function
Abs
Numbers
-53
Example 9: Display
In this scenario, a value of 10000 is converted to include commas resulting in
  a value of 10,000.
Action Configurations
Parameter
Value
Entities
All entities
Function
Display
Numbers
10000
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Calculated result
-90
Run JSONPath Query
Description
Runs a JSONPath Query on a given json and extracts values according to the
  expression.
View
https://github.com/h2non/jsonpath-ng
for more information on JSONPath.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
JSON
Dropdown
JSON
Yes
Specify the JSON input.
JSONPath Expression
String
N/A
Yes
JSON path expressions always refer to a JSON structure in the same way
        as XPath expressions are used in combination with an XML document.
Example
In this scenario, company name is extracted from the json sample input.
Action Configurations
Parameter
Value
Entities
All entities
JSON
JSON
Editor
{
  "company": {
    "name": "Cyber Secure",
    "employees": 1000,
    "founded": "2005",
    "headquarters": {
      "city": "San Francisco",
      "state": "CA",
      "country": "USA"
    },
    "security": {
      "firewall": true,
      "vpn": true,
      "intrusion_detection": true,
      "encryption": true,
      "two_factor_authentication": true
    }
  },
  "products": [
    {
      "name": "CyberShield",
      "type": "firewall",
      "price": 499,
      "description": "A state-of-the-art firewall for maximum protection against cyber attacks."
    },
    {
      "name": "SecureVPN",
      "type": "VPN",
      "price": 99,

      "description": "A fast and secure VPN service for safe browsing and online privacy."
    },
    {
      "name": "IntrusionAlert",
      "type": "intrusion detection",
      "price": 299,
      "description": "An advanced intrusion detection system that monitors your network and alerts you to potential threats."
    }
  ]
}
JSONPath Expression
$.company.name
Action Results
JSON Result
{
"matches" : {"0" : "Cyber Secure"}
}
SanitizeHTML
Description
Given a fragment of HTML, this action will parse it according to the HTML5
  parsing algorithm and sanitize any disallowed tags or attributes. This
  algorithm also handles wrong syntax such as unclosed and (some) misnested
  tags.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Tags
String
N/A
No
Tags is the allowed set of HTML tags. Comma separated list. HTML tags
        not in this list will be escaped or stripped.
Attributes
String
{‘a’ : [‘href’, ‘title’],
        ‘abbr’: [‘title’]}
No
Attributes lets you specify which attributes are allowed. Value should
        be a comma separated list
Styles
String
N/A
No
If you allow the style attribute, specify the allowed style set, for
        example color and background-color. Value should be comma separated.
Allow All Attributes
Checkbox
Unchecked
No
Set true to allow all attributes
Input HTML
String
N/A
Yes
Specify the HTML fragment that will be sanitized.
Example
In this scenario, the Input HTML contains a tag not listed in the Tags section
  resulting in a sanitized output of
  “<script>evil()</script>” .
Action Configurations
Parameter
Value
Entities
All entities
Tags
a,abbr,acronym,b,blockquote,code,em,i,li,ol,strong,ul,table,tr,td,th,h1,h2,h3,body,tbody,thead,div,footer,head,header,html,img,option,p,section,span,strong,svg
Attributes
Blank
Styles
Blank
Allow All Attributes
Unchecked
Input HTML
<script>evil()<</script>
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Sanitized Result
<script>evil()</script>”
String Functions
Description
Includes basic Pythonic string functions:
Lower: Converts a string into lower case.
Upper: Converts a string into upper case.
Count: Returns the number of times a specified value occurs in a string.
Find: Searches the string for a specified value and returns the position of
  where it was found.
IsAlpha: Returns "True" if all characters in the string are in the
  alphabet.
IsDigit: Returns "True" if all characters in the string are digits.
Replace: Returns a string where a specified value is replaced with a specified
  value.
Strip: Returns a trimmed version of the string.
Title: Converts the first character of each word to uppercase.
Regex Replace: Replaces a regular expression match
JSON Serialize: converts a json object to a serialized string.
Regex: Find a match based on regular expression.
Split: Splits the input string into a list using Param 1 as the separator.
  Defaults to comma.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Param2
String
N/A
No
Specify the second parameter.
Param1
String
N/A
No
Specify the first parameter.
Input
String
N/A
Yes
Specify the input for the function.
Function
Dropdown
Lower
Yes
Specify the function you want to run.
Example 1: Lower
In this scenario, input “SAMPLE INPUT” is converted to
  “sample input”.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
SAMPLE INPUT
Function
Lower
Example 2: Upper
In this scenario, input “sample input” is converted to
  “SAMPLE INPUT”.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
sample input
Function
Upper
Example 3: Count
In this scenario, it's counting the number of times the word
  “sample” occurs in the input string, which results in 2. Note,
  param value is case sensitive.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
sample
Input
sample sentence containing sample information.
Function
Count
Example 4: Find
In this scenario, it’s finding the index where the word
  “containing” starts in the input string resulting in a value of
  13.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
containing
Input
sample sentence containing sample information.
Function
Find
Example 5: isAlpha
In this scenario, it’s checking if all characters in the input string
  are alphanumeric, resulting in a False return value.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
%sample sentence containing sample information.
Function
isAlpha
Example 6: isDigit
In this scenario, it’s checking if all characters in the input string
  are digits, resulting in a False return value.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
100000001
Function
isDigit
Example 7: Replace
In this scenario, it’s replacing the word “information” with
  “info” resulting in an output of “sample input containing
  sample info”.
Action Configurations
Parameter
Value
Entities
All entities
Param2
info
Param1
information
Input
sample sentence containing sample information.
Function
Replace
Example 8: Strip
In this scenario, it’s removing spaces in the beginning and end of the
  input string resulting of an output of “sample input containing sample
  information”.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
sample sentence containing sample information.
Function
Strip
Example 9: Title
In this scenario, it’s converting the first character of each word in
  the input string to a capital character resulting in a output of “Sample
  Input Containing Sample Information”.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
sample sentence containing sample information.
Function
Title
Example 10: Regex Replace
In this scenario, we’re searching for “The” using regex and
  replacing it with “a”.
In this scenario, we're searching for "The" using regex and replacing it with "a".
Action Configurations
Parameter
Value
Entities
All entities
Param2
A
Param1
\bThe\b
Input
The quick brown fox jumps over the lazy dog
Function
Regex Replace
Example 11: JSON Serialize
In this scenario, it’s converting the json input to a serialized string
  resulting in a output of "{\"key\" :\"value\"}".
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
Blank
Input
{"ip" : "0.0.0.0"}
Function
JSON Serialize
Example 12: Regex
In this scenario, we’re trying to use a regex to pull the value in the
  input JSON.
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
(?<="resource":").*?(?=")
Input
{"resource":"host001"}
Function
Regex
Example 13: Split
In this scenario, input is converted to a list using comma as a delimiter
  resulting in an output of [100,200,300,400,500].
Action Configurations
Parameter
Value
Entities
All entities
Param2
Blank
Param1
,
Input
100,200,300,400,500
Function
Split
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Result value based on the function
23
Time Duration Calculator
Description
Calculates the difference between two date times.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Input DateTime 1
String
N/A
Yes
Specify the first datetime input value. Supports either strftime format
        or “now” for the current time.
Input DateTime 1 Format
String
%Y-%d-%m'T'%H:%M:%S
Yes
Specify the strftime format of “Datetime 1” string. For more
        info, visit https://strftime.org.
Input DateTime 2
String
now
Yes
Specify the second datetime input value. Supports either strftime format
        or “now” for the current time.
Input DateTime 2 Format
String
%Y-%d-%m'T'%h:%m:%s
Yes
Specify the strftime format of “Datetime 2” string. For more
        info, visit https://strftime.org.
Example
In this scenario, it calculates the difference between
  2022-13-03'T'04:13:01 and now’s date time resulting in an output
  of: 0 years, 200 days, 10 hours, 51 minutes and 20 seconds.
Action Configurations
Parameter
Value
Entities
All entities
Input DateTime 1
2022-13-03'T'04:13:01
Input DateTime 1 Format
%Y-%d-%m'T'%H:%M:%S
Input Datetime 2
now
Input DateTime 2 Format
%Y-%d-%m'T'%h:%m:%s
Action Results
Script Result
Script Result Name
Value options
Example
Seconds
Calculated time in seconds
17319080
JSON Result
{
     "years": 0, "days": 200,
     "hours": 4810, 
     "minutes": 288651, 
     "seconds": 17319080, 
     "duration": "Time between dates: 0 years, 200 days, 10 hours, 51 minutes and 20     
                       seconds"
}
XMLtoJson
Description
Converts XML formatted input to its JSON representation.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
XML
String
N/A
Yes
Specify XML to convert to JSON.
Example
In this scenario, we’re converting a sample xml string to a JSON object.
Action Configurations
Parameter
Value
Entities
All entities
xml
<threats>
    <threat>
      <name>Malware</name>
      <description>Malware is malicious software that is designed to harm computer systems, steal sensitive data, or take control of a network.</description>
      <prevention>
        <tip>Install anti-malware software and keep it up-to-date.</tip>
        <tip>Avoid clicking on suspicious links or downloading attachments from unknown sources.</tip>
        <tip>Regularly backup important data.</tip>
      </prevention>
      <mitigation>
        <tip>Disconnect the infected computer from the network to prevent further spread of the malware.</tip>
        <tip>Use anti-malware software to remove the malware.</tip>
        <tip>Restore any lost or corrupted data from backups.</tip>
      </mitigation>
    </threat>
  </threats>
  <best-practices>
    <practice>
      <name>Access Control</name>
      <description>Access control is the process of managing who has access to what information or resources within a network.</description>
      <tip>Implement strong authentication mechanisms, such as multi-factor authentication, to verify user identities.</tip>
      <tip>Use role-based access control to assign permissions based on job responsibilities.</tip>
      <tip>Monitor and audit user activity to detect any unauthorized access attempts.</tip>
    </practice>
  </best-practices>
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
"cybersecurity": {"threat": [{"name": "Malware", "description": "A type of software designed to harm computer systems.", "severity": "High", "prevention": {"software": "Antivirus", "policy": "Regular software updates and patches"}}, {"name": "Phishing", "description": "A fraudulent attempt to obtain sensitive information by impersonating a trustworthy entity.", "severity": "High", "prevention": {"software": "Firewalls and intrusion detection systems", "policy": "Limiting access to network resources to only authorized personnel"}}]}
}
Need more help?
Get answers from Community members and Google SecOps professionals.
